# Expert read: scope and sequence of Computer Science, Kindergarten (2026-11-26)

Course `computer-science-kindergarten`. Brief: docs/pipeline/briefs/sequence-read.md with {subject} = computer
science, as build/scope-writes/CS-READ.md sets it. Read cold; the reader did not write the scope.

## What I read

- docs/courses/computer-science-kindergarten/scope-and-sequence.md and data/plans/computer-science-kindergarten/days.csv
  (all 32 rows, every goal, note and `retrieves` cell), read in full.
- Beside them: the frame docs/courses/computer-science-kindergarten/frame.md in full; the 14 K rows of
  data/progressions/computer-science.csv; the 16 EK statements in data/standards/csta-2026-statements.txt (lines 98 to
  113); data/plans/calendar.csv for grade K (computer science and math kindergarten); docs/courses/CALENDAR.md rule 1;
  math kindergarten days 41 to 45 in data/plans/math-kindergarten/days.csv (the two leans).
- The bar: docs/ADOPTION-BAR-SUBJECTS.md "5. Computer science" (items 1 to 9, "Fails if", "Scope and sequence
  states"); docs/courses/computer-science/APPROACH.md in full; build/scope-writes/CS-BRIEF.md; the lens
  docs/agents/lenses/computer-science.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-write.md; the
  DESK-ANSWERS entry "2026-11-26: after-core frame calls".
- Gates run first: `scripts/sequence.py check computer-science-kindergarten` 0 failures; `scripts/plan.py check` no
  failure for this course; `scripts/frame.py calendar` places grade K computer science at weeks 12 and 27 (health
  shares both and library 27, all specials or not counted under CALENDAR.md rule 1, so no stagger break);
  `scripts/stale.py check` one failure in this course's frame (frame.md line 238, "until it is loaded" outside a
  Pending marker; the frame is the lead's, finding 7). I read scripts/sequence.py lines 327 to 336: the lead's fix
  (a `C` Check the day after a unit's last day stands for its end-of-unit assessment) is in.
- No outside source was opened for this read; the findings rest on the repo's own statements, rows and calendar.
- Not done: `plan.py defect` logging, because the brief allows no edit but this report. The caller may log them.

## Verdict

The scope is sound and close to ready: every unit, day count and owned row is the frame's, all 16 EK ids sit on
teaching days before they are scored, the two math leans are met before use (sorting in math week 9, positions in
week 9, against computer science weeks 10 and 15), the device days all have a paper path that meets the same ids,
and the shorter path cuts nothing assessed or owned. The biggest risk is the check items: five ids are scored by an
item that asks only part of the statement (PS-01, RD-06, HW-11, CE-16, and the collecting part of DI-09), so a
child can pass without showing what the id says. The one change that matters most is to rewrite those five items
as below; the retrieval spacing in unit 3 and the spoken-answer minutes on check days come next.

Findings: 7 (1 serious, 4 moderate, 2 minor).

## Findings, most serious first

### 1. Five check items ask only part of the id they score (serious)

LAYER sequence (and frame: the frame's Course-level checks table and unit 1, 3 and 5 end-of-unit lines set the same
items). REPEAT yes (the dance K to 2 read found check tasks asking only part of their codes).

- **What is wrong.**
  - EK-ALG-PS-01 (carry out algorithms in daily activities), day 12: "order a new routine's step-cards and name them
    an algorithm". Ordering cards is building a sequence, not carrying one out; no item has the child follow steps.
  - EK-PRO-RD-06 (describe how a sequence of commands completes a task), days 21 and 27: "circle the end square".
    That is the outcome, not how the steps get there; the describe verb is never asked. Day 17 teaches it as
    "First it ___, then it ___".
  - EK-SYS-HW-11 (examine the use of tools to accomplish a task for different users), day 5: "match new tool and job
    cards". The "for different users" part, which day 1 teaches (who a tool works for and who it does not), is not
    asked.
  - EK-SOC-CE-16 (devices at home, at school and at work), day 31: "point to the devices in a new place picture".
    One picture covers one of the three places.
  - EK-DAT-DI-09 (investigate a question answerable by collecting data), day 27: only the spoken "pose a question"
    is scored; the collecting part sits on day 26, which is unscored observation.
- **Why it matters.** sequence-write rule 2, "Each part of each code": a busy item writer at the unit plan will copy
  these lines, and a child who can order cards, circle an end square or spot one device is recorded as meeting ids
  whose verbs (carry out, describe, for different users, at home, school and work) were never seen.
- **Fix** (no day added; paper items replace or extend what is there, so no spoken minutes are added):
  - Day 12, PS-01: the child follows a new three-card picture algorithm on paper (for example: draw a circle, color
    it, draw a line under it) and the product shows the steps were carried out in order. The ordering item may stay
    as the "name it an algorithm" part.
  - Days 21 and 27, RD-06: a three-square strip under a three-card program; the child draws a dot where the robot is
    after each card, then circles the end square. Each dot is one step described, on paper, with no reading.
  - Day 5, HW-11: the match is a triple: a tool card, a job card and a person card (a magnifier, reading a
    book, a person who needs bigger print).
  - Day 31, CE-16: three small pictures (a home, a school, a workplace); the child circles one device in each; the
    spoken "one use" stays.
  - Day 27, DI-09: the note says the DC-08 item (placing pictured answer cards into a new graph mat's groups) also
    carries DI-09's collect part, beside the spoken question. No day 26 score is needed.
  The frame's Course-level checks table and unit lines name the old items; the lead mirrors these in the frame.

### 2. Spoken answers on check days do not fit the session (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** Each check day has about 20 minutes after the retrieval opener. Day 12 asks each of 30 children
  two spoken answers, one of them EK-ALG-IM-03 in three parts (chose the task, noticed its parts, ordered the
  steps); day 21 asks each child to arrange a route and say what the robot will do, plus three signs; day 27 asks
  each child to pose a question and say why. At five groups of six that is about 40 seconds a child for two answers,
  while 24 kindergarten children work a 15-minute paper task unsupervised. The scope plans the overflow ("heard in
  the first minutes of the respond day") only for the shorter period.
- **Why it matters.** The teacher will run out of time on the full-length day too, and the unheard children are
  either skipped or rushed, which hits the "describe" and "explain" ids hardest.
- **Fix.** In "Evidence" and on days 12, 21 and 27, state the budget for 30 children (about 4 minutes a group of
  six) and make the overflow the plan at every length: groups not reached are heard in the first 10 minutes of the
  respond day (13, 22, 28), still one sitting's evidence, collected once. On day 12 the IM-03 answer is prompted by
  three picture cards (choose, parts, order) the child points to and says one word about, so each part has its own
  prompt and the answer is short. Finding 1 keeps RD-06 on paper so day 21's spoken load does not grow.

### 3. Retrieval spacing: unit 3 retrieves itself, k-people-steps never returns, check days warm up what they score (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** APPROACH.md ("How a day opens") and section field 8 make the opener a trace of an earlier
  unit's construct. In unit 3, eight of nine days retrieve the day before in the same unit (15 to 22); units 1 and 2
  rows go unseen from week 14 to week 22. k-people-steps (EK-ALG-IM-03, EK-SOC-HU-15) is in no `retrieves` cell all
  year. Four check days open by retrieving a row they then score: day 5 (k-tools-jobs, HW-11), day 12
  (k-follow-steps, PS-01), day 21 (k-wrong-step, TR-07), day 27 (k-data-decide, IM-10), which turns three minutes of
  the sitting into a rehearsal of its own item.
- **Why it matters.** The spacing report (scripts/spacing.py) reads this column; a row taught once in week 9 and
  never retrieved is the row most likely to be lost by grade 1's g1-change-steps and g1-people-or-machine. And a
  warm-up on the scored row blurs the check.
- **Fix.** The swaps in "Settled by the expert": unit 3 days 16, 18, 20 and 21 retrieve unit 1 and 2 rows, day 12
  retrieves k-tools-jobs, day 27 k-symbols, and day 5 keeps k-tools-jobs as a spoken "what is this tool's job"
  with the day 1 mystery bag, not the card-match form it scores. Days 15, 17 and 19 keep the previous day's row,
  since each builds on it directly. Update the .md "Readiness and retrieval" list to match.

### 4. Children compose their own route before the predict day (moderate, a judgment call)

LAYER sequence (and frame, unit 3 session 2). REPEAT new.

- **What is wrong.** Day 15 traces a worked path, then "move a partner or a toy with arrow cards and lay the cards in
  order as a program"; read as a busy writer would, that is pairs inventing routes in the second session, before
  day 17's predict (RD-06), day 18's debug and day 19's modify. CS-READ asks for trace before modify before make on
  every programming row, and the lens marks "make" before "predict" as trouble.
- **Why it matters.** Pairs who make routes on day 15 meet wrong turns with no debugging method yet (day 18), and
  the predict day becomes review of something they have already done freely.
- **Fix.** Day 15's goal: "After a forward-and-back warm-up, trace a worked path on the floor grid, then in pairs
  lay and walk the cards for that path and for the same path one square longer, the navigator holding the cards and
  the driver moving." The first route of a child's own choosing is day 19 (a moved star) and day 20 (a new star).
  Item level, inside the unit; the lead mirrors the wording in the frame's session 2 line.

### 5. The `observe` marks on days 11 and 26 are now stale (moderate)

LAYER process. REPEAT new.

- **What is wrong.** Days 11 and 26 carry `assess` = `observe` only to pass the old gate (the scope's For the lead
  item 1); sequence.py now accepts the check on days 12 and 27 as each unit's end. `observe` means "an observation
  task standing for the end-of-unit assessment", which these days explicitly are not, and the lead asks for no end
  marks on teaching days.
- **Why it matters.** A unit plan writer reading `observe` will write an assessment task for a make day and a
  checklist record that nothing uses, and the skeleton counts it as the unit's end.
- **Fix.** Clear `assess` on days 11 and 26 and drop "Observation notes by exception ... not scored" to "Notes by
  exception on the class checklist" in their notes. In the .md, remove "Day 11 carries `assess` = `observe` for the
  gate" (unit 2) and the matching unit 4 sentence, and delete For the lead item 1. The gate passes without them
  (sequence.py line 332).

### 6. Flags the .md claims are missing from day notes (minor)

LAYER sequence. REPEAT yes (sensitivity and safety lines not carried to each day, seen in earlier reads).

- **What is wrong.** The .md lists sensitivity on days 1 and 3, 7 to 9, 23 to 27 and 29 to 31; days 3, 8, 25, 27
  and 31 carry no sensitivity line. The public-and-private cards come back on days 6, 12, 13, 27 and 28 with no
  online-safety flag or pointer to health's "If a student tells you something" steps (only day 4 has it). Day 14
  uses the floor grid but lacks the "Last four minutes" put-away line; days 21 and 22 lack the floor-grid lines the
  .md says run "on days 14 to 21", and day 21 does not say whether the route task is on the floor or a table mat.
  Days 17 and 18 end with a stray trailing space.
- **Why it matters.** CS-BRIEF and the frame's Safety bullet ask for the lines on each day; the sensitivity read and
  the section writer work day by day from the notes.
- **Fix.** Add the frame's sensitivity line to days 3, 8, 25, 27 and 31; add "Sensitivity: online safety and
  personal information; no real detail; health's steps on the teacher page" to days 5 (extend), 6, 12, 13, 27 and
  28; add the put-away line to day 14; on day 21 say "the route is laid on a table mat" (the settled choice, so no
  grid is needed during a sitting) and give day 22 the floor-grid lines for its reteach.

### 7. Smaller items for the lead (minor)

LAYER frame and process. REPEAT new.

- **Year-end sample (the scope's For the lead 4).** Agree with the writer: EK-PRO-PD-04 and EK-PRO-VD-05 reach no
  course-level check. Cheapest fix, on paper so no spoken minutes are added: a "glue three arrow cards to reach the
  star" item (PD-04) and a "circle what this sign tells us to do" item (VD-05) in day 27's paper task. A frame change
  (its check table), so the lead's.
- **Day 25's kind (For the lead 2).** Agree: first teaching of k-data-decide, so Understanding; the frame's Day kinds
  bullet should read "unit 4 session 4" only.
- **source-map.csv (For the lead 3).** Rule 8 wants it for a base-text course; the CS brief kept this job to two
  files and the base is not loaded (later.csv L149). The .md's "Sources not yet loaded" list matches the frame's
  Source map lesson by lesson, so the map can be written from it when the store folder exists.
- **Stale frame wording.** stale.py fails frame.md line 238 ("until it is loaded" outside a Pending marker).

## What is right and should not be touched

- Rules before the first device turn (day 2 before day 3), with the base's reorder named.
- Unit 3's arc after day 15: build in picture blocks, predict, find the first wrong step, modify, make, with pair
  roles switching on days 15 and 20 and "bug" taught with both meanings.
- school_day = 5n stated once, every unit and check in the frame's weeks, and the .md correctly explains why the
  checks after units 2 and 4 are the unit's own end and draw unseen items, while earlier units are sampled with new
  cards and no task form from the last two weeks.
- The math leans: checked against data/plans/calendar.csv and math kindergarten days 41, 42 and 45; both met
  before, bridges kept.
- The shorter path: two modify days folded into their make days as a 7-minute opener, the spare named, checks and
  only-teaching days never folded.

## Lens checklist, scope and sequence layer

| Lens line | Met? |
|---|---|
| All five concept areas taught, not programming alone | Met: systems (unit 1), algorithms (2), programming (3), data (4), society (2 and 5) |
| AI inside the concepts, not one late unit | Met at K depth: the sorting rule (EK-ALG-ML-02) in unit 2, with no claim that a machine thinks |
| Read before write, then modify, then make | Part met: finding 4 (day 15) |
| Unplugged teaches the idea, plugged tests it | Met: every unit unplugged; device days carry the screen parts only |
| Notional machine taught | Met at K depth: the teacher-robot, walk the cards, day 17 trace |
| Debugging as a method | Met: day 18 first wrong step, days 19 and 20 change one card, test again |
| Practices inside content | Met: CT, IC, HCD and ESR codes on the days the frame names |
| Society with evidence | Not applicable at K beyond pictures: no dated case is owed by an EK id |
| No id claimed by a day that only mentions it | Met, except the items in finding 1 |
| A tool with no named job, or one needing an install or account | Met: no tool needs either; the picture-block mode is queued (L148) and the paper path meets every id |
| Pair work with roles | Met on days 15 and 20; day 3 "pairs take turns" |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 12 PS-01 item: follow a new three-card picture algorithm on paper (draw, color, line) | "Carry out" needs a followed sequence, not an ordered one | days.csv day 12 note; .md checks table |
| Days 21 and 27 RD-06 item: draw the robot's square after each card on a three-square strip, then circle the end | The describe verb on paper, no added spoken time | days.csv days 21, 27; .md unit 3 and checks table |
| Day 5 HW-11 item: tool, job and person card triples | Carries "for different users" | days.csv day 5; .md unit 1 |
| Day 31 CE-16 item: three small pictures (home, school, workplace), one device circled in each | Carries all three places | days.csv day 31; .md unit 5 |
| Day 27 note: the DC-08 placement item also carries DI-09's collect part | DI-09 scored in full without a day 26 score | days.csv day 27 |
| Spoken overflow: about 4 minutes a group; unheard groups in the first 10 minutes of the respond day, at every length | 30 children do not fit 20 minutes | .md Evidence; days 12, 13, 21, 22, 27, 28 notes |
| Day 12 IM-03 answered by pointing to three picture prompts (choose, parts, order) with one word each | One prompt per part, short answers | days.csv day 12 |
| `retrieves`: day 5 k-tools-jobs as a spoken job guess with the mystery bag; day 12 k-tools-jobs; day 16 k-sort-attributes; day 18 k-people-steps; day 20 k-public-private; day 21 k-device-manners; day 27 k-symbols | Earlier units in unit 3, k-people-steps retrieved, no check warms up its own scored row | days.csv `retrieves` and notes; .md Readiness and retrieval |
| Day 15 goal: trace the worked path, then lay and walk it and the same path one square longer; first own route on day 19 | Trace before make | days.csv day 15; .md unit 3 |
| Clear `assess` on days 11 and 26; remove the .md's observe sentences and For the lead 1 | The gate fix is in; the marks mislead the unit plan | days.csv days 11, 26; .md units 2, 4, For the lead |
| Day 21 route laid on a table mat | No grid needed during a sitting; keeps the paper task and groups in one room layout | days.csv day 21 |
| Sensitivity, online-safety and floor-grid lines added as finding 6 lists | Each day carries its own flags | days.csv days 3, 5, 6, 8, 12, 13, 14, 22, 25, 27, 28, 31 |

## For Cory

Nothing. Every finding is item level or the lead's frame wording.

## What I could not judge

Whether the archived base lessons (later.csv L149) match the .md's lesson-to-day list in content, not only title;
that waits on the store folder. The real minutes of a kindergarten paper task of four items, which only a trial
would show.
