# FreemanCC notes (2026-11-13 run)
## loc.1-13
- loc.1-4 front matter, disclaimers, email-bonus promotion (not carried).
- loc.4-8 intro: covered calls pitched as "risk-free"/no extra risk vs owning stock (loc.7) - marketing claim, flag; cash-account OK, no PDT issue (loc.7). D.
- loc.9 factual error: Thales called founder of Stoicism (flag, not carried).
- loc.9-13 options history (Thales, tulip mania) - no rules. Principle candidate: option is a tool; tulip episode = speculation on a worthless underlying (loc.13) D.
## loc.14-26
- loc.14-19 options basics; no rules. Flags: claim that a fixed option price "will be honored no matter what" vs stop-loss gaps (loc.18) - true for a long put's strike, not for exiting an option at market; Peloton leverage example confused (loc.17).
- loc.19 principle: options leverage tempts over-sizing; beginners stick to simple structures (D).
- loc.23 time decay said to accelerate inside ~30 days to expiry (D) - feeds expiry choice.
- loc.20-26 terminology; calculation in loc.24 wrong (intrinsic $400/share x100 = $40,000 credit treated as profit on $5,000 premium paid per contract quote of $50 -> OK arithmetic, but strike-choice reasoning ad hoc). "covered calls essentially risk-free" repeated (loc.26) - flag.
## loc.27-39
- loc.27-29 writing puts/calls; Buffett put example (second-hand). Flags: says writing puts "not a consistent way" (loc.28) yet later calls cash-secured puts Level 1 (loc.29); naked-call levels; chain quiz answers swap bid/ask (loc.32-33: buy at "bid", sell at "ask") - flag, not carried.
- loc.31 principle: use the stock's own implied volatility (not the VIX) when writing calls on single stocks (D).
- loc.36 FXCM survey: 90% of traders blow accounts in a year (B, outside survey, forex) - context only.
- loc.37-38 principle: the "85% of options expire worthless" figure is a myth; author says ~35% expire worthless, ~60% closed early (cites Smith 2019; B-ish, no method). Sellers have an edge but don't expect casino-like win rates (B).
- loc.38-39 principle: writers win often but small; stick to rules; exit when the thesis changes, not on price (investor stance) (D).
## loc.40-52
- RULE cand. "Covered call only on a stock already held for its own long-term case, with a profit cushion" (loc.40, 43, 45): buy stock on normal investment principles; write calls when the position already has unrealized gain so assignment still profits; don't buy just to write. Inputs: cost basis (own records), price. D (hypothetical Disney example).
- Principle: don't write covered calls in IRA/retirement accounts (tax/penalty claim, loc.40) - tax, out of scope; flag only.
- RULE cand. strike/expiry basics (loc.42): write OTM call at a level the stock is unlikely to breach over ~a month; expiry beyond the last 30 days (i.e., >30 DTE) so you sell before the steep decay; ideally IV falling. D.
- loc.43-44 Disney example: $0.59 premium on $80 basis -> 0.73%/month, x12 = 8.85% "annualized" (computed on cost basis, not market value $12,800 - flag: yield overstated; on market value ~0.46%/mo). Cost-basis reduction framing.
- loc.45 assignment/exercise fees -> many close before expiry (D).
- loc.45-46 says covered call = same risk/reward as short put, yet tells reader to avoid writing puts (stance, D). Conflict with desk's cash-secured put logic; principle only.
- loc.46-47 max profit = (strike - cost) + premium; max loss = cost - premium; breakeven = cost - premium; dividends retained if owned at ex-date (loc.47). Principle D.
- loc.48-49 20-year compounding projections ($116,072; $1,597,034) - projections assuming 8%/yr premium + 10% stock; not evidence; flag.
- loc.49 S&P 500 2011-2019 avg 11.7% (figure 2) - context.
- loc.51 RULE cand: write calls when stock is range-bound (e.g. WMT $116-121 for 90 days, Choppiness Index noted) - sideways stock -> can write closer strikes (loc.52). C/D (single chart example, hindsight).
- loc.52 tax remarks (premium as income, REIT ROC) - out of scope, not carried.
## loc.53-65
- loc.53-55 index covered calls: European/cash-settled index options; writer advantage claim that European style lowers premiums (loc.54) - questionable reasoning, flag; ETF options American. Principle D.
- loc.55-57 IRA remarks - tax/account, out of scope.
- loc.57 buy-write (buy + write same time) called speculative since no gain cushion (agrees with cushion rule). D.
- loc.57 dividend: you still get the dividend if you hold on ex-date; author says expiry after ex-date. Principle D (note: early assignment before ex-date risk not mentioned - flag).
- loc.58 dividend-capture covered call timing = speculation, avoid (D).
- RULE cand. (loc.58-60): don't time covered call writes to special events (earnings, Fed, M&A); write on a regular monthly schedule and factor known events into strike choice. D.
- loc.61-63 Risk 1 opportunity cost; Figure 4 SPX buy-hold vs monthly index covered calls (BXM-like) - covered calls trailed buy-and-hold (B-ish: outside chart, source/period not given in text; figure not readable). Principle: covered calls cap upside; underperform in strong uptrends; write in flat markets at levels unlikely to be hit (loc.63). 
- RULE cand. (loc.63-64): stock falls -> if original thesis invalid, sell (take loss); if thesis valid, hold, keep writing. Trader using CC short-term -> cut losses. D.
- RULE cand. (loc.64): if price rises toward the short strike and you want to keep the shares, buy back the call (accept small loss). D.
- loc.64-65 TA intro; indicators lag. principle.
## loc.66-78
- loc.66-67 TA overview: oscillators fail in trends; Fibonacci works only as self-fulfilling belief; geometric patterns mostly sold by course vendors (D). principles.
- RULE cand. REGIME GATE (loc.68-70): write covered calls when the stock is ranging: Choppiness Index above ~61.8 (trending below 38.2; thresholds per stock, Fibonacci starting points) and/or ADX below 25 (trend above 25; trend traders use >50). Strong trend -> unfavourable. Examples: DIS ranged 29 sessions after CI crossed 61.8 (loc.69, single chart, hindsight) -> C. Strike suggestion: near recent highs in a range (loc.69).
- RULE cand. STRIKE DISTANCE BY VOLATILITY STATE (loc.70-72): Bollinger squeeze (bands narrowing repeatedly) -> expect a break, write farther OTM than usual; wide bands/trend -> far OTM by default; parabolic SAR dots flipping quickly -> can write closer; SAR dots persistently below price -> push strikes out. D (WMT chart). Flag: book calls the Bollinger midline a 20-day EMA and says the bands contain 95% of prices (loc.70) - standard is 20 SMA; normality assumption.
- Contrast: short-term traders may target squeezes and write close to the money (loc.71) - opposite of investor advice; same book.
- STOCK SELECTION screen (loc.73-77) for covered call candidates: stable, boring, ideally dividend payers; avoid penny/hot/speculative stocks; large/mega cap with steady profits+revenue; debt/equity < 2 and declining; company >= 5 years old; avoid cyclicals (travel, real estate, materials, airlines) and commodities; avg volume > 1M shares/day; dividend payout < 40% of net profit averaged over ~10 years; don't chase high yields; implied volatility 30-70; no earnings or major events before expiry; Finviz screen: optionable, yield > 2%, volume > 1M, earnings reported in the prior week, price < $50 (small account), price above 50-day MA (loc.77). D (assertion; examples AT&T, Ford, KO named as good candidates).
- loc.74 management "promote from within" - principle, no data source.
- loc.78 MS example Aug 2020: price above flattening 50 EMA, BB width < 0.20 declining -> expect range $44-54. C (case, outcome not yet given).
## loc.79-91
- loc.79-80 Aug 2020 cases: MS Sep-18 $52.50 call (ITM prob 26.91%, $111), PFE $40 call (29.74%, $70); BAC rejected (rising channel, %B rising -> likely assigned); WU rejected (bearish engulfing on earnings day 2020-08-04 -> expected decline). C (cases, no outcomes reported). Rule cand: skip a covered call when price is in a rising channel (assignment likely) or after a bearish earnings reaction (stock loss > premium) - chart reading, D/C.
- loc.80-82 IV: use stock's IV not VIX/beta; IV falls toward expiry unless event before expiry; RULE cand: write only when IV is between 30% and 70%; below 30 too little premium; above 70 too risky; avoid IV > 100 (binary events e.g. biotech trial) (loc.82). D. Figure 14 (AAL vs DIS yields by IV) not readable.
- STRIKE BY DELTA (loc.82-86): delta ~ probability of finishing ITM (proxy). Long-term holder wanting to keep shares -> lowest delta that still gives satisfactory return (e.g. 0.025 delta = $0.04, ~1.6%/yr on T); income/short-term trader wanting assignment + premium -> delta near 0.40 (T 30 strike, delta .426); avoid ITM and ATM writes. D (single AT&T chain). Flag: arithmetic inconsistent loc.85 ($60 premium then $49 in total; 3.1%x(365/26)=~43%, book says 37.3%); "guaranteeing over 8%/yr" (loc.86) - false certainty, flag.
- EXPIRY (loc.86-88): 30-45 DTE window (theta accelerates inside 30 days); longer expiry only if its premium per month beats the monthly option; long-term holders avoid long expiries. Early exercise mostly in last week; don't count on early exercise. D.
- loc.88-89 if the stock's thesis is gone, sell the stock rather than squeezing premium; if merely sideways, can write close to the money to maximize yield on exit. D. Principle: premium income small vs capital gains.
- loc.89 no earnings/political events within the holding period; reason for 'earnings in prior week' filter. (agrees with event rule)
- ROI (loc.89-91): return = net premium / share cost, annualized x 365/DTE; if assigned add (strike - cost). Big drop: short-term trader closes both legs (sell stock + buy back call; else naked call) - typo in loss calc ($12,000 vs $12,500) flag. Principle/process D.
## loc.92-104
- loc.92 breakeven = stock cost - premium. principle.
- EXITS (loc.92-94): (a) stock up near strike near expiry & want to keep shares -> buy back the call cheaply (T example $1 -> $0.10); (b) stock down -> buy back the far-OTM call cheaply and write a new call at a lower strike to lower cost basis (T $27: buy back at $0.02, write $30 call for $0.60) - flag: writing below the original cost can lock in a loss if assigned; book's net P&L sums realized + unrealized inconsistently ($256 vs $158 loc.93-94); (c) flat -> buy back and roll out to same strike next month (rolling = two separate trades). D (hypothetical numbers).
- loc.94-95 theta largest at/near the money; deep ITM/OTM decay slowly -> roll deep ITM/OTM calls early (loc.96). D.
- RULE cand. 1% ROLL RULE (loc.96): when the short call's extrinsic value falls below 1% of the stock price, buy it back and sell the next month's call (new strike/expiry). D. Inputs: option bid/ask, stock price.
- RULE cand. 2&20 RULE (loc.96-97): if within the first two weeks the call can be bought back for less than 20% of the premium received, buy it back (lock ~80%). D.
- RULE cand. CODE RED (loc.97): if a fraud allegation or serious business-practice scandal hits the stock, sell the stock and close the call at once; don't hold for option income. Example Luckin Coffee after Muddy Waters report: ~$32 -> below $3 within ~3 months, delisted (C, single case). Input: news/short-seller report -> news feed; measurable? event-based: news + price. Principle-ish; could be rule with input = short-seller report/fraud allegation via news/8-K.
- POOR MAN'S COVERED CALL (loc.98-101): long deep-ITM call, delta > 0.75, 1-2 years out (LEAP), + short OTM call 30-45 DTE delta ~0.40; best in mature bull markets with stock rising slowly/sideways (loc.99); SPY example Jul 2020 (34 DTE short $331 for $3.94 vs long $288 6/30/2021 for $46) - arithmetic confused (loc.100), flag. Worst case: short call going ITM -> close it at once (assignment would force exercising the LEAP / margin call); consider farther OTM short strikes (loc.101). D. Flag: vega passage says vol rise raises "intrinsic value" (loc.100) - wrong (extrinsic).
- loc.101-104 tax chapter (OIC-sourced): out of desk scope, not carried (qualified covered calls, holding period, dividends). Flag only.
## loc.105-118
- loc.105-108 process: process goals not outcome goals; sample goals include 0.4-delta strikes, rules-based exits, trade journal, weekly review, paper trade alongside live until 100 live trades (loc.107); skip trading when routine disrupted; scale up one position at a time (loc.108). Principles D; agrees with R-048 (paper trading) loosely.
- loc.109-111 covered-call funds: CEFs only attractive at a discount to NAV (loc.109); fees ~0.8% vs index 0.03%; funds tend to lag; author prefers DIY (loc.111). Principle D. BDJ named - not carried as pick.
- loc.112-116 scam checklist: audited records, Sharpe ratio > 1 "pretty good", licences via FINRA BrokerCheck, broker-dealer agreements (bucketing), fake testimonials (loc.112-116). Principle D (process). Flag: claims every hedge fund needs an SEC "securities-dealing license" (loc.114) - inaccurate, not carried.
- loc.116-117 summary: covered calls best when market sideways/slightly up; investors any regime except wildly bullish; speculators avoid bearish markets (loc.117); rolling down doesn't guarantee recovering a stock loss; pick rolled strikes to avoid locking a stock loss (loc.117) -> agrees with flag on loc.93. Final projection $25k -> $1M in 23 yrs at 15% (projection, flag).
- loc.118 promotions/references.
END OF BOOK reached at loc.119 (2026-11-13)
