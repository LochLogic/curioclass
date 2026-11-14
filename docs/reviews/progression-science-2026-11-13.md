# Expert read: science progression (2026-11-13)

Cold read by a fresh reader who did not write these rows. Layer: progression. Brief: the read-sci-expert brief
(docs/agents/EXPERT.md, lens docs/agents/lenses/science.md, rubric docs/RUBRIC-SCIENCE.md).

## What I read

- data/progressions/science.csv: 198 rows, every row in full (K 11, grade 1 10, grade 2 12, grade 3 15, grade 4 14,
  grade 5 14, grade 6 14, grade 7 18, grade 8 26, grade 9 Biology 24, grade 10 Chemistry 20, grade 11 Physics 20).
- data/progressions/science-excluded.csv: header only, 0 rows.
- data/standards/ngss-pes.txt (208 performance expectations), for coverage.
- The NGSS performance expectation pages with clarification statements, assessment boundaries and DCI articulation
  lines (AllDCI.pdf, local copy), all 208 expectations pulled and matched to their rows.
- NGSS Appendix K, Model Course Map 3 (Modified Science Domains), Table 6 and its reasoning (pp. 28 and 29 of 40).
- OpenSciEd middle school: each unit page's expectation list (6.1 to 8.6) and the Scope and Sequence PDF, Tables
  A.1 to A.3 (local copy in S:\CurioClass-sources\openscied-ms).
- The gate, `python -X utf8 scripts/plan.py check`, science block: 198 rows, 0 failures, notes only.
- Last, docs/reviews/progression-science-reconcile-2026-11-13.md (grade 4 only; nothing here contradicts it).

Not read, as the brief says: parts/, docs/courses/, earlier science reviews.

## Verdict

The progression is sound and close to finished: all 208 expectations are owned once, in the right grade or band,
with their clarifications and boundaries carried into the rows, the grades 6 to 8 split matches OpenSciEd unit by
unit, and the high school allocation follows Appendix K's modified domains map with each departure given a reason.
The real gap is in the assumes column: a cluster of grade 7 and 8 rows (and two Chemistry rows) assume nothing, or
only a practice, where the NGSS articulation names a grade 3 or 5 or middle school prerequisite, so the planner
will not see that photosynthesis builds on grade 5 plant matter and food webs. Fix those links (findings 1 to 3),
one Chemistry row that teaches past its boundary (finding 4), and a handful of stale notes; nothing needs a grade
move.

## Findings, most serious first

### 1. Grade 7 life and Earth rows assume nothing the NGSS says they build on

- **Skill ids:** s7-photosynthesis, s7-ecosystem-disruption, s7-population-consumption, s7-interaction-patterns,
  s7-biodiversity-solutions, s7-synthetic-materials; senders s5-plant-matter, s5-matter-movement,
  s5-food-energy-sun, s3-environment-change-solution, s5-protect-resources, s5-new-substances.
- **What is wrong:** the articulation lines on the MS pages name elementary core ideas that the rows never link.
  - s7-photosynthesis (MS-LS1-6) assumes only s6-cells-body-systems. Articulation: 5.LS1.C, 5.LS2.A, 5.LS2.B,
    5.PS3.D. Those are s5-plant-matter, s5-matter-movement and s5-food-energy-sun. s5-plant-matter has an empty
    hands_on, so the grade 5 "plants get their matter from air and water" idea is handed to no one.
  - s7-ecosystem-disruption (MS-LS2-4): empty assumes. Articulation: 3.LS2.C, 3.LS4.D (s3-environment-change-solution).
    It also uses the food-web model that s5-matter-movement builds.
  - s7-population-consumption (MS-ESS3-4): empty assumes and empty hands_on. Articulation: 3.LS2.C, 3.LS4.D,
    5.ESS3.C (s3-environment-change-solution, s5-protect-resources). HS-ESS3-3 and HS-LS2-7 pick the idea up.
  - s7-interaction-patterns (MS-LS2-2): empty assumes, uses food-web. Articulation names 1.LS1.B (s1-parent-offspring)
    alongside the grade 5 food web.
  - s7-biodiversity-solutions (MS-LS2-5): empty assumes; 5.ESS3.C and 3.LS4.D sit behind it.
  - s7-synthetic-materials (MS-PS1-3): empty assumes; the grade 5 new substances idea is its plain ground.
