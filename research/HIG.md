# HIG — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $135.97 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $134.96 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 37 — Cold — Aligned
Heat = round(0.6 × Substance 45 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 47 (Neutral).

**Substance 45/100**
- Playbook fit 7/25: scout's fired rules R-056, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 135.97 vs 200-day 134.96 (above, +5); 6-month return +0.38% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No rows after 11-02 (CFO Costello sold 31,597 @ $135.75).
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed (PT raises, ratings held).
- News volume 0/20: 2 items 11-12..11-18 vs 9 in the prior window (weekly avg 2.25; ratio 0.89) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Price-target raises to $145 (MS 11-17, Mizuho 11-12) above the $135.97 close.
- **Strongest against:** Wells Fargo downgrade (11-11), Q3 revenue miss and CFO sale 11-02.
- **Long-term case:** High-ROE P&C and group-benefits franchise (TTM core ROE 17.9%) with a dividend raised 12% and ongoing buybacks; compounds steadily if underwriting holds. Softer commercial pricing, rising workers'-comp claim frequency, cat exposure and a modestly dilutive Equitable EB deal cap upside. Steady compounder, not a rerating story.

## What changed since 11-17
- Heat 47 → 37. Nothing new since 11-04 (SEC JSON 11-18). 11-17 MS EW PT $145; 11-12 Mizuho Neutral PT $145.

## Filings (last 90 days)
Today: Nothing new since 11-04 (SEC JSON 11-18).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 10-Q + 8-K (2.02) 10-26; 8-K 09-30 (5.02/7.01); 8-K 09-25 (1.02 termination of a material agreement, 7.01; not opened); Form 3 x2 09-09 and 11-04; Form 4 x3 10-29 and 11-04; Form 144 11-02. No S-3/424B, no 4.01/4.02, no going-concern. Nothing new after 11-04.

## Insiders (6 months)
No rows after 11-02 (CFO Costello sold 31,597 @ $135.75).
Carried context: no rows after 11-02 (CFO Costello sold 31,597 @ $135.75). Prior rows: Tooker sold 8,895 @ $135.13 (05-27); 07-29 director rows no side. Class: none (8), unchanged from 11-16 scoring.

## Institutions
Unknown. No 13G/13D on HIG's SEC submission list since 08-18. MarketBeat institutional page unreachable (client_error). (carried from 11-16; not re-checked)

## Government contracts
None found; P&C/group-benefits insurer, not a plausible federal contractor. Not searched.

## Connections
Closed acquisition of Equitable's Employee Benefits business (~$500M annual premium; modestly dilutive 2027). Agent/broker distribution. Small Business written premium +7% (CR 85.2%); Business Insurance +6% (underlying CR 90.1%). Hurt by rising workers'-comp frequency.

## Sentiment
News 11-12..11-18: 2 items vs 9 in the prior feed (feed incomplete before ~10-19; ratio 0.89); tone mixed (PT raises, ratings held), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-17 MS EW PT $145; 11-12 Mizuho Neutral PT $145.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none. Unscored: Wells Fargo downgrade to Equal-Weight 11-11; Cantor PT cut to $136 (11-02); Q3 revenue $7.220B missed $7.370B; core EPS $3.50 down 2.5% YoY; rising workers'-comp frequency; CFO sale 11-02; 8-K item 1.02 (09-25) still unexamined.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars HIG and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions HIG — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261117/15939953097229312.html
- https://news-static.webullfintech.com/us/news-html/20261112/15910878656720896.html
- https://data.sec.gov/submissions/CIK0000874766.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000874766.json?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261111/15905318571459584.html · https://news-static.webullfintech.com/us/news-html/20261027/15820611978145792.html · Webull get_insider_transactions HIG 2026-11-16
