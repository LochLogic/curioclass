# Scope and sequence: Media Arts, grades 9 to 12

Course `media-arts-grades-9-to-12`, grades 9 to 12, run as Levels 1 to 4 (Level 4 optional), 640 course days, 19 units; draft scope and sequence, 2026-11-26, from the frame of 2026-11-25. The days live in data/plans/media-arts-grades-9-to-12/days.csv; this page holds the judgment.

## How this file is counted

- **Levels and ids.** Each level is a full year of 160 days, taken in turn. Level 1 (days 1 to 160) claims the 18 Proficient ids (`.I`, `.Ia` and so on); Level 2 (days 161 to 320) claims the 18 Accomplished ids (`.II`, `.IIa` and so on); Level 3 (days 321 to 480) claims the 18 Advanced ids (`.III`, `.IIIa` and so on); Level 4 (days 481 to 640) claims no new id: eleven Level 3 ids re-assessed on new, self-directed work (MA:Cr1.1.III, MA:Cr2.1.III, MA:Cr3.1.IIIa, MA:Pr5.1.IIIa, MA:Re7.1.IIIa, MA:Re8.1.III, MA:Re9.1.III, MA:Cn11.1.IIIa, MA:Cn10.1.IIIa, MA:Pr4.1.III, MA:Pr6.1.IIIa). No grade 8 id is claimed; the bridge teaches grade 8 techniques as readiness only. Ids are named, never quoted; their lines are in data/standards/ncas-performance-standards-words.txt.
- **stretch** is the unit number in the frame's Units table; `C` marks a course-level check or respond day. **unit** is `<unit>.1` (no unit is split into sections yet).
- **school_day is blank.** Grades 9 to 12 media arts meets five 45-minute sessions a week, every school day, so course day n is the band's school day n (sequence-write.md). `frame.py calendar` splits the band's 640 days into four 160-day years. Within a level, the level day is the course day minus 160 times (level minus 1), and the level week is (level day - 1) // 5 + 1, the one formula used for every unit and check in this file (checked by script: every unit and check sits in the frame's weeks). school_day stays blank, so it is counted inside each level (1 to 160), since the levels are taken in separate years. So every level's mid-year check falls on level days 77 and 78 (week 16) and its year-end check on level days 157 to 160 (week 32, the finals week).
- **Day shape.** Set-up about 3 minutes, clean-up and wiping shared devices about 5; a retrieval or readiness task 10. A sitting is 3 + 30 + 5 + 2 = 40 of 45 minutes; a screening of six teams of five is 5 + 24 + 5 + 5 = 39. A showing of one piece per student never runs in turn in one period: units 4, 9 and 14 screen in four small-group circles of about seven (5 + 25 + 5 + 5 = 40), units 15 and 19 show as an exhibition that visitors walk (set-up, walk, cards, take-down), and unit 18 shows across a window; in each the look-fors are scored from the kept piece and the audience or note cards after the session, never live. The tool-use look-for (MA:Pr5.1.Ic, IIc, IIIc) is observed for ten students a session, about 90 seconds each, across the last three production sessions, never on a check day.
- **Technique before making; critique and revision before every scored showing.** In every unit the technique days (Understanding, with the step card) come before the first making day that needs them; each made piece meets a critique (describe, ask, suggest) and a logged revision before its end-of-unit showing, and making and showing units carry two critique stages. In Level 4 checkpoints are check days and critiques are respond days (APPROACH).
- **The four processes.** Each level claims all four (create; perform, present or produce; respond; connect). A unit claims the processes the frame names for it, and the unit's "Processes, by day" line lists only days where students do that process; practice of another process on an existing day (a short response, a setting card) costs no day and claims no id. No day carries an id outside its unit's owned rows (checked by script).
- **Notes carry** equipment, hazards and controls and the free path on each making day (from the frame's last column), every sensitivity flag the frame names (units 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14 and 15, and the self-chosen subjects of Level 4), the short-path merge, and the fold-in days of a short year. No tools, supplies or safety columns are added (math and science only).
- **ELA bridge.** The paragraph frame (claim, evidence from the piece, reasoning) is taught on the first study day of each reading unit (days 14, 168 and 328); the critique card's turn rules are modeled on each level's first critique day; the defended talk (unit 17) leans on SL.11-12.4.

## Logic model

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| One 45-minute lesson a day, five a week; step cards, work cards, case cards; paper media tools and found objects; an optional shared device per team | Technique taught in steps; works studied with their setting; making in production roles with a critique and a revision; a showing or a sitting each unit; a screening or showing that ends each level | A portfolio of five pieces a level (four in Level 4, plus the series) with reflections, logs and plans; two marks a unit per student on the main look-for | Met marks on the level's 18 ids (Level 4: the eleven re-assessed ids on new work) and growth on the look-fors. Nothing here has been tried with students, and Curio Class claims no effect of arts study on any other result |

## Retrieval and readiness by row (rule 2)

Each unit's day 2 opener holds a 10-minute retrieval task on the row the unit's own row builds on; the `retrieves` column names it. Level 1 retrieves grade 8 rows (last used in Media Arts, grades 6 to 8); Levels 2 to 4 retrieve the level before's rows, last used a year earlier. Readiness: unit 1's check (day 1, after the hook) samples ma-g8-read, ma-g8-ideas, ma-g8-craft and ma-g8-judge; units 6 and 11 give the frame's readiness check in the last ten minutes of their day 1 (in the note; see For the lead).

| Unit | Day | Rows retrieved |
|---|---|---|
| 2 | 14 | ma-g8-read; ma-g8-society |
| 3 | 44 | ma-g8-ideas; ma-g8-craft |
| 4 | 80 | ma-g9-ideas; ma-g8-make |
| 5 | 118 | ma-g8-present; ma-g8-sources |
| 7 | 168 | ma-g9-read; ma-g9-society |
| 8 | 200 | ma-g9-ideas; ma-g9-craft |
| 9 | 240 | ma-g9-make; ma-g9-judge |
| 10 | 278 | ma-g9-present; ma-g9-sources |
| 12 | 328 | ma-g10-read; ma-g10-society |
| 13 | 360 | ma-g10-ideas; ma-g10-craft |
| 14 | 400 | ma-g10-make; ma-g10-judge |
| 15 | 438 | ma-g10-present; ma-g10-sources |
| 16 | 482 | ma-g11-ideas; ma-g11-make; ma-g11-craft |
| 17 | 530 | ma-g11-read; ma-g11-judge |
| 18 | 560 | ma-g11-society; ma-g11-sources |
| 19 | 600 | ma-g11-present |

## Level 1 (Proficient), days 1 to 160

Claims the 18 Proficient ids (`.I`, `.Ia` and so on). Units 1, 2, 3, 4, 5, then the mid-year check on days 77 and 78 (week 16) and the year-end check on days 157 to 160 (week 32).

### Unit 1. The bridge: frames, shots and a crew

*What does a media maker need to know before the first real piece?*

- **Days:** 1 to 12 (12 days), Level 1 weeks 1 to 3.
- **Arc:** The bridge. Day 1 is the hook on Méliès and the readiness check; days 2 to 10 reteach the eight Level 1 cards (shot set, storyboard and workflow, roles, media-ethics check, source log, critique card, revision log, screening plan) as readiness only, each used once on a six-shot team sequence; day 11 screens it unscored and fills the bridge record; day 12 responds.
- **Why here:** First because Level 1 assumes no earlier media arts learning and every later unit uses the eight models (STANDARD.md 3.2: Level 1 opens with a bridge of at most 12 days). Short because it teaches only the grade 8 tools Level 1 needs, at their first step.
- **Assessment days:** day 1 (readiness, in the note): the readiness check after the hook; day 1 (readiness): Hook; day 11 (end): Bridge check. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the picture-only form of the readiness check is ready on day 1 for a student new to English.
- **Processes, by day:** Create 2 to 4, 6, 9, 12; Produce or present 5 to 8, 10 to 11; Respond 1 to 4, 8, 11 to 12; Connect 5.
- **Short path (6 days):** 1; 2+3+4+5; 6+7; 8+9+10; 11; 12.

### Unit 2. Who gets shown, and how

*How do media makers' choices give or take power, and what does that mean for the people in the frame?*

- **Days:** 13 to 42 (30 days), Level 1 weeks 3 to 9.
- **Arc:** Three makers read for who gets shown (Curtis, Romero, Salgado), then the senses, then a mid-unit sitting; then media and power, the legal and career sides on case cards, and a made "Who gets shown?" six-image sequence with a critique and a revision before the gallery, the sitting and the written evaluation.
- **Why here:** After the bridge because analysis uses its shot words and look-describe-interpret steps; first of the level's paired units because reading media and its power comes before making for an audience, and unit 3's ideas start from the questions raised here. The media-ethics check grows here to digital identity before any team production in unit 3.
- **Assessment days:** day 23 (mid): Mid-unit sitting; day 39 (end): End-of-unit showing; day 40 (end): End-of-unit sitting; day 41 (end): End-of-unit written evaluation. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the unseen clip on the end sitting, day 40, is a Curio Class original, so its rights are certain.
- **Processes, by day:** Create 30 to 35; Produce or present 31, 34, 38 to 39; Respond 13 to 25, 32, 37, 40, 42; Connect 13, 15 to 16, 25 to 30, 35 to 36, 39, 41 to 42.
- **Short path (15 days):** 13; 14+15; 16+17+18; 19+20+21+22; 23; 24+25; 26+27+28; 29+30+31; 32; 33+34; 35+36+37+38; 39; 40; 41; 42.

### Unit 3. Moon shots: ideas and a crew

*How do media makers find an idea and a way to make it, and what does a risk buy them?*

- **Days:** 43 to 76 (34 days), Level 1 weeks 9 to 16.
- **Arc:** Idea methods and three studio works (Patel, Kentridge, Brakhage, plus the kept Asian maker) teach the combined technique before any making; two prototypes (the first in erase-and-redraw only, the second open to cutouts and strip marks once days 51 and 52 have shown them) and the planning portfolio meet the mid-unit checkpoint; then the team moon shot is made by roles with two critique stages and two revisions, and screened on day 75.
- **Why here:** After unit 2 because its questions about who is shown feed the ideas, and the media-ethics check is in place before a team captures anything. Before unit 4 because a piece refined to the student's own goals needs a prototype and the habit of a log first. The longest unit before mid-year: five ids and the level's first team production.
- **Assessment days:** day 57 (mid): Mid-unit checkpoint; day 75 (end): End-of-unit screening. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 1 day (a studied-work day inside the 34): a hand-made animation by an Asian maker, because Level 1 otherwise has no Asian maker; the unit plan picks it and checks its rights line.
- **Processes, by day:** Create 43 to 48, 50, 53 to 58, 61, 66, 73, 76; Produce or present 49 to 55, 59 to 76; Respond 43, 47, 51 to 52, 60, 65, 75; Connect 43, 47.
- **Short path (17 days):** 43; 44+45+46; 47+48; 49+50; 51+52+53; 54; 55+56; 57; 58+59; 60; 61+62+63; 64+65; 66+67+68+69; 70+71; 72+73+74; 75; 76.

### Unit 4. Tone and emphasis

*How does a maker make a piece feel the way they mean it to, and how do we judge it while it is still being made?*

- **Days:** 79 to 116 (38 days), Level 1 weeks 16 to 24.
- **Arc:** Emphasis, tone and the sound bed are shown on Martel, Faye and a radio piece before the student's own image-and-sound piece is planned; reception reading runs beside the making; the rough cut carries the first written critique (mid-unit), and three revisions, each logged with the goal or the taste it serves, lead to the screening in four small-group circles, the second critique and the sitting.
- **Why here:** After mid-year and unit 3 because tone and emphasis are worked on a piece of the student's own, after a team prototype taught the log and standards. Before unit 5 because the collection needs finished pieces, and judging at production stages comes before judging a showing.
- **Assessment days:** day 96 (mid): Mid-unit written critique one; day 112 (end): End-of-unit screening; day 113 (end): End-of-unit written critique two; day 115 (end): End-of-unit sitting. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 1 day (the sound-bed technique day): a public domain radio piece beside the two films, for the sound sense.
- **Processes, by day:** Create 79 to 80, 82 to 84, 88 to 95, 98, 100 to 102, 104 to 106, 108, 110, 116; Produce or present 89, 93 to 94, 100, 102, 106, 108, 110 to 112; Respond 79, 81, 84 to 87, 90, 95 to 97, 99, 103 to 104, 107, 109, 112 to 116; Connect 81, 85 to 86, 99, 103, 115.
- **Short path (18 days):** 79; 80+81; 82+83+84; 85+86+87; 88+89; 90; 91+92+93; 94+95; 96; 97+98; 99+100+101+102; 103+104+105; 106+107+108; 109+110+111; 112; 113+114; 115; 116.

### Unit 5. A collection for two audiences

*How can media weave many sources and forms into one showing, and how does media build culture?*

- **Days:** 117 to 156 (40 days), Level 1 weeks 24 to 32.
- **Arc:** Blending forms, the audience moment and the source log come first; the team piece meets the mid-unit source check; then the collection is curated for two audiences, screened to a younger class, reviewed and improved, screened to families, and written up on its own day.
- **Why here:** Last in Level 1 because the collection is built from the level's pieces and the new team piece, and the showing ends the level before the year-end check in week 32. The source log, kept since the bridge, is weighed here for the first time.
- **Assessment days:** day 129 (mid): Mid-unit checkpoint; day 150 (end): End-of-unit screening one; day 154 (end): End-of-unit screening two; day 155 (end): End-of-unit written account. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Dropped for now, 0 days either way: the frame's Candidate itself allows the family showing in a community partner's space where the school allows it, with every yes, and unit 18 already allows a community space the school allows, so the reason is not the frame. Cory decided 2026-11-26 (DESK-ANSWERS): the Level 1 family showing stays in the school's own space with the school's own adults, the free path (a sheet or wall for a screen, printed programs, a live sound score).
- **Processes, by day:** Create 123 to 126, 128, 135, 137 to 138, 140, 143, 147, 152; Produce or present 117 to 118, 122, 124, 127 to 128, 131 to 133, 135 to 136, 138 to 141, 143, 145, 147 to 154, 156; Respond 117, 119, 125, 134, 136, 146, 150 to 151, 155; Connect 119 to 121, 123, 129 to 130, 134, 142, 144, 155 to 156.
- **Short path (20 days):** 117; 118+119; 120+121+122; 123+124; 125; 126+127+128; 129; 130+131; 132+133+134; 135+136; 137+138+139+140; 141+142+143+144; 145+146+147; 148+149; 150; 151; 152+153; 154; 155; 156.

## Level 2 (Accomplished), days 161 to 320

Claims the 18 Accomplished ids (`.II`, `.IIa` and so on). Units 6, 7, 8, 9, 10, then the mid-year check on days 237 and 238 (week 16) and the year-end check on days 317 to 320 (week 32).

### Unit 6. Review and placement: back in the edit

*What do we carry from Level 1, and where does each of us start?*

- **Days:** 161 to 166 (6 days), Level 2 weeks 1 to 2.
- **Arc:** Review and placement. Day 1 ends with the readiness check (in the note, see For the lead); days 2 and 3 reteach in groups from it; day 4 makes a 30-second piece; day 5 shows it, unscored for Level 2 ids, and scores each placing student on the placement guide; day 6 responds and records placement.
- **Why here:** First in Level 2 because a level requires the one before or a placement (STANDARD.md 3.2), and the review doubles as that placement. At most 6 days.
- **Assessment days:** day 161 (readiness, in the note): the readiness check after the hook; day 165 (end): Review showing. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the placement guide, written from Level 1's year-end check items, scores placing students on day 165.
- **Processes, by day:** Create 162, 164, 166; Produce or present 162 to 165; Respond 161, 163, 165 to 166; Connect 161.
- **Short path (3 days):** 161+162+163; 164+165; 166.

### Unit 7. Persuasion and truth

*How does media sell, rally and persuade, and how can it tell the truth about what was hidden?*

- **Days:** 167 to 198 (32 days), Level 2 weeks 2 to 8.
- **Arc:** Posters and persuasion (the war posters, El Lissitzky, the kept African maker), then the senses with Guzmán, then the mid-unit poster sitting; then commerce, truth and the case cards, and a two-sided persuasive piece with its truth panel, critiqued and revised before the gallery, the sitting and the written route.
- **Why here:** After the review because analysis and the media-ethics check pick up where Level 1's unit 2 left them; first of the level's paired units because unit 8's interactive piece and unit 10's persuasive piece both need the study of persuasion and audience interaction first.
- **Assessment days:** day 179 (mid): Mid-unit sitting; day 195 (end): End-of-unit showing; day 196 (end): End-of-unit sitting; day 197 (end): End-of-unit written route. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 1 day: a persuasive work by a living African maker, because Level 2 otherwise has no African maker.
- **Processes, by day:** Create 186 to 191; Produce or present 187, 190, 194 to 195; Respond 167 to 181, 188, 193, 196, 198; Connect 167, 169 to 170, 177, 181 to 186, 191 to 192, 195, 197 to 198.
- **Short path (16 days):** 167; 168+169; 170+171+172; 173+174+175+176; 177+178; 179; 180+181; 182+183+184; 185+186+187; 188; 189+190; 191+192+193+194; 195; 196; 197; 198.

### Unit 8. Fail, try again: making it interactive

*How does a team keep exploring after a test fails, and how can a viewer steer a piece?*

- **Days:** 199 to 236 (38 days), Level 2 weeks 8 to 16.
- **Arc:** Strategic idea methods, ink-wash tests (Te Wei) and the branching piece (Bear 71, then the branching steps on day 207) come before prototype one on day 208; logged failed tests and two prototypes meet the mid-unit checkpoint; the producer role rotates through ten production days with two critiques and revisions; another class plays the pieces on day 235.
- **Why here:** After unit 7 because the interactive piece uses audience interaction studied there; before mid-year so the managed production is assessed before the level's individual piece. Long because it owns five ids and the level's team production.
- **Assessment days:** day 214 (mid): Mid-unit checkpoint; day 235 (end): End-of-unit showing. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Dropped: unit 7 now carries an African maker and unit 10 a Native maker (Skawennati), so Level 2's range holds.
- **Processes, by day:** Create 199 to 204, 208 to 215, 218, 223, 233, 236; Produce or present 205 to 212, 216 to 236; Respond 199, 203, 206 to 207, 217, 222, 235; Connect 199, 203.
- **Short path (19 days):** 199; 200+201+202; 203+204; 205+206; 207+208+209; 210+211; 212+213; 214; 215+216; 217; 218+219+220; 221+222; 223; 224+225; 226+227+228+229; 230+231; 232+233+234; 235; 236.

### Unit 9. Cut and contrast

*How do continuity and collision between shots make meaning, and how do we defend a judgment of a piece?*

- **Days:** 239 to 276 (38 days), Level 2 weeks 16 to 24.
- **Arc:** Juxtaposition (Eisenstein) and continuity (Dash) are shown and drilled before the student's own 2- to 3-minute piece; the defended evaluation is taught before the rough-cut test, which feeds the mid-unit checkpoint; three revisions for the chosen audience lead to the screening in four small-group circles, the critique and the sitting (four prompts, one per setting).
- **Why here:** After mid-year because the individual piece uses unit 8's prototype habits; before unit 10 because the theme piece needs continuity and a chosen audience first, and the defended evaluation feeds the showing's review.
- **Assessment days:** day 256 (mid): Mid-unit checkpoint; day 272 (end): End-of-unit screening for the chosen audience; day 273 (end): End-of-unit written critique; day 275 (end): End-of-unit sitting. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Dropped: Level 2's range is met (Chile, China, Soviet Russia, the Gullah Geechee Sea Islands, a living African maker, Kanien'kehá:ka, Brazil), and a third collision-cut work would cost a day of making.
- **Processes, by day:** Create 239 to 240, 242 to 244, 248 to 255, 258, 260 to 262, 264 to 266, 268, 270, 276; Produce or present 249, 253 to 254, 260, 262, 266, 268, 270 to 272; Respond 239, 241, 244 to 247, 250, 255 to 257, 259, 263 to 264, 267, 269, 272 to 276; Connect 241, 245 to 246, 259, 263, 275.
- **Short path (18 days):** 239; 240+241; 242+243+244; 245+246+247; 248+249; 250; 251+252+253; 254+255; 256; 257+258; 259+260+261+262; 263+264+265; 266+267+268; 269+270+271; 272; 273+274; 275; 276.