- **Why it matters:** assumes drive the probe and guard for each unit later. A grade 7 teacher plan built from these
  rows will not open with the grade 5 food web or plant matter, and a student who missed grade 5 has no named way in.
  It is the same "prerequisite not named" kind the social studies read found.
- **Fix (row edits):**
  - s7-photosynthesis assumes: add `s5-plant-matter; s5-matter-movement; s5-food-energy-sun`.
  - s5-plant-matter hands_on: set `s7-photosynthesis`.
  - s5-matter-movement hands_on: add `s7-photosynthesis; s7-ecosystem-disruption; s7-interaction-patterns`.
  - s5-food-energy-sun hands_on: add `s7-photosynthesis`.
  - s7-ecosystem-disruption assumes: `s3-environment-change-solution; s5-matter-movement`.
  - s7-population-consumption assumes: `s3-environment-change-solution; s5-protect-resources`; hands_on:
    `bio-biodiversity-simulation` (HS-LS2-7 and HS-ESS3-3 sense; if the Chemistry row that owns HS-ESS3-3 is
    preferred, use that id instead).
  - s7-interaction-patterns assumes: `s5-matter-movement; s1-parent-offspring`.
  - s7-biodiversity-solutions assumes: `s3-environment-change-solution; s5-protect-resources`.
  - s7-synthetic-materials assumes: `s5-new-substances`.
  - Add each sender to the matching hands_on so the symmetry check still passes.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** firm for photosynthesis, ecosystem disruption and
  population consumption (articulation lines); likely for interaction patterns and biodiversity; judgment call for
  synthetic materials.

### 2. Grade 8 life and energy rows with the same empty assumes

- **Skill ids:** s8-anatomical-relationships, s8-selection-math, s8-potential-energy (also s8-embryo-patterns,
  s8-human-trait-technology).
- **What is wrong:**
  - s8-anatomical-relationships (MS-LS4-2): articulation names 3.LS4.A, the fossil skill s3-fossils. Empty assumes.
  - s8-selection-math (MS-LS4-6): articulation names 3.LS4.C (s3-habitat-survival) and the variation skill. Empty
    assumes.
  - s8-potential-energy (MS-PS3-2): no articulation line, but fields and stored energy rest on s3-magnet-static,
    s5-gravity-down and the grade 4 stored energy work. Empty assumes.
  - s8-embryo-patterns and s8-human-trait-technology: no articulation line; their ground is in grade 8 itself.
- **Why it matters:** as in finding 1; the evolution unit is where students most need to see the grade 3 fossil and
  survival work again.
- **Fix (row edits):**
  - s8-anatomical-relationships assumes: `s3-fossils`; add the id to s3-fossils hands_on.
  - s8-selection-math assumes: `s3-habitat-survival; s3-variation-advantage`; add to both hands_on.
  - s8-potential-energy assumes: `s3-magnet-static; s5-gravity-down` (judgment call; s4-energy-device is a fair
    third).
  - s8-embryo-patterns and s8-human-trait-technology: leave empty, add one note line naming the same-grade rows they
    follow.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** firm for the two LS4 rows; judgment call for potential
  energy.

### 3. Two Chemistry rows do not link back to middle school

- **Skill ids:** chem-equilibrium-design (HS-PS1-6), chem-energy-accounting (HS-PS3-1).
- **What is wrong:**
  - chem-equilibrium-design has empty assumes. Articulation: MS.PS1.B (s7-reactions-atoms). Collision ideas also
    rest on s6-particle-temperature.
  - chem-energy-accounting assumes only bio-population-carrying-capacity, a link through the computational modelling
    practice. Articulation: MS.PS3.A, MS.PS3.B (s8-energy-transfer-argument, s6-particle-temperature).
- **Why it matters:** the one assumed id is a practice link that reads as a topic link; the energy content the row
  needs is grade 6 and 8 work that is never named.
- **Fix:** chem-equilibrium-design assumes `s7-reactions-atoms; s6-particle-temperature`. chem-energy-accounting
  assumes `s8-energy-transfer-argument; s6-particle-temperature; bio-population-carrying-capacity` (keep the practice
  link, but name it as such in the note). Add both to the senders' hands_on.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** firm.

### 4. chem-energy-accounting teaches past its assessment boundary

