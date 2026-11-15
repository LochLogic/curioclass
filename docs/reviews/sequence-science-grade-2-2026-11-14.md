# Expert read: scope and sequence of Science, Grade 2

Course `science-grade-2`. Cold read, 2026-11-14, per docs/pipeline/briefs/sequence-read.md, with {subject} = science
and {bar} = docs/RUBRIC-SCIENCE.md. Independent of the Codex read of the same course, which was not opened. This
report closes the band, so it ends with "Across the band".

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/RUBRIC-SCIENCE.md; docs/GLOSSARY.md; the
  brief.
- Cold: docs/courses/science-grade-2/scope-and-sequence.md and data/plans/science-grade-2/days.csv (76 rows).
- Beside them: docs/courses/science-grade-2/frame.md; the K to 2 rows of data/progressions/science.csv; the grade 2
  rows of data/standards/ngss-pe-dimensions.csv; docs/courses/CALENDAR.md (PINS science-grade-2 {40: 84}) and the
  grade 2 rows of data/plans/calendar.csv; the lean rows of the grade 2 math frame (2.MD.D.10 in unit 1, 2.MD.A.1 in
  unit 3) and ELA frame (RI.2.3, W.2.7, W.2.8 in unit 3; W.2.1 in unit 4); the kindergarten and grade 1 science
  scopes and sequences; the social studies sequence reads' "Settled by the expert" tables; for REPEAT tags,
  docs/reviews/frame-science-grade-2-2026-11-14.md, docs/reviews/baseline-1-science-2026-11-14.md and
  docs/reviews/sequence-k-2-fixes-2026-11-14.md.
- Gates: `plan.py check` passes this course (0 failures). The run's only failures are biology's (14), another course
  the running Codex job is writing. `frame.py calendar`: science grade 2 checks in weeks 17 and 28, no stagger break.
  `stale.py check`: 0 failures.
- Judged as if the course meets three times a week (settled). Meetings per school week were counted from the
  CSV's school_day column.

## Verdict

The content plan is good: every unit opens with retrieval of grade 1, the plant experiment runs two weeks on
pre-grown seedlings, the habitat survey is repeated so the count means something, and adult-only heating keeps unit 3
safe. But the calendar does not fit the settled three meetings a week: weeks 26 and 27 each hold four, and the
second half of the year has more meetings than slots. The one change that matters most is to move the mid-year check
to week 20, after unit 4, which frees the slots; second, give the build assessments and the rehearsal days the same
fixes as kindergarten.

## Findings, most serious first

### 1. Weeks 26 and 27 hold four meetings; the second half does not fit three a week (serious; firm)

LAYER frame (the calendar pin). REPEAT yes (docs/reviews/baseline-1-science-2026-11-14.md, finding 6, raised weekly
time for K to 2 science; this is its first breakage on a calendar).
- **What is wrong.** Counting the CSV's school days by week: week 26 holds days 66, 67, 68, 69 and week 27 holds 70,
  71, 72, 73, four each. Week 17 is full with the mid-year check (39, 40, 41, pinned at school day 84). From day 42
  to day 76 there are 35 meetings for weeks 18 to 28, 33 slots at three a week, with the year-end check due in week
  28. Weeks 1 to 16 hold only 38 meetings in 48 slots, so the course has the time; it sits on the wrong side of the
  pin.
- **Why it matters.** A writer builds a fourth science lesson into two weeks the school does not give, or cuts days
  the frame counts. This breaks a decision Cory settled today.
- **Fix (CALENDAR.md PINS and tool (c); days.csv school_day column; scope and sequence mid-year paragraph).** Move the
  mid-year check to week 20, after unit 4 (days 49 and 50 end in week 20): days 39, 40, 41 follow day 50, the pin
  becomes about school day 98, and weeks 17 to 28 then hold 35 meetings in 36 slots. Week 20 holds no other grade 2
  subject's check (social studies 14 and 31, ELA 15 to 16 and 32, math 18 to 19 and 29). Its "What it checks" cell
  becomes units 1 to 4, with unit 4's skills drawn from units 1 to 3's content. Day numbers can stay; only school
  days and the pin change. The alternative, keeping the pin and opening unit 4 before the check after packing units 1
  to 3 at three a week, splits unit 4 around a two-week break and is worse.
