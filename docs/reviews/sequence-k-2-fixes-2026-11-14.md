# Fixes applied: social studies scope and sequence, kindergarten to grade 2

2026-11-14. The scope and sequence fixer for social-studies-kindergarten, social-studies-grade-1 and
social-studies-grade-2 applied the expert reads (docs/reviews/sequence-<course>-2026-11-14.md), the Codex reads
(docs/reviews/sequence-<course>-codex-2026-11-14.md), each course's For the lead items, and the lead's four settled
calls of 2026-11-14 (with the coordinator's clarification of call 1: a row used the year before or earlier the same
year opens as a retrieval task; any other earlier-grade row opens its unit with a readiness check). No days were
added, no unit moved, and no check week moved off its CALENDAR.md target.

Files changed: for each course, docs/courses/<course>/scope-and-sequence.md, data/plans/<course>/days.csv and
docs/courses/<course>/frame.md. No course here has a base text, so no source-map.csv.

Settled call 1 (readiness or retrieval) needed no change: kindergarten has no earlier grade, and every row grades 1
and 2 assume was used the year before, so every unit opens with a retrieval task, as days.csv already had it. The
grade 1 and grade 2 frames' stale "readiness check" wording is fixed. Settled call 2: kindergarten's held on-the-day
lessons stay where days.csv has them. Calls 3 and 4 are applied in every course (below).

## Kindergarten (social-studies-kindergarten)

Expert read:
1. Day 45 flag record: **applied**. days.csv day 45: thirteen stripes from the 1777 flag law, a star per state since
   1818, fifty today; frame unit 5 row adds the 1818 law.
2. Observation tasks miss parts: **applied** (with call 4). days.csv days 9, 18, 29, 39, 50, 60 now ask about every
   part of every listed code (prompts named under Codex 1); days 31, 32, 62, 63 (course-level) likewise.
3. Load of days 35 and 44: **applied**. Day 34 takes morning, afternoon, night and yesterday, today, tomorrow
   (MA.K.T3.3b added to its codes); day 35 the rest, with the daily calendar note. Day 44 teaches Presidents' Day and
   the three holidays already taught in full; Independence Day and Memorial Day go on as picture cards. The read said
   "the other three": the list holds only two more, so two.
