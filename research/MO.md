# MO — researcher deep dive, 2026-11-12

Lane: S&P 500 · tested rules · Scout label: FAIR · Scout lean: Long · Close $77.92 [SOURCED 2026-11-12 close, Webull daily bar]
Scout list updated 2026-11-12 1:55pm PT (close run) — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 45 — Neutral — Aligned
Heat = round(0.6 × Substance 49 + 0.4 × Buzz 38) [computed in Python].

**Substance 49/100**
- Playbook fit 7/25: scout's fired rules R-058 A5, R-042 D1, R-025 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 10/20: scout label FAIR.
- Trend 15/15: above 200-day yes +5 (close 77.92 vs SMA200 68.04); 6-month return +10.96% vs SPY +1.71% (126 sessions from 2026-05-14) +5; R-050 ON +5 [SOURCED 2026-11-12, Webull daily bars; computed in code].
- Insiders 12/20: class buys1. Open-market BUY: director Kathryn McQuade 1,500 @ $67.62 on 2026-09-09 (~$101k). Sales: directors Kelly-Ennis 5,790 @ $72.25 and Strahlman 2,000 @ $72.56 (05-26; 10b5-1 not shown). Awards 05-13 (Mancuso 40,634) and 05-14 (directors 2,571 each; McQuade 4,656). Controller Patterson tax withholding 1,268 @ $71.56 (10-14).
- Institutions 5/10: flat_unknown. Unknown: MarketBeat institutional page failed (client_error).
- Catalysts 0/10: no dated positive catalyst (award, partner deal, approval) 2026-08-14..11-12 found.
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points)
- News tone 20/40: Alpha Vantage unavailable; no ticker news in the last 7 days → neutral 20.
- News volume 0/20: 0 items in 7 days vs 10 in the prior 4 weeks (weekly avg 2.50; ratio 0.00) [SOURCED 2026-11-12, Webull get_stock_news].
- Reddit slot 10/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 4 (mixed-positive (holders wanting to buy dips; one profit-taker)). X: null.

