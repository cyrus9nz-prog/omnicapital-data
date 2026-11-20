# CVS — researcher deep dive, 2026-11-12

Lane: S&P 500 · tested rules · Scout label: FAIR · Scout lean: Long · Close $89.79 [SOURCED 2026-11-12 close, Webull daily bar]
Scout list updated 2026-11-12 1:55pm PT (close run) — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 42 — Neutral — Aligned
Heat = round(0.6 × Substance 44 + 0.4 × Buzz 38) [computed in Python].

**Substance 44/100**
- Playbook fit 7/25: scout's fired rules R-056 A5, R-042 D1, R-025 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 10/20: scout label FAIR.
- Trend 10/15: above 200-day yes +5 (close 89.79 vs SMA200 88.01); 6-month return -6.34% vs SPY +1.71% (126 sessions from 2026-05-14) +0; R-050 ON +5 [SOURCED 2026-11-12, Webull daily bars; computed in code].
- Insiders 12/20: class buys1. Open-market BUY: EVP/Group President Prem Shah (future CVS Pharmacy CEO) 23,855 sh @ $83.895 on 11-06 (~$2.0M; holdings +36.9% to 88,516) per Quiver; Form 4 filed 11-06. Sales since 05-12: director Larry Robbins 370,462 @ $93.45 (05-21, Webull; Quiver: 7 sales, 3,372,000 sh ~$317.5M over 6 mo). Smaller 05-31/06-26 sales @ $90.98 look like vest withholding. Director awards 05-14. 10b5-1 not shown.
- Institutions 5/10: flat_unknown. Quiver (13F Q2 2026): 977 institutions added vs 967 reduced. Adds: JPMorgan +22.1M (new), BofA +13.8M (+148%), Sixth Street +13.3M, Wellington +11.2M (+49.8%), GQG +7.9M. Cuts: Invesco -4.5M (-18.1%), Wells Fargo -4.4M (-54.6%). Roughly balanced -> flat. MarketBeat failed.
- Catalysts 0/10: no dated positive catalyst (award, partner deal, approval) 2026-08-14..11-12 found.
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points)
- News tone 20/40: Alpha Vantage unavailable (rate-limit/premium errors) → scored from the past week's headlines (mostly positive 30, mixed 20, mostly negative 10).
- News volume 0/20: 4 items in 7 days vs 21 in the prior 4 weeks (weekly avg 5.25; ratio 0.76) [SOURCED 2026-11-12, Webull get_stock_news].
- Reddit slot 10/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 5 (mixed (1 'bearish', trader level calls '90 GO', 'alert')). X: null.

