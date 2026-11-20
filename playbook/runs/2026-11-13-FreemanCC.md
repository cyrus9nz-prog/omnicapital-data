# Run report 2026-11-13 — FreemanCC (Covered Calls for Beginners, Freeman Publications, 2020)
Read loc.1–119 of 119 (END OF BOOK).
New rules: 11 — options-income 10 (R-143 gain-cushion base, R-144 regime gate C, R-145 strike by volatility state, R-146 underlying screen, R-147 strike by delta, R-148 1% roll, R-149 2&20 buy-back, R-150 defend near strike, R-151 expiry 30–45d, R-153 poor man's covered call), risk/sizing 1 (R-152 code red on fraud allegation, C). Grades: C 2, D 9.
Merged: 2 (R-076 event gate; R-048 paper trading). Conflicts: 1 new (R-146 vs R-077 on IV ceiling, decided by structure).
Principles: 12 new + 2 agreements (delta ≈ ITM chance; Choppiness > 61.8).
Flags: "risk-free" framing not carried; worked-number errors (loc.32–33, 44, 85, 93–94, 100); tax/IRA chapters out of scope; S&P covered-call chart not converted (check figure loc.62); Aug 2020 candidates without outcomes.
Test first: R-144 regime gate — the inputs (ADX, Choppiness from daily OHLC) are fully computable, so a backtest of monthly ~0.30–0.40-delta covered calls written only when ADX<25 vs always-on can settle whether the gate adds anything over buy-and-hold, which the book's own chart says plain covered calls trail.
