"""TP vs FP calls by sequence context and nearby calls. NOTE: the repeat-length bucket is unreliable (puts ~all calls in rep6-11); the neighbour and GT splits are fine."""
import glob, sys, bisect
from collections import Counter, defaultdict
import pysam
run, ref_path = sys.argv[1], sys.argv[2]
fa = pysam.FastaFile(ref_path)
vf = pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0])
recs = []
for r in vf:
    q = r.samples["QUERY"]; bd = q.get("BD")
    if bd in ("TP", "FP"):
        alt = r.alts[0] if r.alts else r.ref
        kind = "snp" if len(r.ref) == len(alt) == 1 else "indel"
        recs.append((r.chrom, r.pos, bd, kind, str(q.get("GT"))))
pos = [p for _, p, *_ in recs]

def repeat_len(chrom, p):
    s = fa.fetch(chrom, max(0, p - 1), p + 60).upper()
    best = 1
    for k in range(1, 7):
        unit = s[:k]; n = 0
        while s[n * k:(n + 1) * k] == unit: n += 1
        best = max(best, n * k)
    return best

stats = defaultdict(Counter)
for chrom, p, bd, kind, gt in recs:
    rl = repeat_len(chrom, p)
    rb = "rep<6" if rl < 6 else "rep6-11" if rl < 12 else "rep12-24" if rl < 25 else "rep25+"
    i = bisect.bisect_left(pos, p)
    near = min([abs(pos[j] - p) for j in (i - 1, i + 1) if 0 <= j < len(pos)] or [10**9])
    nb = "near<=10" if near <= 10 else "near11-50" if near <= 50 else "isolated"
    stats[(kind, bd)][rb] += 1
    stats[(kind, bd, "n")][nb] += 1
    stats[(kind, bd, "gt")][gt] += 1
for k in sorted(stats, key=str):
    tot = sum(stats[k].values())
    print(k, tot, {a: f"{b/tot:.0%}" for a, b in stats[k].most_common()})
