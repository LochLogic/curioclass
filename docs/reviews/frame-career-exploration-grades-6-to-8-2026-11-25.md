# Expert cold read: the course frame of Career Exploration, grades 6 to 8 (2026-11-25)

Course `career-exploration-grades-6-to-8` (catalogue `cte-explore`), the pilot frame for career education. Brief:
docs/pipeline/briefs/frame-read.md with the after-core changes of the job (bar, rows, frame-write.md's after-core
section, the frame gate in place of plan.py, the calendar, spot checks of named facts). I did not write this frame.

## What was read

- docs/agents/EXPERT.md; docs/agents/lenses/career-education.md; part 7 of docs/ADOPTION-BAR-SUBJECTS.md and the
  subject's row in "Before a scope and sequence in this subject"; docs/courses/career-education/STANDARD.md and
  APPROACH.md in full.
- docs/agents/decisions/DESK-ANSWERS.md, every entry naming the subject: 2026-11-16 (q-later-cs-career-library),
  2026-11-21 (q-prework-open-1 and -2; calibration; q-fix-career-1), 2026-11-22 (q-prog-cte-1), and 2026-11-25
  (the after-core frames as band frames).
- docs/pipeline/briefs/frame-write.md in full, including "After-core courses (added 2026-11-25)".
- The frame docs/courses/career-exploration-grades-6-to-8/frame.md in full; its row in data/plans/frames.csv; its
  rows in data/plans/calendar.csv; its `rows` cell in data/plans/course-list.csv (`grade:8`) over
  data/progressions/cte.csv (85 rows: 28 cluster and sub-cluster, 12 practice, 45 learner-goal rows holding 66
  indicators); data/progressions/cte-edges.md; the grade 10 rows at the seam.
- docs/reviews/progression-career-education-2026-11-21.md (to see what it left for the frame and what was fixed).
- docs/courses/CALENDAR.md (target weeks, stagger rule, generated table); scripts/frame.py (calendar_rows,
  check_weeks, clashes).
- The core frames the course leans on, at their Units and calendar rows only: ELA grade 8, Civics (social studies
  grade 8), math grade 7 (frame and data/plans/math-grade-7/days.csv for the last use of the three m7 rows).
- No career education frame comes before or after this one is written yet (Career Pathways is unwritten), so the
  seam was read against the grade 10 progression rows.

Gates run: `python -X utf8 scripts/frame.py check career-exploration-grades-6-to-8`: 0 failures (note: 7 units,
96 days, 92 in units and 4 for checks and respond days). `python -X utf8 scripts/stale.py check`: 70 files, 0
failures. `python -X utf8 scripts/frame.py calendar`: the course does not appear under any grade (finding 5).
My own script (scratchpad): all 85 grade 8 rows placed exactly once; every code in each unit's Owned standards cell
matches its rows' `standard` cells exactly (none missing, none extra); unit days sum to 92; every grade 8 row's
`hands_on` target appears in the Seams table and exists in grade 10.

**Band or one year.** The course is one year (STANDARD.md section 3: "each course is one year"), open to grades 6 to 8
in the catalogue and placed in grade 8. It is not a band course, so it rightly has no Year column and one mid-year and
one year-end check. Its "6-8" grade cell is a catalogue range, not three grade years (but see finding 5).

## Verdict

Sound, and a good pilot: every owned row is placed once with its codes in full, the seven units follow STANDARD.md's
settled grouping with one reasoned reorder, every unit has a field task, a plan day with feedback and revision before
a score, and the privacy, paths and sensitivity rules are carried into each unit. The biggest risk is the 64-session
short path, whose per-unit numbers cannot be traced to its fold rule and leave unit 7 too few sessions to keep its
packet and skill days. The one change that matters most for the pattern Pathways will copy is a per-unit fold table
that shows which sessions fold, so the short path is checkable; the second is fixing practice 2's thread order.
No finding is serious: 6 moderate, 6 minor, 2 nits.

## Findings, most serious first

