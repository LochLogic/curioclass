"""Render a frame of a tool with headless Chrome, for checking animation and layout.

    python scripts/shoot.py <tool-id> <name> ["<js to run>"] [--wait 3000] [--size 1400,900] [--freeze -0.25 | --settle] [--out DIR]

Loads tools/<id>/<id>.html with motion turned on, runs the JS after load, waits, then saves <out>/<name>.png.
--freeze pauses every CSS animation at that offset (seconds), so a mid-step pose can be inspected.
--settle shows every one-shot animation finished. Headless Chrome's virtual clock runs timers but can leave
CSS animations part way, so pop-ins look faded without it.
Output defaults to the folder in CURIO_SHOTS, else ./shots (gitignored).
"""
import argparse, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
          '/usr/bin/google-chrome', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tool'); ap.add_argument('name'); ap.add_argument('js', nargs='?', default='')
    ap.add_argument('--wait', type=int, default=3000); ap.add_argument('--size', default='1400,900')
    ap.add_argument('--freeze', type=float); ap.add_argument('--settle', action='store_true'); ap.add_argument('--out', default=os.environ.get('CURIO_SHOTS', str(ROOT / 'shots')))
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    src = (ROOT / 'tools' / a.tool / f'{a.tool}.html').read_text(encoding='utf-8')
    head = '<script>try{localStorage.setItem("curio-motion","on")}catch(e){}</script>'
    tail = ''
    if a.settle:
        a.freeze = -1000
    if a.freeze is not None:
        tail += f'<style>*{{animation-play-state:paused!important;animation-delay:{a.freeze}s!important}}</style>'
    if a.js:
        tail += f'<script>addEventListener("load",()=>setTimeout(async()=>{{{a.js}}},50))</script>'
    page = out / f'{a.name}.html'
    page.write_text(src.replace('<head>', '<head>' + head, 1).replace('</body>', tail + '</body>'), encoding='utf-8')
    chrome = next((c for c in CHROME if Path(c).exists()), None) or sys.exit('Chrome not found')
    png = out / f'{a.name}.png'
    subprocess.run([chrome, '--headless=new', '--mute-audio', '--disable-gpu', '--hide-scrollbars', f'--window-size={a.size}',
                    f'--virtual-time-budget={a.wait}', f'--screenshot={png}', page.resolve().as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(png if png.exists() else 'no screenshot written (under a sandbox, run Chrome from PowerShell Start-Process -Wait)')


if __name__ == '__main__':
    main()
