def lin(c): c/=255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def rgb(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]
def lum(h): r,g,b=map(lin,rgb(h)); return .2126*r+.7152*g+.0722*b
def cr(a,b): x,y=sorted([lum(a),lum(b)]); return (y+.05)/(x+.05)
def lab(h):
    r,g,b=map(lin,rgb(h)); X=(r*.4124+g*.3576+b*.1805)/.95047; Y=r*.2126+g*.7152+b*.0722; Z=(r*.0193+g*.1192+b*.9505)/1.08883
    f=lambda t: t**(1/3) if t>0.008856 else 7.787*t+16/116
    return 116*f(Y)-16,500*(f(X)-f(Y)),200*(f(Y)-f(Z))
def dE(a,b): return sum((x-y)**2 for x,y in zip(lab(a),lab(b)))**.5
bg,panel,ink,muted,brand,bink,amber,paper,pink='#15171c','#1e2128','#efe9dc','#a9a294','#3cc7a2','#06231b','#ffc94a','#efe4cc','#2a2118'
for n,a,b in [('ink/bg',ink,bg),('ink/panel',ink,panel),('muted/bg',muted,bg),('muted/panel',muted,panel),('brand/bg',brand,bg),('brand/panel',brand,panel),('brandink/brand',bink,brand),('amber/bg',amber,bg),('paperink/paper',pink,paper),('focus amber/panel',amber,panel)]:
    print(n,round(cr(a,b),2))
for n,h in [('phishing',"#3ee6ff"),('molecule',"#5fd4ff"),('data-def','#875a00'),('ctf','#ff7ac8'),('packet','#b42318'),('model-mech','#a3e635'),('chore','#0e7490'),('code-kitchen','#9a4a12'),('algo','#1e3a8a'),('misleading','#a21caf'),('internet-j','#6a3d9a')]:
    print('dE vs',n,round(dE(brand,h),1))
