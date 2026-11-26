# Scope and sequence: Media Arts, grades 3 to 5

Course `media-arts-grades-3-to-5` (catalog id `media-arts-3-5`), a band course for grades 3, 4 and 5; draft, written 2026-11-26 from the frame (docs/courses/media-arts-grades-3-to-5/frame.md). The days are in data/plans/media-arts-grades-3-to-5/days.csv.

## How this file is read

- **Three years, one file.** The band runs as three years one after another: year 3 (course days 1 to 64, units 1 to 4), year 4 (days 65 to 128, units 5 to 8), year 5 (days 129 to 192, units 9 to 12). `stretch` in days.csv is the unit number of the frame's Units table; `C` marks a course-level check day and its respond day.
- **Which grade's standards fall in which year** (the bar's "Scope and sequence states"). Year 3 claims only the 18 grade 3 media arts ids of the National Core Arts Standards, 2014 (`MA:*.3`, `.3a` and so on), year 4 only the 18 grade 4 ids, year 5 only the 18 grade 5 ids: 54 in all, the count in docs/courses/arts/STANDARD.md 3.2, each taught and assessed in its own year. A year revisits the year before's ids as practice that returns, never as a claim.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn (STANDARD.md 3.1); each year still claims only its grade's ids, so a student's record shows which grade's standards they met. A student who meets year 5 before year 4 gets each unit's day-2 retrieval with its ten-minute reteach.
- **Meeting days and `school_day`.** The course meets two 40-minute sessions a week for 32 weeks a year, 96 weeks over the band, never a daily period (bar criterion 9). `school_day` counts the band's school days in one run, 1 to 480: year 3 is school days 1 to 160, year 4 is 161 to 320, year 5 is 321 to 480, as scripts/frame.py reads it (lead call 5, 2026-11-26). Within a year, course day n (1 to 64) meets in week ceil(n / 2), on the week's second school day when n is odd and its fourth when n is even: school day = 160 x (year index) + 5 x (ceil(n / 2) - 1) + 2 or 4. A day's week of its year is (school_day - 1) // 5 + 1, less 32 for each earlier year; every unit and check falls in the frame's weeks by this count. The filled `school_day` wins over frame.py's even spread, and data/plans/calendar.csv is regenerated from it, so it is not re-counted to match calendar.csv. A school may pick any two days a week; the week stays the same.
- **The session.** Set-up about 5 minutes (trays and any shared device out), clean-up about 4 (6 on a cutting and gluing day) inside the 40; a retrieval task takes ten minutes of a day's opener. Every day runs on paper, card, found objects and printed cards; one shared school device per group of five is one way in, never the only one, and no student account is used. Equipment, safe use of space and the free path are named in each day's note.
- **The four processes** (create; perform, present or produce; respond; connect). Each year touches all four, and each unit touches at least the processes the frame names for it; a unit need not claim all four, and a process is never claimed through an id outside the unit's owned rows (lead call 2, 2026-11-26). In this course every unit happens to carry all four on its own days with its own ids, and each unit section below names them by day. Responding to another maker's work is taught on understanding days (a work studied with its work card), never on a respond day; a respond day acts on a check (GLOSSARY).
- **Unit shape.** Each unit runs: a clean first day (the hook, a work studied, the compelling question); a day-2 opener with the retrieval task; technique days with the step card; one or two fluency days; making days, the second of which holds the unit's one critique (describe, ask, suggest); a revision day; the showing; the check day or days; a respond day after every mark is in. Technique days come before the making that needs them. Each unit opens with a baseline look at its main look-for during the first practice days (no score from the day a technique is first taught), so each student has two marks a unit, and one piece a unit goes to the portfolio folder with a one-line reflection.
- **Rotating look-fors.** The tool, space, ethics and role items (MA:Cn11.1.3b, 4b, 5b; MA:Pr5.1.3a, 3c; MA:Pr5.1.4a, 4c) are never end-of-unit check-day items; a mid-year check samples their "examine" part by a fresh sort or case on paper. They are marked on a class list over the unit's last three making days, ten students a day.
- **Supplies.** No tools, supplies or safety columns (math and science only); each day's note names its equipment, hazard and control in the frame's words, and the free path.

### Readiness and retrieval (rule 2, counted by grade number)

Every earlier-grade row this course assumes, with its last use and treatment. No row is two or more grades idle, so the course has no readiness check; every unit opens with a retrieval task inside day 2's opener and day 1 stays clean. Media Arts, grades K to 2 is optional, so each year 3 retrieval task carries its ten-minute reteach as written, and the same reteach serves a student new to the band in year 4 or 5.

