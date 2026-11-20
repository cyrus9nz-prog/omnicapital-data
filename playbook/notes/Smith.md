# Workflow A output — Smith, "Option Strategies" (3rd ed., 2008)

Read: [[Smith p.1]] through [[Smith p.321]] (end of file, 616,040 bytes), sequentially in ~30 KB chunks. Table page: p.262 (omitted in conversion).
Playbook checked: local copy /home/claude/pb/playbook.md (header "Next rule ID: R-234", 233 rules, 370 principles, 62 conflicts). instructions.md could not be opened in this session (no Projects tool); the task's stated Workflow A rules were followed.

## New rules

### R-NEW1 Implied-volatility forecast: range extreme plus a gap to historical volatility, otherwise neutral
School: process | Horizon: swing (days–weeks) | Instrument: options
IF a stock's at-the-money implied volatility is in the top part of its own range over roughly the past 1–2 years AND sits above its 30-day historical volatility THEN forecast IV falling to at least mid-range (favour short-premium structures); IF IV is in the bottom part of its range AND below 30-day HV THEN forecast IV rising to at least mid-range (favour long-premium structures); the wider the IV–HV gap the stronger the call; any other state → IV neutral | EXIT when IV reaches mid-range (or the opposite end), re-forecast | INVALIDATED BY a structural change in the company (major merger, acquisition or divestiture) or options listed less than about a year ago — IV may trend instead of ranging; stand aside
Inputs: daily ATM IV and its 1–2-year high/low/mean → historical chains (Alpha Vantage HISTORICAL_OPTIONS) or pasted by Cyrus; 30-day HV → computed from daily closes (Alpha Vantage TIME_SERIES_DAILY); option listing date and M&A news → company filings/news. "Top/bottom part of the range" (e.g. top/bottom quintile) is a test parameter; the book gives none
Sources: [BOOK Smith p.80–82]; [BOOK Smith p.83]; [BOOK Smith p.84]
Evidence: C — one real case (IBM IV vs 30-day HV chart, about a year, read in hindsight; the author says the rules "would have created many profitable predictions") with no tally
Conflicts: none yet (refines R-209 with explicit conditions; see Merges)
Status: UNTESTED

### R-NEW2 Fade a market-wide IV spike when the company itself has not changed
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock's IV breaks above its normal range during a market-wide volatility event AND there is no company-specific news or structural change THEN open a short-IV position (the book: short straddle or other short-premium structure), expecting IV to return inside the range | EXIT when IV is back inside its normal range (mid-range target per R-NEW1) | INVALIDATED BY company-specific news, a merger/acquisition/divestiture, or IV continuing to trend higher (range broken for structural reasons)
Inputs: stock IV and its range → historical chains (Alpha Vantage HISTORICAL_OPTIONS); market-wide event → VIX daily close (Cboe/Alpha Vantage) and index-wide IV; company news → news feed / filings
Sources: [BOOK Smith p.83]
Evidence: C — one case (IBM IV peaked near 28.5% in Aug 2007 credit-crunch selling with no IBM news); the author calls the reversion a near certainty with no tally
Conflicts: R-073 — decided by structure and the desk test: index or index-weighted credit spreads while VIX > 30 → R-073 (B evidence) governs; single-stock, defined-risk short-IV with no company news → R-NEW2, paper only until tested
Status: UNTESTED

