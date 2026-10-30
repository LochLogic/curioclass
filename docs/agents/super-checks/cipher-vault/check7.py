from ciphers import *
import json,time
D=json.load(open('rooms.json')); R={int(k):v for k,v in D['R'].items()}; C={int(k):v for k,v in D['C'].items()}
L=letters(C[5]); P=letters(R[5]); crib='WEATHERREPORT'
pos=[i for i in range(len(L)-len(crib)+1) if all(L[i+j]!=crib[j] for j in range(len(crib)))]
print('ct letters',len(L),'crib positions',len(L)-len(crib)+1,'allowed',len(pos),pos,'true',P.index(crib))
# bombe at each allowed position: enigma from start S, advance i letters, check crib
def survivors(pos_list,crib,orders=[('I','II','III')]):
    out=[]
    for o in orders:
        for s in itertools.product(A,repeat=3):
            st=''.join(s)
            for i in pos_list:
                seg=L[:i+len(crib)]
                d=enigma(seg,order=o,start=st)
                if d[i:]==crib: out.append((o,st,i))
    return out
t=time.time(); s=survivors([P.index(crib)],crib); print('true position, 17576 settings, survivors',s,round(time.time()-t,1),'s')
t=time.time(); s=survivors(pos,crib); print('all allowed positions survivors',s,round(time.time()-t,1))
for cl in [3,4,5,6,8]:
    s=survivors([P.index(crib)],crib[:cl]); print('crib length',cl,'survivors',len(s))
# reciprocity and no self-encryption over random settings
rng=random.Random(3); selfhit=0; rec=True
for k in range(300):
    o=tuple(rng.sample(['I','II','III','IV','V'],3)); st=''.join(rng.choice(A) for _ in range(3))
    p=''.join(rng.choice(A) for _ in range(60)); c=enigma(p,o,st)
    selfhit+=sum(a==b for a,b in zip(p,c)); rec&= enigma(c,o,st)==p
print('self-encryptions in 18000 letters:',selfhit,' reciprocal:',rec)
print('AAAAAAAAAA ->',enigma('AAAAAAAAAA',start='BOX'))
# double step positions
def positions(start,n):
    N=[ROT[r][1] for r in ('I','II','III')]; p=[A.index(c) for c in start]; seq=[]
    for _ in range(n):
        if A[p[1]]==N[1]: p[0]=(p[0]+1)%26; p[1]=(p[1]+1)%26
        elif A[p[2]]==N[2]: p[1]=(p[1]+1)%26
        p[2]=(p[2]+1)%26; seq.append(''.join(A[x] for x in p))
    return seq
print('double step from ADU:',positions('ADU',4))
print('window letters after encrypting room 5 from BOX:',positions('BOX',len(L))[-1])
