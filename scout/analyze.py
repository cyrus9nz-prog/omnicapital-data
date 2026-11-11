import json, math, statistics as st, datetime as dt
import numpy as np

SPY = np.array(open('/home/claude/desk/spy.txt').read().split(), float)
import os
LIVE = json.load(open('/home/claude/desk/live_snap.json')) if os.environ.get('LIVE') else None
LIVE_DATE = '2026-11-11'
SPY_6M = (762.3005 if LIVE else SPY[0]) / SPY[126] - 1

def ema(closes_oldest_first, n):
    k = 2 / (n + 1)
    e = np.mean(closes_oldest_first[:n])
    for c in closes_oldest_first[n:]:
        e = c * k + e * (1 - k)
    return e

def rsi(closes_oldest_first, n=14):
    d = np.diff(closes_oldest_first)
    g = np.where(d > 0, d, 0); l = np.where(d < 0, -d, 0)
    ag = g[:n].mean(); al = l[:n].mean()
    for i in range(n, len(d)):
        ag = (ag * (n - 1) + g[i]) / n; al = (al * (n - 1) + l[i]) / n
    return 100 - 100 / (1 + ag / al) if al > 0 else 100

spy_old = SPY[::-1]
SPY_EMA12, SPY_EMA50 = ema(spy_old, 12), ema(spy_old, 50)

FIN = {'SYF', 'PRU', 'HIG', 'VICI', 'O'}  # use OCF instead of FCF
SP = {'CVS','VICI','SYF','T','PRU','VZ','MO','CMCSA','FIS','UPS','PFE','O','HIG','EOG','UHS'}

def FY(r):
    return r.get('fiscal_year') or int(str(r['period_end'])[:4])

def num(x):
    try:
        return None if x is None else float(x)
    except Exception:
        return None

def nearest_month_close(monthly, date):
    d0 = dt.date.fromisoformat(date)
    best = min(monthly, key=lambda m: abs((dt.date.fromisoformat(m['date']) - d0).days))
    if abs((dt.date.fromisoformat(best['date']) - d0).days) > 20:
        return None
    return best['close']

