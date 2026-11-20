# PFE — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $28.06 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $26.25 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 70 — Warm — Aligned
Heat = round(0.6 × Substance 67 + 0.4 × Buzz 75) [computed in Python]. Yesterday: 70 (Warm).

**Substance 67/100**
- Playbook fit 7/25: scout's fired rules R-058, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 28.06 vs 200-day 26.25 (above, +5); 6-month return +12.32% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 20/20: No new Webull rows. Open-market buys Bourla, Blaylock, Buckley (Aug) keep class 2+.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty 0: none scored.

**Buzz 75/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 30/40: mostly positive.
- News volume 10/20: 7 items 11-12..11-18 vs 25 in the prior window (weekly avg 6.25; ratio 1.12) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 20/20: Webull community posts stand in for Reddit: 13 posts 11-12..11-18, tone mostly positive (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: playbook fit (7). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Cluster of officer/director open-market buys (Aug) plus new Starna CAR-T deal 11-18.
- **Strongest against:** ~$22.7B of revenue loses exclusivity by 2028 (carried); Lilly oral GLP-1 competition.
- **Long-term case:** Possible but unproven compounder. Seagen oncology, obesity (berobenatide, Blackstone-funded) and $7.2B in cost savings must replace ~$22.7B of revenue that loses US exclusivity by 2028. Management targets high-single-digit revenue CAGR for 2028-33. The ~6% yield pays holders to wait; 2027-28 is the test.

## What changed since 11-17
- Heat 70 → 70. SEC: Form 4 filed 11-16 (not yet in Webull; not opened). 11-18 Starna in vivo CAR-T license ($330M upfront, up to $2.3B); 11-12 Blackstone funds up to $1.5B berobenatide; 11-12 Lilly oral GLP-1 China approval.

## Filings (last 90 days)
Today: SEC: Form 4 filed 11-16 (not yet in Webull; not opened).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON 11-16): 13F-HR 11-12; 10-Q 11-03; 8-K 11-03 (2.02/9.01); 8-K 11-03 (5.02/9.01); 13G 10-16; Form 4s 09-01..11-03; Form 3 08-28; N-PX 08-31. Nothing new since 11-12. No S-3/424B/144/13D. No going-concern, auditor-change or restatement filing seen.

## Insiders (6 months)
No new Webull rows. Open-market buys Bourla, Blaylock, Buckley (Aug) keep class 2+.
Carried context: no rows after 09-30 (Bourla dividend-reinvest 21 sh). Open-market buys (code P, secform4 per 11-12/11-16 runs): Bourla 38,000 @ $26.34 (08-12), Blaylock 39,231 @ $25.46 (08-05), Buckley 37,632 @ $25.52 (08-05, visible on Webull). Sales: DaMico 3,278 @ $25.40 (08-05), 2,000 @ $25.70 (06-09). Class 2+ (20).

## Institutions
Undetermined. The SEC list shows SCHEDULE 13G 10-16 (accession prefix 0000078003, Pfizer's own CIK; not opened) and Pfizer's own 13F-HR 11-12 (its portfolio, not holders of PFE). (carried from 11-16; not re-checked)

## Government contracts
No new federal award found (not re-searched today). Prior runs found only routine DLA delivery orders under an existing IDV, which are immaterial.

## Connections
Blackstone Life Sciences co-funds up to $1.5B of berobenatide (11-11). Medicus Pharma CD228V ADC collaboration (11-09). Competitors: Lilly oral GLP-1 orforglipron won China approval (11-12). Enanta filed a European Paxlovid patent suit (10-29).

## Sentiment
News 11-12..11-18: 7 items vs 25 in the prior feed (feed incomplete before ~10-19; ratio 1.12); tone mostly positive, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 13 posts, mostly positive. X unreadable (null).
Headlines (7 days): 11-18 Starna in vivo CAR-T license ($330M upfront, up to $2.3B); 11-12 Blackstone funds up to $1.5B berobenatide; 11-12 Lilly oral GLP-1 China approval.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Patent cliff (~$22.7B by 2028, carried from 11-12). TrumpRx/Medicare pricing pressure. Paxlovid -63% and Comirnaty -29% in Q3. Enanta patent suit. Premarin Canada exit (minor). The 'Susie Wiles & PFE' post is unverified rumour.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars PFE and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions PFE — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261118/15944612685541376.html
- https://news-static.webullfintech.com/us/news-html/20261112/15911264004981760.html
- https://data.sec.gov/submissions/CIK0000078003.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://www.secform4.com/insider-trading/78003.htm?v=20261116R · https://data.sec.gov/submissions/CIK0000078003.json?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261111/15907276797297664.html · https://news-static.webullfintech.com/us/news-html/20261113/15917059992055808.html
