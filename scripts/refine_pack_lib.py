r"""Helpers for scripts/refine_pack.py: a small JavaScript scanner, the src.html outline, the string lists and the
contact sheets. Nothing here starts Chrome or writes into the repo.
"""
import html as htmllib
import re
from html.parser import HTMLParser
from pathlib import Path

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
REGEX_AFTER = set('(,=:[!&|?{};+-*%<>~^')
REGEX_WORDS = ('return', 'typeof', 'case', 'in', 'of', 'do', 'else', 'void', 'throw', 'new', 'delete')


class Lines:
    """Offsets to 1-based line numbers for one text."""
    def __init__(self, text):
        self.starts = [0]
        for m in re.finditer('\n', text):
            self.starts.append(m.end())

    def line(self, off):
        lo, hi = 0, len(self.starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.starts[mid] <= off: lo = mid
            else: hi = mid - 1
        return lo + 1

    def offset(self, line, col=0):
        return self.starts[line - 1] + col


def scan_js(code):
    """One pass over JavaScript. Returns (mask, strings, comments): mask is the code with every string, template,
    regex and comment blanked to spaces (same length, newlines kept), so braces and names can be matched safely;
    strings is [(start, end, quote, raw text without quotes)]; comments is [(start, end, text)]."""
    n, i, out, strings, comments = len(code), 0, list(code), [], []

    def blank(a, b):
        for k in range(a, b):
            if out[k] != '\n': out[k] = ' '

    def prev_sig(k):
        k -= 1
        while k >= 0 and code[k] in ' \t\r\n': k -= 1
        return k

    def template(a):
        # a is the opening backtick; returns the index after the closing one. ${ } parts are skipped with nesting.
        k = a + 1
        while k < n:
            c = code[k]
            if c == '\\': k += 2; continue
            if c == '`': return k + 1
            if c == '$' and k + 1 < n and code[k + 1] == '{':
                depth, k = 1, k + 2
                while k < n and depth:
                    c = code[k]
                    if c == '\\': k += 2; continue
                    if c == '`': k = template(k); continue
                    if c in '\'"':
                        q, k = c, k + 1
                        while k < n and code[k] != q and code[k] != '\n':
                            k += 2 if code[k] == '\\' else 1
                        k += 1; continue
                    if c == '{': depth += 1
                    elif c == '}': depth -= 1
                    k += 1
                continue
            k += 1
        return n

    while i < n:
        c = code[i]
        if c == '/' and i + 1 < n and code[i + 1] == '/':
            j = code.find('\n', i); j = n if j < 0 else j
            comments.append((i, j, code[i + 2:j].strip())); blank(i, j); i = j; continue
        if c == '/' and i + 1 < n and code[i + 1] == '*':
            j = code.find('*/', i + 2); j = n if j < 0 else j + 2
            comments.append((i, j, code[i + 2:j - 2].strip())); blank(i, j); i = j; continue
        if c in '\'"':
            j = i + 1
            while j < n and code[j] != c and code[j] != '\n':
                j += 2 if code[j] == '\\' else 1
            strings.append((i, min(j + 1, n), c, code[i + 1:j])); blank(i, min(j + 1, n)); i = j + 1; continue
        if c == '`':
            j = template(i)
            strings.append((i, j, '`', code[i + 1:j - 1])); blank(i, j); i = j; continue
        if c == '/':
            p = prev_sig(i)
            word = re.search(r'([A-Za-z_$]+)$', code[max(0, p - 10):p + 1]) if p >= 0 else None
            if p < 0 or code[p] in REGEX_AFTER or (word and word.group(1) in REGEX_WORDS):
                j, cls, ok = i + 1, False, False
                while j < n and code[j] != '\n':
                    d = code[j]
                    if d == '\\': j += 2; continue
                    if d == '[': cls = True
                    elif d == ']': cls = False
                    elif d == '/' and not cls: ok = True; break
                    j += 1
                if ok:
                    blank(i, j + 1); i = j + 1; continue
        i += 1
    return ''.join(out), strings, comments


def match_close(mask, open_at):
    """Index of the bracket that closes the one at open_at (in a masked text), or -1."""
    pairs = {'{': '}', '[': ']', '(': ')'}
    o, c, depth = mask[open_at], pairs[mask[open_at]], 0
    for k in range(open_at, len(mask)):
        ch = mask[k]
        if ch == o: depth += 1
        elif ch == c:
            depth -= 1
            if not depth: return k
    return -1


class Doc(HTMLParser):
    """src.html as blocks: style and script ranges, elements with an id, and the text a student could read."""
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.text, self.L = text, Lines(text)
        self.stack, self.ids, self.blocks, self.strings = [], [], [], []
        self.raw = None  # (tag, start offset of its content, attrs)
        self.feed(text); self.close()

    def off(self):
        ln, col = self.getpos()
        return self.L.offset(ln, col)

    def where(self):
        return ['#' + i for _, i in self.stack if i]

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        ln = self.getpos()[0]
        if tag in ('script', 'style'):
            end = self.off() + len(self.get_starttag_text() or '')
            self.raw = (tag, end, a)
            if a.get('src') or tag == 'style':
                pass
        if a.get('id') and tag not in ('script', 'style'):
            self.ids.append((ln, len(self.stack), tag, a['id'], (a.get('class') or '').strip(), a.get('hidden') is not None or 'hidden' in a))
        for k in ('aria-label', 'title', 'placeholder', 'alt'):
            if a.get(k) and a[k].strip():
                self.strings.append((ln, k, a[k].strip(), self.where() + (['#' + a['id']] if a.get('id') else [])))
        if tag == 'input' and a.get('type') in ('button', 'submit') and a.get('value'):
            self.strings.append((ln, 'value', a['value'].strip(), self.where()))
        if tag == 'meta' and a.get('name') == 'description' and a.get('content'):
            self.strings.append((ln, 'meta description', a['content'].strip(), ['head']))
        if tag == 'link' and (a.get('href') or '').startswith('kit:'):
            self.blocks.append(('kit css', ln, ln, a['href'], 0, 0))
        if tag not in VOID:
            self.stack.append((tag, a.get('id')))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if self.raw and tag == self.raw[0]:
            t, start, a = self.raw
            end = self.off()
            kind = ('script ' + a['src']) if a.get('src') else ('data ' + a.get('type', '')) if t == 'script' and a.get('type') not in (None, '', 'text/javascript', 'module') else t
            self.blocks.append((kind, self.L.line(start), self.L.line(end), '', start, end))
            self.raw = None
        for k in range(len(self.stack) - 1, -1, -1):
            if self.stack[k][0] == tag:
                del self.stack[k:]
                break

    def handle_data(self, data):
        if self.raw:
            return
        s = re.sub(r'\s+', ' ', data).strip()
        if s and re.search(r'[A-Za-z0-9]', s):
            tag = self.stack[-1][0] if self.stack else ''
            self.strings.append((self.getpos()[0], 'title' if tag == 'title' else 'text', s, self.where() or ([tag] if tag else [])))


def outline(src):
    """Markdown outline of src.html: blocks, elements with an id, CSS landmarks, and for each script its sections,
    data tables and functions with line ranges. Returns (markdown, ranges) where ranges is
    [(start offset, end offset, label)] for grouping strings."""
    d = Doc(src)
    L = d.L
    total = len(L.starts)
    longest = max((len(x) for x in src.split('\n')), default=0)
    md = [f'{total} lines, {len(src) // 1024} KB, longest line {longest} characters.']
    if longest > 1500:
        md.append('Some lines are very long (minified): a line range below can hold many functions. Search for the '
                  'name (Grep with -o and a short context pattern) rather than reading the whole line.')
    md += ['', '## Blocks', '', '| lines | what |', '|---|---|']
    for kind, a, b, extra, s, e in sorted(d.blocks, key=lambda x: x[1]):
        md.append(f'| {a}-{b} | {kind} {extra}'.rstrip() + (f' ({(e - s) // 1024} KB)' if e - s > 1024 else '') + ' |')
    md += ['', '## Elements with an id (markup order; indent is nesting)', '']
    base = min((dep for _, dep, *_ in d.ids), default=0)
    for ln, dep, tag, i, cls, hidden in d.ids:
        md.append(f'{"  " * min(dep - base, 6)}- L{ln} `{tag}#{i}`' + (f' .{cls.replace(" ", ".")}' if cls else '') + (' (hidden at load)' if hidden else ''))
    ranges = []
    for kind, a, b, extra, s, e in sorted(d.blocks, key=lambda x: x[1]):
        if kind == 'style':
            css = src[s:e]
            marks = [(L.line(s + m.start()), 'comment: ' + re.sub(r'\s+', ' ', m.group(1)).strip()[:90]) for m in re.finditer(r'/\*(.*?)\*/', css, re.S)]
            marks += [(L.line(s + m.start()), m.group(0).strip()[:90]) for m in re.finditer(r'@(?:media|keyframes|supports|container)[^{]*', css)]
            md += ['', f'## Style block, lines {a}-{b}', '']
            md += [f'- L{ln} {what}' for ln, what in sorted(marks)[:80]] or ['- no comments or @ rules to mark; search by selector']
        elif kind == 'script':
            md += ['', f'## Script, lines {a}-{b}', '']
            rows, rg = js_outline(src[s:e], s, L)
            md += rows
            ranges += rg
    return '\n'.join(md) + '\n', ranges, d


def js_outline(code, base, L):
    mask, strings, comments = scan_js(code)
    depth, dep = [0] * (len(mask) + 1), 0
    for k, ch in enumerate(mask):
        if ch == '}': dep -= 1
        depth[k] = dep
        if ch == '{': dep += 1
    items = []  # (start, end, depth, kind, name, note)
    for m in re.finditer(r'(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)\s*\(', mask):
        p = match_close(mask, m.end() - 1)
        b = mask.find('{', p) if p > 0 else -1
        e = match_close(mask, b) if b > 0 else -1
        if e > 0:
            items.append((m.start(), e, depth[m.start()], 'function', m.group(1), re.sub(r'\s+', ' ', code[m.end() - 1:p + 1])[:60]))
    for m in re.finditer(r'(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:\([^()]*\)|[A-Za-z_$][\w$]*)\s*=>\s*\{', mask):
        e = match_close(mask, m.end() - 1)
        if e > 0 and e - m.start() > 160:
            items.append((m.start(), e, depth[m.start()], 'function', m.group(1), '=>'))
    for m in re.finditer(r'(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:Object\.freeze\(|new\s+(?:Map|Set)\()?\s*([\[{])', mask):
        e = match_close(mask, m.end() - 1)
        if e > 0 and e - m.start() > 240:
            nstr = sum(1 for s in strings if m.start() < s[0] < e)
            items.append((m.start(), e, depth[m.start()], 'data', m.group(1), f'{(e - m.start())} chars, {nstr} strings'))
    for rx, name in ((r'Curio\.voice\s*\(', 'Curio.voice(...)'), (r'Curio\.init\s*\(', 'Curio.init(...)'), (r'window\.__tool\s*=', 'window.__tool = ...')):
        for m in re.finditer(rx, mask):
            b = m.end() - 1 if mask[m.end() - 1] == '(' else mask.find('{', m.end())
            e = match_close(mask, b) if b > 0 else m.end()
            items.append((m.start(), max(e, m.end()), depth[m.start()], 'call', name, ''))
    for a, b, text in comments:
        t = re.sub(r'\s+', ' ', text)
        if re.match(r'^[-=*#~_ ]{3,}', t) or re.search(r'[-=*#~_]{4,}\s*$', t):
            name = t.strip('-=*#~_ ').strip()
            if name:
                items.append((a, b, depth[a], 'section', name[:90], ''))
    fdepths = [x[2] for x in items if x[3] == 'function']
    d0 = min(fdepths) if fdepths else 0
    items = sorted(set(x for x in items if x[2] <= d0 + (1 if x[3] == 'function' else 2)))
    rows, ranges, seen = [], [], set()
    for s, e, dp, kind, name, note in items:
        if (s, kind) in seen: continue
        seen.add((s, kind))
        la, lb = L.line(base + s), L.line(base + e)
        span = f'L{la}' if la == lb else f'L{la}-{lb}'
        size = f' ({e - s} chars)' if la == lb and e - s > 400 else ''
        ind = '  ' * max(0, min(dp - d0, 3))
        if kind == 'section':
            rows.append(f'- {span} **{name}**')
        elif kind == 'function':
            rows.append(f'{ind}- {span} `{name}{note if note != "=>" else "() =>"}`{size}')
            ranges.append((base + s, base + e, f'function {name}'))
        elif kind == 'data':
            rows.append(f'{ind}- {span} data `{name}` ({note})')
            ranges.append((base + s, base + e, f'data {name}'))
        else:
            rows.append(f'{ind}- {span} {name}{size}')
            if 'voice' in name: ranges.append((base + s, base + e, 'Curio.voice options'))
    if not rows:
        rows = ['- nothing found to mark (search the script by name)']
    return rows, ranges


CODEISH = re.compile(r'^[#.\[@:/\\]|^(https?|data|blob|file):|[{};]|^\s*[\w$]+\([^)]*\)\s*$|^[a-z0-9_-]+(\.[a-z0-9_-]+)+$|^[\w-]+:\s*[\w#-]+$|^(M|m)[\d .,-]+[A-Za-z]|^[a-z]+(-[a-z0-9]+)+$|^[a-z]+[A-Z]\w*$')


def unescape_js(raw):
    return re.sub(r'\\(u[0-9a-fA-F]{4}|x[0-9a-fA-F]{2}|.)', lambda m: chr(int(m.group(1)[1:], 16)) if m.group(1)[0] in 'ux' and len(m.group(1)) > 1
                  else {'n': '\n', 't': '\t'}.get(m.group(1), m.group(1)), raw)


def display_strings(src, doc, ranges):
    """String literals in the scripts that a student could read or hear: [(line, text, group)]."""
    out, L = [], doc.L
    for kind, a, b, extra, s, e in doc.blocks:
        if kind != 'script':
            continue
        mask, strings, comments = scan_js(src[s:e])
        for st, en, q, raw in strings:
            text = unescape_js(raw)
            if q == '`':
                text = re.sub(r'\$\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', '{..}', text)
            pieces = [text]
            if '<' in text and '>' in text:  # markup built in a string: keep the words between the tags and the labels
                pieces = re.findall(r'(?:aria-label|title|placeholder|alt)="([^"]+)"', text) + [p for p in re.split(r'<[^>]*>', text)]
            for p in pieces:
                p = htmllib.unescape(re.sub(r'\s+', ' ', p)).strip()
                if len(p) < 2 or not re.search(r'[A-Za-z]{2}', p) or CODEISH.search(p) or p == 'use strict':
                    continue
                if ' ' not in p and not (p[0].isupper() and p[1:].islower() and len(p) > 2) and not p.endswith(('!', '?', '.')):
                    continue
                if ' ' in p and not re.search(r'[A-Za-z]{2,}\s+[A-Za-z0-9{]', p):
                    continue
                if re.fullmatch(r'[\w$.\s,()=>+*/%<>!&|?:\[\]\'"-]*[=<>&|]{2}[\w$.\s,()=>+*/%<>!&|?:\[\]\'"-]*', p):
                    continue
                off = s + st
                grp = [lab for ra, rb, lab in ranges if ra <= off <= rb]
                out.append((L.line(off), p, grp[-1] if grp else 'top of the script'))
    return out


def find_lines(src, L, text, limit=4):
    """Lines of src.html where this exact text sits as a literal (plain, with \\' or with HTML entities)."""
    forms = {text, text.replace("'", "\\'"), text.replace('"', '\\"'), htmllib.escape(text, quote=False), text.replace("'", '&#39;'), text.replace("'", '’')}
    hits = set()
    for f in forms:
        k = src.find(f)
        while k >= 0 and len(hits) < limit:
            hits.add(L.line(k)); k = src.find(f, k + 1)
    return sorted(hits)


def line_keys(src, texts):
    """For each spoken text found as a literal with a key before it (key: 'text'), the key."""
    keys = {}
    for t in texts:
        for f in (t, t.replace("'", "\\'"), t.replace('"', '\\"')):
            m = re.search(r'([A-Za-z_$][\w$]*)\s*:\s*[\'"`]' + re.escape(f) + r'[\'"`]', src)
            if m:
                keys[t] = m.group(1); break
    return keys


# ---------- contact sheets ----------

def contact_sheets(cells, out, prefix, title, max_w=1568, max_h=1900, cell_w=772, cell_h=900):
    """cells: [(label, png path)]. Packs them, scaled to fit cell_w x cell_h, into labeled JPEG sheets of at most
    max_w x max_h. Returns [(file name, [labels])]."""
    from PIL import Image, ImageDraw, ImageFont
    try:
        font = ImageFont.truetype('arial.ttf', 15); big = ImageFont.truetype('arialbd.ttf', 17)
    except Exception:
        font = big = ImageFont.load_default()
    pad, lab_h, head = 8, 22, 28
    ims = []
    for label, p in cells:
        try:
            im = Image.open(p).convert('RGB')
        except Exception:
            continue
        sc = min(1, cell_w / im.width, cell_h / im.height)
        if sc < 1:
            im = im.resize((max(1, round(im.width * sc)), max(1, round(im.height * sc))), Image.LANCZOS)
        ims.append((label, im, sc))
    pages, rows, row, x, y = [], [], [], pad, head
    def flush_row():
        nonlocal row, y, x
        if row:
            h = max(im.height for _, im, _ in row) + lab_h + pad
            rows.append((y, row)); y += h; row = []; x = pad
    def flush_page():
        nonlocal rows, y
        flush_row()
        if rows:
            pages.append((y, rows)); rows = []; y = head
    for label, im, sc in ims:
        if x + im.width + pad > max_w:
            flush_row()
        if y + im.height + lab_h + pad > max_h and (rows or row):
            flush_page()
        row.append((label, im, sc)); x += im.width + pad
    flush_page()
    made = []
    for n, (h, rws) in enumerate(pages, 1):
        w = max(sum(im.width + pad for _, im, _ in r) + pad for _, r in rws)
        sheet = Image.new('RGB', (max(w, 400), h + pad), (40, 44, 52))
        dr = ImageDraw.Draw(sheet)
        name = f'{prefix}{"-" + str(n) if len(pages) > 1 else ""}.jpg'
        dr.text((pad, 5), f'{title}{f" ({n} of {len(pages)})" if len(pages) > 1 else ""}', fill=(255, 255, 255), font=big)
        labels = []
        for ry, r in rws:
            cx = pad
            for label, im, sc in r:
                dr.text((cx, ry + 2), label + (f'  [{round(sc * 100)}%]' if sc < 1 else ''), fill=(255, 220, 120), font=font)
                sheet.paste(im, (cx, ry + lab_h))
                cx += im.width + pad; labels.append(label)
        sheet.save(Path(out) / name, quality=80, optimize=True)
        made.append((name, labels))
    return made
