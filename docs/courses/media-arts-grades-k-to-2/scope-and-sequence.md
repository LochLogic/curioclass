# Scope and sequence: Media Arts, grades K to 2

Course `media-arts-grades-k-to-2`, a band course for kindergarten, grade 1 and grade 2; draft, written 2026-11-26 from the frame (docs/courses/media-arts-grades-k-to-2/frame.md). The days are in data/plans/media-arts-grades-k-to-2/days.csv.

## How the band runs

- **Three years, one after another.** Year K is course days 1 to 64, year 1 days 65 to 128, year 2 days 129 to 192.
  Each year has four units (18, 22, 10 and 10 days), a mid-year course-level check with its respond day after the
  second unit, and a year-end course-level check with its respond day after the fourth unit: 60 unit days and 4
  course-level days a year. `stretch` is the unit number in the frame's Units table (1 to 12), or `C`.
- **Which grade's standards fall in which year** (National Core Arts Standards, 2014, media arts, by id only, each
  action from its line in data/standards/ncas-performance-standards-words.txt). Year K (units 1 to 4) claims only
  the 18 kindergarten ids, year 1 (units 5 to 8) only the 18 grade 1 ids, year 2 (units 9 to 12) only the 18 grade 2
  ids: 54 in all, the count in docs/courses/arts/STANDARD.md 3.2, and every one is on a teaching day and an
  assessment day of its own year in days.csv. A year revisits the year before's ids only as practice that returns,
  never as a claim. No pre-kindergarten id is claimed.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a child's record shows which grade's standards they met. In a mixed class a
  child may meet year 2 before year 1, so every retrieval task below carries its ten-minute reteach as written.
- **Meeting days and `school_day`.** Two 40-minute sessions a week, 32 weeks a year (96 weeks over the band). Course
  day n of a year (n = 1 to 64) falls in that year's week ceil(n / 2): the odd day on the week's second school day,
  the even day on its fourth. So `school_day` = 160 x (year index, 0 for K, 1 for grade 1, 2 for grade 2) +
  5 x (week - 1) + 2 for an odd day, or + 4 for an even day; each year's 160 school days are the CALENDAR.md year
  for that grade, and scripts/frame.py reads each year onto its own grade's calendar. `school_day` counts across the
  whole band (year K 1 to 160, year 1 161 to 320, year 2 321 to 480), as frame.py reads it; a filled `school_day`
  wins over frame.py's even spread, and calendar.csv is regenerated from it. The band week is
  (school_day - 1) // 5 + 1 (1 to 96), and the week of the year is that less 32 for each earlier year: every unit and
  every check sits in the frame's weeks by this formula (checked by script, 2026-11-26 fix pass). A school may pick
  any two days of the week; the weeks stay.
- **Weeks every year.** First unit weeks 1 to 9; second unit weeks 10 to 20; mid-year check and respond week 21;
  third unit weeks 22 to 26; screening unit weeks 27 to 31; year-end check and respond week 32.
- **The session.** Set-up about 5 minutes (devices and trays out), clean-up, hand-back of devices and collecting work
  about 5 (7 in a cutting and gluing session); a retrieval task takes ten minutes of the opener. The minutes of a
  talk check day, a screening check day and a course-level check day are written in those days' notes.
- **Kinds of day.** Understanding: a technique shown in named steps with the step card, or a work studied with the
  unit's words (the artistic process "responding" is taught here, never on a respond day). Fluency: short repeated
  drills of a taught technique with feedback. Application: making, rehearsing and showing with some choice; the
  unit's critique sits on a making day and the next day's revision is application too. Check: the end-of-unit
  assessment days and the course-level check days. Respond: a second try at what was marked not yet.
- **Assessment slots.** `end` marks the end-of-unit check days. `observe` marks the unit's last three making days,
  where the rotating look-fors are marked at the tray (ten children a day, about a minute and a half each, on a class
  list) and any second talk item is heard, so no child answers two talk items on one day; these are part of the
  end-of-unit evidence the frame names id by id. `course` marks the course-level check days. Each unit opens with a
  baseline look at its main look-for on its first practice day (a recorded mark, never a score), so every child has
  two marks a unit and the growth is the change. No score comes from the day a technique is first taught. Each
  unit's response time is its respond day (the unit's last day). No unit is over 25 days, so none has a mid-unit
  assessment.
- **The four processes** (create; perform, present or produce; respond; connect). Each year carries all four, and
  each unit touches at least the processes its frame row names; the unit's "Processes" line lists the days whose
  note names each one. A unit need not claim an id of every process: where a unit practices a process outside its
  owned rows (a setting card, a short response, a partner line), the day practices it and claims no id. No day
  claims an id outside its unit's owned rows.
