import csv,sys,collections
subj=sys.argv[1]
rows={(r['unit'],int(r['n'])):r for r in csv.DictReader(open(f'input/{subj}.csv',encoding='utf-8'))}
units={r['unit']:r for r in csv.DictReader(open('input/units.csv',encoding='utf-8'))}
cuts=[l.rstrip('\n').split('|',2) for l in open(f'cuts_{subj}.txt',encoding='utf-8') if l.strip()]
out=[];cnt=collections.Counter()
for u,n,why in cuts:
    r=rows[(u,int(n))]; assert r['status']=='open',(u,n)
    assert '\u2014' not in why
    out.append([u,int(n),r['title'],r['type'],r['module'],why.strip()]); cnt[u]+=1
# floor check
bad=[]
for u in sorted({k[0] for k in rows}):
    mods=collections.Counter(); 
    for (uu,n),r in rows.items():
        if uu==u: mods[r['module']]+=1
    fl=2 if len(mods)>10 else 3
    for (uu,n),r in rows.items():
        if uu==u and any(c[0]==u and int(c[1])==n for c in cuts): mods[r['module']]-=1
    for m,c in mods.items():
        if c<fl: bad.append((u,m,c))
    t=int(units[u]['cut_target'])
    if abs(cnt[u]-t)>2: bad.append((u,'count',cnt[u],t))
    elif cnt[u]!=t: print('off',u,cnt[u],t)
print(subj,len(out),'problems',bad)
w=csv.writer(open(f'{subj}.csv','w',newline='',encoding='utf-8'));w.writerow('unit,n,title,type,module,reason'.split(','));w.writerows(sorted(out,key=lambda x:(list(rows.keys()).index((x[0],x[1])))))
