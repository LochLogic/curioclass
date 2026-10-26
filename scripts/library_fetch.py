"""Download Reading Room source books from a Project Gutenberg mirror into library/_sources/gutenberg/<pg>/.

Gets the illustrated EPUB3 and the plain text for every pg id in data/library/sources.csv. Polite: one request every
2 seconds, from the aleph.pglaf.org mirror (Gutenberg asks robots to use mirrors). Skips files already on disk.
`--storyweaver` instead gets the illustrations for data/library/stories-sw.csv (run scripts/library_sw.py first).
`--other` gets the Wikisource sources (`where` = wikisource:<page>) into library/_sources/other/<key>/text.txt.
`--archive` gets Internet Archive OCR text (`where` = archive:<identifier>) and `--sefaria` a whole Tanakh version from
Sefaria (`where` = sefaria:<version title>), into the same other/<key>/ folders.
"""
import csv
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "library" / "_sources" / "gutenberg"
MIRROR = "https://aleph.pglaf.org/cache/epub/{n}/{f}"
UA = {"User-Agent": "CurioClass-ReadingRoom/1.0 (curioclass.org)"}


def get(url, dest, pause=2):
    if dest.exists() and dest.stat().st_size > 0:
        return "have"
    try:
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=180).read()
    except Exception as e:
        return f"FAIL {e}"
    dest.write_bytes(data)
    time.sleep(pause)
    return f"{len(data) // 1024} KB"


def storyweaver():
    """Illustrations for the picked StoryWeaver books (public image URLs; the text came from the signed-in export)."""
    sw = ROOT / "library" / "_sources" / "storyweaver"
    for row in csv.DictReader(open(ROOT / "data/library/stories-sw.csv", encoding="utf-8")):
        book = json.loads((sw / f"{row['sw_id']}.json").read_text(encoding="utf-8"))
        d = sw / row["sw_id"]
        d.mkdir(exist_ok=True)
        urls = [("cover", book["cover"])] + [(f"p{i + 1:02d}", p["image"]) for i, p in enumerate(book["pages"])]
        for name, url in urls:
            if url:
                print(row["sw_id"], name, get(url, d / f"{name}{pathlib.Path(url).suffix}", 0.2), flush=True)


def wikisource():
    """Sources whose `where` is wikisource:<page> go to library/_sources/other/<key>/ (page plus any subpages, as text)."""
    api = "https://en.wikisource.org/w/api.php?"
    for row in csv.DictReader(open(ROOT / "data/library/sources.csv", encoding="utf-8")):
        if not row["where"].startswith("wikisource:"):
            continue
        page, d = row["where"][len("wikisource:"):], ROOT / "library" / "_sources" / "other" / row["key"]
        if (d / "text.txt").exists():
            continue
        d.mkdir(parents=True, exist_ok=True)
        pages = [page] + [p["title"] for p in fetch_json(api + urllib.parse.urlencode(
            {"action": "query", "list": "allpages", "apprefix": page + "/", "aplimit": 200, "format": "json"}))["query"]["allpages"]]
        parts = []
        for p in pages:
            got = fetch_json(api + urllib.parse.urlencode({"action": "parse", "page": p, "prop": "text", "format": "json"}))
            if "parse" in got:
                parts.append(f"== {p} ==\n" + html_text(got["parse"]["text"]["*"]))
        if parts:
            (d / "text.txt").write_text("\n\n".join(parts), encoding="utf-8")
            (d / "source.json").write_text(json.dumps({"pages": pages, "url": "https://en.wikisource.org/wiki/" + urllib.parse.quote(page)}, indent=1), encoding="utf-8")
        print(row["key"], len(parts), "of", len(pages), "pages", flush=True)


def archive():
    """Internet Archive books: the OCR plain text (<id>_djvu.txt). Rough; cleaned up in processing."""
    for row in csv.DictReader(open(ROOT / "data/library/sources.csv", encoding="utf-8")):
        if not row["where"].startswith("archive:"):
            continue
        ident, d = row["where"][len("archive:"):], ROOT / "library" / "_sources" / "other" / row["key"]
        d.mkdir(parents=True, exist_ok=True)
        files = fetch_json(f"https://archive.org/metadata/{ident}")["files"]
        name = next((f["name"] for f in files if f["name"].endswith("_djvu.txt")), f"{ident}_djvu.txt")
        print(row["key"], get(f"https://archive.org/download/{ident}/{urllib.parse.quote(name)}", d / "text.txt", 3), flush=True)
        (d / "source.json").write_text(json.dumps({"url": f"https://archive.org/details/{ident}"}, indent=1), encoding="utf-8")


def sefaria():
    """A Tanakh translation from Sefaria, book by book, as text with chapter and verse numbers."""
    for row in csv.DictReader(open(ROOT / "data/library/sources.csv", encoding="utf-8")):
        if not row["where"].startswith("sefaria:"):
            continue
        version, d = row["where"][len("sefaria:"):], ROOT / "library" / "_sources" / "other" / row["key"]
        if (d / "text.txt").exists():
            continue
        d.mkdir(parents=True, exist_ok=True)
        index = fetch_json("https://www.sefaria.org/api/index/")
        tanakh = next(c for c in index if c["category"] == "Tanakh")
        books = [b["title"] for sec in tanakh["contents"] if sec.get("category") in ("Torah", "Prophets", "Writings")
                 for b in sec["contents"] if "title" in b]
        parts = []
        for book in books:
            got = fetch_json(f"https://www.sefaria.org/api/v3/texts/{urllib.parse.quote(book)}?"
                             + urllib.parse.urlencode({"version": "english|" + version}))
            chapters = got["versions"][0]["text"] if got.get("versions") else []
            parts.append(f"== {book} ==\n" + "\n".join(
                f"{c}:{v} " + html_text(t) for c, ch in enumerate(chapters, 1) for v, t in enumerate(ch, 1) if t))
            print(row["key"], book, len(chapters), "chapters", flush=True)
        (d / "text.txt").write_text("\n\n".join(parts), encoding="utf-8")
        (d / "source.json").write_text(json.dumps({"version": version, "books": books, "url": "https://www.sefaria.org/texts/Tanakh"}, indent=1), encoding="utf-8")


def fetch_json(url):
    for wait in (6, 30, 90):
        time.sleep(wait)
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("still rate limited: " + url)


def html_text(h):
    h = re.sub(r"<(style|script).*?</\1>", " ", h, flags=re.S)
    h = re.sub(r"</p>|<br\s*/?>|</div>|</h\d>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    return "\n".join(" ".join(x.split()) for x in t.splitlines() if x.strip())


def main():
    if "--storyweaver" in sys.argv:
        return storyweaver()
    if "--other" in sys.argv:
        return wikisource()
    if "--archive" in sys.argv:
        return archive()
    if "--sefaria" in sys.argv:
        return sefaria()
    for row in csv.DictReader(open(ROOT / "data/library/sources.csv", encoding="utf-8")):
        for n in row["pg"].split():
            d = OUT / n
            d.mkdir(parents=True, exist_ok=True)
            for f in (f"pg{n}-images-3.epub", f"pg{n}.txt"):
                print(row["key"], n, f, get(MIRROR.format(n=n, f=f), d / f), flush=True)


if __name__ == "__main__":
    main()
