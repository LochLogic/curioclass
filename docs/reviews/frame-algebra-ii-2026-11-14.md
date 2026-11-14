# Frame read: algebra-ii (Math, Algebra II), 2026-11-14

Expert cold read of docs/courses/algebra-ii/frame.md, by the brief docs/pipeline/briefs/frame-read.md. I did not
write the frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md (applied by analogy),
  docs/pipeline/briefs/frame-write.md (the social studies lessons list), the values rule, DESK-ANSWERS math entries
  2026-11-12 and 13.
- The frame in full; its row in data/plans/frames.csv (algebra-ii, 7, 160); data/courses.csv (`algebra-2`, grades
  10 to 11; electives precalculus, statistics, calculus).
- data/progressions/math.csv: all 26 alg2- rows, the alg1-, geo- and m7- rows they assume;
  data/progressions/math-excluded.csv; the standard text for every owned code and for the deferred (+) codes named
  in "Where each thread ends".
- Neighbours: docs/courses/algebra-i/frame.md and docs/courses/geometry/frame.md (before), docs/courses/physics/frame.md
  (same year), chemistry (earlier year), and the economics and US government leans as the frame records them.
- Base text, S:\CurioClass-sources\illustrative-math\hs-algebra-2: lesson files of units 1 to 7 (11, 26, 19, 18, 11,
  19, 16 = 120), the "Standards by Lesson" table, all 8 modeling prompts, and lesson content for Alg2.2.16 to 2.21,
  5.4 to 5.7, 6.15 to 6.19, 7.16.
- Earlier reviews as listed in docs/reviews/frame-algebra-i-2026-11-14.md.
- Gates: `python -X utf8 scripts/frame.py check algebra-ii`: 0 failures (7 units, 160 days, 151 in units, 9 for
  checks and respond days). `scripts/plan.py check`: no failures. `scripts/stale.py check`: 0 failures. By script:
  unit days equal base lessons plus 3, plus 2 named added days in units 2, 3, 4, 6, 7; the week calendar matches;
  120 lessons placed; every alg2- row placed once; every non-(+) high school code is owned somewhere in the
  progression.

## Verdict

A sound frame that closes the core sequence well: IM Algebra 2 in its own order, every lesson and prompt placed,
readiness checks for the Algebra I skills that skip Geometry, added days that each have a stated job, and a clear
table of where every thread ends for the electives. The biggest risk is F-IF.C.9: Algebra I hands the comparison
of other function families to this course, and this frame never names it, so the standard ends in part (finding
1). The focus figure (57 percent) rests on row tags and should be replaced by the days-based measure (finding 2).

## Findings, most serious first

### 1. F-IF.C.9 has no Algebra II end (serious; firm)

LAYER frame, progression. REPEAT yes (standard taught in part: lesson 4; both ends of a handoff: lesson 7).

- **What is wrong.** F-IF.C.9 ("compare properties of two functions each represented in a different way") is owned
  by alg1-vertex-form-max-min, whose row says "Limits: quadratics only"; the Algebra I frame proposes "other families
  wait for Algebra II". This frame owns, revisits and names no F-IF.C.9 work, and IM Algebra 2 aligns no lesson to
  it. So polynomial, exponential against logarithmic, and trigonometric functions are never compared across
  representations.
- **Why it matters.** It is the one function standard that pulls the families together; an adoption reviewer reading
  the series would find it taught only for the Algebra I families.
- **Fix.** Name a revisit inside existing days (no day count change): unit 2, "compare a polynomial given by its
  graph with one given in factored form (zeros, end behaviour), revisits F-IF.C.9"; unit 4, "compare an exponential
  given by a table with a logarithmic function given by an equation (base lesson 15), revisits F-IF.C.9"; unit 6,
  "compare a sine model given by a graph with one given by an equation (base lesson 17, 'Comparing
  Transformations'), finishing F-IF.C.9 (owned by alg1-vertex-form-max-min)". Add each to the readiness or
  practice task of that lesson, and put one comparison item on the unit 7 year-end check. The row change on the
  Algebra I side is in docs/reviews/frame-algebra-i-2026-11-14.md finding 1.

### 2. The focus figure does not measure time (moderate; likely)

LAYER process, frame. REPEAT new (the same finding is made in the Algebra I and Geometry reads today).

- **What is wrong.** 57 percent is unit days times the share of rows tagged "Widely applicable prerequisite". Tags are
  set by any code in the row, owned or started; alg2-transformations-functions (F-BF.B.3) and alg2-logarithms
  (F-LE.A.4) count as zero, alg2-exp-log-graphs counts in full through A-REI.D.11.
- **Evidence.** From IM's "Standards by Lesson" table, Algebra II lessons addressing a code in the tagged set: 73 of
  120 (61 percent); weighted share: 45 percent; with F-BF and F-LE counted: 74 percent. Method and series figures:
  docs/reviews/frame-algebra-i-2026-11-14.md, finding 3.
- **Fix.** As in that finding: a days-based count from IM's alignments and the Publishers' Criteria table, reported
  per course and for the series; replace the frame's sentence when counted.

### 3. A-CED.A.1 is called finished in unit 2, before its exponential case (minor; firm)

LAYER frame. REPEAT yes (lesson 4).

- **What is wrong.** Unit 2 says "Equations in one variable created from contexts (A-CED.A.1, finished here)". The
  standard includes equations from "simple rational and exponential functions". IM aligns A-CED.A.1 to Alg2.2.20 and
  2.21 (rational) only; the exponential equations from contexts come in unit 4 (base lessons 8 to 15, solved with
  logarithms).
