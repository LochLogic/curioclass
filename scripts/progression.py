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
Health (NHES) and physical education (SHAPE) indicators are span-coded (S1.5.2: span ending grade 5): owned by one
grade of the span, the grade where it is first fully met, and ~CODE in the span's other grades (added 2026-11-19);
a physical education span 12 indicator is owned only in grade 9 or 10.
The later subjects (added 2026-11-21): SEL ids are owned once in each of grades 2, 5, 8 and 12 and may be ~ in any
grade; an ELD id is owned by its cluster's last grade (K, 1, 3, 5, 8, 12) and ~ in the cluster's other grades, SI K-3
owned in 3 and SI 4-12 owned in 4 (~ in 5 to 12); library and career education ids carry no grade (one owner, any
grade). Computer science takes only the eight listed Specialty I ids, each in its own grade. A standards file id is
the whole first tab-separated field, spaces included.
Spanish (added 2026-11-22; world-languages STANDARD.md section 6) is level-keyed: the grade column holds L1 to L4,
skill ids start l1- to l4-, and every grade rule above (earlier, later, skipped, model handoffs) runs on level order.
A WRS id is owned at L1 and may be ~ at L2 to L4; a strand id (spanish-strands.txt) is owned once at any level; the
ACTFL.* level ids are listed in spanish-excluded.csv. A cross_subject lean is a teacher pointer, so it has no grade
test; a lean to a core skill of grade 6 or later is allowed only from an L3 or L4 row.
A (+) high school math part is covered only when named or excluded itself, not through its parent. A cross_subject
code must be named by a row of the other subject once that subject's progression exists (added 2026-11-13).
Lean timing (added 2026-11-13, cross-subject read finding 1): a cross_subject lean must be taught at or before the
leaning row's grade, meaning the named skill id's grade, or for a code the earliest grade of any row of the other
subject that owns it or ~ contributes to it (high school by course grade: 9 Biology and Algebra I, 10 Chemistry and
Geometry, 11 Physics and Algebra II). A forward lean FAILs unless the row's notes carry an explicit
"Just in time:" teach that names the same id or code; then it is a note.
Stale notes (added 2026-11-13): scripts/stale.py runs on every progression; see its docstring.
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
# level-keyed subjects (added 2026-11-22): a level list replaces the grade list (world-languages STANDARD.md 6)
LEVELS = ['L1', 'L2', 'L3', 'L4']
LI = {g: i for i, g in enumerate(LEVELS)}
LEVEL_KEYED = {'spanish'}
LATE_LEAN_LEVELS = ['L3', 'L4']  # the only levels that may lean to a core skill of grade 6 or later
# ccss-literacy-6-12.txt (RH, RST, WHST; added 2026-11-14) is accepted in ela, social studies and science rows. It is
# never an anchor, so no row is required to name its codes.
STD_FILES = {'social-studies': ['ma-hss-2018.txt', 'c3-indicators.txt', 'ccss-literacy-6-12.txt'],
             'math': ['ccss-math-standards.txt'],
             'ela': ['ccss-ela-standards.txt', 'ccss-ela-standards-full.txt', 'ccss-literacy-6-12.txt'],
             'science': ['ngss-pes.txt', 'ccss-literacy-6-12.txt'],
             # the later subjects (added 2026-11-19, health and PE pre-work): span-coded indicators, see code_grades
             'health': ['nhes-2024.txt', 'hecat-topics.txt'],
             'physical-education': ['shape-pe-2024.txt'],
             # computer science (added 2026-11-19, CS pre-work): Foundational ids anchor; S1 Specialty ids are accepted
             # but never required, and only in grades 11 and 12 (Cory, 2026-11-20); S2 ids fail (see code_grades)
             'computer-science': ['csta-2026-ids.txt', 'csta-2026-specialty-ids.txt'],
             # arts (added 2026-11-19, arts pre-work): NCAS performance standards, one file for the five disciplines
             'arts': ['ncas-performance-standards.txt'],
             # SEL, ELD, library and career education (added 2026-11-21; owner rules in code_grades)
             'sel': ['casel-5.txt'], 'eld': ['wida-2020.txt'], 'library': ['aasl-2018.txt'],
             'cte': ['cte-career-clusters-2024.txt'],
             # Spanish (added 2026-11-22): the World-Readiness ids plus our sounds and spelling strand
             'spanish': ['actfl-wrs.txt', 'spanish-strands.txt']}
