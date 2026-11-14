# Frame read: geometry (Math, Geometry), 2026-11-14

Expert cold read of docs/courses/geometry/frame.md, by the brief docs/pipeline/briefs/frame-read.md. I did not write
the frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md (applied by analogy),
  docs/pipeline/briefs/frame-write.md (the social studies lessons list), the values rule (docs/ADOPTION-BAR-SUBJECTS.md
  item 11), DESK-ANSWERS math entries 2026-11-12 and 13.
- The frame in full; its row in data/plans/frames.csv (geometry, 8, 160); data/courses.csv (geometry, grades 9 to 10).
- data/progressions/math.csv: all 28 geo- rows, the m7, m8 and alg1- rows they assume and the alg2- rows they hand
  on to; data/progressions/math-excluded.csv; the standard text for every owned code.
- Neighbours: docs/courses/algebra-i/frame.md (before), docs/courses/math-grade-8/frame.md (the grade 8 geometry
  picked up after a year), docs/courses/algebra-ii/frame.md (after), docs/courses/chemistry/frame.md (same year),
  docs/courses/biology/frame.md (earlier year).
- Base text, S:\CurioClass-sources\illustrative-math\hs-geometry: lesson files of units 1 to 8 (22, 15, 16, 11, 18,
  17, 14, 11 = 124), the "Standards by Lesson" table, all 11 modeling prompts, the full text of "2,000 Calories",
  and lesson content for Geo.2.13, 3.5, 6.16, 6.17 and 8.8 to 8.11.
- Earlier reviews as listed in docs/reviews/frame-algebra-i-2026-11-14.md.
- Gates: `python -X utf8 scripts/frame.py check geometry`: 0 failures (8 units, 160 days, 151 in units, 9 for checks
  and respond days). `scripts/plan.py check`: no failures. `scripts/stale.py check`: 0 failures. By script: unit
  days equal base lessons plus 3 (plus one added day in units 1, 2 and 6); the week calendar matches; 124 lessons
  placed; every geo- row placed once.

## Verdict

A sound frame: IM Geometry in its own order, every lesson and every modeling prompt placed, proof built in named
steps, a paper path for every construction, and 160 days with respond days. Judging focus across the three-course
sequence rather than Geometry alone is the right reading, but the 26 and 52 percent figures come from row tags and
do not measure time (finding 1). The one change that matters most for unit writers is the G-CO.C.10 placement:
the midsegment theorem is proved in base unit 3, not unit 6 (finding 2).

## Findings, most serious first

### 1. The focus figures do not measure time, though judging the sequence is sound (moderate; likely)

LAYER process, frame. REPEAT new (the same finding is made in the Algebra I and Algebra II reads today).

- **What is wrong.** "The bar, applied by analogy" counts unit days times the share of tagged rows: Geometry 26
  percent, the series 52. Row tags are set by any code in a row, owned or started (geo-scaling-area-volume is
  tagged through F-IF.C.7b and two tilde codes); rows are not days; and the tagged set has not been checked against
  the Publishers' Criteria table.
- **Evidence.** From IM's "Standards by Lesson" table, Geometry lessons that address at least one code in the
  progression's tagged set (N-RN, N-Q, A-SSE, A-APR, A-CED, A-REI, F-IF, G-SRT.B, G-SRT.C): 52 of 124 (42 percent);
  weighted by each lesson's share of tagged codes: 25 percent. Series: 60 percent by the first count, 45 by the
  second. Full method and per-course figures: docs/reviews/frame-algebra-i-2026-11-14.md, finding 3.
- **Is judging Geometry within the sequence sound?** Yes. The Publishers' Criteria and the adoption reviewers' high
  school tool judge focus on widely applicable prerequisites across the course sequence as designed (from memory;
  the table could not be opened today), and congruence, constructions and circle geometry are outside that list by
  design. What carries weight for Geometry is coherence: how much of it uses the algebra and quantity work. That is
  42 percent of its base lessons, and it is the number Geometry should report.
- **Fix.** Replace the focus sentence with the days-based measure (each day by the standards IM lists for it, each
  Curio Class day by the standards its plan names; the widely applicable list read from the source table), report
  Geometry's own share and the series share, and add the coherence reading: "about 42 percent of Geometry's base
  lessons use a widely applicable algebra or quantity standard". The three added proof and practice days (units 1,
  2, 6) can lift that share: the unit 6 coordinate proof-writing day is already algebra.

### 2. The midsegment theorem is placed in unit 6, but the base text proves it in unit 3 (moderate; firm)

LAYER frame, base text. REPEAT yes (standards in full and named where taught: lesson 4).

