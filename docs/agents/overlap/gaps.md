# Curio Class overlap pass: gaps

Gaps found while tagging all 586 tools. Each gap lists move-to-gap candidates where a planned tool can be re-pointed without losing coverage: its module's standards are also covered by another tool in the same band. Live tools are never candidates.

Move-to-gap is rarer than it looks. Most planned modules carry standards no other module carries (the CSTA 2026 grade-level indicators, for example, give each grade its own codes), so re-pointing them would open a new gap. Where no safe candidate exists, the gap is listed with a "new module" or "add the standard to an existing module" suggestion instead. Both of those are data edits, outside this pass.

## G1. Engineering design in K-5

- **What is missing:** no module carries K-2-ETS1 or 3-5-ETS1. MS-ETS1 (bridge-builder) and HS-ETS1 (design-challenge-studio) are present.
- **Why it matters:** NGSS expects every K-5 grade band to define a problem, compare solutions and test them.
- **Candidates (add the standard, no move):**
  - K-2: shade-builder (K, design a shade that keeps a surface cool) already runs the design-test loop. Add K-2-ETS1-1 to K-2-ETS1-3 to its module.
  - 3-5: rube-goldberg-workshop, retitled "Contraption Workshop" in C20 (g4, 4-PS3-4 is itself a design PE). Add 3-5-ETS1-1 to 3-5-ETS1-3 to its module.
- **Move-to-gap:** none needed.

## G2. NGSS performance expectations with no module

| PE | What it asks | Candidate |
|---|---|---|
| HS-LS2-5 | carbon cycling through photosynthesis, respiration and the spheres | **population-dashboard, move-to-gap** (C38). Its HS-ESS3-1 and HS-LS2-1 are also on island-economy and carrying-capacity. New concept: "Carbon Relay" (in C38). |
| HS-LS2-3 | cycling of matter and energy in aerobic and anaerobic conditions | Fold into Carbon Relay above (one hop runs without oxygen), or add to energy-accountant's module. |
| HS-PS3-4 | thermal equilibrium when two components mix | **ph-detective, move-to-gap (alternative to its rename in C40).** Its HS-PS1-2 is covered elsewhere in 9-12. Concept: "Even Out: Drop hot metal into cold water, mix hot and cold water, and predict the final temperature; watch energy flow until both sides match." Caution: 9-12 already has 12 lab settings. |
| HS-ESS2-7 | coevolution of Earth's systems and life | Possible move-to-gap for biome-atlas (its standards are covered by other 9-12 science tools). Concept: "Living Planet: Scrub through four billion years and watch life and Earth change each other: microbes fill the air with oxygen, plants build soil, reefs build coastlines." Low priority; biome-atlas is a good tool as written. |
| MS-PS2-4 | gravity depends on mass | Add to planet-builder's module (g6, a gravity sandbox; a planet-mass slider would carry it). No move. |
| MS-LS1-8 | sense receptors send signals to the brain | No safe candidate in 6-8 science. New module in a later wave. |
| MS-LS4-5 | genetic engineering and artificial selection | Add an artificial-selection mode to gene-pool's module (g8). No move. |

## G3. CSTA computer science coverage

- **What is missing:** 111 of the 196 CSTA identifiers in the standards set are not on any module. The largest holes:
  - Computing and Society (SOC: history, culture, human factors, ethics) in grades K-4, plus parts of MS-SOC and HS-SOC.
  - Data: inference and models (DAT-IM) at every level.
  - Hardware and software (SYS-HW) in grades 3-5 and middle school.
  - Program development and testing (PRO-RD, PRO-TR) in middle and high school.
  - Several algorithm indicators (ALG-IM).
- **Caution:** I read these from the code prefixes in data/modules.csv. I did not check every sub-code's wording against the CSTA 2026 text, so a few of the 111 may be covered in substance by a module tagged with a sibling code.
- **Candidates:**
  - SOC in K-2: pattern-finder, reshaped in C12 to "Spot the AI" (everyday uses of AI), is a natural place to add a K-2 SOC indicator alongside its current codes.
  - SYS-HW in 3-5 and MS: computer-builder is the existing hardware tool. Add the 3-5 and MS codes to that family in a later wave rather than stretching one tool across bands.