# the core electives' own lists (added 2026-11-16): accepted codes, and every code in them must be owned by a row.
# Career education's learner goals (NCDG 2024) take the same route (career-education STANDARD.md, "What the gate needs")
ELECTIVE_FILES = {'math': ['curio-math-electives.txt'], 'science': ['curio-science-electives.txt'],
                  'social-studies': ['apa-hs-psych-2022.txt'], 'cte': ['ncdg-2024.txt']}
# files that may not be written yet: skipped with a note while absent
OPTIONAL_FILES = set()
for _s, _fs in ELECTIVE_FILES.items():
    STD_FILES[_s] = STD_FILES[_s] + _fs
ANCHOR = {'social-studies': 'ma-hss-2018.txt', 'science': 'ngss-pes.txt', 'ela': 'ccss-ela-standards.txt',
          'math': 'ccss-math-standards.txt', 'health': 'nhes-2024.txt', 'physical-education': 'shape-pe-2024.txt',
          'computer-science': 'csta-2026-ids.txt', 'arts': 'ncas-performance-standards.txt',
          'sel': 'casel-5.txt', 'eld': 'wida-2020.txt', 'library': 'aasl-2018.txt',
          'cte': 'cte-career-clusters-2024.txt',
          # two anchor files: every WRS and strand id owned; the ACTFL.* level ids sit in spanish-excluded.csv
          'spanish': ['actfl-wrs.txt', 'spanish-strands.txt']}
# subjects whose ids are owned once in each of several grades (SEL: once per band, at its last grade)
MULTI_OWNER = {'sel': ['2', '5', '8', '12']}
# computer science Specialty I: only these eight, each in its own grade (computer science STANDARD.md, Specialty)
CS_S1 = {'S1-AIN-DD-02': '11', 'S1-DSC-VZ-11': '11', 'S1-CYB-TS-08': '11', 'S1-SWD-TR-07': '11',
         'S1-AIN-HR-09': '12', 'S1-DSC-PP-13': '12', 'S1-SWD-PP-08': '12', 'S1-SWD-UX-05': '12'}
# ELD cluster -> (owner grade, cluster grades); SI uses K-3 and 4-12 (eld STANDARD.md, Ownership)
ELD_CLUSTER = {'K': ('K', ['K']), '1': ('1', ['1']), '2-3': ('3', ['2', '3']), '4-5': ('5', ['4', '5']),
               '6-8': ('8', ['6', '7', '8']), '9-12': ('12', ['9', '10', '11', '12'])}
ELD_SI = {'K-3': ('3', ['K', '1', '2', '3']), '4-12': ('4', ['4', '5', '6', '7', '8', '9', '10', '11', '12'])}
# anchor codes no row is asked to own: arts pre-K ids (no pre-K course; arts STANDARD.md section 3)
ANCHOR_SKIP = {'arts': re.compile(r'\.PK[a-z]?$')}  # media arts ids may carry no letter
LEVEL = {'I': '9', 'II': '10', 'III': '11'}
SPAN = {'2': ['K', '1', '2'], '5': ['3', '4', '5'], '8': ['6', '7', '8'], '12': ['9', '10', '11', '12']}


