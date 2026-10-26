"""Turn the downloaded Reading Room sources into readable stories: library/<id>/text.md, story.json and art/.

Gutenberg rows are cut from the illustrated EPUB: the section whose heading matches the row's title (the `find` text
picks between repeats), or the whole book when the source is one work. Pictures come along, scaled down, as art/NN.jpg.
StoryWeaver rows become one page per spread with its picture. Wikisource, Internet Archive, Sefaria and PDF sources
(library/_sources/other/<key>/text.txt) are handled by `other()`. The original text is kept word for word: only
Gutenberg furniture (page numbers, licence, contents lists, transcriber notes) is dropped.

    python scripts/library_process.py              every row without a library/<id>/text.md yet
    python scripts/library_process.py ID ...       just these rows (redone even if they exist)
    python scripts/library_process.py --redo       every book row again (StoryWeaver rows are left alone)
    python scripts/library_process.py --report     also write library/_sources/process-report.csv
    python scripts/library_process.py --outline SOURCE [words]   headings (or blocks with the words), for cuts

Fixes go in data/library/cuts.csv (id, pick, why); apply_cut() has the pick syntax.

A folder with "hand": true in story.json is never overwritten. Each run prints the rows it could not place.
"""
import csv
import html
import io
import json
import pathlib
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB, SRC, DATA = ROOT / "library", ROOT / "library" / "_sources", ROOT / "data" / "library"
X = "{http://www.w3.org/1999/xhtml}"
WHOLE = {"novel", "chapter book", "chapter set", "picture book", "play", "memoir", "nonfiction", "epic", "document",
         "scripture", "speech"}
FRONT = re.compile(r"^(contents|table of contents|list of (illustrations|plates|colou?red plates)|illustrations|"
                   r"transcriber.*|index|footnotes|notes|the full project gutenberg.*|preface.*|introduction|"
                   r"introductory note|publisher.*note|bibliography|by the same author.*|.*produced by.*)$")
SMALL = {"a", "an", "and", "the", "of", "in", "on", "at", "to", "for", "by", "or", "with", "from", "as", "but", "nor"}
ROMAN = re.compile(r"(?=[IVXLC])C{0,3}(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")
CHAPTER = re.compile(r"^(chapter|part|book|canto|scene|act|section|stave|fit|chap\.?)\b|^[ivxlc]+\.?$|^\d+\.?$")
ART_W = 800  # widest picture we keep, in px
CUTS = {r["id"]: r["pick"] for r in csv.DictReader(open(DATA / "cuts.csv", encoding="utf-8"))} if (DATA / "cuts.csv").exists() else {}


def norm(s):
    s = re.sub(r"[^a-z0-9]+", " ", s.lower().replace("’", "'").replace("'", "")).strip()
    return re.sub(r"^(the|a|an) ", "", s)


# ---- EPUB to blocks ------------------------------------------------------------------------------------------------