- **Confidence.** Firm (counts from the CSV).

### 2. Three build or plan assessments ask too much of one lesson (moderate; likely)

LAYER sequence. REPEAT yes (finding 1 of the kindergarten and grade 1 reads, this date).
- **What is wrong.** Day 49 observes each child reassembling a set of pieces into a new object (2-PS1-3); day 58
  holds a class record and then each child's own plan in one lesson; day 64 has each child build an individual model
  (2-ESS2-2 or the unit 6 equivalent). With 20 children and one adult, a build plus an observation of each child does
  not fit one 30-minute lesson.
- **Fix (days.csv days 48, 49, 57, 58, 63, 64; scope and sequence assessment paragraph).** Grade 2 children can
  write: the window's parts that are explanation go on paper items with sentence frames, and the practice part
  is one observed station that small groups rotate through, recorded per child. Builds start the lesson before and
  are finished, not begun, on the check day.
- **Confidence.** Likely.

### 3. Eight "fluency" days only rehearse (moderate; likely)

LAYER sequence. REPEAT yes (finding 2 of the kindergarten read, this date).
- **What is wrong.** Days 8, 13, 22, 32, 36, 44, 56 and 62 rehearse the day before and answer no question (S1). Days
  69 and 71, also on the fold-in list, carry the habitat comparison and the anchor answer, so folding them on the
  shorter path loses taught content.
- **Fix.** Each of the eight takes a new case the day before raised (a second sample, a second place, a second
  material), keeping its rehearsal. On the shorter path, fold days 69 and 71 into their neighbours by moving their
  content, not dropping it, or replace them on the fold-in list with two of the eight.
- **Confidence.** Likely.

### 4. No unit carries a cost (minor; firm)

LAYER sequence. REPEAT yes (finding 6 of the kindergarten read).
- **Fix.** Add per-unit allocations inside the settled $50 allowance to the materials paragraph, weighted to unit 3
  (heating and materials) and unit 2 (the plant test); the unit plans hold the prices.
- **Confidence.** Firm.

### 5. The frame's seam table still says "readiness look" (minor; firm)

LAYER frame. REPEAT yes (grade 1 read finding 5; the K to 2 social studies fixes).
- **Fix.** The frame seam table: "retrieval" in place of "readiness look" for every row grade 1 taught; the sequence
  already notes it.
- **Confidence.** Firm.

## Checks the brief asks for