- **Showing, critique, revision.** Every unit has a critique day (the describe, ask, suggest routine: the teacher
  models it in units 1 and 2, the children hold the critique card from unit 3 on), a revision day after it, and a
  showing before or as its end-of-unit assessment. One piece a unit goes into the portfolio folder on the respond day,
  with a one-line spoken reflection.
- **Equipment and safe use** are named in the notes of the days that use them, in the frame's words; every day has a
  paper path (step cards, work cards, paper media tools, found objects) and no student account. A shared school
  device, where there is one, is one way in, never the only one.
- **Sensitivity.** Every day that studies a flagged work, or ties media to a child's own life, names the flag in its
  note. Every task tied to a child's own life offers a story-character, invented or class-shared option marked the
  same, and no task asks what a family watches, owns or posts.

### Readiness and retrieval (rule 2, counted by grade number)

Year K assumes no earlier media arts learning (its eight rows have empty `assumes` cells; no pre-kindergarten id is
taught), so no year K unit has a readiness check. Every year 1 and year 2 row assumes the year before's row in its
thread, last used one grade back, so each such unit opens with a retrieval task inside day 2's opener (the day's
`retrieves` column), never a readiness check, and day 1 stays clean for the hook. No row of this band assumes a row
two grades back, so no readiness check is owed anywhere in the band.

| Unit (day 2) | Earlier rows retrieved | Last used |
|---|---|---|
| 5 (day 66) | ma-k-read; ma-k-society | grade K, unit 1 |
| 6 (day 84) | ma-k-ideas; ma-k-craft | grade K, unit 2 |
| 7 (day 108) | ma-k-make; ma-k-judge | grade K, unit 3 |
| 8 (day 118) | ma-k-present; ma-k-sources | grade K, unit 4 |
| 9 (day 130) | ma-g1-read; ma-g1-society | grade 1, unit 5 |
| 10 (day 148) | ma-g1-ideas; ma-g1-craft | grade 1, unit 6 |
| 11 (day 172) | ma-g1-make; ma-g1-judge | grade 1, unit 7 |
| 12 (day 182) | ma-g1-present; ma-g1-sources | grade 1, unit 8 |

Inside year K, three units also open a same-year retrieval of a tool or plan they build on: day 20 (ma-k-society,
the media rules card before the flashlight), day 44 (ma-k-ideas, the storyboard before the paper stage) and day 54
(ma-k-ideas, before the film strip). Years 1 and 2 do the same where a unit builds on a row of the same year, each a
five-minute warm-up in the day's opener (the cross-year retrievals stay ten minutes, rule 2): day 86 (ma-g1-read, far, middle and close shots before the order practice), day
109 (ma-g1-ideas, pages in order before the six frames), day 156 (ma-g2-society, turns and the credit line before the
first team try) and day 173 (ma-g2-craft, the recorded or shaped sound that goes into the whole).

### Logic model (the frame's, on one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; step cards, work cards, paper media tools, found objects; an optional shared device | Technique taught in steps; works studied with their setting; making with a critique and a revision; a showing or screening each unit | A portfolio folder of 12 pieces over the band with reflections; 12 showings; two marks a unit per child on the main look-for | Met marks on the year's 18 ids and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that media arts study raises any other
result.

## Year K (kindergarten ids, 18)

### Unit 1: Media all around us (days 1 to 18, weeks 1 to 9)

Owns ma-k-read and ma-k-society (MA:Re7.1.Ka, MA:Re7.1.Kb, MA:Cn11.1.Ka, MA:Cn11.1.Kb). The year opens with the media
rules card and the set-up and hand-back routine (day 1), because every later tool day needs them, then looking and
listening come before making: Muybridge's running horse (day 2), the card viewfinder (day 3), Keïta's studio portraits
(day 5), the listening walk and sound map (day 6) and Westerkamp's soundwalk, which gives the first "two pieces feel
different" comparison (day 7). Media in a day (day 9) leads to the media-hunt walk (day 10) and the kept "media in a
day" drawing (day 12). The teacher models describe, ask, suggest on day 13 (the critique), the class revises (day 14)
and shows the "media in our school" wall (day 15).

- Processes (from the day notes): create days 3, 4, 10, 12 to 14; produce or present day 15; respond days 2, 5 to 8,
  13, 15, 16; connect days 1, 2, 5, 7, 9 to 12.
- Assessments: rotation (`observe`) days 13 to 15: MA:Cn11.1.Kb safe, polite handling and one rule, and the
  MA:Re7.1.Kb talk item. End day 17: the MA:Re7.1.Ka talk item, and the kept drawing for MA:Cn11.1.Ka scored after the
  session. Respond day 18.
