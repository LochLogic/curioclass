"""Pocket Universe model checks. Units: world px, seconds, pocket mass units. G = 1e4."""
import numpy as np, math, random
G = 1e4
DT = 1/480
EPS = 1.0  # softening px

KIND = {  # mass, radius
    'star': (1000, 22), 'dwarf': (300, 14), 'hole': (1000, 5), 'giant': (100, 12),
    'planet': (10, 7), 'moon': (0.3, 4), 'comet': (0.001, 3)}

class Sim:
    def __init__(s, bodies, dust=None, gscale=1.0):
        # bodies: list of dict kind, x,y,vx,vy, m(optional)
        s.k = [b['kind'] for b in bodies]
        s.m = np.array([b.get('m', KIND[b['kind']][0]) for b in bodies], float)
        s.r = np.array([b.get('r', KIND[b['kind']][1]) for b in bodies], float)
        s.x = np.array([[b['x'], b['y']] for b in bodies], float)
        s.v = np.array([[b['vx'], b['vy']] for b in bodies], float)
        s.alive = np.ones(len(bodies), bool)
        s.dx = np.zeros((0, 2)) if dust is None else np.array(dust[0], float)
        s.dv = np.zeros((0, 2)) if dust is None else np.array(dust[1], float)
        s.dalive = np.ones(len(s.dx), bool)
        s.g = gscale
        s.t = 0.0
        s.merges = []
        s.substeps_used = 0
    def acc(s, x):
        a = np.zeros_like(x)
        idx = np.where(s.alive)[0]
        for j in idx:
            d = s.x[j] - x
            r2 = (d**2).sum(1) + EPS**2
            a += (G*s.g*s.m[j]*d.T/r2**1.5).T
        return a
    def acc_self(s):
        a = np.zeros_like(s.x)
        idx = np.where(s.alive)[0]
        for i in idx:
            for j in idx:
                if i == j: continue
                d = s.x[j]-s.x[i]; r2 = d@d + EPS**2
                a[i] += G*s.g*s.m[j]*d/r2**1.5
        return a
    def nsub(s):
        idx = np.where(s.alive)[0]; worst = 1e9
        for ii, i in enumerate(idx):
            for j in idx[ii+1:]:
                d = s.x[j]-s.x[i]; dv = s.v[j]-s.v[i]
                r = math.hypot(*d); vv = math.hypot(*dv)+1e-9
                worst = min(worst, r/vv)
        k = 0
        while k < 6 and worst < 20*DT/(2**k): k += 1
        return 2**k
    def step(s, adaptive=True):
        n = s.nsub() if adaptive else 1
        h = DT/n
        s.substeps_used = max(s.substeps_used, n)
        for _ in range(n):
            a = s.acc_self(); s.v += 0.5*h*a; s.x += h*s.v; a = s.acc_self(); s.v += 0.5*h*a
            if len(s.dx):
                ad = s.acc(s.dx); s.dv += 0.5*h*ad; s.dx += h*s.dv; ad = s.acc(s.dx); s.dv += 0.5*h*ad
            s.collide()
        s.t += DT
    def collide(s):
        idx = np.where(s.alive)[0]
        for ii, i in enumerate(idx):
            for j in idx[ii+1:]:
                if not (s.alive[i] and s.alive[j]): continue
                d = s.x[j]-s.x[i]
                if math.hypot(*d) < s.r[i]+s.r[j]:
                    big, small = (i, j) if s.m[i] >= s.m[j] else (j, i)
                    M = s.m[i]+s.m[j]
                    s.x[big] = (s.m[i]*s.x[i]+s.m[j]*s.x[j])/M
                    s.v[big] = (s.m[i]*s.v[i]+s.m[j]*s.v[j])/M
                    if s.k[big] != 'hole':
                        s.r[big] = s.r[big]*(M/s.m[big])**(1/3)
                    s.m[big] = M; s.alive[small] = False
                    s.merges.append((round(s.t, 3), s.k[small], s.k[big]))
        if len(s.dx):
            for j in idx:
                if not s.alive[j]: continue
                hit = s.dalive & (((s.dx-s.x[j])**2).sum(1) < s.r[j]**2)
                s.dalive &= ~hit
    def energy(s):
        idx = np.where(s.alive)[0]; E = 0
        for i in idx:
            E += 0.5*s.m[i]*(s.v[i]@s.v[i])
        for ii, i in enumerate(idx):
            for j in idx[ii+1:]:
                d = s.x[j]-s.x[i]; E -= G*s.g*s.m[i]*s.m[j]/math.sqrt(d@d+EPS**2)
        return E
    def run(s, T, cb=None, every=1):
        n = int(round(T/DT))
        for k in range(n):
            s.step()
            if cb and k % every == 0: cb(s)

def circ(M, r): return math.sqrt(G*M/r)

def twobody_E(sim, i, j):
    d = sim.x[i]-sim.x[j]; dv = sim.v[i]-sim.v[j]
    mu = G*sim.g*(sim.m[i]+sim.m[j])
    return 0.5*(dv@dv) - mu/math.hypot(*d)

class Laps:
    def __init__(s, i, j): s.i, s.j, s.acc, s.prev = i, j, 0.0, None
    def __call__(s, sim):
        d = sim.x[s.i]-sim.x[s.j]; a = math.atan2(d[1], d[0])
        if s.prev is not None:
            da = a-s.prev
            while da > math.pi: da -= 2*math.pi
            while da < -math.pi: da += 2*math.pi
            s.acc += da
        s.prev = a
    @property
    def laps(s): return s.acc/(2*math.pi)

def out(*a): print(*a, flush=True)
