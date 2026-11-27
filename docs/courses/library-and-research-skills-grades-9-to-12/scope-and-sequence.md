# Scope and sequence: Library and Research Skills, grades 9 to 12

Course `library-and-research-skills-grades-9-to-12`, grades 9 to 12 (one band course), draft 2026-11-26, fixed after the expert read the same day. The days are
in data/plans/library-and-research-skills-grades-9-to-12/days.csv; this page holds the judgment.

## How the band sits

- **72 course days, 18 a year for four years**, one session of about 45 minutes (about 39 working minutes) about every
  two weeks, taken from a host class period (most often ELA or history). Each year: two units (14 unit days), a
  mid-year check and its respond day, a year-end check and its respond day. Units: 7 and 7 (grade 9), 7 and 7
  (grade 10), 5 and 9 (grade 11), 6 and 8 (grade 12), as the frame sets them. No unit is over 25 days, so no
  mid-unit assessment. Base text: none; every day is Curio Class's own, on paper, with no device, account, paid
  database or library access needed. No source-map.csv.
- **Which year holds what.** Grade 9 is days 1 to 18 (units 1 and 2, checks 1 and 2); grade 10 days 19 to 36 (units 3
  and 4, checks 3 and 4); grade 11 days 37 to 54 (units 5 and 6, checks 5 and 6); grade 12 days 55 to 72 (units 7 and
  8, checks 7 and 8). AASL ids are owned in the year whose row first checks them alone: grade 9 I.D.2, IV.D.1, II.B.3,
  III.A.3, VI.C.1; grade 10 II.A.3, III.C.2, II.C.2, IV.D.2, VI.B.3; grade 11 IV.D.3, II.D.1, VI.C.2, VI.D.2; grade 12
  VI.D.1, VI.D.3, I.D.3, II.D.3. A `~` code in days.csv is an id owned in an earlier grade and revisited. Grades 9 and
  10 are checked against the continuum's 9-10 cells, 11 and 12 against its 11-12 cells.
- **school_day.** For course day d, year y = (d - 1) // 18 (0 for grade 9 to 3 for grade 12) and n = d - 18y (1 to
  18). The school day within the year is 9n for n = 1 to 8, 9n - 1 for n = 9 to 17, and 160 for n = 18; days.csv
  stores 160y plus that, so week = ((school_day - 1) mod 160) // 5 + 1. This is the frame's "about school day 9n",
  with the second half pulled back one day so the respond days land in weeks 16 and 32. Every unit, check and respond
  day lands in the weeks the frame and CALENDAR.md give (table below).
- **Calendar.** 9 to 12 has only the finals-week rule (CALENDAR.md rule 4): no library check is in week 32. No check
  day falls in a core check week of its grade; the respond days in weeks 16 (grade 9), 13 (grade 11) and 15 (grade 12)
  share a week with a core check, which rule 4 allows. Clashes with the other after-core 9 to 12 courses are the
  lead's one calendar pass (frame For the lead item 4).
- **Kinds** in library's words: Understanding is the show-me day, Fluency the practice day, Application the inquiry
  day (drafting and revising a product are inquiry days), Check the assessment day, Respond the respond day. Every
  unit's day 1 is a show-me day with the hook and the compelling question. Fluency is small: one practice day a unit
  (unit 4 has two, both short tries of a move the day before showed). Nothing is first taught on a practice day:
  where the frame lists a move only under practice, it is modeled the show-me day before (unit 1's source log entry
  on day 2; unit 3's missing view in a reference list on day 20; unit 5's primary-and-news contrast and sponsored
  placement on day 37).
- **The skill card** is held by the teacher on the first show-me day, by pairs on the practice day, and withdrawn on
  the first inquiry day (days 5, 13, 23, 32, 40, 47, 58, 64); every check is taken without it.
