# Expert read: scope and sequence of Science, Kindergarten

Course `science-kindergarten`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with {subject} =
science and {bar} = docs/RUBRIC-SCIENCE.md. Independent of the Codex read of the same course, which was not opened.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/RUBRIC-SCIENCE.md; docs/GLOSSARY.md; the
  brief.
- Cold: docs/courses/science-kindergarten/scope-and-sequence.md and data/plans/science-kindergarten/days.csv (64 rows).
- Beside them: docs/courses/science-kindergarten/frame.md; the K rows of data/progressions/science.csv; the K rows of
  data/standards/ngss-pe-dimensions.csv; docs/courses/CALENDAR.md and the grade K rows of data/plans/calendar.csv; the
  lean rows of the kindergarten math and ELA frames (unit placement of K.MD.A.2, K.MD.B.3, SL.K.3, SL.K.5, W.K.1,
  W.K.2); the "Settled by the expert" tables of the six social studies K to 5 sequence reads; for REPEAT tags,
  docs/reviews/frame-science-kindergarten-2026-11-14.md and docs/reviews/baseline-1-science-2026-11-14.md.
- Gates: `plan.py check` passes this course (`sequence science-kindergarten: 0 failure(s)`). The run's only
  failures are biology's (14, no scope and sequence yet), another course the running Codex job is writing.
  `frame.py calendar`: science K checks in weeks 14 and 29, no stagger break. `stale.py check`: 0 failures.
- Judged as if the course meets three times a week (settled). The CSV never puts more than three meetings in a week,
  so the placement already fits.

## Verdict

The sequence is sound in its bones: six phenomenon-led units in the frame's order and counts, every owned
expectation carried by named days with its practice and crosscutting concept, both checks on their target weeks,
honest bridges for every math and ELA lean, and careful safety and no-kit paths. The biggest risk is assessment
time: every end-of-unit window and both course-level checks ask each kindergartner for a full multi-part
performance inside two 30-minute lessons with one adult, which a writer cannot build as written. The one change
that matters most is to set the K assessment format at this layer (small groups, each child's own response mat or
build, one spoken "why" per code, a named independent task for the rest of the class); second, give the ten
rehearsal days real questions.

## Findings, most serious first

