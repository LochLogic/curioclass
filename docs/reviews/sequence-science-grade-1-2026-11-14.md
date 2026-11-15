# Expert read: scope and sequence of Science, Grade 1

Course `science-grade-1`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with {subject} = science
and {bar} = docs/RUBRIC-SCIENCE.md. Independent of the Codex read of the same course, which was not opened.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/RUBRIC-SCIENCE.md; docs/GLOSSARY.md; the
  brief.
- Cold: docs/courses/science-grade-1/scope-and-sequence.md and data/plans/science-grade-1/days.csv (68 rows).
- Beside them: docs/courses/science-grade-1/frame.md; the K and grade 1 rows of data/progressions/science.csv; the
  grade 1 rows of data/standards/ngss-pe-dimensions.csv; docs/courses/CALENDAR.md and the grade 1 rows of
  data/plans/calendar.csv; the lean rows of the grade 1 math frame (1.MD.C.4 in unit 1, 1.MD.A.1 and 1.MD.A.2 in
  unit 6) and ELA frame (RI.1.1 and W.1.2 in unit 1, SL.1.5 and W.1.8 in unit 2, RI.1.2 in unit 3); the kindergarten
  science scope and sequence (what grade 1 retrieves); the social studies sequence reads' "Settled by the expert"
  tables; for REPEAT tags, docs/reviews/sequence-k-2-fixes-2026-11-14.md and
  docs/reviews/baseline-1-science-2026-11-14.md.
- Gates: `plan.py check` passes this course (0 failures). The run's only failures are biology's (14), another course
  the running Codex job is writing. `frame.py calendar`: science grade 1 checks in weeks 15 and 29, no stagger
  break. `stale.py check`: 0 failures.
- Judged as if the course meets three times a week (settled); no week in the CSV holds more than three meetings.

## Verdict

This is the strongest of the three K to 2 science sequences: each unit is driven by a phenomenon children can see,
its fold-in days mostly carry real second cases, retrieval of kindergarten is placed where it is used, the split
light unit is counted once, and the daylight strips answer the frame read's serious finding. The main risk is two
build-and-test assessment days that ask each child to design, build and test in one 30-minute lesson. The one change
that matters most is to split those days into a build lesson and an observed test lesson inside the same window, and
to name the small-group observation format; the rest are context and wording fixes.

## Findings, most serious first

### 1. Two assessment days ask each child to design, build and test in one lesson (moderate; likely)

LAYER sequence. REPEAT new (the same pattern, more severe, is finding 1 of the kindergarten read).
- **What is wrong.** Day 54 has each child design, build and test a 1-PS4-4 device that uses light or sound to
  send a message over a distance, observed per child, in one 30-minute lesson; day 46 asks a similar observed
  per-child performance. A six-year-old's build alone takes most of a lesson; the teacher cannot also watch 20 tests.
- **Why it matters.** A writer either cuts the test (and the "test" part of the expectation goes unasked) or runs
  over into the response day, which then has no time to respond.
- **Fix (days.csv days 46 and 54 goals and notes; scope and sequence assessment paragraph).** Build in pairs or
  alone on the day before the window's observation (the window's first day becomes "build and record the plan"),
  test on the second day in small groups of four or five with a per-child checklist, each child saying what the
  device sends and why it works. Kind and count stay; only what each day holds moves. Add the kindergarten format
  sentence (small groups, per-child record, named independent task for the rest) to the assessment paragraph.
- **Confidence.** Likely.

### 2. The mid-year check asks 1-PS4-1 in a contrived context (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 36 checks 1-PS4-1 (vibrating materials make sound, sound makes materials vibrate) "using unit
  2's tower and paper materials". Unit 2 is the design unit; a paper tower is not a sound context, so the item asks a
  child to transfer to a setting with no sound in it. The check rule wants earlier units' content, not an invented
  one.
- **Fix.** Day 36 note and the mid-year paragraph: use unit 2's detecting part (the big-ears or paper ear cone the
  class designed), with a tissue strip held near a sounding cone: "What does the strip do, and why?"
- **Confidence.** Firm.

### 3. Day 26 orders leaves by length from pictures (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** Day 26 says "directly order depicted leaves". Photographs at unknown scale cannot be ordered by
  length, and direct comparison (1.MD.A.1, the lean the day bridges) needs the objects side by side.
- **Fix.** Day 26: "directly order real pressed leaves, or life-size printed leaves, by length".
- **Confidence.** Firm.

