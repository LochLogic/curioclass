"""Merge checked gap-fill staging folders into the data files.

    python scripts/overlap/stage_merge.py docs/agents/gapfill/<domain> [...]

Run stage_check.py on the same folders first; this refuses to run if it reports errors. Then, per folder:
- modules.txt lines are appended to their data/modules/<source.txt> under a `# Gap fill` comment,
- concepts.txt lines to data/concepts/<subject file> (ela, eld and library go in ela.txt; math, science and
  social studies in their own files; everything else in electives.txt),
- tags.csv rows to docs/agents/overlap/tags.csv,
- codes.txt goes through scripts/add_codes.py.
Then build_db.py and check_concepts.py --write regenerate modules.csv and tools-concepts.csv.
"""
import csv, io, os, subprocess, sys
from common import ROOT, OUT

CONCEPT_FILE = {'ela': 'ela.txt', 'eld': 'ela.txt', 'library': 'ela.txt', 'math': 'math.txt', 'science': 'science.txt',
                'social-studies': 'social-studies.txt'}


def lines(path):
    if not os.path.exists(path): return []
    return [l.rstrip('\r\n') for l in io.open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]


def append(path, header, new):
    if not new: return
    text = io.open(path, encoding='utf-8').read()
    nl = '\r\n' if '\r\n' in text else '\n'
    if not text.endswith(nl): text += nl
    text += nl + header + nl + nl.join(new) + nl
    io.open(path, 'w', encoding='utf-8', newline='').write(text)


def main():
    dirs = sys.argv[1:]
    py = sys.executable
    here = os.path.dirname(__file__)
    if subprocess.run([py, os.path.join(here, 'stage_check.py'), *dirs, '--quiet'], stdout=subprocess.DEVNULL).returncode:
        raise SystemExit('stage_check.py reports errors: fix them first')
    courses = {c['course_id']: c['subject'] for c in csv.DictReader(io.open(os.path.join(ROOT, 'data', 'courses.csv'), encoding='utf-8'))}
    tag_fields = next(csv.reader(io.open(os.path.join(OUT, 'tags.csv'), encoding='utf-8')))
    for d in dirs:
        name = os.path.basename(d.rstrip('/\\'))
        header = f'# Gap fill 2026-10-27 ({name}): see docs/agents/gapfill/{name}/notes.md'
        by_src, subj_of = {}, {}
        for l in lines(os.path.join(d, 'modules.txt')):
            src, rest = l.split('|', 1)
            by_src.setdefault(src.strip(), []).append(rest)
        for src, new in by_src.items():
            append(os.path.join(ROOT, 'data', 'modules', src), header, new)
        for l in lines(os.path.join(d, 'modules.txt')):
            p = [x.strip() for x in l.split('|')]
            subj_of[p[2]] = courses[p[2]]
        by_file = {}
        for l in lines(os.path.join(d, 'concepts.txt')):
            mid = l.split('|', 1)[0].strip()
            subject = next((s for s in sorted(set(courses.values()), key=len, reverse=True) if mid.startswith(s + '-')), None)
            by_file.setdefault(CONCEPT_FILE.get(subject, 'electives.txt'), []).append(l)
        for f, new in by_file.items():
            append(os.path.join(ROOT, 'data', 'concepts', f), header, new)
        tp = os.path.join(d, 'tags.csv')
        if os.path.exists(tp):
            with io.open(os.path.join(OUT, 'tags.csv'), 'a', encoding='utf-8', newline='') as f:
                w = csv.DictWriter(f, fieldnames=tag_fields, extrasaction='ignore', lineterminator='\n')
                for r in csv.DictReader(io.open(tp, encoding='utf-8')):
                    w.writerow(r)
        cp = os.path.join(d, 'codes.txt')
        if lines(cp):
            subprocess.run([py, os.path.join(ROOT, 'scripts', 'add_codes.py'), cp], check=True)
        print(f'merged {name}')
    subprocess.run([py, os.path.join(ROOT, 'scripts', 'build_db.py')], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([py, os.path.join(ROOT, 'scripts', 'check_concepts.py'), '--write'], check=True)


if __name__ == '__main__':
    main()
