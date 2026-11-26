# Scope and sequence: Music, grades 6 to 8

Course `music-grades-6-to-8` (catalog id `music-6-8`), a band course for grades 6, 7 and 8. Draft, written
2026-11-26 from docs/courses/music-grades-6-to-8/frame.md. The days live in data/plans/music-grades-6-to-8/days.csv;
this page holds the judgment.

## The band, the years and the standards

- **Three years in one file.** Year 6 is course days 1 to 64, year 7 days 65 to 128, year 8 days 129 to 192, run one
  after another. Each year has 60 unit days in four units (18, 18, 12, 12), one mid-year check day and one respond day
  (week 19), and one year-end check day and one respond day (week 32, the finals week).
- **Which grade's standards fall in which year (STANDARD.md 3.1).** Year 6 claims only the 21 grade 6 music ids
  (`MU:...6a`, `.6b`, `.6c`), year 7 only the 21 grade 7 ids, year 8 only the 21 grade 8 ids: 63 in all, the count in
  STANDARD.md 3.2. Every one of the 21 is on at least one teaching day and on its unit's end-of-unit assessment in its
  own year. A year brings back the year before's ids as practice, never as a claim. The connecting ids (`MU:Cn10.1`,
  `MU:Cn11.1`) carry one words line in every grade; each year meets them with its own music.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn; each year
  still claims only its grade's ids, so a student's record shows which grade's standards they met. In that case a
  student may meet year 8 before year 7, and each retrieval task keeps its reteach slot on the next day (UNIT-PLAN
  rule 6).
