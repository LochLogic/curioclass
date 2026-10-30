import numpy as np, itertools, math, collections
from scipy.spatial import cKDTree as KD
BUDGET=600
def grow(seed_atoms, rule, maxatoms=BUDGET, tol=0.25):
    """seed_atoms: list of (pos, kind). rule(pos,kind)-> list of (newpos,newkind). BFS by shell; stop at last full shell <= budget"""
    atoms=[(np.array(p,float),k) for p,k in seed_atoms]; shells=[len(atoms)]; frontier=list(range(len(atoms)))
    while True:
        new=[]; pts=[a[0] for a in atoms]
        tree=KD(np.array(pts))
        newpts=[]
        for i in frontier:
            for q,k in rule(*atoms[i]):
                if tree.query(q)[0]<tol: continue
                if newpts and min(np.linalg.norm(np.array(newpts)-q,axis=1))<tol: continue
                newpts.append(q); new.append((q,k))
        if len(atoms)+len(new)>maxatoms or not new: break
        frontier=list(range(len(atoms),len(atoms)+len(new))); atoms+=new; shells.append(len(atoms))
    return atoms,shells
def neigh_stats(atoms,d,interior_frac=0.5):
    P=np.array([a[0] for a in atoms]); c=P.mean(0); r=np.linalg.norm(P-c,axis=1); R=r.max()
    tree=KD(P); cn=[]; minnb=1e9
    for i in range(len(P)):
        if r[i]>interior_frac*R: continue
        idx=[j for j in tree.query_ball_point(P[i],d*1.1) if j!=i]; cn.append(len(idx))
        dd,_=tree.query(P[i],k=2); minnb=min(minnb,dd[1])
    return collections.Counter(cn), minnb
# ---- diamond / silicon: tetrahedral directions alternate by sublattice
T=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/math.sqrt(3)
def diamond_rule(L):
    def r(p,k):  # k = sublattice sign
        return [(p+k*L*t,-k) for t in T]
    return r
for name,L,el in [('diamond',154.4,'C'),('silicon',235.2,'Si')]:
    A,sh=grow([((0,0,0),1)],diamond_rule(L))
    cn,mn=neigh_stats(A,L)
    P=np.array([a[0] for a in A]); tree=KD(P)
    # bond angles at an interior atom
    i=0; nb=[j for j in tree.query_ball_point(P[0],L*1.1) if j]; 
    angs=sorted({round(math.degrees(math.acos(np.dot(P[a]-P[0],P[b]-P[0])/L/L)),2) for a,b in itertools.combinations(nb,2)})
    a_cubic=4*L/math.sqrt(3)
    print(f"{name}: atoms {len(A)} shells {len(sh)} counts {sh}; interior coordination {dict(cn)}; nearest {mn:.1f} pm; angles {angs}; cubic cell a = {a_cubic:.1f} pm")
# smallest ring in diamond
import networkx as nx
A,_=grow([((0,0,0),1)],diamond_rule(1.0),maxatoms=200)
P=np.array([a[0] for a in A]); G=nx.Graph(); tree=KD(P)
for i,j in tree.query_pairs(1.05): G.add_edge(i,j)
cyc=nx.minimum_cycle_basis(G); print("diamond ring sizes:",collections.Counter(len(c) for c in cyc))
# ---- graphene sheet: planar 3 directions alternating
L=142.0
D3=np.array([[math.cos(math.radians(a)),math.sin(math.radians(a)),0] for a in (90,210,330)])
def gr_rule(p,k): return [(p+k*L*d,-k) for d in D3]
A,sh=grow([((0,0,0),1),((0,L,0),-1)],gr_rule)
cn,mn=neigh_stats(A,L)
P=np.array([a[0] for a in A]); G=nx.Graph(); tree=KD(P)
for i,j in tree.query_pairs(L*1.05): G.add_edge(i,j)
M=nx.max_weight_matching(G,maxcardinality=True)
deg=collections.Counter(dict(G.degree()).values())
cyc=nx.minimum_cycle_basis(G)
print(f"graphene sheet (one layer, budget {BUDGET}): atoms {len(A)} shells {len(sh)}; interior coordination {dict(cn)}; degree counts {dict(deg)}; nearest {mn:.1f}; rings {collections.Counter(len(c) for c in cyc)}; max matching covers {2*len(M)} of {len(A)} (double bonds placeable)")
# graphite: sheets of 150 atoms x 4 layers AB at 335 pm
def sheet(n):
    A,_=grow([((0,0,0),1),((0,L,0),-1)],gr_rule,maxatoms=n); return np.array([a[0] for a in A])
