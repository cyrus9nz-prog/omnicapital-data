# PRU — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $121.54 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $108.02 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 37 — Cold — Aligned
Heat = round(0.6 × Substance 45 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 47 (Neutral).

**Substance 45/100**
- Playbook fit 7/25: scout's fired rules R-058, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 121.54 vs 200-day 108.02 (above, +5); 6-month return +20.73% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No priced rows in Webull since May; SEC Form 4 11-16 not opened.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed (PT raises, Neutral/Underweight).
- News volume 0/20: 3 items 11-12..11-18 vs 14 in the prior window (weekly avg 3.50; ratio 0.86) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Above its 200-day; 6-month return +20.7%; 4.6% yield passes R-058.
- **Strongest against:** Analyst average 3.44 fails R-056; Wells Fargo Underweight PT $113 below price.
- **Long-term case:** Mature insurer/asset manager narrowing to US, Japan and PGIM. Compounding depends on Japan's governance reset (sales resume in phases from Feb 1) and redeploying ~$3.1B net LatAm proceeds. Low growth; returns likely from the ~4.56% yield plus buybacks.

## What changed since 11-17
- Heat 47 → 37. SEC: 424B2 11-16 and 11-17 (likely notes, not equity); SCHEDULE 13G x2 and 13G/A x2 11-13; Form 4 11-16; 13F-HR 11-16. 11-17 Mizuho Neutral PT $124; 11-12 Wells Fargo UW PT $113; 11-12 Mizuho PT $120.

## Filings (last 90 days)
Today: SEC: 424B2 11-16 and 11-17 (likely notes, not equity); SCHEDULE 13G x2 and 13G/A x2 11-13; Form 4 11-16; 13F-HR 11-16.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 10-Q 11-04; 8-K 11-03 (2.02 Q3), 10-20 (7.01/8.01 LatAm sale), 10-15, 10-09, 10-08; 13 424B2 (latest 11-16) = medium-term note/debt takedowns; Form 144 x3 11-06; Form 4s incl. 11-16 (not opened); 13G 11-10; 13F-HR 11-16. No S-3 equity/ATM, going concern or restatement.

## Insiders (6 months)
No priced rows in Webull since May; SEC Form 4 11-16 not opened.
Carried context: no rows after 09-14 (director deferred-unit rows). Webull lacks the 11-06 exercise-and-sell rows seen on secform4 11-16 (Sullivan 3,544 @ $121.32; Kappler 2,797 @ $120.60; Boyle 2,794 @ $121.24). Class none (8) per prior scoring.

## Institutions
Unknown. SCHEDULE 13G 11-10 (accession prefix 0000093751, likely State Street) not opened. The 13G/13G-A filings of 10-07 and 11-13 carry PRU's own prefix (likely PRU reporting on other issuers). New 13F-HR 11-16 is PRU's own portfolio. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor. Not searched.

## Connections
Selling Prudential of Brazil and Mexico to CNP Assurances for $4.025B cash (announced 10-20, close 2H27). Indonesia/South Africa/Kenya JV stakes sold (closed 10-13). PGIM + LGT backed $680M Tree Line continuation vehicle (10-28). Helped: CNP. Hurt: Japan sales suspension until Feb.

## Sentiment
News 11-12..11-18: 3 items vs 14 in the prior feed (feed incomplete before ~10-19; ratio 0.86); tone mixed (PT raises, Neutral/Underweight), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-17 Mizuho Neutral PT $124; 11-12 Wells Fargo UW PT $113; 11-12 Mizuho PT $120.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none (424B2s are debt notes). Unscored: officer exercise-and-sell 11-06 with no buys; Japan sales suspension until Feb; adj EPS $3.77 vs $4.05 y/y; Underweight ratings (WF $113, Barclays $98, MS $100); price above most PTs.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars PRU and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions PRU — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261117/15939799723590656.html
- https://news-static.webullfintech.com/us/news-html/20261112/15911153908903936.html
- https://data.sec.gov/submissions/CIK0001137774.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001137774.json?v=20261116R · https://www.secform4.com/insider-trading/1137774.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261104/15866626112920576.html · https://news-static.webullfintech.com/us/news-html/20261020/15780126462616576.html