- **Daily evidence:** an exit ticket doing the move once on a new case on show-me and practice days; the research
  notebook's working notes on inquiry days; one self-check per unit after the share (days 7, 16, 25, 34, 41, 52, 60,
  69).
- **Readiness and retrieval (rule 2).**

  | Assumed row | Last used | Treatment |
  |---|---|---|
  | g8-test-assumptions; g8-research-product | Library 6 to 8, grade 8 (optional course) | Retrieval day 2 |
  | g8-multiple-views-gather | Grade 8 | Retrieval days 2 and 10 (day 10 for unit 2's use, views for a decision) |
  | g8-news-lateral | Grade 8 | Retrieval day 3 |
  | g8-compare-wikis | Grade 8 | Retrieval day 4 |
  | g8-fair-use-basics | Grade 8 | Retrieval day 11 |
  | g8-diverse-team | Grade 8 | Retrieval day 13 |
  | g7-citation-style (the set citation style g10-label-own-work uses) | Library grade 8 (6 to 8 days 42 and 53, an optional course), two grades back; ELA grade 9 unit 4 taught the works-cited format (e9-w-short-research) | Readiness, last ten minutes of day 27 (check 3's respond day): one source cited in the set style; a miss gets a ten-minute reteach on day 28 or 29 |
| g9 rows (unit 3 and 4 assumptions) | Grade 9 | Retrieval: days 19 (g9-fair-sides), 20, 22, 28, 30, 33 |
  | g10 rows (unit 5 and 6 assumptions) | Grade 10 | Retrieval: days 37, 39, 44, 45, 49, 51 |
  | g11 rows (unit 7 and 8 assumptions) | Grade 11 | Retrieval: days 55, 57, 63, 66 |

  The grade 8 rows are one year back, so each is a five-minute retrieval on a day that builds on it, never a unit's
  first day (group read 2026-11-26; lead call "Readiness on a band year's first day": a row last used the year before
  is a retrieval, never a readiness check). Library 6 to 8 is optional and students reach grade 9 from many middle
  schools, so each retrieval day carries the line "a class that did not take library 6 to 8 gets the ten-minute
  reteach from the 6 to 8 show-me case for every student", as the K to 5 courses do; day 2 is where the teacher reads
  last year's class-level note, where there is one, to plan the reteach. Days 1 and 9 keep their exit ticket and
  respond time. Grades 10 to 12 have one readiness check, day 27's citation style (above, last used in library grade 8,
  two grades back, in an optional course); every other row they assume was taught inside this band the year before.
  Rows used earlier the same year also come back in the
  `retrieves` column (the lateral routine on days 10, 15 and 23, the log on days 12, 21, 25 and 40, the database
  move on day 29, the synthesis map on day 38, the advanced search on day 46, the fast-news check on day 56, the
  system on day 64).
- **Lateral reading time** (frame bullet; the course's one time figure). Grades 9 and 10 hold nine sessions whose main
  move is lateral reading, in working minutes: day 3 (39), day 4 (34), day 5 (34), day 6 (34), day 7 (29), day 23
  (29), day 30 (39), day 31 (34), day 32 (34), about 306 in all, at least the six 50-minute lessons of the one high
  school field study and no claim beyond it. Each figure is in that day's note. A day plan that cuts one below its
  figure moves the other work, not the lateral time, and the unit plan shows each of these sessions' split
  with the lateral move as the main activity and the other work named in minutes (days 5, 6, 23 and 32 also
  search, log or draft). The study is background, not evidence that this course or its
  paper path gets its result; no page claims the method raises scores. Grades 11 and 12 return to lateral work in
  units 5 and 8, not counted here.
- **Sources not loaded (later.csv L149).** The online-reasoning lessons and the web-literacy book (STANDARD.md section
  3's partial bases) are approved for download but not in the source store. The days that would adapt them, the
  lateral days of unit 1 (3 to 7) and unit 4 (30 to 32), and unit 5's sponsored results, slant and news days (37, 39,
  40), are placed from the frame alone, and their notes say so. The continuum's 9 to 12 band file is in the store and
  was read for the frame; the Candidate cells below come from that read. The US Copyright Office fair use index is
  named for the `rights` read on days 11, 12, 14, 33 and 49; it was not opened.
- **Sensitivity.** Every unit gets the fresh sensitivity read on its case set at the unit plan; the license, fair use
  and honesty days (11, 12, 14, 33, 49, 51) also get the `rights` read. Every open-search inquiry day (5, 6, 13, 23,
  32, 41, 64) carries the stop rule in its note; day 56, a practice day, runs on the closed invented set only. Interview days (23, 45, 47) carry APPROACH.md Sensitive ground
  item 8. Library's own case sets touch no cultural, Native, hard-history, health or disability content; a host task's
  own frame notes apply where a unit runs on it (day 47 names ELA grade 11 unit 8's).
- **Supplies and safe use of space.** Paper only: printed invented source sets, results pages, "other tabs" sheets,
  dated captures, the research notebook and license labels, about $8 to $12 a unit at about 5 cents a page (frame).
  At most a shared device for a pair on an open-search day. No field work or trip; interviews outside school are
  arranged through the school or a family in a public or supervised setting.

## Grade 9 (days 1 to 18)

### Unit 1. Staying with a question (days 1 to 7, grade 9 weeks 2 to 13)

*What makes a research question worth weeks of searching, and which sources earn a place in the log?* Owned:
AASL.I.D.2, AASL.IV.D.1. Rows: g9-research-question-design, g9-databases-operators, g9-lateral-method, g9-source-log.

Arc: three show-me days, one per move (the question, the database and plan, the lateral routine), then a practice day
of three lateral checks with the card, then three inquiry days that run rounds 2 and 3 on the student's own question
and end with the findings note and self-check. The student's first try at the question is day 2's exit ticket (their
own question on the teacher-set topic, narrowed, with one operator string), returned with a line before day 4; round
1 is day 4's last five minutes (the string fixed and the log started from that question). The question comes first because every later move serves it; the
database before the lateral routine because the routine judges what the search found; the log starts on day 4 so the
inquiry days have somewhere to put judged sources. Days 3 to 7 are the unit's lateral sessions (170 working minutes),
placed in weeks 6 to 13, after World History I's source checks (its unit 1 ends in week 3). Rows by load: the long product (the log, I.D.2's
evidence) runs across days 4 to 7.

- **Retrieval:** days 2, 3 and 4 (the grade 8 rows above). No readiness check.
- **End-of-unit assessment:** the mid-year check, day 8 (below), with the revised log scored as the I.D.2 product.
  Response time: day 9.
- **Host:** World History I unit 1 (wh1-sources-of-the-past, weeks 1 to 3), a host task only. ELA grade 9 unit 4's short
  research (weeks 14 to 17) comes after the unit, so the unit teaches the question and log itself and ELA then meets
  students who hold both. Stand-alone: "How much do street trees cool a town block in summer?"
- **Candidates:** kept, both on day 2 (about 7 minutes inside its show-me): the search plan's "terms that worked"
  column and a predicted-kinds line (9-10 cells), and the abstract and headings move (9-10 bold); the column is kept
  on day 5.

### Unit 2. Fair to every side (days 10 to 16, grade 9 weeks 18 to 29)

*How do we make a case that is fair to every side and honest about whose work it uses?* Owned: AASL.II.B.3,
AASL.III.A.3, AASL.VI.C.1. Rows: g9-fair-sides, g9-group-shapes-solution, g9-open-licenses.

Arc: two show-me days (each view at its strongest; licenses, fair use and the permission request), one practice day
on both, then four inquiry days that carry one group decision memo from evidence to draft to feedback and revision to
presentation, ending with each student's change line and the self-check. Fair sides come first because the memo
needs them; licenses before the memo because the memo is the first product that uses other people's images and
quotes. The memo takes four days because it holds two owned rows (III.A.3's change line, II.B.3's fair views).

- **Retrieval:** days 10 (g8-multiple-views-gather), 11 (g8-fair-use-basics) and 13 (g8-diverse-team). No readiness
  check.
- **End-of-unit assessment:** the year-end check, day 17, with the day 16 change line scored as the III.A.3 item.
  Response time: day 18.
- **Hosts:** World History I unit 3 (comparing interpretations, weeks 7 to 10) and ELA grade 9 unit 1 (discussion,
  weeks 1 to 5) both run before the unit; day 10 teaches stating each view at its strongest itself, and day 13's group talk
  opens with SEL's grades 9 to 12 talk turn card (taught there if a class has not had ELA's discussion unit). Optional host in step: ELA grade 9 unit 6, "Should school start later?"
  (weeks 20 to 24, beside days 11 to 13), a neutral school decision argued on both sides with data, which can feed
  the memo's evidence. Stand-alone: "Should our school add water refill stations, and where?"
- **Candidates:** kept: images, sound and video used by their terms (9-10 bold) on day 11 (about 5 minutes) and in
  day 12's sort; researching a real problem with others and proposing a change (9-10 bold) is the memo itself, no
  added time.

## Grade 10 (days 19 to 36)

### Unit 3. Who is missing? (days 19 to 25, grade 10 weeks 2 to 13)

*Where do I start on my topic, and whose views are missing from what I have found?* Owned: AASL.II.A.3,
AASL.III.C.2, AASL.II.C.2. Rows: g10-own-lens, g10-others-views-in, g10-database-deep.

Arc: the self-set topic and the private "where I start" note open the year, before any research shapes the reading;
subject terms and reference chains are shown and practiced, because they are how a missing view is found; the
seminar's ground rules are modeled and rehearsed unscored on day 22 before the scored seminar on day 24; day 23's
search for a missing perspective, each source checked laterally, is the session's main move (29 lateral minutes);
day 25 closes with the after-note and the self-check. g10-others-views-in owns two ids and gets four days; g10-own-lens
two; g10-database-deep two.

- **Readiness:** none (all assumed rows are grade 9's). Retrievals: days 19 (g9-fair-sides, which the "where I
  start" note builds on), 20, 22. AASL.II.C.2 is tagged only on the talk days (22, 24, 25 and the checks).
- **Interviews on day 23:** the questions are checked by the teacher and the consent note goes home by day 20;
  otherwise the student uses a missing-view source or the first-person set. The source path is the default.
- **End-of-unit assessment:** the mid-year check, day 26, with the seminar record (day 24) and the missing-view line
  (day 23) scored as its products. Response time: day 27.
- **Host:** ELA grade 10 unit 1's seminar (weeks 1 to 6), the same weeks; day 22 teaches the ground rules and say-back
  turn itself. Stand-alone: "What should a town do with an empty lot?"
- **Candidates:** kept: the 9-10 cells on one's own assumptions and on experience shaping what one takes from media,
  in the day 19 note (about 3 minutes) and the day 25 after-note; the 9-10 bold on confidence questioning views unlike
  one's own, as one rehearsal turn on day 22 (about 2 minutes) and one seminar turn on day 24.

### Unit 4. Putting sources together (days 28 to 34, grade 10 weeks 18 to 29)

*What do my sources say together, and can I trust a machine-made summary of them?* Owned: AASL.IV.D.2, AASL.VI.B.3.
Rows: g10-synthesis-map, g10-lateral-machine-text, g10-label-own-work.

Arc: the matrix and map are shown and practiced first; then the machine-made summary trace is shown and practiced
(days 30 and 31) and run on the student's own project (day 32), the band's second block of lateral time; the label
with point-of-use credits comes last. The matrix and map are drafted between sessions in the host course, with
feedback before day 34. **The labeled product** is a one-page synthesis summary written from the map between days
32 and 34 (in the host course or the notebook), holding a quotation, a paraphrase and a visual; day 34 revises the
matrix and map, places the point-of-use credits in the summary, labels it and shares it. Credits use the set
citation style (the works-cited format ELA grade 9 unit 4 taught), checked for readiness on day 27.

- **Readiness:** day 27, check 3's respond day, last ten minutes: one source cited in the set style (g7-citation-style,
  last used in library grade 8, 6 to 8 days 42 and 53, two grades back). Retrievals:
  days 28, 30, 33.
- **End-of-unit assessment:** the year-end check, day 35, with the revised matrix and map (day 34) as the IV.D.2
  product. Response time: day 36.
- **Hosts:** ELA grade 10 unit 7's research (weeks 26 to 31) is later than most of the unit, so the unit teaches the
  matrix itself on the stand-alone set and ELA's question may host day 34; World History II unit 11 (weeks 29 to 32)
  is a host task only, after the unit. Stand-alone: "How much brighter are our night skies than they were, and does it
  matter?"
- **Candidates:** kept: misinformation judged by its maker's motives (9-10 bold) inside day 31's lateral time;
  sponsored, opinion and news content told apart (9-10 cell) as the kind column on day 29 (about 3 minutes).

## Grade 11 (days 37 to 54)

### Unit 5. Beyond the article, and news that moves (days 37 to 41, grade 11 weeks 2 to 9)

*Where is the evidence that articles only report, and how do you judge a story that is still changing?* No owned
id; it revisits IV.B.1, VI.A.3 and IV.D.1. Rows: g11-advanced-search, g11-lateral-news.

Arc: two rows in five days (both build on grade 10 moves already practiced, so one practice day serves the search
row and the inquiry days serve the news row). Day 37 shows reports, data sets and primary data, the primary-and-news contrast and the sponsored placement, with
the saved search modeled in 2 minutes (its minute split is in the note); day 38 practices them, the saved search
included; day 39 shows holding judgment and degrees of slant;
day 40 follows the bridge case through four captures; day 41 puts both on the student's own question and closes.

- **Readiness:** none. Retrievals: days 37, 39.
- **End-of-unit assessment:** the mid-year check, day 42. Response time: day 43.
- **Hosts:** US History I unit 1's research inquiry (weeks 1 to 4) in step at the start; US History I unit 9's news
  reading (weeks 28 to 31) comes later, and either order works. Stand-alone: "How much water does farming in one dry
  region use, and has it changed?"
- **Candidates:** kept: primary and secondary read laterally for context (11-12 bold) on day 38 (about 3 minutes);
  an item gone viral and how it was made (11-12 cell) as day 40's fourth capture (about 4 minutes).

### Unit 6. Show how you know (days 44 to 52, grade 11 weeks 15 to 29)

*How can a reader check how you found, chose and used your sources, and was your work made honestly?* Owned:
AASL.IV.D.3, AASL.II.D.1, AASL.VI.C.2, AASL.VI.D.2. Rows: g11-method-note, g11-learn-across-difference,
g11-publish-for-audience, g11-honesty-review.

Arc: the method note and one full style are shown (day 44), then learning across difference (day 45), then citations
practiced (day 46); the interview or first-person set (day 47) comes before drafting so it shapes the note and the
published work; the note and the interview or first-person report (one paragraph: what I expected, what the person's experience
showed, what changed) are drafted with written feedback (day 48); day 49 shows choosing a form (about 12 minutes,
a sort of the four format cards, since ELA grade 11 unit 4 taught presenting) and models the honesty review on a
planted-fault project (about 20 minutes); day 50 revises the note and the report and makes the published form; day 51 runs the honesty review
alone on finished work; day 52 finalizes and shares the report, publishes and closes. The method note is the long product (four
days); each other row gets two.

- **Readiness:** none. Retrievals: days 44, 45, 49, 51.
- **End-of-unit assessment:** the year-end check, day 53, with the method note and bibliography (days 48 and 50), the
  interview or first-person report (drafted day 48, revised day 50, final day 52) and the published work (day 52)
  scored as products. Response time: day 54.
- **Hosts:** ELA grade 11 unit 4's reform research (weeks 12 to 16) is finished before the method note, so the note
  and honesty review look back on that project or the stand-alone; in step for days 47 and 50 to 52, ELA grade 11
  unit 8 (weeks 27 to 28) or US History I unit 7 (weeks 22 to 25), each under its own frame's sensitivity notes.
  Stand-alone: "What does it take to work a night shift?"
- **Candidates:** kept: the product carrying the line of reasoning and its evidence (11-12 bold) on day 50, no added
  time; judging one's product and process with self, teacher and peer feedback (11-12 bold) through day 48's teacher
  feedback, day 50's peer comment (about 4 minutes) and day 52's self-check.

## Grade 12 (days 55 to 72)

### Unit 7. A system for after school (days 55 to 60, grade 12 weeks 2 to 11)

*How will you find and check information when no teacher sets the question, and help someone else do it?* Owned:
AASL.VI.D.1, AASL.VI.D.3. Rows: g12-personal-system, g12-help-others.

Arc: the personal system is shown and practiced first (days 55 and 56), with the private strength-to-goal note
driving one next-step search the teacher sees only as search steps, run on the closed invented set of program
pages (practice pages use invented sites; a student may repeat it on the real web at day 60 or at home, with the
stop rule); then teaching one move to someone younger is
shown (day 57), the guide drafted with feedback (58), revised and rehearsed (59) and taught with a teaching record
(60). The guide is the longer product (four days).

- **Readiness:** none. Retrievals: days 55, 57.
- **End-of-unit assessment:** the mid-year check, day 61, with the revised guide and the day 60 teaching record scored
  together as the VI.D.3 product. Response time: day 62.
- **Host:** ELA grade 12 unit 1's reading and research routines (days 1 to 15, in step). Stand-alone: "Which training
  or program after school fits a goal you choose, and how do you check what its pages promise?"
- **Candidates:** kept, no added time: choosing materials by one's own interests and plans (11-12 bold) is day 56's
  next-step search; a leadership role helping others (11-12 bold) is day 60's teaching.

### Unit 8. The capstone (days 63 to 70, grade 12 weeks 16 to 29)

*What should be decided, who does the decision touch, and what does the evidence say?* Owned: AASL.I.D.3, AASL.II.D.3.
Rows: g12-capstone-decision, g12-community-stand, g12-lateral-capstone.

Arc: one show-me day models the decision and the communities map; on day 64 each student names their own
decision and drafts their own communities map (first 10 minutes), then runs the search on their own system; day 65
drafts the recommendation with its method note and the "where I stand and what follows" paragraph; a practice day audits a classmate's source list
(66), and one's own capstone is fixed from that audit, the map included (67); the published form is made (68) and shared (69); day 70
scores it. The capstone is the band's long product (six of eight days).

- **Readiness:** none. Retrievals: days 63, 64, 66, 68.
- **End-of-unit assessment:** day 70 (kind Check, assess `end`), inside the unit in week 29, so the score stands if
  seniors leave early: the capstone on its rubric plus a short sitting on the student's own capstone (an unseen source audited, and
  where they stand and what follows; no upstream trace, which check 8 uses). Response time:
  written feedback with the result, and day 72 where it runs.
