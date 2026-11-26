# Frame fixes: Health, grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

The one fix pass of COURSE-RUN stage 3 for the three health frames after K to 2, after the fresh expert read
(docs/reviews/frame-health-grades-3-to-12-2026-11-25.md) and the three second-model reads
(docs/reviews/frame-health-grades-{3-to-5,6-to-8,9-to-12}-codex-2026-11-25.md). Run beside the SEL 3 to 12 fix pass
(docs/reviews/frame-social-and-emotional-learning-grades-3-to-12-fixes-2026-11-25.md), so the shared cards were set
once for both subjects.

Files changed: docs/courses/health-grades-3-to-5/frame.md, docs/courses/health-grades-6-to-8/frame.md,
docs/courses/health-grades-9-to-12/frame.md, data/progressions/health.csv (14 notes cells; no row id moved or
renumbered, no hands_on or assumes cell touched), and data/plans/frames.csv, data/plans/calendar.csv and
docs/courses/CALENDAR.md through `frame.py sync`. No check week moved.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 117 courses; calendar.csv 2119 rows |
| `python -X utf8 scripts/frame.py check health-grades-3-to-5` | 0 failures; 21 units, 90 days (77 in units, 13 for checks and respond days) |
| `python -X utf8 scripts/frame.py check health-grades-6-to-8` | 0 failures; 30 units, 144 days (132 in units, 12 for checks and respond days) |
| `python -X utf8 scripts/frame.py check health-grades-9-to-12` | 0 failures; 21 units, 80 days (76 in units, 4 for checks and respond days) |
| `python -X utf8 scripts/progression.py check health` | 207 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |

## Findings

