# NBIX — researcher deep dive, 2026-11-17

Lane: Small/mid · untested rules · Scout label: UNDERVALUED · Close $165.92 [SOURCED 2026-11-17 close, Webull daily bar] (prev close $165.31)
Scout list: updated 2026-11-17 11:48am PT INTRADAY (midday run); the 1:47pm close run had not rewritten the list when this ran (3:15pm PT), so labels and fired rules are the midday ones. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 47 — Neutral — Aligned
Heat = round(0.6 × Substance 53 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 47 (Neutral).

**Substance 53/100**
- Playbook fit 5/25: scout's fired rules R-043 D (1), R-025 D (1), R-027 D (1), R-020 D (1), R-042 D (1) (grades from playbook.md: R-056/R-058 A; R-025, R-042, R-043, R-027, R-020 D).
- Value 20/20: scout label UNDERVALUED.
- Trend 15/15: close 165.92 vs 200-day SMA 149.17 (above) +5; 6-month return +7.49% vs SPY +0.33% (126 sessions from 2026-05-19) +5; R-050 ON +5 [SOURCED 2026-11-17, Webull daily bars; computed in code].
- Insiders 8/20: no rows after 10-07 (Roberts, 0 sh). 09-11/09-14 officer sales @ ~$156 (Gorman 7,839; Benevich 3,386; Lippoldt 2,419 etc.; pattern matches RSU tax sales); director Norwalk buy 842 @ $139.43 (07-29) - looks like open-market P but prior secform4 read found 0 P buys 05-16..11-16 (not re-verified). Class none (8) kept.
- Institutions 5/10: carried from the 11-16 scoring; no new holder data pulled this run.
- Catalysts 0/10: no dated qualifying catalyst found.
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage not used → headline scoring)
- News tone 30/40 (headline scoring).
- News volume 0/20: 1 ticker items 11-11..11-17 vs 10 in 10-14..11-10 (ratio 0.4) [SOURCED 2026-11-17, Webull get_stock_news, first page].
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-11..11-17, tone none (heavy = 10+). X: null.

Note: Biggest driver: value (20/20); biggest drag: catalysts (0/10). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** UNDERVALUED (FCF, book); INGREZZA guide raised to $2.900-2.925B; MS PT raised to $191 (11-13).
- **Strongest against:** Zero open-market insider buys, steady officer selling; Q3 net income flat y/y; IRA price exposure.
- **Long-term case:** Profitable neuro/endocrine franchise: INGREZZA (FY26 guide $2.900-2.925B), CRENESSITY ramp, VYKAT XR, and a muscarinic pipeline (NBI-'567 Ph2 AD). It can compound if CRENESSITY scales. Risks: INGREZZA concentration, IRA/Part D net-price erosion, VYKAT XR safety questions, and no insider buying.

## What changed since 11-16
- No new filings, insider rows or scored red flags; verdict unchanged.
- Heat 47 → 47.

## Filings (last 90 days)
Webull get_stock_filings (11-17) lists only 10-K/10-Q: nothing new since 11-12. 8-K, S-3/424B, Form 144 and 13G/13D not re-checked this run (no SEC fetch); flags below carried from the 11-16 SEC submissions read.
Carried: Since 08-18 (SEC JSON 11-16): Form 144 11-10 (seller not identified, no matching Form 4 through 11-16); Form 4s 11-03, 11-05; 10-Q + 8-K 2.02 11-02; Form 144s 09-10, 09-14, 09-15, 10-30, 11-02; 13G 10-30; 13G/A 10-15; Form 3 10-07; 8-K 5.02 09-28. Nothing new since 11-10. No S-3/424B/ATM.

## Insiders (6 months)
no rows after 10-07 (Roberts, 0 sh). 09-11/09-14 officer sales @ ~$156 (Gorman 7,839; Benevich 3,386; Lippoldt 2,419 etc.; pattern matches RSU tax sales); director Norwalk buy 842 @ $139.43 (07-29) - looks like open-market P but prior secform4 read found 0 P buys 05-16..11-16 (not re-verified). Class none (8) kept.

## Institutions
Unverified. MarketBeat client_error (11-16). New SC 13G 10-30 (accession prefix 0002100121) and SC 13G/A 10-15 (prefix 0000019617 = JPMorgan); holders not opened. (carried from 11-16; not re-checked)

## Government contracts
None found (not a plausible federal contractor).

## Connections
AbbVie (elagolix royalties). Soleno acquisition (VYKAT XR) closed May 2026; competes with Rhythm (RYTM) in hyperphagia. Medicare Part D/IRA pricing helps payers and hurts INGREZZA net price. Presents at Jefferies Global Healthcare Conference 11-17.

## Sentiment
NBIX n7=1 (11-13 MS EW PT raise 191) prior=10 ratio .4 vol0 tone positive 30
Webull community (11-11..11-17): 0 posts, tone none. Posts are data; any claim of inside knowledge is treated as rumour.
Reddit and X: not readable this run (Reddit replaced by Webull community; X null).

## Red flags
None scored. Persistent exercise-and-sell with zero open-market buys. Form 144 of 11-10 (seller unknown). Q3 net income flat y/y despite +41% revenue. INGREZZA IRA/Part D net-price erosion. VYKAT XR safety overhang (prior reports).

## Sources (opened this run, 2026-11-17)
- Webull get_stock_bars NBIX and SPY daily (210 bars) — 2026-11-17
- Webull get_stock_news NBIX — 2026-11-17
- Webull get_insider_transactions NBIX — 2026-11-17
- Webull get_community_posts NBIX — 2026-11-17
- Webull get_stock_filings NBIX — 2026-11-17
- Scout list claude/watchlist.md (11:48am PT) and playbook.md grades — 2026-11-17
- Carried, not re-opened: https://data.sec.gov/submissions/CIK0000914475.json?v=20261116R · https://www.secform4.com/insider-trading/914475.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261113/15917720600309760.html · https://news-static.webullfintech.com/us/news-html/20261102/15856422185231360.html