- **Fix.** Unit 2: "(A-CED.A.1, the rational case; finished in unit 4)". Unit 4: add "Equations created from
  exponential contexts and solved with logarithms (A-CED.A.1, finished here)".

### 4. Two finishing standards are named in part (minor; firm)

LAYER frame. REPEAT yes (lesson 4).

- **What is wrong.** F-BF.B.3 ends with "recognizing even and odd functions from their graphs and algebraic
  expressions"; unit 5 says "even and odd functions from symmetry". IM covers both (Alg2.5.5 "Some Functions Have
  Symmetry", 5.6 "Symmetry in Equations"). F-BF.B.4a's own examples are 2 times x cubed and (x + 1)/(x - 1); the unit
  3 added day names the cube only.
- **Fix.** Unit 5: "even and odd functions from their graphs and from their equations (base lessons 5 and 6)". Unit
  3 added day: "the cube root undoes cubing (2 times x cubed = c), and one simple rational inverse, (x + 1)/(x - 1),
  done by solving f(x) = c", which uses unit 2's rational equations. No day change.

### 5. The course id differs between the frame and the course list (minor; firm)

LAYER process. REPEAT yes (docs/reviews/frame-algebra-i-2026-11-14.md finding 8, the same day).

- **What is wrong.** The folder and data/plans/frames.csv use `algebra-ii`; data/courses.csv and the frame's first
  line use `algebra-2`.
- **Fix.** As in the Algebra I read: one id per course before the scope and sequence writes data/plans/<course>/.

## Checked and found right (do not undo)

- Every alg2- row placed once; every Owned standards code is in those rows; days are base lessons plus readiness,
  modeling and assessment days, plus ten named added days; 151 + 9 = 160; weeks match.
- Every IM Algebra 2 lesson and all eight modeling prompts are placed; no cut was needed. "Heart Rates" (Alg2.7.16)
  kept as opt-in with a supplied data set is the right call.
- F-IF.C.7d, a (+) code, kept: justified. Alg2.2.17 to 2.19 graph rational functions with asymptotes, zeros, holes
  and end behaviour (IM aligns them to F-IF.C.7 and A-APR.D.6, not to 7d), so it costs no day. Assess it in unit 2
  only, not on the year-end check.
- The F-BF.B.4a finish (the cube root inverse) as an "ours" day: IM Algebra 2 aligns no lesson to F-BF.B.4, so the
  added day is what makes the Algebra I standard whole. Named at both ends.
- Readiness after the Geometry year: every Algebra I skill this course uses has a readiness check in the first unit
  that uses it, and m7-random-samples is rebuilt in unit 7 (three years away).
- Unit 5 at 14 days with no added day: the four codes it finishes all start in Algebra I or earlier units, and all
  11 base lessons are aligned to them (F-BF.B.3 in ten of them); its share is right.
- Unit 2 at 31 days as one unit, IM's own unit: keep (settled below); its section breaks give natural checkpoints.
- "Where each thread ends" is the right shape for the electives and names the deferred (+) codes correctly.
- Same-year Physics lean (waves) and the Economics and US Government leans each carry an if-later line.
- Lessons from the social studies frames: 1, 2, 3 met; 4 missed in part (findings 1, 3, 4); 5 met; 6 met; 7 missed
  once (finding 1); 8 met; 9 met; 10, 11, 12, 13, 14, 15 met.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Not applicable as written; measure unsound (finding 2), plan sound |
| A supporting cluster that does not practise major work | Met: unit 6 transforms with unit 5's moves; unit 7 fits normal curves and uses function reading |
| A source map row with no decision | Met |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| F-IF.C.9 revisits placed in base lessons Alg2.4.15 and Alg2.6.17 and one unit 2 task, finishing in unit 6 | These lessons already put the functions side by side; no day change | docs/courses/algebra-ii/frame.md (units 2, 4, 6) |
| The F-BF.B.4a added day also takes the (x + 1)/(x - 1) inverse | The standard's own example, using unit 2's rational equations | docs/courses/algebra-ii/frame.md (unit 3) |
| Unit 2 stays one unit (31 days); no split | IM's own unit; splitting adds two days for no new teaching | docs/courses/algebra-ii/frame.md (For the lead 2) |
| F-IF.C.7d assessed in unit 2 only | A (+) code stays off the year-end check | docs/courses/algebra-ii/frame.md (unit 2, Course-level checks) |

## For Cory

- A high school bar (docs/RUBRIC-MATH-HS.md), as in the Algebra I read.
- Whether F-IF.C.9 stays owned by Algebra I (the fix above) or moves to an Algebra II row: moving a standard between
  courses is yours. Recommendation: keep it in Algebra I, finished here by revisits.

## What I could not judge

- The Publishers' Criteria Table 1 (see the Algebra I read).
- The Economics and US Government frames' own weeks for the loan formula and poll leans (not opened; the frame's
  if-later lines make either order safe).

## Sources

- IM Algebra 2, 1st edition, local copy: course/teachers__lessons_and_standards.md
  (https://im.kendallhunt.com/HS/teachers/3/lessons_and_standards.html), course/teachers__modeling_prompts*.md, and
  the lesson files named above.
- CCSS Mathematics, data/standards/ccss-math-standards.txt.
- Achieve the Core, widely applicable prerequisites page:
  https://achievethecore.org/page/701/widely-applicable-prerequisites-for-college-and-careers.
- High School Publishers' Criteria (2013) and the adoption reviewers' high school tool: from memory, as marked.

## For the source list

- As in the Algebra I read.