### 1. Practice 2 is shown "returning" in units 5 and 6 before it is first taught in unit 7 (moderate; firm)

LAYER frame. REPEAT yes (lesson 5, "each thread starts where it is first used").

`g8-prac-2-communicate` sits in unit 7 (its row notes define it as the employer email and the spoken interview
answer). But the Practices column says "8 (creativity); 2 and 12 return" for unit 5 and "2, 4, 9 and 11 return" for
unit 6, and those units hold communication pieces (the note to the owner, the five-minute lesson). A practice is
"judged with two or three look-fors on the piece" (APPROACH.md); a unit writer reading "returns" will judge practice 2
in units 5 and 6 with look-fors no unit has taught. Every other "returns" in the column is correct (5, 10, 4, 11, 12 all
follow their first teaching).

Fix (settled below): keep the row in unit 7, where its notes put it. Unit 5 Practices cell: "8 (creativity); 12
returns; 2 practiced, not judged (its look-fors are first taught in unit 7)". Unit 6 Practices cell: "4, 9 and 11
return; 2 practiced, not judged (unit 7)". Pathways must check every "returns" against the first-teaching unit the
same way.

### 2. The short path's per-unit numbers do not follow its fold rule, and unit 7 cannot keep its packet and skill days (moderate; firm, arithmetic)

LAYER frame. REPEAT yes (lesson 9, days by load; lesson 21).

The Days bullet says 32 sessions fold: each cluster's second explore day (14) and "the units' own learner-goal days"
(18), giving units of 10, 9, 10, 8, 7, 10 and 6. The totals add up, but the per-unit folds do not match the unit
contents:
- Unit 7 (10 to 6) has no cluster and no explore day to fold into. Its 10 sessions are: day 1 (CD1.K1, CD1.A1), the
  high school day or days (ALL2.K4, A4, K6, K7, ALL1.K5, A5), two packet days, two skill days, the field task day,
  plan day, assessment day and respond day. Six sessions keep the four closing days and two more, so it must drop
  either a packet day (the teacher's check-in is on the second, g8-all2-3-own-learning's A3) or a skill day (the only
  first teaching of practice 2 and CD4.K2). The frame's own rule ("field task, plan, assessment and respond days never
  fold") leaves no room.
- Unit 6 (16 to 10) folds 6: four second explore days plus one own learner-goal day (the "who holds which jobs" day)
  is 5, not 6.
- Unit 2 (14 to 9) folds 5: three second explore days plus one own day (working for yourself) is 4; the fifth can only
  be the second day of the stand field task, which the rule forbids.
Pathways is told to copy this fold rule ("For the lead" item 1), so the fault would copy.

