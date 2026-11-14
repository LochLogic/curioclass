# Expert read: course frame, Science Grade 3 (2026-11-14)

Cold read by the curriculum expert (docs/pipeline/briefs/frame-read.md). I did not write this frame. I did not open
docs/courses/science-4-spine.md, the progression reconcile reviews or anything under S:\CurioClass-sources\_calibration.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/science-grade-3/frame.md (whole) and its row in data/plans/frames.csv (6 units, 120 days).
- data/progressions/science.csv: all 15 grade 3 rows, and the K to 2 and grade 4 to 8 rows they assume or hand on to.
- Neighbouring frames: docs/courses/science-grade-2/frame.md (before), docs/courses/science-grade-4/frame.md (after).
- Cross-subject: docs/courses/math-grade-3/frame.md, docs/courses/english-language-arts-grade-3/frame.md,
  docs/courses/social-studies-grade-3/frame.md, data/progressions/math.csv (negative numbers, percent, measurement).
- docs/pipeline/briefs/frame-write.md ("Lessons from the social studies frames"), DESK-ANSWERS entries of
  2026-11-12 and 2026-11-13 for science, the "For the course frames" sections of the two cross progression reviews,
  and the science progression reviews (expert and Codex) for what they left the frames.
- Gates: `python -X utf8 scripts/frame.py check science-grade-3` (0 failures; 6 units, 120 days, 111 in units, 9
  at course level); `python -X utf8 scripts/plan.py check` (science frames 0 failures; the one failure is
  math-grade-6, another subject, ignored as told); `python -X utf8 scripts/stale.py check` (0 failures). A script of
  my own confirmed every assumes and hands_on of the grade 3 rows, and every earlier row handing into grade 3,
  appears in the Seams tables, and every model in the rows appears under "Models carried".
- **Standards in full:** data/standards/ngss-pes.txt holds codes only. I judged each performance expectation, its
  clarification statement and its assessment boundary from my own knowledge of the NGSS text (not re-fetched this
  run); every finding below that rests on that wording says so.

## Verdict

The frame is sound and close to ready: all 16 expectations are placed, the days add up and fit a stated 45-minute,
four-a-week year, the seams match both neighbours, and the anchors are real phenomena with a storyline reason for
each unit's place. The biggest risk is unit 3, whose anchor repeats grade 2's plant-in-the-dark anchor (a puzzle
students already solved) and whose plants have no planting day, so a writer cannot make the life cycle observable
in time. Fix that anchor and planting day, the false "no frog could live there" in unit 4, and the negative
temperatures in unit 6 before the scope and sequence.

## Findings, most serious first

### 1. Unit 4's anchor says no frog could live in the Arctic tundra; that is false, and ELA has just taught frogs

- **What is wrong.** The anchor reads "no frog or cactus could live there" and the habitat lesson uses "a polar bear
  and a frog in the Arctic". Wood frogs range north to the Arctic tree line and beyond the Arctic Circle in Alaska
  and Canada, and survive winter frozen. Students arrive at unit 4 (school days about 79 to 104) straight from ELA
  grade 3 unit 2, "Frogs and the places they live" (about days 40 to 77), where cold-adapted frogs are a likely text.
- **Why it matters.** Accuracy is a door (RUBRIC-SCIENCE S10, Gateway 2d): "a simplification that is false, not
  just simple". A student who read about freezing frogs is told the opposite on day one.
- **Fix.** Anchor: "no rainforest tree frog or cactus could live there". In the habitat lesson, use the wood frog
  as the "survives, but only by a special trait" case beside the polar bear (survives well) and the tree frog (cannot
  survive), which is exactly the three-way pattern 3-LS4-3 asks for, and say the case links to ELA's frog unit.
- **Evidence and confidence.** Wood frog range and freeze tolerance from memory (USGS and state wildlife pages
  describe both); ELA timing from its frame. Likely.
- **LAYER** frame. **REPEAT** new.

### 2. Unit 3's anchor repeats grade 2's anchor, and its plant test reruns grade 2's test

