# Frame read: math-grade-7 (Math Grade 7), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-grade-7/frame.md (all of it) and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-grade-7/source-map.csv does not exist yet; it comes with the scope and sequence.
- The grade 7 rows of data/progressions/math.csv and the grade 6 and 8 rows they meet; the frames before and after,
  docs/courses/math-grade-6/frame.md and docs/courses/math-grade-8/frame.md.
- The base text in S:\CurioClass-sources\illustrative-math\grade-7: every unit overview and all 145 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), lesson 7.4.5 in full, the IM 6 to 8 pacing
  guide and dependency chart, and the IM middle school teacher guide.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 7 clusters).
- The same-year frames the course leans on: docs/courses/science-grade-7/frame.md, docs/courses/science-grade-6/frame.md
  (for the MS-PS1-4 context), the social studies 7 frame (world-geography-and-ancient-civilizations-ii) and
  docs/courses/english-language-arts-grade-7/frame.md.
- Earlier reads: docs/reviews/frame-math-kindergarten-2026-11-14.md, the grade 2, 3 and 5 math frame reads,
  progression-math-*2026-11-13.md and progression-cross-2026-11-13.md. No earlier read of this frame exists.
- Gates: `plan.py check` exits 0; `frame.py check math-grade-7` 0 failures (8 units, 160 days, 154 in units, 6 for
  checks and respond days); `stale.py check` 0 failures.

## Verdict

The frame is sound: IM's order is kept, all 43 owned grade 7 codes sit in exactly one unit, every one of IM's 145
lessons is placed or cut with a reason, and the days add up (123 IM days plus 31 Curio Class days, plus 6 course-level
days). The most serious problem is a thread placed in the wrong unit's text: IM teaches decimal expansions (7.NS.A.2d)
in unit 4, lesson 5, but the frame and the progression row put it in unit 5, where no IM lesson teaches it. Focus is
fine under the evidence guide's rule (about 71 percent), and the frame's own count needs its arithmetic fixed and the
connections named on the page.

## Findings, most serious first

### 1. Decimal expansions (7.NS.A.2d) are taught in IM's unit 4 but placed and described in unit 5 (moderate; firm)

**What is wrong.** m7-decimal-expansion sits in unit 5 (rational number arithmetic). IM teaches long division to
terminating and repeating decimals in 7.4.5 "Say It with Decimals" (activity "Repeating Decimals"), inside unit 4;
no lesson of IM 7.5 teaches it. The row's note, "IM 7.4.4 and 7.5.12", points to the wrong lessons (7.4.4 is "Half as
Much Again", 7.5.12 is "Negative Rates"). Unit 4's text does not mention 7.NS.A.2d. In the same way, unit 5's lessons
7.5.11 and 7.5.14 to 16 already solve equations of the form px = q and x + p = q with signed numbers (IM tags 7.EE.B.4a),
which unit 6 owns, and unit 5 does not say so.
**Why it matters.** Lesson 5: a thread starts where it is first used. A unit 4 writer will not know lesson 5 is the
decimal-expansion lesson; a unit 5 writer will look for a lesson that is not there, and the standard's "why it ends or
repeats" half and its extension to signed numbers get no day.
**Fix (frame, units 4 and 5; For the lead).** Unit 4 "What students learn", add: "long division of a fraction to a
decimal that ends or repeats (IM 7.4.5; 7.NS.A.2d begun here, owned in unit 5)". Unit 5: name one of its 6 Curio Class
days as "decimal expansions finished: why every fraction's decimal ends or repeats, and the decimals of negative
rational numbers (7.NS.A.2d in full)". Unit 5 also add: "equations with signed numbers (IM 7.5.11, 14 to 16; 7.EE.B.4a
begun here, owned in unit 6)". For the lead: "m7-decimal-expansion row note to read IM 7.4.5, with a Curio Class day
in unit 5; the progression fixer edits math.csv." Keeping the row in unit 5 needs no scope decision; moving it to unit
4 would move a standard between units and is Cory's call, and is not needed. LAYER frame and base text. REPEAT yes
(the kindergarten read found a thread started before its owning unit).

### 2. The focus count's arithmetic is off and the connections are not on the page (minor; firm)

