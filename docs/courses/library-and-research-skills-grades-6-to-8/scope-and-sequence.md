# Scope and sequence: Library and Research Skills, grades 6 to 8

Course `library-and-research-skills-grades-6-to-8`, grades 6, 7 and 8 (one course across three school years), draft,
2026-11-26, fixed after the expert read the same day (docs/reviews/sequence-library-and-research-skills-grades-6-to-8-fixes-2026-11-26.md). The days are in data/plans/library-and-research-skills-grades-6-to-8/days.csv; this page holds the
judgment behind them. Built from the frame (docs/courses/library-and-research-skills-grades-6-to-8/frame.md) with no
unit, owned row or day count changed.

## How the band is laid out

- **Years.** Grade 6 is course days 1 to 18 (units 1 to 3, checks 1 and 2), grade 7 days 19 to 36 (units 4 to 6,
  checks 3 and 4), grade 8 days 37 to 54 (units 7 to 9, checks 5 and 6). Each grade's AASL ids are the ones its own
  progression rows own (frame, Standard bullet): grade 6 I.D.1, VI.A.3, II.A.2, IV.C.1, III.A.2, III.B.1, V.B.2;
  grade 7 II.B.2, II.C.1, IV.C.2, III.C.1, V.D.3, V.C.3; grade 8 V.A.2, IV.B.2, IV.C.3, VI.B.1, II.B.1, III.B.2.
  Carried ids are written `~` in the codes column.
- **Meeting days and school_day.** One session of about 45 minutes (about 40 working minutes) every two weeks, 18 a
  year over 32 weeks. `school_day` counts across the band (grade 6 is school days 1 to 160, grade 7 161 to 320,
  grade 8 321 to 480). The one formula: year day k (1 to 18) of year y (0, 1, 2) sits on school day
  `160y + ceil(160k / 18)`, which is frame.py's even spread, so week = ((school_day - 1) mod 160) // 5 + 1 gives the
  frame's weeks 2, 4, 6, 8, 9, 11, 13, 15, 16, 18, 20, 22, 24, 25, 27, 29, 31 and 32.
- **Day kinds.** Most sessions are mixed (a show-me of one move, then practice of the move shown the session before).
  Each day carries its main kind by GLOSSARY: a day that shows anything new is Understanding even where its second
  half is practice, so no day is typed Fluency; practice lives in the second half of show-me days and the five-minute
  opening retrievals. Inquiry days, which draft and revise, are Application. End sittings are Check.
