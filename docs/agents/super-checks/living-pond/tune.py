import pond, sys, json
from pond import *
def go(over=None, weeks=520, show_every=13, **kw):
    if over:
        for k,v in over.items():
            if isinstance(v,dict): P['sp'][k].update(v)
            else: P[k]=v
    s=new_pond(**kw); run(s,weeks)
    show(s,show_every)
    # winter resp
    print('log',s['log'][:6])
    return s
if __name__=='__main__':
    over=json.loads(sys.argv[1]) if len(sys.argv)>1 else None
    s=go(over)
    for y in range(3):
        rows=s['hist'][y*52+35:y*52+52]
        print('y',y,'week resp/G in fall-winter', [(r['week']%52, round(r['acc']['resp'],1), round(r['acc']['G'],1), round(r['O'],1)) for r in rows[::2]])
