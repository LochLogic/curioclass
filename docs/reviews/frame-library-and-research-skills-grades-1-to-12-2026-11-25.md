# Frame read: Library and Research Skills, grades 1 to 12 (2026-11-25)

Fresh expert read of seven Curio Class library course frames, after the kindergarten pilot. Read only; this report is
the only file written.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/frame-read.md (the job), docs/agents/lenses/library.md.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md part 11; docs/courses/library/STANDARD.md and APPROACH.md (Pacing and dose,
  Sensitive ground, the kinds of day); docs/courses/CALENDAR.md (rule 4 for 9 to 12).
- The K pilot: docs/reviews/frame-library-and-research-skills-kindergarten-2026-11-25.md and its fixes file.
- The seven frames in full: docs/courses/library-and-research-skills-grade-1, -grade-2, -grade-3, -grade-4, -grade-5,
  -grades-6-to-8 and -grades-9-to-12, each frame.md.
- Rows: the `rows` cells in data/plans/course-list.csv over data/progressions/library.csv (98 rows), including the
  L103 row-note edits; data/plans/later.csv (L103); data/standards/aasl-words.txt.
- Cross-subject: data/plans/calendar.csv and the cited core units (ELA 3, 7, 9 to 12; science 3; civics 8; World
  History I and II; US History I and II), checked by a small script that every cited core skill id sits in the unit
  the library frame names. All cited ids sit where the frames say.
- Gates: `python -X utf8 scripts/frame.py check <course>` for each of the seven: 0 failures each (grade 1 30 days,
  grade 2 29, grade 3 30, grade 4 30, grade 5 30, 6 to 8 54 with 14 unit days a year, 9 to 12 72 with 14 a year).
  `progression.py check library`: 98 rows, 0 failures. `stale.py` fails 3 times, all in
  docs/courses/physical-education-grades-3-to-5/frame.md: another file, not a finding. `frame.py calendar` for the
  after-core list below.

## Verdict

The seven frames are sound and carry the K pilot's fixes: costed assessment forms, checks that sample earlier units,
every row scored somewhere, topic-open questions, NetSmartz named by title, the Check set read bullet, and the
Placement line naming after-core clashes. The L103 row notes in library.csv read well and every frame matches its rows,
but every frame still asks the lead to "apply" notes that are already applied. The real work left is small and local:
two grade 3 unit fixes, a grade 2 unit 3 load question, an honest count of the 9 to 12 lateral reading time, a
readiness entry for grade 9 like 6 to 8's grade 6, and in-step hosts for 9 to 12 unit 6.

## Findings, most serious first

No serious findings. Moderate first, then minor.

### Moderate

**M1. The L103 "Row changes" items are stale in all seven frames.** Course: all seven. LAYER: process. REPEAT: new.
What is wrong: each frame's For the lead holds a "Row changes (L103)" item ending "Pick: apply ...", but every note
it proposes is already in data/progressions/library.csv (commit 7cef7a5a4): grade 1 items 1 and 2, grade 2 items 1
and 2, grades 3, 4 and 5 items 1 and 4, 6 to 8 items 1 and 5, 9 to 12 item 2 (all seven 9 to 12 notes are in: truncation
in g9-databases-operators, the 11-12 lateral bold in g9-lateral-method, 9-10 depth in g9-open-licenses, embedded
citations in g10-label-own-work, slant to propaganda in g11-lateral-news, primary and secondary plus sponsored results
in g11-advanced-search, the next-step search and strengths goal in g12-personal-system). The "stays open" lists are
also wrong: grades 3, 4 and 5 say L103 "stays open for grades 1, 2 and 6 to 12"; grades 1 and 2 say "for grades 3 to
12". data/plans/later.csv L103 is still "open". Why it matters: a lead acting on these items re-applies done work, and
L103 never closes. Exact fix: in each frame replace the item's Pick with "Applied in data/progressions/library.csv
(commit 7cef7a5a4); nothing left for this grade." and drop the "stays open" sentence; the lead then marks L103 done in
later.csv for grades K to 12 (all eight library frames now carry a Check set read bullet).

