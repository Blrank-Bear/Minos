#!/usr/bin/env python3
"""For false long indels: is there a truth indel in the same repeat nearby?

Near-misses (truth indel within N bp, different length/position) mean the
caller sees a real event but represents it differently; isolated FPs mean an
invented event. Prints, per FP long indel, the nearest truth record and the
length difference, plus a summary.

Usage: .venv/bin/python scripts/fp_neighbours.py data/analysis/<kept_run> <truth.vcf.gz> [--min-len 8]
"""
import bisect
import glob
import sys
from collections import Counter

import pysam

run, truth_path = sys.argv[1], sys.argv[2]
min_len = int(sys.argv[sys.argv.index("--min-len") + 1]) if "--min-len" in sys.argv else 8
truth = [(r.pos, len(r.alts[0]) - len(r.ref) if r.alts else 0, r.ref, r.alts[0] if r.alts else "")
         for r in pysam.VariantFile(truth_path)]
truth.sort()
tpos = [t[0] for t in truth]
near = Counter()
for r in pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0]):
    q = r.samples["QUERY"]
    if q.get("BD") != "FP" or not r.alts:
        continue
    d = len(r.alts[0]) - len(r.ref)
    if abs(d) < min_len:
        continue
    i = bisect.bisect_left(tpos, r.pos)
    cands = [truth[j] for j in range(max(0, i - 3), min(len(truth), i + 3))]
    best = min(cands, key=lambda t: abs(t[0] - r.pos)) if cands else None
    dist = abs(best[0] - r.pos) if best else 10**9
    bucket = "<=10bp" if dist <= 10 else "11-50bp" if dist <= 50 else ">50bp"
    near[bucket] += 1
    tl = best[1] if best else None
    print(f"{r.pos} call {d:+d} GT={q.get('GT')} | nearest truth {dist:>6}bp away"
          + (f" ({tl:+d} len, {'indel' if tl else 'snp'})" if best else ""))
print("\nsummary:", dict(near))
