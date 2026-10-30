import random, string, math, pickle, re, itertools, collections
A=string.ascii_uppercase
lq,floor,words=pickle.load(open('model.pkl','rb'))
def letters(s): return re.sub('[^A-Z]','',s.upper())
def caesar(s,k): return ''.join(A[(A.index(c)+k)%26] if c in A else c for c in s.upper())
def vig(s,key,d=1):
    out=[];i=0
    for c in s.upper():
        if c in A: out.append(A[(A.index(c)+d*A.index(key[i%len(key)]))%26]); i+=1
        else: out.append(c)
    return ''.join(out)
def sub(s,keyalpha): return ''.join(keyalpha[A.index(c)] if c in A else c for c in s.upper())
def unsub(s,keyalpha): return ''.join(A[keyalpha.index(c)] if c in A else c for c in s.upper())
def score(s):
    L=letters(s); return sum(lq.get(L[i:i+4],floor) for i in range(len(L)-3))
ENG={'A':8.04,'B':1.48,'C':3.34,'D':3.82,'E':12.49,'F':2.40,'G':1.87,'H':5.05,'I':7.57,'J':0.16,'K':0.54,'L':4.07,'M':2.51,'N':7.23,'O':7.64,'P':2.14,'Q':0.12,'R':6.28,'S':6.51,'T':9.28,'U':2.73,'V':1.05,'W':1.68,'X':0.23,'Y':1.66,'Z':0.09}
def chi_shift(col):
    n=len(col); best=None
    for k in range(26):
        d=caesar(col,-k); c=collections.Counter(d)
        x=sum((c.get(a,0)-n*ENG[a]/100)**2/(n*ENG[a]/100) for a in A)
        if best is None or x<best[0]: best=(x,k)
    return best[1]
def ioc(s):
    c=collections.Counter(s); n=len(s)
    return sum(v*(v-1) for v in c.values())/(n*(n-1)) if n>1 else 0
# Enigma I simplified: rotors I II III (left..right), UKW-B, rings A, no plugboard, real stepping with double step
ROT={'I':('EKMFLGDQVZNTOWYHXUSPAIBRCJ','Q'),'II':('AJDKSIRUXBLHWTMCQGZNPYFVOE','E'),'III':('BDFHJLCPRTXVZNYEIWGAKMUSQO','V'),
     'IV':('ESOVPZJAYQUIRHXLNFTGKDCMWB','J'),'V':('VZBRGITYUPSDNHLXAWMJQOFECK','Z')}
REF='YRUHQSLDPXNGOKMIEBFZCWVJAT'
def enigma(text,order=('I','II','III'),start='AAA',plug=None):
    W=[ROT[r][0] for r in order]; N=[ROT[r][1] for r in order]
    p=[A.index(c) for c in start]; out=[]
    pb={}
    if plug:
        for a,b in plug: pb[a]=b; pb[b]=a
    for ch in text.upper():
        if ch not in A: out.append(ch); continue
        # stepping
        if A[p[1]]==N[1]: p[0]=(p[0]+1)%26; p[1]=(p[1]+1)%26
        elif A[p[2]]==N[2]: p[1]=(p[1]+1)%26
        p[2]=(p[2]+1)%26
        c=A.index(pb.get(ch,ch))
        for i in (2,1,0): c=(A.index(W[i][(c+p[i])%26])-p[i])%26
        c=A.index(REF[c])
        for i in (0,1,2): c=(W[i].index(A[(c+p[i])%26])-p[i])%26
        out.append(pb.get(A[c],A[c]))
    return ''.join(out)
def hill_sub(ct, iters=4000, restarts=8, seed=0):
    rng=random.Random(seed); best=(-1e18,None)
    L=letters(ct)
    # start from frequency-rank guess
    order=[c for c,_ in collections.Counter(L).most_common()]+[c for c in A if c not in L]
    eng=sorted(A,key=lambda a:-ENG[a])
    for r in range(restarts):
        key={order[i]:eng[i] for i in range(26)}  # cipher->plain
        if r: 
            for _ in range(r*3):
                a,b=rng.sample(A,2); key[a],key[b]=key[b],key[a]
        dec=lambda k:''.join(k.get(c,c) for c in ct)
        s=score(dec(key)); stale=0
        while stale<iters:
            a,b=rng.sample(A,2); key[a],key[b]=key[b],key[a]
            s2=score(dec(key))
            if s2>s: s=s2; stale=0
            else: key[a],key[b]=key[b],key[a]; stale+=1
        if s>best[0]: best=(s,dict(key))
    return ''.join(best[1].get(c,c) for c in ct)
