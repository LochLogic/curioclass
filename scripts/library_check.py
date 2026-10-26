"""Check the Reading Room manifest against the downloaded sources.

Every story row in data/library/stories-pd.csv must point at a source in data/library/sources.csv, and its `find`
text must appear in that source's downloaded plain text (library/_sources/gutenberg/<pg>/pg<pg>.txt). Rows with an
empty `find` (sets picked in processing) only need the source file. StoryWeaver rows (data/library/stories-sw.csv)
must have their saved JSON. data/library/speeches.csv (its own collection) is checked the same way. Prints a summary by
band (reserve rows and speeches are checked but not counted) and every problem.
"""
import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "library" / "_sources"


def band(grades):
    lo = grades.split("-")[0]
    g = 0 if lo == "K" else int(lo)
    return "K-2" if g <= 2 else "3-5" if g <= 5 else "6-8" if g <= 8 else "9-12"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("’", "'")).strip()


def main():
    sources = {r["key"]: r for r in csv.DictReader(open(ROOT / "data/library/sources.csv", encoding="utf-8"))}
    texts, problems, bands, reserve, speeches = {}, [], {}, 0, 0
    rows = [(r, False) for r in csv.DictReader(open(ROOT / "data/library/stories-pd.csv", encoding="utf-8"))]
    rows += [(r, True) for r in csv.DictReader(open(ROOT / "data/library/speeches.csv", encoding="utf-8"))]
    for r, speech in rows:
        s = sources.get(r["source"])
        if not s:
            problems.append(f"{r['id']}: unknown source {r['source']}")
            continue
        other = SRC / "other" / r["source"] / "text.txt"
        if not s["pg"] and not other.exists():
            problems.append(f"{r['id']}: source {r['source']} not downloaded yet ({s['where']})")
            continue
        if r["source"] not in texts:
            parts = [other.read_text(encoding="utf-8")] if other.exists() else []
            for n in s["pg"].split():
                p = SRC / "gutenberg" / n / f"pg{n}.txt"
                if p.exists():
                    parts.append(p.read_text(encoding="utf-8", errors="replace"))
            texts[r["source"]] = norm(" ".join(parts)) if parts else None
        t = texts[r["source"]]
        if t is None:
            problems.append(f"{r['id']}: source text missing for {r['source']}")
            continue
        if r["find"] and norm(r["find"]) not in t:
            problems.append(f"{r['id']}: '{r['find']}' not found in {r['source']}")
            continue
        if r["decision"] == "reserve" or speech:
            reserve += r["decision"] == "reserve"
            speeches += speech
            continue
        bands[band(r["grades"])] = bands.get(band(r["grades"]), 0) + 1
    sw = ROOT / "data/library/stories-sw.csv"
    if sw.exists():
        for r in csv.DictReader(open(sw, encoding="utf-8")):
            if not (SRC / "storyweaver" / f"{r['sw_id']}.json").exists():
                problems.append(f"{r['id']}: StoryWeaver JSON missing")
                continue
            bands[band(r["grades"])] = bands.get(band(r["grades"]), 0) + 1
    print("ok by band:", dict(sorted(bands.items())), "total", sum(bands.values()), "| reserve", reserve, "| speeches", speeches)
    print(len(problems), "problems")
    for p in problems:
        print(" ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
