# Frame read: math-grade-3 (Math Grade 3), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list). The lens also points to docs/courses/math-3-5-progression.md
  and math-4-spine.md; by the caller's instruction I did not open them or any other earlier grade 3 to 5 math
  planning, so this read is not anchored on them.
- The frame docs/courses/math-grade-3/frame.md and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-grade-3/source-map.csv does not exist; it comes with the scope and sequence.
- The 24 grade 3 rows of data/progressions/math.csv, with the grade 2 and grade 4 rows they hand to and from; the
  frames before and after (docs/courses/math-grade-2/frame.md, docs/courses/math-grade-4/frame.md).
- The base text in S:\CurioClass-sources\illustrative-math\grade-3: all eight unit overviews (section and lesson
  titles, optional marks) and the "Addressing" standards on all 143 lesson preparation pages; searches of the
  lesson pages for addition-table work and money.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 3 clusters).
- The same-year frames that lean on or supply this course: science-grade-3, social-studies-grade-3,
  english-language-arts-grade-3.
- Earlier reads: docs/reviews/frame-math-grade-3-codex-2026-11-14.md (stopped at a missing Python module and judged
  nothing; here the gate ran, so its one finding does not apply), and the math grade 2 expert read of today, whose
  findings set the REPEAT tags below.
- Gates: `plan.py check` exit 0; `frame.py check math-grade-3` 0 failures (8 units, 160 days, 144 in units, 16 at
  course level); `stale.py check` 0 failures. A scratchpad script confirmed every grade 3 row placed once, no
  foreign row, and each unit's Owned standards equal to its rows' codes.

## Verdict

The frame is sound and ready for the scope and sequence with small edits: every row and every lettered part is
placed once, the base text's order is kept, all 143 base lessons are placed or cut with a reason, and the days add
up exactly (120 kept lesson days, 8 of our own, 16 assessment and respond days in units, 16 at course level). The
biggest risk is small: the science "if they come first" bridges contradict the science frame now written and two of
them put grade 3 measurement ahead of math. The one change that matters most is to align that table with the
science frame and drop the stale "written later" line.

## Findings, most serious first

### 1. The science bridges disagree with the science frame and run ahead of math (minor; firm)

**What is wrong.** The Cross-subject supply table says, for 3.MD.B.4, "Science measures to the nearest whole or half
inch on a marked ruler", and for 3.MD.A.2, "Science reads a gram scale with whole numbers only". Half inches are
3.MD.B.4 itself (taught here in unit 7, days 117 to 133), and grams are 3.MD.A.2 (unit 7). The science grade 3 frame
(its Cross-subject table and units 1 to 3) bridges differently: lengths in whole inches or whole centimetres, and
the latch criterion "counted in washers held, an equal-unit count with no grams". The table's header also says
"their frames are written later", but docs/courses/science-grade-3/frame.md and social-studies-grade-3/frame.md
both exist and the social studies row already quotes its unit and days.
**Why it matters.** A science writer reading the math frame would use half inches and grams months before math
teaches them (lesson 13, no math ahead of math), and two frames give two bridges for the same need.
**Fix (frame, Cross-subject).** Header: "This course supplies to other subjects in the same year; the science and
social studies grade 3 frames are written, and each bridge below is theirs." 3.MD.B.4 row, last cell: "Science
measures in whole inches or whole centimetres (2.MD.A.1) until unit 7; halves and quarters after it (science frame,
units 1 and 3)." 3.MD.A.2 row: "Science counts an equal unit (washers held) with no grams until unit 7 (science
frame, unit 2)." 3.MD.B.3 row: add "science unit 3 starts near school day 49, after unit 1 ends (day 22): no bridge
needed." LAYER process. REPEAT yes (math grade 2 finding 4; the social studies reads).

### 2. Addition-table patterns are taught in unit 3 but claimed by unit 4 (minor; firm)

