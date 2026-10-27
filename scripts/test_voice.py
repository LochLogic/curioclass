r"""Test the kit's narration helper (Curio.voice) on kit/voice-test.html in muted headless Chrome.

    python scripts/test_voice.py [--profile DIR] [--port 9655] [--only R8]

Each rule runs in a fresh tab with real, held clicks (press, 120 ms, release) and prints PASS or FAIL. Every line in
the test page has a silent clip of a known length, so the page also records which clips really started, ended or were
cut; every rule checks that V.log's spoken lines match those clips exactly. Exit 1 on any failure.
Chrome gets its own absolute profile folder, --mute-audio, and is closed (only the process this script started).
"""
import argparse, asyncio, json, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path
import websockets

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / 'kit' / 'voice-test.html').as_uri()
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# steps: ('click', selector), ('key', 'Tab'), ('sleep', seconds), ('js', code). check: js returning [ok, detail].
# Lines: short clips play 0.5 s (+0.15 s gap), L.long 2 s. Helpers inside checks: spoken(text), plays(text), said(key).
H = """
const L = T.L, V = T.V;
const spoken = x => V.log.filter(e => e.as === 'spoken' && e.text === x).length;
const silent = x => V.log.filter(e => e.as === 'silent' && e.text === x).length;
const dropped = x => V.log.filter(e => e.as === 'dropped' && e.text === x);
const plays = x => T.plays.filter(p => p.text === x).length;
const P = T.plays.map(p => p.text);
"""
RULES = [
    ('R1 nothing speaks before the first tap; a line before it is hint only, unmarked',
     [('sleep', 1.5)],
     "return [T.plays.length === 0 && silent(L.start) === 1 && V.log.some(e => e.why === 'early') && !V.said.has(L.start)"
     " && $('hint').textContent === L.start, {plays: P, log: V.log}]"),
    ('R2 first tap on the stage queues the mode welcome, promptly',
     [('click', '#stage'), ('sleep', 1.2)],
     "const w = T.plays.find(p => p.text === L.wa);"
     "return [P.join('|') === L.wa && V.said.has('w-a') && w.t - T.tapAt < 400, {plays: P, ms: w && w.t - T.tapAt}]"),
    ('R3 first tap whose own line already left the queue skips the welcome (game-remix N2)',
     [('click', '#solo'), ('sleep', 1.5)],
     "return [P.join('|') === L.nice && !V.said.has('w-a') && T.atDecide.queue === 0 && T.atDecide.playing === L.nice,"
     " {plays: P, atDecide: T.atDecide}]"),
    ('R4 a skipped welcome stays unmarked and plays at the next mode entry',
     [('click', '#solo'), ('sleep', 1), ('click', '#m-b'), ('sleep', 2), ('click', '#m-a'), ('sleep', 1.2)],
     "return [plays(L.wa) === 1 && P[P.length - 1] === L.wa && plays(L.wb) === 1 && plays(L.wb2) === 1, {plays: P}]"),
    ('R5 Read as the first tap reads the hint and skips the welcome; Sound off and on queues it',
     [('click', '#read'), ('sleep', 1.2), ('js', 'T.mid = T.plays.map(p => p.text)'), ('click', '#sound'), ('sleep', .3),
      ('click', '#sound'), ('sleep', 1.4)],
     "return [T.mid.join('|') === L.start && P.join('|') === L.start + '|' + L.wa"
     " && V.log.some(e => e.as === 'read' && e.text === L.start), {mid: T.mid, plays: P}]"),
    ('R6 Sound as the first tap skips the welcome; Sound back on queues it once',
     [('click', '#sound'), ('sleep', .6), ('js', 'T.mid = T.plays.length'), ('click', '#sound'), ('sleep', 1.2),
      ('click', '#sound'), ('sleep', .3), ('click', '#sound'), ('sleep', 1.2)],
     "return [T.mid === 0 && P.join('|') === L.wa, {mid: T.mid, plays: P}]"),
    ('R7 a control that brings its own line later (speaks) skips the welcome',
     [('click', '#slow'), ('sleep', 1.6)],
     "return [P.join('|') === L.slow && !V.said.has('w-a'), {plays: P}]"),
    ('R8 five held repeats: the result every time, the how-to once, then hint only',
     [('click', '#stage'), ('sleep', 1.2)] + [('click', '#act'), ('sleep', 1.5)] * 5,
     "return [spoken(L.nice) === 5 && spoken(L.howAct) === 1 && silent(L.howAct) === 4 && plays(L.howAct) === 1"
     " && $('hint').textContent === L.howAct, {nice: spoken(L.nice), how: spoken(L.howAct), silent: silent(L.howAct)}]"),
    ('R9 a failure line ("that code doesn\'t work") is heard all five times',
     [('click', '#fail'), ('sleep', 1.5)] * 5,
     "return [spoken(L.fail) === 5 && plays(L.fail) === 5 && spoken(L.howFix) === 1, {fail: spoken(L.fail), how: spoken(L.howFix)}]"),
    ('R10 a line naming a control that is off is dropped unmarked, then plays once the control is on',
     [('js', "$('fix').disabled = true"), ('click', '#fail'), ('sleep', 1.5), ('js', "$('fix').disabled = false"),
      ('click', '#fail'), ('sleep', 1.5)],
     "const d = dropped(L.howFix);"
     "return [d.length === 1 && d[0].why === 'stale' && spoken(L.howFix) === 1 && plays(L.howFix) === 1, {dropped: d, plays: P}]"),
    ('R11 a stale line is dropped when its turn comes, not when queued (both kinds)',
     [('click', '#stage'), ('sleep', 1.0), ('js', "V.say(L.long); V.how(L.stale, {valid: () => T.state.light}); V.say(L.two, {valid: () => T.state.light});"
      " setTimeout(() => { T.state.light = false; }, 500)"), ('sleep', 2.8),
      ('js', "T.state.light = true; V.how(L.stale)"), ('sleep', 1)],
     "return [dropped(L.stale).length === 1 && dropped(L.stale)[0].why === 'stale' && dropped(L.two).length === 1"
     " && spoken(L.stale) === 1 && plays(L.two) === 0, {plays: P}]"),
    ('R12 lines play in the order they were queued',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.one); V.say(L.two); V.say(L.three)'), ('sleep', 2.4)],
     "return [P.join('|') === [L.nice, L.one, L.two, L.three].join('|'), {plays: P}]"),
    ('R13 a how-to is marked said when it plays, never when queued',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long); V.how(L.stale)'), ('sleep', .4),
      ('js', 'T.mid = V.said.has(L.stale); V.hush()'), ('sleep', .2), ('js', 'V.how(L.stale)'), ('sleep', 1)],
     "return [T.mid === false && dropped(L.stale)[0].why === 'hush' && spoken(L.stale) === 1 && plays(L.stale) === 1, {plays: P}]"),
    ('R14 hush stops everything, including the clip in progress; the next line starts at once',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long); V.say(L.one)'), ('sleep', .5),
      ('js', 'T.hushAt = performance.now(); V.hush(); V.say(L.two)'), ('sleep', 1)],
     "const two = T.plays.find(p => p.text === L.two);"
     "return [T.pauses.some(p => p.text === L.long) && plays(L.one) === 0 && two && two.t - T.hushAt < 250 && !T.ends.some(e => e.text === L.long),"
     " {plays: P, ms: two && two.t - T.hushAt}]"),
    ('R14b hush alone (a reset, nothing after it) silences the clip in progress',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long)'), ('sleep', .5), ('js', 'V.hush()'), ('sleep', 2)],
     "return [T.pauses.some(p => p.text === L.long) && !T.ends.some(e => e.text === L.long) && V.playing === null, {plays: P, ends: T.ends}]"),
    ('R15 dropQueued: a newer action drops older queued lines; the line in progress plays on',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long); V.say(L.one); V.say(L.two)'), ('sleep', .3),
      ('js', 'V.dropQueued(); V.say(L.three)'), ('sleep', 2.6)],
     "return [P.join('|') === [L.nice, L.long, L.three].join('|') && T.ends.some(e => e.text === L.long)"
     " && dropped(L.one)[0].why === 'newer' && !T.pauses.some(p => p.text === L.long), {plays: P}]"),
    ('R16 Read with Sound off speaks the current hint',
     [('click', '#sound'), ('js', "$('hint').textContent = L.two"), ('click', '#read'), ('sleep', 1)],
     "return [P.join('|') === L.two && V.tapped, {plays: P}]"),
    ('R17 Read stops the queue first; a line queued during Read waits for it to end',
     [('click', '#stage'), ('sleep', .2), ('js', 'V.say(L.one)'), ('click', '#read'), ('sleep', .1), ('js', 'V.say(L.two)'), ('sleep', 2)],
     "const rd = T.plays.filter(p => p.text === L.wa)[1], re = T.ends.find(e => e.text === L.wa), two = T.plays.find(p => p.text === L.two);"
     "return [plays(L.one) === 0 && plays(L.wa) === 2 && T.pauses.some(p => p.text === L.wa) && two && re && two.t >= re.t, {plays: P, readEnd: re && re.t, two: two && two.t}]"),
    ('R18 nothing waits on a stopped Read: after Read and a hush, the next line starts at once',
     [('click', '#solo'), ('sleep', .9), ('js', "$('hint').textContent = L.long"), ('click', '#read'), ('sleep', .3),
      ('js', 'T.hushAt = performance.now(); V.hush(); V.say(L.one)'), ('sleep', .8)],
     "const one = T.plays.find(p => p.text === L.one);"
     "return [one && one.t - T.hushAt < 250 && T.pauses.some(p => p.text === L.long), {plays: P, ms: one && one.t - T.hushAt}]"),
    ('R19 one welcome per mode, said once (a list of keys too); re-entry says the how-to once',
     [('click', '#m-b'), ('sleep', 2.2), ('click', '#m-a'), ('sleep', 1.4), ('click', '#m-b'), ('sleep', 1), ('click', '#m-a'), ('sleep', 1)],
     "return [plays(L.wa) === 1 && plays(L.wb) === 1 && plays(L.wb2) === 1 && spoken(L.howAct) === 1 && silent(L.howAct) === 1, {plays: P}]"),
    ('R20 Sound off: the hint still updates and say(wait) paces an estimated time',
     [('click', '#sound'), ('js', 'const t0 = performance.now(); T.r = await V.say(L.long, {wait: true}); T.el = performance.now() - t0')],
     "const est = 600 + 62 * L.long.length;"
     "return [T.r === 'silent' && $('hint').textContent === L.long && Math.abs(T.el - est) < 150 && T.plays.length === 0, {r: T.r, ms: Math.round(T.el), est}]"),
    ('R21 say(..., {wait: true}) resolves when the line has been said, or at once when skipped',
     [('click', '#solo'), ('sleep', .9), ('js', 'let t0 = performance.now(); T.r = await V.say(L.long, {wait: true}); T.el = performance.now() - t0;'
      't0 = performance.now(); T.r2 = await V.say(L.one, {wait: true, valid: () => false}); T.el2 = performance.now() - t0')],
     "const e = T.ends.find(x => x.text === L.long);"
     "return [T.r === 'spoken' && e && T.el > 2000 && T.el < 2600 && T.r2 === 'dropped' && T.el2 < 50, {r: T.r, ms: Math.round(T.el), r2: T.r2, ms2: Math.round(T.el2)}]"),
    ('R22 maxAge: a game beat that waited too long is dropped',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long); V.say(L.one, {maxAge: 500}); V.say(L.two, {maxAge: 5000})'), ('sleep', 3)],
     "return [plays(L.one) === 0 && dropped(L.one)[0].why === 'stale' && plays(L.two) === 1, {plays: P}]"),
    ('R23 now: a line that must be heard now cuts in (music, Pause/Step)',
     [('click', '#solo'), ('sleep', .9), ('js', 'V.say(L.long); V.say(L.two)'), ('sleep', .4),
      ('js', 'T.at = performance.now(); T.r = await V.say(L.one, {now: true, wait: true})')],
     "const one = T.plays.find(p => p.text === L.one);"
     "return [T.r === 'spoken' && one.t - T.at < 250 && T.pauses.some(p => p.text === L.long) && plays(L.two) === 0, {plays: P, ms: Math.round(one.t - T.at)}]"),
    ('R24 a first key counts as the first tap',
     [('key', 'Tab'), ('sleep', 1.2)],
     "return [P.join('|') === L.wa, {plays: P}]"),
]
# every rule also checks: V.log's spoken lines (and Reads) are exactly the clips that started, in order
INVARIANT = ("const lg = V.log.filter(e => e.as === 'spoken' || e.as === 'read').map(e => e.text);"
             "const okLog = lg.join('|') === P.join('|') && V.log.every(e => typeof e.t === 'number' && e.text != null && e.kind && ['spoken','silent','dropped','read'].includes(e.as))"
             " && Array.isArray(V.queue);")


