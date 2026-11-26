# Scope and sequence: Dance, grades 6 to 8

Course `dance-grades-6-to-8` (catalog id `dance-6-8`), a band course for grades 6, 7 and 8. Draft, 2026-11-26, from the
frame (docs/courses/dance-grades-6-to-8/frame.md); the days are in data/plans/dance-grades-6-to-8/days.csv.

## How the band runs

- **Three years, one after another.** Year 6 is course days 1 to 64, year 7 days 65 to 128, year 8 days 129 to 192.
  Each year is 60 days in four units, two course-level check days and two respond days. Units, owned rows and day
  counts are the frame's, unchanged.
- **Which standards fall in which year (STANDARD.md 3.1).** Year 6 claims only the 21 grade 6 dance ids of the
  National Core Arts Standards, 2014 (`DA:...6a` to `6c`), year 7 only the 21 grade 7 ids, year 8 only the 21 grade 8
  ids: 63 in all, the count in STANDARD.md 3.2, each taught and assessed in its own year and each placed on at least
  one day of days.csv. A year revisits the year before's ids as practice that returns, never as a claim. Ids are named
  by id only; their actions come from data/standards/ncas-performance-standards-words.txt.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a student's record shows which grade's standards they met. A student who
  meets year 8 before year 7 uses each day 2 retrieval task's reteach.
- **Meeting days and school_day.** The course meets two 40-minute sessions a week, 32 weeks a year, 96 weeks over the
  band (bar criterion 9: no daily period). `school_day` counts school days across the whole band, 1 to 480: band
  course day n falls on band school day ceil(2.5 x n), the even spread of CALENDAR.md, so year 6 is band school days 1
  to 160, year 7 is 161 to 320 and year 8 is 321 to 480. Take away 160 (year 7) or 320 (year 8) for the school day of
  that grade's own year; the week is (school day - 1) // 5 + 1. Every course day sits on the week the frame names
  (course day n of a year falls in week n / 2, rounded up). scripts/frame.py reads the column this way and files each
  year under its grade. This formula is the one rule for the column: a filled `school_day` wins over frame.py's even
  spread, and data/plans/calendar.csv is regenerated from it by the lead, so the column is never re-counted to match
  either (lead call 8, 2026-11-26).
- **The 40 minutes.** Set-up 3 (desks back, floor checked, spots marked), warm-up 5, teaching and dancing, cool-down
  and closing line 4, room back and cards collected 3. Day 2 of every unit: set-up 3, warm-up 5, retrieval 10,
  teaching 15, cool-down 4, room back 3. A showing day: set-up 3, warm-up 5, six groups of five at about 4 minutes
  (24), self-check 5, room back 3. A written day: set-up 2, the unseen phrase danced twice or its description handed
  out (about 4), items at tables 28, collecting 3.
- **The day pattern of a unit.** Day 1 is the hook, the compelling question and the study of a dance (Understanding,
  kept clean of any check). Day 2 holds the retrieval task. Technique and the dances studied are taught on
  Understanding days before any making uses them; Fluency days are short repeated practice of what earlier days
  taught. The first Application day builds; the second holds the unit's one critique (describe, ask, suggest); the
  next rehearses the change. Kept products (logs, cards, notation, research cards) are finished and collected on the
  last making days and scored after the session with the check marks. Each unit closes with two end-of-unit check
  days, a showing day and a written day, never mixed, then one respond day that acts on the marks (response time is
  that day, counted once). No score comes from the day a move, element or notation is first taught.
- **Readiness and retrieval (rule 2).** Every row of the band assumes only the row one grade back in its thread
  (data/progressions/arts.csv), so every unit opens with a retrieval task on day 2 and no unit has a readiness check.
  Year 6 units retrieve the grade 5 rows of dance 3 to 5, last used one grade back (the frame's "Picked up from"
  table). Because dance 3 to 5 is not required, each year 6 retrieval carries one ten-minute reteach of both threads'
  grade 5 steps inside the same block. Years 7 and 8 retrieve the year before's row in the same thread, used on the
  course days the frame's "Inside the band" table gives. The `retrieves` column names the rows.
  **Same-year retrieval.** Where a unit leans on a row taught earlier the same year (or, on day 165, the year before
  in another unit), the named day's five-minute warm-up is that retrieval, in its note and `retrieves`: day 26
  (da-g6-elements), 42 (da-g6-form), 55 (da-g6-elements, the waltz), 90 and 101 (da-g7-elements), 106 (da-g7-form),
  154 (da-g8-elements), 165 (da-g7-elements) and 170 (da-g8-form). No readiness check is needed: no row is two grades
  idle, and no unit's first day changes.
- **Growth and the portfolio.** Each unit opens with a baseline look at its main look-for during its first practice
  days (named in the notes) and marks the same look-for again at the showing, so each student has two marks a unit.
  One piece a unit goes into the portfolio folder with a one-line reflection, chosen on the respond day (12 pieces
  over the band).
- **Taking part without dancing alone.** Every showing is in groups of five; a student may dance beside a partner,
  show at the teacher's spot, dance a seated or one-limb version, or take the director's, counter's or staging lead's
  role, which counts only for what it shows. A written item may be answered aloud or shown; the mark is the same.
