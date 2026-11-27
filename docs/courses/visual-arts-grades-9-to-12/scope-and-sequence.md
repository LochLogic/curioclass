# Scope and sequence: Visual Arts, grades 9 to 12

Course id visual-arts-grades-9-to-12; grades 9 to 12 run as four levels of 160 days (640 course days); draft, 2026-11-26.

The days live in data/plans/visual-arts-grades-9-to-12/days.csv. This page says why they fall where they do. It
changes none of the frame's units, owned rows or day counts.

## How the band is laid out

- **Standards by level.** National Core Arts Standards, 2014, visual arts, by id only. Level 1 (Proficient) claims
  the 15 `.Ia` ids, Level 2 (Accomplished) the 15 `.IIa` ids, Level 3 (Advanced) the 15 `.IIIa` ids: 45 in all,
  the STANDARD.md 3.2 count, each taught and assessed in its own level. Level 4 claims no new id: its days carry
  the `.IIIa` ids again on new, self-directed work, and its `skills` cells name the unit's va-g12 row. No grade 8 id
  is claimed; the bridge (unit 1) teaches grade 8 techniques as readiness. A level is not a grade: a student new to
  visual arts starts at Level 1 in any grade.
- **Course days and school days.** The course meets five 45-minute sessions a week, every school day. Each level
  is one 160-day school year of 32 weeks, taken in its own year, so school days are counted inside each level: level
  day = course day minus 160 times (level minus 1), level day n is school day n of that year, and week =
  (level day - 1) // 5 + 1. The `school_day` column is left blank; frame.py then reads course day n as band school
  day n, which gives the same week inside each level. Level 1 is course days 1 to 160, Level 2 is 161 to 320,
  Level 3 is 321 to 480, Level 4 is 481 to 640. frame.py files the rows under "9-12 Level n". Every unit and check
  falls in the frame's weeks by this formula.
