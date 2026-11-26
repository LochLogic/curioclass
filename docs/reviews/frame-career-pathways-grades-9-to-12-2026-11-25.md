# Expert cold read: the course frame of Career Pathways, grades 9 to 12 (2026-11-25)

Brief: docs/pipeline/briefs/frame-read.md, with the lead's after-core changes (subject career education; the
cross-subject table checked against the computer science grade 9 and 10, SEL 9 to 12, library 9 to 12 and core
frames; the first job's safety and rights row and device practice 5 are open questions to Cory and are not counted;
the frame.py `split()` bite is a known lead item; the course-level check stagger is the lead's later calendar pass, so
clashes are listed separately).

## What was read

- AGENTS.md; docs/agents/EXPERT.md (head); docs/agents/lenses/career-education.md.
- The frame docs/courses/career-pathways-grades-9-to-12/frame.md in full (saved 22:40) and its row in
  data/plans/frames.csv (6 units, 96 days, 45 minutes, 3 a week, 32 weeks, year); its rows in data/plans/calendar.csv.
- data/progressions/cte.csv, all 143 grade 10 rows and the 85 grade 8 rows (assumes and hands_on both ways).
- The frame before: docs/courses/career-exploration-grades-6-to-8/frame.md (units table and Seams) and its three
  reviews (frame-career-exploration-grades-6-to-8-2026-11-25.md, -codex-, -fixes-), above all the pattern notes for
  Pathways. There is no frame after (the last career education course).
- docs/courses/career-education/STANDARD.md section 3 ("Pathways' width").
- The cross-subject frames' units tables and calendar rows: computer science grades 9 and 10, library and research
  skills 9 to 12, SEL 9 to 12, ELA grades 9 and 10, Algebra I, Civics, Government and Civic Life (grade 8); the
  check rows of every grade 9 and 10 course in data/plans/calendar.csv.
- scripts/frame.py (`split()` and the units check), scripts/course_pages.py (`codes()`),
  scripts/unit_skeleton.py (`split_list()`).
- Gates: `plan.py check` gives the course 0 failures (6 units, 96 days, 92 in units, 4 for checks); `stale.py check`
  flags nothing for the course.

No outside page was fetched for this read. Facts the frame cites from federal pages (the October 2025 gap in the
labor statistics table, the employer disability rule) were judged from knowledge and the pilot's reads, not opened
again.

## Verdict

A strong frame that takes the pilot's lessons well: all 143 rows are placed once, all 122 owned codes and all 106
carried codes sit in the unit that teaches their row, every seam is reciprocal and correctly cited, and the
broad-to-narrow spine, the privacy rules and the paper path are sound. It needs one fix before the scope and
sequence copies it (the lateral check on invented sources cannot be done on paper as written, so the owned CD3.R3 is
taught in part) and a pass on session arithmetic: the shared-device turn, unit 5's session list, two short-path rows
and three one-teacher performance days do not fit their 45 minutes or their counts as written. The remaining items
are wording and stale notes.

## Findings, most serious first

Counts: 1 serious, 6 moderate, 8 minor, 2 judgment calls (17). Not counted: the two open questions to Cory.

### Serious