### Unit 10. A curated channel

*How do we curate a collection under one theme for an audience we cannot see, and what does it say about our culture?*

- **Days:** 277 to 316 (40 days), Level 2 weeks 24 to 32.
- **Arc:** Merging school-subject content under one theme (Skawennati, the Library of Congress exhibitions) and the inner and outer resources come first; the source log meets the mid-unit checkpoint; then the channel is curated, premiered in the school's space, reviewed and improved, and written up on the second check day.
- **Why here:** Last in Level 2 because the channel is curated from the level's pieces and the new theme piece, before the year-end check in week 32; persuasion from unit 7 and the defended evaluation from unit 9 feed the piece and the review.
- **Assessment days:** day 289 (mid): Mid-unit checkpoint; day 310 (end): End-of-unit premiere in the school's space; day 315 (end): End-of-unit written day. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: a school-subject partner teacher checks the theme pieces' content where one is free, outside class time (noted on the planning day).
- **Processes, by day:** Create 283 to 286, 288, 295, 297 to 298, 300, 303, 307, 312; Produce or present 277 to 278, 282, 284, 287 to 288, 291 to 293, 295 to 296, 298 to 301, 303, 305, 307 to 314, 316; Respond 277, 279, 285, 294, 296, 306, 310 to 311, 315; Connect 279 to 281, 283, 289 to 290, 294, 302, 304, 315 to 316.
- **Short path (20 days):** 277; 278+279; 280+281+282; 283+284; 285; 286+287+288; 289; 290+291; 292+293+294; 295+296; 297+298+299+300; 301+302+303+304; 305+306+307; 308+309; 310; 311; 312+313; 314; 315; 316.

