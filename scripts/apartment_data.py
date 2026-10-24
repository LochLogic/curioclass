"""Builds tools/first-apartment-budget/places.json: rents and starting pay for each city in the game.

Rents: HUD Fair Market Rents, FY2026 (the 40th-percentile gross rent, which includes utilities), read from
FY26_FMRs_revised.xlsx. Pay: BLS OEWS annual 25th-percentile wage in each metro area (latest year), our stand-in
for starting pay; national figures fill any gap.

    python scripts/apartment_data.py <FY26 FMR xlsx>
"""
import io, json, os, re, sys, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from bls import oews, fetch
import openpyxl

OUT = os.path.join(os.path.dirname(__file__), '..', 'tools', 'first-apartment-budget', 'places.json')

# id, name, HUD area name prefix, OEWS metro code(s)
CITIES = [
    ('fortwayne', 'Fort Wayne, IN', 'Fort Wayne, IN HUD Metro', [23060]),
    ('columbus', 'Columbus, OH', 'Columbus, OH HUD Metro', [18140]),
    ('houston', 'Houston, TX', 'Houston-The Woodlands', [26420]),
    ('phoenix', 'Phoenix, AZ', 'Phoenix-Mesa', [38060]),
    ('denver', 'Denver, CO', 'Denver-Aurora', [19740]),
    ('boston', 'Boston, MA', 'Boston-Cambridge-Quincy', [14460, 71650]),
    ('seattle', 'Seattle, WA', 'Seattle-Bellevue', [42660]),
]
JOBS = [
    ('retail', '41-2031'), ('cook', '35-2014'), ('warehouse', '53-7062'), ('service', '43-4051'),
    ('pharmtech', '29-2052'), ('medassist', '31-9092'), ('electrician', '47-3013'), ('hvac', '49-9021'),
    ('nurse', '29-1141'), ('accountant', '13-2011'), ('webdev', '15-1254'),
]


def fmr_rows(path):
    # HUD's file carries a malformed modified date that openpyxl rejects; patch it in memory.
    zin, buf = zipfile.ZipFile(path), io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            b = zin.read(it.filename)
            if it.filename == 'docProps/core.xml':
                b = re.sub(rb'(\d{4})- (\d)-', rb'\1-0\2-', b)
            zout.writestr(it, b)
    rows = list(openpyxl.load_workbook(buf, read_only=True).active.iter_rows(values_only=True))
    h = rows[0]
    return [dict(zip(h, r)) for r in rows[1:]]


rows = fmr_rows(sys.argv[1])
series = [oews(soc, '12') for _, soc in JOBS]
for *_, areas in CITIES:
    series += [oews(soc, '12', a) for a in areas for _, soc in JOBS]
bls = fetch(series)

out = {'cities': [], 'jobs': {}}
for jid, soc in JOBS:
    v = bls[oews(soc, '12')]
    out['jobs'][jid] = {'national': round(v['value']), 'year': v['year']}
for cid, name, hud, areas in CITIES:
    r = next(r for r in rows if str(r['hud_area_name']).startswith(hud))
    pay = {}
    for jid, soc in JOBS:
        v = next((bls[oews(soc, '12', a)] for a in areas if bls[oews(soc, '12', a)]), None)
        pay[jid] = round(v['value']) if v else None
        if not v: print('no local pay:', name, jid)
    # BLS suppresses a few local estimates; fill them from the national figure scaled by this city's pay level
    known = [pay[j] / out['jobs'][j]['national'] for j in pay if pay[j]]
    level = sorted(known)[len(known) // 2]
    est = [j for j in pay if not pay[j]]
    for j in est: pay[j] = int(round(out['jobs'][j]['national'] * level, -1))
    out['cities'].append({'est': est, 'id': cid, 'name': name, 'hud': r['hud_area_name'],
                          'fmr': [r['fmr_0'], r['fmr_1'], r['fmr_2'], r['fmr_3']], 'pay': pay})
json.dump(out, open(OUT, 'w', encoding='utf-8'), separators=(',', ':'))
for c in out['cities']: print(c['name'], c['fmr'], c['pay'], c['est'])
