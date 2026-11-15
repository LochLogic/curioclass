# Sequence read: science-grade-7, 2026-11-14

Expert cold read of the scope and sequence for Science, Grade 7, done to docs/pipeline/briefs/sequence-read.md against docs/RUBRIC-SCIENCE.md (scope and sequence layer: Gateway 1 at plan level, 2a to 2c, 2e, 2h, S1, S6 costs, S7, S11). The read is my own; no Codex read was opened.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, the brief.
- docs/courses/science-grade-7/frame.md and scope-and-sequence.md in full.
- data/plans/science-grade-7/days.csv (all 160 rows) and source-map.csv.
- data/progressions/science.csv: every row the grade 7 rows assume, traced to its last user.
- data/plans/calendar.csv (grade 7 rows for all four subjects).
- The OpenSciEd storylines for 7.1 to 7.6 in S:\CurioClass-sources\openscied-ms (lesson questions and base days; ideas only).

Gates: `scripts/plan.py check` shows 0 failures for science-grade-7. `scripts/frame.py calendar` puts its course-level checks in weeks 14 and 32, on days 67 and 159, which matches the calendar. `scripts/stale.py check` shows 0 failures. Biology fails 14 checks because a Codex run is writing it now: another course, not this one.

## Verdict

The course keeps the base order in every unit, places all 89 base lessons, and its cross-subject day ranges match the calendar exactly. Its one serious problem is the returning-skill rule. The frame redefines "two or more grades back" as "two or more grades between", and the scope and sequence then applies the two readings by turns. As a result, six rows and two models that were last used in grade 5 open with a retrieval task, or with no opening at all, while two other grade 5 rows get readiness checks. The other findings are smaller: course-level checks claim more than 40 minutes can hold, and the source map counts some days twice.

## Findings

### 1. The readiness rule is applied unevenly; six grade 5 rows and two models miss their checks (serious)

- **What is wrong.** Sequence-write rule 2 gives a retrieval task only to a row used the year before (grade 6) or earlier this year. Every other earlier-grade row the unit assumes gets a readiness check. The lead confirmed this literal reading for the social studies fixes (docs/reviews/sequence-6-8-fixes-2026-11-14.md). The grade 7 frame instead writes the rule as "two or more grades between its last use and this one" and calls grade 5 rows "idle one grade". The scope and sequence follows the frame for some rows and the brief for others.
  - **Checked (correct under the brief).** s5-food-energy-sun (day 68). s5-protect-resources, s3-environment-change-solution (last used grade 4 by s4-energy-resources) and s1-parent-offspring (last used grade 3 by s3-animal-groups), all on day 96.
  - **Missed, all last used in grade 5:**
    - **s5-plant-matter.** Assumed by s7-photosynthesis. Day 69 says grade 6 cells carry it, but no grade 6 row assumes it.
    - **s5-matter-movement, with its food-web and matter-cycle models.** First used on day 58 (s7-cell-respiration-growth), where the note says "last used in grade 5" and gives a retrieval task. Days 97 and 115 then count unit 3's use as "earlier this year", but unit 3's use was itself the unchecked return.
    - **s5-identify-materials and s5-new-substances.** Assumed by s7-food-molecules (unit 3) and s7-synthetic-materials (unit 4). Days 7 and 10 "revisit" them in unit 1 with no check, and later units count that as earlier-year use.
    - **s4-energy-resources.** Assumed by s7-resource-distribution (unit 6); its last user is grade 5's s5-protect-resources. Day 88 revisits it and day 143 retrieves it, with no check.
- **Why it matters.** A readiness check is the only point where a gap from two years back shows up before the unit leans on it. Here a class can reach photosynthesis, the matter cycle and resource distribution without one. The uneven use also makes the plan harder to audit: two grade 5 rows are checked and six are not, on the same rule.
- **Fix.** Correct the frame's sentence to the brief's wording and its seam table to match, then:
  - **Day 1, last ten minutes:** a check on s5-identify-materials and s5-new-substances. The explicit revisits on days 7 and 10 become the named response.
  - **Day 41:** 30 minutes of assessment, 10 of response, and 10 of readiness on s5-matter-movement with its food-web and matter-cycle models. The response runs inside day 58, which then retrieves rather than reintroduces.
  - **Day 68:** add s5-plant-matter to the s5-food-energy-sun check. Day 70's response covers both, and day 69's note drops the grade 6 claim.
  - **Day 128, last ten minutes:** a check on s4-energy-resources, with the response inside day 143's opening (or day 88's revisit moves to the response).

  Units 1, 3, 4 and 6 have 0, 35, 45 and 10 spare minutes against their frame budgets, so a full reteach lesson does not fit. Where it does not, the response runs inside the lesson that first uses the row, as day 70 already does. The lead records that exception in the frame's Days entry, or condenses a named base day instead.
- LAYER: frame and sequence. REPEAT: yes (the social studies reads found the same rule misapplied). Confidence: firm on the inconsistency; likely on the fix, since the lead chooses between a response inside a lesson and a further condensation.

### 2. Both course-level checks claim every part of four codes in 40 minutes (moderate)

