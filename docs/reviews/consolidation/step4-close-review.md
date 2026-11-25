# Step 4 close review (Fable, cold read, 2026-11-25)

Read from the repository at HEAD (3c4a6353a) against tag `pre-step4`. Commands run are named in each finding. Nothing
was changed except this file. `gate.py --all` and the site build were not rerun; the step4-J run on disk was read.

## Verdict

Step 4 came out largely as intended. The structural work is real and checks out: per-course ledgers with locked
writes (race self-tests pass), 9,464 stored blocks gone with a guard behind them, a working index, one owner file for
homes, and 3,959 fewer tracked files. The project is in a better place than at `pre-step4` for the lead, the site and
the next 118 courses. It is not yet safely better for writers, because the one gate command passes when no baseline is
stored and prints up to 457 KB per run in the course that is next in line. Three of the 12 goal tests read at target
while measuring much less than their words (2, 5, 10), on top of the two the report already admits (6, 11). Two things
should be fixed before any course run: the gate's baseline rule and its output size. One recorded decision should be
reversed: the Word Wall import should not be run as rows in the word table.

## Findings

### 1. The gate passes when no baseline is stored, and the baseline is a local, overwritable folder

Severity: address now.

Evidence. `scripts/gate.py:296-299`: with no `build/gates/base-<course>/`, a course run returns 0 whatever it found.
Run: `gate.py --course science-grade-2` printed 95 failing lines (one plan FAIL, a plan gate at exit 1) and exited 0.
The baseline lives in `build/` (ignored), so it is per machine, lost on any cleanup, and never reviewed.
`--baseline` can be stored at any time, including after the change, and a second job in the same course overwrites
the first job's baseline and absorbs its new failures. The only scripted before and after is `turn.py end`
(turn.py:207, 243), and that queue is empty (`data/pipeline/jobs.csv` holds a header only). Every real course run
uses coursegen job files, where the baseline is a sentence in the kit (day.txt:32, common.txt:10). So the claim
"new work can only land flat" rests on each agent remembering a flag. The same hole sits under goal tests 9 and 12:
"a new miss fails the gate" is true only when a baseline exists.

Recommendation. Make the baseline the lead's, not the writer's: `gate.py --course` with no baseline exits non-zero
with "no baseline", `--baseline` refuses when the course has uncommitted files, and coursegen stores the baseline
when it writes a run's queue.

### 2. The gate prints every known failure on every run: 457 KB for math kindergarten

Severity: address now (math K to 3 is the next lane in HANDOFF).

Evidence. From build/gates/step4-J, the lines a course run prints (`current_failures`): math-kindergarten 8,721
lines, 457,105 bytes (about 115,000 tokens); ELA grade 4 826 lines, 90 KB; social studies grade 4 258 lines. The kit
tells a day job to run the gate at the start, after the last day and after fixes, against a cost target of "well
under 60k tokens a day" (common.txt:8), and the same file says "never print an unfiltered gate". The bulk is one
rule printed pairwise: 4,292 "have the same stem" lines in plan-math-kindergarten, repeated in the lesson gate (8,865
of about 16,800 FAIL lines in the whole run). The step report's headline debt (5,424 lesson FAIL lines, 5,839 plan
FAIL lines) is mostly this one rule in one unread Codex draft course, not broad content debt.

Recommendation. `gate.py --course` prints counts by rule plus only the lines that are new against the baseline (full
list behind `--verbose`), and the same-stem check prints one line per stem group, not one per pair.

### 3. Do not run the Word Wall import as rows in the word table

Severity: address now (it is the open Desk question). Contradicts Desk decision: plan decision 9, "the Word Wall
route (read-only import in 4.I)".

Evidence, from the design only (the folder was not opened). The import would put 4,413 rows, keyed by tool topic and
written for the tool catalog, into `data/plans/vocabulary.csv`, a source table that is empty today, has no consumer
(the "words today" box is L129, undesigned) and no reader assigned (L130, undecided). That is a curriculum list seeded
from the tool catalog, which goal test 4 and the 2026-11-24 "curriculum first" decision exist to prevent, and the
plan's own count says 432 word and band pairs already disagree. Every candidate row would still need a full read at
the band's reading level, so the saving is a first draft, not a finished definition. The permission refusal was the
never-touch rule working as written; the plan and the rule disagree, and the rule is the safer of the two.

Why the alternative serves the goal better. The end goal is one home per fact with nothing unowned. 4,413 unread
rows are a new unowned pile on day one. The same help to writers is available without adding rows.

