# Scope and sequence: Visual Arts, grades K to 2

Course `visual-arts-grades-k-to-2`, a band course for kindergarten, grade 1 and grade 2. Draft, written 2026-11-26
from the frame (docs/courses/visual-arts-grades-k-to-2/frame.md). The days are in
data/plans/visual-arts-grades-k-to-2/days.csv; this page holds the judgment.

## The band, the standards and the calendar

- **Three years, one file.** The band runs as three years one after another: year K (course days 1 to 64), year 1
  (days 65 to 128) and year 2 (days 129 to 192). Each year has four units, two course-level check days and two
  respond days: 60 + 4 = 64 days a year, 192 in all. The `stretch` column is the unit number in the frame's Units
  table (units 1 to 4 in year K, 5 to 8 in year 1, 9 to 12 in year 2).
- **Which grade's standards fall in which year (STANDARD.md 3.1).** Year K claims only the 15 kindergarten visual
  arts ids (`.Ka`), year 1 only the 15 grade 1 ids (`.1a`), year 2 only the 15 grade 2 ids (`.2a`): 15 a year, 45
  in all, the count in STANDARD.md 3.2. Every one is taught and assessed in its own year. A year revisits the year
  before's ids only as practice that returns (the retrieval openers), never as a claim. No pre-kindergarten id is
  claimed.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a child's record shows which grade's standards they met. A child who meets
  year 2 before year 1 gets each retrieval opener's ten-minute reteach as written.
- **Meeting days and `school_day`.** The course meets two 40-minute sessions a week over 32 weeks a year, 96 weeks
  across the band. `school_day` is counted across the whole band as 160 school days a year: course day n of year y
  (y = 0 for K, 1 for grade 1, 2 for grade 2; n = 1 to 64 inside the year) sits on school day 160 x y + ceil(5n / 2),
  so two days fall in every five-school-day week, on the week's third and fifth school days, and course day n of a year falls in week ceil(n / 2) of that year, as the frame and docs/courses/CALENDAR.md give.
  This is the calendar's even spread; no pins are used. The count runs across the whole band (year 1 is school days
  161 to 320, year 2 is 321 to 480), as frame.py reads it. A filled `school_day` is what frame.py reads first, so it
  is not re-counted to match calendar.csv; every unit and check sits in the frame's weeks by week =
  (school_day - 160 x y - 1) // 5 + 1, checked by script on all 192 days.
- **Session minutes.** Each day's note names the session type: a paint or clay session holds set-up 5 minutes and
  clean-up and collecting 7; a drawing or talk session holds set-up 5 and clean-up 4. A retrieval opener takes ten
  minutes. Check days carry no paint or clay.
- **The four processes.** Every day's note opens with the processes it works on (create; present; respond;
  connect). Each year holds all four artistic processes, and each unit touches at least the processes the frame's
  Units table names for it (the frame's rule: at least two). A unit need not claim all four, and no day claims an id
  outside its unit's owned rows: where a unit practices a process it owns no id for (a work's setting told on a work
  card, a short response), the label marks practice, not a claim. The days are listed in each unit section below.
- **Kinds and the unit run.** As the frame's Day kinds: understanding (a technique shown in steps with the step card,
  or a work studied with the unit's words), fluency (short drills of a taught technique), application (making with
  some choice; the second making day holds the unit's one critique in the critique routine (describe, ask, suggest),
  the one name used from K to 12, with its two rules from day 15 on: critique the work, never the person; praise
  alone is not feedback; the next day revises),
  check, respond. Technique days always come before the making that needs them. Each unit opens with a baseline look
  at its main look-for on the first fluency or making day (not scored), and one piece a unit goes into the portfolio
  folder with a spoken one-line reflection.
- **Readiness and retrieval.** Year K assumes no earlier art row (pre-kindergarten ids are not taught), so year K
  has no readiness check. Every year 1 and year 2 unit assumes the year before's row in the same thread, last used
  one grade back, so each opens with a ten-minute retrieval task inside its day 2 opener (the `retrieves` column),
  never a readiness check, and each unit's day 1 stays clean for the hook and the compelling question. No row of this
  band is two grades idle when a unit needs it, so the course has no `readiness` day. Same-year rows also return in
  openers, each in the `retrieves` column (for example unit 2's day 20 brings back unit 1's safe paint pick, unit 6's
  day 85 unit 5's line family, and the rows the frame's "Why this unit, here" names: day 39 va-k-look, day 103
  va-g1-revise, day 165 va-g2-ideas, day 168 va-g2-look).
