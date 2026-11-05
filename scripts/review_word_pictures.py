r"""Does each Word Wall picture show its word? A review with local models only. It changes no card, prompt, picture or spec.

    python scripts/review_word_pictures.py render     draw every diagram spec to PNG in closet/words/art/_raw/review/diagrams/
                                                      and note diagrams whose published webp differs from the spec today
    python scripts/review_word_pictures.py clip       CLIP (openai/clip-vit-large-patch14) score of each picture against
                                                      "word: definition", ranked within its subject and within its module
    python scripts/review_word_pictures.py qwen [--limit N] [--batch 12]
                                                      Qwen3-VL-4B-Instruct rates each picture 1 to 5; appends to qwen.jsonl,
                                                      so a restart skips the cards already done
    python scripts/review_word_pictures.py combine    flag cards, write flags.csv and the contact sheet index.html

Outputs go to docs/agents/audit/wordwall-picture-review/. Pictures are referenced, not copied: paintings from
closet/words/art/, diagrams from the fresh renders (which are gitignored, so run render before opening the sheet).
Flag rule: Qwen 1 or 2, or Qwen 3 with a bottom-10% CLIP rank in its subject. Diagrams with text labels are a known
weak spot for small vision models, so they are flagged apart ("diagram-text") and only at Qwen 1, or Qwen 2 with a
bottom-10% CLIP rank.
"""
import csv, json, re, subprocess, sys, time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_words as cw  # noqa: E402

ROOT = cw.ROOT
OUT = ROOT / 'docs' / 'agents' / 'audit' / 'wordwall-picture-review'
REND = cw.ART / '_raw' / 'review' / 'diagrams'
BANDS = {'k2': 'grades K to 2', '35': 'grades 3 to 5', '68': 'grades 6 to 8', '912': 'grades 9 to 12'}
TEXT_FN = re.compile(r"\b(T|F|eq|label|labels|boxes|tile|tiles|word|words|page|staff|plot|numberline|table|chart|"
                     r"bars|letters?|card|sign|clock|tag|note|caption)\(|'[A-Za-z]{2,}|\"[A-Za-z]{2,}")


def kind_of(c, painted):
    key = f"{c['module_id']}/{c['slug']}"
    if key in painted:
        return 'paint'
    for pre in ('svg', 'people', 'gpt'):
        if c['picture'].startswith(pre + ':'):
            return pre
    return 'paint'


def cards():
    """Every card that has a published picture, with its subject, band, kind and the image the models look at."""
    import wordart
    mods = {m['module_id']: m for m in csv.DictReader(open(ROOT / 'data' / 'modules.csv', encoding='utf-8'))}
    painted = wordart.painted()
    spec = spec_lines()
    out = []
    for mid, cs in cw.load().items():
        for c in cs:
            if not c['art'].exists():
                continue
            key = f"{mid}/{c['slug']}"
            k = kind_of(c, painted)
            img = c['art']
            text = False
            if k == 'svg':
                png = REND / (key.replace('/', '__') + '.png')
                if png.exists():
                    img = png
                text = bool(TEXT_FN.search(spec.get(key, '')))
            out.append(dict(key=key, module_id=mid, subject=mods[mid]['subject'], band=cw.band(mods[mid]['grade']),
                            word=c['word'], definition=c['definition'], picture=c['picture'], kind=k, text=text,
                            img=str(img), art=str(c['art'])))
    return out


def spec_lines():
    src = (ROOT / 'data' / 'closet' / 'words' / 'diagrams.py').read_text(encoding='utf-8').splitlines()
    return {l.partition(' = ')[0].strip(): l.partition(' = ')[2] for l in src if ' = ' in l and not l.lstrip().startswith('#')}


# ---------- render ----------

def render():
    import wordsvg
    from PIL import Image, ImageChops, ImageStat
    sp, env = wordsvg.specs()
    allc = {f"{c['module_id']}/{c['slug']}": c for cs in cw.load().values() for c in cs}
    svgs, errors = {}, []
    for k, (n, expr) in sp.items():
        if k not in allc or 'paint(' in expr:
            continue
        try:
            svgs[k] = wordsvg.render(eval(expr, env))
        except Exception as e:  # noqa: BLE001
            errors.append(f'diagrams.py:{n} {k}: {type(e).__name__}: {e}')
    tmp = REND.parent / 'tmp'
    wordsvg.rasterize(svgs, lambda k: tmp / (k.replace('/', '__') + '.webp'))
    REND.mkdir(parents=True, exist_ok=True)
    stale = []
    for k in svgs:
        f = tmp / (k.replace('/', '__') + '.webp')
        im = Image.open(f).convert('RGB')
        im.save(REND / f.with_suffix('.png').name)
        f.unlink()
        art = allc[k]['art']
        if art.exists():
            d = ImageStat.Stat(ImageChops.difference(im, Image.open(art).convert('RGB'))).mean
            if sum(d) / 3 > 2.0:
                stale.append((k, round(sum(d) / 3, 1)))
        else:
            stale.append((k, 'no published picture'))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'render.json').write_text(json.dumps({'rendered': len(svgs), 'errors': errors, 'differs_from_published': stale}, indent=1), encoding='utf-8')
    print(f'{len(svgs)} diagrams rendered to {REND}, {len(errors)} errors, {len(stale)} differ from the published webp')


