# Scope and sequence: Computer Science, Grade 6

Course `computer-science-grade-6` (catalog id `cs-k12`), grade 6, draft, written 2026-11-26 from the frame
(docs/courses/computer-science-grade-6/frame.md). The days live in data/plans/computer-science-grade-6/days.csv; this
page holds the judgment.

## The year on one page

- **Shape.** 64 course days, two 45-minute sessions a week over 32 weeks: unit 1 days 1 to 15, unit 2 days 16 to 26,
  unit 3 days 27 to 36, the mid-year check days 37 and 38 with respond day 39, unit 4 days 40 to 46, unit 5 days 47 to
  53, unit 6 days 54 to 61, the year-end check days 62 and 63 with respond day 64. Units and their day counts are the
  frame's (15, 11, 10, 7, 7, 8); nothing was resized.
- **School days.** `school_day` is filled on every row by the frame's spread with the lead's pin: course day n falls
  on school day ceil(2.5 n), with day 38 pinned to school day 89, so days 1 to 38 spread as ceil(n x 89 / 38) and days
  39 to 64 as 89 + ceil((n - 38) x 71 / 26) (scripts/frame.py school_day). Week = (school_day - 1) // 5 + 1. Checks
  land where the frame sets them: days 37 and 38 on school days 87 and 89 (week 18), respond day 39 on 92 (week 19);
  days 62 and 63 on 155 and 158 (weeks 31 and 32, week 32 the finals week), respond day 64 on 160.
- **Every session opens** with a three-minute retrieval trace or a predict task (APPROACH.md "How a day opens"); the
  `retrieves` column names what it brings back. Device sessions keep their last five minutes to save or print and shut
  devices, with cords behind the table; each device day's note names its paper path.
- **Trace, modify, make.** In every unit a construct is traced (Understanding) before it is modified (Fluency or a
  worked-then-modify Understanding day) and modified before it is made (Application): unit 1 days 1 to 4 trace, 3 and
  5 modify, 6 makes; procedures trace on 7, modify on 8, make on 9; the team program makes on 11 to 13 after day 10's
  plan. Pairs are assigned and switch driver and navigator at a stated time on every pair device day; the team days
  (11 to 13) run teams of four on one device, with driver, navigator, tester and recorder rotating every eight minutes
  (on paper the recorder writes and the same rotation holds). Day 49 (predict, then watch) is Understanding, since it
  makes nothing.
- **Kinds.** 30 Understanding, 3 Fluency, 17 Application, 8 Check, 6 Respond. The Fluency days (8, 18, 42) practice a
  pattern a named earlier day taught and write no draft; no other day is Fluency because every other teaching day
  either first-teaches or makes.
- **Devices and paper.** Every device day is written with its paper path in the note. The grade 6 side-by-side editor
  view, the table tool, the toy classifier, the toy network and the sensor loop do not exist yet (frame For the lead 5
  and 6); until they do, those days run on their paper path. MS-PRO-VD-16 and MS-PRO-PD-12 are met in full on paper;
  MS-DAT-DC-23, the viewing part of MS-DAT-DC-22, MS-ALG-ML-06 and the shared digital tool part of MS-PRO-PD-15 are
  marked "part met without a device" on that path, never "met".
- **Base text not loaded.** The partial base (the archived Year 7 Teach Computing Curriculum, 2023) is not yet in the
  source store (later.csv L149), so the days that adapt it are planned from the frame's Source map alone and stay
  provisional: days 1 to 9 (block-language programming parts I and II), days 31 to 33 (spreadsheets lessons 1 and 4)
  and days 47 to 49 (networks lessons 3 to 5). Their notes say so. Every other day is our own. No source-map.csv is
  written (For the lead 1).

### Readiness and retrieval (rule 2, counted by grade number)

Every earlier-grade row this course assumes was last used in grade 5 computer science, the year before, so each opens
as a retrieval task inside the day that first uses it, and the course has no readiness check (no row is two or more
grades back; no grade 6 row assumes a grade 4 row directly).