- **Meeting days and `school_day`.** The course meets two 40-minute sessions a week, 32 weeks a year, 96 weeks over
  the band. `school_day` is counted across the whole band, as frame.py reads it (CALENDAR.md's 160 school days a
  year, so year 7 starts at school day 161 and year 8 at 321). The formula, stated once: a year's course day k falls
  in week ceil(k / 2), on that week's second school day when k is odd and its fourth when k is even, so
  school_day = 160 (year - 1) + 5 (ceil(k / 2) - 1) + 2 or 4; read back, week = ((school_day - 1) mod 160) // 5 + 1.
  So course days 37 and 38 of each year are in week 19, day 61 in week 31, days 63 and 64 in week 32 (every unit and
  check checked against the frame's weeks, 2026-11-26). The filled school_day is what frame.py reads; calendar.csv
  is regenerated from it, so a one-day offset there is not re-counted here. A school may use any two days of the
  week; the weeks are what count.
- **The 40 minutes.** Set-up about 3 minutes, the warm-up opener (5), teaching and music making, clean-up and
  collecting about 3. A retrieval opener takes ten minutes of the day it sits in. A written sitting runs 38 minutes
  and a performance day 35 (frame, Scored evidence).
- **Base text.** None; every step card, lead sheet, work card and original take is Curio Class's own. No source map.

### The four processes

Each year claims all four artistic processes (creating, performing, responding, connecting), and each unit teaches
and assesses the processes it names in the frame. A unit need not claim all four. Where a unit's days also practice
a process it does not own (a two-bar ending, a works study as review, a one-line connection a student writes), that
practice costs no day and claims no id: no day carries a code outside its unit's owned rows (checked 2026-11-26).
In this course every unit in fact has days of all four, as practice where not claimed; the unit sections below
name the days. The arc is the same each year (frame "Day kinds"): technique
days (Understanding) come before the making that needs them, fluency drills follow, then rehearsal or composing,
the one critique on a rehearsal day, a revision day, the showing, the end-of-unit assessment and a respond day.

### Readiness and retrieval (rule 2)

Every row each unit assumes was last used one grade back, so the course has **no readiness check**; each unit opens
with a retrieval task in its second day's opener (`retrieves` in days.csv), and day 1 of every unit stays clean for
the hook and the compelling question.

| Unit | Assumed rows | Last used | Treatment |
|---|---|---|---|
| 1 | mu-g5-read, mu-g5-respond | grade 5 (Music 3 to 5 days 192 and 144) | retrieval, day 2; reteach slot day 3 |
| 2 | mu-g5-express, mu-g5-choose | grade 5 (days 158 and 144) | retrieval, day 20; reteach slot day 21 |
| 3 | mu-g5-invent, mu-g5-document | grade 5 (days 158 and 176) | retrieval, day 40; reteach slot day 41 |
| 4 | mu-g5-revise, mu-g5-perform | grade 5 (days 176 and 192) | retrieval, day 52; reteach slot day 53 |
| 5 to 8 | mu-g6 rows of the same threads | grade 6 (units 1 to 4) | retrieval, days 66, 84, 104, 116; reteach slots the next day |
| 9 to 12 | mu-g7 rows of the same threads | grade 7 (units 5 to 8) | retrieval, days 130, 148, 168, 180; reteach slots the next day |

Each retrieval opener gives five minutes a row. Any reteach (ten minutes per row missed) takes the next day's
warm-up and first five minutes, whole class if more than a third missed, otherwise a small group while the rest warm
up (UNIT-PLAN rule 6); that next day's note names the slot. Music 3 to 5 is not a core course, so a student may
arrive without it: the year 6 reteach is often whole class, and no unit depends on it. Rows used earlier the same year are retrieved inside the day that leans on
them: unit 1's symbols (mu-g6-read) on days 24 and 42, unit 3's score (mu-g6-document) on day 52, mu-g7-read on days
84, 106 and 119, mu-g7-document on day 116, mu-g8-read on days 148, 170 and 181 (samba's roots in Bahia from day 134, before "Sambalelê" is performed with
practice true to its culture), mu-g8-document on day 180.

### Leans on the calendar (rule 5)

- **ela:SL.6.1** (unit 1). ELA grade 6 unit 1 teaches its discussion routine in weeks 1 to 7; music's first listening
  talk is day 3 (week 2), so day 3 carries the frame's bridge: the music discussion card gives the routine and the
  teacher models it; nothing is scored as ELA.
- **ela:W.8.1** (units 9 and 10). ELA grade 8 unit 2 teaches argument writing in weeks 7 to 13; music's written
  judgment is taught on day 137 (week 5), so that day teaches the short form (claim, evidence heard, reason) with a
  frame and a model, scored on the music evidence only. Day 149 (week 11) uses the same frame for the backed reading.
- The music and math lean ended in grade 5: dotted notes and ties are read as music signs only.

### Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; step cards, lead sheets, staff paper, listening-log pages; found and low-cost instruments; one teacher device or none | Technique taught in steps; works studied by listening with their settings; composing and rehearsing with a critique and a revision; a showing every unit | A portfolio folder of 12 pieces over the band with reflections; three composed pieces revised and presented; 12 showings, three of them concerts; two marks a unit per student on the main look-for | Met marks on each year's 21 ids and growth on the look-fors. Nothing here has been tried with students, and Curio Class makes no claim that music study raises any other result |

### Safety and supplies in the notes

Hands-on days copy the frame's hazards and controls into their note (recordings at a set low level, buckets at a
set soft stroke and no drum near an ear, comfortable range and a changing voice's own octave or the rhythm spoken,
clear aisles, hands washed; for the composing units, shared bells or keyboard wiped and the chord roots sung on the
free path; for the concert units, the front cleared and no cables across the aisle). The free path (desks and buckets,
the voice, found sounds, printed strips) is named where the frame lists one. Sensitivity flags from the frame are in
the note of each day that meets the work.

## Year 6 (grade 6 ids)

### Unit 1. How a piece works