- **Skill id:** chem-energy-accounting (HS-PS3-1).
- **What is wrong:** the note says "In Chemistry the systems are thermal and chemical". The HS-PS3-1 boundary limits
  the computational model to systems of two or three components with thermal energy, kinetic energy and energy in
  gravitational, magnetic or electric fields. Chemical energy is not in it.
- **Why it matters:** a writer will build bond energy accounting days on this row and assess outside the standard.
- **Fix:** in notes replace "the systems are thermal and chemical" with "the systems are thermal (calorimeter or
  mixing water) and the Earth surface energy budget; bond energy stays qualitative, outside the HS-PS3-1 boundary".
- **LAYER:** standard. **REPEAT:** new. **Confidence:** firm.

### 5. Rows that hand on to no one

- **Skill ids:** s5-plant-matter, s2-best-material, s6-air-masses-weather, s8-growth-factors,
  s8-human-trait-technology, s7-population-consumption.
- **What is wrong:** empty hands_on. s5-plant-matter and s7-population-consumption are fixed by finding 1. The rest:
  s2-best-material to s5-properties (or the grade 5 particle work); s6-air-masses-weather to the Physics or
  Chemistry weather and climate row that owns HS-ESS2-4; s8-growth-factors to bio-cell-division-growth (HS-LS1-4);
  s8-human-trait-technology to the Biology row for HS-LS3-1 or the biotechnology note.
- **Why it matters:** a skill with no handoff looks finished, so later grades do not probe it.
- **Fix:** set the hands_on above (pick the exact high school id from the row that owns the named expectation) and add
  the matching assumes on the receivers.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** likely.

### 6. Practice-only assumes that read as topic links

- **Skill ids:** s2-heat-cool-change (assumes s1-like-parents), s2-water-where (assumes s1-parent-offspring),
  s3-motion-patterns (assumes s1-sky-patterns).
- **What is wrong:** each link carries a practice (claim, evidence and reasoning; patterns), not content. A reader of
  the assumes column sees "heating and cooling builds on young look like parents".
- **Fix:** either drop these links (the practices are tracked in model_in already) or add "(practice link:
  claim-evidence-reasoning)" in each receiving row's notes.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** judgment call.

### 7. The gate's 138 "skips N grades" notes: reasons sit on the wrong row

- **Skill ids:** many; the gate notes every hands_on that jumps a grade.
- **What is wrong:** most reasons are written, but on the receiving row, so `plan.py check` cannot see them. Most skips
  are structural: NGSS teaches some ideas only every other grade in K-5, and middle school to Physics in grade 11
  skips two grades by course order.
- **Fix:** process. Either teach the gate to read the receiver's notes for the reason, or add one stock line on
  sending rows ("next taught in grade N by the NGSS band order"). The first is cheaper and keeps the rows short.
- **LAYER:** process. **REPEAT:** new. **Confidence:** firm (the count), judgment call (which fix).

### 8. Stale notes left from the stitch

- **Skill ids:** s5-shadows-sky, s6-water-cycle-energy, s4-light-eye, s8-gravity-mass.
- **What is wrong:**
  - s5-shadows-sky: "If the K to 2 part already hands on earth-sun-moon ..., the stitcher makes this a carry". The
    stitch is done; earth-sun-moon is introduced here.
  - s6-water-cycle-energy: "if an earlier band already hands it on, it becomes a carry". Same; water-cycle is
    introduced here.
  - s4-light-eye: "merged at the stitch" wording.
  - s8-gravity-mass: notes say "Base unit 8.4" but the assumes note says "(base text unit 8.3)". OpenSciEd places
    MS-PS2-4 in 8.4.
- **Fix:** delete the stitcher sentences; in s8-gravity-mass change "8.3" to "8.4".
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** firm.

### 9. Order inside a grade lives only in the notes

- **Skill ids:** sk-ramp-design and sk-shade-design (use design-cycle; sk-define-problem introduces it);
  s5-food-energy-sun (uses food-web from s5-matter-movement); s4-rock-layers (notes say it follows
  s4-weathering-erosion, CSV lists it first); s6-air-masses-weather, s6-surface-change-scales, s6-geologic-time,
  s6-hazard-forecast (same-grade model uses).
