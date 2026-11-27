# Scope and sequence: Music, grades K to 2

Course `music-grades-k-to-2` (catalog id `music-k-2`), a band course for kindergarten, grade 1 and grade 2, draft written 2026-11-26, fixed 2026-11-26 after the expert read (docs/reviews/sequence-music-grades-k-to-2-fixes-2026-11-26.md).

The day record is [days.csv](../../../data/plans/music-grades-k-to-2/days.csv): 192 course days, 64 a year for three years, in the frame's 12 units (60 unit days a year) and 12 course-level days (two checks and two respond days a year). `stretch` is the unit number in the frame's Units table and `unit` is `<unit>.1`, since no unit is split into sections yet. This file sets purposes and evidence slots, not items, keys or lesson plans. There is no base text, so there is no source map.

## How the band runs

**Which grade's standards fall in which year (the bar's "Scope and sequence states").** National Core Arts Standards, 2014, music, by id only (STANDARD.md 2 and 3.1):

| Year of the band | Course days | Units | Standards claimed | Count (STANDARD.md 3.2) |
|---|---|---|---|---|
| Year K | 1 to 64 | 1 to 4 | Kindergarten ids only (`.Ka`, `.Kb`) | 19 |
| Year 1 | 65 to 128 | 5 to 8 | Grade 1 ids only (`.1a`, `.1b`) | 20 |
| Year 2 | 129 to 192 | 9 to 12 | Grade 2 ids only (`.2a`, `.2b`) | 20 |

That is 59 ids, every one taught and assessed in its own year, each named on its days by id with its line in data/standards/ncas-performance-standards-words.txt, never quoted. A year revisits the year before's ids as practice that returns, never as a claim. No pre-kindergarten id is claimed. The connecting ids (`MU:Cn10.1`, `MU:Cn11.1`) have one words line in every grade; each year meets them with its own music (units 1, 5 and 9 for Cn11; units 2, 6 and 10 for Cn10).

**Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year still claims only its grade's ids, so a child's record shows which grade's standards they met. In a class meeting year 2 before year 1, every retrieval opener carries its ten-minute reteach of the earlier technique as written.

**How school_day is counted.** The course meets two 40-minute sessions a week, 32 weeks a year, 96 weeks over the band. `school_day` counts across the band: year K is school days 1 to 160, year 1 is 161 to 320, year 2 is 321 to 480 (each year's own school day is the number less 160 or 320). Course day n sits on school day ceiling(5n / 2), so the two sessions fall on the third and fifth day of each week and course day n of a year sits in that year's week n / 2, rounded up. This is the even spread scripts/frame.py already uses for this course, written out so the days sit on the frame's and CALENDAR.md's weeks. The week of a day is (school_day - 1) // 5 + 1 within its year; every unit and check sits in the frame's weeks by it. A filled school_day here is the count frame.py reads; calendar.csv is regenerated from it.

**The day.** Each 40-minute session holds the set-up routine (about 3 minutes), a five-minute warm-up opener from earlier technique (or a listen to a work, or the set-up routine), teaching and music making, and clean-up and collecting work (about 3 minutes). A retrieval task takes ten minutes of the opener. Kinds follow the frame's "Day kinds": Understanding shows a technique in named steps with its step card or studies a work by listening; Fluency is short repeated drill with feedback on a technique already taught; Application is making up, rehearsing or performing with some choice, and the second application day of each unit holds its one critique, the next its revision; Check is the end-of-unit assessment or a course-level check; Respond acts on a check. No score comes from the day a technique is first taught.

**Every unit's shape.** The listen to a work comes first (the hook), the techniques come before the making that needs them, then a fluency day with the baseline look at the unit's main look-for (APPROACH "Growth"; rotating groups, not scored), the first application day, the critique on the second application day, the revision, the showing, the end-of-unit assessment and a respond day. Every showing has its critique and revision before the end-of-unit assessment. One piece a unit goes into the portfolio folder with a spoken one-line reflection (12 pieces over the band). Every recording is optional and sound only, on the school's device; the teacher's dated live mark is evidence.

**End-of-unit assessments.** Units 1, 5 and 9 end with a check day in groups of five at the teacher's spot (about four minutes a group, 24 minutes for 30 children, with the self-check first; the others draw in their listening logs with no instruments) and a respond day. Units 4, 8 and 12 end with the class concert in groups as the check day, then a respond day that re-rehearses and gives the family or school concert (the second showing). Units 2, 3, 6, 7, 10 and 11 take the course-level check that follows them as their end-of-unit assessment (frame, "Days"): their last two days are a rehearsal and revision day and a supported practice day, the kept card or log page is made on that last day and scored once from kept work with the check, which carries its codes (the supported practice day carries no `end` mark: scripts/sequence.py accepts the course-level check on the day after a unit's last day as its end-of-unit assessment), and the performance, talk and look-for items are taken on the check day. The check's respond day serves both and holds the unit's second showing for the partner class. Each item asks about each part of each code it lists, at most two talk items a child, and each child's evidence is collected once in its window. On a group check day, any unseen piece or menu song is played once to the whole class in the four spare minutes before the groups (the frame budgets 36 of the 40 minutes), not once a group; a group the teacher has not reached by the end takes its turn in the first ten minutes of the respond day, before the not-yet groups form.

