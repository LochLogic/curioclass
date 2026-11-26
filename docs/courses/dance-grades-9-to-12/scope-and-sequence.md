# Scope and sequence: Dance, grades 9 to 12

Course `dance-grades-9-to-12` (catalog id `dance-9-12`), the high school band of dance, run as Levels 1 to 4; draft, written 2026-11-26 from the frame (docs/courses/dance-grades-9-to-12/frame.md); the fix pass of the same day (docs/reviews/sequence-dance-grades-9-to-12-fixes-2026-11-26.md) changed the frame only in its short-path counts and unit 8's evidence line. The days are in data/plans/dance-grades-9-to-12/days.csv.

## How to read this file

- **Levels, not grades.** The band runs as four levels, one full year each: Level 1 (Proficient), Level 2
  (Accomplished), Level 3 (Advanced, at honors depth) and the optional Level 4 (Advanced, deepened, a year the student
  leads). A student new to dance starts at Level 1 whatever their grade. No page names a grade for a level; the grade
  keys 9 to 12 in data/progressions/arts.csv are data keys only.
- **Which standards fall in which level** (the bar's "Scope and sequence states"). National Core Arts Standards, 2014,
  dance, by id only. Level 1 claims the 21 Proficient ids (`.Ia`, `.Ib`, `.Ic`: `DA:Cr1.1.Ia` to `DA:Cn11.1.Ia`);
  Level 2 the 21 Accomplished ids (`.II`); Level 3 the 21 Advanced ids (`.III`): 63 in all, every one taught and
  assessed in its own level, the count in docs/courses/arts/STANDARD.md 3.2. Level 4 owns no id: it assesses 11 of the
  Level 3 ids again on new, self-directed work (units 16 to 19). No grade 8 id is claimed anywhere; the Level 1 bridge
  teaches grade 8 techniques and words as readiness only.
- **Course days and school days.** days.csv numbers the band's 640 course days in order: Level 1 is course days 1 to
  160, Level 2 161 to 320, Level 3 321 to 480, Level 4 481 to 640. The course meets five 45-minute lessons a week, so
  inside a level course day and school day are the same. School days are counted inside each level (1 to 160), since
  the levels are taken in separate years: course day n falls on school day ((n - 1) mod 160) + 1 of that level's year,
  in week ((that school day - 1) // 5) + 1. That is why `school_day` is blank (sequence-write.md: blank for a course
  that meets every school day); scripts/frame.py places each level on its own year, and every unit and check falls in
  the frame's weeks by this formula. Below, "day" means the course day of days.csv; level days and weeks are given
  beside it.
- **More than one level in one room.** Levels 1 to 3 share the same five slots (opening, body and rehearsal, making,
  watching and changing, production), each student on their own level's rows, ids, guide and checks; the warm-up, the
  works watched and the concert are shared. The slots hold only roughly at once: Level 1's body unit starts on level
  day 13 and Levels 2 and 3 on level day 7, unit lengths differ (38 against 40, 34 against 34, 38 against 40, 34
  against 36), and the mid-year checks fall on level days 85 (Level 1) and 81 (Levels 2 and 3). The rule: the room
  follows Level 1's calendar. Level 2 and 3 students run their review unit on level days 1 to 6, then work as phrase
  leaders in the bridge's days 7 to 12; each level keeps its own check days, which fall in the same weeks (17 and 32).
  A full mixed-room calendar is a course page item (For the lead 6). Level 4 students in the room work as
  choreographers and rehearsal directors beside the slot the class runs.
- **The day block.** Every dancing day: set-up 3, warm-up 7, the teaching, dancing or writing, cool-down with the
  closing line or log entry 4, room back 3. Each owning unit's day 2 holds the ten-minute retrieval after the warm-up
  (set-up 3, warm-up 7, retrieval 10, teaching 18, cool-down 4, room back 3), and day 1 stays clean for the hook and
  the compelling question. A showing day runs six groups of five for about 4 minutes each; a written sitting runs
  set-up 2, the unseen phrase danced twice or the description read (about 4), items alone (about 33), collecting 3.
- **The four processes.** Each level carries all four artistic processes (creating; performing; responding;
  connecting), and each unit touches at least the processes the frame names for it; a unit need not claim all four,
  and no unit claims an id outside its owned rows. Where a process is practiced on an existing day (a setting card, a
  short response), it costs no day and claims no id. Each unit section names the days. Technique and understanding
  days come before the making that needs them, and every end-of-unit showing has the unit's critique (describe, ask,
  suggest) and a revision before it; mid-unit showings have a peer look-for check instead.
- **Safety and supplies.** The optional tools, supplies and safety columns are for math and science only, so the
  note column names a day's floor, space and production rules where they matter (the frame's safety bullet: a clear,
  checked floor, bare feet or soft soles, warm-up first, no lifts, low balances by agreement, jumps from the floor with
  landings first on a resilient floor, no inversions, no ladders, haze or strobe). Every day runs on the free path:
  floor tape or chalk, the voice or claps for the beat, printed cards, plain clothes in one color.
- **Sensitivity.** Each day that studies a work the frame flags (ritual, sacred or ceremonial, hard history, beauty
  ideals, invented-dancer food plans) names the flag in its note. Every unit gets the fresh sensitivity and safety
  (moving) agents' reads with its unit plan.

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Five 45-minute lessons a week, 32 weeks a level; a cleared floor; step cards, work cards, notation sheets and the process log; one optional teacher device and one shared school recording device | Phrases and elements taught in steps; dances watched with their setting; making and rehearsing with one critique and a revision each unit; written analysis; a showing each unit and a concert each level (a led showing and a capstone talk in Level 4) | A portfolio across the levels (one piece a unit, with a one-line reflection); a concert a level; two marks a unit per student on the main look-for (the baseline look in the first practice days and the end check) | Met marks on the level's 21 ids (Levels 1 to 3); the Level 3 ids met again on new work (Level 4); growth on the look-fors. Nothing here has been tried with students, and Curio Class claims no effect of arts study on any other result. |

## Level 1 (Proficient, the 21 `.I` ids): course days 1 to 160

Units 1 to 5, with the mid-year check on days 85 and 86 and the year-end check on days 159 and 160.

### Unit 1. The dancer's toolkit (bridge)