- **What is wrong.** Grade 2 unit 5's anchor is a plant kept in the dark that turned pale and floppy, and its fair
  test (s2-plant-needs-test) varies water and light. Grade 3 unit 3's anchor includes "the pots on the dark shelf
  grow tall, thin and pale", and its class plant test changes "only light or water". The environment half of the
  unit opens on a puzzle the class explained a year ago and repeats the same investigation.
- **Why it matters.** Lesson 11 of frame-write.md (picks do not repeat another grade's picks) and the lens: an
  anchor must be something students cannot yet explain. s3-environment-traits asks for a new idea (a trait shaped
  by the environment), which the old test does not make visible.
- **Fix.** Anchor keeps the seedlings from one packet that look like the parent but not like each other (the
  inheritance puzzle), and adds a trait the environment changes that grade 2 did not show: the same hydrangea
  bush with blue flowers in one garden and pink in another (soil decides the color). The class test changes
  crowding (seeds sown close together against spread out; crowded plants stay smaller), not light or water. The
  standard's own examples (stunted plants, the overfed dog) and the flamingos stay as cases. Grade 2's light test is
  retrieved in one opening task, as the seam table already says.
- **Evidence and confidence.** Grade 2 frame, unit 5 row; s2-plant-needs-test and s3-environment-traits notes.
  Firm.
- **LAYER** frame. **REPEAT** yes (lesson 11).

### 3. The living things of unit 3 have no planting day, so the life cycle cannot be watched in time

- **What is wrong.** Unit 3 (science days 37 to 58, about 5.5 weeks) needs plants already up on its first day (the
  anchor) and a full plant life cycle watched first-hand (birth, growth, reproduction and death). The frame says only
  "planted early in the year so they finish in time"; the brief's "The weather log" bullet says the plant
  investigations "run across weeks while other lessons go on", with no start. Fast-cycling plants need about five to
  six weeks seed to seed under constant light, bush beans longer; a mealworm's larva-pupa-beetle change needs
  several weeks from late-stage larvae.
- **Why it matters.** A writer reading the frame will plant on unit 3's first day; the plants will not flower before
  the unit ends, and the life-cycle model will rest on pictures, not observation (S1, S4).
- **Fix.** Add to the brief: "Planting day: science day 18 (unit 2, first week), about 15 minutes; fast-cycling
  plants or radishes under a lamp, and late-stage mealworm larvae set up the same week. The pots are on show when
  unit 3 opens on day 37 and flower and set seed by about day 58." Name the same day in unit 2's teacher-notes cell.
- **Evidence and confidence.** Plant timings from memory (seed suppliers' growing guides for fast-cycling Brassica
  and radish). Likely.
- **LAYER** frame. **REPEAT** new.

### 4. Negative temperatures and percent slip in ahead of math

- **What is wrong.** Unit 6's named climate comparison includes Utqiagvik, Alaska, whose monthly average
  temperatures are below zero Fahrenheit for several winter months (and below zero Celsius for most of the year).
  The class log in a northern school will also read below zero in winter. Negative numbers are grade 6
  (m6-negative-numbers, 6.NS.C.5). Unit 4's "simple data on hunting success alone and in groups" is, in published
  sources, almost always given as a percent (m6-percent, 6.RP.A.3c).
- **Why it matters.** Lesson 13 of frame-write.md names both negative numbers and percent. A bar graph of
  Utqiagvik's months needs bars below the axis.
- **Fix.** Unit 6 notes: "Climates are compared in words, maps and counts (months below freezing, months with
  rain); no temperature below zero is graphed or compared. A log reading below zero is recorded in words ('below
  zero') and left off the graph." Unit 4 notes: "Hunting data are given as counts out of 10 hunts (alone: 2 of 10
  caught prey; in a group: 5 of 10), read from a bar graph; no percent." Add a "math:" line to s3-climates and
  s3-animal-groups cross_subject under "For the lead" so the fixer edits both ends.
- **Evidence and confidence.** Utqiagvik climate normals from memory (NOAA normals show winter monthly means near
  -10 to -15 F); math progression rows. Firm.
