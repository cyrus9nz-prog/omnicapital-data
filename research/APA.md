# APA — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $45.52 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $38.67 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 47 — Neutral — Aligned
Heat = round(0.6 × Substance 45 + 0.4 × Buzz 50) [computed in Python]. Yesterday: 41 (Neutral).

**Substance 45/100**
- Playbook fit 7/25: scout's fired rules R-056, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 45.52 vs 200-day 38.67 (above, +5); 6-month return +17.17% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No rows after 09-30 director awards. Maddox 05-20 15,500 shares, no price (not counted as open-market).
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 50/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed (PT raises; MS Underweight).
- News volume 20/20: 3 items 11-12..11-18 vs 6 in the prior window (weekly avg 1.50; ratio 2.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Above its 200-day with 6-month return +17% vs SPY -1%; Barclays PT $48.
- **Strongest against:** MS Underweight PT $44 and Bernstein $41 sit below the $45.52 close; 2 of 3 value methods below price.
- **Long-term case:** High-FCF, oil-levered E&P cutting costs ($500M annualized savings, two years early) and debt (new $2B net debt target), with Suriname Grand Morgu first oil in mid-2028 at 10% capex share for 40% WI. Egypt concentration and oil-price risk cap the multiple; 'overvalued' holds only on normalized oil.

## What changed since 11-17
- Heat 41 → 47. Nothing new since 10-Q 11-05 (SEC JSON 11-18). 11-18 MS Underweight PT $44; 11-13 Barclays EW PT $48; 11-12 Bernstein MP PT $41.

## Filings (last 90 days)
Today: Nothing new since 10-Q 11-05 (SEC JSON 11-18).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 10-Q 11-05; 8-K 11-04 (2.02/9.01); 8-K 10-07 (2.02/9.01); nine Form 4s 10-01 (director units); SD 09-25. No S-1/S-3/424B/144, no 13G/13D, no 4.01/4.02, no going concern. Nothing new since 11-13.

## Insiders (6 months)
No rows after 09-30 director awards. Maddox 05-20 15,500 shares, no price (not counted as open-market).
Carried context: no rows after 09-30 (director unit grants @ $0). Maddox 15,500 05-20 (code I row), Henderson 1,968 @ $37.50 05-26. No open-market buys. Class none (8).

## Institutions
MarketBeat failed. No 13G/13D in the 90-day window; last SC 13G/A 2026-08-12 (holder not identified). Direction unknown. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (not searched).

## Connections
Suriname Grand Morgu: carry agreement cuts APA capex share to 10% with 40% WI; first oil mid-2028 (partner per public record TotalEnergies; not opened). Egypt ~206k BOE/d brings Egyptian government counterparty/receivables exposure. Alaska and Uruguay exploration interests (profile).

## Sentiment
News 11-12..11-18: 3 items vs 6 in the prior feed (feed incomplete before ~10-19; ratio 2.00); tone mixed (PT raises; MS Underweight), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-18 MS Underweight PT $44; 11-13 Barclays EW PT $48; 11-12 Bernstein MP PT $41.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Unscored: Egypt concentration and receivables risk; price near 52-week high ($52.96) after more than doubling from a $22.42 low (11-13 snapshot); lukewarm sell-side (MS Underweight, Mizuho Underperform per 11-13); TTM EPS $6.15 vs $3.99 suggests one-offs.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars APA and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions APA — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261118/15945355870716928.html
- https://news-static.webullfintech.com/us/news-html/20261113/15917060015321088.html
- https://data.sec.gov/submissions/CIK0001841666.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://news-static.webullfintech.com/us/news-html/20261105/15872264828380160.html · https://news-static.webullfintech.com/us/news-html/20261113/15917060015321088.html · https://data.sec.gov/submissions/CIK0001841666.json?v=20261116R · Webull get_insider_transactions APA (2026-11-16)
