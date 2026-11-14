# Baseline 1, part B: structure, all subjects (2026-11-14)

Reader: the curriculum expert (docs/agents/EXPERT.md), part B of docs/pipeline/briefs/baseline-1.md. Scope: the layers,
the gates, the words, each grade as a whole and the process into steps 3 and 4. Subject columns and the website are
other readers' parts and are left to them.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; the four lenses; docs/GLOSSARY.md; docs/PRODUCTION-PATH.md (section 3, steps 2 to
  6, existing work, after the core subjects, section 5); docs/pipeline/briefs/frame-write.md (format and its 15
  lessons), plan.md and plan-data.md (the unit plan briefs); docs/reviews/frame-cross-subject-2026-11-14.md in full,
  and a keyword sweep of the 2026-11-13 and 2026-11-14 frame and fix reports for repeats.
- scripts/frame.py, progression.py (docstring and note logic), stale.py (docstring), plan_flow.py (the course join),
  course_status.py output; data/courses.csv, data/plans/frames.csv, data/plans/flow-status.csv; data/plans/math-4/days.csv
  header; plan.py KINDS.
- `python -X utf8 scripts/plan.py check`: 0 failures. `progression.py check` per subject: 0 failures; notes math 96,
  science 177, social studies 191, ELA 1.
- **The 52 frames, sampled this way.** Every frame by script, every section: units tables (days, sizes), the Days bullet
  (minutes, weeks), the Course-level checks section (placed on a week calendar per grade), the Seams and Models carried
  sections against every row's assumes, hands_on, model_in and model_out, the Cross-subject sections against every
  same-grade lean in the four progressions, every cross-frame "unit N, days a to b" citation against the cited frame's
  units table, and a vocabulary count of 45 terms. By eye: the brief, Units and Cross-subject sections of grade 4 (all
  four subjects), grade 6 (all four), the K to 2 brief and checks sections, and the 6 to 12 social studies Days bullets.
  Scratch scripts (not in the repo): weeks.py, leans.py, seams.py, cites.py in the session scratchpad.

## Verdict

The layers line up: every owned row sits in one unit, every model and every assumed row is carried, every same-grade
lean is named, and the 68 cross-frame day citations agree with the frames they cite. The biggest risk is that step 3
starts with social studies, whose 15 frames were written before the lessons that the later 37 frames follow: they set
no end-of-unit assessment in K to 5, no minutes in grades 6 to 12, and check-set cells as commitments, and step 3 has
no brief, file location or day kinds of its own. The one change that matters most: before step 3, write the scope and
sequence brief with the unit rules this report names (an assessment inside every unit, a stagger rule for each grade's
checks, one school calendar) and sweep the social studies frames to the lessons.

## Findings

### 1. Fifteen frames set no end-of-unit assessment, and social studies goes first

