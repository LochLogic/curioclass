r"""Fetch public-domain artworks from museum open-access collections into a tool's art folder.

    python scripts/pd_art.py <tool-id> met:365241 aic:20684 met:500576@1 ... [--long 1400] [--kb 120] [--force]

met:<id>@<n> takes the Met's nth additional image instead of the primary one (when the primary is small or a detail).

Sources: The Met Collection API (collectionapi.metmuseum.org, Open Access images are CC0) and the Art Institute of
Chicago API (api.artic.edu, public-domain images through its IIIF server, CC0). A work is saved only when the museum
marks it public domain (Met isPublicDomain, AIC is_public_domain) and has an image; anything else is reported and
skipped. Each image becomes tools/<id>/art/pd-<museum>-<objectid>.webp (long side --long px, quality lowered until it
fits --kb; images under 500 px are refused), used in src.html as art:pd-met-365241 like any other art. Title, artist, date, credit line and the
collection URL go to tools/<id>/art/public-domain.json, for the tool's Sources and credits. Not listed in
prompts.json, so art.py never tries to draw them.
"""
import io, json, sys, time, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
UA = {'User-Agent': 'CurioClass/1.0 (free K-12 classroom tools; curioclass.org)'}


def get(url, raw=False):
    for tries in range(3):
        try:
            url = urllib.parse.quote(url, safe=':/?&=,%')
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                data = r.read()
            return data if raw else json.loads(data)
        except Exception as e:
            if tries == 2:
                raise
            time.sleep(2 + 3 * tries)


def met(oid):
    oid, _, alt = oid.partition('@')
    o = get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}')
    if not o.get('isPublicDomain') or not o.get('primaryImage'):
        return None, f'not public domain or no image (isPublicDomain={o.get("isPublicDomain")})'
    return {'museum': 'The Metropolitan Museum of Art', 'id': oid, 'title': o.get('title', ''),
            'artist': o.get('artistDisplayName', ''), 'date': o.get('objectDate', ''),
            'credit': o.get('creditLine', ''), 'url': o.get('objectURL', ''), 'license': 'CC0 (Met Open Access)',
            'image': o['additionalImages'][int(alt) - 1] if alt else o['primaryImage']}, None


def aic(oid):
    o = get(f'https://api.artic.edu/api/v1/artworks/{oid}?fields=id,title,artist_display,date_display,credit_line,'
            'image_id,is_public_domain')['data']
    if not o.get('is_public_domain') or not o.get('image_id'):
        return None, f'not public domain or no image (is_public_domain={o.get("is_public_domain")})'
    return {'museum': 'Art Institute of Chicago', 'id': oid, 'title': o.get('title', ''),
            'artist': (o.get('artist_display') or '').split('\n')[0], 'date': o.get('date_display', ''),
            'credit': o.get('credit_line', ''), 'url': f'https://www.artic.edu/artworks/{oid}', 'license': 'CC0 (AIC public domain)',
            'image': f'https://www.artic.edu/iiif/2/{o["image_id"]}/full/1686,/0/default.jpg'}, None


def save(img_bytes, out, long_side, kb):
    im = Image.open(io.BytesIO(img_bytes))
    if max(im.size) < 500:
        raise ValueError(f'museum image is only {im.size[0]}x{im.size[1]}, too small to use')
    im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
    # Engravings and prints are fine detail and compress badly: past the lowest quality, shrink and try again.
    while True:
        im.thumbnail((long_side, long_side), Image.LANCZOS)
        for q in (82, 76, 70, 64, 58, 52, 46):
            buf = io.BytesIO()
            im.save(buf, 'WEBP', quality=q, method=6)
            if buf.tell() <= kb * 1024:
                out.write_bytes(buf.getvalue())
                return buf.tell() // 1024, q, im.size
        long_side = int(max(im.size) * 0.85)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    long_side, kb, force = opt('--long', 1400), opt('--kb', 120), '--force' in sys.argv
    args = [a for a in args if not a.isdigit() or ':' in a]
    tool, works = args[0], args[1:]
    art = ROOT / 'tools' / tool / 'art'
    art.mkdir(parents=True, exist_ok=True)
    meta_path = art / 'public-domain.json'
    meta = json.loads(meta_path.read_text(encoding='utf-8')) if meta_path.exists() else {}
    for w in works:
        museum, oid = w.split(':')
        name = f'pd-{museum}-{oid.split("@")[0]}'
        out = art / f'{name}.webp'
        if out.exists() and name in meta and not force:
            print(f'skip {name} (exists)')
            continue
        try:
            info, why = (met if museum == 'met' else aic)(oid)
            if not info:
                print(f'SKIP {name}: {why}')
                continue
            size, q, dims = save(get(info.pop('image'), raw=True), out, long_side, kb)
            meta[name] = info
            print(f'{name}: {size} KB q{q} {dims[0]}x{dims[1]}  {info["title"][:60]} / {info["artist"][:30]}')
        except Exception as e:
            print(f'FAIL {name}: {e}')
        time.sleep(0.5)
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
