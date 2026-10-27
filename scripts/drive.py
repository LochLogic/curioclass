r"""Drive a bundled tool in muted headless Chrome over CDP: frames, real input, console errors.

    python scripts/drive.py <tool-id> shots.json <outdir>

shots.json is a list of shots, run in order, each in a fresh tab:
  {"name": "default", "w": 1280, "h": 720,      required
   "js": "...",            run after load (async; its return value is printed)
   "clicks": ["#run"],     real mouse clicks on CSS selectors; "hold": 0.12 holds each press (test voice with held clicks),
                           "gap": seconds between clicks
   "xy": [[x, y], ...],    real clicks at points
   "drag": "js returning [[x,y],...]"   a real mouse drag along the points (20 ms apart)
   "keys": ["Tab", "S-ArrowRight", "Enter"]   real keys (S- = Shift)
   "after": "...",         js run after the input, before the shot
   "wait": 300, "calm": false, "mobile": false, "full": false,
   "url": "http://127.0.0.1:8790/host.html?w=375"   instead of the tool file (narrow widths: see --host)
   "save": "path.json"}    write the js result to a file
Prints each shot's js result and any console errors, warnings or exceptions (shoot.py does not), saves <name>.png.
Chrome starts with --mute-audio (clips still play silently with real timing) and is closed at the end. If a Chrome is
already listening on the port, it is used and left running (it is not this script's to close).

    python scripts/drive.py <tool-id> shots.json <outdir> [--port 9383] [--profile <absolute dir>]
      --port: Chrome's debugging port (default 9383); --profile: Chrome's profile folder (default <outdir>/../chrome-prof).
      Only the Chrome this script starts is closed at the end, with its child processes (taskkill /T on Windows).

    python scripts/drive.py <tool-id> --host [port]   serve tools/<id>/ over http with host.html?w=375&h=812, an iframe
                                                     host page: headless Chrome will not go narrower than about 520 px
"""
import asyncio, json, os, sys, subprocess, base64, time, urllib.request
from pathlib import Path
import websockets

PORT = 9383
ROOT = Path(__file__).resolve().parent.parent
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TOOL = None  # set from the command line
PROFILE = None  # --profile: an absolute folder for Chrome's profile (default: next to the output folder)


