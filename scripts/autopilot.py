#!/usr/bin/env python3
"""Autopilot: improve the GATK config continuously until stopped.

Each iteration:
  1. sample K mutations of the current best (random_search.SPACE, ~25% of
     parameters re-drawn per candidate);
  2. screen them on SCREEN_ROUNDS in parallel, scored as the paired mean
     score difference vs the best on the same rounds;
  3. confirm the top few positive candidates on all dev rounds;
  4. if one improves the dev mean gap to #1 (and calls in <= 600 s), make it
     the new best: write configs/gatk-tuned.conf, deploy it as the live
     miner config, journal it and git-commit it.
It starts from whichever of --start configs scores best on the dev rounds.

Live state for the dashboard: data/tune/autopilot.json; events are appended
to data/tune/events.jsonl. Already-scored (config, round) pairs are reused.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/autopilot.py --start configs/gatk-tuned.conf configs/gatk-rs2-001.conf
"""
import argparse
import json
import os
import random
import signal
import subprocess
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import random_search  # noqa: E402
import tune  # noqa: E402

STATE = tune.TUNE / "autopilot.json"
LOG = tune.TUNE / "autopilot_log.jsonl"   # every screen / confirm / full check, for later analysis
CONFIRM_TOP = 3
FOCUS_OUT = tune.ROOT / "configs" / "gatk-focus.conf"

# Value ladders for one-change-at-a-time candidates (one rung up / down).
LADDERS = {
    "standard_min_confidence_threshold_for_calling": [20, 30, 40, 50, 60, 70, 80, 90, 100],
    "min_base_quality_score": [5, 10, 12, 15, 18, 20, 22, 24, 25, 26],
    "min_mapping_quality_score": [10, 20, 30, 40, 45, 50, 55, 58, 60],
    "base_quality_score_threshold": [6, 10, 15, 18, 20, 25, 30],
    # pcr_indel_model: AGGRESSIVE beat NONE/CONSERVATIVE on every round tested (chr12, chr13, pair, 3-round); not re-tested
    "phred_scaled_global_read_mismapping_rate": [20, 25, 30, 35, 40, 45, 50],
    "heterozygosity": [0.0005, 0.001, 0.002, 0.003, 0.005, 0.008],
    "min_pruning": [1, 2, 3, 4],
    "contamination_fraction_to_filter": [0.0, 0.01, 0.02, 0.05, 0.08],
    "assembly_region_padding": [50, 100, 150, 200, 300],
    "max_assembly_region_size": [200, 300, 400, 600],
    "dont_use_soft_clipped_bases": [False, True],
    "pair_hmm_gap_continuation_penalty": [5, 10, 15, 20, 25, 30],
    "min_dangling_branch_length": [2, 4, 6, 8],
    "active_probability_threshold": [0.001, 0.002, 0.005, 0.01, 0.02],
    # Indel-assembly settings, added after the first full-system check showed
    # ~90% of the lost points are indels (1 bp: 0.057, 8+ bp: 0.044 of score).
    "recover_all_dangling_branches": [False, True],
    "max_num_haplotypes_in_population": [32, 64, 128, 256],
    # max_alternate_alleles: no effect (2/3/6 identical to 10 on every round tested)
    # added 2026-10-27: only ever tried on 3 slices before, never on full rounds
    "indel_heterozygosity": [0.00001, 0.00005, 0.000125, 0.0003, 0.0005, 0.001],
    # max_reads_per_alignment_start: no effect at this coverage (25/100 identical to 50 on chr12+chr13)
    # pruning_lod_threshold / adaptive_pruning_initial_error_rate: only used with --adaptive-pruning (not whitelisted) -> no effect
    # min_assembly_region_size: no effect (25/75 identical to 50 on chr12+chr13)
}

# Screening runs on a SLICE_MB slice of each screening round (GATK time scales
# with region size, ~3x faster than the full 6-8 Mb). Only paired deltas vs the
# best on the same slices are used from them; confirmation uses full rounds.
SCREEN_BASE_ROUNDS = ["20261024T154600Z", "20261024T105800Z", "20261024T121000Z"]
SLICE_MB = 2
COOLDOWN = 3  # focus mode: a change that lost is tried last until this many later accepts