Recommendation. Leave the import unrun; when L130 opens, allow one lead-run, read-only script that prints only
overlap counts (ledger term heads that match a card word, by band), and if the overlap is high have it write an
ignored lookup file that definition writers consult, never rows in vocabulary.csv.

### 4. The word backlog is not a vocabulary list

Severity: before writing at scale (before any definition is written).

Evidence. `vocabulary.py report` prints 16,128 undefined heads; the index holds 5,529 distinct word nodes. A random
sample of 60 includes "explained afresh before the chosen action", "family record against a picture of a kind",
"read whole in look at me", "from", "ow". 2,939 of 5,529 heads (53 percent) are two or more words. Ledger term rows
record what a later day may lean on, for teachers and writers; they are not a list of words a student needs defined.
Also, 7,105 of the 13,484 term rows name no day (stage planned), so "day uses word comes from the ledger" holds for
the written half only. The plan's line "the backlog exists today with no marks at all" overstates what the data
holds, and L130 sizes a writing job from a number that is mostly noise.

Recommendation. Before L130 is scoped, add one yes or no column to the ledger term rows ("student word"), set at
writing time and defaulting to no, and count the backlog only from yes rows.

### 5. `uses.py` misses about 48,600 day mentions

Severity: before writing at scale (a one-line fix plus one call).

Evidence. `scripts/index.py` (`_course`, the written plans loop) indexes plan files matching `scope\.md`, but the file is `scope-and-sequence.md`:
the index has 0 scope nodes for 58 courses (query on data/index.db). Day files and pieces are indexed with
`links=True`, which skips day mentions (index.py:267). My count with the index's own pattern: 10,397 "day N" mentions
in the 58 scope and sequence files and 38,214 in days and pieces, against 57,034 in unit and section plans that are
indexed. So the impact list for a day is missing close to half its prose mentions, in the two places a trade of
content inside a section touches first.

Recommendation. Fix the file name pattern and index soft day mentions from day files and pieces, then re-store the
baseline.

### 6. Goal test 2 passes by construction, and writers' stray files are invisible until committed

Severity: before writing at scale.

Evidence. `homes.py kind` on made-up paths: `docs/courses/biology/summary.md` and `unit-notes.md` read as plans
(patterns `s*.md`, `u*.md`); `data/plans/biology/notes.csv` reads as "other course tables";
`courses/biology/u01-1/scratch-notes.md` reads as a piece; `data/plans/newcourse-not-listed/days.csv` is a valid
source although no such course is on course-list.csv. `homes.check` and lint's layout check read tracked files only
(lint.py:139 filters `f in tracked`), so a stray a writer creates is not seen in that writer's gate. The test also
never checks that a course has its homes: 17 courses have a frame, a scope and days.csv but no ledger.csv.

Recommendation. Tighten the course patterns to the real names (`s[0-9][0-9].md`, `u[0-9][0-9]-[0-9]*.md`, a named
table list), require the folder to be a course-list id, and include untracked files in the `--course` layout check.

### 7. The rule docs disagree about how work runs

Severity: address now (an hour of edits).

Evidence. AGENTS.md leads with the queued job path and names `data/jobs.csv` (AGENTS.md:26); the file is
`data/pipeline/jobs.csv` and is empty, and plan 4.G says coursegen job files are the one queue format. common.txt:10
says "two jobs never write the same course at once" and common.txt:12 says "jobs in one course may both write
through them". HANDOFF.md is dated "as of 2026-11-24", says "4.J and the close Fable review are next", and carries the
whole consolidation state in one 2,000-character sentence. docs/pipeline/README.md still presents turn.py and
jobs.csv as "The pieces".

Recommendation. Rewrite AGENTS.md "Who commits" around the path actually used (lead-launched coursegen jobs, the
lead commits), settle the same-course sentence one way in common.txt, and refresh the HANDOFF state block.

### 8. A scripted US spelling sweep now beats "fix when next edited"

Severity: later (cheap whenever chosen). Contradicts Desk decision: q-fix-health-2 (2026-11-21), "no separate pass".

Evidence. Lint style holds 4,210 baseline lines; nine words make up 3,370 of them (L126: labelled 881, licence 601,
practise 525, recognise 300, practised 288, practises 252, modelled 213, modelling 163, colour 147). The lint already
skips quoted titles, links and code, so the safe set is known. That decision was taken before a lint existed. Today
these lines are printed in every course gate (93 for science grade 2) and hide real new lines.

Recommendation. One scripted, quote-aware sweep of those nine words with a dry run, per docs/CHANGES.md, instead of
carrying the lines for 118 courses.

### 9. The catalog lint reads a hand-kept script list

Severity: later.

