r"""Mechanical audit of a bundled tool: the checks every Refine lens used to repeat by hand, as one report.

    python scripts/audit_tool.py <tool-id> <outdir> [--port 9383] [--profile <absolute dir>] [--no-walk]

Bundle first (CURIO_DRAFT=1 python scripts/bundle_tool.py <id>). Writes <outdir>/audit.md and frames. Checks:
  sizes   every STANDARDS size, 375 through an iframe host served from <outdir> (the tool folder is not touched):
          sideways scroll, targets under 44 px (60 px for K-2), controls below the fold, controls with no name,
          overlapping controls and labels, clipped text, the hint in view and not clipped, text under 10 px,
          focus taken on load, console errors
  calm    Motion off: animations still running forever
  walk    at 1366x768, a fresh page per control, one held click each: errors, focus lost or the control rebuilt
          under the pointer, other controls jumping, what was spoken; then the controls that spoke get five held
          clicks 2 s apart: a how-to line spoken twice, an event line lost
It is a checklist, not a judge: every row is a lead for the lens to confirm on its own frames. It cannot see
teaching, giveaways, feel, art or whether a line is right, and a clean report does not mean a clean tool.
"""
import asyncio, base64, functools, http.server, json, re, sys, threading, urllib.request
from pathlib import Path
import websockets

sys.path.insert(0, str(Path(__file__).resolve().parent))
import drive  # Tab, ensure_chrome, close_chrome: one Chrome, closed at the end

ROOT = Path(__file__).resolve().parent.parent
SIZES = [(680, 425), (800, 500), (1000, 625), (1280, 720), (1366, 768), (1920, 1080), (760, 900)]

PAGE_JS = r"""
(() => {
const W = innerWidth, H = innerHeight, K2 = %K2%, T = K2 && W >= 1100 ? 60 : 44, KIT = new Set(['motion', 'sound', 'read']);
const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el);
  return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05 && !el.closest('[hidden],[aria-hidden="true"],[inert]'); };
const name = el => (el.getAttribute('aria-label') || el.textContent || el.title || el.value || el.getAttribute('alt') || '').replace(/\s+/g, ' ').trim().slice(0, 40);
const tag = el => { const n = name(el); return (el.id ? '#' + el.id : el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '')) + (n ? ' "' + n + '"' : ''); };
const ctl = [...document.querySelectorAll('button, [role=button], a[href], input:not([type=hidden]), select, textarea, summary, [tabindex]:not([tabindex="-1"])')].filter(vis);
const out = {hscroll: Math.max(0, document.documentElement.scrollWidth - W), small: [], below: [], noname: [], overlap: [], clipped: [], tiny: [], focus: null, hint: null, count: ctl.length};
for (const el of ctl) {
  const r = el.getBoundingClientRect();
  if (el.type === 'range') { if (r.height < T * 0.5 && r.width < T) out.small.push(tag(el) + ` ${Math.round(r.width)}x${Math.round(r.height)} (slider)`); }
  else if (Math.min(r.width, r.height) < (KIT.has(el.id) ? 44 : T) - 0.5) out.small.push(tag(el) + ` ${Math.round(r.width)}x${Math.round(r.height)}`);
  if (r.top >= H - 2) out.below.push(tag(el) + ` top ${Math.round(r.top)}`);
  if (!name(el) && !el.getAttribute('aria-labelledby')) out.noname.push(tag(el));
}
// labels: elements with their own text, small enough to be a label or badge
const own = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
const texts = [...document.querySelectorAll('body *')].filter(el => own(el) && vis(el)).filter(el => { const r = el.getBoundingClientRect(); return r.width < 500 && r.height < 160; });
const boxes = [...new Set([...ctl, ...texts])].slice(0, 700).map(el => ({el, r: el.getBoundingClientRect()}));
for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
  const a = boxes[i], b = boxes[j];
  if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
  const ix = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), iy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
  if (ix > 3 && iy > 3 && out.overlap.length < 25) out.overlap.push(`${tag(a.el)} / ${tag(b.el)} ${Math.round(ix)}x${Math.round(iy)}`);
}
for (const el of texts) {
  const s = getComputedStyle(el), r = el.getBoundingClientRect();
  const hidesX = /hidden|clip/.test(s.overflowX) || s.textOverflow === 'ellipsis', hidesY = /hidden|clip/.test(s.overflowY);
  if ((hidesX && el.scrollWidth > el.clientWidth + 1) || (hidesY && el.scrollHeight > el.clientHeight + 1)) out.clipped.push(tag(el) + ' (cut by its box)');
  else if (r.right > W + 1 || r.left < -1) out.clipped.push(tag(el) + ' (past the window edge)');
  const fs = parseFloat(s.fontSize) * (el.closest('svg') ? 1 : 1);
  if (fs < 10 && out.tiny.length < 8) out.tiny.push(tag(el) + ` ${fs.toFixed(1)}px`);
}
const h = document.getElementById('hint');
if (h) { const r = h.getBoundingClientRect();
  out.hint = {text: h.textContent.replace(/\s+/g, ' ').trim().slice(0, 160), inView: r.top >= -1 && r.bottom <= H + 1 && vis(h), cut: h.scrollHeight > h.clientHeight + 1 && /hidden|clip/.test(getComputedStyle(h).overflowY)}; }
const a = document.activeElement; if (a && a !== document.body && a !== document.documentElement) out.focus = tag(a);
return out;
})()
"""

