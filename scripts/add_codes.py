"""Add (or drop) standards codes on existing modules, in the source files data/modules/*.txt.

    python scripts/add_codes.py PLAN.txt [PLAN.txt ...] [--dry]

data/modules.csv is generated from data/modules/*.txt by build_db.py, so code edits go in the source line. Each plan
line is `module_id: CODE; CODE; -CODE  # reason`. A plain code is appended when the module lacks it; `-CODE` removes it.
Blank lines and lines starting with # are skipped. Every code is checked with standards.validate before anything is
written, and an unknown module id stops the run. Run `python scripts/build_db.py` afterwards.
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from standards import validate

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def subjects():
    import csv
    with open(DATA / 'courses.csv', newline='', encoding='utf-8') as f:
        return {c['course_id']: c['subject'] for c in csv.DictReader(f)}


def read_plan(paths):
    plan, errors = {}, []
    for p in paths:
        for n, line in enumerate(Path(p).read_text(encoding='utf-8').splitlines(), 1):
            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            mid, _, codes = line.partition(':')
            for c in (c.strip() for c in codes.split(';') if c.strip()):
                if validate(c.lstrip('-')) is None:
                    errors.append(f'{p}:{n}: invalid code {c}')
                plan.setdefault(mid.strip(), []).append(c)
    return plan, errors


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    plan, errors = read_plan(args)
    course_subject = subjects()
    done, changed = set(), 0
    for path in sorted((DATA / 'modules').glob('*.txt')):
        lines = path.read_text(encoding='utf-8').splitlines(keepends=True)
        dirty = False
        for n, line in enumerate(lines):
            if not line.strip() or line.startswith('#'):
                continue
            parts = line.rstrip('\r\n').split('|')
            if len(parts) != 6:
                continue
            grade, course, title = parts[0].strip(), parts[1].strip(), parts[3].strip()
            mid = f'{course_subject.get(course, "?")}-{grade}-{slug(title)}'
            if mid not in plan:
                continue
            done.add(mid)
            codes = [c.strip() for c in parts[5].split(';') if c.strip()]
            new = list(codes)
            for c in plan[mid]:
                if c.startswith('-'):
                    new = [x for x in new if x != c[1:]]
                elif c not in new:
                    new.append(c)
            if new != codes:
                parts[5] = ';'.join(new)
                lines[n] = '|'.join(parts) + line[len(line.rstrip('\r\n')):]
                dirty = True
                changed += 1
        if dirty and '--dry' not in sys.argv and not errors:
            path.write_text(''.join(lines), encoding='utf-8', newline='')
    errors += [f'unknown module {m}' for m in plan if m not in done]
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print(f'{changed} modules changed' + (' (dry run)' if '--dry' in sys.argv else ''))


if __name__ == '__main__':
    main()