**M2. The 9 to 12 lateral reading time is overstated.** Course: 9-12. LAYER: frame and progression. REPEAT: new.
What is wrong: the Lateral reading time bullet and the g9-lateral-method row note count seven sessions as "about 315
minutes" and "at least 300 minutes (seven 45-minute sessions)". That is gross time: each session has about 39 working
minutes (the frame's own Days bullet), so seven sessions are about 273 working minutes, and three of the seven share
the session with other moves (day 4: an operator string fixed and the log begun; day 7: a findings note shared and
the self-check; day 32: the matrix and map with the trace). APPROACH.md says the course "holds at least that much
lateral reading and claims no more" than the field study's six 50-minute lessons. Why it matters: the one number the
course rests on its single field study is the one a reviewer will check. Exact fix: make lateral checking the main
move of one more grade 10 day, unit 3 day 23 ("each missing-view source found is checked laterally before it goes in
the log"), so grades 9 and 10 hold eight sessions; rewrite the bullet as "eight sessions whose main move is lateral
reading (unit 1 days 3, 4, 6 and 7; unit 3 day 23; unit 4 days 30, 31 and 32), about 300 working minutes, about the
six 50-minute lessons of the one high school field study"; and change the row note's "(seven 45-minute sessions)" to
"(eight sessions, about 300 working minutes)". On days 4 and 7 move the non-lateral parts to the exit ticket or the
last five minutes so lateral work holds at least 30 of the 39.

**M3. Grade 9 enters without a readiness check, unlike 6 to 8's grade 6.** Course: 9-12. LAYER: frame. REPEAT: yes
(6 to 8 settled this at its own entry). What is wrong: the Seams section says every grade 9 row "opens as a retrieval
task ... none needs a readiness check". The 6 to 8 frame's Readiness and retrieval bullet reasons that library is not
a core course and a school may not run the grade below (lesson 32), so grade 6 gives each assumed grade 5 row as a
ten-minute readiness check with a reteach. The same holds at grade 9, more so, since students arrive from many middle
schools. Why it matters: a class that never had library 6 to 8 meets a lateral routine "with its card on hard cases"
on day 3 with nothing to retrieve. Exact fix: add a Readiness and retrieval bullet to the 9 to 12 frame on the 6 to 8
model: the seven grade 8 rows in the Seams table are given as ten-minute readiness checks (unit 1's four rows in the
last ten minutes of day 1, after the hook; unit 2's three in the last ten minutes of unit 1's day 7), a class that
shows a move missing gets the ten-minute reteach from the 6 to 8 show-me case next session; grades 10 to 12 stay
retrieval. Change the Seams sentence to match.

**M4. Grade 3 unit 3 has no in-step host.** Course: grade 3. LAYER: frame. REPEAT: new. What is wrong: unit 3's
named host, science's s3-climates, sits in science grade 3 unit 6 (weeks 25 to 30), long after the unit, and the
social studies grade 3 unit near it is excluded for its Native content. Bar part 11 and the lens want a real host task
for the inquiry days. Why it matters: as written the unit always runs on its stand-alone question, while an in-step
host exists. Exact fix: name science grade 3 unit 4, "Surviving where you live" (days 59 to 78, weeks 15 to 20,
neutral content), as unit 3's in-step host for the notes-in-boxes and source-kinds days; keep s3-climates as the later
use and the stand-alone question as the other path.

**M5. Grade 3 unit 4 scores the team skill on the first team meeting.** Course: grade 3. LAYER: frame. REPEAT: yes
(lesson 19, no score on a first-taught day). What is wrong: the team skill (III.D.1, with II.A.1) is scored on day 3,
the first team meeting, with no practice meeting before it; the frame's own Evidence bullet says a move is scored only
after it is practiced. Seven teams at four minutes also take 28 of the 29 working minutes. Why it matters: the score
measures a first try, and the day has no slack for a team that stalls. Exact fix: end day 2's inquiry with a
five-minute practice team meeting (one round, no score) and keep day 3's scored meeting, cut to three minutes a team
(21 minutes) so the day keeps eight minutes for set-up and the exit ticket.

**M6. Grade 2 unit 3 carries three rows in 6 days, and the fallback adds load.** Course: grade 2. LAYER: frame.
REPEAT: yes (pilot pattern: two-row units at 6 days or more). What is wrong: unit 3 holds three rows in 6 days, and For
the lead item 5's fallback "moves unit 2's practice-day shelf sort into unit 3's opening", which adds work to the
heaviest unit instead of relieving it. The Placement line also says "every grade 2 week from 28 on holds a core
check", but week 30 is free of core checks (ELA 15, 16, 32; math 18, 19, 29; science 20, 28; social studies 14, 31).
Why it matters: the fallback makes the problem it names worse, and the Placement reason is false. Exact fix: rewrite
item 5's fallback to move load out of unit 3: fold the maker-and-purpose show-me into unit 2's credit-line show-me
(both read the cover), giving unit 3 back a day; correct the Placement sentence to "weeks 28, 29, 31 and 32 hold core
checks; week 30 is free but a year-end check there would need a 31st or 32nd session".

**M7. 9 to 12 unit 6's hosts are not in step.** Course: 9-12. LAYER: frame. REPEAT: new. What is wrong: unit 6
(grade 11 days 44 to 52, weeks 15 to 29) names ELA grade 11 unit 4 (weeks 12 to 16) and US History I unit 1 (weeks 1
to 4) as hosts; the interview is held around week 20 and the method note drafted around week 22, after both host
projects have ended. The Cross-subject line says "before and beside this unit". Why it matters: the year's
show-your-method unit claims a live project it does not have. Exact fix: say plainly that the method note is written
looking back on the ELA reform project (finished in week 16) or on the stand-alone question, and name an in-step host
for the learning-across-difference and publishing days: ELA grade 11 unit 8, "How the other half lived" (weeks 27 to
28), fits a first-person set, or US History I unit 7 (weeks 22 to 25) under its own frame's sensitivity notes. Change
"before and beside this unit" to "before this unit". Unit 1's ELA grade 9 unit 4 host (weeks 14 to 17, after unit 1
ends) needs the same honesty: keep it as a lean, not a host.

### Minor

**m1. Grades 3 to 5 unit 4 has no respond step of its own.** Course: grades 3, 4, 5. LAYER: frame. REPEAT: new. What
is wrong: unit 4's reteach is folded into the year-end respond day, which also reteaches the year-end check's gaps and
holds the year's reflect step, in one 29-minute session. Why it matters: three jobs in one day, with no split, means
unit 4's groups are the first cut. Exact fix: name the split in the respond day's line (for example 12 minutes of
regrouped reteach from the unit 4 product rubric, 12 from the year-end items, 5 for the reflect step), or state that
unit 4's reteach groups come only from the revised product rubric and run on its revision day.

**m2. Grade 4 unit 3 and unit 4 wording.** Course: grade 4. LAYER: frame. REPEAT: new. What is wrong: unit 3's
observation "runs for a week between sessions" at one session a week, with no one named to run it when a librarian
teaches; the Days bullet calls unit 4's respond step "the revision day", but unit 4 day 7 is "share and self-check ...
then a regrouped reteach". Exact fix: add "the classroom teacher runs the daily two-minute observation; the
observation sheet goes home on the paper path"; make the Days bullet say "unit 4's respond step is the regrouped reteach
at the end of day 7".

**m3. Grade 5 unit 4 is tight at 6 days.** Course: grade 5. LAYER: frame. REPEAT: new (judgment call). What is wrong:
unit 4 carries two owned rows, a group product, a revision and a real-audience share in 6 days, with pool, form, draft
and bibliography in one 29-minute session, while unit 1 has 7 days. The family display inside a library session has
no one named to arrange it. Exact fix: unit 1 to 6 days (merge its two inquiry days), unit 2 weeks 7 to 12, mid-year
check week 13 (core-free in grade 5), respond 14, unit 3 weeks 15 to 20, unit 4 7 days in weeks 21 to 27, year-end
check week 28 unchanged; add "the classroom teacher and librarian set up the display; families see it at pickup or a
school event, never as a required visit".

**m4. g5-evidence-notes row note reads badly after the L103 edit.** Course: grade 5 (and 6 to 8, which cites it).
LAYER: progression. REPEAT: new. What is wrong: the note now runs "Students take answer-only notes from three sources
on one question mark where the sources agree ...", a missing comma and verb. Exact fix: "Students take answer-only
notes from three sources on one question, mark where the sources agree and where they differ on a fact, and arrange
the notes in a simple outline or mind map with help."

**m5. 9 to 12 unit 5 holds two rows in 5 days with no reason given.** Course: 9-12. LAYER: frame. REPEAT: yes (pilot
pattern). What is wrong: grade 11 unit 5 carries g11-advanced-search and g11-lateral-news in 5 days; the pilot pattern
asks 6 or more for two rows. Moving a day from unit 6 would leave four rows in 8, which is worse. Exact fix: keep 5
and write the reason in the Days cell: "both rows build on grade 10 moves already practiced (subject terms, the lateral
routine without its card), so one practice day serves both". No calendar change.