- **What is wrong:** every model is introduced in or before the grade that uses it (checked by script, no model used
  before its grade), but 38 uses fall in the introducing grade and no column says which row comes first. The CSV
  order is not the teaching order.
- **Fix:** process, for the course frame: when the scope and sequence is written, order these pairs so the
  introducing row comes first. No row edit now.
- **LAYER:** process. **REPEAT:** new. **Confidence:** firm (the facts), judgment call (where the fix belongs).

### 10. Pace by row count

- **What is seen:** grade 8 has 26 rows against 14 in grade 6 and 18 in grade 7; Biology 24 against Chemistry 20 and
  Physics 20.
- **Why it is not a fault:** a row is an expectation owner, not a span of time. Grade 8 owns more because OpenSciEd
  completes many expectations there, after partial work in 6 and 7; OpenSciEd's unit lengths are balanced across the
  three years. Biology carries all of LS plus four ETS and three ESS, as Appendix K does.
- **Fix:** none at this layer. The course frame should check days, not rows.
- **LAYER:** progression. **REPEAT:** yes (pace was raised in social studies). **Confidence:** likely.

### 11. Words: mitochondria named before its list

- **Skill ids:** s7-photosynthesis or s7-cell-respiration-growth; s8-cell-parts-function.
- **What is wrong:** grade 7 notes use mitochondria (the 7.4 part of MS-LS1-2) but no grade 7 words list holds it; it
  first appears in s8-cell-parts-function.
- **Fix:** add `mitochondria` to s7-cell-respiration-growth words. Keep it in grade 8 as the reuse.
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** firm. Reading levels of the words otherwise fit each grade.

### 12. Two cross_subject leans missing where math is plainly used

- **Skill ids:** s8-gravity-mass, chem-human-earth-systems.
- **What is wrong:** s8-gravity-mass works from tables of mass, distance and period with no math lean;
  chem-human-earth-systems uses pH, a log scale, with none. (43 rows have an empty cross_subject; most need none.)
- **Fix:** s8-gravity-mass cross_subject add `7.RP.A.2; 8.SP.A.1`. chem-human-earth-systems add `HSF-LE.A.4` or the
  nearest exponent code in the math standards file (no high school math progression yet, so check later).
- **LAYER:** progression. **REPEAT:** yes. **Confidence:** likely.

### 13. HS-ESS3-1 departure note undersells its own support

- **Skill id:** the Chemistry row owning HS-ESS3-1.
- **What is wrong:** the note says "not Biology as Appendix K places it". Appendix K Table 6 places HS-ESS3-1 in
  Biology and repeats it in Chemistry, so the move has direct support.
- **Fix:** notes: "Appendix K places it in Biology and repeats it in Chemistry; owned in Chemistry with the other
  resource and hazard expectations".
- **LAYER:** progression. **REPEAT:** new. **Confidence:** firm.

## Settled by the expert

| Question | Settled | Why |
|---|---|---|
| No grade 12 core course | Accept | Appendix K Course Map 3 covers the band in three courses; every HS expectation is owned. |
| HS-PS2-6 in Chemistry, not Physics | Accept | Molecular material design sits with bonding and forces between particles; reason given in the row. |
| HS-ESS2-2 in Chemistry | Accept | Feedback in Earth systems goes with the climate rows there; reason holds. |
| HS-ESS1-5 and HS-ESS1-6 in Physics | Accept | Appendix K repeats ESS1-5 in Physics; plate motion and early Earth evidence sit with radioactive dating (HS-PS1-8 is in Chemistry, but the decay math is used in Physics too). Stated in the rows. |
| MS-PS4-2 owned in grade 6 though OpenSciEd completes it in 8.2 and 8.4 | Accept, add note | Grade 6 assesses only light reflection, absorption and transmission; s8-earth-sun-moon and s8-wave-amplitude-energy assess the rest. Add that sentence to s6-light-paths. |
| MS-ETS1 split 1 and 4 in grade 7, 2 and 3 in grade 8 | Accept | Matches where OpenSciEd does the full design work. |
| 3-5-ETS1 split one per grade | Accept | Matches the reconcile (difference 4) and the one-owner rule. |
| Age of the Earth, evolution, climate change | Accept as written | Taught as the evidence shows (BASELINE rule 5); no softening found. |
| Grade 8 and Biology row counts | Accept | Ownership count, not time (finding 10). |
| Practice-only links (finding 6) | Note, not delete | Keep, mark as practice links. |

