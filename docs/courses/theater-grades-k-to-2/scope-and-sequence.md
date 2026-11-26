# Scope and sequence: Theater, grades K to 2

Course `theater-grades-k-to-2` (catalogue id `theater-k-2`), grades K to 2 as three years in one file, draft, written 2026-11-26 from the frame (docs/courses/theater-grades-k-to-2/frame.md), fixed the same day from the
expert read (docs/reviews/sequence-theater-grades-k-to-2-fixes-2026-11-26.md). The days live in data/plans/theater-grades-k-to-2/days.csv.

## The band on one page

- **Which grade's standards fall in which year.** Year K (course days 1 to 64) claims only the 17 kindergarten theater
  ids (`.Ka`, `.Kb`); year 1 (days 65 to 128) only the 24 grade 1 ids; year 2 (days 129 to 192) only the 24 grade 2
  ids: 65 in all, the counts in docs/courses/arts/STANDARD.md 3.2. Every id is taught and assessed in its own year,
  each named with its line in data/standards/ncas-performance-standards-words.txt, never quoted. A year brings back
  the year before's techniques as practice, never as a claim. No pre-kindergarten id is claimed.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a child's record shows which grade's standards they met. Where a child meets
  year 2 before year 1, each unit's day 2 retrieval task carries its ten-minute reteach of the earlier technique.
- **Units and days.** 12 units, 192 course days, 64 a year: 60 in four units, 2 course-level check days and 2 respond
  days. `stretch` is the unit number of the frame's Units table; `unit` is `<unit>.1` (no unit is split into
  sections at this stage).
- **How school_day is counted.** The course meets two 40-minute sessions a week for 32 weeks a year, 96 weeks over
  the band. Course day n falls in year i = (n - 1) // 64 (0 for K, 1 for grade 1, 2 for grade 2), as day k = n - 64i of
  that year, in week ceil(k / 2) of the year; the two sessions sit on the second and fourth school days of the week.
  school_day counts on across the band, 160 school days a year: school_day = 160i + 5(week - 1) + 2 for an odd k and
  + 4 for an even k, so a year runs school days 2 to 159, 162 to 319 and 322 to 479. Week of the year = (school_day - 160i - 1) // 5 + 1;
  every unit and check falls in the frame's weeks. school_day counts across the whole band, as frame.py reads it, and
  a filled school_day wins over frame.py's even spread. A school picks its own two days; the week is what CALENDAR.md
  reads.
- **The four processes.** Each year carries all four artistic processes (create; perform; respond; connect), and each
  unit touches at least the processes its frame row names; a unit need not claim all four. Where a unit practices a
  process beyond its owned ids (a connecting talk, the critique as responding, a work looked at), the unit section
  names the day as practice, and no id is claimed outside the unit's owned rows. The unit sections below name the days. Each unit runs technique days before the making that needs them, a
  rehearsal day with the unit's one critique (describe, ask, suggest), a revision day, then the two end-of-unit
  check days (a showing day and a teacher's-table day), then a respond day.
- **Assessment pattern.** No unit is over 25 days, so none holds a mid-unit assessment. Each unit's end-of-unit
  assessment is its two check days, marked against the frame's id-by-id evidence line; kept cards made on the last
  rehearsal or making day are scored after that session with the showing day's marks. Response time is the respond
  day after the two check days, counted once. Each unit opens with a baseline look at its main look-for on its first
  practice day (named in the note), so every child has two marks a unit. One portfolio piece a unit, with a spoken
  one-line reflection, is filed on the respond day (or the family showing day in units 4, 8 and 12).
- **Readiness and retrieval.** Year K assumes no earlier theater (the seven kindergarten threads start here), so no
  readiness check is given anywhere in the band. Every year 1 and year 2 unit opens with a retrieval task inside
  day 2's opener on the year before's row in its thread (last used one grade back), in the `retrieves` column; day 1
  of every unit stays clean for the hook and the compelling question. Inside year K, units 2 to 4 also retrieve the
  agreements, the character voice and the puppets where they are used again (days 20, 40 and 56).
- **Equipment and safe use.** The supplies columns are math and science only. The unit's hazards line (the frame's
  last Units column) holds on every floor day of the unit; a day's note names only its day-specific controls, its
  equipment and the free path where the frame lists one. The day-specific controls sit where a hazard is rehearsed:
  the heap as a slow-motion freeze (days 74 to 78), no falls (95 to 100), no weapons or contact (112 to 114), the
  giant's slow walk and the freeze for "scared" (155 to 158). Safety rules are "from memory" until
  each unit's fresh safety read checks them (frame, "Safety read").
- **Sensitivity.** Each day that studies a flagged tradition or touches the child's own life names it in the note:
  kamishibai (unit 1), the troll (2), Chinese shadow puppetry (3), the Akan tale and Nyame (4), the Handspring horse's
  war story (6), bunraku and mamulengo (7), community stories (8), the Panchatantra tale (9), Peking opera (10),
  Karagöz (11) and the Cherokee story (12). Every tie to a child's own life offers an invented or public option
  marked the same, and carries health's steps for "If a student tells you something".

