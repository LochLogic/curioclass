r"""Section run: section plans unit by unit, two courses at a time (one lane per subject). Spec: docs/pipeline/SECTION-RUN.md.

    python -X utf8 scripts/section_run.py dry-run <subject> [<units>]   every stage's prompt and command, no model calls
    python -X utf8 scripts/section_run.py run <subject>                 run the lane until a stop (resumes where it stopped)
    python -X utf8 scripts/section_run.py status                        per lane: last line, any STOPPED reason, tokens

Per unit: texts (ELA), prep (Codex GPT-6.2 Astra xhigh), write (Codex GPT-6.2 Sol high), refine (Claude Opus 5.5 high,
its report ends with "Changed for the next unit"), second texts pass (ELA), plan data (Codex Sol high), narrow key read
(Claude Opus 5.5 high on a packet the script cuts). The next unit's prep runs beside the current unit's refine, data
and key; every other stage runs one at a time per course. Any stop writes build/sections/<subject>/STOPPED with the
reason; a stage is marked done only after its commit, and unit state is also read from the files, so a rerun resumes.
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys
import threading
import time
import traceback
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import codex_lane as cl  # noqa: E402
import coursegen as cg  # noqa: E402

RUN = ROOT / 'build' / 'sections'
PREP = RUN / 'prep'
PACKETS = RUN / 'packets'
COURSES = {
    'ela': ['english-language-arts-grade-%d' % g for g in range(4, 13)],
    # math-grade-4 is in (Cory 2026-11-26); the old math-4 pilot paths stay untouched (later.csv L13).
    'math': ['math-grade-%d' % g for g in range(1, 9)] + ['algebra-i', 'geometry', 'algebra-ii', 'precalculus',
                                                          'statistics', 'calculus'],
}
MODELS = {   # stage: (runner, model, effort); Cory 2026-11-26
    'texts': ('codex', 'gpt-6.2-sol', 'high'),
    'prep': ('codex', 'gpt-6.2-astra', 'xhigh'),
    'write': ('codex', 'gpt-6.2-sol', 'high'),
    'refine': ('claude', 'claude-opus-5-5', 'high'),
    'texts2': ('codex', 'gpt-6.2-sol', 'high'),
    'data': ('codex', 'gpt-6.2-sol', 'high'),
    'key': ('claude', 'claude-opus-5-5', 'high'),
}
KEY_SKIP = {'practice', 'example', 'fix', 'challenge'}
OPEN_TEXT = ('to write', 'to choose', 'to confirm', 'to decide')
CLAUDE_TOOLS = ','.join(['Read', 'Edit', 'Write', 'Glob', 'Grep', 'Bash(python:*)', 'Bash(python -X utf8:*)',
                         'Bash(cd:*)', 'Bash(ls:*)', 'Bash(head:*)', 'Bash(wc:*)', 'Bash(grep:*)', 'Bash(cat:*)', 'Bash(mkdir:*)'])
CLAUDE_TIMEOUT = 3 * 3600
LIMIT_WORDS = cl.LIMIT_WORDS + ('hit your limit', 'limit reached', 'reached your', 'usage cap', 'out of credits',
                                'credit balance')
NEVER = ('Never open .claude/, docs/Return/, Gemini/, Gemini.*, data/closet/words/, closet/words/, '
         'data/media-manifest.txt, data/docs-manifest.txt, any path containing math-4 or ela-6. No git commands at all. '
         'No em dashes, US spelling, "Curio Class" in full.')


class Stop(Exception):
    """A lane stop with its reason (SECTION-RUN.md "Stops")."""


def now():
    return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def today():
    return dt.date.today().isoformat()


# ---------------------------------------------------------------- course and unit state, read from the files

class Unit:
    def __init__(self, course, u, secs):
        self.course, self.u, self.uu = course, u, '%02d' % u
        self.secs = secs                                     # [('2.1', [days]), ...]
        self.names = [cg.sname(self.uu, s) for s, _ in secs]  # ['u02-1', ...]
        self.days = [d for _, ds in secs for d in ds]
        self.ela = course.startswith('english-language-arts')
        self.key = '%s:u%s' % (course, self.uu)

    def __repr__(self):
        return self.key

    def plan(self, name):
        return ROOT / 'docs' / 'courses' / self.course / ('%s.md' % name)

    def missing_plans(self):
        return [n for n in self.names if not self.plan(n).exists()]

    def has_items(self):
        p = ROOT / 'data' / 'plans' / self.course / 'items.csv'
        if not p.exists():
            return False
        with open(p, encoding='utf-8', newline='') as f:
            return any(r.get('stretch') == str(self.u) for r in csv.DictReader(f))

    def key_report(self):
        return sorted(glob.glob(str(ROOT / 'docs' / 'reviews' / self.course / ('answer-key-%s-u%s-*.md' % (
            self.course, self.uu)))))

    def green(self):
        return not self.missing_plans() and self.has_items() and bool(self.key_report())

    def open_texts(self):
        if not self.ela:
            return []
        with open(ROOT / 'data' / 'plans' / 'ela-texts.csv', encoding='utf-8', newline='') as f:
            return [r['text_id'] for r in csv.DictReader(f) if r['course'] == self.course and r['unit'] == str(self.u)
                    and r['status'].split(':')[0].strip() in OPEN_TEXT]

    def refine_report(self):
        """Dated when first asked, then fixed, so a refine that runs past midnight is still found."""
        if not getattr(self, '_rr', None):
            old = self.refine_reports()
            self._rr = Path(old[-1]) if old and not tracked(old[-1]) else \
                ROOT / 'docs' / 'reviews' / self.course / ('section-refine-%s-u%s-%s.md' % (self.course, self.uu, today()))
        return self._rr

    def key_path(self):
        if not getattr(self, '_kp', None):
            left = [k for k in self.key_report() if not tracked(k)]
            self._kp = Path(left[-1]) if left else \
                ROOT / 'docs' / 'reviews' / self.course / ('answer-key-%s-u%s-%s.md' % (self.course, self.uu, today()))
        return self._kp

    def refine_reports(self):
        return sorted(glob.glob(str(ROOT / 'docs' / 'reviews' / self.course / ('section-refine-%s-u%s-*.md' % (
            self.course, self.uu)))))


def tracked(path):
    """True when git tracks the file (a committed report), so an uncommitted one left by a stop is not taken as done."""
    rel = Path(path).resolve().relative_to(ROOT).as_posix()
    return cl.git('ls-files', '--error-unmatch', '--', rel)[0] == 0


def course_units(course):
    """[Unit] for the course, or raise Stop with the missing inputs."""
    miss, data = cg.missing_inputs(course, 'ela' if course.startswith('english') else 'math')
    if miss:
        raise Stop('%s is missing inputs: %s' % (course, '; '.join(miss)))
    rows, secs = data
    return [Unit(course, u, secs[u]) for u in sorted(secs)]


def changed_list(unit_before):
    """The newest "Changed for the next unit" report path of the unit before, or None."""
    if unit_before is None:
        return None
    reps = unit_before.refine_reports()
    return reps[-1] if reps else None


# ---------------------------------------------------------------- prompts

def kit_job(lane, unit, kind, template, extra, detail):
    """Render a kit template through coursegen's Queue (same tokens and notes as the course run)."""
    out = RUN / lane.subj / 'jobs-kit'
    q = cg.Queue(out, lane.subj, cg.kit_version(), today())
    q.n = int(time.time()) % 100000          # unique job number per render
    name = q.job(kind, unit.course, detail, template, extra)
    text = (out / name).read_text(encoding='utf-8')
    if unit.course in cl.DRAFTED and kind.upper() in cl.MAKE_KINDS:
        text += cl.REVISE.format(course=unit.course)
    return text


