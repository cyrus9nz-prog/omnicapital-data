# CMCSA — researcher deep dive, 2026-11-12

Lane: S&P 500 · tested rules · Scout label: UNDERVALUED · Scout lean: Long · Close $24.80 [SOURCED 2026-11-12 close, Webull daily bar]
Scout list updated 2026-11-12 1:55pm PT (close run) — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 36 — Cold — Aligned
Heat = round(0.6 × Substance 44 + 0.4 × Buzz 25) [computed in Python].

**Substance 44/100**
- Playbook fit 6/25: scout's fired rules R-056 A5, R-042 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 20/20: scout label UNDERVALUED.
- Trend 5/15: above 200-day no +0 (close 24.80 vs SMA200 25.28); 6-month return +1.42% vs SPY +1.71% (126 sessions from 2026-05-14) +0; R-050 ON +5 [SOURCED 2026-11-12, Webull daily bars; computed in code].
- Insiders 8/20: class none. Since 05-12 (secform4 + Webull): no open-market P or S. Director awards (A) 06-30 and 09-30 (Smith, Honickman, Breen, Brady, Baltimore). Co-CEO Cavanagh 958,411 and Roberts 382,860 code I (discretionary plan transactions) at $26.30 on 09-01. Gifts: Roberts 202,500 (05-19), 204,100 (08-05), 101,900 (09-02); Breen 62,440 (08-17). 10b5-1 status not shown.
- Institutions 5/10: flat_unknown. Not determined: MarketBeat institutional page failed (client_error). No 13F source opened.
- Catalysts 0/10: no dated positive catalyst (award, partner deal, approval) 2026-08-14..11-12 found.
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points)
- News tone 10/40: Alpha Vantage unavailable (rate-limit/premium errors) → scored from the past week's headlines (mostly positive 30, mixed 20, mostly negative 10).
- News volume 0/20: 1 items in 7 days vs 14 in the prior 4 weeks (weekly avg 3.50; ratio 0.29) [SOURCED 2026-11-12, Webull get_stock_news].
- Reddit slot 10/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 4 (negative-leaning (2 of 4 are $AENT promo; CMCSA posts '.' and 'no hope')). X: null.

