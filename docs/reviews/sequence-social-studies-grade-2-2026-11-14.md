# Expert read: scope and sequence of Grade 2: Places and Peoples of the World

Course `social-studies-grade-2`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md. Independent of the
Codex read of the same course, which was not opened.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the shared core and the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md.
- Cold: docs/courses/social-studies-grade-2/scope-and-sequence.md and data/plans/social-studies-grade-2/days.csv (96 rows).
- Beside them: the frame docs/courses/social-studies-grade-2/frame.md; the grade 1 and 2 rows of
  data/progressions/social-studies.csv; the MA.2 lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and
  the grade 2 rows of data/plans/calendar.csv; the lean rows of the ELA and science grade 2 frames; data/plans/later.csv
  (L8); the sequence-write and frame-write briefs; docs/reviews/frame-social-studies-grade-2-2026-11-13.md,
  docs/reviews/baseline-1-social-studies-2026-11-14.md and this date's kindergarten and grade 1 reads (for REPEAT tags).
- Gates: `plan.py check` passes this course (0 failures; the run's only failure is the us-history-ii frame).
  `frame.py calendar`: checks in weeks 14 and 31, no stagger break. `stale.py check`: nothing in this course.

## Verdict

The strongest of the three: the order inside every unit builds, the informed action gets two real weeks before its
look back, hard history is named plainly with no role play, the frame read's D2.Geo.10 and D2.Geo.7 gaps are now
carried on named days, and the course-level checks sit on their target weeks. The biggest risk is the same as in
kindergarten and grade 1: four end-of-unit tasks leave a taught standard part unasked. The change that matters most is
those prompts (finding 1); after it, day 61 should stop carrying two forced moves in one lesson (finding 2).

## Findings, most serious first

### 1. End-of-unit tasks name codes they do not ask about (moderate; firm)

LAYER sequence. REPEAT yes (the same kind as the kindergarten and grade 1 reads of this date).
- **What is wrong.** Each task lists all its unit's codes; these parts get no prompt:
  - Unit 1, day 15: the second half of MA.2.T1.1, maps that show how people relate to their environment (day 5).
  - Unit 3, day 44: D2.Geo.8 (how city, suburb, town and farm meet needs from near and far, day 32) and D2.Geo.12
    (how a disaster affects people, day 33).
  - Unit 4, day 56: the purposes of government and "not every government is chosen in elections" in MA.2.T4.2 (day 50).
  - Unit 5, day 70: MA.2.T3.2, "a nation of immigrants" and its honest limits (days 63 and 64), and D2.Geo.7 (moves
    traced on a map, day 62).
- **Why it matters.** C1 and C8: a standard with no check item fails, and the respond day cannot re-teach a gap it
  never saw.
- **Fix** (a short item each, inside the existing day): day 15, "What does this map tell about how people use the
  land here?"; day 44, "Name one thing people in this place get from far away", with D2.Geo.12 recorded from the
  teacher's observation of days 33 to 36 (no written disaster item, given the sensitivity note); day 56, "Name one
  thing a government does for its people. Do all countries choose leaders by voting?"; day 70, trace the move on a
  world map, and one spoken line on why the phrase "a nation of immigrants" is used and whom it leaves out.
- **Confidence.** Firm.

### 2. Day 61 carries Cherokee removal and present-day refugees in one lesson (moderate; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 61 names the forced removal of the Cherokee and other Native nations, the Cherokee Nation and
  the Eastern Band today, and refugees fleeing war today, in one 30 to 40 minute lesson. Day 62 (pick reasons, trace
  moves on a map) carries no new content.
- **Why it matters.** Two hard-history topics in one lesson for seven-year-olds leaves no time for the human side and
  the present-day nations, which the lens and BASELINE rule 5 ask for, and some children in the room may be refugees.
- **Fix.** Day 61 keeps the Cherokee and other Native nations, with the nations today. Refugees fleeing war today move
  to day 62, as the present-day forced move the class traces on the map beside the others (codes add D2.His.14.K-2;
  the sensitivity note moves with it).
- **Confidence.** Likely (a judgment about load and age; the lens and the frame's own hard-history note agree).

### 3. Check 1 re-asks unit 3's claim two lessons after unit 3's assessment (minor; a judgment call)

LAYER frame. REPEAT new.
- **What is wrong.** Unit 3's assessment (day 44, school day 66) ends in "a claim naming its source" about how people
  live with the land in a pictured place. Check 1 (day 46, school day 68) asks for "a claim about how people live with
  the land in a pictured place, with a reason that names the source". Week 14 already holds days 44 to 47, all
  assessment or response (the writer's For the lead item 2).
- **Why it matters.** The course-level check is meant to see what has lasted; an item on content assessed two lessons
  earlier measures the same thing twice and makes the heavy week heavier.
- **Fix.** Keep the pin and the week, as the writer says. Change check 1's claim item to unit 2's content ("Where in
  this pictured place would you choose to live, and why? Name the source."), so it checks a claim on content six weeks
  old. Frame checks table and days.csv day 46; the unit 3 plan keeps its assessment short.

### 4. Course-level checks leave units 4 and 6 unchecked (minor; a judgment call)

LAYER frame. REPEAT yes (baseline 1, finding 6).
- **What is wrong.** Check 1 covers units 1 to 3; check 2 covers units 5 and 7. Countries and trade (unit 4) and the
  interviews and culture (unit 6) reach no course-level check, so the record handed to grade 3 says nothing about them,
  though grade 3 builds on both (ss3-levels-of-government, ss3-world-trade, ss3-community-history).
- **Fix.** Check 2, day two: the source set about a place includes one product label (why does this country trade
  for it?) and one short newcomer memory (what did the newcomer bring?). Frame and days.csv day 95.

### 5. Angel Island detentions were longer than "weeks or months" (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 66: "held for weeks or months". Most stays were a few weeks, many were months, and some
  people were held for close to two years.
- **Why it matters.** Rule 5 asks for the hard fact plain; "weeks or months" is short of the record at its hardest.
- **Fix.** Day 66: "held for weeks, months, and for some people up to two years, because a law kept most Chinese
  people out".
- **Confidence.** Firm (from memory; the station's own histories say so).

### 6. Unit 1's compelling question has one expected answer (minor; a judgment call)

LAYER frame. REPEAT new.
- **What is wrong.** "Can a map ever show the world just as it is?" The unit teaches that every flat map bends
  something, so the defensible answer is "no"; the lens asks for a question with more than one.
- **Fix.** "Which map shows the world best, and best for what?" Students then defend the Mercator, the Peters or the
  globe for a purpose, which is what days 9 to 11 already teach. Frame Units table, scope-and-sequence.md unit 1 and
  days.csv day 1. If the lead prefers to keep the question, day 15's spoken claim should at least ask "best for what".

### 7. Stale lines (minor; firm)

LAYER frame and process. REPEAT yes (the frame read's finding 6).
- Frame Days bullet: "a unit that assumes a grade 1 row opens with a short readiness check". The writer's For the lead
  item 1 is right; apply its wording.
- The same bullet says "32 teaching weeks"; CALENDAR.md says 31 for grade 2 social studies. Fix: "31".
- data/plans/later.csv L8 is open and says grades 2, 4 and 5 lost topics; the grade 2 part is now answered (the
  sequence names each unit's topics taught in full). The lead notes that in L8's detail.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Items added to days 15, 44, 56 and 70 (finding 1) | Every part of every unit standard is asked about | data/plans/social-studies-grade-2/days.csv |
| Refugees today move from day 61 to day 62 | One forced move per lesson for seven-year-olds | days.csv days 61, 62; scope-and-sequence.md unit 5 sensitivity line |
| Check 1's claim item on unit 2 content | Measures what lasted, not unit 3 twice | frame.md checks table; days.csv day 46 |
| Check 2, day two adds a product label and a newcomer memory | Units 4 and 6 reach the year-end record | frame.md checks table; days.csv day 95 |
| Angel Island: "weeks, months, and for some up to two years" | The plain record | days.csv day 66 |
| Unit 1 question: "Which map shows the world best, and best for what?" | More than one defensible answer | frame.md; scope-and-sequence.md; days.csv day 1 |
| Frame Days bullet: retrieval task, 31 weeks | Matches rule 2 and CALENDAR.md | frame.md |

## Judged items the brief named

- **Readiness check or retrieval task.** The writer is right: every grade 1 row a grade 2 unit assumes was used the
  year before, and the kindergarten science leans (K-ESS2-1, K-ESS3-1, K-ESS3-3) are idle one grade, not two, so each
  is a retrieval task or a one-question review, never a readiness check. The frame's wording is stale (finding 7). The
  C8 caution in the grade 1 read applies here too.
- **Held look-back days and the calendar.** No shift: days.csv follows the calendar's spread with the frame's pin, and
  the two files agree. The look back is held two weeks by teaching the resource days between the action (day 36) and
  the look back (day 42), which is the right way to do it.
- **Writer's For the lead item 2 (week 14).** Agree it stays; finding 3 lightens what the week asks.
- **The "full year" paragraph (L8).** Right: the topics handed to grades 1, 3 and 4 are named, and the days went to the
  made map, the action, two accounts, the interviews and the report, all inside the frame's days.

## The lens checklist (scope and sequence layer)

| Line | Met, missed or n/a |
|---|---|
| A unit question answerable without its sources, or with one defensible answer | Missed in part: unit 1 (finding 6); the other six are open and answered from sources |
| History out of time order with no reason | Met: unit 5 runs slavery, removal in the 1830s, Ellis Island, Angel Island, today |
| A contested event with one telling only | Met: "a nation of immigrants" with its limits; two accounts of one arrival |
| Writing from sources builds short to long | Met: a claim naming its source (unit 2), every closing after it, a short report with two facts (unit 7) |
| Informed action once a year, the class's choice | Met: unit 3, checked against published advice, look back two weeks on |
| Own-state method | Met: days 37 and 73 |
| Sensitive days flagged | Met: days 24, 33, 58, 60, 61, 64, 66, 75, 78, 82 |
| Native nations in the present tense | Met: days 61, 64, 78 |

## What is right and should not be touched

Sourcing taught on maps first and then used on every source; projections after sourcing so "who made this map and
what does it bend" has both halves; North America from a word bank (the kept candidate costs one day, inside the
unit); the action placed early in unit 3 with resource days filling the wait; two accounts after the arrivals the
class has read; the practice interview before the real one; every menu country with its own printed source set.

## What I could not judge

The menu of about 16 countries itself, which the unit plan fixes. Whether every family can arrange an interview by
day 75; the frame's fallback to school staff covers it.

## Sources

From memory, not fetched in this run.
- C3 Framework, NCSS 2013 (rev. 2017): https://www.socialstudies.org/standards/c3 , wording of D2.Geo.7, D2.Geo.8,
  D2.Geo.12, D2.His.14.
- Angel Island Immigration Station Foundation, history of the station (detention lengths): https://www.aiisf.org/history
- Massachusetts 2018 grade 2 standards, through data/standards/ma-hss-2018.txt.

## For Cory

None.

## For the source list

None new.
