r"""One evidence pack for a tool's Refine round: the counting checks done by script, contact sheets, every string,
and an outline of src.html (docs/agents/TOKEN-PLAN.md, changes 2 to 4).

    python scripts/refine_pack.py <tool-id> <outdir> --port <n> --profile <absolute dir>
                                  [--audit <dir>] [--no-bundle] [--no-voice] [--no-states]
                                  [--max-controls 24] [--budget-min 25] [--jobs 4]

Writes into <outdir> (keep it outside the repo):
  checks.md      every mechanical check as PASS, FAIL, LEAD or AGENT (the script could not do it), with the evidence:
                 the REFINE.md standard voice check with its counts table, lines against voice/lines.json and
                 allLines(), art tokens against prompts.json, people flags, bundle size, network requests, console
                 errors, em dashes, "Curio" alone, kit use
  sheet-*.jpg    contact sheets (labeled grids) of the default screen, every mode, the narrow window, 1366x768, the
                 builder's states and the 680x425 preview
  strings.md     every on-screen string and every spoken line, by mode or source, with src.html line numbers
  outline.md     src.html as blocks, elements, sections, data tables and functions with line ranges
  README.md      what is here and how a lens, the Exit check and the Finish check use it
  voice-logs.json, frames/   the raw logs and frames behind the voice check

--audit <dir>  the shared audit folder (scripts/audit_tool.py output): its frames are reused for the sheets and its
               audit.md is cited. Without it this script runs the audit's sizes and states part itself (no walk) into
               <outdir>/audit-nowalk, on --port and the next port.
The tool is bundled first (CURIO_DRAFT=1 for a draft) unless --no-bundle. Chrome is driven through scripts/drive.py
and scripts/audit_tool.py (muted, headless, held clicks); only the Chrome this script starts is closed.
--jobs: how many pages the repeat runs and the state runs use at once (the timing checks always run one at a time).
A PASS means the script really ran that test on what it names. Anything it could not test is AGENT, never PASS.
"""
import asyncio, base64, json, os, re, sys, time, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import drive  # noqa: E402
import audit_tool  # noqa: E402  (Audit: tab, held press, keys, state steps; MODES_JS, CLICK_JS)
import bundle_tool  # noqa: E402
import refine_pack_lib as lib  # noqa: E402
from check_safety import scan as safety_scan  # noqa: E402
from voice import clip_name  # noqa: E402
try:
    import websockets
except ImportError:
    import cdp_ws as websockets

ROOT = Path(__file__).resolve().parent.parent
GOAL, REASON = 2 * 1024 * 1024, 6 * 1024 * 1024  # as scripts/check_tools.py
EM = chr(0x2014)

# runs before the page's own scripts: counts the clips and browser-voice utterances that really start and end
HOOK_JS = r"""(() => { try { localStorage.clear(); localStorage.setItem('curio-motion', 'on'); } catch (e) {}
  const P = window.__pack = {plays: [], active: 0};
  const track = (rec) => { rec.t = Math.round(performance.now()); rec.on = true; P.plays.push(rec); P.active++;
    return how => { if (rec.on) { rec.on = false; P.active--; rec.end = Math.round(performance.now()); rec.how = how; } }; };
  const A = window.Audio;
  if (A) { window.Audio = function (src) { const a = new A(src); let off = null;
      a.addEventListener('play', () => { if (!off) off = track({kind: 'clip'}); });
      a.addEventListener('ended', () => { if (off) off('ended'); });
      a.addEventListener('pause', () => { if (off) off(a.ended || (a.duration && a.currentTime >= a.duration - .08) ? 'ended' : 'cut'); });
      a.addEventListener('error', () => { if (off) off('error'); });
      return a; }; window.Audio.prototype = A.prototype; }
  if (window.speechSynthesis) { const ss = speechSynthesis, sp = ss.speak.bind(ss);
    ss.speak = u => { const off = track({kind: 'tts', text: (u.text || '').slice(0, 200)});
      setTimeout(() => off('cap'), 2500 + 80 * (u.text || '').length);   // headless Chrome often never ends an utterance: the kit's own cap
      u.addEventListener('end', () => off('ended')); u.addEventListener('error', e => off(e.error === 'interrupted' || e.error === 'canceled' ? 'cut' : 'error'));
      return sp(u); }; }
})()"""
VIS = r"""const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05 && !el.closest('[hidden],[aria-hidden="true"],[inert]'); };"""
TAG_JS = r"""(() => { %VIS%
  const c = [...document.querySelectorAll('button, [role=button], a[href], summary, [tabindex]:not([tabindex="-1"])')].filter(vis);
  const par = new Map();
  return c.map((el, i) => { el.dataset.pack = i; const r = el.getBoundingClientRect(), x = r.x + r.width / 2, y = r.y + r.height / 2;
    const on = r.top < innerHeight && r.bottom > 0 && r.left < innerWidth && r.right > 0;
    const e = on && x >= 0 && y >= 0 && x < innerWidth && y < innerHeight ? document.elementFromPoint(x, y) : null;
    const p = el.parentElement; if (p && !par.has(p)) par.set(p, par.size);
    const cls = (el.getAttribute('class') || '').split(/\s+/).filter(k => k && !/^(on|off|active|selected|sel|pressed|current|done|ok|bad|right|wrong|picked|chosen)$/.test(k)).sort().join('.');
    return {i, id: el.id || '', label: (el.getAttribute('aria-label') || el.textContent || el.title || '').replace(/\s+/g, ' ').trim().slice(0, 40), x, y, onscreen: on,
      hit: !!e && (el.contains(e) || e.contains(el)), disabled: !!el.disabled || el.getAttribute('aria-disabled') === 'true', header: !!el.closest('header'),
      group: (p ? par.get(p) : -1) + '|' + el.tagName + '|' + cls}; }); })()""".replace('%VIS%', VIS)
LOCATE_JS = r"""(i => { const el = document.querySelector(`[data-pack="${i}"]`); if (!el) return {why: 'gone (rebuilt or removed)'};
  if (el.disabled || el.getAttribute('aria-disabled') === 'true') return {why: 'disabled'};
  el.scrollIntoView({block: 'nearest', inline: 'nearest'}); const r = el.getBoundingClientRect(), s = getComputedStyle(el);
  if (!r.width || !r.height || s.visibility === 'hidden' || s.display === 'none' || el.closest('[hidden],[inert]')) return {why: 'hidden'};
  const x = r.x + r.width / 2, y = r.y + r.height / 2, e = document.elementFromPoint(x, y);
  if (!e || !(el.contains(e) || e.contains(el))) return {why: 'covered'};
  return {x, y}; })"""
VLOG_JS = r"""(() => { const t = window.__tool; const v = t && (t.vlog || (t.V && t.V.log)); return Array.isArray(v) ? v.map(e => ({kind: e.kind || '', key: String(e.key == null ? '' : e.key), text: e.text || '', as: e.as || '', why: e.why || '', n: e.n || 1, t: e.t || 0, cut: e.cut || null})) : null; })()"""
STATE_JS = r"""(() => { const t = window.__tool || {}, v = t.vlog || (t.V && t.V.log) || [], q = t.vq || (t.V && t.V.queue) || [], P = window.__pack || {plays: [], active: 0};
  const ss = window.speechSynthesis; let anim = 0;
  try { anim = document.getAnimations().filter(a => a.playState === 'running' && a.effect && a.effect.getTiming().iterations !== Infinity).length; } catch (e) {}
  const s = document.getElementById('sound'), h = document.getElementById('hint');
  return {now: performance.now(), n: v.length, q: q.length, active: P.active, plays: P.plays.length, speaking: !!(ss && (ss.speaking || ss.pending)),
    busy: !!(t.state && (t.state.busy || t.state.running || t.state.playing)), anim, sound: s ? s.getAttribute('aria-pressed') : null, hint: h ? h.textContent.trim() : null}; })()"""
PLAYS_JS = '(() => (window.__pack || {plays: []}).plays.map(p => ({kind: p.kind, t: p.t, end: p.end || null, how: p.how || null, text: p.text || ""})))()'
STAGE_JS = r"""(() => { const ctl = 'button,[role=button],a[href],input,select,textarea,summary,label,[tabindex]:not([tabindex="-1"]),[onclick]';
  const pick = root => { if (!root) return null; const r = root.getBoundingClientRect();
    for (const fy of [.5, .3, .7, .15, .85]) for (const fx of [.5, .3, .7, .15, .85]) { const x = r.x + r.width * fx, y = r.y + r.height * fy;
      if (x < 1 || y < 1 || x >= innerWidth - 1 || y >= innerHeight - 1) continue; const e = document.elementFromPoint(x, y);
      if (e && root.contains(e) && !e.closest(ctl)) return [x, y, root.id ? '#' + root.id : root.tagName.toLowerCase() + (root.className && root.className.baseVal === undefined ? '.' + String(root.className).split(' ')[0] : '')]; }
    return null; };
  return pick(document.querySelector('.stage')) || pick(document.querySelector('#stage')) || pick(document.querySelector('main')) || pick(document.querySelector('header h1')); })()"""
STR_JS = r"""(() => { %VIS% const out = [], seen = new Set();
  const where = el => { const p = el.closest('[id]'); return p ? '#' + p.id : el.tagName.toLowerCase(); };
  const add = (kind, s, el) => { s = (s || '').replace(/\s+/g, ' ').trim(); if (!s || !/[A-Za-z0-9]/.test(s)) return; const k = kind + '|' + s; if (seen.has(k)) return; seen.add(k); out.push([kind, s.slice(0, 400), where(el)]); };
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) { const n = w.currentNode, el = n.parentElement; if (!el || el.closest('script,style,title,desc') || !vis(el)) continue; add('text', n.nodeValue, el); }
  document.querySelectorAll('[aria-label],[title],[placeholder],img[alt]').forEach(el => { if (!vis(el)) return; for (const a of ['aria-label', 'title', 'placeholder', 'alt']) if (el.getAttribute(a)) add(a, el.getAttribute(a), el); });
  return out; })()""".replace('%VIS%', VIS)
RESET_RX = re.compile(r'reset|clear|restart|start over|new game|play again|again', re.I)
HOWISH = re.compile(r"^(now,? |then,? |next,? )?(tap|press|pick|choose|drag|click|move|use|select|type|draw|slide|set|turn|try (tapping|pressing))\b", re.I)
RESULTISH = re.compile(r"^(yes|correct|great|nice|well done|you (did|got|found|fixed|won)|that'?s (it|right|correct)|not quite|oops|good job|right!|wrong)", re.I)