**The four processes.** Each year carries all four artistic processes (create; perform, present or produce; respond; connect), and each unit touches at least the processes its frame row names. A unit need not claim all four: where a unit practices a process its owned rows do not name (creating in the reading units), the day says "practiced, not claimed", and no day claims an id outside its unit's owned rows. Each unit's Processes line names the days.

**Readiness and retrieval.** The progression rows give the count (rule 2, by grade number). Year K rows assume nothing: no readiness check anywhere in the band, and unit 1's day 1 carries none. Every year 1 row assumes its kindergarten row (last used one grade back) and every year 2 row assumes its grade 1 row, so each year 1 and year 2 unit opens with a retrieval task inside day 2's opener (the `retrieves` column), never a readiness check, and day 1 stays clean for the hook and the question. Earlier units of the same year that a unit builds on are retrieved where first needed: unit 3 day 41 (unit 1's high and low and unit 2's loud and soft, mu-k-read and mu-k-express), unit 4 day 53 (motifs from unit 3), unit 7 day 107 (unit 5's picture notation), unit 8 day 119 (unit 7's replies), unit 10 day 153 (unit 9's conducting and major and minor cards, mu-g2-read), unit 11 day 165 (unit 9's so, mi and la) and unit 12 day 183 (unit 11's A-B piece). Unit 9 builds on unit 7's twos and threes and major and minor as well as on unit 5, so day 131's opener retrieves mu-g1-invent (last used in year 1) beside day 130's retrieval.

| Unit | Earlier row | Last used | Treatment |
|---|---|---|---|
| 5 | mu-k-read, mu-k-respond | Year K, unit 1 | Retrieval, day 66 |
| 6 | mu-k-express, mu-k-choose | Year K, unit 2 | Retrieval, day 82 |
| 7 | mu-k-invent, mu-k-document | Year K, unit 3 | Retrieval, day 100 |
| 8 | mu-k-revise, mu-k-perform | Year K, unit 4 | Retrieval, day 116 |
| 9 | mu-g1-read, mu-g1-respond | Year 1, unit 5 | Retrieval, day 130 |
| 9 | mu-g1-invent | Year 1, unit 7 | Retrieval, day 131 |
| 10 | mu-g1-express, mu-g1-choose | Year 1, unit 6 | Retrieval, day 146 |
| 11 | mu-g1-invent, mu-g1-document | Year 1, unit 7 | Retrieval, day 164 |
| 12 | mu-g1-revise, mu-g1-perform | Year 1, unit 8 | Retrieval, day 180 |

**Leans and boundaries.** No row carries a cross_subject lean. The frame's contacts are carried as bridges in the notes: math counting on day 2 (kindergarten math counts objects in its unit 1, weeks 1 to 4, beside music week 1: beats counted aloud with the teacher only to four, the beat strip pointed at, no counting scored), days 101 and 130 (twos and threes said "1, 2" and "1, 2, 3", no number work), and no note values anywhere (math fractions are grade 3). ELA's class talk (SL.K.1, SL.1.1, SL.2.1) is practiced on the critique days; the first critique (day 14) carries the picture card bridge. Moving days name the physical education boundary.

**Safety and sensitivity.** Each hands-on day's note names its space, equipment and controls in the frame's words (cleared circle, set low recording level, voice rules, found percussion with no small parts and no glass, sticks never near a face, hands washed after shared instruments). Days that study a named community's music name its sensitivity flag and the source the sensitivity agent reads first. Day 179 carries the band's one hard-history flag (the juba). No unit studies a sacred or ceremonial work. Supplies, tools and safety columns are left out, as the arts brief says.

## Year K (kindergarten ids, course days 1 to 64)

### Unit 1. Beat, high and low

Course days 1 to 18, school days 3 to 45, year K weeks 1 to 9. *What can we hear in music, and what does music go with?* Owns mu-k-read and mu-k-respond: MU:Pr4.2.Ka, MU:Re7.2.Ka, MU:Re9.1.Ka, MU:Cn11.1.Ka.

**Arc.** Haydn's sudden loud chord opens the year (day 1) with the circle and sound rules. The steady beat (day 2) and the singing voice (day 3) are taught before anything uses them, drilled on day 4, then loud and soft and same and different with the body (day 5). The rhythm syllables start by ear: "ta" on each patted beat in day 9's echoes and "ti-ti" in day 13's, with no symbols and nothing scored, so year 1's picture notation (day 67) reads sounds the children already say. Haydn returns for the beat and the tune's shape (day 6), the connecting idea follows (day 7, one card kind for each part: another art, a school subject, a setting and daily life), the talking drum adds high and low tones from another place (day 8), and judging by taste is taught on day 10. "Kye Kye Kule" is learned on day 11, rehearsed with a made-up clapped answer (day 12), critiqued (day 14), revised (day 15) and shown to a partner class (day 16), where each child practices "I like it because it is ___" with a partner before day 17 scores it. **Why this order:** the longest kindergarten unit, because its four ids, two techniques and every routine are new; the beat and voice come first because every later day uses them.

**Assessments.** End-of-unit assessment day 17: the table item on three sung pairs (MU:Pr4.2.Ka, one prompt per pair), eight beats and the tune traced on an unseen Curio Class original (MU:Re7.2.Ka), and two talk items (MU:Re9.1.Ka; MU:Cn11.1.Ka, drawn from four cards, one for each part). Respond day 18.

**Processes.** Create: days 12, 15 (practiced, not claimed). Perform: days 2 to 5, 9, 11 to 18. Respond to another artist's work: days 1, 5 to 8, 10, 14, 16, 17. Connect: days 1, 6 to 8, 11, 16, 17.

**Candidate settled.** The set-up minutes for 30 children with sticks (criterion 9): kept, 0 days added. Day 2 teaches the tub routine (out by rows, back by rows, about 3 minutes), and every day's set-up and clean-up minutes sit inside the 40.

### Unit 2. Loud and soft, fast and slow

Course days 19 to 36, school days 48 to 90, year K weeks 10 to 18. *How do singers and players show what a song means, and which music do we like?* Owns mu-k-express and mu-k-choose: MU:Pr4.3.Ka, MU:Re8.1.Ka, MU:Pr4.1.Ka, MU:Re7.1.Ka, MU:Cn10.1.Ka.

**Arc.** Grieg's growing tune opens the unit (day 19). Voice quality (the whisper, speaking and singing voices) and the small and big voice (day 20) and the tempo in the feet (day 21) are taught and drilled (day 22), then used to decide how the lullaby fits its words (day 23). Taiko (day 24) and a pointing drill (day 25) build the hearing of a performer's change. The interests list and the listening log (day 26), the menu of three (day 27) and the log drill (day 28) teach choosing; the "I chose ___ because ___" sentence, with a reason from what the child likes, knows or can do, and the sleepy bear's option follow (day 29). Grieg and taiko side by side (day 30) close the listening. Groups pick and rehearse (day 31), drill (day 32), practice picking for a character (day 33), critique (day 34), revise (day 35) and make the kept log page (day 36). **Why this order:** both techniques come before the singing that needs them; the choosing ids come after the listening so a child has heard enough music to choose among.

**Assessments.** The end-of-unit assessment is the year K mid-year check (day 37, week 19), as the frame sets: the performance item (MU:Pr4.3.Ka in three prompts: soft then loud, slow then fast, whispered then sung, the fitting way pointed to for each), two talk items (MU:Re8.1.Ka on an unseen original that gets louder at one point and faster at another, each change shown; MU:Pr4.1.Ka), the look-for on the group's way and "because" (MU:Cn10.1.Ka, a reason from tastes, knowledge or skills), and the day 36 log page (MU:Re7.1.Ka), scored once from kept work. Respond day 38, with the partner-class showing.

**Processes.** Create: days 31, 35. Perform: days 20 to 23, 31, 32, 34 to 36. Respond: days 19, 24 to 28, 30, 33, 34, 36. Connect: days 19, 23, 24, 26, 29, 33.

**Candidate settled.** A lullaby from an Asian or Native American community beside Arrorró: dropped. Year K already reaches Asia through the Japanese American taiko ensemble, Africa in unit 1 and Latin America in Arrorró, and Native American makers come in units 5 and 10. A lullaby the children would sing needs that community's own word that it is open to be taught, which a unit plan cannot settle from a page, and the unit's 18 days are full with five ids.

### Unit 3. Making up music

Course days 39 to 48, school days 98 to 120, year K weeks 20 to 24. *How do musicians make up a new idea, and how can we keep it?* Owns mu-k-invent and mu-k-document: MU:Cr1.1.Ka, MU:Cr1.1.Kb, MU:Cr2.1.Ka, MU:Cr2.1.Kb.

**Arc.** Beethoven's four-sound motif (day 39), exploring by doing with McFerrin (day 40), a motif from a movement (day 41, opened by retrieving unit 1's high and low and unit 2's loud and soft) and the drill (day 42) teach inventing; picking (day 43) and keeping in picture symbols (day 44) are taught as two ids on two days. Groups make (day 45), critique (day 46), revise (day 47), then play the idea-bank chain and finish the kept card (day 48). **Why this order:** motifs are made from unit 1's beat and high and low and unit 2's loud and soft, and the pick comes before the keeping, as the two Cr2.1 ids ask. Shortest kindergarten unit: four ids, one technique.

**Assessments.** The end-of-unit assessment is the year K year-end check (day 49, week 25): the two performance items (MU:Cr1.1.Ka, beat and melodic shape each prompted; MU:Cr1.1.Kb from a new movement card), the talk item on the pick (MU:Cr2.1.Ka) and the day 48 card (MU:Cr2.1.Kb), scored once from kept work. Respond day 50.

**Processes.** Create: days 40 to 48. Perform: days 42, 45 to 48. Respond: days 39 to 41, 43, 46. Connect: days 39, 41.

**Candidate settled.** A motif-built piece by a living maker from Asia or Africa: kept, 0 days added, a ten-minute listen inside day 41, described and linked; it gives the unit a living maker beyond the United States and Europe.

### Unit 4. Our first concert

Course days 51 to 64, school days 128 to 160, year K weeks 26 to 32. *How do musicians make their music better, and how do we play for an audience?* Owns mu-k-revise and mu-k-perform: MU:Cr3.1.Ka, MU:Cr3.2.Ka, MU:Pr5.1.Ka, MU:Pr5.1.Kb, MU:Pr6.1.Ka, MU:Pr6.1.Kb.

**Arc.** Ella Jenkins (day 51) opens the performer's view of an audience. The practice card (day 52) and improving a motif with help (day 53) are taught before the drill and baseline (day 54); Raffi and audience manners (day 55) and the expressive plan (day 56) follow. Groups rehearse (day 57), drill manners (day 58), critique with the record sheet's rehearsal mark (day 59), revise (day 60), share the finished motif (day 61) and run the concert (day 62). **Why this order:** the concert is built from the year's songs and unit 3's idea bank, and it ends the year after the year-end check (CALENDAR.md weeks 29 to 32 hold every core year-end check in K).

**Assessments.** End-of-unit assessment day 63 (week 32), the class concert in groups: the talk item on the change (MU:Cr3.1.Ka), look-fors (MU:Cr3.2.Ka; MU:Pr5.1.Ka against the day 59 mark; MU:Pr6.1.Ka; MU:Pr6.1.Kb) and the table item on a practice way (MU:Pr5.1.Kb). Respond day 64 with the family concert.

**Processes.** Create: days 53, 57, 59, 60, 63. Perform: days 52, 54 to 64. Respond: days 51, 53, 55, 59, 63. Connect: days 51, 55, 64.

**Candidate settled.** A doubled version of every group part for the home room: kept, 0 days added, written on the concert plan card on day 57.

## Year 1 (grade 1 ids, course days 65 to 128)

### Unit 5. Beat and tune around the world

Course days 65 to 80, school days 163 to 200 (year 1 school days 3 to 40), year 1 weeks 1 to 8. *What jobs do beat and tune do in music from different places?* Owns mu-g1-read and mu-g1-respond: MU:Pr4.2.1a, MU:Pr4.2.1b, MU:Re7.2.1a, MU:Re9.1.1a, MU:Cn11.1.1a.

**Arc.** Sousa's march (day 65), the retrieval (with "ta" and "ti-ti" echoed by ear) and melody direction (day 66), then picture notation (day 67) and its drill (day 68). Nakai's flute (day 69) and "Sakura Sakura" (day 70) carry beat and tune in two more places, drilled on day 71. Judging for a purpose (day 72) and connecting (day 73, with a short listen to Vivaldi's "Spring", 1725, beside "Sakura Sakura" and the spring picture) are taught before the making: groups read and play with "Sakura Sakura" (day 74), drill (day 75), critique (day 76), revise (day 77) and show it to a partner class, then make the kept log page (day 78). **Why this order:** reading begins after the summer's retrieval of the year K beat and listening routine, and the notation taught here is what unit 7 writes with.

**Assessments.** End-of-unit assessment day 79: performance items (MU:Pr4.2.1a, beat and melody direction each prompted; MU:Pr4.2.1b), two talk items (MU:Re7.2.1a, MU:Cn11.1.1a) and the day 78 log page (MU:Re9.1.1a). Respond day 80.

**Processes.** Create: days 74, 77. Perform: days 66 to 68, 70, 71, 74 to 80. Respond: days 65, 66, 69, 72, 73, 76, 78 to 80. Connect: days 65, 69, 70, 73, 79.

**Candidate settled.** A fourth piece from Africa or South America with a clear beat for a purpose: dropped. Year 1 already reaches Africa (unit 6) and South America (unit 8), the end item uses an unseen recording from a culture not studied, and a fourth work would crowd a 16-day unit that also starts reading.

### Unit 6. Two ways to sing it

Course days 81 to 96, school days 203 to 240 (year 1 school days 43 to 80), year 1 weeks 9 to 16. *How do loudness and speed change what a song means, and how do we pick music for a purpose?* Owns mu-g1-express and mu-g1-choose: MU:Pr4.3.1a, MU:Re8.1.1a, MU:Pr4.1.1a, MU:Re7.1.1a, MU:Cn10.1.1a.

**Arc.** Brahms (day 81), the retrieval and one song sung two ways (days 82 and 83) and the drill (day 84). Ladysmith Black Mambazo (day 85) and a second soft song (day 86) teach naming a performer's choice, drilled on day 87. The menu for a purpose (day 88), interests and experiences (day 89) and the "we chose ___ because ___" sentence (day 90) teach choosing. Groups pick and map (day 91), drill (day 92), practice a log pick (day 93), critique (day 94), revise (day 95) and make the kept log page (day 96). **Why this order:** the purpose that unit 5's beat and pitch served grows into loudness and speed chosen for a purpose, which unit 7's reply phrases use.

**Assessments.** The end-of-unit assessment is the year 1 mid-year check (day 97, week 17): the performance item (MU:Pr4.3.1a), two talk items (MU:Re8.1.1a, with a prompt for the loudness choice and one for the speed choice; MU:Re7.1.1a), the look-for (MU:Cn10.1.1a) and the day 96 log page (MU:Pr4.1.1a). Respond day 98, with the partner-class showing.

**Processes.** Create: days 91, 95. Perform: days 82 to 84, 91, 92, 94 to 96. Respond: days 81, 82, 85 to 89, 93, 94, 96. Connect: days 81, 85, 86, 89, 90.

**Candidate settled.** A lullaby or soft song by a living maker from Asia or the Americas: kept, 0 days added, inside day 86 as the second performer whose choice the class names.

### Unit 7. Reply phrases

Course days 99 to 112, school days 248 to 280 (year 1 school days 88 to 120), year 1 weeks 18 to 24. *How do musicians answer a musical question, and how can we write our answer down?* Owns mu-g1-invent and mu-g1-document: MU:Cr1.1.1a, MU:Cr1.1.1b, MU:Cr2.1.1a, MU:Cr2.1.1b.

**Arc.** A call-and-response song (day 99), the retrieval and the reply phrase (day 100), meter by feel with "The Blue Danube" (day 101) and the drill (day 102). Major and minor by reference patterns with Mahler and "Frère Jacques" (day 103), inventing in both tonalities and meters (day 104) and the drill (day 105). Choosing (day 106) and documenting in unit 5's picture notation (day 107) come before partners make (day 108), critique (day 109), revise the next session (day 110), drill (day 111) and finish the kept card (day 112). **Why this order:** each Cr1.1.1b dimension (tonality, meter) is taught on its own day before ideas are invented in it.

**Assessments.** The end-of-unit assessment is the year 1 year-end check (day 113, week 25): two performance items (MU:Cr1.1.1a; MU:Cr1.1.1b with the tonal and the metric mark apart), the talk item (MU:Cr2.1.1a) and the day 112 card (MU:Cr2.1.1b). Respond day 114, with the partner-class chain.

**Processes.** Create: days 100, 102, 104 to 112. Perform: days 100 to 102, 105, 108 to 112. Respond: days 99, 101, 103, 106, 109. Connect: days 99, 101, 103.

**Candidate settled.** A call-and-response song from a West African or African American tradition, from that community's own published teaching: kept, 0 days added, as day 99's hook (listen only); the unit plan picks a game or work song, not a sacred one.

### Unit 8. Songs for the day

Course days 115 to 128, school days 288 to 320 (year 1 school days 128 to 160), year 1 weeks 26 to 32. *How do musicians practice a hard part, and how do we fit a song to its audience?* Owns mu-g1-revise and mu-g1-perform: MU:Cr3.1.1a, MU:Cr3.2.1a, MU:Pr5.1.1a, MU:Pr5.1.1b, MU:Pr6.1.1a, MU:Pr6.1.1b.

**Arc.** Mariachi Los Camperos (day 115), the retrieval and rehearsal strategies (day 116), "Los pollitos dicen" and its hard spot (day 117) and the drill (day 118). Polishing a unit 7 reply (day 119) and performing for a purpose and audience (day 120) are taught before groups rehearse (day 121), drill starts (day 122), critique (day 123), revise (day 124), share the finished reply (day 125) and run the concert (day 126). **Why this order:** the concert is built from the year's songs and replies and follows the year-end check.

**Assessments.** End-of-unit assessment day 127 (week 32), the class concert in groups: talk item (MU:Cr3.1.1a), look-fors (MU:Cr3.2.1a; MU:Pr5.1.1a against the day 123 mark; MU:Pr6.1.1a; MU:Pr6.1.1b) and the table item on the strategy (MU:Pr5.1.1b). Respond day 128 with the "songs for the day" concert.

**Processes.** Create: days 119, 121, 123, 124, 127. Perform: days 116 to 118, 120 to 128. Respond: days 115, 119, 123, 127. Connect: days 115, 117, 120, 125, 128.

**Candidate settled.** A doubled version of every group part for the home room: kept, 0 days added, on day 121's plan card.

## Year 2 (grade 2 ids, course days 129 to 192)

### Unit 9. Major or minor, twos or threes

Course days 129 to 144, school days 323 to 360 (year 2 school days 3 to 40), year 2 weeks 1 to 8. *How can we tell a song's tonality and its meter, and what do they do for the music?* Owns mu-g2-read and mu-g2-respond: MU:Pr4.2.2a, MU:Pr4.2.2b, MU:Re7.2.2a, MU:Re9.1.2a, MU:Cn11.1.2a.

**Arc.** Joplin (day 129), the retrieval and meter by conducting (day 130), the retrieval of unit 7's major and minor and twos and threes and tonality by reference patterns (day 131) and the drill (day 132). Rhythm with a rest (day 133) and so, mi and la on the staff (day 134) are taught and drilled (day 135). "Arirang" (day 136) and the "Tumbalalaika" refrain (day 137), both sung and conducted by the class, carry tonality, meter, purpose and setting in songs of two cultures chosen for performance; judging for a purpose follows (day 138). Groups read and play an accompaniment (day 139), critique on the second application day (day 140), revise the next session (day 141), then show it to a partner class and make the kept log page (day 142); the reading and conducting drill runs in the openers of days 140 and 141. **Why this order:** tonality and meter are named before the songs that show them, and the melody reading here is what unit 11's patterns inside a given tonality need.

**Assessments.** End-of-unit assessment day 143: the table item (MU:Pr4.2.2a, tonality and meter each prompted), the performance item (MU:Pr4.2.2b, rhythm and melody), two talk items (MU:Re7.2.2a, MU:Cn11.1.2a) and the day 142 log page (MU:Re9.1.2a). Respond day 144.

**Processes.** Create: day 139. Perform: days 130 to 137, 139 to 144. Respond: days 129, 131, 137, 138, 140 to 144. Connect: days 129, 136, 137, 143.

**Candidate settled.** A piece in threes or in minor from Africa or the Americas: dropped. Year 2 reaches Africa (unit 11), the Americas (Joplin, Shenandoah) and living makers (units 10 and 11), and unit 9 already carries three works and the new staff reading.

### Unit 10. How performers show meaning

Course days 145 to 160, school days 363 to 400 (year 2 school days 43 to 80), year 2 weeks 9 to 16. *How do music makers plan sounds to show what they mean, and how do we explain the music we pick?* Owns mu-g2-express and mu-g2-choose: MU:Pr4.3.2a, MU:Re8.1.2a, MU:Pr4.1.2a, MU:Re7.1.2a, MU:Cn10.1.2a.

**Arc.** Boléro (day 145), the retrieval and smooth and short sounds (day 146), the expression map with planned parts (day 147) and the drill (day 148). Mozart's variations (day 149), a living maker's several takes (day 150) and Shenandoah (day 151) teach how choices serve intent, drilled on day 152. Explaining a pick (day 153, opened by retrieving unit 9's conducting and major and minor cards), interests and experiences (day 154, practiced again on day 160's log page before day 161 scores it) and the "we planned ___ because ___" line (day 155) come before groups map and rehearse (day 156), drill (day 157), critique (day 158), revise (day 159) and make the kept log page and map card (day 160). **Why this order:** unit 9's named tonality and meter give the words for explaining a pick, and unit 11's patterns for a purpose use the plan made here.

**Assessments.** The end-of-unit assessment is the year 2 mid-year check (day 161, week 17): the look-for (MU:Pr4.3.2a), two talk items (MU:Re8.1.2a, MU:Re7.1.2a) and the day 160 log page and map card (MU:Pr4.1.2a, MU:Cn10.1.2a). Respond day 162, with the partner-class showing.

**Processes.** Create: days 147, 156, 159. Perform: days 146 to 148, 156 to 160. Respond: days 145, 149 to 154, 158, 160. Connect: days 145, 149 to 151, 154, 155, 160.

**Candidate settled.** A second living maker from Asia or Africa who performs one tune several ways: kept, 0 days added, inside day 150; it keeps a living maker in the year beside Shenandoah (1957 to 2021).

### Unit 11. Patterns into a piece

Course days 163 to 176, school days 408 to 440 (year 2 school days 88 to 120), year 2 weeks 18 to 24. *How do musicians build a piece from patterns, and how do we put our patterns in order?* Owns mu-g2-invent and mu-g2-document: MU:Cr1.1.2a, MU:Cr1.1.2b, MU:Cr2.1.2a, MU:Cr2.1.2b.

**Arc.** Clapping Music (day 163), the retrieval and rhythm patterns for a purpose (day 164), melody patterns on so, mi and la (day 165) and the drill (day 166). Patterns inside a given tonality and meter (day 167), Olatunji's locking patterns (day 168) and the drill (day 169), then explaining (day 170) and the A-B piece documented, combined and sequenced (day 171). Partners build (day 172), critique (day 173), revise the next session (day 174), drill (day 175) and finish the kept card (day 176). **Why this order:** improvising for a purpose comes before improvising inside a given frame, and the explanation and notation come after there are patterns to explain and write.

**Assessments.** The end-of-unit assessment is the year 2 year-end check (day 177, week 25): two performance items (MU:Cr1.1.2a, rhythm and melody; MU:Cr1.1.2b, meter and tonality), the talk item (MU:Cr2.1.2a) and the day 176 card (MU:Cr2.1.2b). Respond day 178, with the partner-class showing.

**Processes.** Create: days 164 to 167, 169 to 176. Perform: days 163 to 166, 169, 172 to 176. Respond: days 163, 168, 170, 173. Connect: days 163, 168.

**Candidate settled.** A pattern-built piece by a living maker from Asia or Latin America: dropped. Reich and Olatunji give two pattern models and unit 10 already adds a living maker from Asia or Africa; the 14 days carry two techniques and the A-B piece.

### Unit 12. Our morning concert

Course days 179 to 192, school days 448 to 480 (year 2 school days 128 to 160), year 2 weeks 26 to 32. *How do we judge a performance and make it better, and how do we fit it to our audience?* Owns mu-g2-revise and mu-g2-perform: MU:Cr3.1.2a, MU:Cr3.2.2a, MU:Pr5.1.2a, MU:Pr5.1.2b, MU:Pr6.1.2a, MU:Pr6.1.2b.

**Arc.** Florence Price's "Juba Dance" (day 179), the retrieval and the checklist on two adult takes (day 180), choosing a strategy (day 181) and the drill (day 182). Making sense of feedback on the unit 11 A-B piece (day 183) and performing for purpose and audience (day 184) come before groups rehearse (day 185), drill the checklist (day 186), critique (day 187), revise (day 188), share the finished piece (day 189) and run the last rehearsal with the kept checklist card (day 190). **Why this order:** the set criteria are taught on adult takes before any class take is judged, and the concert is built from the year's songs and unit 11's piece.

**Assessments.** End-of-unit assessment day 191 (week 32), the class concert in groups: talk item (MU:Cr3.1.2a), look-fors (MU:Cr3.2.2a, MU:Pr6.1.2a accurate and expressive, MU:Pr6.1.2b), the day 190 checklist card (MU:Pr5.1.2a) and the table item on the strategy (MU:Pr5.1.2b). Respond day 192 with the morning concert.

**Processes.** Create: days 183, 185, 187, 188, 191. Perform: days 180 to 182, 184, 185, 187 to 192. Respond: days 179, 180, 183, 186, 187, 190, 191. Connect: days 179, 184, 189, 192.

**Candidate settled.** The two adult takes written so each fails a different checklist line: kept, 0 days added, used on day 180.

## Course-level checks

| Check | Course days | Band school days | Year week | Unit's end-of-unit assessment | Earlier unit sampled |
|---|---|---|---|---|---|
| Year K mid-year | 37 (check), 38 (respond) | 93, 95 | 19 | Unit 2 | Unit 1: MU:Re7.2.Ka, a new piece |
| Year K year-end | 49, 50 | 123, 125 | 25 | Unit 3 | Unit 1: MU:Re9.1.Ka, a new piece |
| Year 1 mid-year | 97, 98 | 243, 245 | 17 | Unit 6 | Unit 5: MU:Pr4.2.1b, a new card |
| Year 1 year-end | 113, 114 | 283, 285 | 25 | Unit 7 | Unit 5: MU:Re9.1.1a, new pieces |
| Year 2 mid-year | 161, 162 | 403, 405 | 17 | Unit 10 | Unit 9: MU:Pr4.2.2b, a new card |
| Year 2 year-end | 177, 178 | 443, 445 | 25 | Unit 11 | Unit 9: MU:Re7.2.2a, a new piece |

All six sit on the frame's and CALENDAR.md's target weeks, off every core check week for the grade (K: 14 to 17 and 29 to 32; grade 1: 14 to 16, 19 and 29 to 32; grade 2: 14 to 16, 18 to 20, 28, 29, 31 and 32). Arts are specials in K to 5, so these checks do not count against the classroom teacher's stagger (CALENDAR.md rule 1). Each check follows its unit's last day directly, and each is that unit's end-of-unit assessment (the frame's after-core design), so the unit's items are its own evidence line, taken once; the items for earlier units come from earlier units only, as one sample on a new piece or card in a task form not given in the last two weeks. Each check is followed by its respond day.

**Codes not sampled on a course-level check (rule 3), and why.** The frame's Course-level checks table fixes what each check holds, and each check's 40 minutes are full with its unit's whole evidence line and one earlier sample (six groups of five at about four minutes each, at most two talk items a child). These codes are assessed at their own unit's end only:
- Units 1, 5 and 9, the codes the checks do not sample: MU:Pr4.2.Ka, MU:Cn11.1.Ka; MU:Pr4.2.1a, MU:Re7.2.1a, MU:Cn11.1.1a; MU:Pr4.2.2a, MU:Re9.1.2a, MU:Cn11.1.2a. Each check samples one earlier code by design (frame); the others return as warm-up practice in later units.
- Units 4, 8 and 12, all six codes each (MU:Cr3.1, Cr3.2, Pr5.1 a and b, Pr6.1 a and b in each grade): the concert unit comes after the year-end check, because weeks 29 to 32 hold every core year-end check in K to 2 (CALENDAR.md tool c), and its own check day in week 32 assesses every id.

## Shorter path

**The once-a-week path (the frame's 32 sessions a year).** Each unit keeps its demonstration with the step card opened by the listen, one making or rehearsal day with the critique, its showing and check, and one respond day; fluency days fold into the warm-up openers and the understanding days merge. Every check and respond day keeps its own session, so the check sessions stay in weeks 19 (year K) or 17 (years 1 and 2) and 25, and the respond sessions fall a week later. Sessions, by course days merged:

| Unit | Sessions | Course days in each session |
|---|---|---|
| 1 | 9 | 1-2, 3-5, 6-7, 8-10, 11-13, 14, 15-16, 17, 18 |
| 2 | 9 | 19-20, 21-23, 24-25, 26-28, 29-30, 31-33, 34, 35, 36 |
| Year K mid-year | 2 | 37, 38 |
| 3 | 4 | 39-42, 43-45, 46, 47-48 |
| Year K year-end | 2 | 49, 50 |
| 4 | 6 | 51-54, 55-58, 59, 60-62, 63, 64 |
| 5 | 8 | 65-68, 69-71, 72-73, 74-75, 76, 77-78, 79, 80 |
| 6 | 8 | 81-82, 83-85, 86-87, 88-90, 91-93, 94, 95, 96 |
| Year 1 mid-year | 2 | 97, 98 |
| 7 | 6 | 99-102, 103-105, 106-108, 109, 110-111, 112 |
| Year 1 year-end | 2 | 113, 114 |
| 8 | 6 | 115-118, 119-122, 123, 124-126, 127, 128 |
| 9 | 8 | 129-132, 133-135, 136-137, 138-139, 140, 141-142, 143, 144 |
| 10 | 8 | 145-148, 149-150, 151-152, 153-155, 156-157, 158, 159, 160 |
| Year 2 mid-year | 2 | 161, 162 |
| 11 | 6 | 163-166, 167-169, 170-172, 173, 174-175, 176 |
| Year 2 year-end | 2 | 177, 178 |
| 12 | 6 | 179-182, 183-186, 187, 188-190, 191, 192 |

That is 32 sessions a year (year K 9, 9, 4, 6 and years 1 and 2 8, 8, 6, 6, with 4 check and respond sessions), 96 over the band. No merged session drops a critique, a revision, a kept-work making day or a respond day; the session holding a fluency day keeps its drill as the warm-up opener.

**A year about 10 days short.** Ten school days is two weeks, which for a course meeting twice a week is about four sessions. Each year names four fold-in days, one in each unit, and lists spares for a school that loses more of its own sessions. The fold-in days are fluency days: their drill moves into the five-minute warm-up opener of the next two sessions (which already hold an opener), nothing on them is assessed, and no owned part is cut. A baseline look that sat on a fold-in day moves to the next practice day. Each fold-in day saves its 40-minute session. Fold the days in the stretch where the sessions are lost, so the check sessions keep their weeks.

| Year | Fold-in days (40 minutes each) | Sessions | Spares, in order |
|---|---|---|---|
| Year K | 4, 25, 42, 54 | 64 to 60 (160 minutes) | 22, 28, 32, 58 |
| Year 1 | 68, 84, 102, 118 | 64 to 60 (160 minutes) | 71, 75, 87, 92, 105, 122 |
| Year 2 | 132, 148, 166, 182 | 64 to 60 (160 minutes) | 135, 152, 157, 169, 175, 186 |

Against the frame's 192 days, the twelve named fold-in days give 180 (60 a year); folding every spare as well gives 164.

**A shorter period.** A 30-minute session keeps set-up and clean-up (about 3 minutes each) and the five-minute opener, so it has 19 minutes for teaching and music making: the day's order stays, the second listen to a work moves into the next opener, and each check day splits over two sessions (three groups of five each), with the respond day after the second.

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; step cards, picture-notation cards, listening-log pages; found and low-cost instruments; one teacher device or none | Technique taught in steps; works studied by listening with their setting; making up and rehearsing with a critique and a revision; a showing each unit | A portfolio folder of 12 pieces over the band with spoken reflections; 12 showings, three of them concerts; two marks a unit per child on the main look-for | Met marks on the year's ids (19, 20, 20) and growth on the look-fors |

Nothing here has been tried with children, and Curio Class makes no claim that music study raises any other result.

## For the lead

1. **`observe` in a band course.** sequence.py accepts `observe` only where the course's grade is K, 1 or 2; this band's grade is `k-2`, so a K to 2 band course cannot use it. Not needed here; noted for the other K to 2 arts bands.
2. **Rule 3 coverage.** Twenty-six of the 59 codes are not sampled on any course-level check (listed under Course-level checks). The frame's table fixes the checks, and its time budget leaves no room; if L107 wants every code on a check, the frame would need one more item per check or a check on the concert unit, which the calendar's weeks 29 to 32 rule out in K to 2.
3. **Supplies ceiling (decided),** carried from the frame: $75 a class a year (Cory approved 2026-11-26, Desk q-frames-money-1); planning costs $55, $20 and $20, all optional beside the free path.
