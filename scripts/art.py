"""Generate tool artwork with Gemini, cut it out, and save small WebP files for bundling.

    python scripts/art.py <tool-id> [asset names...] [--force] [--rekey]

--force draws again; --rekey only redoes the cutout and sizing from the saved original in art/raw/ (free).

Reads tools/<tool-id>/art/prompts.json:
    {"house_style": "optional, replaces the storybook house style (older grades; an asset can set its own too)",
     "style": "optional extra style notes",
     "assets": [{"name": "pig", "prompt": "a cheerful pink pig ...", "width": 360, "cutout": true}]}

Needs GEMINI_API_KEY (environment, or the Windows user setting). CURIO_IMAGE_MODEL overrides the model.
Asset options: "ref": "<other asset>" sends that asset's raw image along so a character stays consistent;
"ref_mode": "style" matches only the drawing style and outfit, not the character;
"crop": [top, bottom] keeps that vertical slice (0-1) of the cut-out figure, e.g. a musician from hat to waist;
"height" sizes by height instead of width, so a set of characters lines up;
"aspect": "9:16" (or "3:4", "16:9"...) sets the frame shape, e.g. portrait for a full-length figure.
"size": "2K" asks for a larger drawing, for a scene the tool zooms into (Frame It).
"key": "magenta" draws on magenta instead of green, for green subjects (lettuce, frogs, leaves).
"cutout": "keyed" removes the key color without the subject-alone wording, e.g. a scene whose sky is drawn flat green.
"trim": 0.03 shaves that fraction off every side, for backgrounds that come back with a painted frame.
Raw images go to art/raw/ (not committed); finished art/<name>.webp is committed and bundled
into the tool by scripts/bundle_tool.py. See docs/ART.md for the house style.
"""
import io, json, os, sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get('CURIO_IMAGE_MODEL', 'gemini-3.1-flash-image')
HOUSE_STYLE = ("Warm storybook illustration for a children's classroom tool. Soft gouache and colored-pencil texture, "
               "clean confident shapes, gentle shading, friendly proportions, rich but not neon colors. "
               "No text, no letters, no watermark, no border, no frame.")
KEYS = {'green': 'pure green (#00FF00)', 'magenta': 'pure magenta (#FF00FF)'}
CUTOUT = ("Draw the subject alone, centered, fully in frame, on a perfectly flat solid {key} background. "
          "No ground, no cast shadow, no other objects. Keep that background color out of the subject itself.")


def api_key():
    key = os.environ.get('GEMINI_API_KEY')
    if not key and os.name == 'nt':  # set with [Environment]::SetEnvironmentVariable(..., 'User')
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment') as k:
                key = winreg.QueryValueEx(k, 'GEMINI_API_KEY')[0]
        except OSError:
            pass
    if not key:
        sys.exit('GEMINI_API_KEY is not set (see docs/ART.md)')
    return key


def generate(prompt, refs=(), aspect=None, size=None):
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key())
    opts = {k: v for k, v in (('aspect_ratio', aspect), ('image_size', size)) if v}
    image = types.ImageConfig(**opts) if opts else None
    resp = client.models.generate_content(model=MODEL, contents=[prompt, *refs],
                                          config=types.GenerateContentConfig(response_modalities=['IMAGE'], image_config=image))
    for part in resp.candidates[0].content.parts:
        if part.inline_data and part.inline_data.data:
            return Image.open(io.BytesIO(part.inline_data.data)).convert('RGBA')
    raise RuntimeError('no image in response')


