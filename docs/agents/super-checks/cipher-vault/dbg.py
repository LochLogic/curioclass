from solver2 import *
exec(open('check3.py').read().split('res={}')[0])
for ti,t in enumerate(T):
  p=prefix(t,200); key=list(A); random.Random(ti*10+200).shuffle(key); key=''.join(key)
  ct=sub(p,key)
  for uw in (True,False):
    d=solve(ct,iters=4000,restarts=12,seed=1,use_words=uw)
    a=sum(x==y for x,y in zip(letters(d),letters(p)))/len(letters(p))
    print(ti,uw,round(a,2),round(score(d)+2*wscore(d)),round(score(p)+2*wscore(p)),d[:70])
