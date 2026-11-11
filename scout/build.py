import json, sys
sys.path.insert(0, '/home/claude/desk')
from analyze import analyze, SPY_6M, SPY_EMA12, SPY, FY
import numpy as np

SRC = '[SOURCED 2026-11-11 ~10:47am PT, Webull snapshot, intraday]'
SA = '[SOURCED 2026-11-11 page, stockanalysis; short-interest date not shown, one web source]'
PREV = {'CVS': 'UNDERVALUED', 'VICI': 'UNDERVALUED', 'SYF': 'FAIR', 'T': 'FAIR', 'PRU': 'FAIR', 'VZ': 'FAIR',
        'MO': 'FAIR', 'EXEL': 'FAIR', 'TGTX': "CAN'T TELL"}
SHORT_OVR = {'UPS': 3.49, 'O': 4.05, 'VZ': 2.01, 'EOG': 3.33, 'NBIX': 6.45, 'ADMA': 8.98}
LAST_RPT = {}
SECT = {'CVS': 'Health Care', 'VICI': 'Real Estate (REIT)', 'SYF': 'Financials', 'T': 'Communication Services',
        'PRU': 'Financials (insurance)', 'VZ': 'Communication Services', 'MO': 'Consumer Staples',
        'CMCSA': 'Communication Services', 'UPS': 'Industrials', 'PFE': 'Health Care', 'O': 'Real Estate (REIT)',
        'HIG': 'Financials (insurance)', 'EOG': 'Energy', 'UHS': 'Health Care', 'RYTM': 'Biotech',
        'TGTX': 'Biotech', 'NBIX': 'Biotech', 'EXEL': 'Biotech', 'ADMA': 'Biotech'}
CAVEAT = {
 'CVS': 'Q3-2025 carried a $5.24B one-off charge and Q4-2025 a $1.57B tax benefit, so GAAP history is noisy.',
 'VICI': 'Q3-2026 net income fell to $343M from $527M (about $190M extra expense, possibly a credit-loss reserve; check the 10-Q) and EPS missed the estimate.',
 'SYF': 'Consumer-credit lender: earnings swing with charge-offs; short interest 5.32% of float.',
 'T': 'Q3-2026: $3.38B one-off charge and debt up $15.7B alongside a $20.2B intangibles increase (likely spectrum; check the 10-Q).',
 'PRU': 'Analyst average is worse than hold (13 hold, 2 underperform, 3 sell); unrealized investment losses -$34.2B at 2026-09-30.',
 'VZ': 'Goodwill +$7.8B and PP&E +$16B in Q1-2026 (acquisition closing; check the 10-Q); revenue growth only +1.5% y/y.',
 'MO': 'Negative shareholder equity, so book value and D/E are not meaningful; revenue flat (+1.0% y/y).',
 'CMCSA': 'A 2026 spin-off shrank the company (goodwill -$8.1B in Q1-2026), so pre-2026 multiples describe a bigger business; revenue -6.1% y/y and operating margin down.',
 'UPS': 'FY2025 free cash flow ($4.77B) did not cover dividends paid ($5.40B); EPS missed the estimate.',
 'PFE': 'FY2025 dividends paid ($9.77B) exceeded free cash flow ($9.08B); GAAP P/E 42 on one-off charges.',
 'O': 'REIT funded by share issuance (361M shares in 2020 to about 951M); GAAP P/E 41 is not a REIT measure.',
 'HIG': 'Q2/Q3-2026 include discontinued items and goodwill fell (likely a divestiture; check the 10-Q).',
 'EOG': 'Oil-price exposure; FY2025 had an $878M unusual charge.',
 'UHS': 'Q3-2026 acquisition (goodwill +$755M, debt +$873M); short interest 5.56% of float; EPS missed the estimate.',
 'RYTM': 'Loss-making with negative operating cash flow; short interest 19.47% of float.',
 'TGTX': 'Q3-2026 statements not yet in the data; FY2025 profit includes a $340M tax benefit; FCF negative every year 2020–2025; short interest 21.88%.',
 'NBIX': 'Own-history multiples come from years of fast growth, which flatters the cash-flow method; Q2-2026 acquisition added $2.7B of goodwill and intangibles; RSI 72.5 (overbought).',
 'EXEL': 'Book value is small after heavy buybacks, so the book method sits far below price; short interest 13.06%.',
 'ADMA': 'Operating cash flow well below net income (inventory and receivables growing); debt up to $197M in Q1-2026; short interest 8.98%; fell about 42% in March 2026.',
}

