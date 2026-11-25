"""Line-level census of the <!-- skel --> blocks in written plans, sorted by cause (consolidation 4.E2 step 1).

    python -X utf8 scripts/skel_census.py [<course> ...] [--out DIR] [--pickaxe]

Report only: changes no plan. For every line inside a plan's skel blocks that is not in today's fresh render of that
plan's skeleton (compared by content, so a moved block counts once), the cause is one of:
  stale       the line is in a generated version from git history (unit plans: the first committed version and the
              version of each scripted regeneration; section plans: every committed version of the section skeleton
              sidecar); data or the generator changed since, so data wins.
  unit-prose  (section plans) the line is quoted from the unit plan sNN.md (any committed version or today's): its owner
              is the unit plan, nothing to do here.
  pickaxe     (--pickaxe, plans with no generated baseline) `git log -S` finds the line's text added to a data file or a
              generator script: a stale copy.
              A line is also stale (the why column says which) when, against the closest line of today's render, it
              adds no words, its extra words (three or more each) are in the course's data files, or an older generator
              printed them (`git log -S` in scripts/).
  hand        anything else: typed into the block by a writer. Each goes on the review list with a suggested outcome:
              back-port (a fact the data lacks or has wrong), move (judgment, to the plan's prose), discard (data
              wins), or check (needs a look).
Writes DIR/census.csv (every non-fresh line), DIR/hand-list.csv (hand lines with a suggestion and a group id),
DIR/groups.md (the hand lines by group, for marking a group at a time) and DIR/summary.md.
Default DIR: docs/reviews/consolidation/step4-E2.
"""
import collections
import csv
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skel_drift as sd   # noqa: E402

ROOT = sd.ROOT
DOCS = sd.DOCS
REGEN = ['8dd354eed']        # scripted in-place regenerations of unit plans (git log, 2026-11-25)


class Git:
    def __init__(self):
        self.p = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=ROOT, stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE)

    def show(self, rev, path):
        self.p.stdin.write(('%s:%s\n' % (rev, path)).encode())
        self.p.stdin.flush()
        head = self.p.stdout.readline().decode()
        if head.endswith('missing\n'):
            return None
        n = int(head.split()[2])
        data = self.p.stdout.read(n)
        self.p.stdout.read(1)
        return data.decode('utf-8', 'replace').replace('\r\n', '\n')


def revs(path):
    out = subprocess.run(['git', 'log', '--format=%H', '--', path], cwd=ROOT, capture_output=True, text=True).stdout
    return out.split()


def norm(s):
    return ' '.join(s.split())


def block_lines(text):
    return [norm(x) for b in sd.blocks(text) for x in b.splitlines() if norm(x)]


def all_lines(text):
    return {norm(x) for x in (text or '').splitlines() if norm(x)}


def numless(s):
    return re.sub(r'\d+(\.\d+)?', '#', s)


ORDER_NOTE = re.compile(r'^(none|(no )?(source )?(lesson )?order( conflict| retained| preserved| kept| unchanged)?|(original|source) order '
                        r'(retained|preserved|kept)|order retained|keep|ours|adapt|replace|split|cut|merge|reorder(ed)?|'
                        r'original [a-z ]+ (with)?in (the )?reserved (days|slot))$')


def decision(line):
    m = re.search(r': our days [\d, to-]*(?:;\s*[\d, to-]+)*;\s*([a-z]+)', line or '')   # days may be "13; 14"
    return m.group(1) if m else None


