# Bonus Lab — Trade on our three exchanges (Spot / Perp / Prediction)

**Optional, extra credit. No due date — do it whenever.**

Three live exchanges, all built from the same matching engine we study in class. They're
**live and shared** — everyone trades on the same order book. No install, no login to start;
just open them in a browser.

- 🟢 **Spot CEX** — https://ai-finance.tail6afcc7.ts.net/
- 🟣 **Perpetual futures** — https://ai-finance.tail6afcc7.ts.net:8443/
- 🔵 **Prediction market** — https://ai-finance.tail6afcc7.ts.net:10000/

## What to do

1. Open all three. Do at least one action on each: place a spot order, open a long/short on
   the perp, and buy YES or NO on the prediction market.
2. Take **one screenshot of each** after you've traded on it.
3. Write **2–3 sentences of feedback**: what confused you, what broke, what you'd add.

I'm not grading your P&L — I want you to *feel* how an order book, leverage & liquidation,
and "a price = a probability" actually work, and to **break things so I can fix them**.
Finding a real bug and reporting it clearly earns the most credit.

## Submit (same as the mid-term — via a Pull Request)

```
submissions/lab-exchanges/
  <your-github-username>/      <- you create this, put your work here
    spot.png
    perp.png
    prediction.png
    FEEDBACK.md
  _TEMPLATE/                   <- copy this to start; do NOT edit _TEMPLATE itself
```

1. Copy `_TEMPLATE/FEEDBACK.md` into `submissions/lab-exchanges/<your-github-username>/`.
2. Add your three screenshots (`spot.png`, `perp.png`, `prediction.png`) and fill in
   `FEEDBACK.md`.
3. Commit and open a **Pull Request**.

**Rules:** only add files under your own folder · don't edit `_TEMPLATE/` or anyone else's
folder · never commit a private key · keep the diff to your folder. We review in the PR and
don't merge into the reference code — your folder is yours.

## Notes

- The `:8443` and `:10000` URLs use non-standard ports; if your network blocks them, try a
  phone hotspot / another network and tell the instructor.
- It's a **testnet sandbox** — play freely, no real money at risk.
