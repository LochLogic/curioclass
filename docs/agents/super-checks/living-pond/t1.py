from pond import *
s=new_pond(); t0=ident(s); run(s,520)
show(s,13)
print('ident drift',ident(s)-t0, s['log'][:12])
