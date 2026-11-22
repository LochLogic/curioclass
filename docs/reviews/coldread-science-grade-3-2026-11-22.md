# Cold read, science-grade-3, course finish (2026-11-22)

Reader: a fresh reader who did not write the course. Read-only pass; this file is the only thing edited.
Read: AGENTS.md, all of docs/RUBRIC-SCIENCE.md, the pass rule in docs/ADOPTION-BAR-SUBJECTS.md, the whole scope and sequence and its coverage table, three whole units (2, 4, 5: unit plan, section plans, every day file and cards), ten standards traced to lesson set and check item. Units 1, 3 and 6 were read only through the scope and sequence, the days.csv rows and the unit plans' seams, not day by day.

## Verdict

**Would it pass today: no, but it is close.** Three things stop it.

1. **Unit 2 is rated 7 on EQuIP** (needs 8 or 9 in every sampled unit). Units 4 and 5 are 8. The unit 2 shortfall is local: a static idea that rests on one case, a day 29 labeled Fluency that carries new work, and living-record routines for unit 3 crowding magnet days.
2. **Gateway 3 is estimated at 14 to 15 of 18** against a pass line of 16, with 3h not at full marks until the unit 2 demonstration wording is tightened. The three known gaps (below) are most of the shortfall.
3. **S10 (a door) cannot be cleared on unit 5's anchor.** The Svalbard anchor mixes facts from two different geologic ages (ferns and palms, "near the equator", trunks "preserved where they grew"). I could not open sources.csv under this job's limits, so this is flagged for the lead to check against the source row. Until it is checked the door stays open.

A fourth issue is not a rubric fail but is the most serious design finding: **no unit records what a child can do alone on a fresh case.** The scored points come from an earlier product revised after written feedback, and the 32-minute fresh check days (95, 96, and the matching days in units 2 and 4) are diagnostic and score nothing. The same pattern also puts a very heavy scoring and feedback load on the teacher (findings 2 and 3).

Gate: `plan.py check` for science-grade-3 prints "sequence 0 failure(s)" and "874 items and 624 wrong answers checked, 21 failure(s)". All 21 are the same line: "section N.M (science-grade-3-uNN-M) is not in data/units.csv" (finding 7). The remaining lines are notes (errors resting on memory, prose word counts).

## Scores

### Gateways (estimates; the rubric says every answer is a plan until classroom use)

| Gateway | Estimate | Pass line | Basis |
|---|---|---|---|
| 1 (phenomena 1a to 1e, three dimensions 1f to 1k) | 30 of 34 | 29 | Anchors drive every sampled unit through the question board and model revisions (s05.md section 2; d082 hook; d087, d093). Held back at 1i and 1j: end-of-unit "assessments" score no fresh work (finding 2). |
| 2 (scope 2a to 2c, accuracy 2d, band 2e, connections 2f to 2h) | 30 of 34, 2d provisional | 29, with 2d and 2e full | Coverage table traces all 16 expectations (scope-and-sequence.md lines 99 to 118). 2e looks full (limits are named and kept: no species names, no dates, no mechanism). 2d is open on the Svalbard facts (finding 1). |
| 3 (supports) | 14 to 15 of 18 | 16, 3h full | Strong day files (Safety and set-up, Words and supports, Other rooms, At home). Short by the three known gaps and a heavy scoring load (3g). 3h short only by one wording point (finding 12). |

Cannot judge from a plan: 3l to 3u (reported in words), classroom use claims, readability of science texts at grade level, whether the sources rows hold (I did not open sources.csv), and the 3k extension quality beyond the "Longer" lines on each day.

### EQuIP for the three sampled units

| Unit | I Three-dimensional design | II Instructional supports | III Monitoring progress | Total | Rating |
|---|---|---|---|---|---|
| 2 Pushes and pulls without touching (days 17 to 33) | 3 | 2 | 2 | 7 | One if improved; fix before the course is called finished |
| 4 Living in groups and habitats (days 59 to 78) | 3 | 3 | 2 | 8 | Model |
| 5 Environments change (days 82 to 97) | 3 | 3 | 2 | 8 | Model |