- Candidate (criterion 9, device set-up and hand-back minutes): kept, no day added. Day 1 times the routine (5 and 5
  minutes) and every later day counts it inside its 40 minutes.

### Unit 2: Playing with light and shadow (days 19 to 40, weeks 10 to 20)

Owns ma-k-ideas and ma-k-craft (MA:Cr1.1.K, MA:Cr2.1.K, MA:Pr5.1.Ka, MA:Pr5.1.Kb, MA:Pr5.1.Kc). The longest
kindergarten unit: five ids, two techniques and the first partner work. Reiniger's flying horse opens it (day 19);
shadow play with the flashlight is shown after the tool rules are retrieved (day 20); play with tools until an idea
turns up comes next (day 21, with shapes pre-cut by an adult; children cut their own from day 23), then the light
explored (day 22, what a tool taught), the silhouette cutout (day 23), McLaren and Lambart's painted film and a
second play try (days 25 and 26; day 26 also tells one thing the crayon strip taught, the practice MA:Pr5.1.Kc gets
before its talk item on day 39). The storyboard is taught (day 27),
practiced (day 28) and made (day 29) before partner roles (day 30), rehearsal (days 31 and 32), the feedback day
(day 33) and the revision (day 34). Kept idea pages and storyboards are finished on day 36.

- Processes (from the day notes): create days 21, 23, 26 to 29, 32, 36; produce or present days 20, 22 to 24, 26, 30
  to 35, 37, 38; respond days 19, 22, 25, 33; connect days 19, 25.
- Assessments: two end days. Day 38, the shadow screening (MA:Pr5.1.Ka, MA:Pr5.1.Kb marked at the screen; the kept
  idea page for MA:Cr1.1.K and storyboard for MA:Cr2.1.K scored after the session). Day 39, the MA:Pr5.1.Kc talk item.
  Respond day 40. No rotating look-for in this unit (none of its ids is a rotation item).
- Candidate (a doubled parent-and-child version of the partner piece): kept, no day added, on day 30's step card.

### Mid-year course-level check (days 41 and 42, week 21)

See "Course-level checks" below.

### Unit 3: Make it, change it (days 43 to 52, weeks 22 to 26)

Owns ma-k-make and ma-k-judge (MA:Cr3.1.Ka, MA:Cr3.1.Kb, MA:Re8.1.K, MA:Re9.1.K). Short because the plan, the framing
and the tool skills are built. The lianhuanhua picture-story books open it (day 43); the paper stage is shown after
the storyboard is retrieved (day 44); the three-card story is made (day 45); Atkins's algae prints teach "the same
thing, laid out differently" and the before-and-after card (day 46); the critique card goes to the children (day 47)
and they use it (day 48), revise (day 49) and tell both versions to a partner class (day 50).

- Processes (from the day notes): create days 44 to 46, 48, 49; produce or present days 44, 50; respond days 43, 46 to
  48, 50; connect days 43, 46, 47.
- Assessments: rotation days 48 to 50 (the MA:Re8.1.K talk item). End day 51: the MA:Re9.1.K talk item, and the kept
  three cards (MA:Cr3.1.Ka) and before-and-after card (MA:Cr3.1.Kb) scored after the session. Respond day 52.
- Candidate (a second picture-sequence form from Africa or the Americas): kept, no day added. It is the practice
  piece for the critique card on day 47: a picture sequence by a living maker from Africa or the Americas, described
  and linked, since year K's works are otherwise thin on living makers (APPROACH, bar item 7). The unit plan picks
  it, records its rights line and whether the maker is living as of its date, and checks every arts frame for a
  repeat.

### Unit 4: Our class screening (days 53 to 62, weeks 27 to 31)

Owns ma-k-present and ma-k-sources (MA:Pr4.1.K, MA:Pr6.1.Ka, MA:Pr6.1.Kb, MA:Cn10.1.Ka, MA:Cn10.1.Kb). Ruttmann's
painted shapes moving to music open it with a remembered media moment (day 53); the pull-through film strip and what
goes on it (day 54); McLaren's Pas de deux and the class movement (day 55); the screening-plan card and how to tell
how a showing felt (day 56). The strips are drawn (day 57), critiqued in rehearsal (day 58) and revised, with the
screening-plan card filled (day 59). The screening for families is the end-of-unit assessment.

- Processes (from the day notes): create days 55, 57 to 59; produce or present days 54, 56, 58 to 60; respond days 53,
  55, 56, 61; connect days 53 to 55, 57.