- **Days:** 1 to 12 (level days 1 to 12, weeks 1 to 3). 12 days, the most STANDARD.md 3.2 allows.
- **Arc:** the class warm-up and cool-down first (every later day uses them), then the elements and energy words on the
  1898 Ella Lola film, accent and timing with a 16-count phrase, phrase recall, the four choreographic tools, the
  inspiration list and style words, the critique routine and the process log, motif symbols with describe and
  interpret, and stage terms with the connecting routines; a group rehearsal and the bridge showing close it.
- **Order:** the warm-up and elements come before any phrase; the phrase exists before the tools reshape it; the
  critique routine and log come before the showing that uses them.
- **Readiness:** the bridge assumes no earlier dance. It teaches the grade 8 rows' techniques and words (da-g8-ideas to
  da-g8-connect, named in each day's note) to every student, as readiness, and claims no id. Day 11's showing holds
  the readiness record (phrase recalled, an element named in the film, eight counts in motif symbols); it carries
  `assess` = `end` because the gate needs an end day in every unit, and it scores no standard. Its results shape the
  first days of units 2 and 3. Response time: day 12.
- **Processes:** creating 5, 6, 10; performing 1, 3, 4, 10, 11; responding 2, 7, 8; connecting 9.
- **Candidate:** a second short public domain film from outside the United States for the elements look: **dropped**.
  The bridge is readiness only, and Level 1's range starts on day 18 (South Africa), then Germany, the United Kingdom
  and Belgium, the Netherlands, Denmark and Sierra Leone; a second film needs its own record check for one look.

### Unit 2. Body, rhythm and rehearsal

- **Days:** 13 to 50 (level days 13 to 50, weeks 3 to 10). 38 days, six owned ids, three performed live.
- **Arc:** accents, syncopation, cues and breath first (DA:Pr4.1.Ib), then energy through the whole body on Gula
  Matari (DA:Pr4.1.Ic), a small-group section, and the invented dancer's habits plan (DA:Pr5.1.Ib) drafted and revised
  around the mid-unit showing. The second half teaches low balances and transitions (DA:Pr4.1.Ia), the 32-count phrase
  (DA:Pr5.1.Ia) and rehearsal planning with an observer's sheet (DA:Pr5.1.Ic), then the partner and group section,
  the critique (day 42), the revision (day 43) and the end showing.
- **Order:** rhythm before dynamics, because the section needs both; balances only after the transitions drill; the
  rehearsal plan is taught after the phrase exists, so there is something to rehearse.
- **Retrieval:** day 14, ten minutes: the bridge's elements, accent and timing, warm-up and phrase recall
  (`retrieves` da-g8-elements; da-g8-technique). Grade 8 rows are one grade back by number and the bridge taught them
  days ago, so retrieval, not a readiness check.
- **Assessments:** mid-unit showing day 30 (unit day 18) on DA:Pr4.1.Ib and DA:Pr4.1.Ic; respond day
  31. End: day 47 showing (DA:Pr4.1.Ia, DA:Pr5.1.Ia, one full performance), day 48 kept pieces (DA:Pr5.1.Ib, DA:Pr5.1.Ic,
  drafted on days 25, 39 and 44, given written feedback, revised on days 28 and 45); response time day 49.
- **Processes:** creating 22, 40, 42; performing 14 to 30, 32 to 47; responding 13, 18, 21, 42; connecting 13 (tap's
  roots and the PE boundary), 24 (habits and the health lean).
- **Leans:** PE grade 9 unit 5 ("Dance by design") sits in weeks 22 to 26, after this unit, so day 13 names the
  boundary and the unit assumes no PE cue. Health's habits unit may fall in either half or another grade; day 24
  teaches the dance habits itself.
- **Candidate:** a third rhythm work from Asia: **dropped**. Unit 4 (day 91) now holds Level 1's Asian work, and this
  unit's 38 days carry six performed and planned ids.

### Unit 3. Making a dance

- **Days:** 51 to 84 (level days 51 to 84, weeks 11 to 17). 34 days, four owned ids.
- **Arc:** sources tried and analyzed (DA:Cr1.1.Ia), the strengths test and two demanding moves (DA:Cr1.1.Ib), a study,
  the mid-unit assessment; then the four structures (DA:Cr2.1.Ia), group making for a stated purpose, the artist's
  statement (DA:Cr2.1.Ib), the critique (day 75), the revision (day 76), the end showing and statement.
- **Order:** sources and strengths come first because the group dance is built from them; structures are taught before
  groups choose one; the statement is drafted after the dance has a shape and revised after the critique.
- **Retrieval:** day 52: the bridge's inspiration list, movement challenge, start, middle and finish, and the four
  tools (`retrieves` da-g8-ideas; da-g8-form).