def texts_prompt(lane, unit, second=False):
    return kit_job(lane, unit, 'text2' if second else 'text', 'text2' if second else 'text',
                   {'UNIT': str(unit.u), 'UU': unit.uu}, 'u%d' % unit.u)


def prep_prompt(unit, changed):
    notes = ', '.join('build/sections/prep/%s/%s.md' % (unit.course, n) for n in unit.names)
    approach = 'docs/APPROACH-%s.md' % ('ELA' if unit.ela else 'MATH')
    ch = ('The refine of an earlier unit listed what later units must also do: read the heading "Changed for the next '
          'unit" at the end of %s and carry every line into your notes.' % changed) if changed else \
        'No earlier unit of this run has a refine report yet.'
    return """You are the prep pass of the section run in the Curio Class repository, S:\\CurioClass (Windows; Bash with POSIX paths like /s/CurioClass, `python -X utf8`). Read AGENTS.md first.

The run (docs/pipeline/SECTION-RUN.md): for each unit, you write short prep notes, a writer then writes the section plans from them, and a refine pass brings them to the bar. Your notes carry the judgment the writer most often gets wrong: solved exits and keys, error letters, part minutes, turn counting, continuity with earlier units and grades, and new cases that never reuse a taught one.

Course {course}, unit {u}, sections {names}. First rebuild the skeletons: `python -X utf8 scripts/section_skeleton.py {course} u{u}` (ignored working files: never edit one). Then read, filtered to what you need:
- docs/pipeline/briefs/section-write.md and docs/pipeline/kit/section.txt (the job form the writer gets)
- docs/courses/UNIT-PLAN.md: "The rules", "The section plan: fields, in order", "Length"
- docs/courses/{course}/s{uu}.md whole, DEFAULTS.md, and frame.md only this unit's row, notes and Sensitive topics lines
- {approach}
- the skeletons docs/courses/{course}/section-skeletons/u{uu}-<n>.md
- the ledger, filtered only: `python -X utf8 scripts/ledger.py show {subj} --before {course} --term "<word>"` per term your sections touch; `--course {course} --kind term` (and `--kind routine`, `--kind case`) for this course's earlier units
- this course's section plan just before your first section, if it exists, and at most one lower-grade section plan{ela}
{changed}

Write one prep note per section: {notes}. Each note at most 1,100 words, dense shorthand under these heads:
- Title and the section's share of each code (verb quoted, limits that bite).
- Exits: for each teaching day, the exit question in full, solved, its key, two or three wrong answers each with one error letter from s{uu}'s register, and a "Shape:" line (what practice, model or card the day must avoid). Every number and key solved cold. Exits are new cases, never the worked example with new numbers.
- Check items this section owns (by unit plan number) with keys.
- Error letters met, each with a wrong example beside a right one, the day shown, the if-many repair minutes and where they land.
- Days: for each day, the part lines with minutes adding to DEFAULTS' day length (`- **N min. Part.**`), the worked cases, the model or manipulative with its no-kit stand-in, who is heard (turn counting for about 30 children), the hand-back slot.
- Continuity: terms, routines, characters and cases to reuse by name (in the ledger's words), what is review not new, and "planned only" for anything at stage planned.
- Talk and writing questions; practice that returns; supports (English learner words and one frame); two rooms; not in this section.
- Fallbacks for any hinge; "source to check" for any real-world fact without a source.
Do not write the plan prose; the writer does.

Write ONLY those note files (create the folder). Edit nothing else: no docs/, data/, courses/, no ledger writes. {never} Helper scripts only in S:/CurioClass/_scratch/sections/{course}-u{uu}-prep/.

Final message under 200 words: the files with word counts, decisions the writer should check first, and any fault you saw in the unit plan or skeletons.""".format(
        course=unit.course, u=unit.u, uu=unit.uu, names=', '.join(unit.names), approach=approach, notes=notes,
        subj='ela' if unit.ela else 'math', changed=ch, never=NEVER,
        ela=('\n- for each text your sections read: its row in data/plans/ela-texts.csv (filtered) and its file in '
             'courses/%s/texts/' % unit.course) if unit.ela else '')


def write_prompts(lane, unit, changed):
    """The kit section job(s) for the unit's missing plans, with the prep notes and the last Changed list added."""
    todo = set(unit.missing_plans())
    groups = [g for g in cg.halves(unit.secs) if any(cg.sname(unit.uu, s) in todo for s, _ in g)]
    out = []
    for i, g in enumerate(groups):
        names = [cg.sname(unit.uu, s) for s, _ in g if cg.sname(unit.uu, s) in todo]
        text = kit_job(lane, unit, 'sec', 'section', {'UNIT': str(unit.u), 'UU': unit.uu, 'SECTIONS': ', '.join(names)},
                       'u%d%s' % (unit.u, 'ab'[i] if len(groups) > 1 else ''))
        text += ('\n\nNote from the section run (it wins over the job above where they differ):\n'
                 '- Prep notes for your sections are in %s. Follow them: they hold solved exits, keys, error letters, part '
                 'minutes and continuity. Where a note breaks a rule, the unit plan or the skeleton, the rule wins; '
                 'list it under Plan points.\n' % ', '.join('build/sections/prep/%s/%s.md' % (unit.course, n) for n in names))
        if changed:
            text += ('- The refine of the previous unit listed what later units must also do: read the heading "Changed '
                     'for the next unit" at the end of %s and apply every line.\n' % changed)
        written = [n for n in unit.names if n not in todo]
        if written:
            text += '- These sections of the unit are already written; leave them as they are: %s.\n' % ', '.join(written)
        out.append((names, text))
    return out


