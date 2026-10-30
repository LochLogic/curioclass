import itertools
W='''the a an and to of in is it on at by for from with as be was are not no yes go see run eat sit get got let put bad big dog cat sun hot red ten one two six man men car bus top box fox hat pen pig cow egg leg arm ear eye day way say may now new old you all can her his him she he we me my our out off up us its two who why how did had has use can cup map mat mud nap net nut pan pet pot rat rug sad bag bed bee bit bun cab cap cut dad den dig dot fan fat fig fin fit fun gum gym hen hid hip hit hop hug hum hut jam jar jet jog kid kit lab lap lid lip lit log mom mop nod pal pat pig pin pit pop pup rag ram ran rid rip rob rod rot rub sat set sip sob tag tan tap tin tip toe ton tub tug van vet wag web wet win wig yak zip
meet meat team seen soon noon moon book look took cook good food feed need seed tree free three green sleep sheep keep deep week jump help send come home here there where when what that this then them they time tile late gate game same name came make take cake lake bake rake ride side hide wide note vote rose nose hose bell tell well sell fell yell ball call fall hall tall wall mall fill hill will mill kill pill bill till door poor floor road load toad boat coat goat moat park dark bark mark barn yarn farm harm cold bold gold hold told fold rain gain main pain train snow slow glow show grow blow flow know crow stop shop drop chop frog flag swim spin skip ship fish dish wish kiss miss less mess dress press class grass glass pass bridge river noon dawn dusk night today lunch fort camp path gift
'''.split()
W=sorted(set(w.upper() for w in W))
def pat(s):
    m={};out=[]
    for ch in s:
        if ch==' ': out.append(' '); continue
        m.setdefault(ch,len(m)); out.append(m[ch])
    return tuple(out)
for msg in ['MEET AT TEN','SEND HELP NOW','SEE YOU SOON','MEET AT NOON']:
    ws=msg.split(); P=pat(msg); found=[]
    cands=[[w for w in W if len(w)==len(x)] for x in ws]
    for combo in itertools.product(*cands):
        s=' '.join(combo)
        if s!=msg and pat(s)==P: found.append(s)
    print(msg,len(found),found[:12])
