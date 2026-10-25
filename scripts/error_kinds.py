#!/usr/bin/env python3
"""Break a kept run's FNs and FPs down by what went wrong (hap.py match kinds).

For every hap.py record: TRUTH BD/BK and QUERY BD/BK. An FN with a query call
at the same record is a genotype/allele error (BK am/lm), an FN with no query
call is a missed variant. Same for FPs: with a truth record = genotype error,
without = extra call. Prints counts per difficulty class.

Usage: .venv/bin/python scripts/error_kinds.py data/analysis/<kept_run>
"""
import glob
import sys
from collections import Counter

import pysam

run = sys.argv[1]
vf = pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0])


def klass(ref, alts):
    alt = alts[0] if alts else ref
    n = abs(len(ref) - len(alt))
    return "snp" if n == 0 else "ind1" if n == 1 else "ind2-3" if n <= 3 else "ind4+"


kinds = Counter()
for r in vf:
    t, q = r.samples["TRUTH"], r.samples["QUERY"]
    tbd, qbd = t.get("BD"), q.get("BD")
    tgt, qgt = t.get("GT"), q.get("GT")
    cls = klass(r.ref, r.alts)
    has_q = qgt is not None and any(a not in (None, 0) for a in qgt)
    has_t = tgt is not None and any(a not in (None, 0) for a in tgt)
    if tbd == "FN":
        kinds[("FN", "genotype/allele (called)" if has_q else "missed (no call)", cls, t.get("BK") or ".")] += 1
    if qbd == "FP":
        kinds[("FP", "genotype/allele (truth here)" if has_t else "extra call", cls, q.get("BK") or ".")] += 1

for side in ("FN", "FP"):
    print(f"\n{side}:")
    tot = sum(v for k, v in kinds.items() if k[0] == side)
    by_kind = Counter()
    for k, v in kinds.items():
        if k[0] == side:
            by_kind[(k[1], k[2])] += v
    for (kind, cls), v in sorted(by_kind.items(), key=lambda kv: -kv[1]):
        print(f"  {v:5d}  {100 * v / tot:5.1f}%  {kind:<30} {cls}")
