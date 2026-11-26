# Scope and sequence: Theater, grades 3 to 5

Course `theater-grades-3-to-5`, grades 3 to 5 as three years in one file, draft, written 2026-11-26 from the frame (docs/courses/theater-grades-3-to-5/frame.md), with the expert read's fix pass of 2026-11-26 applied (docs/reviews/sequence-theater-grades-3-to-5-fixes-2026-11-26.md). The days live in data/plans/theater-grades-3-to-5/days.csv.

## The band on one page

- **Which grade's standards fall in which year.** Year 3 (course days 1 to 64) claims only the 24 grade 3 theater
  ids (`.3a`, `.3b`, `.3c`); year 4 (days 65 to 128) only the 24 grade 4 ids; year 5 (days 129 to 192) only the 24
  grade 5 ids: 72 in all, the count in docs/courses/arts/STANDARD.md 3.2. Every id is taught and assessed in its own
  year, each named with its line in data/standards/ncas-performance-standards-words.txt, never quoted. A year brings
  back the year before's techniques as practice, never as a claim.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a student's record shows which grade's standards they met. Where a student
  meets year 5 before year 4, each unit's day 2 retrieval task carries its ten-minute reteach of the earlier technique.
- **Units and days.** 12 units, 192 course days, 64 a year: 60 in four units, 2 course-level check days and 2 respond
  days. `stretch` is the unit number of the frame's Units table (C on a course-level day); `unit` is `<unit>.1` (no
  unit is split into sections at this stage).
- **How school_day is counted.** The course meets two 40-minute sessions a week for 32 weeks a year, 96 weeks over
  the band, 160 school days a year. school_day counts on across the whole band, as frame.py reads it: course day n
  sits on school day ceil(2.5 n), the even spread, so it falls in year 3 + (school_day - 1) // 160 and in band week
  (school_day - 1) // 5 + 1 (1 to 96); its week of the year is ((school_day - 1) mod 160) // 5 + 1, which is also
  ceil(k / 2), where k is the day's place in its year (k = n - 64 for year 4, n - 128 for year 5). Year 3 runs
  school days 3 to 160, year 4 163 to 320 and year 5 323 to 480. This formula is the scope's own and is not
  re-counted to match calendar.csv; every unit and check sits in the frame's weeks by it. A school picks its own two
  days; the week is what CALENDAR.md reads.
- **The four processes.** Each year carries all four artistic processes (create; perform; respond; connect), and
  each unit touches at least the processes its frame row names, through its owned ids. A unit need not claim all
  four: where a unit practices a process it owns no id for (the connecting step named on a study day of units 1, 2,
  5, 6, 9 and 10), the day says "practiced, no id claimed", and no id outside the unit's owned rows is ever claimed.
  The unit sections below name the days. Each unit runs technique days before the making that needs them, a
  rehearsal day with the unit's one critique (describe, ask, suggest: led by the teacher in units 1 to 4, run by the
  students with the critique-protocol card from unit 5), a revision day, then the two end-of-unit check days (a
  showing day and a written day), then a respond day. Units 4, 8 and 12 end with a family showing.
- **Assessment pattern.** No unit is over 25 days, so none holds a mid-unit assessment. Each unit's end-of-unit
  assessment is its two check days, marked against the frame's id-by-id evidence line: guide look-fors marked live
  on the showing day, kept cards made on the last rehearsal day and collected on the written day, and at most two
  written items a student on the unseen Curio Class scene the teacher performs. Response time is the respond day
  after the two check days, counted once. Each unit takes a baseline look at its main look-for on its first practice
  day (named in the note), so every student has two marks a unit. One portfolio piece a unit, with a one-line
  reflection, is filed on the written day.
- **Readiness and retrieval.** Every row the band assumes is one grade back: year 3 assumes the grade 2 rows of
  Theater, grades K to 2 (th-g3-judge assumes th-g2-notice), years 4 and 5 assume the year before. So no readiness
  check is given anywhere in the band. Every unit opens with a retrieval task inside day 2's opener (10 minutes, with
  its reteach) on the rows in the `retrieves` column; day 1 of every unit stays clean for the hook and the compelling
  question.
- **Equipment and safe use.** The supplies columns are math and science only, so each day's note names its
  equipment, safe use of the floor and the free path where the frame lists one: a clear floor with room for arms out;
  blunt scissors, tape not pins, costume pieces loose and quick to remove; LED flashlights with screw-closed battery
  doors, never shone into eyes, no flashing, the room dimmed but never dark; signs on a loose yarn loop, never round
  the neck; voice below shouting with a rest after siren and pitch work. Safety rules are "from memory" until each
  unit's fresh safety read checks them.
- **Sensitivity.** Each day that studies a flagged tradition or touches the student's own life names it in the note:
  commedia types (unit 1), kyogen (2), Holder's Wiz designs and Roadside Theater's community plays (3), the griots and
  the Sosso-Bala (4), wayang kulit (5), Chaplin and Deaf West Theatre (6), tholu bommalata and FastHorse's Peter Pan
  (7), the meddah, Mhlophe and the Dionysus festival (8), the Tin Soldier's ending (9), pansori (10), the grape
  strike and Laedza Batanani (11), the Zuni Poor Turkey Girl and the Cinderella stepfamily (12). Every tie to a
  student's own life or community offers an invented or public option marked the same, and carries health's steps
  for "If a student tells you something". The experience items of TH:Re8.1.3a, TH:Re8.1.4a and TH:Re8.1.5a are the
  one exception: the standard asks for the student's own experiences, so at least one comes from this year's theater
  class (a class scene, a partner showing), which every student has, and an invented or outside-school one may be the
  second. TH:Re8.1.5b keeps its invented-viewer option as a deliberate sensitivity trade.