**S1. The lateral check in unit 6 cannot be done on the paper path, so CD3.R3 is taught only in part.**
LAYER frame. REPEAT new (the pilot frame carries the same sentence, in its unit 1).
What is wrong: Cross-subject (library row) says unit 6 "teaches the lateral check it needs (open a new tab, see who
stands behind the source, compare two others)". The Devices bullet gives no device per student, and the three
sources are invented ("an invented training school ad, an invented job board post, an invented machine-made
summary"). An invented source has nothing behind it on the open web, and a student with paper has no tab to open.
Why it matters: CD3.R3 (rate sources) is owned here and nowhere after; the unit 6 check item "one source rated on the
four criteria" and the lateral-reading model's only use in the course both rest on it.
Fix: replace the parenthesis with a paper version, and add the materials to unit 6's "Curio Class writes" list: for
each invented source, a "who is behind it" sheet (an invented about page of the owner, and two other invented pages
that report on it, one that confirms and one that contradicts), so students leave the source, read the two others
and come back, on paper. Name on the teacher page that the same three steps run on a live browser where a school
has one. Apply the same wording to the pilot's unit 1 sentence.

### Moderate

**M1. The practice 5 device turn does not fit its session.**
LAYER frame. REPEAT new. Counted because it is a days-fit fact, not the open scope question.
What is wrong: Devices: "each pair takes a turn of about five minutes at one shared device". A class of 30 has 15
pairs: 75 minutes, more than one 45-minute session, and the short path puts the turn in session (1) with the hook and
the pick.
Fix: say the turns run across unit 4's first three sessions (the comparison table day and the two job study days on
the full path; sessions 1 to 3 on the short path) while the rest work on paper, and name it in unit 4's What students
learn. Or cut the turn to three minutes, as the pilot did, which still takes a full session.

**M2. Unit 5's fold list names sessions its full path does not have.**
LAYER frame. REPEAT yes (pilot finding 2, the short path).
What is wrong: the full path fits 13 only if the hook shares the first resume day and the carry-over lines sit inside
the two-day field task (2 resume + cover letter + outside class + 2 workplace + self-employment + 2 interview + 4
closing = 13). The fold list folds "the hook day" and "the carry-over day", which would make the full path 15, and
never folds the outside-class day or the self-employment day, which the short path merges (sessions 2 and 3).
Fix: fold list "5: the second resume day, the outside-class day (into session 3), the second workplace day, the
self-employment day (into session 2), the second interview day". In What students learn, say the hook opens the
first resume day.

**M3. Short path rows for units 1 and 4 leave one session unnamed.**
LAYER frame. REPEAT yes (pilot finding 2).
What is wrong: unit 1's "(5 to 8)" is four sessions for three closing days (plan, assessment, respond), because
session (2) packs the values day and the study-log day together. Unit 4 names the plan day twice ("(5) plan day" and
"(6 to 8) assessment, respond, and the trade-off and fallback revision on the plan day"), so (6 to 8) is three
sessions for two days. The floor count (18 closing, 20, 4 and 18 for teaching) is right; the rows are not.
Fix: unit 1: (2) values and learner moments (CD2.A5, ALL2.A2); (3) study log begun and the grade 8 school plan
reviewed (ALL1.R5); (4) the three sorts; (5) field task; (6 to 8) closing. Unit 4: (4) field task: the full plan
drafted (ALL2.A6, R6, practice 10, CD3.R1, CD1.R5); (5) trade-offs and fallback (CD2.R9, practice 6); (6) plan day
(CD1.R2, R1, CD2.R1); (7) assessment; (8) respond.

**M4. Three one-teacher performance days are booked to the minute.**
LAYER frame. REPEAT new.
What is wrong: unit 5's mock interview assessment is "each student about 90 seconds with the teacher" (30 x 90 s = 45
minutes, no changeover); unit 6's panels are "about four minutes with questions, ten students a session" (40 of 45
minutes, with the teacher on every panel); the packet check-ins are "about 45 minutes for a class of 30". The Days
bullet says the 45 minutes also hold set-up and collecting the work.
Fix: hear the interviews over two days (half the class on the written assessment day, half on the interview day,
which also gives the written pieces a quiet room), or 70 seconds on one question plus one follow-up; give the
panels nine students a session with a stated limit (a class over 27 adds a fourth panel day, taken from the unit's
work sessions); for check-ins say about 75 seconds, or split the class over packet days 2 and 3, 5 and 6, 8.

