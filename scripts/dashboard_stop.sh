#!/usr/bin/env bash
# Stop the dashboard server (run inside WSL). A running tuner is left alone.
pids=$(pgrep -f "python dashboard/server.py")
[ -z "$pids" ] && { echo "dashboard not running"; exit 0; }
kill $pids && echo "stopped dashboard ($pids)"
