# Frame read: math-grade-2 (Grade 2 Math), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-grade-2/frame.md and its row in data/plans/frames.csv (9 units, 160 days).
  data/plans/math-grade-2/source-map.csv does not exist yet; it comes with the scope and sequence.
- The 28 grade 2 rows of data/progressions/math.csv, the grade 1 rows before and the grade 3 rows after; the frames
  before and after (docs/courses/math-grade-1/frame.md, docs/courses/math-grade-3/frame.md, which now exists).
- The base text in S:\CurioClass-sources\illustrative-math\grade-2: every unit overview and all 146 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), with grades 1 and 2 searched for "tape
  diagram".
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 2 clusters).
- The same-year frames: docs/courses/science-grade-2/frame.md and docs/courses/social-studies-grade-2/frame.md (no
  ELA grade 2 frame exists yet).
- Earlier reads: the social studies frame reads and fixes of 2026-11-13, the math progression reads of 2026-11-13,
  and docs/reviews/frame-math-grade-2-codex-2026-11-14.md. That Codex read stopped at the gate (its Python lacked a
  module) and judged nothing; here `plan.py check` ran in full, so its one finding does not apply to this run.
- Gates: `plan.py check` exits 1 only on math-grade-6 unit 6, outside this read; `frame.py check math-grade-2`
  0 failures (9 units, 160 days, 154 in units, 6 for checks and respond days); `stale.py check` 0 failures.

## Verdict

The frame is sound: all 28 rows are placed once, every grade 2 standard and lettered part is owned, the base text's
nine units are kept in its own order (ruler, then number line, then three-digit numbers placed on it), the days add
up (138 kept lessons, 7 Curio Class lessons, 9 assessment days) and every base lesson is placed or cut with a named
decision. The biggest risk is the reason for the eight cuts: they are said to keep major work above 75 percent, but
every cut day practises major work by the base text's own tags, and the reviewer's guide counts supporting work tied
to major work, so the cuts lower the fluency practice they were meant to protect. The one change that matters most
is to give the true reason (the day budget) and spend the cuts and additions by load, as settled below.

## Findings, most serious first

### 1. The center-day cuts rest on a miscount of major work (moderate; firm)

**What is wrong.** The frame cuts eight optional lessons (2.1.12, 2.3.17, 2.6.5, 2.6.10, 2.6.14, 2.6.21, 2.8.6,
2.8.13) "so that major work stays above 75 percent by days", and says keeping them "would put major work at about 71
percent". By the base text's own Addressing tags, all eight practise major work: for example 2.1.12 (2.NBT.B.5,
2.OA.B.2), 2.6.14 (2.NBT.B.5, B.6), 2.8.6 (2.NBT.B.7, B.8, 2.OA.B.2), 2.8.13 (2.NBT.A.2, B.7). The EdReports evidence
guide says "connections between supporting work and major work should be included in the calculations" for indicator
1e (PDF page 14 (printed 13)), and the frame itself says units 6 and 8 practise major work on purpose (money adds
within 100, time skip-counts, arrays use repeated addition). Counted that way, most of units 6 and 8 count, and major
work is near 88 percent whether or not the center days stay. The real constraint is the day budget: 146 base lessons,
9 assessment days and 6 check days are already 161, so some cut is needed whatever the major-work count. My count of
kept lessons with a major tag is 121 of 138, not 123.
**Why it matters.** The two fluency targets (2.OA.B.2, 2.NBT.B.5) are what these center games practise; the cut is
made for a reason that does not hold, and the next writer will repeat the method and cut more supporting days that
carry major practice. "Unit 6 ... cut here so the year stays above the major-work line" and "Two optional center days
cut to keep the year above the major-work line" (unit 8) carry the same error.
**Fix (frame, Days, Major work, units 6 and 8, For the lead item 2).** Days: "146 base lessons, 9 assessment days and
6 check and respond days exceed 160, so eight optional lessons are cut (the base text marks them optional; their
games move into warm-ups) to make room for seven Curio Class lessons where the load is heaviest." Major work: count
with the guide's rule (major clusters plus supporting work that practises them) and state the three numbers; drop
"about 71 percent". Units 6 and 8: replace the major-work line in each reason with "four (two) optional center and
puzzle days are cut for the day budget; their games move into warm-ups". For the lead item 2: same reason. LAYER
frame. REPEAT new (first math frame read; the social studies frames have no major-work line).

### 2. The added estimating lesson repeats four base lessons, while a center day is cut (minor; firm)