- **Move-to-gap:** none. CS tools carry unique codes. The CTE and world-language tools are the only subjects whose standards are fully covered elsewhere, and CTE is already thin (G6), so pulling tools out of them would trade one gap for another. Recommend new CS modules in a later wave.

## G4. ELA

- **Speaking and listening:** SL codes appear only at grades K, 6, 8, 9-10 and 12. Grades 1 to 5 and grade 7 have none.
  - Candidates (add the standard, no move): retell-puppets ("Bedtime Retell", C10) and two-sides-theater ("Bear's Side of the Story", C07) both have learners speaking to the class; one SL code each at their grade would fit. counterclaim-ping-pong (g7) is spoken argument and can carry SL.7.
- **Fluency:** RF.x.4 appears only at grade 1. Grades 2 and 3 have no fluency tool. No safe move candidate; new module.
- **Writing in grade 6:** no grade 6 informative or narrative writing module. debate-prep-desk ("Reason Builder", C13) stays on argument. New module.
- **Conventions in grades 3 and 4:** thin. mad-libs-machine ("Story Blanks", C20) is the only grade 3 grammar play tool.

## G5. Social studies

Module counts by grade: 5 each for K-5, 7 or 8 each for 6-8, then 4 (g9), 5 (g10), 8 (g11) and 16 (g12).

- **No 9-12 geography.** Geography stops at grade 8 (five-themes-field-trip, region-compare).
- **No world history before 1750 in 9-12.** Grade 9 starts at the Enlightenment.
- **Civics, economics and psychology all sit in grade 12** (16 modules), while grade 9 has 4.
- **Thin 6-8 economics:** 6-8 economics appears only inside history units (silk-road-traders, salt-and-gold-caravan, mill-town); there is no 6-8 economics module of its own.
- **Candidates:** none for move-to-gap; every SS module carries its own C3 indicator. The grade 12 stack is the natural source if Cory wants to rebalance grades (for example, federal-or-state and checks-and-balances to grade 9 civics), but that is a course-sequence decision, not an overlap fix.

## G6. Thin subjects and bands

| Area | Count | Note |
|---|---|---|
| SEL | 2 per band, 8 total, all live | No planned SEL tools at all. |
| Library | 2 per band, 8 total | K-2 pair is live. |
| Health-PE | 6 per band | 6-8 has no nutrition tool (pressure-point, stress-toolkit, boundaries-builder, screen-time-detective, rules-referee, goal-tracker). |
| CTE | 0 in K-5, 3 in 6-8, 11 in 9-12 | Career awareness in K-5 is absent. |
| World languages | 10 K-12, 7 6-12, 3 9-12 | No K-5-specific tools. |
| Arts K-2 | 7 | Only 1 theater (story-dress-up) and 1 dance (move-like-me). |
| Arts 3-5 | 8 | No media arts in K-5 at all. |

- **Move-to-gap candidate:** boundaries-builder to 6-8 nutrition (alternative to its reshape in C04). NHES.S4 is also on feelings-faces and pressure-point, so nothing is lost. Concept: "Fuel Check: Plan a day of meals and snacks around a busy schedule (practice, a test, a late night), then see how energy, focus and mood hold up and adjust the plan." Recommendation stays with the C04 reshape, because relationships are a required 6-8 health topic and the reshape keeps it.

## G7. Overused actions and formats

| Band | Overused | Rare |
|---|---|---|
| K-2 (124 tools) | format showdown 20; actions build 12, explore 12 | escape 1 |
| 3-5 (137) | format puzzle 16; actions explore 13, compose 12, build 12 | creature 1, sandbox 2, escape 2 |
| 6-8 (153) | action simulate-tune 19; format simulator 16 | showdown 1, escape 1 |
| 9-12 (209) | actions explore 30, simulate-tune 29; formats simulator 28, explorer 25 | creature 1, showdown 1 |

- The cluster fixes shift a few of these: C08 and C09 move a K-2 builder and a K-2 tycoon to manipulate; C13, C14 and C29 move 6-8 and 9-12 debates and tycoons to fix, order and investigate; C38 removes one 9-12 data desk.
- No format goes above 25 percent of any subject.
- **Recommendation for future specs:** in 9-12, prefer predict-reveal, order, fix and trace over another explore or simulate-tune; in 3-5, a sandbox or creature tool is the cheapest way to add variety.
