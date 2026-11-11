# Spec fixes: math, grade 11

8 tools: 7 rework, 1 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (7), Close the guessable check (4), Add the missing part (8), Add a model or a guide (2), Add a check (4), Reach five items that differ (3), Put it on the main path (3), Teach the code or drop it (1).

Shape for this course: ../../agents/catalog/shape/math-11.md.

## Undo Machine

- Spec: `tools/undo-machine/spec.md` . Module: math-11-building-and-inverting-functions. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Add a check, Reach five items that differ, Put it on the main path, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Undo levels 1-6 and 12: about 15 parts and 2-4 slots, Run names the lost tokens, hint 2 names each opposite, free tries
  - Gate levels 7, 8, 10: a switch for >= or <= and a value from -10 to 10 with Run feedback naming the crash, free tries
- **F-BF.A.1c** (practiced, in Workshop; formula strip): build a forward chain of machines and read f(x)
  - To do: no model or guide: add one
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - a real context such as the balloon example
    - write the composite in function notation themselves
- **F-BF.B.4a** (practiced, in Workshop; Puzzles 1-6, 12): build the undo chain in reverse order, Run tokens
  - Parts of the standard the student never does (must add):
    - solve f(x) = c as an equation
    - write the expression for the inverse (the tool writes g(x))
    - rational example such as (x+1)/(x-1)
- **F-BF.B.4b** (shown, in Workshop verdict and formula strip): watch Run bring tokens home; strip reads g(f(x)) = x
  - To do: the tool does the "verify" step: the student must do it
  - Parts of the standard the student never does (must add):
    - verify by composing the two expressions themselves
    - write g(f(x)) = x with algebra
- **F-BF.B.4c** (claimed, in Graph view, Mirror): none: Mirror button draws the reflection, no values are read
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "read" step: the student must do it
  - Parts of the standard the student never does (must add):
    - read values of the inverse from a graph
    - read values of the inverse from a table
- **F-BF.B.4d** (practiced, in Workshop Gate; Puzzles 7, 8, 10): set a gate (x >= c or x <= c) so the fold is safe, then undo
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - restrict the domain of a named function in symbols
    - say which restricted domain makes the function invertible
- **F-BF.B.5** (touched, in Parts bin; Puzzle 6): use Power of 2 and Log base 2 as an undo pair
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - explain why exponents and logs are inverses
    - solve exponent or log problems
    - bases other than 2
- The module also lists codes this tool does not carry: F-BF.A.1, F-BF.A.1a, F-BF.A.1b, F-BF.A.2, F-BF.B.3.
- The read was unsure about (check these against the spec; the read may be wrong):
  - F-BF.B.4c scored claimed because Mirror is a button and nothing is read; touched is possible
  - Puzzles are labeled optional, Workshop holds the same build, so 4a/4d count on_path
  - function-machine engine does not exist yet, so new-engine

## Imaginary Island

- Spec: `tools/imaginary-island/spec.md` . Module: math-11-complex-numbers. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Put it on the main path.
- **N-CN.A.1** (shown, in Explore readouts and dial): Drag the lantern, read z = a + bi, watch the i-power dial
  - To do: the tool does the "know" step: the student must do it
  - Parts of the standard the student never does (must add):
    - state i squared equals -1 unprompted
    - state that every complex number is a + bi
- **N-CN.A.2** (shown, in Explore operations; Clue Trail (optional)): Press x i, Square it, + w, x w and read worked lines
  - To do: the tool does the "use" step: the student must do it
  - Parts of the standard the student never does (must add):
    - subtract (no subtract button)
    - multiply two complex numbers they choose
    - write the expansion with i squared themselves
- **N-CN.C.7** (shown, in Springs mode): Slide b and c, watch springs leave the Real Road; read worked formula
  - To do: the tool does the "solve" step: the student must do it
  - Parts of the standard the student never does (must add):
    - solve a quadratic themselves
    - leading coefficient other than 1
    - write the complex solutions
- **N-CN.A.3** (touched, in Explore Reflect button; Clue Trail 10 and 11): Press Reflect; read |z|
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "find" step: the student must do it
  - Parts of the standard the student never does (must add):
    - use conjugates to find quotients
    - find the conjugate or modulus themselves
- **N-CN.B.4** (shown, in Explore readouts and layers): Read distance and heading of the lantern; Distance rings and Heading spokes
  - To do: the tool does the "represent" step: the student must do it
  - Parts of the standard the student never does (must add):
    - convert between rectangular and polar form
- **N-CN.B.5** (shown, in Explore animations, Turned by line): Watch x i, x w and Reflect turn, stretch and mirror the lantern
  - To do: the tool does the "represent" step: the student must do it
  - Parts of the standard the student never does (must add):
    - predict the result before the operation (prediction only in optional Clue Trail)
    - subtraction geometry
