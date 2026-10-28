r"""Mechanical audit of a bundled tool: the checks every Refine lens used to repeat by hand, as one report.

    python scripts/audit_tool.py <tool-id> <outdir> [--port 9383] [--profile <absolute dir>] [--no-walk]
                                 [--states <file>] [--tool-file <bundled html>]

Bundle first (CURIO_DRAFT=1 python scripts/bundle_tool.py <id>). Writes <outdir>/audit.md and frames. Checks:
  sizes   every STANDARDS size, 375 through an iframe host served from <outdir> (the tool folder is not touched):
          sideways scroll, targets under 44 px (60 px for K-2), controls below the fold, controls with no name,
          overlapping controls and labels (text hidden under another box or a scroll edge is listed apart), clipped
          text, the hint in view and not clipped, the hint naming a disabled control, keep regions out of view,
          text under 10 px, focus taken on load, console errors
  states  the same checks at every size after each mode button (automatic) and after each state the builder lists
          in tools/<id>/audit-states.json, plus focus lost after any step's click (a control disabled under focus)
  calm    Motion off: animations still running forever
  walk    at 1366x768, a fresh page per control, one held click each: errors, focus lost or the control rebuilt
          under the pointer, other controls jumping, what was spoken, and whether the mode's welcome was heard
          after that first tap; then the controls that spoke get five held clicks 2 s apart (a how-to line spoken
          twice, an event line lost) and two quick taps 0.7 s apart (a line cut mid-speech that never came back)

audit-states.json (written by the builder; every step is real input, so states cost what a student would do):
  {"keep": ["#results"],                       regions that must be in view and uncovered in every state
   "states": [{"name": "after-run",            frames are state-<name>-<size>.png
               "steps": [{"click": "#run"}, {"click": "#skip"}, {"until": "__tool.state.done", "max": 30000}],
               "keep": ["#bars"], "sizes": ["680x425", "1366x768"]}]}      sizes: default every size and 375
  steps: {"click": sel, "times": n, "gap": s}  {"key": "Enter"}  {"js": "..."}  {"wait": ms}
         {"until": "js expression", "max": ms}  {"drag": "js returning [[x, y], ...]"}
  An element can also carry data-audit-keep to be a keep region everywhere.

Spoken-line cuts come from the kit's V.log (a spoken entry gets cut: hush, read, sound or now; kit/curio.js).
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
const out = {hscroll: Math.max(0, document.documentElement.scrollWidth - W), small: [], below: [], noname: [], overlap: [], hidden: [], clipped: [], tiny: [], focus: null, hint: null, keep: [], disabledNamed: [], count: ctl.length};
const inWin = (x, y) => x >= 0 && y >= 0 && x < W && y < H;
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
const hid = new Set();
// share of an element's box that its scrolling or clipping ancestors leave visible
const shown = (el, r) => { let L = r.left, T = r.top, R = r.right, B = r.bottom;
  for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
    const s = getComputedStyle(p); if (!/hidden|auto|scroll|clip/.test(s.overflowX + s.overflowY)) continue;
    const q = p.getBoundingClientRect(); L = Math.max(L, q.left); T = Math.max(T, q.top); R = Math.min(R, q.right); B = Math.min(B, q.bottom); }
  return Math.max(0, R - L) * Math.max(0, B - T) / Math.max(1, r.width * r.height); };
for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
  const a = boxes[i], b = boxes[j];
  if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
  const ix = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), iy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
  if (!(ix > 3 && iy > 3)) continue;
  const dlg = el => el.closest('[role=dialog], [aria-modal=true], dialog[open]');
  if (dlg(a.el) !== dlg(b.el)) continue;  // an open dialog covering the page is meant to
  for (const x of [a, b]) if (x.cut === undefined) x.cut = shown(x.el, x.r) < .5;
  if (a.cut || b.cut) {  // one of them is mostly past a scroll box's edge: not drawn there, so not an overlap
    for (const x of [a, b]) if (x.cut && !hid.has(x.el) && hid.size < 12) { hid.add(x.el); out.hidden.push(tag(x.el) + ' (cut by a scroll box)'); }
    continue;
  }
  // what is drawn at the middle of the overlap: one of the two is a real overlap; neither means both are hidden
  // (under another box or past a scroll box's edge), which is a different lead
  const cx = Math.max(a.r.left, b.r.left) + ix / 2, cy = Math.max(a.r.top, b.r.top) + iy / 2, e = inWin(cx, cy) ? document.elementFromPoint(cx, cy) : null;
  if (e && !a.el.contains(e) && !b.el.contains(e)) {
    for (const x of [a.el, b.el]) if (!hid.has(x) && hid.size < 12) { hid.add(x); out.hidden.push(tag(x) + (e ? ' under ' + tag(e) : '')); }
  } else if (out.overlap.length < 25) out.overlap.push(`${tag(a.el)} / ${tag(b.el)} ${Math.round(ix)}x${Math.round(iy)}`);
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
// keep regions: listed selectors and [data-audit-keep], fully in the window and drawn (not covered, not cut by a scroll box)
const keeps = [...%KEEP%.map(s => [s, document.querySelector(s)]), ...[...document.querySelectorAll('[data-audit-keep]')].map(el => [tag(el), el])];
for (const [s, el] of keeps) {
  if (!el) { out.keep.push(`${s}: not on the page`); continue; }
  if (!vis(el)) { out.keep.push(`${s}: hidden`); continue; }
  const r = el.getBoundingClientRect(), vw = Math.max(0, Math.min(r.right, W) - Math.max(r.left, 0)), vh = Math.max(0, Math.min(r.bottom, H) - Math.max(r.top, 0));
  const f = vw * vh / (r.width * r.height);
  let pts = 0, cov = 0;
  for (const fx of [.2, .5, .8]) for (const fy of [.2, .5, .8]) { const x = r.left + r.width * fx, y = r.top + r.height * fy; if (!inWin(x, y)) continue; pts++; const e = document.elementFromPoint(x, y); if (!e || !el.contains(e)) cov++; }
  if (f < .95 || cov) out.keep.push(`${s}: ${Math.round(f * 100)}% inside the window` + (cov ? `, ${cov} of ${pts} sample points covered or cut by a scroll box` : ''));
}
// the hint, or the line spoken last, naming a control that is disabled right now
const norm = s => (s || '').toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
const vl = window.__tool && (window.__tool.vlog || (window.__tool.V && window.__tool.V.log));
const last = vl ? vl.filter(e => e.as === 'spoken').slice(-1)[0] : null;
const said = [['hint', norm(h && h.textContent)], ['last line', norm(last && last.text)]];
for (const el of document.querySelectorAll('button, [role=button]')) {
  if (!vis(el) || !(el.disabled || el.getAttribute('aria-disabled') === 'true')) continue;
  for (const n of new Set([norm(el.textContent), norm(el.getAttribute('aria-label'))])) {
    if (n.length < 6 || !n.includes(' ') && n.length < 8) continue;
    const who = said.filter(([w, t]) => t && (' ' + t + ' ').includes(' ' + n + ' ')).map(([w]) => w);
    if (who.length) out.disabledNamed.push(`${who.join(' and ')} name${who.length > 1 ? '' : 's'} "${n}" (${el.id ? '#' + el.id : 'button'}), which is disabled`);
  }
}
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
VLOG_JS = r"""(() => { const t = window.__tool; const v = t && (t.vlog || (t.V && t.V.log)); return v ? v.map(e => ({kind: e.kind, key: e.key, text: (e.text || '').slice(0, 70), as: e.as, why: e.why, n: e.n || 1, t: e.t, cut: e.cut || null})) : null; })()"""
# the narration is quiet: nothing queued and the last line has had its longest time (the kit's cap) to finish
IDLE_JS = r"""(() => { const t = window.__tool, v = t && (t.vlog || (t.V && t.V.log)), q = t && (t.vq || (t.V && t.V.queue)) || [];
  if (!v) return true; if (t.V && t.V.playing) return false; if (q.length) return false;
  const s = v.filter(e => e.as === 'spoken' || e.as === 'read').slice(-1)[0];
  return !s || s.cut || performance.now() - s.t > 2500 + 80 * (s.text || '').length; })()"""
CLICK_JS = r"""(s => { const el = document.querySelector(s); if (!el) return null; el.scrollIntoView({block: 'nearest', inline: 'nearest'});
  const r = el.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })"""
FOCUS_JS = r"""(() => { const a = document.activeElement; return !a || a === document.body || a === document.documentElement ? 'body' : (a.id ? '#' + a.id : a.tagName.toLowerCase()); })()"""
MODES_JS = r"""(() => [...document.querySelectorAll('header .seg button, header [role=group] button, header [role=tablist] [role=tab]')].filter(b => b.id)
  .map(b => [b.id, (b.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 30), b.getAttribute('aria-pressed') === 'true' || b.getAttribute('aria-selected') === 'true']))()"""
KIT_IDS = {'motion', 'sound', 'read'}
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
        self.modes = []  # [[id, label, pressed]] from the header's mode buttons

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

    async def size(self, w, h, url=None, label=None, steps=(), keep=(), shot=None):
        """Load the tool at a size, run a state's steps (real input), then the page checks. Returns (label, result)."""
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
        lost, missing = await self.steps(t, ctx, steps)
        r = await self.ev(t, PAGE_JS.replace('%K2%', 'true' if self.k2 else 'false').replace('%KEEP%', json.dumps(list(keep))), ctx)
        r = r if isinstance(r, dict) else {'audit_error': str(r)}
        r['errors'] = self.errs(t)
        r['focus_lost'], r['missing'] = lost, missing
        await self.close(t, shot or f'size-{label}')
        return label, r

    async def steps(self, t, ctx, steps):
        """Run a state's steps with real input (the iframe host sits at 0,0, so frame points are page points).
        Returns (clicks after which focus fell to the page, selectors not found)."""
        lost, missing = [], []
        for s in steps:
            if 'click' in s:
                for n in range(s.get('times', 1)):
                    p = await self.ev(t, f'({CLICK_JS})({json.dumps(s["click"])})', ctx)
                    if not p:
                        missing.append(s['click']); break
                    await self.press(t, *p)
                    await asyncio.sleep(s.get('gap', .4))
                    if await self.ev(t, FOCUS_JS, ctx) == 'body':
                        lost.append(f'{s["click"]} (click {n + 1})')
            elif 'key' in s:
                kk = s['key']; code, cname, text = drive_keys()[kk]
                await t.send('Input.dispatchKeyEvent', type='keyDown' if text else 'rawKeyDown', key=kk, code=cname, windowsVirtualKeyCode=code, **({'text': text} if text else {}))
                await t.send('Input.dispatchKeyEvent', type='keyUp', key=kk, code=cname, windowsVirtualKeyCode=code)
                await asyncio.sleep(.15)
            elif 'js' in s:
                await self.ev(t, f'(async () => {{ {s["js"]} }})()', ctx)
            elif 'until' in s:
                for _ in range(int(s.get('max', 10000) / 250)):
                    if await self.ev(t, f'!!({s["until"]})', ctx) is True:
                        break
                    await asyncio.sleep(.25)
            elif 'drag' in s:
                pts = await self.ev(t, f'(() => {{ {s["drag"]} }})()', ctx) or []
                if pts:
                    x, y = pts[0]
                    await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y)
                    await t.send('Input.dispatchMouseEvent', type='mousePressed', x=x, y=y, button='left', buttons=1, clickCount=1)
                    for x, y in pts[1:]:
                        await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y, button='left', buttons=1)
                        await asyncio.sleep(.02)
                    await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=x, y=y, button='left', clickCount=1)
            if 'wait' in s:
                await asyncio.sleep(s['wait'] / 1000)
        await asyncio.sleep(.4)
        return lost, missing

    async def quiet(self, t, most=15):
        """Wait until nothing is queued and the last line has had its time (at most `most` seconds)."""
        for _ in range(int(most * 2)):
            if await self.ev(t, IDLE_JS):
                return
            await asyncio.sleep(.5)

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
            # the welcome after this first tap: wait for the narration to finish, then look for a welcome spoken whole
            await self.quiet(t)
            full = await self.ev(t, VLOG_JS) or []
            wl = [e for e in full if e['kind'] == 'welcome' and e['as'] == 'spoken']
            welcome = 'heard' if any(not e['cut'] for e in wl) else f'cut ({wl[0]["cut"]})' if wl else 'not heard'
            row = {'i': i, 'label': label, 'errors': self.errs(t), 'gone': after.get('gone'), 'focus': after.get('focus'),
                   'jumped': len(jumps), 'of': len(now), 'spoke': [e['text'] for e in spoke], 'hint': after.get('hint', '')[:100], 'voice': vlog is not None,
                   'welcome': welcome, 'id': label.split(' ')[0][1:] if label.startswith('#') else ''}
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
        # two quick taps on the same control (a line is playing when the second lands): a line cut mid-speech by the
        # tool (hush or now, not Read or Sound) that never plays whole afterwards is lost
        modes = {m[0] for m in self.modes}
        quick, seen = [], set()
        for i, label, x, y in speakers[:10] + [(r['i'], r['label'], None, None) for r in rows if r.get('id') in modes]:
            if i in seen:
                continue
            seen.add(i)
            t = await self.tab(1366, 768)
            pts = {c[0]: (c[2], c[3]) for c in (await self.ev(t, TAG_JS) or [])}
            if i not in pts:
                await self.close(t); continue
            await self.press(t, *pts[i])
            await asyncio.sleep(.7)
            await self.press(t, *pts[i])
            await self.quiet(t)
            vlog = await self.ev(t, VLOG_JS) or []
            lost = []
            for j, e in enumerate(vlog):
                if e['as'] == 'spoken' and e['cut'] in ('hush', 'now') and not any(f['as'] == 'spoken' and not f['cut'] and f['key'] == e['key'] for f in vlog[j + 1:]):
                    lost.append(f'{e["kind"]} line cut ({e["cut"]}) and never heard whole: {e["text"]}')
            quick.append({'label': label, 'lost': lost, 'errors': self.errs(t)})
            await self.close(t)
        return rows, reps, quick


