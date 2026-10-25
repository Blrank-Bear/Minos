#!/usr/bin/env python3
"""Score a miner config against a revealed round, the way a validator would.

Wraps neurons.miner._run_and_score (template run + hap.py + AdvancedScorer)
with what the stock --score path lacks for tuning:

  * the region comes from meta.json (scripts/fetch_round_meta.py), falling back
    to the truth VCF's extent when the round has no metadata,
  * the score is placed on the round's real leaderboard when meta.json has it,
  * the scoring version is set explicitly (default v2, the live one),
  * the thread count is set explicitly, to mimic a small validator (2-8),
  * every run is appended to data/replays/results.jsonl with the score, its
    v2 breakdown, runtime and projected placement (read by the dashboard).

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/score_round.py data/rounds/<dir> \
      [--config configs/my.conf] [--tool gatk] [--threads 2] [--label name]
"""
import argparse
import gzip
import hashlib
import json
import math
import os
import shutil
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT / "minos_subnet"
RESULTS = ROOT / "data" / "replays" / "results.jsonl"
sys.path.insert(0, str(REPO))
# Keep miner state inside the project folder even when .env isn't loaded.
os.environ.setdefault("MINOS_SCORING_VERSION_STATE", str(ROOT / "state" / "scoring_version.json"))

# Pad around the outermost truth variants when inferring the region.
REGION_PAD = 1000
METRIC_KEYS = ("f1_snp", "f1_indel", "recall_snp", "recall_indel", "precision_snp",
               "precision_indel", "fp_snp", "fp_indel", "fp_per_target", "titv_query_snp",
               "titv_truth_snp", "hethom_query_snp", "hethom_truth_snp", "query_total_snp",
               "query_total_indel", "truth_total_snp", "truth_total_indel")


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


