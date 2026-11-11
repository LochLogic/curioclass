# Spec fixes: math, grade 12

20 tools: 15 rework, 5 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (17), Close the guessable check (10), Add the missing part (20), Add a model or a guide (1), Add a check (5), Reach five items that differ (11), Put it on the main path (5), Teach the code or drop it (3), Sensitivity read (1).

Shape for this course: ../../agents/catalog/shape/math-12.md.

## Optimization Workshop

- Spec: `tools/optimization-workshop/spec.md` . Module: math-12-applications-of-derivatives. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Each Best design challenge (for example more than 190 square meters) can be met by moving the slider and watching the goal readout
- **AP-CALC.U4** (shown, in Moving parts (ladder, balloon, shadow)): Runs a rig, freezes it, reads the related-rates formula with numbers
  - To do: the tool does the "solve" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write the relation between quantities
    - differentiate with respect to time
    - solve for the unknown rate
- **AP-CALC.U5** (shown, in Best design (5 projects)): Drags a slider for dots, then opens Prove it for the work card
  - To do: the tool does the "optimize" step: the student must do it
  - Parts of the standard the student never does (must add):
    - write the goal function
    - differentiate and find critical points
    - justify with the first derivative test and endpoints
- The module also lists codes this tool does not carry: AP-CALC.U4 local linearity and L'Hospital's rule (named out in spec), AP-CALC.U5 concavity, second derivative test, curve sketching (not named in spec).
- The read was unsure about (check these against the spec; the read may be wrong):
  - cost_class super judged from 5 benches, 3 rigs and 14 images
  - student never sets up the function; Prove it does it
  - Moving parts counted on path though it is a second mode
  - minutes is midpoint of 30 to 45

## Solid Spinner

- Spec: `tools/solid-spinner/spec.md` . Module: math-12-applications-of-integrals. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **AP-CALC.U8** (shown, in Shelf, Cross sections, Throw a pot): Drags a cutting wire, picks slice count, reads coin sum against exact
  - To do: the tool does the "find" step: the student must do it
  - Parts of the standard the student never does (must add):
    - set up the integral for a volume
    - evaluate it
    - rectangular cross sections
    - shells
- The module also lists codes this tool does not carry: AP-CALC.U8 average value, motion and net change (topics 8.1 to 8.3, not named in spec).
- The read was unsure about (check these against the spec; the read may be wrong):
  - Predict box is optional so the check is only on an optional path
  - only first 120 lines read
  - area between curves is shown only as B1 base area
  - no standard texts printed for AP-CALC
  - minutes is midpoint of 25 to 40

## Courtroom Statistics

- Spec: `tools/courtroom-statistics/spec.md` . Module: math-12-confidence-intervals-and-significance-tests. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Ha charge has three options and the clerk quotes the wording on a wrong pick, free to retry (marked in record)
  - Verdict has two live options (Innocent is always refused) and the clerk corrects a wrong one
  - Admissibility yes/no chips can be cycled until the case is admitted or dismissed
- **S-IC.B.4** (shown, in Trial (Sentencing), Lineup): Reads the sentence interval and drags a claim in Lineup
  - To do: the tool does the "estimate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - develop a margin of error by simulation of random sampling
    - compute the interval themselves
- **S-IC.B.5** (practiced, in Trial (cases 3 and 6)): Runs the trial on the two randomized cases; picks verdict and writes sentence
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - use simulations to decide whether a difference is significant
    - compute the test statistic and p-value
- **S-IC.B.6** (practiced, in Trial (Admissibility), case 7): Answers three yes/no admissibility chips per case
  - Parts of the standard the student never does (must add):
    - judge conclusions, causal claims or practical importance in a report
- **AP-STAT.U6** (practiced, in Trial (cases 1, 3), Docket): Picks charge and alpha, checks conditions, files verdict on proportion cases
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute SE, z and p-value by hand
    - compute the interval by hand
- **AP-STAT.U7** (practiced, in Trial (cases 2, 4, 5, 6)): Same trial stages on one-sample, paired and Welch mean cases
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute SE, t and p-value by hand
    - compute the interval by hand
