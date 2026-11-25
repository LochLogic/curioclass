# Consolidation step 4: report

Step 4 of docs/CONSOLIDATION-PLAN.md, sub-steps 4.A to 4.J, built 2026-11-25 from tag `pre-step4` (block one under
Cory's block-one go, block two under "Yes continue work"). This report lists every count that moved and why. The
plan's Built notes hold the detail; this page is the summary the close review reads alongside the repository.

## What each sub-step left

| Sub-step | What it built | Proof |
|---|---|---|
| 4.A gates that test what ships | the runner gained unitplan, frame, sequence, skeleton self-tests and check_site; site builds go to a scratch CURIO_DIST with the deploy flags; raw dumps ignored | runs step4-B onward |
| 4.B data/units.csv retired | plan.py, lesson_course.py and coverage_ledger.py read frames.csv instead | non-zero gates 29 to 26 by 4.E2 |
| 4.C the course list as data | data/plans/course-list.csv (120 rows) owns which courses exist | COURSES-STATUS.md same apart from the date and the math 4 pilot count |
| 4.D ledgers per course, one row writer | data/plans/<course>/ledger.csv; scripts/rows.py upsert; scripts/safe_write.py locks | ledger.py check identical before and after; race self-tests |
| 4.E skeletons ignored | 2,763 skeleton files untracked, always rebuilt | docs/courses 3,925 tracked files to 1,156 |
| 4.E2 plans hold judgment only | 9,464 stored blocks stripped from 916 plans; scripts/plan_facts.py the one renderer; hand list signed (discard 1,438, move 235, back-port 168) | skel-guard 0; 3,112 renders before and after differ only by moved prose |
| 4.F the index | scripts/index.py, data/index.db (ignored), five reports with a baseline, scripts/uses.py | resolve 11 known, orphans 386 known |
| 4.G one gate command | scripts/gate.py, scripts/lint.py, kit `{GATE}` (kit 7) | step4-G against step4-E2-final: 0 new failing |
| 4.H homes and ids | data/homes.csv, scripts/homes.py, scripts/subjects.py, scripts/ids.py, item suffix baseline, docs/CHANGES.md, per-course reports (kit 8) | homes check 0 lines over 36,344 tracked files; step4-H against step4-G: 0 failing |
| 4.I words | data/plans/vocabulary.csv, scripts/vocabulary.py, `[[word:...]]` in lesson.py, word nodes in the index | self-test; read-only Word Wall import NOT run (below) |
| 4.J close | scripts/goal_tests.py and data/plans/goal-tests.csv; uses.py rebuilds only when stale | this report |

## Counts that moved, `pre-step4` to now

| Count | pre-step4 | now | Why |
|---|---|---|---|
| Commits | | 17 | one or two per sub-step |
| Tracked files | 40,314 | 36,355 | skeletons untracked (2,763), raw gate dumps out of git (1,280), units.csv gone, new scripts and tables in |
| Lines in tracked files (diff) | | -650,724 net (67,490 in, 718,214 out) | stored skel blocks, skeletons and raw dumps |
| docs/courses tracked files | 3,925 | 1,156 | skeleton folders ignored |
| docs/reviews tracked files | 4,925 | 3,680 | raw gate dumps out (the tags keep them); three grade-fix records moved in |
| data/plans tracked files | 302 | 342 | per-course ledgers (from four subject files), course-list, vocabulary, suffix baseline |
| Curriculum scripts added | | 13 | gate, homes, ids, index, lint, plan_facts, rows, safe_write, skel_strip, subjects, uses, vocabulary, goal_tests |
| Gates in a full run | 128 | 210 | unitplan check per course (59), self-tests (10), frame, sequence, check_site, lint, index reports, rows, ids, homes, vocabulary, skel guard |
| Gates exiting non-zero | 29 | 26 | plan.py drops the units.csv section check (4.B); three science plan gates now pass. Of the 26: 22 plan-<course> (pre-existing content findings), 3 unitplan (new gate, known), check_tools (tool side, frozen), lesson-check (the aggregate, baseline L126) |
| FAIL lines, per-course lesson gates | 5,916 | 5,424 (5,437 with the pilot math-4, now in scope) | units.csv lines gone; science K-3 and ELA K-3 fixes that landed in steps 2 and 4.E2 |
| FAIL lines, plan gates | 6,318 | 5,839 | about 479 units.csv section lines gone (4.B) |
| Kit version | 3 | 8 | retools 3 to 7 in docs/pipeline/kit/RETOOL.md |
| Index | none | 48,639 nodes, 315,379 edges (226,858 hard) | word nodes from ledger term rows added in 4.I |
| uses.py lookup | none | 0.3 s fresh, about 22 s after a change | rebuilds the index only when a source file is newer (4.J) |
| Word table backlog | none | 16,128 ledger term heads with no definition | the table is empty until definitions are written (later L130) |

## The 12 end-goal tests (data/plans/goal-tests.csv)

| # | Test | Count | Target | Reading |
|---|---|---|---|---|
| 1 | one working folder | 1 | 1 | met |
| 2 | every course has the same homes | 0 | 0 | met (layout report over 36,344 tracked files) |
| 3 | one home per fact | 0 | 0 | met (marker guard) |
| 4 | no curriculum list from the tool catalog | 0 | 0 | met, with the named exception course_pages.known_standards |
| 5 | any object found by id | 0.2 s | seconds | met with a fresh index; about 22 s after a change (one rebuild) |
| 6 | changes run as scripts, rows through rows.py | 0 | 0 | met as measured: no plan CSV a hand edit broke. The test cannot see a hand edit that left the CSV valid |
| 7 | one gate command | 0 | 0 | met |
| 8 | generated things never stored twice | 0 | 0 | met |
| 9 | every relation resolves | 11 | 0 | 0 new; 11 known misses (7 objects) on the baseline, later L125 |
| 10 | one status per object | 0 | 0 | met; 412 flow-status rows kept on purpose (4.H note) |
| 11 | retired ids never reused | 0 | 0 | met, but nothing has been retired yet, so the test is untried on real data |
| 12 | nothing orphaned | 386 | 0 | 386 pieces no day leans on, all on the baseline, later L125 |

Nine of twelve read at target. Tests 9 and 12 hold a known backlog that cannot grow (any new miss fails the gate);
tests 6 and 11 measure less than their words promise.

## Left open, with their homes

- **4.I step 5, the read-only Word Wall import:** not run. Reading data/closet/words was refused by the session's
  permission check, because data/homes.csv and AGENTS.md mark it never-touch. The plan says read-only; the rule says
  never touch. Cory decides: allow one read-only read (the import writes only data/plans/vocabulary.csv rows with
  status candidate), or leave definitions to writers from scratch.
- later.csv rows opened in step 4: L116 (reading-level lint), L119 (word popup), L120 (Word Wall as a view), L122 to
  L124 (4.E2 leftovers), L125 (index misses), L126 (lesson-check and style baseline: 5,470 FAIL lines, 4,210 style
  lines), L127 (Codex scripts still write top-level reports), L128 (remaining band helpers), L129 (Words today box),
  L130 (who writes definitions).
- Pilot math-4 stays blind, reconciled under L13.

## Gate runs

- step4-J (docs/reviews/consolidation/step4-J/summary.csv): 210 gates, 26 non-zero.
- step4-J against step4-H: 0 failing findings, 12 new note lines (the vocabulary gates, the index's new node count).
- step4-J against pre-step4 (the tag's step3-after run, extracted to build/gates/pre-step4): the compare prints 9,628
  "failing" findings, and none is a regression of an old gate. They are the lines of gates that did not exist before
  step 4: lesson-check (5,416 FAIL lines, the aggregate over every course, baselined in later L126), the 59 new
  unitplan gates, frame (129 lines) and the rest of the "only now" list. Every gate present in both runs held or
  fell: plan-science-grade-1, -3 and -kindergarten went from exit 1 to 0, and every per-course lesson gate's failing
  count fell (for example ELA grade 1 48 to 13, math K 4,463 to 4,426, science grade 1 13 to 0).
- The site built into a scratch folder with the deploy flags (`--library --closet --courses`) and check_site passed: 6,777 pages, 0 broken internal links, 0 external loads, 8,610 files (limit 20,000).
