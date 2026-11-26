# Scope and sequence: Dance, grades K to 2

Course `dance-grades-k-to-2` (catalogue id `dance-k-2`), a band course for kindergarten, grade 1 and grade 2; draft, written 2026-11-26 from the frame (docs/courses/dance-grades-k-to-2/frame.md). The days are in data/plans/dance-grades-k-to-2/days.csv; this page gives the judgment behind them.

## First page

- **Which grade's standards fall in which year** (STANDARD.md 3.1). The band runs as three years one after another. Year K (course days 1 to 64) claims only the 21 kindergarten dance ids (`.Ka`, `.Kb`, `.Kc`); year 1 (days 65 to 128) only the 21 grade 1 ids; year 2 (days 129 to 192) only the 21 grade 2 ids: 63 in all, the count in STANDARD.md 3.2, each taught and assessed in its own year. No pre-kindergarten id is claimed. A year revisits the year before's ids as practice that returns, never as a claim.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year still claims only its grade's ids, so a child's record shows which grade's standards they met. Where a child meets year 2 before year 1, each day 2 retrieval task becomes a ten-minute reteach of the earlier steps of both threads (APPROACH "Readiness and the baseline look").
- **Meeting days and `school_day`.** Two 40-minute sessions a week, 32 weeks a year, 64 course days a year, 96 weeks over the band. `school_day` counts school days across the band: year K is school days 1 to 160, year 1 is 161 to 320, year 2 is 321 to 480 (scripts/frame.py reads each 160 as one year's calendar under its grade). Inside a year, course day m of that year sits in week ceil(m / 2); the odd day of the week falls on the week's second school day and the even day on its fourth (a Tuesday and Thursday pattern; a school may use any two days). As one formula: for band course day n in year y (0 for K, 1, 2) with m = n - 64y, `school_day` = 160y + 5(ceil(m / 2) - 1) + 2 when m is odd, + 4 when m is even; the week inside the year is (school_day - 160y - 1) // 5 + 1. Every unit and check sits in the frame's weeks by it. A filled `school_day` is what frame.py reads, so it is not re-counted to frame.py's even spread or to calendar.csv, which the lead regenerates at commit (lead call 8, 2026-11-26).
- **The session.** Set-up 3 minutes (tables back, floor checked, spots marked), warm-up 5, teaching and dancing, cool-down and the closing line 4, room back 3. A day with a retrieval task (day 2 of every unit) runs set-up 3, warm-up 5, retrieval 10, teaching 15, cool-down 4, room back 3. Showing and watching days follow the frame's Scored evidence timings, copied into each check day's note.
- **Kinds of day** follow GLOSSARY "teaching day" and APPROACH "Kinds of day". Each unit runs understanding, fluency, application, the critique on an application day, the rehearsal of the change, the showing, two check days (unit 10: one) and one respond day. The artistic process "responding" lives on understanding days; a respond day only acts on a check.
- **The four processes.** Each year has all four (create; perform, present or produce; respond; connect), and each unit claims only the processes its frame row names, on its owned ids; the other processes are touched as practice on existing days and claim no id. A unit need not claim all four (lead call 2, 2026-11-26).
- **Day counts.** 192 days: 180 in the twelve units (20, 14, 14, 12; 18, 14, 14, 14; 18, 14, 14, 14), 12 course-level days (six check days, six respond days). No unit is over 25 days, so no unit holds a mid-unit assessment.
- **No readiness check in this course.** Year K assumes no earlier dance learning (its eight threads have empty `assumes`). Every year 1 and year 2 row assumes the year before's row in its thread, last used one grade back, so it opens with a retrieval task on day 2 of its unit (rule 2, by grade number). No day carries `assess` = `readiness`. The full list is under "Readiness and retrieval".
- **Equipment, space and safety** go in the day notes where the frame names them (hand drum or a pot and wooden spoon, floor tape or chalk, soft props). Rules for every day: a floor cleared and checked, bare feet or soft-soled shoes, spots an arm's length apart, no lifts, no jumping from heights, no inverted moves, partner contact only by agreement, the freeze cue every session. Jumps, landings and soft stamping use a resilient floor the school confirms; on an unsuitable floor they are done low and without impact and marked met only in a suitable space. Every unit gets the fresh safety (moving) and sensitivity reads with its unit plan.
- **No child dances alone.** Every showing is in a group of five; a child may dance beside the teacher or a partner, show at the teacher's spot, or take a seated, one-limb, caller's or drummer's version, which counts only for what it shows. The home room has a solo-with-parent version of every showing.

### Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; a cleared floor; step cards, work cards, symbol and idea cards; a drum or the voice | Moves and elements taught in named steps; dances watched with their setting; making and rehearsing with one critique and a change a unit; a showing each unit | A portfolio folder of 12 pieces over the band with one-line reflections; 12 unit showings; two marks a unit per child on the main look-for (the baseline look and the check) | Met marks on each year's 21 ids, and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that dance study raises any other result.

## Year K (kindergarten ids, course days 1 to 64, school days 1 to 160)

21 ids: DA:Cr1.1.Ka, Cr1.1.Kb, Cr2.1.Ka, Cr2.1.Kb, Cr3.1.Ka, Cr3.1.Kb, Pr4.1.Ka, Pr4.1.Kb, Pr4.1.Kc, Pr5.1.Ka, Pr5.1.Kb, Pr5.1.Kc, Pr6.1.Ka, Pr6.1.Kb, Re7.1.Ka, Re7.1.Kb, Re8.1.Ka, Re9.1.Ka, Cn10.1.Ka, Cn10.1.Kb, Cn11.1.Ka.

### Unit 1. My body, our space

- **Calendar.** Course days 1 to 20, weeks 1 to 10.
- **Arc.** The dance space and the freeze cue come first (days 1 to 3), then copying patterns with matching and crossing moves (4 to 6), body parts in relation and recall after the demonstration stops (7, 8), shapes, levels, sizes and the group circle (9 to 11), speed to the drum and the three qualities (12 to 14), and a class-made shapes-and-speeds game made, critiqued and changed (15 to 17).
- **Why this order.** Every later day needs the stop cue and own space, so they open the unit and the band; copying needs the space; recall needs moves already learned; the elements follow the technique because the class game uses both. Technique days come before the making days that use them. Load: the unit owns six ids and every routine is new, so the technique ids get 8 days and the element ids 6, with 3 making days.
- **Assessments.** Baseline look on day 3. Day 18 (end, showing): Pr5.1.Ka, Kb, Kc, one look-for per part (pattern in place then traveling; travel and stop in own space; body part to body part, then a recalled move). Day 19 (end, showing, a partner class invited): Pr4.1.Ka, Kb, Kc (straight and curved, high and low, big and small, the circle grown and shrunk; speed to a slow and a fast drum; quick, floppy, sharp). Response time: respond day 20.
- **Processes.** Perform: every day. Respond (touched, no claim): days 1 and 13 (the Serpentine film), 9 (Noumenon). Create (touched): days 15 to 17. Connect (touched): days 1 and 9, each work with its maker, place and date.
- **Candidate.** Criterion 9 on the set-up and room-back minutes in a classroom with tables pushed back: kept, 0 days; day 1 practices the 3-minute set-up and 3-minute room back as a routine, and every day's minutes include them.
- **Once a week (9 sessions).** 1 to 3; 4 to 8; 9 to 11; 12 to 14; 15; 16 and 17; 18; 19; 20.

### Unit 2. Dances from ideas

- **Calendar.** Course days 21 to 34, weeks 11 to 17.
- **Arc.** Starting points (a picture, music, objects) on days 21 and 22, new ways to travel and stay with one element changed (23, 24), the start-middle-finish shape and feelings (25 to 27), and animal dances made, run, critiqued, changed and shown to a partner class (28 to 31).
- **Why this order.** Changing an element needs unit 1's elements card (retrieved on day 22); a three-part dance needs moves from starting points first; the animal dance uses all four ids.
- **Assessments.** Baseline look on day 24. Day 32 (end): Cr1.1.Ka (moves that show the drawn card) and Cr1.1.Kb (a travel and a stay, then changed in speed or size). Day 33 (end): Cr2.1.Ka (held start, middle, held finish) and Cr2.1.Kb (the card's feeling shown, alone or with a partner). Response time: respond day 34.
- **Processes.** Create: every day. Perform: every warm-up, days 29 to 33. Respond: days 21, 22 (the peacock dance, the Saint-Saens music), 30 (critique). Connect: day 21 (the dance's Dai setting).
- **Candidate.** A doubled parent-and-child version of the partner feeling dance for the home room: kept, 0 days, named on days 26 and 33.
- **Once a week (7 sessions).** 21 to 24; 25 to 27; 28 and 29; 30 and 31; 32; 33; 34.

### Year K mid-year check (course days 35 and 36, week 18)

See "Course-level checks".

### Unit 3. Watch, tell and change

- **Calendar.** Course days 37 to 50, weeks 19 to 25.
- **Arc.** Watching first: the fan dance and the tap piece, the move that comes back, moves shown, easy dance words and a move that stood out (37 to 41); then changing: the suggestion card on the unit 2 dance and a drawn symbol (42 to 44); then the changed dance made, critiqued, changed and the kept symbol card finished (45 to 47).
- **Why this order.** The dance words come from unit 1 (retrieved on day 38) and are needed before describing; a change needs the child's own unit 2 dance (relearned on day 42); watching first lets the class see repeats and changes in another artist's work before making its own.
- **Assessments.** Baseline look on day 44. Day 48 (end, showing): Cr3.1.Ka (the dance, then with the teacher's suggested change), Re9.1.Ka (a show item and one talk item), Cr3.1.Kb (the kept card from day 47, scored after). Day 49 (end, watching, an unseen Curio Class phrase): Re7.1.Ka, Re7.1.Kb (show items), Re8.1.Ka (one talk item). Response time: respond day 50.
- **Processes.** Respond: days 37 to 41, 48, 49. Create: 42 to 47. Perform: 45 to 48. Connect: 37 and 38 (each work's place, maker and date).
- **Candidate.** A third short dance by a living maker from Africa, for range in year K: kept, 0 days, watched on the look-and-say practice day 41 (year K otherwise has no African work); the unit plan picks it and checks its rights line.
- **Leave-out fallback.** A class that left out unit 2 learns a short Curio Class original sequence on day 42 instead.
- **Once a week (6 sessions).** 37 to 39; 40 to 43; 44 to 47 (the critique and the rehearsed change together); 48; 49; 50.

### Year K year-end check (course days 51 and 52, week 26)

See "Course-level checks".

### Unit 4. Our dance for families

- **Calendar.** Course days 53 to 64, weeks 27 to 32.
- **Arc.** The umbrella dance and the like-me line (53), the marked dance area (54), the Matisse painting and a question (55), one prop (56), moves from a dance watched or done (57), then the family dance built, critiqued, changed and run (58 to 61).
- **Why this order.** The family dance is built from units 2 and 3 (retrieved on day 54), so it needs the space and the prop first; the connecting items are taught on days that study a work and practiced on the dress run, before the teacher's-spot check. The year-end check (week 26) comes before this unit, so the family showing is its own assessment, outside the core checks of weeks 29 to 32.
- **Assessments.** Baseline look on day 58. Day 62 (end, at the teacher's spot): Cn10.1.Ka (one talk item; the invented child's line marked the same), Cn10.1.Kb (a show item and one talk item), Cn11.1.Ka (a show item). Day 63 (end, the family showing): Pr6.1.Ka, Pr6.1.Kb (look-fors). Response time: respond day 64.
- **Processes.** Perform: 54, 56, 58 to 61, 63. Connect: 53, 55, 57, 62. Respond (review): 53, 55. Create: 58.
- **Candidate.** The doubled solo-with-parent version of the family dance for the home room: kept, 0 days, named on days 58 and 63.
- **Once a week (6 sessions, as the frame now sets).** 53 to 55 (the umbrella dance, the marked area, the painting); 56 to 58 (the prop, recalled moves, the dance begun); 59 to 61 (making, critique and the change rehearsed in the same session); 62; 63; 64.

## Year 1 (grade 1 ids, course days 65 to 128, school days 161 to 320)

21 ids: DA:Cr1.1.1a, Cr1.1.1b, Cr2.1.1a, Cr2.1.1b, Cr3.1.1a, Cr3.1.1b, Pr4.1.1a, Pr4.1.1b, Pr4.1.1c, Pr5.1.1a, Pr5.1.1b, Pr5.1.1c, Pr6.1.1a, Pr6.1.1b, Re7.1.1a, Re7.1.1b, Re8.1.1a, Re9.1.1a, Cn10.1.1a, Cn10.1.1b, Cn11.1.1a.

### Unit 5. Lines, circles and paths

- **Calendar.** Course days 65 to 82, weeks 1 to 9 of year 1.
- **Arc.** The space reopened and many ways to travel and stay still (65, 66), formations and changes on the call (67 to 69), paths, facing and returning to a spot (70, 71), three speeds and a steady beat (72, 73), quality words (74, 75), then a paths-and-formations dance made, critiqued, changed and shown (76 to 79).
- **Why this order.** After the summer the space and cue come back first; formations need own space; paths need formations to end in; the quality words named here are the words unit 7's responses use. Load: six ids in 15 teaching days: 5 technique days (the routines return from year K), 6 element days and 4 making days.
- **Assessments.** Baseline look on day 69. Day 80 (end): Pr5.1.1a, 1b, 1c. Day 81 (end): Pr4.1.1a (each path, level, facing, the return to the spot, the line or circle), Pr4.1.1b (a look-for and one talk item), Pr4.1.1c (a show item and one talk item). Response time: respond day 82.
- **Processes.** Perform: every day. Respond (touched): 65, 67, 74 (Carmencita, folklórico). Create (touched): 76 to 78. Connect (touched): 65, 67 (each work's place and date).
- **Candidate.** A dance in lines and circles from Africa or Asia beside folklórico: dropped; year 1 already studies Ghana and India in unit 7 and China in unit 8, and a third work would take a teaching day the six ids need.
- **Once a week (9 sessions).** 65 and 66; 67 to 69; 70 and 71; 72 to 75; 76; 77 to 79; 80; 81; 82.

### Unit 6. Where dances begin

- **Calendar.** Course days 83 to 96, weeks 10 to 16.
- **Arc.** Starting points named (83, 84), an element changed on purpose (85, 86), a sequence with a told choice and moves for a feeling or the music (87 to 89), then starting-point dances made, critiqued, changed and shown (90 to 93).
- **Why this order.** An element change on purpose needs unit 5's paths, levels and speeds (recalled on day 85); a told choice needs a sequence; the remembered sequence unit 7 changes is made here.
- **Assessments.** Baseline look on day 86. Day 94 (end): Cr1.1.1a (a look-for and one talk item), Cr1.1.1b. Day 95 (end): Cr2.1.1a (a look-for and one talk item), Cr2.1.1b. Response time: respond day 96.
- **Processes.** Create: every day. Perform: 93 to 95. Respond: 83, 87, 91. Connect: 83, 87 (Ailey's childhood songs; Khan's family story, each with its place and date).
- **Candidate.** A second starting-point dance with no religious source, for a school that leaves out Revelations: kept, 0 days; that school opens day 83 with Chotto Desh and uses a Curio Class poem-and-picture card on day 87, so every id stays met.
- **Once a week (7 sessions).** 83 and 84; 85 and 86; 87 to 89; 90 to 93; 94; 95; 96.

### Year 1 mid-year check (course days 97 and 98, week 17)

See "Course-level checks".

### Unit 7. Patterns and meanings

- **Calendar.** Course days 99 to 112, weeks 18 to 24.
- **Arc.** Watching: Kpanlogo's pattern and style (99, 100), Bharatanatyam gestures that stand for ideas (101), eye-catching moves (102), practice (103); changing: suggested changes to the remembered unit 6 sequence and symbols for jump, turn and slide (104 to 106); the changed sequence made, critiqued, changed and the kept card finished (107 to 109).
- **Why this order.** Quality words from unit 5 carry the descriptions (retrieved on day 102); moves that stand for ideas come before unit 8's story; the remembered sequence must exist (unit 6) before it changes.
- **Assessments.** Baseline look on day 107, the first making day (not day 104, where the skill is first taught, nor fold-in day 106). Day 110 (end, showing): Cr3.1.1a (a suggested change tried in a short improvisation and in the remembered sequence), Re9.1.1a (a show item and one talk item: what makes the move interesting, and why the dancer might have picked it), Cr3.1.1b (the kept card from day 109). Day 111 (end, watching): Re7.1.1a, Re7.1.1b (a show item and one talk item), Re8.1.1a (one talk item). Response time: respond day 112, where the pairs not retrying rehearse the unit 5 dance for the year-end check.
- **Processes.** Respond: 99 to 103, 111. Create: 104 to 110. Perform: 107 to 110. Connect: 99, 100 (the Ga people and Accra in the 1960s), 101.
- **Candidate.** The Bharatanatyam piece confirmed non-devotional from its teacher's own published words: kept, 0 days, done in the unit plan before day 101; if it cannot be confirmed, Kpanlogo keeps every id met (leave-out line).
- **Leave-out fallback.** A class that left out unit 6 learns a Curio Class original sequence on day 104.
- **Once a week (6 sessions).** 99 to 101; 102 to 105; 106 to 109 (the critique and the rehearsed change together); 110; 111; 112.

### Year 1 year-end check (course days 113 and 114, week 25)

See "Course-level checks".

### Unit 8. Dancing a story for an audience

- **Calendar.** Course days 115 to 128, weeks 26 to 32.
- **Arc.** The ribbon dance's movement types (115), the Peter Rabbit pictures and big ideas, danced (116, 117), a familiar experience (118), a seated audience (119), props tried and judged (120), then the story dance built from units 6 and 7, run, critiqued, changed and dress-run (121 to 125).
- **Why this order.** A second culture's dance comes first because the dance-two-ties model starts here; the story's big ideas come before staging them; props are judged only once the dance exists.
- **Assessments.** Baseline look on day 122. Day 126 (end, at the teacher's spot): Cn10.1.1a, Cn11.1.1a (talk items, one move shown). Day 127 (end, the family showing): Pr6.1.1a, Pr6.1.1b (a look-for and one spoken line), Cn10.1.1b. Response time: respond day 128.
- **Processes.** Connect: 115 to 118, 125, 126. Perform: 119 to 127. Respond: 115. Create: 121.
- **Candidate.** The ribbon dance's source confirmed as a Chinese cultural body's own teaching: kept, 0 days, done in the unit plan before day 115.
- **Once a week (6 sessions).** 115 to 117; 118 to 121; 122 to 125 (the critique and the rehearsed change together); 126; 127; 128.

## Year 2 (grade 2 ids, course days 129 to 192, school days 321 to 480)

21 ids: DA:Cr1.1.2a, Cr1.1.2b, Cr2.1.2a, Cr2.1.2b, Cr3.1.2a, Cr3.1.2b, Pr4.1.2a, Pr4.1.2b, Pr4.1.2c, Pr5.1.2a, Pr5.1.2b, Pr5.1.2c, Pr6.1.2a, Pr6.1.2b, Re7.1.2a, Re7.1.2b, Re8.1.2a, Re9.1.2a, Cn10.1.2a, Cn10.1.2b, Cn11.1.2a.

### Unit 9. Pathways and strong beats

- **Calendar.** Course days 129 to 146, weeks 1 to 9 of year 2.
- **Arc.** Pathways (129, 130), spatial relationships (131), repeating aware of others and fixing spacing (132, 133), direction and symmetry (134), circling and turning, facing (135), phrases and count groups (136), strong beats with tinikling (137, 138), quality words chosen (139), then a pathways dance made, critiqued, changed and shown (140 to 143).
- **Why this order.** Pathways and spacing first, since every later dance travels; shapes and facing before phrases; strong beats and phrases here because unit 10's linked phrase needs them.
- **Assessments.** Baseline look on day 133. Day 144 (end): Pr5.1.2a, 2b, 2c (including one spacing fix made unasked). Day 145 (end): Pr4.1.2a (a look-for and a show item on two shape cards), Pr4.1.2b (each part: strong beats in two and three, short and long phrases, phrase start and end with the count groups; one talk item), Pr4.1.2c (one talk item). Response time: respond day 146.
- **Processes.** Perform: every day. Respond (touched): 129, 131, 137. Create (touched): 140 to 142. Connect (touched): 129, 137 (Swan Lake's Russia of 1895; tinikling's Philippines).
- **Candidate.** A dance by a living maker from Africa with clear pathways: kept, 0 days, watched on day 131 (year 2's only other African work is Kpanlogo revisited); the unit plan picks it.
- **Once a week (9 sessions).** 129 and 130; 131 to 133; 134 and 135; 136 to 138; 139 and 140; 141 to 143; 144; 145; 146.

### Unit 10. The heart of a dance

- **Calendar.** Course days 147 to 160, weeks 10 to 16.
- **Arc.** Starting points and a growing inspiration list (147, 148), moves linked into a phrase with one element changed (149, 150), the central idea in the middle and a clear ending (151), moves chosen with a reason (152, 153), then each child's linked phrase made, the idea card begun, critiqued, changed and the card finished (154 to 158).
- **Why this order.** Linking needs unit 9's phrases and strong beats (recalled on day 149); a central idea needs a linked phrase; unit 11 changes this phrase.
- **Assessments.** Baseline look on day 150. Day 159 (end, the one showing day): Cr1.1.2b, Cr2.1.2a, Cr2.1.2b (a look-for and one talk item), and Cr1.1.2a in both parts: moves that show the card's starting point (a look-for in the phrase) and the kept idea card's two more idea places (made on day 158, scored after). Response time: respond day 160.
- **Processes.** Create: every day. Perform: 157 to 159. Respond: 147, 149, 156. Connect: 147, 149 (Graham's 1930 dance; Ito's 1916 dance and life).
- **Candidate.** A dance by a living maker whose idea came from a place or a story: kept, 0 days, heard about on day 148 as one more idea source (unit 10's two works are by makers who died).
- **Once a week (7 sessions).** 147 and 148; 149 and 150; 151 to 153; 154 and 155; 156 to 158; 159; 160.

### Year 2 mid-year check (course days 161 and 162, week 17)

See "Course-level checks".

### Unit 11. Styles, clues and choices

- **Calendar.** Course days 163 to 176, weeks 18 to 24.
- **Arc.** Watching: breaking's building footwork (163), flamenco and two styles (164), clues to meaning and purpose (165), what makes flamenco work well (166), practice (167); changing: a chosen and a suggested change to the recalled unit 10 phrase and level symbols (168 to 170); the changed phrase made, critiqued, changed and the level card finished (171 to 173).
- **Why this order.** Patterns that build need unit 9's phrases (retrieved on day 165); the recalled phrase is unit 10's (recalled on day 168); two styles watched with their settings come before unit 12's people and place.
- **Assessments.** Baseline look on day 171, the first making day (not day 168, where the skill is first taught). Day 174 (end, showing): Cr3.1.2a, Re9.1.2a (one talk item), Cr3.1.2b (the kept card from day 173). Day 175 (end, watching): Re7.1.2a, Re7.1.2b (a show item and one talk item), Re8.1.2a (one talk item). Response time: respond day 176, where the pairs not retrying rehearse the unit 9 pathways dance for the year-end check.
- **Processes.** Respond: 163 to 167, 175. Create: 168 to 174. Perform: 171 to 174. Connect: 163, 164 (the Bronx in the 1970s; Andalusia and the Roma people).
- **Candidate.** A third style from Asia or Africa for the two-styles item: dropped; breaking and flamenco meet the item, year 2 has Asia in unit 9 and Africa in unit 12, and the 11 teaching days hold six ids.
- **Leave-out fallback.** A class that left out unit 10 learns a Curio Class original sequence on day 168.
- **Once a week (6 sessions).** 163 to 165; 166 to 169; 170 to 173 (the critique and the rehearsed change together); 174; 175; 176.

### Year 2 year-end check (course days 177 and 178, week 25)

See "Course-level checks".

### Unit 12. Where dances come from

- **Calendar.** Course days 179 to 192, weeks 26 to 32.
- **Arc.** The hoop dance watched with its people and place (179), Kpanlogo revisited (180), set questions on a Kpanlogo excerpt with an original move (181), a personal dance (182), separate zones (183), staging extras (184), then the staged dance built from units 10 and 11, the extra readied, critiqued, changed and dress-run (185 to 189).
- **Why this order.** Origins first, since the unit's question is where dances come from; the personal dance before staging so it can be staged; the year-end check (week 25) sits before this unit and the family showing is its own assessment.
- **Assessments.** Baseline look on day 185, the first build in the zones (not day 183, where the zones are first taught). Day 190 (end, at the teacher's spot): Cn10.1.2b (a show item and one talk item), Cn11.1.2a (one talk item). Day 191 (end, the family showing): Pr6.1.2a, Pr6.1.2b, Cn10.1.2a (a look-for and one spoken line). Response time: respond day 192.
- **Processes.** Connect: 179 to 182, 189, 190. Perform: 183 to 191. Respond: 179, 181. Create: 182, 185.
- **Candidate.** The hoop dance's teaching confirmed from a Native-run source beside the museum's pages, and the Kpanlogo excerpt confirmed suitable for children: both kept, 0 days, done in the unit plan before days 179 and 181.
- **Once a week (6 sessions).** 179 to 181; 182 to 185; 186 to 189 (the critique and the rehearsed change together); 190; 191; 192.

## Course-level checks

Every check day is a showing day in groups of five (40 minutes: set-up 3, warm-up 5, six groups of about 4 minutes, cool-down and self-check 5, room back 3), each child with at most one talk or show item after the group's turn, followed by one respond day that asks no test of any child. All sit on the weeks CALENDAR.md lists for this course, off every core check week (K 14 to 17 and 29 to 32; grade 1 14 to 16, 19 and 29 to 32; grade 2 14 to 16, 18 to 20, 28, 29, 31, 32). Arts are specials in K to 5 and do not count against the classroom teacher's stagger.

| Check | Course days (school days) | Week | Live sample (retention) | Reused from the unit record, not collected again |
|---|---|---|---|---|
| Year K mid-year | 35 check, 36 respond (87, 89) | 18 | DA:Pr5.1.Kb, Pr4.1.Kb, Pr4.1.Ka, Pr5.1.Kc (unit 1), each part a look-for: travel and freeze on the drum; a new slow and fast tempo; a straight, high, big and a curved, low, small shape and the circle grown and shrunk; body part to body part, then a recalled unit 1 move | DA:Cr1.1.Ka, Cr2.1.Ka (days 32, 33) |
| Year K year-end | 51 check, 52 respond (127, 129) | 26 | DA:Cr1.1.Ka (a new picture card), Pr4.1.Kc (a quality on the called word), Cr2.1.Kb (a new feeling card, alone or paired), all look-fors | DA:Cr3.1.Ka, Re8.1.Ka (days 48, 49) |
| Year 1 mid-year | 97 check, 98 respond (242, 244) | 17 | DA:Pr4.1.1a (curved and zigzag paths with shape, level and facing changes, a line then a circle), Pr5.1.1c (a layout and a move changed on the call), Pr4.1.1b (quick, medium and slow; a steady beat as the tempo changes) | DA:Cr2.1.1a (day 95) |
| Year 1 year-end | 113 check, 114 respond (282, 284) | 25 | DA:Cr1.1.1b (the unit 5 dance with a traveling and an in-place move each changed), Cr2.1.1b (moves for a new feeling card or the music), Re7.1.1a (the one show item: the repeating move in a folklórico pattern from unit 5's work card) | DA:Cr3.1.1a (day 110) |
| Year 2 mid-year | 161 check, 162 respond (402, 404) | 17 | DA:Pr4.1.2b (strong-beat landings in a new three-beat piece; short or long clapped phrase as the one show item), Pr5.1.2c (aware of others, a move and a position adjusted on request), Pr4.1.2a (clear direction, a symmetrical and an uneven shape, circling then turning) | DA:Cr2.1.2a (day 159); math's mid-year check is week 18 |
| Year 2 year-end | 177 check, 178 respond (442, 444) | 25 | DA:Cr1.1.2b (moves of the unit 9 pathways dance linked into a new phrase with one element changed), Cr2.1.2b (moves for a new mood card or the music, the reason as the one talk item) | DA:Cr3.1.2a, Re8.1.2a (days 174, 175) |

Each check's ids of the unit just ended are reused from that unit's record and never collected again (rule 2, Collect once; lead call 7); the live sample is drawn from the units before it, on new cards, a new piece or an earlier unit's work. Each is a showing on earlier-unit work with its own items, which meets rule 2's two-week rule (lead call 6). The year-end checks begin with a warm-up run of the earlier dance they use, rehearsed on the unit's respond day (days 112 and 176). Day 177 samples two ids live, not three: Cr2.1.2b's reason is each child's one talk item, so Re8.1.2a (a talk item, scored on day 175) stays reused.

**Codes no course-level check samples live** (Cory 2026-11-24, later.csv L107; lead call 3), and why: 18 of the 63 ids are sampled live (7 in year K, 6 in year 1, 5 in year 2), so 45 are not. Year K: Pr5.1.Ka, Cr1.1.Kb, Cr2.1.Ka and Cr3.1.Ka (reused), Cr3.1.Kb, Re7.1.Ka, Re7.1.Kb, Re8.1.Ka (reused), Re9.1.Ka, Pr6.1.Ka, Pr6.1.Kb, Cn10.1.Ka, Cn10.1.Kb, Cn11.1.Ka. Year 1: Pr5.1.1a, Pr5.1.1b, Pr4.1.1c, Cr1.1.1a, Cr2.1.1a and Cr3.1.1a (reused), Cr3.1.1b, Re7.1.1b, Re8.1.1a, Re9.1.1a, Pr6.1.1a, Pr6.1.1b, Cn10.1.1a, Cn10.1.1b, Cn11.1.1a. Year 2: Pr5.1.2a, Pr5.1.2b, Pr4.1.2c, Cr1.1.2a, Cr2.1.2a, Cr3.1.2a and Re8.1.2a (all three reused), Cr3.1.2b, Re7.1.2a, Re7.1.2b, Re9.1.2a, Pr6.1.2a, Pr6.1.2b, Cn10.1.2a, Cn10.1.2b, Cn11.1.2a. Reasons: a 40-minute showing day watched group by group holds three or four look-fors and one talk or show item a child; the ids of the unit just ended are reused, not collected again; the year-end check comes before each year's performance unit (the core checks fill weeks 29 to 32), so the Pr6 and Cn ids of units 4, 8 and 12 are assessed only by their own family showings; kept cards (Cr3 symbols, Cr1.1.2a) are not remade on a check day; talk-heavy response ids (Re8, Re9, Cn10) would need a second talk item a child. Every one of these ids still has its own end-of-unit item and a baseline look. The frame's check table limits the sample; a change to it is under "For the lead".

## Readiness and retrieval

Every earlier-grade row a unit assumes, with its last use (counted by grade number; the band's order K, then 1, then 2) and its treatment. No row is two or more grades back, so no readiness check is owed.

| Unit | Earlier row | Last used | Treatment |
|---|---|---|---|
| 1 to 4 (year K) | none (pre-kindergarten not taught) | | none |
| 5 | da-k-technique, da-k-elements | year K (unit 1) | retrieval, day 66 |
| 6 | da-k-ideas, da-k-form | year K (unit 2) | retrieval, day 84 |
| 7 | da-k-revise, da-k-respond | year K (unit 3) | retrieval, day 100 |
| 8 | da-k-stage, da-k-connect | year K (unit 4) | retrieval, day 116 |
| 9 | da-g1-technique, da-g1-elements | year 1 (unit 5) | retrieval, day 130 |
| 10 | da-g1-ideas, da-g1-form | year 1 (unit 6) | retrieval, day 148 |
| 11 | da-g1-revise, da-g1-respond | year 1 (unit 7) | retrieval, day 164 |
| 12 | da-g1-stage, da-g1-connect | year 1 (unit 8) | retrieval, day 180 |

Same-year rows a unit builds on are retrieved where first needed, in the `retrieves` column: da-k-elements (days 22, 38), da-k-form (42, 54), da-k-revise (54), da-g1-elements (85, 102), da-g1-form (104, 121), da-g1-revise (121), da-g2-elements (149, 165), da-g2-form (168, 185), da-g2-revise (185). Each year 1 and 2 retrieval task is ten minutes after the warm-up on day 2, and day 1 of every unit stays clean for the hook and the compelling question.

## Leans on the calendar

- **Physical education K to 2** (data/plans/calendar.csv). Kindergarten: physical education unit 1 (weeks 1 to 6) and unit 2 (weeks 6 to 10) teach traveling and in-place moves as motor skill in the same weeks as dance unit 1; the frame's "if later" bridge is on days 2 and 4: the dance days use only moves a kindergartner already makes and teach only the dance technique, assuming no physical education cue. Kindergarten physical education unit 7, "Moving and feeling" (weeks 29 to 32), follows dance unit 2's feeling dances (weeks 11 to 17): dance teaches first, named only. Grade 1: physical education unit 8, "Ways to travel" (weeks 1 to 4), teaches traveling, paths and speed as motor skill in the same weeks as dance unit 5; days 66 and 70 use the traveling as material for paths and formations, teach only the dance words, and use physical education's cue words where the school's teacher has taught them. Dance unit 5 teaches before physical education unit 13 (weeks 23 to 27). Grade 2: physical education unit 15, "Circuit sequences" (weeks 1 to 4), links a travel, a jump and a balance in the same weeks as dance unit 9's pathways and sequences; day 130 carries the same bridge. Dance units 9 and 10 (weeks 1 to 16) teach before physical education unit 21 (weeks 24 to 26). Computer science grade 2 units 2 and 3 (weeks 7 to 20) build programs from dance cards; that lean is computer science's to bridge, and dance year 2 asks nothing of it.
- **Math K to 2.** Counting the beat (days 12, 72, 136, 137): the class counts aloud and claps, no number written or added, to 4 in years K and 1 and in twos and threes in year 2. Symmetry (day 134) is "the same on both sides" with the body and a folded shape; symmetry as math is grade 4 (4.G.A.3).
- **ELA K to 2.** Talk and critique practice collaborative conversation (SL.K.1, SL.1.1, SL.2.1), not owned; the first critique (day 16) uses the picture talk-rules card in case ELA has not taught them. Day 116 practices retelling key details (RL.1.2), not owned.
- **Social studies K to 2.** Unit 12's people and place sits near grade 2's family stories and culture; no lean either way, and no child is asked to explain their own family's culture.

## Shorter path

- **The once-a-week path** (32 sessions a year, the frame's). Each unit's merges are in its "Once a week" line: year K units of 9, 7, 6 and 6 sessions, years 1 and 2 of 9, 7, 6 and 6, and each check keeps 1 check session and 1 respond session. Check sessions fall in the same weeks as the full path (K weeks 18 and 26; years 1 and 2 weeks 17 and 25), respond sessions one week later. Every merged session keeps the watch of a work, the step-card demonstration, a rehearsal with the critique, the showing and the respond day; fluency days fold into the warm-ups. No session holds more than four teaching days or two works. On the once-a-week path the retrieval task runs in the unit's first session, after the hook and the question.
- **A year about 10 school days short** loses about 4 sessions at two a week. Four fold-in days a year (lead call 1: 10 school days is about 4 sessions at two a week), each a fluency day with no baseline look, no candidate work, nothing assessed and no owned part cut, whose practice folds into the next day's warm-up: year K days 6, 11, 14, 27; year 1 days 73, 89, 103, 106; year 2 days 138, 153, 167, 170. Day 41 is not one, since it carries year K's only African work. Each saves 40 minutes: 160 minutes a year, 480 over the band, leaving 180 of the frame's 192 days.

## For the lead

1. **Course-level checks sample 18 of 63 ids live** (L107). The 2026-11-26 fix pass rewrote the frame's check table so each check reuses the just-ended unit's record and samples the units before it live (sequence read finding 1). A further frame change could add a second course-level form (a short talk round on another day) to sample the response and connecting ids; the Pr6 and Cn ids of units 4, 8 and 12 cannot be sampled while the year-end check sits before those units.
2. **Checks right after a unit, and the two-week task-form rule.** Settled by the read (finding 1) and lead calls 6 and 7: the unit's ids are reused, and the live sample is a showing on earlier-unit work with its own items.
3. **Shared weeks with other specials.** The frame's For the lead 1 lists the check weeks shared with other specials and ELD; specials do not count for the K to 5 stagger, so nothing moves here.