Days 1 to 18, weeks 1 to 9. Seven ids, two techniques (naming symbols one by one, the listening response), two check
days. The arc opens on a lead sheet and a returning violin theme (day 1), teaches symbols in two sets (day 2 rhythm
and pitch, day 4 dynamics and articulation) before the form of "Shady Grove" is marked (day 6) and its history read
(day 7), so the symbols are in hand when form and style are discussed. The listening days (3, 8, 9, 10) build from
structure to setting to connection to judgment, so the teacher's criteria come last, once there is something to
judge. Rehearsal follows (12), then the critique (13), revision and the kept sheet (14), the showing to a partner
class (15). Day 16 is the reading sitting (MU:Pr4.2.6a kept sheet, 6b, 6c), day 17 the listening sitting (MU:Re7.2.6a,
6b, MU:Re9.1.6a, MU:Cn11.1.6a), each item marked met, partly or not yet; day 18 is the respond day for both.
The listening ids are spaced, no day added: the five-minute openers of rehearsal days 12 to 15 are a rotating
listening round on short new excerpts (12 structure, MU:Re7.2.6a; 13 judge on one criterion, MU:Re9.1.6a; 14 a
connection, MU:Cn11.1.6a; 15 a setting match, MU:Re7.2.6b), and day 11's drills add one structure item.
Processes: performing days 2, 4 to 6, 12 to 16; responding 3, 8, 10, 11 to 13, 15, 17; connecting 7, 9, 14, 17;
creating 12 (a two-bar ending, practice). Unit 1 has no readiness check: its rows are retrieved on day 2.
Candidate (a third listening work by a living Native American or Pacific Islander maker): dropped. Four works already
fill seven ids in 18 days, a fifth would cost a day, and year 6's range has a living Native American drum group in
unit 4. If a school leaves out unit 4's powwow study, the unit plan swaps one unit 1 listening work for a living
Native American maker's, so year 6 keeps one.

### Unit 2. Our interpretation

Days 19 to 36, weeks 10 to 18. Five ids, a rehearsed performance and a performance program. Two Satie takes open the
question (19); the expression map is taught in steps (20) before any rehearsal, and the three listening studies (19,
21, 22) give performer intent its evidence before students plan their own. Rehearsal starts on day 24 with the
practice plan. Choosing for a purpose (25 performing, 26 listening) and the three-choice chart (27) come after the
interpretation is under way, so day 28's two-bar phrase and program draft have real choices to point to. The critique
is day 30, revision day 31. Assessment: day 34, the showing, carries the performance item (MU:Pr4.3.6a), marked once
and kept; day 35 re-rehearses and finishes the kept program page (MU:Pr4.1.6a); day 36 is supported practice; the
written items (MU:Re8.1.6a, MU:Re7.1.6a, MU:Cn10.1.6a) sit in the mid-year check on day 37, which the frame makes
this unit's end-of-unit assessment; day 38 responds to both. MU:Re8.1.6a names creators' and performers' choices:
day 21 sets one choice Elgar wrote into the score beside one of du Pre's, and day 37's item on two takes asks for
one choice the composer made that both performers keep. Processes: performing 20, 23, 24, 29 to 35; responding
19, 21, 22, 26, 36; connecting 27, 28, 31; creating 28 (a two-bar phrase, practice).
Candidate (a second interpretation tradition from Africa or the Arab world): kept, no day cost. Day 22 hears, beside
the alap, a short take by a living woman performer from Africa or the Arab world in a tradition where the performer
shapes the music; the unit plan picks it, records whether she is living as of its date, checks its rights line, and
describes and links it. It gives year 6 a living woman maker (its only other woman is du Pre, a performer).

### Unit 3. AB and ABA