- Assessments: rotation days 57 to 59 (the MA:Cn10.1.Kb talk item). End day 60, the screening (MA:Pr4.1.K; kept strip
  for MA:Cn10.1.Ka and screening-plan card for MA:Pr6.1.Ka scored after the session). End day 61, the MA:Pr6.1.Kb talk
  item. Respond day 62.
- Candidate (the found-sound track as the full equal of the movement version): kept, no day added; days 55 and 58
  carry both versions, and the leave-out note names it.

### Year-end course-level check (days 63 and 64, week 32)

See "Course-level checks" below.

## Year 1 (grade 1 ids, 18)

### Unit 5: Media that links people (days 65 to 82, weeks 1 to 9)

Owns ma-g1-read and ma-g1-society (MA:Re7.1.1a, MA:Re7.1.1b, MA:Cn11.1.1a, MA:Cn11.1.1b). Reopens the tools and rules
after the summer and moves the looking from parts to contents and messages. The hook (day 65) stays clean; day 66
studies the Lumière family breakfast with the kindergarten retrieval in its opener; far, middle and close shots are
taught (day 67) and practiced (day 68) before Poolaw's Kiowa family photographs (day 69) and the still against moving
comparison (day 70). Media links (day 72) and the class media rules written together (day 73) lead to the three-frame
drawings (day 75) and the kept link drawing (day 76), the critique (day 77), revision (day 78) and the wall (day 79).

- Processes (from the day notes): create days 67, 68, 75 to 78; produce or present day 79; respond days 66, 69 to 71,
  77, 79, 80; connect days 65, 66, 69, 72 to 76.
- Assessments: rotation days 77 to 79 (MA:Cn11.1.1b in use and the MA:Re7.1.1b talk item). End day 81: the
  MA:Re7.1.1a talk item, and the kept link drawing for MA:Cn11.1.1a. Respond day 82.
- Candidate (a third family-life photograph by a living maker from Asia or Africa): dropped here. Year 1's Africa is
  Ojeikere (unit 7); its missing Asia is filled in unit 6, where the work fits the animation study, and unit 5 keeps
  its two works for the still and moving comparison.

### Unit 6: Pictures in order (days 83 to 104, weeks 10 to 20)

Owns ma-g1-ideas and ma-g1-craft (MA:Cr1.1.1, MA:Cr2.1.1, MA:Pr5.1.1a, MA:Pr5.1.1b, MA:Pr5.1.1c). Cohl's line-drawing
film opens it (day 83); three sketches in order are taught with the kindergarten retrieval (day 84), made (day 85) and
practiced with unit 5's shots (day 86). Linnett's kineograph (day 87) leads to the flip book taught (day 88), drilled
(day 89) and built as the mockup (day 90). Roles come next (days 91 and 92), then varied uses of a tool (days 93 and
94), then changing up a technique (days 95 and 96), team making (days 97 and 98), the critique (day 99), revision (day
100), finishing (day 101) and the showing to a partner class (day 102).

- Processes (from the day notes): create days 84 to 86, 88 to 90, 92, 95 to 97, 100, 101; produce or present days 91
  to 94, 97 to 100, 102; respond days 83, 87, 93, 95, 99, 102; connect days 83, 87.
- Assessments: rotation days 99 to 101 (MA:Pr5.1.1c: the varied use shown to a tablemate, and what it found told,
  while the teacher watches and marks). End day 103: the MA:Pr5.1.1a talk item with the role card, and
  the kept sketch page (MA:Cr1.1.1), mockup (MA:Cr2.1.1) and two flip books (MA:Pr5.1.1b) scored after the session.
  Respond day 104.
- Candidate (an animated work by a living maker from Africa or Asia): kept, ten minutes of day 95, no day added; the
  unit plan picks a maker from Asia (year 1 has no Asian work otherwise), records the rights line and checks every arts
  frame for a repeat.

### Mid-year course-level check (days 105 and 106, week 21)

### Unit 7: Patterns that repeat (days 107 to 116, weeks 22 to 26)

Owns ma-g1-make and ma-g1-judge (MA:Cr3.1.1a, MA:Cr3.1.1b, MA:Re8.1.1, MA:Re9.1.1). The Bechers' water towers open it
(day 107); the six-frame strip with a repeat is taught after the kindergarten retrieval (day 108) and made (day 109);
Ojeikere's Hairstyles and the before-and-after card come next (day 110), then the part that works best for viewers
(day 111), the critique (day 112), revision (day 113) and the showing (day 114).

- Processes (from the day notes): create days 108 to 110, 112, 113; produce or present day 114; respond days 107, 110
  to 112, 114; connect days 107, 110.