def _lit_codes():
    p = os.path.join(ROOT, 'data', 'standards', 'ccss-literacy-6-12.txt')
    if not os.path.exists(p):
        return set()
    return {l.split('	')[0].strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')}


LIT_CODES = _lit_codes()   # the lit: form of cross_subject (an also-met RH, RST or WHST code)


def code_grades(subject, code):
    """(owner grades, all grades) a grade-coded standard may sit in, or None when the code carries no grade.
    ELA: RL.4.2 sits in grade 4; a band code (RL.9-10.1) is used across the band and owned by its last grade."""
    if subject == 'math':
        g = code.split('.')[0]
        return ([g], [g]) if g in GI else None
    if subject in ('health', 'physical-education'):
        # NHES.S1.5.2 and SHAPE.S1.5.2: span end 5 = grades 3 to 5. Owned by one grade of the span (where it is
        # first fully met; the span's last grade is the deadline), ~ in the span's other grades (health and PE
        # STANDARD.md section 3, 2026-11-19)
        p = code.split('.')
        if len(p) == 4 and p[0] in ('NHES', 'SHAPE') and p[2] in SPAN:
            band = SPAN[p[2]]
            if subject == 'physical-education' and p[2] == '12':
                # grades 9 and 10 own every span 12 indicator; 11 and 12 carry them as ~ (PE STANDARD.md 3, rule 5)
                return ['9', '10'], band
            return band, band
        return None
    if subject == 'spanish':
        # WRS.Communication.1.1: owned at L1 (met at Novice depth), ~ at L2 to L4; SPA.Sounds.3: owned once at any
        # level (world-languages STANDARD.md section 6)
        if code.startswith('WRS.'):
            return ['L1'], LEVELS
        if code.startswith('SPA.'):
            return LEVELS, LEVELS
        return None
    if subject == 'sel':
        # CASEL.Self-Awareness.3: owned once per band at its last grade, ~ in any grade (sel STANDARD.md, Ownership)
        return (MULTI_OWNER['sel'], GRADES) if code.startswith('CASEL.') else None
    if subject == 'eld':
        # WIDA.ELD-LA.2-3.Inform.Expressive: owned by the cluster's last grade, ~ in its other grades
        p = code.split('.')
        if len(p) < 4 or p[0] != 'WIDA':
            return None
        own, band = (ELD_SI if p[1] == 'ELD-SI' else ELD_CLUSTER).get(p[2], (None, None))
        return ([own], band) if own else None
    if subject == 'computer-science':
        # E3-ALG-IM-03: EK = K, E1 to E5 = own grade; MS and HS ids are owned by one grade of the band and may be
        # ~ in its other grades (computer science STANDARD.md, 2026-11-19)
        b = code.split('-')[0]
        if b == 'EK':
            return ['K'], ['K']
        if len(b) == 2 and b[0] == 'E' and b[1] in '12345':
            return [b[1]], [b[1]]
        if b == 'S1':
            if code not in CS_S1:
                return [], []  # not on the eight-id list: any use fails (see check)
            return [CS_S1[code]], ['11', '12']
        if b == 'S2':
            return [], []  # S2 is out of the course list: any use fails (see check)
        if b in ('MS', 'HS'):
            band = BAND['6-8' if b == 'MS' else '9-12']
            return band, band
        return None
    if subject == 'arts':
        # VA:Cr2.3.4a sits in grade 4 (Ka in K). High school levels (arts STANDARD.md 3.2): Level 1 = grade 9 (.Ia),
        # Level 2 = 10 (.IIa), Level 3 = 11 (.IIIa); grade 12 is the optional Level 4 and may only contribute (~)
        m = re.match(r'^(?:VA|MU|TH|DA|MA):[A-Za-z]+\d+\.\d+\.(?:C\.)?(K|[1-8]|I|II|III)[a-z]?$', code)
        if not m:
            return None
        g = m.group(1)
        if g in LEVEL:
            return [LEVEL[g]], [LEVEL[g]] + (['12'] if g == 'III' else [])
        return [g], [g]
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
        out.append(line.split('\t')[0].strip())  # the whole first field: SEL and CTE ids hold spaces
    return out


def std_codes(subject, missing=None):
    """Every code in a subject's standards files; an absent optional file is skipped (and listed in missing)."""
    out = set()
    for f in STD_FILES.get(subject, []):
        if f in OPTIONAL_FILES and not os.path.exists(os.path.join(ROOT, 'data', 'standards', f)):
            if missing is not None:
                missing.append(f)
            continue
        out.update(codes(f))
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
    lvl = subject in LEVEL_KEYED
    G, OI, unit = (LEVELS, LI, 'level') if lvl else (GRADES, GI, 'grade')
    absent = []
    known = std_codes(subject, absent)
    for f in absent:
        notes.append('data/standards/%s not written yet: its codes are not checked' % f)
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
        if g not in OI:
            fails.append(where + (': level %r not L1 to L4' % g if lvl else ': grade %r not K or 1 to 12' % g))
        elif lvl and not sid.startswith(g.lower() + '-'):
            fails.append(where + ': a level %s skill id starts with %s-' % (g, g.lower()))
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
            if not allowed:
                if raw.lstrip('~').startswith('S1-'):
                    fails.append('%s names %s: not one of the eight listed Specialty I ids (computer science '
                                 'STANDARD.md, Specialty standards)' % (sid, raw.lstrip('~')))
                else:
                    fails.append('%s names %s: Specialty II ids are not taught (Cory, 2026-11-20)' % (sid, raw.lstrip('~')))
                continue
            if grade_of[sid] not in allowed:
                fails.append('%s (%s %s) %s %s: belongs in %s(s) %s' % (
                    sid, unit, grade_of[sid], 'contributes to' if raw.startswith('~') else 'owns', raw.lstrip('~'), unit,
                    ', '.join(allowed)))
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
        afiles = ANCHOR[subject] if isinstance(ANCHOR[subject], list) else [ANCHOR[subject]]
        anchor = [c for f in afiles for c in codes(f)]
        plus_codes = set()
        for f in afiles:
            for line in open(os.path.join(ROOT, 'data', 'standards', f), encoding='utf-8'):
                if not line.startswith('#') and '(+)' in line:
                    plus_codes.add(line.split('	')[0].strip())
        kids = {}
        for code in anchor:
            if parent(code):
                kids.setdefault(parent(code), []).append(code)
        for code in anchor:
            if HEADING.match(code) or (subject in ANCHOR_SKIP and ANCHOR_SKIP[subject].search(code)):
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
            if subject in MULTI_OWNER:
                continue  # checked below: once in each owner grade
            if (code.startswith('MA.') or subject != 'social-studies') and len(gs) > 1:
                fails.append('%s owned by %ss %s' % (code, unit, ', '.join(sorted(gs, key=OI.get))))
        if subject in MULTI_OWNER:
            want = MULTI_OWNER[subject]
            per = {}
            for sid, r in by_id.items():
                for code in split(r['standard']):
                    if not code.startswith('~'):
                        per.setdefault((code, grade_of[sid]), []).append(sid)
            for (code, g), sids in sorted(per.items()):
                if len(sids) > 1:
                    fails.append('%s owned twice in grade %s (%s)' % (code, g, ', '.join(sids)))
            for code in anchor:
                if code in excl or code not in owners:
                    continue  # excluded, or already failed as named by no skill
                gap = [g for g in want if g not in owners[code]]
                if gap:
                    fails.append('%s not owned in grade(s) %s (owned once in each of grades %s)' % (
                        code, ', '.join(gap), ', '.join(want)))
    for f in ELECTIVE_FILES.get(subject, []):
        if os.path.exists(os.path.join(ROOT, 'data', 'standards', f)):
            for code in codes(f):
                if code not in owners:
                    fails.append('%s (%s) named by no skill' % (code, f))
    # quieter notes (baseline 1 structure finding 7): a note stays only while the rows have not said why
    def said(sids, *words):
        nt = ' '.join((by_id[x].get('notes') or '') for x in sids if x in by_id).lower()
        return any(w.lower() in nt for w in words if w)
    namers = {}
    for sid, r in by_id.items():
        for c in split(r.get('standard') or ''):
            namers.setdefault(c.lstrip('~'), []).append(sid)
    for code, gs in owners.items():
        later = [x for x in namers.get(code, []) if grade_of[x] != min(gs, key=OI.get)]
        if code.startswith('D') and len(gs) > 1 and not said(later, code):
            notes.append('%s named in grades %s (say in notes how the depth differs)' % (code, ', '.join(sorted(gs, key=OI.get))))
    for code in known:
        if code.startswith('D') and code not in owners:
            band = code.rsplit('.', 1)[-1]
            if band in BAND and any(grade_of.get(s) in BAND[band] for s in by_id):
                notes.append('%s named by no grade in band %s' % (code, band))
    # handoffs
    for sid, r in by_id.items():
        g = OI.get(grade_of[sid], -1)
        for a in split(r['assumes']):
            if a not in by_id:
                fails.append('%s assumes %s, which is not a skill here' % (sid, a))
                continue
            if OI.get(grade_of[a], 99) >= g:
                fails.append('%s (%s %s) assumes %s (%s %s): not an earlier %s' % (sid, unit, grade_of[sid], a, unit, grade_of[a], unit))
            if sid not in split(by_id[a]['hands_on']):
                fails.append('%s assumes %s, but %s does not hand on to it' % (sid, a, a))
        for h in split(r['hands_on']):
            if h not in by_id:
                fails.append('%s hands on to %s, which is not a skill here' % (sid, h))
                continue
            gh = OI.get(grade_of[h], -1)
            if gh <= g:
                fails.append('%s (%s %s) hands on to %s (%s %s): not a later %s' % (sid, unit, grade_of[sid], h, unit, grade_of[h], unit))
            if sid not in split(by_id[h]['assumes']):
                fails.append('%s hands on to %s, which does not assume it' % (sid, h))
            if gh > g + 1 and not said([sid, h], h, sid, 'skip', 'idle', 'dormant', 'returns'):
                notes.append('%s (%s %s) hands on to %s (%s %s): skips %d %s(s); say why in notes' % (
                    sid, unit, grade_of[sid], h, unit, grade_of[h], gh - g - 1, unit))
    # models
    intro = {}
    for sid, r in by_id.items():
        g = OI.get(grade_of[sid], -1)
        ins, outs = set(split(r['model_in'])), set(split(r['model_out']))
        for m in outs - ins:
            intro.setdefault(m, set()).add(('intro', g))
        for m in outs & ins:
            intro.setdefault(m, set()).add(('carry', g))
    for sid, r in by_id.items():
        g = OI.get(grade_of[sid], -1)
        for m in split(r['model_in']):
            ok = any((k == 'carry' and gg < g) or (k == 'intro' and gg <= g) for k, gg in intro.get(m, ()))
            if not ok:
                fails.append('%s (%s %s) uses model %s, which no earlier %s hands on and no row of this %s introduces' % (
                    sid, unit, grade_of[sid], m, unit, unit))
    # model continuity (Codex read 2026-11-13): grades between a model's first and last use where no row uses it
    used = {}
    for sid, r in by_id.items():
        for m in set(split(r['model_in'])) | set(split(r['model_out'])):
            used.setdefault(m, set()).add(OI.get(grade_of[sid], -1))
    for m, gs in sorted(used.items()):
        gaps = [G[i] for i in range(min(gs), max(gs) + 1) if i not in gs]
        users = [x for x, r in by_id.items() if m in set(split(r['model_in'])) | set(split(r['model_out']))]
        why = any(m in (by_id[x].get('notes') or '') and said([x], 'skip', 'idle', 'dormant', 'return', 'unused', 'not used',
                                                               'paused', 'rest', 'again', 'reactivat') for x in users)
        if gaps and not why:
            notes.append('model %s unused in %s(s) %s between its first and last use (reactivate, or say why)' % (
                m, unit, ', '.join(gaps)))
    # cross-subject
    def lean_timing(sid, x, ref, og):
        if lvl:
            # a level row's lean is a teacher pointer, not an assumption: no grade test, except that a lean to a core
            # skill of grade 6 or later is allowed only from L3 or L4 (world-languages STANDARD.md 6, Cross-subject leans)
            if og is not None and GI.get(og, -1) >= GI['6'] and grade_of[sid] not in LATE_LEAN_LEVELS:
                fails.append('%s (level %s) cross_subject %r: taught in grade %s; a lean to grade 6 or later is allowed '
                             'only from %s rows' % (sid, grade_of[sid], x, og, ' or '.join(LATE_LEAN_LEVELS)))
            return
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
            full = ref
            ref = ref.split(' ')[0] if ref else ref
            if subj == 'lit':
                # an also-met literacy standard (RH, RST, WHST: data/standards/ccss-literacy-6-12.txt), cited without an
                # ELA row; science and social studies teach it in their own rows (added 2026-11-14). Notes only.
                if subject == 'ela':
                    notes.append('%s cross_subject %r: ELA owns its literacy codes; name them in standard instead' % (sid, x))
                elif ref not in LIT_CODES:
                    notes.append('%s cross_subject %r: not a code in ccss-literacy-6-12.txt' % (sid, x))
                else:
                    band = re.search(r'\.(\d+)-(\d+)\.', ref)
                    g = GI.get(grade_of[sid], -1) - GI.get('K', 0)
                    if band and not int(band.group(1)) <= g <= int(band.group(2)):
                        notes.append('%s (grade %s) cross_subject %r: outside the grade band of the code' % (sid, grade_of[sid], x))
                continue
            if subj not in STD_FILES or subj == subject:
                fails.append('%s cross_subject %r names no other subject' % (sid, x))
                continue
            other = load(subj)
            other_ids = {o['skill_id'] for o in other} if other else set()
            other_codes = std_codes(subj)
            if full in other_codes:
                ref = full  # an id holding spaces (CASEL.Social Awareness.1, CTE.Career Clusters.Construction)
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
    import stale  # stale-note catch: Pending(...) markers that have landed, unmarked work-status wording
    fails += stale.check_file(os.path.join(ROOT, 'data', 'progressions', subject + '.csv'))
    counts = {}
    for sid in by_id:
        counts[grade_of[sid]] = counts.get(grade_of[sid], 0) + 1
    notes.append('rows by %s: ' % unit + ', '.join('%s %d' % (g, counts[g]) for g in G if g in counts))
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
