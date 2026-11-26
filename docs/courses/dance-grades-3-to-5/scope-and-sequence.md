# Scope and sequence: Dance, grades 3 to 5

Course `dance-grades-3-to-5` (catalog id `dance-3-5`), a band course for grades 3, 4 and 5. Draft, written 2026-11-26,
fixed the same day after the expert read (docs/reviews/sequence-dance-grades-3-to-5-fixes-2026-11-26.md),
from the frame (docs/courses/dance-grades-3-to-5/frame.md). The days live in data/plans/dance-grades-3-to-5/days.csv;
this page holds the judgment.

## On the first page

- **Which grade's standards fall in which year.** The band runs as three years one after another. Year 3 (course days
  1 to 64) claims only the 21 grade 3 dance ids (`DA:...3a` to `3c`); year 4 (days 65 to 128) only the 21 grade 4 ids;
  year 5 (days 129 to 192) only the 21 grade 5 ids: 63 in all, the count in docs/courses/arts/STANDARD.md 3.2, each
  taught and assessed in its own year. A year revisits the year before's ids as practice that returns, never as a
  claim. Standard: National Core Arts Standards, 2014, dance performance standards, named by id only.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a student's record shows which grade's standards they met. In a mixed class a
  student may meet year 5 before year 4; each day-2 retrieval task then carries its ten-minute reteach as written.
- **Meeting days.** Two 40-minute sessions a week, 32 weeks a year, 96 weeks over the band; never a daily period.
- **How `school_day` is counted.** One band-long count of 480 school days, 160 a year (year 3 is school days 1 to 160,
  year 4 is 161 to 320, year 5 is 321 to 480), the count scripts/frame.py reads. Course day n of a year (n = 1 to 64)
  falls in that year's week ceil(n / 2); the odd day of a week sits on its second school day and the even day on its
  fourth, so `school_day = 160 x (year index) + 5 x (week - 1) + 2 or 4`, and the week of the year is
  `(school_day - 160 x (year index) - 1) // 5 + 1`. Every unit day and check sits on the week the frame and
  docs/courses/CALENDAR.md give (checked day by day, 2026-11-26). This filled column wins over frame.py's even spread;
  data/plans/calendar.csv is regenerated from it by the lead, so it is not re-counted to match (lead calls 5 and 8).
- **Dance here, motor skill in physical education.** This course teaches the art; dance steps as motor skill are
  physical education's. Dance assumes no physical education instruction (units 1, 5 and 9 name the lean in day 1's
  connection).

## The calendar

| Year | Unit | Course days | Weeks of the year | Days |
|---|---|---|---|---|
| 3 | 1. Space, time and energy | 1 to 16 | 1 to 8 | 16 |
| 3 | 2. Where dances come from | 17 to 32 | 9 to 16 | 16 |
| 3 | Mid-year check and respond | 33, 34 | 17 | 2 |
| 3 | 3. Patterns, forms and styles | 35 to 50 | 18 to 25 | 16 |
| 3 | Year-end check and respond | 51, 52 | 26 | 2 |
| 3 | 4. Our dance on a stage | 53 to 64 | 27 to 32 | 12 |
| 4 | 5. Rhythm, balance and cues | 65 to 80 | 1 to 8 | 16 |
| 4 | 6. Dances from facts and places | 81 to 96 | 9 to 16 | 16 |
| 4 | Mid-year check and respond | 97, 98 | 17 | 2 |
| 4 | 7. Styles inside one genre | 99 to 114 | 18 to 25 | 16 |
| 4 | Year-end check and respond | 115, 116 | 26 | 2 |
| 4 | 8. Making a room a stage | 117 to 128 | 27 to 32 | 12 |
| 5 | 9. Rhythm from the body and the world | 129 to 145 | 1 to 9 | 17 |
| 5 | 10. Many sources, opposing themes | 146 to 162 | 9 to 17 | 17 |
| 5 | Mid-year check and respond | 163, 164 | 18 | 2 |
| 5 | 11. How dance speaks without words | 165 to 178 | 19 to 25 | 14 |
| 5 | Year-end check and respond | 179, 180 | 26 | 2 |
| 5 | 12. One dance, two spaces | 181 to 192 | 27 to 32 | 12 |

Each year: 60 unit days, 2 check days, 2 respond days (64). Units and their day counts are the frame's, unchanged.

## How every unit runs

- **Shape.** Day 1 is the hook: a dance watched, described and linked, the compelling question, and the room set; it
  carries no readiness check. Day 2 opens with the ten-minute retrieval task after the warm-up (set-up 3, warm-up 5,
  retrieval 10, teaching 15, cool-down 4, room back 3) and shows the first technique in steps with its step card.
  The first fluency day holds the baseline look at the unit's main look-for (the first of two marks; growth is the
  change). Technique and understanding days come before the making that needs them; the first application day makes,
  the second holds the unit's one critique (describe, ask, suggest), and the next day rehearses the change. Step
  cards are withdrawn before the check. The end-of-unit check days come next, then one respond day, which is the
  response time for every check day of the unit (counted once) and where the portfolio piece and its one-line
  reflection are kept.
