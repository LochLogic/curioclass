import itertools, json, networkx as nx
from networkx.algorithms import isomorphism as iso
from mol import *
P=json.load(open('pubchem.json'))
known={n:parse(P['data'][n]['SMILES']) for n in P['book']+P['also']}
def heavy_key(G):
    return nx.weisfeiler_lehman_graph_hash(G,node_attr='el',edge_attr='os')
found=[]
els=['C','N','O']
for k in (1,2,3):
    for combo in itertools.combinations_with_replacement(els,k):
        pairs=list(itertools.combinations(range(k),2))
        for orders in itertools.product(range(0,4),repeat=len(pairs)):
            G=nx.Graph()
            for i,e in enumerate(combo): G.add_node(i,el=e)
            for (a,b),o in zip(pairs,orders):
                if o: G.add_edge(a,b,o=o)
            if not nx.is_connected(G): continue
            if any(sum(G[a][b]['o'] for b in G[a])>VAL[G.nodes[a]['el']] for a in G): continue
            n=k
            for a in list(G.nodes):
                for _ in range(VAL[G.nodes[a]['el']]-sum(G[a][b]['o'] for b in G[a])):
                    G.add_node(n,el='H'); G.add_edge(a,n,o=1); n+=1
            for a,b in G.edges: G[a][b]['os']=str(G[a][b]['o'])
            if any(nx.is_isomorphic(G,F,node_match=iso.categorical_node_match('el',None),edge_match=iso.categorical_edge_match('o',1)) for F in found): continue
            found.append(G)
print("legal C/N/O structures with 1-3 heavy atoms:",len(found))
inbook=0; names=[]
odd=[]
for G in found:
    m=[n for n,K in known.items() if skel_iso(G,K)]
    if m: names.append(m[0])
    else: odd.append(hill(G)+':'+','.join(sorted(f"{G.nodes[a]['el']}{G.nodes[b]['el']}{G[a][b]['o']}" for a,b in G.edges if 'H' not in (G.nodes[a]['el'],G.nodes[b]['el']))))
print("named by book/also:",len(names),sorted(names))
print("unnamed (strange but legal):",len(odd)); print(odd)