def md_escape(t):
    t = t.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`").replace("{", "\\{")
    return t


def inline(el, drop):
    """Markdown for an element's inline content. `drop` collects page-number spans etc. to skip."""
    out = [md_escape(el.text or "")]
    for c in el:
        tag, cls = c.tag.replace(X, ""), c.get("class", "")
        if "pageno" in cls or "pagenum" in cls or tag in ("script", "style"):
            pass
        elif tag == "br":
            out.append("  \n")
        elif tag == "img":
            alt = c.get("alt", "")
            if len(alt) == 1 and alt.isalpha():
                out.append(alt)
        elif tag in ("i", "em", "cite"):
            inner = inline(c, drop).strip()
            out.append(f"*{inner}*" if inner else "")
        elif tag in ("b", "strong"):
            inner = inline(c, drop).strip()
            out.append(f"**{inner}**" if inner else "")
        else:
            out.append(inline(c, drop))
        out.append(md_escape(c.tail or ""))
    return "".join(out)


def clean(t):
    t = re.sub(r"[ \t\r\n]+", " ", t.replace("  \n", "\x00")).replace("\x00", "  \n")
    t = re.sub(r" *  \n *", "  \n", t).strip()
    return re.sub(r"^(\d+)\. ", r"\1\\. ", re.sub(r"^([#>+\-]) ", r"\\\1 ", t))


BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "table", "ul", "ol", "li", "hr", "img",
         "figure", "section", "pre", "dl", "dd", "dt", "center", "header", "footer", "figcaption", "body", "tr", "td"}


def has_block(el):
    return any(c.tag.replace(X, "") in BLOCK for c in el.iter() if c is not el)


def titled_poems(el, base, blocks):
    """Read a poem div in document order: a title div is a heading, text between <br>s is a line, a nested poem
    div is the next rhyme. Indents count from the poem's own left margin."""
    raw = [""]

    def flush():
        lead = [len(re.match(r"[\r\n]*([ \xa0]*)", x)[1]) for x in raw if clean(x)]
        lines = []
        for x in raw:
            if clean(x):
                lines.append("\u2003\u2003" * (len(re.match(r"[\r\n]*([ \xa0]*)", x)[1]) - min(lead) >= 2) + clean(x))
            elif lines and lines[-1]:
                lines.append("")
        while lines and not lines[-1]:
            lines.pop()
        if lines:
            blocks.append(("poem", lines))
        raw[:] = [""]

    def go(e):
        raw[-1] += e.text or ""
        for c in e:
            t, k = c.tag.replace(X, ""), c.get("class", "")
            if t == "br":
                raw.append("")
            elif t == "div" and "title" in k:
                flush()
                blocks.append(("h", 3, clean(re.sub(r"\s+", " ", "".join(c.itertext())))))
            elif t == "div" and "poem" in k:
                flush()
                go(c)
                flush()
            elif t == "img" or list(c.iter(X + "img")):
                for i in c.iter(X + "img"):
                    blocks.append(("img", posixpath.normpath(posixpath.join(base, i.get("src", ""))), i.get("alt", "")))
            else:
                raw[-1] += "".join(c.itertext())
            raw[-1] += c.tail or ""
    go(el)
    flush()


def walk(el, base, blocks, state):
    tag, cls, eid = el.tag.replace(X, ""), el.get("class", ""), el.get("id", "")
    if eid in ("pg-header", "pg-footer") or "pg-boilerplate" in cls or "toc" in cls.split() or "tnote" in cls or "transnote" in cls or tag in ("script", "style"):
        return
    if re.fullmatch(r"h[1-6]", tag):
        text = clean(re.sub(r"\s+", " ", "".join(el.itertext())))
        imgs = [i for i in el.iter(X + "img")]
        for i in imgs:
            blocks.append(("img", posixpath.normpath(posixpath.join(base, i.get("src", ""))), i.get("alt", "")))
        if text:
            blocks.append(("h", int(tag[1]), text))
        return
    if tag == "hr":
        blocks.append(("hr",))
        return
    if tag == "pre":  # verse set in <pre>: its own line breaks, indents from its left margin
        raw = "".join(el.itertext()).replace("\t", "    ").split("\n")
        lines = []  # (indent, text), "" between stanzas

        def flush():
            while lines and not lines[-1]:
                lines.pop()
            if lines:
                low = min(n for n, _ in filter(None, lines))
                blocks.append(("poem", [x and "\u2003\u2003" * (x[0] - low >= 2) + x[1] for x in lines]))
            lines.clear()
        for k, x in enumerate(raw):
            if re.fullmatch(r"\s*(\d+\.\s+)?[A-Z][A-Z ,'\u2019;:.!?-]{3,}", x) and not (raw[k - 1].strip() if k else "") and \
                    not (raw[k + 1].strip() if k + 1 < len(raw) else ""):
                flush()  # a SHOUTED title line between blank lines: the next poem
                blocks.append(("h", 3, re.sub(r"^\d+\.\s+", "", x.strip()).rstrip(".")))
            elif x.strip():
                lines.append((len(x) - len(x.lstrip(" \xa0")), clean(md_escape(x.strip()))))
            elif lines and lines[-1]:
                lines.append("")
        flush()
        return
    if tag == "img":
        alt = el.get("alt", "")
        if len(alt) == 1 and alt.isalpha():
            state["cap"] = alt  # a drop-cap picture: its letter goes on the next paragraph
        else:
            blocks.append(("img", posixpath.normpath(posixpath.join(base, el.get("src", ""))), alt))
        return
    if tag == "table":
        if all(a.get("href", "").startswith("#") or "pginternal" in a.get("class", "") for a in el.iter(X + "a")) and \
                list(el.iter(X + "a")) and not list(el.iter(X + "img")):
            return  # a contents table
        cells = [td for td in el.iter() if td.tag.replace(X, "") in ("td", "th")]
        if any(c.tag.replace(X, "") in ("p", "div") for td in cells for c in td):  # a layout table: text and pictures
            for td in cells:
                walk(td, base, blocks, state)
            return
        for row in el.iter(X + "tr"):
            cells = [clean(inline(td, None)) for td in row if td.tag.replace(X, "") in ("td", "th")]
            if any(cells):
                blocks.append(("p", " · ".join(c for c in cells if c)))
        for i in el.iter(X + "img"):
            blocks.append(("img", posixpath.normpath(posixpath.join(base, i.get("src", ""))), i.get("alt", "")))
        return
    poem = any(k in cls for k in ("poem", "stanza", "verse")) and tag != "span"
    if poem and any(c.tag.replace(X, "") == "div" and "title" in c.get("class", "") for c in el):
        return titled_poems(el, base, blocks)  # rhymes with a title div, the lines as bare text (nesting may be broken)
    if poem and not any(c.tag.replace(X, "") in ("div", "p") and any(k in c.get("class", "") for k in ("stanza", "poem"))
                        for c in el):
        lines = []
        for c in [el] if not has_block(el) else [c for c in el.iter() if c.tag.replace(X, "") in ("p", "div", "span")
                                                  and not has_block(c) and "pageno" not in c.get("class", "")
                                                  and (c.tag.replace(X, "") != "span" or "i" in c.get("class", "")[:1])]:
            t = inline(c, None)
            for x in t.split("  \n"):  # an empty line between <br>s is a stanza break, kept as ""
                if clean(x) or lines and lines[-1]:
                    indent = clean(x) and len(re.match(r"[\r\n]*([ \xa0]*)", x)[1]) >= 2  # indented verse lines stay indented
                    lines.append("\u2003\u2003" * bool(indent) + clean(x))
        while lines and not lines[-1]:
            lines.pop()
        if lines:
            blocks.append(("poem", lines))
        return
    if not has_block(el) and tag not in ("body", "section"):
        t = clean(inline(el, None))
        if t:
            links = [a for a in el.iter(X + "a") if a.get("href", "").startswith("#")]
            if links and len("".join("".join(a.itertext()) for a in links)) > 0.8 * len(re.sub(r"\W", "", t)):
                return  # a contents line
            if state.get("cap") and t.startswith(state["cap"]) and t[1:2].islower():
                state["cap"] = None  # the letter is in the text as well as in the picture
            if state.get("cap"):
                t, state["cap"] = state["cap"] + t.lstrip("*").replace("**", "", 1) if t.startswith("**") else state["cap"] + t, None
            blocks.append(("p", t))
        return
    if (el.text or "").strip():
        t = clean(md_escape(el.text))
        if t:
            blocks.append(("p", t))
    for c in el:
        walk(c, base, blocks, state)
        if (c.tail or "").strip() and tag not in ("body",):
            blocks.append(("p", clean(md_escape(c.tail))))


def epub_blocks(path):
    z = zipfile.ZipFile(path)
    root = re.search(r'full-path="([^"]+)"', z.read("META-INF/container.xml").decode()).group(1)
    opf = z.read(root).decode("utf-8")
    items = dict(re.findall(r'<item\b[^>]*\bid="([^"]+)"[^>]*\bhref="([^"]+)"', opf))
    items.update({i: h for h, i in re.findall(r'<item\b[^>]*\bhref="([^"]+)"[^>]*\bid="([^"]+)"', opf)})
    base = posixpath.dirname(root)
    blocks, state = [], {}
    for idref in re.findall(r'<itemref\b[^>]*\bidref="([^"]+)"', opf):
        href = items.get(idref, "")
        if not href or "wrap" in href or posixpath.basename(href).startswith("toc"):
            continue
        name = posixpath.normpath(posixpath.join(base, href))
        try:
            tree = ET.fromstring(z.read(name))
        except ET.ParseError:
            continue
        body = tree.find(X + "body")
        if body is not None:
            walk(body, posixpath.dirname(name), blocks, state)
    return z, blocks


# ---- picking the section ---------------------------------------------------------------------------------------------

def plain(b):
    return norm(" ".join(b[2] if b[0] == "h" else b[1] if b[0] == "p" else " ".join(b[1]) if b[0] == "poem" else "" for b in [b]))


def section(blocks, title, find, whole):
    """(start, end, how): the slice of blocks for this story."""
    heads = [(i, b[1], norm(b[2])) for i, b in enumerate(blocks) if b[0] == "h"]
    t, f = norm(title), norm(find) if find else ""
    cands = [h for h in heads if h[2] == t or h[2].endswith(" " + t) or h[2].startswith(t + " ")] or \
            [h for h in heads if t and (t in h[2] and len(h[2]) < len(t) + 25)]
    if cands and not (whole and cands[0][0] == heads[0][0]):
        good = [(i, l) for i, l, _ in cands if not f or f in text_of(blocks, i, end_of(blocks, i, l))]
        pick = max(good or [(i, l) for i, l, _ in cands], key=lambda c: end_of(blocks, c[0], c[1]) - c[0])
        return pick[0] + 1, end_of(blocks, *pick), "heading"
    if whole:
        return 0, len(blocks), "whole"
    if f:  # the find text, then back to its heading
        for i, b in enumerate(blocks):
            if f in plain(b):
                h = next(((j, blocks[j][1]) for j in range(i, -1, -1) if blocks[j][0] == "h"), None)
                if h:
                    return h[0] + 1, end_of(blocks, *h), "find"
    return None


def end_of(blocks, i, lvl):
    """Where the section under heading i (level lvl) ends: the next heading as big, unless it is a chapter mark
    (and the section's own heading is not one)."""
    own = blocks[i][0] == "h" and bool(CHAPTER.match(norm(blocks[i][2]) or "x"))
    for j, b in enumerate(blocks[i + 1:], i + 1):
        if b[0] == "h" and b[1] <= lvl and (own or FRONT.match(norm(b[2])) or not CHAPTER.match(norm(b[2]) or "x")):
            return j
    return len(blocks)


def text_of(blocks, a, z):
    return " ".join(plain(b) for b in blocks[a:z])


def find_block(blocks, phrase, after=0):
    if re.fullmatch(r"@\d+", phrase.strip()):  # a block number, as --outline prints it
        return int(phrase.strip()[1:])
    p = norm(phrase)
    return next((i for i in range(after, len(blocks)) if p and p in plain(blocks[i])), None)


def apply_cut(blocks, spec):
    """A cuts.csv `pick`: pieces split by ' | '. '#Heading' is that heading's section (add '@ phrase' to pick the
    one holding the phrase); 'start >> end' is a run of blocks (end '$' = to the end of the book). '[Label] ' in
    front of a piece puts a ## Label heading over it; in a set, a '#Heading' piece keeps its own heading."""
    pieces, out = [p.strip() for p in spec.split(" | ")], []
    for piece in pieces:
        label = None
        m = re.match(r"\[([^\]]+)\]\s*(.*)", piece)
        if m:
            label, piece = m.groups()
        if piece.startswith("#"):
            head, _, at = piece[1:].partition(" @ ")
            h = norm(head)
            cands = [i for i, b in enumerate(blocks) if b[0] == "h" and (norm(b[2]) == h or norm(b[2]).startswith(h + " "))] or \
                    [i for i, b in enumerate(blocks) if b[0] == "h" and h in norm(b[2])]
            if at:
                cands = [i for i in cands if norm(at) in text_of(blocks, i, end_of(blocks, i, blocks[i][1]))]
            if not cands:
                raise LookupError(f"heading not found: {head}")
            i = max(cands, key=lambda c: end_of(blocks, c, blocks[c][1]) - c)
            part = blocks[i + 1:end_of(blocks, i, blocks[i][1])]
            while len(pieces) > 1 and part and part[-1][0] == "img":  # the next piece's picture
                part.pop()
            if len(pieces) > 1 or label:
                part = [("h", 1, label or re.sub(r"^[IVXLC]+\.\s+", "", blocks[i][2]))] + [("h", max(2, b[1]), b[2]) if b[0] == "h" else b for b in part]
        else:
            a, _, z = piece.partition(" >> ")
            i = find_block(blocks, a)
            if i is None:
                raise LookupError(f"start not found: {a}")
            j = len(blocks) - 1 if z.strip() == "$" else find_block(blocks, z, i) if z else i
            if j is None:
                raise LookupError(f"end not found: {z}")
            part = blocks[i:j + 1]
            if label:
                part = [("h", 1, label)] + [("h", max(2, b[1]), b[2]) if b[0] == "h" else b for b in part]
        out += part
    return out


IMPRINT = re.compile(r"publish|printed|copyright|all rights|& co\b|\bco\.|limited|\bltd\b|illustrat(ed|ions) by|^by\b|"
                     r"press$|^london|^new york|^boston|^philadelphia|^chicago|^\d{4}$|edition|dedicat|^to\b|^for\b", re.I)
FIRST = re.compile(r"^(chapter (i|1|one)|i|1|part (i|1|one|the first)|book (i|1|one|the first)|stave (i|one)|"
                   r"canto (i|1)|act (i|1)|scene (i|1)|book the first)( [a-z].*)?$")
FURNITURE = re.compile(r"transcriber|typographical errors|project gutenberg|this e-?book|e-?text was produced|"
                       r"plain text version|craphound\.com|^enlarge|^\[?contents\]?$|^page$|^\d{1,4}$|"
                       r"^\[(illustration|pg \d+)[^\]]*\]$|was produced from|copyright on this publication|"
                       r"^the end of the project|full-size|^\W*illustration\W*$|^(left|right) side image", re.I)
TAIL = re.compile(r"^(glossary|index|footnotes|notes|endnotes|vocabulary|pronouncing (index|vocabulary).*|appendix.*|"
                  r"advertisements?|the full project gutenberg.*|transcriber.*|list of .*|books by .*|other books.*|"
                  r"by the same author.*|.*catalogue.*|colophon|a note on the text|pronunciation of .*|notes (to|on) .*)$")


LEAD_JUNK = re.compile(r"copyright|all rights reserved|first published|\bimpression\b|illustrat(ed|ions) by|fulcrum edition|"
                       r"hyphenation|project gutenberg|\betexts?\b|produced by|^\W*by\W*$|printed in|\bendowed\b|^established by|^\W*contents\W*$|^\W*contents:?\s*\n", re.I)
TAIL_JUNK = re.compile(r"printed (by|in)|\bpress\b|\bltd\b|\blimited\b|\bprice\b|\bnet\W*$|\b(12|16|24)mo\b|\b8vo\b|catalog|"
                       r"transcriber|hyphenation|links have been added|obvious print(er|ing) errors|misspelled words|illustrations have been relocated|by (kind )?permission|reproduced as printed|"
                       r"^\W*\$\d|^\W*(the end|fin|finis)\W*$|\blondon\W*$|\bimpression of the first edition", re.I)
AD = re.compile(r"\b(12|16|24)mo\b|\b8vo\b|\bprice\b|\$\d|\bcloth\b|\bnet\W*$|book ?stores?|catalog|postpaid|"
                r"per volume|uniform with|outstanding science fiction|\bpublishers?\b", re.I)
AD_SURE = re.compile(r"\b(12|16|24)mo\b|\b8vo\b|\bcloth\b|\bnet\W*$|book ?stores?|catalog|postpaid|per volume", re.I)
END_MARK = re.compile(r"^\W*(the end|finis)\W*$", re.I)


def trim_ends(out):
    """Book furniture at the ends of a story: copyright and edition lines in front; printers, ads and price lists
    behind (and anything after a closing THE END)."""
    def short(x):
        return not x.startswith("![") and len(x.split()) < 60
    k = next((i for i in range(len(out) - 1, int(len(out) * 0.85) - 1, -1) if END_MARK.match(out[i])), None)
    if k is not None and k >= 3:
        out = out[:k]
    ads = [i for i in range(int(len(out) * 0.8), len(out))
           if short(out[i]) and AD.search(out[i]) and not re.search(r"dedicated to", out[i], re.I)]
    while len(ads) > 1 and max(y - x for x, y in zip(ads, ads[1:])) > 6:
        ads.pop(0)  # an ad run is one close run of hits that goes to the end
    if len(ads) >= 2 and ads[-1] >= len(out) - 10 and any(AD_SURE.search(out[i]) for i in ads):  # the publisher's list
        k = ads[0]
        while k > 0 and (out[k - 1].startswith("#") or short(out[k - 1]) and len(out[k - 1].split()) <= 12):
            k -= 1
        out = out[:k]
    k = next((i for i in range(int(len(out) * 0.8), len(out)) if re.match(r"\W*uniform with (this|the) (volume|series)", out[i], re.I)), None)
    if k:
        out = out[:k]  # the series list at the back of a picture book
    if len(out) > 2 and out[-2] == "---" and re.search(r"\be-?book\b|print(ing|er) errors|transcriber", out[-1], re.I):
        out = out[:-2]  # a long transcriber's note after the last rule
    while out and (out[-1].startswith("![") and len(out) > 1 and short(out[-2]) and TAIL_JUNK.search(out[-2]) or
                   short(out[-1]) and TAIL_JUNK.search(out[-1]) or out[-1] == "---"):
        out.pop(-2 if out[-1].startswith("![") else -1)
    lead = [i for i, x in enumerate(out[:8]) if not x.startswith("![") and x != "---"][:4]
    for i in reversed(lead):
        if short(out[i]) and LEAD_JUNK.search(out[i]) and not re.match(r"#+ (chapter|part|book)\b", out[i], re.I):
            if re.match(r"\W*contents\W*$", out[i], re.I) and i + 1 < len(out) and short(out[i + 1]):
                out.pop(i + 1)  # and the contents list under it
            out.pop(i)
    while out and out[0] == "---":
        out.pop(0)
    return out


def text(b):
    return b[2] if b[0] == "h" else b[1] if b[0] == "p" else " ".join(b[1]) if b[0] == "poem" else ""


def tidy(part):
    """Drop Gutenberg furniture wherever it is: contents runs (short lines ending in page numbers), page numbers,
    transcriber notes, [Contents] links."""
    toc = [b[0] == "p" and len(text(b).split()) < 16 and bool(re.search(r"[\s·.]\d{1,3}$", text(b))) for b in part]
    out = []
    for i, b in enumerate(part):
        if toc[i] and sum(toc[max(0, i - 2):i + 3]) >= 3:
            continue
        if b[0] in ("p", "h") and len(text(b).split()) < 40 and FURNITURE.search(re.sub(r"[\\*]", "", text(b)).strip()):
            continue
        if b[0] == "p":
            b = ("p", re.sub(r"\s*\\?\[\d+\\?\]$", "", re.sub(r"\s*\\?\[(Contents|Pg \d+)\\?\]", "", b[1])))
        out.append(b)
    return out


def trim(part, title):
    """A whole book: start at chapter one (or past the title page and imprint), stop before end matter."""
    t = norm(title)
    words = lambda b: len(plain(b).split())
    first = next((i for i, b in enumerate(part[:len(part) // 3 + 30]) if b[0] == "h" and FIRST.match(norm(b[2]))), None)
    if first is not None:
        part = part[first:]
    else:
        cut = None
        for i, b in enumerate(part[:60]):
            if b[0] == "h" and FRONT.match(norm(b[2])):
                cut = next((j for j in range(i + 1, len(part)) if part[j][0] == "h" and part[j][1] <= b[1]), i + 1) - 1
                continue
            if cut is not None and i <= cut:
                continue
            if b[0] in ("p", "h") and words(b) < 25 and (IMPRINT.search(text(b)) or norm(text(b)) == t):
                cut = i
            if b[0] == "p" and words(b) > 50:
                break
        if cut is not None:
            part = part[cut + 1:]
    while part and (part[0][0] == "hr" or part[0][0] == "h" and (norm(part[0][2]) in (t, "") or
                                                                  norm(part[0][2]).startswith("by "))):
        part = part[1:]
    tail = next((i for i, b in enumerate(part) if b[0] == "h" and i > len(part) // 2 and TAIL.match(norm(b[2]))), None)
    if tail is not None:
        part = part[:tail]
    ends = [i for i, b in enumerate(part) if b[0] in ("p", "h") and re.fullmatch(r"\**the end\.?\**", text(b).strip(), re.I)]
    if ends and len(part) - ends[-1] < 0.1 * len(part) + 40:
        part = part[:ends[-1] + 1]
    return part


# ---- writing -------------------------------------------------------------------------------------------------------

def save_art(data, dest):
    im = Image.open(io.BytesIO(data))
    if im.width < 60 and im.height < 60:
        return False
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")
    if im.width > ART_W:
        im = im.resize((ART_W, round(im.height * ART_W / im.width)), Image.LANCZOS)
    im.save(dest, "JPEG", quality=72, optimize=True, progressive=True)
    return True


FIXES = {  # id -> [(old, new)]: typos in the source text itself, applied after every other step
    "poe-helen": [("How statue-like I me thee stand", "How statue-like I see thee stand")],
    "poe-marie-roget": [('THE MYSTERY OF MARIE ROGET.\n\nA SEQUEL TO "THE MURDERS IN THE RUE MORGUE."\n\n', ""),
                        ("lauft. Selten fallen sie zusammen. Menschen und zufalle modifieiren gewohulich",
                         "läuft. Selten fallen sie zusammen. Menschen und Zufälle modificiren gewöhnlich")],
    "poe-composition": [('" Barnaby Rudge,"', '"Barnaby Rudge,"')],
}


def fix(sid, text):
    """Editors' brackets from the 1903 Raven edition ({*1} footnote marks whose notes are not kept, {image}, {...ed.}),
    a footnote or editor's note standing alone, then the row's FIXES."""
    text = re.sub(r"\n\n(\\?\{\\?\*\d+\}|\\?\{This poem|\(Note: No figures)[^\n]*", "", text)
    text = re.sub(r"\s*\\?\{\\?\*\d+\}", "", text)
    text = re.sub(r"\s*\\?\{(image|[^{}\n|]*—\s*ed\.?)\}", "", text, flags=re.I)
    for a, b in FIXES.get(sid, []):
        text = text.replace(a, b)
    return text


def write_story(sid, blocks, z, meta):
    d = LIB / sid
    old = d / "story.json"
    if old.exists() and json.loads(old.read_text(encoding="utf-8")).get("hand"):
        return
    if (d / "art").is_dir():
        for f in (d / "art").iterdir():
            f.unlink()
    d.mkdir(parents=True, exist_ok=True)
    top = min((b[1] for b in blocks if b[0] == "h"), default=2)
    out, n, seen = [], 0, set()
    numbered = sum(b[0] == "h" and bool(re.match(r"(II|III|IV|V|VI) [A-Z]", b[2])) for b in blocks) >= 2
    for i, b in enumerate(blocks):
        if b[0] == "h":
            if FRONT.match(norm(b[2])):
                continue
            h = re.sub(r"(\s*\[\d+\])+$", "", b[2].replace("  \n", " "))  # footnote marks off a heading
            if numbered:
                h = re.sub(r"^([IVXLC]+) (?=[A-Z“\"'])", r"\1. ", h)  # "I The Old Sea-dog" reads "I. The Old Sea-dog"
            near = [blocks[k][0] for k in (i - 1, i + 1) if 0 <= k < len(blocks)]
            if "img" in near and b[1] > top and not CHAPTER.match(norm(h) or "x"):
                out.append(f"*{h}*")  # a picture caption set as a heading
                continue
            if h.isupper() and len(h) > 3:  # SHOUTED HEADINGS in title case, roman numerals kept
                h = re.sub(r"[A-Za-z][A-Za-z'\u2019]*", lambda m: m[0] if ROMAN.fullmatch(m[0]) and m[0] != "I" or
                           m[0] == "I" and m.start() == 0 else m[0].lower() if m[0].lower() in SMALL and m.start() and
                           not re.search(r"[:.]\s*$", h[:m.start()]) else m[0].capitalize(), h)
            out.append("#" * min(4, 2 + b[1] - top) + " " + h)
        elif b[0] == "p":
            m = re.fullmatch(r"\*\*((chapter|part) [\w.]+)\*\*\s*(.*)", b[1].strip(), re.I | re.S)
            out += [f"## {m[1]}"] + [m[3]] * bool(m[3]) if m else [b[1]]  # a chapter title set as a bold paragraph
        elif b[0] == "poem":
            out += ["  \n".join(st.split("\n")) for st in "\n".join(b[1]).split("\n\n")]
        elif b[0] == "hr":
            if out and out[-1] != "---":
                out.append("---")
        elif b[0] == "img" and z is not None and b[1] not in seen:
            seen.add(b[1])
            try:
                data = z.read(b[1])
            except KeyError:
                continue
            (d / "art").mkdir(exist_ok=True)
            name = f"art/{n + 1:02d}.jpg"
            if save_art(data, d / name):
                n += 1
                alt = re.sub(r"[\[\]\n]", " ", b[2]).strip()
                alt = "Illustration" if not alt or alt.isdigit() else alt
                out.append(f"![{alt}]({name})")
    while out and out[0] == "---":
        out.pop(0)
    while out and (out[-1] == "---" or out[-1].startswith("#") or
                   re.match(r"\d{1,3} \S", out[-1]) and len(out[-1].split()) < 40 or
                   len(out) > 3 and len(out[-1].split()) <= 5 and re.fullmatch(r"[^a-z]*[A-Z]{3}[^a-z]*", out[-1]) or
                   re.fullmatch(r"!\[[^a-z\]]*[A-Z]{3}[^a-z\]]*\]\(.*\)", out[-1])):  # the next piece's title or title picture  # nor the next chapter's heading, footnotes
        out.pop()
    out = [x for i, x in enumerate(out)  # a bare chapter number left over before the next piece's heading
           if not (re.fullmatch(r"#+ [IVXLC\d]+\.?", x) and i + 1 < len(out) and out[i + 1].startswith("#"))]
    out = trim_ends(out)
    text = fix(sid, "\n\n".join(out) + "\n")
    (d / "text.md").write_text(text, encoding="utf-8", newline="\n")
    if (d / "art").is_dir() and not any((d / "art").iterdir()):
        (d / "art").rmdir()
    prev = json.loads(old.read_text(encoding="utf-8")) if old.exists() else {}
    prev.update(meta)
    old.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return text


def rows():
    out = []
    for f, coll in (("stories-pd", "stories"), ("mythology", "mythology"), ("sacred-texts", "sacred"), ("speeches", "speeches")):
        for r in csv.DictReader(open(DATA / f"{f}.csv", encoding="utf-8")):
            if r["title"] and r["decision"] != "reserve":
                out.append(dict(r, collection=coll))
    return out


def txt_poem(src, first):
    """A cut 'txt:first line': one poem from the book's plain-text file, where the epub lost its stanzas. It runs
    from that line to the first gap of two or more blank lines; one blank line is a stanza break."""
    n = src["pg"].split()[0]
    lines = (SRC / "gutenberg" / n / f"pg{n}.txt").read_text(encoding="utf-8-sig").splitlines()
    i = next(i for i, l in enumerate(lines) if norm(first) in norm(l))
    out = []
    for l in lines[i:]:
        if not l.strip() and out and not out[-1]:
            break
        out.append((len(l) - len(l.lstrip()), clean(md_escape(l.strip()))) if l.strip() else "")
    while out and not out[-1]:
        out.pop()
    low = min(n for n, _ in filter(None, out))
    return [("poem", [x and "\u2003\u2003" * (x[0] - low >= 2) + x[1] for x in out])]


def unshape(part, src):
    """Picture-book text set around the pictures, a word or two to a line, comes back as paragraphs (pictures that
    fell mid-sentence move to after it), and a drop cap set as a letter picture comes back from the plain text."""
    n = src["pg"].split()[0]
    p = SRC / "gutenberg" / n / f"pg{n}.txt"
    flat = " ".join(p.read_text(encoding="utf-8-sig").split()) if p.exists() else ""
    out, held = [], []
    for b in part:
        if b[0] == "img" and out and out[-1][0] == "p" and not re.search(r"[.!?:\"”]\s*$", out[-1][1]):
            held.append(b)  # a picture in the middle of a sentence
            continue
        if b[0] == "p" and out and out[-1][0] == "p" and not re.search(r"[.!?:\"”]\s*$", out[-1][1]) and \
                (b[1][:1].islower() or len(out[-1][1].split()) <= 3 or len(b[1].split()) <= 2 and out[-1][1][-1:].islower()):
            out[-1] = ("p", re.sub(r" *\n", " ", out[-1][1] + " " + b[1].strip()))
            continue
        if b[0] == "p" and flat and (not out or out[-1][0] == "img" or held):
            words = b[1].split()[:4]
            if words and b[1][:1].islower():
                m = re.search(r"(?<![A-Za-z])([A-Z])" + r"\s+".join(map(re.escape, words)), flat)
            elif words:
                m = re.search(r"(?<!\S)(A|I) " + r"\s+".join(map(re.escape, words)), flat)
            if words and m:
                b = ("p", m[1] + ("" if b[1][:1].islower() else " ") + b[1])
                if not held and out and out[-1][0] == "img":
                    out.pop()  # the letter picture itself
        out += held
        held = []
        out.append(b)
    return out + held


def gutenberg(r, src, uses, cache):
    if r["source"] not in cache:
        cache.clear()  # one book in memory at a time (rows are sorted by source)
        books = [epub_blocks(p) for n in src["pg"].split() if (p := SRC / "gutenberg" / n / f"pg{n}-images-3.epub").exists()]
        cache[r["source"]] = (Zips([z for z, _ in books]), [b for _, bl in books for b in bl])
    z, blocks = cache[r["source"]]
    if not blocks:
        return None, "no epub"
    if r["source"] == "pickthall-quran":
        return (pickthall(blocks), z), "pickthall only"
    if CUTS.get(r["id"], "").startswith("txt:"):
        return (txt_poem(src, CUTS[r["id"]][4:]), z), "cut from the plain text"
    if r["id"] in CUTS:
        try:
            part, how = apply_cut(blocks, CUTS[r["id"]]), "cut"
        except LookupError as e:
            return None, f"cut failed: {e}"
    else:
        whole = uses[r["source"]] == 1 or r["kind"] in WHOLE and norm(r["title"]) in norm(src["title"])
        got = section(blocks, r["title"], r["find"], whole)
        if not got:
            return None, "not placed"
        a, e, how = got
        part = trim(unshape(tidy(blocks[a:e]), src), r["title"]) if how == "whole" else blocks[a:e]
    part = unshape(tidy(part), src)
    if r["source"].startswith("ovid-riley"):  # Riley's footnote numbers and line references sit in the text
        part = [(b[0], re.sub(r"(?<=[a-z,;:.!?’”*])\d{1,3}(?=[\s,;:.]|$)", "",
                              re.sub(r"\s*\b[IVX]+\. \d+-\d+\s+", " ", b[1]))) if b[0] == "p" else b for b in part]
    while part and (part[0][0] == "hr" or part[0][0] in ("h", "p") and len(text(part[0]).split()) < 14 and
                    re.match(r"(by|edited by|translated by)\b|.*edition\W*$", text(part[0]).strip(), re.I)):
        part = part[1:]  # a byline or edition line left over the start
    while part and part[-1][0] in ("p", "h", "hr") and len(text(part[-1]).split()) < 14 and \
            (part[-1][0] == "hr" or IMPRINT.search(text(part[-1])) and not re.search(r"the end", text(part[-1]), re.I)):
        part = part[:-1]  # a printer's line at the very end
    if r["id"] not in CUTS and not part:
        return None, "empty"
    if r["find"] and norm(r["find"]) not in norm(r["title"]) and norm(r["find"]) not in " ".join(plain(b) for b in part):
        how += " (find text missing)"
    return (part, z), how


def pickthall(blocks):
    """The Gutenberg Qur'an sets three translations verse by verse (Y:, P:, S:). Keep Pickthall's: a heading per
    surah, its verses as numbered runs of ten."""
    out, verses, num = [], [], None
    def flush():
        for i in range(0, len(verses), 10):
            out.append(("p", " ".join(verses[i:i + 10])))
        verses.clear()
    for i, b in enumerate(blocks):
        if b[0] == "h" and re.match(r"Chapter (\d+):", b[2]):
            flush()
            name = text(blocks[i + 1]).split("  ")[0].strip()  # "AL-FATIHA (THE OPENING)    Total Verses: 7"
            out.append(("h", 1, f"{b[2].split()[1].rstrip(':')}. {name.title()}"))
        elif b[0] == "p":
            m = re.match(r"\d{3}\.(\d{3}) Y:", b[1])
            if m:
                num = int(m[1])
            elif b[1].startswith("P: ") and num:
                verses.append(f"<sup>{num}</sup>{b[1][3:].strip()}".replace("  \n", " "))
    flush()
    return out


class Zips:
    """Several EPUBs read as one (a source split over more than one Gutenberg book)."""
    def __init__(self, zips):
        self.zips = zips

    def read(self, name):
        for z in self.zips:
            if name in z.namelist():
                return z.read(name)
        raise KeyError(name)


def storyweaver(r):
    sw = SRC / "storyweaver"
    book = json.loads((sw / f"{r['sw_id']}.json").read_text(encoding="utf-8"))
    d = LIB / r["id"]
    old = d / "story.json"
    if old.exists() and json.loads(old.read_text(encoding="utf-8")).get("hand"):
        return "hand"
    (d / "art").mkdir(parents=True, exist_ok=True)
    out = []
    for i, p in enumerate(book["pages"]):
        img = next(iter(sorted((sw / r["sw_id"]).glob(f"p{i + 1:02d}.*"))), None)
        bits = []
        if img and save_art(img.read_bytes(), d / f"art/{i + 1:02d}.jpg"):
            bits.append(f"![Picture for page {i + 1}](art/{i + 1:02d}.jpg)")
        text = (p.get("text") or "").replace("�", "").strip()
        if text:
            bits.append("  \n".join(clean(md_escape(l)) for l in text.splitlines() if l.strip()))
        if bits:
            out.append("\n\n".join(bits))
    (d / "text.md").write_text(fix(r["id"], "\n\n---\n\n".join(out) + "\n"), encoding="utf-8", newline="\n")
    prev = json.loads(old.read_text(encoding="utf-8")) if old.exists() else {}
    prev.setdefault("summary", " ".join(book.get("description", "").split()))
    old.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return "storyweaver"


PAGES = {  # which Wikisource pages a row takes (default: the first); a trailing "/" takes every subpage under it
    "sandburg-fog": "Chicago Poems/Fog", "sandburg-chicago-poem": "Chicago Poems/Chicago",
    "johnson-creation": "God's Trombones/The Creation", "larsen-passing": "Passing (Larsen)/Part",
    "kojiki": "Kojiki (Chamberlain, 1882)/Section",
}
WS_ID = re.compile(r"^(?!.{0,80} by )(\S+ ){0,4}\d{3,8} ")  # the page id line that ends Wikisource's header
WS_END = re.compile(r"^(this work is (in the public domain|a translation)|this work was published|public domain|"
                    r"authority control|the longest-living author|layout \d)", re.I)
DROP_CAP = re.compile(r"^(“?[A-Z]) (?=[b-z]\b|[A-Z]+\b)")  # "I t was", "O FF there": a drop cap set apart


def ws_tidy(t):
    t = re.sub(r"\s*\[\s*\d+\s*\]", "", t)  # footnote marks
    t = re.sub(r" ([,.;:!?)\]’”»])", r"\1", t)
    return re.sub(r"([(\[“]) ", r"\1", t).strip()


def ws_pages(path, author=""):
    """{page title: body lines}: the article text, without the Wikisource header, footnotes and license box."""
    parts = re.split(r"^== (.+) ==$", path.read_text(encoding="utf-8"), flags=re.M)
    out = {}
    for title, body in zip(parts[1::2], parts[2::2]):
        lines = body.split("\n")
        start = max((i for i, l in enumerate(lines[:20]) if WS_ID.match(l) and len(l.split()) < 30 and
                     not re.search(r"[.!?:;,”\"’)]\s*$", l)), default=None)
        if start is None:
            start = 0
        elif len(lines[start].split()) > 25:  # the id line runs straight into the text
            lines[start] = lines[start].split(author, 1)[-1] if author in lines[start] else lines[start]
        else:
            start += 1
        keep = []
        for l in lines[start:]:
            if WS_END.match(l.strip()):
                break
            if not l.startswith("↑"):
                keep.append(l)
        out[title] = keep
    return out


def wikisource(r, src):
    pages = ws_pages(SRC / "other" / r["source"] / "text.txt", src["author"])
    want = PAGES.get(r["id"])
    if not want:
        names = [next(iter(pages))]
    elif want in pages:
        names = [want]
    else:  # every subpage, in number order
        names = sorted((p for p in pages if p.startswith(want)),
                       key=lambda p: [int(n) if n.isdigit() else n for n in re.split(r"(\d+)", p)])
    poem = r["kind"] == "poem"
    blocks = []
    for name in names:
        lines = pages[name]
        while lines and not lines[0].replace("\u200b", "").strip():
            lines = lines[1:]
        if r["id"] == "larsen-passing":
            if name.count("/") == 1:  # a Part page: "part one", then its name
                blocks.append(("h", 1, f"Part {name[-1]}: {lines[1].strip()}"))
                continue
            blocks.append(("h", 2, f"Chapter {name[-1]}"))
            lines = lines[1:]  # the chapter's number word
        if r["id"] == "kojiki":
            m = next((re.match(r"\[ ?Sect\. ([IVXLC]+)\.\s*[—-]\s*(.*?)\.? ?\]", l) for l in lines[:4] if "Sect." in l), None)
            blocks.append(("h", 1, f"{m[1]}. {m[2]}" if m else name.rsplit("/", 1)[1]))
            lines = [l for l in lines if "Sect." not in l and l.strip() != "RECORDS OF ANCIENT MATTERS."]
        # the poem's own title (and a book's section name) in capitals at the top
        while lines and (lines[0].replace("\u200b", "").strip().isupper() and len(lines[0].split()) < 6 or
                         not lines[0].replace("\u200b", "").strip()):
            lines = lines[1:]
        while lines and re.match(r"(by|from) [A-Z’'\w ]+$", lines[0].strip(), re.I) and len(lines[0].split()) < 6:
            lines = lines[1:]  # byline, "From Collier's"
        if lines and DROP_CAP.match(lines[0]):
            lines[0] = DROP_CAP.sub(r"\1", lines[0])
            if re.match(r"[^“]*”", lines[0]):  # the opening quote went with the drop cap
                lines[0] = "“" + lines[0]
        verse = []
        for l in lines:
            s = ws_tidy(l.replace("\u200b", ""))
            if not s:
                if poem and verse and verse[-1]:
                    verse.append("")
                continue
            if re.fullmatch(r"(\* ?)+\*", s):
                blocks.append(("hr",))
                continue
            if poem:
                verse.append(("\u2003\u2003" if l.startswith("\u200b ") else "") + md_escape(s))
            else:
                if l.startswith("\u200b ") and blocks and blocks[-1][0] == "p" and not re.search(r"[.!?”’:;)]$", blocks[-1][1]):
                    blocks[-1] = ("p", blocks[-1][1] + " " + md_escape(s))  # a paragraph split over a printed page
                else:
                    blocks.append(("p", md_escape(s)))
        if verse:
            blocks.append(("poem", verse))
    return blocks if any(b[0] in ("p", "poem") for b in blocks) else None


def sacred(r, src):
    """Clean transcriptions from archive.sacred-texts.com: the text between the site's credit line and the footnotes,
    without page numbers, footnote marks, line numbers, or the translator's commentary and notes (set in small type)."""
    blocks = []
    for f in sorted((SRC / "other" / r["source"]).glob("st-*.htm")):
        h = f.read_bytes().decode("utf-8", "replace")
        start = re.search(r"at sacred-texts\.com</font></p>\s*<hr\s*/?>", h, flags=re.I) or \
            re.search(r">Next</a>.*?<hr\s*/?>", h, flags=re.I | re.S)  # past the site's credit line, or its top links
        h = h[start.end():] if start else h
        h = re.split(r"<h3[^>]*>\s*Footnotes|<nav\b|<hr width|<center>\s*<a href=\"\.\./", h, maxsplit=1, flags=re.I)[0]
        h = re.sub(r"<a name=\"?page_\w+\"?>.*?</a>|<a name=\"?fr_\d+\"?></a>|<a href=\"#fn_\d+\">.*?</a>|"
                   r"<span class=\"margnote\">.*?</span>|\{(footnote )?p\. \d+\}|\[\d+\]", "", h, flags=re.S | re.I)
        h = re.sub(r"<font size=\"?(-1|2)\"?>.*?</font>", " ", h, flags=re.S | re.I)  # after the page numbers' own fonts
        parts = re.split(r"<(h[1-6]|p)\b[^>]*>", h, flags=re.I)
        page = []
        for tag, chunk in zip(parts[1::2], parts[2::2]):
            inner = re.split(r"</(?:p|h[1-6])>", chunk, maxsplit=1, flags=re.I)[0]
            inner = re.sub(r"</?(i|em)>", "\x01", inner, flags=re.I)
            inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.I)
            t = html.unescape(re.sub(r"<[^>]+>", "", inner)).replace("\x01\x01", "")
            t = re.sub(r"(?<=\w)\x01(\w+)\x01|\x01(\w+)\x01(?=\w)", r"\1\2", t)  # Zarathu<i>s</i>tra: a transliteration mark
            t = re.sub(r"(?<=\w)[ \xa0]+([,;:.])(?=\s|$)(?! \.)", r"\1", t)  # the gap a dropped footnote mark leaves
            lines = [("\u2003\u2003" if re.match(r"[ \xa0]{8,}", l) else "") + md_escape(" ".join(l.split())).replace("\x01", "*")
                     for l in t.split("\n")]
            lines = [l for l in lines if l.strip("\u2003 *")]
            if not lines:
                continue
            if tag.lower().startswith("h"):
                page.append(("h", int(tag[1]), " ".join(lines).rstrip(".").replace("*", "")))
            elif len(lines) > 1:
                page.append(("poem", lines))
            elif page and page[-1][0] == "p" and re.match(r"[a-z(]", lines[0]) and \
                    not re.search(r"[.!?:;)\]\"’”*]$", page[-1][1]):
                page[-1] = ("p", page[-1][1] + " " + lines[0])  # a paragraph split over a printed page
            else:
                page.append(("p", lines[0]))
        if sum(b[0] == "h" for b in page) > 1:  # the book's own title, repeated over every page
            page = [b for b in page if not (b[0] == "h" and b[1] == 1)]
        for b in page:  # "THE FIRST TABLET" over "OF THE TYRANNY OF GILGAMISH": one heading
            if b[0] == "h" and blocks and blocks[-1][0] == "h" and b[1] > blocks[-1][1]:
                blocks[-1] = ("h", blocks[-1][1], f"{blocks[-1][2]}: {b[2]}")
            else:
                blocks.append(b)
    while blocks and blocks[-1][0] == "p" and re.search(r"\b(SONS|PRINTED|PRESS)\b", blocks[-1][1]):
        blocks.pop()  # the printer's line
    return blocks if any(b[0] in ("p", "poem") for b in blocks) else None


def sefaria(r, src):
    """The JPS 1917 Tanakh: ## book, ### chapter, verse numbers as superscripts."""
    blocks, chap, verses = [], None, []
    def flush():
        if verses:
            blocks.append(("p", " ".join(verses)))
            verses.clear()
    for l in (SRC / "other" / r["source"] / "text.txt").read_text(encoding="utf-8").split("\n"):
        m = re.match(r"== (.+) ==$", l)
        if m:
            flush()
            blocks.append(("h", 1, m[1]))
            chap = None
            continue
        m = re.match(r"(\d+):(\d+) (.*)", l)
        if not m:
            continue
        if m[1] != chap:
            flush()
            chap = m[1]
            blocks.append(("h", 2, f"Chapter {chap}"))
        verses.append(f"<sup>{m[2]}</sup>{md_escape(m[3].strip())}")
    flush()
    return blocks


def outline(key, pattern=""):
    """--outline SOURCE [words]: the source's blocks (headings, or blocks holding the words) with their first words,
    for writing a cuts.csv pick."""
    src = {r["key"]: r for r in csv.DictReader(open(DATA / "sources.csv", encoding="utf-8"))}[key]
    blocks = [b for n in src["pg"].split() for b in epub_blocks(SRC / "gutenberg" / n / f"pg{n}-images-3.epub")[1]]
    p, span = norm(pattern), re.fullmatch(r"(\d+)-(\d+)", pattern)
    for i, b in enumerate(blocks):
        if span and int(span[1]) <= i <= int(span[2]) or not span and ((b[0] == "h" and not p) or (p and p in plain(b))):
            print(i, b[0], b[1] if b[0] == "h" else "", text(b)[:110].replace("\n", " "))


def main():
    if "--outline" in sys.argv:
        return outline(*[a for a in sys.argv[1:] if a != "--outline"])
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    sources = {r["key"]: r for r in csv.DictReader(open(DATA / "sources.csv", encoding="utf-8"))}
    all_rows = rows()
    uses = {}
    for r in all_rows:
        uses[r["source"]] = uses.get(r["source"], 0) + 1
    report, cache = [], {}
    todo = [r for r in all_rows if r["id"] in only] if only else all_rows if "--redo" in sys.argv else \
        [r for r in all_rows if not (LIB / r["id"] / "text.md").exists()]
    todo.sort(key=lambda r: r["source"])
    for r in todo:
        src = sources[r["source"]]
        if src["where"].startswith(("wikisource:", "sefaria:", "sacredtexts:")):
            blocks = {"wikisource": wikisource, "sefaria": sefaria, "sacredtexts": sacred}[src["where"].split(":")[0]](r, src)
            got, how = ((blocks, None), src["where"].split(":")[0]) if blocks else (None, "empty")
        elif src["where"] != "gutenberg":
            report.append((r["id"], "other source, by hand", 0, 0, "", ""))
            continue
        else:
            got, how = gutenberg(r, src, uses, cache)
        if not got:
            report.append((r["id"], how, 0, 0, "", ""))
            continue
        text = write_story(r["id"], got[0], got[1], {"source_part": how})
        if text is None:
            report.append((r["id"], "hand (kept)", 0, 0, "", ""))
            continue
        body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
        report.append((r["id"], how, len(body.split()), text.count("](art/"), " ".join(body.split()[:14]),
                       " ".join(body.split()[-10:])))
        print(r["id"], how, len(body.split()), flush=True)
    sw = DATA / "stories-sw.csv"
    for r in csv.DictReader(open(sw, encoding="utf-8")):
        if r["decision"] == "reserve" or (only and r["id"] not in only) or "--redo" in sys.argv or \
                (not only and (LIB / r["id"] / "text.md").exists()):
            continue
        report.append((r["id"], storyweaver(r), 0, 0, "", ""))
    bad = [x for x in report if x[1] in ("no epub", "not placed") or "missing" in x[1] or x[1].startswith("other")]
    print(len(report), "processed;", len(bad), "need a look:")
    for x in bad:
        print(" ", x[0], x[1])
    if "--report" in sys.argv:
        with open(SRC / "process-report.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([("id", "how", "words", "art", "starts", "ends")] + report)


if __name__ == "__main__":
    main()
