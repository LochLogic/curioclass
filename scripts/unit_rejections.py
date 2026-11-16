"""Collect the findings the unit loop's fix step rejected, for the lead to rule on, and apply overruled ones.

Usage:
  python -X utf8 scripts/unit_rejections.py collect          gather new rejections into data/plans/unit-rejections.csv
  python -X utf8 scripts/unit_rejections.py open             print the rows not yet ruled on
  python -X utf8 scripts/unit_rejections.py apply [logdir=]  send each overruled, unapplied row back to Codex to fix
  python -X utf8 scripts/unit_rejections.py calendar <course> [logdir=]  send the course's unapplied `lead` rows to
      Codex with docs/pipeline/briefs/unit-calendar-fix.md (days.csv, scope and sequence, s*.md); run only when no
      other job is writing that course

The fix step (docs/pipeline/briefs/unit-lens-fix.md) ends with one `REJECTED:` line per finding it turned down:
`REJECTED: <lens> <n> | <finding> | <why> | <rule relied on>`. Reports written before that format (2026-11-16) have
free-text rejections; collect takes any line naming a rejection, with format `old`, so nothing is lost.

The lead (Claude) rules in the csv: `ruling` is `upheld` (the rejection stands) or `overruled` (the finding is right;
fix it), with a one-line `note` that becomes Codex's instruction. A ruling that comes from a loosely worded rule also
gets the rule fixed once (UNIT-PLAN or the brief), so the same rejection does not recur. Two more rulings: `lead`
(the finding is right but needs a change outside the unit plan, such as days.csv; the lead makes it) and `noise`
(a line that is not a rejection, from the old free-text format).

apply runs docs/pipeline/briefs/unit-ruling-fix.md once per unit holding overruled rows, through codex_write.py with
only that unit's s<NN>.md allowed, then the unitplan.py gate, and sets `applied` to the date and pass or fail.
"""
import csv
import datetime
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, 'data', 'plans', 'unit-rejections.csv')
COLS = ['report_date', 'course', 'unit', 'lens', 'finding', 'reason', 'rule', 'format', 'ruling', 'note', 'applied']
NAME = re.compile(r'codex-write-fix-(.+)-s(\d\d)-(\d{4}-\d\d-\d\d)\.md$')
COUNT_ONLY = re.compile(r'^\W*(merged|fixed|findings)\b.*\brejected\W*\s*\**\s*\d+\W*$', re.I)
NONE = re.compile(r'rejected\W*\s*\**\s*(0|none|no findings)\b', re.I)
sys.path.insert(0, os.path.join(ROOT, 'scripts'))


def load():
    if not os.path.exists(CSV):
        return []
    with open(CSV, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def parse(text):
    """Rejected findings in one fix report: list of (lens, finding, reason, rule, format)."""
    out = []
    body = text.split('\n## Files changed outside', 1)[0]
    lines = [ln.strip() for ln in body.splitlines()]
    tagged = [ln for ln in lines if ln.startswith('REJECTED:')]
    if tagged:
        for ln in tagged:
            rest = ln[len('REJECTED:'):].strip()
            if rest.lower().startswith('none'):
                continue
            p = [x.strip() for x in rest.split('|')]
            p += [''] * (4 - len(p))
            out.append((p[0], p[1], p[2], p[3], 'new'))
        return out
    i = 0
    while i < len(lines):
        clean = lines[i].replace('*', '').strip('- ').strip()
        i += 1
        low = clean.lower()
        if ('reject' not in low or NONE.search(clean) or COUNT_ONLY.match(clean) or 'held up' in low
                or re.match(r'^(\d+\s+)?(findings\s+)?merged', low)):
            continue
        items = [clean]
        if re.match(r'^rejected(\s+findings)?\W*\s*\d*\s*:?$', low):      # a header: the rejections follow as a list
            items = []
            while i < len(lines) and (not lines[i] or re.match(r'^(-|\d+\.)\s', lines[i])):
                if lines[i]:
                    items.append(re.sub(r'^(-|\d+\.)\s+', '', lines[i]).replace('*', ''))
                elif items:
                    break
                i += 1
        for it in items:
            lens = next((l for l in ('assessment', 'sources', 'sequence') if l in it.lower()), '')
            out.append((lens, it, '', '', 'old'))
    return out


def collect():
    rows = load()
    seen = {(r['report_date'], r['course'], r['unit'], r['finding']) for r in rows}
    added = 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'docs', 'reviews', 'codex-write-fix-*-s??-*.md'))):
        m = NAME.search(os.path.basename(path))
        if not m:
            continue
        course, uu, date = m.groups()
        for lens, finding, reason, rule, fmt in parse(open(path, encoding='utf-8').read()):
            key = (date, course, uu, finding)
            if key in seen:
                continue
            seen.add(key)
            rows.append(dict(report_date=date, course=course, unit=uu, lens=lens, finding=finding, reason=reason,
                             rule=rule, format=fmt, ruling='', note='', applied=''))
            added += 1
    save(rows)
    print('collected %d new rejections; %d open' % (added, sum(1 for r in rows if not r['ruling'])))


