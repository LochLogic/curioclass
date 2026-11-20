"""Upload new or changed pictures in dist/ to the R2 bucket curioclass-media before a deploy.

The site's pictures (Reading Room art and Word Wall art) are served from R2 by worker/index.js, because static assets
are capped at 20,000 files. data/media-manifest.txt lists what is in the bucket (key and size); this script uploads
anything in dist/ that is missing or a different size, then rewrites the manifest.

    python scripts/sync_media.py            # upload what changed
    python scripts/sync_media.py --check    # list what would upload; exit 1 if anything is missing (run before deploy)

The Front Office documents (dist/front-office/docs/, scripts/front_office_docs.py) go to the same bucket under the
same path, also kept out of the asset upload. They change in place, so data/docs-manifest.txt lists each key with a
content hash, not a size; a document no longer built is deleted from the bucket.
"""
import hashlib, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
MANIFEST = ROOT / 'data' / 'media-manifest.txt'
BUCKET = 'curioclass-media'
PATTERNS = ['library/*/art/*.jpg', 'topics/*/words/art/*.webp']  # same as worker/index.js and dist/.assetsignore


TYPES = {'.jpg': 'image/jpeg', '.webp': 'image/webp', '.json': 'application/json; charset=utf-8'}
DOCS = 'front-office/docs/*/*.json'
DOCS_MANIFEST = ROOT / 'data' / 'docs-manifest.txt'


def local_docs():
    return {p.relative_to(DIST).as_posix(): hashlib.sha1(p.read_bytes()).hexdigest() for p in DIST.glob(DOCS)}


def read_docs_manifest():
    if not DOCS_MANIFEST.exists():
        return {}
    return dict(l.rsplit(' ', 1) for l in DOCS_MANIFEST.read_text(encoding='utf-8').splitlines() if l.strip())


def save_docs(m):
    DOCS_MANIFEST.write_text(''.join(f'{k} {m[k]}\n' for k in sorted(m)), encoding='utf-8', newline='\n')


def key(rel):
    """The R2 key for a path under dist/. Word Wall art keeps its key from before topic pages moved to /topics/
    (worker/index.js maps it the same way), so nothing uploads again and the manifest keeps its names."""
    return 'modules/' + rel[len('topics/'):] if rel.startswith('topics/') else rel


def file_of(k):
    """The file in dist/ for an R2 key (the reverse of key())."""
    return DIST / ('topics/' + k[len('modules/'):] if k.startswith('modules/') else k)


def local():
    return {key(p.relative_to(DIST).as_posix()): p.stat().st_size for pat in PATTERNS for p in DIST.glob(pat)}


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
    dhave, dsent = local_docs(), read_docs_manifest()
    dtodo = sorted(k for k, h in dhave.items() if dsent.get(k) != h)
    dgone = sorted(k for k in dsent if k not in dhave) if dhave else []   # no docs built at all: delete nothing
    print(f'{len(dhave)} Front Office documents in dist, {len(dtodo)} to upload, {len(dgone)} to delete')
    if '--check' in sys.argv:
        for k in (todo + dtodo)[:20]:
            print('  ', k)
        sys.exit(1 if todo or dtodo else 0)
    cmd, lock, fails = wrangler(), threading.Lock(), []

    def run(args):
        for attempt in range(5):
            r = subprocess.run(cmd + args + ['--remote'], capture_output=True, text=True, encoding='utf-8',
                               errors='replace', cwd=ROOT)
            if r.returncode == 0:
                return None
            time.sleep(5 * (attempt + 1))
        return r.stderr[-300:].encode('ascii', 'replace').decode()

    def put_doc(k):
        err = run(['r2', 'object', 'put', f'{BUCKET}/{k}', '--file', str(DIST / k), '--content-type', TYPES['.json']])
        with lock:
            if err:
                fails.append(k)
                print('FAIL', k, err, flush=True)
            else:
                dsent[k] = dhave[k]

    def drop_doc(k):
        err = run(['r2', 'object', 'delete', f'{BUCKET}/{k}'])
        with lock:
            if err:
                fails.append(k)
                print('FAIL delete', k, err, flush=True)
            else:
                dsent.pop(k, None)

    try:
        with ThreadPoolExecutor(8) as ex:
            list(ex.map(put_doc, dtodo))
            list(ex.map(drop_doc, dgone))
    finally:
        save_docs(dsent)
    print(f'documents: uploaded {sum(1 for k in dtodo if dsent.get(k) == dhave[k])}, deleted '
          f'{sum(1 for k in dgone if k not in dsent)}')

    def put(k):
        for attempt in range(5):
            r = subprocess.run(cmd + ['r2', 'object', 'put', f'{BUCKET}/{k}', '--file', str(file_of(k)),
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
