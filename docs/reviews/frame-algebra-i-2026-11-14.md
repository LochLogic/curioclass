# Frame read: algebra-i (Math, Algebra I), 2026-11-14

Expert cold read of docs/courses/algebra-i/frame.md, by the brief docs/pipeline/briefs/frame-read.md. I did not
write the frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md (the bar, applied by analogy here),
  docs/pipeline/briefs/frame-write.md (including "Lessons from the social studies frames"), the values rule
  (docs/ADOPTION-BAR-SUBJECTS.md item 11, DESK-ANSWERS 2026-11-12), DESK-ANSWERS math entries 2026-11-12 and 13.
- The frame in full; its row in data/plans/frames.csv (algebra-i, 7, 160); data/courses.csv (`algebra-1`).
- data/progressions/math.csv: all 28 alg1- rows, the m6 to m8 rows they assume, and the geo- and alg2- rows they hand
  on to; data/progressions/math-excluded.csv; data/standards/ccss-math-standards.txt for every owned code.
- Neighbours: docs/courses/math-grade-8/frame.md (before), docs/courses/geometry/frame.md and
  docs/courses/algebra-ii/frame.md (after), docs/courses/biology/frame.md (same year), chemistry and physics frames
  (later years leaning back).
- Base text, from S:\CurioClass-sources\illustrative-math\hs-algebra-1: the lesson files of units 1 to 7 (16, 26,
  10, 18, 21, 17, 24 lessons = 132), the "Standards by Lesson" table (course/teachers__lessons_and_standards.md),
  the 9 modeling prompts and the full text of "Critically Examining National Debt"; hs-algebra-1-supports (13, 26,
  10, 18, 21, 16, 24 = 128 lessons) and its licence lines in MANIFEST.csv.
- Earlier reviews: docs/reviews/progression-math-*2026-11-13.md (not the reconcile), progression-cross reviews,
  frame-math-grade-2-codex-2026-11-14.md, frame-science-grade-1-2026-11-14.md and the social studies frame reviews
  (for REPEAT).
- Gates: `python -X utf8 scripts/frame.py check algebra-i`: 0 failures (7 units, 160 days, 151 in units, 9 for
  checks and respond days). `scripts/plan.py check`: no failures. `scripts/stale.py check`: 54 files, 0 failures.
  I checked by script what the gate does not: every unit's days equal its kept base lessons plus 3 (unit 1: 16
  lessons with 6 to 8 merged into one day, so 14 + 3 = 17), the week calendar in Cross-subject matches the day
  counts, and every non-(+) high school code is owned by exactly one row.

## Verdict

A sound frame that follows IM Algebra 1 in its own order, places every base lesson and all nine modeling prompts,
fits 160 days with a respond day after each check, and carries "if later" lines on every same-year lean. The
biggest risk is F-IF.C.9: the frame calls it "done in full" in unit 7 and proposes a row fix that hands the other
function families to Algebra II, but the Algebra II frame names no F-IF.C.9 work, so the standard ends in part.
The one change that matters most is to close that thread at both ends (the IM lessons that carry it are Alg1.6.14
and Alg1.7.23, and Algebra II needs named comparison work). The focus share (72 percent) is computed from row
tags in a way that does not hold up; a better measure is given in finding 3.

## Findings, most serious first

### 1. F-IF.C.9 is not taught in full anywhere, and the proposed row fix points at nothing (serious; firm)

LAYER frame, progression. REPEAT yes (standard narrowed or taught in part: social studies frame lesson 4).

- **What is wrong.** Unit 7 says F-IF.C.9 is "done in full" by reviewing unit 4 ("comparing graphs", base lesson
  4.9) and unit 5 (linear against exponential), then two quadratics. For the lead item 3 proposes the row limit
  "other families wait for Algebra II". But the Algebra II frame owns no F-IF.C.9 and names no comparison day, so
  "wait for Algebra II" hands the rest of the standard to no unit. The evidence is also off: IM aligns F-IF.C.9 to
  Alg1.6.14 ("Graphs That Represent Situations") and Alg1.7.23 only; Alg1.4.9 ("Comparing Graphs") is aligned to
  A-REI.D.11, F-IF.B.4 and F-IF.B.6 and compares two graphs (one representation), and Alg1.5.19 is aligned to
  F-LE.A.3, not F-IF.C.9. Lesson 6.14 is not mentioned in the frame at all.