- Assessments: rotation days 112 to 114 (the MA:Re8.1.1 talk item). End day 115: the MA:Re9.1.1 talk item, the kept
  strip (MA:Cr3.1.1a) and before-and-after card (MA:Cr3.1.1b). Respond day 116.
- Candidate (a pattern-based piece by a living maker from Asia or the Americas): dropped. The Asia gap is filled in
  unit 6, the year's living makers of the Americas are Morales and Tonatiuh (unit 8), and the ten-day unit has no
  spare time.

### Unit 8: A picture-book tale (days 117 to 126, weeks 27 to 31)

Owns ma-g1-present and ma-g1-sources (MA:Pr4.1.1, MA:Pr6.1.1a, MA:Pr6.1.1b, MA:Cn10.1.1a, MA:Cn10.1.1b). Morales's
Viva Frida opens it with a meaningful media experience shared, as units 4 and 12 open (day 117); the sound on cue at
a page turn is taught after the kindergarten retrieval (day 118); Tonatiuh's Dear Primo and what he drew on, an
interest and an example (day 119); showing conditions and one task (day 120). The tales
are made (day 121), critiqued in rehearsal (day 122) and revised with the screening-plan card (day 123).

- Processes (from the day notes): create day 121 to 123; produce or present days 118, 120, 122 to 124; respond days
  117, 119, 120, 125; connect days 117, 119, 121.
- Assessments: rotation days 121 to 123 (the MA:Cn10.1.1b talk item). End day 124, the showing for families
  (MA:Pr4.1.1, MA:Pr6.1.1a with its kept card, MA:Cn10.1.1a with the tale and source card). End day 125, the MA:Pr6.1.1b
  talk item. Respond day 126.
- Candidate (a quiet visual cue card for a child sensitive to noise): kept, no day added, on day 118's step card.

### Year-end course-level check (days 127 and 128, week 32)

See "Course-level checks" below.

## Year 2 (grade 2 ids, 18)

### Unit 9: Media messages (days 129 to 146, weeks 1 to 9)

Owns ma-g2-read and ma-g2-society (MA:Re7.1.2a, MA:Re7.1.2b, MA:Cn11.1.2a, MA:Cn11.1.2b). Group project rules and the
credit line come first (day 129), since the unit's making is a group poster. WPA posters (day 130, grade 1 retrieval
in the opener), the one-message poster technique (day 131) and its drill (day 132) come before Red Star's Four Seasons
and the first comparison of experiences (day 133), and before what a media message is and how media fits cultural life
(day 134). Credit is taught in one short step (day 136) and practiced (day 137); groups plan (day 138), make (day 139)
and fill the kept poster card (day 140), then critique (day 141), revise (day 142) and hang the posters in the hall
(day 143).

- Processes (from the day notes): create days 131, 132, 138 to 142; produce or present day 143; respond days 130, 132
  to 135, 141, 143, 144; connect days 129, 130, 133, 134, 136 to 138, 140.
- Assessments: rotation days 141 to 143 (MA:Cn11.1.2b in use and the MA:Re7.1.2b talk item). End day 145: the
  MA:Re7.1.2a talk item and the kept poster card (MA:Cn11.1.2a). Respond day 146.
- Candidate (a media message piece by a maker from Africa or Asia): kept, ten minutes of day 134, no day added; the
  unit plan picks a maker from Africa (year 2 has Asian works in units 10, 11 and 12 and no African one otherwise).

### Unit 10: Many ideas, one piece (days 147 to 168, weeks 10 to 20)

Owns ma-g2-ideas and ma-g2-craft (MA:Cr1.1.2, MA:Cr2.1.2, MA:Pr5.1.2a, MA:Pr5.1.2b, MA:Pr5.1.2c). Rao's Printed
Rainbow opens it (day 147); brainstorming and improvising (day 148, grade 1 retrieval) and the brainstorm page (day
149) come before choosing one idea and its storyboard and mockup (days 150 and 151). Reynaud's hand-shown band (day
152) leads to stop-motion taught (day 153) and drilled (day 154), roles (day 155), a first try (day 156), trying again
(days 157 and 158), the shaped sound or sound score (days 159 and 160), production (days 161 and 162), the critique
(day 163), revision (day 164), finishing (day 165) and the showing (day 166).

- Processes (from the day notes): create days 148 to 151, 156, 158, 161, 162, 165; produce or present day 153 to 166;
  respond days 147, 152, 157, 163, 166; connect days 147, 152.