def ensure_chrome(prof):
    global CHROME_PROC
    try:
        urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json/version', timeout=1); return
    except Exception:
        pass
    CHROME_PROC = subprocess.Popen([CHROME, '--headless=new', '--mute-audio', '--disable-gpu', '--hide-scrollbars', f'--remote-debugging-port={PORT}',
                      f'--user-data-dir={prof}', '--no-first-run', '--autoplay-policy=no-user-gesture-required', 'about:blank'],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(50):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json/version', timeout=1); return
        except Exception:
            time.sleep(.2)
    sys.exit('chrome did not start')


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


async def main(shots, out):
    out.mkdir(parents=True, exist_ok=True)
    ensure_chrome(Path(PROFILE).resolve() if PROFILE else out.resolve().parent / 'chrome-prof')  # Chrome can't use a relative profile folder: it shows a "Failed To Create Data Directory" box and exits
    errors = {}
    for s in shots:
        req = urllib.request.Request(f'http://127.0.0.1:{PORT}/json/new?about:blank', method='PUT')
        info = json.loads(urllib.request.urlopen(req).read())
        try:
            async with websockets.connect(info['webSocketDebuggerUrl'], max_size=2**28) as ws:
                t = Tab(ws); rd = asyncio.create_task(t.reader())
                for d in ['Page', 'Runtime', 'Log']:
                    await t.send(d + '.enable')
                await t.send('Emulation.setDeviceMetricsOverride', width=s['w'], height=s['h'], deviceScaleFactor=1, mobile=bool(s.get('mobile')))
                calm = s.get('calm', False)
                await t.send('Page.addScriptToEvaluateOnNewDocument', source=f'try{{localStorage.setItem("curio-motion","{"calm" if calm else "on"}")}}catch(e){{}}')
                url = s['url'] if s.get('url','').startswith('http') else Path(s.get('url', str(TOOL))).resolve().as_uri()
                await t.send('Page.navigate', url=url)
                await asyncio.sleep(1.2)
                res = None
                if s.get('js'):
                    r = await t.send('Runtime.evaluate', expression=f'(async()=>{{{s["js"]}}})()', awaitPromise=True, returnByValue=True)
                    res = r.get('result', {}).get('value')
                    if r.get('exceptionDetails'):
                        res = 'EXC: ' + json.dumps(r['exceptionDetails'])[:600]
                if s.get('drag'):
                    r = await t.send('Runtime.evaluate', expression=s['drag'], returnByValue=True)
                    pts = r['result']['value']
                    await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=pts[0][0], y=pts[0][1])
                    await t.send('Input.dispatchMouseEvent', type='mousePressed', x=pts[0][0], y=pts[0][1], button='left', clickCount=1)
                    for x, y in pts[1:]:
                        await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y, button='left', buttons=1)
                        await asyncio.sleep(.02)
                    await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=pts[-1][0], y=pts[-1][1], button='left', clickCount=1)
                if s.get('clicks'):
                    for sel in s['clicks']:
                        r = await t.send('Runtime.evaluate', expression=f'(()=>{{const b=document.querySelector("{sel}").getBoundingClientRect();return [b.x+b.width/2,b.y+b.height/2]}})()', returnByValue=True)
                        x, y = r['result']['value']
                        await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y)
                        await t.send('Input.dispatchMouseEvent', type='mousePressed', x=x, y=y, button='left', buttons=1, clickCount=1)
                        await asyncio.sleep(s.get('hold', 0))
                        await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=x, y=y, button='left', clickCount=1)
                        await asyncio.sleep(s.get('gap', .5))
                for x, y in s.get('xy', []):
                    await t.send('Input.dispatchMouseEvent', type='mouseMoved', x=x, y=y)
                    await t.send('Input.dispatchMouseEvent', type='mousePressed', x=x, y=y, button='left', buttons=1, clickCount=1)
                    await asyncio.sleep(.12)
                    await t.send('Input.dispatchMouseEvent', type='mouseReleased', x=x, y=y, button='left', clickCount=1)
                    await asyncio.sleep(s.get('gap', .5))
                KM = {'Tab': (9, 'Tab', None), 'ArrowRight': (39, 'ArrowRight', None), 'ArrowLeft': (37, 'ArrowLeft', None), 'ArrowUp': (38, 'ArrowUp', None),
                      'ArrowDown': (40, 'ArrowDown', None), 'Enter': (13, 'Enter', chr(13)), 'Escape': (27, 'Escape', None), 'Delete': (46, 'Delete', None),
                      '[': (219, 'BracketLeft', '['), ']': (221, 'BracketRight', ']'), '=': (187, 'Equal', '='), '-': (189, 'Minus', '-'), ' ': (32, 'Space', ' ')}
                for k in s.get('keys', []):
                    shift = k.startswith('S-'); kk = k[2:] if shift else k
                    code, cname, text = KM[kk]
                    mods = 8 if shift else 0
                    if text:
                        await t.send('Input.dispatchKeyEvent', type='keyDown', key=kk, code=cname, windowsVirtualKeyCode=code, text=text, modifiers=mods)
                    else:
                        await t.send('Input.dispatchKeyEvent', type='rawKeyDown', key=kk, code=cname, windowsVirtualKeyCode=code, modifiers=mods)
                    await t.send('Input.dispatchKeyEvent', type='keyUp', key=kk, code=cname, windowsVirtualKeyCode=code, modifiers=mods)
                    await asyncio.sleep(s.get('kgap', .08))
                if s.get('after'):
                    r = await t.send('Runtime.evaluate', expression=f'(async()=>{{{s["after"]}}})()', awaitPromise=True, returnByValue=True)
                    res = [res, r.get('result', {}).get('value')]
                await asyncio.sleep(s.get('wait', 300) / 1000)
                shot = await t.send('Page.captureScreenshot', format='png', captureBeyondViewport=bool(s.get('full')))
                (out / f'{s["name"]}.png').write_bytes(base64.b64decode(shot['data']))
                errs = []
                for e in t.events:
                    if e.get('method') == 'Runtime.exceptionThrown':
                        errs.append('EXC ' + json.dumps(e['params']['exceptionDetails'])[:500])
                    elif e.get('method') == 'Runtime.consoleAPICalled' and e['params']['type'] in ('error', 'warning', 'assert'):
                        errs.append('CONSOLE ' + ' '.join(str(a.get('value', a.get('description', ''))) for a in e['params']['args'])[:400])
                    elif e.get('method') == 'Log.entryAdded' and e['params']['entry']['level'] in ('error', 'warning') and 'AudioContext was not allowed' not in e['params']['entry'].get('text', ''):
                        errs.append('LOG ' + e['params']['entry'].get('text', '')[:300] + ' ' + e['params']['entry'].get('url', ''))
                print(f'{s["name"]}: {json.dumps(res)[:1500] if res is not None else ""}', flush=True)
                if s.get('save'): Path(s['save']).write_text(json.dumps(res), encoding='utf-8')
                if errs:
                    print('   ERRORS:', *errs, sep=chr(10) + '     ')
                    errors[s['name']] = errs
                rd.cancel()
        except Exception as ex:
            print(f'{s["name"]}: DRIVER FAIL {ex!r}', flush=True); errors[s['name']] = ['driver']
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json/close/{info["id"]}', timeout=3)
        except Exception:
            pass
    print('errors in', len(errors), 'shots')
    close_chrome()