def refine_prompt(unit):
    subj = 'ela' if unit.ela else 'math'
    approach = 'docs/APPROACH-%s.md' % ('ELA' if unit.ela else 'MATH')
    rep = unit.refine_report().relative_to(ROOT).as_posix()
    plans = ', '.join('docs/courses/%s/%s.md' % (unit.course, n) for n in unit.names)
    return """You are the refine pass of the section run in the Curio Class repository, S:\\CurioClass (Windows; Bash with POSIX paths like /s/CurioClass, `python -X utf8`). Read AGENTS.md first.

The section plans of {course} unit {u} were just written from prep notes: {plans}. Bring them to the section plan bar so the plan data job and the answer-key read can run next. The gates already pass or list their lines; judge what a gate cannot.

1. Re-check cold: every exit, key, worked case and listed wrong answer solved; each wrong answer with exactly one error letter from s{uu}'s register; rule 4 (no taught case, number, picture or text passage in an exit or check, across section edges and earlier units); one ask per stem; "Shape:" lines; each day gives its goal in student words and its kind; part minutes per DEFAULTS.md; turn counting for about 30 children with a hand-back for those not heard; terms and notation taught before tested; owed codes, days and assessment items from the unit plan and skeletons; the 1,600-word cap outside fields 3, 4 and 6; plain words a teacher can use.
2. Fix every real fault in the plans in place. Keep what meets the bar; do not rewrite for taste.
3. Check the ledger rows the writer added for these sections (`python -X utf8 scripts/ledger.py show {subj} --course {course} --term "<word>"`, filtered, never the whole ledger) and add or fix rows as docs/pipeline/briefs/section-write.md says ("In a course run": one `python -X utf8 scripts/ledger.py add` call each, day blank; "planned only" where a lower-grade row is still at stage planned).

The rules: docs/pipeline/briefs/section-write.md, docs/courses/UNIT-PLAN.md ("The rules", "The section plan: fields, in order", "Length"), docs/courses/{course}/DEFAULTS.md, {approach}, the unit plan docs/courses/{course}/s{uu}.md and the skeletons docs/courses/{course}/section-skeletons/u{uu}-<n>.md (rebuild them first with `python -X utf8 scripts/section_skeleton.py {course} u{u}`; never edit one). The prep notes build/sections/prep/{course}/u{uu}-<n>.md say what the writer was told.

Write the report {rep}: a table of faults (file, fault, fix or rejected with why, the stage that made it: unit plan, prep, write), then plan points (faults in the unit plan or data you may not edit), then last the heading "## Changed for the next unit": a short list of what later units must also do (a routine or term fixed, a fault class the writer kept making, a case now used up). Write "None." under it if nothing carries.

Edit only {plans}, the ledger through scripts/ledger.py, and the report. Never edit s{uu}.md, days.csv or other data; list such faults under plan points. Gates: `python -X utf8 scripts/unitplan.py check {course}` passes these files; `python -X utf8 scripts/ledger.py check {subj}` reports 0 problems; `python -X utf8 scripts/gate.py --course {course}` shows no new FAIL your edits made; no em dash and no TODO(writer). Other writers work in other courses at the same time: never touch their files. {never} Helper scripts only in S:/CurioClass/_scratch/sections/{course}-u{uu}-refine/.

Final message under 200 words: faults fixed and rejected, ledger rows added or fixed, gate results, plan points, and the Changed list.""".format(
        course=unit.course, u=unit.u, uu=unit.uu, plans=plans, subj=subj, approach=approach, rep=rep, never=NEVER)


def data_prompts(lane, unit):
    hs = cg.halves(unit.secs) if unit.ela else [unit.secs]
    out = []
    for i, grp in enumerate(hs):
        ds = [d for _, x in grp for d in x]
        names = ', '.join(cg.sname(unit.uu, s) for s, _ in grp)
        if len(hs) == 1:
            ul = 'You also write the unit-level rows (error register, readiness and end-of-unit items, family note).'
            end = 'the end-of-unit items'
        elif i == 0:
            ul = ("This unit is split in two data jobs; you are the first: you also write the unit-level rows (the whole "
                  "unit's error register, readiness items, every end-of-unit item and the family note), so the second "
                  "job (sections %s) only adds its sections' rows." % ', '.join(cg.sname(unit.uu, s) for s, _ in hs[1]))
            end = 'every end-of-unit item of the whole unit'
        else:
            ul = ("This unit is split in two data jobs; you are the second: the first job wrote the unit-level rows "
                  "(error register, readiness, end items, family note); read them, add only your sections' rows, and "
                  "reuse its error letters (add a letter only if your sections need a new one, after the last).")
            end = 'no end items (the first job wrote them)'
        text = kit_job(lane, unit, 'data', 'data', {'UNIT': str(unit.u), 'UU': unit.uu, 'SECTIONS': names,
                                                     'FIRST': str(min(ds)), 'LAST': str(max(ds)), 'UNITLEVEL': ul,
                                                     'ENDITEMS': end}, 'u%d%s' % (unit.u, 'ab'[i] if len(hs) > 1 else ''))
        if unit.has_items():
            text += ('\n\nNote from the section run (it wins over the job above): data/plans/%s/ already holds rows for '
                     'this unit (an earlier draft or run). Update them in place by their full ids; never add a second row '
                     'for an id or a case that is already there.\n' % unit.course)
        if unit.ela:
            text += ('\n\nNote from the section run (it wins over the job above): every source-map.csv row of these days '
                     'with an order_conflict needs harms_learning set to yes, no or unclear, decided by you from the unit '
                     'plan and the days, with the reason in `why`; list every "unclear" in your last message (the lead '
                     'takes those to the Desk).\n')
        out.append(('%s' % ('ab'[i] if len(hs) > 1 else ''), text))
    return out


