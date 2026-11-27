"""Local-model day drafting pilot (Cory 2026-11-26: set up, do not run yet). See docs/pipeline/LOCAL-DRAFT-PILOT.md.

    python -X utf8 scripts/local_draft.py prompts [<course> <days>]   build the prompts only (no model call)
    python -X utf8 scripts/local_draft.py draft   [<course> <days>]   call the local model, write the drafts
    python -X utf8 scripts/local_draft.py check   [<course> <days>]   run lesson.py's day checks on the drafts
    python -X utf8 scripts/local_draft.py compare [<course> <days>]   size and overlap against the signed-off days
    python -X utf8 scripts/local_draft.py sec-prompts|sec-draft [<course> <units>]   section plans (math-grade-1 u1)
    python -X utf8 scripts/local_draft.py sec-check [<course> <units> [drafts|fixed|refined|fresh]]

<days> is a list or ranges, e.g. 1-8 or 1,3,7. With no course the pilot set is used: science-grade-1 days 1 to 8
(unit 1, sections 1.1 and 1.2; science K to 3 was signed off by Cory 2026-11-23, so every day has a known-good twin).

The model fills only what scripts/day_skeleton.py leaves as TODO(writer); every mechanical field comes from the
skeleton. It never sees the signed-off day it is drafting. It does see one signed-off day of the same kind from
another course as an example of the shape. Everything is written under build/local-pilot/ (git-ignored); nothing
touches courses/, data/ or docs/. The model is the coder backend on this PC: S:\\AI\\Start-Coder.bat (KoboldCpp,
gpt-oss-20b, OpenAI-compatible API on port 5003, 32k context). Run it alone on the GPU.
"""
import difflib
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'build' / 'local-pilot'
API = 'http://localhost:5003/v1'
MODEL = 'gpt-oss-20b'
CONTEXT = 32768
MAX_OUT = 7000
PILOT = ('science-grade-1', '1-8')
EXAMPLE_COURSE = 'science-grade-2'    # signed off with K to 3 science; same family, never the drafted course
# LESSON-DAY sections left out of the prompt: they describe our scripts or point at files the model cannot open
SKIP_SECTIONS = ('What the script checks', 'Not decided here', 'The worked case')


def days_arg(s):
    out = []
    for part in s.split(','):
        a, _, b = part.partition('-')
        out += list(range(int(a), int(b or a) + 1))
    return out


def tokens(text):
    return len(text) // 3   # rough; English markdown runs about 3.5 to 4 characters a token, so this errs high


def day_file(course, day):
    hits = sorted((ROOT / 'courses' / course).glob('u*/d%03d.md' % day))
    return hits[0] if hits else None


def day_row(course, day):
    import csv
    with open(ROOT / 'data' / 'plans' / course / 'days.csv', encoding='utf-8', newline='') as f:
        return next((r for r in csv.DictReader(f) if r['day'] == str(day)), None)


def lesson_rules():
    text = (ROOT / 'docs' / 'courses' / 'LESSON-DAY.md').read_text(encoding='utf-8')
    parts = re.split(r'(?=^## )', text, flags=re.M)
    return ''.join(p for p in parts if not any(p.startswith('## ' + s) for s in SKIP_SECTIONS)).strip()


def skeleton(course, day):
    out = OUT / 'skeletons'
    subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'scripts' / 'day_skeleton.py'), course, str(day),
                    '--out', str(out)], check=True, capture_output=True, cwd=ROOT)
    return (out / course / ('d%03d.md' % day)).read_text(encoding='utf-8')


def section_block(course, day):
    import day_skeleton
    r = day_row(course, day)
    return (day_skeleton.section_block(course, r, day) or '') if r else ''