- **The unit shape.** Each paired unit opens with the hook and its compelling question on day 1, retrieval in day
  2's opener (10 minutes, the row before in the same thread), technique taught in steps with a step card before the
  making that needs it, the baseline look in the first practice days, the mid-unit assessment on the frame's day,
  one critique in the critique routine (describe, ask, suggest; critique the work, never the person; praise alone is
  not feedback) in the second making stretch with a revision after it, practice items
  before the end, then two end days: a sitting of written items on unseen works (no paint, ink or clay out), and
  the showing with self-score, where the product is scored from kept work afterward. A respond day follows. One
  piece goes to the portfolio each unit with a one-line reflection. The portfolio (or a photo record of each piece)
  stays at school across levels, since Level 2 (days 161, 203, 237) and Level 3 (day 328) draw on Level 1 work; a
  placed student uses the work brought for the placement checklist (the frame's brought-work route) on days 203 and
  237, and writes a first reaction on day 329.
- **The four processes.** Each level holds all four artistic processes (create; present; respond; connect), and each
  unit touches at least the processes its frame row names; a unit need not claim all four (lead call, 2026-11-26).
  Each unit's "Processes" line names the unit days. A respond day (acting on a check) is tagged only by the process
  of the part it reteaches, never as responding by itself; a Level 4 critique held as the respond day is responding.
- **Baseline looks.** Every unit opens its main look-for with a baseline look on two practice days, one group each,
  never on a day a technique or work is first taught and never on a fold-in day, so each student has two marks a
  unit (the baseline and the end). The days are named in each day's note.
- **Equipment and safety** are in each day's note, as the frame lists them: the hazard and its control, the free or
  borrowed path. No blades for students anywhere in the band (APPROACH "Safe use"; For the lead 3 of the frame).
  An adult hangs work above head height and handles any light.

## Readiness and retrieval (rule 2, counted by grade number)

| Earlier row | Last used | Where it comes back | Treatment |
|---|---|---|---|
| va-g8-look, va-g8-craft | Grade 8 | Unit 1 (days 3, 9) and unit 2 day 2 (course day 14) | Retrieval (one grade back); the bridge reteaches the techniques for a student new to visual arts, standing in for the readiness check (frame) |
| va-g8-ideas, va-g8-revise | Grade 8 | Unit 1 (day 10, before its critique), unit 3 day 2 (day 46) | Retrieval |
| va-g8-design, va-g8-judge | Grade 8 | Unit 4 day 2 (day 82) | Retrieval |
| va-g8-show, va-g8-museum | Grade 8 | Unit 1 day 9, unit 5 day 2 (day 122) | Retrieval |
| va-g9-ideas, va-g9-judge | Earlier in Level 1 | Unit 4 day 2, unit 5 day 2 | Retrieval (same year) |
| va-g9 rows (all eight) | Level 1 | Unit 6 days 2 to 4, then day 2 of units 7 to 10 | Retrieval; the unit 6 placement sitting and checklist stand as the readiness check for a student who placed in or skipped a year (frame) |
| va-g10 rows (all eight) | Level 2 | Unit 11 days 2 to 4, then day 2 of units 12 to 15 | Retrieval; the unit 11 placement stands as readiness |
| va-g9 rows (two levels back) | Level 1 | Used again in Level 2 by one hop (each va-g10 row assumes its va-g9 row) | Counts as used in Level 2, so Level 3 retrieves, never re-checks |
| va-g11 rows | Level 3 | Unit 16 day 2, unit 17 day 2, unit 18 day 2, unit 19 day 2 | Retrieval; a returning student who skipped a year does the frame's 10-minute readiness check on unit 16 day 2 while the class does the retrieval opener (in the note; settled, see For the lead 1) |

Every unit's first day stays clean for the hook. The `retrieves` column carries each retrieval.

## Level 1 (course days 1 to 160)

Carries the 15 `.Ia` ids (Proficient).

### Unit 1. The bridge: tools of seeing (12 days)
Course days 1 to 12, weeks 1 to 3. Value, contour and gesture, one-point perspective, a mixed color wheel, the
looking routine and the credit idea, taught again so every Level 1 student starts level: value, gesture, perspective,
the looking routine and the credit idea come from grades 6 to 8; contour is taught in grade 6 (6 to 8 days 7, 10) and
retaught here; the full mixed color wheel is first built here (day 8), since grade 5 mixes colors and grade 6
names schemes but no earlier day builds the wheel. Order:
pencil before charcoal before wet media, so the hazard routine grows with the material; the looking routine (day 9)
comes before the first critique (day 10). End: day 11, the showing with a readiness record (met, partly, not yet),
no score, which sets unit 2's groups; response time on day 12. No id claimed; 12 of 160 days (7.5 percent) are
outside the standards, inside the bar's 10 percent. Candidate (a value study by a maker from Asia or Africa set
beside Dürer's): kept, 10 minutes inside day 3. Sensitivity: Melencolia I's meaning is argued over (day 1 note).
Processes (unit days): create 1 to 8, 10, 12; present 11, 12; respond 1 to 3, 7, 9 to 11; connect 3, 9.

### Unit 2. How images shape us (32 days)
Course days 13 to 44, weeks 3 to 9. The Migration Series, Frankenthaler and El-Salahi carry a hypothesis about a
set of works (Re7.1), a reflection on an everyday image (Re7.2), unplanned making in ink, watercolor or air-dry clay
(Cr2.1) and the hazard card (Cr2.2). Order: the hazard card comes on day 2, before any wet material; the hypothesis
is taught (day 9) only after two looking days; the everyday-image days follow the mid so the hazard card is
assessed while fresh. Mid: day 16 (course day 28), the hazard card item. Critique day 22, revision day 23. End: day
30 (sitting: Re7.2, Cr2.2 on unseen work) and day 31 (showing; Re7.1 and Cr2.1 from kept work); response day 32.
Candidate (an unplanned work by a living maker from Asia or the Americas): dropped; the unit already studies three
works, and Level 1 meets Asia in units 3 and 5, so a fourth work would cut making time. Sensitivity: the Migration
Series' panels of violence (days 1, 8). Processes: create 2 to 4, 6, 7, 13 to 18, 21 to 23, 27, 28, 30, 32;
present 29, 31; respond 1, 5, 8 to 12, 19, 20, 22, 24 to 26, 28, 30, 31; connect 1, 5, 8, 10, 12, 13, 19, 20.

### Unit 3. Starting points (34 days)
Course days 45 to 78, weeks 9 to 16. Three start routes (days 5 and 6) and a reasoned pick (Cr1.1), a question about daily life
today tied to a current maker (Cr1.2), and standards named as whose applied to unfinished work (Cr3.1), on Mutu and
a caryatid. Order: routes before the pick, the sustained-study technique (days 10, 13) before study sessions, the
two kinds of standards (days 19, 20) right before the critique that uses them. Mid: day 17 (course day 61), the
planning portfolio entry. Critique day 22, revision days 23, 24. End: day 31 (sitting, Cr3.1) and day 32 (showing;
the planning entry, critique record and revised work scored from kept work), course days 75 and 76 as the frame
sets; response day 33; day 34 is a portfolio day. Candidate (a present-day standards set from outside Europe and
North America): kept, inside day 20. Sensitivity: the caryatid's old use and Mutu's stated aims (day 1).
Processes: create 2 to 18, 21 to 24, 26 to 28, 31, 33, 34; present 26, 29, 32; respond 1, 19, 20, 22, 25, 30, 31;
connect 1, 8, 9, 19, 20.

### Level 1 mid-year check (course days 79 and 80, week 16)
See Course-level checks.

### Unit 4. Changing a place (40 days)
Course days 81 to 120, weeks 17 to 24. A team proposes a change to one school space with plan drawing at 1 to 50
and a card model (Cr2.3), an idea log of dated steps (Cn10.1), an interpretation with evidence (Re8.1) and jury
standards (Re9.1), on Lin's memorial, Olowe's posts and The Gates. Order: the brief and the site walk before
scale drawing; the scale ruler card (day 6) before any plan; the model technique (day 12) before model sessions;
the jury reading (day 14) before the standards are drafted. Mid: day 20 (course day 100), the idea log and first
plan. Critique day 26, revision day 27. End: day 38 (sitting, Re8.1 and Re9.1) and day 39 (panel showing; model,
rationale and log from kept work); response day 40. Candidate (a team-design case from Asia or Latin America):
kept, 15 minutes inside day 3. Sensitivity: the memorial lists the dead (day 1). Math lean: grade 7 scale drawing,
carried by the ruler card (day 6). Processes: create 2, 4 to 8, 11 to 13, 16, 17, 20 to 24, 26 to 28, 32, 37, 39,
40; present 31, 34, 35, 39; respond 1, 3, 9, 10, 14, 15, 18, 19, 25, 26, 29, 30, 36, 38; connect 1 to 5, 8,
9, 11, 14, 15, 17, 20, 27, 33.

### Unit 5. The curator's eye (38 days)
Course days 121 to 158, weeks 25 to 32. Choosing, keeping and showing a collection (Pr4.1), why and how a real
exhibition is laid out (Pr5.1), how an exhibit shapes awareness (Pr6.1), and how a culture reading changes a
reaction (Cn11.1), on Mining the Museum, Americans and Sunflower Seeds. Order: two exhibitions studied before the
class plans its own; mounting and labels taught (days 13, 14) before mounting sessions; Sunflower Seeds is seen
before its reading (days 21, 22) so the change in reaction is real. Mid: day 19 (course day 139), the exhibition
plan. Critique day 29, revision day 30. End: day 35 (the show, level day 155, as the frame sets) and day 36 (the
sitting, Pr6.1 and Cn11.1); respond days 37 and 38 (course days 157, 158) in week 32 beside the year-end check.
Candidate (an exhibition from Africa or Asia whose pages explain its layout): kept as a third option inside day 3.
Sensitivity: Mining the Museum and slavery's record (day 1); Americans (day 4); Sunflower Seeds and Chinese
politics (day 21). Leave-out (frame, a unit this course names: a museum show built around objects of slavery): a
work may be swapped, which keeps the unit, its show and its ids; if a school or family, or a student aged 18 or
older, leaves the unit out for its community's reasons, the course page and the family note name the ids not
claimed that level: VA:Pr4.1.Ia, VA:Pr5.1.Ia, VA:Pr6.1.Ia, VA:Cn11.1.Ia. Never a short-year or time cut.
Processes: create none (the frame's processes for this unit are presenting and connecting; its
making is mounting and installing, tagged present); present 1 to 20, 25 to 38; respond 1, 3, 5, 6, 21, 25, 29;
connect 1, 4, 7, 8, 21 to 24, 26, 33, 36, 37.

### Level 1 year-end check (course days 159 and 160, week 32)
See Course-level checks.

## Level 2 (course days 161 to 320)

Carries the 15 `.IIa` ids (Accomplished).

### Unit 6. Review and placement (6 days)
Course days 161 to 166, weeks 1 and 2. Revisits of the Migration Series and Lin's memorial, review stations on
Level 1's techniques and routines (days 2, 3: retrieval of all eight va-g9 rows), the placement checklist (day 4),
and the placement sitting on day 5, a parallel form of Level 1's year-end check, assess = end, scored for
placement only; response day 6 sets unit 7's groups. Candidate (the sitting as a parallel form): kept, day 5. No
id claimed. Processes: create 2 to 6; present 4; respond 1, 3 to 5; connect 1, 4.

### Unit 7. Images that move people (34 days)
Course days 167 to 200, weeks 2 to 8. Aesthetic and empathetic reactions to natural and built places (Re7.1), how
well an image sways an audience (Re7.2), a term in one medium with a practice log (Cr2.1), and the ethics of making
and sharing (Cr2.2), on Migrant Mother, the 2008 poster and The Oxbow. Order: the collagraph and wash techniques
(days 3, 4; each names grade 3's and grade 8's prints and grade 5's and grade 7's washes as known, and adds one
step) before medium studies; the two cases (days 13, 14) before the reasoning is written. Mid: day 17 (course
day 183), the practice log and first studies. Critique day 23, revision day 24. End: day 32 (sitting, Re7.2 and
Cr2.2) and day 33 (showing; reaction page and log from kept work); response day 34. Candidate (an image from Asia
or Africa that swayed an audience): kept, inside day 10. Sensitivity: Florence Owens Thompson taught by name with
dignity; the poster studied for its making and credit, never a side (day 1). Processes: create 2 to 6, 12 to 18,
21 to 24, 26, 28 to 32, 34; present 29, 31, 33; respond 1, 7 to 11, 19, 20, 23, 25, 27, 30, 32; connect 1, 7,
9, 10, 13, 14.

### Unit 8. Problems from my own work (36 days)
Course days 201 to 236, weeks 9 to 16. A fresh problem posed from an earlier piece (Cr1.1), old and new materials
and methods weighed (Cr1.2), and revision toward a stated vision (Cr3.1), on Butler and Hung Liu. Order: the
portfolio review (day 3) before any planning; fabric collage taught (day 5) before making; vision taught (day 14)
before the critique that tests it (day 22). Mid: day 18 (course day 218), the planning entry. Critique day 22,
revision days 24, 25. End: day 33 (sitting, Cr3.1) and day 34 (showing; entry, page, critique record and draft and
final from kept work), level days 73 and 74 as the frame sets; response day 35; day 36 a portfolio day. Candidate
(an old method made new by a living maker from Africa or the Pacific): kept, inside day 4. Sensitivity: Resident
Alien and immigration; no student asked about status (day 1). Processes: create 2 to 8, 10 to 20, 22 to 29, 33,
35, 36; present 27, 30, 32, 34; respond 1, 9, 21, 22, 31, 33; connect 1, 4, 9.

### Level 2 mid-year check (course days 237 and 238, week 16)
See Course-level checks.

### Unit 9. Redesign for now (40 days)
Course days 239 to 278, weeks 16 to 24. A redesign answering an issue of today (Cr2.3), a dated research page
(Cn10.1), the background facts that change a reading (Re8.1), and another person's standards tested (Re9.1), on
Stony Island Arts Bank, the Mirror Shield Project, Red Star's delegation portraits and Lin's memorial (a return with
a new task). Order: issue and research before drawing; the three-view and model technique (day 11) before model
sessions; the standards test (days 14 to 16) before its practice. Mid: day 20 (course day 258), the research page
and first drawings. Critique day 27, revision day 28. End: day 38 (sitting, Re8.1 and Re9.1) and day 39 (panel
showing; model, rationale, research page from kept work); response day 40. Candidate (a redesign case from Asia or
Latin America): kept, inside day 2. Sensitivity: Standing Rock and the water protectors, no side on the pipeline,
no Native designs copied (day 3); Red Star's own nation (day 6). Issues come from a checked list; the side is never
scored. Processes: create 2, 10 to 12, 18, 20 to 24, 26 to 29, 32, 37, 39, 40; present 31, 34, 35, 39; respond 1, 3, 6 to 8, 14 to 17, 25, 27, 30, 36, 38; connect 1 to 6, 9, 13, 14, 19 to 21, 28, 33.

### Unit 10. Art, power and place (40 days)
Course days 279 to 318, weeks 24 to 32. Choosing and critiquing one's own works for a show (Pr4.1), hanging and
lighting in one real place (Pr5.1), an argument tying works to history and politics (Pr6.1), and art serving power
then and now (Cn11.1), on Augustus, Shah Jahan, Sherald's portrait, Shonibare's ship and a local mural. Order:
past uses (days 1 to 5) before the argument; the site survey (day 13) before the plan. Mid: day 20 (course day
298), the argument's draft. Critique day 26, revision day 27. End: day 37 (the portfolio show, level day 155) and
day 38 (sitting, Cn11.1); respond days 39, 40 in week 32. Candidate (a local mural or monument the school names):
kept, day 4. Sensitivity: naval history and colonial trade (day 6); local monuments may be disputed (day 4).
Processes: create none (presenting and connecting by the frame); present 10 to 14, 16, 19, 24 to 30, 33 to 37,
39, 40; respond 1, 3, 6, 26; connect 1 to 9, 15, 17, 18, 20 to 23, 31, 32, 38, 39.

### Level 2 year-end check (course days 319 and 320, week 32)
See Course-level checks.

## Level 3 (course days 321 to 480)

Carries the 15 `.IIIa` ids (Advanced).

### Unit 11. Review and placement (6 days)
Course days 321 to 326, weeks 1 and 2. Revisits of Migrant Mother and Shonibare's ship, review stations (days 2, 3:
retrieval of all eight va-g10 rows), the checklist (day 4), and the placement sitting on day 5, a parallel form of
Level 2's year-end check, assess = end, for placement only; response day 6. Candidate (parallel form): kept, day 5.
No id claimed. Processes: create 2 to 6; present 4; respond 1, 3 to 5; connect 1, 4.

