r"""Draw tool artwork with FLUX.2 [klein] 4B (Apache 2.0) on Cloudflare Workers AI, using the free daily allowance.

    python scripts/cfart.py <tool-id> [asset names...] [--n 1] [--k 9] [--ref name] [--force]
    python scripts/localart.py <tool-id> --pick name:9      cut out and size a candidate, as with local art

Same prompts.json and prompt wording as localart.py (house style + prompt + cutout wording + "No people.").
Candidates go to art/raw/<name>.c<k>.png (k starts at 9 so they don't overwrite local candidates) with a
contact sheet art/raw/_sheet-<name>-cf.jpg. --ref <asset> sends that asset's finished raw art (art/raw/<asset>.png)
as a reference image, so a character stays the same across poses.

Auth: the wrangler login (`npx wrangler login`, which has ai:write). The token is read from wrangler's config at
run time and never printed or stored. CURIO_CF_ACCOUNT sets the account id (otherwise taken from wrangler whoami).
Cost: a 1024x1024 image is 4 output tiles, about 104 of the 10,000 free neurons a day (about 95 images a day).
Assets marked "people" or "skip_local" are skipped here too: people come from Gemini with a review.
"""
import io, json, os, re, subprocess, sys, time
from pathlib import Path

import requests
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from localart import SIZES, build, sheet  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODEL = '@cf/black-forest-labs/flux-2-klein-4b'


def token():
    cfg = Path(os.environ.get('APPDATA', '')) / 'xdg.config' / '.wrangler' / 'config' / 'default.toml'
    if not cfg.exists():
        cfg = Path.home() / '.wrangler' / 'config' / 'default.toml'
    subprocess.run('npx wrangler whoami', shell=True, cwd=ROOT, capture_output=True)  # refreshes an expired token
    m = re.search(r'oauth_token\s*=\s*"([^"]+)"', cfg.read_text(encoding='utf-8'))
    if not m:
        sys.exit('no wrangler login found: run npx wrangler login')
    return m.group(1)


def account():
    if os.environ.get('CURIO_CF_ACCOUNT'):
        return os.environ['CURIO_CF_ACCOUNT']
    out = subprocess.run('npx wrangler whoami', shell=True, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    m = re.search(r'\b([0-9a-f]{32})\b', out)
    if not m:
        sys.exit('no account id: set CURIO_CF_ACCOUNT')
    return m.group(1)


def draw(tok, acct, prompt, w, h, refs=()):
    files = {'prompt': (None, prompt), 'width': (None, str(w)), 'height': (None, str(h))}
    for i, r in enumerate(refs):
        buf = io.BytesIO(); Image.open(r).convert('RGB').resize((768, 768)).save(buf, 'PNG')
        files[f'input_image_{i}'] = (f'ref{i}.png', buf.getvalue(), 'image/png')
    for attempt in range(4):
        resp = requests.post(f'https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/{MODEL}',
                             headers={'Authorization': f'Bearer {tok}'}, files=files, timeout=180)
        if resp.status_code == 200:
            import base64
            return Image.open(io.BytesIO(base64.b64decode(resp.json()['result']['image'])))
        if resp.status_code in (429, 500, 502, 503) and attempt < 3:
            time.sleep(10); continue
        if '"code":3030' in resp.text:  # Cloudflare's output filter flagged it: skip this one, keep going
            print('  flagged by the output filter; reword the prompt'); return None
        sys.exit(f'{resp.status_code}: {resp.text[:300]}')


def main():
    args = sys.argv[1:]
    tool = args[0]
    opt = lambda k, d: args[args.index(k) + 1] if k in args else d
    n, k0, ref = int(opt('--n', 1)), int(opt('--k', 9)), opt('--ref', None)
    art = ROOT / 'tools' / tool / 'art'
    raw = art / 'raw'; raw.mkdir(parents=True, exist_ok=True)
    spec = json.loads((art / 'prompts.json').read_text(encoding='utf-8'))
    skip = {opt('--n', ''), opt('--k', ''), opt('--ref', '')}
    wanted = {a for a in args[1:] if not a.startswith('--') and a not in skip}
    tok, acct = token(), account()
    for asset in spec['assets']:
        name = asset['name']
        if wanted and name not in wanted:
            continue
        if asset.get('people') or asset.get('skip_local'):
            print(f'skip {name} (people come from Gemini with a review)'); continue
        if (art / f'{name}.webp').exists() and '--force' not in args and not wanted:
            print(f'skip {name} (finished art exists)'); continue
        prompt = build(spec, asset)
        if ref:
            prompt = f'The same character as in the reference image, same colors and design. {prompt}'
        w, h = SIZES.get(asset.get('aspect', '1:1'), (1024, 1024))
        paths = []
        for k in range(k0, k0 + n):
            t = time.time()
            img = draw(tok, acct, prompt, w, h, [raw / f'{ref}.png'] if ref else [])
            if img is None:
                continue
            p = raw / f'{name}.c{k}.png'
            img.save(p); paths.append(p)
            print(f'{name} c{k}: {time.time() - t:.0f}s')
        if paths:
            sheet(paths, raw / f'_sheet-{name}-cf.jpg')


if __name__ == '__main__':
    main()
