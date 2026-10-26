#!/usr/bin/env python3
"""Compare true vs false long indels (>= 8 bp) in a kept run.

For each long-indel call: hap.py verdict, length, insertion/deletion, QUAL,
genotype, GQ, depth, allele balance, and the reference repeat context (longest
homopolymer / short tandem repeat run at the site). Prints the distributions
side by side so a separating feature (and thus a GATK lever) can be spotted.

Usage: .venv/bin/python scripts/long_indels.py data/analysis/<kept_run> <reference.fa>
"""
import glob
import statistics
import sys
from collections import Counter

import pysam

run, ref_path = sys.argv[1], sys.argv[2]
fa = pysam.FastaFile(ref_path)
calls = {}
with pysam.VariantFile(f"{run}/output.vcf.gz") as vf:
    for r in vf:
        s = r.samples[0]
        ad = s.get("AD")
        af = (ad[1] / max(1, sum(x or 0 for x in ad))) if ad and len(ad) > 1 and ad[1] is not None else None
        calls[(r.chrom, r.pos)] = {"qual": r.qual or 0, "gt": s.get("GT"), "gq": s.get("GQ"), "dp": r.info.get("DP"),
                                   "af": af, "qd": r.info.get("QD"), "fs": r.info.get("FS"), "sor": r.info.get("SOR")}


def repeat_run(chrom, pos):
    """Longest run of a 1-6 bp unit starting right after pos (reference)."""
    seq = fa.fetch(chrom, pos, pos + 120).upper()
    best = 0
    for unit in range(1, 7):
        motif = seq[:unit]
        n = 0
        while seq[n * unit:(n + 1) * unit] == motif:
            n += 1
        best = max(best, n * unit)
    return best


rows = []
for r in pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0]):
    q, t = r.samples["QUERY"], r.samples["TRUTH"]
    alt = r.alts[0] if r.alts else r.ref
    n = len(alt) - len(r.ref)
    if abs(n) < 8:
        continue
    verdict = "FP" if q.get("BD") == "FP" else "TP" if t.get("BD") == "TP" else "FN" if t.get("BD") == "FN" else None
    if not verdict:
        continue
    c = calls.get((r.chrom, r.pos), {})
    rows.append({"v": verdict, "len": abs(n), "kind": "ins" if n > 0 else "del", "rep": repeat_run(r.chrom, r.pos), **c})

for v in ("TP", "FP", "FN"):
    rs = [x for x in rows if x["v"] == v]
    print(f"\n{v}: {len(rs)}  ins/del {Counter(x['kind'] for x in rs)}")
    for key in ("len", "rep", "qual", "gq", "dp", "af", "qd", "sor"):
        vals = sorted(x[key] for x in rs if x.get(key) is not None)
        if vals:
            q = lambda p: vals[min(len(vals) - 1, int(p * len(vals)))]  # noqa: E731
            print(f"  {key:<5} p10 {q(.1):8.2f}  p50 {q(.5):8.2f}  p90 {q(.9):8.2f}")
    if v != "FN":
        print("  GT:", Counter(str(x.get("gt")) for x in rs).most_common(4))