- **Check days.** Units 1 to 3, 5 to 7 and 9 to 11 have two check days, the unit's third-last and second-last; unit
  12 has two showings (one per venue); units 4 and 8 have one showing day and kept cards scored after the session. A
  showing day and a written day are never mixed; their minute budgets are in each day's note and in the frame.
- **Mid-unit assessments.** None: no unit is over 25 days.
- **No student dances alone.** Every showing is in groups of five; seated, one-limb and role versions map to the same
  look-for.
- **Safety.** Every unit's day 1 note carries the hazards and controls; days with their own hazard (spins, jumps, found
  sound, outdoors, light, props) name it. Floor rule: jumps, landings and stamping only on a level, resilient surface
  the school confirms; otherwise low and without impact, and the look-for is seen in a suitable space before it is
  marked met. Equipment and the free path are in the notes where the frame lists them. Every unit gets the fresh
  safety and sensitivity reads with its unit plan.

## Readiness and retrieval (rule 2)

Every unit assumes the year before's row in its thread, last used one grade back, so every unit opens with a retrieval
task on day 2 (the `retrieves` column) and no unit has a readiness check. Counted by grade number:

| Unit | Earlier-grade rows assumed | Last used | Treatment |
|---|---|---|---|
| 1 | da-g2-technique, da-g2-elements | grade 2 (Dance K to 2 unit 9) | retrieval, day 2, with the by-course-order reteach |
| 2 | da-g2-ideas, da-g2-connect | grade 2 (Dance K to 2 units 10 and 12) | retrieval, day 18, with the reteach |
| 3 | da-g2-form, da-g2-respond | grade 2 (Dance K to 2 units 10 and 11) | retrieval, day 36, with the reteach |
| 4 | da-g2-revise, da-g2-stage | grade 2 (Dance K to 2 units 11 and 12) | retrieval, day 54, with the reteach |
| 5 | da-g3-technique, da-g3-elements | grade 3 (unit 1) | retrieval, day 66 |
| 6 | da-g3-ideas, da-g3-connect | grade 3 (unit 2) | retrieval, day 82 |
| 7 | da-g3-form, da-g3-respond | grade 3 (unit 3) | retrieval, day 100 |
| 8 | da-g3-revise, da-g3-stage | grade 3 (unit 4) | retrieval, day 118 |
| 9 | da-g4-technique, da-g4-elements | grade 4 (unit 5) | retrieval, day 130 |
| 10 | da-g4-ideas, da-g4-connect | grade 4 (unit 6) | retrieval, day 147 |
| 11 | da-g4-form, da-g4-respond | grade 4 (unit 7) | retrieval, day 166 |
| 12 | da-g4-revise, da-g4-stage | grade 4 (unit 8) | retrieval, day 182 |

Year 3 is a "by course order" seam: Dance, grades K to 2 is an after-core course a school may not have run, so each
year 3 retrieval task carries one ten-minute reteach of both threads' grade 2 steps together inside the same block,
and the unit's first understanding day teaches its grade 3 step from the start.

## The four processes, unit by unit

Each year claims all four processes, create (Cr), perform (Pr), respond (Re) and connect (Cn), through its units'
owned ids; each unit claims only its owned ids and works on at least the processes the frame names for it. A unit
need not claim all four. The table also names the days where a unit touches another process as practice (a watch, a
setting sentence, a short response); practice claims no id and costs no day (lead call 2). No day carries a code
outside its unit's owned rows (checked 2026-11-26). Days below are course days.