**What is wrong.** Unit 4's cell says it teaches "Patterns in the addition and multiplication tables, explained with
the properties (3.OA.D.9)". In the base text, the addition-table patterns are in its unit 3 (lessons 3.2 and 3.5 tag
3.OA.D.9 and use a partly filled addition table), which is our unit 3; its unit 4 has only lesson 4.9 (patterns in
the multiplication table). Unit 3's cell does not say it begins m3-arithmetic-patterns, though it does say so for
two-step problems. (Lessons 1.14, 1.15 and 1.19 also tag 3.OA.D.9 on the multiplication side.)
**Why it matters.** A unit 4 writer would add an addition-table day the base text does not have there, or a unit 3
writer would trim lessons 3.2 and 3.5 as off-topic for add and subtract fluency; either way the "addition table"
half of 3.OA.D.9 is at risk.
**Fix (frame, units 3 and 4).** Unit 3, What students learn, add: "Lessons 2 and 5 begin m3-arithmetic-patterns
(owned by unit 4) with patterns in a partly filled addition table, explained with the properties." Unit 4: "Patterns
in the multiplication table, explained with the properties, and the addition-table patterns of unit 3 recalled
beside them (3.OA.D.9, finished here)." LAYER frame. REPEAT new.

### 3. The merged subtraction lessons have no rule for what a day keeps (minor; firm)

**What is wrong.** Base lessons 3.8 to 3.10 ("Subtraction Algorithms", parts 1 to 3) are "Taught in 2 days". Each
is a 60-minute lesson (warm-up, two or three activities, synthesis, cool-down), so 180 minutes go into 120 with no
word on what is dropped.
**Why it matters.** The scope and sequence writer will either build two overfull days or drop a different part each
time; the same gap sits in grades 4 and 5.
**Fix (frame, Source map, the 3.3 merge row).** Add: "Day 1: lesson 8's warm-up and first activity, lesson 9's
main activity; day 2: lesson 10's two activities; one synthesis and our exit question each day; the dropped
activities are named in the day-level source map." LAYER base text. REPEAT new.

### 4. "split" names a routine reuse in the source map (minor; firm)

**What is wrong.** Row "3.8 | 12 to 15 ... | Warm-ups through the year | split". The frame defines split as "one base
unit into two of ours"; these four lessons become warm-up routines, not a unit.
**Why it matters.** The lens checks that every row carries a defined decision; a mislabelled one will be copied
into the day-level map and the other grades (grades 4 and 5 do the same).
**Fix (frame, Source map).** Decision "cut", note: "Not days; the four routines (notice and wonder, how many do you
see, estimation, number talk) are used as warm-ups across units." LAYER base text. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met. By units 6 of 8 (75 percent). By days, my count by each lesson's main standard (read from its title and Addressing tags), assessment and respond days split in the same share, the year review by its tags and the checks at about three quarters: about 106 of 160 (66 percent), against the frame's 109; the difference is in unit 3 and the checks, and both are above 65. By the evidence guide's rule (supporting work tied to major counts: scaled graphs, line plots, partitioned shapes) about 124 (78 percent) |
| A supporting cluster that does not practise major work | Met. 3.MD.B.3 reads scales by multiplying, 3.MD.B.4 puts halves and fourths on a number line, 3.G.A.2 names unit fractions. 3.G.A.1 is supporting with no stated tie; it is last and short, which is acceptable |
| A source-map row with no keep, split, merge, cut or ours decision | Met, with one decision word wrong (finding 4) |
| A skill owned by two grades, a handoff that skips a grade | None. The three grade 2 rows passing to grade 4 and the two grade 3 rows passing to grades 5 and 6 are named, and grade 4 and grade 2 say the same |
| A model used before the grade that builds it | None. Area model, fraction strip, place value chart and shape hierarchy are introduced here; I found no grade 1 or 2 frame naming a place value chart, so "introduced in grade 3" holds |
| A limit broken | None. Products within 100, denominators 2, 3, 4, 6, 8, no standard algorithm, no unit conversion, angles not measured |

## The brief's other checks

- **Owned skills:** 24 rows, each in exactly one unit; no unit teaches another grade's row except as named review.
- **Standards in full:** every grade 3 standard and lettered part owned (3.MD.C.5a, b; 3.MD.C.7a to d; 3.NF.A.2a, b;
  3.NF.A.3a to d). The two clauses the base text is thin on have days of our own: grouping factors (3.OA.B.5),
  measurement-quantity problems (3.OA.A.3), the order with no parentheses (3.OA.D.8). 3.OA.D.9 is finding 2.
- **Units and reasons:** order holds. Area (unit 2) needs only unit 1's arrays; two-step problems finish in unit 5
  after division and rounding; line plots (unit 7) follow fractions (unit 6); perimeter follows area.