Note: Biggest driver: trend (15/15); biggest drag: catalyst (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- Strongest evidence for the scout's call: Q3 beat, FY EPS guide raised to $5.66-5.74, 61st consecutive dividend increase (+4.7%), $1B buyback expansion, and a director open-market buy (McQuade 09-09).
- Strongest evidence against: Secular cigarette decline (shipments -6.4%), negative equity, 88.5% payout ratio, FDA dependence for smoke-free growth; price $77.92 already above every PT opened this run.
- Long-term case: Marlboro pricing power grows profits slowly despite volume decline; buybacks and a rising dividend compound per-share returns. The long run depends on smoke-free (on!, NJOY) scaling past FDA hurdles; otherwise a high-yield melting ice cube.

## 1 Identity
Confirmed: Webull profile: Altria Group Inc, NYSE, CEO Salvatore Mancuso.

## 2 Filings (last 90 days)
10-Q + 8-K (2.02/8.01) 2026-10-29; S-3ASR 10-29 = shelf for debt securities/warrants for debt guaranteed by PM USA (not equity); 8-K 10-09 (1.01): $3.0B 5-yr revolver extended one year; 8-K 08-28 (5.02); Form 3 09-02, Form 4s 09-11 and 10-16. 10-K/A 05-27 (before window). No equity offering/ATM, going-concern or restatement seen.

## 3 Insiders (last 6 months)
Open-market BUY: director Kathryn McQuade 1,500 @ $67.62 on 2026-09-09 (~$101k). Sales: directors Kelly-Ennis 5,790 @ $72.25 and Strahlman 2,000 @ $72.56 (05-26; 10b5-1 not shown). Awards 05-13 (Mancuso 40,634) and 05-14 (directors 2,571 each; McQuade 4,656). Controller Patterson tax withholding 1,268 @ $71.56 (10-14). Cluster buying: no.

## 4 Institutions
Unknown: MarketBeat institutional page failed (client_error).

## 5 Government contracts
None found (not expected).

## 6 Connections
Subsidiaries PM USA, John Middleton, USSTC, Helix (on!), NJOY. Helix and NJOY suing the FDA over slow authorizations. on! PLUS 12mg national expansion; Helix shipments +13.3%. UK extended under-18 sales ban to nicotine products (10-29). Exposed to FDA policy and consumer pressure.

## 7 Sentiment
No Webull ticker news 11-06..11-12 vs 10 items 10-09..11-05 (Q3 beat, guide raised, dividend raise, PT changes). Motley Fool 11-10 (balanced): 5.8% yield more secure than it looks but payout ratio 88.5% and falling cigarette/oral volumes. Close $77.92 above all three opened PTs (MS $77, Citi $72, Barclays $60) and rising on no fresh news - price ahead of analysts. AV not called; Reddit/X unreadable.
Headlines: 2026-11-02 Barclays Underweight, PT raised to $60 | 2026-10-30 Morgan Stanley Equal-Weight PT $77; Citi Neutral PT $72 | 2026-10-29 Altria lifts profit forecast as pricing cushions volume declines (adj EPS $1.52, FY guide $5.66-5.74, dividend +4.7% to $1.11) | 2026-10-29 Altria files for debt shelf
Congressional trades: None found (no source loaded).

## 8 Red flags
No scored flag. Negative equity; payout 88.5% (Fool); cigarette volume decline; FDA authorization risk (lawsuit); securities-firm investigation into on! PLUS FDA statements (from ~08-01, per yesterday's report; not re-opened); price above PTs.

## What changed since yesterday's report
New this run: debt shelf identified as S-3ASR (debt only, no dilution); 8-K 10-09 $3.0B revolver extension; 8-K 08-28 item 5.02; Barclays UW PT $60 (11-02) seen; Fool 11-10 payout-ratio caution; Webull posts 4 in 7d (yesterday 4). No new red flags. The Levi & Korsinsky probe was not re-verified this run.

## Sources (opened this run, 2026-11-12)
- Webull get_company_profile MO (Webull get_company_profile MO) — 2026-11-12
- Webull get_stock_news MO (Webull get_stock_news MO) — 2026-11-12
- Webull get_insider_transactions MO (Webull get_insider_transactions MO) — 2026-11-12
- Webull get_stock_filings MO (Webull get_stock_filings MO) — 2026-11-12
- Webull get_community_posts MO (Webull get_community_posts MO) — 2026-11-12
- [SEC submissions CIK0000764180](https://data.sec.gov/submissions/CIK0000764180.json?v=20261112R) — 2026-11-12
- [secform4 Altria](https://www.secform4.com/insider-trading/764180.htm?v=20261112R) — 2026-11-12
- [autobound: Altria extends $3.0B revolver 8-K](https://www.autobound.ai/companies/altria/8-k/altria-extends-3-0b-revolving-credit-facility-to-october-e87a358e) — 2026-10-09
- [Motley Fool: Is Altria's 5.8% dividend yield too good?](https://fool.com/investing/2026/11/10/is-altria-58-dividend-yield-too-good-2027) — 2026-11-10
- [Benzinga via Webull: Altria lifts profit forecast](https://news-static.webullfintech.com/us/news-html/20261029/15832219715445760.html) — 2026-10-29
- [Benzinga via Webull: Altria files debt shelf](https://news-static.webullfintech.com/us/news-html/20261029/15832467450504192.html) — 2026-10-29
- Webull get_stock_bars daily, 210 sessions to 2026-11-12 (trend, SMA200, 6-month return); SPY 2026-05-14 close 744.40 → 2026-11-12 close 757.12

Data caveats: Alpha Vantage not called for MO (budget went to NBIX/UPS); MarketBeat institutional page client_error (one try); Reddit and X site searches returned no dated posts (null); secform4 shows no 10b5-1 flags so plan status is 'not shown'. S-3ASR debt-only status from Webull/Benzinga summary, not the filing itself. Securities-probe red flag carried from yesterday, not re-opened.
