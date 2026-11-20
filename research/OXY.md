# OXY — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: UNDERVALUED · Close $53.76 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $56.61 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 49 — Neutral — Aligned
Heat = round(0.6 × Substance 48 + 0.4 × Buzz 50) [computed in Python]. Yesterday: 49 (Neutral).

**Substance 48/100**
- Playbook fit 6/25: scout's fired rules R-056, R-042 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 20/20: scout label UNDERVALUED.
- Trend 5/15: close 53.76 vs 200-day 56.61 (below, 0); 6-month return -7.84% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 12/20: No rows after 10-02. CEO Jackson open-market buy 06-23 (4,770 @ $52.38, carried) keeps class one.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 50/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed, leaning negative.
- News volume 10/20: 5 items 11-12..11-18 vs 17 in the prior window (weekly avg 4.25; ratio 1.18) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 10/20: Webull community posts stand in for Reddit: 1 posts 11-12..11-18, tone negative (heavy = 10+). X: null.

Note: Biggest driver: value (20); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Three valuation methods +18% to +62% above price; Barclays OW PT $73; Berkshire holding unchanged.
- **Strongest against:** Closed -4.9% to $53.76, below its 200-day ($56.61), RSI 31; Seaport downgrade 11-16.
- **Long-term case:** Deleveraging Permian-heavy producer: principal debt hit the $10B milestone with a new $6B target, and management targets >$4B of added sustainable cash flow by 2030 via lower decline rates and costs. CO2 EOR/carbon capture is a long-dated option. Returns stay oil-price-dependent, and 2027 production is guided flat.

## What changed since 11-17
- Heat 49 → 49. SEC: 8-K filed 11-18, items 7.01/9.01 (Reg FD; content not read). No dilution forms. 11-16 Seaport downgrade to Neutral; 11-13 Barclays OW PT $73; 11-16 Berkshire 13F unchanged.

## Filings (last 90 days)
Today: SEC: 8-K filed 11-18, items 7.01/9.01 (Reg FD; content not read). No dilution forms.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 10-Q 11-09; 8-K 11-09 (2.02/9.01); Form 3 11-05; 8-K 10-13 (2.02/9.01); Form 4s 09-29, 10-02; SD 09-25. No S-1/S-3/424B/144, no 13G/13D, no 4.01/4.02, no going concern. Nothing new since 11-13.

## Insiders (6 months)
No rows after 10-02. CEO Jackson open-market buy 06-23 (4,770 @ $52.38, carried) keeps class one.
Carried context: no rows after 10-02. CEO Jackson 06-24 row (no side; secform4 earlier: P 4,770 @ $52.38 on 06-23). Hollub 90,000 @ $0 (gift) 09-25. Class one (12), unchanged.

## Institutions
MarketBeat failed. No 13G/13D in 90 days. Berkshire Q3 2026 13F: OXY 7th-largest holding, top-7 unchanged, OXY not listed among new/exited/changed positions [SOURCED 2026-11-16, Webull/Benzinga 11-16]. Direction for other holders unknown. (carried from 11-16; not re-checked)

## Government contracts
1PointFive (OXY subsidiary) South Texas DAC hub: DOE cooperative agreement, $50M initially obligated Sept 2024, up to $500M; DOE kept it on the preserved-awards list (April 2026). A grant, not a contract; nothing new in the 90-day window. Carried from 11-13.

## Connections
11-09: long-term CO2 offtake from third-party Delaware Basin gas plants (two unnamed developers fund capture; ~2 Mtpa). Berkshire Hathaway: 7th-largest 13F holding, unchanged in Q3 2026; OxyChem buyer (2025 deal). Helped by higher oil; hurt by oil declines and higher Q4 CO2-driven LOE.

## Sentiment
News 11-12..11-18: 5 items vs 17 in the prior feed (feed incomplete before ~10-19; ratio 1.18); tone mixed, leaning negative, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 1 posts, negative. X unreadable (null).
Headlines (7 days): 11-16 Seaport downgrade to Neutral; 11-13 Barclays OW PT $73; 11-16 Berkshire 13F unchanged.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Unscored: TTM EPS inflated by one-offs ($7.43 TTM vs $1.61 per Webull 11-13 snapshot); unexplained total vs outstanding share gap (999.9M vs 731.7M); preferred equity; Q4 LOE higher; flat 2027 production; Seaport downgrade 11-16 (new). New unscored: price broke below 200-day SMA.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars OXY and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions OXY — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261116/15934396934702080.html
- https://news-static.webullfintech.com/us/news-html/20261113/15917252674503680.html
- https://data.sec.gov/submissions/CIK0000797468.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://news-static.webullfintech.com/us/news-html/20261116/15934396934702080.html · https://news-static.webullfintech.com/us/news-html/20261110/15901036445888512.html · https://news-static.webullfintech.com/us/news-html/20261116/15935615899660288.html · https://data.sec.gov/submissions/CIK0000797468.json?v=20261116R
