"""Token report for a course-run token log.

Usage: python -X utf8 scripts/tokens.py <token-log.csv> [--md]

Log columns: stage, course, unit, sections, tokens, minutes, note
(minutes there is agent wall time, not class time; it is ignored).

RULES (edit here if the stage names change)
- OTHER (not fill): stage starts with "sample" (sample, samplefix,
  samplefix-sens) or is "fix-after-report" (science's fixes that follow the
  sample report). These measure the run's quality check, not building the course.
- FILL: every other stage (day writing, section plans, plan data, keys, day
  lists, texts, fix, runend-fix, cleanup, checks, sensitivity, capstone, catchup,
  science day-write / section-write / plan-data ...). Matches the SS+ELA report
  (83.31M fill = log total minus sample, samplefix, samplefix-sens).
- PLANNING (a subset of fill, also reported per unit): sec, sections,
  section-write (section plans); data, plan-data, data-fix (plan data);
  key (answer-key check); days (day lists).
- Days written: rows in data/plans/<course>/days.csv (falls back to the
  frames.csv "days" column). Class minutes per day: midpoint of frames.csv
  minutes_min and minutes_max (the DEFAULTS.md day length). Rows whose course
  has no days (subject-level jobs, e.g. "social-studies") count in fill and in
  the totals but show no per-day figure.
- Tokens per day = fill / days. Tokens per class minute = fill / (days * minutes).
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANNING = {"sec", "sections", "section-write", "data", "plan-data", "data-fix", "key", "days"}


def is_other(stage):
    return stage.startswith("sample") or stage == "fix-after-report"


def frames():
    out = {}
    with open(ROOT / "data/plans/frames.csv", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            out[r["course"]] = r
    return out


def days_written(course, fr):
    p = ROOT / "data/plans" / course / "days.csv"
    if p.exists():
        with open(p, encoding="utf-8", newline="") as f:
            return sum(1 for _ in csv.DictReader(f))
    return int(fr[course]["days"]) if course in fr else 0


def fmt(n):
    return f"{n:,}"


def k(n):
    return f"{n/1000:.0f}k" if n >= 10000 else f"{n/1000:.2f}k"


def m(n):
    return f"{n/1e6:.2f}M"


def table(head, rows, md):
    if md:
        print("| " + " | ".join(head) + " |")
        print("|" + "---|" * len(head))
        for r in rows:
            print("| " + " | ".join(str(c) for c in r) + " |")
    else:
        w = [max(len(str(x)) for x in col) for col in zip(head, *rows)]
        for r in [head] + rows:
            print("  ".join(str(c).ljust(w[i]) if i == 0 else str(c).rjust(w[i]) for i, c in enumerate(r)))
    print()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    md = "--md" in sys.argv
    if len(args) != 1:
        print(__doc__)
        sys.exit(1)
    with open(args[0], encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    fr = frames()
    fill = defaultdict(int)
    other = defaultdict(int)
    stage_fill = defaultdict(int)
    stage_other = defaultdict(int)
    plan_unit = defaultdict(lambda: defaultdict(int))
    for r in rows:
        t = int(r["tokens"] or 0)
        c, s = r["course"], r["stage"]
        if is_other(s):
            other[c] += t
            stage_other[s] += t
        else:
            fill[c] += t
            stage_fill[s] += t
            if s in PLANNING and r["unit"]:
                plan_unit[(c, s)][r["unit"]] += t
    h = "### " if md else "== "
    print(f"{h}Fill by course ({args[0]})")
    body = []
    td = tm = 0
    tf = sum(fill.values())
    for c in sorted(fill):
        d = days_written(c, fr) if c in fr else 0
        if d:
            mn = (int(fr[c]["minutes_min"]) + int(fr[c]["minutes_max"])) / 2
            ms = f"{mn:g}"
            td += d
            tm += d * mn
            body.append([c, d, ms, m(fill[c]), k(fill[c] / d), k(fill[c] / (d * mn))])
        else:
            body.append([c, "-", "-", m(fill[c]), "-", "-"])
    body.append(["All", td, "", m(tf), k(tf / td) if td else "-", k(tf / tm) if tm else "-"])
    table(["Course", "Days", "Class min/day", "Fill tokens", "Per day", "Per class min"], body, md)
    print(f"{h}Fill by stage")
    table(["Stage", "Tokens", "Planning"], [[s, m(v), "yes" if s in PLANNING else ""]
          for s, v in sorted(stage_fill.items(), key=lambda x: -x[1])] + [["Total fill", m(tf), ""]], md)
    print(f"{h}Not fill (quality-check stages)")
    to = sum(other.values())
    table(["Stage", "Tokens"], [[s, m(v)] for s, v in sorted(stage_other.items(), key=lambda x: -x[1])]
          + [["Total not fill", m(to)]], md)
    print(f"{h}Not fill by course")
    table(["Course", "Tokens"], [[c, m(v)] for c, v in sorted(other.items())], md)
    print(f"{h}Planning stages per unit")
    body = []
    for (c, s), u in sorted(plan_unit.items()):
        tot = sum(u.values())
        body.append([c, s, len(u), m(tot), k(tot / len(u))])
    table(["Course", "Stage", "Units", "Tokens", "Per unit"], body, md)
    print(f"{h}All courses")
    table(["Fill", "Not fill", "Log total"], [[m(tf), m(to), m(tf + to)]], md)


main()
