# Sequence read: math grade 5, 2026-11-15

Expert cold read of the Curio Class math grade 5 scope and sequence, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens. This report closes the grades 3 to 5 read and carries the "Across the band" section.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-5/scope-and-sequence.md in full and docs/courses/math-grade-5/frame.md.
- data/plans/math-grade-5/days.csv (all 160 rows) and data/plans/math-grade-5/source-map.csv (178 rows).
- data/plans/math-grade-3/days.csv and data/plans/math-grade-4/days.csv, for readiness and retrieval rows.
- The base: Illustrative Mathematics grade 5 at S:\CurioClass-sources\illustrative-math (148 lessons), lesson purposes, learning goals and titles.
- Earlier reads: sequence-math-kindergarten, sequence-math-grade-1 and sequence-math-grade-2 (2026-11-15), and my grade 3 and grade 4 reads of today.
- Gates: `plan.py check` 0 failures, `sequence.py check` 0 failures for math-grade-5, `frame.py calendar` checks in weeks 11, 22 and 31 with no stagger break, `stale.py` 0 failures.

## Verdict

The strongest of the three courses. Volume opens the year as in the base, fractions run from quotient meaning through multiplication to unit-fraction division before the whole-number algorithms, the standard multiplication algorithm is explained before it is practised and then kept alive in spaced untimed warm-ups to the last day, and goals are entirely in our own words. Most end days reuse saved products exactly as collect once intends. It is fit to plan from after one moderate fix to the day 117 end day; the rest is end-day load on a few days, one check item that should be a performance rather than a correction, and source-map tidying.

## Findings

### 1. Day 117 end day stacks two full performances

- What is wrong: day 117 asks fresh for powers-of-ten patterns (5.NBT.A.2: zeros in products, decimal placement, exponents) and for within-system conversions in both directions with decimals and multi-step real problems, metric and customary separately (5.MD.A.1). No saved product is named.
- Evidence: days.csv day 117; days 114 (multi-step metric) and 116 (multi-step customary, both directions) already produce independent conversion work.
- Cost: breaks the end-day rule; multi-step conversion in two systems is a full performance on its own.
- Fix: on days 114 and 116 add "Assessment window: retain the independent multi-step conversion", and on day 117 reuse them for the multi-step parts, asking fresh only the pattern prompts and short one-step conversions.
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 2 stacked end days; grade 3 day 21; grade 4 day 43).

### 2. Several end days carry a heavy fresh load

- What is wrong: four end days are within the rule but heavy. Day 89 asks four fresh blocks across four codes with no reuse. Day 106 has one code (5.NBT.B.7) but four full operation performances, each with a model, a written method and an explanation, plus an estimate and a critique. Day 133 asks the same-whole context problem (5.NF.A.2) fresh beside unlike-fraction computation. Day 13 asks five codes fresh beside the reused volume products.
- Evidence: days.csv days 13, 89, 106, 133; days 88, 96, 101, 105 and 123 produce matching independent work.
- Cost: 60 minutes will not hold four model-to-written explanations from 30 ten-year-olds; the reasoning evidence thins to answers.
- Fix: day 106 reuses day 96 (sums and differences in context) and day 105 (decimal division with check) and asks the other two operations fresh; day 133 reuses day 123 for 5.NF.A.2; day 89 reuses the day 88 rounding-and-precision product. Day 13 stands.
- Severity: low. Confidence: judgment call. LAYER: sequence. REPEAT: new.

### 3. Check 3 asks for multiplication fluency inside a correction task

- What is wrong: day 154 (check 3 part B) is a "validate a supplied report with annotated corrections" form and lists "untimed standard multiplication" among nine codes. As written, the multiplication evidence can be a correction of supplied work.
- Evidence: days.csv day 154; grade 2 read finding 2 (diagnosing an error is not fluency).
- Cost: 5.NBT.B.5 is the grade 5 named fluency; the year-end record should show children computing.
- Fix: in day 154's note, state that the multiplication part is a short independent untimed set (about 4 multi-digit products, no supplied work) set beside the report, recorded for the day 156 handoff.
- Severity: low. Confidence: likely. LAYER: sequence. REPEAT: yes (grade 2 finding 2).

