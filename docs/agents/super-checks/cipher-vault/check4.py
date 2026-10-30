from solver2 import *
import time
exec(open('check3.py').read().split('res={}')[0])
f=lambda s: score(s)+2*wscore(s)
t0=time.time()
for n in [30,50,75,100,150,200]:
    ok=0;uniq=0;tot=0
    for ti,t in enumerate(T):
        for s in range(2):
            p=prefix(t,n); key=list(A); random.Random(ti*10+s+n).shuffle(key); key=''.join(key); ct=sub(p,key)
            cands=[solve(ct,iters=2500,restarts=10,seed=s+j,use_words=uw) for j,uw in ((0,True),(1,False),(2,True))]
            d=max(cands,key=f)
            a=sum(x==y for x,y in zip(letters(d),letters(p)))/len(letters(p))
            ok+=a>=0.9; uniq+= f(p)>=f(d)-1e-9; tot+=1
    print(n,'cracked',ok,'/',tot,' true text scores best or tied',uniq,'/',tot, round(time.time()-t0))
