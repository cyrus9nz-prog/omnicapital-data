Morning check 2026-11-18 5:44am PT

Alert pass only. Not a new analysis, and nothing here is an order or advice. Ratings change only in the trader's after-close run. Pre-market prices come from Webull get_stock_snapshot with extended hours, taken 5:41–5:44am PT (trade_status PRE), compared with the 2026-11-17 regular-session closes [SOURCED 2026-11-18 5:44am PT, Webull pre-market snapshot]. ADR(7) is the mean high−low of the 7 completed daily bars from 11-09 to 11-17, computed in code [SOURCED 2026-11-18, Webull daily bars]. Pre-market volume is thin on most names, so treat these prints as indicative.

## Market
- SPY $734.85, +0.33% vs the $732.44 close. QQQ $662.05, +0.78% vs $656.95. IWM $268.46, −0.22% vs $269.05 [SOURCED 2026-11-18 5:44am PT, Webull pre-market snapshot].
- Today's scheduled releases (PT) [SOURCED 2026-11-18, Webull macroeconomic calendar]:
  - 6:25am: Lagarde at DealBook.
  - 7:00am: October pending home sales. Forecast −2%, prior −7.3%.
  - 7:30am: EIA weekly crude stocks. Forecast −0.477M bbl, prior +4.657M. This one matters for OXY, EOG and APA.
  - 10:00am: 20-year bond auction.
  - 10:35am: Barr speaks.
  - 11:00am: FOMC minutes (Oct 27–28 meeting).
  - 11:30am: Williams speaks.
  - 1:00pm: TIC flows.
  - 1:15pm: Kashkari speaks.

## Alerts
1. **ADMA, pending buy-stop P-0010 (C-0083):** likely fills at the open.
   - Pre-market is $13.86, $0.19 above the $13.67 trigger.
   - That is inside 1×ADR(7) above the trigger ($0.604, so the line is $14.274). It has not gapped past the planned entry, so R-023 (don't chase) does not apply.
   - The quote is thin: 252 shares, bid $13.50 / ask $14.12.
   - Stop $12.76, target $15.48, as planned (R-044/R-045).
   - Review at today's close: the trader confirms whether it filled and whether the 11-18 bar is black.
2. **RYTM, pending buy-stop P-0009 (C-0082):** not at its trigger.
   - Pre-market is $115.00, 3.05% below the $118.51 trigger.
   - The extended-hours high was $119.80, above the trigger. The plan checks fills on the regular session, so the trader judges the fill from today's daily high.
   - If the stock opens at or above $118.51 + ADR(7) $6.498 = $125.01, R-023 says don't chase.
3. **PFE, open position P-0008 (C-0081): overnight news.**
   - Pfizer signed an exclusive license with Starna Therapeutics for three pre-IND in-vivo CAR-T programs. Terms: $330M upfront, up to $2.3B in milestones (Benzinga, 2026-11-18 3:49am PT) [SOURCED 2026-11-18, Webull get_stock_news].
   - Pre-market is $28.27, −0.69%. The stop is $24.16 (17.0% below) and the target is $37.09. Neither is at risk.
   - No dilution or red-flag content. It goes to the researcher for context only.

No stop, target or invalidation level is at risk in pre-market:
- OXY P-0005: $56.14 vs stop $50.56 (11.0% cushion), target $75.14, label line $69.86.
- No listed stock gapped ≥3% or by more than 1×ADR(7). The largest move is TGTX at +2.60% ($64.34 vs $62.71), with no overnight news; its ADR(7) is $3.965.

Near levels (no rule action; review at today's close):
- APA at $46.68 is $0.24 above the $46.44 line where its label drops from OVERVALUED to FAIR.
- DOC at $19.29 is below the $19.44 low end of its fair value. This does not change its label (UNDERVALUED only below $16.20).

## Quiet (17 stocks)
NBIX +0.05%, EOG +0.04%, PRU +0.63%, UPS −0.01%, OKE −0.40%, APA −0.43%, CF −0.45%, T −0.45%, AMCR −0.51%, O −0.60%, VICI −0.65%, OXY −0.67%, DOC −0.87%, VZ −0.89%, TGTX +2.60%, HIG and ACGL (no pre-market print; last close $136.22 and $109.22).

None of these had news since yesterday's 1pm PT close. The only overnight item across all 20 names was PFE's. VZ was tagged on a general FAA/Starlink story, which is not company-specific.

## Events, filings and insiders
- **Earnings today or tomorrow:** not sourced. Webull's earnings calendar gives no next date (config, 2026-11-11). All 20 names last reported between 2026-10-21 and 2026-11-09 (watchlist). No C6 IV-crush flag was raised for any options idea.
- **Dilution filings:** none seen. Webull get_stock_filings for PFE, RYTM, ADMA, OXY and TGTX lists only 10-Q/10-K filings, the latest dated 2026-11-03 to 11-09.
  - This check is incomplete. That source does not list 8-K, S-3, 424B or Form 144 filings. The SEC submissions JSON could not be fetched because this run had no WebFetch tool.
  - The other 15 names were not filing-checked. Known ATM flags carry over from the researcher: O, OKE, DOC, VICI.
- **Insider Form 4:** no new transactions since 2026-11-17 for RYTM, ADMA, PFE or OXY. The latest rows are dated 2026-10-02 or earlier [SOURCED 2026-11-18, Webull get_insider_transactions]. The other names were not checked this run.

## Sources
- Webull get_stock_snapshot, extended hours: 20 stocks plus SPY, QQQ and IWM, 5:41–5:44am PT.
- Webull get_stock_bars: daily, regular session, 10 bars per name to 2026-11-17.
- Webull get_stock_news: all 20 names.
- Webull get_macroeconomic_calendar: 2026-11-18.
- Webull get_stock_filings: 5 names.
- Webull get_insider_transactions: 4 names.
- Read first: claude/stock-desk-config.md, claude/watchlist.md (2026-11-17 11:48am run), claude/signals.md (2026-11-17 after close), claude/calls-ledger.md.
- Not used: stockanalysis.com, SEC EDGAR JSON (no WebFetch this run), Alpha Vantage (0 calls).