Days 39 to 50, weeks 20 to 25. Three ids, one product drafted, critiqued and revised. The ABA model (39) and the
question-and-answer phrase (40) come before the chords (41) and the notation ladder (42), so day 43's brief examples
in AB and ABA use all three. Day 45 develops one piece; critique 46, revision 47, showing 48. Day 49 is the
end-of-unit assessment: another pair plays four bars from each score (MU:Cr1.1.6a, MU:Cr2.1.6a, MU:Cr2.1.6b on the
guide); day 50 responds. Processes: creating 40 to 49; responding 39, 41 (works studied, review); performing 48, 49;
connecting 41 (each student writes one line on how Libertango's repeated phrase fits the dance it was made for,
practice).
Candidate (a model ABA piece by a living composer from Asia or Africa): dropped. The unit is 12 days with three works
and a fourth would cost a day; year 6 has living makers from Asia (Huun-Huur-Tu, Chaurasia) and Africa (N'Dour).

### Unit 4. Ready for the stage

Days 51 to 62, weeks 26 to 31. Six ids met in one revised piece and one concert. The venue study (51, 53) and the
judging of the unit 3 piece (52) come before revision (54), and the readiness card is taught (55) before it is used
in rehearsal (57). Critique at the dress rehearsal (58), the final piece and revision note (59), the last rehearsal
and kept readiness card (60). Day 61, the concert in week 31, is the end-of-unit assessment for all six ids; day 62
responds. Processes: creating 52, 54, 59; performing 55 to 61; responding 51, 52, 58; connecting 53, 61.
Candidate (the readiness card written for reuse in years 7 and 8): kept, no day cost; the card is used again on days
124 and 188.

## Year 7 (grade 7 ids)

### Unit 5. Two pieces, two worlds

Days 65 to 82, weeks 1 to 9 of year 7. Same shape as unit 1, one step harder: two contrasting pieces, form and tempo
signs, syncopation. Form signs (66) and tempo words with syncopation (68) come before the structure comparison (70)
and the culture-and-history readings (71). Listening moves from Vivaldi's plan (67) to the pipa piece against it (72),
the sonnet connection (73) and judging on chosen criteria (74). Day 80 is the reading sitting (MU:Pr4.2.7a kept sheet,
7b, 7c), day 81 the listening sitting (MU:Re7.2.7a, 7b, MU:Re9.1.7a, MU:Cn11.1.7a), day 82 the respond day.
As in unit 1, the openers of days 76 to 79 are the rotating listening round (structure, judge, connection, setting
match, with the 7a and 7b codes) and day 75 adds one structure item. Processes: performing 65, 66, 68 to 71, 76 to
80; responding 67, 72, 74 to 77, 79, 81; connecting 71, 73, 78, 81; creating 76 (a syncopated fill, practice).
Candidate (a contrasting piece by a living Native American composer): kept, no day cost. It is one of the two takes
judged on day 74; the unit plan picks the work, checks its rights line on its own page and confirms it repeats no
pick of another frame. Without it year 7 has no Native American maker.

### Unit 6. Two ways to tell it

Days 83 to 100, weeks 10 to 18. Same shape as unit 2: two expression maps for unit 5's pieces (84) after the blues
hook (83), the twelve-bar pattern (85) and Ethio-jazz beside it (86). The class agrees program criteria (89) before
the purpose and interest picks (90) and the three-choice chart (91). Critique 94, revision 95. Day 98, the showing,
carries the performance item (MU:Pr4.3.7a: two short contrasting excerpts in one group turn of at most four
minutes); day 99 finishes the kept program note (MU:Pr4.1.7a); day 100 is supported practice; the written items
(MU:Re8.1.7a, MU:Re7.1.7a, MU:Cn10.1.7a) sit in the mid-year check on day 101, the unit's end-of-unit assessment;
day 102 responds to both. Processes: performing 84, 85, 87, 88, 93 to 99; responding 83, 85, 86, 90, 100;
connecting 91, 92, 95; creating 92 (a two-bar blues answer, practice).
Candidate (a contrasting take by a living woman performer from Asia or the Arab world): dropped. Year 7 already has
Wu Man (living, Asia) in unit 5, and another take would cost a day.

### Unit 7. Theme and variations

Days 103 to 114, weeks 20 to 25. Same shape as unit 3: the four ways to vary a theme (104) and the four-chord pattern
(105) come before unity and variety on a score (106), then the theme and first variation (107), the second variation
and notation (109), critique 110, revision 111, showing 112. Day 113 is the end-of-unit assessment (MU:Cr1.1.7a,
MU:Cr2.1.7a, MU:Cr2.1.7b); day 114 responds. Processes: creating 104 to 113; responding 103, 106; performing 112, 113;
connecting 103 (the tune's two national uses, told), 106 (each student says how Umoja's title, unity, shows in
what the piece keeps, practice).
Candidate (a variation work by a living Native American or Asian composer): dropped. Unit 5's kept candidate gives
year 7 its Native American maker, and a fourth work in 12 days would cost a day.

### Unit 8. In style

Days 115 to 126, weeks 26 to 31. Same shape as unit 4, with criteria the student chooses (116) and class-written
rehearsal criteria (119). Day 125, the concert, is the end-of-unit assessment for all six ids; day 126 responds.
Processes: creating 116, 118, 123; performing 119 to 125; responding 115, 116, 122; connecting 117, 125.
Candidate (the class criteria chart carried into year 8): kept, no day cost; day 183 starts from it.

## Year 8 (grade 8 ids)

### Unit 9. Whole programs

Days 129 to 146, weeks 1 to 9 of year 8. Same shape as unit 1, with reading at sight new: the four steps on the
treble staff (131) and the bass staff (132) come before the drill (133, 139) and the reading day (144).
Culture-and-history effects (134) precede the program studies (135, 136); the student's own criteria (137) come
after the programs give something to judge. Day 144 is the reading day (MU:Pr4.2.8b at sight in groups at the
teacher's spot while the others write MU:Pr4.2.8c; MU:Pr4.2.8a kept sheet), day 145 the listening sitting
(MU:Re7.2.8a, 8b, MU:Re9.1.8a, MU:Cn11.1.8a), day 146 the respond day. As in unit 1, the openers of days 140 to
143 are the rotating listening round (with the 8a and 8b codes) and day 139 adds one structure item. Processes:
performing 129 to 133, 140 to 144; responding 135 to 137, 139 to 141, 143, 145; connecting 134, 138, 142, 145;
creating 140 (an introduction, practice).
Candidate (a fourth program from a living Native American or Pacific ensemble): dropped. Three whole programs already
fill the listening days, a fourth would cost a day, and year 8 has Brent Michael Davids in unit 10.

### Unit 10. What a program says

Days 147 to 164, weeks 10 to 18. Same shape as unit 2, with the backed reading taught in three steps (149) after the
interpretation is explained (148). Day 162, the showing, carries the performance item (MU:Pr4.3.8a: two short
excerpts and a spoken item); day 163 finishes the kept program note (MU:Pr4.1.8a); day 164 is supported practice;
the written items (MU:Re8.1.8a, MU:Re7.1.8a, MU:Cn10.1.8a) sit in the mid-year check on day 165, the unit's
end-of-unit assessment; day 166 responds. Processes: performing 148, 151, 152, 157 to 163; responding 147, 149, 150,
154, 164; connecting 155, 156, 159; creating 156 (a two-bar phrase, practice).
Candidate (a program by a living woman composer from Africa or Asia): dropped. Year 8 has living women makers
(Mariza) and Mary Lou Williams in this unit; another program would cost a day.

### Unit 11. Intro to coda

Days 167 to 178, weeks 20 to 25. Same shape as unit 3: the expanded form (168), the four ways to build tension
(169) and the accompaniment notation (170) come before composing (171, 173). Critique 174, revision 175, showing
176. Day 177 is the end-of-unit assessment (MU:Cr1.1.8a, MU:Cr2.1.8a, MU:Cr2.1.8b, eight bars played by another
pair); day 178 responds. Processes: creating 168 to 177; responding 167, 169; performing 176, 177; connecting 167
(Finlandia's later uses, told), 168 (students match each part of the expanded form to a moment in the Butterfly
Lovers tale, practice).
Candidate (a living Native American composer's expanded-form work): dropped. Year 8 has Davids in unit 10, and a
fourth work in 12 days would cost a day.

### Unit 12. Our closing concert

Days 179 to 190, weeks 26 to 31. Same shape as unit 4, with the student's own criteria (180, 183) and practice taken
from a named community source (181). Day 189, the concert, is the end-of-unit assessment for all six ids; day 190
responds. Processes: creating 180, 182, 187; performing 181, 183 to 189; responding 179, 180, 186; connecting 179,
183, 189.
Candidate (the samba de roda performance's source and setting recorded before the look-fors are written): kept, no
day cost; a unit plan step, named in day 179's note.

## Course-level checks

| Check | Days | Week | Samples |
|---|---|---|---|
| Year 6 mid-year | 37, respond 38 | 19 | Unit 2's end-of-unit assessment: MU:Re8.1.6a, MU:Re7.1.6a, MU:Cn10.1.6a written; MU:Pr4.3.6a from day 34; MU:Pr4.1.6a from day 35; unit 1's MU:Pr4.2.6b as a growth mark |
| Year 6 year-end | 63, respond 64 | 32 | Units 1 to 3: a four-bar answer phrase on a given two-chord pattern with its mood in one line and its A or B place in an ABA piece with the reason (MU:Cr1.1.6a, MU:Cr2.1.6b); a symbol set on a new score (MU:Pr4.2.6b); an unseen take judged on the teacher's criteria (MU:Re9.1.6a) |
| Year 7 mid-year | 101, respond 102 | 19 | Unit 6's end-of-unit assessment: MU:Re8.1.7a, MU:Re7.1.7a, MU:Cn10.1.7a written; MU:Pr4.3.7a from day 98; MU:Pr4.1.7a from day 99; unit 5's MU:Pr4.2.7b as a growth mark |
| Year 7 year-end | 127, respond 128 | 32 | Units 5 to 7: one variation of a given theme over a given chord pattern, its expressive aim written at the top and one decision that carries it named, with what stays and what changes (MU:Cr1.1.7a, MU:Cr2.1.7a); an unseen take judged with criteria chosen from the teacher's list (MU:Re9.1.7a) |
| Year 8 mid-year | 165, respond 166 | 19 | Unit 10's end-of-unit assessment: MU:Re8.1.8a, MU:Re7.1.8a, MU:Cn10.1.8a written; MU:Pr4.3.8a from day 162; MU:Pr4.1.8a from day 163; unit 9's MU:Pr4.2.8c as a growth mark |
| Year 8 year-end | 191, respond 192 | 32 | Units 9 to 11: a new eight-bar line at sight in groups at the teacher's spot (MU:Pr4.2.8b); a short introduction and coda for a given tune with its tension line, its expressive aim at the top, one coda decision that carries it named, and one line on unity, variety and where tension is released (MU:Cr1.1.8a, MU:Cr2.1.8a); an unseen take judged on criteria the student writes (MU:Re9.1.8a) |

- **Weeks.** Week 19 holds no other grade 6, 7 or 8 course's mid-year check (CALENDAR.md target weeks and
  data/plans/calendar.csv, read 2026-11-26); the other arts electives' week 17 counts with music as one (CALENDAR.md
  rule 3). Week 32 is the finals week. `frame.py calendar` reports no break.
- **The mid-year checks do not repeat a unit assessment.** Each is the end-of-unit assessment of the unit just
  ended (units 2, 6 and 10), as the frame sets it, so its items for that unit are the unit's own, given once; its
  only earlier-unit item is a growth mark from the year's first unit, not a second claim. The year-end checks come
  after the concert unit, whose own concert (week 31) is its end-of-unit assessment, so they draw only on the year's
  first three units.
- **Collect once.** The showing marks (days 34, 98, 162) and the kept program pages are used by the mid-year check
  and never taken again: the check carries the unit's record and says so, and re-asks nothing a unit day gave one to
  three days before (lead call 7). The concert record (days 61, 125, 189) is carried by the year-end check unscored.
- **Task form (lead call 6).** A showing or performance is music's own evidence and may follow a unit showing; what
  may not repeat inside two weeks is the same item. The year-end checks come one week after the concert and use new
  work with their own items (a new chord pattern or theme, a new line at sight, an unseen take), which meets the
  rule; each check day's note says so.
- **Codes not sampled on a course-level check (rule 3, L107).** Each is taught and assessed on its unit's
  end-of-unit assessment in its own year, and one 38-minute sitting a check cannot hold more without crowding the
  items it has: MU:Pr4.2.6a, 6c, MU:Re7.2.6a, 6b, MU:Cn11.1.6a and MU:Cr2.1.6a (year 6, units 1 and 3); MU:Pr4.2.7a,
  7c, MU:Re7.2.7a, 7b, MU:Cn11.1.7a and MU:Cr2.1.7b (year 7, units 5 and 7); MU:Pr4.2.8a,
  MU:Re7.2.8a, 8b, MU:Cn11.1.8a and MU:Cr2.1.8b (year 8, units 9 and 11). The concert units' six ids a year (units 4,
  8 and 12: Cr3.1a, Cr3.1b, Cr3.2a, Pr5.1a, Pr6.1a, Pr6.1b) are assessed by the week 31 concert, the frame's design,
  and the year-end check carries that record unscored. MU:Pr4.2.8c is sampled on day 165 (a growth mark). Naming
  these with the reason is enough where the frame's check table limits the sample (lead call 3).

## Shorter path

**Once a week (32 sessions a year).** Every unit and every id is kept by merging the days below; fluency days fold
into the warm-up openers. Days are given by their place in the year (year 7 adds 64, year 8 adds 128); each unit
keeps the demonstration with its step card opened by the listening work, one rehearsal or composing session with the
critique, the showing or check, and a respond session, and no merge drops a critique, a revision or a respond day.

| Unit (year 6 / 7 / 8) | Sessions | Sessions, by year days merged |
|---|---|---|
| 1 / 5 / 9 | 8 (weeks 1 to 8) | 1+2; 3+4+5; 6+7; 8+9+10+11; 12+13 (critique); 14+15 (revision and showing); 16+17 (one sitting on the budget below, the kept sheet from 14); 18 |
| 2 / 6 / 10 | 8 (weeks 9 to 16) | 19+20; 21+22+23; 24+25; 26+27+28; 29+30 (critique); 31+32+33 (revision); 34 (showing, performance item); 35+36 |
| Mid-year check | 2 (weeks 17, 18) | 37; 38 |
| 3 / 7 / 11 | 6 (weeks 19 to 24) | 39+40; 41+42+44; 43+45; 46+47 (critique and revision); 48+49 (showing and check); 50 |
| 4 / 8 / 12 | 6 (weeks 25 to 30) | 51+52+53; 54+55+56; 57+58 (critique); 59+60 (revision, kept readiness card); 61 (concert); 62 |
| Year-end check | 2 (weeks 31, 32) | 63; 64 |

Minute budgets for the merged sittings, so no assessed part shrinks:
- **Merged listening and reading sitting (units 1 and 5, year days 16+17).** Set-up 2, items 30, collecting 3; the
  5-minute self-check moves to the respond session. Items, each recording played twice: symbols 5, culture and
  history 4, elements and structure 6, three short setting excerpts 5 (all three kept, so several genres, cultures
  and eras stay in the item), a take judged 6, connection map 4.
- **Unit 9 (days 144+145).** The listening items come first with the whole class (14 minutes); then six groups
  sight-read at the teacher's spot (15 minutes) while the others write the MU:Pr4.2.8c item and the connection map
  with no playback, so no group is heard while the room works to a recording.
- **Units 3, 7 and 11 (days 48+49, showing and check).** The showing is to the partner pair only (10 minutes), then
  the check; the class hears the pieces in the respond session.

**A year about 10 days short.** Ten school days is about four sessions of a course meeting twice a week (lead call
1, 2026-11-26), so each year names four fold-in days and lists more as spares. None is assessed and no owned part is
cut; each folds into the neighbor named and saves the minutes shown. Days are year days (year 7 adds 64, year 8
adds 128).

| Year day | Kind | Folds into | Minutes saved |
|---|---|---|---|
| 5 | Fluency drills | the next day's opener (5 minutes); the baseline look moves into that day's first practice time, rotating groups as written | 35 |
| 11 | Fluency drills | the next day's opener; the structure item joins day 12's listening round | 35 |
| 23 | Fluency drills | the next day's opener; the baseline look moves into that day's first practice time, rotating groups as written | 35 |
| 44 | Fluency drills | the next day's opener | 35 |

Total: 140 minutes a year saved, four of 64 course days (60 left), 12 of 192 over the band.

Spares, for a year shorter still (same rule):

| Year day | Kind | Folds into | Minutes saved |
|---|---|---|---|
| 56 | Fluency drills | the next day's opener; the baseline look moves into that day's first practice time, rotating groups as written | 35 |
| 15 | Showing to a partner class | the end of day 14, for the class (15 minutes); its listening round is skipped, the other three keep the spacing | 25 |
| 48 | Showing of drafts | the end of day 47 (15 minutes) | 25 |
| 29 | Rehearsal | days 28 and 30 (10 minutes) | 30 |
| 33 | Final rehearsal | day 32 (10 minutes) | 30 |
| 36 | Supported practice | the last 10 minutes of day 35 | 30 |

The same holds in years 7 and 8: on every folded fluency day that carries the unit's baseline look (69, 87, 120,
133, 151, 184 and their year 6 twins), the look moves into the next day's first practice time, so each unit keeps its
two marks a student.