## Year 3 (grade 3 ids, course days 1 to 64)

### Unit 1. Characters out of nothing

Days 1 to 16, weeks 1 to 8 of year 3. *How do actors invent a whole scene with no script, and how does a group make it better?*

Arc: commedia's printed outlines as the hook, then the freeze and three idea methods (what-if, Spolin's "Where",
the passed object), the scenario-to-scene steps, then working inside a time and space limit with the rehearsal log,
then rehearsal, the teacher-led critique, revision and the showing. Order: the freeze and the room's routines come
before any group improvises; the idea methods come before the choosing and comparing of ideas; the limit comes before
the rehearsal it governs.

- Processes: create on days 3 to 8 and 12; perform on days 4, 6, 10, 13 and 14 (showing 14); respond to another
  artist's work on day 1 (commedia, Scala) and day 3 (Spolin), and as critic on day 11; connect, practiced with no
  id claimed, on day 1 (what the 1611 players and the class both do with an outline).
- Readiness: none. Retrieval on day 2 (th-g2-imagine, th-g2-show). Baseline look on day 4.
- End-of-unit assessment: day 14 (showing; TH:Cr1.1.3a, TH:Cr1.1.3c, TH:Cr3.1.3a) and day 15 (written: TH:Cr2.1.3b;
  kept rehearsal-log page TH:Pr6.1.3a and idea sheet TH:Cr2.1.3a). Respond day 16.