## Level 3 (Advanced, at honors depth), days 321 to 480

Claims the 18 Advanced ids (`.III`, `.IIIa` and so on). Units 11, 12, 13, 14, 15, then the mid-year check on days 397 and 398 (week 16) and the year-end check on days 477 to 480 (week 32).

### Unit 11. Review and placement: the systems we work in

*What do we carry from Level 2, and how do media reach the whole world?*

- **Days:** 321 to 326 (6 days), Level 3 weeks 1 to 2.
- **Arc:** Review and placement for Level 3 on Hopinka's Kicking the Clouds. Day 1 ends with the readiness check (in the note); days 2 and 3 reteach; day 4 makes a short piece with a stated purpose; day 5 shows it and scores placing students on unit 6's placement guide form; day 6 responds.
- **Why here:** First in Level 3, the review that doubles as placement (STANDARD.md 3.2); its study piece opens unit 12's question of personal and worldwide purpose.
- **Assessment days:** day 321 (readiness, in the note): the readiness check after the hook; day 325 (end): Review showing. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: unit 6's placement guide form is reused against Level 2's year-end check and guides.
- **Processes, by day:** Create 322, 324, 326; Produce or present 322 to 325; Respond 321, 323, 325 to 326; Connect 321.
- **Short path (3 days):** 321+322+323; 324+325; 326.