### Unit 12. Seeing again (34 days)
Course days 327 to 360, weeks 2 to 8. How a reaction grows with learning (Re7.1, the student's own Level 1 reaction
to the Migration Series set beside a new one), patterns across the Harlem Renaissance (Re7.2), a themed set of
three works (Cr2.1), and liberty and duty in using another maker's image, with the 2023 ruling taught as decided
(Cr2.2). Order: the old reaction is pulled (day 2) before the new is written (day 3); the series medium is taught in
named steps by medium group with its step and hazard cards (day 6) before work 1 (day 10), one step past Level 2's
sustained studies; the era reading (day 8) before the open-collection search (day 9). Cr2.2 covers both its parts:
using another maker's image (days 13, 14) and a materials or tools choice that affects others (days 14, 27 and the
sitting, day 32). Mid: day 17 (course day 343), the theme plan and first work. Critique
day 23, revision day 24. End: day 32 (sitting, Re7.2 and Cr2.2) and day 33 (showing; two-reaction page and works
from kept work); response day 34. Candidate (a second pattern study, an era group from Asia or Latin America):
kept, one Fluency day (day 15). Sensitivity: Douglas's murals show slavery and its aftermath (day 1). Processes:
create 5 to 7, 10, 12 to 14, 16 to 19, 22 to 25, 27 to 30, 32, 34; present 29, 31, 33; respond 1 to 4, 8, 9, 11, 15, 20, 21, 23, 26, 30, 32; connect 1, 8, 9, 13, 15.

