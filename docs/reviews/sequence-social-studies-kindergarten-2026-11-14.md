# Expert read: scope and sequence of Kindergarten: Living and Learning Together

Course `social-studies-kindergarten`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md. Independent of
the Codex read of the same course, which was not opened.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the shared core and the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md.
- Cold: docs/courses/social-studies-kindergarten/scope-and-sequence.md and data/plans/social-studies-kindergarten/days.csv (64 rows).
- Beside them: the frame docs/courses/social-studies-kindergarten/frame.md; the K rows of data/progressions/social-studies.csv;
  the MA.K lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and the grade K rows of
  data/plans/calendar.csv; the lean rows of the ELA and math kindergarten frames; docs/GLOSSARY.md; the sequence-write
  and frame-write briefs (rule 2, lesson 16); the earlier frame read docs/reviews/frame-social-studies-kindergarten-2026-11-13.md
  and docs/reviews/baseline-1-social-studies-2026-11-14.md (for REPEAT tags).
- Gates: `plan.py check` passes this course (`sequence social-studies-kindergarten: 0 failure(s)`; the run's only failure is
  the us-history-ii frame's stale line). `frame.py calendar`: checks in weeks 15 and 30, no stagger break. `stale.py check`:
  nothing in this course.

## Verdict

The sequence is sound and teachable: units keep the frame's order and days, every owned code sits on a day, the
on-the-day holiday lessons fix the frame read's main fault, and both course-level checks sit on their target weeks.
The biggest risk is the end-of-unit observation tasks: they list every code of the unit but ask about only some of
them, so four of six units leave a standard part unchecked. The one change that matters most is to give each
observation task one short prompt per unchecked part (finding 2); the flag fact on day 45 must also be corrected
before a writer builds the day.

## Findings, most serious first

### 1. Day 45 gives the 1777 flag law as the reason for fifty stars (moderate; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 45: "its colors, thirteen stripes and fifty stars, and why (the 1777 flag law)". The 1777
  resolution set thirteen stripes and thirteen stars. One star per state, with the stripes fixed at thirteen, is the
  1818 Flag Act; fifty stars date from 1960 (Executive Order 10834, 1959, in force July 4, 1960). The progression row
  has it right ("13 stripes for the first 13 states, 50 stars for the states now"); the day sentence does not.
- **Why it matters.** The "the record says" sort on this day turns on the record. A writer building from this row
  puts a wrong source behind the stars, an uncorrected error under C3(a).
- **Fix.** Day 45 goal: "The flag: its colors, thirteen stripes for the first thirteen states and one star for each
  state, fifty today, and why (the 1777 flag law for the stripes, a star for each new state since 1818)". The teacher
  still says the dates; nothing changes on the student page.
- **Confidence.** Firm (the 1777 resolution, 4 U.S.C. 1 and 2, and the 1959 order agree; from memory, not fetched).

### 2. The observation tasks name codes they never ask about (moderate; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** An end-of-unit assessment must cover every part of every standard the unit teaches. The
  observation rows list every code of their unit, but the prompts leave these out:
  - Unit 1, day 9: D2.Civ.12 (how people make and change rules, taught day 5) and D2.Civ.10 (two points of view,
    taught day 7) have no prompt.
  - Unit 3, day 29: MA.K.T2.4 (the school's town on a state map, the school on a town map, day 28) has no prompt;
    the address prompt covers only MA.K.T2.3.
  - Unit 5, day 50: MA.K.T1.4 has four lettered parts, each "explain why"; the prompt asks for one symbol's why, so
    three of a to d go unchecked for each child.
  - Unit 6, day 60: the sort covers needs and wants and goods and services, but not D2.Eco.1 and the second half of
    MA.K.T4.2 (explain how people choose because there is not enough).
- **Why it matters.** The teacher records "can do" for standards no child was asked about, and the respond day
  re-teaches only what was asked. C1 and C8 read a standard with no check item as a fail.
- **Fix** (each a short spoken prompt inside the existing day, no added day):
  - Day 9: add "What could we do if a class rule does not work?" and "Tell me what your friend likes and why."
  - Day 29: add "Point to our town on this state map" (the same state map as day 28, the school's town only).
  - Day 50: the child explains one symbol's why from the unseen photograph, and the teacher points to a picture card
    of each of the other three for a one-sentence "why" (flag, eagle, anthem, Pledge: all four heard across days 49
    and 50).
  - Day 60: add "You can only pick one. Which, and why?" on two want cards.
- **Confidence.** Firm (the rows themselves).

### 3. Two days carry far more than one 20 to 30 minute lesson holds (minor; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Unit 4 has five teaching days for three lettered codes and three C3 indicators, and day 35
  carries every word of MA.K.T3.3b (about twenty time words, from "morning" to "next year") in one lesson. Day 44
  gathers six holidays on the strip, adds Presidents' Day with Washington and Lincoln (a kept candidate) and recalls
  three earlier on-the-day lessons, also in one lesson.
- **Why it matters.** Kindergartners hold a few new words a lesson; a writer will either rush the list or drop words,
  and MA.K.T3.3b is "in full" only on paper.
- **Fix.** Day 34 teaches morning, afternoon, night and yesterday, today, tomorrow with the ordered school day (they
  are the school day's own words); day 35 keeps now, then, long ago, before, after and last or next week, month and
  year; day 36's strip uses all of them. Note on day 35: the class's daily calendar talk (outside the course days)
  uses these words all year. Day 44: the three holidays already taught and Presidents' Day are the lesson; the other
  three go on the strip as picture cards with one sentence each.
- **Confidence.** Likely (kindergarten vocabulary load, from memory; the count is from the rows).

### 4. The spoken claim is first taught on the day its observation starts (minor; a judgment call)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 8 introduces "I think ..., because ..." and its note says "The observation task starts here";
  day 9 observes it. The model is shown once and watched at once, with no practice day between.
- **Why it matters.** C7: a new skill should be practised with help before it is checked. The claim is the course's
  through-line, and unit 1 sets the habit.
- **Fix.** Day 5 (the class proposes rules "and gives the reason for each") models the frame aloud: "I think we need
  this rule, because ...". Day 8 is then the second meeting and the observation can start there. No day moves.
- **Confidence.** A judgment call.

### 5. Veterans Day and Thanksgiving never fall in the same week (minor; firm)

LAYER frame. REPEAT new.
- **What is wrong.** The frame's holiday bullet teaches them together "or Thanksgiving alone if the class calendar
  puts them in different weeks". Veterans Day is November 11 and Thanksgiving is never earlier than November 22, so
  the fallback always applies, and Veterans Day would never have its lesson. The scope and sequence quietly does the
  other thing: day 42 sits in week 12, the Veterans Day week, and Thanksgiving is taught about two weeks early.
- **Why it matters.** A unit plan writer reading the frame will drop Veterans Day; one reading the sequence will
  teach Thanksgiving early. Both are defensible, but the two files disagree.
- **Fix.** Keep the sequence's choice. Day 42 note: "Taught in the Veterans Day week; Thanksgiving is met as a day
  coming soon, from the record and from what Wampanoag people say today." Frame, holiday bullet: replace the
  parenthesis with "(the two dates are always in different weeks, so the lesson falls in the Veterans Day week and
  meets Thanksgiving as a day coming soon)".
- **Confidence.** Firm.

### 6. Counts and claims in the prose that the CSV does not bear out (minor; firm)

LAYER sequence. REPEAT yes (the frame read's finding 5 and baseline 1's finding 10 were the same kind: prose that
says something the data does not).
- The header says "3 course-level check days, 3 respond days". days.csv has four check days (31, 32, 62, 63) and two
  respond days (33, 64), as the frame says. Fix: "4 course-level check days, 2 respond days".
- Unit 5 says "Every lettered part of MA.K.T1.4 has its own day". Days 45 and 46 do; c and d share day 47. Fix:
  "Every lettered part of MA.K.T1.4 is taught on a named day (c and d together on day 47)".

### 7. The calendar file and the frame lag days.csv (minor; firm)

LAYER process. REPEAT yes (stale lines, as in the frame read's finding 5).
- **What is wrong.** The on-the-day lessons (days 41 to 43) are taught in weeks 7, 12 and 19, so units 2 to 5 sit up
  to one week later in days.csv than in data/plans/calendar.csv, which frame.py builds from the frame alone. The
  frame's Days bullet also still says "32 teaching weeks"; CALENDAR.md and the sequence say 30.
- **The right call.** The writer's: CALENDAR.md already says a days.csv `school_day` column wins. The held lessons are
  the point of the frame's fix and must stay where their dates are. The check weeks (15 and 30) do not move, and I
  re-checked each lean against the days.csv weeks: all still hold (ELA unit 1 for SL.K.1, SL.K.3, W.K.1 and RI.K.1;
  ELA unit 2 from week 7 for RL.K.3, carried by its bridge; ELA unit 3 from week 16 for RI.K.3; math unit 2 for
  K.CC.B.5 and unit 3 for K.G.A.1).
- **Fix.** As the writer's For the lead item 1: `frame.py` (calendar_rows) reads `school_day` from days.csv where
  filled, then `frame.py sync`. Frame Days bullet: "across 30 teaching weeks".

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 45 goal names 1777 for the stripes and a star per state since 1818, fifty today | Correct record behind the "the record says" sort | data/plans/social-studies-kindergarten/days.csv |
| One short prompt added to each of days 9, 29, 50 and 60 (finding 2) | Every part of every unit standard is asked about | days.csv (goal of days 9, 29, 50, 60) |
| Time words split: day 34 takes morning, afternoon, night, yesterday, today, tomorrow; day 35 the rest | Kindergarten word load per lesson | days.csv days 34, 35 |
| Day 44 teaches four holidays in full, three as one-sentence cards | Load of a 20 to 30 minute lesson | days.csv day 44 |
| Day 5 models the "I think ..., because ..." frame aloud | A practice meeting before the day 8 to 9 observation | days.csv day 5 note |
| Day 42 is in the Veterans Day week and meets Thanksgiving as a day coming soon | The dates are never in one week | days.csv day 42 note; frame.md holiday bullet |
| Header counts 4 check days and 2 respond days; MA.K.T1.4 sentence reworded | Prose matches the data | scope-and-sequence.md |
| frame.py reads days.csv `school_day`; frame says 30 weeks | CALENDAR.md's rule that days.csv wins | scripts/frame.py; frame.md |

## Judged items the brief named

- **Readiness check or retrieval task.** Not applicable: kindergarten has no earlier grade, and the sequence rightly
  opens no unit with a readiness check. Unit 2's retrieval of unit 1's rules (day 11) is the right form.
- **Held days and the calendar.** Right as written: keep the held on-the-day lessons and the informed action's
  look back (day 17, eight school days after the decision, which meets the frame's "after a week"); fix the tool, not
  the days (finding 7).
- **Writer's For the lead item 1.** Agree, with the stale-weeks line added.

## The lens checklist (scope and sequence layer)

| Line | Met, missed or n/a |
|---|---|
| A unit question answerable without its sources, or with one defensible answer | Met: all six questions take more than one answer, and unit 4's answer is held to a named photograph |
| History out of time order with no reason | Met: unit 4 runs then to now; unit 5's on-the-day lessons are out of number order for a stated reason |
| A contested event with one telling only | Met: Thanksgiving from the record and from Wampanoag people today; the October holiday "as the community observes it" |
| Writing from sources once a year or not building | n/a at kindergarten (spoken claims every unit; written claims start in grade 1) |
| Informed action once a year, the class's choice | Met: unit 2, days 13 to 17 |
| Own-state method | Met: days 27 and 28, the school's address and the student's own state |
| Sensitive days flagged for the sensitivity read | Met: days 41 to 44, 48, 49, 52 |

## What is right and should not be touched

The on-the-day holiday lessons with their school days; the class decision placed early with a real look back;
position words before every map task; the address work on the school's address only; the Pledge and anthem as a
choice under Barnette; tokens worth one each at prices 1 to 5; every candidate cell settled with its place.

## What I could not judge

Whether each on-the-day lesson lands on its holiday in a real school year (CALENDAR.md gives positions, not dates;
the weeks chosen are plausible for a late-August start). The read-alouds themselves, which the unit plans write.

## Sources

From memory, not fetched in this run; each is a standard reference.
- C3 Framework, NCSS 2013 (rev. 2017): https://www.socialstudies.org/standards/c3 , indicator wording for D2.Civ.10,
  D2.Civ.12, D2.Eco.1, D2.His.10.
- 4 U.S.C. 1 and 2 (flag stripes and stars): https://www.law.cornell.edu/uscode/text/4/chapter-1
- Executive Order 10834 (1959), the fifty-star flag: https://www.archives.gov/federal-register/codification/executive-order/10834.html
- Massachusetts 2018 kindergarten standards, through data/standards/ma-hss-2018.txt.

## For Cory

None.

## For the source list

None new.