| Unit (days) | Rows assumed | Last used | Treatment |
|---|---|---|---|
| 1 (1 to 14) | ma-g2-read, ma-g2-society | grade 2 (Media Arts K to 2, unit 9) | Retrieval with reteach, day 2 |
| 2 (15 to 32) | ma-g2-ideas, ma-g2-craft | grade 2 (unit 10) | Retrieval with reteach, day 16; the unit 1 critique card retrieved in the same opener |
| 3 (35 to 50) | ma-g2-make, ma-g2-judge | grade 2 (unit 11) | Retrieval with reteach, day 36 |
| 4 (53 to 64) | ma-g2-present, ma-g2-sources | grade 2 (unit 12) | Retrieval with reteach, day 54 |
| 5 (65 to 78) | ma-g3-read, ma-g3-society | grade 3 (unit 1) | Retrieval, day 66 |
| 6 (79 to 96) | ma-g3-ideas, ma-g3-craft | grade 3 (unit 2) | Retrieval, day 80 |
| 7 (99 to 112) | ma-g3-make, ma-g3-judge | grade 3 (unit 3) | Retrieval, day 100 |
| 8 (115 to 128) | ma-g3-present, ma-g3-sources | grade 3 (unit 4) | Retrieval, day 116 |
| 9 (129 to 144) | ma-g4-read, ma-g4-society | grade 4 (unit 5) | Retrieval, day 130 |
| 10 (145 to 162) | ma-g4-ideas, ma-g4-craft | grade 4 (unit 6) | Retrieval, day 146 |
| 11 (165 to 176) | ma-g4-make, ma-g4-judge | grade 4 (unit 7) | Retrieval, day 166 |
| 12 (179 to 192) | ma-g4-present, ma-g4-sources | grade 4 (unit 8) | Retrieval, day 180 |

**Same-year retrieval.** A row taught earlier in the same year and leaned on again gets a five-minute warm-up in the opener of the making day that needs it (APPROACH "How a day opens"), named in the note and in `retrieves`. No unit's first day changes, and no readiness check is needed.

| Day | Row retrieved | Taught in | What the warm-up recalls |
|---|---|---|---|
| 41 | ma-g3-craft | unit 2 | the 24-frame flip book and spacing |
| 58 | ma-g3-craft, ma-g3-make | units 2 and 3 | the crew roles, and the ordered frames kept from units 2 and 3 |
| 105 | ma-g4-craft | unit 6 | capture skills |
| 120 | ma-g4-craft | unit 6 | stop-motion and the rotating roles |
| 170 | ma-g5-craft | unit 10 | capture in varied roles |
| 186 | ma-g5-make, ma-g5-society | units 11 and 9 | emphasis for clarity, and the media-literacy checklist |

### Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; step cards, work cards, paper media tools (viewfinder, loop strips, shot strips, sound cue cards), found objects; an optional shared device | Technique taught in steps; works studied with their setting; crew making with one critique and a revision; a showing or screening each unit | A portfolio folder of 12 pieces over the band with reflections; 12 showings; two marks a unit per student on the main look-for | Met marks on each year's 18 ids and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that arts study raises any other result (APPROACH "Sources").

## Year 3 (grade 3 ids), course days 1 to 64

### Unit 1. How media works on us

Days 1 to 14, weeks 1 to 7. Owns ma-g3-read (MA:Re7.1.3a, 3b) and ma-g3-society (MA:Cn11.1.3a, 3b).

**Arc.** The Chōjū-giga scroll opens the band on parts that build a message (day 1); the tool and space card is set before any tool is handed out (day 2), then the viewfinder's shot sizes and angles are taught in steps (days 3 and 4) and drilled (day 5), so that Bear Story (day 6) can be read for how a technique steers. Days 7 and 8 turn to media in daily and cultural life and to online behavior on invented cases. The class media map is made over days 9, 11 and 12, with the critique routine modeled on day 10 before its first use on day 11; the map is hung on day 12.

**Why this order.** Every later unit needs the tool and space rules and the reading routine, so they come first; framing is taught before the media map uses it, and the critique is modeled before it is asked for (frame, Readiness and retrieval).

**Assessment.** Retrieval inside day 2 (table above). End of unit on day 13: the written item on six unseen stills (MA:Re7.1.3a) and the talk item (MA:Re7.1.3b), with the kept day-of-media card made on day 12 (MA:Cn11.1.3a) and the rotating tool-step marks from days 9, 11 and 12 (MA:Cn11.1.3b) entered. Response time: day 14. No mid-unit assessment (14 days).

**Processes.** Create: days 3, 4, 9, 11, 12. Present: day 12 (the hallway map). Respond: days 1, 5, 6, 10. Connect: days 1, 6, 7, 8.

**Candidate settled.** Kept, no day added: device hand-out and hand-back minutes inside a 40-minute session (bar criterion 9) sit in the 5-minute set-up and 4-minute clean-up, named in the notes of days 2 and 9 and in units 5 and 9's day 2.

### Unit 2. Ideas in motion

Days 15 to 32, weeks 8 to 16. Owns ma-g3-ideas (MA:Cr1.1.3, Cr2.1.3) and ma-g3-craft (MA:Pr5.1.3a, 3b, 3c).

**Arc.** A zoetrope strip shows twelve drawings looping into motion (day 15). The loop is taught in steps (day 16: register and an even flip; day 17: spacing) and drilled (day 18). La Mort du Gandji (day 19) shows how a maker develops animal characters; live sound on cue is taught (day 20) and drilled (day 21), and the crew roles are set (day 22). Crews develop at least three ideas (day 23) and test a mockup with another crew (day 24), then make the loop over days 25 to 27 (critique on day 26, revision on day 27), run it (day 28) and show it with live sound (day 29).

**Why this order.** Both techniques, the loop and live sound, are taught and drilled before the crews plan with them, and the roles are named before the crew work starts; the test (day 24) comes before making so that its change shows in the loop. Longest unit of year 3 (five ids, two techniques, the roles), as the frame sets.