42 findings: 37 applied, 5 kept with a reason (J1, J3, J4, and the two row-cell halves of M3 and expert S3's PE side,
which are other files').

| Read | # | Finding | Applied or kept | What changed, or why not |
|---|---|---|---|---|
| Expert | S1 | I-statement breaks the one-card rule ("Please ___") | Applied | 3 to 5 and 6 to 8 use "I feel ___ when ___ because ___. I need ___." everywhere it is quoted (Course in brief, Reading level, Models carried, unit 4, Cross-subject). 3 to 5 Models carried says "because" is added to the K to 2 card. 9 to 12 Models carried adds "Does that work for you?" as SEL 9 to 12 does. "Please" stays only as an ask-for-help frame in unit 10 |
| Expert | S2 | "The three kinds" of activity are wrong | Applied | All three frames and the grade 3, 6 and 9 activity rows name aerobic, muscle-strengthening and bone-strengthening activity, with the CDC children's and adolescents' guideline wording (aerobic most of the hour; muscle and bone at least three days a week) |
| Expert | S3 | SEL and PE seams not written from the landed frames | Applied (health side) | Each frame's SEL and PE Cross-subject tables are rebuilt from those frames and data/plans/calendar.csv, with band unit numbers and school weeks. PE's own lines are other frames': Left for the lead |
| Expert | M1 | Refusal and listening cards ignore K to 2 and SEL | Applied | 3 to 5 takes SEL's refusal steps and the K to 2 listening card as retrieval, grown by one step; 6 to 8 and 9 to 12 Models carried name the SEL card each grows from |
| Expert | M2 | Stale lead notes and Cross-subject lines | Applied | "not written" and "when SEL and PE are written" lines are gone in all three; For the lead items rewritten as done or as lead items |
| Expert | M3 | Grade 5 dead ends treated differently at each end | Applied (frames); row cells to the lead | 3 to 5 moves g5-fn-claims-that-hurt and g5-s-online-safety from "threads that end" to Handed on; 6 to 8 keeps its two readiness checks (end of units 12 and 13). The hands_on and assumes cells in health.csv are the lead's (Left for the lead 1) |
| Expert | M4 | 9 to 12 unit 2 states a minority as the norm | Applied | Unit 2's figure (CDC YRBS 2025: 25 percent active every day) is the gap the unit explains; the Course in brief names units 11 and 12 as the norm days, with an optional third (a YRBS item where most do the safe thing) picked and dated at the unit plan |
| Expert | M5 | 6 to 8 unit 7 does not fence off sexual harassment | Applied | Unit 7 Out line and row g6-v-bullying-harassment-help: sexual harassment and unwanted touch are sensitive units 9 and 20; harassment here is non-sexual |
| Expert | M6 | Facts named but not checked at source | Applied | Each Sensitivity reads bullet: the unit planner names the exact page and date before the unit plan's expert read; a page that refuses an automated read is browser check |
| Expert | m1 | NHTSA back seat until 13 | Applied | 6 to 8 unit 12: "ride in the back seat until age 13 (NHTSA, year at the expert read; browser check)" |
| Expert | m2 | Naloxone wording | Applied | 9 to 12 unit 12: the nasal spray has been sold over the counter since 2023; what varies is state and school rules for students carrying it |
| Expert | m3 | SAMHSA toolkit with no year | Applied | 9 to 12 unit 21: 2012, with the expert read to confirm the latest edition or its successor |
| Expert | m4 | Day 36 respond day crowded by the goal slot | Applied | 9 to 12 goal slots on days 6, 11, 16, 21, 26, 31, 37, 41, 46 and 51; day 36 holds respond and the readiness check only |
| Expert | m5 | Spoken records one at a time | Applied | All three End-of-unit evidence bullets: two or three short pair stations the teacher moves between |
| Expert | J1 | 6 to 8 dose 48 | Kept | With Cory already; the read and this pass both pick keep 48 (For Cory 2) |
| Expert | J2 | Two-day sensitive units | Applied | Each Sensitivity reads bullet: a school that keeps a sensitive unit may add one practice day before its check |
| Expert | J3 | Puberty in two grade 4 lessons | Kept | Agreed with the frame's pick; the HECAT Sexual Health 3 to 5 read at the unit plan decides, and a third day would come from unit 11's slack |
| Expert | J4 | 9 to 12 goal thread | Kept | Cory accepted the shape; each unit plan of units 2 to 15 shows its slot day (the slot days above) |
| Codex 3-5 | 1 | Puberty reassurance about timing | Applied | Unit 14 and row g4-sh-body-changes take Codex's wording (wide variation, may already have begun, concerns taken privately to a trusted adult or health professional) and the teacher direction not to judge or reassure about an individual's timing. Earlier preparation is a Cory question |
| Codex 3-5 | 2 | Bullying definition omits the distinguishing feature | Applied | Unit 4 (where bullying is first taught): behavior that hurts or threatens, involves unequal power, and happens again or is likely to, told apart from ordinary conflict |
| Codex 3-5 | 3 | S4.5.2 and S1.5.4 judged without the evidence | Applied | Unit 4 adds the listening record (attend, ask, say back the meaning, two settings, text or AAC allowed); unit 9 adds an unseen condition case and the routine record carried into the judgment. The local S1.5.4 description is in data/standards/nhes-2024.txt, outside this pass: Left for the lead 2 |
| Codex 3-5 | 4 | Coordination notes describe absent frames and old SEL cards | Applied | As expert S1, S3 and M2; SEL unit numbers now run through the band (SEL 3 to 5 units 1 to 18) |
| Codex 3-5 | 5 | Grade 4 total one dollar short | Applied | Grade 4 $20; supplies ceiling figures corrected |
| Codex 6-8 | 1 | Bullying unit carries conflict steps without their limit | Applied | Unit 7: conflict steps never settle bullying; the federal bullying response page added to unit 7's source pack |
| Codex 6-8 | 2 | Written answers substitute for demonstrated skills | Applied | End-of-unit evidence names a doing record for each performance indicator, scored on steps |
| Codex 6-8 | 3 | Owned indicators narrowed by their tasks | Applied | Units 13 and 16 widen their tasks to the full indicator demand |
| Codex 6-8 | 4 | Nine-week route cannot hold the course | Applied | Days bullet takes Codex's sentence: the planned route is 48 sessions over 32 weeks; a daily nine-week route needs a separately specified 45-session short path, not labeled available until its table exists |
| Codex 6-8 | 5 | SEL bridge assumes an absent card and old unit numbers | Applied | SEL table rebuilt with SEL 6 to 8 band units and weeks; the calm card is SEL's "stop, breathe, name it, choose, go on" |
| Codex 6-8 | 6 | Readiness checks ignore grade 5 use | Applied | The two readiness checks name grade 5's earlier form (as expert M3) |
| Codex 6-8 | 7 | Assessment-day instructions conflict with the brief | Applied | Units 18 and 26 and the evidence bullet follow the after-core brief (no score on a first-taught day; checks on check days) |
| Codex 6-8 | 8 | Unmarked process statements and template text | Applied | Fluency line and Course-level checks rewritten; template wording removed |
| Codex 6-8 | 9 | Grade 6 printing overstated by two dollars | Applied | Grade 6 $30 |
| Codex 9-12 | 1 | Unit 20 carries negotiation into abuse scenarios | Applied | Unit 20 rewritten: the skill is telling a disagreement from abuse; no negotiation or I-statement with an abusive partner; the response route is leave, tell a trusted adult, call a hotline; Why and teacher note match; row g9-v-abuse-and-dating-violence matches |
| Codex 9-12 | 2 | Indicator tasks omit part of the demand | Applied | Units 2 and 13 name all five influence levels; S1.12.7 names benefits; S1.12.8 three prompts; units 4 and 6 add product and service-directory cards; row g9-phw-factors-and-behavior matches |
| Codex 9-12 | 3 | Doing records still let planning stand for performance | Applied | Unit 14: several distinct practices at stations, eating optional; unit 15: the adapted step enacted once in class. Rows g9-fn-habits-groups and g9-pa-habits-ease-adapt match |
| Codex 9-12 | 4 | Unit 20 names a removable unit as prerequisite | Applied | Unit 20 now follows only non-sensitive units 8 and 10, whose help and boundary steps it retrieves; unit 19 is not a prerequisite, and day 1 supplies the consent facts unit 20 needs whether or not unit 19 was taught |
| Codex 9-12 | 5 | Shared-course handoffs unresolved | Applied (health side) | PE and SEL Cross-subject tables rebuilt with units and weeks; the other frames' lines are Left for the lead 4 |
| Codex 9-12 | 6 | Week 8 goal slot crowds the respond day | Applied | As expert m4 |
| Codex 9-12 | 7 | Source-packet reading beyond the approach's support | Applied | Reading level bullet: packets hold short labeled excerpts or original summaries of two to four agency pages with source and date; the teacher reads them aloud or gives pictured and chunked versions, and the full pages stay as references, so source evaluation stays demanding under every access option |
| Codex 9-12 | 8 | Unit 2 activity gap as a majority norm | Applied | As expert M4 |
| Codex 9-12 | 9 | Semester-term instruction is stale | Applied | Days bullet: one semester of 16 weeks, the fall half (school weeks 1 to 16), with a spring school keeping the same order; units and weeks verified against calendar.csv |
| Codex 9-12 | 10 | Units table keeps older headings and an implicit year | Applied | Header `| # | Year | ... | Skill steps |` with 9 in every row; 3 to 5 and 6 to 8 headers also say Skill steps |

Where the reads disagreed: Codex 6-8 (5.3) kept "Please ___" as health's own request; the expert read and SEL
STANDARD section 7 set "I need ___", which this pass took, because one card serves K to 2 health, SEL and health.

### After-core check clashes (stagger rule)

Not moved, per the lead's instruction. They are listed in the expert read's "Stagger clashes" section, including the
6 to 8 day 84 clash with PE (J1).

## Pattern notes

- A shared card is quoted once, word for word, from SEL STANDARD section 7, and every other frame cites it rather
  than restating a variant.
- An abuse or harassment unit never carries the conflict steps; it says so in its Out line and teacher note.
- CDC activity types are named aerobic, muscle-strengthening and bone-strengthening, never "three kinds".
- A norm day states what most peers do; a figure that shows a healthy behavior is rare is the gap a unit explains.

## Left for the lead

1. health.csv cells: g5-fn-claims-that-hurt hands_on `g7-fn-judge-claims` and g5-s-online-safety hands_on
   `g7-s-online-boundaries`, each grade 7 row's assumes adding it (expert M3); grade 9 rows' cross_subject leans to
   SEL (SEL 9 to 12 For the lead 4); the word "stretch" in a grade 3 notes cell, which is an internal term.
2. data/standards/nhes-2024.txt: own-words descriptions for S1.5.4 (explain, including managing conditions), S1.12.7,
   S1.12.8 and S3.12.2 to S3.12.4 as the Codex reads give them.
3. PE 3 to 5: "three kinds" of activity in its own lines, to the CDC wording.
4. PE 6 to 8: its calm cue "stop, breathe, name it, pick a tool, go on" (lines 288, 305) becomes "choose"; one goal
   sheet with health; the day 84 clash. PE 9 to 12: line 317 "SEL 9 to 12 unit 2's goal steps" should be unit 6 (or
   unit 1); line 334 "unit 22's balanced week" (the balanced week is grade 9 unit 5); its docs/plans/calendar.csv
   path is data/plans/calendar.csv.
5. Career exploration 6 to 8: an obsolete Pending paragraph about health.
6. Browser checks: NHTSA child passenger and impaired driving pages (6 to 8 unit 12).
7. A Spanish translation brief for the family notes the frames now hold.
8. The calendar clashes above.

## For Cory

1. **Supplies ceilings (money).** Pick: 3 to 5 $30 a year for a class of 30; 6 to 8 $40 a year, with the bought
   helmet outside it; 9 to 12 $70 a semester, with the optional no-cook demonstration (about $45) outside it.
2. **6 to 8 dose (scope, already on the Desk).** Pick: keep 48 lessons a year.
3. **Earlier puberty preparation (scope, Codex 3-5).** Grade 4 unit 14 cannot promise teaching before changes begin.
   Pick: no new grade 3 content; a family note before grade 4 unit 14 and the private nurse or counselor route.