def placement(score: float, leaderboard: list) -> dict:
    scores = sorted((e["combined_final"] for e in leaderboard if e.get("combined_final") is not None), reverse=True)
    if not scores:
        return {}
    return {
        "rank": 1 + sum(1 for s in scores if s > score),
        "field": len(scores) + 1,
        "top1": scores[0],
        "median": scores[len(scores) // 2],
        "gap": score - scores[0],
    }


def config_hash(options: dict) -> str:
    return hashlib.sha256(json.dumps(options, sort_keys=True).encode()).hexdigest()[:12]


def _clean(v):
    return v if not isinstance(v, float) or math.isfinite(v) else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("round_dir", type=Path)
    ap.add_argument("--tool", default="gatk", choices=["gatk", "deepvariant", "bcftools"])
    ap.add_argument("--config", type=Path, default=None, help="default: minos_subnet/configs/<tool>.conf")
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--memory-gb", type=int, default=None,
                    help="cap the caller container's RAM (default: host RAM - 1 GB); set when running several at once")
    ap.add_argument("--scoring-version", default="v2", choices=["v1", "v2"])
    ap.add_argument("--region", default=None, help="override the inferred region")
    ap.add_argument("--label", default=None, help="config name in results (default: config file stem)")
    ap.add_argument("--job", default=None, help="dashboard job id, recorded with the result")
    ap.add_argument("--no-record", action="store_true", help="don't append to data/replays/results.jsonl")
    args = ap.parse_args()

    rd = args.round_dir.resolve()
    config_path = str(args.config.resolve()) if args.config else None
    label = args.label or (args.config.stem if args.config else f"stock-{args.tool}")
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
    import templates
    from base.genomics_config import MINER_CONFIG
    from neurons import miner as m
    from utils import scoring

    MINER_CONFIG["num_threads"] = args.threads
    tool_config = m._load_config_for_scoring(config_path, args.tool)
    options = tool_config.get(f"{args.tool}_options", {})
    if args.memory_gb:
        # Infra setting read by the template, outside <tool>_options, so it is
        # not part of the submitted config or its hash.
        tool_config["memory_gb"] = args.memory_gb

    # Observe the run without changing it: wrap the template call (runtime,
    # variant count) and the v2 scorer (its inputs, for the breakdown).
    seen = {}
    real_load = templates.load_template

    def load_template(tool):
        mod = real_load(tool)
        real_call = mod.variant_call

        class Timed:
            def __getattr__(self, name):
                return getattr(mod, name)

            @staticmethod
            def variant_call(**kw):
                t = time.time()
                res = real_call(**kw)
                seen["calling_seconds"] = time.time() - t
                seen["variant_count"] = res.get("variant_count")
                seen["calling_error"] = None if res.get("success") else res.get("error")
                return res
        return Timed()

    templates.load_template = load_template
    real_v2 = scoring.AdvancedScorer.compute_score_v2

    def compute_score_v2(metrics, class_counts=None):
        seen["metrics"] = {k: metrics.get(k) for k in METRIC_KEYS}
        seen["class_counts"] = class_counts
        return real_v2(metrics, class_counts)

    scoring.AdvancedScorer.compute_score_v2 = staticmethod(compute_score_v2)

    print(f"round={rd.name} region={region} tool={args.tool} threads={args.threads} "
          f"scoring={args.scoring_version} config={config_path or f'configs/{args.tool}.conf'}", flush=True)
    # _run_and_score writes next to the BAM (score_run/). Give every run its own
    # directory with hard-linked inputs so concurrent replays of one round (tuner
    # + dashboard jobs) can't overwrite each other's VCFs.
    work = rd / "runs" / f"{os.getpid()}-{uuid.uuid4().hex[:8]}"
    work.mkdir(parents=True)
    for name in ("input.bam", "input.bam.bai"):
        if (rd / name).exists():
            try:
                os.link(rd / name, work / name)
            except OSError:
                shutil.copy2(rd / name, work / name)
    t0 = time.time()
    try:
        score = m._run_and_score(
            tool=args.tool, tool_config=tool_config, bam_path=work / "input.bam", ref_path=ref,
            truth_path=truth, mutations_path=muts, region=region,
            scoring_version=args.scoring_version,
        )
    finally:
        shutil.rmtree(work, ignore_errors=True)
    total = time.time() - t0
    place = placement(score, meta["leaderboard"]) if score is not None and meta.get("leaderboard") else {}
    print(f"RESULT round={rd.name} score={score} total_seconds={total:.0f}", flush=True)
    if place:
        print(f"PLACEMENT round={rd.name} would rank {place['rank']} of {place['field']} | "
              f"#1={place['top1']:.6f} gap={place['gap']:+.6f} | median={place['median']:.6f}", flush=True)

    if not args.no_record:
        breakdown = {}
        counts = seen.get("class_counts") or {}
        if counts:
            class_f1 = {}
            for cls, c in counts.items():
                denom = 2 * c["tp"] + c["fn"] + c["fp"]
                class_f1[cls] = {**c, "f1": (2 * c["tp"] / denom) if denom else None}
            breakdown["class"] = class_f1
            core = scoring.difficulty_weighted_f1(counts)
            fpt = (seen.get("metrics") or {}).get("fp_per_target")
            breakdown["core"] = core
            if fpt is not None:
                breakdown["germline"] = math.exp(-float(fpt) / scoring.GERMLINE_FP_SCALE)
        record = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "job": args.job,
            "label": label,
            "config_hash": config_hash(options),
            "tool": args.tool,
            "options": options,
            "round": rd.name,
            "round_id": meta.get("round_id"),
            "region": region,
            "chromosome": chrom,
            "threads": args.threads,
            "scoring_version": args.scoring_version,
            "score": score,
            "ok": score is not None,
            "error": seen.get("calling_error"),
            "calling_seconds": seen.get("calling_seconds"),
            "total_seconds": total,
            "variant_count": seen.get("variant_count"),
            "metrics": {k: _clean(v) for k, v in (seen.get("metrics") or {}).items()},
            "breakdown": breakdown,
            **place,
        }
        RESULTS.parent.mkdir(parents=True, exist_ok=True)
        with RESULTS.open("a") as fh:
            fh.write(json.dumps(record) + "\n")
    return 0 if score is not None else 1


if __name__ == "__main__":
    sys.exit(main())