def close_chrome():
    """Close the Chrome this script started (only that one): on Windows terminate() leaves headless children on the port."""
    global CHROME_PROC
    if not CHROME_PROC:
        return
    if os.name == 'nt':
        subprocess.run(['taskkill', '/T', '/F', '/PID', str(CHROME_PROC.pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        CHROME_PROC.terminate()
    try:
        CHROME_PROC.wait(10)
    except Exception:
        CHROME_PROC.kill()
    CHROME_PROC = None


HOST = """<!doctype html><meta charset=utf-8><style>body{margin:0;background:#888}iframe{border:0;display:block;background:#fff}</style>
<script>const q=new URLSearchParams(location.search);document.write(`<iframe src="TOOL.html" width="${q.get('w')||375}" height="${q.get('h')||812}"></iframe>`)</script>"""


def host(tool, port):
    import http.server, functools, os
    d = ROOT / 'tools' / tool
    (d / 'host.html').write_text(HOST.replace('TOOL', tool), encoding='utf-8')
    print(f'http://127.0.0.1:{port}/host.html?w=375&h=812  (Ctrl+C to stop; delete tools/{tool}/host.html after)')
    http.server.ThreadingHTTPServer(('127.0.0.1', port), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(d))).serve_forever()


CHROME_PROC = None
def flag(name):
    """Take --name value out of sys.argv (so the positional arguments stay as they were)."""
    if name not in sys.argv:
        return None
    i = sys.argv.index(name)
    v = sys.argv[i + 1]
    del sys.argv[i:i + 2]
    return v


if __name__ == '__main__':
    if '--host' not in sys.argv:
        PORT = int(flag('--port') or PORT)
        PROFILE = flag('--profile')
        if PROFILE and not Path(PROFILE).is_absolute():
            sys.exit('--profile must be an absolute folder')
    tool = sys.argv[1]
    if '--host' in sys.argv:
        host(tool, int(sys.argv[sys.argv.index('--host') + 1]) if len(sys.argv) > 3 else 8790)
    else:
        TOOL = ROOT / 'tools' / tool / f'{tool}.html'
        try:
            asyncio.run(main(json.loads(Path(sys.argv[2]).read_text(encoding='utf-8')), Path(sys.argv[3])))
        finally:
            close_chrome()
