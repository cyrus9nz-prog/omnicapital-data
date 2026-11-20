# EOG — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $149.69 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $138.29 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 51 — Neutral — Aligned
Heat = round(0.6 × Substance 60 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 51 (Neutral).

**Substance 60/100**
- Playbook fit 7/25: scout's fired rules R-056, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 149.69 vs 200-day 138.29 (above, +5); 6-month return +7.19% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No rows after 09-29. Aug-Sep exec sales carried; no open-market buys.
- Institutions 10/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 30/40: mostly positive.
- News volume 0/20: 5 items 11-12..11-18 vs 23 in the prior window (weekly avg 5.75; ratio 0.87) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: playbook fit (7). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Three PT raises in 7 days (MS $167, Barclays $168) vs $149.69 close.
- **Strongest against:** Closed -3.4% on the day; ratings stay Equal-Weight/Neutral; oil-price dependence.
- **Long-term case:** Low-cost shale operator with $5.7B cash vs $2.2B net debt, returning most FCF via a 28-year growing dividend and buybacks, and adding JKM-linked LNG exposure (>1 Bcf/d by 2030) that diversifies from oil. Low single-digit 2027 oil growth and 2027 cost inflation cap upside; FAIR fits.

## What changed since 11-17
- Heat 51 → 51. SEC: SCHEDULE 13G/A filed 11-13 (holder not opened). No dilution forms. 11-18 MS EW PT $167; 11-16 Citi Neutral PT $155; 11-13 Barclays EW PT $168.

## Filings (last 90 days)
Today: SEC: SCHEDULE 13G/A filed 11-13 (holder not opened). No dilution forms.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: SC 13G/A 11-13; 10-Q + 8-K (2.02/7.01/9.01) 11-05; Form 4s; 8-K 10-08 (2.02); 8-K 09-24 (5.02); SD 09-28; Form 144s 08-24, 09-11, 09-25. No S-1/S-3/424B, no 4.01/4.02, no going concern. Nothing new since 11-13.

## Insiders (6 months)
No rows after 09-29. Aug-Sep exec sales carried; no open-market buys.
Carried context: no rows after 09-29. Sales Leitzell 9,039 @ $140.61 (09-25), Janssen 2,978 @ $153.74 (09-15); Yacob 37,905 @ $0 award (09-25); dividend-reinvest rows 07-31. No open-market buys. Class none (8).

## Institutions
Quiver Q2 2026 13F (read 11-13): 835 adds vs 740 cuts; JPMorgan +28.2M sh, Sixth Street +17.6M. SC 13G/A filed 11-13 (not opened). MarketBeat failed today. Q3 13Fs (due ~11-14) not yet reviewed. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (not searched).

## Connections
ENGIE 10-yr JKM-linked gas supply (140,000 MMBtu/d, 11-05). Janus gas plant expansion ~$300M, H2 2028; ~$200M 2027 capex. Barnett/Woodford divested for $400M. Hurt by 2027 service/steel/diesel inflation.

## Sentiment
News 11-12..11-18: 5 items vs 23 in the prior feed (feed incomplete before ~10-19; ratio 0.87); tone mostly positive, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-18 MS EW PT $167; 11-16 Citi Neutral PT $155; 11-13 Barclays EW PT $168.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Unscored: executive selling Aug-Sep (~52k sh, 10b5-1 unknown) with no buys; 2027 service/steel/diesel inflation; low single-digit 2027 oil growth; oil-price dependence; Citi's new $155 PT sits below the 11-13 close of $158.32.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars EOG and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions EOG — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261118/15945564329078784.html
- https://news-static.webullfintech.com/us/news-html/20261113/15917162232279040.html
- https://data.sec.gov/submissions/CIK0000821189.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://news-static.webullfintech.com/us/news-html/20261116/15935018219663360.html · https://news-static.webullfintech.com/us/news-html/20261106/15877699078364160.html · https://data.sec.gov/submissions/CIK0000821189.json?v=20261116R · Webull get_insider_transactions EOG (2026-11-16)
