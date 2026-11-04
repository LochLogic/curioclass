r"""Measure the printed length of Worksheet Generator sheets (docs/SUPPLY-CLOSET-PLAN.md, Generators).

    python scripts/check_gen_print.py                 every generator
    python scripts/check_gen_print.py fractions ...   one or more by id
    python scripts/check_gen_print.py --quick         defaults and the highest item count only

scripts/check_generators.mjs checks the answers but cannot see the page. This script opens each generator's real page
from a built dist/ (build with --closet first), sets every setting on its own plus the highest item count with each
other setting, prints the student copy to PDF in headless Chrome, and counts the pages. The limit is the one the
authored worksheets keep: 1 page for a kindergarten sheet, 2 for everything else. The teacher key is not counted
(it is the same pages plus the teacher page). Exit code 1 when any sheet is over its limit.
"""
import asyncio, io, json, os, sys, threading, base64, urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import drive  # noqa: E402  the headless Chrome helper (Chrome path, Tab, ensure_chrome)
from pypdf import PdfReader  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
HTTP_PORT = 8419
REG = json.loads((ROOT / 'data/closet/generators.json').read_text(encoding='utf-8'))
QUICK = '--quick' in sys.argv
WANT = [a for a in sys.argv[1:] if not a.startswith('--')]
IDS = [g['id'] for g in REG['generators'] if not WANT or g['id'] in WANT]
SEEDS = ['TAAAA'] if QUICK else ['TAAAA', 'TAAAB']

# in the page: the settings to try, same idea as check_generators.mjs (defaults, each option alone, number min and
# max, then the biggest item count with each option of every other setting, which is where a sheet gets longest)
COMBOS_JS = r"""
(() => {
  const id = document.getElementById('gen').dataset.gen, def = Gen.defs[id];
  const d = window.__genData || null;
  const base = Gen.values(def, {}, d), out = [base], quick = %s;
  const key = v => JSON.stringify(v), seen = new Set([key(base)]);
  const add = v => { v = Gen.values(def, v, d); if (!seen.has(key(v))) { seen.add(key(v)); out.push(v); } };
  const cnt = def.fields.find(f => f.id === 'count');
  const top = cnt ? (cnt.type === 'number' ? cnt.max : Gen.opts(cnt, base, d).slice(-1)[0][0]) : null;
  if (!quick || top == null) for (const f of def.fields) {
    if (f.type === 'select') for (const [val] of Gen.opts(f, base, d).slice(0, 40)) add({ ...base, [f.id]: val });
    if (f.type === 'check') add({ ...base, [f.id]: !base[f.id] });
    if (f.type === 'number') for (const val of [f.min, f.max]) if (val != null) add({ ...base, [f.id]: val });
    if (f.type === 'text') add({ ...base, [f.id]: 'Plants and animals of the desert' });
  }
  if (top != null) {
    add({ ...base, count: top });
    for (const f of def.fields) {
      if (f.id === 'count') continue;
      const b = Gen.values(def, { ...base, count: top }, d);
      if (f.type === 'select') { const o = Gen.opts(f, b, d); const step = Math.max(1, Math.floor(o.length / 12)); for (let i = 0; i < o.length; i += step) { const val = o[i][0];
        const v = Gen.values(def, { ...b, [f.id]: val }, d);
        add(v);
        // a skill list that depends on the grade: try a few skills of that grade too (a long list, like the Word Wall
        // modules, is sampled: the sheet's length depends on the count and the kind, not on which module)
        for (const g of def.fields) if (g !== f && typeof g.options === 'function') { const o = Gen.opts(g, v, d); const step = Math.max(1, Math.floor(o.length / 6)); for (let i = 0; i < o.length; i += step) add({ ...v, [g.id]: o[i][0] }); }
      } }
      if (f.type === 'check') add({ ...b, [f.id]: !b[f.id] });
    }
  }
  return out.map(v => { const p = new URLSearchParams(); for (const f of def.fields) p.set(f.id, f.type === 'check' ? (v[f.id] ? '1' : '0') : v[f.id]); return [v, p.toString()]; });
})()
"""


