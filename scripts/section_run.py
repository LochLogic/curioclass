r"""Curio Class section run. One process per subject. See docs/pipeline/SECTION-RUN.md.

    python -X utf8 scripts/section_run.py dry-run <subject> [<units>]   every stage's prompt and command, no model calls
    python -X utf8 scripts/section_run.py run <subject>                 run the lane until a stop (resumes where it stopped)
    python -X utf8 scripts/section_run.py status                        progress, backlog, cooldown, carry and usage

Codex runs texts (ELA), prep, write, crefine, texts2 (ELA) and data. Opus takes finished
units in FIFO order and combines refine and the narrow key read. The next unit's texts and prep
can overlap this pass. Codex sweeps Claude feedback into units written ahead. Claude limits
start a cooldown. Codex limits switch the lane to draining with hourly retries. Stage marks
and reports support resume. A green unit has its plans, plan data and completed key read.
"""
from collections import deque
from contextlib import contextmanager
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
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

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
    'crefine': ('codex', 'gpt-6.2-astra', 'xhigh'),
    'claude': ('claude', 'claude-opus-5-5', 'high'),
    'sweep': ('codex', 'gpt-6.2-sol', 'high'),
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
# Codex's sandbox may run a Python without the markdown module, so a gate can crash before any edit
# (math-grade-1 u04 data stopped this way, 2026-11-27 04:57).
PY_NOTE = ('\n\nPython: use C:\\Users\\Cory\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -X utf8 (it has every '
           'module the gates need). If a gate or check you run before your edits still crashes or exits 2 for a '
           'reason outside your job (a missing module, no baseline), do not stop: do the job, run the checks your job '
           'can, and say so in your last message. The lead re-runs the course gate after every job and hands new '
           'lines back.')
NEVER = ('Never open .claude/, docs/Return/, Gemini/, Gemini.*, data/closet/words/, closet/words/, '
         'data/media-manifest.txt, data/docs-manifest.txt, any path containing math-4 or ela-6. No git commands at all. '
         'No em dashes, US spelling, "Curio Class" in full.')


class Stop(Exception):
    """A lane stop with its reason (SECTION-RUN.md "Stops")."""


class CodexLimit(Stop):
    pass


class ClaudeLimit(Exception):
    pass


def reset_time(message, current):
    """Return an absolute reset timestamp. Clock times without a zone use the lane's local time."""
    m = re.search(r'"resets?_?at"\s*:\s*"?(\d{10})(?=\D|$)', message, re.I)
    if m and int(m[1]) > current:
        return int(m[1])
    m = re.search(r'(?:reset(?:s|ting)?|try again|retry)(?:[_ ]?at| in| after| on)?[\s:"=]*'
                  r'(\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?::\d\d(?:\.\d+)?)?(?:Z|[+-]\d\d:\d\d)?)', message, re.I)
    if m:
        try:
            stamp = dt.datetime.fromisoformat(m[1].upper()).timestamp()
            if stamp > current:
                return stamp
        except ValueError:
            pass
    duration = r'(\d+)\s*(hours?|hrs?|h|minutes?|mins?|m|seconds?|secs?|s)\b'
    m = re.search(r'(?:resets?|try again|retry)\s+(?:in|after)\s+((?:' + duration + r'\s*)+)', message, re.I)
    if m:
        seconds = sum(int(n) * {'h': 3600, 'm': 60, 's': 1}[unit[0].lower()]
                      for n, unit in re.findall(duration, m[1], re.I))
        return current + max(1, seconds)
    m = re.search(r'(?:resets?|try again|retry)\s+(?:at\s+)?(?:(\w{3,9} \d{1,2}),?\s+(?:at\s+)?)?'
                  r'(\d{1,2})(?::(\d\d))?\s*(am|pm)?\b(?:\s*\(?(UTC|GMT|[A-Za-z_]+/[A-Za-z_/]+)\b)?', message, re.I)
    if m:
        h, minute = int(m[2]), int(m[3] or 0)
        if minute < 60 and (1 <= h <= 12 if m[4] else h < 24):
            if m[4]:
                h = h % 12 + 12 * (m[4].lower() == 'pm')
            try:
                zone = None
                if m[5]:
                    if m[5].upper() in ('UTC', 'GMT'):
                        zone = dt.timezone.utc
                    else:
                        try:
                            zone = ZoneInfo(m[5])
                        except ZoneInfoNotFoundError:
                            # Windows Python can lack tzdata. The CLI normally prints the machine's own zone.
                            local = {'America/Denver': 'Mountain', 'America/Los_Angeles': 'Pacific',
                                     'America/New_York': 'Eastern', 'America/Chicago': 'Central'}
                            if time.tzname[0] != local.get(m[5], '') + ' Standard Time':
                                raise
                base = dt.datetime.fromtimestamp(current, zone)
                end = base.replace(hour=h, minute=minute, second=0, microsecond=0)
                if m[1]:
                    month, day = m[1].split()
                    date = dt.datetime.strptime(month[:3] + ' ' + day + ' ' + str(base.year), '%b %d %Y')
                    end = end.replace(month=date.month, day=date.day)
                    if end <= base:
                        end = end.replace(year=end.year + 1)
                elif end <= base:
                    end += dt.timedelta(days=1)
                return end.timestamp()
            except (ValueError, ZoneInfoNotFoundError):
                pass
    return current + 3600


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

    def report_path(self, prefix):
        """Reuse a landed report, including one left before midnight by an interrupted job."""
        if not hasattr(self, '_reports'):
            self._reports = {}
        if prefix not in self._reports:
            stem = ROOT / 'docs' / 'reviews' / self.course / ('%s-%s-u%s' % (prefix, self.course, self.uu))
            existing = sorted(stem.parent.glob(stem.name + '-*.md'))
            self._reports[prefix] = existing[-1] if existing else Path('%s-%s.md' % (stem, today()))
        return self._reports[prefix]

    def refine_report(self, stage='refine'):
        return self.report_path('section-' + stage)

    def key_path(self):
        return self.report_path('answer-key')


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