Category III is a 2 in all three for the same reason: checks are formative and well built, but the unit-end score rests on a revised, feedback-shaped product and the fresh check is unscored; and the teacher scoring load is unrealistic as written (findings 2 and 3). It is not below 2 anywhere.

### Rows S1 to S13

| Row | Result | Evidence |
|---|---|---|
| S1 storyline | Pass | Unit 5: anchor drives to day 93 (s05.md "Carried" paragraph, d082 hook, d093 "One wall"); question board sorted into past evidence, changed needs, useful responses (u05-1.md section 5). The anchor is not given away: captions hidden (d082). |
| S2 three dimensions in lessons | Pass | Each section plan names elements (s05.md three-dimension table, lines after "Three dimensions of each performance expectation"); days use practice and idea together (d083 solid and dotted lines; d089 merit argument). |
| S3 three dimensions in assessment | Pass | Scored points need a practice with an idea on a case new at production (s05.md "All 12 scored points require a practice with an idea on a case new at production: 100 percent"). Pass on the letter; see finding 2 on the spirit. |
| S4 models revised | Pass | Past-environment model drawn d082, revised d83, d84, d85, d86, d93; system model d87, d90, d91, d94; end task uses both (d93, d94). |
| S5 safe hands-on (door) | Pass, one local wording fix | Weather days carry hazards with controls (d085 Safety and set-up; thermometer non-glass, adult empties jar). Unit 2 day 24 teacher demonstration covers cell, wire, goggles (d024.md line 21); one gap in finding 12. |
| S6 low cost | Pass | Unit 5 states a $25 class budget and a room-with-nothing path on every day; fossil work is photographs and cards only. |
| S7 right source | Pass for K-5 | Every day carries "credit: ours". I did not open the sources file. |
| S8 credit lines | Pass | "credit: ours" on every day read; "Ours, all of it." in each Credit section. |
| S9 checks the teacher can act on | Pass | Each section ends in an exit ticket with answer and wrong answers by letter (u05-1.md section 3); the end-of-unit items have Meets and Does-not samples (s05.md "Meets:" and "Does not:"); next steps are on day 97. Load and timing are findings 2 and 3. |
| S10 accurate and in band (door) | **Part pass, not cleared** | Svalbard anchor (finding 1). Everything else in unit 5 I checked is correct and kept inside the band (extinct means gone everywhere, deeper is older only in undisturbed layers, size alone cannot give a climate, no mechanism taught). |
| S11 every standard traced | Pass | Ten traced below. Gap in spaced checks (finding 5), not in coverage. |
| S12 math and ELA in step | Pass | Whole-number counts and tokens only; the unit plan states "no percentages, averages" (s05.md section 3). RI.3.7 and RI.3.8 are named as taught before (cross-subject rows). |
| S13 engineering as design | Pass | Unit 2 defines needs, criteria and limits for the latch problem (d025 to d030, 3-PS2-4, 3-5-ETS1-1); unit 5 judges solutions against goals and limits with token budgets (d088 to d092, d096). |

Part passes: one (S10). Fails: none. The pass rule allows two part passes; with S10 cleared the course meets rule 5.

### Ten standards traced (coverage table to teaching days to check item)