Evidence. `lint.py:27-30` lists 23 curriculum scripts. `course_status.py` opens data/modules.csv (line 32) and still
runs the full catalog placement before joining course-list.csv; `coverage_ledger.py` reads modules.csv and
tools-concepts.csv. Neither is on the list, and none of the 13 new scripts except those typed in are. Goal test 4
reads 0 for the scripts someone remembered to list.

Recommendation. Invert the list: lint every script under scripts/ except a named tool-side set, with
course_status.py's catalog counts as a second named exception.

## The 12 goal tests, my reading

| # | Test | Count | My reading |
|---|---|---|---|
| 1 | One working folder | 1 | Met. |
| 2 | Same homes, nothing else | 0 | Weaker than its words: loose patterns, tracked files only, no check that homes exist or that the folder is a listed course (finding 6). |
| 3 | One home per fact | 0 | Met for the stored blocks, which was the large case. It counts only the marker; other copies (frames.csv, the two in-file copies, day frontmatter `unit:`) rely on their own gates, and 412 flow-status rows restate a file on purpose. |
| 4 | No list from the tool catalog | 0 | Met for 23 listed scripts; the list is hand-kept and leaves out course_status.py (finding 9). The Word Wall import would breach it in spirit (finding 3). |
| 5 | Found by id, with soft mentions | 0.2 s | Speed met (0.24 s measured; 24 s for any run that rebuilds). Coverage is not: about 48,600 day mentions are outside the index (finding 5). |
| 6 | Changes as scripts, rows through rows.py | 0 | As the report says: it tests that CSVs parse, not how they were written. Accept it as a convention, not a test. |
| 7 | One gate command | 0 | The command exists and is the only one named. It counts leftover placeholders, not whether the gate can fail (finding 1) or be afforded (finding 2). |
| 8 | Generated never stored twice | 0 | Met for generated-ignored files. Hand edits to generated-committed files rest on their own checks. |
| 9 | Every relation resolves | 11 | Honest: 0 new, 7 objects known. Item ids inside handbacks, errors and materials rows are not edges, so "every CSV id" is "day, code, skill and item-to-day ids". |
| 10 | One status per object | 0 | Covers unit and section plans against flow-status only. Day status (frontmatter `version:` against ledger `stage`) is not compared. |
| 11 | Retired ids never reused | 0 | Untried, as the report says. Also one-sided: an id deleted without `ids.py retire` leaves no trace, so "every retired id is recorded" cannot fail. |
| 12 | Nothing orphaned | 386 | Honest backlog, baselined. Holds only while finding 1 is open in the lead's hands. |

## Sub-steps

4.A, 4.B, 4.C, 4.D, 4.E and 4.E2 did what they set out to do; I found no departure in the data (120 list rows, 58
framed courses all present in each home, 41 per-course ledgers, 0 exact duplicate ledger rows, 0 markers). 4.F works
with the gap in finding 5. 4.G built the command but not the enforcement (findings 1, 2). 4.H built homes.csv with
loose course patterns (finding 6). 4.I built a table with no consumer on a noisy backlog (findings 3, 4). 4.J's
report is accurate about what it measured.

## What got worse

- **More to learn.** 13 new scripts (2,456 lines) and 210 gates against 128. A writer must now know gate.py,
  rows.py, ledger.py, plan_facts.py, homes.py and uses.py; the kit went from version 3 to 8 in one day.
- **Slower floor.** Any course gate takes about 24 seconds (measured), because each run rebuilds the index, and the
  first `uses.py` after any edit takes about 22 seconds.
- **Plans no longer read whole on GitHub.** A stripped plan shows an empty "## Header" and no facts; a reader needs
  `plan_facts.py <course> <file>` or the Front Office to see days, codes and minutes beside the prose.
- **The debt is now formal.** About 16,800 FAIL lines, 4,210 style lines, 386 orphans and 636 suffixed ids sit on
  baselines "worked off by course". Nothing schedules that work, and a baseline that never shrinks trains workers to
  ignore the list.
- **Rules live in Built notes.** The consolidation plan is 10,200 words, and some standing rules (the 412 flow-status
  rows stay, the pilot stays in the gate but out of the index) are recorded only in its Built notes.
- **Machinery ahead of use.** vocabulary.py (272 lines), ids.py and the word nodes have no first real user yet,
  which is the pattern the plan itself warns about.

## Before step 5

Findings 1, 2 and 7 first; they are small and they decide whether the next course run is checked at all. Finding 3
needs Cory's answer. Findings 4 to 6 before writing runs at scale. Step 5 itself is not blocked by anything here:
the index's type column and the 14 TOOL-ASKS.md files are ready for tool nodes.
