# SYF — researcher deep dive, 2026-11-12

Lane: S&P 500 · tested rules · Scout label: FAIR · Scout lean: Long · Close $71.66 [SOURCED 2026-11-12 close, Webull daily bar]
Scout list updated 2026-11-12 1:55pm PT (close run) — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 30 — Cold — Aligned
Heat = round(0.6 × Substance 34 + 0.4 × Buzz 25) [computed in Python].

**Substance 34/100**
- Playbook fit 6/25: scout's fired rules R-056 A5, R-042 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 10/20: scout label FAIR.
- Trend 5/15: above 200-day no +0 (close 71.66 vs SMA200 72.85); 6-month return +1.46% vs SPY +1.71% (126 sessions from 2026-05-14) +0; R-050 ON +5 [SOURCED 2026-11-12, Webull daily bars; computed in code].
- Insiders 8/20: class none. Since 05-12 (Webull): no officer open-market buys. Director 'BUY' rows are quarter-end equal-size lots (846 sh @ $70.97, 09-30) = deferred comp, not open-market. Sales: Mothner 11,258 @71.23 (05-15); CEO Doubles 2,353 @77.12 (07-28); Tiliakos 1,738 @75.79 (07-31); Coviello 4,000 @77.17, Gentleman 721, Owens 610 (08-03); Casellas 5,456 @80 (08-13). 10b5-1 not shown.
- Institutions 5/10: flat_unknown. Not determined: MarketBeat institutional page failed (client_error). No 13F source opened.
- Catalysts 0/10: no dated positive catalyst (award, partner deal, approval) 2026-08-14..11-12 found.
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points)
- News tone 20/40: Alpha Vantage unavailable; no ticker news in the last 7 days → neutral 20.
- News volume 0/20: 0 items in 7 days vs 10 in the prior 4 weeks (weekly avg 2.50; ratio 0.00) [SOURCED 2026-11-12, Webull get_stock_news].
- Reddit slot 0/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 0 (none (latest post 10-25)). X: null.

