from ciphers import *
import json
D=json.load(open('rooms.json')); R={int(k):v for k,v in D['R'].items()}; C={int(k):v for k,v in D['C'].items()}
# Room 1: score all 26 shifts
sc=sorted(((score(caesar(C[1],-k)),k) for k in range(26)),reverse=True)
print('R1 best shifts',[k for s,k in sc[:3]])
# Room 3: hill climb full
ct=C[3]; dec=hill_sub(ct,iters=3000,restarts=6)
acc=sum(a==b for a,b in zip(letters(dec),letters(R[3])))/len(letters(R[3]))
print('R3 full solver letter accuracy',round(acc,3))
# rank-only
L=letters(ct); order=[c for c,_ in collections.Counter(L).most_common()]
eng=sorted(A,key=lambda a:-ENG[a])
m={order[i]:eng[i] for i in range(len(order))}
ra=sum(m[c]==p for c,p in zip(L,letters(R[3])))/len(L)
print('R3 rank-only accuracy',round(ra,3))
top=collections.Counter(letters(R[3])).most_common(8); print('R3 plaintext top letters',top)
# which plaintext letters are correct under rank-only
ok=sorted({p for c,p in zip(L,letters(R[3])) if m[c]==p}); print('rank-only right letters',ok)
