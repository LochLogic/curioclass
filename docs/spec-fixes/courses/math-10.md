# Spec fixes: math, grade 10

9 tools: 6 rework, 3 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (8), Close the guessable check (7), Add the missing part (9), Add a model or a guide (1), Reach five items that differ (7), Put it on the main path (1), Teach the code or drop it (2), Sensitivity read (1).

Shape for this course: ../../agents/catalog/shape/math-10.md.

## Circle Theorem Explorer

- Spec: `tools/circle-theorem-explorer/spec.md` . Module: math-10-circles. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Predict (optional) hides only the locked value while the Measures layer still draws the numbers on the figure; a wrong guess retries free
- **G-C.A.2** (shown, in Cards 1-7; locked-line banner): Drag points, watch the locked line, press Break it and Fix it
  - To do: the tool does the "identify" step: the student must do it
  - Parts of the standard the student never does (must add):
    - describe the relationship in own words (the banner states it)
    - circumscribed angles
    - identify the relationship without the tool naming it
- **G-C.A.3** (shown, in Card 8 (circles of a triangle), card 5 (cyclic quadrilateral)): Drag a triangle and watch Around and Inside circles; drag cyclic vertices
  - To do: the tool does the "construct" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - construct the inscribed and circumscribed circles
    - prove the quadrilateral angle property
- **G-C.A.1** (shown, in Card 9): Press Match to slide then dilate one circle onto another
  - To do: the tool does the "prove" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - prove that all circles are similar
    - carry out the slide and the dilation themselves
- **G-C.B.5** (shown, in Cards 10 and 11): Move radius and angle, press Unroll, read arc over radius
  - To do: the tool does the "derive" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - derive the proportionality themselves
    - define radian as the constant of proportionality
    - derive the sector area formula
- **G-C.A.4** (claimed, in Card 6): Equal tangents seen from an outside point; no construction
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "construct" step: the student must do it
  - Parts of the standard the student never does (must add):
    - construct a tangent from an outside point
- The module also lists codes this tool does not carry: G-C.A.4.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Spec maps cards 1-7 to A.2, but card 5 is the cyclic quadrilateral (A.3 wording)
  - Predict is optional so no code reaches explored or taught
  - beatable inferred: spec does not say whether Measures hides during Predict
  - minutes midpoint of 10 to 35

## Coordinate Proof Lab

- Spec: `tools/coordinate-proof-lab/spec.md` . Module: math-10-coordinate-geometry. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Prove: extra cells never fail a proof, so tapping every table cell and choosing the conclusion passes; wrong conclusions say which light is off
  - Partition: Skip guess shows P, and a tap within 0.25 of P counts, so tapping by eye on the grid passes without computing
- **G-GPE.B.4** (practiced, in Prove mode; Circle point test): Tap table cells for a proof, pick a conclusion, press Check
  - Parts of the standard the student never does (must add):
    - compute the lengths and slopes themselves (table gives them)
    - write the algebraic argument
    - disprove a claim by computing
- **G-GPE.B.5** (shown, in Quad lab, Prove table): Read slopes and mark lights in the measuring table
  - To do: the tool does the "prove" step: the student must do it
  - Parts of the standard the student never does (must add):
    - prove the slope criteria
    - find an equation of a parallel or perpendicular line through a point
- **G-GPE.B.6** (practiced, in Partition mode): Set ratio m:n, tap where P should land, press Show
  - Parts of the standard the student never does (must add):
    - compute the coordinates of P (student taps by eye)
    - state P as exact fractions
- **G-GPE.B.7** (shown, in Quad lab measuring table): Drag corners and read perimeter and shoelace area
  - To do: the tool does the "compute" step: the student must do it
  - Parts of the standard the student never does (must add):
    - compute perimeter and area themselves
    - triangles (only quadrilaterals in Quad lab)
- **G-GPE.A.1** (shown, in Circle mode, Complete the square): Drag center and rim, read equation; press Next step on a general form
  - To do: the tool does the "derive" step: the student must do it
  - Parts of the standard the student never does (must add):
    - derive the equation using the Pythagorean Theorem
    - do the completing-the-square steps themselves