LAYER frame, process. REPEAT yes for one course (the social studies grade 3 Codex read: "unit assessments and
responses must fit inside the existing unit allocations"); new as a structure gap.

- **Files.** No end-of-unit assessment named: social-studies-kindergarten to -grade-5 (6), science-kindergarten to
  -grade-2 (3), english-language-arts-kindergarten to -grade-5 (6). No readiness check named: 21 frames, among them
  social-studies-kindergarten, -grade-2, -grade-4, -grade-5, world-history-i and -ii, us-history-i and -ii, biology,
  ELA K, 2, 7 to 10, science K to 3 and 6, math-kindergarten.
- **What is wrong.** GLOSSARY defines a unit as "opened by a readiness check and closed by an end-of-unit assessment".
  The other 37 frames budget the assessment day inside each unit's days ("each unit's days include one end-of-unit
  assessment day"). These 15 are silent, so nobody can tell whether a K to 5 social studies unit of 6 to 32 days has an
  assessment day inside it or needs one more.
- **Why it matters.** Step 3 is social studies' scope and sequence. Its writer sets every day; if a day is added per
  unit, grade 5 social studies (10 units, 152 unit days) goes over 160; if none is set, the record sheet, the respond
  day and the unit plan's end items have no day. ELA K to 5 keeps the base text's unit assessments mid-unit (source
  maps: "the essay and its assessment kept"), so its units do have assessments, just not where the glossary says.
- **Fix.** A rule in the step 3 brief and in GLOSSARY's unit row: "Every unit closes with an end-of-unit assessment
  inside its days (in K to 2, an observation task spread over the unit's last lessons may stand for it); a unit
  longer than 25 days also holds a mid-unit assessment inside its days. A unit opens with a readiness check where it
  assumes an earlier grade's row." Then one line per affected frame's Days bullet: "Each unit's days include its
  end-of-unit assessment (and, in units over 25 days, its mid-unit assessments)". For ELA K to 5, the base text's
  three unit assessments per module are the mid-unit and end-of-unit assessments; name them so in the source map.

### 2. Step 3 has no brief, no file, no day kinds; step 4's brief and template are grade 4 math

LAYER process. REPEAT new.

- **Files.** docs/pipeline/briefs/ holds no scope and sequence brief. plan.md (the unit plan brief) reads
  `docs/courses/{course}-spine.md`, docs/courses/math-3-5-progression.md and docs/RUBRIC-MATH-K8.md and models on
  docs/courses/math-4/s03.md. scripts/plan.py line 23 `KINDS = {'Understanding', 'Fluency', 'Application', 'Check',
  'Respond'}`; GLOSSARY's "teaching day" row names the same three math kinds. GLOSSARY's scope and sequence row gives
  the file as `docs/courses/<course>-spine.md`, while every frame sits at `docs/courses/<slug>/frame.md`.
- **Why it matters.** Social studies' scope and sequence writers start next with nothing that says where the file
  goes, what a day row holds, what kinds an inquiry, source-work, discussion or writing day takes, or how the frame's
  "Check set adds" candidates are decided and costed in days.
- **Fix.** Before step 3: (a) docs/pipeline/briefs/sequence-write.md and sequence-read.md, written from frame-write.md
  and its lessons; (b) the file: `docs/courses/<slug>/scope-and-sequence.md`, with day rows in
  `data/plans/<slug>/days.csv` (GLOSSARY's lag cell then reads "Older files `docs/courses/<course>-spine.md`; new ones
  `docs/courses/<slug>/scope-and-sequence.md`"); (c) a ruling on day kinds: keep the five kinds for every subject and
  let the goal say the activity (my pick; it keeps plan.py and the site unchanged), and say so in GLOSSARY's teaching
  day row: "Understanding, fluency and application are used in every subject"; (d) the brief says the scope and sequence
  settles each "Candidate:" check-set addition and its day cost; (e) before step 4, a subject-neutral version of plan.md
  and a note in docs/courses/UNIT-PLAN.md on which fields are math only.

### 3. The social studies frames predate the lessons, and the gate holds none of the lessons

LAYER frame, gate. REPEAT yes (lessons 2, 3, 12 and 14 came from these frames' own reads).

- **Files and counts.** No minutes in the Days bullet: civics-government-and-civic-life, economics,
  us-government-and-politics, us-history-i, us-history-ii, world-geography-and-ancient-civilizations-i and -ii,
  world-history-i and -ii (all nine social studies 6 to 12; grade 8 says "the pick in For the lead is 45").
  "Check set adds" cells not marked Candidate: the same nine (every or nearly every unit) and social-studies-grade-3
  unit 1. No "paper path" line: all 15 social studies frames but world-geography-and-ancient-civilizations-i, plus
  science-kindergarten and -grade-1. No "Sensitivity reads" line: civics, economics, social-studies K, 1, 2,
  us-government-and-politics, us-history-ii, both world geography frames. (Several carry the content in other words.)
- **Why it matters.** These are the frames step 3 starts from; a check-set cell written as settled reads as a day the
  writer must find.
- **Fix.** A sweep of the 15 social studies frames before step 3: prefix every Check set adds cell with "Candidate:";
  add to each 6 to 12 Days bullet "One lesson of about 50 minutes a day, five a week, 32 weeks" (pick, see For Cory);
  add a "Paper path." and a "Sensitivity reads." bullet to The course in brief where missing. Then four FAIL rules in
  scripts/frame.py, each a few lines: the Days bullet (or a bullet labelled Time) contains `\d+[- ]minute`; every Check
  set adds cell starts "Candidate"; every course-level check row has at least one respond day; The course in brief has
  a bullet starting "**Sensitivity reads.**" and the text "paper path". Lessons 2, 3, 1, 12 and 14 then cannot come back.

### 4. Each grade's course-level checks stack in the same weeks

LAYER frame. REPEAT new for K to 8 (the high school writing-deadline clashes were found and fixed by the ELA 9 to 12
reads).

Weeks from each frame's units table and check table at its own lessons a week (grade 4 example: science check 3 week
29.5; math year review weeks 30 to 31, check 3 week 31.4; ELA check 2 week 31.4; social studies check 3 week 31.4).

| Grade | Mid-year checks (week) | Year-end checks (week) |
|---|---|---|
| K | science 14.5, ELA 15.4 (one-to-one), social studies 15.5, math 16.8 (one-to-one) | all four 31 to 31.6 |
| 1, 2 | ELA 15, math 18 to 19, science 17 to 20 | ELA, math 31.6; science 33 to 37 (its own weeks) |
| 3 to 5 | grade 4: math check 1 11.2 and social studies check 1 11.4, the same week | all four between 29.5 and 31.4 |
| 6, 7 | ELA 21.8, social studies 22.8 to 23.4, math 23.8 to 24 | all four 31.4 to 31.8 |
| 9 to 12 | spread | all four week 32 (a normal finals week) |

- **Why it matters.** In K to 5 one teacher gives and marks every check. Kindergarten's ELA and math checks are
  one-to-one for every child; four subjects' year-end checks in the last week and a half, each with respond days,
  leave the respond days nothing to act on and the teacher no time to hear every child.
- **Fix.** A rule in the step 3 brief (I settle it; see the table): "In K to 8, no school week holds course-level
  check days of two subjects of the same grade; in K to 2 the ELA and math one-to-one checks are at least a week
  apart. Year-end order: science and social studies in week 30, math in week 31, ELA in week 32; a check moves by
  shifting its respond days, never by moving a unit." The scope and sequence writers of each subject read the grade's
  other frames' check weeks from the calendar in finding 6.

### 5. The time a day, added across a grade

LAYER frame. REPEAT yes for each subject alone (the grade 3 social studies 40-minute block, ELA's 120 against 90 with
Cory); the sum across a grade is new.

| Grade | ELA | Math | Science | Social studies | Core minutes a week (a day) |
|---|---|---|---|---|---|
| K | 600 | 300 | about 60 | 40 to 60 | about 1,010 (200) |
| 1 | 600 | 300 | about 65 | about 90 | about 1,055 (210) |
| 2 | 600 | 300 | 70 to 80, some weeks 3 lessons | 90 to 120 | about 1,090 (220) |
| 3 to 5 | 450 | 300 | 180 | 200 | 1,130 (226) |
| 6 to 8 | 250 | 250 | 250 | not stated (pick 45 a day) | about 975 |

- **What is right.** The grade 2 to 3 seam is coherent: science and social studies double (about 190 to 380 minutes a
  week) and ELA's drop from 120 to 90 a day pays for it, so the core day stays near 220 minutes.
- **What is at risk.** ELA's open item (120 minutes in K to 2 against 90 in 3 to 5) cannot be decided by ELA alone:
  at 120 minutes in grades 3 to 5 the core day becomes 256 minutes, and the science and social studies budgets of
  grades 3 to 5 no longer fit. Grades 3 to 5 also assume about 76 minutes a day for science and social studies
  together, above what most elementary schools give (from memory: national survey reports put elementary science at
  roughly 20 to 25 minutes a day; I could not re-read them in this run). In grades 6 to 8, social studies' 45 against
  the other three's 50 implies two bell schedules.
- **Fix.** For Cory, as one question (below). Social studies 6 to 12 take 50 minutes, matching the other subjects
  (pick).

### 6. "School day" and "week" have no single definition, and day citations are copied by hand

LAYER gate, process. REPEAT new.

- **What is wrong.** 160-day courses count 32 weeks. Science K counts 32 weeks, grades 1 and 2 "about 34 of 36", grades
  3 to 5 "30 weeks of 36", yet the grade 5 Cross-subject section converts "science day n falls near school day 4n/3",
  which is 32 weeks. Course-level check tables come in five shapes (`Check | Falls after | What | Days` in 24 frames,
  `After unit | Weeks | Days | What` in 12, `After | What | Days` in 3, `After unit | Day range | ...` in 1, bullets in
  12), so no script can place a check. The 68 cross-frame citations of the form "math grade 5 unit 8 (about school days
  110 to 118)" all agree today within 3 days, but only because the cross-subject pass edited about 25 by hand; when
  social studies' scope and sequence sets real days in step 3, every math, science and ELA frame that cites a social
  studies day drifts.
- **Fix.** (a) GLOSSARY row: "**school day**, **week**: a position in the 160-day, 32-week teaching year (school day 1
  to 160, week 1 to 32); a course that meets fewer days a week spreads its days over the same 32 weeks". (b) frame-write
  rule: The course in brief states lessons a week; the Course-level checks section is one table `| Check | After unit |
  Check days | Respond days | What it checks |` (settled below). (c) `frame.py calendar` writes data/plans/calendar.csv
  (course, unit, first school day, last school day, check weeks) from the units and check tables; frame.py check FAILs a
  citation "<subject> grade g unit u ... days a to b" more than 3 school days off the calendar (the pattern I used
  parses all 68 citations). Step 3's scope and sequence then updates calendar.csv, and the gate names every frame to
  touch.

### 7. The progression gate's notes are noise

LAYER gate. REPEAT new.

- **What is wrong.** progression.py appends "skips N grade(s); say why in notes" and "named in grades ... (say in notes
  how the depth differs)" whether or not the notes already say it: 393 skip notes across math, science and social
  studies, of which 384 already carry a reason in either row's notes, and 46 C3 depth notes in social studies. A reader
  cannot find the 9 real ones.
