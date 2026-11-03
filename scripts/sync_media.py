"""Upload new or changed pictures in dist/ to the R2 bucket curioclass-media before a deploy.

The site's pictures (Reading Room art and Word Wall art) are served from R2 by worker/index.js, because static assets
are capped at 20,000 files. data/media-manifest.txt lists what is in the bucket (key and size); this script uploads
anything in dist/ that is missing or a different size, then rewrites the manifest.

    python scripts/sync_media.py            # upload what changed
    python scripts/sync_media.py --check    # list what would upload; exit 1 if anything is missing (run before deploy)
"""
import os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
MANIFEST = ROOT / 'data' / 'media-manifest.txt'
BUCKET = 'curioclass-media'
PATTERNS = ['library/*/art/*.jpg', 'modules/*/words/art/*.webp']  # same as worker/index.js and dist/.assetsignore
TYPES = {'.jpg': 'image/jpeg', '.webp': 'image/webp'}


def local():
    return {p.relative_to(DIST).as_posix(): p.stat().st_size for pat in PATTERNS for p in DIST.glob(pat)}


def manifest():
    if not MANIFEST.exists():
        return {}
    return {k: int(n) for k, n in (l.rsplit(' ', 1) for l in MANIFEST.read_text(encoding='utf-8').splitlines() if l.strip())}


def save(m):
    MANIFEST.write_text(''.join(f'{k} {m[k]}\n' for k in sorted(m)), encoding='utf-8')


def wrangler():
    for d in (ROOT / 'node_modules' / 'wrangler' / 'bin', ):
        if (d / 'wrangler.js').exists():
            return ['node', str(d / 'wrangler.js')]
    return ['npx', '--yes', 'wrangler'] if os.name != 'nt' else ['npx.cmd', '--yes', 'wrangler']


def main():
    if not DIST.exists():
        sys.exit('dist/ is missing: run scripts/build_site.py first')
    have, sent = local(), manifest()
    todo = sorted(k for k, n in have.items() if sent.get(k) != n)
    print(f'{len(have)} pictures in dist, {len(sent)} in the bucket manifest, {len(todo)} to upload')
    if '--check' in sys.argv:
        for k in todo[:20]:
            print('  ', k)
        sys.exit(1 if todo else 0)
    cmd, lock, fails = wrangler(), threading.Lock(), []

    def put(k):
        for attempt in range(5):
            r = subprocess.run(cmd + ['r2', 'object', 'put', f'{BUCKET}/{k}', '--file', str(DIST / k),
                                      '--content-type', TYPES[Path(k).suffix], '--remote'],
                               capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT)
            if r.returncode == 0:
                with lock:
                    sent[k] = have[k]
                return
            time.sleep(5 * (attempt + 1))
        with lock:
            fails.append(k)
            print('FAIL', k, r.stderr[-300:].encode('ascii', 'replace').decode(), flush=True)

    try:
        with ThreadPoolExecutor(8) as ex:
            for i, _ in enumerate(ex.map(put, todo), 1):
                if i % 250 == 0:
                    print(i, flush=True)
                    with lock:
                        save(sent)
    finally:
        save(sent)
    print(f'uploaded {len(todo) - len(fails)}, failed {len(fails)}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
