import numpy as np, itertools, math
from scipy.spatial import cKDTree as KD
# SALT: 8x8x8 ions, unit spacing (282 pm), charges by parity. Slip plane between z=3 and z=4. Shift top by s along x.
n=8; P=np.array(list(itertools.product(range(n),repeat=3)),float); Q=np.where(P.sum(1)%2==0,1,-1)
top=P[:,2]>=4; bot=~top
def coul(s):
    T=P[top]+[s,0,0]; B=P[bot]; E=0
    for p,q in zip(T,Q[top]):
        r=np.linalg.norm(B-p,axis=1); E+=np.sum(q*Q[bot]/r)
    return E
for s in (0,0.5,1.0):
    print(f"salt: top half shifted {s*282:.0f} pm -> energy between halves {coul(s):+.1f} (units e^2/282pm; negative = halves pull together, positive = push apart)")
# COPPER fcc: atoms on fcc sites, nn d=1 (255.6 pm). Slip on (111) plane along [1,-1,0]: count contacts across plane & min distance
a=math.sqrt(2)
base=[np.array(v) for v in [(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)]]
pts=np.array([a*(np.array(c)+b) for c in itertools.product(range(-4,4),repeat=3) for b in base])
nrm=np.array([1,1,1])/math.sqrt(3); h=pts@nrm; lay=np.round(h/(a/math.sqrt(3)))  # (111) spacing a/sqrt3
top=lay>=1; bot=lay<=0
u=np.array([1,-1,0])/math.sqrt(2)
for s in (0,0.5,1.0):
    T=pts[top]+s*u; tr=KD(pts[bot]); dd,_=tr.query(T); 
    c=sum(len(x) for x in tr.query_ball_point(T,1.05))
    print(f"copper: (111) layers shifted {s*255.6:.0f} pm along a row -> contacts across the plane {c}, closest approach {dd.min()*255.6:.0f} pm")
# DIAMOND: bonds crossing a (111) plane & (001) plane per 100 atoms
L=1.0; a_c=4/math.sqrt(3)
db=[np.array(v) for v in [(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)]]
D=np.array([a_c*(np.array(c)+b+o) for c in itertools.product(range(-3,3),repeat=3) for b in db for o in (np.zeros(3),np.array([.25,.25,.25]))])
tr=KD(D); bonds=list(tr.query_pairs(1.05))
z=D[:,2]; cut=sum(1 for i,j in bonds if (z[i]<0.1)!=(z[j]<0.1))
print(f"diamond: {len(D)} atoms, {len(bonds)} bonds; bonds crossing one flat cut through the middle: {cut} (each must stretch and break to slide)")
print("graphite: bonds crossing a layer gap: 0 (from crystal.py)")