Note: Biggest driver: value label (10/20); biggest drag: catalyst (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- Strongest evidence for the scout's call: Q3 EPS $2.68 beat, FY26 EPS guide raised to $9.50, RoTCE 25.2%, CET1 12.9%, $1.2B returned in Q3 (Webull Q3 transcript 10-20).
- Strongest evidence against: No insider buying with steady officer/director selling; Evercore downgrade and UBS PT cut; price below 200-day; APR-cap regulatory risk.
- Long-term case: Moderate compounder: high returns (RoTCE 25.2%) and buybacks drive per-share growth, with large partner programs (Walmart/OnePay, Venmo, CareCredit). But it is cyclical consumer credit with APR-cap policy exposure, so returns track the credit cycle.

## 1 Identity
Confirmed: Webull profile: Synchrony Financial, NYSE, CEO Brian D. Doubles; matches ticker.

## 2 Filings (last 90 days)
Since 2026-08-14 (SEC submissions): 8-K 11-10 (7.01/9.01; exhibit is monthly credit-stats tables — contents not read); 10-Q 10-22; 8-Ks 10-20 (2.02 earnings; 7.01); 8-K 09-14 (7.01); 8-K 08-17; Form 144 08-17; Form 4s 08-19 (x20), 10-02 (x11). No S-3/424B/13D. No going-concern, auditor change or restatement seen.

## 3 Insiders (last 6 months)
Since 05-12 (Webull): no officer open-market buys. Director 'BUY' rows are quarter-end equal-size lots (846 sh @ $70.97, 09-30) = deferred comp, not open-market. Sales: Mothner 11,258 @71.23 (05-15); CEO Doubles 2,353 @77.12 (07-28); Tiliakos 1,738 @75.79 (07-31); Coviello 4,000 @77.17, Gentleman 721, Owens 610 (08-03); Casellas 5,456 @80 (08-13). 10b5-1 not shown. Cluster buying: no.

## 4 Institutions
Not determined: MarketBeat institutional page failed (client_error). No 13F source opened.

## 5 Government contracts
None found (not a plausible federal contractor; not searched beyond news).

## 6 Connections
Q3: record Q3 purchase volume ~$50B (+8%); Venmo and Stripe partnerships expanded, OpenAI integration, CareCredit Pay Later (Q3 call 10-20). Big retail partner programs (Walmart/OnePay). Credit-card APR-cap proposal is a policy overhang for issuers; consumer-credit cycle drives losses.

## 7 Sentiment
No Webull news in 7d vs 10 in prior 28d; no community posts in 7d. Recent tone mixed: beat-and-raise vs downgrade/PT cuts. AV null; Reddit/X unreadable. Mild divergence: fundamentals/guidance positive while price $71.66 (11-12 close, scout) sits below its 200-day and ~$80 August levels.
Headlines: 2026-11-02 UBS Neutral, PT lowered to $80 | 2026-10-21 Evercore downgrade to In-Line (PT $78); Barclays PT $93->$94; JPM PT ->$77 | 2026-10-20 Q3 EPS $2.68 vs ~$2.43 est; FY26 EPS guide raised to $9.50 | 2026-10-12 Morgan Stanley PT ->$83; JPM PT ->$74
Congressional trades: None found.

## 8 Red flags
No scored flag. APR-cap policy risk; Evercore downgrade; UBS PT cut 11-02; insider selling, no buys; short interest 5.32% of float per scout (just above R-058's 5% line).

## What changed since yesterday's report
New: 8-K filed 11-09/accepted 11-10 (Item 7.01, monthly credit-stats exhibit) — contents not read (EDGAR Archives blocked); yesterday listed it only as Reg FD. UBS PT cut to $80 (11-02) now in the window. No new insider trades after 10-02. Close $72.02 -> $71.66. No new scored red flags.

## Sources (opened this run, 2026-11-12)
- Webull get_company_profile (Webull get_company_profile) — 2026-11-12
- Webull get_stock_filings (Webull get_stock_filings) — 2026-11-12
- Webull get_insider_transactions (Webull get_insider_transactions) — 2026-11-12
- Webull get_stock_news (Webull get_stock_news) — 2026-11-12
- Webull get_community_posts (US_STOCK) (Webull get_community_posts) — 2026-11-12
- [SYF Q3 call transcript (Webull)](https://news-static.webullfintech.com/us/news-html/20261020/15780728075660288.html) — 2026-10-20
- [Analysts revise SYF forecasts (Webull)](https://news-static.webullfintech.com/us/news-html/20261021/15786724632767488.html) — 2026-10-21
- [SEC submissions CIK0001601712](https://data.sec.gov/submissions/CIK0001601712.json?v=20261112R) — 2026-11-12
- [last10k: SYF 8-K 0001601712-26-000045](https://last10k.com/sec-filings/syf/0001601712-26-000045.htm) — 2026-11-10
- [Quantisnow: Synchrony & Planet DDS partnership (2026-02-18, outside window)](https://quantisnow.com/insight/synchrony-and-planet-dds-expand-strategic-partnership-to-integrate-carecredit-6398502) — 2026-02-18
- Webull get_stock_bars daily, 210 sessions to 2026-11-12 (trend, SMA200, 6-month return); SPY 2026-05-14 close 744.40 → 2026-11-12 close 757.12

Data caveats: Alpha Vantage NEWS_SENTIMENT returned premium/rate-limit error (1 call, not retried) -> null. MarketBeat institutional page client_error (1 try). Reddit and X WebSearch returned no dated posts 11-05..11-12 -> null (unreadable). News counts are all items Webull get_stock_news returned for the symbol (includes market roundups tagging the ticker). secform4 not fetched this run (rate limits on secform4); deferred-comp reading of director 'BUY' rows is inferred from the equal-lot quarter-end pattern plus yesterday's secform4 check. 11-10 8-K credit stats not read. SEC JSON partly inconsistent (Form 144 acceptance date).
