#!/usr/bin/env bash
# Wait until the autopilot logs its next test, then restart it (picks up code changes, loses no test).
cd "$(dirname "$0")/.." || exit 1
n0=$(wc -l < data/tune/autopilot_log.jsonl)
while [ "$(wc -l < data/tune/autopilot_log.jsonl)" -le "$n0" ]; do sleep 10; done
tail -n 1 data/tune/autopilot_log.jsonl | cut -c1-200
curl -s -X POST -m 10 http://localhost:8787/api/autopilot/stop; echo
for i in $(seq 1 90); do st=$(node -e 'const a=JSON.parse(require("fs").readFileSync("data/tune/autopilot.json"));console.log(a.status)' 2>/dev/null || python3 -c 'import json;print(json.load(open("data/tune/autopilot.json"))["status"])'); case $st in stopped|error) break;; esac; sleep 10; done
echo "status $st"
curl -s -X POST -m 20 -H 'Content-Type: application/json' -d "{\"focus_round\":\"$1\"}" http://localhost:8787/api/autopilot/start; echo
