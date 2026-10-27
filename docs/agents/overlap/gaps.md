# Curio Class overlap pass: gaps

Gaps found while tagging all 586 tools, revised after the cold check (check.md). Each gap lists move-to-gap candidates where a planned tool could be re-pointed without losing coverage: its module's standards are also carried by another tool in the same band (`python scripts/overlap/standards.py` lists these). Live tools are never candidates.

Move-to-gap is rarer than it looks. Most planned modules carry standards no other module carries (the CSTA 2026 grade-level codes, for example, give each grade its own identifiers), so re-pointing them would open a new gap. Every move also needs a new module row, and leaves the old module without a tool unless something else takes it. So most suggestions below are "add the standard to an existing module" or "new module in a later wave". Both are data edits, outside this pass.

No move-to-gap is recommended in this revision. Three are offered as options in clusters.md: boundaries-builder (G6), ph-detective (G2) and population-dashboard (G2).

## G1. Engineering design in K-5

- **What is missing:** no module carries K-2-ETS1 or 3-5-ETS1. MS-ETS1 is on bridge-builder and HS-ETS1 on design-challenge-studio.
- **Why it matters:** NGSS expects every K-5 band to define a problem, compare solutions and test them.
- **Candidates (add the standard, no move):**
  - K-2: shade-builder (K, design a shade that keeps a surface cool) already runs the design and test loop. Add K-2-ETS1-1 to K-2-ETS1-3 to its module.
  - 3-5: rube-goldberg-workshop, retitled Contraption Workshop (C33; g4, 4-PS3-4 is itself a design PE). Add 3-5-ETS1-1 to 3-5-ETS1-3 to its module.

## G2. NGSS performance expectations with no module

The full list, checked against the NGSS PE list: K-2-ETS1 and 3-5-ETS1 (G1), plus these seven.

| PE | What it asks | Candidate |
|---|---|---|
| HS-LS2-5 | carbon cycling among the biosphere, atmosphere, hydrosphere and geosphere | **Add to energy-accountant's module before its wave 1 spec** (W3, recommended). Its ledger already tracks carbon through photosynthesis and respiration. The first draft's move of population-dashboard ("Carbon Relay") is withdrawn: it would have put the same hops beside energy-accountant, needed a new module row, and left science-12-population-and-resources with no tool. |
| HS-LS2-3 | matter and energy in aerobic and anaerobic conditions | Add to energy-accountant's module with HS-LS2-5 (optional). |
| HS-PS3-4 | thermal equilibrium when two components mix | Option, not recommended: move ph-detective (its HS-PS1-2 is also on equation-balancer). "Even Out: Drop hot metal into cold water, mix hot and cold water, and predict the final temperature; watch energy flow until both sides match." 9-12 already has 12 lab settings, and the move needs a new module row. Otherwise a new module in a later wave. |
| HS-ESS2-7 | coevolution of Earth's systems and life | Option: move population-dashboard (its HS-ESS3-1 and HS-LS2-1 are also on island-economy and carrying-capacity). "Living Planet: Scrub through four billion years and watch life and Earth change each other: microbes fill the air with oxygen, plants build soil, reefs build coastlines." Needs a new module row and orphans science-12-population-and-resources. Low priority. |
| MS-PS2-4 | gravity depends on mass | Add to planet-builder's module (g6, a gravity sandbox; a planet-mass slider would carry it). |
| MS-LS1-8 | sense receptors send signals to the brain | No safe candidate in 6-8 science. New module in a later wave. |
| MS-LS4-5 | genetic engineering and artificial selection | Add to the natural selection module (bug-hunt, g8), where artificial selection sits beside natural selection more naturally than in gene-pool's heredity module. |

## G3. CSTA computer science

85 of the 196 CSTA 2026 identifiers in data/standards/csta-2026-ids.txt are on a module; 111 are not (exact match, `python scripts/overlap/standards.py` prints the full grid). The largest holes:

- **Computing and Society (SOC):** K-2 and grades 3-5 are patchy, not empty: E1-SOC-HU-15 (on pattern-finder's module), E4-SOC-HU-18 and E5-SOC-HU are covered. EK and E2 SOC are all uncovered, and grade 5 SOC-CE, SOC-HI and SOC-ET are uncovered. Middle school has 1 of 8 covered; high school has 0 of 9.
- **Data collection (DAT-DC):** 9 uncovered: E1, E2, E3 and E5, 3 of 4 in MS and 2 of 4 in HS.
- **Program development (PRO-PD):** 9 uncovered: one in E3, both in E4, one in E5, 3 of 4 in MS and 2 of 4 in HS.
- **Data inference and models (DAT-IM):** 11 of 12 uncovered (only one HS code is on a module).
- **Impacts of computing systems (SYS-IM):** 8 uncovered: E1 to E5, both MS and one HS.
- **Hardware (SYS-HW):** EK and grades 3-5 uncovered, MS 0 of 2.
- **Testing and refining (PRO-TR, PRO-RD):** PRO-TR is covered K-5 and uncovered in MS and HS (0 of 2 each). PRO-RD's hole is mostly EK to E3 and E5; MS and HS each have 1 of 2.
- **Algorithms and their impacts (ALG-IM):** 7 uncovered.

Candidates (add the standard, no move; CS tools carry unique codes, so none can move):

- **HS-SOC-ET:** data-policy-council's module (computer-science-9-12-ethics-law-and-data-policy) carries HS-ALG-IM-10, HS-DAT-IM-28 and HS-SYS-IM-36 but no SOC code. It is the natural home for the HS ethics codes.
- **EK and E2 SOC:** secret-keeper (K, what is OK to share) or teach-the-robot (g2, training an AI by examples).
- **SYS-HW in 3-5 and MS:** computer-builder (live, g1) and input-output-machine (g2) are the hardware family. Add the 3-5 and MS codes to that family in a later wave rather than stretching one tool across bands.
- **DAT-DC in E1 to E5:** class-snack-vote's reshape (Me vs the Counter, C21) is a K data-collection tool; the grade 1 to 5 codes need their own modules.

The CTE and world-language tools are the only subjects whose standards are fully covered elsewhere, and CTE is already thin (G6), so pulling tools out of them to fill CS would trade one gap for another. New CS modules in a later wave are the honest fix.

## G4. ELA

- **Speaking and listening:** SL codes appear only at grades K, 6, 8, 9-10 and 12. Grades 1 to 5 and grade 7 have none.
  - Candidates (add the standard, no move): two-sides-theater (Bear's Side of the Story, C15, g2) has the class voicing a scene; counterclaim-ping-pong (g7) is spoken argument and can carry SL.7. retell-puppets (Bedtime Retell, C20) is ELD and carries WIDA codes, not SL.
- **Fluency:** CCSS has RF.x.4 from K to grade 5. Only RF.1.4 is on a module (ela-1-reading-fluency). RF.K.4, RF.2.4, RF.3.4, RF.4.4 and RF.5.4 are all missing. No safe move candidate; new modules, or one K-5 fluency tool whose module carries all six codes.
- **Writing in grade 6:** no grade 6 informative or narrative writing module. debate-prep-desk (Reason Builder, C23) stays on argument. New module.
- **Conventions in grades 3 and 4:** thin. mad-libs-machine (Story Blanks, C33) is the only grade 3 grammar play tool.

## G5. Social studies

Module counts by grade: 5 each for K-5, 7 or 8 each for 6-8, then 4 (g9), 5 (g10), 8 (g11) and 16 (g12).

- **No 9-12 geography course.** Geography standards do appear in 9-12: D2.Geo.5, D2.Geo.7 and D2.Geo.11 are on five history modules (industrial revolution, imperialism, decolonization, globalization, the Gilded Age). What is missing is a geography course or unit of its own after five-themes-field-trip and region-compare in 6-8.
- **No world history before 1750 in 9-12.** Grade 9 starts at the Enlightenment.
- **Civics, economics and psychology all sit in grade 12** (16 modules), while grade 9 has 4.
- **Thin 6-8 economics:** economics appears only inside history units (silk-road-traders, salt-and-gold-caravan, mill-town); there is no 6-8 economics module of its own.
- **Candidates:** none for move-to-gap that would not just move the gap; many 6-8 and 9-12 history modules have their C3 codes covered elsewhere (standards.py lists them), but each also carries a history unit no other tool covers. The grade 12 stack is the natural source if Cory wants to rebalance grades (for example federal-or-state and checks-and-balances to grade 9 civics), but that is a course-sequence decision, not an overlap fix.

## G6. Thin subjects and bands

| Area | Count | Note |
|---|---|---|
| SEL | 2 per band, 8 total, all live | No planned SEL tools at all. |
| Library | 2 per band, 8 total | The K-2 pair is live. |
| Health-PE | 6 per band | 6-8 has no nutrition tool (pressure-point, stress-toolkit, boundaries-builder, screen-time-detective, rules-referee, goal-tracker). |
| CTE | 0 in K-5, 3 in 6-8, 11 in 9-12 | Career awareness in K-5 is absent. |
| World languages | 10 K-12, 7 6-12, 3 9-12 | No K-5-specific tools. |
| Arts K-2 | 7 | Only 1 theater (story-dress-up) and 1 dance (move-like-me). |
| Arts 3-5 | 8 | No media arts in K-5 at all. |

- **Move-to-gap option:** boundaries-builder to 6-8 nutrition (C07). NHES.S4 is also on feelings-faces and pressure-point, so nothing is lost. "Day of Meals: Plan a day of meals and snacks around a busy schedule (practice, a test, a late night), then see how energy, focus and mood hold up and adjust the plan." The recommendation stays with the C07 reshape, because relationships are a required 6-8 health topic and the reshape keeps them.

## G7. Overused actions, formats and settings

Counts per band include the K-12 and 6-12 tools that count against every band they span. The "rare" column counts tools tagged to that band only.

| Band | Heavy before the fixes | Rare |
|---|---|---|
| K-2 (124 tools) | format showdown 22; actions explore 12, manipulate 11, build 11 | escape 1 |
| 3-5 (137) | format puzzle 16; actions explore 13, compose 12, build 12 | creature 1, showdown 1, sandbox 2, escape 2 |
| 6-8 (153) | actions simulate-tune 19, build 17; formats simulator 16, builder 15 | showdown 1, escape 1 |
| 9-12 (209) | actions explore 30, simulate-tune 29; formats simulator 28, explorer 27 | creature 1, showdown 1 |

- **After the fixes** (`python scripts/overlap/stats.py --after`): 9-12 simulate-tune drops from 29 to 27 and manage from 14 to 12; 6-8 build rises from 17 to 18; K-2 robot or machine settings drop from 10 to 7 and food from 8 to 6. No format goes above 25 percent of any subject.
- **Sports settings:** the fixes add one sports setting in 9-12 (Curling Stones, C39). The first draft's Essay Relay and Play-by-Play Voice would have added two more; Essay Relay is now Essay Train, and voice-switcher is kept. Sports stand at 6 in 3-5, 4 in 6-8 and 5 in 9-12 after the fixes.
- **Recommendation for future specs:** in 9-12, prefer predict-reveal, order, fix and trace over another explore or simulate-tune; in 6-8, another builder should be a sandbox or a sort; in 3-5, a sandbox or creature tool is the cheapest way to add variety; avoid new sports settings in 3-5 to 9-12.