Note: Biggest driver: value label (20/20); biggest drag: catalyst (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- Strongest evidence for the scout's call: Q3 FCF $4.2B and adj EPS $1.07 beat; Peacock profitable; cost transformation and mid-2027 separation could unlock value (Webull Q3 transcript/news 10-22).
- Strongest evidence against: Core broadband shrinking (-144k residential subs Q3, losses up 58% y/y), Connectivity revenue -2.6%, >1,000 job cuts, PT cuts, and zero open-market insider buying at multi-year lows.
- Long-term case: Doubtful compounder. Connectivity (most of profit) is losing broadband subs to fiber and FWA amid 'irrational' pricing; revenue flat. Upside rests on the mid-2027 NBCU/Sky separation, Peacock and cost cuts; FCF funds buybacks and the dividend. Cheap for a reason.

## 1 Identity
Confirmed: Webull profile: Comcast Corp, NASDAQ, CEO Brian L. Roberts; matches ticker.

## 2 Filings (last 90 days)
Since 2026-08-14 (SEC submissions): 10-Q + 8-K (2.02) 10-22; 25-NSE 09-14 (delisting notice, likely a debt class; not opened); Form 4s 08-18, 09-03 x2, 10-02 x5. No S-3/424B/144/13D in window. No going-concern, auditor change or restatement seen. Q3 call: >$1B Q4 cost-transformation charge flagged.

## 3 Insiders (last 6 months)
Since 05-12 (secform4 + Webull): no open-market P or S. Director awards (A) 06-30 and 09-30 (Smith, Honickman, Breen, Brady, Baltimore). Co-CEO Cavanagh 958,411 and Roberts 382,860 code I (discretionary plan transactions) at $26.30 on 09-01. Gifts: Roberts 202,500 (05-19), 204,100 (08-05), 101,900 (09-02); Breen 62,440 (08-17). 10b5-1 status not shown. Cluster buying: no.

## 4 Institutions
Not determined: MarketBeat institutional page failed (client_error). No 13F source opened.

## 5 Government contracts
No material new federal award found. Search surfaced only older state broadband awards (e.g. Pennsylvania CPF >$61M, article 2024-05-02, outside window). Immaterial to revenue.

## 6 Connections
Peacock 48M paid subs, profitable ($261M adj EBITDA Q3); 10.6M wireless lines (MVNO); Sky-ITV merger under UK investigation (11-04); Jio technology-licensing talks (Reuters sources, rumour, 11-03). NBCU/Sky separation targeted mid-2027. Rivals' fiber/FWA pricing (AT&T fiber ARPU -4%) hurts Connectivity.

## 7 Sentiment
News volume fell: 1 item in 7d vs 14 in prior 28d (weekly avg 3.5); the only 7d item is negative (job cuts). Webull posts few and negative. AV null; Reddit/X unreadable. Price $24.80 (11-12 close, scout) near lows and below 200-day; sentiment and price aligned (both weak), no divergence.
Headlines: 2026-11-09 Bloomberg via Benzinga: Comcast planning >1,000 job cuts in Connectivity & Platforms ahead of separation (negative) | 2026-11-04 UK opens investigation into Sky-ITV merger | 2026-11-03 Reuters: Jio held talks to license tech to Comcast, Charter for shares | 2026-10-23 TD Cowen PT $39->$36 (Buy); Evercore PT ->$29 (Outperform)
Congressional trades: None found (no source opened showed congressional trades).

## 8 Red flags
No scored flag. Broadband -144k, video -274k; parks adj EBITDA -17.1%; >$1B Q4 restructuring charge; >1,000 job cuts; analyst PT cuts; no insider buying.

## What changed since yesterday's report
No new filings or news since 11-09. New detail from secform4: Co-CEOs' 09-01 code-I plan transactions (Cavanagh 958,411; Roberts 382,860 at $26.30) and Roberts gifts (05-19, 08-05, 09-02) — not open-market, not scored. Close fell $25.02 -> $24.80. No new red flags.

## Sources (opened this run, 2026-11-12)
- Webull get_company_profile (Webull get_company_profile) — 2026-11-12
- Webull get_stock_filings (Webull get_stock_filings) — 2026-11-12
- Webull get_insider_transactions (Webull get_insider_transactions) — 2026-11-12
- Webull get_stock_news (Webull get_stock_news) — 2026-11-12
- Webull get_community_posts (US_STOCK) (Webull get_community_posts) — 2026-11-12
- [Comcast job cuts (Bloomberg via Benzinga/Webull)](https://news-static.webullfintech.com/us/news-html/20261109/15896459446513664.html) — 2026-11-09
- [Comcast calls rival pricing 'irrational' (Webull)](https://news-static.webullfintech.com/us/news-html/20261022/15792335820399616.html) — 2026-10-22
- [SEC submissions CIK0001166691](https://data.sec.gov/submissions/CIK0001166691.json?v=20261112R) — 2026-11-12
- [secform4 Comcast](https://www.secform4.com/insider-trading/1166691.htm?v=20261112R) — 2026-11-12
- [Stocktwits: CMCSA CFO sees no improvement in broadband losses (dated 2026-09-09, context only)](https://stocktwits.com/news-articles/markets/equity/cmcsa-cfo-sees-no-improvement-in-broadband-user-losses/cZt7kt5RJCc) — 2026-09-09
- [Telecompetitor: Comcast Pennsylvania funding win (2024, outside window)](https://www.telecompetitor.com/comcast-formally-announces-pennsylvania-funding-win/) — 2024-05-02
- Webull get_stock_bars daily, 210 sessions to 2026-11-12 (trend, SMA200, 6-month return); SPY 2026-05-14 close 744.40 → 2026-11-12 close 757.12

Data caveats: Alpha Vantage NEWS_SENTIMENT returned premium/rate-limit error (1 call, not retried) -> null. MarketBeat institutional page client_error (1 try). Reddit and X WebSearch returned no dated posts 11-05..11-12 -> null (unreadable). News counts are all items Webull get_stock_news returned for the symbol (includes market roundups tagging the ticker). secform4 first fetch rate-limited, second succeeded. 25-NSE not opened. SEC submissions JSON read to char 100000 only (recent filings fully covered). Ticker-tagged CMCSA items in prior 28d ~9 of 14.
