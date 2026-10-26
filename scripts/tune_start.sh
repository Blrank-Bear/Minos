#!/usr/bin/env bash
# Start (or resume) the tuner detached from this shell (run inside WSL).
# Every new best is deployed as the live miner config (--deploy).
# Extra args go to scripts/tune.py, e.g. --workers 4.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1
mkdir -p data/tune
setsid nohup .venv/bin/python scripts/tune.py --workers 1 --resume --deploy "$@" >> data/tune/tuner.log 2>&1 < /dev/null &
echo "tuner started (pid $!)"