class Tab:
    def __init__(self, ws):
        self.ws, self.i, self.pending, self.events = ws, 0, {}, []

    async def reader(self):
        async for msg in self.ws:
            m = json.loads(msg)
            if 'id' in m and m['id'] in self.pending:
                self.pending.pop(m['id']).set_result(m)
            else:
                self.events.append(m)

    async def send(self, method, **params):
        self.i += 1
        f = asyncio.get_event_loop().create_future(); self.pending[self.i] = f
        await self.ws.send(json.dumps({'id': self.i, 'method': method, 'params': params}))
        r = await asyncio.wait_for(f, 60)
        if 'error' in r:
            raise RuntimeError(f'{method}: {r["error"]}')
        return r.get('result', {})

    async def js(self, code):
        r = await self.send('Runtime.evaluate', expression=f'(async()=>{{{code}}})()', awaitPromise=True, returnByValue=True)
        if r.get('exceptionDetails'):
            raise RuntimeError('js: ' + json.dumps(r['exceptionDetails'])[:400])
        return r.get('result', {}).get('value')


async def run_rule(port, name, steps, check):
    req = urllib.request.Request(f'http://127.0.0.1:{port}/json/new?about:blank', method='PUT')
    info = json.loads(urllib.request.urlopen(req).read())
    try:
        async with websockets.connect(info['webSocketDebuggerUrl'], max_size=2**26) as ws:
            t = Tab(ws); rd = asyncio.create_task(t.reader())
            for d in ['Page', 'Runtime']:
                await t.send(d + '.enable')
            await t.send('Emulation.setDeviceMetricsOverride', width=1000, height=700, deviceScaleFactor=1, mobile=False)
            await t.send('Page.navigate', url=PAGE)
            for _ in range(50):
                await asyncio.sleep(.1)
                try:
                    if await t.js('return !!(window.T && T.V)'):
                        break
                except Exception:
                    pass
            await asyncio.sleep(.3)
            for st in steps:
                kind, arg = st
                if kind == 'sleep':
                    await asyncio.sleep(arg)
                elif kind == 'js':
                    await t.js(H.replace('const P', 'let P') + arg)
                elif kind == 'click':   # a real held click: press, 120 ms, release
                    x, y = await t.js(f'const b = document.querySelector("{arg}").getBoundingClientRect(); return [b.x + b.width / 2, b.y + b.height / 2]')
                    await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y)
                    await t.send('Input.dispatchMouseEvent', type='mousePressed', x=x, y=y, button='left', buttons=1, clickCount=1)
                    await asyncio.sleep(.12)
                    await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=x, y=y, button='left', clickCount=1)
                elif kind == 'key':
                    await t.send('Input.dispatchKeyEvent', type='rawKeyDown', key=arg, code=arg, windowsVirtualKeyCode=9)
                    await asyncio.sleep(.08)
                    await t.send('Input.dispatchKeyEvent', type='keyUp', key=arg, code=arg, windowsVirtualKeyCode=9)
            res = await t.js(H + INVARIANT + "const [ok, d] = (() => {" + check + "})(); return [ok && okLog, d, okLog, lg, P];")
            errs = [e for e in t.events if e.get('method') == 'Runtime.exceptionThrown']
            rd.cancel()
            ok, detail, ok_log, lg, plays = res
            if errs:
                ok, detail = False, {'exception': json.dumps(errs[0]['params']['exceptionDetails'])[:300]}
            if not ok_log:
                detail = {'log/clip mismatch': {'log': lg, 'clips': plays}}
            return ok, detail
    finally:
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{port}/json/close/{info["id"]}', timeout=3)
        except Exception:
            pass