## Year K (kindergarten ids, course days 1 to 64)

### Unit 1. Let's pretend together

Days 1 to 18, weeks 1 to 9 of year K. *How do we go into a make-believe place together, and how do we each add to it?*

Arc: the room's routines come first (the set-up, the agreements card, the freeze signal), then the two techniques
(freeze and melt, walking as someone in a place), then the what-if card, questions with the teacher in role and
adding on to a classmate, then groups choose a place card, rehearse, take the critique, revise and show it to a
partner class. The order follows the frame: no child is asked to use voice, props or a tale before they can play
safely in a shared place. Days by load: five ids and the year's routines learned for the first time; four days on
technique and routine (1 to 4), five on the ideas, questions and adding on (5 to 10), five on rehearsal, critique and
revision (11 to 15).

- Processes: create on days 4, 6, 8 to 15; perform on days 9 and 11 to 16 (showing 16); respond to another artist's
  work on days 1 (kamishibai) and 5 (Polyglot Theatre), and as critic on day 13; connect on days 5 and 15 (a real or
  story place like ours).
- Readiness: none (first unit of the band). Baseline look on day 9, the first day the place is played.
- End-of-unit assessment: day 16 (showing; look-fors TH:Cr1.1.Ka, TH:Cr2.1.Ka, TH:Re9.1.Ka) and day 17 (teacher's
  table; talk items TH:Cr2.1.Kb, TH:Cr3.1.Ka). Respond day 18.
