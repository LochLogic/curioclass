r"""Draw tool artwork on this PC with the local image model (FLUX.1-schnell in KoboldCpp), then finish it with art.py.

    python scripts/localart.py <tool-id> [asset names...] [--n 3] [--force]   draw candidates
    python scripts/localart.py <tool-id> --pick name:2 [name:1 ...]            use a candidate, cut out and size it

Reads the same tools/<tool-id>/art/prompts.json as art.py (house_style + prompt + the same cutout wording).
Candidates go to art/raw/<name>.c<k>.png with a contact sheet art/raw/_sheet-<name>.jpg. Nothing is used until it is
picked, so look at every candidate first. --pick copies the candidate to art/raw/<name>.png and runs art.py --rekey,
so the cutout, trim and sizing options work exactly as they do for Gemini art.

Model: FLUX.1-schnell Q6_K GGUF (Apache 2.0) with the T5-XXL fp8 and CLIP-L encoders and the FLUX VAE, in
S:\AI\models\flux, served by S:\AI\Start-FluxModel.bat on port 5002 (CURIO_SD_URL overrides). For many pictures at once,
scripts/fluxbatch.py draws from the same files without KoboldCpp, about twice as fast. Schnell is distilled:
4 steps, guidance 1, no negative prompt. Assets marked "people": true or "skip_local": true are never drawn here
(the first local model tried, a Pony SDXL merge, drew a 13-year-old in underwear; people get Gemini and a review).
Color codes are left out of the prompt: FLUX paints "#00FF00" into the picture as text.
"shadow": "dark" also removes a near-black cast shadow joined to the backdrop.
Per asset, "sd" replaces the prompt for this model only.
"""
import base64, io, json, os, subprocess, sys, time, urllib.request
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from art import CUTOUT, HOUSE_STYLE, KEYS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
URL = os.environ.get('CURIO_SD_URL', 'http://localhost:5002')
SIZES = {'1:1': (1024, 1024), '16:9': (1344, 768), '9:16': (768, 1344), '3:4': (896, 1152), '4:3': (1152, 896),
         '16:10': (1536, 960), '4:1': (1536, 384), '5:1': (1600, 320)}  # multiples of 64


def txt2img(prompt, w, h, seed):
    body = json.dumps({'prompt': prompt, 'width': w, 'height': h, 'steps': 4, 'cfg_scale': 1,
                       'sampler_name': 'Euler', 'seed': seed}).encode()
    req = urllib.request.Request(f'{URL}/sdapi/v1/txt2img', body, {'Content-Type': 'application/json'})
    return Image.open(io.BytesIO(base64.b64decode(json.load(urllib.request.urlopen(req, timeout=900))['images'][0])))


def build(spec, asset):
    style = asset.get('house_style', spec.get('house_style', HOUSE_STYLE))
    cut = CUTOUT.format(key=KEYS[asset.get('key', 'green')].split(' (')[0]) if asset.get('cutout') is True else ''
    return ' '.join(p for p in [style, asset.get('sd', asset['prompt']), cut, 'No people.'] if p)


def flatten_key(img, key, dark_shadow=False):
    """FLUX paints the key as a shaded backdrop with a soft shadow, not a flat color. Every key-tinted pixel
    connected to the border (backdrop, vignette and cast shadow, however dark) becomes the pure key, so art.py's
    distance key cuts it cleanly."""
    import numpy as np
    from scipy import ndimage
    a = np.asarray(img).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    tint = g - np.maximum(r, b) if key == 'green' else np.minimum(r, b) - g
    bg = tint > 10  # only areas touching the border, so a loose rule is safe
    labels, _ = ndimage.label(bg)
    edge = np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))
    bg = np.isin(labels, edge[edge > 0])
    # clearly tinted pockets too, like the gaps between an ant's legs, but not specks showing through a bee's wing
    pockets, n = ndimage.label((tint > 26) & ~bg)
    if n:
        sizes = ndimage.sum(np.ones(tint.shape), pockets, range(1, n + 1))
        bg |= np.isin(pockets, 1 + np.flatnonzero(sizes > tint.size * .0015))
    if dark_shadow:  # a near-black cast shadow joined to the backdrop (opt-in: it would eat a black ant)
        shade, n = ndimage.label(a.max(-1) < 90)
        touch = np.unique(shade[ndimage.binary_dilation(bg) & (shade > 0)])
        bg |= np.isin(shade, touch[touch > 0])
    out = a.copy()
    out[bg] = (0, 255, 0) if key == 'green' else (255, 0, 255)
    return Image.fromarray(out.astype(np.uint8))


def sheet(paths, out):
    ims = [Image.open(p).convert('RGB') for p in paths]
    H = 420
    ims = [i.resize((round(i.width * H / i.height), H)) for i in ims]
    c = Image.new('RGB', (sum(i.width for i in ims) + 10 * (len(ims) - 1), H), 'white')
    x = 0
    for i in ims:
        c.paste(i, (x, 0)); x += i.width + 10
    c.save(out, quality=85)


def main():
    args = sys.argv[1:]
    tool = args[0]
    art = ROOT / 'tools' / tool / 'art'
    raw = art / 'raw'; raw.mkdir(parents=True, exist_ok=True)
    spec = json.loads((art / 'prompts.json').read_text(encoding='utf-8'))
    if '--pick' in args:
        names = []
        for p in args[args.index('--pick') + 1:]:
            name, k = p.split(':')
            asset = next(a for a in spec['assets'] if a['name'] == name)
            img = Image.open(raw / f'{name}.c{k}.png').convert('RGB')
            if asset.get('cutout') is True:
                img = flatten_key(img, asset.get('key', 'green'), asset.get('shadow') == 'dark')
            elif 'black background' in asset['prompt']:  # shown with screen blending: near-black must be true black
                img = img.point(lambda v: max(0, round((v - 16) * 255 / 239)))
            img.save(raw / f'{name}.png')
            names.append(name)
            # record where the art came from and that it needs a look (scripts/artstatus.py tracks this)
            asset['source'] = 'gpt-image-2 (Codex)' if int(k) >= 20 else 'flux2-klein-4b (Cloudflare)' if int(k) >= 9 else 'flux1-schnell (local)'
            asset['review'] = 'pending'
        (art / 'prompts.json').write_text(json.dumps(spec, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'scripts' / 'art.py'), tool, *names, '--rekey'], check=True)
        return
    n = int(args[args.index('--n') + 1]) if '--n' in args else 3
    force = '--force' in args
    wanted = {a for a in args[1:] if not a.startswith('--') and not a.isdigit()}
    for asset in spec['assets']:
        name = asset['name']
        if wanted and name not in wanted:
            continue
        if asset.get('people') or asset.get('skip_local'):
            print(f'skip {name} (people are never drawn with the local model)'); continue
        if (art / f'{name}.webp').exists() and not force and not wanted:
            print(f'skip {name} (finished art exists)'); continue
        prompt = build(spec, asset)
        w, h = SIZES.get(asset.get('aspect', '1:1'), (1024, 1024))
        if asset.get('size') == '2K':  # a scene the tool zooms into
            w, h = w * 10 // 7 // 16 * 16, h * 10 // 7 // 16 * 16
        paths = []
        for k in range(1, n + 1):
            t = time.time()
            img = txt2img(prompt, w, h, seed=hash((name, k, time.time())) % 2**31)
            p = raw / f'{name}.c{k}.png'; img.save(p); paths.append(p)
            print(f'{name} c{k}: {time.time() - t:.0f}s', flush=True)
        sheet(paths, raw / f'_sheet-{name}.jpg')


if __name__ == '__main__':
    main()
