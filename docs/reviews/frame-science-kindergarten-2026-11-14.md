# Frame read: science-kindergarten (Science, Kindergarten), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (to "How this differs").
- The frame docs/courses/science-kindergarten/frame.md and its row in data/plans/frames.csv (6 units, 64 days).
- The 11 kindergarten rows of data/progressions/science.csv, and the grade 1 and grade 2 rows that assume them.
- The frame after: docs/courses/science-grade-1/frame.md (kindergarten has no course before).
- Same-year frames this course leans on or is leaned on by: docs/courses/math-kindergarten/frame.md (cross-subject
  tables), docs/courses/social-studies-grade-1/frame.md and docs/courses/social-studies-grade-2/frame.md (their leans
  on K-ESS2-1, K-ESS3-1, K-ESS3-3). No ELA kindergarten frame exists yet.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames" (all 15 checked below).
- DESK-ANSWERS 2026-11-12 and 2026-11-13 (science base texts, equipment paths, simulations).
- Earlier reads: docs/reviews/progression-science-2026-11-13.md (finding 9: in-grade order of design-cycle users),
  docs/reviews/frame-k-2-fixes-2026-11-13.md (the kinds of finding the social studies K to 2 frames drew).
- Gates: `frame.py check science-kindergarten` 0 failures (6 units, 64 days, 58 in units, 6 at course level);
  `plan.py check` passes for this frame (its failures are other subjects' frames, ignored as asked);
  `stale.py check` 0 failures. Handoffs at both ends checked by my own script: every K hands_on is answered by the
  receiving row's assumes.
- Standards: data/standards/ngss-pes.txt holds codes only. The performance expectations, clarification statements,
  assessment boundaries and their crosscutting concepts are judged **from my knowledge of NGSS (2013), not
  re-fetched**; each finding that rests on that says so.

## Verdict

The frame is sound: all 11 rows sit once, the order never uses a model before it is introduced (design-cycle in unit 3
before units 5 and 6; claim-evidence-reasoning in unit 4 before 5 and 6), every clarification example is named in its
unit, and the 64 days at two 30-minute lessons a week are honest for what kindergarten owns. The biggest risk is a
calendar fault: the weather chart starts in unit 2 (about week 5) but the unit is told to compare two months of data
at its end (about week 10), which a writer cannot build. The one change that matters most is starting the chart as a
week 1 routine; next, K-ESS3-1's "including humans" must be taught, since two social studies frames lean on it.

## Findings, most serious first

### 1. The two-month weather comparison falls before two months of data exist (moderate; firm)

**What is wrong.** Unit 2 runs about weeks 5 to 10 (unit 1 is 9 days at two a week). The frame says "The class weather
chart begins" in unit 2 and "The two-month comparison falls at the unit's end." At week 10 the chart holds about five
weeks of data, one month at most. The quantitative half of K-ESS2-1's clarification (counts of sunny, windy and rainy
days in a month, compared across months) cannot be done where the frame puts it.
**Why it matters.** A unit writer builds a closing day on data the class does not have, or quietly drops the
quantitative part, which narrows the standard (lesson 4).
**Fix (frame, course brief "Days" bullet and unit 2).** Start the chart in week 1 as the two-minute daily routine,
teacher-led with picture squares (the observing habits of unit 1 grow beside it; the row's "uses the habits begun in
sk-push-pull" still holds because unit 2 is where the chart is read and taught). Unit 2 then opens on about a month of
data and closes with September against October. Add to unit 2's reason: "The chart starts in week 1 so the unit has
two months to compare." LAYER frame. REPEAT new.

### 2. K-ESS3-1 is taught without its humans (moderate; firm from memory of the standard, firm from the repo)

**What is wrong.** K-ESS3-1 reads "the needs of different plants and animals (including humans) and the places they
live". Unit 4's model names deer, grass and fish only, and the row sk-needs-places does too. Social studies grade 1
(ss1-landforms-waters, "people live where their needs are met") and grade 2 (ss2-resources-industries, "people use what
the land provides") both review K-ESS3-1 for its human part.
**Why it matters.** The standard is taught to its animal and plant half only, and two later social studies units open
on a review of something kindergarten science never taught.
**Fix (frame unit 4 "What students learn"; progression row note through "For the lead").** Add after the fish:
"People too: our town is where it is because people need water, food and shelter (the class's own town and its water
source, a river, lake or wells, drawn on the class picture map)." Add to "For the lead": change sk-needs-places notes
to name people in the model the same way. No day change. LAYER frame and progression. REPEAT yes (a standard taught in
part, as in the social studies frame reads).

### 3. Season claims do not match the day count (minor; likely)

**What is wrong.** By the frame's own counts (unit days plus the mid-year check and respond day, two lessons a week),
unit 4 runs about weeks 16 to 22 and unit 5 about weeks 22 to 27 of 32: December to January and February to March.
Unit 4's anchor is a schoolyard walk to a weed growing out of a sidewalk crack and a squirrel's fresh hole; unit 5
says "Spring, when sun on the schoolyard is strong enough" and asks why the slide is "too hot to touch". In much of
the country the weed is dead or under snow in January and no slide is hot in February.
**Why it matters.** The anchors are the unit's driver (S1); a writer builds a first day on a walk that shows nothing.
**Fix (frame units 4 and 5).** Unit 4: photograph the weed and a squirrel's cache during unit 1 or 2's outdoor time
and open unit 4 on those photographs plus the class plants; the walk is used where the ground is clear. Unit 5: change
the question to "Why is the slide in the sun warmer than the one under the tree?" and the anchor to a sunny-day touch
test (relative warmer and cooler is the boundary anyway, and a dark surface in winter sun is still warmer than its
shaded twin); delete "Spring". "For the lead" item 3 then covers only warm-climate swaps. LAYER frame. REPEAT new.

### 4. Stale note: the math frame is written (minor; firm)

**What is wrong.** Cross-subject says "The other subjects' frames are written later and set their own unit numbers."
docs/courses/math-kindergarten/frame.md exists and places K.MD.B.3 in its unit 2 (about week 8) and K.MD.A.2 in its
unit 3 (about weeks 12 and 13), and its own table answers this frame's leans.
**Why it matters.** The availability calendar is half settled; the note tells a reader nothing is.
**Fix (frame, Cross-subject lead-in and the Mathematics table).** Replace the sentence with: "Mathematics kindergarten
teaches K.MD.B.3 in its unit 2 (about week 8) and K.MD.A.2 in its unit 3 (about weeks 12 and 13); the ELA kindergarten
frame sets its own unit numbers." Add a column or note to the Mathematics table: units 1 (week 2) and 2 (week 6) come
before math teaches these and run on the bridge given; units 3, 4 and 5 come after or alongside. LAYER process.
REPEAT yes (stale notes in every social studies frame read).

## Checked and found right (do not undo)

- **Owned skills.** All 11 rows placed once; design-cycle and claim reuse in units 5 and 6 named as review, never in
  the Skills column. sk-define-problem sits in unit 3 before sk-ramp-design inside the same unit, which settles
  progression finding 9 for kindergarten.
- **Standards in full (from memory of NGSS).** K-PS2-1 all four clarification pushes, strength or direction never
  both, no magnets; K-PS2-2 distance, path, corner, knock-down, no friction; K-PS3-1 sand, soil, rocks, water,
  relative only; K-PS3-2 with umbrellas, canopies, tents; K-LS1-1 all four patterns; K-ESS2-1 qualitative and
  quantitative (finding 1 is timing, not content); K-ESS2-2 both examples, as argument; K-ESS3-2 local severe weather,
  prepare and respond; K-ESS3-3 both impact and both solution examples; K-2-ETS1-1 ask, observe, gather, define. Each
  unit's crosscutting concept matches its expectations' own (cause and effect for the PS and ESS3-2/3, patterns for
  LS1-1 and ESS2-1, systems for ESS2-2 and ESS3-1).
- **Days.** 58 in units for 11 rows, about 5 lessons a row, heavier for the design units and unit 4's three rows;
  60 minutes a week is below typical K to 3 science time but fits what the rows ask, and the lead is asked.
- **Seams.** Every hand-on in the table is answered by the grade 1 frame's "Picked up" table and the rows; the K to
  grade 2 skips (plant needs, habitats, Earth events) are named with the grade 1 row that keeps them in use.
- **Lessons 1 to 15.** Respond day after each check (1); "Candidate:" cells (2); time stated (3); picks named
  (thunderstorm worked case with regional swap, the litter tally) (11); sensitivity line with the disaster reader
  (12); whole numbers and direct comparison only (13); paper path, no account (14); no status lines beyond finding 4
  (15). Lesson 4 is missed once (finding 2), lesson 5 once (finding 1).

## Seams

No course before. Handed on to grade 1: the 13 lines match the grade 1 frame row for row, and the grade 3 frame picks
up sk-push-pull, sk-weather-watch, sk-forecast-severe and sk-reduce-impact with retrieval tasks.

## Cross-subject

Math K: K.MD.A.2 is needed in weeks 2 and 11, before math's unit 3 (weeks 12 and 13); the bridges (tape marks,
side-by-side) need no number and hold. K.MD.B.3 needed about week 6, math week 8; the bridge (rows compared by length,
teacher counts) holds. ELA K: no frame yet, so "taught first" cannot be checked; each lean has an if-later line.
Social studies grades 1 and 2 lean back on K-ESS3-1's human part: finding 2.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation for the grade has no unit, or a unit claims one it only touches | Met for placement; K-ESS3-1 touched in part (finding 2) |
| Grades 6 to 8: departure from OpenSciEd order, or a topic lost | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met (two anchors need a season fix, finding 3) |