**m6. 9 to 12 Placement and For the lead item 3.** Course: 9-12. LAYER: frame. REPEAT: new. What is wrong: Placement
says "None falls in a week where data/plans/calendar.csv shows a core check", but the respond days in weeks 16 (grade
9), 13 (grade 11) and 15 (grade 12) sit in core check weeks the same paragraph lists; for 9 to 12 only the finals week
binds (CALENDAR.md rule 4), so nothing breaks, but the sentence is wrong. For the lead item 3 says the 6 to 8 Seams
note and the career pathways frame hold a Pending marker on this frame "which stale.py now fails": the 6 to 8 frame
no longer has one, and stale.py fails only on the physical education 3 to 5 frame. Exact fix: Placement: "No check day
falls in a core check week; respond days in weeks 16, 13 and 15 share their week with a core check, which 9 to 12
allows (CALENDAR.md rule 4)." Item 3: "The 6 to 8 seam is settled. The career pathways 9 to 12 frame's For the lead
item 6 asks whether library 9 to 12 uses lateral reading in grade 9 or 10 before unit 6: yes, units 1 and 4 (weeks 2
to 13 and 18 to 29 of grades 9 and 10)."

## Settled by the expert

| Question | Settled | Why |
|---|---|---|
| L103 row notes: do they read well and match the frames? | Yes, all of them, except the g5-evidence-notes grammar (m4) | Each note records a band-file difference named in its frame's Check set read bullet; no id or row moved |
| Two units a year in 6 to 8 and 9 to 12, not three | Keep two | 14 unit days a year; a third unit costs an end-of-unit check and respond day out of teaching days, and every row is placed and scored |
| 9 to 12 check 1 samples no earlier unit | Right | It is the band's first check; the grade 8 rows belong to another course, reached by the readiness checks (M3) |
| K to 5 year-to-year retrieval, no readiness checks | Keep | One-grade courses run by the same school library in sequence; the band entries (grades 6 and 9) are where students change schools |
| Lateral reading first owned in library before social studies 8 uses it | Meets the lens | The 6 to 8 frame names who teaches it first (grade 6) and the either-order retrieval rule |
| 6 to 8 grade 6 readiness checks | Right | Library grade 5 is not core (lesson 32) |
| aasl-words.txt "licence" (9 to 12 item 5) | The lead's shared-file edit stands | US spelling rule; replacement text is in the frame |
| 9 to 12 grade 12 calendar (capstone by week 29, days 71 and 72 fold) | Sound | The capstone score stands as unit 8's end-of-unit evidence if seniors leave |
| Every row scored somewhere | Yes in all seven | Checked row by row against the check tables |
| Cited core skills sit in the cited units | Yes | Script check over the calendar and core frames |

## For Cory

1. **6 to 8 load at 18 sessions a year** (6 to 8 frame's For the lead item 2): units of 4 to 6 days carry up to four
   owned ids (unit 6: four in 5 days; unit 3: three in 4 days). Keep the dose, or raise 6 to 8 above 18 sessions a year.
2. **The open lateral-reading and web-literacy material** (6 to 8 and 9 to 12 For Cory): your yes is needed to download
   the CC BY online-reasoning lessons and the open web-literacy book into S:\CurioClass-sources\library before any day
   adapts them. The grades 3 to 5 band file the K pilot asked for is already in the store.

## After-core calendar clashes (for the lead's calendar pass, not findings)

From `frame.py calendar`: grade 1 week 13 (computer science) and week 28 (ELD, physical education); grade 2 week 27
(ELD, health, media arts, physical education, theater); grade 3 week 29 (health); grade 4 weeks 14 and 29 (health);
grade 5 week 28 (health); grade 8 week 16, the 6 to 8 mid-year check beside career exploration's (cte) week 16 check.
9 to 12 is not checked by the tool; its check weeks are 15 and 31 (grades 9 and 10), 11 and 31 (grade 11), 13 and 31
(grade 12).
