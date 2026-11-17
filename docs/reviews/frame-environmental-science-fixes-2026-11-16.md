# Frame fixes: environmental-science (Environmental Science), 2026-11-16

The writer's fix pass on docs/reviews/frame-environmental-science-2026-11-16.md (the expert's cold read, 13 findings, and its "Settled by the expert" table), with the coordinator's decisions of 2026-11-16:
- The outcomes widen: CUR-ENV.7, 10 and 11, with no added days. Cory may still reverse this.
- The seams with Earth and Space Science are made explicit.
- Unit 5's uranium chemistry is corrected and its sensitivity sources are widened.

Files changed:
- docs/courses/environmental-science/frame.md
- the env- rows of data/progressions/science.csv (standard and notes only; no assumes or hands_on changed)
- data/standards/curio-science-electives.txt, now version 2
- the sync outputs

Counts: all 13 findings and all 6 settled items are applied. The two For Cory items are under For the lead with picks.

## Gates (run after the last edit)

| Gate | Result |
|---|---|
| `python -X utf8 scripts/progression.py check science` | 237 rows, 0 failures |
| `python -X utf8 scripts/frame.py check environmental-science` | 0 failures; 9 units, 160 days (149 in units, 11 for checks and respond days) |
| `python -X utf8 scripts/frame.py check earth-and-space-science` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 62 files, 0 failures |
| `python -X utf8 scripts/frame.py sync` | frames.csv 58 courses; calendar.csv 782 rows |
| Scratchpad self-check | 20 env- rows each placed once; CUR-ENV.1 to 21 each owned and placed; 149 + 11 = 160 days |
| Grep of the frame | no em dashes, no "Curio" without "Class", no exam-programme names |

## Findings

