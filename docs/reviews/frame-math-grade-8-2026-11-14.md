# Frame read: math-grade-8 (Math Grade 8), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-grade-8/frame.md (all of it) and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-grade-8/source-map.csv does not exist yet; it comes with the scope and sequence.
- The grade 8 rows of data/progressions/math.csv and the grade 7 and high school rows they meet; the frames before and
  after, docs/courses/math-grade-7/frame.md and docs/courses/algebra-i/frame.md ("Picked up"), and the m8 rows of
  docs/courses/geometry/frame.md.
- The base text in S:\CurioClass-sources\illustrative-math\grade-8: every unit overview and all 131 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), lessons 8.6.1 to 8.6.8 in full and 8.1.16, the
  IM 6 to 8 pacing guide and dependency chart.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 8 clusters).
- The same-year frames: docs/courses/science-grade-8/frame.md, the civics frame
  (civics-government-and-civic-life) and docs/courses/english-language-arts-grade-8/frame.md.
- Earlier reads: docs/reviews/frame-math-kindergarten-2026-11-14.md, the grade 2, 3 and 5 math frame reads,
  progression-math-*2026-11-13.md and progression-cross-2026-11-13.md. No earlier read of this frame exists.
- Gates: `plan.py check` exits 0; `frame.py check math-grade-8` 0 failures (8 units, 160 days, 154 in units, 6 for
  checks and respond days); `stale.py check` 0 failures.

## Verdict

The frame is sound and its one move from IM's order holds: IM's chart lets the data unit (8.6) follow linear
relationships (8.3), and science 8's real days (scatter plots in its unit 4, days 78 to 105) show that IM's order would
have come too late. All 36 owned codes sit in one unit and all 131 IM lessons are placed or cut with a reason. The most
serious problem is that the moved unit's lessons are kept as written though they speak the language of functions,
which now comes two units later; the source map must say they are adapted. Major work is well over the line (about 81
percent of days, 85 percent of kept lessons by IM's tags).

## Findings, most serious first

### 1. The data unit moves ahead of functions but its lessons are kept as written, in function language (moderate; firm)

**What is wrong.** IM 8.6 is written to follow 8.5 (Functions and Volume). Its lessons lean on that: 8.6.1 contrasts a
scatter plot with plotting points for a function; 8.6.2 asks whether hand span is a linear function of height; 8.6.3
says dog weight is not a function of dog height; 8.6.4 and 8.6.5 speak of a linear function as a model; 8.6.8 of the
rate of change of the function. The practice sets review "From Unit 5" lessons 17 and 18, which this frame cuts. The
source map row is "keep" for 1 to 10, and the m8-scatter-plots row says it "practises the linear functions of 8.F".
**Why it matters.** Lesson 5 and the lens line "a model before the grade (or unit) that builds it": a writer keeping
these lessons as written teaches the word function two units before unit 6 defines it, and the cumulative practice
points at cut lessons.
**Fix (frame, source map, unit 4, unit 6 and For the lead).** Source map: "8.6 | 1 to 10 | 4 | keep; adapt 1 to 5 and
8: say relationship, line, or the equation of a line y = mx + b (unit 3), not function; replace the practice problems
drawn from IM unit 5 with unit 1 to 3 review". Unit 6 "What students learn", add: "opens by naming the scatter-plot
lines of unit 4 as linear functions". For the lead: "m8-scatter-plots row note to read: practises the linear
relationships of 8.EE.B (unit 3); the progression fixer edits math.csv." Close For the lead item 2: "Science 8's frame
places base unit 8.4 (gravity and mass, scatter plots) at days 78 to 105 and base unit 8.5 at days 106 to 130; in IM's
order the data unit would fall about days 101 to 114, after science's unit 4 begins. The move stands." LAYER base
text. REPEAT yes (the kindergarten read found the same: a move in the frame not carried into the source map's "keep").

### 2. 8.G.A.5 and 8.NS.A.2 are not taught in full (minor; firm)

**What is wrong.** 8.G.A.5 asks for informal arguments about "the angle sum and exterior angle of triangles, about the
angles created when parallel lines are cut by a transversal, and the angle-angle criterion for similarity of
triangles". Unit 1 names alternate interior angles and the triangle sum; the exterior angle and the full set of
transversal angle pairs are not named, and IM gives the exterior angle only one practice problem (8.1.16). 8.NS.A.2's
"estimate the value of expressions (e.g., π²)" is not named in unit 8.
**Why it matters.** Lesson 4: standards in full. The exterior angle is the one 8.G.A.5 item a reviewer looks for and
does not find in IM's activities.
**Fix (frame, units 1 and 8; source map).** Unit 1 add: "the exterior angle of a triangle equals the sum of the two far
interior angles, and the angle pairs on a transversal (corresponding, alternate interior, same-side) (8.G.A.5 in full,
with the angle-angle criterion in unit 2)". Source map 8.1 row: "adapt 16: add an activity on the exterior angle".
Unit 8 add: "estimating the value of expressions with irrational numbers, such as π² or √2 + 1 (8.NS.A.2 in full)".
LAYER standard. REPEAT yes (the kindergarten read found the same).

### 3. The Algebra I and Geometry frames now exist; the hand-on table says they do not (minor; firm)

**What is wrong.** The Seams section says "Handed on to Algebra I and Geometry ... their frames are not written, so the
rows are named, not their units". Both frames are written (2026-11-14). Algebra I's "Picked up" table names a unit for
every grade 8 hand-on except m8-proportional-compare and m8-scientific-notation, which this frame already raises in
For the lead item 6; the Geometry frame picks up the grade 8 geometry rows.
**Why it matters.** Lesson 15: no status lines about other files. Lesson 7: both ends of a handoff.
**Fix (frame, Seams).** Replace the status sentence with "Handed on to Algebra I and Geometry (their frames name the
units)" and fill the "What the next course does with it" column with the units from algebra-i/frame.md (unit 2: linear
equations, graphs and systems; unit 3: scatter plots, linear models, two-way tables; unit 4: functions; unit 5:
exponents; unit 7: roots and irrational numbers) and geometry/frame.md for the transformation, angle and Pythagorean
rows. LAYER process. REPEAT yes (lesson 15).

