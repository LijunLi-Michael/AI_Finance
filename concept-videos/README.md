# AI Finance · Concept Videos

Short, animated **explainer videos** that accompany the whole course — a **full-course companion**, from the very first idea (what a smart contract even *is*) through DeFi, autonomous agents, quant, and derivatives. Each one takes a single concept and makes it visual. Watch them as many times as you need — there's no separate problem set for this unit.

## Watch

- **Online player:** open [`index.html`](./index.html) — on GitHub Pages: **https://aaron-recompile.github.io/AI_Finance/concept-videos/**
- **Offline:** download any file from the [Release](https://github.com/aaron-recompile/AI_Finance/releases/tag/concept-videos-v1) and play it locally.

## Order (by course week)

**W1 · Smart Contracts**
1. **A Contract = a Vending Machine** — poke it, it acts: deterministic, no owner, code is law (even its bugs).

**W2 · DeFi Lego**
2. **What is an AMM** — a `x·y=k` curve plus a pool; the tangent is the spot price, the chord is what you pay, and buying more slips more.
3. **Lending & Liquidation** — over-collateralize, then borrow; a health factor watches you, and below 1 you get liquidated.
4. **Yield Farming** — the protocol prints a reward token; everyone mines, withdraws and dumps, so high APY ≠ real yield.

**W3 · Composability · Arbitrage**
5. **What is Arbitrage** — same thing at two prices; buy low, sell high, and your own trades close the gap.
6. **What is a Flash Loan** — zero collateral, but atomic: repay within one transaction or the whole thing reverts (all-or-nothing).
7. **Bots vs Manual** — the window is milliseconds; a bot wins on speed, not IQ — it's fast hands, the brain is still human-given.

**W4 · From Tool to Agent**
8. **Brain and Hands (Program vs Agent)** — a program is just hands; add a brain and it's an Agent. Put a rule between them: brain proposes, rules approve, hands act, then verify — and the gate blocks prompt injection.

**W5 · Quant — what you can do on a CEX (e.g. OKX)**
9. **Common Quant Strategies** — what are you betting on? four buckets: direction / spread / flow / sizing.
10. **Quant Metrics 101** — how to judge a strategy: drawdown, Sharpe, Calmar (from a real backtest).
11. **What is Cash-and-Carry** — futures must converge, so you lock the basis; up, down or flat, always the same profit.
12. **What is a Perpetual** — spot plus a funding "spring"; never expires, still leveraged.

**W6 · On-chain & a new game**
13. **What is Hyperliquid** — the whole perpetual exchange, on-chain: CEX speed + DEX transparency.
14. **What is Polymarket** — same matching engine, new game: price *is* probability.

**W7 · x402 & Farcaster — pay & speak**
15. **What is x402** — HTTP 402, revived by Coinbase: the agent pays USDC on Base per call, inside the request (GET → 402 → sign → retry → 200), behind a spend fence (per-call cap + daily cap + seller allowlist).
16. **The Agent Economy** — earn → pay → speak; an agent that earns, pays and speaks is an economic actor, not a tool. Pay-per-call is the plumbing Coinbase is building.
17. **What is Farcaster** — on-chain social identity; the agent posts in public what it did, human-gated (draft → preview → `--yes` → posted, sanitized).

**Foundations · overview · the map**
- **Futures & Options Basics** — futures vs options; futures come in two kinds; the call/put × long/short quadrants; binary options.
- **Obligation or Right** — one question sorts every derivative: an obligation is a straight line, a right bends into a kink.
- **Three Anchors** — what pins a contract's price to reality: delivery, funding, or an oracle.

## Notes

- Format: 1920×1080, machine voiceover (no burned-in subtitles).
- Content is **AI-assisted**. Figures in examples are illustrative; the backtest numbers come from a real MA-50 run on BTC daily data, and the flash-loan figures come from the Week-3 lab.
