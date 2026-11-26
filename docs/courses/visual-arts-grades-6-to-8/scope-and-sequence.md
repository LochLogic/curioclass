# Scope and sequence: Visual Arts, grades 6 to 8

Course `visual-arts-grades-6-to-8`, grades 6 to 8, scope stage draft (2026-11-26; fix pass 2026-11-26 after the expert read, docs/reviews/sequence-visual-arts-grades-6-to-8-fixes-2026-11-26.md). Frame: docs/courses/visual-arts-grades-6-to-8/frame.md. Day map: data/plans/visual-arts-grades-6-to-8/days.csv (192 rows).

## How the course runs

- **Three years in one file.** Year 6 is course days 1 to 64, year 7 days 65 to 128, year 8 days 129 to 192. Each year has 60 unit days, two course-level check days and two respond days, on two 40-minute sessions a week for 32 weeks.
- **Which NCAS grade falls in which year.** Year 6 teaches and assesses the grade 6 performance standards (the 15 `VA:...6a` codes), year 7 the grade 7 standards (`.7a`) and year 8 the grade 8 standards (`.8a`): 45 codes, every one owned by a unit and assessed (STANDARD.md 3.2).
- **Rotations.** A daily rotation with at least 64 meetings runs the full path in order. A quarter rotation (about 40 meetings) runs the marked 32-session path (the once-a-week merges named in each unit), keeping every unit, assessment, critique, revision and respond session. The school places its course checks on its rotation calendar.
- **Mixed-grade classes.** A class that mixes grades 6 to 8 runs one year's units for the whole class (year 6 in a school's first year, then 7, then 8, then back to 6), and each student's record is kept against the year being taught. The retrieval openers carry a ten-minute reteach for a student new to the band, so a grade 8 student who arrives in a year 6 cycle is never behind on routines.
- **How `school_day` is counted.** `school_day` counts school days across the whole band, 160 per year: year 6 is school days 1 to 160, year 7 is 161 to 320, year 8 is 321 to 480 (this is how scripts/frame.py reads it). The formula, stated once: course day n of year y (y = 0 for year 6, 1 for year 7, 2 for year 8; n = 1 to 64 inside the year) sits on school day 160 x y + ceil(2.5 x n), so the course meets on the third and fifth school day of each five-day week and course day n of a year falls in week ceil(n / 2) of that year; the week is (school_day - 1) // 5 + 1, counted band-wide (subtract 32 for year 7, 64 for year 8). The filled `school_day` is the one frame.py reads; data/plans/calendar.csv is regenerated from it by the lead. The checks land on school days 83 and 85 (week 17) and 158 and 160 (week 32) of each year, as the frame and docs/courses/CALENDAR.md set.
- **Calendar.** In grades 6 to 8 the arts electives count as one course against the stagger (CALENDAR.md rules 1 and 3). The mid-year check sits on school day 83 of each year, where no core course of grades 6 to 8 checks; health 6 to 8 checks on day 84 and physical education in weeks 15 and 16. The year-end check is in week 32, the finals week. `python -X utf8 scripts/frame.py calendar` on this file: 0 failures for this course, no stagger break (2026-11-26, after the fix pass).
- **Readiness.** No unit needs a readiness check: every unit's assumed rows were last used one grade back (the grade 5 rows for year 6, the band's own year before for years 7 and 8), so each is retrieved in the unit's second-day opener (the `retrieves` column), never on day 1. A row last used two grades back would get a readiness check; none is.
- **The four processes.** Every year touches all four artistic processes (creating; presenting; responding; connecting), the bar's criterion 1, and each unit touches at least the processes the frame's Units table names for it. A unit need not claim all four; where a unit practices a process it does not own (the show units' making, a response slot on a showing day), it is practice on an existing day that claims no id outside the unit's owned rows. Each unit's "Four processes" line names the days; a respond day (the day kind for a second try) is listed apart and is not counted as the responding process.
- **The day 1 rule.** Each unit's day 1 is its hook and question only.
- **Equipment and safety.** Each day's equipment, safe use of space and free path are named in its note (no supply columns, which are math and science only). The supply ceiling is the frame's (see For the lead).

### Logic model (one page)

| Inputs | Activities | Outputs | Outcome sought |
|---|---|---|---|
| Two 40-minute sessions a week for three years; one art teacher; graphite, charcoal, chalk pastel, watercolor, water-based ink, foam relief plates, cardboard, collage paper, mount card and markers within the frame's ceiling, with a free path for each; Curio Class work cards, step cards, criteria sheets and record sheets; open-access and public domain works, and museum and maker pages read first | Hooks on real works from many places; step-taught techniques before each making; drills with partner feedback; long making with daily evidence; critique (describe, ask, suggest) and a revision before every end-of-unit assessment; a showing in every unit; written looks, analyses and judgments with evidence; retrieval openers; course-level checks twice a year | Per year: four finished portfolio pieces with one-line reflections, kept cards (test sheet, waste audit, planning page, design note, display plan, process log, sharing plan, criteria card, gathering record, checklist, risk log, source labels, group plan, jury card); four showings; four end-of-unit records and two course-level checks | A student who leaves grade 8 makes work from their own inquiry over several sessions, chooses and controls materials with care for people and place, reads and judges any work with evidence from the work and its setting, and plans and hangs a show that guides its viewers, across the 45 grade 6 to 8 standards |

Nothing here has been tried with students, and Curio Class makes no claim that arts study raises any other result (the frame's logic model; APPROACH "Sources").

## Year 6 (grade 6 standards, 15 ids)

### Unit 1. Value and the world's ways of life (days 1 to 16, weeks 1 to 8)

- **Arc.** Lawrence's Street to Mbari opens how a work shows a people's life; graphite value is taught in steps, then new materials on a test sheet, a still life from observation, WPA posters for persuasion, and a hallway showing. A one-week studio waste audit (days 2 to 4) sets the class's one environmental change for the year.
- **Why here.** Value and studio routine come first because every later unit uses them; the look at how people live builds on the grade 5 look at cultural links.
- **Assessments.** Baseline look day 3; end-of-unit day 15 (VA:Re7.1.6a, VA:Re7.2.6a written; VA:Cr2.1.6a, VA:Cr2.2.6a from the kept test sheet, log and waste card); respond day 16.
- **Retrieval.** Day 2 opener retrieves va-g5-look and va-g5-craft (last used grade 5).
- **Four processes.** Create 2 to 4, 6 to 8, 10 to 12; present 13; respond 1, 5, 9, 11, 13 to 15; connect 1, 2, 4, 5, 9, 12, 14; respond day 16. Critique day 11, revision day 12, before the showing and the check.
- **Candidate.** Kept: a work of daily life in Oceania or Southeast Asia, day 14, inside the unit's 16.
- **Once a week (8 sessions).** Check and respond stay whole; 1 and 2, 3 and 4, 5 and 6, 7 and 8 merge in pairs; 9 to 11 merge (day 10's drill is day 11's opener, with the critique); 12 to 14 merge (the revision, the showing, and day 14's candidate cut to a ten-minute look after the showing). No session holds more than three days, and the critique does not share a session with the revision and the showing.

### Unit 2. Ideas into collage (days 17 to 32, weeks 9 to 16)

- **Arc.** Berni's Juanito Laguna opens how a concern becomes a work; the idea swap, color schemes, Bradford's gathered sources and a planning page lead to a collage taught from Matisse's The Snail, a critique where a partner retells the work first, a revision to match intent, a statement and a showing for a partner class.
- **Why here.** Unit 1's value and routines carry into painted papers; idea-making comes before the design and judgment of unit 3.
- **Assessments.** Baseline look day 20; end-of-unit day 31 (VA:Cr3.1.6a written on the student's own collage; VA:Cr1.1.6a, VA:Cr1.2.6a from idea pages and planning page); respond day 32. Day 30 is practice for the mid-year check, nothing scored; it is dropped on the once-a-week path and the short year, never folded into a check.
- **Retrieval.** Day 18 opener retrieves va-g5-ideas and va-g5-revise; day 24 opener va-g6-craft; day 30 va-g6-look and va-g6-craft.
- **Four processes.** Create 18 to 28, 30, 31; present 29; respond 17, 21, 23, 26, 29 to 31; connect 17, 21; respond day 32. Critique day 26, revision day 27.
- **Candidate.** Dropped: an Asian collage maker; Asia is studied in units 3 and 4, and the unit has no spare day.
- **Once a week (8 sessions).** Check and respond stay whole; 17 and 18, 19 and 20, 21 and 22, 23 and 24, 25 and 26 merge in pairs; 27 to 29 become one revise-finish-show session; day 30 (practice, nothing scored) is dropped.

### Course-level check, year 6 mid-year (days 33 and 34, week 17, school days 83 and 85)

Samples VA:Cr2.1.6a (a short value study in a dry material unit 1 did not use), VA:Re7.1.6a and VA:Re7.2.6a, on unseen works. It draws on unit 1 only; unit 2's record from day 31 is carried unscored. Day 34 responds. Once a week: session 17 checks, session 18 responds.

### Unit 3. Design for a user, and judging with criteria (days 35 to 48, weeks 18 to 24)

- **Arc.** Inuit snow goggles and the Berkeley curb cut open design for users' needs; an idea wall, user interviews and a design brief come before cardboard construction; Sher-Gil's Three Girls carries context sorting and criteria with evidence sentences; a model is critiqued, revised and shown at a user fair.
- **Why here.** It needs unit 2's idea-making; its criteria and evidence sentences are needed by unit 4's source-based response.
- **Assessments.** Baseline look day 39; practice before the check: day 45's opener (a second work card, VA:Re8.1.6a, partner-marked, nothing scored); end-of-unit day 47 (VA:Re8.1.6a, VA:Re9.1.6a written; VA:Cr2.3.6a, VA:Cn10.1.6a from the kept model, note and idea card); respond day 48.
- **Retrieval.** Day 36 opener retrieves va-g5-design and va-g5-judge; day 38 va-g6-ideas and va-g6-revise (unit 2's planning page and intent check, which the unit leans on); day 41 va-g6-look.
- **Four processes.** Create 36 to 40, 42, 44, 45, 47; present 46; respond 35, 36, 41, 43 to 47; connect 35 to 38, 41, 47; respond day 48. Day 37 opens with the teacher gathering four ideas aloud before students gather their own. Critique day 44, revision day 45.
- **Candidate.** Dropped: the unit is 14 days with two products.
- **Once a week (6 sessions).** Check and respond stay whole; 35 to 37, 38 to 40, 41 to 43, and 44 to 46 merge into four sessions.

### Unit 4. Showing work and how art keeps a people's story (days 49 to 62, weeks 25 to 31)

- **Arc.** Lascaux and Leang Tedongnge open how art shows its era; keeping flat, 3D and digital work; the Seminole tribe's Ah-Tah-Thi-Ki Museum and patchwork; mounting and labels; a display plan drawn, critiqued, revised and hung for the year-end family show.
- **Why here.** The year ends with a show of the year's kept work.
- **Assessments.** Baseline look day 52; practice before the check: day 53 (the three-column chart on a second set of works, VA:Pr4.1.6a, partner-marked, nothing scored); end-of-unit day 61 (VA:Pr4.1.6a, VA:Cn11.1.6a written; VA:Pr5.1.6a, VA:Pr6.1.6a from the kept plan and response); respond day 62.
- **Retrieval.** Day 50 opener retrieves va-g5-show and va-g5-museum; day 56 va-g6-ideas and va-g6-judge.
- **Four processes.** Present 50 to 55, 57 to 61; create 55 (the display plan drawn as a design for viewers and checked on unit 3's design-brief look-for, practice of VA:Cr2.3.6a, no claim; daily evidence line on technique and change); respond 49, 51, 56, 57, 60, 61; connect 49, 51, 56, 57, 61; respond day 62. Critique day 57, revision day 58.
- **Candidate.** Kept at no day cost: the Seminole museum pages checked open and free when the unit plan is written, with a local museum named as the alternative.
- **Once a week (6 sessions).** Check and respond stay whole; 49 to 51, 52 to 54, 55 to 57, and 58 to 60 merge into four sessions.

### Course-level check, year 6 year-end (days 63 and 64, week 32, school days 158 and 160)

Samples VA:Cr1.2.6a (a new planning page for a question the student picks from three given ones or writes as their own, marked the same, so the "content that matters to you" part is carried), VA:Re8.1.6a and VA:Re9.1.6a on one unseen work. It draws on units 2 and 3; unit 4's record from day 61 is carried unscored. Day 64 responds. Once a week: sessions 31 and 32.

## Year 7 (grade 7 standards, 15 ids)

### Unit 5. Watercolor and ink over many sessions (days 65 to 82, weeks 1 to 9)

- **Arc.** The Benin plaques in three settings open how display and place change a work's value; washes in steps, Fan Kuan's layered ink, a five-session long piece with a process log, Rockwell's Freedom of Speech for audiences, the duty when sharing images online, and a classroom showing.
- **Why here.** It opens the year with the grade 7 look and craft, the base for unit 6.
- **Assessments.** Baseline look day 67; end-of-unit day 81 (VA:Re7.1.7a, VA:Re7.2.7a written; VA:Cr2.1.7a, VA:Cr2.2.7a from the piece, log and sharing card); respond day 82. Day 80 is practice, nothing scored; dropped on the once-a-week path and the short year.
- **Retrieval.** Day 66 opener retrieves va-g6-look and va-g6-craft.
- **Four processes.** Create 66 to 70, 72 to 77, 81; present 78; respond 65, 67, 71, 72, 78 to 81; connect 65, 66, 71, 76, 79; respond day 82. Critique day 72, revision day 73.
- **Candidate.** Kept: a living maker's work shown online and in a gallery, day 79.
- **Once a week (9 sessions).** Check and respond stay whole; 65 and 66, 67 and 68, 69 and 70, 71 and 72 merge in pairs; 73 to 75 merge (day 74's drill is day 75's opener); 76 and 77 merge; 78 and 79 merge (the living maker's two displays studied at the showing); day 80 (practice, nothing scored) is dropped.

### Unit 6. Perspective, aims and criteria (days 83 to 96, weeks 10 to 16)

- **Arc.** Caillebotte's Paris Street opens how a stated aim shapes a work; one-point perspective from a Curio Class diagram, a Persian or Mughal space system for contrast, LeWitt's written rules and the criteria card, strategies when stuck with Mehretu, a perspective work, and a reflection in a chosen format.
- **Why here.** Unit 5's control of materials carries into a planned work; criteria for an aim come before judging by established criteria in unit 7.
- **Assessments.** Baseline look day 84; end-of-unit day 95 (VA:Cr3.1.7a in the chosen format; VA:Cr1.1.7a, VA:Cr1.2.7a from the sketchbook and criteria card); respond day 96.
- **Retrieval.** Day 84 opener retrieves va-g6-ideas and va-g6-revise; day 92 va-g7-look and va-g7-craft.
- **Four processes.** Create 84 to 92, 94, 95; present 93; respond 83, 86, 87, 89, 90, 93 to 95; connect 83, 86; respond day 96. Critique day 90, revision day 91.
- **Candidate.** Kept at no day cost: the Persian or Mughal painting, ten minutes of day 86.
- **Once a week (7 sessions).** Check and respond stay whole; 83 and 84; 85 to 87 (day 85's drill is the opener, and the two understanding days merge, the frame's rule); 88 and 89; 90 and 91 (critique and revision); 92 to 94 (finish, the showing and the reflection formats, so VA:Cr3.1.7a is taught in its own third of a session, not the last minutes of a four-day one): five sessions.

### Course-level check, year 7 mid-year (days 97 and 98, week 17, school days 243 and 245)

Samples VA:Re7.1.7a, VA:Re7.2.7a and VA:Cr2.2.7a (a new sharing plan). It draws on unit 5 only; unit 6's record from day 95 is carried unscored. Once a week: sessions 17 and 18.

### Unit 7. Information design and judging two ways (days 99 to 112, weeks 18 to 24)

- **Arc.** Minard's map opens information read at a glance; a visual record of where people gather for art locally, hierarchy and lettering, Jaune Quick-to-See Smith's State Names, a poster-map to a whole-number scale, Mondrian judged by taste and by established criteria, and a display for the school.
- **Why here.** It uses unit 6's criteria; its gathering record feeds unit 8's venues.
- **Assessments.** Baseline look day 102; practice before the check: day 110's last 15 minutes (ideas and mood, and two judgments, on a Curio Class card, VA:Re8.1.7a and VA:Re9.1.7a, partner-marked, nothing scored); end-of-unit day 111 (VA:Re8.1.7a, VA:Re9.1.7a written; VA:Cr2.3.7a, VA:Cn10.1.7a from the record and map); respond day 112.
- **Retrieval.** Day 100 opener retrieves va-g6-design and va-g6-judge; day 104 va-g7-look; day 105 va-g7-ideas (unit 6's criteria card, which the unit uses).
- **Four processes.** Create 101 to 103, 105, 106, 108, 109, 111; present 110; respond 99, 104, 107, 108, 110, 111; connect 99 to 101, 104, 110, 111; respond day 112. Critique day 108, revision day 109.
- **Candidate.** Dropped: 14 days, two products.
- **Once a week (6 sessions).** Check and respond stay whole; 99 to 101, 102 to 104, 105 to 107, and 108 to 110 merge.

### Unit 8. Technology, venues and the ledger drawing (days 113 to 126, weeks 25 to 31)

- **Arc.** The terracotta army in pits, shows and screens opens how technology changes keeping and seeing; a Plains ledger drawing read before and after its setting card; three ways to prepare work scored on a checklist; venues compared with a born-digital work; a two-venue year-end show (wall and catalog).
- **Why here.** The year ends with a show of the year's kept work.
- **Assessments.** Baseline look day 116; end-of-unit day 125 (VA:Pr6.1.7a written; VA:Pr4.1.7a, VA:Pr5.1.7a, VA:Cn11.1.7a from the kept cards); respond day 126.
- **Retrieval.** Day 114 opener retrieves va-g6-show and va-g6-museum; day 124 va-g7-ideas and va-g7-judge.
- **Four processes.** Present 113, 114, 116 to 125; create 118 (the catalog page or storyboard laid out with unit 7's hierarchy look-for, practice of VA:Cr2.3.7a, no claim; daily evidence line on technique and change); respond 113, 115, 119, 120, 123 to 125; connect 113, 115, 121, 125; respond day 126. Critique day 120, revision day 121.
- **Candidate.** Kept at no day cost: the born-digital work as the third venue of day 119.
- **Once a week (6 sessions).** Check and respond stay whole; 113 to 115, 116 to 118, 119 to 121, and 122 to 124 merge.

### Course-level check, year 7 year-end (days 127 and 128, week 32, school days 318 and 320)

Samples VA:Cr1.2.7a, VA:Re8.1.7a and VA:Re9.1.7a. It draws on units 6 and 7; unit 8's record from day 125 is carried unscored. Once a week: sessions 31 and 32.

## Year 8 (grade 8 standards, 15 ids)

### Unit 9. Relief prints, borrowing and the projected self (days 129 to 146, weeks 1 to 9)

- **Arc.** Rigaud's Louis XIV and Wiley's Obama open the image a sitter projects; one-color then two-color relief prints with registration and a planned risk; copyright, fair use and open licenses on case cards; Cheri Samba and the settings where images sway; an edition of three with source labels and a showing.
- **Why here.** It opens the year with the grade 8 look and craft; its source labels carry into unit 11.
- **Assessments.** Baseline look day 131; end-of-unit day 145 (VA:Re7.1.8a, VA:Re7.2.8a written; VA:Cr2.1.8a, VA:Cr2.2.8a from the edition, risk log and label card); respond day 146. Day 144 is practice, nothing scored; dropped on the once-a-week path and the short year. The risk log carries the planned risk and one thing invented (days 134, 140), and the day 145 look-for names both, so all of VA:Cr2.1.8a (try, invent and risk) is met.
- **Retrieval.** Day 130 opener retrieves va-g7-look and va-g7-craft.
- **Four processes.** Create 130 to 136, 138 to 141, 145; present 143; respond 129, 137, 139, 142 to 145; connect 129, 130, 132, 133, 137, 142; respond day 146. Critique day 139, revision day 140.
- **Candidate.** Kept: a living maker's self-portrait from Asia or Latin America, day 142.
- **Once a week (9 sessions).** Check and respond stay whole; 129 and 130, 131 and 132, 133 and 134, 135 and 136 (day 135's drill is the opener), 137 and 138, 139 and 140 merge in pairs; 141 to 143 merge (day 142's candidate cut to a ten-minute look at the showing); day 144 (practice, nothing scored) is dropped.

### Unit 10. The figure, the record and group inquiry (days 147 to 160, weeks 10 to 16)

- **Arc.** Leonardo's notebooks open the record of early steps; gesture and proportion; Do Ho Suh and a group inquiry into a shared school space; criteria for unfinished work and a written revision plan; a showing for a partner class.
- **Why here.** It builds on unit 9's risk log as the record page; its group inquiry is the subject of unit 11's zine.
- **Assessments.** Baseline look day 149; end-of-unit day 159 (VA:Cr3.1.8a written on a Curio Class unfinished work; VA:Cr1.1.8a, VA:Cr1.2.8a from the record and group plan card); respond day 160.
- **Retrieval.** Day 148 opener retrieves va-g7-ideas and va-g7-revise; day 151 va-g8-craft; day 158 va-g8-look and va-g8-craft.
- **Four processes.** Create 148 to 156, 158, 159; present 157; respond 147, 150, 154, 155, 157 to 159; connect 147, 150, 151; respond day 160. Critique day 155, revision day 156.
- **Candidate.** Dropped: 14 days with a group inquiry.
- **Once a week (7 sessions).** Check and respond stay whole; 147 and 148, 149 and 150, 151 and 152, 153 and 154 merge in pairs; 155 to 157 merge; day 158 (practice, nothing scored) is dropped: five sessions.

### Course-level check, year 8 mid-year (days 161 and 162, week 17, school days 403 and 405)

Samples VA:Re7.1.8a, VA:Re7.2.8a and VA:Cr2.2.8a (source labels on a given collage). It draws on unit 9 only; unit 10's record from day 159 is carried unscored. Once a week: sessions 17 and 18.

### Unit 11. Words and pictures, a mural and an argued judgment (days 163 to 178, weeks 18 to 25)

- **Arc.** Baca's Great Wall of Los Angeles opens art made together; Corita Kent's prints and a grid layout lead to a zine on the unit 10 inquiry; Lam's The Jungle carries a written analysis; a class mural on a shared positive theme, its panel-and-grid method shown in steps with a step card on day 168 before day 169 paints it; claim, reasons, evidence and counterclaim; a showing to the school.
- **Why here.** It needs unit 10's inquiry and unit 9's source labels; its mural is one of the works sorted in unit 12.
- **Assessments.** Baseline look day 164; two end-of-unit check days, 176 (VA:Re8.1.8a written; VA:Cr2.3.8a, VA:Cn10.1.8a from the zine, panel and group note) and 177 (VA:Re9.1.8a); respond day 178. Day 175 is practice, nothing scored; dropped on the once-a-week path and the short year.
- **Retrieval.** Day 164 opener retrieves va-g7-design and va-g7-judge; day 166 va-g8-craft; day 167 va-g8-look.
- **Four processes.** Create 164 to 166, 168 to 171, 173, 176; present 174; respond 163, 164, 167, 170, 172, 174 to 177; connect 163, 167, 168, 173, 176; respond day 178. Critique day 170, revision day 171.
- **Candidate.** Dropped: two products and a written argument fill the 16 days.
- **Once a week (7 sessions).** The two check days merge into one session (the frame's rule); respond stays whole; 163 to 165, 166 to 168, 169 to 171, 172 and 173, and 174 merge into five sessions; day 175 (practice, nothing scored) is dropped.

### Unit 12. Jurying and hanging a themed show (days 179 to 190, weeks 26 to 31)

- **Arc.** The Nation to Nation treaty exhibition opens how a show's choices influence visitors; jurying the year's work against criteria; a Robert Davidson pole and a sort of how works serve a group's identity; sequencing, sight lines and exhibition stories; the year-end and band-end themed show.
- **Why here.** The band ends with a show of the band's kept work.
- **Assessments.** Baseline look day 183; practice before the check: day 184 (two works sorted by how each serves a group's identity, VA:Cn11.1.8a, partner-marked, nothing scored); end-of-unit day 189 (VA:Pr6.1.8a, VA:Cn11.1.8a written; VA:Pr4.1.8a, VA:Pr5.1.8a from the jury card and the showing); respond day 190.
- **Retrieval.** Day 180 opener retrieves va-g7-show and va-g7-museum; day 186 va-g8-revise and va-g8-judge.
- **Four processes.** Present 179 to 181, 183 to 189; create 185 (the introduction panel laid out on unit 11's pictures-and-words grid, practice of VA:Cr2.3.8a, no claim; daily evidence line on technique and change); respond 179, 181, 182, 186, 188, 189; connect 179, 182, 184, 189; respond day 190. Critique day 186, revision day 187.
- **Candidate.** Dropped: 12 days, and the unit already reads Native-told community stories.
- **Once a week (5 sessions).** Check and respond stay whole; 179 to 181, 182 to 185 (day 184's drill is the opener), and 186 to 188 (critique, revision and hang, the family show) merge.

### Course-level check, year 8 year-end (days 191 and 192, week 32, school days 478 and 480)

Samples VA:Cr3.1.8a and VA:Re9.1.8a, with VA:Re8.1.8a folded into the argued judgment's evidence (the frame's choice). The 27-minute sitting holds a 10-minute VA:Cr3.1.8a item (two criteria applied, two changes) and a 17-minute short argued paragraph (a claim, two reasons each with evidence that names the work's subject, form or media, which carries VA:Re8.1.8a, and one counterclaim answered); it is not sized to day 177's whole-sitting model. It draws on units 10 and 11; unit 12's record from day 189 is carried unscored. Once a week: sessions 31 and 32.

## Course-level checks and rule 3

| Year | Mid-year (week 17) | Year-end (week 32) |
|---|---|---|
| 6 | days 33, 34: Cr2.1.6a, Re7.1.6a, Re7.2.6a | days 63, 64: Cr1.2.6a, Re8.1.6a, Re9.1.6a |
| 7 | days 97, 98: Re7.1.7a, Re7.2.7a, Cr2.2.7a | days 127, 128: Cr1.2.7a, Re8.1.7a, Re9.1.7a |
| 8 | days 161, 162: Re7.1.8a, Re7.2.8a, Cr2.2.8a | days 191, 192: Cr3.1.8a, Re9.1.8a (Re8.1.8a folded in) |

18 of 45 owned codes are sampled on a course-level day; the 27 not sampled, and why (each is assessed in its own unit's end-of-unit record; naming them with the reason is enough where the frame's check table limits the sample):

| Codes | Why not sampled |
|---|---|
| Cr2.1.7a, Cr2.1.8a; Cr2.3.6a, Cr2.3.7a, Cr2.3.8a; Cr1.1.8a | Multi-session products (a five-session piece, an edition, a model, a map, a zine, a record over three sessions): a 27-minute sitting cannot hold them. Cr2.1.6a is sampled because a short value study can. |
| Cn10.1.6a, Cn10.1.7a, Cn10.1.8a; Cr1.1.6a; Cr1.2.8a | Group or gathered work (idea wall, gathering record, mural, idea swap, group inquiry) that one student cannot redo alone at a sitting. |
| Pr4.1, Pr5.1, Pr6.1, Cn11.1 in all three years | The show units sit right before each year-end check; their records are taken days before and carried unscored rather than re-asked, and Pr5.1 is the hang itself. |
| Cr2.2.6a; Cr3.1.6a, Cr3.1.7a; Cr1.1.7a | The three-item limit: each check holds three codes, chosen by the frame. Cr2.2.6a's waste audit and the reflections need the student's own kept work. |

## Leans on other courses

| Day | Lean | Taught there before |
|---|---|---|
| 43 | Argument writing for evidence sentences | ELA grade 6 unit 2, school days 33 to 58 (art day 43 is school day 108) |
| 49 | Early humans and cave art dates | Social studies grade 6 (world-geography-and-ancient-civilizations-i) unit 2, school days 11 to 25 |
| 105 | Whole-number scale | Math grade 7 unit 1 scale drawings, school days 1 to 12 |
| 172 | Claim, reasons, evidence, counterclaim | ELA grade 8 unit 2, school days 31 to 62 |

Each lean still carries its own frame or step card, and the item never scores the other course's skill.

## Shorter path

- **Shorter periods.** A 30-minute session keeps the day's order and drops the opener's drill first, then shortens the making. A check day runs self-check on the session before, then set-up 2, sitting 25, collecting 3; every prompt per part is kept and sized to the 25 minutes.
- **Once a week.** The frame's path: 32 sessions a year (year 6: 8, 8, 6, 6; year 7: 9, 7, 6, 6; year 8: 9, 7, 7, 5), the mid-year check in session 17 and its response in 18, the year-end check in 31 and its response in 32. Each unit's merges are named in its section: check and respond days stay whole (unit 11's two check days merge into one); drills fold into the making they serve; the showing joins the last making day. A practice day marked "nothing scored" (days 30, 80, 144, 158, 175) is dropped, never folded into a check day, which has only 2 spare minutes; no session holds more than three days (units 3 and 7 keep their three-day critique, revision and showing session, as the expert read settled).
- **A year 10 school days short.** At two sessions a week that loses 4 sessions a year (160 minutes). Four named days a year come out, 64 days become 60, and no assessed day is touched: drill days fold into the day after them, and practice days marked "nothing scored" are dropped, never folded into a check. None of these days holds a unit's baseline look (days 3, 20, 39, 52, 67, 84, 102, 116, 131, 149, 164, 183), so no rotating group goes unobserved:
  - Year 6: days 10 (value drills into 11), 24 (collage drills into 25), 30 (practice, dropped), 53 (label drills into 54; its chart practice moves to 54's opener).
  - Year 7: days 74 (wash drills into 75), 80 (practice, dropped), 103 (lettering drills into 104), 117 (mount drills into 118).
  - Year 8: days 135 (registration drill into 136), 144 (practice, dropped), 165 (grid drills into 166), 175 (practice, dropped).

## For the lead

1. **Day 83 is shared.** The mid-year check sits on school day 83 of each year with no core check; health 6 to 8 checks on day 84 and physical education in weeks 15 and 16. If a school's electives rotate across days, the check still holds week 17.
2. **Rule 3 unsampled codes.** 27 of 45 owned codes are not sampled on a course-level day (table above, with reasons). Each is assessed in its unit. Any frame change to widen the sample is proposed in the fix report, not here.

## For Cory

- **Supplies ceiling (money).** Decided at $100 a class of 30 a year (Cory approved 2026-11-26, Desk q-frames-money-1), every unit keeping its free path (provisional costs $60, $70 and $100 by year; year 8's print unit carries brayers and block ink). This plan's materials (graphite, charcoal, chalk pastel, watercolor, water-based ink, foam plates, mount card, markers) fit inside it, each with a free path in its note.
