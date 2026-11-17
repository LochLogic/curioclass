# Frame fixes: earth-and-space-science (Earth and Space Science), 2026-11-16

This is the writer's fix pass on docs/reviews/frame-earth-and-space-science-2026-11-16.md (the expert's cold read, 14 findings, and its "Settled by the expert" table). It also applies the coordinator's decisions of 2026-11-16:
- The outcome set widens, adding volcanic hazards and tropical cyclones, with no added days. Cory may still reverse this.
- The seams with Environmental Science are made explicit.
- The Physics frame and data/courses.csv are not edited; each goes under For the lead with its exact replacement text.

Files changed:
- docs/courses/earth-and-space-science/frame.md
- the ess- rows of data/progressions/science.csv (standard and notes only; no assumes or hands_on changed)
- data/standards/curio-science-electives.txt, now version 2
- the sync outputs: data/plans/frames.csv, data/plans/calendar.csv and the table in docs/courses/CALENDAR.md

Counts: all 14 findings and all 7 settled items applied. Two findings are applied as For the lead items rather than as edits, because the files they touch are outside this writer's edit list: finding 13 (the Physics frame) and the grade part of For Cory 1 (data/courses.csv).

## Gates (run after the last edit)

| Gate | Result |
|---|---|
| `python -X utf8 scripts/progression.py check science` | 237 rows, 0 failures |
| `python -X utf8 scripts/frame.py check earth-and-space-science` | 0 failures; 9 units, 160 days (149 in units, 11 for checks and respond days) |
| `python -X utf8 scripts/frame.py check environmental-science` | 0 failures; 9 units, 160 days |
| `python -X utf8 scripts/stale.py check` | 62 files, 0 failures |
| `python -X utf8 scripts/frame.py sync` | frames.csv 58 courses; calendar.csv 782 rows |
| Scratchpad self-check | 19 ess- rows each placed once; CUR-ESS.1 to 26 each owned by a row and placed in one unit; 149 + 11 = 160 days |
| Grep of the frame | no em dashes, no "Curio" without "Class", no exam-programme names |

## Findings

