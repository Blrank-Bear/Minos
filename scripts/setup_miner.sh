#!/usr/bin/env bash
# Non-interactive Minos (SN107) miner setup for WSL. No wallet, no TAO.
#
# Everything lives under the project folder:
#   .venv/                       Python environment
#   .cache/pip/                  pip download cache
#   state/                       miner ledgers + scoring-version state
#   minos_subnet/datasets/       reference data (gitignored by the repo)
#   minos_subnet/.env            miner settings (gitignored by the repo)
# Docker images are the one exception: they live in Docker's own data root.
#
# Usage: bash scripts/setup_miner.sh [step...]
#   steps: venv images reference env verify   (default: all, in that order)
#   CHROMS="chr11 chr12" overrides which chromosomes get reference data.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="$ROOT/minos_subnet"
VENV="$ROOT/.venv"
STATE="$ROOT/state"
REF_BASE="https://api.theminos.ai/reference"
CHROMS="${CHROMS:-$(echo chr{1..22})}"
SDF_FILES="done mainIndex nameIndex0 namedata0 namepointer0 progress seqdata0 seqpointer0 sequenceIndex0 summary.txt"
IMAGES=(
  "broadinstitute/gatk:4.5.0.0"
  "quay.io/biocontainers/samtools:1.20--h50ea8bc_0"
  "quay.io/biocontainers/bcftools:1.20--h8b25389_0"
  "genonet/hap-py@sha256:03acabe84bbfba35f5a7234129d524c563f5657e1f21150a2ea2797f8e6d05f2"
)

export PIP_CACHE_DIR="$ROOT/.cache/pip"
log() { printf '\n[%s] %s\n' "$(date +%H:%M:%S)" "$*"; }

step_venv() {
  log "Python venv at $VENV"
  [ -x "$VENV/bin/python" ] || python3 -m venv "$VENV" || python3 -m venv --copies "$VENV"
  "$VENV/bin/python" -m pip install -q --upgrade pip wheel
  "$VENV/bin/python" -m pip install -q -r "$REPO/requirements.txt"
  "$VENV/bin/python" -c "import bittensor, pysam; print('bittensor', bittensor.__version__, '| pysam', pysam.__version__)"
}

step_images() {
  for img in "${IMAGES[@]}"; do
    log "docker pull $img"
    docker pull -q "$img"
  done
}

fetch() {  # fetch URL DEST — skip if present and non-empty, else download atomically
  local url="$1" dest="$2"
  [ -s "$dest" ] && return 0
  mkdir -p "$(dirname "$dest")"
  curl -fsSL --retry 3 --retry-delay 5 -o "$dest.part" "$url" && mv "$dest.part" "$dest"
}

step_reference() {
  log "Reference data for: $CHROMS"
  local d
  for c in $CHROMS; do
    d="$REPO/datasets/reference/$c"
    for ext in fa fa.fai dict; do fetch "$REF_BASE/$c/$c.$ext" "$d/$c.$ext"; done
    # RTG SDF: needed by hap.py for local self-scoring (--score / --practice).
    for f in $SDF_FILES; do fetch "$REF_BASE/$c/$c.sdf/$f" "$d/$c.sdf/$f"; done
    echo "  $c ok ($(du -sh "$d" | cut -f1))"
  done
}

step_env() {
  mkdir -p "$STATE"
  if [ -f "$REPO/.env" ]; then
    log ".env already exists; leaving it unchanged"
    return 0
  fi
  log "Writing $REPO/.env"
  cp "$REPO/.env.miner.example" "$REPO/.env"
  cat >> "$REPO/.env" <<EOF

# --- Local paths: keep all miner state inside the project folder ---
MINOS_COMMITMENT_LEDGER=$STATE/commitments.jsonl
MINOS_PAYMENT_LEDGER=$STATE/submission_payments.jsonl
MINOS_SCORING_VERSION_STATE=$STATE/scoring_version.json
EOF
}

step_verify() {
  log "Verification"
  cd "$REPO"
  "$VENV/bin/python" - <<'EOF'
import sys
sys.path.insert(0, ".")
from templates.tool_params import validate_and_build_flags
from utils.config_loader import extract_tool_options
for tool in ("gatk", "bcftools"):
    opts = extract_tool_options(tool)
    r = validate_and_build_flags(tool, opts)
    print(f"{tool}.conf: {len(opts)} params, valid={r['valid']}", r.get("errors") or "")
EOF
  for img in "${IMAGES[@]}"; do
    docker image inspect "$img" >/dev/null 2>&1 && echo "image ok: $img" || echo "image MISSING: $img"
  done
  curl -fsS --max-time 15 https://api.theminos.ai/health && echo
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(venv images reference env verify)
for s in "${steps[@]}"; do "step_$s"; done
log "Done: ${steps[*]}"