**What is wrong.** "Major work" says about 98 of 160 days strictly, from "units 2, 4, 5, 6, the ratio days of unit 1
and about two thirds of the course-level days". Units 2, 4, 5 and 6 are 21 + 22 + 23 + 28 = 94 and two thirds of 6 is
4: that is already 98, leaving the ratio days of unit 1 at zero. The by-units line ("4 of 8 strictly, 5 of 8 with unit
1") does not count unit 8, whose sampling and probability lessons use percent and proportional reasoning. My count
from IM's "Addressing" tags: 88 of 126 kept lessons (70 percent) touch a grade 7 major cluster (units 1: 6 of 12, 2: 15
of 15, 3: 3 of 9, 4: 16 of 16, 5: 17 of 17, 6: 23 of 23, 7: 4 of 16, 8: 4 of 18, or 15 of 18 counting proportional work
in its supporting tags); by days about 115 of 160 (72 percent).
**Why it matters.** The strict count by owning rows, 61 percent, is in the evidence guide's 60 to 64 percent band.
Indicator 1e counts supporting work that is connected to major work, but a reviewer credits the connection only where
the materials show it; the frame names it for unit 1 alone.
**Fix (frame, course in brief and For the lead item 2).** "Counted by days: 98 of 160 (61 percent) by owning rows
(units 2, 4, 5 and 6 and two thirds of the course-level days); about 114 (71 percent) with connected supporting work,
the evidence guide's rule. By units: 4 of 8 strictly, 6 of 8 with units 1 and 8. By lessons, from IM's tags: 88 of 126
kept lessons touch major work (70 percent)." In units 1, 3, 7 and 8 add one line naming the major work practised:
unit 1 scale factors as constants of proportionality (7.RP.A.2, IM 7.1.2, 3, 5, 6, 8, 10); unit 3 circumference as a
proportional relationship (7.RP.A.2, IM 7.3.1, 3, 7); unit 7 angle and volume equations (7.EE.B.4a); unit 8
probabilities and population estimates as percents and proportions (7.RP.A.3). Close item 2 with option (a). LAYER
frame. REPEAT yes.

### 3. Units 4 and 5 do not say what their 6 Curio Class days are (minor; firm)

**What is wrong.** The source map names the Curio Class days for units 2 and 6 but gives units 4 and 5 only "6 ours",
and unit 7 and 8 only "2 ours".
**Why it matters.** Lesson 9 (days by load) and lesson 1 (a respond day after each check). Unit 5 also needs one of its
days named for finding 1.
**Fix (frame, source map).** Unit 4: "readiness, mixed practice, mid-unit check and respond, assessment and respond".
Unit 5: "decimal expansions finished (finding 1), mid-unit check and respond, mixed practice, assessment and respond".
Units 1, 3, 7, 8: "assessment and respond". LAYER frame. REPEAT yes (days by load).

### 4. Cross-subject rows are written against guesses, and one lean names the wrong course (minor; firm)

**What is wrong.** The MS-PS1-4 row (temperature across zero) is labelled Science 7, but that performance expectation
is placed in science 6 (s6-state-change); it is an earlier-grade context, already available. The s7-design-optimize row
says science 7's base unit 7.2 "should come after about day 33"; science 7's frame places its unit 2 at days 24 to 42
with the design work late in it, so the timing is close, not settled. Science 7's population unit (its unit 6, days 129
to 158) is long after unit 4's percent (days 47 to 68): available. Social studies 7's time zones (about days 78 to 86)
fall just after unit 5's adding and subtracting (days 69 to 77): available, and the frame's line holds.
**Why it matters.** The availability calendar needs real days; a lean filed under the wrong course is never checked by
the right one.
**Fix (frame, Cross-subject).** Move the MS-PS1-4 row to "Earlier grades this course assumes from other subjects:
s6-state-change (temperatures below zero on a thermometer), used as a context in unit 5." s7-design-optimize row:
"Science 7's design work falls late in its unit 2 (days 24 to 42), close to unit 2's end (day 33). Science gives one
worked example comparing ratios in a table with grade 6 tools; no student is asked whether a relationship is
proportional." Percent row: "Available: science 7 unit 6 is days 129 to 158." Time-zone row: "Available: social studies
7 is about days 78 to 86." LAYER process. REPEAT yes (lesson 15; the kindergarten read found the same).

### 5. The 7.7.17 cut gives the wrong reason (minor; firm)