### 4. Source map off the band layout; routine rows marked "cut" carry days

- What is wrong: columns are source_lesson, source_title, source_url, stretch, day, decision, note, short_period, not the band layout, with no license column. Base routines 5.8.14 to 5.8.18 are marked "cut" yet carry a unit and day (21, 64, 70, 124, 76) because they are adapted into warm-ups. 78 one-day rows are labelled "split".
- Evidence: source-map.csv header and rows 145 to 149.
- Cost: a "cut" with a day reads as a contradiction; band tools need one layout.
- Fix: band layout (base_lesson, base_title, course_unit, day, decision, reason, source_url, license; keep short_period as an extra last column only if the band adopts it); mark the five routines "merge" with the reason already written; relabel one-day rows "keep".
- Severity: low. Confidence: firm. LAYER: process. REPEAT: yes.

## Checks the brief asks for

- Source map against the base: every one of the 148 IM lessons has a row, titles match, base order is kept except the five routines placed into warm-ups. Decisions: 50 keep, 78 split, 4 merge, 16 cut, 30 ours. Cuts are optional lessons, two home investigations (replaced by supplied data for privacy, a sound reason), one third multiplication review and two game days; reasons hold.
- Departures from base order: base unit 2 is split into course units 2 and 3 and base 3 into 3 and 4; base 4 becomes units 5 and the start of 6; base 8 review lessons serve the course-level days 150 to 160. Our days 49 (mixed-number products, 5.NF.B.6) and 131 (equivalence as multiplication by n/n, the 5.NF.B.5b clause) fill real gaps in the base.
- Our words: copy rate 0 of 131 goal cells (highest similarity 0.66, a paraphrase of the idea only); notes and source-map cells 0.
- Focus: about 86 percent of days by code share are major work (5.NBT, 5.NF, 5.MD.C); the scope and sequence reports 77.3 percent by minutes.
- Coherence: readiness on m3-area-concepts in the last ten minutes of day 1 (last used grade 3), correct; grade 4 rows retrieved throughout (m4-multiply-multidigit day 5, m4-divide-multidigit day 15, m4-mixed-numbers day 31, m4-line-plots-eighths day 125, and so on). Fraction division stays with unit fractions and whole numbers; unlike-denominator sums wait for unit 9 and day 73 avoids them on purpose.
- Rigor balance: understanding, fluency and application in each major unit; application days use supplied data with sensitivity notes.
- Fluency: 5.NBT.B.5 standard algorithm from day 60, practice days 63 and 64, an independent untimed sample on day 76 reused on day 77, spaced untimed warm-ups from day 79 to day 160, a check 2 prompt on day 108 and a check 3 prompt on day 154 (finding 3). Timers are not used.
- End days: day 117 (finding 1); days 89, 106, 133 heavy (finding 2); days 20, 40, 53, 77 and 148 reuse products well.
- Collect once: day 77 reuses day 76's sample and day 75's application; day 133 reuses 125, 126, 132; day 148 reuses 142 and 147. Checks change form from the end day before them (day 55 against day 53, day 108 against day 106, days 153 and 154 against day 148) and draw on earlier contexts.
- Planning class size 30: no child-by-child interviews are planned; checks reuse records.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | about 86 percent |
| Progression coherence | yes | grade 3 readiness, grade 4 retrieval |
| Rigor balance | yes | |
| Named fluencies | yes | finding 3 tightens the year-end item |
| Practices named | yes | all eight |
| Models consistent | yes | layers, tape, area, place-value chart, line plot |
| Precise language | yes | positive factors for scaling claims; inclusive trapezoid; first quadrant only |
| Readiness by grade number | yes | |
| End days not stacked | partly | finding 1 |
| Collect once | yes | |
| Our words | yes | 0 percent |
| Source-map layout | no | finding 4 |