| # | Finding | What was done |
|---|---|---|
| 1 | Safety rules contradict an outcome and miss hazards | The expert's option (a) is taken.<br>**Water tests.**<br>- nitrate and pH by strip; turbidity by transparency tube<br>- no liquid or tablet reagents<br>- dissolved oxygen from published monitoring records or a loaned electronic meter<br>These are written into the course rules, the unit 3 cell, CUR-ENV.7's teaching line and row env-water-quality.<br>**New course rules.**<br>- eye protection for every soil, water and leaching activity<br>- long trousers, socks over trouser legs and a tick check<br>- stream animals kept in shaded trays and returned where they were found<br>- stream work never after rain, with cuts covered<br>**Cells and rows.** Unit 1 adds ticks; unit 2 adds eye protection and no hydrogen peroxide; the safety read names ticks and stream animals. Rows env-field-sampling and env-water-quality match. |
| 2 | Outcomes leave out water supply, solid waste, toxicology | Coordinator's decision: widen, with no new unit, row or code (no renumbering).<br>- **CUR-ENV.7** adds where a town's water comes from, and pumping and diversion drawing down groundwater and rivers. The Aral Sea is unit 3's supply case.<br>- **CUR-ENV.10** adds a town's waste (reduce, reuse, recycle, landfill) beside mine waste.<br>- **CUR-ENV.11** adds dose-response and biomagnification. The env-exposure-risk boundary is lifted to "dose-response and biomagnification read from published data; no toxicology models built".<br>Days use the expert's widened split (finding 6). For the lead 3 records how to reverse it. |
| 3 | Uranium harm is mainly chemical in water | **Unit 5 and row env-exposure-risk now match each pathway to its harm:**<br>- uranium in drinking water is a chemical kidney toxin, often with arsenic and other metals<br>- radon and its decay products in air are the radiation (lung) route<br>- DNA change belongs to the radiation route only<br>The ~HS-LS3-2 deepening is kept and marked as limited to the radon route. |
| 4 | Two causal claims given before the evidence | Unit 8's question is the settled one: "does a line drawn on a 1930s lending map still show in today's temperatures?"<br>CUR-ENV.9, the unit 4 cell and row env-energy-transition now weigh rival causes: a carbon price floor, gas prices, plant-emission rules, wind and solar growth, falling demand.<br>Unit 4's check set adds the nature of science element on weighing alternative explanations, and its practice element now ends "...to determine the merits of arguments". |
| 5 | Unit 8 carries an outcome its anchor does not drive; late-winter walk | The question board now reaches air pollution through the anchor ("the hottest blocks also have the most ozone days and the busiest roads").<br>The walk is on a clear, sunny day, surface readings first and air readings second, against the 2017 summer data. "Summer heat walks" becomes "heat walks ... cancelled on dangerous heat days".<br>Unit 8 has 18 days. |
| 6 | Days do not follow load | The widened split is used: 18, 15, 18, 15, 16, 15, 14, 18, 20 (149).<br>Weeks are recomputed:<br>- unit 3: weeks 7 to 11<br>- unit 6: weeks 18 to 20<br>- unit 8: weeks 24 to 27<br>- check 1: week 11<br>Cross-subject weeks match, and each lean keeps its kind. The Days sentence is rewritten from the counts. |
| 7 | Grade 11 taker's social studies leans lack a one-lesson version | If-later lines are added to the seven same-year "Earlier this year" rows:<br>- gov-federalism, units 5 and 9<br>- econ-scarcity-choice, unit 7<br>- gov-policy-debates, unit 8<br>- us2-postwar-domestic, unit 8<br>- econ-government-role, unit 9<br>- gov-local-action, unit 9<br>The closing sentence now excludes World History II (grade 10, an earlier year for any taker). |
| 8 | Source map sections unplaced; wrong transfer case | **Placed:**<br>- chapter 6: 6.1 to 6.3 in unit 5 (exposure, health, toxicology)<br>- chapter 9: 9.1 to 9.5 each in unit 2<br>- 7.5: the unit 3 supply case<br>- 12.1 and 12.2: a town's waste in unit 5<br>- 3.3: marked as one framing reading<br>**Transfer case:** unit 3's is now the Mississippi low-oxygen zone (settled). |
| 9 | Three shared ideas with Earth and Space Science have no line | The Beside section is a five-row table (watershed, groundwater, contaminants, inversions, stormwater). Each row gives the owning course and unit with weeks, the other course's part-lesson, and what a student who takes both meets.<br>Rows env-water-quality, env-mining-legacy, env-air-pollution and env-solution-design carry the matching line.<br>The Earth and Space Science frame carries the same table. |
| 10 | Unit 5's reading list misses the Nation's research rules and naming | **Added to Sensitivity reads, the unit 5 cell and row env-mining-legacy:**<br>- the Navajo Nation Human Research Review Board's public rules<br>- the Nation's uranium commission reports<br>- the 1979 Church Rock tailings spill in the Nation's own accounts<br>- the Native American Journalists Association's guide, by name<br>- "Diné" and "Navajo Nation" used as the Nation does<br>The frame states that only material the Nation has already released publicly is used, with no contact and no class collection of health information. For the lead 2 asks Cory to confirm. |
| 11 | Anchor figures; one wording over-attributes the cause | Unit 2's anchor uses the settled wording: slopes terraced, dammed and replanted, and dams on the river itself.<br>Unit 7 names the north-of-park road surveys as the control.<br>Figures not checked by the expert are listed under For the lead 8. |
| 12 | Two seams not named | Unit 7 names grade 7's judged designs and adds ~HS-ESS3-3 (Biology unit 10) to its deepens list and to row env-conservation-strategies' standard cell. |
| 13 | Small inconsistencies | bio-sources-of-variation: a grade 11 taker now gets a readiness check at the end of unit 4. This is in the Seams row, the unit 5 cell and the row note, and the Seams paragraph's grade 11 sentence is corrected.<br>The heading now reads "grade 7".<br>The Days sentence is rewritten. |

## Settled items

All six are applied:
- the unit 8 question
- the unit 2 anchor
- Simpson's index (unit 1, row env-field-sampling)
- the three-group pollution tolerance index (unit 3, row env-water-quality)
- the Mississippi transfer case
- the clear-day heat walk

## For Cory items

- **1 (scope).** Applied on the coordinator's decision; For the lead 3 keeps it open.
- **2 (people).** Under For the lead 2 with the pick: released material only, no contact, sensitivity read first.

