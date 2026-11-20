# UHS — researcher deep dive, 2026-11-12

Lane: S&P 500 · tested rules · Scout label: UNDERVALUED · Scout lean: Long · Close $193.84 [SOURCED 2026-11-12 close, Webull daily bar]
Scout list updated 2026-11-12 1:55pm PT (close run) — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 48 — Neutral — Aligned
Heat = round(0.6 × Substance 54 + 0.4 × Buzz 38) [computed in Python].

**Substance 54/100**
- Playbook fit 6/25: scout's fired rules R-056 A5, R-025 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 20/20: scout label UNDERVALUED.
- Trend 15/15: above 200-day yes +5 (close 193.84 vs SMA200 176.20); 6-month return +13.87% vs SPY +1.71% (126 sessions from 2026-05-14) +5; R-050 ON +5 [SOURCED 2026-11-12, Webull daily bars; computed in code].
- Insiders 8/20: class none. secform4, since 05-12: no open-market buys or sales. NEW 11-11 (filed 11-12): CEO Marc D. Miller exercised 75,000 options @ $143.81 and had 63,377 shares withheld @ $196.77 (net-settled, kept ~11.6k; owns 756,679). 05-20: five director option awards (1,217 each); 05-27: Alan B. Miller 'Other' 114,029 (Webull shows 25,495 award). 10b5-1 not noted.
- Institutions 5/10: flat_unknown. Quiver (13F Q2 2026, page dated 10-28): 307 institutions added vs 335 reduced. Adds: LA Capital +729k (+215%), Sixth Street +575k (new), CPP Investments +554k, Dimensional +429k (+24%). Cut: Goldman Sachs -729k (-54.8%). Slightly more reducers than adders; no share-count total -> flat/unknown. MarketBeat failed.
- Catalysts 0/10: no dated positive catalyst (award, partner deal, approval) 2026-08-14..11-12 found.
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points)
- News tone 30/40: Alpha Vantage unavailable (rate-limit/premium errors) → scored from the past week's headlines (mostly positive 30, mixed 20, mostly negative 10).
- News volume 0/20: 1 items in 7 days vs 5 in the prior 4 weeks (weekly avg 1.25; ratio 0.80) [SOURCED 2026-11-12, Webull get_stock_news].
- Reddit slot 0/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 0 (none (latest post 2026-07-28)). X: null.

