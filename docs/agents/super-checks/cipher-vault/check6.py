from ciphers import *
exec(open('check3.py').read().split('res={}')[0].replace('from solver2 import *',''))
big=letters(' '.join(T))
rng=random.Random(7)
for per in [4,6,8,10,15,20,30,40]:
    shift_ok=0;shift_tot=0;key_ok=0;key_tot=0
    for trial in range(200):
        Lk=rng.randint(3,7); n=per*Lk; st=rng.randint(0,len(big)-n); p=big[st:st+n]
        key=''.join(rng.choice(A) for _ in range(Lk)); c=vig(p,key)
        g=''.join(A[chi_shift(c[i::Lk])] for i in range(Lk))
        shift_ok+=sum(a==b for a,b in zip(g,key)); shift_tot+=Lk; key_ok+=g==key; key_tot+=1
    print('letters per column',per,': shifts right',round(shift_ok/shift_tot,2),' whole key right',round(key_ok/key_tot,2))
# key length detection by IoC (pick k in 1..8 with highest mean IoC, ties to smaller multiples)
for n in [40,80,120,200]:
    ok=0
    for trial in range(200):
        Lk=rng.randint(3,7); st=rng.randint(0,len(big)-n); p=big[st:st+n]; key=''.join(rng.choice(A) for _ in range(Lk)); c=vig(p,key)
        sc={k:sum(ioc(c[i::k]) for i in range(k))/k for k in range(1,9)}
        best=max(sc.values()); cand=min(k for k in sc if sc[k]>=0.9*best)
        ok+= cand==Lk
    print('message',n,'letters: key length found by splitter',round(ok/200,2))