### 4. Curio Class days are unnamed in units 2, 5, 6, 7 and 8, and unit 4's mid-unit check has no respond day (minor; firm)

**What is wrong.** The source map names the Curio Class days for units 1, 3 and 4 only. Unit 4's are "readiness and
practice, mid-unit check, assessment, respond": the mid-unit check has no respond day.
**Why it matters.** Lessons 1 and 9.
**Fix (frame, source map).** Unit 4: "readiness, mid-unit check and respond, assessment and respond" (practice moves
into the 5-minute openings). Unit 2: "readiness with scale, assessment and respond". Units 5 and 6: "mid-unit check
and respond, mixed practice, assessment and respond". Units 7 and 8: "mid-unit check and respond, assessment and
respond". LAYER frame. REPEAT yes (days by load).

### 5. Cross-subject rows give guessed days where science 8 now has its own (minor; firm)

**What is wrong.** The rows ask science 8's base unit 8.4 to come "after about day 60" and treat the kinetic-energy
graphs (base unit 8.1) as the only qualitative-graph lean. Science 8's frame places its units 1 and 2 at days 1 to 48,
with s8-wave-amplitude-energy as well as s8-kinetic-energy-graphs reading relationships from graphs; its unit 4 at days
78 to 105 and unit 5 at days 106 to 130. The scatter-plot leans are therefore available (math days 56 to 69); the
graph-reading leans come before unit 6 (days 93 to 116) and need their bridge.
**Why it matters.** The availability calendar; the "if later" line must reach every lean that needs it.
**Fix (frame, Cross-subject).** Scatter-plot rows: "Available: science 8 unit 4 is days 78 to 105, unit 5 days 106 to
130." Graph-reading row: name both s8-kinetic-energy-graphs and s8-wave-amplitude-energy, "science units 1 and 2, days 1
to 48: earlier; science reads the shape of a graph in words with grade 7 proportional graphs and asks for no function
or rate of change." The civics row (polling data, about days 52 to 63) is right. LAYER process. REPEAT yes (lesson 15).

### 6. The by-units focus line overstates (minor; firm)

