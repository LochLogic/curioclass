# Sequence read: math grade 3, 2026-11-15

Expert cold read of the Curio Class math grade 3 scope and sequence, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-3/frame.md and docs/courses/math-grade-3/scope-and-sequence.md, in full.
- data/plans/math-grade-3/days.csv (all 160 rows) and data/plans/math-grade-3/source-map.csv (175 rows), in full.
- data/plans/math-grade-2/days.csv, for every m2 row the grade 3 ledger assumes.
- The base: Illustrative Mathematics grade 3 at S:\CurioClass-sources\illustrative-math (143 lessons, all units), lesson purposes, learning goals and titles.
- Earlier reads for the standard: sequence-math-kindergarten, sequence-math-grade-1 and sequence-math-grade-2 (2026-11-15), above all grade 2's "Across the band".
- Gates: `plan.py check` 0 failures, `sequence.py check` 0 failures for math-grade-3, `frame.py calendar` checks in weeks 12, 23 and 31 with no stagger break, `stale.py` 0 failures.

## Verdict

A sound grade 3 year that teaches the major work in the right order: multiplication and division meaning before the facts, area tied to multiplication, fractions on the number line with comparisons kept to the same whole, and untimed fact practice every day from day 15. It is fit to plan from once three things are fixed: a block of added days carries its text in the wrong columns, the year-end fluency evidence for 3.OA.C.7 and 3.NBT.A.2 is not asked directly, and the day 21 end day stacks two full performances. The remaining items are small: stale ledger wording, a handful of goal cells that track the base too closely, and the band source-map layout.

## Findings

### 1. Added days carry note text in the supplies column

- What is wrong: on days 73, 74, 75, 82, 85, 94, 100 and 110 (own added days in units 3 and 5) the "Own added day..." note text sits in the supplies column and the warm-up text sits in the note column. Day 100's note opens "3.NF.A.2a; 3.NF.A.2b Warm-up..." and day 74's teaching content (division with zero and one) is only findable in supplies.
- Evidence: days.csv rows 73 to 110 as listed; compare any base day, where supplies is empty or names materials.
- Cost: a unit-plan writer reading the note column gets a warm-up line and no reason for the day; a materials list built from supplies prints paragraphs.
- Fix: for each of the eight rows, move the "Own added day..." text back to note, append the warm-up line after it, and set supplies to real materials or blank (paper fraction strips on days 94, 100 and 110; blank elsewhere).
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: new.

### 2. Year-end fluency for 3.OA.C.7 and 3.NBT.A.2 is not asked directly

- What is wrong: the facts record is taken on day 75 (week 15). Day 152 lists 3.OA.C.7 as "untimed and private" but does not update the memory, strategy or counting categories child by child. Day 153 lists 3.NBT.A.2 among 18 codes as supplied-reasoning diagnosis with no independent computation sample. Grade 4 day 1 retrieves "from the grade 3 handoff", so the handoff rests on a week 15 record and a diagnosis task.
- Evidence: days.csv days 75, 152, 153, 160; grade 2 read finding 2 (diagnosing an error is not fluency).
- Cost: the grade 3 end-of-year fluency expectations, the two the brief names, have no direct year-end evidence, and grade 4's facts retrieval starts from stale data.
- Fix: day 152 adds an untimed private facts station (about 10 minutes, groups of 8 at a time across the day's work time) that updates each child's day 75 category; day 153 adds about 8 independent within-1000 addition and subtraction items done without a supplied method; day 160's handoff records both. No days added.
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 2 finding 2).

### 3. Day 21 end day stacks two full performances

- What is wrong: day 21 asks fresh for both drawn graph types (scaled picture graph and scaled bar graph, 3.MD.B.3) and for equal-groups interpretation (3.OA.A.1), with no saved product reused.
- Evidence: days.csv day 21; days 4 and 5 already produce scaled graphs that could be retained.
- Cost: breaks the end-day rule; the day runs long for 8-year-olds and the graph evidence crowds out the multiplication evidence that matters more.
- Fix: mark the day 4 to 5 scaled picture and bar graph products as retained for the unit window, and have day 21 ask short graph-reading prompts plus the equal-groups performance.
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 2 stacked end days).

### 4. Ledger and frame readiness wording are stale

- What is wrong: the scope-and-sequence ledger and "For the lead" item 1 say grade 2 days.csv does not exist and last use is "planned, not verified". It now exists. I checked every m2 row the ledger assumes (for example m2-picture-bar-graphs day 144, m2-shape-attributes day 110, m2-time-five-minutes day 144): each is used in grade 2, so retrieval in grade 3 is correct. The frame still says each unit opens with a readiness check on grade 2 rows, which contradicts the brief's grade-number rule.
- Evidence: scope-and-sequence.md ledger and "For the lead"; frame.md readiness paragraph; data/plans/math-grade-2/days.csv.
- Cost: a writer may add readiness checks on grade 2 rows that the rule says get retrieval only.
- Fix: replace "planned, not verified" with "verified against grade 2 days.csv 2026-11-15"; drop "For the lead" item 1; in frame.md state the rule (grade 2 rows get retrieval in grade 3; readiness only on rows last used in grade 1 or earlier).
- Severity: low. Confidence: firm. LAYER: frame (wording) and sequence (ledger). REPEAT: yes (grade 2 stale frame readiness wording).