- **What is wrong.** Unit 6 says "The four triangle theorems of G-CO.C.10, now all proved: the angle sum (unit 1),
  isosceles base angles (unit 2), the midsegment, and medians meeting at one point." IM proves the midsegment in
  Geo.3.5 ("Splitting Triangle Sides with Dilation, Part 1", aligned to G-CO.C.10 and G-SRT.B.4); unit 3's text
  names no G-CO.C.10 work. Medians meeting at a point are in Geo.6.16 ("Weighted Averages in a Triangle"), which is
  right. IM also aligns G-CO.C.10 to Geo.7.5 to 7.7 (perpendicular and angle bisectors meeting in a point).
- **Why it matters.** A unit 6 writer would plan a midsegment proof that has no base lesson, and unit 3's
  end-of-unit assessment would not assess a theorem unit 3 actually proves.
- **Fix.** Unit 3 "What students learn": add "The segment joining two midpoints is parallel to the third side and
  half its length, proved with a dilation (a G-CO.C.10 theorem, base lesson 5; recorded in unit 6)". Unit 6: "the
  midsegment (unit 3), and medians meeting at one point (base lesson 16)". Unit 7 may add "the bisector
  concurrences (base lessons 5 to 7) use the G-CO.C.10 habit of proof" as review.

### 3. "2,000 Calories" is rightly cut, but its geometry can be kept (minor; judgment call)

LAYER base text. REPEAT new.

- **What is wrong.** The cut is sound: the prompt asks students to plan 2,000 calories a day, read food labels and
  list "food available close to your home", a calorie-counting task for teenagers and a window into a household's
  food access. Rule (d) of the values rule (grade level and life experience) and the frame's own sensitivity line
  support leaving it out. But the prompt's last part, siting a food co-op on a grid of stores, is the geometry
  (equidistance, perpendicular bisectors, G-CO.D.12 and G-MG.A.3) and carries none of the risk. For the lead item
  5 calls both cut prompts "left out as separate days" though only "On a Roll" is kept as an extension.
- **Fix.** Source map row: "cut: calorie counting and household food access; the siting task (where to place a new
  shop so it is fair to every neighbourhood) is kept as a candidate extension in unit 1, written by Curio Class
  with no food, calorie or home-address content". Unit 1 Check set adds: add that candidate. For the lead item 5:
  "One modeling prompt is cut ('2,000 Calories', sensitivity; its siting task kept as an extension) and one is an
  extension ('On a Roll', one prompt day a unit)."

### 4. The chemistry weeks in two unit reasons do not match the Chemistry frame (minor; firm)

LAYER frame. REPEAT yes (availability calendar mismatches in the science frame reads).

- **What is wrong.** Unit 4: "Chemistry in the same year leans on N-Q.A.2 and N-Q.A.3 from about week 17."
  Chemistry needs N-Q.A.3 in weeks 4 to 7 (chem-bulk-properties-forces, unit 2) and N-Q.A.2 by week 29
  (chem-resource-cost-benefit). Unit 5: "Chemistry's carbon-cycle stocks lean on units and density from about week
  17"; Chemistry needs them by week 27, and N-Q.A.1 already in weeks 9 to 11 (chem-conservation-mole). The
  Cross-subject table is right and every row has an if-later line, so no student is hurt; the unit reasons would
  mislead a writer.
- **Fix.** Unit 4: "Chemistry uses N-Q.A.3 from week 4 (retrieval from Algebra I) and N-Q.A.2 by week 29; this unit
  finishes both by week 17." Unit 5: "Chemistry uses unit-guided conversion from week 9 (retrieval from Algebra I)
  and stock-and-flow units by week 27; this unit finishes N-Q.A.1 by week 21."

### 5. Two standards are named in part (minor; firm)

LAYER frame. REPEAT yes (lesson 4).