| Earlier row | Last used | Treatment | Day |
|---|---|---|---|
| g5-variables-use | grade 5 | retrieval | 1 (and 2 to 4) |
| g5-systematic-debug | grade 5 | retrieval | 5, 6, 12, 20, 22 |
| g5-remix-program | grade 5 | retrieval | 7 to 9 |
| g5-team-project | grade 5 | retrieval | 10, 11, 13 |
| g5-visual-algorithm | grade 5 | retrieval | 16 |
| g5-professionals | grade 5 | retrieval | 23 |
| g5-collect-tools | grade 5 | retrieval | 27, 28, 29 |
| g5-data-benefits-risks | grade 5 | retrieval | 30 |
| g5-variability | grade 5 | retrieval | 34 |
| g5-train-model | grade 5 | retrieval | 40 |
| g5-human-centered | grade 5 | retrieval | 43 |
| g5-network-parts | grade 5 | retrieval | 47 |
| g5-cia-triad | grade 5 | retrieval | 50 |
| g5-hardware-software | grade 5 | retrieval | 54, 56 |
| g5-who-included | grade 5 | retrieval | 58 |
| g5-use-or-not | grade 5 | retrieval | 60 |

Later units also retrieve this year's earlier units (the `retrieves` column): unit 2 brings back procedures and
variables, unit 3 reads its tool steps as unit 2's algorithms, unit 4 reads the training set as a unit 3 table, unit 5
reads a packet header as unit 3's metadata, and unit 6 brings back design principles, the triangle and unit 1's
choice.

### Leans on the calendar (rule 5)

- **Math, variables (g6-variable-types, g6-model-algorithm).** Math grade 6 unit 6 (expressions with variables) runs
  in weeks 20 to 24, after units 1 and 2 (weeks 1 to 13). Days 1 to 6 and 16 to 19 carry the frame's bridge in their
  notes: the variable is a named box, its math meaning named beside it, and no task writes, simplifies or solves an
  expression.
- **Math, summaries (g6-sort-filter-tool).** Days 31 to 33 fall on school days 73 to 78 (weeks 15 and 16), before
  math grade 6 unit 8 (weeks 29 to 32). Days 32 and 33 carry the bridge: the average as the total shared out evenly,
  with median, spread and the mean as a measure of center left to math.
- **Science, digital signals (g6-packets).** Days 47 to 49 fall on school days 114 to 120 (weeks 23 and 24); science
  grade 6 unit 5 starts on school day 116, so day 47 comes just before it and day 49 just after. Day 47 carries the
  frame's either-order bridge: the code card does the encoding, and the link to science is named in one line only if
  science has started.

## Unit 1. Programs with memory

Days 1 to 15, weeks 1 to 8 (school days 3 to 36). The arc goes from being the computer on a paper program (day 1)
through the side-by-side editor (day 2), changing and combining values of three types (day 3), the choice and the
count-controlled repeat traced in the text view (day 4) and the running-total, maximum, minimum and counting patterns
on the rain-gauge anchor (day 5), to a pair make on a brief (day 6). Procedures follow the same trace (day 7), modify
(day 8), make (day 9) order, because a procedure reuses lines students can already trace. The team program comes last
because it needs variables, a choice, a repeat and a procedure together: plan and agreement on day 10, draft on 11,
written feedback from another team on 12, revision with the reflection on 13. The base lessons are kept in order except
that the choice (base lesson 3) is traced after the operators (lesson 4), as the frame's Source map sets.

- **Readiness:** none (all rows retrieval, above).
- **End-of-unit assessment, day 14:** unseen trace, predict, running-total, type-error and procedure-rewrite items
  (the procedure named, with one way the new version is clearer or easier to reuse) and a short build or debug task (paper version) for MS-PRO-VD-16 and MS-PRO-PD-12; MS-PRO-PD-15 scored from the
  day 13 revised team program and reflection against the rubric; its shared digital tool part is part met without a
  device until the grade 6 editor view exists. Response time: respond day 15.
- **Candidate:** kept, the base operators lesson as the comparing and joining steps inside day 3, zero added days.

## Unit 2. Models of an algorithm

Days 16 to 26, weeks 8 to 13 (school days 38 to 61). The flowchart comes first (day 16) because it calls a named
procedure from unit 1, and pseudocode is built from it line by line (day 17); a fix between two disagreeing models
(day 18, Fluency) precedes modeling a new algorithm alone (day 19). Verifying follows modeling because a test-table is
filled against a model: choose inputs (day 20), run given programs on them (day 21), find the input that exposes a
hidden fault (day 22). Careers comes last (days 23 and 24) because g6-careers-ct writes pseudocode lines.