Fix: add under the Shorter path bullet a small table, one row per unit: full days, short days, and the named
sessions that fold. Then make unit 7's short path 8 (fold day 1 and the high school day into the skill and packet days
as their openers), unit 6's 11 (the five folds named), unit 2's 10, and take the 3 sessions back from unit 1 (10 to 9:
its job-study second day folds into the first) and unit 3 (10 to 8: the two routes days fold into the three explore
days of their clusters' second halves, or one of them stays and unit 4 gives one). Whatever the split, the table must
total 60 and each row must name its folds. The scope still names the sessions by day.

### 3. Unit 7 is short for its load on the full path (moderate; likely)

LAYER frame. REPEAT yes (lesson 9).

Weighed by codes per day: unit 1 22 codes in 16 days, unit 2 11 in 14, unit 3 19 in 15, unit 4 12 in 11, unit 5 14 in
10, unit 6 17 in 16, unit 7 13 in 10. Unit 7's 10 days hold the four closing days, two packet days and two skill days,
which leaves two days for eight learner-goal codes, three of them A-stage drafting tasks (CD1.A1 two plan steps,
ALL2.A4 next year's course choices from the school's own guide, ALL1.A5 a school plan for next term). Drafting next
year's courses is the most consequential real decision in the course (course selection in the spring of grade 8) and
it gets part of one day.

Fix: name unit 7's days in the What students learn cell: day 1 the hook and CD1.K1 and A1; day 2 the move to high
school, programs and learning outside class (ALL2.K4, K6, K7) with the course-choice draft begun (ALL2.A4); the school
plan for next term (ALL1.K5, A5) drafted on the field task day as the plan's changed line, so it gets the plan day's
feedback. If the fixer finds that too tight, move one day from unit 2 (14, the lightest by codes) to unit 7 (11) and
say so in both Why cells.

### 4. Bar part 7 item 6 asks for "safety taught"; the course teaches no student anything about safety at work (moderate; judgment call)

LAYER progression and frame. REPEAT new.

The frame names the NIOSH young worker curriculum (Talking Safety) only as a guide for the safety agent's read. No
row and no unit teaches students the basics of a safe first job: that a worker has a right to a safe workplace, the
common hazards for young workers, and that under-16 workers have limits on hours and tasks. Grade 8 students are 13 or
14 and some already work or will next summer (the frame plans for "students who already work"). Talking Safety (free,
federal) and OSHA's young workers pages (free, federal) are built for exactly this age (both opened, see Spot checks).
The lens wants hands-on work "with safety taught"; the paper production line in unit 3 and the job search in unit 7 are
the natural places.

Fix: in unit 7's job search skill day, add "a first job's rights: a safe workplace, the hours and task limits for
workers under 16 and 18, and who to ask (from the federal young workers pages, dated)", practiced, not owned; in
unit 3, the production line day names one hazard and its control as the worker would, from the NIOSH curriculum. Add a
"For the lead" item: whether a row should own it (a `~` on g8-cd4-2-job-search-steps or a note on
g8-sub-adv-manufacturing-production; Pathways owns Safety and Quality at depth). This adds a little content beyond the
rows, so it is listed for Cory below.

### 5. The stagger gate never sees this course: `frame.py` files its checks under grade "6-8", which the check skips (moderate; firm, the code)

LAYER process. REPEAT new.

scripts/frame.py `calendar_rows` takes the grade from the catalogue cell (`6-8`) for a course with no Year column;
`check_weeks` and `clashes` keep only `K` and `1` to `8`, so `frame.py calendar` lists no career checks for any grade,
and a future clash would pass silently. The frame's own claims hold by hand (below), but the gate cannot hold them for
this course, for a grade 7 placement, or for any later one-year after-core course with a range grade.

Calendar check by hand. The calendar rows match the frame: course day n on school day ceil(n x 160 / 96); unit 1 days
1 to 16 on school days 2 to 27, check 1 days 46 and 47 on school days 77 and 79 (week 16), check 2 days 95 and 96 on
school days 159 and 160 (week 32), and every Cross-subject school-day citation matches calendar.csv (ELA grade 8 unit 1
days 1 to 30 and unit 5 days 129 to 156; Civics unit 7 days 100 to 119). Grade 8 core check weeks are ELA 18, 25 to 26,
32; math 14, 24, 32; science 15, 32; social studies 10, 20, 29 to 30: week 16 holds none. For a grade 7 placement
(ELA 12, 22, 32; math 9, 24, 32; science 14, 32; social studies 13, 24, 32) week 16 is also clear. Even a grade 6
school (math grade 6 check 1 is school day 80, week 16) has no same-day clash with days 77 and 79, which is what rule 3
asks in grades 6 to 8.

Fix (scripts/frame.py, `calendar_rows`): for a course with no Year column, use the grade of its `rows` selector
(`grade:8`) when the catalogue grade is a range, so the course is read beside grade 8. The frame's Course-level checks
paragraph then adds: "For a grade 7 placement, week 16 is also clear of grade 7's core checks."

### 6. Unit 5's two-week habit practice does not fit before the plan day (moderate; firm, arithmetic)

LAYER frame. REPEAT new.

`g8-all1-3-study-habits` (ALL1.A3) has the student practice one habit "for two weeks" and report what it changed; the
frame puts the report on the plan day and says the practice "fits the unit's three weeks". The how-I-learn day comes
after Financial Services' three days, so about course day 62 (school day 104); the plan day is about course day 66
(school day 110): six school days, not two weeks.

Fix (settled below): the how-I-learn day becomes unit 5's day 2 (day 1 stays clean for the hook), so the practice runs
from about school day 101 to the plan day at school day 110, two school weeks. The Why cell's "three weeks" becomes
"from day 2 to the plan day, two school weeks".

### 7. One safety guide does not say what it is cited for, and the "not opened" sentence is now out of date (minor; firm, at source)

LAYER frame. REPEAT yes (lesson 22).

The Safety read bullet cites NSTA's position statement "Safety and School Science Instruction" "for handling soil and
seeds". The page exists, is free and carries that title (adopted October 2015, revised April 2024), but it covers
biological, chemical and physical hazards in general and does not mention soil, seeds or plants. NIOSH's Talking Safety
and OSHA's young workers page both hold at the given addresses.

Fix: keep all three by title, change "for handling soil and seeds" to "for hands-on hazards in general", and add "a free
school garden or extension soil-handling guide, chosen by the safety agent" for the seed tray. Replace "These links are
named from the writer's knowledge and were not opened in this pass" with "Opened 2026-11-25 by the frame read: all
three hold at these addresses; the safety agent opens each again before its read."

### 8. Two "unseen" check items may not be unseen (minor; firm)

LAYER frame. REPEAT new.

Check 1 uses "an unseen job card for a sub-cluster not studied at depth (Web and Cloud)", but unit 2's Digital
Technology explore days give every student a web developer job card, a Web and Cloud job. Check 2 draws an unseen job
card "from a Healthcare and Human Services or Education sub-cluster not studied", but unit 7's packet lets a student
choose any of the 58 sub-clusters, so some students will have studied that one in their packet.

Fix (settled below): check 1 uses Network Systems and Cybersecurity (no unit 2 card is in it; the help desk card is IT
Support and Services). Check 2 uses Health Data and Administration, with Early Childhood Development for a student whose
packet took the first; neither is a sensitive sub-cluster.

### 9. A lean on a non-core course is treated as retrieval with no bridge, and the core lean lacks its unit (minor; firm)

LAYER frame. REPEAT yes (lessons 18 and 32).

Computer science `g7-viz-choices` opens as a retrieval task in units 1 and 2 with "Not needed" in the if-later
column. Computer science is not a core course, so lesson 32 asks for a bridge the unit teaches, not an assumption that
grade 7 computer science was taken. Separately, lesson 18 asks for the core course's unit or days where its scope
exists; math grade 7's scope does exist (data/plans/math-grade-7/days.csv) and the frame gives only "grade 7, the year
before".

Fix: the g7-viz-choices row's last cell becomes "The field task sheet shows one fair and one misleading chart of the
same table and names the difference, so no student depends on computer science grade 7". The Readiness and retrieval
bullet names the last uses: `m7-unit-rate-fractions` and `m7-percent-problems` in math grade 7 unit 4 (days 47 to 68;
percent again in the year-end check, days 158 to 160), `m7-compare-populations` in unit 8 (days 139 to 157).

### 10. The interview task does not carry the disability line the progression read asked for (minor; firm)

LAYER frame. REPEAT new.

The progression read (finding 7) asked that the interview task state plainly that an employer may not ask about a
disability before a job offer and that a student never has to disclose a disability in a course task; the fix landed
on the grade 10 row only. Grade 8 students meet the interview first, in unit 7, whose teacher note has the lawful
question rule but not the disability line.

Fix: unit 7's last column, after "nothing private", add: "The teacher page states that an employer may not ask about a
disability before a job offer, that a worker may ask for a reasonable change to how a job is done, and that no student
discloses a disability in any course task."

### 11. Stale and conflicting notes (minor; firm, the repository)

LAYER process. REPEAT yes.

- docs/ADOPTION-BAR-SUBJECTS.md, career education row: "Owed: the second state rubric; five calls (Desk
  q-fix-career-1)". The five calls were answered 2026-11-21 (DESK-ANSWERS). Replace with "Owed: the second state
  rubric. The five calls were answered 2026-11-21 (Desk q-fix-career-1); the pilot frame is written and read
  (docs/reviews/frame-career-exploration-grades-6-to-8-2026-11-25.md)."
