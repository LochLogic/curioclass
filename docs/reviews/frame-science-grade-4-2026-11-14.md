# Expert read: course frame, Science Grade 4 (2026-11-14)

Cold read by the curriculum expert (docs/pipeline/briefs/frame-read.md). I did not write this frame. I did not open
docs/courses/science-4-spine.md, the progression reconcile reviews or anything under S:\CurioClass-sources\_calibration.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/science-grade-4/frame.md (whole) and its row in data/plans/frames.csv (6 units, 120 days).
- data/progressions/science.csv: all 14 grade 4 rows, and the K to 3 and grade 5 to 8 rows they assume or hand on to.
- Neighbouring frames: docs/courses/science-grade-3/frame.md and docs/courses/science-grade-5/frame.md (read whole
  for the same-day reads of those courses), and docs/courses/science-grade-6/frame.md for the threads that skip
  grade 5.
- Cross-subject: docs/courses/math-grade-4/frame.md, docs/courses/english-language-arts-grade-4/frame.md,
  docs/courses/social-studies-grade-4/frame.md, data/progressions/math.csv.
- docs/pipeline/briefs/frame-write.md ("Lessons from the social studies frames"), DESK-ANSWERS 2026-11-12 and
  2026-11-13 for science, the cross progression reviews' "For the course frames" sections and the science
  progression reviews.
- Gates: `python -X utf8 scripts/frame.py check science-grade-4` (0 failures; 6 units, 120 days, 111 in units, 9
  at course level); `python -X utf8 scripts/plan.py check` (science frames 0 failures; math-grade-6's failure is
  another subject, ignored); `python -X utf8 scripts/stale.py check` (0 failures). My own script confirmed every
  assumes and hands_on of the grade 4 rows, and every earlier row handing into grade 4, appears in the Seams tables,
  and every row model appears under "Models carried".
- **Standards in full:** data/standards/ngss-pes.txt holds codes only; I judged the 15 expectations, clarification
  statements and boundaries from my own knowledge of the NGSS text (not re-fetched).

## Verdict

The frame is sound: all 15 expectations are placed and taught in full as far as the NGSS examples go, one energy
story runs through units 1 to 3, the design work grows from grade 3's problem statement to compared solutions, and
the order is argued against both the rows and social studies' hazards unit. The biggest risk is an accuracy slip
in unit 3, where sound is shown as a wave on a rope (a sideways wave; sound is a push-and-squeeze wave). The other
fixes are math ahead of math (percent in the state energy data), a wrong math calendar cell and a stale note about
ELA; none moves a unit.

## Findings, most serious first

### 1. Sound is modeled as a rope wave

- **What is wrong.** Unit 3: "sound as a wave in the rope, built on grade 1's vibrations". A wave on a rope moves the
  rope side to side across the direction the wave travels; sound in air is a compression wave, the air pushed
  together and spread apart along the direction of travel.
- **Why it matters.** Accuracy is a door (S10, Gateway 2d): this is a simplification that is false, and it is the
  misconception middle school must undo (s8-wave-amplitude-energy). 4-PS4-1 does not need sound at all; if sound is
  used, it must be right.
- **Fix.** "Sound shown with the slinky pushed and pulled along its length (bunched and spread coils travel along
  it), beside the rope or water wave as a second kind; both carry energy without carrying the material away. No
  names for the two kinds of wave." Keep amplitude and wavelength on the rope and water models.
- **Evidence and confidence.** Physics of mechanical waves; NGSS PS4.A in grades 4 and middle school (memory).
  Firm.
- **LAYER** frame. **REPEAT** new.

### 2. Percent and millilitres ahead of math

- **What is wrong.** Unit 2's local case is the state's energy data from the US Energy Information Administration,
  whose state profiles give each source as a percent of the state's electricity (and in units like billion
  kilowatt-hours). Percent is grade 6 (m6-percent, 6.RP.A.3c). Unit 4's bridge measures water "in millilitres";
  millilitres first appear in m4-unit-conversion (4.MD.A.1), which the math-grade-4 frame teaches in its unit 6,
  about the same weeks as science unit 4.
- **Why it matters.** Lesson 13 of frame-write.md names percent; reading a millilitre scale before the unit is met
  is a smaller version of the same fault.
- **Fix.** Unit 2: "The state's energy data are shown as a bar graph or picture graph ordered by size ('of every 10
  lights lit in our state, about 4 run on natural gas'), with no percent and no number over 1,000,000." Unit 4:
  "Water is measured in equal cupfuls (a nonstandard equal unit, as grade 3 counted washers) until math teaches
  millilitres." Add both to s4-energy-resources and s4-weathering-erosion cross_subject under "For the lead".
- **Evidence and confidence.** EIA state profile format from memory; math rows and math-grade-4 frame. Firm for
  percent, likely for millilitres.
- **LAYER** frame. **REPEAT** yes (lesson 13).

### 3. The math calendar is wrong for 4.OA.C.5, and cites the base text's units elsewhere

- **What is wrong.** The Cross-subject table says the math base text teaches 4.OA.C.5 in its first unit, so no bridge
  is needed. The written math-grade-4 frame places m4-patterns in its unit 7 (about school days 97 to 111), after
  science unit 3 (school 60 to 79). The other cells give the base text's unit numbers (fifth, sixth and ninth;
  seventh; fifth) where the math frame has m4-multistep-problems in unit 8, m4-lines-angles in unit 9 and
  m4-unit-conversion in unit 6.
- **Why it matters.** The 4.OA.C.5 row's "if later" says the bridge is probably not needed; it is needed. The
  other errors do not change a science day, since their bridges hold.