- Assessments: rotation days 163 to 165 (MA:Pr5.1.2a seen done; MA:Pr5.1.2c one recording method, move, capture,
  move, and one shaping move, a sound made louder, softer or given a longer pause, each shown on the device or the
  sound score and named; all in one visit). End day 167: the
  role reflection with the role card (MA:Pr5.1.2a), and the kept brainstorm page (MA:Cr1.1.2), storyboard and mockup
  (MA:Cr2.1.2) and first and second tries (MA:Pr5.1.2b) scored after the session. Respond day 168.
- Candidate (a living stop-motion maker from Africa or the Americas): dropped. Year 2's Africa is filled in unit 9,
  Rao is a living maker, and the unit's two works carry its ids.

### Mid-year course-level check (days 169 and 170, week 21)

### Unit 11: Putting it together (days 171 to 180, weeks 22 to 26)

Owns ma-g2-make and ma-g2-judge (MA:Cr3.1.2a, MA:Cr3.1.2b, MA:Re8.1.2, MA:Re9.1.2). Paik's Electronic Superhighway, by
a still photograph only, opens it (day 171); placement for attention is taught after the grade 1 retrieval (day 172)
and used (day 173); Villareal's Bay Lights and the before-and-after card (day 174); how well a piece works where it is
seen (day 175); the critique (day 176), revision (day 177) and each piece shown in its chosen place (day 178).

- Processes (from the day notes): create days 172 to 174, 176, 177; produce or present day 178; respond days 171, 174
  to 176, 178; connect days 171, 174.
- Assessments: rotation days 176 to 178 (the MA:Re8.1.2 talk item). End day 179: the MA:Re9.1.2 talk item, the kept
  whole (MA:Cr3.1.2a) and before-and-after card (MA:Cr3.1.2b). Respond day 180.
- Candidate (a whole for a public place by a living maker from Africa or the Americas): dropped. Villareal's Bay Lights
  is already that (a living maker of the Americas, a public place), and Africa is in unit 9.

### Unit 12: Our narrated picture scroll (days 181 to 190, weeks 27 to 31)

Owns ma-g2-present and ma-g2-sources (MA:Pr4.1.2, MA:Pr6.1.2a, MA:Pr6.1.2b, MA:Cn10.1.2a, MA:Cn10.1.2b). McCay's Gertie
opens it with a media experience and what it was for (day 181); a patua scroll and the picture-scroll technique follow
the grade 1 retrieval (day 182); sources, credit and the tale choice (day 183); showing conditions (day 184). The scroll
is made (day 185), critiqued in rehearsal (day 186) and revised with the screening-plan card (day 187). The year-end
scroll screening for families is the band's last end-of-unit assessment. Day 182 holds a retrieval, a flagged
work and a step card, so the unit plan times it to the minute; if it runs over, the step card moves to the first
half of day 184 and the conditions take its second half. On the first making day of each screening unit (days 57,
121 and 185) the baseline is a glance mark made while walking the tables, and the tray rotation starts after it.

- Processes (from the day notes): create days 183, 185 to 187; produce or present days 182, 184, 186 to 188; respond
  days 181, 182, 184, 189; connect days 181 to 183, 185.
- Assessments: rotation days 185 to 187 (the MA:Cn10.1.2b talk item). End day 188, the screening (MA:Pr4.1.2,
  MA:Pr6.1.2a with its kept card, MA:Cn10.1.2a with the source card: three picture boxes, I know, I like, I read,
  and an example line; met = the "I read" box, one of the other two and the example). End day 189, the MA:Pr6.1.2b talk item. Respond
  day 190.
- Candidate (a public domain or openly licensed tale collection from more than one region): kept, no day added; the
  tales are chosen from it on day 183.

### Year-end course-level check (days 191 and 192, week 32)

See "Course-level checks" below.

## Course-level checks

Each check day runs as the frame's talk check day: one fresh table task every child does and keeps, and one talk item
a child in six groups of five. Each check draws its items from earlier units, never the unit just assessed, and no
artifact is scored twice (collect once). Marks are in before the
respond day. Arts are specials in K to 2, so these weeks do not count against the classroom teacher's stagger
(CALENDAR.md rule 1); they sit on the frame's weeks, off every core check week of each grade.