def drive_keys():
    return {'Tab': (9, 'Tab', None), 'Enter': (13, 'Enter', '\r'), 'Escape': (27, 'Escape', None), ' ': (32, 'Space', ' '),
            'ArrowRight': (39, 'ArrowRight', None), 'ArrowLeft': (37, 'ArrowLeft', None), 'ArrowUp': (38, 'ArrowUp', None), 'ArrowDown': (40, 'ArrowDown', None)}


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(folder, port):
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), functools.partial(Quiet, directory=str(folder)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def size_items(r, onload=True):
    items = []
    if r.get('audit_error'): items.append(f'audit could not read the page: {r["audit_error"]}')
    for s in r.get('missing', []): items.append(f'state step: {s} not found (the state did not run as written)')
    for s in r.get('focus_lost', []): items.append(f'focus fell to the page after clicking {s}')
    if r.get('hscroll'): items.append(f'sideways page scroll {r["hscroll"]} px')
    for k, what in (('small', 'small target'), ('below', 'control below the fold'), ('noname', 'control with no name'),
                    ('overlap', 'overlap'), ('hidden', 'text hidden under another box or a scroll edge'), ('clipped', 'clipped text'),
                    ('tiny', 'text under 10 px'), ('keep', 'keep region'), ('disabledNamed', 'names a disabled control')):
        for v in r.get(k, []):
            items.append(f'{what}: {v}')
    h = r.get('hint')
    if h is None: items.append('no #hint element (fine if the tool owns its hint: confirm Read speaks it)')
    elif not h['inView'] or h['cut']: items.append(f'hint {"out of view" if not h["inView"] else ""}{" and " if not h["inView"] and h["cut"] else ""}{"cut off" if h["cut"] else ""}: "{h["text"]}"')
    if onload and r.get('focus'): items.append(f'focus taken on load: {r["focus"]}')
    for e in r.get('errors', []): items.append(f'error: {e}')
    return items


def report(a, sizes, calm, rows, reps, quick, states):
    L = [f'# Audit: {a.tool}', '',
         f'Mechanical checks only (scripts/audit_tool.py). Each row is a lead to confirm on your own frames, not a verdict.',
         f'It does not judge teaching, giveaways, feel, art or the words of a line. Targets: ' + ('60 px full screen (1100 px wide and up), 44 px in the preview sizes and at 375 (K-2)' if a.k2 else '44 px') + '; the kit header buttons are 44 px everywhere.', '']
    flags = 0
    L += ['## Sizes', '']
    for label, r in sizes:
        items = size_items(r)
        flags += len(items)
        L.append(f'**{label}** ({r.get("count", "?")} controls): ' + ('clean' if not items else ''))
        L += [f'- {x}' for x in items]
        L.append('')
    L += ['## States (every mode button, then audit-states.json; frames state-<name>-<size>.png)', '']
    if not states: L.append('none: one mode and no tools/<id>/audit-states.json (the builder lists the states a student reaches)')
    # a state lists only what is new against the first screen at the same size, and one lead per finding with its sizes
    base = {label: set(size_items(r)) for label, r in sizes}
    for name, how, res in states:
        by = {}
        for label, r in res:
            for x in size_items(r, onload=False):
                if x not in base.get(label, ()):
                    by.setdefault(x, []).append(label.split(' ')[0])
        flags += len(by)
        L.append(f'**{name}** ({how}): ' + ('nothing new at any size' if not by else ''))
        L += [f'- {x} [{", ".join(s) if len(s) < len(res) else "every size"}]' for x, s in by.items()]
        L.append('')
    L += ['## Motion off (1366x768)', '', ('- running forever: ' + ', '.join(calm)) if calm else 'clean: nothing runs forever', '']
    flags += len(calm)
    if rows is not None:
        L += ['## One held click per control (1366x768, fresh page each)', '',
              '| # | control | errors | after the click | others moved | spoken | welcome after this first tap |', '|---|---|---|---|---|---|---|']
        # a tool with no welcome at all is not flagged for each control; Read and Sound skip the welcome by design
        has_welcome = any(r.get('welcome', '').startswith(('heard', 'cut')) for r in rows)
        lost_welcome = []
        for r in rows:
            if r.get('skip'):
                L.append(f'| {r["i"]} | {r["label"]} | | {r["skip"]} | | | |'); continue
            after = 'rebuilt, focus lost' if r['gone'] and r['focus'] == 'body' else 'rebuilt, focus kept' if r['gone'] else ('focus lost' if r['focus'] == 'body' else 'ok')
            if after.endswith('lost'): flags += 1
            if r['errors']: flags += 1
            w = r.get('welcome', '')
            if has_welcome and w != 'heard' and r['id'] not in ('read', 'sound'):
                flags += 1; lost_welcome.append(r['label']); w = '**' + w + '**'
            L.append(f'| {r["i"]} | {r["label"]} | {"; ".join(r["errors"])[:120]} | {after} | {r["jumped"]} of {r["of"]} | {" / ".join(r["spoke"])[:140] if r["voice"] else "(no __tool.vlog)"} | {w} |')
        L += ['', '"others moved" counts controls that shifted more than 12 px: expected on a mode change, a panel jump otherwise.']
        if lost_welcome:
            L += [f'Welcome not heard whole after a first tap on: {", ".join(lost_welcome)}. A student who starts there never hears the',
                  'premise (unless the tool brings it back later): a lead for welcomeAfter or for the welcome waiting on that tap\'s own line.']
        L.append('')
        L += ["## Five held clicks, 2 s apart (controls that spoke; counted after the first tap's lines finish)", '']
        if not reps: L.append('none spoke on one click (or the tool has no __tool.vlog)')
        for r in reps:
            items = [f'how line spoken twice: {x}' for x in r['how_twice']] + [f'event line lost: {x}' for x in r['event_lost']] + [f'error: {e}' for e in r['errors']]
            flags += len(items)
            L.append(f'- **{r["label"]}**: ' + ('clean' if not items else '; '.join(items)))
        L.append('')
        L += ['## Two quick taps, 0.7 s apart (controls that spoke, and the mode buttons)', '']
        if not quick: L.append('none')
        for r in quick:
            items = r['lost'] + [f'error: {e}' for e in r['errors']]
            flags += len(items)
            L.append(f'- **{r["label"]}**: ' + ('clean' if not items else '; '.join(items)))
        L.append('')
    L.insert(4, f'**{flags} leads.** Frames: size-*.png, state-*.png, calm-*.png in this folder.\n')
    return '\n'.join(L)


async def run(tool, out, walk, states_file=None, tool_file=None):
    a = Audit(tool, out)
    if tool_file:
        a.file = Path(tool_file).resolve()
    if not a.file.exists():
        sys.exit(f'{a.file} not found: bundle first (CURIO_DRAFT=1 python scripts/bundle_tool.py {tool})')
    sf = Path(states_file) if states_file else ROOT / 'tools' / tool / 'audit-states.json'
    spec = json.loads(sf.read_text(encoding='utf-8')) if sf.exists() else {}
    keep = spec.get('keep', [])
    host = out / 'host'; host.mkdir(parents=True, exist_ok=True)
    (host / 'tool.html').write_bytes(a.file.read_bytes()); (host / 'host.html').write_text(HOST, encoding='utf-8')
    hp = drive.PORT + 1
    srv = serve(host, hp)
    drive.ensure_chrome(Path(drive.PROFILE).resolve() if drive.PROFILE else out.resolve() / 'chrome-prof')
    hosturl = f'http://127.0.0.1:{hp}/host.html'
    every = [(w, h, None, f'{w}x{h}') for w, h in SIZES] + [(395, 832, hosturl, '375x812 (iframe host)')]
    try:
        sizes = [await a.size(w, h, url=u, label=lb, keep=keep) for w, h, u, lb in every]
        t = await a.tab(1366, 768)
        a.modes = await a.ev(t, MODES_JS) or []
        await a.close(t)
        plan = [(f'mode {lab or mid}', f'click #{mid}', [{'click': '#' + mid}], keep, None) for mid, lab, pressed in a.modes if not pressed]
        plan += [(s['name'], 'audit-states.json', s.get('steps', []), keep + s.get('keep', []), s.get('sizes')) for s in spec.get('states', [])]
        states = []
        for name, how, steps, kp, only in plan:
            slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
            res = [await a.size(w, h, url=u, label=lb, steps=steps, keep=kp, shot=f'state-{slug}-{lb.split(" ")[0]}')
                   for w, h, u, lb in every if not only or lb.split(' ')[0] in only]
            states.append((name, how, res))
        calm = await a.calm()
        rows, reps, quick = (await a.walk()) if walk else (None, None, None)
    finally:
        srv.shutdown()
    md = report(a, sizes, calm, rows, reps, quick, states)
    (out / 'audit.md').write_text(md, encoding='utf-8')
    print(md.split('\n')[4] if len(md.split('\n')) > 4 else '', f'\nreport: {out / "audit.md"}')


if __name__ == '__main__':
    drive.PORT = int(drive.flag('--port') or drive.PORT)
    drive.PROFILE = drive.flag('--profile')
    states_file, tool_file = drive.flag('--states'), drive.flag('--tool-file')
    walk = '--no-walk' not in sys.argv
    args = [x for x in sys.argv[1:] if x != '--no-walk']
    if len(args) != 2:
        sys.exit(__doc__)
    out = Path(args[1]); out.mkdir(parents=True, exist_ok=True)
    try:
        asyncio.run(run(args[0], out, walk, states_file, tool_file))
    finally:
        drive.close_chrome()