Note: Biggest driver: value label (20/20); biggest drag: catalyst (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- Strongest evidence for the scout's call: Acute adjusted admissions +4.9% and behavioral same-facility revenue +4.0% in Q3; P/E ~8 on TTM EPS with buybacks; RBC raised PT to $207 (11-11).
- Strongest evidence against: Q3 adj EPS -8% y/y with 2026 guide at the low end, revenue per adjusted admission -1.7%, 2027 Medicaid supplemental-payment risk; price already near the top of analyst targets.
- Long-term case: Family-controlled hospital and behavioral operator with buybacks and an expanding behavioral/virtual footprint (Talkspace). Can compound if volumes hold, but Medicaid supplemental-payment cuts, labor costs, slow de novo ramps and litigation reserves threaten margins; UNDERVALUED depends on 2027 payments holding.

## 1 Identity
Confirmed: Webull profile: Universal Health Services Inc, NYSE, CEO listed Alan B. Miller (secform4 lists Marc D. Miller as President & CEO, Alan B. Miller Exec Chairman); acute care + behavioral hospitals. Matches.

## 2 Filings (last 90 days)
Since 2026-08-14 (SEC submissions): 10-Q 11-06; 8-K 10-27 (2.02); 13Gs 10-08, 10-19; 8-K 08-21 (1.01/2.03 new debt agreement); S-8 08-18 (employee plan registration); 8-K 08-17 (2.03/8.01). 424B5 08-13 ($1.1B secured notes, debt) falls just before window. No S-1/S-3/equity 424B/ATM, no 4.01/4.02, no NT 10-Q. Form 4 filed 11-12.

## 3 Insiders (last 6 months)
secform4, since 05-12: no open-market buys or sales. NEW 11-11 (filed 11-12): CEO Marc D. Miller exercised 75,000 options @ $143.81 and had 63,377 shares withheld @ $196.77 (net-settled, kept ~11.6k; owns 756,679). 05-20: five director option awards (1,217 each); 05-27: Alan B. Miller 'Other' 114,029 (Webull shows 25,495 award). 10b5-1 not noted. Cluster buying: no.

## 4 Institutions
Quiver (13F Q2 2026, page dated 10-28): 307 institutions added vs 335 reduced. Adds: LA Capital +729k (+215%), Sixth Street +575k (new), CPP Investments +554k, Dimensional +429k (+24%). Cut: Goldman Sachs -729k (-54.8%). Slightly more reducers than adders; no share-count total -> flat/unknown. MarketBeat failed.

## 5 Government contracts
None found (search 'Universal Health Services contract award 2026 VA TRICARE DoD' returned no UHS award). Revenue is Medicare/Medicaid reimbursement, not contract awards.

## 6 Connections
Talkspace acquisition closed 08-17 (synergies 12-24 months). Payers: Medicare, Medicaid incl. supplemental payments (2027 risk), commercial. De novo hospitals Palm Beach Gardens and Washington DC ramping slowly; Laurel Ridge recertification expected 2027; Cumberland Hospital tentative settlement (~$26M pre-tax reserve charges in Q3).

## 7 Sentiment
Webull news 1 in 7d (RBC PT raise to $207, rating unchanged at Sector Perform) vs 5 in prior 28d; thin coverage. No Webull posts since July; Reddit/X unreadable. Divergence: price $193.84 sits near the top of the $156-$207 target range while EPS fell 8% y/y and margins compress; 'positive' tone rests on one headline. AV not called.
Headlines: 2026-11-11 RBC maintains Sector Perform, raises PT to $207 | 2026-11-02 Wells Fargo Equal-Weight, raises PT to $170 | 2026-10-29 Baird Neutral, lowers PT to $156; Guggenheim Buy, lowers PT to $201 | 2026-10-27 Q3 adj EPS $5.22 beats $5.16 (down 8% y/y); sales $4.733B beat
Congressional trades: None found (Quiver page did not cover congressional trades).

## 8 Red flags
No scored flag. Unscored: margin compression (EPS -8% y/y); 2026 guide at low end; 2027 Medicaid supplemental risk; Cumberland settlement reserve; Laurel Ridge recertification; short interest 5.56% of float (scout figure, not re-verified); S-8 08-18 is employee-plan registration (not counted as dilution).

## What changed since yesterday's report
New: Form 4 filed 11-12 — CEO Marc Miller exercised 75,000 options @ $143.81 on 11-11 and net-settled (63,377 withheld @ $196.77); not an open-market trade, holdings rose. New: institutions now readable via Quiver (307 added vs 335 reduced, Q2 13F). No new red flags. Close $193.84 (-1.5% vs $196.77).

## Sources (opened this run, 2026-11-12)
- Webull get_company_profile UHS (Webull get_company_profile UHS) — 2026-11-12
- Webull get_insider_transactions UHS (Webull get_insider_transactions UHS) — 2026-11-12
- Webull get_stock_news UHS (Webull get_stock_news UHS) — 2026-11-12
- Webull get_community_posts UHS (Webull get_community_posts UHS) — 2026-11-12
- Webull get_stock_filings UHS (Webull get_stock_filings UHS) — 2026-11-12
- [SEC submissions CIK0000352915 (UHS)](https://data.sec.gov/submissions/CIK0000352915.json?v=20261112R) — 2026-11-12
- [secform4 UHS insider trading (Form 4 filed 2026-11-12)](https://www.secform4.com/insider-trading/352915.htm?v=20261112R) — 2026-11-12
- [Quiver: Why Universal Health Services (UHS) Stock Is Down Today](https://www.quiverquant.com/news/Why+Universal+Health+Services+%28UHS%29+Stock+Is+Down+Today) — 2026-10-28
- [RBC raises UHS PT to $207 (Webull/Benzinga)](https://news-static.webullfintech.com/us/news-html/20261111/15905841601561600.html) — 2026-11-11
- [UHS Q3 2026 call transcript summary (Webull news item)](https://news-static.webullfintech.com/us/news-html/20261028/15826030502609920.html) — 2026-10-28
- Webull get_stock_bars daily, 210 sessions to 2026-11-12 (trend, SMA200, 6-month return); SPY 2026-05-14 close 744.40 → 2026-11-12 close 757.12

Data caveats: No Alpha Vantage call (not one of the 2 chosen names). Full pass, not abbreviated. Reddit: site:reddit.com search returned no reddit.com pages -> null. X: site:x.com search returned no x.com posts -> null. MarketBeat institutional pages failed (client_error) where tried. Institutions are Q2 2026 13F from Quiver (no totals). Webull profile 'CEO' field differs from secform4 title (Marc D. Miller President & CEO).