**What is wrong.** Unit 3 adds "estimating lengths in inches, feet, centimeters and meters with benchmarks (2.MD.A.3)"
in place of center day 2.3.17. The base text already teaches estimating in each unit: 3.4 (Measure and Estimate in
Centimeters), 3.5 (meters), 3.8 (What is an Inch?) and 3.9 (From Feet to Inches) all address 2.MD.A.3. The cut 2.3.17
practises measuring, line plots and adding within 100 (2.MD.A.1, A.3, A.4, D.9, 2.NBT.B.5, 2.OA.B.2).
**Why it matters.** Lesson 9 of the brief: days go by load. The added day spends time on a standard the base text
already covers four times, and the day it replaces practised a fluency target.
**Fix (frame, unit 3 and source map).** Settled below: keep 2.3.17 and drop the added estimating lesson. Source map:
"2.3 | 1 to 18 (7, 13, 17, 18 optional) | 3 | Keep all"; delete the 2.3 Cut row and the unit 3 Ours row. Unit 3 text:
"estimating with benchmarks (base lessons 3.4, 3.5, 3.8, 3.9)". Course brief and totals: six Curio Class lessons, and
"146 base lessons, 139 placed, 7 cut; 6 Curio Class lessons; 9 assessment days"; unit 3 stays 19 days. LAYER base text. REPEAT new.

### 3. The tape diagram's handoff is worded as if grade 1's base text taught it (minor; firm)

**What is wrong.** The Models table says the tape diagram comes from "Grade 1 (m1-all-problem-types, late in grade
1)" and is "introduced or first used" in unit 1 here. The base text teaches the tape diagram for the first time in
grade 2 lessons 1.14 to 1.16, built from the bar graph; grade 1's base lesson 8.6 calls its drawing a precursor to the
grade 2 tape diagram. The grade 1 read asks the grade 1 frame to adapt its unit 6 lessons so the model is taught there
(grade 1 read, finding 1). Unit 1's readiness check names "facts within 10 and problem types" but not the diagram.
**Why it matters.** Lesson 6 of the brief: one thread keeps one wording across grades, and a "first" claim is checked
against the grade before. Unit 1's writer needs to know whether students arrive with the model.
**Fix (frame, Models table and unit 1).** Models row: "Grade 1 unit 6 (redrawn from the base text's cube diagrams) |
Unit 1: built again from the bar graph, as the base text does (2.1.14 to 2.1.16), for all Compare subtypes". Unit 1's
readiness check: add "a Compare problem shown with a tape diagram". LAYER frame. REPEAT yes (lesson 6).

### 4. A cross-subject reason and a status line do not match the science frame now written (minor; firm)

**What is wrong.** Unit 3's reason says "Grade 2 science measures plants and seeds with rulers in the fall". The
science grade 2 frame measures with a ruler first in its erosion unit (s2-erosion-solutions, about week 9); plant
height is about week 23 and the model seed about week 27. The science table gives the 2-LS2-1 plant-height lean
"About week 8". The Cross-subject section still says "The other subjects' frames are written later", though this
frame quotes the social studies grade 2 frame.
**Why it matters.** The availability calendar is what the science frame honours; the erosion lean (week 9, in math
unit 3's first two weeks) is the one that is tight, and it is not in the "used here" table.
**Fix (frame).** Unit 3 reason: "Grade 2 science first reads a ruler in centimeters about week 9 (erosion), in this
unit's second week; its plant and seed measuring comes in the spring". Science table: m2-measure-with-tools needed
by "about week 9 (s2-erosion-solutions), then week 23 (plant height)". Cross-subject opening: "The science and social
studies grade 2 frames are written and their weeks are used below; the ELA grade 2 frame sets its own." LAYER
process. REPEAT yes (the social studies reads found stale notes and lean weeks that did not match).

### 5. 2.G.A.3 is described in part (minor; firm)

**What is wrong.** Unit 6 gives "two, three or four equal shares (halves, thirds, fourths), and equal shares of the
same whole that are not the same shape". The standard also asks for the phrases "half of, a third of" and to
"describe the whole as two halves, three thirds, four fourths". The kept base lessons 6.7 to 6.9 teach it; the frame's
cell is short.
**Why it matters.** Lesson 4 of the brief, and grade 3's unit fractions start from "the whole as b parts".
**Fix (frame, unit 6).** Add: "the phrases half of and a third of, and the whole as two halves, three thirds or four
fourths (2.G.A.3 in full)". LAYER standard. REPEAT yes (the social studies reads found standards narrowed to their
headline).

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met, but miscounted (finding 1). By the frame's own method 7 of 9 units, 122 of 160 days (76 percent); by the guide's rule, which counts supporting work connected to major work, well above the line |
| A supporting cluster that does not practise major work | Met. Money adds within 100, time skip-counts by 5s, odd and even and arrays use doubles and repeated addition, line plots use rulers and subtraction |
| A source-map row with no keep, split, merge, cut or ours decision | Met; every row has one |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None. The two threads that end in grade 2 and the three that pass grade 3 are named, and the grade 3 frame says the same |
| A model used before the grade that builds it | None. Ruler (unit 3) before number line (unit 4) before three-digit numbers placed on it (unit 5) |
| A limit broken | None. Within 100 fluently, within 1000 with methods, no standard algorithm, arrays to 5 by 5, scale of one, time to five minutes |