def suggest(line, fresh_numless, extra='', near=''):
    low = line.lower()
    if decision(line):                                      # a source row
        if decision(near) and decision(near) != decision(line):
            return 'check', 'the plan says %s, data says %s (data wins unless the plan is the later ruling)' % (
                decision(line), decision(near))
        notes = [y.strip(' ;,.') for y in extra.lower().replace(' ... ', ';').split(';') if y.strip(' ;,.')]
        notes = [n for n in notes if not re.fullmatch(r'[\d, to-]+', n)]     # day numbers, written another way
        if notes and all(ORDER_NOTE.match(n) for n in notes):
            return 'discard', 'the writer confirmed source order: nothing a teacher needs'
        if notes:
            return 'back-port', 'a writer\'s note on a source row: goes to the source-map note column'
    if numless(line) in fresh_numless:
        return 'discard', 'only numbers differ from data (data wins); check it is not a deliberate budget'
    code = re.match(r'^- \*\*~?([A-Za-z0-9][\w.-]*):\*\*', line)
    if code and near.startswith('- **') and code.group(1) in near:
        if 'no own-word line' in near:
            return 'back-port', 'the writer\'s own words for a standard the data has none for: goes to the standards file'
        return 'check', 'the writer reworded a standard the data already words (data wins unless the plan\'s is better)'
    if near and extra and len(extra.replace('...', ' ').split()) <= 2:
        return 'discard', 'a one- or two-word wording change from data (data wins)'
    if re.search(r'source-map|\bcredit\b|\bdecision\b', low) or line.startswith('| s') and 'http' in low:
        return 'check', 'source row typed by the writer: compare with source-map.csv'
    if re.search(r'\(a\)|\bparts?\b.*\bdays?\b|\bsplit\b', low):
        return 'move', 'the writer\'s split of a standard across days (judgment)'
    if re.search(r'\bminutes?\b|\btime\b|\bbudget\b|\bweight', low):
        return 'move', 'time or weight budget (judgment)'
    if re.search(r'sensitiv|slur|trauma|omit|teacher note|caution|warning', low):
        return 'back-port', 'a sensitivity or teacher note: goes to the frame'
    if re.search(r'\ballocation\b|\breused evidence\b|\brecord\b', low):
        return 'move', 'record or evidence allocation (judgment)'
    return 'check', ''


def format_only(line, fresh_text):
    """The generator's wording changed, not the fact: with the bold label and its parenthetical taken off, the rest of
    the line (at least 60 characters, such as a standard's own words) stands in today's render."""
    rest = re.sub(r'^[-*>|\s]*\*\*[^*]+\*\*\s*(\([^)]*\)\s*)?', '', line).strip()
    return len(rest) >= 60 and rest in fresh_text


