#!/usr/bin/env python3
"""Attach public round metadata to downloaded rounds, from the Minos MCP server.

For each data/rounds/<dir>/ (made by fetch_rounds.sh) writes meta.json with:
  * the round's exact region (rounds' verification records omit it),
  * the finalized leaderboard: every scored miner's rank, combined_final,
    SNP/indel scores, tool and weight.

Rounds that are not finalized with identities revealed yet are re-fetched on
the next run; finalized ones are left alone.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/fetch_round_meta.py [--refresh]
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from minos_mcp import MinosMCP  # noqa: E402

ROUNDS = Path(__file__).resolve().parent.parent / "data" / "rounds"
LEADERBOARD_TOP = 256  # more than the subnet has miners
KEEP = ("rank", "uid", "hotkey", "combined_final", "snp_final", "indel_final",
        "weight", "eligible", "validator_count", "tool_name")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refresh", action="store_true", help="re-fetch even finalized rounds")
    args = ap.parse_args()

    mcp = MinosMCP()
    for rd in sorted(p for p in ROUNDS.iterdir() if (p / "round.json").exists()):
        meta_path = rd / "meta.json"
        if meta_path.exists() and not args.refresh:
            old = json.loads(meta_path.read_text())
            if old.get("finalized") and old.get("leaderboard"):
                print(f"{rd.name}: cached ({old['region']}, {len(old['leaderboard'])} scored)")
                continue
        round_id = json.loads((rd / "round.json").read_text())["round_id"]
        summary = mcp.call("get_round_summary", round_id=round_id)
        board = mcp.call("get_leaderboard", round_id=round_id, top=LEADERBOARD_TOP)
        entries = [{k: e.get(k) for k in KEEP} for e in board.get("leaderboard") or []]
        meta = {
            "round_id": round_id,
            "region": summary.get("region"),
            "chromosome": summary.get("chromosome"),
            "submission_count": summary.get("submission_count"),
            "scored_submission_count": summary.get("scored_submission_count"),
            "finalized": bool(summary.get("is_finalized") and board.get("identity_revealed") and entries),
            "leaderboard": entries,
        }
        meta_path.write_text(json.dumps(meta, indent=2))
        top = entries[0]["combined_final"] if entries else None
        print(f"{rd.name}: {meta['region']} scored={len(entries)} top={top} "
              f"{'final' if meta['finalized'] else 'NOT final yet'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