- **Earlier-grade rows, last use and treatment (rule 2, re-run 2026-11-26).** Each row's `assumes` cell is its own
  thread one grade back. va-k-look, va-k-craft: last used year K, retrieved day 66. va-k-ideas, va-k-revise: year K,
  retrieved day 84. va-k-design, va-k-judge: year K, retrieved day 102. va-k-show, va-k-museum: year K, retrieved day
  118. va-g1-look, va-g1-craft: year 1, retrieved day 130. va-g1-ideas, va-g1-revise: year 1, retrieved day 146.
  va-g1-design, va-g1-judge: year 1, retrieved day 164. va-g1-show, va-g1-museum: year 1, retrieved day 182. No year 2
  unit leans on a year K row, so no readiness check is owed.
- **Cross-subject.** No row carries a cross-subject lean, so no bridge is owed. The frame's practiced contacts are
  carried in the notes: shapes named by pointing (kindergarten math names flat shapes in weeks 9 to 13; unit 1 day 11
  points without teaching counting, and unit 3 day 38 falls after math has taught them), sorting by use only (unit 7
  day 102), and the critique routine card's turn-taking pictures for ELA's collaborative conversation (unit 1 day 15, unit 10
  day 150).
- **Supplies and safety.** Each hands-on day's note names its equipment, its safe use and the free path where the
  frame lists one, in the frame's words: premixed non-toxic paint, moist clay or adult-made flour-salt dough (wheat
  allergy checked), blunt-tip scissors, blades used only by an adult, no heat source, hands washed after paint, clay
  and found objects. Every unit gets the fresh safety and sensitivity reads with its unit plan.

## Year K (kindergarten ids)

### Unit 1. Art all around us

Days 1 to 18, weeks 1 to 9 of year K. The unit opens the studio and the looking routine together: a hook on the
Great Wave and the class's own photographs of nearby art (day 1), then the set-up and clean-up routine and the safe
supply pick (day 2) before any material is handled. Each material (crayon, paint, dough, paper) is shown in steps
before it is drilled, and each look and tell on a work (Hokusai, Mahlangu, Kusama) comes between the technique days,
so the unit alternates hands and eyes and no day asks for a step not yet shown. The experiment sheet (days 14 to 16)
uses all four materials once every one has been taught; the critique is on its second making day (15), the revision
and the class gallery on day 16. It is the longest year K unit, as the frame says, because four ids, two techniques
and the studio routine are all new.

- End-of-unit assessment: day 17 (check), every owned id: Re7.1.Ka and Re7.2.Ka as talk items, Cr2.2.Ka as the tray
  table item, Cr2.1.Ka as the guide look-for on the kept experiment sheets. Response time: respond day 18.
- Processes: create 2, 4, 5, 6, 8, 9, 11, 12, 14 to 18; present 16 (the gallery); respond 1, 3, 7, 10, 12, 13, 15, 17,
  18; connect 1, 3, 10, 13 (what nearby art is for).
- Candidate settled: **kept, no added day.** The set-up and clean-up minutes in a 40-minute paint session (5 and 7)
  are timed on day 5, the first paint day, and stated on every paint day's note.
- Sensitivity: Mahlangu's Ndebele painting (day 10) is described and linked, never copied; the looking walk (day 3)
  photographs art, never faces.

### Unit 2. Playing for ideas

Days 19 to 34, weeks 10 to 17 of year K. The hook (day 19) is Kandinsky's play with color and line; mixing two
colors (day 20) and telling choices in everyday words (day 21) come next because the idea page (day 23) needs both.
The Great Wave returns beside Kandinsky (day 24) to show two ideas carried by line and color. Fold-and-stand paper
(days 25, 26) is taught before the partner problem card (day 27), which comes before the bridge making (days 28 to
30), so the partner work rests on a technique already drilled. The showing (day 31) gives the Cr1.2.Ka look-for
record; a second idea page (day 32) is the kept sketchbook evidence.