- **Assessments:** mid day 62 (DA:Cr1.1.Ia log entry; DA:Cr1.1.Ib strengths test and moves at the teacher's spot);
  respond day 63. End: day 80 showing (DA:Cr2.1.Ia with the spoken line), day 81 statement (DA:Cr2.1.Ib); response
  time day 82.
- **Processes:** creating 54 to 61, 68 to 81; performing 60, 74, 78 to 80; responding 51, 53, 65, 83; connecting 53
  (a place as a source), 67 (the PE boundary), 83.
- **Lean:** day 67 names PE grade 9 unit 5 (weeks 22 to 26, later this year for a grade 9 student): PE designs a
  phrase as a movement problem; dance owns intent and the statement.
- **Candidate:** a choreographer from Africa or Latin America whose source is a place: **kept**, as a Latin American
  work card on day 53 (about 15 minutes of that day, no day added), since Level 1 has three African makers and no
  Latin American one. The unit plan picks it outside every other dance frame, with its rights line.

### Unit 4. Seeing patterns, changing a dance

- **Days:** 87 to 124 (level days 87 to 124, weeks 18 to 25). 38 days, six owned ids, four of them written response.
- **Arc:** patterns and relationships (DA:Re7.1.Ia) on Sinfonietta, intent in setting (DA:Re7.1.Ib) on Niicugni,
  Exit/Exist and an Asian work, practice analysis, then the unit 3 dance reworked by device and structure
  (DA:Cr3.1.Ia) and the criteria card, the mid-unit sitting; then two notation methods (DA:Cr3.1.Ib), comparing dances
  (DA:Re8.1.Ia), analyzing expression with criteria (DA:Re9.1.Ia), the critique (day 114), the revision (day 115) and
  the end showing and sitting.
- **Order:** analysis words before the sitting that asks for them;
  the rework uses the bridge's criteria card, retrieved on day 88; the evaluation criteria for analysis follow on day 99;
  notation follows the revision so the revised section is what gets recorded.
- **Retrieval:** day 88: the bridge's try-a-change, motif symbols, describe and interpret and the criteria card, and
  unit 3's structures and devices, used earlier this level (`retrieves` da-g8-revise; da-g8-respond; da-g9-form). Day 88
  also models the analysis frame (the ELA lean's bridge).
- **Assessments:** mid day 102 (written sitting: DA:Re7.1.Ia on the unseen Curio Class phrase; DA:Re7.1.Ib on two short
  written descriptions from two traditions, each with its stated setting, written by Curio Class from the work cards'
  facts); respond day 103. End: day 119 showing
  (DA:Cr3.1.Ia), day 120 sitting and kept pieces (DA:Re9.1.Ia written; DA:Re8.1.Ia comparison and DA:Cr3.1.Ib notation
  handed in); response time day 121.
- **Processes:** creating 95 to 98, 104 to 108, 115, 117 to 119, 124; performing 98, 100, 117 to 119; responding 87 to
  94, 99 to 102, 109 to 116, 120; connecting 89 to 91 (settings), 122.
- **Candidate:** a dance from Asia for the comparison: **kept**, as day 91's work card (no day added); it is Level 1's
  only Asian maker beside Akram Khan's story.

### Unit 5. The concert and the question

- **Days:** 125 to 158 (level days 125 to 158, weeks 25 to 32). 34 days, five owned ids.
- **Arc:** a dance's ideas and its maker's view (DA:Cn10.1.Ia) on Kykunkor, two periods compared (DA:Cn11.1.Ia) with La
  Sylphide, team research questions (DA:Cn10.1.Ib), the mid-unit assessment; the answer dances, the comparison with
  another field's procedure, rehearsal leadership and documented methods (DA:Pr6.1.Ia), production design options
  (DA:Pr6.1.Ib), the critique (day 145), the revision (day 146), the technical and full runs, the dress rehearsal, the
  concert and the process record.
- **Order:** research before the answer dance; design options are judged after the dances exist; the dress rehearsal
  is the scored rehearsal so a senior leaving early still has a concert mark.
- **Retrieval:** day 126: the bridge's stage terms and etiquette, research notes and the like-me line, and unit 2's
  rehearsal plan, used earlier this level (`retrieves` da-g8-stage; da-g8-connect; da-g9-technique).
- **Assessments:** mid day 134 (DA:Cn10.1.Ia written item; DA:Cn11.1.Ia comparison); respond day 135. End over three
  days: day 153 dress rehearsal (DA:Pr6.1.Ia), day 154 the concert (week 31; DA:Cn10.1.Ib, DA:Pr6.1.Ib), day 155 the
  process record; response time day 156.
- **Processes:** creating 136, 137, 146; performing 140 to 155; responding 125, 127, 145, 157; connecting 125 to 134,
  138, 139, 149, 157.
- **Sensitivity:** Kykunkor is studied by reading and watching only (days 125 and 157); the unit may be left out.
- **Candidate:** a third period's dance from Asia: **dropped**. DA:Cn11.1.Ia asks for two periods, and unit 4 holds
  Level 1's Asian work.

## Level 2 (Accomplished, the 21 `.II` ids): course days 161 to 320

Units 6 to 10, with the mid-year check on days 241 and 242 (level days 81 and 82) and the year-end check on days 319
and 320 (level days 159 and 160).

### Unit 6. Back on the floor (review and placement)

- **Days:** 161 to 166 (level days 1 to 6, weeks 1 to 2).
- **Arc:** the warm-up, balances and syncopation; Sinfonietta revisited for the criteria card and motif notation; the
  statement and research notes on each portfolio piece; a rehearsal; the review showing and placement; a second try.
- **Readiness:** Level 2 rows assume their Level 1 rows, which for a student in consecutive years were used the year
  before, so each Level 2 unit opens with day 2 retrieval. For a student returning after a gap or new to the school,
  day 165's review showing is the readiness check and placement showing, scored against the Level 1 year-end check and
  unit 5's guide; it carries `assess` = `end` (no Level 2 id is scored) and its note says so.
- **Processes:** creating 163; performing 164, 165; responding 162, 165; connecting 163 (research notes).
- **Candidate:** a self-check form a student new to the school fills in before day 1: **kept**, no day cost (it is
  filled before the course starts, with the counselor).

### Unit 7. Space, time and the body's care

- **Days:** 167 to 206 (level days 7 to 46, weeks 2 to 10). 40 days, six owned ids.
- **Arc:** ground then aerial sequences with landings first (DA:Pr4.1.IIa), unpredictable time and spontaneous
  response (DA:Pr4.1.IIb), a group passage and the mid-unit showing; anatomy and the invented dancer's eating plan
  (DA:Pr5.1.IIb), energy at each start and transitions (DA:Pr4.1.IIc), demanding sequences with set goals
  (DA:Pr5.1.IIa), solo and group rehearsal plans (DA:Pr5.1.IIc), the critique (day 197), the revision (day 198) and the
  end showing and kept pieces.
- **Retrieval:** day 168: Level 1's balances, syncopation and rehearsal plan (`retrieves` da-g9-elements;
  da-g9-technique).
- **Assessments:** mid day 183 (DA:Pr4.1.IIa, DA:Pr4.1.IIb); respond day 184. End: day 202 showing (DA:Pr4.1.IIc,
  DA:Pr5.1.IIa, the live parts of DA:Pr5.1.IIb and DA:Pr5.1.IIc), day 203 kept pieces (the anatomy note and eating plan;
  the rehearsal plans and reflection); response time day 204.
- **Processes:** creating 175, 189; performing 168 to 183, 185 to 203; responding 167, 170, 200, 205; connecting 170
  (Benguelê's setting), 180 (the body and daily habits).
- **Candidate:** a work from Asia with ground work: **dropped**. Level 2's Asian work is Dancing Grandmothers (unit 9),
  and two works already carry the six performed ids.

### Unit 8. Blending styles

- **Days:** 207 to 240 (level days 47 to 80, weeks 10 to 16). 34 days, four owned ids.
- **Arc:** invented and established movement (DA:Cr1.1.IIa), Push Comes to Shove and Pavement, blending strengths with
  styles (DA:Cr1.1.IIb), the study and the comparison with Tharp and Abraham, the mid-unit assessment; composition and
  design (DA:Cr2.1.IIa) alone and with others (day 224: each student designs one solo passage of at least 8 counts
  inside the group dance, duet version allowed), the statement of aesthetic (DA:Cr2.1.IIb), the critique (day 229), the
  revision (day 230) and the end showing and statement. The last day looks over unit 7's plans in the log before the mid-year sitting
  (practice, nothing new).
- **Retrieval:** day 208: Level 1's sources, strengths test and artist's statement (`retrieves` da-g9-ideas;
  da-g9-form).
- **Assessments:** mid day 218 (DA:Cr1.1.IIa, DA:Cr1.1.IIb); respond day 219. End: day 234 showing (DA:Cr2.1.IIa: the
  group structure and each student's solo or duet passage inside it; DA:Cr2.1.IIb chosen movements), day 235 statement;
  response time day 236. The frame's unit 8 evidence line names the solo passage (changed in this fix pass).
- **Processes:** creating 209 to 218, 220 to 235; performing 214, 217, 218, 228, 232 to 234; responding 207, 210, 229,
  237; connecting 208 (a community's own teaching rule), 237.
- **Candidate:** a choreographer from Asia or Africa who blends styles: **dropped**. DA:Cr1.1.IIb names two known
  choreographers, and unit 9 brings Africa (the 2021 Rite with the École des Sables) and Korea.

### Unit 9. One dance, three times

- **Days:** 243 to 282 (level days 83 to 122, weeks 17 to 25). 40 days, six owned ids.
- **Arc:** the 1913 Rite and its riot, patterns that build form and meaning (DA:Re7.1.IIa), Bausch's Rite and setting
  (DA:Re8.1.IIa), the 2021 staging and Dancing Grandmothers compared across traditions (DA:Re7.1.IIb), refining unit
  8's dance against criteria (DA:Cr3.1.IIa), the mid-unit sitting; the recording plan (DA:Cr3.1.IIb), critique weighing
  societal values (DA:Re9.1.IIa), a described work card on social dance across eras (day 268) and the values talk (day
  269), the critique (day 270), the refinement (day 271), a second practice day on the written ids (day 272), the
  revisions, the recording plan carried out on one more section (day 275), and the end showing and kept pieces. After
  the respond day only the portfolio choice (day 281) and unit 10's setup (day 282) remain.
- **Retrieval:** day 244: Level 1's notation methods, change log and criteria card, and unit 8's dance and its
  structure, used earlier this level (`retrieves` da-g9-revise; da-g9-respond; da-g10-form); the analysis frame is
  modeled the same day (ELA bridge).
- **Assessments:** mid day 257 (DA:Re7.1.IIa, DA:Re8.1.IIa); respond day 258. End: day 278 showing (DA:Cr3.1.IIa), day
  279 kept pieces (DA:Re7.1.IIb, DA:Re9.1.IIa, DA:Cr3.1.IIb); response time day 280.
- **Processes:** creating 251 to 254, 259 to 262, 271, 275 to 278, 282; performing 254, 276 to 278; responding 243 to
  250, 255 to 257, 263 to 274, 279; connecting 243 (the 1913 audience), 246, 247, 268, 269.
- **Sensitivity:** the Rite stages an invented sacrificial rite: watched and read only, no role play (days 243 and
  245); the unit may be left out.
- **Candidate:** a fourth dance from the Americas: **dropped**. Four works already carry 40 days, and Level 2 has the
  Americas in units 7, 8 and 10.

### Unit 10. Light, motion and the whole concert

- **Days:** 283 to 318 (level days 123 to 158, weeks 25 to 32). 36 days, five owned ids.
- **Arc:** Fuller's serpentine dance and her designs linked to physics (DA:Cn10.1.IIa), Nikolais linked to visual art,
  styles and eras linked to their people's views (DA:Cn11.1.IIa), the mid-unit assessment; topic research and movement
  problems (DA:Cn10.1.IIb), leadership, projection and one's own process (DA:Pr6.1.IIa), the whole concert from a
  production plan (DA:Pr6.1.IIb), the critique (day 302), the revision (day 303), the technical, full and dress runs,
  the concert and the process record.
- **Retrieval:** day 284: Level 1's production plan, etiquette and research notes, and unit 7's rehearsal plans, used
  earlier this level (`retrieves` da-g9-stage; da-g9-connect; da-g10-technique).
- **Assessments:** mid day 290 (DA:Cn10.1.IIa, DA:Cn11.1.IIa); respond day 291. End: day 312 dress rehearsal
  (DA:Pr6.1.IIa), day 313 the concert (week 31; DA:Cn10.1.IIb, DA:Pr6.1.IIb), day 314 the process record; response
  time day 315.
- **Processes:** creating 292 to 295, 303; performing 296 to 314; responding 283, 285, 302, 317; connecting 283 to 290,
  292, 301, 317.
- **Candidate:** a dance-and-science link from outside the United States and Europe: **dropped**. Fuller and Nikolais
  carry DA:Cn10.1.IIa; the unit plan may add one only if its rights line holds.
- **Fuller's film:** several early serpentine films show imitators, not Fuller herself. The unit plan confirms on the
  archive's record who dances, and day 283 calls it "her design" where the dancer is another.

## Level 3 (Advanced at honors depth, the 21 `.III` ids): course days 321 to 480

Units 11 to 15, with the mid-year check on days 401 and 402 (level days 81 and 82) and the year-end check on days 479
and 480 (level days 159 and 160).

### Unit 11. The Advanced dancer (review and placement)

- **Days:** 321 to 326 (level days 1 to 6, weeks 1 to 2).
- **Arc and readiness:** as unit 6 at Level 2 depth. Day 325's review showing is the readiness check and placement for
  a student returning after a gap or new to the school, scored against the Level 2 year-end check and unit 10's guide
  (`assess` = `end`, no Level 3 id scored); students from Level 2 the year before get day 2 retrieval in each unit.
- **Processes:** creating 323; performing 324, 325; responding 322, 325; connecting 323 (growth since Level 1).
- **Candidate:** unit 6's self-check form at Level 2 depth: **kept**, no day cost.

### Unit 12. Body, mind and the audience

- **Days:** 327 to 366 (level days 7 to 46, weeks 2 to 10). 40 days, six owned ids.
- **Arc:** the fullest range of space toward an audience (DA:Pr4.1.IIIa), layered rhythms and complex phrasing
  (DA:Pr4.1.IIIb), a passage, body-mind principles (DA:Pr5.1.IIIa) and safe-practice research begun (DA:Pr5.1.IIIb),
  the mid-unit showing; dynamics across a broad range (DA:Pr4.1.IIIc), the piece and a contrasting phrase, the
  self-evaluation, leading a rehearsal (DA:Pr5.1.IIIc), the critique (day 355), the revision (day 356), the end
  showing, the led rehearsals and the kept pieces.
- **Retrieval:** day 328: Level 2's ground and aerial work, transitions and rehearsal plans (`retrieves`
  da-g10-elements; da-g10-technique).
- **Assessments:** mid day 342 (DA:Pr4.1.IIIa, DA:Pr4.1.IIIb); respond day 343. End: day 361 showing (DA:Pr4.1.IIIc,
  DA:Pr5.1.IIIa), day 362 led rehearsals (DA:Pr5.1.IIIc), day 363 kept pieces (DA:Pr5.1.IIIa self-evaluation,
  DA:Pr5.1.IIIb); response time day 364.
- **Processes:** creating 335, 347; performing 328 to 342, 344 to 363; responding 327, 331, 355, 358; connecting 327,
  331 (the two works' settings), 340 (safe practice in one's own life).
- **Candidate:** a European or Latin American work with layered rhythm: **dropped**. Europe comes in unit 13 (Bausch),
  and two works carry the six ids; Latin America is in Level 2.

### Unit 13. A voice of one's own

- **Days:** 367 to 400 (level days 47 to 80, weeks 10 to 16). 34 days, four owned ids.
- **Arc:** risk toward a personal voice (DA:Cr1.1.IIIa) on Café Müller, habits broken (DA:Cr1.1.IIIb), the study and
  log, the mid-unit assessment; Masilo's Swan Lake and a viewpoint (DA:Cr2.1.IIIb), choreographing fluently in a
  personal voice (DA:Cr2.1.IIIa), the comparison of where risk and viewpoint showed (day 385) before the statement is
  drafted, the critique (day 389), the revision (day 390), the statement revised, two rehearsals with the statement
  (days 392 and 393) and the end showing and statement. After the respond day only the portfolio choice (day 398),
  unit 14's setup (day 399) and the mid-year check's setup (day 400) remain.
- **Retrieval:** day 368: Level 2's blending, composition and aesthetic statement (`retrieves` da-g10-ideas;
  da-g10-form).
- **Assessments:** mid day 377 (DA:Cr1.1.IIIa, DA:Cr1.1.IIIb); respond day 378. End: day 395 showing (DA:Cr2.1.IIIa),
  day 396 statement (DA:Cr2.1.IIIb); response time day 397.
- **Processes:** creating 368 to 377, 382 to 396, 399; performing 373, 376, 388, 392 to 395; responding 367, 379, 385,
  389; connecting 379, 384 (the viewpoint statement), 385.
- **Candidate:** a living choreographer from Asia or the Pacific with a personal voice: **dropped**. Level 3 already has
  Lin Hwai-min (unit 12) and Lemi Ponifasio (unit 14).

### Unit 14. Beauty, belief and taste

- **Days:** 403 to 442 (level days 83 to 122, weeks 17 to 25). 40 days, six owned ids.
- **Arc:** Creole Giselle, patterns that build structure across genres (DA:Re7.1.IIIa), butoh and Birds with
  Skymirrors interpreted (DA:Re8.1.IIIa), refining unit 13's dance and its criteria (DA:Cr3.1.IIIa), the mid-unit
  sitting; the complete dance notated (DA:Cr3.1.IIIb), beauty ideals and beliefs (DA:Re7.1.IIIb), one's own taste
  defended (DA:Re9.1.IIIa), the talk on whose beauty and belief (day 426), the critique (day 427), the revision (day
  428), a second practice day on each written id (days 429 and 432) before its revision, the dances-in-places lead-in
  (day 434), the end showing, the peer discussion and the kept pieces. After the respond day only the portfolio choice
  with the filed record (day 441) and unit 15's setup (day 442) remain.
- **Retrieval:** day 404: Level 2's criteria, critique with societal values and recording plan, and unit 13's dance and
  its structure, used earlier this level (`retrieves` da-g10-revise; da-g10-respond; da-g11-form); the analysis frame is
  modeled the same day.
- **Assessments:** mid day 416 (DA:Re7.1.IIIa, DA:Re8.1.IIIa); respond day 417. End: day 437 showing and revision record
  (DA:Cr3.1.IIIa), day 438 peer discussion (DA:Re9.1.IIIa spoken), day 439 kept pieces (DA:Re7.1.IIIb, DA:Re9.1.IIIa,
  DA:Cr3.1.IIIb); response time day 440.
- **Processes:** creating 410 to 413, 419, 420, 428, 431, 435 to 437; performing 413, 435 to 437; responding 403 to 409,
  414 to 416, 422 to 427, 429, 430, 432 to 434, 438; connecting 403, 405 (settings and beliefs), 422, 426.
- **Sensitivity:** beauty ideals are studied in the works, never on students' bodies (day 405); Birds with Skymirrors
  is watched, never danced (day 406).
- **Candidate:** a fourth genre from Africa or South Asia: **dropped**. Masilo (unit 13) carries Africa in Level 3, and
  three works already fill the 40 days.

### Unit 15. Two stages and a life in dance

- **Days:** 443 to 478 (level days 123 to 158, weeks 25 to 32). 36 days, five owned ids.
- **Arc:** River and staging for a place, the growth review across the portfolio (DA:Cn10.1.IIIa), Rooms and dances
  across eras (DA:Cn11.1.IIIa), the mid-unit assessment; leading rehearsals and the process portfolio (DA:Pr6.1.IIIa),
  two venues designed (DA:Pr6.1.IIIb), dance careers and the capstone (DA:Cn10.1.IIIb), the critique (day 462), the
  revision (day 463), rehearsals and technical runs in both venues, the led rehearsal, the two concerts and the record.
- **Retrieval:** day 444: Level 2's production plan, concert roles and research notes, and unit 12's led rehearsals,
  used earlier this level (`retrieves` da-g10-stage; da-g10-connect; da-g11-technique).
- **Assessments:** mid day 450 (DA:Cn10.1.IIIa, DA:Cn11.1.IIIa); respond day 451. End over four days: day 470 a led
  rehearsal (DA:Pr6.1.IIIa), days 471 and 472 the two concerts (week 31; DA:Pr6.1.IIIb), day 473 the process portfolio,
  venue designs and career capstone (DA:Pr6.1.IIIa, DA:Pr6.1.IIIb, DA:Cn10.1.IIIb); response time day 474.
- **Processes:** creating 455, 460, 461, 463; performing 443, 452 to 455, 459 to 473; responding 443, 446, 462, 476;
  connecting 444 to 450, 456 to 458, 476, 478.
- **Candidate:** a site dance from Africa or Asia: **dropped**. River (Eiko and Koma, born in Japan) is the unit's site
  dance, and two works carry the five ids.

## Level 4 (Advanced, deepened; no owned id, 11 `.III` ids reassessed): course days 481 to 640

Units 16 to 19, one sustained project. Level 4 owns no id; its days list the Level 3 ids they reassess, on the Level 3
guide with a higher bar. Checkpoint 1 is days 551 and 552 (level days 71 and 72, week 15) and checkpoint 2 days 617 and
618 (level days 137 and 138, week 28), so a senior who leaves early has finished both.

### Unit 16. The proposal and the series

- **Days:** 481 to 550 (level days 1 to 70, weeks 1 to 14). 70 days, the studio phase.
- **Arc:** The Statement as the starting work, the proposal and its works chosen with their settings, the proposal
  checkpoint; dance one built in studio days, its critique (day 507), revision (day 508) and showing; dance two built,
  dance three (or a deeper dance two) built, the defended series statement and the revision record, and the last
  rehearsal days.
- **Retrieval:** day 482: Level 3's risk-taking, viewpoint statement and revision record (`retrieves` da-g11-ideas;
  da-g11-form; da-g11-revise); for a returning student the same block is the readiness check on the Level 3 guide.
- **Assessments:** mid checkpoints day 490 (the proposal approved after written feedback) and day 510 (the first dance
  shown, unit day 30: the frame says "about day 40"; it comes earlier so dance two and three keep their studio days);
  respond days 491 and 511. Day 550 collects the kept pieces (`assess` = `end`), and checkpoint 1 on day 551 scores them
  once with the series showing, the frame's single end-of-unit assessment (For the lead 1).
- **Processes:** creating 481 to 550; performing 506, 509, 510, 537, 546 to 550; responding 481, 483, 507; connecting
  483 (each work's setting).
- **Candidate:** a fourth checkpoint day for a three-dance series: **kept**, as day 538 inside the unit, an
  Application day (a studio showing to the teacher and panel group, feedback only, nothing scored; a studio day for the
  others).

### Unit 17. The critic's year

- **Days:** 553 to 576 (level days 73 to 96, weeks 15 to 20). 24 days.
- **Arc:** Dido and Aeneas, the critique frame and evidence log, Hibiki, the first critique in three parts, the
  checkpoint; the third genre, the self-critique of the series, the practice panel (day 569) and its revision, a
  rehearsal from the self-critique whose remade section is shown to the student's panel group (day 571, describe only,
  unscored), the peer panel and the scored critique set.
- **Retrieval:** day 554: Level 3's critique and taste defense, and the student's unit 16 series (`retrieves`
  da-g11-respond; da-g12-studio); the baseline look at the main look-for begins the same day.
- **Assessments:** mid checkpoint day 562 (the first critique, written feedback); respond day 563. End: day 572 peer
  panel (DA:Re9.1.IIIa spoken), day 573 critique set (DA:Re7.1.IIIa, DA:Re8.1.IIIa, DA:Re9.1.IIIa); response time day
  574.
- **Processes:** creating 571; performing 571 (the remade section shown to the panel group); responding 553 to 573;
  connecting 553 (Dido and Aeneas's setting), 555.
- **Candidate:** a fourth genre from Africa or the Americas: **dropped**. The critique set is three genres, and the
  third may be the student's own choice.

### Unit 18. Leading the showing

- **Days:** 577 to 616 (level days 97 to 136, weeks 20 to 28). 40 days.
- **Arc:** Café Müller revisited for a found space, leading a cast, the rehearsal plan and call sheet, the full spatial
  range and body-mind principles on one's own series, seven led rehearsals, the checkpoint; six more led rehearsals,
  the critique (day 607), the revision (day 608), the technical, full and dress runs, two showing evenings and the
  kept pieces.
- **Retrieval:** day 578: Level 3's projection strategies, led rehearsal and venue design, and the unit 16 series (`retrieves`
  da-g11-elements; da-g11-technique; da-g11-stage; da-g12-studio).
- **Assessments:** mid checkpoint day 596 (the rehearsal plan and a led rehearsal); respond day 597. End: days 613 and
  614 the series showings (week 27; DA:Pr4.1.IIIa, DA:Pr5.1.IIIa), day 615 the rehearsal record and production
  (DA:Pr6.1.IIIa); response time day 616.
- **Processes:** creating 579, 608; performing 577 to 615; responding 577, 607; connecting 577 (Café Müller's setting).
- **Candidate:** a cast-care card on giving notes: **kept**, used on every led rehearsal day (named on day 578), no day
  added.

### Unit 19. The capstone

- **Days:** 619 to 640 (level days 139 to 160, weeks 28 to 32). 22 days.
- **Arc:** an era and a community's view chosen, research notes, growth traced, the written link to context, the talk
  card, an answer phrase made for the talk, the checkpoint; the talk drafted, practiced, critiqued (day 632), revised
  (day 633), rehearsed and given.
- **Retrieval:** day 620: Level 3's growth review and career capstone, and the unit 16 series (`retrieves`
  da-g11-connect; da-g12-studio); the baseline look at the main look-for begins the same day.
- **Assessments:** mid checkpoint day 628 (the written link, given written feedback); respond day 629. End: days 636 and
  637 the capstone talks and the written links (week 32; DA:Cn10.1.IIIa, DA:Cn11.1.IIIa); response time day 638. A
  senior leaving early gives the talk in week 30, with days 634 and 635 folded into one.
- **Processes:** creating 626 (the answer phrase); performing 634 to 637 (every talk includes the day 626 answer
  phrase, danced by the student or a cast, or a seated or described version); responding 632; connecting 619 to 637.
- **Candidate:** a recorded-talk version on the family's device: **kept**, no day cost (named on day 625, marked the
  same).