- **Fix.** In progression.py (lines about 207 and 234), add the note only when neither row's notes contain the other
  row's skill_id or one of "skip", "idle", "dormant", "returns", and for a C3 code only when the later grade's notes do
  not contain the code. Same for "model ... unused in grade(s)".

### 8. "Standards in full" came back in every band and is not gated

LAYER gate. REPEAT yes (lesson 4; again in the ELA 6 to 8 fixes: W.7.1c, W.7.2c, W.8.2a to c, W.8.3c).

- **What is wrong.** frame.py checks owned codes, not their lettered parts. A rough scan (a part counts as named when
  its code appears) finds 265 of 771 lettered parts of owned codes not named by code in their frame; many are named in
  words only (world-history-ii names "the Thirty Years War ... after Westphalia" for MA.WHII.T1.1a without the code).
- **Fix.** A convention in frame-write.md and the step 3 brief: "a lettered part is named by its code in the What
  students learn cell of the unit that teaches it". Then a frame.py note (not a FAIL, until the sweep) listing each
  owned code's lettered parts from the standards files that the frame never names.

### 9. Course ids: the recommended fix

LAYER standard, gate. REPEAT yes (frame-cross-subject-2026-11-14.md, "Course ids").

I agree with the cross-subject report's four steps (keep both ids; a `catalog_id` column in data/plans/frames.csv
written by `frame.py sync` from COURSE_ROWS; one first-line form; retire `math-4` with the grade 4 scope and sequence)
and add four things it did not see:
- **plan_flow.py joins frames by `slug(title)`** of course_status.py's titles, a third key. It matches all 52 today; a
  title edit in course_status would silently drop a course back to the estimate (150 days, 16 units). Join on
  frames.csv's `catalog_id` and `grade` instead.