**What is wrong.** 7.7.17 "Building Prisms" is cut as "Application; extension candidate". IM marks it optional on its
page; the reason should say so. (7.1.6 and 7.5.10 are optional on their pages too, and are rightly kept; the frame does
not need to change for them.)
**Why it matters.** A cut of a non-optional lesson needs a stronger reason than this; a reader cannot tell which it is.
**Fix (frame, source map).** "IM optional (prep page); extension candidate." LAYER base text. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met on the guide's rule (about 71 percent of days, 70 percent of kept lessons, 6 of 8 units with connections); strictly 61 percent by owning rows, in the borderline band, so the connections must be shown on the page (finding 2) |
| A supporting cluster that does not practise major work | Met in substance (scale, circles and probability all use proportional reasoning); not yet said in units 3, 7 and 8 (finding 2) |
| A source-map row with no keep, split, merge, cut or ours decision | Met; one cut reason to correct (finding 5) |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None found. Grade 6's hand-ons are picked up; grade 8's "Picked up" table matches |
| A model used before the grade that builds it | None. Hangers and tape diagrams for equations come after unit 5's signed numbers |
| A limit broken | None. Equations stay px + q = r and p(x + q) = r; no variables on both sides (grade 8) |

## The brief's other checks

- **Owned skills:** all grade 7 rows placed once; all 43 codes owned. ~7.RP.A.2a is a begun-elsewhere touch, named.
- **Standards in full:** 7.NS.A.2d's "why" and its signed decimals have no day (finding 1); the rest are named in
  full, including 7.G.A.2's "with technology" path (For the lead item 4).
- **Units and reasons:** IM order kept; the chart's edges (7.2 to 7.3 and 7.4, 7.4 to 7.8, 7.5 to 7.6 to 7.7) hold.
- **Days:** 12 + 21 + 11 + 22 + 23 + 28 + 18 + 19 = 154, plus 6 = 160; IM days per unit are within the pacing guide's
  ranges. No unit far over or under its load.
- **Source map:** 145 lessons accounted for; optional cuts match IM (7.1.8, 7.1.13, 7.3.5, 7.3.11, 7.8.17, 7.8.20, all
  of 7.9); 7.4.15 is optional and kept with a reason. No NC or reference source mapped.
- **Seams:** grade 6 hand-ons picked up row for row; grade 8 picks up every hand-on.
- **Cross-subject:** finding 4. Every lean carries an "if later" line.
- **Lessons from the social studies frames:** 1 finding 3; 2 met; 3 met (50 minutes, IM's 45 plus 5); 4 finding 1; 5
  finding 1; 6 met; 7 met (the row note is finding 1); 8 met; 9 finding 3; 10 met; 11 met; 12 met; 13 met; 14 met;
  15 finding 4.

## What is right and should not be touched

- IM's lengths for the geometry and probability units: they carry proportional reasoning and are worth their days.
- The equations unit's balance between hangers, tape diagrams and the algebraic step, and the "compare the two
  methods" aim of 7.EE.B.4a.
- The time-zone bridge that counts hours on a clock line without signed sums.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| m7-decimal-expansion stays owned in unit 5; unit 4 says it begins it (IM 7.4.5); one unit 5 Curio Class day finishes it | Matches IM without moving a standard between units | docs/courses/math-grade-7/frame.md, units 4 and 5, source map |
| Focus: option (a), keep IM's lengths and count connected supporting work, with the connections named in units 1, 3, 7 and 8 | EdReports indicator 1e counts connected work; option (b) would cut real proportional reasoning days to move a number | frame.md, course in brief, For the lead item 2 |
| Curio Class days per unit as in finding 3 | A respond day after each check | frame.md, source map |
| MS-PS1-4 is a grade 6 science context | s6-state-change owns it | frame.md, Cross-subject |

## For Cory

None. Nothing here changes scope, money, people or audience.

## What I could not judge

Where exactly in science 7's unit 2 the proportional-comparison lesson falls; its frame gives the unit, not the day.

## Sources

- IM K-12 Math 1st edition, grade 7, local copy (S:\CurioClass-sources\illustrative-math\grade-7, CC BY 4.0): lesson
  lists, optional marks, Addressing tags, lesson 7.4.5, the 6 to 8 pacing guide and dependency chart.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf (three counts, connected supporting
  work counts, 60 to 64 percent borderline). Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv; CCSS text via
  data/standards/ccss-math-standards.txt.
- Confidence: findings 1, 3, 4 and 5 firm; finding 2's arithmetic firm, the choice of option (a) a judgment call.

## For the source list

None new.