def cut_out(img, scene=False):
    """Key out the background (green or magenta), soften the edge, and remove color spill.

    Keys by distance from the actual background color (sampled at the border) rather than by "how green",
    so a green jacket stays solid. Only background touching the border is keyed, plus enclosed pockets that
    are very close to the key color (a gap between an arm and the body)."""
    from scipy import ndimage
    a = np.asarray(img).astype(np.float32)
    # a keyed scene (flat sky above a landscape) only touches the key along the top
    border = a[0, :, :3] if scene else np.concatenate([a[0, :, :3], a[-1, :, :3], a[:, 0, :3], a[:, -1, :3]])
    key = np.median(border, axis=0)
    dist = np.sqrt(((a[..., :3] - key) ** 2).sum(-1))
    alpha = np.clip((dist - 25) / 45, 0, 1)
    labels, _ = ndimage.label(alpha < .5)
    edge = np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))
    background = np.isin(labels, edge[edge > 0]) | (dist < 25)
    near = ndimage.binary_dilation(background, iterations=3)  # keep the soft keyed edge next to real background
    if not scene:  # a scene keys sky showing through leaves too, wherever it is
        alpha = np.where(near, alpha, 1)
    # drop specks and faint ground shadows that are not part of the figure
    blobs, count = ndimage.label(alpha > .5)
    if count > 1 and not scene:
        sizes = ndimage.sum(np.ones_like(alpha), blobs, range(1, count + 1))
        keep = np.isin(blobs, 1 + np.flatnonzero(sizes >= sizes.max() * .02))
        alpha = np.where(ndimage.binary_dilation(keep, iterations=2), alpha, 0)
    # remove key-color spill from soft edges: each edge pixel is a mix of figure and key, so un-mix it
    edge_px = (alpha > .05) & (alpha < 1)
    fg = (a[..., :3] - (1 - alpha[..., None]) * key) / np.maximum(alpha[..., None], .05)
    a[..., :3] = np.where(edge_px[..., None], fg, a[..., :3])
    if scene:  # painted leaves blend toward the flat sky color; pull that cast back out
        k = int(np.argmax(key)) if key.max() - key.min() > 100 else None
        if k == 1:  # green sky: green may not exceed the brighter of red and blue by much
            a[..., 1] = np.minimum(a[..., 1], np.maximum(a[..., 0], a[..., 2]) * 1.08 + 4)
    a[..., 3] = alpha * 255
    out = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')
    box = out.getchannel('A').point(lambda v: 255 if v > 128 else 0).getbbox()  # faint haze doesn't stretch the frame
    return out.crop(box) if box and not scene else out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    rekey = '--rekey' in sys.argv
    force = '--force' in sys.argv or rekey
    tool, wanted = args[0], set(args[1:])
    art = ROOT / 'tools' / tool / 'art'
    spec = json.loads((art / 'prompts.json').read_text(encoding='utf-8'))
    (art / 'raw').mkdir(parents=True, exist_ok=True)
    for asset in spec['assets']:
        name = asset['name']
        if wanted and name not in wanted:
            continue
        out = art / f'{name}.webp'
        if out.exists() and not force:
            print(f'skip {name} (exists; --force to redo)')
            continue
        tool_style = '' if asset.get('skip_style') else spec.get('style', '')  # backgrounds skip character notes
        prompt = ' '.join([asset.get('house_style', spec.get('house_style', HOUSE_STYLE)), tool_style, asset['prompt'], CUTOUT.format(key=KEYS[asset.get('key', 'green')]) if asset.get('cutout') is True else ''])
        raw = art / 'raw' / f'{name}.png'
        refs = [Image.open(art / 'raw' / f'{asset["ref"]}.png')] if asset.get('ref') else []
        if refs and asset.get('ref_mode') == 'style':
            prompt += (' Match only the drawing style, line quality, proportions and uniform design of the reference image.'
                       ' Draw a different child with a different face, skin tone and hair.')
        elif refs:
            prompt += ' Match the character design, colors and drawing style of the reference image exactly.'
        if rekey:  # redo the cutout and sizing from the saved original, without drawing again
            img = Image.open(raw).convert('RGBA')
        else:
            img = generate(prompt, refs, asset.get('aspect'), asset.get('size'))
            img.save(raw)
        if asset.get('trim'):  # shave a painted frame off every side
            t = asset['trim']; img = img.crop((round(img.width * t), round(img.height * t), round(img.width * (1 - t)), round(img.height * (1 - t))))
        if asset.get('cutout'):
            img = cut_out(img, scene=asset['cutout'] == 'keyed')
        if asset.get('crop'):
            top, bottom = asset['crop']
            img = img.crop((0, round(img.height * top), img.width, round(img.height * bottom)))
        if asset.get('height'):
            h = asset['height']
            img = img.resize((round(img.width * h / img.height), h), Image.LANCZOS)
        else:
            w = asset.get('width', 512)
            img = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
        img.save(out, 'WEBP', quality=asset.get('quality', 82), method=6)
        print(f'made {name}: {img.width}x{img.height}, {out.stat().st_size // 1024} KB')


if __name__ == '__main__':
    main()
