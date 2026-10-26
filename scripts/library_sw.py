"""Split the StoryWeaver export into one clean JSON per book.

Input: library/_sources/storyweaver/_all.json (saved from Cory's signed-in Chrome: {id: {meta, info, read}}).
Output: library/_sources/storyweaver/<id>.json with title, level, publisher, authors, illustrators, license,
attribution text, and pages [{text, image}] (largest illustration crop), plus _index.csv for curation.
"""
import csv
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SW = ROOT / "library" / "_sources" / "storyweaver"


def text_of(h):
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<img[^>]*>", " ", h)
    h = re.sub(r"</p>|<br\s*/?>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    lines = (" ".join(line.split()) for line in t.splitlines())
    return "\n".join(x for x in lines if x and not re.fullmatch(r"\d+/\d+", x))


def biggest(h):
    urls = re.findall(r'data-size(\d+)-src="([^"]+)"', h)
    return max(urls, key=lambda u: int(u[0]))[1] if urls else ""


def main():
    data = json.loads((SW / "_all.json").read_text(encoding="utf-8"))
    rows = []
    for sid, b in data.items():
        meta, pages = b["meta"], b["read"]["pages"]
        story = [{"text": text_of(p["html"]), "image": biggest(p["html"])} for p in pages if p["pageType"] == "StoryPage"]
        back = " ".join(text_of(p["html"]) for p in pages if p["pageType"] == "BackInnerCoverPage")
        lic = re.search(r"Released under (CC[ -][A-Z -]*?\d\.\d)", back)
        words = sum(len(p["text"].split()) for p in story)
        out = {
            "sw_id": sid, "slug": meta["slug"], "title": meta["t"], "level": meta["l"], "publisher": meta["pub"],
            "authors": meta["a"], "illustrators": meta["i"], "description": meta["d"], "reads": meta["r"],
            "license": lic.group(1).strip() if lic else "", "attribution": back, "words": words,
            "cover": biggest(pages[0]["html"]) if pages else "", "pages": story,
            "url": f"https://storyweaver.org.in/en/stories/{meta['slug']}",
        }
        (SW / f"{sid}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        rows.append({k: out[k] for k in ("sw_id", "level", "title", "publisher", "license", "words", "reads", "description")})
    with open(SW / "_index.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "books")


if __name__ == "__main__":
    main()