def key_packet(unit):
    """The narrow key read's packet (SECTION-RUN.md): the unit's item rows and what the key read needs, nothing more."""
    d = ROOT / 'data' / 'plans' / unit.course

    def rows(name, keep):
        p = d / name
        if not p.exists():
            return [], []
        with open(p, encoding='utf-8', newline='') as f:
            rd = csv.DictReader(f)
            return rd.fieldnames, [r for r in rd if keep(r)]

    # the key read owes the judged items (exit, readiness, end), not practice, worked examples or fix items
    icols, items = rows('items.csv', lambda r: r.get('stretch') == str(unit.u) and r.get('check') not in KEY_SKIP)
    ids = {r['item_id'] for r in items}
    wcols, wrongs = rows('wrongs.csv', lambda r: r.get('item_id') in ids)
    ecols, errs = rows('errors.csv', lambda r: r.get('stretch') == str(unit.u))

    def table(cols, rs):
        if not rs:
            return '(none)\n'
        import io
        b = io.StringIO()
        w = csv.DictWriter(b, cols, lineterminator='\n')
        w.writeheader()
        w.writerows(rs)
        return '```csv\n' + b.getvalue() + '```\n'

    parts = ['# Key packet: %s unit %d (days %d to %d), cut %s by scripts/section_run.py\n' % (
        unit.course, unit.u, min(unit.days), max(unit.days), now()),
        '## items.csv rows (%d)\n' % len(items), table(icols, items),
        '## wrongs.csv rows of these items (%d)\n' % len(wrongs), table(wcols, wrongs),
        '## errors.csv register of the unit (%d)\n' % len(errs), table(ecols, errs),
        '## Field 3 exit lines of each section plan\n']
    for n in unit.names:
        p = unit.plan(n)
        text = p.read_text(encoding='utf-8') if p.exists() else ''
        m = re.search(r'^## 3\..*?(?=^## 4\.)', text, re.S | re.M)
        parts.append('### %s\n\n%s\n' % (n, (m.group(0).strip() if m else '(no field 3 found)')))
    parts.append('## Shared pieces of the unit (open one only for an item that needs it)\n')
    for p in sorted((ROOT / 'courses' / unit.course).glob('u%s-*/*' % unit.uu)):
        if p.is_file():
            parts.append('- %s (%d words)\n' % (p.relative_to(ROOT).as_posix(), len(p.read_text(encoding='utf-8',
                                                                                              errors='replace').split())))
    if unit.ela:
        parts.append('\n## Texts of the items\n')
        for t in sorted({r.get('text_id', '') for r in items if r.get('text_id')}):
            parts.append('- %s: courses/%s/texts/%s.md\n' % (t, unit.course, t))
    PACKETS.mkdir(parents=True, exist_ok=True)
    out = PACKETS / ('%s-u%s.md' % (unit.course, unit.uu))
    out.write_text('\n'.join(parts), encoding='utf-8')
    return out, len(items)


def key_prompt(unit, packet):
    subj = 'ela' if unit.ela else 'math'
    rep = unit.key_path().relative_to(ROOT).as_posix()
    return """You work in S:\\CurioClass (a free K-12 lessons site; Windows, Bash with POSIX paths like /s/CurioClass, `python -X utf8`). Read AGENTS.md first. You are a fresh reader: you did not write this data.

Job: the narrow answer-key read of {course} unit {u} (days {first} to {last}). Your packet is {packet}: the unit's items.csv rows, their wrongs.csv rows, the unit's error register, each section plan's field 3 exit lines, the list of shared pieces and (ELA) the text of each item. Work from the packet. Open a shared piece, a text or a day block only for an item that needs it; never re-read whole section plans or the unit plan. Read docs/pipeline/briefs/sensitivity-read.md sections 1 and 2 for kind `answer-key` (this job, not its section 3, says where the report goes and what you may edit).

1. Solve every item cold from its stem (and its text or picture), writing your own answer and method, before you look at its answer, samples or look-fors. If a piece prints keys, do not open it before you have solved.
2. Compare. Each mismatch is the key's error, an ambiguous item (two right answers, an answer given away by the stem, caption or picture, passable by elimination, needing a fact or number the child is not given), an item that does not test its day's goal, a two-part question (split it into two items, each with its own key, wrongs row, handbacks row and print line), a stem over the grade's length limit, or your error (say so).
3. Rule 4: no item reuses a case, picture or numbers shown in a shared piece of the unit or a lower grade (`python -X utf8 scripts/ledger.py show {subj} --before {course} --term "<word>"`, filtered, never the whole ledger).
4. Field 3 sync: items.csv is the truth; list each field 3 exit line in the packet that no longer matches its item, and fix that line in the section plan.
5. Facts: each fact an item rests on traces to a sources.csv row; say which you checked. A key printed on a piece children hold moves to a teacher key piece.
6. Fix every real fault now: items.csv and wrongs.csv rows of this unit (Python csv module, full ids, read the whole file before writing), any shared piece that prints the item, and the field 3 lines. Keep item ids; keep each item on its day and goal. Answer every changed item cold again.

Write the report {rep}: items read (count), a table of faults (item, kind: key, ambiguous, off-goal, rule4, needs-info, two-asks, key-on-child-page, field3; what was wrong; the fix; the stage that made it: unit plan, section plan, data), and your own errors.

Edit only items.csv, wrongs.csv, handbacks.csv, errors.csv and sources.csv rows of this unit, this unit's shared pieces in courses/{course}/u{uu}-*/, field 3 lines of docs/courses/{course}/u{uu}-*.md, and the report. Gate: `python -X utf8 scripts/gate.py --course {course}` shows no new FAIL. {never} Helper scripts only in S:/CurioClass/_scratch/sections/{course}-u{uu}-key/.

Final message under 150 words: items read, faults by kind, fixed, left (with why).""".format(
        course=unit.course, u=unit.u, uu=unit.uu, first=min(unit.days), last=max(unit.days),
        packet=packet.relative_to(ROOT).as_posix(), subj=subj, rep=rep, never=NEVER)


# ---------------------------------------------------------------- the lane

def claude_exe():
    hits = sorted(glob.glob(os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Claude-Data', 'claude_*', 'claude-code',
                                         '*', '*', 'claude.exe')),
                  key=lambda p: [int(x) if x.isdigit() else 0 for x in re.split(r'[.\\/]', p.split('claude-code')[1])[1:4]])
    if not hits:
        raise Stop('no Claude CLI found under %LOCALAPPDATA%\\Claude-Data')
    return hits[-1]