- The module also lists codes this tool does not carry: G-GPE.A.2, G-GPE.A.3.
- The read was unsure about (check these against the spec; the read may be wrong):
  - B.4 practiced because the all-cells tray passes; no Can it be beaten section in spec
  - G-GPE.B.6 check is distance feedback only
  - kinds fluency 0: measuring is done by the table
  - minutes midpoint of 15 to 40

## Packaging Challenge

- Spec: `tools/packaging-challenge/spec.md` . Module: math-10-modeling-with-geometry. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Reveal best and Show curve are available at any time and print the best radius and height, so a student can copy them with no reasoning
- **G-MG.A.3** (taught, in Orders O1-O6, graph, Reveal best): Drag radius or side at fixed volume, plot dots, compare with the best
  - Parts of the standard the student never does (must add):
    - compute surface area and volume themselves (readouts give each piece)
    - derive the best shape by formula
    - typographic grid systems
- **G-MG.A.1** (shown, in Shelf mode): Tap four real cans and read the cylinder comparison
  - To do: the tool does the "describe" step: the student must do it
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - build the cylinder model of an object themselves (cans come pre-modeled)
    - objects other than cans
- **G-MG.A.2** (shown, in Case mode): Press Pack the case and read fill and grams per case
  - To do: the tool does the "apply" step: the student must do it
  - Parts of the standard the student never does (must add):
    - compute fill or density themselves
    - rates such as people per square mile
- The read was unsure about (check these against the spec; the read may be wrong):
  - A.3 taught: guide is the live graph, check is the Reveal best exact minimum; no pass or fail gate (notes: explorer, no mastery score)
  - minutes midpoint of 15 to 40

## Medical Test Paradox

- Spec: `tools/medical-test-paradox/spec.md` . Module: math-10-probability-rules. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Reach five items that differ, Sensitivity read.
- **S-CP.A.1** (shown, in Town; addition-rule panel in Table): Watch the town sort into four groups; Positives only
  - To do: the tool does the "describe" step: the student must do it
  - Parts of the standard the student never does (must add):
    - describe events with or, and, not themselves
    - unions, intersections and complements in notation
- **S-CP.A.2** (shown, in Cases C7; Second test assumption): Predict the coin test case and see the share stay at 1 percent
  - To do: the tool does the "understand" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - test P(A and B) = P(A)P(B)
    - decide independence for given events
- **S-CP.A.3** (explored, in Town sliders and Predict beat; Cases): Set rates, predict the share of positives who have it, reveal
  - To do: see-why code, fine here; the unit must add: Student writes P(A and B)/P(B) from the table counts, and tests independence as P(A given B) = P(A) on more than one pair.
  - Parts of the standard the student never does (must add):
    - write P(A and B)/P(B)
    - interpret independence as P(A given B) = P(A) outside the coin case
- **S-CP.A.4** (taught, in Table mode, Which question?): Tap a table row or column to divide by it; match questions to fractions
  - Parts of the standard the student never does (must add):
    - construct the two-way table
    - use the table to decide independence
    - collect data from a sample
- **S-CP.A.5** (taught, in Table, Which question? (two sound alike)): Drag everyday sentences onto the fraction each asks about
  - Parts of the standard the student never does (must add):
    - explain in own words
    - independence in an everyday situation beyond the coin case
- **S-CP.B.6** (taught, in Table divide-by and Which question?): Pick the group named after 'if' to divide by
  - Parts of the standard the student never does (must add):
    - compute the fraction themselves (fractions are supplied)
    - interpret the answer in own words
- **S-CP.B.7** (shown, in Table addition panel): Read the addition-rule panel with the double-counted block
  - To do: the tool does the "apply" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute the sum themselves
    - apply to a new pair of events (fixed to has it and positive)
- **S-CP.B.8** (shown, in Second test tree): Switch tree between Counts and Chances; read branch products
  - To do: the tool does the "apply" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - apply the rule themselves
    - use P(A)P(B given A) in both orders
- The module also lists codes this tool does not carry: S-CP.B.9.
- The read was unsure about (check these against the spec; the read may be wrong):
  - S-CP.A.3 explored: Predict has Skip guess, so not forced; no student set-up of cases in Cases mode
  - Which question? wrong drop returns the correct fraction; notes label later matches worked examples, so treated as closed
  - A.4 and B.6 taught though construct and compute are missing, per the depth rules
  - minutes midpoint of 15 to 40