# ---------- CLIP ----------

def feats(o):
    """transformers 5 returns an output object (the projected embedding is pooler_output), 4.x a tensor."""
    return (o if hasattr(o, 'float') else o.pooler_output).float()


def clip():
    import torch
    from PIL import Image
    from transformers import CLIPModel, CLIPProcessor
    cs = cards()
    name = 'openai/clip-vit-large-patch14'
    model = CLIPModel.from_pretrained(name, torch_dtype=torch.float16).cuda().eval()
    proc = CLIPProcessor.from_pretrained(name)
    tok = proc.tokenizer
    ie, te = [], []
    with torch.no_grad():
        for s in range(0, len(cs), 64):
            b = cs[s:s + 64]
            ims = [Image.open(c['img']).convert('RGB') for c in b]
            px = proc(images=ims, return_tensors='pt')['pixel_values'].cuda().half()
            ie.append(torch.nn.functional.normalize(feats(model.get_image_features(pixel_values=px)), dim=-1).cpu())
            txt = [f"a picture of {c['word']}: {c['definition']}" for c in b]
            t = tok(txt, padding=True, truncation=True, max_length=77, return_tensors='pt').to('cuda')
            te.append(torch.nn.functional.normalize(feats(model.get_text_features(**t)), dim=-1).cpu())
    ie, te = torch.cat(ie), torch.cat(te)
    score = (ie * te).sum(-1).tolist()
    for c, s in zip(cs, score):
        c['clip'] = s
    # rank within subject (percentile, 0 = worst) and within module (does it pick its own word among the module's words?)
    by_sub, by_mod = defaultdict(list), defaultdict(list)
    for i, c in enumerate(cs):
        by_sub[c['subject']].append(i)
        by_mod[c['module_id']].append(i)
    for idx in by_sub.values():
        order = sorted(idx, key=lambda i: cs[i]['clip'])
        for r, i in enumerate(order):
            cs[i]['clip_pct'] = r / max(len(order) - 1, 1)
    for idx in by_mod.values():
        sims = ie[idx] @ te[idx].T  # image x text
        for a, i in enumerate(idx):
            row = sims[a]
            cs[i]['mod_rank'] = int((row > row[a]).sum()) + 1
            cs[i]['mod_n'] = len(idx)
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / 'clip.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['key', 'subject', 'kind', 'clip', 'clip_pct', 'mod_rank', 'mod_n'])
        for c in cs:
            w.writerow([c['key'], c['subject'], c['kind'], f"{c['clip']:.4f}", f"{c['clip_pct']:.3f}", c['mod_rank'], c['mod_n']])
    print(f'{len(cs)} cards scored, clip.csv written')


# ---------- Qwen3-VL ----------

PROMPT = ('You are checking a picture card for a classroom word wall ({band}). The card teaches the word "{word}", '
          'which means: {definition}. The picture is {what}.\n'
          'Rate how well the picture shows this word. 5 = a student would name or understand the word from the picture. '
          '4 = clearly fits the word. 3 = related but vague, or it fits other words just as well. 2 = weak or confusing. '
          '1 = wrong or misleading for this word.\n'
          'Answer with strict JSON only, no other text: {{"match": <1-5>, "shows": "<what the picture shows, a few words>", '
          '"problem": "<the problem if match is 3 or less, else empty>"}}')
WHAT = {'svg': 'a simple diagram drawn in code', 'paint': 'a simple flat illustration',
        'people': 'a simple flat illustration with people', 'gpt': 'a simple flat illustration'}


def nodash(s):
    """House rule: no em dashes anywhere, model text included."""
    return re.sub('\\s*\u2014\\s*', ', ', s)


def parse(txt):
    txt = nodash(txt)
    m = re.search(r'\{.*\}', txt, re.S)
    if m:
        try:
            d = json.loads(m.group(0))
            return {'match': int(d.get('match', 0)), 'shows': str(d.get('shows', '')), 'problem': str(d.get('problem', ''))}
        except Exception:  # noqa: BLE001
            pass
    m = re.search(r'"match"\s*:\s*(\d)', txt)
    return {'match': int(m.group(1)) if m else 0, 'shows': '', 'problem': '', 'raw': txt[:300]}