- **End-of-unit assessment, day 25:** an unseen algorithm modeled both ways (MS-ALG-PS-02), a test-table for another
  unseen algorithm with an accuracy judgment (MS-ALG-PS-03), two computational thinking moves in a new worker case
  (MS-SOC-CE-44). Response time: respond day 26.
- **Candidate:** kept, the sorting and shape examples on day 21 as the boundary's own kinds of algorithm, zero added
  days.

## Unit 3. Data with care

Days 27 to 36, weeks 13 to 17 (school days 64 to 85), then the mid-year check in week 18. Precision and granularity
(day 27, with what each does to accuracy, storage and the questions a log can answer) come before metadata (days 28 and 29) because the anchor logs differ in both, and the metadata a device adds
without asking (day 29) leads to the first look at records about people (day 30, MS-DAT-IM-28 begun, not claimed).
The table tool runs worked (day 31), worked then modify with the summaries and the average bridge (day 32), then make
(day 33, which also applies DC-21 and DC-22: a fourth question the table's granularity or missing header cannot
answer, and which recording or metadata would answer it at what storage cost). Messy data closes the unit: problems and causes (day 34), options and what each does, including leaving a
group out (day 35), two options tried and compared (day 36).

- **End-of-unit assessment:** lesson one of the mid-year course-level check (day 37) scores the unit in full, as the
  frame sets: the check on the day right after the unit's last day stands for its end-of-unit assessment. Day 36's
  comparison sheet is collected for respond day 39, not scored. Response time: day 39, once.
- **Sensitivity:** day 30 uses invented profile cards and carries health's "If a student tells you something" steps;
  day 29 uses a supplied photo, never a student's.
- **Candidate:** kept, the base data-master lesson's summary functions as day 32's summaries, zero added days.

## Unit 4. Learning machines and who they serve

Days 40 to 46, weeks 19 to 23 (school days 95 to 111). A hidden-rule card sort (day 40) teaches hypothesis and test
before any machine, so day 41's classifier is read with a habit already in hand; day 42 practices the test-and-revise
loop on new chosen examples. The design checklist (day 43) then turns the sorter's failures into evidence for the
audit (day 44).

- **End-of-unit assessment, day 45:** a hypothesis tested on an unseen classifier (MS-ALG-ML-06; sealed card set on
  paper, part met without a device) and two principles marked on unseen screens with the user most affected
  (MS-ALG-IM-09). Response time: respond day 46.
- **Sensitivity:** days 43 and 44 (disability and language, home internet) carry the frame's guard; no faces, voices
  or people's pictures go into the classifier. Swap or leave out: a school may leave this unit out (frame), and then
  claims neither id that year.
- **If unit 4 is left out:** day 63's two unit 4 items become a ten-line trace (MS-PRO-VD-16) and a sort-and-summarize
  item on a printed table (MS-DAT-DC-23); days 40 to 46 stay in the calendar for the school's own use, so units 5 and
  6 and the pinned checks do not move.
- **Candidate:** kept, a second sorter with few examples of one kind as an extension on day 42, zero added days.

## Unit 5. Packets and protection

Days 47 to 53, weeks 23 to 26 (school days 114 to 130). The packet game (day 47) makes the message, packets, headers
and rebuild physical; loss and resend follow on the same game (day 48), then the toy network shows the same trip with
predictions checked (day 49). The triangle sort (day 50, MS-SYS-SE-32 begun, not claimed) comes after packets because
a lost packet is an availability case, which the make on day 51 joins.

- **End-of-unit assessment, day 52:** an unseen scenario modeled from send to rebuild, with a loss's cause and a way
  to lessen it (MS-SYS-NT-34); the triangle sort is practice, not scored. Response time: respond day 53.
- **Safety:** days 47 and 48 carry the frame's walking-route lines.
- **Candidate:** kept, the base performance lesson as day 48's loss causes, zero added days.

## Unit 6. Systems, history and choices

Days 54 to 61, weeks 27 to 31 (school days 133 to 152), then the year-end check in weeks 31 and 32. Each of the four
rows gets an Understanding day and an Application day: systems compared (54, with one societal, one environmental and one ethical impact; 55,
naming impacts of two different kinds by kind), industry devices (56, 57), eras
(58, 59), decisions (60, 61). Systems come first because the system-diagram from grade 5 carries both system rows;
history follows the devices so the eras read as changes in the same parts; decisions close the year because they draw
on units 3, 4 and 5 (data, design, the triangle).

