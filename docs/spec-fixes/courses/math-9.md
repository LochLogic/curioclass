# Spec fixes: math, grade 9

11 tools: 5 rework, 5 small addition, 1 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (8), Close the guessable check (11), Add the missing part (10), Add a model or a guide (3), Add a check (2), Reach five items that differ (7), Put it on the main path (1), Teach the code or drop it (2).

Shape for this course: ../../agents/catalog/shape/math-9.md.

## Which Model Wins?

- Spec: `tools/which-model-wins/spec.md` . Module: math-9-linear-quadratic-and-exponential-models. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Computer's best fit button moves handles to the answer
  - Live mean error readout while dragging lets handles be tuned by trial
  - Reveal works with no pick, so the winner can be seen before choosing
- **F-LE.A.1** (practiced, in Look; Build pick and reason chips): read Differences and Ratios columns; pick model and reason
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - tell models apart from a graph or a spoken situation
- **F-LE.A.2** (practiced, in Build): drag handles to fit line, parabola, exponential to data
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - compute the function from two input-output pairs
    - arithmetic and geometric sequences
- **F-LE.A.3** (shown, in Reveal Long run, two datasets): press Long run and watch the exponential pull away
  - To do: the tool does the "observe" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - comparison with polynomials beyond the quadratic
    - finding the crossing themselves
- **F-BF.A.1b** (practiced, in Build Combine card, stopping distances): fit a line and a parabola; their sum is drawn
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write the combined function symbolically
    - operations other than adding
- **F-BF.B.3** (practiced, in Build handles): shift and stretch curves with vertex and stretch handles
  - To do: no model or guide: add one
  - Parts of the standard the student never does (must add):
    - identify the effect of f(x+k) and f(kx)
    - negative k
    - find k from a graph
    - even and odd functions
- **F-LE.B.5** (shown, in Reveal parameter cards): read the winning model's parameter card in words
  - To do: the tool does the "interpret" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write their own interpretation
- The module also lists codes this tool does not carry: F-LE.A.1a, F-LE.A.1b, F-LE.A.1c, F-LE.A.4, F-BF.A.1, F-BF.A.1a, F-BF.A.1c, F-BF.A.2, F-BF.B.4, F-BF.B.4a, F-BF.B.4b, F-BF.B.4c, F-BF.B.4d, F-BF.B.5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Parent code F-BF.A.1 listed as untaught though Build writes functions by handles
  - F-BF.B.3 depth practiced: handles shift and stretch but the effect is never identified
  - Reason chips are not checked

## Exponent Rule Builder

- Spec: `tools/exponent-rule-builder/spec.md` . Module: math-9-rational-exponents-and-real-numbers. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Rule lab: three candidate rules, picks are not scored and retries are free
  - Rung puzzles: Check marks each tile and retries are free
  - Rational or not: two bins, a wrong drop slides back with the reason, no score
- **N-RN.A.1** (shown, in Rule lab R6 and R7): Slides r until r times r is the base; tool states the proof; picks rules
  - To do: the tool does the "explain" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain in own words (the proof text is shown)
    - radical notation for rational exponents written by the student
- **N-RN.A.2** (practiced, in Rung puzzles): Drags each expression tile to the rung where its value lands
  - Parts of the standard the student never does (must add):
    - write the rewritten expression (tiles are placed, not written)
- **N-RN.B.3** (shown, in Rational or not): Drags 12 numbers to Rational or Irrational; reason card shows why
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain why the sum or product is rational or irrational
- The read was unsure about (check these against the spec; the read may be wrong):
  - Rational or not check is none: no score kept
  - Rung puzzles items: 42 tiles in levels 1 to 7 plus 7 in level 8
  - older spec format with no Can it be beaten section
  - N-RN.A.1 not explored since 'explain' is not an understand verb

## Equation Golf

- Spec: `tools/equation-golf/spec.md` . Module: math-9-solving-linear-equations-and-inequalities. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Inequality sign pick after a negative multiply or divide: two buttons, free retries with no stroke, wrong pick shows the shading
- **A-REI.A.1** (shown, in Front and Back nine move log): read the move log with each step's reason
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain each step in own words
    - construct a viable argument for a method
- **A-REI.B.3** (taught, in Holes 1-18): choose balance moves until x equals a number
  - Parts of the standard the student never does (must add):
    - equations with coefficients represented by letters
- The module also lists codes this tool does not carry: A-REI.A.2, A-REI.B.4, A-REI.B.4a, A-REI.B.4b.
- The read was unsure about (check these against the spec; the read may be wrong):
  - A-REI.A.1 set shown because the tool writes the reasons; the student only picks the move
  - coefficients as letters left to model-my-world per Open questions

## Algebra Tile Studio

- Spec: `tools/algebra-tile-studio/spec.md` . Module: math-9-structure-of-expressions. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Frame gap tips name the tile that fits each dashed cell, with free tries, so a rectangle can be closed by following tips
- **A-SSE.A.1** (practiced, in Mat): build tiles on free mat; read live expression and term names
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - interpret in terms of a context (no situation, only tiles)
- **A-SSE.A.2** (practiced, in Frame cards 1-10): drag tiles into frame until the rectangle closes
  - Parts of the standard the student never does (must add):
    - rewrite symbolically; tool writes the factored form from the edges
    - structure above degree 2 such as x^4 - y^4