def qwen():
    import torch
    from PIL import Image
    from transformers import AutoProcessor, Qwen3VLForConditionalGeneration
    a = sys.argv
    bs = int(a[a.index('--batch') + 1]) if '--batch' in a else 12
    limit = int(a[a.index('--limit') + 1]) if '--limit' in a else None
    OUT.mkdir(parents=True, exist_ok=True)
    res = OUT / 'qwen.jsonl'
    done = set()
    if res.exists():
        for l in res.read_text(encoding='utf-8').splitlines():
            try:
                done.add(json.loads(l)['key'])
            except Exception:  # noqa: BLE001
                pass
    todo = [c for c in cards() if c['key'] not in done][:limit]
    print(f'{len(done)} done, {len(todo)} to go', flush=True)
    if not todo:
        return
    name = 'Qwen/Qwen3-VL-4B-Instruct'
    model = Qwen3VLForConditionalGeneration.from_pretrained(name, dtype=torch.bfloat16, device_map='cuda').eval()
    proc = AutoProcessor.from_pretrained(name)
    proc.tokenizer.padding_side = 'left'
    t0 = time.time()
    with open(res, 'a', encoding='utf-8') as f:
        for s in range(0, len(todo), bs):
            b = todo[s:s + bs]
            msgs = [[{'role': 'user', 'content': [
                {'type': 'image'},
                {'type': 'text', 'text': PROMPT.format(band=BANDS[c['band']], word=c['word'], definition=c['definition'],
                                                       what=WHAT[c['kind']])}]}] for c in b]
            texts = [proc.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in msgs]
            ims = [Image.open(c['img']).convert('RGB').resize((448, 448)) for c in b]
            inp = proc(text=texts, images=ims, return_tensors='pt', padding=True).to('cuda')
            with torch.no_grad():
                out = model.generate(**inp, max_new_tokens=96, do_sample=False)
            dec = proc.batch_decode(out[:, inp['input_ids'].shape[1]:], skip_special_tokens=True)
            for c, d in zip(b, dec):
                f.write(json.dumps(dict(key=c['key'], **parse(d)), ensure_ascii=False) + '\n')
            f.flush()
            n = s + len(b)
            el = time.time() - t0
            print(f'{n}/{len(todo)}  {el / n:.2f}s a card, about {el / n * (len(todo) - n) / 60:.0f} min left', flush=True)


# ---------- combine ----------

def prior_audits():
    """{key: 'VERDICT (file)'} from the earlier paintings and diagrams audits."""
    out = {}
    for fn in ('WORDWALL-PAINTINGS.md', 'WORDWALL-DIAGRAMS.md'):
        for l in (ROOT / 'docs' / 'agents' / 'audit' / fn).read_text(encoding='utf-8').splitlines():
            cells = [x.strip() for x in l.strip().strip('|').split('|')]
            for i, x in enumerate(cells):
                if x in ('REDO', 'CODE', 'FIX', 'PAINT'):
                    keys = [y for y in cells if re.fullmatch(r'[a-z0-9-]+/[a-z0-9-]+', y)]
                    if keys:
                        out[keys[0]] = f'{x} in {fn}'
                    break
    return out


