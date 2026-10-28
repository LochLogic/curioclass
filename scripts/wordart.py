r"""Draw Word Wall pictures (docs/SUPPLY-CLOSET-PLAN.md, Phase C) with the local image model, and review them.

    python scripts/wordart.py [--band k2,35] [--subject math] [--limit 50] [--force]   draw missing pictures
    python scripts/wordart.py --redo <module_id>/<slug> ["new prompt"] [--seed 7]     draw one again
    python scripts/wordart.py --redo <key> <key> ...                                  draw several again
    any draw: --kobold uses the KoboldCpp server, one picture at a time, instead of fluxbatch
    python scripts/wordart.py --sheets [--band k2]                                   contact sheets to review
    python scripts/wordart.py --status                                               how many are drawn, by band

Only cards whose picture is a painting are drawn here ("svg:" pictures are diagrams drawn in code, except the few
whose spec in data/closet/words/diagrams.py is paint('prompt'), which are painted from that prompt). Each picture is
the card's picture text in one flat house style (simple shapes, dark outlines, white background, no text), saved as
closet/words/art/<module_id>/<slug>.webp at 512 px. A better prompt for one card goes in closet/words/art/prompts.json
({"<module_id>/<slug>": "prompt"}) so a redraw keeps it. Sheets go to closet/words/art/_raw/ (gitignored): look at
every one, then --redo the misses (image models get counts, small animals and balances wrong; they never draw people
here, see localart.py). Draws go through scripts/fluxbatch.py (local FLUX in two phases, much faster for a batch;
stop KoboldCpp first) when diffusers and the model files are here, else through the KoboldCpp server on port 5002
(S:\AI\Start-FluxModel.bat), which --kobold forces.
"""
import csv, hashlib, json, re, sys, time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_words, fluxbatch  # noqa: E402
from localart import txt2img  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ART = check_words.ART
RAW = ART / '_raw'
PROMPTS = ART / 'prompts.json'
STYLE = ('Simple flat vector illustration of {p}. A children\'s flashcard picture: bold clean shapes, thick dark '
         'outlines, a few bright friendly colors, plain white background, centered with space around it, no text.')
SIZE = 512


def painted():
    """Diagram cards whose spec hands them back to the painter: {key: prompt}."""
    lines = (ROOT / 'data' / 'closet' / 'words' / 'diagrams.py').read_text(encoding='utf-8').splitlines()
    return {m[1]: m[2] for m in (re.match(r"^(\S+) = paint\('(.+)'\)$", l) for l in lines) if m}


def cards(bands=None, subjects=None):
    mods = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    out, pd = [], painted()
    for mid, cs in check_words.load(subjects).items():
        b = check_words.band(mods[mid]['grade'])
        if bands and b not in bands:
            continue
        for c in cs:
            key = f"{mid}/{c['slug']}"
            if key in pd:
                out.append(dict(c, picture=pd[key], band=b, key=key))
            elif c['picture'] and not c['picture'].startswith(('svg:', 'people:')):
                out.append(dict(c, band=b, key=key))
    return out


def job(c, prompts, seed=None):
    """(prompt, w, h, seed) for one card, as txt2img and fluxbatch take them."""
    seed = seed if seed is not None else int(hashlib.md5(c['key'].encode()).hexdigest()[:6], 16)
    return STYLE.format(p=prompts.get(c['key'], c['picture'])), 768, 768, seed


def save(im, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    im.convert('RGB').resize((SIZE, SIZE), Image.LANCZOS).save(path, 'WEBP', quality=80, method=6)


def draw(c, prompts, seed=None):
    """One card through the KoboldCpp server."""
    save(txt2img(*job(c, prompts, seed)), c['art'])


def draw_many(cs, prompts, seed=None, kobold=False):
    """Cards through fluxbatch (each phase loaded once for the lot), or one by one through KoboldCpp."""
    if cs and not kobold and fluxbatch.available():
        return fluxbatch.txt2img_many([(*job(c, prompts, seed), c['art']) for c in cs], save)
    t0 = time.time()
    for i, c in enumerate(cs, 1):
        draw(c, prompts, seed)
        if i % 25 == 0 or i == len(cs):
            print(f'{i}/{len(cs)} drawn, {(time.time() - t0) / i:.1f} s each', flush=True)


def sheets(cs):
    RAW.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=15)
    drawn = [c for c in cs if c['art'].exists()]
    per, cell = 30, 256
    for n in range(0, len(drawn), per):
        group = drawn[n:n + per]
        sheet = Image.new('RGB', (cell * 6, (cell + 40) * 5), 'white')
        d = ImageDraw.Draw(sheet)
        for k, c in enumerate(group):
            x, y = (k % 6) * cell, (k // 6) * (cell + 40)
            sheet.paste(Image.open(c['art']).convert('RGB').resize((cell - 8, cell - 8)), (x + 4, y + 4))
            d.text((x + 6, y + cell - 2), f"{n + k + 1}. {c['word']}", fill='#b23a17', font=font)
            d.text((x + 6, y + cell + 16), c['picture'][:34], fill='#333', font=font)
        sheet.save(RAW / f'sheet-{n // per + 1:03d}.jpg', quality=85)
        with open(RAW / f'sheet-{n // per + 1:03d}.txt', 'w', encoding='utf-8') as f:
            f.writelines(f"{n + k + 1}\t{c['key']}\t{c['picture']}\n" for k, c in enumerate(group))
    print(f'{len(drawn)} pictures on {-(-len(drawn) // per)} sheets in {RAW}')


def main():
    a = sys.argv[1:]
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    bands = opt('--band').split(',') if opt('--band') else None
    subjects = opt('--subject').split(',') if opt('--subject') else None
    prompts = json.loads(PROMPTS.read_text(encoding='utf-8')) if PROMPTS.exists() else {}
    cs = cards(bands, subjects)
    if '--status' in a:
        for b in ('k2', '35', '68', '912'):
            bc = [c for c in cs if c['band'] == b]
            print(f"{b}: {sum(c['art'].exists() for c in bc)} of {len(bc)} drawn")
        return
    if '--sheets' in a:
        return sheets(cs)
    kobold = '--kobold' in a
    if '--redo' in a:
        rest = a[a.index('--redo') + 1:]
        rest = rest[:next((i for i, x in enumerate(rest) if x.startswith('--')), len(rest))]
        by = {c['key']: c for c in cs}
        keys = [x for x in rest if x in by]
        if len(keys) == 1 and len(rest) == 2 and rest[0] in by:  # one card with a new prompt
            prompts[keys[0]] = rest[1]
            PROMPTS.write_text(json.dumps(prompts, indent=1, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')
        elif len(keys) < len(rest) or not keys:
            sys.exit(f'not a painted card: {" ".join(x for x in rest if x not in by)}')
        draw_many([by[k] for k in keys], prompts, int(opt('--seed')) if opt('--seed') else None, kobold)
        print('drew', *(by[k]['art'] for k in keys))
        return
    todo = [c for c in cs if '--force' in a or not c['art'].exists()]
    todo = todo[:int(opt('--limit'))] if opt('--limit') else todo
    draw_many(todo, prompts, kobold=kobold)


if __name__ == '__main__':
    main()
