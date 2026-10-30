"""Living Pond model v3. Weekly step of 7 daily substeps. Matter in units (dots), exactly conserved.
Pools: N water and air (carbon dioxide, water, minerals), Af floating algae (green water), As algae on
stems and stones, S snails, M[0..7] minnows by shade (0 pale silver .. 7 dark olive), Dn dragonfly nymphs,
D decomposers (bacteria, fungi, worms), Det muck (dead stuff and droppings), F fish food flakes.
Turtles and herons are adults that do not grow: what they eat is breathed out (to N) or dropped (to Det).
Energy: each unit of matter algae build stores 10 energy units of sunlight; each unit breathed out by
anything (algae, animals, decomposers) releases its 10 units as heat."""
import math

WEEKS = 52
SUB = 7
BINS = 8
W = {'snail': 0.5, 'minnow': 2.0, 'dragon': 0.5, 'turtle': 30.0, 'algae': 5.0}

P = dict(
    ra=1.4, KN=40.0, Afmax=900.0, Asmax=500.0, shade=250.0,
    a_resp=0.08, a_die=0.05,
    assim=0.7,
    sp=dict(
        snail=dict(cmax=1.0, H=100.0, eff=0.30, maint=0.07, mort=0.02),
        minnow=dict(cmax=1.0, H=100.0, eff=0.30, maint=0.07, mort=0.015),
        dragon=dict(cmax=0.7, H=35.0, eff=0.30, maint=0.07, mort=0.02),
        decomp=dict(cmax=1.5, H=100.0, eff=0.20, maint=0.08, mort=0.10),
    ),
    turtle_c=1.2, turtle_H=40.0,
    heron_c=1.6, heron_H=10.0,
    po=0.05, co=0.05, kr=0.6,
    vis_base=0.15, clear50=400.0,
    ref=dict(Af=15.0, As=15.0, S=4.0, M=6.0, Dn=1.0, D=2.0),
    sun0=70000.0,
)

def temp(w):
    return 13 - 11 * math.cos(2 * math.pi * (w - 46) / 52)
def tf(T):
    return 2 ** ((T - 20) / 10)
def ice(w):
    return temp(w) < 4.0
def sunsurf(w):
    return 0.6 + 0.4 * math.cos(2 * math.pi * (w - 14) / 52)
def light(w):
    return sunsurf(w) * (0.3 if ice(w) else 1.0)
def osat(T):
    return 14.6 - 0.39 * T + 0.007 * T * T

def new_pond(**kw):
    s = dict(week=0, N=300.0, Af=80.0, As=70.0, S=40.0, M=[0.0] * BINS, Dn=12.0, D=20.0, Det=150.0, F=0.0,
             turtles=1, herons=1, heron_here=True, heron_bad=0, turtle_bad=0, decomp_on=True,
             O=10.0, bottom=1.0,
             ledger=dict(added=0.0, removed=0.0, left=0.0),
             energy=dict(sun=0.0, caught=0.0, heat=0.0), hist=[], log=[])
    for k in range(2, 6):
        s['M'][k] = 10.0
    s.update(kw)
    return s

def Mt(s): return sum(s['M'])
def living(s): return s['Af'] + s['As'] + s['S'] + Mt(s) + s['Dn'] + s['D'] + s['turtles'] * W['turtle']
def total(s): return s['N'] + living(s) + s['Det'] + s['F']
def ident(s):
    L = s['ledger']; return total(s) - L['added'] + L['removed'] + L['left']
def mean_color(s):
    m = Mt(s); return sum(k * s['M'][k] for k in range(BINS)) / m if m > 0 else float('nan')

