"""Distance from each TP/FP query call to the nearest *other* truth record (TP or FN)."""
import glob, sys, bisect
from collections import Counter
import pysam
vf = pysam.VariantFile(glob.glob(f"{sys.argv[1]}/happy_*.vcf.vcf.gz")[0])
truth, calls = [], []
for r in vf:
    t, q = r.samples["TRUTH"].get("BD"), r.samples["QUERY"].get("BD")
    if t in ("TP", "FN"): truth.append(r.pos)
    if q in ("TP", "FP"): calls.append((r.pos, q))
truth.sort()
def bucket(d): return "<=100" if d <= 100 else "101-1k" if d <= 1000 else "1k-5k" if d <= 5000 else ">5k"
c = {"TP": Counter(), "FP": Counter()}
for p, q in calls:
    i = bisect.bisect_left(truth, p)
    ds = [abs(truth[j] - p) for j in (i - 1, i, i + 1) if 0 <= j < len(truth) and truth[j] != p]
    c[q][bucket(min(ds) if ds else 10**9)] += 1
for q, cc in c.items():
    tot = sum(cc.values()); print(q, tot, {k: f"{v/tot:.0%}" for k, v in sorted(cc.items())})
