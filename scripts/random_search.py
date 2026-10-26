#!/usr/bin/env python3
"""Random search over whole GATK configs on one round (finds interaction basins).

One-at-a-time screening and greedy descent only see single-parameter moves.
This samples N complete configs from moderate ranges of every parameter that
showed an effect, replays them all on one round in parallel (validator-
identical scoring), and prints the best. Results are recorded in
data/replays/results.jsonl (label rs-<seed>-<i>) and the sampled configs are
kept in data/analysis/rs/.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/random_search.py --round 20261024T154600Z --n 40 [--workers 8] [--seed 1]
"""
import argparse
import json
import os
import random
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import tune  # noqa: E402

OUT = ROOT / "data" / "analysis" / "rs"

SPACE = {
    "standard_min_confidence_threshold_for_calling": lambda r: float(r.choice([30, 40, 50, 60, 70, 80, 90, 100])),
    "min_base_quality_score": lambda r: r.choice([10, 12, 15, 18, 20, 22, 24, 25]),
    "min_mapping_quality_score": lambda r: r.choice([20, 30, 40, 45, 50, 55, 58, 60]),
    "pcr_indel_model": lambda r: r.choice(["CONSERVATIVE", "AGGRESSIVE", "AGGRESSIVE", "NONE"]),
    "phred_scaled_global_read_mismapping_rate": lambda r: r.choice([25, 30, 35, 40, 45, 50]),
    "heterozygosity": lambda r: r.choice([0.001, 0.002, 0.003, 0.005, 0.008]),
    "min_pruning": lambda r: r.choice([2, 2, 3, 4]),
    "contamination_fraction_to_filter": lambda r: r.choice([0.0, 0.0, 0.02, 0.05, 0.08]),
    "assembly_region_padding": lambda r: r.choice([50, 100, 150, 200, 300]),
    "max_assembly_region_size": lambda r: r.choice([200, 300, 400, 600]),
    "dont_use_soft_clipped_bases": lambda r: r.random() < 0.3,
    "base_quality_score_threshold": lambda r: r.choice([10, 15, 18, 20, 25]),
    "pair_hmm_gap_continuation_penalty": lambda r: r.choice([5, 10, 15, 25]),
    "min_dangling_branch_length": lambda r: r.choice([2, 4, 6, 8]),
    "active_probability_threshold": lambda r: r.choice([0.001, 0.002, 0.005, 0.01, 0.02]),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--round", required=True)
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--base", default=str(ROOT / "configs" / "stock-gatk.conf"))
    ap.add_argument("--mutate", type=float, default=1.0,
                    help="probability each parameter is re-drawn; <1 searches around --base")
    args = ap.parse_args()
    sys.argv = sys.argv[:1]
    os.chdir(ROOT)
    defs = tune.param_defs()
    base = tune.parse_conf(Path(args.base), defs)
    rng = random.Random(args.seed)
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = []
    for i in range(args.n):
        opts = dict(base)
        while opts == base:  # at least one change
            for k, f in SPACE.items():
                if rng.random() < args.mutate:
                    opts[k] = tune.typed(defs, k, f(rng)) if defs[k]["type"] in ("int", "float") else f(rng)
        label = f"rs-{args.seed}-{i:03d}"
        conf = OUT / f"{label}.conf"
        tune.write_conf(conf, opts, f"random search {label}")
        jobs.append((label, conf, opts))

    def run(label, conf):
        cmd = [str(tune.PY), "scripts/score_round.py", str(tune.ROUNDS / args.round), "--config", str(conf),
               "--label", label, "--threads", "2", "--memory-gb", "5"]
        return label, subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True).stdout

    scores = []
    with ThreadPoolExecutor(args.workers) as ex:
        futs = [ex.submit(run, l, c) for l, c, _ in jobs]
        for f in as_completed(futs):
            label, out = f.result()
            line = next((l for l in out.splitlines() if l.startswith("RESULT")), "")
            s = line.split("score=")[1].split()[0] if "score=" in line else "None"
            score = float(s) if s not in ("None", "") else None
            scores.append((score, label))
            print(f"{label} score={score}", flush=True)
    scores.sort(key=lambda x: -(x[0] or -1))
    print("\nTOP 8:")
    by_label = {l: o for l, _, o in jobs}
    for s, l in scores[:8]:
        diff = {k: v for k, v in by_label[l].items() if v != base.get(k)}
        print(f"{s}  {l}  {json.dumps(diff)}")


if __name__ == "__main__":
    main()
