#!/usr/bin/env bash
# Download revealed Minos rounds (BAM + truth + mutations) for offline tuning.
#
# Usage: bash scripts/fetch_rounds.sh [round_id...]
#   No args: every round the current /verification/task-window lists as drawn.
# Files land in data/rounds/<YYYYMMDDTHHMMSSZ>/, with round.json holding the
# verification record. Downloads are hash-checked. Kept outside minos_subnet/
# so the upstream clone stays clean (its auto-updater skips a dirty tree).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/data/rounds"
API="https://api.theminos.ai"
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY=python3

latest_drawn() {
  curl -fsS --max-time 30 "$API/verification/task-window" | "$PY" -c '
import json, sys
d = json.load(sys.stdin)
print("\n".join(sorted(e["drawn"]["round_id"] for e in d["entries"] if e.get("drawn"))))'
}

if [ $# -eq 0 ]; then
  mapfile -t ids < <(latest_drawn)
elif [ "$1" = "--last" ]; then
  # Rounds run every 72 minutes: step back from the newest drawn round.
  newest=$(latest_drawn | tail -1)
  mapfile -t ids < <("$PY" - "$newest" "${2:?--last needs a count}" <<'EOF'
import sys
from datetime import datetime, timedelta
t = datetime.fromisoformat(sys.argv[1])
for k in range(int(sys.argv[2])):
    print((t - timedelta(minutes=72 * k)).isoformat())
EOF
)
else
  ids=("$@")
fi

for rid in "${ids[@]}"; do
  enc=$("$PY" -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=""))' "$rid")
  rec=$(curl -fsS --max-time 30 "$API/verification/round/$enc") || { echo "skip $rid: no record"; continue; }
  dir=$(echo "$rec" | "$PY" -c '
import json, sys
d = json.load(sys.stdin)
r = d.get("reveal") or {}
print((r.get("prefix") or "").rsplit("/", 1)[-1])')
  if [ -z "$dir" ]; then echo "skip $rid: not revealed yet"; continue; fi
  mkdir -p "$OUT/$dir"
  echo "$rec" > "$OUT/$dir/round.json"
  echo "$rec" | "$PY" -c '
import json, sys
d = json.load(sys.stdin)
for f in d["reveal"]["files"]:
    print(f["name"], f["url"])' | while read -r name url; do
    dest="$OUT/$dir/$name"
    [ -s "$dest" ] && continue
    if curl -fsSL --retry 3 -o "$dest.part" "$url"; then
      mv -f "$dest.part" "$dest"
    else
      echo "  download failed: $name"; rm -f "$dest.part"
    fi
  done
  # Verify the three hashed files.
  "$PY" - "$OUT/$dir" <<'EOF'
import hashlib, json, sys, pathlib
base = pathlib.Path(sys.argv[1])
d = json.loads((base / "round.json").read_text())
names = {"bam": "input.bam", "truth_vcf": "truth.vcf.gz", "mutations_vcf": "mutations.vcf.gz"}
bad = []
for key, name in names.items():
    p = base / name
    want = (d.get("file_hashes") or {}).get(key)
    if not p.exists():
        bad.append(f"{name} missing"); continue
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if want and got != want:
        bad.append(f"{name} sha256 mismatch")
chrom = "?"
if not bad:
    import gzip
    with gzip.open(base / "truth.vcf.gz", "rt") as fh:
        chrom = next(l for l in fh if not l.startswith("#")).split("\t", 1)[0]
print(f"{base.name}: " + (f"ok {chrom}" if not bad else "; ".join(bad)))
EOF
done