## Course-level checks

| Check | Days (level days) | Week | Samples | Respond |
|---|---|---|---|---|
| Level 1 mid-year | 85 (85) | 17 | Unit 2 only, because unit 3 ended the day before: DA:Pr5.1.Ib, DA:Pr5.1.Ic | 86 (week 18) |
| Level 1 year-end | 159 (159) | 32, finals | Unit 4 (unit 3 carried), because unit 5 ended with its concert: DA:Re7.1.Ia, DA:Re7.1.Ib (one short item on a described dance with its stated setting), DA:Re9.1.Ia, DA:Re8.1.Ia, DA:Cr3.1.Ib | 160 |
| Level 2 mid-year | 241 (81) | 17 | Unit 7 only: DA:Pr5.1.IIb, DA:Pr5.1.IIc | 242 |
| Level 2 year-end | 319 (159) | 32, finals | Unit 9 (unit 8 carried): DA:Re7.1.IIa, DA:Re7.1.IIb (one short item on a described dance with its stated setting), DA:Re8.1.IIa, DA:Re9.1.IIa, DA:Cr3.1.IIb | 320 |
| Level 3 mid-year | 401 (81) | 17 | Unit 12 only: DA:Pr5.1.IIIa, DA:Pr5.1.IIIb | 402 |
| Level 3 year-end | 479 (159) | 32, finals | Unit 14 (unit 13 carried): DA:Re7.1.IIIa, DA:Re7.1.IIIb, DA:Re8.1.IIIa, DA:Re9.1.IIIa | 480 |
| Level 4 checkpoint 1 | 551 (71) | 15 | Unit 16's end: DA:Cr1.1.IIIa, DA:Cr2.1.IIIa, DA:Cr3.1.IIIa | 552, a critique day |
| Level 4 checkpoint 2 | 617 (137) | 28 | Unit 17, because unit 18 ended with its showing: DA:Re7.1.IIIa, DA:Re9.1.IIIa, DA:Re8.1.IIIa | 618, a critique day |

