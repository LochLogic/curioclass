# Expert read: course frame, Science Grade 5 (2026-11-14)

Cold read by the curriculum expert (docs/pipeline/briefs/frame-read.md). I did not write this frame. I did not open
docs/courses/science-4-spine.md, the progression reconcile reviews or anything under S:\CurioClass-sources\_calibration.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/science-grade-5/frame.md (whole) and its row in data/plans/frames.csv (6 units, 120 days).
- data/progressions/science.csv: all 14 grade 5 rows, and the K to 4 and grade 6 to 8 rows they assume or hand on to.
- Neighbouring frames: docs/courses/science-grade-4/frame.md (before) and docs/courses/science-grade-6/frame.md
  (after; it exists, so I read its brief and its "Picked up" table rather than the grade 6 rows alone).
- Cross-subject: docs/courses/math-grade-5/frame.md, data/progressions/math.csv, data/progressions/ela.csv (grade 5
  rows; no ELA grade 5 frame is written yet), docs/courses/social-studies-grade-5/frame.md, DESK-ANSWERS 2026-11-13
  (card q-cross-progression-1: ELA grade 5 unit 4 becomes water).
- docs/pipeline/briefs/frame-write.md ("Lessons from the social studies frames"), the cross progression reviews'
  "For the course frames" sections and the science progression reviews (the Codex read settled "out of 100" for
  the water shares and supplied averages).
- Gates: `python -X utf8 scripts/frame.py check science-grade-5` (0 failures; 6 units, 120 days, 111 in units, 9
  at course level); `python -X utf8 scripts/plan.py check` (science frames 0 failures; math-grade-6's failure is
  another subject, ignored); `python -X utf8 scripts/stale.py check` (0 failures). My own script confirmed every
  assumes and hands_on of the grade 5 rows, and every earlier row handing into grade 5, appears in the Seams tables,
  and every row model appears under "Models carried". Each grade 5 hand-on matches a "Picked up" line in grade 6
  or a grade 7 or 8 row.
- **Standards in full:** data/standards/ngss-pes.txt holds codes only; I judged the 14 expectations, clarification
  statements and boundaries from my own knowledge of the NGSS text (not re-fetched).

## Verdict

The frame is sound: all 14 expectations are placed, the particle model is a real spine for the year, 3-5-ETS1-3 is
done as a full design cycle on a problem the previous unit supplies, and the seams with grade 4 and grade 6 match
line for line. The biggest risk is unit 2's own soil-weighing investigation, which as written will give data that
show nothing (the weight of wet soil swings with its water), so the argument the unit exists for would rest on the
1600s story alone. Fix that, add the fresh-water-only shares 5-ESS2-2 asks for, and give star distances a form
grade 5 math can read.

## Findings, most serious first

### 1. The class's weighed soil will show water, not soil

- **What is wrong.** "The class's weighed pots of soil and plants (set up in unit 2's first week, weighed again at
  its end)". Over unit 2's six weeks a pot's soil gains and loses tens of grams with each watering, while a seedling
  adds a few grams. The before and after weights will move with the last watering, not with where the plant's matter
  came from. Six weeks is also short for a plant to add enough to weigh.
- **Why it matters.** The lens: "data with no pattern to find" and a model that does not change after the
  investigation. 5-LS1-1 is an argument from evidence; this is the class's only first-hand evidence for it.
- **Fix.** Long investigations bullet: "Pots set up in the first week of the year (like the shadow record): soil
  dried on trays for two days, weighed dry into each pot, fast-growing beans planted. At the end of unit 2 (about
  science day 41) the plant is lifted out and weighed, and the soil is dried and weighed again: the plant has gained
  many grams, the dry soil has lost about none." Name the set-up day in unit 1's teacher notes.
- **Evidence and confidence.** Soil water content and seedling growth from memory (the classic classroom version of
  the willow experiment dries the soil). Likely.
- **LAYER** frame. **REPEAT** new.

### 2. 5-ESS2-2 asks for the shares of fresh water too; the frame graphs only the whole