### Unit 12. Many media, one world

*How do the best media works reach across systems and borders, and what purpose should our work serve?*

- **Days:** 327 to 358 (32 days), Level 3 weeks 2 to 8.
- **Arc:** Three kinds of work (Du Bois's charts, Varda, Mita) are synthesized before the student searches for top-quality examples; the mid-unit sitting follows; then purposes, the route map and the made essay piece with its critique and revision, ending with the showing, the written review of found examples and the route map.
- **Why here:** After the review; first of Level 3's paired units because the student-set problems of units 13 to 15 start from a purpose found here, and the route map sets the system unit 13 works within.
- **Assessment days:** day 339 (mid): Mid-unit sitting; day 355 (end): End-of-unit showing; day 356 (end): End-of-unit written review; day 357 (end): End-of-unit route map. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the Curio Class example list is ready on the search day for a student who finds none.
- **Processes, by day:** Create 346 to 351; Produce or present 347, 350, 354 to 355; Respond 327 to 341, 348, 353, 356, 358; Connect 327, 329 to 330, 341 to 346, 351 to 352, 355, 357 to 358.
- **Short path (16 days):** 327; 328+329; 330+331+332; 333+334+335+336; 337+338; 339; 340+341; 342+343+344; 345+346+347; 348; 349+350; 351+352+353+354; 355; 356; 357; 358.

### Unit 13. Systems and rules

*How can a set of rules or a system become the idea of a piece, and what question is the team really asking?*

- **Days:** 359 to 396 (38 days), Level 3 weeks 8 to 16.
- **Arc:** Design principles, rules and systems (Molnár, Lozano-Hemmer) come before the framework is proposed, tested and revised; the planning portfolio meets the mid-unit checkpoint; conventional and experimental versions are produced with two critiques (the second run team to team on day 382); both versions are shown side by side on day 395, with one innovative tool or method named in the experimental version.
- **Why here:** After unit 12 because the framework works inside a system the route map named; before mid-year so the team production is assessed before the hybrid piece. Long for five ids and the level's team production.
- **Assessment days:** day 374 (mid): Mid-unit checkpoint; day 395 (end): End-of-unit showing. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Dropped: Level 3 already has makers from Iran, Senegal, Mexico, Aotearoa New Zealand and Nunavut, and a third studied work would cost a production day the team piece needs.
- **Processes, by day:** Create 359 to 364, 366, 369 to 375, 378, 383, 386, 393, 396; Produce or present 365 to 369, 372, 376 to 385, 387 to 396; Respond 359, 363, 367 to 368, 377, 382, 395; Connect 359, 363.
- **Short path (19 days):** 359; 360+361+362; 363+364; 365+366; 367+368+369; 370+371; 372+373; 374; 375+376; 377; 378+379+380; 381+382; 383; 384+385+386; 387+388+389; 390+391; 392+393+394; 395; 396.

### Unit 14. Hybrids

*What happens when a piece joins forms that are not meant to meet, and how do we judge our own bias?*

- **Days:** 399 to 436 (38 days), Level 3 weeks 16 to 24.
- **Arc:** Hybridization (Neshat, Diop) and polish are shown before the student's hybrid is made; reception with bias runs beside the making; the rough-cut test is the mid-unit checkpoint; three revisions, the second of them after feedback from two chosen readers, lead to the screening in four small-group circles, the kept critique and the sitting.
- **Why here:** After mid-year because the hybrid uses unit 13's framework and toolset habits; before unit 15 because the cross-platform piece needs a hybrid made and judged first.
- **Assessment days:** day 416 (mid): Mid-unit checkpoint; day 432 (end): End-of-unit screening; day 433 (end): End-of-unit kept critique; day 435 (end): End-of-unit sitting. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Dropped: the same range reason as unit 13; Level 3 has Native makers in units 11, 12 and 15.
- **Processes, by day:** Create 399 to 400, 402 to 404, 408 to 415, 418, 420 to 422, 424 to 426, 428, 430, 436; Produce or present 409, 413 to 414, 420, 422, 426, 428, 430 to 432; Respond 399, 401, 404 to 407, 410, 415 to 417, 419, 423 to 424, 427, 429, 432 to 436; Connect 401, 405 to 406, 419, 423, 435.
- **Short path (18 days):** 399; 400+401; 402+403+404; 405+406+407; 408+409; 410; 411+412+413; 414+415; 416; 417+418; 419+420+421+422; 423+424+425; 426+427+428; 429+430+431; 432; 433+434; 435; 436.

### Unit 15. Across platforms, for real

*How do we make and promote a showing that changes something, and how do we know it did?*

- **Days:** 437 to 476 (40 days), Level 3 weeks 24 to 32.
- **Arc:** Holding a piece across three platforms (Isuma, Chalabi) and finding sources alone come first; the source log meets the mid-unit checkpoint; then the promoted showing is planned, held in the school's space as an exhibition of every student's piece (each piece made by its student, critiqued in pairs of students), its results read, an improvement folded into the second context, and the results day written.
- **Why here:** Last in Level 3 because the showing is built from the level's work and ends it before the year-end check in week 32; the purpose from unit 12 and the hybrid from unit 14 feed it.
- **Assessment days:** day 449 (mid): Mid-unit checkpoint; day 470 (end): End-of-unit promoted showing in the school's space, first context; day 475 (end): End-of-unit results day. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the effect check uses paper audience cards and attendance, never data from students' accounts or devices.
- **Processes, by day:** Create 443 to 446, 448, 455, 457 to 458, 460, 463, 467, 472; Produce or present 437 to 438, 442, 444, 447 to 448, 451 to 453, 455 to 456, 458 to 461, 463, 465, 467 to 474, 476; Respond 437, 439, 445, 454, 456, 466, 470 to 471, 475; Connect 439 to 441, 443, 449 to 450, 454, 462, 464, 475 to 476.
- **Short path (20 days):** 437; 438+439; 440+441+442; 443+444; 445; 446+447+448; 449; 450+451; 452+453+454; 455+456; 457+458+459+460; 461+462+463+464; 465+466+467; 468+469; 470; 471; 472+473; 474; 475; 476.

## Level 4 (Advanced, deepened; optional), days 481 to 640

Claims no new id: eleven Level 3 ids re-assessed on new, self-directed work, each on the Level 3 guide with a higher bar for independence. One self-directed series in four phases; checkpoints are check days and critiques are respond days. A school may offer Levels 1 to 3 only (480 days).

### Unit 16. The proposal and the series

*What series will I make, and how will I plan, make and revise it on my own?*

- **Days:** 481 to 528 (48 days), Level 4 weeks 1 to 10.
- **Arc:** The series proposal: a series and its makers, ideas and a framework, a paper prototype tested, a critique and a revision, then studio checkpoint one (mid-unit). Pieces one and two follow, each with a technique day, production, two critiques (respond days) and two revisions; studio checkpoint two shows the two pieces and scores the log.
- **Why here:** First in Level 4 because the series is the year's sustained project and every later unit adds to it. Longest unit in the band: the proposal and the first pieces of a self-led series.
- **Assessment days:** day 493 (mid): Studio checkpoint one; day 526 (end): Studio checkpoint two; day 527 (end): Studio log check. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the proposal guide is read on day 482.
- **Processes, by day:** Create 481 to 483, 485 to 489, 491, 493 to 496, 502, 505, 508 to 510, 516, 522 to 523, 528; Produce or present 488 to 489, 492, 495 to 500, 503 to 504, 506, 508 to 514, 517 to 520, 522 to 528; Respond 481, 484, 490, 501, 505, 507, 515, 521, 526; Connect 483 to 484.
- **Short path (24 days):** 481; 482+483; 484+485+486; 487+488+489; 490; 491+492; 493; 494; 495+496+497+498; 499+500; 501; 502+503; 504+505+506; 507+508; 509+510+511+512; 513+514; 515; 516+517; 518+519+520; 521+522; 523+524+525; 526; 527; 528.

### Unit 17. Reading the field

*Which reading of a set of works is the most believable, and how do I defend it?*

- **Days:** 529 to 556 (28 days), Level 4 weeks 10 to 16.
- **Arc:** Reading the field: three to four works near the series are chosen and cleared; comparison, criteria and bias are taught before the essay is drafted; the draft meets the mid-unit checkpoint; two readers' feedback and two revisions come before the talk notes and a 30-second evidence reel (day 549), then the defended talks with the reel shown, scored over the last four sessions in groups of 8, 8, 8 and 6.
- **Why here:** After unit 16 because the works chosen sit near the student's own series, which now exists; before mid-year so the defended reading informs the real-audience piece.
- **Assessment days:** day 539 (mid): Mid-unit checkpoint; day 552 (end): Defended talks, group 1; day 553 (end): Defended talks, group 2; day 554 (end): Defended talks, group 3; day 555 (end): Defended talks, group 4. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the essay guide with two levels of sample described is used on the criteria day.
- **Processes, by day:** Create 549 (the 30-second evidence reel cut from stills of the chosen work); Produce or present 552 to 555 (the reel shown inside each defended talk); Respond 529 to 556; Connect 530, 533. Essay drafting is responding, not creating, so it is not listed under Create.
- **Short path (14 days):** 529+530; 531+532+533+534; 535+536+537+538; 539; 540; 541+542; 543+544+545; 546+547+548; 549+550+551; 552; 553; 554; 555; 556.

### Unit 18. Work for a real audience

*How can my series speak to a real audience, and what do I owe the people and sources in it?*

- **Days:** 559 to 598 (40 days), Level 4 weeks 16 to 24.
- **Arc:** A piece for a real audience: the audience, purposes, ethics and consent plans come first, with a critique and a revision; the piece's technique is shown in steps with the adaptation for this audience named (day 570) before production one; the source log and the ethics account meet the mid-unit checkpoint; then production with two critiques and an audience test, the showing to its audience across a window (scored from the kept piece and audience cards), and the written day.
- **Why here:** After mid-year and the criticism unit, so the real-audience piece is made with the defended reading and the series in hand; before the showing, which the piece joins.
- **Assessment days:** day 575 (mid): Mid-unit checkpoint; day 594 (end): End-of-unit showing; day 597 (end): End-of-unit written day. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the audience and consent plan template is used on day 2.
- **Processes, by day:** Create 567, 569, 571, 573, 577 to 579, 581 to 585, 587 to 590, 593; Produce or present 564, 571 to 573, 577 to 579, 581 to 585, 587 to 590, 593 to 594; Respond 559, 568, 580, 586, 595, 598; Connect 559 to 566, 574 to 576, 591 to 592, 594 to 598.
- **Short path (20 days):** 559+560+561; 562+563+564; 565+566+567; 568; 569+570; 571+572+573+574; 575; 576+577; 578+579; 580; 581+582+583; 584+585; 586; 587+588; 589+590+591; 592+593; 594; 595+596; 597; 598.

### Unit 19. The series showing

*How do I show my series so its audience meets it as I mean, and what happened when they did?*

- **Days:** 599 to 636 (38 days), Level 4 weeks 24 to 32.
- **Arc:** The series showing: the plan, platforms and labels come first, with a critique; the plan meets the mid-unit checkpoint; set-up test and dress run each have a critique and a revision; the showing is an exhibition visitors walk (day 630, with a second half on day 631 where the room needs it), scored from the set-up and the kept series; the responses read and the written review (from day 632) and the respond day end the band before the year-end check.
- **Why here:** Last in the band because the showing gathers the whole year's series and ends the subject's threads before the year-end check in week 32.
- **Assessment days:** day 612 (mid): Mid-unit checkpoint; day 630 (end): End-of-unit series showing; day 634 (end): End-of-unit written day. What each scores is named in its goal in days.csv; end-of-unit evidence is the frame's, id by id.
- **Candidate settled:** Kept, 0 days: the showing checklist for a student working alone is given with the showing plan on day 2.
- **Processes, by day:** Create 609 to 611, 615, 617, 621; Produce or present 599 to 606, 608 to 618, 620 to 624, 626 to 630, 632, 634 to 636; Respond 599, 607, 619, 625, 630 to 636; Connect 599, 632.
- **Short path (18 days):** 599; 600+601+602+603; 604+605+606; 607; 608+609; 610+611; 612; 613+614; 615+616+617+618; 619; 620+621+622; 623+624; 625; 626+627+628+629; 630; 631+632+633; 634; 635+636.

## Course-level checks

| Level | Check | Days | Week | Samples |
|---|---|---|---|---|
| 1 | mid-year | check 77, respond 78 | 16 | MA:Re7.1.Ia; MA:Cr1.1.I |
| 1 | year-end | check 157, 158, respond 159, 160 | 32 | MA:Re7.1.Ib; MA:Re8.1.I; MA:Cn11.1.Ib; MA:Re9.1.I |
| 2 | mid-year | check 237, respond 238 | 16 | MA:Re7.1.IIa; MA:Cr1.1.II; MA:Cr2.1.II |
| 2 | year-end | check 317, 318, respond 319, 320 | 32 | MA:Re7.1.IIb; MA:Re8.1.II; MA:Cn11.1.IIb; MA:Re9.1.II |
| 3 | mid-year | check 397, respond 398 | 16 | MA:Re7.1.IIIa; MA:Cr2.1.III |
| 3 | year-end | check 477, 478, respond 479, 480 | 32 | MA:Re8.1.III; MA:Re7.1.IIIb; MA:Cn11.1.IIIb; MA:Re9.1.III |
| 4 | mid-year | check 557, respond 558 | 16 | MA:Cr2.1.III |
| 4 | year-end | check 637, 638, respond 639, 640 | 32 | MA:Pr5.1.IIIa; MA:Re9.1.III |

Each item set is fresh; a check right after a unit draws its planning brief from an earlier unit's content (Level 1 from unit 2, Level 2 from unit 7, Level 3 from unit 12, Level 4 from unit 17's works) so the unit just scored is not rerun. Records of the unit just ended are carried unscored, as the frame's table says. Grades 9 to 12 have no stagger rule beyond the finals week (CALENDAR.md rule 4): the year-end checks sit in week 32 and the mid-year checks in week 16 of every level.

