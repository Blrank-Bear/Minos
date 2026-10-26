#!/usr/bin/env bash
# Bring the mining workspace back after WSL restarts (run inside WSL, in a terminal):
#   bash /mnt/d/CODE/Bittensor/Minos/Minos/scripts/resume_all.sh
# 1. starts Docker (asks for your sudo password; WSL here has no systemd),
# 2. starts the dashboard (http://localhost:8787),
# 3. resumes the autopilot from its saved state (best config, history, caches).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1

if ! docker info >/dev/null 2>&1; then
  echo "Starting Docker (sudo password needed)..."
  sudo service docker start || { echo "Docker did not start"; exit 1; }
  for _ in $(seq 1 30); do docker info >/dev/null 2>&1 && break; sleep 1; done
fi
docker info >/dev/null 2>&1 && echo "Docker: up" || { echo "Docker: still down"; exit 1; }

if ! pgrep -f "python dashboard/server.py" >/dev/null; then
  setsid nohup .venv/bin/python dashboard/server.py >> data/dashboard.log 2>&1 < /dev/null &
  for _ in $(seq 1 20); do curl -s -m 2 http://localhost:8787/api/jobs >/dev/null && break; sleep 1; done
fi
curl -s -m 2 http://localhost:8787/api/jobs >/dev/null && echo "Dashboard: up at http://localhost:8787" || echo "Dashboard: not responding"

if ! pgrep -f "scripts/autopilot.py" >/dev/null; then
  curl -s -m 10 -X POST http://localhost:8787/api/autopilot/start -H 'Content-Type: application/json' \
       -d '{"workers":10,"mode":"single"}' && echo
fi
echo "Autopilot: $(pgrep -f scripts/autopilot.py >/dev/null && echo running || echo NOT running)"