- **The ordinary room and safe use.** A cleared classroom, hall or gym, floor tape or chalk, a drum or a pot and
  spoon, claps and counts; nothing must be bought. The frame's rules hold every day (clear floor checked first, bare
  feet or soft shoes, no lifts, no jumping from heights, small jumps landed softly on a suitable floor, no inverted
  moves, no pushed stretch, contact only by agreement, the stop cue, soft or light props, water and rest). Each
  unit's day 1 note carries its hazards and controls in the frame's words; days with jumps, props, chairs or a second
  space repeat the rule that applies. The floor rule: jumps, landings and stamping only on a level, resilient surface
  the school confirms suitable; otherwise low and without impact, with the look-for seen later in a suitable space.

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week, 32 weeks a year; a cleared floor; step cards, work cards, criteria and notation cards; a drum or counts; one teacher who may have no dance training | Moves, elements, tools and notation taught in named steps; dances studied with their setting; making and rehearsing with a critique and a revision; a showing each unit; a retrieval task each unit | A portfolio folder of 12 pieces over the band with reflections; 12 showings; two marks a unit per student on the main look-for; six course-level checks with respond days | Met marks on the year's 21 ids, and growth on the look-fors |

Nothing here has been tried with students, and Curio Class makes no claim that arts study raises any other result.

## The four processes, by day

Each year carries all four artistic processes (bar criterion 1), and each unit touches at least the processes the
frame names for it; a unit need not claim all four, and no day claims an id outside its unit's owned rows (lead call
2, 2026-11-26). In this course every unit's days do in fact carry all four as practice, listed by day under each
unit. Creating: the build, critique and rehearse-the-change
days (Application). Performing: every day dances (warm-up, technique, rehearsal, showing). Responding: the day 1 study
and each later study of a dance (Understanding), plus the response items of units 3, 7 and 11. Connecting: each dance
studied with its setting (when, where, by whom, for what), and the connecting ids of units 4, 8 and 12. Each unit
below names its days.

## Year 6 (grade 6 ids, course days 1 to 64)

### Unit 1. Together in space and time

- **Calendar.** Course days 1 to 18, school days 3 to 45, weeks 1 to 9.
- **Arc.** Stepping (accents in four) opens; partner and group spacing follows on day 2, then the waltz in three
  with its setting on the work card (day 3: Vienna's ballrooms of the 1860s, who danced it and what the turning
  couple meant then, about 5 minutes), butoh's tension and flow (day 5), changes and transitions (day 6), small jumps and landings (day 7) and the
  anatomy warm-up (day 9), each with a drill after it (days 4, 8, 10). Groups build ensemble sections (day 11),
  critique them (day 12), test fixes (day 13), run them with the card withdrawn (day 14) and close the rehearsal log
  (day 15). The showing answers the compelling question: dancers sharing space and hitting threes and fours.
- **Why this order.** The floor, the stop cue, the warm-up and spacing come before any group work; the elements come
  before the technique they are danced with; jumps are taught on a day of their own before a drill and before any
  section uses them. Six ids, three of them technique steps that need drills, so this is the year's longest unit
  (four Fluency days).
- **Assessments.** Retrieval on day 2 (da-g5-elements, da-g5-technique, with the reteach). Baseline look on days 3 and
  4. End: day 16, the showing (look-fors Pr4.1.6a, Pr4.1.6b, Pr5.1.6a and the warm-up for Pr5.1.6b; show item
  Pr4.1.6c), and day 17, the written day (the warm-up plan card, Pr5.1.6b; the rehearsal log collected on day 15
  scored for Pr5.1.6c). Respond: day 18. The written day holds one item; the unit plan may give its slack to the
  self-check and the portfolio line.
- **Processes.** Create days 11 to 13; perform every day; respond (studying a dance) days 1 and 5; connect days 1
  (stepping's history), 3 (the waltz's setting) and 5 (butoh's setting).
- **Candidate.** Kept: a three-beat social dance from outside Europe beside Strauss, about 8 minutes inside day 3, the
  unit plan's pick with its rights line. No day added.

### Unit 2. Ideas that agree and ideas that clash

- **Calendar.** Course days 19 to 32, school days 48 to 80, weeks 10 to 16.
- **Arc.** Childs's Dance (three arts joined) opens; the inspiration list joins two ideas by likeness or clash (day
  20); Fancy Free's solos open the style menu (day 21), drilled on day 22; the tools and forms (day 23), drilled on
  day 24; criteria for a personal or cultural study (day 25). Groups build a 32-count study with a stated goal (day
  26), critique it (day 27), rehearse the change and close the kept cards (day 28) and run it (day 29).
- **Why this order.** Ideas before styles, styles before tools, tools before the criteria that judge a study, and all
  four before the build; the study uses unit 1's spacing, accents and tension as material.
- **Assessments.** Retrieval on day 20 (da-g5-ideas, da-g5-form). Baseline look on days 22 and 24. End: day 30, the
  showing (Cr2.1.6a look-for; the inspiration list, Cr1.1.6a, and criteria sheet, Cr2.1.6b, collected on day 28 and
  scored with these marks), and day 31, the written day (the styles note, Cr1.1.6b). Respond: day 32.
- **Processes.** Create days 20, 22 to 29; perform every day; respond days 19, 21; connect days 19 and 21 (each work's
  time and makers).
- **Candidate.** Kept: one inspiration card from a maker outside the United States on the day 20 class set. No day
  added.

### Year 6 mid-year check

Course day 33 (school day 83, week 17), showing day; respond day 34 (school day 85, week 17). See "Course-level
checks".

### Unit 3. Criteria and critique