## What I could not judge

- The ELA kindergarten frame (not written), so SL.K.3, SL.K.5, W.K.1 and W.K.2 timing.
- Whether $40 a class covers the kit (finding no fault; Cory's money call).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Weather chart starts week 1 as a teacher-led two-minute routine; unit 2 compares September and October | Two months of data by the unit's end | docs/courses/science-kindergarten/frame.md |
| K-ESS3-1's human case is the class's own town and its water source on the picture map | Local, first hand, and what social studies grades 1 and 2 review | frame unit 4; sk-needs-places notes (through For the lead) |
| Unit 4 opens on fall photographs of the weed and the squirrel's cache; the walk only where ground is clear | Anchor visible in January | frame unit 4 |
| Unit 5 anchor: sun and shade slides compared warmer or cooler on a sunny day, "too hot to touch" and "Spring" dropped | Works in February and stays inside the relative-only boundary | frame unit 5 |

## For Cory

- Materials ceiling of about $40 a class for the year (the frame's own item 4): money.
- K to 2 science time against grade 3: kindergarten 60, grade 1 about 65, grade 2 about 80 minutes a week, then grade 3
  180 (docs/courses/science-grade-3/frame.md). One decision on elementary science time would keep the step from grade 2
  to grade 3 deliberate.
- The disaster-aware reader for unit 2 and the science teacher's safety read: people.

## Sources

From memory, not re-fetched this run: NGSS (2013) kindergarten and K-2 ETS performance expectations, clarification
statements, assessment boundaries and foundation boxes (crosscutting concepts). The repo files above for everything
else.
