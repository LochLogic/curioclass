# Consolidation step 2: the Codex draft merge (2026-11-24)

draft/codex (244 commits ahead of main) merged into main with `git merge --no-ff`; `git revert -m 1 <merge>` undoes it.
Main was first merged into draft/codex in S:\CurioClass-draft, the shared CSVs rebuilt by script, the gates run on the
branch, then the branch landed on main.

## 1. The surface

Files both sides changed since the merge base (f5b295314): .gitignore, AGENTS.md, data/plans/ela-texts.csv,
data/plans/ledgers/ela.csv and data/plans/ledgers/math.csv (plus build/, which both sides stopped tracking the same
way). Git reported two conflicts (.gitignore, ledgers/math.csv) and merged the rest silently.

- .gitignore: main's copy (it holds every draft line plus the step 1 lines).
- AGENTS.md: both sides made the same edit.

## 2. Union rule

Gone since step 0 (`git check-attr merge` says unspecified).

## 3. The CSVs, rebuilt by course (scripts/consolidation_csv_merge.py)

Rows are grouped by course. The draft owns only its six lane courses (english-language-arts-grade-4,
math-kindergarten, science-grade-4, science-grade-5, social-studies-grade-4, social-studies-grade-5); every other course
takes main's rows.

**What this caught.** The draft's own ledgers had lost 455 rows of courses it never worked on, in the earlier merge
of main into the draft (bd20bc418, run under the union rule): science kindergarten 169, grade 1 47, grade 2 98, grade 3
77 (the signed-off science K to 3), ELA kindergarten 23, grade 2 2, grade 3 41. Science and social studies ledgers were
not on the "both changed" list, so a plain merge would have taken the draft's copy and carried that loss onto main.
Both ledgers were added to the rebuild; every non-lane course now has main's rows exactly.

| File | Rows | How |
|---|---|---|
| ela-texts.csv | 676 | main 640, plus the draft's grade 4 (29 to 65) |
| ledgers/ela.csv | 10,482 | main, with grade 4 from the draft (291 to 1,517) |
| ledgers/math.csv | 5,630 | main 1,537, plus the draft's 4,093 math-kindergarten rows |
| ledgers/science.csv | 10,067 | main, with grades 4 (151 to 1,347) and 5 (153 to 1,698) from the draft |
| ledgers/social-studies.csv | 7,994 | main, plus grades 4 (1,822) and 5 (1,263) from the draft |

**math-kindergarten**, the one course both sides changed: main seeded 83 unit-level planned rows (where s01 to s10)
after the branch split; the draft wrote 4,093 section and day rows (where u..). None of main's rows has a written twin
at the same where, and `ledger.py add` never promotes unit rows (it matches the same where). The ELA courses keep their
unit rows beside their section rows, so both sets are kept, unit rows first. Assertions passed: one header, no exact
duplicate rows, text_id unique, each course's count equal to its side's. `ledger.py check`: 0 problems in all four
subjects.

## 4. Duplicate keys over the 60 plan CSVs the draft touched

One natural key per file type. Where a file showed repeats, main's own finished courses were checked with the same
key: handbacks, materials, parts, source-map and wrongs repeat there too, so those keys are not unique by design. The
errors.csv repeats were letters differing only in case. One real repeat: the math ledger has day 37's term "one more"
(u02-6) twice with two different review notes, logged as a defect.

## 5. Gates on the branch

Against main's step2-before: no non-lane course has a new failure (lesson counts equal for every non-lane course;
the new lesson lines are only the draft's lesson_course.py format, ", N in day files"; ledger citation findings
identical). The six lane courses carry the draft's own failures, measured on the draft tip before this merge and
after it:

LANE_TABLE

The site build cannot run in the draft folder (built tool pages are git-ignored and live only in S:\CurioClass); it is
run on main after the landing.

## 6. Draft status

The field is `version` in each day's frontmatter: every Codex day says `draft 1, not ready, not yet taught`. Main's
own days carry the same words, so the field does not tell Codex days from read days. What does: course_status.py
counts a day as read only from review files (docs/reviews/cheap-dNNN-*.md and expert reads), and no Codex day has one,
so COURSES-STATUS shows them as written and unread. Course pages are built only with `--courses`, never by the deploy,
so no draft day reaches the public site.

## 7. Carry-overs

The six carry-overs of docs/reviews/codex-draft-baseline-2026-11-24.md and the math ledger repeat are open rows in
data/plans/defects.csv. later.csv L105 now holds the review classes and stays paused at Cory's call.

## 8 and 9

See the step close below.