- **What is wrong.** The expectation is to describe and graph the amounts and percentages of water and of fresh
  water in the reservoirs (oceans, lakes, rivers, glaciers, ground water, polar ice caps). Unit 5 gives "about 97 of
  every 100 parts in the ocean" and says in words that most fresh water is ice or underground. Read against all of
  Earth's water, lakes and rivers are a tiny decimal no grade 5 student can graph, so a writer will either graph
  decimals or leave the fresh-water graph out.
- **Why it matters.** Lesson 4 of frame-write.md (standards in full, the unit says how); lesson 13 (no decimals
  past hundredths as data before grade 5 math reaches them, and no percent procedures).
- **Fix.** Unit 5: "Two hundred-square grids and two bar graphs: all of Earth's water (about 97 ocean, 3 fresh), then
  the fresh water alone as its own 100 parts (about 69 ice caps and glaciers, 30 ground water, 1 lakes, rivers and
  swamps). Each reservoir the boundary names has a place on one of the two graphs."
- **Evidence and confidence.** NGSS 5-ESS2-2 wording and boundary from memory; USGS water distribution figures from
  memory. Firm.
- **LAYER** frame. **REPEAT** yes (lesson 4).

### 3. Star distances cannot be read with the math grade 5 has by unit 4

- **What is wrong.** Unit 4 uses "star distance data written in powers of ten", with the bridge "a given table
  written both ways (10 with three zeros, 1,000)". Real star distances are tens of trillions of kilometres; grade 4
  place value stops at 1,000,000, and the math-grade-5 frame teaches powers of ten (m5-powers-of-ten, 5.NBT.A.2) in
  its unit 8, about school days 110 to 118, after science unit 4 (school 83 to 108). The bridge's own example uses
  the exponent idea it is meant to avoid.
- **Why it matters.** Lesson 13; and the argument for 5-ESS1-1 needs a distance comparison students can actually
  read.
- **Fix.** "Distances given as the time light takes to arrive: about 8 minutes from the sun, more than 4 years from
  the nearest other star, many more years from the bright stars of the night sky; and a scale model (if the sun
  were a grain of sand on the classroom table, the nearest star would be a grain of sand in a town far away). No
  number over 1,000,000; powers of ten only after math teaches them." Change s5-star-brightness cross_subject under
  "For the lead".
- **Evidence and confidence.** Distances from memory; math-grade-5 frame. Firm.
- **LAYER** frame. **REPEAT** yes (lesson 13).

### 4. The math calendar cites the base text's units, not Curio Class's math frame

- **What is wrong.** The Cross-subject table places 5.MD.A.1 in the base text's sixth unit, 5.NBT.A.2 in its first
  and sixth, 5.G.A.2 in its seventh and 5.MD.B.2 in its sixth. The written math-grade-5 frame has
  m5-measurement-conversion and m5-powers-of-ten in unit 8 (about days 110 to 118), m5-line-plots in unit 9 (about
  119 to 134) and m5-graph-points in unit 10 (about 135 to 149).
- **Why it matters.** The calendar is what the math frame honours. Every bridge still holds, so no science day moves;
  the line-plot row's "Not likely needed" stays true only just (unit 6 starts near school day 133).
- **Fix.** Name math grade 5 units 8, 8, 10 and 9 in the four rows, and change the line-plot "if later" to "If math
  unit 9 has not reached line plots by science day 100, the plot is marked in whole and half units."
- **LAYER** frame. **REPEAT** new.

### 5. No paper path or student-account line

- **What is wrong.** Every unit lists a simulation; the frame never says each electronic tool has a paper path and
  needs no student account (grades 2 and 6 say it).
- **Fix.** Add to the Materials bullet: "Every simulation has a paper path (the same data on a printed sheet) and
  needs no student account."
- **LAYER** frame. **REPEAT** yes (lesson 14).

### 6. The balloon on the fizzing bottle will seem to lose weight

- **What is wrong.** Unit 1 weighs baking soda and vinegar in a bottle with a balloon on top. As the balloon fills,
  the air it pushes aside holds it up a little, so a scale that reads to the gram can show a loss of a gram or two
  that is not a loss. The frame's boundary rightly keeps buoyancy out of grade 5.
- **Why it matters.** The data would contradict the conclusion they are meant to support, and the frame gives the
  teacher nothing to say.
- **Fix.** "Small amounts (a quarter teaspoon of baking soda, a tablespoon of vinegar) so the balloon barely fills;
  the scale reads the same to the gram. The open-bottle version, which does lose weight, is the comparison."