- **Why it matters.** The standard has no family limit ("two functions each represented in a different way").
  A unit 7 writer would build one comparison day on quadratics with a review of graph-to-graph work, which an
  adoption reviewer would mark as partial; the polynomial, exponential-logarithmic and trigonometric cases of
  Algebra II would never be compared across representations.
- **Fix.** (a) Unit 6 "What students learn": add "Comparing two quadratic functions given different ways starts
  here (base lesson 14; F-IF.C.9 is owned in unit 7)". (b) Unit 4: replace "Comparing two functions given different
  ways starts here (base lesson 9), owned in unit 7" with "Base lesson 9 compares two graphs, which prepares
  F-IF.C.9 (unit 7)". (c) Unit 7: keep the comparison day on base lesson 23, comparing a quadratic with a linear
  or exponential function given another way, and drop "done in full"; say "finished for the Algebra I families
  (linear, exponential, quadratic, absolute value); Algebra II finishes it". (d) For the lead item 3, new row
  text for alg1-vertex-form-max-min: "Limits: comparisons across linear, exponential, quadratic and absolute value
  functions (IM Alg1.6 lesson 14, Alg1.7 lesson 23); Algebra II revisits it with polynomial, logarithmic and
  trigonometric functions (alg2-factors-zeros-graphs, alg2-exp-log-graphs, alg2-trig-functions-graphs)". Ownership
  stays here (as with F-BF.B.4a); the Algebra II frame names the revisit days (see
  docs/reviews/frame-algebra-ii-2026-11-14.md finding 1 for the receiving end). Moving ownership of F-IF.C.9 to an
  Algebra II row instead would move a standard between courses, which is Cory's (For Cory).

### 2. F-LE.A.3's quadratic and power-function comparison sits in unit 5, before quadratic functions (moderate; firm)

LAYER frame, base text. REPEAT yes (a skill used before it is taught: lesson 5).

- **What is wrong.** Unit 5 says an increasing exponential "eventually exceeds a linear, a quadratic and a simple
  power function such as x cubed (F-LE.A.3 ... in base lesson 19)", and the Source map adds "the power-function
  comparison ... (x cubed and x to the fourth) as one added activity" to Alg1.5.19. IM lesson 5.19 ("Which One
  Changes Faster?") compares linear and exponential only (no quadratic or power term in it). IM puts the quadratic
  case in Alg1.6.4 ("Comparing Quadratic and Exponential Functions", aligned to F-LE.A.3, including 1,000x squared
  against 2 to the x). The frame lists lesson 6.4 only "as review".
- **Why it matters.** Quadratic functions are unit 6's subject. A unit 5 day comparing 2 to the x with x squared
  and x cubed uses a function family before it is taught; a busy writer will build it as written.
- **Fix.** Unit 5: "F-LE.A.3, the linear case, in base lesson 19 (finished in unit 6)". Unit 6: add "An increasing
  exponential eventually exceeds a quadratic and, as one added activity after base lesson 4, a power function such
  as x cubed (F-LE.A.3, finished here)". Source map: move the added activity note from Alg1.5 to Alg1.6 lesson 4,
  and change "as review" to "finishes F-LE.A.3". No day count changes (the activity sits inside the lesson).

### 3. The focus share is built on row tags that do not measure time (moderate; likely)

LAYER process, frame. REPEAT new.

