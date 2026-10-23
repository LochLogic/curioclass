"""Generate tool artwork with Gemini, cut it out, and save small WebP files for bundling.

    python scripts/art.py <tool-id> [asset names...] [--force]

Reads tools/<tool-id>/art/prompts.json:
    {"style": "optional extra style notes",
     "assets": [{"name": "pig", "prompt": "a cheerful pink pig ...", "width": 360, "cutout": true}]}

Needs GEMINI_API_KEY (environment, or the Windows user setting). CURIO_IMAGE_MODEL overrides the model.
Asset options: "ref": "<other asset>" sends that asset's raw image along so a character stays consistent;
"ref_mode": "style" matches only the drawing style and outfit, not the character;
"crop": [top, bottom] keeps that vertical slice (0-1) of the cut-out figure, e.g. a musician from hat to waist;
"height" sizes by height instead of width, so a set of characters lines up;
"aspect": "9:16" (or "3:4", "16:9"...) sets the frame shape, e.g. portrait for a full-length figure.
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
CUTOUT = ("Draw the subject alone, centered, fully in frame, on a perfectly flat solid pure green (#00FF00) background. "
          "No ground, no cast shadow, no other objects. Keep green out of the subject itself.")


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


def generate(prompt, refs=(), aspect=None):
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=api_key())
    image = types.ImageConfig(aspect_ratio=aspect) if aspect else None
    resp = client.models.generate_content(model=MODEL, contents=[prompt, *refs],
                                          config=types.GenerateContentConfig(response_modalities=['IMAGE'], image_config=image))
    for part in resp.candidates[0].content.parts:
        if part.inline_data and part.inline_data.data:
            return Image.open(io.BytesIO(part.inline_data.data)).convert('RGBA')
    raise RuntimeError('no image in response')


def cut_out(img):
    """Key out the green background, soften the edge, and remove green spill."""
    a = np.asarray(img).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = g - np.maximum(r, b)
    alpha = np.clip(1 - (green - 25) / 70, 0, 1)
    spill = alpha < 1
    a[..., 1] = np.where(spill, np.minimum(g, np.maximum(r, b) + 10), g)
    a[..., 3] = alpha * 255
    out = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')
    box = out.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    return out.crop(box) if box else out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    force = '--force' in sys.argv
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
        prompt = ' '.join([HOUSE_STYLE, tool_style, asset['prompt'], CUTOUT if asset.get('cutout') else ''])
        raw = art / 'raw' / f'{name}.png'
        refs = [Image.open(art / 'raw' / f'{asset["ref"]}.png')] if asset.get('ref') else []
        if refs and asset.get('ref_mode') == 'style':
            prompt += (' Match only the drawing style, line quality, proportions and uniform design of the reference image.'
                       ' Draw a different child with a different face, skin tone and hair.')
        elif refs:
            prompt += ' Match the character design, colors and drawing style of the reference image exactly.'
        img = generate(prompt, refs, asset.get('aspect'))
        img.save(raw)
        if asset.get('cutout'):
            img = cut_out(img)
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
