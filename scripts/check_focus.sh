#!/usr/bin/env bash
# Pause the autopilot after its next finished test, run the sequential 8-round check of
# configs/gatk-focus.conf vs the live configs/gatk-tuned.conf, then resume the autopilot.
#   bash scripts/check_focus.sh <focus_rounds_comma_list> <candidate_name>
cd "$(dirname "$0")/.." || exit 1
rounds="$1"; name="$2"
n0=$(wc -l < data/tune/autopilot_log.jsonl)
while [ "$(wc -l < data/tune/autopilot_log.jsonl)" -le "$n0" ]; do sleep 10; done
curl -s -X POST -m 10 http://localhost:8787/api/autopilot/stop; echo
for i in $(seq 1 90); do st=$(node -e 'const a=JSON.parse(require("fs").readFileSync("data/tune/autopilot.json"));console.log(a.status)'); case $st in stopped|error) break;; esac; sleep 10; done
cp configs/gatk-focus.conf "configs/$name.conf"
MSYS_NO_PATHCONV=1 wsl -d Ubuntu -- bash -c "cd /mnt/d/CODE/Bittensor/Minos/Minos && .venv/bin/python scripts/validate.py configs/$name.conf configs/gatk-tuned.conf --dev-only --workers 1 --out data/tune/validation.json > data/tune/validate.log 2>&1"
tail -2 data/tune/validate.log
curl -s -X POST -m 20 -H 'Content-Type: application/json' -d "{\"focus_round\":\"$rounds\"}" http://localhost:8787/api/autopilot/start; echo