- The module also lists codes this tool does not carry: N-CN.C.8, N-CN.C.9.
- The read was unsure about (check these against the spec; the read may be wrong):
  - N-CN.B.4 and B.5 wording not in packet; spec says 'touches without requiring them' but multiplication as turning is the tool's one idea, so marked shown
  - Clue Trail (optional, guess pin then Walk it, tool-key within 0.25) is the only place the student predicts
  - minutes midpoint of 15 to 25

## Outbreak Model

- Spec: `tools/outbreak-model/spec.md` . Module: math-11-exponential-and-logarithmic-functions. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **F-LE.A.4** (shown, in Ask when mode): Drag the target line; read Solve it in bases 2, 10 and e
  - To do: the tool does the "express" step: the student must do it
  - Parts of the standard the student never does (must add):
    - write the logarithm form themselves
    - solve for t from their own equation
    - evaluate with technology (tool shows the value)
- **F-IF.C.8b** (shown, in Same curve, three ways card): Switch Describe growth by; read factor and percent growth
  - To do: the tool does the "interpret" step: the student must do it
  - Parts of the standard the student never does (must add):
    - interpret a given expression themselves
    - classify given expressions as growth or decay
- **F-IF.C.9** (shown, in Grow mode): Toggle Compare steady growth; read two milestone columns
  - To do: the tool does the "compare" step: the student must do it
  - Parts of the standard the student never does (must add):
    - compare two functions given in different ways and state which is larger
- The module also lists codes this tool does not carry: F-IF.C.7, F-IF.C.7a, F-IF.C.7b, F-IF.C.7c, F-IF.C.7d, F-IF.C.7e, F-IF.C.8, F-IF.C.8a.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Student never solves: Ask when shows all steps; Guess first is optional and unscored
  - Hit the ceiling mode (logistic limit) has no listed code
  - Virus stories are made up; sensitive flag not set
  - minutes midpoint of 15 to 30

## Rollercoaster Polynomials

- Spec: `tools/rollercoaster-polynomials/spec.md` . Module: math-11-polynomial-functions. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Survey: the stake snaps to 21 half-steps with a free remainder at each, so trying every position finds the zeros without choosing candidates
  - Commissions blueprints B1-B4: live 'Zeros match yes/no' lets a student nudge zeros until each flips to yes
- **A-APR.B.2** (practiced, in Survey mode, Plans 1-9): Move the stake, press Survey here, read the synthetic division remainder
  - Parts of the standard the student never does (must add):
    - explain why the remainder equals p(a)
    - do the synthetic division (tool does it)
    - state the factor if and only if themselves
- **A-APR.B.3** (practiced, in Build mode; Commissions (optional)): Plant zeros, set multiplicity and leading coefficient, read the graph
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - read zeros from a given factored form
    - sketch the graph by hand
- **A-APR.C.4** (shown, in Build button; Survey end check at x = -2, 0, 2): Press Show the multiplication; read the equal-values check table
  - To do: the tool does the "prove" step: the student must do it
  - Parts of the standard the student never does (must add):
    - prove an identity
    - use an identity for numerical relationships such as Pythagorean triples
- **F-IF.C.7c** (practiced, in Build readouts): Build tracks and read the end-behavior sentence
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - state end behavior themselves (tool prints the sentence)
    - graph a polynomial given symbolically
- The module also lists codes this tool does not carry: A-APR.C.5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Build has no goal; checks only in optional Commissions
  - F-IF.C.7c is support in the spec
  - minutes midpoint of 20 to 40

## Savings Plan

- Spec: `tools/savings-plan/spec.md` . Module: math-11-sequences-and-series. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Plan Desk customers 2-6: first deposit set on a cent-step slider with live 'short by $' and cap checks, free edits before the one Run
- **F-IF.A.3** (shown, in Race plan cards; chart dots): change a plan and read its explicit and recursive rule
  - To do: the tool does the "recognize" step: the student must do it
  - Parts of the standard the student never does (must add):
    - recognize that a sequence is a function
    - say the domain is a subset of the integers
    - write a recursive definition themselves
    - Fibonacci-style recursion
- **A-SSE.B.4** (shown, in Show the shortcut drawer; Plan Desk formula): step through the 5-step derivation with the plan's own numbers
  - To do: the tool does the "derive" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - derive the formula themselves (the drawer shows each step)
    - use the formula to solve problems on the main path (Desk is optional)
    - a mortgage-style context
- The read was unsure about (check these against the spec; the read may be wrong):
  - Plan Desk is optional, so the 'use the formula' half of A-SSE.B.4 is not on the main path
  - Desk 'Show the formula' never solves for the unknown, so the live checks may carry students

