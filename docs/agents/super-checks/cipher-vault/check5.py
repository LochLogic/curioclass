from ciphers import *
import json
D=json.load(open('rooms.json')); R={int(k):v for k,v in D['R'].items()}; C={int(k):v for k,v in D['C'].items()}
L=letters(C[4]); print('R4 letters',len(L))
reps=collections.defaultdict(list)
for i in range(len(L)-2): reps[L[i:i+3]].append(i)
reps={k:v for k,v in reps.items() if len(v)>1}
gaps=[]
for k,v in sorted(reps.items(),key=lambda kv:-len(kv[1])):
    g=[v[i+1]-v[i] for i in range(len(v)-1)]; gaps+=g
    print(k,v,'gaps',g)
for m in range(2,11): print('gaps divisible by',m,':',sum(g%m==0 for g in gaps),'of',len(gaps))
for k in range(1,9):
    cols=[L[i::k] for i in range(k)]; print('key length',k,'mean IoC',round(sum(ioc(c) for c in cols)/k,4),'col sizes',min(map(len,cols)))
print('English IoC approx', round(sum((v/100)**2 for v in ENG.values()),4),' random',round(1/26,4))
key=''.join(A[chi_shift(L[i::5])] for i in range(5)); print('chi-square key at length 5:',key)
print('decrypt ok', vig(C[4],key,-1)==R[4])
# Caesar-room counter: Caesar on R3 plaintext -> chi finds shift
print('caesar chi on R3 pt shift 11 ->',chi_shift(caesar(letters(R[3]),11)))