def _slice(rd):
    meta = json.loads((tune.ROUNDS / rd / "meta.json").read_text())
    chrom, span = meta["region"].split(":")
    start, end = (int(x) for x in span.split("-"))
    s = start + 1_000_000
    return f"{chrom}:{s}-{min(end, s + SLICE_MB * 1_000_000)}"


SLICES = {rd: _slice(rd) for rd in SCREEN_BASE_ROUNDS}
SCREEN_ROUNDS = [f"{rd}@slice" for rd in SCREEN_BASE_ROUNDS]


class Autopilot:
    def __init__(self, args):
        self.args = args
        self.defs = tune.param_defs()
        self.stop = False
        self.rng = random.Random(args.seed)
        # --focus-round accepts a comma list: a change must raise the mean over those rounds.
        self.dev = args.focus_round.split(",") if args.focus_round else tune.DEV_ROUNDS
        # Focus mode: test directly on one full round (fast feedback); otherwise
        # screen on slices and confirm on the 8 dev rounds.
        self.focus = bool(args.focus_round)
        # --focus-slice: screen on a SLICE_MB slice of the focus round (~3x faster)
        # and confirm each slice winner on the full focus round before accepting.
        self.focus_slice = self.focus and args.focus_slice and len(self.dev) == 1
        if self.focus_slice:
            SLICES.setdefault(args.focus_round, _slice(args.focus_round))
        self.screen = ([f"{args.focus_round}@slice"] if self.focus_slice else self.dev) if self.focus else SCREEN_ROUNDS
        prev = json.loads(STATE.read_text()) if STATE.exists() else {}
        if args.reset:  # choose a new start point among --start; keep iteration count and history
            prev = {"iteration": prev.get("iteration", 0), "history": prev.get("history", [])}
        self.state = {"status": "starting", "pid": os.getpid(), "started": tune.now(), "iteration": prev.get("iteration", 0),
                      "best": prev.get("best"), "history": prev.get("history", []), "phase": None, "batch": [],
                      "mode": args.mode}
        # Keep what the loop has learned (test counts, gains, recent losses, rejects,
        # momentum, ladder step) across restarts; --reset starts it afresh.
        for k in ("param_tests", "param_gain", "losses", "rejected", "accepts", "last_accept", "step", "prev_best_opts"):
            if k in prev:
                self.state[k] = prev[k]
        self.save()

    def save(self):
        self.state["heartbeat"] = tune.now()
        tmp = STATE.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.state, indent=2))
        os.replace(tmp, STATE)

    def event(self, kind, **kw):
        with tune.EVENTS.open("a") as fh:
            fh.write(json.dumps({"ts": tune.now(), "kind": f"autopilot_{kind}", **kw}) + "\n")

    # ---------- running replays ----------
    def results(self, chash, keys):
        """Results keyed by round key: '<round>' = full region, '<round>@slice' = SLICE_MB slice."""
        out = {}
        keys = set(keys)
        if tune.RESULTS.exists():
            for line in tune.RESULTS.read_text().splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("config_hash") != chash or not r.get("ok"):
                    continue
                rd = r.get("round")
                if r.get("subregion"):
                    key = f"{rd}@slice"
                    if key in keys and r.get("region") == SLICES.get(rd):
                        out[key] = r
                elif rd in keys:
                    out[rd] = r
        return out

    def run_many(self, items):
        """items: [(conf_path, label, round_key)] -> runs the missing ones in parallel."""
        def one(conf, label, key):
            if self.stop:
                return
            rd, _, sl = key.partition("@")
            cmd = [str(tune.PY), "scripts/score_round.py", str(tune.ROUNDS / rd), "--config", str(conf), "--label", label,
                   "--threads", "2", "--memory-gb", "5"]
            if sl:
                cmd += ["--region", SLICES[rd]]
            subprocess.run(cmd, cwd=tune.ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with ThreadPoolExecutor(self.args.workers) as ex:
            futs = [ex.submit(one, *it) for it in items]
            for f in as_completed(futs):
                f.result()
                self.refresh_batch()

    def materialise(self, opts, label):
        chash = tune.opts_hash(opts)
        conf = tune.CANDIDATES / f"{chash}.conf"
        tune.write_conf(conf, opts, f"autopilot {label} ({chash})")
        return chash, conf

    def summary(self, chash, rounds):
        have = self.results(chash, rounds)
        rs = [have[r] for r in rounds if r in have]
        mean = lambda xs: sum(xs) / len(xs) if xs else None  # noqa: E731
        return {"done": len(rs), "total": len(rounds),
                "mean_gap": mean([r["gap"] for r in rs if r.get("gap") is not None]),
                "mean_score": mean([r["score"] for r in rs]),
                "mean_rank": mean([r["rank"] for r in rs if r.get("rank")]),
                "wins": sum(1 for r in rs if r.get("rank") == 1),
                "max_calling_seconds": max((r.get("calling_seconds") or 0 for r in rs), default=None),
                "scores": {k: have[k]["score"] for k in rounds if k in have}}

    def evaluate(self, items_opts, rounds, phase):
        """items_opts: [(label, opts)] -> summaries on `rounds` (runs what's missing)."""
        self.state["phase"] = phase
        batch = []
        todo = []
        for label, opts in items_opts:
            chash, conf = self.materialise(opts, label)
            batch.append({"label": label, "hash": chash, "rounds": rounds,
                          "changes": {k: v for k, v in opts.items() if v != self.state["best"]["options"].get(k)}
                          if self.state.get("best") else {}})
            have = self.results(chash, rounds)
            todo += [(conf, label, r) for r in rounds if r not in have]
        self.state["batch"] = batch
        self.refresh_batch()
        self.run_many(todo)
        return {b["label"]: self.summary(b["hash"], rounds) for b in batch}

    def refresh_batch(self):
        best_scores = self.state["best"]["scores"] if self.state.get("best") else {}
        for b in self.state.get("batch", []):
            s = self.summary(b["hash"], b["rounds"])
            diffs = [s["scores"][r] - best_scores[r] for r in s["scores"] if r in best_scores]
            b.update(done=s["done"], total=s["total"], mean_gap=s["mean_gap"],
                     delta=sum(diffs) / len(diffs) if diffs else None)
        self.save()

    # ---------- one-change candidates, logging, full-system check ----------
    def single_changes(self, opts):
        """(param, new_value) pairs: each parameter one step up and down its ladder."""
        out = []
        for param, ladder in LADDERS.items():
            d = self.defs[param]
            cur = opts.get(param, d["default"])
            if d["type"] in ("enum", "bool"):
                out += [(param, v) for v in ladder if v != cur]
                continue
            ladder = [tune.typed(self.defs, param, v) for v in ladder]
            k = self.state.get("step", 1)
            if cur in ladder:
                i = ladder.index(cur)
                steps = [ladder[j] for j in (i - k, i + k) if 0 <= j < len(ladder)]
            else:  # between rungs: the nearest rung on each side
                lower = [v for v in ladder if v < cur]
                upper = [v for v in ladder if v > cur]
                steps = ([lower[-1]] if lower else []) + ([upper[0]] if upper else [])
            out += [(param, v) for v in steps]
        return out

    def solo_timing(self, label, opts):
        """GATK calling time of opts on its slowest dev round with nothing else running."""
        chash, conf = self.materialise(opts, label)
        have = self.results(chash, self.dev)
        if not have:
            return None
        slowest = max(have.values(), key=lambda r: r.get("calling_seconds") or 0)["round"]
        self.state["phase"] = f"timing {label} alone on {slowest}"
        self.save()
        cmd = [str(tune.PY), "scripts/score_round.py", str(tune.ROUNDS / slowest), "--config", str(conf),
               "--label", f"{label}-solo", "--threads", "2", "--memory-gb", "8", "--no-record"]
        t = time.time()
        out = subprocess.run(cmd, cwd=tune.ROOT, capture_output=True, text=True).stdout
        line = next((l for l in out.splitlines() if "Variants called" in l), "")
        try:  # "Variants called: N  (123s)"
            secs = float(line.rsplit("(", 1)[1].rstrip("s)"))
        except (IndexError, ValueError):
            secs = None
        self.log("solo_timing", label=label, round=slowest, calling_seconds=secs, wall_seconds=time.time() - t,
                 contended_seconds=have[slowest].get("calling_seconds"))
        return secs

    def breakdown(self, chash, rounds):
        """Summed per-class TP/FN/FP over full rounds (from replay records)."""
        tot = {"tp": 0, "fn": 0, "fp": 0, "class": {}}
        for r in self.results(chash, rounds).values():
            for k, c in (r.get("breakdown", {}).get("class") or {}).items():
                cls = tot["class"].setdefault(k, {"tp": 0, "fn": 0, "fp": 0})
                for x in ("tp", "fn", "fp"):
                    cls[x] += c.get(x, 0)
                    tot[x] += c.get(x, 0)
        return tot

    def full_check(self, when):
        """Whole-system look at the best config: where are the points being lost?"""
        best = self.state["best"]
        br = self.breakdown(best["hash"], self.dev)
        from utils.scoring import DIFFICULTY_WEIGHTS
        loss = []
        for k, c in br["class"].items():
            d = 2 * c["tp"] + c["fn"] + c["fp"]
            f1 = 2 * c["tp"] / d if d else 1.0
            share_fp = c["fp"] / max(1, c["fp"] + c["fn"])
            loss.append({"class": k, "weight": DIFFICULTY_WEIGHTS.get(k), "f1": f1,
                         "weighted_loss": DIFFICULTY_WEIGHTS.get(k, 0) * (1 - f1),
                         "fp": c["fp"], "fn": c["fn"], "fp_share": share_fp})
        loss.sort(key=lambda x: -x["weighted_loss"])
        verdict = ("false positives" if br["fp"] > br["fn"] else "missed variants")
        check = {"when": when, "ts": tune.now(), "best": best["label"], "mean_gap": best.get("mean_gap"),
                 "fp": br["fp"], "fn": br["fn"], "dominant_error": verdict, "by_class": loss}
        self.state["full_check"] = check
        self.log("full_check", **check)
        self.save()

    def log(self, kind, **kw):
        with LOG.open("a") as fh:
            fh.write(json.dumps({"ts": tune.now(), "kind": kind, **kw}, default=str) + "\n")

    # ---------- main loop ----------
    def accept(self, label, opts, summ, why):
        self.state["best"] = {"label": label, "options": opts, "hash": tune.opts_hash(opts), "since": tune.now(), **summ}
        out = FOCUS_OUT if self.focus else tune.BEST_OUT
        tune.write_conf(out, opts, f"GATK config tuned by scripts/autopilot.py ({label})\n"
                        f"{'focus round ' + ','.join(self.dev) if self.focus else 'dev'} mean gap to #1 {summ['mean_gap']:+.5f}, "
                        f"mean rank {summ['mean_rank']:.1f} over {len(self.dev)} rounds ({tune.now()})")
        if not self.focus:  # focus results are verified on other rounds before going live
            live = tune.REPO / "configs" / "gatk.conf"
            live.write_bytes(tune.BEST_OUT.read_bytes())
        with tune.JOURNAL.open("a") as fh:
            fh.write(json.dumps({"ts": tune.now(), "tag": "tuning", "text": f"Autopilot accepted {label}: {why}."
                                 + ("" if self.focus else " Deployed as live config.")}) + "\n")
        self.event("accept", label=label, mean_gap=summ["mean_gap"], mean_rank=summ["mean_rank"], why=why)
        changes = ", ".join(f"{k}={v}" for k, v in opts.items() if v != self.state.get("prev_best_opts", {}).get(k))
        where = ("Focus-round result: NOT deployed; verify on the other rounds first."
                 if self.focus else "Deployed as the live miner config.")
        msg = (f"Autopilot{' (focus)' if self.focus else ''}: new best config ({label})\n\n{why}\n"
               f"mean rank {summ['mean_rank']:.1f}, max calling {summ['max_calling_seconds']:.0f} s, "
               f"{len(self.dev)} round(s).\nChanges vs previous best: {changes or 'n/a'}\n{where}\n\n"
               "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
        # The dashboard polls git, so .git/index.lock can be briefly taken: retry.
        for attempt in range(10):
            add = subprocess.run(["git", "add", str(out)], cwd=tune.ROOT, capture_output=True, text=True)
            com = subprocess.run(["git", "commit", "-q", "-m", msg], cwd=tune.ROOT, capture_output=True, text=True)
            if add.returncode == 0 and com.returncode == 0:
                self.event("commit", label=label)
                break
            if "nothing to commit" in (com.stdout + com.stderr):
                break
            time.sleep(3)
        else:
            self.event("commit_failed", label=label, error=(com.stderr or add.stderr)[-300:])
        self.state["prev_best_opts"] = dict(opts)
        self.save()

    def run(self):
        self.state["status"] = "running"
        self.event("start", workers=self.args.workers)
        if not self.state.get("best"):
            starts = [(Path(p).stem, tune.parse_conf(Path(p), self.defs)) for p in self.args.start]
            summ = self.evaluate(starts, self.dev, "choosing start")
            label = max(summ, key=lambda l: summ[l]["mean_gap"] if summ[l]["mean_gap"] is not None else -9)
            opts = dict(next(o for l, o in starts if l == label))
            self.state["prev_best_opts"] = dict(opts)
            self.state["best"] = {"label": label, "options": opts, "hash": tune.opts_hash(opts), "since": tune.now(), **summ[label]}
            self.event("start_point", label=label, mean_gap=summ[label]["mean_gap"],
                       candidates={l: s["mean_gap"] for l, s in summ.items()})
            if label != Path(self.args.start[0]).stem:
                self.accept(label, opts, summ[label], f"better start point: dev gap {summ[label]['mean_gap']:+.5f}")
            self.save()

        self.full_check("start")
        while not self.stop:
            self.state["iteration"] += 1
            it = self.state["iteration"]
            best = self.state["best"]
            # make sure the best has scores on the screen slices for paired deltas
            self.evaluate([(best["label"], best["options"])], self.screen + self.dev, "scoring best")
            self.state["best"]["scores"] = self.summary(best["hash"], self.screen + self.dev)["scores"]
            cands = []
            if self.args.mode == "global":
                # Exploration: whole configs drawn at random from every ladder, to
                # find a different basin than the one single steps are stuck in.
                seen = {best["hash"]}
                while len(cands) < self.args.batch:
                    opts = dict(best["options"])
                    for p, ladder in LADDERS.items():
                        v = self.rng.choice(ladder)
                        opts[p] = tune.typed(self.defs, p, v) if self.defs[p]["type"] in ("int", "float") else v
                    h = tune.opts_hash(opts)
                    if h not in seen:
                        seen.add(h)
                        n = sum(1 for k in opts if opts[k] != best["options"].get(k))
                        cands.append((f"ap-{it:03d}-global-{len(cands):02d}", opts, "(global)", None, f"{n} changes"))
            else:
                # ONE change per candidate: each parameter one step up/down its value ladder.
                for param, new in self.single_changes(best["options"]):
                    opts = {**best["options"], param: new}
                    cands.append((f"ap-{it:03d}-{param}={new}", opts, param, best["options"].get(param), new))
            base = self.state["best"]["scores"]
            if self.focus:
                # Wave by wave (one wave = `workers` tests, ~5 min): stop at the first
                # wave that beats the best so it can be accepted immediately. Params
                # that helped before go first.
                # Order so a winner turns up early: (1) keep going in the direction of
                # the last accepted change, (2) params that helped before, (3) changes
                # that already lost recently (within COOLDOWN accepts) go last.
                gains = self.state.setdefault("param_gain", {})
                losses = self.state.setdefault("losses", {})
                accepts = self.state.get("accepts", 0)
                last = self.state.get("last_accept")

                def momentum(c):
                    if not last or c[2] != last[0]:
                        return False
                    try:
                        return (c[4] - c[3]) * (last[2] - last[1]) > 0
                    except TypeError:
                        return False

                def cooled(c):
                    k = f"{c[2]}={c[4]}"
                    return k in losses and accepts - losses[k] < COOLDOWN

                # Undoing the last accepted change is already known to lose on the full round.
                cands = [c for c in cands if not (last and c[2] == last[0] and c[4] == last[1])]
                tests = self.state.setdefault("param_tests", {})
                cands.sort(key=lambda c: (not momentum(c), tests.get(c[2], 0) > 0, cooled(c), -gains.get(c[2], 0.0), tests.get(c[2], 0)))
                w = self.args.workers
                waves = (len(cands) + w - 1) // w
                screened = {}
                self.full_ok = set()
                rejected = set(self.state.setdefault("rejected", {}).get(best["hash"], []))
                for i in range(0, len(cands), w):
                    wave = cands[i:i + w]
                    res = self.evaluate([(l, o) for l, o, *_ in wave], self.screen,
                                        f"iteration {it}: wave {i // w + 1}/{waves} ({len(wave)} single changes)")
                    screened.update(res)
                    for label, opts, param, old, new in wave:  # log each test as soon as it is done
                        tests[param] = tests.get(param, 0) + 1
                        sc = res[label]["scores"]
                        d = [sc[r] - base[r] for r in self.screen if r in sc and r in base]
                        self.log("screen", iteration=it, label=label, param=param, old=old, new=new,
                                 expected_delta=sum(d) / len(d) if len(d) == len(self.screen) else None,
                                 per_slice={r: sc.get(r) for r in self.screen})
                    if self.stop:
                        break
                    hits = [c for c in wave if tune.opts_hash(c[1]) not in rejected
                            and sum(res[c[0]]["scores"].get(r, -9) - base[r] for r in self.screen) / len(self.screen)
                            > tune.MIN_IMPROVEMENT]
                    if hits and not self.focus_slice:
                        break
                    for label, opts, param, old, new in hits:  # slice winner -> check it on the full round
                        full = self.evaluate([(label, opts)], self.dev, f"iteration {it}: confirming {label} on the full round")
                        rd = self.dev[0]
                        d = full[label]["scores"].get(rd, -9) - base[rd]
                        sk = self.screen[0]
                        self.log("slice_confirm", iteration=it, label=label, param=param, old=old, new=new,
                                 slice_delta=res[label]["scores"][sk] - base[sk], full_delta=d, accepted=d > tune.MIN_IMPROVEMENT)
                        if d > tune.MIN_IMPROVEMENT:
                            self.full_ok.add(label)
                            break
                        self.state["rejected"].setdefault(best["hash"], []).append(tune.opts_hash(opts))
                        rejected.add(tune.opts_hash(opts))
                    if self.full_ok or self.stop:
                        break
                cands = [c for c in cands if c[0] in screened]
            else:
                screened = self.evaluate([(l, o) for l, o, *_ in cands], self.screen,
                                         f"iteration {it}: screening {len(cands)} {'global samples' if self.args.mode == 'global' else 'single changes'}")
            if self.stop:
                break
            ranked = []
            for label, opts, param, old, new in cands:
                s = screened[label]
                diffs = [s["scores"][r] - base[r] for r in s["scores"] if r in base]
                expected = sum(diffs) / len(diffs) if len(diffs) == len(self.screen) else None
                if not self.focus:  # focus mode logged it per wave already
                    self.log("screen", iteration=it, label=label, param=param, old=old, new=new, expected_delta=expected,
                             per_slice={r: s["scores"].get(r) for r in self.screen})
                if expected is not None:
                    ranked.append((expected, label, opts, param, old, new))
                    if expected <= tune.MIN_IMPROVEMENT:
                        self.state.setdefault("losses", {})[f"{param}={new}"] = self.state.get("accepts", 0)
                    if expected > 0 and param != "(global)":
                        g = self.state.setdefault("param_gain", {})
                        g[param] = g.get(param, 0.0) + expected
            ranked.sort(key=lambda x: -x[0])
            # Skip candidates that already failed 8-round confirmation against this
            # best; otherwise the same cached winners are re-confirmed forever.
            rejected = set(self.state.setdefault("rejected", {}).get(best["hash"], []))
            ranked = [c for c in ranked if tune.opts_hash(c[2]) not in rejected]
            top = [c for c in ranked[:CONFIRM_TOP] if c[0] > 0]
            hist = {"iteration": it, "ts": tune.now(), "screened": len(cands),
                    "best_delta": ranked[0][0] if ranked else None, "confirmed": [c[1] for c in top]}
            self.state["history"].append(hist)
            if self.focus:
                # The candidate was scored on the full focus round itself: no
                # separate confirmation step, accept the best improvement now.
                win = next((c for c in ranked if c[0] > tune.MIN_IMPROVEMENT
                            and (not self.focus_slice or c[1] in self.full_ok)), None)
                if win:
                    summ = self.summary(tune.opts_hash(win[2]), self.dev)
                    if self.focus_slice:  # report the full-round gain, not the slice one
                        win = (summ["scores"][self.dev[0]] - best["scores"][self.dev[0]], *win[1:])
                    hist.update(winner=win[1], winner_gap=summ["mean_gap"], accepted=True)
                    self.log("confirm", iteration=it, label=win[1], param=win[3], old=win[4], new=win[5],
                             expected_delta=win[0], actual_gap_delta=win[0], mean_gap=summ["mean_gap"],
                             mean_rank=summ["mean_rank"], max_calling_seconds=summ["max_calling_seconds"],
                             per_round=summ["scores"], fp_delta=0, fn_delta=0, class_delta={}, matched_expectation=True)
                    self.accept(win[1], dict(win[2]), summ,
                                f"focus round {','.join(self.dev)}: one change {win[3]}: {win[4]} -> {win[5]}; "
                                + ", ".join(f"{r} {best['scores'][r]:.5f} -> {summ['scores'][r]:.5f}" for r in self.dev)
                                + f" (mean gap to #1 {summ['mean_gap']:+.5f})")
                    self.state["step"] = 1
                    self.state["accepts"] = self.state.get("accepts", 0) + 1
                    self.state["last_accept"] = [win[3], win[4], win[5]]
                    self.save()
                    continue
                top = []  # nothing improved: fall through to the step-widening below
            if not top and self.args.mode == "global":
                self.event("iteration", iteration=it, result="no global sample beat the best on the slices")
                self.log("iteration", iteration=it, result="global: no sample beat the best", best=best["label"])
                self.save()
                continue
            if not top:
                step = self.state.get("step", 1)
                self.event("iteration", iteration=it, result=f"no single change helped at step {step}")
                self.log("iteration", iteration=it, result=f"no positive single change (ladder step {step})",
                         best=best["label"])
                if step >= 3:
                    self.state["status"] = "converged"
                    self.save()
                    break
                self.state["step"] = step + 1  # widen: one parameter, two/three rungs away
                self.save()
                continue
            confirmed = self.evaluate([(c[1], c[2]) for c in top], self.dev,
                                      f"iteration {it}: confirming top {len(top)} on {len(self.dev)} full rounds")
            if self.stop:
                break
            base_break = self.breakdown(best["hash"], self.dev)
            for expected, label, opts, param, old, new in top:
                w = confirmed[label]
                actual = (w["mean_gap"] - best["mean_gap"]) if w["mean_gap"] is not None else None
                br = self.breakdown(tune.opts_hash(opts), self.dev)
                self.log("confirm", iteration=it, label=label, param=param, old=old, new=new,
                         expected_delta=expected, actual_gap_delta=actual, mean_gap=w["mean_gap"],
                         mean_rank=w["mean_rank"], max_calling_seconds=w["max_calling_seconds"],
                         per_round={r: w["scores"].get(r) for r in self.dev},
                         fp_delta=br["fp"] - base_break["fp"], fn_delta=br["fn"] - base_break["fn"],
                         class_delta={k: {x: br["class"][k][x] - base_break["class"][k][x] for x in ("fp", "fn")}
                                      for k in br["class"]},
                         matched_expectation=None if actual is None else (actual > 0) == (expected > 0))
            winner = max(top, key=lambda c: confirmed[c[1]]["mean_gap"] if confirmed[c[1]]["mean_gap"] is not None else -9)
            w = confirmed[winner[1]]
            ok = (w["done"] == len(self.dev) and w["mean_gap"] is not None
                  and w["mean_gap"] > best["mean_gap"] + tune.MIN_IMPROVEMENT)
            if ok and (w["max_calling_seconds"] or 0) > tune.MAX_CALLING_SECONDS:
                # Timings above come from ~10 runs sharing 12 cores (~2x slower than a
                # validator job, which gets its own cores). Re-time the slowest round alone.
                solo = self.solo_timing(winner[1], dict(winner[2]))
                w["solo_calling_seconds"] = solo
                ok = solo is not None and solo <= tune.MAX_CALLING_SECONDS
                if not ok:
                    self.log("iteration", iteration=it, result=f"{winner[1]} better but too slow alone ({solo}s)")
            hist.update(winner=winner[1], winner_gap=w["mean_gap"], accepted=ok)
            if ok:
                self.accept(winner[1], dict(winner[2]), w,
                            f"one change {winner[3]}: {winner[4]} -> {winner[5]}; "
                            f"dev mean gap {best['mean_gap']:+.5f} -> {w['mean_gap']:+.5f} "
                            f"(screen expected {winner[0]:+.5f})")
                self.state["step"] = 1
                self.full_check(f"after iteration {it}")
            else:
                self.state["rejected"].setdefault(best["hash"], []).extend(tune.opts_hash(c[2]) for c in top)
                self.event("iteration", iteration=it, result=f"confirmed best {w['mean_gap']} not better than {best['mean_gap']}")
                self.log("iteration", iteration=it, result="screen winners did not hold on 8 rounds", best=best["label"])
            self.save()
        if self.state["status"] != "converged":
            self.state["status"] = "stopped"
        self.state["phase"] = None
        self.save()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", nargs="+", default=[str(tune.BEST_OUT)])
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--batch", type=int, default=18)
    ap.add_argument("--mutate", type=float, default=0.25)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--mode", choices=["single", "global"], default="single",
                    help="single = one change per candidate; global = whole random configs (exploration)")
    ap.add_argument("--focus-round", default=None,
                    help="optimise on this one full round (fast feedback); results go to configs/gatk-focus.conf, not live")
    ap.add_argument("--focus-slice", action="store_true",
                    help="with --focus-round: screen on a slice of it, confirm slice winners on the full round")
    ap.add_argument("--reset", action="store_true",
                    help="forget the saved best and pick the best of --start on the dev rounds")
    ap.add_argument("--stop-when-converged", action="store_true",
                    help="stop when no single change helps (default: keep re-checking)")
    args = ap.parse_args()
    sys.argv = sys.argv[:1]
    os.chdir(tune.ROOT)
    a = Autopilot(args)

    def handle(sig, _):
        a.stop = True
        a.state["status"] = "stopping"
        a.save()
    signal.signal(signal.SIGTERM, handle)
    signal.signal(signal.SIGINT, handle)
    try:
        a.run()
    except Exception as e:  # noqa: BLE001
        a.state["status"] = "error"
        a.state["error"] = f"{type(e).__name__}: {e}"
        a.save()
        raise


if __name__ == "__main__":
    main()
