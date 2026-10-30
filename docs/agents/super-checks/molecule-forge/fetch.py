import json, urllib.request, urllib.parse, time
BOOK = ["hydrogen","oxygen","nitrogen","chlorine","hydrogen chloride","water","hydrogen sulfide","ammonia","carbon dioxide",
"methane","hydrogen peroxide","acetylene","formic acid","silane","hydrazine","methanol","ethylene","urea","ethane","acetic acid",
"ethanol","dimethyl ether","acetone","propane","butane","isobutane","isopropyl alcohol","glycine","benzene",
"vanillin","aspirin","caffeine"]
ALSO = ["formaldehyde","acetaldehyde","formamide","propene","propyne","cyclopropane","cyclohexane","1-propanol","methoxyethane",
"chloromethane","dichloromethane","chloroform","carbon tetrachloride","methylamine","methanethiol","hydrogen cyanide",
"hypochlorous acid","carbonic acid","carbon disulfide","carbonyl sulfide","sulfur dichloride","dichlorine monoxide",
"ethylene glycol","disilane","hydroxylamine","chloramine","dimethylamine","ethylamine","acetonitrile","cyclohexene","toluene","cyclopentane","ethylene oxide","allene","ketene","diazene","methanimine","aziridine","cyclopropene","methylhydrazine"]
out={}
for n in BOOK+ALSO:
    u="https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/%s/property/MolecularFormula,SMILES,AtomStereoCount,BondStereoCount,Charge/JSON"%urllib.parse.quote(n)
    try:
        d=json.load(urllib.request.urlopen(u,timeout=20))["PropertyTable"]["Properties"][0]
    except Exception as e:
        d={"err":str(e)}
    out[n]=d; print(n,d); time.sleep(0.25)
json.dump({"book":BOOK,"also":ALSO,"data":out},open("pubchem.json","w"),indent=1)