### R-NEW3 Direction view × IV view picks the structure
School: process | Horizon: swing (days–weeks) | Instrument: options
IF price view higher AND IV view higher THEN buy a call or a bull spread; IF higher AND IV lower THEN sell a put or write a covered call; IF lower AND IV higher THEN buy a put or a bear spread; IF lower AND IV lower THEN sell a call or write a covered put; IF stable AND IV lower THEN sell a straddle/strangle or ratio write; IF a big move of unknown direction AND IV higher THEN buy a straddle; IV neutral → either side | EXIT n/a (structure selection; then follow the chosen strategy's rules) | INVALIDATED BY no price view (the book starts every trade from the price view)
Inputs: price view → the share rule or thesis that triggered it; IV view → R-NEW1; time-decay sign → options chain greeks (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK Smith p.84]; [BOOK Smith p.89–90]; [BOOK Smith p.100]; [BOOK Smith p.101]
Evidence: D — strategy table and one IBM worked example at a single date, no outcomes (the butterfly rows of Fig. 6.8 contradict Ch.17 and are not carried)
Conflicts: none yet
Status: UNTESTED

### R-NEW4 Long-option expiry from the timing and IV views
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF buying a call or put AND the move is expected imminently OR IV is expected to fall THEN buy the nearby expiry (higher gamma, lower vega); IF the timing is uncertain OR IV is expected to rise THEN buy a farther expiry (more vega, lower decay per day) and plan to sell before decay accelerates | EXIT sell before the final weeks of fast decay; roll forward if the view still holds near expiry | INVALIDATED BY poor liquidity in the far month (avoid it unless holding to expiry)
Inputs: expected move timing → the trade plan; IV view → R-NEW1; expiries, vega, theta, volume/open interest → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK Smith p.106–107]; [BOOK Smith p.118–119]
Evidence: D — asserted
Conflicts: R-046 and R-071 (30+ days) — decided by expected timing: move expected within days → nearby allowed if it passes the desk's C4 move check; otherwise 30+ days per R-046/R-071
Status: UNTESTED

### R-NEW5 Long-option strike from a target price and a loss budget
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF buying an option for direction THEN first set a target price for the move and the dollar loss you accept, then compute each candidate strike's payoff at the target for the quantity the budget buys and take the best; as a guide: very strong view → out of the money, moderate view → in the money, quick move expected → at or slightly in the money; never pick out-of-the-money because it is cheap | EXIT at the target or when the view changes (see R-NEW8, R-NEW9) | INVALIDATED BY no target price (don't trade)
Inputs: target and loss budget → the trade plan; strikes, premiums, deltas → options chain snapshot; payoff at target computed in code
Sources: [BOOK Smith p.107–108]; [BOOK Smith p.119–120]
Evidence: D — one hypothetical $2,000-budget example
Conflicts: R-034 — decided by the desk's C4 move check: an out-of-the-money strike is allowed only when its breakeven still sits inside the typical move; otherwise R-034's at/in-the-money choice
Status: UNTESTED

### R-NEW6 Rank candidate options by repricing after a one-implied-move rise and fall
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF choosing among options on several stocks for the same directional view THEN pick a horizon, reprice each option (pricing model) after the stock moves up and after it moves down by one implied-volatility standard deviation over that horizon, compute (price after the favourable move) ÷ (price after the adverse move), and prefer the highest ratios | EXIT n/a (ranking) | INVALIDATED BY n/a
Inputs: price, IV, strike, expiry, rate → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus) and Black-Scholes in code; horizon → the trade plan
Sources: [BOOK Smith p.109–110]; [BOOK Smith p.121–122]
Evidence: D — asserted method, no example output
Conflicts: none yet
Status: UNTESTED

