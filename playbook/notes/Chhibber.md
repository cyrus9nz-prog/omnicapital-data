# Notes — Chhibber (read 2026-11-09 in chat, p.1–p.5, END OF BOOK reached)
p.1  Proposes Neural Prophet + deep neural net (NP-DNN) for price prediction; abstract claims 99.21% accuracy.
p.2  Method: z-score normalisation, interpolation of missing values, MLP features, Optuna tuning. DATASET = Crunchbase startup/funding/LinkedIn data (p.2), not stock price series.
p.3  Model equations only (MLP, dense/softmax layers, NP trend+seasonality+holiday terms). No trading rule.
p.4  Results reported as classification metrics (accuracy/precision/recall/F1); results text says 93.21% (conflicts with p.1's 99.21%). No out-of-sample period, no trading P&L, no benchmark vs buy-and-hold.
p.4  Discussion: authors say historical prices alone are limited because outside events drive volatility; suggest adding news/microblog data. (principle, D)
p.5  References only.
Rules: none — no measurable IF/THEN; the only "evidence" is a model-accuracy claim on non-price data.
Flags: accuracy inconsistent (p.1 vs p.4); dataset mismatch (p.2); classification metrics for a price-forecast claim.