def analyze(t):
    d = json.load(open(f'/home/claude/desk/data/{t}.json'))
    daily = d['daily']
    closes = np.array([b['close'] for b in daily], float)  # newest first
    price, pdate = closes[0], daily[0]['date']
    if LIVE and t in LIVE:
        price, pdate = float(LIVE[t]['price']), LIVE_DATE
    old = closes[::-1]
    n_ret = min(252, len(closes) - 1)
    lr = np.diff(np.log(old[-(n_ret + 1):]))
    sig = lr.std(ddof=1)
    r1 = (price * math.exp(-sig * math.sqrt(21)), price * math.exp(sig * math.sqrt(21)))
    r3 = (price * math.exp(-sig * math.sqrt(63)), price * math.exp(sig * math.sqrt(63)))
    sma50, sma200 = closes[:50].mean(), closes[:200].mean()
    e12, e50 = ema(old, 12), ema(old, 50)
    rsi14 = rsi(old[-120:])
    ret6 = price / closes[126] - 1
    vol20 = np.mean([b['volume'] for b in daily[:20]])
    dollar_vol = vol20 * price

    iq = d['income_quarterly']; ia = d['income_annual']
    cq = d['cashflow_quarterly']; ca = d['cashflow_annual']
    bq = d['balance_quarterly']; ba = d['balance_annual']
    q4 = iq[:4]
    def s4(rows, k):
        v = [num(r.get(k)) for r in rows[:4]]
        return None if any(x is None for x in v) or len(v) < 4 else sum(v)
    eps_gaap = s4(iq, 'eps_diluted')
    eps_norm = s4(iq, 'eps_diluted_normalized') if all(r.get('eps_diluted_normalized') is not None for r in iq[:4]) else None
    eps_ttm = eps_norm if eps_norm is not None else eps_gaap
    eps_basis = 'normalized' if eps_norm is not None else 'GAAP'
    rev_ttm = s4(iq, 'revenue'); opi_ttm = s4(iq, 'operating_income')
    rev_prev = None
    if len(iq) >= 8:
        rev_prev = sum(num(r['revenue']) for r in iq[4:8])
        try:
            opi_prev = sum(num(r['operating_income']) for r in iq[4:8])
        except Exception:
            opi_prev = None
    else:
        opi_prev = None
    ocf_ttm = s4(cq, 'operating_cash_flow')
    fcf_ttm = s4(cq, 'free_cash_flow')
    shares = num(bq[0]['shares_outstanding'])
    eq = num(bq[0]['total_equity']) - (num(bq[0].get('preferred_equity')) or 0)
    debt = num(bq[0]['total_debt']) or 0
    cash = num(bq[0].get('cash_and_equivalents'))
    bvps = eq / shares
    pb = price / bvps if bvps > 0 else None
    pe = price / eps_ttm if eps_ttm and eps_ttm > 0 else None
    ocfps = ocf_ttm / shares if ocf_ttm else None
    pcf = price / ocfps if ocfps and ocfps > 0 else None
    de = debt / eq if eq > 0 else None
    # quarterly P/CF (latest quarter OCF annualized)
    q_ocf = num(cq[0]['operating_cash_flow'])
    pcf_q = price / (q_ocf * 4 / shares) if q_ocf and q_ocf > 0 else None
    # EPS q/q and sales y/y
    e0, e1 = num(iq[0].get('eps_diluted')), num(iq[1].get('eps_diluted'))
    eps_qq = (e0 / e1 - 1) if e0 is not None and e1 and e1 > 0 else None
    sales_yy = num(iq[0]['revenue']) / num(iq[4]['revenue']) - 1 if len(iq) >= 5 else None
    # dividends
    ttm_dps = None
    dq = [num(r.get('dps')) for r in iq[:4]]
    if all(x is not None for x in dq) and all(x > 0 for x in dq):
        ttm_dps = sum(dq)
    snap_y = num(d['snapshot'].get('yield'))
    yld = snap_y * 100 if snap_y is not None else (ttm_dps / price * 100 if ttm_dps else None)
    # analyst
    a = d.get('analyst') or {}
    w = {'strong_buy': 1, 'buy': 2, 'hold': 3, 'under_perform': 4, 'sell': 5}
    cnt = {k: int(a.get(k) or 0) for k in w}
    ntot = sum(cnt.values())
    arate = sum(w[k] * cnt[k] for k in w) / ntot if ntot else None

    # own-history multiples: unadjust dividend-adjusted month-end closes
    fys = [r for r in ia if r.get('period_end')][:5]
    hist = []
    for r in fys:
        padj = nearest_month_close(d['monthly'], r['period_end'])
        if padj is None:
            continue
        hist.append((r, padj))
    # approximate un-adjustment: divide by product of (1 - dps_k / P_k) for later fiscal years and 2026 YTD
    dps_by_year = {FY(r): num(r.get('dps')) for r in ia}
    ytd = sum(num(r.get('dps')) or 0 for r in iq if str(r['period_end']).startswith('2026'))
    hist2 = []
    for r, padj in hist:
        fy = FY(r)
        f = 1.0
        later = [(y, v) for y, v in dps_by_year.items() if y > fy and v]
        for y, v in later:
            py = next((p for rr, p in hist if FY(rr) == y), price)
            f *= (1 - v / py)
        if ytd and fy < 2026:
            f *= (1 - ytd / price)
        praw = padj / f
        hist2.append((r, praw, padj))
    pe_h, pcf_h, pb_h, y_h = [], [], [], []
    for r, praw, padj in hist2:
        fy = FY(r)
        e = num(r.get('eps_diluted_normalized')) if eps_basis == 'normalized' and r.get('eps_diluted_normalized') is not None else num(r.get('eps_diluted'))
        if e and e > 0:
            pe_h.append(praw / e)
        sh = num(r.get('shares_diluted'))
        cfr = next((c for c in ca if FY(c) == fy), None)
        if cfr and sh:
            v = num(cfr.get('operating_cash_flow')) if t in FIN else num(cfr.get('free_cash_flow'))
            if v and v > 0:
                pcf_h.append(praw / (v / sh))
        br = next((b for b in ba if FY(b) == fy), None)
        if br and num(br.get('shares_outstanding')):
            beq = num(br['total_equity']) - (num(br.get('preferred_equity')) or 0)
            if beq > 0:
                pb_h.append(praw / (beq / num(br['shares_outstanding'])))
        dv = dps_by_year.get(fy)
        if dv:
            y_h.append(dv / praw * 100)
    methods = {}; excluded = {}
    def ok(h, name):
        if len(h) < 3:
            excluded[name] = f'only {len(h)} usable years'; return False
        if name != 'book' and st.median(h) > 40:
            excluded[name] = f'own median multiple {st.median(h):.0f}x (history distorted by small or one-off profits)'; return False
        return True
    pe_h = pe_h if ok(pe_h, 'earnings') else []
    pcf_h = pcf_h if ok(pcf_h, 'cashflow') else []
    pb_h = pb_h if ok(pb_h, 'book') else []
    if pe_h and eps_ttm and eps_ttm > 0:
        methods['earnings'] = (eps_ttm * st.median(pe_h), st.median(pe_h), len(pe_h))
    cf_ttm = ocf_ttm if t in FIN else fcf_ttm
    if pcf_h and cf_ttm and cf_ttm > 0:
        methods['cashflow'] = (cf_ttm / shares * st.median(pcf_h), st.median(pcf_h), len(pcf_h))
    if pb_h and bvps > 0:
        methods['book'] = (bvps * st.median(pb_h), st.median(pb_h), len(pb_h))
    ups = {k: v[0] / price - 1 for k, v in methods.items()}
    above = sum(1 for u in ups.values() if u >= 0.20)
    below = sum(1 for u in ups.values() if u <= -0.20)
    if len(methods) < 2:
        label = "CAN'T TELL"
    elif above >= 2:
        label = 'UNDERVALUED'
    elif below >= 2:
        label = 'OVERVALUED'
    else:
        label = 'FAIR'
    pos = sum(1 for u in ups.values() if u > 0); neg = sum(1 for u in ups.values() if u < 0)
    disagree = pos > 0 and neg > 0 and label == 'FAIR'
    # label change thresholds: price at which 2nd-highest fair value is 20% above (undervalued) / 2nd lowest 20% below
    fv = sorted(v[0] for v in methods.values())
    thr_under = fv[-2] / 1.2 if len(fv) >= 2 else None
    thr_over = fv[1] / 0.8 if len(fv) >= 2 else None

    # annual revenue trend
    ra = sorted([(r['period_end'], num(r['revenue'])) for r in ia if num(r.get('revenue'))])
    last4 = ra[-4:]
    rev_rising = all(last4[i + 1][1] > last4[i][1] for i in range(len(last4) - 1)) and len(last4) >= 4
    opm = opi_ttm / rev_ttm if opi_ttm is not None and rev_ttm else None
    opm_prev = opi_prev / rev_prev if opi_prev is not None and rev_prev else None
    ea = d['earnings'] or {}
    beat = None
    if ea.get('last_eps_actual') is not None and ea.get('last_eps_estimate') is not None:
        beat = num(ea['last_eps_actual']) > num(ea['last_eps_estimate'])
    si = d.get('short_interest_pct_float')
    sval = None
    if isinstance(si, dict):
        v = si.get('value_pct', si.get('value'))
        if v is not None:
            sval = float(str(v).replace('%', ''))
    elif si is not None:
        try: sval = float(str(si).replace('%', ''))
        except: pass
    return dict(t=t, d=d, price=price, pdate=pdate, sig=sig, n_ret=n_ret, r1=r1, r3=r3, sma50=sma50, sma200=sma200,
                e12=e12, e50=e50, rsi=rsi14, ret6=ret6, vol20=vol20, dollar_vol=dollar_vol, eps_ttm=eps_ttm,
                eps_basis=eps_basis, eps_gaap=eps_gaap, pe=pe, pb=pb, pcf=pcf, pcf_q=pcf_q, de=de, bvps=bvps,
                debt=debt, cash=cash, eq=eq, shares=shares, rev_ttm=rev_ttm, ocf_ttm=ocf_ttm, fcf_ttm=fcf_ttm,
                eps_qq=eps_qq, sales_yy=sales_yy, yld=yld, ttm_dps=ttm_dps, y5=(st.mean(y_h) if len(y_h) >= 5 else (st.mean(y_h) if y_h else None)),
                ny5=len(y_h), arate=arate, ntot=ntot, methods=methods, excluded=excluded, ups=ups, label=label, disagree=disagree,
                thr_under=thr_under, thr_over=thr_over, ra=ra, rev_rising=rev_rising, opm=opm, opm_prev=opm_prev,
                beat=beat, ea=ea, short=sval, q10=d.get('latest_10q_period'))