def example(kind):
    """One signed-off day of the same kind from EXAMPLE_COURSE: the shape to copy, never the content."""
    import csv
    with open(ROOT / 'data' / 'plans' / EXAMPLE_COURSE / 'days.csv', encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            p = day_file(EXAMPLE_COURSE, int(r['day']))
            if r['kind'] == kind and p:
                return p
    return None


SYSTEM = """You write one teaching day for Curio Class, a free K-12 curriculum. You are given:
1. The rules every day file follows (LESSON-DAY).
2. A skeleton for this day. Lines between <!-- skel --> markers are facts from our data: keep them exactly, do not
   invent other standards, supplies, links or ids. Every TODO(writer) is yours to write.
3. The section plan's block for this day.
4. One finished day from another course, only as an example of the shape and tone. Do not copy its content.

Write the finished day file and nothing else: it starts with the --- header block and ends with the student page.
Rules: US spelling, no em dashes, write "Curio Class" in full, plain words a teacher reads aloud, the minutes of the
time blocks add up to the day, questions are named only by their [[id]] (never write an answer key), lean only on
files the skeleton names, and no timer without a stated purpose."""


def build_prompt(course, day):
    r = day_row(course, day)
    ex = example(r['kind'])
    user = '\n\n'.join([
        '# 1. Rules (docs/courses/LESSON-DAY.md)\n\n' + lesson_rules(),
        '# 2. Skeleton for %s day %d\n\n' % (course, day) + skeleton(course, day),
        '# 3. Section plan block\n\n' + (section_block(course, day) or '(no section plan block for this day)'),
        '# 4. Example day (shape only): %s\n\n' % (ex.relative_to(ROOT).as_posix() if ex else 'none')
        + (ex.read_text(encoding='utf-8') if ex else ''),
    ])
    return [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': user}]


def prompts(course, days, write=True):
    rows = []
    for d in days:
        msgs = build_prompt(course, d)
        n = sum(tokens(m['content']) for m in msgs)
        ok = n + MAX_OUT <= CONTEXT
        rows.append((d, n, ok))
        if write:
            p = OUT / 'prompts' / course / ('d%03d.json' % d)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(msgs, ensure_ascii=False, indent=1), encoding='utf-8')
        print('  day %3d: about %5d prompt tokens + %d out = %s' % (d, n, MAX_OUT, 'fits' if ok else 'TOO BIG'))
    return rows


def server_up():
    try:
        urllib.request.urlopen(API + '/models', timeout=5).read()
        return True
    except Exception:
        return False


def call(msgs):
    body = json.dumps(dict(model=MODEL, messages=msgs, max_tokens=MAX_OUT, temperature=0.4)).encode('utf-8')
    req = urllib.request.Request(API + '/chat/completions', body, {'Content-Type': 'application/json',
                                                                   'Authorization': 'Bearer local'})
    with urllib.request.urlopen(req, timeout=3600) as resp:
        out = json.loads(resp.read().decode('utf-8'))
    text = out['choices'][0]['message'].get('content') or ''
    i = text.find('---\n')            # drop any reasoning or preamble before the header block
    return (text[i:] if i >= 0 else text).strip() + '\n', out.get('usage', {})


def draft_path(course, day):
    real = day_file(course, day)
    folder = real.parent.name if real else 'u00-0'
    return OUT / 'drafts' / course / folder / ('d%03d.md' % day)


def draft(course, days):
    if not server_up():
        raise SystemExit('The local model is not answering on %s. Start S:\\AI\\Start-Coder.bat (alone on the GPU) '
                         'and run this again.' % API)
    log = OUT / 'drafts' / 'log.csv'
    log.parent.mkdir(parents=True, exist_ok=True)
    new = not log.exists()
    with open(log, 'a', encoding='utf-8') as f:
        if new:
            f.write('course,day,seconds,prompt_tokens,completion_tokens\n')
        for d in days:
            t = time.time()
            text, use = call(build_prompt(course, d))
            p = draft_path(course, d)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding='utf-8')
            s = round(time.time() - t)
            f.write('%s,%d,%d,%s,%s\n' % (course, d, s, use.get('prompt_tokens', ''), use.get('completion_tokens', '')))
            f.flush()
            print('  day %3d: %ds, %s' % (d, s, p.relative_to(ROOT).as_posix()))


def check(course, days):
    import lesson
    items, rows, *_ = lesson.load(course)
    total = 0
    for d in days:
        p = draft_path(course, d)
        if not p.exists():
            print('  day %3d: no draft' % d); continue
        parsed = lesson.parse(p)
        fails = ['no header block'] if parsed is None else [x for x in lesson.check_day(parsed, items, rows)
                                                             if not x.startswith('NOTE ')]
        total += len(fails)
        print('  day %3d: %d failures' % (d, len(fails)))
        for x in fails:
            print('      ', x)
    print('  %d failures in all' % total)