- The same row cites the approach approval as Desk q-prework-open-1, while APPROACH.md and DESK-ANSWERS give
  q-prework-open-2 for career education. Make the row say q-prework-open-2.
- Frame, "For the lead" item 11: "are being written beside this one" is work-status wording without `Pending(...)`.
  Replace with "Pending(docs/courses/computer-science-grade-8/frame.md, docs/courses/library-and-research-skills-grades-6-to-8/frame.md, docs/courses/social-and-emotional-learning-grades-6-to-8/frame.md):
  their units are cited once those frames set them; each lean here has an if-later line."
- APPROACH.md, "The kinds of day": "Skill day" sits on the Fluency row, while GLOSSARY's teaching day rule makes a
  first teaching Understanding. The frame resolves it correctly (a skill day that first teaches is Understanding).
  Replace the APPROACH row's first cell with "Understanding on first teaching, Fluency after" so Pathways and the scope
  writers do not inherit the conflict.

### 12. Week 32 for the year-end check: the brief's after-core line and stagger rule 3 disagree (minor; firm)

LAYER process. REPEAT new.

The frame flags this itself ("For the lead" item 3) and keeps week 32. I agree with keeping it: rule 3 makes week 32
a grades 6 to 8 finals week, scripts/frame.py already exempts it from the same-day test, and moving the course to 31
weeks costs unit 6 three sessions for no gain to a student. But the brief's line ("do not take the core subjects'
target weeks") read literally bars it, and every grade 6 to 8 after-core frame will meet the same question.

