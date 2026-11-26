# Step 4.L review (2026-11-25)

A fresh read of `git diff b3a63f3fd..28b995ce6` only. Nothing was changed. Run for this review: the self-tests of homes, ids, index and plan_facts (all pass), `homes.py check` (0 lines), `ids.py check`
(0 lines, 3.8 s), `plan_facts.py links` (0), an in-memory `index.build()` compared with `index.load()` (identical:
49,554 nodes, 358,471 edges), and a cell-by-cell compare of all 34,214 migrated ledger rows (no cell changed but the
new column).

## Verdict per row

| Row | Verdict | In one line |
|---|---|---|
| 1 | done | Built note is accurate. A 14-edge sample of day and piece mentions was all real cross-day references. |
| 2 | done with issues | Homes are tight and tested. Goal test 2 sees only framed courses (finding 4). |
| 3 | done with issues | Inverted as asked, 29 names. Still a line regex, so an indirect read passes (finding 6). |
| 4 | done with issues | Test 11 as asked. Test 10 is one direction only and never reads `version:` (finding 1). |
| 5 | done | Said in the doc and in goal_tests.py. |
| 6 | done with issues | Column, writer and check are correct. The 0 backlog is not yet a real number (finding 3). |
| 7 | not run | By design; the note says so. |
| 8 | done with issues | (a) and (b) each add a new failure path (findings 2 and 5); (c), (d), (e) are fine. |

## Findings, most severe first

**1. Goal test 10 checks half of what row 4 asked.** `scripts/index.py:481` (`day_status`). The row said: compare the
day file's `version:` with the ledger `stage`. Built: a ledger row at stage written must name a day that has a file.
Frontmatter is never read, and the reverse direction is not checked. Failure case: us-history-i and world-history-i
each have 5 written days and a header-only ledger (the very case later.csv L132 records), and test 10 reports 0. Today
82 of 2,107 day files have no written ledger row for their day (48 in the math-4 pilot, 34 in eight courses); some
may teach nothing new, but the test cannot tell. The Built note's "reads the day status in both homes" claims more
than the one direction built. Fix: add the file-to-ledger direction with its own
baseline key, or name a "no new entry" marker.

**2. A new plan fails the shared `plan-links` gate for every course.** `scripts/plan_facts.py:38` (`strip` now
removes the link line) and `scripts/unit_skeleton.py:2346` (writes a starter plan as `plan_facts.strip(text)`);
`scripts/section_skeleton.py:516` writes section skeletons with no link line either, and no brief or kit file
mentions the line. Failure case: a job runs `unit_skeleton.py` for one of the 62 courses not yet framed; the new
`s01.md` has no link line; `plan-links` is a shared check, so it shows as a new failing line in that course's gate
and in any other course's gate that runs before the lead runs `links --write`. Fix: the skeleton writers call
`plan_facts.link_line` when they write the plan.

**3. `student_word` defaults to "no", so "judged no" and "never judged" are the same value.**
`scripts/ledger.py:141` and `:259`, `scripts/vocabulary.py:223`. All 13,484 older term rows are "no" and the backlog
is 0. The Built note is honest about that, but row 6's "done when" (a real number before L130 is scoped) is not met:
the number will only ever count words marked from now on. Failure case: geometry's "compass" and "radius" (seeded
from the progression's `words` list, which is the plan of student words) read "no" forever, so they never get a
definition. Better ways, either of which avoids the hand reading pass:
- Leave the migrated rows blank (not judged), have `report` print "undecided" beside the backlog, and mark the
  1,451 term rows whose note says "seeded from ... words" as yes by script.
- Or drop the hand flag: a `[[word:...]]` mark on a student page already says "this is a student word". Deriving
  the backlog from marks keeps one home for the fact; today a marked word with flag "no" is highlighted for
  students and silently left out of the backlog.

**4. Goal test 2 cannot see an unframed course, and one of its four homes can never fail.**
`scripts/goal_tests.py:28-35`. `missing_homes` lists courses by globbing for `frame.md`, then checks `frame.md`
among the homes, which is true by construction. 62 of the 120 course-list ids have no frame. Failure case: a frame
is deleted or a course is added to the list with days.csv but no frame; the test stays 0. Fix: iterate active
course-list ids; count those past a stated stage.

**5. The fresh-index check trusts the save time, not the build start.** `scripts/index.py:360` (`stale`) and
`:619`. A build takes about 24 s and the database's mtime is the end of it. Failure cases:
- Side by side: job A's gate starts a build; at second 10 job B saves a day in a course the build already read; the
  database is stamped at second 24, newer than B's file. B's gate then loads the saved index and B's broken link or
  new orphan does not fail.
- A writer makes an untracked piece, runs the gate, deletes the piece, runs the gate: no file is newer, so the index
  still holds the piece (a deleted untracked file is not in `git ls-files`).
Fix: store the build start time and a file count in the database and compare against those.

**6. The catalog lint still reads lines, not behavior.** `scripts/lint.py:52` and `:81`. A curriculum script that
does `import build_db` (or any TOOL_SIDE module) and calls its loader names no catalog file and passes.
`scripts/*.py` also skips `scripts/overlap/` and the `.mjs` files. Cheap tightening: also fail a
non-tool-side script that imports a TOOL_SIDE module.

**7. Goal test 11 fails the wrong course's gate, and only before a commit.** `scripts/ids.py:84`. It is a shared
check over every course, so course A's uncommitted item deletion is a new failing line in course B's gate. After
the commit the deletion is invisible, so the count in goal-tests.csv (written by `--all`, after commits) is always
0. As asked, and the lead's pre-commit gate does catch it; say so in the test's note.

**8. Small.** `gate.py --record` (`scripts/gate.py:341`) counts lines from shared checks that name the course, so
a course's debt number can move without the course changing.