### Unit 13. Art for change (36 days)
Course days 361 to 396, weeks 9 to 16. A prediction of how art could move a community (Cr1.1), a themed series that
follows or breaks a named norm (Cr1.2), and changes defended against old and new standards and a vision (Cr3.1), on
What Is Missing? and I See Red: Target. Order: the change and community (day 4) before the series plan; old and new
standards (day 16) before the critique (day 21). Mid: day 18 (course day 378), the series plan. Critique day 21,
revision plan day 22. End: day 33 (sitting, Cr3.1) and day 34 (showing), level days 73 and 74; response day 35;
day 36 a portfolio day. A second adult reads work on a sensitive subject before it is shown (day 32). Candidate (a
series by a living maker from Africa or Asia aimed at a change in its community): kept, inside day 5.
Sensitivity: I See Red and the Columbus anniversary, no imagery copied (day 3); the change chosen is never scored.
Processes: create 2, 4 to 15, 17 to 30, 33, 35, 36; present 30, 32, 34; respond 1, 3, 16, 21, 31, 33; connect 1 to
5.

### Level 3 mid-year check (course days 397 and 398, week 16)
See Course-level checks.

### Unit 14. Images that help or hinder (40 days)
Course days 399 to 438, weeks 16 to 24. An argument work in collage about how a culture's images help or hinder
(Cr2.3), a research page tying history, society and experience to making choices (Cn10.1), the most believable
reading of Guernica defended (Re8.1), and one work judged by several sets of standards (Re9.1), on Unbranded,
Guernica, Reihana's in Pursuit of Venus and the Dufour wallpaper. Order: research and collage technique (days 3 to
6) before the work; readings weighed (days 7, 8) before they are written. Mid: day 20 (course day 418), the research
page and the competing-readings argument (about 500 words, day 15). Critique day 26, revision day 27. End: day 38 (sitting) and day 39 (showing); response
day 40. Candidate (a culture's material objects from Africa or Asia as a research source): kept, inside day 4.
Sensitivity: Unbranded's racial images (day 1); Guernica and war, another work by choice (day 7); the wallpaper as
a European view (day 12). Leave-out (frame, a unit this course names: war and colonial imagery): a work may be
swapped (another work for Guernica, day 7), which keeps the unit, its showing and its ids; if a school or family, or
a student aged 18 or older, leaves the unit out for its community's reasons, the course page and the family note
name the ids not claimed that level: VA:Cr2.3.IIIa, VA:Cn10.1.IIIa, VA:Re8.1.IIIa, VA:Re9.1.IIIa. Never a
short-year or time cut. Processes: create 2, 5, 6, 10, 16, 19, 22 to 28, 32, 37, 39, 40; present 34, 35, 39;
respond 1, 7 to 9, 12 to 15, 17, 20, 26, 29 to 31, 36, 38; connect 1 to 4, 7, 11, 12, 18, 20, 21, 33.

### Unit 15. Keeping and changing (40 days)
Course days 439 to 478, weeks 24 to 32. Curating an event show with a reason for each choice (Pr4.1), two ways to
store and protect compared (Pr5.1), a small collection that helps viewers understand one experience (Pr6.1), and
a judgment of artists' influence on a society (Cn11.1), on The Night Watch's conservation, América Tropical and
Rivera's Detroit murals. Mid: day 20 (course day 458), the collection plan and judgment draft. Critique day 26,
revision day 27. End: day 37 (the event show, level day 155) and day 38 (sitting, Cn11.1); respond days 39, 40 in
week 32. Candidate (a conservation case from Africa or Asia): kept, inside day 4. Sensitivity: América Tropical's
crucified figure, a unit a school may leave out (day 3); Rivera's murals disputed in their day (day 7). Leave-out
(frame, a unit this course names): a work may be swapped, which keeps the unit, its show and its ids; if a school or
family, or a student aged 18 or older, leaves the unit out for its community's reasons, the course page and the
family note name the ids not claimed that level: VA:Pr4.1.IIIa, VA:Pr5.1.IIIa, VA:Pr6.1.IIIa, VA:Cn11.1.IIIa. Never
a short-year or time cut.
Processes: create none (presenting and connecting by the frame); present 1 to 6, 11 to 18, 20, 21, 23 to 31, 33
to 37, 39, 40; respond 7, 26; connect 1, 3, 7 to 12, 19 to 22, 32, 38, 39.

### Level 3 year-end check (course days 479 and 480, week 32)
See Course-level checks.

## Level 4 (course days 481 to 640)

Carries the 15 `.IIIa` ids again on new work; claims no new id.

Level 4 is the student's own year. Its checkpoints are Check days with assess = mid; each is followed by a
critique as its respond day (APPROACH). Ids are `.IIIa`, applied again.

### Unit 16. The proposal and the series (50 days)
Course days 481 to 530, weeks 1 to 10. A written proposal with a checkpoint calendar, then a series made with
growing independence, on Monet's Stacks of Wheat and Ojih Odutola's A Countervailing Theory. Checkpoint 1: day 10
(course day 490), the proposal; the proposal critique on day 11. Checkpoint 2: day 30 (course day 510), the first
works; the series critique on day 31. End: day 48, the series so far and the defended statement draft; response
day 49; day 50 writes next steps. After unit 16 the series continues as homework sketchbook time, in unit 18's
studio sessions for a student whose project grows from it, and in a class studio session on unit 19 day 35. The
hazard card for the student's medium is written and checked (day 7) before the material trials (day 8). Readiness: a returning
student who skipped a year does the frame's 10-minute check on day 2 (note). Candidate (a series by a living maker
from Asia, the Pacific or Native North America): kept, inside day 3. Sensitivity: an invented history of Nigeria
(day 3). Processes: create 1, 2, 4 to 46, 48 to 50; present 38, 47, 48; respond 1, 3, 11, 31; connect 3, 4.

