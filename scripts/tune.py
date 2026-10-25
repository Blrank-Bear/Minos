#!/usr/bin/env python3
"""One-parameter-at-a-time (coordinate descent) tuning of a GATK config.

Starting from a base config, each step changes ONE parameter to a candidate
value, replays the result on a dev set of past rounds (scripts/score_round.py,
validator-identical scoring), and keeps the change only if it improves the
objective: the mean gap to each round's real #1 score. Candidates whose
calling time could break the validators' 900 s limit are rejected.

Live progress for the dashboard (Tuning tab):
  data/tune/state.json    current step, candidate, per-round progress, best so far
  data/tune/events.jsonl  one line per event (start, candidate result, accept, ...)
  configs/gatk-tuned.conf the best config so far (rewritten on every acceptance)
Results land in data/replays/results.jsonl like any replay, and already-scored
(config, round) pairs are reused, so a stopped run resumes where it left off.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/tune.py [--workers 5] [--plan default] [--base configs/stock-gatk.conf]
"""
import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT / "minos_subnet"
PY = ROOT / ".venv" / "bin" / "python"
TUNE = ROOT / "data" / "tune"
STATE = TUNE / "state.json"
EVENTS = TUNE / "events.jsonl"
CANDIDATES = TUNE / "configs"
RESULTS = ROOT / "data" / "replays" / "results.jsonl"
ROUNDS = ROOT / "data" / "rounds"
BEST_OUT = ROOT / "configs" / "gatk-tuned.conf"
JOURNAL = ROOT / "data" / "journal.jsonl"
sys.path.insert(0, str(REPO))

# Mixed chromosomes and window sizes; all finalized with leaderboards.
DEV_ROUNDS = [
    "20261024T045800Z",  # chr11 14.4 Mb
    "20261024T121000Z",  # chr11  7.8 Mb
    "20261024T034600Z",  # chr11  8.0 Mb
    "20261024T154600Z",  # chr12  6.0 Mb
    "20261025T012200Z",  # chr12 10.2 Mb
    "20261024T214600Z",  # chr13 14.6 Mb
    "20261024T105800Z",  # chr13  6.4 Mb
    "20261025T034600Z",  # chr14 11.8 Mb
]

# Parameter order: biggest expected precision levers first.
PLANS = {
    "default": [
        ("standard_min_confidence_threshold_for_calling", [20.0, 40.0, 50.0, 60.0, 80.0]),
        ("pcr_indel_model", ["NONE", "AGGRESSIVE", "HOSTILE"]),
        ("min_mapping_quality_score", [10, 30, 40, 50]),
        ("min_base_quality_score", [5, 15, 20]),
        ("heterozygosity", [0.0005, 0.002]),
        ("indel_heterozygosity", [0.00005, 0.00025]),
        ("phred_scaled_global_read_mismapping_rate", [30, 60]),
        ("contamination_fraction_to_filter", [0.01, 0.03, 0.05]),
        ("max_reads_per_alignment_start", [0, 25, 100]),
        ("dont_use_soft_clipped_bases", [True]),
        ("base_quality_score_threshold", [10, 25]),
        ("active_probability_threshold", [0.001, 0.005]),
        ("min_pruning", [1, 3]),
        ("pruning_lod_threshold", [1.5, 3.5]),
        ("pair_hmm_gap_continuation_penalty", [5, 15]),
        ("assembly_region_padding", [50, 200]),
        ("max_alternate_alleles", [3, 10]),
        ("recover_all_dangling_branches", [True]),
    ],
}

