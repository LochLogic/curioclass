"""Find the water in painted pictures so a tool can answer "land or water?" when a child taps one.

    python scripts/water_mask.py <tool-id> <art-name>:<width>x<height> [...]

Water = clearly blue pixels in big connected patches (blue roofs and toys are too small to count).
Writes tools/<id>/water.json: {name: {w, h, bits}}, bits = base64 of a row-major 1-bit mask.
"""
import base64, json, sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = Path(__file__).resolve().parent.parent


def mask(path, w, h, min_px=40):
    a = np.asarray(Image.open(path).convert('RGB').resize((w, h), Image.LANCZOS)).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    blue = (b > r + 40) & (b > g + 5)
    lab, k = ndimage.label(blue)
    sizes = ndimage.sum(blue, lab, range(1, k + 1))
    keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > min_px])
    return ndimage.binary_closing(keep, iterations=2)


if __name__ == '__main__':
    folder = ROOT / 'tools' / sys.argv[1]
    out = {}
    for spec in sys.argv[2:]:
        name, size = spec.split(':')
        w, h = map(int, size.split('x'))
        m = mask(folder / 'art' / f'{name}.webp', w, h)
        out[name] = {'w': w, 'h': h, 'bits': base64.b64encode(np.packbits(m.ravel()).tobytes()).decode()}
        print(f'{name}: {m.mean():.0%} water')
    (folder / 'water.json').write_text(json.dumps(out), encoding='utf-8')