4. Claim frame modelled before it is observed: **applied**. Day 5 note models it; day 8 note says second meeting.
5. Veterans Day and Thanksgiving: **applied** (expert's version; see Codex 4). Day 42 goal and note; frame holiday
   bullet; scope and sequence unit 3 line and a "Holiday dates are positions" paragraph.
6. Prose counts: **applied**. Header "4 course-level check days, 2 course-level respond days"; unit 5 MA.K.T1.4
   sentence.
7. Calendar and stale weeks: **applied**. Frame "30 teaching weeks"; frame.py change listed for the structure pass
   (settled call 2); the scope and sequence's For the lead item now records it as settled.

Codex read:
1. Assessments do not secure full performances: **applied**. Day 9 (rule outside school, changing a rule, my view
   and a friend's, rule-following noted through the unit); day 18 (job carried through, noted on day 17;
   responsible or in-charge characters); day 29 (map and globe alike and different, the two world maps with help,
   the day 28 location work kept); day 39 (personal, nature and text sequences, near and far time words, how a photo
   tells about the past, observed over days 36 to 39); day 50 (all four symbols, observed over days 45 to 50); day 60
   (choice with a reason, a buying or trading question, earned money).
2. D1.1 and D2.Eco.3 untaught parts: **applied**. Day 1 "Finding this out matters to me because ..."; day 9 look back;
   day 53 knowledge, skills and tools, modelled then told; day 60. Progression row wording: structure pass.
3. Informed action has no implementation: **applied**. Day 14 takes the first step and the arrangement runs to
   day 17; day 17 uses a before-and-after chart.
4. Calendar and holiday dates: **applied in part**. Generator change: structure pass. Holiday positions marked as
   provisional with a placing rule: applied. Renaming day 42 a November study with Veterans Day recalled afterwards:
   **not applied**; the expert's version kept, because it gives Veterans Day an on-the-day lesson in its own week and
   still meets Thanksgiving before it comes, where Codex's would lose Veterans Day's day.
5. Shorter path: **applied**. Scope and sequence "The 20-minute route" paragraph (same 64 lessons, nothing assessed
   cut).
6. Stale prose: **applied**. Header counts, MA.K.T1.4 sentence, frame cross-subject introduction.

Settled call 3: check 1 (after unit 3) puts its map items on the classroom places of units 1 and 2 (day 32); check 2
(after unit 6) takes its needs, wants, goods and services items from unit 2's jobs and unit 4's photographs (day 63).
Both said in the scope and sequence.

## Grade 1 (social-studies-grade-1)

Expert read:
1. Look back three school days after the action: **applied**. Unit 7 reordered by day swap: 69 citizens, 70 to 74 the
   action cycle (action on day 74, school day 120), 75 good community member read beside the action, 76 people who
   improved communities (the helper case, candidate note moved), 77 elsewhere, 78 look back (school day 126). Scope
   and sequence unit 7 and frame informed-action bullet.
2. Leaders out of time order: **applied, with Codex 2's case** (see there). Day 24 Dolores Huerta (1962 on), day 25
   Mankiller (1985 to 1995); episode dates in day 22's note and the scope and sequence.
3. Observation tasks miss parts: **applied** (with Codex 1 and call 4): days 9, 18, 30, 40, 54, 67, 79, 92, and the
   course-level days 42, 94, 95.
4. Argument days carry explanation codes: **applied**. D4.1.K-2 (review) on days 28, 29, 38, 39, 53, 78, 91, and on
   check and respond days 42, 43, 95, 96; D4.2 left on 27 (taught), 30 and 42 (each asks for steps in order), 31.
5. Unit 7 in no course-level check: **applied**. Day 95 adds how people in a town work on a problem and how a class
   could help; frame checks table.
6. Stale frame lines: **applied**. Frame Days bullet: retrieval task, 31 weeks.

Codex read:
1. Assessment omissions: **applied** in days 9 (part of social studies and a fact; what belonging gives; roles incl.
   someone not in charge; rule-following noted day 8), 18 (calendar pattern with yesterday and tomorrow; which source
   would help and why), 30 (responsibility, a question about the leader, asking and answering recorded), 40 (election
   or issue vote; re-election from a made-up record, day 38 noted), 54 (what the map stands for, what makes a capital,
   rivers, lakes, mountains; day 52 map criteria), 67 (a, b and c each; united and diverse both), 79 (citizenship
   with made-up people; the problem beyond the town), 92 (employment words, prices, values-based choice, bank,
   saving reasons compared; days 87 and 88 now compare).
2. Cesar Chavez as the good-leader exemplar: **applied**: Dolores Huerta replaces him on day 24 (frame unit 3 row and
   sensitivity bullet, scope and sequence). The expert read only swapped the order. Decided for Codex: the swap costs
   no day, standard or topic (the farm workers' movement stays), Huerta's organizing is documented by the National
   Park Service, and an exemplar under published 2026 allegations cannot be taught to six-year-olds as a plain "good
   leader". I could not verify the 2026 statements in this run; the change holds on its low cost either way.
   Progression note: structure pass.
3. Election versus issue vote: **applied with one change**. Day 32 compares talk-to-agreement with a vote; day 33
   keeps the election definition; day 34 elects a leader for a pretend class job; day 39 chooses a fair way for a
   given situation; day 73 (was 75) is a "secret-ballot vote"; frame rows match. Not applied: Codex's "elect a
   willing class member". The candidates are two made-up people, so no six-year-old loses a public vote; the
   leadership qualities are still weighed.
4. Four meetings in weeks 11, 21 and 31: **applied as wording; the referral to Cory not applied**. The 96 lessons and
   the week 31 check need 95 lessons in weeks 1 to 31, so three weeks carry four. The scope and sequence and frame now
   say so exactly. It is not sent to Cory: the frame's own total and "about three lessons a week" stand, nothing about
   audience changes, and three extra 30-minute lessons a year are a calendar detail.

For the lead: item 1 applied (frame wording); item 2 kept as written, and the expert agrees.

Settled call 3: check 1 (after unit 4) asks its ballot item about unit 1's garden team (day 42); check 2 (after unit 8)
asks its choice-and-cost item about unit 7's class decision (day 95).

## Grade 2 (social-studies-grade-2)

Expert read:
1. End-of-unit tasks miss parts: **applied** (with Codex 1 and call 4): days 15, 28, 44, 56, 70, 80, 92, and the
   course-level days 46 and 95. D2.Geo.12 is recorded from observation of days 33 to 36, with no written disaster item.
2. Day 61 carries two forced moves: **applied**. Day 61 keeps Cherokee removal and the nations today; day 62 opens
   with refugees fleeing war today (codes add D2.His.14.K-2 and MA.2.T3.1; the sensitivity note moves with it).
3. Check 1 repeats unit 3's claim: **applied**. Day 46's claim is about where to live in a unit 2 region and how to
   live with its land (keeps MA.2.T2.4, on earlier content); frame checks table.
4. Units 4 and 6 in no course-level check: **applied**. Day 95 adds a product label and a newcomer memory.
5. Angel Island length: **applied**. Day 66; frame unit 5 row; scope and sequence sensitivity line.
6. Unit 1 question: **applied** (expert's wording, see Codex 4). Days 1, 11, 14, 15; frame Units table; scope and
   sequence unit 1.
7. Stale lines: **applied**. Frame Days bullet (retrieval, 31 weeks); later.csv L8: structure pass.

Codex read:
1. Assessment evidence: **applied** (see expert 1): day 15 origin and the people-and-land map; day 28 all continents
   and oceans, vegetation, effect on people, observation of days 17 to 27; day 44 costs, tools and skills, near and
   far, settlement; day 56 trade both ways and day 55 scored; day 70 nation of immigrants, past and present, goods and
   ideas recorded in units 4 and 6; day 80 a student question and culture elements; day 92 source choices of days 84
   to 87 and the tie to the big question.
2. Three untaught requirements: **applied**. Day 40 adds services made here and elsewhere (D2.Eco.4); day 30 explains
   settlement by a river and by a landform (MA.2.T2.4's clarification); days 90 to 92 add a digital version made with
   an adult on the shared device, paper path kept. Codex sent the device question to Cory; **not sent**: Cory's
   standing call already allows one shared classroom device in K to 2 with a paper path. Progression notes and the
   standard description: structure pass.
3. Writing bridge ends too early: **applied**. Scope and sequence "The writing bridge" paragraph; notes on days 27,
   28, 43, 44, 46, 55, 56, 69.
4. Unit 1 question: **applied with the expert's wording** ("Which map shows the world best, and best for what?") over
   Codex's ("Which map would we choose to answer a question about our world, and why?"): both open the question;
   the expert's is shorter for seven-year-olds and names purpose, which days 9 to 11 teach. Codex's point that the old
   question stays as a supporting question: applied.
5. Candidate claims overstated: **applied**. Day 37 (Tennessee 2.04 informs, survey not adopted), day 39 (California
   2.4.1 present-day only, with the reason), days 77 and 78 (two cultural examples compared, one shared goal; Tennessee
   2.01 and 2.02 inform); frame unit 3 and 6 rows; scope and sequence.
6. Shorter path: **applied**. "The 30-minute core path" paragraph.
7. Stale frame wording: **applied**. Days bullet; the opening line now points to the scope and sequence and days.csv;
   the scope and sequence's For the lead item 1 closed.

For the lead: item 1 applied; item 2 kept, now lighter (check 1's claim moved to unit 2 content).

Settled call 3: check 1 (after unit 3) uses a unit 2 region for its living-with-the-land claim (day 46); check 2
(after unit 7) takes its source-and-claim items from a place in units 2 to 6, not a menu country (day 95).

## Settled

| Choice | Reason | File |
|---|---|---|
| K day 45: stripes from the 1777 flag law, a star per state since 1818, fifty today | The record behind the "record says" sort | data/plans/social-studies-kindergarten/days.csv; frame.md |
| K observation and check days ask every part of every listed code (days 9, 18, 29, 31, 32, 39, 50, 60, 62, 63) | Settled call 4; both reads | K days.csv; scope-and-sequence.md |
| K time words split: day 34 the school day's words, day 35 the rest | Kindergarten word load | K days.csv |
| K day 44: four holidays in full, Independence Day and Memorial Day as picture cards | Lesson load (two, not three, remain) | K days.csv |
| K day 5 models "I think we need this rule, because ..." | A practice meeting before the observation | K days.csv |
| K day 42 in the Veterans Day week, Thanksgiving met as coming soon; holiday school days are positions a school moves to its local week | The two dates never share a week; positions are not dates | K days.csv; frame.md; scope-and-sequence.md |
| K day 1 and day 9: why the question matters to the child | D1.1 in full | K days.csv |
| K day 53 and 60: a worker's knowledge, skills and tools | D2.Eco.3 in full | K days.csv |
| K day 14 takes the action's first step; day 17 a before-and-after chart | The action is done, not only planned | K days.csv |
| K 20-minute route over the same 64 lessons | Shorter path, nothing assessed cut | K scope-and-sequence.md |
| K checks: items for units 3 and 6 use units 1, 2 and 4 content | Settled call 3 | K days.csv days 32, 63 |
| K frame: 30 teaching weeks; cross-subject intro current | Stale lines | K frame.md |
| G1 unit 7 reordered: action day 74, look back day 78 | Six school days for the action to show | data/plans/social-studies-grade-1/days.csv; scope-and-sequence.md |
| G1 day 24 Dolores Huerta, day 25 Wilma Mankiller | Exemplar fit for "a good leader" and time order | G1 days.csv; frame.md; scope-and-sequence.md |
| G1 observation and check days ask every part (days 9, 18, 30, 40, 42, 54, 67, 79, 92, 94, 95) | Settled call 4; both reads | G1 days.csv |
| G1 D4.1.K-2 (review) on the claim days 28, 29, 38, 39, 42, 43, 53, 78, 91, 95, 96 | The code matches the argument skill | G1 days.csv |
| G1 day 32 compares agreement and voting; day 34 elects a leader for a pretend job from two made-up candidates; day 73 is a secret-ballot vote | An election chooses a leader; no child loses a public vote | G1 days.csv; frame.md |
| G1 days 87 and 88 compare (two shops, two saving reasons) | MA.1.T4.8 and T4.9 verbs | G1 days.csv |
| G1 check 2 adds unit 7 (a town's problem, a class's help) | Year-end record covers unit 7 | G1 days.csv day 95; frame.md |
| G1 checks: items for units 4 and 8 use unit 1's garden team and unit 7's decision | Settled call 3 | G1 days.csv days 42, 95 |
| G1 schedule wording: three a week, four in weeks 11, 21, 31 | The 96 days and the week 31 check need it | G1 scope-and-sequence.md; frame.md |
| G1 frame Days bullet: retrieval task | Settled call 1 | G1 frame.md |
| G2 end-of-unit and check days ask every part (days 15, 28, 44, 46, 56, 70, 80, 92, 95) | Settled call 4; both reads | data/plans/social-studies-grade-2/days.csv |
| G2 refugees today move from day 61 to day 62 | One forced move a lesson for seven-year-olds | G2 days.csv |
| G2 check 1 claim on a unit 2 region; check 2 on a place from units 2 to 6, with a product label and a newcomer memory | Settled call 3; units 4 and 6 reach the record | G2 days.csv days 46, 95; frame.md |
| G2 Angel Island: weeks, months, for some up to two years | The plain record | G2 days.csv day 66; frame.md |
| G2 unit 1 question "Which map shows the world best, and best for what?" | More than one defensible answer | G2 days.csv; frame.md; scope-and-sequence.md |
| G2 day 40 services, day 30 settlement reasons, days 90 to 92 digital version on the shared device | D2.Eco.4, MA.2.T2.4, D4.3 in full; standing device call | G2 days.csv |
| G2 writing bridge until a child shows the claim without it | ELA's W.2.1 comes at week 24 | G2 scope-and-sequence.md; days.csv notes |
| G2 candidate wording: Tennessee 2.01, 2.02, 2.04 and California 2.4.1 "inform", not "met" | No false coverage claim | G2 days.csv; frame.md; scope-and-sequence.md |
| G2 30-minute core path | Shorter path, nothing owned cut | G2 scope-and-sequence.md |
| G2 frame: retrieval task, 31 weeks, opening points to the days | Stale lines | G2 frame.md |

## For the structure pass

1. scripts/frame.py, `calendar_rows`: read `school_day` from data/plans/<course>/days.csv where filled, and emit a
   unit's days as separate segments where they are not contiguous (kindergarten unit 5's days 41 to 43 sit in weeks
   7, 12 and 19); then `python -X utf8 scripts/frame.py sync` to regenerate data/plans/calendar.csv. (Settled call 2.)
2. data/progressions/social-studies.csv, line 17 (ssk-work), notes: old "and the skills and tools each job needs."
   new "and the knowledge, skills and tools each job needs."
3. data/progressions/social-studies.csv, line 23 (ss1-leaders), notes: old "(a principal, a crossing guard, Harriet
   Tubman, Abraham Lincoln, Wilma Mankiller, the first woman to be Principal Chief of the Cherokee Nation, Cesar
   Chavez)" new "(a principal, a crossing guard, Harriet Tubman, Abraham Lincoln, Dolores Huerta, Wilma Mankiller,
   the first woman to be Principal Chief of the Cherokee Nation)".
4. data/progressions/social-studies.csv, line 41 (ss1-community-problems), notes: old "decides it by the
   secret-ballot class election (ss1-voting)" new "decides it by a secret-ballot vote (ss1-voting)".
5. data/progressions/social-studies.csv, line 24 (ss1-voting), notes: old "Hold a class election with secret
   ballots, tally the votes and read the result." new "Hold a secret-ballot class election of a leader for a pretend
   class job, from made-up candidates, tally the votes and read the result; tell an election from a vote on a matter,
   and compare voting with talking to agreement."
6. data/progressions/social-studies.csv, line 47 (ss2-people-environment), notes: old "How people use and change
   their environment (farming terraces, dams, cities by rivers)" new "How people use and change their environment
   (farming terraces, dams, cities by rivers), and why people settle near particular bodies of water and landforms".
7. data/progressions/social-studies.csv, line 57 (ss2-resources-industries), notes: old "goods made in our community
   and goods made in other places;" new "goods and services made in our community and in other places;".
8. data/standards/ma-hss-2018.txt, MA.2.T2.4: old "Explain and describe how people interact with the physical
   environment." new "Explain and describe how people interact with the physical environment, including why people
   settle near particular bodies of water and landforms." and add MA.2.T2.4 to the line 7 note's list of widened
   codes.
9. data/plans/later.csv, L8, detail: append " Grade 2 answered 2026-11-14: its scope and sequence names each unit's
   topics taught in full and where the freed days went (docs/courses/social-studies-grade-2/scope-and-sequence.md,
   \"A full year\")."
10. Optional (expert, grade 1 read, judged items): docs/ADOPTION-BAR-SUBJECTS.md C8 or docs/courses/UNIT-PLAN.md: one
    line that in K to 2, where no unit holds a readiness check, the retrieval task's teacher notes stand as the
    before-teaching evidence when the unit plan says so.

## For Cory

None. The two items the Codex reads sent to Cory are settled here: the grade 1 four-meeting weeks are a calendar
detail inside the frame's total, and the grade 2 digital presentation is covered by the standing call that K to 2 may
assume one shared classroom device with a paper path.

## Gates

`python -X utf8 scripts/sequence.py check` and `python -X utf8 scripts/frame.py check` for each of the three courses:
0 failures. `python -X utf8 scripts/plan.py check`: exit 0, no failures. `python -X utf8 scripts/frame.py calendar`:
check weeks K 15 and 30, grade 1 14 and 31, grade 2 14 and 31 (unchanged), no stagger break. `scripts/stale.py check`:
0 failures.