- **A-SSE.B.3a** (practiced, in Frame cards 1-8): close a tile rectangle; read factors and zeros
  - Parts of the standard the student never does (must add):
    - state the zeros (the tool prints them)
- **A-SSE.B.3b** (shown, in Square, six cards): press Split strips then Fill the corner; read minimum
  - To do: the tool does the "complete" step: the student must do it
  - Parts of the standard the student never does (must add):
    - choose the corner size
    - write the completed-square form
    - state the minimum
    - odd middle coefficients
- The module also lists codes this tool does not carry: A-SSE.A.1b, A-SSE.B.3c, A-SSE.B.4.
- The read was unsure about (check these against the spec; the read may be wrong):
  - notes.md says No rectangle is a worked check, not a binary guess, and Square is a guided demonstration; spec says Square is a card pick with checks; followed notes
  - cost_class new-engine because this spec holds the algebra-tiles engine
  - A.1a (term, coefficient names on hover) not a separate code in spec

## Unit Sense

- Spec: `tools/unit-sense/spec.md` . Module: math-9-units-and-quantities. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Units-match light: rack holds only needed cards plus two decoys and Undo is free, so cards can be tried until the light turns on
  - Holds up or Falls apart: two choices, a wrong pick only gets a hint and a retry
  - Report stepper: a few figure counts with free retries until it says fits the data
- **N-Q.A.1** (practiced, in Bench; Case board steps 1-3): build conversion-card chains; compare to claim; pick verdict
  - Parts of the standard the student never does (must add):
    - choose and interpret units consistently in formulas
    - choose and interpret scale and origin in graphs and data displays
- **N-Q.A.2** (claimed, in Bench): pick a starting quantity from a menu in Bench
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "define" step: the student must do it
  - Parts of the standard the student never does (must add):
    - define quantities for a modeling purpose (quantities are given by the case or menu)
- **N-Q.A.3** (practiced, in Case board step 4 Report): step significant figures until tool says fits the data
  - Parts of the standard the student never does (small, add if cheap):
    - limits on accuracy other than significant figures in products and quotients
- The module also lists codes this tool does not carry: N-Q.A.2.
- The read was unsure about (check these against the spec; the read may be wrong):
  - N-Q.A.2 depth claimed: Bench menu is picking, not defining
  - A.1 set practiced because the match light and verdict are beatable

## Model My World

- Spec: `tools/model-my-world/spec.md` . Module: math-9-creating-equations. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Linear cases 1, 3, 7: gap bars show the offset on each row, so slope and intercept can be tuned by trial with free checks
- **A-CED.A.1** (taught, in Cases 1,2,4,6 question cards): write inequality and answer one-variable questions
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - simple rational equations
- **A-CED.A.2** (taught, in Cases 1,3,4,6,7): type equation that hits every record row
  - Parts of the standard the student never does (must add):
    - graph equations with labeled axes and scales (tool plots)
    - three or more variables
- **A-CED.A.3** (taught, in Case 5): type constraint lines; read viable and non-viable mixes
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - constraints written as equations
    - systems of equations
- **A-CED.A.4** (taught, in Cases 3 and 7 rearranging step): solve a formula for another letter and test it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - show the solving steps
    - rearranging formulas beyond one linear step
- The read was unsure about (check these against the spec; the read may be wrong):
  - A.1 items counted as the four question cards; explicit one-variable writing is only case 2
  - cost_class new-engine for the safe parser and checkers; it uses the graphing kit for the plot
  - A.2 and A.1 depth taught because questions and exponential or quadratic cases are not beatable by trial

## Correlation Guessing Game

- Spec: `tools/correlation-guessing-game/spec.md` . Module: math-9-data-in-one-and-two-variables. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Is a line a good model? and Does x cause y? have two choices each, and the cause question always has the same answer (Not shown)
- **S-ID.A** (claimed, in Plot screen): box plots sit on each axis of the plot
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "represent" step: the student must do it
  - Parts of the standard the student never does (must add):
    - represent data with plots
    - compare center and spread of data sets
- **S-ID.B.6** (practiced, in Run rounds 6-9): say if a line is a good model; judge trick plots
  - To do: no model or guide: add one
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - represent data on a scatter plot (plots are generated)
    - describe the relationship in words
- **S-ID.C.7** (shown, in Run round 10): read the slope in context on the headline card
  - To do: the tool does the "interpret" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - interpret the intercept
    - student interprets the slope
- **S-ID.C.8** (taught, in Run rounds 1-10; Cloud lab): guess r for ten plots; play with Target r in Cloud lab
  - Parts of the standard the student never does (must add):
    - compute r with technology (the tool shows it)
    - explain r in words
- **S-ID.C.9** (practiced, in Run round 10): answer Does x cause y? after the headline round
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain why correlation does not show cause
    - name the lurking variable themselves