- **What is wrong.** "The bar, applied by analogy" counts each unit's days times the share of its rows whose notes
  say "Widely applicable prerequisite", giving 72 percent. Three problems. (a) A row is tagged when any code in
  it, owned or started with a tilde, is in the tagged clusters: alg1-exponential-functions and
  alg1-percent-change-interest own no code at all (every code is a tilde) yet count as fully tagged, while
  alg1-linear-vs-exponential (F-LE.A.1 to A.3) and alg1-inverse-functions (F-BF.B.4) count as zero. (b) Rows are not
  days: unit 5's three rows weigh the same though IM spends 21 lessons on them. (c) The tagged set (N-RN, N-Q,
  A-SSE, A-APR, A-CED, A-REI, F-IF, G-SRT.B, G-SRT.C, from the rows) has not been checked against the source table
  (High School Publishers' Criteria, Table 1); I could not reach that table (see Sources), so whether F-BF, F-LE or
  G-CO.C belong is open.
- **Evidence.** Using IM's own "Standards by Lesson" tables and the same tagged set, I counted base lessons that
  address at least one tagged code: Algebra I 102 of 132 (77 percent), Geometry 52 of 124 (42), Algebra II 73 of
  120 (61); the three-course series 227 of 376 (60). Weighted by the share of each lesson's codes that are tagged:
  65, 25, 45, series 45. Adding F-BF and F-LE: 81, 42, 74, series 66. The frame's figures (72, 26, 57, series 52)
  sit inside this spread by chance of method, not by measurement.
- **Is the sequence reading sound?** Yes in principle. The High School Publishers' Criteria and the adoption
  reviewers' high school tool judge focus on the widely applicable prerequisites over the course sequence as
  designed, not per course (from memory; the source could not be opened today), and geometry content is mostly
  outside that list by design. Holding Geometry alone to a 65 percent line would push algebra into it for no
  student gain. What does not hold is the number: under a fractional count the series falls under half.
- **Fix (a better measure).** Count lesson days, not rows: each base day by the standards IM lists for that
  lesson (course/teachers__lessons_and_standards.md), each Curio Class day by the standards its plan names. Read
  the list of widely applicable standards from the Publishers' Criteria table itself, not from the row tags.
  Report per course and across the three courses both "days that address one or more" and the fractional share;
  the reading is a majority across the series by the first count, with the fractional count shown beside it.
  Add a coherence reading for courses below half: the share of their days that also use a widely applicable
  algebra or quantity code (Geometry: 42 percent). Replace the frame's sentence with the counted figures once the
  table is read, and carry the method into the docs/RUBRIC-MATH-HS.md the frame already proposes.

### 4. The national debt prompt is cut wider than the values question needs (moderate; judgment call)

LAYER base text. REPEAT new.

- **What is wrong.** The Source map cuts "Critically Examining National Debt" for "political framing" and replaces
  it with an unwritten savings-plan prompt "on the same standards (F-LE.A.1c, F-IF.C.8b started)". Only version 1
  of the prompt asks a policy question ("What would you suggest the government do to reduce the growing debt?").
  Version 2 asks only for a linear or exponential model and a judgement of its accuracy; version 3 supplies the
  debt figures (1987 to 2017, every other year) and asks for an exponential model. The prompt's own standards are
  F-BF.A.1, F-LE.A.1, F-LE.A.2 and F-LE.B.5, not the two the replacement names.
- **Judgement.** Under the values rule, facts and backed sources decide claims (rule b); fitting a model to public
  debt data and judging its limits is that kind of work and is the strongest real-data exponential task in unit
  5. The policy question is the only part that invites advocacy. Cutting the whole prompt loses real data and the
  F-LE.A.2 and F-LE.B.5 practice, and adds a writing job (a new prompt and rubric).
- **Fix.** Settled below: keep version 3 (or 2 where students can look up data), drop version 1's last question
  and the launch's video suggestion, and frame the teacher note on debt as a share of national income as IM does.
  Source map row: "keep (version 3, no policy question)". Remove For the lead item 5 and the unit 5 sensitive-topic
  line about the replacement. If a savings prompt is still wanted, it is a candidate extension tagged F-BF.A.1,
  F-LE.A.2 and F-LE.B.5.

### 5. Two grade 8 handoffs have no Algebra I end, and the grade 8 frame's note on them is stale (minor; firm)

LAYER frame, progression, process. REPEAT yes (both ends of every handoff, lesson 7; stale "frame not written",
docs/reviews/frame-science-grade-1-2026-11-14.md finding 5).

- **What is wrong.** The grade 8 frame (For the lead item 6) asks for m8-proportional-compare to hand on to
  alg1-linear-equation-graphs, with the matching assumes on the Algebra I row; neither row is changed yet and the
  Algebra I frame does not carry its end. The Algebra I frame's own Models table even names m8-proportional-compare
  as where function-table was last carried. The grade 8 frame also says m8-scientific-notation hands on to nothing
  "because N-Q.A.3 has no row" and calls the high school frames "not written": both are now false (N-Q.A.3 is
  owned by geo-solving-right-triangles and started in alg1-scatter-linear-models, and the frames exist). No IM
  Algebra 1 or Geometry lesson uses scientific notation, so no math row should invent a link.
- **Fix.** Algebra I For the lead, new item: "Row change with grade 8: add m8-proportional-compare to the assumes
  of alg1-linear-equation-graphs (and alg1-linear-equation-graphs to its hands_on); add the matching line to Seams,
  unit 2, next grade, direct." Grade 8 frame (for its fixer): replace "Handed on to Algebra I and Geometry (where
  the middle school threads end; their frames are not written, so the rows are named, not their units)" with
  "Handed on to Algebra I and Geometry (where the middle school threads end)"; replace the scientific notation
  cell with "Ends in core math here; Chemistry (grade 10) retrieves it for particle counts (8.EE.A.4)".

### 6. Two "why here" lines give Biology weeks that the Biology frame does not (minor; firm)

LAYER frame. REPEAT yes (availability calendar mismatches in the science frame reads).

- **What is wrong.** Unit 2: "Biology's population model leans on naming quantities by about week 5"; Biology
  needs it by week 13 (bio-population-carrying-capacity, unit 5). Unit 5: "Biology's population simulation leans
  on a stepping rule by about week 17"; Biology needs it by week 29 (bio-biodiversity-simulation, unit 10). The
  Cross-subject table itself is right (available from about week 5 and week 19; each has an if-later line).
- **Fix.** Unit 2: "Biology's population model leans on naming quantities by week 13 (Biology unit 5)". Unit 5:
  "Biology's biodiversity simulation leans on a stepping rule by week 29 (Biology unit 10)".

### 7. Two owned standards are named only in part (minor; firm)

LAYER frame. REPEAT yes (lesson 4).

- **What is wrong.** F-IF.C.8a asks factoring and completing the square to show "zeros, extreme values, and
  symmetry"; unit 7 names the maximum or minimum only (zeros are named under A-SSE.B.3a, symmetry nowhere).
  F-BF.B.4 and F-BF.B.4a are listed as owned in unit 4 "for linear functions"; the frame does say the cubing case
  is in Algebra II unit 3, which is the right handoff, but the Owned standards cell reads as complete.
- **Fix.** Unit 7: "(A-SSE.B.3b, F-IF.C.8a: zeros, the maximum or minimum, and the line of symmetry, read in
  context)". Unit 4 Owned standards: keep the codes and add to the text "taught in full for linear functions; the
  nonlinear case finishes in Algebra II unit 3 (named there)".

