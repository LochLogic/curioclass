r"""Draw the Word Wall cards that need a person (an action like hop or skip) with gpt-image-2 through Codex.

    python scripts/wordpeople.py [module_id/slug ...] [--n 1] [--force]   draw candidates to closet/words/art/_raw/people/
    python scripts/wordpeople.py --pick module_id/slug:k                  keep candidate k as the card's picture

A card whose picture starts "people:" is drawn here, never by the local painter (scripts/wordart.py skips it, since
the local models never draw people) and never in code. So is a card whose picture starts "gpt:": a picture FLUX has
failed twice (usually lettering, numbers or a precise idea), which goes to gpt-image-2 before Gemini, not down to code. Same flat flashcard style as wordart.py, drawn by
scripts/gptart.py's Codex call on the ChatGPT plan. Every candidate is looked at before it is picked (docs/ART.md).
"""
import shutil, sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_words  # noqa: E402
from gptart import draw  # noqa: E402
from wordart import SIZE, STYLE  # noqa: E402

RAW = check_words.ART / '_raw' / 'people'
PEOPLE = (' Each child is cheerful, about 7, in a plain t-shirt, shorts and sneakers, the whole body in view, '
          'with the pose doing the work so the action reads at a glance.')


def cards():
    return {f"{mid}/{c['slug']}": c for mid, cs in check_words.load().items() for c in cs
            if c['picture'].startswith(('people:', 'gpt:'))}


def main():
    args = sys.argv[1:]
    if '--pick' in args:
        key, k = args[args.index('--pick') + 1].rsplit(':', 1)
        src = RAW / f"{key.replace('/', '__')}.c{k}.png"
        out = check_words.ART / f'{key}.webp'
        out.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(src).convert('RGB')
        side = max(im.size)  # pad to a square on white, then size like every other card
        sq = Image.new('RGB', (side, side), 'white')
        sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
        sq.resize((SIZE, SIZE), Image.LANCZOS).save(out, 'WEBP', quality=80, method=6)
        print(f'{key}: kept c{k}')
        return
    n = int(args[args.index('--n') + 1]) if '--n' in args else 1
    wanted = {a for a in args if '/' in a}
    RAW.mkdir(parents=True, exist_ok=True)
    work = RAW / '_work'; work.mkdir(exist_ok=True)
    for key, c in cards().items():
        if wanted and key not in wanted:
            continue
        if (check_words.ART / f'{key}.webp').exists() and not wanted and '--force' not in args:
            continue
        kind, _, p = c['picture'].partition(':')
        prompt = STYLE.format(p=p.strip()) + (PEOPLE if kind == 'people' else '')
        have = len(list(RAW.glob(f"{key.replace('/', '__')}.c*.png")))
        for k in range(have + 1, have + 1 + n):
            src = draw(prompt, 'square', [], work)
            if src:
                shutil.copyfile(src, RAW / f"{key.replace('/', '__')}.c{k}.png")
                print(f'{key} c{k}', flush=True)


if __name__ == '__main__':
    main()