- The module also lists codes this tool does not carry: S-IC.B.3.
- The read was unsure about (check these against the spec; the read may be wrong):
  - S-IC.B.6 missing weight set core because unsure what 'evaluate reports' covers beyond data gathering
  - AP unit labels are legacy numbering per notes.md
  - verdict depth set practiced not taught because of the beatable two-option checks
  - minutes is midpoint of 20 to 40

## Conic Focus Finder

- Spec: `tools/conic-focus-finder/spec.md` . Module: math-12-conic-sections. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Match M1-M6: drag pins snapped to 0.5 with live 'Pins match' and 'String matches' lines over a ghost curve, free tries
- **G-GPE.A.3** (shown, in Draw; equation card): drag the pencil with the string fixed, press Show equation
  - To do: the tool does the "derive" step: the student must do it
  - Parts of the standard the student never does (must add):
    - derive the equation from the distance rule
    - explain why constant sum or difference gives the equation
- **G-GPE.A.2** (shown, in Draw, Pin and rail; Eccentricity): drag the pencil between pin and rail, press Show equation
  - To do: the tool does the "derive" step: the student must do it
  - Parts of the standard the student never does (must add):
    - derive the equation of the parabola
    - tilted parabolas (xy term is left out)
- The read was unsure about (check these against the spec; the read may be wrong):
  - G-GPE.A.3 and A.2 both scored shown: the tool derives and the student draws
  - Match is labeled optional, so derive-by-matching is not on_path

## Slope Field Garden

- Spec: `tools/slope-field-garden/spec.md` . Module: math-12-differential-equations. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **AP-CALC.U7** (shown, in Garden, Step by step, Models): Plants seeds, watches vines follow blades, presses Step for Euler
  - To do: the tool does the "reason" step: the student must do it
  - Parts of the standard the student never does (must add):
    - sketch a solution curve by hand
    - separate variables themselves
    - compute Euler steps by hand
    - solve a model equation
- The read was unsure about (check these against the spec; the read may be wrong):
  - sandbox with no wrong answers, so no check on the main path
  - Check a guess is optional and ungraded
  - only first 130 lines read
  - AP-CALC.U7 topics given as 7.1 to 7.9 in spec, no sub-codes
  - minutes is midpoint of 20 to 40

## Data Desk: Distributions

- Spec: `tools/data-desk-distributions/spec.md` . Module: math-12-exploring-data. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Reach five items that differ, Put it on the main path.
- Checks a student can pass by guessing:
  - Describe: Check marks each clause backed or not backed with the reason, shape 5 chips, center 2, spread 3, unusual few, free retries
- **S-ID.A.1** (practiced, in Explore; chart type buttons): choose Dot, Histogram or Box and set bin width
  - To do: no check: add one where thinking is cheaper than guessing
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - place the values on the plot themselves
- **S-ID.A.2** (practiced, in Describe center and spread chips; Check): pick the median or mean and IQR, SD or range chips for the shape
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compare two or more data sets in Describe (Split by region is a look only)
    - compute the statistics themselves
- **S-ID.A.3** (practiced, in Describe shape and unusual rows; Check): pick shape and unusual-feature chips and read the built sentence
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - interpret differences between data sets
    - write the sentence in their own words
    - say how an outlier changes the statistics
- **S-ID.A.4** (touched, in Explore, Normal model): toggle Normal model and read the 68-95-99.7 table
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "use" step: the student must do it
  - Parts of the standard the student never does (must add):
    - fit a normal model themselves
    - estimate population percentages
    - say when the model is not appropriate
    - use tables or a calculator for areas
- The read was unsure about (check these against the spec; the read may be wrong):
  - S-ID.A.2 compare: only Split by region on desk 3 compares data sets, and it is a look in Explore
  - Items counted as the four desks
  - AP-STAT codes not rowed, no wording printed

## Function Family Reunion

- Spec: `tools/function-family-reunion/spec.md` . Module: math-12-functions-and-their-graphs. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Put it on the main path.
- Checks a student can pass by guessing:
  - Who's who: four sliders with a live 'Same curve' check over the guest curve, feedback is visual overlap, 10 guests, free tries
