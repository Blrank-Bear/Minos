#!/usr/bin/env python3
"""Why are true SNPs missed? Read evidence at each FN SNP in the round BAM.

For FN SNPs from a kept run's hap.py output: total depth, reads supporting the
truth ALT base, and the base-quality / mapping-quality distribution of those
ALT bases -- i.e. how much ALT evidence survives a given min_base_quality_score
or min_mapping_quality_score. Compared with the same numbers at TP SNPs.

Usage: .venv/bin/python scripts/fn_evidence.py data/analysis/<kept_run> data/rounds/<round>/input.bam
"""
import glob
import statistics
import sys
from collections import Counter

import pysam

run, bam_path = sys.argv[1], sys.argv[2]
bam = pysam.AlignmentFile(bam_path)
fn, tp = [], []
for r in pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0]):
    if len(r.ref) != 1 or not r.alts or len(r.alts[0]) != 1:
        continue
    t = r.samples["TRUTH"]
    if t.get("BD") == "FN":
        fn.append((r.chrom, r.pos, r.alts[0]))
    elif t.get("BD") == "TP" and len(tp) < 400:
        tp.append((r.chrom, r.pos, r.alts[0]))


def evidence(sites):
    out = []
    for chrom, pos, alt in sites:
        depth, alt_bq, alt_mq = 0, [], []
        for col in bam.pileup(chrom, pos - 1, pos, truncate=True, min_base_quality=0, min_mapping_quality=0,
                              ignore_orphans=False, stepper="nofilter"):
            for pr in col.pileups:
                if pr.is_del or pr.is_refskip:
                    continue
                depth += 1
                if pr.alignment.query_sequence[pr.query_position] == alt:
                    alt_bq.append(pr.alignment.query_qualities[pr.query_position])
                    alt_mq.append(pr.alignment.mapping_quality)
        out.append((depth, alt_bq, alt_mq))
    return out


for name, sites in (("FN SNPs", fn), ("TP SNPs (sample)", tp)):
    ev = evidence(sites)
    if not ev:
        continue
    alt_n = [len(b) for _, b, _ in ev]
    bq_all = [q for _, b, _ in ev for q in b]
    mq_all = [q for _, _, m in ev for q in m]
    keep25 = [sum(1 for q in b if q >= 25) for _, b, _ in ev]
    print(f"\n{name}: {len(ev)} sites")
    print(f"  depth median {statistics.median(d for d, _, _ in ev)}   ALT reads median {statistics.median(alt_n)}"
          f"   sites with 0 ALT reads: {sum(1 for n in alt_n if n == 0)}")
    print(f"  ALT base qualities: {Counter(bq_all).most_common(6)}")
    print(f"  ALT reads surviving BQ>=25 per site, median {statistics.median(keep25)}"
          f" (sites left with <2: {sum(1 for k in keep25 if k < 2)})")
    print(f"  ALT mapping qualities: {Counter(mq_all).most_common(5)}")
