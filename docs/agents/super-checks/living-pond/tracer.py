from pond import *
import random
EFF = {'snail': ('S', .3, .4), 'minnow': ('M', .3, .4), 'dragon': ('Dn', .3, .4), 'decomp': ('D', .2, .8), 'turtle': (None, 0, .7), 'heron': (None, 0, .7)}
def move(pool, row, rnd):
    fl = row['acc']['flow']; B = row['start'][pool]
    if B <= 0: return pool, None
    u = rnd.random() * B; c = 0.0
    for (src, dst), amt in fl.items():
        if src != pool: continue
        c += amt
        if u < c:
            if dst.startswith('eat_'):
                body, g, r = EFF[dst[4:]]; v = rnd.random()
                if body and v < g: return body, dst[4:]
                if v < g + r: return 'N', dst[4:]
                return 'Det', dst[4:]
            return dst, None
    return pool, None
s = new_pond(); run(s, 520)
rnd = random.Random(1)
res = []
for trial in range(2000):
    start = rnd.randrange(0, 52*5)
    pool = 'Det'; stage = 0; w = start
    while w < 520:
        pool, via = move(pool, s['hist'][w], rnd)
        if stage == 0 and pool == 'N': stage = 1
        elif stage == 1 and pool in ('Af', 'As'): stage = 2
        elif stage == 2 and pool in ('S', 'M', 'Dn'): stage = 3; break
        w += 1
    res.append(w - start if stage == 3 else None)
ok = sorted(x for x in res if x is not None)
print('journeys done %d of %d; median weeks %d, 75th %d, 90th %d' % (len(ok), len(res), ok[len(ok)//2], ok[int(len(ok)*.75)], ok[int(len(ok)*.9)]))
# where does a dot spend its time: share of weeks per pool over 10 years
cnt = {}
pool = 'Det'
for trial in range(200):
    pool = rnd.choice(['Det', 'N', 'Af'])
    for w in range(520):
        pool, _ = move(pool, s['hist'][w], rnd); cnt[pool] = cnt.get(pool, 0) + 1
tot = sum(cnt.values()); print({k: round(100*v/tot) for k, v in cnt.items()})
print('mean matter share', {k: round(100*sum(r['start'][k] for r in s['hist'])/sum(total(new_pond()) for r in s['hist'])) for k in ('N','Af','As','S','M','Dn','D','Det')})
