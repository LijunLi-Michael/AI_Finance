# Quant Strategies & Arbitrage

Extension Reading · MB/CSE 599 AI Finance

**A map of how trading strategies actually make money**

In class we wrote three small strategies and pointed them at real venues: a trend-follower, a mean-reverter, and a cash-and-carry. They are tiny on purpose. This reading zooms out and gives you the map they sit on — the common families of quant strategies, and the common arbitrages that financial-engineering desks run. It is a map, not a textbook: each section tells the idea in a few sentences and hands you the door to go deeper.

**How to use it:** read each section's idea first. If it grabs you, open the Further reading links. Every section ends with a question worth chasing. You do not need to read all of it — skim, then dig where you are curious.

**One throughline:** a strategy either bets on where a price is going, or it bets on the relationship between two prices. The first is direction; the second is arbitrage. Almost everything in quant trading is one of those two, and the honest question for both is the same — after fees and execution, is the edge still there? Keep that in your pocket.

**Start with these three**

- [★ Arbitrage — the law of one price (Wikipedia)](https://en.wikipedia.org/wiki/Arbitrage)

- [★ Trend following — ride the move (Wikipedia)](https://en.wikipedia.org/wiki/Trend_following)

- [★ Pairs trade — the classic market-neutral bet (Wikipedia)](https://en.wikipedia.org/wiki/Pairs_trade)

*Direction, direction, and relationship — the three shapes you will see everywhere.*

**I. Betting on direction — trend vs. mean reversion**

**Trend-following (momentum).** The bet: what has been going up keeps going up. You hold while price is above a moving average and step aside when it falls below. It wins rarely but big — a few large trends pay for many small losses — and it behaves like crash insurance, giving up a little in calm markets and cutting the deep drawdowns. Our trend_follow.py is exactly this on a 50-day average.

**Mean-reversion.** The opposite bet: a price that overshoots snaps back. You buy when a short-term oscillator (like RSI(2)) says oversold, and sell when it bounces. It wins often but small — high hit rate, tiny winners — which makes it brutally sensitive to trading costs. Our mean_reversion.py is this.

**The deep point.** These two are not 'good' or 'bad' — they fit different markets. A trending market rewards momentum and punishes reversion; a choppy, range-bound market does the reverse. Choosing a strategy is really a claim about what kind of market you are in.

**🔍 Worth digging into:** if trend-following has a low win rate and mean-reversion has a high one, why can the high-win-rate strategy still lose money overall?

**Further reading:**

- [Momentum in finance (Wikipedia)](https://en.wikipedia.org/wiki/Momentum_(finance))

- [Mean reversion (Wikipedia)](https://en.wikipedia.org/wiki/Mean_reversion_(finance))

- [Moving average — the trend's backbone (Wikipedia)](https://en.wikipedia.org/wiki/Moving_average)

- [RSI — the reversion oscillator (Wikipedia)](https://en.wikipedia.org/wiki/Relative_strength_index)

- [Our code: trend_follow.py & mean_reversion.py](https://github.com/aaron-recompile/AI_Finance/tree/main/week-05/code/strategies)

**II. The third family — market-neutral**

**Don't bet on direction at all.** A market-neutral strategy holds offsetting long and short positions so that if the whole market moves, the two legs cancel. What is left is the bet you actually care about: a relationship between two things. You are no longer asking 'will BTC go up?' — you are asking 'will A outperform B?'

**The classic form: pairs trading.** Find two assets that normally move together (two similar stocks, two exchanges' prices for the same coin). When they drift apart, short the rich one and buy the cheap one, betting the gap closes. Scaled up across hundreds of pairs with statistics, this becomes statistical arbitrage — the engine of many quant funds.

**Why it matters here.** Our cash-and-carry is the simplest market-neutral trade there is: long spot, short the perpetual, equal size, so price moves cancel and you are left collecting the funding. Same idea, cleaner relationship.

**🔍 Worth digging into:** a market-neutral book can lose money even when it is 'right' about every pair — what has to happen for that?

**Further reading:**

- [Market neutral (Wikipedia)](https://en.wikipedia.org/wiki/Market_neutral)

- [Statistical arbitrage (Wikipedia)](https://en.wikipedia.org/wiki/Statistical_arbitrage)

**III. Arbitrage — same thing, two prices**

**The core idea.** Arbitrage is the law of one price with a profit motive: if the same thing trades at two prices, buy the cheap one, sell the dear one, and pocket the gap. Pure arbitrage is riskless in theory; in practice the 'gap' is usually a structural spread you earn for providing a service, and the risk lives in execution. Here are the ones a desk actually runs.

**Cash-and-carry (spot vs. futures/perp).** Buy the spot asset, sell the future or perpetual against it. You lock in the basis (the gap between the two) plus, on a perp, the funding rate — while the two legs cancel each other's price risk. The cost of carry (financing, storage, fees) is what sets the fair gap. This is the trade we ran live in class.

**Cross-exchange & triangular (crypto).** The same coin can cost slightly different amounts on two exchanges, or a loop of three pairs (USD→BTC→ETH→USD) can leave you with more than you started. Bots race to close these in milliseconds.

**Options: put–call parity.** A call and a put on the same strike are tied together by a fixed relationship to the spot and the bond. Break the relationship and there is a riskless trade — which is why the relationship rarely breaks.

**🔍 Worth digging into:** every arbitrage closes the gap it feeds on. So who is on the other side paying you, and why do they keep paying?

**Further reading:**

- [Arbitrage (Wikipedia)](https://en.wikipedia.org/wiki/Arbitrage)

- [Cost of carry — what sets the fair basis (Wikipedia)](https://en.wikipedia.org/wiki/Cost_of_carry)

- [Carry (investment) (Wikipedia)](https://en.wikipedia.org/wiki/Carry_(investment))

- [Triangular arbitrage (Wikipedia)](https://en.wikipedia.org/wiki/Triangular_arbitrage)

- [Put–call parity (Wikipedia)](https://en.wikipedia.org/wiki/Put%E2%80%93call_parity)

- [Our code: cash_and_carry.py (live OKX basis + funding)](https://github.com/aaron-recompile/AI_Finance/tree/main/week-05/code/strategies)

**IV. Why 'arbitrage' is never free**

**The honest floor.** Textbook arbitrage is riskless. Real arbitrage is not. The carry round we ran in class lost money — not because the idea was wrong, but because four fills of fees ate a spread that was already thin. Every real arbitrage carries the same taxes: trading costs, execution risk (the gap can close before you finish), leg risk (one leg fills and the other doesn't, leaving you exposed), capacity (the trade stops working once enough people crowd in), and — for funding trades — the rate can flip and start charging you.

**The takeaway.** The edge in arbitrage is thin and structural, so costs decide everything. You measure it by the week, not the trade, and you respect the floor: on-chain we stay on testnet, on an exchange we stay in demo/paper and use a withdrawal-disabled key.

**🔍 Worth digging into:** if an arbitrage is 'riskless' but stops working once it's crowded, was it ever really free money — or were you being paid to take a risk no one names?

**Three things to take away**

1.  **Direction or relationship.** A strategy either bets on where a price goes (trend, mean-reversion) or on the relationship between two prices (market-neutral, arbitrage). Know which one you are running.

2.  **The shape tells the risk.** Trend = low win-rate, big winners. Reversion = high win-rate, small winners, cost-sensitive. Arbitrage = thin structural edge where costs decide. The payoff shape is the strategy's fingerprint.

3.  **Nothing is free after fees.** The same question judges all of them: once you subtract trading costs and execution, is the edge still there? Usually that is where strategies live or die.

**Before class:** bring one question — pick any strategy above and ask: who is on the other side of this trade, and why are they willing to lose to me?
