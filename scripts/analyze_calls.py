#!/usr/bin/env python3
"""Where do a config's false positives come from? Offline analysis of one kept run.

Joins hap.py's per-call verdicts (happy_output.vcf.vcf.gz, QUERY BD=TP/FP)
with the caller's own annotations (output.vcf.gz INFO/FORMAT: QUAL, DP, MQ,
QD, FS, SOR, GQ, AF) and reports how TP and FP calls differ. It also simulates
a QUAL cut-off -- the effect of raising standard_min_confidence_threshold_for_calling
-- on per-class TP/FP and on the v2 score (core + germline), without rerunning
GATK.

Usage (inside WSL, from the project root), on a dir made with score_round.py --keep:
  .venv/bin/python scripts/analyze_calls.py data/analysis/<run> --mutations data/rounds/<round>/mutations.vcf.gz
"""
import argparse
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import pysam

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "minos_subnet"))
from utils.scoring import DIFFICULTY_WEIGHTS, GERMLINE_FP_SCALE, V2_CORE_WEIGHT, V2_GERMLINE_WEIGHT  # noqa: E402


def klass(ref, alt, gt):
    n = abs(len(ref) - len(alt))
    if n:
        return "indel_8bp" if n >= 8 else "indel_4_7bp" if n >= 4 else "indel_2_3bp" if n >= 2 else "indel_1bp"
    hom = gt and len(set(gt)) == 1 and gt[0] not in (0, None)
    return "snp_hom" if hom else "snp_het"


def load_calls(output_vcf):
    calls = {}
    with pysam.VariantFile(str(output_vcf)) as vf:
        for r in vf:
            s = r.samples[0]
            info = r.info
            calls[(r.chrom, r.pos)] = {
                "qual": r.qual or 0.0, "dp": info.get("DP"), "mq": info.get("MQ"), "qd": info.get("QD"),
                "fs": info.get("FS"), "sor": info.get("SOR"), "gq": s.get("GQ"),
                "af": (s.get("AD")[1] / max(1, sum(x or 0 for x in s.get("AD")))) if s.get("AD") and len(s.get("AD")) > 1 and s.get("AD")[1] is not None else None,
            }
    return calls


def load_verdicts(happy_vcf):
    """Per-variant verdicts from hap.py's annotated VCF (TRUTH, QUERY samples)."""
    out = []
    with pysam.VariantFile(str(happy_vcf)) as vf:
        for r in vf:
            t, q = r.samples["TRUTH"], r.samples["QUERY"]
            alt = r.alts[0] if r.alts else r.ref
            bq, bt = q.get("BD"), t.get("BD")
            if bq in ("TP", "FP"):
                gt = t.get("GT") if bq == "TP" else q.get("GT")
                out.append({"pos": (r.chrom, r.pos), "v": bq, "cls": klass(r.ref, alt, gt)})
            elif bt == "FN":
                out.append({"pos": (r.chrom, r.pos), "v": "FN", "cls": klass(r.ref, alt, t.get("GT"))})
    return out


def v2(counts, n_targets, fp_total):
    present = {k: c for k, c in counts.items() if c["tp"] + c["fn"] > 0 or c["fp"] > 0}
    wsum = sum(DIFFICULTY_WEIGHTS[k] for k in present)
    core = 0.0
    for k, c in present.items():
        d = 2 * c["tp"] + c["fn"] + c["fp"]
        core += DIFFICULTY_WEIGHTS[k] / wsum * ((2 * c["tp"] / d) if d else 0.0)
    germ = math.exp(-(fp_total / max(1, n_targets)) / GERMLINE_FP_SCALE)
    return 100 * (V2_CORE_WEIGHT * core + V2_GERMLINE_WEIGHT * germ), core, germ


def q(xs, p):
    xs = sorted(x for x in xs if x is not None)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", type=Path)
    ap.add_argument("--mutations", type=Path, required=True)
    args = ap.parse_args()

    happy = next(args.run_dir.glob("happy_*.vcf.vcf.gz"))
    calls = load_calls(args.run_dir / "output.vcf.gz")
    verdicts = load_verdicts(happy)
    n_targets = sum(1 for _ in pysam.VariantFile(str(args.mutations)))

    for v in verdicts:
        v["ann"] = calls.get(v["pos"], {})
    tp = [v for v in verdicts if v["v"] == "TP"]
    fp = [v for v in verdicts if v["v"] == "FP"]
    fn = [v for v in verdicts if v["v"] == "FN"]
    print(f"calls={len(calls)} TP={len(tp)} FP={len(fp)} FN={len(fn)} targets={n_targets} "
          f"fp/target={len(fp) / max(1, n_targets):.2f}")

    print("\nannotation      TP p10 / p50 / p90           FP p10 / p50 / p90")
    for key in ("qual", "dp", "mq", "qd", "fs", "sor", "gq", "af"):
        a = [v["ann"].get(key) for v in tp]
        b = [v["ann"].get(key) for v in fp]
        fmt = lambda x: "  -   " if x is None else f"{x:6.1f}"  # noqa: E731
        print(f"{key:<8} {fmt(q(a, .1))} {fmt(q(a, .5))} {fmt(q(a, .9))}      {fmt(q(b, .1))} {fmt(q(b, .5))} {fmt(q(b, .9))}")

    print("\nFP by class:", {k: sum(1 for v in fp if v["cls"] == k) for k in DIFFICULTY_WEIGHTS})
    print("FN by class:", {k: sum(1 for v in fn if v["cls"] == k) for k in DIFFICULTY_WEIGHTS})

    print("\nsimulated QUAL cut-off (calls below it dropped; TP lost become FN):")
    print(" QUAL    score    core   germ   TP_lost  FP_removed")
    base_counts = None
    for cut in (0, 30, 40, 50, 60, 80, 100, 150, 200):
        counts = defaultdict(lambda: {"tp": 0, "fn": 0, "fp": 0})
        tl = fr = 0
        for v in verdicts:
            c = counts[v["cls"]]
            qual = v["ann"].get("qual", 0.0)
            if v["v"] == "TP":
                if qual >= cut:
                    c["tp"] += 1
                else:
                    c["fn"] += 1; tl += 1
            elif v["v"] == "FP":
                if qual >= cut:
                    c["fp"] += 1
                else:
                    fr += 1
            else:
                c["fn"] += 1
        counts = {k: counts[k] for k in DIFFICULTY_WEIGHTS}
        fp_total = sum(c["fp"] for c in counts.values())
        s, core, germ = v2(counts, n_targets, fp_total)
        base_counts = base_counts or s
        print(f" {cut:4d}  {s:7.3f}  {core:.4f} {germ:.4f}  {tl:7d}  {fr:9d}")


if __name__ == "__main__":
    main()