- **What is wrong.** G-CO.C.11 lists "and conversely": a quadrilateral whose diagonals bisect each other is a
  parallelogram. Unit 2 names the forward theorems only; IM teaches the converse in Geo.2.13 ("Proofs about
  Parallelograms", the "if and only if" close). G-CO.D.12 and the constructions are named in full.
- **Fix.** Unit 2: "... diagonals bisect each other, and conversely a quadrilateral whose diagonals bisect each other
  is a parallelogram (base lesson 13), and rectangles are parallelograms with congruent diagonals (G-CO.C.11)."

### 6. The S-CP.B.8 keep is right, but its evidence is cited wrongly (minor; firm)

LAYER frame. REPEAT new.

- **What is wrong.** For the lead item 3 keeps S-CP.B.8, a (+) code, "because the base text teaches the
  multiplication rule in Geo.8 lessons 8, 10 and 11". IM aligns no Geometry lesson to S-CP.B.8. The rule
  P(A and B) = P(A given B) times P(B) is worked in lessons 8 to 10 (Conditional Probability; Using Tables for
  Conditional Probability; Using Probability to Determine Whether Events Are Independent); lesson 11 ("Probabilities
  in Games") does not use it. Unit 8's Check set adds also calls "Probabilities in Games" an extension, but it is
  base lesson 11, already counted in the unit's days.
- **Judgement on the keep.** Justified: it costs no day, the base lessons teach it, and a student who meets the
  rule here is better placed for Algebra II's inference unit. Assess it inside unit 8 only, not in the year-end
  check, since a (+) code is beyond the college and career line.
- **Fix.** For the lead item 3: "the base text works the rule in Geo.8 lessons 8 to 10, without aligning the code".
  Unit 8 Check set adds: replace the "Probabilities in Games" extension with another (for example, one game analysed
  with a two-way table and a tree both). Settled below.

### 7. "Construction: new here" overstates; compasses were used in grade 7 (minor; firm)

LAYER frame. REPEAT yes ("first" claims checked against the grade before: lesson 6).

- **What is wrong.** Models carried says construction is "New here". IM grade 7 unit 7 uses a compass to draw
  triangles from given sides (lessons 7 and 10), and the frame's own readiness day rebuilds m7-triangle-conditions.
  What is new is construction as a tool of proof.
- **Fix.** "New here as a reasoning tool (geo-constructions); compass drawing of triangles met in grade 7 (IM 7.7
  lessons 7 and 10, m7-triangle-conditions)".

## Checked and found right (do not undo)

- Every geo- row placed once; every Owned standards code is in those rows; every non-(+) Geometry code owned.
- The G-CO.C.9 split across units 1 and 2 (perpendicular bisector theorem in Geo.2.8 and 2.14) follows the base text
  and is named at both ends; the same pattern serves G-CO.C.10 once finding 2 is applied.
- The order: rigid motions before congruence, congruence before similarity, similarity before trigonometry,
  roots (unit 5) before coordinate geometry (unit 6), circle equations (unit 6) before circles (unit 7). Nothing is
  used before it is taught.
- F-IF.C.7b finished in unit 5 matches IM (Geo.5.4 to 5.7 and 5.18 are aligned to it) and the Algebra I start.
- N-Q.A.1 to A.3 finished here: IM aligns Geometry lessons to all three (for example Geo.1.9, 3.12, 4.1).
- Proof steps, paper-first constructions and the no-account tool rule are exactly what a teacher needs.
- The "2,000 Calories" sensitivity cut, and the illness and games notes in unit 8.
- Lessons from the social studies frames: 1, 2, 3 met; 4 missed in part (findings 2, 5); 5 met; 6 missed once
  (finding 7); 7 met (grade 8 rows picked up with readiness checks); 8 met (each Chemistry lean has an if-later
  line); 9 met (base lessons plus named extra days for proof); 10, 11, 12, 13, 14, 15 met.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Not applicable as written; the sequence reading is sound, the measure is not (finding 1) |
| A supporting cluster that does not practise major work | Met in part: units 3 to 6 practise algebra and quantity (42 percent of base lessons); units 1, 2, 7 and 8 are geometry and probability by design |
| A source map row with no decision | Met |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Keep the co-op siting part of "2,000 Calories" as a unit 1 candidate extension, rewritten with no food or home content | Keeps the geometry, drops the risk | docs/courses/geometry/frame.md (Source map, unit 1, For the lead 5) |
| Keep S-CP.B.8; assess it in unit 8 only | Taught in base lessons 8 to 10 at no extra cost; a (+) code stays off the year-end check | docs/courses/geometry/frame.md (unit 8, For the lead 3, Course-level checks) |
| Midsegment named in unit 3 (base lesson 5) | Where the base text proves it | docs/courses/geometry/frame.md (units 3 and 6) |
| Chemistry weeks in the unit 4 and 5 reasons corrected | The Chemistry frame's own weeks | docs/courses/geometry/frame.md |

## For Cory

- A high school bar (docs/RUBRIC-MATH-HS.md): as in the Algebra I read. Geometry would be judged by the series share
  plus its own coherence share, not held to a per-course line.
- The accelerated path (Geometry in grade 9) is already yours (For the lead 6); nothing here changes it.

## What I could not judge

- The Publishers' Criteria Table 1 itself (see the Algebra I read); in particular whether G-CO.C (proof about lines,
  triangles and parallelograms) is on the list: with G-CO.C counted, Geometry lessons addressing a listed code rise
  from 52 to 73 of 124 (42 to 59 percent).

## Sources

- IM Geometry, 1st edition, local copy: course/teachers__lessons_and_standards.md
  (https://im.kendallhunt.com/HS/teachers/2/lessons_and_standards.html), course/teachers__modeling_prompts*.md, and
  lesson files Geo.2.13, 3.5, 6.16, 6.17, 8.8 to 8.11; IM grade 7 unit 7 lessons 7 and 10.
- CCSS Mathematics, data/standards/ccss-math-standards.txt.
- Achieve the Core, widely applicable prerequisites page:
  https://achievethecore.org/page/701/widely-applicable-prerequisites-for-college-and-careers.
- High School Publishers' Criteria (2013) and the adoption reviewers' high school tool: from memory, as marked.

## For the source list

- As in the Algebra I read: IM's per-lesson "Standards by Lesson" pages, and the reach problem for the Publishers'
  Criteria table.