| Check | Days (week) | Samples | Record carried unscored |
|---|---|---|---|
| Year K mid-year | 41, respond 42 (week 21) | MA:Cn11.1.Kb (safe-use picture sort: knowing the rule), MA:Re7.1.Ka (talk), both unit 1 | Unit 2 (days 38 and 39) |
| Year K year-end | 63, respond 64 (week 32) | MA:Cr2.1.K (three-box plan, unit 2), MA:Re7.1.Kb (talk, unit 1) | Unit 3 (day 51) |
| Year 1 mid-year | 105, respond 106 (week 21) | MA:Cn11.1.1b (fair-turn sort: knowing the rule), MA:Re7.1.1a (talk), both unit 5 | Unit 6 (day 103) |
| Year 1 year-end | 127, respond 128 (week 32) | MA:Cr1.1.1 (three sketches, one folded into a stand-up paper model, unit 6), MA:Cn11.1.1a (talk, unit 5) | Unit 7 (day 115) |
| Year 2 mid-year | 169, respond 170 (week 21) | MA:Cn11.1.2b (one-message card with credit: knowing the rule), MA:Re7.1.2a (talk), both unit 9 | Unit 10 (day 167) |
| Year 2 year-end | 191, respond 192 (week 32) | MA:Cr2.1.2 (three ideas as the input, the chosen storyboard folded into a stand-up mockup, unit 10), MA:Re7.1.2b (talk, unit 9) | Unit 11 (day 179) |

**Codes not sampled on a course-level check, and why** (rule 3). The frame's check design samples 12 of the 54 ids:
each check has one table task and one talk item a child in 40 minutes. The other 42 are assessed only in their own
units, for these reasons:

- Units 4, 8 and 12 (MA:Pr4.1.K, Pr6.1.Ka, Pr6.1.Kb, Cn10.1.Ka, Cn10.1.Kb; MA:Pr4.1.1, Pr6.1.1a, Pr6.1.1b, Cn10.1.1a,
  Cn10.1.1b; MA:Pr4.1.2, Pr6.1.2a, Pr6.1.2b, Cn10.1.2a, Cn10.1.2b): the screening unit is the unit just before the
  year-end check of week 32 (lead structure pass, 2026-11-26), so by rule that check does not draw from it; the
  screening is their own assessment.
- Units 3, 7 and 11 (MA:Cr3.1.Ka, Cr3.1.Kb, Re8.1.K, Re9.1.K; MA:Cr3.1.1a, Cr3.1.1b, Re8.1.1, Re9.1.1; MA:Cr3.1.2a,
  Cr3.1.2b, Re8.1.2, Re9.1.2): since the year-end check moved to week 32 these units are no longer the unit just
  before it, but its items were kept as written (each day keeps its content and codes); sampling the third unit's
  judge row there is open (For the lead item 1).
- The shadow, flip-book and stop-motion production ids (MA:Pr5.1.Ka, Kb, Kc; MA:Pr5.1.1a, 1b, 1c; MA:Pr5.1.2a, 2b,
  2c) and MA:Cr1.1.K, MA:Cr2.1.1: performed or made in the unit just before the mid-year check and carried unscored, and
  a fresh production task does not fit a 40-minute talk check day beside six talk groups.
- MA:Cr1.1.2 (unit 10, "brainstorming and improvising"): a paper table task cannot show improvising, so on day 191
  the three ideas are only the input to choosing; the id stays assessed on unit 10's brainstorm page.
- MA:Cn11.1.Ka (unit 1), MA:Re7.1.1b (unit 5) and MA:Cn11.1.2a (unit 9): each year's checks already sample two other
  ids of that unit; one talk item a child per check day leaves no room for a third.

The safe-use ids (MA:Cn11.1.Kb, 1b and 2b) are rotation items, never an end-of-unit check day item. A course-level
check samples knowing the rule by a fresh paper task (the picture sort or the credit card); the use itself stays
assessed at the unit's tray rotation. For the lead item 1 asks whether to widen the year-end
checks.

## Leans and the calendar

No media arts row of grades K to 2 carries a `cross_subject` lean, so no day waits on another course. The contacts
are practiced, not owned: first, next and last on the storyboard (day 27) come after math kindergarten unit 1 (days 1
to 18) has counted small sets, and no counting past three is asked; the repeat in unit 7 is found by looking, never by
counting rules (day 108); the critique practices collaborative conversation (SL.K.1, SL.1.1, SL.2.1), and days 13 and
47 carry the frame's bridge (the turn-taking rules shown in pictures and modeled) in case ELA has not yet taught them.
Social studies grade 2 unit 6 ("Family stories and culture") sits near unit 9; the art unit teaches its own setting on
work cards and never asks a child to explain their family's culture. Credit and asking before a picture are taught in
short steps here (days 1, 73, 129, 136, 183) and do not wait for computer science.

## Shorter path