class Handler(SimpleHTTPRequestHandler):
    """dist/ the way Cloudflare serves it: /x also finds /x.html (scripts/serve.py starts a server on import, so not imported)."""
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(DIST), **k)

    def send_head(self):
        path = Path(self.translate_path(self.path))
        if not path.exists() and path.with_name(path.name + '.html').is_file():
            self.path = self.path.split('?')[0] + '.html'
        return super().send_head()

    def log_message(self, *a):
        pass


def limit_for(v):
    g = str(v.get('grade', v.get('band', ''))).lower()
    return 1 if g in ('k', 'kindergarten') else 2


async def main():
    httpd = ThreadingHTTPServer(('127.0.0.1', HTTP_PORT), Handler)
    httpd.handle_error = lambda *a: None
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    prof = Path(os.environ.get('TEMP', str(ROOT))).resolve() / 'curio-gen-print-prof'
    drive.ensure_chrome(prof)
    bad_total, rows = 0, []
    try:
        for gid in IDS:
            req = urllib.request.Request(f'http://127.0.0.1:{drive.PORT}/json/new?about:blank', method='PUT')
            info = json.loads(urllib.request.urlopen(req).read())
            async with drive.websockets.connect(info['webSocketDebuggerUrl'], max_size=2**28) as ws:
                t = drive.Tab(ws); asyncio.create_task(t.reader())
                for d in ['Page', 'Runtime']:
                    await t.send(d + '.enable')
                await t.send('Emulation.setDeviceMetricsOverride', width=1000, height=1400, deviceScaleFactor=1, mobile=False)
                page = f'http://127.0.0.1:{HTTP_PORT}/closet/worksheets/make/{gid}/'
                await t.send('Page.navigate', url=page)
                for _ in range(100):   # wait for the page and its generator script
                    await asyncio.sleep(.1)
                    r = await t.send('Runtime.evaluate', expression="!!(window.Gen && document.getElementById('gen') && Gen.defs[document.getElementById('gen').dataset.gen])", returnByValue=True)
                    if r['result'].get('value'):
                        break
                # the data file some generators fetch (the Word Wall list), so the combo list can see its options
                r = await t.send('Runtime.evaluate', expression="(async () => { const def = Gen.defs[document.getElementById('gen').dataset.gen]; if (def.data) window.__genData = await (await fetch('/closet/worksheets/make/' + def.data + '.json')).json(); return 'ok'; })()", awaitPromise=True, returnByValue=True)
                r = await t.send('Runtime.evaluate', expression=COMBOS_JS % ('true' if QUICK else 'false'), returnByValue=True)
                if r.get('exceptionDetails'):
                    print(f'{gid}: could not list settings: {json.dumps(r["exceptionDetails"])[:300]}'); bad_total += 1; continue
                combos = r['result']['value']
                worst, bad, n = (0, None), [], 0
                for v, qs in combos:
                    for seed in SEEDS:
                        await t.send('Page.navigate', url=f'{page}?{qs}&s={seed}')
                        for _ in range(40):   # wait for the sheet
                            await asyncio.sleep(.1)
                            r = await t.send('Runtime.evaluate', expression="!!document.querySelector('#gen-view .ws-sheet')", returnByValue=True)
                            if r['result'].get('value'):
                                break
                        await asyncio.sleep(.15)
                        pdf = await t.send('Page.printToPDF', printBackground=True, preferCSSPageSize=True)
                        pages = len(PdfReader(io.BytesIO(base64.b64decode(pdf['data']))).pages)
                        n += 1
                        if pages > worst[0]:
                            worst = (pages, v)
                        if pages > limit_for(v):
                            bad.append((pages, v, seed))
                rows.append((gid, n, worst, bad))
                print(f'{gid}: {n} sheets, longest {worst[0]} page{"s" if worst[0] != 1 else ""}, {len(bad) or "none"} over the limit' + (f'   [{json.dumps(worst[1])}]' if bad else ''))
                for pages, v, seed in bad[:8]:
                    print(f'  {pages} pages   settings {json.dumps(v)} sheet {seed}')
                if len(bad) > 8:
                    print(f'  ... {len(bad) - 8} more')
                bad_total += bool(bad)
                await t.send('Page.close')
    finally:
        httpd.shutdown()
        drive.close_chrome()
    print(f'{bad_total} generator(s) over the page limit' if bad_total else f'all {len(IDS)} generators print within their limit')
    sys.exit(1 if bad_total else 0)


if __name__ == '__main__':
    asyncio.run(main())
