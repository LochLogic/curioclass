# Sequence read: science-grade-4 (Grade 4 science), 2026-11-14

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2), and the "Settled by the expert" tables of the
  social studies K to 5 sequence reads of today (not the Codex ones).
- Cold, as it now stands after the reconcile: docs/courses/science-grade-4/scope-and-sequence.md and
  data/plans/science-grade-4/days.csv (all 120 days). I did not open the reconcile report.
- Beside them: docs/courses/science-grade-4/frame.md (brief, seams, units 4 and 6), the grade 1 to 4 rows of
  data/progressions/science.csv, data/standards/ngss-pe-dimensions.csv (grade 4 and 3-5-ETS1 rows),
  docs/courses/CALENDAR.md and data/plans/calendar.csv (grade 4 rows).
- Gates: `plan.py check` passes for this course (0 failures), with notes on days 24 and 37 ("reads like hands-on work but
  names no supplies and no safety"); it fails on biology, another course being written now. `frame.py calendar` places the
  checks in weeks 10, 19 and 30 with no stagger break. `stale.py check`: 56 files, 0 failures.
- For REPEAT: the non-Codex reads in docs/reviews/, including my grade 3 read of today. I did not open any Codex read.

## Verdict

A good year with a clear energy, waves, Earth and structures storyline, engineering in three units and the qualitative
wave boundary respected. It is not ready for unit plans: units 2, 4 and 6 each put two or three expectations on one
45-minute end day, and day 37 judges 4-PS3-2 from teaching-day records instead of a new case. Readiness is half applied
(two grade 2 rows treated as kept in use), reteaches sit on three hook days, and course-level checks re-score unit
portfolios. All fixes move work inside the 120 days.

## Findings, most serious first

### 1. Three units assess two or three expectations on one end day (serious; likely)

- **LAYER** sequence. **REPEAT** new (grade 3 split its assessments; grade 5 has the same fault, its finding 2).
  **Confidence** likely.
- **What is wrong.**
  - Day 37 (unit 2) holds 4-PS3-2, 4-PS3-4 and 4-ESS3-1, and judges 4-PS3-2 from the observation records of teaching days,
    not a new case.
  - Day 72 (unit 4) holds a hands-on erosion comparison (4-ESS2-1) and a rock-layer landscape history (4-ESS1-1).
  - Day 116 (unit 6) holds two models (4-PS4-2, 4-LS1-2) and two written arguments (4-LS1-1).
- **Why it matters.** Nine- and ten-year-olds cannot plan, observe and write for three expectations in 45 minutes; the
  writer will cut parts, and a record from a teaching day tests memory, not transfer (the lens's end-of-unit rule).
- **Fix (settled here, no day cost).**
  - Unit 2: day 35's work folds into day 34; day 35 is the consensus (was 36); day 36 is Check end for 4-PS3-2 (new
    observation stations showing energy moved by sound, light, heat and electric current; give its supplies and safety)
    and 4-PS3-4 (design portfolio plus a trace of a new device); day 37 is Check end for 4-ESS3-1 (two new sources). The
    shorter path replaces "35 into 34" with "103 into 102".
  - Unit 4: day 70 folds into day 69; day 70 is the consensus; day 71 is Check end for 4-ESS2-1; day 72 is Check end for
    4-ESS1-1. The shorter path replaces "70 into 69" with "98 into 97".
  - Unit 6: day 114 absorbs day 115's transfer rehearsal; day 115 is Check end for 4-PS4-2 and 4-LS1-2 (two models);
    day 116 is Check end for 4-LS1-1 (two arguments). The "114 into 113" fold stays.
  - Units 1, 3 and 5 stay at one end day; the unit plan times them.
  - The gate's notes on days 24 and 37 are false positives as written (supplied records); the new day 36 stations need
    supplies and safety.

### 2. Two grade 2 rows get retrieval where rule 2 needs readiness (moderate; firm)

- **LAYER** sequence, frame. **REPEAT** yes (grade 5 finding 1, larger there). **Confidence** firm.
- **What is wrong.** s1-signal-device was last used in grade 2 and is treated as "maintained", with retrieval on day 48.
  s1-see-with-light was last used in grade 2; day 18's refresh covers s1-light-materials, not seeing by reflected light,
  and unit 6 relies on it. The frame's rule (lines 17 to 18, "a row from grade 2 or 3 ... opens with a retrieval task")
  conflicts with rule 2, which has no exception for a row two grades back.
- **Why it matters.** A teacher gets no signal on who lacks the idea before the ray model and the information codes
  build on it.
- **Fix.** Add s1-signal-device to day 41's readiness check (beside s1-sound-vibrates), with the reteach on day 43. Add an
  s1-see-with-light readiness check in day 93's last ten minutes, with the reteach inside a unit 6 lesson before the ray
  model, not on the first day. Rewrite frame lines 17 to 18 as rule 2 states it, and align the seams at lines 103 to 110
  and the progression notes. s2-water-where readiness on day 76 is right; leave it.

### 3. Reteaches sit on three unit first days (moderate; firm)

- **LAYER** sequence. **REPEAT** new (grades 3 and 5 got this right). **Confidence** firm.
- **What is wrong.** The one-lesson reteaches are on days 16, 42 and 77, the hook days of units 2, 3 and 5.
- **Why it matters.** Splitting the class on the hook day breaks the question board, which rule 2 keeps clean.
- **Fix.** Move them to day 18 (the sunlight warming day), day 43 and day 78.

### 4. Course-level checks re-score unit portfolios, and day 119 is overloaded (moderate; likely)

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** Day 39 carries the unit 2 design portfolio forward for 4-PS3-4; day 74 re-scores the 3-5-ETS1-2
  records from unit 3. Day 119 holds three expectations.
- **Why it matters.** The same artifact scored twice is not a check of what is retained, and an overloaded year-end day
  repeats finding 1's fault.
- **Fix.** Day 39 lists 4-PS3-1, 4-PS3-3 and 4-PS3-2 only (the unseen device's energy path drawn). Day 74 drops
  3-5-ETS1-2; its 4-PS4-3 item asks students to write one more code and compare it with two given codes against criteria.
  Move 4-PS4-2 to day 118 (a ray model of unit 2's illuminated device); day 119 keeps 4-LS1-2 and 4-LS1-1. Day 75's
  wave-basin erosion context is good; keep it.

### 5. The frame's fossil case is on no day (minor; firm)

- **LAYER** sequence. **REPEAT** new. **Confidence** firm.
- **What is wrong.** The 4-ESS1-1 clarification case the frame names (marine shells in layers above plant fossils: land
  became sea) is taught on no day.
- **Fix.** Add it to day 67 or day 69 as a layered rock card set.

### 6. Day 57 piles five retrievals onto the hook day (minor; likely)

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **Fix.** Day 57 keeps s2-fast-slow-events. Move s3-weather-data to day 62 and s2-erosion-solutions to day 65; s3-fossils
  stays on day 67.

## Checked and found right (do not undo)

- sk-sun-warms readiness on day 15 and s1-sound-vibrates readiness on day 41, both in the right last-ten-minutes slots.
- s2-water-where readiness on day 76.
- All candidate days settled; the qualitative wave boundary (no quantitative wave work) is kept.
- Engineering in units 2, 3 and 5; the $30 a unit ceiling is the frame's own settled number.
- Calendar leans and check weeks 10, 19 and 30; the shorter path is named.
- Every end day lists its unit's codes.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| Each unit's anchor is a phenomenon or design problem, not a topic | Met |
| No model used before the unit that builds it | Met |
| Engineering design in a unit | Met (units 2, 3, 5) |
| Equipment has a substitute or no-kit path | Met |
| End-of-unit task is a new case | Missed on day 37 for 4-PS3-2 (finding 1); met elsewhere |
| Three dimensions joined on the end days | Met in kind; crowded (finding 1) |
| Safety named | Met; new day 36 stations need it |
| Readiness rule 2 | Partly met (finding 2); reteach placement off (finding 3) |
| Check days name every owned code | Met |

## Settled by the expert

| Item | Settled as |
|---|---|
| Unit 2 end | 35 into 34; 35 consensus; 36 Check end 4-PS3-2 and 4-PS3-4; 37 Check end 4-ESS3-1; shorter path "103 into 102" |
| Unit 4 end | 70 into 69; 70 consensus; 71 Check end 4-ESS2-1; 72 Check end 4-ESS1-1; shorter path "98 into 97" |
| Unit 6 end | 115's rehearsal into 114; 115 Check end 4-PS4-2 and 4-LS1-2; 116 Check end 4-LS1-1 |
| Units 1, 3, 5 end | One day each, as written |
| Readiness | s1-signal-device added to day 41; s1-see-with-light check in day 93's last ten minutes; frame rule and seams follow rule 2 |
| Reteach days | 18, 43, 78 |
| Course checks | Day 39 without 4-PS3-4; day 74 without 3-5-ETS1-2; 4-PS4-2 on day 118 |
| Fossil case | Day 67 or 69 |
| Day 57 retrievals | Split across days 57, 62, 65, 67 |

## For Cory

None.

## What I could not judge

- Whether units 1, 3 and 5 fit their two end-day expectations in 45 minutes; the unit plan's timed task will show it.
- Whether the shorter path (90 meetings) holds every expectation at depth; the folds are named but the route is not yet
  demonstrated day by day.

## Sources

- S:\CurioClass\docs\courses\science-grade-4\scope-and-sequence.md; data\plans\science-grade-4\days.csv;
  docs\courses\science-grade-4\frame.md; data\progressions\science.csv; data\standards\ngss-pe-dimensions.csv;
  docs\courses\CALENDAR.md; data\plans\calendar.csv.
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\science.md;
  docs\RUBRIC-SCIENCE.md.