S=sheet(150); layers=[]
for z in range(4):
    off=np.array([0, L if z%2 else 0, 335.0*z]); layers.append(S+off)
GP=np.vstack(layers); tr=KD(GP)
inter=[ (i,j) for i,j in tr.query_pairs(200) if abs(GP[i,2]-GP[j,2])>1]
print(f"graphite: {len(S)} atoms per sheet x 4 = {len(GP)}; covalent bonds (<200 pm) between layers: {len(inter)}; layer gap 335 pm")
# ---- rock salt: octahedral opposite ions
a=282.0
O6=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
def salt_rule(p,k): return [(p+a*o,-k) for o in O6]
A,sh=grow([((0,0,0),1),((a,0,0),-1)],salt_rule)
P=np.array([x[0] for x in A]); K=np.array([x[1] for x in A]); tree=KD(P)
bad=0; cn=collections.Counter()
c=P.mean(0); R=np.linalg.norm(P-c,axis=1).max()
for i in range(len(P)):
    nb=[j for j in tree.query_ball_point(P[i],a*1.05) if j!=i]
    if np.linalg.norm(P[i]-c)<0.5*R: cn[len(nb)]+=1
    bad+=sum(K[j]==K[i] for j in nb)
print(f"salt: ions {len(A)} (Na {sum(K==1)}, Cl {sum(K==-1)}) shells {len(sh)}; interior coordination {dict(cn)}; like-charge touching pairs {bad}; Na-Cl {a} pm, cube cell {2*a} pm")
# ---- copper fcc: 12 neighbors
d=255.6
F=[np.array(v)/math.sqrt(2) for v in itertools.product((-1,0,1),repeat=3) if sum(x!=0 for x in v)==2]
def cu_rule(p,k): return [(p+d*f,k) for f in F]
A,sh=grow([((0,0,0),0)],cu_rule)
cn,mn=neigh_stats(A,d)
print(f"copper: atoms {len(A)} shells {len(sh)} counts {sh}; interior coordination {dict(cn)}; nearest {mn:.1f} pm; cubic cell {d*math.sqrt(2):.1f} pm")
# ---- silica: Si on diamond sites (Si..Si = 2*161*sin(145/2)), O bridging, bent 145
dSiO=161.0; ang=145.0; SS=2*dSiO*math.sin(math.radians(ang/2)); off=dSiO*math.cos(math.radians(ang/2))
Asi,_=grow([((0,0,0),1)],diamond_rule(SS),maxatoms=200)
P=np.array([x[0] for x in Asi]); tree=KD(P); Opos=[]
for i,j in tree.query_pairs(SS*1.05):
    m=(P[i]+P[j])/2; u=P[j]-P[i]; u/=np.linalg.norm(u); w=np.cross(u,[0.3,0.5,0.81]); w/=np.linalg.norm(w)
    Opos.append(m+off*w)
Opos=np.array(Opos)
# check Si-O distances and angle
k=KD(Opos); cnt=collections.Counter(); c=P.mean(0); R=np.linalg.norm(P-c,axis=1).max()
for i in range(len(P)):
    if np.linalg.norm(P[i]-c)<0.5*R: cnt[len(k.query_ball_point(P[i],dSiO*1.05))]+=1
o=Opos[0]; si=[j for j in tree.query_ball_point(o,dSiO*1.05)]
v1,v2=P[si[0]]-o,P[si[1]]-o
print(f"silica: Si {len(P)} + O {len(Opos)} = {len(P)+len(Opos)} atoms (O:Si {len(Opos)/len(P):.2f}, interior is 2.00); interior Si has O neighbors {dict(cnt)}; Si-O {np.linalg.norm(v1):.1f} pm; Si-O-Si {math.degrees(math.acos(np.dot(v1,v2)/np.linalg.norm(v1)/np.linalg.norm(v2))):.1f} deg; Si..Si {SS:.1f} pm")
# min O-O distance (no overlap)
print("  silica closest O-O pm:", round(KD(Opos).query(Opos,k=2)[0][:,1].min(),1))