def show_open():
    for i, r in enumerate(load()):
        if not r['ruling']:
            print('%d | %s s%s | %s | %s | %s | %s' % (i, r['course'], r['unit'], r['lens'], r['finding'], r['reason'],
                                                      r['rule']))


def apply(opts):
    import codex_units as cu
    rows = load()
    todo = {}
    for r in rows:
        if r['ruling'] == 'overruled' and not r['applied']:
            todo.setdefault((r['course'], r['unit']), []).append(r)
    logdir = opts.get('logdir', os.path.join(ROOT, '..', 'codex-ruling-logs'))
    os.makedirs(logdir, exist_ok=True)
    for (course, uu), rs in todo.items():
        subject, _ = cu.units(course)
        text = ' '.join('(%d) %s Ruling: %s' % (i + 1, r['finding'], r['note']) for i, r in enumerate(rs))
        tag = 'ruling-%s-s%s' % (course, uu)
        subprocess.run([sys.executable, '-X', 'utf8', 'scripts/codex_write.py', 'docs/pipeline/briefs/unit-ruling-fix.md',
                        course, 'unit=%d' % int(uu), 'uu=' + uu, 'writer_brief=' + cu.brief_for(subject),
                        'rulings=' + text, 'allow=docs/courses/{course}/s%s.md' % uu, 'tag=' + tag,
                        'log=' + os.path.join(logdir, tag + '.log')], cwd=ROOT)
        ok = cu.passes(course, uu)
        stamp = '%s %s' % (datetime.date.today().isoformat(), 'pass' if ok else 'FAIL')
        for r in rs:
            r['applied'] = stamp
        save(rows)
        print(course, uu, len(rs), 'rulings applied:', stamp, flush=True)


def calendar(course, opts):
    import codex_units as cu
    rows = load()
    rs = [r for r in rows if r['course'] == course and r['ruling'] == 'lead' and not r['applied']]
    if not rs:
        print(course, 'no calendar items')
        return
    subject, nums = cu.units(course)
    items = chr(10).join('- unit %s (%s): %s' % (r['unit'], r['lens'], r['finding']) for r in rs)
    logdir = opts.get('logdir', os.path.join(ROOT, '..', 'codex-ruling-logs'))
    os.makedirs(logdir, exist_ok=True)
    tag = 'calendar-%s' % course
    subprocess.run([sys.executable, '-X', 'utf8', 'scripts/codex_write.py', 'docs/pipeline/briefs/unit-calendar-fix.md',
                    course, 'items=' + items, 'writer_brief=' + cu.brief_for(subject),
                    'allow=data/plans/{course}/days.csv;docs/courses/{course}/scope-and-sequence.md;docs/courses/{course}/s*.md',
                    'tag=' + tag, 'log=' + os.path.join(logdir, tag + '.log')], cwd=ROOT)
    gates = [subprocess.run([sys.executable, '-X', 'utf8', 'scripts/%s' % g, 'check', course], cwd=ROOT,
                            capture_output=True).returncode == 0 for g in ('plan.py', 'unitplan.py')]
    stamp = '%s calendar %s' % (datetime.date.today().isoformat(), 'pass' if all(gates) else 'FAIL')
    for r in rs:
        r['applied'] = stamp
    save(rows)
    print(course, len(rs), 'calendar items:', stamp, '(see the report for any LEFT: lines)', flush=True)


def main(a):
    if a and a[0] == 'calendar' and len(a) > 1:
        calendar(a[1], dict(x.split('=', 1) for x in a[2:]))
        return 0
    if not a or a[0] not in ('collect', 'open', 'apply'):
        print(__doc__)
        return 2
    if a[0] == 'collect':
        collect()
    elif a[0] == 'open':
        show_open()
    else:
        apply(dict(x.split('=', 1) for x in a[1:]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