def f(x, p=2):
    return 'n/a' if x is None else f'{x:,.{p}f}'

TESTED = ['HIG','EOG','CVS','UHS','CMCSA','SYF','VICI','PFE','O','PRU','T','VZ','UPS','MO']
SMALL = ['NBIX','EXEL','RYTM','TGTX','ADMA']
R = {t: analyze(t) for t in TESTED + SMALL}
for t, v in SHORT_OVR.items():
    R[t]['short'] = v

# R-056 / R-058 passers and D/E ranks
def r056(r):
    return (r['pe'] is not None and r['pe'] < 20 and r['pb'] is not None and r['pb'] < 8 and r['pcf'] is not None
            and r['pcf'] < 10 and r['arate'] is not None and r['arate'] <= 3.0)
def r058(r):
    return (r['yld'] or 0) > 4 and (r['y5'] or 0) > 4 and r['short'] is not None and r['short'] < 5
p56 = sorted([t for t in TESTED if r056(R[t])], key=lambda t: R[t]['de'])
p58 = sorted([t for t in TESTED if r058(R[t])], key=lambda t: (R[t]['de'] is None, R[t]['de'] or 0))
print('R-056 passers', [(t, round(R[t]['de'], 2)) for t in p56])
print('R-058 passers', [(t, R[t]['de'] and round(R[t]['de'], 2)) for t in p58])