def report_changes(path):
    if path.exists():
        parts = re.split(r'^## Changed for the next unit[ \t]*\r?$', path.read_text(encoding='utf-8'), flags=re.M)
        if len(parts) > 1 and parts[-1].strip() and not re.search(r'^#{1,6} ', parts[-1], re.M):
            return parts[-1].strip()
    return ''


def changed_list(previous, carry, course=None):
    lists = []
    if previous:
        prior = report_changes(previous.refine_report('crefine'))
        if not prior and previous.course == course:
            prior = report_changes(previous.refine_report())
        lists.append(prior)
    lists.extend(item['text'] for item in carry)
    lines = [line.rstrip() for block in lists for line in block.splitlines() if line.strip() and line.strip() != 'None.']
    return '\n'.join(reversed(dict.fromkeys(reversed(lines))))


# ---------------------------------------------------------------- read bundles (Cory 2026-11-27)

BUNDLE_CAP = 80000          # words; past it the largest files stay as paths for the model to open
UNIT_RULES = ('The rules', 'The section plan: fields, in order', 'Length')
WRITE_NOTE = ('\n\nWriting: when you create or change several files, do it in as few tool calls as you can (one '
              'apply_patch call can add or change several files; Claude: send independent edits together in one '
              'message), then run the checks once over all of them.')


def cut(text, heads):
    """The parts of a Markdown file under the named headings (any level), each to the next heading of its level or
    higher."""
    out, keep = [], 0
    for ln in text.splitlines():
        m = re.match(r'^(#{1,6}) (.*?)\s*$', ln)
        if m:
            lvl = len(m.group(1))
            if keep and lvl <= keep:
                keep = 0
            if not keep and m.group(2).strip() in heads:
                keep = lvl
        if keep:
            out.append(ln)
    return '\n'.join(out)


def bundle(entries):
    """Files put in the prompt in full, so a job spends no turns opening them. entries: (path, heads or None).
    Missing files are skipped; past BUNDLE_CAP words the largest are listed as paths instead."""
    got = []
    for rel, heads in entries:
        p = ROOT / rel
        if not p.is_file() or any(rel == g[0] for g in got):
            continue
        text = p.read_text(encoding='utf-8', errors='replace')
        if heads:
            text = cut(text, heads)
            if not text.strip():
                continue
        got.append((rel, heads, text.strip()))
    left = []
    while got and sum(len(t.split()) for _, _, t in got) > BUNDLE_CAP:
        big = max(got, key=lambda g: len(g[2].split()))
        got.remove(big)
        left.append(big[0])
    if not got:
        return ''
    parts = ['\n\n# Read bundle from the section run lead\n\nThese files are below in full as they stood just before '
             'your job (a heading list means only those parts). Do not open them again; read them here. Where your '
             'job says to read only part of one, use that part. After you edit one of them, read your edit from disk, '
             'not from here. Open other files as your job says.' +
             ('\nLeft out for length (open them as your job says): %s.' % ', '.join(left) if left else '')]
    for rel, heads, text in got:
        parts.append('\n===== %s%s =====\n%s' % (rel, ' (parts: %s)' % '; '.join(heads) if heads else '', text))
    parts.append('\n===== end of the read bundle =====')
    return '\n'.join(parts)


def rule_files(unit, unit_plan=True):
    approach = 'docs/APPROACH-%s.md' % ('ELA' if unit.ela else 'MATH')
    out = [('AGENTS.md', None), ('docs/pipeline/briefs/section-write.md', None),
           ('docs/courses/UNIT-PLAN.md', UNIT_RULES), ('docs/courses/%s/DEFAULTS.md' % unit.course, None),
           (approach, None)]
    if unit_plan:
        out.append(('docs/courses/%s/s%s.md' % (unit.course, unit.uu), None))
    return out


def unit_files(unit, names=None, skel=True, prep=True, plans=True):
    out = []
    for n in names or unit.names:
        if skel:
            out.append(('docs/courses/%s/section-skeletons/%s.md' % (unit.course, n), None))
        if prep:
            out.append(('build/sections/prep/%s/%s.md' % (unit.course, n), None))
        if plans:
            out.append(('docs/courses/%s/%s.md' % (unit.course, n), None))
    return out


def plan_before(unit):
    """This course's section plan just before the unit's first section (the last plan of the unit before)."""
    if unit.u <= 1:
        return []

    def num(p):
        m = re.search(r'-(\d+)\.md$', p.name)
        return int(m.group(1)) if m else 0
    prev = sorted((ROOT / 'docs' / 'courses' / unit.course).glob('u%02d-*.md' % (unit.u - 1)), key=num)
    return [(prev[-1].relative_to(ROOT).as_posix(), None)] if prev else []


# ---------------------------------------------------------------- prompts

def kit_job(lane, unit, kind, template, extra, detail):
    """Render a kit template through coursegen's Queue (same tokens and notes as the course run)."""
    out = lane.dir / 'jobs-kit'
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
    ch = ('Carry these lessons from earlier units into your notes where they apply:\n' + changed
          if changed else 'There are no earlier changes to carry into these notes.')
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
            text += '- Apply these lessons from earlier units where they fit:\n%s\n' % changed
        written = [n for n in unit.names if n not in todo]
        if written:
            text += '- These sections of the unit are already written; leave them as they are: %s.\n' % ', '.join(written)
        out.append((names, text))
    return out


