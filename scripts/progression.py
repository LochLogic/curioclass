"""Gate for data/progressions/<subject>.csv (PRODUCTION-PATH step 1).

    python -X utf8 scripts/progression.py check [subject]

One row per skill: strand, grade, skill_id, standard, assumes, hands_on, model_in, model_out, words,
cross_subject, notes. Lists are '; ' separated.

FAIL (exit 1):
- a missing column, a blank skill_id, standard or notes, a grade outside K and 1 to 12, a duplicate skill_id;
- a standard code that is not in the subject's standards files;
- an anchor standard named by no row (unless listed in <subject>-excluded.csv with a reason), or named by
  rows of two grades (owned twice);
- an assumes id that does not exist or is not at an earlier grade; a hands_on id that does not exist or is not
  at a later grade; a hands_on not matched by the target's assumes, or an assumes not matched by the source's
  hands_on (both ends of a handoff are written);
- a model_in at grade g that no row hands on at an earlier grade and no row of grade g introduces
  (has it in model_out without it in model_in);
- a cross_subject entry that is not subject:CODE with a code in that subject's standards file, or
  subject:skill_id with an id in that subject's progression file once it exists.
A standard written ~CODE marks a row that contributes to a standard another row owns (added 2026-11-13): it is
checked as a code but does not count as owning it, and the code must be owned by some row (an earlier contributing
row starts the work; a later one applies it).
An ELA code sits in its own grade; a band code (9-10, 11-12) is owned by the band's last grade and started
with ~CODE in the earlier one. A K to 8 math code sits in its own grade (4.NBT.B.5 in grade 4); high school math codes
carry no grade.
A (+) high school math part is covered only when named or excluded itself, not through its parent. A cross_subject
code must be named by a row of the other subject once that subject's progression exists (added 2026-11-13).
Lean timing (added 2026-11-13, cross-subject read finding 1): a cross_subject lean must be taught at or before the
leaning row's grade, meaning the named skill id's grade, or for a code the earliest grade of any row of the other
subject that owns it or ~ contributes to it (high school by course grade: 9 Biology and Algebra I, 10 Chemistry and
Geometry, 11 Physics and Algebra II). A forward lean FAILs unless the row's notes carry an explicit
"Just in time:" teach that names the same id or code; then it is a note.
note (exit 0): a handoff that skips one or more grades; a C3 indicator named in more than one grade (depth must
differ, and the notes must say how); a C3 indicator of a grade band named by no grade in that band; grade row counts.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = ['strand', 'grade', 'skill_id', 'standard', 'assumes', 'hands_on', 'model_in', 'model_out', 'words',
        'cross_subject', 'notes']
GRADES = ['K'] + [str(g) for g in range(1, 13)]
GI = {g: i for i, g in enumerate(GRADES)}
STD_FILES = {'social-studies': ['ma-hss-2018.txt', 'c3-indicators.txt'],
             'math': ['ccss-math-standards.txt'],
             'ela': ['ccss-ela-standards.txt', 'ccss-ela-standards-full.txt'],
             'science': ['ngss-pes.txt']}
ANCHOR = {'social-studies': 'ma-hss-2018.txt', 'science': 'ngss-pes.txt', 'ela': 'ccss-ela-standards.txt',
          'math': 'ccss-math-standards.txt'}


def code_grades(subject, code):
    """(owner grades, all grades) a grade-coded standard may sit in, or None when the code carries no grade.
    ELA: RL.4.2 sits in grade 4; a band code (RL.9-10.1) is used across the band and owned by its last grade."""
    if subject == 'math':
        g = code.split('.')[0]
        return ([g], [g]) if g in GI else None
    if subject != 'ela':
        return None
    p = code.split('.')
    if len(p) < 3:
        return None
    g = p[1]
    if g in GI:
        return [g], [g]
    if '-' in g:
        a, b = g.split('-')
        if a in GI and b in GI:
            band = GRADES[GI[a]:GI[b] + 1]
            return [b], band
    return None
HEADING = re.compile(r'^MA\.[A-Z0-9]+\.T\d+[a-z]?$')
BAND = {'K-2': ['K', '1', '2'], '3-5': ['3', '4', '5'], '6-8': ['6', '7', '8'], '9-12': ['9', '10', '11', '12']}


def split(cell):
    return [x.strip() for x in (cell or '').split(';') if x.strip()]


def codes(fname):
    out = []
    for line in open(os.path.join(ROOT, 'data', 'standards', fname), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        out.append(line.split('\t')[0].split()[0].strip())
    return out


def load(subject):
    p = os.path.join(ROOT, 'data', 'progressions', subject + '.csv')
    if not os.path.exists(p):
        return None
    return list(csv.DictReader(open(p, encoding='utf-8', newline='')))


def parent(code):
    m = re.match(r'^(.*\d)[a-z]$', code)
    return m.group(1) if m else None


def other_grade(other, ref):
    """Earliest grade at which another subject owns or ~ contributes to ref (a skill id or a standard code)."""
    best = None
    for o in other:
        hit = o['skill_id'] == ref
        if not hit:
            for c in split(o['standard']):
                c = c.lstrip('~')
                if c == ref or parent(c) == ref or c == parent(ref):
                    hit = True
                    break
        g = (o['grade'] or '').strip()
        if hit and g in GI and (best is None or GI[g] < GI[best]):
            best = g
    return best


def check(subject):
    fails, notes = [], []
    rows = load(subject)
    if rows is None:
        return ['no file data/progressions/%s.csv' % subject], notes, 0
    if rows and list(rows[0].keys()) != COLS:
        fails.append('columns must be: ' + ', '.join(COLS))
        return fails, notes, len(rows)
    known = set()
    for f in STD_FILES.get(subject, []):
        known.update(codes(f))
    by_id, grade_of = {}, {}
    for n, r in enumerate(rows, 2):
        sid = (r['skill_id'] or '').strip()
        where = 'line %d %s' % (n, sid or '(no id)')
        if not sid:
            fails.append(where + ': blank skill_id')
            continue
        if sid in by_id:
            fails.append(where + ': duplicate skill_id')
        by_id[sid] = r
        g = (r['grade'] or '').strip()
        if g not in GI:
            fails.append(where + ': grade %r not K or 1 to 12' % g)
        grade_of[sid] = g
        for c in ('standard', 'notes', 'strand'):
            if not (r[c] or '').strip():
                fails.append(where + ': blank ' + c)
        for code in split(r['standard']):
            code = code.lstrip('~')
            if code not in known:
                fails.append(where + ': standard %s not in the standards files' % code)
    # anchor coverage and single-grade ownership
    owners, contrib = {}, []
    for sid, r in by_id.items():
        for code in split(r['standard']):
            if code.startswith('~'):
                contrib.append((sid, code[1:]))
                continue
            owners.setdefault(code, set()).add(grade_of[sid])
    for sid, r in by_id.items():
        for raw in split(r['standard']):
            cg = code_grades(subject, raw.lstrip('~'))
            if not cg:
                continue
            allowed = cg[1] if raw.startswith('~') else cg[0]
            if grade_of[sid] not in allowed:
                fails.append('%s (grade %s) %s %s: belongs in grade(s) %s' % (
                    sid, grade_of[sid], 'contributes to' if raw.startswith('~') else 'owns', raw.lstrip('~'), ', '.join(allowed)))
    for sid, code in contrib:
        if code not in owners:
            fails.append('%s contributes to %s, which no row owns' % (sid, code))
    if subject in ANCHOR:
        excl = {}
        ep = os.path.join(ROOT, 'data', 'progressions', subject + '-excluded.csv')
        if os.path.exists(ep):
            for e in csv.DictReader(open(ep, encoding='utf-8', newline='')):
                if not (e.get('reason') or '').strip():
                    fails.append('excluded %s has no reason' % e['code'])
                excl[e['code'].strip()] = e
        anchor = codes(ANCHOR[subject])
        plus_codes = set()
        for line in open(os.path.join(ROOT, 'data', 'standards', ANCHOR[subject]), encoding='utf-8'):
            if not line.startswith('#') and '(+)' in line:
                plus_codes.add(line.split('	')[0].split()[0].strip())
        kids = {}
        for code in anchor:
            if parent(code):
                kids.setdefault(parent(code), []).append(code)
        for code in anchor:
            if HEADING.match(code):
                continue
            plus = code in plus_codes
            named = code in owners or (parent(code) in owners and not plus) or (
                code in kids and all(k in owners for k in kids[code]))
            if code in excl:
                if code in owners:
                    fails.append('%s is both excluded and named' % code)
                continue
            if not named:
                fails.append('%s named by no skill' % code)
        for code, gs in owners.items():
            if (code.startswith('MA.') or subject != 'social-studies') and len(gs) > 1:
                fails.append('%s owned by grades %s' % (code, ', '.join(sorted(gs, key=GI.get))))
    for code, gs in owners.items():
        if code.startswith('D') and len(gs) > 1:
            notes.append('%s named in grades %s (say in notes how the depth differs)' % (code, ', '.join(sorted(gs, key=GI.get))))
    for code in known:
        if code.startswith('D') and code not in owners:
            band = code.rsplit('.', 1)[-1]
            if band in BAND and any(grade_of.get(s) in BAND[band] for s in by_id):
                notes.append('%s named by no grade in band %s' % (code, band))
    # handoffs
    for sid, r in by_id.items():
        g = GI.get(grade_of[sid], -1)
        for a in split(r['assumes']):
            if a not in by_id:
                fails.append('%s assumes %s, which is not a skill here' % (sid, a))
                continue
            if GI.get(grade_of[a], 99) >= g:
                fails.append('%s (grade %s) assumes %s (grade %s): not an earlier grade' % (sid, grade_of[sid], a, grade_of[a]))
            if sid not in split(by_id[a]['hands_on']):
                fails.append('%s assumes %s, but %s does not hand on to it' % (sid, a, a))
        for h in split(r['hands_on']):
            if h not in by_id:
                fails.append('%s hands on to %s, which is not a skill here' % (sid, h))
                continue
            gh = GI.get(grade_of[h], -1)
            if gh <= g:
                fails.append('%s (grade %s) hands on to %s (grade %s): not a later grade' % (sid, grade_of[sid], h, grade_of[h]))
            if sid not in split(by_id[h]['assumes']):
                fails.append('%s hands on to %s, which does not assume it' % (sid, h))
            if gh > g + 1:
                notes.append('%s (grade %s) hands on to %s (grade %s): skips %d grade(s); say why in notes' % (
                    sid, grade_of[sid], h, grade_of[h], gh - g - 1))
    # models
    intro = {}
    for sid, r in by_id.items():
        g = GI.get(grade_of[sid], -1)
        ins, outs = set(split(r['model_in'])), set(split(r['model_out']))
        for m in outs - ins:
            intro.setdefault(m, set()).add(('intro', g))
        for m in outs & ins:
            intro.setdefault(m, set()).add(('carry', g))
    for sid, r in by_id.items():
        g = GI.get(grade_of[sid], -1)
        for m in split(r['model_in']):
            ok = any((k == 'carry' and gg < g) or (k == 'intro' and gg <= g) for k, gg in intro.get(m, ()))
            if not ok:
                fails.append('%s (grade %s) uses model %s, which no earlier grade hands on and no row of this grade introduces' % (
                    sid, grade_of[sid], m))
    # model continuity (Codex read 2026-11-13): grades between a model's first and last use where no row uses it
    used = {}
    for sid, r in by_id.items():
        for m in set(split(r['model_in'])) | set(split(r['model_out'])):
            used.setdefault(m, set()).add(GI.get(grade_of[sid], -1))
    for m, gs in sorted(used.items()):
        gaps = [GRADES[i] for i in range(min(gs), max(gs) + 1) if i not in gs]
        if gaps:
            notes.append('model %s unused in grade(s) %s between its first and last use (reactivate, or say why)' % (
                m, ', '.join(gaps)))
    # cross-subject
    def lean_timing(sid, x, ref, og):
        # a lean must be owned or taught (~ contribution counts) at or before the leaning row's grade
        g = GI.get(grade_of[sid], -1)
        if og is None or GI.get(og, -1) <= g:
            return
        nt = by_id[sid]['notes'] or ''
        if 'just in time:' in nt.lower() and ref in nt:
            notes.append('%s (grade %s) cross_subject %r: taught in grade %s, bridged by a just-in-time teach in notes' % (
                sid, grade_of[sid], x, og))
        else:
            fails.append('%s (grade %s) cross_subject %r: taught in grade %s, after this row (repoint to an earlier skill, '
                         'lower the demand, or add "Just in time: ..." naming %s in notes)' % (sid, grade_of[sid], x, og, ref))

    for sid, r in by_id.items():
        for x in split(r['cross_subject']):
            if ':' not in x:
                fails.append('%s cross_subject %r is not subject:code' % (sid, x))
                continue
            subj, ref = [s.strip() for s in x.split(':', 1)]
            ref = ref.split(' ')[0] if ref else ref
            if subj not in STD_FILES or subj == subject:
                fails.append('%s cross_subject %r names no other subject' % (sid, x))
                continue
            other = load(subj)
            other_ids = {o['skill_id'] for o in other} if other else set()
            other_codes = set()
            for f in STD_FILES[subj]:
                other_codes.update(codes(f))
            if ref in other_ids:
                lean_timing(sid, x, ref, other_grade(other, ref))
                continue
            if ref in other_codes:
                if other is not None:
                    named = set()
                    for o in other:
                        for c in split(o['standard']):
                            c = c.lstrip('~')
                            named.add(c)
                            if parent(c):
                                named.add(parent(c))
                    if ref not in named and parent(ref) not in named:
                        fails.append('%s cross_subject %r: no %s row names that code (point at the skill id or a code a row owns)' % (sid, x, subj))
                    else:
                        lean_timing(sid, x, ref, other_grade(other, ref))
                continue
            if other is None:
                notes.append('%s cross_subject %r: %s progression not written yet, check the id then' % (sid, x, subj))
            else:
                fails.append('%s cross_subject %r: not a %s standard code or skill id' % (sid, x, subj))
    counts = {}
    for sid in by_id:
        counts[grade_of[sid]] = counts.get(grade_of[sid], 0) + 1
    notes.append('rows by grade: ' + ', '.join('%s %d' % (g, counts[g]) for g in GRADES if g in counts))
    return fails, notes, len(rows)


def main(a):
    if not a or a[0] != 'check':
        raise SystemExit(__doc__)
    subjects = a[1:] or [s for s in STD_FILES if load(s) is not None]
    bad = 0
    for s in subjects:
        fails, notes, n = check(s)
        print('progression %s: %d rows, %d failure(s)' % (s, n, len(fails)))
        for x in fails:
            print('  FAIL', x)
        for x in notes:
            print('  note', x)
        bad += len(fails)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
