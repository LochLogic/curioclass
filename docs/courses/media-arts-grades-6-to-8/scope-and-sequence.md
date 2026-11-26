# Scope and sequence: Media Arts, grades 6 to 8

Course `media-arts-grades-6-to-8` (catalog id `media-arts-6-8`), grades 6, 7 and 8, draft, written 2026-11-26 from the frame (docs/courses/media-arts-grades-6-to-8/frame.md), fixed the same day from the expert read (docs/reviews/sequence-media-arts-grades-6-to-8-fixes-2026-11-26.md). The days are in data/plans/media-arts-grades-6-to-8/days.csv; this page gives the judgment behind them. Units, owned rows and day counts are the frame's, unchanged.

## The band at a glance

- **Three years in one file.** Year 6, then year 7, then year 8, one after another: 192 course days, 64 a year. Each
  year holds four units (14, 18, 14 and 14 days), a mid-year course-level check with its respond day after the
  second unit, and a year-end course-level check with its respond day after the fourth.
- **Which grade's standards fall in which year** (National Core Arts Standards, 2014, media arts, by id; each action
  in its line of data/standards/ncas-performance-standards-words.txt, never quoted). Year 6 (days 1 to 64, units 1 to
  4) claims only the 18 grade 6 ids (`MA:...6`); year 7 (days 65 to 128, units 5 to 8) only the 18 grade 7 ids; year 8
  (days 129 to 192, units 9 to 12) only the 18 grade 8 ids. That is 54 in all, the count in STANDARD.md 3.2, and every
  one is on at least one day of its own year and has an end-of-unit item or look-for. A year meets the year before's
  ids again only as practice that returns, never as a claim.
- **Mixed-grade classes.** A school that teaches the band as one mixed class runs the three years in turn. Each year
  still claims only its grade's ids, so a student's record shows which grade's standards they met. A student who meets
  year 8 before year 7 gets the reteach each retrieval task carries.
- **Meeting days and school_day.** Two 40-minute sessions a week, 32 weeks a year, 96 weeks over the band. The
  `school_day` column counts school days across the band, as scripts/frame.py reads it: year 6 is school days 1 to
  160, year 7 is 161 to 320, year 8 is 321 to 480 (CALENDAR.md's school day s of a year is band school day
  s + 160 for year 7 and s + 320 for year 8). Course day n sits on band school day 2.5 x n, rounded up, the frame's even
  spread, so course day n of a year falls on that year's school day 2.5 x (its day in the year), rounded up. Week =
  (that year's school day - 1) // 5 + 1. This is the one formula; school_day is not re-counted to calendar.csv, which
  the lead regenerates at commit, and every unit and check sits in the frame's weeks by it.
- **The session.** Set-up about 5 minutes (devices, trays, the day's step card), the teaching and making, clean-up and
  hand-back about 5 (7 on a cutting, gluing or stop-motion day). A retrieval task takes ten minutes inside an opener.
- **Kinds.** Understanding: a technique shown in named steps with its step card, or a work studied with the unit's
  words (the artistic process of responding lives here, never on a respond day). Fluency: short repeated drills of a
  technique already shown, with feedback. Application: planning, making, producing, the critique, the revision, the
  showing. Check: the self-check and the written items, a screening, or the portfolio page. Respond: a second try at
  the part marked not yet, after every mark is in; nothing is assessed on a respond day.
- **Every unit's arc.** Day 1 is the hook: the compelling question and a work studied. Day 2 opens with the retrieval
  task and shows the technique with its step card. A fluency day follows with the baseline look at the unit's main
  look-for (APPROACH "Growth"), so every student has two marks a unit. Technique days come before the making that
  needs them. The second making day holds the unit's one critique (describe, ask, suggest); the next day is the
  revision; every unit shows its work before its check; the check is followed by one respond day. One piece a unit goes
  into the portfolio with a one-line reflection (12 over the band).
- **The four processes.** Each year claims all four artistic processes (creating; producing, which in media arts is
  the performing or presenting process; responding; connecting), and each unit touches at least the processes the
  frame's Units table names for it. A unit need not claim all four, and no day claims an id outside its unit's owned
  rows. Where a unit's own ids hold no connecting, a two-question setting card on an existing work-study day (who
  made it and for whom, where and when, and what it tells us about that time and place) practices connecting without
  a claim: days 15, 38, 84, 102, 148 and 166.
- **Scored evidence.** Each owned id is scored once, in its unit, by the form the frame's "End-of-unit evidence" line
  names: a guide look-for on a kept piece, a kept card scored with the piece, at most two written items a student on a
  check day, or look-fors marked at a screening. The production ids (MA:Pr5.1.6b, 6c, 7b, 7c, 8b, 8c) are marked from
  each student's kept trials and production-log line over the unit's last three production sessions, ten students a
  session (days 26 to 28, 90 to 92, 154 to 156); those days carry `assess` = end. No score comes from a day a technique
  is first shown.
- **The paper path.** No student device and no student account. Every day runs from printed step cards, work cards,
  case cards and paper media tools (card viewfinder, flip book, paper film strip, drawn animatic, sound score performed
  live, paper screen); a shared school device per team of five or six is one way in where a school has one. Each
  making day's note names its equipment, its free path and its safe use.
- **Safety, every unit** (from the frame, "from memory" until the fresh safety read): no filming, photographing or
  recording a student without the family's yes, and a face or voice never required; no flashing light or strobe, and
  every work's excerpt checked against the flash rule first; screen breaks (no student at a screen more than about
  fifteen minutes at a stretch); headphones, where used, at low volume; lamps low-power, never shone in eyes, kept off
  paper; cords taped down or none; blades by an adult only; non-toxic supplies; hands washed after glue and found
  objects.