### 5. A few goal cells track the base too closely

- What is wrong: days 144 and 145 swap one verb in the base learning goals ("Make rectangles with the same perimeter and different areas" against the base "Draw ..."; day 145 the same for same area); day 29 "Use square feet and square meters to measure larger regions" is near the base goal. Days 106, 108, 109 and 125 are light edits of base purposes.
- Evidence: comparison of all 128 base-mapped goal cells with IM grade 3 goals and purposes, plus a 30-cell sample read by hand.
- Cost: breaks ideas only, never wording.
- Fix: rewrite the seven goals around what children do and say in our course, for example day 144 "Hold the perimeter fixed, build several rectangles and explain why their areas differ".
- Severity: low. Confidence: firm. LAYER: base text. REPEAT: yes (math grade 1 goal rewrites).

### 6. Source map off the band layout, with duplicated day cells

- What is wrong: columns are base_unit, base_lesson, source_title, course_unit, day, decision, reason, source_url, license, not the band layout (base_lesson, base_title, course_unit, day, decision, reason, source_url, license). Unit 7 rows (base unit 6) repeat the day ("117; 117").
- Evidence: source-map.csv header and unit 7 rows.
- Cost: band tools and readers have to special-case each course.
- Fix: drop base_unit (it is in base_lesson), rename source_title to base_title, and de-duplicate the day cells.
- Severity: low. Confidence: firm. LAYER: process. REPEAT: yes (grade 2 layout finding).

## Checks the brief asks for

- Source map against the base: every one of the 143 IM lessons has a row, titles match, base order is kept. Decisions: 105 keep, 32 ours, 21 split, 14 cut, 3 merge. The cuts are optional lessons, design days, survey days and routines, and each reason holds. The merge of 3.3.8 to 3.3.10 into days 46 and 47 keeps every idea.
- Departures from the base order: none in unit order; the added measurement-quantity day before unit 7 and the denominator-error day are reasoned and sound.
- Our words: copy rate 3 of 128 goal cells as near copies (2 percent), 7 of 128 (5.5 percent) counting light edits; notes and source-map reasons 0.
- Focus: about 68 percent of coded days are major work (3.OA, 3.NF, 3.MD.A, 3.MD.C), above the 65 percent line.
- Coherence: grade 2 rows are retrieved, not checked; facts build from meaning (units 1 and 2) to strategies to the day 75 record; fractions build from unit fractions to the number line to same-whole comparison.
- Rigor balance: understanding, fluency and application all present in each major unit.
- Fluency: 3.OA.C.7 daily untimed from day 15, record on day 75; 3.NBT.A.2 taught in unit 3; year-end evidence weak (finding 2).
- Readiness: unit 1's readiness sits in the last ten minutes of day 1; no grade 2 row gets a readiness check.
- End days: day 21 stacks (finding 3); day 58 (written computation plus a short rounding prompt) is acceptable.
- Collect once: course checks use new forms and earlier contexts; day 153 reuses a day 21 record (week 5) for 3.MD.B.3, which is allowed but old.
- Planning class size 30: observation days fit at groups of 8.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | about 68 percent |
| Progression coherence | yes | grade 2 hand-offs verified |
| Rigor balance | yes | three kinds in each major unit |
| Named fluencies | partly | year-end evidence (finding 2) |
| Practices named | yes | all eight |
| Models consistent | yes | arrays, area, number line, tape |
| Precise language | yes | fractions tied to the same whole |
| Readiness by grade number | yes | frame wording stale (finding 4) |
| End days not stacked | partly | day 21 (finding 3) |
| Collect once | yes | |
| Our words | partly | 5.5 percent with light edits |
| Source-map layout | no | finding 6 |

## What is right and should not be touched

- Daily untimed private fact practice from day 15 and the day 75 categories record.
- Division with zero and one has its own day (day 74).
- The measurement-quantity day before unit 7, and comparisons always tied to the same whole, with a day on denominator errors.
- Course checks change form and draw on earlier contexts.
- The fold-in list for the shorter path, marked draft.

## What I could not judge

- Minute shares inside days; the plan gives one major code first, so the major share is by code, not minutes.
- Whether the day 75 categories are workable at 30 children in one day; the plan says groups and stations, which looks right.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Grade 2 rows get retrieval, not readiness | Readiness counts by grade number | scope-and-sequence.md ledger |
| Day 58 end day stands | Computation plus a short rounding prompt is one full performance | days.csv day 58 |
| Day 153 may reuse the day 21 graph record | Allowed, though old; new graph task not needed | days.csv day 153 |
| Merge of 3.3.8 to 3.3.10 into days 46 and 47 | Every idea kept | source-map.csv |
| Fact practice untimed | Timers only with a grounded purpose; none needed here | days.csv from day 15 |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grade 3 (openly licensed pages), S:\CurioClass-sources\illustrative-math.
- Common Core State Standards for Mathematics, grade 3, and the progressions documents (operations and algebraic thinking, number and operations: fractions).

## For the source list

Nothing new.