### Unit 17. Criticism (28 days)
Course days 531 to 558, weeks 11 to 16. A critical essay of about 1,500 to 2,000 words on Las Meninas and a second
work: competing readings and a defended one (Re8.1), two sets of standards (Re9.1), reactions over time (Re7.1),
shared features of a group (Re7.2), and a defended talk. ELA lean: W.11-12.1, claim, counterclaim and evidence.
Grade 11 English's argument unit ends on its day 55, so day 3 (level day 53) carries the bridge from the frame's
"if later" line: it teaches the frame the essay needs where English has not, and the guide scores the art criticism,
not the English standard. Mid: day 14 (course day 544), the planner and first sections. Critique day 18. End: day
26, the talk, with the essay scored from kept work; response day 27; day 28 files the essay for the mid-year check.
Candidate (a second work from Africa or Asia offered first): kept, inside day 6. Sensitivity: the court attendants
of short stature named with dignity (day 1). Processes: create 7 (two-minute compositional thumbnails of the two works, drawing as a way of looking);
present 21 to 23, 25, 26, 28; respond 1 to 14, 16 to 21, 24, 26, 28; connect 1, 4, 5.

### Level 4 mid-year check (course days 559 and 560, week 16)
See Course-level checks.

### Unit 18. Art with a purpose (40 days)
Course days 561 to 600, weeks 17 to 24. A project for a real audience, with an ethics record and consent plan
(Cr2.2), the making (Cr2.3) and a knowledge record (Cn10.1), on Project Row Houses and Blanket Stories.
Checkpoint 1: day 8 (course day 568), the brief and consent plan; brief critique day 9. Checkpoint 2: day 25
(course day 585), the work and its records; project critique day 26. End: day 39, the project shown to its
audience; response day 40. Candidate (a community project led by a maker from Africa, Asia or Latin America):
kept, inside day 5. Sensitivity: Seneca and other community stories, no Native designs copied (day 3); a project
with people in it needs their yes and a family's yes under 18 (day 4). Processes: create 2, 4 to 10, 12 to 15, 17
to 21, 23 to 35, 37, 39, 40; present 36 to 39; respond 1, 3, 9, 26; connect 1 to 3, 5, 11, 16, 22, 25, 39.