- **Sensitivity.** Each day that studies a flagged work or setting names the flag in its note (units 1, 2, 3, 4, 5, 6,
  7, 8, 9, 10, 11 and 12). Leave-out units named on the course page: 4, 5 and 12; each has its swap in the note of the
  day it touches. Every task tied to a student's own life offers a public, invented or class-shared option marked the
  same.
- **Works range.** Year 6: France, Russia, Inuit Canada, India, Egypt, the United Kingdom, Ukraine, Japan, the
  United States (living makers Kunuk and Bey). Year 7: the United States, Senegal, France, Ho-Chunk Nation, India, the
  United Kingdom (living makers Hopinka and the unit 7 Candidate pick, a maker working after 2000). Year 8: the
  United States, Cree Quebec, France, Kenya, China, Ireland, India (living makers Diamond, Kahiu and Moore, and the
  unit 12 Candidate pick, a maker working after 2000). The works lean to the twentieth century and none is
  interactive; For the lead item 6 names the change the unit plans may make.
- **Time figure.** 80 minutes a week, 40 on the once-a-week path; the association's checklists give no media arts
  weekly minimum, so no gap is claimed (frame Days bullet).

## Logic model (one page)

| Inputs | Activities | Outputs | Outcome claimed |
|---|---|---|---|
| Two 40-minute sessions a week; step cards, work cards, case cards, paper media tools, found objects; an optional shared device per team | Technique shown in steps; works studied with their setting; planning and producing in roles with a critique and a revision; a showing or screening every unit | A portfolio of 12 pieces over the band with reflections; 12 showings; two marks a unit per student on the main look-for | Met marks on each year's 18 ids, and growth on the look-fors |

Nothing here has been tried with students, and Curio Class makes no claim that arts study raises any other result.

## Readiness and retrieval (rule 2, by grade number)

Every unit assumes only the rows of its two threads one grade back, so every unit opens with a retrieval task in the
first ten minutes of day 2 (the `retrieves` column), and no unit needs a readiness check: no day carries `assess` =
readiness, and every first day stays clean for the hook.

| Unit (day 2) | Rows retrieved | Last used | Treatment |
|---|---|---|---|
| 1 (day 2) | ma-g5-read; ma-g5-society | grade 5, Media Arts 3 to 5 unit 9 | retrieval, with the ten-minute reteach of the grade 5 technique (not a core course, so a student may be new to media arts) |
| 2 (day 16) | ma-g5-ideas; ma-g5-craft | grade 5, its unit 10 | retrieval with reteach |
| 3 (day 36) | ma-g5-make; ma-g5-judge | grade 5, its unit 11 | retrieval with reteach |
| 4 (day 50) | ma-g5-present; ma-g5-sources | grade 5, its unit 12 | retrieval with reteach |
| 5 (day 66) | ma-g6-read; ma-g6-society | grade 6, unit 1 | retrieval |
| 6 (day 80) | ma-g6-ideas; ma-g6-craft | grade 6, unit 2 | retrieval |
| 7 (day 100) | ma-g6-make; ma-g6-judge | grade 6, unit 3 | retrieval |
| 8 (day 114) | ma-g6-present; ma-g6-sources | grade 6, unit 4 | retrieval |
| 9 (day 130) | ma-g7-read; ma-g7-society | grade 7, unit 5 | retrieval |
| 10 (day 144) | ma-g7-ideas; ma-g7-craft | grade 7, unit 6 | retrieval |
| 11 (day 164) | ma-g7-make; ma-g7-judge | grade 7, unit 7 | retrieval |
| 12 (day 178) | ma-g7-present; ma-g7-sources | grade 7, unit 8 | retrieval |

Each year 7 and year 8 retrieval task carries its reteach for a student in a mixed class who meets that year first.

## Year 6 (grade 6 ids; days 1 to 64, school days 1 to 160)

### Unit 1. Reading the frame

