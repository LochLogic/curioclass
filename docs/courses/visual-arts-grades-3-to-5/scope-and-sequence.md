# Scope and sequence: Visual Arts, grades 3 to 5

Course id visual-arts-grades-3-to-5. Grades 3 to 5, three years in one file. Draft, 2026-11-26. Built on frame.md (same folder); the day-by-day plan is data/plans/visual-arts-grades-3-to-5/days.csv.

## The band at a glance

- **Which standards fall in which year.** Year 3 teaches and claims the grade 3 NCAS visual arts ids (the `.3a` ids, 15), year 4 the grade 4 ids (`.4a`, 15), year 5 the grade 5 ids (`.5a`, 15): 45 ids in all, each year's 15 against STANDARD.md 3.2.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn (STANDARD.md 3.1). Each year still claims only its grade's ids, so a child's record shows which grade's standards they met.
- **Meetings.** Two 40-minute sessions a week, 32 weeks a year, 96 weeks over the band: 64 course days a year, 192 in all. The national figure is about 50 minutes a week (arteducators.org), so the plan runs 30 minutes a week over it; the once-a-week path (Shorter path) runs 10 minutes short of it.
- **How school_day is counted.** school_day counts across the whole band, as frame.py reads it: year 3 is school days 1 to 160, year 4 is 161 to 320, year 5 is 321 to 480. A year's course day n (1 to 64) sits in week ceil(n/2); the first session of a week is that week's day 2 (Tuesday) and the second is day 4 (Thursday). So school_day = 160 times (year minus 1) + 5 times (week minus 1) + 2 or 4, and the week inside a year is (school_day minus 160 times (year minus 1) minus 1) // 5 + 1. Year 3's mid-year check (course day 35) is week 18, school day 87. This formula is the file's own; data/plans/calendar.csv is regenerated from the filled school_day at commit, so a one-day offset against today's calendar.csv is not re-counted (every unit and check falls in the frame's weeks either way).
- **Readiness and retrieval.** Every unit assumes only its thread's row from one grade back (grade 2 rows for year 3, then the band's own rows year to year), so no unit needs a readiness check. Day 1 of each unit is a clean hook; day 2 opens with a ten-minute retrieval task on the rows one grade back, with a written ten-minute reteach for a child new to the band. Unit 11 adds a second ten-minute retrieval on day 3 (band day 167): lines of symmetry (m4-symmetry, math grade 4 unit 9), one grade back, with a fold reteach.
- **Same-year retrieval.** Where a unit leans on a row taught earlier the same year (the frame's "Why this unit, here" cells), a five-minute retrieval warm-up opens the day that uses it, named in the note and in `retrieves`: day 21 and day 43 (va-g3-look, unit 1), day 90 (va-g4-craft, unit 5), day 103 (va-g4-revise, unit 6), day 122 (va-g4-craft, with unit 5's mark step card or unit 6's color-plan step card in hand, the child choosing which the piece uses), day 150 (va-g5-craft, unit 9), day 171 (va-g5-revise, unit 10). No readiness check is needed and no unit's first day changes.
- **Studio routine.** Monitors run set-up and clean-up from day 1. Every hands-on day's note names the equipment, the safe use of space, the clean-up minutes and the free path. No paint, ink or clay on a check day.
- **The four processes.** Each year holds all four artistic processes (creating; presenting; responding; connecting), and each unit touches at least the processes the frame names for it (at least two); a unit need not claim all four, and no day claims an id outside its unit's owned rows. In this scope every unit in fact works all four, units 4 and 12 creating by a finishing change before mounting (practice, unscored). Each unit section names the days. Technique days come before the making that needs them; every unit's showing follows a critique day and a revision day, and the end-of-unit assessment comes after both.
- **Portfolio.** One piece a unit with a one-line reflection, 12 over the band, going home at each year's last respond day.

### Logic model

- **Inputs:** two 40-minute sessions a week; step cards, work cards, setting cards; found and low-cost materials.
- **Activities:** technique taught in named steps; works studied with their setting; making with a critique and a revision; written responses to unseen works; a showing each unit.
- **Outputs:** a portfolio folder of 12 pieces with written reflections, 12 showings, two marks a unit per child on the main look-for (a baseline look in the first practice days and the end-of-unit mark).
- **Outcome claimed:** met marks on the year's 15 ids and growth on the look-fors. Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result (APPROACH "Sources").

| Year | Units (days) | Course checks (course days, week) |
|---|---|---|
| 3 (grade 3) | 1 (18), 2 (16), 3 (14), 4 (12) | mid-year 35 to 36 (week 18), year-end 51 to 52 (week 26) |
| 4 (grade 4) | 5 (16), 6 (16), 7 (14), 8 (14) | mid-year 97 to 98 (week 17), year-end 113 to 114 (week 25) |
| 5 (grade 5) | 9 (16), 10 (18), 11 (14), 12 (12) | mid-year 163 to 164 (week 18), year-end 179 to 180 (week 26) |

## Year 3 (grade 3)

### Unit 1. Art detectives (days 1 to 18, weeks 1 to 9)

*How can we tell how a work was made, and what message it sends?* Ids: VA:Re7.1.3a, VA:Re7.2.3a, VA:Cr2.1.3a, VA:Cr2.2.3a (va-g3-look, va-g3-craft). Works: Romare Bearden, The Block; an Asante adinkra cloth; Elizabeth Catlett, Sharecropper.

- **Order.** Clues on The Block (1 to 2), then the adinkra cloth (3) before foam-plate printing (4 to 5), Catlett (6) before collage (7 to 8), modeling (9 to 10), stations with the step cards withdrawn (11), making with the plan card (12), critique (13), revision (14), finish (15), showing (16), end-of-unit assessment (17), respond (18).
- **Processes.** Creating 4 to 5 and 7 to 15; presenting 16; responding 1 to 3, 6, 11, 13, 17; connecting 2, 3, 6 (setting cards).
- **Checks.** End-of-unit day 17. The handling observations for VA:Cr2.2.3a sit on the last two making days (14, 15), never on a check day. Baseline look from day 4.
- **Candidate settled.** Kept: set-up and clean-up minutes on printing days, with half the class printing while half sorts collage paper (day 5 note); no day cost.
- **Sensitivity.** Adinkra as a mourning cloth, symbols by looking only (day 3); Catlett's setting told plainly, children do not cut lino (day 6).
- **Once a week.** 9 sessions: 1-2 / 3-5 / 6-8 / 9-11 / 12 / 13 / 14-16 / 17 / 18. Observations for VA:Cr2.2.3a run on sessions 12 and 13 (the two making sessions), and on 14-16 for any child not yet seen; the showing (16) is hung at the end of session 14-16 and visited outside art time.

### Unit 2. Invented worlds (days 19 to 34, weeks 10 to 17)

*Where do artists' ideas come from, and how do they grow?* Ids: VA:Cr1.1.3a, VA:Cr1.2.3a, VA:Cr3.1.3a (va-g3-ideas, va-g3-revise). Works: Henri Rousseau, The Repast of the Lion; a Hamzanama page; Shaun Tan's invented worlds.

- **Order.** Hook (19), idea page 1 (20), the Hamzanama page (21), overlap for depth (22 to 23), layering texture (24), tools and resources with Tan (25), idea pages 2 and 3 (26, 27), the partner talk card (28), making (29), making with the partner talk (30), revision with the "tools I chose" card (31), showing (32), end-of-unit assessment (33), respond (34).
- **Processes.** Creating 20, 22 to 27, 29 to 31; presenting 32; responding 19, 21, 25, 28, 30, 33; connecting 19 and 21 (setting cards).
- **Checks.** End-of-unit day 33 (no written sitting: self-check, the teacher's table and look-fors scored from the kept work).
- **Candidate settled.** Dropped (a fourth invented world): three works carry the unit and the year's range is met.
- **Lean.** The partner talk leans on ELA grade 3 SL.3.1, which ELA teaches in its unit 1 (weeks 1 to 8), before this unit; no bridge is needed and the card is kept.
- **Sensitivity.** The Hamzanama page is one without battle or demons (day 21).
- **Once a week.** 8 sessions: 1-2 / 3-5 / 6-7 / 8, 9, 11 / 10, 12 / 13 / 14-15 / 16 (local days). The showing (14) is hung at the end of session 13, the revision, and visited outside art time; session 14-15 gives its time to the check.

### Unit 3. Places we know (days 37 to 50, weeks 19 to 25)

*How do artists show the places they know, and how do we judge a work?* Ids: VA:Cr2.3.3a, VA:Cn10.1.3a, VA:Re8.1.3a, VA:Re9.1.3a (va-g3-design, va-g3-judge). Works: a Marshall Islands stick chart; Camille Pissarro, Boulevard Montmartre on a Winter Morning; a third place-and-mood work.

- **Order.** The stick chart (37), map words and the "made for" card (38), Pissarro (39), drawing from looking and the walk (40), the map with a key (41), the box model (42), the checklist (43), drill (44), making (45), making with the critique (46), revision and the "know our school" showing (47), end-of-unit assessment over two days (48, 49), respond (50).
- **Processes.** Creating 40 to 42, 44 to 47; presenting 47; responding 37, 39, 43, 44, 46, 48, 49; connecting 37, 40 (observed details), 45 to 47.
- **Checks.** End-of-unit days 48 (Re8 and the map) and 49 (Re9 and the drawing).
- **Candidate settled.** Kept inside day 39 (band day 39, the unit's day 3): a third place-and-mood work by a living maker from Asia or Africa, picked by the unit plan; no day cost.
- **Sensitivity.** The stick chart carries navigators' knowledge, studied by looking (day 37). Maps show the school only, never a home (day 38); the walk stays on school grounds; an adult cuts any card.
- **Once a week.** 6 sessions: 1-3 / 4-6 / 7-9 / 10-11 / 12-13 / 14. The "know our school" showing (11) is hung at the end of session 10-11 and visited outside art time; the two check days (12-13) take one session: the self-checks move to the last five minutes of session 10-11, and the session holds one written sitting of all the unit's items (about 25 minutes) and the teacher's table (about 8).

### Unit 4. Stories kept in art (days 53 to 64, weeks 27 to 32)

*How do people keep stories and history in art, and how do we show our own?* Ids: VA:Pr4.1.3a, VA:Pr5.1.3a, VA:Pr6.1.3a, VA:Cn11.1.3a (va-g3-show, va-g3-museum). Works: Jacob Lawrence, The Migration Series (travel, work and home panels); a Lakota winter count; the Bayeux embroidery.

- **Order.** Lawrence with the first reaction and setting card (53), work cards (54), the winter count (55), the Bayeux embroidery and the two-work card (56), show spaces (57), choose and mount (58), the artist note (59), critique of notes and mounts (60), revision, the last making day (61), the family show (62), end-of-unit assessment (63), respond (64).
- **Processes.** Creating 58 (a finishing detail before mounting); presenting 57 to 62; responding 53, 60, 63; connecting 53 to 56.
- **Checks.** End-of-unit day 63; the show's look-fors are scored from the kept work after day 62.
- **Candidate settled.** Dropped: three cultures meet VA:Pr6.1.3a and it is a 12-day unit.
- **Sensitivity.** Lawrence (hard history): panels of travel, work and new homes, not violence (53). A hard year on the winter count in one plain sentence (55). Bayeux shown in building, sailing and feasting, not battle (56). Family yes for any showing outside class.
- **Leave-out unit.** If a year runs short past the shorter path, this is the unit a school leaves out (frame).
- **Once a week.** 5 sessions: 1-4 / 5-6 / 7-9 / 11 / 12. The family show (local day 10, day 62) is held outside art time; session 11 is the check.

## Year 4 (grade 4)

### Unit 5. Marks and messages (days 65 to 80, weeks 1 to 8)

*How do artists invent techniques, and what parts of an image carry its message?* Ids: VA:Re7.1.4a, VA:Re7.2.4a, VA:Cr2.1.4a, VA:Cr2.2.4a (va-g4-look, va-g4-craft). Works: Vincent van Gogh, Wheat Field with Cypresses; an ink drawing by Ibrahim El-Salahi; a 1930s national parks poster.

- **Order.** First reaction (65), marks named (66), the sample sheet and practice log (67 to 68), inventing a technique (69), the tool check taught (70), the tool-check gate and small piece (71), second reaction (72), poster parts (73 to 74), making (75), making with the critique (76), revision (77), the "technique library" showing (78), end-of-unit assessment (79), respond (80).
- **Processes.** Creating 67 to 71, 75 to 77; presenting 78; responding 65, 66, 72 to 74, 76, 79; connecting 65, 66, 73 (setting cards).
- **Checks.** End-of-unit day 79. VA:Cr2.2.4a: the gate record (71) and a later observation (76, 77).
- **Candidate settled.** Kept inside day 69 (the unit's day 5): a mark-making work by a living Native American maker; no day cost.
- **Sensitivity.** El-Salahi's work draws on Arabic script; no child copies script as decoration (66). Pointed scissors only after each child passes the gate.
- **Once a week.** 8 sessions: 1-2 / 3-4 / 5-6 / 7-8 / 9-11 / 12-13 / 14-15 / 16. The "technique library" showing (14) is hung at the end of session 12-13 and visited outside art time; session 14-15 is the check.

### Unit 6. A panel together (days 81 to 96, weeks 9 to 16)

*How does a group plan and make one artwork, and how does critique improve it?* Ids: VA:Cr1.1.4a, VA:Cr1.2.4a, VA:Cr3.1.4a (va-g4-ideas, va-g4-revise). Works: the murals of Chicano Park; the painted house walls of Tiébélé.

- **Order.** Chicano Park (81), how a community plans (82), Tiébélé (83), the design problem and brainstorm (84), three approaches (85), the goal card (86), color plan and grid (87 to 88), the critique protocol (89), drawing the sections (90), painting with the protocol critique (91), revision (92), joining (93), the entrance-hall showing (94), end-of-unit assessment (95), respond (96).
- **Processes.** Creating 84 to 88, 90 to 93; presenting 94; responding 81, 83, 89, 91, 95; connecting 81 to 83.
- **Checks.** End-of-unit day 95 (no written sitting; each child marked on their own sketches, card line and section).
- **Candidate settled.** Dropped (a group-made work from Asia): year 4 already studies two Asian works (Zhang Zeduan, Mogao) and the panel needs its 16 days.
- **Sensitivity.** Tiébélé's walls are Kassena women's own work, studied by looking (83). The roll is laid on tables, never on a walkway.
- **Once a week.** 8 sessions: 1-3 / 4-6 / 7-8 / 9-10 / 11 / 12-13 / 14-15 / 16. The entrance-hall showing (14) is hung at the end of session 12-13 and visited outside art time; session 14-15 is the check.

### Unit 7. Buildings and cities (days 99 to 112, weeks 18 to 24)

*How do artists draw the places people build, and how do we judge two works by one checklist?* Ids: VA:Cr2.3.4a, VA:Re8.1.4a, VA:Re9.1.4a (va-g4-design, va-g4-judge). Works: Canaletto, Piazza San Marco; Zhang Zeduan, Along the River During the Qingming Festival; the region's own buildings.

- **Order.** Canaletto (99), the Qingming scroll (100), drawing a building (101 to 102), one checklist on two works (103), drawing outside (104), the three-sentence description (105), the region's buildings (106), checklist drill (107), making with the critique (108), revision (109), the showing wall (110), end-of-unit assessment (111), respond (112).
- **Processes.** Creating 101, 102, 104, 105, 108, 109; presenting 110; responding 99, 100, 103, 107, 108, 111; connecting 99, 100, 106.
- **Checks.** End-of-unit day 111.
- **Candidate settled.** Kept as one of the two unseen city views on day 111 (from Africa or Latin America); no day cost.
- **Safety.** Drawing outside stays on school grounds or the sidewalk in view, a second adult for any walk off the grounds, never a building near a child's home (104).
- **Once a week.** 6 sessions: 1-4 / 5-6 / 7-9 / 10-11 / 12-13 / 14. The showing wall (12) is hung at the end of session 10-11 and visited outside art time; session 12-13 is the check.

### Unit 8. Keeping and showing art (days 115 to 128, weeks 26 to 32)

*How do people keep and show art, and what can an object tell us about where it came from?* Ids: VA:Pr4.1.4a, VA:Pr5.1.4a, VA:Pr6.1.4a, VA:Cn11.1.4a, VA:Cn10.1.4a (va-g4-show, va-g4-museum). Works: the cave temples of Mogao; a tapestry by D.Y. Begay; venue cards; a community tradition from a community source.

- **Order.** Mogao and keeping art (115), technologies past to emerging (116), Begay and inference (117 to 118), venues (119), showing in two places (120), the community tradition (121), making (122), making with the critique (123), revision, label and plan card (124), the wall and slide-set showing (125), end-of-unit assessment over two days (126, 127), respond (128).
- **Processes.** Creating 122 to 124; presenting 115, 116, 119, 120, 124, 125; responding 117, 118, 123, 126, 127; connecting 115, 117, 121 to 125.
- **Checks.** End-of-unit days 126 and 127; the showing's look-fors scored from the kept work after day 125.
- **Candidate settled.** Kept as a unit plan task: the community source list checked open and free for the school's town (day 121 note); no day cost.
- **Sensitivity.** Mogao is sacred, looked at only (115); no Dine design copied (117); no child explains their own family's culture or religion, no sacred practice imitated (121).
- **Leave-out unit.** The year's leave-out unit (frame).
- **Once a week.** 6 sessions: 1-2 / 3-5 / 6-8 / 9-10 / 12-13 / 14. The wall and slide-set showing (local day 11, day 125) is hung at the end of session 9-10 and visited outside art time; the two check days (12-13) take one session as in unit 3.

## Year 5 (grade 5)

### Unit 9. Many readings (days 129 to 144, weeks 1 to 8)

*Why do people read the same picture in different ways, and what cultural links can an image carry?* Ids: VA:Re7.1.5a, VA:Re7.2.5a, VA:Cr2.1.5a, VA:Cr2.2.5a (va-g5-look, va-g5-craft). Works: Diego Rivera, The Flower Carrier; a Yangliuqing New Year print; an Anishinaabe beaded bandolier bag.

- **Order.** Own reading (129), compared readings (130), the Yangliuqing print (131), washes (132 to 133), color mixing (134), the bandolier bag (135), scratch-through (136), the practice-log day (137), making (138), making with the critique (139), revision (140), finish (141), showing (142), end-of-unit assessment (143), respond (144).
- **Processes.** Creating 132 to 134, 136 to 141; presenting 142; responding 129 to 131, 135, 137, 139, 143; connecting 131, 135.
- **Checks.** End-of-unit day 143. Observations for VA:Cr2.2.5a on the last two making days (140, 141).
- **Candidate settled.** Kept as the unseen image on day 143 (a fourth image with cultural links, from Africa); no day cost.
- **Sensitivity.** The vendor's heavy load (129); the bag studied by looking only, no design copied (135); no child speaks for their own culture.
- **Once a week.** 8 sessions: 1-2 / 3-5 / 6-7 / 8-9 / 10-11 / 12-13 / 14-15 / 16. Observations for VA:Cr2.2.5a run on sessions 10-11 and 12-13; the showing (14) is hung at the end of session 12-13 and visited outside art time; session 14-15 is the check.

### Unit 10. Two ideas, one new work (days 145 to 162, weeks 9 to 17)

*How do artists research and merge ideas into something new, and how does an artist statement explain the choices?* Ids: VA:Cr1.1.5a, VA:Cr1.2.5a, VA:Cr3.1.5a (va-g5-ideas, va-g5-revise). Works: Nick Cave's Soundsuits; Romuald Hazoumè's fuel-can masks; Maria Sibylla Merian's Suriname plates.

- **Order.** Soundsuits (145), Hazoumè (146), Merian and research methods (147), two methods tried (148), the merge sketch (149), joining (150), sewing (151), drill (152), making (153), the statement frame (154), statement draft (155), critique on work and statement (156), revising the work (157), revising the statement (158), finish with the research card (159), showing (160), end-of-unit assessment (161), respond (162).
- **Processes.** Creating 148 to 153, 155, 157 to 159; presenting 160; responding 145, 146, 154, 156, 161; connecting 146, 147.
- **Checks.** End-of-unit day 161 (no written sitting).
- **Candidate settled.** Dropped (a merged-idea work from Asia or Latin America): three works carry the unit, year 5 Asia and Latin America are met by Yangliuqing, Qian Xuan and Rivera, and the 18 days are needed for two products.
- **Sensitivity.** Hazoumè's masks are his own art, not ceremonial, and no child wears one (146); Merian's helpers named plainly (147); interviews of a classmate or school adult only (148). Needles counted out and in; an adult cuts any card; no hot glue.
- **Once a week.** 9 sessions: 1-2 / 3-4 / 5 / 6-8 / 9-10 / 11-12 / 13-15 / 16-17 / 18. The showing (16) is hung at the end of session 13-15 and visited outside art time; session 16-17 is the check.

### Unit 11. Seeing freshly (days 165 to 178, weeks 19 to 25)

*How do art and design words help us see our surroundings freshly, and why are works judged by different standards?* Ids: VA:Cr2.3.5a, VA:Cn10.1.5a, VA:Re8.1.5a, VA:Re9.1.5a (va-g5-design, va-g5-judge). Works: an Iznik tile panel; Qian Xuan, Wang Xizhi Watching Geese; Berthe Morisot, The Cradle.

- **Order.** Iznik (165), places that matter (166), art and design words with the symmetry retrieval (167), the map or sketch set (168), Qian Xuan (169), Morisot and comparing standards (170), the grounds walk and labels (171), standards drill (172), making (173), making with the critique (174), revision and showing (175), end-of-unit assessment over two days (176, 177), respond (178).
- **Processes.** Creating 168, 171, 173 to 175; presenting 175; responding 165, 169, 170, 172, 174, 176, 177; connecting 165, 167, 169, 170.
- **Checks.** End-of-unit days 176 (Re8 and the map) and 177 (Re9 and the made work).
- **Candidate settled.** Kept as one of the two unseen works on day 177 (a work judged by different standards, from Africa or the Americas); no day cost.
- **Sensitivity.** Iznik tiles' mosque and tomb settings told (165); places that matter are invited, never required, with no home address drawn (166).
- **Once a week.** 6 sessions: 1-3 / 4-6 / 7-9 / 10-11 / 12-13 / 14. The showing in day 175 is hung at the end of session 10-11 and visited outside art time; the two check days (12-13) take one session as in unit 3.

### Unit 12. Art that changes minds (days 181 to 192, weeks 27 to 32)

*How can art change what people believe, value or do, and how does a curator present it?* Ids: VA:Pr4.1.5a, VA:Pr5.1.5a, VA:Pr6.1.5a, VA:Cn11.1.5a (va-g5-show, va-g5-museum). Works: Lewis Hine's child-labor photographs; Thomas Moran's Yellowstone paintings; Te Papa's exhibition Te Taiao Nature.

- **Order.** Hine (181), Moran (182), curator jobs (183), the Te Taiao pages (184), evidence drill (185), the mounting argument (186), planning the show (187), preparing with the critique of argument cards (188), revising the card and hanging (189), the curated family show (190), end-of-unit assessment (191), respond (192).
- **Processes.** Creating 188 (a finishing change before mounting); presenting 183 to 190; responding 184, 185, 188, 191; connecting 181, 182, 184.
- **Checks.** End-of-unit day 191; the show's look-fors scored from the kept work after day 190.
- **Candidate settled.** Kept as the unseen exhibit page set on day 191 (a second exhibit from Africa or Asia); no day cost.
- **Sensitivity.** Hine (hard history): photographs without injury, health's steps if a child tells something (181). Moran: the Native nations pushed out of the Yellowstone lands, in one plain sentence (182). Te Taiao is shaped with Maori knowledge (184).
- **Leave-out unit.** The year's leave-out unit (frame).
- **Once a week.** 5 sessions: 1-3 / 4-6 / 7-9 / 11 / 12. The curated show (local day 10, day 190) is hung at the end of session 7-9 and held outside art time; session 11 is the check.

## Course-level checks

| Check | Course days (school days) | Week | Covers |
|---|---|---|---|
| Year 3 mid-year | 35, respond 36 (87, 89) | 18 | Units 1 and 2: VA:Re7.1.3a and VA:Re7.2.3a on an unseen print or collage; VA:Cr1.1.3a on a given sketch |
| Year 3 year-end | 51, respond 52 (127, 129) | 26 | Units 1 to 3: VA:Re8.1.3a as a comparison of Catlett's Sharecropper and Bearden's The Block (which media make the quieter mood), VA:Re9.1.3a as a given checklist applied to a Curio Class sample student work, VA:Cr3.1.3a on a given drawing |
| Year 4 mid-year | 97, respond 98 (242, 244) | 17 | Units 5 and 6: VA:Re7.2.4a on an unseen poster; VA:Cr1.1.4a on a new problem from unit 5 (a technique-library cover) |
| Year 4 year-end | 113, respond 114 (282, 284) | 25 | Units 5 to 7: VA:Re8.1.4a on El-Salahi with a new background card, VA:Re9.1.4a as a given filled-in checklist for the van Gogh, the same checklist applied to a Chicano Park mural and the given marks judged for fairness, VA:Cr3.1.4a on a given drawing and comment |
| Year 5 mid-year | 163, respond 164 (407, 409) | 18 | Units 9 and 10: VA:Re7.1.5a and VA:Re7.2.5a on unseen works; VA:Cr3.1.5a as a statement for a unit 9 piece |
| Year 5 year-end | 179, respond 180 (447, 449) | 26 | Units 9 to 11: VA:Re8.1.5a as a comparison of the Yangliuqing print and The Flower Carrier (which visual elements carry the stronger mood), VA:Re9.1.5a as a standard from another time or culture tested against Hazoumè's mask, VA:Cr1.1.5a as a quick merge sketch |

- **Weeks.** All six sit on CALENDAR.md's weeks for this course (18 and 26; 17 and 25; 18 and 26). Arts are specials in K to 5 and do not count against the classroom teacher's stagger (CALENDAR.md rule 1). Each check is one 39-minute session (set-up 3, self-check 5, written sitting 15 with every prompt read aloud once, the teacher's table 12, clean-up 4); its respond session is the next session, the same week.
- **Drawn from earlier units.** Every check falls right after a unit's end-of-unit assessment (days 33, 49, 95, 111, 161, 177). Its items for that unit's skills draw content from earlier units, as the table and each day's goal say: the mid-year idea items use a given sketch or a unit 5 or 9 problem, not the unit 2, 6 or 10 work just scored; the year-end Re8 and Re9 items use works from the year's first two units, not the unseen works the unit 3, 7 or 11 assessment used. Each year-end Re8 and Re9 item uses an earlier unit's work in a form the unit did not use: a comparison, a given checklist checked for fairness, or a standard tested against a work. The just-finished unit's product records are carried, not re-collected.
- **Codes not sampled on a course check (L107), with the reason.** 17 of the 45 codes are sampled. The other 28 are carried from the unit records:
  - *Making and handling, built over several days* (a 40-minute check day with no paint, ink or clay cannot hold them): VA:Cr2.1 and VA:Cr2.2 at each grade (6 codes), VA:Cr1.2 at each grade (3), VA:Cr2.3 at each grade (3), VA:Cn10.1 at each grade (3), and VA:Re7.1.4a (the before-and-after reaction card needs the making between).
  - *Presenting units after the year-end check* (units 4, 8 and 12 come after it, by CALENDAR.md's stagger tool c, and are assessed by their own showing): VA:Pr4.1, VA:Pr5.1, VA:Pr6.1 and VA:Cn11.1 at each grade (12 codes).

## Shorter path

Every route keeps each owned code, skill and end-of-unit assessment, every observation and every respond day. The unit plans check them against real minutes, so none is yet shown to fit.

- **Once a week (the frame's path).** One 40-minute session a week, 32 a year: units in the session groups each unit section lists (year 3: 9, 8, 6 and 5 sessions; year 4: 8, 8, 6 and 6; year 5: 8, 9, 6 and 5), plus each check as one session and its respond session the week after. Merged days keep the technique step card and the making; a second demonstration becomes the next session's five-minute opener. On this path a unit's showing is hung at the end of its revision session and visited outside art time (a partner class walk-by, a drop-in at arrival or pick-up, a family evening); its look-fors are scored from the kept work as on the full path. The end session is the check. Where a unit has two check days (units 3, 8 and 11), the self-check moves to the last five minutes of the revision session and the session holds one written sitting of all the unit's items (about 25 minutes) and the teacher's table (about 8). About 10 minutes a week short of the national figure.
- **Shorter sessions (30 to 35 minutes, same days).** Each day keeps its demonstration, its making and its clean-up; the share at the end shortens. On check days the self-check moves to the last five minutes of the session before; the check runs set-up 2, written sitting 15 (every prompt read aloud once), teacher's table 10, clean-up 2: 29 minutes, with no mounting task for early finishers beyond labeling.
- **A year 10 school days short (2 weeks, 4 sessions).** Four Fluency days a year fold into a neighbor, each saving 40 minutes, 160 minutes a year; the folded drill becomes the next day's five-minute opener:
  - Year 3: day 8 (collage drill, into 9), day 10 (modeling drill, into 11's stations), day 23 (depth thumbnails, into 24), day 44 (drawing and checklist drill, into 45).
  - Year 4: day 68 (mark drill, into 69), day 74 (parts drill, into 75), day 88 (grid drill, into 89), day 102 (building sketches, into 103).
  - Year 5: day 133 (wash strips, into 134; its log entry moves to 137), day 152 (joining and sewing drill, into 153), day 172 (standards drill, into 173), day 185 (evidence drill, into 186).
  - Where a fold day is a baseline practice day (days 8, 10, 23, 44, 68, 102, 133 and 185), its rotating group is observed in the next day's opener.
  - No check, respond, observation or showing day folds. Past this, the year's leave-out unit (4, 8 or 12) is the frame's last resort.

## For the lead

1. **Frame cells for the year-end checks repeat the end items (frame fix).** The frame's checks table sets each year-end check (days 51, 113, 179) to the Re8 and Re9 written items on an unseen work, the same task form the unit 3, 7 and 11 end-of-unit assessment gives one or two days before. That breaks rule 2 (no task form repeated within two weeks) and rule 3 (a check right after a unit's assessment draws that unit's skills from earlier units). This scope draws them from earlier-unit works in a form the unit did not use (Course-level checks table): year 3 a comparison of Catlett's Sharecropper and Bearden's The Block, and a given checklist applied to a sample student work; year 4 El-Salahi with a new background card, and a given filled-in van Gogh checklist applied to a Chicano Park mural and judged for fairness; year 5 a comparison of the Yangliuqing print and The Flower Carrier, and a standard from another time or culture tested against Hazoumè's mask (expert read finding 2). Fix: change the frame's year-end check cells to match (the exact wording is in docs/reviews/sequence-visual-arts-grades-3-to-5-fixes-2026-11-26.md, "For the structure pass").
2. **Codes not sampled on any course check (L107).** 28 of 45, listed with reasons under Course-level checks. If the lead wants more on the checks, the cheapest adds are VA:Cn11.1 (a written item on a unit 1, 5 or 9 work's setting) at each year-end check.
3. **Stale link: the winter count and media arts.** The frame's unit 4 row and its For the lead item 2 name the Lakota winter count as a link to media arts 3 to 5 unit 12, but the media arts fix review (docs/reviews/frame-music-theater-media-arts-fixes-2026-11-26.md) dropped it there. Day 55's note says the link is stale. Lewis Hine is also linked from music 3 to 5, which the frame does not say. Fix: update the frame's link lines.
4. **Carried from the frame, unchanged.** The after-core check-week clashes for the lead's calendar pass (frame item 1); the supplies ceiling for Cory ($60, $50, $50 a class, pick $75 a class a year with the free path kept, frame item 3); the facts the unit plans confirm at source (frame item 4).
5. **ELA lean is moot.** The frame's "if ELA teaches SL.3.1 later" line need not apply: ELA grade 3 teaches it in weeks 1 to 8, before unit 2 (weeks 10 to 17).
