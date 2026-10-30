from suite import *
for amt in (2,3,4,6,10,20):
    s=new_pond(); run(s,520,summer_feed(amt))
    g=first(s,lambda r:r['M']==0); o=first(s,lambda r:r['O']<3)
    tot=s['ledger']['added']
    yrs_omin=[round(min(r['O'] for r in s['hist'][y*52:(y+1)*52]),1) for y in range(10)]
    print(amt,'/wk each summer: minnows gone',yw(g),'O<3 first',yw(o),'Omin per year',yrs_omin,'gone',present(s),'added',tot, 'Det y5w0 %.0f'%s['hist'][208]['Det'])