- Candidate (a further tradition's form): dropped. Africa is met in unit 4 and the unit already studies two works.
- Once-a-week path, 8 sessions: 1 (days 1, 2), 2 (3, 4, 5), 3 (6, 7), 4 (8, 9, 10), 5 (11, 12, 13: critique,
  revision, last run), 6 showing (14), 7 written (15), 8 respond (16). Fluency days 4 and 10 fold into their
  session's opener.

### Unit 2. The actor's tools

Days 17 to 32, weeks 9 to 16 of year 3. *How do actors use body, voice and mind to make a character, and why did they choose what they did?*

Arc: kyogen's set walk and voice as the hook, then the three exercise sets (body, voice, thinking), Bill Irwin and the
character map, exploring body and voice unscripted then scripted, connecting with a character's feeling and with
one's own experiences of drama, then rehearsal, critique, revision and the showing. Order: the exercise sets come
before any character is built; the unscripted beat comes before the two-line script; the response card frame is
taught before the written day uses it.

- Processes: create on days 22, 23 and 26 to 29; perform on days 20, 25, 26 and 30 (showing 30); respond on days 17
  (kyogen), 21 (Irwin), 24 and 25 (audience card, and the student's own experiences of drama, at least one from this
  year's class), and as critic on day 27; connect, practiced with no id claimed, on day 17 (where kyogen sits on a
  day of noh and why families hand it down).
- Readiness: none. Retrieval on day 18 (th-g2-actor, th-g2-notice). Baseline look on day 20.
- End-of-unit assessment: day 30 (showing; TH:Pr5.1.3a, TH:Cr3.1.3b; kept audience-journal card TH:Re7.1.3a) and
  day 31 (written: TH:Re8.1.3c, TH:Re8.1.3a; kept character map TH:Pr4.1.3b). Respond day 32.
- Bridge: grade 3 ELA teaches opinion writing in its unit 3 (weeks 17 to 24), after this unit, so day 24 teaches the
  response card frame and the written day sets at most two written items.
- Candidate (a tradition's own teaching of actor training): dropped. No tradition's own teaching was named or checked
  for it, and kyogen is already studied from its own cultural body's page.
- Once-a-week path, 8 sessions: 1 (days 17, 18, 19), 2 (20, 21), 3 (22, 23, 24, 25), 4 (26, 27), 5 (28, 29), 6
  showing (30), 7 written (31), 8 respond (32). Fluency days 20 and 25 fold into openers.

### Unit 3. Dressing the story

Days 35 to 52, weeks 18 to 26 of year 3. *How do costumes, props and sets fit a story's world, and how does a drama show the people who make it?*

Arc: the tech elements named, then design sketches for a retold Oz scene, Geoffrey Holder's designs for The Wiz,
the making steps, Roadside Theater and the two-ties card, a community scene, then rehearsal with costume and set,
critique, revision with the tech comparison, and the showing for a partner class. The longest year 3 unit: seven ids
and two products. Order: sketching comes before making; the design study comes before the comparison it feeds; the
community study comes before the community scene.

- Processes: create on days 38 to 40, 44, 46 and 48; perform on days 43, 45 and 49 to 50 (showing 50); respond on
  days 37 (Holder's Wiz) and 41 (Roadside Theater), and as critic on day 47; connect on days 41, 42 and 44 (community
  life, a social problem and another subject on the two-ties card).
- Readiness: none. Retrieval on day 36 (th-g2-design, th-g2-world). Baseline look on day 38.
- End-of-unit assessment: day 50 (showing; TH:Cn10.1.3a, TH:Cr3.1.3c) and day 51 (written: TH:Pr5.1.3b,
  TH:Re9.1.3b; kept prop-sketch TH:Cr1.1.3b with its character box TH:Re8.1.3b, kept two-ties card TH:Cn11.1.3a).
  Respond day 52.
- Candidate (an Asian design tradition): dropped. Asia is already in the year (kyogen, unit 2) and the unit carries
  the year's heaviest load.
- Once-a-week path, 9 sessions, weeks 17 to 25 (the year drops its mid-year check on this path): 1 (days 35, 36,
  37), 2 (38, 39: the making steps), 3 (40, 41, 42), 4 (43, 44, 45), 5 (46, 47: making finished, then the critique),
  6 (48, 49: the revision, then the last run with the kept sheets), 7 showing (50), 8 written (51), 9 respond (52).
  Fluency days 38 and 43 fold into openers. No session holds more than three days.

### Unit 4. From page to stage

Days 55 to 64, weeks 28 to 32 of year 3. *How does a written story become a play, and how does an audience decide what it thinks?*

Arc: The Bremen Town Musicians in Curio Class's retelling, the parts of dramatic structure on the story map, past
artists' other tellings (the Grimms' book, Marcks's statue, the griots), the class criteria card for judging, then
one rehearsal day with critique and revision, the showing, the written day, respond and the family showing. Order:
structure comes before rehearsal; the criteria card is made before the audience judges with it.

- Processes: create on days 56 and 60; perform on days 58, 60, 61 and 64 (showing 61, family showing 64); respond on
  days 57 (griots, Marcks) and 59 (the criteria card), and as critic on day 60; connect on days 55 and 57 (how one
  story was retold across times and places).
- Readiness: none. Retrieval on day 56 (th-g2-story, th-g2-notice). Baseline look on day 58.
- End-of-unit assessment: day 61 (showing; TH:Pr4.1.3a) and day 62 (written: TH:Cn11.2.3b, TH:Re9.1.3c; kept story
  map TH:Cn11.2.3a, completed in the last 5 minutes of day 58 and revisable on day 60, and criteria card
  TH:Re9.1.3a, completed on day 60). Day 60 then holds the critique, the revision and the criteria card only. Respond day 63; family showing day 64, not scored.
- Lean: RL.3.3 is taught in ELA grade 3 unit 1 (weeks 1 to 8), so it is used, not retaught.
- Candidate (a griot practitioner's own words): kept, at no day cost: read inside the griot study on day 57 (10
  minutes, credited), with the Sosso-Bala's sacred keeping named plainly.
- Once-a-week path, 5 sessions: 1 study and teaching only (days 55, 56, 57; 28 teaching minutes: hook and the
  adaptation 6, the retrieval with its reteach 10, dramatic structure on the story map 6, past tellings with a short
  griot reading 6), 2 (58, 59, 60; baseline run of the three scenes 8, the criteria card made 7, the critique 7, the
  revision 6), 3 showing (61, given as the family showing, day 64, with an in-class version for any student without
  a family yes), 4 written (62; the story map and criteria card are completed in its 7 spare minutes before
  collection), 5 respond (63). Fluency day 58 runs as session 2's opener.

## Year 4 (grade 4 ids, course days 65 to 128)

### Unit 5. Who, where, when

Days 65 to 80, weeks 1 to 8 of year 4. *How do the given circumstances change every idea, and what jobs does a show need?*

Arc: Stanislavski's given circumstances, the card and an improvised story fitted to it, the circumstances walk, the
hot seat, wayang kulit and the jobs a showing needs, the run-review-rerun cycle and the critique-protocol card, then
rehearsal run by the stage manager, the first student-run critique, revision and the showing. Order: the
circumstances come before the walk that fits them; the jobs are named before a group runs itself; the protocol card
is taught before the students run the critique.

- Processes: create on days 66, 67, 69, 70 and 77; perform on days 68, 72, 74, 75 and 78 (showing 78); respond on days
  65 (Stanislavski) and 71 (wayang kulit), and as critic on day 76; connect, practiced with no id claimed, on day 71
  (the dalang's many jobs set beside the jobs of a school showing).
- Readiness: none. Retrieval on day 66 (th-g3-imagine, th-g3-show). Baseline look on day 68.
- End-of-unit assessment: day 78 (showing; TH:Cr1.1.4c, TH:Pr6.1.4a) and day 79 (written: TH:Cr1.1.4a; kept log
  page TH:Cr3.1.4a, jobs list TH:Cr2.1.4b, hot-seat sheet TH:Cr2.1.4a). Respond day 80.
- Candidate (a Stanislavski exercise from a public domain source): kept, at no day cost: the unit plan checks the
  wording against a public domain English source before day 65 uses it.
- Once-a-week path, 8 sessions: 1 (days 65, 66), 2 (67, 68, 69), 3 (70, 71, 72), 4 (73, 74, 75), 5 (76, 77:
  critique, revision and last rehearsal), 6 showing (78), 7 written (79), 8 respond (80). Fluency days 68 and 74 fold
  into openers.

### Unit 6. Walks and faces

Days 81 to 96, weeks 9 to 16 of year 4. *How does a character's walk tell us who they are, and what do feelings do to the body?*

Arc: Chaplin's Tramp walk, the three-centers walk, ensemble exercises, Deaf West Theatre and look-describe-interpret,
two named techniques on the character map, a wordless pair scene, comparing experiences of drama, then lines added,
critique, revision and the showing. Order: the walk and the exercises come before the character built from them; the
wordless scene comes before the scene with lines.

- Processes: create on days 86, 87, 90 and 92; perform on days 84, 89, 90 and 94 (showing 94); respond on days 81
  (Chaplin) and 85 (Deaf West), on days 88 and 89 (look, describe, interpret; experiences of drama compared with a
  partner), and as critic on day 91; connect, practiced with no id claimed, on day 81 (the Tramp in 1925 and who
  laughed at him).
- Readiness: none. Retrieval on day 82 (th-g3-actor, th-g3-notice). Baseline look on day 84.
- End-of-unit assessment: day 94 (showing; TH:Pr5.1.4a, TH:Pr4.1.4b; kept audience-journal card TH:Re7.1.4a) and
  day 95 (written: TH:Re8.1.4c; kept character map TH:Cr3.1.4b and partner card TH:Re8.1.4a). Respond day 96. The
  audience-journal card has two lines, a choice another group's actor made (watching) and one the student's own pair
  made (joining in), so both parts of TH:Re7.1.4a are asked; each partner card draws at least one experience from
  this year's class.
- Lean and bridge: SL.4.4 is taught in ELA grade 4 unit 1 (weeks 1 to 8) and used on day 86; opinion writing (W.4.1)
  comes in ELA unit 3 from week 17, so day 88 teaches the response card frame.
- Candidate (a further tradition): dropped. The unit already studies two works and the year's range is met.
- Once-a-week path, 8 sessions: 1 (days 81, 82, 83), 2 (84, 85, 86), 3 (87, 88, 89), 4 (90, 91), 5 (92, 93), 6
  showing (94), 7 written (95), 8 respond (96). Fluency days 84 and 89 fold into openers.

### Unit 7. Light, sound and point of view

Days 99 to 114, weeks 18 to 25 of year 4. *How do lights and sound serve a story, and whose view does a play show?*

Arc: Appia's drawings and a flashlight on a face, the light plan, tholu bommalata and sound on cue, Larissa
FastHorse's Peter Pan, characters compared through looks drawn from a source, a local-problem scene with a fact card,
then rehearsal with tech and snags fixed, critique, revision and the showing for a partner class. Order: the light
plan and cues come before rehearsal with tech; the viewpoint study comes before the scene that takes a view.

- Processes: create on days 100, 104, 106 and 108; perform on days 102, 107, 108 and 112 (showing 112); respond on days
  99 (Appia), 101 (tholu bommalata) and 103 (FastHorse), and as critic on day 109; connect on days 103 and 105 (a
  culture's view, a local problem and a fact from another subject).
- Readiness: none. Retrieval on day 100 (th-g3-design, th-g3-world). Baseline look on day 102.
- End-of-unit assessment: day 112 (showing; TH:Cn11.1.4a, TH:Pr5.1.4b) and day 113 (written: TH:Re9.1.4b,
  TH:Cn10.1.4a; kept prop-sketch TH:Cr1.1.4b, log page TH:Cr3.1.4c and character card TH:Re8.1.4b). Respond day 114.
- Candidate (a further tradition): dropped. Three works are already studied and the year's range is met.
- Once-a-week path, 9 sessions, weeks 17 to 25 (the year drops its mid-year check on this path): 1 (days 99, 100),
  2 (101, 102), 3 (103, 104: FastHorse studied with its own time), 4 (105, 106, 107), 5 (108, 109: tech rehearsal,
  then the critique), 6 (110, 111: the revision, then the tech run with the kept sheets), 7 showing (112), 8 written
  (113), 9 respond (114). Fluency days 102 and 107 fold into openers. No session holds more than three days.

### Unit 8. Endings and eras

Days 117 to 128, weeks 27 to 32 of year 4. *How does changing a choice change the ending, and how have people told stories on stage in other times and places?*

Arc: a Nasreddin Hodja tale and the turn of a scene, storytelling in two cultures (the meddah and Gcina Mhlophe),
the theater at Epidaurus on the era chart, an ending rewritten, a way of judging offered, then critique, revision, the
showing with both endings, the written day, respond and the family showing. Two days longer than units 4 and 12: it
compares two cultures and two eras besides rewriting an ending. Order: the turn is marked before it is rewritten;
the two cultures are studied before they are compared.

- Processes: create on days 120 and 124; perform on days 121, 123, 125 and 128 (showing 125, family showing 128);
  respond on days 118 (meddah, Mhlophe) and 122 (judging), and as critic on day 123; connect on days 118 and 119
  (two cultures and two eras).
- Readiness: none. Retrieval on day 118 (th-g3-story, th-g3-judge). Baseline look on day 121.
- End-of-unit assessment: day 125 (showing; TH:Pr4.1.4a; kept audience-journal card TH:Re9.1.4c) and day 126
  (written: TH:Cn11.2.4a; kept era chart TH:Cn11.2.4b and criteria card TH:Re9.1.4a). Respond day 127; family
  showing day 128, not scored.
- Candidate (a further tradition): dropped. Three traditions are already studied in a 12-day unit.
- Once-a-week path, 5 sessions: 1 study and teaching only (days 117, 118, 119; 28 teaching minutes: the hook and
  the turn 8, the retrieval with its reteach 10, the two storytellers 5, Epidaurus on the era chart 5), 2 (120 to
  124; the ending rewritten 6, the baseline run of both endings 5 as the opener, a way of judging offered 5, the
  critique 7, the revision 5), 3 showing (125, given as the family showing, day 128, with an in-class version for
  any student without a family yes), 4 written (126; the era chart and criteria card are completed in its 7 spare
  minutes before collection), 5 respond (127). Fluency day 121 runs as session 2's opener. Session 2 is the year's
  one five-day merge: the story unit cannot gain a session (weeks 28 to 32 are fixed by the year-end check), so its
  minute line is named here for the unit plan to test.

## Year 5 (grade 5 ids, course days 129 to 192)

### Unit 9. Inside the character

Days 129 to 144, weeks 1 to 8 of year 5. *How does what a character thinks inside change what they do, and how does each of us own a part of the show?*

Arc: Andersen's Steadfast Tin Soldier and physical traits, the inner-thought line, Bottom's waking speech, an
original scene shaped from the group's questions, set jobs and a relaxed sharing, the self-review run, then
rehearsal with jobs, critique, revision and the showing for a partner class. Order: traits and inner thought come
before the scene they shape; the self-review is taught before the revision that uses it.

- Processes: create on days 132 to 134 and 139 to 141; perform on days 132, 137, 138 and 142 (showing 142); respond on
  days 129 (Andersen) and 131 (Shakespeare), and as critic on day 139; connect, practiced with no id claimed, on day
  129 (an 1838 toy and a toy of today).
- Readiness: none. Retrieval on day 130 (th-g4-imagine, th-g4-show). Baseline look on day 132.
- End-of-unit assessment: day 142 (showing; TH:Cr1.1.5a, TH:Cr2.1.5b, TH:Pr6.1.5a) and day 143 (written:
  TH:Cr1.1.5c; kept question sheet TH:Cr2.1.5a and log page TH:Cr3.1.5a). Respond day 144.
- Candidate (a further continent): dropped. Year 5 already spans four continents and the unit carries six ids.
- Once-a-week path, 8 sessions: 1 (days 129, 130, 131), 2 (132, 133, 134), 3 (135, 136, 137), 4 (138, 139), 5 (140,
  141), 6 showing (142), 7 written (143), 8 respond (144). Fluency days 132 and 137 fold into openers.

### Unit 10. Breath, stance and meaning

Days 145 to 162, weeks 9 to 17 of year 5. *How does the body carry meaning, and how do we back up what we think of a performance?*

Arc: Mummenschanz and the gesture with a meaning, pansori and breath and pitch, warm-ups that fit the piece, body
and voice for a character, a wordless scene, a reaction explained and defended, then lines added, critique, revision,
written and defended reactions, and the showing. The longest year 5 unit: responses are written and defended for
the first time. Order: gesture and breath come before the scene built from them; a reaction is explained before it
is defended.

- Processes: create on days 150, 151, 155 and 157; perform on days 148, 154, 155 and 160 (showing 160); respond on days
  145 (Mummenschanz) and 147 (pansori), on days 152 to 154 and 158 (reactions explained and defended, with at least
  one experience from this year's class), and as critic on day 156; connect, practiced with no id claimed, on day 147
  (where pansori was sung and for whom).
- Readiness: none. Retrieval on day 146 (th-g4-actor, th-g4-notice). Baseline look on day 148.
- End-of-unit assessment: day 160 (showing; TH:Pr4.1.5b, TH:Cr3.1.5b; kept four-field audience-journal card
  TH:Re8.1.5c) and day 161 (written: TH:Re7.1.5a, TH:Re8.1.5a; kept warm-up card TH:Pr5.1.5a). Respond day 162.
- Bridge: opinion writing (W.5.1) comes in ELA grade 5 unit 3 (weeks 17 to 25), after this unit, so day 152 teaches
  the response card frame and the written day sets at most two written items.
- Candidate (a further tradition): dropped. Two works already studied, the range is met.
- Once-a-week path, 9 sessions: 1 (days 145, 146), 2 (147, 148, 149), 3 (150, 151), 4 (152, 153, 154), 5 (155, 156,
  157), 6 (158, 159), 7 showing (160), 8 written (161), 9 respond (162). Fluency days 148 and 154 fold into openers.

### Unit 11. Theater for a cause

Days 165 to 180, weeks 19 to 26 of year 5. *How do people make theater about the problems they face, and how can light and sound carry a play's theme?*

Arc: El Teatro Campesino's signs and truck-bed plays, design ideas for given circumstances, the cue sheet, Laedza
Batanani's village plays, a problem investigated on the fact card, cultural views and a viewer's response, then a
scene on a problem built with its cues, rehearsal with tech and fixes, critique, revision and the showing for a
partner class. Order: the cue sheet comes before rehearsal with cues; the investigation comes before the scene it
voices.

- Processes: create on days 166, 172, 174 and 176; perform on days 168, 173, 174 and 178 (showing 178); respond on
  days 165 (El Teatro Campesino), 169 (Laedza Batanani) and 171 (a viewer's response), and as critic on day 175;
  connect on days 169 and 170 (a person tied to a community; a past, worldwide or social problem).
- Readiness: none. Retrieval on day 166 (th-g4-design, th-g4-world). Baseline look on day 168.
- End-of-unit assessment: day 178 (showing; TH:Pr5.1.5b, TH:Cn11.1.5a) and day 179 (written: TH:Re9.1.5b,
  TH:Re8.1.5b; kept investigation sheet TH:Cn11.1.5a, prop-sketch TH:Cr1.1.5b, log page TH:Cr3.1.5c and two-ties card
  TH:Cn10.1.5a). Respond day 180.
- Candidate (a further tradition): dropped. Two traditions already studied, the range is met.
- Once-a-week path, 8 sessions, weeks 18 to 25 (the year drops its mid-year check on this path): 1 (days 165, 166),
  2 (167, 168, 169: the cue sheet with its drill, then Laedza Batanani), 3 (170, 171: the investigation, then
  cultural views, the only teaching of TH:Re8.1.5b), 4 (172, 173, 174: the scene built, the cue run as the opener,
  rehearsal with tech; the prop-sketch and investigation sheet completed in the last 5 minutes), 5 (175, 176, 177:
  the critique 10, the revision 8, the last run 6, the log page and two-ties card 4), 6 showing (178), 7 written
  (179), 8 respond (180). Fluency days 168 and 173 fold into openers.

### Unit 12. Same story, new eyes

Days 183 to 192, weeks 28 to 32 of year 5. *How do different cultures tell the same story, and how do we judge a play fairly?*

Arc: three Cinderella tellings compared (Ye Xian, Perrault's Cendrillon, the Zuni Poor Turkey Girl read only), the
hidden-thought line, the First Folio's stage directions as a source for terms and customs, a class judging guide,
then one rehearsal day with critique and revision, the showing, the written day, respond and the family showing that
closes the band. Order: the comparison comes before the choice of telling; the stage terms come before the script
pages that use them.

- Processes: create on days 184, 185 and 188; perform on days 186, 188, 189 and 192 (showing 189, family showing
  192); respond on days 183 (three tellings), 185 (the First Folio) and 187 (the judging guide), and as critic on day
  188; connect on days 183 and 185 (one story across cultures; an old source for today's stage customs).
- Readiness: none. Retrieval on day 184 (th-g4-story, th-g4-judge). Baseline look on day 186.
- End-of-unit assessment: day 189 (showing; TH:Pr4.1.5a; kept judging guide TH:Re9.1.5a) and day 190 (written:
  TH:Cn11.2.5a, TH:Re9.1.5c; kept script page TH:Cn11.2.5b and annotation TH:Pr4.1.5a, the annotation completed in
  the last 5 minutes of day 186 and revisable on day 188). Day 188 then holds the critique, the revision and the
  script page only. Respond day 191; family showing day 192, not scored.
- Lean: RL.5.3 is taught in ELA grade 5 unit 1 (weeks 1 to 9) and used on day 183's comparison chart.
- Candidate (a fourth telling): kept as the swap pool only, at no day cost. If the Zuni check fails, the unit plan
  swaps in another culture's telling with the same ids.
- Once-a-week path, 5 sessions: 1 study and teaching only (days 183, 184, 185; 28 teaching minutes: the hook and
  three tellings 8, the retrieval with its reteach 10, the hidden-thought line 5, the First Folio 5), 2 (186, 187,
  188; baseline run 8, the judging guide 7, the critique 7, the revision 6), 3 showing (189, given as the family
  showing, day 192, with an in-class version for any student without a family yes), 4 written (190; the script
  annotation and script page are completed in its 7 spare minutes before collection), 5 respond (191). Fluency day
  186 runs as session 2's opener.

## Course-level checks

Each check is one check day and one respond day, on the frame's weeks and CALENDAR.md's weeks for this course, all
off the core check weeks for the grade. Arts are specials in K to 5 and do not count against the classroom teacher's
stagger (CALENDAR.md rule 1). `frame.py calendar` reads the same weeks from days.csv.

| Check | Course days | Week | What it samples |
|---|---|---|---|
| Year 3 mid-year | 33, respond 34 | 17 | Unit 1: TH:Cr1.1.3a (characters, a place and a story made up from the card), TH:Cr1.1.3c, TH:Cr3.1.3a live on a fresh scenario card; TH:Cr2.1.3b on a kept card. Unit 2, just assessed, carried unscored |
| Year 3 year-end | 53, respond 54 | 27 | Units 1 and 2: TH:Cr3.1.3b live, TH:Pr6.1.3a on a kept reflection card (one line alone, one agreed with the group), TH:Re8.1.3c on an audience card. Unit 3 carried unscored |
| Year 4 mid-year | 97, respond 98 | 17 | Unit 5: TH:Cr1.1.4a, TH:Cr1.1.4c, TH:Pr6.1.4a live; TH:Cr2.1.4b on a kept jobs list. Unit 6 carried unscored |
| Year 4 year-end | 115, respond 116 | 26 | Units 5 and 6: TH:Pr4.1.4b live, TH:Cr2.1.4a on a kept hot-seat sheet, TH:Re8.1.4c on an audience card. Unit 7 carried unscored |
| Year 5 mid-year | 163, respond 164 | 18 | Unit 9: TH:Cr1.1.5a, TH:Cr2.1.5b, TH:Pr6.1.5a live; a kept record card of two lines, one group question the scene was shaped from (TH:Cr2.1.5a, which a performance cannot show) and the inner-thought line (TH:Cr1.1.5c). Unit 10 carried unscored |
| Year 5 year-end | 181, respond 182 | 27 | Units 9 and 10: TH:Pr4.1.5b, TH:Cr3.1.5b live, TH:Cr3.1.5a on a kept self-review line written after the first rehearsal run inside the 8 planning minutes and naming the change made in the rerun, TH:Re8.1.5a on an audience card. Unit 11 carried unscored |

Each check day: set-up 3; warm-up 3; the groups read the new card, plan and rehearse (8); each student completes the
record the card names (4); six group slots of 3 minutes, each performance at most 2 minutes (18); close 4. That is
40 minutes. Each check comes right after a unit's end-of-unit assessment, so it draws its items from the earlier
units and never collects that unit's evidence again. A check is a showing that may follow the unit's showing inside
two weeks: it is on earlier-unit work from a fresh card with its own items, so no item repeats (rule 2, lead call 6
of 2026-11-26; each check day's note says so). No check re-asks an item a unit gave one to three days before: the
nearest sampled item was last given at least ten weeks earlier. On the once-a-week path the year keeps only its
year-end check (week 26, respond week 27); the mid-year check is dropped there (Shorter path).

**Codes no course-level check samples, and why** (sequence-write rule 3). Each is assessed id by id in its own unit's
end-of-unit assessment.

- Ids of the first two units that the one-session form cannot hold beside its live marks and one kept card:
  TH:Cr2.1.3a, TH:Pr4.1.3b, TH:Pr5.1.3a, TH:Re7.1.3a, TH:Re8.1.3a (3); TH:Cr3.1.4a, TH:Pr5.1.4a, TH:Cr3.1.4b,
  TH:Re7.1.4a, TH:Re8.1.4a (4); TH:Pr5.1.5a, TH:Re7.1.5a, TH:Re8.1.5c (5). The exercise-set ids need a warm-up mark
  and the written response ids need the written day's unseen scene, which a check day does not hold.
- The third unit of each year, assessed one week before the year-end check, which by rule 3 draws from earlier units:
  TH:Cr1.1.3b, TH:Pr5.1.3b, TH:Cr3.1.3c, TH:Re9.1.3b, TH:Cn10.1.3a, TH:Cn11.1.3a, TH:Re8.1.3b (3); TH:Cr1.1.4b,
  TH:Pr5.1.4b, TH:Cr3.1.4c, TH:Re9.1.4b, TH:Cn10.1.4a, TH:Cn11.1.4a, TH:Re8.1.4b (4); TH:Cr1.1.5b, TH:Pr5.1.5b,
  TH:Cr3.1.5c, TH:Re9.1.5b, TH:Cn10.1.5a, TH:Cn11.1.5a, TH:Re8.1.5b (5).
- The story unit of each year, which comes after the year-end check: TH:Pr4.1.3a, TH:Cn11.2.3a, TH:Cn11.2.3b,
  TH:Re9.1.3a, TH:Re9.1.3c (3); TH:Pr4.1.4a, TH:Cn11.2.4a, TH:Cn11.2.4b, TH:Re9.1.4a, TH:Re9.1.4c (4); TH:Pr4.1.5a,
  TH:Cn11.2.5a, TH:Cn11.2.5b, TH:Re9.1.5a, TH:Re9.1.5c (5).

The checks sample 7 of the 24 grade 3 ids, 7 of the 24 grade 4 ids and 9 of the 24 grade 5 ids. The frame's check
table limits the sample to one session's live marks and one or two kept cards, so naming these codes with the
reason is enough here (lead call 3); any change to the frame's checks is proposed in the fix report.

## Leans on English language arts

| Lean | Used here | ELA teaches it | Treatment |
|---|---|---|---|
| RL.3.3 | Unit 4, weeks 28 to 32 of year 3 | ELA grade 3 unit 1, weeks 1 to 8 | Taught by then; the story map's "because" arrows carry it |
| W.3.1 | Unit 2 written day, week 16 of year 3 | ELA grade 3 unit 3, weeks 17 to 24 | Theater comes first; bridge on day 24 (response card frame), at most two written items |
| SL.4.4 | Unit 6, weeks 9 to 16 of year 4 | ELA grade 4 unit 1, weeks 1 to 8 | Taught by then; the warm-up card shows "to the back wall" |
| W.4.1 | Unit 6 written day, week 16 of year 4 | ELA grade 4 unit 3, from week 17 | Bridge on day 88 (response card frame) |
| W.5.1 | Unit 10, weeks 9 to 17 of year 5 | ELA grade 5 unit 3, weeks 17 to 25 | Bridge on day 152 (response card frame), at most two written items |
| RL.5.3 | Unit 12, weeks 28 to 32 of year 5 | ELA grade 5 unit 1, weeks 1 to 9 | Taught by then; the comparison chart gives the tellings in rows |
| SL.3.1, SL.4.1, SL.5.1 | Every critique day | ELA from its first unit | Practiced, not owned; the group agreements card shows the turns |

## Shorter path

**The once-a-week path** (32 sessions a year) is written out unit by unit above: each unit keeps its study and
demonstration, rehearsal with the critique and the revision, the showing check, a separate written check and a
respond session, with Fluency days folded into the openers. On this path each year keeps its year-end course-level
check (1 check session in week 26, 1 respond session in week 27) and drops the mid-year one: every id is already
assessed id by id in its own unit, the mid-year check samples only 4 or 5 ids, and the two freed sessions go to the
design and community unit, the heaviest of the year (frame, "The once-a-week path"). Sessions: year 3 8, 8, 9, 5;
year 4 8, 8, 9, 5; year 5 8, 9, 8, 5 (30 a year, plus the check and its respond session). The design unit runs
weeks 17 to 25 (18 to 25 in year 5) and no session of units 3 and 7 holds more than three days. The story units keep
5 sessions: the first holds the study and teaching only, the baseline run and the judging teaching open the second
before its critique and revision, and each of their sessions gives its minute line above; unit 8's second session
is the one five-day merge, named for its unit plan to test. On this path the story units' showing check is the
family showing, with an in-class version for any student without a family yes, and their kept cards are completed
in the written session's 7 spare minutes. No merged session drops a critique, a revision or a respond session.

**A shorter period** (30 to 35 minutes). Set-up drops to 2 minutes, the warm-up to 3, the close to 3. A showing day
fits: six groups of about 4 minutes (24) with set-up and close, the warm-up done in the line before entering, and
the self-check on the guide moves from the showing day to the written day. Units 2 and 6 mark the warm-up itself on
the showing day (TH:Pr5.1.3a, TH:Pr5.1.4a), so they keep their 5-minute warm-up there and run groups of about 3.5
minutes. A written day fits with the response card time cut from 15 to 12 minutes (still at most two written items)
and the self-check added: set-up 2, the unseen scene 6, response card 12, kept cards and the portfolio line 5,
self-check 3, close 3, 31 minutes. A making day keeps its 6-minute clean-up and loses about 7 minutes of making; the
unit's next rehearsal day takes the rest.

**A year about 10 days short, by named fold-in days.** Ten school days short means about 4 sessions of a course that
meets twice a week, so each year names four fold-in days; the spares after them are used, in order, only by a
school that loses more. None of these days is assessed, none is a baseline, critique or revision day, none is the
only teaching day of an owned id, and no owned part is cut: each day's work folds into the neighbor named, as its
opener or a short segment, and no receiving day already carries the 10-minute retrieval (each fold-in day's note in
days.csv says "named" or "spare").

| Year | Fold-in day | Folds into | Saves | Kind |
|---|---|---|---|---|
| 3 | 10 (runs inside the limit) | 11, as the opener | 35 minutes | named |
| 3 | 25 (two versions run) | 26, as the opener | 35 | named |
| 3 | 43 (community scene beat) | 44, as the opener | 35 | named |
| 3 | 45 (rehearsal with costume) | 46, inside the making session | 30 | named |
| 3 | 6 (improvise from a new card) | 5, a 15-minute segment | 25 | spare |
| 3 | 7 (comparing two ideas) | 8, a 15-minute segment | 25 | spare |
| 3 | 19 (voice and thinking sets) | 20, a 15-minute segment of the fluency day that runs the sets | 25 | spare |
| 3 | 23 (pairs play both versions) | 22, a 15-minute segment | 25 | spare |
| 3 | 40 (groups sketch a scene) | 39, a 15-minute segment | 25 | spare |
| 3 | 42 (a community piece) | 41, a 15-minute segment | 25 | spare |
| 4 | 74 (run, review, rerun) | 75, as the opener | 35 | named |
| 4 | 89 (wordless beat runs) | 90, as the opener | 35 | named |
| 4 | 107 (cue run) | 108, as the opener | 35 | named |
| 4 | 70 (improvise from a new card) | 69, a 15-minute segment | 25 | named |
| 4 | 72 (jobs listed) | 71, a 15-minute segment | 25 | spare |
| 4 | 87 (wordless pair scene) | 86, a 15-minute segment | 25 | spare |
| 4 | 83 (ensemble exercises) | 84, a 15-minute segment of the fluency day that runs the exercise | 25 | spare |
| 4 | 104 (characters compared) | 103, a 15-minute segment | 25 | spare |
| 4 | 106 (local-problem scene built) | 105, a 15-minute segment | 25 | spare |
| 4 | 67 (circumstances walk) | 68, a 15-minute segment of the fluency day that runs the walk | 25 | spare |
| 5 | 137 (self-review run) | 138, as the opener | 35 | named |
| 5 | 154 (wordless beat runs) | 155, as the opener | 35 | named |
| 5 | 173 (cue run) | 174, as the opener | 35 | named |
| 5 | 134 (original scene shaped) | 133, a 15-minute segment | 25 | named |
| 5 | 135 (set jobs) | 136, a 15-minute segment | 25 | spare |
| 5 | 151 (wordless scene built) | 150, a 15-minute segment | 25 | spare |
| 5 | 149 (picking matched warm-ups) | 148, in its warm-up slot, a 15-minute segment | 25 | spare |
| 5 | 131 (Bottom's speech) | 132, a 15-minute segment of the fluency day that runs the beat | 25 | spare |
| 5 | 167 (the cue sheet) | 168, a 15-minute segment of the cue drill | 25 | spare |
| 5 | 158 (reactions written in pairs) | 159, a 10-minute segment | 30 | spare |

Total: the four named days save 135 minutes in year 3, 130 in year 4 and 130 in year 5, leaving 60 sessions a year
against the frame's 64. Every spare as well saves 285, 280 and 285 minutes, leaving 54. Days 153 and 171 are no longer
fold-in days (with them folded, TH:Re8.1.5a and TH:Re8.1.5b had no teaching day of their own), and day 158, the
unit's only feedback on defended reactions, is the last spare. Baseline-look days, critique days, revision days, both
check days, respond days and family showings never fold.

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week (one on the once-a-week path); a clear floor; step cards, scene cards, response cards; found and low-cost materials; a classroom teacher led by each unit's teacher page (a drama teacher where the school has one) | The body, voice and design taught in steps; plays, forms and makers studied with their setting; improvising and rehearsal with a critique and a revision; a showing each unit | A portfolio folder of 12 pieces over the band with reflections; 12 showings, three of them for families; two marks a unit per student on the main look-for | Met marks on the year's 24 ids and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result.

## For the lead

1. **Course-level check coverage (rule 3).** The frame's checks sample 23 of the 72 ids; the other 49 are named
   above with the reason (the one-session form, the unit just assessed, the story unit after the year-end check).
   Each is assessed id by id in its unit. If the lead wants more sampled, the frame's fix would be a talk-free kept
   card on the year-end check for the third unit's ids (a prop-sketch item); this scope does not add it.
2. **school_day pattern.** Filled as the even spread, school day ceil(2.5 n), counting on across the band (3 to
   480), which frame.py reads as the frame's weeks (lead call 5 of 2026-11-26 keeps the band-wide count; the lead
   documents it in CALENDAR.md). Theater, grades K to 2 uses a different pattern (second and fourth school days of
   each week) that reads the same weeks; the lead may want one pattern for all arts courses.
3. **Once-a-week path (settled in the 2026-11-26 fix pass).** The frame now drops the mid-year check on that path
   and gives the design unit 9 sessions (8 in year 5); units 3, 7 and 11 hold at most three days a session, and the
   story units' sessions carry minute lines. Unit 8's second session stays a five-day merge, which its unit plan
   tests; if it fails, the frame's fix would be a critique on two model groups.
4. **Supplies ceiling (money, for Cory).** Carried from the frame: provisional $35, $40 and $30 a class of 30 for
   years 3, 4 and 5, all optional beside a free path; pick a $40 ceiling a class a year. Not decided here.
5. **Browser checks for the unit plans:** Holder's Wiz designs (unit 3), a griot practitioner's published words
   (unit 4), the public domain Stanislavski wording (unit 5), FastHorse's own words (unit 7), Mhlophe's own words
   (unit 8), the Laedza Batanani account (unit 11) and the Zuni Pueblo heritage pages (unit 12). The living-or-not
   line for Irwin, FastHorse, Mhlophe and Valdez is recorded by each unit plan as of its date.
6. **Frame items 1 to 3 and 7 stand** (check weeks, the once-a-week respond session in week 27, the theater time
   figure, the three sensitivity calls); this scope follows them and asks no change.
7. **Days 60 and 188 (unit 4 and 12 critique days).** The kept cards moved to days 58 and 186, so each holds the
   critique, the revision and one card. If a whole-class critique of six groups still cannot hold, the frame's unit
   4 and 12 rows may run the critique on two model groups, the rest applying the three steps to their own run
   (expert read, finding 3).
