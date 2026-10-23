"""Build data/modules.csv and data/curioclass.db from data/modules/*.txt and the catalog CSVs.

Run from the repo root:  python scripts/build_db.py
Fails loudly on bad rows so the data stays clean.
"""
import csv, re, sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from standards import validate

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
GRADES = ['k'] + [str(i) for i in range(1, 13)]


def expand(span):
    a, _, b = span.partition('-')
    b = b or a
    if a not in GRADES or b not in GRADES:
        raise ValueError(f'bad grade span {span!r}')
    return GRADES[GRADES.index(a):GRADES.index(b) + 1]


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def read_csv(name):
    with open(DATA / name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


courses = {c['course_id']: c for c in read_csv('courses.csv')}

# grade_subjects.csv is derived from courses.csv
with open(DATA / 'grade_subjects.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['grade', 'subject', 'course_id', 'core'])
    for c in courses.values():
        for g in expand(c['grades']):
            w.writerow([g, c['subject'], c['course_id'], c['core']])
errors, modules, seen = [], [], set()

for path in sorted((DATA / 'modules').glob('*.txt')):
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('|')
        where = f'{path.name}:{n}'
        if len(parts) != 6:
            errors.append(f'{where}: expected 6 fields, got {len(parts)}')
            continue
        grade, course, strand, title, desc, standards = (p.strip() for p in parts)
        if course not in courses:
            errors.append(f'{where}: unknown course {course}')
            continue
        try:
            grades = expand(grade)
            if not set(grades) <= set(expand(courses[course]['grades'])):
                errors.append(f'{where}: grade {grade} outside course {course} ({courses[course]["grades"]})')
        except ValueError as e:
            errors.append(f'{where}: {e}')
            continue
        codes = [c.strip() for c in standards.split(';') if c.strip()]
        frameworks = [validate(c) for c in codes]
        if not codes or None in frameworks:
            errors.append(f'{where}: invalid or missing standards code(s) in {standards!r}')
            continue
        standards = ';'.join(codes)
        subject = courses[course]['subject']
        mid = f'{subject}-{grade}-{slug(title)}'
        if mid in seen:
            errors.append(f'{where}: duplicate module id {mid}')
        seen.add(mid)
        modules.append(dict(module_id=mid, subject=subject, grade=grade, course_id=course,
                            strand=strand, title=title, description=desc, standards=standards,
                            frameworks=';'.join(dict.fromkeys(frameworks)), source=path.name))

if errors:
    print('\n'.join(errors))
    sys.exit(1)

fields = ['module_id', 'subject', 'grade', 'course_id', 'strand', 'title', 'description', 'standards', 'frameworks', 'source']
with open(DATA / 'modules.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(modules)

db_path = DATA / 'curioclass.db'
db_path.unlink(missing_ok=True)
db = sqlite3.connect(db_path)
for name in ['grades', 'bands', 'subjects', 'courses', 'grade_subjects', 'tool-types', 'tools', 'modules']:
    rows = read_csv(f'{name}.csv')
    table = name.replace('-', '_')
    cols = list(rows[0].keys())
    db.execute(f'CREATE TABLE {table} ({", ".join(f"\"{c}\" TEXT" for c in cols)})')
    db.executemany(f'INSERT INTO {table} VALUES ({",".join("?" * len(cols))})',
                   [[r[c] for c in cols] for r in rows])
db.execute('CREATE TABLE module_grades (module_id TEXT, grade TEXT)')
db.executemany('INSERT INTO module_grades VALUES (?,?)',
               [(m['module_id'], g) for m in modules for g in expand(m['grade'])])
db.commit()

# Coverage: modules per subject per grade (a band-level module counts in each grade it spans)
subjects = [s['subject_id'] for s in read_csv('subjects.csv')]
counts = dict(db.execute('SELECT m.subject || "|" || g.grade, count(*) FROM modules m '
                         'JOIN module_grades g USING(module_id) GROUP BY 1').fetchall())
print(f'{len(modules)} modules\n')
print('subject'.ljust(18) + ''.join(g.rjust(4) for g in GRADES))
for s in subjects:
    print(s.ljust(18) + ''.join(str(counts.get(f'{s}|{g}', '.')).rjust(4) for g in GRADES))
db.close()
