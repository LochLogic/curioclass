# Frame read: math-grade-5 (Math Grade 5), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list). By the caller's instruction I did not open the earlier grade 3
  to 5 math planning the lens points to.
- The frame docs/courses/math-grade-5/frame.md and its row in data/plans/frames.csv (10 units, 160 days).
  data/plans/math-grade-5/source-map.csv does not exist; it comes with the scope and sequence.
- The 25 grade 5 rows of data/progressions/math.csv, the grade 4 and grade 6 rows; the frames before and after
  (math-grade-4, math-grade-6).
- The base text in S:\CurioClass-sources\illustrative-math\grade-5: all eight unit overviews and the Addressing tags
  and timelines of all 148 lesson preparation pages; a search of every grade 5 lesson page for brackets and braces.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 5 clusters).
- The same-year frames: science-grade-5, social-studies-grade-5, english-language-arts-grade-5.
- Earlier reads: docs/reviews/frame-math-grade-5-codex-2026-11-14.md (stopped at a missing Python module, judged
  nothing; the gate ran here) and the math grade 2 expert read of today (REPEAT tags).
- Gates: `plan.py check` exit 0; `frame.py check math-grade-5` 0 failures (10 units, 160 days, 145 in units, 15 at
  course level); `stale.py check` 0 failures. My script confirmed all 25 rows placed once and each unit's Owned
  standards equal to its rows' codes.

## Verdict

The frame is sound: every row and lettered part is placed once, the base text's lesson order is kept with unit edges
moved on section lines for stated reasons, all 148 base lessons are placed or cut, and the days add up (123 base
lessons in 123 days, 2 of our own, 20 assessment and respond days in units, 15 at course level). The late coordinate
plane is handled as the brief asks: science and social studies each have an "if later" bridge, and "For the lead"
names a fallback. The biggest risk is 5.OA.A.1: the frame promises brackets and braces in unit 1, but no base lesson
uses them and no day is named; that one sentence of placement is the change that matters most.

## Findings, most serious first

### 1. Brackets and braces (5.OA.A.1) are promised but no lesson carries them (moderate; firm)

**What is wrong.** Unit 1's cell says "parentheses, brackets and braces, evaluated (5.OA.A.1)". The standard reads
"Use parentheses, brackets, or braces in numerical expressions, and evaluate expressions with these symbols." A
search of every grade 5 lesson page in the base text finds parentheses (lessons 1.4, 1.6, 1.9) but no bracket or
brace anywhere; the lessons that tag 5.OA.A.1 (1.6, 1.10, 2.13, 5.18) use parentheses only. Unit 1 has no day of our
own, and the source map names no addition.
**Why it matters.** A day writer adapting the base lessons will teach parentheses only; nested grouping is what
grade 6 expressions (m6-expressions-variables, m6-equivalent-expressions) assume, and check 1 would test what no day
taught. The frame states the standard in full but the plan teaches it in part.
**Fix (frame, unit 1, Source map 5.1 row).** Unit 1, after "(5.OA.A.1)": "brackets and braces are not in the base
text: base lesson 1.10 (expressions for figures made of prisms) adds nested grouping, such as 2 x [3 x (4 + 1)], and
base lesson 2.13 (area and properties, unit 3) adds one with braces; check 1 has an item on each." Source map note:
"1.10 extended with brackets and braces (5.OA.A.1 in full)." LAYER base text. REPEAT yes (lesson 4; math grade 2
finding 5).

### 2. The supply table is stale and two bridges disagree with the science frame (minor; firm)

**What is wrong.** The Cross-subject text says "their frames are written later", but science-grade-5 and
social-studies-grade-5 frames exist and the table already quotes their units. Two "If they come first" cells differ
from the science frame's own bridges: for 5.MD.A.1 this frame says science "converts larger to smaller units only
(kilograms to grams)", the science frame says "All weights on one scale in grams ... no conversion asked"; for
5.NBT.A.2 this frame says numerals and "ten times farther", the science frame reads distances "from a given table
written both ways ... no computing with exponents". The text also says "two of its own rows record science leans";
three do (m5-decimal-operations, m5-measurement-conversion, m5-graph-points). For the lead item 4 still offers moving
unit 10's section A "if the science frame cannot bridge it"; the science frame does bridge it (unit 4: "Shadow data
graphed as bar graphs if math has not yet taught points on a grid").
**Why it matters.** The fixer of each frame reads only its own file; two bridges for one need, and an open fallback
that is no longer needed, invite a change to the base text's order nobody wants.
**Fix (frame, Cross-subject and For the lead item 4).** Header: "...three of its own rows record science leans; the
science and social studies grade 5 frames are written, and the bridges below are theirs." 5.MD.A.1 cell: "Science
weighs every substance in grams on one scale, no conversion (science frame, units 1 and 2)." 5.NBT.A.2 cell:
"Science reads the distances from a given table, written both as numerals and as powers of ten, with no computing
(science frame, unit 4)." For the lead item 4: "Settled: the science frame bridges with bar graphs (its unit 4), so
the base text's order stands; no fallback needed." LAYER process. REPEAT yes (math grade 2 finding 4; the social
studies reads).

