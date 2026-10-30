import ast, os, sys, re, collections, math, pickle
lib = os.path.dirname(os.__file__)
txt=[]
for root,d,fs in os.walk(lib):
    if 'site-packages' in root or 'test' in root: continue
    for f in fs:
        if f.endswith('.py'):
            try: t=ast.parse(open(os.path.join(root,f),encoding='utf8').read())
            except Exception: continue
            for n in ast.walk(t):
                if isinstance(n,(ast.FunctionDef,ast.ClassDef,ast.Module,ast.AsyncFunctionDef)):
                    s=ast.get_docstring(n)
                    if s: txt.append(s)
s=' '.join(txt).upper()
s=re.sub(r'[^A-Z ]+',' ',s); s=re.sub(' +',' ',s)
print(len(s))
L=re.sub('[^A-Z]','',s)
q=collections.Counter(L[i:i+4] for i in range(len(L)-3))
N=sum(q.values())
lq={k:math.log10(v/N) for k,v in q.items()}
floor=math.log10(0.01/N)
words=collections.Counter(s.split())
pickle.dump((lq,floor,words),open('model.pkl','wb'))
print(N,len(lq),words.most_common(12))