- **frames.csv also gets `subject`, `grade` and `title`**, so the flow, the site and later scripts read one table.
- **frame.py misses two cases:** a COURSE_ROWS slug with no frame (found() lists only frames on disk), and a frames.csv
  row with no frame (sync keeps every old row). FAIL both.
- **course_status.py still reports the old plans' totals** (math grade 4: 18 units, 150 days; ELA 6: 8, 150; science 4:
  9, 108) beside the frames' 9/160, 6/160, 6/120. The flow prefers frames.csv, but any other reader of course_status
  sees the old numbers; have it read frames.csv first.

### 10. One thing, several names

LAYER frame, process. REPEAT yes for the C3 column (cross-subject item 53); the rest new.

| Thing | Names in the frames (files) | Fix |
|---|---|---|
| The check across units, set in the frame | course-level check, course check (10), year check (13), mid-year check (13), end-of-year check (12), year-end check (4), cumulative check (4), year review (3) | GLOSSARY row: **course-level check** (mid-year, year-end as adjectives); do not call it course check, cumulative check, benchmark |
| The short look back before a unit | readiness check (31), readiness day (6), retrieval task (24), opening retrieval task (1) | GLOSSARY: readiness check is the item set; a **readiness day** is the day that holds it; a **retrieval task** is a short look back inside a day, not a check |
| What a unit adds beyond its codes | "Check set adds": three states' standards (social studies), the Progressions documents (math), practice and crosscutting elements (science), candidate texts (ELA) | Keep the column name for the gate; GLOSSARY row **check set**: "the sources a subject checks its units against beyond the anchor standard (social studies: California, Tennessee, New York and the college-level frameworks; math: the Progressions; science: the practice and crosscutting elements; ELA: candidate texts)" |
| A row's use of another subject's skill; what a unit does if it is not yet taught | lean (47 files), bridge, local bridge, if-later line | GLOSSARY rows **lean** (the cross_subject column) and **bridge** (the if-later line) |
| A check partway through a unit | mid-unit check (math 6 to 8), the base text's mid-unit assessments (ELA K to 5) | GLOSSARY: **mid-unit assessment** |
| An assessment day | "check day" (economics, us-government-and-politics, us-history-ii Days bullets) | "assessment day" |
| A daily warm-up | "grammar opener", "openers" (ELA 3, 4) | "grammar warm-up" (opener is a section's teacher page) |
| Stale numbers in GLOSSARY | unit row "3 to 15 in grade 4 math"; sub-ready day "18 a year in grade 4 math" | "5 to 42 days across the courses (grade 4 math: 8 to 22)"; "one per unit (9 a year in grade 4 math)" |

The Massachusetts "topics" (WHI.T1) and EL Education's "modules" are a standards document's and a base text's own
words; they may stay when quoted, as "domain" does in math.

### 11. Unit size runs from 5 to 42 days, and per-unit pieces follow the count

LAYER frame. REPEAT new.

- **What is wrong.** Median unit length: ELA 26 days (K to 5: four units of 32 to 42), math 19, science 16, social
  studies 13. The record sheet, family note and sub-ready day are one per unit (GLOSSARY), so a kindergarten family gets
  4 ELA notes a year against 8 in math, and an ELA K to 5 substitute has one sub-ready day per eight weeks.
- **Fix.** In ELA K to 5 the record sheet, family note and sub-ready day go per base unit (three per Curio Class unit,
  12 a year); the unit stays the base module (it carries the compelling question and the performance task). One line
  in each ELA K to 5 frame's brief and in GLOSSARY's sub-ready day row: "per unit, and in ELA K to 5 per base unit".

### 12. PRODUCTION-PATH's course count and the courses no step owns

LAYER process. REPEAT yes for the source-map location (cross-subject item 54); the rest new.

- **Files.** docs/PRODUCTION-PATH.md line 259 "The 58 courses of the four core subjects get one each" and line 301 "all
  58 courses of the four core subjects": 52 frames exist and the flow shows 52; the other 6 are electives
  (precalculus, statistics, calculus, earth and space, environmental science, psychology). "After the core subjects"
  counts only the 49 courses of other subjects. data/courses.csv marks personal-finance core (`y`, cte) and the flow
  draws it as a core course with no frame, while economics' frame carries personal finance.
- **Fix.** Line 259: "The 52 core courses of the four subjects get one each (the 6 electives in these subjects wait,
  see After the core subjects)." Line 301: "across all 52 core courses". "After the core subjects" adds: "the 6
  electives of the four core subjects (precalculus, statistics, calculus, earth and space science, environmental
  science, psychology)". Line 256 (source map) as the cross-subject report gives it: "the source map (a section of the
  frame; the day-level data/plans/<course>/source-map.csv comes with the scope and sequence)". Personal finance: For
  Cory.