The weeks are the ones CALENDAR.md lists for this course (Levels 1 to 3 weeks 17 and 32, Level 4 weeks 15 and 28), and
`scripts/frame.py calendar` places them there. Grades 9 to 12 have no stagger rule but the finals week (rule 4), so the
course breaks no rule. Each check that follows a unit draws its items from the units before it, as the table says, so
it never repeats the end-of-unit assessment just given; no task form repeats within two weeks, and evidence is
collected once (a showing record is carried, not scored again). A showing is the discipline's own evidence and may
follow a unit showing; what may not repeat inside two weeks is the same item on the same work, so checkpoint 2's written
critique (day 617) after unit 18's showings (days 613 and 614) meets the rule.

**Owned codes no course-level check samples, and why** (sequence-write rule 3):

- **Performed live** (scored at showings and concerts on the guide, which a written sitting cannot sample, and carried
  unscored so the same evidence is not collected twice): Level 1 DA:Pr4.1.Ia, Ib, Ic, DA:Pr5.1.Ia, DA:Pr6.1.Ia, Ib;
  Level 2 DA:Pr4.1.IIa, IIb, IIc, DA:Pr5.1.IIa, DA:Pr6.1.IIa, IIb; Level 3 DA:Pr4.1.IIIa, IIIb, IIIc, DA:Pr5.1.IIIc,
  DA:Pr6.1.IIIa, IIIb.