# Screening: every single change, wide ranges, on three short rounds (one per
# main chromosome). Scored as the paired mean score difference vs the base
# config on the same rounds, so round difficulty cancels out.
SCREEN_ROUNDS = ["20261024T154600Z", "20261024T105800Z", "20261024T121000Z"]  # chr12 6.0, chr13 6.4, chr11 7.8 Mb
SCREEN = [
    ("standard_min_confidence_threshold_for_calling", [50.0, 80.0, 100.0, 150.0]),
    ("min_mapping_quality_score", [30, 40, 50, 60]),
    ("min_base_quality_score", [15, 20, 25]),
    ("base_quality_score_threshold", [10, 25]),
    ("pcr_indel_model", ["NONE", "AGGRESSIVE", "HOSTILE"]),
    ("heterozygosity", [0.0001, 0.0005, 0.003]),
    ("indel_heterozygosity", [0.00001, 0.00005, 0.0005]),
    ("phred_scaled_global_read_mismapping_rate", [20, 30, 60]),
    ("contamination_fraction_to_filter", [0.02, 0.05, 0.1, 0.2]),
    ("max_reads_per_alignment_start", [0, 10, 25]),
    ("dont_use_soft_clipped_bases", [True]),
    ("active_probability_threshold", [0.0005, 0.005, 0.02]),
    ("min_pruning", [1, 3, 5]),
    ("pruning_lod_threshold", [1.0, 4.0]),
    ("adaptive_pruning_initial_error_rate", [0.0001, 0.01]),
    ("pair_hmm_gap_continuation_penalty", [5, 15, 25]),
    ("max_alternate_alleles", [2, 10]),
    ("min_dangling_branch_length", [2, 8]),
    ("recover_all_dangling_branches", [True]),
    ("max_num_haplotypes_in_population", [32, 256]),
    ("min_assembly_region_size", [25, 100]),
    ("max_assembly_region_size", [200, 500]),
    ("assembly_region_padding", [50, 200]),
]
SCREEN_MIN_DELTA = 0.0002   # paired score gain (0-1 scale) for a value to enter the descent plan
SCREEN_KEEP_VALUES = 2      # best values per parameter carried into the descent

MAX_CALLING_SECONDS = 600   # headroom under the validators' 900 s at 2 threads
MIN_IMPROVEMENT = 1e-5      # mean-gap units; ties keep the current config


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def param_defs():
    from templates.tool_params import GATK_QUALITY_PARAMS
    return GATK_QUALITY_PARAMS


def typed(defs, k, v):
    t = defs[k]["type"]
    return float(v) if t == "float" else int(v) if t == "int" else v


def opts_hash(opts):
    return hashlib.sha256(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:12]


def parse_conf(path: Path, defs) -> dict:
    out = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip()
        t = defs[k]["type"]
        out[k] = (v.lower() == "true") if t == "bool" else typed(defs, k, v) if t in ("int", "float") else v
    return out