def substep(s, dt, w, acc):
    p = P; sp = p['sp']; R = p['ref']
    T = temp(w); f = tf(T); Lt = light(w); iced = ice(w)
    N, Af, As, S, Dn, D, Det, F = (s[k] for k in ('N', 'Af', 'As', 'S', 'Dn', 'D', 'Det', 'F'))
    Mb = s['M']; m = sum(Mb)
    out = {}
    def o(src, amt, tag):
        if amt > 0: out.setdefault(src, []).append([tag, amt])
    # algae: build from water and air; floating algae shade the algae on stems and stones
    nut = N / (N + p['KN'])
    Gf = p['ra'] * Lt * f * Af * nut * max(0.0, 1 - Af / p['Afmax']) * dt
    Ls = Lt / (1 + Af / p['shade'])
    Gs = p['ra'] * Ls * f * As * nut * max(0.0, 1 - As / p['Asmax']) * dt
    if Gf + Gs > N:
        sc = N / (Gf + Gs); Gf *= sc; Gs *= sc
    die = p['a_die'] * (1.6 if Lt < 0.35 else 1.0) * dt
    o('Af', p['a_resp'] * f * Af * dt, ('to', 'N')); o('Af', die * Af, ('to', 'Det'))
    o('As', p['a_resp'] * f * As * dt, ('to', 'N')); o('As', die * As, ('to', 'Det'))
    def feed(name, B, prey):
        c = sp[name]; P_ = sum(wt * a for _, wt, a in prey)
        if B <= 0 or P_ <= 0: return
        I = c['cmax'] * f * B * P_ / (c['H'] + P_) * dt
        for pool, wt, a in prey:
            o(pool, I * wt * a / P_, ('eat', name))
    Afe, Ase = max(0.0, Af - R['Af']), max(0.0, As - R['As'])
    Se, me, De = max(0.0, S - R['S']), max(0.0, m - R['M']), max(0.0, Dn - R['Dn'])
    feed('snail', S, [('As', 1, Ase)])
    feed('minnow', m, [('Af', 1, Afe), ('F', 3, F)])
    feed('dragon', Dn, [('S', 1, Se), ('M', 0.5, me)])
    if s['decomp_on']:
        feed('decomp', D, [('Det', 1, Det)])
    tneed = s['turtles'] * p['turtle_c'] * f * dt
    if s['turtles'] > 0 and T >= 10:
        prey = [('S', 1, Se), ('Dn', 0.5, De), ('M', 0.5, me), ('As', 0.3, Ase)]
        P_ = sum(wt * a for _, wt, a in prey)
        if P_ > 0:
            I = tneed * P_ / (p['turtle_H'] + P_)
            for pool, wt, a in prey: o(pool, I * wt * a / P_, ('eat', 'turtle'))
    clarity = 1.0 / (1.0 + (Af / p['clear50']) ** 2)
    vis = [p['vis_base'] + (1 - p['vis_base']) * abs(k - s['bottom']) / 7.0 * clarity for k in range(BINS)]
    hneed = s['herons'] * p['heron_c'] * dt
    heron_on = s['herons'] > 0 and not iced and s['heron_here']
    V = sum(vis[k] * Mb[k] for k in range(BINS)) * (me / m if m > 0 else 0)
    if heron_on and V > 0:
        o('M', hneed * V / (p['heron_H'] + V), ('eat', 'heron'))
    O = s['O']
    ox = dict(M=1.2 * max(0.0, (3.0 - O) / 3.0), Dn=0.6 * max(0.0, (1.5 - O) / 1.5), S=0.15 * max(0.0, 1.0 - O))
    for name, B, key in (('snail', S, 'S'), ('minnow', m, 'M'), ('dragon', Dn, 'Dn'), ('decomp', max(0.0, D - R['D']) if s['decomp_on'] else D, 'D')):
        c = sp[name]
        o(key, c['maint'] * f * B * dt, ('to', 'N'))
        acc['maint_' + name] += c['maint'] * f * B * dt
        o(key, c['mort'] * B * dt, ('to', 'Det'))
        if key in ox: o(key, ox[key] * B * dt, ('to', 'Det')); acc['ox_' + key] += ox[key] * B * dt
    o('F', 0.4 * F * dt, ('to', 'Det'))
    pools = dict(N=N - Gf - Gs, Af=Af, As=As, S=S, M=m, Dn=Dn, D=D, Det=Det, F=F)
    for src, lst in out.items():
        tot = sum(a for _, a in lst)
        if tot > pools[src]:
            sc = pools[src] / tot
            for it in lst: it[1] *= sc
    d = {k: 0.0 for k in pools}
    d['Af'] += Gf; d['As'] += Gs
    acc.setdefault('flow', {})
    acc['flow'][('N', 'Af')] = acc['flow'].get(('N', 'Af'), 0.0) + Gf
    acc['flow'][('N', 'As')] = acc['flow'].get(('N', 'As'), 0.0) + Gs
    acc['G'] += Gf + Gs; acc['Gf'] += Gf; acc['Gs'] += Gs
    intake = {k: 0.0 for k in ('snail', 'minnow', 'dragon', 'decomp', 'turtle', 'heron')}
    resp = 0.0; M_unsel = 0.0; M_heron = 0.0
    fl = acc.setdefault('flow', {})
    for src, lst in out.items():
        for tag, amt in lst:
            key = (src, tag[1]) if tag[0] == 'to' else (src, 'eat_' + tag[1])
            fl[key] = fl.get(key, 0.0) + amt
            d[src] -= amt
            if tag[0] == 'to':
                d[tag[1]] += amt
                if tag[1] == 'N': resp += amt
                if src in ('Af', 'As') and tag[1] == 'N': acc['aresp'] += amt
            else:
                intake[tag[1]] += amt
                if src == 'M':
                    if tag[1] == 'heron': M_heron += amt
                    else: M_unsel += amt
    # M losses other than eating come through 'to' tags; collect them separately
    M_other = sum(a for tag, a in out.get('M', []) if tag[0] == 'to')
    body = dict(snail='S', minnow='M', dragon='Dn', decomp='D')
    gM = 0.0
    for name, I in intake.items():
        if name in body:
            c = sp[name]; g = c['eff'] * I
            if name == 'decomp': r = I - g; wst = 0.0
            else: r = (p['assim'] - c['eff']) * I; wst = I - g - r
            d['N'] += r; d['Det'] += wst; resp += r
            if name == 'minnow': gM = g
            else: d[body[name]] += g
            acc['prod_' + name] += g
        else:
            r = p['assim'] * I; d['N'] += r; d['Det'] += I - r; resp += r
        acc['eat_' + name] += I
    # minnows by shade
    newM = Mb[:]
    if m > 0:
        Vk = [vis[k] * Mb[k] for k in range(BINS)]; Vs = sum(Vk)
        kid = [0.0] * BINS
        for k in range(BINS):
            for dk, wt in ((-1, 0.06), (0, 0.88), (1, 0.06)):
                kid[min(BINS - 1, max(0, k + dk))] += Mb[k] / m * wt
        for k in range(BINS):
            newM[k] = max(0.0, Mb[k] - (M_unsel + M_other) * Mb[k] / m - (M_heron * Vk[k] / Vs if Vs > 0 else 0) + gM * kid[k])
    for k in ('N', 'Af', 'As', 'S', 'Dn', 'D', 'Det', 'F'):
        s[k] = max(0.0, pools[k] + d[k] + (Gf + Gs if k == 'N' else 0) - (Gf + Gs if k == 'N' else 0))
    s['N'] = max(0.0, pools['N'] + d['N'])
    s['M'] = newM
    s['O'] = max(0.0, min(20.0, O + p['po'] * (Gf + Gs) - p['co'] * resp + (0 if iced else p['kr'] * dt * (osat(T) - O))))
    acc['resp'] += resp; acc['hneed'] += hneed if heron_on else 0; acc['tneed'] += tneed if T >= 10 else 0
    acc['sun'] += p['sun0'] * sunsurf(w) * dt
    acc['heron_on'] = heron_on; acc['clarity'] = clarity