def refine_prompt(unit, stage='refine'):
    subj = 'ela' if unit.ela else 'math'
    approach = 'docs/APPROACH-%s.md' % ('ELA' if unit.ela else 'MATH')
    rep = unit.refine_report(stage).relative_to(ROOT).as_posix()
    plans = ', '.join('docs/courses/%s/%s.md' % (unit.course, n) for n in unit.names)
    return """You are the refine pass of the section run in the Curio Class repository, S:\\CurioClass (Windows; Bash with POSIX paths like /s/CurioClass, `python -X utf8`). Read AGENTS.md first.

Review the section plans of {course} unit {u}: {plans}. Bring them to the section plan bar. The gates already pass or list their lines; judge what a gate cannot.

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


def key_packet(unit, directory=PACKETS):
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
    directory.mkdir(parents=True, exist_ok=True)
    out = directory / ('%s-u%s.md' % (unit.course, unit.uu))
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


def read_state(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def save_state(path, value):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2), encoding='utf-8')
    tmp.replace(path)


def course_inventory(subj):
    units = []
    for course in COURSES[subj]:
        try:
            units.extend(course_units(course))
        except Stop as e:
            return units, str(e)
    return units, None


def unit_state(unit, marks, check_tracked=False):
    """Read old and new stage marks. A report from an unfinished pass still needs its gate and commit."""
    stages = {m[len(unit.key) + 1:] for m in marks if m.startswith(unit.key + ':')}
    if unit.missing_plans() or not unit.has_items():
        return 'todo'
    interrupted = any(s + '-start' in stages and s not in stages for s in ('claude', 'key'))
    if not interrupted and any(not check_tracked or tracked(p) for p in unit.key_report()):
        return 'green'
    if 'codex-done' in stages or 'data' in stages:
        return 'backlog'
    if stages.isdisjoint({'write', 'write-start', 'refine', 'refine-start', 'data-start', 'data-a-start', 'data-b-start'}):
        return 'backlog'   # pilot or existing plans and data
    return 'todo'


KEY_TABLES = ('items', 'wrongs', 'handbacks', 'errors', 'sources')
DATA_TABLES = KEY_TABLES + ('parts', 'days', 'words', 'materials', 'source-map', 'wordlist')


def table_paths(course, tables):
    return tuple('data/plans/%s/%s.csv' % (course, name) for name in tables)


@contextmanager
def quota_guard(paths, dry):
    """Undo only this attempt's unfinished, exclusively owned edits before another unit uses its course CSVs."""
    def files():
        found = set()
        for pattern in paths:
            p = ROOT / pattern
            if pattern.endswith('/'):
                found.update(p.rglob('*'))
            elif pattern.endswith('-'):
                for match in p.parent.glob(p.name + '*'):
                    found.update(match.rglob('*') if match.is_dir() else [match])
            else:
                found.add(p)
        return {p for p in found if p.is_file() and p.suffix not in ('.lock', '.tmp')}

    before = {} if dry else {p: p.read_bytes() for p in files()}
    try:
        yield
    except (ClaudeLimit, CodexLimit):
        if not dry:
            for p in files() - before.keys():
                p.unlink()
            for p, contents in before.items():
                if not p.exists() or p.read_bytes() != contents:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    tmp = p.with_name(p.name + '.tmp')
                    tmp.write_bytes(contents)
                    tmp.replace(p)
        raise