- End-of-unit assessment: day 33: Cr3.1.Ka as a talk item; Cr1.1.Ka (kept sketchbook, three tries) and Cr1.2.Ka
  (the day 31 showing record, each child's added part) as guide look-fors. Response time: respond day 34.
- Processes: create 19 to 23, 25 to 30, 32 to 34; present 31; respond 19, 24, 29; connect 19 (Kandinsky's setting),
  27 (the bridges people use and what a bridge is for).
- Candidate settled: **kept, no added day.** The doubled parent-and-child version of the partner problem card is
  part of day 27's problem card.
- The mid-year check follows (days 35 and 36, week 18).

### Unit 3. Pictures of my places

Days 37 to 50, weeks 19 to 25 of year K. Tar Beach opens the unit with a work's subject and details (day 37). The
ground line, sky band and shape buildings (day 38) are shown and drilled (day 40) before the place-story picture is
planned (day 42) or made (days 44 to 46). Judging builds in two steps: subject and details (days 37, 39), then
"I like it because" (day 41), with a fluency day (43) that joins them. The showing (day 47) puts the place-story wall
in front of a partner class, whose visitors practice the because sentence.

- End-of-unit assessment, two check days (the unit owns two products of judging and a picture): day 48 (Re8.1.Ka
  talk item; Cr2.3.Ka look-for on the picture, a natural and a built thing on its ground line) and day 49 (Re9.1.Ka talk item; Cn10.1.Ka look-for on the story in
  the picture), so each child answers one talk item a day. Response time: respond day 50.
- Processes: create 38, 40, 42 to 46, 48, 50; present 47; respond 37, 39, 41, 43, 45, 47 to 50; connect 37, 42, 44,
  49 (a story from the child's life, a story character or an invented child, marked the same).
- Retrieval: va-k-look (unit 1, same year) on day 39, since judging builds on look and tell.
- Candidate settled: **kept, no added day.** A natural-place work from outside Europe and North America is the work
  on day 41, picked by the unit plan from an open-access collection with its rights line.
- Sensitivity: Tar Beach is told as the rooftop and the family; Wiltshire is taught through his drawings; the child's
  own story is never required (days 37, 39, 42).
- The year-end check follows (days 51 and 52, week 26).

### Unit 4. Our class collection

Days 53 to 64, weeks 27 to 32 of year K. Two quilts open the unit (days 53, 54): what a quilt is for and why each is
kept. Collections and portfolios (day 55) and what a museum is (day 56) come before the frame and label technique
(day 57), which comes before the child chooses three works (day 58), frames and labels them with the critique (day
60) and revises (day 61). The year's portfolio folder is the collection, so the unit sits last in the year, after the
year-end check.

- End-of-unit assessment: day 62 (Pr5.1.Ka and Cn11.1.Ka talk items; the Pr6.1.Ka kept sort card) and day 63, the
  class collection shown to families, which is the unit's own assessment (Pr4.1.Ka look-for, the reasons noted as
  each child shows). Response time: respond day 64.
- Processes: create 57, 60 (making the border frames); present 55 to 64; respond 53, 54, 60; connect 53, 54, 62, 64.
- Candidate settled: **kept, no added day.** The museum virtual visit's free pages are checked open on the day the
  unit plan is written (day 56); the picture cards are the paper path.
- Sensitivity: the Gee's Bend quilters (day 53); works shown outside class only with the family's yes, under the
  child's chosen name (day 63).

## Year 1 (grade 1 ids)

### Unit 5. Same subject, two pictures

Days 65 to 82, weeks 1 to 9 of year 1. The studio reopens with Cassatt beside Utamaro (day 65) and, before any real
work, the safe grip and handling of each tool (day 66, with the retrieval of kindergarten look and tell and safe
supply pick). The line family is shown with crayon (day 67), drilled (68), then shown with the brush (69); printing
with found objects is shown (73) and drilled (74) before the line-and-print sheet (76 to 78). Comparison grows from two
pictures (day 70) to three (day 75), and the everyday-life description (day 71) feeds the gallery (day 79), where each
child describes a classmate's sheet.

- End-of-unit assessment: day 81: Re7.1.1a and Re7.2.1a talk items, Cr2.2.1a tray item (one tool's grip and handling),
  Cr2.1.1a look-for on the kept sheet. Response time: respond day 82.
- Processes: create 66 to 69, 72 to 74, 76 to 78, 80 to 82; present 79; respond 65, 70 to 72, 75, 77, 79 to 82;
  connect 65 (Cassatt studied Japanese prints of this kind).
- Retrieval: va-k-look and va-k-craft (last used in year K, one grade back) on day 66.
- Candidate settled: **kept, no added day.** A third picture of the same subject by a living maker, described and
  linked, is the work on day 75.

### Unit 6. Looking closely for ideas

Days 83 to 98, weeks 10 to 17 of year 1. Dürer's hare (day 83) sets the question; look, draw, look again is shown
(84) and drilled (86), and the art words line, shape, color and texture (85) are taught on top of unit 5's line
family. Rubbings (87) come before the shared material tables (89), which give the kept Cr1.1.1a page. The second
observational study (90) and Goldsworthy (88) widen what "looking closely" means before the research drawings (92)
and the finished work (93 to 95), whose critique and revision are told in art words.

- End-of-unit assessment: day 97: Cr3.1.1a talk item; Cr1.1.1a (shared-table page) and Cr1.2.1a (sketchbook research
  drawings) as look-fors. Response time: respond day 98.
- Processes: create 83 to 87, 89, 91 to 95, 97, 98; present 96; respond 83, 88, 90, 91, 94; connect 88 (art made from
  found natural material in its place).
- Retrieval: va-k-ideas and va-k-revise on day 84.
- Candidate settled: **kept, no added day.** An observational study by a maker from Asia, Africa or the Americas is
  the work on day 90, so the unit's two works are not both European.
- The mid-year check follows (days 99 and 100, week 18).

### Unit 7. Things we use, art we make

Days 101 to 114, weeks 19 to 25 of year 1. The Ming dish (101) and the Martinez jar (103) are useful objects that are
also art; the hook sorts what is in the dish (people, animals, things, plants) and day 103 adds lines, shapes and
colors after a retrieval of unit 6's art words; the sort by use (102, with the retrieval of the kindergarten "made for" card and "because") comes before the
pinch pot is shown (104) and drilled (105). Art beyond school (106) and the reasons chart (107) come before the sort
sheet (109) and the pot made to use (110, with the critique), revised and displayed on day 111.

- End-of-unit assessment, two check days (two products): day 112 (Re8.1.1a, the child sorts two or three things in
  an unseen work and then names its lines, shapes and colors; Cn10.1.1a talk item; Cr2.3.1a
  look-for on the sort sheet with the pot) and day 113 (Re9.1.1a kept reasons card). Response time: respond day 114.
- Processes: create 102, 104, 105, 109 to 111, 114; present 111; respond 101, 103, 107, 108, 110, 112 to 114; connect
  101, 103, 106, 112, 114.
- Retrieval: va-k-design and va-k-judge on day 102; va-g1-revise (unit 6, same year) on day 103.
- Candidate settled: **dropped.** A useful object from Africa: year 1 already studies an African work in unit 8 (the
  faience hippopotamus, Egypt), and the unit's three works fill its looking days.
- Sensitivity: the Martinez jar (day 103) avoids the water serpent design and no child copies a Pueblo design; art
  from the child's family is optional (day 106).
- The year-end check follows (days 115 and 116, week 26).

### Unit 8. At the museum

Days 117 to 128, weeks 27 to 32 of year 1. The hippo known as William (117) asks why a museum prizes a very old
object; museum jobs follow (118, with the retrieval of the kindergarten collection and museum), then the alebrije
(119) for reasons across two times and places and the question "why would a museum keep this alebrije, made today,
beside William?", so Pr4.1.1a is taught past the hook and drilled again on day 122 ("which would a museum keep, and
why"). Mounting and labeling (120) and the exhibit-plan card (121, with one question the child asks of their own)
are shown and drilled (122) before each child readies a work (123 to 125). The class museum is built from the year's kept work,
so the unit closes the year after the year-end check.

- End-of-unit assessment: day 126 (Pr4.1.1a and Cn11.1.1a talk items; Pr6.1.1a kept job-card sort) and day 127, the
  class museum with children as guides, which is the unit's own assessment (Pr5.1.1a: the exhibit-plan card with the
  mounted piece, the child's own question read and answered). Response time: respond day 128.
- Processes: create 123, 124 (finishing and mounting a work); present 117 to 128; respond 119, 124; connect
  117, 119, 126, 128.
- Retrieval: va-k-show and va-k-museum on day 118.
- Candidate settled: **kept, no added day.** The job-card sort is written as the full equal of acting (day 118), and
  it is the scored form, so acting is never needed for the mark.
- Sensitivity and leave-out: William is a burial object, studied by looking only; the acting may be left out; no
  child copies a named carver's design. Leave-out (frame, a unit the course page names): leaving out the acting or
  swapping a work keeps the unit, its showing and every id; if a school or family leaves the unit out for its
  community's reasons, the course page and the family note name the ids not claimed that year: VA:Pr4.1.1a,
  VA:Pr5.1.1a, VA:Pr6.1.1a, VA:Cn11.1.1a. It is never a short-year or time cut.

## Year 2 (grade 2 ids)

### Unit 9. How places feel

Days 129 to 144, weeks 1 to 8 of year 2. Two bridges, one stormy and one calm, open the year (129), each told with
its setting. The clean-up card (130, with the retrieval of year 1's comparison and safe handling) and the looking walk
(131) come before tints and shades are shown (132) and drilled (133). The feeling sort (134) and the second look at
the two bridges (135) tie mood to tint and shade before the choice day (137). The interest the child finds on the
choice day is the subject of the mood painting (138 to 140), so the critique (139) and the revision (140) fall on the
piece that is scored; it is shown on day 141.

- End-of-unit assessment: day 143: Re7.1.2a (two looking-walk photos, one natural and one built place) and Re7.2.2a
  talk items, Cr2.2.2a table item (a brush washed by the clean-up card), Cr2.1.2a look-for on the revised mood
  painting with the choice-day work kept beside it (a material tried for the child's own interest, carried into the
  painting with tints or shades used on purpose). The day 133 baseline watches the same look-fors on the ladders.
  Response time: respond day 144.
- Processes: create 130, 132, 133, 135, 137 to 140, 142 to 144; present 141; respond 129, 131, 134 to 136, 139, 141 to
  144; connect 129 (the two bridges' settings: Hiroshige's print sold in a series of views of Edo, Monet's bridge in
  his own garden), practice only, since the frame names no connecting id for this unit.
- Retrieval: va-g1-look and va-g1-craft on day 130.
- Candidate settled: **dropped.** A third mood work by a living maker: the two bridges are the unit's paired
  comparison, the feeling sort cards supply more pictures, and year 2 meets living makers in units 10 to 12.

### Unit 10. Many ways to solve it

Days 145 to 160, weeks 9 to 16 of year 2. Asawa (145) and Clark (147) show many forms from one method. Fold and curl
(146, with the retrieval of year 1's research drawing and art words) and tab and slot (148) are shown and drilled (149)
before partners sketch many solutions (152). The two-way talk (150) is taught before it is drilled (153) and used in
the critique (155). The child's own question (151) comes before the making that follows it (154 to 156), shown on day
157.

- End-of-unit assessment: day 159: Cr3.1.2a two-way talk item with a classmate; Cr1.1.2a (three solutions) and
  Cr1.2.2a (the child's question and the work that follows it, made with two or more materials) as look-fors on the
  sketchbook and creature. Response time: respond
  day 160.
- Processes: create 145, 146, 148 to 156, 159, 160; present 157; respond 145, 147, 150, 151, 153, 155, 158; connect
  145 (Asawa's setting), 151 (a question from the child's own life or interests, or an invented one).
- Retrieval: va-g1-ideas and va-g1-revise on day 146.
- Candidate settled: **kept, no added day.** Asawa and Clark are no longer living, so a living many-solutions maker
  from Asia or Africa is the work on day 151.
- The mid-year check follows (days 161 and 162, week 17).

### Unit 11. New from old

Days 163 to 178, weeks 18 to 25 of year 2. El Anatsui (163) sets the question. Joining cast-offs (164, with the
retrieval of year 1's sort by use and sorted reasons) is shown before the "made for" plan (165) and drilled (166)
before the transformed object (167, 170); the plan opens with a retrieval of unit 10's many solutions. Meaning from
mood, subject and form (Bruegel, 168) opens with a feeling sort of known cards (unit 9's mood); preference in two art
words (172) is taught before the end-of-unit talk on it. The event scene, year 2's drawing step, is shown in named
steps on a step card with The Harvesters as the model (169: ground line raised, main people large and in front, the
action, the place behind) and drilled as a "person doing an action" drill (171) before the event picture is made
(173, 174). The unit owns two products, so its one critique falls on the object's second making day (170) and
the event picture gets partner feedback on day 174 before its revision and the "new from old" show (175).

- End-of-unit assessment, two check days: day 176 (Re8.1.2a talk item; Cr2.3.2a look-for on the object) and day 177
  (Re9.1.2a talk item; Cn10.1.2a look-for on the event picture). Response time: respond day 178.
- Processes: create 164 to 167, 169 to 171, 173 to 176, 178; present 175; respond 163, 168, 170 to 172, 174, 176 to
  178; connect 163, 168, 169, 173, 177, 178.
- Retrieval: va-g1-design and va-g1-judge on day 164; va-g2-ideas (unit 10) on day 165 and va-g2-look (unit 9) on
  day 168, same year.
- Candidate settled: **dropped.** An event picture by a living maker from Asia or Africa: El Anatsui is the unit's
  living African maker, year 2 has Asian works in units 9 and 12, and a third work would take time from the two
  products.
- Sensitivity: "bottle caps" (day 163); home events invited, never required (day 169); cast-offs cleaned, no glass or
  sharp lids, blades by an adult only (day 164).
- The year-end check follows (days 179 and 180, week 26).

### Unit 12. Art for our community

Days 181 to 192, weeks 27 to 32 of year 2. Cloud Gate (181) asks how public art helps a community; mounting, labels
and frames are told apart (182, with the retrieval of year 1's exhibit-plan card and work cards). The two cut-paper
traditions are studied on work cards (183, 184) before the theme is taught (185) and drilled (186). Each child's piece
is grouped (187, with who our exhibit is for and how it helps our school, so Pr6.1.2a's inside-school part is taught
past the hook), mounted and critiqued (188) and revised (189) for the year-end theme exhibit, which closes the band.

- End-of-unit assessment: day 190 (Pr6.1.2a talk item on Cloud Gate, a museum or the class exhibit, inside or
  outside school; Cn11.1.2a talk item with where and when each cut-paper use is found; the Pr5.1.2a kept card) and day 191, the theme
  exhibit for families, which is the unit's own assessment (Pr4.1.2a look-for). Response time: respond day 192.
- Processes: create 187, 188 (finishing and mounting a piece); present 181, 182, 185 to 192; respond 183, 184, 188;
  connect 181, 183, 184, 187, 190, 192.
- Retrieval: va-g1-show and va-g1-museum on day 182.
- Candidate settled: **kept, no added day.** Both traditions' sources are confirmed as the communities' own published
  teaching before the unit plan is written (day 183's note).
- Sensitivity and leave-out: papel picado's Day of the Dead use is ceremonial, named and studied by looking only; no
  child imitates either tradition's designs or explains their own family's culture. Leave-out (frame, a unit the
  course page names): swapping a work keeps the unit, its showing and every id; if a school or family leaves the
  unit out for its community's reasons, the course page and the family note name the ids not claimed that year:
  VA:Pr4.1.2a, VA:Pr5.1.2a, VA:Pr6.1.2a, VA:Cn11.1.2a. It is never a short-year or time cut.

## Course-level checks

Each check day: the class makes at tables with drawing tools while the teacher hears six groups of five for about
four minutes each; set-up 5 and clean-up 4. No paint or clay on a check day. Each is followed by one respond day.

| Check | Days | Week of its year | What it samples |
|---|---|---|---|
| Year K mid-year | 35 (respond 36) | 18 | Unit 1: a fresh making task in two dry media, crayon and torn paper with a glue stick, each tried two ways, with the safe supplies picked from a tray (VA:Cr2.1.Ka, VA:Cr2.2.Ka); talk items on an unseen picture (VA:Re7.2.Ka) and a new photo of nearby art (VA:Re7.1.Ka). Unit 2's day 33 record is carried unscored. |
| Year K year-end | 51 (respond 52) | 26 | A short place drawing from a new prompt drawn from unit 1's looking-walk photo cards, with a natural and a built thing in it (VA:Cr2.3.Ka), begun with three quick tries (VA:Cr1.1.Ka, unit 2), and one telling of a choice while making (VA:Cr3.1.Ka, unit 2). |
| Year 1 mid-year | 99 (respond 100) | 18 | Unit 5: a fresh print or line task (crayon rubbing over found objects or dry stamp pads) with safe handling shown first (VA:Cr2.1.1a, VA:Cr2.2.1a); a talk comparing two unseen pictures of one subject (VA:Re7.2.1a). Unit 6's day 97 record is carried unscored. |
| Year 1 year-end | 115 (respond 116) | 26 | An observational drawing of a new object (VA:Cr1.2.1a, unit 6), a talk in art words about the choices made (VA:Cr3.1.1a), and a talk on an unseen everyday-life picture (VA:Re7.1.1a, unit 5). |
| Year 2 mid-year | 161 (respond 162) | 17 | Unit 9: a picture of a subject of the child's own interest in two materials chosen from crayon, colored pencil and torn paper, light and dark made by pressure or paper choice (look-for: two materials chosen, used for the child's own subject), with the clean-up card led (VA:Cr2.1.2a, VA:Cr2.2.2a); a feeling sort of unseen pictures with reasons (VA:Re7.2.2a). Unit 10's day 159 record is carried unscored. |
| Year 2 year-end | 179 (respond 180) | 26 | Many sketched solutions to a new small problem (VA:Cr1.1.2a, unit 10), the two-way choices talk (VA:Cr3.1.2a), and a look-and-feel talk on two unseen place pictures, one natural and one built (VA:Re7.1.2a, unit 9). |

- **Checks after an end-of-unit assessment draw on earlier units.** Each check sits one or two days after a unit's
  end-of-unit assessment. The mid-year checks sample only the unit before it (unit 1, 5 or 9), whose end was 18 days
  earlier. The year-end checks sample units two back; where year K's year-end samples unit 3's own Cr2.3.Ka, its
  prompt is a place from unit 1's looking walk and its form (a short timed drawing) is not the unit 3 picture.
- **Collect once, and a change from the frame's table.** The frame's year-end rows also hear the judging talk items
  (Re8.1 and Re9.1) of units 3, 7 and 11. Those records were taken one to three days before (days 48 and 49, 112 and
  113, 176 and 177), inside the ten-day window, so sequence-write rule 2 ("Collect once") carries them and they are
  not heard again. In years 1 and 2 the freed talk slot samples Re7.1 instead, which no check otherwise reaches. The
  frame's table is corrected under For the lead.
- **Task forms.** No check repeats an item from the two weeks before: each mid-year check follows an end day of
  sketchbook look-fors and a choices talk, and each year-end check follows judging talks and product look-fors. In
  arts a making task or a showing is the discipline's own evidence and may follow a unit's; what may not repeat inside
  two weeks is the same item (the same prompt type on the same work or content). Each check is on new or
  earlier-unit work with its own items, and each check day's note says so.
- **Codes no course-level check samples (rule 3), and why.**
  - The showing units' ids, after the year-end check by the calendar (CALENDAR.md tool c, as the frame sets):
    VA:Pr4.1.Ka, VA:Pr5.1.Ka, VA:Pr6.1.Ka, VA:Cn11.1.Ka (unit 4); VA:Pr4.1.1a, VA:Pr5.1.1a, VA:Pr6.1.1a,
    VA:Cn11.1.1a (unit 8); VA:Pr4.1.2a, VA:Pr5.1.2a, VA:Pr6.1.2a, VA:Cn11.1.2a (unit 12). Each is assessed by its own
    unit's end days and showing to families.
  - Product and judging ids of units 3, 7 and 11, carried by collect once: VA:Cn10.1.Ka, VA:Re8.1.Ka, VA:Re9.1.Ka;
    VA:Cr2.3.1a, VA:Cn10.1.1a, VA:Re8.1.1a, VA:Re9.1.1a; VA:Cr2.3.2a, VA:Cn10.1.2a, VA:Re8.1.2a, VA:Re9.1.2a.
  - Partner and multi-day products that a 38-minute check cannot hold beside the table talk: VA:Cr1.2.Ka (a partner
    bridge), VA:Cr1.1.1a (a shared-table page made with classmates), VA:Cr1.2.2a (a question followed into a made
    work over several days). Their unit records stand.
- **Calendar.** All six checks sit on the frame's weeks and on CALENDAR.md's table for this course (K and 1: weeks 18
  and 26; 2: weeks 17 and 26), off every core check week of the grade. Arts are specials in K to 5 and do not count
  against the classroom teacher's stagger (CALENDAR.md rule 1).

## Logic model

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week, 32 weeks a year; step cards, work cards, problem and record sheets (Curio Class's own); found and low-cost materials, every unit with a free path | Technique taught in named steps and drilled; works from many times and places studied with their setting; making with choice, one critique and a revision each unit; a showing each unit | A portfolio folder of 12 pieces over the band, each with a spoken reflection; 12 showings; two marks a unit per child on the main look-for (baseline and check) | Met marks on each year's 15 ids, and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result.

## Shorter path

**A shorter period.** In a 30-minute session, keep set-up (5) and clean-up (4 or 7) whole and cut the teaching and
making to fit: the demonstration keeps every named step, the drill keeps one round, the critique keeps all three
moves for every pair, and a making day finishes on the next session's opener. Check days: set-up 3 and clean-up 3
(drawing tools only), the six groups at four minutes each (24 minutes), and the self-check moved to the day before:
30 minutes, so each child keeps about 48 seconds at the teacher's table.

**Once a week (32 sessions a year, the frame's path).** Every unit and id stays. Each unit keeps, in order, the
demonstration with its step card opened by a look at a work; one making day with the critique; the showing (the
check); one respond day. Fluency days fold into the openers and the two rows' understanding days merge. No merged
session drops a critique, a revision or a respond day. Sessions, as course days merged:

| Unit | Sessions | Course days in each session |
|---|---|---|
| 1 | 9 | 1+3+7; 2+4; 5+6; 8+9+11+12; 10+13; 14+15; 16; 17; 18 |
| 2 | 8 | 19+24; 20+21+22+23; 25+26+27; 28+29; 30+31; 32; 33; 34 |
| 3 | 6 | 37+39+41; 38+40+42+43; 44+45; 46+47; 48+49; 50 |
| 4 | 5 | 53+54+55+56; 57+58+59; 60+61; 62+63; 64 |
| 5 | 9 | 65+70+71+75; 66+67+68; 69+72; 73+74; 76+77; 78; 79+80; 81; 82 |
| 6 | 8 | 83+88+90; 84+85+86; 87+89+91; 92; 93+94; 95+96; 97; 98 |
| 7 | 6 | 101+103+106+107+108; 102+104+105; 109+110; 111; 112+113; 114 |
| 8 | 5 | 117+118+119; 120+121+122; 123+124+125; 126+127; 128 |
| 9 | 8 | 129+131; 130+132+133; 134+135+136; 137; 138+139; 140+141+142; 143; 144 |
| 10 | 8 | 145+147+151; 146+148+149; 150+152; 153+154; 155; 156+157+158; 159; 160 |
| 11 | 7 | 163+168+172; 164+165+166; 167+170; 169+171+173; 174+175; 176+177; 178 |
| 12 | 5 | 181+183+184; 182+185+186; 187+188+189; 190+191; 192 |

Each year adds one check session and one respond session per course-level check: years K and 1, 9 + 8 + 6 + 5 + 4 =
32; year 2, 8 + 8 + 7 + 5 + 4 = 32. The check sessions fall in the full path's weeks (18 or 17, and 26); the respond
sessions fall one week later (19 or 18, and 27). Where a unit's two end days merge (units 3, 7, 11), the session
holds the self-check and at most two talk items a child, and the kept cards and products are scored after it. The
unit 9 order keeps tints and shades (session 2) before the bridges are judged by them (session 3), and the unit 10
order keeps the sketches (session 3) before the two-way talk on them (session 4); the critique stays on day 155 and
the revision on day 156.

**The exhibit units on the once-a-week path (units 4, 8, 12).** One adult cannot host families and hear six table
groups in the same 40 minutes, so the merged end session (62+63, 126+127, 190+191) is the check only: the talk items
plus the Pr4.1 reasons heard at the teacher's table (year K, why each of the three works went in; year 1, Pr5.1.1a,
the child guides the teacher through the mounted work and its exhibit-plan card; year 2, why the piece fits its
group), scored as on the full path. The family showing is held as a drop-in gallery at arrival or pick-up, or at a
family evening, unscored; the class still shows to an audience (bar item 4).

**A year about 10 school days short.** Ten school days are two weeks, four sessions of this course a year. Four
fluency days a year fold into their neighbor: each moves its eight-minute drill into the neighbor's opener and saves
one 40-minute session. None holds an `assess` value, a critique, a revision or a showing, and no owned part is cut.

| Year | Fold-in days (into) | Minutes saved |
|---|---|---|
| K | 12 (13), 26 (27), 43 (44), 59 (60) | 4 x 40 = 160 |
| 1 | 80 (79), 91 (92), 108 (109), 122 (123) | 160 |
| 2 | 136 (137), 153 (154), 171 (172), 186 (187) | 160 |

Each year then runs 60 sessions (2,400 minutes) against the full 64 (2,560); the band runs 180 against 192. The
check days keep their weeks when the lost days fall after the folds; otherwise the check moves at most one week
later, never into a core check week of the grade. Where a fold day carries a baseline look (days 122 and 186), the
baseline look moves with the drill into the neighbor's opener.

## For the lead

1. **Frame Course-level checks table, year-end rows (sequence-write rule 2, "Collect once").** The frame's year-end
   rows for years K, 1 and 2 hear the Re8.1 and Re9.1 talk items again one to three days after units 3, 7 and 11
   heard them. This scope carries those records instead and samples: year K, VA:Cr2.3.Ka, VA:Cr1.1.Ka, VA:Cr3.1.Ka;
   year 1, VA:Cr1.2.1a, VA:Cr3.1.1a, VA:Re7.1.1a; year 2, VA:Cr1.1.2a, VA:Cr3.1.2a, VA:Re7.1.2a. Replacement cells for
   the frame's "What it checks": as the table above. `frame.py calendar` is unaffected (same days and weeks).
2. **Frame For the lead items 1 to 6 are unchanged here.** The after-core week sharing (item 1) and the arts
   discipline key in the stagger check (item 2) are the calendar pass's; the VA:Re7.1.Ka words line (item 3), the
   stale bar row (item 4), the time figures (item 5) are untouched; the supplies ceiling (item 6) is decided at $75 a class a year (Cory approved 2026-11-26, Desk q-frames-money-1).
3. **Year 1 mid-year check and paint.** The frame's "fresh print task" sits on a check day, which the frame keeps
   free of paint; this scope uses crayon rubbing over found objects or dry stamp pads. If the lead prefers wet prints,
   the frame's check-day rule needs a line.
