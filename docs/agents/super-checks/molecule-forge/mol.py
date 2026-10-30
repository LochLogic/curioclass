import json, re, itertools, collections
import networkx as nx
from networkx.algorithms import isomorphism as iso
VAL={'H':1,'C':4,'N':3,'O':2,'S':2,'Cl':1,'Si':4}
VE={'H':1,'C':4,'N':5,'O':6,'S':6,'Cl':7,'Si':4}
def parse(smi):
    G=nx.Graph(); i=0; prev=None; stack=[]; rings={}; bo=1; n=0
    def add(el,h=None):
        nonlocal n; G.add_node(n,el=el,hx=h); n+=1; return n-1
    while i<len(smi):
        c=smi[i]
        if c=='(':stack.append(prev); i+=1; continue
        if c==')':prev=stack.pop(); i+=1; continue
        if c in '=#': bo={'=':2,'#':3}[c]; i+=1; continue
        if c.isdigit():
            if c in rings:
                a,b0=rings.pop(c); G.add_edge(a,prev,o=max(bo,b0)); bo=1
            else: rings[c]=(prev,bo); bo=1
            i+=1; continue
        if c=='[':
            j=smi.index(']',i); t=smi[i+1:j]; m=re.match(r'([A-Z][a-z]?)(H(\d*))?',t)
            el=m.group(1); h=0
            if m.group(2): h=int(m.group(3) or 1)
            a=add(el,h); i=j+1
        else:
            el=smi[i:i+2] if smi[i:i+2]=='Cl' else c; i+=len(el); a=add(el)
        if prev is not None: G.add_edge(prev,a,o=bo)
        bo=1; prev=a
    # hydrogens
    for a in list(G.nodes):
        el=G.nodes[a]['el']; hx=G.nodes[a]['hx']
        used=sum(G[a][b]['o'] for b in G[a])
        h = hx if hx is not None else VAL[el]-used
        if el=='H': h = hx or 0
        for _ in range(h):
            k=add('H'); G.add_edge(a,k,o=1)
    return G
def valence_ok(G):
    bad=[(a,G.nodes[a]['el'],sum(G[a][b]['o'] for b in G[a])) for a in G if sum(G[a][b]['o'] for b in G[a])!=VAL[G.nodes[a]['el']]]
    return bad
def hill(G):
    c=collections.Counter(G.nodes[a]['el'] for a in G)
    keys=([k for k in ['C','H'] if c[k]] if 'C' in c else [])+sorted(k for k in c if c[k] and not('C' in c and k in ('C','H')))
    return ''.join(k+(str(c[k]) if c[k]>1 else '') for k in keys)
def pubhill(f):
    # pubchem formula -> counter
    return collections.Counter({m[0]:int(m[1] or 1) for m in re.findall(r'([A-Z][a-z]?)(\d*)',f)})
def cnt(G): return collections.Counter(G.nodes[a]['el'] for a in G)
def resonance(G):
    # count bond-order assignments on skeleton satisfying valence (orders 1..3)
    E=list(G.edges); need={a:VAL[G.nodes[a]['el']]-G.degree(a) for a in G}
    sol=0
    def rec(k,need):
        nonlocal sol
        if k==len(E):
            if all(v==0 for v in need.values()): sol+=1
            return
        a,b=E[k]
        for extra in range(0,3):
            if need[a]>=extra and need[b]>=extra:
                need[a]-=extra; need[b]-=extra; rec(k+1,need); need[a]+=extra; need[b]+=extra
    rec(0,dict(need)); return sol
def skel_iso(G,H):
    return nx.is_isomorphic(G,H,node_match=iso.categorical_node_match('el',None))
def domains(G,a):
    el=G.nodes[a]['el']; used=sum(G[a][b]['o'] for b in G[a])
    lp=(VE[el]-used)//2 if el not in ('H',) else 0
    return G.degree(a), lp
SHAPE={(2,0):'linear 180',(3,0):'trigonal planar 120',(4,0):'tetrahedral 109.5',(3,1):'pyramid 107',(2,2):'bent 104.5',(2,1):'bent ~120',(1,3):'end',(1,2):'end',(1,1):'end',(1,0):'end'}