Days 1 to 14, weeks 1 to 7. Ids: MA:Re7.1.6a, MA:Re7.1.6b, MA:Cn11.1.6a, MA:Cn11.1.6b (ma-g6-read, ma-g6-society).

Reading comes first: four works are studied on days 1, 4 and 5 (the Lumière brothers beside Starevich on day 1, a
filmed record against a staged scene, two styles; Kunuk; Phalke), with the shot-size step card shown on day 2 on
stills from day 1 and drilled on day 3, so the written analysis (day 6, one technique and one style) has a technique
and words under it. The copyright and ethics card comes on day 7, just before the investigation piece needs it
(planned on day 8, made on days 10 and 11 with the three-line tie card at the end of day 10, critiqued on day 11,
revised and shown in a pair gallery walk on day 12).

- Processes: responding days 1 to 6 and 13; connecting days 4, 5, 7 to 12; creating days 8, 10 to 12; presenting day 12.
- End-of-unit assessment: day 13, two written items on an unseen public domain clip (Re7.1.6a its parts and meaning;
  Re7.1.6b one technique and one style and how they steer), with the investigation piece and its three-line tie card
  (Cn11.1.6a, guide look-for, so every tie the standard names is asked: the piece shows one, the card the other three)
  and its media-ethics card (Cn11.1.6b) scored after the session. Respond: day 14.
- Candidate (flash and content check of each work at its excerpt): kept, no day cost; the teacher checks before day 1
  and each work day's note says so.

### Unit 2. Plan, test, produce

Days 15 to 32, weeks 8 to 16. Ids: MA:Cr1.1.6, MA:Cr2.1.6, MA:Pr5.1.6a, MA:Pr5.1.6b, MA:Pr5.1.6c (ma-g6-ideas,
ma-g6-craft).

The longest unit of the year, by load: five ids, a planning portfolio and a team production. Methods are shown (day
16) before teams set aims (17); the flip book and stop motion, the ordinary tool use, are shown and drilled (18, 19)
before Lye's experimental use (20); the portfolio card (21) comes before the storyboard and mockup (22); the role cards
and the constraint (23, 24) come before production (25 to 28). The critique sits in production session 3 (27) and the
revision on day 28; the screening is day 29 and the portfolio and role record are finished on day 30.

- Processes: creating days 16, 17, 21, 22, 25 to 28; producing days 18 to 20, 23 to 30; responding on the works (review)
  days 15 and 20 and as audience on day 29; connecting practiced on day 15's setting card (the Frenkel brothers' Cairo
  studio and its first audience), no id claimed.
- End-of-unit assessment: production look-fors on days 26 to 28 (Pr5.1.6b and 6c), then day 31: self-check and the
  portfolio's last page, with Cr1.1.6 and Cr2.1.6 as guide look-fors on the portfolio and Pr5.1.6a on the kept role
  record. Respond: day 32.
- Candidate (a living animator from Asia, for range): dropped. Year 6 already has Asia (Phalke, Ozu) and living
  makers (Kunuk, Bey), and a third work would take a production day the five ids need.

### Mid-year course-level check, year 6

Day 33 (school day 83, week 17), respond day 34 (school day 85). See "Course-level checks" below.

### Unit 3. Point of view

Days 35 to 48, weeks 18 to 24. Ids: MA:Cr3.1.6a, MA:Cr3.1.6b, MA:Re8.1.6, MA:Re9.1.6 (ma-g6-make, ma-g6-judge).

Vertov opens with many angles and the given criteria card (35); the angle step card comes on day 36 and its drill on
37, before Ozu's still, low camera (38) and the approaches students try (39). Chosen criteria and the context card
(40) come before the critique that uses them (43). The revision log (44) and the audience refinement (45) come after
the critique; the sequences are shown on day 46.

- Processes: responding days 35, 38, 40, 41, 43 and 47; creating days 36, 37, 39, 42 to 46; presenting day 46;
  connecting practiced on day 38's setting card (postwar Japan and the family Tokyo Story shows), no id claimed.
- ELA lean: ma-g6-judge leans on class talk (ela:SL.6.1), owned by English language arts grade 6 unit 1 (school days
  1 to 32), well before day 40 (school day 100), so no bridge is needed; day 40's note carries the "if later" bridge
  for a school whose ELA runs late.