## For Cory

- **Biology before Chemistry.** HS-LS1-5, HS-LS1-6 and HS-LS1-7 lean on bond ideas a year before Chemistry; the rows
  keep bond energy qualitative, which works. This is Appendix K's order and I agree, but it has that cost.
- **No grade 12 core course.** Confirm it stands. docs/RUBRIC-SCIENCE.md still says Physics is not core; that line
  should change to match the three-course plan.
- **A working science teacher's read** is still owed (FOUNDATION 7.3). Already on file; listed only so it is not lost.

## Lens checklist (progression layer)

| Line | Mark | Note |
|---|---|---|
| A core idea owned by two grades at the same depth | met | Each expectation has one owner; shared OpenSciEd expectations are split by element with notes. |
| A handoff that skips a band (K-2 to 3-5 to MS) | met | Skips are structural to NGSS and explained (finding 7 is about where). |
| A grade assumes a model no earlier grade builds | met for model columns; missed for assumes | No model used before its grade; findings 1 to 3 for prerequisites. |
| A practice that grows in no grade | met | Planning, modelling, data and argument grow across notes and model columns. |
| A crosscutting concept listed everywhere, developed nowhere | met | patterns, cause-effect, scale-proportion, system-model, stability-change, structure-function each introduced once and reused. |
| Clarifications and boundaries carried into rows | met, one miss | Finding 4. |
| Coverage of every expectation | met | 208 of 208, no doubles, none in a wrong grade or band. |
| cross_subject leans name a skill owned at or before the grade | met | Math, ELA and social studies ids all exist and are on time; high school math not checkable. |
| No "NGSS" or endorsement claims in student copy | not applicable | No student copy at this layer. |
| Course frame, scope and sequence, unit and day lines | not applicable | Not this layer. |

## What is right and should not be touched

- Coverage and ownership: every expectation once, in its grade or band; the engineering owners placed once each.
- The grades 6 to 8 split matches OpenSciEd's unit expectation lists, including the multi-unit expectations
  (MS-PS4-2, MS-LS1-8, MS-LS1-2, MS-LS1-3, MS-LS1-4, MS-LS1-5, MS-PS1-1, MS-PS1-2, MS-PS1-4, MS-ESS3-3).
- Boundaries are carried into rows almost everywhere (spot checked across K-5 and all MS and HS rows opened),
  including MS-PS4-1 leaving out electromagnetic waves and the passive solar heater kept in 4-PS3-4.
- The HS-ESS placements follow Appendix K Table 6, with reasons on every departure.
- assumes and hands_on are symmetric; every assume points to an earlier grade; no missing ids.
- Model order: every model introduced at or before its first use (cause-effect, claim-evidence-reasoning,
  data-graph, design-cycle, patterns and system-model in K; structure-function 1; stability-change 2;
  force-diagram 3; energy-transfer, wave-model and light-ray 4; particle-model, scale-proportion, earth-sun-moon,
  matter-cycle and food-web 5; water-cycle, rock-cycle and plate-model 6; field-model 8; computational-model 9;
  periodic-table 10).
- Safety teacher notes throughout; evolution, deep time and climate taught plainly.

## What I could not judge

- High school math leans: there is no high school math progression to check them against.
- OpenSciEd teacher editions inside the full unit zips; I used the unit pages and the scope and sequence PDF only.
- Teaching order inside a grade (no column holds it; finding 9).
- Practice and crosscutting concept elements by grade: there is no data file for them, so only the model columns
  were checked.

## Sources

- NGSS DCI arrangement, AllDCI.pdf (Achieve, 2017): https://www.nextgenscience.org/sites/default/files/AllDCI.pdf
- NGSS Appendix K, Model Course Mapping in Middle and High School (revised 8.30.13), Table 6 p. 28:
  https://www.nextgenscience.org/sites/default/files/Appendix%20K_Revised%208.30.13.pdf
- OpenSciEd middle school Scope and Sequence, Tables A.1 to A.3, and unit pages: https://www.openscied.org/
  (local copy S:\CurioClass-sources\openscied-ms)

## For the source list

- NGSS Appendix K (URL above): add to docs/APPROACH-SOURCES.md if it is not there; it is the basis for the three
  course high school map.
