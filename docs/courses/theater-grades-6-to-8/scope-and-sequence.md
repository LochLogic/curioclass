# Scope and sequence: Theater, grades 6 to 8

Course `theater-grades-6-to-8` (catalog id `theater-6-8`), grades 6 to 8 as one band course, written 2026-11-26 from the frame (docs/courses/theater-grades-6-to-8/frame.md) and fixed the same day after the expert read (docs/reviews/sequence-theater-grades-6-to-8-fixes-2026-11-26.md). The days live in data/plans/theater-grades-6-to-8/days.csv; this page gives the judgment behind them.

## How this course runs

- **Three years in one file.** Year 6, then year 7, then year 8, each 64 course days: four units (18, 14, 14 and 14 days), a mid-year check with its respond day after the second unit, and a year-end check with its respond day after the fourth. Course days run 1 to 192 across the band; `stretch` is the frame's unit number (1 to 12).
- **Which standards fall in which year** (STANDARD.md 3.1): year 6 claims only the 24 grade 6 theater ids (`TH:...6a` to `6c`), year 7 only the 24 grade 7 ids, year 8 only the 24 grade 8 ids: 72 in all, the count in STANDARD.md 3.2, and days.csv carries all 72, each taught and assessed in its own year. A year revisits the year before's ids as practice that returns, never as a claim.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn; each year still claims only its own grade's ids, so a student's record shows which grade's standards they met. A student who meets year 8 before year 7 gets each retrieval task's printed reteach card, inside its 10 minutes, as written.
- **Meeting days and `school_day`.** Two 40-minute sessions a week, 32 weeks a year. `school_day` counts school days across the whole band, 1 to 480 (year 6 is 1 to 160, year 7 is 161 to 320, year 8 is 321 to 480), as scripts/frame.py reads a band course: course day n sits on school day ceil(2.5 x n), so the two sessions fall on the third and fifth school day of each week. Inside a year, course day k of that year is in week ceil(k / 2) and on school day ceil(2.5 x k) of that year's calendar (subtract 160 for year 7, 320 for year 8). This is the frame's even spread, written out, and the one formula for the course: school_day = ceil(2.5 x course day), counted across the band; a filled school_day is what frame.py reads, and the week is (school_day of the year - 1) // 5 + 1. Every unit and check falls in the weeks the frame gives (checked by script in the fix pass).
- **Minutes.** Every day's 40 minutes hold the set-up routine (3), the warm-up (5), the work and the close (4); a making day with card, tape and paint takes 6 for clean-up. A retrieval task takes ten minutes of the opener for both rows together; the reteach runs inside those same 10 minutes from a printed reteach card for the students new to theater while the others do the retrieval task. Day 2 of each unit reads: set-up 3, retrieval 10 (it stands in for that day's warm-up; in unit 1 the warm-up routine taught in steps takes 15 and replaces the 5-minute warm-up), the day's teaching 15, practice 8, close 4. A retrieval of a model from an earlier unit of the same band (days 137, 171, 186) takes 5 minutes of the opener. The showing day and the written day are timed in their notes (39 and 40 minutes), the course check days at 36.
- **Day kinds** follow docs/GLOSSARY.md and the frame: Understanding days show a technique in named steps with its step card or study a work with its setting (the artistic process "responding" lives here, never on a respond day); Fluency days repeat a taught technique with feedback (drills and run-throughs); Application days rehearse, devise or make, the second rehearsal holding the unit's one critique and the next day the revision; Check days are the showing and the written day; Respond days act on marks already made. Every unit opens with a baseline look at its main look-for during its first practice days and closes with the same look on the showing day, so each student has two marks and the growth is the change.
- **Order inside every unit.** Technique days come before the making that needs them; each showing has a critique (second rehearsal) and a revision (the day after) before the showing check; final observation rounds, with roles rotated, sit on the last rehearsal days so every student has an observed acting turn before the check.
- **End-of-unit assessment.** Two check days near each unit's end, a showing day (look-fors marked live, kept sheets scored after) and a written day (items on an unseen description or the teacher's unseen Curio Class scene), so the teacher never marks a performance and reads other work at once. Response time is the unit's respond day, its last day. No unit is over 25 days, so none has a mid-unit assessment. Every student is marked on their own evidence: where a group makes a sketch, cue sheet or venue plan, each student fills their own sheet first or copies the group's chosen version onto it, and in a group presentation each student speaks one part.

### Readiness and retrieval (rule 2)

Every row the band assumes was last used one grade back, so every unit opens with a retrieval task in day 2's opener and no unit owes a readiness check; day 1 of every unit stays clean for the hook and the compelling question. No `assess` cell says `readiness`.