def write_conf(path: Path, opts: dict, header: str):
    lines = [f"# {l}" for l in header.splitlines()]
    for k, v in opts.items():
        lines.append(f"{k}={'true' if v is True else 'false' if v is False else repr(v) if isinstance(v, float) else v}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


class Tuner:
    def __init__(self, args):
        self.args = args
        self.defs = param_defs()
        self.rounds = args.rounds
        self.stop = False
        TUNE.mkdir(parents=True, exist_ok=True)
        prev = json.loads(STATE.read_text()) if STATE.exists() else {}
        base = parse_conf(Path(args.base), self.defs)
        self.state = {
            "status": "starting", "pid": os.getpid(), "started": now(), "heartbeat": now(),
            "plan": args.plan, "objective": "mean gap to #1 over dev rounds (higher is better)",
            "dev_rounds": self.rounds, "workers": args.workers, "threads": args.threads,
            "base": {"file": str(Path(args.base)), "options": base, "hash": opts_hash(base)},
            "best": prev.get("best") if args.resume and prev.get("best") else None,
            "step": None, "current": None, "history": prev.get("history", []) if args.resume else [],
            "completed_params": prev.get("completed_params", []) if args.resume else [],
            "runs": 0,
        }
        self.save()

    # ---------- persistence ----------
    def save(self):
        self.state["heartbeat"] = now()
        tmp = STATE.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.state, indent=2))
        os.replace(tmp, STATE)

    def event(self, kind, **kw):
        with EVENTS.open("a") as fh:
            fh.write(json.dumps({"ts": now(), "kind": kind, **kw}) + "\n")

    def journal(self, text, tag="tuning"):
        with JOURNAL.open("a") as fh:
            fh.write(json.dumps({"ts": now(), "tag": tag, "text": text}) + "\n")

    # ---------- evaluation ----------
    def cached(self, chash, rounds=None):
        rounds = set(rounds or self.rounds)
        out = {}
        if RESULTS.exists():
            for line in RESULTS.read_text().splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("config_hash") == chash and r.get("round") in rounds and r.get("ok"):
                    out[r["round"]] = r
        return out

    # ---------- phase 1: screening ----------
    def screen(self):
        """Each single change vs the base on SCREEN_ROUNDS, all runs in one pool."""
        base_opts = dict(self.state["best"]["options"])
        rounds = self.args.screen_rounds
        configs = [{"param": None, "value": None, "opts": base_opts, "label": "screen-base"}]
        for param, values in SCREEN:
            for v in values:
                v = typed(self.defs, param, v) if self.defs[param]["type"] in ("int", "float") else v
                if v == base_opts.get(param, self.defs[param]["default"]):
                    continue
                configs.append({"param": param, "value": v, "opts": {**base_opts, param: v},
                                "label": f"screen-{param}={v}"})
        for c in configs:
            c["hash"] = opts_hash(c["opts"])
            c["conf"] = CANDIDATES / f"{c['hash']}.conf"
            write_conf(c["conf"], c["opts"], f"screen candidate {c['label']} ({c['hash']})")
        sc = self.state.setdefault("screen", {})
        sc.update(status="running", rounds=rounds, base_hash=configs[0]["hash"], started=sc.get("started") or now(),
                  candidates=[{"param": c["param"], "value": c["value"], "hash": c["hash"], "label": c["label"],
                               "done": 0, "total": len(rounds), "delta": None, "per_round": {}} for c in configs[1:]])
        self.state["phase"] = "screen"
        self.state["current"] = None
        self.state["step"] = {"index": 0, "param": "(screening)", "of": len(configs) - 1}

        def refresh():
            base = self.cached(configs[0]["hash"], rounds)
            sc["base_done"] = len(base)
            for c, entry in zip(configs[1:], sc["candidates"]):
                have = self.cached(c["hash"], rounds)
                entry["done"] = len(have)
                entry["per_round"] = {r: {"score": v["score"], "calling_seconds": v.get("calling_seconds")}
                                      for r, v in have.items()}
                diffs = [have[r]["score"] - base[r]["score"] for r in have if r in base]
                entry["delta"] = sum(diffs) / len(diffs) if diffs else None
                entry["max_calling_seconds"] = max((v.get("calling_seconds") or 0 for v in have.values()), default=None)
            self.state["step"]["index"] = sum(1 for e in sc["candidates"] if e["done"] == e["total"])
            self.save()

        tasks = []
        for c in configs:
            have = self.cached(c["hash"], rounds)
            tasks += [(c, r) for r in rounds if r not in have]
        refresh()
        self.event("screen_start", candidates=len(configs) - 1, runs=len(tasks), rounds=rounds)
        with ThreadPoolExecutor(self.args.workers) as ex:
            futs = [ex.submit(self.run_round, c["conf"], c["label"], r) for c, r in tasks]
            for f in as_completed(futs):
                if f.cancelled():  # cancelled below once a stop was requested
                    continue
                f.result()
                self.state["runs"] += 1
                refresh()
                if self.stop:
                    for g in futs:
                        g.cancel()
        refresh()
        if self.stop:
            return None
        # Descent plan: parameters ordered by their best screened gain; per
        # parameter the best few positive values, fastest-enough ones only.
        by_param = {}
        for e in sc["candidates"]:
            if e["delta"] is None or e["delta"] < SCREEN_MIN_DELTA:
                continue
            if (e.get("max_calling_seconds") or 0) > MAX_CALLING_SECONDS:
                continue
            by_param.setdefault(e["param"], []).append(e)
        plan = sorted(((p, sorted(es, key=lambda e: -e["delta"])[:SCREEN_KEEP_VALUES]) for p, es in by_param.items()),
                      key=lambda pe: -pe[1][0]["delta"])
        sc["plan"] = [[p, [e["value"] for e in es]] for p, es in plan]
        sc["status"] = "done"
        sc["finished"] = now()
        self.save()
        top = ", ".join(f"{p}={es[0]['value']} ({es[0]['delta']:+.4f})" for p, es in plan[:6])
        self.event("screen_done", plan=sc["plan"])
        self.journal(f"Screening done ({len(configs) - 1} single changes x {len(rounds)} rounds). "
                     f"{len(plan)} parameters improved the score; strongest: {top or 'none'}.")
        return sc["plan"]

    def run_round(self, conf: Path, label: str, rd: str):
        if self.stop:  # stopping: don't start queued replays (pool threads pick them up before cancel)
            return rd, -1
        cmd = [str(PY), "scripts/score_round.py", str(ROUNDS / rd), "--config", str(conf), "--tool", "gatk",
               "--threads", str(self.args.threads), "--memory-gb", str(self.args.memory_gb), "--label", label]
        log = TUNE / "logs" / f"{label}-{rd}.log"
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("w") as fh:
            rc = subprocess.run(cmd, cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT).returncode
        return rd, rc

    def evaluate(self, opts: dict, label: str):
        chash = opts_hash(opts)
        conf = CANDIDATES / f"{chash}.conf"
        write_conf(conf, opts, f"tune candidate {label} ({chash})")
        have = self.cached(chash)
        todo = [r for r in self.rounds if r not in have]
        cur = self.state["current"]
        cur.update(hash=chash, label=label, rounds_total=len(self.rounds), rounds_done=len(have),
                   per_round={r: {"score": v["score"], "gap": v.get("gap"), "rank": v.get("rank"),
                                  "calling_seconds": v.get("calling_seconds"), "cached": True} for r, v in have.items()})
        self.save()
        if todo:
            with ThreadPoolExecutor(self.args.workers) as ex:
                futs = [ex.submit(self.run_round, conf, label, rd) for rd in todo]
                for f in as_completed(futs):
                    rd, rc = f.result()
                    r = self.cached(chash).get(rd)
                    cur["rounds_done"] += 1
                    cur["per_round"][rd] = ({"score": r["score"], "gap": r.get("gap"), "rank": r.get("rank"),
                                             "calling_seconds": r.get("calling_seconds")} if r else {"failed": True, "rc": rc})
                    self.state["runs"] += 1
                    self.save()
        res = self.cached(chash)
        ok = [res[r] for r in self.rounds if r in res]
        failed = len(self.rounds) - len(ok)
        mean = lambda xs: sum(xs) / len(xs) if xs else None  # noqa: E731
        return {
            "hash": chash, "label": label, "failed": failed,
            "mean_gap": mean([r["gap"] for r in ok if r.get("gap") is not None]),
            "mean_score": mean([r["score"] for r in ok]),
            "mean_rank": mean([r["rank"] for r in ok if r.get("rank")]),
            "wins": sum(1 for r in ok if r.get("rank") == 1),
            "top5": sum(1 for r in ok if r.get("rank") and r["rank"] <= 5),
            "max_calling_seconds": max((r.get("calling_seconds") or 0 for r in ok), default=None),
            "mean_core": mean([r["breakdown"].get("core") for r in ok if r.get("breakdown", {}).get("core") is not None]),
            "mean_germline": mean([r["breakdown"].get("germline") for r in ok if r.get("breakdown", {}).get("germline") is not None]),
        }

    def deploy(self):
        """Make the best config the live miner config (what a registered miner submits)."""
        live = REPO / "configs" / "gatk.conf"
        backup = ROOT / "state" / "config_backups" / f"gatk-{datetime.now():%Y%m%d-%H%M%S}.conf"
        backup.parent.mkdir(parents=True, exist_ok=True)
        if live.exists():
            backup.write_bytes(live.read_bytes())
        live.write_bytes(BEST_OUT.read_bytes())
        self.event("deploy", file=str(live.relative_to(ROOT)), backup=str(backup.relative_to(ROOT)))

    def extend(self, param, start, accepted, tried):
        """Next value beyond `accepted`, moving away from `start`, or None.

        Only when `accepted` is the most extreme value tried in that direction.
        Step = a third of the distance travelled from the start (at least 1 for
        ints), clamped to the parameter's valid range.
        """
        d = self.defs[param]
        direction = 1 if accepted > start else -1
        if any((t - accepted) * direction > 0 for t in tried):
            return None
        step = abs(accepted - start) / 3
        if d["type"] == "int":
            step = max(1, round(step))
        nxt = accepted + direction * step
        nxt = min(d["max"], max(d["min"], nxt))
        nxt = int(nxt) if d["type"] == "int" else round(float(nxt), 10)
        return None if nxt == accepted or nxt in tried else nxt

    def better(self, cand, best):
        if cand["failed"] or cand["mean_gap"] is None:
            return False, "failed rounds"
        if (cand["max_calling_seconds"] or 0) > MAX_CALLING_SECONDS:
            return False, f"too slow ({cand['max_calling_seconds']:.0f}s > {MAX_CALLING_SECONDS}s)"
        if cand["mean_gap"] > best["mean_gap"] + MIN_IMPROVEMENT:
            return True, f"gap {best['mean_gap']:+.5f} -> {cand['mean_gap']:+.5f}"
        return False, f"no gain ({cand['mean_gap']:+.5f} vs {best['mean_gap']:+.5f})"

    # ---------- main loop ----------
    def run(self):
        self.state["status"] = "running"
        self.event("start", plan=self.args.plan, rounds=self.rounds, workers=self.args.workers)

        if not self.state["best"]:
            self.state["step"] = {"index": 0, "param": "(baseline)", "of": 0}
            self.state["current"] = {"param": None, "value": None}
            base = self.evaluate(dict(self.state["base"]["options"]), "tune-base")
            self.state["best"] = {**base, "options": dict(self.state["base"]["options"]), "since": now()}
            self.event("baseline", **base)
            self.save()

        if self.args.plan == "screen":
            sc = self.state.get("screen") or {}
            plan = sc.get("plan") if sc.get("status") == "done" else self.screen()
            if plan is None:  # stopped mid-screen
                self.state["status"] = "stopped"
                self.save()
                return
        else:
            plan = PLANS[self.args.plan]
        self.state["phase"] = "descent"
        self.state["plan_params"] = [p for p, _ in plan]

        for idx, (param, values) in enumerate(plan, 1):
            if self.stop:
                break
            if param in self.state["completed_params"]:
                continue
            self.state["step"] = {"index": idx, "param": param, "of": len(plan), "values": values}
            start_value = self.state["best"]["options"].get(param, self.defs[param]["default"])
            numeric = self.defs[param]["type"] in ("int", "float")
            queue = [typed(self.defs, param, v) if numeric else v for v in values]
            tried = set()
            while queue:
                v = queue.pop(0)
                if self.stop:
                    break
                if v == start_value or v in tried:
                    continue
                tried.add(v)
                opts = dict(self.state["best"]["options"])
                opts[param] = v
                label = f"tune-{idx:02d}-{param}={v}"
                self.state["current"] = {"param": param, "value": v, "from": self.state["best"]["options"].get(param)}
                self.save()
                cand = self.evaluate(opts, label)
                accept, why = self.better(cand, self.state["best"])
                entry = {"ts": now(), "step": idx, "param": param, "value": v,
                         "from": self.state["best"]["options"].get(param), "accepted": accept, "reason": why, **cand}
                self.state["history"].append(entry)
                self.event("candidate", **entry)
                if accept:
                    self.state["best"] = {**cand, "options": opts, "since": now()}
                    write_conf(BEST_OUT, opts, f"GATK config tuned by scripts/tune.py\n"
                               f"dev mean gap to #1 {cand['mean_gap']:+.5f}, mean rank {cand['mean_rank']:.1f} "
                               f"over {len(self.rounds)} rounds ({now()})")
                    self.event("accept", param=param, value=v, mean_gap=cand["mean_gap"])
                    if self.args.deploy:
                        self.deploy()
                    self.journal(f"Accepted {param}={v}: {why} (mean rank {cand['mean_rank']:.1f}, "
                                 f"wins {cand['wins']}/{len(self.rounds)}).")
                    # Edge extension: if this value is the furthest tried in its
                    # direction, keep stepping that way until a step stops helping.
                    nxt = self.extend(param, start_value, v, tried) if numeric else None
                    if nxt is not None:
                        queue = [nxt]
                self.save()
            if not self.stop:
                self.state["completed_params"].append(param)
                self.save()

        self.state["status"] = "stopped" if self.stop else "finished"
        self.state["current"] = None
        self.save()
        self.event(self.state["status"], best=self.state["best"]["mean_gap"])
        if not self.stop:
            b = self.state["best"]
            self.journal(f"Tuning pass finished: best dev mean gap {b['mean_gap']:+.5f}, "
                         f"mean rank {b['mean_rank']:.1f}, {b['wins']} wins. Config: configs/gatk-tuned.conf.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=str(ROOT / "configs" / "stock-gatk.conf"))
    ap.add_argument("--plan", default="screen", choices=sorted(PLANS) + ["screen"],
                    help="'screen' = screen every single change first, then descend in order of gain")
    ap.add_argument("--rounds", nargs="+", default=DEV_ROUNDS)
    ap.add_argument("--screen-rounds", nargs="+", default=SCREEN_ROUNDS)
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--memory-gb", type=int, default=6)
    ap.add_argument("--resume", action="store_true", help="continue from data/tune/state.json")
    ap.add_argument("--deploy", action="store_true",
                    help="copy every new best into minos_subnet/configs/gatk.conf (the live miner config)")
    args = ap.parse_args()
    sys.argv = sys.argv[:1]
    os.chdir(ROOT)
    t = Tuner(args)

    def handle(sig, _):
        t.stop = True
        t.state["status"] = "stopping"
        t.save()
    signal.signal(signal.SIGTERM, handle)
    signal.signal(signal.SIGINT, handle)
    try:
        t.run()
    except Exception as e:  # noqa: BLE001
        t.state["status"] = "error"
        t.state["error"] = f"{type(e).__name__}: {e}"
        t.save()
        raise


if __name__ == "__main__":
    main()
