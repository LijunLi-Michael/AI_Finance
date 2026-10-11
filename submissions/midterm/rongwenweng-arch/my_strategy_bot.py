"""my_strategy_bot.py — CrossFamilyRouter (Track B mid-term, Rongwen Weng).

IDEA
  The arena quotes MAX/tUSDC on FOUR venues that belong to two separate "families":
      flash-demo AMMs   : CHEAP, DEAR      (SimpleAMM, you call the pool directly)
      Uniswap-v2 style  : PoolA, PoolB     (you go through RouterA / RouterB)
  The provided bots only arbitrage INSIDE a family (swap-arb: CHEAP<->DEAR,
  dex-arb: PoolA<->PoolB). Nobody connects the two families, so a gap BETWEEN them
  just sits there. This bot treats all four as one market:

    scan()  read all 4 venues, try every ordered (buy venue, sell venue) pair,
            size each with the closed-form optimum for two constant-product pools,
            cap by my own tUSDC balance, keep the pair with the highest net profit.
    fire()  leg 1: buy MAX on the cheapest venue.
            leg 2: RE-ROUTE — re-read the chain and sell on whichever venue pays the
            most right now (the gap may have moved between my two transactions).

  Every round uses my whole tUSDC balance, so profit compounds into the next round.

RUN (from week-03/code/lab-bot/)
    python run.py my_strategy_bot              # DRY-RUN (scan only, safe)
    python run.py my_strategy_bot --live       # LIVE (needs AGENT_KEY)
  Dry-run works without a key: set AGENT_ADDR=0x... to size against a real wallet.
"""
import os
import sys
import time
from math import isqrt
from web3 import Web3
from chain import ADDR, at, erc20, send, ensure_allowance, acct_of

NAME = "cross-family-router"
KEY = os.environ.get("AGENT_KEY")            # my wallet's key — only needed for --live
ME = acct_of(KEY).address if KEY else os.environ.get("AGENT_ADDR")
if ME:
    ME = Web3.to_checksum_address(ME.lower())

WAD = 10 ** 18
G, T = 9970, 10000                           # 0.3% swap fee on every venue: keep G/T
MIN_PROFIT = 1 * WAD                         # don't fire for less than 1 tUSDC
MIN_EDGE_BPS = 20                            # ...or for less than 0.20% of the trade size
SLIPPAGE_BPS = 100                           # router legs revert if I get <99% of my quote
DRY_SIZE = 1_000 * WAD                       # sizing cap when no wallet is known (dry-run)

# name -> (kind, pool address key, router address key or None)
VENUES = {
    "CHEAP": ("amm", "CHEAP", None),
    "DEAR":  ("amm", "DEAR", None),
    "PoolA": ("pair", "PoolA", "RouterA"),
    "PoolB": ("pair", "PoolB", "RouterB"),
}
_MAX_IS_T0 = {}                              # cache: is MAX token0 of this pool?


def _max_is_token0(v):
    if v not in _MAX_IS_T0:
        kind, pool, _ = VENUES[v]
        c = at(ADDR[pool], "SimpleAMM" if kind == "amm" else "Pair")
        _MAX_IS_T0[v] = c.functions.token0().call().lower() == ADDR["MAX"].lower()
    return _MAX_IS_T0[v]


def _reserves(v):
    """(MAX reserve, tUSDC reserve) of a venue, whichever way round the pool stores them."""
    kind, pool, _ = VENUES[v]
    if kind == "amm":
        c = at(ADDR[pool], "SimpleAMM")
        r0, r1 = c.functions.reserve0().call(), c.functions.reserve1().call()
    else:
        r0, r1 = at(ADDR[pool], "Pair").functions.getReserves().call()
    return (r0, r1) if _max_is_token0(v) else (r1, r0)


def _out(amount_in, r_in, r_out):
    """Constant-product quote with the 0.3% fee — same formula the contracts use."""
    a = amount_in * G
    return a * r_out // (r_in * T + a)


def _optimal_in(buy, sell):
    """Best tUSDC size for: buy MAX on `buy` (m1,u1), sell it on `sell` (m2,u2).

    Chaining the two swaps gives   usd_out(D) = a*D / (b + c*D)   with
        a = G^2*m1*u2,   b = T^2*m2*u1,   c = G*T*m2 + G^2*m1
    Profit usd_out(D) - D peaks where d(usd_out)/dD = 1, i.e.  D* = (sqrt(a*b) - b) / c.
    a <= b means the gap is smaller than the two fees: no trade.
    """
    (m1, u1), (m2, u2) = buy, sell
    a, b, c = G * G * m1 * u2, T * T * m2 * u1, G * T * m2 + G * G * m1
    return (isqrt(a * b) - b) // c if a > b else 0


def _round_trip(D, buy, sell):
    (m1, u1), (m2, u2) = buy, sell
    return _out(_out(D, u1, m1), m2, u2)