- **Creating** (scored on the dances, logs and statements made over a unit; a sitting cannot hold a made dance):
  Level 1 DA:Cr1.1.Ia, Ib, DA:Cr2.1.Ia, Ib, DA:Cr3.1.Ia; Level 2 DA:Cr1.1.IIa, IIb, DA:Cr2.1.IIa, IIb, DA:Cr3.1.IIa;
  Level 3 DA:Cr1.1.IIIa, IIIb, DA:Cr2.1.IIIa, IIIb, DA:Cr3.1.IIIa, IIIb.
- **The production unit's connecting ids** (the unit ends with its concert the day before the year-end sitting, so the
  frame's checks draw from the two units before it): Level 1 DA:Cn10.1.Ia, Ib, DA:Cn11.1.Ia; Level 2 DA:Cn10.1.IIa,
  IIb, DA:Cn11.1.IIa; Level 3 DA:Cn10.1.IIIa, IIIb, DA:Cn11.1.IIIa.
- **Written ids the frame's year-end sitting left out:** none now. Level 1 DA:Re7.1.Ib and Level 2 DA:Re7.1.IIb are
  sampled by one short item on a described dance with its stated setting on days 159 and 319 (no day added); the
  frame's Course-level checks cells get the same words in the structure pass.

## Shorter path