## What is right and should not be touched

- Frames against progressions: every owned row in exactly one unit, every owned code listed, all 52 pass.
- Seams and models: every assumes row of every course is in its Seams tables, every model_in and model_out in Models
  carried (checked by script on all 52).
- Cross-subject: 364 of the 367 same-grade leans in the four progressions are named in the leaning frame's
  Cross-subject section (the other 3 are named elsewhere in the frame); sampled both ends in grade 6 (ELA research
  days 63 to 86 before social studies unit 8, days 100 to 113) and grade 4: consistent.
- The grade 12 timetable (Government fall, Economics spring, US History II all year) is Cory's and holds.
- The high school check weeks: one finals week is normal practice.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| One Course-level checks table: `| Check | After unit | Check days | Respond days | What it checks |` | One shape a script can place on the calendar | docs/pipeline/briefs/frame-write.md; the 28 frames in other shapes, at their next edit |
| Week stagger: K to 8, no week with two subjects' check days; year-end science and social studies week 30, math 31, ELA 32; K to 2 one-to-one checks a week apart | One teacher marks every check | Step 3 brief (finding 2) |
| Day kinds stay five in every subject | Keeps plan.py, days.csv and the site as they are | GLOSSARY teaching day row; step 3 brief |
| Scope and sequence file: docs/courses/<slug>/scope-and-sequence.md and data/plans/<slug>/days.csv | Beside the frame, one folder per course | GLOSSARY scope and sequence row |
| School day and week: positions in the 160-day, 32-week year | One calendar for every cross-subject citation | GLOSSARY; frame-write.md |
| Units over 25 days hold a mid-unit assessment | Matches the base texts (ELA K to 5, math 6 to 8) | GLOSSARY unit row; step 3 brief |
| GLOSSARY rows: course-level check, readiness day, retrieval task, check set, lean, bridge, mid-unit assessment; the two stale numbers | One name for one thing | docs/GLOSSARY.md |
| progression.py notes silenced when the reason is written | 384 of 393 notes already answered | scripts/progression.py |

## For Cory

1. **The elementary day, as one decision** (audience): ELA 120 minutes in K to 2 and 90 in 3 to 5 (ELA's open item), and
   science 180 plus social studies 200 minutes a week in grades 3 to 5, add to about 220 core minutes a day. Pick: keep
   the frames as they are; raising ELA 3 to 5 to 120 needs science and social studies 3 to 5 cut back to about 120
   minutes a week each.
2. **Minutes in social studies 6 to 12** (audience): pick 50, the other three subjects' period, so a school runs one bell
   schedule.
3. **Courses with no step** (scope): the 6 electives of the four core subjects and personal finance (marked core in
   data/courses.csv; economics already teaches personal finance). Pick: personal finance stays inside economics and its
   catalogue row turns to `n`; the electives come after the core subjects, with the 49.

## Sources

- The repo files above; scripts run on 2026-11-14. Elementary minutes a day: from memory (national surveys of science
  and social studies time in elementary schools), not re-read in this run.