### 3. "9 of 10 units mainly major" overstates unit 8 (minor; firm)

**What is wrong.** The Major work bullet counts unit 8 (powers of ten and conversion) as mainly major. Of its seven
base lessons, 6.1 and 6.2 are place value and powers of ten (5.NBT.A, major), 6.3 and 6.4 join conversion to powers of
ten (5.MD.A.1 with 5.NBT.A.2), and 6.5 to 6.7 are multi-step conversion problems (5.MD.A.1, supporting): about half.
By units it is 8 of 10 (80 percent). The days figure holds: my count is about 134 to 137 of 160 (84 to 86 percent),
against the frame's 133.
**Why it matters.** Only the stated figure; the line is far clear either way. A count that does not add up is copied
forward.
**Fix (frame, Major work).** "Units 1 to 7 and 9 are mainly major work (8 of 10, 80 percent by units); unit 8 is about
half, and its conversions practise powers of ten." LAYER frame. REPEAT yes (math grade 2 finding 1, the count).

### 4. Merged review lessons have no rule, and "split" names a routine reuse (minor; firm)

**What is wrong.** The year review merges 8.1 and 8.2, and 8.7 and 8.8 (two 60-minute lessons each into one day) with
no word on what is kept. Row "5.8 | 14 to 18 ... | Warm-ups through the year | split" uses split, defined as one base
unit into two of ours, for five routines that become warm-ups.
**Fix (frame, Source map).** Merge rows: "A merged day keeps one warm-up, the first lesson's main activity in short
form, the second lesson's activities, one synthesis; the dropped activities are named in the day-level source map."
Routines row: decision "cut", note "not days; the five routines are used as warm-ups". LAYER base text. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met: 8 of 10 units (80 percent), about 134 to 137 of 160 days by each lesson's main standard (84 to 86 percent), more by the guide's rule. Finding 3 is the wording only |
| A supporting cluster that does not practise major work | Met: conversion uses powers of ten and decimals (5.MD.A), line plots use this grade's fraction operations (5.MD.B) |
| A source-map row with no keep, split, merge, cut or ours decision | Met, one decision word wrong (finding 4) |
| A skill owned by two grades, a handoff that skips a grade | None. m3-area-concepts (grade 3) is picked up in unit 1 with a readiness check, as the grade 3 and 4 frames say; m5-volume-additive and two fraction rows that skip to grade 7 are named, and the grade 6 frame's "Picked up" table matches |
| A model used before the grade that builds it | None. The coordinate plane and the function table are new here; the standard algorithm for multiplying (unit 5) comes before decimal products (unit 7) |
| A limit broken | None. Division of unit fractions by whole numbers and the reverse only; two-digit divisors without the long-division algorithm; decimals to hundredths in operations; first quadrant only |

## The brief's other checks

- **Owned skills:** 25 rows, each in exactly one unit.
- **Standards in full:** every lettered part placed (5.MD.C.3a, b; 5.MD.C.5a to c; 5.NF.B.4a, b; 5.NF.B.5a, b;
  5.NF.B.7a to c; 5.NBT.A.3a, b). In part: 5.OA.A.1 (finding 1). 5.NF.B.5b's "multiplying by n/n = 1" has a day of
  our own and optional lesson 6.20 kept; 5.NF.B.6's mixed numbers before unlike denominators have a day of our own.