if __name__ == '__main__':
    import sys
    R = {}
    for t in ['CVS','VICI','SYF','T','PRU','VZ','MO','CMCSA','FIS','UPS','PFE','O','HIG','EOG','UHS','RYTM','TGTX','NBIX','EXEL','ADMA']:
        r = analyze(t); R[t] = r
        m = ' '.join(f"{k}:{v[0]:.2f}({r['ups'][k]*100:+.0f}%,x{v[1]:.2f},n{v[2]})" for k, v in r['methods'].items())
        print(f"{t:5} {r['price']:.2f} {r['pdate']} {r['label']}{' disagree' if r['disagree'] else ''} | {m}")
        f = lambda x, p=2: 'NA' if x is None else f'{x:.{p}f}'
        print(f"   PE{f(r['pe'])}({r['eps_basis']} {f(r['eps_ttm'])}) PB{f(r['pb'])} PCF{f(r['pcf'])} PCFq{f(r['pcf_q'])} DE{f(r['de'])} rate{f(r['arate'])}/{r['ntot']} yld{f(r['yld'])} y5{f(r['y5'])}(n{r['ny5']}) short{r['short']} | epsqq{f(r['eps_qq'],3)} salesyy{f(r['sales_yy'],3)} RSI{f(r['rsi'],1)} beat{r['beat']}")
        print(f"   SMA50 {r['sma50']:.2f} SMA200 {r['sma200']:.2f} EMA12 {r['e12']:.2f} EMA50 {r['e50']:.2f} 6m {r['ret6']*100:.1f}% vol20 {r['vol20']/1e6:.2f}M sig {r['sig']:.4f} revRising {r['rev_rising']} opm {f(r['opm'],3)} vs {f(r['opm_prev'],3)} q10 {r['q10']}")
    print('SPY 6m', SPY_6M, 'SPY EMA12/50', SPY_EMA12, SPY_EMA50)
