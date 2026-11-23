"""lesson.py check for one course (and optionally a day range), without checking every other course's days.

    python -X utf8 scripts/lesson_course.py <course> [<first_day> <last_day>]

Prints the same lines as `python -X utf8 scripts/lesson.py check 2>&1 | grep "courses/<course>/"`, plus the course's
plan failures, in a fraction of the time (the full check prints every day of every course through Chrome). Built
2026-11-22 for the Codex draft run (scripts/codex_draft.py); jobs there are pointed at it instead of the full check.
The last line is "lesson_course: N failure(s) in M day(s)". Exit 0 always (it reports; it does not block).
"""
import contextlib
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson  # noqa: E402

KNOWN = 'is not in data/units.csv'   # known, ignored by every course run


def main(a):
    if not a:
        raise SystemExit(__doc__)
    course = a[0]
    lo, hi = (int(a[1]), int(a[2])) if len(a) >= 3 else (0, 10 ** 6)
    every = lesson.day_files

    def mine():
        return [p for p in every() if p.parent.parent.name == course and lo <= int(p.stem[1:]) <= hi]

    folders = {p.parent for p in mine()}
    pieces = lesson.piece_files

    def my_pieces():
        return [p for p in pieces() if p.parent.parent.name == course and (len(a) < 3 or p.parent in folders)]

    lesson.day_files = mine
    lesson.piece_files = my_pieces
    days = len(mine())
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            lesson.main(['check'])
        except SystemExit:
            pass
    out = buf.getvalue()
    keep = [ln for ln in out.splitlines() if 'courses/%s/' % course in ln or ln.startswith('  FAIL')]
    print('\n'.join(keep))
    n = sum(1 for ln in keep if ln.startswith('  FAIL') and KNOWN not in ln)
    print('lesson_course: %d failure(s) in %d day(s)' % (n, days))


if __name__ == '__main__':
    main(sys.argv[1:])
