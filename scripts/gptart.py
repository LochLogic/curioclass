r"""Draw tool artwork with gpt-image-2 through the Codex CLI, on Cory's ChatGPT subscription (no API key).

    python scripts/gptart.py <tool-id> [asset names...] [--n 1] [--k 20] [--ref name]
    python scripts/localart.py <tool-id> --pick name:20      cut out and size a candidate, as with other art

Same prompts.json and prompt wording as art.py (house style + tool style + prompt + cutout wording), so it suits the
hard cases: hands, tricky objects, and people (people still get a review of every image, like Gemini art).
Candidates go to art/raw/<name>.c<k>.png (k starts at 20, clear of local c1-8 and Cloudflare c9-19) with a contact
sheet art/raw/_sheet-<name>-gpt.jpg. --ref <asset> attaches that asset's finished raw art (art/raw/<asset>.png).

How: each image is one `codex exec` run (read-only sandbox, ephemeral session) asked only to call its image tool.
Codex saves the picture under ~/.codex/generated_images; the newest file made during the run is the candidate.
Sign-in: `codex login` with the ChatGPT account (done once, stored by Codex, never read here).
Cost: image turns use the plan's Codex allowance 3-5x faster than plain turns. When the limit is hit, codex
exits with a usage message and this script stops; the allowance refills on the plan's own schedule.
"""
import json, os, shutil, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from art import CUTOUT, HOUSE_STYLE, KEYS  # noqa: E402
from localart import sheet  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GEN = Path.home() / '.codex' / 'generated_images'
SHAPE = {'1:1': 'square', '16:9': 'wide landscape (3:2)', '4:3': 'landscape (3:2)', '9:16': 'tall portrait (2:3)', '3:4': 'portrait (2:3)'}
CODEX = shutil.which('codex') or 'codex'


def prompt_for(spec, asset, ref):
    style = '' if asset.get('skip_style') else spec.get('style', '')
    cut = CUTOUT.format(key=KEYS[asset.get('key', 'green')]) if asset.get('cutout') is True else ''
    p = ' '.join(x for x in [asset.get('house_style', spec.get('house_style', HOUSE_STYLE)), style, asset['prompt'], cut] if x)
    if ref:
        p += ' Match the character design, colors and drawing style of the attached reference image exactly.'
    return p


def draw(prompt, shape, refs, work):
    start = time.time()
    ask = (f'Use your image generation tool to make exactly one {shape} image from this description, used word for word '
           f'as the image prompt. Do not run commands, edit files or explain.\n\n{prompt}')
    cmd = [CODEX, 'exec', '--skip-git-repo-check', '--ephemeral', '-s', 'read-only', '-C', str(work)]
    for r in refs:
        cmd += ['-i', str(r)]
    out = subprocess.run(cmd + ['-'], input=ask, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=900)
    made = sorted((p for p in GEN.rglob('*.png') if p.stat().st_mtime >= start - 1), key=lambda p: p.stat().st_mtime)
    if made:
        return made[-1]
    tail = (out.stdout + out.stderr)[-600:]
    if any(w in tail.lower() for w in ('usage limit', 'rate limit', 'quota')):
        sys.exit('Codex usage limit reached; it refills on the ChatGPT plan schedule')
    print(f'  no image came back:\n{tail}')
    return None


def main():
    args = sys.argv[1:]
    tool = args[0]
    opt = lambda k, d: args[args.index(k) + 1] if k in args else d
    n, k0, ref = int(opt('--n', 1)), int(opt('--k', 20)), opt('--ref', None)
    art = ROOT / 'tools' / tool / 'art'
    raw = art / 'raw'; raw.mkdir(parents=True, exist_ok=True)
    spec = json.loads((art / 'prompts.json').read_text(encoding='utf-8'))
    skip = {opt('--n', ''), opt('--k', ''), opt('--ref', '')}
    wanted = {a for a in args[1:] if not a.startswith('--') and a not in skip}
    work = Path(os.environ.get('TEMP', str(raw))) / 'gptart'; work.mkdir(exist_ok=True)
    for asset in spec['assets']:
        name = asset['name']
        if wanted and name not in wanted:
            continue
        if (art / f'{name}.webp').exists() and not wanted:
            print(f'skip {name} (finished art exists)'); continue
        r = ref or asset.get('ref')
        refs = [raw / f'{r}.png'] if r else []
        prompt, shape = prompt_for(spec, asset, r), SHAPE.get(asset.get('aspect', '1:1'), 'square')
        paths = []
        for k in range(k0, k0 + n):
            t = time.time()
            src = draw(prompt, shape, refs, work)
            if src is None:
                continue
            p = raw / f'{name}.c{k}.png'
            shutil.copyfile(src, p); paths.append(p)
            print(f'{name} c{k}: {time.time() - t:.0f}s', flush=True)
        if paths:
            sheet(paths, raw / f'_sheet-{name}-gpt.jpg')


if __name__ == '__main__':
    main()