- **Hosts:** ELA grade 12 unit 8's senior research (weeks 25 to 32) and US History II unit 12 (weeks 30 to 32) are
  later than most of the unit; the unit runs the capstone on its own question, one question serves both where the
  teachers agree, and library adds no second paper. Optional host in step: ELA grade 12 unit 6, "Public words and a
  public decision" (weeks 18 to 21, beside days 64 and 65), a town zoning decision, under its own frame's guards and
  the evenness rule. Stand-alone: "How should our school spend a one-time grant for
  student spaces?"
- **Candidates:** kept: answering a competing interpretation (11-12 bold) on day 65 (about 5 minutes of the draft);
  corroborating across diverse sources and balancing perspectives (11-12 bold) in day 63's map and day 66's audit, no
  added time.

## Course-level checks

| Check | Course day | Grade, week | Respond | What it samples |
|---|---|---|---|---|
| 1, grade 9 mid-year | 8 | 9, week 15 | day 9, week 16 | Unit 1 (its end-of-unit assessment), plus the log product. No earlier unit: the band's first check |
| 2, grade 9 year-end | 17 | 9, week 31 | day 18, week 32 | Unit 2 (its end), the memo's change line reused; unit 1 on new cases (one lateral check, one operator string) |
| 3, grade 10 mid-year | 26 | 10, week 15 | day 27, week 16 | Unit 3 (its end), seminar record and missing-view line reused; units 1 and 2 (a log recheck, a license reading) |
| 4, grade 10 year-end | 35 | 10, week 31 | day 36, week 32 | Unit 4 (its end), matrix and map reused; unit 3 (a subject-term search) and unit 2 (a fair-sides rewrite) |
| 5, grade 11 mid-year | 42 | 11, week 11 | day 43, week 13 | Unit 5 (its end); grade 10 units 3 and 4 (a synthesis map, a product label) |
| 6, grade 11 year-end | 53 | 11, week 31 | day 54, week 32 | Unit 6 (its end), four products reused; unit 5 (one fast-news capture) |
| 7, grade 12 mid-year | 61 | 12, week 13 | day 62, week 15 | Unit 7 (its end), guide and teaching record reused; grade 11 unit 6 (two citations, one honesty fault) |
| 8, grade 12 year-end | 71 | 12, week 31 | day 72, week 32 | Three compact band cases (units 1 and 4, on a street-trees or night-sky page; 2 and 4; 6 and 2); unit 7 and the capstone reused, not retaken |