**A shorter session (30 minutes).** The days hold: the opener drops to 3 minutes, a listening study plays its work
once instead of twice (sittings still twice), and a written sitting moves its 5-minute self-check into the next day's
opener; performance days hear five groups of six for about four minutes each.

## For the lead

1. **Showing days 34, 98 and 162.** The frame calls each an application day whose mark is kept for the mid-year
   check. GLOSSARY puts an end-of-unit assessment on a Check day with `assess` = `end`, and the gate asks for one in
   every unit, so these three days are Check / end here (the performance item of the unit's end-of-unit assessment),
   with no day count changed. Fix for the frame: in Scored evidence, read "heard and marked at the unit's showing (a
   check day, the mark kept for the mid-year check)".
2. **Codes not sampled on a course-level check** (rule 3, L107) are listed above with the reason. If every code must
   be sampled, each year-end check needs a second session or a check task per unit, which the frame's one check day
   cannot hold.
3. **The once-a-week path's mid-year check is in week 17** (the frame's choice). Health 6 to 8 holds its grade 6, 7 and
   8 mid-year checks in week 17, and ELD grades 6 and 7 too; CALENDAR.md rule 3 counts every course by school day, and
   calendar.csv does not carry the once-a-week path, so frame.py cannot see it. A school on that path picks a meeting
   day that week apart from those checks; the frame's line "weeks 17 and 31 hold no core check" is true but not the
   whole rule.
4. **Year 6 retrieval of grade 5 rows.** Checked against Music 3 to 5's scope (2026-11-26): every mu-g5 row is
   last used in year 5 (respond and choose day 144, express and invent day 158, document and revise day 176, read and
   perform day 192); retrieval holds.
5. **Unit 5's kept Candidate** needs the unit plan to pick a living Native American composer's piece that no other
   frame uses (Tate, Ballard and Davids are taken).

Settled in the fix pass (2026-11-26): the once-a-week merged sitting keeps every item on a minute budget (Shorter
path), and "a year about 10 days short" means ten school days, about four sessions (lead call 1).