- **End-of-unit assessment:** lesson one of the year-end course-level check (day 62) scores the unit in full, as the
  frame sets: the check on the day right after the unit's last day stands for its end-of-unit assessment. Day 61's
  written claim is collected for respond day 64, not scored. Response time: day 64, once.
- **Sensitivity:** days 58 and 59 (Dorothy Vaughan and the segregation she worked under, named as a sourced fact);
  days 60 and 61 (sharing a private photo) carry health's steps. Companies are never named.
- **Candidate:** dropped, a visit by a local worker who uses an industry device: the cards carry the row and a visit
  needs a school's own arrangement, zero days.

## Course-level checks

- **Mid-year, days 37 and 38 (school days 87 and 89, week 18; respond day 39, school day 92, week 19).** Lesson one
  scores unit 3 in full with unseen items (MS-DAT-DC-21 to 24, the DC-21 item asking for one effect on accuracy beside
  the storage cost and the question answered; about 6, 6, 16 and 12 minutes, the DC-23 table at most 15 rows) and
  stands for its end-of-unit assessment. Lesson two
  samples units 1 and 2 with five short new items (MS-PRO-VD-16, MS-PRO-PD-12, MS-ALG-PS-02, MS-ALG-PS-03,
  MS-SOC-CE-44), drawn as new items, not the unit 1 and 2 end-of-unit forms (both given more than four weeks earlier).
  Off every core check day (science's day 90 is the next school day).
- **Year-end, days 62 and 63 (school days 155 and 158, weeks 31 and 32; respond day 64, school day 160).** Lesson one
  scores unit 6 in full (MS-SYS-HW-30 with impacts of two different kinds named by kind, MS-SYS-HW-31,
  MS-SOC-HI-38, MS-SOC-HU-43; about 10 minutes an id). Lesson two samples units 1 to 5
  (MS-ALG-ML-06, MS-ALG-IM-09, MS-SYS-NT-34, MS-PRO-PD-12, MS-DAT-DC-24) with new items; the two procedure items
  (days 38 and 63) ask the student to name the procedure and say one way the rewrite is clearer or easier to reuse.
  Where unit 4 was left out, its two items are swapped as Unit 4 says.
- **Owned codes not sampled on a check day:** MS-PRO-PD-15 only. It is a team product over three sessions (draft,
  written feedback from another team, revision with reflection) that no 40-minute sitting can stand for; it is scored
  from the revised program on day 14 and carried into the year record.

## Shorter path

- **A shorter period (40 minutes).** The opening retrieval holds to three minutes, device days keep their five-minute
  shut-down, and the teaching block runs about 30 minutes; the exit ticket shrinks to one question. Check days keep
  their 40 minutes by starting at the bell with materials on desks.
- **A year about 10 days short.** Ten fold-in days, each folding into a neighbor, nothing assessed and no owned part
  cut. Each saves about 35 of its 45 minutes (about 10 move to the neighbor):
  - Day 2 (first editor session) folds into day 3's first 10 minutes: the worked program run there.
  - Day 4 (choice and repeat traced) folds into day 5: the anchor's choice and repeat are traced before it is modified.
  - Day 8 (procedure blanks) folds into day 9 as a blank-fill warm-up.
  - Day 18 (fix disagreeing models) folds into day 19's first task.
  - Day 21 (programs run on test inputs) folds into day 22 on the sealed answer sheet.
  - Day 24 (pseudocode for a worker case) folds into day 23's last 15 minutes as one shorter case.
  - Day 29 (photo properties) folds into day 28's last 10 minutes: pairs open the supplied photo's properties on a
    device (the printed panel only where there is none), so DC-22's device part is kept.
  - Day 36 (two options tried) folds into day 35 as one option tried on paper.
  - Day 49 (toy network) folds into day 48 as a teacher demonstration.
  - Day 57 (sensor loop) folds into day 56: the chosen device's function written on its card.
  Total: 10 days, about 350 minutes, leaving 54 of the frame's 64 course days; every check and respond day stays.

## For the lead

1. **No source-map.csv: waits on L149.** The base is not loaded (later.csv L149), so placements stay in this page and
   the frame's Source map; write source-map.csv when the archive is loaded and each lesson's file is read (lead call
   2, 2026-11-26).