### 8. The course id differs between the frame and the course list (minor; firm)

LAYER process. REPEAT new.

- **What is wrong.** The folder and data/plans/frames.csv use `algebra-i`; data/courses.csv and the frame's first
  line use `algebra-1` (Algebra II likewise: `algebra-ii` and `algebra-2`). The scope and sequence step writes
  data/plans/<course>/, so one of the two ids will be wrong there.
- **Fix.** For the lead: pick one id per course (the courses.csv id, `algebra-1` and `algebra-2`, keeps data ids
  stable) and rename the frame folders before step 3, or record the mapping in data/courses.csv notes.

## Checked and found right (do not undo)

- Every one of the 28 alg1- rows sits in exactly one unit; every Owned standards code is in those rows; units in
  IM order; day counts are base lessons plus readiness, modeling and assessment days; 151 + 9 = 160.
- Every IM Algebra 1 lesson is placed (132); the merge of lessons 6 to 8 is sound (IM aligns no standard to them;
  they teach a spreadsheet tool, and a paper path is given). All nine modeling prompts are placed; "Planning a
  Vacation" kept as an extension is a fair call (F-IF.B.4 is modeled again in "Designing a Fountain").
- The supports course is CC BY 4.0 (MANIFEST.csv) and is kept outside the 160 days; no gated or NC material used.
- Readiness checks sit in the first unit that needs each earlier skill (grade 6 and 7 statistics in unit 1, grade
  7 inequalities in unit 2, grade 7 percent in unit 5, grade 8 roots in unit 7). Model reactivations are named.