- **Evidence.** Exit tickets on show-me days, the research log on inquiry days, a self-check once a unit, a sitting of
  30 to 35 minutes for units 1, 4 and 7, and the course-level checks as the end-of-unit assessment for units 2, 3, 5,
  6, 8 and 9 (each check sits on the course day right after its unit's last day). Products in units 3, 6 and 9 are
  scored after their draft, written feedback and revision days.
- **Unloaded sources.** The CC BY online-reasoning lessons are not yet in the source store (later.csv L149). Days 6,
  8, 20, 47 and 48 lean on their lesson kinds, and the item forms of days 11, 22 and 53 may follow their parallel
  assessments; each says so in its note and is planned from the frame meanwhile. No source-map.csv is written this run.
  The web-literacy book is not used in this band (grades 9 to 12 and teacher background). The continuum's 6 to 8 band
  file was read for the frame; no day here leans on the 3 to 5 band file.
- **The skill card and the strip.** Every inquiry day withdraws the card for the moves already practiced; the line for
  the move shown last session stays on a one-line strip for that session, so a new move gets one session with its
  card. The response log, shown in day 32's first ten minutes, keeps its strip through day 33's first half. Sittings
  and checks run without the card or the strip.
- **Teacher written feedback** (days 15, 33 and 51) is written between sessions on the draft and handed back at the
  start of the session, since a session falls only every two weeks.
- **Paper path.** Every day runs on printed pages and the research log notebook; devices are optional, pairs share
  one where a school has them, under the stop rule and the privacy rule.

## Grade 6 (course days 1 to 18)

### Unit 1. Plan it, note it, ask again (days 1 to 5, weeks 2 to 9)

Arc: the search plan shown on day 1 with the question chain, note cards shown on day 2 while the search plan is
practiced, the cycle run on the host question on day 3 (card withdrawn), findings shared and question chains written on
day 4 with the self-check, then the sitting. The search plan comes first because day 2's practice and day 3's inquiry
use it; note cards come before the inquiry that fills them; the question chain closes the cycle, so its practice sits
on the share day.

- Readiness (day 1, last ten minutes, after the hook): g5-research-or-guess, g5-search-log-look-back, g5-search-revise,
  g5-bibliography, each last used in library grade 5. By the grade count these are retrieval rows; the frame gives
  them as readiness checks because a school may not run library grade 5 (frame For the lead item 4, kept). The
  ten-minute reteach is day 2's opening.
- End-of-unit assessment: day 5, a 30-minute sitting on all three rows (I.D.1 plus the carried search and citation
  ids), then unit 2's readiness check. Response: the opening five minutes of day 7 and the mid-year respond day.
- Host: ss6-mena-settlement, social studies grade 6 unit 3 (weeks 6 to 8): days 3 and 4 fall in weeks 6 and 8, in step.
  Stand-alone: food kept from spoiling before refrigerators. ELA's e6-short-research comes later (weeks 13 to 18): unit
  1 teaches the plan, the cards and the chain itself.
- Candidates: key words from background reading (kept, about 3 minutes on day 1); several note forms (kept, a choice of
  two card layouts on day 2); topics of passion (kept, the follow-up picked on day 4). No day added.

### Unit 2. Leave the page (days 6 to 10, weeks 11 to 18)

Arc: lateral reading shown on day 6 on a polished wrong page and a plain right one; point of view shown on day 7 while
three claims are checked laterally; the group-written article's references and history on day 8 while point-of-view
lines are practiced; the host sources judged on day 9 (card withdrawn); lists shared and the two best sources agreed
on day 10. Lateral reading first because the point-of-view and article days both judge by looking behind a source.

- Readiness: day 5's last ten minutes (g5-first-lateral-check, g5-evidence-notes, g5-choose-sources); reteach in the
  last ten minutes of day 6, after the hook and show-me.
- End-of-unit assessment: the mid-year check, day 11 (VI.A.3, II.A.2, IV.C.1 each with its own prompt; the lateral item
  asks VI.A.3 whole in three prompts: what was found upstream, so is it accurate; is it fair in its context; is it fit
  for this task).
- Leans: ELA grade 6 unit 3 (credibility, weeks 13 to 18) meets days 8 to 10 (weeks 15 to 18), the same weeks, either
  order; ELA grade 6 unit 2 (author purpose, weeks 7 to 12) came before, and day 7 still teaches the move.
- Candidates: authority, accuracy and point of view of every source (kept, the three judgment lines on day 9); inaccurate
  or misleading information at the upstream step (kept, one cut-quote claim on day 7).

### Unit 3. Build it together (days 13 to 16, weeks 24 to 29)

Arc: the sharing plan, team sheet and version log shown on day 13; version 1 made on day 14 with the plan in use (card
withdrawn); version 1 tried on a reader, teacher feedback, version 2 begun on day 15; revision finished and shared with a
younger class on day 16. Draft, feedback and revision sit in the unit's days, before any score.

- Readiness: the mid-year respond day, day 12, last ten minutes (g5-group-inquiry, g5-share-real-audience); reteach at
  the end of day 13.
- Retrieval: day 14 opens with s5-design-test (science grade 5, the year before), without criteria or fair tests.
- End-of-unit assessment: the year-end check, day 17: the sharing plan (III.B.1) and version log (V.B.2) scored from
  the revised work, and the written item on the team's new idea (III.A.2).
- Host: s6-hazard-forecast, science grade 6 unit 5 (weeks 24 to 27): days 14 and 15 in step; natural hazards flag on
  every day of the unit.
- Candidates: building on others' ideas and encouraging members to share (kept, the "built on" column, about 2
  minutes on day 13); presenting conclusions in several ways (kept, the product menu, day 13); drafting for the
  audience (kept, version 1 names its reader, day 14).

## Grade 7 (course days 19 to 36)

### Unit 4. Search smarter, check the hard cases (days 19 to 22, weeks 2 to 8)

Arc: filters, a reference work, a site's menu and search box, a subject heading and the choice rule shown on day 19;
the hard cases shown on day 20 while filtered searches (one by menu, one by subject heading) are practiced; the host
or stand-alone inquiry on day 21 with one route each and one hard case, shared and self-checked in its last ten
minutes; the sitting on day 22. The navigation additions from the frame fix pass sit in all four days.

