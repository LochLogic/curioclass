# Pedagogy and architecture review (Fable, 2026-11-25)

A cold read of where the teaching design meets the flat database built in the consolidation. Read-only: nothing was
changed except this file. No gate was run, the index was queried as it stood on disk (data/index.db, built
2026-11-25 19:12), and skeletons were rendered only into a scratch folder. Counts come from short scripts over the
CSVs, the index and `ledger.py check` and `recheck`; a count marked "rough" rests on a regex or on the ledger's
own loose matcher. Courses followed end to end: science-grade-1 (signed off), social-studies-grade-5 (mid-build,
51 of 160 days), math-grade-4 (scope and unit plans only), with science-grade-4 as a spot check.

## Verdict

The data model carries far more of the teaching design than the file layout alone. From the unit down, backward
design is real data with gates: parts of a standard, items tied to parts, a goal-to-item trace on every written
teaching day, wrong answers tied to lettered errors, hand-backs, and a ledger that stops a day from claiming a
review of something not yet written. Umbrella first is the right order for this project and it has mostly held.
The weak points are at the edges of that core. Top-down order is kept by the job queue, not by the gate, so it can
be skipped without a failure. A change to an upper layer leaves no lasting mark on the work below it. And the
quality state of a piece of work (read, fixed, signed off) is not in the data at all, so a signed-off day and an
unread draft look the same. None of this needs a restructure: each fix is a new information source or a check on
top of what exists.

## Findings

### 1. Quality state is not in the data: a signed-off day and an unread draft carry the same status

**What.** The fact map says a day's status is "the file's own state (frontmatter `version:`, ledger `stage`)".
Neither moves when the work is read, fixed, sampled or signed off.

**Evidence.**
- science-grade-1 was signed off on 2026-11-23 (stage 7). All 68 of its day files read
  `version: draft 1, not ready, not yet taught`. social-studies-grade-5's 51 days, an unread draft run, read the
  same. Across the repository 1,643 of 2,059 day files carry that exact line.
- The only record of a sign-off is four `finish:` rows in data/plans/flow-status.csv and prose in HANDOFF.md.
  course-list.csv `status` is `active` for both courses.
- The pass marks of COURSE-RUN section 5 (serious faults a day, wrong keys, tokens a day) live in report prose
  ("K 0.9, grade 1 1.2, grade 2 0.8, grade 3 0.8 FIRM a day" in HANDOFF.md). No table holds them.
- science-grade-4 and science-grade-5 each have 120 day files and over 1,100 ledger rows at stage `written`, while
  HANDOFF says science grades 4 and up "can climb". Both statements are true, and only a reader of later.csv L105
  can tell why.
- The 12 goal tests in data/plans/goal-tests.csv are all engineering tests. None measures the curriculum.

**Why it matters.** The promise is that every course is finished to the adoption bar. A teacher, a later agent
and the Dashboard cannot tell finished from drafted by looking at the object. At 118 courses the lead will not
hold this in memory, and a draft will be taken for finished work or the reverse.

**Recommendation.** Keep the rule that the file's own state wins, and make the state move. One lead-run script
sets the `version:` line of a course's days when a stage closes (for example "draft 1, grade read 2026-11-22" and
"signed off 2026-11-23"), and one small table, data/plans/pass-marks.csv (course, date, days sampled, serious
faults a day, wrong keys, tokens a day), gets a row at each grade close, the way debt.csv does now.

### 2. A change to an upper layer leaves no lasting mark on the work below

**What.** When a fact changes, the gates catch what is structural. What was written against the old fact
(a section plan's prose, a day's teaching) is not marked anywhere as needing a read.

**Evidence.**
- What does resurface: a skill moved between grades fails `progression.py` (both ends of a handoff), `frame.py`
  ("a Skills id that is not one of the course's rows") and `sequence.py` ("owned skill is on no day"); a part with
  no assessment item fails `plan.py`; a broken `leans_on` or item link fails the index's resolve report. That is
  good coverage of facts.
- What drifts: the 4.E census found 860 of 916 written plans (5,286 of 9,464 blocks) differed from a fresh render,
  "most of it data that arrived after the plan was written". 4.E2 removed the copies, which was right. The
  proposal's step 6, "flag prose that leans on a changed fact for a read", is not in the Built note.
- The plans say so themselves. science-grade-1 s01.md, field 5: "where a case here differs (day 4: a moon strip
  and a next dot, not one paths question), the written day governs and this text records the plan-stage intent."
- The cross-grade continuity pass found 7 of 257 review claims drifted in social studies and 29 of 302 in ELA.
  They were found by a capstone read, not by a marker.