- **Units and reasons:** order holds: quotient meaning before fraction multiplication, multiplication before unit
  fraction division, the algorithm before decimal products, place value to thousandths before decimal operations,
  unlike denominators after decimals (the base text's choice, with the mixed-number day bridging it).
- **Days:** 14 + 7 + 20 + 13 + 22 + 12 + 17 + 9 + 16 + 15 = 145; checks 4, respond 4, year review 7: 160. Each unit's
  count equals its base lessons, its days of our own and two. Unit 2 (7 days, one row) and unit 8 (9 days, two rows)
  are short because their rows are; unit 5 (22) and unit 3 (20) carry the heaviest rows.
- **Source map:** 148 lessons: 123 placed in units (5 of them optional, kept for load), 7 optional cut in units with
  reasons (two because they ask about home life: 4.21 food waste at home, 6.21 weekend activities), and the base
  text's unit 8 as 9 review lessons in 7 days, 4 cut (8.3, 8.9, 8.12, 8.13) and 5 routines: 148. Every new edge falls
  on a section line and keeps the lesson order. No NC or reference source mapped.
- **Review units (empty Skills cell):** none; the base text's unit 8 becomes 7 course-level review days, justified.
- **Seams:** this "Picked up" table matches the grade 4 frame's "Handed on" table; the "Handed on" table matches the
  grade 6 frame's "Picked up" table (fraction-side areas, scaling, first-quadrant graphing and the function table,
  the algorithm, decimals, volume, line plots, m4-factors-multiples and m3-scaled-graphs passing over).
- **Cross-subject:** the rows lean on no other subject. Supplies: the coordinate plane (5.G.A.2, unit 10, days 135 to
  149) comes after science unit 4 (about school days 83 to 108); the science frame bridges with bar graphs, and social
  studies grade 5 needs no bridge (its route uses latitude and longitude). Conversion (unit 8) and powers of ten
  (unit 8) come after science units 1, 2 and 4; each has a bridge (wording in finding 2). Line plots (unit 9, days 119
  to 134) come before science unit 6.
- **Lessons from the social studies frames:** 1 met; 2 met; 3 met (60 minutes; 127 of 148 base lessons are 60 minutes
  by their own timelines); 4 finding 1; 5 met (readiness on grade 3 area opens unit 1); 6 met; 7 met; 8 met, with the
  "if later" lines and the fallback (finding 2 closes it); 9 met; 10 met; 11 met; 12 met (home-life lessons cut); 13
  met; 14 met; 15 finding 2.

## What is right and should not be touched

- Fraction multiplication made one unit (base unit 2 sections B and C with base unit 3 section A), in lesson order.
- The day of our own on mixed-number products, so units 3 and 4 need no unlike denominators.
- Two-digit division kept to partial quotients; the multiplication algorithm tied step by step to partial products.
- The cuts of 4.21 and 6.21 for asking about home life.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Brackets and braces added to base lesson 1.10 and base lesson 2.13; one check 1 item each | The base text has none; 5.OA.A.1 names them | docs/courses/math-grade-5/frame.md, unit 1, Source map |
| Keep the base text's order for the coordinate plane; drop the fallback in For the lead item 4 | The science frame bridges with bar graphs | frame.md, For the lead item 4, Cross-subject |
| Science bridge wording taken from the science frame (grams on one scale; distances read from a table) | One bridge per need | frame.md, Cross-subject |
| Major work by units: 8 of 10 | Unit 8 is about half supporting | frame.md, Major work |
| Merge rule for 8.1 and 2, 8.7 and 8; routines row "cut" | Two 60-minute lessons in one day; "split" is a unit split | frame.md, Source map |

## For Cory

None new. The 60-minute day is already on the frame's "For the lead" list.

## What I could not judge

- Whether 1.10 can hold brackets and braces without crowding its volume work; the unit plan may move it to a warm-up
  pair instead.
- The Progressions page pointers in the "Check set adds" cells were not re-opened.

## Sources

- IM K-12 Math 1st edition, grade 5, local copy (S:\CurioClass-sources\illustrative-math\grade-5, CC BY 4.0): unit
  overviews, optional marks, Addressing tags, timelines; lessons 1.4, 1.6, 1.9, 1.10, 2.13, 5.18 (grouping
  symbols), 6.1 to 6.7, 7.5 (the inclusive trapezoid), 8.1 to 8.18. Firm.
- CCSS mathematics text (5.OA.A.1) and the Student Achievement Partners focus clusters (data/standards/). Firm.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e, as cited with page in
  docs/reviews/frame-math-grade-2-2026-11-14.md; not re-opened on this run.
- Confidence: findings 1 to 4 firm.

## For the source list

None new.

**Verdict:** sound; one moderate fix (5.OA.A.1 brackets and braces). **Finding count:** 4 (1 moderate, 3 minor).
