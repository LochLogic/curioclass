from ciphers import *
W=sum(words.values()); wl={w:math.log10(c/W) for w,c in words.items() if c>=3}
def wscore(s):
    ws=re.sub('[^A-Z ]',' ',s).split()
    return sum(wl.get(w,-9) for w in ws)
def solve(ct,iters=3000,restarts=10,seed=0,use_words=True):
    rng=random.Random(seed); L=letters(ct); best=(-1e18,None)
    order=[c for c,_ in collections.Counter(L).most_common()]+[c for c in A if c not in L]
    eng=sorted(A,key=lambda a:-ENG[a])
    f=(lambda s: score(s)+ (2*wscore(s) if use_words else 0))
    for r in range(restarts):
        key={order[i]:eng[i] for i in range(26)}
        if r>=restarts//2:
            p=list(A); rng.shuffle(p); key=dict(zip(A,p))
        elif r:
            for _ in range(r*2):
                a,b=rng.sample(A,2); key[a],key[b]=key[b],key[a]
        dec=lambda k:''.join(k.get(c,c) for c in ct)
        s=f(dec(key)); stale=0
        while stale<iters:
            a,b=rng.sample(A,2); key[a],key[b]=key[b],key[a]
            s2=f(dec(key))
            if s2>=s: s=s2; stale=0 if s2>s else stale+1
            else: key[a],key[b]=key[b],key[a]; stale+=1
        if s>best[0]: best=(s,dict(key))
    return ''.join(best[1].get(c,c) for c in ct)
