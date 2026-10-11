# Mid-term strategy notes

**Name:** Rongwen Weng
**GitHub:** rongwenweng-arch
**Wallet:** 0x7Bfe6bef0E8092bf2d829a75Af11dDfd6A7b4140

## Files
- `strategy.py` — the strategy itself: `decide(view)` takes a market snapshot (each venue's
  reserves + my tUSDC balance) and returns the trade to make. No RPC, no wallet; run
  `python strategy.py` for an offline self-check.
- `my_strategy_bot.py` — the on-chain adapter in the arena's `scan()` + `fire()` shape: it
  builds the view, calls `decide(view)`, and sends the transactions. Copy both files into
  `week-03/code/lab-bot/` to run.

## What my strategy does
`cross-family-router` treats the arena's four MAX/tUSDC venues as one market. The provided
bots only arbitrage inside a family (swap-arb: CHEAP↔DEAR, dex-arb: PoolA↔PoolB); mine reads
all four, tries every ordered (buy venue, sell venue) pair, and trades the best one — which in
practice is a pair that crosses the two families (e.g. buy on PoolA, sell on DEAR). After the
buy lands it re-reads the chain and sells on whichever venue pays the most at that moment.

## Why it should make money
The same token has a different price on each venue, and nobody was connecting the Uniswap-v2
pools to the flash-demo AMMs, so the gap between the families stayed open (about 15% when I
wrote this: PoolA ≈ 1750 vs DEAR ≈ 2023 tUSDC per MAX, against only 0.6% of total swap fees).
Buying where MAX is cheap and selling where it is dear captures that difference minus fees.
Size is not a grid search: chaining two constant-product swaps gives
`out(D) = a·D / (b + c·D)`, so profit peaks at `D* = (√(a·b) − b) / c`; I trade
`min(D*, my tUSDC balance)`. Each round uses the whole balance, so profit compounds.

## What would make it lose
- **Not atomic.** Buy and sell are two transactions. If the price moves between them (another
  bot, or the instructor re-skewing a pool) I can end up selling for less than I paid. The
  re-route in leg 2 and the 1% slippage floor on router legs limit this but do not remove it.
  This bit me for real: I stopped the orchestrator while a seventh round was between its two
  legs, so the wallet was left holding 2.1312 MAX and 0 tUSDC. It showed the risk is not
  theoretical, so I added `--unwind <amount>` to sell a stranded leg on whichever venue pays
  the most, and used it to close the position (see Evidence). The price had not moved against
  me, so that round still ended +241.91 tUSDC; had it moved, the same unwind would have
  locked in a loss.
- **The edge closes as I trade.** Every round pushes the cheap pool up and the dear pool down,
  so profit per round shrinks; once the gap is inside ~0.6% fees the bot correctly stops.
- **Competition.** Anyone running the same idea with more capital or a higher gas bid takes
  the gap first, and my leg 1 may then land at a worse price (it reverts on the router pools,
  but the SimpleAMM pools have no min-out, so there I would eat the slippage).
- **Fee assumption.** I assume 0.3% on all four venues; if a router charged more, my estimate
  would be too optimistic (the slippage floor would revert the trade rather than lose money).

## Evidence
- Live run on Base Sepolia, one round: bought 1.2401 MAX on PoolA with 2,193.46 tUSDC, sold it
  on DEAR. Wallet tUSDC went 2,193.46 → 2,500.54, a profit of **+307.08 tUSDC** (the dry-run
  estimate was +307.08).
  - Buy (RouterA, block 47963972): https://sepolia.basescan.org/tx/0x466585f303eac3dc6bb506f6fa7c58d582cd9c15e91a33d5b28d4448ce116cd1
  - Sell (DEAR, block 47963975): https://sepolia.basescan.org/tx/0x7da3974d5f1cbb063aa37231fa9ea2219099ad6221b55cd0d7a58cb7c05045e7
- Then ran it under `orchestrator.py --only my_strategy_bot --live`; the route changes round to
  round as my own trades move the pools (sell txs shown):
  - PoolB → DEAR, +320.88 tUSDC: https://sepolia.basescan.org/tx/0xb319a4885550913443fee41d7a7f211760dd11f891bedf34c884a2736dd06e32
  - PoolA → DEAR, +333.86 tUSDC: https://sepolia.basescan.org/tx/0x23d75d1c26e109d159921a5f2c6293821f75b745650c005e8bbebeb708fd4c72
  - PoolB → DEAR, +309.55 tUSDC: https://sepolia.basescan.org/tx/0x9ac8b21f8976d9ba7599f8c1fead45850a96c37a5d90f54c49a3670e6c5026f3
  - PoolA → DEAR, +318.88 tUSDC: https://sepolia.basescan.org/tx/0xc85ca3b9be89b1a46c72b0922f6b240e59a631f6154208874d887f41500f5b28
  - PoolA → DEAR, +242.90 tUSDC: https://sepolia.basescan.org/tx/0x58d4ac405aedd21c998f0e6ca7640fbb5311b70ea6ab706a9b342deb827a7018
- Orchestrator session total: 5 fires, **+1,526.07 tUSDC**; the gap narrowed from 15.6% to 8.5%
  as I traded, so profit per round was already falling.
- All of the transactions above were sent before I split the decision logic out into
  `strategy.py`; the split moved code between files without changing the math.
- Seventh round, interrupted between its legs and closed with `--unwind 2.1312` (this one ran
  on the split code): sold 2.1312 MAX on DEAR for 4,268.52 tUSDC, +241.91 tUSDC on the round.
  https://sepolia.basescan.org/tx/0x89f0f3d496858237c9831e3520c79d8133f581f52b9aa1af73c2e34e8774fc93
- Wallet over all seven rounds: 2,193.46 → 4,268.52 tUSDC (**+2,075.06**).
- Leaderboard: (attach a screenshot in your Classroom PDF)