**Which ids the course-level checks sample, and why the rest are not.**

| Level 1 id | Course-level check | If not sampled |
|---|---|---|
| MA:Re7.1.Ia | day 77 | |
| MA:Re7.1.Ib | day 157 | |
| MA:Cn11.1.Ia | not sampled | a made piece, scored on the unit's kept piece |
| MA:Cn11.1.Ib | day 158 | |
| MA:Pr5.1.Ib | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr1.1.I | day 77 | |
| MA:Pr5.1.Ic | not sampled | a tool-use id, observed over production sessions; never a check-day task |
| MA:Cr2.1.I | not sampled | scored on the unit's kept prototype and test record; a prototype cannot be rebuilt in a sitting |
| MA:Pr5.1.Ia | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr3.1.Ia | not sampled | scored on the unit's own finished piece and revision log |
| MA:Cr3.1.Ib | not sampled | scored on the unit's own finished piece and revision log |
| MA:Re8.1.I | day 157 | |
| MA:Re9.1.I | day 158 | |
| MA:Pr6.1.Ia | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr4.1.I | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.Ib | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.Ia | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr6.1.Ib | not sampled | the showing unit is assessed by its own showings and written day (frame) |

| Level 2 id | Course-level check | If not sampled |
|---|---|---|
| MA:Re7.1.IIa | day 237 | |
| MA:Re7.1.IIb | day 317 | |
| MA:Cn11.1.IIa | not sampled | a made piece, scored on the unit's kept piece |
| MA:Cn11.1.IIb | day 318 | |
| MA:Pr5.1.IIb | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr1.1.II | day 237 | |
| MA:Pr5.1.IIc | not sampled | a tool-use id, observed over production sessions; never a check-day task |
| MA:Cr2.1.II | day 237 | |
| MA:Pr5.1.IIa | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr3.1.IIa | not sampled | scored on the unit's own finished piece and revision log |
| MA:Cr3.1.IIb | not sampled | scored on the unit's own finished piece and revision log |
| MA:Re8.1.II | day 317 | |
| MA:Re9.1.II | day 318 | |
| MA:Pr6.1.IIa | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr4.1.II | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.IIb | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.IIa | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr6.1.IIb | not sampled | the showing unit is assessed by its own showings and written day (frame) |