| Unit | Earlier row assumed | Last used | Treatment |
|---|---|---|---|
| 1 | th-g5-actor; th-g5-notice | grade 5 (Theater, grades 3 to 5 unit 10) | retrieval, day 2, with the reteach card inside the 10 minutes for a student new to theater (grades 3 to 5 is not a core course) |
| 2 | th-g5-imagine (unit 9); th-g5-story (unit 12) | grade 5 | retrieval, day 20, reteach card |
| 3 | th-g5-design (unit 11); th-g5-judge (unit 12) | grade 5 | retrieval, day 36, reteach card |
| 4 | th-g5-show (unit 9); th-g5-world (unit 11) | grade 5 | retrieval, day 50, reteach card |
| 5 | th-g6-actor; th-g6-notice (unit 1, days 1 to 18) | grade 6 | retrieval, day 66 |
| 6 | th-g6-imagine; th-g6-story (unit 2, days 19 to 32) | grade 6 | retrieval, day 84 |
| 7 | th-g6-design; th-g6-judge (unit 3, days 35 to 48) | grade 6 | retrieval, day 100 |
| 8 | th-g6-show; th-g6-world (unit 4, days 49 to 62) | grade 6 | retrieval, day 114 |
| 9 | th-g7-actor; th-g7-notice (unit 5, days 65 to 82) | grade 7 | retrieval, day 130 |
| 10 | th-g7-imagine; th-g7-story (unit 6, days 83 to 96) | grade 7 | retrieval, day 148 |
| 11 | th-g7-design; th-g7-judge (unit 7, days 99 to 112) | grade 7 | retrieval, day 164 (day 165's opener if the walk of the real space leaves the room) |
| 12 | th-g7-show; th-g7-world (unit 8, days 113 to 126) | grade 7 | retrieval, day 178 |

The `retrieves` column names these ids on those days. Three days also open with a 5-minute retrieval of a model from an earlier unit: day 137 (th-g7-judge, unit 7, days 99 to 112), day 171 (th-g8-notice, unit 9, days 129 to 146) and day 186 (th-g8-design, unit 11, days 163 to 176). The frame's models (warm-up routine, character map, critique protocol and the rest) return as review on the days its Models table names.

### The four processes

The bar asks for all four artistic processes in each course, and each year claims all four through owned ids. A unit claims only the processes its owned rows name (the frame's Units table) and need not claim all four; where a process is touched beyond them, it is practice on an existing day (a one-line reaction, a critique question), costs no day and claims no id. No day carries a code outside its unit's owned rows (checked by script). Days below are counted from days.csv codes, plus the days marked "touched" in their notes.

| Unit | Create | Perform | Respond | Connect |
|---|---|---|---|---|
| 1 | 3, 6, 7, 9 to 12, 14, 16 to 18 | 2, 4 to 7, 10 to 12, 14 to 16, 18 | 1, 8, 10, 13, 15, 17, 18 | touched day 8 (an artist's life, a company's setting) |
| 2 | 22 to 24, 26 to 30, 32 | 20, 23, 26, 28 to 30, 32 | touched days 21 (each student's one-line reaction to a choice in Bean's version) and 26 (critique) | 19, 21, 25, 29, 31, 32 |
| 3 | 36, 40, 41, 43 to 46, 48 | 37, 38, 40, 41, 43, 45, 46, 48 | 35, 39, 42, 43, 45, 47, 48 | touched days 35 and 42 (works in their setting, purpose and audience) |
| 4 | 51 to 53, 55 to 58, 60, 62 | 57 to 60, 62 | 54, 59, 61, 62 | 49, 50, 53, 55, 59 to 62 |
| 5 | 68, 70 to 72, 74 to 76, 78 to 80, 82 | 66, 67, 69, 70, 72, 74 to 76, 78 to 80, 82 | 65, 73, 74, 77, 79, 81, 82 | touched day 73 (artists' lives and settings) |
| 6 | 84, 87, 89 to 92, 94, 96 | 83, 87, 88, 90, 91, 93, 94, 96 | touched days 85 (each student's one-line reaction to the stage manager's opening) and 90 (critique) | 85, 86, 89, 95, 96 |
| 7 | 100, 104, 105, 107 to 110, 112 | 101, 103, 104, 108, 110, 112 | 99, 102, 106, 107, 109, 111, 112 | touched days 99 and 102 (kabuki in its time and place; purpose) |
| 8 | 115, 116, 119 to 124, 126 | 115, 116, 119, 120, 122 to 124, 126 | 118, 122, 125, 126 | 113, 114, 116, 117, 119, 124, 126 |
| 9 | 131, 135, 136, 138 to 140, 142 to 144, 146 | 130, 132 to 134, 136, 139, 140, 142 to 144, 146 | 129, 137, 141, 143, 145, 146 | touched days 132 and 134 (Stanislavski and Spolin in their time and place) |
| 10 | 148, 152 to 158, 160 | 149, 150, 152, 155, 157, 158, 160 | touched days 151 (each student's one-line reaction to a choice in one production) and 155 (critique) | 147, 151, 153, 156, 158 to 160 |
| 11 | 164, 166, 167, 169, 170, 172 to 174, 176 | 165, 167, 169, 170, 173, 174, 176 | 163, 168, 171, 172, 175, 176 | touched days 163 and 168 (playhouses and a touring company in their settings) |
| 12 | 180, 181, 183 to 185, 187, 188, 190 | 184, 186 to 188, 190 | 182, 186, 189, 190 | 177 to 179, 181, 185, 188, 190 |

Every year touches all four processes through owned ids (bar criterion 1). Each responding or connecting id that had one teaching day before its written check now has a second short touch on a later day of its unit, coded there: one written line in the close (5 minutes from the second run or self-check) or as the critique's question (days 10, 15, 29, 43, 45, 55, 59, 74, 79, 89, 107, 109, 122, 143, 153, 172, 186). TH:Re9.1.8a has a full day of its own (171) and no second touch.

### Logic model (one page, from the frame)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; a clear floor; step cards; adapted scenes; research and object cards; found and low-cost materials | The actor's tools, staging, design and devising taught in steps; plays, forms and companies studied with their setting; rehearsal with a critique and a revision; a showing each unit | A portfolio folder of 12 pieces over the band with reflections; 12 showings; two marks a unit per student on the main look-for | Met marks on the year's 24 ids and growth on the look-fors |

Nothing here has been tried with students, and Curio Class makes no claim that arts study raises any other result.

### Equipment, space and the free path

The unit's floor line (chairs and bags to the walls, room for arms out, soft soles or bare feet on a clean floor; no lifts, no falls, no contact) is set in the note of its first floor day and on its first Application day, holds on every floor day after, and is printed on every section plan; day-specific controls (the making rules, the light rules, a seated faint, the real-space check) stay in the notes of the days that need them, with the free stand-in where the frame lists one. A class of 30 needs a clear floor, chairs, printed scenes, card, tape, found objects, the room's own switch and blinds, and the voice; nothing must be bought. The optional flashlights and colored film are year 6's ($30 in unit 3, reused for the band). A school device plays a sound cue only in units 7 and 11 and records a take only by the student's and family's choice. One student at home: the parent is the audience and critique partner, a group scene has a doubled version, and the showing is to the family or a recorded take.

## Year 6 (grade 6 ids, 24)

### Unit 1. Who is this character? (days 1 to 18, weeks 1 to 9, school days 3 to 45)

Arc: the hook on Lloyd's store scenes and the year's floor routine (day 1), then the warm-up routine (2), given circumstances on the character map (3), three body choices (4) and an acting method (6), each followed by practice and a first rehearsal (5, 7). The study of an artist's life (8) and of traits (9) feed the second rehearsal's critique (11) and the revision (12); tastes and beliefs (13) come after students have watched and joined in enough scenes to name them. Final observation rounds (14) and a run-through (15) lead to the showing check (16), the written check (17) and respond (18). Why this order: the warm-up and floor routine come first because every later day uses them; the body choice is taught before it is rehearsed, and traits are named before the critique asks for them. Unit 1 is longest (18 days): seven ids, the year's routines and two grade 5 rows retrieved. SL.6.4 is practiced, not owned; ELA grade 6 teaches presentation in unit 3 (weeks 13 to 18), later, so day 2's warm-up card carries the bridge line and nothing marks a presentation.

Assessments: no readiness check (retrieval day 2). End-of-unit assessment: day 16, the showing, marks TH:Pr4.1.6b live and collects the character map (TH:Cr1.1.6c), the rehearsal record (TH:Pr4.1.6b) and the rehearsal note (TH:Pr5.1.6a); day 17, the written day, carries TH:Cr3.1.6b, TH:Re7.1.6a, TH:Re8.1.6a and TH:Re8.1.6c on the teacher's unseen scene and an unseen artist description. Respond day 18.

Candidate settled: **kept, no added days.** The bar's criterion 9 on set-up and close minutes: every day's 40 minutes hold set-up 3 and close 4; chairs move once to the walls at set-up and back at close, and on showing days the audience sits on those same chairs along the walls, so no day moves chairs twice.

### Unit 2. One servant, two masters (days 19 to 32, weeks 10 to 16, school days 48 to 80)

Arc: the Goldoni hook with a commedia print in its setting (19), key events marked on the adapted scene (20), the two versions mapped (21), the staging problem and its fixes (22), a walking-pace run of the key events (23) and a first rehearsal that analyzes each fix (24). The era cards (25) come before the critique (26) so the defense of a fix can draw on them; revision (27), final observation rounds (28) and a run-through (29) lead to the showing (30), the written day (31) and respond (32). Why this order: the script markup comes first because the staging problem is defined by the key events; the fixes are listed before they are tested.

Assessments: end-of-unit day 30 (TH:Pr4.1.6a script markup, TH:Cr1.1.6a idea sheet, TH:Cr2.1.6a look-for with its reason line) and day 31 (TH:Cn11.2.6a, TH:Cn11.2.6b written). Respond day 32.

Candidate settled: **dropped.** A third mistaken-identity version from outside Europe: TH:Cn11.2.6a is met in full by two versions, year 6 already spans five continents (Ghana, Peru, the United States, Japan, Italy, England, Aotearoa New Zealand), and a third study would cost a day the 14-day unit cannot spare; the unit plan may offer one as an extension reading.

### Unit 3. Designing the scene (days 35 to 48, weeks 18 to 24, school days 88 to 120)

Arc: the Bread and Puppet and Ishioka hook (35), the design problem (36), cues on the cue sheet (37) and a cue drill (38), then the class criteria card (39) before the making (40) and the first tech rehearsal (41). Audience and aim (42) sit before the critique (43) so the critique can ask who the design is for; revision (44) and a cue run with the final observation round (45) lead to the showing (46), the written day (47) and respond (48). Why this order: cues are taught and drilled before anything is built; the criteria come before any judgment is written. W.6.1 is practiced, not owned: ELA grade 6 units 1 and 2 (weeks 1 to 12) teach claim and evidence before day 39.

Assessments: end-of-unit day 46 (TH:Cr1.1.6b sketch, TH:Pr5.1.6b cue sheet, TH:Cr3.1.6c look-for; the sketch sheet and cue sheet are each student's own, filled on days 37 and 40 with the group's chosen version copied) and day 47 (TH:Re9.1.6b, TH:Re9.1.6a, TH:Re9.1.6c written). Respond day 48.

Candidate settled: **dropped.** A lighting maker from Africa or Latin America beside the two: year 6 already holds Africa (Ghana, unit 4) and Latin America (Peru, unit 1), and day 35 already studies two makers in its 40 minutes; the unit plan keeps the idea as the first swap if a rights line fails.

### Unit 4. Our shared story (days 49 to 62, weeks 25 to 31, school days 123 to 155)

Arc: Foriwa's townspeople (49), the class's shared theme or problem (50), offers and "yes, and" (51) and offer rounds (52), the first devising rehearsal (53), then Taki Rua and how cultural views shape judgment (54) before the critique (55) and revision (56). The audience adaptation (57), final observation rounds (58) and a run-through (59) lead to the informal showing (60), the written day (61) and respond (62). Why this order: the theme is chosen before devising starts; offers are practiced before the group builds; the audience change comes after the piece is polished.

Assessments: end-of-unit day 60 (TH:Pr6.1.6a and TH:Cn11.1.6a live; TH:Cr2.1.6b log and TH:Cr3.1.6a note collected) and day 61 (TH:Cn10.1.6a, one character's action and want and the view of the community they give; TH:Re8.1.6b written). Respond day 62. The year-end check follows in week 32 and draws on units 1 to 3.

Candidate settled: **kept, no added days.** The problem list's items are checked as local, public and non-partisan before the unit plan is written (day 50's note).

## Year 7 (grade 7 ids, 24)

### Unit 5. What does the character want? (days 65 to 82, weeks 1 to 9 of year 7, school days 163 to 205)

Arc: the Proposal hook and a first compared reaction (65), varied warm-ups (66), goals (67), the inner monologue (68), a goal drill (69), two rehearsal methods (70) and traits that fit a goal (71) before the first rehearsal (72). Artists' lives (73) and a trait and goal drill (74) feed the critique (75) and revision (76); taste and beliefs in discussion (77) follow, then final observation rounds (78) and a run-through (79), the showing (80), the written day (81) and respond (82). Why this order: a goal is named before it is played, and traits are fitted to it before rehearsal; comparison of reactions starts on day 65 so the day 81 item has had practice.

Assessments: end-of-unit day 80 (TH:Pr4.1.7b, TH:Cr3.1.7b live; TH:Pr5.1.7a note with the rotating-list marks; TH:Cr1.1.7c map) and day 81 (TH:Re7.1.7a, TH:Re8.1.7a, TH:Re8.1.7c written). Respond day 82.

Candidate settled: **dropped.** A third artist-from-life work by a maker from Asia or Africa: day 73 already studies three artists, and year 7 holds Asia (India, Japan) and Africa (Kenya) in units 6 to 8.

### Unit 6. The lost ring (days 83 to 96, weeks 10 to 16, school days 208 to 240)

Arc: the ring scene in its setting with the story map (83), three fixes from named viewpoints (84), research on the first production (85) and object study (86) before the stagings are rehearsed (87) and drilled (88). The defense note frame (89: claim, analysis, background, context, the Gupta court) is shown before the critique (90) asks which staging is stronger; revision with the written defense (91), final observation rounds (92) and a run-through (93) lead to the showing (94), the written day (95) and respond (96). RL.7.3 is practiced, not owned: ELA grade 7 unit 1 (weeks 1 to 6) teaches it first.

Assessments: end-of-unit day 94 (TH:Pr4.1.7a live; TH:Cr1.1.7a idea sheet; TH:Cr2.1.7a defense note) and day 95 (TH:Cn11.2.7a, TH:Cn11.2.7b written). Respond day 96.

Candidate settled: **dropped.** A living Indian theater maker's staging of Shakuntala: the unit has no free day, and year 7 already has living makers (Miranda, Devlin, Spiderwoman Theater). The unit plan may link one in the teacher notes.

### Unit 7. Stage magic (days 99 to 112, weeks 18 to 24, school days 248 to 280)

Arc: the kabuki print and UNESCO's page (99), the design problem (100), several elements chosen (101), Devlin and the hanamichi on aim and viewers (102), a cue drill (103), the making with the two-minute presentation (104) and the first tech rehearsal (105). Preference with evidence (106) comes before the critique (107); revision (108) and a run-through with the final observation round (109) lead to the showing (110), the written day (111) and respond (112).

Assessments: end-of-unit day 110 (TH:Cr1.1.7b presentation live in the four-minute slot, each student marked on the one part they speak and on their own explain line from day 104; TH:Pr5.1.7b cue sheet, each student's own from day 101; TH:Cr3.1.7c note) and day 111 (TH:Re9.1.7b, TH:Re9.1.7a, TH:Re9.1.7c written). Respond day 112.

Candidate settled: **dropped.** A living designer from Africa or the Americas beside the two: Devlin is living, the year's range holds both regions elsewhere, and day 102 is full; kept as a swap option for the unit plan.

### Unit 8. Weaving our voices (days 113 to 126, weeks 25 to 31, school days 283 to 315)

Arc: Spiderwoman Theater's storyweaving (113), the interview cards' five voices (114), respect, focus and the log (115), the first weaving rehearsal (116), another art from the setting (117) and Kamiriithu's two judgments (118), then a second rehearsal adding the art (119), the critique (120), revision (121), a transition drill (122) and final observation rounds (123), the showing (124), the written day (125) and respond (126).

Assessments: end-of-unit day 124 (TH:Cn10.1.7a and TH:Cn11.1.7a live; TH:Cr2.1.7b rotating-list marks; TH:Cr3.1.7a note; TH:Pr6.1.7a log) and day 125 (TH:Re8.1.7b written). Respond day 126. The year-end check follows in week 32 and draws on units 5 to 7.

Candidate settled: **kept, no added days.** The interview cards are read for fairness to every voice before the unit plan is written (day 114's note).

## Year 8 (grade 8 ids, 24)

### Unit 9. Tactics (days 129 to 146, weeks 1 to 9 of year 8, school days 323 to 365)

Arc: The Rivals hook and talk about decisions noticed (129), tactics against an obstacle (130), the motive line (131), Stanislavski's objectives (132), a tactic-switch drill (133), Spolin's games and status (134), the bodily response (135) and the first rehearsal (136). Judging by criteria (137) and a bodily-response drill (138) feed the critique (139) and revision (140); taste and beliefs beside criteria (141), final observation rounds (142) and a run-through (143) lead to the showing (144), the written day (145) and respond (146). SL.8.4 is practiced, not owned; ELA grade 8 teaches presentation in unit 5 (weeks 26 to 32), later, so day 130's warm-up card carries projection and eye focus for the stage.

Assessments: end-of-unit day 144 (TH:Pr4.1.8b and TH:Cr3.1.8b live with their kept records; TH:Cr1.1.8c map; TH:Pr5.1.8a technique note) and day 145 (TH:Re7.1.8a, TH:Re8.1.8a, TH:Re8.1.8c written). Respond day 146.

Candidate settled: **dropped.** A living actor's account of a technique from Asia, Africa or the Americas: days 132 and 134 are full, and year 8 holds Brazil, China and South Africa elsewhere with living companies in units 10 to 12.

### Unit 10. The chalk circle (days 147 to 160, weeks 10 to 16, school days 368 to 400)

Arc: the judge's test and the 1324 troupe painting (147), three viewpoints with fixes (148), pacing (149) and a pacing drill (150), research on two productions of Brecht's play (151), the first rehearsal in two paces (152), objects and researched background (153) and the original scene devised from it (154), then the critique (155), revision with the staging note (156) and a run-through with the final observation round (157), the showing (158), the written day (159) and respond (160).

Assessments: end-of-unit day 158 (TH:Pr4.1.8a live; TH:Cr1.1.8a and TH:Cr2.1.8a idea sheets; TH:Cn11.2.8b staging note; the research sheet collected) and day 159 (TH:Cn11.2.8a transfer item, with the kept research sheet). Respond day 160.

Candidate settled: **dropped.** A living Chinese opera or theater maker's account of Yuan drama: no free day; the unit plan may link one for the teacher.

### Unit 11. The room is the stage (days 163 to 176, weeks 18 to 24, school days 408 to 440)

Arc: the Globe and Arena Stage (163), the real space walked and its venue plan (164), elements combined (165), simple technology shown (166) and drilled (167), Ilbijerri on effect (168), the making (169) and a first tech rehearsal in the real space (170). The paired judgment (171) comes before the critique (172); the revision holds the cue refinement, the final observation round and the portfolio piece (173), then the showing (174), the written day (175) and respond (176). This unit has no run-through day: the frame's 14 days hold six technique and study days because the design id set is six ids wide. W.8.1 is practiced, not owned: ELA grade 8 units 1 and 2 (weeks 1 to 13) teach it first.

Assessments: end-of-unit day 174 (TH:Cr3.1.8c live; TH:Cr1.1.8b venue plan and TH:Pr5.1.8b cue sheet, each student's own from days 164 and 165) and day 175 (TH:Re9.1.8b, TH:Re9.1.8a, TH:Re9.1.8c written). Respond day 176.

Candidate settled: **dropped.** A site-specific or touring company from Africa or Asia: Ilbijerri already gives the touring case, and South Africa and China are in units 12 and 10.

### Unit 12. Theater for a change (days 177 to 190, weeks 25 to 31, school days 443 to 475)

Arc: Boal's forum theater (177), the issue and its interview cards (178), kinds of drama (179) and rotating leads (180) before the first devising rehearsal (181); cultural views and judgment (182), a run and analysis (183), the critique (184), revision (185), a polish drill using unit 11's venue plan (186) and final observation rounds with a dress run (187), the showing (188), the written day (189) and respond (190).

Assessments: end-of-unit day 188 (TH:Cn10.1.8a and TH:Pr6.1.8a live; TH:Cn11.1.8a, TH:Cr2.1.8b log; TH:Cr3.1.8a note) and day 189 (TH:Re8.1.8b written). Respond day 190. The year-end check follows in week 32 and draws on units 9 to 11.

Candidate settled: **kept, no added days.** The issue list is checked as local, public and non-partisan, and the forum scenes as low-stakes, before the unit plan is written (day 178's note).

## Course-level checks

| Check | Course days | School days (band; in its year) | Week | Samples | Drawn from |
|---|---|---|---|---|---|
| Year 6 mid-year | 33 check, 34 respond | 83, 85 | 17 | TH:Pr4.1.6b (body choices tried), TH:Cr3.1.6b (body and voice traits) live; TH:Re7.1.6a written | unit 1 only (unit 2's assessment was days 30 and 31) |
| Year 6 year-end | 63 check, 64 respond | 158, 160 | 32 (finals) | TH:Cr1.1.6a, TH:Pr5.1.6b live, with each student's one line on how their cue is woven in (what, when, why); TH:Re9.1.6a written | units 1 to 3 (unit 4 assessed by its showing) |
| Year 7 mid-year | 97, 98 | 243, 245; 83, 85 | 17 | TH:Pr4.1.7b, TH:Cr3.1.7b (body and voice traits that fit the goal) live; TH:Re7.1.7a written | unit 5 only |
| Year 7 year-end | 127, 128 | 318, 320; 158, 160 | 32 (finals) | TH:Pr4.1.7a, TH:Cr3.1.7c live; TH:Re9.1.7a written | units 5 to 7 |
| Year 8 mid-year | 161, 162 | 403, 405; 83, 85 | 17 | TH:Pr4.1.8b, TH:Cr3.1.8b (a physical, a vocal and a bodily-response choice, each held) live; TH:Re7.1.8a written | unit 9 only |
| Year 8 year-end | 191, 192 | 478, 480; 158, 160 | 32 (finals) | TH:Pr4.1.8a, TH:Cr1.1.8b live; TH:Re9.1.8a written | units 9 to 11 |

Each check follows the unit the frame names; each check right after a unit's end-of-unit assessment draws its items from earlier units, so it never repeats the assessment just given. The weeks are CALENDAR.md's (weeks 17 and 32 in every year); no core check day is touched, and the arts electives count as one course in 6 to 8 (CALENDAR.md rule 3). Task form (rule 2): a check is a showing on a fresh card with its own items, so it may follow a unit showing; what never repeats inside two weeks is the same item on the same work, and each check's note says so. Collect once: no check re-asks items its unit gave one to three days before; the mid-year checks draw on the unit before (the just-assessed unit's showing and kept sheets are carried unscored), and the year-end checks on units 1 to 3 of the year (the fourth unit is assessed by its own showing).

**Codes not sampled on a check day** (Cory 2026-11-24, L107). The six checks sample 18 of the 72 ids. The other 54 are each assessed in full by their own unit's end-of-unit assessment and are not sampled because a 36-minute fresh-task check marks two live look-fors and one written item, so the teacher marks one group at a time and hears no talk (the frame's check design). Year 6: TH:Cr1.1.6b, TH:Cr1.1.6c, TH:Cr2.1.6a, TH:Cr2.1.6b, TH:Cr3.1.6a, TH:Cr3.1.6c, TH:Pr4.1.6a, TH:Pr5.1.6a, TH:Pr6.1.6a, TH:Re8.1.6a, TH:Re8.1.6b, TH:Re8.1.6c, TH:Re9.1.6b, TH:Re9.1.6c, TH:Cn10.1.6a, TH:Cn11.1.6a, TH:Cn11.2.6a, TH:Cn11.2.6b. Year 7: TH:Cr1.1.7a, TH:Cr1.1.7b, TH:Cr1.1.7c, TH:Cr2.1.7a, TH:Cr2.1.7b, TH:Cr3.1.7a, TH:Pr5.1.7a, TH:Pr5.1.7b, TH:Pr6.1.7a, TH:Re8.1.7a, TH:Re8.1.7b, TH:Re8.1.7c, TH:Re9.1.7b, TH:Re9.1.7c, TH:Cn10.1.7a, TH:Cn11.1.7a, TH:Cn11.2.7a, TH:Cn11.2.7b. Year 8: TH:Cr1.1.8a, TH:Cr1.1.8c, TH:Cr2.1.8a, TH:Cr2.1.8b, TH:Cr3.1.8a, TH:Cr3.1.8c, TH:Pr5.1.8a, TH:Pr5.1.8b, TH:Pr6.1.8a, TH:Re8.1.8a, TH:Re8.1.8b, TH:Re8.1.8c, TH:Re9.1.8b, TH:Re9.1.8c, TH:Cn10.1.8a, TH:Cn11.1.8a, TH:Cn11.2.8a, TH:Cn11.2.8b. Naming them with the reason is enough where the frame's check table limits the sample (lead call, 2026-11-26); any wider sample is a frame change.

## Shorter path

**A year about 10 school days short.** Ten school days are two weeks, about four sessions of this course (the one reading of "10 days short" for a K to 8 arts course; lead call, 2026-11-26). Each year folds four unassessed Fluency days into a neighbor; nothing assessed moves and every owned id stays on other days of its unit. Each fold saves one 40-minute session; the neighbor stays at 40 minutes because the folded work replaces that day's repeated warm-up or second run.

| Year | Fold this day | Into | Work kept in the neighbor | Minutes inside the neighbor | Minutes saved |
|---|---|---|---|---|---|
| 6 | 10 (trait drill) | 11 | the trait drill as the opener; day 10's TH:Re8.1.6a line in day 11's close | 5: the drill is that day's warm-up | 40 |
| 6 | 29 (run-through) | 28 | one run of each staging after the observation rounds | 10, replacing the second observation pass | 40 |
| 6 | 45 (cue run) | 44 | one cue run and the final observation round; day 45's TH:Re9.1.6a line in day 44's close | 12: groups run in parallel; the observation round covers only students still without an observed turn, and any mark still missing is taken live in an observation round before the respond day; the portfolio write-up moves to the respond day's close | 40 |
| 6 | 59 (run-through) | 58 | one run of the adapted piece | 8, replacing the second observation pass | 40 |
| 7 | 74 (trait and goal drill) | 75 | the drill as the critique day's opener; day 74's TH:Re8.1.7a line in day 75's close | 5: the drill is that day's warm-up | 40 |
| 7 | 93 (run-through) | 92 | one run of each staging | 8, replacing the second observation pass | 40 |
| 7 | 109 (run with presentation) | 108 | one run with the presentation and the observation round; day 109's TH:Re9.1.7a line in day 108's close | 12: groups run in parallel; the observation round covers only students still without an observed turn, and any mark still missing is taken live in an observation round before the respond day; the portfolio write-up moves to the respond day's close | 40 |
| 7 | 122 (transition drill) | 123 | the transition drill as the opener; day 122's TH:Re8.1.7b line in day 123's close | 5: the drill is that day's warm-up | 40 |
| 8 | 138 (bodily-response drill) | 139 | the drill as the critique day's opener | 5: the drill is that day's warm-up | 40 |
| 8 | 157 (slot run-through) | 156 | one run of the four-minute slot and the observation round | 12: groups run in parallel; the observation round covers only students still without an observed turn, and any mark still missing (TH:Pr4.1.8a needs every student's observed turn) is taken live in an observation round before the respond day; the portfolio write-up moves to the respond day's close | 40 |
| 8 | 167 (cue-run drill) | 166 | the cue run after the step card | 10, replacing the second demonstration pass | 40 |
| 8 | 186 (polish drill) | 187 | the polish points run in the dress run; day 186's 5-minute retrieval opens day 187 and its TH:Re8.1.8b line goes in day 187's close | 8, replacing the second observation pass | 40 |

Total: 12 folds save 480 minutes of the frame's 192 x 40 = 7,680, leaving 180 sessions and 7,200 minutes (60 a year, 2,400 minutes). A folded day's second-touch line goes with the folded work into the neighbor's close. The minimum is four fold-in days a year, the twelve above; no spares are listed beyond them. The checks keep their school days; the saved sessions are gaps inside the units' weeks, never a reason to move a check earlier. A school losing more than four sessions in a year uses the once-a-week merges below for the rest, rehearsal merges first.

**The once-a-week path (32 sessions a year).** Every unit and every id is kept by merging the days marked here, in the frame's order and no fewer: study and the demonstration with a step card, rehearsal with the critique and the revision, the showing check, a separate written check and a respond session that starts from marks already made. Fluency days fold into the openers; a merged session never drops a critique, a revision or a respond day. S1 holds the hook and the compelling question clean: each unit's retrieval task (day 2's opener) opens S2 in units with two study sessions, or the first rehearsal session in units with one, never S1; day 2's own teaching stays where the table puts it. Sessions by unit: 9, 7, 6, 6 a year, plus 1 check and 1 respond session for each course check (mid-year check week 17, respond week 18; year-end check week 31, respond week 32).

| Unit | Study and demonstration | Rehearsal, critique and revision | Showing | Written | Respond |
|---|---|---|---|---|---|
| 1 | S1: 1, 2, 3, 8; S2: 4, 6, 9 | S3: 5, 7; S4: 10, 11; S5: 12, 13; S6: 14, 15 | S7: 16 | S8: 17 | S9: 18 |
| 2 | S1: 19, 20, 21; S2: 22, 23, 25 | S3: 24, 26; S4: 27, 28, 29 | S5: 30 | S6: 31 | S7: 32 |
| 3 | S1: 35, 36, 37, 42 | S2: 38, 40, 41, 43; S3: 39, 44, 45 | S4: 46 | S5: 47 | S6: 48 |
| 4 | S1: 49, 50, 51, 54 | S2: 52, 53, 55; S3: 56, 57, 58, 59 | S4: 60 | S5: 61 | S6: 62 |
| 5 | S1: 65, 66, 67, 73; S2: 68, 70, 71 | S3: 69, 72; S4: 74, 75; S5: 76, 77; S6: 78, 79 | S7: 80 | S8: 81 | S9: 82 |
| 6 | S1: 83, 84, 85; S2: 86, 89 | S3: 87, 88, 90; S4: 91, 92, 93 | S5: 94 | S6: 95 | S7: 96 |
| 7 | S1: 99, 100, 101, 106 | S2: 103, 104, 105, 107; S3: 102, 108, 109 | S4: 110 | S5: 111 | S6: 112 |
| 8 | S1: 113, 114, 115, 117, 118 | S2: 116, 119, 120; S3: 121, 122, 123 | S4: 124 | S5: 125 | S6: 126 |
| 9 | S1: 129, 130, 131, 137; S2: 132, 134, 135 | S3: 133, 136; S4: 138, 139; S5: 140, 141; S6: 142, 143 | S7: 144 | S8: 145 | S9: 146 |
| 10 | S1: 147, 148, 151; S2: 149, 150, 153 | S3: 152, 154, 155; S4: 156, 157 | S5: 158 | S6: 159 | S7: 160 |
| 11 | S1: 163, 164, 165, 166, 171 | S2: 167, 169, 170, 172; S3: 168, 173 | S4: 174 | S5: 175 | S6: 176 |
| 12 | S1: 177, 178, 179, 180 | S2: 181, 183, 184; S3: 182, 185, 186, 187 | S4: 188 | S5: 189 | S6: 190 |

The study sessions are full: on this path each study day is taught in short form, about ten minutes, with the written understanding work on the step and research cards, so no reader should take the path for the full course. A moved day keeps its order relative to what needs it (on unit 3's path the criteria card, day 39, still comes before any written judgment). The design units (3, 7, 11) still put a making day, a tech rehearsal and a critique into one or two sessions; the frame's split is the lead's call (For the lead item 1). The unit plan times them.

## For the lead

1. **The once-a-week split (frame layer, expert read finding 1).** Even after the fix pass's moves, the design units (3, 7, 11) put a making day, a tech rehearsal and a critique into one or two sessions. Either change the year's split to 8, 7, 7, 6 (unit 1 gives up its lone revision session; the design unit gets a session for the making alone), or the frame says plainly that on the once-a-week path the study days are taught in short form, about ten minutes each. This scope already says the second; the frame wording is in the fix report's structure pass.
2. **Course-check sampling (L107). Closed.** The six checks sample 18 of 72 ids; the other 54 are named above with the reason, which is enough where the frame's check table limits the sample (lead call, 2026-11-26).
3. **Calendar. Closed.** frame.py calendar passes; the check days share school days only with the other arts electives, which CALENDAR.md rule 3 counts as one.
4. **Unit 11 has no run-through day.** Its six ids need six teaching and study days inside the frame's 14, so the final observation round sits in the revision day (173). No resize asked.
5. **Source pages not opened in this job.** Every work's page (the Safety Last! archive copy, Yuyachkani, Bread and Puppet, Ishioka, Taki Rua, the commedia print, the Gupta coin, the kabuki print, Devlin, Spiderwoman Theater, Kamiriithu, Stanislavski and Spolin pages, the Brecht production pages, the Yuan painting, the Globe, Arena Stage, Ilbijerri, Boal, Woza Albert!, Native Voices) is for the unit plan to open and record with its rights line; none was fetched here.
