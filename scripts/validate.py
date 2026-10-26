#!/usr/bin/env python3
"""Held-out validation: replay configs on every finalized round outside the dev set.

The tuner picks changes using 8 dev rounds; this checks that the result holds on
rounds it never saw. Each config is replayed (validator-identical scoring) on all
finalized held-out rounds in parallel, then summarised: mean score, mean gap to
#1, mean projected rank, wins, top-5 count, and how often it would have beaten
the round's actual #1 outright.

Live progress for the dashboard: data/tune/validation.json.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/validate.py configs/gatk-tuned.conf [configs/stock-gatk.conf ...] [--workers 6]
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tune  # noqa: E402

OUT = tune.TUNE / "validation.json"


def finalized_rounds(exclude):
    out = []
    for rd in sorted(tune.ROUNDS.iterdir()):
        meta = rd / "meta.json"
        if rd.name in exclude or not meta.exists():
            continue
        m = json.loads(meta.read_text())
        if m.get("finalized") and m.get("leaderboard") and (rd / "input.bam").exists():
            out.append(rd.name)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("configs", nargs="+", type=Path)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--memory-gb", type=int, default=6)
    ap.add_argument("--include-dev", action="store_true", help="also replay the tuner's dev rounds")
    ap.add_argument("--dev-only", action="store_true", help="replay only the tuner's 8 dev rounds")
    ap.add_argument("--out", type=Path, default=OUT, help="progress file (default data/tune/validation.json)")
    args = ap.parse_args()
    sys.argv = sys.argv[:1]
    os.chdir(tune.ROOT)
    defs = tune.param_defs()
    rounds = (list(tune.DEV_ROUNDS) if args.dev_only
              else finalized_rounds(set() if args.include_dev else set(tune.DEV_ROUNDS)))
    out_path = args.out

    state = {"status": "running", "pid": os.getpid(), "started": tune.now(), "rounds": rounds, "configs": []}
    entries = []
    for cfg in args.configs:
        opts = tune.parse_conf(cfg, defs)
        entries.append({"name": cfg.stem, "file": str(cfg), "hash": tune.opts_hash(opts), "done": 0,
                        "total": len(rounds), "per_round": {}})
    state["configs"] = entries

    def save():
        state["heartbeat"] = tune.now()
        tmp = out_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2))
        os.replace(tmp, out_path)

    class Runner:  # minimal stand-in so tune.Tuner.run_round / cached can be reused
        stop = False
        rounds = None
    runner = Runner()
    runner.args = args
    runner.rounds = rounds
    run_round = tune.Tuner.run_round.__get__(runner)
    cached = tune.Tuner.cached.__get__(runner)

    def summarise(e):
        have = cached(e["hash"], rounds)
        e["done"] = len(have)
        e["per_round"] = {r: {k: v.get(k) for k in ("score", "gap", "rank", "field", "top1", "calling_seconds")}
                          for r, v in have.items()}
        rs = list(have.values())
        mean = lambda xs: sum(xs) / len(xs) if xs else None  # noqa: E731
        e.update(
            mean_score=mean([r["score"] for r in rs]),
            mean_gap=mean([r["gap"] for r in rs if r.get("gap") is not None]),
            mean_rank=mean([r["rank"] for r in rs if r.get("rank")]),
            wins=sum(1 for r in rs if r.get("rank") == 1),
            beats_top1=sum(1 for r in rs if (r.get("gap") or -1) > 0),
            top5=sum(1 for r in rs if r.get("rank") and r["rank"] <= 5),
            max_calling_seconds=max((r.get("calling_seconds") or 0 for r in rs), default=None),
        )

    tasks = []
    for e, cfg in zip(entries, args.configs):
        have = cached(e["hash"], rounds)
        tasks += [(cfg, e, r) for r in rounds if r not in have]
        summarise(e)
    save()
    with ThreadPoolExecutor(args.workers) as ex:
        futs = [ex.submit(run_round, cfg, f"val-{cfg.stem}", r) for cfg, e, r in tasks]
        for f in as_completed(futs):
            f.result()
            for e in entries:
                summarise(e)
            save()
    for e in entries:
        summarise(e)
    state["status"] = "finished"
    state["finished"] = tune.now()
    save()
    for e in entries:
        print(f"{e['name']}: {e['done']}/{e['total']} rounds  mean score {e['mean_score']:.5f}  "
              f"gap {e['mean_gap']:+.5f}  rank {e['mean_rank']:.1f}  wins {e['wins']}  beats #1 {e['beats_top1']}  "
              f"top5 {e['top5']}  max calling {e['max_calling_seconds']:.0f}s")


if __name__ == "__main__":
    main()
