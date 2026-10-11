# Five Interviews Worth Your Time

Supplementary Reading · MB/CSE 599 AI Finance

We've spent this stretch of the course building and trading — order books, AMMs, perpetuals, arbitrage, carry, and agents that do it on their own. Before the final push, step back and listen to five people who actually did this at scale.

**How to use it:** these are long conversations, and you do not need every minute. Each section says why it is worth your time and what to focus on — that focus is the 20% that matters. Watch in any order; #1 and #5 are the shortest ways in.

**One throughline:** none of these hands you a strategy. They hand you the mental models the rest of the course runs on — making vs. taking, funding, skepticism, position sizing, and 'trust the data, not the story.' Keep those five in your pocket as you watch.

**Start with these two**

- [★ Jim Simons — TED 2015 (~23 min): the shortest, clearest 'why quant at all'](https://www.ted.com/talks/jim_simons_a_rare_interview_with_the_mathematician_who_cracked_wall_street)

- [★ Jeff Yan — the founder of the exchange you actually ran code against](https://www.youtube.com/results?search_query=Flirting%20with%20Models%20Jeff%20Yan%20Hyperliquid%20market%20making)

**I. Jeff Yan — the person who built what you studied**

**Flirting with Models (2023), "High-Frequency Crypto Market Making & the Hyperliquid Exchange."** The founder of Hyperliquid, formerly of the HFT firm Hudson River Trading. This is the bridge from market-making in the abstract to the exchange you placed orders on in Week 6.

**Focus on:** making vs. taking — the two sides of every order book — why latency and infrastructure decide who wins, and why he put a full order book on its own chain instead of settling for an AMM. Pair it with our 'What is Hyperliquid' video.

**🔍 Worth digging into:** he chose an on-chain order book over an AMM. From what you learned about AMMs (slippage, LPs) and order books, why would a professional market maker insist on the order book?

**Where to watch:**

- [YouTube search — Flirting with Models · Jeff Yan · Hyperliquid](https://www.youtube.com/results?search_query=Flirting%20with%20Models%20Jeff%20Yan%20Hyperliquid%20market%20making)

- [Flirting with Models (the podcast home)](https://www.flirtingwithmodels.com/)

**II. Arthur Hayes — who made the perpetual a mass product**

**BitMEX founder; look for a long-form interview on perps and leverage.** Perps are now the dominant instrument in crypto — the contract you studied in Week 6. Hayes is the person most responsible for turning them into a product traded by millions, at up to 100x leverage.

**Focus on:** why a contract with no expiry needs funding to stay glued to spot, and what high leverage really does to a book when it moves. A caveat worth teaching: the perpetual concept predates BitMEX — economist Robert Shiller proposed it in the 1990s — but BitMEX made it mainstream.

**🔍 Worth digging into:** funding keeps a perp near spot without any expiry date. If funding is strongly positive for weeks, who is paying whom, and what is that telling you about how crowded one side of the trade is?

**Where to watch:**

- [YouTube search — Arthur Hayes · perpetual swap · interview](https://www.youtube.com/results?search_query=Arthur%20Hayes%20perpetual%20swap%20BitMEX%20interview%20funding)

- [Background: Perpetual futures (how funding works)](https://en.wikipedia.org/wiki/Perpetual_futures)

**III. Sam Bankman-Fried — the cautionary one, watch it critically**

**Bloomberg Odd Lots, 25 April 2022, "SBF on yield farming" (with Matt Levine and Joe Weisenthal).** The most-quoted crypto interview ever. SBF describes a 'box' that does 'literally nothing' yet keeps attracting billions; about twenty-seven minutes in, Matt Levine reacts: 'I'm in the Ponzi business and it's pretty good.' Six months later FTX collapsed in fraud, and SBF was convicted.

**Focus on:** listen to it as a BS-detector exercise. This is the hype machine that blew up — and it is exactly why this course's spine is 'verify, don't trust.' It is the reason Hyperliquid puts every order, fill, and liquidation on-chain where anyone can check. The smartest-sounding story in the room turned out to be a fraud.

**🔍 Worth digging into:** re-listen to the 'box' explanation knowing how it ended. Which specific claims should have been checkable at the time — and which were just vibes you were asked to take on faith?

**Where to watch:**

- [YouTube search — SBF · Odd Lots · yield farming · Matt Levine](https://www.youtube.com/results?search_query=SBF%20Odd%20Lots%20yield%20farming%20Matt%20Levine%20Ponzi)

- [Episode notes & excerpts (life itself)](https://web3.lifeitself.org/notes/sam-bankman-fried-on-yield-farming-with-matt-levine-april-2022)

**IV. Ed Thorp — how much to bet (the one risk lesson)**

**Chat With Traders, "The man who beat the dealer, and later, beat the market."** Thorp beat blackjack with card counting, then ran a hedge fund for decades. He is the father of 'bet size follows your edge.'

**Focus on:** how he defines an edge, and the Kelly idea — bet too little and you barely win even when you are right; bet too much and you are almost certainly ruined. This maps straight onto the position-sizing bucket from our quant videos, and it is the single most useful risk lesson in trading.

**🔍 Worth digging into:** two traders have the same winning edge. One sizes with Kelly, one bets twice Kelly. Over a long run of bets, why does the aggressive one tend to blow up even though every single bet had positive expected value?

**Where to watch:**

- [YouTube search — Ed Thorp · Chat With Traders · Kelly criterion](https://www.youtube.com/results?search_query=Ed%20Thorp%20Chat%20With%20Traders%20Kelly%20criterion%20edge)

**V. Jim Simons — why quant at all (the shortest watch)**

**TED 2015, "A Rare Interview with the Mathematician Who Cracked Wall Street" (~23 min).** Renaissance Technologies' Medallion fund is the best track record in the history of markets. Simons is the patron saint of systematic trading.

**Focus on:** the mindset — patterns over stories, data over opinions, and letting the model decide instead of your gut. The best twenty-three minutes on why we do any of this with numbers in the first place.

**🔍 Worth digging into:** Simons hired code-breakers and physicists, not Wall Street traders. If the edge comes from data and models, what does that say about where an edge will come from in the agent era you are training for?

**Where to watch:**

- [Jim Simons — TED (full talk)](https://www.ted.com/talks/jim_simons_a_rare_interview_with_the_mathematician_who_cracked_wall_street)

**The through-line — five mental models**

1.  **Making vs. taking (Yan).** Every order book has two sides; knowing which one you are on is the start of market structure.

2.  **Funding anchors a perp (Hayes).** No expiry, so a running payment keeps the contract honest to spot — and tells you where the crowd is.

3.  **Verify, don't trust (SBF, the hard way).** The most convincing story can be a fraud; this is why we put everything on-chain where it can be checked.

4.  **Size by your edge (Thorp).** A good edge bet too big still ruins you; position sizing is where trading is won or lost.

5.  **Trust the data, not the story (Simons).** The best record in history came from models and discipline, not opinions.

**Before class**

Pick at least two of the five and come with one question worth chasing — ideally from the 'Worth digging into' prompts. You do not need to watch all five, and you do not need every minute of any of them: the 'Focus on' line in each section is the part that matters.

*A note on the SBF interview: it is included as a cautionary case, not an endorsement. Listen critically — the point is to build the instinct the market lacked in 2022.*
