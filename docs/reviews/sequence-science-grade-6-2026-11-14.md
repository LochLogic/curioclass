# Sequence read: science-grade-6, 2026-11-14

Expert cold read of the scope and sequence for Science, Grade 6, done to docs/pipeline/briefs/sequence-read.md against docs/RUBRIC-SCIENCE.md (scope and sequence layer: Gateway 1 at plan level, 2a to 2c, 2e, 2h, S1, S6 costs, S7, S11). The read is my own; no Codex read was opened.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, the brief.
- docs/courses/science-grade-6/frame.md and scope-and-sequence.md in full.
- data/plans/science-grade-6/days.csv (all 160 rows) and source-map.csv.
- data/progressions/science.csv (assumes chains for every row the course uses), data/plans/calendar.csv (grade 6 rows).
- The OpenSciEd storylines for units 6.1 to 6.6 in S:\CurioClass-sources\openscied-ms (lesson questions and base days, for order and the source map; ideas only).
- The social studies sequence reads' "Settled by the expert" tables, for the standard applied.

Gates: `scripts/plan.py check` shows 0 failures for science-grade-6. `scripts/frame.py calendar` puts its course-level checks in weeks 18 and 32, which matches the calendar. `scripts/stale.py check` shows 0 failures. Biology fails 14 checks because a Codex run is writing it now: another course, not this one.

## Verdict

The course is close. The base order is kept unit by unit, the source map's base days match the storylines, and the retrieval and readiness calls are right for almost every returning row. One part of unit 3 is not: its climate days (85 to 88) label a Curio Class addition as base lesson 19 and leave that lesson's own content, and the frame's second anchor, without a day. One readiness check is missing, and the assessment periods claim more parts than their minutes can carry. All of it can be fixed inside the units' current days.

## Findings

### 1. Unit 3's climate arc drops base lesson 19 and leaves the second anchor unopened (serious)

- **What is wrong.**
  - **Day 85** is labelled base 6.3 lesson 19, but its goal is sun angle by latitude and uneven heating. Lesson 19's own content gets no time: prevailing-wind patterns, the two hemispheres mirroring each other, and climate as the long-run average of weather.
  - **Days 86 and 87** are labelled lesson 20, but they run density-driven circulation (warm, cold, fresh and salty water) and global wind and current patterns. Lesson 20's question, how ocean temperature and currents change evaporation and so the humidity of air masses, is not asked.
  - **Day 88:** lesson 21 (2 base days: two coasts compared, elevation and rain shadow) gets one day.
  - **Lesson 22**, the rainforest synthesis (1 base day), has no day and is not named.
  - **The second anchor.** The frame's second anchor, why some regions get far more rain, has no day that opens it.

  MS-ESS2-6 ends up with 4 teaching days, against 6 base days plus what Curio Class added.
- **Why it matters.** MS-ESS2-6 is owned here in full. Without lesson 19, students meet climate before anyone has defined it. Without lesson 20, the ocean's part in rainfall becomes a density lab that does not answer the rain question. The storyline rule says each lesson answers the question the last one raised, and every anchor needs a day that opens it.
- **Fix (settled below, a day swap inside the unit).** Fold day 71 into day 70; the Shorter path already pairs them and nothing assessed moves. Renumber days 72 to 84 down by one, which frees one day for the climate arc:
  - **Day 84:** lesson 19. It opens with retrieval of latitude and shadows and states the second anchor, then covers sun angle by latitude, prevailing winds, the mirrored hemispheres and climate as the long-run average.
  - **Days 85 and 86:** lesson 20, aimed at its question: ocean temperature and currents, evaporation and air-mass humidity. The density, salinity and rotation work stays inside these days, labelled as a Curio Class addition.
  - **Day 87 and the first half of day 88:** lesson 21.
  - **The second half of day 88:** lesson 22's synthesis, which answers the second anchor.
  - **Day 89:** the end-of-unit assessment, unchanged.

  Rewrite the source map's lesson 19 to 22 rows to match.
- LAYER: base text and sequence. REPEAT: new. Confidence: firm on the mismatch between label and content; likely on the exact day placement.

### 2. s3-weather-data needs a readiness check before unit 3 (moderate)