class SectionLane(cl.Lane):
    def __init__(self, subj, dry=False):
        if subj not in COURSES:
            sys.exit('no section lane %r (lanes: %s)' % (subj, ', '.join(COURSES)))
        super().__init__(subj)
        self.dry = dry
        self.dir = RUN / subj / ('dry' if dry else '')
        self.dir.mkdir(parents=True, exist_ok=True)
        if dry:                   # a dry run keeps its own state, fresh each time
            for f in ('done.txt', 'run.log', 'usage.csv'):
                if (self.dir / f).exists():
                    (self.dir / f).unlink()
        self.lock = threading.Lock()
        self.bg = None            # (unit, thread, result dict) of the prep running beside the current unit
        if dry and (self.dir / 'counts.json').exists():
            (self.dir / 'counts.json').unlink()

    def stopped(self):
        return (RUN / 'STOP').exists() or (RUN / self.subj / 'STOP').exists()

    def log(self, line):
        with self.lock:
            super().log(line)

    def mark(self, key):
        with self.lock:
            super().mark(key)

    def check_stop(self):
        if self.stopped():
            raise Stop('STOP file seen')

    # ------------------------------------------------------------ one model call
    def usage(self, unit, stage, result, t0, toks, cost=''):
        p = self.dir / 'usage.csv'
        fresh = not p.exists()
        runner, model, effort = MODELS[stage.split('-')[0]]
        with self.lock, open(p, 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            if fresh:
                w.writerow(['ended', 'course', 'unit', 'stage', 'model', 'effort', 'result', 'minutes', 'tokens_in',
                            'cached_in', 'tokens_out', 'reasoning_out', 'cost_usd'])
            w.writerow([now(), unit.course, unit.u, stage, model, effort, result, round((time.time() - t0) / 60, 1),
                        *toks, cost])

    def run_codex(self, unit, stage, prompt, gate_course=None):
        """One Codex job with the stage's model and effort; a usage limit or two failures raise Stop."""
        _, model, effort = MODELS[stage.split('-')[0]]
        extra = ['-c', 'model="%s"' % model, '-c', 'model_reasoning_effort="%s"' % effort]
        step = dict(course=unit.course, num='u%s' % unit.uu, kind=stage)
        if self.dry:
            self.dry_show(unit, stage, prompt, 'codex exec %s' % ' '.join(extra))
            return dict(last='dry run', thread=None, resume=lambda *a: None)
        for attempt in (1, 2):
            t0 = time.time()
            self.log('start %s %s (%s %s, try %d)' % (unit, stage, model, effort, attempt))
            job = self.codex(step, prompt, extra)
            ok = bool(job['last'].strip())
            ev = ''
            for f in (self.dir / 'jobs').glob('%s-%s-%s*.jsonl' % (step['course'], step['num'], stage.lower())):
                ev += f.read_text(encoding='utf-8', errors='replace')[-20000:].lower()
            limit = job['limit'] or (not ok and any(w in ev for w in LIMIT_WORDS))
            self.usage(unit, stage, 'limit' if limit else ('ok' if ok else 'failed'), t0, job['usage'])
            if limit:
                raise Stop('usage limit reported by Codex at %s %s' % (unit, stage))
            if not ok and ('model_not_found' in ev or 'not supported when using codex' in ev):
                raise Stop('Codex refused the model %s at %s %s (update the Codex CLI, or change MODELS)'
                           % (model, unit, stage))
            if ok:
                return job
            self.log('%s %s ended with no last message' % (unit, stage))
        raise Stop('%s %s failed twice (no last message)' % (unit, stage))

    def run_claude(self, unit, stage, prompt, resume=None):
        """One Claude CLI job. Returns (text, session id). resume: a session id to continue (the gate hand-back)."""
        _, model, effort = MODELS[stage.split('-')[0]]
        base = [claude_exe() if not self.dry else 'claude.exe', '-p', '--model', model, '--effort', effort,
                '--output-format', 'json']
        if self.dry:
            self.dry_show(unit, stage, prompt, ' '.join(base + ['--session-id', '<uuid>', '--allowedTools', CLAUDE_TOOLS]))
            return 'dry run', None
        env = {k: v for k, v in os.environ.items() if not k.startswith(('CLAUDECODE', 'CLAUDE_CODE_'))}
        stem = self.dir / 'jobs' / ('%s-u%s-%s' % (unit.course, unit.uu, stage))
        stem.parent.mkdir(parents=True, exist_ok=True)
        for attempt in (1, 2):
            sid = resume or str(uuid.uuid4())
            cmd = base + (['--resume', sid] if resume else ['--session-id', sid]) + ['--allowedTools', CLAUDE_TOOLS]
            t0 = time.time()
            self.log('start %s %s (%s %s, try %d)' % (unit, stage, model, effort, attempt))
            outp, errp = Path('%s-%d.json' % (stem, attempt)), Path('%s-%d.err' % (stem, attempt))
            with open(outp, 'w', encoding='utf-8') as fo, open(errp, 'w', encoding='utf-8') as fe:
                pr = subprocess.Popen(cmd, cwd=ROOT, stdin=subprocess.PIPE, stdout=fo, stderr=fe, text=True,
                                      encoding='utf-8', env=env,
                                      creationflags=getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0))
                pr.stdin.write(prompt)
                pr.stdin.close()
                timed_out = False
                while pr.poll() is None:
                    time.sleep(15)
                    if time.time() - t0 > CLAUDE_TIMEOUT:
                        timed_out = True
                        subprocess.run(['taskkill', '/T', '/F', '/PID', str(pr.pid)], capture_output=True)
                        break
            raw = outp.read_text(encoding='utf-8', errors='replace')
            errt = errp.read_text(encoding='utf-8', errors='replace')
            try:
                out = json.loads(raw.strip().splitlines()[-1]) if raw.strip() else {}
            except ValueError:
                out = {}
            u = out.get('usage') or {}
            toks = [u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0), u.get('cache_read_input_tokens', 0),
                    u.get('output_tokens', 0), 0]
            text = out.get('result') or ''
            err = timed_out or bool(out.get('is_error')) or not text.strip()
            blob = (text + ' ' + raw[-2000:] + ' ' + errt[-2000:]).lower()
            limit = err and any(w in blob for w in LIMIT_WORDS)
            login = err and any(w in blob for w in ('not logged in', '/login', 'invalid api key', 'authentication'))
            self.usage(unit, stage, 'limit' if limit else ('timeout' if timed_out else ('failed' if err else 'ok')), t0,
                       toks, out.get('total_cost_usd', ''))
            if limit:
                raise Stop('usage limit reported by Claude at %s %s' % (unit, stage))
            if login:
                raise Stop('the Claude CLI is not signed in (run `claude` once and /login), at %s %s' % (unit, stage))
            if not err:
                Path('%s-last.md' % stem).write_text(text, encoding='utf-8')
                return text, sid
            self.log('%s %s: Claude ended in error%s: %s' % (unit, stage, ' (timed out)' if timed_out else '',
                                                            (text or errt or raw or 'no output')[:300]))
            resume = None
            prompt += ('\n\nNote: an earlier run of this job stopped part way. Files it changed may already hold part of '
                       'the work: read them, keep what meets the job, and finish it.')
        raise Stop('%s %s failed twice' % (unit, stage))

    def dry_show(self, unit, stage, prompt, cmd):
        d = self.dir / 'prompts'
        d.mkdir(parents=True, exist_ok=True)
        p = d / ('%s-u%s-%s.txt' % (unit.course, unit.uu, stage))
        p.write_text('COMMAND: %s\n\n%s' % (cmd, prompt), encoding='utf-8')
        toks = re.findall(r'\{[A-Z][A-Z0-9_]*\}', prompt)
        self.log('DRY %s %s: %d words, %s%s' % (unit, stage, len(prompt.split()), p.relative_to(ROOT).as_posix(),
                                               ', UNFILLED %s' % toks if toks else ''))

    # ------------------------------------------------------------ gate, commit
    def gated(self, unit, stage, job=None, sid=None):
        """Re-run the course gate; hand new lines back once (Codex: same session; Claude: a fix call)."""
        if self.dry:
            return 0
        code, out, new = self.gate(unit.course)
        if code == 1:
            self.log('%s %s: %d new gate line(s); handing them back once' % (unit, stage, len(new)))
            msg = ('The lead re-ran the gate for %s after your job (`python -X utf8 scripts/gate.py --course %s`). Fix '
                   'every new failing line below that your job made, as your job says (never bend content to pass a '
                   'gate: a rule that truly does not fit stays, listed as a template point). Then send your last message '
                   'again, updated.\n\n%s' % (unit.course, unit.course, out[-7000:]))
            if job and job.get('thread'):
                u0, t0 = list(job['usage']), time.time()
                job['resume'](msg, '-fix')
                self.usage(unit, stage + '-fix', 'ok' if job['last'].strip() else 'failed', t0,
                           [a - b for a, b in zip(job['usage'], u0)])
            elif sid:
                self.run_claude(unit, stage + '-fix', msg, resume=sid)
            code, out, new = self.gate(unit.course)
        if code == 2:
            raise Stop('%s %s: gate exit 2 (the course changed and has no baseline)' % (unit, stage))
        n = len(new) if code == 1 else 0
        if n:
            self.count(unit.course, new=n)
        return n

    def commit_stage(self, unit, stage, allowed, before, note=''):
        """Commit only this stage's paths; changes inside the course folders but outside them stop the lane."""
        if self.dry:
            return ''
        own = ('docs/courses/%s/' % unit.course, 'data/plans/%s/' % unit.course, 'courses/%s/' % unit.course)
        waited = False
        while True:
            while cl.turn_held():               # wait for a held turn outside the git lock (review 11)
                if not waited:
                    self.log('%s %s: the turn is held; the commit waits' % (unit, stage))
                    waited = True
                time.sleep(60)
            with cl.gitlock():
                if cl.turn_held():
                    continue
                paths, stray, other = [], [], []
                for p, st in cl.porcelain():
                    if p.endswith(('.lock', '.tmp')) or p.startswith(('build/', '_scratch/')):
                        continue                    # safe_write lock and temp files are never work
                    if any(p == x or (x.endswith(('/', '-')) and p.startswith(x)) for x in allowed):
                        paths.append(p)
                    elif p in before:
                        continue
                    elif p.startswith(own):
                        stray.append(p)
                    else:
                        other.append(p)
                if other:
                    self.log('note: files outside %s changed during %s (not committed by this run): %s'
                             % (unit.course, stage, ', '.join(other[:12])))
                if stray:
                    raise Stop('%s %s changed files outside its stage (not committed): %s' % (
                        unit, stage, ', '.join(stray[:12])))
                if not paths:
                    return ''
                cl.git('add', '-A', '--', *paths)
                code, out = cl.git('commit', '-q', '-m', 'Section run (%s): %s %s%s\n\nRun by scripts/section_run.py '
                                   '(docs/pipeline/SECTION-RUN.md); the gate was re-run after the stage.\n\n'
                                   'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'
                                   % (self.subj, stage, unit, note), '--', *paths)
                if code:
                    raise Stop('commit failed at %s %s: %s' % (unit, stage, out.strip()[:300]))
                sha = cl.git('rev-parse', '--short', 'HEAD')[1].strip()
            push(self.log)                       # outside the lock, with a timeout
            return sha

    def stage_done(self, unit, stage):
        return '%s:%s' % (unit.key, stage) in self.done()

    def start(self, unit, stage):
        """Mark that a stage has begun; with no done mark beside it, a rerun knows the stage stopped part way."""
        if not self.stage_done(unit, stage + '-start'):
            self.mark('%s:%s-start' % (unit.key, stage))

    def started(self, unit, stage):
        return self.stage_done(unit, stage + '-start') and not self.stage_done(unit, stage)

    def finish(self, unit, stage, allowed, before, newn=0):
        sha = self.commit_stage(unit, stage, allowed, before, ', %d new gate lines left' % newn if newn else '')
        self.mark('%s:%s' % (unit.key, stage))
        self.log('done %s %s%s%s' % (unit, stage, ', %d new gate lines left' % newn if newn else '',
                                     ', commit ' + sha if sha else ''))

    def counts(self):
        p = self.dir / 'counts.json'
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            return {}

    def count(self, course, new=0, written=0):
        """New gate lines left and sections written per course, kept across reruns (review 13)."""
        with self.lock:
            c = self.counts()
            n = c.setdefault(course, {'new': 0, 'written': 0})
            n['new'] += new
            n['written'] += written
            (self.dir / 'counts.json').write_text(json.dumps(c, indent=1), encoding='utf-8')
            return n

    def pileup(self, unit):
        n = self.count(unit.course)
        if n['new'] > 10 + n['written']:
            raise Stop('%s: %d new gate lines left in %d sections written; read `gate.py --course %s --verbose` and fix '
                       'or note, then clear the "new" count in %s, before going on'
                       % (unit.course, n['new'], n['written'], unit.course, (self.dir / 'counts.json').as_posix()))

    def baseline(self, unit):
        """Before a gated job: a clean course stores its baseline; a changed one with no baseline stops now, before a
        model call is spent on it (review 9)."""
        if self.dry:
            return
        code, out, new = self.gate(unit.course)
        if code == 2:
            raise Stop('%s: the course has uncommitted changes and no gate baseline (gate.py exit 2); commit or clear '
                       'them first' % unit)

    # ------------------------------------------------------------ stages
    def texts(self, unit, second=False):
        stage = 'texts2' if second else 'texts'
        if not unit.ela or self.stage_done(unit, stage) or (not second and not unit.open_texts()
                                                            and not self.started(unit, stage)):
            return
        self.check_stop()
        before = dict(cl.porcelain()) if not self.dry else {}
        self.start(unit, stage)
        self.run_codex(unit, stage, texts_prompt(self, unit, second))
        if not self.dry:
            with self.lock:
                n = cl.merge_texts(unit.course, second)
            code, out = self.py('scripts/section_skeleton.py', unit.course, 'u%d' % unit.u)
            self.log('%s %s: %d text rows merged; skeletons rebuilt (exit %d)' % (unit, stage, n, code))
        self.finish(unit, stage, ('courses/%s/texts/' % unit.course, 'data/plans/ela-texts.csv'), before)

    def prep(self, unit, changed):
        """Prep notes (build/ only, never committed). Safe to run beside another stage."""
        if self.stage_done(unit, 'prep') or not unit.missing_plans():
            return
        self.run_codex(unit, 'prep', prep_prompt(unit, changed))
        miss = [n for n in unit.missing_plans() if not (PREP / unit.course / ('%s.md' % n)).exists()]
        if miss and not self.dry:
            raise Stop('%s prep wrote no note for %s' % (unit, ', '.join(miss)))
        self.mark('%s:prep' % unit.key)
        self.log('done %s prep' % unit)

    def start_bg_prep(self, nxt, changed):
        """Texts of the next unit run here first (they commit), then its prep runs in a thread beside the refine."""
        if nxt is None or self.bg or nxt.green() or not nxt.missing_plans() or self.stage_done(nxt, 'prep'):
            return
        self.texts(nxt)
        res = {}

        def work():
            try:
                self.prep(nxt, changed)
            except Exception as e:            # carried to the main thread at the join
                res['err'] = e
                res['tb'] = traceback.format_exc()
        t = threading.Thread(target=work, daemon=True)
        t.start()
        self.bg = (nxt, t, res)

    def join_bg(self, unit=None):
        if self.bg and (unit is None or self.bg[0].key == unit.key):
            u, t, res = self.bg
            t.join()
            self.bg = None
            if 'err' in res:
                if isinstance(res['err'], Stop):
                    raise res['err']
                raise Stop('%s background prep crashed: %s' % (u, res['tb'][-1500:]))

    def plan_paths(self, unit, names=None):
        return tuple('docs/courses/%s/%s.md' % (unit.course, n) for n in (names or unit.names)) + \
            ('data/plans/%s/ledger.csv' % unit.course,)

    def write(self, unit, changed):
        """Returns the number of sections written. A write that stopped after its plans landed is committed, not redone."""
        if self.stage_done(unit, 'write'):
            return 0
        if not unit.missing_plans():
            if not self.started(unit, 'write'):
                return 0                      # every plan was there before this run (ELA-4): no write, no refine
            self.baseline(unit)
            newn = self.gated(unit, 'write')
            self.finish(unit, 'write', self.plan_paths(unit), {}, newn)
            return 0
        self.check_stop()
        written = 0
        for names, text in write_prompts(self, unit, changed):
            self.check_stop()
            self.baseline(unit)
            before = dict(cl.porcelain()) if not self.dry else {}
            self.start(unit, 'write')
            job = self.run_codex(unit, 'write', text)
            newn = self.gated(unit, 'write', job=job)
            self.commit_stage(unit, 'write', self.plan_paths(unit, names), before,
                              ' %s%s' % (', '.join(names), ', %d new gate lines left' % newn if newn else ''))
            written += len(names)
        miss = unit.missing_plans()
        if miss and not self.dry:
            raise Stop('%s write left no plan for %s' % (unit, ', '.join(miss)))
        self.count(unit.course, written=written)
        self.mark('%s:write' % unit.key)
        self.log('done %s write' % unit)
        return written

    def refine(self, unit):
        if self.stage_done(unit, 'refine'):
            return
        self.check_stop()
        self.baseline(unit)
        before = dict(cl.porcelain()) if not self.dry else {}
        rep = unit.refine_report()
        allowed = self.plan_paths(unit) + (rep.relative_to(ROOT).as_posix(),)
        if self.started(unit, 'refine') and rep.exists():
            self.log('%s refine: its report is there from a stopped run; gate and commit it' % unit)
            self.finish(unit, 'refine', allowed, {}, self.gated(unit, 'refine'))
            return
        self.start(unit, 'refine')
        text, sid = self.run_claude(unit, 'refine', refine_prompt(unit))
        newn = self.gated(unit, 'refine', sid=sid)
        if not self.dry and not rep.exists():
            raise Stop('%s refine wrote no report (%s)' % (unit, rep.relative_to(ROOT).as_posix()))
        self.finish(unit, 'refine', allowed, before, newn)

    def data(self, unit):
        if self.stage_done(unit, 'data'):
            return
        if unit.has_items() and not any(self.stage_done(unit, s) for s in (
                'write-start', 'refine', 'data-start', 'data-a-start', 'data-b-start')):
            # data existed before this run (for example the pilot): keep it, the key read checks it
            self.log('%s data: items rows already exist; kept' % unit)
            self.mark('%s:data' % unit.key)
            return
        allowed = ('data/plans/%s/' % unit.course, 'courses/%s/u%s-' % (unit.course, unit.uu),
                   'docs/courses/%s/u%s-' % (unit.course, unit.uu), 'data/plans/defects.csv')
        for half, text in data_prompts(self, unit):
            st = 'data' + ('-' + half if half else '')
            if self.stage_done(unit, st):
                continue
            self.check_stop()
            self.baseline(unit)
            before = dict(cl.porcelain()) if not self.dry else {}
            self.start(unit, st)
            job = self.run_codex(unit, st, text)
            newn = self.gated(unit, st, job=job)
            self.finish(unit, st, allowed, before, newn)
        if not self.dry and not unit.has_items():
            raise Stop('%s data wrote no items.csv rows for the unit' % unit)
        self.mark('%s:data' % unit.key)

    def key(self, unit):
        if self.stage_done(unit, 'key') or any(tracked(k) for k in unit.key_report()):
            return
        self.check_stop()
        self.baseline(unit)
        before = dict(cl.porcelain()) if not self.dry else {}
        rep = unit.key_path()
        allowed = tuple('data/plans/%s/%s.csv' % (unit.course, t) for t in ('items', 'wrongs', 'handbacks', 'errors',
                                                                           'sources')) + \
            ('courses/%s/u%s-' % (unit.course, unit.uu), 'docs/courses/%s/u%s-' % (unit.course, unit.uu),
             rep.relative_to(ROOT).as_posix())
        if self.started(unit, 'key') and rep.exists():
            self.log('%s key: its report is there from a stopped run; gate and commit it' % unit)
            self.finish(unit, 'key', allowed, {}, self.gated(unit, 'key'))
            return
        packet, n = key_packet(unit)
        if not self.dry and n == 0:
            raise Stop('%s key: the packet has no items rows' % unit)
        self.start(unit, 'key')
        text, sid = self.run_claude(unit, 'key', key_prompt(unit, packet))
        newn = self.gated(unit, 'key', sid=sid)
        if not self.dry and not rep.exists():
            raise Stop('%s key read wrote no report (%s)' % (unit, rep.relative_to(ROOT).as_posix()))
        self.finish(unit, 'key', allowed, before, newn)

    # ------------------------------------------------------------ the waterfall
    def all_units(self):
        """Every unit of the lane in order; a course with a missing input ends the list there (its reason kept)."""
        out, why = [], None
        for c in COURSES[self.subj]:
            try:
                out += course_units(c)
            except Stop as e:
                why = str(e)
                break
        return out, why

    def run(self, limit=None):
        old = cl.LANES_DIR / self.subj
        if not self.dry and old.exists() and not (old / 'STOP').exists() and not (cl.LANES_DIR / 'STOP').exists():
            raise Stop('the codex_lane %s lane has no STOP file; stop it first (build/lanes/%s/STOP)' % (self.subj,
                                                                                                         self.subj))
        stopped = self.dir / 'STOPPED'
        if stopped.exists() and not self.dry:
            stopped.rename(self.dir / ('STOPPED-%s.txt' % dt.datetime.now().strftime('%Y%m%d-%H%M%S')))
        cl.keep_awake(True)
        units, why = self.all_units()
        todo = [u for u in units if not u.green()]
        if limit:
            todo = todo[:limit]
        self.log('section run starts%s: %d units to go (%s first)%s' % (
            ' (DRY)' if self.dry else '', len(todo), todo[0] if todo else 'none',
            '; then stops: %s' % why if why else ''))
        for i, unit in enumerate(todo):
            self.check_stop()
            nxt = todo[i + 1] if i + 1 < len(todo) else None
            changed = changed_list(todo[i - 1]) if i else None   # the previous unit is through its refine by now
            self.join_bg(unit)
            if unit.missing_plans() or self.started(unit, 'write'):
                self.texts(unit)
                self.prep(unit, changed)       # skipped when it already ran beside the previous unit
                self.write(unit, changed)
                self.pileup(unit)
            # the next unit's texts, then its prep beside this refine (prep reads the newest Changed list there is)
            self.start_bg_prep(nxt, changed)
            if self.stage_done(unit, 'write'):
                self.refine(unit)
                self.texts(unit, second=True)
            self.data(unit)
            self.key(unit)
            self.pileup(unit)
            self.log('unit %s green%s' % (unit, ' (dry)' if self.dry else ''))
        if why and not limit:
            raise Stop(why)
        self.log('section run finished: every unit of %s done%s' % (self.subj, ' (dry)' if self.dry else ''))
        cl.keep_awake(False)