**Assessment.** Retrieval inside day 16. End of unit over two check days: day 30, the storyboard look-fors (MA:Cr1.1.3, Cr2.1.3) and the loop look-for for made-up content (MA:Pr5.1.3b); day 31, the role record (MA:Pr5.1.3a) with the rotating role and tool marks from days 25 to 27 (MA:Pr5.1.3a, 3c). Response time: day 32. No mid-unit assessment (18 days).

**Processes.** Create: days 23 to 27. Produce: days 20, 22, 25 to 29 (the showing on day 29). Respond: days 15, 19, 29. Connect: days 15 and 19 (each work's place and time from its work card).

**Candidate settled.** Kept, no day added: the doubled parent-and-student crew (two roles each) for one student at home, named on the role cards (day 22).

### Year 3 mid-year check

Days 33 (check) and 34 (respond), week 17. See Course-level checks.

### Unit 3. Order and stress

Days 35 to 50, weeks 18 to 25. Owns ma-g3-make (MA:Cr3.1.3a, 3b) and ma-g3-judge (MA:Re8.1.3, Re9.1.3).

**Arc.** Marey's pelican breaks one movement into ordered stages (day 35). Purposeful order with movement and force is taught (day 36) and drilled (day 37); Luminaris (day 38) is read for its order, its stressed parts and its setting; stress is taught on the revision log (day 39) and named criteria on the criteria card (day 40). Each student orders a piece (day 41), drills movement (day 42), stresses one element (day 43), takes the critique with named criteria (day 44) and revises with the "after" line (day 45); day 46 practices judging with the criteria card. The class viewing (day 50) comes after the respond day so every piece shown is finished.

**Why this order.** Order before stress, both before the criteria are used on a student's own piece; judging with named criteria for the first time needs a piece of the student's own to judge. Lean on ela:SL.3.1: ELA grade 3 unit 1 teaches collaborative discussion in weeks 1 to 8, well before this unit; the critique card still shows the discussion rules (day 40's note).

**Assessment.** Retrieval inside day 36. End of unit over days 47 (the written item on purpose, meaning and setting, MA:Re8.1.3; the piece and revision log look-fors, MA:Cr3.1.3a, 3b) and 48 (the talk item on two criteria and one improvement, MA:Re9.1.3). Response time: day 49. No mid-unit assessment (16 days).

**Processes.** Create: days 36, 39, 41, 43, 45. Present: day 50. Respond: days 35, 38, 40, 44, 46. Connect: days 35 and 38.

**Candidate settled.** Kept, no day added: an ordered-motion work by a living maker from Africa or Asia, described and linked, in 10 minutes of day 38. Year 3's living makers are otherwise from Chile, Argentina and the Abenaki nation; the unit plan picks the work and checks its rights line.

### Year 3 year-end check

Days 51 (check) and 52 (respond), week 26. See Course-level checks.

### Unit 4. Our class screening

Days 53 to 64, weeks 27 to 32. Owns ma-g3-present (MA:Pr4.1.3, Pr6.1.3a, 3b) and ma-g3-sources (MA:Cn10.1.3a, 3b).

**Arc.** Méliès's Cendrillon opens the question of how a popular retelling changes a story (day 53). Blending forms into a narrated photo-story is taught (day 54) and studied in Sigwan (day 55); the source log (day 56) and a class-invented retelling beside Méliès's film (day 57) carry the connecting ids. Crews build the photo-story from frames and sounds kept from units 2 and 3 (day 58), learn the showing conditions and roles (day 59), take the critique (day 60) and revise and rehearse (day 61), where after the run the watching crew says what it noticed and the crew describes the run's experience, shares that result and names one way to present better (MA:Pr6.1.3b taught before day 63 scores it). The class screening is the unit's first check (day 62).

**Why this order.** Last in year 3 because the screening uses the year's crew roles and ordered pieces and ends the year after the year-end check; it is shorter than unit 2 though it owns five ids because kept frames and sounds are its material.

**Assessment.** Retrieval inside day 54. End of unit: day 62, the screening with look-fors marked at the screening place (MA:Pr4.1.3, the look-for naming the school-subject fact in the blended piece; the role carried out for MA:Pr6.1.3a); day 63, the talk item (one sentence describing the screening's experience, one result shared, one improvement; MA:Pr6.1.3b) and written item (MA:Cn10.1.3b), with the source log (MA:Cn10.1.3a) and screening-plan card (MA:Pr6.1.3a) scored. Response time: day 64. The screening is the unit's own end-of-unit assessment (the year-end check comes before it).

**Processes.** Create: days 58, 60, 61. Present and produce: days 54, 59, 61, 62. Respond: days 53, 55, 57. Connect: days 53, 56, 57.

**Candidate settled.** Kept, no day added: the film board's page for Sigwan is checked open and free on the day the unit plan is written (day 55's note).

## Year 4 (grade 4 ids), course days 65 to 128

### Unit 5. Real or made?

Days 65 to 78, weeks 1 to 7 of year 4. Owns ma-g4-read (MA:Re7.1.4a, 4b) and ma-g4-society (MA:Cn11.1.4a, 4b).

**Arc.** El hotel eléctrico asks how a trick film makes the impossible look real (day 65). The ethics card reopens the tool rules (day 66); angle and light are taught (day 67) and drilled (day 68); the parts-and-message chart gains its "because" column (day 69), and Muluneh's staged photographs are read for why their techniques steer (day 70). The invented real-or-made pairs (day 71) lead into the three-picture piece, made over days 72, 74 and 75 (critique on day 74), with an explain-why drill on day 73 and the real-or-made wall for a partner class on day 76.

**Why this order.** First in year 4 because it reopens the tool rules (now with ethics) and the reading routine after the summer and moves reading from describing how to explaining why; the fantasy study needs angle and light first.

**Assessment.** Retrieval inside day 66. End of unit on day 77: the written item (MA:Re7.1.4a) and talk item (MA:Re7.1.4b), with the three-picture piece look-for (MA:Cn11.1.4a), the kept ethics-card case and the rotating marks from days 72, 74 and 75 (MA:Cn11.1.4b). Response time: day 78.

**Processes.** Create: days 67, 72, 74, 75. Present: day 76. Respond: days 65, 69, 70. Connect: days 65, 66, 71, 72.

**Candidate settled.** Dropped: a fantasy work from the Americas by a living maker. Year 4 already studies living makers from the Americas (Iturbide in unit 7, Skawennati in unit 8), and the 14 days hold four ids and the angle-and-light technique with no room for a third work.

### Unit 6. Design it, test it

Days 79 to 96, weeks 8 to 16 of year 4. Owns ma-g4-ideas (MA:Cr1.1.4, Cr2.1.4) and ma-g4-craft (MA:Pr5.1.4a, 4b, 4c).

**Arc.** Plateau's phenakistiscope disc (day 79) opens a tool used in a new way. Paper cut-out stop-motion with replacement parts is taught (day 80), seen in Ōfuji's chiyogami animation (day 81) and drilled (day 82). The goal (day 83), the design steps (day 84), two plans combined (day 85), a tool in a new way (day 86) and the rotating roles (day 87, drilled on day 88) come before the making: sets and a test shot (day 89), capture (day 90), the critique (day 91), the revision logged on the design card (day 92) and the showing (day 93).

**Why this order.** Stop-motion is taught and drilled before the crews plan for it, and goal, design steps and roles are named before capture starts; a new use of a tool grows from unit 5's angle and light.

**Assessment.** Retrieval inside day 80. End of unit over days 94 (storyboard look-fors for MA:Cr1.1.4 and Cr2.1.4; the design card for MA:Pr5.1.4b) and 95 (the role record for MA:Pr5.1.4a, with the rotating role and tool marks from days 90 to 92 for MA:Pr5.1.4a and 4c). Response time: day 96.

**Processes.** Create: days 83, 85, 89 to 92. Produce: days 80, 87, 90 to 93. Respond: days 79, 81, 93. Connect: days 79 and 81.

**Candidate settled.** Dropped: a living cut-paper or stop-motion maker from Africa or the Americas. Year 4 already has living makers from Ethiopia, Mexico and Kahnawà:ke, and a third work would take one of the unit's technique days.

### Year 4 mid-year check

Days 97 (check) and 98 (respond), week 17 of year 4. See Course-level checks.

### Unit 7. Balance and contrast

Days 99 to 112, weeks 18 to 24 of year 4. Owns ma-g4-make (MA:Cr3.1.4a, 4b) and ma-g4-judge (MA:Re8.1.4, Re9.1.4).

**Arc.** Adams's Tetons (day 99) opens with a reasoned reaction to strong contrast; balance and contrast are taught for a six-frame photo-story (day 100), seen in Iturbide's photograph (day 101) and drilled (day 102). Refining by stressing chosen elements (day 103) and criteria on production steps (day 104) are taught before the making: arranging (day 105), the critique on the piece and one production step (day 106), two logged refinements (days 107 and 108). The class viewing (day 112) follows the respond day.

**Why this order.** Arrangement before refinement, and criteria on steps before they are used in the critique; the revision log and critique card return from year 3 one step harder.

**Assessment.** Retrieval inside day 100. End of unit over days 109 (the written reaction item, MA:Re8.1.4; the piece and revision log look-fors, MA:Cr3.1.4a, 4b) and 110 (the talk item on two criteria applied to a piece and a production step, MA:Re9.1.4). Response time: day 111.

**Processes.** Create: days 100, 105 to 108. Present: day 112. Respond: days 99, 101, 104, 106. Connect: days 99 and 101 (the Tetons work card names the Shoshone and other peoples' homelands).

**Candidate settled.** Dropped: a balance-and-contrast work from Asia or Africa. Year 4 has Japan (unit 6) and Ethiopia (unit 5); the unit's 14 days have no spare time.

### Year 4 year-end check

Days 113 (check) and 114 (respond), week 25 of year 4. See Course-level checks.

### Unit 8. Show it to the school

Days 115 to 128, weeks 26 to 32 of year 4. Owns ma-g4-present (MA:Pr4.1.4, Pr6.1.4a, 4b) and ma-g4-sources (MA:Cn10.1.4a, 4b).

**Arc.** Painlevé's L'Hippocampe shows science and music coordinated in one film (day 115). Coordinating a school-subject topic, an art form and media is taught (day 116); research with two sources and cultural knowledge (day 117) and CyberPowWow beside an invented online space (day 118) carry the connecting ids. Crews plan (day 119) and make (day 120), learn the public showing conditions (day 121), take the critique (day 122), revise (day 123), run the showing (day 124, where after each run the crew explains how it went and one thing to improve: MA:Pr6.1.4b taught before day 127 scores it) and dress it (day 125). The public school showing is the first check (day 126).

**Why this order.** The research comes before the plan that uses it, and the showing conditions before the run-through; last in year 4 because the showing uses the year's stop-motion, crew and arranged piece.

**Assessment.** Retrieval inside day 116. End of unit: day 126, the showing look-fors (MA:Pr4.1.4; the role for MA:Pr6.1.4a); day 127, the talk item (MA:Pr6.1.4b) and written item (MA:Cn10.1.4b), with the source log (MA:Cn10.1.4a) and screening-plan card scored. Response time: day 128.

**Processes.** Create: days 119, 120, 122, 123. Produce: days 121, 124, 125, 126. Respond: days 115 and 118. Connect: days 115, 117, 118.

**Candidate settled.** Kept, no day added: the topic card lists what the grade 4 science and social studies courses have taught that term (day 116); nothing waits on a set unit, and the source cards carry the facts used.

## Year 5 (grade 5 ids), course days 129 to 192

### Unit 9. Selling and telling

Days 129 to 144, weeks 1 to 8 of year 5. Owns ma-g5-read (MA:Re7.1.5a, 5b) and ma-g5-society (MA:Cn11.1.5a, 5b).

**Arc.** A Ghanaian painted film poster beside a trade card opens two pieces told apart (day 129). The media-literacy checklist reopens the tool rules (day 130); the trade cards and their history (day 131) and the Ghana posters (day 132) are studied; the eye path is taught (day 133) and drilled (day 134); telling apart is practiced on a two-column chart (day 135). Advertising's ethics and an investigation question (day 136) lead into the investigation (day 137) and the invented ad, made over days 138, 140 and 141 (critique on day 140), with a tell-apart drill on day 139 and the ad wall on day 142.

**Why this order.** The two works are studied one at a time before they are told apart, and the eye path is taught before the ad uses it; 16 days, two more than years 3 and 4, for the advertising history study, as the frame sets.

**Assessment.** Retrieval inside day 130. End of unit on day 143: the written item on two unseen pieces (MA:Re7.1.5a) and the talk item (MA:Re7.1.5b), with the ad, caption and investigation card look-for (MA:Cn11.1.5a), the checklist card and the rotating marks from days 138, 140 and 141 (MA:Cn11.1.5b). Response time: day 144.

**Processes.** Create: days 133, 138, 140, 141. Present: day 142. Respond: days 129, 131, 132, 135. Connect: days 130, 131, 136, 137.

**Candidate settled.** Dropped: an advertising work from Asia. Year 5 studies China (units 10 and 12) and Iran (unit 11), and the unit's two extra days already hold the history study.

### Unit 10. Bend the rules

Days 145 to 162, weeks 9 to 17 of year 5. Owns ma-g5-ideas (MA:Cr1.1.5, Cr2.1.5) and ma-g5-craft (MA:Pr5.1.5a, 5b, 5c).

**Arc.** Western Spaghetti opens a convention bent on purpose (day 145). Object stop-motion is taught (day 146); Where Is Mama (day 147) shows ideas drawn from another art form; wash animation sets the ordinary and the experimental brush side by side (day 148); a capture drill follows (day 149). Ideas from experience or another artist's work (day 150), the proposal for an audience (day 151), a tested model (day 152), the varied roles (day 153) and bending a convention (day 154) come before the making (days 155, 157, 158, with a wash drill on day 156 and the critique on day 157) and the showing for the stated audience (day 159).

**Why this order.** Both techniques are taught before the crews propose with them, and the model is tested before making; the proposal uses unit 9's reading of how pieces steer an audience.

**Assessment.** Retrieval inside day 146. End of unit over days 160 (storyboard look-fors for MA:Cr1.1.5 and Cr2.1.5; the piece's bent convention for MA:Pr5.1.5b) and 161 (the role record for MA:Pr5.1.5a; the written item comparing a tool's ordinary and experimental use for MA:Pr5.1.5c). Response time: day 162.

**Processes.** Create: days 150, 151, 152, 154, 155, 157, 158. Produce: days 146, 153, 155, 159. Respond: days 145, 147, 159. Connect: days 145 and 147.

**Candidate settled.** Kept, no day added: an experimental animation by a living maker from Africa or Latin America, described and linked, in 10 minutes of day 147. Year 5's living makers are otherwise PES and possibly the Ghanaian painters, whose living status the unit plan must still confirm (frame For the lead item 5).

### Year 5 mid-year check

Days 163 (check) and 164 (respond), week 18 of year 5. See Course-level checks.

### Unit 11. Make it clear

Days 165 to 176, weeks 19 to 24 of year 5. Owns ma-g5-make (MA:Cr3.1.5a, 5b) and ma-g5-judge (MA:Re8.1.5, Re9.1.5).

**Arc.** One Week opens how shots stress a joke (day 165). The cut is taught on the shot strip (day 166); Bread and Alley (day 167) sets each student's reading beside the group's; the cut is drilled (day 168); students set their own criteria and practice feedback that names a look-for (day 169). The sequence is made with the clarity decision written first (day 170), critiqued with the student's own criteria (day 171), refined with the change logged (day 172) and shown at a class viewing (day 173). The kept criteria card is made on check day 175, on a classmate's finished sequence.

**Why this order.** The cut and the student's own criteria are both in place before the sequence and its critique; the revision log returns one step harder (the change decided before it is made).

**Assessment.** Retrieval inside day 166. End of unit over days 174 (the written item on personal and group readings, MA:Re8.1.5; the sequence and revision log look-fors, MA:Cr3.1.5a, 5b) and 175 (the kept criteria card, MA:Re9.1.5: each student's own criteria from day 169 applied to a classmate's finished sequence and one of its production steps, aim and setting named, feedback naming a look-for; then a self-check). Response time: day 176.

**Processes.** Create: days 166, 170, 171, 172. Present: day 173. Respond: days 165, 167, 169, 171, 175. Connect: days 165 and 167.

**Candidate settled.** Kept, no day added: the group-reading chart has a paper version for one adult at home (day 167's note).

### Year 5 year-end check

Days 177 (check) and 178 (respond), week 25 of year 5. See Course-level checks.

### Unit 12. Our newscast

Days 179 to 192, weeks 26 to 32 of year 5. Owns ma-g5-present (MA:Pr4.1.5, Pr6.1.5a, 5b) and ma-g5-sources (MA:Cn10.1.5a, 5b).

**Arc.** A Dianshizhai Pictorial page opens what news keeps of an event (day 179). The newscast's parts and voice-over are taught on the run sheet (day 180); a Posada broadside and a newsreel story of a community event are studied (day 181); the interview and voice-over are taught in steps (day 182); sources are gathered, the interview with a consenting adult among them (day 183), and the hand-offs drilled (day 184); the two showing formats are weighed and the teacher models comparing two presentations' results on a Curio Class example (day 185). Crews make the newscast (day 186), take the critique (day 187), revise (day 188) and rehearse in both formats (day 189): the printed news sheet is presented to a partner crew and one audience result logged, and day 190's live showing gives the second result to compare on day 191. The newscast is the first check (day 190).

**Why this order.** The three news works are studied before the class makes its own; the interview is taught before it is used, and the sources are gathered before the reports are written; MA:Pr6.1.5b is modeled (day 185) and practiced on a real second showing (day 189) before it is scored; the newscast blends the year's reading of ads, its capture and its emphasis for clarity, and ends the band after the year-end check.

**Assessment.** Retrieval inside day 180. End of unit: day 190, the newscast look-fors (MA:Pr4.1.5; the role for MA:Pr6.1.5a); day 191, the talk item comparing the two logged results (printed sheet on day 189, live newscast on day 190) and one improvement (MA:Pr6.1.5b) and the written item (MA:Cn10.1.5b), with the source log (MA:Cn10.1.5a) and screening-plan card scored. Response time: day 192.

**Processes.** Create: days 186, 187, 188. Produce: days 180, 182, 185, 189, 190. Respond: days 179 and 181. Connect: days 179, 181, 183.

**Candidate settled.** Dropped: a picture-news form from Africa. The unit already studies three works beside the newscast production, and year 5 studies Ghana in unit 9.

## Course-level checks

Each check day follows the frame's form (set-up 4; the fresh plan or sort task 10 and the written item 8 done by every student at the tables while the teacher hears six groups of five at the table, about three minutes each; self-check 5; clean-up 3; about 10 minutes of slack). Each is followed by a respond day; marks are in before it. A check right after a unit never draws its items from that unit: the unit just before it is carried unscored, and every item is a new piece, prompt, sort or case.

| Check | Days | Week (of its year) | What it samples |
|---|---|---|---|
| Year 3 mid-year | 33 check, 34 respond | 17 | Unit 1 with new pieces: written MA:Re7.1.3a, talk MA:Re7.1.3b, a fresh tool-and-space sort MA:Cn11.1.3b. Unit 2's storyboard and role record (days 30 and 31) carried unscored. |
| Year 3 year-end | 51 check, 52 respond | 26 | Units 1 and 2: a fresh plan with three ideas using at least two tools or materials, tested with a partner (MA:Cr1.1.3, Cr2.1.3), written MA:Re7.1.3a, talk on a new day-of-media card and one invented online case sorted fair or unfair with a reason MA:Cn11.1.3a. Unit 3 (days 47 and 48) carried unscored; unit 4 is assessed by its screening. |
| Year 4 mid-year | 97 check, 98 respond | 17 | Unit 5: written MA:Re7.1.4a, talk MA:Re7.1.4b, a fresh ethics-card case MA:Cn11.1.4b. Unit 6 (days 94 and 95) carried unscored. |
| Year 4 year-end | 113 check, 114 respond | 25 | Units 5 and 6: a fresh goal and two quick plans combined, with one test named and the showing in mind (MA:Cr1.1.4, Cr2.1.4), written MA:Re7.1.4a, talk on a new real-or-made pair MA:Cn11.1.4a. Unit 7 (days 109 and 110) carried unscored; unit 8 is assessed by its showing. |
| Year 5 mid-year | 163 check, 164 respond | 18 | Unit 9: written MA:Re7.1.5a, talk MA:Re7.1.5b, a fresh checklist case MA:Cn11.1.5b. Unit 10 (days 160 and 161) carried unscored. |
| Year 5 year-end | 177 check, 178 respond | 25 | Units 9 and 10: a fresh proposal with its goal and audience and one test named (MA:Cr2.1.5), written MA:Re7.1.5a, talk on a new invented ad, what it leaves out and one way its form differs from a trade card of the 1880s for a named community, public or invented (MA:Cn11.1.5a). Unit 11 (days 174 and 175) carried unscored; unit 12 is assessed by its newscast. |

**Codes not sampled on a course-level check** (rule 3, L107). The frame's check table limits each check to the read, society and ideas rows of the units before the one just finished, so these are never sampled at course level: ma-g3-craft, make, judge, present and sources (MA:Pr5.1.3a, 3b, 3c; Cr3.1.3a, 3b; Re8.1.3; Re9.1.3; Pr4.1.3; Pr6.1.3a, 3b; Cn10.1.3a, 3b), the same rows for grade 4 (MA:Pr5.1.4a, 4b, 4c; Cr3.1.4a, 4b; Re8.1.4; Re9.1.4; Pr4.1.4; Pr6.1.4a, 4b; Cn10.1.4a, 4b) and for grade 5 (MA:Pr5.1.5a, 5b, 5c; Cr3.1.5a, 5b; Re8.1.5; Re9.1.5; Pr4.1.5; Pr6.1.5a, 5b; Cn10.1.5a, 5b), and the year 5 ideas code MA:Cr1.1.5. The reason: the craft and role codes are rotating look-fors marked over making days, never check-day items; each year's third unit is carried unscored by the check right after it; and the screening unit comes after the year-end check, which sits before the core year-end weeks 28 to 32 (frame, Course-level checks). Each of these codes is still taught and assessed in its own unit.

All six sit on the weeks CALENDAR.md lists for this course, none on a core check week of its grade (grade 3: 9, 12, 14, 16, 20, 23, 25, 28, 30 to 32; grade 4: 8 to 10, 12, 16, 19, 21, 23, 27, 30 to 32; grade 5: 10, 11, 16, 17, 21, 22, 29 to 32). Arts are specials in K to 5 and do not count against the classroom teacher's stagger (CALENDAR.md rule 1); the clashes with other specials are the frame's For the lead item 2.

## Shorter path

**The once-a-week path (32 sessions a year, 40 minutes).** Every unit and every id is kept by merging the marked days; a merged session never drops a critique, a revision or a respond session, and fluency days fold into the openers. Check sessions fall in the full path's weeks (year 3: 17 and 26; year 4: 17 and 25; year 5: 18 and 25), respond sessions one week later. No assessment is done in a respond session; the rotating look-fors fall on the last two making sessions, fifteen students a session.

| Unit | Sessions | Sessions, as course days merged |
|---|---|---|
| 1 | 7 | 1-3 (scroll, tool card, viewfinder); 4-6 (angles, Bear Story, drill as opener); 7-8; 9-11 (making with the modeled critique); 12 (revision and map); 13 (check); 14 (respond) |
| 2 | 9 | 15-17; 18-20; 21-22; 23-24; 25-26 (making with critique); 27-29 (revision, run, showing); 30 (check); 31 (check); 32 (respond) |
| 3 | 6 | 35-37 (hook, retrieval, order, the drill as opener); 38-40 (Luminaris, stress, criteria); 41-44 (making with critique); 45-46 and 50 (revision and criteria practice, the unscored class viewing as its last ten minutes); 47-48 (one talk-and-written check session); 49 (respond) |
| 4 | 6 | 53-57 (week 25, before the year-end check); 58-60 (making with critique); 61 (revision); 62 (screening, check 1); 63 (check 2); 64 (respond) |
| 5 | 7 | 65-67; 68-70; 71; 72-74 (making with critique); 75-76 (revision and wall); 77 (check); 78 (respond) |
| 6 | 9 | 79-81; 82-84; 85-86; 87-88; 89-91 (making with critique); 92-93 (revision and showing); 94 (check); 95 (check); 96 (respond) |
| 7 | 6 | 99-101 (hook, retrieval, balance and contrast, Iturbide); 102-104 (drill as opener, refining, criteria on steps); 105-106 (making with critique); 107-108 and 112 (revision, the unscored class viewing as its last ten minutes); 109-110 (one check session); 111 (respond) |
| 8 | 6 | 115-118; 119-122 (making with critique); 123-125 (revision and run); 126 (showing, check 1); 127 (check 2); 128 (respond) |
| 9 | 8 | 129-131; 132-134; 135-136; 137-138; 139-140 (making with critique); 141-142 (revision and wall); 143 (check); 144 (respond) |
| 10 | 9 | 145-147; 148-150; 151-152; 153-154; 155-157 (making with critique); 158-159 (revision and showing); 160 (check); 161 (check); 162 (respond) |
| 11 | 5 | 165-167 (hook, retrieval, the cut, Bread and Alley); 168-171 (drill as opener, criteria set, making with critique); 172-173 (revision and viewing); 174-175 (one check session: the written item, about 10, and the kept criteria card on a classmate's finished sequence, about 15, with set-up and clean-up); 176 (respond) |
| 12 | 6 | 179-182 and 184 (hook, retrieval, newscast parts with voice-over and the interview steps, Posada and a newsreel, hand-offs as opener: two works and one technique only); 183 and 186-187 (gathering sources with the interview, making with critique); 185 and 188-189 (formats weighed and the comparison modeled, revision, rehearsal with the printed sheet shown to a partner crew); 190 (newscast, check 1); 191 (check 2); 192 (respond) |

Units 4 and 8 keep the frame's counts here, and their opening sessions (53-57, 115-118) still hold two works, a technique, a retrieval and a connecting study each; the expert read's rebalance (one session moved from each ideas-and-crew unit to the screening unit) is a frame change sent to the structure pass, and the unit 12 row above is the in-count fallback it names until then.

Year 3 pauses unit 4 for the year-end check: unit 3 in weeks 19 to 24, unit 4's first session in week 25, the check and respond in weeks 26 and 27, unit 4's last five sessions in weeks 28 to 32. Each year totals 32 sessions (units plus 2 check and 2 respond sessions).

**A shorter period (30 minutes).** Set-up (4) and clean-up (3) stay; the 5-minute opener stays, and a retrieval task takes 8 minutes of it on day 2; teaching days keep the demonstration and one try with the step card; making days keep the critique and cut repeated turns. On a talk-and-written check day the written item and self-check stay on the day and the talk items move to the unit's last three making days (two groups a day at the teacher's table, never on a day a technique is first taught), which changes the evidence window, not the items or the day count.

**A year about ten school days short.** Ten school days are two weeks, four meetings of this course. These fold-in days carry no `assess` value and teach nothing new; each is a drill whose five most useful minutes move into the next day's opener. Where the fold day ends the baseline look (days 5, 37, 68, 82, 102, 134, 149), its last rotating group is observed in the next day's opener, so each student keeps two marks in the unit. Each removes one 40-minute meeting and saves 35 minutes of teaching.

| Year | Fold course day | Into day | Minutes saved |
|---|---|---|---|
| 3 | 5 (viewfinder call drill) | 6 | 35 |
| 3 | 21 (sound-on-cue drill) | 22 | 35 |
| 3 | 37 (shot-order card drill) | 38 | 35 |
| 3 | 42 (movement and force drill) | 43 | 35 |
| 4 | 68 (angle and light drill) | 69 | 35 |
| 4 | 82 (move-a-little drill) | 83 | 35 |
| 4 | 88 (capture-in-roles drill) | 89 | 35 |
| 4 | 102 (balance and contrast drill) | 103 | 35 |
| 5 | 134 (eye-path drill) | 135 | 35 |
| 5 | 139 (tell-apart drill) | 140 | 35 |
| 5 | 149 (stand-in object drill) | 150 | 35 |
| 5 | 156 (wash-frame drill) | 157 | 35 |

Total: 12 of the frame's 192 days, 4 of each year's 64, leaving 60 a year (180 over the band) and saving 420 minutes of teaching. Every critique, revision, showing, check and respond day stays. Where the lost weeks fall before a course-level check, the check keeps its week if the school's lost days fall outside it; otherwise it moves to the nearest week free of the grade's core checks (CALENDAR.md tool a).

## For the lead

1. **Units 3 and 7 show after the respond day.** The frame fixes their check days at 47-48 and 109-110 inside 16- and 14-day units, which leaves two days after the checks; this file puts the respond day next and the class viewing last (days 50 and 112), so every piece shown is finished and nothing is scored on the viewing. Unit 11's check days (174-175) leave only the respond day after, so its viewing comes before the checks (day 173). If the lead wants one pattern, the frame's Units table would need to move those check days, which this file does not do.
2. **The frame's year-end labels say "Samples units 1 to 3" (and 5 to 7, 9 to 11),** while the items listed sample only the two earlier units and the unit just before is carried unscored, as the frame's own rule says ("never the unit just before it"). This file states what is sampled; the frame's label could say "Samples units 1 and 2; carries unit 3" (and the same for years 4 and 5).
3. **Unit 2 and unit 6 have no talk or written item,** only kept cards, guide look-fors and rotating look-fors, so their two check days are self-check and kept-card days. That is the frame's evidence line; noted so the unit plan does not add a talk item.
4. **The once-a-week path's merged check sessions** (units 3 and 7) fit the frame's talk-and-written day form (written 10, talk 18, set-up and clean-up 7, slack 5) exactly; there is no slack for a written item that runs long. Unit plans should keep the written item to 8 minutes there. Unit 11's merged check session holds the written item (about 10) and the kept criteria card (about 15) with set-up and clean-up.
5. **After-core clashes:** the check weeks are the frame's (grade 3 weeks 17 and 26, grade 4 weeks 17 and 25, grade 5 weeks 18 and 25); arts are specials, so `frame.py calendar` shows no stagger break for this course. The clashes with other specials stay the frame's For the lead item 2.
6. **Waiting on the structure pass** (docs/reviews/sequence-media-arts-grades-3-to-5-fixes-2026-11-26.md): the once-a-week rebalance for units 4, 8 and 12 (a frame change), the 30-minute period's talk items (an exception to APPROACH "Kinds of day"), and the frame's check-table wording that this file's items now go beyond.