### Unit 19. The exhibit (38 days)
Course days 601 to 638, weeks 25 to 32. A public exhibit of the year's work, with labels that justify (Pr4.1), a
protection plan (Pr5.1), a stated understanding for viewers (Pr6.1), and an appraisal of an artist's effect on a
society (Cn11.1), on Mastry and Hearts of Our People. Checkpoint: day 15 (course day 615), the plan and labels;
exhibit critique day 16. End: day 29, the exhibit opens (level day 149, week 30, as the frame asks) and day 30,
the talk to visitors; respond days 31, 32; days 33 to 38 keep the exhibit open, give a second talk, hold a series studio session
(day 35: the next work of the series toward its final state, the checkpoint calendar updated), take the exhibit down
and close the portfolio. Candidate (a show from Asia or Africa whose labels the museum publishes): kept, inside day
3. Sensitivity: Hearts of Our People's advisory board; ceremonial works studied by looking only (day 2).
Processes: create 35 (the series studio session); present 1 to 10, 12 to 18, 20 to 34, 36 to 38; respond 1, 16, 37, 38; connect 2, 5, 11, 19, 29, 30, 35, 38.

### Level 4 year-end check (course days 639 and 640, week 32)
See Course-level checks.

## Course-level checks

Each check is a 45-minute sitting (set-up 3, work 38, collecting 4) with no paint, ink or clay out, followed by a
respond day in groups from the record sheet. Each check sits right after a unit's end-of-unit assessment and
carries that unit's product record unscored. Where its items come from:

- Level 1 mid-year (day 79): unit 2's ids, on unseen works and an unseen material; nothing from unit 3.
- Level 1 year-end (day 159): units 3 and 4's ids on a new prompt and unseen works; unit 5 is assessed by its own
  show and sitting.
- Level 2 mid-year (day 237): unit 7's ids on unseen work; the Cr1.1 item (unit 8's id) poses a new problem from a
  different piece of the student's own Level 1 portfolio than the one used in unit 8, so it draws on earlier content
  and keeps the id's own-work part.
