# Cayman — Options Trading Crash Course (read 2026-11-10, in chat after scheduled run failed)
## loc.1–13
- loc.1–3: front matter, TOC, intro (options as short-term momentum style; plan your patterns in advance). No rules.
- loc.4–5: broker selection (ratings, low commission, simple UI, research tools); test platform; get options approval. Principles only. Evidence: none.
- loc.5: practise on simulated account first (agrees w/ existing demo-account principle). Use limit orders to control entry price (agrees MetaStock limit-entry principle). D.
- loc.6: keep the few strategies that work, drop the ones that don't; learn greeks. D.
- loc.6–7: call/put definitions; options as zero-sum between buyer and writer. Definitions.
- loc.8–10: strategy catalog (covered call, naked call = high risk, married put, bull call / bear put spreads, protective collar, long straddle/strangle when big move expected but direction unknown, butterfly, iron condor, iron butterfly). Descriptions only, no entry conditions or numbers.
- loc.11: worked hypothetical: ATM call, premium all time value 3.50; stock +2.00 → intrinsic +2.00, time decay −3.50 → net −1.50. Long call profits only if the underlying rises enough to beat time decay AND add intrinsic value. Decay speeds up into expiry. → candidate RULE (long-call breakeven vs move). Evidence: hypothetical example → D.
- loc.12: buy calls instead of stock to cap loss at the premium; or to defer a stock purchase (hypothetical $19 call, $1 premium, 5 months). D.
- loc.13: speculative calls: strike close to current price; expiry long enough for the move to outrun decay. No thresholds → principle. D.
- loc.13: naked long options are very risky because of time value/expiry.
## loc.14–26
- loc.14–15: "back spread" chapter actually describes a vertical spread (buy ITM, sell OTM); hypothetical $5.2/$2.7 legs, max profit = max loss = $2.5/unit, breakeven 82.5; full profit only at expiry. Muddled; definitions only.
- loc.15–17: premium = intrinsic + extrinsic; only extrinsic decays; theta largest at the money, speeds up in the last days; hypothetical theta −0.15 → −0.12. Only short options carry positive theta. D (mechanics).
- loc.18: theta/gamma trade-off: a position helped by time is hurt by movement and vice versa. Mechanics.
- loc.18–19: historical vol (realised) vs implied; HV hints at the size of future moves, not direction. D.
- loc.19–20: fundamentals for swing trades: margins, P/E, cash flow; product failure or legal trouble → short/puts; strong launch → long. D, no thresholds.
- loc.20: favour companies that beat analysts' forecasts; author says they tend to keep succeeding (assertion, no data) → candidate RULE earnings-surprise long filter. D.
- loc.20–21: earnings momentum (YoY EPS growth) matters most in bull markets; multi-year earnings growth. D.
- loc.21: revenue trend: steadily rising YoY revenue = healthy; flat/falling revenue → profits and price likely flat/falling; check a long trade is aligned with the revenue trend → candidate RULE. D.
- loc.21–22: earnings ≠ profit (book's own definitions); debt vs equity risk explained; no threshold. Principle-level.
- loc.22–24 weekly options: little time to be right; short weeklies carry high gamma (small move flips OTM→ITM); need tight sizing; IV higher. Selling: lower-priced underlyings use less buying power; high IV more likely to revert within the week (assertion); short puts beat short calls short-term (assertion). Debit spread struck near the current price ≈ 1:1 reward:risk. D throughout.
- loc.24–25: beginners shouldn't run only day-trading option strategies (leverage); part-time day trading discouraged. D.
- loc.25: ideal portfolio 25–30 securities, uncorrelated (assertion; conflicts with R-028 cap of 7). D.
- loc.26: "studies" say pros rarely beat their asset-class index; asset class drives returns; selection+timing ≈ 6% of variance — studies not named → D (unnamed source).
## loc.27–39
- loc.27: correlations between asset classes shift; rebalance out of lagging classes into ones performing; don't let one class get overweight after a long bull run. D.
- loc.28–29 BULL CALL SPREAD: best mid-trend, when the advance is slowing and daily ranges are widening; early in a strong trend just buy the call. Long ATM/OTM call + short OTM call beyond the nearest resistance; both legs ≥30 days to expiry. Adjust: when price clears that resistance, roll the short call up to the next resistance; close both legs if the counter-trend grows too strong. → candidate RULE (options-directional). Evidence: none (assertion) → D.
- loc.29–30 BULL PUT SPREAD: same conditions; long OTM put below strong support + short put near/at the money; net credit; adjust lower / exit if the short put goes in the money. → candidate RULE (options-income). D.
- loc.30–32 INDEX-PUT HEDGE: hedge an equity portfolio with index puts; pick the index that tracks the portfolio (S&P 500 for large caps; Russell 2000 / S&P 400 for small/mid); compare the portfolio to candidate indexes well before hedging. Hypothetical sizing: 60% of $1M in equities, 3% budget for 3 months, ATM index puts → 4 contracts; hedged 5% drop loss ~$9.1k vs ~$47.1k unhedged; hedge drags returns in rallies. Book also makes a 60/40 index-option tax claim → tax is out of scope, flag only. D (hypothetical). Principle (trigger is the owner's wish to hedge, not a market condition).
- loc.32–35: Black-Scholes assumptions; models don't hold exactly in practice (no continuous rebalancing, costs, unknown vol). Author asserts volatility is easier to predict than price. D.
- loc.35 SWING AMPLITUDE: in an uptrend, pullbacks are smaller than up-legs; a pullback larger than the preceding up-leg means the uptrend is challenged → stop buying. Mirror: in a downtrend, a rebound larger than the last down-leg flags a turn. → candidate RULE (swing-technical). D.
- loc.35: "according to Wilder" markets trend ~1/3 of the time (attributed, no data) → D. Momentum bias traps buyers near resistance and sellers near support.
- loc.36: trend line needs ≥2 lows (up) / ≥2 highs (down); a break of a well-tested line is a reversal warning; broken line often retested from the other side; BUT a break alone only warns of consolidation, not reversal. D. → merge candidate with role-reversal retest (R-005) / principle.
- loc.37 CHANNELS: ≥2 touches on each line; a midline often acts as intermediate resistance; in a rising channel, a break above the midline often runs to the top of the channel. → candidate RULE. D.
- loc.37: "various researches" say large, slow-forming reversal patterns precede big corrections (unnamed) → D.
- loc.38–39: stock basics (common vs preferred, auction); income investors → utilities/REITs/MLPs; capital-preservation → blue chips. Definitions.
## loc.40–52
- loc.40: in a weak market look for stocks sliding toward a breakdown to short; don't pile on chart tools; write down total capital and the amount you can put at risk. D.
- loc.41: (names big liquid stocks — not carried into playbook). Day-trading universe: stocks that typically move ≥3% a day or ≥$1.50 a day → candidate RULE (day-trading, universe filter). D. Trade industries you know; consider foreign exchanges. D.
- loc.42–43: leverage example, hypothetical and garbled (premium/strike confused). Not used.
- loc.44–45: broker checks (regulated entity, discount broker for beginners, minimum balance $500–1,000, withdrawal rules, simple fees). Principles. D.
- loc.45: avoid cheap out-of-the-money options; they have far to go and often expire worthless; prefer pricier in-the-money options for a better chance of profit (assertion). With loc.13 (strike near current price, expiry long enough) → candidate RULE directional long-option strike/expiry choice. D.
- loc.46: set entry and exit points in advance; don't ride greed or hold losers hoping. Allocate 3–5% of capital per trade, never more than 5% → candidate RULE (risk/sizing). D. Conflicts with R-028 (max 7 positions) in spirit.
- loc.46–47: commissions ~$2–5/contract (dated); options settle same/next day; keep cash aside in case a complex trade obliges you to buy shares. D.
- loc.47–50: stocks vs options basics (spun text); arbitrage example with broken arithmetic — not used.
- loc.51: know max loss and max gain before entering; cut losses and move on (agrees existing exit-before-entry principle). Book's "5 calls need 500 shares bought first" is wrong — ignored.
- loc.52: don't use long-horizon tactics (averaging) with options because they expire; watch margin requirements; dividends, decay and IV changes can erase gains from a favourable move. D.