def new_acc():
    a = dict(G=0.0, Gf=0.0, Gs=0.0, resp=0.0, hneed=0.0, tneed=0.0, sun=0.0, aresp=0.0, heron_on=False, clarity=1.0)
    for k in ('snail', 'minnow', 'dragon', 'decomp', 'turtle', 'heron'):
        a['prod_' + k] = 0.0; a['eat_' + k] = 0.0; a['maint_' + k] = 0.0
    for k in ('M', 'Dn', 'S'): a['ox_' + k] = 0.0
    return a

def step(s):
    w = s['week'] % WEEKS
    acc = new_acc()
    start = dict(N=s['N'], Af=s['Af'], As=s['As'], S=s['S'], M=Mt(s), Dn=s['Dn'], D=s['D'], Det=s['Det'], F=s['F'])
    if w == 0 and s['herons'] > 0 and not s['heron_here']:
        s['heron_here'] = True; s['heron_bad'] = 0
    for i in range(SUB):
        substep(s, 1.0 / SUB, w, acc)
    T = temp(w)
    s['energy']['sun'] += acc['sun']; s['energy']['caught'] += 10 * acc['G']; s['energy']['heat'] += 10 * acc['resp']
    for key, lim in (('S', 0.5 * W['snail']), ('Dn', 0.5 * W['dragon']), ('D', 0.5), ('Af', 0.5), ('As', 0.5)):
        if 0 < s[key] < lim:
            s['Det'] += s[key]; s[key] = 0.0
    if 0 < Mt(s) < 0.5 * W['minnow']:
        s['Det'] += Mt(s); s['M'] = [0.0] * BINS
    if acc['heron_on']:
        s['heron_bad'] = s['heron_bad'] + 1 if acc['eat_heron'] < 0.3 * acc['hneed'] else 0
        if s['heron_bad'] >= 3:
            s['heron_here'] = False; s['log'].append((s['week'], 'heron flew off'))
    if s['turtles'] > 0 and T >= 10:
        s['turtle_bad'] = s['turtle_bad'] + 1 if acc['eat_turtle'] < 0.25 * acc['tneed'] else 0
        if s['turtle_bad'] >= 8:
            s['turtles'] -= 1; s['ledger']['left'] += W['turtle']; s['turtle_bad'] = 0
            s['log'].append((s['week'], 'turtle walked off'))
    row = dict(start=start, week=s['week'], T=T, ice=ice(w), L=light(w), N=s['N'], Af=s['Af'], As=s['As'], A=s['Af'] + s['As'],
               S=s['S'], M=Mt(s), Dn=s['Dn'], D=s['D'], Det=s['Det'], F=s['F'], O=s['O'],
               heron=int(acc['heron_on']) * s['herons'], turtles=s['turtles'], color=mean_color(s), acc=acc,
               Mbins=s['M'][:])
    s['hist'].append(row)
    s['week'] += 1
    return row