| Standard | Teaching days | End item (days.csv / items.csv) | Holds |
|---|---|---|---|
| 3-PS2-1 | 1 to 8, 13 | Day 15 items: plan, conduct, explain, plus three more | Yes; course check day 34 returns to it |
| 3-PS2-3 | 17 to 24, 29 | Day 31 items: ask, explain, ask, plus four more | Yes; course check day 35 |
| 3-PS2-4 | 25 to 30 | Day 32 item: name, plus two more | Yes; only repaired on day 36, no course check item |
| 3-5-ETS1-1 | 25 to 30 | Day 32 items: define, limits, plus four more | Yes; same note |
| 3-LS2-1 | 59 to 63, 74 | Day 76 items: food, protect, change, jobs | Yes; course check day 80 |
| 3-LS4-2 | 64 to 68, 74 | Day 75 items: survive, mates, young, model | Yes; **no course check** (finding 5) |
| 3-LS4-3 | 69 to 74 | Day 77 items: well, poorly, cannot, links | Yes; **no course check** (finding 5) |
| 3-LS4-1 | 82 to 86, 93 to 94 | Day 95 items: lake, places, size, order, extinct, revise | Yes; course check day 118 |
| 3-LS4-4 | 83, 87 to 94 | Day 96 items: water, results, arrows, goals, costs, limit | Yes; course check day 118 |
| 3-ESS2-1 | Log throughout, 98 to 102, 107, 113 to 114 | Day 115 items: temps, wetwind, bars, scale, compare, likely | Yes; course check day 119 |

## Coherence across units

- **Models carry.** The design cycle (unit 2 criteria and limits) returns in unit 5 days 88 to 92 and unit 6 day 108 on (s05.md "Carried" paragraph; days 88, 89, 91). Claim, evidence, reasoning moves from unit 3 through unit 4 into unit 5 (d089 frame). The system model drawn in unit 4 is retaped and revised on days 87 and 90. The weather log runs through units 5 and 6, and day 97 explicitly retrieves a dated wind row for day 98.
- **Seams hand off.** Unit 4 to 5 runs through the course check days 79 to 81 and the day 81 readiness item (d081 Tomorrow, lines 69 to 71). Unit 5 to 6 runs through d097 (wind row, goal against limit). Unit 2 to 3 carries a living record into the magnet days.
- **Weak points.** (a) s05.md section 3 still says "No last-day file or Tomorrow line exists" while d081 now has one (finding 8). (b) Units 2 and 4 contain a design cycle that depends on feedback the teacher writes after class, so any late return breaks the revision day (finding 3). (c) Spaced retrieval skips two standards (finding 5).
- **Progression of difficulty.** Solution judging steps up cleanly: one-count goals (d088), count and budget (d089), two counts and two limits (d091, d096). Evidence reading steps up from one find (d082) to layers and extinction (d085) to a region (d086) to a fresh site (d095).

## Known gaps (named already by the rubric; not counted below)

- No APPROACH-SCIENCE.md for the course (3e).
- No family note for the course (the per-section family.md files exist, but the course-level note is missing).
- No course supplies list (3f); costs are stated per unit only.

## Findings, most serious first