def md_cell(s):
    return str(s).replace('|', '/').replace('\n', ' ')


class Checks:
    def __init__(self):
        self.sections = []

    def section(self, title):
        self.sections.append((title, []))

    def add(self, status, title, *evidence):
        self.sections[-1][1].append((status, title, [e for e in evidence if e]))

    def count(self, status):
        return sum(1 for _, items in self.sections for s, _, _ in items if s == status)

    def render(self):
        out = []
        for title, items in self.sections:
            out += ['', f'## {title}', '']
            for status, t, ev in items:
                out.append(f'- **{status}** {t}')
                for e in ev:
                    out += ['  ' + ln for ln in str(e).split('\n')]
        return '\n'.join(out)


class Pack(audit_tool.Audit):
    def __init__(self, tool, out):
        super().__init__(tool, out)
        self.runs, self.tabs_opened, self.tab_errors, self.requests = [], 0, [], []

    async def tab(self, w=1366, h=768, calm=False, url=None):
        req = urllib.request.Request(f'http://127.0.0.1:{drive.PORT}/json/new?about:blank', method='PUT')
        info = json.loads(urllib.request.urlopen(req).read())
        ws = await websockets.connect(info['webSocketDebuggerUrl'], max_size=2**28)
        t = drive.Tab(ws); t.rd = asyncio.create_task(t.reader()); t.id = info['id']; t.wsock = ws
        for d in ('Page', 'Runtime', 'Log', 'Network'):
            await t.send(d + '.enable')
        await t.send('Emulation.setDeviceMetricsOverride', width=w, height=h, deviceScaleFactor=1, mobile=False)
        await t.send('Page.addScriptToEvaluateOnNewDocument', source=HOOK_JS + (';try{localStorage.setItem("curio-motion","calm")}catch(e){}' if calm else ''))
        await t.send('Page.navigate', url=url or self.file.as_uri())
        await asyncio.sleep(1.5)
        self.tabs_opened += 1
        return t

    async def done(self, t, name, shot=None):
        """Close a tab, keeping its errors and any request that left the file."""
        for e in self.errs(t):
            self.tab_errors.append((name, e))
        for m in t.events:
            if m.get('method') == 'Network.requestWillBeSent':
                u = m['params']['request']['url']
                if not re.match(r'(file|data|blob|about|chrome|devtools):', u):
                    self.requests.append((name, u[:200]))
        if shot:
            png = await t.send('Page.captureScreenshot', format='png')
            (self.out / 'frames').mkdir(exist_ok=True)
            (self.out / 'frames' / f'{shot}.png').write_bytes(base64.b64decode(png['data']))
        await self.close(t)

    async def st(self, t):
        return await self.ev(t, STATE_JS) or {}

    async def idle(self, t, least=.7, most=14):
        """Wait until nothing is playing, queued or moving and the log has stopped growing. Returns seconds waited."""
        t0 = time.time(); await asyncio.sleep(least)
        last, calm = None, 0
        while time.time() - t0 < most:
            s = await self.st(t)
            waited = time.time() - t0
            quiet = not s.get('active') and not s.get('q') and not s.get('speaking') and not s.get('busy') and (not s.get('anim') or waited > 6)
            if quiet and last == (s.get('n'), s.get('plays')):
                calm += 1
                if calm >= 2: break
            else:
                calm = 0
            last = (s.get('n'), s.get('plays'))
            await asyncio.sleep(.25)
        return round(time.time() - t0, 1)

    async def tap(self, t, x, y):
        now = await self.ev(t, 'performance.now()')
        await self.press(t, x, y)
        return now

    async def tap_sel(self, t, sel):
        p = await self.ev(t, f'({audit_tool.CLICK_JS})({json.dumps(sel)})')
        return await self.tap(t, *p) if p else None

    async def fresh(self, mode=None):
        """A fresh 1366x768 page; with a mode id, switched there with one held click and left to go quiet."""
        t = await self.tab()
        if mode:
            await self.tap_sel(t, '#' + mode)
            await self.idle(t)
        return t

    async def log(self, t):
        return await self.ev(t, VLOG_JS)

    def keep(self, name, mode, taps, log, plays, **more):
        r = {'name': name, 'mode': mode, 'taps': taps, 'log': log or [], 'plays': plays or [], **more}
        self.runs.append(r)
        return r

    # ---------- the voice runs ----------

    async def profile(self):
        t = await self.tab()
        await asyncio.sleep(1.5)
        s = await self.st(t)
        v = await self.log(t)
        info = {'has_log': v is not None, 'early_spoken': [e for e in (v or []) if e['as'] in ('spoken', 'read')], 'early_plays': s.get('plays', 0),
                'sound': s.get('sound'), 'hint': s.get('hint'),
                'kit_buttons': await self.ev(t, "['motion','sound','read'].filter(i => document.getElementById(i))"),
                'all_lines': await self.ev(t, "(() => { try { return window.__tool && window.__tool.allLines ? window.__tool.allLines() : null; } catch (e) { return 'ERR ' + e; } })()"),
                'has_tool': await self.ev(t, '!!window.__tool')}
        self.modes = await self.ev(t, audit_tool.MODES_JS) or []
        info['strings'] = {'(first screen)': await self.ev(t, STR_JS) or []}
        await self.done(t, 'load, no input')
        for mid, lab, pressed in self.modes:
            if pressed: continue
            t = await self.fresh(mid)
            info['strings'][lab or mid] = await self.ev(t, STR_JS) or []
            await self.done(t, f'mode {lab or mid}')
        return info

    async def controls(self, mode):
        t = await self.fresh(mode)
        c = await self.ev(t, TAG_JS) or []
        await self.done(t, f'list controls ({mode or "first mode"})')
        return c

    async def repeat(self, mode, c, slow=False):
        """A fresh page, then five held clicks on one control, each after the page has gone quiet."""
        t = await self.fresh(mode)
        await self.ev(t, TAG_JS)
        n0 = len(await self.log(t) or [])
        taps, stop = [], ''
        for k in range(5):
            p = await self.ev(t, f'({LOCATE_JS})({c["i"]})') or {'why': 'gone'}
            if 'x' not in p:
                stop = f'{p["why"]} after {k} click{"" if k == 1 else "s"}'; break
            taps.append(await self.tap(t, p['x'], p['y']))
            await self.idle(t, least=6 if slow else .7)
            if k == 1 and len(await self.log(t) or []) == n0:
                stop = 'no line queued in two clicks'; break
        log = (await self.log(t) or [])[n0:]
        r = self.keep(f'repeat {c["label"] or c["id"]}', mode, taps, log, await self.ev(t, PLAYS_JS), control=c, stop=stop, slow=slow, kind='repeat')
        await self.done(t, r['name'])
        return r

    async def fast(self, mode, picks, gap, name, then_mode=None):
        """A fresh page; tap the picked controls `gap` seconds apart, then (stale run) another mode and its Reset."""
        t = await self.fresh(mode)
        await self.ev(t, TAG_JS)
        n0 = len(await self.log(t) or [])
        taps, acts = [], []
        for c in picks:
            p = await self.ev(t, f'({LOCATE_JS})({c["i"]})') or {}
            if 'x' in p:
                taps.append(await self.tap(t, p['x'], p['y'])); acts.append(c['label'] or c['id'])
                await asyncio.sleep(gap)
        switch = reset = None
        if then_mode:
            switch = await self.tap_sel(t, '#' + then_mode[0])
            if switch is not None:
                taps.append(switch); acts.append(f'mode {then_mode[1]}')
            await asyncio.sleep(gap)
            cs = [c for c in (await self.ev(t, TAG_JS) or []) if not c['header'] and not c['disabled'] and c['onscreen'] and c['hit'] and RESET_RX.search(c['id'] + ' ' + c['label'])]
            if cs:
                reset = await self.tap(t, cs[0]['x'], cs[0]['y']); taps.append(reset); acts.append(cs[0]['label'] or cs[0]['id'])
        await self.idle(t)
        s = await self.st(t)
        r = self.keep(name, mode, taps, (await self.log(t) or [])[n0:], await self.ev(t, PLAYS_JS), acts=acts, switch=switch, reset=reset, hint=s.get('hint'), kind='fast', gap=gap)
        await self.done(t, name, shot=re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-'))
        return r

    async def first_tap(self, what, mode_id=None):
        t = await self.tab()
        s0 = await self.st(t)
        tap, note = None, ''
        if what == 'stage':
            p = await self.ev(t, STAGE_JS)
            if p:
                tap, note = await self.tap(t, p[0], p[1]), f'a point in {p[2]} that is not a control'
        elif what == 'key':
            tap = await self.ev(t, 'performance.now()'); await self.key(t, 'Tab'); note = 'Tab'
        else:
            tap = await self.tap_sel(t, '#' + (mode_id or what))
        if tap is None:
            await self.done(t, f'first tap: {what}')
            return None
        await self.idle(t, least=1.2)
        s = await self.st(t)
        r = self.keep(f'first tap: {what if not mode_id else "mode " + mode_id}', None, [tap], await self.log(t), await self.ev(t, PLAYS_JS), kind='first', what=what, note=note,
                      sound0=s0.get('sound'), sound1=s.get('sound'), hint=s.get('hint'))
        await self.done(t, r['name'])
        return r

    async def first_control(self, c):
        """One control as the first tap, alone (no other page running): the timing the parallel repeat runs cannot give."""
        t = await self.tab()
        await self.ev(t, TAG_JS)
        p = await self.ev(t, f'({LOCATE_JS})({c["i"]})') or {}
        if 'x' not in p:
            await self.done(t, 'first tap on a control'); return None
        tap = await self.tap(t, p['x'], p['y'])
        await self.idle(t, least=1.2)
        r = self.keep(f'first tap alone: {c["label"] or c["id"]}', None, [tap], await self.log(t), await self.ev(t, PLAYS_JS), kind='firstc', control=c)
        await self.done(t, r['name'])
        return r

    async def read_runs(self, other_mode):
        out = {}
        # a: Read during a line
        t = await self.tab()
        p = await self.ev(t, STAGE_JS)
        t1 = await self.tap(t, p[0], p[1]) if p else None
        if not p:
            t1 = await self.ev(t, 'performance.now()'); await self.key(t, 'Tab')
        await asyncio.sleep(.7)
        before = await self.st(t)
        t2 = await self.tap_sel(t, '#read')
        await asyncio.sleep(.3)
        hint_at = (await self.st(t)).get('hint')
        await self.idle(t, least=1)
        out['during'] = self.keep('read: Read during a line', None, [t1, t2], await self.log(t), await self.ev(t, PLAYS_JS), kind='read', playing_before=before.get('active', 0) or before.get('speaking'), hint=hint_at)
        await self.done(t, 'read during a line')
        # b: Read with Sound off
        t = await self.tab()
        t1 = await self.tap_sel(t, '#sound'); await asyncio.sleep(.5)
        s = await self.st(t)
        t2 = await self.tap_sel(t, '#read'); await self.idle(t, least=1)
        out['off'] = self.keep('read: Read with Sound off', None, [t1, t2], await self.log(t), await self.ev(t, PLAYS_JS), kind='read', sound=s.get('sound'), hint=s.get('hint'))
        await self.done(t, 'read with sound off')
        # c: a mode change right after Read
        if other_mode:
            t = await self.tab()
            t1 = await self.tap_sel(t, '#read'); await asyncio.sleep(.35)
            t2 = await self.tap_sel(t, '#' + other_mode[0]); await self.idle(t, least=1)
            out['mode'] = self.keep('read: mode change right after Read', None, [t1, t2], await self.log(t), await self.ev(t, PLAYS_JS), kind='read', to=other_mode[1])
            await self.done(t, 'mode change after read')
        return out

    async def state_run(self, st):
        t = await self.tab()
        t0 = await self.ev(t, 'performance.now()')
        lost, missing = await self.steps(t, None, st.get('steps', []))
        await self.idle(t)
        r = self.keep(f'state {st["name"]}', None, [t0], await self.log(t), await self.ev(t, PLAYS_JS), kind='state', missing=missing)
        await self.done(t, r['name'])
        return r


# ---------- reading the logs ----------

def windows(run):
    """The run's log split by its taps: [[entries after tap k and before tap k+1]]."""
    taps = run['taps']
    out = [[] for _ in taps]
    for e in run['log']:
        k = max((i for i, tp in enumerate(taps) if tp is not None and e['t'] >= tp - 5), default=None)
        if k is not None:
            out[k].append(e)
    return out


def line_name(e, keys):
    k = e['key']
    if k and k != e['text']:
        return k
    return keys.get(e['text']) or ('"' + e['text'][:38] + ('..."' if len(e['text']) > 38 else '"'))


def repeat_rows(run, keys):
    """One row per line the control queued: (name, kind, expected, spoken text, status, note, text)."""
    wins = windows(run)
    lines, order = {}, []
    for k, w in enumerate(wins):
        for e in w:
            if not e['text']:
                continue
            key = (e['key'] or e['text'], e['kind'])
            if key not in lines:
                lines[key] = {'e': e, 'wins': {}, 'spoken': 0, 'silent': 0, 'dropped': 0, 'why': set(), 'cut': 0}; order.append(key)
            L = lines[key]
            L['wins'].setdefault(k, set()).add(e['as'])
            if e['as'] in ('spoken', 'silent', 'dropped'):
                L[e['as']] += e['n'] if e['as'] != 'spoken' else 1
            if e['as'] != 'spoken' and e['why']:
                L['why'].add(e['why'])
            if e['cut']:
                L['cut'] += 1
    rows, n = [], len(run['taps'])
    for key in order:
        L, e = lines[key], lines[key]['e']
        kind, name = e['kind'], line_name(e, keys)
        extra = ', '.join(x for x in (f'{L["silent"]} silent' if L['silent'] else '', f'{L["dropped"]} dropped: {"/".join(sorted(L["why"])) or "?"}' if L['dropped'] else '',
                                      f'{L["cut"]} cut by the next' if L['cut'] else '') if x)
        if kind == 'read':
            continue
        if kind in ('how', 'welcome'):
            exp = '1' if L['spoken'] else '0 more' if 'heard' in L['why'] or 'off' in L['why'] else '1'
            status = 'FAIL' if L['spoken'] > 1 else 'ok' if L['spoken'] == 1 or exp == '0 more' else 'LEAD'
            note = 'spoken more than once' if status == 'FAIL' else 'queued but never spoken in this run' if status == 'LEAD' else ''
            if status == 'ok' and kind == 'how' and RESULTISH.search(e['text']):
                status, note = 'LEAD', 'a how line that reads like a result: it goes quiet after the first time; check its kind'
        else:
            queued = len(L['wins'])
            heard = sum(1 for k, a in L['wins'].items() if 'spoken' in a or (k + 1 in L['wins'] and False))
            # a line queued late in one window and spoken at the start of the next still counts for its own window
            for k, a in L['wins'].items():
                if 'spoken' not in a and k + 1 < len(wins) and any(x['as'] == 'spoken' and (x['key'] or x['text']) == key[0] for x in wins[k + 1][:2]) and L['spoken'] > heard:
                    heard += 1
            exp = f'{queued}'
            status = 'ok' if heard >= queued else 'LEAD'
            note = '' if status == 'ok' else f'queued after {queued} of {n} clicks, spoken after {heard}'
            if status == 'ok' and HOWISH.search(e['text']) and L['spoken'] >= 3:
                status, note = 'LEAD', 'an event line that reads like a how-to and comes back after every tap; check its kind'
        rows.append({'name': name, 'kind': kind, 'exp': exp, 'spoken': str(L['spoken']) + (f' ({extra})' if extra else ''), 'status': status, 'note': note, 'text': e['text'], 'key': key[0]})
    return rows


def spoken_seq(entries, tap):
    return [(e['kind'], e['key'], e['text'], round(e['t'] - tap)) for e in entries if e['as'] in ('spoken', 'read') and e['text']]


# ---------- the static checks ----------

def static_checks(C, tool, folder, src, bundle_note, meta, k2):
    L = lib.Lines(src)
    html = folder / f'{tool}.html'
    C.section('Contract (Craft 1, Exit check 6, Finish check 5)')
    if html.exists():
        size = html.stat().st_size
        notes = (folder / 'notes.md').read_text(encoding='utf-8') if (folder / 'notes.md').exists() else ''
        reason = re.search(r'^Size:.*', notes, re.M)
        where = f'`tools/{tool}/{tool}.html` is {size / 1024:.0f} KB ({size / 1e6:.2f} MB). {bundle_note}'
        if size <= GOAL:
            C.add('PASS', 'Bundle size: under the 2 MB goal.', where)
        elif size <= REASON:
            C.add('LEAD', 'Bundle size: over the 2 MB goal, under the 6 MB rule (fine; trim if it is easy).', where)
        else:
            C.add('PASS' if reason else 'FAIL', 'Bundle size: over 6 MB' + (', with a Size: reason in notes.md.' if reason else ' and notes.md has no "Size:" line.'), where, reason.group(0) if reason else '')
        C.add('PASS', 'One file: the bundle is a single .html.', 'Whether it works offline is the network check below.')
        text = html.read_text(encoding='utf-8', errors='replace')
        problems, notices = safety_scan(text, folder)
        C.add('FAIL' if problems else 'PASS', f'Outside servers, tracking, code from strings (scripts/check_safety.py on the bundle): {len(problems)} problem{"" if len(problems) == 1 else "s"}.',
              *[f'- {p[:200]}' for p in problems[:12]], *[f'- notice: {p[:200]}' for p in notices[:6]])
    else:
        C.add('FAIL', f'No bundle at tools/{tool}/{tool}.html.', bundle_note)
    return L


def words_checks(C, tool, folder, src):
    C.section('Words (Craft 6)')
    files = [('src.html', True), ('notes.md', True), ('plan.md', True), ('voice/lines.json', True), ('tool.json', True), ('tool.draft.json', True),
             ('spec.md', False), ('art/prompts.json', False), ('handoff.md', False)]
    em, en, alone, seen = [], 0, [], []
    for name, ships in files:
        p = folder / name
        if not p.exists():
            continue
        seen.append(name)
        for n, line in enumerate(p.read_text(encoding='utf-8', errors='replace').split('\n'), 1):
            if EM in line or '&mdash;' in line or '\\u2014' in line or '&#8212;' in line:
                k = max(line.find(EM), 0)
                em.append((ships, f'- {name}:{n}: ...{line[max(0, k - 40):k + 40].strip()}...'))
            en += line.count('–')
            for m in re.finditer(r'\bCurio\b(?!\s+Class)(?!\.[A-Za-z_$])(?![-_\w])', line):
                if name == 'src.html' and re.search(r'(window\.|typeof\s+|const\s+|=\s*)$', line[:m.start()]):
                    continue
                alone.append((ships, f'- {name}:{n}: ...{line[max(0, m.start() - 40):m.end() + 40].strip()}...'))
    for what, hits in (('Em dashes', em), ('"Curio" without "Class"', alone)):
        ship = [h for s, h in hits if s]; other = [h for s, h in hits if not s]
        if ship:
            C.add('FAIL', f'{what}: {len(ship)} in files that ship.', *ship[:15], f'(and {len(other)} in spec.md, prompts.json or handoff.md)' if other else '')
        elif other:
            C.add('LEAD', f'{what}: none in files that ship, {len(other)} in working files.', *other[:10])
        else:
            C.add('PASS', f'{what}: none.', 'Looked in: ' + ', '.join(seen) + '.')
    if en:
        C.add('LEAD', f'En dashes: {en} (allowed in number ranges such as a grade span; check none stands in for an em dash).')
    mask_src = src
    store = [f'- src.html:{n}: {ln.strip()[:140]}' for n, ln in enumerate(mask_src.split('\n'), 1)
             if re.search(r'localStorage|sessionStorage|indexedDB|document\.cookie', ln) and 'curio-motion' not in ln]
    notes = (folder / 'notes.md').read_text(encoding='utf-8') if (folder / 'notes.md').exists() else ''
    said = [f'- notes.md:{n}: {ln.strip()[:160]}' for n, ln in enumerate(notes.split('\n'), 1) if re.search(r'\b(saved?|stored?|this device|privacy|kept on)\b', ln, re.I)]
    C.add('AGENT', 'Privacy stated where anything is stored (rule 7): the script only lists the evidence.',
          f'Storage calls in src.html (the kit keeps the Motion setting under curio-motion): {len(store)}.', *store[:8],
          f'Lines in notes.md that speak of saving or privacy: {len(said)}.', *said[:6])
    C.add('AGENT', 'Classroom-safe language (rule 6): read strings.md; not checked by script.')


def art_checks(C, tool, folder, src):
    C.section('Art (Craft 5)')
    L = lib.Lines(src)
    tokens = {}
    for m in re.finditer(r'(?<![\w-])art:([a-z0-9-]+)', src):
        tokens.setdefault(m.group(1), []).append(L.line(m.start()))
    pj = folder / 'art' / 'prompts.json'
    if not tokens and not pj.exists():
        C.add('PASS', 'No `art:` token in src.html and no art/prompts.json: nothing to match.')
        return
    assets = {}
    if pj.exists():
        try:
            data = json.loads(pj.read_text(encoding='utf-8'))
            items = data.get('assets') if isinstance(data, dict) and isinstance(data.get('assets'), list) else data if isinstance(data, list) else \
                [dict(v, name=k) for k, v in data.items() if isinstance(v, dict)] if isinstance(data, dict) else []
            for a in items:
                if isinstance(a, dict):
                    name = a.get('name') or (a.get('token') or '').replace('art:', '')
                    if name: assets[name] = a
        except Exception as e:
            C.add('FAIL', f'art/prompts.json does not parse: {e}')
    missing = sorted(set(tokens) - set(assets))
    C.add('FAIL' if missing else 'PASS', f'Every `art:` token has a prompts.json entry: {len(tokens)} token{"" if len(tokens) == 1 else "s"}, {len(missing)} without an entry.',
          *[f'- art:{n} (src.html line {", ".join(map(str, tokens[n][:4]))}) has no entry' for n in missing],
          'Tokens: ' + ', '.join(f'{n} (L{tokens[n][0]})' for n in sorted(tokens)) if tokens else '')
    unused = sorted(n for n, a in assets.items() if n not in tokens)
    live = [n for n in unused if not assets[n].get('deferred') and not assets[n].get('superseded_by')]
    if unused:
        C.add('LEAD' if live else 'PASS', f'prompts.json entries no token uses: {len(unused)} ({len(live)} not marked deferred or superseded).',
              ', '.join(live[:30]) if live else 'All are marked deferred or superseded.')
    painted = [n for n in tokens if (folder / 'art' / f'{n}.webp').exists()]
    C.add('LEAD' if len(painted) < len(tokens) else 'PASS', f'Painted: {len(painted)} of {len(tokens)} tokens have their .webp (a draft bundle stands in a labeled circle for the rest).',
          'Not painted: ' + ', '.join(sorted(set(tokens) - set(painted))) if len(painted) < len(tokens) else '')
    PEOPLE = re.compile(r'\b(person|people|child|children|kid|kids|girl|boy|woman|man|men|women|teacher|student|students|dancer|dancers|face|faces|hand|hands|portrait|crowd|baby|farmer|worker|scientist|musician|player|nurse|doctor|family|grandmother|grandfather|elder)\b', re.I)
    rows, leads = [], []
    for n in sorted(assets):
        a = assets[n]
        prompt = ' '.join(str(a.get(k, '')) for k in ('prompt', 'sd'))
        positive = ' '.join(s for s in re.split(r'(?<=[.!?])\s+', prompt) if not re.match(r'\s*(no|without|never|nobody|empty)\b', s, re.I) and not re.search(r'\b(no|without) (people|person|faces|hands|figures)', s, re.I))
        words = sorted({m.group(1).lower() for m in PEOPLE.finditer(positive)})
        ppl = a.get('people')
        by = str(a.get('drawn_by') or a.get('route') or a.get('model') or '')
        if n in tokens or not (a.get('deferred') or a.get('superseded_by')):
            rows.append(f'| {n} | {ppl} | {by or "-"} | {"yes" if n in tokens else "no"} | {", ".join(words[:5]) or "-"} |')
        if ppl is not True and words and n in tokens:
            leads.append(f'- {n}: people is {ppl}, but its prompt names {", ".join(words[:5])}')
        if ppl is True and re.search(r'flux|local|sdxl|\bsd\b|cfart|cloudflare', by, re.I):
            leads.append(f'- {n}: people: true but drawn_by is "{by}" (local models never draw people)')
        if ppl is None:
            leads.append(f'- {n}: no people field')
    C.add('LEAD' if leads else 'PASS', 'People flags against the words of each prompt (a word match, not a look at the picture): ' + (f'{len(leads)} to check.' if leads else 'nothing stands out.'),
          *leads[:15], '', '| asset | people | drawn by | used by a token | people words in the prompt |', '|---|---|---|---|---|', *rows[:40])
    C.add('AGENT', 'Whether a painted picture really shows people, matches the spec and sits well in the frame: needs eyes (Craft 5, Finish check 2).')


def kit_checks(C, src, info):
    C.section('Kit (Craft 1)')
    d = lib.Doc(src)
    kits = sorted({b[0].split(' ', 1)[1] for b in d.blocks if b[0].startswith('script kit:')} | {b[3] for b in d.blocks if b[0] == 'kit css'})
    C.add('PASS' if kits else 'FAIL', 'Kit files included: ' + (', '.join(kits) if kits else 'none'))
    leads, uses = [], []
    pats = [(r'\bspeechSynthesis\b|SpeechSynthesisUtterance', 'speaks through the browser voice itself'), (r'new\s+Audio\s*\(', 'plays its own audio element'),
            (r'prefers-reduced-motion', 'reads the motion setting itself'), (r'curio-motion', 'reads or writes the Motion setting itself'),
            (r'''(?:getElementById\(\s*|\$\(\s*|querySelector\(\s*)['"]#?(read|sound|motion)['"]\s*\)\s*\.(?:onclick|addEventListener)''', 'wires Read, Sound or Motion itself'),
            (r'function\s+(narrate|hush|readNow|firstTap|speakLine|sayLine|enqueue)\s*\(', 'has its own narration function (the copied queue)'),
            (r'new\s+(?:webkit)?AudioContext|window\.AudioContext', 'makes its own AudioContext (fine for music or tones the kit does not offer; check it obeys Sound)')]
    for kind, a, b, extra, s, e in d.blocks:
        if kind != 'script':
            continue
        code = src[s:e]
        mask, strings, comments = lib.scan_js(code)
        for m in re.finditer(r'Curio\.([A-Za-z_$]+)', mask):
            uses.append(m.group(1))
        for rx, what in pats:
            hay = code if 'reduced-motion' in rx or 'curio-motion' in rx or 'read|sound' in rx else mask
            for m in re.finditer(rx, hay):
                if any(ca <= m.start() < cb for ca, cb, _ in comments):
                    continue
                leads.append(f'- src.html:{d.L.line(s + m.start())}: {what}: `{code[m.start():m.start() + 60].splitlines()[0]}`')
    cnt = {}
    for u in uses: cnt[u] = cnt.get(u, 0) + 1
    C.add('PASS' if 'voice' in cnt else 'LEAD', 'Narration goes through Curio.voice.' if 'voice' in cnt else 'No Curio.voice call: the tool narrates some other way (STANDARDS: new tools use the kit helper).',
          'Curio calls in src.html: ' + ', '.join(f'{k} x{v}' for k, v in sorted(cnt.items())))
    C.add('LEAD' if leads else 'PASS', f'Kit parts done again by hand (pattern search): {len(leads)} place{"" if len(leads) == 1 else "s"}.' if leads else
          'No speech, audio element, Motion setting or Read, Sound, Motion wiring outside the kit (pattern search).', *leads[:14],
          'A layout, hint or queue written again under other names is not detected: AGENT if the outline shows suspiciously kit-like functions.')
    if info:
        kb = info.get('kit_buttons') or []
        C.add('PASS' if len(kb) == 3 else 'FAIL', f'Header has the kit buttons Motion, Sound and Read: found {", ".join(kb) or "none"}.')
        C.add('PASS' if info.get('sound') == 'true' else 'LEAD', f'Sound starts on (aria-pressed is {info.get("sound")} at load).' if info.get('sound') == 'true'
              else f'Sound does not start on: #sound aria-pressed is {info.get("sound")} at load, so a first tap may get no welcome.')


def lines_checks(C, tool, folder, src, info, runs, k2):
    C.section('Lines (Craft 3)')
    lj = folder / 'voice' / 'lines.json'
    if not lj.exists():
        C.add('LEAD', 'No voice/lines.json (fine only for a tool that never speaks).')
        return [], {}
    spec = json.loads(lj.read_text(encoding='utf-8'))
    lines = [*spec.get('lines', []), *(t for g in spec.get('groups', []) for t in g)]
    keys = lib.line_keys(src, lines)
    dup = sorted({t for t in lines if lines.count(t) > 1})
    if dup:
        C.add('LEAD', f'lines.json lists {len(dup)} line{"" if len(dup) == 1 else "s"} twice.', *[f'- {t[:100]}' for t in dup[:6]])
    al = (info or {}).get('all_lines')
    if isinstance(al, list):
        a, b = set(al), set(lines)
        only_code, only_json = [t for t in al if t not in b], [t for t in lines if t not in a]
        same_order = al == lines
        C.add('PASS' if not only_code and not only_json else 'FAIL',
              f'`__tool.allLines()` and voice/lines.json hold the same lines, word for word: {len(al)} in the tool, {len(lines)} in lines.json'
              + (f'; {len(only_code)} only in the tool, {len(only_json)} only in lines.json.' if only_code or only_json else ('; same order.' if same_order else '; order differs (not a rule).')),
              *[f'- only in the tool: "{t[:110]}"' for t in only_code[:10]], *[f'- only in lines.json: "{t[:110]}"' for t in only_json[:10]])
    elif info:
        C.add('FAIL', f'`__tool.allLines()` is missing or failed ({str(al)[:80]}): lines.json cannot be compared with the code.')
    else:
        C.add('AGENT', 'allLines() against lines.json: not run (--no-voice).')
    # spoken literals in the code
    d = lib.Doc(src); lits, dyn = [], 0
    lset = set(lines)
    for kind, a, b, extra, s, e in d.blocks:
        if kind != 'script': continue
        code = src[s:e]
        mask, strings, comments = lib.scan_js(code)
        starts = {st: (q, raw) for st, en, q, raw in strings}
        for m in re.finditer(r'\bV\.(?:say|how)\(\s*\[?\s*', mask):
            if m.end() in starts:
                q, raw = starts[m.end()]
                text = lib.unescape_js(raw)
                if re.fullmatch(r'[A-Za-z_$][\w$]*', text) or text == '':
                    continue  # a key of the line table (or the empty barrier line)
                if text not in lset:
                    lits.append(f'- src.html:{d.L.line(s + m.start())}: `V.say("{text[:80]}")` is not in lines.json')
            else:
                dyn += 1
    C.add('FAIL' if lits else 'PASS', f'Text written straight into V.say or V.how: {len(lits)} not in lines.json.' if lits else 'No V.say or V.how call speaks a text that is missing from lines.json.',
          *lits[:10], f'{dyn} call{"" if dyn == 1 else "s"} pass a computed line (a variable or expression): covered only by the run-time row below.' if dyn else '')
    heard = {}
    for r in runs:
        for e in r['log']:
            if e['as'] == 'spoken' and e['text']:
                heard.setdefault(e['text'], set()).add(r['name'])
    if runs:
        stray = [t for t in heard if t not in lset]
        C.add('FAIL' if stray else 'PASS', f'Every line spoken in the script\'s runs is in lines.json, word for word: {len(heard)} different lines heard, {len(stray)} not in lines.json.',
              *[f'- "{t[:110]}" (heard in: {sorted(heard[t])[0]})' for t in stray[:10]])
        never = [t for t in lines if t not in heard]
        C.add('AGENT' if never else 'PASS', f'Coverage: {len(lines) - len(never)} of {len(lines)} lines.json lines were heard in the script\'s runs; {len(never)} were never reached and are unchecked.',
              *[f'- {keys.get(t, "?")}: "{t[:100]}"' for t in never[:60]], f'(and {len(never) - 60} more; see strings.md)' if len(never) > 60 else '')
    clips = [t for t in lines if (folder / 'voice' / clip_name(t)).exists()]
    C.add('PASS' if len(clips) == len(lines) else 'LEAD', f'Recorded clips: {len(clips)} of {len(lines)} lines have a clip in voice/ (the rest use the browser voice'
          + ('; K-2 needs every fixed line recorded by the Finish check).' if k2 else ').'))
    C.add('AGENT', 'Each line matches what the screen shows when it plays: strings.md lists each line with the runs it was heard in; judging the match needs an agent.')
    return lines, keys


# ---------- the voice section ----------

def voice_checks(C, P, info, results, keys, modes):
    C.section('Standard voice check (Craft 4, Exit check 7, Finish check 3)')
    md = []
    if not info.get('has_log'):
        C.add('AGENT', 'No voice log (`__tool.vlog` or `__tool.V.log`): the script cannot count lines. The whole standard voice check stays with the agent.')
        return ''
    C.add('PASS' if not info['early_spoken'] and not info['early_plays'] else 'FAIL',
          'Nothing speaks before the first tap (3 s on a fresh page, no input): ' + (f'{len(info["early_spoken"])} log lines spoken, {info["early_plays"]} clips or utterances started.'))
    order = {m[0]: k for k, m in enumerate(modes)}
    reps = sorted((r for r in P.runs if r.get('kind') == 'repeat'), key=lambda r: (order.get(r['mode'], -1), r['control']['i']))
    # 1. repeats
    table, fails, leads, quiet, merged = [], [], [], [], {}
    empties = 0
    for r in reps:
        rows = repeat_rows(r, keys)
        empties += sum(e['n'] for e in r['log'] if not e['text'])
        lab = r['control']['label'] or '#' + r['control']['id']
        ml = next((m[1] for m in modes if m[0] == r['mode']), 'first mode')
        if not rows:
            quiet.append(f'{lab} ({ml})'); continue
        for row in rows:
            k = (ml, row['name'], row['kind'], row['exp'], re.sub(r'\d+ cut by the next', 'cut', row['spoken']), row['status'], row['note'])
            merged.setdefault(k, []).append(f'{lab} x{len(r["taps"])}' + (f' [{r["stop"]}]' if r['stop'] else '') + (' [6 s gaps]' if r.get('slow') else ''))
            if row['status'] == 'FAIL': fails.append((lab, row))
            if row['status'] == 'LEAD': leads.append((lab, row))
    for (ml, name, kind, exp, spoken, status, note), labs in merged.items():
        who = ', '.join(labs[:4]) + (f' and {len(labs) - 4} more' if len(labs) > 4 else '')
        table.append(f'| {md_cell(name)} | {kind} | {md_cell(ml)}: {md_cell(who)} | {exp}{" each" if len(labs) > 1 else ""} | {md_cell(spoken)}{" each" if len(labs) > 1 else ""} | {status}{": " + note if note else ""} |')
    n_ctl = len(reps)
    head = f'{n_ctl} control runs (a fresh page each, five held clicks, each click after the page went quiet), {len(merged)} line rows.'
    if fails:
        C.add('FAIL', f'1. Repeats: {len(fails)} how-to or welcome line{"" if len(fails) == 1 else "s"} spoken more than once in a run of five. {head}', *[f'- {lab}: {row["name"]} spoken {row["spoken"]}' for lab, row in fails[:10]])
    if leads:
        C.add('LEAD', f'1. Repeats: {len(leads)} row{"" if len(leads) == 1 else "s"} to confirm (an event queued but not spoken every time, a line never spoken, or a kind that reads wrong). {head}',
              *[f'- {lab}: {row["name"]} ({row["kind"]}): {row["note"]}; spoken {row["spoken"]}: "{row["text"][:70]}"' for lab, row in leads[:14]])
    if not fails and not leads:
        C.add('PASS' if reps else 'AGENT', f'1. Repeats: every how-to and welcome line was spoken at most once and every event line was spoken each time it was queued. {head}' if reps else '1. Repeats: no control was driven.')
    C.add('AGENT', '1. Repeats, what the script cannot see: whether each line has the right kind (a result marked how goes quiet; a how-to marked event nags). Read the kind column of the counts table against the text in strings.md.')
    md += ['### Counts table (repeats)', '', 'Expected for a how-to or welcome line is once (or "0 more" when it was already heard on this page). Expected for an event line is the number of clicks that queued it.', '',
           '| line | kind | action | expected | spoken | result |', '|---|---|---|---|---|---|', *table]
    if quiet:
        md += ['', f'| (none) | - | {md_cell(", ".join(quiet[:12]))}{f" and {len(quiet) - 12} more" if len(quiet) > 12 else ""}, two clicks each | 0 | 0 | no line queued |']
    if empties:
        md += ['', f'The log also holds {empties} entries with an empty text (a tool queuing an empty line as a barrier); they are left out of the table.']
    # first tap per control (first mode)
    ft_rows, ft_leads = [], []
    for r in reps:
        if r['mode'] or not r['taps']:
            continue
        alone = next((x for x in P.runs if x.get('kind') == 'firstc' and x['control']['i'] == r['control']['i']), None)
        w = windows(alone or r)
        seq = spoken_seq(w[0], (alone or r)['taps'][0]) if w else []
        lab = r['control']['label'] or '#' + r['control']['id']
        if not seq:
            other = [f'{e["kind"]} {line_name(e, keys)} {e["as"]}({e["why"]})' for e in (w[0] if w else []) if e['text']][:3]
            ft_leads.append(f'- {lab}: nothing spoken after the first tap' + (f' ({"; ".join(other)})' if other else ' (no line queued)'))
            ft_rows.append((lab, 'nothing', '-', 'LEAD'))
        elif seq[0][0] == 'welcome':
            ok = seq[0][3] <= 700
            ft_rows.append((lab, 'welcome ' + line_name({'key': seq[0][1], 'text': seq[0][2]}, keys), f'{seq[0][3]} ms', 'ok' if ok else 'LEAD'))
            if not ok: ft_leads.append(f'- {lab}: the welcome started {seq[0][3]} ms after the tap (about half a second is the rule)')
        else:
            wl = [s for s in seq[1:] if s[0] == 'welcome']
            ft_rows.append((lab, 'its own line ' + line_name({'key': seq[0][1], 'text': seq[0][2]}, keys) + (', then the welcome' if wl else ''), f'{seq[0][3]} ms', 'ok'))
    results['first_controls'] = (ft_rows, ft_leads)
    # 2. stale, 5. order
    owner = {}
    for r in reps:
        for e in r['log']:
            if e['text'] and e['kind'] != 'welcome':
                owner.setdefault(e['key'] or e['text'], set()).add((r['mode'], r['control']['label'] or r['control']['id']))
    mode_keys = {}
    for r in reps:
        for e in r['log']:
            if e['text']: mode_keys.setdefault(r['mode'], set()).add(e['key'] or e['text'])
    fasts = [r for r in P.runs if r.get('kind') == 'fast']
    st_leads, st_lines, ord_bad, ord_seen = [], [], [], 0
    for r in fasts:
        acts = r.get('acts', [])
        tl = []
        for e in r['log']:
            if not e['text']: continue
            k = max((i for i, tp in enumerate(r['taps']) if e['t'] >= tp - 5), default=0)
            tl.append(f'{e["as"]}{"(" + e["why"] + ")" if e["why"] else ""}{" cut:" + e["cut"] if e["cut"] else ""} {e["kind"]} {line_name(e, keys)} +{round(e["t"] - r["taps"][k])} ms after "{acts[k] if k < len(acts) else "?"}"')
        st_lines.append(f'- **{r["name"]}** (gap {r["gap"]} s): taps: {" > ".join(acts)}. Log: ' + ('; '.join(tl) if tl else 'nothing queued') + f'. Hint at the end: "{(r.get("hint") or "")[:120]}". Frame: frames/{re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")}.png')
        if r.get('switch') is not None:
            new = next((m[0] for m in modes if f'mode {m[1]}' in acts), None)
            for e in r['log']:
                if e['as'] == 'spoken' and e['t'] > r['switch'] + 150 and e['text']:
                    k = e['key'] or e['text']
                    if k in mode_keys.get(r['mode'], set()) and k not in mode_keys.get(new, set()) and e['kind'] != 'welcome':
                        st_leads.append(f'- {r["name"]}: "{line_name(e, keys)}" started {round(e["t"] - r["switch"])} ms after the switch to another mode; in the repeats it was only ever queued in the mode that was left')
            for p in r['plays']:
                if p['t'] < r['switch'] and (p['end'] is None or p['end'] > r['switch'] + 600):
                    st_leads.append(f'- {r["name"]}: a clip or utterance that began before the mode switch was still playing {"at the end of the run" if p["end"] is None else str(round(p["end"] - r["switch"])) + " ms after it"}')
        # order: lines owned by exactly one tapped control must come in tap order
        labs = [a for a in acts]
        last = -1
        for e in r['log']:
            if e['as'] != 'spoken' or not e['text'] or e['kind'] != 'event': continue
            own = {lab for m, lab in owner.get(e['key'] or e['text'], set()) if m == r['mode']}
            idx = [i for i, a in enumerate(labs) if a in own]
            if len(idx) != 1: continue
            ord_seen += 1
            if idx[0] < last:
                ord_bad.append(f'- {r["name"]}: "{line_name(e, keys)}" (from tap {idx[0] + 1}, {labs[idx[0]]}) was spoken after a line from tap {last + 1}')
            last = max(last, idx[0])
    if fasts:
        C.add('LEAD' if st_leads else 'PASS', ('2. Stale lines: ' + (f'{len(st_leads)} to confirm.' if st_leads else f'in {sum(1 for r in fasts if r.get("switch") is not None)} fast run(s) (taps 0.2 s apart, then a mode switch and Reset) no line that belongs to the mode left behind started after the switch, and no clip played on across it.')),
              *st_leads[:10])
        C.add('AGENT', '2. Stale lines, what the script cannot see: whether each spoken line fits the screen at its time, and lines naming a hidden control. Read the timelines below and open the end frames (sheet-voice-ends) only where a line looks out of place.')
        C.add('LEAD' if ord_bad else 'PASS' if ord_seen >= 2 else 'AGENT', '5. Order: ' + (f'{len(ord_bad)} event line{"" if len(ord_bad) == 1 else "s"} that the repeats tie to an older tap spoken after the line of a newer tap (confirm in the timeline: a later tap may queue it again by right).' if ord_bad else
              f'{ord_seen} spoken event lines that belong to exactly one tapped control came in tap order (fast and 1.2 s runs).' if ord_seen >= 2 else
              f'not exercised: only {ord_seen} spoken line{"" if ord_seen == 1 else "s"} in the mixed runs could be tied to one tap. Read the timelines.'), *ord_bad[:8])
    else:
        C.add('AGENT', '2. Stale lines and 5. Order: no mixed runs were made (no control with a line of its own was found, or the budget ran out).')
    md += ['', '### Timelines (stale and order runs)', '', *st_lines]
    # 3. first tap
    rows3, leads3, fails3 = [], [], []
    first_welcome = None
    for r in [x for x in P.runs if x.get('kind') == 'first']:
        seq = spoken_seq(r['log'], r['taps'][0])
        heard = '; '.join(f'{k} {line_name({"key": key, "text": text}, keys)} at {ms} ms' for k, key, text, ms in seq[:4]) or 'nothing'
        what, ok, note = r['what'], 'ok', ''
        if what in ('stage', 'key'):
            if seq and seq[0][0] == 'welcome':
                first_welcome = first_welcome or seq[0][1]
                if seq[0][3] > 700: ok, note = 'LEAD', 'welcome later than about half a second'
            elif seq:
                ok, note = 'LEAD', 'the first line was not the welcome (fine only if this tap is an action with its own line)'
            else:
                ok, note = 'LEAD', 'a plain first tap spoke nothing'
        elif what == 'read':
            others = [s for s in seq if s[0] != 'read']
            if not seq or seq[0][0] != 'read': ok, note = 'FAIL', 'Read as the first tap did not speak the hint first'
            elif others: ok, note = 'FAIL', 'Read as the first tap was followed by another line'
            elif r.get('hint') and seq[0][2].strip() != r['hint']: ok, note = 'LEAD', f'Read spoke "{seq[0][2][:60]}" but #hint shows "{r["hint"][:60]}"'
        elif what == 'sound':
            if r.get('sound0') != 'true':
                ok, note = 'LEAD', f'Sound was {r.get("sound0")} at load, so this tap turned it on; heard: {heard}'
            elif seq or any(p['t'] >= r['taps'][0] for p in r['plays']): ok, note = 'FAIL', 'Sound as the first tap spoke'
        else:  # a mode button
            if not seq: ok, note = 'LEAD', 'a first tap on a mode button spoke nothing'
            elif seq[0][0] != 'welcome': ok, note = 'LEAD', 'the first line was not a welcome'
            elif first_welcome and seq[0][1] == first_welcome: ok, note = 'LEAD', 'the welcome heard is the first mode\'s, not this mode\'s'
            elif seq[0][3] > 700: ok, note = 'LEAD', 'welcome later than about half a second'
        rows3.append(f'| {md_cell(r["name"].replace("first tap: ", ""))}{" (" + r["note"] + ")" if r.get("note") else ""} | {md_cell(heard)} | {ok}{": " + md_cell(note) if note else ""} |')
        if ok == 'LEAD': leads3.append(f'- {r["name"]}: {note}')
        if ok == 'FAIL': fails3.append(f'- {r["name"]}: {note}; heard: {heard}')
    ft_rows, ft_leads = results.get('first_controls', ([], []))
    own = sum(1 for x in ft_rows if x[1].startswith('its own line')); wel = sum(1 for x in ft_rows if x[1].startswith('welcome'))
    if fails3:
        C.add('FAIL', f'3. First-tap timing: {len(fails3)} wrong.', *fails3)
    if leads3 or ft_leads:
        C.add('LEAD', f'3. First-tap timing: {len(leads3) + len(ft_leads)} to confirm.', *leads3, *ft_leads[:14], f'(and {len(ft_leads) - 14} more controls)' if len(ft_leads) > 14 else '')
    if not fails3 and not leads3 and not ft_leads and rows3:
        C.add('PASS', f'3. First-tap timing: {len(rows3)} kinds of first tap and {len(ft_rows)} controls as the first tap behaved as the rule asks.')
    md += ['', '### First tap (a fresh page each)', '', '| first tap | heard | result |', '|---|---|---|', *rows3,
           f'| each of {len(ft_rows)} controls in the first mode (click 1 of its repeat run, taken again alone when it looked late or silent) | {wel} got the welcome first, {own} spoke their own line first, {len(ft_rows) - wel - own} spoke nothing | {"ok" if not ft_leads else "LEAD: see checks.md"} |']
    slow = [x for x in ft_rows if x[1].startswith('welcome')]
    if slow:
        ms = sorted(int(x[2].split()[0]) for x in slow)
        md += ['', f'Welcome start after a plain first tap on a control: fastest {ms[0]} ms, slowest {ms[-1]} ms.']
    # 4. Read
    rd = results.get('read', {})
    if rd:
        ev4, bad4, lead4 = [], [], []
        r = rd.get('during')
        if r:
            reads = [e for e in r['log'] if e['as'] == 'read']
            before = [e for e in r['log'] if e['as'] == 'spoken' and e['t'] < r['taps'][1]]
            after = [e for e in r['log'] if e['as'] == 'spoken' and e['t'] > r['taps'][1]]
            rp = [p for p in r['plays'] if p['t'] >= r['taps'][1] - 5]
            cut = before and before[-1]['cut'] == 'read'
            ev4.append(f'- Read 0.7 s after a first tap: line playing then: {line_name(before[-1], keys) if before else "none"}{" (cut by Read)" if cut else ""}; Read spoke "{reads[0]["text"][:90] if reads else ""}"; '
                       f'hint on screen "{(r.get("hint") or "")[:90]}"; audio for Read: {rp[0]["kind"] + ", end: " + str(rp[0]["how"]) if rp else "none started"} (cap = the browser voice gave no end event in headless Chrome, so a cut could not be seen); lines after Read with no input: {", ".join(line_name(e, keys) for e in after) or "none"}.')
            if not reads: bad4.append('- Read during a line logged no read entry')
            elif before and r.get('playing_before') and not cut: bad4.append(f'- the line playing ({line_name(before[-1], keys)}) was not cut by Read')
            if reads and r.get('hint') is not None and reads[0]['text'].strip() != r['hint']: lead4.append('- Read spoke a text that differs from #hint (fine when the tool passes its own read(); check it is the current step)')
            if rp and rp[0]['how'] == 'cut': bad4.append('- the Read audio was cut off with no input')
            if not rp: lead4.append('- no audio started for Read in headless Chrome (log only; could not confirm sound)')
        r = rd.get('off')
        if r:
            reads = [e for e in r['log'] if e['as'] == 'read']
            rp = [p for p in r['plays'] if p['t'] >= r['taps'][1] - 5]
            ev4.append(f'- Sound off (aria-pressed {r.get("sound")}), then Read: read entries {len(reads)}; audio started: {"yes, " + rp[0]["kind"] if rp else "no"}.')
            if r.get('sound') != 'false': lead4.append(f'- the Sound tap left aria-pressed at {r.get("sound")} (Sound may start off): this run did not test Read with Sound off')
            elif not reads or not rp: bad4.append('- Read with Sound off did not speak')
        r = rd.get('mode')
        if r:
            nxt = [e for e in r['log'] if e['as'] == 'spoken' and e['t'] >= r['taps'][1]]
            ms = round(nxt[0]['t'] - r['taps'][1]) if nxt else None
            ev4.append(f'- Read, then mode {r["to"]} 0.35 s later: next line {line_name(nxt[0], keys) + " at " + str(ms) + " ms" if nxt else "none"}.')
            if not nxt: lead4.append('- after Read then a mode change, no line started (the new mode\'s welcome was expected)')
            elif ms > 700: bad4.append(f'- after Read then a mode change the next line waited {ms} ms')
        C.add('FAIL' if bad4 else 'LEAD' if lead4 else 'PASS', '4. Read: ' + ('wrong: see below.' if bad4 else 'to confirm: see below.' if lead4 else 'Read cut the line and spoke the hint, spoke with Sound off, and a mode change right after Read let the next line start at once.'), *bad4, *lead4, *ev4)
        C.add('AGENT', '4. Read, not tested by script: Read during every kind of line and during a long animation (the script tried it once, during the first line after a first tap).')
    return '\n'.join(md)


def strings_md(tool, src, doc, ranges, info, lines, keys, runs):
    L = doc.L
    out = [f'# Strings: {tool}', '', 'Every string a student can read or hear, with src.html line numbers (L). "run time" means the text is put '
           'together in code and is not in src.html as one literal; search for a distinctive word.', '']
    out += ['## Spoken lines (voice/lines.json order)', '', '| key | L | line | heard in the script\'s runs as |', '|---|---|---|---|']
    heard = {}
    for r in runs:
        for e in r['log']:
            if e['text'] and e['as'] == 'spoken':
                h = heard.setdefault(e['text'], {'kinds': set(), 'n': 0, 'runs': []})
                h['kinds'].add(e['kind']); h['n'] += 1
                if r['name'] not in h['runs']: h['runs'].append(r['name'])
    for t in lines:
        h = heard.get(t)
        ln = lib.find_lines(src, L, t)
        out.append(f'| {keys.get(t, "")} | {", ".join(map(str, ln)) or "run time"} | {md_cell(t)} | ' + (f'{"/".join(sorted(h["kinds"]))}, {h["n"]} times ({md_cell("; ".join(h["runs"][:2]))}{" ..." if len(h["runs"]) > 2 else ""})' if h else 'never heard') + ' |')
    extra = [t for t in heard if t not in set(lines)]
    for t in extra:
        out.append(f'| NOT IN lines.json | {", ".join(map(str, lib.find_lines(src, L, t))) or "run time"} | {md_cell(t)} | {heard[t]["n"]} times |')
    reads = {}
    for r in runs:
        for e in r['log']:
            if e['as'] == 'read' and e['text']: reads[e['text']] = r['name']
    if reads:
        out += ['', '## What Read spoke (the hint at that moment)', '', *[f'- "{t[:200]}" ({n})' for t, n in reads.items()]]
    if info and info.get('strings'):
        out += ['', '## On screen, by mode (the first screen of each mode at 1366x768, visible text and labels)']
        base = {(k, s) for k, s, w in info['strings'].get('(first screen)', [])}
        for mode, items in info['strings'].items():
            out += ['', f'### {mode}' + ('' if mode == '(first screen)' else ' (only what the first screen did not already show)'), '']
            for kind, s, where in items:
                if mode != '(first screen)' and (kind, s) in base:
                    continue
                ln = lib.find_lines(src, L, s)
                out.append(f'- {"L" + ",".join(map(str, ln)) if ln else "run time"} {where}{" [" + kind + "]" if kind != "text" else ""}: {s}')
    out += ['', '## In the markup of src.html (static, by nearest id)', '']
    for ln, kind, s, where in doc.strings:
        out.append(f'- L{ln} ({where[-1] if where else ""}){" [" + kind + "]" if kind != "text" else ""}: {s}')
    ds = lib.display_strings(src, doc, ranges)
    spoken = set(lines)
    out += ['', '## String literals in the script (by function or data table; spoken lines above are left out)']
    grp = None
    shown = 0
    last = None  # short strings on the same line of the same table share one bullet
    for ln, s, g in ds:
        if s in spoken:
            continue
        if g != grp:
            out += ['', f'### {g}', '']; grp = g; last = None
        shown += 1
        if len(s) < 32 and last == ln and len(out[-1]) < 600:
            out[-1] += ' / ' + s
        else:
            out.append(f'- L{ln}: {s[:300]}'); last = ln if len(s) < 32 else None
    out.append('')
    out.append(f'{shown} literals. The filter keeps anything that looks like words and drops selectors, CSS and code; it can miss a one-word label written in lower case and can keep a stray code string.')
    return '\n'.join(out) + '\n'


def sheets(out, audit, own_frames, modes_n):
    """Contact sheets from the audit folder's frames (and this script's own voice frames). Returns README rows."""
    made, used = [], set()
    if audit and audit.exists():
        pngs = sorted(p for p in audit.glob('*.png'))
        def size_of(p):
            m = re.search(r'(\d{3,4})x(\d{3,4})', p.name)
            return (int(m.group(1)), int(m.group(2))) if m else (0, 0)
        default = [p for p in pngs if p.name.startswith('size-')]
        modes = [p for p in pngs if p.name.startswith('state-mode-')]
        states = [p for p in pngs if p.name.startswith('state-') and not p.name.startswith('state-mode-')]
        calm = [p for p in pngs if p.name.startswith('calm-')]
        lab = lambda p: p.name[:-4]
        at = lambda ps, w: [p for p in ps if size_of(p)[0] == w]
        plan = [('sheet-1-modes-1366x768', 'Default screen and every mode at 1366x768, and Motion off', at(default, 1366) + at(modes, 1366) + calm, 772, 900),
                ('sheet-2-narrow', 'Default screen and every mode in a narrow window (760x900) and on a phone (375x812)', at(default, 760) + at(modes, 760) + at(default, 375) + at(modes, 375), 772, 600),
                ('sheet-3-preview-680x425', 'Default screen, every mode and every state at the 680x425 tool-page preview', at(default, 680) + at(modes, 680) + at(states, 680), 680, 600),
                ('sheet-4-states-1366x768', 'The states the builder listed (audit-states.json) at 1366x768', at(states, 1366), 772, 900),
                ('sheet-5-states-phone', 'The states the builder listed, on a phone (375x812)', at(states, 375), 772, 600),
                ('sheet-6-default-other-sizes', 'The default screen at 800x500, 1000x625, 1280x720 and 1920x1080', sorted([p for p in default if size_of(p)[0] in (800, 1000, 1280, 1920)], key=size_of), 512, 600)]
        for prefix, title, ps, cw, ch in plan:
            if not ps: continue
            for name, labels in lib.contact_sheets([(lab(p), p) for p in ps], out, prefix, title, cell_w=cw, cell_h=ch):
                made.append((name, title, labels))
            used |= {p.name for p in ps}
        rest = [p.name for p in pngs if p.name not in used]
    else:
        rest = []
    if own_frames:
        for name, labels in lib.contact_sheets([(p.name[:-4], p) for p in own_frames], out, 'sheet-voice-ends', 'How the screen stood at the end of each stale and order run', cell_w=512):
            made.append((name, 'The end of each stale and order run (frames/ in the pack)', labels))
    return made, rest


def flag(name, takes=True):
    if name not in sys.argv:
        return None
    i = sys.argv.index(name)
    v = sys.argv[i + 1] if takes else True
    del sys.argv[i:i + (2 if takes else 1)]
    return v


async def drive_voice(P, C, info, max_controls, budget, do_states, results, jobs):
    t_start = time.time()
    sem = asyncio.Semaphore(jobs)
    over = lambda: time.time() - t_start > budget * 60
    modes = P.modes
    notdone = []
    by_mode = {}
    for mode in [None] + [m[0] for m in modes if not m[2]]:
        ml = next((m[1] for m in modes if m[0] == mode), 'first mode')
        if over():
            notdone.append(f'{ml}: every control (the budget ran out)'); continue
        ctl = [c for c in await P.controls(mode) if not c['header'] and c['id'] not in audit_tool.KIT_IDS]
        todo, groups = [], {}
        for c in ctl:
            if c['disabled']: notdone.append(f'{ml}: {c["label"] or c["id"]} (disabled on the first screen)'); continue
            if not c['onscreen'] or not c['hit']: notdone.append(f'{ml}: {c["label"] or c["id"]} ({"off screen" if not c["onscreen"] else "covered at its centre"})'); continue
            groups.setdefault(c['group'], []).append(c)
        for g, cs in groups.items():
            pick = cs if len(cs) <= 3 else [cs[0], cs[1], cs[-1]]
            todo += pick
            if len(cs) > 3:
                notdone.append(f'{ml}: {len(cs) - 3} more of the same group as "{cs[0]["label"]}" ({", ".join(c["label"] for c in cs[2:-1])[:120]})')
        todo.sort(key=lambda c: c['i'])
        for c in todo[max_controls:]:
            notdone.append(f'{ml}: {c["label"] or c["id"]} (over --max-controls {max_controls})')
        speakers = []

        async def one(c):
            async with sem:
                if over():
                    notdone.append(f'{ml}: {c["label"] or c["id"]} (the budget ran out)'); return
                r = await P.repeat(mode, c)
                if any(x['status'] == 'LEAD' and x['kind'] == 'event' for x in repeat_rows(r, {})):
                    # an event that looked lost: once more with 6 s between clicks, so only a real loss stays a lead
                    r2 = await P.repeat(mode, c, slow=True)
                    lost2 = any(x['status'] == 'LEAD' and x['kind'] == 'event' for x in repeat_rows(r2, {}))
                    P.runs.remove(r2 if lost2 else r)
                    r = r if lost2 else r2
                w = windows(r)
                if w and any(e['as'] == 'spoken' and e['kind'] != 'welcome' and e['text'] for e in w[0]):
                    speakers.append(c)
        await asyncio.gather(*(one(c) for c in todo[:max_controls]))
        speakers.sort(key=lambda c: c['i'])
        by_mode[mode] = speakers
        print(f'  repeats, {ml}: {len(todo[:max_controls])} controls, {len(speakers)} with a line of their own, {round(time.time() - t_start)} s', flush=True)
    # the repeat runs share Chrome with other pages, which can delay a timer by seconds: any first tap that looked
    # late or silent there is taken again alone
    for r in [x for x in P.runs if x.get('kind') == 'repeat' and not x['mode'] and x['taps']]:
        w = windows(r)
        seq = spoken_seq(w[0], r['taps'][0]) if w else []
        if not seq or (seq[0][0] == 'welcome' and seq[0][3] > 700):
            await P.first_control(r['control'])
    for mode, speakers in by_mode.items():
        if over(): break
        ml = next((m[1] for m in modes if m[0] == mode), 'first mode')
        others = [m for m in modes if m[0] != mode and (mode or not m[2])]
        seen, picks = set(), []
        for c in speakers:
            if c['group'] in seen and len(speakers) > 3: continue
            seen.add(c['group']); picks.append(c)
        picks = (picks + [c for c in speakers if c not in picks])[:3]
        if not picks:
            continue
        await P.fast(mode, picks, .2, f'stale {ml}', then_mode=others[0] if others else None)
        if len(picks) > 1:
            await P.fast(mode, picks, 1.2, f'order {ml}')
    for what in ('stage', 'key', 'read', 'sound'):
        await P.first_tap(what)
    for m in modes:
        if not m[2]:
            await P.first_tap('mode', m[0])
    if 'read' in (info.get('kit_buttons') or []):
        results['read'] = await P.read_runs(next((m for m in modes if not m[2]), None))
    if do_states:
        sf = ROOT / 'tools' / P.tool / 'audit-states.json'
        if sf.exists():
            async def state(st):
                async with sem:
                    if over():
                        notdone.append(f'state {st["name"]} (the budget ran out)'); return
                    await P.state_run(st)
            await asyncio.gather(*(state(st) for st in json.loads(sf.read_text(encoding='utf-8')).get('states', [])))
    return notdone


async def run(tool, out, audit, a):
    t0 = time.time()
    folder = ROOT / 'tools' / tool
    src_p = folder / 'src.html'
    if not src_p.exists():
        sys.exit(f'{src_p} not found')
    src = src_p.read_text(encoding='utf-8')
    out.mkdir(parents=True, exist_ok=True)
    meta = next((json.loads((folder / f).read_text(encoding='utf-8')) for f in ('tool.draft.json', 'tool.json') if (folder / f).exists()), {})
    draft = (folder / 'tool.draft.json').exists()
    bundle_note = 'Not rebundled (--no-bundle).'
    if not a['no_bundle']:
        if draft: os.environ['CURIO_DRAFT'] = '1'
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):  # its 'no recording yet' lines: the clips row reports that count
            size = bundle_tool.bundle(folder)
        bundle_note = f'Bundled just now from src.html{" as a draft (CURIO_DRAFT=1: art not painted yet is a labeled circle)" if draft else ""}.' if size else 'bundle_tool did not bundle it.'
    C = Checks()
    P = Pack(tool, out)
    static_checks(C, tool, folder, src, bundle_note, meta, P.k2)
    info, results, notdone, times = None, {}, [], {}
    if not a['no_voice'] or not audit:
        drive.ensure_chrome(Path(drive.PROFILE).resolve())
    if not audit:
        t1 = time.time()
        audit = out / 'audit-nowalk'; audit.mkdir(exist_ok=True)
        print('no --audit: running the sizes and states part of audit_tool.py (no walk)', flush=True)
        await audit_tool.run(tool, audit, False)
        times['audit sizes and states (no --audit given)'] = time.time() - t1
        own_audit = True
    else:
        own_audit = False
    if not a['no_voice']:
        t1 = time.time()
        info = await P.profile()
        times['load and strings'] = time.time() - t1
        t1 = time.time()
        if info['has_log']:
            notdone = await drive_voice(P, C, info, a['max_controls'], a['budget'], not a['no_states'], results, a['jobs'])
        times['voice runs'] = time.time() - t1
    # network and console, from every tab this script opened
    if info:
        C.add('FAIL' if P.requests else 'PASS', f'Network requests while driven: {len(P.requests)} left the file, across {P.tabs_opened} fresh pages (every mode, the voice runs, the states).',
              *[f'- {n}: {u}' for n, u in P.requests[:10]])
        errs = sorted({(n, e) for n, e in P.tab_errors})
        C.add('FAIL' if errs else 'PASS', f'Console errors and exceptions while driven: {len(errs)}, across {P.tabs_opened} fresh pages.', *[f'- {n}: {e[:200]}' for n, e in errs[:12]],
              'Console errors at every size and state are in the shared audit (audit.md): cite it.')
    else:
        C.add('AGENT', 'Network requests and console errors at run time: not checked (--no-voice).')
    am = audit / 'audit.md'
    if am.exists():
        txt = am.read_text(encoding='utf-8', errors='replace')
        lead = re.search(r'\*\*(\d+) leads?\.\*\*', txt)
        stale = am.stat().st_mtime < src_p.stat().st_mtime
        C.add('LEAD' if (lead and int(lead.group(1))) or stale else 'PASS',
              f'Shared audit ({am}): {lead.group(1) + " leads" if lead else "no lead count found"}{"" if not own_audit else " (sizes and states only: this script ran it without the walk)"}.',
              'THE AUDIT IS OLDER THAN src.html: its frames and the contact sheets built from them show an earlier build. Re-run audit_tool.py.' if stale else '',
              'Its leads are for the lens to confirm on a frame; they are not repeated here.')
    else:
        C.add('AGENT', f'No audit.md in {audit}: sizes, targets, fold and overlaps were not checked by anything.')
    kit_checks(C, src, info)
    lines, keys = lines_checks(C, tool, folder, src, info, P.runs, P.k2)
    art_checks(C, tool, folder, src)
    words_checks(C, tool, folder, src)
    C.section('Access (Craft 2)')
    C.add('AGENT', 'Keyboard path, visible focus and color never the only signal: not checked by script. Target sizes (44 px, 60 px for K-2) and Motion off are in the shared audit; Sound and Read are in the voice check below.')
    vmd = voice_checks(C, P, info, results, keys, P.modes) if info else ''
    if not info:
        C.section('Standard voice check'); C.add('AGENT', 'Not run (--no-voice).')
    if notdone:
        C.add('AGENT', f'Not driven by the script ({len(notdone)}): sliders, selects, text boxes, drags and taps on the stage are never driven; also:', *[f'- {x}' for x in notdone[:40]],
              f'(and {len(notdone) - 40} more)' if len(notdone) > 40 else '')
    elif info and info.get('has_log'):
        C.add('AGENT', 'Not driven by the script: sliders, selects, text boxes, drags and taps on the stage. Lines that only those reach are in the Coverage row under Lines.')
    states = [r for r in P.runs if r.get('kind') == 'state']
    if states:
        vmd += '\n\n### Lines heard in each builder state (audit-states.json steps, run once)\n\n' + '\n'.join(
            f'- **{r["name"].replace("state ", "")}**: ' + ('; '.join(f'{e["as"]}{"(" + e["why"] + ")" if e["why"] else ""} {e["kind"]} {line_name(e, keys)}' for e in r['log'] if e['text']) or 'nothing queued')
            + (f' (steps not found: {", ".join(r["missing"])})' if r.get('missing') else '') for r in states)
    # the other files
    t1 = time.time()
    omd, ranges, doc = lib.outline(src)
    (out / 'outline.md').write_text(f'# Outline: tools/{tool}/src.html\n\nUse this to pick a slice, then Read src.html with offset and limit, or Grep for a name. Line numbers are src.html lines.\n\n' + omd, encoding='utf-8')
    (out / 'strings.md').write_text(strings_md(tool, src, doc, ranges, info, lines, keys, P.runs), encoding='utf-8')
    own = sorted((out / 'frames').glob('*.png')) if (out / 'frames').exists() else []
    made, rest = sheets(out, audit, own, len(P.modes))
    times['outline, strings, sheets'] = time.time() - t1
    (out / 'voice-logs.json').write_text(json.dumps([{k: v for k, v in r.items()} for r in P.runs], indent=1, ensure_ascii=False), encoding='utf-8')
    total = time.time() - t0
    head = [f'# Checks: {tool}', '', f'Made by scripts/refine_pack.py on {time.strftime("%Y-%m-%d %H:%M")} in {total / 60:.1f} minutes, on the bundle tools/{tool}/{tool}.html '
            f'({"K-2, 60 px targets" if P.k2 else meta.get("grades_label", "")}). {bundle_note}', '',
            f'**FAIL {C.count("FAIL")}, LEAD {C.count("LEAD")}, PASS {C.count("PASS")}, AGENT {C.count("AGENT")}.**', '',
            '- **PASS**: the script ran this test, on exactly what the line names. Cite it; do not redo it.',
            '- **FAIL**: measured and wrong. Confirm it in one look, then report it at the level it deserves.',
            '- **LEAD**: something to confirm on a frame, a log or a line of src.html before you report it. Many leads are fine.',
            '- **AGENT**: the script could not do this. It is still yours, in full.', '',
            'Time: ' + ', '.join(f'{k} {v:.0f} s' for k, v in times.items()) + '.']
    (out / 'checks.md').write_text('\n'.join(head) + '\n' + C.render() + ('\n\n## Voice check tables\n\n' + vmd if vmd else '') + '\n', encoding='utf-8')
    readme = [f'# Evidence pack: {tool}', '', f'Made {time.strftime("%Y-%m-%d %H:%M")} by `python scripts/refine_pack.py {tool}` from the current src.html. Read this pack before you open src.html or start Chrome.', '',
              '| file | what | size |', '|---|---|---|']
    for f, what in (('checks.md', 'the counting checks, each PASS, FAIL, LEAD or AGENT, and the voice counts table'), ('strings.md', 'every on-screen string and spoken line with src.html lines'),
                    ('outline.md', 'src.html as blocks, elements, sections, tables and functions with line ranges'), ('voice-logs.json', 'the raw voice log, taps and audio starts of every run (open only to dig into one run)')):
        readme.append(f'| {f} | {what} | {(out / f).stat().st_size // 1024} KB |')
    for name, title, labels in made:
        readme.append(f'| {name} | {title}: {", ".join(labels)} | {(out / name).stat().st_size // 1024} KB |')
    readme += ['', f'Single frames: the audit folder `{audit}` ({len(rest)} more frames not on a sheet: the states at the other sizes, which the audit checks by measurement) and `frames/` here. '
               'Each sheet cell is labeled with its frame file name and its scale; open the single frame only to confirm a lead.', '',
               '## How to use it', '',
               '- **Every lens:** look at sheets 1 to 3 first (every mode at 1366x768, narrow and phone, the 680x425 preview), then the states sheets. Use outline.md to find the function or table you need and read that slice of src.html; do not read src.html whole. Use strings.md for every word on screen or spoken.',
               '- **Craft lens:** start from checks.md. Confirm each FAIL and LEAD (one frame, one log or one slice each), do every AGENT item in full, and cite the PASS rows. Copy the counts table into your Standard voice check section, with your own rows for anything listed as not driven or never heard.',
               '- **Teaching lens:** strings.md is your list of facts, numbers and claims to check against the spec\'s Sources, and of answers a label could give away. The script judges none of that.',
               '- **Play lens:** the sheets replace your first 20 or so frames. Shoot your own only for the extremes, the end of a round and anything a sheet makes you doubt; the solo-student and teacher runs are still yours.',
               '- **Exit check:** read checks.md made on the polished bundle. Gate items 6 (bundle, console, network) and 7 (voice counts) are the Contract and voice rows: confirm FAILs and LEADs only. Re-check the merged list and the frames tied to each fix yourself.',
               '- **Finish check:** run the pack again on the bundle with real art and clips. Step 5 (contract) and the counting half of step 3 (the voice check, clips recorded, every played line in lines.json) are here; clip timing by ear, art against the spec and the full runs are yours.', '',
               'A clean checks.md does not mean a clean tool. The script cannot see teaching, giveaways, feel, art, or whether a line is the right one for its moment.']
    (out / 'README.md').write_text('\n'.join(readme) + '\n', encoding='utf-8')
    print(f'{tool}: FAIL {C.count("FAIL")}, LEAD {C.count("LEAD")}, PASS {C.count("PASS")}, AGENT {C.count("AGENT")}; {total / 60:.1f} min; pack: {out}')


if __name__ == '__main__':
    sys.stdout.reconfigure(errors='replace')  # mode labels can hold glyphs a Windows console cannot print
    drive.PORT = int(flag('--port') or drive.PORT)
    drive.PROFILE = flag('--profile')
    audit = flag('--audit')
    opts = {'no_bundle': bool(flag('--no-bundle', False)), 'no_voice': bool(flag('--no-voice', False)), 'no_states': bool(flag('--no-states', False)),
            'max_controls': int(flag('--max-controls') or 24), 'budget': float(flag('--budget-min') or 25), 'jobs': int(flag('--jobs') or 4)}
    if len(sys.argv) != 3 or not drive.PROFILE:
        sys.exit(__doc__)
    if not Path(drive.PROFILE).is_absolute():
        sys.exit('--profile must be an absolute folder')
    try:
        asyncio.run(run(sys.argv[1], Path(sys.argv[2]).resolve(), Path(audit).resolve() if audit else None, opts))
    finally:
        drive.close_chrome()
