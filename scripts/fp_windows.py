import glob, sys
from collections import Counter
import pysam
run = sys.argv[1]
vf = pysam.VariantFile(glob.glob(f"{run}/happy_*.vcf.vcf.gz")[0])
fp, tp = Counter(), Counter()
W = 50_000
for r in vf:
    q = r.samples["QUERY"]
    bd = q.get("BD")
    if bd == "FP": fp[r.pos // W] += 1
    elif bd == "TP": tp[r.pos // W] += 1
tot = sum(fp.values())
rows = sorted(fp.items(), key=lambda x: -x[1])
cum = 0
print(f"FP total {tot}, windows with FP: {len(fp)} of {len(set(fp)|set(tp))} ({W//1000} kb)")
for i, (w, n) in enumerate(rows[:15]):
    cum += n
    print(f"{w*W:>11,}  FP {n:4d}  TP {tp[w]:4d}  ratio {n/max(1,tp[w]):.2f}  cum {cum/tot:.0%}")
# share of FPs in windows where FP > TP
bad = [w for w in fp if fp[w] > tp[w]]
print("windows FP>TP:", len(bad), "hold", sum(fp[w] for w in bad), "FP and", sum(tp[w] for w in bad), "TP")
