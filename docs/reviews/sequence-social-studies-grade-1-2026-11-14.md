# Expert read: scope and sequence of Grade 1: Leaders, Helpers and Communities

Course `social-studies-grade-1`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md. Independent of the
Codex read of the same course, which was not opened.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the shared core and the social studies part of
  docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md.
- Cold: docs/courses/social-studies-grade-1/scope-and-sequence.md and data/plans/social-studies-grade-1/days.csv (96 rows).
- Beside them: the frame docs/courses/social-studies-grade-1/frame.md; the K and grade 1 rows of
  data/progressions/social-studies.csv; the MA.1 lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and
  the grade 1 rows of data/plans/calendar.csv; the lean rows of the ELA, math and science grade 1 frames; the
  sequence-write and frame-write briefs; docs/reviews/frame-social-studies-grade-1-2026-11-13.md,
  docs/reviews/baseline-1-social-studies-2026-11-14.md and this date's kindergarten read (for REPEAT tags).
- Gates: `plan.py check` passes this course (0 failures; the run's only failure is the us-history-ii frame).
  `frame.py calendar`: checks in weeks 14 and 31, no stagger break. `stale.py check`: nothing in this course.

## Verdict

The sequence is sound: units keep the frame's order and days, each unit's arc reaches its compelling question, every
owned code is on a day, and the checks sit on their target weeks. The biggest risk is the informed action in unit 7:
the class carries out its action on day 76 and looks back on day 78, three school days later, too soon for a
six-year-old's action to show anything. The change that matters most is the day swap in finding 1; after it, the
observation tasks need the missing prompts named in finding 3.

## Findings, most serious first

### 1. The informed action is looked back on three school days after it is carried out (moderate; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 76 (school day 123) carries out the action; day 78 (school day 126) looks back on "what
  changed after we acted". Day 77's note says it "gives the action time to show results", but it adds one lesson.
  Kindergarten's look back came about a week on, and grade 2's two weeks on.
- **Why it matters.** The look back is the step that makes the action informed rather than a one-off. With three
  school days, a litter or crosswalk action has nothing to show, and the claim on day 78 rests on no evidence.
- **Fix** (a day swap inside the unit, same codes per day): 69 who is a citizen (MA.1.T1.9); 70 name a problem and its
  supporting questions; 71 how people already work on it; 72 more than one view; 73 list ways and choose by secret
  ballot; 74 carry out the action (school day 120); 75 what makes a good citizen or community member (MA.1.T1.10);
  76 people who made their communities better, with the local helper case; 77 the same problem elsewhere; 78 look
  back and the written answer (school day 126). The action then runs six school days before the look back, and days
  75 and 76 let the class read its own action beside other helpers' ("Is what we did what a good community member
  does?"). The frame's reason for the unit's place is untouched.
- **Confidence.** Firm (the school days are in days.csv).

### 2. The four leaders are said to be in time order and are not (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Unit 3 says days 22 to 25 take Harriet Tubman, Abraham Lincoln, Wilma Mankiller and Cesar Chavez
  "in time order". Chavez's leadership of farm workers began in 1962; Mankiller was Principal Chief from 1985 to 1995.
- **Why it matters.** The lens asks for history in time order unless a reason is given, and the timeline model is
  carried in this unit (a leader's life in order). A wrong order taught as time order is a small accuracy fault.
- **Fix.** Swap days 24 and 25: Cesar Chavez on day 24, Wilma Mankiller on day 25. Notes move with their goals.
- **Confidence.** Firm (from memory; both dates are standard).

### 3. Observation tasks name codes they do not ask about (moderate; firm)

LAYER sequence. REPEAT yes (the same kind as the kindergarten read of this date, finding 2).
- **What is wrong.** Each end-of-unit task lists all its unit's codes, but these parts get no prompt:
  - Unit 1, day 9: D1.2 (which part of social studies a question belongs to, day 2).
  - Unit 2, day 18: D1.5 (which kinds of sources would help answer a question, day 15) and the past, present and
    future words of MA.1.T3.3 (day 12).
  - Unit 4, day 40: MA.1.T1.8 (set terms; judging whether to re-elect, days 37 and 38).
  - Unit 6, day 67: MA.1.T3.2 a, b and c are three parts, and "one symbol, phrase or song" checks one of them.
  - Unit 7, day 79: MA.1.T1.9 (who is a citizen, day 69); the read-aloud is about a helper only.
  - Unit 8, day 92: MA.1.T4.8 (choices made for values, day 87) and D2.Eco.9 (what a bank does, day 89).
- **Why it matters.** The record says a child has a standard nobody asked about, and the respond day cannot see the
  gap. C1 and C8 fail a standard with no check item.
- **Fix** (a short prompt each, inside the existing day): day 9, "Is this a history, geography, civics or economics
  question?"; day 18, "Which of these would help us find out about our school long ago?" with three source cards, and
  one sentence each about yesterday and tomorrow; day 40, "Should the class re-elect this leader? Why?" on a short
  made-up record; day 67, the child explains one part from the unseen source and gives a one-line meaning for a card
  from each of the other two parts; day 79, "Name two ways a person can be a citizen" (never about the child or the
  family; the read-aloud's helper may be a newcomer); day 92, "Why might someone buy from this shop instead?" and
  "Where can people keep money safe?".
- **Confidence.** Firm.

### 4. Argument days carry explanation codes (minor; likely)

LAYER standard. REPEAT yes (the progression read's finding 1: C3 codes that do not fully match the row's skill).
- **What is wrong.** Grade 1 owns D4.2.K-2 (an explanation in correct order with relevant facts) and D4.5.K-2
  (questions about explanations). Days 28, 29, 38, 39, 53, 78 and 91 teach or use a claim, reason and closing, which is
  C3's argument (D4.1.K-2, owned by kindergarten). Day 27 and the "in order" part of day 30 are the explanation days.
- **Why it matters.** The coverage table will show D4.2 as assessed by claim tasks, while an explanation in order is
  only taught on day 27. A reviewer tracing D4.2 finds argument work.
- **Fix.** Add D4.1.K-2 (as review, kindergarten's row) to days 28, 29, 38, 39, 53, 78 and 91, and keep D4.2 on them
  only where the day asks for steps in order. The row's own wording in the progression is the lead's call, not this
  read's.
- **Confidence.** Likely (C3 indicator wording from memory; data/standards/c3-indicators.txt holds codes only).

### 5. Unit 7 reaches no course-level check (minor; a judgment call)

LAYER frame. REPEAT yes (baseline 1, finding 6: year-end checks below what the year taught).
- **What is wrong.** Check 1 covers units 1 to 4; check 2 covers units 5, 6 and 8. Citizens and the action cycle
  (unit 7) are in neither.
- **Why it matters.** The record handed to grade 2 says nothing about community problems and taking part, which
  grade 2 builds on in unit 3 (ss2-people-environment).
- **Fix.** Check 2, day two: add one spoken item, "Name one way people in a town work on a problem, and one way a
  class could help." Frame and days.csv day 95.

### 6. Stale frame lines (minor; firm)

LAYER frame. REPEAT yes (the frame read's finding 4).
- The frame's Days bullet says a unit that assumes a kindergarten row "opens with a short spoken readiness check".
  The writer's For the lead item 1 is right; apply its wording.
- The same bullet says "32 teaching weeks"; CALENDAR.md and the sequence say 31. Fix: "31".

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 7 days reordered so the action is day 74 and the look back day 78 | Six school days for the action to show results | data/plans/social-studies-grade-1/days.csv days 69 to 78; scope-and-sequence.md unit 7 |
| Chavez day 24, Mankiller day 25 | Time order (1962 before 1985) | days.csv days 24, 25 |
| Prompts added to days 9, 18, 40, 67, 79, 92 | Every part of every unit standard is asked about | days.csv |
| D4.1.K-2 added as review on the seven claim days | The code matches the skill | days.csv |
| One unit 7 item added to check 2, day two | The year-end record covers unit 7 | frame.md checks table; days.csv day 95 |
| Frame Days bullet: retrieval task, 31 weeks | Matches rule 2 and CALENDAR.md | frame.md |

## Judged items the brief named

- **Readiness check or retrieval task.** The writer is right: every row a grade 1 unit assumes is a kindergarten row
  used the year before, none idle two grades, so each unit opens with a retrieval task in its first day
  (sequence-write rule 2, frame-write lesson 16). The frame's wording is stale (finding 6). One caution for the
  lead, not a fault here: C8 in the bar asks for checks "before" teaching, and K to 2 now holds none. The retrieval
  task's teacher notes can stand as that evidence if the unit plan says so; worth one line in the bar or the unit
  plan template.
- **Held look-back days and the calendar.** No shift here: days.csv uses the calendar's even spread, so it and
  calendar.csv agree. The right call is to hold the look back inside the unit by a day swap (finding 1), not by
  moving school days.
- **Writer's For the lead item 2 (W.1.1 later in ELA).** Agree: no change. The bridge (shared writing with a frame,
  dictation allowed) is the main teaching of the written claim for fifteen weeks, so unit 3's plan must model it in
  full on days 27 to 29, which the days already do.
- **The writer's own doubts.** None written beyond the two For the lead items.

## The lens checklist (scope and sequence layer)

| Line | Met, missed or n/a |
|---|---|
| A unit question answerable without its sources, or with one defensible answer | Met: all eight take more than one answer from the unit's sources |
| History out of time order with no reason | Missed in part: unit 3's leaders (finding 2) |
| A contested event with one telling only | Met: no contested event is taught as settled; leaders are told from what they did |
| Writing from sources builds short to long | Met: spoken claim (units 1, 2), written claim (unit 3), claim with a piece of evidence (unit 6) |
| Informed action once a year, the class's choice | Met, but its look back is too soon (finding 1) |
| Own-state method | Met: days 35 and 48 |
| Sensitive days flagged | Met: days 3, 22, 24, 25, 37, 49, 56, 60, 69, 81 |

## What is right and should not be touched

Supporting questions taught first; the calendar placed early so it runs all year; the secret ballot in unit 4 reused
in unit 7; the shared economics topic taught here once, as the frame splits it; every lean dated against the other
subjects' units and bridged where later (W.1.1, 1-ESS1-2); Plyler v. Doe and Barnette notes where they belong.

## What I could not judge

Whether a grade 1 class can carry an action through the school in one lesson (day 76, day 74 after the swap): it
depends on the action the class chooses; the unit plan should say the action may run as a short daily routine.

## Sources

From memory, not fetched in this run.
- C3 Framework, NCSS 2013 (rev. 2017): https://www.socialstudies.org/standards/c3 , wording of D1.2, D1.5, D4.1, D4.2, D4.5.
- United Farm Workers history (Chavez, from 1962): https://ufw.org/research/history/
- Cherokee Nation, Wilma Mankiller (Principal Chief 1985 to 1995): https://www.cherokee.org/
- Massachusetts 2018 grade 1 standards, through data/standards/ma-hss-2018.txt.

## For Cory

None.

## For the source list

None new.