- The "started here, finished there" convention (A-CED, A-REI.A.1, F-BF.B.3, F-IF.B.4, N-Q) is named at both ends.
- Same-year Biology and ELA 9 leans each carry an "if later" line; later-year leans are listed.
- Lessons from the social studies frames: 1 (respond days) met; 2 (Candidate:) met; 3 (45 to 50 minutes, five a
  week, 32 weeks) met; 4 missed in part (findings 1, 7); 5 missed once (finding 2); 6 met; 7 missed once
  (finding 5); 8 met; 9 met (days follow IM's lessons, a defensible load measure in a base-text course); 10 met;
  11 met (contexts picked, survey screened); 12 met; 13 met; 14 met; 15 met.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Not applicable as written (no high school bar); the analogy's measure is unsound (finding 3); the plan itself is IM's order and is not the problem |
| A supporting cluster that does not practise major work | Met: unit 3 fits lines with unit 2's equations; unit 1 is the statistics a modeling standard asks for |
| A source map row with no keep, split, merge, cut or ours decision | Met: every row has one |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Keep "Critically Examining National Debt", version 3 (version 2 where data lookup works), without version 1's policy question | Real public data, the prompt's own F-LE.A.2 and F-LE.B.5 practice; only the policy question raised the values issue | docs/courses/algebra-i/frame.md (unit 5, Source map, For the lead 5) |
| F-IF.C.9 thread starts at Alg1.6 lesson 14 and closes in unit 7 on lesson 23 | IM's own alignments | docs/courses/algebra-i/frame.md (units 4, 6, 7) |
| Biology weeks in the unit 2 and unit 5 reasons: 13 and 29 | The Biology frame's own weeks | docs/courses/algebra-i/frame.md |

## For Cory

- F-IF.C.9 (compare two functions given different ways): the fix keeps it owned by Algebra I and has Algebra II
  revisit it with its own function families. The alternative, moving ownership to Algebra II, moves a standard
  between courses and is yours to pick. Recommendation: keep it in Algebra I.
- Finding 2 finishes F-LE.A.3 in unit 6 instead of unit 5, following IM's own lesson 6.4. It touches which unit a
  standard is finished in, so it is listed for a yes; the ownership row does not change.
- The accelerated path (Algebra I in grade 8) and a two-year Algebra I are audience and scope questions, already
  raised in the frame (For the lead 4 and 7); nothing in this read changes them.
- A high school bar (docs/RUBRIC-MATH-HS.md) is the lens gap. Whether to write it from the Publishers' Criteria and
  the adoption reviewers' high school tool is Cory's call; finding 3 gives the measure it should use.

## What I could not judge

- The Publishers' Criteria Table 1 itself (which high school standards are "widely applicable"): the Achieve the
  Core page loads but its table file did not come through as text; a scripted download was refused. The tagged set
  above is the progression's, not checked against the table.
- The ELA 9 frame's week for e9-ri-argument-evaluate (the frame's reciprocal line reads well; I did not open ELA 9).

## Sources

- IM Algebra 1, 1st edition, local copy: course/teachers__lessons_and_standards.md (per-lesson alignments, used for
  findings 1 to 3), course/teachers__modeling_prompts*.md (prompt list and standards), unit lesson files
  (5.19, 6.4, 4.9, 6.14, 7.23 titles and content). https://im.kendallhunt.com/HS/teachers/1/lessons_and_standards.html
- CCSS Mathematics standard text, data/standards/ccss-math-standards.txt (standards in full).
- Achieve the Core, "Widely applicable prerequisites for college and careers":
  https://achievethecore.org/page/701/widely-applicable-prerequisites-for-college-and-careers (what the list is for;
  its table file https://achievethecore.org/file/1210 could not be read as text).
- High School Publishers' Criteria for the CCSS for Mathematics (2013), Table 1, and the adoption reviewers' high
  school review tool (focus judged over the series): from memory, marked so in finding 3.

## For the source list

- IM's "Standards by Lesson" page for each high school course (local: course/teachers__lessons_and_standards.md)
  gives per-lesson alignments; it is the right data for any days-based focus count. Not in docs/APPROACH-SOURCES.md.
- The High School Publishers' Criteria PDF at its old corestandards.org and achievethecore.org/content/upload
  addresses now returns an HTML page; the table is reachable only as achievethecore.org/file/1210 (a PDF that a
  browser opens; scripted fetches got HTML or unreadable streams).
