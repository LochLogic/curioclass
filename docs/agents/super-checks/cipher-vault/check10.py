from solver2 import *
import json
D=json.load(open('rooms.json')); otp=D['otp']
alt='THE VAULT IS EMPTY GO HOME'; a=letters(alt); print(len(a))
k=''.join(A[(A.index(c)-A.index(p))%26] for c,p in zip(otp,a)); print('key for alt',k)
lip=('A BIG BROWN DOG RAN UP A HILL TO FIND HIS BALL. IT WAS NOT ON TOP, SO HIS PAL, A SMALL GRAY CAT, LOOKS IN A DITCH AND FINDS IT. '
     'NOW THAT DOG IS SO HAPPY THAT HIS TAIL WAGS AND WAGS. HIS PAL NAPS IN THE SUN AS HE RUNS IN CIRCLES AROUND HIS FAVORITE TRUNK.')
lip=('A BIG BROWN DOG RAN UP A HILL TO FIND HIS BALL. IT WAS NOT ON TOP, SO HIS PAL, A SMALL GRAY CAT, LOOKS IN A DITCH AND FINDS IT. '
     'NOW THAT DOG IS SO HAPPY THAT HIS TAIL WAGS AND WAGS. HIS PAL NAPS IN A SUNNY SPOT AS HIS DOG BUDDY RUNS IN LOOPS AROUND A BIG OAK.')
print('E in lipogram:',letters(lip).count('E'),'letters',len(letters(lip)))
key=list(A); random.Random(5).shuffle(key); key=''.join(key); ct=sub(lip,key)
L=letters(ct); top=collections.Counter(L).most_common(3); print('top cipher letters decode to',[unsub(c,key) for c,_ in top])
f=lambda s: score(s)+2*wscore(s)
d=max([solve(ct,iters=3000,restarts=10,seed=j,use_words=uw) for j,uw in ((0,True),(1,False),(2,True))],key=f)
print('solver acc on lipogram',round(sum(x==y for x,y in zip(letters(d),letters(lip)))/len(letters(lip)),2)); print(d[:90])
# double vigenere crack harder: RAVEN then CAT on room4 text; splitter finds 15?
R4=json.load(open('rooms.json'))['R']['4']; c=vig(vig(R4,'RAVEN'),'CAT'); Lc=letters(c)
sc={kk:round(sum(ioc(Lc[i::kk]) for i in range(kk))/kk,4) for kk in range(1,17)}; print('double key IoC by length',sc)