- **Calendar.** Course days 35 to 48, school days 88 to 120, weeks 18 to 24.
- **Arc.** Rome & Jewels's patterns (day 35), time and energy in hip-hop beside stepping (day 36), purpose (day 37),
  the criteria card (day 38) and the critique draft (day 39); then the student's own notation (day 40) and its drill
  (day 41); then the unit 2 study revised against group criteria (day 42), critiqued (day 43) and rehearsed with the
  revision note and the notation collected (day 44); the critique revised from written feedback (day 45).
- **Why this order.** The responding words come first because the critique and the revision criteria both use them;
  the critique is drafted early (day 39) so the teacher's written feedback is back before its revision day (day 45),
  inside the unit, as the frame asks. Notation is taught before the day that writes the study down. Four of six ids
  are response ids met in writing, so the unit has one Fluency day (day 41) beside the daily warm-up.
- **Assessments.** Retrieval on day 36 (da-g5-revise, da-g5-respond). Baseline look on days 41 and 42. End: day 46,
  the showing (Cr3.1.6a with the revision note; the notation, Cr3.1.6b, scored on whether a partner could dance it),
  and day 47, the written day on an unseen Curio Class phrase and an unseen dance's description (Re7.1.6a, Re7.1.6b,
  Re8.1.6a), with the revised critique (Re9.1.6a) scored with it. Respond: day 48.
- **Processes.** Create days 40, 42 to 45; perform every day; respond days 35 to 39, 47; connect days 35 and 37
  (hip-hop in Philadelphia, setting as part of purpose).
- **Candidate.** Dropped: a third style from Asia or Latin America for the element comparison. DA:Re7.1.6b asks for
  two styles, the written item is a paragraph, and the unit's 14 days hold six ids; year 6 already studies Japan
  (unit 1) and China and Central Asia (unit 4).
- **Fallback.** A class that left out unit 2 learns a short Curio Class original study inside day 42 and revises it.

### Unit 4. Dance with a point of view

- **Calendar.** Course days 49 to 62, school days 123 to 155, weeks 25 to 31. The family showing is day 60 (week 30)
  and the written day 61 (week 31).
- **Arc.** The Green Table (day 49), the Tang figurine's whirl (day 50) and Kaha:wi (day 51) carry cultural meaning
  and the like-me line; the research card (day 52) and the viewpoint dance planned (day 53); then performing in the
  space (day 54) and production elements, with the waltz context card drafted in its last ten minutes from the day 3
  work card after a waltz retrieval warm-up (day 55); the viewpoint dance built (day 56), critiqued with a
  choreographer's note (day 57), rehearsed in the showing space with the kept cards, the waltz context card among
  them, finished and collected (day 58) and dress-run (day 59).
- **Why this order.** The meaning of other people's dances comes before the class makes its own viewpoint dance; the
  research is done before the dance is built; the performing and production steps come before the rehearsals that
  apply them. Last in the year because the family showing gathers the year's spacing, studies and revisions.
- **Assessments.** Retrieval on day 50 (da-g5-stage, da-g5-connect). Baseline look on days 53 and 54. End: day 60,
  the family showing (Pr6.1.6a and Cn10.1.6b look-fors; the waltz demonstration with its context card as the
  Cn11.1.6a show item, the card drafted on day 55 and collected on day 58; the production card, Pr6.1.6b, scored
  with these marks), and day 61, the written day
  (Cn10.1.6a, Cn11.1.6a). Respond: day 62. The family showing is the unit's own end-of-unit assessment, before the
  year-end check.
- **Processes.** Create days 53, 56 to 58; perform every day; respond days 49 to 51; connect days 49 to 53, 55
  (the waltz context card) and 60, 61.
- **Candidate.** Kept: the issue list checked for party politics and for any issue that asks a student to tell their
  own hardship, by the unit plan before day 52. No day added.
- **Bridge.** Social studies grade 6 unit 8 (school days 100 to 113, weeks 20 to 23) teaches the Silk Roads exchange
  before day 50; the work card still carries the three setting lines for a class that has not met it.

### Year 6 year-end check

Course day 63 (school day 158, week 32, the finals week), written day; respond day 64 (school day 160).

## Year 7 (grade 7 ids, course days 65 to 128)

### Unit 5. Borrowed shapes and growing bodies

- **Calendar.** Course days 65 to 82, grade 7 school days 3 to 45 (band 163 to 205), weeks 1 to 9.
- **Arc.** The Nicholas Brothers (day 65) and borrowed body designs (day 66), the accent card (day 67) and its drill
  (day 68), qualities compared across styles (day 69); then alignment and weight shifts (day 70) with a copy-and-recall
  drill (day 71), the invented dancer's habits (day 72), Dance Theatre of Harlem's rehearsal goals (day 73) and a
  mixed drill (day 74); groups build (day 75), critique (day 76), rehearse the change (day 77), run with the card
  withdrawn (day 78) and close the goals note (day 79).
- **Why this order.** It reopens the floor and warm-up after the summer, moves the elements from spacing to borrowing,
  and sets the group goals only after the class has watched professionals set theirs.
- **Assessments.** Retrieval on day 66 (da-g6-elements, da-g6-technique, unit 1). Baseline look on days 67 and 68.
  End: day 80, the showing (Pr4.1.7a, Pr4.1.7b look-fors; Pr5.1.7a show item), and day 81, the written day
  (Pr4.1.7c, Pr5.1.7b; the goals note, Pr5.1.7c, collected on day 79). Respond: day 82.
- **Processes.** Create days 75 to 77; perform every day; respond days 65, 69, 73; connect days 65 (a segregated film
  industry) and 73 (a working company).
