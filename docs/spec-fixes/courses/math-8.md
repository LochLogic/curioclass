# Spec fixes: math, grade 8

10 tools: 2 rework, 6 small addition, 2 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Hand the key step to the student (4), Close the guessable check (7), Add the missing part (8), Add a model or a guide (2), Add a check (1), Reach five items that differ (2), Put it on the main path (1), Teach the code or drop it (1).

Shape for this course: ../../agents/catalog/shape/math-8.md.

## Size of Everything

- Spec: `tools/size-of-everything/(no spec.md yet)` . Module: math-8-exponents-roots-and-scientific-notation. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Write the spec, Hand the key step to the student, Add the missing part.
- **8.EE.A.3** (practiced, in Place it): Drags a pin to the power of ten for ten things
  - Parts of the standard the student never does (must add):
    - use a single digit times a power of ten
    - say how many times as much one is than another (Compare does it)
- **8.EE.A.4** (shown, in Compare; Write it): Watches Compare divide in scientific notation; slides the decimal in Write it
  - To do: the tool does the "perform" step: the student must do it
  - Parts of the standard the student never does (must add):
    - perform operations with scientific notation
    - mixed decimal and scientific notation problems
    - choose units of appropriate size
- The module also lists codes this tool does not carry: 8.EE.A.1, 8.EE.A.2.
- The read was unsure about (check these against the spec; the read may be wrong):
  - all four modes treated as on path (teacher plan uses all); a student could skip them
  - Place it retry rules unknown; stars scored within one power
  - 8.EE.A.4 'shown': the student converts forms in Write it but the operation is done by the tool
  - cost_class guessed new-engine from the scale slider and 38 drawn things
  - no Sources entry per size; only a general note
  - Write it check assumed tool-key

## Ski Slope Designer

- Spec: `tools/ski-slope-designer/spec.md` . Module: math-8-slope-and-proportional-relationships. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Run card shows the slope, so the typed slope can be copied
  - Three triangles of any size satisfy the triangles check
- **8.EE.B.5** (taught, in Build; Compare): Builds runs, types rise over run, ranks runs given as graph, equation, table
  - Parts of the standard the student never does (small, add if cheap):
    - interpret unit rate in a situation beyond drop per meter across
- **8.EE.B.6** (shown, in Triangles; Lodge): Draws slope triangles; Stack shows them similar; types y = mx + b for lodge runs
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain why the slope is the same (Stack shows it)
    - derive y = mx from similar triangles
    - derive y = mx + b (intercept given)
- The read was unsure about (check these against the spec; the read may be wrong):
  - 8.EE.B.6 'shown' because the Stack and the ratio list do the explaining; student draws and types the lodge equation
  - build check: slope card visible while typing

## Data Detective

- Spec: `tools/data-detective/spec.md` . Module: math-8-bivariate-data. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Slope and intercept meaning is chosen from listed sentences
  - Association verdict on the table is a yes or no
- **8.SP.A.1** (taught, in Scatter): Taps rows to plot, taps words for the pattern, taps an outlier
  - Parts of the standard the student never does (must add):
    - choose axes and scale and plot the data themselves
    - negative association (no such case listed)
- **8.SP.A.2** (taught, in Fit): Drags two handles to fit a line, improves the closeness meter
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - judge closeness of fit without the meter
- **8.SP.A.3** (practiced, in Fit; Predict): Types slope and intercept, predicts, picks sentences for each
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - use the equation on problems beyond the one held-back case
- **8.SP.A.4** (taught, in The table): Types row totals and row percentages, judges association
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - construct the two-way table from collected data (survey table given)
    - column relative frequencies
- The read was unsure about (check these against the spec; the read may be wrong):
  - items for 8.SP.A.1 is five scatter cases though 'Done when' says six
  - 8.SP.A.3 practiced: interpretation check is a sentence pick; prediction only shows an error
  - which paired data ship is an open question
  - cost_class: data-desk kit 'as described in data-desk-distributions'; sibling guessed

## Function Machine Factory

- Spec: `tools/function-machine-factory/spec.md` . Module: math-8-defining-functions. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Linear or nonlinear sort has two bins and the differences row shows after the pick
- **8.F.A.1** (taught, in Inspect): Feeds inputs, stamps Pass or Reject, points to two outputs for one input
  - Parts of the standard the student never does (small, add if cheap):
    - state the definition in own words
    - plot the ordered pairs (dots appear on each feed)
- **8.F.A.3** (practiced, in Straight or curved): Sets m and b and feeds 0 to 4; sorts ten machines linear or nonlinear
  - Parts of the standard the student never does (must add):
    - give examples of functions that are not linear (the square machine is given)
- The read was unsure about (check these against the spec; the read may be wrong):
  - cost_class: function-machine engine is 'as described in undo-machine' spec; sibling guessed
  - sort retry rules not stated
  - 8.F.A.3 practiced because its sort check is listed as beatable

## Square Root Hunt

- Spec: `tools/square-root-hunt/spec.md` . Module: math-8-irrational-numbers. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Sort: two bins and three reason cards, retries not limited by the spec
- **8.NS.A.1** (taught, in Catch; Sort): Catches repeating decimals as fractions by shift and subtract; sorts 12 numbers
  - Parts of the standard the student never does (must add):
    - show that a rational number's decimal expansion repeats eventually (shown as a reminder only)
    - show that an irrational has no repeat (given)
