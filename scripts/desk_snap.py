"""Write a read-only snapshot of the Desk's data for viewers who are not signed in.

    python -X utf8 desk_snap.py <snap_dir> <desk-pub dir>

snap_dir holds items/*.json and stats/*.json from ArtifactData list with out_dir. Writes <desk-pub>/snap.json,
published beside the page (Artifact `files: {"snap.json": ...}`). Comments are never included.
"""
import json, os, re, sys, datetime
snap, pub = sys.argv[1], sys.argv[2]
def load(coll):
    d = os.path.join(snap, coll)
    return [dict(id=f[:-5], data=json.load(open(os.path.join(d, f), encoding='utf-8')))
            for f in sorted(os.listdir(d)) if f.endswith('.json')]
blob = dict(at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), items=load('items'), stats=load('stats'))
open(os.path.join(pub, 'snap.json'), 'w', encoding='utf-8').write(json.dumps(blob, separators=(',', ':'), ensure_ascii=False))
# drop any inline copy an older version baked into the page
page = os.path.join(pub, 'desk.html')
html = open(page, encoding='utf-8', newline='').read()
html2 = re.sub(r'\n?<script>window\.DESK_SNAP=.*?;</script>', '', html, flags=re.S)
html2 = re.sub(r'\n?<script type="application/json" id="snap">.*?</script>', '', html2, flags=re.S)
if html2 != html:
    open(page, 'w', encoding='utf-8', newline='').write(html2)
print('snapshot', blob['at'], len(blob['items']), 'items', len(blob['stats']), 'stats docs')