**The 80-day path (Levels 1 to 3).** A school that cannot give dance every day keeps every unit and every id in 80
days a level by folding and merging the days below (frame unit counts: Level 1 6, 18, 16, 19 and 17; Levels 2 and 3
3, 20, 17, 19 and 17, rebalanced in this fix pass so the production units keep their drafts and revisions apart; each
check keeps its check day and respond day: 76 in units and 4 for checks). Fluency days fold into the next day's
warm-up; other days merge with their neighbors. Never merged: a day 2 retrieval block, the unit's critique, the
revision after it, the rehearsal before a showing, any mid-unit or end-of-unit day, any respond day (the review units
6 and 11 alone merge their rehearsal into the review day), except a kept-piece end day, handed in on the showing day
before it. A kept piece's first version and its revision from written feedback never share a merged lesson; at least
one lesson lies between them. The bridge's 6 days are 7.5 percent of 80. Level 4 has no 80-day path (STANDARD.md 3.2).

- Unit 1 (12 to 6): fold 4; merge 1+2; 3+5; 6+7; 8+9+10.
- Unit 2 (38 to 18): fold 17, 20, 27, 34, 37; 48 handed in on 47; merge 15+16+18+19+21; 22+23+24+25; 26+28; 32+33;
  35+36+38; 39+40+41; 44+45.
- Unit 3 (34 to 16): fold 57, 66, 74; 81 on 80; merge 53+54+55; 56+58+59+60+61; 64+65+67; 68+69+70+71; 72+73; 77+78;
  83+84.