def closest(line, fresh):
    """Today's rendered line that this plan line most resembles (same bold label when it has one), and the words only the
    plan has: what a reviewer compares."""
    import difflib
    lab = re.match(r'^[-*>|\s]*(\*\*[^*]+\*\*)', line)
    pool = [x for x in fresh if lab and lab.group(1).split(':')[0] in x] or list(fresh)
    best = difflib.get_close_matches(line, pool, n=1, cutoff=0.4)
    if not best:
        return '', ''
    a, b = best[0].split(), line.split()
    sm = difflib.SequenceMatcher(None, a, b)
    only = [' '.join(b[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op in ('insert', 'replace')]
    return best[0], ' ... '.join(only)[:400]


_data = {}
_hist = {}


def course_data(c):
    """All of a course's plan data, lowercased and space-normalized (where a source decision's note lives)."""
    if c not in _data:
        d = ROOT / 'data' / 'plans' / c
        _data[c] = ' '.join(norm(p.read_text(encoding='utf-8', errors='replace')).lower()
                            for p in sorted(d.glob('*.csv'))) if d.exists() else ''
    return _data[c]


def script_hist(frag):
    """`git log -S` finds this text in a generator script's history: an older generator printed it."""
    if frag not in _hist:
        out = subprocess.run(['git', 'log', '-S', frag, '--format=%H', '-1', '--', 'scripts'], cwd=ROOT,
                             capture_output=True, text=True).stdout
        _hist[frag] = bool(out.strip())
    return _hist[frag]


def pickaxe(line):
    words = re.findall(r"[A-Za-z][A-Za-z'-]{3,}", line)
    probe = ' '.join(words[:6]) if len(words) >= 3 else None
    if not probe:
        return False
    out = subprocess.run(['git', 'log', '-S', probe, '--format=%H', '-1', '--', 'data', 'scripts'], cwd=ROOT,
                         capture_output=True, text=True).stdout
    return bool(out.strip())


SUBJECT = {'math': 'math', 'algebra': 'math', 'geometry': 'math', 'precalculus': 'math', 'calculus': 'math',
           'statistics': 'math', 'english': 'ela', 'science': 'science', 'biology': 'science', 'chemistry': 'science',
           'physics': 'science', 'earth': 'science', 'environmental': 'science'}


def subject(plan):
    c = plan.split('/')[2]
    return SUBJECT.get(c.split('-')[0], 'social studies')


def write_groups(out, head, hand):
    """Hand lines grouped by suggested outcome, its reason and subject: the unit Cory marks (one mark per group, or
    a line-level mark in hand-list.csv where a group needs splitting)."""
    order = {'back-port': 0, 'move': 1, 'check': 2, 'discard': 3}
    def key(r):
        why = re.sub(r'the plan says \w+, data says \w+', "the plan's source decision differs from data", r[5])
        return order.get(r[4], 9), why, subject(r[0])
    keys = sorted({key(r) for r in hand})
    gid = {k: 'G%02d' % (i + 1) for i, k in enumerate(keys)}
    with open(out / 'hand-list.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(['group'] + head + ['cory'])
        w.writerows([gid[key(r)]] + r + [''] for r in sorted(hand, key=lambda r: (gid[key(r)], r[0])))
    md = ['# Hand-edited skel lines by group (consolidation 4.E2 step 2)', '',
          'Each group is one suggested outcome, its reason and one subject. Mark a group with back-port, move, discard or',
          'check (or "split" and mark its lines in hand-list.csv, column `cory`). back-port: the fact goes into data.',
          'move: the line goes into the plan\'s own prose. discard: data wins. check: a look at the line decides.', '']
    for k in keys:
        rs = [r for r in hand if key(r) == k]
        cs = sorted({r[0].split('/')[2] for r in rs})
        md += ['## %s: suggest %s, %s (%d lines, %d courses)' % (gid[k], rs[0][4], k[2], len(rs), len(cs)), '',
               'Why: %s.' % (k[1] or 'no pattern matched; read the lines'), '',
               'Courses: %s.' % ', '.join(cs), '']
        for r in rs[:4]:
            md.append('- `%s`: %s' % (r[0][13:], r[6][:260].replace('|', '/')))
            if r[8]:
                md.append('  - only in the plan: %s' % r[8][:200].replace('|', '/'))
        md.append('')
    (out / 'groups.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    return gid


def regroup(out):
    with open(out / 'census.csv', encoding='utf-8', newline='') as f:
        rs = list(csv.reader(f))
    hand = [r for r in rs[1:] if r[3] == 'hand']
    for r in hand:       # suggestions again from the saved columns (the numbers-only test needs the render: kept)
        if not r[5].startswith('only numbers'):
            r[4], r[5] = suggest(r[6], set(), r[8], r[7])
    write_groups(out, rs[0], hand)
    with open(out / 'census.csv', 'w', encoding='utf-8', newline='') as f:
        csv.writer(f, lineterminator='\n').writerows(rs)
    return 0


def main(a):
    out = ROOT / 'docs' / 'reviews' / 'consolidation' / 'step4-E2'
    if '--out' in a:
        i = a.index('--out')
        out, a = Path(a[i + 1]), a[:i] + a[i + 2:]
    if a == ['--regroup']:
        return regroup(out)
    use_pick = '--pickaxe' in a
    a = [x for x in a if x != '--pickaxe']
    cs = a or sorted(p.name for p in DOCS.iterdir() if p.is_dir())
    g = Git()
    rows, cnt, per_course = [], collections.Counter(), collections.defaultdict(collections.Counter)
    plans = lines_total = 0
    for c in cs:
        for p in sorted((DOCS / c).glob('*.md')):
            m = re.fullmatch(r's(\d+)\.md|u(\d+)-(\d+)\.md', p.name)
            if not m:
                continue
            text = p.read_text(encoding='utf-8').replace('\r\n', '\n')
            have = block_lines(text)
            if not have:
                continue
            plans += 1
            lines_total += len(have)
            rendered = sd.fresh(c, p.name)
            fresh_text = ' | '.join(norm(x) for x in rendered.splitlines())
            fresh = all_lines(rendered)
            fresh_nl = {numless(x) for x in fresh}
            rel = p.relative_to(ROOT).as_posix()
            gen, prose, baseline = set(), set(), False
            if m.group(1):                       # unit plan: first version and scripted regenerations
                rv = revs(rel)
                t0 = g.show(rv[-1], rel) if rv else None
                if t0 and 'TODO(writer)' in t0:          # first committed as a raw skeleton
                    gen |= all_lines(t0)
                    baseline = True
                for x in REGEN:                          # only the lines a regeneration wrote, not ones it kept
                    if any(y.startswith(x) for y in rv):
                        gen |= all_lines(g.show(x, rel)) - all_lines(g.show(x + '^', rel))
            else:                                # section plan: every committed sidecar, and the unit plan's text
                side = 'docs/courses/%s/section-skeletons/%s' % (c, p.name)
                for r in revs(side):
                    gen |= all_lines(g.show(r, side))
                    baseline = True
                unit = 'docs/courses/%s/s%02d.md' % (c, int(m.group(2)))
                prose |= all_lines((DOCS / c / ('s%02d.md' % int(m.group(2)))).read_text(encoding='utf-8')
                                   if (DOCS / c / ('s%02d.md' % int(m.group(2)))).exists() else '')
                for r in revs(unit):
                    prose |= all_lines(g.show(r, unit))
            seen = set()
            for ln in have:
                if ln in fresh or ln in seen:
                    continue
                seen.add(ln)
                if ln in gen or format_only(ln, fresh_text):
                    cause = 'stale'
                elif ln in prose:
                    cause = 'unit-prose'
                elif use_pick and not baseline and pickaxe(ln):
                    cause = 'pickaxe'
                else:
                    cause = 'hand'
                near, extra = closest(ln, fresh) if cause == 'hand' else ('', '')
                why = ''
                if cause == 'hand' and not near:     # nothing like it today: is the text after the label old output?
                    rest = re.sub(r'^[-*>|\s]*\*\*[^*]+\*\*\s*', '', ln).strip(' ;,.:()')
                    if len(rest) >= 12 and rest != ln and script_hist(rest):
                        cause, why = 'stale', 'an older generator printed this text'
                if cause == 'hand' and near:
                    frags = [y.strip(' ;,.:()') for x in extra.split(' ... ') for y in x.split(';')]
                    frags = [x for x in frags if len(x) >= 4]
                    if not frags:
                        cause, why = 'stale', 'adds no words to today\'s render'
                    elif all(len(x.split()) >= 3 and norm(x).lower() in course_data(c) for x in frags):
                        cause, why = 'stale', 'its extra words are in the course\'s data files'
                    elif all(script_hist(x) for x in frags):
                        cause, why = 'stale', 'its extra words were printed by an older generator'
                if cause == 'hand':
                    s, why = suggest(ln, fresh_nl, extra, near)
                else:
                    s, near, extra = '', ('' if not why else near), ('' if not why else extra)
                cnt[cause] += 1
                per_course[c][cause] += 1
                rows.append([rel, 'unit' if m.group(1) else 'section', 'yes' if baseline else 'no', cause, s, why, ln,
                             near, extra])
    out.mkdir(parents=True, exist_ok=True)
    head = ['plan', 'type', 'baseline', 'cause', 'suggest', 'why', 'line', 'data_says', 'plan_only_words']
    with open(out / 'census.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(head)
        w.writerows(rows)
    hand = [r for r in rows if r[3] == 'hand']
    write_groups(out, head, hand)
    sug = collections.Counter(r[4] for r in hand)
    nb = sum(1 for r in hand if r[2] == 'no')
    md = ['# Skel census by cause (consolidation 4.E2 step 1)', '',
          'Command: `python -X utf8 scripts/skel_census.py%s` (report only).' % (' --pickaxe' if use_pick else ''), '',
          '- %d written plans with skel blocks, %d block lines; %d distinct lines per plan are not in today\'s fresh render.'
          % (plans, lines_total, len(rows)),
          '- By cause: ' + ', '.join('%s %d' % (k, cnt[k]) for k in ('stale', 'unit-prose', 'pickaxe', 'hand')) + '.',
          '- Hand lines by suggested outcome: ' + ', '.join('%s %d' % (k or 'none', v) for k, v in sug.most_common()) + '.',
          '- Hand lines in plans with no generated baseline in git (social studies unit plans and others): %d.' % nb, '',
          '| Course | stale | unit-prose | pickaxe | hand |', '|---|---|---|---|---|']
    for c in sorted(per_course):
        k = per_course[c]
        md.append('| %s | %d | %d | %d | %d |' % (c, k['stale'], k['unit-prose'], k['pickaxe'], k['hand']))
    (out / 'summary.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('\n'.join(md[:8]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