- **What is wrong.**
  - **Day 67:** four codes (MS-PS1-2, MS-PS1-5, MS-PS1-6, MS-LS1-7) in four evidence blocks in 40 minutes. The note says "each part of each listed code is elicited".
  - **Day 159:** the same claim for four other codes (MS-LS1-6, MS-LS2-4, MS-ESS3-1, MS-ESS3-4).

  That is about 10 minutes per expectation, including the practice and the crosscutting concept.
- **Why it matters.** Each unit's end-of-unit assessment already covers each part of its codes. A course-level check that claims full coverage again either cannot be written in the time, or gets written as recall. Either way it misleads the unit-plan and answer-key writers.
- **Fix.** Both notes name the part each block samples (for example: MS-PS1-6's test-and-modify part, carried by the day 41 portfolio) and call the check a sample across units. The scope and sequence's course-level check lines change to match.
- LAYER: sequence. REPEAT: yes. Confidence: firm.

### 3. The source map counts several days twice, and day 94's research shares a lesson's time without minutes (minor)

- **What is wrong.**
  - **Days counted twice.** The "ours" rows list days 1 and 3 (the safety sheet), 68, 94 and 96, and every one of those days also appears under a base lesson (7.1 lesson 1, check 1's respond day, 7.4 lesson 14, 7.4 lesson 15). Day 68 is listed twice among the "ours" rows alone.
  - **Day 94.** The frame funds 50 minutes of synthetic-material research for MS-PS1-3 on its own. Day 94 instead "shares the model synthesis with day 93", so base lesson 14 (2 base days) and the research share two periods. One of the two is short, and the map does not say which.
- **Why it matters.** The source map is how the lead checks the frame's loss claim. When days are counted twice, it cannot show what was kept.
- **Fix.** Give split days minutes, as the grade 8 map does (day: minutes for each source). Day 94 records its split, for example lesson 14 at 30 minutes and the research at 20, with the rest of the research taken from unit 4's 45 spare minutes on a named day. Remove the duplicate day 68 row.
- LAYER: process. REPEAT: new. Confidence: firm.

## What is right (do not touch)

- **Base order and the source map.** Every unit keeps the 7.1 to 7.6 lesson order. All base lessons are placed, including the two optional 7.5 lessons, which are cut at 0 days as the frame says.
- **Mid-unit assessments.** Every unit over 25 days has one: day 54 in unit 3, 82 in unit 4, 113 in unit 5 and 148 in unit 6. Unit 1 keeps the base midpoint on day 13 as well.
- **Response counted once.** Each response runs once, and readiness never falls on a unit's first day. Day 97 says so in its own note.
- **Course-level checks draw from earlier units.** Day 67 frames its cell food-use case with unit 1 property records and unit 2 energy records. Day 159 uses the geology of a resource for a unit 4 synthetic material, and unit 5 land-use evidence for the consumption argument.
- **Cross-subject cells.** The frame's day ranges for math 7 and ELA 7 match calendar.csv. The ELA research overlap with unit 6 (days 154 to 156) is flagged for the lead.
- **Shorter path.** The section is present, with ten unassessed folds (days 3, 6, 12, 28, 37, 46, 56, 71, 116 and 137).
- **Safety and sensitivity.** The safety and sensitivity notes are specific and carried on every day that needs them: the health case, the farmers' and Indigenous communities' voices, and community water.

## What I could not judge

- The EdReports 6 to 8 science evidence guide (not read this session).
- Real classroom fit of the 40-minute course-level checks.
- The element references, which I sampled, not checked row by row.
- Material costs, which are unpriced in the plan.

## Sources

The OpenSciEd Middle School 2022 storylines for 7.1 to 7.6 (S:\CurioClass-sources\openscied-ms, CC BY 4.0, ideas only); data/progressions/science.csv; data/plans/calendar.csv; data/standards/ngss-pe-dimensions.csv; docs/reviews/sequence-6-8-fixes-2026-11-14.md (the lead's clarification of the readiness rule).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Readiness checks added: day 1 (s5-identify-materials, s5-new-substances), day 41 (s5-matter-movement and its food-web and matter-cycle models), day 68 (adds s5-plant-matter) and day 128 (s4-energy-resources), each response named inside the lesson that uses the row | Applies the readiness rule by last use; the timing rule is unchanged | data/plans/science-grade-7/days.csv, scope-and-sequence.md, frame.md seams |
| Day 41 becomes 30 minutes of assessment, 10 of response and 10 of readiness | Makes room for the unit 3 check inside existing time | days.csv |
| Day 69's note drops "carried by grade 6 cells"; days 97 and 115 cite this year's checked use | The notes match the progression | days.csv |
| The notes for days 67 and 159 name the part each block samples and call the check a sample | Coverage claims match the minutes | days.csv, scope-and-sequence.md |
| The source map gives minutes for split days, records day 94's split and drops the duplicate day 68 row | The base record can be checked | source-map.csv |

## For Cory

Nothing needs Cory: there is no scope, money, people or audience question. If the lead chooses further base condensation over responses inside lessons for finding 1, the year still holds at 160, which Cory has already settled.