| Unit | Create | Perform | Respond | Connect |
|---|---|---|---|---|
| 1 | 7, 9, 11 (improvising, group choices) | every day | 1, 4, 12 | 1, 4 (the works' settings) |
| 2 | 18 to 20, 22, 25 to 28, 30 | 19, 25 to 28, 30 | 17, 21, 23, 24, 26 | 21, 23 to 25, 27, 29 to 31 |
| 3 | 36, 38, 39, 43 to 46, 48 | 41, 42, 44 to 46, 48 | 35, 37, 40, 41, 43, 47, 49 | 40, 41 (two traditions' settings) |
| 4 | 56 to 58, 60 to 63 | 54, 55, 59, 60, 62, 63 | 53, 59, 61 | 53, 59 (the Bauhaus stage, kabuki) |
| 5 | 71, 72, 75 | every day | 65, 70, 74, 76 | 65, 70 (bomba, legong settings) |
| 6 | 82 to 85, 89 to 91, 94 | 89 to 92, 94 | 81, 86, 87, 90 | 81, 86 to 89, 91, 93 to 95 |
| 7 | 100, 101, 107 to 110, 112 | 103, 104, 108 to 110, 112 | 99, 102, 103, 105, 106, 109, 111, 113 | 102, 105 (styles and settings) |
| 8 | 120 to 122, 124 to 126 | 118, 119, 123 to 127 | 117, 123, 125 | 117, 123 (Firebird, community stages) |
| 9 | 138, 140, 141 | every day | 129, 132, 135, 139 | 129, 132 (Stomp, sasa settings) |
| 10 | 147 to 150, 154 to 157, 160 | 154 to 160 | 146, 151, 152, 155 | 151 to 154, 157, 158, 161 |
| 11 | 166, 167, 172 to 176 | 167, 173 to 176 | 165, 168 to 171, 174, 177 | 169, 171 (a staged company, style cards) |
| 12 | 182, 183, 186 to 189 | 184, 185, 187 to 191 | 181, 184, 188 | 181, 184 (Roof Piece, frevo settings) |

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; a cleared floor; step, work, challenge and research cards; a drum, a pot and spoon or the voice; one optional teacher device | Moves, elements and tools taught in steps; dances watched with their setting; research and sources turned into movement; making and rehearsing with a critique and a change; a showing each unit | A portfolio folder of 12 pieces over the band with reflections; 12 unit showings (three for families); two marks a unit per student on the main look-for | Met marks on each year's 21 ids, and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result.

## Year 3 (grade 3 ids)

### Unit 1. Space, time and energy (days 1 to 16, weeks 1 to 8)

**Arc.** The Acogny hook reopens the room and the stop cue; day 2 retrieves grade 2 pathways and strong beats and
shows the alignment check, so every later move is copied aligned (DA:Pr5.1.3a). Space comes next (distance,
dimensions, filled and empty space, focus; the Pilobolus watch, day 4), then the partner signal for safe level, path
and direction changes (day 5), set counts and improvisation with and against the beat (day 7), energy qualities (day
8) and the recall card (day 10). Groups build the showing (11), critique it (12) and rehearse the change (13).
**Why this order.** Alignment and partner safety come before anything travels; counts come before the improvisation
that fills them; energy comes before the drill that combines both (day 9); recall is taught last because it recalls
the whole built sequence.
**Assessments.** Baseline look on day 3. End: day 14, showing 1 (DA:Pr5.1.3a, DA:Pr5.1.3b, DA:Pr5.1.3c with the
recall card); day 15, showing 2 (DA:Pr4.1.3a, DA:Pr4.1.3b, DA:Pr4.1.3c), each part of each code a look-for as the
frame's evidence line names it. Response on day 16.
**Candidate settled.** Kept: a seated version of each look-for, written into the showing guide; used on days 3, 14 and
15; no day added.
**Leans.** Physical education grades 3 to 5 unit 8 (grade 3 weeks 30 to 32) teaches dance steps as motor skill after
this unit; nothing here waits on it. Counts are clapped, never written (math contact).

### Unit 2. Where dances come from (days 17 to 32, weeks 9 to 16)

**Arc.** Esplanade's everyday moves open the question (17). Day 18 retrieves grade 2 idea sources and a dance's
people and place and shows starting points (DA:Cr1.1.3a); the challenge card follows (20, DA:Cr1.1.3b). Three
dances carry the connecting ids: Esplanade's relationships (21, DA:Cn10.1.3a), L'Ag'Ya's moves and the Martinique
fighting dance (23, DA:Cn11.1.3a), and the Dancing Earth piece's view on water or seeds as a research question (24),
researched and danced while each group sets its showing (25, DA:Cn10.1.3b). The critique comes on day 26, the
rehearsal of the change and the kept cards on day 27, a run-through on day 28 and the response frames practiced on
day 29.
**Why this order.** Students try their own starting points before solving a set challenge; the tie ids sit on the
days that study a dance; research comes after the class has watched the dance it asks about, and the research moves
join the making days.
**Assessments.** Baseline look on day 19. End: day 30, showing (DA:Cr1.1.3a, DA:Cr1.1.3b, DA:Cn10.1.3b, with the
starting-point and research cards); day 31, written (DA:Cn10.1.3a, DA:Cn11.1.3a on unseen described dances, the
invented-child option marked the same). Response on day 32.
**Candidate settled.** Kept: a research card set that keeps the issue a question a grade 3 student answers from two
short cards; inside days 24 and 25, no day added.
**Sensitivity.** Dancing Earth (Native nations, watched only, no regalia, no ceremony), Dunham's L'Ag'Ya only (no Haiti
ceremonies), a school-safe issue; the flags are in the day notes.

### Unit 3. Patterns, forms and styles (days 35 to 50, weeks 18 to 25)

**Arc.** Accumulation hooks the unit (35). Day 36 retrieves grade 2's central idea and clues to meaning and shows the
tools card (DA:Cr2.1.3a); day 37 spots how Accumulation's pattern builds a phrase (DA:Re7.1.3a); AB and ABA follow
(39). Kathak and Irish step dance are watched and charted (40), then the class phrase is danced both ways from
practitioner step cards (41) (DA:Re7.1.3b, DA:Re9.1.3a). A phrase that shows a feeling or idea and the clues that
tie to a main idea come on day 43 (DA:Cr2.1.3b, DA:Re8.1.3a). Groups make the ABA dance (44), critique it (45) and
rehearse (46); this ABA is the dance unit 4 revises and stages.
**Why this order.** Tools before forms, forms before a whole ABA dance; two traditions are watched before they are
danced two ways; the feeling-or-idea phrase comes after unit 2's starting points and just before the making.
**Assessments.** Baseline look on day 38. End: day 48, showing (DA:Cr2.1.3a, DA:Cr2.1.3b); day 49, written and show
items (DA:Re7.1.3a, DA:Re8.1.3a, DA:Re9.1.3a written; DA:Re7.1.3b at the teacher's spot). Response on day 50.
**Candidate settled.** Kept: each written item read aloud a second time for a student who reads below grade 3, inside
day 49's slack; no day added.
**Leans.** Class talk practices ELA's SL.3.1, taught in ELA grade 3 unit 1 (weeks 1 to 8), before this unit.
**Sensitivity.** Kathak: a non-devotional piece, no bells, costume or devotional gesture (leave-out line: Irish step
dance with Accumulation keeps every id met). Spins slow, three at most.

### Unit 4. Our dance on a stage (days 53 to 64, weeks 27 to 32)

**Arc.** Triadic Ballet's shaped costumes hook the unit and the unit 3 ABA dance is danced through (53). Day 54
retrieves grade 2's chosen change and zones and shows the stage map (DA:Pr6.1.3a). Using feedback is modeled (56,
DA:Cr3.1.3a), the floor map shown (57, DA:Cr3.1.3b) and drilled (58), kabuki's scenery, music and costume change
watched and design choices tried (59, DA:Pr6.1.3b). Groups keep one design choice and map the dance (60), take the
partner critique on the change card (61) and rehearse on the marked stage with the program card (62).
**Why this order.** Stage areas first, so every later day uses them; the change is modeled before the critique that
uses it; the design choice is tried before it is kept.
**Assessments.** Baseline look on day 55. End: day 63, the family showing (look-fors for DA:Cr3.1.3a, DA:Pr6.1.3a,
DA:Pr6.1.3b; the change card, floor map and stage sketch scored after the session). Response on day 64. The year-end
check sits before this unit (week 26), clear of the core checks of weeks 28 to 32.
**Candidate settled.** Kept: the program card written by the students, one line each, 10 minutes inside day 62, read
aloud on day 63; no day added.
**Fallback.** A class that left out unit 3 learns a short Curio Class original study on days 53 to 55.

## Year 4 (grade 4 ids)

### Unit 5. Rhythm, balance and cues (days 65 to 80, weeks 1 to 8)

**Arc.** Bomba's call and answer between dancer and drum hooks the unit (65). Day 66 retrieves unit 1's aligned
recall and elements and adds balance (DA:Pr5.1.4a). The strengthening routine (68) and the invented dancer's week
(69) carry DA:Pr5.1.4b; shapes, soft landings and eye contact with the legong watch (70, DA:Pr4.1.4a); the rhythm
card and drum parts (71, DA:Pr4.1.4b); cues and goals (73, DA:Pr5.1.4c); the energy word bank (74, DA:Pr4.1.4c).
Drum-and-dance groups build (75), critique and set goals (76) and rehearse (77).
**Why this order.** Balance and strength before jumps and landings; drum parts before cues, so a cue can come from
the drum; energy words last, since the written day and unit 7 use them.
**Assessments.** Baseline look on day 67. End: day 78, showing (DA:Pr5.1.4a; DA:Pr5.1.4c as starting together on a
dancer's cue and changing on the drum or the held card, with the goal card; DA:Pr4.1.4a; DA:Pr4.1.4b as two
percussion sounds played, a steady and an uneven pattern danced and a tempo change answered); day 79, written and show (DA:Pr5.1.4b from a new invented dancer card plus two routine
moves shown; DA:Pr4.1.4c). Response on day 80.
**Candidate settled.** Kept: the invented dancer card read by the health course's lens for its food line, a unit plan
step before day 69; no day.
**Leans.** Physical education unit 15 (grade 4 weeks 27 to 30) comes later; nothing waits on it. Food: no task asks
about a student's own diet, weight or body.

### Unit 6. Dances from facts and places (days 81 to 96, weeks 9 to 16)

**Arc.** Lerman's work with scientists hooks the unit (81). Day 82 retrieves unit 2's starting points and research
ties and shows the idea card (DA:Cr1.1.4a); a challenge invented for a partner follows (84, DA:Cr1.1.4b). The gumboot
dance carries DA:Cn11.1.4a (86); a dance's main idea tied to an experience carries DA:Cn10.1.4a (87). The research
notes sheet opens the topic dance (88), researched and choreographed (89), critiqued (90) and rehearsed with its
reflection and art-form lines (91) (DA:Cn10.1.4b).
**Why this order.** The idea card and invented challenge come first because the topic dance uses both; the dances
are studied before the research so the class has seen facts become movement.
**Assessments.** Baseline look on day 83. End: day 94, showing (DA:Cr1.1.4a idea card, DA:Cr1.1.4b, DA:Cn10.1.4b);
day 95, written (DA:Cn10.1.4a, DA:Cn11.1.4a). Response on day 96.
**Candidate settled.** Kept: the source cards checked against the science course's readings fact by fact, a unit plan
step before day 88; no day.
**Leans.** Science grade 4 units 1 and 2 are taught by week 10 (calendar.csv); day 88 falls in week 12 while science
unit 3 (waves, weeks 11 to 14) runs, so its note carries the frame's bridge: waves only once science has taught them.
**Sensitivity.** The gumboot dance's history in one plain sentence; no boots, no imitation; gentle slaps.

### Unit 7. Styles inside one genre (days 99 to 114, weeks 18 to 25)

**Arc.** Beach Birds and its chance order hook the unit (99). Day 100 retrieves unit 3's tools and traditions and
alters tools, chance draw included (DA:Cr2.1.4a). Locking and popping carry DA:Re7.1.4a (102) and DA:Re7.1.4b (103);
Beach Birds' meaning from moves, idea and setting carries DA:Re8.1.4a (105); the reason card carries DA:Re9.1.4a
(106). The study around one main idea grows from the unit 6 idea card (107, DA:Cr2.1.4b), is built (108), critiqued
(109) and rehearsed (110); unit 8 reworks it.
**Why this order.** Altered tools come before the study that uses them; style patterns are spotted before they are
danced two ways; the artistic traits come after meaning, so the reason card has something to point at.
**Assessments.** Baseline look on day 101. End: day 112, showing (DA:Cr2.1.4a, DA:Cr2.1.4b); day 113, written and show
(DA:Re7.1.4a, DA:Re8.1.4a, DA:Re9.1.4a written with one trait shown; DA:Re7.1.4b shown). Response on day 114.
**Candidate settled.** Kept as an extension card on day 104: a third style inside one genre from outside the United
States, never assessed; no day added.
**Leans.** Class talk practices ELA's SL.4.1. Physical education unit 15 (weeks 27 to 30) comes after this unit's
study; neither needs the other.

### Unit 8. Making a room a stage (days 117 to 128, weeks 27 to 32)

**Arc.** The Firebird with Maria Tallchief hooks the unit and the unit 7 study is danced through (117). Day 118
retrieves unit 4's feedback, map and stage areas and shows the stage plan for a gym, hall or lawn (DA:Pr6.1.4a). The
rework card (120, DA:Cr3.1.4a), the relationship sketch (121, DA:Cr3.1.4b, drilled 122) and the Urban Bush Women
watch with production elements tried (123, DA:Pr6.1.4b) follow; groups choose the element and set the plan (124),
take the classmates' critique on the rework card (125) and rehearse in the planned space (126).
**Why this order.** The space is planned first because every rehearsal after it happens in that space; the rework is
modeled before the critique that feeds it.
**Assessments.** Baseline look on day 119. End: day 127, the family showing (look-fors plus the rework card,
relationship sketch, stage plan and program card scored after the session). Response on day 128. The year-end check
sits before this unit, clear of grade 4's core checks in weeks 27 and 30 to 32.
**Candidate settled.** Kept: a seated audience place for a family member who uses a wheelchair, in every stage plan;
inside days 118 and 124, no day added.

## Year 5 (grade 5 ids)

### Unit 9. Rhythm from the body and the world (days 129 to 145, weeks 1 to 9)

**Arc.** Stomp hooks the unit (129). Day 130 retrieves unit 5's balance, cues and drum parts and shows the run card
(DA:Pr5.1.5a). Body percussion with the sasa watch (132) and found sound (133) carry DA:Pr4.1.5b; ground and air
paths with focus and projection carry DA:Pr4.1.5a (134); Water Study's tight and flowing carries DA:Pr4.1.5c (135);
safe habits and the invented dancer carry DA:Pr5.1.5b (136); ensemble rehearsal and the goal card carry DA:Pr5.1.5c
(137). Ensembles build (138), critique (139) and rehearse in two cycles (140, 141), then run the whole dance (142).
**Why this order.** The run of phrases is the material every later day rehearses; body sound comes before found sound;
air paths come after the landings retrieved from unit 5; the second rehearsal cycle is why the frame gives 17 days.
**Assessments.** Baseline look on day 131. End: day 143, showing (DA:Pr5.1.5a, DA:Pr5.1.5c with the goal card,
DA:Pr4.1.5a, DA:Pr4.1.5b, and DA:Pr5.1.5b's safe practice); day 144, written and show (DA:Pr5.1.5b written,
DA:Pr4.1.5c shown and written). Response on day 145.
**Candidate settled.** Kept: the found-sound kit checked item by item by the safety agent, a unit plan step before day
133; no day.
**Leans.** Physical education unit 22 (grade 5 weeks 22 to 25) comes later; nothing waits on it. Food through the
invented dancer only.

### Unit 10. Many sources, opposing themes (days 146 to 162, weeks 9 to 17)

**Arc.** Cursive's calligraphy hooks the unit (146). Day 147 retrieves unit 6's idea card and research notes and shows
the source card (DA:Cr1.1.5a); the challenge log follows (149, DA:Cr1.1.5b). Hard Time Blues against the Lindy hop
carries DA:Cn10.1.5a (151); style qualities and their period carry DA:Cn11.1.5a (152); the matter research opens
DA:Cn10.1.5b (153). Groups make in two cycles: material and the matter dance begun (154), the critique (155), the
material set (156), the matter dance finished (157), the whole showing rehearsed with the comparison lines (158).
**Why this order.** Sources and challenges build the material unit 11 chooses from, so they come first; the two
opposing dances are watched before the research so the class has seen movement carry a viewpoint; the second making
cycle is why the frame gives 17 days.
**Assessments.** Baseline look on day 148. End: day 160, showing (DA:Cr1.1.5a, DA:Cr1.1.5b, DA:Cn10.1.5b with the
notes); day 161, written (DA:Cn10.1.5a, DA:Cn11.1.5a). Response on day 162.
**Candidate settled.** Kept: the news card set kept to items with no harm or conflict in them, written before day 147;
no day.
**Leans.** Science grade 5 unit 1 (particles of matter, weeks 1 to 4) is taught before day 153 (week 13).
**Sensitivity.** Hard Time Blues: one plain sentence on the hardship, no student plays a sharecropper or is asked about
hard times; Lindy hop aerials watched only.

### Unit 11. How dance speaks without words (days 165 to 178, weeks 19 to 25)

**Arc.** Emergence's swarm hooks the unit (165). Day 166 retrieves unit 7's study and responding rows and shows two
tools altered together (DA:Cr2.1.5a). Emergence's purpose from pattern (168, DA:Re7.1.5a), the Les Ballets Africains
piece interpreted (169, DA:Re8.1.5a), the traits of a meaningful dance with the opinion frame (170, DA:Re9.1.5a) and
the style cards (171, DA:Re7.1.5b) follow. The study from unit 10's material (172, DA:Cr2.1.5b) is built (173),
critiqued (174) and rehearsed, and the style card finished (175). The warm-ups of days 174 and 175 run the
responding frames aloud in pairs (purpose from pattern, two moves that carry the idea, an opinion with two traits),
practice before the written day.
**Why this order.** Tools return from grades 3 and 4, so the study builds fast; the responding days come before the
study so its "without words" line has words to use; the style card is finished on the last making day, as the frame
asks.
**Assessments.** Baseline look on day 167. End: day 176, showing (DA:Cr2.1.5a, DA:Cr2.1.5b); day 177, written
(DA:Re7.1.5a, DA:Re8.1.5a, DA:Re9.1.5a), with the style card (DA:Re7.1.5b) from day 175 scored with it and listed in
day 177's codes. Response on day 178.
**Candidate settled.** Kept: a style card set of at least six styles from five regions, so no student must use their
own; on day 171, no day added.
**Leans.** ELA grade 5 unit 3 teaches opinion writing (W.5.1) in these same weeks (17 to 25); day 170 carries the
bridge: the frame is taught on the day, practiced, not owned, and only the reasons are marked. Physical education
unit 22 runs in the same weeks; this unit uses only the class's own moves.

### Unit 12. One dance, two spaces (days 181 to 192, weeks 27 to 32)

**Arc.** Roof Piece hooks the unit and the unit 11 study is danced through (181). Day 182 retrieves unit 8's rework
and stage plan and shows the change log (DA:Cr3.1.5b). Frevo and the venue plan (184, DA:Pr6.1.5a), staging trials
(185, DA:Pr6.1.5b) and the suggestion card (186, DA:Cr3.1.5a) follow. Groups adapt to both venues (187), take peer
suggestions in the critique (188) and rehearse in both venues (189).
**Why this order.** The log starts first so every later change is logged; venues before staging, since the staging
must suit both.
**Assessments.** Baseline look on day 183. End: day 190, showing in the first venue; day 191, showing for families in
the second venue (DA:Pr6.1.5a across both days; the change log and staging note scored after the session). Response on
day 192.
**Candidate settled.** Kept: for a school with one room only, the second venue offered as a recorded showing with the
family's yes; on day 191, no day added.

## Course-level checks

| Check | Course days | Week of the year | Samples | Respond |
|---|---|---|---|---|
| Year 3 mid-year | 33 | 17 | unit 1: DA:Pr5.1.3a, DA:Pr5.1.3c (recall, one coach comment, own check), DA:Pr4.1.3b (set count, the music's timing, beat phrasing), DA:Pr4.1.3c | 34 |
| Year 3 year-end | 51 | 26 | units 1 and 2: DA:Cn11.1.3a, DA:Cn10.1.3a (written); DA:Pr5.1.3b, DA:Cr1.1.3a (a starting point the student picks from three cards) (showing) | 52 |
| Year 4 mid-year | 97 | 17 | unit 5: DA:Pr5.1.4a, DA:Pr5.1.4c (a dancer's cue to start, the drum or held card to change, a goal line) | 98 |
| Year 4 year-end | 115 | 26 | units 5 and 6: DA:Pr4.1.4c (with a refining line), DA:Cn11.1.4a, DA:Cr1.1.4b's invented challenge (written); DA:Pr4.1.4a, DA:Cr1.1.4b's solving (showing) | 116 |
| Year 5 mid-year | 163 | 18 | unit 9: DA:Pr5.1.5a, DA:Pr5.1.5c (unison, spacing refined on a coach cue, a goal line), DA:Pr4.1.5b (body percussion and a found-sound rhythm through a timing change) | 164 |
| Year 5 year-end | 179 | 26 | units 9 and 10: DA:Cn10.1.5a, DA:Cn11.1.5a (written); DA:Pr4.1.5a, DA:Cr1.1.5a (two new sources) (showing) | 180 |

- **The weeks** are CALENDAR.md's for this course (17 and 26 in grades 3 and 4; 18 and 26 in grade 5). Arts are
  specials in K to 5 and do not count against the classroom teacher's stagger.
- **No repeat of the unit just assessed.** Each check follows a unit's end-of-unit days by one day, so it draws its
  items from the units before that one (mid-year: the year's first unit only; year-end: the first two), and each
  goal says so. The just-assessed unit's records are carried unscored.
- **Each part of each code.** Every code a check lists has each part of its words-file line asked on the day (the
  parts are in the table). Where a part cannot be seen for every student inside the minutes, the code is not listed:
  DA:Pr4.1.4b at the year 4 mid-year (the percussion part; the tempo change is danced as practice) and DA:Pr4.1.5c at
  the year 5 year-end (its moving parts; DA:Cn10.1.5a, fully answerable in writing, is sampled in its place).
- **Task form inside two weeks (lead call 6).** A showing is dance's own evidence and may follow a unit showing; what
  may not repeat inside two weeks is the same item. Every check showing is on earlier-unit work with its own new
  items (a new count, cue, timing change, starting point, challenge or source), so rule 2 holds; each day's note
  says so.
- **Collect once (lead call 7).** No check re-asks items a unit gave one to three days before: each draws from units
  assessed seven or more weeks earlier, in a new form, and carries the just-assessed unit's record unscored.
- **Minutes.** Mid-year checks have no written part: set-up 3, warm-up 5, six groups of five at about 4 minutes (24),
  goal lines at seats 4 (years 4 and 5; a cool-down in year 3), cool-down and room back 4: 40. Year-end checks: set-up
  3, warm-up 2, written part 10 (every student seated), six groups of five at about 3 minutes (18), cool-down and room
  back 5: 38 of 40. At most two look-fors a student in a group turn; the mid-year checks pair their codes into two
  look-fors (the day notes name the pairs), with the goal line a kept card.
- **Codes not sampled on any check (rule 3).** 42 of the 63 ids are evidenced only by their unit's end-of-unit
  assessment: year 3 DA:Pr4.1.3a, DA:Cr1.1.3b, DA:Cn10.1.3b, the six unit 3 ids (DA:Cr2.1.3a, DA:Cr2.1.3b,
  DA:Re7.1.3a, DA:Re7.1.3b, DA:Re8.1.3a, DA:Re9.1.3a) and the four unit 4 ids (DA:Cr3.1.3a, DA:Cr3.1.3b, DA:Pr6.1.3a,
  DA:Pr6.1.3b); year 4 DA:Pr4.1.4b, DA:Pr5.1.4b, DA:Cr1.1.4a, DA:Cn10.1.4a, DA:Cn10.1.4b, the six unit 7 ids and the
  four unit 8 ids; year 5 DA:Pr4.1.5c, DA:Pr5.1.5b, DA:Cr1.1.5b, DA:Cn10.1.5b, the six unit 11 ids and the four unit
  12 ids. Why: units 3, 7 and 11 are assessed one day before the year-end check, which by rule draws from earlier
  units; units 4, 8 and 12 come after the year-end check on purpose (core checks fill weeks 28 to 32), and their
  family showings are their assessment; DA:Pr4.1.4b and DA:Pr4.1.5c have parts that cannot be seen for every student
  in a check's minutes (above); the rest do not fit a check at two look-fors a student. The frame's Course-level
  checks table limits the sample (lead call 3); a frame option is under For the lead.

## The once-a-week path

A school that meets once a week keeps every unit and every id in 32 sessions a year by merging days; each day's note
in days.csv names its session ("Weekly path: session n", the week of the year). Every unit keeps the dance watch with
the step-card demonstration, one rehearsal session with the critique, the showing and one respond session; fluency
days fold into the warm-ups.

| Unit | Sessions | Merged course days by session |
|---|---|---|
| 1, 5 | 8 | 1+2, 3+4+5, 6+7, 8+9+10, 11+12+13, 14, 15, 16 (unit days) |
| 2, 6 | 8 | as units 1 and 5 |
| 3, 7 | 7 | 1+2+3, 4+5+6+7, 8+9+10, 11+12+13, 14, 15, 16 |
| 4, 8 | 5 | 1 to 4, 5 to 8, 9+10 (critique and rehearsal), 11 (showing), 12 (respond) |
| 9 | 9 | 1+2, 3+4, 5+6, 7+8+9, 10+11, 12+13+14, 15, 16, 17 |
| 10 | 8 | 1+2, 3+4+5, 6+7+8, 9+10+11, 12+13+14, 15, 16, 17 |
| 11 | 6 | 1+2+3+4 (tools, rounds and the Emergence purpose on the hook's own dance), 5+6+7 (three responding ids), 8+9+10+11, 12, 13, 14 |
| 12 | 5 | 1 to 5 (works, change log, venue plan, staging trials), 6 to 9 (suggestion card, adapting, critique, rehearsal), 10, 11, 12 |
| Each check | 1 + 1 | the check session in the same week as the full path (17 or 18, and 26), respond one week later |

Sessions a year: 8 + 8 + 7 + 5 + 4 = 32 (years 3 and 4); 9 + 8 + 6 + 5 + 4 = 32 (year 5). A merged session never
drops a critique, a rehearsal before a showing or a respond day; on the merged path the rehearsal follows the critique
inside the same session. The national figure is at least 90 minutes of dance a week in grades 3 to 5; the full path
gives 80 (10 short) and this path 40 (50 short). A school can add time.

## Shorter path

- **A shorter period (30 minutes).** Set-up 2, warm-up 3, cool-down and room back 4; the day-2 retrieval keeps its ten
  minutes and the teaching gives way. A showing day fits (six groups at about 3 minutes, 18, plus 9). A written day
  does not: its written items stay (15) and three groups' show items are taken that day, the other three in the first
  6 minutes of the respond day, inside its own making time. Year-end checks keep the written part (10) and split the
  showing over the check day and the first minutes of its respond day; mid-year checks keep the goal lines and split
  the group turns the same way. Nothing assessed is cut.
- **A year about 10 school days short.** Ten school days is two weeks, four sessions of this course a year. Four
  fold-in days a year (12 over the band), each a practice day whose drill moves into the five-minute warm-ups of the
  two sessions after it, nothing assessed there and no owned part cut; each saves one 40-minute session.

| Year | Fold-in days | What moves where | Minutes saved |
|---|---|---|---|
| 3 | 6, 9, 22, 42 | partner and dimension drill; count-and-quality drill; challenge rounds; two-ways drill, each into the next two warm-ups | 160 |
| 4 | 72, 85, 104, 122 | drum-and-dance rounds; challenge swaps; two-styles rounds; sketch rounds | 160 |
| 5 | 142, 150, 159, 167 | full run (into day 141's cycle); challenge-log rounds; the frames (into the warm-ups of days 157 and 158; day 158's rehearsal stands for the run-through); paired-tool rounds and the baseline look (into the warm-ups of days 168 and 169, half the groups each day) | 160 |

Total: 12 days, 480 minutes, so the band holds on 180 of the frame's 192 course days (60 of 64 a year). The days are
marked "Shorter year: fold-in day" in their notes. Day 158 is kept on the shorter year: it is unit 10's only
rehearsal of the whole showing and the day the comparison lines scored on day 160 are written. Each year names four
fold-in days, the four sessions that ten school days hold (lead call 1); no other reading of "10 days" is used.

## For the lead

1. **Rule 3 gap (later.csv L107).** 42 of 63 owned ids are sampled on no course-level check (listed above, named with
   the reason, which lead call 3 accepts). A frame option, if the lead wants more sampled: the year 5 mid-year check
   adds one written item on a unit 9 id, DA:Pr5.1.5b's "discuss how habits and nutrition prevent injury" from a new
   invented dancer card, its safe-practice part seen in the showing (the goal-line minutes would need to be shared).
   Never a unit 2, 6 or 10 id there: those were assessed the days before.
2. **The two-look-for cap at mid-year.** The frame's mid-year checks list two or three codes, all in the showing; the
   scope pairs them into two look-fors a student, with the goal line a kept card. The frame's checks paragraph now
   states the mid-year budget; it could also name the pairing.
3. **Once-a-week sessions in year 5 (expert read finding 4).** Moving a session from unit 9 to unit 11 would put the
   year 5 mid-year check session in week 17, not CALENDAR.md's week 18, and unit 11 sits between the week 19 respond
   session and the week 26 check (six sessions). The scope rebalances inside unit 11's six sessions instead; a frame
   fix would need the check weeks moved.
4. **Physical education checks in the same weeks.** Physical education grades 3 to 5 also checks in weeks 18 and 26;
   both are specials, so the stagger rule is not broken (frame For the lead 1 still waits on the lead's after-core
   calendar pass).

## What was hard to settle

- The fold-in days are only four a year: the frame's units have few practice days that carry nothing new. Run-throughs
  before showings are kept, except day 142, whose full run sits inside day 141's cycle, and day 159, whose run-through
  day 158's whole-showing rehearsal stands for. One baseline-look day folds (day 167), its look split over the warm-ups
  of days 168 and 169.
- The baseline look is placed on each unit's first fluency day (day 3), before most of the unit is taught; it is an
  observation of the main look-for only, as APPROACH "Growth" asks.