### R-NEW7 Short-option strike beyond one implied move
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF selling a call (or put) for premium THEN choose a strike beyond the price ± one implied-volatility move to expiry (price × IV × √(days/365)); conservative: about twice that distance; prefer options whose IV is high against its own record, with expiry inside about six weeks when decay accelerates | EXIT see R-NEW1 (IV back to mid-range) and the desk's buy-back rules; roll or close if price approaches the strike | INVALIDATED BY IV low against its own record (selling underpriced options)
Inputs: price → daily quote; IV, strikes, expiry → options chain snapshot; IV history → Alpha Vantage HISTORICAL_OPTIONS; implied move computed in code
Sources: [BOOK Smith p.130–131]; [BOOK Smith p.166–167]
Evidence: D — one Swiss-franc worked example (61.00 ± 1.83 → 63 call); naked writing; the put version mislabels the strike a call (p.167)
Conflicts: none yet (consistent with the delta ≈ 0.16 principle; naked calls remain subject to the desk's gates)
Status: UNTESTED

### R-NEW8 Losing long call or put: repair into a vertical at about even money
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a long call has lost value because the stock fell AND you are still bullish THEN sell two of the held calls and buy one call at the next lower strike for about the same total premium (net cost near zero), turning it into a bull call spread with a lower breakeven (mirror for puts: sell two, buy one higher strike); if now bearish, liquidate; if little premium is left, simply hold | EXIT per the vertical-spread rules (R-NEW12) | INVALIDATED BY the new spread failing the entry tests for a new bull/bear spread
Inputs: held option, strikes, bid/ask → options chain snapshot; current view → the trade plan
Sources: [BOOK Smith p.110–111]; [BOOK Smith p.122–123]
Evidence: D — one hypothetical OEX example
Conflicts: none yet
Status: UNTESTED

### R-NEW9 Winning long option: take the stake out or sell the next strike
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a long call has gained (stock up) AND you are still bullish THEN either sell the call and buy a higher strike using only the profit (original stake withdrawn), or sell a higher-strike call against it (bull spread, locking in a gain; preferred when IV is expected to fall); if now bearish, take the profit; near expiry, roll forward rather than exercise | EXIT at the target or the spread's maximum | INVALIDATED BY n/a
Inputs: entry cost, current premiums, strikes → options chain snapshot; IV view → R-NEW1
Sources: [BOOK Smith p.112–113]; [BOOK Smith p.124–125]
Evidence: D — hypothetical OEX examples (put version mislabels puts as calls, p.125)
Conflicts: none yet (cf. R-041 trailing stop — compatible alternatives)
Status: UNTESTED

### R-NEW10 Covered write defence at the breakeven: roll down or exit, planned before entry
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a covered call's stock falls to the position's breakeven (entry price − premium) OR to a support level or money-management point set before entry THEN if now bearish close the whole position; if still bullish buy back the call and sell a lower strike (or part of the position, or lower and farther out) for added credit, accepting a lower maximum gain | EXIT when the rolled position cannot add protection without locking in a loss you would not accept | INVALIDATED BY no rolling plan written before the original write
Inputs: entry price, premium → trade record; support → daily OHLC; strikes, bid/ask → options chain snapshot
Sources: [BOOK Smith p.146–148]; [BOOK Smith p.182] (covered-put mirror)
Evidence: D — one hypothetical Widget-futures example (190 long, 180 call → 160 call)
Conflicts: R-143 — decided by why the shares are held: shares owned for their own case → R-143 forbids a strike below cost basis; a buy-write held for the trade → R-NEW10
Status: UNTESTED

### R-NEW11 Pick vertical spreads by probability-weighted reward to risk
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF choosing a bull or bear spread on a stock THEN list every candidate's maximum profit ÷ maximum risk, weight each by its probability of reaching maximum profit from IV (or your own volatility estimate), and take the highest expected value after commissions; prefer the call version for bull spreads where puts are illiquid or the short leg is in the money (early exercise) | EXIT per R-NEW12 | INVALIDATED BY commissions large against the maximum profit
Inputs: strikes, premiums, IV, open interest → options chain snapshot; probabilities computed in code (lognormal with IV)
Sources: [BOOK Smith p.199–200]; [BOOK Smith p.213–214]
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-NEW12 Vertical-spread follow-up: roll winners when the new risk is below the banked profit; don't roll losers
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a vertical spread has moved in your favour AND the view still holds THEN close it and open the next spread further out only if the new spread's maximum loss is less than the profit just banked (a locked-in gain); IF the spread is at maximum profit and the view is now neutral THEN close it; IF the spread is losing THEN don't roll it toward the price (the new spread's potential is cut by the realised loss) — hold if at maximum loss, or close | EXIT as stated | INVALIDATED BY n/a
Inputs: spread prices, strikes → options chain snapshot; realised P&L → trade record
Sources: [BOOK Smith p.202]; [BOOK Smith p.205–206]; [BOOK Smith p.216–218]
Evidence: D — hypothetical MMI tables
Conflicts: none yet
Status: UNTESTED

### R-NEW13 Long butterfly only when the debit is under 10% of the strike interval
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the stock is expected to stay still AND a long butterfly (buy 1 low, sell 2 middle, buy 1 high, equal intervals) with the middle strike at the money costs less than 10% of the interval between adjacent strikes (e.g. under 0.50 on 5-point strikes) AND the outer strikes lie beyond the stock's expected range for the holding period THEN buy it | EXIT near the middle strike at expiry; if the view changes, convert to a vertical or roll the middle strike to the new price | INVALIDATED BY the debit at or above 10% of the interval
Inputs: strikes, bid/ask → options chain snapshot; expected range → IV-implied move computed in code
Sources: [BOOK Smith p.225]; [BOOK Smith p.226–233]
Evidence: D — rule of thumb, hypothetical OEX tables
Conflicts: none yet
Status: UNTESTED

### R-NEW14 Calendar spread: sell the rich near month as its decay accelerates
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the near-month option's IV is above the far month's AND the near option is entering its fast-decay period THEN sell the near option and buy the same strike in the next expiry; neutral → at-the-money strike; bullish/bearish → strike at the price objective; use the two nearest expiries for liquidity | EXIT close if price moves beyond the estimated breakeven at the near expiry and is expected to stay there; otherwise re-centre the strikes | INVALIDATED BY a sharp move through the strike before the near expiry (near-leg gamma)
Inputs: near/far IV, premiums, theta → options chain snapshot; price objective → the trade plan
Sources: [BOOK Smith p.237–238]; [BOOK Smith p.240]; [BOOK Smith p.241–243]
Evidence: D — asserted (the text says "sell a far contract" where buying is meant, p.240)
Conflicts: none yet
Status: UNTESTED

### R-NEW15 Long straddle: your expected range beats the implied range, IV at the low end
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF your expected price range to expiry is wider than the IV-implied range AND IV is at the low end of its own range (R-NEW1) THEN buy an at-the-money straddle, preferring long-dated options (more vega, less daily decay); for a specific news catalyst only, use the highest-gamma near expiry and hold a few days | EXIT when the expected move or IV rise has happened; if you now expect stable prices, close (the premise is gone) | INVALIDATED BY IV in the middle or high end of its range, or a pre-announcement IV run-up (straddles often drop after the report)
Inputs: expected range → the trade plan; IV, implied move, strikes → options chain snapshot; IV history → Alpha Vantage HISTORICAL_OPTIONS; event dates → earnings calendar
Sources: [BOOK Smith p.264–266]; [BOOK Smith p.268]; [BOOK Smith p.271]
Evidence: C — one real IV-vs-actual-volatility chart (nearest T-bond futures option, about two years) plus a hypothetical earnings example
Conflicts: none yet (agrees with R-209: buy only when a move is expected)
Status: UNTESTED

### R-NEW16 Delta-neutral far-dated straddle to trade the IV forecast
School: options-income | Horizon: position (months) | Instrument: options
IF R-NEW1 forecasts IV rising THEN buy an at-the-money straddle in a far expiry; IF it forecasts IV falling (and no price move expected) THEN sell it; keep the position delta neutral with the stock, and roll to a farther expiry when theta and gamma become noticeable; if the stock moves away, re-centre strikes or add straddles at the new at-the-money strike | EXIT when IV reaches the R-NEW1 target | INVALIDATED BY the R-NEW1 invalidations
Inputs: IV forecast → R-NEW1; delta, gamma, theta, vega → options chain snapshot; stock hedge → daily quote
Sources: [BOOK Smith p.266]; [BOOK Smith p.277–278]; [BOOK Smith p.84]
Evidence: D — asserted
Conflicts: none yet (short straddles carry unlimited risk; subject to the desk's gates)
Status: UNTESTED

### R-NEW17 Ratio spread: buy intrinsic, sell time, in the delta ratio
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF expecting prices to stay between two strikes THEN buy deep in-the-money options and sell at- or slightly out-of-the-money options in the ratio of their deltas (e.g. 0.69 ÷ 0.46 ≈ 1.5 short per long), preferably for a credit (no risk on the long side); re-hedge whenever the net delta shifts by one contract and roll the short strike to the new at-the-money as price moves | EXIT close or convert to a vertical if price heads through the upside breakeven (high strike + max profit ÷ naked contracts) | INVALIDATED BY a small position that can't be adjusted in whole contracts
Inputs: strikes, deltas, premiums → options chain snapshot; breakeven computed in code
Sources: [BOOK Smith p.245–246]; [BOOK Smith p.248–250]
Evidence: D — hypothetical S&P 500 futures-options example
Conflicts: none yet
Status: UNTESTED

### R-NEW18 Covered call as a pre-sale at the target price; roll up only for a credit
School: options-income | Horizon: position (months) | Instrument: options
IF you own shares with a set sell target AND the call struck at that target pays a worthwhile premium (the book: more than about $50 a contract) THEN write it, pre-selling at the target; IF that premium is too small THEN write near the current price and roll up as the stock climbs, only for a net credit, until the target strike is reached | EXIT assignment at the target | INVALIDATED BY a long-term bearish view on the shares (sell them instead)
Inputs: sell target → the valuation or trade plan; strikes, premiums → options chain snapshot; share position → Cyrus's records
Sources: [BOOK Smith p.144–145]; [BOOK Smith p.180] (covered-put mirror)
Evidence: D — asserted
Conflicts: none yet (complements R-143)
Status: UNTESTED

### R-NEW19 Rank covered writes: minimum protection first, then profit ÷ protection weighted by probability
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF choosing among covered writes THEN drop those below your minimum downside protection (premium ÷ stock price), rank the rest by potential profit ÷ downside protection and by return-if-unchanged, and weight by the IV-implied chance of each outcome; compare annualised returns only between similar writes | EXIT n/a (ranking) | INVALIDATED BY n/a
Inputs: price, strikes, premiums, IV, expiry → options chain snapshot; minimum protection → Cyrus's setting; returns computed in code
Sources: [BOOK Smith p.140–141]; [BOOK Smith p.145–146]; [BOOK Smith p.181]
Evidence: D — hypothetical Widget arithmetic
Conflicts: none yet
Status: UNTESTED

### R-NEW20 Moderately bullish: bull spread instead of a long call
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF your target price sits at or below the bull spread's upper strike (a moderate rise) THEN buy the bull spread rather than the call — for the same money it pays more unless the stock rises well beyond the upper strike (mirror: bear spread instead of a put when moderately bearish) | EXIT per R-NEW12 | INVALIDATED BY a target well above the upper strike (buy the call per R-NEW5)
Inputs: target → the trade plan; strikes, premiums → options chain snapshot; payoff comparison computed in code
Sources: [BOOK Smith p.195–198]; [BOOK Smith p.209–212]
Evidence: D — hypothetical MMI tables (about three spreads for the cost of one call)
Conflicts: none yet (cf. R-035, which uses a slowing uptrend as the trigger)
Status: UNTESTED

## Merges
R-209 | agrees: [BOOK Smith p.80–84] (high IV vs its own range and above HV → write; low and below HV → buy; explicit conditions in R-NEW1)
R-009 | agrees: [BOOK Smith p.295–296] (risk about 1% of equity per trade; 2–3% raises the risk of ruin; a third of capital per trade is a sure wipe-out)
R-034 | agrees: [BOOK Smith p.27]; [BOOK Smith p.113] (sell rather than exercise while any time premium remains)
R-148 | agrees: [BOOK Smith p.150] (no reason to hold a short call once its time premium is gone: roll forward or close)
R-151 | agrees: [BOOK Smith p.150–151] (roll forward only if the next month's return per day beats the current write's); [BOOK Smith p.131] (decay accelerates in the last six weeks)

## Conflicts
- R-NEW2 Fade a market-wide IV spike vs R-073 No new credit spreads while the VIX is above 30 — decided by structure and evidence: index or index-weighted credit spreads while VIX > 30 → R-073 (B); single-stock defined-risk short IV with no company news → R-NEW2, paper only until tested [BOOK Smith p.83]; [BOOK FreemanCS loc.67–68]
- R-NEW4 Nearby expiry for an imminent move vs R-046 / R-071 (30+ days) — decided by expected timing: a move expected within days → nearby, if it passes the desk's C4 move check; otherwise 30+ days [BOOK Smith p.106–107]; [BOOK Heitkoetter loc.37]; [BOOK EDay loc.15–16]
- R-NEW5 Out of the money for a strong view vs R-034 At or in the money — decided by the desk's C4 move check: out of the money only when its breakeven sits inside the typical move [BOOK Smith p.107–108]; [BOOK Cayman loc.11]
- R-NEW10 Roll a covered call down at the breakeven vs R-143 (no strike below cost basis) — decided by why the shares are held: owned for their own case → R-143; buy-write held for the trade → R-NEW10 [BOOK Smith p.146–148]; [BOOK FreemanCC loc.45]

## Principles
- Include at least one tick of slippage on each side, plus commissions, financing, opportunity cost (T-bills) and taxes, when computing an option trade's return and breakeven [BOOK Smith p.14–16]; [BOOK Smith p.45] — D
- An option with little open interest or volume is easy to enter and hard to leave: expect to hold it to expiry [BOOK Smith p.20] — D
- Buying and selling options earn the same before costs; selling because most options expire worthless only swaps many small wins for a few large losses [BOOK Smith p.21–22]; [BOOK Smith p.292]; agrees with the existing '85% expire worthless is a myth' principle [BOOK FreemanCC loc.37–38]; the book itself repeats the 70% figure without comment at p.127 and p.163; in tension with the existing FreemanCS 'sideways 80–85% of the time favours selling' principle — D
- Exercise early only when the option is bid below intrinsic value; abandon an option whose premium is below the cost of closing it [BOOK Smith p.27–28] — D
- Price matters most in hedged strategies (covered writes, spreads, straddles); enter at limit prices, but pay up a dime to catch a big expected move [BOOK Smith p.43–44]; agrees with the existing 'limit orders in, market orders out' principle [BOOK MetaStock p.10] — D
- Compare annualised returns only between similar strategies, and judge each by risk per unit of profit [BOOK Smith p.45–46] — D
- Prefer probability-weighted expected return over return-if-unchanged when comparing strategies; delta roughly approximates the chance of finishing in the money [BOOK Smith p.47–48]; [BOOK Smith p.59]; agrees with the existing delta ≈ probability principle [BOOK FreemanCS loc.31] — D
- A delta-neutral short strangle drifts long or short through gamma; each rebalance locks in small losses that eat the credit, so rebalancing frequency is a cost trade-off (professionals rebalance each $1 move or each day) [BOOK Smith p.66–69] — D
- No option combination equals the stock except a conversion or reversal; keep watching gamma, vega and theta on a delta-neutral position [BOOK Smith p.69] — D
- Real price distributions have fat tails and gaps that Black-Scholes ignores; the gap matters mainly to market makers chasing small edges [BOOK Smith p.76–78] — D
- Implied volatility is usually the second most important price driver after the stock; calls can fall while the stock rises if IV drops [BOOK Smith p.80]; [BOOK Smith p.84] — C
- Options demand a view on how far and how fast, not only which way: an out-of-the-money call must reach its breakeven before expiry [BOOK Smith p.87–88]; agrees with the existing 'direction, size and timing' principle [BOOK Broker p.203] — D
- Buying an option is mostly a market-timing bet; everything else is secondary [BOOK Smith p.103]; [BOOK Smith p.115] — D
- Writing a call against an existing holding is a new trade with its own risk, not the old position; if long-term bearish, sell the shares instead [BOOK Smith p.144–145] — D
- Enter covered writes as a single net order and skip the trade if the net price isn't filled [BOOK Smith p.141–142]; [BOOK Smith p.177–178]; agrees with the existing one-order principle [BOOK FreemanCS loc.25] — D
- Diversify covered writes across strikes and expiries rather than one strike [BOOK Smith p.154]; [BOOK Smith p.184–185] — D
- Ratio writes and ratio spreads need large positions and constant delta re-hedging; small accounts can't adjust in whole contracts [BOOK Smith p.156]; [BOOK Smith p.158]; [BOOK Smith p.160–161] — D
- After a losing spread, beware 'doubling up to catch up' by lifting the hedge leg on emotion [BOOK Smith p.201]; [BOOK Smith p.218]; agrees with the existing 'don't revenge trade' principle [BOOK Heitkoetter loc.56–57] — D
- Straddle prices tend to rise before earnings and economic reports and drop after the release; cheap straddles come in dull markets [BOOK Smith p.264–265] — D
- Conversions, reversals, boxes and butterflies at the margin are floor-trader arbitrage dominated by carry and costs; enter only if the gap beats carry and costs, exit if carry turns against you [BOOK Smith p.15]; [BOOK Smith p.283–285] — D (recorded only)
- Author claims about 90% of option traders lose, 5% break even and 5% profit (no source) [BOOK Smith p.287]; agrees with the existing '90% of day traders don't last' principle [BOOK Anderson loc.58] — D
- Trade to make money, not to be right: ego makes you hold losers and cut winners [BOOK Smith p.290–291] — D
- Small accounts: keep each trade's risk to a few hundred dollars with call or put spreads rather than cheap out-of-the-money options [BOOK Smith p.296–297] — D
- Stick with a strategy until it has a meaningful number of closed trades; don't cut planned profits short or bail on a news item — author claims an informal study of his traders found the original plan beat the override over 80% of the time (no sample given) [BOOK Smith p.303–305]; agrees with the existing 'don't gut a working plan' principle [BOOK Heitkoetter loc.59–61] and the 'reread pre-news notes' principle [BOOK Wachenheim loc.11–15] — D
- Write a trading plan before entering (price view, IV view, strategy, entry, stop, follow-up) and run a postmortem on each trade, graded against the plan; review the file every few months [BOOK Smith p.305–310]; agrees with the existing 'write a trading plan … journal every trade' principle [BOOK Pansheriya loc.21–23] — D
- Edges decay when too much money follows one method; the author says he moved from trend-following systems to chart analysis in the late 1980s for that reason [BOOK Smith p.301–302] — C

## Ingest log row
| 2026-11-19 | Smith | p.321/321 | 20 (options-directional 9, options-income 9, process 2; C 3, D 17) | 5 (R-009, R-034, R-148, R-151, R-209) | 26 new + 9 agreements | Wiley practitioner textbook (2008); author promotes his Investment Mentoring Institute (plan form p.307), CTCR journal (p.301) and a book website (p.321); author claims a strategy that should make about 65% a year nets about 45% after costs (p.31), 1970s accounts at 200%/100% a year (p.288) and only one near-losing year in 30 (p.301); 90% figure unsourced (p.287); informal >80% plan study with no sample (p.304); Donchian claim unsourced (p.289); nearly all examples hypothetical (Widget, OEX, MMI) at fractional prices; real cases only IBM IV charts (p.81–82, 91–99) and T-bond IV (p.266); table page 262 omitted (check table: straddle/strangle option charts); futures-specific margin, T-bond 64ths and FX phi material out of desk scope; errors not carried: Fig. 6.8 butterfly rows contradict Ch.17 (p.100 vs p.222–225), 70% expire worthless repeated (p.127, 163) against p.21, put profit called unlimited then limited (p.115), put profit formula garbled (p.165), puts labelled calls (p.125, 167), covered-put roll example mixes strikes/'call' (p.182), break-even 'raised' on a credit roll (p.184), bear-spread text contradicts itself on decay and says 'bull' (p.213–214, 217), 'MMI at 350.50' (p.211), bull-spread rally table repeats the decline table (p.207), calendar 'sell a far contract' (p.240), Ch.20 header table copied from straddles (p.257), short-straddle example says 'buy' (p.264) |

## Run report
Read all 321 PDF pages (markers p.1–p.321, end of file reached); one table page (p.262, straddle/strangle charts) omitted in conversion. Rule candidates: 20 new — options-directional 9, options-income 9, process 2; grades C 3, D 17; no A/B (the book has no systematic tests or cited studies). 5 merges (R-009, R-034, R-148, R-151, R-209), 4 conflicts (R-073, R-046/R-071, R-034, R-143), 26 principles. Mostly a strategy reference built on hypothetical worked examples; follow-up chapters were condensed into rules R-NEW8–R-NEW12; about 30 further candidates listed under Cut. Day-trading: none. Caveat: instructions.md was not reachable here (no Projects tool), so the task's Workflow A rules and the local playbook copy were used.
Test first: R-NEW1 (IV forecast from range position plus IV–HV gap). It is the book's only explicit, conditioned forecasting rule; inputs (ATM IV history, 30-day HV) are available from HISTORICAL_OPTIONS and daily closes; it underlies R-NEW2/3/15/16 and gives R-209 its missing thresholds, so one backtest of "IV reverts to mid-range" settles several rules.

## Cut
- Covered call/put near expiry: roll forward by return per day (recorded as merges R-148, R-151) [p.150–151, 184]
- Long option near expiry: roll forward, never exercise with time premium (merge R-034) [p.113, 125]
- Covered call when stock rises: roll forward instead of assignment to save commissions [p.149]
- Hedge-motive covered call: in-the-money call sized by delta to cover the expected drop, expiry after the planned exit [p.144]
- Covered-call profit motive: OTM or fewer calls than shares when very bullish, ITM for protection [p.145]
- Write covered calls against convertibles [p.151–154]
- Ratio covered call / put delta-neutral write with one-contract rebalancing [p.155–161, 187–193]
- Skew ratio trade: buy low-IV strike, sell high-IV strike vega-neutral, only if the skew has a history of reverting [p.65, 156, 159]
- Theoretical-edge straddle: buy ATM straddle when forecast IV > current IV [p.64]
- Naked call vs short stock (and naked put vs long stock) by strength of view [p.128, 163–164]
- Naked call/put follow-ups (hold, roll down/up, roll forward, convert to covered write) [p.131–133, 167–169]
- Covered put writing set (pre-buy at target, roll up at resistance) [p.171–185]
- Bull put spread vs bull call spread choice [p.199–200]
- Vertical spread: convert to a single leg when the view turns [p.201–207, 214–220]
- Long butterfly follow-ups (convert to vertical, roll middle strike) [p.226–235]
- Short butterfly selection [p.225]
- Calendar spread follow-ups (liquidate short leg, roll strikes) [p.241–243]
- Reverse calendar spread [p.238]
- Ratio spread follow-ups by view [p.250–255]
- Ratio calendar spread construction and defensive exit [p.257–259]
- Short straddle selection (IV high end, no move expected) — folded into R-NEW16 [p.266]
- Straddle follow-ups by view (liquidate, lift a leg, roll) [p.266–277]
- Synthetic calls/puts follow-ups [p.279–282]
- Conversion/reversal arbitrage (floor-trader only, recorded as principle) [p.283–285]
- Historical volatility lookback equal to days to expiry [p.80]
- Delta-neutral rebalancing every $1 or each day [p.69]
- Expiration-cycle and strike-interval conventions [p.24–25]
- Stop a long option out when its premium falls by a few hundred dollars (small accounts) [p.297]