## The brief's other checks

- **Owned skills:** all 28 rows placed once. No unit teaches another grade's skill.
- **Standards in full:** every grade 2 standard and lettered part owned; 2.G.A.3 wording short (finding 5); 2.OA.A.1,
  2.NBT.B.5 and 2.NBT.B.7 begun and finished as stated.
- **Units and reasons:** order holds; the reasons in units 3, 6 and 8 need the edits in findings 1 and 4.
- **Days:** 154 + 4 + 2 = 160; each unit's days are its kept and added lessons plus one assessment day. Unit 7 (21
  days, two heavy rows) and unit 2 (19, five rows) are weighted as their loads ask.
- **Source map:** 146 lessons, 138 placed, 8 cut, each named; the optional marks match the base text in every unit.
  Eureka named only as a check-set reference.
- **Seams:** the grade 1 table matches the grade 1 frame's "Handed on" table row for row; the grade 3 table matches
  the grade 3 frame's "Picked up" table, including m2-unit-size and m2-money passing to grade 4 and the models
  (number line, dot plot, tape diagram, bar graph, array, base-ten blocks) that grade 3 lists.
- **Cross-subject:** social studies grade 2 has no same-year lean on math (its frame agrees); the grade 1 social
  studies lean (saving) is the year before; science is finding 4.
- **Unit 9 with an empty Skills cell:** justified. The base text's closing spaced review of the major work and both
  fluency targets, before the end-of-year check; its 13 lessons need a home.
- **Lessons from the social studies frames:** 1 met; 2 met; 3 met; 4 finding 5; 5 met (readiness checks in units 1,
  2, 3 and 5); 6 finding 3; 7 met (For the lead item 4); 8 met; 9 finding 2; 10 met; 11 met; 12 met (the saree silk
  reader named, who and pay left to Cory); 13 not applicable; 14 met; 15 finding 4.

## What is right and should not be touched

- The base text's order of the ruler, the number line and three-digit numbers, and the progression's reason for it.
- Decomposing a ten early, beside subtraction without it; subtracting across a zero named as its own day.
- Fluency checked by watching and short untimed items, never a timer.
- The sensitivity notes on money, odd and even (never pairing children) and the saree silk lessons.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Keep base lesson 2.3.17 (Center Day 3) and drop the added estimating lesson; unit 3 stays 19 days | The base text already teaches 2.MD.A.3 in 3.4, 3.5, 3.8 and 3.9; the center day practises measuring and fluency within 100 | docs/courses/math-grade-2/frame.md, unit 3 and source map |
| The eight (now seven) cuts are justified by the day budget, not by the major-work line | Every cut day practises major work by the base text's tags | frame.md, Days, Major work, units 6 and 8, For the lead item 2 |

## For Cory

None new. The saree silk reader (who, and any pay) is already on the frame's "For the lead" list.

## What I could not judge

Whether warm-ups can absorb all the cut center games; the unit plans will show it.

## Sources

- IM K-12 Math 1st edition, Grade 2 and Grade 1, local copy (S:\CurioClass-sources\illustrative-math, CC BY 4.0):
  lesson lists, optional marks and Addressing tags of every lesson; grade 2 lessons 1.14 to 1.16, 3.4 to 3.9, 6.7
  to 6.9; grade 1 lesson 8.6.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf, PDF pages 13 to 15 (printed 12 to
  14): supporting work connected to major work is counted. Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv.
- Confidence: findings 1 to 5 firm.

## For the source list

None new.
