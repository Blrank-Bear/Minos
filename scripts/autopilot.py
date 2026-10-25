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
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import random_search  # noqa: E402
import tune  # noqa: E402

STATE = tune.TUNE / "autopilot.json"
SCREEN_ROUNDS = ["20261024T154600Z", "20261024T105800Z", "20261024T121000Z"]
CONFIRM_TOP = 3


class Autopilot:
    def __init__(self, args):
        self.args = args
        self.defs = tune.param_defs()
        self.stop = False
        self.rng = random.Random(args.seed)
        self.dev = tune.DEV_ROUNDS
        prev = json.loads(STATE.read_text()) if STATE.exists() else {}
        self.state = {"status": "starting", "pid": os.getpid(), "started": tune.now(), "iteration": prev.get("iteration", 0),
                      "best": prev.get("best"), "history": prev.get("history", []), "phase": None, "batch": []}
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
    def results(self, chash, rounds):
        out = {}
        if tune.RESULTS.exists():
            for line in tune.RESULTS.read_text().splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("config_hash") == chash and r.get("round") in rounds and r.get("ok"):
                    out[r["round"]] = r
        return out

    def run_many(self, items):
        """items: [(conf_path, label, round)] -> runs the missing ones in parallel."""
        def one(conf, label, rd):
            if self.stop:
                return
            cmd = [str(tune.PY), "scripts/score_round.py", str(tune.ROUNDS / rd), "--config", str(conf), "--label", label,
                   "--threads", "2", "--memory-gb", "5"]
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
                "scores": {r["round"]: r["score"] for r in rs}}

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

    # ---------- main loop ----------
    def accept(self, label, opts, summ, why):
        self.state["best"] = {"label": label, "options": opts, "hash": tune.opts_hash(opts), "since": tune.now(), **summ}
        tune.write_conf(tune.BEST_OUT, opts, f"GATK config tuned by scripts/autopilot.py ({label})\n"
                        f"dev mean gap to #1 {summ['mean_gap']:+.5f}, mean rank {summ['mean_rank']:.1f} "
                        f"over {len(self.dev)} rounds ({tune.now()})")
        live = tune.REPO / "configs" / "gatk.conf"
        live.write_bytes(tune.BEST_OUT.read_bytes())
        with tune.JOURNAL.open("a") as fh:
            fh.write(json.dumps({"ts": tune.now(), "tag": "tuning", "text": f"Autopilot accepted {label}: {why}. Deployed as live config."}) + "\n")
        self.event("accept", label=label, mean_gap=summ["mean_gap"], mean_rank=summ["mean_rank"], why=why)
        changes = ", ".join(f"{k}={v}" for k, v in opts.items() if v != self.state.get("prev_best_opts", {}).get(k))
        msg = (f"Autopilot: new best config ({label})\n\n{why}\nmean rank {summ['mean_rank']:.1f}, "
               f"max calling {summ['max_calling_seconds']:.0f} s, {len(self.dev)} dev rounds.\n"
               f"Changes vs previous best: {changes or 'n/a'}\nDeployed as the live miner config.\n\n"
               "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
        subprocess.run(["git", "add", str(tune.BEST_OUT)], cwd=tune.ROOT)
        subprocess.run(["git", "commit", "-q", "-m", msg], cwd=tune.ROOT)
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

        while not self.stop:
            self.state["iteration"] += 1
            it = self.state["iteration"]
            best = self.state["best"]
            # make sure the best has scores on the screen rounds for paired deltas
            self.evaluate([(best["label"], best["options"])], SCREEN_ROUNDS + self.dev, "scoring best")
            self.state["best"]["scores"] = self.summary(best["hash"], SCREEN_ROUNDS + self.dev)["scores"]
            cands = []
            seen = {best["hash"]}
            while len(cands) < self.args.batch:
                opts = dict(best["options"])
                for k, f in random_search.SPACE.items():
                    if self.rng.random() < self.args.mutate:
                        v = f(self.rng)
                        opts[k] = tune.typed(self.defs, k, v) if self.defs[k]["type"] in ("int", "float") else v
                h = tune.opts_hash(opts)
                if h not in seen:
                    seen.add(h)
                    cands.append((f"ap-{it:03d}-{len(cands):02d}", opts))
            screened = self.evaluate(cands, SCREEN_ROUNDS, f"iteration {it}: screening {len(cands)} mutations")
            if self.stop:
                break
            base = self.state["best"]["scores"]
            ranked = []
            for label, opts in cands:
                s = screened[label]
                diffs = [s["scores"][r] - base[r] for r in s["scores"] if r in base]
                if len(diffs) == len(SCREEN_ROUNDS):
                    ranked.append((sum(diffs) / len(diffs), label, opts))
            ranked.sort(key=lambda x: -x[0])
            top = [(l, o) for d, l, o in ranked[:CONFIRM_TOP] if d > 0]
            self.state["history"].append({"iteration": it, "ts": tune.now(), "screened": len(cands),
                                          "best_delta": ranked[0][0] if ranked else None, "confirmed": [l for l, _ in top]})
            if not top:
                self.event("iteration", iteration=it, result="no positive mutation")
                self.save()
                continue
            confirmed = self.evaluate(top, self.dev, f"iteration {it}: confirming {len(top)} on {len(self.dev)} rounds")
            if self.stop:
                break
            winner = max(confirmed, key=lambda l: confirmed[l]["mean_gap"] if confirmed[l]["mean_gap"] is not None else -9)
            w = confirmed[winner]
            ok = (w["done"] == len(self.dev) and w["mean_gap"] is not None
                  and w["mean_gap"] > best["mean_gap"] + tune.MIN_IMPROVEMENT
                  and (w["max_calling_seconds"] or 0) <= tune.MAX_CALLING_SECONDS)
            self.state["history"][-1].update(winner=winner, winner_gap=w["mean_gap"], accepted=ok)
            if ok:
                self.accept(winner, dict(next(o for l, o in top if l == winner)), w,
                            f"dev mean gap {best['mean_gap']:+.5f} -> {w['mean_gap']:+.5f}")
            else:
                self.event("iteration", iteration=it, result=f"best confirmed {w['mean_gap']} not better than {best['mean_gap']}")
            self.save()
        self.state["status"] = "stopped"
        self.state["phase"] = None
        self.save()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", nargs="+", default=[str(tune.BEST_OUT)])
    ap.add_argument("--workers", type=int, default=9)
    ap.add_argument("--batch", type=int, default=18)
    ap.add_argument("--mutate", type=float, default=0.25)
    ap.add_argument("--seed", type=int, default=7)
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