- **Days:** 22 + 16 + 21 + 16 + 14 + 23 + 17 + 15 = 144; checks 4, respond 4, year review 8: 160. Each unit's count
  equals its kept lessons, its days of our own and two. The heaviest rows get the most days (fractions 23, the
  first multiplication unit 22). Unit 3 (21 days on an additional cluster) is the base text's own size less one
  merged day; it is the grade's add and subtract fluency, so I leave it.
- **Source map:** 143 lessons: 121 kept in units in 120 days (three merged into two; two of them optional, 2.11 and
  5.18), five optional cut, 2 required design lessons cut (7.13, 7.14), and the base text's unit 8 split as 8 year
  review days, 3 cut (8.6, 8.7, 8.9) and 4 routines (8.12 to 8.15) as warm-ups: 121 + 5 + 2 + 8 + 3 + 4 = 143. Every cut has a reason. The unit 4 split falls on the base text's
  section edge (A and B, then C and D). No NC or reference source is mapped; Eureka is named as a reference only.
- **Review units (empty Skills cell):** none. The base text's unit 8 becomes 8 course-level review days; its lessons
  tag no new standard, so that is justified.
- **Seams:** the grade 2 "Handed on" table matches this "Picked up" table row for row (including m2-unit-size,
  m2-money and the circle half of m2-halves-thirds-fourths passing to grade 4); the "Handed on" table matches the
  grade 4 frame's "Picked up" table.
- **Cross-subject:** ELA grade 3 teaches SL.3.1 in its unit 1 and RI.3.4 in its unit 2 (about days 40 to 78), both
  before math needs them (units 6 and 5); the "if later" lines are in place anyway. Supplies: finding 1.
- **Lessons from the social studies frames:** 1 met; 2 met; 3 met (60 minutes, five a week; the base lessons are
  60 minutes on 140 of 143 pages); 4 met but for finding 2; 5 met (readiness opens units 1, 3, 6, 7, 8; the
  course-wide rule covers the rest); 6 met; 7 met (no row change needed); 8 met; 9 met; 10 met; 11 met (contexts
  named); 12 met; 13 finding 1; 14 met; 15 finding 1.

## What is right and should not be touched

- The base text's order, including scaled graphs opening multiplication and line plots after fractions.
- The days of our own: each answers a clause the base lessons leave thin, not a taste.
- Facts as strategies in unit 4 and spaced, untimed, own-score practice after it; no timer anywhere.
- Mass taught in grams and kilograms where the base text says "weight", and no student weighing themselves.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Addition-table patterns begin in unit 3 (base lessons 3.2, 3.5); unit 4 finishes 3.OA.D.9 | That is where the base text teaches them | docs/courses/math-grade-3/frame.md, units 3 and 4 |
| The 3.8 to 3.10 merge keeps lesson 8's first activity and lesson 9's and 10's main activities, one synthesis a day | 180 minutes into two 60-minute days; the algorithm is not required in grade 3 | frame.md, Source map |
| Base lessons 8.12 to 8.15: decision "cut", reused as warm-up routines | "split" is defined as a unit split | frame.md, Source map |
| Science bridges: whole units until unit 7; an equal-unit count (washers) for mass | Match the science frame and keep math first | frame.md, Cross-subject |

## For Cory

None new. The 60-minute day is already on the frame's "For the lead" list.

## What I could not judge

- Whether warm-ups can carry the daily facts practice and the cut center routines; the unit plans will show it.
- The Progressions page pointers in the "Check set adds" cells were not re-opened.

## Sources

- IM K-12 Math 1st edition, grade 3, local copy (S:\CurioClass-sources\illustrative-math\grade-3, CC BY 4.0): unit
  overviews, optional marks, every lesson's Addressing tags and Lesson Timeline; lessons 3.2 and 3.5 (addition
  table), 3.8 to 3.10, 8.5 (tiny house cost in whole dollars). Firm.
- CCSS mathematics text and the Student Achievement Partners focus clusters (data/standards/). Firm.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e (supporting work connected to major work is counted), as cited
  with page in docs/reviews/frame-math-grade-2-2026-11-14.md; not re-opened on this run.
- Confidence: findings 1 to 4 firm.

## For the source list

None new.

**Verdict:** sound; minor edits. **Finding count:** 4 (all minor).