def push(log):
    try:
        r = subprocess.run(['git', 'push', '-q', 'origin', 'HEAD:main'], cwd=ROOT, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=300)
        if r.returncode:
            log('push held (the commit stays local; the next push carries it): %s' % (r.stdout + r.stderr).strip()[:200])
    except subprocess.TimeoutExpired:
        log('push timed out after 5 minutes (the commit stays local; the next push carries it)')


def pid_alive(pid):
    r = subprocess.run(['tasklist', '/FI', 'PID eq %d' % pid, '/NH'], capture_output=True, text=True)
    return str(pid) in (r.stdout or '')


class running:
    """One process per lane: build/sections/<subject>/RUNNING holds the pid (review 3)."""
    def __init__(self, lane):
        self.p = lane.dir / 'RUNNING'

    def __enter__(self):
        if self.p.exists():
            try:
                pid = int(self.p.read_text(encoding='utf-8').split()[0])
            except (ValueError, IndexError):
                pid = 0
            if pid and pid != os.getpid() and pid_alive(pid):
                sys.exit('this lane is already running (pid %d, %s)' % (pid, self.p))
        self.p.write_text('%d %s\n' % (os.getpid(), now()), encoding='utf-8')
        return self

    def __exit__(self, *a):
        try:
            self.p.unlink()
        except FileNotFoundError:
            pass