- Unit 4 (38 to 19): fold 92, 98, 106, 113; merge 89+90+91; 93+94+95; 96+97+99; 100+101; 104+105+107+108; 109+110;
  111+112; 116+117; 122+123+124.
- Unit 5 (34 to 17): fold 144; 155 on 154; merge 127+128+129; 130+131+132+133; 136+137+138+139; 140+141+142+143;
  147+148; 149+150+151; 157+158.
- Unit 6 (6 to 3): merge 161+162+163+164.
- Unit 7 (40 to 20): fold 171, 174, 178, 187, 196; 203 on 202; merge 169+170; 172+173; 175+176+177; 179+180+181;
  185+186+188; 189+190; 191+192; 193+194+195; 199+200; 205+206.
- Unit 8 (34 to 17): fold 212, 222, 228; 235 on 234; merge 209+210+211+215; 213+214+216; 220+221; 223+224+225;
  226+227; 231+232; 237+238+239+240.
- Unit 9 (40 to 19): fold 248, 254, 261, 267; 279 on 278; merge 245+246+247; 249+250+251; 252+253; 255+256;
  259+260; 262+263+264; 265+266+268+269; 272+273+274; 275+276; 281+282.
- Unit 10 (36 to 17): fold 297, 308; 314 on 313; merge 285+286+287; 288+289; 292+293+294; 295+296+298+299;
  300+301+305; 304+306+307+309+310; 316+317+318.
- Unit 11 (6 to 3): merge 321+322+323+324.
- Unit 12 (40 to 20): fold 330, 334, 339, 345, 354; 363 on 362; merge 329+331; 332+333; 335+336+337; 338+340;
  344+346+347; 348+349+350; 351+352+353; 357+358+359; 365+366.
- Unit 13 (34 to 17): fold 370, 381, 388; 396 on 395; merge 369+371+372; 373+374+375; 379+380; 382+383+384;
  385+386+387; 391+392+393; 398+399+400.
- Unit 14 (40 to 19): fold 407, 413, 421; 439 on 438; merge 405+406; 408+409+410; 411+412+414+415; 418+419+420;
  422+423+424; 425+426; 429+430+431; 432+433+434+435; 441+442.
- Unit 15 (36 to 17): fold 459; 473 on 472; merge 445+446+447; 448+449; 452+453+454+455+456; 457+458+460+461;
  464+465+466+467; 468+469; 475+476+477+478.

No merge now puts a kept piece's draft and its revision in one lesson. The largest merges left are five days of
lighter work (unit 10's 304+306+307+309+310 and unit 15's 452 to 456); a unit plan may swap a pair if it keeps the
protected days whole and the draft and revision apart.

**A year about 10 days short (every level).** Ten named fold-in days a level, each saving one 45-minute lesson (45
minutes; 450 minutes a level), whose drill or studio work moves into the next day's warm-up or studio time. Nothing on
them is assessed and no owned part is cut, so each level runs in 150 days against the frame's 160.

- Level 1: days 4, 17, 20, 27, 57, 66, 74, 92, 98, 106 (all Fluency drills and runs; the concert running order run,
  day 144, never folds).
- Level 2: days 171, 174, 187, 212, 222, 228, 248, 254, 261, 267 (all Fluency; a landing run, day 178, and the
  production unit's drill and running order, days 297 and 308, never fold).
- Level 3: days 330, 334, 339, 354, 370, 381, 388, 407, 413, 421 (all Fluency; the projection drill in each venue,
  day 459, never folds).
- Level 4: days 492, 495, 498, 501 (four dance-one studio days, folded into the studio days beside them), 506, 537,
  559, 586, 605, 631 (Fluency runs and drills).

## Cross-subject

- **Physical education, grade 9:** same year only for a grade 9 student in Level 1. PE's "Dance by design" (its unit
  5, weeks 22 to 26) comes after dance units 2 and 3 (weeks 3 to 17), so days 13 and 67 carry the boundary and the
  dance units assume no PE cue; nothing is taught twice.
- **Health:** the habits lean (day 24) is taught here through the invented dancer; health's semester may fall in
  either half or another grade, so no day waits on it.
- **ELA:** written analysis practices argument with evidence; days 88, 244, 404 and 554 model the claim, evidence and
  reason frame in case ELA has not taught it yet that year.
- **Social studies:** works are taught with who, when, where and for what on the work card itself.

## For the lead

1. **A Level 4 unit whose end-of-unit assessment is a checkpoint.** Settled by the expert read: keep the form (day 550
   collects the kept pieces with `assess` = `end`, day 551 scores them once with the showing). No gate change now.
2. **Short-path counts in the production units.** Taken in the fix pass: Levels 2 and 3 run 3, 20, 17, 19 and 17 on
   the 80-day path; frame.md's short-path bullet and the unit 9, 10, 14 and 15 rows were changed with it.
3. **The rule 2 count cannot read a band course.** `unit_skeleton.py` reads the course grade "9-12" as no number, so
   the gate's rule 2 check prints nothing for this course. Here every owning unit retrieves its earlier-level rows on
   day 2 (`retrieves` filled), as the frame and rule 2 ask by level. Pick: the skeleton reads a band course's level
   from the Year column (Level n as grade 8 + n), as frame.py already does for the calendar.
4. **Two written ids no year-end check sampled.** Taken in the fix pass: days 159 and 319 carry one short item on a
   described dance with its stated setting (DA:Re7.1.Ib, DA:Re7.1.IIb); the frame's Course-level checks cells for the
   Level 1 and Level 2 year-end checks need the same words (structure pass).
5. **"None" read as a code.** `sequence.py` prints "standard None is on no day" for units 1, 6, 11 and 16 to 19, whose
   Owned standards cell is "None". Pick: sequence.py skips "None" as frame.py does (frame For the lead 1 is the same
   question for the Skills cell).
6. **A mixed-room calendar.** The room follows Level 1's calendar (see "More than one level in one room"); a full
   mixed-room calendar, day by day, is a course page item.
7. **CALENDAR.md's cut labels.** docs/courses/CALENDAR.md's four 9 to 12 dance rows print truncated labels ("Level 1
   mid-year (week 1 week 17"); the generated label column needs fixing (not this scope).

Unsure: the short-path merge lists come from a fixed rule (fold Fluency, hand in kept pieces on the showing day, merge
the smallest neighbors); a unit plan may swap a merge for a better pair if it keeps the protected days whole.
