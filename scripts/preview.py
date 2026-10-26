r"""Make a tool's card art (tools/<id>/preview.svg): a 16:10 screenshot of the bundled tool, as a small WebP in an SVG.

    python scripts/preview.py <tool-id> [...] ["--js=<js run after load>"] [--wait 3000]
    python scripts/preview.py --missing        every built tool (tool.json) that has no preview.svg yet

Shoots tools/<id>/<id>.html at 1280x800 with scripts/shoot.py (muted headless Chrome), scales it to 640x400 and wraps it
the way the site expects (docs/TOOL-CONTRACT.md: "card art, 16:10"). Without one, the site shows a play-style pattern.
Look at the result: a default screen that is mostly a menu makes a weak card; pass --js to open a livelier screen.
"""
import base64, io, subprocess, sys, tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def make(tool, js='', wait=3000):
    with tempfile.TemporaryDirectory() as out:
        subprocess.run([sys.executable, str(ROOT / 'scripts' / 'shoot.py'), tool, 'card', js, '--wait', str(wait),
                        '--size', '1280,800', '--out', out], check=True, capture_output=True)
        img = Image.open(Path(out) / 'card.png').convert('RGB').resize((640, 400), Image.LANCZOS)
    buf = io.BytesIO(); img.save(buf, 'WEBP', quality=72)
    b64 = base64.b64encode(buf.getvalue()).decode()
    (ROOT / 'tools' / tool / 'preview.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400"><image href="data:image/webp;base64,{b64}" '
        f'width="640" height="400"/></svg>', encoding='utf-8')
    print(f'{tool}: preview.svg {len(buf.getvalue()) // 1024} KB')


def main():
    argv = sys.argv[1:]
    args = [a for i, a in enumerate(argv) if not a.startswith('--') and (i == 0 or argv[i - 1] != '--wait')]
    js = next((a[5:] for a in sys.argv[1:] if a.startswith('--js=')), '')
    wait = int(sys.argv[sys.argv.index('--wait') + 1]) if '--wait' in sys.argv else 3000
    if '--missing' in sys.argv:
        args = sorted(d.name for d in (ROOT / 'tools').iterdir()
                      if (d / 'tool.json').exists() and not (d / 'preview.svg').exists())
    for t in args:
        make(t, js, wait)


if __name__ == '__main__':
    main()