- **8.NS.A.2** (taught, in Squeeze; Compare): Traps roots between decimals, places marks, estimates pi squared
  - Parts of the standard the student never does (small, add if cheap):
    - explain in words how to continue to better approximations
- The read was unsure about (check these against the spec; the read may be wrong):
  - cost_class: number-line engine is 'as described in roller-coaster-rounding' spec; sibling guessed
  - items for 8.NS.A.1 counts five catch cards plus twelve sort numbers
  - explaining how to continue weighted edge

## Two Trains

- Spec: `tools/two-trains/spec.md` . Module: math-8-linear-equations-and-systems. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Put it on the main path.
- Checks a student can pass by guessing:
  - Dispatch cards 1 to 5 and 8: slider has few steps and Check names the actual meeting, so each try shows which way to move
- **8.EE.C.8a** (explored, in Yard; presets): Sets trains, plays, sees the lines cross where they meet
  - To do: see-why code, fine here; the unit must add: Ask the student to predict the meeting and say why the crossing satisfies both equations before each run.
  - Parts of the standard the student never does (must add):
    - explain why intersection points satisfy both equations
- **8.EE.C.8b** (shown, in Yard algebra box): Watches Show the algebra set the equations equal; reads the crossing
  - To do: the tool does the "solve" step: the student must do it
  - Parts of the standard the student never does (must add):
    - solve a system algebraically themselves on the main path
    - solve simple cases by inspection (banners show them)
- **8.EE.C.8c** (touched, in Dispatch cards 1 to 8): Sets a speed or departure so the trains meet at a target; predicts card 6
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - write the two equations from a story
    - decide whether lines through given points intersect
- The module also lists codes this tool does not carry: 8.EE.C.7, 8.EE.C.7a, 8.EE.C.7b.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Dispatch called an optional challenge, so C.8c is touched and C.8b main-path depth is shown
  - plan.md uses Dispatch tickets in class; if a teacher requires them depth would rise
  - items for 8a counts five presets

## Square Slicer

- Spec: `tools/square-slicer/spec.md` . Module: math-8-the-pythagorean-theorem. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide.
- Checks a student can pass by guessing:
  - Square or Not square stamp is two choices per corner
- **8.G.B.6** (taught, in Dissect; Deck corners): Cuts and slides squares to fill the big square; judges six deck corners
  - Parts of the standard the student never does (must add):
    - explain the proof in words (guide lines supply the cuts)
    - prove the converse in general (six example corners only)
- **8.G.B.7** (practiced, in Missing sides): Types missing sides: ladder, TV, ramp, truck box in 3D
  - To do: no model or guide: add one
- The read was unsure about (check these against the spec; the read may be wrong):
  - deck corner retry rules not stated
  - 8.G.B.7 has no hint or model stated, so practiced

## Transformation Dock

- Spec: `tools/transformation-dock/spec.md` . Module: math-8-transformations. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Add a check, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Angle taps in the floor yards have few choices and free tries
- **8.G.A.1** (practiced, in Route; measuring tools): Measures sides before and after each move with a ruler
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - lines taken to lines (not named)
- **8.G.A.1a** (practiced, in Route; measuring tools): Measures side lengths before and after each move with a ruler
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
- **8.G.A.1b** (practiced, in Route; measuring tools): Measures angles before and after each move with a protractor
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
- **8.G.A.1c** (claimed, in Standards map): Listed; only a ruler and protractor are described, nothing measures parallels
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "verify" step: the student must do it
  - Parts of the standard the student never does (must add):
    - check parallel lines taken to parallel lines
- **8.G.A.2** (taught, in Route; Match): Builds a route that lands a tile on its outline; labels docks congruent
  - Parts of the standard the student never does (small, add if cheap):
    - describe the sequence in words
- **8.G.A.4** (taught, in Match): Builds a route with a resize; labels docks similar; replays
  - Parts of the standard the student never does (small, add if cheap):
    - describe the sequence in words
- **8.G.A.5** (practiced, in Floor pattern): Taps three angles on a straight edge and equal angles at parallel tracks
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - give the argument in words
    - exterior angle of a triangle
    - AA criterion argued (checked angle by angle)
- The module also lists codes this tool does not carry: 8.G.A.1c.
- The read was unsure about (check these against the spec; the read may be wrong):
  - 8.G.A.1 parent listed once and again as a, b, c
  - cost_class: transformations kit 'as described in rigid-motion-twins'; sibling guessed
  - 8.G.A.1a and b check marked none: numbers are shown, no right answer asked
  - 8.G.A.5 practiced but the argument itself is not asked

## Story Graphs

- Spec: `tools/story-graphs/spec.md` . Module: math-8-modeling-with-functions. Stage: built (the code changes after the spec). Sort: **fine**.
- Fixes: none found; confirm at final review.
- **8.F.B.4** (taught, in Model): Types m and b from a description, points, table or graph; picks meaning cards
  - Parts of the standard the student never does (small, add if cheap):
    - write the whole equation (template given, only m and b typed)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items: six Match, five Sketch (spares extend to nine and seven), six Model
  - minutes from 20 to 35 in spec

## Snow Globe Maker

- Spec: `tools/snow-globe-maker/spec.md` . Module: math-8-volume-of-cylinders-cones-and-spheres. Stage: spec only. Sort: **fine**.
- Fixes: none found; confirm at final review.
- The read was unsure about (check these against the spec; the read may be wrong):
  - items: three pours, four booth days, six backward orders
  - a real pour test could also do the pour part