**M5. Where `split()` bites (the known lead item), with two bites the frame's note does not name.**
LAYER process. REPEAT new.
- scripts/frame.py line 134 splits on `;` and `,`. The note in For the lead item 2 names six carried codes; nine
  owned codes also contain commas (the five Arts, Entertainment, & Design sub-clusters, the three Hospitality, Events
  & Tourism sub-clusters and Marketing & Sales.Market Research, Analytics, & Ethics). They pass only because both
  sides split the same way, so the owned check runs on fragments (`Analytics`, `& Ethics`, `Entertainment`), and the
  contributed-code note at line 577 searches for truncated heads such as `CTE.Career Clusters.Arts`, which any Arts
  text matches.
- The six `~` codes in unit 2's Owned standards cell break the rule frame.py itself prints ("no ~CODE in Owned
  standards").
- scripts/course_pages.py `codes()` (line 285) splits on `[;,]` and also drops any code with a space, so every CTE
  cluster code (all 58 owned sub-clusters here) is missing from the public course page's standards list; and it
  strips `~`, so a fixed regex would publish the six carried codes as owned.
- scripts/unit_skeleton.py `split_list()` (lines 1513 and 2031) splits the progression's standard column the same
  way, so unit 2's skeleton will cite fragments.
- No other progression's standard column and no other frame's Owned standards cell uses commas (checked), so a
  semicolon-only split for those two fields is safe; Skills, assumes, hands_on and models keep the current split.
Fix (lead): add a `codes()` splitter (semicolons only) for the standard column and the Owned standards cell in
frame.py, course_pages.py and unit_skeleton.py, let course_pages accept codes with spaces and `&`, then take the six
`~` codes out of unit 2's cell. Correct item 2 to "six carried and nine owned codes".

**M6. Unit 3 puts its anchor decision in a shared day.**
LAYER frame. REPEAT yes (pilot findings 3 and 6, a unit short for its load).
What is wrong: the full path fits 11 only if luck and timing (CD2.A8, R8), how an experience shaped a choice (CD2.A6,
R6) and the uncommon-job decision (CD3.A6) share one 45-minute session; the fold list confirms it. CD3.A6 is the row
the pay-gap unit is built around (Sensitive ground bullet), and it asks for a reasoned decision written into the
plan.
Fix: give CD3.A6 its own day (unit 3 to 12 days) and take the day from unit 1 (12 days for 7 rows; 11 is enough once
M3's session list is set), so the course stays at 96. Or state that the luck and experience rows are short pieces
done as the day's opener, and say so in the unit row.

### Minor

**m1. SEL's "As above" is wrong for units 3, 4 and 6.** LAYER frame. REPEAT new. SEL 9 to 12 teaches
`g10-sa-snap-judgments`, `g10-sa-what-interests-me` and `g10-rel-different-ways` in grade 10 unit 9 (school days 53
to 73), and `g10-rel-teamwork` and `g10-sm-plan-and-tidy` in unit 11 (108 to 133): before this course's units 3 (74
to 90), 4 (92 to 112) and 6 (135 to 157). `g10-rds-who-is-affected` (unit 12, 135 to 155) runs alongside unit 6.
The "late in the year and after this unit" reading holds only for units 1, 2 and 5. Fix: in the unit 3, 4 and 6 rows,
"SEL 9 to 12 teaches it earlier the same year (unit 9 or 11, school days ...): retrieval for a student who takes SEL;
the bridge below stands for every other student." The units cited are all correct.

**m2. The computer science grade 10 row gives course days, not school days.** LAYER frame. REPEAT new. "Unit 3
(course days 22 to 29), unit 4 (days 33 to 42), unit 5 (days 43 to 53)" are school days 55 to 73, 83 to 105 and 108
to 133, the table's own unit. Fix: give school days. Units cited are correct.