def _budget():
    if not ME:
        return DRY_SIZE
    return erc20("tUSDC").functions.balanceOf(ME).call()


def scan():
    R = {v: _reserves(v) for v in VENUES}
    px = {v: R[v][1] / R[v][0] for v in VENUES}                 # tUSDC per MAX
    budget = _budget()
    best = None
    for b in VENUES:
        for s in VENUES:
            if b == s:
                continue
            D = min(_optimal_in(R[b], R[s]), budget)             # can't trade more than I hold
            if D <= 0:
                continue
            profit = _round_trip(D, R[b], R[s]) - D
            if best is None or profit > best["profit_wei"]:
                best = {"buy": b, "sell": s, "size_wei": D, "profit_wei": profit}
    prices = " ".join(f"{v} {px[v]:.0f}" for v in VENUES)
    if best is None:
        return {"hit": False, "line": f"{prices} | no gap wider than fees"}
    D, p = best["size_wei"], best["profit_wei"]
    hit = p >= MIN_PROFIT and p * 10000 >= D * MIN_EDGE_BPS
    gap = (px[best["sell"]] / px[best["buy"]] - 1) * 100
    return {"hit": hit, "buy": best["buy"], "sell": best["sell"], "gap": gap,
            "size_wei": D, "size": D / WAD, "profit": p / WAD,
            "line": f"{prices} | buy {best['buy']} -> sell {best['sell']} gap {gap:.2f}% "
                    f"| size {D/WAD:,.0f} | est {p/WAD:+,.2f} tUSDC"}


def _buy_max(v, usd_in, min_out):
    kind, pool, router = VENUES[v]
    if kind == "amm":
        ensure_allowance("tUSDC", ADDR[pool], key=KEY)
        c = at(ADDR[pool], "SimpleAMM")       # MAX is token0 here, so tUSDC -> MAX is 1For0
        fn = c.functions.swap1For0(usd_in) if _max_is_token0(v) else c.functions.swap0For1(usd_in)
        return send(fn, key=KEY)
    ensure_allowance("tUSDC", ADDR[router], key=KEY)
    return send(at(ADDR[router], "Router").functions.swapExactTokensForTokens(
        usd_in, min_out, ADDR["tUSDC"], ADDR["MAX"], ME), key=KEY)


def _sell_max(v, max_in, min_out):
    kind, pool, router = VENUES[v]
    if kind == "amm":
        ensure_allowance("MAX", ADDR[pool], key=KEY)
        c = at(ADDR[pool], "SimpleAMM")
        fn = c.functions.swap0For1(max_in) if _max_is_token0(v) else c.functions.swap1For0(max_in)
        return send(fn, key=KEY)
    ensure_allowance("MAX", ADDR[router], key=KEY)
    return send(at(ADDR[router], "Router").functions.swapExactTokensForTokens(
        max_in, min_out, ADDR["MAX"], ADDR["tUSDC"], ME), key=KEY)


def _wait_change(token, before, tries=12):
    """Public RPCs can lag a block behind my own tx — poll until the balance moves."""
    now = before
    for _ in range(tries):
        now = token.functions.balanceOf(ME).call()
        if now != before:
            break
        time.sleep(0.5)
    return now


def fire(s):
    if not KEY:
        raise RuntimeError("set AGENT_KEY to go --live")
    usdc, mx = erc20("tUSDC"), erc20("MAX")
    u_before = usdc.functions.balanceOf(ME).call()
    m_before = mx.functions.balanceOf(ME).call()
    D = min(s["size_wei"], u_before)

    # leg 1: buy MAX on the cheap venue (re-quoted now, with a slippage floor)
    m1, u1 = _reserves(s["buy"])
    floor = _out(D, u1, m1) * (10000 - SLIPPAGE_BPS) // 10000
    r1 = _buy_max(s["buy"], D, floor)
    got_max = _wait_change(mx, m_before) - m_before
    if got_max <= 0:
        raise RuntimeError("buy landed but MAX balance still stale — not selling")
    u_mid = _wait_change(usdc, u_before)

    # leg 2: re-route — sell on whichever venue pays the most at THIS moment
    quotes = {}
    for v in VENUES:
        m, u = _reserves(v)
        quotes[v] = _out(got_max, m, u)
    sell_v = max(quotes, key=quotes.get)
    r2 = _sell_max(sell_v, got_max, quotes[sell_v] * (10000 - SLIPPAGE_BPS) // 10000)
    u_final = _wait_change(usdc, u_mid)
    return {"tx": r2.transactionHash.hex(), "buy_tx": r1.transactionHash.hex(),
            "profit": (u_final - u_before) / WAD,
            "note": f"bought {got_max/WAD:.4f} MAX on {s['buy']}, sold on {sell_v}"}


if __name__ == "__main__":
    s = scan()
    print(f"[{NAME}] {s['line']} -> {'HIT' if s['hit'] else 'skip'}")
    if s["hit"] and "--live" in sys.argv:
        print("  firing...", fire(s))