Fix: the lead adopts the frame's replacement text for frame-write.md ("In grades 6 to 8, a year-end check may share
the finals week (week 32) with the core subjects' year-end checks, as stagger rule 3 allows; mid-year checks avoid the
core target weeks."), and the frame's item 3 then records the ruling.

### 13. "Assessed the day before" is off by a day in both checks (nit; firm)

LAYER frame. REPEAT new. Unit 3's assessment is course day 44 and its respond day 45; unit 7's are 93 and 94. Both
What it checks cells: "since unit 3 (unit 7) was assessed two course days before, with its respond day between".

### 14. Two anchors have no named kind of free source, and one data note for the data sheets (nit; firm)

LAYER frame. REPEAT yes (lesson 23). The growing guide extract (unit 4) and the town budget line (unit 6) say "with
its source and year" but not what kind of source. Add "(a state extension service's planting calendar)" and "(a
town's adopted budget on its own public site)". For the who-holds-the-job figures in unit 6: the federal labor
statistics table that gives employment by occupation, sex, race and Hispanic or Latino ethnicity (table 11) now shows
2025 annual averages built from eleven months (October 2025 missing) and gives sex as the percent who are women only;
the unit 6 data sheet should say both.

## Spot checks of facts named from memory

| Fact in the frame | Checked at | Holds? |
|---|---|---|
| Talking Safety, NIOSH's free young worker safety curriculum, at cdc.gov/niosh/talkingsafety/ | The page itself | Holds (free; teaching manual, slides, videos) |
| OSHA young workers pages at osha.gov/young-workers | The page itself | Holds ("Young Workers - You have rights!", with an educators section) |
| NSTA "Safety and School Science Instruction", for soil and seeds | The page itself | Title and address hold; it does not cover soil or seeds (finding 7) |
| O*NET is CC BY 4.0, attribution in the credit line | O*NET Resource Center licence page | Holds (O*NET 31.0, credit the database and USDOL/ETA, link the licence, note changes) |
| BLS Occupational Outlook Handbook at bls.gov/ooh/ with a typical entry-level education field | The page itself | Holds (an entry-level education filter; 2025 pay shown) |
| 14 clusters, 72 sub-clusters, 3 cross-cutting: Digital Technology, Management and Entrepreneurship, Marketing and Sales | Search over Advance CTE's FAQ and guidebook and state pages | Holds |
| Federal Office of Disability Employment Policy pages (sensitivity source) | dol.gov/agencies/odep | Holds (a youth page; ADA material; no disclosure page found) |
| Federal employment-by-demographic tables (sensitivity source) | bls.gov/cps/cpsaat11.htm | Holds, with the two data notes in finding 14 |

The 2024 National Career Development Guidelines and the guidelines' terms were read in earlier runs (STANDARD.md
section 2); not rechecked.