### 1. The observations ask for more per child than the reserved lessons can hear (serious; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Each unit's end-of-unit observation is two lessons (about 50 minutes once day 2's ten response
  minutes are taken), and in that time "each child" plans and carries out separate strength and direction trials
  with pushes and pulls and explains collisions (day 8), or compares all four materials and also designs, builds
  and tests a new cover (day 53). The mid-year check (days 29 and 30) asks every child for a "complete talk-and-point
  battery" on five expectations, about 12 to 15 parts, in two 30-minute lessons; the year-end check (62, 63) does
  the same for seven expectations and adds a build. With 20 children that is two to three minutes a child for the
  whole battery. The sequence itself flags the risk ("If the school cannot hear every child ... flag the local
  timing constraint", Shorter path) but leaves the format to the unit plans. Day 53 has a second, physical problem:
  a new cover cannot be built, left in the sun long enough to make a felt difference, and compared, inside one lesson.
- **Why it matters.** A unit plan writer builds one-to-one observations that run over by a lesson each time, or the
  teacher marks parts "can do" for children never asked. Either way the record that goes to grade 1 is not true.
  The frame and the year's check weeks leave no spare meeting to absorb it.
- **Fix (scope and sequence, "Kindergarten assumes no earlier science course" paragraph; days 8, 18, 27, 42, 53, 60,
  29, 30, 62, 63 notes).** Add: "Kindergarten observations run in small groups of four or five. Each child answers on
  their own picture mat (pointing, placing a card, drawing) while the teacher records each child on a checklist; the
  practice parts (planning, carrying out, building) are observed during the group's work, recorded per child; each
  child gives one spoken 'why' per code. The other children work on a named independent task from the unit (a
  drawing of the anchor explained, a picture sort). About 10 to 12 minutes a group fits five groups in the two
  lessons." Day 53: children build the new cover and set it in the sun; day 54 compares covered and uncovered spots
  before the response minutes (or at the afternoon routine look the same day).
- **Confidence.** Likely (the counts are from the rows; the minutes per child are arithmetic; the small-group
  format is common kindergarten practice, from memory).

### 2. Ten "rehearsal" days answer no question (moderate; likely)

LAYER sequence. REPEAT new.
- **What is wrong.** Days 7, 12, 16, 23, 26, 35, 39, 48, 51 and 58 are Fluency days whose goal is to "rehearse" or
  "practise" something already done, each noted as a "six-minute rehearsal" that can join its neighbour. They are
  exactly the Shorter path's fold-in list: the days were written to be cut. That is 10 of 58 unit days; with the 12
  observation days, 22 of 58 days teach nothing new. The lens asks that each lesson answer a question the last one
  raised (S1); a 30-minute kindergarten lesson built on a six-minute job will be padded or rushed. Meanwhile unit 4,
  the heaviest (three expectations), gives K-ESS3-1's model only days 36 and 37 of its own.
- **Why it matters.** A writer has nothing to build these days from but repetition; kindergartners lose the
  storyline; the load-heavy parts get no more time.
- **Fix (days.csv goals and notes of the ten days; no kind, count or code change; the fold-in list stays).** Each
  day takes a new case the day before raised, and keeps its rehearsal inside it:
  - Day 7: "Does a pull work the same way on something heavier? Compare a gentle and a strong pull on a loaded box."
  - Day 12: the frame's candidate as a second look: "Is the slide warmer or cooler than the morning at afternoon
    recess?" with the chart words used to record it.
  - Day 16: the class asks a second forecast question of a different source (a calm picture forecast for the
    region's own severe weather).
  - Day 23: "Will the same ramp work for a bigger ball?" read from reached or not-reached results.
  - Day 26: the ramp tried on a new target the class picks.
  - Day 35: a second place added to the needs sort: what lives near our town's water source, and what it needs.
  - Day 39: a beaver dam or nest picture as a new change to explain with "I think ..., because I saw ...".
  - Day 48: the four materials compared in a second sunny spot (the playground edge).
  - Day 51: the tested cover tried on a second small area (as the CSV has it), now asked "does it still work in
    the afternoon?"
  - Day 58: the class tells another class's picture of litter what its solution would do.
- **Confidence.** Likely.

### 3. Day 14 uses archived records when the class's first month is already complete (moderate; firm)

LAYER sequence. REPEAT yes (the frame read's finding 1 was the same fault: the monthly comparison set before the data
exist).
- **What is wrong.** Day 14 (school day 32) "Compare the two completed weather-record months" and, because two live
  months do not exist yet, tells the teacher to obtain "dated local archived records". Public daily climate records
  give temperatures and rain, not the sunny, cloudy and windy picture categories the chart uses, so the teacher would
  have to invent the translation. The class's own first month (school days 1 to about 20) is complete by day 14, and
  K-ESS2-1 asks for counts of sunny, windy and rainy days in a month, not a comparison of two months.
- **Why it matters.** A writer sends every teacher hunting for data that do not hold the class's categories; the
  live record, which is the point of the routine, waits until day 19.
- **Fix (days.csv days 14 and 19; scope and sequence unit 2, second paragraph).** Day 14: "Count the sunny, cloudy,
  rainy and windy days in our first month and revise the class pattern chart." Day 19 keeps the two-month
  comparison on the live record (school day 44 holds about two months). Archived records only where a school's
  science starts late; then they are labelled as someone else's data.
- **Confidence.** Firm (the dates are the CSV's; the standard's clarification from the dimensions file and memory).

### 4. K-ESS3-3 asks every child for all four of land, water, air and living things (minor; firm)

LAYER sequence (and standard: the dimensions file's paraphrase). REPEAT new.
- **What is wrong.** Day 60 requires each child to connect the action "to an effect on land, water, air AND living
  things", and the year-end check says the same. The expectation reads "land, water, air, and/or other living things";
  data/standards/ngss-pe-dimensions.csv shortens it to "land, water, air and living things", which is where the
  over-reading starts.
- **Why it matters.** The observation asks more than the standard, takes time the window does not have (finding 1),
  and marks a child short who met the expectation.
- **Fix.** Days 60, 61, 62, 63 notes and the scope and sequence unit 6 and year-end paragraphs: "connects the action to
  an effect on one or more of land, water, air and living things; the class model holds all four." The dimensions
  file's K-ESS3-3 statement gets "and/or" back (for the fix pass to file with the data owner).
- **Confidence.** Firm (the standard's text, from memory; the CSV rows).

### 5. The mid-year check's design item reuses unit 3's own context (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** The rule is that a check right after a unit's assessment draws that unit's items from earlier
  units' content. Days 29 and 30 say so ("never the just-assessed ramp/tower"), but the prose's item is "the new
  ball-to-bin problem", a ball rolled to a target, which is unit 3's ramp task in a new costume.
- **Why it matters.** The check repeats the end-of-unit assessment of the week before, the thing the rule exists to
  stop, and the CSV and the prose disagree on what the item is.
- **Fix.** Scope and sequence, Mid-year paragraph: replace "defining the new ball-to-bin problem" with "defining a
  problem in unit 1's toy-car context (the car must stop before the rug's edge) and judging a shown fix from
  yes-or-no results".
- **Confidence.** Firm.

### 6. No unit carries a cost (minor; firm)

LAYER sequence. REPEAT new.
- **What is wrong.** The rubric reads a scope and sequence on S6 (costs). The frame's allowance is about $40 a class
  (settled); this sequence hands all costing to the unit plans and gives no allocation, where the grade 1 sequence
  gives one per unit.
- **Fix.** Add to "The three materials paths" paragraph the allocations under "Settled by the expert".
- **Confidence.** Firm.

## Checks the brief asks for

- **Order inside each unit:** met. Each unit opens on its anchor, builds an initial picture model, revises it from
  evidence and returns to the anchor; unit 3 defines the problem before building; unit 4 puts needs before the
  place model and the claim; unit 5 observes warming before designing a cover.
- **Assessments:** each end-of-unit window lists every code its unit teaches and names a prompt or product per part
  (apart from finding 4's over-reach); no unit exceeds 25 days; response is counted once, in each window's last ten
  minutes. The time to give them is finding 1.
- **Readiness or retrieval:** met. Kindergarten assumes no earlier row, so no readiness checks; later units retrieve
  this year's ideas inside their hook days (days 10, 20, 32, 44, 55). Days 44 and 55 each retrieve three units in a
  30-minute hook: keep each to one short question so the hook stays the hook.
- **Checks that do not repeat:** stated for both checks; finding 5 is the one slip.
- **Standards in full:** every part of the 11 expectations is on a named day (K-LS1-1's four parts on 33 and 34,
  K-PS3-1's four materials on 45 and 46, K-PS2-1's strength and direction separately on 2 to 4, collisions on 5).
  K-ESS2-2's "choose ways to do less harm" (day 40) is inside that expectation's own secondary core idea, rightly
  assessed on day 42.
- **Days by load:** fair across units (9, 10, 9, 12, 11, 7 for 1, 2, 2, 3, 2, 1 expectations); inside unit 4 see
  finding 2.
- **Calendar:** checks in weeks 14 and 29, on target. Leans checked against calendar.csv: math K.MD.B.3 (school
  days 19 to 44) and K.MD.A.2 (45 to 63), ELA SL.K.3, W.K.1, W.K.2 (unit 1, 1 to 34) and SL.K.5 (unit 2, 35 to 76);
  each science use either follows or carries the frame's bridge. ELA's weather unit (from school day 35) and trees
  unit (from 80) come after science units 2 and 4 begin.
- **Candidate cells:** all six settled with day costs (kept 1, 2, 3, 6; dropped 4, 5).
- **Shorter path:** present: a 20-minute period and ten named fold-ins, nothing assessed folded.
- **Source map:** not applicable (no base text).
- **Stale notes:** `stale.py check` clean. The frame's Cross-subject weeks ("unit 4 begins about week 16") differ
  from the CSV (week 15); the fix pass's frequency rewrite of the frame covers it.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| A unit's anchor is a topic, not a phenomenon | Met: every anchor is a thing seen at school (a rolling ball, the coat pile, the missed tower, the weed and dug hole, the sunlit slide, the litter tally) |
| A model is used before the unit that builds it | Met: cause-effect from unit 1, patterns from 2, design cycle from 3, claim and system model from 4, each reused only later |
| Engineering design expectations appear in no unit | Met: K-2-ETS1-1 in unit 3, K-PS3-2 in unit 5, unit 6's chosen solution |
| Equipment assumed with no substitute or no-kit path | Met: household stand-ins and labelled media paths throughout; builds keep paper and tape so no child loses the making |

Rubric rows this layer owns: Gateway 1 at plan level and S1 met (phenomena drive each unit; storyline weakened only by
finding 2); 2a to 2c and S11 met for the grade's expectations; 2e met (no thermometers, no friction, no magnets, no
food chains or photosynthesis; the class plant is not a grade 2 experiment); 2h met in plan (claims grow from spoken to
drawn); S6 part (stand-ins yes, costs finding 6); S7 met (our own, OpenSciEd elementary named as reference only).

## What is right and should not be touched

- The weather routine from school day 1 to 160, with "do not add category counts to infer days" and the teacher
  counting past ten.
- One variable at a time in unit 1, written into every day; contact forces only.
- The plant records as observation, not a controlled test, with no plant left to die (keeps grade 2's experiment
  fresh).
- The unit 6 follow-up count with its honest caveat that a smaller count does not prove the solution worked.
- Every safety cell (back-of-hand touch after the teacher checks, no sun viewing, gloves and grabbers, adults bag
  waste) and every sensitivity line (no disaster retellings, no questions about home heating, coats or recycling).

## What I could not judge

- Whether 30-minute lessons hold the hook-day retrievals in units 5 and 6 (needs a written day).
- Local data: the town's water source and the region's severe weather are left to the unit plans, rightly.
- No outside source was fetched in this run; the standards' wording rests on data/standards/ngss-pe-dimensions.csv
  and memory.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Small-group observation format (groups of four or five, own picture mat, per-child checklist, one spoken "why" per code, named independent task for the rest) | Every child heard on every part inside the reserved lessons | scope-and-sequence.md assessment paragraph; days.csv notes of days 8, 18, 27, 29, 30, 42, 53, 60, 62, 63 |
| Day 53 builds and sets out the new cover; the covered and uncovered comparison opens day 54 (or the afternoon look) | Sunlight needs time to make a felt difference | days.csv days 53, 54 |
| The ten Fluency days take the new cases listed in finding 2 | Each day answers a question the last raised | days.csv days 7, 12, 16, 23, 26, 35, 39, 48, 51, 58 |
| Day 14 counts the first live month; day 19 compares two live months; archived data only for a late start | The class's own record holds the categories | days.csv days 14, 19; scope-and-sequence.md unit 2 |
| K-ESS3-3 assessed as "one or more of land, water, air and living things" | The expectation says "and/or" | days.csv days 60 to 63; scope-and-sequence.md unit 6 and year-end |
| Mid-year design item in unit 1's toy-car context | The check must not repeat unit 3's assessment | scope-and-sequence.md mid-year paragraph |
| Cost allocations inside the $40 allowance: unit 1 $4, unit 2 $2, unit 3 $5, unit 4 $8, unit 5 $9, unit 6 $12 (gloves and grabbers) | S6 asks the plan for costs; limits, not prices | scope-and-sequence.md materials paragraph |

## For Cory

Nothing. No finding here changes scope, money, people or audience.

## Sources

- data/standards/ngss-pe-dimensions.csv (the K expectations' elements, clarifications and boundaries) and the
  Next Generation Science Standards K expectations, from memory for the "and/or" of K-ESS3-3.
- docs/RUBRIC-SCIENCE.md and docs/agents/lenses/science.md (the bar and the lens).
- docs/courses/CALENDAR.md, data/plans/calendar.csv, the kindergarten math and ELA frames (lean timing).

## For the source list

None.