Note: Biggest driver: trend (10/15); biggest drag: catalyst (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- Strongest evidence for the scout's call: Future CVS Pharmacy CEO Prem Shah bought ~$2.0M on the open market 11-06 (first insider buy in ~17 months per Quiver) after guidance was raised to >$8.20 (2026) and >=$8.65 (2027).
- Strongest evidence against: Analysts keep cutting targets (WF to $112 on 11-12, UBS $107, Leerink $104); PBM transparency rule and break-up legislation threaten Caremark; director Robbins sold ~$317M of stock in May.
- Long-term case: Turnaround, not a quality compounder: if Aetna margins keep recovering (2027 guide >=$8.65, ~13% growth) and the 2028 split unlocks value, shares can compound from a depressed base with ~3% yield. PBM regulation, Medicare Advantage rates and shrinking retail pharmacy are the risks.

## 1 Identity
Confirmed: Webull profile: CVS Health Corp, NYSE, CEO J. David Joyner; Health Care Benefits (Aetna), Health Services (Caremark), Pharmacy & Consumer Wellness. Matches.

## 2 Filings (last 90 days)
Since 2026-08-14 (SEC submissions): 10-Q 11-04; 8-Ks 11-04 (2.02 results; 7.01 separation announcement); 13F-HR 11-05; Form 4 11-06 (Shah buy); 8-K 08-17 (5.02/7.01). No S-1/S-3/424B/S-8/144, no NT 10-Q, no 4.01/4.02. 10-Q: Omnicare asset sale probable Q4, $193M guarantee liability. $315M DOJ opioid settlement (10-13).

## 3 Insiders (last 6 months)
Open-market BUY: EVP/Group President Prem Shah (future CVS Pharmacy CEO) 23,855 sh @ $83.895 on 11-06 (~$2.0M; holdings +36.9% to 88,516) per Quiver; Form 4 filed 11-06. Sales since 05-12: director Larry Robbins 370,462 @ $93.45 (05-21, Webull; Quiver: 7 sales, 3,372,000 sh ~$317.5M over 6 mo). Smaller 05-31/06-26 sales @ $90.98 look like vest withholding. Director awards 05-14. 10b5-1 not shown. Cluster buying: no.

## 4 Institutions
Quiver (13F Q2 2026): 977 institutions added vs 967 reduced. Adds: JPMorgan +22.1M (new), BofA +13.8M (+148%), Sixth Street +13.3M, Wellington +11.2M (+49.8%), GQG +7.9M. Cuts: Invesco -4.5M (-18.1%), Wells Fargo -4.4M (-54.6%). Roughly balanced -> flat. MarketBeat failed.

## 5 Government contracts
No dated federal award found (search 'CVS Health contract award 2026 VA DoD TRICARE' surfaced only military-community PR and a HigherGov awardee page, not opened). Medicare/Medicaid are reimbursement, not contracts.

## 6 Connections
Split into CVS Health (Aetna, Caremark, Specialty, Oak Street, Signify; CEO Joyner) and CVS Pharmacy (~9,000 stores, MinuteClinic, mail; CEO Prem Shah) by H1 2028, tax-free. Headwinds: DOL PBM fee-disclosure rule (effective July); Warren/Hawley 'Break Up Big Medicine Act'; Omnicare sale with DOJ minimum $440M. Possible tailwind: state Medicaid expansion (STAT, 11-10).

## 7 Sentiment
Webull news 4 in 7d vs 21 in prior 28d (earnings/split burst 11-03..11-05 and opioid settlement 10-13); 7d tone mixed: PT cuts while ratings stay Buy/Overweight, PBM-policy noise. 5 Webull posts in 7d, mixed. Reddit/X unreadable. Divergence: beat-and-raise 11-04 but stock fell on the split news; analysts keep cutting targets ($107-$112) yet all remain above the $89.79 close.
Headlines: 2026-11-12 Wells Fargo maintains Overweight, lowers PT to $112 | 2026-11-09 Mark Cuban attacks healthcare conglomerates/PBMs; 'Break Up Big Medicine Act' cited | 2026-11-06 UBS maintains Buy, lowers PT to $107 | 2026-11-04 CVS raises 2026 adj EPS guide to >$8.20, 2027 >=$8.65; confirms split into two companies
Congressional trades: None found (Quiver pages did not cover congressional trades).

## 8 Red flags
No scored flag. Unscored: $315M DOJ opioid FCA settlement (10-13); $193M Omnicare guarantee liability; ~$317M director (Glenview) sales in May, plan status unknown; PBM disclosure rule and Break Up Big Medicine Act; separation execution risk; continued PT cuts.

## What changed since yesterday's report
New: Wells Fargo cut PT to $112 (Overweight) on 11-12; Shah buy re-verified via Quiver (Webull insider feed does not show it yet). Prior-28d news count is 21 with full pagination (yesterday 16). No new filings since 11-06; no new red flags. Close $89.79 vs $89.52.

## Sources (opened this run, 2026-11-12)
- Webull get_company_profile CVS (Webull get_company_profile CVS) — 2026-11-12
- Webull get_insider_transactions CVS (Webull get_insider_transactions CVS) — 2026-11-12
- Webull get_stock_news CVS (2 pages) (Webull get_stock_news CVS (2 pages)) — 2026-11-12
- Webull get_community_posts CVS (Webull get_community_posts CVS) — 2026-11-12
- Webull get_stock_filings CVS (Webull get_stock_filings CVS) — 2026-11-12
- [SEC submissions CIK0000064803 (CVS)](https://data.sec.gov/submissions/CIK0000064803.json?v=20261112R) — 2026-11-12
- [Quiver: CVS Group President Buys $2 Million in Stock, Ending 17-Month Insider Buying Gap](https://www.quiverquant.com/news/CVS+Group+President+Buys+%242+Million+in+Stock%2C+Ending+17-Month+Insider+Buying+Gap) — 2026-11
- [Quiver: CVS Releases Q3 2026 Earnings (institutions, insiders)](https://www.quiverquant.com/news/CVS+HEALTH+%28%24CVS%29+Releases+Q3+2026+Earnings) — 2026-11-04
- [Wells Fargo lowers CVS PT to $112 (Webull/Benzinga)](https://news-static.webullfintech.com/us/news-html/20261112/15911208960389120.html) — 2026-11-12
- [CVS raises outlook, confirms breakup (Webull/Benzinga)](https://news-static.webullfintech.com/us/news-html/20261104/15866783399517184.html) — 2026-11-04
- Webull get_stock_bars daily, 210 sessions to 2026-11-12 (trend, SMA200, 6-month return); SPY 2026-05-14 close 744.40 → 2026-11-12 close 757.12

Data caveats: Alpha Vantage NEWS_SENTIMENT rate-limited (HIG called twice: rate limit then premium error; CVS once: rate limit) -> null. Note: 3 AV calls made vs 2 allowed (one retry on HIG). secform4 CVS rate-limited twice (not read); Shah buy confirmed via Quiver + SEC Form 4 filing date only; Robbins sale size differs by source (Webull 370,462 sh 05-21; Quiver 3,372,000 sh over 7 sales). MarketBeat CVS failed (client_error). Reddit/X null as above. Institutions are Q2 2026 13F.
