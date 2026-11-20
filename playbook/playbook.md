# Playbook — Stock Desk rules ledger

The only source of strategy for watchlist research (Workflow B) and verdicts (Workflow C).
Built one book at a time by Workflow A from the books in `library.md`. Every rule cites the
page or loc that says it; every rule starts UNTESTED and changes status only on ledger
evidence (Workflow D) or a real test.

Citations: `[BOOK Key p.N]` = PDF page N of the source file. `[BOOK Key loc.N]` = the Nth
~2,000-character segment of `text/<Key>.md` for ebooks (not a print page).
Evidence grades describe the book's support, not the idea: A systematic test with rules,
sample and period · B cites outside studies/data · C author's own trades or cases · D assertion.
Author returns or win rates appear only as "author claims X [BOOK …]".

Rule schema:
```
### R-### <short name>
School: <value | growth/momentum | swing-technical | day-trading | options-income | options-directional | risk/sizing | process> | Horizon: day / swing (days–weeks) / position (months) / long-term (years) | Instrument: shares / options
IF … THEN … | EXIT … | INVALIDATED BY …
Inputs: <input> → <data source>; …
Sources: [BOOK Key p.N]; agrees: [BOOK Key2 p.N]
Evidence: A/B/C/D — <one line why>
Conflicts: R-### — decided by <condition>
Status: UNTESTED | PAPER n=<reviewed calls> held=<n> | TESTED <link/date> | RETIRED <date, why>
```

Next rule ID: R-273

## Index by school
- swing-technical: R-001 Trend pullback to the last higher low; R-002 Pullback to the short moving average in an uptrend; R-003 Double top / double bottom neckline break; R-004 Head-and-shoulders neckline break; R-005 Breakout, then buy the retest; R-006 Fade the failed breakout; R-007 Range trading at support and resistance; R-008 Confluence-zone reversal entry; R-025 200-day moving average as a sentiment gauge; R-026 Trade with the 12/50-day EMA trend; R-030 Candle reversal signal at support; R-031 ADX and MACD trend confirmation; R-032 Guppy multiple moving averages: rally or trend; R-037 Pullback bigger than the prior up-leg: stop buying; R-038 Rising channel: a midline break targets the top; R-044 PowerX: first bar with all three indicators aligned; R-063 Inside-bar cluster: trade the break in the trend's direction; R-064 Pin bar or two-bar reversal as a continuation in a trend pause; R-065 Buying climax at the end of an ageing trend: stop buying, tighten, exit; R-066 Bollinger Band fade inside a range; R-067 DeMarker oversold buys inside a range within an uptrend; R-068 ADX rising above 25 with higher lows inside a base: early breakout entry; R-095 Penny stocks: trust chart patterns only on high turnover; R-142 Read volume with price: favour light-volume pullbacks, respect heavy-volume selling; R-170 Triangle breakout: wait for the break before three-quarters of the way to the apex; R-208 9 EMA crosses above the 13 EMA while the 13 EMA is above the 50 EMA; R-211 Take RSI signals only in the direction of the MACD trend; R-226 Short a broken former leader on a dry-volume rally into resistance
- risk/sizing: R-009 Per-trade risk cap; R-010 Minimum reward-to-risk of 2; R-020 Avoid sub-penny stocks; R-021 Short holding limit for penny stocks; R-022 Never add to a losing position; R-024 Broad sell-off exit for speculative names; R-027 Only positions you can exit in one day; R-028 Cap the number of open positions; R-040 Allocate 3–5% of capital per trade; R-045 ADR stop and target: 1.5× and 3× the 7-day range; R-047 Raise risk only after proven profits (fixed ratio); R-049 Account circuit breaker; R-050 Index trend filter: S&P 500 50-day above 200-day; R-055 Market filter: S&P 500 EPS estimate vs 15 weeks ago; R-061 20% stop from cost, 20% trailing stop from the peak; R-070 Set the target multiple from your measured hit rate; R-080 Credit-spread sizing: up to 10% per trade and 10% a month, falling to 2%; R-081 Pyramid only into a winning position, each add with its own stop; R-082 Time stop: close a short-term trade that shows no profit within 2–3 days; R-084 Trade with no more than 5–10% of liquid capital; R-085 OTC stocks: trade only the top tiers; R-089 Dollar-cost averaging: fixed amounts on a fixed schedule; R-090 Penny stocks: take a 20–30% gain made within days; R-108 Sell on an analyst downgrade after a large fall; R-121 Kelly-scaled position weight, trimmed as price nears expected value; R-139 Trim a single stock that has grown to about a fifth of the portfolio; R-140 Keep trading costs at or under 2% of the order value; R-152 Code red: exit the stock (and its short call) on a fraud allegation; R-158 Insider sales that matter: selling into weakness, or a finance officer liquidating before earnings; R-159 Don't hold a weakening company into earnings after a run of negative reactions; R-168 Move the stop to breakeven once the trade is modestly in profit; never let a winner become a loser; R-169 No chart stop? Set the stop from the target and a fixed reward-to-risk ratio; R-175 Speculative 'top stock' bets: a couple of percent of the portfolio in total; R-180 Rebalance an allocation when a sleeve drifts more than 10% from its target, or once a year; R-187 Sell a high-multiple holding on stalled earnings or any operating crack; R-200 Concentrated but capped: 15–25 holdings, at most 12% per stock and 25% per industry, measured at cost; R-214 Inverse-variance weights inside a per-name cap; R-216 Negative news-sentiment shift on a holding: review, reduce if price agrees; R-220 Seven-Week Rule: trail a growth winner on the 10-day or 50-day line; R-221 7–8% maximum loss from the purchase price (on the underlying for option proxies); R-222 Earnings-gap budget: size into a report by the portfolio hit you can take; R-223 Big high-volume gap-down on a holding: sell at the open; R-230 Build a long-term position in thirds over up to two or three years; R-261 Three-year rule for a conviction holding; R-263 Position caps at cost by company risk class
- day-trading: R-011 Daily direction, intraday confirmation; R-012 Bull-flag channel breakout; R-013 Keltner Channel close-outside breakout; R-014 Fibonacci retracement: continue above 0.5, reverse below; R-015 Alligator fan-out entry; R-016 EMA(5) high/low channel snap-back; R-017 News and session timing filter; R-039 Day-trading list: big daily movers only; R-088 Penny-stock new-high breakout that holds the morning high; R-160 Early range breakout (ERBO): trade the break of the first 30 minutes' high or low; R-161 Opening reversal on a gapper: trade the early-range break, target the gap fill; R-162 1234 consolidation at the day's high above a whole number; R-163 Previous day's range break, mainly after lunch; R-164 Gap-fill bias: expect an opening gap to retrace to the prior close, more so inside yesterday's range; R-165 Day-trading watchlist: fresh catalyst news plus price, volume and range filters; R-166 Index-futures direction filter for intraday entries; R-167 Intraday exits: half at a whole number, the rest on a 10 EMA break or three bars against; R-212 Daily pivot levels: range between S1 and R1, breakouts count only beyond them; R-213 LLM headline score: long good news, short bad news, hold one day
- value: R-018 Market valuation regime: forward earnings yield vs 10-year Treasury; R-033 Dividend trend as a health check; R-056 Value screen: cheap on book, cash flow and earnings, low debt; R-058 Dividend screen: yield over 4% now and over 5 years; R-060 Margin of safety: price at most two-thirds of intrinsic value; R-062 Dividend yield above 5%: check for a yield trap; R-083 Average down only when the company has strengthened while the price fell; R-087 Skip companies that keep issuing shares; R-092 Solvency screen: liquidity ratios of at least 1; R-093 Cash runway of at least 12 months; R-094 No earnings: price at most half of sales per share; R-101 Value premium: the cheapest fifth by EV/EBITDA or P/E; R-102 Long-term reversal: favour three-year losers over three-year winners; R-103 F score: among value stocks, buy 8–9, avoid 0–1; R-104 Avoid high-accrual earnings; R-105 Cluster insider buying: three or more insiders within three months; R-106 Favour companies actually buying back their shares; R-107 Avoid IPOs and stocks within three years of listing; R-110 ROE-growth fair price/book for mature companies; R-111 Market-implied growth check before buying; R-112 Value on normalised margins and ROE, not a peak year; R-113 Cash hoarder: value operations separately and discount the cash; R-114 Debt paydown at a steady EV/EBITDA; R-115 Strip one-off acquisition intangibles before judging ROE; R-116 Dividend-yield band for steady dividend growers; R-117 Residual-income trend: count only growth that beats the cost of equity; R-118 Low-leverage cyclicals: buy the bottom of the P/B band; R-119 Sell only when price passes a refreshed fair value; R-122 Segment drag: a low-return division hiding a good business; R-123 REITs: favour the lowest short-interest fifth; R-124 Companion-variable mismatch: cheap multiple with strong fundamental; R-125 Peer regression: actual multiple below the growth- and risk-adjusted prediction; R-126 Buy only when intrinsic and relative valuations both say cheap, beyond the valuation's error; R-127 Young or loss-making company: weight the value by its chance of surviving; R-128 Distress-adjusted value from the bond rating's default history; R-131 Badly managed mature company with a credible path to management change; R-132 Turnaround: overlevered firm with sound operations and a debt fix in progress; R-133 Banks and insurers: capital buffer, ROE above cost of equity, average risk; R-134 Commodity producer: compare the price-implied commodity price with a normalised one; R-135 Cyclical bargain: same normalised multiple as peers, better normalised margins; R-136 Capitalise R&D before comparing returns or multiples; R-138 Dividend payout above 100% or on losses: expect a cut; R-141 Value screen: forward P/E below the market's with broad analyst Buy support; R-154 Cheap is not enough: require a dated catalyst before buying; R-155 True spin-off: value it before distribution, buy after the forced selling; R-156 Spin-off checks: avoid spins loaded with debt or inherited liabilities; R-157 Weigh insider buys by type: open-market only, first-time and pre-event buyers count most; R-173 Credit improvement from speculative grade: get ahead of a positive rating-outlook change; R-176 Dow dividend ten: hold the ten highest-yielding Dow stocks, reset once a year; R-177 Favour dividend payers over non-payers; R-178 Own-universe dividend rotation: top yielders from a fixed list of large, growing dividend payers; R-181 Survival floor: net current assets less long-term debt per share; R-182 Book-value cushion scaled to the earnings record; R-183 Loss-type turnaround: cushion, falling cost ratios, then the first profitable quarter; R-184 Own-history P/E band: buy at the low end, project at a constant multiple; R-185 Operating-trend gate: sales direction, cost ratios and margins over two and four years; R-186 Sell when operating indicators turn down, before earnings do; R-188 Flat earnings: sell for opportunity cost unless a change is visible within a year; R-190 Value on recurring, fully taxed earnings; R-191 Balance-sheet warning flags: find out why before going on; R-193 Two-method earnings power 2–3 years out × a quality-adjusted market multiple; buy only with about 30% a year to value; R-194 Consensus-catch-up exit: sell once the expected development has happened and Wall Street agrees; R-195 Industry thesis: own only the net-cash, positive-tangible-book names; R-196 Cyclical peak: industry volume far above normal demand and the company expanding on debt — sell; R-197 Cyclical trough: industry volume far below normal and the overhang clearing — buy the strongest beneficiary; R-198 Strong franchise with a temporary, solvable problem: buy when the worst case still covers the price; R-199 Thesis-break exit: sell at a modest loss when the expected development fails or value drops below price; R-201 Pension expense at economic cost when discount rates are abnormally low; R-202 Large financial near tangible book with normal return on tangible equity well above the cost of equity; R-203 Capacity discipline: industry capacity shrinking while demand grows — buy the best-financed operator; R-206 Acquisition-built companies: value the bought businesses near what was paid; R-207 Market normal value: trend-line S&P 500 earnings × the long-run average P/E; R-228 Graham two-stage value: buy only at or below the 7-year hurdle-rate price; R-232 Capital-discipline flag: buybacks that only offset dilution, deals that drag ROIC down; R-233 Stewardship screen from the proxy statement
- process: R-019 VIX settlement-day distortion filter; R-023 Don't chase past the planned entry; R-029 Half now, half at the ideal price; R-048 40 paper trades and 4 profitable weeks before real money; R-054 Four-season calendar: stocks March–April and October–December; R-059 Strategy acceptance gate; R-109 January barometer: after a negative January, T-bills for the rest of the year; R-120 Walkaway-price watchlist for quality companies; R-137 DCF guardrails: stable growth, terminal risk and reinvestment; R-189 Earnings projection from interim reports: compare like quarters, don't annualise blindly; R-192 Announcement-triggered staged screen with early cut-offs; R-205 Credit-crisis re-entry: hold cash until credit spreads narrow, then buy the most depressed cyclicals; R-229 Growth-input guardrails: normalise, cap at 20%, use the low end, fade to 7% after year 7; R-234 Implied-volatility forecast: range extreme plus a gap to historical volatility, otherwise neutral; R-236 Direction view × IV view picks the structure; R-257 CEO pay far above the next executives: one-man-management flag; R-260 War scare: buy slowly on the threat, faster on the outbreak; R-264 Long-term buys at the market; give block buys a price range; R-266 Disclosure retreat after bad news: exclude
- options-directional: R-034 Long option: breakeven inside the typical move; R-035 Bull call spread in a slowing uptrend; R-041 Trail a long option 5% below its high once it hits target; R-046 PowerX options: in-the-money, 30–45 days, managed on the stock; R-071 Swing options: buy, 30+ days to expiry, slightly out of the money; R-237 Long-option expiry from the timing and IV views; R-238 Long-option strike from a target price and a loss budget; R-239 Rank candidate options by repricing after a one-implied-move rise and fall; R-241 Losing long call or put: repair into a vertical at about even money; R-242 Winning long option: take the stake out or sell the next strike; R-244 Pick vertical spreads by probability-weighted reward to risk; R-245 Vertical-spread follow-up: roll winners when the new risk is below the banked profit; don't roll losers; R-248 Long straddle: your expected range beats the implied range, IV at the low end; R-253 Moderately bullish: bull spread instead of a long call
- options-income: R-036 Bull put spread above strong support; R-072 SPY bull put spread after a cross above the 50-day average; R-073 No new credit spreads while the VIX is above 30; R-074 Credit-spread exits: take 75% of the credit, stop at a loss equal to the credit; R-075 Close short options a few days before expiration; R-076 Credit-spread timing gate: 30–45 days, no earnings or binary event inside; R-077 Credit-spread underlying screen: liquid, mid/large cap, implied volatility under 50%; R-078 Range credit spreads: short strikes outside the range while the bands contract; R-079 Short iron butterfly for a sideways stock; R-143 Covered call only on shares held for their own case, with a gain cushion; R-144 Covered-call regime gate: write when the stock is ranging, not trending; R-145 Covered-call strike distance from the volatility state; R-146 Covered-call underlying screen: boring, liquid, low-debt dividend payer, IV 30–70%; R-147 Covered-call strike by delta: lowest acceptable delta to keep the shares, about 0.40 for income; R-148 Roll a covered call when its time value falls below 1% of the stock price; R-149 2 & 20: buy back a covered call early when 80% of the premium is captured within two weeks; R-150 Buy back the covered call when the stock nears the strike and you want to keep the shares; R-151 Covered-call expiry: 30–45 days unless a longer expiry pays more per month; R-153 Poor man's covered call: deep in-the-money long-dated call plus a 30–45 day short call; R-209 Implied volatility against its own history picks the side: rich → write, cheap → buy; R-210 Iron condor for a stock holding a range; R-235 Fade a market-wide IV spike when the company itself has not changed; R-240 Short-option strike beyond one implied move; R-243 Covered write defence at the breakeven: roll down or exit, planned before entry; R-246 Long butterfly only when the debit is under 10% of the strike interval; R-247 Calendar spread: sell the rich near month as its decay accelerates; R-249 Delta-neutral far-dated straddle to trade the IV forecast; R-250 Ratio spread: buy intrinsic, sell time, in the delta ratio; R-251 Covered call as a pre-sale at the target price; roll up only for a credit; R-252 Rank covered writes: minimum protection first, then profit ÷ protection weighted by probability
- growth/momentum: R-042 Favour stocks that beat analyst estimates; R-043 Go long only with rising revenue; R-051 Sector rotation: top 6 by 20-day return, Treasuries when the filter is off; R-052 Global asset rotation: top 5 of 7 by 120-day return; R-053 Paired switch: stock index vs long Treasuries on 60-day return; R-057 Growth screen: rising EPS and sales, not overbought, low debt; R-069 Relative-strength filter: strongest stocks in the strongest sectors; R-086 Penny-stock screen: $0.50–$2, 100,000+ shares a day, rising, earnings growth not negative; R-091 Penny-stock earnings breakout to a 52-week high on heavy volume; R-096 Rising earnings estimates from several analysts; R-097 Post-earnings drift: buy the biggest beats, sell on a miss; R-098 12-month price momentum, held for a quarter; R-099 Analyst upgrades in small caps, with a valuation check; R-100 G score: avoid growth stocks that fail most of eight quality tests; R-129 Growth company that keeps its margins, at a low PEG vs its sector; R-130 Buy a qualifying growth company after an earnings-miss sell-off; R-171 One-year top-performer screen: volatile, disputed, sub-investment-grade, smaller than the median stock; R-172 EPS-estimate dispersion: skip stocks the analysts agree on when seeking outsized one-year gains; R-174 S&P 500 entry candidate: a profitable, large-enough non-member nearing eligibility; R-179 Value Line Timeliness rank 1, held while the rank and industry rank hold; R-204 Structural share shift: unit growth far above the industry for a reason the Street hasn't written up; R-215 Momentum names: check news sentiment before buying; R-217 Pocket pivot: early buy inside a quiet base; R-218 Continuation pocket pivot: add to a winner at the 10-day line; R-219 Buyable gap-up: buy the big-volume gap, stop under the gap-day low; R-224 Too extended: no new buys 80% or more above the 200-day line; R-225 Prefer breakouts to all-time highs over breakouts below heavy overhead supply; R-227 Institutional sponsorship: owned but not saturated, and rising; R-231 Favour a high, sustained return on invested capital; R-254 Cycle-peak EPS test: hold or sell a growth holding; R-255 No promotional companies: 2–3 years of commercial sales and a year of operating profit first; R-256 Outside CEO at a large company: no new buying, re-underwrite the holding; R-258 Operating-margin leader by a modest, lasting gap; R-259 Debottlenecking: small added capital, large added output, before earnings show it; R-262 Hold a qualifying compounder through a high multiple or a feared bear market; R-265 Value a long-run compounder at its own normal multiple of the market's P/E; R-267 Capital-growth sleeve: low or no payout where reinvestment is rich; R-268 Prefer the clear profit leader to the number two or three; R-269 Industry margins widening only on price rises: no long-term buy; R-270 Research productivity: share of sales from new products; R-271 Switch only for clearly faster growth; R-272 Industry-specific cost ratio as a check on management (Point 11)

## Rules

### R-001 Trend pullback to the last higher low
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF the daily chart shows a run of higher highs and higher lows AND price pulls back toward the latest higher low without closing below it THEN buy when the advance resumes | EXIT stop just below that higher low | INVALIDATED BY a close below the latest higher low (uptrend structure broken)
Inputs: swing highs/lows → daily OHLC price history (pivot definition and run length are test parameters; the book gives none)
Sources: [BOOK Pansheriya loc.8–9]; agrees: [BOOK Regan loc.25] (buy the first pullback after a new high); agrees: [BOOK Walsh loc.31–32] (trade with the trend: buy a bounce off the up-trend line, short a bounce off the down-trend line; picking tops and bottoms is high risk)
Evidence: D — asserted; the only example uses hypothetical round prices
Conflicts: none yet
Status: UNTESTED

### R-002 Pullback to the short moving average in an uptrend
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price is above its moving averages AND the short EMA (9 or 21) is above the longer average (21 EMA or 50 SMA) AND price pulls back to the short EMA and prints a bullish reversal candle THEN buy | EXIT stop just below the EMA; exit when price closes below the average and stays there (how long is not specified — test parameter) | INVALIDATED BY the short EMA crossing below the longer average
Inputs: EMA/SMA → computed in code from daily closes; reversal candle → daily OHLC
Sources: [BOOK Pansheriya loc.9–10]; agrees: [BOOK Walsh loc.39] (buy the bounce off the moving average in an established uptrend; exit if price breaks down through it); agrees: [BOOK Broker p.264] (credits Elder: buy at the EMA 'baseline' while the stock heads up, short it on the way down); [BOOK Broker p.285–286] (example: since the uptrend began price returned to the average about three times, piercing it by about 1.5%; place a buy limit about 1% below the average, stop near entry once moving, take profit at the upper channel line; average length not stated)
Evidence: D — asserted with a hypothetical example
Conflicts: none yet
Status: UNTESTED

### R-003 Double top / double bottom neckline break
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF two troughs (peaks) form at about the same level after a downtrend (uptrend) AND price closes through the neckline between them THEN enter in the new direction (buy a double-bottom break; on a double-top break, exit longs or short) | EXIT stop beyond the second trough (peak); target = trough-to-neckline height projected from the neckline | INVALIDATED BY a close back through the neckline
Inputs: swing highs/lows and neckline → daily OHLC (the "same level" tolerance is a test parameter)
Sources: [BOOK Pansheriya loc.11]; pattern described at [BOOK Pansheriya loc.4]; agrees: [BOOK Regan loc.26] (real breaks tend to come on the third or fourth test); agrees: [BOOK Walsh loc.35–36] (stronger when the second high is slightly lower; confirmed on the break of the intervening lows; target = pattern height)
Evidence: D — asserted; hypothetical prices
Conflicts: none yet
Status: UNTESTED

### R-004 Head-and-shoulders neckline break
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF three troughs form with the middle one lowest (inverse H&S; or three peaks with the middle highest) AND price closes through the neckline THEN enter in the reversal direction | EXIT stop beyond the right shoulder; target = head-to-neckline height projected from the break | INVALIDATED BY a close back beyond the right shoulder
Inputs: swing highs/lows and neckline → daily OHLC
Sources: [BOOK Pansheriya loc.11–12]; agrees: [BOOK Walsh loc.36] (confirmed on the neckline break; target = head-to-neckline); agrees: [BOOK MoralesKacher loc.32] (gap-downs through head-and-shoulders necklines started big declines in NFLX and GMCR, 2011)
Evidence: D — asserted; hypothetical prices
Conflicts: none yet
Status: UNTESTED

### R-005 Breakout, then buy the retest
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price closes above resistance on a large candle with a volume surge (often after a consolidation) AND later pulls back to the broken level and prints a bullish reversal candle there THEN buy | EXIT stop just below the retest level; target = height of the prior range added to the breakout level | INVALIDATED BY a close back below the broken level
Inputs: resistance level, candle range, volume vs its average → daily OHLCV (size of the "surge" is a test parameter; the book gives none)
Sources: [BOOK Pansheriya loc.13–14]; agrees: [BOOK EDay loc.54–55] (a broken strong range boundary flips to resistance or support and is often retested); agrees: [BOOK Snow loc.113]; [BOOK Snow loc.114] (a break of a well-defined level often runs; one chart example); agrees: [BOOK Walsh loc.29–30] (broken support becomes resistance and vice versa); [BOOK Walsh loc.31] (a break on rising volume is more likely to carry); agrees: [BOOK Broker p.257–258] (enter on the break above resistance with improved volume; levels touched more often matter more; target the average recent swing)
Evidence: D — asserted; hypothetical prices
Conflicts: R-007 — decided by regime (a close outside the range on rising volume vs repeated rejections inside it); R-006 — decided by whether the breakout close holds beyond the level; R-217 — decided by a desk test: R-217 buys inside the base before the breakout; this rule waits for the breakout and retest
Status: UNTESTED

### R-006 Fade the failed breakout
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price pushes through resistance (support) but quickly closes back inside the prior range with weak follow-through AND a reversal candle forms THEN trade against the breakout (exit longs or short after a failed upside break; buy after a failed downside break) | EXIT stop just beyond the false-break extreme; target = the other side of the range or the prior support/resistance | INVALIDATED BY a new close beyond the false-break extreme
Inputs: range boundaries, closes, reversal candle → daily OHLC ("quickly" is a test parameter)
Sources: [BOOK Pansheriya loc.14–15]
Evidence: D — the claim that big players engineer these traps is asserted, not shown
Conflicts: R-005 — decided by whether price closes back inside the range
Status: UNTESTED

### R-007 Range trading at support and resistance
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price has respected a horizontal support and resistance several times each AND reaches support with a bullish reversal candle (or resistance with a bearish one) THEN buy at support (exit or short at resistance) | EXIT stop just outside the boundary; target = the opposite boundary | INVALIDATED BY a close outside the range
Inputs: range boundaries, touch count, reversal candle → daily OHLC (touch count and band width are test parameters)
Sources: [BOOK Pansheriya loc.16]; agrees: [BOOK Regan loc.25] (buy near support, sell near resistance, don't bet on breaks); agrees: [BOOK EDay loc.53–55] (in a large range after a trend, trade both boundaries until one breaks; avoid the middle); [BOOK EDay loc.55] (in small ranges inside a trend, trade only with the trend); agrees: [BOOK Snow loc.113] (buy support, sell resistance in a defined range); agrees: [BOOK Walsh loc.30] (a level that holds through about four tests tends to reverse price; false breaks happen)
Evidence: D — asserted; hypothetical prices
Conflicts: R-005 — decided by regime (repeated rejections inside the range with falling volume vs a close outside it on rising volume)
Status: UNTESTED

### R-008 Confluence-zone reversal entry
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF two or more independent levels sit at about the same price (trendline with at least 2 touches, prior support/resistance, 50% Fibonacci retracement, a moving average) AND a reversal candle forms there THEN enter in the reversal's direction | EXIT tight stop just beyond the zone | INVALIDATED BY a close through the zone
Inputs: trendline, support/resistance, Fibonacci and moving-average levels → computed from daily OHLC (how close the levels must be is a test parameter)
Sources: [BOOK Pansheriya loc.18–19]
Evidence: D — asserted; hypothetical example
Conflicts: none yet
Status: UNTESTED

### R-009 Per-trade risk cap
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF (entry − stop) × position size would exceed 2% of account equity THEN cut the size until it fits; if even the smallest tradable size breaks the cap, skip the trade | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: entry and stop → the trade plan; account equity → Cyrus (never assumed)
Sources: [BOOK Pansheriya loc.20]; agrees: [BOOK Salvon loc.9–10] (2% of the unleveraged deposit; skip if the minimum size breaks it); agrees: [BOOK MetaStock p.6] (3% on overnight trades, 1% on day trades), [BOOK MetaStock p.10] (under 2% per trade); agrees: [BOOK Heitkoetter loc.17] (2% while starting; later raised, see the fixed-ratio rule); agrees: [BOOK Anderson loc.40] (about 1% or less per trade; example 0.5% of $50,000 = $250); agrees: [BOOK EDay loc.83] (no more than 0.5% while starting; 2% is too much for a beginner); agrees: [BOOK Walsh loc.49–50] (example: $100 a trade on a $15,000 account, under a $200 daily limit); agrees: [BOOK Broker p.235] (swing traders risk about 0.5% a trade); [BOOK Broker p.251] (1% or less per trade plus a daily limit); [BOOK Broker p.254]; [BOOK Broker p.268] (no more than 2%); agrees: [BOOK MoralesKacher loc.181] (set the maximum loss, then the dollar and account drawdown in the worst case, before entering); agrees: [BOOK Smith p.295–296] (risk about 1% of equity per trade; 2–3% raises the risk of ruin; a third of capital per trade is a sure wipe-out)
Evidence: D — both books assert it; neither tests it
Conflicts: R-040 — decided by instrument: for long options the allocation is the risk, so R-009 governs; R-047 — decided by track record per its author, with the desk's C7 tiers governing verdicts. Note: the desk's own C7 tiers (core 1.0–1.5%, speculative 0.5–1.0%, lotto 0.5% or less) are tighter and govern verdicts.; R-080 — decided by the desk's C7 tiers, which always govern verdicts; R-121 — decided by measure: R-121 sets a long-term holding's portfolio weight; this rule and C7 cap the loss at the stop
Status: UNTESTED

### R-010 Minimum reward-to-risk of 2
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF (target − entry) ÷ (entry − stop) is below 2 THEN don't take the trade | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: entry, stop, target → the trade plan
Sources: [BOOK Pansheriya loc.20]; agrees: [BOOK Salvon loc.9] (take-profit 2–3× the stop), [BOOK Salvon loc.21]; agrees: [BOOK Regan loc.20] (at least 2×, preferably 5×); agrees: [BOOK Heitkoetter loc.17]; [BOOK Heitkoetter loc.19–20] (exactly 2:1, exit at target); agrees: [BOOK Wyckoff p.51] (anticipated profit at least three or four times the risk); agrees: [BOOK Walsh loc.52] (minimum 1:2); [BOOK Walsh loc.89] (no support or resistance, including whole numbers, within twice the risk)
Evidence: D — asserted in both books
Conflicts: R-035, R-036, R-046 — decided by instrument: stop-based share trades → R-010; defined-risk option spreads → max gain ÷ max loss plus the desk's C4–C5 gates; R-070 — decided by evidence (a measured hit rate → the higher required multiple); R-220 — decided by school: trend-following growth holdings trailed without targets → R-220; target-based swing trades → this rule
Status: UNTESTED

### R-011 Daily direction, intraday confirmation
School: day-trading | Horizon: day | Instrument: shares
IF the daily chart shows a trend and marked support/resistance AND, after the session opens, the first 2–4 hourly candles move in the daily trend's direction THEN enter in that direction | EXIT stop just beyond the nearest level; target ≈ the instrument's average daily range | INVALIDATED BY a close back through the level the stop sits behind
Inputs: daily trend and levels → daily OHLC; hourly candles → intraday OHLC; average daily range → computed from daily highs and lows
Sources: [BOOK Salvon loc.2–3]; [BOOK Salvon loc.8]
Evidence: C — one dated EUR/USD walk-through; the outcome is not reported
Conflicts: R-160 — decided by setup (see Conflicts); Intraday: recorded only; the desk does not call intraday entries.
Status: UNTESTED

### R-012 Bull-flag channel breakout
School: day-trading | Horizon: day | Instrument: shares
IF a sharp advance (flagpole) is followed by a flat or down-sloping channel with at least 3 highs and 3 lows on parallel or converging lines AND price breaks out of the top of the channel THEN buy | EXIT take profit at 0.5× the flagpole length or more, or on a reversal candle; stop just below the lower channel line | INVALIDATED BY a close below the lower channel line
Inputs: flagpole and channel pivots → 30-minute to 1-hour OHLC
Sources: [BOOK Salvon loc.13–14]; agrees: [BOOK Pansheriya loc.7] (a break of the flag continues the trend); agrees: [BOOK Walsh loc.33–34] (wait for the flag line to break; the move often equals the full flagpole); [BOOK Walsh loc.62]
Evidence: C — one chart example; author claims about $1,100 on it before spread (loc.14)
Conflicts: none yet. Intraday: recorded only.
Status: UNTESTED

### R-013 Keltner Channel close-outside breakout
School: day-trading | Horizon: day | Instrument: shares
IF an hourly candle closes outside the Keltner Channel with more than half its body outside THEN enter in the breakout direction on the next candle | EXIT on a reversal candle; stop at the channel midline or the opposite band | INVALIDATED BY a close back inside the channel
Inputs: Keltner Channel → computed from hourly OHLC (settings not given)
Sources: [BOOK Salvon loc.14–15]
Evidence: C — one annotated chart; the author marks several of its signals false and gives no win/loss tally
Conflicts: R-016 — decided by the next candle: follow-through outside the band → this rule; a close back inside → R-016 (also H1 here vs H4 there); R-066 — decided by regime (sideways range → fade; trend → follow)
Status: UNTESTED

### R-014 Fibonacci retracement: continue above 0.5, reverse below
School: day-trading | Horizon: day | Instrument: shares
IF a strong trend retraces, holds above the 0.5 level, then recrosses 0.382 back in the trend's direction THEN enter with the trend; first target 0.236, second the prior extreme | EXIT at the targets or on a trailing stop | INVALIDATED BY a break of 0.5 — the book then treats the move as a reversal (trade the other way, targets 0.786 then 0)
Inputs: swing high and low → 30-minute/1-hour OHLC; retracement levels computed in code
Sources: [BOOK Salvon loc.15–16]
Evidence: C — one CAD/CHF chart walk-through; no tally
Conflicts: none yet. Intraday: recorded only.
Status: UNTESTED

### R-015 Alligator fan-out entry
School: day-trading | Horizon: day | Instrument: shares
IF the three Alligator moving averages converge at one point and then fan out all pointing the same way, within 6 candles of the trend starting THEN enter in that direction | EXIT on a reversal pattern, a trailing stop, the slowest average turning, or the averages converging again; stop just beyond the nearest local extreme | INVALIDATED BY the fan-out arriving more than 6 candles after the trend began, or no three-way crossing
Inputs: Alligator averages (default settings) → computed from 30-minute/1-hour OHLC
Sources: [BOOK Salvon loc.16–17]
Evidence: C — one chart walk-through; no tally
Conflicts: none yet. Intraday: recorded only.
Status: UNTESTED

### R-016 EMA(5) high/low channel snap-back
School: day-trading | Horizon: day | Instrument: shares
IF on a 4-hour chart a candle closes outside the channel formed by a 5-period EMA of highs and a 5-period EMA of lows, with at least half its body outside, AND a later signal candle closes back inside the channel THEN enter in the direction of that return on the next candle | EXIT at the next reversal, or within 2–3 candles if price leaves the channel on the other side; stop 2–3 points beyond the local extreme | INVALIDATED BY the signal candle closing beyond the opposite band, or its wick reaching outside the channel
Inputs: EMA(5) of highs and of lows → computed from 4-hour OHLC
Sources: [BOOK Salvon loc.17–19]
Evidence: C — one annotated chart with five signals, one marked false; author claims about 22–25 points a trade (loc.18)
Conflicts: R-013 — decided by the next candle (a close back inside → this rule; follow-through outside → R-013). Intraday: recorded only.
Status: UNTESTED

### R-017 News and session timing filter
School: day-trading | Horizon: day | Instrument: shares
IF a high-impact scheduled release is within 30–60 minutes, OR the session opened less than 30 minutes ago, OR the close is less than 30–60 minutes away THEN don't open new intraday positions (close open ones before the release and before the close) | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: release times → economic calendar; session times → exchange calendar
Sources: [BOOK Salvon loc.19]; [BOOK Salvon loc.22]; agrees: [BOOK Regan loc.27] (avoid the first 5–15 minutes after the open); agrees: [BOOK Walsh loc.72] (novices avoid the first 30 minutes; ~09:55–10:05 and 11:00–11:15 ET are common reversal times; lunch lull; best windows ~10:00–12:00 and 14:00–16:00 ET); [BOOK Walsh loc.75] (be flat when a scheduled economic release lands mid-session; check two calendars); agrees: [BOOK Broker p.248] (best stock day-trading windows: first one to two hours after the open and the last hour)
Evidence: D — asserted
Conflicts: none yet. Intraday: recorded only.
Status: UNTESTED


### R-018 Market valuation regime: forward earnings yield vs 10-year Treasury
School: value | Horizon: position (months) | Instrument: shares
IF the S&P 500's valuation gap (index ÷ fair value − 1, where fair value = 12-month forward consensus operating EPS ÷ 10-year Treasury yield) is below −5% THEN label the market backdrop undervalued (supports adding equity exposure over the next 12 months); IF the gap is above +15% THEN label it overvalued (supports trimming and stricter entries) | EXIT the label changes when the gap moves back inside −5%…+15% | INVALIDATED BY a deflationary regime with very low bond yields, where the model implies implausibly high P/Es (the author notes it failed for Japan), or an earnings-quality shock that makes consensus EPS unreliable
Inputs: S&P 500 12-month forward consensus EPS → analyst-consensus source (FactSet / S&P / Yardeni Research; not connected yet, so the rule cannot fire until sourced); 10-year Treasury yield → Alpha Vantage TREASURY_YIELD or FRED DGS10; S&P 500 level → index quote
Sources: [BOOK Yardeni p.8]; [BOOK Yardeni p.9] (thresholds and outcomes); deflation caveat [BOOK Yardeni p.5], [BOOK Yardeni p.14]
Evidence: B — cites Ned Davis Research averages since 1980 (gap below −5% → average next-year S&P gain 31.7%; above +15% → average −8.7%), method not shown; the author says it is not a timing tool (p.17); check table p.25–27
Conflicts: R-207 — decided by input availability
Status: UNTESTED

### R-019 VIX settlement-day distortion filter
School: process | Horizon: day | Instrument: options
IF the date is a VIX futures/options settlement day (the Wednesday 30 days before the next standard monthly S&P 500 option expiry, usually the 3rd or 4th Wednesday) THEN don't read that session's VIX jump, S&P 500 option put/call ratio or option-volume spike as a sentiment signal, and size anything VIX-linked for a wider-than-normal VIX range | EXIT from the next session | INVALIDATED BY Cboe changing the settlement method away from the single opening auction
Inputs: settlement dates → Cboe expiration calendar; VIX open/high/low → daily VIX history; S&P 500 option put/call ratio and volume → Cboe daily market statistics
Sources: [BOOK Baumgartner p.15–16] (settlement mechanics); [BOOK Baumgartner p.30–31]; [BOOK Baumgartner p.33–35] (results); alternative explanations [BOOK Baumgartner p.36–37]
Evidence: A — systematic test on 2011–2019 daily data, 114 settlement days vs a trailing 10-day window (1- and 3-day for put/call), t-tests: VIX daily range +23.7% vs +6.1% on all days; put/call +22.6% vs the prior day (all days +3.1%); S&P 500 option volume +29.2% vs its 10-day average (all days +1.6%). The test establishes the settlement-day anomaly; the "discount the reading" action is the desk's application and is untested. Legitimate causes (auction liquidity, hedge unwinds) are not ruled out.
Conflicts: none yet
Status: UNTESTED


### R-020 Avoid sub-penny stocks
School: risk/sizing | Horizon: any (every trade) | Instrument: shares
IF a stock trades below $0.01 a share (OTC sub-penny) THEN don't trade or hold it | EXIT n/a | INVALIDATED BY n/a
Inputs: price → quote; listing venue → exchange data
Sources: [BOOK Regan loc.4]; agrees: [BOOK MoralesKacher loc.186–187] (a promoted shell-company stock fell from $1.24 to 3.5 cents; stick to listed stocks with institutions and real sales)
Evidence: D — asserted (heavy manipulation and illiquidity)
Conflicts: none yet
Status: UNTESTED

### R-021 Short holding limit for penny stocks
School: risk/sizing | Horizon: day | Instrument: shares
IF the stock trades under $5 (especially over the counter) THEN plan to exit within a few trading days and never hold it as an investment | EXIT at the planned day count or the stop, whichever comes first | INVALIDATED BY n/a
Inputs: price → quote; entry date → trade log (the exact day cap is a test parameter; the author says a few days)
Sources: [BOOK Regan loc.12]; [BOOK Regan loc.6–7]; agrees: [BOOK Gibbs loc.65] (when a holding spikes, sell within about an hour and no later than 3 months after the first spike)
Evidence: D — asserted; the author shows screenshots of his own winners only (loc.10)
Conflicts: R-027 — decided by strategy: short-hold penny-stock trading (this rule) vs liquid names only (R-027); for position and long-term calls R-027 wins
Status: UNTESTED

### R-022 Never add to a losing position
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF a position shows a loss THEN don't buy more to lower the average cost; add only once the trend is clearly in your favour | EXIT n/a | INVALIDATED BY n/a
Inputs: position cost and current price → position list
Sources: [BOOK Regan loc.15] (said of penny stocks); agrees: [BOOK MetaStock p.7] (no 'disaster cost averaging'); agrees: [BOOK Cayman loc.52] (averaging is unsuitable for options because they expire); agrees: [BOOK Anderson loc.13] (pride drives averaging down); agrees: [BOOK Wyckoff p.152–153] (averaging Union Pacific down without reserve capital ended in a wipe-out); agrees: [BOOK Snow loc.65] (averaging down magnified losses in 2008 bank stocks and raised sector concentration); agrees: [BOOK Osman loc.106] (sunk-cost averaging into losers; keep disciplined stops); agrees: [BOOK Broker p.226–227] (don't double up on an option position to win back a loss; close it and move on); agrees: [BOOK MoralesKacher loc.22] (a falling position is the market saying you may be wrong); [BOOK MoralesKacher loc.54] (anger leads to averaging down)
Evidence: D — asserted
Conflicts: R-083 — decided by the fundamentals since purchase: lower debt and higher earning power while the price fell → R-083; anything else → this rule; R-089 — decided by plan type: a fixed schedule set before the first purchase for a long-term holding → R-089; adding to a trade that shows a loss → this rule; R-180 — decided by plan type (see Conflicts)
Status: UNTESTED

### R-023 Don't chase past the planned entry
School: process | Horizon: swing (days–weeks) | Instrument: shares
IF price has already moved beyond the planned entry by more than a distance set in advance THEN skip the trade rather than buying late | EXIT n/a | INVALIDATED BY price returning to the planned entry zone
Inputs: planned entry and allowed distance → trade plan; price → quote
Sources: [BOOK Regan loc.25]; agrees: [BOOK Heitkoetter loc.26] (take only the first signal; if missed, find another stock); agrees: [BOOK FreemanCS loc.66] (enter spreads with a limit at the bid-ask midpoint; never chase past the ideal entry)
Evidence: D — asserted
Conflicts: R-029 — decided by reward-to-risk at the current price: still at least 3 → half now (R-029); below 3 → don't chase (this rule); R-264 — see Conflicts
Status: UNTESTED

### R-024 Broad sell-off exit for speculative names
School: risk/sizing | Horizon: day | Instrument: shares
IF the broad market is down more than 2.5% on the day THEN expect nearly every stock to move with the index; exit or don't open penny-stock and speculative small-cap positions | EXIT n/a | INVALIDATED BY n/a
Inputs: index daily change → S&P 500 quote
Sources: [BOOK Regan loc.26]
Evidence: D — the author claims almost all stocks move together on such days; no data
Conflicts: none yet
Status: UNTESTED

### R-025 200-day moving average as a sentiment gauge
School: swing-technical | Horizon: position (months) | Instrument: shares
IF price is above its 200-day moving average THEN treat the stock as in buyers' territory and favour long setups; IF it is below THEN expect rallies to be sold and favour caution or shorts | EXIT n/a (a gauge, not a trigger) | INVALIDATED BY n/a — the author says not to trade crosses of it
Inputs: 200-day simple moving average → computed in code from daily closes
Sources: [BOOK Regan loc.27]; agrees: [BOOK Snow loc.112] (crosses of the 200-day and the 50/200 golden and death crosses as signals — note the book treats crosses as signals, unlike R-025's source)
Evidence: D — asserted
Conflicts: R-050 — decided by level: this rule reads a single stock and is not traded on crosses; R-050 switches index-level exposure on the 50/200 cross, checked weekly
Status: UNTESTED


### R-026 Trade with the 12/50-day EMA trend
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF the stock's 12-day EMA is above its 50-day EMA with price above both, AND its sector and the broad market pass the same test THEN take trades only in the trend's direction (long) | EXIT take profits or tighten stops when the trend turns (the exact turn test is a parameter: a close under the 50-day EMA or the 12-day crossing under it) | INVALIDATED BY the 12-day EMA crossing below the 50-day EMA
Inputs: 12- and 50-day EMAs → computed in code from daily closes of the stock, its sector ETF and the S&P 500
Sources: [BOOK MetaStock p.6]; [BOOK MetaStock p.8] (market and sector must be in trend too); agrees: [BOOK Wyckoff p.50] (trade with the market's trend; author claims it gives three or four times the chances); agrees: [BOOK Gibbs loc.54–55] (two moving averages: short crossing above long = buy, below = sell; no lengths recommended); agrees: [BOOK Broker p.266]; [BOOK Broker p.270] (check the daily or weekly chart and trade only in the long-term trend's direction)
Evidence: D — the author's rule of thumb; no test shown
Conflicts: none yet
Status: UNTESTED

### R-027 Only positions you can exit in one day
School: risk/sizing | Horizon: any (every trade) | Instrument: shares
IF the planned position is larger than the stock's average daily volume lets you sell in a single day, OR the float is not in the millions of shares, OR the stock is low-priced THEN don't take it | EXIT n/a | INVALIDATED BY n/a
Inputs: average daily volume and float → quote and company-overview data (Alpha Vantage / FMP); position size → trade plan (the share of daily volume that counts as sellable in a day is a test parameter)
Sources: [BOOK MetaStock p.6]; agrees: [BOOK Piard loc.63–64] (illiquid names fill 5–10% worse than simulated; filter on volume, market cap or index membership); agrees: [BOOK EDay loc.60] (skip stocks averaging under 100,000 shares a day); agrees: [BOOK Gibbs loc.59]; [BOOK Gibbs loc.86] (trade no more than about 10% of a stock's daily volume, and only stocks trading at least 100,000 shares a day); [BOOK Gibbs loc.88] (a position must not be big enough to move the price); agrees: [BOOK Plotnick p.95–96] (too few shares outstanding to make a fair market; thin floats swing sharply); [BOOK Plotnick p.201] (floating supply); agrees: [BOOK Wachenheim loc.91] (liquid large caps so mistakes can be exited quickly)
Evidence: D — asserted
Conflicts: R-021 — decided by strategy: Regan's short-hold penny-stock trading vs this liquid-only rule; for position and long-term calls this rule wins; R-086 — decided by strategy: short-hold penny-stock trading → R-086 with R-021; position and long-term calls → this rule
Status: UNTESTED

### R-028 Cap the number of open positions
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF 7 or more positions are already open THEN add no new position until one closes | EXIT n/a | INVALIDATED BY n/a
Inputs: open positions → Cyrus's position list
Sources: [BOOK MetaStock p.10]; agrees: [BOOK Piard loc.54] (4–8 positions often the best return/volatility balance in his screens)
Evidence: D — the author's own practice (more than about seven is too many to watch)
Conflicts: R-200 — decided by horizon
Status: UNTESTED

### R-029 Half now, half at the ideal price
School: process | Horizon: swing (days–weeks) | Instrument: shares
IF the trade offers at least 3× reward for the risk at the current price THEN buy half the planned size now and place the other half as a limit order at the preferred entry | EXIT the trade's own stop and target | INVALIDATED BY reward-to-risk at the current price falling below 3
Inputs: entry, stop, target → trade plan; price → quote
Sources: [BOOK MetaStock p.12]
Evidence: D — the author's advice for traders who wait for a perfect entry and miss the big trends
Conflicts: R-023 — decided by reward-to-risk at the current price: still at least 3 → half now (this rule); below → don't chase (R-023)
Status: UNTESTED

### R-030 Candle reversal signal at support
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF at a support level price prints a hammer (body in the upper part of the range, lower shadow at least twice the body, little or no upper shadow) or a bullish engulfing candle (a white body wrapping the prior black body during a decline) THEN treat it as a possible base and look for a long entry, more strongly when two signals confirm the same support | EXIT a close below the pattern's low | INVALIDATED BY a close below the pattern's low
Inputs: daily OHLC; support level → prior swing lows
Sources: [BOOK MetaStock p.24]; [BOOK MetaStock p.25]; agrees: [BOOK Pansheriya loc.6]; agrees: [BOOK EDay loc.40–42] (engulfing bars as reversals only in a range forming at a trend's end; enter on close, stop at the outside bar's midpoint or beyond)
Evidence: C — two chart examples; the author notes a hammer often leads to sideways basing before any rally and calls candles a tool, not a system
Conflicts: R-064 — decided by trend context (a pause inside an established trend → R-064; a decline ending at support → R-030)
Status: UNTESTED

### R-031 ADX and MACD trend confirmation
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF the 14-period ADX is rising AND MACD is above its signal line and above zero THEN an uptrend is confirmed (long side); IF ADX is rising AND MACD is below its signal line and below zero THEN a downtrend is confirmed (avoid longs); IF after a decline ADX turns down while MACD climbs toward zero THEN expect a countertrend rally, not a new uptrend | EXIT when ADX and MACD turn down with price | INVALIDATED BY ADX and MACD no longer moving with price
Inputs: ADX(14), MACD and its signal line → computed from daily OHLC (Alpha Vantage ADX / MACD)
Sources: [BOOK MetaStock p.27–30]
Evidence: C — four chart examples; ADX 20–30 described as a mild-to-moderate trend and above 30 as strong; no tally
Conflicts: none yet
Status: UNTESTED

### R-032 Guppy multiple moving averages: rally or trend
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price breaks a downtrend while the long EMA group (30, 35, 40, 45, 50, 60 days) is still widely spread THEN treat it as a short-lived rally; IF the long group compresses, turns up and starts expanding with the short group (3, 5, 10, 12, 15 days) above it THEN treat it as a trend change and buy; IF price pulls back in an uptrend while the long group stays separated and rising THEN buy the pullback | EXIT when the long group compresses and the short group falls through it | INVALIDATED BY the long group turning down
Inputs: eleven EMAs → computed in code from daily closes
Sources: [BOOK MetaStock p.37–39]
Evidence: C — one stock analysed in real time with the author's own trade; author claims the three phases offered 11%, 49% and 30%
Conflicts: none yet
Status: UNTESTED


### R-033 Dividend trend as a health check
School: value | Horizon: long-term (years) | Instrument: shares
IF a company's dividend per share has been cut or has shrunk over several years THEN treat it as a sign of financial strain and require a stronger case before buying; IF it has paid a stable or rising dividend THEN count that as a sign of healthy finances | EXIT n/a (a screen) | INVALIDATED BY n/a
Inputs: dividend history → Alpha Vantage DIVIDENDS or company filings (how many years count as a trend is a test parameter)
Sources: [BOOK Hammond loc.22]; agrees: [BOOK Yardeni p.16–17] (cash dividends are harder to dress up than earnings); agrees: [BOOK Anderson loc.37] (prefer companies raising the dividend year after year); [BOOK Anderson loc.47]; agrees: [BOOK Zacks loc.65]; [BOOK Zacks loc.67] (dividend initiations draw a positive reaction and eliminations a stronger negative one; sell when a company eliminates its dividend; studies cited, B)
Evidence: D — asserted in a beginner primer
Conflicts: none yet
Status: UNTESTED


### R-034 Long option: breakeven inside the typical move
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF buying a call (or put) for direction THEN pick a strike at or in the money and an expiry far enough out that the breakeven (strike + premium for a call, strike − premium for a put) sits inside the move the stock typically makes over the days left | EXIT sell the option rather than exercise it (the book gives no exit level; see R-041) | INVALIDATED BY a breakeven beyond the typical move: reject the structure
Inputs: strike, premium, expiry → options chain snapshot; typical move over the same number of days → daily price history or the chain's implied move
Sources: [BOOK Cayman loc.11]; [BOOK Cayman loc.13]; [BOOK Cayman loc.45]; agrees: [BOOK Heitkoetter loc.40–42] (prefers in-the-money, never out-of-the-money); agrees: [BOOK Broker p.229] (second-hand: deep in-the-money, roughly 70-delta, longer-dated options limit time decay); agrees: [BOOK Smith p.27]; [BOOK Smith p.113] (sell rather than exercise while any time premium remains)
Evidence: D — one hypothetical worked example (an at-the-money call loses $1.50 on a $2 rise because time decay took $3.50) plus assertion
Conflicts: R-238 — see Conflicts
Status: UNTESTED

### R-035 Bull call spread in a slowing uptrend
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF the daily chart is in an uptrend (higher highs and higher lows) AND the advance is slowing while daily ranges widen THEN buy an at- or out-of-the-money call and sell a further out-of-the-money call beyond the nearest resistance, both legs 30 or more days to expiry (early in a strong trend the book prefers the plain long call, R-034) | EXIT when price clears that resistance, roll the short call up to the next resistance; close both legs if the counter-move grows too strong | INVALIDATED BY the uptrend failing (the book gives no level; a close below the latest higher low is the desk's proxy, as in R-001)
Inputs: trend, swing highs/lows, resistance → daily OHLC; widening ranges → average true range from daily OHLC (how much widening counts is a test parameter); strikes, expiry, premiums → options chain snapshot
Sources: [BOOK Cayman loc.28–29]
Evidence: D — asserted; no example trades or numbers
Conflicts: R-010 — decided by instrument (see Conflicts section)
Status: UNTESTED

### R-036 Bull put spread above strong support
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the stock is in an uptrend with a strong support level below THEN sell a put at or near the money and buy an out-of-the-money put below that support, for a net credit | EXIT if the short put moves into the money, roll the spread lower or close it | INVALIDATED BY a close below that support (the book only says to adjust; this is the desk's proxy)
Inputs: trend and support → daily OHLC; strikes, credit, expiry → options chain snapshot; assignment price and capital → computed from the short strike (desk gate C6)
Sources: [BOOK Cayman loc.29–30]; agrees: [BOOK FreemanCS loc.14–16] (worked bull put spread arithmetic); [BOOK FreemanCS loc.64] (places the short put just below support rather than near the money, for safety)
Evidence: D — asserted; no example trades or numbers
Conflicts: R-010 — decided by instrument (see Conflicts section)
Status: UNTESTED

### R-037 Pullback bigger than the prior up-leg: stop buying
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF in an uptrend the latest pullback (swing high to swing low) is larger than the up-leg before it THEN treat the uptrend as challenged and open no new longs; mirror: in a downtrend, a rebound larger than the last down-leg flags a possible turn, so open no new shorts | EXIT n/a (filter) | INVALIDATED BY a new swing high above the prior one (uptrend case)
Inputs: swing highs/lows and leg sizes → daily OHLC (pivot definition is a test parameter)
Sources: [BOOK Cayman loc.35]
Evidence: D — asserted
Conflicts: none yet (acts as a filter on R-001 and R-002 entries)
Status: UNTESTED

### R-038 Rising channel: a midline break targets the top
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price trades in a rising channel (at least 2 touches on the lower line and 2 on the upper) AND closes above the channel midline THEN expect a run to the upper line: buy with the upper line as the target | EXIT at the upper line (the book gives no stop; a close back below the midline is the desk's proxy) | INVALIDATED BY a close below the lower channel line
Inputs: channel lines, touch count, midline → daily OHLC
Sources: [BOOK Cayman loc.37]
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-039 Day-trading list: big daily movers only
School: day-trading | Horizon: day | Instrument: shares
IF the stock's typical daily move is at least 3% or at least $1.50 THEN it qualifies for the day-trading list; otherwise skip it | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: typical daily move → average daily range (high − low) over a recent window from daily OHLC (window length is a test parameter)
Sources: [BOOK Cayman loc.41]; agrees: [BOOK Walsh loc.80–81] (daily high–low range of $1 or more, volume of 1–1.5 million shares, price $20–$100); agrees: [BOOK Broker p.255] (pick day trades by liquidity, volatility and average daily volume); [BOOK Broker p.259] (momentum: some stock moves 20–30% on most days; hold until reversal signs or shrinking volume)
Evidence: D — asserted
Conflicts: none yet. Note: the desk records day-trading rules but does not call intraday entries
Status: UNTESTED

### R-040 Allocate 3–5% of capital per trade
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF a new trade would use more than 5% of investment capital THEN cut it to 3–5% | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: position cost → trade plan; capital → Cyrus (never assumed)
Sources: [BOOK Cayman loc.46]; [BOOK Cayman loc.58]; agrees: [BOOK Heitkoetter loc.44] (rarely more than 5% of trading funds in one trade); agrees: [BOOK Gibbs loc.53] (cap each purchase at a set share of the portfolio; example $500 of $10,000); agrees: [BOOK LopezLira p.260] (cap each long or short at a fixed share of the portfolio, examples 1–10%; trim when a winner exceeds it)
Evidence: D — asserted
Conflicts: R-009 — decided by instrument: when the whole stake can be lost (a long option) the allocation is the risk, so R-009 and the desk's C7 tiers govern
Status: UNTESTED

### R-041 Trail a long option 5% below its high once it hits target
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a long option's price reaches the planned profit target THEN trail a stop 5% below the highest option price since (the book's example: cost $80, stop $70, target $100) | EXIT when the option falls to the trailing level | INVALIDATED BY n/a
Inputs: option price → options chain or broker quotes; entry, stop and target → trade plan
Sources: [BOOK Cayman loc.53]
Evidence: D — hypothetical numbers only ($100 target → $95 trail; $150 → $142.50)
Conflicts: none yet. Tension with the principle to place stops at chart levels [BOOK MetaStock p.15]; trail width is a test parameter (the book warns that too tight triggers often and too wide gives gains back)
Status: UNTESTED

### R-042 Favour stocks that beat analyst estimates
School: growth/momentum | Horizon: swing (days–weeks) | Instrument: shares / options
IF the latest reported EPS beat the consensus estimate THEN keep the stock on the long-side list (the author asserts that companies beating forecasts tend to keep succeeding) | EXIT n/a (filter) | INVALIDATED BY a later quarter that misses
Inputs: reported EPS and consensus estimate → earnings data (Alpha Vantage EARNINGS, FMP or Financial Datasets)
Sources: [BOOK Cayman loc.20]; agrees: [BOOK Zacks loc.86–87] (top-10% surprises beat the market over the next quarter across 30 years of studies, B; R-097 is the tested form)
Evidence: D — asserted; no data
Conflicts: none yet
Status: UNTESTED

### R-043 Go long only with rising revenue
School: growth/momentum | Horizon: swing (days–weeks) | Instrument: shares / options
IF considering a long position THEN check annual revenue: rising year over year → aligned; flat or falling → don't go long (the book links falling revenue to falling profits and price) | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: annual revenue, 3–5 years → latest 10-K or a financial-data connector (how many rising years count is a test parameter)
Sources: [BOOK Cayman loc.21]; [BOOK Cayman loc.20]; agrees: [BOOK Piard loc.56–57] (sales up over 5% a year is one leg of a tested growth screen); agrees: [BOOK Anderson loc.45–46] (rising profits and rising sales are the first two of ten traits; sales are harder to fake than earnings)
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED


### R-044 PowerX: first bar with all three indicators aligned
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares / options
IF on daily bars Slow Stochastic %K (14,3,3) is above 50 and rising AND RSI(7) is above 50 and rising AND MACD (12,26,9) is above its signal line and rising (a green bar), and this is the first green bar of the move THEN place a buy stop $0.01 above that bar's high and keep it working while bars stay green (shorts mirror: all three below and falling, sell stop $0.01 under the first red bar's low) | EXIT stop and target per R-045; close at the next open after a black bar (indicators disagree); close after 20 days if neither stop nor target has hit | INVALIDATED BY a black bar before the fill (cancel the order); a missed first signal is never chased
Inputs: Slow Stochastic, RSI, MACD and the 7-day average daily range → computed from daily OHLC price history
Sources: [BOOK Heitkoetter loc.21–26]; [BOOK Heitkoetter loc.30–31]; [BOOK Heitkoetter loc.65]
Evidence: C — chart examples only; author claims 61% on one stock over 12 months vs 16% buy-and-hold [BOOK Heitkoetter loc.22]; the 20-day exit comes from his own log, no numbers shown
Conflicts: R-082 — decided by strategy: PowerX swing trades with ADR stops → this rule; trades that expect an immediate move → R-082's 2–3 day time stop
Status: UNTESTED

### R-045 ADR stop and target: 1.5× and 3× the 7-day range
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares / options
IF entering a swing trade THEN set the stop 1.5 × ADR(7) from entry and the target 3 × ADR(7) from entry, where ADR(7) is the average of daily high minus low over the last 7 trading days; place both orders right after the fill | EXIT at the stop or the target | INVALIDATED BY n/a
Inputs: daily high and low, 7 days → daily OHLC price history; entry → fill price
Sources: [BOOK Heitkoetter loc.27–30]; agrees: [BOOK Broker p.287] (measure typical volatility, e.g. ATR, and set the stop outside it); [BOOK Broker p.262] (or a multiple of the per-minute move intraday)
Evidence: C — the author's experience across market environments, worked examples only; no test shown
Conflicts: none yet. Gives R-010's 2:1 by construction
Status: UNTESTED

### R-046 PowerX options: in-the-money, 30–45 days, managed on the stock
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a R-044 stock signal fills (the stock trades through the signal bar) THEN buy an in-the-money call (a put for shorts) with 30–45 days to expiry, never out of the money, so the 10–20-day hold ends before the last 3 weeks of fast decay | EXIT close the option when the STOCK hits its R-045 stop or target or prints a black bar; don't put stop orders on the option itself, because option quotes are wider | INVALIDATED BY the same conditions as R-044
Inputs: stock signal and exits → daily OHLC; strike, expiry, bid/ask → options chain snapshot
Sources: [BOOK Heitkoetter loc.28]; [BOOK Heitkoetter loc.37]; [BOOK Heitkoetter loc.40–43]; agrees: [BOOK MoralesKacher loc.184] (when an option stands in for stock, measure the stop on the stock)
Evidence: C — one example using the author's software estimates (ITM 1:1.7, ATM 1:1.6, OTM 1:1.2 reward:risk) and one filled example (+85% vs +9% on the stock) [BOOK Heitkoetter loc.39]
Conflicts: R-010 — decided by instrument (see Conflicts section); R-071 — decided by the desk's C4 move check on a real chain; R-237 — see Conflicts
Status: UNTESTED

### R-047 Raise risk only after proven profits (fixed ratio)
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF trading has been profitable 4 weeks in a row AND equity has grown by twice the current per-trade risk since the last step THEN raise per-trade risk by one step (one step = the starting 2% amount); IF the account is losing THEN cut per-trade risk (anti-martingale) | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: weekly P&L and equity → Cyrus's trade log and account (never assumed); current per-trade risk → trading plan
Sources: [BOOK Heitkoetter loc.45]; [BOOK Heitkoetter loc.47–49]; agrees: [BOOK Walsh loc.110–111] (start live at 100 shares; add 100 only after consistent profit, e.g. $1,000 at the current size or 4 profitable days in 5; halve size after a losing run; back to the simulator if losses continue)
Evidence: D — projections only (the step threshold is read off the book's worked table: +$400, +$800, +$1,200); the Vince experiment it cites (B) shows sizing matters but doesn't test this scheme
Conflicts: R-009 — decided by track record per the author; the desk's C7 tiers govern every verdict regardless
Status: UNTESTED

### R-048 40 paper trades and 4 profitable weeks before real money
School: process | Horizon: any (every trade) | Instrument: shares / options
IF a strategy has fewer than 40 round-trip simulated trades, or has not been profitable in simulation for 4 weeks THEN don't trade it with real money; apply the same gate to any tweak of a working strategy | EXIT n/a (gate) | INVALIDATED BY n/a
Inputs: simulated trades and weekly results → Cyrus's simulator or paper log (the desk's PAPER counts are the equivalent for its calls)
Sources: [BOOK Heitkoetter loc.50–51]; [BOOK Heitkoetter loc.54]; [BOOK Heitkoetter loc.59–60]; agrees: [BOOK EDay loc.82–84] (1,000 simulated trades, then a 6-month demo that must be net profitable within the drawdown limits); agrees: [BOOK FreemanCS loc.72] (paper-trade a new platform first); [BOOK FreemanCS loc.79] (watch a new underlying for 2–6 months, through an earnings season, before trading it); agrees: [BOOK Wyckoff p.17–18] (two or three years of paper practice before real money); agrees: [BOOK FreemanCC loc.107] (keep paper trading alongside live trading until at least 100 live trades); agrees: [BOOK Walsh loc.109–110] (simulate honestly until regularly profitable before going live)
Evidence: D — asserted (the author calls 40 trades statistically relevant without showing why)
Conflicts: none yet. A principle elsewhere cites 500 practice trades for day traders
Status: UNTESTED

### R-049 Account circuit breaker
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF the account's loss hits the preset daily, weekly or per-trade limit, or its drawdown from peak hits the preset catastrophic limit (the book's examples: 10%, 15%, 20%) THEN stop opening trades until the limit resets or the plan is reviewed | EXIT n/a | INVALIDATED BY n/a
Inputs: equity and peak equity → Cyrus's account history; limits → Cyrus's trading plan (the desk never sets them for him)
Sources: [BOOK Heitkoetter loc.58]; agrees: [BOOK EDay loc.83–84] (starting limits: stop after 3 straight losses in a session, 2% a week, 4% a month); agrees: [BOOK Wyckoff p.154–155] (after an unprofitable stretch, suspend operations until the cause is found; practise on paper or with tiny lots); agrees: [BOOK Walsh loc.49–50] (daily loss limit ends the day; four limit days in a row → fifth day off; three losing weeks → fourth week off; sized so a beginner survives six months); agrees: [BOOK Broker p.251] (set a daily risk limit alongside the per-trade limit)
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED


### R-050 Index trend filter: S&P 500 50-day above 200-day
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF at the weekly check the S&P 500's 50-day simple moving average is above its 200-day THEN hold the equity book (index ETFs, sector ETFs or stocks); IF it is at or below THEN move the equity book to cash or 7–10-year Treasuries | EXIT at the first weekly check with the 50-day at or below the 200-day | INVALIDATED BY n/a (a filter; it lagged buy-and-hold in the 2009–2012 uptrend)
Inputs: S&P 500 daily closes → 50- and 200-day SMAs computed in code, ending the day before the decision
Sources: [BOOK Piard loc.17–20]; [BOOK Piard loc.21–22]; [BOOK Piard loc.27]; agrees: [BOOK Wyckoff p.98–100] (no new investment unless the market's long trend is up; the market discounts business 6–12 months ahead)
Evidence: A — simulated 2000–2013 on the S&P 500 ETF: CAGR 5.8% / max drawdown −17.0% vs 1.8% / −55.4% buy-and-hold, 15 trades in 13 years; same filter on five index ETFs 7.0% / −17.9%, on S&P 500 stocks 8.2% / −22.4%; cites Faber 1900–2008 (10-month average: 10.5% / −50.3% vs 9.2% / −83.7%) [BOOK Piard loc.20]
Conflicts: R-025 — decided by level: R-025 reads a single stock and says not to trade its crosses; this rule switches index-level exposure on the 50/200 cross, checked weekly; R-260 — see Conflicts
Status: UNTESTED

### R-051 Sector rotation: top 6 by 20-day return, Treasuries when the filter is off
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF R-050 is on THEN each week rank the 11 broad US sector ETFs by 20-day return, take the top 6, keep only those whose own 50-day average is above their 200-day, and hold them equal weight; IF R-050 is off THEN hold a 7–10-year Treasury ETF (only while its own 50-day is above its 200-day, else cash) | EXIT a holding leaves when it drops out of the top 6 or below its own 50/200 cross at a weekly check | INVALIDATED BY n/a
Inputs: sector and Treasury ETF daily closes → 20-day returns and 50/200-day SMAs computed in code; S&P 500 closes for R-050
Sources: [BOOK Piard loc.22–24]; [BOOK Piard loc.28–30]
Evidence: A — simulated 2002-08 to 2013-01 with 0.1% costs: CAGR 12.3% / max drawdown −16.2% / Sortino 0.79 (9.3% without the Treasury leg; S&P 500 6.8% / −55.4%); before the bond leg, 20- to 200-day lookbacks all gave 8–10% and 4–11 holdings all 8.8–9.8%; 4-week rebalancing: worst start 10.5% / −22.5%
Conflicts: none yet
Status: UNTESTED

### R-052 Global asset rotation: top 5 of 7 by 120-day return
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF it is the weekly check THEN rank 7 asset-class ETFs (7–10-year Treasuries, 20+-year Treasuries, S&P 500, Europe, Latin America, Pacific ex-Japan, US REITs) by 120-day return, take the top 5, keep those whose own 50-day average is above their 200-day, each capped at 20% (the rest in cash) | EXIT a holding leaves when it drops out of the top 5 or below its own 50/200 cross | INVALIDATED BY n/a
Inputs: ETF daily closes → 120-day returns and 50/200-day SMAs computed in code
Sources: [BOOK Piard loc.24–26]; [BOOK Piard loc.30–32]
Evidence: A — simulated 2003-06 to 2013-01 (about 9.6 years, 0.1% costs): CAGR 15.3% / max drawdown −13.7% / Sortino 0.96 / Kelly 0.20, longest drawdown 88 weeks; the trend filter alone 11.2% / −11.4% vs buy-and-hold 11.9% / −45.8%; 60- to 200-day lookbacks all beat the filter alone; cites Faber 1973–2008 (over 11%, drawdown under 10%) [BOOK Piard loc.26]
Conflicts: none yet
Status: UNTESTED

### R-053 Paired switch: stock index vs long Treasuries on 60-day return
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF it is the 4-week rebalance date THEN hold 100% in whichever of a broad stock index ETF (mid- and small-cap indexes did best; single-sector ETFs don't suit) or a 20+-year Treasury ETF had the higher 60-day return | EXIT switch at the next rebalance if the other leg leads | INVALIDATED BY stocks and long Treasuries turning positively correlated (the author's stated condition; the correlation window is a test parameter)
Inputs: ETF daily closes → 60-day returns and rolling stock–bond return correlation computed in code
Sources: [BOOK Piard loc.32–35]; concept from Maewal & Bock (2011) [BOOK Piard loc.73]
Evidence: A — simulated 2002-08 to 2013-01 with 0.1% costs: mid-cap version 18.1% / −22.9% / Sortino 1.12 (17.8–22% across 4 start dates) vs buy-and-hold 9.9% / −55.4%; S&P 500 version 12.2% / −17.7%; emerging-markets version 20.3–24.1% (2003–2013)
Conflicts: none yet
Status: UNTESTED

### R-054 Four-season calendar: stocks March–April and October–December
School: process | Horizon: position (months) | Instrument: shares
IF the date is 1 March–30 April or 1 October–31 December THEN hold a broad stock index ETF; IF 1 January–end of February or 1 May–30 September THEN hold long Treasuries, or cash when unsure about bonds (simpler two-season version: stocks 1 November–30 April, out 1 May–31 October) | EXIT on the calendar switch dates | INVALIDATED BY n/a (the author warns long Treasuries are not an all-weather shelter)
Inputs: calendar dates; ETF prices → broker quotes
Sources: [BOOK Piard loc.37–43]; [BOOK Piard loc.70]; agrees: [BOOK Zacks loc.101–102] (sell-in-May holds in many countries, Southern Hemisphere included; over 17 years, selling on 1 May and buying back six trading days before the end of October beat buy-and-hold; author suspects data mining, B)
Evidence: A — simulated 2002-08 to 2013-01 with 0.1% costs: S&P 500 version 17.6% / −35.5% vs buy-and-hold 6.8% / −55.4%; Nasdaq-100 20.3% / −35.0%; Germany 27.2% / −38.4%; a 2011 Treasury surge helped [BOOK Piard loc.42]. Dow by season 1950–2011: May–October compounded to −10.2%, November–April to +6,920% [BOOK Piard loc.70]; Jacobsen & Zhang (2012), 1693–2009, 108 countries (B)
Conflicts: R-109 — decided by a desk test on the same index data: both are calendar switches and disagree in March–April and October–December after a negative January
Status: UNTESTED

### R-055 Market filter: S&P 500 EPS estimate vs 15 weeks ago
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF at the 4-week check the S&P 500's current-year consensus EPS estimate is below its value 15 weeks earlier THEN sell the stock-screen portfolios (R-056, R-057, R-058) into cash or Treasuries; buy back when it is strictly above | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: S&P 500 current-year consensus EPS estimate, weekly history → analyst-consensus source (not connected yet, so the rule cannot fire until sourced)
Sources: [BOOK Piard loc.54]; [BOOK Piard loc.58–59]
Evidence: A — simulated 2001–2013: without it the three screens made 12–17% a year but drew down 55–65%; with it, −17.3% to −28.5%; it beat an equal index short (hedge) on return and Sortino for all three
Conflicts: none yet
Status: UNTESTED

### R-056 Value screen: cheap on book, cash flow and earnings, low debt
School: value | Horizon: position (months) | Instrument: shares
IF an S&P 500 stock has price/book (last quarter) below 8, price/cash flow per share (TTM) below 10, P/E excluding extraordinary items (TTM) below 20, and an average analyst rating of hold or better THEN rank the passers by lowest total debt/equity and hold the top 6 equal weight, rebalanced every 4 weeks, while R-055 is on | EXIT a holding leaves when it fails the screen or the top 6 at a rebalance | INVALIDATED BY R-055 turning off
Inputs: P/B, P/CF, P/E, debt/equity → latest 10-Q/10-K via FMP or Financial Datasets; analyst consensus rating → FMP analyst data; index membership → current S&P 500 list
Sources: [BOOK Piard loc.54–56]
Evidence: A — simulated 1999–2013 with 0.2% costs: top 6 CAGR 14.6% / max drawdown −28.5% / Sortino 0.64 vs the S&P 500 ETF 3.0% / −55.4%; top 10 14.0%, top 20 12.1%
Conflicts: R-171 — decided by sleeve (see Conflicts)
Status: UNTESTED

### R-057 Growth screen: rising EPS and sales, not overbought, low debt
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF an S&P 500 stock's EPS grew more than 5% vs the previous quarter AND sales grew more than 5% vs the same quarter a year earlier AND price/cash flow (quarterly) is below 8 AND RSI(14) is below 70 THEN rank by lowest total debt/equity and hold the top 4, each capped at 25%, rebalanced every 4 weeks, while R-055 is on | EXIT a holding leaves when it fails the screen or the top 4 | INVALIDATED BY R-055 turning off
Inputs: quarterly EPS and sales, P/CF, debt/equity → 10-Q via FMP or Financial Datasets; RSI(14) → computed from daily closes
Sources: [BOOK Piard loc.56–57]
Evidence: A — simulated 1999–2013 with 0.2% costs: top 4 CAGR 20.0% / max drawdown −25.3% / Sortino 0.92; top 6 15.2%, top 10 13.3%; few names pass (18 at writing)
Conflicts: none yet
Status: UNTESTED

### R-058 Dividend screen: yield over 4% now and over 5 years
School: value | Horizon: position (months) | Instrument: shares
IF an S&P 500 stock outside utilities has a current dividend yield above 4% AND a 5-year average yield above 4% AND short interest below 5% of float THEN rank by lowest total debt/equity and hold the top 10, each capped at 10%, rebalanced every 4 weeks, while R-055 is on | EXIT a holding leaves when it fails the screen or the top 10 | INVALIDATED BY R-055 turning off
Inputs: dividend and price history → FMP or Alpha Vantage DIVIDENDS; short interest and float → FMP or exchange short-interest data; debt/equity → 10-Q
Sources: [BOOK Piard loc.57–58]; agrees: [BOOK Trefz p.40] (for REITs, the lowest short-interest fifth earned a positive risk-adjusted return 1999–2019, supporting the low-short-interest leg)
Evidence: A — simulated 2001–2013 with 0.2% costs: CAGR 14.3% / max drawdown −17.3% / Sortino 0.89; a 50/25/25 mix with the value and growth screens: 16% / −10.4% on 4-week closes [BOOK Piard loc.59–60]
Conflicts: R-062 — decided by the yield's history (5-year average above 4% → R-058; a new spike above 5% from a falling price → R-062's warning)
Status: UNTESTED

### R-059 Strategy acceptance gate
School: process | Horizon: any (every strategy) | Instrument: shares / options
IF a strategy's backtest covers fewer than 10 years or 100 decision points, misses a bull, bear or sideways period, or shows CAGR under 15%, max drawdown over 30% (or well above its CAGR), Sortino under 0.9 or Kelly under 0.2, or results that swing with start date, holding count or small parameter changes THEN don't adopt it; don't start one that sits in its longest historical drawdown; run at least three strategies on different rationales | EXIT quarantine a live strategy whose real results diverge from its simulation without an explanation | INVALIDATED BY n/a
Inputs: backtest statistics → the desk's own backtests in code; live vs simulated results → calls ledger and trade log
Sources: [BOOK Piard loc.12–13]; [BOOK Piard loc.66–68]
Evidence: D — the author's own standards, not themselves tested (he also accepts drawdowns up to 35% inside a combined portfolio [BOOK Piard loc.67])
Conflicts: none yet. Note: the desk can use it to judge a rule's move to TESTED
Status: UNTESTED


### R-060 Margin of safety: price at most two-thirds of intrinsic value
School: value | Horizon: long-term (years) | Instrument: shares
IF price ≤ 2/3 of estimated intrinsic value per share (margin of safety = 1 − price ÷ intrinsic value ≥ 33%) AND earnings have grown about 7% a year or more, rising year after year, AND debt/equity (total liabilities ÷ equity) is low THEN the stock qualifies as a long-term value buy | EXIT n/a in the book (hold for months or years) | INVALIDATED BY earnings no longer rising, or price rising above intrinsic value less the margin
Inputs: price → price history; intrinsic value → the desk's B3 valuation (two methods; DCF inputs [ESTIMATED]); annual EPS, total liabilities, equity → latest 10-K/10-Q via FMP or Financial Datasets; "low" debt/equity has no threshold in the book (the example is 0.5) — a test parameter
Sources: [BOOK Anderson loc.32–33]; agrees: [BOOK Ramnarayanan p.44] (buy below fair value; the gap is the margin of safety and the extra return; no fixed threshold); agrees: [BOOK Snow loc.77] (buy at about two-thirds of true value or less); agrees: [BOOK Wachenheim loc.9] (margin of safety; no percentage given)
Evidence: D — asserted with hypothetical examples; no test
Conflicts: none yet (the desk's own B3 margin is 20%; this book asks for about 33%)
Status: UNTESTED

### R-061 20% stop from cost, 20% trailing stop from the peak
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a growth holding falls 20% below its purchase price THEN sell it; IF a holding in profit falls 20% from its highest price since purchase THEN sell it (the book's example: bought $10, peak $80, sell by $64) | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: purchase price and price history since purchase → position list and daily closes
Sources: [BOOK Anderson loc.34]; agrees: [BOOK Gibbs loc.52–53] (for stocks expected to swing widely, a stop near 25% below cost rather than 5–10%, to avoid whipsaws)
Evidence: D — asserted with a hypothetical example
Conflicts: R-090 — decided by instrument and horizon: penny-stock trades take 20–30% within days (R-090); growth holdings kept for months → this rule. Looser than the chart-level stops in the swing rules; the horizon decides; R-119 — decided by school and horizon: valuation-based long-term holdings → R-119; growth holdings managed on price → this rule; R-199 — decided by school; R-220 — decided by a desk test on the same growth holdings; R-221 — decided by entry type: a buy at a defined pivot → R-221's 7–8%; a wide-swinging holding bought without a pivot → this rule; R-262 — see Conflicts
Status: UNTESTED

### R-062 Dividend yield above 5%: check for a yield trap
School: value | Horizon: long-term (years) | Instrument: shares
IF a stock's dividend yield is above 5% THEN treat it as a warning that the company may be failing and using the dividend to attract buyers: require rising revenue, low debt/equity and no falling price trend before counting it as a dividend buy; the book's preferred zone is quality payers yielding about 2–3% (it also names 3% as a minimum to keep up with inflation) | EXIT n/a (a screen) | INVALIDATED BY n/a
Inputs: dividend per share and price → FMP or Alpha Vantage DIVIDENDS plus daily closes; revenue, debt/equity → 10-K/10-Q
Sources: [BOOK Anderson loc.69]; [BOOK Anderson loc.37–38]; agrees: [BOOK Snow loc.74] (Fidelity data cited: about 9% of the highest yielders cut within a year on average, about 40% in 2009)
Evidence: C — one case (a retailer that raised its dividend to about 11% while its share price fell); otherwise asserted
Conflicts: R-058 — decided by the yield's history: R-058 requires a 5-year average yield above 4% plus short interest under 5% and ranks by low debt, which screens out a yield that spiked because the price collapsed; a yield above 5% that is new relative to the 5-year average → this rule's warning governs; R-116 — not a contradiction: R-116 uses the stock's own yield range and is invalidated when dividend growth stalls; R-176 — decided by universe and construction (see Conflicts)
Status: UNTESTED


### R-063 Inside-bar cluster: trade the break in the trend's direction
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares / options
IF price is trending AND a large bar in the trend's direction is followed by one or more bars whose ranges sit inside it (more inside bars = stronger, per the author) THEN place a stop order to enter on a break beyond the large bar in the trend's direction | EXIT stop beyond the smaller inside bars; target a preset R multiple | INVALIDATED BY a break the other way, or the pattern appearing inside a sideways range (the author says never trade it in ranges)
Inputs: daily or hourly OHLC → price history; trend state → the trend/range reading (how many bars define the trend is a test parameter)
Sources: [BOOK EDay loc.36–38]; [BOOK EDay loc.52]
Evidence: D — chart examples only
Conflicts: none yet
Status: UNTESTED

### R-064 Pin bar or two-bar reversal as a continuation in a trend pause
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares / options
IF price is trending AND during a short sideways pause it prints a pin bar (small body, long tail for longs / long wick for shorts) or a two-bar reversal pointing back in the trend's direction THEN enter at market on that bar's close in the trend's direction | EXIT stop beyond the pin's tail (or, for a two-bar reversal, at the midpoint of the two bars if they are large, beyond them if small); target a preset R multiple | INVALIDATED BY a pin against an established trend — the author treats those as invalid and warns that trading pins as reversals is how traders lose
Inputs: daily or hourly OHLC → price history; trend state → the trend/range reading
Sources: [BOOK EDay loc.38–40]; [BOOK EDay loc.42]; [BOOK EDay loc.52]
Evidence: D — chart examples; the author says this contradicts most books
Conflicts: R-030 — decided by trend context: a pause inside an established trend → this rule; a decline ending at support or a range forming after a trend → R-030
Status: UNTESTED

### R-065 Buying climax at the end of an ageing trend: stop buying, tighten, exit
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF an uptrend's sideways pauses have been getting longer and deeper AND the advance is coming mainly from opening gaps rather than intraday gains AND a bar prints far larger than recent bars on volume far above average THEN open no new longs and move stops close; exit on the first large bearish engulfing or two-bar reversal that follows (mirror for downtrends) | EXIT as stated | INVALIDATED BY price resuming small, orderly pauses with normal volume
Inputs: daily or hourly OHLCV → price history (what counts as 'far larger' bar size and volume is a test parameter; the book gives none); gaps → open vs prior close
Sources: [BOOK EDay loc.43–45]; [BOOK EDay loc.47–51]; agrees: [BOOK MoralesKacher loc.70] (silver April 2011: up 8 days in a row and 16 of 18, a huge pre-open gap, record volume and a mid-range close → sold the whole position); [BOOK MoralesKacher loc.141] (an exhaustion gap after a parabolic run is not buyable); [BOOK MoralesKacher loc.177] (climax runs come after months of advance; be ready to sell)
Evidence: C — one case (a large-cap EV maker's hourly chart, Dec 2019–Feb 2020: growing ranges, gap-driven rise, a volume surge and a gap of over $100, then a bearish engulfing bar); hindsight
Conflicts: none yet
Status: UNTESTED

### R-066 Bollinger Band fade inside a range
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price is in a sideways range (not trending) AND a bar pokes below the lower Bollinger Band (20-bar average; the book says 3 standard deviations) THEN buy on that bar's open or close, or with a stop order at the band; mirror at the upper band for shorts | EXIT at the opposite band or a preset R multiple; stop beyond the band extreme | INVALIDATED BY the range turning into a trend (the author says bands fail in trends)
Inputs: Bollinger Bands(20, 3) → computed from daily or hourly closes (Alpha Vantage BBANDS); range vs trend → the trend/range reading
Sources: [BOOK EDay loc.68–69]
Evidence: D — one chart example
Conflicts: R-013 — decided by regime: in a range, a close outside the band is faded (this rule); in a trend, a close outside the channel is followed (R-013, intraday); MoralesKacher principle (oscillators fight trends) — decided by regime: ranges → this rule; trending leaders → avoid
Status: UNTESTED

### R-067 DeMarker oversold buys inside a range within an uptrend
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price is in a range within an uptrend (or a late-trend range) AND the DeMarker oscillator drops into its oversold zone (about 0.3 or lower) THEN buy in the trend's direction; at a range that forms after a trend has ended, also short when DeMarker drops back from overbought (about 0.7 or higher) | EXIT stop below the range's bottom boundary; target the range top or a preset R multiple | INVALIDATED BY a clean trend (the author says oscillators stay pinned in trends and must not be used there) or a close below the range
Inputs: DeMarker(14) → computed from daily or hourly highs and lows (period not given in the book; a test parameter); range boundaries → price history
Sources: [BOOK EDay loc.67–68]
Evidence: D — one chart example; the author says some of the seven marked entries lose
Conflicts: MoralesKacher principle (oscillators fight trends) — decided by regime: ranges → this rule; trending leaders → avoid
Status: UNTESTED

### R-068 ADX rising above 25 with higher lows inside a base: early breakout entry
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF price has been in a large sideways range AND it is making higher lows toward the range top AND ADX rises above 20–25 THEN buy before or near the breakout, keyed to the higher lows rather than the ADX value | EXIT stop below the latest higher low; target a preset R multiple | INVALIDATED BY a lower low inside the range
Inputs: ADX(14) → computed from daily or hourly OHLC (Alpha Vantage ADX); swing lows and range top → price history
Sources: [BOOK EDay loc.69–71]
Evidence: C — one case (hourly chart of a large-cap EV maker, Oct 2019, ahead of a gap up)
Conflicts: none yet (complements R-031, which reads ADX inside an established trend)
Status: UNTESTED

### R-069 Relative-strength filter: strongest stocks in the strongest sectors
School: growth/momentum | Horizon: swing (days–weeks) | Instrument: shares / options
IF the S&P 500 is in an uptrend THEN consider longs only in sectors outperforming the index and, within them, the strongest stocks; IF it is in a downtrend THEN consider shorts only in the weakest stocks of sectors lagging the index; a technical entry is still required | EXIT n/a (a filter) | INVALIDATED BY the index trend flipping
Inputs: S&P 500 and sector index prices → daily closes (sector ETFs as proxies); stock vs sector return → daily closes (look-back window not given; a test parameter)
Sources: [BOOK EDay loc.60–61]; agrees: [BOOK Wyckoff p.102–104] (pick the industries likely to do best; some groups rise while the market falls); agrees: [BOOK Walsh loc.101–102] (intraday top-down: on a strong market day find the strongest sector, then its strongest stocks); agrees: [BOOK MoralesKacher loc.26] (the stock's and the market's relative strength are the best predictors of continued strength)
Evidence: D — asserted
Conflicts: none yet. Caution: a tested principle found short-term momentum ranking failed on single S&P 500 stocks while working on sectors [BOOK Piard loc.36]
Status: UNTESTED

### R-070 Set the target multiple from your measured hit rate
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF a strategy's hit rate h is known from at least several hundred recorded trades THEN require a target of at least (1 − h) ÷ h times the risk, plus a margin (the book: a 30% hit rate needs about 2.5R); size every trade as risk per trade ÷ (entry − stop), with the stop at the nearest relevant support or resistance, so size varies but R stays fixed | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: hit rate and average win/loss → the strategy's trade log or simulation report; entry and stop → the trade plan; account equity → Cyrus
Sources: [BOOK EDay loc.73–78]
Evidence: D — the breakeven arithmetic is shown and correct (30% hit, +3/−1 vs 90% hit, +1/−10), but the rule is not tested
Conflicts: R-010 — decided by evidence: no measured hit rate yet → R-010's fixed 2:1 floor; a measured hit rate → this rule's required multiple, whichever is higher
Status: UNTESTED

### R-071 Swing options: buy, 30+ days to expiry, slightly out of the money
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a swing setup calls for an option instead of shares THEN buy (never sell) the option: a call for a bullish view, a put for a bearish one, with at least 30 days to expiry, struck some distance out of the money for leverage, and exit before expiry | EXIT when the stock setup exits or hits target; the premium is the maximum loss and the exit must recover it | INVALIDATED BY the stock setup failing
Inputs: strike, expiry, bid/ask → options chain snapshot; stock setup → the share rule that triggered it
Sources: [BOOK EDay loc.15–16]
Evidence: D — asserted with one hypothetical example
Conflicts: R-046 — decided by the move check: the desk's C4 gate (breakeven inside the typical move) decides between the in-the-money choice of R-046 and this rule's out-of-the-money choice; agrees with R-046 on 30+ days and on buying rather than selling; R-237 — see Conflicts
Status: UNTESTED


### R-072 SPY bull put spread after a cross above the 50-day average
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF SPY closes back above its 50-day moving average THEN sell a put spread about 30 days to expiry with the short put near 0.31 delta | EXIT take profit at 50% of the maximum credit; losing trades in the test were held to maximum loss | INVALIDATED BY n/a in the book (the desk's gates C3–C6 still apply)
Inputs: SPY daily closes and 50-day average → price history; strikes, deltas, bid/ask, expiry → options chain snapshot
Sources: [BOOK FreemanCS loc.52]
Evidence: A — the authors report a backtest on SPY options, 2009–2019: 211 trades, 90.5% winners, 433% total profit; also net positive over 46 trades when 2007–09 is included. Check: spread width, costs and fill assumptions are not shown, and the text mixes up the 50-day average with the 50/200 golden cross
Conflicts: R-074 — decided by a test: this rule's 50% take-profit with losers run to maximum loss vs R-074's 75% take-profit with a stop at a loss equal to the credit
Status: UNTESTED

### R-073 No new credit spreads while the VIX is above 30
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the VIX is above 30 THEN don't open new credit spreads on S&P 500 index options or on large index-weighted stocks | EXIT n/a (an entry filter) | INVALIDATED BY n/a
Inputs: VIX daily close → Cboe / Alpha Vantage index data
Sources: [BOOK FreemanCS loc.67–68]
Evidence: B — cites an outside backtest (projectoption, 2020) of SPY bull put spreads, 2008–2020: skipping VIX-above-30 entries raised the win rate from 74% to 77% and total profit by about 50%; method only partly shown
Conflicts: R-235 — see Conflicts
Status: UNTESTED

### R-074 Credit-spread exits: take 75% of the credit, stop at a loss equal to the credit
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a credit spread is open THEN place a good-till-cancelled order to buy it back at 25% of the credit received (capturing 75%) AND a stop that buys it back when the loss equals the credit (net premium = 2× the credit) | EXIT as stated | INVALIDATED BY n/a
Inputs: credit received, live spread price → options chain / broker positions
Sources: [BOOK FreemanCS loc.69–71]
Evidence: B — cites the same outside SPY backtest (2008–2020): taking profit at 25% of max won 86% of trades but made the least; at 75% it won 76% and made the most; stops at 2× and 3× the credit did no better than 1×. Book's own order example is inconsistent about the buy-back price (loc.71)
Conflicts: R-072 — decided by a test (see that rule)
Status: UNTESTED

### R-075 Close short options a few days before expiration
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a short option position (credit spread or iron butterfly) is within about 2 trading days of expiration, OR in its final week with the short strike near the money THEN close the whole position even if it is out of the money | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: expiry date, short strike vs price → options chain and daily price
Sources: [BOOK FreemanCS loc.74–76]; [BOOK FreemanCS loc.32–33] (gamma surges in the last week)
Evidence: C — one real case: a $1-wide put spread that looked worthless at the close was assigned after a post-close drop before the exercise cut-off; the broker's late notice left the long put unexercised and the account lost about $30,000 on a $500 maximum-loss trade
Conflicts: none yet
Status: UNTESTED

### R-076 Credit-spread timing gate: 30–45 days, no earnings or binary event inside
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF opening a credit spread or iron butterfly THEN use an expiry 30–45 days out AND require no earnings release, ex-dividend date (for call spreads), drug decision, lawsuit ruling, shareholder vote, restructuring news, Fed meeting or jobs report (for index options) before expiry; entering in the week after earnings is the book's preferred timing | EXIT n/a (an entry gate) | INVALIDATED BY a new event being scheduled inside the window, which calls for closing early
Inputs: expiry → options chain; earnings and ex-dividend dates → earnings and dividend calendars (Alpha Vantage EARNINGS_CALENDAR, FMP); macro dates → economic calendar
Sources: [BOOK FreemanCS loc.34–39]; [BOOK FreemanCS loc.59]; agrees: [BOOK FreemanCC loc.58–60]; [BOOK FreemanCC loc.76–77]; [BOOK FreemanCC loc.89] (covered calls: no earnings or major event before expiry; screen for stocks that reported earnings in the past week; don't time writes to events); agrees: [BOOK Broker p.218–219] (know stock-specific and market-wide events before choosing the expiry)
Evidence: D — asserted (supports the desk's C6 event gate)
Conflicts: none yet
Status: UNTESTED

### R-077 Credit-spread underlying screen: liquid, mid/large cap, implied volatility under 50%
School: options-income | Horizon: position (months) | Instrument: options
IF choosing an underlying for credit spreads THEN require: optionable; average volume above 500,000 shares a day; mid or large cap and price above $10 (ETFs: above 500,000 shares a day and at least $5 billion in assets); implied volatility below 50% (never above 100%); trading above its 50-day average for bull put spreads | EXCLUDE leveraged or inverse ETFs, volatility products, commodity funds that don't track spot, and heavily hyped or activist-targeted stocks | EXIT n/a (a screen) | INVALIDATED BY n/a
Inputs: volume, market cap, price → quote and company data (FMP, Alpha Vantage); implied volatility → options chain; 50-day average → daily closes; ETF assets → fund profile (Alpha Vantage ETF_PROFILE)
Sources: [BOOK FreemanCS loc.42–43]; [BOOK FreemanCS loc.57–60]
Evidence: D — asserted; the screen's output at writing is reported but not tested
Conflicts: R-146 — decided by structure (covered call on owned shares vs credit spread)
Status: UNTESTED

### R-078 Range credit spreads: short strikes outside the range while the bands contract
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock has held a clear sideways range AND its Bollinger Bands (2 standard deviations) are narrowing after a trend THEN sell a call spread with the short call just above resistance and/or a put spread with the short put just below support; messier ranges need a wider zone and further-out strikes | EXIT when the bands have squeezed unusually tight versus the last 30–60 days with shrinking bars and higher lows or lower highs, close the side the expected breakout threatens; widening bands → no new spreads | INVALIDATED BY a close outside the range
Inputs: range boundaries, Bollinger Bands(20 or 60, 2) and band width → daily OHLC (Alpha Vantage BBANDS); strikes, deltas, bid/ask, expiry → options chain snapshot
Sources: [BOOK FreemanCS loc.51–52]; [BOOK FreemanCS loc.53–55]; [BOOK FreemanCS loc.64–65]
Evidence: C — one case (a telecom stock held a range of about $1.60 for 62 trading days in mid-2020; the book places the short strikes just outside it) plus one band chart
Conflicts: none yet
Status: UNTESTED

### R-079 Short iron butterfly for a sideways stock
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock is expected to stay near its current price through expiry (sideways, low or falling implied volatility) THEN sell an at-the-money call and put at the same strike and buy equidistant wings, for a net credit (maximum profit = the credit; maximum loss = wing width − credit; breakevens = short strike ± credit) | EXIT take profit at about 15% of the maximum profit, stop at about 25% of the maximum loss; adjust only before a breakeven is reached, never after | INVALIDATED BY a change in the sideways view early in the trade (close it)
Inputs: price and range → daily OHLC; strikes, deltas, bid/ask, expiry → options chain snapshot
Sources: [BOOK FreemanCS loc.18–20]; [BOOK FreemanCS loc.72–74]
Evidence: D — hypothetical worked examples only
Conflicts: none yet
Status: UNTESTED

### R-080 Credit-spread sizing: up to 10% per trade and 10% a month, falling to 2%
School: risk/sizing | Horizon: any (every trade) | Instrument: options
IF sizing a credit spread in a small account THEN let the margin at risk ((width − credit) × 100 per spread) be at most 10% of the account per trade and 10% across all trades opened in a month; as the account grows, step down toward 2% per trade | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: spread width and credit → options chain; account equity → Cyrus
Sources: [BOOK FreemanCS loc.76–79]; [BOOK FreemanCS loc.85]
Evidence: D — asserted; the authors justify it by the stop at a loss equal to the credit and one or two trades a month
Conflicts: R-009 — decided by the desk: verdicts use the C7 tiers (at most 1.5% at risk), so this rule never governs a desk verdict; it is recorded as the book's view
Status: UNTESTED


### R-081 Pyramid only into a winning position, each add with its own stop
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares
IF a trade entered where a sharp move is expected goes in your favour by a set interval (the author used 2 points on U.S. Steel) THEN add a smaller lot (his 100 shares on a 300-share start), each add with its own stop (3 points under it), and stop adding once the move has run the planned distance (about 10 points, 800 shares in all) | EXIT each lot at its own stop; at the end take profit on a further advance or raise the stops so a profit is locked in | INVALIDATED BY the first lot's stop being hit (never add to a position showing a loss)
Inputs: entry, add levels and stops → trade plan; price → daily OHLC (add interval, stop distance and the cap are test parameters: the book gives points on a 1910s–20s stock, not percentages)
Sources: [BOOK Wyckoff p.45–46]; agrees: [BOOK Wyckoff p.47] (a speculator he knew added every point up and sold at once if it fell 2–3 points); agrees: [BOOK MoralesKacher loc.69–70] (in a 2× silver ETF, added 0.75× the initial share count every 10% higher; a claimed back-test is not shown)
Evidence: C — the author's own U.S. Steel campaigns; author claims about $20,000 net in one year from three campaigns using no more than $3,000 margin each; no losing campaigns shown
Conflicts: none yet. Consistent with R-022 (adds only to winners); the combined position's risk must still fit R-009 and the desk's C7 tiers
Status: UNTESTED

### R-082 Time stop: close a short-term trade that shows no profit within 2–3 days
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares
IF a trade (long or short) entered for an immediate move shows no profit within 2–3 trading days THEN close it, on the view that the timing judgment was wrong | EXIT also at a price stop a few points away (a time stop and a price stop together) | INVALIDATED BY n/a
Inputs: entry date and price → trade log; daily closes → daily OHLC
Sources: [BOOK Wyckoff p.130–131] (Jesse Livermore's rule as he described it to the author); agrees: [BOOK MoralesKacher loc.169] (longer window: a pocket-pivot buy that goes nowhere for 1–2 weeks in a rising market can be swapped for a fresh signal); [BOOK MoralesKacher loc.142] (weak buyable gap-up that goes nowhere for weeks: sell)
Evidence: D — a second-hand description of another trader's practice; no trades or results shown
Conflicts: R-044 — decided by strategy: this rule is for trades that expect an immediate move; R-044's PowerX swing trades run up to 20 days with ADR stops
Status: UNTESTED

### R-083 Average down only when the company has strengthened while the price fell
School: value | Horizon: position (months) | Instrument: shares
IF a stock you hold has fallen far below your cost (the author's case: from 45 to about 15) AND its latest reports show lower debt and higher earning power than when you bought THEN buy an equal amount, keep capital in reserve for a further fall two or three times what you expect, and sell the added lot on rallies to mark down the cost of the original | EXIT sell each added lot on a rally | INVALIDATED BY debt rising or earnings falling (value shrinking faster than the price)
Inputs: price → daily OHLC; total debt and earnings at purchase and now → 10-Q/10-K (how far below cost is a test parameter)
Sources: [BOOK Wyckoff p.149–152]; caution: [BOOK Wyckoff p.152–153] (a friend averaged Union Pacific down from 185 to 135 without reserve capital and was wiped out at 116); agrees: [BOOK Snow loc.34] (add only once the cause of the fall is confirmed temporary); agrees: [BOOK Wachenheim loc.103]; [BOOK Wachenheim loc.76] (add on weakness only if the purchase reasons still hold; AIG shows the risk); agrees: [BOOK Martin p.103–104] (bought at $10 vs a $30 value; at $20 it is still at a large discount: add, don't sell)
Evidence: C — one own case over 2–3 years that ended about even after interest, plus one second-hand failure
Conflicts: R-022 — decided by the fundamentals since purchase: lower debt and higher earnings → this rule; anything else → R-022
Status: UNTESTED

### R-084 Trade with no more than 5–10% of liquid capital
School: risk/sizing | Horizon: any (every trade) | Instrument: shares / options
IF the money committed to active trading would exceed 10% of your liquid capital THEN cut it back to 5–10% and keep the rest in income-producing investments; IF trading keeps drawing down the invested capital THEN stop trading and reassess | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: trading account size and liquid capital → Cyrus (never assumed)
Sources: [BOOK Wyckoff p.44]; [BOOK Wyckoff p.164–165]; agrees: [BOOK Wyckoff p.162–163] (a friend who saw his bond savings drift into his margin account stopped trading)
Evidence: C — the author's own practice ("not over five or ten per cent. of my loose capital"); no results by allocation shown
Conflicts: none yet. Sits above R-009 and R-040, which size single trades inside the trading account
Status: UNTESTED


### R-085 OTC stocks: trade only the top tiers
School: risk/sizing | Horizon: any (every trade) | Instrument: shares
IF a stock trades over the counter AND its OTC Markets tier is below the top two (the book names OTCQX and OTCQB; distressed, defunct, grey-market and caveat-emptor names fail) THEN don't trade it; beginners should keep to exchange-listed stocks | EXIT n/a (filter) | INVALIDATED BY n/a
Inputs: listing venue and OTC tier → OTC Markets Group company page or exchange data
Sources: [BOOK Gibbs loc.20]; [BOOK Gibbs loc.17–19] (the tiers as the book describes them; some names are dated); agrees: [BOOK Gibbs loc.55–57]; [BOOK Gibbs loc.78] (start on higher-caliber markets, not the Pink Sheets)
Evidence: D — asserted (the lower tiers give too little information)
Conflicts: none yet. Consistent with R-020 (no sub-penny stocks) and R-027 (liquid names only)
Status: UNTESTED

### R-086 Penny-stock screen: $0.50–$2, 100,000+ shares a day, rising, earnings growth not negative
School: growth/momentum | Horizon: swing (days–weeks) | Instrument: shares
IF a stock trades between $0.50 and $2 AND averages at least 100,000 shares a day AND is moving higher AND its earnings growth is not negative THEN it may go on the penny-stock candidate list (a list, not an entry signal) | EXIT n/a (screen) | INVALIDATED BY average volume under 100,000 a day, the trend turning down, or negative earnings growth in a new report
Inputs: price → quote; average daily volume → daily bars; 'moving higher' → computed from daily closes (the book gives no test, so the trend test is a parameter); earnings growth → latest 10-Q/10-K
Sources: [BOOK Gibbs loc.24]; agrees: [BOOK Gibbs loc.59]; [BOOK Gibbs loc.86] (only stocks trading at least 100,000 shares a day)
Evidence: D — asserted; no test or results
Conflicts: R-027 — decided by strategy: short-hold penny-stock trading (this rule, with R-021) vs liquid names only (R-027); for position and long-term calls R-027 wins
Status: UNTESTED

### R-087 Skip companies that keep issuing shares
School: value | Horizon: position (months) | Instrument: shares
IF the company's shares outstanding keep rising from report to report (employee options, repeated capital raises) THEN avoid it: each issue cuts existing holders' share and tends to pull the price down | EXIT a holding whose share count starts climbing again | INVALIDATED BY n/a
Inputs: shares outstanding over the last 4–8 quarters → 10-Q/10-K or a financial-data connector (the book gives no threshold; the growth rate that counts as constant dilution is a test parameter)
Sources: [BOOK Gibbs loc.37]; agrees: [BOOK Gibbs loc.38–39] (low-priced sectors such as mining lean on new issuance); [BOOK Gibbs loc.55–57] (dilution among the main penny-stock risks); agrees: [BOOK Zacks loc.60]; [BOOK Zacks loc.66] (companies issuing shares, by IPO or secondary offering, tend to underperform; studies cited, B); agrees: [BOOK Damodaran p.247] (avoid companies cavalier about issuing options to managers); agrees: [BOOK Fisher loc.78–79] (Point 13: count every convertible as converted and every option and warrant as exercised; reject when equity financing within a few years leaves only a small gain in per-share earnings; if cash plus prudent borrowing covers the next several years, ignore capital structure)
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-088 Penny-stock new-high breakout that holds the morning high
School: day-trading | Horizon: day | Instrument: shares
IF a penny stock breaks out to a new high, holds above the morning's high and is still up on the day THEN buy with the move (piggyback on stocks already rising); be cautious on Friday afternoons, when a short squeeze into the close can drive the move | EXIT not stated in the book (stop and target are test parameters) | INVALIDATED BY not stated in the book
Inputs: intraday high, morning high and VWAP → intraday bars (the book mentions VWAP without saying how to use it); day of week → calendar
Sources: [BOOK Gibbs loc.40]
Evidence: D — asserted; the payoff stories that follow are message-board anecdotes (loc.41–42)
Conflicts: none yet. Recorded only: the desk does not call intraday entries
Status: UNTESTED

### R-089 Dollar-cost averaging: fixed amounts on a fixed schedule
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF building a long-term position THEN buy a fixed dollar amount at preset intervals regardless of price instead of all at once | EXIT n/a (an accumulation method) | INVALIDATED BY n/a (the book's stated drawback: every purchase pays a commission)
Inputs: amount and interval → plan; price → quote; commission per trade → broker
Sources: [BOOK Gibbs loc.50]; agrees: [BOOK Osman loc.113] (regular fixed amounts into a quality index)
Evidence: D — the book calls it "proven to work" and shows no evidence
Conflicts: R-022 — decided by plan type: a fixed schedule set before the first purchase for a long-term holding → this rule; adding to a trade that shows a loss → R-022 (or R-083 when the fundamentals have improved)
Status: UNTESTED

### R-090 Penny stocks: take a 20–30% gain made within days
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares
IF a penny-stock position is up 20–30% within a few days of entry THEN sell rather than hold out for a far bigger move; a fast gain in days is also a pump-and-dump warning | EXIT this rule is the exit | INVALIDATED BY n/a
Inputs: entry price and date → trade log; price → daily closes
Sources: [BOOK Gibbs loc.58]; agrees: [BOOK Gibbs loc.85] (let go of fast risers up about 25% within days); [BOOK Gibbs loc.88] (author says not to try for more than about $0.75 a share)
Evidence: D — asserted
Conflicts: R-061 — decided by instrument and horizon: penny-stock trades → this rule; growth holdings kept for months → R-061's trailing stop, which lets winners run. Also in tension with the principle of holding until insiders sell [BOOK Wyckoff p.92–93]
Status: UNTESTED

### R-091 Penny-stock earnings breakout to a 52-week high on heavy volume
School: growth/momentum | Horizon: swing (days–weeks) | Instrument: shares
IF a penny stock with growing earnings breaks out to a 52-week high AND trades at least 250,000 shares that day THEN treat it as a buy candidate, once a check finds no paid promotion behind the move | EXIT not stated in the book (stop and target are test parameters) | INVALIDATED BY a promotion behind the high (a paid-newsletter disclosure, spam, promoter press releases)
Inputs: 52-week high and daily volume → daily bars; earnings growth → latest 10-Q (what counts as good earnings is a test parameter); promotion check → news and newsletter disclosures
Sources: [BOOK Gibbs loc.59]; agrees: [BOOK Gibbs loc.85] (earnings growth, 52-week highs and earnings breakouts, but on at least 100,000 shares: the book's two volume floors differ)
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-092 Solvency screen: liquidity ratios of at least 1
School: value | Horizon: position (months) | Instrument: shares
IF current ratio ≥ 1 AND quick ratio ≥ 1 AND operating cash-flow ratio (cash from operations ÷ current liabilities) ≥ 1 THEN the company passes the book's solvency check (a cash ratio ≥ 1 is a plus, not required); IF debt exceeds three times assets, or the current ratio is near 1/3, THEN stay away. The book's ideal pairs a pass with a cheap P/B, P/E or P/S | EXIT a holding whose latest report fails | INVALIDATED BY n/a
Inputs: current assets, inventory, cash, current liabilities, cash from operations, total debt, total assets → latest 10-Q/10-K balance sheet and cash-flow statement (ratios computed in code)
Sources: [BOOK Gibbs loc.66–68]; [BOOK Gibbs loc.65] (debt over three times assets is very vulnerable); agrees: [BOOK Gibbs loc.60–61] (the worked example screens on quick ratio ≥ 1); agrees: [BOOK Plotnick p.98] (a current ratio below 1 is a danger sign; 3.7 to 1 called healthy); [BOOK Plotnick p.153] (current assets below current liabilities ends the investigation)
Evidence: D — benchmarks asserted; the book's reference list cites a magazine article for them (loc.92), with no data shown
Conflicts: none yet
Status: UNTESTED

### R-093 Cash runway of at least 12 months
School: value | Horizon: position (months) | Instrument: shares
IF a company that burns cash has cash plus committed financing covering less than 12 more months of operations THEN avoid it | EXIT a holding whose latest report shows under 12 months | INVALIDATED BY n/a
Inputs: cash and short-term investments → 10-Q balance sheet; operating cash burn → 10-Q cash-flow statement (annualised in code); committed financing → 10-Q liquidity note or 8-K
Sources: [BOOK Gibbs loc.64]
Evidence: D — asserted, one of the book's success checks alongside a patent, partners and government interest
Conflicts: none yet
Status: UNTESTED

### R-094 No earnings: price at most half of sales per share
School: value | Horizon: position (months) | Instrument: shares
IF the company has no earnings, so P/E can't be used, THEN value it on price-to-sales and price-to-cash-flow: a P/S at or below 0.5 is the book's benchmark for a strong penny stock, and both ratios should tell the same story across several reports | EXIT n/a (valuation filter) | INVALIDATED BY P/S and P/CF disagreeing across reports
Inputs: price → quote; sales and operating cash flow (TTM) and shares outstanding → 10-Q/10-K (per-share values computed in code)
Sources: [BOOK Gibbs loc.72]
Evidence: D — asserted; the book's own worked P/S example is inverted (loc.60), so its numbers are not carried
Conflicts: none yet
Status: UNTESTED

### R-095 Penny stocks: trust chart patterns only on high turnover
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF a penny stock's daily volume is around 1% of its shares outstanding THEN treat its chart patterns as unreliable and don't act on them; IF it is around 5% THEN the book calls the pattern highly reliable | EXIT n/a (a gate on other technical rules) | INVALIDATED BY n/a
Inputs: daily volume → daily bars; shares outstanding → 10-Q or company overview (the cut-off between 1% and 5% is a test parameter)
Sources: [BOOK Gibbs loc.76]; agrees: [BOOK Gibbs loc.75] (patterns built on high volume are more reliable)
Evidence: D — asserted
Conflicts: none yet. Applies to the swing-technical rules when they are used on penny stocks
Status: UNTESTED


### R-096 Rising earnings estimates from several analysts
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF several analysts have raised their EPS estimates over the recent period (net upward revisions to the consensus), with extra weight when a revision moves above the consensus or is large relative to it THEN favour the stock; IF several analysts are cutting THEN avoid or sell it | EXIT when revisions turn net downward | INVALIDATED BY net downward revisions to the consensus
Inputs: consensus EPS history and up/down revision counts → Alpha Vantage EARNINGS_ESTIMATES, FMP analyst estimates or Webull EPS forecasts; number of analysts → same (the look-back window and how many analysts count as several are test parameters)
Sources: [BOOK Zacks loc.30–31]; [BOOK Zacks loc.32] (revisions away from the consensus and bold revisions predict more; stronger in smaller, lightly covered companies); agrees: [BOOK Zacks loc.37] (underreaction found in most international markets)
Evidence: B — studies summarised: long the top 5% / short the bottom 5% by revisions earned about 10% a year before costs, with significant results in 1970s, 1980s and 1990s studies; sample sizes and methods not shown
Conflicts: none yet
Status: UNTESTED

### R-097 Post-earnings drift: buy the biggest beats, sell on a miss
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF the latest quarterly EPS beat the consensus by enough to rank in the top 10% of surprises (surprise as a percentage of the consensus, actual and estimate on the same accounting basis) THEN buy after the announcement day and hold 3–12 months; IF a holding reports EPS below the consensus THEN sell it sooner rather than later | EXIT on a miss, or at the end of the 3–12 month hold | INVALIDATED BY a negative surprise at the next report
Inputs: actual and consensus EPS → Webull earnings calendar, Alpha Vantage EARNINGS or FMP; surprise ranking across the universe → computed in code (the hold length within 3–12 months is a test parameter)
Sources: [BOOK Zacks loc.86–87]; [BOOK Zacks loc.88] (the drift runs for years and much of it arrives around the next report; only about 13–20% in the first five days); agrees: [BOOK Zacks loc.89] (consensus-based surprises beat year-ago comparisons); [BOOK Zacks loc.93] (drift is larger in busy reporting periods and in volatile, costly-to-trade stocks); [BOOK Zacks loc.95] (sell a miss sooner rather than later); agrees: [BOOK Osman loc.89] (prices move on results against expectations); agrees: [BOOK Fridson loc.42] (about 80% of reports beat the consensus, so an ordinary beat carries little news; only large surprises do); [BOOK Fridson loc.17]; [BOOK Fridson loc.44] (a beat can still fall on revenue, gross margin or guidance)
Evidence: B — 30 years of research summarised: hedged surprise portfolios earned 4–7% a quarter before costs; one study positive in every year 1988–2005; extreme positive vs negative surprises differed by 14% over one year, 20% over two and 24% over three; sample sizes not shown
Conflicts: R-130 — decided by horizon: quarter → R-097; multi-year hold with intrinsic value above price → R-130. A sharper, study-backed form of R-042 (any beat, D)
Status: UNTESTED

### R-098 12-month price momentum, held for a quarter
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a stock ranks in the top 10% of its universe by return over the past 12 months (measured as of one week ago), or trades near its 52-week high, or well above its 120- or 240-day moving average THEN buy and hold about three months, then re-rank | EXIT at the quarterly re-rank if it has left the top group | INVALIDATED BY the economy entering a recession (over about 70 years momentum returns turned negative in recessions, with recent losers beating recent winners over the next three months)
Inputs: 12-month return, 52-week high, 120/240-day averages → daily closes; universe ranking → screener or the desk's data pipeline; recession → macro data (the book notes recessions are dated after the fact, so a real-time recession test is a parameter)
Sources: [BOOK Zacks loc.41–42]; [BOOK Zacks loc.43] (6-month/6-month variant; 52-week-high and moving-average versions do as well or better); agrees: [BOOK Zacks loc.44–45] (strongest in mid caps and lightly covered stocks, absent in the smallest and largest); [BOOK Zacks loc.47–48] (stronger with low volume and individual ownership; fails in recessions)
Evidence: B — studies summarised: long top-decile / short bottom-decile momentum earned about 12% a year (about 1% a month) before costs; a 2001 study's 6/6 version +1.39% a month; momentum crashed around 2000, giving back about a decade of gains, and recovered about five years later; found in most of 39 non-US markets; sample sizes not shown
Conflicts: R-102 — decided by horizon: a quarter → this rule; multi-year holds → R-102. Consistent with the caution that 20-day ranking failed on the largest stocks [BOOK Piard loc.36]
Status: UNTESTED

### R-099 Analyst upgrades in small caps, with a valuation check
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a small-cap stock received the strongest net recommendation upgrades in its universe over the past month AND it passes a valuation check THEN favour it for about a quarter, re-ranked quarterly to keep turnover down; weigh downgrades more than upgrades | EXIT at the quarterly re-rank | INVALIDATED BY a downgrade
Inputs: recommendation changes → analyst rating history (FMP grades, Webull analyst ratings); market cap → quote (small cap is under $2 billion in the book); valuation → the desk's B3 methods
Sources: [BOOK Zacks loc.8–10]; [BOOK Zacks loc.12–13] (excess returns concentrate in small caps; add a valuation factor or you may just be buying momentum); agrees: [BOOK Zacks loc.14–16] (downgrades are more informative; a test in the 3,000 largest stocks combining changes with valuation gave excess returns at reasonable turnover)
Evidence: B — the author's firm's database, 1990–2010, quarterly: the top decile of upgrades beat the bottom decile of downgrades in 19 of 21 years, while sorting on recommendation levels won 14 of 21 and failed after 1997; one study: best-rated stocks +9.4% a year before costs, −3.1% after; universe size and return magnitudes for the change test not shown
Conflicts: none yet
Status: UNTESTED

### R-100 G score: avoid growth stocks that fail most of eight quality tests
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a growth stock (the expensive group by price/book) scores low on the G score — one point each when its ROA, operating cash flow ÷ assets, cash flow above net income, stability of ROA (low 5-year variance), stability of sales growth (low 5-year variance), R&D ÷ assets, capex ÷ assets and advertising ÷ assets beat its industry median THEN avoid it; a score of 8 favours it | EXIT re-score each quarter | INVALIDATED BY applying it outside growth stocks
Inputs: five years of income statement, cash-flow statement and balance sheet → 10-K/10-Q; advertising expense → 10-K notes; industry medians → sector peers via a financial-data connector (computed in code; the low-score cut-off is a test parameter)
Sources: [BOOK Zacks loc.112–113]; [BOOK Zacks loc.114]
Evidence: B — studies summarised: long G=8 / short G=0 earned excess returns, mostly from the short side, positive in most years and not explained by other anomalies; weaker since it was popularised around 2005; sample sizes not shown
Conflicts: none yet
Status: UNTESTED

### R-101 Value premium: the cheapest fifth by EV/EBITDA or P/E
School: value | Horizon: long-term (years) | Instrument: shares
IF a stock sits in the cheapest 20% of its universe by enterprise value ÷ EBITDA (or P/E, or price/book) THEN favour it for a multi-year hold, especially small, volatile names with low institutional ownership, and keep buying through recessions | EXIT n/a in the book (hold for years and keep the discipline through growth-led stretches) | INVALIDATED BY n/a
Inputs: price, shares, debt, preferred, cash, EBITDA, EPS, book value → quote and 10-K/10-Q (EV/EBITDA computed in code); universe ranking → screener; institutional ownership → 13F data
Sources: [BOOK Zacks loc.82]; [BOOK Zacks loc.77] (groups sorted by P/B, P/E or cash-flow multiples give similar results); agrees: [BOOK Zacks loc.83] (works in most countries; premium largest in recessions); [BOOK Zacks loc.84–85] (larger in volatile, costly, individually owned stocks: small-cap value); agrees: [BOOK Wildermuth p.86] (asserts academic studies find value beats growth over time; no study named); agrees: [BOOK Martin p.99] (Graham's footnote: Nicholson, 100 stocks over 11 spans 1939–59: the lowest-P/E half gained over 50% more than the highest; similar in 29 chemical stocks)
Evidence: B — studies summarised: the cheapest beat the most expensive by about 10% a year over 45 years; the EV/EBITDA gap just under 1% a month equal-weighted, about 0.5% value-weighted; value beat growth in 58% of years since 1927; international value beat growth by up to 8% a year on P/B; sample sizes not shown
Conflicts: none yet. Complements R-098: in recessions momentum fails while value's premium is largest
Status: UNTESTED

### R-102 Long-term reversal: favour three-year losers over three-year winners
School: value | Horizon: long-term (years) | Instrument: shares
IF choosing stocks to hold for about three years THEN favour those in the bottom 10% by return over the past 36 months and avoid those in the top 10% | EXIT after about 36 months, then re-rank | INVALIDATED BY n/a
Inputs: 36-month returns → monthly closes; universe ranking → screener
Sources: [BOOK Zacks loc.43–44]; agrees: [BOOK Zacks loc.41] (short-term momentum and long-term reversal are the two stable patterns)
Evidence: B — a study summarised in the book: sorted on 36-month returns and held 36 months, past winners substantially underperformed past losers; no figures, sample or period shown
Conflicts: R-154 — decided by method (statistical basket vs single-name catalyst position); R-098 — decided by horizon: multi-year holds → this rule; a quarter → R-098; R-261 — see Conflicts
Status: UNTESTED

### R-103 F score: among value stocks, buy 8–9, avoid 0–1
School: value | Horizon: position (months) | Instrument: shares
IF a value stock (the cheapest group by price/book) scores 8 or 9 on the F score — one point each for positive ROA, rising ROA, positive operating cash flow, operating cash flow above net income, rising gross margin, rising asset turnover, falling leverage, rising current ratio, and no common shares issued in the past year, each change measured against the same quarter a year earlier THEN favour it; IF it scores 0 or 1 THEN avoid it | EXIT re-score each quarter (the score at which to sell is a test parameter) | INVALIDATED BY applying it outside value stocks
Inputs: income statement, balance sheet and cash-flow statement for this quarter and a year earlier → 10-Q/10-K (computed in code); share issuance → cash-flow statement or share count
Sources: [BOOK Zacks loc.110–111]; agrees: [BOOK Zacks loc.111–112] (works within value stocks, not growth); [BOOK Zacks loc.114] (positive in Brazil and Japan)
Evidence: B — studies summarised: long 8–9 / short 0–1 within value stocks earned double-digit annual returns, mostly from the long side, not explained by momentum or accruals; much weaker in the ten years after publication; sample sizes not shown
Conflicts: none yet
Status: UNTESTED

### R-104 Avoid high-accrual earnings
School: value | Horizon: position (months) | Instrument: shares
IF accruals — this year's minus last year's current net operating assets, where current net operating assets = (current assets − cash) − (current liabilities − short-term debt − income taxes payable), scaled by total assets — rank in the highest group of the universe THEN avoid the stock, watching especially for fast-rising inventory and receivables | EXIT a holding whose accruals move into the highest group | INVALIDATED BY n/a. Works best where working capital matters (construction, toys, computers, electrical equipment), poorly for drug, mining and energy companies
Inputs: two years of balance-sheet lines and total assets → 10-K/10-Q (computed in code); industry → company profile
Sources: [BOOK Zacks loc.69–70]; [BOOK Zacks loc.74–75] (better as an avoid filter than a buy screen; accruals also rise with genuine growth, so combine with other methods); agrees: [BOOK Zacks loc.72] (industry pattern); [BOOK Zacks loc.73] (data need not be fresh; the underperformance tends to arrive around the next earnings report); agrees: [BOOK Fridson loc.22–24] (channel stuffing and timing of inventory, receivable and goodwill write-downs); [BOOK Fridson loc.28–29] (Livnat and Tan: 3.4% of 220,000 quarterly reports later restated, originals possibly managed); agrees: [BOOK Plotnick p.201] (inventory near a full year's sales means overstatement or output not selling)
Evidence: B — four decades of studies summarised: long low-accrual / short high-accrual earned a double-digit annual return before costs, positive in 30 of 38 years; positive in all but one year before 1996 and about half the years after, fading around 1998–2000 as the anomaly was traded; sample sizes not shown
Conflicts: none yet
Status: UNTESTED

### R-105 Cluster insider buying: three or more insiders within three months
School: value | Horizon: position (months) | Instrument: shares
IF at least three insiders (officers, directors, 10% owners) bought shares in the open market within a three-month window AND the latest purchase was filed in the last 30 days THEN treat the stock as a buy candidate, strongest in small caps, in high-information sectors (transportation, consumer staples including drug companies, technology, financial and business services) and when officer-directors are buying | EXIT the signal expires about six months after the purchases | INVALIDATED BY n/a in the book (insider selling is mostly uninformative)
Inputs: open-market purchases with filing dates and insider roles → Form 4 filings (SEC EDGAR, Webull insider transactions, Financial Datasets insider trades); market cap → quote; sector → company profile
Sources: [BOOK Zacks loc.51]; [BOOK Zacks loc.52] (small caps and high-information sectors); [BOOK Zacks loc.56–57] (act fast: most of the reaction comes within 30 days; purchases older than five or six months say little); agrees: [BOOK Zacks loc.50]; [BOOK Zacks loc.55] (the excess return from the filing date tripled once filings were due within two days); agrees: [BOOK Osman loc.57] (cluster buying by two to four insiders, open-market purchases only); agrees: [BOOK Wachenheim loc.148] (management buying for its own account is a favourable sign); see the AIG counter-case principle
Evidence: B — studies summarised: following purchases by at least three insiders within three months averaged just under 2% a month over 27 years vs a little over 1% for the S&P 500, before costs; small caps with intensive insider buying beat the S&P 500 by almost 0.91% a month; Brochet (2010), 1997–2006: 3-day excess return from filing 0.6% before Sarbanes-Oxley vs 1.9% after; results inconsistent year to year
Conflicts: R-158 — decided by sale type (routine sales are noise; selling into weakness or a finance officer's full pre-earnings liquidation is a red flag); R-157 complementary; In tension with the principle of taking profits when insiders sell [BOOK Wyckoff p.92–93]: this book finds insider selling mostly uninformative
Status: UNTESTED

### R-106 Favour companies actually buying back their shares
School: value | Horizon: long-term (years) | Instrument: shares
IF a company has announced a substantial buyback AND is actually repurchasing (falling share count, or repurchases on the cash-flow statement) THEN favour the stock, especially small-cap and value names; IF a small company makes a self-tender offer THEN buy the stock and don't tender | EXIT n/a (the cited study measured four years) | INVALIDATED BY the program being cancelled or left unexecuted
Inputs: buyback announcement → 8-K or news; repurchases and share count → 10-Q cash-flow statement and cover page
Sources: [BOOK Zacks loc.62–63]; [BOOK Zacks loc.64] (the company must actually buy; open-ended programs can be cancelled); agrees: [BOOK Zacks loc.66] (buy companies that announced substantial buybacks; small-cap self-tenders); agrees: [BOOK Ramnarayanan p.83–85] (a buyback below fair value is accretive for holders who don't tender; insiders not tendering is a confidence signal); [BOOK Ramnarayanan p.87–89] (cash-hoarder buyback case: about 25% of market cap, promoter stake 39% → 52%); agrees: [BOOK Wachenheim loc.33]; [BOOK Wachenheim loc.87] (IBM's 1995–1997 share-count cuts; Lowe's plan to buy back about half its market value)
Evidence: B — a 1995 study of more than 1,200 open-market repurchases in the 1980s: repurchasers usually beat the market over the next four years; 3,400+ programs announced in the 1990s: large long-run abnormal returns, especially in value and small-cap stocks; a 2009 follow-up found the effect across periods and segments; small-cap self-tenders earned more than 9% in a week in some studies; return figures for the main studies not shown
Conflicts: none yet. Mirror image of R-087 (companies issuing shares lag)
Status: UNTESTED

### R-107 Avoid IPOs and stocks within three years of listing
School: value | Horizon: long-term (years) | Instrument: shares
IF a stock listed by IPO within the past 36 months (the book: three to four years) THEN don't buy it, and pass on IPO allocations offered at the offer price; exception: an IPO sold by Dutch auction | EXIT n/a | INVALIDATED BY n/a
Inputs: IPO date and offering method → company profile or the S-1/prospectus on SEC EDGAR
Sources: [BOOK Zacks loc.58–59]; [BOOK Zacks loc.66]; agrees: [BOOK Zacks loc.61–62] (small investors are offered the IPOs the big clients don't want); agrees: [BOOK Osman loc.74–75] (IPOs priced to benefit sellers; lock-up expiries; author asserts historical underperformance, no study named)
Evidence: B — one study of more than 1,500 IPOs: cumulative average return of nearly −30% over the 36 months after listing, holding after matching by size and industry; a mid-1990s study: over five years non-venture-backed IPOs lagged an equal-weight benchmark by 33%, venture-backed by 16%; results vary by period
Conflicts: R-171 — decided by sleeve (see Conflicts)
Status: UNTESTED

### R-108 Sell on an analyst downgrade after a large fall
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a stock you hold has fallen sharply AND an analyst then downgrades it THEN sell rather than hold, to counter the urge to keep a losing position | EXIT this rule is the exit | INVALIDATED BY n/a in the book
Inputs: price decline → daily closes (the size of a large fall is a test parameter); downgrade → analyst rating changes (FMP grades, Webull ratings); insider selling → Form 4 filings
Sources: [BOOK Zacks loc.13]; agrees: [BOOK Zacks loc.14–15] (downgrades are more informative than upgrades; institutions trade on them); [BOOK Zacks loc.54] (downgrades moved prices only when insiders were not already net sellers)
Evidence: B — studies summarised: after large falls analysts mostly downgrade, and downgrades carry more information than upgrades; the sell-after-a-fall use is the author's suggestion, not tested in the book
Conflicts: none yet
Status: UNTESTED

### R-109 January barometer: after a negative January, T-bills for the rest of the year
School: process | Horizon: long-term (years) | Instrument: shares
IF the S&P 500's January return is negative THEN hold Treasury bills from February through December; IF positive THEN stay invested in the index for the rest of the year | EXIT at the next January | INVALIDATED BY n/a. The author does not recommend it and suspects data mining
Inputs: S&P 500 January return → index monthly closes; T-bill yield → Treasury data
Sources: [BOOK Zacks loc.99–100]; agrees: [BOOK Zacks loc.101] (out of sample it worked only in the US and Norway among 19+ countries)
Evidence: A — US test 1940–2006: 12.8% a year vs 11.9% for buy-and-hold; 1940–2010: after a positive January the rest of the year rose 87% of the time (44 years), after a negative one 52% (27 years); 12 of 19 failures came after 1978; it failed out of sample in most other countries; the text later rounds 87% to roughly 80%
Conflicts: R-054 — decided by a desk test on the same index data: both are calendar switches and disagree in March–April and October–December after a negative January
Status: UNTESTED


### R-110 ROE-growth fair price/book for mature companies
School: value | Horizon: long-term (years) | Instrument: shares
IF a mature company's sustainable ROE exceeds the required return r AND its sustainable earnings growth g is below r THEN fair P/B = (ROE − g) ÷ (r − g) and fair value = fair P/B × latest book value; treat price well below that (the book's case: about 30% below) as a candidate buy | EXIT when price exceeds the rolled-forward fair value (see the sell rule from this book) | INVALIDATED BY ROE falling to r or below (fair P/B ≤ 1, growth then adds no value), or g turning out at or above r (the formula breaks; use the two-stage version)
Inputs: net income and opening shareholders' equity (ROE, using a geometric mean over 5–10 years) → 10-K via FMP or Financial Datasets; g → [ESTIMATED] from earnings history, capped near nominal GDP (the author won't go above 8%); r → the 10-year Treasury yield from Alpha Vantage TREASURY_YIELD (the book uses 2× the bond yield; 12% in its examples); book value and price → 10-Q and daily close
Sources: [BOOK Ramnarayanan p.33–39] (derived from the Gordon growth model); [BOOK Ramnarayanan p.46–48] (city-gas case: ROE 25%, g 8%, r 12% → P/B 4.25, about 30% above market value); [BOOK Ramnarayanan p.30–32] (sustainable growth = ROE × retention); [BOOK Ramnarayanan p.48] (value is hypersensitive to g; stay conservative); agrees: [BOOK Damodaran p.94] (P/B rises with ROE, growth and payout, falls with cost of equity); [BOOK Damodaran p.201] (book value plus present value of excess returns)
Evidence: C — worked cases on unnamed Indian companies at the time of writing; no test of returns; the author says he avoided his own past winners to limit hindsight (p.19)
Conflicts: none yet
Status: UNTESTED

### R-111 Market-implied growth check before buying
School: value | Horizon: long-term (years) | Instrument: shares
IF solving the ROE-growth P/B model (single-stage, or the two-stage version: n years of growth g then g' forever, keeping only the mature term for a closed-form answer) for the growth the current price implies gives a growth rate above what the company has delivered over comparable periods, or one that few listed companies have ever sustained THEN don't buy: the price leaves no margin of safety even if the growth arrives | EXIT n/a (an entry filter) | INVALIDATED BY your own documented growth case exceeding the implied rate (then the stock may be underpriced)
Inputs: price and book value per share → daily close and 10-Q; ROE → 10-K history; r → 10-year Treasury yield; mature growth g' and horizon n (5 or 10 years) → [ESTIMATED] (the book uses g' 8%, r 12%); historical earnings CAGR → 10-K history; base rate of companies sustaining that CAGR → screener over listed companies (computed in code)
Sources: [BOOK Ramnarayanan p.49] (invert the model: implied g and implied ROE); [BOOK Ramnarayanan p.112–115] (two-stage model; dropping the first term understates fair P/B by about 5–15%); [BOOK Ramnarayanan p.117–121] (electrical-goods case: implied 10-year growth about 19% vs about 14–18% plausible → probably priced high); [BOOK Ramnarayanan p.120] (base-rate checks); agrees: [BOOK Ramnarayanan p.132–133] (niche-products case: P/E 80 implied 18% growth; profit in 20 years matched by about ten listed companies → avoid); agrees: [BOOK Martin p.91] (Graham reprint: Bohmfalk computed the growth rate implicit in each price, 1960); [BOOK Martin p.92] (work out the growth a price implies)
Evidence: C — the author's cases at the time of writing; base-rate check proposed, not run in the book; implied-growth tables on p.122–123 are not in the text (check table p.122–123)
Conflicts: none yet
Status: UNTESTED

### R-112 Value on normalised margins and ROE, not a peak year
School: value | Horizon: long-term (years) | Instrument: shares
IF the latest operating margin or ROE sits near the top of its own 5- and 10-year range (well above the period mean) with no documented structural reason THEN value the company on the multi-year mean margin and ROE instead of the latest year; IF it sits near the bottom THEN don't sell on the latest year alone | EXIT n/a (a valuation input rule) | INVALIDATED BY a structural change that justifies the new level (documented, not assumed)
Inputs: operating margin, net income, equity for 5–10 years → 10-K via FMP or Financial Datasets (means and ranges computed in code; how near the top counts is a test parameter)
Sources: [BOOK Ramnarayanan p.69–73] (cyclical case: margins 7–15%; FY21 near the top gave P/B 5.5x vs about 2.3–3x on normalised numbers); [BOOK Ramnarayanan p.69–70] (Nifty 50 ROE 2000–2021 stayed within one standard deviation about 68% of the time, range 13.5–21.8%); agrees: [BOOK Ramnarayanan p.176–178] (same company: a 10-bagger FY13–17, then falling sales and ROE FY17–21); agrees: [BOOK Damodaran p.212]; [BOOK Damodaran p.213] (normalise cyclicals on full-cycle average or average margin × current revenue); agrees: [BOOK Wachenheim loc.85–86]; [BOOK Wachenheim loc.99] (Lowe's and Whirlpool valued on prior-normal margins; a positive trough margin signals higher normal earnings); agrees: [BOOK Martin p.75–76] (normalise current EPS for the economic, industry and company investment cycle); [BOOK Martin p.138] (smooth a cyclical rebound before estimating growth)
Evidence: C — the author's cases plus his own tabulation of index ROE; no test of a trading rule
Conflicts: R-186 — decided by where the margin sits in its own range (see Conflicts)
Status: UNTESTED

### R-113 Cash hoarder: value operations separately and discount the cash
School: value | Horizon: long-term (years) | Instrument: shares
IF cash and investments keep rising as a share of equity, ROE trends down, and the payout (dividends plus buybacks) stays low while capex needs are small THEN value the operating business on its operating ROE (ex other income, ex cash) with the P/B model and add the cash at 0–100% of face depending on management's record (the book's case uses 50%); a low fixed payout b drives long-run ROE toward g ÷ (1 − b) | EXIT n/a | INVALIDATED BY a credible payout change (large buyback or stated distribution policy) → raise the cash value; cash diverted to unrelated assets or related parties → cut it toward zero
Inputs: cash and investments, other income, equity, dividends, buybacks, capex → 10-K/10-Q via FMP or Financial Datasets; payout announcements → 8-K or news
Sources: [BOOK Ramnarayanan p.56–63] (retaining more than growth needs lowers ROE; each excess unit retained cuts value by g ÷ (r − g) units); [BOOK Ramnarayanan p.63–66] (case: operations at 4x operating book, cash at 50%); [BOOK Ramnarayanan p.66–68] (related-party loans and real-estate diversions; signals of new payout policies); agrees: [BOOK Fisher loc.118] (cash piled up beyond any present or prospective need gives holders no benefit; nor do earnings retained to enlarge an operation earning subnormal returns)
Evidence: C — the author's cases and worked arithmetic; no test
Conflicts: none yet
Status: UNTESTED

### R-114 Debt paydown at a steady EV/EBITDA
School: value | Horizon: long-term (years) | Instrument: shares
IF a company has high debt relative to its market value, depreciation well above maintenance capex, and is using most operating cash flow to repay debt THEN estimate equity value as (historical EV/EBITDA × current EBITDA) − net debt and buy when price is well below it, with a small position because the payoff behaves like a call option | EXIT when the debt/equity ratio is under control, re-evaluate as an ordinary holding | INVALIDATED BY debt rising again or EBITDA falling enough to break the historical multiple
Inputs: market cap → quote; debt, cash, EBITDA, operating cash flow, debt repayments, depreciation, capex → 10-K/10-Q via FMP or Financial Datasets; historical EV/EBITDA → computed in code from past prices and filings
Sources: [BOOK Ramnarayanan p.74–78] (equipment-lessor case: about 95% of operating cash flow to debt and interest FY18–21; implied equity value 301 → 673 at a constant 10x EV/EBITDA while the market cap swung 766 → 212 → about 1,000); [BOOK Ramnarayanan p.79–82] (named asset-sale case: EV about unchanged, equity up about 35% once proceeds prepaid debt; one-off windfalls get priced fast, gradual paydowns leave time)
Evidence: C — two cases, one named; no test; the author stresses capital loss is possible (p.78)
Conflicts: none yet
Status: UNTESTED

### R-115 Strip one-off acquisition intangibles before judging ROE
School: value | Horizon: long-term (years) | Instrument: shares
IF a large share of equity is acquisition intangibles that need no reinvestment (or strategic stakes marked up to market) AND the company grows organically THEN compute ROE on equity excluding them and value on that ROE; IF amortisation of a one-off acquisition is depressing reported profit THEN look through it to the year it ends | EXIT n/a | INVALIDATED BY the company being a serial acquirer (acquisitions are its capex) or the intangible being a patent that expires (use a DCF instead)
Inputs: goodwill and intangibles, amortisation, equity, net income → 10-K notes via FMP or Financial Datasets; acquisition history → 10-K and 8-Ks; patent expiry → 10-K
Sources: [BOOK Ramnarayanan p.93–95] (media case: reported ROE about 12% vs about 20% on tangible equity; fair value about twice the unadjusted estimate); [BOOK Ramnarayanan p.95–96] (consumer case: amortisation cut reported ROE from 50%+ to about 15%; small, lightly covered companies are most often mispriced); [BOOK Ramnarayanan p.96–97] (patent and serial-acquirer exceptions)
Evidence: D — illustrations and cases without outcomes or a test
Conflicts: none yet
Status: UNTESTED

### R-116 Dividend-yield band for steady dividend growers
School: value | Horizon: long-term (years) | Instrument: shares
IF a mature, low-capex company has a long record of rising dividends with most earnings paid out AND its dividend yield is near the top of its own 10-year range (well above the median) with fundamentals intact THEN it is a candidate buy; near the bottom of the range it is a candidate trim | EXIT when the yield falls to or below the median (trim) or the bottom of the range | INVALIDATED BY dividend growth stalling or a threat to the business: the de-rating can then be permanent and the old median no longer applies
Inputs: dividends per share and daily price → FMP or Alpha Vantage DIVIDENDS and daily closes (yield range and median computed in code); payout ratio and capex → 10-K
Sources: [BOOK Ramnarayanan p.98–102] (bond-equivalence: a 2.4% starting yield growing 5% a year with a 3% exit yield matches a 5% ten-year bond); [BOOK Ramnarayanan p.103–104] (case: yield 0.9–2.63%, median 1.85%; a move from 2.5% to 1.5% is a 66% gain on price); [BOOK Ramnarayanan p.105–106] (case of a stalled dividend: don't assume reversion)
Evidence: C — two of the author's cases; no test
Conflicts: R-062 — not a contradiction: R-062 flags an absolute yield above 5%; this rule uses the stock's own range and fails the same way when dividend growth stalls
Status: UNTESTED

### R-117 Residual-income trend: count only growth that beats the cost of equity
School: value | Horizon: long-term (years) | Instrument: shares
IF earnings are growing but residual earnings (net income − r × opening equity) are flat or falling over 5 years THEN treat the growth as value-neutral or worse: value the company on its current residual earnings with zero growth (equity + residual earnings ÷ r) rather than with the reported growth | EXIT n/a | INVALIDATED BY residual earnings growing roughly in line with earnings
Inputs: net income and opening equity for 5+ years → 10-K via FMP or Financial Datasets; r → 10-year Treasury yield (computed in code)
Sources: [BOOK Ramnarayanan p.135–138] (residual-income model; equals the P/B model under steady growth; EVA is the firm-level cousin); [BOOK Ramnarayanan p.138–140] (blue-chip case: earnings about 12% and residual earnings about 10% a year; second case: earnings +6% a year FY17–21 while residual income fell, giving about half the naive P/B value); agrees: [BOOK Damodaran p.201]; [BOOK Damodaran p.202] (excess-return model: equity converges to book when ROE equals the cost of equity)
Evidence: C — two cases; method from Penman cited, not tested in the book
Conflicts: none yet
Status: UNTESTED

### R-118 Low-leverage cyclicals: buy the bottom of the P/B band
School: value | Horizon: long-term (years) | Instrument: shares
IF a commodity or cyclical company has mature operations, little planned capex, low leverage and an attractive ROE across past cycles AND its P/B is at or below its multi-year mean minus one standard deviation THEN it is a candidate buy; near mean plus one standard deviation it is a candidate trim | EXIT at the median P/B or the upper band | INVALIDATED BY losses eating into book value, a rise in leverage, or a structural change such as a new royalty or profit-sharing regime
Inputs: monthly price and book value per share → daily closes and 10-Q (P/B mean, standard deviation and conditional means computed in code over about 7 years); debt, capex plans, ROE history → 10-K; royalty or policy changes → news
Sources: [BOOK Ramnarayanan p.141] (screen: mature, little capex, low leverage, ROE across cycles); [BOOK Ramnarayanan p.142–144] (miner case: buy-and-hold gained almost nothing; P/B mean 1.36, sd 0.3 over 85 months; 64% of the time inside ±1 sd; mean below the band 0.96, above it 1.81; 4–10% cash yield while waiting); [BOOK Ramnarayanan p.145] (book value is an unstable anchor when losses or leverage are high)
Evidence: C — one case, measured in-sample by the author; no out-of-sample test
Conflicts: none yet
Status: UNTESTED

### R-119 Sell only when price passes a refreshed fair value
School: value | Horizon: long-term (years) | Instrument: shares
IF the price reaches your original target THEN first roll the fair value forward (fair P/B × the new book value, with updated ROE and growth) and sell only if price exceeds fair value under the most optimistic assumptions you still find reasonable; a small overshoot with fundamentals on track can be held | EXIT the rule is the exit | INVALIDATED BY assumptions cut by new results (then re-run fair value downward)
Inputs: book value per share and price → 10-Q and daily close; ROE and growth assumptions → the desk's B3 valuation (updated after each quarterly report)
Sources: [BOOK Ramnarayanan p.54–58] (fair value grows with book value; don't anchor on the purchase-time target); [BOOK Ramnarayanan p.124–130] (home-products case: market cap 149 → 827 → 2,200 Cr, above every estimate; selling at perceived overvaluation would have missed most of it; the author keeps a fixed process anyway); agrees: [BOOK Martin p.62–63] (trim a concentrated winner only when its margin of safety has deteriorated enough to threaten its future return, as at 2000 tech prices); [BOOK Martin p.232–233] (Plexus: bought at $9.50, sold much of it in the $60s in 2000); [BOOK Martin p.285] (think of selling only when the price threatens the margin of safety); [BOOK Martin p.267–269] (Dell: sold at about +200% on passing worries, never rebought, missed a 100-fold rise)
Evidence: C — one hindsight case plus worked arithmetic; the author says he does not know the right holding strategy for fast growers (p.130)
Conflicts: R-061 — decided by school and horizon: valuation-based long-term holdings → this rule; growth holdings managed on price → R-061; R-186, R-187 — decided by trigger and earnings trend (see Conflicts); R-194 — decided by price vs refreshed value; R-262 — see Conflicts
Status: UNTESTED

### R-120 Walkaway-price watchlist for quality companies
School: process | Horizon: long-term (years) | Instrument: shares
IF a company passes your quality work but trades above the price at which your valuation still gives an acceptable return THEN record a walkaway price (the most you would pay), refresh it after each quarterly report, and act only if price falls below it, typically in a sharp market correction | EXIT n/a | INVALIDATED BY quality failing on new results
Inputs: walkaway price → the desk's B3 valuation; price → daily close; quarterly results → 10-Q
Sources: [BOOK Ramnarayanan p.133–134]; agrees: [BOOK Ramnarayanan p.131] (quality stocks bought at peak multiples, as in the 1960s–70s, fell more than 50% before recovering); agrees: [BOOK Martin p.223–224] (Ralph Lauren on a wish list near $100 in 2006, bought at about $56 in 2008); [BOOK Martin p.240] (Middleby on a wish list after a run to an all-time high)
Evidence: D — assertion with one case
Conflicts: none yet
Status: UNTESTED

### R-121 Kelly-scaled position weight, trimmed as price nears expected value
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF a scenario table (probability and payoff for each outcome, from your valuation) has positive expected value THEN position weight = your per-stock cap × (edge ÷ odds), where edge = expected return and odds = the probability-weighted average of the positive payoffs; use half of that for a company you have only just researched; re-run after each price move or report and trim to the new weight, which reaches zero when price equals the probability-weighted expected value | EXIT at zero weight | INVALIDATED BY negative expected value (don't enter)
Inputs: scenario values and probabilities → [ESTIMATED] from the desk's B3 valuation; price → daily close; per-stock cap → Cyrus (the book's example is 10%)
Sources: [BOOK Ramnarayanan p.161–164] (Kelly derivation and scaling by a per-stock cap); [BOOK Ramnarayanan p.166–167] (commodity case: 7.5% at P/B 1.0, trimmed to 4% at 1.25); [BOOK Ramnarayanan p.168] (half-Kelly for new names); [BOOK Ramnarayanan p.169–171] (growth case: weight falls to 3.8% by a 550 Cr market cap and zero at the 601 Cr expected value); agrees: [BOOK Ramnarayanan p.171–172] (tracking positions of 0.1–0.2%, about 5% in all)
Evidence: D — worked examples with the author's own probabilities; no test
Conflicts: R-009 — decided by measure: this sets a holding's portfolio weight for long-term shares; R-009 and the desk's C7 tiers cap the loss at the stop, and C7 governs every verdict
Status: UNTESTED

### R-122 Segment drag: a low-return division hiding a good business
School: value | Horizon: long-term (years) | Instrument: shares
IF segment reporting shows a division with a large share of capital employed (the book's case: about 40%) earning well below r, or losing money, while the core earns well above r THEN value the core and the drag separately; a sale, spin-off or turnaround of the drag is a catalyst that lifts value | EXIT n/a | INVALIDATED BY management adding more capital to the drag
Inputs: segment revenue, operating profit and assets → 10-K segment note; subsidiary vs parent results → 10-K; restructuring announcements → 8-K or news
Sources: [BOOK Ramnarayanan p.151–154] (illustration: 20% of capital in a −20% ROE line cut value by about 48%); [BOOK Ramnarayanan p.154–157] (case with an 'others' segment); [BOOK Ramnarayanan p.157] (spin-offs sold by funds for non-fundamental reasons; watch insider buying in the spun-off company)
Evidence: D — illustration and one case without an outcome
Conflicts: none yet
Status: UNTESTED


### R-123 REITs: favour the lowest short-interest fifth
School: value | Horizon: position (months) | Instrument: shares
IF a US equity REIT ranks in the lowest fifth of equity REITs by short-interest ratio (days to cover = shares sold short ÷ average daily volume) at the latest month-end THEN favour it for the next month; re-sort monthly | EXIT when it leaves the lowest fifth at a monthly re-sort | INVALIDATED BY a desk test on recent data showing no excess return over a REIT benchmark after costs
Inputs: short interest → FINRA/exchange short-interest data (via FMP or a data connector, published twice a month); average daily volume → daily price and volume history; equity REIT universe → FTSE Nareit All Equity REITs constituents (computed in code; compare with an equity REIT index, not the S&P 500)
Sources: [BOOK Trefz p.36–38]; [BOOK Trefz p.40] (lowest quintile alpha about 0.3% a month, significant at 5%, against REIT-specific factors; highest quintile about zero); agrees: [BOOK Trefz p.41] (also positive against plain Fama-French factors); [BOOK Trefz p.156–158] (holds with a credit factor added); [BOOK Trefz p.23] (earlier studies: heavily shorted REITs underperformed)
Evidence: A — monthly sorts of about 113–185 equity REITs (Nareit index members, survivorship controlled), January 1999–December 2019, equal-weighted, one-month holds; in-sample, before trading costs; a tradable long-short short-interest factor was not significant overall [BOOK Trefz p.45]
Conflicts: none yet
Status: UNTESTED


### R-124 Companion-variable mismatch: cheap multiple with strong fundamental
School: value | Horizon: long-term (years) | Instrument: shares
IF a stock trades below its peer median on a multiple AND sits above the peer median on that multiple's companion variable (low P/E with high expected EPS growth; low P/B with high ROE; low P/S with high net margin; low EV/sales with high after-tax operating margin; low EV/invested capital with high ROIC; low EV/EBITDA with low reinvestment needs) THEN flag it as a candidate for full valuation | EXIT n/a (a screen feeding the desk's B3 valuation) | INVALIDATED BY a risk measure (beta or price volatility) well above peers that explains the low multiple
Inputs: price, shares, debt, cash → quote and 10-Q; EPS, book equity, revenue, net income, operating income, tax rate, capex, depreciation, working capital → 10-K/10-Q via FMP or Financial Datasets; expected EPS growth → analyst consensus (FMP analyst) or [ESTIMATED] fundamental growth; peer set and medians → screener, computed in code
Sources: [BOOK Damodaran p.95] (each multiple derived from a stable-growth model and traced to its drivers); [BOOK Damodaran p.96] (mismatch table); agrees: [BOOK Damodaran p.246] (low multiples of corrected earnings with high corrected growth)
Evidence: C — derivation shown plus illustrative cases (beverage, apparel, bank); no test of returns
Conflicts: none yet
Status: UNTESTED

### R-125 Peer regression: actual multiple below the growth- and risk-adjusted prediction
School: value | Horizon: long-term (years) | Instrument: shares
IF regressing the multiple (P/E, P/B or EV/EBITDA) on expected growth and a risk measure across a sector's comparable companies gives a predicted multiple for the company that is meaningfully above its actual multiple THEN treat it as relatively cheap; actual well above predicted → relatively expensive | EXIT n/a (relative-valuation input) | INVALIDATED BY a low R-squared (the book's fits explain about a third to a half of the spread) or too few comparables to fit
Inputs: multiples and fundamentals for the peer set → FMP or Financial Datasets; expected growth → analyst consensus; risk → beta or standard deviation of returns from price history; regression computed in code (minimum fit quality is a test parameter)
Sources: [BOOK Damodaran p.100]; [BOOK Damodaran p.101] (beverage sector, R-squared 51%: both cases look cheap, less than the simple comparison suggested); [BOOK Damodaran p.146] (apparel: predicted P/E about 11 vs actual about 21); [BOOK Damodaran p.205] (small banks: P/B on ROE and volatility, R-squared 31%)
Evidence: C — three worked cross-sections at single dates; no outcomes reported
Conflicts: none yet
Status: UNTESTED

### R-126 Buy only when intrinsic and relative valuations both say cheap, beyond the valuation's error
School: value | Horizon: long-term (years) | Instrument: shares
IF the intrinsic value estimate exceeds price by more than the valuation's margin of error AND the relative valuation (peer median or the peer regression) also says cheap THEN the stock is a buy candidate; IF the gap is inside the margin of error, or the two methods point opposite ways, THEN don't buy | EXIT n/a (pair with the desk's sell rules) | INVALIDATED BY a revised intrinsic value that closes the gap
Inputs: intrinsic value → the desk's B3 DCF/earnings-yield work ([ESTIMATED] assumptions shown); relative value → peer multiples via FMP or Financial Datasets; price → daily close
Sources: [BOOK Damodaran p.29] (odds improve when a stock is undervalued on both bases); [BOOK Damodaran p.81] (the author passed on a gap under 10% as within the margin of error, then bought months later when his value was about a third above the price); [BOOK Damodaran p.146] (when the two disagree, long-term holders should expect short-term turbulence); agrees: [BOOK Damodaran p.250]
Evidence: C — the author's own purchase decision on one stock; no test
Conflicts: none yet (close to the desk's own B3 rule: two methods, 20% margin)
Status: UNTESTED

### R-127 Young or loss-making company: weight the value by its chance of surviving
School: value | Horizon: long-term (years) | Instrument: shares
IF a company is young or loss-making and its value rests on reaching mature margins THEN value it as a going concern (revenue path, target margin set from mature peers, reinvestment from a sales-to-capital ratio) and multiply by the probability it survives, using sector failure rates adjusted for its cash and capital access; buy only if the survival-weighted value clears the price | EXIT when margins miss the targets on the path to profitability | INVALIDATED BY a funding gap the company cannot close (needs new capital every year with markets shut)
Inputs: revenue, operating margin, cash, debt, share count → 10-K/10-Q; mature-peer margins and sales-to-capital → peer financials via FMP; sector failure rates → US Bureau of Labor Statistics business survival data; cost of capital → sector beta and Treasury yield; value [ESTIMATED] in code
Sources: [BOOK Damodaran p.109] (study: 44% of businesses founded in 1998 lasted four years, 31% seven years); [BOOK Damodaran p.118]; [BOOK Damodaran p.119]; [BOOK Damodaran p.120] (solar-panel case: going-concern value well below the price; 33% failure probability cuts it by a third); [BOOK Damodaran p.123] (relative version: forward revenue × mature-peer multiple, discounted and survival-weighted); [BOOK Damodaran p.126] (set margin targets and treat misses as a reason to sell); check table p.116
Evidence: C — one company case plus survival statistics cited from outside data (B for the base rate only)
Conflicts: R-255 — see Conflicts
Status: UNTESTED

### R-128 Distress-adjusted value from the bond rating's default history
School: value | Horizon: long-term (years) | Instrument: shares
IF a company carries heavy debt (rated below investment grade, or a low interest-coverage ratio that maps to such a rating) THEN value it as a going concern, then weight by the cumulative default probability for its rating over the horizon, with distress-sale proceeds (a haircut to book assets) in the default case; buy only if that weighted value exceeds the price | EXIT n/a | INVALIDATED BY a rating downgrade or failed refinancing (re-run with the new probability)
Inputs: credit rating → S&P/Moody's via news or filings, else synthetic rating from EBIT ÷ interest expense (10-K); cumulative default rates by rating → rating-agency default studies; book value of assets, cash, debt → 10-K; going-concern value → [ESTIMATED] DCF in code
Sources: [BOOK Damodaran p.70] (synthetic rating from interest coverage); [BOOK Damodaran p.172]; [BOOK Damodaran p.176]; [BOOK Damodaran p.177] (cumulative default rates by rating, 1971–2007; B+ about 28% over 10 years); [BOOK Damodaran p.178] (distress proceeds as a haircut to book assets); [BOOK Damodaran p.179] (casino case: adjusted value about 30% above the price); [BOOK Damodaran p.181]; [BOOK Damodaran p.182] (relative version gave a value below the price for the same company)
Evidence: B — default rates from outside rating studies; applied in one company case (C) where the two methods disagreed; check table p.175
Conflicts: none yet
Status: UNTESTED

### R-129 Growth company that keeps its margins, at a low PEG vs its sector
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF revenue keeps growing while operating margin and return on capital hold or rise year over year (growth not bought with lower margins) AND the PEG ratio (P/E ÷ expected EPS growth in %) is below the sector median THEN shortlist it | EXIT if margins or ROIC start falling to sustain growth | INVALIDATED BY risk well above the sector (PEG assumes equal risk)
Inputs: revenue, operating income, invested capital for 3–5 years → 10-K via FMP or Financial Datasets; P/E → price and EPS; expected EPS growth → analyst consensus (FMP analyst); sector medians → screener, computed in code
Sources: [BOOK Damodaran p.147] (scalable growth, sustainable margins, the right price via low PEG); [BOOK Damodaran p.99]; [BOOK Damodaran p.100] (PEG assumes equal risk and proportional growth; high growers can look cheap on PEG); agrees: [BOOK Fisher loc.182] (Part Two: a profit stream that grows at least as fast as sales)
Evidence: D — asserted value plays; examples only
Conflicts: none yet
Status: UNTESTED

### R-130 Buy a qualifying growth company after an earnings-miss sell-off
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company that passes the growth-company screen misses earnings expectations AND the price falls sharply AND the desk's intrinsic value now sits above the price THEN treat the drop as an entry | EXIT on the desk's long-term sell rules | INVALIDATED BY the miss coming from shrinking margins or returns rather than a timing slip
Inputs: earnings vs consensus → earnings calendar and FMP/Alpha Vantage EARNINGS; price reaction → daily price history; margins and ROIC → 10-Q; intrinsic value → the desk's B3 work
Sources: [BOOK Damodaran p.148] (every growth company eventually disappoints; overreacting sellers offer the right price); agrees: [BOOK Martin p.116] (negative reactions to quarterly reports can bring the price under the hurdle-rate ceiling); [BOOK Martin p.215] (Apple: −52% in a day on a preannounced shortfall in 2000; added); [BOOK Martin p.224] (Ralph Lauren's first revenue-guidance miss in 14 quarters, 2007, started the research); agrees: [BOOK Fisher loc.240] (Part Three: when a proven management's project fails, P/E falls below its usual level and the shares can be bargains); [BOOK Fisher loc.256–259] (Raychem 1976: Stilan write-off and reorganisation, stock fell to about a third of its high and more than doubled within one to two years after the January 1978 meeting)
Evidence: D — assertion
Conflicts: R-097 — decided by horizon and evidence: R-097 (sell on a miss, quarter horizon) is graded B on studies; this rule is a long-term valuation entry graded D and needs intrinsic value above the price; R-213 — decided by horizon (one-day news hold → R-213); R-223 — decided by horizon and thesis: price-managed growth holding → R-223; multi-year value-backed hold → this rule
Status: UNTESTED

### R-131 Badly managed mature company with a credible path to management change
School: value | Horizon: long-term (years) | Instrument: shares
IF a mature company's operating margin is below its sector, its ROIC is below its cost of capital or its debt ratio is far below its optimum AND nothing structural blocks a change of control (no dual-class shares or anti-takeover provisions, no controlling holder) AND a catalyst is visible (an ageing CEO, a new large holder on the board, a charter change, activist involvement) THEN it is a candidate: value = status-quo value + probability of change × (optimal value − status-quo value) | EXIT when the price reflects the change | INVALIDATED BY entrenchment (control or voting structure) or the catalyst going away
Inputs: operating margin, ROIC, debt ratio, sector medians → 10-K via FMP or Financial Datasets; cost of capital → sector beta and Treasury yield; share classes, anti-takeover provisions, holders → proxy statement (DEF 14A), 13D/13F filings; CEO age, board changes → proxy and 8-K
Sources: [BOOK Damodaran p.160]; [BOOK Damodaran p.161] (food-company case: value of control about $6 a share); [BOOK Damodaran p.162] (studies: change is likelier with poor price and earnings, small independent boards, high institutional and low insider holdings, competitive sectors); [BOOK Damodaran p.164]; [BOOK Damodaran p.165]; [BOOK Damodaran p.166] (screen and catalysts); agrees: [BOOK Fridson loc.95] (Etsy: activist stakes, strategic review, new CEO, CFO and CTO a year before its run); [BOOK Fridson loc.116–117] (outside pressure for change at NRG, Etsy, Devon; cases); agrees: [BOOK Wachenheim loc.40–41]; [BOOK Wachenheim loc.50] (Interstate: a 12% holder became chairman and replaced the CEO; holder incentive vs CEO incentive)
Evidence: C — one company case; determinants of management change from studies (not detailed)
Conflicts: R-256 — see Conflicts
Status: UNTESTED

### R-132 Turnaround: overlevered firm with sound operations and a debt fix in progress
School: value | Horizon: long-term (years) | Instrument: shares
IF a distressed company's operating business is sound (positive operating income in a healthy sector) and the distress comes from too much debt AND a debt restructuring is actively under way with good odds AND the company can still raise equity or bank funding THEN it is a candidate, sized as one of several small bets | EXIT n/a in the book | INVALIDATED BY the restructuring failing or capital access closing
Inputs: operating income, debt, interest, maturities → 10-K/10-Q; sector health → peer revenue and margins; restructuring status, new financing → 8-K filings and news
Sources: [BOOK Damodaran p.182]; [BOOK Damodaran p.183] (operating potential, debt restructuring, access to capital; spread the bets because many fail)
Evidence: D — assertion; the book's casino case is valuation only, not an outcome
Conflicts: R-198 — decided by company strength
Status: UNTESTED

### R-133 Banks and insurers: capital buffer, ROE above cost of equity, average risk
School: value | Horizon: long-term (years) | Instrument: shares
IF a bank or insurer's regulatory capital ratio is above both the requirement and its own target AND its ROE exceeds its cost of equity AND it operates in average or below-average risk lines without heavy trading or securitisation THEN it qualifies; value it on equity only (dividend discount or book value + present value of excess returns) and compare on P/B vs ROE | EXIT if the capital buffer falls below target or growth comes from riskier lines without added capital | INVALIDATED BY opaque reporting of risk exposures
Inputs: regulatory capital ratios → 10-K/10-Q and regulatory filings (FR Y-9C for US banks); ROE, payout incl. buybacks averaged over years → 10-K; cost of equity → bank sector beta and Treasury yield; P/B → price and book
Sources: [BOOK Damodaran p.189]; [BOOK Damodaran p.191]; [BOOK Damodaran p.196] (g = ROE × retention; long-term ROE is the key number); [BOOK Damodaran p.200]; [BOOK Damodaran p.201] (capital shortfall → worth less); [BOOK Damodaran p.202]; [BOOK Damodaran p.206]; [BOOK Damodaran p.207] (value plays)
Evidence: C — one large-bank case and one small-bank regression at single dates; screen asserted
Conflicts: none yet
Status: UNTESTED

### R-134 Commodity producer: compare the price-implied commodity price with a normalised one
School: value | Horizon: long-term (years) | Instrument: shares
IF the commodity price at which the producer's intrinsic value equals its share price is below a normalised commodity price (inflation-adjusted long-run average, or the futures strip) THEN it is undervalued on that view; prefer low-cost producers and hedge the commodity with futures if you don't want the commodity bet | EXIT when the implied commodity price exceeds the normalised one | INVALIDATED BY a lasting cost or reserve change at the company
Inputs: production, costs, reserves → 10-K; commodity spot and futures prices → Alpha Vantage commodities or exchange data; inflation → CPI; value as a function of commodity price → [ESTIMATED] DCF in code
Sources: [BOOK Damodaran p.216] (normalise on the average inflation-adjusted price, or use futures to keep your price view out); [BOOK Damodaran p.217]; [BOOK Damodaran p.218] (oil major: the share price implied about $42.5 oil); [BOOK Damodaran p.224] (low-cost reserves, hedge with futures)
Evidence: C — one company case at one date
Conflicts: none yet
Status: UNTESTED

### R-135 Cyclical bargain: same normalised multiple as peers, better normalised margins
School: value | Horizon: long-term (years) | Instrument: shares
IF a cyclical company trades at about the sector's multiple of normalised earnings (earnings at its full-cycle average margin times current revenue) while its normalised operating margin and ROIC are above the sector's THEN it is a candidate | EXIT when its normalised multiple moves above the sector's | INVALIDATED BY a structural fall in its margins
Inputs: revenue and operating margin over a full cycle (5–10 years) → 10-K history; sector margins and multiples → peer financials via FMP; normalisation computed in code
Sources: [BOOK Damodaran p.213] (three normalisation methods: absolute average, average margin × current revenue, sector margin); [BOOK Damodaran p.214]; [BOOK Damodaran p.215] (carmaker: normalised value well above price in early 2009); [BOOK Damodaran p.220] (P/E on current earnings bottoms at the cycle peak); [BOOK Damodaran p.225]
Evidence: C — one company case plus an oil-sector cross-section; no outcomes
Conflicts: none yet
Status: UNTESTED

### R-136 Capitalise R&D before comparing returns or multiples
School: value | Horizon: long-term (years) | Instrument: shares
IF R&D (or another expense with multi-year benefits) is a material share of revenue THEN capitalise it over its useful life (straight-line), add the unamortised balance to book capital and recompute operating income (+ R&D − amortisation), ROIC and P/E; compare peers on price ÷ (net income + R&D − amortisation) | EXIT n/a (valuation input) | INVALIDATED BY no evidence the spending pays off over several years (then leave it as an expense)
Inputs: R&D expense for the past n years (n = useful life, e.g. 10 for drugs, shorter for software), operating income, net income, equity → 10-K history via FMP or Financial Datasets; adjustments computed in code
Sources: [BOOK Damodaran p.232]; [BOOK Damodaran p.233]; [BOOK Damodaran p.234]; [BOOK Damodaran p.235] (biotech case: ROE about 23% falls to about 18%); [BOOK Damodaran p.236] (capitalise SG&A only with evidence of lasting benefit); [BOOK Damodaran p.239] (value well above price only after capitalising, given a record of R&D payoffs); [BOOK Damodaran p.241]; [BOOK Damodaran p.242] (pharma P/E three ways); agrees: [BOOK Fridson loc.31–34] (GAAP expenses R&D, understating asset-light firms; EVA capitalises R&D and advertising; Amazon case)
Evidence: C — one company valuation and one sector table at single dates
Conflicts: none yet
Status: UNTESTED

### R-137 DCF guardrails: stable growth, terminal risk and reinvestment
School: process | Horizon: long-term (years) | Instrument: shares
IF a DCF is used for a verdict THEN check: perpetual growth no higher than the risk-free rate; terminal beta near 1 and debt ratio near the industry's; terminal reinvestment rate = stable growth ÷ terminal ROIC; near-term growth no higher than reinvestment rate × ROIC (or retention × ROE) unless efficiency gains are documented; employee options subtracted at option value, not via diluted shares; reject the DCF if any check fails | EXIT n/a | INVALIDATED BY n/a
Inputs: 10-year Treasury yield → Alpha Vantage TREASURY_YIELD; beta → sector average betas; ROIC, reinvestment, payout, options outstanding and strikes → 10-K; checks computed in code
Sources: [BOOK Damodaran p.42]; [BOOK Damodaran p.73]; [BOOK Damodaran p.74] (fundamental growth = reinvestment rate × return on capital); [BOOK Damodaran p.76]; [BOOK Damodaran p.77] (value depends on the excess return accompanying growth, not the growth rate); [BOOK Damodaran p.80]; [BOOK Damodaran p.117]; [BOOK Damodaran p.142]; [BOOK Damodaran p.244]; [BOOK Damodaran p.245] (option-value approach is the right one); agrees: [BOOK Martin p.84] (Graham reprint: perpetual growth at or above the discount rate gives infinite value, so the high-growth period must be finite)
Evidence: D — method asserted with worked examples; no test
Conflicts: none yet
Status: UNTESTED


### R-138 Dividend payout above 100% or on losses: expect a cut
School: value | Horizon: long-term (years) | Instrument: shares
IF trailing dividends exceed net income (payout ratio above 100%) or net income is negative while the dividend continues THEN treat the dividend as at risk of a cut (likely funded by borrowing) and don't count the yield in a value or income case | EXIT a dividend-income holding if the payout stays above 100% for consecutive years | INVALIDATED BY free cash flow comfortably covering the dividend (e.g. heavy non-cash charges)
Inputs: dividends paid and net income (trailing 4 quarters and annual) → 10-K/10-Q via FMP or Financial Datasets; free cash flow → cash flow statement; computed in code
Sources: [BOOK Snow loc.72]; agrees: [BOOK Snow loc.74] (Fidelity data cited: on average about 9% of the highest-yield stocks cut or dropped the dividend within a year over two decades, about 40% in 2009); agrees: [BOOK Plotnick p.181] (a baker's $2.40 dividend uncovered by $2.18 of EPS, then cut to $1.80); [BOOK Plotnick p.184] (directors cut a dividend earnings no longer cover); [BOOK Plotnick p.61] (a steelmaker's dividend barely covered was a signal of trouble)
Evidence: D — asserted definition; the cited cut-rate statistic is about high yields in general, not this threshold
Conflicts: none yet
Status: UNTESTED

### R-139 Trim a single stock that has grown to about a fifth of the portfolio
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF one holding's market value reaches about 20% of the stock portfolio (in a portfolio of about 15 names) THEN sell part of it back toward its intended weight and spread the proceeds, keeping a meaningful stake while the company stays healthy and growing | EXIT n/a (a rebalancing rule) | INVALIDATED BY n/a
Inputs: position values → Cyrus's position list with daily closes; target weights → his plan (the 20% trigger and the trim size are test parameters)
Sources: [BOOK Snow loc.33]; agrees: [BOOK Snow loc.122] (a quoted manager cuts positions once they become large holdings)
Evidence: D — asserted; the book also warns that big wealth comes from letting outstanding winners run
Conflicts: R-179 — decided by level (see Conflicts); R-200 — decided by measurement base; R-263 — see Conflicts
Status: UNTESTED

### R-140 Keep trading costs at or under 2% of the order value
School: risk/sizing | Horizon: any (every trade) | Instrument: shares
IF the round-trip commission and fees on an order would exceed 2% of its value THEN enlarge the order, use a cheaper venue or skip the trade | EXIT n/a | INVALIDATED BY n/a
Inputs: commission schedule → broker; order value → planned share count × price
Sources: [BOOK Snow loc.29]; [BOOK Snow loc.26] (five $10 trades on $1,000 cost 5% on the way in and 10% round trip)
Evidence: D — arithmetic example only
Conflicts: none yet
Status: UNTESTED

### R-141 Value screen: forward P/E below the market's with broad analyst Buy support
School: value | Horizon: position (months) | Instrument: shares
IF a company's market cap is at least $1 billion AND its forward P/E is below the S&P 500's forward P/E AND at least ten analysts cover it with most rating it Buy or Strong Buy THEN put it on the value watchlist for full valuation | EXIT n/a in the book | INVALIDATED BY estimate cuts that lift the forward P/E above the market's
Inputs: market cap, forward EPS consensus, analyst ratings and count → FMP analyst/quote data; S&P 500 forward P/E → index data or FactSet-style aggregate; computed in code
Sources: [BOOK Snow loc.95] (the author's screen behind a list of 15 picks for 2022; no outcomes reported)
Evidence: D — a screen used for a published list without results
Conflicts: none yet (note: the desk's principles record that analyst recommendations lean optimistic; this screen leans on them)
Status: UNTESTED

### R-142 Read volume with price: favour light-volume pullbacks, respect heavy-volume selling
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF a liquid large-cap stock in an uptrend pulls back on volume below its recent average THEN treat the dip as a pause and keep or add long exposure per the pullback rules; IF it falls on volume well above average THEN treat it as institutional selling and avoid new longs | EXIT n/a (a filter for other entries) | INVALIDATED BY use on thin small caps, where the book says the signal is weaker
Inputs: daily volume and its moving average, daily OHLC → price history (the light/heavy thresholds are test parameters)
Sources: [BOOK Snow loc.110]; [BOOK Snow loc.111] (four volume patterns; works best on widely traded large stocks); agrees: [BOOK Broker p.279] (a trend should be carried by rising volume); agrees: [BOOK MoralesKacher loc.65] (a rise on below-average volume, 'wedging', is unhealthy); [BOOK MoralesKacher loc.161] (no pocket-pivot buys after wedging)
Evidence: D — assertion with one chart example
Conflicts: none yet
Status: UNTESTED


### R-143 Covered call only on shares held for their own case, with a gain cushion
School: options-income | Horizon: position (months) | Instrument: options
IF you already own at least 100 shares bought on their own investment case (not bought in order to write calls) AND the position shows an unrealised gain so that assignment at the chosen strike still realises a profit THEN covered calls may be written against it (one contract per 100 shares) | EXIT see the roll and buy-back rules | INVALIDATED BY the strike sitting below the cost basis (assignment would lock in a loss) or a buy-write entry with no cushion, which the authors call speculative
Inputs: share count and cost basis → Cyrus's position records; current price → daily quote (FMP/Alpha Vantage); strike → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK FreemanCC loc.40]; [BOOK FreemanCC loc.43]; [BOOK FreemanCC loc.45]; agrees: [BOOK FreemanCC loc.57] (buy-write has no cushion); [BOOK FreemanCC loc.61–62]
Evidence: D — asserted; the worked example (100 Disney shares bought at $80, now $128) is hypothetical
Conflicts: R-243 — see Conflicts
Status: UNTESTED

### R-144 Covered-call regime gate: write when the stock is ranging, not trending
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the daily Choppiness Index has crossed above about 61.8 (ranging) OR the 14-day ADX is below 25 THEN conditions suit writing a covered call, with the strike near the recent range high | SKIP when ADX is above 25 (trend; trend traders look for above 50), the Choppiness Index is below about 38.2, price is climbing inside a rising channel (assignment likely), or the stock just printed a large bearish engulfing candle on its earnings day (expected stock loss exceeds the premium) | EXIT n/a (an entry gate) | INVALIDATED BY a break out of the range; thresholds are starting points to refine per stock
Inputs: Choppiness Index(14) and ADX(14) → computed from daily OHLC (Alpha Vantage ADX); range high/low and candles → daily OHLC; earnings date → earnings calendar
Sources: [BOOK FreemanCC loc.68–70]; [BOOK FreemanCC loc.51–52] (Walmart held about $116–121 for 90 days); [BOOK FreemanCC loc.79–80] (Bank of America and Western Union rejected, Aug 2020); agrees: [BOOK FreemanCC loc.116–117] (write when the market is sideways or slightly up, not wildly bullish)
Evidence: C — chart cases only (Disney ranged 29 sessions after the Choppiness Index crossed 61.8; Walmart ADX boxes; two rejected candidates); hindsight, no tally or outcomes
Conflicts: none yet
Status: UNTESTED

### R-145 Covered-call strike distance from the volatility state
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF Bollinger Bands (20, 2) keep squeezing tighter THEN expect a breakout and write the call farther out of the money than usual; IF the bands are wide (a trend) THEN write far out of the money by default; IF the parabolic SAR dots flip sides in quick succession THEN a closer strike is acceptable; IF the SAR dots print persistently below price THEN push the strike farther out | EXIT n/a (strike placement) | INVALIDATED BY n/a
Inputs: Bollinger Bands and band width, parabolic SAR → computed from daily OHLC (Alpha Vantage BBANDS, SAR); strikes → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK FreemanCC loc.70–72]
Evidence: D — asserted with Walmart charts; the book also misdescribes the band midline as a 20-day EMA and treats 2 SD as a 95% containment (loc.70)
Conflicts: the book's own trader variant writes close to the money into a squeeze to court assignment (loc.71) — decided by goal: keep the shares → this rule; want assignment → the trader variant
Status: UNTESTED

### R-146 Covered-call underlying screen: boring, liquid, low-debt dividend payer, IV 30–70%
School: options-income | Horizon: position (months) | Instrument: options
IF choosing a stock to hold and write covered calls on THEN require: optionable; large or mega cap with steadily rising revenue and profit; debt-to-equity under 2 and falling; listed at least 5 years; average volume above 1 million shares a day; dividend yield above 2% with payout under about 40% of net income averaged over the past decade; implied volatility between 30% and 70% (never above 100%); price above its 50-day average; not cyclical (travel, real estate, materials, airlines), not a commodity fund, penny stock or media-hyped name | EXIT drop the name when it fails the screen | INVALIDATED BY n/a (a screen)
Inputs: revenue, net income, debt, equity, dividends → 10-K/10-Q via FMP or Financial Datasets (computed in code); market cap, volume, price, 50-day average, listing date → quote and company data (FMP, Alpha Vantage); implied volatility → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); sector → company profile
Sources: [BOOK FreemanCC loc.73–77]; [BOOK FreemanCC loc.81–82] (IV band and the over-100% case)
Evidence: D — asserted; the August 2020 screen's candidates are shown on charts but no results are reported
Conflicts: R-077 (credit-spread screen caps IV below 50%) — decided by structure: owned shares under a covered call → this rule; defined-risk credit spreads → R-077; the desk's C5 liquidity gate applies to both
Status: UNTESTED

### R-147 Covered-call strike by delta: lowest acceptable delta to keep the shares, about 0.40 for income
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF writing a covered call AND the goal is to keep the shares THEN sell the out-of-the-money strike with the lowest delta that still pays an acceptable premium; IF the goal is income and assignment is acceptable THEN sell the out-of-the-money strike nearest 0.40 delta; never write at or in the money | EXIT see the roll and buy-back rules | INVALIDATED BY a volatility shock that makes delta a poor guide to the chance of finishing in the money
Inputs: delta, bid/ask, strike → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); price → daily quote
Sources: [BOOK FreemanCC loc.83–86]; agrees: [BOOK FreemanCC loc.107]; [BOOK FreemanCC loc.116]
Evidence: D — one AT&T chain (26 days to expiry); the book's worked return is arithmetically inconsistent (premium given as $60 then $49; annualised figure does not match, loc.85) and it wrongly calls dividend plus premium a guaranteed return (loc.86)
Conflicts: none yet
Status: UNTESTED

### R-148 Roll a covered call when its time value falls below 1% of the stock price
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the short call's extrinsic value (its price minus intrinsic value) falls below 1% of the stock price THEN buy it back and sell the next month's call at a strike chosen afresh | EXIT the roll is the exit | INVALIDATED BY a rolled strike below the cost basis (it can lock in a stock loss if assigned)
Inputs: option bid/ask and strike → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); stock price → daily quote; cost basis → position records
Sources: [BOOK FreemanCC loc.95–96]; agrees: [BOOK FreemanCC loc.94] (buy back and re-sell the same strike further out when the stock has not moved); [BOOK FreemanCC loc.117] (choose rolled strikes so as not to lock in a stock loss); agrees: [BOOK Smith p.150] (no reason to hold a short call once its time premium is gone: roll forward or close)
Evidence: D — asserted with a hypothetical Las Vegas Sands example
Conflicts: none yet
Status: UNTESTED

### R-149 2 & 20: buy back a covered call early when 80% of the premium is captured within two weeks
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF within the first two weeks after writing a covered call it can be bought back for less than 20% of the premium received THEN buy it back and free the shares for a new write | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: premium received → trade record; current ask → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); trade date → trade record
Sources: [BOOK FreemanCC loc.96–97]
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-150 Buy back the covered call when the stock nears the strike and you want to keep the shares
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the stock rises to or near the short call's strike AND the shares are meant to be kept THEN buy the call back (accepting a small loss on it, offset by the stock's gain) rather than risk assignment | EXIT the rule is the exit | INVALIDATED BY a decision to let the shares go at the strike
Inputs: stock price → daily quote; short call strike and ask → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK FreemanCC loc.64]; agrees: [BOOK FreemanCC loc.92–93] (a $32 call bought back for $0.10 with four days left)
Evidence: D — asserted with hypothetical numbers
Conflicts: none yet
Status: UNTESTED

### R-151 Covered-call expiry: 30–45 days unless a longer expiry pays more per month
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF writing a covered call THEN choose an expiry 30–45 days out (time decay accelerates inside 30 days) AND choose a longer expiry only if its premium per month beats the monthly option's; don't count on early exercise | EXIT see the roll and buy-back rules | INVALIDATED BY an earnings date or major event before expiry (see R-076)
Inputs: expiry, premium → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); earnings date → earnings calendar; premium-per-month comparison computed in code
Sources: [BOOK FreemanCC loc.86–88]; agrees: [BOOK FreemanCC loc.23]; [BOOK FreemanCC loc.42]; agrees: [BOOK Smith p.150–151] (roll forward only if the next month's return per day beats the current write's); [BOOK Smith p.131] (decay accelerates in the last six weeks)
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-152 Code red: exit the stock (and its short call) on a fraud allegation
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a credible fraud allegation (for example a published short-seller report alleging fabricated sales) or a regulatory action over business practices hits a held stock THEN sell the shares and close any short call against them at once, at any price; don't hold on for option income | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: short-seller reports, regulatory actions → news feeds (Alpha Vantage NEWS_SENTIMENT, FMP news) and SEC 8-K filings (FMP secFilings); price → daily quote
Sources: [BOOK FreemanCC loc.97]; agrees: [BOOK Osman loc.123–124] (Wirecard 2020 and Luckin Coffee 2020 accounting frauds; case examples)
Evidence: C — one case: Luckin Coffee fell from about $32 when the Muddy Waters report came out to below $3 within about three months and was delisted; selling within a month would have kept most gains (hindsight, single winner-picked example)
Conflicts: none yet
Status: UNTESTED

### R-153 Poor man's covered call: deep in-the-money long-dated call plus a 30–45 day short call
School: options-income | Horizon: position (months) | Instrument: options
IF a stock or index ETF is in a mature, slowly rising or sideways market AND buying 100 shares is too costly THEN buy an in-the-money call 1–2 years out with delta above 0.75 and sell an out-of-the-money call 30–45 days out near 0.40 delta against it | EXIT close the short call at once if it moves into the money (assignment would force exercising the long call or a margin call); consider farther-out short strikes | INVALIDATED BY a falling stock (the long call loses more than the short premium covers)
Inputs: deltas, strikes, bid/ask, expiries → strikes, deltas, bid/ask, implied volatility, expiry → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); trend state → daily closes
Sources: [BOOK FreemanCC loc.98–101]
Evidence: D — one SPY example (July 2020) whose cost arithmetic is confused (loc.100); the vega passage wrongly says higher volatility raises intrinsic value (loc.100)
Conflicts: none yet
Status: UNTESTED


### R-154 Cheap is not enough: require a dated catalyst before buying
School: value | Horizon: position (months) | Instrument: shares
IF a stock screens cheap on the playbook's valuation rules THEN buy only when a specific, announced or scheduled corporate event can move price toward value within the holding horizon — a spin-off, split-off, Reverse Morris Trust, tender offer, deeply discounted rights offering, management change, open-market insider buying, restructuring or emergence from bankruptcy (the author prefers hard, dated events over soft ones such as product launches or sentiment); with no such event, keep it on the watchlist | EXIT when the event has played out and price has reached the refreshed value, or the event is cancelled | INVALIDATED BY the event being withdrawn or the reason the stock is cheap (falling sales, heavy debt, no strategy) worsening
Inputs: valuation → the playbook's value rules (10-K/10-Q via FMP or Financial Datasets); corporate events → SEC filings (8-K, Form 10, SC TO, S-1/S-3) via FMP secFilings or EDGAR, news (Alpha Vantage NEWS_SENTIMENT, FMP news); insider buying → Form 4 filings with transaction codes and 10b5-1 flags, insider roles and holdings after the trade (SEC EDGAR, Financial Datasets insider trades, FMP insiderTrades, Alpha Vantage INSIDER_TRANSACTIONS)
Sources: [BOOK Osman loc.2–3]; [BOOK Osman loc.13–16]; agrees: [BOOK Osman loc.63] (hard catalysts preferred because their outcomes are quantifiable); [BOOK Osman loc.113–114]; agrees: [BOOK Fridson loc.61–62] (NRG sat 70% below analysts' targets yet lagged for a year until activists and a subsidiary debt fix arrived, loc.63–65; case); [BOOK Fridson loc.115] (known virtues don't re-rate a stock without an unexpected change); agrees: [BOOK Wachenheim loc.8]; [BOOK Wachenheim loc.146] (buy undervalued strong companies ahead of a positive development not yet priced; if it never comes, expect roughly market returns)
Evidence: C — the author's cases (Sears and Toys R Us as cheap stocks that got cheaper; Pfizer and spin-off examples as successes); no tally or test
Conflicts: R-102 (buy three-year losers as a basket, no catalyst) — decided by method: a diversified statistical basket → R-102 (B); a concentrated single-name position → this rule
Status: UNTESTED

### R-155 True spin-off: value it before distribution, buy after the forced selling
School: value | Horizon: position (months) | Instrument: shares
IF a parent distributes a subsidiary's shares pro rata to its holders (a true spin-off with a Form 10; not an IPO, carve-out or split-off) AND the new company is too small for the parent's index, sits in a different sector, or has no analyst coverage THEN expect index funds and uninterested holders to sell in the first weeks; prepare a valuation beforehand (peer EV/EBITDA, P/E, P/S and a DCF) and buy once the distribution selling has passed (wait period is a test parameter) if the spin trades below peers on those multiples | EXIT on reaching fair value, or on a takeover bid | INVALIDATED BY the spin-off checks in the companion rule failing (heavy assumed debt or legacy liabilities)
Inputs: distribution ratio, record and distribution dates, assumed debt → Form 10 and 8-K (FMP secFilings, EDGAR); market cap at distribution vs index rules (S&P 500 minimum market cap and positive GAAP earnings) → quote and income statement; volume → daily price history; peer multiples → FMP/Financial Datasets statements computed in code
Sources: [BOOK Osman loc.39–40]; [BOOK Osman loc.43]; [BOOK Osman loc.66]; agrees: [BOOK Osman loc.30–31] (only pro-rata distributions are true spin-offs); [BOOK Osman loc.48] (peer multiples and DCF)
Evidence: C — case examples (Zoetis, Corteva, PayPal, HP, Mondelez, Pfizer) with rebased charts not converted; author claims studies show spin-offs beat the market by over 10%, and that his firm's 20-year data show about 35% are acquired around two years after the spin, with no study named or method shown (loc.40, 114); several examples in the book's spin-off list look factually wrong (loc.67)
Conflicts: none yet
Status: UNTESTED

### R-156 Spin-off checks: avoid spins loaded with debt or inherited liabilities
School: value | Horizon: position (months) | Instrument: shares
IF a spun-off company's debt-to-equity or net debt/EBITDA sits well above its industry's after the separation, OR the Form 10 shows it assumed the parent's legacy liabilities (environmental clean-up, litigation, pensions), OR its standalone revenue is unstable THEN avoid it or require a larger discount to peers; favour spins with stable revenue, peer-level or better margins and ROE, and management with a record in the business | EXIT when leverage or liabilities rise after the spin | INVALIDATED BY debt being paid down to industry levels
Inputs: debt, equity, EBITDA, revenue, net margin, ROE → 10-K/10-Q and Form 10 via FMP or Financial Datasets, computed in code; industry medians → peer statements; assumed liabilities → Form 10 risk factors and separation agreements (EDGAR)
Sources: [BOOK Osman loc.42–43]; [BOOK Osman loc.46–47]; agrees: [BOOK Osman loc.24]
Evidence: C — single cases (Adient inherited heavy debt from Johnson Controls; Chemours drew DuPont's environmental claims; Ferrari and PayPal as strong standalone cases); no tally
Conflicts: none yet
Status: UNTESTED

### R-157 Weigh insider buys by type: open-market only, first-time and pre-event buyers count most
School: value | Horizon: position (months) | Instrument: shares
IF a director or officer makes an open-market purchase with own cash (not an option exercise, award or 10b5-1 planned trade) that is large relative to their existing holding, especially a non-executive director or an insider with no purchase in years, AND a corporate event (spin-off, merger, restructuring) is pending THEN treat it as a strong catalyst-buyer signal and research the stock; value buyers (buying near book or perceived value) add conviction but in bear markets wait for an uptrend and renewed buying | EXIT the signal fades after about six months | INVALIDATED BY the purchase being under a 10b5-1 plan or tied to options
Inputs: transaction code, 10b5-1 flag, shares bought vs holdings after, role, prior purchase history → Form 4 filings with transaction codes and 10b5-1 flags, insider roles and holdings after the trade (SEC EDGAR, Financial Datasets insider trades, FMP insiderTrades, Alpha Vantage INSIDER_TRANSACTIONS); pending events → 8-K/Form 10 (FMP secFilings); trend → daily closes
Sources: [BOOK Osman loc.55–58]; [BOOK Osman loc.59–61] (Pfizer, 2020: first purchases by board members in years ahead of the Upjohn/Viatris separation)
Evidence: C — one case: the author's firm told clients to buy Pfizer in August 2020 after the director purchases; author claims $36.41 (25 Aug 2020) to $61.25 (16 Dec 2021), +68% vs +36% for the S&P 500, with the vaccine a large confound; the 80/20 split of value vs catalyst buyers is a quoted practitioner's claim, not data
Conflicts: R-105 (cluster buying) — complementary: R-105 counts buyers (B); this rule weighs each buy's type
Status: UNTESTED

### R-158 Insider sales that matter: selling into weakness, or a finance officer liquidating before earnings
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF an officer or director sells on the open market while the share price is falling, OR the CFO or chief accounting officer sells their entire holding (even under a 10b5-1 plan) shortly before an earnings report, especially at lower prices than their previous sales THEN treat it as a red flag: don't add, review the thesis and consider exiting before the report; other insider sales (diversification, option-related) are mostly noise | EXIT as stated | INVALIDATED BY the sale being a small fraction of holdings or an option-related disposal
Inputs: sale size, holdings after, role, 10b5-1 flag, prior sale prices → Form 4 filings with transaction codes and 10b5-1 flags, insider roles and holdings after the trade (SEC EDGAR, Financial Datasets insider trades, FMP insiderTrades, Alpha Vantage INSIDER_TRANSACTIONS); price trend → daily closes; next earnings date → earnings calendar
Sources: [BOOK Osman loc.56]; [BOOK Osman loc.59]; [BOOK Osman loc.90–93]; agrees: [BOOK Fisher loc.152–153] (Texas Instruments 1956: officers sold a small part of large holdings for diversification and estate needs; the author bought the block at 20× expected EPS, and a year later the stock had roughly doubled)
Evidence: C — one case: Varex Imaging's chief accounting officer sold all his shares in July 2019 under a 10b5-1 plan before the 6 Aug 2019 report; author reports the stock fell about 20% on the report (single winner-picked call); the author elsewhere says 10b5-1 trades carry little signal (loc.55), so this is his stated exception
Conflicts: R-105 and the principle that insider selling is mostly uninformative — decided by sale type: routine or option-related sales → noise; the two patterns here → red flag
Status: UNTESTED

### R-159 Don't hold a weakening company into earnings after a run of negative reactions
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares
IF most of a holding's last ~10 one-day earnings reactions were declines (the case: 7 of 10) AND fundamentals are weakening against peers (falling gross margin, leverage above the peer average, EBITDA margin below peers, heavy customer concentration) THEN don't carry the position into the next report; reduce or exit beforehand | EXIT re-enter only after the report on the playbook's entry rules | INVALIDATED BY guidance raised or margins recovering
Inputs: earnings dates → earnings calendar (Alpha Vantage EARNINGS_CALENDAR); one-day reactions → daily closes, computed in code; gross margin, net debt/EBITDA, EBITDA margin → 10-K/10-Q vs peers (FMP, Financial Datasets); customer concentration → 10-K disclosure
Sources: [BOOK Osman loc.91–93]; agrees: [BOOK Osman loc.89] (stocks move on results against expectations, not on 'good' earnings)
Evidence: C — one case (Varex Imaging, 2018–2019): biggest drops on a guidance cut (−26.3%) and a revenue miss (−20.3%); the stock fell about 20% on the next report; hindsight, single name
Conflicts: none yet
Status: UNTESTED


### R-160 Early range breakout (ERBO): trade the break of the first 30 minutes' high or low
School: day-trading | Horizon: day | Instrument: shares
IF a stock on the news watchlist has set its high and low for the first 30 minutes of the session (20 or 60 minutes are variants; the author says beginners should use 30 for their first six months to avoid the ~10:00 ET reversal) AND price has leaned toward one side of that range, ideally held on one side of the 10-period EMA, AND it then breaks that side by a few cents with a run of prints beyond the level on time & sales (not one stray print) AND no support/resistance — prior-day high/low/close, whole or decade dollar numbers — sits within twice the planned risk THEN enter in the break's direction with a limit order a couple of cents past the level and place the stop at once | EXIT half at the first whole number or prior-day level, the rest on a break or flattening of the 10 EMA or three bars against the trade; close everything before the session ends | INVALIDATED BY price returning inside the early range (author's typical loss 5–10 cents)
Inputs: early-range high/low, 10 EMA, prior-day high/low/close → 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY) and daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars); whole/decade numbers → price; tape confirmation → real-time time & sales (Webull get_stock_tick); the desk has no live feed to act on it
Sources: [BOOK Walsh loc.87–88]; [BOOK Walsh loc.88–89] (risk 5–10 cents; no level within 2× risk); [BOOK Walsh loc.89–91] (examples); agrees: [BOOK Walsh loc.95–97] (tape is the go/no-go); [BOOK Walsh loc.111–114]; [BOOK Walsh loc.117–118] (exercises)
Evidence: C — the author's annotated chart examples (about ten, one loser shown, loc.116); no tally, sample or period; author claims the patterns have worked for him for over ten years (loc.84). Intraday: recorded only; the desk does not call intraday entries.
Conflicts: R-011 (enter only in the daily trend's direction) — decided by setup: a news-driven stock breaking its early range → this rule, which takes either direction from the chart; an instrument without a catalyst whose daily trend sets the bias → R-011. Intraday: recorded only; the desk does not call intraday entries.
Status: UNTESTED

### R-161 Opening reversal on a gapper: trade the early-range break, target the gap fill
School: day-trading | Horizon: day | Instrument: shares
IF a stock opens with a gap from the prior close AND, within the early range, price moves back toward the prior close and then breaks the opening range on the gap-fill side (gap down that breaks above the opening high, gap up that breaks below the opening low) THEN enter that way with the prior day's close as the target; IF instead it fails to fill the gap and breaks the opening range away from the prior close THEN enter with the gap (late gap-fill sellers or buyers are trapped) | EXIT at the prior close or the first whole number or prior-day level (half), the rest on a 10 EMA break or three bars against; wait for an adjacent whole number or prior-day level to clear before entering | INVALIDATED BY price returning inside the early range
Inputs: prior close, open, early-range high/low → 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY) and daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars); gap list → pre-market movers (Webull get_gainers_losers / news feed); tape → real-time time & sales (Webull get_stock_tick); the desk has no live feed to act on it
Sources: [BOOK Walsh loc.91–92]; agrees: [BOOK Walsh loc.115–116] (exercise 5–6, one winner and one 7-cent loser); [BOOK Walsh loc.118] (gap down that breaks the early high, gap-fill target)
Evidence: C — two worked charts plus exercises, author-selected; no tally. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-162 1234 consolidation at the day's high above a whole number
School: day-trading | Horizon: day | Instrument: shares
IF four consecutive 5-minute bars hold at or near the day's high just above a whole-dollar level (or at the day's low just below one) THEN go long when price trades above the fourth bar's high (short below the fourth bar's low) | EXIT at the next whole or decade number (half), then three bars against or a 10 EMA break; close by the session end | INVALIDATED BY price falling back through the whole number the pattern sat on (stop just beyond it)
Inputs: 5-minute bars, day's high/low, 10 EMA → 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY); whole/decade numbers → price
Sources: [BOOK Walsh loc.92–93]; agrees: [BOOK Walsh loc.119–120] (exercise 10)
Evidence: C — two author-selected chart examples; no tally. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-163 Previous day's range break, mainly after lunch
School: day-trading | Horizon: day | Instrument: shares
IF price breaks above the prior day's high (or below its low) during the session, especially when that level already rejected price earlier in the day or price has been consolidating just under it THEN enter in the break's direction; an early-range breakout that also clears the prior day's high or low is given more room | EXIT at the next whole number or level (half), the rest on a 10 EMA break, three bars against, sideways action late in the day, or at the close | INVALIDATED BY price closing back inside the prior day's range (stop just beyond the level or the nearest whole number)
Inputs: prior-day high/low/close → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars); intraday bars and 10 EMA → 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY)
Sources: [BOOK Walsh loc.93–94]; agrees: [BOOK Walsh loc.118–120] (exercises 9 and 11: late-session level breaks, 10-cent stop, R:R 1:4.5)
Evidence: C — author-selected chart examples; no tally. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-164 Gap-fill bias: expect an opening gap to retrace to the prior close, more so inside yesterday's range
School: day-trading | Horizon: day | Instrument: shares
IF a stock opens away from the prior close (a gap) THEN treat the prior close as a likely intraday target for trades back toward it, with a stronger bias when the open sits inside the prior day's high–low range | EXIT at the prior close | INVALIDATED BY the gap failing to fill and price breaking the opening range away from the prior close (see the opening-reversal rule)
Inputs: open, prior close, prior high/low, whether the session's range reached the prior close → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars) (testable on daily bars alone)
Sources: [BOOK Walsh loc.82]; applied at [BOOK Walsh loc.91–92]
Evidence: D — author claims about 70% of gaps fill during the session and about 85% when the open is inside the prior day's range (loc.82); no study, sample or period given. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: R-161 continuation branch — decided by the early-range break: a break toward the prior close → this rule; a failed fill and a break away from it → R-161. Intraday: recorded only; the desk does not call intraday entries.; R-213 — decided by a desk test on the same news days; R-219 — decided by horizon and setup: intraday gaps → this rule; a daily gap ≥0.75× ATR on ≥1.5× volume out of a base → R-219
Status: UNTESTED

### R-165 Day-trading watchlist: fresh catalyst news plus price, volume and range filters
School: day-trading | Horizon: day | Instrument: shares
IF a stock has news since the last close that is likely to move it — earnings or revenue versus consensus, a guidance change, an analyst rating change, a drug trial or approval, a sudden executive departure, a merger or acquisition (both companies) — AND it trades around $20–$100 AND its average daily volume is at least 1–1.5 million shares AND its typical daily high–low range is $1 or more (very strong news can override the last two) THEN put it on the day's watchlist (10–15 names, 20 at most, ranked by a 1–5 news-importance score), plus 5–6 core stocks that range and trend well; decide direction only from the chart | EXIT drop names that trade little volume or drift without direction early in the session | INVALIDATED BY n/a (filter)
Inputs: news → Alpha Vantage NEWS_SENTIMENT, FMP news, Webull get_stock_news; earnings vs consensus → Alpha Vantage EARNINGS, FMP; rating changes → FMP analyst, Webull get_analyst_rating; price, volume, daily range → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars)
Sources: [BOOK Walsh loc.74]; [BOOK Walsh loc.76–80]; [BOOK Walsh loc.80–81] (filters, list size, scoring); [BOOK Walsh loc.84] (core list); [BOOK Walsh loc.102] (strike drifting names); quote: "the chart will tell us which direction it is moving in later" (loc.77)
Evidence: D — asserted; the news items shown are fictitious (loc.77). Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-166 Index-futures direction filter for intraday entries
School: day-trading | Horizon: day | Instrument: shares
IF considering an intraday long (short) THEN require the relevant index future (E-mini Nasdaq-100 for Nasdaq stocks, E-mini S&P 500 for NYSE) to be rising (falling) or at least flat, and prefer the advance/decline line and up/down volume trending the same way; a sudden futures surge in the trade's direction is a cue to enter, a sudden move against an open trade a cue to tighten or exit | EXIT when the futures turn hard against the position | INVALIDATED BY n/a (filter); news-driven stocks are less tied to the futures, per the author
Inputs: index futures → intraday futures bars (Webull get_futures_bars, ES and NQ); advance/decline and up/down volume → exchange breadth data (not connected); overnight Europe/Asia moves → index data
Sources: [BOOK Walsh loc.82] (overnight sentiment); [BOOK Walsh loc.98–99]; [BOOK Walsh loc.100–101] (internals); [BOOK Walsh loc.103–104]; agrees: [BOOK Walsh loc.108] (trade with as many factors aligned as possible)
Evidence: D — asserted (futures said to lead the cash index by seconds); no test. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-167 Intraday exits: half at a whole number, the rest on a 10 EMA break or three bars against
School: day-trading | Horizon: day | Instrument: shares
IF an intraday trade is in profit THEN take half off where price stalls at a whole-dollar (stronger: decade) number or a prior-day high/low/close, and run the rest until price breaks the 10-period EMA (on closes) that has been containing the move, the EMA goes flat for a few bars, or three consecutive bars close against the position; if the EMA has been crossed back and forth all day, use price action instead | EXIT all positions before the close (never hold overnight) | INVALIDATED BY n/a (exit rule)
Inputs: 10 EMA, bar sequence → 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY); whole numbers → price; prior-day levels → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars)
Sources: [BOOK Walsh loc.85–87]; agrees: [BOOK Walsh loc.90–91]; [BOOK Walsh loc.112–115] (exercises); [BOOK Walsh loc.119] (EMA ignored when price crossed it all day); [BOOK Walsh loc.120] (flat at the close)
Evidence: D — asserted; illustrated on the author's winning examples. Intraday: recorded only; the desk does not call intraday entries.
Conflicts: none yet
Status: UNTESTED

### R-168 Move the stop to breakeven once the trade is modestly in profit; never let a winner become a loser
School: risk/sizing | Horizon: day | Instrument: shares
IF a trade is in profit by a set amount (the author uses 10–15 cents on $20–$100 day-trade stocks, about the size of his initial risk) THEN move the protective stop to the entry price, then trail it to lock in profit as price advances; IF a breakout trade goes sideways without follow-through THEN exit manually before the stop | EXIT at the trailed stop | INVALIDATED BY n/a (management rule)
Inputs: entry price, initial risk, current price → the trade plan and 5-minute intraday OHLC (Webull get_stock_bars, Alpha Vantage TIME_SERIES_INTRADAY)
Sources: [BOOK Walsh loc.104–105]; agrees: [BOOK Walsh loc.52] (stop to entry after the retest holds); [BOOK Walsh loc.86]; [BOOK Walsh loc.108] (golden rule 1)
Evidence: D — asserted. The trigger size is a test parameter outside intraday trading (e.g. 1× initial risk)
Conflicts: none yet
Status: UNTESTED

### R-169 No chart stop? Set the stop from the target and a fixed reward-to-risk ratio
School: risk/sizing | Horizon: any (every trade) | Instrument: shares
IF a trade has a realistic target (pattern measure or prior support/resistance) but no obvious technical stop THEN set the maximum loss to the target distance divided by the chosen reward-to-risk ratio (the author's example: 1:4, so a 55-cent target allows 13 cents of risk) and exit there; with a chart stop, compute the ratio and skip trades below the minimum | EXIT at that stop | INVALIDATED BY n/a (planning rule)
Inputs: entry, target, ratio → the trade plan; levels → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars)
Sources: [BOOK Walsh loc.48–49]
Evidence: D — asserted with hypothetical prices
Conflicts: none yet. Related: R-010 sets the minimum ratio; R-045 sets stops from the average daily range instead
Status: UNTESTED

### R-170 Triangle breakout: wait for the break before three-quarters of the way to the apex
School: swing-technical | Horizon: day / swing (days–weeks) | Instrument: shares
IF price is contained by converging lines (ascending: flat top, rising bottom; descending: flat bottom, falling top; symmetrical: both sloped) AND it closes out of the pattern before about three-quarters of the distance to the apex THEN enter in the break's direction (ascending favours up, descending down, symmetrical the prior trend, but wait for the break); target = the triangle's height at its widest point projected from the break | EXIT at the target, or trail below the rising trend line | INVALIDATED BY price falling back inside the pattern below the trend line that formed it, or a break later than three-quarters to the apex (treated as drift, not a pattern)
Inputs: pattern lines, height and apex distance → daily OHLCV (FMP chart, Alpha Vantage TIME_SERIES_DAILY, Webull get_stock_bars) or intraday bars; computed in code (pivot definition and line tolerance are test parameters)
Sources: [BOOK Walsh loc.34–35]; agrees: [BOOK Walsh loc.51–53] (worked ascending-triangle trade, R:R 1:2.5); [BOOK Walsh loc.65] (descending-triangle short, stop above the falling line or tighter above the broken base); [BOOK Walsh loc.95]
Evidence: D — asserted; the worked trade is on a fictitious stock (loc.51) and its arithmetic is inconsistent (loc.53)
Conflicts: none yet
Status: UNTESTED


### R-171 One-year top-performer screen: volatile, disputed, sub-investment-grade, smaller than the median stock
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF at year-end an S&P 500 stock (or a likely index entrant) meets all four: (a) last year's price volatility — standard deviation of daily closes ÷ mean close — at least 1.5× the same measure for the stock ranked #250 by total return, (b) EPS-estimate dispersion (the companion dispersion rule) of 18% or more, (c) rated Baa3/BBB− or lower, or unrated (split ratings → midpoint), (d) market cap at most 80% of the prior year's #250 stock's AND at least one qualitative marker (activist or other outside pressure for change, a technology lead in a fast-moving industry, improving credit ratios, a dominant rival that may stumble) THEN shortlist it as a one-year speculative pick, sized under the lottery-sleeve rule | EXIT at the end of the 12-month window, or earlier when the qualitative marker reverses (activist exits, rival recovers, credit ratios deteriorate) | INVALIDATED BY a desk backtest showing stocks that pass the screen don't beat the index more often than chance
Inputs: volatility → daily closes (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED, Webull bars), computed in code; #250 benchmark → S&P 500 constituents and prior-year total returns to find the #250 stock → FMP index constituents plus dividend-adjusted closes, computed in code; dispersion → analysts' high and low EPS estimates for the coming fiscal year as of the prior year-end (FMP analyst estimates, Alpha Vantage EARNINGS_ESTIMATES, Webull EPS forecasts); ratings → Moody's and S&P issuer ratings and outlooks → rating-agency releases via news (FMP news, Alpha Vantage NEWS_SENTIMENT) or 10-K/8-K debt disclosures; no rating feed is connected; market cap → quote (shares outstanding × price); activists → 13D filings (FMP secFilings, EDGAR); credit ratios → 10-K via FMP or Financial Datasets
Sources: [BOOK Fridson loc.103–104] (volatility ratio: #1 stocks 1.5× to 6.3× the #250 stock); [BOOK Fridson loc.105–106] (dispersion); [BOOK Fridson loc.107–108] (ratings); [BOOK Fridson loc.109] (market cap: median 33.5%, max 80% outside two exceptions); [BOOK Fridson loc.116–120] (qualitative markers); [BOOK Fridson loc.123] (the four-test recipe and Table 5.1); agrees: [BOOK Fridson loc.121] (2008's #1 fit three of four)
Evidence: B — the author's own Bloomberg study: the 10 #1 S&P 500 stocks of 2012–2021 compared with the #250 stock, plus one 2008 check; it profiles winners only (no count of how many stocks pass the screen or how they did, so no hit rate); Figures 4.1–4.4 not converted; Table 5.1 shows NVDA 2016 at 1.465× (below the stated 1.5× floor), DVN 2021 dispersion 11.7%, and TSLA 2020 (669%) and AMD 2019 (236%) failing the market-cap test; the author owns TSLA
Conflicts: R-056 (rank by lowest debt) and R-107 (avoid recent IPOs) — decided by sleeve: a one-year speculative sleeve capped by the lottery-sleeve rule → this rule; core holdings → R-056 / R-107
Status: UNTESTED

### R-172 EPS-estimate dispersion: skip stocks the analysts agree on when seeking outsized one-year gains
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF the year-end spread of analysts' EPS estimates for the coming year, (highest − lowest) ÷ lowest, is below about 18% (the book's 'Fridson-Lee statistic'; the median stock sat near 2–3%) THEN drop the stock from any search for an outsized one-year gain, since a near-unanimous outlook is already in the price; IF it is 18% or more THEN keep it as a candidate, knowing the surprise can run either way | EXIT n/a (screen; refresh at each year-end) | INVALIDATED BY fewer than three estimates (the spread is not meaningful) or a lowest estimate at or below zero (the ratio breaks)
Inputs: high, low and count of estimates → analysts' high and low EPS estimates for the coming fiscal year as of the prior year-end (FMP analyst estimates, Alpha Vantage EARNINGS_ESTIMATES, Webull EPS forecasts); computed in code
Sources: [BOOK Fridson loc.105–106] (Table 4.1: the #1 stock's spread exceeded the #250 stock's in all 10 years; medians 39.0% vs 2.6%; 9 of 10 at 18% or more); [BOOK Fridson loc.115–116] (why: a surprise to a large share of holders moves the price); agrees: [BOOK Fridson loc.75] (TSLA began 2020 with 15 Sells vs 11 Buys); [BOOK Fridson loc.43] (hard-to-forecast companies can land near #1 or near #500)
Evidence: B — the author's Bloomberg data, n=10 winners, 2012–2021, against one middle stock per year; no test of the screen across all stocks; how negative or zero lowest estimates are handled is not stated
Conflicts: none yet
Status: UNTESTED

### R-173 Credit improvement from speculative grade: get ahead of a positive rating-outlook change
School: value | Horizon: position (months) | Instrument: shares
IF a company rated at or just above speculative grade (Baa3/BBB− or lower, or unrated) shows a multi-year improving trend in simple credit ratios — rising profit margins and return on capital, falling debt leverage (debt ÷ EBITDA), rising interest coverage (EBITDA or EBIT ÷ interest) — or makes a concrete step such as repaying term debt early THEN treat it as a candidate ahead of a rating-agency outlook change to Positive, which the cited study found moves share prices; an outlook change itself is the confirming event | EXIT when the improvement is already recognised (outlook or rating raised and priced) or the ratio trend turns | INVALIDATED BY leverage rising again or a Negative outlook
Inputs: margins, return on capital, debt, EBITDA, interest expense, debt repayments → 10-K/10-Q history via FMP or Financial Datasets, computed in code over 3+ years; ratings and outlooks → Moody's and S&P issuer ratings and outlooks → rating-agency releases via news (FMP news, Alpha Vantage NEWS_SENTIMENT) or 10-K/8-K debt disclosures; no rating feed is connected
Sources: [BOOK Fridson loc.118–119] (Holthausen and Leftwich 1986: prices respond to outlook upgrades, not rating upgrades; agencies wait for a clear trend; compute the ratios yourself); agrees: [BOOK Fridson loc.80] (TSLA: cash $1bn to $6.3bn, upgrades B3→B2, B+→BB−→BB); [BOOK Fridson loc.88] (DVN early debt repayment, Moody's outlook to Positive, then Baa3); [BOOK Fridson loc.99] (ENPH repaid all term loans); [BOOK Fridson loc.65] (NRG outlook to Positive)
Evidence: B — one cited study (1986) for the outlook effect; the #1-stock links are cases (C); check table loc.119 (Table 4.2, the ratio list, not converted); the author's own test found Positive outlooks at year-end did not separate top-five stocks [BOOK Fridson loc.114], so the edge is in the change, not the level
Conflicts: none yet
Status: UNTESTED

### R-174 S&P 500 entry candidate: a profitable, large-enough non-member nearing eligibility
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a U.S.-listed non-member has market cap at or above S&P's current minimum (2022: $14.6 billion; the book's rule of thumb: about 0.3% of the index level, read in billions) AND at least 10% of its shares in the public float AND positive GAAP earnings in the latest quarter and over the trailing four quarters THEN flag it as an inclusion candidate whose addition would bring index-fund buying; inclusion is at the index committee's discretion | EXIT after the addition takes effect, or when it fails an eligibility test | INVALIDATED BY the committee passing it over at a scheduled rebalance (TSLA's largest one-day loss followed one)
Inputs: market cap → quote; float → company profile or 10-K/10-Q cover; quarterly GAAP net income → 10-Q/10-K via FMP or Financial Datasets; index level → FMP indexes; S&P methodology thresholds → S&P Dow Jones Indices (check the current minimum before use); membership changes → news
Sources: [BOOK Fridson loc.90–91] (eligibility tests and the 0.3% rule of thumb across 13 threshold changes since 2007); [BOOK Fridson loc.81] (Investor's Business Daily: 14 additions through late October 2020 gained about twice the index over a comparable period; TSLA added December 2020)
Evidence: B — one outside data point (14 additions in 2020, method not shown) plus the TSLA case; no test of buying candidates before announcement
Conflicts: none yet
Status: UNTESTED

### R-175 Speculative 'top stock' bets: a couple of percent of the portfolio in total
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a position is a one-year speculative bet on an outsized gain (such as a pick from the top-performer screen) THEN cap all such bets together at about 1–2% of the portfolio, splitting among two or three names if needed, with the rest in a diversified core | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: portfolio value → Cyrus (never assumed); position values → Cyrus's holdings
Sources: [BOOK Fridson loc.8] (Siegel's 10–15% is far more than needed); [BOOK Fridson loc.56]; [BOOK Fridson loc.122] (the best candidates can finish near the bottom); agrees: [BOOK Fridson loc.101]
Evidence: D — assertion; no results by allocation; the desk's C7 lotto tier (≤0.5% at risk) governs every verdict
Conflicts: R-084 (5–10% of liquid capital for active trading) — complementary: R-084 caps the whole trading account; this rule caps the speculative one-year bets inside it; R-263 — see Conflicts
Status: UNTESTED


### R-176 Dow dividend ten: hold the ten highest-yielding Dow stocks, reset once a year
School: value | Horizon: long-term (years) | Instrument: shares
IF it is the annual rebalance date THEN rank the 30 Dow Jones Industrial Average members by dividend yield (trailing dividend ÷ price) and hold the top 10 in roughly equal dollar amounts; make no trades in between; at the next anniversary sell any holding no longer in the top 10, buy the new entrants and bring carried-over holdings back to equal weight (skip trades whose cost is out of proportion to the gap). Variant: the top 5 only, which the book shows with a higher return and higher volatility and says to use only alongside other strategies | EXIT annually, by re-ranking only | INVALIDATED BY a desk backtest on point-in-time Dow membership, after costs, failing to beat the Dow over the same windows
Inputs: Dow members → DJIA membership on each rebalance date, including historical members (S&P Dow Jones Indices; FMP indexes constituents and historical changes); dividends per share, trailing 12 months, and the price on the rebalance date → FMP or Alpha Vantage DIVIDENDS plus daily closes, yield computed in code; position values → Cyrus's position list with daily closes
Sources: [BOOK Wildermuth p.81–84]; [BOOK Wildermuth p.86–87] (five-stock variant and summary); [BOOK Wildermuth p.88–90]; [BOOK Wildermuth p.92]
Evidence: B — a backtest table from outside sources (Nike Securities, the Hirsch Organization, dogsofthedow.com) with defined rules and period, buying at the start of each year from 1973 to 2001: ten-stock version 16.3% a year, five-stock 18.8%, Dow 12.3%, S&P 500 12.0%. Standard deviation 15.7 for the ten-stock version, 19.3 for the five-stock version and 16.4 for the Dow. The table doesn't show its costs, taxes or dividend handling, and the start date was not tested for sensitivity. The year-by-year table is omitted, check table p.91. The book's text says the strategy lagged in 1998–99 and rose in 2000–01 while the S&P 500 fell about 20%
Conflicts: R-062 (yield above 5% as a trap warning) — decided by universe and construction: an equal-weight, annually reset basket drawn only from Dow members → this rule; a single name outside such a basket whose yield is new because its price fell → R-062; R-022 — decided by plan type: a mechanical annual reset set before the first purchase → this rule; adding to a losing discretionary trade → R-022
Status: UNTESTED

### R-177 Favour dividend payers over non-payers
School: value | Horizon: long-term (years) | Instrument: shares
IF choosing between otherwise comparable stocks for a multi-year hold THEN favour those that pay a dividend and have a record of paying one over those that pay none | EXIT n/a (a screen) | INVALIDATED BY the dividend being cut or suspended, or a payout above earnings (see R-138)
Inputs: dividend history → FMP or Alpha Vantage DIVIDENDS; payout vs earnings → 10-K/10-Q (FMP, Financial Datasets)
Sources: [BOOK Wildermuth p.95–96]; agrees: [BOOK Wildermuth p.103] (the author's own index: top yielders beat the rest by a similar margin); agrees: [BOOK Martin p.201] (Arnott and Asness, FAJ 2003: higher payout ratios preceded faster, not slower, earnings growth)
Evidence: B — cites one study (Fuller of the University of Georgia and Goldstein of Babson College): dividend payers earned about 4% a year more, risk-adjusted and pretax, than non-payers. The book gives no sample, period or method
Conflicts: R-267 — see Conflicts
Status: UNTESTED

### R-178 Own-universe dividend rotation: top yielders from a fixed list of large, growing dividend payers
School: value | Horizon: long-term (years) | Instrument: shares
IF a list of about 30 stocks was fixed in advance (large caps above $5 billion from the roughly 1,700 largest US-listed names, paying a significant dividend with a history of doing so, at least 10 years of growth, spread across industries; foreign companies listed in the US allowed) THEN each year apply the Dow dividend method to that list: hold the 5 (or 10) highest yielders in equal dollar amounts for 12 months, then re-rank and rebalance; don't drop laggards from the list to improve the backtest | EXIT annually, by re-ranking only | INVALIDATED BY the top 5 failing to beat the equal-weight list itself over the same windows (the author's own test of whether the screen adds anything)
Inputs: market cap → quote and shares outstanding; dividend history → FMP or Alpha Vantage DIVIDENDS; 10-year revenue and EPS growth → 10-K history via FMP or Financial Datasets, computed in code; sector → FMP company profile. The author's further 'future growth potential' test is judgement and is left out
Sources: [BOOK Wildermuth p.96–100]; [BOOK Wildermuth p.102–104]
Evidence: C — the author's own roughly 10-year test on an index he built with hindsight (he notes the selection bias himself). Author claims about 26% a year for the top 10 vs 25% for his index, and just under 30% for the top 5. The top-5 version was about 35% more volatile than his index. No list, dates or costs are shown, and the method is the author's trademarked product
Conflicts: none yet. Note: as tested in the book it fails R-059's acceptance gate (under 10 years, hand-picked universe)
Status: UNTESTED

### R-179 Value Line Timeliness rank 1, held while the rank and industry rank hold
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a stock is ranked 1 (Highest) for Timeliness by the Value Line Investment Survey THEN it is a buy candidate. The author narrows the list to about 10 stocks: industry rank in the top 10–15 of about 90 industries, Safety rank 3 or better, the highest 3–5 year appreciation potential, spread across industries | EXIT active version: hold rank 1 even if it becomes overweight, unless its industry rank falls into the bottom third. At rank 2, hold while the industry is in the top 10–15 and trim or sell once the industry falls out of the top third. At rank 3, sell unless the industry is in the top 5%. Annual version: once a year sell everything not ranked 1, refill with rank-1 names and equal-weight | INVALIDATED BY the rank-1 basket failing to beat the market over the review window
Inputs: Timeliness, Safety, industry rank, 3–5 year appreciation potential → Value Line Investment Survey (paid subscription; not a connected desk source, so this rule cannot fire until Cyrus supplies the ranks); prices → daily closes
Sources: [BOOK Wildermuth p.108–110]; [BOOK Wildermuth p.112–119]
Evidence: B — Value Line's own published record, reported in the book: buying rank-1 stocks at the start of each year and selling at year end returned about 14.5% a year from 1965 to 2001, vs 6.8% for the Dow excluding dividends. The weekly-replacement version returned 18.0%. The author notes the gains were concentrated in the early years. In down years the annual version beat the Dow in 6 of 11, and the weekly version in 7 of 11. The book shows no costs or method. The author's narrowing filters and sell ladder are his own and untested (C); he says he hasn't measured the commentaries' value
Conflicts: R-139 (trim a holding near 20% of the portfolio) — decided by where the weight cap applies: the book holds a rank-1 name even when it becomes overweight within a sleeve of about 10 stocks, but a position that reaches about a fifth of the whole stock portfolio falls under R-139 and the desk's risk tiers
Status: UNTESTED

### R-180 Rebalance an allocation when a sleeve drifts more than 10% from its target, or once a year
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF a portfolio has a written target allocation (stocks vs safe money, and sleeves within each) AND a sleeve's weight has moved more than 10% of its own target (a 20% target now at 23% is a 15% drift) THEN sell the overweight sleeve and buy the underweight one back to target. A lighter version rebalances once a year. Prefer waiting when a trade would turn a nearly long-term gain into a short-term one | EXIT n/a (a maintenance rule) | INVALIDATED BY n/a
Inputs: sleeve values → Cyrus's position list with daily closes; targets → his written plan; drift computed in code (the 10% band is a test parameter)
Sources: [BOOK Wildermuth p.75–77]; [BOOK Wildermuth p.79] (constant allocation assumed under every strategy in the book); agrees: [BOOK Wildermuth p.68–69] (trim the fund that ran, add to the laggard unless something is fundamentally wrong); [BOOK Wildermuth p.165]
Evidence: D — asserted. The author says the approach is backed by volumes of research but cites none, and the 10% band is his own figure
Conflicts: R-022 — decided by plan type: rebalancing to targets written before the first purchase → this rule; adding to a losing discretionary trade → R-022. Complements R-139 (single-stock trim)
Status: UNTESTED


### R-181 Survival floor: net current assets less long-term debt per share
School: value | Horizon: position (months) | Instrument: shares
IF a candidate value stock's (current assets − current liabilities − long-term debt) ÷ common shares — after deducting goodwill and other intangibles carried above nominal value and marking hard-to-sell inventory at about 50% of book when inventory dominates current assets — is only pennies against the share price, OR current assets do not cover current liabilities THEN reject it before any further work; IF that figure is a large share of the price (the book's passing cases run from about two-thirds of price to above it) THEN it passes the first financial-strength check | EXIT a holding whose figure collapses toward zero on new reports | INVALIDATED BY a company whose current assets are mostly receivables or inventory of doubtful value (re-run with the haircuts)
Inputs: current assets, current liabilities, long-term debt, goodwill and intangibles, inventory, shares outstanding → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); price → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED); the passing ratio of the figure to price is a test parameter (the book sets none)
Sources: [BOOK Plotnick p.96–98] (step 5 of the first look: what the company could raise quickly if creditors called); [BOOK Plotnick p.97] (a case: about 16 cents a share of net current assets against a price of roughly 2–8 → stay away); [BOOK Plotnick p.99] (a case: $14.43 a share against a price of about 23 → strong); [BOOK Plotnick p.119] (deduct goodwill; haircut specialised inventory to about half); agrees: [BOOK Plotnick p.63] (protection against bankruptcy lies in book value, working capital and net current assets less long-term debt; an electronics name without it went to near zero)
Evidence: C — single-company cases chosen by the authors, 1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact; no tally of passes vs fails
Conflicts: R-092 (solvency screen) — complementary: R-092 tests liquidity ratios; this rule sizes the cushion per share against the price
Status: UNTESTED

### R-182 Book-value cushion scaled to the earnings record
School: value | Horizon: position (months) | Instrument: shares
IF the candidate has lost money for some time and now shows signs of recovery THEN require net tangible book value per share at or above the price; IF its record is erratic THEN require book close to the price; IF it has improved steadily in all operating lines THEN book below half the price is acceptable; where losses have been severe, cut fixed assets and inventory by up to 50% to a liquidation estimate before comparing | EXIT re-check when losses resume and book shrinks | INVALIDATED BY large write-downs that show book was overstated (re-run on the written-down figure)
Inputs: total equity, goodwill, intangibles, preferred, fixed assets, inventory, shares → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); profit history (losses, erratic, steady) → 4 years of annual net income from the 10-K; price → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED)
Sources: [BOOK Plotnick p.112–113]; agrees: [BOOK Plotnick p.110–111] (book is a safety line, not a price driver; trading below book is not by itself a buy); [BOOK Plotnick p.203–204] (conservative investors cut asset values by up to half when liquidation is a risk); [BOOK Plotnick p.199] (be absolutely strict with a stock emerging from losses, not with well-rated stocks)
Evidence: D — the authors state the sliding scale and refuse a fixed limit; no test
Conflicts: in tension with the principle that a P/B below 1 can mean overstated book [BOOK Anderson loc.29] — decided by the earnings record: a recovering loss-maker needs the cushion here; a stock with no earnings turn is not a candidate under this rule at all
Status: UNTESTED

### R-183 Loss-type turnaround: cushion, falling cost ratios, then the first profitable quarter
School: value | Horizon: position (months) | Instrument: shares
IF years of losses have pushed the price below net tangible book and down near net current assets less long-term debt per share AND cost of goods sold and selling/administrative expense as a share of sales are falling AND losses have narrowed AND the latest quarter shows a profit against a loss in the same quarter a year earlier on higher sales THEN it is a buy candidate on that report rather than waiting for the full year; IF losses are only narrowing, put it on a watch list and re-check at the next quarterly report | EXIT when quarterly EPS falls sharply against the same quarter a year earlier (the case: −42%) or R-186 fires | INVALIDATED BY current assets falling below current liabilities, or no improvement in cost and margin ratios
Inputs: quarterly and annual sales, cost of goods sold, SG&A, pretax income, EPS → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); book value, current assets and liabilities, long-term debt, shares → 10-Q balance sheet; report dates → earnings calendar (Alpha Vantage EARNINGS_CALENDAR); price → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED)
Sources: [BOOK Plotnick p.159] (three elements of the loss-type case); [BOOK Plotnick p.150–152] (cost ratios down on lower sales; loss margin from 7.5% to 2.8%; first-quarter profit 4.2%); [BOOK Plotnick p.151] (watch list until promise becomes reality); [BOOK Plotnick p.158–159] (sell on a 42% drop in first-quarter EPS); agrees: [BOOK Plotnick p.62] (a gauge maker moving from deficit to profit, with net current assets near the price, rose); [BOOK Plotnick p.92] (falling losses qualify as a candidate); contrast: [BOOK Plotnick p.63] (a loss-maker with no asset cushion went bankrupt)
Evidence: C — winner-picked cases (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact); author claims about $900 became $5,600 in the 1958 automaker case [BOOK Plotnick p.159]; the same case's earnings were largely untaxed because of loss carry-forwards (p.158); check table p.157
Conflicts: R-154 (require a dated catalyst) — complementary: here the reported earnings turn is the event; R-127 — complementary: R-127 values a loss-maker's survival, this rule requires the turn to have started
Status: UNTESTED

### R-184 Own-history P/E band: buy at the low end, project at a constant multiple
School: value | Horizon: position (months) | Instrument: shares
IF the stock's P/E on current-run-rate earnings sits at or below the low end of its own yearly mean P/Es (each year's (high + low) ÷ 2 ÷ that year's EPS) over at least four years AND price is near its four-year low AND earnings are improving THEN it is a candidate; set the upside as projected EPS × the historic low-to-mean multiple (assume no multiple expansion; expansion is a bonus) and treat the four-year high as the outer reference, not a target | EXIT when the P/E reaches the top of its historic band while margins stop improving | INVALIDATED BY a change in the business that makes the old earnings and multiples irrelevant (a lost main product, a new tax or regulatory burden)
Inputs: annual high and low prices and EPS for 4+ years → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED) and 10-K EPS via FMP/Financial Datasets (adjusted for splits); current-run-rate EPS → trailing four quarters or R-189 [ESTIMATED]; all computed in code
Sources: [BOOK Plotnick p.116–117] (price range and mean P/E per year show whether the stock is depressed or historically high); [BOOK Plotnick p.66] (buy at a low multiple, expect the same multiple on higher earnings; don't count on expansion); [BOOK Plotnick p.94] (buy at the bottom of a 12–15x historic band, not the top); [BOOK Plotnick p.139] (a case: current P/E 10 vs 9–16 over four years, price near the four-year low); [BOOK Plotnick p.167] (a case: mean P/Es 5–11, price near a four-year low); agrees: [BOOK Plotnick p.56] (a sub-7 P/E on earnings that would not continue was not a buy)
Evidence: C — the authors' winner cases (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact); no count of stocks that met the test and fell; check table p.142
Conflicts: R-118 (P/B band for cyclicals) — complementary: same band logic on earnings instead of book
Status: UNTESTED

### R-185 Operating-trend gate: sales direction, cost ratios and margins over two and four years
School: value | Horizon: position (months) | Instrument: shares
IF over the last two fiscal years plus the current period sales are off sharply, OR sales are flat or down while gross and pretax margins narrow and cost ratios (cost of goods sold ÷ sales, SG&A ÷ sales) rise THEN drop the candidate; IF sales are up sharply and margins narrowed only slightly (start-up costs, a losing division) THEN keep going; THEN over four years reject a company whose sales or cost of goods sold ratio swing erratically from year to year; the ideal is rising sales with falling cost ratios and widening margins | EXIT n/a (an entry gate; see R-186 for holdings) | INVALIDATED BY a nonrecurring item explaining the change (document it)
Inputs: annual and year-to-date sales, cost of goods sold, gross profit, SG&A, pretax income for 4 years plus the current period → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); volatility of the ratios computed in code (what counts as erratic is a test parameter; the book mentions 15–20% swings)
Sources: [BOOK Plotnick p.106] (sales off sharply → stop; flat → finish the second look); [BOOK Plotnick p.111–112] (declining sales and narrowing margins end the investigation; sharp sales growth gets the benefit of the doubt); [BOOK Plotnick p.107–109] (cost ratios as a share of sales; a stationery case: cost of goods 87.6% → 85.7%, pretax margin 8.3% → 9.9%); [BOOK Plotnick p.124] (erratic sales are very dangerous; four years needed); [BOOK Plotnick p.140] (erratic cost of goods ratios mean risk); agrees: [BOOK Plotnick p.164] (improved margins usually come before improved earnings)
Evidence: C — worked company cases (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact); thresholds asserted
Conflicts: R-129 — complementary: R-129 asks growth companies to hold margins; this gate applies to any candidate
Status: UNTESTED

### R-186 Sell when operating indicators turn down, before earnings do
School: value | Horizon: position (months) | Instrument: shares
IF a holding's latest report shows pretax margin below the same period a year earlier (even with sales rising), OR sales flattening or declining, OR quarterly EPS down against the same quarter a year earlier, OR full-year EPS flat after a run of gains, AND the cause is not a documented nonrecurring item THEN sell; IF earnings have declined for several years in a row, sell even when the balance sheet is strong and the dividend long-standing | EXIT the rule is the exit | INVALIDATED BY the decline being a one-off (plant start-up, strike, disposal of a losing line) shown in the filing
Inputs: quarterly and annual sales, gross profit, SG&A, pretax income, EPS, same quarter prior year → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); nonrecurring items → 10-Q/10-K notes; report dates → earnings calendar
Sources: [BOOK Plotnick p.173–174] (review sales, cost of goods, gross profit, cost of sales and net profit at each report; downtrends rarely reverse within a quarter); [BOOK Plotnick p.48] (a decline in earnings, sales or margins in a quarterly report is the sell signal); [BOOK Plotnick p.182–183] (a grocery-chain case: sales up, margin down → sell; full-year EPS then fell); [BOOK Plotnick p.144] (a publisher case: margin from 3.6% to 2.1% plus a record P/E → sell); [BOOK Plotnick p.168] (flat annual EPS triggered the sale of a mail-order holding); [BOOK Plotnick p.180] (a baker with no debt and a current ratio near 4 slid from $50 to $22 as EPS fell six years running); agrees: [BOOK Plotnick p.181–182] (revenues and costs crack before earnings); [BOOK Plotnick p.183] (investigate nonrecurring causes before selling)
Evidence: C — hindsight cases picked by the authors (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact); no count of false signals
Conflicts: R-112 — decided by where the margin sits in its own multi-year range: already near the bottom after a long decline (cyclical trough) → R-112 (don't sell on the latest year); falling from a normal or recovering level → this rule; R-119 — decided by trigger: price reaching a target while fundamentals are on track → R-119; operating indicators turning down → this rule
Status: UNTESTED

### R-187 Sell a high-multiple holding on stalled earnings or any operating crack
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a holding's P/E is well above both its own history and the market's while earnings are flat or growing slowly (the case: about 30x vs the index's about 23x), OR its price needs 5–10 years of compounded industry-rate growth to look reasonable at a normal multiple, OR it trades in line with similar companies so further gains need extraordinary enthusiasm THEN take profits; IF a high-P/E holding shows any weakness in sales, margins or the growth rate THEN sell at once | EXIT the rule is the exit | INVALIDATED BY earnings growth that keeps pace with the multiple (re-check at each report)
Inputs: P/E, its 4+ year history and the index P/E → price history and 10-K EPS (FMP, Financial Datasets), index P/E → FMP indexes or a computed S&P 500 aggregate; industry growth rate → peer revenue/EPS history computed in code; operating indicators → 10-Q
Sources: [BOOK Plotnick p.184–185] (a publisher at 30x on flat earnings vs the index at 23x: risk of decline exceeded the gain); [BOOK Plotnick p.183–184] (in a growth or high-P/E stock any operating weakness is a red flag to sell); [BOOK Plotnick p.187] (sell when 5–10 years of compounded growth are needed to justify the price, or the rate of growth falters); [BOOK Plotnick p.196] (sell when in line with peers and further gains need extraordinary buying); agrees: [BOOK Plotnick p.186] (a small clock maker at 36x swung to a loss and fell from 33 to about 12 in five months); [BOOK Plotnick p.44–45] (a camera maker at about 105x lost most of its price); [BOOK Plotnick p.61] (a steel leader at 83x fell to 16x)
Evidence: C — winner-picked hindsight cases (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact)
Conflicts: R-119 (sell only above a refreshed fair value) — decided by earnings trend: fundamentals on track → R-119 lets a small overshoot run; flat earnings or an operating crack at a high multiple → this rule; R-262 — see Conflicts
Status: UNTESTED

### R-188 Flat earnings: sell for opportunity cost unless a change is visible within a year
School: value | Horizon: position (months) | Instrument: shares
IF a holding's sales and EPS have been flat for about two years or more with margins unchanged AND neither reported results nor announced changes point to strong earnings improvement within about a year THEN sell it and redeploy (the book's view for a profit-seeking, not income, investor) | EXIT the rule is the exit | INVALIDATED BY reported margin or sales gains that start a new uptrend (the case stock later rose on an earnings jump)
Inputs: annual sales, EPS, pretax margin for 3+ years → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); announced changes → 8-K and press releases (FMP secFilings/news)
Sources: [BOOK Plotnick p.175–178] (a restaurant chain earned 50–69 cents a year for six years and traded in about the same range while the Dow roughly doubled; rose when earnings jumped, fell back when they flattened); [BOOK Plotnick p.178] (when earnings are flat, the price stays flat until improvement within about a year is in sight); agrees: [BOOK Plotnick p.182] (a grocery chain fell from 61 to 47 on flat earnings); [BOOK Plotnick p.198] (re-run the full review on a long-inactive holding)
Evidence: C — one detailed case plus examples (1958–1962 cases; prices, tax rates and disclosure rules of that era are not carried as current fact)
Conflicts: none yet
Status: UNTESTED

### R-189 Earnings projection from interim reports: compare like quarters, don't annualise blindly
School: process | Horizon: position (months) | Instrument: shares
IF projecting full-year earnings from interim results THEN compare each quarter with the same quarter a year earlier; don't annualise year-to-date EPS when last year's remaining quarters were weak or loss-making (use the year-to-date figure or less); haircut a projection built on a single quarter; build it as prior full-year sales × (1 + year-to-date sales growth) × current pretax margin × (1 − normal tax rate) ÷ shares, tag it [ESTIMATED], and revise it at every report | EXIT n/a (a method rule) | INVALIDATED BY a nonrecurring item in the interim figures
Inputs: quarterly and annual sales, pretax income, EPS, share count → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); statutory/normal tax rate → 10-K tax note
Sources: [BOOK Plotnick p.130–131] (nine-month EPS of 1.51 not annualised to 2.00 because last year's fourth quarter lost money); [BOOK Plotnick p.135] (sales × margin × tax projection gave $2.40); [BOOK Plotnick p.144] (actual was $1.84 as the margin came in at 3.8% not 4.4%); [BOOK Plotnick p.148] (one strong quarter ×4 gave $3.62; the authors used about $3.00); [BOOK Plotnick p.149–150] (revise when the next quarter's growth differs); [BOOK Plotnick p.174–175] (seasonal quarters: compare with the same quarter a year earlier, then with the prior full year)
Evidence: C — the authors' own projections; the one checked against results overshot EPS by about 30% (p.135 vs p.144); the method sets expectations, it is not a forecast
Conflicts: none yet
Status: UNTESTED

### R-190 Value on recurring, fully taxed earnings
School: value | Horizon: position (months) | Instrument: shares
IF reported EPS is lifted by a low tax charge from loss carry-forwards or tax credits, OR includes nonrecurring gains, other non-operating income or one-off losses THEN restate EPS to recurring operating earnings taxed at the normal rate before computing P/E, the P/E band or any projection; with a large unused carry-forward, assume the market will value the stock on the restated figure | EXIT n/a (a valuation input rule) | INVALIDATED BY a carry-forward that will shelter earnings for the whole holding horizon (then value the shelter separately)
Inputs: income tax expense, pretax income, deferred tax assets/NOL carry-forwards, nonrecurring items, other income → 10-K/10-Q tax and income-statement notes via FMP or Financial Datasets (effective rate and restated EPS computed in code)
Sources: [BOOK Plotnick p.206–207] (a hypothetical: $1.32 of mostly untaxed EPS is about 64 cents taxed, so 24x becomes about 50x; a fruit shipper's untaxed $5 would be valued nearer $2.50); [BOOK Plotnick p.205] (separate other income and nonrecurring items from operating profit); [BOOK Plotnick p.94] (a growth rate inflated by nonrecurring capital gains); agrees: [BOOK Plotnick p.158] (automaker earnings after a loss carry-forward were in effect pretax; halve them to compare); agrees: [BOOK Snow loc.76]
Evidence: D — illustrative arithmetic and assertions; 1960s tax rates (about 50–52%) are dated, use today's statutory rate
Conflicts: none yet
Status: UNTESTED

### R-191 Balance-sheet warning flags: find out why before going on
School: value | Horizon: position (months) | Instrument: shares
IF short-term bank borrowing jumps, OR accounts payable rise much faster than sales, OR current assets fall about 40% in a year with no matching rise in fixed assets or operating loss, OR year-end inventory approaches a full year's sales, OR working capital per share has fallen by half or more over four years, OR the balance sheet carries large assets unrelated to the business THEN stop and get the explanation from the filing; continue only if it is benign | EXIT a holding whose flag is not explained | INVALIDATED BY a documented benign cause (seasonal build, inventory method change, write-off of a long-dead asset, bank borrowing for a profitable expansion)
Inputs: short-term debt, accounts payable, current assets, fixed assets, inventory, working capital, sales, shares for 4 years → 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code); explanations → 10-K/10-Q notes and MD&A (EDGAR)
Sources: [BOOK Plotnick p.119–120] (a 40% drop in current assets: find out what happened; unrelated assets may be a danger sign); [BOOK Plotnick p.121] (short-term bank loans and swelling payables as signs of strain); [BOOK Plotnick p.199] (bank loans are not always adverse); [BOOK Plotnick p.201] (inventory close to a year's sales means overstatement or unsold output); [BOOK Plotnick p.153] (an automaker's working capital per share fell more than 50% in four years: a definite negative)
Evidence: D — asserted checks with one case
Conflicts: R-104 (avoid high accruals) — complementary: R-104 ranks accruals across a universe; this rule flags single-company changes
Status: UNTESTED

### R-192 Announcement-triggered staged screen with early cut-offs
School: process | Horizon: position (months) | Instrument: shares
IF a company announces a change (cost cuts or a labour settlement, a new plant, product or market, a management or board change, a capital-structure change, a financing, a lawsuit settled) THEN run a short first look — price, EPS for the current period vs a year earlier and the last two full years, P/E, shares outstanding, net current assets less long-term debt per share — and stop if earnings are flat or falling while the P/E is rich against the stock's own history; only survivors get the two-year operating review and then the four-year review, and the announcement's content is weighed only once the change is accomplished and the review is done | EXIT n/a (a research-process rule) | INVALIDATED BY n/a
Inputs: announcements → 8-K filings and press releases (FMP secFilings, FMP news, Alpha Vantage NEWS_SENTIMENT); first-look data → quote and 10-K/10-Q income statement and balance sheet via FMP statements or Financial Datasets (computed in code)
Sources: [BOOK Plotnick p.73–74] (signal, then first, second and third looks, each an elimination stage); [BOOK Plotnick p.80] (the signal only directs attention; weigh its meaning after it is accomplished and examined); [BOOK Plotnick p.81–86] (five signal areas); [BOOK Plotnick p.98] (first-look cut-off); [BOOK Plotnick p.197] (most investigations die at the first look; keep promising names under watch at each quarterly report)
Evidence: C — cases where the signal led to a winner (the authors give no count of signals screened or failures)
Conflicts: none yet
Status: UNTESTED


### R-193 Two-method earnings power 2–3 years out × a quality-adjusted market multiple; buy only with about 30% a year to value
School: value | Horizon: long-term (years) | Instrument: shares
IF earnings per share 2–3 years out, projected by two independent methods (a driver model: revenue growth, margin, cost cuts, interest, tax, share count incl. buybacks; and a cross-check: projected revenue × a normal or efficient-peer after-tax margin), land close together AND fair value = that EPS × a multiple anchored on the market's long-run average P/E (about 16; lower for below-average quality or growth, higher for above; no higher than the industry's usual multiple when the industry trades lower) implies roughly 30% a year to fair value over 2–3 years (in the cases, price about 50–65% of the 2–3-year value) THEN the stock is a candidate buy | EXIT when price reaches the refreshed value or the expected development has happened and is priced in (see the consensus-catch-up exit) | INVALIDATED BY the two methods disagreeing materially, or the balance sheet failing the desk's gates
Inputs: revenue, margins, interest, tax rate, diluted shares, buybacks → 10-K/10-Q statements via FMP statements or Financial Datasets (computed in code); projected EPS and multiple → [ESTIMATED] with assumptions shown; market average P/E → S&P 500 P/E history (the author uses 15.8 for 1960–2010); industry multiples → peer quotes via FMP; price → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED); the 30%-a-year hurdle and the agreement band between methods are test parameters
Sources: [BOOK Wachenheim loc.31–32] (IBM 1993: cost-cut model and revenue × 5–6% margin both near $1.50–1.80; valued at 12–13×, bought at about $11.50 vs $20–21); [BOOK Wachenheim loc.44] (base multiple 15.8 = S&P 500 average P/E 1960–2010, adjusted for quality and growth); [BOOK Wachenheim loc.52] (toned down to the industry's lower multiple); [BOOK Wachenheim loc.57] (buys only with about 30% a year potential to net 15–20% after mistakes); agrees: [BOOK Wachenheim loc.86]; [BOOK Wachenheim loc.99]; [BOOK Wachenheim loc.120]; [BOOK Wachenheim loc.128]; [BOOK Wachenheim loc.133] (Lowe's, Whirlpool, Boeing, Southwest, Goldman cases); [BOOK Wachenheim loc.148] (models are aids to judgment, not formulas)
Evidence: C — the author's own fund cases (1985–2014), reconstructed partly from memory (loc.4), winners and losers both shown but no tally; author claims a large share of projections are eventually reached though timing is often off (loc.32), with no count; AIG 2006 on the same method became a near-total loss (loc.75–77)
Conflicts: R-060 (two-thirds-of-value margin of safety) — compatible: this rule adds the 2–3-year return hurdle and the two-method check
Status: UNTESTED

### R-194 Consensus-catch-up exit: sell once the expected development has happened and Wall Street agrees
School: value | Horizon: long-term (years) | Instrument: shares
IF the positive development behind the purchase (cost-cut plan, decongestion, fix of a product problem, price increases) now shows in reported results or in the operating measures the thesis named AND sell-side ratings and estimates have turned broadly positive (upgrades, estimates converging on yours) THEN sell gradually; when the stock can't be valued with confidence, sell about half first and the rest once the good news is widely known | EXIT the rule is the exit | INVALIDATED BY your refreshed value still well above the price because results beat your own assumptions (then hold; see R-119)
Inputs: reported results and named operating measures (e.g. rail train speed and terminal dwell) → 10-K/10-Q statements via FMP statements or Financial Datasets (computed in code) and company quarterly releases; rating changes and estimate revisions → analyst ratings and estimate revisions (FMP analyst, Alpha Vantage EARNINGS_ESTIMATES); price → daily price history (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED); how much upgrade activity counts as consensus is a test parameter
Sources: [BOOK Wachenheim loc.32] (IBM sold at about $16 once the cut was announced and sentiment turned); [BOOK Wachenheim loc.70] (Union Pacific: speed and dwell improved, analysts turned positive, sold near $31 after 3.7 years); [BOOK Wachenheim loc.122] (Boeing: consensus positive by late 2013, reduced); [BOOK Wachenheim loc.131–132] (Southwest: sold half near 3×, the rest when the news was out)
Evidence: C — four author cases; one (IBM 1994) the author calls a costly mistake because buybacks and margins beat his model (loc.33)
Conflicts: R-119 — decided by price vs refreshed value
Status: UNTESTED

### R-195 Industry thesis: own only the net-cash, positive-tangible-book names
School: value | Horizon: long-term (years) | Instrument: shares
IF a stock is chosen to express an industry or cycle thesis THEN study the balance sheet first and accept only names with low debt against cash flow and assets (in the cases: net cash, or debt about a third of equity and falling) and positive tangible book; skip leveraged peers with negative tangible book even when their upside looks larger | EXIT when management turns the balance sheet against holders — debt-funded buybacks or asset purchases at peak prices that push net debt up and tangible book toward zero | INVALIDATED BY n/a (a gate)
Inputs: total debt, cash, equity, goodwill and intangibles (tangible book), operating cash flow → 10-K/10-Q statements via FMP statements or Financial Datasets (computed in code); the debt threshold is a test parameter (the book sets none)
Sources: [BOOK Wachenheim loc.42] (starts every analysis with the balance sheet; drops the idea when debt is high against assets or cash flow); [BOOK Wachenheim loc.129] (Southwest chosen over Delta and United, whose tangible book was negative); [BOOK Wachenheim loc.84] (skipped homebuilders in 2011 on weak balance sheets); [BOOK Wachenheim loc.49–50] (Interstate's later debt-funded buyback left negative tangible book and led to Chapter 11); agrees: [BOOK Wachenheim loc.60] (Centex levering up to buy land at the peak)
Evidence: C — author cases and one cautionary postscript; no tally of rejected names
Conflicts: R-132 — decided by company strength (see that pair)
Status: UNTESTED

### R-196 Cyclical peak: industry volume far above normal demand and the company expanding on debt — sell
School: value | Horizon: position (months) | Instrument: shares
IF industry unit volume (e.g. housing starts) runs well above its normalised level (household formation plus replacement) because demand was pulled forward AND the company is buying inventory or capacity at high prices financed by rising net debt THEN treat current earnings as peak earnings, don't value them at a normal multiple, and sell ahead of the downturn without waiting for signs of weakening demand | EXIT the rule is the exit | INVALIDATED BY a documented structural rise in normal demand
Inputs: monthly housing starts and completions → U.S. Census Bureau new residential construction (released about the 12th business day); household formation → Census housing vacancy survey; company land/lot inventory and net debt → 10-K; how far above normal counts is a test parameter (the case: about 2.0 million starts vs about 1.6 million normal)
Sources: [BOOK Wachenheim loc.58–59] (starts at 1.87–2.0 million vs about 1.6 million normal; pulled-forward demand); [BOOK Wachenheim loc.60–61] (Centex lots up 25% and net debt up over $500 million in 2004; sold at about 6× cost by early 2006, before the bust); agrees: [BOOK Wachenheim loc.100] (capacity additions in tight markets); [BOOK Wachenheim loc.148] (supply responds to high prices)
Evidence: C — one episode (homebuilders 2003–2006), well timed in hindsight
Conflicts: none yet
Status: UNTESTED

### R-197 Cyclical trough: industry volume far below normal and the overhang clearing — buy the strongest beneficiary
School: value | Horizon: long-term (years) | Instrument: shares
IF industry unit volume runs at about half or less of normalised demand (household formation plus replacement, cross-checked against long-run averages scaled to today's population) AND an estimate of excess inventory (past overbuilding plus units vacated by doubling-up, less underbuilding since) clears within about two years at current volume THEN buy the beneficiary with the strongest balance sheet and the cheapest valuation against peers (e.g. most revenue per dollar of market value), valued on revenue at normal unit productivity × its prior normal margin | EXIT when volume normalises and consensus catches up | INVALIDATED BY the overhang estimate rising (e.g. more doubled-up households) or the beneficiary's own fix stalling
Inputs: housing starts and completions, population, doubled-up households → U.S. Census Bureau; company selling space, sales per square foot, operating margin history → 10-K; price/sales vs peers → FMP quotes and statements; normal demand and overhang → [ESTIMATED] with assumptions shown
Sources: [BOOK Wachenheim loc.82–84] (normal demand about 1.5 million units; 2010–2011 build about 40% of that; overhang about 1.5 million clearing by late 2012); [BOOK Wachenheim loc.85–86] (Lowe's valued on sales per square foot back to the 2003 level and 10.5% margin: about $48 vs $24); [BOOK Wachenheim loc.91] (Lowe's $2.08 of revenue per $1 of market value vs Home Depot $1.25; avoided small illiquid names); agrees: [BOOK Wachenheim loc.99] (Whirlpool stayed profitable at the trough)
Evidence: C — one cycle (2011–2014), author's winning case; outcome +160% by end-2014 (loc.90)
Conflicts: none yet
Status: UNTESTED

### R-198 Strong franchise with a temporary, solvable problem: buy when the worst case still covers the price
School: value | Horizon: long-term (years) | Instrument: shares
IF a strong, well-financed company (protected market or duopoly, net cash or low debt) is depressed by a specific operating problem it can fix (congestion, start-up defects, a bloated cost base with a new CEO committing to cuts) AND the problem unit is a small share of earnings or the price sits near book, so the worst case still leaves earnings power that supports the price, AND value on fixed earnings 2–3 years out is at least about 50% above the price THEN buy, and track the operating measures that define the fix | EXIT see the consensus-catch-up exit | INVALIDATED BY the problem proving structural, i.e. the company is weak rather than temporarily impaired
Inputs: segment revenue and earnings → 10-K segment note; book value, net debt → 10-K/10-Q statements via FMP statements or Financial Datasets (computed in code); operating measures of the fix (e.g. train speed, terminal dwell, delivery counts, headcount) → company quarterly releases and 10-Q; value → [ESTIMATED]
Sources: [BOOK Wachenheim loc.66–67] (Union Pacific 2004: congestion, about $0.70 EPS vs $1.55 once fixed, book $12 vs price $14.50); [BOOK Wachenheim loc.70] (fix confirmed by speed and dwell; about 24% a year); [BOOK Wachenheim loc.117–121] (Boeing 2012: the 787 about 18% of revenue and 4–5% of earnings, value about $145 vs $75); [BOOK Wachenheim loc.31–32] (IBM cost cuts under a new CEO); agrees: [BOOK Wachenheim loc.122] (prefers strong companies with solvable problems; avoids weak-company turnarounds); agrees: [BOOK Fisher loc.94–96] (first full-scale plant shake-down depresses EPS and the price; buy then; American Cyanamid's Fortier plant, 1954); [BOOK Fisher loc.98–100] (Food Machinery's chemical divisions, 1957); [BOOK Fisher loc.102–103] (labour trouble fixable in months; buying points A and B while officers bought heavily)
Evidence: C — three author cases, all winners as told
Conflicts: R-132 — decided by company strength (see that pair); R-256 — see Conflicts
Status: UNTESTED

### R-199 Thesis-break exit: sell at a modest loss when the expected development fails or value drops below price
School: value | Horizon: long-term (years) | Instrument: shares
IF a holding falls THEN re-test the purchase reasons: IF the specific development the purchase relied on visibly fails (a competitor cuts costs instead of raising prices; a cartel stops defending a commodity price) OR a new adverse fact (currency collapse in a large segment, commodity price below the thesis level) lowers the refreshed value to or below the price THEN sell, even at a loss, and don't adopt a new theory to keep holding; IF the reasons still hold THEN hold or add per R-083 | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: refreshed valuation → [ESTIMATED] with assumptions shown; catalyst evidence → news (Alpha Vantage NEWS_SENTIMENT, FMP news) and 8-Ks; geographic segment share → 10-K; commodity prices → Alpha Vantage WTI/BRENT or other commodity series
Sources: [BOOK Wachenheim loc.80] (Praxair 2014: the expected competitor price discipline did not come and about 14% of earnings were in Brazil as the real fell; sold at a modest loss); [BOOK Wachenheim loc.142–144] (oil 2014: crude below $80 with a growing surplus, normal price estimated at $55–70, sold before OPEC's formal shift); [BOOK Wachenheim loc.103] (re-test reasons on weakness; add if valid, sell if the analysis was wrong); [BOOK Wachenheim loc.148] (admit mistakes readily); agrees: [BOOK Fisher loc.108–109] (sell a purchase once the facts are clearly worse than believed; waiting to break even is the costliest habit)
Evidence: C — author cases; the counter-case is AIG, held through 2008 on an intact-looking thesis (loc.76–77)
Conflicts: R-061 — decided by school (see that pair)
Status: UNTESTED

### R-200 Concentrated but capped: 15–25 holdings, at most 12% per stock and 25% per industry, measured at cost
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF building a long-term stock portfolio THEN hold about 15–25 names, buy no stock beyond 12% of the portfolio and no industry beyond 25%, measuring both at cost so a holding that has risen is not forced down while still attractive | EXIT n/a (a sizing rule) | INVALIDATED BY n/a
Inputs: cost basis per position and industry → Cyrus's position list; industry → company profile (FMP company); the caps are test parameters
Sources: [BOOK Wachenheim loc.56] (the 12%/25% at-cost policy); [BOOK Wachenheim loc.148] (15–25 holdings; first picks carry the best risk/reward); agrees: [BOOK Wachenheim loc.36] (typical holdings about 8–9.5% each); agrees: [BOOK LopezLira p.270–271] (when news clusters in one sector, cap further buying there or hedge with other sectors or an index)
Evidence: C — the author's stated fund policy; no test against other limits
Conflicts: R-139 — decided by measurement base; R-028 — decided by horizon; MoralesKacher principle (fewer, larger positions) — decided by style and horizon: active trend-following book → fewer names; long-term value portfolio → this rule; R-263 — see Conflicts
Status: UNTESTED

### R-201 Pension expense at economic cost when discount rates are abnormally low
School: value | Horizon: long-term (years) | Instrument: shares
IF a company's reported pension liability and expense have jumped mainly because the discount rate fell (long-term yields well below their multi-year average) THEN compute a second EPS with pension expense adjusted using the 10-K's sensitivity to a 1-point rate change, moving the rate toward its average, and value on both the GAAP and the adjusted figure | EXIT n/a (a valuation input rule) | INVALIDATED BY rates staying low, or underfunding that forces cash contributions
Inputs: pension liability, expense, discount rate and rate sensitivity → 10-K pension note; long-term yields → FRED (corporate AA or Treasury series); adjusted EPS → [ESTIMATED] with assumptions shown
Sources: [BOOK Wachenheim loc.119] (Boeing: each 1-point rise cut liability by $9.1 billion and expense by $930 million; GAAP vs adjusted 2015 EPS $7.50 vs $8.25); [BOOK Wachenheim loc.117] (pension and health liabilities $23.0 billion vs $8.2 billion five years earlier)
Evidence: C — one author case
Conflicts: none yet
Status: UNTESTED

### R-202 Large financial near tangible book with normal return on tangible equity well above the cost of equity
School: value | Horizon: long-term (years) | Instrument: shares
IF a large, well-capitalised financial trades near tangible book (the case: 1.1×) AND normal earnings power (capital-light segments' earnings plus allocated tangible equity × a conservative normal ROE) is about 14% of tangible book or more AND leverage has fallen and regulators are allowing large buybacks THEN value it at 12–15× that earnings power grown a few years | EXIT see the consensus-catch-up exit | INVALIDATED BY a funding or collateral squeeze (marked-to-market losses that force capital raising) — the AIG failure mode
Inputs: tangible book per share, segment earnings, total assets and equity → 10-K/10-Q; buyback amounts → cash-flow statement; regulatory capital and stress-test results → regulator releases; normal ROE and earnings power → [ESTIMATED]
Sources: [BOOK Wachenheim loc.132–133] (Goldman 2014: price $159.80 vs tangible book $145.04, earnings power about $20 = about 14% of TBV, value $265–330); [BOOK Wachenheim loc.134] (assets/equity from 26× to under 12×; Fed-approved buybacks); [BOOK Wachenheim loc.141] (first quarter 2015 at 15% return on tangible equity); counter-case: [BOOK Wachenheim loc.75–77] (AIG valued on a 15% normal ROE × book, collapsed in September 2008)
Evidence: C — one success and one near-total loss on the same logic
Conflicts: R-133 — compatible: R-133 sets the capital and risk gates; this rule adds the tangible-book entry and earnings-power method
Status: UNTESTED

### R-203 Capacity discipline: industry capacity shrinking while demand grows — buy the best-financed operator
School: value | Horizon: position (months) | Instrument: shares
IF industry capacity (e.g. airline available seat-miles) has fallen over several years while demand (revenue passenger-miles) has risen, so utilisation is near a record and few new units are on order THEN expect real price increases; estimate EPS per 1% of price, add announced cost programmes and buybacks, cross-check with revenue × the company's past peak margin, and buy the operator with net cash and positive tangible book | EXIT when the price gains show in results and consensus catches up | INVALIDATED BY a wave of new capacity orders
Inputs: capacity, traffic and load factor → Bureau of Transportation Statistics T-100 data or company 10-K; order backlogs → manufacturer releases; revenue, margins, net debt, tangible book → 10-K/10-Q statements via FMP statements or Financial Datasets (computed in code); EPS sensitivity → [ESTIMATED]
Sources: [BOOK Wachenheim loc.123–124] (domestic seat-miles −3.1% and traffic +12.4% in 2000–2011; load factor 71.6% → 83.1%); [BOOK Wachenheim loc.127–128] (Southwest: 1% fare ≈ $0.13 EPS; second method on the 16–18% pre-2001 margin); [BOOK Wachenheim loc.129] (Southwest chosen for its balance sheet); [BOOK Wachenheim loc.130] (fuel-adjusted fares +8.6% in Q3 2013; EPS +161%)
Evidence: C — one author case (2012–2014)
Conflicts: none yet
Status: UNTESTED

### R-204 Structural share shift: unit growth far above the industry for a reason the Street hasn't written up
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company's unit growth runs far above its industry's (the cases: 12–27% a year vs about 1.5%) for an identifiable structural reason (smaller rivals losing their financing) AND no sell-side report reflects that share-shift thesis AND the stock trades at a low multiple THEN buy on 2–4-year EPS with operating leverage on fixed costs | EXIT on the cyclical-peak rule or the consensus-catch-up exit | INVALIDATED BY the industry's unit volume rising above normal demand (then the gains are cyclical, not structural)
Inputs: company unit deliveries → 10-K; industry units → U.S. Census Bureau; analyst coverage → analyst ratings and estimate revisions (FMP analyst, Alpha Vantage EARNINGS_ESTIMATES) and report text; multiple → price and EPS
Sources: [BOOK Wachenheim loc.54–55] (public builders gaining on private ones after the savings-and-loan crisis cut small builders' credit; Centex valued at about $63 vs under $12); [BOOK Wachenheim loc.57] (EPS $2.11 → $6.01 in 1999–2003, yet the stock stayed under 10× earnings); agrees: [BOOK Fisher loc.104] (the buying range is an earnings rise coming in the right company that the price has not yet reflected); [BOOK Fisher loc.164] (improvements made by little-known executives re-rate slowly)
Evidence: C — one episode, a winner (about 6× by 2006)
Conflicts: none yet
Status: UNTESTED

### R-205 Credit-crisis re-entry: hold cash until credit spreads narrow, then buy the most depressed cyclicals
School: process | Horizon: position (months) | Instrument: shares
IF a systemic credit crisis has frozen funding and spreads between Treasuries and lower-quality debt are at extremes THEN hold the cash raised from sold financials and fully valued stocks; once spreads have clearly narrowed and confidence returns, redeploy into the most depressed, most economically sensitive sector (largest drawdown vs the index) | EXIT n/a | INVALIDATED BY spreads widening again
Inputs: corporate credit spreads → FRED (Moody's Baa minus 10-year Treasury, high-yield option-adjusted spread); sector drawdowns → sector index or ETF price history; the narrowing threshold is a test parameter
Sources: [BOOK Wachenheim loc.77–78] (cash to about 40% after Lehman; reinvested in March 2009 as spreads narrowed, mostly industrials, down 54% vs the S&P's 45%); author claims −38% in 2008, +47% in 2009, +21% in 2010
Evidence: C — one episode; the author otherwise rejects market timing (loc.148), so this applies only to systemic credit crises
Conflicts: none yet
Status: UNTESTED

### R-206 Acquisition-built companies: value the bought businesses near what was paid
School: value | Horizon: long-term (years) | Instrument: shares
IF a company has been largely assembled from recent acquisitions THEN value the acquired businesses at about their purchase price, plus a premium only for growth or synergies achieved since, less a discount where it overpaid, so the whole is worth little premium to stated book | EXIT n/a (a valuation input rule) | INVALIDATED BY acquired units showing returns well above the price paid
Inputs: acquisition prices, goodwill and intangibles, segment results → 10-K and 8-Ks; book value → balance sheet; how large an acquired share counts is a test parameter
Sources: [BOOK Wachenheim loc.148] (auction buyers pay the price no one else would; acquired parts worth about their cost); agrees: [BOOK Wachenheim loc.104] (seller knows more than buyer)
Evidence: D — assertion with an auction analogy
Conflicts: none yet
Status: UNTESTED

### R-207 Market normal value: trend-line S&P 500 earnings × the long-run average P/E
School: value | Horizon: long-term (years) | Instrument: shares
IF the S&P 500 sits well above its normal level (trend-line earnings fitted over several decades × the long-run average P/E; the author's example flags about 21% over as overvalued) THEN tighten buy standards and let cash build from selling fully valued holdings, without hedging or shorting; near or below normal, stay fully invested if enough stocks qualify | EXIT the label changes as the gap moves | INVALIDATED BY a structural change in the earnings trend
Inputs: S&P 500 annual earnings history → S&P Dow Jones Indices or the Shiller data set; index level → index quote; trend fit and normal level computed in code; the overvaluation threshold is a test parameter
Sources: [BOOK Wachenheim loc.148] (regression of S&P 500 earnings 1960–2000: about 6.8% a year, average P/E 15.8, normal level about 739 in 2000 and about 1,427 in 2010); agrees: [BOOK Wachenheim loc.8] (cash builds as a by-product of selling, not as a hedge)
Evidence: B — the author's own regression on S&P data with the method described; its use as a signal is untested
Conflicts: R-018 — decided by input availability
Status: UNTESTED


### R-208 9 EMA crosses above the 13 EMA while the 13 EMA is above the 50 EMA
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF the 9-period EMA crosses above the 13-period EMA while the 13-period EMA is above the 50-period EMA THEN buy | EXIT not given by the book (test parameter, e.g. the 9 EMA crossing back under the 13 EMA, or R-045 stops) | INVALIDATED BY the 13 EMA falling below the 50 EMA
Inputs: EMA(9), EMA(13), EMA(50) → computed in code from daily closes (FMP chart, Alpha Vantage TIME_SERIES_DAILY); bar length not stated by the book, daily assumed for swing use
Sources: [BOOK Broker p.247]
Evidence: D — one-sentence assertion; no example, sample or test
Conflicts: none yet. Close cousin of R-026 (12/50 EMA trend filter) and R-002 (pullback entry in the same alignment)
Status: UNTESTED

### R-209 Implied volatility against its own history picks the side: rich → write, cheap → buy
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock's implied volatility is high against its own IV history (and against the market's level) THEN favour writing structures (covered calls, credit spreads); IF it is low THEN favour buying options, and only when a move is expected | EXIT n/a (structure selection) | INVALIDATED BY n/a (the book gives none); a scheduled event inside the expiry that explains the high IV falls under R-076
Inputs: current IV → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus); IV history → historical chains (Alpha Vantage HISTORICAL_OPTIONS); event dates → earnings and economic calendars. 'High' and 'low' (e.g. an IV percentile cut-off) are test parameters; the book gives none
Sources: [BOOK Broker p.218]; [BOOK Broker p.218–219] (earnings, spin-offs, launches, data releases and Fed meetings move IV, so know them before picking an expiry); agrees: [BOOK Smith p.80–84] (high IV vs its own range and above HV → write; low and below HV → buy; explicit conditions in R-234)
Evidence: D — asserted
Conflicts: none yet. Consistent with the credit-seller principle (IV high at entry, falling during the trade) [BOOK FreemanCS loc.40–42]
Status: UNTESTED

### R-210 Iron condor for a stock holding a range
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock has been holding between clear support and resistance (neutral view; the desk would require the R-007 range conditions) THEN sell an out-of-the-money put below support and an out-of-the-money call above resistance and buy a further-out put and call as wings, all the same expiry, for a net credit; the trade profits if price stays between the short strikes | EXIT not given by the book (test parameter; see R-074 for credit-spread exits) | INVALIDATED BY a sharp move through either short strike
Inputs: support/resistance → daily OHLC; strikes, bid/ask, IV, open interest, expiry → options chain snapshot
Sources: [BOOK Broker p.198]; [BOOK Broker p.207–208] (hypothetical: stock at $120, short 100 put and 140 call at $3 each, long 90 put and 160 call; one wing premium missing and the wings are unequal, 10 vs 20 points)
Evidence: D — one incomplete hypothetical example
Conflicts: none yet. Sibling of R-079 (short iron butterfly): same neutral view, wider profit zone, smaller credit
Status: UNTESTED

### R-211 Take RSI signals only in the direction of the MACD trend
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF the MACD line (12-EMA minus 26-EMA) is above its 9-period signal line THEN act only on bullish RSI signals (RSI dropping toward its oversold zone and turning up) and ignore overbought readings; IF the MACD line is below its signal line THEN act only on bearish RSI signals and ignore oversold readings | EXIT not given by the book (test parameter) | INVALIDATED BY a MACD cross against the position
Inputs: RSI(14), MACD(12,26,9) → computed from daily closes (Alpha Vantage RSI, MACD); the trend-adjusted oversold/overbought zones are test parameters (the book says only that they sit well above 30 in uptrends and well below 70 in downtrends)
Sources: [BOOK Broker p.281] (credits Constance Brown for the shifted zones; pairs a leading with a lagging indicator)
Evidence: D — second-hand assertion; no example or test
Conflicts: none yet. Related: R-031 (MACD trend confirmation); MoralesKacher principle (oscillators fight trends) — decided by regime: ranges → this rule; trending leaders → avoid
Status: UNTESTED

### R-212 Daily pivot levels: range between S1 and R1, breakouts count only beyond them
School: day-trading | Horizon: day | Instrument: shares
IF trading intraday THEN compute from the prior session P = (high + low + close) / 3, R1 = 2P − low, S1 = 2P − high, R2 = P + (R1 − S1), S2 = P − (R1 − S1); expect the session to trade mostly between S1 and R1: range traders fade at R1/S1, breakout traders count a move only once it clears R1 or S1 | EXIT not given by the book | INVALIDATED BY n/a
Inputs: prior day high, low, close → daily OHLC; intraday price → intraday bars
Sources: [BOOK Broker p.261–262]
Evidence: D — asserted, mainly for FX, also said to apply to index day trading; no test
Conflicts: none yet. Intraday: recorded only
Status: UNTESTED


### R-213 LLM headline score: long good news, short bad news, hold one day
School: day-trading | Horizon: day | Instrument: shares
IF a headline (full article or press release, highly relevant to one company, duplicates removed, not a price-move item) is classified by a large language model at temperature 0 as good news for that company's stock (score +1) or bad news (−1), averaged across the stock's headlines that day, THEN go long positive-score stocks and short negative-score stocks in a zero-cost book, entering at the first open (or close) after the news — pre-open news trades that day, intraday news through the next day's close, after-close news the next day | EXIT after the one-day / overnight hold | INVALIDATED BY a desk backtest after costs on the desk's own news feed showing no edge, or returns that vanish once spreads are charged (the book says higher costs erode it)
Inputs: headlines with release timestamps → news feeds (Alpha Vantage NEWS_SENTIMENT, FMP news, Financial Datasets news); relevance and de-duplication → computed in code; good/bad/unknown score → an LLM prompt run in code (persona: financial expert; first line yes/no/unknown on whether the headline is good for the named company's stock, then one sentence); next-day returns → daily OHLC (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED)
Sources: [BOOK LopezLira p.225–227] (data, filters, timestamps); [BOOK LopezLira p.227–230] (prompt design, temperature 0; context can make a negative-sounding headline good for the named company); [BOOK LopezLira p.231–232] (scoring, timing, regression with stock and time controls, long-short build); [BOOK LopezLira p.233] (author claims about 550% for the GPT-3.5 long-short, Oct 2021–Dec 2022, before costs; short leg about 250%; GPT-4 lower return but lower volatility and drawdown); [BOOK LopezLira p.234] (newer models beat GPT-1/2 and BERT, and held up on hard-to-read news); [BOOK LopezLira p.256] (author expects the edge to be larger in smaller, less liquid stocks that underreact, where costs are also higher); agrees: [BOOK LopezLira p.382] (costs up to 25 bps per trade still left notable returns; higher costs eroded them sharply); agrees: [BOOK LopezLira p.337–338] (short leg strongest, combined long-short better); agrees: [BOOK LopezLira p.397] (source study: Lopez-Lira & Tang, SSRN working paper, April 2023)
Evidence: B — the author's own academic study: rules, universe (US common stocks with news) and period are shown, but the text gives no observation count or significance figures, results are simulated and before costs, and the headline return differs between sections (over 400% in about 18 months at p.19–20 vs 550% at p.233)
Conflicts: R-130 — decided by horizon: a one-day hold on fresh news → this rule; a multi-year hold where intrinsic value sits above the price → R-130. R-164 Gap-fill bias — decided by a desk test on the same news days. Recorded only for calls: the desk has no real-time feed to act at the next open on overnight news, but it can backtest the rule
Status: UNTESTED

### R-214 Inverse-variance weights inside a per-name cap
School: risk/sizing | Horizon: any (portfolio construction) | Instrument: shares
IF building a multi-name basket (long, short or both) THEN weight each position in proportion to 1 ÷ its historical return variance, then cap every name at a fixed share of the portfolio (the book's examples: 1%, 2%, 5% or 10%) and trim any name that rises above the cap | EXIT n/a (sizing rule) | INVALIDATED BY n/a
Inputs: return variance → daily closes (FMP chart, Alpha Vantage TIME_SERIES_DAILY_ADJUSTED), computed in code (look-back length is a test parameter; the book gives none); position weights → Cyrus's position list
Sources: [BOOK LopezLira p.260] (cap per position, long or short; trim when exceeded); [BOOK LopezLira p.261] (inverse-variance weighting as simplified mean-variance); [BOOK LopezLira p.264] (worked setup: 2% cap with inverse-variance weights); agrees: [BOOK LopezLira p.385] (no position above 2% of the portfolio; inverse-variance weights)
Evidence: D — asserted; the five-year backtest at p.264 is described as a hypothetical with no results
Conflicts: none yet. The desk's C7 tiers govern every verdict; complements R-121 (Kelly weight) and R-200 (concentration caps)
Status: UNTESTED

### R-215 Momentum names: check news sentiment before buying
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF a stock passes a price-momentum screen (e.g. R-098) THEN score its recent news with an LLM: positive momentum with clearly negative sentiment → mark it a riskier bet and skip or downsize; positive momentum with strongly positive sentiment → keep as the stronger candidate | EXIT per the momentum rule in use | INVALIDATED BY a desk backtest showing the sentiment overlay adds nothing to the momentum screen
Inputs: momentum → daily closes, computed in code; news sentiment → news feeds (Alpha Vantage NEWS_SENTIMENT, FMP news, Financial Datasets news) scored by an LLM run in code; look-back for news and score cut-offs are test parameters (the book gives none)
Sources: [BOOK LopezLira p.282–284]; [BOOK LopezLira p.281] (weigh sentiment against financial metrics rather than trading it alone); agrees: [BOOK LopezLira p.389] (combine momentum signals with sentiment scores)
Evidence: D — a hypothetical firm's workflow; no test
Conflicts: none yet. An overlay on R-098
Status: UNTESTED

### R-216 Negative news-sentiment shift on a holding: review, reduce if price agrees
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF a holding's rolling news-sentiment score turns clearly negative (an LLM-scored average over recent news) AND recent price and volume confirm the weakness THEN re-check the holding's case and reduce the position; keep monitoring | EXIT the rule is a reduce trigger | INVALIDATED BY the fundamentals check showing the news doesn't touch the case, or sentiment recovering
Inputs: news → news feeds (Alpha Vantage NEWS_SENTIMENT, FMP news, Financial Datasets news), scored by an LLM in code; price and volume → daily OHLCV; fundamentals → 10-K/10-Q via FMP or Financial Datasets. Window and 'clearly negative' cut-off are test parameters
Sources: [BOOK LopezLira p.285–286] (sentiment as an early warning that complements, not replaces, financial analysis); [BOOK LopezLira p.287–288] (worked scenario); agrees: [BOOK LopezLira p.388] (sentiment as an early-warning system for preemptive action)
Evidence: D — the scenario's happy outcome is invented for illustration, not a result
Conflicts: none yet. Close cousin of R-186 (sell when operating indicators turn down) and R-199 (thesis-break exit)
Status: UNTESTED


### R-217 Pocket pivot: early buy inside a quiet base
School: growth/momentum | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF a fundamentally strong leading stock (strong earnings and sales growth, margins, ROE) is in a constructive base — tight sideways action with volume drying up, usually on the base's right side — AND today it moves up off or through its 10-day or 50-day SMA AND today's volume is higher than the highest down-day volume of the prior 10 sessions AND the day's price bar touches the 10-day SMA (not extended) AND it closes up on the day in the upper half of its range THEN buy an initial position (pivot price = the day's close; next-day buys only within a preset small distance of it) | EXIT 7–8% below cost at most (see R-221), then the moving-average guide in R-220 | INVALIDATED BY a multimonth (≥5-month) downtrend, a close under the 50-day or 200-day SMA (exception: support near the 200-day after a big market correction), a V-shaped straight-up-from-the-bottom move just before, or a rise on below-average volume (wedging) just before
Inputs: 10-day/50-day/200-day SMA, up/down-day volume, daily range and close → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code; earnings, sales, pretax margin, ROE → 10-K/10-Q (FMP, Financial Datasets); 'constructive base' and 'leader' are judgement inputs to be defined as test parameters (e.g. 20-day range width, volume below its 50-day average)
Sources: [BOOK MoralesKacher loc.8–9] (definition and volume signature); [BOOK MoralesKacher loc.106] (context); [BOOK MoralesKacher loc.160–161] (ten commandments); [BOOK MoralesKacher loc.161] (close in upper half); [BOOK MoralesKacher loc.163] (pivot price); [BOOK MoralesKacher loc.164] (bar must touch the 10-day SMA); [BOOK MoralesKacher loc.171] (late-entry distance)
Evidence: C — chart case exercises (about 40 charts, hindsight) and the authors' trades; they say Kacher back-tested pocket pivots to the 1920s on 'thousands' of charts with no sample, rules or results shown [BOOK MoralesKacher loc.167]; authors claim about half of high-quality pocket pivots work in uptrending markets with losses usually held to about 5% [BOOK MoralesKacher loc.173], and decline to give aggregate results [BOOK MoralesKacher loc.166]
Conflicts: R-005 — decided by a desk test: this rule buys inside the base before the breakout; R-005 waits for the breakout and a retest
Status: UNTESTED

### R-218 Continuation pocket pivot: add to a winner at the 10-day line
School: growth/momentum | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF a stock already held at a profit after a breakout is trending along its 10-day or 50-day SMA AND it moves up off or through that average on volume above the highest down-day volume of the prior 10 sessions AND the day's bar touches the 10-day SMA THEN add to the position instead of adding at a fixed +2% from the buy price | EXIT each add on the R-220 guide; a continuation buy that is your first position uses the 10-day violation as its stop | INVALIDATED BY a price bar well above the 10-day SMA (extended: wait for the average to catch up) or the stock sinking back into its base
Inputs: 10-day/50-day SMA, up/down-day volume → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code; position cost → position list
Sources: [BOOK MoralesKacher loc.5]; [BOOK MoralesKacher loc.10] (Google 2004 example; preferred to adding 2% higher); [BOOK MoralesKacher loc.164] (extended = bar not touching the 10-day line); [BOOK MoralesKacher loc.172] (stop for a first position bought this way)
Evidence: C — chart cases (GOOG 2004, FSLR 2007, APKT 2010) told in hindsight; no tally
Conflicts: consistent with R-081 and R-022 (adds only to winners); total risk must still fit R-009 and the desk's C7 tiers
Status: UNTESTED

### R-219 Buyable gap-up: buy the big-volume gap, stop under the gap-day low
School: growth/momentum | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF a fundamentally strong stock gaps up out of a constructive base or a coherent uptrend AND the gap is at least 0.75× its 40-day average true range AND volume is above 1.5× its 50-day average volume THEN buy on the gap day (at least part at the open) or the next day while still near the gap-day range | EXIT below the gap day's intraday low with 1–2% leeway; no leeway for a flawed setup; skip the trade if that stop is more than 7–8% below your price | INVALIDATED BY a gap after a severe downtrend or below the 200-day SMA without a rounded base, an exhaustion gap at the end of a multi-month parabolic run, a second gap-up within about two weeks, or a former leader that has already topped
Inputs: gap size (open vs prior high), 40-day ATR, 50-day average volume, 200-day SMA → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code; earnings date as the usual catalyst → Alpha Vantage EARNINGS_CALENDAR; fundamentals → 10-K/10-Q
Sources: [BOOK MoralesKacher loc.11–12]; [BOOK MoralesKacher loc.128] (worked thresholds: 1.48× volume fails, gap 1.95 vs 0.75×ATR 1.85 passes); [BOOK MoralesKacher loc.130]; [BOOK MoralesKacher loc.131–132] (1–2% leeway; exhaustion gap); [BOOK MoralesKacher loc.133] (defective base: no leeway); [BOOK MoralesKacher loc.141] (SPWR exhaustion gap); [BOOK MoralesKacher loc.175–176] (fundamentals required; 7–8% check)
Evidence: C — chart cases with some failures shown (NFLX, CPHD, ISRG Aug 2011) but no tally; the leeway is given as 2–3% [BOOK MoralesKacher loc.12], 1–3% [BOOK MoralesKacher loc.101] and 1–2% [BOOK MoralesKacher loc.131] — inconsistent, a test parameter
Conflicts: R-164 — decided by horizon and setup: R-164 is an intraday gap-fill bias; this rule needs a daily close-based base and volume ≥1.5× average and holds for weeks; R-161 — decided likewise
Status: UNTESTED

### R-220 Seven-Week Rule: trail a growth winner on the 10-day or 50-day line
School: risk/sizing | Horizon: position (months) | Instrument: shares
IF after a buy point (pocket pivot in or out of a base, breakout or buyable gap-up; not a continuation add) the stock has held its 10-day SMA for at least seven weeks without a violation THEN use a 10-day violation as the sell signal (all or part); IF it violated the 10-day within the first seven weeks THEN use a 50-day violation instead. A violation = a close below the average AND a later trade below that day's intraday low | EXIT as stated; reduce 50%+ earlier on a mini gap-down or a high-volume reversal off a peak | INVALIDATED BY n/a (an exit rule); the 7–8% maximum loss (R-221) comes first
Inputs: 10-day/50-day SMA, daily closes and lows, buy-point date → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code; buy dates → trade log
Sources: [BOOK MoralesKacher loc.13–15]; [BOOK MoralesKacher loc.95] (why the first close below is not a violation); [BOOK MoralesKacher loc.147–149] (FSLR walk-through); [BOOK MoralesKacher loc.165] (when the seven-week count resets); [BOOK MoralesKacher loc.176–177]; [BOOK MoralesKacher loc.168]
Evidence: C — chart cases (AAPL 2010/2012, FSLR 2007, APKT 2010–11) in hindsight; APKT shook out at the 50-day several times before rising, which the authors show
Conflicts: R-061 — decided by a desk test on the same growth holdings: both trail a growth winner on price (20% from the peak vs a moving-average violation); R-010 — decided by school: this rule sets no target (authors reject fixed reward:risk targets) while R-010 needs one
Status: UNTESTED

### R-221 7–8% maximum loss from the purchase price (on the underlying for option proxies)
School: risk/sizing | Horizon: swing (days–weeks) to position (months) | Instrument: shares / options
IF a long stock position falls 7–8% below its purchase price THEN sell it, before any moving-average or gap-low stop is reached; IF an option is used as a stock proxy THEN apply the same 7–8% to the underlying stock's move, not the option's price | EXIT the rule is the exit | INVALIDATED BY n/a. Before buying: if the planned stop is further away than this, buy less or skip
Inputs: purchase price and daily lows → position list and price history; underlying price for options → quote
Sources: [BOOK MoralesKacher loc.24] (O'Neil's 7–8%; Livermore's 10%); [BOOK MoralesKacher loc.26] (stock 10% above your exit → skip or buy smaller); [BOOK MoralesKacher loc.168] (obey 7–8% first); [BOOK MoralesKacher loc.172]; [BOOK MoralesKacher loc.176] (allow 9–10% only for outstanding leaders on a gap-up); [BOOK MoralesKacher loc.184] (options: measure on the stock)
Evidence: D — O'Neil's rule relayed second-hand; the authors note O'Neil claims his studies show winners rarely fall more than 7–8% below the buy point, not shown here [BOOK MoralesKacher loc.24]
Conflicts: R-061 — decided by entry type: a buy at a defined pivot near support → this rule; a growth holding expected to swing widely, bought without a pivot → R-061's 20%
Status: UNTESTED

### R-222 Earnings-gap budget: size into a report by the portfolio hit you can take
School: risk/sizing | Horizon: swing (days–weeks) | Instrument: shares
IF a holding reports earnings before the next session THEN compute portfolio damage = position weight × a 10%, 20% and 30% gap-down; IF the damage at the plausible gap exceeds what the profit cushion allows (authors' example: up to 5–10% of the portfolio only with a large cushion; about 2–5% with a 1–2% cushion; a small position only with no cushion) THEN cut the position to fit before the report | EXIT after the report by the normal sell rules | INVALIDATED BY n/a
Inputs: earnings date → Alpha Vantage EARNINGS_CALENDAR; position weight and cost → position list; profit cushion → price vs cost; tolerance → Cyrus
Sources: [BOOK MoralesKacher loc.44]; [BOOK MoralesKacher loc.172] (worst case 20–30%; hold big positions only with a cushion); agrees [BOOK MoralesKacher loc.51] (sold half of AAPL before the October 2004 report)
Evidence: D — arithmetic with the authors' own example (AAPL 2004 half-sale); no test
Conflicts: complements R-159 (which exits weak names before reports)
Status: UNTESTED

### R-223 Big high-volume gap-down on a holding: sell at the open
School: risk/sizing | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF a holding gaps down sharply relative to its chart on heavy volume (the authors' line: more than 15%) THEN sell at the open; if that wasn't done, sell when it later trades below the gap-down day's low; IF the gap is smaller THEN sell part and watch the close and the next days | EXIT the rule is the exit | INVALIDATED BY n/a
Inputs: open vs prior close, volume vs 50-day average, gap-day low → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code
Sources: [BOOK MoralesKacher loc.179–180]; agrees [BOOK MoralesKacher loc.156] (APKT July 2010: sold at the open on a massive-volume gap-down); agrees [BOOK MoralesKacher loc.64] (FFIV: stop hit on an earnings gap-down, sold at the open)
Evidence: D — the authors say 'statistical studies have shown' such stocks should be sold but cite none [BOOK MoralesKacher loc.179]; two of their own cases
Conflicts: R-130 — decided by horizon and thesis: a multi-year value-backed buy after an earnings miss → R-130; a price-managed growth holding → this rule
Status: UNTESTED

### R-224 Too extended: no new buys 80% or more above the 200-day line
School: growth/momentum | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF a stock's price is 80% or more above its 200-day SMA THEN treat a new buy as higher risk: skip it or buy a smaller-than-normal position | EXIT n/a (an entry filter) | INVALIDATED BY n/a
Inputs: price and 200-day SMA → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code
Sources: [BOOK MoralesKacher loc.183]
Evidence: D — one sentence of assertion; no test
Conflicts: none yet
Status: UNTESTED

### R-225 Prefer breakouts to all-time highs over breakouts below heavy overhead supply
School: growth/momentum | Horizon: swing (days–weeks) to position (months) | Instrument: shares
IF two related candidates break out at the same time AND one is at a fresh all-time high while the other is still below a recent peak where heavy volume traded before a sharp fall THEN favour the all-time-high breakout, since no holder is waiting to sell at breakeven | EXIT per the entry rule used | INVALIDATED BY n/a (a ranking rule)
Inputs: all-time high, prior peak and its volume → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code (full history)
Sources: [BOOK MoralesKacher loc.72] (gold vs silver ETFs, July 2011)
Evidence: C — one pair, told in hindsight as the authors' own mistake
Conflicts: none yet
Status: UNTESTED

### R-226 Short a broken former leader on a dry-volume rally into resistance
School: swing-technical | Horizon: swing (days–weeks) | Instrument: shares
IF a stock that led the prior bull phase has broken down from its peak and is forming a top (head-and-shoulders or a late-stage failed base) AND it rallies on shrinking volume up into its 50-day or 200-day SMA or the neckline AND an up day prints volume at least 45% below average (a 'voodoo' dry-up day) THEN sell short, scaling in over three or more pieces | EXIT stop 3–5% above entry, or just above the resistance or the entry day's high | INVALIDATED BY a heavy-volume move back above the resistance level
Inputs: prior leadership, peak, moving averages, neckline, volume vs 50-day average → daily OHLCV → price history (Alpha Vantage TIME_SERIES_DAILY / FMP chart), moving averages computed in code
Sources: [BOOK MoralesKacher loc.191] (short candidates are the prior bull market's leaders); [BOOK MoralesKacher loc.192] (stops); [BOOK MoralesKacher loc.193] (voodoo day; X 2008 example); [BOOK MoralesKacher loc.194] (layering); [BOOK MoralesKacher loc.155] (FSLR Sep 2008 late-stage failed base under the 200-day)
Evidence: C — two chart cases (U.S. Steel 2008, First Solar 2008), hindsight; the authors defer detail to another book
Conflicts: agrees in spirit with R-004 (H&S neckline); new short sellers should use only 10–20% of the account at first [BOOK MoralesKacher loc.193]
Status: UNTESTED

### R-227 Institutional sponsorship: owned but not saturated, and rising
School: growth/momentum | Horizon: position (months) | Instrument: shares
IF institutions own roughly 30–60% of a stock's shares AND the total shares held by institutions is rising quarter over quarter THEN count sponsorship as a positive for a growth buy; IF ownership is far above that range after a big run THEN treat it as potential supply | EXIT n/a (a filter) | INVALIDATED BY n/a; a stock lacking it may still qualify if other inputs compensate
Inputs: institutional share counts by quarter → 13F holdings (FMP / Financial Datasets institutional holdings); shares outstanding → 10-Q
Sources: [BOOK MoralesKacher loc.188] (agrees with O'Neil's 30–60%); [BOOK MoralesKacher loc.26] (institutions create base bottoms and drive big moves)
Evidence: D — second-hand from O'Neil; the authors' wish for 'A-rated' funds needs a fund-rating feed the desk lacks
Conflicts: none yet
Status: UNTESTED


### R-228 Graham two-stage value: buy only at or below the 7-year hurdle-rate price
School: value | Horizon: long-term (years) | Instrument: shares
IF normalised current EPS (see R-229) grown at a conservative 7-year rate g gives EPS7 = EPS0 × (1 + g)^7 AND the year-7 value FV7 = EPS7 × (8.5 + 2 × 7) = 22.5 × EPS7, plus net cash per share (minus net debt per share) AND the current price ≤ FV7 ÷ (1 + h)^7, where h is a fixed hurdle rate set once (the author uses 12%) and never moved with market conditions or a benchmark THEN the stock is a candidate long-term buy at a buyer's-advantage price; also compute today's value EPS0 × (8.5 + 2g) as a check that current operations are understood | EXIT consider trimming only when the price rises so far that the implied return from today's price to a refreshed FV7 falls well below h (the margin of safety is gone; see R-119) | INVALIDATED BY a cut to normalised EPS or growth that pushes the ceiling below the price, or being unable to estimate current operations with adequate precision (then pass)
Inputs: trailing EPS, revenue, operating margin, cash, debt, diluted shares → 10-K/10-Q via FMP statements or Financial Datasets; normalised EPS and g → [ESTIMATED] with assumptions shown (low end of a range, capped per R-229); h → a fixed desk parameter; price → daily close (FMP quote, Alpha Vantage GLOBAL_QUOTE); ceiling and implied 7-year return (FV7 ÷ price)^(1/7) − 1 computed in code
Sources: [BOOK Martin p.70–71] (formula EPS × (8.5 + 2g)); [BOOK Martin p.75–76] (normalised EPS, 7-year growth); [BOOK Martin p.78–79] (7% after year 7 → 22.5× year-7 EPS; the four steps); [BOOK Martin p.104–111] (hurdle-rate ceiling: FV7 $40 → $28.43 at 5%, $20.53 at 10%, $15.04 at 15%); [BOOK Martin p.141–143] (12% hurdle; buying below the ceiling adds margin); [BOOK Martin p.74] (add non-operating cash, subtract non-operating debt); [BOOK Martin p.218–219] (Apple 2001: FV7 $34.20 + $6 cash per share); [BOOK Martin p.96] (Graham's own 1962 formula); agrees: [BOOK Martin p.109]; [BOOK Martin p.143–144] (keep the hurdle fixed, never benchmark-relative)
Evidence: C — the author's firm's own cases told in hindsight, almost all winners: Apple 1998–2001 buys at $7.60–13.90 (expected 18–24% a year) [BOOK Martin p.211–219], Ralph Lauren 2008 (15.6%) [BOOK Martin p.225], Plexus 2002–2008 (16–30%) [BOOK Martin p.233–237], Middleby 2008–2010 (about 20%) [BOOK Martin p.241–242]; one loss shown, McLeodUSA bought at about half its computed value and sold at about $0.50 [BOOK Martin p.228–230]; no tally of all purchases; author claims double-digit long-run client returns [BOOK Martin p.12]; Graham's reprinted chapter cites studies where growth-stock selection only matched the market [BOOK Martin p.93–94]; the Appendix that p.73 says compares the formula with a DCF has no such comparison in the text
Conflicts: R-193 — decided by horizon: a 7-year forecast at a fixed hurdle (this rule) vs 2–3-year earnings power needing about 30% a year (R-193); each counts as one method in the desk's B3 two-method test; R-060 — compatible (the book's buys sat well below today's Graham value)
Status: UNTESTED

### R-229 Growth-input guardrails: normalise, cap at 20%, use the low end, fade to 7% after year 7
School: process | Horizon: long-term (years) | Instrument: shares
IF a growth rate enters any valuation (Graham formula, DCF, PEG) THEN: start from normalised EPS (raise it in a recession, industry slump or heavy-investment phase; lower it in a boom) and never treat a cyclical rebound off a trough as growth; cap near-term growth at 20% a year; estimate a range (e.g. 8–12% around 10%) and decide on its low end; fade growth to 7% or less after year 7 (no more than 22.5× year-7 EPS under the Graham formula); cross-check the year-7 revenue against a comparable company's historical path | EXIT n/a (an input rule) | INVALIDATED BY n/a
Inputs: EPS, revenue and margins for 5–10 years → 10-K via FMP or Financial Datasets (multi-year means computed in code); growth range → [ESTIMATED] with assumptions shown; comparable-company history → peer 10-Ks
Sources: [BOOK Martin p.75–76]; [BOOK Martin p.78] (use a range, never decide on its high end); [BOOK Martin p.137–138] (cap at 20%; above 10% is rare; normalise cyclical rebounds); [BOOK Martin p.140] (fade every company to 7% or less after seven years, no exceptions); [BOOK Martin p.95] (Graham capped 7-year growth at 20%); [BOOK Martin p.220] (Apple 2006 forecast checked against Sony 1990–95); [BOOK Martin p.40] (20% growth doubles a company every 3½ years)
Evidence: D — asserted; the author cites 'empirical work' and 'years of market experience' for the 7% fade without showing it [BOOK Martin p.78]
Conflicts: consistent with R-137 (DCF guardrails) and R-112 (normalised margins)
Status: UNTESTED

### R-230 Build a long-term position in thirds over up to two or three years
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF a stock first passes R-228 THEN buy about a third of the intended weight (the author: 1% toward a 3% position) and add the other thirds only on later price drops while the price is still at or below the hurdle-rate ceiling on a refreshed forecast AND management has met its stated milestones and kept its business model | EXIT the R-228 exit | INVALIDATED BY missed milestones or a cut forecast (stop adding and re-test the thesis, see R-199)
Inputs: position weights → Cyrus's position list; ceiling → R-228, computed in code; milestones → prior guidance vs 10-Q/8-K results
Sources: [BOOK Martin p.122–124] (three increments, up to three years, learn management in real time); [BOOK Martin p.286] (add on drops when milestones are met); agrees: [BOOK Martin p.215] (Apple: added after a 52% one-day fall in 2000); [BOOK Martin p.234] (Plexus: added 36% below the first buy in 2002); [BOOK Martin p.243] (Middleby: added at $29 after buying at $52); agrees: [BOOK Fisher loc.106–107] (new money after a long rise: start buying now and spread the rest over several years); [BOOK Fisher loc.244] (Part Three: a small first position while contact with management is slight)
Evidence: C — the author's firm practice and winner cases in hindsight; no tally of adds that kept falling (Apple later traded below every purchase until 2003 [BOOK Martin p.219])
Conflicts: R-022 — decided as R-083: add only with the forecast and milestones intact and the price under the ceiling; R-029 — decided by horizon: swing half-now/half-later (R-029) vs long-term thirds (this rule); total risk still fits the desk's C7 tiers
Status: UNTESTED

### R-231 Favour a high, sustained return on invested capital
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF ROIC = normalised after-tax operating earnings ÷ average invested capital (debt plus equity, non-operating items excluded) puts the company in the top fifth of its universe AND ROIC has held or risen over about five years while the company keeps reinvesting THEN favour it as a long-term candidate (price still decided by R-228 or the desk's B3) | EXIT n/a (a screen) | INVALIDATED BY ROIC falling materially over several years (the Adobe case: about 36% in 2005 to 12% in 2010)
Inputs: operating income, tax rate, debt, equity, cash → 10-K via FMP or Financial Datasets (ROIC computed in code); universe ranking → screener
Sources: [BOOK Martin p.176] (definition); [BOOK Martin p.178] (quintile sort); [BOOK Martin p.177] (compounding illustration: 7%, 15%, 25% ROIC); [BOOK Martin p.203–204] (Adobe); agrees: [BOOK Martin p.277] (growth investors prize return on capital over growth)
Evidence: B — the authors' own sort: median total return by ROIC quintile over 15 years to September 2010 of about 387%, 281%, 171% and 33% for the top four quintiles (quintile median ROIC about 25%, 16%, 11%, 7%); the bottom quintile's figure is garbled in the conversion (check table p.178); universe, sample size and method not shown; said to be a snapshot with other periods similar (not shown) [BOOK Martin p.178]
Conflicts: consistent with R-129 and R-100; R-258 — see Conflicts
Status: UNTESTED

### R-232 Capital-discipline flag: buybacks that only offset dilution, deals that drag ROIC down
School: value | Horizon: long-term (years) | Instrument: shares
IF over several years acquisitions plus buybacks absorb a large share of cumulative free cash flow AND the diluted share count has not fallen meaningfully (buybacks mostly offsetting option or deal issuance) OR ROIC has fallen materially over the same years THEN treat it as a stewardship failure: haircut the growth forecast or pass, even if revenue and EPS are growing | EXIT for a holding, re-test the thesis (R-199) | INVALIDATED BY management showing returns at or above its stated hurdle on those deals and buybacks
Inputs: acquisitions, repurchases, free cash flow → cash-flow statements in the 10-K (FMP statements, Financial Datasets); diluted share count → 10-K/10-Q; ROIC → computed in code; the share-of-FCF and ROIC-drop thresholds are test parameters
Sources: [BOOK Martin p.200–201] (buybacks must earn an adequate return; offsetting option dilution is a transfer to insiders; a shrinking count alone proves nothing); [BOOK Martin p.202] (EPS accretion is not a return test); [BOOK Martin p.203–204] (Adobe 2004–10: revenue +128%, normalised EPS +62%, stock −8%; $5.2bn of acquisitions and $6.8bn of buybacks; ROIC 36% → 12%); agrees: [BOOK Martin p.199] (most acquisitions destroy value; good ones are small, in the core, with a price cushion)
Evidence: C — one hindsight case plus assertion
Conflicts: R-106 — decided by share count: executed buybacks with a falling count → R-106; large buybacks with a flat count → this flag
Status: UNTESTED

### R-233 Stewardship screen from the proxy statement
School: value | Horizon: long-term (years) | Instrument: shares
IF the latest proxy shows shareholder-hostile structures (classified board, poison pill, dual-class voting, limits on calling meetings or acting by written consent) OR pay tilted to time-based options, high base salaries or executive-only perks instead of equity that vests on long-term fundamental targets (return on capital plus growth) THEN count it against the company and require a larger margin of safety, or pass; favour material insider ownership (the book's cases: executives required to hold a year's salary in stock; a CEO holding about 2.3%) | EXIT n/a (a screen) | INVALIDATED BY n/a
Inputs: governance provisions, pay mix, perquisites → DEF 14A proxy and 10-K via SEC filings (FMP secFilings, Financial Datasets get_filings); insider holdings → Financial Datasets get_insider_ownership
Sources: [BOOK Martin p.195–198] (alignment, perks, equity type, governance); [BOOK Martin p.231] (Plexus ownership requirement); [BOOK Martin p.240–241] (Middleby's CEO: ask whether management owns more than 1%; his own test, second-hand); agrees: [BOOK Fisher loc.80–81] (Point 15: options granted far beyond a fair reward, relatives on the payroll, related-party leases and broker arrangements; integrity is the one point that allows no exception)
Evidence: D — asserted, with cases
Conflicts: none yet
Status: UNTESTED

### R-234 Implied-volatility forecast: range extreme plus a gap to historical volatility, otherwise neutral
School: process | Horizon: swing (days–weeks) | Instrument: options
IF a stock's at-the-money implied volatility is in the top part of its own range over roughly the past 1–2 years AND sits above its 30-day historical volatility THEN forecast IV falling to at least mid-range (favour short-premium structures); IF IV is in the bottom part of its range AND below 30-day HV THEN forecast IV rising to at least mid-range (favour long-premium structures); the wider the IV–HV gap the stronger the call; any other state → IV neutral | EXIT when IV reaches mid-range (or the opposite end), re-forecast | INVALIDATED BY a structural change in the company (major merger, acquisition or divestiture) or options listed less than about a year ago — IV may trend instead of ranging; stand aside
Inputs: daily ATM IV and its 1–2-year high/low/mean → historical chains (Alpha Vantage HISTORICAL_OPTIONS) or pasted by Cyrus; 30-day HV → computed from daily closes (Alpha Vantage TIME_SERIES_DAILY); option listing date and M&A news → company filings/news. "Top/bottom part of the range" (e.g. top/bottom quintile) is a test parameter; the book gives none
Sources: [BOOK Smith p.80–82]; [BOOK Smith p.83]; [BOOK Smith p.84]
Evidence: C — one real case (IBM IV vs 30-day HV chart, about a year, read in hindsight; the author says the rules "would have created many profitable predictions") with no tally
Conflicts: none yet (refines R-209 with explicit conditions; see Merges)
Status: UNTESTED

### R-235 Fade a market-wide IV spike when the company itself has not changed
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a stock's IV breaks above its normal range during a market-wide volatility event AND there is no company-specific news or structural change THEN open a short-IV position (the book: short straddle or other short-premium structure), expecting IV to return inside the range | EXIT when IV is back inside its normal range (mid-range target per R-234) | INVALIDATED BY company-specific news, a merger/acquisition/divestiture, or IV continuing to trend higher (range broken for structural reasons)
Inputs: stock IV and its range → historical chains (Alpha Vantage HISTORICAL_OPTIONS); market-wide event → VIX daily close (Cboe/Alpha Vantage) and index-wide IV; company news → news feed / filings
Sources: [BOOK Smith p.83]
Evidence: C — one case (IBM IV peaked near 28.5% in Aug 2007 credit-crunch selling with no IBM news); the author calls the reversion a near certainty with no tally
Conflicts: R-073 — decided by structure and the desk test: index or index-weighted credit spreads while VIX > 30 → R-073 (B evidence) governs; single-stock, defined-risk short-IV with no company news → R-235, paper only until tested
Status: UNTESTED

### R-236 Direction view × IV view picks the structure
School: process | Horizon: swing (days–weeks) | Instrument: options
IF price view higher AND IV view higher THEN buy a call or a bull spread; IF higher AND IV lower THEN sell a put or write a covered call; IF lower AND IV higher THEN buy a put or a bear spread; IF lower AND IV lower THEN sell a call or write a covered put; IF stable AND IV lower THEN sell a straddle/strangle or ratio write; IF a big move of unknown direction AND IV higher THEN buy a straddle; IV neutral → either side | EXIT n/a (structure selection; then follow the chosen strategy's rules) | INVALIDATED BY no price view (the book starts every trade from the price view)
Inputs: price view → the share rule or thesis that triggered it; IV view → R-234; time-decay sign → options chain greeks (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK Smith p.84]; [BOOK Smith p.89–90]; [BOOK Smith p.100]; [BOOK Smith p.101]
Evidence: D — strategy table and one IBM worked example at a single date, no outcomes (the butterfly rows of Fig. 6.8 contradict Ch.17 and are not carried)
Conflicts: none yet
Status: UNTESTED

### R-237 Long-option expiry from the timing and IV views
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF buying a call or put AND the move is expected imminently OR IV is expected to fall THEN buy the nearby expiry (higher gamma, lower vega); IF the timing is uncertain OR IV is expected to rise THEN buy a farther expiry (more vega, lower decay per day) and plan to sell before decay accelerates | EXIT sell before the final weeks of fast decay; roll forward if the view still holds near expiry | INVALIDATED BY poor liquidity in the far month (avoid it unless holding to expiry)
Inputs: expected move timing → the trade plan; IV view → R-234; expiries, vega, theta, volume/open interest → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus)
Sources: [BOOK Smith p.106–107]; [BOOK Smith p.118–119]
Evidence: D — asserted
Conflicts: R-046 and R-071 (30+ days) — decided by expected timing: move expected within days → nearby allowed if it passes the desk's C4 move check; otherwise 30+ days per R-046/R-071
Status: UNTESTED

### R-238 Long-option strike from a target price and a loss budget
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF buying an option for direction THEN first set a target price for the move and the dollar loss you accept, then compute each candidate strike's payoff at the target for the quantity the budget buys and take the best; as a guide: very strong view → out of the money, moderate view → in the money, quick move expected → at or slightly in the money; never pick out-of-the-money because it is cheap | EXIT at the target or when the view changes (see R-241, R-242) | INVALIDATED BY no target price (don't trade)
Inputs: target and loss budget → the trade plan; strikes, premiums, deltas → options chain snapshot; payoff at target computed in code
Sources: [BOOK Smith p.107–108]; [BOOK Smith p.119–120]
Evidence: D — one hypothetical $2,000-budget example
Conflicts: R-034 — decided by the desk's C4 move check: an out-of-the-money strike is allowed only when its breakeven still sits inside the typical move; otherwise R-034's at/in-the-money choice
Status: UNTESTED

### R-239 Rank candidate options by repricing after a one-implied-move rise and fall
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF choosing among options on several stocks for the same directional view THEN pick a horizon, reprice each option (pricing model) after the stock moves up and after it moves down by one implied-volatility standard deviation over that horizon, compute (price after the favourable move) ÷ (price after the adverse move), and prefer the highest ratios | EXIT n/a (ranking) | INVALIDATED BY n/a
Inputs: price, IV, strike, expiry, rate → options chain snapshot (Alpha Vantage REALTIME_OPTIONS or pasted by Cyrus) and Black-Scholes in code; horizon → the trade plan
Sources: [BOOK Smith p.109–110]; [BOOK Smith p.121–122]
Evidence: D — asserted method, no example output
Conflicts: none yet
Status: UNTESTED

### R-240 Short-option strike beyond one implied move
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF selling a call (or put) for premium THEN choose a strike beyond the price ± one implied-volatility move to expiry (price × IV × √(days/365)); conservative: about twice that distance; prefer options whose IV is high against its own record, with expiry inside about six weeks when decay accelerates | EXIT see R-234 (IV back to mid-range) and the desk's buy-back rules; roll or close if price approaches the strike | INVALIDATED BY IV low against its own record (selling underpriced options)
Inputs: price → daily quote; IV, strikes, expiry → options chain snapshot; IV history → Alpha Vantage HISTORICAL_OPTIONS; implied move computed in code
Sources: [BOOK Smith p.130–131]; [BOOK Smith p.166–167]
Evidence: D — one Swiss-franc worked example (61.00 ± 1.83 → 63 call); naked writing; the put version mislabels the strike a call (p.167)
Conflicts: none yet (consistent with the delta ≈ 0.16 principle; naked calls remain subject to the desk's gates)
Status: UNTESTED

### R-241 Losing long call or put: repair into a vertical at about even money
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a long call has lost value because the stock fell AND you are still bullish THEN sell two of the held calls and buy one call at the next lower strike for about the same total premium (net cost near zero), turning it into a bull call spread with a lower breakeven (mirror for puts: sell two, buy one higher strike); if now bearish, liquidate; if little premium is left, simply hold | EXIT per the vertical-spread rules (R-245) | INVALIDATED BY the new spread failing the entry tests for a new bull/bear spread
Inputs: held option, strikes, bid/ask → options chain snapshot; current view → the trade plan
Sources: [BOOK Smith p.110–111]; [BOOK Smith p.122–123]
Evidence: D — one hypothetical OEX example
Conflicts: none yet
Status: UNTESTED

### R-242 Winning long option: take the stake out or sell the next strike
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a long call has gained (stock up) AND you are still bullish THEN either sell the call and buy a higher strike using only the profit (original stake withdrawn), or sell a higher-strike call against it (bull spread, locking in a gain; preferred when IV is expected to fall); if now bearish, take the profit; near expiry, roll forward rather than exercise | EXIT at the target or the spread's maximum | INVALIDATED BY n/a
Inputs: entry cost, current premiums, strikes → options chain snapshot; IV view → R-234
Sources: [BOOK Smith p.112–113]; [BOOK Smith p.124–125]
Evidence: D — hypothetical OEX examples (put version mislabels puts as calls, p.125)
Conflicts: none yet (cf. R-041 trailing stop — compatible alternatives)
Status: UNTESTED

### R-243 Covered write defence at the breakeven: roll down or exit, planned before entry
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF a covered call's stock falls to the position's breakeven (entry price − premium) OR to a support level or money-management point set before entry THEN if now bearish close the whole position; if still bullish buy back the call and sell a lower strike (or part of the position, or lower and farther out) for added credit, accepting a lower maximum gain | EXIT when the rolled position cannot add protection without locking in a loss you would not accept | INVALIDATED BY no rolling plan written before the original write
Inputs: entry price, premium → trade record; support → daily OHLC; strikes, bid/ask → options chain snapshot
Sources: [BOOK Smith p.146–148]; [BOOK Smith p.182] (covered-put mirror)
Evidence: D — one hypothetical Widget-futures example (190 long, 180 call → 160 call)
Conflicts: R-143 — decided by why the shares are held: shares owned for their own case → R-143 forbids a strike below cost basis; a buy-write held for the trade → R-243
Status: UNTESTED

### R-244 Pick vertical spreads by probability-weighted reward to risk
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF choosing a bull or bear spread on a stock THEN list every candidate's maximum profit ÷ maximum risk, weight each by its probability of reaching maximum profit from IV (or your own volatility estimate), and take the highest expected value after commissions; prefer the call version for bull spreads where puts are illiquid or the short leg is in the money (early exercise) | EXIT per R-245 | INVALIDATED BY commissions large against the maximum profit
Inputs: strikes, premiums, IV, open interest → options chain snapshot; probabilities computed in code (lognormal with IV)
Sources: [BOOK Smith p.199–200]; [BOOK Smith p.213–214]
Evidence: D — asserted
Conflicts: none yet
Status: UNTESTED

### R-245 Vertical-spread follow-up: roll winners when the new risk is below the banked profit; don't roll losers
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF a vertical spread has moved in your favour AND the view still holds THEN close it and open the next spread further out only if the new spread's maximum loss is less than the profit just banked (a locked-in gain); IF the spread is at maximum profit and the view is now neutral THEN close it; IF the spread is losing THEN don't roll it toward the price (the new spread's potential is cut by the realised loss) — hold if at maximum loss, or close | EXIT as stated | INVALIDATED BY n/a
Inputs: spread prices, strikes → options chain snapshot; realised P&L → trade record
Sources: [BOOK Smith p.202]; [BOOK Smith p.205–206]; [BOOK Smith p.216–218]
Evidence: D — hypothetical MMI tables
Conflicts: none yet
Status: UNTESTED

### R-246 Long butterfly only when the debit is under 10% of the strike interval
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the stock is expected to stay still AND a long butterfly (buy 1 low, sell 2 middle, buy 1 high, equal intervals) with the middle strike at the money costs less than 10% of the interval between adjacent strikes (e.g. under 0.50 on 5-point strikes) AND the outer strikes lie beyond the stock's expected range for the holding period THEN buy it | EXIT near the middle strike at expiry; if the view changes, convert to a vertical or roll the middle strike to the new price | INVALIDATED BY the debit at or above 10% of the interval
Inputs: strikes, bid/ask → options chain snapshot; expected range → IV-implied move computed in code
Sources: [BOOK Smith p.225]; [BOOK Smith p.226–233]
Evidence: D — rule of thumb, hypothetical OEX tables
Conflicts: none yet
Status: UNTESTED

### R-247 Calendar spread: sell the rich near month as its decay accelerates
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF the near-month option's IV is above the far month's AND the near option is entering its fast-decay period THEN sell the near option and buy the same strike in the next expiry; neutral → at-the-money strike; bullish/bearish → strike at the price objective; use the two nearest expiries for liquidity | EXIT close if price moves beyond the estimated breakeven at the near expiry and is expected to stay there; otherwise re-centre the strikes | INVALIDATED BY a sharp move through the strike before the near expiry (near-leg gamma)
Inputs: near/far IV, premiums, theta → options chain snapshot; price objective → the trade plan
Sources: [BOOK Smith p.237–238]; [BOOK Smith p.240]; [BOOK Smith p.241–243]
Evidence: D — asserted (the text says "sell a far contract" where buying is meant, p.240)
Conflicts: none yet
Status: UNTESTED

### R-248 Long straddle: your expected range beats the implied range, IV at the low end
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF your expected price range to expiry is wider than the IV-implied range AND IV is at the low end of its own range (R-234) THEN buy an at-the-money straddle, preferring long-dated options (more vega, less daily decay); for a specific news catalyst only, use the highest-gamma near expiry and hold a few days | EXIT when the expected move or IV rise has happened; if you now expect stable prices, close (the premise is gone) | INVALIDATED BY IV in the middle or high end of its range, or a pre-announcement IV run-up (straddles often drop after the report)
Inputs: expected range → the trade plan; IV, implied move, strikes → options chain snapshot; IV history → Alpha Vantage HISTORICAL_OPTIONS; event dates → earnings calendar
Sources: [BOOK Smith p.264–266]; [BOOK Smith p.268]; [BOOK Smith p.271]
Evidence: C — one real IV-vs-actual-volatility chart (nearest T-bond futures option, about two years) plus a hypothetical earnings example
Conflicts: none yet (agrees with R-209: buy only when a move is expected)
Status: UNTESTED

### R-249 Delta-neutral far-dated straddle to trade the IV forecast
School: options-income | Horizon: position (months) | Instrument: options
IF R-234 forecasts IV rising THEN buy an at-the-money straddle in a far expiry; IF it forecasts IV falling (and no price move expected) THEN sell it; keep the position delta neutral with the stock, and roll to a farther expiry when theta and gamma become noticeable; if the stock moves away, re-centre strikes or add straddles at the new at-the-money strike | EXIT when IV reaches the R-234 target | INVALIDATED BY the R-234 invalidations
Inputs: IV forecast → R-234; delta, gamma, theta, vega → options chain snapshot; stock hedge → daily quote
Sources: [BOOK Smith p.266]; [BOOK Smith p.277–278]; [BOOK Smith p.84]
Evidence: D — asserted
Conflicts: none yet (short straddles carry unlimited risk; subject to the desk's gates)
Status: UNTESTED

### R-250 Ratio spread: buy intrinsic, sell time, in the delta ratio
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF expecting prices to stay between two strikes THEN buy deep in-the-money options and sell at- or slightly out-of-the-money options in the ratio of their deltas (e.g. 0.69 ÷ 0.46 ≈ 1.5 short per long), preferably for a credit (no risk on the long side); re-hedge whenever the net delta shifts by one contract and roll the short strike to the new at-the-money as price moves | EXIT close or convert to a vertical if price heads through the upside breakeven (high strike + max profit ÷ naked contracts) | INVALIDATED BY a small position that can't be adjusted in whole contracts
Inputs: strikes, deltas, premiums → options chain snapshot; breakeven computed in code
Sources: [BOOK Smith p.245–246]; [BOOK Smith p.248–250]
Evidence: D — hypothetical S&P 500 futures-options example
Conflicts: none yet
Status: UNTESTED

### R-251 Covered call as a pre-sale at the target price; roll up only for a credit
School: options-income | Horizon: position (months) | Instrument: options
IF you own shares with a set sell target AND the call struck at that target pays a worthwhile premium (the book: more than about $50 a contract) THEN write it, pre-selling at the target; IF that premium is too small THEN write near the current price and roll up as the stock climbs, only for a net credit, until the target strike is reached | EXIT assignment at the target | INVALIDATED BY a long-term bearish view on the shares (sell them instead)
Inputs: sell target → the valuation or trade plan; strikes, premiums → options chain snapshot; share position → Cyrus's records
Sources: [BOOK Smith p.144–145]; [BOOK Smith p.180] (covered-put mirror)
Evidence: D — asserted
Conflicts: none yet (complements R-143)
Status: UNTESTED

### R-252 Rank covered writes: minimum protection first, then profit ÷ protection weighted by probability
School: options-income | Horizon: swing (days–weeks) | Instrument: options
IF choosing among covered writes THEN drop those below your minimum downside protection (premium ÷ stock price), rank the rest by potential profit ÷ downside protection and by return-if-unchanged, and weight by the IV-implied chance of each outcome; compare annualised returns only between similar writes | EXIT n/a (ranking) | INVALIDATED BY n/a
Inputs: price, strikes, premiums, IV, expiry → options chain snapshot; minimum protection → Cyrus's setting; returns computed in code
Sources: [BOOK Smith p.140–141]; [BOOK Smith p.145–146]; [BOOK Smith p.181]
Evidence: D — hypothetical Widget arithmetic
Conflicts: none yet
Status: UNTESTED

### R-253 Moderately bullish: bull spread instead of a long call
School: options-directional | Horizon: swing (days–weeks) | Instrument: options
IF your target price sits at or below the bull spread's upper strike (a moderate rise) THEN buy the bull spread rather than the call — for the same money it pays more unless the stock rises well beyond the upper strike (mirror: bear spread instead of a put when moderately bearish) | EXIT per R-245 | INVALIDATED BY a target well above the upper strike (buy the call per R-238)
Inputs: target → the trade plan; strikes, premiums → options chain snapshot; payoff comparison computed in code
Sources: [BOOK Smith p.195–198]; [BOOK Smith p.209–212]
Evidence: D — hypothetical MMI tables (about three spreads for the cost of one call)
Conflicts: none yet (cf. R-035, which uses a slowing uptrend as the trigger)
Status: UNTESTED

### R-254 Cycle-peak EPS test: hold or sell a growth holding
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a holding's expected per-share EPS at the next business-cycle peak (adjusted for splits and stock dividends, not for shares issued to raise capital) will not be up from today's EPS by at least as much as today's EPS is up from EPS at the last cycle peak, OR multi-year sales and EPS growth has slowed to about the economy's rate with no new product line in sight THEN sell; otherwise hold | EXIT the rule is the exit; when the cause is an exhausted market rather than weaker management, sell gradually (part can wait for a replacement), and capital-gains tax should not block the sale | INVALIDATED BY today's EPS sitting at a cyclical trough (use R-112 instead)
Inputs: EPS history → 10-K/10-Q; last cycle-peak year → NBER business-cycle dates; forward EPS → desk forecast or consensus; split and stock-dividend factors → price data; nominal GDP growth → BEA/FRED
Sources: [BOOK Fisher loc.111] (Part One); [BOOK Fisher loc.110] (Part One); agrees: [BOOK Fisher loc.260] (Part Three, point 3: hold until growth no longer beats the economy)
Evidence: D — the book states the test with no cases or tally
Conflicts: none yet (related R-188, which covers flat earnings)
Status: UNTESTED

### R-255 No promotional companies: 2–3 years of commercial sales and a year of operating profit first
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company has fewer than about 2–3 years of commercial operations OR has not yet reported one full year of operating profit THEN don't buy it; leave such financing to venture groups that can supply management | EXIT n/a (a filter) | INVALIDATED BY n/a
Inputs: first year of commercial revenue → S-1/10-K business history; operating income by fiscal year → 10-K
Sources: [BOOK Fisher loc.126–127] (Part One)
Evidence: D — reasoned argument with no cases
Conflicts: R-127 — decided by sleeve (see Conflicts); complementary with R-107 (listing age, not operating history)
Status: UNTESTED

### R-256 Outside CEO at a large company: no new buying, re-underwrite the holding
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a large, established company names a chief executive recruited from outside THEN read it as a sign that something was badly wrong with the existing management, whatever recent earnings show: make no new purchases, re-run the full quality review on a holding (and check what in your own process missed it) | EXIT sell at once, whatever the market outlook or the tax, if the review confirms management has deteriorated | INVALIDATED BY a later record of the new chief building an internal team (the stock can qualify again)
Inputs: CEO appointment and prior employer → 8-K Item 5.02, proxy biographies (DEF 14A)
Sources: [BOOK Fisher loc.184] (Part Two); [BOOK Fisher loc.262] (Part Three appendix: outside CEO recruitment is a dangerous sign); [BOOK Fisher loc.110] (Part One: sell at once on management deterioration)
Evidence: D — author's observation; the claim that senior outside hires often leave within a few years comes with no statistics (loc.184)
Conflicts: R-131 and R-198 — decided by school and starting point (see Conflicts)
Status: UNTESTED

### R-257 CEO pay far above the next executives: one-man-management flag
School: process | Horizon: long-term (years) | Instrument: shares
IF the proxy's summary compensation table shows the top executive paid very much more than each of the next two or three THEN flag one-man management (depth and succession risk, counted against Points 8–9 and R-233); pay that steps down gradually is no flag | EXIT n/a (a flag) | INVALIDATED BY n/a. The book gives no ratio; the desk sets one as a test parameter (e.g. CEO pay at least 2× the next highest)
Inputs: named-executive total pay → DEF 14A summary compensation table
Sources: [BOOK Fisher loc.185] (Part Two)
Evidence: D — the book offers it as a clue, untested; it says the flag tells nothing about how good the team is
Conflicts: none yet (complementary with R-233)
Status: UNTESTED

### R-258 Operating-margin leader by a modest, lasting gap
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF operating margin measured over a run of years (not one year) is at or near the top of the company's industry AND it leads the next-best competitor by a modest margin (the book: 2–3 points of sales is enough; a margin many times the industry's invites entry) THEN favour the company as a long-term candidate; IF it is one of the lowest-margin (marginal) firms in its industry THEN don't hold it long-term | EXIT the margin lead is lost over several years | INVALIDATED BY a low margin deliberately caused by R&D and promotion well beyond what normal growth needs (R&D ÷ sales and selling ÷ sales clearly above peers, gross margin at or above peers), or margins improving through a real internal change (efficiency, new products) and not only through volume; those cases may still qualify
Inputs: operating margin for 5+ years, company and peers → 10-K; R&D ÷ sales, SG&A ÷ sales, gross margin → 10-K
Sources: [BOOK Fisher loc.66–67] (Part One); [BOOK Fisher loc.199] (Part Two); [BOOK Fisher loc.193] (Part Two: for safety, use margin on sales; a 2% cost rise wipes out a 1% margin but only a fifth of a 10% margin); agrees: [BOOK Fisher loc.178] (Part Two: low-cost producer)
Evidence: D — author asserts most big gains in older companies came from broad-margin firms; no tally
Conflicts: R-231 — decided by purpose (see Conflicts)
Status: UNTESTED

### R-259 Debottlenecking: small added capital, large added output, before earnings show it
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company whose plants are already profitable and fully running commits roughly 15% of their cost to raise output by roughly 40% with little added overhead AND the project is big enough to move company EPS AND the share price has not yet moved on it THEN buy before the extra output reaches reported earnings | EXIT the desk's long-term sell rules (R-254, R-262) | INVALIDATED BY demand not absorbing the added output (utilisation or selling prices falling)
Inputs: capex plan and capacity figures → 10-K, 8-K, investor presentations; utilisation → filings, industry data; price reaction since the announcement → price data
Sources: [BOOK Fisher loc.104] (Part One; capital-intensive chemical example)
Evidence: D — hypothetical arithmetic, no case
Conflicts: none yet (related R-204: an earnings rise not yet in the price)
Status: UNTESTED

### R-260 War scare: buy slowly on the threat, faster on the outbreak
School: process | Horizon: long-term (years) | Instrument: shares
IF you had already decided to buy a stock AND a war scare knocks its price down THEN start buying, slowly and on a scale-down; IF fighting actually breaks out (US forces engaged) THEN buy noticeably faster; buy only companies whose demand holds in wartime or that can convert to war work | EXIT the desk's long-term sell rules | INVALIDATED BY a war the country could lose (the book: money and stocks would both lose their value)
Inputs: price → market data; dates of the scare and of the outbreak → news wires
Sources: [BOOK Fisher loc.146–148] (Part One); agrees: [BOOK Fisher loc.11] (Ken Fisher's introduction: his late-1990 buy columns during the Gulf war scare); agrees: [BOOK Wyckoff p.78] (prices more often bottom on the threat than on the event)
Evidence: C — author's survey of 20th-century wars (WWI, WWII, Korea) and about ten scares in 22 years, with no data table; Ken Fisher's own 1990 call
Conflicts: R-050 — decided by level and horizon (see Conflicts)
Status: UNTESTED

### R-261 Three-year rule for a conviction holding
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF a holding bought on a fundamental thesis has not produced worthwhile results (total return at or below the market's) three years after purchase AND nothing learned since has changed the original view THEN sell it; before three years, lagging the market is no reason to sell | EXIT the rule is the exit | INVALIDATED BY the author's one exception: a candid management whose profits are depressed by a specific, identified spending programme that is being corrected (then hold or add)
Inputs: purchase date and total return vs S&P 500 → desk ledger, price data
Sources: [BOOK Fisher loc.232] (Part Three); [BOOK Fisher loc.233–234] (Motorola 1955: 5–10% below cost for over a year, then led the insurer's whole portfolio within three years); [BOOK Fisher loc.234–235] (Rogers: the one exception)
Evidence: C — author's own practice; the author says he can recall no sale made only under this rule that he later regretted (loc.234)
Conflicts: R-102 — decided by method (see Conflicts)
Status: UNTESTED

### R-262 Hold a qualifying compounder through a high multiple or a feared bear market
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a holding still passes the quality review (fifteen points; management and growth intact) AND its P/E has run above its usual level (the book's example: 35× against a normal 25×) or a market decline is expected THEN hold; don't sell on the multiple, on a market forecast or because it has already risen a lot; IF the multiple is above what even strong fundamentals justify THEN keep it but put no new money in | EXIT only for the fundamental reasons: a mistaken thesis, deterioration (R-256), growth exhaustion (R-254) or a clear-cut better switch (R-271) | INVALIDATED BY earnings stalling or an operating crack at the high multiple (→ R-187)
Inputs: P/E and its 5–10-year range → price data, 10-K EPS; quality review → desk checklist
Sources: [BOOK Fisher loc.112–117] (Part One); [BOOK Fisher loc.202–203] (Part Two: the risk ladder; legendary quality at too high a P/E = hold, no fresh buying); [BOOK Fisher loc.246–249] (Part Three: Texas Instruments fell 80% from its 1962 peak, then traded at more than double that peak; a client who sold in 1956 at a 125% gain saw the stock's 1960s low still almost 40% above his sale price)
Evidence: C — author's own cases; author claims that fewer than one in ten investors who sold ahead of a bear market got back in lower (loc.113)
Conflicts: R-187; R-119; R-061 — see Conflicts
Status: UNTESTED

### R-263 Position caps at cost by company risk class
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF building a long-term portfolio THEN cap each position at original cost by class: large, entrenched growth companies at most 20% each (so at least five names) with little product overlap between them; mid-sized established companies with team management (the book: $15–100 million of sales in 1959 dollars; rescale) 8–10% each, 8% for the riskier; small young companies at most 5% each, and only with money you can afford to lose. An individual holding more than about 20 names has too many (10–12 is usually better). Don't trim a holding because growth has raised its weight (the book: 40% after ten years is acceptable while the outlook holds; a small company that matures into the mid class can be held larger) | EXIT n/a (a sizing rule) | INVALIDATED BY n/a
Inputs: cost basis → desk ledger; revenue and market cap class → 10-K, price data; industry and product overlap → SIC/GICS codes, 10-K segment data
Sources: [BOOK Fisher loc.138–139] (Part One); [BOOK Fisher loc.144–146] (Part One); [BOOK Fisher loc.88] (Part One: example of up to 15% of a fortune in small young companies, or new savings only); [BOOK Fisher loc.260] (Part Three, point 6: more than 20 holdings shows incompetence; companies under $25 million of sales need wider diversification)
Evidence: D — guidance with no test
Conflicts: R-139; R-200; R-175 — see Conflicts
Status: UNTESTED

### R-264 Long-term buys at the market; give block buys a price range
School: process | Horizon: long-term (years) | Instrument: shares
IF a stock has passed the long-term buy work AND the order is small next to normal trading THEN buy at the market rather than holding out for a fraction of a point; IF the order is a large block THEN give the broker the full size and discretion up to an agreed amount above the last sale, passing up small offerings that would draw competing bids | EXIT n/a | INVALIDATED BY n/a
Inputs: order size vs average daily volume → market data
Sources: [BOOK Fisher loc.135–137] (Part One: an investor held out for half a point and missed a stock that later sold above 500); [BOOK Fisher loc.237–238] (Part Three: a client's limit 3/4 point below the close missed a rise of over 50%; the author's own limit sell missed by a quarter point)
Evidence: C — anecdotes from the author and his clients
Conflicts: principle "Enter with limit orders…" [BOOK MetaStock p.10] and R-023 — decided by horizon (see Conflicts)
Status: UNTESTED

### R-265 Value a long-run compounder at its own normal multiple of the market's P/E
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company has sold for many years at a steady multiple of the market's P/E (the book's case: about twice the Dow's for decades) AND the new-product flow that earned the premium is still visible THEN project its future price at that same relative P/E: twice the market's P/E with earnings doubling in five years is not discounting five years ahead; IF the coming earnings spurt is a one-time event THEN assume the relative P/E falls back to the market's | EXIT n/a (a valuation input) | INVALIDATED BY the new-product flow ending (then use the market's multiple)
Inputs: company P/E and index P/E over 10+ years → price data, EPS history; product pipeline → 10-K, R&D disclosures
Sources: [BOOK Fisher loc.133–135] (Part One); [BOOK Fisher loc.155] (Part One: past P/E is the base, but a company moving up a class can go from 8× to 15×); [BOOK Fisher loc.210] (Part Two: the further ahead profits keep growing, the higher the P/E an investor can afford)
Evidence: D — a worked fictitious example
Conflicts: none yet (complementary with R-184's own-history band)
Status: UNTESTED

### R-266 Disclosure retreat after bad news: exclude
School: process | Horizon: long-term (years) | Instrument: shares
IF after a disappointment the company discloses less than it did in good times (drops guidance or segment detail it used to give, files late with an NT 10-K/10-Q, or its annual report leaves out matters of real significance) THEN exclude it from new buying and count a holding as failing Point 14 | EXIT for a holding, re-run the integrity and thesis review | INVALIDATED BY a prompt, full account of the problem and the plan to fix it (the book's positive case is the Rogers president who reported repeated bad news openly)
Inputs: NT 10-K/10-Q filings → SEC EDGAR; segment notes and guidance history → 10-K, 10-Q, earnings releases
Sources: [BOOK Fisher loc.80] (Part One, Point 14); [BOOK Fisher loc.133] (Part One: reports that omit significant matters); [BOOK Fisher loc.234] (Part Three)
Evidence: D — assertion
Conflicts: none yet
Status: UNTESTED

### R-267 Capital-growth sleeve: low or no payout where reinvestment is rich
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF the goal is capital growth AND a company pays out a high share of earnings while it has high-return uses for the money (payout stressed so much it limits growth) THEN don't buy it; favour low- or no-payout companies; a maturing grower paying about 25–40% of earnings on a steady, announced policy is acceptable; one-off extra dividends count for nothing | EXIT n/a (a screen) | INVALIDATED BY retained earnings earning subnormal returns or piling up as idle cash (then retention adds nothing; see R-113)
Inputs: payout ratio → 10-K; ROIC or return on retained earnings → 10-K; cash vs needs → balance sheet
Sources: [BOOK Fisher loc.120–125] (Part One); [BOOK Fisher loc.118] (Part One); [BOOK Fisher loc.250–251] (Part Three)
Evidence: D — the author says every study he has seen found high-yield stocks did worse on price, but names none (loc.90, loc.122)
Conflicts: R-177 — decided by goal and reinvestment returns (see Conflicts)
Status: UNTESTED

### R-268 Prefer the clear profit leader to the number two or three
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF one company clearly leads its field in both sales and profitability AND its management stays competent THEN prefer it to the number two or three; don't buy a follower on the theory that it can catch up | EXIT leadership lost (share and margin rank falling) | INVALIDATED BY a field with no clear leader
Inputs: market share and margin rank → 10-K, industry data
Sources: [BOOK Fisher loc.195] (Part Two: GE vs Westinghouse, Sears vs Montgomery Ward, IBM in computers); [BOOK Fisher loc.196] (Part Two: pharmaceutical saying, first entrant about 60% of the market, second about 25%, next three 10–15%)
Evidence: C — author's observed cases; the pharmaceutical split is an industry saying with no data
Conflicts: none yet
Status: UNTESTED

### R-269 Industry margins widening only on price rises: no long-term buy
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF an industry's margins are widening mainly because selling prices keep rising (strong demand, costs passed on) AND new competing capacity is being announced THEN don't buy its companies as long-term holdings; expect margins to shrink as that capacity arrives | EXIT a holding bought for margin expansion once the capacity starts up | INVALIDATED BY a company that is widening margins through cost cutting (new equipment, methods, logistics, branch plants), which is the book's preferred case
Inputs: product prices → BLS PPI, commodity price series; industry margins → peer 10-Ks; capacity announcements → 8-Ks, industry data
Sources: [BOOK Fisher loc.68–69] (Part One: aluminum moved from shortage to aggressive selling within weeks in fall 1956; copper 1956–57)
Evidence: C — two industry cases from 1956–57
Conflicts: none yet (complementary with R-196)
Status: UNTESTED

### R-270 Research productivity: share of sales from new products
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company reports the share of sales coming from products launched in the last few years AND that share is high or rising against peers THEN credit its research (Point 3); IF R&D ÷ sales is well above peers while the new-product share stays low THEN flag research that isn't productive. Book benchmarks: a 1957 survey expected about 10% of 1960 manufacturing sales from products less than three years old; Ampex had 80% of sales from products that did not exist four years earlier | EXIT n/a | INVALIDATED BY inconsistent R&D accounting (sales engineering booked as R&D, pilot plants charged to production); compare like with like (see R-136)
Inputs: new-product share of sales → 10-K, investor presentations; R&D ÷ sales → 10-K
Sources: [BOOK Fisher loc.43] (Part One: McGraw-Hill / Business Week surveys, 1956–57); [BOOK Fisher loc.59–60]; [BOOK Fisher loc.64]; [BOOK Fisher loc.144]
Evidence: D — the benchmark comes from outside surveys, but the rule itself is untested
Conflicts: none yet (complementary with R-100's R&D ÷ assets test)
Status: UNTESTED

### R-271 Switch only for clearly faster growth
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a new candidate passes the same quality work AND its well-evidenced long-run EPS growth is clearly above the holding's (the book: 20% against 12% a year) THEN switch, even after capital-gains tax; if the evidence isn't clear-cut, keep the holding you know | EXIT n/a | INVALIDATED BY doubtful evidence on the new company (the book warns that a holding you know well has fewer surprises)
Inputs: long-run EPS growth estimates → desk forecast, consensus; tax lots → desk ledger
Sources: [BOOK Fisher loc.111–112] (Part One); [BOOK Fisher loc.97] (Part One: American Cyanamid sold in 1959 at about +110% for a better-looking company; the author later questioned the sale); agrees: [BOOK Fisher loc.260] (Part Three: as holdings near 20, switch the least attractive into more of the best); agrees: [BOOK Wyckoff p.81–82]
Evidence: C — author's own switch, with its doubtful result reported
Conflicts: none yet
Status: UNTESTED

### R-272 Industry-specific cost ratio as a check on management (Point 11)
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF the industry has a cost line that decides margins (retail leases: occupancy cost ÷ sales; lending: credit losses ÷ loans; insurance-heavy operations: insurance cost ÷ sales) THEN compare it with peers of similar size and count a clearly better ratio as evidence of overall management skill (the book: insurance costs 35% below a same-size rival can widen the margin) | EXIT n/a (supporting evidence) | INVALIDATED BY n/a
Inputs: occupancy or lease cost, net charge-offs, insurance expense → 10-K, bank call reports
Sources: [BOOK Fisher loc.75] (Part One)
Evidence: D — assertion
Conflicts: none yet
Status: UNTESTED

## Conflicts
_(pairs of rules that disagree, and the condition that decides between them)_
- R-005 Breakout-retest vs R-007 Range trading — decided by regime: a close outside the range on rising volume → R-005; repeated rejections inside the range with falling volume → R-007 [BOOK Pansheriya loc.16]; [BOOK Pansheriya loc.19]
- R-005 Breakout-retest vs R-006 Failed-breakout fade — decided by whether the breakout close holds beyond the level (→ R-005) or price closes back inside the range (→ R-006) [BOOK Pansheriya loc.14–15]
- R-013 Keltner close-outside (follow the break) vs R-016 EMA(5) channel (fade the break) — decided by the next candle: follow-through outside the band → R-013; a close back inside → R-016; also H1 vs H4 [BOOK Salvon loc.14]; [BOOK Salvon loc.18]
- R-027 Exit-in-a-day liquidity vs R-021 Penny-stock holding limit — decided by strategy: short-hold penny-stock trading (R-021) vs liquid names only (R-027); for position and long-term calls R-027 wins [BOOK MetaStock p.6]; [BOOK Regan loc.12]
- R-029 Half now vs R-023 Don't chase — decided by reward-to-risk at the current price: at least 3 → R-029; below 3 → R-023 [BOOK MetaStock p.12]; [BOOK Regan loc.25]
- R-035 Bull call spread and R-036 Bull put spread vs R-010 Minimum reward-to-risk of 2 — decided by instrument: R-010 is written for stop-based share trades; defined-risk spreads are judged on max gain ÷ max loss plus the desk's C4–C5 gates, and the book calls a near-the-money debit spread about 1:1 [BOOK Cayman loc.24]; [BOOK Pansheriya loc.20]
- R-040 3–5% allocation vs R-009 Per-trade risk cap — decided by instrument: when the whole stake can be lost (a long option) the allocation is the risk, so R-009 and the desk's C7 tiers govern; for stop-protected shares both apply [BOOK Cayman loc.46]; [BOOK Pansheriya loc.20]
- R-047 Fixed-ratio step-up vs R-009 Per-trade risk cap — decided by track record per the author (2% until four profitable weeks, then step up); the desk's C7 tiers govern every verdict regardless [BOOK Heitkoetter loc.45]; [BOOK Pansheriya loc.20]
- R-046 PowerX options vs R-010 Minimum reward-to-risk of 2 — decided by which leg is measured: the stock leg is 2:1 by construction (R-045); the in-the-money option the book picks estimates about 1.7:1 [BOOK Heitkoetter loc.41–42]; [BOOK Pansheriya loc.20]
- R-050 Index trend filter vs R-025 200-day gauge — decided by level: R-025 reads a single stock and says not to trade its crosses; R-050 switches index-level exposure on the 50/200 cross, checked weekly [BOOK Piard loc.17–19]; [BOOK Regan loc.27]
- R-062 Dividend yield-trap warning vs R-058 Dividend screen (yield over 4%) — decided by the yield's history: a high yield sustained over 5 years with low short interest → R-058; a yield above 5% that is new because the price fell → the yield-trap warning [BOOK Anderson loc.69]; [BOOK Piard loc.57–58]
- R-064 Pin bar / two-bar continuation vs R-030 Candle reversal at support — decided by trend context: a pause inside an established trend → R-064; a decline ending at support, or a range after a trend → R-030 [BOOK EDay loc.38–42]; [BOOK MetaStock p.24–25]
- R-066 Bollinger Band fade vs R-013 Keltner close-outside breakout — decided by regime: inside a sideways range → fade (R-066); in a trend → follow (R-013, intraday) [BOOK EDay loc.68–69]; [BOOK Salvon loc.14]
- R-071 Out-of-the-money swing options vs R-046 in-the-money options — decided by the desk's C4 move check on a real chain [BOOK EDay loc.15–16]; [BOOK Heitkoetter loc.40–43]
- R-070 Hit-rate-based target multiple vs R-010 fixed 2:1 floor — decided by evidence: no measured hit rate → R-010; a measured hit rate → the higher of the two [BOOK EDay loc.77–78]; [BOOK Pansheriya loc.20]
- R-072 50% take-profit, losers to max loss vs R-074 75% take-profit, stop at a loss equal to the credit — both from one book on different tests; decided by a desk test on the same data [BOOK FreemanCS loc.52]; [BOOK FreemanCS loc.69–70]
- R-080 Up to 10% per credit-spread trade vs R-009 2% per-trade cap — decided by the desk: C7 tiers govern every verdict, so R-080 is the book's view only [BOOK FreemanCS loc.76–79]; [BOOK Pansheriya loc.20]
- R-083 Average down on improving fundamentals vs R-022 Never add to a losing position — decided by the fundamentals since purchase: lower debt and higher earning power while the price fell → R-083; anything else → R-022 [BOOK Wyckoff p.149–152]; [BOOK Regan loc.15]
- R-082 2–3 day time stop vs R-044 PowerX 20-day time limit — decided by strategy: trades that expect an immediate move → R-082; PowerX swing trades with ADR stops → R-044 [BOOK Wyckoff p.130–131]
- R-089 Dollar-cost averaging vs R-022 Never add to a losing position — decided by plan type: a fixed schedule set before the first purchase for a long-term holding → R-089; adding to a trade that shows a loss → R-022 (or R-083 when the fundamentals have improved) [BOOK Gibbs loc.50]; [BOOK Regan loc.15]
- R-086 Penny-stock screen vs R-027 Exit-in-a-day liquidity — decided by strategy: short-hold penny-stock trading → R-086 with R-021; position and long-term calls → R-027 [BOOK Gibbs loc.24]; [BOOK MetaStock p.6]
- R-090 Take 20–30% within days vs R-061 20% trailing stop — decided by instrument and horizon: penny-stock trades → R-090; growth holdings kept for months → R-061 [BOOK Gibbs loc.58]; [BOOK Anderson loc.34]
- R-098 12-month momentum vs R-102 36-month reversal — decided by horizon: a quarter → R-098; multi-year holds → R-102 [BOOK Zacks loc.41]; [BOOK Zacks loc.43–44]
- R-109 January barometer vs R-054 Four-season calendar — decided by a desk test on the same index data; the barometer's own author rejects it as likely data mining [BOOK Zacks loc.99–101]; [BOOK Piard loc.37–43]
- R-121 Kelly-scaled weight vs R-009 Per-trade risk cap — decided by measure: Kelly sets a long-term holding's portfolio weight; R-009 and the desk's C7 tiers cap the loss at the stop and govern every verdict [BOOK Ramnarayanan p.164]; [BOOK Pansheriya loc.20]
- R-119 Sell only above a refreshed fair value vs R-061 20% trailing stop — decided by school and horizon: valuation-based long-term holdings → R-119; growth holdings managed on price → R-061 [BOOK Ramnarayanan p.58]; [BOOK Anderson loc.34]
- R-130 Buy a growth company after an earnings-miss sell-off vs R-097 Post-earnings drift (sell on a miss) — decided by horizon and evidence: a quarter's hold → R-097 (B); a multi-year hold where intrinsic value sits above the price → R-130 (D) [BOOK Damodaran p.148]
- R-146 Covered-call IV 30–70% vs R-077 credit-spread IV under 50% — decided by structure: owned shares under a covered call → R-146; defined-risk credit spreads → R-077 [BOOK FreemanCC loc.82]; [BOOK FreemanCS loc.42–43]
- R-154 Require a dated catalyst vs R-102 Long-term reversal basket — decided by method: a diversified statistical basket of three-year losers → R-102 (B); a concentrated single-name position → R-154 (C) [BOOK Osman loc.13–16]; [BOOK Zacks loc.43–44]
- R-158 Insider sales that matter vs R-105 (insider selling mostly uninformative) — decided by sale type: routine or option-related sales → noise; selling into weakness or a finance officer's full liquidation before earnings → R-158 [BOOK Osman loc.56]; [BOOK Osman loc.90–93]; [BOOK Zacks loc.51]
- R-160 Early range breakout (either direction, from the chart) vs R-011 Daily direction, intraday confirmation — decided by setup: a news-driven stock breaking its early range → R-160; an instrument without a catalyst whose daily trend sets the bias → R-011 [BOOK Walsh loc.77]; [BOOK Walsh loc.87–88]; [BOOK Salvon loc.2–3]
- R-164 Gap-fill bias vs R-161 continuation branch — decided by the early-range break: a break toward the prior close → R-164; a failed fill and a break away from it → R-161 [BOOK Walsh loc.82]; [BOOK Walsh loc.91–92]
- R-171 One-year top-performer screen (sub-investment-grade, volatile) vs R-056 Value screen ranked by lowest debt — decided by sleeve: a one-year speculative sleeve capped by R-175 → R-171; core holdings → R-056 [BOOK Fridson loc.107–108]; [BOOK Piard loc.54–56]
- R-171 One-year top-performer screen vs R-107 Avoid stocks within three years of listing — decided by sleeve: the book's non-index winners were recent IPOs trading below their offer prices (SolarEdge, Etsy); speculative sleeve → R-171; core holdings → R-107 [BOOK Fridson loc.91]; [BOOK Fridson loc.94]; [BOOK Zacks loc.58–59]
- R-176 Dow dividend ten vs R-062 Yield above 5% trap warning — decided by universe and construction: an equal-weight, annually reset basket of Dow members → R-176; a single name outside such a basket whose yield is new because its price fell → R-062 [BOOK Wildermuth p.81–88]; [BOOK Anderson loc.69]
- R-180 Rebalance on drift vs R-022 Never add to a losing position — decided by plan type: rebalancing to targets written before the first purchase → R-180; adding to a losing discretionary trade → R-022 [BOOK Wildermuth p.75–77]; [BOOK Regan loc.15]
- R-179 Hold rank-1 names even when overweight vs R-139 Trim near a fifth of the portfolio — decided by level: within a rule-driven sleeve of about 10 names → R-179; a position reaching about 20% of the whole stock portfolio → R-139 and the desk's risk tiers [BOOK Wildermuth p.116–118]; [BOOK Snow loc.33]
- Wildermuth principle (count-based technical system tested no better than chance) vs the swing-technical school (e.g. R-001, R-005, R-044) — decided by a desk backtest of each rule on the same data; the book's test is a single unpublished anecdote (C) and most swing-technical rules are C/D [BOOK Wildermuth p.137–139]
- Wildermuth principle (market timing is futile) vs R-050 Index trend filter — decided by evidence: R-050 carries a book-reported simulation (A); Wildermuth names no study (D) [BOOK Wildermuth p.139–140]; [BOOK Piard loc.17–19]
- R-186 Sell when operating indicators turn down vs R-112 Value on normalised margins (don't sell on a trough year) — decided by where the margin sits in its own multi-year range: near the bottom after a long decline → R-112; falling from a normal or recovering level → R-186 [BOOK Plotnick p.173–174]; [BOOK Ramnarayanan p.69–73]
- R-186 Sell when operating indicators turn down vs R-119 Sell only above a refreshed fair value — decided by trigger: price reaching target with fundamentals on track → R-119; operating indicators turning down → R-186 [BOOK Plotnick p.182–183]; [BOOK Ramnarayanan p.54–58]
- R-187 Sell a high-multiple holding on stalled earnings vs R-119 Sell only above a refreshed fair value — decided by earnings trend: fundamentals on track → R-119; flat earnings or an operating crack at a high multiple → R-187 [BOOK Plotnick p.184–185]; [BOOK Ramnarayanan p.54–58]
- R-194 Consensus-catch-up exit vs R-119 Sell only above a refreshed fair value — decided by price vs refreshed value: price still well below a refreshed value with results beating assumptions → R-119 (the author's IBM 1994 sale below value is his stated mistake); at or near value with consensus caught up → R-194 [BOOK Wachenheim loc.32–33]; [BOOK Wachenheim loc.70]; [BOOK Ramnarayanan p.54–58]
- R-198 Strong franchise, solvable problem vs R-132 Turnaround of an overlevered firm — decided by company strength: a strong, well-financed franchise with an operating problem → R-198; an overlevered firm needing a debt fix → R-132 as one of several small bets; the author avoids weak-company turnarounds [BOOK Wachenheim loc.122]; [BOOK Wachenheim loc.129]; [BOOK Damodaran p.182–183]
- R-199 Thesis-break exit (hold or add while the thesis holds) vs R-061 20% stop from cost and 20% trailing stop — decided by school: value holdings bought on a written thesis → re-test the thesis (R-199, R-083); growth holdings managed on price → R-061 [BOOK Wachenheim loc.103]; [BOOK Anderson loc.34]
- R-200 12% per stock at cost vs R-139 Trim near a fifth of the portfolio — decided by measurement base: at cost, winners may run (R-200); R-139 trims on market value; the desk's C7 tiers govern every verdict [BOOK Wachenheim loc.56]; [BOOK Snow loc.33]
- R-200 15–25 holdings vs R-028 At most 7 open positions — decided by horizon: R-028 for active trades; R-200 for a long-term stock portfolio [BOOK Wachenheim loc.148]; [BOOK MetaStock p.10]
- R-207 Trend-earnings market value vs R-018 Forward earnings yield vs 10-year Treasury — decided by input availability and use: R-018 needs forward consensus EPS (not connected); R-207 needs only reported EPS history; both are regime labels that set buying standards, not trade signals [BOOK Wachenheim loc.148]; [BOOK Yardeni p.8–9]
- R-213 LLM headline long-short (one day) vs R-130 Buy a growth company after an earnings-miss sell-off — decided by horizon: one-day hold on fresh news → R-213; multi-year hold with intrinsic value above price → R-130 [BOOK LopezLira p.231–233]; [BOOK Damodaran p.148]
- R-213 LLM headline long-short (trade in the news direction) vs R-164 Gap-fill bias — decided by a desk test on the same news days [BOOK LopezLira p.231–232]; [BOOK Walsh loc.82]
- R-217 Pocket pivot (buy inside the base) vs R-005 Breakout-retest (wait for the break and the retest) — decided by a desk test on the same bases [BOOK MoralesKacher loc.5]; [BOOK MoralesKacher loc.8–9]; [BOOK Pansheriya loc.13–14]
- R-219 Buyable gap-up (buy the gap, expect continuation) vs R-164 Gap-fill bias — decided by horizon and setup: intraday gaps inside yesterday's range → R-164; a daily gap of at least 0.75× ATR on ≥1.5× volume out of a base → this rule [BOOK MoralesKacher loc.128]; [BOOK Walsh loc.82]
- R-220 Seven-Week Rule (moving-average trail) vs R-061 20% trailing stop — decided by a desk test on the same growth holdings [BOOK MoralesKacher loc.14–15]; [BOOK Anderson loc.34]
- R-220 Seven-Week Rule (no target) vs R-010 Minimum reward-to-risk of 2 — decided by school: trend-following growth holdings are trailed without targets; target-based swing trades → R-010 [BOOK MoralesKacher loc.183]; [BOOK Pansheriya loc.20]
- R-221 7–8% maximum loss vs R-061 20% stop from cost — decided by entry type: a buy at a defined pivot near support → 7–8%; a wide-swinging growth holding bought without a pivot → R-061 [BOOK MoralesKacher loc.168]; [BOOK Anderson loc.34]; [BOOK Gibbs loc.52–53]
- R-223 Sell a big gap-down at the open vs R-130 Buy a growth company after an earnings-miss sell-off — decided by horizon and thesis: price-managed growth holding → this rule; multi-year hold with intrinsic value above price → R-130 [BOOK MoralesKacher loc.179]; [BOOK Damodaran p.148]
- MoralesKacher principle (mean-reversion indicators fight trends) vs R-066 Bollinger fade, R-067 DeMarker oversold buys and R-211 RSI signals — decided by regime: trending leaders → avoid the oscillators; sideways ranges → those rules [BOOK MoralesKacher loc.98]; [BOOK MoralesKacher loc.183]
- MoralesKacher principle (fewer, larger positions; more than ~20 names unsuited) vs R-200 15–25 holdings capped at 12% — decided by style and horizon: active trend-following book → fewer names; long-term value portfolio → R-200; the desk's C7 tiers govern every verdict [BOOK MoralesKacher loc.26]; [BOOK Wachenheim loc.148]
- R-228 Graham 7-year hurdle valuation vs Graham's own reprinted evidence that portfolios picked on expected growth only matched the market (1939–60) — decided by a desk test of the rule's buys against the S&P 500 over the same windows [BOOK Martin p.93–94]; [BOOK Martin p.104–111]
- Martin principle (trim a concentrated winner only when its margin of safety is gone, not on size) vs R-139 Trim near a fifth of the portfolio — decided by measure: valuation-based holdings → R-119 with this book; position-size limits → R-139 and the desk's C7 tiers [BOOK Martin p.62–63]; [BOOK Snow loc.33]
- Martin principle (no stop-loss orders on long-term holdings) vs R-061 and R-221 — decided by school and horizon: valuation-based long-term holdings re-test the thesis instead (R-199); price-managed growth holdings use stops [BOOK Martin p.278]; [BOOK Anderson loc.34]; [BOOK MoralesKacher loc.168]
- R-230 adding on drops vs R-022 Never add to a losing position — decided as R-083: forecast and milestones intact and price under the R-228 ceiling → add; otherwise R-022 [BOOK Martin p.122–124]; [BOOK Regan loc.15]
- R-235 Fade a market-wide IV spike vs R-073 No new credit spreads while the VIX is above 30 — decided by structure and evidence: index or index-weighted credit spreads while VIX > 30 → R-073 (B); single-stock defined-risk short IV with no company news → R-235, paper only until tested [BOOK Smith p.83]; [BOOK FreemanCS loc.67–68]
- R-237 Nearby expiry for an imminent move vs R-046 / R-071 (30+ days) — decided by expected timing: a move expected within days → nearby, if it passes the desk's C4 move check; otherwise 30+ days [BOOK Smith p.106–107]; [BOOK Heitkoetter loc.37]; [BOOK EDay loc.15–16]
- R-238 Out of the money for a strong view vs R-034 At or in the money — decided by the desk's C4 move check: out of the money only when its breakeven sits inside the typical move [BOOK Smith p.107–108]; [BOOK Cayman loc.11]
- R-243 Roll a covered call down at the breakeven vs R-143 (no strike below cost basis) — decided by why the shares are held: owned for their own case → R-143; buy-write held for the trade → R-243 [BOOK Smith p.146–148]; [BOOK FreemanCC loc.45]
- R-262 Hold a compounder through a high multiple vs R-187 Sell a high-multiple holding on stalled earnings — decided by the earnings trend: fundamentals on track and quality review passed → R-262; flat earnings or an operating crack at the high multiple → R-187 [BOOK Fisher loc.113–114]; [BOOK Fisher loc.202–203]; [BOOK Plotnick p.184–185]
- R-262 Hold a compounder through a high multiple vs R-119 Sell only when price passes a refreshed fair value — decided by school: a growth compounder held for its management and growth → R-262 (Fisher holds even above value); a valuation-based holding → R-119 [BOOK Fisher loc.114]; [BOOK Ramnarayanan p.54–58]
- R-262 Hold a compounder through a high multiple vs R-061 20% stop from cost, 20% trailing stop — decided by school and horizon: a fundamental long-term compounder is reviewed on its fundamentals (Texas Instruments fell 80% and later more than doubled its peak) → R-262; a price-managed growth holding → R-061 [BOOK Fisher loc.247–248]; [BOOK Anderson loc.34]
- R-263 Position caps at cost by class vs R-139 Trim a single stock near a fifth of the portfolio — decided by measurement base: caps at original cost, with no trim for growth-driven drift while the outlook holds → R-263; market-weight trims → R-139; the desk's C7 tiers govern every verdict [BOOK Fisher loc.139]; [BOOK Snow loc.33]
- R-263 Position caps at cost by class vs R-200 15–25 holdings, at most 12% per stock at cost — decided by company risk class: large entrenched companies up to 20% at cost (Fisher), mid-sized 8–10%, small at most 5%; a portfolio not classified this way → R-200 [BOOK Fisher loc.139]; [BOOK Wachenheim loc.56]
- R-263 small companies at most 5% each vs R-175 Speculative bets at 1–2% in total — decided by bet type: one-year speculative bets on outsized gains → R-175; multi-year small-company holdings that pass the full quality work → R-263 [BOOK Fisher loc.144]; [BOOK Fridson loc.8]
- R-267 Low or no payout for capital growth vs R-177 Favour dividend payers — decided by goal and reinvestment returns: a capital-growth sleeve where retained earnings earn high returns → R-267; income goals, or comparable stocks without such opportunities → R-177 [BOOK Fisher loc.122]; [BOOK Fisher loc.251]; [BOOK Wildermuth p.95–96]
- R-261 Three-year rule (sell a three-year laggard) vs R-102 Favour three-year losers — decided by method: a concentrated conviction holding judged on its own thesis → R-261; a diversified statistical basket → R-102 [BOOK Fisher loc.232]; [BOOK Zacks loc.43–44]
- R-255 No promotional companies vs R-127 Weight a young or loss-making company's value by its chance of surviving — decided by sleeve: Fisher growth sleeve → never buy before an operating record; a valuation sleeve that prices survival → R-127 [BOOK Fisher loc.126–127]; [BOOK Damodaran p.109]
- R-260 War-scare buying vs R-050 Index trend filter — decided by level and horizon: long-term accumulation of single names already chosen → R-260; index-level exposure switched on the 50/200 cross → R-050 [BOOK Fisher loc.148]; [BOOK Piard loc.17–20]
- R-256 Outside CEO: no new buying vs R-131 Badly managed company with a path to management change and R-198 Strong franchise with a temporary problem (a new CEO committing to cuts) — decided by school and starting point: a growth holding bought for its existing management → R-256; a value turnaround where the change of management is the catalyst → R-131/R-198 [BOOK Fisher loc.184]; [BOOK Damodaran p.160]; [BOOK Wachenheim loc.66–67]
- R-264 Buy at the market vs principle "Enter with limit orders…" and R-023 Don't chase past the planned entry — decided by horizon: swing and day entries at planned levels → limit orders / R-023; long-term growth buys sized small against volume → R-264 [BOOK Fisher loc.135–136]; [BOOK MetaStock p.10]; [BOOK Regan loc.25]
- R-258 Margin on sales vs R-231 Favour high, sustained ROIC — decided by purpose: Fisher distrusts return on assets because assets sit at historic cost, and uses margin on sales for safety (R-258); ROIC ranks profitability where asset costs are comparable (R-231); use both, with age-adjusted assets when comparing ROIC [BOOK Fisher loc.193]; [BOOK Martin p.176]
- Fisher principle (low P/E is as often a trap as a bargain) vs R-101 Value premium (cheapest fifth) — decided by method: a diversified statistical basket → R-101 (B); a single-name pick → explain the low P/E with scuttlebutt before buying [BOOK Fisher loc.221–222]; [BOOK Zacks loc.82]

## Principles
_(one line each: ideas with no measurable trigger, with their citation)_
- Price history alone misses the outside events that drive volatility; the authors suggest adding news and social-media data (no test shown) [BOOK Chhibber p.4]; agrees [BOOK LopezLira p.231–233] (headline text scored by an LLM forecast next-day returns in the author's study; see R-213) — D
- A level gains weight with each test that holds, yet repeated tests also make a break more likely; the book asserts both [BOOK Pansheriya loc.4] — D
- Early reversal warnings: price/indicator divergence, shrinking swings and volume, and how price reacts at key levels [BOOK Pansheriya loc.10] — D
- Match the method to the regime: trend tools and trailing stops in trends, range tools in ranges, wider stops with smaller size when volatile, step back around major news [BOOK Pansheriya loc.19–20] — D
- Write a trading plan, wait for valid setups, cap the number of trades per period, and journal every trade [BOOK Pansheriya loc.21–23]; agrees [BOOK Salvon loc.8]; agrees [BOOK Cayman loc.59] (plan, patience, records); agrees [BOOK Heitkoetter loc.53]; [BOOK Heitkoetter loc.63–65] (seven-part plan on one page; log every trade); agrees [BOOK Anderson loc.59–60] (plan entry, stop and target before entering; skip days without top-grade setups; review wins and losses); agrees [BOOK EDay loc.84] (journal entries, exits, screenshots and mood; review weekly); agrees [BOOK Gibbs loc.49]; [BOOK Gibbs loc.87] (journal every move, size and result); agrees [BOOK Broker p.250] (log results in points or cents rather than dollars and review them each weekend); [BOOK Broker p.289] (keep the strategy's rules written beside the screen); agrees [BOOK MoralesKacher loc.55] (diary of emotions and reasons for each buy; rehearse price scenarios on the chart in advance); [BOOK MoralesKacher loc.63–64] (real-time trade blotter sorted by profit and loss for postmortems) — D
- Practise on a demo account before risking money [BOOK Pansheriya loc.23]; agrees [BOOK Salvon loc.24]; agrees [BOOK Cayman loc.5]; agrees [BOOK Heitkoetter loc.50–51] (set the simulator to your real account size); agrees [BOOK Anderson loc.10–11]; [BOOK Anderson loc.55]; agrees [BOOK EDay loc.82–84] (simulate, then demo for six months); agrees [BOOK FreemanCS loc.72]; agrees [BOOK Gibbs loc.26–30]; [BOOK Gibbs loc.79–80] (paper-trade with real fees until consistently profitable) — D
- Loss aversion makes traders hold losers: set the exit before entering, and never move a stop because price is temporarily against you [BOOK Pansheriya loc.21]; agrees [BOOK Salvon loc.22]; agrees [BOOK Cayman loc.51] (know max loss and max gain before entering); agrees [BOOK Heitkoetter loc.27] (decide every exit before entering); agrees [BOOK Anderson loc.56] (close losers early); agrees [BOOK EDay loc.21–23] (exit at the preset stop without hesitation; don't become an accidental investor); agrees [BOOK Wyckoff p.50] (a 2–3 point stop behind every trade); [BOOK Wyckoff p.131–132] (most of his large losses came from not placing the stop at entry); agrees [BOOK Gibbs loc.45–47] (set the gain, the loss and the exit plan before entering) — D
- Tune settings per instrument and backtest a system before trading it live; published strategies are templates, not instructions [BOOK Salvon loc.13]; [BOOK Salvon loc.21]; agrees [BOOK Cayman loc.57–58] (test over long periods; a backtest is not proof); agrees [BOOK Piard loc.66–67] (vary each parameter and reject unstable results); agrees [BOOK Zacks loc.108–109] (test out of sample, in another period or country; Dogs of the Dow worked only when formed at year-end) — D
- Cap total risk across all open positions, not only risk per trade [BOOK Salvon loc.20]; agrees [BOOK Broker p.268] (example: six open trades at 1% each = 6% total) — D
- Keep a hard stop at the broker even when trailing a stop, in case the connection drops [BOOK Salvon loc.20]; agrees [BOOK Gibbs loc.51–52] (use automatic broker stops; a mental stop needs a price alert); agrees [BOOK Broker p.262] (a hard stop at the maximum loss plus a mental exit when the entry criteria break) — D
- Spread and commission costs grow with trade frequency; net them out of intraday targets [BOOK Salvon loc.24]; agrees [BOOK Wyckoff p.132–133] (very active in-and-out trading mostly pays the broker); agrees [BOOK Gibbs loc.13] (more trades, more commission); [BOOK Gibbs loc.82] (illiquidity's frictional costs erode profit) — D
- FX only: avoid the first ~2 hours of the Monday European session and late Friday because of weekend gaps [BOOK Salvon loc.2] — D
- Author claims a new day trader needs at least 500 practice trades over 3–6 months [BOOK Salvon loc.23] — D
- Value the index on 12-month forward consensus earnings (a time-weighted blend of this year's and next year's estimates); trailing earnings arrive late [BOOK Yardeni p.3]; [BOOK Yardeni p.7] — D
- Valuation models are not timing tools: over- or undervaluation can persist; the author ties them to below- or above-average returns over the next 12–24 months [BOOK Yardeni p.17] — D
- Don't re-engineer a model to fit the view: in 1999–2000 the models flagged overvaluation and some strategists swapped inputs to stay bullish [BOOK Yardeni p.4] — C
- A model reading is one input: the author cut equity exposure despite a record undervaluation reading because of earnings-quality worries [BOOK Yardeni p.5] — C
- Long-term consensus earnings-growth forecasts run above what aggregate profits can sustain (roughly GDP growth, about 7% a year historically); haircut them [BOOK Yardeni p.13]; agrees [BOOK Zacks loc.30] (analysts' estimates are too optimistic on average) — B
- Investors leaning heavily on long-term growth forecasts (the SVM-2 weight well above its ~0.13 average; ~0.23 at the 1999–2000 peak) signals a market priced for perfection [BOOK Yardeni p.12] — B
- Reverse the model: index × 10-year yield gives the market-implied forward EPS; its gap to consensus shows how much of an earnings cut is already priced [BOOK Yardeni p.14] — D
- Cash dividends are harder to dress up than reported earnings; a steady dividend record disciplines accounting [BOOK Yardeni p.16–17] — D
- Consumer expectations readings are most depressed at major market bottoms: use them to confirm a bottom, not to call one [BOOK Yardeni p.19]; [BOOK Yardeni p.29] — B
- Quantum/ML forecasting papers measure distribution fit, not trading returns; these authors say classical deep models still beat near-term quantum models for large-scale forecasting, so treat it as research, not a signal [BOOK Mourya p.12–13] — A for fit only
- Modelling correlated stocks together fitted each stock's up/down distribution better than single-stock models, with fewer parameters [BOOK Mourya p.13] — A for fit only
- VIX spikes tend to fall back toward the long-run level and calm stretches end abruptly; short-volatility products can be wiped out in one spike (an inverse-VIX note went to near zero in Feb 2018) [BOOK Baumgartner p.13–14]; agrees [BOOK Zacks loc.18–19] (selling naked index puts looks low-risk on history until the crash) — B
- Thin, wide-spread options keep arbitrageurs out and are cheap to push around; a liquid derivative settled on illiquid inputs invites manipulation [BOOK Baumgartner p.15]; [BOOK Baumgartner p.20] — B
- Shorting sub-$1 penny-stock promotions needs large capital and scarce borrow, and invites squeezes, buy-ins and margin calls; promotions can run several hundred percent before collapsing [BOOK Regan loc.16–19]; agrees [BOOK Gibbs loc.86] (shorting penny stocks is best left to professionals) — D
- Tiny positions in penny stocks lose to commissions, slippage and wide spreads [BOOK Regan loc.9] — D
- Most over-the-counter penny stocks have no revenue, earnings or cash; long holds tend to end near zero, so fundamental research on them adds little [BOOK Regan loc.5–8]; agrees [BOOK Gibbs loc.11–12] (Pink Sheet companies need not file regular reports); [BOOK Gibbs loc.88] (author claims about 99% ultimately fail) — D
- Size by the worst expected loss first: one oversized loss can erase many winners [BOOK Regan loc.13] — D
- The author claims default-setting indicators and textbook breakouts no longer work, without evidence; this cuts against R-002 and R-005 and should be settled by a test [BOOK Regan loc.15]; [BOOK Regan loc.20] — D
- Use message boards to see what the crowd is chasing and lean against it, not to find picks [BOOK Regan loc.21]; agrees [BOOK Wyckoff p.172] (the crowd is generally wrong); agrees [BOOK Gibbs loc.39–40]; [BOOK Gibbs loc.86–87] (ignore chat rooms, message boards and paid alert services for picks) — D
- Author claims exhaustion gaps are almost always filled, while breakaway and continuation gaps often are not [BOOK Regan loc.26] — D
- Very heavy volume often marks a trend change; tops tend to form fast and bottoms slowly [BOOK Regan loc.27] — D
- Short into rallies rather than after sharp drops, where short-covering squeezes hit [BOOK Regan loc.25] — D
- Never hedge a losing stock with options to justify holding it; cut the loss [BOOK MetaStock p.6] — D
- Enter with limit orders and exit with market orders, so an exit is never missed [BOOK MetaStock p.10]; [BOOK MetaStock p.12]; agrees [BOOK Cayman loc.5] (limit orders control the entry price) — D
- After a losing streak, paper-trade your signals until execution is back; exit any trade that no longer fits your documented best-trade profile [BOOK MetaStock p.13]; agrees [BOOK Wyckoff p.154–155] (suspend operations after an unprofitable stretch until the cause is found) — D
- Match indicators to the market condition (trend tools such as MACD in trends, oscillators such as stochastics in ranges) and confirm with indicators from a different category [BOOK MetaStock p.18]; [BOOK MetaStock p.40]; agrees [BOOK Broker p.281–282] (pair indicators of different types, one leading with one lagging); [BOOK Broker p.283] (one each of trend, momentum and volatility, e.g. a moving average, RSI and ATR) — D
- Place stops at chart-pattern levels rather than fixed percentages [BOOK MetaStock p.15] — D
- A doji or a cluster of small-bodied candles right after a rally or breakout warns that momentum is fading, but is not a sell signal by itself [BOOK MetaStock p.22–23] — D
- A Bollinger Band touch is not a signal by itself, and closes outside the bands can mean continuation [BOOK MetaStock p.41] — D
- Spot volatility shifts by comparing the latest swing size and duration with their recent averages: bigger swings or shorter cycles mean volatility is expanding [BOOK MetaStock p.31–34] — D
- Author claims markets fall 67–80% faster than they rise, so a trader should be able to short [BOOK MetaStock p.8]; agrees [BOOK Wyckoff p.48–49]; [BOOK Wyckoff p.51] (deal freely on both sides, or be an investor instead) — D
- Spread money across several companies rather than one; the author suggests about ten equal positions for a starting investor (in tension with R-028's cap of seven, which is about active trades) [BOOK Hammond loc.21]; agrees [BOOK Wyckoff p.202–203] (at least 10–20 securities in different businesses and places); agrees [BOOK Gibbs loc.59] (diversify; don't get attached) — D
- Check every source's motive and reliability before acting; company filings beat cherry-picked commentary [BOOK Hammond loc.22]; agrees [BOOK Gibbs loc.57–58]; [BOOK Gibbs loc.84–85] (read a newsletter's disclosure to see whether the pick was paid for) — D
- Confirm the ticker before acting on news: a 2021 celebrity post sent buyers into an unrelated over-the-counter stock with a similar name, which spiked several hundred percent in a day [BOOK Hammond loc.25–26] — C
- Treat high debt relative to EBITDA as a caution flag (the book gives no threshold) [BOOK Hammond loc.24] — D
- Long options lose value every day; decay is fastest at the money and in the final days, and a position helped by time is hurt by movement (and vice versa) [BOOK Cayman loc.16–18] — D
- Historical volatility hints at how big moves may be, not which way [BOOK Cayman loc.18–19] — D
- Rebalance between asset classes as correlations shift; don't let one class grow overweight after a long bull run [BOOK Cayman loc.27] — D
- Hedge an equity portfolio with puts on the index that tracks it best (large caps: S&P 500; small and mid caps: Russell 2000 or S&P 400), checked against the portfolio before hedging; the hedge drags returns in rallies; the book's hypothetical spends 3% of the hedged value on 3-month puts. Its tax claim about index options is out of the desk's scope [BOOK Cayman loc.30–32] — D
- A trend line needs at least two touches; breaking a well-tested line warns of consolidation, not a reversal by itself, and the broken line is often retested from the other side [BOOK Cayman loc.36] — D
- Author attributes to Wilder that markets trend about a third of the time and range the rest; momentum bias traps buyers near resistance and sellers near support [BOOK Cayman loc.35] — D
- Author asserts an ideal portfolio holds 25–30 uncorrelated securities, in tension with R-028's cap of seven [BOOK Cayman loc.25] — D
- Unnamed studies in the book say asset-class choice drives most returns, with selection plus timing about 6% of the variance; source not given, verify before use [BOOK Cayman loc.26] — D
- Sell puts only on stocks you understand and would accept owning; covered calls can be sold against long stock [BOOK Cayman loc.53–54] — D
- Weekly options leave little time to be right, and short weeklies carry high gamma (a small move can flip an out-of-the-money option into the money); the author asserts short puts beat short calls over short periods [BOOK Cayman loc.23–24]; agrees [BOOK FreemanCS loc.33] (avoid credit spreads on weekly options because gamma surges in the final week) — D
- Keep cash aside in case a complex option trade obliges you to buy shares [BOOK Cayman loc.47] — D
- Author asserts a bear market comes about every five years and called the market overdue as of writing (about 2017–19), from a chart of post-war bear markets; a forecast, not a timing rule [BOOK Heitkoetter loc.6–7] — D
- Ranges and trends both tend to persist, and moves that start tend to continue; chart examples only [BOOK Heitkoetter loc.15–16] — D
- Take profits at the planned target: in the book's IPO cases, holders who rode a first-day pop later saw prices far below [BOOK Heitkoetter loc.18–19] — C
- Ralph Vince experiment: 40 PhDs with $1,000 played 100 trades at a 60% win rate and even payoff; only 2 finished profitable, which the author puts down to poor sizing (source cited: CSI News Journal, March 1992) [BOOK Heitkoetter loc.45–46] — B
- Choose shares or options by account size, experience, share price, and the liquidity of both the stock and its options [BOOK Heitkoetter loc.33] — D
- Author asserts low-priced stocks make bigger percentage moves, so his examples are low-priced; in tension with R-027's low-price exclusion [BOOK Heitkoetter loc.31] — D
- An underfunded account breeds fear and gambling: ten $100 losses are 20% of $5,000 but 50% of $2,000 [BOOK Heitkoetter loc.51–52] — D
- Don't force trades in slow markets, don't revenge trade, and don't gut a working plan after a short losing streak; check the journal first [BOOK Heitkoetter loc.56–57]; [BOOK Heitkoetter loc.59–61]; agrees [BOOK Gibbs loc.48] (don't let a loss push you into a bigger, rushed trade) — D
- Mine your own trade log for filters (the book's hypothetical examples: long-only if longs do better, a minimum share price if cheap stocks lose) [BOOK Heitkoetter loc.66] — D
- Author claims his sizing scheme could turn $5,000 into $41,400, or $10,000 into $52,000, in 12 months; these are projections, not results [BOOK Heitkoetter loc.43]; [BOOK Heitkoetter loc.49] — D
- Recovering from a drawdown of x needs a gain of x/(1−x): 30% needs 43%, 50% needs 100% [BOOK Piard loc.14] — A (arithmetic shown)
- A backtest counts only on data available at each decision point: keep dead companies, time-stamp index membership and fundamentals, end moving averages the day before, model costs, and leave out illiquid names; its main use is measuring risk [BOOK Piard loc.13–15]; [BOOK Piard loc.62–64] — D
- Costs can erase high-turnover edges: buying Dow stocks after 4 down days and selling 2 days later went from about 16% a year to negative with 0.1% costs [BOOK Piard loc.64]; agrees [BOOK Zacks loc.10–11] (a recommendation strategy's 9.4% a year abnormal return became −3.1% after costs) — A
- Market timing's main benefit is shallower drawdowns, not higher returns, and it can lag in strong uptrends [BOOK Piard loc.18]; [BOOK Piard loc.58] — A
- Short-term momentum ranking failed on single large caps: the top 100 S&P 500 stocks by 20-day return made 0.7% a year vs 6.2% for the benchmark (2001–2013), while it worked on sectors and asset classes; a caution for single-stock momentum rules [BOOK Piard loc.36]; agrees [BOOK Zacks loc.44–45] (momentum absent in the largest stocks, strongest in mid caps) — A
- Variants of one anomaly (the same trend filter on several index ETFs) are one bet, not several, when sizing [BOOK Piard loc.22] — D
- Run 3–4 separate strategies on distinct anomalies with money-management rules rather than merging their rules; merged rules often did worse, separate sleeves cut drawdown [BOOK Piard loc.48–51]; agrees [BOOK Zacks loc.106–107] (combining factors can dilute a real one with a mined one) — A
- Overrating a win rate shrinks the edge fast: in one mix, using the 95%-confidence floor for the win rate (57.2% vs 61.6%) cut Kelly from 0.24 to 0.16 [BOOK Piard loc.11–12]; [BOOK Piard loc.52–53] — A (calculation shown)
- Seasonality: Jacobsen & Zhang's 1693–2009 data across 108 countries show November–April beating May–October; September was negative in all four periods tabulated; the January effect failed 1999–2012; 26 of 108 countries are inverted; sector seasonals are unreliable [BOOK Piard loc.37–39]; [BOOK Piard loc.45]; agrees [BOOK Zacks loc.99] (the January effect moved to December after 1995) — B
- Commodity seasonal tendencies are filters, not strategies; check contango and ETN counterparty risk [BOOK Piard loc.46–47] — B
- Short selling is asymmetric (recallable borrow, unlimited loss) and can't be backtested reliably without borrow data; squeezes can multiply a price in days [BOOK Piard loc.64–65] — C
- Daily-rebalanced leveraged ETFs lose to volatility: +25% then −20% leaves the asset flat but a 2× fund down 10%, so their backtests are path-dependent [BOOK Piard loc.68–69] — A (arithmetic shown)
- Few traders know the real probabilities behind patterns such as double tops or doji candles; they may be worse than assumed (a caution for the D-graded pattern rules) [BOOK Piard loc.69]; agrees [BOOK Zacks loc.39–40] (technical analysts found confident patterns in computer-generated random charts) — D
- Search-volume spikes (Google Trends at twice the prior months' average) flagged 4 of 9 tops in one stock, 2004–2012, with 4 neutral and 1 wrong: a warning, not a signal [BOOK Piard loc.71–73] — C
- A stock investment pays only above a hurdle of inflation plus the risk-free government yield plus a risk margin; the author puts the gross minimum at about 11% before costs and taxes (no data) [BOOK Anderson loc.7–8] — D
- The author doubts anyone beats the market consistently: he claims 95% of hedge funds don't beat the S&P 500 (citing only his own report) and calls chart patterns random, so he favours the index as the core holding; untested, and it cuts against the swing-technical rules [BOOK Anderson loc.19–21] — D
- The book says unnamed research found technical analysts' calls did not predict prices, while fundamental analysts' buy/sell advice and upgrades/downgrades were followed by matching moves the same and next day, and takeover bids below analysts' targets failed more often; no study named [BOOK Anderson loc.54]; agrees [BOOK Zacks loc.9–10]; [BOOK Zacks loc.14–15] (recommendation changes, especially downgrades, move prices) — D
- A price/book below 1 can mean overstated book value or a struggling company rather than a bargain; compare with the industry's usual P/B (in tension with R-056's cheap-on-book leg) [BOOK Anderson loc.29] — D
- Big, old companies can still fail (GM needed a bailout and Bear Stearns collapsed in 2008), so spread holdings across sizes and asset classes and rebalance [BOOK Anderson loc.26]; [BOOK Anderson loc.50–51] — C
- When fear stops you pulling the trigger, cut the risk per trade (the book's example halves $200 to $100) and step back up once trading calmly again [BOOK Anderson loc.61]; agrees [BOOK Gibbs loc.30] (if fear of loss hurts performance, move to lower-risk stocks or a calmer sector) — D
- Judge a strategy over the next 100 trades, not the last one, and stick with one framework long enough to evaluate it; constant tinkering hides whether it works [BOOK Anderson loc.61]; [BOOK Anderson loc.65]; agrees [BOOK Zacks loc.6]; [BOOK Zacks loc.107] (anomalies lag for years; swapping factors after a bad stretch means switching at the wrong time) — D
- Investors tend to sell winners too soon and hold losers too long; decide the goal before entering [BOOK Anderson loc.56]; [BOOK Anderson loc.67]; agrees [BOOK Zacks loc.46]; [BOOK Zacks loc.94–95] (small traders under-react; stocks individuals sell beat those they buy); agrees [BOOK Martin p.62–63] (trimming a winner early forfeits the late compounding) — D
- Author asserts a bear market (a fall of 20% or more from highs) comes about every 8 years on average, in tension with Heitkoetter's ~5 years; neither shows data [BOOK Anderson loc.70] — D
- Author claims the S&P 500 averaged 9.8% a year over 90 years plus about 2% from dividends, citing only his own report [BOOK Anderson loc.68] — D
- Author claims 90% of day traders don't last [BOOK Anderson loc.58]; agrees [BOOK Gibbs loc.86–87] (author claims only about 5–10% of investors profit consistently) — D
- DailyFX research cited in the book: almost 90% of retail traders lose their capital within a year (Rodriguez 2017) [BOOK EDay loc.3] — B
- Indicators lag because they are computed from price, so use them to confirm the trend/range reading, never as the system [BOOK EDay loc.66–67]; [BOOK EDay loc.71]; agrees [BOOK Broker p.274] (don't buy only because RSI is under 30 or sell only because stochastics is over 80); [BOOK Broker p.283] — D
- Reading a trend's health: real strength is many solid bars with small pauses; pauses that keep growing outweigh big bars; a shallow angle is weak, a steep angle early is strong, a steep angle late after countertrend selling hints at a climax [BOOK EDay loc.50–51] — D
- A level that bounces less each time is weakening; if a long at a well-tested level fails, the author flips short with the break [BOOK EDay loc.55–56] — C
- In high volatility (a high VIX) widen stops (the book gives no level; combine with smaller size per the existing regime principle) [BOOK EDay loc.60] — D
- High debt/equity (above 1) makes a stock swing harder both ways, which the author uses to pick fast movers; goodwill-heavy acquirers with repeated impairments are weak and may suit shorts if the chart agrees [BOOK EDay loc.61–62] — D
- Don't trade the headline itself; news is priced fast. Scheduled events (lawsuits, settlements) and spinoffs can start trends: wait for the trend that forms afterwards [BOOK EDay loc.22]; [BOOK EDay loc.63] — D
- Stay out around known high-volatility events to limit slippage; use stop orders, not limit orders, for the loss exit because a limit may not fill [BOOK EDay loc.27–28] — D
- Results come from hit rate and payoff together: in the book's arithmetic a 30% hit rate winning 3 and losing 1 makes money while a 90% hit rate winning 1 and losing 10 loses [BOOK EDay loc.73–75] — A (arithmetic shown)
- Judge a strategy on a large sample: small samples stray far from the true hit rate, and a losing streak does not make a win more likely (gambler's fallacy) [BOOK EDay loc.75–77] — D
- Risk a fixed percentage of equity, not a fixed dollar amount: losses shrink during streaks and gains compound [BOOK EDay loc.78–79] — D
- Don't trade when upset; loss aversion and framing make losing streaks feel worse than they are [BOOK EDay loc.80–81] — D
- Trade only money you can afford to lose, keep at least three months of living costs aside, and never need the market to pay bills [BOOK EDay loc.81]; agrees [BOOK Gibbs loc.14]; [BOOK Gibbs loc.48] (never rent, food or car money; keep trading money separate) — D
- Add instruments one at a time through the same test steps, keeping the same percentage risk across all of them [BOOK EDay loc.77]; [BOOK EDay loc.85] — D
- Author asserts swing trades last more than a day and up to about a week; holds of a month are not swing trades in his view (the desk's swing horizon is days–weeks) [BOOK EDay loc.20] — D
- Authors assert markets move sideways or only slightly up about 80–85% of the time, which favours non-directional option selling (no source) [BOOK FreemanCS loc.3–4] — D
- An option's delta roughly approximates its chance of finishing in the money (0.16 ≈ one standard deviation out); use it with support and resistance to place short strikes [BOOK FreemanCS loc.31]; [BOOK FreemanCS loc.65]; agrees [BOOK FreemanCC loc.84] — D
- An outside backtest cited in the book (projectoption, 2020): SPY bull put spreads 2008–2020 selling ~0.30 delta and buying ~0.16 delta, entered on the first and exited on the last trading day of each month, finished out of the money about 74% of the time [BOOK FreemanCS loc.65] — B
- Writing an in-the-money short leg brings a bigger credit but adds early-assignment risk; writing at or slightly out of the money avoids it for a smaller credit; cash-settled index options (SPX, RUT) remove assignment altogether. Early exercise is rare because the holder gives up the remaining time value [BOOK FreemanCS loc.21–23]; [BOOK FreemanCS loc.56] — D
- Enter multi-leg option trades as one order (or each spread as a unit), not leg by leg, and use a computer rather than a phone app [BOOK FreemanCS loc.25]; [BOOK FreemanCS loc.29]; [BOOK FreemanCS loc.66] — D
- Credit sellers want implied volatility high at entry and falling during the trade; widening Bollinger Bands or a rising IV mean stand aside [BOOK FreemanCS loc.40–42]; [BOOK FreemanCS loc.54] — D
- Choppiness Index readings above 61.8 suggest a ranging market (one chart shown) [BOOK FreemanCS loc.60–61]; agrees [BOOK FreemanCC loc.68–69] — D
- A credit spread that has been losing for more than about half of a 30–45-day hold rarely recovers, per the authors [BOOK FreemanCS loc.64] — D
- Keep the options-trading account separate from the long-term investment account so assignments never force sales of long-term holdings [BOOK FreemanCS loc.78] — D
- Specialise: learn two or so underlyings well, ideally with earnings in different months, rather than scanning hundreds [BOOK FreemanCS loc.80] — D
- Place option orders after the open has settled (the authors say by about 11 a.m. Eastern) and avoid after-hours orders, when spreads widen [BOOK FreemanCS loc.81] — D
- Don't trade hungry, angry, lonely, tired or impaired; keep the routine dull and consistent [BOOK FreemanCS loc.80–84] — D
- Authors claim credit spreads can earn 1–3% a month and project $5,000 growing to about $53,800 in 10 years; three reader testimonials report 86–96% win rates; projections and unverified testimonials, not results [BOOK FreemanCS loc.77–78]; [BOOK FreemanCS loc.84–85] — D
- Beyond value, prices move on manipulation, technical conditions and the market's trend; the trend matters most, and an overbought or oversold market decides the next swing's direction (no measurable definition given) [BOOK Wyckoff p.18–19] — D
- Dow's three simultaneous movements: the long trend over years, 30–60 day swings, and small swings of one to several days [BOOK Wyckoff p.30–31] — D
- The author made more from 10–20 point swings lasting 30–60 days, entered while accumulation or distribution is visible, than from trading for daily profits [BOOK Wyckoff p.40]; [BOOK Wyckoff p.132–133] — C
- A campaign runs accumulation (weeks to months), mark-up, then distribution; operators often overshoot and sell on the way down [BOOK Wyckoff p.41–42] — D
- Investment checklist, in order: the market's long trend, the industry's condition and direction, the company's trend, management's character and record, financial position and earning power, then the stock's place in its 30–60 day swing [BOOK Wyckoff p.98–101] — D
- Securities more often bottom when a danger is threatened than when it happens: fearful holders have already sold, so the event itself tends to bring a rally [BOOK Wyckoff p.78] — D
- Technical position: a stock held by many outside speculators once buying power is exhausted must fall whatever its fundamentals; heavy short selling that can't push the price lower is a source of strength, because shorts must buy back [BOOK Wyckoff p.108–109] — D
- Value by payout: on the author's arithmetic a stock paying 1% is worth about 12–20 against 60–100 for one paying 5–8%, and a non-payer's price above that is 'hope capitalized', so high-priced earners can be cheaper than low-priced stocks (in tension with the low-priced-stock principle) [BOOK Wyckoff p.79–80] — D
- Hold a well-researched position until something definite changes the premise, and take profits when the insiders start to sell rather than at a set number of points or percent (the author read insider selling from the stock's action) [BOOK Wyckoff p.92–93]; [BOOK Wyckoff p.112]; [BOOK Wyckoff p.121–123] — C
- Sell enough on strength to recover the original cost and hold the rest: selling part at a profit marks down the cost of the remainder [BOOK Wyckoff p.51]; [BOOK Wyckoff p.74]; [BOOK Wyckoff p.122] — C
- Reinvest every dividend, right and stock distribution rather than spending them, so the holding compounds; favour companies that retain and reinvest earnings [BOOK Wyckoff p.64–67]; [BOOK Wyckoff p.76] — D
- Each day's high, low and last are enough to judge a stock; the author judged best from market action alone, one hour a day, without news or the ticker [BOOK Wyckoff p.133–135] — C
- Know who owns the stock: buying by bankers, pools or large operators exhausts the floating supply ahead of a rise, while a stock spread among small holders after large interests have left rarely rises in concert until accumulation shows in the trading (13F and insider filings are today's observable proxy, a desk note) [BOOK Wyckoff p.207–212] — D
- Investigate before investing, not after; in speculative or early-stage ventures put in only money you can lose entirely, and check who else is invested, the financing, the experts and the product's market [BOOK Wyckoff p.84–87]; [BOOK Wyckoff p.193–200]; agrees [BOOK Gibbs loc.64] (a patent, 12+ months of financing, partners, government interest); [BOOK Gibbs loc.84] (management's record and legal issues) — D
- Keep part of the capital liquid so a panic can be used to buy: bear markets are swift, and two years of paper profits can vanish in 30–60 days; author claims the public is about 95% bullish at a top [BOOK Wyckoff p.71]; [BOOK Wyckoff p.173–174]; [BOOK Wyckoff p.184–185] — D
- Favour industries where demand outruns supply; the author bought oil producers in 1920 on consumption running ahead of production and a 1925 demand forecast [BOOK Wyckoff p.139–146]; check table p.138 — C
- Never get married to a security: review holdings against alternatives and switch, even at a loss, into ones that will work harder [BOOK Wyckoff p.81–82]; [BOOK Wyckoff p.164] — D
- The public is led, not leading: rising prices themselves draw buyers, and pools accumulate quietly, then mark prices up to bring the public in [BOOK Wyckoff p.106–107] — D
- Inside tips mislead even when true: the holder stays in too long or plunges afterwards; act on public facts you can verify [BOOK Wyckoff p.123]; [BOOK Wyckoff p.170–172]; agrees [BOOK Gibbs loc.39–40] (tips reach thousands at once, leaving scraps); agrees [BOOK MoralesKacher loc.27] (tips and headlines pull you off your rules; the authors fled to cash on March 2009 headlines) — C
- Penny-stock investing (research, then hold) is the book's advice for novices, yet it later claims unnamed studies show short-term penny trading is less risky; no study is named and the book contradicts itself [BOOK Gibbs loc.6–8]; [BOOK Gibbs loc.43] — D
- Regulators can halt a penny stock that rises irregularly fast, and holders can't sell during the halt [BOOK Gibbs loc.9] — D
- Pump-and-dump and related schemes: promoters buy cheap, hype through cold calls, spam, paid newsletters, message-board aliases and dubious press releases, then sell into the rise; also reverse mergers that inflate results, short-and-distort campaigns and paid 'guru' secrets [BOOK Gibbs loc.12–13]; [BOOK Gibbs loc.80–83] — D
- A stock that failed to rise on news that should have lifted it suggests buyers are avoiding it; study how it reacted to past events before trading it [BOOK Gibbs loc.21]; [BOOK Gibbs loc.35] — D
- Judge a company's size by market cap and share count, not share price: a $0.05 stock with 1 billion shares and a $50 stock with 1 million shares are both $50 million companies [BOOK Gibbs loc.36] — D
- Benchmark paper and real results against the sector (one sector) or the market (several), review the best and worst trades weekly with the reason for each, and drop information sources that keep proving false [BOOK Gibbs loc.26–30] — D
- In a thin stock, buyers who chase it push the price up themselves and may find no buyers when they sell [BOOK Gibbs loc.14]; [BOOK Gibbs loc.81] — D
- Beware story stocks: a compelling concept (a cure, a clean engine) attached to weak finances is often priced far above its value; media-hyped penny stocks tend to overinflate then fall, so check ratios rather than buy the story [BOOK Gibbs loc.14]; [BOOK Gibbs loc.64]; [BOOK Gibbs loc.79] — D
- Author claims buying below book value (his example: three-quarters of book) limits the loss if the company fails; in tension with the warning that a P/B below 1 can mean overstated book value [BOOK Gibbs loc.68–69] — D
- Judge a penny company's growth quarter by quarter; growing sales are not required for the price to rise but mark many big winners (the book's growth example uses market cap, which mixes price with business growth) [BOOK Gibbs loc.69–70] — D
- The book first says technical analysis lets a trader skip fundamentals, then recommends combining both; chart trading means smaller, more frequent gains, missing big moves, and often no overnight or weekend holds [BOOK Gibbs loc.73–75] — D
- Vet advisors and mentors on records: ask for at least a year of picks (or trade records and tax statements) and check them by following the picks forward; avoid advisors who call a stock undervalued for years against the evidence [BOOK Gibbs loc.86–87]; [BOOK Gibbs loc.89–90] — D
- Common mistakes by style: day traders misjudge liquidity and can't sell; value traders overvalue an asset they think the market cap ignores; the author says day trading needs a full day and at least four trades a day [BOOK Gibbs loc.91] — D
- Analysts' recommendations are biased (few sells, attachment to their industry, access to management), while their earnings estimates are tied to each quarter's report; even so, estimates run too optimistic on average and lean on accrual earnings [BOOK Zacks loc.29–30] — B
- Analysts herd: in one study other analysts' revisions explained about 15% of estimate changes, deviation from the consensus 12%, earnings reports 13%, price moves 11% and guidance 3%, with 46% company-specific; prices usually move before estimates do [BOOK Zacks loc.33–37] — B
- The small-cap premium is unstable: Banz (1981) found the smallest fifth beat by almost 5% a year, then small caps lagged for about two decades (about 40% behind large caps 1983–98) before leading 1999–2010; it comes mainly from the smallest, neglected, beaten-down names and historically much of it in January, so it needs decades of patience and low turnover [BOOK Zacks loc.16–17]; [BOOK Zacks loc.19–26] — B
- Many anomalies weakened after publication — the size effect after 1981, accruals after the late 1990s, the F and G scores in the decade after they appeared — so expect smaller edges than the original studies [BOOK Zacks loc.17]; [BOOK Zacks loc.71]; [BOOK Zacks loc.111]; [BOOK Zacks loc.114] — B
- Excess returns concentrate where institutions can't or won't trade: smaller, lightly covered, volatile, individually owned or costly-to-trade stocks (seen for recommendation changes, revisions, momentum, insider buying, value, accruals and earnings drift) [BOOK Zacks loc.12]; [BOOK Zacks loc.32]; [BOOK Zacks loc.45]; [BOOK Zacks loc.52]; [BOOK Zacks loc.75]; [BOOK Zacks loc.84]; [BOOK Zacks loc.93] — B
- Insider selling is mostly uninformative (diversification, option pay); studies found exceptions: stocks lagged by about 2% over six months after insiders adopted pre-set selling plans, and a CEO's large luxury-home purchase usually preceded weakness (in tension with taking profits when insiders sell) [BOOK Zacks loc.53] — B
- Heavy IPO and equity issuance, especially rising relative to debt issuance, has preceded weak market returns, and a dearth of issuance strong ones over about five years; a market-level gauge with no threshold given [BOOK Zacks loc.60–61]; [BOOK Zacks loc.66] — B
- Acquirers tend to overpay (the winning bidder's curse); paying in stock, especially in a spree, suggests managers think their shares are expensive, and paying with debt that they think them cheap [BOOK Zacks loc.65] — D
- Firms that look less likely to default (for example, higher interest coverage) have outperformed, and high bankruptcy risk has earned lower returns rather than a premium: the market misprices distress [BOOK Zacks loc.114–115] — B
- Calendar effects are prone to data mining: the January effect moved to December after 1995, holiday and Friday effects are small and noisy, and turn-of-the-month is the most significant and best explained (money flows); the author uses seasonality only for small timing tweaks (trade in the afternoon, buy near the turn of the month, sell after a holiday) and rejects market timing [BOOK Zacks loc.96–99]; [BOOK Zacks loc.102–105] — B
- Author's tally: only 2 of 40 Indian large-cap funds beat the Nifty 50 (17.4% a year) over five years to November 2021, at about 2% fees; low-cost index funds suit most investors [BOOK Ramnarayanan p.13–15] — B
- Quality at any price is a fallacy: returns depend on ROE, growth and the price paid together [BOOK Ramnarayanan p.17–18] — D
- DCF is error-prone for fast growers because the terminal value dominates; for low-capex, high-payout companies with clean working capital, value earnings as a perpetuity, net income ÷ (r − g) [BOOK Ramnarayanan p.18]; [BOOK Ramnarayanan p.35–36]; [BOOK Ramnarayanan p.109–110] — D
- Use magic-formula style rankings as a screen only: the top of the list fills with poor earnings quality, weak governance and cyclicals at the wrong end of the cycle [BOOK Ramnarayanan p.22–23] — D
- Check whether a high ROE comes from operations or leverage before paying for it [BOOK Ramnarayanan p.26–27] — D
- Set the required return from a public anchor, e.g. 2× the 10-year government bond yield (2× inflation when real rates are negative), or the index's long-run CAGR (Nifty 50 15-year rolling 10–17%, mean 12.8%); too high a hurdle shrinks the universe, too low overpays [BOOK Ramnarayanan p.41–45] — D
- When your fair value is far from the price, assume the market may be right and try to kill the idea first [BOOK Ramnarayanan p.49–51] — D
- Value screens bunch in one out-of-favour sector at a time; map holdings by sector and keep business drivers different [BOOK Ramnarayanan p.51]; [BOOK Ramnarayanan p.181–182] (a stock can lag for years even when the business delivers) — C
- Author's experience: Graham net-nets and stocks below their cash seldom paid off in India without a catalyst, given high promoter stakes [BOOK Ramnarayanan p.67–68] — C
- Before valuing: check cash flow against reported profit, governance, where the industry is in its cycle, one-off tailwinds and executive pay vs peers [BOOK Ramnarayanan p.179] — D
- Advertising and similar spending is economic capex; capitalising it shows a different ROE for 'zero-capex' companies [BOOK Ramnarayanan p.107–109] — D
- A high P/E embeds a high growth expectation and so a larger correction risk; the author cites a fund manager's study of 25 compounders 1973–2021 where very high entry multiples still beat the market [BOOK Ramnarayanan p.115–117] — B
- Borrowing to hold stable dividend payers or REITs when the yield covers the interest is discussed; recorded only, outside the desk's scope [BOOK Ramnarayanan p.147–150] — D
- Pre-commit to slow down decisions: keep spare cash where it takes a day to deploy, sell on a fixed weekly schedule, place orders outside market hours, keep derivatives disabled unless needed [BOOK Ramnarayanan p.173–175] — D
- Don't publicise holdings: public commitment makes it harder to change your mind when facts change [BOOK Ramnarayanan p.183–186] — D
- Judge REITs against REIT factors, not the broad market: a REIT market, size and dividend-yield model explained about 88–98% of REIT portfolio returns 1999–2019 vs at most about 51% for the standard three-factor model; REITs barely load on the stock market once REIT factors are in [BOOK Trefz p.32–36]; [BOOK Trefz p.139] — A
- Studies of short selling in REITs conflict; an apparent short-interest effect in large REITs disappears once REIT-specific factors are controlled [BOOK Trefz p.22–24]; [BOOK Trefz p.44–45] — A
- First Covid wave (Jan–Jun 2020): industrial and infrastructure REITs did best on return and risk, healthcare, lodging and retail worst; data centres led on return but carried high tail risk after adjustment; REITs were riskier than the stock market; prices moved with US Covid deaths about three weeks before they were reported [BOOK Trefz p.58–63]; [BOOK Trefz p.75]; [BOOK Trefz p.109–110] — A (one episode)
- In a crisis, co-movement across real-estate sectors rose sharply before adjustment, so spreading across property types may not diversify when it matters [BOOK Trefz p.90–92]; [BOOK Trefz p.110] — A (one episode)
- High-ESG REITs showed no return edge before or during the 2020 crash but significantly lower volatility and value-at-risk during it once stock and REIT factors were controlled; the wider ESG–return literature is mixed [BOOK Trefz p.112–114]; [BOOK Trefz p.122–127]; [BOOK Trefz p.137] — A (one episode)
- Write down your biases before valuing (why this company, do you own it, do you like management) and research from filings rather than opinion sources such as analyst reports [BOOK Damodaran p.32]; [BOOK Damodaran p.33] — D
- Use the simplest valuation model that works: fewer inputs and shorter explicit forecasts mean fewer errors [BOOK Damodaran p.35]; [BOOK Damodaran p.36] — D
- Most valuations are wrong; the author overvalued Cisco (2001) and a bank before the 2008 crisis; uncertainty is shared by every investor, so refusing to value doesn't remove it [BOOK Damodaran p.34]; [BOOK Damodaran p.35] — C
- The author cites studies finding past growth and analyst or management growth forecasts weakly predict future growth; growth falls as companies get larger [BOOK Damodaran p.72]; [BOOK Damodaran p.73]; [BOOK Damodaran p.132] — B
- Studies cited say CAPM betas explain return differences poorly; prefer sector-average betas to a single stock's noisy regression beta [BOOK Damodaran p.46]; [BOOK Damodaran p.68] — B
- Multiples: define numerator and denominator consistently (equity with equity, enterprise value with operating measures); price/sales and price/EBITDA make indebted firms look cheap; compare to medians, not means; distrust a multiple that drops many firms (e.g. P/E with losses) [BOOK Damodaran p.87]; [BOOK Damodaran p.88]; [BOOK Damodaran p.90]; [BOOK Damodaran p.91] — B (2010 US cross-section)
- A P/E compared with its own history misleads when interest rates differ from their norms, and relative valuations go stale within months [BOOK Damodaran p.92] — D
- Relative valuation assumes the peer group is priced right on average; when a whole sector is overpriced (internet stocks in 2000) members look cheap on multiples while a DCF says expensive [BOOK Damodaran p.102] — C
- Intrinsic valuation needs a long horizon (three to five years) for the market to correct; an undervalued stock can get cheaper first [BOOK Damodaran p.81] — D
- Debt-funded buybacks and recapitalisations move equity multiples (P/E, P/B) far more than enterprise multiples; prefer EV multiples when leverage is changing [BOOK Damodaran p.153]; [BOOK Damodaran p.154] — D
- Markets discount cash held at low returns or at risk of misuse, and conglomerates' cross-holdings; payouts and spin-offs can release the discount [BOOK Damodaran p.159]; [BOOK Damodaran p.160] — D
- Equity in a heavily indebted firm acts like a call option and can keep value even when the business is worth less than the debt, more so in risky businesses with long-dated debt [BOOK Damodaran p.179]; [BOOK Damodaran p.180] — D
- Undeveloped commodity reserves act as options: more price volatility raises their value, most when the commodity is cheap, so a DCF on expected prices understates reserve-rich producers [BOOK Damodaran p.222]; [BOOK Damodaran p.223] — D
- Studies cited put the US premium of voting over non-voting shares at about 5–10% [BOOK Damodaran p.144] — B
- Banks' reported earnings depend on how conservatively they provision for bad loans, which skews P/E comparisons [BOOK Damodaran p.203] — D
- Valuation pays only if the market corrects and luck cooperates; spread money across many undervalued stocks to blunt luck [BOOK Damodaran p.252]; [BOOK Damodaran p.253] — D
- Missing the market's best days costs most of the return: Putnam data cited, 15 years to 2017: 9.9% a year fully invested, about 5% missing the 10 best days, about 2% missing 20, slightly negative missing 30 [BOOK Snow loc.20]; agrees [BOOK Snow loc.35] (Morningstar 1992–2011 figures, garbled in the text) — B
- Reinvested dividends: the book cites S&P 500 returns of about 6.7% a year on price alone vs about 11% with dividends reinvested, 1921–2021 (source not named) [BOOK Snow loc.21] — B
- S&P data cited: about 84% of US stock funds lagged the S&P 1500 over 15 years to mid-2018, and 92% of large-cap funds lagged the S&P 500; benchmark your own picks against an index fund over several years [BOOK Snow loc.32]; [BOOK Snow loc.33] — B
- A 1992–2006 study of frequent traders is cited: about 80% lost money and about 1% were reliably profitable [BOOK Snow loc.30] — B
- When a holding falls, find the cause: hold through temporary setbacks (a raw-material spike, a plant fire); consider selling on lasting damage (a strong new rival, an accounting scandal, hostile regulation); sell a stock you've lost faith in rather than waiting to break even [BOOK Snow loc.31]; [BOOK Snow loc.34] — D
- Invest only money not needed for about five years, after paying off high-interest debt and keeping an emergency fund (the book says six to twelve months in one place, three in another) [BOOK Snow loc.28]; [BOOK Snow loc.54] — D
- Diversify across industries and countries, not just names: the author treats fewer than about 15 stocks as risky and 10–20 as typical (in tension with R-028's cap of seven active positions) [BOOK Snow loc.30–31] — D
- Read the 10-K footnotes, and strip truly one-off items, but a company reporting 'extraordinary' charges year after year is reporting ordinary costs [BOOK Snow loc.76]; [BOOK Snow loc.77] — D
- Judge a company by market cap, not share price: splits add no value, and a reverse split usually follows a collapse in the price [BOOK Snow loc.45]; [BOOK Snow loc.46] — D
- A quoted manager sells a stock that has reached its objective even with no replacement lined up, and sets trailing stops from fundamentals and chart levels rather than a fixed percentage [BOOK Snow loc.122] — D
- A quoted planner calls option-based 'portfolio insurance' a costly expense for a diversified portfolio and prefers holding cash and short high-quality bonds, using options only for a large concentrated holding that can't yet be sold [BOOK Snow loc.120–121] — D
- A study cited (Witter and Coyne) found the 40–100 most active investors in a stock account for over half of its price changes [BOOK Snow loc.83] — B
- The book's title calls covered calls risk-free; they carry the stock's full downside less the premium and cap the upside (max profit = strike − cost + premium; max loss = cost − premium; breakeven = cost − premium) [BOOK FreemanCC loc.7]; [BOOK FreemanCC loc.46–47]; [BOOK FreemanCC loc.92] — D
- The '85% of options expire worthless' figure is a myth because many options are closed before expiry; the authors put the worthless share nearer 35% and early closes near 60%, citing a 2019 article without method [BOOK FreemanCC loc.37–38]; agrees [BOOK Broker p.191]; [BOOK Broker p.203] (attributes to a CBOE report, undated: about 10% exercised, 60% closed early, 30% expire worthless) — B
- Writers win often but small; the authors warn against expecting casino-like win rates and say to exit when the investment thesis changes, not on price [BOOK FreemanCC loc.37–39] — D
- A chart in the book shows monthly covered calls on the S&P 500 trailing buy-and-hold; period and source not given in the text (figure not converted) [BOOK FreemanCC loc.62–63] — B (check figure loc.62)
- For single-stock calls use the stock's own implied volatility, not the VIX or beta [BOOK FreemanCC loc.31]; [BOOK FreemanCC loc.80] — D
- If the stock falls: a trader closes both legs together (selling only the stock leaves a naked call); an investor whose thesis still holds keeps the shares and keeps writing [BOOK FreemanCC loc.63]; [BOOK FreemanCC loc.91] — D
- Rolling the call down after a decline lowers the cost basis but can lock in a stock loss if assigned, and premiums may never recover the loss [BOOK FreemanCC loc.93]; [BOOK FreemanCC loc.117] — D
- A covered-call writer still collects dividends if holding on the ex-date; the authors call timing writes around dividends speculation (early assignment before an ex-date is not discussed) [BOOK FreemanCC loc.47]; [BOOK FreemanCC loc.57–58] — D
- The authors tell beginners to avoid writing puts even though a covered call has the same risk profile as a short put; contrast R-036 and the Cayman principle on selling puts on stocks you'd own [BOOK FreemanCC loc.45–46] — D
- Covered-call funds charge around 0.8% versus about 0.03% for index funds and tend to lag; consider closed-end ones only at a discount to NAV; the authors prefer writing your own [BOOK FreemanCC loc.109–111] — D
- Vet trading educators: ask for broker-audited records and a risk-adjusted return (Sharpe ratio), check registration on FINRA BrokerCheck, and treat screenshots and testimonials as unverified [BOOK FreemanCC loc.112–116] — D
- Author projections (an 8.85% annual premium yield on Disney computed on an old cost basis, not market value; $116,072 vs $30,580 over 20 years; $25,000 to $1 million in 23 years at 15%) are projections, not results [BOOK FreemanCC loc.43–44]; [BOOK FreemanCC loc.48–49]; [BOOK FreemanCC loc.117] — D
- Ask why a stock is cheap before buying: falling sales or heavy debt, an out-of-favour sector, a conglomerate discount, no coherent strategy, or sentiment; cheap can get cheaper (Toys R Us, Sears) [BOOK Osman loc.3]; [BOOK Osman loc.13–14] — C
- Start with risk, not upside: set risk controls before entry, keep reserves, and review a thesis when planned financial targets are missed, competition shifts, unforeseen legal or regulatory problems appear, or management changes plan [BOOK Osman loc.7]; [BOOK Osman loc.9]; [BOOK Osman loc.30] — D
- Merger arbitrage earns a small spread (time value plus deal risk) and one broken deal can erase many wins; market sell-offs can sink whole arbitrage books; the author leaves it to professionals [BOOK Osman loc.16]; [BOOK Osman loc.64–65] — D
- Identify a spin-off's stated reason (focus, activist pressure, visibility, regulation, complexity); the company is telling you how it plans to create value [BOOK Osman loc.32]; [BOOK Osman loc.38] — C
- Track the event calendar for each holding (announcement, record date, ratio, first trading day; earnings and corporate dates) and set news alerts rather than following macro commentary [BOOK Osman loc.39]; [BOOK Osman loc.97] — D
- Distressed, bankruptcy and post-reorganisation equity is for specialists; equity is last in line, and following investors with good records who inject new money is safer but still needs your own work [BOOK Osman loc.16–17]; [BOOK Osman loc.67–68] — D
- Rights offerings and other need-driven transactions deserve attention because the company acts out of necessity; weigh dilution and the use of proceeds [BOOK Osman loc.17–18]; [BOOK Osman loc.69] — D
- Activist campaigns and proxy fights add volatility and distraction and many activists are not good; judge the plan, not the name [BOOK Osman loc.19–20]; [BOOK Osman loc.70] — D
- Shorting has capped gain and unlimited loss, borrow costs, timing risk and takeover or good-news risk; use it rarely and small (Ackman's Herbalife short lost about $1 billion) [BOOK Osman loc.84–89] — C
- Only one edge is legal and durable for most investors: better analysis of public information plus behavioural discipline; inside information is illegal and speed is lost to machines [BOOK Osman loc.83–84] — D
- Avoid one oversized position; size bets evenly, keep quality holdings in downturns, and don't use 'long-term' to excuse fundamentals turning against you (the author himself runs 10–15 concentrated positions) [BOOK Osman loc.7]; [BOOK Osman loc.96]; [BOOK Osman loc.98] — D
- Bias traps to check: confirmation, anchoring (build a relative-value table of competitors), sunk cost, overconfidence and blind spots; get a second opinion on big decisions [BOOK Osman loc.105–109]; [BOOK Osman loc.125] — D
- Don't build positions on market forecasts; models built on past data fail when regimes change, so stress-test and use preset decision rules [BOOK Osman loc.112]; [BOOK Osman loc.118–120] — D
- Rule one: end losing trades quickly and let winners run; winners larger than losers is essential, a high win rate is not [BOOK Walsh loc.10]; [BOOK Walsh loc.47–48]; agrees [BOOK MoralesKacher loc.23] (one big winner, CUBE 1995, rescued a year with a hit rate of about 1–2 in 10); [BOOK MoralesKacher loc.45] — D
- Day traders hold nothing overnight, avoiding after-hours news risk; margin magnifies losses and can force liquidation [BOOK Walsh loc.8]; [BOOK Walsh loc.18–19]; [BOOK Walsh loc.120] — D
- Market depth and single prints mislead: watch order flow over time, and check volume before trusting an odd bar [BOOK Walsh loc.22]; [BOOK Walsh loc.26–27] — D
- Trade only obvious patterns; if you have to squint, it isn't there. Too many indicators cause paralysis, and an oscillator warning needs price confirmation [BOOK Walsh loc.37]; [BOOK Walsh loc.42]; [BOOK Walsh loc.108] — D
- Always place a protective stop on entry but exit manually first; stops sitting just past obvious levels get run, so give them room [BOOK Walsh loc.45–46]; [BOOK Walsh loc.87] — D
- Over-trading: cap trades per day (start at one, raise by one once each day's pick is consistently good, reimpose on relapse); the author rarely takes more than 6–7 a day [BOOK Walsh loc.60]; [BOOK Walsh loc.73] — D
- Psychology: think in points, not money; talk the trade aloud; write fears down while trading and answer them after the close; no revenge trading; stay ready to re-enter the same stock [BOOK Walsh loc.57–60]; [BOOK Walsh loc.105]; [BOOK Walsh loc.108] — D
- Log each trade (pattern, confirmations, size, feelings, exit reason, 1–5 execution score), tally average win vs average loss daily, review at the weekend, and drop setups that don't pay [BOOK Walsh loc.106–107] — D
- Author claims markets trend only about 20% of the time, so moving-average crosses whipsaw; no source given [BOOK Walsh loc.32]; [BOOK Walsh loc.38] — D
- News picks the stock, the chart picks the direction; scanners only show moves already made, so prepare the list before the open [BOOK Walsh loc.77]; [BOOK Walsh loc.83] — D
- The book's market-structure notes are dated (NYSE specialist fills, uptick rule called abolished, Pattern Day Trader $25,000 / 3-trades-in-5-days, offshore workarounds); verify current rules, and the desk does not advise on regulation [BOOK Walsh loc.71]; [BOOK Walsh loc.72–74]; agrees [BOOK Broker p.239–241] (2020: $25,000 day-trading minimum, 2× overnight vs 4× intraday margin); [BOOK Broker p.272] (EU retail leverage cap) — D
- Value tracks free cash flow (operating cash flow − capex), not EPS: EPS can be raised by low-return borrowing, longer depreciation lives or accounting-rule changes without moving value [BOOK Fridson loc.14–16]; [BOOK Fridson loc.26–27] — B (Stern, FAJ 1974)
- An ordinary EPS beat is the norm, not news: 78.8% of early 4Q21 S&P 500 reporters beat, 84% over the prior four quarters; companies guide to a beatable bar. This weakens R-042 (any beat) relative to R-097 (top-decile surprises) [BOOK Fridson loc.39]; [BOOK Fridson loc.42] — B
- Read analyst ratings against their skew: Buy 52.9% / Hold 41.1% / Sell 6.0% (FactSet, five-year monthly average to April 2022); Hold often means sell, and a consensus Buy is the base rate [BOOK Fridson loc.48]; [BOOK Fridson loc.50–52] — B
- Price-target upside doesn't find the year's biggest winners: NRG's highest 2017 target implied 80.5% vs an actual 134%; TSLA's upgraded targets implied about 23% vs 743% [BOOK Fridson loc.77]; [BOOK Fridson loc.102] — C
- Rejected for spotting the year's top five S&P 500 stocks (author's Bloomberg test, top five each year 2012–2021 vs the other 495; results stated as 'no pattern', numbers not shown): analyst price-target upside, five-year revenue growth, ROE growth, FCF yield, short-interest ratio, insider buying, rating outlooks. These say nothing about the average-outperformance rules that use them (R-096, R-101, R-105) [BOOK Fridson loc.112–114] — C
- Outsized one-year gains need a surprise to a large share of holders; long-known virtues are already priced (Zoom 2020; TSLA's unexpected 3Q19 profit) [BOOK Fridson loc.73]; [BOOK Fridson loc.115–116] — C
- Qualitative markers of past top performers: a technology lead in a fast-moving industry, and a dominant rival that stumbles (Intel flaws and delays for AMD, Huawei's setback for Enphase, Etsy holding off Amazon) [BOOK Fridson loc.117]; [BOOK Fridson loc.120] — C
- Prior-year laggards can lead the next year: AMD −9% in 2017 then #1 in 2018; Devon #481 in 2020 then #1 in 2021; SolarEdge −56% in 2016 then +203% [BOOK Fridson loc.66]; [BOOK Fridson loc.83]; [BOOK Fridson loc.91] — C
- Watch for big-bath write-offs that build reserves to release later, and treat company-defined adjusted EPS as non-comparable [BOOK Fridson loc.33]; [BOOK Fridson loc.55] — D
- Lower earnings volatility earns no valuation premium, and diversifying to smooth earnings doesn't add value (McKinsey 2013) [BOOK Fridson loc.19]; [BOOK Fridson loc.21] — B
- Analyst estimates cluster around company guidance: when 180 S&P 500 companies dropped guidance in 2020, estimate dispersion was the widest since at least 2007; wider coverage is linked to higher value [BOOK Fridson loc.37]; [BOOK Fridson loc.41] — B
- Don't forecast commodity prices: the 2021 NYMEX median WTI forecast was $42 vs $75.21 actual; hold some exposure positioned for a spike instead (Energy led the S&P 500 sectors in 20% of years 2007–2021) [BOOK Fridson loc.83]; [BOOK Fridson loc.87] — C
- Market lore and trading rules are guesses until tested on data; anecdotes prove nothing [BOOK Fridson loc.110–111] — D
- Technical analysis: one study summarised by Lo and Hasanhodzic found 10 chart patterns statistically valid but did not show them profitable; the author doesn't use charts to hunt for top stocks [BOOK Fridson loc.57–59] — B
- Match horizon to stocks: from 1926 to 2001 the share of periods with a positive average annual return was about 67% for 1 year, 90% for 5, 97% for 10 and 100% for 15 (Ibbotson). Money needed within about 5 years doesn't belong in stocks [BOOK Wildermuth p.15–16]; [BOOK Wildermuth p.18] — B
- Most actively managed funds trail the index after costs. After a survivorship adjustment, only 14 of 821 funds with 15-year records beat the Dow to 2001. Funds ranked first went on to trail the average similar fund about 80% of the time [BOOK Wildermuth p.36–37]; [BOOK Wildermuth p.47–48] — B
- Behaviour costs more than fees. Dalbar: from 1984 to 2000 the average stock fund returned 14% a year, but the average fund investor earned 5.3%, because investors switch into what just did well. Don't chase recent winners [BOOK Wildermuth p.51–53]; [BOOK Wildermuth p.67] — B
- Hidden trading costs compound. Bogle cites a 1993 study putting an average transaction at about 0.6%, so 200% turnover costs about 2.4% a year, and many funds total 3–5% a year all in [BOOK Wildermuth p.42–43] — B
- Follow a written, rule-based system so fear and greed don't make the decisions: fix buy and sell triggers in advance, and if you can't follow them with all the money, follow them with part and measure the result [BOOK Wildermuth p.72–73]; [BOOK Wildermuth p.114]; [BOOK Wildermuth p.157] — D
- Don't tune a backtest universe by dropping laggards. A list built from stocks with good past records overstates its history, so judge a screen by its edge over its own universe [BOOK Wildermuth p.102–104] — C
- Value-tilted rule systems lag in fast, growth-led markets (1998–99 here) and earn their keep in the declines that follow. Hold the rules through the lag [BOOK Wildermuth p.90]; [BOOK Wildermuth p.92] — B; check table p.91
- Rank-driven lists cluster in one or two industries. Cap industry overlap when building from them [BOOK Wildermuth p.116]; [BOOK Wildermuth p.119] — D
- Discount sell-side ratings: research departments are conflicted by banking clients. The book asserts that fewer than 3% of ratings were sells in July 2002, with no source [BOOK Wildermuth p.107–108] — D
- Ignore hot tips, testimonials and systems that are sold. A system that needs more than about ten steps, or inputs you don't understand, won't be followed [BOOK Wildermuth p.144–147] — D
- Technical analysis: the author's own early-career test of a quantitative up-day/down-day count system on S&P 500 stocks matched chance, and he says the same of every system he has seen since. He gives no rules, period or statistics [BOOK Wildermuth p.137–139] — C
- Market timing: the author asserts that every study finds it futile but names none. Contrast the playbook's tested index filter (R-050) and Piard's finding that timing mainly reduces drawdowns [BOOK Wildermuth p.139–140] — D
- Day trading is called gambling. The often-quoted figure that 96% lose all their principal within two years is one the author can't source and says he doesn't know is true, so it is not carried as data [BOOK Wildermuth p.140–143] — D
- Shock sell-offs (Pearl Harbor 1941, 9/11, the 2002 accounting scandals) were largely recovered within weeks to months; most damage came from panic selling, not the events themselves [BOOK Wildermuth p.17–18]; [BOOK Wildermuth p.26] — C
- Recorded only, outside desk scope: the Rule of 100 for retirees, retirement-plan and fund selection, index annuities and the author's annuity Partition System (a product he sells), and choosing an adviser [BOOK Wildermuth p.19–20]; [BOOK Wildermuth p.55–67]; [BOOK Wildermuth p.121–132]; [BOOK Wildermuth p.161–181] — D
- Low prices are not accidents: a cheap stock is cheap for a reason, a low price is itself a danger signal, and a loss-maker can liquidate, drift at breakeven or recover; only the third pays [BOOK Plotnick p.23–25] — D
- A low P/E on earnings that will not continue (a main product being phased out with no replacement) is not value [BOOK Plotnick p.56] — C
- Risk rises as information falls: prefer companies that report quarterly and promptly; an investor in an annual-only reporter is operating blind [BOOK Plotnick p.32–34] — C
- Prices discount expected earnings; rumoured good news is often sold when it arrives, and overdiscounted stocks fall faster than they rose [BOOK Plotnick p.37–39]; [BOOK Plotnick p.44–45] — C
- Don't snatch small profits: hold while the earnings trend holds; the reasons to sell are faltering company performance or a price far ahead of present and future performance [BOOK Plotnick p.47] — D
- Sell promptly when new adverse facts appear, even a week after buying; hoping to get even turns small losses into large ones and ties up money that could work elsewhere [BOOK Plotnick p.49–50]; [BOOK Plotnick p.172]; [BOOK Plotnick p.197] — D
- New-product and R&D announcements move prices fastest but many developments fail to develop; invest in the corporation's figures, not its press releases [BOOK Plotnick p.83]; [BOOK Plotnick p.87] — C
- Acquisitions inflate sales and digestion is often costly; expansion outside the company's field is a risk that calls for a strong acquirer balance sheet [BOOK Plotnick p.83–84]; [BOOK Plotnick p.105]; agrees [BOOK Martin p.199] (most acquisitions destroy value; good ones are small, in the core, bought with a price cushion) — C
- Heavy government involvement (antitrust suits, investigations, price-fixing charges) usually depresses a stock for a long time; settlement of a large suit can create a bargain [BOOK Plotnick p.85–86] — C (1960s cases)
- Industry-wide adversity is a sell reason even when the company is sound, and a depressed industry tends to keep all its stocks depressed [BOOK Plotnick p.175]; [BOOK Plotnick p.198] — C
- A promising stock that is not yet ripe goes on a watch list and is re-checked at each quarterly report; most investigations should end early [BOOK Plotnick p.151]; [BOOK Plotnick p.197] — D
- A typical recovery stock takes about two years to come to fruition; patience is needed after purchase (author estimate) [BOOK Plotnick p.173]; [BOOK Plotnick p.167] — D
- Don't fix target prices; a fixed dream price blinds you to the company's actual performance [BOOK Plotnick p.197] — D
- Don't disqualify a sound, well-rated company for having already risen; be strict only with stocks emerging from losses [BOOK Plotnick p.198–199] — C
- A small account spread over many positions cannot gain meaningfully; concentrate in one or two well-researched names, with money not needed for living costs [BOOK Plotnick p.195–196] — D (in tension with the desk's position-count and tier rules, which govern)
- Charts are a tool, not a machine: price and volume patterns reflect fundamentals and can refine timing, but used alone they are dangerous [BOOK Plotnick p.58]; [BOOK Plotnick p.196–197] — D
- Forecasting sales from inventory build-ups needs about ten years of a steady inventory-to-sales pattern and is called extremely dangerous; rising inventory turnover is a useful efficiency signal [BOOK Plotnick p.202–203]; [BOOK Plotnick p.37] — D
- Taxes are secondary; don't let capital-gains tax hold you in a stock that should be sold (the desk flags tax questions, it doesn't answer them) [BOOK Plotnick p.188] — D
- Volatility is not risk; permanent loss is. Don't hedge the market (index puts were too expensive, loc.39); cash should build as a by-product of selling fully valued stocks [BOOK Wachenheim loc.6–8]; [BOOK Wachenheim loc.39]; agrees [BOOK Martin p.25] (Graham: risk is the chance of permanent loss); [BOOK Martin p.50–51] (Sharpe ratios built on short-term variability mislead long-term investors) — C
- Long-run market return ≈ nominal EPS growth about 6% + about 1% from buybacks and acquisitions + about 2.5% dividend ≈ 9–10% a year, 1960–2009 (no source shown) [BOOK Wachenheim loc.5–6] — B
- Behavioural edge: act before the all-clear signal, decide on probabilities, judge decisions rather than outcomes, and on dramatic news reread your pre-news notes and ask what really changed in value [BOOK Wachenheim loc.11–15]; agrees [BOOK Wachenheim loc.148] — D
- Avoid both weak cheap companies and high-P/E growth: growth fades (Whirlpool about 20% a year 1949–1961, then 8.7%; Nifty-Fifty about 42× in Dec 1972 before falls of 71–91% in Xerox, Avon, Polaroid) [BOOK Wachenheim loc.10]; [BOOK Wachenheim loc.93–94] — C
- Most wonderful businesses become less wonderful: sell when fully valued rather than hold forever (Coca-Cola 2003–2013 EPS +7.1% a year, price +4.9%) [BOOK Wachenheim loc.34] — C
- Screens rarely yield ideas: thousands run, a tiny fraction became investments; about 1% of companies studied enter the portfolio [BOOK Wachenheim loc.50]; [BOOK Wachenheim loc.56] — C
- A cheap stock in an unloved industry can stay cheap: U.S. Home doubled EPS yet stayed at 6–7× and was bought out at 6.6× after about six years, about 12% a year [BOOK Wachenheim loc.51–53] — C
- A sharp drop in input costs lifts margins temporarily because price cuts lag; a large-holder chairman sold Interstate into that spike [BOOK Wachenheim loc.46–47]; [BOOK Wachenheim loc.50] — C
- Revenue-recognition changes (lease-to-sale conversions, full-payout leases) can pull profits forward and flatter a trend (IBM 1980–1985) [BOOK Wachenheim loc.27–28] — C
- Commodity tightness rarely lasts outside cartels: high prices draw new supply and substitution; capex cases built on top-of-range prices are a warning [BOOK Wachenheim loc.100–101]; agrees [BOOK Wachenheim loc.148] — C
- Don't project margins above the company's past peak; models are directional — check a downside case too [BOOK Wachenheim loc.87–88] — C
- Discount management projections, especially for acquisitions; redo the arithmetic yourself [BOOK Wachenheim loc.43]; [BOOK Wachenheim loc.104]; agrees [BOOK Wachenheim loc.148] — C
- Directors see information management has prepared; weigh their reassurance lightly [BOOK Wachenheim loc.140] — C
- Counter-case to insider-buying rules: an AIG director bought 30,000 shares in August 2008, weeks before a near-total loss — insider buying does not protect against a liquidity crisis [BOOK Wachenheim loc.77] — C
- Read sell-side reports to learn the consensus, not to decide; author claims analysts are wrong more often than right, wait for proof, and downgrade fixable problems [BOOK Wachenheim loc.35]; [BOOK Wachenheim loc.69–71]; [BOOK Wachenheim loc.130] — C
- Don't base decisions on short-term market, economic, rate, commodity or currency forecasts; the author found such calls about a coin flip, his own oil call included [BOOK Wachenheim loc.89–90]; agrees [BOOK Wachenheim loc.148] — D
- A few big winners drive returns: if one holding in five triples in three years, the rest need only about 12% a year for a 20% portfolio; stay fully invested while holdings are reasonably priced, but hold cash rather than stretch [BOOK Wachenheim loc.102]; agrees [BOOK Wachenheim loc.148]; agrees [BOOK Martin p.42] (in a growth portfolio the winners control the return) — D
- Shorting is usually a poor business: it fights the market's long upward drift and has unlimited loss [BOOK Wachenheim loc.68] — D
- After a loss, ask whether you would make the same decision with what you knew then; tail events happen, but don't invest as if the 100-year storm is next [BOOK Wachenheim loc.79] — D
- When unsure whether to sell, sell a fraction [BOOK Wachenheim loc.131] — C
- A stop order gives no protection against an overnight gap: it fills at the first trade below it, e.g. a $45 stop filled near $20 after bad news; a long put keeps its floor at the strike (less the premium paid) [BOOK Broker p.187–188]; [BOOK Broker p.185] — D
- Collar: hold the shares, buy an out-of-the-money put and sell an out-of-the-money call with the same expiry and size, bounding both the loss and the gain [BOOK Broker p.209] — D
- Bought calls and puts need direction, size and timing all right: an option that expires before the move loses even when the view was correct [BOOK Broker p.203]; [BOOK Broker p.190] — D
- In an uptrend, a fresh high followed by repeated failures to exceed it can mark a reversal; counter-trend trades are for experienced traders and need a fast exit if the trend resumes [BOOK Broker p.266]; [BOOK Broker p.287] — D
- Set a trade's profit target from the size of its recent average swings [BOOK Broker p.258] — D
- Day trading removes overnight and weekend gap risk but costs more per period, caps the profit per setup and invites over-leverage; swing trades carry gap risk with wider room [BOOK Broker p.255–256]; [BOOK Broker p.287–288] — D
- The book cites Larry Connors' research that very short RSI periods (2–4) gave a better long-term edge than the standard 14, without method or sample [BOOK Broker p.278–279] — B
- Market-on-close order imbalances, tracked over 20–50 days by sector, are offered as a sign of institutional accumulation; the desk has no such data feed [BOOK Broker p.280] — D
- Any trading edge has a limited life: as others adopt the same tools it fades, so treat a published strategy as a starting point and keep re-checking it [BOOK LopezLira p.245]; [BOOK LopezLira p.295–297] (model obsolescence); agrees [BOOK LopezLira p.341–342] (seek gaps left by institutional constraints and information asymmetry) — D
- Mispricing lasts longest where large institutions can't trade — illiquid, small or mandate-excluded securities — and where some traders hold better data; trading costs there are higher [BOOK LopezLira p.246–248]; [BOOK LopezLira p.47]; [BOOK LopezLira p.256–257] — D
- Pick a rebalancing horizon from your own costs: too frequent and costs eat the gain; too long and you are no longer trading the signal [BOOK LopezLira p.257–258] — D
- Judge a backtest against a benchmark on return, volatility, Sharpe and maximum drawdown across several periods, and treat it as one indicator, not a forecast (overfitting) [BOOK LopezLira p.262–265]; [BOOK LopezLira p.66–68] — D
- When using an LLM for research: hand it the source text instead of asking it to recall or browse, ask one narrow, closed question, break long tasks into steps, and verify the output, since models invent statistics and backtests [BOOK LopezLira p.180–184]; [BOOK LopezLira p.134–135] — D
- Spreads widen in volatile markets, so market orders can fill outside the quote; prefer limit orders then [BOOK LopezLira p.290] — D
- Crowding: many systems reading the same news the same way can amplify moves and errors (including fake articles) through feedback loops, especially in illiquid names [BOOK LopezLira p.297–299]; [BOOK LopezLira p.272] — D
- Models trained on price history struggle because markets don't stay the same: investors adapt, so only recent data is relevant, and novel shocks break learned patterns; keep a human override [BOOK LopezLira p.98–100]; [BOOK LopezLira p.300–301]; agrees [BOOK LopezLira p.323] (models struggle with sudden shifts; AI feedback loops can amplify volatility) — D
- Academic finance is sceptical of technical analysis; where it works it may be self-fulfilling herding on popular signals [BOOK LopezLira p.53–54] — D
- Self-learning (reinforcement-learning) trading agents are hard to train on markets: fees, spreads, regime changes and sparse, delayed rewards mislead them, so they need hard constraints, shaped rewards and stress tests against extreme scenarios before real money [BOOK LopezLira p.311]; [BOOK LopezLira p.350] — D
- A leading stock's own price/volume buy signal outranks the index signal: leaders often break out before a market follow-through day (Iomega 1996, Lockheed 2001, silver 2011), every follow-through day in 2011 failed, and a 'foolproof' follow-through indicator would be overfit [BOOK MoralesKacher loc.36–42]; [BOOK MoralesKacher loc.190] — C
- When the market-direction signal turns to cash, cut first the weakest and most volatile holdings and halve positions carrying little profit cushion; screens get stricter while it is negative [BOOK MoralesKacher loc.75]; [BOOK MoralesKacher loc.77–78]; [BOOK MoralesKacher loc.174] — C (the authors' signal is a proprietary model)
- Leaders can keep rising for weeks or months after the market tops, so keep managing them on their own sell rules rather than selling on index action alone [BOOK MoralesKacher loc.151]; [BOOK MoralesKacher loc.37–40] — C
- Fewer, larger positions: holding more than about 20 names, or average positions under 10%, may be 'a hedge for ignorance' for this style; sell the laggard to fund a new buy signal in a stronger stock [BOOK MoralesKacher loc.19]; [BOOK MoralesKacher loc.26]; [BOOK MoralesKacher loc.163–164]; [BOOK MoralesKacher loc.181] — D
- Mean-reversion indicators (RSI, stochastics, Bollinger, MACD, overbought/oversold) fight trends and can shake a holder out early — silver's RSI was overbought before the biggest part of its 2011 run; they may suit only sideways markets [BOOK MoralesKacher loc.95–98]; [BOOK MoralesKacher loc.183] — C
- Price level is irrelevant; trend is what matters: rebuying higher than you sold is fine when a new trend starts (AAPL 2004 sold near $16, rebought near $24), and haggling over 50 cents misses a 50–100% move [BOOK MoralesKacher loc.50–52]; [BOOK MoralesKacher loc.173]; [BOOK MoralesKacher loc.184] — C
- Re-enter a stock on its next valid buy signal even right after being stopped out at a loss; refusing to rebuy after a loss is a frustration bias [BOOK MoralesKacher loc.54]; [BOOK MoralesKacher loc.128]; [BOOK MoralesKacher loc.159] — C
- Test the waters with a smaller-than-normal position in an uncertain setup and cut fast; expect many small losses and a few large gains — the authors put the hit rate near half or lower [BOOK MoralesKacher loc.47]; [BOOK MoralesKacher loc.173]; [BOOK MoralesKacher loc.190] — C
- Adjust size and pace to how wide the market's 'window of opportunity' is: in choppy years scale in slowly and trade less; the authors say the 2000s offered big money only two to three months a year [BOOK MoralesKacher loc.59–60]; [BOOK MoralesKacher loc.67]; [BOOK MoralesKacher loc.79–81] — C
- Late-stage bases (a fourth base or later, or a breakout more than a year into a run) fail more often, but the strongest leaders can still make climax runs from them; judge by price/volume, not base count alone [BOOK MoralesKacher loc.159]; [BOOK MoralesKacher loc.187] — D
- Success bias: a big win in one stock or theme makes you over-concentrate in it later (silver over gold, July 2011); approach each trade fresh [BOOK MoralesKacher loc.72] — C
- Paper trading teaches mechanics but not emotions; start real trading with about 10% of the intended capital and watch for euphoria, discouragement, anger and frustration [BOOK MoralesKacher loc.53–55] — D
- Judge any timing model before trusting it: at least 20 years of results across different eras, internal logic before optimisation, annual return since a hard period, number of switches a year (75–100+ means cost drag), mid-stream rule changes, and live versus theoretical history; ignore total return [BOOK MoralesKacher loc.194–197] — D
- Author claims: 18,000% in their prior book's title [BOOK MoralesKacher loc.3]; a 'mid-double-digit' 2011 return [BOOK MoralesKacher loc.37]; a market-direction model returning +32.55% a year since 1974 [BOOK MoralesKacher loc.195] (+33.1% on the next page [BOOK MoralesKacher loc.196]) with a −15.7% worst drawdown — unaudited, rules undisclosed; both authors sell an advisory service [BOOK MoralesKacher loc.6]; [BOOK MoralesKacher loc.198] — D
- Computers spotted too many bases when the authors' 1998 O'Neil project tried to automate base recognition; chart reading needed judgement [BOOK MoralesKacher loc.189] — C
- Use mental stops trailed on moving averages; if placing physical stops, set them a few cents under round numbers and at logical levels with a 1–2% cushion [BOOK MoralesKacher loc.178–179] — D
- 'Value' is a purchasing style, not an investing style: analyse the business independently of its price, then buy with a margin of safety; growth companies can be bought this way, substituting conservative future earnings for the past record [BOOK Martin p.20–22]; [BOOK Martin p.23] — D
- Buy discipline matters more than sell discipline: buy as if you had to hold for 30 years, and never buy what you don't intend to hold indefinitely [BOOK Martin p.102]; [BOOK Martin p.286] — D
- Value companies (growing slower than average) must be bought below intrinsic value and need the gap to close quickly; growth companies can be bought at fair value or less because the value compounds ($10 value, 50% payout: buying at $8 gives about 8.6% a year, at $12 about 2.5%, assuming 10-year convergence) [BOOK Martin p.33–34]; [BOOK Martin p.37] — D
- Value trap ('concrete rowboat'): a sound mature company bought at a discount can slowly squander capital (GM to its 2009 bankruptcy; Kodak's ~$15bn of failed acquisitions; Legg Mason Value Trust −77% in 2007–09) [BOOK Martin p.38–39] — C
- Set the target return about 2 points above the return you need: one −50% year or one flat decade in 50 years cuts 9% compounded to about 7% [BOOK Martin p.45–47]; [BOOK Martin p.108] — D
- Graham's reprinted 1962 evidence: recommended growth-stock portfolios (1939–46 lists, held to 1955) gained 307% vs 315% for the Dow; 24 selected growth stocks returned about 13% a year in 1946–57 vs 13.4% for the S&P 425; growth funds averaged 289% in 1951–60 vs 322% for the S&P 500 — picking on expected growth alone has not beaten the market [BOOK Martin p.93–94] — B
- Graham's 1974 revision scales his formula by 4.4 ÷ the AAA corporate bond yield; the author advises against cutting multiples for rates without strong conviction that rates are entering a long rise (the AAA yield is not a connected input) [BOOK Martin p.74–75] — D
- Skip macro forecasting: a company's future value depends more on its management and industry than on the economy; a crisis usually marks the end of a problem and offers prices on companies already analysed (2008–09) [BOOK Martin p.80–81]; [BOOK Martin p.117–118] — D
- Industry growth is not shareholder profit: airline revenue rose from $135m to $2.9bn in 1941–60 with meagre profits, and the industry lost $39.6bn in 1971–2009 while Southwest earned $6.6bn; look for a structural advantage (barriers to entry or customer captivity) [BOOK Martin p.149–150]; [BOOK Martin p.153] — C
- Signs of a structural advantage: high and stable market share, steady share gains, few entries and exits, persistent pricing power, operating margins well above direct competitors, low churn and repeat purchases, brand extensions, long product cycles; a hot product, a celebrity CEO or efficient execution alone is not one (Crocs, Sunbeam, grocers vs Walmart) [BOOK Martin p.174]; [BOOK Martin p.179–180] — C
- Advantages usually erode through management neglect or distraction over years rather than sudden attack; watch for diversification away from the core [BOOK Martin p.181]; [BOOK Martin p.182–183] — D
- Be sceptical of markets that exist mainly by government mandate (ethanol), as opposed to organic demand that a subsidy merely funds [BOOK Martin p.187–188] — D
- Accept high financial risk only with low operational risk, and vice versa: McLeodUSA combined debt with a national data-network build-out, missed the author's cash-flow forecast by 55% and was sold at about $0.50 after purchases at $13–15 [BOOK Martin p.229–231] — C
- The hardest time to hold is after a 50–100% gain: the author sold Dell (c.1993) at about +200% on quality and financing worries while its direct-sales edge was intact, never rebought, and missed a rise of 100-fold or more [BOOK Martin p.267–269] — C
- The author's stop-loss orders were triggered in a 1973 dip that quickly recovered; he has not used stops on long-term holdings since [BOOK Martin p.278] — C
- Own individually only as many stocks as you can compute a margin of safety for (perhaps four or five) and hold the rest in a low-fee S&P 500 index fund (e.g. 75/25), shifting as you find more [BOOK Martin p.133]; [BOOK Martin p.274] — D
- Turnover above 100% a year is trading, not investing, and leaves no time to work out a margin of safety for each name; a 1.5% annual fee roughly halves 50-year wealth at 10% gross [BOOK Martin p.262–263]; [BOOK Martin p.280] — D
- Keep a fixed, absolute hurdle rate: a benchmark-relative standard loosens as markets rise; expect stretches of lagging the index (the author's firm lost clients in 1999–2000) [BOOK Martin p.143–144]; [BOOK Martin p.258] — C
- Growth-stock values are more sensitive to the growth estimate (a 25% cut in growth lowers the Graham value about 8% at 2% growth but about 18% at 10%), so growth stocks swing more and offer more entry points [BOOK Martin p.118–119] — D
- Buy large blocks in small lots over time; the author saw prices jump on his large orders (front-running) and pulled them [BOOK Martin p.264–265] — C
- Author claims (in a client's foreword) a pension account he managed from 1980 to April 2011 compounded 13.8% a year (stocks 16.1%) vs 11.4% for the S&P 500 [BOOK Martin p.12]; unaudited — C
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
- Return dispersion across stocks dwarfs the market's own move: in the author's Stanford class sample (all 140 NYSE common stocks starting with A or T, utilities and preferreds excluded, end-1956 to 13 Oct 1961, Dow +41%), 27% lost money and 4% lost over half; the five best turned $10,000 into $70,260 and the five worst into $3,180; a repeat with two other letters gave a similar spread (figures not shown); table not converted [BOOK Fisher loc.253–254] (Part Three) — A (one small sample, one window; check table loc.254)
- Scuttlebutt: competitors, customers, vendors, research scientists, trade-association staff and former employees (check why they left) give a clear picture once enough views agree; promise and keep anonymity [BOOK Fisher loc.50–51]; Ken Fisher calls it a craft that takes years, built on follow-up questions [BOOK Fisher loc.4–8] (introduction) — D
- Visit management only after gathering about half the knowledge you need, introduced by a banker, customer or large holder; the author's funnel: about one buy per 2–2.5 companies visited, one per 40–50 looked at, one per ~250 considered [BOOK Fisher loc.170–172] (Part One) — C
- Drop an investigation when outside sources can't be reached: what matters is being right on the few buys, not having an answer on every company [BOOK Fisher loc.169] — D
- Source of ideas: the author's own review found about four-fifths of his investigations and five-sixths of his worthwhile buys started with a few able investment men, about one-fifth and one-sixth with executives and scientists; public brokerage bulletins are a poor source [BOOK Fisher loc.166–168] (Part One) — C
- First read of a prospect: SEC prospectus/proxy for sales by product line, competition, officer ownership, depreciation, margins, R&D and nonrecurring costs, not years of old balance sheets [BOOK Fisher loc.169] — D
- Don't time buys or sells on economic or market forecasts, except in rare manic years like 1928–29 (the author guesses about one year in ten); he puts his short-term calls at about 60% right against about 90% for spotting outstanding companies [BOOK Fisher loc.92]; [BOOK Fisher loc.105]; [BOOK Fisher loc.246–247] — D; agrees [BOOK Wachenheim loc.89–90]; agrees [BOOK Martin p.80–81]
- A low P/E guarantees nothing and often flags weakness: the author's 1929 buys of low-P/E locomotive, billboard and taxi stocks were nearly wiped out by 1932; judge price against earnings a few years ahead [BOOK Fisher loc.221–222] (Part Three) — C (see Conflicts vs R-101)
- Former price ranges have little bearing on value; buying the stock that "hasn't gone up yet" assumes all stocks rise alike [BOOK Fisher loc.149–150]; [BOOK Fisher loc.213] — D
- Past five years' EPS is a secondary tool, useful for cyclicality and as a P/E base; even the best growers have one- to three-year dips [BOOK Fisher loc.151]; [BOOK Fisher loc.155] — D
- Sales growth should be judged in blocks of several years: research and launches make it come in uneven spurts [BOOK Fisher loc.53] — D
- A stock's moves against the market come from a changed appraisal by the financial community; the biggest gains combine rising EPS with a rising P/E (the book's G company: EPS $1 to $1.82 and P/E 10 to 22 took the price from $10 to $40) [BOOK Fisher loc.200–202] (Part Two) — D
- Price blends three appraisals (market, industry, company); industries re-rate when the emphasis shifts, not the facts (chemicals 1950s vs 1960s, computer peripherals 1969, franchising 1969–72, A. C. Nielsen 1958) [BOOK Fisher loc.205–208] (Part Two) — C
- In falling markets a worse image is accepted faster than a better one: Motorola jumped about 25% on selling its TV business in March 1974, then gave it back as rates rose [BOOK Fisher loc.212] (Part Two) — C
- Improvement by little-known executives re-rates slowly; a famous new president makes the stock over-react at first [BOOK Fisher loc.164] (Part One) — D
- Going against the crowd pays only when you are very sure you are right (buying streetcar stocks just because they were unloved would have been costly) [BOOK Fisher loc.230–231] (Part Three) — D; agrees [BOOK Regan loc.21]
- Market-wide misjudgements recur: the 1927–29 "new era"; 1946–49, when good earnings were dismissed in expectation of a post-war crash and companies were "worth more dead than alive" around 1949; 1972–74 [BOOK Fisher loc.159]; [BOOK Fisher loc.213–214]; [BOOK Fisher loc.241–242] — C
- Interest rates set the general level of stocks (high rates pull money away); new-issue volume follows the market more than it leads it [BOOK Fisher loc.215] (Part Two) — D (in tension with the principle that heavy issuance precedes weak returns [BOOK Zacks loc.60–61])
- For long-term holders, bonds lose real value under the post-1932 inflation bias: 16 countries' money lost value 1946–56 (US −29%, 3.4% a year against a 2.19% Treasury yield) per a First National City Bank letter of Dec 1956 [BOOK Fisher loc.46–48] (Part One) — B (one decade; era-bound)
- In-and-out trading: the author profited three times trading California Packing in the 1930s, judged the gains trivial next to long holds and riskier, and stopped after WWII [BOOK Fisher loc.236]; [BOOK Fisher loc.248–249] — C; agrees [BOOK Wyckoff p.132–133]
- Ego is the costliest habit: holding until "at least even"; review every loss for its lesson; take small losses and let big profits run, never take a profit just to take one [BOOK Fisher loc.109]; [BOOK Fisher loc.260] — D; agrees [BOOK Anderson loc.56]
- Be most thorough when things are going well: a 1960s drug stock bought on one specialist's and one officer's word fell over 50%, and later complacency at "Central California Electronics" missed management decline [BOOK Fisher loc.243–244]; [BOOK Fisher loc.248] (Part Three) — C
- Don't pay a hot market's entry price for real promise: a 1969 equipment company grew for years but was sold near cost [BOOK Fisher loc.244–245] (Part Three) — C
- Stay inside your competence: the author's results outside industrial and technology manufacturing (consumer products, real estate) disappointed him [BOOK Fisher loc.216]; [BOOK Fisher loc.245–246] (Part Three) — C
- A large company relying mainly on patents for its margin is weak; for a small young company the patent position matters, though steady engineering leadership protects better [BOOK Fisher loc.76–77] (Part One) — C
- Labour and people signals: turnover and applicant waiting lists against local employers, above-area wages paid out of above-average profits, quick grievance handling; Texas Instruments' sales ÷ payroll index rose from about 2.25 to 2.5 over 1969–73 [BOOK Fisher loc.71]; [BOOK Fisher loc.188–190] — C
- Management depth becomes necessary once sales reach somewhere between $15 and $40 million (1958 dollars): delegation, merit promotion, openness to criticism; promotion from within is the norm [BOOK Fisher loc.72–73]; [BOOK Fisher loc.183–184] — D
- Research takes seven to eleven years to pay off; crash programmes and stop-start budgets raise its cost; government-funded research is worth what transfers to commercial lines [BOOK Fisher loc.43]; [BOOK Fisher loc.61–63] — D
- For a top-quality company, financial structure matters little if cash plus prudent borrowing covers several years; never buy a weak company for its cash [BOOK Fisher loc.78–79] — D
- Retained earnings help holders only if reinvested well; under inflation, depreciation doesn't cover replacement, which hurts fast-growing firms less [BOOK Fisher loc.118–119] — D
- Steady dividend policy wins a following; one-off extra dividends leave no lasting mark on the price [BOOK Fisher loc.123–124] — D
- A low-cost producer survives price wars, takes share from closing rivals and funds growth itself; high-cost firms' profits jump more in booms and fall harder after (the widget arithmetic) [BOOK Fisher loc.66]; [BOOK Fisher loc.178] — D
- High margins draw competitors; the lasting defences are efficiency, multidisciplinary technology and specialised niches with many small customers for whom the product is critical but cheap [BOOK Fisher loc.194]; [BOOK Fisher loc.197–198]; [BOOK Fisher loc.199] (ask what the company can do that others can't) — D; agrees [BOOK Martin p.174] (signs of a structural advantage, incl. operating margins well above direct competitors)
- Don't buy on an annual report's tone, photos or charts [BOOK Fisher loc.132] — D
- Over-the-counter stocks with two or more high-grade dealers can be liquid enough (describes 1950s market structure) [BOOK Fisher loc.130–132] — D
- The author's view that over about five years a statistical bargain hunter makes a small fraction of what growth-company appraisal makes [BOOK Fisher loc.82–83] — D
- Pick an adviser on at least five years of results against the market, checked for style (bond-heavy in falls, marginal companies in rises, market guessing) [BOOK Fisher loc.85–86] — D; agrees [BOOK Gibbs loc.86–87]
- Invest only true surplus funds, after an emergency reserve and money set aside for specific needs [BOOK Fisher loc.89] — D
- Efficient-market theory fails the diligent long-term investor: Raychem's frank January 1978 meeting moved the stock not at all, though it more than doubled from $23¼ over the next year or two [BOOK Fisher loc.252–253]; [BOOK Fisher loc.258–259] (Part Three) — C
- Ken Fisher: stop making investment decisions before you grow old; his father's late-life sales of FMC, Texas Instruments and Raychem were consistently badly timed [BOOK Fisher loc.23–24] (introduction) — C
- Ken Fisher: a falling market is the time to swap the weakest holding for a better company, not to sell out [BOOK Fisher loc.12] (introduction) — D
- Ken Fisher claims the fifteen points and scuttlebutt would have kept investors out of Enron, Tyco, WorldCom and the 2000–02 "95 percent club" [BOOK Fisher loc.4]; [BOOK Fisher loc.6] (introduction) — D

## Ingest log
| Date | Book | Read | Rules added | Merged | Principles | Flags |
|---|---|---|---|---|---|---|
| 2026-11-09 | Chhibber | p.5/5 | 0 | 0 | 1 | no rules: accuracy figure inconsistent (p.1 vs p.4); dataset is startup/Crunchbase data, not price series (p.2) |
| 2026-11-09 | Pansheriya | loc.24/24 | 8 swing-technical + 2 risk/sizing (all D) | 0 | 6 | no tests; hypothetical prices |
| 2026-11-09 | Salvon | loc.24/24 | 7 day-trading (6 C, 1 D) | 2 (risk cap, 2R) | 6 new + 3 agreements | forex/crypto focus; intraday rules recorded only; broker promo; unsourced turnover table loc.12 |
| 2026-11-09 | Yardeni | p.31/31 | 1 value (B) | 0 | 9 | market-level (S&P 500) only; forward-EPS input not connected yet; table pages 2, 25–27, 30 |
| 2026-11-09 | Mourya | p.19/19 | 0 | 0 | 2 | no rules: tests distribution fit (KL divergence), not trading; authors concede classical models outperform |
| 2026-11-09 | Baumgartner | p.52/53 | 1 process (A) | 0 | 2 | grade A covers the settlement-day anomaly, not a trading rule; table page 3 |
| 2026-11-09 | Regan | loc.34/34 | 6 (risk/sizing 4, process 1, swing-technical 1; all D) | 5 | 9 | sales pitch for a paid course; winners-only screenshots; penny-stock focus |
| 2026-11-09 | MetaStock | p.42/42 | 7 (swing-technical 4, risk/sizing 2, process 1; C 3, D 4) | 2 (R-009, R-022) | 9 | vendor booklet of eight short essays; chart examples only; table page 3 |
| 2026-11-09 | Hammond | loc.40/40 | 1 value (D) | 0 | 4 | beginner primer; PEG example miscalculated (loc.24); broker list dated; personal-finance and real-estate chapters outside desk scope |
| 2026-11-10 | Cayman | loc.61/61 | 10 (options-directional 3, options-income 1, swing-technical 2, growth/momentum 2, risk/sizing 1, day-trading 1; all D) | 1 (R-022) | 11 new + 5 agreements | machine-spun text; no tests or real trades; garbled leverage and arbitrage examples ignored (loc.42–43, 50); tax claim flagged, not used (loc.31); read in chat after the scheduled run failed |
| 2026-11-10 | Heitkoetter | loc.69/69 | 6 (swing-technical 1, options-directional 1, risk/sizing 3, process 1; C 3, D 3) | 5 (R-009, R-010, R-023, R-034, R-040) | 10 new + 3 agreements | vendor book selling software and coaching; hypothetical-performance disclaimer (loc.2); chart examples only; growth figures are projections; tax remarks not carried (loc.56) |
| 2026-11-10 | Piard | loc.74/74 | 10 (growth/momentum 4, risk/sizing 2, value 2, process 2; A 9, D 1) | 3 (R-027, R-028, R-043) | 14 new + 1 agreement | first book with systematic tests; all results are simulations (CFTC 4.41 note, loc.2); test windows 1999–2013, some under 10 years; the Treasury legs gained from a 2011 bond surge (loc.42); ETF tickers generalised to asset classes |
| 2026-11-11 | Anderson | loc.71/71 | 3 (value 2, risk/sizing 1; C 1, D 2) | 4 (R-009, R-022, R-033, R-043) | 11 new + 3 agreements | spun/translated text (loc.11–18, 43–51); binary-option and CFD broker promotion (loc.3–5, 10) not carried; promotional claims for the author's other books not carried (loc.68, 70); garbled intraday 'tick' passage ignored (loc.63–64); asset-allocation-by-age rule out of desk scope (loc.24) |
| 2026-11-11 | EDay | loc.88/88 | 9 (swing-technical 6, growth/momentum 1, risk/sizing 1, options-directional 1; C 2, D 7) | 7 (R-005, R-007, R-009, R-027, R-030, R-048, R-049) | 14 new + 3 agreements | beginner book by an FX trader; most examples from one stock's hourly chart (Dec 2019–Feb 2020, hindsight); FX, carry and broker chapters out of scope (loc.10–14, 29–31); PDT workaround via FX not carried (loc.24–25); one stop placement in the text looks reversed and was not carried (loc.52); book promotion loc.87–88 |
| 2026-11-11 | FreemanCS | loc.87/87 | 9 (options-income 8, risk/sizing 1; A 1, B 2, C 2, D 4) | 3 (R-023, R-036, R-048) | 13 new + 2 agreements | publisher's credit-spread book; email-list bonus promotion (loc.2–3) not carried; one in-house backtest with width/costs missing (loc.52); outside backtest via a YouTube source (loc.65–70); internal inconsistencies flagged (ITM/OTM labels loc.15, 17; 50-day vs golden cross loc.52; buy-back price loc.71); reader testimonials not used as evidence (loc.85); 10%-per-trade sizing recorded but overridden by desk C7 |
| 2026-11-11 | Wyckoff | p.220/220 | 4 (risk/sizing 3, value 1; C 3, D 1) | 7 (R-010, R-022, R-026, R-048, R-049, R-050, R-069) | 19 new + 6 agreements | 1924 memoir by a magazine publisher; prices in points on 1910s–20s stocks, so add intervals and stops are test parameters; OCR noise on contents and figure pages; bond, convertible, bank-stock and mining-property chapters mostly out of desk scope (p.55–74, 84–91); leverage suggestion (buy twice, pay half on bank credit, p.61) not carried; Livermore and Keene practices are second-hand; table p.138 (oil supply graph) unreadable; read in chat |
| 2026-11-11 | Gibbs | loc.93/93 | 11 (value 4, risk/sizing 3, growth/momentum 2, day-trading 1, swing-technical 1; all D) | 5 (R-021, R-026, R-027, R-040, R-061) | 13 new + 16 agreements | penny-stock beginner book; title page names a second author and the body title differs (loc.1–3); contradicts itself on investing vs trading (loc.6–8 vs 43) and on technical analysis without fundamentals (loc.73–75); Enron miscast as a pump and dump (loc.43–45); worked P/S example inverted (loc.60); P/E section mixes revenue and earnings (loc.71); two volume floors, 100,000 vs 250,000 shares (loc.24, 59, 85); OTC tier names dated (loc.17–19); 2019 broker commissions and sign-up offers not carried (loc.31–35); intraday breakout recorded only; read in chat |
| 2026-11-11 | Zacks | loc.116/116 | 14 (value 7, growth/momentum 5, risk/sizing 1, process 1; A 1, B 13) | 4 (R-033, R-042, R-054, R-087) | 10 new + 11 agreements | practitioner summary of academic studies (Handbook of Equity Market Anomalies, 2011); results mostly long-short and before costs, without sample sizes, so graded B; several anomalies faded after publication; the author's firm sells the estimate and recommendation data the book favours; 2011 market forecasts not carried (loc.6, 61); January-barometer text rounds 87% to roughly 80% (loc.99–100); political and party effects not carried (loc.104–105); Exhibit 3.1 table read as text (loc.37); duplicated paragraphs in the ebook; read in chat |
| 2026-11-12 | Ramnarayanan | p.188/188 | 13 (value 11, process 1, risk/sizing 1; B 0, C 9, D 4) | 2 (R-060, R-106) | 15 | Indian practitioner; examples from unnamed Indian companies at the time of writing (one named, HSIL p.79–82), INR figures; implied-growth tables p.122–123 not in text; survey of other authors' methods (p.21–24) second-hand, not carried as rules; leverage, tax and SEBI remarks not carried; Buffett letter extracts not quoted |
| 2026-11-12 | Trefz | p.191/191 | 1 (value; A 1) | 1 (R-058) | 5 | doctoral thesis (three papers); academic regressions, not trading advice; short-interest result in-sample 1999–2019, before costs; Covid and ESG papers cover one episode (2018–2020 weekly data); table pages 60, 64–65, 69, 159, 162, 176–177 omitted in conversion (check table); spillover tables summarised, not carried; policy view on ESG regulation not carried |
| 2026-11-12 | Damodaran | p.264/264 | 14 (value 11, growth/momentum 2, process 1; B 1, C 9, D 4) | 4 (R-087, R-110, R-112, R-117) | 16 | academic author's primer; worked cases at single dates (2008–2009), no outcomes; OCR noise on chapter titles; table pages 116, 139, 175 omitted (check table); 10 rules for the road recorded as principles' spirit only, not copied |
| 2026-11-12 | Snow | loc.125/125 | 5 (value 2, risk/sizing 2, swing-technical 1; all D) | 7 (R-005, R-007, R-022, R-025, R-060, R-062, R-083) | 12 | beginner compilation built largely from quoted advisers and outside articles; ticker list for 2022 (loc.95–107) not carried as picks, only its screen; PDT workarounds (loc.71) not carried; tax, retirement-account, age-based allocation and robo-advisor chapters out of desk scope; inconsistent emergency-fund advice (loc.28 vs 54); S&P 500 P/E history and Morningstar best/worst-day figures garbled (loc.35, 81); day-trading chapter recorded only |
| 2026-11-13 | FreemanCC | loc.119/119 | 11 (options-income 10, risk/sizing 1; C 2, D 9) | 2 (R-048, R-076) | 12 | publisher's beginner book; title and text call covered calls risk-free (loc.1, 26, 60) — not carried; email-bonus and YouTube promotion not carried; chain quiz swaps bid and ask (loc.32–33); several worked-number errors (Disney yield on cost basis loc.44; AT&T return loc.85; roll P&L loc.93–94; SPY diagonal loc.100); Thales called the founder of Stoicism (loc.9); IRA and tax chapters out of desk scope (loc.40, 55–57, 101–105); Aug 2020 candidates named on charts, no outcomes; S&P covered-call chart not converted (loc.62) |
| 2026-11-13 | Osman | loc.127/127 | 6 (value 4, risk/sizing 2; all C) | 6 (R-022, R-089, R-097, R-105, R-107, R-152) | 13 | practitioner book by the founder of a spin-off research firm that sells this research (loc.2, 55, 114); outperformance claims for spin-offs (over 10% a year; ~35% acquired within about two years) cite no study or method; several factual errors in examples (spin-off list loc.67; Darden and Evergrande proxy dates loc.70; VMware called a carve-out loc.77; Trane RMT garbled loc.73; Martha Stewart sale dated 2004 at loc.83 vs 2001 at loc.53); author's own calls (Pfizer 2020, Varex 2019) are winner-picked; rebased charts not converted; 2023–2024 market commentary and bank forecasts not carried; shorting chapter recorded as principles only |
| 2026-11-13 | Walsh | loc.122/122 | 11 (day-trading 8, risk/sizing 2, swing-technical 1; C 4, D 7) | 15 (R-001, R-002, R-003, R-004, R-005, R-007, R-009, R-010, R-012, R-017, R-039, R-047, R-048, R-049, R-069) | 11 | intraday day-trading book: 8 rules recorded only (desk can't call intraday; tape and breadth inputs not connected); all trade examples author-selected (about ten winners, one 7-cent loser) with no tally, sample or period; author claims ~70%/85% gap-fill rates without a source (loc.82); customer income testimonials (loc.1–2); news items fictitious (loc.77); arithmetic errors (target $55.05 vs sold $56.05, loc.53; exercise 5 entry $29.95 vs stop $23.05 and fill $22.85, loc.115–116); dated market-structure notes (loc.71–74); illustrations not converted |
| 2026-11-13 | Fridson | loc.138/138 | 5 (growth/momentum 3, value 1, risk/sizing 1; B 4, D 1) | 5 (R-097, R-104, R-131, R-136, R-154) | 14 | screen built from 10 winners (2012–2021) vs the #250 stock: no hit rate or false-positive count; Figures 4.1–4.4 not converted; check table loc.119 (Table 4.2 credit ratios missing); Table 5.1 inconsistencies (NVDA 1.465× vs stated 1.5× floor; date labels a year later than 'day before'); 2008 #1 return given as 38% (loc.102) and 36% (loc.121); rejected-method test results stated without numbers; author owns TSLA |
| 2026-11-13 | Wildermuth | p.184/184 | 5 (value 3, growth/momentum 1, risk/sizing 1; B 3, C 1, D 1) | 1 (R-101) | 15 | 2002 book for retail investors by an adviser who sells advisory and index-annuity services (p.121–132, 166–170, 184); much of it is out of desk scope (mutual-fund, retirement, annuity and adviser chapters recorded only); year-by-year Dow table omitted, check table p.91; Dow-dividend and Value Line results are backtests reported by outside sources, not independent (Nike Securities/Hirsch, Value Line's own record); the Kalos test is the author's own on a hand-picked universe, a trademarked product; the Value Line rule needs a paid feed the desk lacks; the 96% day-trader figure is unsourced by the author's own account; the 'asset allocation explains over 90%' and written-plan 3%/97% figures are unsourced; the S&P comparison at p.36 is garbled ('104 funds or 87%') |
| 2026-11-13 | Plotnick | p.214/214 | 12 (value 9, risk/sizing 1, process 2; C 9, D 3) | 4 (R-027, R-092, R-104, R-138) | 18 | 1964 book: all cases 1955–1962, winner-picked and hindsight, no tally or test; prices, 52% corporate tax rate, exchange/OTC disclosure rules and sources (S&P Stock Guide, Moody's) dated, not carried as current fact; the authors' own checked projection overshot EPS by about 30% (p.135 vs p.144); OCR'd scan with garbled image pages; check table p.142, p.157 |
| 2026-11-14 | Wachenheim | loc.152/152 | 15 (value 12, growth/momentum 1, risk/sizing 1, process 1; B 1, C 13, D 1) | 8 (R-027, R-060, R-083, R-105, R-106, R-112, R-131, R-154) | 20 | fund manager's memoir of 11 cases (1985–2014) told in hindsight, details reconstructed from memory and some names changed (loc.4); fund returns are author claims, unaudited (19% a year over 25 years loc.8; yearly figures loc.78, 97); winners and losers both shown (AIG, Praxair, U.S. Home) but no tally; tax-loss-selling view out of desk scope (loc.62–63); speculative genetic theory of herding not carried (loc.95–96); Buffett and other quotations not reproduced; biography and history chapters have no rules |
| 2026-11-16 | Broker | p.290/290 | 5 (swing-technical 2, options-income 2, day-trading 1; all D) | 12 (R-002, R-005, R-009, R-017, R-022, R-026, R-034, R-039, R-045, R-049, R-076, R-142) | 8 new + 7 agreements | 4-in-1 self-published compilation (2020) despite the title: no machine-learning or algorithmic-trading content; p.3–177 are Python programming (no rules); options section (p.179–233) and day/swing section (p.234–290) are spun, partly garbled text; errors not carried: options called low risk and 'safer' than stocks (p.181, 187), most listed options called European (p.191–192), delta read as a chance of expiring (p.192), bear call described as a bullish trade (p.208), covered call/put confused (p.222), collar and broken-wing examples inconsistent (p.209–211), day trading said to lose less than swing trading (p.237–238) against its own SEC quote and p.242; Everhart, Bischoff, Elder, Connors, Brown and OTA material is second-hand; income claims (p.220), 2020 broker lists and Admiral Markets/MetaTrader and binary-option/copy-trading promotion (p.196, 200–201, 269–273, 290) not carried; pages p.23, 46–47, 49–50, 59–61, 76–78, 147, 149, 151 missing from the conversion (programming pages) |
| 2026-11-16 | LopezLira | p.305/477 (partial) | 4 (risk/sizing 2, day-trading 1, growth/momentum 1; B 1, D 3) | 2 (R-040, R-200) | 9 new + 1 agreement | second run of 2026-11-16: day budget left after Broker ≈51,700 words, so stopped at p.305 (end of Ch.8), resume p.306 (Ch.9–10, appendix answers, references); Ch.1–5 are a finance/AI/LLM primer with no rules; the study is the author's own (with Y. Tang): headline return given as over 400% in about 18 months (p.19–20) and 550% Oct 2021–Dec 2022 before costs (p.233); no observation counts or significance figures in the text; the text read does not discuss whether model training data overlapped the test window; Ch.7–8 backtest (p.264) and risk scenario outcome (p.288) are hypothetical; short-sale example arithmetic garbled (p.64); LLM landscape dated 2023 (p.157–161); prompt not reproduced |
| 2026-11-18 | LopezLira | p.306–477 (now p.477/477, done) | 0 | 4 (R-213, R-214, R-215, R-216) | 1 new + 2 agreements | completion run: Ch.9–10 are forward-looking commentary (RL agents, blockchain/IoT, personalisation, regulation) with no rules; appendix answers restate earlier chapters; p.382 adds the study's cost sensitivity (notable returns at up to 25 bps per trade, eroded at higher costs); p.385 states a 2% per-position cap; the study is the author's own SSRN working paper (p.397) and the author's bio cites its prize (p.401); index and references p.396–477 have no rules |
| 2026-11-18 | MoralesKacher | loc.209/209 | 11 (growth/momentum 6, risk/sizing 4, swing-technical 1; C 7, D 4) | 10 (R-004, R-009, R-020, R-022, R-046, R-065, R-069, R-081, R-082, R-142) | 16 | O'Neil-style practitioners' workbook (2012); authors sell an advisory website and cite their own '18,000%' and a proprietary market model (+32.55% vs +33.1% a year, loc.195–196) — author claims, rules undisclosed; pocket-pivot back-test 'to the 1920s' claimed with no sample or results (loc.167), so nothing above C; examples are hand-marked chart exercises in hindsight, with some failures shown but no tally; buyable gap-up leeway given as 2–3%, 1–3% and 1–2% (loc.12, 101, 131); O'Neil's 7–8% rule and 30–60% ownership are second-hand; 2× leveraged ETF and margin use not carried; QE commentary dated; charts not converted (figure placeholders only) |
| 2026-11-18 | Martin | p.312/312 | 6 (value 3, process 1, risk/sizing 1, growth/momentum 1; B 1, C 3, D 2) | 9 (R-083, R-101, R-111, R-112, R-119, R-120, R-130, R-137, R-177) | 21 new + 4 agreements | second run of 2026-11-18; DGI practitioner book (2012) by a firm selling the method; Ch.3 reprints Graham's 1962 Security Analysis ch.39; Ch.7 cases (Apple, Ralph Lauren, Plexus, Middleby, McLeodUSA) are the firm's own trades told in hindsight, one loss shown, no tally; client-foreword returns are unaudited claims; the Appendix promised at p.73 (Graham formula vs DCF) contains no comparison; Ch.6 company tables omitted (check table p.157, 159, 161, 164–165, 167–168, 172, 175); ROIC quintile chart p.178 partly garbled; OCR noise on cover, figure and blank pages; tax remarks not carried; Ch.8 industry critique recorded as principles only |
| 2026-11-19 | Smith | p.321/321 | 20 (options-directional 9, options-income 9, process 2; C 3, D 17) | 5 (R-009, R-034, R-148, R-151, R-209) | 26 new + 9 agreements | Wiley practitioner textbook (2008); author promotes his Investment Mentoring Institute (plan form p.307), CTCR journal (p.301) and a book website (p.321); author claims a strategy that should make about 65% a year nets about 45% after costs (p.31), 1970s accounts at 200%/100% a year (p.288) and only one near-losing year in 30 (p.301); 90% figure unsourced (p.287); informal >80% plan study with no sample (p.304); Donchian claim unsourced (p.289); nearly all examples hypothetical (Widget, OEX, MMI) at fractional prices; real cases only IBM IV charts (p.81–82, 91–99) and T-bond IV (p.266); table page 262 omitted (check table: straddle/strangle option charts); futures-specific margin, T-bond 64ths and FX phi material out of desk scope; errors not carried: Fig. 6.8 butterfly rows contradict Ch.17 (p.100 vs p.222–225), 70% expire worthless repeated (p.127, 163) against p.21, put profit called unlimited then limited (p.115), put profit formula garbled (p.165), puts labelled calls (p.125, 167), covered-put roll example mixes strikes/'call' (p.182), break-even 'raised' on a credit roll (p.184), bear-spread text contradicts itself on decay and says 'bull' (p.213–214, 217), 'MMI at 350.50' (p.211), bull-spread rally table repeats the decline table (p.207), calendar 'sell a far contract' (p.240), Ch.20 header table copied from straddles (p.257), short-straddle example says 'buy' (p.264) |
| 2026-11-19 | Fisher | loc.267/267 | 19 (growth/momentum 13, process 4, risk/sizing 2; C 7, D 12) | 10 (R-087, R-113, R-129, R-130, R-158, R-198, R-199, R-204, R-230, R-233) | 43 new + 9 agreements | classic growth-stock book plus two later monographs: Part One 1958 (rev. 1960) loc.38–174, Part Two 1975 loc.175–215, Part Three 1980 loc.216–263, and Ken Fisher's 2003 preface/intro loc.3–37 (mostly biography); all examples 1929–1979 with unadjusted prices and dollar size thresholds (rescale $15–100m sales classes); case-based and winner-heavy, but the author reports misses (Mallory, Elox, the Cyanamid sale, a 1960s drug stock, a 1969 equipment company, "Central California Electronics"); the only systematic data is the Stanford dispersion sample, whose table was not converted (check table loc.254); likely conversion error in Raychem EPS "$.08 from $7.95" (loc.256); appendix OCR garble ("profitable" replaces "w", loc.261–263); stray editor notes (loc.23, loc.236); no product promotion; instructions.md not read (no Projects tool) |