class SectionLane(cl.Lane):
    def __init__(self, subj, dry=False):
        if subj not in COURSES:
            sys.exit('no section lane %r (lanes: %s)' % (subj, ', '.join(COURSES)))
        self.subj = subj
        self.dry = dry
        self.dir = RUN / subj / ('dry' if dry else '')
        self.dir.mkdir(parents=True, exist_ok=True)
        if dry:                   # a dry run keeps its own state, fresh each time
            for f in ('done.txt', 'run.log', 'usage.csv', 'counts.json', 'carry.json', 'claude-cooldown.json'):
                if (self.dir / f).exists():
                    (self.dir / f).unlink()
        self.lock = threading.Lock()
        self.bg = None            # (unit, thread, result dict) of the prep running beside the current unit
        self.reviewing = None
        self.parallel_paths = ()
        self.carry = read_state(self.dir / 'carry.json', [])
        self.cooldown = read_state(self.dir / 'claude-cooldown.json', 0)
        self.dry_sweep = dry
        self.prompt_counts = {}

    def stopped(self):
        if self.dry:
            return (self.dir / 'STOP').exists()
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
        runner, model, effort = MODELS[stage.split('-')[0]]
        with self.lock, open(p, 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            if f.tell() == 0:
                w.writerow(['ended', 'course', 'unit', 'stage', 'model', 'effort', 'result', 'minutes', 'tokens_in',
                            'cached_in', 'tokens_out', 'reasoning_out', 'cost_usd'])
            w.writerow([now(), unit.course, unit.u, stage, model, effort, result, round((time.time() - t0) / 60, 1),
                        *toks, cost])

    def run_codex(self, unit, stage, prompt):
        """One Codex job. Return quota denials to the scheduler separately from job failures."""
        _, model, effort = MODELS[stage.split('-')[0]]
        extra = ['-c', 'model="%s"' % model, '-c', 'model_reasoning_effort="%s"' % effort]
        step = dict(course=unit.course, num='u%s' % unit.uu, kind=stage)
        prompt += PY_NOTE + WRITE_NOTE
        if self.dry:
            self.dry_show(unit, stage, prompt, 'codex exec %s' % ' '.join(extra))
            return dict(last='dry run', thread=None, resume=lambda *a: None)
        for attempt in (1, 2):
            self.check_stop()
            t0 = time.time()
            self.log('start %s %s (%s %s, try %d)' % (unit, stage, model, effort, attempt))
            job = self.codex(step, prompt, extra)
            ok = bool(job['last'].strip())
            ev = ''
            for suffix in ('', '-resume'):
                f = self.dir / 'jobs' / ('%s-%s-%s%s.jsonl' % (step['course'], step['num'], stage.lower(), suffix))
                if not ok and not job['limit'] and f.exists() and f.stat().st_mtime >= t0 - 0.01:
                    with f.open('rb') as events:
                        events.seek(max(0, f.stat().st_size - 20000))
                        ev += events.read().decode('utf-8', errors='replace').lower()
            limit = job['limit'] or (not ok and any(w in ev for w in LIMIT_WORDS))
            self.usage(unit, stage, 'limit' if limit else ('ok' if ok else 'failed'), t0, job['usage'])
            if limit:
                raise CodexLimit('usage limit reported by Codex at %s %s' % (unit, stage))
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
        # --tools loads only these six: the fixed overhead per call drops from about 31k to 13k tokens (measured
        # 2026-11-26); --allowedTools then scopes what Bash may run
        base = [claude_exe() if not self.dry else 'claude.exe', '-p', '--model', model, '--effort', effort,
                '--output-format', 'json', '--tools', 'Read,Edit,Write,Glob,Grep,Bash']
        if self.dry:
            self.dry_show(unit, stage, prompt, ' '.join(base + ['--session-id', '<uuid>', '--allowedTools', CLAUDE_TOOLS]))
            return 'dry run', None
        env = {k: v for k, v in os.environ.items() if not k.startswith(('CLAUDECODE', 'CLAUDE_CODE_'))}
        stem = self.dir / 'jobs' / ('%s-u%s-%s' % (unit.course, unit.uu, stage))
        stem.parent.mkdir(parents=True, exist_ok=True)
        for attempt in (1, 2):
            self.check_stop()
            sid = resume or str(uuid.uuid4())
            cmd = base + (['--resume', sid] if resume else ['--session-id', sid]) + ['--allowedTools', CLAUDE_TOOLS]
            t0 = time.time()
            self.log('start %s %s (%s %s, try %d)' % (unit, stage, model, effort, attempt))
            outp, errp = Path('%s-%d.json' % (stem, attempt)), Path('%s-%d.err' % (stem, attempt))
            with open(outp, 'w', encoding='utf-8') as fo, open(errp, 'w', encoding='utf-8') as fe:
                pr = subprocess.Popen(cmd, cwd=ROOT, stdin=subprocess.PIPE, stdout=fo, stderr=fe, text=True,
                                      encoding='utf-8', env=env,
                                      creationflags=getattr(subprocess, 'CREATE_NEW_PROCESS_GROUP', 0))
                try:
                    pr.stdin.write(prompt)
                    pr.stdin.close()
                except BrokenPipeError:
                    pass  # The CLI can reject the call before reading stdin. Classify its output below.
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
            err = timed_out or bool(pr.returncode or out.get('is_error')) or not text.strip()
            blob = (text + ' ' + raw[-2000:] + ' ' + errt[-2000:]).lower()
            login = any(w in blob for w in ('not signed in', 'not logged in', 'invalid api key')) or (
                err and any(w in blob for w in ('/login', 'authentication')))
            limit = not login and any(w in (blob if err else text.lower()) for w in LIMIT_WORDS)
            self.usage(unit, stage, 'limit' if limit else ('timeout' if timed_out else ('failed' if err else 'ok')), t0,
                       toks, out.get('total_cost_usd', ''))
            if limit:
                raise ClaudeLimit(text + '\n' + errt + '\n' + raw)
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
        stem = '%s-u%s-%s' % (unit.course, unit.uu, stage)
        count = self.prompt_counts.get(stem, 0) + 1
        self.prompt_counts[stem] = count
        p = d / (stem + (('-%d' % count) if count > 1 else '') + '.txt')
        p.write_text('COMMAND: %s\n\n%s' % (cmd, prompt), encoding='utf-8')
        toks = re.findall(r'\{[A-Z][A-Z0-9_]*\}', prompt)
        self.log('DRY %s %s: %d words, %s%s' % (unit, stage, len(prompt.split()), p.relative_to(ROOT).as_posix(),
                                               ', UNFILLED %s' % toks if toks else ''))

    # ------------------------------------------------------------ gate, commit
    def gate(self, course):
        """The course gate, without index-reports orphan lines: the index reads leans_on only from written lesson
        files, so every piece of a unit still at section-plan stage is an orphan until its days are written. Those
        lines are neither handed back nor counted toward a pileup (Cory 2026-11-27 overnight run)."""
        code, out, new = super().gate(course)
        if code != 1 or self.dry:
            return code, out, new
        full = ROOT / 'build' / 'gates' / ('now-' + course) / 'compare.txt'
        def orphan_free(text_lines):
            kept, gate = [], ''
            for ln in text_lines:
                if ln.startswith('== '):
                    gate = ln[3:].split(' ')[0].rstrip(':')
                if gate == 'index-reports' and ln.startswith('  FAIL-NEW') and 'orphans:' in ln:
                    continue
                kept.append(ln)
            return kept
        lines = full.read_text(encoding='utf-8').splitlines() if full.exists() else out.splitlines()
        fails = [ln for ln in lines if ln.startswith('  FAIL-NEW')]
        keep = [ln for ln in orphan_free(lines) if ln.startswith('  FAIL-NEW')]
        if len(keep) == len(fails):
            return code, out, new
        if not keep and not any('GATE GONE' in ln or ('exit code' in ln and not ln.startswith('== index-reports'))
                                for ln in lines if ln.startswith('== ')):
            return 0, out, []
        return code, '\n'.join(orphan_free(out.splitlines())) + \
            '\n(index-reports orphan lines left out: their lessons are not written yet)\n', keep

    def gated(self, unit, stage, job=None, sid=None, recovery_prompt=None):
        """Re-run the course gate; hand new lines back once (Codex: same session; Claude: a fix call)."""
        if self.dry:
            return 0
        code, out, new = self.gate(unit.course)
        if code == 1:
            self.check_stop()
            self.log('%s %s: %d new gate line(s); handing them back once' % (unit, stage, len(new)))
            msg = ('The lead re-ran the gate for %s after your job (`python -X utf8 scripts/gate.py --course %s`). Fix '
                   'every new failing line below that your job made, as your job says (never bend content to pass a '
                   'gate: a rule that truly does not fit stays, listed as a template point). Then send your last message '
                   'again, updated.\n\n%s' % (unit.course, unit.course, out[-7000:]))
            if job and job.get('thread'):
                u0, t0 = list(job['usage']), time.time()
                job['resume'](msg, '-fix')
                self.usage(unit, stage + '-fix', 'limit' if job['limit'] else ('ok' if job['last'].strip() else 'failed'), t0,
                           [a - b for a, b in zip(job['usage'], u0)])
                if job['limit']:
                    raise CodexLimit('usage limit reported by Codex at %s %s-fix' % (unit, stage))
            elif sid or recovery_prompt:
                self.run_claude(unit, stage + '-fix', msg if sid else recovery_prompt + '\n\n' + msg, resume=sid)
            code, out, new = self.gate(unit.course)
        if code == 2:
            raise Stop('%s %s: gate exit 2 (the course changed and has no baseline)' % (unit, stage))
        n = len(new) if code == 1 else 0
        if n:
            self.count(unit.course, new=n)
        self.level(unit.course, out)
        return n

    def commit_stage(self, unit, stage, allowed, before, note=''):
        """Commit only this stage's paths; changes inside the course folders but outside them stop the lane."""
        if self.dry:
            return ''
        own = tuple('%s/%s/' % (folder, unit.course) for folder in ('docs/courses', 'docs/reviews', 'data/plans', 'courses'))
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
                    elif any(p == x or (x.endswith(('/', '-')) and p.startswith(x)) for x in self.parallel_paths):
                        continue
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

    def level(self, course, out):
        """The course's failing lines now, without index-reports orphans, read from the gate's own summary. The pileup
        reads this level, not the sum of 'new' reports: a line a unit's pass leaves stays one line, where the sum
        counted it again at the next pass (math grade 1, 2026-11-27 07:20: 31 counted, 15 real). 'start' is the level
        when the lane first reads a course, so lines older than the run do not count (set by hand when a course's
        older lines should count, as math grade 1's 15 do)."""
        if self.dry:
            return
        m = re.search(r'(\d+) failing line\(s\) for \S+ now', out)
        if not m:
            return
        orph = sum(int(x) for x in re.findall(r'^\s+(\d+)\s+index-reports: orphans\s*$', out, re.M))
        now = int(m.group(1)) - orph
        with self.lock:
            c = self.counts()
            n = c.setdefault(course, {'new': 0, 'written': 0})
            if 'start' not in n:
                n['start'] = now
            n['now'] = now
            (self.dir / 'counts.json').write_text(json.dumps(c, indent=1), encoding='utf-8')

    def pileup(self, unit):
        n = self.count(unit.course)
        left = n['now'] - n.get('start', 0) if 'now' in n else n['new']
        if left > 10 + n['written']:
            raise Stop('%s: %d gate lines left in %d sections written (%d failing now, %d before the run); read '
                       '`gate.py --course %s --verbose` and fix or note them, then raise "start" in %s to the lines '
                       'you are leaving, before going on'
                       % (unit.course, left, n['written'], n.get('now', n['new']), n.get('start', 0), unit.course,
                          (self.dir / 'counts.json').as_posix()))

    def baseline(self, unit):
        """Before a gated job: a clean course stores its baseline; a changed one with no baseline stops now, before a
        model call is spent on it (review 9)."""
        if self.dry:
            return
        code, out, new = self.gate(unit.course)
        self.level(unit.course, out)
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
        side = cl.TEXTS_OUT / ('%s-u%d%s.csv' % (unit.course, unit.u, '-new' if second else ''))
        with quota_guard(('courses/%s/texts/' % unit.course, side.relative_to(ROOT).as_posix()), self.dry):
            self.run_codex(unit, stage, texts_prompt(self, unit, second))
        if not self.dry:
            with self.lock:
                n = cl.merge_texts(unit.course, second)
            code, out = self.py('scripts/section_skeleton.py', unit.course, 'u%d' % unit.u)
            self.log('%s %s: %d text rows merged; skeletons rebuilt (exit %d)' % (unit, stage, n, code))
        self.finish(unit, stage, ('courses/%s/texts/' % unit.course, 'data/plans/ela-texts.csv',
                                  'data/plans/%s/sources.csv' % unit.course), before)

    def feedback(self, unit):
        marks = self.done()
        seen = {m.split(':prep-carry:', 1)[1] for m in marks if ':prep-carry:' in m}
        return [item for item in self.carry if item['unit'].split(':')[0] == unit.course and 'dry_target' not in item and
                (item['unit'] not in seen or '%s:prep-carry:%s' % (unit, item['unit']) in marks)]

    def prep(self, unit, previous):
        """Prep notes (build/ only, never committed). Safe to run beside another stage."""
        missing = unit.missing_plans()
        if not missing or (self.stage_done(unit, 'prep') and
                           (self.dry or all((PREP / unit.course / (n + '.md')).is_file() for n in missing))):
            return
        self.check_stop()
        carry = self.feedback(unit)
        self.skeletons(unit)
        self.run_codex(unit, 'prep', prep_prompt(unit, changed_list(previous, carry, unit.course)) + bundle(
            rule_files(unit) + unit_files(unit, prep=False, plans=False) +
            plan_before(unit)))
        miss = [n for n in unit.missing_plans() if not (PREP / unit.course / ('%s.md' % n)).exists()]
        if miss and not self.dry:
            raise Stop('%s prep wrote no note for %s' % (unit, ', '.join(miss)))
        self.mark('\n'.join(['%s:prep-carry:%s' % (unit, item['unit']) for item in carry] + ['%s:prep' % unit]))
        self.log('done %s prep' % unit)

    def skeletons(self, unit):
        """Rebuild the unit's section skeletons before a bundle reads them (the job would rebuild them anyway)."""
        if not self.dry:
            self.py('scripts/section_skeleton.py', unit.course, 'u%d' % unit.u)

    def start_bg_prep(self, nxt, previous):
        """One worker does the next unit's texts and then prep while Opus reviews an older unit."""
        if nxt is None or self.bg or not nxt.missing_plans() or self.stage_done(nxt, 'prep'):
            return
        res = {}

        def work():
            try:
                self.texts(nxt)
                self.prep(nxt, previous)
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
        if self.stage_done(unit, 'write') and (self.dry or not unit.missing_plans()):
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
        self.skeletons(unit)
        for names, text in write_prompts(self, unit, changed):
            self.check_stop()
            self.baseline(unit)
            text += bundle(rule_files(unit) + unit_files(unit, names, plans=False) + plan_before(unit) +
                           [('docs/courses/%s/%s.md' % (unit.course, n), None) for n in unit.names if n not in names])
            before = dict(cl.porcelain()) if not self.dry else {}
            self.start(unit, 'write')
            with quota_guard(self.plan_paths(unit, names), self.dry):
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

    def crefine(self, unit):
        if unit.refine_report().exists():
            if not self.dry and not tracked(unit.refine_report()):
                self.baseline(unit)
                allowed = self.plan_paths(unit) + (unit.refine_report().relative_to(ROOT).as_posix(),)
                self.finish(unit, 'refine', allowed, {}, self.gated(unit, 'refine'))
            return
        rep = unit.refine_report('crefine')
        if self.stage_done(unit, 'crefine') and (self.dry or rep.exists()):
            return
        self.check_stop()
        self.baseline(unit)
        before = dict(cl.porcelain()) if not self.dry else {}
        allowed = self.plan_paths(unit) + (rep.relative_to(ROOT).as_posix(),)
        self.start(unit, 'crefine')
        with quota_guard(allowed, self.dry):
            if not report_changes(rep):
                self.skeletons(unit)
            job = None if report_changes(rep) else self.run_codex(
                unit, 'crefine', refine_prompt(unit, 'crefine') + bundle(rule_files(unit) + unit_files(unit)))
            newn = self.gated(unit, 'crefine', job=job)
        if not self.dry and not report_changes(rep):
            raise Stop('%s crefine left no final Changed list in %s' % (unit, rep))
        self.finish(unit, 'crefine', allowed, before, newn)

    def data(self, unit):
        if self.stage_done(unit, 'data') and (self.dry or unit.has_items()):
            return
        if unit.has_items() and not any(self.stage_done(unit, s) for s in (
                'write-start', 'refine', 'data-start', 'data-a-start', 'data-b-start')):
            # data existed before this run (for example the pilot): keep it, the key read checks it
            self.log('%s data: items rows already exist; kept' % unit)
            self.mark('%s:data' % unit.key)
            return
        owned = ('data/plans/%s/' % unit.course, 'courses/%s/u%s-' % (unit.course, unit.uu),
                 'docs/courses/%s/u%s-' % (unit.course, unit.uu))
        allowed = owned + ('data/plans/defects.csv',)
        rebuild = not self.dry and not unit.has_items()
        halves = data_prompts(self, unit)
        groups = cg.halves(unit.secs) if unit.ela else [unit.secs]
        for i, (half, text) in enumerate(halves):
            st = 'data' + ('-' + half if half else '')
            if self.stage_done(unit, st) and not rebuild:
                continue
            self.check_stop()
            # A split data stage is gated once, after its last half, against the baseline from before the first
            # half: the first half's open lines (often the exits the second half writes) are not counted twice,
            # and what neither half fixed goes back to the last half's session (Cory 2026-11-27 overnight run).
            last = i == len(halves) - 1
            if i == 0:
                self.baseline(unit)
            before = dict(cl.porcelain()) if not self.dry else {}
            self.start(unit, st)
            names = [cg.sname(unit.uu, s) for s, _ in groups[i]] if i < len(groups) else unit.names
            text += bundle([('AGENTS.md', None), ('docs/pipeline/briefs/plan-data.md', None),
                            ('data/plans/README.md', None), ('docs/courses/LESSON-DAY.md', None),
                            ('docs/courses/%s/s%s.md' % (unit.course, unit.uu), None),
                            ('docs/courses/%s/DEFAULTS.md' % unit.course, None)] +
                           ([('docs/courses/UNIT-PLAN.md', ('English language arts data',))] if unit.ela else []) +
                           unit_files(unit, names, skel=False, prep=False))
            with quota_guard(owned, self.dry):
                job = self.run_codex(unit, st, text)
                newn = self.gated(unit, st, job=job) if last else 0
            self.finish(unit, st, allowed, before, newn)
        if not self.dry and not unit.has_items():
            raise Stop('%s data wrote no items.csv rows for the unit' % unit)
        self.mark('%s:data' % unit.key)

    def record_carry(self, unit):
        if any(item['unit'] == unit.key for item in self.carry):
            return
        changes = changed_list(None, [{'text': report_changes(p)} for p in (unit.refine_report(), unit.key_path())])
        if changes:
            self.carry.append(dict(unit=unit.key, text=changes, time=now(), applied_to=[]))
            save_state(self.dir / 'carry.json', self.carry)

    def sweep_items(self, unit, marks):
        return [item for item in self.carry if item['unit'].split(':')[0] == unit.course and item['unit'] != unit.key
                and item.get('dry_target', unit.key) == unit.key
                and unit.key not in item['applied_to'] and '%s:write-carry:%s' % (unit, item['unit']) not in marks]

    def sweep(self, backlog):
        groups = {}
        marks = self.done()
        for unit in backlog:
            if unit == self.reviewing:
                continue
            items = self.sweep_items(unit, marks)
            if self.dry_sweep and not items:
                example = dict(unit=unit.course + ':dry-example', time=now(), applied_to=[], dry_target=unit.key,
                               text='- Check that each changed exit still matches its item and teacher key.')
                self.carry.append(example)
                items = [example]
            self.dry_sweep = False
            if items:
                groups.setdefault(unit.course, []).append((unit, items))
        for course, targets in groups.items():
            self.check_stop()
            first = targets[0][0]
            paths = tuple(dict.fromkeys(path for unit, _ in targets for path in self.plan_paths(unit)))
            allowed = paths + table_paths(course, DATA_TABLES)
            prompt = ('Read AGENTS.md and docs/pipeline/briefs/section-write.md. Apply the Claude feedback below only '
                      'where it fits each named unit. Inspect the section plans and their data first. Keep exits, keys, '
                      'wrong answers, handbacks, sources and ledger entries consistent. Solve changed items cold. '
                      'Never bend content for a gate. Preserve edits already made on an interrupted sweep. '
                      'Use scripts/ledger.py for the ledger. In shared CSVs edit only rows belonging to the named '
                      'sections and days, preserving other rows and full IDs. Edit only these paths:\n%s\n\n%s\n\n%s\n'
                      'Run python -X utf8 scripts/gate.py --course %s and report what you applied or left with why.'
                      % ('\n'.join(allowed), '\n\n'.join('%s (sections %s, days %d to %d)\n%s' % (
                          u, ', '.join(u.names), min(u.days), max(u.days), changed_list(None, items))
                          for u, items in targets), NEVER, course))
            prompt += bundle([('AGENTS.md', None), ('docs/pipeline/briefs/section-write.md', None)] +
                             [f for u, _ in targets for f in unit_files(u, skel=False, prep=False)])
            self.baseline(first)
            before = {} if self.dry else dict(cl.porcelain())
            with quota_guard(allowed, self.dry):
                job = self.run_codex(first, 'sweep', prompt)
                newn = self.gated(first, 'sweep', job=job)
            self.commit_stage(first, 'sweep', allowed, before)
            for unit, items in targets:
                for item in items:
                    item['applied_to'].append(unit.key)
            save_state(self.dir / 'carry.json', self.carry)
            self.log('done %s sweep: %s (%d new gate lines)' % (course, ', '.join(str(u) for u, _ in targets), newn))
            self.pileup(first)

    def claude_pass(self, unit, nxt, previous):
        """Finish the oldest queued unit. Return False on cooldown, leaving it at the head."""
        self.check_stop()
        self.baseline(unit)
        refine, key = unit.refine_report(), unit.key_path()
        combined = self.started(unit, 'claude') or not refine.exists()
        stage = 'claude' if combined else 'key'
        reports = [refine, key] if combined else [key]
        allowed = table_paths(unit.course, KEY_TABLES) + ('courses/%s/u%s-' % (unit.course, unit.uu),
                  'docs/courses/%s/u%s-' % (unit.course, unit.uu), key.relative_to(ROOT).as_posix())
        if combined:
            allowed += self.plan_paths(unit) + (refine.relative_to(ROOT).as_posix(),)
        elif not self.dry and not tracked(refine):
            self.finish(unit, 'refine', self.plan_paths(unit) + (refine.relative_to(ROOT).as_posix(),), {},
                        self.gated(unit, 'refine'))

        packet, n = key_packet(unit, self.dir / 'packets' if self.dry else PACKETS)
        if not self.dry and n == 0:
            raise Stop('%s key: the packet has no judged items' % unit)
        prompt = key_prompt(unit, packet)
        if combined:
            prompt = ('Complete both jobs in this session on the finished unit. First solve the narrow key packet cold '
                      'before reading plans, keys or prep notes for the refine. Then run the full refine. The read '
                      'and edit restrictions below apply to their respective tasks. Reconcile both sets of fixes in '
                      'the plans, ledger, shared pieces and the listed data rows of this unit. Recheck changed items '
                      'cold against the final files. Write both named reports.\n\n' + prompt + '\n\n' + refine_prompt(unit))
        prompt += ('\n\nEnd each report you write with the final heading "## Changed for the next unit" and the same '
                   'list of lessons from this pass, or "None." if nothing carries.')
        swept = [item for item in self.carry if unit.key in item['applied_to']]
        if swept:
            prompt += '\n\nVerify that these swept changes landed where applicable:\n' + changed_list(None, swept)
        pending = self.sweep_items(unit, self.done())
        if pending:
            prompt += ('\n\nCodex has not swept these lessons yet. Check them within this review\'s scope and '
                       'apply where relevant. Identify any applicable fix outside that scope in the report:\n' +
                       changed_list(None, pending))

        # Rules only: the key read solves its packet cold before it sees plans, prep notes, skeletons or the unit
        # plan, so none of those are bundled (they hold keys).
        prompt += WRITE_NOTE + bundle(rule_files(unit, unit_plan=False) if combined else
                         [('AGENTS.md', None), ('docs/pipeline/briefs/sensitivity-read.md',
                                                ('1. Study first (every kind)', '2. Read the target'))])
        # An interrupted old key read can legitimately predate the final Changed heading.
        legacy_key = (not combined and self.started(unit, 'key') and key.exists() and
                      not self.stage_done(unit, 'key-with-carry'))
        landed = legacy_key or all(report_changes(p) for p in reports)
        before = {} if self.dry else dict(cl.porcelain())
        self.reviewing = unit
        text_paths = ('courses/%s/texts/' % nxt.course, 'data/plans/ela-texts.csv') if nxt and nxt.ela else ()
        self.parallel_paths = allowed + text_paths
        try:
            self.start_bg_prep(nxt, previous)
            if not combined and not legacy_key and not self.stage_done(unit, 'key-with-carry'):
                self.mark('%s:key-with-carry' % unit)
            self.start(unit, stage)
            with quota_guard(allowed, self.dry):
                sid = None
                if not landed:
                    _, sid = self.run_claude(unit, stage, prompt)
                newn = self.gated(unit, stage, sid=sid, recovery_prompt=prompt)
            if not self.dry and (not all(p.exists() for p in reports) or
                                 (not legacy_key and not all(report_changes(p) for p in reports))):
                raise Stop('%s %s left an incomplete report: %s' % (unit, stage, ', '.join(map(str, reports))))
            if not self.dry and not unit.green():
                raise Stop('%s %s left missing section plans, unit items or key report' % (unit, stage))
            self.finish(unit, stage, allowed, before, newn)
            self.record_carry(unit)
            self.pileup(unit)
            self.log('unit %s green%s' % (unit, ' (dry)' if self.dry else ''))
            return True
        except ClaudeLimit as exc:
            self.cooldown = reset_time(str(exc), time.time())
            save_state(self.dir / 'claude-cooldown.json', self.cooldown)
            self.log('%s %s: Claude usage limit; cooldown until %s' % (unit, stage, dt.datetime.fromtimestamp(self.cooldown)))
            return False
        finally:
            self.reviewing = None
            # The caller joins prep before any further stage, including a quota drain.

    def codex_unit(self, unit, previous):
        self.check_stop()
        if unit.missing_plans() or self.started(unit, 'write'):
            self.texts(unit)
            self.prep(unit, previous)
            carry = self.feedback(unit)
            written = self.write(unit, changed_list(previous, carry, unit.course))
            if written == len(unit.names):
                for item in carry:
                    self.mark('%s:write-carry:%s' % (unit, item['unit']))
            self.pileup(unit)
        if self.stage_done(unit, 'write'):
            self.crefine(unit)
            self.texts(unit, second=True)
        self.data(unit)
        self.pileup(unit)
        self.mark('%s:codex-done' % unit)
        self.log('unit %s codex-done' % unit)

    def run(self, limit=None):
        old = cl.LANES_DIR / self.subj
        if not self.dry and old.exists() and not (old / 'STOP').exists() and not (cl.LANES_DIR / 'STOP').exists():
            raise Stop('the codex_lane %s lane has no STOP file; stop it first (build/lanes/%s/STOP)' % (self.subj,
                                                                                                         self.subj))
        stopped = self.dir / 'STOPPED'
        if stopped.exists() and not self.dry:
            stopped.rename(self.dir / ('STOPPED-%s.txt' % dt.datetime.now().strftime('%Y%m%d-%H%M%S')))
        cl.keep_awake(True)
        units, why = course_inventory(self.subj)
        previous = dict(zip(units, [None] + units[:-1]))
        marks = self.done()
        work = []
        for u in units:
            state = unit_state(u, marks, check_tracked=not self.dry)
            if state != 'green':
                work.append((u, state))
            elif any('%s:%s-start' % (u, stage) in marks for stage in ('claude', 'key')):
                self.record_carry(u)   # also recovers a crash just after committing the pass
        if limit:
            sample = work[:limit]
            if self.dry and limit > 1 and sample and not any(u.missing_plans() for u, _ in sample):
                example = next((pair for pair in work[limit:] if pair[0].missing_plans()), None)
                if example:
                    self.log('DRY sample includes %s to show the stages for unwritten plans' % example[0])
                    sample[-1] = example
            work = sample
        backlog = deque(u for u, state in work if state == 'backlog')
        if backlog and (self.dir / 'done.txt').exists():
            order = {}
            for mark in (self.dir / 'done.txt').read_text(encoding='utf-8').splitlines():
                if mark.endswith((':data', ':codex-done')):
                    order.setdefault(mark.rsplit(':', 1)[0], len(order))
            backlog = deque(sorted(backlog, key=lambda u: order.get(u.key, len(order))))
        todo = deque(u for u, state in work if state == 'todo')
        for u in backlog:
            if not self.stage_done(u, 'codex-done'):
                self.mark('%s:codex-done' % u)
        self.log('section run starts%s: %d Codex units, %d awaiting Claude%s' % (
            ' (DRY)' if self.dry else '', len(todo), len(backlog), '; after drain: %s' % why if why else ''))
        self.schedule(todo, backlog, previous)
        if why and not limit:
            raise Stop(why)
        self.log('section run finished: %s units done%s' % (self.subj, ' (dry sample)' if self.dry else ''))
        cl.keep_awake(False)

    def schedule(self, todo, backlog, previous):
        """One foreground stage at a time. Recover an interrupted job before another unit edits shared rows."""
        resume_review = bool(backlog) and any(self.started(backlog[0], s) for s in ('claude', 'key'))
        resume_codex = bool(todo) and any(self.started(todo[0], s) for s in
                                          ('write', 'crefine', 'refine', 'texts2', 'data', 'data-a', 'data-b'))
        retry = 0
        while todo or backlog:
            self.check_stop()
            limited = time.time() < retry
            try:
                if not limited and not (resume_review and time.time() >= self.cooldown and not resume_codex):
                    if not resume_codex:
                        self.sweep(backlog)
                    resume_codex = False
                    if todo:
                        unit = todo[0]
                        self.codex_unit(unit, previous[unit])
                        backlog.append(todo.popleft())
                        self.sweep(backlog)  # includes a unit that had no prep or write
                    retry = 0
                if backlog and time.time() >= self.cooldown:
                    resume_review = False
                    nxt = todo[0] if todo and not limited else None
                    if self.claude_pass(backlog[0], nxt, previous.get(nxt)):
                        backlog.popleft()
                    try:
                        self.join_bg()
                    finally:
                        self.parallel_paths = ()
                elif limited or not todo:
                    deadlines = ([retry] if limited else []) + ([self.cooldown] if backlog else [])
                    if deadlines:
                        self.wait_until(min(deadlines))
            except CodexLimit as exc:
                if not backlog:
                    raise
                retry = time.time() + 3600
                self.log('%s; draining Claude backlog, Codex retry at %s' % (exc, dt.datetime.fromtimestamp(retry)))

    def wait_until(self, deadline):
        while time.time() < deadline:
            self.check_stop()
            time.sleep(max(0, min(30, deadline - time.time())))


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
        marks = set((d / 'done.txt').read_text(encoding='utf-8').splitlines()) if (d / 'done.txt').exists() else set()
        units, _ = course_inventory(subj)
        states = {u: unit_state(u, marks) for u in units}
        green = sum(state == 'green' for state in states.values())
        backlog = [u for u in units if states[u] == 'backlog']
        cooldown = read_state(d / 'claude-cooldown.json', 0)
        seen = {m.split(':prep-carry:', 1)[1] for m in marks if ':prep-carry:' in m}
        carry = read_state(d / 'carry.json', [])
        pending = sum(any(u.course == item['unit'].split(':')[0] and (
            (states[u] == 'todo' and u.missing_plans() and item['unit'] not in seen) or
            (states[u] == 'backlog' and u.key != item['unit'] and u.key not in item['applied_to'] and
             '%s:write-carry:%s' % (u, item['unit']) not in marks)) for u in units) for item in carry)
        print('      codex-done %d, green %d, backlog %d, Claude cooldown until %s, carry items pending %d' %
              (green + len(backlog), green, len(backlog),
               dt.datetime.fromtimestamp(cooldown).isoformat(sep=' ', timespec='seconds') if cooldown > time.time()
               else 'none', pending))
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
