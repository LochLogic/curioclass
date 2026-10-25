"""Paint the Large Magellanic Cloud in code: local image models only draw it as a spiral, and it is an irregular galaxy.

    python tools/size-of-everything/art/make_lmc.py && python scripts/art.py size-of-everything lmc --rekey
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

rng = np.random.default_rng(14)
N = 1024
y, x = np.mgrid[0:N, 0:N] / N


def blob(cx, cy, sx, sy, a=0):
    c, s = np.cos(a), np.sin(a)
    dx, dy = x - cx, y - cy
    return np.exp(-((c * dx + s * dy) / sx) ** 2 - ((-s * dx + c * dy) / sy) ** 2)


noise = np.array(Image.fromarray((rng.random((64, 64)) * 255).astype(np.uint8)).resize((N, N), Image.BICUBIC)) / 255
# a lumpy body of stars, a bright bar off to one side, and pink star-forming clouds (the biggest is the Tarantula Nebula)
dens = (blob(.5, .5, .3, .22, .3) + .7 * blob(.34, .42, .15, .13) + .6 * blob(.63, .63, .17, .11, -.4) + .45 * blob(.72, .36, .11, .09)) * (.45 + noise)
bar = blob(.46, .52, .21, .05, .35)
img = (dens * .42 + bar * .8)[..., None] * np.array([.72, .8, 1.0])
k = np.clip(dens * .022 + bar * .06, 0, .5)
stars = (rng.random((N, N)) < k).astype(float) * (rng.random((N, N)) * .8 + .5)
stars = np.array(Image.fromarray((np.clip(stars, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))) / 255
col = np.where(rng.random((N, N))[..., None] < .7, np.array([.9, .94, 1.0]), np.array([1.0, .9, .75]))
img += stars[..., None] * col
for cx, cy, s, amp in [(.67, .37, .045, 1.1), (.3, .56, .028, .7), (.58, .67, .022, .6), (.42, .3, .02, .55), (.22, .45, .016, .5)]:
    img += (blob(cx, cy, s, s) * (.4 + noise * 1.2))[..., None] * np.array([1.0, .32, .55]) * amp
out = Path(__file__).parent / 'raw' / 'lmc.png'
out.parent.mkdir(exist_ok=True)
Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.6)).save(out)