## The lens checklist, course frame layer

| Lens line | Result |
|---|---|
| Clusters listed and toured with no personal plan made or revised | Met: the plan starts in unit 1 and every unit's plan day revises it, with a changed line per cluster |
| All 14 clusters given equal one-day slots with no depth anywhere | Met: each cluster gets two explore days and a field task, with one sub-cluster studied in a task; depth is in the field tasks and the packet |
| No applied task from a field in a unit; no data source named | Met: every unit has field tasks; BLS and O*NET named with dates and the "check these figures" line |
| A practice claimed with no task that practices it | Met for all 12, each with its task; but practice 2's "returns" before its teaching (finding 1) |
| Bar part 7 items 1 to 8 | 1, 2, 3, 4, 5, 7, 8 met at Exploration's level (the full resume, mock interview and program of study are Pathways', named); 6 met for hands-on, missed for "safety taught" (finding 4) |
| Fails-if lines (quizzes with no plan, no real data, no applied task, employability as a poster) | None present |

## The brief's data checks

- **Owned skills:** all 85 placed once; no unit teaches another grade's row (no career row exists below grade 8).
- **Standards in full:** every code placed in the unit that teaches its row; no lettered parts in this standard; the
  K and A pairs (CD2.K9 and A9, CD2.K4 and A4 and others) are both named in What students learn.
- **Units and reasons:** each Why cell holds; the order uses no model before unit 1 introduces it; the one reorder
  (serving people sixth) has two good reasons (the civics budget lean, five units of data reading before the pay-gap
  unit). Practice 2 is the one thread fault (finding 1).
- **Days:** 96 = 92 + 4, fits the subject's settled dose (three 45-minute sessions a week, 32 weeks); loads in
  findings 2, 3 and 6.
- **Source map:** not applicable (no base text).
- **Seams:** no course before; every hands_on target is in the Seams table and in grade 10; where the threads end is
  stated.
- **Cross-subject:** ELA grade 8 and Civics teach their leans first or the unit teaches its own (each with an if-later
  line); the after-core leans carry Pending notes and bridges, except g7-viz-choices (finding 9).
- **Stale notes:** finding 11.

## What is right and should not be touched

- Unit 1 introduces all six models before any cluster unit, as cte-edges.md asks; the self comes first, as the lens
  asks.
- The closing-day order (field task, plan day with written feedback and one revision, assessment day, respond day) and
  one scored piece a unit with unseen data items. Item 6 of "For the lead" is right: scoring three pieces a unit would
  need feedback days the year does not hold.
- The privacy rules: private inventory and plan, the family note's choices, no family money, no student naming their
  own group, the school address on the resume line, the same-cluster swap with every owned id still claimed.
- Placing no owned row on a sensitive sub-cluster, so the leave-out rule never costs a claimed id.
- The grade 7 placement bullet with its lean swaps.
- The Practices column header (item 5 of "For the lead") and the replacement text for frame-write.md.

## What the other career education frame should and should not copy

Career Pathways (grade 10) is the subject's only other frame (personal finance has no frame).