## Poll Workshop

- Spec: `tools/poll-workshop/spec.md` . Module: math-11-statistical-inference. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part, Add a check, Put it on the main path.
- **S-IC.A.1** (practiced, in Workshop; Run poll, Run 50 more, Reveal): pick method, wording and n, run a poll, reveal the truth
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (small, add if cheap):
    - say in words how a sample statistic estimates a population parameter
- **S-IC.B.3** (touched, in Workshop methods; Case file prompts): choose among sampling methods and read the Case file card
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - experiments
    - observational studies
    - purposes and differences among the three study types
    - explain how randomization relates to each (prompts have no answer box)
- **S-IC.B.4** (practiced, in Workshop Results and wall; Budget desk): read p-hat and plus or minus, see 50 repeat polls on the wall
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - estimate a mean (proportions only)
    - develop the margin of error from the simulation (the tool prints the formula value)
    - compute the estimate themselves
- **S-ID.A.4** (touched, in Headline wall, Normal curve toggle): toggle the normal curve over the dots
  - To do: off the main path or can be skipped: put it on the path
  - To do: the tool does the "use" step: the student must do it
  - Parts of the standard the student never does (must add):
    - estimate population percentages from a normal model
    - say when a normal model is not appropriate
    - use tables or a calculator for areas
- The module also lists codes this tool does not carry: S-IC.A.2, S-IC.B.5, S-IC.B.6.
- The read was unsure about (check these against the spec; the read may be wrong):
  - S-IC.A.1 is understand but has no predict step in the spec (notes only suggest asking aloud), so practiced not explored
  - Whether Case file prompts count toward S-IC.B.3 explaining; they have no answer box
  - Budget desk checks are simulated outcomes; no beatable found
  - S-IC.B.6 not named in spec but Case file touches it

## Ferris Wheel

- Spec: `tools/ferris-wheel/spec.md` . Module: math-11-trigonometric-functions. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Match (optional): Check names the biggest gap and where, with free tries and Show my curve, so sliders can be nudged to a match without reading amplitude, midline or period
- **F-TF.A.1** (shown, in Unit Circle mode): Press One radian and Unroll the arc; read arc = theta
  - To do: the tool does the "understand" step: the student must do it
- **F-TF.A.2** (shown, in Unit Circle mode, Show cosine): Ride the unit circle and watch sin theta draw past 2 pi
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain how the unit circle extends trig to all real numbers
    - negative angles and angles past 4 pi
    - tangent
- **F-TF.B.5** (practiced, in Ride mode; Match (optional)): Set radius, hub, turn time and boarding point; read the equation
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - write the model equation themselves (tool prints it)
    - choose sine or cosine
    - start from a described real situation
- **F-TF.C.8** (shown, in Unit Circle identity readout; sideways-distance line): Read the live cos squared + sin squared line
  - To do: the tool does the "prove" step: the student must do it
  - Parts of the standard the student never does (must add):
    - prove the identity
    - use it to find a value from another and the quadrant
- The module also lists codes this tool does not carry: F-TF.A.3, F-TF.A.4, F-TF.B.6, F-TF.B.7, F-TF.C.9.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Spec names clusters F-TF.A, B, C only; split into A.1, A.2, B.5, C.8 by wording
  - B.5 practiced: Ride has no check; Match is optional
  - minutes midpoint of 15 to 30

## Work Rate Crew

- Spec: `tools/work-rate-crew/spec.md` . Module: math-11-rational-expressions-and-equations. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Add a model or a guide, Reach five items that differ.
- **A-APR.D.7** (practiced, in Calls: Rate sum and Equation steps): Combine two crew rates into one fraction; build rational equations
  - To do: no model or guide: add one
  - Parts of the standard the student never does (must add):
    - add, subtract, multiply or divide rational expressions with variables (rates are numbers)
    - subtract, multiply, divide
    - the closure idea
- **A-APR.D.6** (practiced, in Quote sheet): Fill q and r boxes to rewrite 4x/(x + 4)
  - To do: no model or guide: add one
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - use long division or inspection visibly
    - any expression beyond this one
    - numerators of degree 2
- **A-REI.A.2** (taught, in Calls 3-5; Office audit): Build equations, solve, mark roots Fits or Doesn't fit, audit worksheets
  - Parts of the standard the student never does (must add):
    - radical equations
    - write own examples of extraneous solutions
    - show the algebra steps (answers typed)
- The read was unsure about (check these against the spec; the read may be wrong):
  - D.7 practiced: rates are numeric, tool writes the sum, no hint named
  - A-REI.A.2 taught: equation step tool-rule, typed answers; Check in the original turns the sheet into worked practice (notes)
  - minutes midpoint of 20 to 40