**What is wrong.** "By units: 6 of 8 wholly major". Units 1, 2, 3, 5 and 7 are wholly major; unit 8 includes 8.NS.A,
which is supporting; unit 6's volume (8.G.C.9) is additional. By days the frame's 81 percent holds; my count from IM's
tags is 103 of 121 kept lessons (85 percent).
**Why it matters.** A reviewer checking the claim finds it wrong and trusts the rest less; the margin needs no help.
**Fix (frame, course in brief).** "By units: 5 of 8 wholly major, unit 8 mostly (8.NS.A supporting), unit 6 partly.
By lessons, from IM's tags: 103 of 121 kept lessons touch major work (85 percent)." LAYER frame. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met: about 81 percent of days, 85 percent of kept lessons, 5 of 8 units wholly major (finding 6) |
| A supporting cluster that does not practise major work | Met. The data unit uses lines and slope (8.EE.B); volume as a function practises 8.F; irrational numbers serve the Pythagorean theorem |
| A source-map row with no keep, split, merge, cut or ours decision | Met on decisions; the 8.6 and 8.1 rows need "adapt" written in (findings 1 and 2) |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None found. Grade 7's hand-ons are picked up; Algebra I and Geometry pick up the rest (finding 3) |
| A model used before the unit that builds it | Function language in the moved unit (finding 1); fixed by adapting, not by moving |
| A limit broken | None. Volume problems before roots use perfect squares and cubes only, as IM does (For the lead item 5 is right) |

## The brief's other checks

- **Owned skills:** all grade 8 rows placed once; all 36 codes owned. ~8.F.A.3 and ~8.F.B.4 are begun in unit 3
  (linear relationships), named as such.
- **Standards in full:** finding 2; the rest are named in full.
- **Units and reasons:** IM's chart (8.1 to 8.2 to 8.3; 8.3 to 8.4, 8.5, 8.6; 7.8 to 8.6; 6.6 to 8.7; 6.1 to 8.8)
  allows the one move, and its reason is now confirmed by science 8's days.
- **Days:** 20 + 16 + 19 + 14 + 21 + 24 + 20 + 20 = 154, plus 6 = 160; 121 IM days plus 33 Curio Class days. No unit far
  over or under its load.
- **Source map:** 131 lessons accounted for; optional cuts match IM (8.5.17, 8.5.18, 8.5.22, 8.6.11, all of 8.9). No
  NC or reference source mapped.
- **Seams:** grade 7 hand-ons picked up; the hand-ons to high school are finding 3.
- **Cross-subject:** finding 5; every lean carries an "if later" line.
- **Lessons from the social studies frames:** 1 finding 4; 2 met; 3 met (50 minutes); 4 finding 2; 5 finding 1; 6 met;
  7 finding 3; 8 met; 9 finding 4; 10 met; 11 met; 12 met (data sets avoid body measures and family votes); 13 met;
  14 met; 15 findings 3 and 5.

## What is right and should not be touched

- Moving the data unit to fourth place, with the chart cited and the reason tied to science.
- Volume before roots, in IM's order, with perfect squares and cubes.
- The neutral polling context and the rule that no student's family vote is asked.
- The standard three-year path as the frame's default (accelerated path left as Cory's scope question, For the lead
  item 4).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| The data unit stays fourth; lessons 8.6.1 to 5 and 8 are adapted to relationship and line language | IM's chart allows it; science 8 needs scatter plots by about day 78 | docs/courses/math-grade-8/frame.md, source map, units 4 and 6, For the lead item 2 |
| 8.1.16 gets an exterior-angle activity | 8.G.A.5 names it; IM gives it one practice problem | frame.md, unit 1 and source map |
| Curio Class days per unit as in finding 4 | A respond day after each check | frame.md, source map |

## For Cory

- Already in the frame and still his: whether an accelerated path (Algebra I in grade 8) is offered (For the lead
  item 4). Nothing new.

## What I could not judge

Whether science 8's gravity unit asks students to draw a line of fit or only to describe a trend; its frame says
trend in words, and I took it at its word.

## Sources

- IM K-12 Math 1st edition, grade 8, local copy (S:\CurioClass-sources\illustrative-math\grade-8, CC BY 4.0): lesson
  lists, optional marks, Addressing tags, lessons 8.1.16 and 8.6.1 to 8.6.8, the 6 to 8 pacing guide and dependency
  chart.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf. Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv; CCSS text via
  data/standards/ccss-math-standards.txt.
- Confidence: findings 1 to 6 firm (each rests on IM's own pages, the standard's text or another frame's own table).

## For the source list

None new.