| # | Finding | What was done |
|---|---|---|
| 1 | The one-layer greenhouse cannot explain Venus | **Row ess-planetary-climates.** The boundary now gives the layered greenhouse in the settled wording: the single-layer model first, its failure for Venus found, then the number of layers fitted as the unknown (the fourth root of n plus 1).<br>**Unit 8.** The cell says the one-layer model works for Earth and Mars, fails for Venus by more than 400 degrees, and that students find how many layers Venus's 90-bar air acts like. The paper path gains a number-of-layers column.<br>**CUR-ESS.22** (formerly .20) adds "tested against measurements and revised where it fails". |
| 2 | Source map and unit 4 re-teach earlier courses | **Source map, retrieval only:**<br>- Physical Geology 19.1 and 19.2: one reading recalling Chemistry unit 9<br>- Physical Geology 5.6: one reading recalling Chemistry unit 9<br>- Physical Geology 10.4: recalls grade 6 and Physics unit 9 (the locked boundary is in 12.1)<br>- Astronomy 4.5 and 4.7: recall grade 8, then observed<br>- Astronomy 9.3: recalls Physics unit 10<br>- JetStream 14: warning and preparedness recall grade 6 and are used only for the town advice<br>**Source map, left out:** Physical Geology 19.3 (Chemistry units 9 and 11); Astronomy 8.4 (Biology unit 8).<br>**Unit 4.** The stream table now measures runoff timing and discharge from a paved and a vegetated surface (a hydrograph). Erosion and deposition are Chemistry unit 3's, recalled, not re-run (cell and row ess-streams-floods).<br>**Unit 7.** The cell says Chemistry unit 9's timescales, human cause and forecast are recalled in one reading. |
| 3 | Unit 4's anchor cannot be answered from its evidence | The question is now the settled one: "how rare were they, and how much did the built-over upland add?"<br>The cell names three sources:<br>- the federal rainfall atlas's precipitation-frequency estimates<br>- the county's hydrology study<br>- the Patapsco River gauge<br>Each is checked before the scope and sequence (For the lead 7). |
| 4 | Safety: two units missing, rule gaps | Units 2 and 7 are added to the safety read; every unit is now read.<br>New course rules:<br>- mineral sets hold no asbestiform, lead, mercury, arsenic or radioactive specimens, with handwashing<br>- road cuts from photographs only<br>- stream work never after rain, with gloves, cuts covered and handwashing<br>- pairs inside a group with an adult<br>- the cloud bottle is squeezed by hand, with no alcohol or pump<br>- lamps are incandescent clamp lamps of 60 watts or less, never halogen<br>- night observing at home or at a school evening event<br>Cells changed: units 1, 2, 4, 5, 8 and 9. Rows changed: ess-topographic-maps, ess-rocks-minerals, ess-relative-dating, ess-streams-floods and ess-atmosphere-moisture. |
| 5 | Native nations sources named for unit 3 only | **Unit 1.** Sensitivity reads names a published place-name source and the W8banaki Nation's (Odanak and Wôlinak) own material. The cell says the name is from an Algonquian language, usually given as Abenaki, that its meaning is uncertain, and takes no side.<br>**Unit 3.** Names the Quinault Indian Nation's and Chehalis Tribe's published material for the Copalis River homeland, in one line, checked before writing.<br>**Unit 9.** No nation's star knowledge is used. |
| 6 | Days do not follow load | Unit 1 goes to 18 days and unit 8 to 14, as settled. Weeks are recomputed in the units table, the checks and Cross-subject:<br>- unit 3: weeks 7 to 11<br>- unit 4: weeks 11 to 15<br>- unit 5: weeks 15 to 18<br>- unit 7: weeks 22 to 25<br>- check 1: week 11<br>The Days sentence is rewritten from the counts. |
| 7 | No volcano or severe storm outcome | Coordinator's decision: widen. Two outcomes are added, with no added days, and CUR-ESS is renumbered in teaching order to 1 to 26:<br>- new CUR-ESS.11, volcanic hazard: unit 3, row ess-cascadia-hazard, Mount St. Helens 1980<br>- new CUR-ESS.16, tropical cyclones: unit 5, row ess-atmosphere-moisture, archived advisories<br>Source map: Physical Geology 4.4 and 4.5 placed in unit 3; JetStream tropical cyclones and Webb 8.4 in unit 5.<br>Check 2 and check 3 sample the new outcomes. For the lead 3 records how to reverse it. |
| 8 | Anchor wording | Unit 1: "a hard, quartz-rich metamorphic rock that wears down more slowly than the rock around it".<br>Unit 2: "gently tilted".<br>Unit 5: "up to about 2 metres".<br>Unit 6: the 1972 case is read from ship, coastal and catch records; the buoy array serves the later El Niños. |
| 9 | Two outcomes claim more than their method gives | CUR-ESS.25 (formerly .23): size and stage of life, plus the mass of a main-sequence star.<br>Row ess-stars-exoplanets boundary: the star's mass is supplied; a cubed equals mass times period squared.<br>The unit 9 cell matches. |
| 10 | Source map housekeeping | Each section now has a first-use unit, with "returns in unit n" where it is used again: Astronomy 1.4, 5.1 and 5.2, JetStream Energy Balance.<br>Physical Geology 3.2 and 3.3 and Webb ch 12 are written as "left out as student reading: teacher background for unit n". |
| 11 | The Environmental Science seam misses two touches | The Beside section is rewritten as a five-row table: watershed, groundwater, contaminants, inversions, stormwater. Each row names the owning course and unit, how the other course retrieves or skips it, and what a student who takes both meets.<br>Physical Geology 14.4 is left out as Environmental Science unit 5's.<br>The Environmental Science frame carries the same table. |
| 12 | Check set wording | Unit 3 takes "science arguments are strengthened by multiple lines of evidence supporting a single explanation".<br>Unit 7 takes "most scientific knowledge is quite durable, but is, in principle, subject to change...".<br>Unit 5's practice ends "explanations or solutions to determine the merits of arguments". |
| 13 | Stale Physics frame note | Not edited (outside this writer's files). For the lead 2 gives the line and its exact replacement. |
| 14 | Field work and paper path gaps | The sky log starts on unit 8's first day (week 25), with daytime Moon observations allowed (units 8 and 9, row ess-sky-observation).<br>The live forecast uses the teacher's printed map and sounding, or an archived situation (unit 5, row ess-weather-maps-forecast).<br>A protractor-and-string clinometer is added to the materials and to row ess-topographic-maps' boundary. |

## For Cory items

- **1 (grade).** Under For the lead 1, with the exact row: `earth-space,science,Earth and Space Science,12,12,n,Follows Physics and Algebra II`.
- **2 (added outcomes).** Applied on the coordinator's decision; For the lead 3 keeps it open for Cory.

## Not applied

None.

## Unit-level lessons pass (2026-11-16)

Lessons 17 to 32 of docs/pipeline/briefs/frame-write.md ("Lessons from below the frame"), evidence in docs/reviews/frame-unit-lessons-2026-11-16.md. No unit, skill placement, day total or owned standard changed.

- **Day kinds.** New bullet: Fluency here means short map, section, lag-time, decay, sounding and light-curve sets on new data, about one a unit, none scored.
- **Readiness.** Seams rows now give the course, grade, unit and last day of each row's last use, counted from the core courses' days.csv as the scope gate counts it (one hop included); the count starts from grade 12 and the scope gate's count governs. Every verdict in the first draft held.
- **End-of-unit evidence.** New section "Unit by unit: evidence, tools, writing, data and costs" (before Course-level checks): each unit's end-of-unit evidence inside its days, products with draft, written feedback and revision before the score, at most one full performance per end day.
- **Checks name what they sample.** Check 1 samples units 1 and 2 (unit 3 returns in check 2; the unit 3 Why cell says so); check 2 units 3 to 5; check 3 units 6 to 8 plus one item each from units 3 and 4. Each names its task forms and what is reused unscored.
- **Minutes.** The Days bullet says set-up, clean-up and collection come out of the 50 minutes; each lab or field unit names its clean-up time.
- **Safety.** The Safety read bullet names its guides by title with a free link (never a student form); the last Units column gives each hands-on or field unit's hazards and controls as a "Safety (days.csv words)" sentence.
- **Facts and data.** Every named figure and data set has a free source and an "as of" where it can change.
- **Depth limits.** Each unit's "What students learn" cell gains an "Out:" line.
- **Devices.** New bullet: shared display, devices in pairs, no owned outcome needs technology, scientific calculator per pair.
- **Tools, writing, cost.** Per unit in the new section: key tools by generic name with job and paper path, what Curio Class writes, provisional cost for a class of 30 (about $915 a year).
- **Literacy.** Side codes relabelled "Practised, not owned" in all 9 units; none is claimed in full.
- **Sensitivity.** Unit 6 names Peru's own marine research institute and fishing communities' published accounts; unit 8 has no community content.
- **Source map.** New paragraph on how sections become days (lesson 27). Standard bullet: "Deepens" lines are review, checked by the owning core course.
- **Grade 12 calendar.** New bullet: unit 9 in weeks 28 to 31, check 3 in week 32, fold order for up to 5 days, nothing folded from feedback, revision or end sittings.
- **Leans.** The frame leans on core courses only (unchanged).

Gates: progression science 0 failures; frame earth-and-space-science 0 failures (160 days); stale 62 files, 0 failures; frame sync run (58 courses, 782 calendar rows); no em dash, "AP" or "College Board"; "Curio" appears only as "Curio Class" or in paths.

New For the lead: 10 cost ceiling (pick: $1,000 a year for a class of 30, reusable kit shared with Environmental Science, a cheaper route named for any unit over $150); 11 safety guide links not opened in this pass (pick: the safety agent opens each before its read).