- Level 2 year-end (day 319): units 7 to 9's ids on unseen cases, problems and works.
- Level 3 mid-year (day 397): unit 12's ids on unseen works and an unseen case; the Cr1.2 item (unit 13's id) takes
  its theme from unit 12 (the pattern-study era or the student's unit 12 theme), not unit 13's change and community.
- Level 3 year-end (day 479): units 13 and 14's ids on unseen works.
- Level 4 mid-year (day 559): new evidence only: a fresh timed study in pencil or a dry medium for the series' next
  work with a written revision decision (Cr2.1, Cr3.1), and a defense of one of two given readings of a unit 16 work,
  Monet's Stacks of Wheat or Ojih Odutola's series (Re8.1, Re9.1); the series scored on day 528 and the essay are
  not scored again.
- Level 4 year-end (day 639): a written plan for continuing the series and a defended change on one exhibited piece
  (Cr1.2, Cr3.1), and an unseen sharing case (Cr2.2, unit 18).

| Level | Check | Course days | Level week | Codes sampled |
|---|---|---|---|---|
| 1 | Mid-year | 79, 80 | 16 | Cr2.1, Cr2.2, Re7.2 (`.Ia`), items from unit 2 |
| 1 | Year-end | 159, 160 | 32 | Cr1.1, Cr3.1, Re8.1, Re9.1, items from units 3 and 4 |
| 2 | Mid-year | 237, 238 | 16 | Cr2.1, Re7.2, Cr1.1 (`.IIa`); the Cr1.1 item is a new problem from another Level 1 piece of the student's own |
| 2 | Year-end | 319, 320 | 32 | Cr2.2, Cr1.2, Re8.1, Re9.1, items from units 7 to 9 |
| 3 | Mid-year | 397, 398 | 16 | Re7.2, Cr2.2, Cr1.2 (`.IIIa`); the Cr1.2 item is a plan for a new theme drawn from unit 12 |
| 3 | Year-end | 479, 480 | 32 | Cr1.1, Re8.1, Re9.1, items from units 13 and 14 |
| 4 | Mid-year | 559, 560 | 16 | Cr2.1, Cr3.1, Re8.1, Re9.1 (`.IIIa` again), on a fresh study and a unit 16 work |
| 4 | Year-end | 639, 640 | 32 | Cr1.2, Cr3.1, Cr2.2 (`.IIIa` again), on a continuation plan and a defended change |

**Owned codes no course-level check samples, and why** (rule 3). In each of Levels 1 to 3: Pr4.1, Pr5.1, Pr6.1
and Cn11.1 are assessed by the curating unit's own show and sitting on level days 155 and 156, three days before
the year-end check; a check cannot hang a show again, and a fresh Cn11.1 item would repeat the sitting just given.
Cr2.3 and Cn10.1 are a model and a dated log or research page built over a unit, scored from kept work. Re7.1 rests
on a hypothesis or reaction page kept over the unit. Level 1 also leaves Cr1.2 (a sustained study, kept work);
Level 2 leaves Cr3.1 (the draft-and-final pair, kept on level days 73 and 74, four days before the check); Level 3
leaves Cr2.1 and Cr3.1 (the series and defended statement, kept). Level 4 claims no id; its checks take new evidence
(a fresh study, a plan, a defended change, a reading), never the series or the essay scored again. The frame's
table sets these samples (its Level 4 rows changed with this scope, finding 1 of the expert read).

**Calendar.** Checks sit in weeks 16 and 32 of every level, as the frame and CALENDAR.md rule 4 set (week 32 is
the 9 to 12 finals week). Grades 9 to 12 have no stagger rule beyond the finals week, so the course breaks none.

## Shorter path

**The 80-day path (a semester or a rotation), per the frame.** Each level runs 80 days: Level 1 units of 6, 15, 16,
20 and 19; Levels 2 and 3 of 3, 16, 17, 20 and 20; Level 4 of 25, 14, 19 and 18; each check keeps one check day
and one respond day. Checks fall in week 8 and week 16 (the half-year finals week); in Level 4 the first two units
fill 39 days, so it checks on day 40 and responds on day 41. Merges are picked by one rule: a merged day holds at
most one first teaching of a technique or hazard card; it joins making sessions (the rest become sketchbook time),
fluency days and revision days around it; check, respond and critique days never merge, and a revision day keeps its
revision; where day 1 (the hook) and day 2 merge, day 2's retrieval moves to the next short day's opener, so the
hook stays clean. Two units stand apart. Units 6 and 11 (review) merge 1+2+3+4 with no first teaching: the
stations are review, and on the short path the placement checklist is filled from work the student brings before
the level opens (the frame's "brought work" route), so no making task is squeezed in. Unit 1 (the bridge) teaches
six grade 8 techniques in days 1 to 9 again and has 3 short days for them inside the bar's 10 percent cap; its
merges keep one material family a day, dry before wet (value in pencil and charcoal with the charcoal hazard card;
contour, gesture and perspective in pencil; the color wheel with wet clean-up and the looking routine), two re-taught
techniques a day at most; see For the lead 3.

| Unit | Short days | Days merged |
|---|---|---|
| 1 | 6 | 1+2+3+4; 5+6+7; 8+9 |
| 2 | 15 | 1+2; 3+4; 5+6; 7+8+9; 10+11+12; 13+14+15; 18+19+20+21; 23+24+25; 26+27+28+29 |
| 3 | 16 | 1+2; 3+4; 5+6+7+8; 9+10; 11+12+13; 14+15+16; 19+20+21; 23+24+25+26; 27+28+29+30 |
| 4 | 20 | 1+2; 4+5; 6+7+8; 9+10+11; 12+13; 14+15+16; 17+18+19; 22+23; 24+25; 27+28; 29+30+31; 32+33+34; 35+36+37 |
| 5 | 19 | 1+2; 3+4; 5+6+7; 8+9; 10+11+12; 13+14; 15+16+17+18; 22+23+24; 25+26+27+28; 30+31; 32+33+34 |
| 6 | 3 | 1+2+3+4 |
| 7 | 16 | 1+2; 4+5; 6+7; 8+9+10; 11+12+13; 14+15+16; 19+20+21+22; 24+25+26+27; 28+29+30+31 |
| 8 | 17 | 1+2+3; 4+5; 6+7+8; 9+10+11; 12+13+14; 15+16+17; 20+21; 23+24+25; 26+27+28; 29+30+31+32 |
| 9 | 20 | 1+2; 3+4; 5+6; 7+8; 9+10+11; 12+13+14; 15+16; 17+18+19; 22+23; 24+25+26; 28+29; 30+31; 32+33+34; 35+36+37 |
| 10 | 20 | 1+2; 3+4; 5+6; 7+8; 9+10; 11+12+13; 14+15+16; 17+18+19; 22+23; 24+25; 27+28+29; 30+31+32; 33+34+35+36 |
| 11 | 3 | 1+2+3+4 |
| 12 | 16 | 1+2; 3+4; 5+6; 7+8; 9+10; 11+12+13; 14+15+16; 19+20+21+22; 24+25+26+27; 28+29+30+31 |
| 13 | 17 | 1+2; 3+4; 5+6+7; 8+9; 10+11+12+13; 14+15+16+17; 22+23+24; 25+26+27+28; 29+30+31+32 |
| 14 | 20 | 1+2; 4+5; 6+7; 8+9; 10+11+12; 13+14; 15+16; 17+18+19; 22+23+24+25; 27+28; 29+30+31; 32+33+34; 35+36+37 |
| 15 | 20 | 1+2; 4+5; 6+7; 8+9+10; 11+12+13; 14+15+16; 17+18+19; 22+23; 24+25; 27+28+29; 30+31+32; 33+34+35+36 |
| 16 | 25 | 1+2; 4+5; 6+7; 8+9; 12+13; 14+15; 16+17; 18+19+20; 21+22+23; 24+25+26; 27+28+29; 32+33; 34+35; 36+37+38; 39+40+41; 42+43+44; 45+46+47 |
| 17 | 14 | 1+2; 3+4; 5+6+7; 8+9+10; 11+12+13; 16+17; 19+20+21; 22+23+24+25 |
| 18 | 19 | 1+2; 4+5; 6+7; 10+11+12; 13+14+15; 16+17+18; 19+20+21; 22+23+24; 27+28+29; 30+31+32; 33+34+35; 36+37+38 |
| 19 | 18 | 1+2; 3+4; 5+6; 7+8; 9+10+11; 12+13+14; 17+18+19; 20+21+22; 23+24+25; 26+27+28; 33+34+35; 36+37+38 |

Where three or four making sessions join, the short path keeps one session in class and the rest become the
student's own sketchbook time; the unit plan says which. A baseline day that merges keeps its baseline look. The ids, the critique, the revision, the mid and end
days and the respond days all stay.

**A year about 10 days short.** Ten named Fluency days per level fold into the next day's opener: each fold-in
saves 35 of its 45 minutes (10 minutes of its practice move to the next day's opener), nothing on it is assessed
and no owned part is cut. Each level then runs 150 of its 160 days (600 of 640 over the band). On that year the checks fall on level days
149 and 150. No fold-in day carries a baseline look.

| Level | Fold-in course days (unit.day) |
|---|---|
| 1 | 23 (2.11), 33 (2.21), 55 (3.11), 69 (3.25), 90 (4.10), 96 (4.16), 105 (4.25), 134 (5.14), 137 (5.17), 144 (5.24) |
| 2 | 177 (7.11), 187 (7.21), 211 (8.11), 226 (8.26), 250 (9.12), 263 (9.25), 286 (10.8), 292 (10.14), 295 (10.17), 306 (10.28) |
| 3 | 337 (12.11), 348 (12.22), 370 (13.10), 387 (13.27), 407 (14.9), 415 (14.17), 423 (14.25), 447 (15.9), 455 (15.17), 467 (15.29) |
| 4 | 496 (16.16), 503 (16.23), 516 (16.36), 523 (16.43), 542 (17.12), 574 (18.14), 592 (18.32), 608 (19.8), 612 (19.12), 621 (19.21) |

**Senior calendar.** Any level may be taken in grade 12 (Levels 3 and 4 most often), and seniors often finish
early. The show, critiques, revisions, checks, respond days and baseline days never fold.

| Level | Finish by level day 155 (four fold-ins and one merged making pair) |
|---|---|
| 1 | Fold 134, 137, 144, 153 (unit 5's practice items move to day 154's opener); merge 147+148 |
| 2 | Fold 286, 292, 295, 306; merge 302+303 |
| 3 | Fold 447, 452, 455, 467; merge 462+463 |
| 4 | Fold 496, 503, 516, 523, 542 (five fold-ins, all Level 4 studio drills or essay fluency) |

In Levels 1 to 3 the show then falls on level day 150, its sitting on 151, the respond days on 152 and 153, and the
year-end check on 154 and 155; in Level 4 the exhibit opens on level day 144 and the check moves up by five. To
finish by level day 150, fold the level's remaining fold-in days from the 10-days-short row above and merge further
making pairs in the curating unit by the same rule (Level 4: all ten fold-ins, the exhibit on level day 139). The
expert read's Level 1 and Level 3 lists named days 125 and 443; those now carry baseline looks, so days 153 and 452
fold in their place.

## Logic model (one page)

- **Inputs:** a 45-minute lesson a day, five a week; step cards, work cards, hazard cards, readings, case cards;
  found and low-cost materials with a free path on every unit.
- **Activities:** technique taught in steps before the making that needs it; works and exhibitions studied with
  their settings; making with one critique and a revision; a show each level.
- **Outputs:** a portfolio of four to five pieces a level with reflections and artist statements; a show a level;
  two marks a unit per student on the main look-for (the baseline look and the end).
- **Outcome claimed:** met marks on the level's 15 ids and growth on the look-fors. Nothing here has been tried with
  students, and Curio Class claims no effect of arts study on any other result.

## Two levels in one room (Cory, 2026-11-26, Desk q-frames-arts-1 and q-va-levels-1)

Levels 1 and 2 may share a room: each level keeps its own units and ids, and the paired units share the opening
look (day 1) and the critique day. Level 1 runs a few days behind because the bridge is 12 days and the review
units 6. Shared critique days, by level day: units 2 and 7 (34 and 29), 3 and 8 (66 and 62), 4 and 9 (106 and
105), 5 and 10 (149 and 144). Shared opening days: units 2 and 7 at level days 13 and 7, 3 and 8 at 45 and 41, 4
and 9 at 81 and 79, 5 and 10 at 121 and 119. Where the days differ, the teacher holds the joint critique on the
later level's day and the earlier level makes in that slot; the unit plans mark these shared days, as the frame
asks.

Levels 2 and 3 may also share a room, by the same rule (Cory, 2026-11-26, Desk q-va-levels-1): each level keeps its
own units and ids, and the paired units share the opening and critique days. The pairs line up almost exactly: shared critique days units 7 and 12 (29 and 29), 8 and 13 (62 and
61), 9 and 14 (105 and 104), 10 and 15 (144 and 144), and Levels 2 and 3 open on the same level days.

## For the lead

1. **Level 4 readiness day.** The frame puts a returning student's 10-minute readiness check on unit 16's day 2;
   the gate allows readiness only on the previous unit's last day or a respond day just before. Since a student who
   skipped a year is not in the room on course day 480, the check stays in day 2's note with no `assess` value,
   done while the class does the retrieval opener. Settled by the expert read (2026-11-26): kept there.
2. **Processes in every unit.** Settled by the lead (2026-11-26): each level must hold all four processes, a unit
   need not. Units 5, 10 and 15 keep their frame processes (presenting and connecting, responding practiced); unit
   17 gains a creating moment on day 7 and unit 19 a series studio day (day 35), both inside their days.
3. **Short-path merges.** The merges now follow one rule (Shorter path). Two units are open picks for the lead.
   Unit 1: its six re-taught grade 8 techniques need 9 short days to hold one a day, but the bar's 10 percent cap
   allows the bridge 8 of 80; the scope keeps the frame's 6 with two re-taught techniques a day at most. The lead
   may instead cut contour and gesture and the color wheel from the short-path bridge and teach each at its first
   need in units 2 and 3. Units 6 and 11: the scope keeps 3 short days with the checklist from brought work; the
   lead may instead give each 4 short days (units 7 and 12 at 15).
4. **Two levels in one room.** Levels 1 and 2: decided by Cory (2026-11-26, Desk q-frames-arts-1), see that
   section; the Level 1 offset (up to 5 days) comes from the bridge's 12 days against the review units' 6. Levels 2
   and 3: decided by Cory (2026-11-26, Desk q-va-levels-1), by the same rule; see that section.
5. The frame's own For the lead items 1 to 8 (check weeks, level rows, blades, two levels, the STANDARD 3.4 row,
   the stale ADOPTION-BAR line, the $150 supplies ceiling, facts to confirm) stand; nothing here changes them.