- **Evidence and confidence.** Buoyancy of an inflated balloon, from memory (about 1.2 grams per litre of air). Likely.
- **LAYER** frame. **REPEAT** new.

### 7. The noon shadow jumps an hour when clocks change

- **What is wrong.** "A noon-shadow record, one measurement a month from the first month". From early November
  clock noon is an hour later in sun time than in September, so the monthly series mixes two times of day and the
  shadow's direction swings for a reason that is not the season.
- **Fix.** "Measured at the same sun time each month: 1 pm while clocks are on daylight saving time, 12 noon after
  they change back (or at the time the National Weather Service gives as solar noon for the town)."
- **LAYER** frame. **REPEAT** new. **Confidence** firm.

## What is right and should not be touched

- The particle model built from the four examples the standard names (the ball, the syringe, dissolved sugar, dried
  salt water) and carried into units 2, 3 and 5.
- 3-5-ETS1-3 done as the full cycle on unit 5's water problem, with repeated trials and failure points, and grade
  4's start named honestly.
- The willow-in-a-pot history as how science works; the decomposers and "energy flows, matter cycles" in unit 2.
- Water units placed beside ELA grade 5's water unit, as Cory chose (2026-11-13), with an "if earlier" line for ELA.
- Supplied "out of 100" language for the water shares (the Codex progression read's settled item), the no-tasting
  rule, filtered water never drunk, the state test question sent to Cory rather than decided.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Dry-soil weighing, pots set up in week 1 | Gives a measurable pattern before unit 2's argument | docs/courses/science-grade-5/frame.md, brief and units 1 and 2 |
| Fresh water shares: about 69 ice, 30 ground water, 1 lakes, rivers and swamps, on its own grid | Covers "and fresh water" with whole numbers out of 100 | frame.md, unit 5 |
| Star distance as light travel time plus a grain-of-sand scale model | Readable with grade 4 numbers; powers of ten after math unit 8 | frame.md, unit 4 |
| Quarter teaspoon of baking soda in the balloon test | Keeps the buoyancy error under the scale's gram | frame.md, unit 1 |
| Monthly shadow at the same sun time | Removes the clock-change jump | frame.md, brief and unit 4 |
| Add a cooling case to 5-PS1-2 (water frozen in a sealed bag, weighed before and after) | The standard names heating, cooling and mixing; the frame shows no cooling | frame.md, unit 1 |
| Anchor wording: the soil "lost less than a pound" (not "a few ounces") | Keeps the frame's own one-unit rule for the historical data | frame.md, unit 2 |

## For Cory

- **Grade 5 state science tests (audience)** and **time a week (audience)**, as the frame raises them; I agree with
  keeping the order.
- **Materials cost (money)** and **a science teacher's read of safety (people)**: unit 1's fizzing and unit 3's
  mixing are the first items a qualified reader should see.

## Lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation of the grade has no unit, or a unit claims one it only touches | Met for placement; missed in part on 5-ESS2-2 (finding 2) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met |
| Progression lines (model assumed but not built; practice that grows nowhere) | Met: particle model before its uses; food web before the energy row; the design cycle completes the band |
| Rubric rows read at frame level: S11 placement, S12 math, S13 engineering, 2f how science works | S11 met; S12 missed in part (finding 3); S13 met (unit 6); 2f met (units 2 and 6) |

## What I could not judge

The exact NGSS wording, from memory only; element-level practices and crosscutting concepts (sent to the scope and
sequence by the frame's "For the lead" item 6, rightly). ELA grade 5's unit timing, since its frame is not written;
the frame's "if earlier" line covers either order.

## Sources

- NGSS 5-PS1-1 to 5-PS1-4, 5-PS2-1, 5-PS3-1, 5-LS1-1, 5-LS2-1, 5-ESS1-1, 5-ESS1-2, 5-ESS2-1, 5-ESS2-2, 5-ESS3-1,
  3-5-ETS1-3, https://www.nextgenscience.org/ (from memory, not re-fetched).
- USGS, Where is Earth's water, https://www.usgs.gov/special-topics/water-science-school (shares from memory).
- Repository files listed under "What I read".

## For the source list

Nothing new read this run.