- **Order inside each unit:** met.
- **Assessments:** every part of every code has a named prompt or product; time is finding 2.
- **Readiness or retrieval:** met as written: grade 1 rows are retrieved on days 6, 11, 16, 27, 42, 51, 60 and 66.
  The skip-grade threads (sk-forecast-severe, sk-needs-places; the frame read's finding 2) are rows grade 1 retrieved
  only in part: grade 1 used the information-seeking practice, not the severe-weather content. Day 11's look back
  should therefore carry a short reteach of the kindergarten content, which the note can say in one line. It is
  retrieval by the letter and not a finding.
- **Checks that do not repeat:** met; the mid-year check's 2-PS1-2 item uses unit 2's content (day 40).
- **Standards in full:** every lettered part carried by a day.
- **Days by load:** fair.
- **Calendar:** checks in weeks 17 and 28 on target but week loads break (finding 1). Leans checked against
  calendar.csv; the erosion ruler bridge to 2.MD.A.1 is correct.
- **Candidate cells:** settled with day costs.
- **Shorter path:** present; see finding 3 on days 69 and 71.
- **Source map:** not applicable.
- **Stale notes:** `stale.py check` clean; finding 5 is the frame's.

## The lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| A unit's anchor is a topic, not a phenomenon | Met |
| A model is used before the unit that builds it | Met |
| Engineering design expectations appear in no unit | Met: K-2-ETS1-3 in unit 2, the erosion solution in its unit |
| Equipment assumed with no substitute or no-kit path | Met; heating is adult-only with a media path |

Rubric rows this layer owns: Gateway 1 at plan level and S1 met (finding 3 weakens it); 2a to 2c and S11 met; 2e met;
2h met (frames continue from grade 1, bar graphs replace picture rows); S6 part (finding 4); S7 met.

## What is right and should not be touched

- The two-week plant test with pre-grown seedlings and one variable at a time.
- The repeated habitat survey, and the pair "equal counts, different kinds".
- The erosion ruler bridge.
- Adult-only heating with distance rules.
- Every unit opening with retrieval of the grade 1 row it uses.

## What I could not judge

- Local land and water examples for the erosion unit are left to the unit plans, rightly.
- No outside source was fetched; standards rest on data/standards/ngss-pe-dimensions.csv and memory.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Paper items with sentence frames plus one observed station for build and plan parts | Each child is heard in the window | days.csv days 48, 49, 57, 58, 63, 64; scope-and-sequence.md |
| Eight fluency days take a new case; days 69 and 71 keep their content on the shorter path | Each day answers a question; nothing taught is folded away | days.csv |
| Cost allocations inside $50, weighted to units 2 and 3 | S6 | scope-and-sequence.md |
| Frame seam table says retrieval | Grade 1 is the year before | frame.md |
| Day 11 adds a short reteach of the kindergarten severe-weather content | Grade 1 retrieved only the practice | days.csv day 11 |

The mid-year check's move (finding 1) changes a calendar pin, so it is the lead's or fix pass's call, not settled
here.

## For Cory

- Grade 2 science does not fit three meetings a week as placed: two weeks hold four. The fix moves the mid-year check
  from week 17 to week 20 and keeps every day. If you would rather keep week 17, a few days would have to come out of
  the course. Recommended: move it.

## Sources

- data/standards/ngss-pe-dimensions.csv and the Next Generation Science Standards grade 2 expectations, from memory.
- docs/RUBRIC-SCIENCE.md, docs/agents/lenses/science.md.
- docs/courses/CALENDAR.md, data/plans/calendar.csv, the grade 2 math and ELA frames.

## For the source list

None.

## Across the band

- **Observation load is the band's main fault.** Kindergarten is serious and grades 1 and 2 are moderate. One rule
  across K to 2 fixes it: small groups of four or five, a per-child record, one spoken "why" per code (kindergarten)
  or paper items with frames (grade 2), builds started before the check day, and a named independent task for the
  rest of the class. Write it once in the frames' shared assessment wording so the unit plans do not invent three
  versions.
- **Rehearsal fold-ins.** Kindergarten (10) and grade 2 (8) fill their fold-in days with rehearsal; grade 1 mostly
  uses them for second cases (2 left). Grade 1's pattern is the model: a fold-in day is a new case that can be folded.
- **Hand-offs, K to grade 1:** the six kindergarten models are handed on and retrieved where used (sk-weather-watch on
  days 1 and 9, needs on day 10, sk-push-pull on days 28 and 43). Sound.
- **Hand-offs, grade 1 to grade 2:** retrieval on days 6, 11, 16, 27, 42, 51, 60 and 66. Sound; the skip-grade
  severe-weather content needs the short reteach above.
- **The engineering chain is clean:** K-2-ETS1-1 in kindergarten unit 3, K-2-ETS1-2 in grade 1 unit 2, K-2-ETS1-3 in
  grade 2 unit 2, and grade 1 leaves the two-device comparison for grade 2.
- **Data and language grow on purpose:** picture rows (K), three-group counts (grade 1), bar graphs (grade 2); sentence
  frames start in grade 1 unit 5 and continue.
- **Checks have one shape:** two lessons plus a respond lesson, with respond records passed to the next teacher.
- **Costs:** grade 1 allocates per unit; kindergarten and grade 2 should match it.
- **Time:** three meetings a week holds in kindergarten and grade 1 and breaks in grade 2 (finding 1).
- **Frame wording:** grades 1 and 2 frames both carry stale "readiness" words for rows that are retrieved.
