exec(open('check7.py').read().split("t=time.time(); s=survivors([P")[0])
O=list(itertools.permutations(['I','II','III']))
for c in ['WEAT','WEATH','WEATHER']:
    s=survivors([P.index(crib)],c,orders=O); print(c,'true pos, 6 orders:',len(s),s[:3])
s=survivors([2,20,30],'WEAT',orders=O); print('WEAT at 3 wrong positions, 6 orders:',len(s))
