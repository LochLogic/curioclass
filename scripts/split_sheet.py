r"""Split a character sheet (several full-length drawings of one character in a row) into one WebP per cell.

    python scripts/split_sheet.py <tool-id> [sheet names...]

For every asset in tools/<id>/art/prompts.json with a "cells" list (the looks, left to right), this keys out
art/raw/<name>.png with art.py's cutout, finds the figures by the empty alpha columns between them, crops each one,
scales the sheet so its tallest figure is "cell_height" (default 200 px) and saves art/<name>-<n>.webp (n from 0, in "cells" order) at
"cell_quality" (default 60) with a lighter alpha channel. Cells keep their own width; the tool stands them on their
feet. Each cell's [width, height] goes to tools/<id>/cells.json for the tool. The whole-sheet art/<name>.webp is not needed afterwards. Prints each cell's size; a sheet
whose figures touch (fewer gaps than cells) stops with a message instead of guessing.
"""
import json, sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from art import cut_out  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def runs(mask):
    """(start, end) of each run of True in a 1-D mask."""
    out, start = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            out.append((start, i)); start = None
    return out


def split(img, n):
    a = np.asarray(img.getchannel('A')) > 128
    cols = a.sum(0)
    parts = runs(cols > 0)
    while len(parts) > n:  # a stray speck or a tail tip: merge the narrowest run into its nearer neighbor
        k = min(range(len(parts)), key=lambda i: parts[i][1] - parts[i][0])
        if k == 0: j = 1
        elif k == len(parts) - 1: j = k - 1
        else: j = k - 1 if parts[k][0] - parts[k - 1][1] < parts[k + 1][0] - parts[k][1] else k + 1
        lo, hi = sorted((k, j))
        parts[lo:hi + 1] = [(parts[lo][0], parts[hi][1])]
    if len(parts) < n:  # two drawings touch (a shoe tip): cut at the emptiest column near each expected boundary
        x0, x1 = parts[0][0], parts[-1][1]
        step = (x1 - x0) / n
        cuts = [x0]
        for i in range(1, n):
            lo, hi = round(x0 + step * (i - .35)), round(x0 + step * (i + .35))
            cuts.append(lo + int(np.argmin(cols[lo:hi])))
        cuts.append(x1)
        print(f'  {len(parts)} gaps for {n} figures: cut at the emptiest columns ({[int(cols[c]) for c in cuts[1:-1]]} px deep)')
        parts = list(zip(cuts[:-1], cuts[1:]))
    return parts


def main():
    tool, wanted = sys.argv[1], set(sys.argv[2:])
    art = ROOT / 'tools' / tool / 'art'
    spec = json.loads((art / 'prompts.json').read_text(encoding='utf-8'))
    total = 0
    dims_file = ROOT / 'tools' / tool / 'cells.json'
    dims = json.loads(dims_file.read_text(encoding='utf-8')) if dims_file.exists() else {}
    for asset in spec['assets']:
        name, cells = asset['name'], asset.get('cells')
        if not cells or (wanted and name not in wanted):
            continue
        img = cut_out(Image.open(art / 'raw' / f'{name}.png').convert('RGBA'), despill=asset.get('despill', False))
        h, q = asset.get('cell_height', 200), asset.get('cell_quality', 60)
        dims[name] = []
        for i, (x0, x1) in enumerate(split(img, len(cells))):
            c = img.crop((x0, 0, x1, img.height))
            c = c.crop(c.getchannel('A').point(lambda v: 255 if v > 128 else 0).getbbox())
            f = h / img.height  # one scale per sheet, so a slumped pose stays a little shorter
            c = c.resize((max(1, round(c.width * f)), max(1, round(c.height * f))), Image.LANCZOS)
            out = art / f'{name}-{i}.webp'
            c.save(out, 'WEBP', quality=q, alpha_quality=asset.get('cell_alpha', 70), method=6)
            dims[name].append([c.width, c.height])
            total += out.stat().st_size
            print(f'{name}-{i} ({cells[i]}): {c.width}x{c.height}, {out.stat().st_size / 1024:.1f} KB')
    dims_file.write_text(json.dumps(dims, separators=(',', ':')), encoding='utf-8')
    print(f'total {total / 1024:.1f} KB; cell sizes in {dims_file.relative_to(ROOT)} (src.html reads them as "json:cells")')


if __name__ == '__main__':
    main()