- `uses.py --changed` prints the right impact list at the moment of a change, then the list is gone. `stale.py`
  follows only `Pending(...)` notes. Git dates cannot stand in: the strip commit and the spelling sweep touched
  every plan on one day.

**Why it matters.** Umbrella first means 52 courses of plans exist before most days do, and every grade's retool
edits upper layers. That is the price of the approach. Without a mark, a child gets a day whose exit no longer
measures the goal its row now states, and nobody is told to look.

**Recommendation.** A fingerprint, not a workflow. When a day is written or read, a script stores one hash of its
upstream facts (its days.csv row, its item rows with keys, its section plan's `## Day N` block) in a per-course
table. The index status report then lists "upstream changed since last read" days, baselined like the other
reports. Start with the days.csv row and item rows only.

### 3. Top-down order is kept by the job queue, not by the gate

**What.** `coursegen.py` refuses to queue a course whose frame, days.csv or unit plan files are missing, and
`ledger.py gate` holds a day job until the rows it cites are written. Both act when a queue is generated. Nothing
in `gate.py` fails work that arrived another way.

**Evidence.**
- science-grade-4 unit 4: 20 day files in four section folders (u04-1 to u04-4) with no section plan
  (docs/courses/science-grade-4/ has u01 to u03 and u05 to u06 plans, no u04-*.md). The days' `leans_on` names
  s04.md and skips the section plan, so the resolve report is clean. No report lists them.
- The orphans report covers three cases (a day file with no days.csv row, a piece no day leans on, a plan row
  with no frame unit). "A day whose section has no plan" is not one of them.
- "Passed" is a hand-kept flow-status row (397 `unit:` rows, 21 `section:` rows). coursegen tests that a file
  exists, not that its read closed.

**Why it matters.** COURSE-RUN's third principle is "Nothing claims what is not written." A day written straight
from a unit plan skips stage 5, where exits are written first and keys are solved cold. That is the stage that
protects assessment quality.

**Recommendation.** Three existence rules in the index status report, baselined: a day file needs its section
plan; a section plan needs its unit plan; a section's item rows need its section plan. Add "the unit's
flow-status row is done" once the first three read clean.

### 4. The trace is solid in the middle and breaks at both ends

**What.** One can walk standard to day and back through data from the unit down. The joints above the unit, and
every sideways link (review, retrieval, cross-subject), are prose or are parsed by one script and invisible to
the index.

**Evidence.**
- Solid: all 1,411 owned skills of the four core subjects sit on at least one day in their course's days.csv, and
  2,534 of 2,548 owned codes do (the 14 are ELA parent codes carried by lettered parts). 8,429 of 8,504 day rows
  name a skill. All 1,592 written teaching days fill `shows`, and the gate requires every part in parts.csv to
  have an end-of-unit item.
- Break, upward: `uses.py 1-ESS1-1` lists parts, days and items, but not the progression row that owns the code
  (s1-sky-patterns) or its unit. The index has no edge from a skill to its standard, none from a unit to its
  skills (that lives in the frame.md Units table, which only `frame.py` parses), and unit nodes are bare numbers.
- Break, sideways: `uses.py sk-weather-watch` shows no use in science-grade-1, though grade 1 retrieves it on days
  1, 9 and 62. The retrieval is in the days.csv `note` cell and in a prose table in scope-and-sequence.md. Rough
  count: 1,998 day notes mention retrieval, and in 1,520 of them no earlier skill is named in the `skills` column.
  Math names earlier skills in `skills` (508 days); social studies never does (0 of 248).
- The ledger's review claims (14,260 citations, 14 unmatched, 153 pointing at planned-only rows) are parsed from
  note text by `ledger.py`. The index holds only "ledger row to day" edges, so "what later reviews this?" has no
  answer in `uses.py`.
- Cross-subject leans (546 progression rows in the core) are gated for grade timing in `progression.py` but are
  not index edges, so a math unit that moves does not list the science days that lean on it.
- The Goal map (goal verb, exit kind, exit shape, practice shape: 5,354 rows in 364 unit plans) is a markdown
  table checked by regex in `unitplan.py`.

**Why it matters.** The questions a curriculum designer asks most ("where is this standard assessed", "what
depends on this skill being taught by week 12", "does this come back") cross exactly these joints.

**Recommendation.** Add edges to the index from sources that already exist: skill owns code (progression
`standard`), unit teaches skill (frame Units table through `frame.py`), row reviews row (`ledger.citations`),
skill leans on skill or code (`cross_subject`). Then one `trace.py <code | skill | day>` that prints the chain up
and down. For retrieval, pick one convention: a `retrieves` column in days.csv holding skill ids, filled for new
courses from now and for written courses when each is next opened.

### 5. Some facts still live as prose, and the days.csv note is the largest pile

**What.** After 4.E2 the line between judgment and facts is drawn well inside plans. It is drawn less well in
three places.

**Evidence, facts held as prose.**
- days.csv `note`: non-empty on 8,157 of 8,504 rows, median 39 words, longest 378. Rough counts: 2,726 name
  another day, 1,998 retrieval, 1,341 a base lesson ("Base 1.1", a second home for source-map.csv), 253 a bridge,
  127 math focus minutes ("Focus ledger: 0 of 60 instructional minutes"), which is a number kept in a sentence.
- scope-and-sequence.md "Earlier-grade rows and their treatment": a table of skill, last-use days and retrieval
  days. It is a fact table with no data home.
- Section plan field 3 writes every exit in full (E1a to E4c in u01-1.md) and field 4 repeats the error register;
  items.csv and errors.csv hold the same things as taught. Once days exist the plan copy is history, and nothing
  on the page says so.

**Evidence, judgment held as data.** Little, and mostly right. The ledger `none` rows exist to satisfy a status
check (L133); that is acceptable. errors.csv `source` records provenance honestly: rough count, 1,375 of 2,161
errors are "from memory" and 4 cite a source. That is a judgment flag worth showing, not hiding.

**Why it matters.** A note cell is where a writer puts what the columns cannot hold. At 39 words a row it is now
a second, unchecked plan.

**Recommendation.** Do not rewrite notes. Give the three most-used facts a column as courses are next opened
(`retrieves`, a base lesson id read from source-map.csv instead of typed, focus minutes for math). In the plan
facts view, show the items.csv exits beside a section plan's field 3 once its days are written, so a reader sees
which one governs.

### 6. Review and spacing are recorded in detail and never read as a signal

**What.** APPROACH principle 7 is "Practice over time, mixed, and from memory". The ledger records every review
with its target. No report reads the spacing.

**Evidence (rough, using `ledger.py`'s own matcher).** Same-course review citations point back a median of 4 days
in science and 7 in social studies and ELA; 57 percent of science citations point back 5 days or less and 12
percent more than 20. In days.csv, 1,052 of 1,411 owned skills appear in one unit only and 359 in more than one.

**Why it matters.** A course can pass every review-claim check and still be mostly next-day repair with little
spaced return. That is a design property a reader of single days cannot see.

**Recommendation.** One read-only report per course (gap distribution, owned skills that never return after their
unit, terms introduced and never cited again), read at the stage 4 gate and at grade close. A report, not a gate:
the right spacing differs by subject.

### 7. Pedagogical concepts and their homes

| Concept | Where it lives now | Checked? | What it should be |
|---|---|---|---|
| Assessment alignment | parts.csv, items.csv `code` and `part`, days.csv `shows`, Goal map in unit plans | Yes, strongly (`plan.py`); 328 alignment defects open in defects.csv | Leave. Show open alignment defects on the Dashboard |
| Spiral review | ledger notes ("review of ..."), section plan field 8, unit plan "Returns" | Claims yes; spacing no | Finding 6 report; review edges in the index |
| Retrieval of earlier grades | days.csv note, scope prose table; `assess` = readiness (154 days) | Rule 2 as notes only | A `retrieves` column |
| Prerequisites across grades | progressions `assumes` and `hands_on` (3,798 edges), frame Seams | Yes, both ends | Leave |
| Misconceptions | errors.csv per unit, wrongs.csv `error` (13,540 of 16,036 lettered), handbacks `error` | Letters resolve; provenance not | Leave the shape. Source the "from memory" rows at course finish. No cross-grade error ids yet |
| Vertical coherence | progressions, ledger ladder, continuity pass | Yes | Leave; add the order rule of finding 3 |
| Cross-subject links | progressions `cross_subject`, frame Cross-subject, bridges in notes | Grade timing yes; calendar as a note; day level no | Lean edges in the index |
| Differentiation and access | section plan field 9; day "Words and supports", "At home" (present in all 2,107 day files), "Shorter or longer" | Headings and At home rules yes; content by readers | Leave as judgment. Note: COURSE-RUN makes English learner supports at stage 7, while APPROACH principle 9 says built into the lesson; settle which |
| Pacing and calendar | frames.csv minutes, calendar.csv, days.csv `school_day`, per-part minutes in section plans | Yes (`frame.py`, `sequence.py`, `unitplan.py`) | Leave |

### 8. The skeleton is earning its place

It is the mechanism that makes umbrella first work: a rendered brief that hands the writer the upper layers
(kind and what the kind forbids, goal, each skill marked own or earlier-grade review, codes in own words,
hand-backs in and out, existing items with keys, reserved sources and watch words) and leaves only judgment
slots. Since 4.E2 it is a pure view and an ignored working file, which is the right status. Its STOP lines are
the nearest thing to a top-down guard at day level. Two notes, neither urgent: `unit_skeleton.py` (2,352 lines)
is really the shared curriculum rules library that the scope gate, `unitplan.py` and the index import, so its
name hides its weight; and the day skeleton does not show the day's Goal map row, which the writer reaches only
through the section plan.

### 9. The Dashboard shows progress; these quality signals are already in the data

- Open defects by kind and course (defects.csv: 456 open, 328 of them alignment). `plan_flow.py` does not read it.
- Review-claim health per subject (`ledger.py recheck`: unmatched, planned-only).
- Coverage: owned skills and codes with a day, with an assessment item, and written.
- Day status by course once finding 1 lands; today it would show one value.
- Error provenance ("from memory" share) and sources still at "browser check" (14 of 3,440).
- Written teaching days with no exit item (22, rough) and courses whose days ran ahead of plans (finding 3).
- Pass marks per grade close, once pass-marks.csv exists.

## What is right and should stay

- **Umbrella first.** Progression, frame, scope and sequence, unit plan, section plan with items and keys, days,
  finish. Each layer answers a different question, and assessment is written before teaching. Keep the order and
  keep the probe, retool and sweep loop that lets lower layers correct upper ones.
- **Files in git with a generated index.** Right for this project; do not move the source into a database.
- **The assessment core:** parts.csv, items, `shows`, wrongs, errors, handbacks, reserved. This is backward
  design as data and it is gated.
- **The ledger and the ledger gate.** "Review, never taught as new" backed by 14,260 checked citations is rare in
  any curriculum.
- **Progressions with both ends of every handoff written.**
- **Plans hold judgment, facts render from data** (4.E2), and skeletons as ignored renders.
- **The kit frozen within a grade,** with defects tagged by the stage that made them.
- **Section plans as prose.** Fields 5 to 10 are judgment and should not become columns.

## Ranked changes

| # | Change | When | Size | Smallest version that works |
|---|---|---|---|---|
| 1 | Order rules in the gate (finding 3) | now | S | Three baselined lines in the index status report: day needs section plan, section plan needs unit plan, section items need section plan |
| 2 | Make status move (finding 1) | now | S | One lead script sets `version:` on a course's days at grade close and at sign-off; no new status table |
| 3 | pass-marks.csv (finding 1) | now | S | One row per grade close, typed by the lead from the sample read, beside debt.csv |
| 4 | Dashboard quality panel (finding 9) | now | S | Read defects.csv (open by kind and course), `ledger.py recheck` totals and pass-marks.csv into the health block |
| 5 | Index edges and a trace view (finding 4) | before grades 4+ climb | S | Four edge kinds from existing sources (owns, unit teaches, reviews, leans) and `trace.py` printing up and down |
| 6 | Upstream-changed mark (finding 2) | before grades 4+ climb | M | A stored hash per written day of its days.csv row and item rows; a baselined "changed since last read" list |
| 7 | One convention for retrieval (finding 4) | before grades 4+ climb | M | A `retrieves` column in days.csv; new courses fill it, written courses when next opened; the scope gate reads it for rule 2 |
| 8 | Spacing report (finding 6) | before grades 4+ climb | S | A read-only print per course from the ledger, read at the stage 4 gate and at grade close |
| 9 | Settle where English learner supports are made (finding 7) | before grades 4+ climb | S | One decision: in the day (APPROACH 9) or at stage 7 (COURSE-RUN); edit the doc that loses |
| 10 | Thin the days.csv note (finding 5) | later | M | Columns for base lesson id and math focus minutes when a course is next opened; no rewrite of old notes |
| 11 | Show which exit governs (finding 5) | later | S | The plan facts view prints items.csv exits beside a section plan's field 3 once its days exist |
| 12 | Goal map as data (finding 4) | later | M | Only if stage 4 checks keep growing: one goals table per course, rendered into the plan |
| 13 | Source the error register (finding 7) | later | M | At each course finish, one job checks "from memory" errors against a named source |
| 14 | Curriculum goal tests (finding 1) | later | S | Add four counts to goal-tests.csv: owned codes with no assessed item, open alignment defects, unmatched review claims, days below "grade read" |

Leave alone: the seven stages, the three course homes, the CSV shapes of the assessment core, the ledger's kinds,
the skeleton's place as an ignored render, and section plan prose.
