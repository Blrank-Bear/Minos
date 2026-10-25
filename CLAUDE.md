# Minos (Bittensor SN107) mining workspace

## Rules
- Keep all work inside this folder: session data, temp files (`.tmp/`), caches (`.cache/`), miner state (`state/`). Do not use the system temp dir or the scratchpad.
- Commit to git after each completed change in this repo.
- Never create wallets, register, stake or transfer TAO without the user's explicit go-ahead.

## Layout
- `minos_subnet/` – upstream clone of minos-protocol/minos_subnet. Gitignored here; keep it unmodified so `git pull` / auto-update work.
- `scripts/` – our tooling (setup, round fetching, offline scoring). Run inside WSL (Ubuntu) from the project root.
- `.venv/` – Python env (bittensor 10.3.1) used by the scripts.
- `state/` – miner ledgers and scoring-version state (paths set in `minos_subnet/.env`).
- `data/rounds/` – revealed past rounds (BAM, truth, mutations) for offline tuning; fetched by `scripts/fetch_rounds.sh`.
  `meta.json` per round (exact region + finalized leaderboard) comes from `scripts/fetch_round_meta.py`,
  which uses the public Minos MCP server via `scripts/minos_mcp.py`.

## Running things
Windows host; tools run in WSL. From Git Bash use `MSYS_NO_PATHCONV=1 wsl -d Ubuntu -- bash <script>`;
put multi-step shell work in a script file rather than inline `wsl ... -c "..."` (quoting breaks).
