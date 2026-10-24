"""Small cached client for the BLS public API v1 (no key, 25 series per request, 25 requests a day).
OEWS series: OEU + area type (N national, M metro) + 7-digit area + 6-digit industry + 6-digit SOC + 2-digit data type.
Data types used: 01 employment, 08 hourly median, 12 annual 25th percentile, 13 annual median."""
import json, os, sys, urllib.request

CACHE = os.path.join(os.environ.get('CURIO_CACHE', os.path.join(os.path.dirname(__file__), '..', 'Gemini')), 'bls_cache.json')


def oews(soc, dtype, area=None):
    soc = soc.replace('-', '')[:6]
    return f"OEU{'M' if area else 'N'}{(area or 0):07d}000000{soc}{dtype}"


def fetch(series):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [s for s in dict.fromkeys(series) if s not in cache]
    for i in range(0, len(todo), 25):
        body = json.dumps({'seriesid': todo[i:i + 25]}).encode()
        req = urllib.request.Request('https://api.bls.gov/publicAPI/v1/timeseries/data/', body, {'Content-Type': 'application/json'})
        res = json.load(urllib.request.urlopen(req, timeout=60))
        if res['status'] != 'REQUEST_SUCCEEDED':
            sys.exit(f"BLS: {res['message']}")
        for s in res['Results']['series']:
            d = [x for x in s['data'] if x['value'] not in ('-', '*', '#')]
            cache[s['seriesID']] = {'year': d[0]['year'], 'value': float(d[0]['value'])} if d else None
        json.dump(cache, open(CACHE, 'w'), indent=0)
    return {s: cache.get(s) for s in series}