async def main(port, only):
    fails = 0
    for name, steps, check in RULES:
        if only and not name.split()[0] == only:
            continue
        try:
            ok, detail = await run_rule(port, name, steps, check)
        except Exception as ex:
            ok, detail = False, repr(ex)
        fails += not ok
        print(f'{"PASS" if ok else "FAIL"}  {name}' + ('' if ok else f'\n      {json.dumps(detail)[:900]}'), flush=True)
    print(f'{len(RULES) - fails if not only else ""} passed, {fails} failed' if not only else f'{fails} failed')
    return fails


def up(port):
    try:
        urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=1); return True
    except Exception:
        return False


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--profile', default=str(Path(tempfile.gettempdir()) / 'curio-voicetest'))
    ap.add_argument('--port', type=int, default=9655)
    ap.add_argument('--only')
    a = ap.parse_args()
    prof = Path(a.profile).resolve()   # Chrome needs an absolute profile folder
    prof.mkdir(parents=True, exist_ok=True)
    if up(a.port):
        sys.exit(f'port {a.port} is already in use by another Chrome: not touching it')
    proc = subprocess.Popen([CHROME, '--headless=new', '--mute-audio', '--disable-gpu', f'--remote-debugging-port={a.port}',
                             f'--user-data-dir={prof}', '--no-first-run', '--autoplay-policy=no-user-gesture-required',
                             '--allow-file-access-from-files', 'about:blank'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(60):
            if up(a.port):
                break
            time.sleep(.2)
        else:
            sys.exit('chrome did not start')
        fails = asyncio.run(main(a.port, a.only))
    finally:   # close only the Chrome this script started
        proc.terminate()
        try:
            proc.wait(10)
        except Exception:
            proc.kill()
    sys.exit(1 if fails else 0)