| # | Where | Rubric row | What is wrong | Exact fix | Stage |
|---|---|---|---|---|---|
| 1 | s05.md anchor lines (frame field, line 31 region); u05-1.md section 1 "What the teacher page must explain" item (1); u05-1.md header; d082 hook table rows (fern print, palm leaf print) | S10, 2d | The anchor names "ferns and palms" and says the trunks grew "near the equator" as the land moved, and that the trees were "preserved where they grew". Fern and palm finds, equatorial position and in-place trunks belong to different times and sites on Svalbard; they cannot all be one story. I did not open the source row. | Open the sources.csv row for the anchor and rewrite the anchor, the u05-1 teacher note and d082's find table to one source's account (kinds, age, place). If the source gives equatorial coal-age trunks, drop "palm" and any warm-climate wording; if it gives a warm high-latitude forest, drop "near the equator". Keep "no mechanism taught". Keep the swap-in line for a state fossil. | unit plan, section plan, day |
| 2 | s05.md assessment paragraph "Assessment products and scoring" (and the same design in s02.md lines 121 to 129 and s04.md lines 104 to 109); d095.md line 31 and d096.md line 31 | 1i, 1j, EQuIP III, S9 | The only scored points are earlier products revised after written feedback, scored outside class. The 32-minute fresh check days (95, 96) are "not scored", so the course never records what a child can do alone on a case never met. A child who gets the feedback question right in revision earns the same points as one who could not start. | Score the day 95 and 96 fresh work on the same six-point sheets (12 points) and keep the product F and S revisions as repair evidence, recorded beside them. In s05.md, s02.md and s04.md replace "Only the revised earlier products are scored" with "Fresh work on the check day is scored; revised products show repair". Change each day's "not scored" line and score-sheet.md heading to match. | scope, unit plan, section plan, day |
| 3 | d086.md ("Plan 3 minutes a child after class"), d091.md (same), d097.md lines 18 and 28 | 3g, EQuIP III | The teacher writes feedback on two products (3 minutes a child each, 75 to 90 minutes for 25 to 30 children each time) and scores 12 points across all papers, with fresh-day papers and scores due back in the first five minutes of day 97, one school day after day 96. That is not doable as written. | Cut feedback to one look-for checklist (six ticks) and one question stamp, 1 minute a child. On day 97 hand back checklists and exit tickets only; hand back scored fresh papers on day 98 as part of the Return slot. Make the same change in units 2 and 4 return days (33, 78 to 81). | section plan, day |
| 4 | days.csv line 30 (day 29, kind Fluency, codes 3-PS2-3, 3-PS2-4, 3-5-ETS1-1); d029.md | Unit 2 EQuIP II; day kinds | A day labeled Fluency carries new work: the consensus model joins static, magnet and latch evidence for the first time with eight sort cards and a gap card. | Relabel day 29 as Application in days.csv and the day 29 front matter, and move the gap-card sort to day 28 or add a named retrieval slot. | data, day |
| 5 | scope-and-sequence.md lines 140 to 148 (course checks 1 to 3) | S11, EQuIP III | No course check returns to 3-LS4-2 or 3-LS4-3 (unit 4's survival and habitat standards); 3-PS2-4 and 3-5-ETS1-1 get only a respond day (36). Unit 6 standards are reached at the end only. | Add one item each for 3-LS4-2 and 3-LS4-3 to course check 2 (days 79 to 80) or to check 3 (day 118 to 119), and one 3-PS2-4 problem-definition item to day 34 or 35. Update the check table and days.csv codes. | scope, data |
| 6 | s05.md section 6 error register (rows A to F, source "Anticipated, from memory"); same in s01, s02, s03 (plan.py notes "error ... rests on a memory, not a source") | Core: errors from evidence | Every error in the register is a guess. Day 97's four groups and every Return and repair slot are built on those letters. | Mark each letter "watch list" in the plan text; make day 97 grouping pick by the child's own marked component (already the case) and keep the letters as hints only. Replace "Anticipated" rows with one source row each where a source exists (a standards-progression page or a published misconception study) or leave them labeled as watch list. | unit plan |
| 7 | data/units.csv (21 sections absent) | Gate | plan.py check prints 21 FAIL lines: sections 1.1 to 6.4 are not in data/units.csv. | Add 21 rows to data/units.csv (full ids science-grade-3-u01-1 through science-grade-3-u06-4), matching each section plan's days and title. Read the whole file first and append; re-run the filtered gate. | data |
| 8 | s05.md section 3 ("No last-day file or Tomorrow line exists") | EQuIP I, seams | Stale: d081.md lines 69 to 71 now carry a Tomorrow line to day 82. | Delete that sentence; say the day 81 Tomorrow line hands over to day 82. | unit plan |
| 9 | Student cards and plan text in units 1 to 5 (34 files in courses/science-grade-3 with "centimetre"; 11 plan files; for example u05-1/product-f-card.md lines 21 and 25, s05.md lines 126, 128, 157); d096 uses "50 centimeter" | US spelling rule | UK spelling throughout, mixed with US spelling in 33 files. | Replace "centimetre(s)" with "centimeter(s)" in those files; rerun the filtered gate for spelling. | scope, section plan, data, day |
| 10 | d083.md "Support groups" (10 minutes) and days.csv day 83 (codes 3-LS4-1 and 3-LS4-4) | Day plan fit | A kindergarten reteach for the readiness item takes 10 of 45 minutes on a day coded to the fossil standard and to 3-LS4-4, a standard first taught on day 87. The class that all passed still spends the day around it. | Move the readiness reteach to a day 81 Respond slot (the day already holds readiness) or keep 10 minutes only for the group that missed and give everyone else the extra fossil card for the full time. Drop 3-LS4-4 from day 83's codes. | day, data |
| 11 | s02.md line 125 (static cards) and u02-1 days 17 to 20 | 3-PS2-3, EQuIP II | Static interaction rests on one case (rubbed plastic and paper), so the idea may be taken as a one-example trick. | Add a second static case with a different pair of objects to one of days 19 to 21 and put it in day 31's item stem. | section plan, day |
| 12 | d024.md materials line 6 and Safety and set-up line 21 | S5, 3h | The materials list a switch in the circuit; the safety text covers taped wire ends, no shorting and stopping if the wire warms, but never says the switch stays off until the class is ready, who closes it, or that the nail and wire stay untouched until they cool. | Add: the teacher alone closes the switch for the count of 10, opens it, and waits for the nail to cool before it is handed or touched. | day |
| 13 | d097.md "Four six-minute groups" (24 minutes) | S9 next step | Four groups of 6 minutes means one revision each for up to 7 children and a pair task for everyone else; repair of two or three components per child is not possible in the time. | Make day 97 a 15-minute group on the one component marked plus 9 minutes of repair-sheet work per child, and say day 98's Return slot finishes the second component. | section plan, day |
| 14 | u02-2 day 24 materials (labeled class plants and pots, enclosed mealworm habitat, living record) | EQuIP II unit 2 | Unit 3's living-record routine starts inside unit 2's magnet days, adding set-up and observation work to a day that already runs a demonstration. | Move the living-record start to a one-sheet 3-minute routine (not a demonstration-day task) or start it on day 36. | section plan, day |
| 15 | d093.md line 17 ("Make 30 wall cards, one a child") | Day plan fit | Fixed to a class of 30. | Write "one card a child plus 6 blanks"; state the counts per card type as a share of the class. | day |

## Notes for the lead

- Browser check: none arose (this job edits no sources).
- Stray folders: none seen.
- Not read: unit 1, unit 3 and unit 6 day files, sources.csv, the other course checks' items, the course-level teacher pages.

## Fixes applied (2026-11-22)

1. Applied: checked G42 (opened 2026-11-22): about 380 million years old, mainly lycopod trees, stumps preserved in place, Svalbard on the equator then. "Near the equator" and "where they grew" are supported and kept; "ferns and palms" and the fern and palm rows in u05-1.md were not, and are changed. No day file printed ferns or palms. G42 row updated.
2. Left for Cory (scoring design), with options in the finish-fix report.
3. Left for Cory (feedback load), with options.
4. Applied: days.csv day 29 kind is now Application. The gap-card sort was not moved.
5. Left: scope and data stage (course check items), for the lead.
6. Left: unit plan stage (error register).
7. Left: data/units.csv is outside this job (known gap).
8. Left: unit plan stage (the s05.md stale sentence), for the lead.
9. Applied: Part E spelling pass in the course folder and items.csv; plan docs outside them left.
10. Applied: days.csv day 83 drops 3-LS4-4. The reteach already runs only for the readiness group.
11. Left: a second static case touches days 19 to 21 and day 31, all at their word caps; section plan stage. Days 23 (balloon) and 29 (rubbed straw) already give other pairs.
12. Applied by the safety fix to d024.
13. Left: the d097 grouping is a section-plan routine shared with day 98 (unit 6).
14. Left: section plan stage (living records start in unit 2).
15. Applied: d093 "one wall card a child plus 6 blanks; for 24 children".
