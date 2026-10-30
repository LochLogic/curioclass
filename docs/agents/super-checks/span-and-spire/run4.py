from designs import *
T5=['Pickup','School bus','Fire engine','Grain truck','Semi']
def mk(J,M,sup,deckpts):
    tr=Truss(J,M,sup); tr.abut={J.index((0,0)),J.index((24,0))}
    deck=[J.index(p) for p in deckpts]; return tr,deck
def run(name,J,M,sup,deckpts,trucks=T5):
    J=[tuple(map(float,p)) for p in J]
    idx=lambda p: J.index(tuple(map(float,p)))
    MM=[(idx(a),idx(b),t) for a,b,t in M]
    tr=Truss(J,MM,{idx(p):k for p,k in sup.items()}); tr.abut={idx((0,0)),idx((24,0))}
    deck=[idx(p) for p in deckpts]
    report(tr,deck,name,trucks); return tr,deck
deckpts=[(x,0) for x in range(0,25,4)]
D=[((x,0),(x+4,0),'T') for x in range(0,24,4)]
# through arch, no bracing
J=deckpts+[(2,-2),(22,-2),(8,4),(12,5),(16,4)]
M=D+[((2,-2),(4,0),'T'),((4,0),(8,4),'T'),((8,4),(12,5),'T'),((12,5),(16,4),'T'),((16,4),(20,0),'T'),((20,0),(22,-2),'T'),
     ((8,4),(8,0),'C'),((12,5),(12,0),'C'),((16,4),(16,0),'C')]
sup={(0,0):'pin',(24,0):'roller',(2,-2):'pin',(22,-2):'pin'}
run('through arch, cable hangers, no bracing',J,M,sup,deckpts)
M2=M+[((8,4),(12,0),'C'),((12,0),(16,4),'C'),((4,0),(8,4),'T')]
M2=M+[((8,4),(12,0),'C'),((12,5),(8,0),'C'),((12,5),(16,0),'C'),((16,4),(12,0),'C')]
run('through arch, cable hangers + crossed cables',J,M2,sup,deckpts)
# pier in stream
J=deckpts+[(12,-5),(4,2),(8,2),(16,2),(20,2)]
M=D+[((12,0),(12,-5),'T')]
run('deck + pier only',J[:8],M,{(0,0):'pin',(24,0):'roller',(12,-5):'pin'},deckpts)