| Level 3 id | Course-level check | If not sampled |
|---|---|---|
| MA:Re7.1.IIIa | day 397 | |
| MA:Re7.1.IIIb | day 477 | |
| MA:Cn11.1.IIIa | not sampled | a made piece, scored on the unit's kept piece |
| MA:Cn11.1.IIIb | day 478 | |
| MA:Pr5.1.IIIb | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr1.1.III | not sampled | scored at the unit's mid-unit checkpoint on the planning portfolio |
| MA:Pr5.1.IIIc | not sampled | a tool-use id, observed over production sessions; never a check-day task |
| MA:Cr2.1.III | day 397 | |
| MA:Pr5.1.IIIa | not sampled | a team production; it cannot be rerun in 45 minutes, so the unit's own log and screening score it |
| MA:Cr3.1.IIIa | not sampled | scored on the unit's own finished piece and revision log |
| MA:Cr3.1.IIIb | not sampled | scored on the unit's own finished piece and revision log |
| MA:Re8.1.III | day 477 | |
| MA:Re9.1.III | day 478 | |
| MA:Pr6.1.IIIa | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr4.1.III | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.IIIb | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Cn10.1.IIIa | not sampled | the showing unit is assessed by its own showings and written day (frame) |
| MA:Pr6.1.IIIb | not sampled | the showing unit is assessed by its own showings and written day (frame) |

