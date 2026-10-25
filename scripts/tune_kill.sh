#!/usr/bin/env bash
# Stop the tuner immediately (run inside WSL): its process group, then any
# caller/hap.py containers it left running. Finished replays stay cached, so
# `tune.py --resume` picks up where it left off. For a graceful stop that
# finishes the current candidate, use the dashboard's Stop button instead.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pid=$("$ROOT/.venv/bin/python" -c "import json;print(json.load(open('$ROOT/data/tune/state.json')).get('pid',''))" 2>/dev/null)
if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
  kill -TERM -- "-$(ps -o pgid= -p "$pid" | tr -d ' ')" 2>/dev/null
  echo "sent SIGTERM to tuner process group (pid $pid)"
  sleep 3
fi
left=$(docker ps -q --filter "name=minos-")
[ -n "$left" ] && docker rm -f $left >/dev/null && echo "removed $(echo "$left" | wc -l) leftover container(s)"
"$ROOT/.venv/bin/python" - "$ROOT/data/tune/state.json" <<'EOF'
import json, sys
p = sys.argv[1]
s = json.load(open(p))
if s.get("status") in ("running", "starting", "stopping"):
    s["status"] = "stopped"
    s["current"] = None
    json.dump(s, open(p, "w"), indent=2)
print("tuner state:", s.get("status"))
EOF
