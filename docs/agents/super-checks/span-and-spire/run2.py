from designs import *
T5=['Pickup','School bus','Fire engine','Grain truck','Semi']
for h in [2,2.5,3,3.5,4,4.5,5]:
    tr,deck=build(h=h); tr.abut={0,6}
    res=[]
    for t in T5:
        w,_,_=tr.crossing(deck,t); res.append(f'{t[:5]} {w.max()*100:5.1f}')
    print('pratt h',h, ' | '.join(res))
print('--- cables as diagonals')
for k in ['pratt','howe']:
    tr,deck=build(h=4,kind=k,diag='C'); report(tr,deck,f'{k} cable diagonals h4')
print('--- one panel with no diagonal (remove first interior diagonal)')
tr,deck=build(h=4); 
idx=[i for i,m in enumerate(tr.M) if tr.J[m[0]][1]!=tr.J[m[1]][1] and tr.J[m[0]][0]!=tr.J[m[1]][0] and m not in (tr.M[10],tr.M[11])]
print('diagonals',[ (tr.J[tr.M[i][0]],tr.J[tr.M[i][1]]) for i in idx])
del tr.M[idx[0]]; report(tr,deck,'pratt h4 minus one diagonal',['Pickup'])