- **What is wrong.** s6-air-masses-weather assumes s3-weather-data. In the progression, its last user is grade 4 (s4-weathering-erosion). No grade 5 row assumes it, and s5-sphere-interactions carries no data-graph model. That makes it two grades back, which needs a readiness check under sequence-write rule 2; the lead clarified the same reading for the social studies fixes (docs/reviews/sequence-6-8-fixes-2026-11-14.md). The scope and sequence and the frame instead say it was "maintained through grade 5" and open it with a retrieval task.
- **Why it matters.** Without the check, a class that has not read a weather graph since grade 4 meets air-mass data with no warning sign and no reteach.
- **Fix.** On day 51 (unit 2's end-of-unit day, now 35 minutes of assessment and 15 of response), run 30 minutes of assessment, 10 of response and 10 of readiness on s3-weather-data. The prototype portfolio from days 48 and 49 already carries the construction and testing parts. Fold day 54 into day 53, which the Shorter path already supports, so day 54 becomes the one-lesson reteach. Correct the frame seam and the scope and sequence line. If the lead instead holds that grade 5 data work keeps the row alive, the progression needs an assumes link that shows it.
- LAYER: sequence and progression. REPEAT: yes (the social studies reads found the same rule misapplied). Confidence: likely.

### 3. Base lesson 1 is condensed in units 4 and 5 without saying so (moderate)

- **What is wrong.**
  - **Unit 5:** base 6.5 lesson 1 (3 base days) maps to days 116 and 117, but day 117 is the wave reteach. The anchor, the related phenomena and the question board therefore get one period.
  - **Unit 4:** lesson 1 (4 base days) gets days 92 and 94, with day 93 as the rock-layer reteach between them.

  The source map gives both as plain lesson 1 days, and the frame lists no condensation for either unit.
- **Why it matters.** The anchor lesson is where the question board and the initial model are built, and the frame's loss check claims every condensation is named. A reteach day counted as base time hides a real cut from the lead.
- **Fix.** In the source map, mark days 93 and 117 "ours" (reteach), and record lesson 1 as condensed in both units, saying what is kept: the anchor, the related-phenomena list and the question board. Then do one of the following:
  - recover the time from the Shorter path's unassessed folds in the same unit, settling it here as a day swap;
  - or name the condensation in the frame's source map column for the lead.
- LAYER: base text. REPEAT: new. Confidence: firm.

### 4. Assessment periods claim more parts than their minutes carry (moderate)

- **What is wrong.**
  - **Day 115:** the unit 4 end-of-unit assessment gives four full expectations (MS-ESS2-1, MS-ESS2-3, MS-ESS2-2, MS-ESS1-4) 30 minutes, with 10 of response and 10 of readiness on the same day.
  - **Day 90:** course-level check 1 runs four codes in four panels.
  - **Day 159:** course-level check 2 runs five full expectations in about 8 to 10 minutes each, yet claims "each part of each listed code".
- **Why it matters.** The brief asks that every part of every code on the row is asked. At these lengths, parts are either skipped or reduced to recall. A claim of full coverage that the minutes cannot hold misleads the unit-plan writer.
- **Fix.**
  - **Day 115:** name which parts each earlier product carries. For example, day 112's written explanation carries MS-ESS2-2's scale part and the timeline carries MS-ESS1-4. Leave the 30 minutes for the parts no product holds.
  - **Days 90 and 159:** the notes list the parts each check samples, and say they sample rather than re-cover each code. The end-of-unit assessments already cover each code.
- LAYER: sequence. REPEAT: yes. Confidence: firm on the claim; likely on the fix.

### 5. The day 115 readiness check is in the note only (minor)

The assess column for day 115 says `end`, so the data does not show the readiness check that the note puts in the last ten minutes. Fix: record both in the assess column the way other combined days do, or move the readiness to the respond position the gate reads. LAYER: process. REPEAT: new. Confidence: firm.

### 6. Day 84 is a Respond day with nothing to respond to (minor)

Day 84 has kind Respond, but no assessment comes before it. It is base lesson 18's second day. Fix: relabel it Application; after finding 1's renumbering, this day becomes day 83. LAYER: process. REPEAT: new. Confidence: firm.

### 7. Day 37 lists MS-PS1-4 without the start mark (minor)

MS-PS1-4 is begun here and completed later, but day 37's codes cell lists it bare. Fix: `~MS-PS1-4`. LAYER: process. REPEAT: new. Confidence: firm.

### 8. Stale cross-subject cells in the frame (minor)

- **The tsunami line.** The frame says ELA grade 6 unit 6 reads the 2011 Japan tsunami. The calendar's ELA unit 6 (days 137 to 156) is Galveston 1900, a hurricane. The scope and sequence line "later ELA hazard work uses the same content boundaries" should name the hurricane, or the content note moves.
- **Day ranges.** These frame ranges differ from calendar.csv by a day:
  - math statistics: 143 to 158 in the frame, 142 to 157 in the calendar;
  - negative numbers: 121 to 142, against 120 to 141;
  - social studies latitude: 26 to 39, against 26 to 38.

  The scope and sequence already uses the calendar's ranges.
- **A lean worth naming.** ELA unit 3 (days 63 to 86, "Reading the sky: how forecasters see a storm coming") runs beside science unit 3's weather work, and the frame does not mention it.
- **Fix.** Correct the frame cells and add the ELA unit 3 lean as a note: available, no dependency.

LAYER: frame. REPEAT: yes (stale calendar citations were found in the social studies reads). Confidence: firm.

### 9. Unit 6 answers "are all things made of cells?" three lessons late (minor, judgment call)

Base 6.6 lesson 7 asks whether all things are made of cells and closes with an assessment on living and nonliving images; day 147 keeps it as a checkpoint. The added microscope investigation of unicellular, multicellular and nonliving samples (day 150, with more fields of view on day 151) answers exactly that question. It sits inside lesson 10 instead, whose question is what cells need to grow and divide. Day 147's own note has to hold back a whole-code claim until the investigation arrives. Fix (settled below):
- **Day 147:** the added investigation day, labelled as ours.
- **Day 148:** the lesson 7 checkpoint, which can now claim the investigation.
- **Days 149 and 150:** lessons 8 and 9.
- **Days 151 and 152:** lesson 10, with day 151's extra fields of view folded into the first of them.

Update the source map to match. LAYER: sequence. REPEAT: new. Confidence: judgment call.

## What is right (do not touch)

- **Base order.** Every unit keeps the base order. The source map's base days match the 6.1 to 6.6 storylines lesson by lesson.
- **Retrieval calls.** s4-light-eye, s4-energy-transfer, s4-weathering-erosion, s4-earth-feature-maps, s4-hazard-solutions, s4-information-codes and s4-structures-function are each assumed by a grade 5 row, so a retrieval task is correct for every one.
- **Readiness calls.** The checks on s4-rock-layers (day 91) and s4-wave-model (day 115) are correct, each before its unit opens and never on a first day. s4-senses-brain is taught on day 13 and retrieved afterwards.
- **Course-level checks.** They draw a just-assessed unit's skills from earlier units' content: the dew case uses unit 2's cup condensation, and the day 159 cell station uses day 98's rock grains.
- **Candidates.** All are settled at 0 days.
- **Shorter path.** The section is present: 10 unassessed folds and a plan for 40-minute periods.
- **Content and care.** The age of the Earth is stated plainly. Safety controls are named on every hands-on day.

## What I could not judge

- The EdReports 6 to 8 science evidence guide (not read this session), so the Gateway 1 reading here is at plan level only.
- Real classroom timing of the 30 and 40 minute assessment blocks.
- The element-by-element references to data/standards/ngss-pe-dimensions.csv, which I sampled, not checked row by row.
- Material costs, which are unpriced in the plan itself.

## Sources

The OpenSciEd Middle School 2022 storylines for 6.1 to 6.6 (S:\CurioClass-sources\openscied-ms, CC BY 4.0, ideas only); data/progressions/science.csv; data/plans/calendar.csv; data/standards/ngss-pe-dimensions.csv; docs/reviews/sequence-6-8-fixes-2026-11-14.md (the lead's clarification of the readiness rule, as applied to social studies).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 71 folds into day 70 and days 72 to 84 renumber down by one. The climate arc becomes lesson 19 on day 84 (with the second anchor stated), lesson 20 on days 85 and 86 (the density work labelled as an addition), then lessons 21 and 22 on days 87 and 88 | Restores the base content and the owned MS-ESS2-6 inside unit 3's days; the fold is already an unassessed Shorter path pair | data/plans/science-grade-6/days.csv, source-map.csv, scope-and-sequence.md |
| Day 51 runs 30 minutes of assessment, 10 of response and 10 of readiness on s3-weather-data; day 54 folds into 53, and day 54 becomes the reteach | Applies the readiness rule by last use, inside unit 2's days | days.csv, scope-and-sequence.md, frame.md seam |
| Days 93 and 117 are marked "ours" (reteach) in the source map, and lesson 1's condensation is recorded for units 4 and 5 | Honest record of base time | source-map.csv |
| Day 115 and the two course-level checks name the parts each product or panel carries, and the checks are called samples | Coverage claims match the minutes | days.csv, scope-and-sequence.md |
| The day 115 assess column shows the readiness check | The data matches the note | days.csv |
| Day 84 is relabelled Application; day 37 gets `~MS-PS1-4` | Labels match content | days.csv |
| The added microscope investigation moves to day 147, ahead of the lesson 7 checkpoint (day 148), then lessons 8 and 9 (days 149 and 150) and lesson 10 (days 151 and 152) | Answers the question in the lesson that raises it | days.csv, source-map.csv |

## For Cory

Nothing needs Cory: there is no scope, money, people or audience question. Material costs stay unpriced until unit planning.
