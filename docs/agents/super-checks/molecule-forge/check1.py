import json,collections, networkx as nx
from mol import *
P=json.load(open('pubchem.json'))
mols={}
print("== valence + formula check ==")
for n in P['book']+P['also']:
    d=P['data'][n]; G=parse(d['SMILES']); bad=valence_ok(G)
    fok = cnt(G)==pubhill(d['MolecularFormula'])
    res=resonance(G)
    mols[n]=G
    tag='BOOK' if n in P['book'] else 'also'
    print(f"{tag} {n:20s} {d['SMILES']:32s} pubchem {d['MolecularFormula']:10s} graph {hill(G):10s} atoms {G.number_of_nodes():2d} formula_ok {fok} valence_bad {bad} kekule_forms {res}")
print("== pairwise skeleton isomorphism (should be none) ==")
names=list(mols)
for i in range(len(names)):
    for j in range(i+1,len(names)):
        if skel_iso(mols[names[i]],mols[names[j]]): print("ISO!",names[i],names[j])
print("== isomer groups (same formula, different skeleton) ==")
g=collections.defaultdict(list)
for n,G in mols.items(): g[hill(G)].append(n)
for k,v in g.items():
    if len(v)>1: print(k,v)
print("== central atom shapes (book) ==")
for n in P['book']:
    G=mols[n]; s=[]
    for a in G:
        if G.nodes[a]['el']!='H' and G.degree(a)>1: s.append(G.nodes[a]['el']+':'+SHAPE[domains(G,a)])
    print(n, collections.Counter(s))
json.dump({n:{'atoms':[mols[n].nodes[a]['el'] for a in mols[n]],'bonds':[[a,b,mols[n][a][b]['o']] for a,b in mols[n].edges]} for n in mols},open('graphs.json','w'))