## Ramp and Roof

- Spec: `tools/ramp-and-roof/spec.md` . Module: math-10-right-triangle-trigonometry. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Inspect names the needed number ('needs at least 288 in', 'Needs 420 in, the lot has 240 in'), so a student can set that value with no trig
  - Roof pitch picks are half-inch steps with pass or fail on Inspect and free tries (F4 and F5 have only a few passing or failing values)
- **G-SRT.C.6** (shown, in Ratio lab mode; triangle readout in every mode): Drag triangle corners, Stamp copies, compare ratio table
  - To do: the tool does the "understand" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain by similarity why ratios belong to the angle
    - name the ratios as the definitions of sine, cosine, tangent
    - predict before stamping
- **G-SRT.C.7** (shown, in Roof readouts and every mode's triangle block): Read sin and cos(90 - angle) readout lines
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain the relationship
    - use it to find a value
- **G-SRT.C.8** (practiced, in Ramp jobs R1-R4 and My porch, Roof jobs F1-F5): Set run length or pitch until Inspect passes the code
  - Parts of the standard the student never does (must add):
    - find sides or angles with sine, cosine or tangent (readouts do it)
    - use the Pythagorean Theorem
    - write the calculation
- The read was unsure about (check these against the spec; the read may be wrong):
  - C.8 key_step shared: student picks values, readouts compute the trig
  - Ratio lab shown not explored: no prediction step
  - minutes midpoint of 15 to 40

## Slice and Stack

- Spec: `tools/slice-and-stack/spec.md` . Module: math-10-volume-and-cross-sections. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Find them all: three plane sliders with a live section name, free tries and Show me one per item give each shape without reasoning about the cut
- **G-GMD.B.4** (practiced, in Cut (Find them all checklist) and Spin): Tilt the plane to find each cube section; spin shapes to name solids
  - Parts of the standard the student never does (must add):
    - name the section or solid themselves (readout names it)
    - predict the rotated solid
    - hunt sections on solids other than the cube
- **G-GMD.A.3** (shown, in Cut readouts): Change solid size sliders and read V formula with numbers
  - To do: the tool does the "solve" step: the student must do it
  - Parts of the standard the student never does (must add):
    - solve problems with the formulas
    - compute any volume themselves
- **G-GMD.A.1** (shown, in Twins pairs 1-6): Press Sweep and watch equal slice bars for twin solids
  - To do: the tool does the "give an argument" step: the student must do it
  - Parts of the standard the student never does (must add):
    - give the argument in words
    - circle circumference and area
    - dissection and limit arguments
- **G-GMD.A.2** (shown, in Twins pair 5): Sweep the hemisphere and bowl pair, read the sphere line
  - To do: the tool does the "give an argument" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - give the Cavalieri argument for the sphere themselves
- The read was unsure about (check these against the spec; the read may be wrong):
  - Spec has no explicit beaten section; beatable inferred
  - B.4 cross-section half is practiced, rotation half is shown; recorded as practiced
  - Twins is watch-only, so A.1 and A.2 are shown not explored (verb is give an argument)
  - minutes midpoint of 10 to 35

## Proof Tower

- Spec: `tools/proof-tower/spec.md` . Module: math-10-proofs-and-constructions. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Wobble messages name the missing premise or say the reason cannot give this statement, and tries are free, so reasons can be found by elimination from the shelf
- **G-CO.C.9** (practiced, in Tower levels 1, 2, 5): drag statement blocks and reasons until each locks
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write the statements and reasons (blocks are given)
    - explain the argument in own words
- **G-CO.C.10** (practiced, in Tower levels 3, 4): stack angle-sum and isosceles proofs from given blocks
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - midsegment theorem
    - medians meet at a point
    - write statements themselves
- **G-CO.C.11** (practiced, in Tower levels 6, 7, 8): stack parallelogram and rectangle proofs from given blocks
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - opposite angles congruent
    - converse for rectangles
    - write statements themselves
- **G-CO.D.12** (practiced, in Compass challenges C1-C6): draw constructions with compass and straightedge tools
  - To do: no model or guide: add one
  - Parts of the standard the student never does (small, add if cheap):
    - copying a segment as its own task
- **G-CO.D.13** (practiced, in Compass challenges C7, C8): construct inscribed hexagon and square in a circle
  - To do: no model or guide: add one
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - inscribed equilateral triangle
- The read was unsure about (check these against the spec; the read may be wrong):
  - Tower depth practiced because the lock check is beatable by elimination; statement text is given
  - Compass has no model or guide before success, only a how line
  - Levels open in order and cards are earned

## Rigid Motion Twins

- Spec: `tools/rigid-motion-twins/spec.md` . Module: math-10-rigid-motions-and-congruence. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Level 9: tray reads Found k of n and hexagon handles snap to vertices, midpoints and center, so every motion can be tried
  - Level 10: Not twins is the only possible call there, so pressing it at once may win without Measure
- **G-CO.A.2** (taught, in Tracks levels 1-8): set slide, turn, flip to move the cast; read function rules
  - Parts of the standard the student never does (must add):
    - compare motions that keep distance and angle with those that do not
    - describe the transformation as a function themselves
- **G-CO.A.3** (practiced, in Tracks level 9): hunt every turn and flip mapping a shape to itself
  - Parts of the standard the student never does (must add):
    - describe each motion in words or symbols (tool names it)
- **G-CO.A.4** (claimed, in listed in CCSS clusters line): none: motions are applied, never defined
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "develop" step: the student must do it
  - Parts of the standard the student never does (must add):
    - develop definitions from angles, circles, perpendicular and parallel lines
- **G-CO.A.5** (taught, in Tracks levels 1-8): specify a motion sequence that carries cast onto print
  - Parts of the standard the student never does (must add):
    - draw the image of a given figure (the tool animates it)
- **G-CO.B.6** (practiced, in Tracks level 10): call Not twins after Measure on level 10
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - predict the effect of a motion before applying it
    - decide congruence for a pair without moving
- **G-CO.B.7** (claimed, in listed under Criteria): none: no triangle iff statement of sides and angles
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "show" step: the student must do it
  - Parts of the standard the student never does (must add):
    - show triangles congruent iff corresponding sides and angles are congruent
- **G-CO.B.8** (shown, in Criteria cards): press Next step as SSS, SAS, ASA triangles land
  - To do: the tool does the "explain" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain in own words
- The module also lists codes this tool does not carry: G-CO.A.1.
- The read was unsure about (check these against the spec; the read may be wrong):
  - cost_class new-engine because the transformations engine is first described in this spec
  - B.7 claimed: only Measure on a footprint pair touches the idea
  - Level 10 may require a Measure first; spec only hints after five moves
  - G-CO.A.2 depth taught although comparison with non-rigid motions is missing

## Shadow Measure

- Spec: `tools/shadow-measure/spec.md` . Module: math-10-similarity. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Add the missing part, Reach five items that differ, Put it on the main path.
- **G-SRT.A.1** (touched, in Streetlight mode, Show dilation layer): Toggle Show dilation, hover points, read k
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "verify" step: the student must do it
  - Parts of the standard the student never does (must add):
    - lines not through the center map to parallel lines (A.1a)
    - lines through the center stay unchanged (A.1a)
    - verify by checking, not just watching
    - segment ratio shown only as k, not tested (A.1b)
- **G-SRT.A.3** (taught, in Why similar? step, every mode): Pick two angle reasons that make the triangles similar
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - use properties of similarity transformations (cards are plain angle facts)
    - establish the AA criterion in own words
- **G-SRT.B.5** (taught, in Set up, Measure, Why similar?, Reveal in all modes): Tape two lengths, give AA reason, compare estimate with real height
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute the proportion themselves (notebook formula does it)
    - congruence criteria
    - prove relationships in a figure
- The module also lists codes this tool does not carry: G-SRT.A.1a, G-SRT.A.1b, G-SRT.A.2, G-SRT.B.4.
- The read was unsure about (check these against the spec; the read may be wrong):
  - A.3 marked taught but the cards are angle facts, not similarity transformations
  - A.1 touched because Show dilation is an optional layer; notes say numeric k appears only after Reveal
  - minutes is midpoint of 15 to 40