**m3. Stale notes.** LAYER process. REPEAT yes (pilot finding 11). Cross-subject's opening says "the computer science,
library and SEL grade 9 to 12 frames are not written", and For the lead item 6 is still "Pending(...)": all four
frames are on file and the table cites their units. Fix: opening, "Frames on file: ELA grades 9 and 10, Algebra I,
Civics (grade 8), computer science grades 9 and 10, library 9 to 12 and SEL 9 to 12, whose units are cited below; the
optional courses' leans are bridges (lesson 32)." Item 6: "Reconciled 2026-11-25: SEL 9 to 12 places the goal and
decision rows in grade 10 units 11 and 12, after unit 1, so unit 1 runs its own; library 9 to 12 teaches lateral
reading in grade 9 unit 1, before unit 6."

**m4. "Why 96 fits" miscounts its rows.** LAYER frame. REPEAT new. "The other 51 rows (the learner goals and the twelve
practices)": the learner goals and practices are 57 rows (45 + 12); 6 of them sit in unit 2, and 51 is the count of
rows outside unit 2. "One student meets about 70 of the course's 143 rows": 57 + 3 clusters + their 12 to 21
sub-clusters is 72 to 81. Fix: "the 51 rows outside unit 2 (learner goals and practices; six more sit in unit 2)";
"about 75 (72 to 81)". If STANDARD.md section 3 carries the 70, the lead fixes it there.

**m5. The grade 12 fold is one session short, and the panels are all in week 31.** LAYER frame. REPEAT new. Unit 6's
panel days are course days 91 to 93 (school days 152 to 155, week 31); week 32 holds the respond day and check 2.
Losing weeks 31 and 32 loses course days 91 to 96 (6 sessions); the short path's unit 6 folds free 5 (three work
sessions, not "its two last"), so unit 6 at 9 sessions plus check 2's 2 is 11 sessions for the 10 left. Fix: "unit 6
runs its short path (9 sessions, days 81 to 89) and check 2 runs on day 90, its respond day folded into the plan and
portfolio sent home with written feedback"; "unit 6's panels fall in week 31".

**m6. Unit 4's "mid-year progress check, in weeks 19 to 23, the year's middle."** LAYER frame. REPEAT new. Week 16 is
the middle; weeks 19 to 23 open the second half. Fix: "the private progress check, early in the year's second half
(weeks 19 to 23)".

**m7. Unit 2's Practices cell: "3 practiced, not judged (unit 6 judges it, on the failed-first-try field task)".**
LAYER frame. REPEAT new. Reads as if unit 6 judges practice 3 on a unit 2 task; unit 6 judges it on the project's
second try. Fix: "3 practiced, not judged, on each block's failed-first-try field task (unit 6 judges it on the
project's second try)".

**m8. The school garden guide's address is a development host.** LAYER frame. REPEAT new (the pilot has the same
address). `https://dev.extension.umd.edu/resource/...fs-1077` is a "dev." host, which may move or close. Fix: the
safety agent opens the extension's live site for FS-1077 at its read and replaces the address, keeping the title
(the bullet already allows this); note it now so the "dev." address is not copied further. Also a nit: line 3 says
"catalogue"; it is the repository's template wording (82 frames), so leave it to a sweep.

### Judgment calls

**J1. Real workers.** LAYER frame. REPEAT new. The lens asks for stereotypes "countered with real workers from many
groups"; this frame uses invented workers in every block and real workers' public accounts only in unit 3. Invented
workers are the right default for privacy and currency. Pick: keep, and let each cluster data sheet carry one real
worker's dated public account (a published interview or a federal profile) where one is free to read, marked with
source and date.

**J2. Feedback load in unit 2.** LAYER frame. REPEAT new. Every field task piece gets written feedback "after class"
before the next session's five-minute fix: about 30 pieces three times a week for nine weeks, on two or three
look-fors. That is heavy but the design depends on it. Pick: keep; the scope and sequence gives each field task sheet
a one-line look-for strip the teacher ticks, so the feedback is a tick and a word, not a paragraph.

## Not counted (open questions to Cory)

