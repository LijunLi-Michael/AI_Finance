# ───────────────────────────────────────────────────────────────
# Buyer (Python SDK version) — pay your own /btc-fee service
#   Compare your hand-rolled JS my-pay.js: those 6 steps (hit 402 -> parse -> sign EIP3009 -> assemble envelope -> resend -> read receipt)
#   Here the SDK wraps it all; you just provide a "wallet that can sign" + register the scheme.
# Run:  python buyer.py
# ───────────────────────────────────────────────────────────────
import os
from pathlib import Path
from eth_account import Account
from x402 import x402ClientSync
from x402.mechanisms.evm.signers import EthAccountSigner
from x402.mechanisms.evm.exact.client import ExactEvmScheme
from x402.http.clients.requests import x402_requests

URL = "http://localhost:4031/btc-fee"


def load_private_key() -> str:
    # Prefer the env var; otherwise read the .env in your lab root (PRIVATE_KEY=...)
    pk = os.environ.get("PRIVATE_KEY")
    if pk:
        return pk
    env = Path(__file__).resolve().parent.parent / ".env"
    for line in env.read_text().splitlines():
        if line.strip().startswith("PRIVATE_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("PRIVATE_KEY not found (env var or ../.env)")


# 1) Build a local account from the private key -> wrap it as an x402 signer
account = Account.from_key(load_private_key())
signer = EthAccountSigner(account)
print("Buyer address:", account.address)

# 2) Build the buyer client: register "chain 84532 uses the EVM exact scheme, I'm the signer"
client = x402ClientSync().register("eip155:84532", ExactEvmScheme(signer))

# 3) Get an "auto-paying" requests.Session: on a 402 it auto-signs + pays + resends
session = x402_requests(client)

# 4) Just request — paywall, signing, settlement all done by the SDK behind the scenes
print("\nRequesting", URL, "...")
r = session.get(URL)
print("Final status:", r.status_code, r.reason)
print("Got data:", r.text)

# 5) Read the settlement receipt (with on-chain tx hash), proving the money really moved
import base64, json
for h in ("x-payment-response", "payment-response"):
    v = r.headers.get(h)
    if v:
        try:
            print("\nSettlement receipt:", json.dumps(json.loads(base64.b64decode(v)), ensure_ascii=False))
        except Exception:
            print("\nSettlement receipt (raw):", v)
        break