**The once-a-week path** (32 sessions a year, the frame's path). Every unit and every id is kept by merging days; a
merged day never drops a critique, a revision, a showing, a check or a respond session, and fluency days fold into the
openers. Positions are the unit's own days (1 is its first day):

| Unit shape | Sessions | Days merged, by position in the unit |
|---|---|---|
| 18-day first unit (units 1, 5, 9) | 8 | S1 1 to 3 (hook, first study, first technique); S2 4 to 6; S3 7 to 9; S4 10 to 12; S5 13 (making with the critique); S6 14 and 15 (revision and showing); S7 16 and 17 (check, the practice in its opener); S8 18 (respond) |
| 22-day second unit, two check days (unit 2) | 9 | S1 1 and 2; S2 3 and 4; S3 5 to 8; S4 9 to 11; S5 12 to 15 (making with the critique); S6 16 to 19 (revision and finish); S7 20 (screening); S8 21 (talk check); S9 22 (respond) |
| 22-day second unit, one check day (units 6, 10) | 9 | S1 1 to 3; S2 4 to 6; S3 7 to 9; S4 10 to 12; S5 13 to 16; S6 17 (making with the critique); S7 18 to 20 (revision, finish, showing); S8 21 (check); S9 22 (respond) |
| 10-day third unit (units 3, 7, 11) | 5 | S1 1, 2 and 4 (studies and technique); S2 3, 5 and 6 (making with the critique); S3 7 and 8 (revision and showing); S4 9 (check); S5 10 (respond) |
| 10-day screening unit (units 4, 8, 12) | 6 | S1 1 and 2 (the hook study and the technique); S2 3, 5 and 6 (the second study as the opener, making, the critique); S3 4 and 7 (the plan card or conditions taught at the start of the revision session, then filled); S4 8 (screening, check 1; the card is scored after it, never in S3); S5 9 (talk check, check 2); S6 10 (respond) |
| Each course-level check | 2 | 1 check session, 1 respond session |

The rotating look-fors fall on the last two making sessions, fifteen children a session. The weeks are the frame's:
first unit weeks 1 to 8, second 9 to 17, the third unit's first three sessions weeks 18 to 20, mid-year check week 21
and respond week 22, the third unit's last two sessions weeks 23 and 24, the screening unit's six sessions weeks 25 to
30, year-end check week 31 and respond week 32 (as in media arts 6 to 8, the check session sits in week 31 on this
path because a once-a-week year has one session in week 32).

**A shorter session.** On a 30-minute period, set-up and clean-up stay, making time shrinks, and a talk check day moves
its self-check to the end of the day before, so the six talk groups still fit (5 + 21 + 4).

**A year about 10 school days short** (two weeks, four sessions of this course). Four fold-in days a year, each a
fluency day with nothing assessed and no owned part cut; each saves one 40-minute session, and ten minutes of its
practice move into the named later day's opener, so 30 minutes of teaching time are given up per fold-in. No
fold-in carries a unit's baseline look (days 68 and 132 keep theirs), and day 94's ten minutes go to day 97, since
day 95 is full.

| Year | Fold-in days (into the opener of) |
|---|---|
| K | 8 (9), 11 (12), 28 (29), 31 (32) |
| 1 | 71 (72), 74 (75), 86 (87, with its same-year retrieval), 94 (97) |
| 2 | 135 (136), 137 (138), 154 (155), 160 (161) |

Total: 12 fold-in days, 192 course days become 180 (60 a year), 120 minutes of teaching time given up a year. All the
fold-ins sit before the mid-year check, so on that path each check comes two weeks earlier in the school's own year;
arts are specials in K to 2, so this breaks no stagger rule.

## For the lead

1. **Rule 3 coverage (later.csv L107; expert read finding 4).** The frame's checks sample 12 of 54 ids (MA:Cr1.1.2
   left the year 2 year-end check in the 2026-11-26 fix pass); this scope names the other 42 and why. The year-end
   week is settled: the lead's structure pass (2026-11-26, option (a) of the media arts group read finding 1) moved
   each year-end check and its respond day to week 32, after the screening unit (days 63 and 64 of each year, the
   screening unit in weeks 27 to 31), and the once-a-week screening unit no longer pauses for a check. Each day kept
   its content and codes, so the checks still sample the same ids; widening them to the third unit's judge row
   (MA:Re8.1.K, 1, 2), as media arts 6 to 8 does, is left open.
2. **Candidate picks still owed by the unit plans:** a living maker's picture sequence from Africa or the Americas
   (unit 3, day 47), an animated work by a living maker from Asia (unit 6, day 95) and a media message piece by a
   maker from Africa (unit 9, day 134), each with its rights line and checked against every arts frame for a repeat.

The frame's "never a check day item" sentence and unit 10's "stop-motion and role record" (this file's earlier lead
items 2 and 3) were changed in the frame in the 2026-11-26 fix pass.