- Candidate (the bar's criterion 9 on set-up and close minutes when desks must be moved): kept, at no added day. Day 1
  teaches the set-up routine slowly (the unit plan may run day 1's entering seated, faces and hands only, so the
  freeze signal is learned before anyone moves; the full place walk waits for day 4); from day 2 the 3-minute set-up and 4-minute close sit inside every 40-minute day,
  and the unit plan's day rows give those minutes.
- Once-a-week path, 8 sessions: 1 (days 1, 2), 2 (3, 4, 5), 3 (6, 7, 8), 4 (9, 10, 11), 5 (12 to 15: critique,
  revision, last run), 6 showing (16), 7 teacher's table (17), 8 respond (18). Fluency days 3, 7, 10 and 12 fold into
  their session's opener.

### Unit 2. Voices and sounds

Days 19 to 36, weeks 10 to 18 of year K. *How do our voices and sounds tell a story, and how do we feel about the characters?*

Arc: Billy Goats Gruff told flat and then with voices opens the question; the voice warm-up and the goat voices and
sound effects are taught in steps; a second kamishibai story and the teacher's live sound story give the class two
works to feel about and name a favorite part of, on the first audience cards; groups then take parts, drill their
cues, take the critique, revise and show the sound story. Voices come before puppets (unit 3) because a puppet
speaks with a character voice. Days by load: four ids, but two of them are the year's first responding ids, so four
days are study and audience-card days (23, 26, 27, 32) beside eight voice and cue days.

- Processes: create on days 22 and 28 (choosing a part and its sound); perform on days 20 to 33 and 34; respond on
  days 19, 23 and 26 (the retelling, the kamishibai story, the teacher's show) and as critic on day 30; connect on
  day 32 (a sound from the child's day).
- Retrieval: day 20 opener brings back the agreements and freeze signal (th-k-show, unit 1). Baseline look on day 25, the first day the story cues are played.
- End-of-unit assessment: day 34 (showing; look-for TH:Pr6.1.Ka, kept audience card TH:Re7.1.Ka) and day 35 (talk
  items TH:Pr5.1.Ka, TH:Re8.1.Ka). Respond day 36.
- Lean SL.K.6: ELA kindergarten carries it from its day 36 (week 8), before this unit; the frame's bridge stays on
  day 21 (the warm-up card's "say it so the back row hears" in pictures), and no sentence-level speaking is marked.
- Candidate (a sound story from Africa or the Americas beside Billy Goats Gruff): dropped. Year K already studies an
  Akan tale (unit 4) and works from Japan, Australia, China and Malaysia; a fourth work in an 18-day voice unit would
  take a rehearsal day, and the band's range is checked across the three years (Brazil in unit 7, a Cherokee story
  in unit 12).
- Once-a-week path, 8 sessions: 1 (19, 20, 21), 2 (22, 23, 24), 3 (25, 26, 27), 4 (28, 29, 30), 5 (31, 32, 33),
  6 showing (34), 7 teacher's table (35), 8 respond (36).

### Unit 3. Puppets and props

Days 39 to 52, weeks 20 to 26 of year K. *How can a paper bag become a character, and how is a character like me?*

Arc: the Paper Bag Players open the question; the prop-sketch and the puppet steps come before the making day; the
shadow tradition and the flashlight and sound cue are taught next; the two-ties card brings in "like me" and a skill
from another subject; then the puppet scene is rehearsed, critiqued, revised and shown. Making comes before cue work
because a shadow scene needs a puppet to move. Days by load: four ids in 14 days, two making days (40, 41), three
technique and study days (39, 42, 43), one connecting day (44), five rehearsal days.

- Processes: create on days 40, 41 and 45; perform on days 45 to 50; respond on days 39 and 42 (the Paper Bag Players,
  Chinese shadow puppetry) and as critic on day 47; connect on days 44, 45 and 49.
- Retrieval: day 40 opener brings back the character voice (th-k-actor, unit 2). Baseline look on day 45, the first scene played with the puppets.
- End-of-unit assessment: day 50 (look-fors TH:Cr1.1.Kb, TH:Pr5.1.Kb) and day 51 (talk items TH:Cn10.1.Ka,
  TH:Cn11.1.Ka). Respond day 52.
- Candidate (a puppet form from Africa or the Americas beside the two works): dropped. The band meets Brazilian
  mamulengo in unit 7 and South Africa's Handspring in unit 6; a third work here would cost one of the unit's two
  making days.
- Once-a-week path, 7 sessions: 1 (39, 40), 2 making (41, with its 6-minute clean-up), 3 (42, 43, 44), 4 (45 to 49:
  the puppet scene, critique, revision), 5 showing (50), 6 teacher's table (51), 7 respond (52).

### Unit 4. Acting out a tale

Days 55 to 64, weeks 28 to 32 of year K. *Who is in a story and where does it happen, and how is one tale different from another?*

Arc: the Anansi tale on the story map (who and where), then its places and the step card for acting one moment,
then the mouse-deer tale told beside it; the class acts the Anansi tale with the year's puppets and props, takes the
critique, revises, makes its kept story map, and shows it; day 64 is the family showing. Last in the year because the
tale uses units 1 to 3, after the year-end check in week 27. Days by load: the shortest unit; its tale is short and
its showing reuses the year's props and warm-ups, so three teaching days carry four ids.

- Processes: create on days 58 and 60 (choosing an animal, revising); perform on days 58 to 61 and 64; respond on days
  55 and 57 (the two tales) and as critic on day 59; connect on days 57 and 62 (telling two tales apart, TH:Cn11.2.Ka).
- Retrieval: day 56 opener brings back puppets, props and the character voice (th-k-design, th-k-actor). Baseline
  look on day 58.
- End-of-unit assessment: day 61 (look-for TH:Cn11.2.Kb; kept story map TH:Pr4.1.Ka from day 60) and day 62 (talk
  items TH:Re8.1.Kb, TH:Cn11.2.Ka). Respond day 63; family showing day 64, unscored.
- Lean RL.K.3: ELA kindergarten carries it from its day 49 (week 10), so it is taught by now.
- Candidate (the Akan source confirmed against a Ghanaian or Akan-run telling): kept, at no added day; the unit plan
  and the sensitivity agent check it before day 55.
- Once-a-week path, 5 sessions: 1 study and teaching only (55, 56, 57), 2 acting, critique and revision with the kept
  story map (58, 59, 60), 3 showing check as the family showing (61 with 64, an in-class version for any child
  without a family yes), 4 teacher's table (62), 5 respond (63).

## Year 1 (grade 1 ids, course days 65 to 128)

### Unit 5. Building a story together

Days 65 to 80, weeks 1 to 8 of year 1. *How do we build a story one step at a time, and who decides what happens next?*

Arc: the Turnip on a story strip, then "yes, and", then a kamishibai plot built card by card and what a character
might choose, then gestures and movement; the class plays the Turnip, votes at a choice point, changes the plot, and
groups rehearse, take the critique, revise and show their own endings. Days by load: six ids in two threads; each id
gets a teaching day (65, 66, 68, 69, 71, 72) before rehearsal.

- Processes: create on days 65 and 68 to 72; perform on days 70 and 74 to 78; respond on day 68 (the kamishibai
  teller, with kamishibai named again as a real form from unit 1's collection page) and as critic on day 75; connect on day 77 (a group decision at home, school or in a story).
- Retrieval: day 66 opener on entering a place and the agreements (th-k-imagine, th-k-show). Baseline look on day 67.
- End-of-unit assessment: day 78 (look-fors TH:Cr2.1.1a, TH:Cr3.1.1a, TH:Re9.1.1a; kept vote card TH:Cr2.1.1b from
  day 77) and day 79 (talk items TH:Cr1.1.1a, TH:Cr1.1.1c). Respond day 80.
- Candidate (a cumulative tale from Africa, Asia or the Americas beside the Turnip): dropped. Year 1 meets South
  Africa, Brazil and Japan in units 6 and 7; a second tale would take a rehearsal day from a 16-day unit with six ids.
- Once-a-week path, 7 sessions: 1 (65, 66, 67), 2 (68, 69, 70), 3 (71, 72, 73), 4 (74 to 77), 5 showing (78), 6
  teacher's table (79), 7 respond (80).

### Unit 6. Face, body, voice

Days 81 to 102, weeks 9 to 19 of year 1. *How can we show what a character feels without saying it, and what do we remember about the choices we made?*

Arc: Marceau's Bip opens; the feelings warm-up, still-then-moving and the mirror game come first (81 to 86); the
Handspring horse and two contrasting characters follow; then a guided drama of changing feelings, and four
responding days (remember a choice, preference, comparing self and a character, what two characters went through)
before the groups plan, rehearse, take the critique, revise and show a "no words" scene. Days by load: the longest
year 1 unit, eight ids in two threads; nine teaching days, then nine rehearsal days.

- Processes: create on days 88 and 94; perform on days 82 to 89 and 94 to 100; respond on days 81, 87 and 91 (Marceau,
  the Handspring horse, the teacher's show), 90 and 92, and as critic on day 97; connect on days 92 and 99.
- Retrieval: day 82 opener on voices and sounds and how a character made you feel (th-k-actor, th-k-notice).
  Baseline look on day 83.
- End-of-unit assessment: day 100 (look-fors TH:Pr4.1.1b, TH:Pr6.1.1a; audience cards TH:Re7.1.1a, TH:Re8.1.1c) and
  day 101 (the teacher's original scene answered on audience cards TH:Re8.1.1a, TH:Re9.1.1c; talk items TH:Pr5.1.1a,
  TH:Cr3.1.1b). Respond day 102.
- Candidate (a third work showing feeling without words, by a maker from Asia or the Americas): dropped. Unit 7 brings
  Japan and Brazil a few weeks later; the unit's eight ids need its nine teaching days.
- Once-a-week path, 9 sessions: 1 (81, 82, 83), 2 (84, 85, 86), 3 (87, 88, 89), 4 (90, 91, 92), 5 (93 to 96,
  fluency 93 and 95 in the opener), 6 (97, 98, 99), 7 showing (100), 8 teacher's table (101), 9 respond (102).

### Unit 7. One thing, many things

Days 105 to 116, weeks 21 to 26 of year 1. *How can a scarf become a river or a cape, and what do we bring to a drama from what we know?*

Arc: bunraku and the object game open; mamulengo and the prop-sketch plan come next; the tech elements and the
class box, then the two-ties card; one making day on which the group labels its kept prop-sketch with the teacher, one rehearsal, the
critique and a revision with each child's "what we changed" line; then the showing. Days by load: six ids in 12 days;
three ids are prop-sketch items, so planning (106, 108) and the making day (110) carry them: the plan is begun before
the making and labeled during it, so it is scored as a plan.

- Processes: create on days 105 to 107 and 110; perform on days 111 to 114; respond on days 105 and 106 (bunraku,
  mamulengo) and as critic on day 112; connect on days 109 and 115.
- Retrieval: day 106 opener on puppets, props and "like me" (th-k-design, th-k-world). Baseline look on day 107.
- End-of-unit assessment: day 114 (look-for TH:Cr3.1.1c; prop-sketch items TH:Cr1.1.1b, TH:Re9.1.1b, TH:Pr5.1.1b begun
  day 106 and labeled day 110) and day 115 (talk items TH:Cn10.1.1a, TH:Cn11.1.1a). Respond day 116.
- Candidate (a third object-theater work by a living maker from Africa or Asia): dropped. Both traditions studied are
  living, and the unit has one making day already; a third work would cut the rehearsal.
- Once-a-week path, 7 sessions: 1 (105, 106), 2 (107, 108, 109), 3 (110, 111), 4 (112, 113), 5 showing (114), 6
  teacher's table (115), 7 respond (116).

### Unit 8. Stories from our community

Days 119 to 128, weeks 28 to 32 of year 1. *Why do characters do what they do, and how are the stories told around us alike and different?*

Arc: the Lion and the Mouse and what its characters do and say; the "because" arrow and the three-freeze scene;
two school-made community stories compared; then rehearsal, critique, revision with the kept story map, the showing
and the family showing. Days by load: four ids, three teaching days, as unit 4.

- Processes: create on days 120 and 122; perform on days 122 to 125 and 128; respond on days 119 and 121 and as critic
  on day 123; connect on days 121 (TH:Cn11.2.1a) and 124 (TH:Cn11.2.1b).
- Retrieval: day 120 opener on who and where in a tale (th-k-story). Baseline look on day 122.
- End-of-unit assessment: day 125 (look-for TH:Cn11.2.1b; kept story map TH:Re8.1.1b from day 124) and day 126 (talk
  items TH:Pr4.1.1a, TH:Cn11.2.1a). Respond day 127; family showing day 128, unscored.
- Lean RL.1.3: ELA grade 1 carries it from its day 10, so it is taught by now.
- Candidate (the community storyteller visit planned with the school's own visitor rules): kept as an optional extra
  inside day 121, no day added; the two school-made stories stay the default.
- Once-a-week path, 5 sessions: 1 study and teaching only (119, 120, 121), 2 acting, critique and revision with the
  kept story map (122, 123, 124), 3 showing check as the family showing (125 with 128), 4 teacher's table (126), 5
  respond (127).

## Year 2 (grade 2 ids, course days 129 to 192)

### Unit 9. Words for the characters

Days 129 to 144, weeks 1 to 8 of year 2. *How do we make up what characters say, and how do we decide together where a story goes?*

Arc: the Monkey and the Crocodile, then new details, then a line said three ways and the voice and sounds, then
Rizal's Monkey and the Turtle and the "line, reply" pair; groups make lines, decide how the story goes on, change
lines, rehearse, take the critique, revise and share the scene. Days by load: seven ids, five teaching days (129 to
131, 133, 135), two fluency days, six rehearsal days because three ids are marked in the shared scene.

- Processes: create on days 130 to 137; perform on days 138 to 142; respond on days 129 and 133 (the two tellings; day 129 adds one line on a living storyteller or company that tells
  the Panchatantra to children, described and linked) and
  as critic on day 139; connect on day 141.
- Retrieval: day 130 opener on a plot built in order and group decisions (th-g1-imagine, th-g1-show). Baseline look on
  day 134, the first day lines are made up.
- End-of-unit assessment: day 142 (look-fors TH:Pr6.1.2a, TH:Re9.1.2a, TH:Cr2.1.2a; kept scene card TH:Cr3.1.2a and
  vote card TH:Cr2.1.2b from day 141) and day 143 (talk items TH:Cr1.1.2a, TH:Cr1.1.2c). Respond day 144.
- Candidate (a dialogue tale from the Americas or Oceania): dropped. Unit 9 already compares two tellings (India and
  the Philippines); year 2 meets the Americas in units 11 and 12, and Oceania is met in year K.
- Once-a-week path, 8 sessions: 1 (129, 130), 2 (131, 132, 133), 3 (134, 135), 4 (136, 137, 138), 5 (139, 140, 141), 6
  showing (142), 7 teacher's table (143), 8 respond (144).

### Unit 10. Small changes, big differences

Days 145 to 160, weeks 9 to 16 of year 2. *How do small changes in voice and movement show who a character is, and when do performers choose how to show a character?*

Arc: Peking opera opens; the three-ways drill and think-move-speak are taught; Marceau's The Mask Maker and the
teacher's scene played twice make performers' choices visible; problems characters face, others' feelings and the
child's own reactions follow; groups build one character in three moods, adjust them with the teacher's side-coaching
(155), take the unit's one critique (156), revise and show. Days by load: seven ids, nine teaching days, five rehearsal
days.

- Processes: create on days 155 to 157 (adjusting movements and sounds; the critique only on 156); perform on days 146 to 158; respond on days
  145, 149 and 150 (Peking opera, The Mask Maker, the teacher's scene), 152 and 153, and as critic on day 156; connect
  on day 157.
- Retrieval: day 146 opener on face, body, gesture and voice and comparing self with a character (th-g1-actor,
  th-g1-notice). Baseline look on day 147.
- End-of-unit assessment: day 158 (look-fors TH:Pr4.1.2b, TH:Cr3.1.2b; audience cards TH:Re7.1.2a, TH:Re8.1.2c) and
  day 159 (the teacher's original scene opens; talk items TH:Re8.1.2a, TH:Pr5.1.2a; audience card TH:Re9.1.2c).
  Respond day 160.
- Lean SL.2.4: ELA grade 2 carries it from its day 104 (week 21), after this unit; the frame's "if later" bridge is
  in the notes of days 145 and 158: the unit marks only the voice and movement changes of a character, never a whole
  story told aloud.
- Candidate (a third work by a living maker from Africa or the Americas, showing a character through movement):
  dropped. Peking opera has living performers and Basil Twist (unit 11) is a living American maker; the unit's seven
  ids need its days.
- Once-a-week path, 8 sessions: 1 (145, 146, 147), 2 (148, 149, 150), 3 (151, 152, 153), 4 (154, 155), 5 (156, 157),
  6 showing (158), 7 teacher's table (159), 8 respond (160).

### Unit 11. Setting the scene

Days 163 to 180, weeks 18 to 26 of year 2. *How can a sheet, a light and a box make a whole place, and what do we know that fits the drama?*

Arc: Basil Twist's light and fabric open; the bird's-eye set plan, Karagöz and the light-and-sound cue, an object
alone as many things, a prop that shows a place, and the two-ties card are taught first (163 to 170); then the group
draws its kept set plan (171), labels it with the teacher as it builds over two making days (172, 173), rehearses in
the set, takes the critique and revises with each child's "what we changed" line. Days by load: the longest year 2 unit; scenery joins props and the cue needs rehearsal, so two making days and
four rehearsal days.

- Processes: create on days 164, 167 and 171 to 173; perform on days 174 to 178; respond on days 163 and 165 (Basil
  Twist, Karagöz) and as critic on day 176; connect on days 170 and 171.
- Retrieval: day 164 opener on planning costumes and props and feelings tied to my life (th-g1-design, th-g1-world).
  Baseline look on day 166, the first day cues are run.
- End-of-unit assessment: day 178 (look-fors TH:Pr5.1.2b, TH:Re9.1.2b; kept set plan TH:Cr1.1.2b drawn day 171, labeled day 172) and day
  179 (table item TH:Cr3.1.2c; talk items TH:Cn10.1.2a, TH:Cn11.1.2a). Respond day 180.
- Candidate (a set or light work by a living maker from Africa or Asia): dropped. Karagöz is a living tradition of
  Türkiye; a third work would take a making day.
- Once-a-week path, 7 sessions: 1 (163, 164, 165), 2 (166 to 170, fluency 166 and 168 in the opener), 3 making (171,
  172, 173), 4 (174 to 177: cue run, critique, revision), 5 showing (178), 6 teacher's table (179), 7 respond (180).

### Unit 12. One story, many tellings

Days 183 to 192, weeks 28 to 32 of year 2. *How do people in different places tell the same kind of story, and how can a true text become a scene?*

Arc: the Tortoise and the Hare with its parts and cause and result arrows; the Cherokee story heard and compared,
with a short third telling; the bee card turned into a narrator-and-movers scene; then rehearsal, critique, revision
with the kept story map, the showing and the family showing. Last in the band because it uses the year's dialogue,
character work and set.

- Processes: create on days 185 and 186; perform on days 186 to 189 and 192; respond on days 183 and 184 and as
  critic on day 187; connect on days 184 (TH:Cn11.2.2a) and 185 (TH:Cn11.2.2b).
- Retrieval: day 184 opener on what a character does and why (th-g1-story), asked of the short third telling. Baseline look on day 186.
- End-of-unit assessment: day 189 (look-for TH:Cn11.2.2b; kept story map TH:Re8.1.2b from day 188) and day 190 (talk
  items TH:Pr4.1.2a, TH:Cn11.2.2a). Respond day 191; family showing day 192, unscored.
- Candidates: (a) the Cherokee source confirmed as the nation's own published teaching: kept, no day added, checked
  by the unit plan and the sensitivity agent before day 184, with the frame's swap if it fails; (b) a second
  culture's race or trickster story from Africa or Asia for a three-way compare: kept, no day added, heard inside day
  184's retrieval opener, whose task asks what its character does and why (th-g1-story), so the opener serves both
  and the rest of the day goes to the Cherokee story and the three-way compare; TH:Cn11.2.2a ("several cultures")
  compares three tellings. The unit plan picks the telling and checks
  its rights line.
- Once-a-week path, 5 sessions: 1 study and teaching only (183, 184, 185), 2 acting, critique and revision with the
  kept story map (186, 187, 188), 3 showing check as the family showing (189 with 192), 4 teacher's table (190), 5
  respond (191).

## Course-level checks

Each check is one check day and one respond day, on the frame's weeks, all off the core check and respond weeks for
the grade (CALENDAR.md target weeks: K 14 to 18 and 29 to 32; grade 1 14 to 16, 19 and 29 to 32; grade 2 14 to 16,
18 to 20 and 28 to 32). Arts are specials in K to 2 and do not count against the classroom teacher's stagger
(CALENDAR.md rule 1), and the course has no one-to-one ELA or math check of its own (rule 2).

| Check | Course days | Week | What it samples |
|---|---|---|---|
| Year K mid-year | 37, respond 38 | 19 | Unit 1, an earlier unit: TH:Cr1.1.Ka, TH:Cr2.1.Ka, TH:Re9.1.Ka live on a fresh what-if drama. Unit 2, just assessed, is carried unscored |
| Year K year-end | 53, respond 54 | 27 | Units 1 and 2: TH:Cr2.1.Kb live (each child adds one idea of their own to the scene), TH:Pr6.1.Ka live, TH:Re7.1.Ka on an audience card. Unit 3, just assessed, carried unscored |
| Year 1 mid-year | 103, respond 104 | 20 | Unit 5: TH:Cr2.1.1a, TH:Cr2.1.1b, TH:Re9.1.1a. Unit 6 carried unscored |
| Year 1 year-end | 117, respond 118 | 27 | Units 5 and 6: TH:Cr3.1.1a, TH:Pr4.1.1b, TH:Pr6.1.1a live, TH:Re7.1.1a on an audience card. Unit 7 carried unscored |
| Year 2 mid-year | 161, respond 162 | 17 | Unit 9: TH:Cr2.1.2a, TH:Cr2.1.2b, TH:Pr6.1.2a, TH:Re9.1.2a. Unit 10 carried unscored |
| Year 2 year-end | 181, respond 182 | 27 | Units 9 and 10: TH:Cr3.1.2a (each group says one line, tries it another way at the teacher's prompt and keeps the change), TH:Pr4.1.2b, TH:Cr3.1.2b live, TH:Re7.1.2a on an audience card. Unit 11 carried unscored |

Each check comes right after a unit's end-of-unit assessment, so it draws its items from the earlier units, as the
day's goal and note say, and never collects that unit's evidence again; each is a fresh guided drama, not the task
form of the showing just given. A showing is theater's own evidence, so a check showing on a fresh scene card with its
own items, drawn from earlier units, meets the two-week rule though it follows a unit showing (lead call 6; each
check day's note says so). No check re-asks items a unit gave one to three days before: every sampled id comes from a
unit that ended at least two weeks earlier (lead call 7). The teacher marks one group at a time and hears no talk
items on a check day.

**Codes no course-level check samples, and why** (sequence-write rule 3). Each is assessed id by id in its own unit's
end-of-unit assessment.

- Talk and teacher's-table items: TH:Cr3.1.Ka, TH:Pr5.1.Ka, TH:Re8.1.Ka (K); TH:Cr1.1.1a, TH:Cr1.1.1c, TH:Pr5.1.1a,
  TH:Cr3.1.1b (1); TH:Cr1.1.2a, TH:Cr1.1.2c, TH:Pr5.1.2a, TH:Re8.1.2a (2). The frame's check day is a live group
  showing with no talk items, so the teacher never marks a performance and hears talk at once.
- Audience-card ids beyond the one card each year-end check uses: TH:Re8.1.1a, TH:Re8.1.1c, TH:Re9.1.1c (1);
  TH:Re8.1.2c, TH:Re9.1.2c (2).
- The third unit of each year, assessed one week before the year-end check, which by rule 3 draws from earlier units:
  TH:Cr1.1.Kb, TH:Pr5.1.Kb, TH:Cn10.1.Ka, TH:Cn11.1.Ka (K); TH:Cr1.1.1b, TH:Pr5.1.1b, TH:Cr3.1.1c, TH:Re9.1.1b,
  TH:Cn10.1.1a, TH:Cn11.1.1a (1); TH:Cr1.1.2b, TH:Pr5.1.2b, TH:Cr3.1.2c, TH:Re9.1.2b, TH:Cn10.1.2a, TH:Cn11.1.2a (2).
- The story unit of each year, which comes after the year-end check (weeks 29 to 32 hold every core year-end check):
  TH:Pr4.1.Ka, TH:Re8.1.Kb, TH:Cn11.2.Ka, TH:Cn11.2.Kb (K); TH:Pr4.1.1a, TH:Re8.1.1b, TH:Cn11.2.1a, TH:Cn11.2.1b (1);
  TH:Pr4.1.2a, TH:Re8.1.2b, TH:Cn11.2.2a, TH:Cn11.2.2b (2).

The checks sample 6 of 17 kindergarten ids, 7 of 24 grade 1 ids and 8 of 24 grade 2 ids (see For the lead).

## Leans on English language arts

| Lean | Used here | ELA teaches it | Treatment |
|---|---|---|---|
| SL.K.6 | Unit 2, days 19 to 36, weeks 10 to 18 | ELA K from its day 36, week 8 | Taught first; bridge kept on day 21 (picture card), no sentence-level speaking marked |
| RL.K.3 | Unit 4, weeks 28 to 32 | ELA K from its day 49, week 10 | Taught by then |
| RL.1.3 | Unit 8, weeks 28 to 32 of year 1 | ELA grade 1 from its day 10, week 2 | Taught by then |
| SL.2.4 | Unit 10, weeks 9 to 16 of year 2 | ELA grade 2 from its day 104, week 21 | Theater comes first; bridge on days 145 and 158 |
| SL.K.1, SL.1.1, SL.2.1 | Every critique day | ELA from its day 1, 6 and 1 | Practiced, not owned; the agreements card shows the turn-taking rules in pictures and the teacher models the first critique (day 13) |

## Shorter path

**The once-a-week path** (32 sessions a year) is written out unit by unit above: each unit keeps its study and
demonstration, rehearsal with the critique and the revision, the showing check, a separate teacher's-table check and
a respond session, with Fluency days folded into the openers. Sessions: year K 8, 8, 7, 5; year 1 7, 9, 7, 5; year 2
8, 8, 7, 5 (the frame's counts, rebalanced in this fix so a making day keeps a session of its own and no session
carries more than about three teaching days); each year's two course-level checks keep 1 check session and 1 respond
session, in weeks 17 and 26 in every year, each respond session a week later. Year K's week 17 session sits inside the
kindergarten core weeks 14 to 18, which CALENDAR.md rule 1 allows for an arts special. A story unit's study session
holds only its study and teaching days; its acting, critique and revision come in session 2 with the kept story map. On this path the story units' showing check is
the family showing, with an in-class version for any child without a family yes.

**A shorter period** (30 to 35 minutes). Set-up drops to 2 minutes, the warm-up to 3, the close to 3. A showing day
still fits: at 30 minutes, six groups run about 3.5 minutes each (21) with set-up 2, self-check 3 and close 3, the
warm-up done in the line before entering; at 35 minutes they keep about 4 minutes (24). A teacher's-table day fits
the same way, units 6 and 10 included (about 21 minutes at the table at 30 minutes). A making day keeps its 6-minute
clean-up and loses about 7 minutes of making; the unit's making days (110, and 172 to 173) or the revision day take
the rest.

**A year about 10 days short, by named fold-in days.** About 10 school days short is about 4 sessions at two a
week, so each year names four fold-in days, one per unit; the rest are spares, folded in the order listed only when a
year runs shorter still. None of these days is assessed and no owned part is cut: each day's work folds into the
neighbor named, as its opener or a short segment. Baseline-look days, critique days, revision days, both check days,
respond days, family showings and the only teaching day of any id never fold.

| Year | Fold-in day | Folds into | Saves |
|---|---|---|---|
| K | 7 (place-walk practice) | 8, as the opener | 35 minutes |
| K | 24 (sound cues) | 25, as the opener | 35 |
| K | 29 (cue drill) | 30, as the opener | 35 |
| K | 46 (puppet scene run) | 47, as the opener | 35 |
| 1 | 73 (slow-motion and strip run) | 74, as the opener | 35 |
| 1 | 86 (mirror-game rounds) | 85, a 10-minute segment | 30 |
| 1 | 95 (scene beats) | 96, as the opener | 35 |
| 1 | 99 (last rehearsal) | 98, the compare-card practice | 30 |
| 2 | 136 (line-and-reply pairs) | 137, as the opener | 35 |
| 2 | 151 (drill run) | 152, as the opener | 35 |
| 2 | 168 (object rounds) | 167, a 10-minute segment | 30 |
| 2 | 175 (cue run in the set) | 176, as the opener | 35 |

Spares, in order: year K 10 (into 11, opener, 35), 12 (into 13, opener, 35), 15 (into 14, the self-check practice,
30), 27 (into 28, opener, 35), 33 (into 32, the audience card practice, 30), 43 (into 45, opener after day 44's
two-ties teaching, 35); year 1 74 (into 75, the critique rehearsal, 30), 93 (into 94, opener, 35), 96 (into 97, the
critique rehearsal, 30), 89 (into 90, a 15-minute drama before the choices are remembered, 25), 70 (into 69, a
15-minute guided Turnip segment that uses the gestures just taught, 25), 87 (into 88, a 15-minute segment, 25); year 2
138 (into 139, the critique rehearsal, 30), 171 (into 172, its first 15 minutes, where the set plan is drawn, 25), 174
(into 176, the critique rehearsal, 30), 149 (into 150, a 10-minute segment, 30), 155 (into 156, the critique
rehearsal, 30), 133 (into 134, a 15-minute segment, 25). Day 95 folds into 97 when 96 folds too, and 73 into 75 when 74
does.

Total: the four named days save 140 minutes in year K, 130 in year 1 and 135 in year 2 (four sessions), leaving 60 of
the frame's 64 sessions a year; with every spare folded too, 340, 300 and 305 minutes, leaving 54.

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week (one on the once-a-week path); a clear floor; step cards, scene cards, audience cards; found and low-cost materials; a teacher with no drama training, led by each unit's teacher page | The voice and body taught in steps; tales and works heard or watched with their setting; guided drama and rehearsal with a critique and a revision; a showing each unit | A portfolio folder of 12 pieces over the band, each with a spoken reflection; 12 showings, three of them for families; two marks a unit per child on the main look-for | Met marks on the year's ids (17, 24, 24) and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result.

## For the lead

1. **Course-level check coverage (rule 3, later.csv L107).** The frame's checks sample 21 of the 65 ids; the other 44
   are named above with the reason (talk items, the unit just assessed, the story unit after the year-end check).
   Each is assessed id by id in its unit. If the lead wants more ids sampled, the frame's fix is a talk-free kept
   card on the year-end check for the third unit's ids (a prop-sketch or set-plan item), which the frame does not
   have now; this scope does not add it.
2. **school_day pattern.** Filled as the second and fourth school days of each week, counted on across the band (2
   to 479). data/plans/calendar.csv still holds frame.py's even spread; `frame.py calendar` at commit brings it in line
   (the weeks already agree).
3. **Four processes.** Settled by the lead (2026-11-26): each year carries all four, each unit at least those its
   frame row names; no claim was stretched. Closed.
4. **Browser checks for the unit plans** (from the frame fix review): the Skeat mouse-deer telling (unit 4), Rizal's
   1889 text (unit 9), a public archive page for Marceau's The Mask Maker (unit 10) and the UNESCO Karagöz page (unit
   11). The unit 12 third race telling is new here and needs its rights line.
5. **Once-a-week grade 2 mid-year respond session** in week 18 beside the grade 2 math mid-year check: closed, no
   change. CALENDAR.md rule 1: arts specials do not count against the classroom teacher's stagger. The same rule
   covers year K's once-a-week check session in week 17, inside the kindergarten core weeks.
6. **Theater-maker revisits in units 5 and 9** (expert read finding 11, optional): applied at no day (day 68 names
   kamishibai again as a real form; day 129 adds one line on a living Panchatantra storyteller or company, picked by
   the unit plan with its rights line). The lead may strike them.