### 4. Two fold-in days only rehearse (minor; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Most fold-in days carry a second case (days 3, 12, 14, 17, 24, 30, 45, 52). Days 6 and 41 only
  rehearse the previous day's talk, so they answer no question (S1).
- **Fix.** Day 6 and day 41 each take a new case the day before raised (a second material or a second young
  animal), keeping the rehearsal inside it. Both stay on the shorter path's fold-in list.
- **Confidence.** Likely.

### 5. The frame still calls two retrievals "readiness" (minor; firm)

LAYER frame. REPEAT yes (the K to 2 social studies fixes carried the same stale readiness wording,
docs/reviews/sequence-k-2-fixes-2026-11-14.md).
- **What is wrong.** The frame's unit 2 row says "readiness review" and unit 4 says "readiness look"; its Days
  bullet and this sequence rightly say retrieval, since kindergarten is the year before.
- **Fix.** Frame unit 2 and unit 4 rows: "retrieval of ..." in place of "readiness review" and "readiness look".
- **Confidence.** Firm.

## Checks the brief asks for

- **Order inside each unit:** met; each opens on its anchor with retrieval where kindergarten applies, builds a
  model, revises it from evidence and returns to the anchor.
- **Assessments:** every part of every code has a named prompt or product; response counted once per window. Time
  per child is finding 1.
- **Readiness or retrieval:** met. Kindergarten rows are retrieved, not checked, as call 1 of the K to 2 fixes
  settled (sk-weather-watch on days 1 and 9, needs on day 10, sk-push-pull on days 28 and 43).
- **Checks that do not repeat:** stated for both; finding 2 is the one weak item.
- **Standards in full:** every lettered part is carried by a named day; unit 8, split around the year, is counted
  once.
- **Days by load:** fair.
- **Calendar:** checks in weeks 15 and 29, on target. Leans checked against calendar.csv; the 1.MD.A.2 bridge on day
  50 is required and correct, and the other leans follow their math or ELA unit.
- **Candidate cells:** settled with day costs.
- **Shorter path:** present, with named fold-ins and nothing assessed folded.
- **Source map:** not applicable.
- **Stale notes:** `stale.py check` clean; finding 5 is the frame's.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| A unit's anchor is a topic, not a phenomenon | Met |
| A model is used before the unit that builds it | Met |
| Engineering design expectations appear in no unit | Met: K-2-ETS1-2 in unit 2 and 1-PS4-4's device |
| Equipment assumed with no substitute or no-kit path | Met: paper and household stand-ins, a single-device media path |

Rubric rows this layer owns: Gateway 1 at plan level and S1 met (finding 4 is small); 2a to 2c and S11 met; 2e met (no
light speeds or wave models; patterns of sky motion described, not explained); 2h met (sentence frames begin in unit
5); S6 met (per-unit costs given inside the frame's allowance); S7 met.

## What is right and should not be touched

- The daylight strips, so the seasonal comparison rests on the class's own record.
- Retrieval of kindergarten placed on the day it is used, not front-loaded.
- Dropping the two-group device comparison so grade 2 owns it.
- Per-unit cost allocations ($2, 10, 1, 8, 8, 8, 1, 2).
- At most three meetings in any week; the split unit 8 counted once.

## What I could not judge

- Local sky and daylight data are left to the unit plans, rightly.
- No outside source was fetched; the standards' wording rests on data/standards/ngss-pe-dimensions.csv and memory.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 46 and 54: build on the window's first day, observed small-group test on the second | Each child's test is heard inside the window | days.csv days 45, 46, 53, 54; scope-and-sequence.md assessment paragraph |
| Small-group observation format named, as in kindergarten | One rule across the band | scope-and-sequence.md assessment paragraph |
| Mid-year 1-PS4-1 item uses unit 2's ear cone with a tissue strip | Earlier content in a sound context | days.csv day 36; scope-and-sequence.md mid-year |
| Day 26 orders real pressed or life-size printed leaves | Direct comparison needs true length | days.csv day 26 |
| Days 6 and 41 take a new case | Each day answers a question | days.csv days 6, 41 |
| Frame units 2 and 4 say retrieval | Kindergarten is the year before | frame.md |

## For Cory

Nothing.

## Sources

- data/standards/ngss-pe-dimensions.csv and the Next Generation Science Standards grade 1 expectations, from memory.
- docs/RUBRIC-SCIENCE.md, docs/agents/lenses/science.md.
- docs/courses/CALENDAR.md, data/plans/calendar.csv, the grade 1 math and ELA frames.

## For the source list

None.