- **F-IF.C.7** (shown, in Reunion; Key features card): pick a parent, watch its graph and key-features card update
  - To do: the tool does the "graph" step: the student must do it
  - Parts of the standard the student never does (must add):
    - graph by hand in simple cases
    - find zeros and asymptotes from factorizations themselves
    - polynomials beyond the cube, piecewise and step functions, trig
- **F-BF.B.3** (practiced, in Reunion sliders; Where points land table): drag handles or sliders for a, b, h, k and read the effect
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - find k from given graphs on the main path (Who's who only)
    - recognize even and odd from algebraic expressions
    - explain the effects in words
- **F-BF.B.4** (shown, in Mirror cousin; Keep the right half): tap the relative to drop a pin and see its mirror pin
  - To do: the tool does the "find" step: the student must do it
  - Parts of the standard the student never does (must add):
    - find an inverse by solving themselves
    - verify by composition
    - read inverse values from a table
- **F-IF.C.9** (touched, in Reunion, Add to the photo): freeze up to four relatives with Add to the photo
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - compare two functions in different representations (table, verbal)
    - say which has the larger maximum or other property
- The module also lists codes this tool does not carry: F-IF.C.8, F-IF.C.8a, F-IF.C.8b, F-BF.B.4b, F-BF.B.4c, F-BF.B.5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - F-BF.B.3 is identify/experiment but has no predict step, so practiced not explored
  - Mirror cousin tab and Who's who: only Who's who is labeled optional
  - F-BF.B.4d (Keep the right half) is present but the spec names only F-BF.B.4
  - AP-PRECALC unit codes not rowed, no wording printed

## Zoom to the Limit

- Spec: `tools/zoom-to-the-limit/spec.md` . Module: math-12-limits-and-rates-of-change. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **F-IF.B.6** (shown, in Secant; Zoom, Read the slope; Equal steps): step the secant closer and read the table of average rates
  - To do: the tool does the "calculate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - calculate the average rate themselves
    - interpret it in context in words
    - a given table or interval chosen by the student
- The read was unsure about (check these against the spec; the read may be wrong):
  - Only F-IF.B.6 has printed wording; AP-PRECALC.U1 not rowed
  - Student drags b and presses Step closer, tool computes the rate, so key_step is tool
  - No check anywhere in the spec

## Image Transformer

- Spec: `tools/image-transformer/spec.md` . Module: math-12-matrices. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Reach five items that differ, Put it on the main path.
- Checks a student can pass by guessing:
  - Undo it: Show the formula and Show me (after two misses) give the inverse, and Move 4 is a two-way choice
  - Undo it pixel and color cards: Show me after two misses
- **N-VM.C.7** (touched, in Studio, Scale by k): press Scale by k and read the new determinant
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "multiply" step: the student must do it
  - Parts of the standard the student never does (must add):
    - multiply a matrix by a scalar themselves
    - game payoff context
- **N-VM.C.8** (shown, in Order matters): set A and B, read the products BA and AB
  - To do: the tool does the "add" step: the student must do it
  - Parts of the standard the student never does (must add):
    - multiply by hand
    - subtract matrices
    - other dimensions than 2 by 2
    - add matrices (optional A + B toggle)
- **N-VM.C.9** (practiced, in Order matters; Same picture / Different pictures): compare BA and AB, press Swap, find a pair that commutes
  - Parts of the standard the student never does (must add):
    - associative and distributive properties
    - explain why order matters
- **N-VM.C.10** (practiced, in Undo it, Moves 1-4; det readout): find an undo matrix, or press It can't be undone for det 0
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - role of the zero matrix in addition
    - explain why nonzero determinant means an inverse (given only for det 0)
- **N-VM.C.11** (shown, in Studio probe): tap a pixel and read M times (x, y) with numbers
  - To do: the tool does the "multiply" step: the student must do it
  - Parts of the standard the student never does (must add):
    - multiply a vector by a matrix themselves
- **N-VM.C.12** (practiced, in Studio; presets; area readout): drag i-hat and j-hat tips or type four entries, read det and area
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - say in words what |det| means for area (the readout states it)
- **A-REI.C.9** (practiced, in Undo it, three cards): type the inverse, solve for a moved pixel's origin, invert a color filter
  - Parts of the standard the student never does (small, add if cheap):
    - 3 by 3 inverse by hand (technology does it, as the standard allows)
    - start from a written system of equations
- The module also lists codes this tool does not carry: N-VM.C.6.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Whether Show me counts as solving (spec says only that it appears after two misses)
  - N-VM.C.9 and C.10 are understand verbs with no predict step, so practiced not explored
  - Built tool: read spec and notes only, no src check
  - AP-PRECALC.U4 not rowed, no wording printed

## Polar Rose Studio

- Spec: `tools/polar-rose-studio/spec.md` . Module: math-12-polar-coordinates-and-complex-plane. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Add a check, Put it on the main path.
- **N-CN.B.4** (shown, in Studio pen readout): scrub the pen and read r, (x, y), x + yi and polar form
  - To do: the tool does the "represent" step: the student must do it
  - Parts of the standard the student never does (must add):
    - represent numbers themselves in both forms
    - explain why the two forms are the same number
    - real and pure imaginary numbers as cases
- **N-CN.B.5** (practiced, in Stamps; stamp cards): choose Turn n, Spiral s and alpha, Mirror or Shift and read the preview
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - subtraction
    - compute with modulus and argument, such as (-1 + sqrt(3) i)^3
    - multiply two chosen complex numbers (only fixed stamp factors)
- **N-CN.B.6** (touched, in Studio, Ruler toggle): tap two points with the Ruler and read distance and midpoint
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "calculate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - calculate distance as a modulus themselves
    - calculate the midpoint as an average themselves
- The read was unsure about (check these against the spec; the read may be wrong):
  - N-CN.B.5 scored practiced because the student picks the factor but the tool applies it and no check exists
  - Ruler is a toggle so scored touched
  - Spec read up to Art and Done when; Gallery treated as extra
  - AP-PRECALC.U3 not rowed, no wording printed

## Game Show Strategist

- Spec: `tools/game-show-strategist/spec.md` . Module: math-12-probability-and-random-variables. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Add a model or a guide, Reach five items that differ, Teach the code or drop it.
- **S-CP.A.2** (claimed, in Why (tree)): Plays doors; Why tree multiplies along branches
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "understand" step: the student must do it
  - Parts of the standard the student never does (must add):
    - test independence with P(A and B) = P(A)P(B)
    - decide whether two events are independent
- **S-CP.A.3** (shown, in Why (tree, given())): Reads the given-a-goat value on the Why tree
  - To do: the tool does the "understand" step: the student must do it
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute P(A and B)/P(B)
    - interpret independence as P(A|B) = P(A)
- **S-CP.A.5** (shown, in Play (host rule picker), Why): Plays Random and Devious host, then reads the Why tree
  - To do: the tool does the "explain" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain conditional probability or independence in everyday words
- **S-MD.A.1** (shown, in Strategy lab (winnings bars)): Sees the tool draw bars of winnings
  - To do: the tool does the "define" step: the student must do it
  - Parts of the standard the student never does (must add):
    - define a random variable by assigning values to events
    - graph the distribution themselves
- **S-MD.A.2** (shown, in Strategy lab, Why EV table): Watches the running average settle onto the exact EV
  - To do: the tool does the "calculate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - calculate the expected value themselves
- **S-MD.A.3** (shown, in Why (Lucky Guess table)): Reads the binomial table and EV per guess
  - To do: the tool does the "develop" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - develop the distribution from theoretical probabilities
    - find the expected value themselves
- **S-MD.A.4** (shown, in Strategy lab): Presses Play 10,000 games and watches the distribution build
  - To do: the tool does the "develop" step: the student must do it
  - Parts of the standard the student never does (must add):
    - assign probabilities from real data
    - find the expected value of a real data distribution
- **S-MD.B.5** (practiced, in Play (Briefcases, Push Your Luck), Strategy lab): Chooses Deal or No deal, Stick or Switch, Spin or Stop by gut
  - To do: no model or guide: add one
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - assign probabilities to payoff values
    - find the expected value themselves
- **S-MD.B.6** (claimed, in table only): Nothing here uses probability to make a fair decision
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "use" step: the student must do it
  - Parts of the standard the student never does (must add):
    - use probabilities to make fair decisions (lots, random number generator)
- **S-MD.B.7** (practiced, in Strategy lab): Picks up to 3 strategies and reads which has the best EV
  - To do: no model or guide: add one
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - analyze product testing, medical testing or similar contexts
    - write why a strategy is chosen
- **AP-STAT.U4** (shown, in Why, Strategy lab readouts): Reads binomial and geometric tables and the SD readout
  - To do: the tool does the "calculate" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute binomial or geometric probabilities
    - compute spread of a random variable
- The module also lists codes this tool does not carry: S-CP.A.1, S-CP.A.4, S-MD.B.6.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Why is a tab, so on_path true is a judgment
  - S-CP.A.2 marked claimed: tree multiplies but no independence test is asked
  - B.5a and B.5b folded into S-MD.B.5
  - spec has no Standards map table; codes taken from the CCSS clusters line
  - Content says the student writes which briefcase choice they would pick and why, but Screens shows no writing box
  - minutes is midpoint of 20 to 40
  - cost sibling though two additions to the probability engine are requested

## Design the Study

- Spec: `tools/design-the-study/spec.md` . Module: math-12-sampling-and-experiments. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Story: the editor names one flawed row per letter, each row has 2-4 chips, Revise and resubmit are free
- **S-IC.B.3** (practiced, in Story draft rows; editor letters): choose assignment, control, blinding and timing for the methods section
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - sample surveys
    - observational studies as a type
    - differences among the three study types
    - explain in words how randomization relates (letters explain it)
- **S-IC.B.5** (practiced, in Story, Shuffle check; Bench Run 400 studies): run the study, press Shuffle check, read the count of 1,000
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - decide significance themselves (the editor's threshold decides)
    - compare treatments in data collected from real subjects
- **S-IC.B.6** (shown, in Story, Submit to the journal): read the editor's letter and the waterfall of named flaws
  - To do: the tool does the "evaluate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - evaluate a report written by someone else
- The module also lists codes this tool does not carry: S-IC.B.4.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Built tool: spec and notes only, no src check
  - Health note on energy drinks and children is in the spec, flagged sensitive
  - S-IC.B.6 scored shown because the editor judges the student's report and the student does not evaluate one
  - S-IC.B.5 shuffle for restricted designs is approximate per notes

## Rain Gauge

- Spec: `tools/rain-gauge/spec.md` . Module: math-12-the-integral. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **AP-CALC.U6** (shown, in Storm, Slices (5 storms)): Picks n and method, pours slices, reads sum against exact
  - To do: the tool does the "approximate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - compute a Riemann sum by hand
    - evaluate a definite integral with an antiderivative themselves
    - properties of the accumulation function
- The module also lists codes this tool does not carry: AP-CALC.U6 integration techniques after topic 6.7 (not named in spec).
- The read was unsure about (check these against the spec; the read may be wrong):
  - Forecast cards (student solves for overflow time) are optional and left as part of this one code
  - no standard texts printed for AP-CALC
  - only first 120 lines of the spec read
  - minutes is midpoint of 25 to 40

## Identity Proof Race

- Spec: `tools/identity-proof-race/spec.md` . Module: math-12-trigonometric-identities-and-equations. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Workbench laps: any card tried on a plate either rewrites or says nothing to rewrite, with no penalty, so trying cards from the tray finds the route
  - Solve Lock in: names the missing or extra mark ('pi/2 is not a solution'), free retries on a 24-point dial
- **F-TF.C.8** (practiced, in Workbench laps L2, L3, L4, L6, L8; Race): drag Pythagorean cards onto either side to rewrite
  - Parts of the standard the student never does (must add):
    - prove the Pythagorean identity itself
    - find sin, cos or tan given another and the quadrant
- **F-TF.C.9** (practiced, in Workbench laps L5, L7): apply sum and difference cards in laps
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - prove the addition and subtraction formulas
    - tangent formulas
    - solve problems beyond the two laps
- **F-TF.B.6** (shown, in Solve S6, S7 Calculator): press Calculator and see the restricted range shaded on the dial
  - To do: the tool does the "understand" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain why restricting the domain lets an inverse be built
    - restrict the domain of tan
- **F-TF.B.7** (practiced, in Solve S1-S8; Lock in): rewrite the equation, then mark every solution on the dial
  - Parts of the standard the student never does (must add):
    - a modeling context
    - interpret the solution in the context
- The module also lists codes this tool does not carry: F-TF.B.5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Which mode is on_path: none of the three modes is marked optional
  - Gave every proof lap the same depth; the Pythagorean card is handed to the student, not derived
  - AP-PRECALC.U3 not rowed, no wording printed

## Flight Planner

- Spec: `tools/flight-planner/spec.md` . Module: math-12-vectors. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Flight plans heading: ground arrow and course line are both drawn, Fly it and Try again are free, Check names the error direction, tolerance 1 degree
  - Landing crab heading: Fly final shows the drift side, free retries
- **N-VM.A.1** (practiced, in Free fly; vector card): drag the air and wind arrow tips, set heading and speed
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - use the symbols v, |v|, ||v||
- **N-VM.A.2** (claimed, in Components table): none: coordinates of airfields are used by the tool, not by the student
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "find" step: the student must do it
  - Parts of the standard the student never does (must add):
    - find components by subtracting initial from terminal coordinates
- **N-VM.A.3** (practiced, in Flight plans 1-5, Find the wind, Landing): pick a heading so the ground arrow lies on the course, then type ground speed and time
  - Parts of the standard the student never does (small, add if cheap):
    - interpret results without the fly-it preview
- **N-VM.B.4** (practiced, in Find the wind 1-2; Flight plans): drag the wind arrow until air plus wind equals ground
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - subtract vectors with a method (done by dragging)
    - add or subtract by components themselves
- **N-VM.B.4a** (shown, in Free fly vector card; components table): watch air, wind and sum arrows draw tip to tail
  - To do: the tool does the "add" step: the student must do it
  - Parts of the standard the student never does (must add):
    - add vectors themselves
    - the parallelogram rule
    - explain why the magnitude of a sum is not the sum of magnitudes
- **N-VM.B.5** (shown, in Free fly dashed line): see the 30-minute line, 0.5 h times the ground velocity
  - To do: the tool does the "multiply" step: the student must do it
  - Parts of the standard the student never does (must add):
    - multiply a vector by a scalar themselves
    - reverse direction for a negative scalar
    - compute |c|v
- The module also lists codes this tool does not carry: N-VM.B.4b, N-VM.B.4c, N-VM.B.5a, N-VM.B.5b.
- The read was unsure about (check these against the spec; the read may be wrong):
  - The spec names clusters N-VM.A and N-VM.B; I split them into the finest codes the mode lines imply
  - N-VM.A.2 mentioned only in the cluster gloss, scored claimed
  - N-VM.B.4b: Free fly table shows sum magnitude and direction but the student does not find it, so it is in untaught
  - AP-PRECALC.U4 not rowed, no wording printed

## Fair Dice Investigation

- Spec: `tools/fair-dice-investigation/spec.md` . Module: math-12-chi-square-and-regression-inference. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **AP-STAT.U8** (taught, in Cases 1 and 2, Dice lab): Rolls and tests dice, builds expected counts, picks the biggest-contribution cell
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - test of independence (one sample, two variables)
    - compute the chi-square statistic and p-value by hand
- **AP-STAT.U9** (taught, in Case 3): Tests both slopes, reads residuals, cites p-value or interval to pick the link
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute slope SE, t and interval by hand
- The read was unsure about (check these against the spec; the read may be wrong):
  - AP unit codes are legacy numbering per notes.md; no CCSS codes in module and no standard texts in the packet
  - Case 1 and 2 share U8 and are folded into one entry
  - minutes is midpoint of 25 to 45

## Hole Hunter

- Spec: `tools/hole-hunter/spec.md` . Module: math-12-limits-and-continuity. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Kind buttons (Hole, Moved point, Jump, Asymptote): four choices, free retries with clue feedback
  - Patch dot drags on a 0.25 snap and sticks only at the limit, so trial finds it
  - Parameter levels 11 and 13: seam lights green live while sliders move
- **AP-CALC.U1** (taught, in Hunt (13 levels), Bench): Finds breaks, reads approach tables, names limits and kind, patches
  - Parts of the standard the student never does (must add):
    - limits by algebra, squeeze theorem
    - intermediate value theorem
    - formal three-part continuity check written out
- The module also lists codes this tool does not carry: AP-CALC.U1 algebraic limits, squeeze theorem, intermediate value theorem (spec names topics 1.2 to 1.6 and 1.10 to 1.15 only).
- The read was unsure about (check these against the spec; the read may be wrong):
  - AP-CALC.U1 spelled without sub-codes; spec gives topic numbers only
  - Bench is explore mode, Hunt counted as main path
  - minutes is midpoint of 25 to 40

## Sample Machine

- Spec: `tools/sample-machine/spec.md` . Module: math-12-sampling-distributions. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Add the missing part, Put it on the main path.
- **S-IC.A.1** (explored, in Machine, Predict): Sets hopper, n, statistic; predicts center, spread, shape; draws 1,000
  - To do: see-why code, fine here; the unit must add: A unit must add drawing an inference about an unknown parameter from one actual random sample, with an estimate and a statement of its uncertainty.
  - Parts of the standard the student never does (must add):
    - infer an unknown population parameter from one real random sample
    - say what a sample can and cannot tell about the population
- **S-IC.A.2** (touched, in Machine (Show theory toggle), Predict result lines): Compares the pile with the optional theory curve
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "decide" step: the student must do it
  - Parts of the standard the student never does (must add):
    - decide whether a stated model is consistent with results
    - judge a result such as 5 tails in a row
- **AP-STAT.U5** (taught, in Predict (8 challenges), Machine): Predicts mean, SD and shape of a statistic, then checks
  - Parts of the standard the student never does (must add):
    - differences of two proportions or two means
- The read was unsure about (check these against the spec; the read may be wrong):
  - Predict counted as on the main path although it is a second mode
  - S-IC.A.2 touched: theory curve is a toggle and no decision is asked
  - AP-STAT.U5 verb chosen as describe; no standard text printed
  - Predict has no free retry per item so shape guessing not listed as beatable

## Fire Lookout Triangles

- Spec: `tools/fire-lookout-triangles/spec.md` . Module: math-12-solving-any-triangle. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Add the missing part, Reach five items that differ, Teach the code or drop it.
- **G-SRT.D.9** (claimed, in Burn area): Types burn area and sees 'Area = 1/2 ab sin C' shown
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "derive" step: the student must do it
  - Parts of the standard the student never does (must add):
    - derive the formula by drawing an auxiliary perpendicular
- **G-SRT.D.10** (taught, in Dispatch): Uses the laws of sines and cosines to find AF and CF
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - prove the Law of Sines
    - prove the Law of Cosines
- **G-SRT.D.11** (taught, in Dispatch, Radio, Burn area): Finds fire distance, the ambiguous case and burn area
  - Parts of the standard the student never does (must add):
    - find an angle from three sides (SSS)
    - right triangles beyond one radio case
    - resultant forces
- The module also lists codes this tool does not carry: G-SRT.D.9.
- The read was unsure about (check these against the spec; the read may be wrong):
  - G-SRT.D.10 verb is prove and use; student only uses, marked taught for the use part and proof listed missing
  - G-SRT.D.9 marked claimed because the student applies the formula but never derives it (notes.md says so)
  - minutes is midpoint of 25 to 40

## Speedometer

- Spec: `tools/speedometer/spec.md` . Module: math-12-the-derivative. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **AP-CALC.U2** (taught, in Needle lock (trips 1 to 5, 7, 9)): Types the derivative of a trip; ghost needle must stay locked
  - Parts of the standard the student never does (must add):
    - find a derivative from the limit definition
    - tangent line equation
    - derivatives of cos and higher-order derivatives
- **AP-CALC.U3** (taught, in Needle lock (trips 6, 8, 10, 11)): Types chain-rule and inverse trig derivatives; needles must lock
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - implicit differentiation
    - derivative of an inverse function in general
- The read was unsure about (check these against the spec; the read may be wrong):
  - action changed from simulate-tune to solve because the main task is typing a derivative
  - Rate check (difference quotient) is shown by the tool, so definition part counted missing
  - no standard texts printed for AP-CALC codes
  - minutes is midpoint of 25 to 45