- End-of-unit assessment: day 47, two written items (Re8.1.6 an unseen piece's intent on the given criteria; Re9.1.6
  chosen criteria on a classmate's piece and production steps, with the context card and one constructive suggestion),
  with the sequence (Cr3.1.6a) and revision log (Cr3.1.6b) scored after the session. Respond: day 48.
- Candidate (a living maker known for point-of-view shots, from Africa or the Americas): kept, a ten-minute look
  inside day 41, no added day; the unit plan picks the maker, described and linked.

### Unit 4. Then and now: our screening

Days 49 to 62, weeks 25 to 31. Ids: MA:Pr4.1.6, MA:Pr6.1.6a, MA:Pr6.1.6b, MA:Cn10.1.6a, MA:Cn10.1.6b (ma-g6-present,
ma-g6-sources).

Hine (49) and Bey (51) frame the question of new meaning around the source log (50); the narrated photo sequence is
shown and drilled (52, 53) before research (54) and making (55). The piece is made in pairs, 60 seconds, each partner
owning one half and its forms, with a one-line card "how my half's forms back the message" kept and scored with the
piece for Pr4.1.6 (a pair piece never stands in for one student). Showing formats (56) come before the trial and the
critique (57), where each pair also writes a review of the trial with the review frame (how it went, one improvement,
one piece of audience evidence), so Pr6.1.6b is taught before day 61 scores it; the revision on day 58 puts that
improvement in place, and the run-through is day 59.

- Processes: connecting days 49 to 51, 54, 55 and 61; producing and presenting days 52, 53, 55 to 60; creating days
  55, 57, 58; responding on the works days 49 and 51 and in the review on day 61.
- End-of-unit assessment, two check days: day 60, the scored screening (15 pair pieces of about a minute with
  turnover in 25 minutes; Pr4.1.6 on each student's own half with their card, and the presenting tasks of Pr6.1.6a,
  marked at the screening); day 61, self-check and two written items (Pr6.1.6b the written review; Cn10.1.6b an unseen
  photograph's later meaning and cultural experience), with the showing plan (Pr6.1.6a) and source log (Cn10.1.6a)
  scored after the session. Respond: day 62.
- Candidate (an archive set from outside the United States, for range): dropped. Year 6's works already span four
  continents; the event research needs the days a third work would take. A swap of Hine for a non-US set remains the
  lead's option (frame fix review, lead item 6).

### Year-end course-level check, year 6

Day 63 (school day 158, week 32), respond day 64 (school day 160).

## Year 7 (grade 7 ids; days 65 to 128, band school days 161 to 320)

### Unit 5. Taste and technique

Days 65 to 78, weeks 1 to 7. Ids: MA:Re7.1.7a, MA:Re7.1.7b, MA:Cn11.1.7a, MA:Cn11.1.7b (ma-g7-read, ma-g7-society).

The reading routine reopens after the summer and moves to comparing two pieces with taste weighed: Guy-Blaché (65),
the long take against the cut (66, drilled 67), Sembène (68), then the written comparison (69). Careers (70) and the
invented feed (71, drilled 72, where each student also finishes their own lines of the class rules) come before the
explainer is planned (73), made (74, 75 with the critique), revised and shown beside the class rules in a pair gallery
walk (76), so the rules govern the year's later productions. Style comes in on day 68: Guy-Blaché's studio-staged
drama against Sembène's street film.

- Processes: responding days 65 to 69 and 77; connecting days 70 to 76; creating days 73 to 76; presenting day 76.
- End-of-unit assessment: day 77, two written items (Re7.1.7a; Re7.1.7b one technique and one style with taste) on
  two unseen public domain clips, with the
  explainer (Cn11.1.7a) and the rules card (Cn11.1.7b) scored after the session. Respond: day 78.
- Candidate (a media maker's own published account of their job, for a career card): kept on day 70, no added day.

### Unit 6. Prototype it

Days 79 to 96, weeks 8 to 16. Ids: MA:Cr1.1.7, MA:Cr2.1.7, MA:Pr5.1.7a, MA:Pr5.1.7b, MA:Pr5.1.7c (ma-g7-ideas,
ma-g7-craft).

Same place and shape as unit 2, one step harder: prototyping (80, 81) before the animatic is shown and drilled (82,
83); Hopinka (84) shows a method adapted; the resource check (85) comes before plans are judged against it (86); the
organizer role (87, 88) comes before production (89 to 92), the critique on day 91 and the revision on 92. The notice is
screened on day 93; portfolio and role record are finished on day 94.

- Processes: creating days 80, 81, 85, 86, 89 to 92; producing days 82 to 84, 87 to 94; responding on the works
  (review) days 79 and 84 and as audience on day 93; connecting practiced on day 84's setting card (Hopinka's language
  and family, under the day's flag), no id claimed.
- End-of-unit assessment: production look-fors on days 90 to 92 (Pr5.1.7b and 7c), then day 95: self-check and the
  portfolio's last page (Cr1.1.7, Cr2.1.7), with the role record (Pr5.1.7a). Respond: day 96, with the new-purpose card
  as unscored practice.
- Candidate (a third prototype-led work from Asia): dropped. Ray's Two carries Asia in unit 7, and the 18 days hold no
  free day.

### Mid-year course-level check, year 7

Day 97 (year 7 school day 83, week 17), respond day 98.

### Unit 7. A story in shots

Days 99 to 112, weeks 18 to 24. Ids: MA:Cr3.1.7a, MA:Cr3.1.7b, MA:Re8.1.7, MA:Re9.1.7 (ma-g7-make, ma-g7-judge).

The Kid (99) shows structure before the shot list is shown (100) and drilled (101); Ray's Two (102) and the criteria
builder (103) come before the shot list is written (104); stressing an element is shown (105) before production (106),
the critique (107) and the revision log (108, 109). The pieces are shown on day 110.

- Processes: responding days 99, 102, 103, 107 and 111; creating days 100, 101, 104 to 110; producing day 106;
  presenting day 110; connecting practiced on day 102's setting card (Calcutta in 1964, a rich boy and a poor boy), no
  id claimed.
- Beside ELA: English language arts grade 7 unit 4 (text against film, RL.7.7) uses the same shot words in about the
  same weeks; practiced, not owned, and neither course waits on the other.
- End-of-unit assessment: day 111, two written items (Re8.1.7 on the student's own criteria; Re9.1.7 the criteria
  justified and used on a classmate's piece and one production step, with the context card), with the story piece
  (Cr3.1.7a) and revision log (Cr3.1.7b) scored after the session. Respond: day 112.
- Candidate (a living storyteller in film from the Americas): kept, a ten-minute look inside day 102, no added day; it
  gives year 7 a second living maker beside Hopinka, and the pick is a maker working after 2000, for range of period.

### Unit 8. Media that teaches

Days 113 to 126, weeks 25 to 31. Ids: MA:Pr4.1.7, MA:Pr6.1.7a, MA:Pr6.1.7b, MA:Cn10.1.7a, MA:Cn10.1.7b (ma-g7-present,
ma-g7-sources).

Smith (113) and Edgerton (114) show media that made knowledge; the source log with model works (115) and the slowed
motion sequence (116, drilled 117) come before research (118) and making (119, in pairs, 60 seconds, each
partner's half and one-line card scored for Pr4.1.7, as in unit 4); evaluating formats (120) comes before the trial
and critique (121, with the review frame and a growth line since unit 4, so Pr6.1.7b is taught before day 125), the
revision that puts the improvement in place (122) and the run-through (123).

- Processes: connecting days 113 to 115, 118, 119 and 125; producing and presenting days 116, 117, 119 to 124; creating
  days 119, 121, 122; responding on the works days 113 and 114 and in the review on day 125.
- End-of-unit assessment, two check days: day 124, the scored screening (15 pair pieces; Pr4.1.7 on each student's
  own half, Pr6.1.7a tasks); day 125,
  self-check and two written items (Pr6.1.7b with growth since unit 4; Cn10.1.7b), with the showing plan and source log
  scored after the session. Respond: day 126.
- Candidate (a science or teaching film from Asia or Africa): dropped. Ray and Sembène carry those regions in year 7,
  and the screening unit has no free day.

### Year-end course-level check, year 7

Day 127 (year 7 school day 158, week 32), respond day 128.

## Year 8 (grade 8 ids; days 129 to 192, band school days 321 to 480)

### Unit 9. Media and the values we share

Days 129 to 142, weeks 1 to 7. Ids: MA:Re7.1.8a, MA:Re7.1.8b, MA:Cn11.1.8a, MA:Cn11.1.8b (ma-g8-read, ma-g8-society).

Parks (129), style by its conventions on the Parks portrait (130), the Earthrise contrast inside the style drill
(131) and Reel Injun (132) come before the written contrast (133). The legal setting (134), the case cards (135) and
the license drill with one case card analyzed for responsible use (136) come before the values piece is planned (137),
made (138, with the three-line values card at its end; 139 with the critique), revised and shown in a pair gallery
walk (140), so every later piece of the year answers to the license line.

- Processes: responding days 129 to 133 and 141; connecting days 132, 134 to 140; creating days 137 to 140; presenting
  day 140.
- End-of-unit assessment: day 141, two written items (Re7.1.8a; Re7.1.8b one technique and one style in each) on two
  unseen public domain pieces, with the values piece and its three-line values card (Cn11.1.8a, so civic,
  environmental and community values are all asked) and the media-ethics check with license lines and a line for each
  of the two case cards, the virtual world and the shared-image tool (Cn11.1.8b), scored after the session. Respond:
  day 142.
- Candidate (a civic or environmental piece by a living maker from Asia): dropped. Year 8 has Asia (Wan Laiming,
  Vyarawalla) and three living makers; a fourth work would take the license drill day.

### Unit 10. Workflow

Days 143 to 160, weeks 8 to 16. Ids: MA:Cr1.1.8, MA:Cr2.1.8, MA:Pr5.1.8a, MA:Pr5.1.8b, MA:Pr5.1.8c (ma-g8-ideas,
ma-g8-craft).

Schaeffer (143) shows a convention bent; thinking in many directions (144, 145) comes first; the found-sound layer
is shown and drilled (146, 147) before Pumzi's workflow (148) and the workflow chart (149, 150); bending a convention
and the range of role skills (151, 152) come before production (153 to 156), the critique on day 155 and the revision
on 156. The pieces are screened on day 157; portfolio and role record are finished on day 158.

- Processes: creating days 144, 145, 149, 150, 153 to 156; producing days 146 to 148, 151 to 158; responding on the
  works (review) days 143 and 148 and as audience on day 157; connecting practiced on day 148's setting card (a Kenyan
  team making science fiction on a small budget), no id claimed.
- End-of-unit assessment: production look-fors on days 154 to 156 (Pr5.1.8b and 8c), then day 159: self-check and the
  portfolio's last page (Cr1.1.8, Cr2.1.8), with the role record (Pr5.1.8a). Respond: day 160.
- Candidate (a Native American maker who bends a media convention): dropped. Neil Diamond (Cree) carries the year in
  unit 9, and the 18 days hold no free day.

### Mid-year course-level check, year 8

Day 161 (year 8 school day 83, week 17), respond day 162.

### Unit 11. Style and unity

Days 163 to 176, weeks 18 to 24. Ids: MA:Cr3.1.8a, MA:Cr3.1.8b, MA:Re8.1.8, MA:Re9.1.8 (ma-g8-make, ma-g8-judge).

Havoc in Heaven (163) opens the blend; the style sheet is shown and drilled (164, 165) before Song of the Sea (166)
and judging against goals and setting (167); the team style sheet, opened by a five-minute recall of the unit 10
workflow chart (168), and technical polish (169) come before
production (170), the critique (171) and the revision log (172, 173). The pieces are shown on day 174.

- Processes: responding days 163, 166, 167, 171 and 175; creating days 164, 165, 168 to 174; producing day 170;
  presenting day 174; connecting practiced on day 166's setting card (Irish folklore and early Irish art), no id
  claimed.
- End-of-unit assessment: day 175, two written items (Re8.1.8 intent and meaning in form and setting; Re9.1.8 built
  criteria weighed against a classmate's goals and the setting, on the piece and one production decision), with the
  style piece (Cr3.1.8a) and revision log (Cr3.1.8b) scored after the session. Respond: day 176.
- Candidate (a style-blending work from Africa or the Americas): dropped. Kahiu (Kenya) and Diamond and Parks carry
  those regions this year, and a third work would take the polish day.

### Unit 12. From here to the world

Days 177 to 190, weeks 25 to 31. Ids: MA:Pr4.1.8, MA:Pr6.1.8a, MA:Pr6.1.8b, MA:Cn10.1.8a, MA:Cn10.1.8b (ma-g8-present,
ma-g8-sources).

The Moon landing broadcast (177) and Vyarawalla's photographs (178) set local against worldwide; the source log
(179) and one theme across two formats (180, drilled 181) come before research (182) and making (183, in pairs, each
partner's half and one-line card scored for Pr4.1.8, as in unit 4); the showing plan
(184) comes before the second format with the critique (185), the trial showing with audience feedback (186) and the
counted revision session that puts an improvement in place (187), as Pr6.1.8b asks.

- Processes: connecting days 177 to 179, 182, 183 and 189; producing and presenting days 180, 181, 183 to 188; creating
  days 183, 185, 187; responding on the works days 177 and 178 and in the review on day 189.
- End-of-unit assessment, two check days: day 188, the year-end screening for families (15 pair pieces; Pr4.1.8 on
  each student's own half, Pr6.1.8a tasks);
  day 189, self-check and two written items (Pr6.1.8b the trial results, the improvement, growth and audience effect;
  Cn10.1.8b), with the showing plan and source log scored after the session. Respond: day 190.
- Candidate (a model work by a living maker from Africa or Asia on a local-to-worldwide event): kept on day 179 as the
  model work judged on the source log, no added day; the pick is a maker working after 2000, for range of period.

### Year-end course-level check, year 8

Day 191 (year 8 school day 158, week 32), respond day 192.

## Course-level checks

Each check is a written sitting of two tasks on day kind Check, `stretch` C: set-up 3 minutes, self-check 5, the two
tasks 25 (about 12 and 13 minutes), collecting and clean-up 5, 2 slack; each is followed by one respond day.

| Check | Day (school day, week) | Codes sampled | Why these |
|---|---|---|---|
| Year 6 mid-year | 33 (83, week 17); respond 34 | MA:Re7.1.6a, MA:Re7.1.6b (one technique and one style), MA:Cn11.1.6b | Right after unit 2's end-of-unit assessment, so it draws its items from unit 1; unit 2's portfolio and role record are carried unscored |
| Year 6 year-end | 63 (158, week 32); respond 64 | MA:Cr2.1.6, MA:Re8.1.6 | Right after unit 4's screening and written check, so it draws from units 2 and 3; unit 3's sequence and revision log are carried unscored |
| Year 7 mid-year | 97 (83, week 17); respond 98 | MA:Re7.1.7a, MA:Re7.1.7b (technique, style and taste), MA:Cn11.1.7b | Draws from unit 5; unit 6 carried unscored |
| Year 7 year-end | 127 (158, week 32); respond 128 | MA:Cr2.1.7, MA:Re8.1.7 | Draws from units 6 and 7; unit 8 assessed by its own two check days |
| Year 8 mid-year | 161 (83, week 17); respond 162 | MA:Re7.1.8a, MA:Re7.1.8b (techniques and styles), MA:Cn11.1.8b | Draws from unit 9; unit 10 carried unscored |
| Year 8 year-end | 191 (158, week 32); respond 192 | MA:Cr2.1.8, MA:Re8.1.8 | Draws from units 10 and 11; unit 12 assessed by its own two check days |

**Codes not sampled on a course-level check, and why** (rule 3). Each year samples 5 of its 18 ids. The other 13 a year
are, by grade g: MA:Cn11.1.ga (a made investigation, explainer or values piece), MA:Cr1.1.g and MA:Pr5.1.ga, gb, gc
(a method page, roles and production trials, observed over several sessions), MA:Cr3.1.ga and gb (a made sequence or
piece and its revision log), MA:Re9.1.g (criteria used on a classmate's piece and its production steps with a context
card; the frame cuts each check to two tasks, and the two the frame names take them), and MA:Pr4.1.g, MA:Pr6.1.ga, gb, MA:Cn10.1.ga, gb (the screening unit's ids,
assessed by its own screening and written check two to three days before the year-end check). Each is met only in a
made piece, an observed production or a screening, which a 40-minute written sitting of two tasks cannot hold, and the
frame cut each check to two tasks (second-model read C-68 finding 4). Sampling the screening ids again would collect the
same evidence twice inside ten days (rule 2, "Collect once"). Every one of them has its end-of-unit item. Naming them
with the reason is enough here, since the frame's check table limits the sample (lead call 3, 2026-11-26); any change
to that table is the structure pass's.

**No repeat of a task form.** Each check's two tasks are fresh (an unseen clip or piece, new sources, a new prompt or
case card). The mid-year checks fall about ten weeks after the unit 1, 5 or 9 written items, and the year-end checks'
forms (a fresh plan, an unseen interpretation) differ from the screening unit's written review and source item of the
two weeks before. A showing or screening is the discipline's own evidence: the screening on a check day may follow
a unit's trial or showing, since what may not repeat inside two weeks is the same item (the same prompt type on the
same work), and each check day's note says so (lead call 6).

**Collect once.** No check re-asks items a unit gave one to three days before: each mid-year check draws from the
unit that ended about five weeks earlier (unit 1, 5 or 9) and carries the just-assessed unit's records unscored; each
year-end check draws from units 2 and 3 (6 and 7, 10 and 11), whose items were given four or more weeks before, with
new prompts and unseen pieces, and carries the screening unit's record (lead call 7).

**The calendar and the stagger rule.** The mid-year checks sit on school day 83 of each year (week 17) and the year-end
checks on school day 158 (week 32, the finals week), the frame's days. In grades 6, 7 and 8 no core subject holds a
check on school day 83 (CALENDAR.md target weeks: grade 6 math 16, science 18, social studies 15, ELA 12; grade 7 ELA 12,
math 9, social studies 13, science 14; grade 8 math 14, science 15, ELA 18, social studies 10). The other arts electives
on day 83 count as one course with this one (CALENDAR.md rule 3), and health and physical education sit on other school
days. `python -X utf8 scripts/frame.py calendar` reports no break of the stagger rule for this course.

## Shorter path

**A shorter period.** The 40-minute session is already the short arts session (STANDARD.md 3.4). Where a period runs
shorter, the opener drill drops first, then the clean-up runs to 5 minutes on every day; check days keep their 25
minutes of written items.

**The once-a-week path (32 sessions a year).** Every unit and every id is kept by merging the days named below; a
merged day never drops a critique, a revision, a check or a respond session, and fluency days fold into openers. Each
year: units of 7, 9, 6 and 6 sessions, each check 1 session and its respond 1. The mid-year check session falls in week
17 and its respond in week 18; the year-end check session in week 31 and its respond in week 32. Days are given for
year 6; years 7 and 8 merge the same positions (add 64 or 128). Each unit's baseline look runs in the session that
holds its folded fluency opener, so the path keeps two marks a unit.

| Unit (sessions) | Sessions, by the days merged |
|---|---|
| 1, 5, 9 (7) | 1: days 1 to 3 (the work opens the step card demonstration, retrieval in the opener); 2: days 4, 5 and 7 (the two works merged with the ethics or rules or license card); 3: days 6 and 8 (the written practice and the plan); 4: days 9 to 11 (making with the critique, the drill in the opener); 5: day 12 (revision and showing); 6: day 13 (check); 7: day 14 (respond) |
| 2, 6, 10 (9) | 1: days 15 to 17 (hook, method, aims); 2: days 18 to 20 (the step card demonstration opened by the second work, drill in the opener); 3: days 21 and 22 (portfolio, storyboard and mockup); 4: days 23 to 25 (roles, constraint, production 1); 5: days 26 and 27 (production with the critique); 6: day 28 (revision); 7: days 29 and 30 (screening, records finished); 8: day 31 (check); 9: day 32 (respond). The production look-fors run over sessions 4 to 6, ten students each |
| 3, 7, 11 (6) | 1: days 35 to 38 (both works open the step card demonstration, drill in the opener); 2: days 39 to 42 (approaches or shot list or style sheet, criteria, first making); 3: day 43 (making with the critique); 4: days 44 to 46 (revision log, refinement, showing); 5: day 47 (check); 6: day 48 (respond) |
| 4, 8, 12 (6) | 1: days 49 to 53 (study the works, the source log, the technique demonstrated, drill in the opener); 2: days 54, 55 and 57 (research from a teacher-prepared archive packet, the pair piece made, the trial in pairs with the critique and the review frame); 3: days 56, 58 and 59 (the showing formats on the showing plan, the revision that puts the review's improvement in place, the run-through and records finished; in unit 12, session 2 holds days 182, 183 and 185, the research, the screen version and the second format with the critique, and session 3 days 184, 186 and 187, the showing plan, the trial with audience feedback and the counted revision); 4: day 60 (the scored screening); 5: day 61 (written items and self-check); 6: day 62 (respond). This moves the research and the draft out of session 1; the frame's six sessions stay, see For the lead item 7 |

**A year about 10 days short.** Ten school days is about four sessions at two a week (lead call 1). Four fold-in days a
year, each a fluency day whose drill moves into the next day's opener (and, where it holds the baseline look, the look
moves to the named day, a day where the look-for can be seen); nothing is assessed on them and no owned part lives
only on them. Each saves 40 minutes, 160 minutes a year, leaving 60 of the
frame's 64 days (180 of 192 over the band).

| Year | Fold-in days (the day that takes the drill) |
|---|---|
| 6 | 9 (10), 24 (25), 41 (42), 53 (54; baseline look on 55, the making day) |
| 7 | 67 (68; baseline look on 69), 72 (73, which also takes the class-rules lines), 88 (89), 117 (118; baseline look on 119) |
| 8 | 136 (137, which also takes the case-card analysis), 152 (153), 165 (166; baseline look on 170), 181 (182; baseline look on 183) |

Day 131 is no longer a fold-in day: it now holds the Earthrise contrast, a work study.

Day 41 also holds unit 3's Candidate look; on the short year it moves with the drill to day 42.

## For the lead

1. **Course-level checks sample 5 of each year's 18 ids.** Settled by lead call 3 (2026-11-26): naming the 13 a year
   with the reason is enough where the frame's check table limits the sample.
2. **school_day across the band.** Settled by lead call 5 (2026-11-26): the column counts band school days 1 to 480,
   as frame.py reads it; the lead documents it in CALENDAR.md.
3. **Year 7 living makers.** Of the frame's named year 7 works only Hopinka is a living maker; unit 7's Candidate is
   kept to add a second. The frame's Base text bullet ("Each year's works include living makers") stays true only with
   that pick; the unit plan should confirm it.
4. **Production look-fors marked `assess` = end.** Days 26 to 28, 90 to 92 and 154 to 156 carry `end` because the
   Pr5 b and c evidence is collected there; each unit's check day also carries `end`. If the lead prefers one end day
   per unit with the look-fors named in its note, only the assess cells change.
5. **Once-a-week year-end check in week 31.** On that path the year-end check session sits in week 31 and the respond
   in week 32 (the frame's choice); on the full path the check is in week 32. Both stay off the core check weeks.

6. **Works by period and form** (expert read finding 6). Three of 27 works are from after 2010 and none is
   interactive. The unit 7 and unit 12 Candidate picks are now makers working after 2000; when the unit plans confirm
   works, one of unit 8's two science works (Smith 1910 or Edgerton 1957) may be swapped for a contemporary
   science-visualization or interactive explainer, described and linked. No day changes; the swap is a frame works
   change.
7. **Once-a-week screening units** (expert read finding 5). The read asked for units of 7, 8, 6 and 7 sessions. With the
   mid-year check held in week 17 and the year-end check in week 31, units 3 and 4 have 12 sessions between them, so a
   seventh unit 4 session would move the mid-year check to week 16, grade 6 mathematics's check week. The fix pass
   kept six sessions and moved the research and the draft out of session 1 (Shorter path table); session 1 still
   holds both works and the technique. A seventh session needs a calendar call.

The exact week of each work's excerpt flash check is the unit plan's.