- The module also lists codes this tool does not carry: S-ID.A.1, S-ID.A.2, S-ID.A.3, S-ID.A.4, S-ID.B.5, S-ID.B.6a, S-ID.B.6c.
- The read was unsure about (check these against the spec; the read may be wrong):
  - C.8 taught: student estimates r and interprets it by eye; compute is done by technology
  - Residual plot shown at reveal (B.6b) not entered as a code
  - S-ID.A spelled as the bare cluster as the spec spells it

## Graph Story Lab

- Spec: `tools/graph-story-lab/spec.md` . Module: math-9-function-notation-and-graphs. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Function or Not a function: two choices on one story
- **F-IF.A.1** (practiced, in Oval track story 8, Read and Mark): drag cursor across oval; call Function or Not a function
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain why one input must give one output
    - other cases of functions versus relations
- **F-IF.A.2** (shown, in Read readout; Answer boxes): read f(x) notation and values as cursor moves
  - To do: the tool does the "use" step: the student must do it
  - Parts of the standard the student never does (must add):
    - write function notation themselves
    - evaluate from a formula
- **F-IF.A.3** (practiced, in Cups story 4): answer h(1), h(20); bracket whole-number domain
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - define a sequence recursively
- **F-IF.B.4** (taught, in Mark tasks, eight stories): flag extremes, bracket intervals, secant on stories
  - Parts of the standard the student never does (must add):
    - sketch a graph from a verbal description
    - key features from tables
    - symmetry, end behavior, periodicity
- **F-IF.B.5** (taught, in Mark tasks: tea, cups, parking): bracket the domain; refuse continuous domain for cups
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write the domain in a sentence
- **F-IF.B.6** (shown, in Secant tool; Compare toggle): pick two points; read secant slope with units
  - To do: the tool does the "calculate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - calculate the rate by hand from a table or formula
    - interpret the rate in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - F-IF.B.6 set shown since the tool computes the slope from picked points
  - A.1 and A.3 each sit in one story of eight; counted on_path anyway
  - tool-key on Answer tasks may be copying the readout

## Polynomials as Numbers

- Spec: `tools/polynomials-as-numbers/spec.md` . Module: math-9-polynomial-arithmetic. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Orders 1-4: result row sits above the target with free tries, so factor pairs can be found by trial
- **A-APR.A.1** (practiced, in Orders 1-6; Columns and Multiply examples): set factor or sum rows to hit a target polynomial
  - Parts of the standard the student never does (must add):
    - tool does each column sum and product
    - explain closure (one printed line)
    - factors above degree 2
- The read was unsure about (check these against the spec; the read may be wrong):
  - Columns and Multiply: tool computes, student watches; only Orders has the student choose rows
  - depth could be shown if Orders are skipped

## Intersection Quest

- Spec: `tools/intersection-quest/spec.md` . Module: math-9-systems-of-equations. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Add a check, Reach five items that differ, Put it on the main path.
- Checks a student can pass by guessing:
  - Shade course: solid or dashed and the side to shade are two-way choices with a test point shown, free retries
- **A-REI.C.5** (touched, in Race Eliminate lane; note under sum row): add scaled equations in the optional Eliminate lane
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "prove" step: the student must do it
  - Parts of the standard the student never does (must add):
    - prove the replacement keeps the solutions (a printed note only)
- **A-REI.C.7** (taught, in Race Curves course): solve line-with-curve systems by graph or substitution
  - To do: only 4 items: reach five or more that differ
- **A-REI.D.10** (practiced, in Practice lap): type or drag two graphs; read yes or no per point
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - say in own words that a graph is all its solutions (the readout states it)
- **A-REI.D.11** (practiced, in Race Curves course): find crossings by graph or by solving f = g
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain why the x-coordinates solve f(x) = g(x)
    - rational, absolute value, exponential, logarithmic cases
    - tables and successive approximations
- **A-REI.D.12** (taught, in Race Shade course): set boundary, solid or dashed, shade side; pin the overlap
  - To do: only 2 items: reach five or more that differ
- The module also lists codes this tool does not carry: A-REI.C.8, A-REI.C.9.
- The read was unsure about (check these against the spec; the read may be wrong):
  - D.11 given practiced although its verb is explain; student finds crossings but never explains
  - Practice lap has no prediction, so D.10 not explored
  - Lines course Graph lane could be beaten only at +10 s per wrong tap; not listed

## Launch Pad

- Spec: `tools/launch-pad/spec.md` . Module: math-9-quadratic-equations. Stage: built (the code changes after the spec). Sort: **fine**.
- Fixes: Close the guessable check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Launch mode lists the times at any height, so a mission answer can be read off without solving
  - Factor boxes (t - p)(t - q) are checked by expansion with free tries, so small integer pairs can be tried
- **A-REI.B.4a** (taught, in Missions 7, Complete the square method): complete the square on mission 7; fill formula derivation blanks
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - derive the formula without fill-in blanks
- The read was unsure about (check these against the spec; the read may be wrong):
  - A-REI.B.4 parent not entered; 4a and 4b are the finest codes
  - Notes say the curve is hidden until a prediction checks, which blunts the Launch-mode shortcut inside Missions