- **Candidate.** Kept: a fourth style's body designs from Africa or South Asia, from its community's own published
  teaching, inside day 69. No day added.

### Unit 6. Choosing what inspires

- **Calendar.** Course days 83 to 96, grade 7 school days 48 to 80 (band 208 to 240), weeks 10 to 16.
- **Arc.** Shen Wei's Rite of Spring (day 83), the source card (day 84), Deuce Coupe and styles chosen for an aim (day
  85) with its drill (day 86), tools and forms with reasons (day 87) and their drill (day 88), criteria that carry
  meaning (day 89); each student shapes a study (day 90), critique (day 91), rehearse with kept cards closed (day 92),
  run-through (day 93).
- **Why this order.** As unit 2, one step harder: sources are compared and chosen, styles are chosen for an aim, and
  every choice is explained. The study draws on unit 5's borrowed designs and accents.
- **Assessments.** Retrieval on day 84 (da-g6-ideas, da-g6-form, unit 2). Baseline look on days 86 and 88. End: day
  94, the showing (Cr2.1.7a with its spoken line; the source card, Cr1.1.7a, and criteria sheet, Cr2.1.7b, scored
  with these marks), and day 95, the written day (Cr1.1.7b). Respond: day 96.
- **Processes.** Create days 84, 86 to 93; perform every day; respond days 83, 85; connect days 83 (Chinese painting
  and opera, in the company's words) and 85.
- **Candidate.** Kept: one source card from a Native or African maker in the day 84 set. No day added.

### Year 7 mid-year check

Course day 97 (grade 7 school day 83, band 243, week 17), showing day; respond day 98 (school day 85).

### Unit 7. Weighing changes, comparing meanings

- **Calendar.** Course days 99 to 112, grade 7 school days 88 to 120 (band 248 to 280), weeks 18 to 24.
- **Arc.** L'Allegro's patterns (day 99), the Moiseyev piece contrasted with it (day 100), two meanings compared (day
  101), the criteria card refined (day 102) and the comparison drafted (day 103); motif notation (day 104) and its
  drill (day 105); the unit 6 study revised by weighing changes (day 106), critiqued (day 107), rehearsed with the
  change log and notation card collected (day 108); the comparison revised from feedback (day 109).
- **Why this order.** As unit 3: the comparison is drafted early so the written feedback returns before its revision
  day; the established notation is taught before the day that records the study. One Fluency day (day 105) beside
  the warm-up, for the same reason as unit 3.
- **Assessments.** Retrieval on day 100 (da-g6-revise, da-g6-respond, unit 3). Baseline look on days 105 and 106. End:
  day 110, the showing (Cr3.1.7a with the change log; the notation card, Cr3.1.7b), and day 111, the written day on an
  unseen phrase and two short descriptions (Re7.1.7a, Re7.1.7b, Re8.1.7a), with the revised comparison (Re9.1.7a).
  Respond: day 112.
- **Processes.** Create days 104, 106 to 109; perform every day; respond days 99 to 103, 111; connect days 100 and 101
  (stage folk dance and the village dances it came from; each dance's setting).
- **Candidate.** Kept: the Dance Notation Bureau's pages checked open and free when the unit plan is written. No day
  added.
- **Fallback.** A class that left out unit 6 learns a short Curio Class original study inside day 106.

### Unit 8. Where styles come from

- **Calendar.** Course days 113 to 126, grade 7 school days 123 to 155 (band 283 to 315), weeks 25 to 31. Family
  showing day 124 (week 30), written day 125 (week 31).
- **Arc.** Capoeira's history and spirit (day 113), tango compared with it (day 114), Weave and perspective (day 115),
  the research card for a style's history (day 116) and the lecture demonstration planned (day 117); preparing a
  performance with the rehearsal journal (day 118) and another venue (day 119); the spirit study built (day 120),
  critiqued with a note (day 121), rehearsed with the kept cards closed (day 122) and dress-run (day 123).
- **Why this order.** Two places' dances are compared before a style's history is researched, and the research comes
  before the spirit study it shapes; a style's history needs unit 7's comparing of styles.
- **Assessments.** Retrieval on day 114 (da-g6-stage, da-g6-connect, unit 4). Baseline look on days 117 and 118. End:
  day 124, the family showing (Pr6.1.7a with the journal; Cn10.1.7b with the research card; the venue card, Pr6.1.7b),
  and day 125, the written day (Cn10.1.7a, Cn11.1.7a). Respond: day 126.
- **Processes.** Create days 117, 120 to 122; perform every day; respond days 113 to 115; connect days 113 to 117 and
  124, 125.
- **Candidate.** Kept: the class list of styles checked for sources from each style's own community, before day 116.
  No day added.

### Year 7 year-end check

Course day 127 (grade 7 school day 158, band 318, week 32), written day; respond day 128 (school day 160).

## Year 8 (grade 8 ids, course days 129 to 192)

### Unit 9. Shaping space, layering time

- **Calendar.** Course days 129 to 146, grade 8 school days 3 to 45 (band 323 to 365), weeks 1 to 9.
- **Arc.** Juice and a second site dance (day 129), sculpting around people, props and the room (day 130), the Rosas
  chair section's breath phrasing and unequal phrases (day 131), sabar's layered time (day 132) and the layered-counts
  drill (day 133); texture (day 134), accuracy in copying and recalling (day 135) and its drill (day 136); the invented
  dancer's habits rated (day 137), personal goals and the progress record (day 138) and a site-phrase drill (day 139);
  groups build site phrases (day 140), critique (day 141), rehearse the change (day 142) and close the progress record
  (day 143).
- **Why this order.** Space before time, single tempos before layered ones, and both before texture; accuracy is
  taught before the progress record measures it. DA:Pr4.1.8b gets two teaching days and a drill because it is the
  heaviest step of the band. Three Fluency days (133, 136, 139) beside the warm-up: the unit owns six ids and its
  making days carry the site work.
- **Assessments.** Retrieval on day 130 (da-g7-elements, da-g7-technique, unit 5). Baseline look on days 133 and 136.
  End: day 144, the showing in school spaces (Pr4.1.8a, Pr4.1.8c look-fors; Pr4.1.8b and Pr5.1.8a show items), and
  day 145, the written day (Pr5.1.8b; the progress record, Pr5.1.8c). Respond: day 146.
- **Processes.** Create days 140 to 142; perform every day; respond days 129, 131, 132; connect days 129 (a museum as a
  site) and 132 (sabar's social and family uses).
- **Candidate.** Kept: a site dance by a living maker from Latin America or Asia beside Juice, inside day 129 (Latin
  America preferred, since unit 10's candidate is dropped). No day added.
- **Bridge.** Health 6 to 8 unit 26 (grade 8 weeks 18 to 22) comes later, so day 137 gives its own habit words.

### Unit 10. Making it together

- **Calendar.** Course days 147 to 160, grade 8 school days 48 to 80 (band 368 to 400), weeks 10 to 16.
- **Arc.** Grand Union (day 147), the material page (day 148), Pichet Klunchun and Myself with the student's own
  strongest moves (day 149) and their drill (day 150), making together with the process note (day 151) and its drill
  (day 152), criteria and their effect (day 153); groups build the original dance (day 154), critique (day 155),
  rehearse with the kept cards closed (day 156), run-through (day 157).
- **Why this order.** As unit 6, made with others: material and the student's own moves first, the group process
  next, criteria last before the build. The group dance draws on unit 9's sculpted shapes and layered time.
- **Assessments.** Retrieval on day 148 (da-g7-ideas, da-g7-form, unit 6). Baseline look on days 150 and 152. End: day
  158, the showing (Cr2.1.8a with the process note; the material page, Cr1.1.8a, and criteria sheet, Cr2.1.8b), and
  day 159, the written day (Cr1.1.8b). Respond: day 160.
- **Processes.** Create days 148, 150 to 157; perform every day; respond days 147, 149; connect days 147 and 149 (a
  collective's time and place; khon and the Thai royal court).
- **Candidate.** Dropped: a group-made dance by a Latin American company. The unit's two works already fill its study
  days and its making days carry the group dance; the region is carried by unit 9's kept candidate instead.

### Year 8 mid-year check

Course day 161 (grade 8 school day 83, band 403, week 17), showing day; respond day 162 (school day 85).

### Unit 11. Evidence for a judgment

- **Calendar.** Course days 163 to 176, grade 8 school days 88 to 120 (band 408 to 440), weeks 18 to 24.
- **Arc.** The class list and the chosen dance's patterns (day 163), elements across two styles (day 164), named
  moments as evidence (day 165), judging an effective performance with the analysis frame (day 166) and the analysis
  drafted (day 167); excerpt notation (day 168) and its drill (day 169); the unit 10 dance revised (day 170),
  critiqued (day 171), rehearsed with the excerpt notated (day 172); the analysis revised (day 173).
- **Why this order.** As units 3 and 7: the band's longest writing (about a page) is drafted early so its feedback
  returns before its revision day. Evidence-gathering comes before the judgment that uses it. One Fluency day (day 169).
- **Assessments.** Retrieval on day 164 (da-g7-revise, da-g7-respond, unit 7). Baseline look on days 169 and 170. End:
  day 174, the showing (Cr3.1.8a with the revision note; the Re7.1.8a show item; the excerpt, Cr3.1.8b), and day 175,
  the written day on the unseen phrase (Re7.1.8a, Re7.1.8b), with the revised analysis scored for Re8.1.8a and its
  closing judgment for Re9.1.8a. Respond: day 176.
- **Processes.** Create days 168, 170 to 173; perform every day; respond days 163 to 167, 175; connect days 163 and 166
  (each chosen dance's context).
- **Candidate.** Kept: every dance on the class list checked for an open, free linked page when the unit plan is
  written. No day added.
- **Fallback.** A class that left out unit 10 learns a Curio Class original group study inside day 170.

### Unit 12. Dances across eras, staged for two places

- **Calendar.** Course days 177 to 190, grade 8 school days 123 to 155 (band 443 to 475), weeks 25 to 31. Family
  showing day 188 (week 30), written day 189 (week 31).
- **Arc.** The court ballet of 1653 (day 177), the Charleston (day 178), the fancy shawl dance watched only, and the
  dances linked (day 179); the research card for two contrasting topics (day 180) and the study planned (day 181);
  leading preparation with the rehearsal record (day 182) and staging for two spaces (day 183); the study built (day
  184), critiqued with a student leading the warm-up (day 185), rehearsed in the second space with the kept cards
  closed (day 186) and dress-run in both spaces (day 187).
- **Why this order.** Many eras are studied before the class links them to a view; the research comes before the
  study; leading and staging are taught before the rehearsals that use them. Last in the band because analyzing many
  eras needs the styles studied across all three years.
- **Assessments.** Retrieval on day 178 (da-g7-stage, da-g7-connect, unit 8). Baseline look on days 181 and 182. End:
  day 188, the family showing in two spaces (Pr6.1.8a with the record and its plan; Pr6.1.8b with the staging design;
  Cn10.1.8b with the research card), and day 189, the written day (Cn10.1.8a, Cn11.1.8a). Respond: day 190.
- **Processes.** Create days 181, 184 to 186; perform every day; respond days 177 to 179; connect days 177 to 181 and
  188, 189.
- **Candidate.** Kept: the topic list checked for party politics and for any topic that asks a student to tell their
  own hardship, before day 180. No day added.

### Year 8 year-end check

Course day 191 (grade 8 school day 158, band 478, week 32), written day; respond day 192 (school day 160).

## Course-level checks

| Check | Course day (school day, week) | Kind | Samples | Respond |
|---|---|---|---|---|
| Year 6 mid-year | 33 (83, week 17) | Showing | DA:Pr4.1.6a, DA:Pr4.1.6b, DA:Pr5.1.6a (frame), DA:Pr4.1.6c (show item, this scope) | 34 (85) |
| Year 6 year-end | 63 (158, week 32) | Written | DA:Pr5.1.6b, DA:Cr1.1.6b, DA:Re9.1.6a, DA:Re7.1.6a | 64 (160) |
| Year 7 mid-year | 97 (83, week 17) | Showing | DA:Pr4.1.7a, DA:Pr4.1.7b (frame), DA:Pr5.1.7a (show item, this scope) | 98 (85) |
| Year 7 year-end | 127 (158, week 32) | Written | DA:Pr4.1.7c, DA:Cr2.1.7b, DA:Re8.1.7a, DA:Re7.1.7a | 128 (160) |
| Year 8 mid-year | 161 (83, week 17) | Showing | DA:Pr4.1.8a, DA:Pr5.1.8a, DA:Pr4.1.8b (frame), DA:Pr4.1.8c (look-for, this scope) | 162 (85) |
| Year 8 year-end | 191 (158, week 32) | Written | DA:Pr5.1.8b, DA:Cr2.1.8b, DA:Re9.1.8a, DA:Re8.1.8a | 192 (160) |

School days are each grade's own year. The weeks are CALENDAR.md's for this course in each of grades 6, 7 and 8:
week 17 is free of every core check, and school day 83 is shared only with the other arts electives (visual arts,
media arts, theater), which count as one course under stagger rule 3; physical education (day 82), health (day 84)
and English language development (days 81 and 82) sit on other days. Week 32 is the finals week.

- **Checks that do not repeat.** Each mid-year check comes right after the end-of-unit assessment of unit 2, 6 or 10,
  so it draws its items only from the year's first unit (1, 5 or 9) on new material; the just-assessed unit's records
  are carried unscored and none of its ids is scored again. Each year-end check comes two sessions after the
  performance unit's written day, samples the year's first three units on new material, and leaves the performance
  unit to its own family showing. A check claims only the codes in the table, each taught and assessed in a unit
  first; each item asks about every part of each code it lists. Rule 2's "never repeats a task form given in the
  last two weeks" is read as the same item (the same prompt type on the same work or content), not the kind of check
  day (lead call 6, 2026-11-26): a showing is the discipline's own evidence and may follow a unit showing, and each
  check's items are new, so each check day's note says the rule is met. No check cell re-asks an item a unit gave one
  to three days before (Collect once): the mid-year checks sample unit 1, 5 or 9, not the unit just assessed, and the
  year-end checks sample units 1 to 3 of the year, not the performance unit two sessions before (lead call 7 checked).
- **New material taught first.** The mid-year showings dance new material; it is taught, unscored, in the last ten
  minutes of the respond day before (days 32, 96 and 160) from a Curio Class step card of about 16 counts, and the
  check day's warm-up runs it once. On the once-a-week path that block sits in the unit's session 8.
- **Item wording, so each code's every part is asked.** Day 33: the new piece has a three-beat and a four-beat part,
  with one sudden and one sustained change (DA:Pr4.1.6b). Day 63: the critique names the repeating patterns and how
  one relates to another (DA:Re7.1.6a). Day 127: one line on how to perform each quality clearly (DA:Pr4.1.7c); the
  patterns compared, alike and different, and how they link (DA:Re7.1.7a). Day 161: the layered phrase includes one
  breath phrase, its choice named (DA:Pr4.1.8b). Day 191: criteria defined, then applied to a described new group
  dance, and their effect (DA:Cr2.1.8b); how two elements in two named moments create the phrase's expression, a
  prompt of its own apart from the judgment (DA:Re8.1.8a).
- **Added samples.** The frame allows one show item per student and three to five look-fors; this scope fills that room
  with one more owned code in each mid-year check (marked "this scope"), so more codes are sampled at the course level.
- **Codes not sampled at a course-level check, and why** (rule 3). Each was taught and assessed in its own unit.

| Year | Codes | Why not |
|---|---|---|
| 6 | DA:Pr5.1.6c, DA:Cr1.1.6a, DA:Cr2.1.6b, DA:Cr3.1.6a, DA:Cr3.1.6b | Each is evidenced by a kept product built over several rehearsal or making days (the rehearsal log, the inspiration list, the criteria sheet, the revision note, the tested notation); one 40-minute session cannot make a fresh one. |
| 6 | DA:Cr2.1.6a | A study of about 32 counts needs several making days; unit 2 assessed it three sessions before the mid-year check, and the frame carries those records. |
| 6 | DA:Re7.1.6b, DA:Re8.1.6a | The year-end written day holds three items in 28 minutes; the frame gives them to the warm-up plan, the styles note and the critique with patterns. Both were assessed on day 47 on an unseen phrase. |
| 6 | DA:Pr6.1.6a, DA:Pr6.1.6b, DA:Cn10.1.6a, DA:Cn10.1.6b, DA:Cn11.1.6a | Unit 4, assessed by its own family showing and written day two to three sessions before the year-end check; the frame carries its records unscored. |
| 7 | DA:Pr5.1.7b, DA:Pr5.1.7c | The habit card was assessed on day 81 and the year-end written day samples unit 5 through DA:Pr4.1.7c; the goals note is a kept product of several rehearsals. |
| 7 | DA:Cr1.1.7a, DA:Cr1.1.7b, DA:Cr2.1.7a | Unit 6, assessed three sessions before the mid-year check (records carried); DA:Cr2.1.7b stands for the unit at the year-end. The source card is a kept product. |
| 7 | DA:Cr3.1.7a, DA:Cr3.1.7b, DA:Re7.1.7b, DA:Re9.1.7a | Kept products (the change log, the notation card) and a written comparison revised over days; DA:Re7.1.7b's contrast was assessed on day 111, and the year-end written day holds three items. |
| 7 | DA:Pr6.1.7a, DA:Pr6.1.7b, DA:Cn10.1.7a, DA:Cn10.1.7b, DA:Cn11.1.7a | Unit 8, assessed by its own family showing; records carried. |
| 8 | DA:Pr5.1.8c, DA:Cr1.1.8a, DA:Cr1.1.8b, DA:Cr2.1.8a | The progress record and the material page are kept products; DA:Cr1.1.8b and DA:Cr2.1.8a belong to unit 10, assessed three sessions before the mid-year check (records carried); DA:Cr2.1.8b stands for unit 10 at the year-end. |
| 8 | DA:Cr3.1.8a, DA:Cr3.1.8b, DA:Re7.1.8a, DA:Re7.1.8b | Kept products (the revision note, the notated excerpt); DA:Re7.1.8a and DA:Re7.1.8b were assessed on days 174 and 175, and the year-end written day holds three items. |
| 8 | DA:Pr6.1.8a, DA:Pr6.1.8b, DA:Cn10.1.8a, DA:Cn10.1.8b, DA:Cn11.1.8a | Unit 12, assessed by its own family showing; records carried. |

## Cross-subject leans on the calendar

| Lean | Other subject's days (data/plans/calendar.csv) | Here | Bridge |
|---|---|---|---|
| Physical education 6 to 8 dance units (grade 6 unit 6, weeks 22 to 26; grade 7 unit 13, weeks 22 to 26; grade 8 unit 18, weeks 14 to 16) | After units 1, 5 and 9 (weeks 1 to 9) | Days 11, 75 and 140 note it | None needed: dance teaches first and assumes no physical education step |
| Physical education grade 8 unit 22 (weeks 28 to 31), capoeira | A year after unit 8 | Day 113 notes the planned return | None needed |
| Health 6 to 8 unit 26 (grade 8 weeks 18 to 22) | After unit 9 | Day 137 | The day gives its own habit words, with no health step |
| ELA grade 6 unit 1, SL.6.1 (weeks 1 to 7) | Before unit 3 (weeks 18 to 24) | Day 37 | None needed; practiced, not owned |
| ELA grade 8 unit 2, W.8.1 (weeks 7 to 13) | Before unit 11 (weeks 18 to 24) | Day 166 | None needed; the analysis frame still gives claim, evidence and reasoning |
| Social studies grade 6 unit 8, Silk Roads exchange (school days 100 to 113, weeks 20 to 23) | Before unit 4 (weeks 25 to 31) | Day 50 | The work card names the trade; its three setting lines serve a class that has not met it |

No unit asks for fractions, ratios or time signatures as math: counts are spoken and clapped.

## Sensitivity and leave-out

Each flagged day names its flag in the note: stepping (day 1), butoh (day 5), the invented dancer for food and body
(days 9, 72, 137), Rome & Jewels and hip-hop (day 35), The Green Table (day 49), the Tang tomb figurines (day 50),
Kaha:wi (day 51), the issue and topic lists (days 52, 180), the Nicholas Brothers (day 65), growing bodies (day 70),
Dance Theatre of Harlem (day 73),
Shen Wei (day 83), the Moiseyev company (day 100), capoeira (day 113), Weave (day 115), sabar (day 132), khon (day
149), the class-list dances of unit 11 (day 163), the Charleston (day 178) and the fancy shawl dance (day 179). A
school or family may leave out unit 4, the Pichet Klunchun work in unit 10 or the fancy shawl dance in unit 12, as the
frame's Leave-out bullet says; leaving out a whole unit names its ids not claimed that year on the course page and
in the family note.

## Shorter path

**The once-a-week path (32 sessions a year).** Every unit and every id stays. Each day's note names its session:
units 1, 5 and 9 run in 8 sessions (weeks 1 to 8), units 2, 6 and 10 in 8 (weeks 9 to 16), each mid-year check in 1
session (week 17) with its respond session (week 18), units 3, 4, 7, 8, 11 and 12 in 6 sessions each (weeks 19 to 24
and 25 to 30), each year-end check in 1 session (week 31) with its respond session (week 32). The merges keep, in
this order: the demonstration with a step card opened by the study of a dance (session 1); a rehearsal session with
the critique; the showing; and the respond session. Fluency days fold into the warm-ups and the two rows'
understanding days merge. No merge drops a critique, a rehearsal before a showing, a revision or a respond day. On
this path the course gives 40 minutes a week, 50 short of the dance educators' 90 (frame, Days bullet). Unit days
below count from the unit's first day.

- **Units 2, 6 and 10: the written day keeps a session.** Sessions: 1 unit days 1 and 2; 2 days 3 and 4; 3 days 5 to
  7; 4 days 8 and 9; 5 days 10 and 11; 6 the written day (unit day 13) alone, with unit day 11's run-through danced
  once as its warm-up; 7 the showing (unit day 12); 8 the respond day. Course days: 19 to 32, 83 to 96, 147 to 160.
- **The other nine units: timed blocks.** Their sessions have no room for a 37-minute written day, so on this path
  only its items run as one or two timed blocks of about 12 minutes at the close of a later rehearsal session, each a
  session or more after the part it assesses is taught (the unseen phrase danced at the block's start), one prompt
  per part, scored after the session like a kept product. This is the path's one exception to "two check days, never
  mixed" (frame, once-a-week bullet). Units 1 and 9 (one item): the block closes session 6 (unit days 13 to 15).
  Unit 5: block A (the habit card) closes session 5, block B (the qualities compared) closes session 6. Units 3, 7
  and 11: block A closes session 3 (unit days 8 and 9), block B session 4 (unit days 10 and 11). Units 4, 8 and 12:
  block A (the like-me or linking item) closes session 3, block B (the work card or cultures item) session 4.
- **Units 4, 8 and 12: the research card starts in session 1.** Its first ten minutes (days 52, 116 and 180) move to
  the last ten minutes of session 1, after the hook, so the card is not begun and planned in one quarter session.

**A shorter period.** On a period of 30 to 39 minutes, set-up and room back stay; the warm-up drops to 3 minutes, the
teaching shortens, and a drill runs twice instead of three times. A showing day keeps all six groups by cutting the
warm-up to 2 minutes and moving the self-check to the next session's opening; show items are given at the teacher's
spot in that opening. Nothing assessed moves out of its unit.

**A year about 10 school days short.** Ten school days are two weeks, which is 4 sessions of this course (lead
call 1, 2026-11-26). Each year folds in four Fluency days, each saving 40 minutes; nothing on them is assessed and no
owned part is cut, because their runs move into the named next day's warm-up and opening. The folds sit in the
18-day units and the making units, which hold three or four Fluency days each, so the revising units keep their only
notation drill and every dress run stays (in year 8 one revising-unit fold is kept, day 169, because units 9 and 10
then keep one Fluency day each). Where a fold day carries the baseline look, its last rotating group is observed in
the next day's opener.

| Year | Fold-in days (their work goes to) | Minutes saved |
|---|---|---|
| 6 | 10 (11), 14 (15), 22 (23), 29 (30's warm-up only) | 160 |
| 7 | 74 (75), 78 (79), 86 (87), 93 (94's warm-up only) | 160 |
| 8 | 139 (140), 150 (151), 157 (158's warm-up only), 169 (172) | 160 |

Total: 12 fold-in days, 480 minutes; the band runs 180 of the frame's 192 days (60 a year). The days are marked
"Shorter year: fold-in day" in their notes.

## Candidate cells settled

| Unit | Candidate | Settled |
|---|---|---|
| 1 | A three-beat social dance from outside Europe beside Strauss | Kept, inside day 3, no day added |
| 2 | An inspiration from a maker outside the United States | Kept, on the day 20 card set, no day added |
| 3 | A third style from Asia or Latin America for the element comparison | Dropped: the id asks for two styles, the unit holds six ids in 14 days, and year 6 already studies Japan, China and Central Asia |
| 4 | The issue list checked for party politics and personal hardship | Kept, by the unit plan before day 52, no day added |
| 5 | A fourth style's body designs from Africa or South Asia | Kept, inside day 69, no day added |
| 6 | A source from a Native or African maker | Kept, on the day 84 card set, no day added |
| 7 | The Dance Notation Bureau's pages checked open and free | Kept, a unit plan task, no day added |
| 8 | The class list of styles checked for community sources | Kept, before day 116, no day added |
| 9 | A site dance by a living maker from Asia or Latin America | Kept, inside day 129 (Latin America preferred), no day added |
| 10 | A group-made dance by a Latin American company | Dropped: unit 10's study days are full and its making days carry the group dance; unit 9's kept candidate carries the region |
| 11 | Every class-list dance checked for an open linked page | Kept, a unit plan task, no day added |
| 12 | The topic list checked for party politics and personal hardship | Kept, before day 180, no day added |

## For the lead

The writer's five items of 2026-11-26 were settled by the expert read and the fix pass
(docs/reviews/sequence-dance-grades-6-to-8-fixes-2026-11-26.md):

1. **Mid-year checks: one sample added each** (DA:Pr4.1.6c, DA:Pr5.1.7a show items; DA:Pr4.1.8c look-for). Agreed
   by the read; the frame's Course-level checks table now names them.
2. **Task form within two weeks.** Settled by lead call 6: the rule is about the same item, not the kind of check
   day; nothing in the frame changes.
3. **Fluency days in the 14-day units.** Agreed; the frame's Day kinds bullet now says one to three in the 14-day
   units, beside the daily warm-up.
4. **"The unit's waltz" in unit 4.** Agreed; the frame now says unit 1's waltz, and day 3 teaches its setting.
5. **Once-a-week written day.** Replaced by the timed-block exception and the units 2, 6 and 10 re-merge (Shorter
   path); the frame's once-a-week bullet now names the exception.