CALM_JS = r"""(() => (document.getAnimations ? document.getAnimations() : []).filter(a => a.playState === 'running' && a.effect && a.effect.getTiming().iterations === Infinity && (a.effect.getComputedTiming().duration || 0) > 1)
  .map(a => (a.animationName || a.constructor.name) + ' on ' + (a.effect.target ? (a.effect.target.id ? '#' + a.effect.target.id : a.effect.target.tagName.toLowerCase()) : '?')).slice(0, 10))()"""

# tags every visible control in DOM order (the same order on every fresh load), returns [[i, label, x, y]]
TAG_JS = r"""(() => { const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05 && !el.closest('[hidden],[aria-hidden="true"],[inert]'); };
  const c = [...document.querySelectorAll('button, [role=button], a[href], summary, [tabindex]:not([tabindex="-1"])')].filter(vis).filter(el => !el.disabled && el.getAttribute('aria-disabled') !== 'true');
  return c.map((el, i) => { el.dataset.audit = i; const r = el.getBoundingClientRect();
    return [i, (el.id ? '#' + el.id + ' ' : '') + (el.getAttribute('aria-label') || el.textContent || el.title || '').replace(/\s+/g, ' ').trim().slice(0, 30), r.x + r.width / 2, r.y + r.height / 2, r.top < innerHeight && r.bottom > 0 && r.left < innerWidth && r.right > 0]; }); })()"""
SNAP_JS = r"""(() => { const m = {}; document.querySelectorAll('[data-audit]').forEach(el => { const r = el.getBoundingClientRect(); if (r.width) m[el.dataset.audit] = [r.x, r.y]; }); return m; })()"""
VLOG_JS = r"""(() => { const t = window.__tool; const v = t && (t.vlog || (t.V && t.V.log)); return v ? v.map(e => ({kind: e.kind, key: e.key, text: (e.text || '').slice(0, 70), as: e.as, why: e.why, n: e.n || 1})) : null; })()"""
AFTER_JS = r"""(i => { const el = document.querySelector(`[data-audit="${i}"]`); const a = document.activeElement;
  return {gone: !el, focus: a && a !== document.body ? (a.id || a.tagName.toLowerCase()) : 'body', hint: (document.getElementById('hint') || {}).textContent || ''}; })"""

HOST = """<!doctype html><meta charset=utf-8><style>body{margin:0;background:#888}iframe{border:0;display:block;background:#fff}</style>
<iframe src="tool.html" width="375" height="812"></iframe>"""


