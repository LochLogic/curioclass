from pond import *
import sys
s=new_pond(); t0=ident(s); run(s,520); show(s,13)
print('drift',ident(s)-t0,'log',s['log'][:8])
s2=new_pond(decomp_on=False); run(s2,520); print('--- no decomposers'); show(s2,26)
