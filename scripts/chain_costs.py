#!/usr/bin/env python3
"""Read-only check of what mining on SN107 costs right now. No wallet needed.

Prints the registration (recycle) fee, slot usage, immunity period, and the
transaction fee of one Minos config-commitment extrinsic. The fee is estimated
with chain payment_info on a throwaway keypair; nothing is signed or submitted.

Usage (inside WSL, from the project root):
  .venv/bin/python scripts/chain_costs.py [--netuid 107] [--network finney]
"""
import argparse
import hashlib
import sys
import time

ROUNDS_PER_DAY = 20  # 72-minute rounds


def connect(network: str, attempts: int = 3):
    import bittensor as bt

    for i in range(attempts):
        try:
            return bt.Subtensor(network=network)
        except Exception as e:  # noqa: BLE001 - websocket handshakes time out now and then
            if i == attempts - 1:
                raise
            print(f"connect failed ({e}); retrying...", file=sys.stderr)
            time.sleep(5)


def commitment_fee_rao(st, netuid: int) -> int:
    from bittensor_wallet import Keypair

    # Same shape as minos_subnet/utils/config_commit.chain_payload.
    payload = "m1:" + hashlib.sha256(b"round").hexdigest()[:8] + ":" + hashlib.sha256(b"cfg").hexdigest()
    call = st.substrate.compose_call(
        call_module="Commitments",
        call_function="set_commitment",
        call_params={"netuid": netuid, "info": {"fields": [[{f"Raw{len(payload)}": payload.encode()}]]}},
    )
    info = st.substrate.get_payment_info(call=call, keypair=Keypair.create_from_uri("//fee-estimate"))
    return int(info["partial_fee"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--netuid", type=int, default=107)
    ap.add_argument("--network", default="finney")
    args = ap.parse_args()
    sys.argv = sys.argv[:1]  # bittensor parses argv at import time

    st = connect(args.network)
    print(f"registration fee (recycle): {st.recycle(args.netuid)}")
    print(f"registered neurons: {len(st.metagraph(args.netuid).hotkeys)}")
    print(f"immunity period: {st.immunity_period(args.netuid)} blocks (~12 s each)")
    fee = commitment_fee_rao(st, args.netuid)
    print(f"commitment extrinsic fee: {fee} rao = {fee / 1e9:.9f} TAO "
          f"(x{ROUNDS_PER_DAY}/day = {ROUNDS_PER_DAY * fee / 1e9:.9f} TAO)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
