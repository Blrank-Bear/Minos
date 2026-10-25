#!/usr/bin/env python3
"""Minimal client for the public Minos MCP server (https://mcp.theminos.ai/mcp).

Read-only public subnet data: round regions, per-round leaderboards, miner
history. No auth. Prints the tool result as JSON.

Usage:
  .venv/bin/python scripts/minos_mcp.py tools
  .venv/bin/python scripts/minos_mcp.py list_recent_rounds limit=30
  .venv/bin/python scripts/minos_mcp.py get_leaderboard round_id=2026-10-25T04:58:00+00:00 top=10
"""
import json
import sys

import httpx

URL = "https://mcp.theminos.ai/mcp"
PROTOCOL = "2025-06-18"


class MinosMCP:
    def __init__(self, timeout: float = 60.0):
        self.http = httpx.Client(timeout=timeout)
        self.headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        self._id = 0
        init = self._rpc("initialize", {
            "protocolVersion": PROTOCOL, "capabilities": {},
            "clientInfo": {"name": "minos-miner-tools", "version": "0.1"},
        })
        self.server = init.get("serverInfo", {})
        self._notify("notifications/initialized")

    def _post(self, payload: dict) -> httpx.Response:
        r = self.http.post(URL, json=payload, headers=self.headers)
        r.raise_for_status()
        sid = r.headers.get("mcp-session-id")
        if sid:
            self.headers["mcp-session-id"] = sid
            self.headers["mcp-protocol-version"] = PROTOCOL
        return r

    def _notify(self, method: str) -> None:
        self._post({"jsonrpc": "2.0", "method": method})

    def _rpc(self, method: str, params: dict | None = None) -> dict:
        self._id += 1
        r = self._post({"jsonrpc": "2.0", "id": self._id, "method": method, "params": params or {}})
        body = r.text
        if "text/event-stream" in r.headers.get("content-type", ""):
            body = next(l[len("data: "):] for l in body.splitlines() if l.startswith("data: "))
        msg = json.loads(body)
        if "error" in msg:
            raise RuntimeError(f"{method}: {msg['error']}")
        return msg["result"]

    def tools(self) -> list:
        return self._rpc("tools/list")["tools"]

    def call(self, name: str, **arguments):
        res = self._rpc("tools/call", {"name": name, "arguments": arguments})
        if res.get("structuredContent") is not None:
            return res["structuredContent"]
        texts = [c.get("text", "") for c in res.get("content", []) if c.get("type") == "text"]
        joined = "\n".join(texts)
        try:
            return json.loads(joined)
        except json.JSONDecodeError:
            return joined


def _parse_arg(kv: str):
    k, _, v = kv.partition("=")
    for conv in (int, float):
        try:
            return k, conv(v)
        except ValueError:
            pass
    if v.lower() in ("true", "false"):
        return k, v.lower() == "true"
    return k, v


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    mcp = MinosMCP()
    if sys.argv[1] == "tools":
        for t in mcp.tools():
            print(f"{t['name']}: {(t.get('description') or '').splitlines()[0]}")
        return 0
    out = mcp.call(sys.argv[1], **dict(_parse_arg(a) for a in sys.argv[2:]))
    print(json.dumps(out, indent=2) if not isinstance(out, str) else out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