Checks 1 to 7 are their units' end-of-unit assessments, the frame's design (a course-level check on the day right
after a unit's last day stands for its end, sequence.py accepts it). So their items for the unit just finished are
that unit's own unseen cases, not drawn from earlier units; each check's earlier-unit items are the new cases in the
table. Unit 8 ends in its own assessment (day 70), so check 8, right after it, draws unit 8's audit move from earlier
units' content: its first case is a lateral check with one claim traced upstream on unit 1's or unit 4's content,
labeled "units 1 and 4", and day 70 traces no claim upstream, so no form repeats within two weeks. Check items ask
the whole of each id or row they claim: the operator string (days 8 and 17) adds database or open web and why, the
license item (day 17) a credit line, the starting-point item (day 26) an invented reader's before note and findings
with whether the start shaped the reading, the fast-news item (day 42) which log entry changes after the fourth
capture, the honesty item (day 53) one source summarized against its own conclusion, and the guide item (day 61) an
all-rights-reserved image reused without permission. A `~` code on a later year's check is a one-item sample of an
id an earlier year owns, not a claim on the whole id. Each check is one sitting of about 35 of the 39 working minutes, alone, without the card;
a product scored with a check was drafted, given written feedback and revised inside the unit's days. No task form
repeats one given in the two weeks before.

**Owned codes on a course-level check.** Every owned code is on a course-level check of its year (days 8, 17, 26, 35, 53
and 61; unit 5 owns none, check 5 samples its revisited ids), except AASL.I.D.3 and AASL.II.D.3 (unit 8): they are sampled on day 70, the unit's own
end-of-unit assessment inside the unit, which the frame puts there so the score stands if seniors leave before week
31; check 8 reuses that score rather than retaking it.

**Leans on the calendar.** Each Cross-subject lean in the frame was read against data/plans/calendar.csv as the frame
gives it; where the core course teaches the move later (ELA 9 unit 4, ELA 10 unit 7, World History II unit 11, US
History I unit 9, ELA 12 unit 8, US History II unit 12) the library day teaches it itself on the stand-alone set and
says so in its note, inside the unit's days.

## Shorter path

- **A shorter session (40 minutes, about 34 working minutes).** The opening retrieval and the exit ticket drop to 3
  minutes each. Each of the nine lateral sessions runs 34 lateral minutes: days 3 and 30 drop from 39 to 34; days 7
  and 23 move their non-lateral work to the host period (day 7's findings note and self-check; day 23's "why it was
  missing" log line, written as homework in the notebook) and rise from 29 to 34; days 4, 5, 6, 31 and 32 keep 34,
  their other work (the operator string on day 4, the drafting on day 32) moving to the host course. Sum: 9 x 34 =
  306 lateral minutes, at least the field study's 300. A check sitting keeps every item; the
  host teacher gives the 5 minutes it needs from the host period, or the one-answer items go to the host period's
  opening.
- **A year about 10 school days short (about one session lost a year).** One fold-in day a year; nothing assessed,
  no lateral session and no owned part is cut:
  1. Day 15 (grade 9, unit 2 memo feedback and revision), saves the 45-minute session: the teacher's feedback is
     written between sessions, the other group's two-line feedback and the revision happen in the host period, and
     day 16 opens with 5 minutes to check the revised memo.
    2. Day 22 (grade 10, unit 3 seminar ground rules and unscored rehearsal), saves the 45-minute session: the
     ground-rule modeling goes into day 21's last 8 minutes in place of its exit ticket, and the rehearsal turns into
     day 24's first 8 minutes, before the scored seminar. Unit 3 keeps its practice day and every card stage.
  3. Day 43 (grade 11, check 5 respond), saves the 45-minute session: the regrouped reteach takes the first 10 minutes
     of day 45 (not a unit's first day), and the fresh try goes back on the marked sheet.
  4. Day 62 (grade 12, check 7 respond), saves the 45-minute session: the regrouped reteach takes the first 10
     minutes of day 64, and the fresh try goes back on the marked sheet.
  Total about 180 minutes, one session a year, leaving 17 of 18 sessions each year and 68 of the frame's 72 days.
- **Seniors leaving before week 31** (the frame's named grade 12 path). Days 71 and 72 fold: the capstone's day 70
  score stands as unit 8's end-of-unit evidence, check 8's band items are not taken that year, and the feedback on
  the capstone goes to each student in writing.
- **A left-out unit** (STANDARD.md section 4). A school may leave out a unit; its ids are named as not claimed that
  year on the course page and in the family note. Where a later unit uses a left-out unit's card (unit 4's trace uses
  unit 1's lateral routine card; unit 8's audit uses unit 6's citation style), that unit teaches the card's one-step
  form in its first ten minutes after the hook and claims none of the left-out unit's sub-skills (the leave-out
  bridge rule).
- **No once-a-week path** is named in the frame; a school meeting more often finishes sooner, which is a faster pace,
  not a shorter path.

## For the lead

None open.

Settled in the group fix pass (2026-11-26): the grade 8 rows are retrievals only (days 2, 3, 4, 10, 11, 13) with the
reteach-for-all line, by the lead call on a band year's first day; the readiness checks on days 1 and 9 are gone. The
lateral routine card (day 3) is the band's end form, and day 3 names how the grade 5 and 6 to 8 cards map to it. Talk
days 13, 22 and 24 open with SEL's grades 9 to 12 talk turn card. The frame now states the school-day formula (fix pass, lead call 4); unit 8's owned codes on day 70 and unit 5's
empty owned cell are settled (lead calls 10 and 12), so they are no longer items here.
