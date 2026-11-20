# FreemanCS notes (2026-11-11 run)
## loc.1–13
- loc.1–3: publisher disclaimers; email-list bonus promotion (stock tips teased) — not carried.
- loc.3: author asserts markets move sideways or slightly up ~80–85% of the time (no source) → non-directional strategies. D. Sept 2020 OTM call buyers hurt when TSLA/AAPL reversed (anecdote).
- loc.5–7: selling options with covered risk; predicting a range is easier than a price. D.
- loc.7–8: time decay favours sellers; premium = cushion. D.
- loc.8: claims spread traders often string 8–10 winners; directional traders win 30–40% (no data). D.
- loc.9–10: ~30-day trades avoid PDT; start with ~$1,000 (even $500). Author's estimate: hit rate 65–85% for a solid credit-spread strategy (no data) → "author claims". D.
- loc.10–11: "synthetic dividends" from selling options. D.
- loc.11–12: defined risk/reward; stop orders can be gapped but strikes can't (note: true for max loss at expiry; early assignment caveat later?). D.
- loc.12: credit trades last ~1 month; let them ride rather than grab small profits (to check vs later exit rules). D.
- loc.13: only three credit spreads needed; horizontal vs vertical spreads defined.
## loc.14–26
- loc.14–16: BULL PUT SPREAD (book's version: short an in-the-money put above price, long a lower OTM put, same expiry ~30 days). Hypothetical: stock 280, short 290 put / long 270 put, net credit 6 → max profit 6, max loss = width − credit = 14; breakeven = short strike − credit. Arithmetic correct. Figure caption swaps the ITM/OTM labels (book error). Use when moderately bullish or range-bound; you form a price range you expect (example: unlikely below 265). D (hypothetical).
- loc.16–17: BEAR CALL SPREAD mirror (short lower call, long higher call); max loss width − credit. D.
- loc.17–18: risk/reward 6/14; example: 80% wins at +100/−300 → +200 per 10 trades (arithmetic). Wider/OTM spreads raise win rate, cut reward:risk. D/A arithmetic.
- loc.18–20: SHORT IRON BUTTERFLY: short ATM call + put at same strike, long equidistant wings; max profit = credit at the short strike; max loss = wing width − credit; breakevens = short strike ± credit. Hypothetical Visa example (credit 7.18 on $10 wings; max loss 2.82). Book labels upper/lower breakeven formulas with swapped leg names (minor). D.
- loc.20: credit spreads allowed in IRAs at most brokers (account mechanics).
- loc.21–23: EARLY ASSIGNMENT RISK when writing ITM options; mitigate by writing ATM/slightly OTM short strikes (e.g. 280 or 275 put with stock at 280; bear call short 285/long 300) at the cost of a smaller credit; early exercise rare because the buyer forfeits extrinsic value; extrinsic value drops sharply in the last 30 days; cash-settled index options (SPX, RUT) remove assignment. D. Candidate rule: prefer OTM/ATM short strike to avoid early assignment.
- loc.23–26: broker selection: fees (contract + assignment), risk-graph tools, multi-leg order entry (enter both legs at once to avoid legging risk), service, FINRA registration, education. Principle: enter spreads as one multi-leg order.
- loc.26: margin account needed for spreads (cash to cover max loss).
## loc.27–39
- loc.27–29: broker account level for spreads (often level 3), hidden fees; recommends a computer, not a phone app, for multi-leg trades; recommended brokers (not affiliated). Not rules.
- loc.29–31: DELTA ≈ probability of finishing in the money (approximate); strategy deltas: bear call negative, bull put positive, iron butterfly neutral. D (standard approximation).
- loc.31–33: GAMMA spikes in the last ~7 days for near-the-money options → avoid credit spreads on weekly options; in the final week close near-the-money or barely-OTM positions and take the profit (also removes assignment risk). D. Candidate rule (exit in final week).
- loc.33–34: THETA: decay accelerates in last 30 days; sellers want it.
- loc.34–35: ENTRY WINDOW: open credit spreads 30–45 days to expiry (beyond 45: little movement, poor liquidity; inside: decay accelerates). D. Candidate rule.
- loc.36–37: NO EARNINGS inside the trade's life (30–45 days); insider trades cluster after earnings. D. Candidate rule (agrees desk C6).
- loc.37: ex-dividend inside the trade lowers call premiums. D.
- loc.37–38: avoid stocks prone to binary announcements: small pharma (drug approvals; cites Frazier 2015 for 8–10 yrs to market), restructurings, lawsuits, shareholder votes, CEOs announcing on social media; prefer boring businesses. D.
- loc.38: avoid Fed decisions, jobs reports for index options (stocks less affected); Jackson Hole; emergency Fed meetings → exit. D.
- loc.39: political events (presidential elections, US–China trade war names). Best: a stock moving from high to low volatility (sell when premiums are rich). D.
## loc.40–52
- loc.40–42: IV = market's 1-standard-deviation one-year range (~68%); want IV high at entry and falling during the trade. D (standard).
- loc.42–43: IV ENTRY FILTER: ideally IV below 50% at entry; never write credit spreads above 100% IV; example IVs at writing (AT&T 17%, SPY 18%, ... Nio 143%). D. Candidate rule. Also: sell options on stocks whose IV is high and likely to fall (no measure given).
- loc.43–44: IV drivers: supply/demand imbalance; time to expiry; market-wide VIX; mega-cap weight in S&P. D.
- loc.44–47: HFT front-running (cites Lewis 2015), payment for order flow; algos mostly in bonds (cites a 2019 article, ratio 95:1 — dubious). Not carried except as background.
- loc.47–48: use TA only to find sideways/mild-trend periods. D.
- loc.48–49: trendlines/channels subjective, hindsight → prefer S/R. D.
- loc.49–51: S/R: swing points, polarity (broken resistance becomes support; gold $1,690 example), strength = force of approach and rejection. D.
- loc.51–52: RANGE SETUP: AT&T traded $29.22–$30.84 for 62 trading days (Jun–Aug 2020) → short call strike just above resistance ($31), short put strike just below support ($29); messier range → wider zone → more conservative strikes. C (one case). Candidate rule: credit-spread strikes outside the range boundaries.
- loc.51: watch counter-trend reactions at swing points grow → a range may be forming; shrinking reactions → trend strong, unsuited. D.
- loc.52: BACKTEST (authors'): SPY options 2009–2019, sell ~0.31-delta put spreads, 30 days to expiry, each time SPY crosses above its 50-day moving average; take profit at 50% of max, losers held to max loss → 211 trades, 90.5% win rate, 433% total profit over 10 yrs; including 2007–09 still net positive over 46 trades (unclear). Spread width, costs, fills not stated; text confuses 50EMA with the 50/200 golden cross. Grade A for the test as reported (rules, sample, period), with caveats. Candidate rule (options-income).
## loc.53–65
- loc.53: the 50-day crossover flags stocks leaving a long range; very bullish names raise volatility risk for bull put spreads. D.
- loc.53–55: BOLLINGER WIDTH (2 SD, 60-day average in example): for credit spreads read band WIDTH, not touches: widening bands = rising volatility → stay away; contracting bands after a trend = ideal; but a very tight squeeze after a long range (shrinking bars, higher lows/lower highs) warns of an explosive new trend → close positions on the threatened side; compare band width with the past 30–60 days. AT&T chart, C. Candidate rule.
- loc.55–56: low volatility + mild trends; sectors differ (2020: S&P +4%, Nasdaq +27%, XLE −37%).
- loc.56–57: index options (SPX, RUT) cash-settled → no assignment; stick to liquid broad/large-sector indexes; thin option chains get wide spreads. D.
- loc.57–58: ETFs: liquidity first; ≥500,000 shares/day and ≥$5B AUM; avoid leveraged/inverse ETFs for credit spreads; prefer big issuers. D.
- loc.59–60: STOCK SCREEN (authors): above 50-day MA; volume >500k shares/day; optionable; mid/large cap; earnings in the previous week (so none inside the trade). Avoid media darlings, activist targets, IV >50%, small caps / stocks under $10, USO-like non-tracking products, inverse ETFs that can halt, VIX products (UVXY), leveraged ETFs. D. Candidate rule (options-income screen).
- loc.60–61: Choppiness Index >61.8 = ranging (optional). D, one chart.
- loc.61: index options → more wins, lower premium; stocks → more premium, lower win rate (assertion).
- loc.61–64: STRIKES: nearer-the-money short strike = bigger credit, higher loss odds (Disney $5-wide spreads: 1.77 credit / 3.23 risk vs 0.46 / 4.54 — hypothetical quotes). Authors prefer further-OTM, high-probability strikes; choose short strike first; long strike 1–2 strikes away; set a pre-planned stop level inside the spread (e.g. exit at 218 on a 215/220 call spread). If the trade is against you for >15 days of a 30–45 day hold, it probably loses. D.
- loc.64–65: short strike just below support (bull put) / just above resistance (bear call); deeper in the zone = safer. D.
- loc.65: delta 0.16 ≈ 1 SD; cites projectoption (2020) backtest: SPY bull put spreads 2008–2020, short ~0.30 delta / long ~0.16 delta, entered first day and exited last day of each month regardless → ~74% of trades expired OTM. B (outside study, method partly shown). Book mislabels 0.30 delta as two SD.
## loc.66–78
- loc.66: enter spreads with a limit at the bid-ask midpoint; never chase past the ideal entry; wide spreads (some index chains ~$1.50) → no market orders. Enter an iron butterfly as two separate spreads if the broker can't take 4 legs. D (agrees R-023 don't chase).
- loc.66–68: VIX FILTER: in the projectoption backtest (SPY bull put spreads 2008–2020, 74% win), skipping entries when VIX > 30 raised win rate to 77% and overall profit by ~50% (as reported). Apply VIX<30 also to big index-weighted stocks. B (outside test, partly shown). Candidate rule. Don't write options on the VIX itself.
- loc.69–70: MANAGEMENT (same projectoption backtest): take-profit at 25% of max profit → 86% win but lowest total profit; 75% → 76% win, highest total; stop when the loss equals 100% of the max profit (tested −200%/−300% did not do better). Authors' rule: take profit at 75% of max, stop at −100% of credit. B. (NOTE conflict with loc.52 own backtest that took profit at 50% and ran losers to max loss.)
- loc.70–72: order mechanics: stop on the spread's net premium (credit 1 → stop buy-back at 2), GTC; take-profit buy-back at 25% of the credit (book says "75% of initial credit… set at 0.75" — inconsistent: buying back at 0.75 captures only 25%; flag); paper-trade the platform first. D.
- loc.72–74: IRON BUTTERFLY management: standard targets 15% of max profit / stop at 25% of max loss; adjust before breakeven, not after; exit whole trade if outlook changed early; late test → roll the untested long wing closer only if it keeps a net credit (PZZA hypothetical); doing nothing is valid for defined risk. D.
- loc.74–76: AFTER-HOURS ASSIGNMENT CASE: a trader's $1-wide 410/409 put spreads on a volatile EV stock looked OTM at the close ($418) but the stock fell to $393 after hours before the 4:30pm CT exercise cutoff; short puts assigned, broker notice came too late to exercise the long puts; forced liquidation, ~$30,000 loss on a $500-max-loss trade. Cites OIC rule text. C (one real case). → Close all short options a couple of days before expiration, even if OTM. Candidate rule (strong).
- loc.76–78: money management: margin per spread = (width − credit) × 100; authors allow up to 10% of account per trade, 1–2 trades a month (because losses are capped at −100% of credit) — CONFLICT with R-009 2% cap and desk C7 tiers. Keep trading and long-term accounts separate. Authors claim 1–3% a month expected return (no record). D.
## loc.79–87 (END OF BOOK loc.87)
- loc.79: scale per-trade risk down toward 2% as the account grows; cap total monthly risk at 10% (one 10% trade or two 5% trades); smaller accounts use narrower spreads or save up. D.
- loc.79–80: paper-trade and observe a new instrument 2–6 months (through an earnings season) before trading it live; master two names with earnings in different months. D.
- loc.80–84: routine: place orders after the open settles, by ~11am ET; avoid after-hours orders (wide spreads); avoid social media; diet/sleep/exercise; never trade hungry, angry, lonely, tired or impaired. D (process principles).
- loc.84: authors project 1–3%/month; $5,000 → $53,825 in 10 yrs if compounding (projection, not result).
- loc.85: three reader testimonials (win rates 86–96%, $28k profits) — unverified, survivorship; not carried as evidence.
- loc.86–87: promotion + references (projectoption YouTube 2020; OIC exercise FAQ; Lewis 2015; Frazier 2015).
- Overall: options-income book; two backtests cited (own SPY 2009–2019 one at loc.52; projectoption 2008–2020 at loc.65, 68–70). Several internal inconsistencies flagged (ITM/OTM labels loc.15, 17; golden cross vs 50EMA loc.52; take-profit order price loc.71).