## What is right and should not be touched

- Spaced untimed multiplication warm-ups from day 79 to day 160, with feedback and no visible countdown.
- Grouping symbols taught separately and never nested (days 10, 13, 29), as the standard intends.
- Days 49 and 131, which close real gaps in the base.
- Supplied data in place of home investigations, and the science and social studies timing notes on days 96, 112, 125 and 146.
- The decimal-operation boundary: explained strategies to hundredths, algorithm fluency left to grade 6.

## What I could not judge

- Minute shares within days; the 77.3 percent by minutes is the writer's figure.
- The lead's note that no math digital-tool entry exists; outside this read.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Readiness on m3-area-concepts in the last ten minutes of day 1 | Last used grade 3; unit 1 timing | days.csv day 1 |
| Day 13 stands | Volume parts reuse days 11 and 12; fresh parts are short prompts | days.csv day 13 |
| Day 77 reuses the day 76 untimed sample | Collect once within ten days | days.csv days 76, 77 |
| Home investigations cut for supplied data | Privacy; same mathematics | source-map.csv 5.4.21, 5.6.21 |
| Routines 5.8.14 to 5.8.18 in warm-ups | No full day needed | days.csv days 21, 64, 70, 76, 124 |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grade 5 (openly licensed pages), S:\CurioClass-sources\illustrative-math.
- Common Core State Standards for Mathematics, grade 5, and the progressions documents (number and operations: fractions, number and operations in base ten, geometric measurement).

## For the source list

Nothing new.

## Across the band

Patterns across grades 3 to 5, read against the grade 2 "Across the band":

1. **Readiness is counted right in all three.** Grade 3 retrieves every grade 2 row; grade 4 runs readiness on four grade 2 rows, none on a first day; grade 5 runs it on one grade 3 row in the last ten minutes of day 1. Only grade 3's ledger and frame wording are stale.
2. **Year-end fluency is the weak hand-off, and it improves up the band.** Grade 3 has no direct year-end sample for 3.OA.C.7 or 3.NBT.A.2; grade 4 has none for 4.NBT.B.4; grade 5 keeps 5.NBT.B.5 alive all year and only needs its check item made a performance. The fix is the same at each grade: a short untimed independent station inside the last check, recorded for the handoff. Grade 4 day 1 and grade 5 day 5 then retrieve from real records.
3. **Stacked end days recur in every grade** (grade 3 day 21, grade 4 day 43 and 148, grade 5 day 117), always where an application product already exists a few days earlier and is not named for retention. The pattern grade 5 uses well ("Assessment window: retain ..." on the application day, reused on the end day) is the band fix.
4. **Our words improve up the band:** grade 3 about 5.5 percent with light edits, grade 4 under 1 percent, grade 5 0 percent.
5. **Source maps use three different layouts,** none the band layout, and "split" means three different things. One layout and one decision vocabulary (keep, split for multi-day, merge, cut, ours) should be applied across K to 5.
6. **Major share is thinnest in grade 4** (on the 65 percent line by codes), against about 68 percent in grade 3 and 86 percent in grade 5.
7. **Hand-offs line up.** Grade 3 builds area as multiplication, which grade 4 extends to formulas and grade 5 uses for volume and fraction area; grade 3 unit fractions on the number line feed grade 4 equivalence and grade 5 quotient meaning; the inclusive trapezoid definition holds in all three; the 45-minute shorter path is marked draft in all three.

For the lead:

- Settle one source-map layout and decision vocabulary for the band.
- Settle one standard for a "full performance" on a math end day (proposal: an independent task that shows reasoning on a whole code; short prompts and reused products do not count), so writers stop stacking.
- Fix the frame readiness wording wherever it still says each unit checks the prior grade's rows.
- Ask the grade 4 unit plans to report minutes on major codes.
