# Baseline 1, structure fixes (2026-11-14)

The expert, as structure fixer, applying the findings of docs/reviews/baseline-1-structure-2026-11-14.md and
docs/reviews/baseline-1-codex-2026-11-14.md that live outside the frames and progressions, and the findings of
docs/reviews/baseline-1-site-2026-11-14.md that need no yes from Cory. Four subject fixers edited the frames and
progressions at the same time; this pass edited neither. Frame-side changes are listed per frame for the next pass.

Gate at the end: `python -X utf8 scripts/plan.py check` exit 0, 0 failures (math-4 plan, 4 progressions, 52 frames,
the new catalogue check); `scripts/stale.py check` 0 failures; `scripts/sequence.py check` 0 courses at the scope
stage yet. The python markdown package: installed on this PC; plan.py needs it only through lesson.py when it checks
written days (math-4 today), so it matters only on a machine without it. Nothing was installed.

## Applied

| Finding | Files | What changed |
|---|---|---|
| Structure 2 (step 3 has no brief, file or kinds) | docs/pipeline/briefs/sequence-write.md, sequence-read.md (new); scripts/sequence.py (new); scripts/plan.py | The scope and sequence brief: files `docs/courses/<course>/scope-and-sequence.md` and `data/plans/<course>/days.csv` (columns `day,stretch,unit,kind,goal,skills,codes,assess,school_day,note`), the unit, stagger and calendar rules, the five day kinds in every subject, Candidate cells settled with their day cost, reserved assessment slots with no items or section plans, `C` days for course-level checks. The expert read brief beside it. The scope-stage gate `sequence.py` (consecutive days, frame totals per unit, stretch 1..units or C, kinds, an end-of-unit assessment per unit, a mid-unit one over 25 days, a respond day after each course-level check, owned skills placed, owned codes placed as notes, the .md present); `plan.py check` runs it for a plan folder with days.csv and no parts or items. Smoke-tested on a synthetic social studies grade 3 day file |
| Structure 4 and 6, Codex 2 (no shared calendar; checks stack) | docs/courses/CALENDAR.md (new); scripts/frame.py; data/plans/calendar.csv (new, generated) | One calendar: school day 1 to 160, week 1 to 32, course day; meeting patterns (science 3 to 5 four a week over 30 weeks; K to 2 science and social studies over 28 to 31 weeks, the `WEEKS` table; Government fall, Economics spring); course day n on school day `start + ceil(n x 5W / D)`; the stagger rule (K to 5 by week, K to 2 one-to-one checks five school days apart, 6 to 8 by school day with week 32 a finals week, the three tools in order, never move a unit); target weeks K to 8. `frame.py sync` writes calendar.csv and the generated table; `frame.py calendar` prints check weeks and rule breaks; citation drift (a cross-frame "unit N (days a to b)" more than 3 days off) is a note |
| Structure 3 and Codex 3 (gate holds none of the lessons) | scripts/frame.py | New rules, added as notes and turned to failures where all 52 frames passed at the end: FAIL for no minutes or no lessons a week in Days, a Check set adds cell not starting Candidate or None, a course-level check with no respond day, no check readable or placeable, check days not adding to the remainder, no Sensitivity reads bullet, no paper path, a model missing from Models carried, a lean missing from Cross-subject, an empty Seams, Models carried, Course-level checks or Cross-subject section. Notes (not every frame passes yet): the one checks-table shape (12), Seams ids (2), ~contribution codes (1), lettered parts (1), outside-reader wording (0), citation drift (0), frames.csv behind (0). The three Codex in-memory omissions (contribution codes, empty sections, an empty checks table) now each produce a note or failure |
| Structure 7 (progression notes are noise) | scripts/progression.py | The depth note goes only when a later grade's rows do not mention the code in notes; the skip note only when neither row names the other or says skip, idle, dormant or returns; the model gap note only when no user row names the model with a reason word. Notes: 609 before, 196 after (skips 393 to 8, model gaps 25 to 2) |
| Structure 8 (standards in full) | scripts/frame.py; frame-write.md; sequence-write.md | The lettered-part note (owned code's parts from the standards files not named in the unit row); the convention "a lettered part is named by its code in the unit that teaches it" in both briefs. Stays a note: 1 frame left |
| Structure 9, Codex 1.1 to 1.3 (course ids) | scripts/frame.py; data/plans/frames.csv; scripts/plan.py; scripts/lesson.py; scripts/course_status.py; scripts/plan_flow.py; data/plans/later.csv | frames.csv now `course,catalog_id,subject,grade,title,units,days,minutes_min,minutes_max,per_week,weeks,term,legacy_plan_id`, written by `frame.py sync`; `check_global` fails a row with no frame, a frame with no metadata, or a catalogue id not in courses.csv. plan.py and lesson.py read subject, grade and day minutes from it (`course_meta`, `day_range`, the math-4 alias kept), accept a day inside the frame's minute range, fail an unknown course or a plan check on zero records, sort `C` days, skip the section lookup on them. `plan.check("biology")` no longer crashes. course_status.py exposes `course` (the frame slug); plan_flow.py joins on it and warns on a core course with no frame. L12 marked done |
| Structure 10, Codex 5 (one name for one thing) | docs/GLOSSARY.md | Rows: course (frame slug, catalogue id, the math-4 lag), scope and sequence (new location, brief), unit (course days 5 to 42, grade 4 math 8 to 22; readiness where it assumes an earlier grade; end-of-unit assessment inside its days with response once; mid-unit over 25 days), end-of-unit assessment (near the end, response counted once, K to 2 observation), teaching day (every subject), warm-up (grammar warm-up), sub-ready day (9 a year in grade 4 math; ELA K to 5 per base unit), record sheet and family note (ELA K to 5 per base unit). New rows: mid-unit assessment, course-level check, day and course day, school day and week, readiness day, retrieval task, check set, lean, bridge |
| Structure 11 (per-unit pieces in ELA K to 5) | docs/GLOSSARY.md | Record sheet, family note and sub-ready day per base unit in ELA K to 5 (frame lines are for the next pass) |
| Structure 12, Codex counts | docs/PRODUCTION-PATH.md; data/courses.csv; scripts/plan_flow.py | 52 core courses get frames, the 6 electives wait; step 6 "all 52 core courses"; the source map is a frame section and the day-level CSV comes with the scope and sequence; After the core subjects lists the 6 electives first, then the 49, and personal finance inside Economics; "units for the 52 core courses"; personal-finance `core` y to n with the reason. The flow's After the core text counts its courses instead of a fixed 49 |
| Structure 2(e), Codex 1.4 and 1.5 (old math assumptions downstream) | docs/pipeline/briefs/plan.md | Subject-neutral: reads the frame, scope-and-sequence.md and days.csv, the subject's progression, lens and bar; unit plans follow steps 3 and 4, a preceding unit need not have written lessons, section plans in step 7 except the probe section; response time named once |
| Step 3 in PRODUCTION-PATH | docs/PRODUCTION-PATH.md | Step 3 names its brief, files, the calendar, `C` days, the gate and the read brief |
| People (FOUNDATION 7.3, Codex 4) | docs/PRODUCTION-PATH.md | The people paragraph: reviewers are agents; answer-key, safety and sensitivity agents do the content reads; no outside human reader; "a human read if a person is found" removed from step 2 and step 6 |
| Codex 3 (what the gates prove) | docs/pipeline/briefs/baseline-1.md | The sentence now says what the gates establish and what they do not |
| Lesson 16, from the subject fixers | docs/pipeline/briefs/frame-write.md; sequence-write.md | New lesson 16 "Readiness by idle time": a skill idle two or more grades gets a readiness check on the unit's first day; one used the year before opens as a retrieval task, not a check (as the science frames applied it). The step 3 brief's readiness rule says the same. The frame-write brief had no lesson 16 before, so this adds it rather than rewording it |
| Literacy codes as also-met, from the subject fixers | scripts/progression.py; scripts/frame.py | cross_subject takes `lit:<code>` (for example `lit:RST.6-8.1`), checked against data/standards/ccss-literacy-6-12.txt (119 codes) with no ELA row needed. Notes only: a code not in the file, a row outside the code's grade band, or `lit:` used in ELA. frame.py does not ask for `lit:` entries in Cross-subject, since they are not leans. Tested in memory on science rows: a valid code passes, and a bad code and a grade 4 use of a 6-8 code each give a note |
| Lessons in the brief | docs/pipeline/briefs/frame-write.md | Days bullet gives minutes, lessons a week and the end-of-unit line, and calls them course days; lettered parts by code; the one Course-level checks table with review rows and the target weeks; the citation rule; which lessons the gate now checks; the sync outputs |

**Should the literacy cells move to `lit:`?** Yes. Today 122 science rows and 58 social studies rows name RST, RH or
WHST codes in notes. Where a note says the row also meets a literacy standard, the later mechanical pass should move
the code to cross_subject as `lit:<code>`, so the gate checks it. Where the row's own skill is the literacy practice
(a science writing row that owns WHST in standard), leave it where it is. Run `plan.py check` after the move and
expect notes only.

**Final sync.** `python -X utf8 scripts/frame.py sync` ran at the end of this pass, after the subject fixers' last
edits: 52 frames, 670 calendar rows. `plan.py check` then gave exit 0 with 0 failures and 195 notes.

## Not applied, with the reason

| Item | Reason |
|---|---|
| Site finding "For Cory" items and SITE-DESIGN | Waiting for Cory, as instructed; nothing on the site or SITE-DESIGN changed |
| Site finding 2 (course-level days `stretch` = `C`, unit blank) | Applied in data terms only: plan.py, sequence.py, GLOSSARY and the brief take it; no site code touched |
| docs/courses/UNIT-PLAN.md rule 5 and "respond half" (Codex 1.5, 5) | Not in my files. Next pass: rule 5 becomes "Unit plans follow the subject-wide order in PRODUCTION-PATH steps 3 and 4. A preceding unit need not have written lessons. Section plans follow step 7, except the probe section"; "respond half" becomes **Response allocation**: "Name the marking time and the response time separately. State whether response occurs within the assessment day or on later respond days, and count it once"; and a line naming its math-only fields |
| data/plans/README.md | Not in my files; it should list the scope-stage days.csv columns and calendar.csv (next pass) |
| Per-course units.csv and modules.csv grades | Replaced for planning by frames.csv and calendar.csv; data/units.csv is blinded to me and still used by math-4 only |
| Codex 1.6 (ELA text-record columns) | ELA's step 5 scope work; the sequence brief allows a source-map row to name a unit before sections exist |
| A `school_day` read in frame.calendar() from a written days.csv | No scope and sequence exists yet; sequence.py checks the column, and CALENDAR.md says it wins once written |
| Frame wording and week moves | Frames belong to the subject fixers; listed below |
| One leftover file: S:\chk.txt | A stray gate log I wrote at the drive root; the safety check blocked my removal. Cory may delete it |

## Frame-side changes for the next pass, per frame

**Week moves (the stagger rule; `frame.py calendar` shows the breaks).** Tools in order: meeting days, split review,
the other side of a unit; no unit moves.

| Frame | Now (weeks) | Change |
|---|---|---|
| math-kindergarten | 17, 32 | Year-end check in week 31, inside unit 8 (it owns counting sequence and fluency within 5): unit 8's last 5 days after the check |
| math-grade-1 | 19, 32 | Year-end check after unit 7 (week 30); unit 8, a review unit owning nothing, after it serves as respond time |
| math-grade-2 | 18 to 19, 32 | Year-end check after unit 8 (about week 29); unit 9 (review, owns nothing) after it |
| science-grade-2 | 15, 28 | Mid-year check in week 17 (schedule its sessions so the check days fall there) |
| social-studies-grade-2 | 15, 31 | Mid-year check in week 14 (school days 66 to 70) |
| math-grade-3, -4, -5 | year-end 32 | Split the year review: rows "Year review, part 1 / 9 / 3 / 0", "Check 3 / 9 / 2 / 2", "Year review, part 2 / 9 / 4 / 0" so check 3 falls in week 31 (days 153 to 154, respond 155 to 156) |
| social-studies-grade-3 | 14, 25, 32 | Check 3 before unit 7 ("How our community changed"), about week 28; unit 7's end-of-unit assessment covers unit 7 |
| social-studies-grade-4 | 12, 21, 32 | Check 1 after unit 2 (week 8), the first-peoples claim moving to check 2 (or, the alternative, math-grade-4 check 1 after unit 3, week 9); check 3 after unit 6, about week 27 |
| science-grade-5 | 11, 21, 30 | Five sessions in weeks 9 and 10, so check 1 falls in week 10, clear of math's week 11 |
| math-grade-6 | 12, 24, 32 | Check 1 after unit 4 (about day 80, week 16), checking units 1 to 4, clear of ELA's day 59 to 60 |
| Grades 7 and 8, the K to 2 science and social studies year-ends, and the high school frames | | None: inside the rule (7: math and social studies share week 24 on different days) |

**Other frame changes.**

| Frame(s) | Change | Source |
|---|---|---|
| algebra-i, algebra-ii, geometry, math-kindergarten to math-grade-8 (12) | Course-level checks in the one table `| Check | After unit | Check days | Respond days | What it checks |` | Structure settled table |
| science-grade-6 | Seams names chem-energy-accounting, chem-equilibrium-design, chem-reaction-rates, chem-resources-hazards and the other hands_on ids the gate lists | frame.py note |
| science-grade-7 | Seams names chem-nuclear-processes | frame.py note |
| science-grade-8 unit 3 | ~MS-PS3-5 in Owned standards | frame.py note (Codex 3) |
| social-studies-grade-5 unit 8 | MA.5.T5.6a and MA.5.T5.6b named in What students learn | frame.py note (structure 8) |
| science-grade-3, -4, -5 | Replace the "near school day 4n/3" conversion with: "Science has 120 sessions in 30 weeks of four sessions each; their school days come from docs/courses/CALENDAR.md and data/plans/calendar.csv" | Codex 2 |
| Every frame whose Days bullet says "teaching days" (25: algebra-i, algebra-ii, geometry, ELA 3 to 12, social studies 3 to 5 and 6 to 12) | "course days" for the totals | Codex 5, GLOSSARY |
| Every frame | The Days bullet line "Each unit's days include its end-of-unit assessment (and, in units over 25 days, its mid-unit assessments)" where missing; a readiness line where a unit assumes an earlier grade's row | Structure 1 |
| english-language-arts-kindergarten to -grade-5 | "Record sheet, family note and sub-ready day go per base unit (three per unit)"; the source map names the base text's assessments as the mid-unit and end-of-unit assessments | Structure 1, 11 |
| ELA 3 to 8, math 3 to 5, science 3 to 5, social studies 3 to 5 ("Four check days", "Six check days") | "course-level check days" | Structure 10 |
| Any frame identification line | "Course `<slug>` (catalogue id `<catalog_id>`)", from frames.csv | Codex 1.1 |

The minutes, Candidate, paper path, sensitivity, respond-day, missing-lean (math-6, ela-8, science 4's
s4-energy-resources) and outside-reader items the reviews listed were fixed by the subject fixers during this pass:
the gate now fails them, and all 52 frames pass.

## Settled

| Choice | Reason | Files |
|---|---|---|
| frames.csv is the course registry: frame slug, catalogue id, subject, grade, minutes, meetings, weeks, term, legacy id | One generated source for every script; catalogue ids unchanged | scripts/frame.py, plan.py, lesson.py, course_status.py, plan_flow.py |
| Calendar positions, not dates: 160 school days, 32 weeks; course day n on school day `start + ceil(n x 5W / D)` | Every cross-subject citation means the same week | docs/courses/CALENDAR.md, frame.py |
| Stagger rule by teacher model: K to 5 by week, 6 to 8 by school day with a finals week 32, 9 to 12 finals only; K to 2 one-to-one checks five school days apart | One teacher marks every elementary check; middle school students sit one check a day | CALENDAR.md, sequence-write.md |
| Week fixes in order: meeting days, split review, the other side of a unit; never move a unit | Units carry the frame's reasoning | CALENDAR.md |
| K to 2 science and social studies spread over 28 to 31 weeks | Clears weeks 31 and 32 for math and ELA without moving a day | frame.py `WEEKS` |
| Scope-stage days.csv columns and the `assess` values readiness, mid, end, course, observe | Reserves slots without items (Codex 1.4) | sequence-write.md, sequence.py |
| A lesson rule becomes a failure only when all 52 frames pass it | No gate broken mid-edit | frame.py |
| Progression notes stay only while the rows have not said why | 384 of 393 skip notes were answered | progression.py |
| Day length per course from its frame, a range where the frame gives one | 40 to 90 minute courses are checked against their own day (Codex 1.2) | plan.py, lesson.py |
| Personal finance: catalogue `core` n, taught inside Economics | Cory, 2026-11-14 | data/courses.csv, PRODUCTION-PATH |

## For Cory

Nothing new. The two minute questions (the elementary day; social studies 6 to 12 minutes) are the site and
structure reviews' existing For Cory items; the frames now all state minutes.