rows, md = [], []
for t in TESTED + SMALL:
    r = R[t]; d = r['d']
    lane = 'S&P 500 · tested rules' if t in TESTED else 'Small/mid · untested rules'
    fired, failed = [], []
    if t in TESTED:
        leg = f"P/E {f(r['pe'])} on TTM {r['eps_basis']} EPS ${f(r['eps_ttm'])} (<20), P/B {f(r['pb'])} (<8), P/CF {f(r['pcf'])} on TTM OCF (<10), analyst average {f(r['arate'])} of {r['ntot']} (1 strong buy … 5 sell; hold or better ≤3), D/E {f(r['de'])}"
        if t in p56:
            rk = p56.index(t) + 1
            fired.append(f"R-056 value screen: {leg} — rank {rk} of {len(p56)} by lowest D/E" + (' (inside the top 6)' if rk <= 6 else ' (outside the top 6 the rule holds)'))
        else:
            failed.append(f"R-056: {leg}")
        yl = f"yield {f(r['yld'])}% (>4), 5-yr average yield {f(r['y5'])}% (>4; FY dividends ÷ month-end prices un-adjusted for dividends [ESTIMATED]), short interest {f(r['short'])}% of float (<5)"
        if t in p58:
            fired.append(f"R-058 dividend screen: {yl} — rank {p58.index(t)+1} of {len(p58)} by lowest D/E" + (' (negative equity, ranked last)' if r['de'] is None else ''))
        else:
            failed.append(f"R-058: {yl}")
    else:
        ra = r['ra'][-4:]
        fired.append('R-043 rising revenue: ' + ' → '.join(f"FY{p[:4]} ${v/1e6:,.0f}M" for p, v in ra) + f"; latest quarter {r['sales_yy']*100:+.1f}% y/y")
        fired.append(f"Trend reading (R-025 + own R-026 legs): close {f(r['price'])} > 200-day SMA {f(r['sma200'])}; EMA12 {f(r['e12'])} > EMA50 {f(r['e50'])}, price above both")
        fired.append(f"R-027/R-020 liquidity: 20-day average volume {r['vol20']/1e6:.2f}M shares (~${r['dollar_vol']/1e6:,.0f}M a day), price above $1")
    # common
    if r['beat'] is not None:
        txt = f"R-042: last EPS {r['ea']['last_eps_actual']} vs estimate {round(float(r['ea']['last_eps_estimate']),2)} (reported {r['ea'].get('last_report_date')})"
        (fired if r['beat'] else failed).append(txt + (' — beat' if r['beat'] else ' — miss'))
    if t in TESTED:
        txt = f"R-025: close {f(r['price'])} vs 200-day SMA {f(r['sma200'])}"
        (fired if r['price'] > r['sma200'] else failed).append(txt)
    g_ok = (r['eps_qq'] is not None and r['eps_qq'] > 0.05 and r['sales_yy'] is not None and r['sales_yy'] > 0.05
            and r['pcf_q'] is not None and r['pcf_q'] < 8 and r['rsi'] < 70)
    gtxt = f"R-057: EPS q/q {f(r['eps_qq']*100 if r['eps_qq'] is not None else None,1)}% (>5), sales y/y {f(r['sales_yy']*100,1)}% (>5), P/CF on latest quarter annualised {f(r['pcf_q'])} (<8), RSI(14) {f(r['rsi'],1)} (<70)"
    if t in TESTED:
        (fired if g_ok else failed).append(gtxt)
    failed.append(f"R-026: market leg fails (SPY EMA12 {SPY_EMA12:.2f} < EMA50 761.32); sector leg not sourced")
    failed.append('R-055 can\'t fire (no consensus-EPS history source)')
    # value
    meth = '; '.join(f"{k} ({'latest book value' if k=='book' else 'TTM'} × own {v[2]}-FY median {'P/E' if k=='earnings' else ('P/OCF' if k=='cashflow' and t in {'SYF','PRU','HIG','VICI','O'} else ('P/FCF' if k=='cashflow' else 'P/B'))} {v[1]:.2f}): ${v[0]:.2f} ({r['ups'][k]*100:+.0f}%)" for k, v in r['methods'].items())
    if r['excluded']:
        meth += '; excluded: ' + '; '.join(f"{k} — {v}" for k, v in r['excluded'].items())
    meth += ' [ESTIMATED from SOURCED Webull statements and month-end closes]'
    fvs = [v[0] for v in r['methods'].values()]
    label = r['label']
    fv = f"${min(fvs):.2f}–${max(fvs):.2f}" if len(fvs) >= 2 else ('— (one usable method: ' + ', '.join(f"{k} ${v[0]:.2f}" for k, v in r['methods'].items()) + ')' if fvs else '—')
    if label == "CAN'T TELL":
        trig = 'Needs two usable valuation methods: positive, steady earnings or free cash flow for 3+ years.'
    else:
        trig = (f"UNDERVALUED below ${r['thr_under']:.2f}" if label != 'UNDERVALUED' else f"Drops to FAIR above ${r['thr_under']:.2f} (fewer than 2 methods ≥20% above price)")
        trig += f"; OVERVALUED above ${r['thr_over']:.2f}" if label != 'OVERVALUED' else ''
        trig += '; the next 10-Q changes the inputs.'
    if t in p58:
        trig += ' R-058 fails if short interest reaches 5% of float or yield drops to 4%.'
    # profile
    traits = []
    rg = r['sales_yy']; traits.append(rg is not None and rg > 0.25)
    traits.append(r['opm'] is not None and r['opm_prev'] is not None and r['opm'] > r['opm_prev'])
    traits.append(bool(r['beat']))
    traits.append(r['price'] > r['sma200'])
    traits.append(r['ret6'] > SPY_6M)
    unknown = 1 if (r['opm'] is None or r['opm_prev'] is None) else 0
    k = sum(traits)
    word = {'CVS': 'turnaround', 'VICI': 'income', 'SYF': 'value', 'T': 'income', 'PRU': 'income', 'VZ': 'income',
            'MO': 'income', 'CMCSA': 'cheap for a reason', 'UPS': 'income', 'PFE': 'income', 'O': 'income',
            'HIG': 'value', 'EOG': 'value', 'UHS': 'value', 'RYTM': 'speculative growth', 'TGTX': 'speculative growth',
            'NBIX': 'compounder', 'EXEL': 'compounder', 'ADMA': 'speculative growth'}[t]
    profile = f"{k} of 5 big-winner traits" + (f" ({unknown} unknown: operating-margin line not reported)" if unknown else '') + f" — {word}"
    lean = 'Long' if label != 'OVERVALUED' else 'Neither'
    names = [x.split(':')[0].split(' ')[0] for x in fired if x.startswith('R-0')]
    main = ', '.join(dict.fromkeys(names))
    why = {
        'tested': f"Passes the A-graded {' and '.join(n for n in ['R-056','R-058'] if n in names)} screen{'s' if ('R-056' in names and 'R-058' in names) else ''} on sourced data; label {label}" + (' (methods disagree)' if r['disagree'] else '') + '.',
        'small': f"Growth/momentum fit (untested lane): revenue up each year (R-043), above its 200-day with its 12/50 EMA legs up; label {label}.",
    }['tested' if t in TESTED else 'small']
    q = 'margins ' + (f"op margin {r['opm']*100:.1f}% TTM" if r['opm'] is not None else 'n/a') + f", D/E {f(r['de'])}, TTM FCF ${f(r['fcf_ttm']/1e9 if r['fcf_ttm'] else None)}B"
    long_term = f"Fair value {fv} vs ${r['price']:.2f}; {q}. Main risk: {CAVEAT[t]}"
    nxt = f"not sourced (last reported {r['ea'].get('last_report_date')}; Webull and stockanalysis show no next date)"
    status = 'kept'
    rr = r
    row = dict(ticker=t, company=d['company'], sector=SECT[t], universe=lane, price=round(float(r['price']), 2),
               price_date=r['pdate'], label=label, fair_value=fv,
               range_1m=f"${r['r1'][0]:.2f}–${r['r1'][1]:.2f}", range_3m=f"${r['r3'][0]:.2f}–${r['r3'][1]:.2f}",
               lean=lean, profile=profile, why=why, long_term=long_term, next_earnings=nxt, change_trigger=trig,
               rules_fired=fired, status=status, added='2026-11-10')
    rows.append(row)
    md.append('| ' + ' | '.join([
        t, lane, label + (' (methods disagree)' if r['disagree'] else ''), fv, f"${r['price']:.2f} {SRC}", meth,
        '**Fired:** ' + '; '.join(fired) + '. **Failed / can\'t fire:** ' + '; '.join(failed) + '. R-050 ON.',
        f"price {r['pdate']} intraday (averages and σ from closes to 2026-11-10); statements to {r['q10']}" + (f"; short interest {SA}" if r['short'] is not None else ''),
        nxt, trig,
        f"${r['r1'][0]:.2f}–${r['r1'][1]:.2f} [ESTIMATED: σ {r['sig']:.4f} of {r['n_ret']} daily log returns]",
        f"${r['r3'][0]:.2f}–${r['r3'][1]:.2f}", lean, profile, why]).replace('\n', ' ') + ' |')

json.dump(rows, open('/home/claude/desk/watchlist.json', 'w'), indent=1, ensure_ascii=False)
open('/home/claude/desk/table.md', 'w').write('\n'.join(md))
for row in rows:
    print(row['ticker'], row['label'], row['price'], row['fair_value'], row['profile'], row['status'])
print('SPY 6m', SPY_6M)