- **LAYER** frame. **REPEAT** yes (lesson 13).

### 5. "Every clarification example has a place" is claimed, but three are missing

- **What is wrong.** The Standard bullet says every clarification example has a place in its unit. Judged from the
  NGSS text (memory):
  - 3-PS2-3 names the force between an electromagnet and steel paper clips. The row and unit 2 exclude circuits, so
    the example has no place.
  - 3-LS4-4 lists changes in land, water, temperature, food and other organisms. Unit 2's cases (a highway, a dam,
    a fire) cover land, water and food; unit 5 claims "the changes cover the clarification's kinds" but no case
    carries temperature or other organisms.
  - 3-LS4-2 names advantages in surviving, finding mates and reproducing. Unit 4 lists "finds mates" but gives no
    case for it.
- **Why it matters.** Lesson 4 of frame-write.md: a standard is never narrowed to its headline, and the unit that
  teaches a part says so. NGSS examples are "could include", so the gap is not fatal, but the frame claims more than
  it does and a writer will trust the claim.
- **Fix.** Unit 2: "A teacher demonstration of an electromagnet (a nail wound with wire on one D cell) picking up
  paper clips, switched on and off; students observe and ask questions, they build no circuit (grade 4)." Unit 5:
  add "a stream warmed when the shading trees on its bank are cut (temperature)" and "a new plant that spreads and
  crowds out the food of local animals (other organisms)" as short cases. Unit 4: add "brighter-colored male birds
  of one kind attract mates more often" as the mates case.
- **Evidence and confidence.** NGSS 3-PS2-3, 3-LS4-2, 3-LS4-4 clarification statements, from memory. Likely.
- **LAYER** frame. **REPEAT** yes (lesson 4).

### 6. No paper path or student-account line

- **What is wrong.** Every unit lists a Curio Class simulation for the no-kit path, but the frame never says each
  electronic tool has a paper path and needs no student account. The grade 2 and grade 6 frames both say it.
- **Why it matters.** Lesson 14 of frame-write.md.
- **Fix.** Add to the Materials bullet: "Every simulation has a paper path (the same data on a printed sheet) and
  needs no student account."
- **LAYER** frame. **REPEAT** yes (lesson 14).

### 7. The math calendar cites the base text's unit numbers, not Curio Class's math frame

- **What is wrong.** The Cross-subject table says 3.MD.B.4 and 3.MD.A.2 come in "its sixth of eight units". The
  written math-grade-3 frame places them in its unit 7 of 8 (m3-line-plots, m3-mass-volume), after fractions.
  3.MD.B.3 in math unit 1 is right.
- **Why it matters.** The calendar is what the other subject's frame honours; it should name that frame's units now
  that it exists. The bridges already cover the late teaching, so no science day changes.
- **Fix.** Replace "the math base text teaches it in its sixth of eight units, late in the year" with "math grade 3
  unit 7 (late in the year)" in both rows.
- **LAYER** frame. **REPEAT** new.

### 8. Seam with grade 2: grade 2's frame says grade 3 runs fair tests of many solutions, and counts 34 weeks

- **What is wrong.** Grade 2's "Handed on" table says s3-design-problem does "criteria, constraints and fair tests of
  many solutions". Grade 3 (and the row) define the problem only; comparing is grade 4 and fair tests of a prototype
  grade 5. Grade 2 also assumes 34 teaching weeks where grades 3 to 5 assume 32 (the 160-day yardstick).
- **Why it matters.** One thread, one wording (lesson 6); a grade 2 writer would promise grade 3 work that is not
  there.
- **Fix.** In docs/courses/science-grade-2/frame.md, Handed on row s2-compare-designs: "Need, criteria and
  constraints, stated precisely enough that two solutions could be judged (3-5-ETS1-1)". The weeks: grade 2 restates
  its time on the band's 32 weeks, or says why it differs.
- **LAYER** frame (grade 2's file). **REPEAT** yes (lesson 6).

### 9. Unit 6's anchor counts on two weather warnings that may not happen

- **What is wrong.** "twice this year the town had a warning" is a fact about the year, not a phenomenon the class
  can be sure of.
- **Fix.** "and, this year or last, the town had a weather warning (from the National Weather Service's record for
  the county if the class has not seen one)".