- Retrieval (day 20): g6-lateral-reading and g6-search-strategy (grade 6, the year before). No readiness check.
- End-of-unit assessment: day 22, about 35 minutes, both rows with a prompt per part. Response: day 24's opening five
  minutes and the mid-year respond day.
- Host: ELA grade 7 unit 2 (the Dust Bowl, weeks 7 to 12) opens after day 21 (week 6), so the stand-alone T-shirt
  water question carries the inquiry unless a school runs ELA's unit earlier (For the lead, item 1).
- Candidates: fact-checking on websites and social media (kept, the share-or-not line); visual literacy at the photo
  case (kept, about 3 minutes on day 20); encyclopedias and directories for background (kept, day 19's reference step).

### Unit 5. When sources disagree (days 23 to 27, weeks 9 to 16)

Arc: the comparison table on day 23; the citation style on day 24 while the table is practiced; the sourced discussion
fishbowl on day 25, rotated so every student makes one sourced claim and one source challenge, while citations are
practiced; the host table from three or more cited sources on day 26 (card
withdrawn); the scored discussion in groups of five on day 27 with the self-check (two marks per student on the record sheet, the
teacher sitting with each group for about five minutes in turn, and a turn slip naming the source behind each
student's claim, so a student not heard live is marked from the slip by the teacher). The table comes first because the
discussion argues from it, and citations come before the cited table.

- Retrieval: day 24 (g6-point-of-view), day 25 (g6-keep-questioning, g6-quote-paraphrase), all grade 6.
- End-of-unit assessment: the mid-year check, day 28 (II.B.2 and the citation items sat; II.C.1 from day 27's record
  sheet, after its unscored, rotating fishbowl practice on day 25).
- Leans: ELA grade 7 unit 3 (citation format, smallpox host, weeks 13 to 18) meets days 25 to 27; day 24 (week 11) is
  before it, so the show-me teaches the format from the model and ELA's day retrieves it. ELA grade 7 unit 4 (author
  position, weeks 18 to 22) is later; the unit teaches the table itself. ELA grade 7 unit 1 (discussion) came before.
- Candidates: supporting and refuting evidence combined into a conclusion (kept, the table's last line, day 26); hearing
  others' opinions with an open mind (kept, the say-back turn, days 25 and 27).

### Unit 6. Our class page (days 30 to 34, weeks 22 to 29)

Arc: ideas before judging, each tied to a finding, on day 30; the class page (section, sources, credit, history) on day
31; the response log shown in ten minutes on day 32, then sections and solution lists drafted and comments asked
(card withdrawn for the moves already practiced, the log line kept on a strip through day 33's first half;
Understanding because the log is first taught there); every comment answered and the page revised
after teacher feedback on day 33; the page and ideas shared with the school office on day 34.

- Retrieval: day 31 (g7-citation-style, unit 5 this year), day 32 (g6-group-wiki, g6-team-product,
  g6-make-and-improve from a short packet of grade 6 work). No readiness check.
- End-of-unit assessment: the year-end check, day 35: the revised section (IV.C.2), the response log (III.C.1,
  V.D.3), the solution list with each student's part (V.C.3) and a written item on an idea and its finding.
- Host: science grade 7 unit 6 (weeks 26 to 32) is in step only for days 33 and 34; the cafeteria question carries days
  30 to 32. Food and meals flag on every day.
- Candidates: curating and sharing good sources (kept, the "best two sources" box, day 31); criteria for judging the
  product (kept, two class criteria, about 3 minutes on day 32); sharing research to raise awareness (kept, the note to
  the office, day 34).

## Grade 8 (course days 37 to 54)

### Unit 7. Test what you expect (days 37 to 40, weeks 2 to 8)

Arc: the written expectation, marked findings and honest update on day 37; the search plan for views on day 38 while
marking is practiced; the inquiry on day 39 (expectation, three views collected in the log, update; card withdrawn;
shared and self-checked in the last ten minutes); the scored log and sitting on day 40.

- Retrieval: day 38 (g7-sources-disagree, g7-search-results), day 39 (g7-evidence-discussion), all grade 7.
- End-of-unit assessment: day 40: the day 39 log scored for a source and a finding from each of three views (IV.B.2),
  then a 35-minute sitting (the views plan as transfer; V.A.2's marked findings, update and one line on how what I
  expected shaped what I looked for, the line day 37 teaches and day 39's log also asks).
- Host: ELA grade 8 unit 2 (weeks 7 to 13) opens after day 39 (week 6), so the stand-alone school start question
  carries the inquiry (For the lead, item 1); science grade 8 unit 5 (weeks 21 to 27) is later.
- Candidates: questioning prior knowledge (kept, day 37); predicting the views likely to be found (kept, about 2
  minutes on day 38); changing one's opinion when reasons have merit (kept, the update, day 39).

### Unit 8. Compare and use fairly (days 41 to 44, weeks 9 to 15)

Arc: entries compared and differences traced on day 41; the four fair use questions and the safer path on day 42 while
comparing is practiced; pairs chart three entries (lines initialed) and make a page with an image chosen by the safer
path on day 43 (card withdrawn); pages finished and shared on day 44.

- Retrieval: day 42 (g7-citation-style, g7-class-wiki), after unit 7's five-minute respond step.
- End-of-unit assessment: the mid-year check, day 45 (IV.C.3 by the unseen comparison and the scored pair chart,
  VI.B.1 by a new case).
- Host: ELA grade 8 unit 3 (the 1906 research, weeks 13 to 18) is in step for days 43 and 44. Rights read on days 42
  to 45.
- Candidates: ethical choices in using and remixing images within fair use (kept, the safer path, day 42); citing what
  is specific rather than common knowledge (kept, a three-minute sort on day 42); copyright in safe use of technology
  (dropped: met by the stop and privacy rules on every device day, and digital footprint is computer science's).

### Unit 9. Read the news, research as a team (days 47 to 52, weeks 20 to 29)

Arc: report and opinion, the outlet check and tracing a claim on day 47, with first answers written and teams formed
from them; the question sort by kind shown on day 48 (Understanding: the frame calls it practice, but the sort is new
here) while four news items are checked and the exchange planned; research and findings sent to the partner class on
day 49 (card withdrawn); the other class's findings built on and the product drafted on day 50; comments answered and
the product revised after teacher feedback on day 51; the product shared with its real audience and the change lines
written on day 52.

- Retrieval: day 48 (g7-lateral-hard-cases; g8-multiple-views-gather, unit 7 this year), day 49 (g7-group-solutions,
  g7-feedback-loop).
- End-of-unit assessment: the year-end check, day 53 (the revised product and log, the news written part, the two
  change lines for II.B.1 and III.B.2; the views sample asks a views plan and one finding per view from a given short
  set, so IV.B.2's gathering is sat, not only planned).
- Leans: social studies' news unit (ss8-news-literacy, civics unit 9, weeks 27 to 29) is later than day 47 (week 20)
  and teaches its own news check: this unit teaches the method itself, a class that has both meets it twice, and days
  51 and 52 share its weeks. ELA grade 8 unit 5
  (weeks 26 to 32) may host the product from day 51. ELA grade 8 unit 1 (discussion) came before; day 47's team talk rules start from SEL's grades 6 to 8
  talk turn card, so students meet one set of words.
- Candidates: checking methods by kind of source (kept, the four-item set, day 48); bias and persuasion (kept, a
  two-minute line on day 47; propaganda as a term left to social studies); a project with others for a real audience
  (kept, the product); revising with self, teacher and peer feedback (kept, a self-review line, about 3 minutes, day 51).

## Course-level checks

| Check | Course day | Week (of its grade) | Respond day, week | Samples |
|---|---|---|---|---|
| 1, mid-year, grade 6 | 11 | 20 | 12, week 22 (plus unit 3 readiness) | Unit 2 in full; unit 1 on a new case |
| 2, year-end, grade 6 | 17 | 31 | 18, week 32 (year's reflect) | Unit 3 in full; units 1 and 2 on new cases |
| 3, mid-year, grade 7 | 28 | 18 | 29, week 20 | Unit 5 in full; unit 4 |
| 4, year-end, grade 7 | 35 | 31 | 36, week 32 | Unit 6 in full; units 4 and 5 |
| 5, mid-year, grade 8 | 45 | 16 | 46, week 18 | Unit 8 in full; unit 7 |
| 6, year-end, grade 8 | 53 | 31 | 54, week 32 (band reflect) | Unit 9 in full; units 7 and 8 |

Every check is the end-of-unit assessment of the unit just before it, so its own unit's items are new cases, not a
repeat; the earlier units it samples are sat on new cases 8 to 23 weeks after their sittings (8 to 11
weeks at the mid-year checks, about 22 to 23 at the year-end checks), so no task form repeats
inside two weeks. Every owned code is sampled on at least one check day: II.C.1 through day 27's record sheet, counted
at check 3. The checks sit on the frame's weeks and on the target weeks the end table of CALENDAR.md gives (20 and 31,
18 and 31, 16 and 31), off every core check week. By school day (rule 3, mid-year checks), day 11 is school day 98
(grade 6), day 28 is 89 (grade 7) and day 45 is 80 (grade 8): no other subject's grade 6, 7 or 8 mid-year check
falls on those days in calendar.csv (the nearest are grade 8 career exploration on 77 and SEL on 78). Year-end checks
sit in week 31, outside the finals week; the grade 6 and 7 computer science year-end checks also sit in week 31
(school days 155 to 158), on other days than library's 152.

## Shorter path

- **A shorter period** (35 working minutes):
  - Day 5 drops its one-answer items (about 5 minutes); the rubric parts and the readiness check stay.
  - Days 28 and 45 cut their earlier-unit sample to one item (about 5 minutes).
  - Show-me days give one fewer practice try in their practice half (about 5 minutes); the hook or retrieval, the
    think-aloud and the exit ticket stay.
  - On inquiry days the self-check moves to the next session's opening slot. Nothing assessed or owned is cut.
- **A year about 10 days short** (10 school days is about one session at this dose): one or two named fold-ins a
  year, nothing assessed and no owned part cut.
  - Grade 6: day 10 (shared source lists and the class's two best sources) folds into day 9's last ten minutes and the
    opening of day 12 (saves about 30 minutes); day 4 (share and question chain) folds into day 3's last 15 minutes,
    with the chain written as day 3's exit work (saves about 25 minutes).
  - Grade 7: day 34 (sharing with the office) folds into day 33's last ten minutes, the page posted rather than
    presented (saves about 30 minutes). Optional trim, not a fold: day 21's self-check and group share move to day
    22's opening (about 10 minutes; the day stays).
  - Grade 8: day 44 (pages finished and shared) folds into day 43's last ten minutes and day 46's opening (saves about
    30 minutes). Day 52 is not folded: it is where each student writes the two change lines day 53 scores.
  - Total: four sessions folded across the band (two in grade 6, one each in grades 7 and 8), about 115 minutes, so
    54 days run in 50 without losing an assessed item or an owned part. One fold a year covers a year 10 school days
    short at this dose.
- **A left-out unit** (STANDARD.md section 4): the course page and family note name its owned ids as not claimed that
  year. Leave-out bridge: where a later unit uses the left-out unit's card, it teaches the card's one-step form in its
  first ten minutes and claims none of the left-out unit's ids.
  - Unit 1 left out: day 20 opens with the search plan's one-step form, and day 25 with the quote-or-paraphrase card.
  - Unit 2 left out: unit 4 day 19 teaches "leave the page, see who is behind it".
  - Unit 3 left out: day 32 teaches "mark who added what, log each change".
  - Unit 4 left out: day 38 teaches "filter, pick three", and day 48 "check the photo, the number, the maker".
  - Unit 5 left out: day 31 and unit 8 day 41 teach the works-cited model, and day 38 "table the claims".
  - Unit 6 left out: unit 9 day 47 teaches the response log line.
  - Unit 7 left out: unit 9 day 48 teaches the views plan.
  - Unit 8 left out: day 52's product uses only invented or public domain images, and day 53 drops its fair use item.
  - Checks: a check that is a left-out unit's end-of-unit assessment keeps only its earlier-unit samples, and any check
    drops the items that sample a left-out unit. In both cases the family note names the ids not claimed.

## For the lead

1. **Grade 6 readiness on grade 5 rows** (frame item 4, kept): by the grade count these are retrieval rows; the days
   give them as readiness checks as the frame decided. sequence.py prints no rule 2 note for library (its count does
   not run on this subject), so the choice is recorded here.

Settled in the fix pass and dropped from this list: the unit 4 and 7 host lines (the frame now says the stand-alone
question carries the inquiry), the "standard None" gate note (it comes from the frame's "None" cell; left as it is)
and the source map (no source-map.csv; it waits on later.csv L149).
