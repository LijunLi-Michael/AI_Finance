# ───────────────────────────────────────────────────────────────
# Your first real Bitcoin x402 service (Python SDK version)
#   GET /btc-fee  ->  current Bitcoin recommended fee (data from the free mempool.space)
#   Charges $0.001 USDC, on the Base Sepolia testnet (eip155:84532)
#   Compare your JS seller.js: same logic, swapped to the official Python SDK
# Run:  uvicorn seller:app --port 4031      then  curl -i localhost:4031/btc-fee
# ───────────────────────────────────────────────────────────────
import requests
from fastapi import FastAPI
from x402 import x402ResourceServer
from x402.http import HTTPFacilitatorClient
from x402.http.middleware.fastapi import payment_middleware
from x402.mechanisms.evm.exact.server import ExactEvmScheme

app = FastAPI()

# Receiving address: who ultimately gets paid (reusing the seller receiving address from your lab)
PAY_TO = "0xYOUR_TESTNET_RECEIVING_ADDRESS"

# facilitator = the "cashier who verifies the bill". Empty constructor -> defaults to https://x402.org/facilitator (testnet, free)
facilitator = HTTPFacilitatorClient()

# Resource server: register "chain 84532 verifies with EVM's exact scheme" — equivalent to your JS .register(...)
server = x402ResourceServer(facilitator).register("eip155:84532", ExactEvmScheme())

# Which routes charge and how much (only GET /btc-fee charges, the rest are free)
routes = {
    "GET /btc-fee": {
        "accepts": {
            "scheme": "exact",
            "payTo": PAY_TO,
            "price": "$0.001",          # priced in USD, USDC underneath
            "network": "eip155:84532",  # Base Sepolia testnet
        },
        "description": "current Bitcoin recommended fee (sat/vB)",
        "mimeType": "application/json",
    }
}

# Hook the payment middleware into FastAPI: request without payment -> return 402; with valid authorization -> pass to the business logic below
@app.middleware("http")
async def x402_gate(request, call_next):
    return await payment_middleware(routes, server)(request, call_next)


# The actual business logic. Reaching here itself proves "payment has been verified".
@app.get("/btc-fee")
def btc_fee():
    # The data source is the free mempool.space — echoing the lecture line: don't charge for the free data itself,
    # you charge for the convenience of "packaging + being directly pay-per-call by an agent" (this is just practice).
    r = requests.get("https://mempool.space/api/v1/fees/recommended", timeout=8)
    fees = r.json()  # {fastestFee, halfHourFee, hourFee, economyFee, minimumFee} in sat/vB
    return {
        "source": "mempool.space",
        "unit": "sat/vB",
        "recommended": fees,
    }
