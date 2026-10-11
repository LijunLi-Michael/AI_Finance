# x402 — pay-per-call (the "pay" verb)

An agent pays USDC on Base per API call, right inside the HTTP request:

    GET /data  →  402 (price + payTo)  →  sign a USDC payment  →  retry  →  200 + data

No account, no card, no human at the till. The server states a price; the agent decides whether it's worth it, pays, and gets the data — in one round trip.

## Files

- **`x402_agent.py`** — run this first, **no setup needed**. The paying agent behind a fence:
  it proposes several pay-per-call requests; a signer approves only by rules — per-call cap,
  daily cap, seller allowlist — and rejects the injected / over-cap ones.
      python x402_agent.py
- **`seller.py`** — a paid endpoint (402 → settle → 200). Needs the `x402` SDK.
      uvicorn seller:app --port 4031
- **`buyer.py`** — auto-pays and retries against the seller. Needs the `x402` SDK + testnet USDC;
  reads your key from `PRIVATE_KEY` (env var or `.env`), never hard-coded.
      python buyer.py

**Testnet only.** The fence is the whole point: a malicious server just... asks for more. The caps and the allowlist are what stop the agent from paying it.
