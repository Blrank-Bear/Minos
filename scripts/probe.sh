#!/usr/bin/env bash
# Quick single-round probes: variants of a base config, run in parallel (inside WSL).
#   bash scripts/probe.sh <round_dir_name> <base.conf> "name:key=val,key=val" ["name:..." ...]
# Each probe writes data/analysis/probe-<name>.conf, is replayed with
# validator-identical scoring (2 threads), recorded in results.jsonl with
# label probe-<name>, and its RESULT/PLACEMENT lines are printed.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1
round="$1"; base="$2"; shift 2
mkdir -p data/analysis
for spec in "$@"; do
  name="${spec%%:*}"; edits="${spec#*:}"
  conf="data/analysis/probe-$name.conf"
  cp "$base" "$conf"
  IFS=',' read -ra kvs <<< "$edits"
  for kv in "${kvs[@]}"; do
    k="${kv%%=*}"; v="${kv#*=}"
    if grep -q "^$k=" "$conf"; then sed -i "s|^$k=.*|$k=$v|" "$conf"; else echo "$k=$v" >> "$conf"; fi
  done
  ( .venv/bin/python scripts/score_round.py "data/rounds/$round" --config "$conf" --label "probe-$name" \
      --threads 2 --memory-gb 6 2>&1 | grep -E 'RESULT|PLACEMENT|ERROR' | sed "s/^/[$name] /" ) &
done
wait