def run(s, weeks, events=None):
    events = events or {}
    for i in range(weeks):
        ev = events.get(s['week'])
        if ev:
            for e in (ev if isinstance(ev, list) else [ev]): e(s)
        step(s)
    return s

def add(s, what, amount=None):
    if what == 'M':
        for k in range(2, 6): s['M'][k] += amount / 4
    elif what == 'turtle':
        s['turtles'] += 1; amount = W['turtle']
    elif what == 'algae':
        s['Af'] += amount / 2; s['As'] += amount / 2
    else:
        s[what] += amount
    s['ledger']['added'] += amount

def remove_all(s, what):
    if what == 'M':
        amt = Mt(s); s['M'] = [0.0] * BINS
    elif what == 'turtle':
        amt = s['turtles'] * W['turtle']; s['turtles'] = 0
    elif what == 'heron':
        s['herons'] = 0; amt = 0.0
    else:
        amt = s[what]; s[what] = 0.0
    s['ledger']['removed'] += amt

def show(s, every=13, start=0, end=None):
    for r in s['hist'][start:end:every]:
        print(f"y{r['week']//52+1}w{r['week']%52:2d} T{r['T']:4.1f}{'I' if r['ice'] else ' '} N{r['N']:5.0f} Af{r['Af']:5.0f} As{r['As']:5.0f} "
              f"S{r['S']:5.1f} M{r['M']:5.1f} Dn{r['Dn']:5.1f} D{r['D']:5.1f} Det{r['Det']:5.0f} O{r['O']:5.1f} "
              f"H{r['heron']} Tu{r['turtles']} c{r['color']:4.2f}")