Copy: the opening unit that introduces the plan and its tools and the closing unit that defends the plan; the
closing-day order and one scored piece per unit; the dated data sheet with "check these figures this school year";
the Practices column; the readiness timing (unit 1 after the hook, other units at the previous respond day); the
privacy, paths and family-note rules; the paper path and devices bullets; the per-unit cost line; the packet format
(task template, data sheet, check-in line) at its own count; one-year shape with no Year column (Pathways is also one
year). Week 32 for its year-end check is already a finals week in high school (rule 4).

Do not copy until fixed: the short path's fold rule without a per-unit fold table (finding 2); "returns" in the
Practices column without checking the first-teaching unit (finding 1); retrieval on a non-core course's row with no
bridge (finding 9); the NSTA citation's purpose (finding 7); work-status wording about other frames (finding 11).
Pathways must also recount its own readiness: every Exploration row is two grades back, so each needs a readiness
check, not retrieval, as the frame's seam line already says.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Practice 2 stays in unit 7; units 5 and 6 say "2 practiced, not judged" | Its row notes define it as the email and interview; relabeling is the smaller change | docs/courses/career-exploration-grades-6-to-8/frame.md (Units, Practices cells) |
| The how-I-learn day is unit 5's day 2 | Gives the two-week habit practice two school weeks before the plan day | frame.md (unit 5) |
| Check 1's unseen sub-cluster: Network Systems and Cybersecurity | No unit 2 job card sits in it | frame.md (Course-level checks) |
| Check 2's unseen sub-cluster: Health Data and Administration, Early Childhood Development as the alternate | Not sensitive; the alternate covers a student whose packet took the first | frame.md (Course-level checks) |
| Week 16 for check 1 stands; week 32 for check 2 stands, pending the lead's wording of the after-core line | Both clear of same-day clashes in grades 6, 7 and 8 | frame.md; docs/pipeline/briefs/frame-write.md (lead) |
| Keep the three safety guides by title; the safety agent adds a free soil-handling guide | NIOSH and OSHA hold at source; NSTA is general only | frame.md (Safety read) |

## For Cory

- Scope (finding 4): should Career Exploration teach a short piece on safety and rights at a first job (a safe
  workplace, the hours and task limits for workers under 16), practiced in unit 7's job search day, with a row question
  for the lead? My pick: yes, practiced, not owned; it is free federal material made for this age.

## What it could not judge

- Whether the 96 and 64 session figures fit real schools: no national time figure exists (APPROACH.md), and none was
  found here.
- The contents of the DC school garden checklist PDF and the CSSS plant safety guide (not opened); the safety agent
  picks the soil guide.
- The SEL 6 to 8, library 6 to 8 and computer science grade 8 frames are not written, so the leans on them were read
  against their progression rows only.

## Sources

- https://www.cdc.gov/niosh/talkingsafety/ : Talking Safety, checked that it is NIOSH's free young worker curriculum.
- https://www.osha.gov/young-workers : OSHA's young workers pages, checked title and coverage.
- https://www.nsta.org/nstas-official-positions/safety-and-school-science-instruction : checked title, dates and
  that it does not cover soil or seeds.
- https://www.onetcenter.org/license_db.html : O*NET licence and attribution.
- https://www.bls.gov/ooh/ : the handbook and its entry-level education field.
- https://www.bls.gov/cps/cpsaat11.htm : the employment-by-occupation-and-demographic table, its 2025 data note.
- https://www.dol.gov/agencies/odep : the federal disability employment office's pages.
- https://careertech.org/resource/guidebook-career-clusters and https://www.acteonline.org/blog/cte-policy-watch/cross-cutting-career-clusters-new-resources/ :
  14 clusters, 72 sub-clusters and the three cross-cutting clusters (via search results).

## For the source list

- bls.gov/cps/cpsaat11.htm: the 2025 annual averages omit October 2025; sex is given as percent women only.
- osse.dc.gov/publication/school-garden-safety-checklist: a free state school garden safety checklist (PDF not
  opened; check it is a staff checklist, not a sign-off form).

## Confidence

Findings 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13 and 14 are firm (arithmetic, the repository or the source page).
Finding 3 is likely (a load judgment on counts). Finding 4 is a judgment call.