def words(t):
    return re.findall(r"[A-Za-z0-9']+", t.lower())


def compare(course, days):
    print('  day  draft words  signed-off words  word overlap')
    for d in days:
        p, real = draft_path(course, d), day_file(course, d)
        if not (p.exists() and real):
            print('  %3d  (missing)' % d); continue
        a, b = words(p.read_text(encoding='utf-8')), words(real.read_text(encoding='utf-8'))
        r = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
        print('  %3d  %11d  %16d  %11.2f' % (d, len(a), len(b), r))
    print('  Overlap only says how far apart the texts are, not which is better; quality is judged by the fix '
          'pass and the side-by-side read (LOCAL-DRAFT-PILOT.md).')


# ---------------------------------------------------------------- section plans (Cory 2026-11-26: "the pilot for
# sections only"; math-grade-1 unit 1). Prep (Claude) -> local draft -> cheap fix -> refine; see LOCAL-DRAFT-PILOT.md.
SEC = OUT / 'sec'
SEC_MAX_OUT = 14000
SEC_PILOT = ('math-grade-1', '1')


def doc_parts(path, heads):
    text = (ROOT / path).read_text(encoding='utf-8')
    parts = re.split(r'(?=^## )', text, flags=re.M)
    return '\n'.join(p.strip() for p in parts if any(p.startswith('## ' + h) for h in heads))


SEC_SYSTEM = """Reasoning: low

You write one section plan for Curio Class, a free K-12 curriculum, for the teacher who will teach it. You are given:
1. The rules for section plans (from UNIT-PLAN.md and the section-write brief).
2. The course defaults (what holds every day; write only what differs).
3. A prep note from the lead: the decisions for this section (cases, exits, errors, routines). Follow it.
4. The skeleton. Lines between <!-- skel --> markers are facts from our data: never copy them into the plan and
   never contradict them. Every TODO(writer) is yours: replace it with finished prose under the same heading.

Write the finished section plan file and nothing else, from its first # heading to field 11, in the skeleton's
headings, with no <!-- skel --> markers and no TODO left. Rules: US spelling, no em dashes, "Curio Class" in full,
plain words, every number and key solved before it is written, each wrong answer tagged with one error letter, the
`- **N min. Part.**` lines of each day add up to the day's minutes, and nothing invented that the prep note or the
skeleton does not give (say "source to check" instead)."""


def sec_prompt(course, sec):
    skel = ROOT / 'docs' / 'courses' / course / 'section-skeletons' / ('%s.md' % sec)
    prep = SEC / 'prep' / course / ('%s.md' % sec)
    if not prep.exists():
        raise SystemExit('no prep note: %s (the Claude prep pass writes it first)' % prep.relative_to(ROOT))
    rules = '\n\n'.join([doc_parts('docs/courses/UNIT-PLAN.md', ('The rules', 'The section plan: fields', 'Length')),
                         doc_parts('docs/pipeline/briefs/section-write.md', ('Write', 'Rules from the probes'))])
    user = '\n\n'.join([
        '# 1. Rules\n\n' + rules,
        '# 2. Course defaults (docs/courses/%s/DEFAULTS.md)\n\n' % course
        + (ROOT / 'docs' / 'courses' / course / 'DEFAULTS.md').read_text(encoding='utf-8'),
        '# 3. Prep note for %s\n\n' % sec + prep.read_text(encoding='utf-8'),
        '# 4. Skeleton for %s\n\n' % sec + skel.read_text(encoding='utf-8'),
    ])
    return [{'role': 'system', 'content': SEC_SYSTEM}, {'role': 'user', 'content': user}]


def sections(course, units):
    out = []
    for u in units:
        subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'scripts' / 'section_skeleton.py'), course,
                        'u%d' % u], check=True, capture_output=True, cwd=ROOT)
        out += sorted(p.stem for p in (ROOT / 'docs' / 'courses' / course / 'section-skeletons').glob('u%02d-*.md' % u))
    return out