Level 4: day 557 samples MA:Cr2.1.III; days 637 and 638 sample MA:Pr5.1.IIIa and MA:Re9.1.III, with the independence bar. The other eight re-assessed ids are scored in their own units (the showing, the talks and the real-audience piece cannot be rerun in 45 minutes).

## Shorter path

**The 80-day path (a semester or a rotation), per level.** It keeps every unit and every id by merging the days each unit section lists under "Short path" (a `+` joins days taught as one 45-minute day; days.csv notes each merged day with "Short path: folds into day N"). Unit lengths are the frame's, as fixed on 2026-11-26: Level 1 6, 15, 17, 18 and 20; Levels 2 and 3 3, 16, 19, 18 and 20; Level 4 24, 14, 20 and 18. Units 4, 9 and 14 fold their reception drill (days 114, 274, 434) into the written critique the day before as its 5-minute opener, and the day freed goes to units 5, 10 and 15, so the dress run stands with the consent work only (148+149, 308+309, 468+469) instead of inside a five-day merge. A mid-unit respond day shares its 45 minutes with at most one other day (24+25, 97+98, 130+131, 180+181, 257+258, 290+291, 340+341, 417+418, 450+451, 576+577), each unit's count kept by joining the next days as listed. Unit 16 splits its two five-day merges (502+503 and 504+505+506; 516+517 and 518+519+520) and keeps its 24 by pairing each second critique with its revision (507+508, 521+522); unit 18 keeps its 20 by joining its planning days (562+563+564, 565+566+567). On it each level's mid-year check is day 39 with respond day 40 (week 8), and the year-end check day 79 with respond day 80 (week 16, the half-year finals week), its two check days' items cut to one sitting. Pieces are shorter (a 60-second piece in place of 2 to 3 minutes, six frames in place of twelve), Fluency days fold into openers, and no merge drops a critique, a revision, a mid-unit checkpoint, a check day or a respond day. Two exceptions, both from the frame's figures: the review units (6 and 11) keep 3 days, so the short piece is made and shown on one day; unit 17 keeps its four talk days, so the essay shortens to about 600 words.

