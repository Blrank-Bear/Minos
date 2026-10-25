#!/usr/bin/env python3
"""Score a miner config against a revealed round, the way a validator would.

Wraps neurons.miner._run_and_score (template run + hap.py + AdvancedScorer)
with what the stock --score path lacks for tuning:

  * the region comes from meta.json (scripts/fetch_round_meta.py), falling back
    to the truth VCF's extent when the round has no metadata,
  * the score is placed on the round's real leaderboard when meta.json has it,
  * the scoring version is set explicitly (default v2, the live one),
  * the thread count is set explicitly, to mimic a small validator (2-8).

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/score_round.py data/rounds/<dir> \
      [--config minos_subnet/configs/gatk.conf] [--tool gatk] [--threads 2]
"""
import argparse
import gzip
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT / "minos_subnet"
sys.path.insert(0, str(REPO))
# Keep miner state inside the project folder even when .env isn't loaded.
os.environ.setdefault("MINOS_SCORING_VERSION_STATE", str(ROOT / "state" / "scoring_version.json"))

# Pad around the outermost truth variants when inferring the region.
REGION_PAD = 1000


def infer_region(truth_vcf: Path) -> str:
    chrom, lo, hi = None, None, None
    with gzip.open(truth_vcf, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            c, pos = line.split("\t", 2)[:2]
            pos = int(pos)
            if chrom is None:
                chrom = c
            elif c != chrom:
                raise ValueError(f"truth spans several contigs ({chrom}, {c})")
            lo = pos if lo is None else min(lo, pos)
            hi = pos if hi is None else max(hi, pos)
    if chrom is None:
        raise ValueError("truth VCF has no records")
    return f"{chrom}:{max(1, lo - REGION_PAD)}-{hi + REGION_PAD}"


def load_meta(round_dir: Path) -> dict:
    p = round_dir / "meta.json"
    return json.loads(p.read_text()) if p.exists() else {}


def placement(score: float, leaderboard: list) -> str:
    scores = sorted((e["combined_final"] for e in leaderboard if e.get("combined_final") is not None), reverse=True)
    if not scores:
        return "no leaderboard"
    rank = 1 + sum(1 for s in scores if s > score)
    return (f"would rank {rank} of {len(scores) + 1} | #1={scores[0]:.6f} "
            f"gap={score - scores[0]:+.6f} | median={scores[len(scores) // 2]:.6f}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("round_dir", type=Path)
    ap.add_argument("--tool", default="gatk", choices=["gatk", "deepvariant", "bcftools"])
    ap.add_argument("--config", type=Path, default=None, help="default: minos_subnet/configs/<tool>.conf")
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--scoring-version", default="v2", choices=["v1", "v2"])
    ap.add_argument("--region", default=None, help="override the inferred region")
    args = ap.parse_args()

    rd = args.round_dir.resolve()
    config_path = str(args.config.resolve()) if args.config else None
    # The miner resolves configs/ and datasets/ relative to the repo.
    os.chdir(REPO)
    bam, truth, muts = rd / "input.bam", rd / "truth.vcf.gz", rd / "mutations.vcf.gz"
    for p in (bam, truth, muts):
        if not p.exists():
            print(f"missing {p}", file=sys.stderr)
            return 2

    meta = load_meta(rd)
    region = args.region or meta.get("region") or infer_region(truth)
    chrom = region.split(":")[0]
    ref = REPO / "datasets" / "reference" / chrom / f"{chrom}.fa"
    if not ref.exists():
        print(f"missing reference {ref}; run scripts/setup_miner.sh reference", file=sys.stderr)
        return 2

    # bittensor reads --config out of sys.argv at import time (as YAML), so
    # hide our arguments from it.
    sys.argv = sys.argv[:1]
    from base.genomics_config import MINER_CONFIG
    from neurons import miner as m

    MINER_CONFIG["num_threads"] = args.threads
    tool_config = m._load_config_for_scoring(config_path, args.tool)

    print(f"round={rd.name} region={region} tool={args.tool} threads={args.threads} "
          f"scoring={args.scoring_version} config={config_path or f'configs/{args.tool}.conf'}", flush=True)
    t0 = time.time()
    score = m._run_and_score(
        tool=args.tool, tool_config=tool_config, bam_path=bam, ref_path=ref,
        truth_path=truth, mutations_path=muts, region=region,
        scoring_version=args.scoring_version,
    )
    print(f"RESULT round={rd.name} score={score} total_seconds={time.time() - t0:.0f}", flush=True)
    if score is not None and meta.get("leaderboard"):
        print(f"PLACEMENT round={rd.name} {placement(score, meta['leaderboard'])}", flush=True)
    return 0 if score is not None else 1


if __name__ == "__main__":
    sys.exit(main())