- The first job's safety and rights row (now practiced, not owned, here in unit 5's teacher page).
- Practice 5 for a student with no device (For the lead item 3). M1 is only the time the turns take.

## Calendar clashes (for the lead's later pass; rule 4 makes none of them a break)

- School day 72 (week 15): this course's check 1 respond day is the same school day as library 9 to 12's mid-year
  check (grade 9 and grade 10 sections).
- Week 15: SEL 9 to 12's mid-year check (school day 75, grades 9 and 10) and computer science grade 10's check (75
  to 78, into week 16) sit in the week of this course's respond day.
- Grade 9 placement: ELA grade 9's check 1 respond day (school day 66) is in week 14, the week of this course's check
  day (70), so the frame's "weeks 14 and 15 are also clear" holds for check days only.
- The grade 10 core list omits chemistry's check 1 respond day (school day 56, week 12); no clash.
- Week 32 holds every course's year-end check (finals week), this one included.

## The brief's data checks

- **Owned skills:** all 143 grade 10 rows placed once (gate and a semicolon-only recount); no row from another grade.
- **Standards in full:** all 122 owned codes (58 sub-clusters, 64 indicators) listed in the unit that teaches their
  row, none extra; all 106 carried codes named in each unit's "Carried from grade 8" list; the 5 adult-only
  indicators left out with reasons. S1 is the one standard taught in part.
- **Units and reasons:** each Why cell holds; no model or skill is used before it is taught (the models table checks
  out; lateral reading's first use is unit 6, readiness on unit 5's respond day).
- **Days:** 96 = 92 + 4; 12 + 29 + 11 + 13 + 13 + 14 = 92; short path 8 + 20 + 7 + 8 + 8 + 9 = 60 and its floor count
  is right. Session fits: M1 to M4 and M6.
- **Source map:** not applicable (no base text).
- **Seams:** every grade 8 `hands_on` points at a grade 10 row that `assumes` it back, and every Exploration unit and
  day span cited matches the Exploration frame and calendar. Handed on: none, correctly.
- **Cross-subject:** every lean in the rows' `cross_subject` is in the table. The cited units and days check out for
  ELA 9 (units 4 and 7), ELA 10 (unit 7, days 128 to 155), Algebra I (units 1, 3, 5), Civics (unit 7, days 100 to
  119), computer science 9 (units 2 and 4), computer science 10 (units 3, 4, 5), library 9 to 12 (grade 9 unit 1,
  grade 10 units 3 and 4) and SEL 9 to 12 (grade 10 units 9, 11, 12). Timing wording: m1, m2.
- **Stale notes:** m3.

## The lens checklist, course frame layer

| Line | Result |
|---|---|
| Clusters toured with no personal plan made or revised | Met: the plan is revised on every plan day and goes home |
| One cluster only (Pathways) | Met: three clusters at depth per student, all 14 built |
| No applied task from a field; no data source named | Met: a field task per sub-cluster; federal sources named with years |
| A practice claimed with no task that practices it | Met: all 12 placed with tasks and evidence attachments |
| Many paths, no ranking; stereotypes countered | Met; J1 on real workers |
| Honest about what a school adds | Met: work-based learning, labs, employers named as school additions with a paper path |

## Settled by the expert

| Choice | Reason |
|---|---|
| The ~ hack stays until the lead fixes the splitter | Taking it out now fails the gate; it is marked and explained in For the lead |
| SEL, library and computer science leans stay bridges even where taught earlier | They are optional courses (lesson 32); only the timing wording changes (m1) |
| Unit 3 may take its day from unit 1 (M6) | Unit 1 has the lightest load per day; course total stays 96 |
| Interviews over two days (M4) | Keeps one full performance per assessment day and the teacher hears every student |
| Lateral sheets written by Curio Class (S1) | Invented sources keep companies and real ads off student pages |

## For Cory

Nothing new. The two open questions above stand as the lead has them.