**A year 10 days short.** Each level names ten fold-in days, all Fluency days with nothing assessed and no owned part cut; each one's drill moves into the next day's opener as a 5-minute warm-up and saves 40 minutes, except days 114, 274 and 434, whose drill opens the written critique the day before (days 113, 273, 433), so the sittings on days 115, 275 and 435 keep their slack. Ten school days is ten course days here, since the course meets daily. Ten a level: 150 days against the frame's 160 (600 against 640 across the band).

- Level 1 fold-in days: 17, 21, 37, 46, 68, 92, 101, 114, 121, 139 (10 days, 400 minutes).
- Level 2 fold-in days: 171, 175, 185, 202, 227, 243, 252, 267, 281, 299 (10 days, 400 minutes).
- Level 3 fold-in days: 331, 335, 345, 362, 387, 403, 412, 427, 441, 459 (10 days, 400 minutes).
- Level 4 fold-in days: 486, 498, 512, 519, 544, 547, 550, 572, 583, 603 (10 days, 400 minutes).

Where seniors leave before week 32, the days that fold first are unit 5's, 10's, 15's or 19's merged short-path days (never a critique, a revision or a respond day), and the year-end check moves no earlier than the frame allows.

## For the lead

1. **Readiness on a level's first day (gate and frame differ; the expert read of 2026-11-26 agrees with the widening).** The frame puts the review units' readiness check in the last ten minutes of day 1 (days 161 and 321), because a student placing in or back after a year away is first present then; a check on the previous level's last day, a summer earlier, would miss them. sequence.py allows a first-day readiness check only on course day 1, so the check sits in those days' notes with `assess` blank. Pick: widen the gate's exception to the first day of a level (days 161, 321 and 481 here), then set `assess` to readiness on days 161 and 321.
2. **Unit 5 has three end days, not two.** The frame names two screenings, but its rule that a screening and a written task never share a day puts the written account (MA:Cn10.1.Ib, with the review completed for MA:Pr6.1.Ib) on its own day 155, inside the unit's 40. Units 10 and 15 instead keep the frame's two check days (the showing and the written or results day); their second showing is an Application day whose evidence is scored on the written day.
3. **Unit 5 Candidate (audience, for Cory).** The frame's Candidate moves the family showing to a community partner's space where the school allows it, with every yes, and unit 18 already allows such a space. Dropped (0 days either way): Cory decided 2026-11-26 that the Level 1 family showing stays in the school's own space with the school's own adults, on the free path (DESK-ANSWERS). Unit 18's community space is unchanged.
4. **Review units on the short path.** The frame sets 3 short days for units 6 and 11; with a check day and a respond day kept, the short piece is made and shown on the same day. Pick: keep, or allow 4 short days and take one from unit 7 or 12. The expert read of 2026-11-26 recommends 4 (161+162, 163+164, 165, 166; 321+322, 323+324, 325, 326) with units 7 and 12 folding their hook into the first study day (167+168+169, 327+328+329) and dropping to 15 short days; a frame change, left to the lead.
5. **Level 4 year-end statement.** Day 637's portfolio and statement carry MA:Pr5.1.IIIa and are scored with day 638's answers as one evidence set, so no artifact is scored twice. Pick: keep, or leave 637's codes blank.
6. **Supplies ceiling (money, for Cory).** The frame's item 5 stands unchanged: $90, $80, $80 and $60 a class a level, all optional beside a free path; this scope adds no supply.
7. **Facts to confirm at the unit plan.** Every work, date, holder and living status is the frame's, still unchecked on the holders' pages (frame item 6); the scope adds no new work beyond the kept Candidates, which the unit plans pick (an Asian hand-made animation for unit 3, a public domain radio piece for unit 4, a living African persuasive maker for unit 7).