class Audit:
    def __init__(self, tool, out):
        self.tool, self.out = tool, out
        self.file = ROOT / 'tools' / tool / f'{tool}.html'
        meta = {}
        for f in ('tool.draft.json', 'tool.json'):
            p = ROOT / 'tools' / tool / f
            if p.exists():
                meta = json.loads(p.read_text(encoding='utf-8')); break
        g = meta.get('grades_label', '')
        nums = [int(n) for n in re.findall(r'\d+', g)]
        self.k2 = ('K' in g and not nums) or (bool(nums) and max(nums) <= 2) or 'K-' in g
        self.target = 60 if self.k2 else 44
        self.errors = []

    async def tab(self, w, h, calm=False, url=None):
        req = urllib.request.Request(f'http://127.0.0.1:{drive.PORT}/json/new?about:blank', method='PUT')
        info = json.loads(urllib.request.urlopen(req).read())
        ws = await websockets.connect(info['webSocketDebuggerUrl'], max_size=2**28)
        t = drive.Tab(ws); t.rd = asyncio.create_task(t.reader()); t.id = info['id']; t.wsock = ws
        for d in ('Page', 'Runtime', 'Log'):
            await t.send(d + '.enable')
        await t.send('Emulation.setDeviceMetricsOverride', width=w, height=h, deviceScaleFactor=1, mobile=False)
        await t.send('Page.addScriptToEvaluateOnNewDocument', source=f'try{{localStorage.clear();localStorage.setItem("curio-motion","{"calm" if calm else "on"}")}}catch(e){{}}')
        await t.send('Page.navigate', url=url or self.file.as_uri())
        await asyncio.sleep(1.5)
        return t

    async def ev(self, t, js, frame=None):
        p = dict(expression=js, returnByValue=True, awaitPromise=True)
        if frame is not None:
            p['contextId'] = frame
        r = await t.send('Runtime.evaluate', **p)
        if r.get('exceptionDetails'):
            return {'audit_error': json.dumps(r['exceptionDetails'])[:300]}
        return r.get('result', {}).get('value')

    def errs(self, t):
        e = []
        for m in t.events:
            if m.get('method') == 'Runtime.exceptionThrown':
                e.append('exception: ' + m['params']['exceptionDetails'].get('exception', {}).get('description', m['params']['exceptionDetails'].get('text', ''))[:200])
            elif m.get('method') == 'Runtime.consoleAPICalled' and m['params']['type'] in ('error', 'assert'):
                e.append('console: ' + ' '.join(str(a.get('value', a.get('description', ''))) for a in m['params']['args'])[:200])
            elif m.get('method') == 'Log.entryAdded' and m['params']['entry']['level'] == 'error' and 'favicon' not in m['params']['entry'].get('url', ''):
                e.append('log: ' + m['params']['entry'].get('text', '')[:200])
        return e

    async def close(self, t, name=None):
        if name:
            shot = await t.send('Page.captureScreenshot', format='png')
            (self.out / f'{name}.png').write_bytes(base64.b64decode(shot['data']))
        t.rd.cancel()
        await t.wsock.close()
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{drive.PORT}/json/close/{t.id}', timeout=3)
        except Exception:
            pass

    async def size(self, w, h, url=None, label=None):
        label = label or f'{w}x{h}'
        t = await self.tab(w, h, url=url)
        ctx = None
        if url:  # the tool runs in the iframe: find its execution context
            await asyncio.sleep(.5)
            main = (await t.send('Page.getFrameTree'))['frameTree']['frame']['id']
            cs = [m['params']['context'] for m in t.events if m.get('method') == 'Runtime.executionContextCreated']
            cs = [c for c in cs if c.get('auxData', {}).get('isDefault') and c.get('auxData', {}).get('frameId') != main]
            if not cs:
                r = {'audit_error': 'iframe context not found'}; await self.close(t); return label, r
            ctx = cs[-1]['id']
        r = await self.ev(t, PAGE_JS.replace('%K2%', 'true' if self.k2 else 'false'), ctx)
        r = r if isinstance(r, dict) else {'audit_error': str(r)}
        r['errors'] = self.errs(t)
        await self.close(t, f'size-{label}')
        return label, r

    async def calm(self):
        t = await self.tab(1366, 768, calm=True)
        await asyncio.sleep(1)
        r = await self.ev(t, CALM_JS)
        await self.close(t, 'calm-1366x768')
        return r or []

    async def press(self, t, x, y):
        await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y)
        await t.send('Input.dispatchMouseEvent', type='mousePressed', x=x, y=y, button='left', buttons=1, clickCount=1)
        await asyncio.sleep(.12)
        await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=x, y=y, button='left', clickCount=1)

    async def walk(self):
        t = await self.tab(1366, 768)
        ctls = await self.ev(t, TAG_JS) or []
        await self.close(t)
        rows, speakers = [], []
        for i, label, x, y, onscreen in ctls[:45]:
            if not onscreen:
                rows.append({'i': i, 'label': label, 'skip': 'off screen at load'}); continue
            t = await self.tab(1366, 768)
            await self.ev(t, TAG_JS)
            before = await self.ev(t, SNAP_JS) or {}
            n0 = len(await self.ev(t, VLOG_JS) or [])
            await self.press(t, x, y)
            await asyncio.sleep(2.5)
            after = await self.ev(t, f'({AFTER_JS})({i})') or {}
            now = await self.ev(t, SNAP_JS) or {}
            vlog = await self.ev(t, VLOG_JS)
            jumps = [k for k, p in now.items() if k in before and k != str(i) and max(abs(p[0] - before[k][0]), abs(p[1] - before[k][1])) > 12]
            spoke = [e for e in (vlog or [])[n0:] if e['as'] in ('spoken', 'read')]
            row = {'i': i, 'label': label, 'errors': self.errs(t), 'gone': after.get('gone'), 'focus': after.get('focus'),
                   'jumped': len(jumps), 'of': len(now), 'spoke': [e['text'] for e in spoke], 'hint': after.get('hint', '')[:100], 'voice': vlog is not None}
            rows.append(row)
            if spoke and not after.get('gone'):
                speakers.append((i, label, x, y))
            await self.close(t)
        reps = []
        for i, label, x, y in speakers[:10]:
            t = await self.tab(1366, 768)
            await self.ev(t, TAG_JS)
            await self.press(t, x, y)  # the first tap: let the welcome and its own line finish before counting
            for _ in range(30):
                await asyncio.sleep(.5)
                q = await self.ev(t, "(() => { const v = window.__tool && (window.__tool.V || null); const vq = window.__tool && window.__tool.vq; return !!((v && (v.playing || (v.queue || []).length)) || (vq && vq.length)); })()")
                if not q: break
            n0 = len(await self.ev(t, VLOG_JS) or [])
            for _ in range(5):
                await self.press(t, x, y)
                await asyncio.sleep(2)
            await asyncio.sleep(2)
            vlog = (await self.ev(t, VLOG_JS) or [])[n0:]
            cnt = {}
            for e in vlog:
                k = (e['kind'], e['text'])
                c = cnt.setdefault(k, {'spoken': 0, 'dropped': 0, 'silent': 0, 'why': set()})
                if e['as'] in c:
                    c[e['as']] += e['n']
                if e['as'] == 'dropped' and e.get('why'):
                    c['why'].add(e['why'])
            reps.append({'label': label, 'errors': self.errs(t),
                         'how_twice': [k[1] for k, c in cnt.items() if k[0] == 'how' and c['spoken'] > 1],
                         'event_lost': [f'{k[1]} (spoken {c["spoken"]} of 5, dropped {c["dropped"]}: {", ".join(sorted(c["why"])) or "?"})' for k, c in cnt.items() if k[0] not in ('how', 'welcome', 'read') and c['dropped'] and c['spoken'] < 5]})
            await self.close(t)
        return rows, reps


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(folder, port):
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), functools.partial(Quiet, directory=str(folder)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def report(a, sizes, calm, rows, reps):
    L = [f'# Audit: {a.tool}', '',
         f'Mechanical checks only (scripts/audit_tool.py). Each row is a lead to confirm on your own frames, not a verdict.',
         f'It does not judge teaching, giveaways, feel, art or the words of a line. Targets: ' + ('60 px full screen (1100 px wide and up), 44 px in the preview sizes and at 375 (K-2)' if a.k2 else '44 px') + '; the kit header buttons are 44 px everywhere.', '']
    flags = 0
    L += ['## Sizes', '']
    for label, r in sizes:
        items = []
        if r.get('audit_error'): items.append(f'audit could not read the page: {r["audit_error"]}')
        if r.get('hscroll'): items.append(f'sideways page scroll {r["hscroll"]} px')
        for k, what in (('small', 'small target'), ('below', 'control below the fold'), ('noname', 'control with no name'),
                        ('overlap', 'overlap'), ('clipped', 'clipped text'), ('tiny', 'text under 10 px')):
            for v in r.get(k, []):
                items.append(f'{what}: {v}')
        h = r.get('hint')
        if h is None: items.append('no #hint element (fine if the tool owns its hint: confirm Read speaks it)')
        elif not h['inView'] or h['cut']: items.append(f'hint {"out of view" if not h["inView"] else ""}{" and " if not h["inView"] and h["cut"] else ""}{"cut off" if h["cut"] else ""}: "{h["text"]}"')
        if r.get('focus'): items.append(f'focus taken on load: {r["focus"]}')
        for e in r.get('errors', []): items.append(f'error: {e}')
        flags += len(items)
        L.append(f'**{label}** ({r.get("count", "?")} controls): ' + ('clean' if not items else ''))
        L += [f'- {x}' for x in items]
        L.append('')
    L += ['## Motion off (1366x768)', '', ('- running forever: ' + ', '.join(calm)) if calm else 'clean: nothing runs forever', '']
    flags += len(calm)
    if rows is not None:
        L += ['## One held click per control (1366x768, fresh page each)', '',
              '| # | control | errors | after the click | others moved | spoken |', '|---|---|---|---|---|---|']
        for r in rows:
            if r.get('skip'):
                L.append(f'| {r["i"]} | {r["label"]} | | {r["skip"]} | | |'); continue
            after = 'rebuilt, focus lost' if r['gone'] and r['focus'] == 'body' else 'rebuilt, focus kept' if r['gone'] else ('focus lost' if r['focus'] == 'body' else 'ok')
            if after.endswith('lost'): flags += 1
            if r['errors']: flags += 1
            L.append(f'| {r["i"]} | {r["label"]} | {"; ".join(r["errors"])[:120]} | {after} | {r["jumped"]} of {r["of"]} | {" / ".join(r["spoke"])[:140] if r["voice"] else "(no __tool.vlog)"} |')
        L += ['', '"others moved" counts controls that shifted more than 12 px: expected on a mode change, a panel jump otherwise.', '']
        L += ["## Five held clicks, 2 s apart (controls that spoke; counted after the first tap's lines finish)", '']
        if not reps: L.append('none spoke on one click (or the tool has no __tool.vlog)')
        for r in reps:
            items = [f'how line spoken twice: {x}' for x in r['how_twice']] + [f'event line lost: {x}' for x in r['event_lost']] + [f'error: {e}' for e in r['errors']]
            flags += len(items)
            L.append(f'- **{r["label"]}**: ' + ('clean' if not items else '; '.join(items)))
        L.append('')
    L.insert(4, f'**{flags} leads.** Frames: size-*.png, calm-*.png in this folder.\n')
    return '\n'.join(L)


async def run(tool, out, walk):
    a = Audit(tool, out)
    if not a.file.exists():
        sys.exit(f'{a.file} not found: bundle first (CURIO_DRAFT=1 python scripts/bundle_tool.py {tool})')
    host = out / 'host'; host.mkdir(parents=True, exist_ok=True)
    (host / 'tool.html').write_bytes(a.file.read_bytes()); (host / 'host.html').write_text(HOST, encoding='utf-8')
    hp = drive.PORT + 1
    srv = serve(host, hp)
    drive.ensure_chrome(Path(drive.PROFILE).resolve() if drive.PROFILE else out.resolve() / 'chrome-prof')
    try:
        sizes = [await a.size(w, h) for w, h in SIZES]
        sizes.append(await a.size(395, 832, url=f'http://127.0.0.1:{hp}/host.html', label='375x812 (iframe host)'))
        calm = await a.calm()
        rows, reps = (await a.walk()) if walk else (None, None)
    finally:
        srv.shutdown()
    md = report(a, sizes, calm, rows, reps)
    (out / 'audit.md').write_text(md, encoding='utf-8')
    print(md.split('\n')[4] if len(md.split('\n')) > 4 else '', f'\nreport: {out / "audit.md"}')


if __name__ == '__main__':
    drive.PORT = int(drive.flag('--port') or drive.PORT)
    drive.PROFILE = drive.flag('--profile')
    walk = '--no-walk' not in sys.argv
    args = [x for x in sys.argv[1:] if x != '--no-walk']
    if len(args) != 2:
        sys.exit(__doc__)
    out = Path(args[1]); out.mkdir(parents=True, exist_ok=True)
    try:
        asyncio.run(run(args[0], out, walk))
    finally:
        drive.close_chrome()