def changed_since(date='2026-10-27T23:00'):
    """Art files committed after the earlier audits were written."""
    r = subprocess.run(['git', 'log', f'--since={date}', '--name-only', '--format=', '--', 'closet/words/art'],
                       cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    return {Path(p).as_posix() for p in r.stdout.split() if p.endswith('.webp')}


def combine():
    from html import escape
    cs = {c['key']: c for c in cards()}
    for r in csv.DictReader(open(OUT / 'clip.csv', encoding='utf-8')):
        if r['key'] in cs:
            cs[r['key']].update(clip=float(r['clip']), clip_pct=float(r['clip_pct']), mod_rank=int(r['mod_rank']), mod_n=int(r['mod_n']))
    for l in (OUT / 'qwen.jsonl').read_text(encoding='utf-8').splitlines():
        d = json.loads(l)
        if d['key'] in cs:
            cs[d['key']].update(q=d['match'], shows=nodash(d.get('shows', '')), problem=nodash(d.get('problem', '')))
    prior, changed = prior_audits(), changed_since()
    rows = []
    for c in cs.values():
        q, low = c.get('q', 0), c.get('clip_pct', 1) < 0.10
        if c['kind'] == 'svg' and c['text']:
            flag = 'diagram-text' if (q == 1 or (q == 2 and low)) else ''
        else:
            flag = ('qwen-1-2' if q in (1, 2) else 'qwen-3+clip' if q == 3 and low else '')
        c['flag'] = flag
        c['prior'] = prior.get(c['key'], '')
        if c['prior']:
            rel = Path(c['art']).relative_to(ROOT).as_posix()
            c['prior'] += ', picture changed since' if rel in changed else ', picture not changed since'
        rows.append(c)
    cols = ['key', 'subject', 'band', 'kind', 'text', 'word', 'definition', 'picture', 'q', 'shows', 'problem', 'clip',
            'clip_pct', 'mod_rank', 'mod_n', 'flag', 'prior']
    with open(OUT / 'flags.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, cols, extrasaction='ignore')
        w.writeheader()
        for c in sorted(rows, key=lambda c: (c['subject'], c['key'])):
            w.writerow(c)
    flagged = [c for c in rows if c['flag']]
    by = defaultdict(list)
    for c in flagged:
        by[c['subject']].append(c)
    css = ('body{font:14px Segoe UI,Arial,sans-serif;margin:16px;background:#fff;color:#1f2430}h2{margin-top:28px}'
           '.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}'
           '.c{border:1px solid #ccd;border-radius:8px;padding:8px}.c img{width:100%;aspect-ratio:1;object-fit:contain;'
           'background:#fafafa}.w{font-weight:700;color:#b23a17}.k{font-size:11px;color:#667;word-break:break-all}'
           '.d{margin:3px 0}.s{color:#2f5f9e}.p{color:#a33}.m{font-size:12px;color:#445}.f{font-size:11px;background:#fde3c8;'
           'border-radius:4px;padding:1px 5px}.pr{font-size:11px;background:#e8dcf5;border-radius:4px;padding:1px 5px}')
    out = [f'<!doctype html><meta charset="utf-8"><title>Word Wall picture review</title><style>{css}</style>',
           f'<h1>Word Wall picture review: {len(flagged)} flagged of {len(rows)}</h1>',
           '<p>Flag kinds: <b>qwen-1-2</b> Qwen3-VL-4B rated 1 or 2; <b>qwen-3+clip</b> rated 3 and the CLIP score is in the '
           'bottom 10% of its subject; <b>diagram-text</b> a diagram with text labels rated 1, or 2 with a bottom-10% CLIP '
           '(small vision models read labels poorly, so these are weaker signals). Purple tag: the card was in an earlier '
           'audit. Diagram images are the fresh renders in closet/words/art/_raw/review (run the render step first).</p>',
           '<p>' + ' &middot; '.join(f'<a href="#{s}">{s} ({len(v)})</a>' for s, v in sorted(by.items())) + '</p>']
    for s, v in sorted(by.items()):
        out.append(f'<h2 id="{s}">{s} ({len(v)})</h2><div class="g">')
        for c in sorted(v, key=lambda c: (c['flag'] == 'diagram-text', c.get('q', 0), c.get('clip_pct', 1))):
            src = Path(c['img']).relative_to(ROOT).as_posix()
            out.append(
                f'<div class="c"><img loading="lazy" src="../../../../{src}"><div class="w">{escape(c["word"])}</div>'
                f'<div class="d">{escape(c["definition"])}</div>'
                f'<div class="m">{c["band"]} &middot; {c["kind"]} &middot; Qwen {c.get("q", "?")} &middot; CLIP pct '
                f'{c.get("clip_pct", 0):.2f} &middot; own word {c.get("mod_rank", "?")}/{c.get("mod_n", "?")} in module</div>'
                f'<div class="s">shows: {escape(c.get("shows", ""))}</div><div class="p">{escape(c.get("problem", ""))}</div>'
                f'<span class="f">{c["flag"]}</span> ' + (f'<span class="pr">{escape(c["prior"])}</span>' if c['prior'] else '') +
                f'<div class="k">{escape(c["key"])}<br>prompt: {escape(c["picture"][:120])}</div></div>')
        out.append('</div>')
    (OUT / 'index.html').write_text('\n'.join(out), encoding='utf-8')
    cnt = defaultdict(lambda: defaultdict(int))
    for c in rows:
        cnt[c['subject']]['cards'] += 1
        cnt[c['subject']][c['flag'] or 'ok'] += 1
    print(f'{len(flagged)} flagged of {len(rows)}')
    print('subject', 'cards', 'qwen-1-2', 'qwen-3+clip', 'diagram-text', sep='\t')
    for s in sorted(cnt):
        print(s, cnt[s]['cards'], cnt[s]['qwen-1-2'], cnt[s]['qwen-3+clip'], cnt[s]['diagram-text'], sep='\t')
    qd = defaultdict(int)
    for c in rows:
        qd[c.get('q', 0)] += 1
    print('qwen scores', dict(sorted(qd.items())))


if __name__ == '__main__':
    {'render': render, 'clip': clip, 'qwen': qwen, 'combine': combine}[sys.argv[1]]()