- **LAYER** frame. **REPEAT** new. **Confidence** firm.

## What is right and should not be touched

- One anchor driving two or three rows per unit (the swing, the tundra, the class's own weather log), with the
  order reasoned from the rows ("inherited before environment", "weather data before climates").
- 3-5-ETS1-1 done in full in unit 2 with a named problem and the second clarification example kept as transfer.
- The weather log from week 1 read in unit 6; supplied averages (no mean before grade 6).
- Respond day after each check; checks on unseen phenomena; "Candidate:" check-set cells; sensitivity line; time a
  day stated and the day total argued from the rows.
- The non-human-only rule on traits and the no-role-play note on the camouflage hunt.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 3 environment phenomenon: hydrangea flower color by soil; class test varies crowding | New to grade 3, puzzling, explainable with 3-LS3-2, no repeat of grade 2 | docs/courses/science-grade-3/frame.md, unit 3 |
| Planting day: science day 18, fast-cycling plants or radishes under a lamp, late-stage mealworm larvae | Lets the life cycle be seen inside unit 3 | frame.md, brief and units 2 and 3 |
| Unit 4 frog: tree frog cannot survive, wood frog survives by a special trait | True, and gives the three-way pattern | frame.md, unit 4 |
| Electromagnet as a teacher demonstration only, no student circuit | Covers 3-PS2-3's example inside the row's no-circuits boundary | frame.md, unit 2 |
| 3-LS4-4 extra cases: warmed stream after bank trees are cut; a spreading plant that crowds out food | Covers temperature and other organisms, one change at a time | frame.md, unit 5 |
| 3-LS4-2 mates case: brighter-colored males attract mates | Covers the third advantage the standard names | frame.md, unit 4 |
| Hunting data as counts out of 10 | No percent before grade 6 | frame.md, unit 4 |
| No temperature below zero graphed or compared | No negative numbers before grade 6 | frame.md, unit 6 |
| Keep the C3 column holding practices and crosscutting concepts; rename the header in the brief as the frame proposes | No gate reads it; the name misleads a science writer | docs/pipeline/briefs/frame-write.md |

## For Cory

- **Time a week (audience).** Grade 2 assumes about 80 minutes of science a week; grade 3 assumes 180, while social
  studies grade 3 assumes a daily 40-minute block. The frame's "For the lead" item 1 already asks; the jump between
  grades 2 and 3 is worth weighing in the same answer.
- **Materials cost (money)** and **a science teacher's read of safety (people)**, as the frame raises them.

## Lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation of the grade has no unit, or a unit claims one it only touches | Met for placement (all 16 placed); missed in part on "in full" (finding 5) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met (every unit names one; unit 3's needs changing, finding 2) |
| Progression lines (core idea at the same depth twice, model assumed but not built, practice that grows nowhere) | Met at this layer: force arrows and claim-evidence-reasoning are built before use; the fair test grows from grade 2 |
| Rubric rows read at frame level: S11 placement, S12 math in step, S13 engineering as design, 2f how science works | S11 met; S12 missed in part (finding 4); S13 met (unit 2, judged again in 5 and 6); 2f met (units 1 and 5) |

## What I could not judge

The exact NGSS wording, from memory only; the element-level practices and crosscutting concepts (the frame's "For
the lead" item 4 is right that the scope and sequence must check them against the standard's own text).

## Sources

- NGSS performance expectations 3-PS2-1 to 3-PS2-4, 3-LS1-1, 3-LS2-1, 3-LS3-1, 3-LS3-2, 3-LS4-1 to 3-LS4-4,
  3-ESS2-1, 3-ESS2-2, 3-ESS3-1, 3-5-ETS1-1, https://www.nextgenscience.org/ (from memory, not re-fetched).
- NOAA climate normals for Utqiagvik (from memory): winter monthly means below zero Fahrenheit.
- Repository files listed under "What I read".

## For the source list

Nothing new read this run.