- **Fix.** 4.OA.C.5 row: "math grade 4 unit 7 (late); the bridge is used: the code rule is stated and followed, no
  features of the pattern explained." Other rows: name math grade 4 units 8, 9 and 6.
- **LAYER** frame. **REPEAT** new.

### 4. No paper path or student-account line

- **What is wrong.** Every unit lists a simulation for the no-kit path; the frame never says each electronic tool has
  a paper path and needs no student account (grades 2 and 6 say it).
- **Fix.** Add to the Materials bullet: "Every simulation has a paper path (the same data on a printed sheet) and
  needs no student account."
- **LAYER** frame. **REPEAT** yes (lesson 14).

### 5. Stale note: ELA grade 4 has already planned the animal structures

- **What is wrong.** The Cross-subject paragraph says "ELA's frame should plan for teaching the animal structures
  its texts need", and "For the lead" item 2 ends "the ELA frame may raise it again". The ELA grade 4 frame is written
  and already says unit 2's book teaches the structures and functions it needs (its Cross-subject table, 4-LS1-1).
- **Why it matters.** The brief's stale-notes rule: a note that says something is not yet done when the repository
  shows it is.
- **Fix.** Replace the sentence with "ELA grade 4 unit 2 (about days 39 to 77) teaches the structures its texts need
  from its own book; science unit 6 deepens them later." In "For the lead" item 2, drop "the ELA frame may raise it
  again".
- **LAYER** process. **REPEAT** yes (lesson 15).

### 6. Unit 4's anchor leads with the puzzle grade 3 already solved

- **What is wrong.** Grade 3 unit 5's anchor is seashell fossils in a hill far from the sea, explained as "sea once
  covered it"; grade 6 unit 4 opens on a sea fossil near the top of Mount Everest. Grade 4 unit 4's anchor names
  "seashell fossils high in the layers" beside the river and striped walls.
- **Why it matters.** Lesson 11 (picks do not repeat another grade's), and an anchor must puzzle; the shells will
  not. The canyon and its ordered layers will.
- **Fix.** Anchor: "the Grand Canyon: a small river at the bottom of a canyon a mile deep, and the same stripes of
  rock on both walls". The shell-above-plant layers stay as the 4-ESS1-1 evidence met in the lessons, opened by a
  retrieval task on grade 3's fossils.
- **LAYER** frame. **REPEAT** yes (lesson 11). **Confidence** judgment call.

## What is right and should not be touched

- The energy transfer arrows built on a collision students can watch, then extended through sound, light, heat
  and current, then across a wave.
- 3-5-ETS1-2 taught in full on codes and reused on hazards; the device as the start of test and
  improve, with the planned fair test left to grade 5.
- The order argued against social studies grade 4 (resources before its unit 6, hazards before its unit 7), and the
  ELA tension named rather than hidden.
- All three 4-PS4-3 examples (drums, a grid of 1s and 0s, Morse code) and the 4-ESS3-1 effects (dams, mines, burning
  fuels) in place; the boundaries (no number measures of energy, no electromagnetic waves, no retina) kept.
- Respond days, "Candidate:" cells, sensitivity line, safety bullet, stated time a day.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Sound shown on a slinky pushed along its length; no wave-type names | Accurate at grade 4, inside the boundary | docs/courses/science-grade-4/frame.md, unit 3 |
| State energy data as an ordered bar or picture graph, "of every 10", no percent | No percent before grade 6 | frame.md, unit 2 |
| Water in equal cupfuls until math teaches millilitres | Same rule grade 3 used for mass | frame.md, unit 4 |
| Unit 4 anchor leads with the river and the matching walls | The shells are grade 3's solved puzzle | frame.md, unit 4 |
| Keep unit 6 last (the frame's own item-level pick) | Hazards must end before social studies unit 7; ELA teaches its own structures | frame.md, For the lead 2 |

## For Cory

- **Time a week (audience)** and **materials cost (money)**, as the frame's "For the lead" items 1 and 6 raise them.
- **A science teacher's read of safety (people):** unit 2's circuits and solar heaters and unit 5's shake table are
  the items a qualified reader should see first.

## Lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation of the grade has no unit, or a unit claims one it only touches | Met (all 15 placed and taught to their examples) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met (unit 4's anchor to be reworded, finding 6) |
| Progression lines (model assumed but not built, practice that grows nowhere) | Met: energy arrows and the wave and light-ray models are introduced before use; compare-several grows from grade 3 |
| Rubric rows read at frame level: S10 accuracy, S11 placement, S12 math, S13 engineering, 2f how science works | S10 missed once (finding 1); S11 met; S12 missed in part (finding 2); S13 met (units 2, 3, 5); 2f met (units 4 and 6) |

## What I could not judge

The exact NGSS wording, from memory only; element-level practices and crosscutting concepts (the frame's "For the
lead" item 5 sends them to the scope and sequence, which is right). Whether unit 3's 15 days hold both a wave model
and a full compare-several design task is for the scope and sequence to show; I read it as tight but possible.

## Sources

- NGSS 4-PS3-1 to 4-PS3-4, 4-PS4-1 to 4-PS4-3, 4-LS1-1, 4-LS1-2, 4-ESS1-1, 4-ESS2-1, 4-ESS2-2, 4-ESS3-1, 4-ESS3-2,
  3-5-ETS1-2, https://www.nextgenscience.org/ (from memory, not re-fetched).
- US Energy Information Administration state energy profiles, https://www.eia.gov/state/ (format from memory).
- Repository files listed under "What I read".

## For the source list

Nothing new read this run.