def stop_note(lane, reason):
    lane.log('STOPPED: %s' % reason)
    (lane.dir / 'STOPPED').write_text('%s\n%s\nResume: python -X utf8 scripts/section_run.py run %s\n'
                                      % (now(), reason, lane.subj), encoding='utf-8')


def status():
    for subj in COURSES:
        d = RUN / subj
        last = (d / 'run.log').read_text(encoding='utf-8').splitlines()[-1:] if (d / 'run.log').exists() else ['not started']
        print('%-5s last: %s' % (subj, last[0][:160]))
        if (d / 'STOPPED').exists():
            print('      STOPPED: %s' % (d / 'STOPPED').read_text(encoding='utf-8').splitlines()[1][:300])
        p = d / 'usage.csv'
        if p.exists():
            tot = {}
            with open(p, encoding='utf-8', newline='') as f:
                for r in csv.DictReader(f):
                    t = tot.setdefault(r['stage'].split('-')[0], [0, 0, 0.0, 0.0])
                    t[0] += int(r['tokens_in'] or 0) + int(r['cached_in'] or 0)
                    t[1] += int(r['tokens_out'] or 0) + int(r['reasoning_out'] or 0)
                    t[2] += float(r['minutes'] or 0)
                    t[3] += float(r['cost_usd'] or 0)
            for k, t in tot.items():
                print('      %-7s in %9d  out %8d  %6.1f min%s' % (k, t[0], t[1], t[2], '  $%.2f' % t[3] if t[3] else ''))


def main(a):
    if a[:1] == ['status']:
        status()
        return 0
    if a[:1] in (['run'], ['dry-run']) and len(a) >= 2:
        dry = a[0] == 'dry-run'
        lane = SectionLane(a[1], dry=dry)
        os.environ['GIT_TERMINAL_PROMPT'] = '0'          # a push never waits on a credential prompt
        with running(lane):
            reason = None
            try:
                lane.run(limit=int(a[2]) if len(a) > 2 else None)
                code = 0
            except Stop as e:
                reason, code = str(e), 3
            except Exception:
                reason, code = 'script error:\n' + traceback.format_exc()[-3000:], 4
            if lane.bg:                        # a prep still running beside the stopped stage ends first
                lane.log('waiting for the prep of %s to end before the lane exits' % lane.bg[0])
                try:
                    lane.join_bg()
                except Stop as e:
                    reason = (reason + '; also: ' if reason else '') + str(e)
                    code = code or 3
            if reason:
                stop_note(lane, reason)
            cl.keep_awake(False)
        return code
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