def sec_prompts(course, units):
    for sec in sections(course, units):
        msgs = sec_prompt(course, sec)
        n = sum(tokens(m['content']) for m in msgs)
        print('  %s: about %5d prompt tokens + %d out = %s' % (sec, n, SEC_MAX_OUT,
              'fits' if n + SEC_MAX_OUT <= CONTEXT else 'TOO BIG'))


def strip_reasoning(text):
    i = 0 if text.startswith('# ') else text.find('\n# ')
    text = (text[i:] if i >= 0 else text).strip() + '\n'
    # mechanical only: the model writes non-breaking and figure hyphens and narrow spaces for plain ones
    for a, b in (('‑', '-'), ('‐', '-'), ('‒', '-'), (' ', ' '), (' ', ' ')):
        text = text.replace(a, b)
    return text


def sec_draft(course, units):
    if not server_up():
        raise SystemExit('The local model is not answering on %s. Start S:\\AI\\Start-Coder.bat.' % API)
    log = SEC / 'drafts' / 'log.csv'
    log.parent.mkdir(parents=True, exist_ok=True)
    new = not log.exists()
    with open(log, 'a', encoding='utf-8') as f:
        if new:
            f.write('course,section,seconds,prompt_tokens,completion_tokens\n')
        for sec in sections(course, units):
            t = time.time()
            body = json.dumps(dict(model=MODEL, messages=sec_prompt(course, sec), max_tokens=SEC_MAX_OUT,
                                   temperature=0.4)).encode('utf-8')
            req = urllib.request.Request(API + '/chat/completions', body, {'Content-Type': 'application/json',
                                                                           'Authorization': 'Bearer local'})
            with urllib.request.urlopen(req, timeout=7200) as resp:
                out = json.loads(resp.read().decode('utf-8'))
            raw = out['choices'][0]['message'].get('content') or ''
            p = SEC / 'drafts' / course / ('%s.md' % sec)
            p.parent.mkdir(parents=True, exist_ok=True)
            (p.parent / ('%s.raw.txt' % sec)).write_text(raw, encoding='utf-8')
            p.write_text(strip_reasoning(raw), encoding='utf-8')
            use, s = out.get('usage', {}), round(time.time() - t)
            f.write('%s,%s,%d,%s,%s\n' % (course, sec, s, use.get('prompt_tokens', ''), use.get('completion_tokens', '')))
            f.flush()
            print('  %s: %ds, %s out tokens, %d words' % (sec, s, use.get('completion_tokens', '?'),
                                                         len(words(p.read_text(encoding='utf-8')))))


def sec_check(course, units, stage='drafts'):
    """unitplan.py check on a stage folder (drafts, fixed, refined, fresh), with the real unit plan copied beside."""
    import shutil
    d = SEC / stage / course
    for u in units:
        shutil.copy(ROOT / 'docs' / 'courses' / course / ('s%02d.md' % u), d / ('s%02d.md' % u))
    r = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'scripts' / 'unitplan.py'), 'check', course,
                        '--dir', str(SEC / stage)], capture_output=True, text=True, encoding='utf-8', cwd=ROOT)
    print(r.stdout[-6000:])
    for p in sorted(d.glob('u*-*.md')):
        t = p.read_text(encoding='utf-8')
        print('  %s: %d words, %d TODO, %d skel markers, %d em dashes' % (
            p.name, len(words(t)), t.count('TODO(writer)'), t.count('<!-- skel'), t.count('\u2014')))


def main(a):
    if a and a[0].startswith('sec-'):
        course, spec = (a[1], a[2]) if len(a) >= 3 else SEC_PILOT
        units, cmd = days_arg(spec), a[0][4:]
        if cmd == 'check':
            return sec_check(course, units, a[3] if len(a) > 3 else 'drafts')
        return dict(prompts=sec_prompts, draft=sec_draft)[cmd](course, units)
    if not a or a[0] not in ('prompts', 'draft', 'check', 'compare'):
        raise SystemExit(__doc__)
    course, spec = (a[1], a[2]) if len(a) >= 3 else PILOT
    days = days_arg(spec)
    dict(prompts=prompts, draft=draft, check=check, compare=compare)[a[0]](course, days)


if __name__ == '__main__':
    main(sys.argv[1:])
