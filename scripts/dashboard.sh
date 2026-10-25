#!/usr/bin/env bash
# Start the Minos mining dashboard (run inside WSL). Open http://localhost:8787
# in the Windows browser. Extra args go to dashboard/server.py (--port, --host).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" && exec .venv/bin/python dashboard/server.py "$@"