## Not applied

None.

## Unit-level lessons pass (2026-11-16)

Lessons 17 to 32 of docs/pipeline/briefs/frame-write.md ("Lessons from below the frame"), evidence in docs/reviews/frame-unit-lessons-2026-11-16.md. No unit, skill placement, day total or owned standard changed.

- **Day kinds.** New bullet: Fluency here means short index, tolerance-score, grid-record, population-step and exposure sets on new data, about one a unit, none scored.
- **Readiness.** Seams rows now give the course, grade, unit and last day of each row's last use, counted from the core courses' days.csv as the scope gate counts it (one hop included). The count starts from grade 12; for a grade 11 taker from grade 11, with Physics not counted, and each Physics row names its earlier use. Recount results: bio-evaluate-impact-solutions (unit 2) and bio-define-human-impact-problem (unit 7) were last used in Physics unit 2, so both are now retrieval (also for a grade 11 taker, via Chemistry unit 7); the unit 2 and unit 7 Why cells changed to match. s7-human-impact-design and s7-population-consumption were last used in Chemistry, grade 10, not grade 9, and stay readiness checks. bio-sources-of-variation stays the one grade 11 taker readiness check. The scope gate's count governs.
- **End-of-unit evidence.** New section "Unit by unit: evidence, tools, writing, data and costs" (before Course-level checks). Unit 9's field project counts its days: draft, written feedback, two revision lessons, report on one end day, presentations on a second (about seven teams, about six minutes each); units 1, 5 and 8 pair a revised product with a sitting on separate end days.
- **Checks name what they sample.** Check 1 samples units 1 and 2 (unit 3 returns in check 2) and reuses the unit 1 field counts unscored; check 2 units 3 to 5; check 3 units 6 to 8 with one item from unit 1, unit 9 assessed by its field project. CUR-ENV.20 and 21 left check 3 (unit 9's project assesses them).
- **Minutes.** The Days bullet says set-up, clean-up and collection come out of the 50 minutes; each lab or field unit names its clean-up time (5 minutes bench, 10 field or stream).
- **Safety.** The Safety read bullet names its guides by title with a free link (the NSTA position statement, the NIOSH school laboratory guide, the CDC tick and harmful algal bloom pages, the National Weather Service heat and lightning pages, safety data sheets; never a student form). The last Units column gives units 1 to 5 and 7 to 9 a "Safety (days.csv words)" sentence; unit 6 reads "none (data and paper only)".
- **Facts and data.** Every named figure and data set has a free source and an "as of" where it can change.
- **Depth limits.** Each unit's "What students learn" cell gains an "Out:" line.
- **Devices.** New bullet: shared display, devices in pairs, CUR-ENV.12 by a step table, dissolved oxygen from published records where no meter is loaned, calculator per pair.
- **Tools, writing, cost.** Per unit in the new section: key tools by generic name with job and paper path, what Curio Class writes, provisional cost for a class of 30 (about $840 a year).
- **Literacy.** Side codes relabelled "Practised, not owned" in all 9 units.
- **Sensitivity.** Unit 2 (Chinese researchers' studies and the programme's published accounts), unit 7 (the park's and state wildlife agency's removal pages), unit 9 (the town's published plans and meeting records); unit 1 has no community content.
- **Source map.** New paragraph on how sections become days (lesson 27). Standard bullet: "Deepens" lines are review, checked by the owning core course.
- **Grade 12 calendar.** New bullet: unit 9 in weeks 28 to 31, check 3 in week 32, fold order for up to 5 days, never a feedback or revision day, the scored report or the presentation day.
- **Leans.** The frame leans on core courses only (unchanged).

Gates: progression science 0 failures; frame environmental-science 0 failures (160 days); stale 62 files, 0 failures; frame sync run (58 courses, 782 calendar rows); no em dash, "AP" or "College Board"; "Curio" appears only as "Curio Class" or in paths.

New For the lead: 11 cost ceiling (pick: $1,000 a year for a class of 30, reusable kit shared with Earth and Space Science, a cheaper route named for any unit over $150); 12 safety guide links not opened in this pass (pick: the safety agent opens each before its read).
