# Frame read: calculus (Math, Calculus, grade 12 core elective), 2026-11-16

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md, bar docs/RUBRIC-MATH-HS.md). I did not
write this frame.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-HS.md in full, data/plans/later.csv
  (L15, L25, L49), the lessons list in docs/pipeline/briefs/frame-write.md.
- The frame docs/courses/calculus/frame.md in full; its row in data/plans/frames.csv (11 units, 160 days, 50-minute
  lessons, 5 a week, 32 weeks, year). No data/plans/calculus/source-map.csv exists yet; the Source map is the frame's
  own table.
- All 30 calc- rows of data/progressions/math.csv, and the rows they assume or lean on: every pc- row, and
  alg2-logarithms, alg2-exp-log-graphs, alg2-number-e-continuous, alg2-unit-circle-radians, alg2-trig-functions-graphs,
  alg2-geometric-series, alg2-normal-distributions, geo-arcs-sectors-radians; a scan of which grade 11 and 12 rows
  assume each readiness row.
- data/standards/curio-math-electives.txt (CUR-CA.1 to CUR-CA.30 and the file notes) and G-GMD.A.2 in
  data/standards/ccss-math-standards.txt.
- The frames before and beside: docs/courses/algebra-ii/frame.md (brief, Seams, Units) and
  docs/courses/precalculus/frame.md (brief, Seams, the "Handed on to Calculus" table, units 1, 9, 10, check 3).
- Cross-subject: the unit tables of docs/courses/physics/frame.md (units 1 to 3 and the math-readiness bullet),
  docs/courses/chemistry/frame.md (unit 8) and docs/courses/biology/frame.md (unit 5).
- The base-text scout notes (side-session notes, base-text-scout-2026-11-16.md, section 3, Calculus): licence and
  table of contents of Dale Hoffman, Contemporary Calculus. I did not open the author's site.
- Earlier reads of the same layer, for REPEAT tags: docs/reviews/frame-algebra-ii-2026-11-14.md and
  frame-psychology-2026-11-16.md.
- Gates: `python -X utf8 scripts/plan.py check`: frame calculus 0 failures, 11 units, 160 days (151 in units, 9 for
  checks and respond days); the Algebra II note "Seams does not name calc-..." is For the lead 7 and stays the lead's.
  `python -X utf8 scripts/stale.py check`: 60 files, 0 failures.

Arithmetic I checked and found right: every unit's days equal its rows' loads (14, 22, 14, 15, 16, 9, 9, 17, 10, 12,
13 = 151); the readiness days 36, 50 and 102 are the respond days of units 2, 3 and 7 once check 1 (days 82 to 84) sits
after unit 5; the week ranges in Cross-subject match the day count; all 30 rows sit in exactly one unit; every
CUR-CA code and G-GMD.A.2 is owned by one row and sits in one unit; the Source map places every section of the scout's
table of contents (chapters 0 to 11) once, and maps no NC or reference source.

## Verdict

For a class that took Precalculus the frame is sound: the order teaches well, the mathematics is right almost
everywhere, the base text is placed section by section and the outcome list matches an exam-equivalent two-semester
course. The biggest risk is the route For the lead 1 recommends, Calculus straight after Algebra II: the frame's 151
days hold both semesters only because every day is already spoken for, and the just-in-time teaches are neither sized
nor complete (logarithm laws, the addition and double-angle identities, special-angle values and trigonometric
equations are needed and never named), so a straight-from-Algebra-II class cannot reach units 9 to 11 as written. The
one change that matters most is to size the bridge honestly and let Cory choose between a Precalculus-first route and
a straight route with a named bridge and a named cut (findings 1 and 2).

## Findings, most serious first

### 1. The straight-from-Algebra-II route does not fit the days (serious; likely)

LAYER frame, process. REPEAT yes (days by load, frame-write lesson 9).

What is wrong. "Two ways in" says a class straight from Algebra II gets each just-in-time teach "inside the row's own
days (no day is added)", and For the lead 1 picks that as the route for now. "A tight course" says every unit already
runs on its load with no spare day, and each unit's days include its end-of-unit assessment and respond day (22 of
the 151 days). The just-in-time content is Precalculus content that the Precalculus rows give 86 days to (the 14 pc-
rows named in the second Seams table, by their own loads), before the four rows finding 2 adds. The sharpest cases:

| Calculus row (load) | Teaching days left after the unit's share of assessment | Just-in-time content it must also hold | Precalculus load for that content |
|---|---|---|---|
| calc-chain-rule-inverses (6) | about 5 | composition, inverse functions, inverse trigonometric functions | 5 + 6 + 5 |
| calc-parametric-vector-motion (6) and calc-polar-calculus (4), unit 9 (10) | 8 for both rows | parametric equations, vectors, polar coordinates and polar graphs | 6 + 6 + 7 |
| calc-series-convergence (6) | about 5 | sigma notation, infinite geometric series | 6 |
| calc-implicit-differentiation (4) | about 3 | ellipse and hyperbola standard forms | 9 (pc-conics) |

From memory (not opened): the published pacing for the two-semester calculus exam course allots roughly 110 to 120
class periods of instruction, and that course assumes a full precalculus year. The frame's roughly 129 teaching days
are enough for that content with Precalculus behind it, which is why the frame is sound for the Precalculus route. They
are not enough for that content plus a bridge of what I estimate at 15 to 25 days of new Precalculus work.

Why it matters. A unit writer told "no day is added" will either write just-in-time teaches of ten minutes that do not
teach (a straight-from-Algebra-II student meets polar area on a polar grid introduced the same lesson) or run over,
and the run-over lands on units 9 to 11, the series and Taylor work, which then get cut by the calendar, not by a
decision.

Exact fix. (a) In "Two ways in", replace "(no day is added, which is part of why the course is tight)" with: "The
row loads are written for a class that took Precalculus. For a class straight from Algebra II the just-in-time teaches
need about 20 more days than the loads hold; the route decision (For the lead 1) says where they come from." (b) Give
each row in the second Seams table a size column ("about N lessons of just-in-time teaching", the unit plan confirms).
(c) Rewrite For the lead 1 as a choice between: Precalculus first (via L15, or both courses in one year) with the
current loads; or straight from Algebra II with a named bridge (about 20 days) paid for by a named cut, which is scope
(For Cory 1). The frame should not recommend the straight route as costless.

### 2. Four Precalculus prerequisites are used but never named, and one seam misstates what Algebra II hands on (serious; firm)

LAYER frame, progression. REPEAT yes (both ends of every handoff, lesson 7; each thread starts where it is first used,
lesson 5).

What is wrong. The second Seams table (and the Precalculus frame's "Handed on to Calculus" table, which mirrors it)
names 13 pc- rows. Calculus also leans on four more, which the Algebra II rows say are not taught there:

- **Logarithm laws and ln as the inverse of e to the x (pc-logarithmic-functions).** alg2-logarithms' own limits:
  "logarithms as inverse functions and the laws of logarithms are for advanced courses". Calculus needs both in unit 2
  (the derivative of ln x, logarithmic differentiation), unit 5 (ln of an absolute value as an antiderivative), unit 6
  (partial fraction answers combined), unit 7 (ln of y = kt + C to y = Ce to the kt). The first Seams table's row for
  alg2-exp-log-graphs says it hands on "the logarithm as the exponential's inverse"; that row's limits say "logarithmic
  graphs read as the solutions of exponential equations, not as inverses (+)". The brief's fluency bullet also lists
  "exponent and logarithm rules" among "the Algebra II rewriting skills".
- **The addition and double-angle identities (pc-trig-identities, F-TF.C.9 and CUR-PC.6).** Needed in unit 1 for the
  limit of (1 - cos x)/x, in unit 2 for the derivative of sine "explained from ... limits" (sin(x + h) expanded), and in
  unit 9 for polar area (finding 3).
- **Exact values at the special angles (pc-special-angles-symmetry, F-TF.A.3).** Needed for every derivative or
  integral evaluated at pi/6, pi/4, pi/3. Algebra II reaches some exact values by symmetry but leaves F-TF.A.3 as (+).
- **Solving trigonometric equations (pc-trig-equations, CUR-PC.7).** Needed for critical points of trigonometric
  functions (unit 4) and the intersections of two polar curves (unit 9, "the region between two of them").
- Also, adding rational expressions (A-APR.D.7, pc-rational-functions-inequalities) is first used in unit 1 ("common
  denominators" in CUR-CA.2), but its just-in-time teach is placed in unit 6.

Why it matters. A straight-from-Algebra-II student will meet these as unexplained steps, and a Precalculus student gets
no retrieval of the very skills the Precalculus frame lists as its own fluencies (special-angle values, identities,
logarithm rules).

Exact fix. In the frame: add four rows to the second Seams table: calc-derivative-rules picks up pc-trig-identities
(just-in-time: sin(x + h) by the addition formula) and pc-special-angles-symmetry (exact values at the special
angles); calc-chain-rule-inverses picks up pc-logarithmic-functions (ln as the inverse of e to the x, and the three
logarithm laws); calc-mean-value-extrema picks up pc-trig-equations (solving sin x = c and cos x = c on an interval);
calc-polar-calculus also picks up pc-trig-identities (cos squared and sin squared from the double angle). Move the
"adding rational expressions" just-in-time teach to calc-limit-techniques (unit 1), with unit 6 as retrieval. Replace
the alg2-exp-log-graphs cell "the logarithm as the exponential's inverse, solutions of f(x) = g(x) as intersections"
with "logarithmic graphs and solutions of f(x) = g(x) as intersections (the inverse relation is pc-logarithmic-functions,
by course order)". In the fluency bullet replace "exponent and logarithm rules" with "exponent rules, and the logarithm
laws from Precalculus (or unit 2's just-in-time teach)". In data/progressions/math.csv notes (progression layer): the
same pc- rows named in calc-derivative-rules, calc-chain-rule-inverses, calc-mean-value-extrema and
calc-polar-calculus, and calc-chain-rule-inverses' re-entry text "(the logarithm as the exponential's inverse)"
replaced by "(logarithms as solutions of exponential equations)". The Precalculus frame's handed-on table takes the
same four rows (both ends).

### 3. Polar area needs integrals of sin squared and cos squared, which no unit teaches (serious; firm)

LAYER frame, standard, base text. REPEAT new.

What is wrong. CUR-CA.26 owns the area of regions bounded by polar curves. The area is one half the integral of r
squared; for every standard polar curve (a cardioid r = 1 + cos theta, a rose r = cos 2 theta, a circle r = 2 sin
theta) that integrand is a square of a sine or cosine, which needs the power-reducing identity. CUR-CA.17 does not name
it, and the Source map leaves out base section 8.5 (Integrals of Trigonometric Functions) as "not in CUR-CA.17".

Why it matters. Unit 9's central outcome cannot be done by hand as the outcomes stand; a writer either evaluates every
polar area with technology (which the outcome does not say) or teaches an untaught integral inside a 4-day row.

Exact fix. Add to CUR-CA.17: "and integrals of the squares of sine and cosine with the double-angle identity"; in unit
6's What students learn add the same clause; change the Source map row for 8.4 and 8.5 to two rows: "8.4 Trigonometric
Substitution: left out, unit 6's extension only" and "8.5 Integrals of Trigonometric Functions: 6, keep in part: sin
squared and cos squared by the double-angle identity only (needed for polar area, unit 9); other powers are left out".
The day comes out of unit 6's six-day load (the choose-the-method practice absorbs it) or, if the reader of the scope
finds no room, out of the trim order. The double-angle identity itself is finding 2's just-in-time teach.

### 4. Two outcomes are taught in part, and the outcome list drops clauses its rows teach (moderate; firm)

LAYER standard, frame. REPEAT yes (standards in full, lesson 4).

What is wrong.
- CUR-CA.5 says "exponential and logarithmic functions"; the row and unit 2 teach only e to the x and the natural
  logarithm. Base-b exponentials and logarithms (b to the x, log base b of x) are never placed.
- CUR-CA.10 says "limits of indeterminate forms"; the row and unit 3 teach only 0/0 and infinity over infinity. The
  forms 0 times infinity, infinity minus infinity and 1 to the infinity are not placed, though 1 to the infinity is the
  very limit that defines e in Algebra II (alg2-number-e-continuous).
- The outcome text is narrower than its rows in three places: CUR-CA.1 leaves out limit notation, CUR-CA.3 leaves out
  choosing a constant to make a piecewise function continuous, CUR-CA.27 leaves out limits of sequences. Checks name
  codes, so a clause missing from the code text can drop out of the assessment.
- One idea every first-year course states is missing from the list: a differentiable function is continuous, and the
  converse fails (absolute value at 0).

Why it matters. An end-of-unit assessment written to the outcome text will test what the unit never taught (base-b
derivatives, other indeterminate forms) or skip what it did teach (sequence limits).

Exact fix. Narrow or teach, item by item. CUR-CA.5: keep the wording, and add to unit 2's What students learn (in
calc-chain-rule-inverses, where the chain rule makes it one step) "b to the x and log base b of x, from e to the x ln b
and the change of base". CUR-CA.10: reword to "limits of the forms 0/0 and infinity over infinity, and of products and
differences rewritten into them" and add the same to unit 3 (1 to the infinity stays an extension, shown once on the
compounding limit for e). CUR-CA.1 add "write it in limit notation"; CUR-CA.3 add "choose a constant to make a
piecewise function continuous"; CUR-CA.27 add "find limits of sequences"; CUR-CA.4 add "and explain why a
differentiable function is continuous but not the reverse", with the same clause in unit 2's text. Each is a wording
change to Curio Class's own list and the unit text, with no load change except the CUR-CA.10 clause (inside unit 3's
four days of calc-linearization-limits).

### 5. Three ideas are used before the unit that teaches them (moderate; firm)

LAYER frame, progression. REPEAT yes (each thread starts where it is first used, lesson 5).

What is wrong.
- **Concavity in unit 3.** CUR-CA.10 judges a tangent-line estimate "over or under from concavity seen on a graph";
  concavity is defined in unit 4 (CUR-CA.12).
- **Sector area before unit 8.** The squeeze argument for sin x over x (unit 1) compares a triangle with a circular
  sector, and polar area (unit 9) is built "from thin sectors"; both use the sector area of geo-arcs-sectors-radians,
  which the first Seams table picks up first in unit 8 (arc length) only.
- **The derivative of ln x before inverses.** calc-derivative-rules (CUR-CA.5) differentiates ln x, but explains only
  the sine and exponential derivatives; the natural explanation (ln x as the inverse of e to the x) comes in
  calc-chain-rule-inverses, the next row.

Why it matters. Each forces a writer to improvise a definition mid-lesson, and the readiness and retrieval plan misses
the sector-area thread in unit 1.

Exact fix. Unit 3: replace "judged over or under from concavity seen on a graph" with "judged over or under from
whether the graph bends up or down near the point, read from the sign of the second derivative (unit 2); unit 4 names
this concavity". First Seams table: geo-arcs-sectors-radians is "Unit 1, calc-limit-techniques (sector area in the
squeeze argument); unit 8, calc-arc-length; unit 9, calc-polar-calculus", retrieval (built on by alg2-unit-circle-radians);
add it to calc-limit-techniques' and calc-polar-calculus' assumes in data/progressions/math.csv. The ln order is a day
order inside unit 2 (Settled by the expert).

### 6. The fallback scope "units 1 to 5 and 8" contradicts the frame's own dependencies and semester line (moderate; firm)

LAYER frame. REPEAT new.

What is wrong. "A tight course" calls units 1 to 5 and 8 "the first-semester content"; check 1 calls units 1 to 5 the
first semester's content. Unit 8's "Why this unit, here" says it "Needs ... unit 6's methods to evaluate the
integrals", and unit 8 carries arc length, which the frame elsewhere treats as second-semester work. So the fallback
drops a unit that a kept unit depends on, and misnames what it is.

Why it matters. A school taking the fallback (or Cory deciding it) would teach unit 8 without the integration methods
it is said to need.

Exact fix. In unit 8's reason replace "unit 6's methods to evaluate the integrals" with "unit 5's substitution for its
core integrals (unit 6's methods only where an item names them)". In "A tight course" replace "(the first-semester
content)" with "(first-semester content plus the measuring unit; differential equations, motion in the plane and series
are left out)", and say the decision is Cory's (For Cory 1), not the lead's.

### 7. The L49 answer is right in shape but drops the time question (moderate; judgment call)

LAYER process. REPEAT yes (the focus figure does not measure time, frame-algebra-ii-2026-11-14.md finding 2).

What is wrong. The frame replaces focus 1a to 1c with an owned-outcome account and sets no time line. Coverage in full
and "no day only reteaches" are the right replacements for 1a and the gap 7 check. But 1b's question (where does the
time go) still has a meaningful form here: the share of instructional minutes spent on owned outcomes rather than on
review and just-in-time Precalculus teaching. With finding 1 that share is the course's main risk, and the account as
written cannot see it.

Why it matters. Without a minutes line, just-in-time and review time can grow unnoticed until units 10 and 11 shrink.

Exact fix. Confirm L49 with one addition, for Precalculus, Statistics and Calculus alike: "The owned-outcome account
states, in the scope and sequence, the minutes on owned outcomes, the minutes of review and the minutes of
just-in-time teaching, each counted once, check and respond days left out; for Calculus the review and just-in-time
minutes for a Precalculus class stay under about 5 percent, and for a straight-from-Algebra-II class are shown
separately." The replacement line For the lead 6 proposes for RUBRIC-MATH-HS.md then reads: "Precalculus, Statistics
and Calculus apply this file except focus 1a to 1c, replaced by an owned-outcome account with a minutes line
(later.csv L49)". Coherence 1d and 1e, assessment, rigor, the practices, supports and the multilingual criteria
applying in full is right; I agree with the frame there.

### 8. The paper path misses four tools the units need (minor; firm)

LAYER frame. REPEAT yes (paper path, lesson 14).

What is wrong. The brief's paper path covers graphs, slope fields, sums, Euler steps and partial sums, but not: polar
grid paper for unit 9 (the Precalculus frame prints its own); a table of t values for parametric curves; intersection
points for area between curves (unit 8 says "by algebra or technology"); and fitting a cooling or population model to
given data (unit 7's modeling task), which on a basic calculator needs a linearising step.

Exact fix. Add to "Technology and the paper path": "polar grid paper printed from the course's own sheets (unit 9),
parametric curves plotted from a printed table of t values, intersection points found by a table of values and
successive approximation as in Algebra II (A-REI.D.11), and a cooling or growth model fitted by taking logarithms of
the given values (temperature minus room temperature) and fitting a line by eye on grid paper".

### 9. The orbit lean is a system of equations, not the first-order equations unit 7 teaches (minor; likely)

LAYER frame. REPEAT new.

What is wrong. Unit 7 lists "the step-by-step orbit model of Physics" as a context for Euler's method. Physics' orbit
model steps position and velocity together in two dimensions (a system), and the Physics frame keeps it a supplied
model with no vector components. Unit 7 teaches Euler's method for one equation y' = f(x, y).

Exact fix. In unit 7 and in the Cross-subject table, call the orbit a "same idea" link named in one sentence, not a
task: "Physics' stepped orbit is Euler's idea applied to two quantities at once; students step only one equation
here."

### 10. One Seams sentence is stale now that the Precalculus frame exists (minor; firm)

LAYER process. REPEAT yes (stale notes).

What is wrong. "The Precalculus frame sets its unit numbers; this table names rows only." The Precalculus frame now
passes the gate with its units set (pc-informal-limits unit 10, pc-polar-graphs unit 8, and so on), and its own
handed-on table gives them.

Exact fix. Replace the sentence with "Precalculus unit numbers are from docs/courses/precalculus/frame.md" and add each
row's unit in the second column (for example "pc-informal-limits (Precalculus unit 10)").

### 11. The modeling cycle leaves out two steps (minor; firm)

LAYER frame. REPEAT new.

What is wrong. The Modeling bullet lists "assumptions, model, solution, interpretation, check, revision"; the rubric's
gap 2 and the Precalculus frame use the full cycle "assumptions, model, computation, interpretation, validation,
revision, report".

Exact fix. Replace the list with "(assumptions, model, computation, interpretation, validation, revision, report)" and
add "with our own rubric" as Precalculus does.

## Checked and found right (do not undo)

- Unit order: limits, derivative rules all in one unit, applications, accumulation, methods, differential equations,
  measuring, the plane, series, Taylor. Every "needs" in the units' reasons holds except finding 6. Improper integrals
  before the integral test, L'Hospital beside linearization, partial fractions (unit 6) before the logistic equation
  (unit 7), arc length (unit 8) before parametric arc length (unit 9), the ratio test (unit 10) before intervals of
  convergence (unit 11) are each right.
- Mathematical statements checked and correct: the three ways a limit fails; the hemisphere matched with a cylinder
  less a cone for G-GMD.A.2; discs and washers about any horizontal or vertical line; 1/x against 1/x squared; the
  tangent line as the degree 1 Taylor polynomial; the Lagrange and alternating series error bounds; the five Taylor
  series named.
- G-GMD.A.2 is taught in full (sphere and "other solids") and the reason for owning it here holds.
- Fluency without a timer, the untimed year-end fluency station, and the check plan (fresh codes named, recent
  evidence reused with its date).
- The Source map: every section placed once, each move from the base text's order given a reason, the LibreTexts copy
  excluded, 7.6 and 7.7 left out as unfinished at source, the base-text record left to the load (For the lead 3).
- Cross-subject: each Physics, Chemistry and Biology unit named teaches the lean in an earlier year at the weeks given.
- The readiness count by grade number and the For the lead 2 rewording of the row notes.
- The outcome list is in Curio Class's own words as far as I can judge from memory of the published exam course
  description, and its scope matches an exam-equivalent two-semester course.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, counted by units, days or time | Not applicable as written (no major work for an outcome list); its stand-in is finding 7 |
| A supporting cluster that does not practise major work | Not applicable |
| A source map row with no keep, split, merge, cut or ours decision | Met: every row decided (8.5 changes, finding 3) |
| Progression: a model used before the grade that builds it | Met for the course's own models; missed for sector area (finding 5) |
| Progression: a skill owned twice at the same depth, or a skipped handoff | Missed: four Precalculus handoffs unnamed (finding 2) |
| Progression: a limit broken | Met |

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 2 day order: the derivative of ln x is first read from the slopes of its graph (1/x) in calc-derivative-rules, then proved from e to the ln x = x on the first inverse-derivative day of calc-chain-rule-inverses | Gives the rule when the fluency set needs it and the reason once the tool exists (finding 5) | docs/courses/calculus/frame.md, unit 2 What students learn |
| The arc-length check on a circle uses y = root(r squared - x squared) from x = 0 to x = r/2 (angle pi/6, length pi r/6), not a quarter circle | The quarter-circle integral is improper at x = r; this arc is proper and exact | frame.md unit 8; calc-arc-length notes |
| The "other solid" for G-GMD.A.2 is the spherical ring (napkin ring): by Cavalieri its volume depends only on its height, checked by washers later in the unit | A true Cavalieri result past G-GMD.A.1's cone and pyramid, and it joins the two halves of the unit | frame.md unit 8 |
| The logistic model is read from dP/dt = kP(1 - P/K): carrying capacity K and fastest growth at P = K/2 from the equation; its explicit solution is shown once as a worked example with unit 6's partial fractions, not required of students | Matches CUR-CA.20's wording (model and read) and keeps unit 7 inside 9 days | frame.md unit 7 |
| Improper integrals compare 1/x and 1/x squared on both [1, infinity) and (0, 1] | Shows students that the same pair swaps behaviour at an unbounded integrand | frame.md unit 6 |
| Euler's method by hand uses step 0.5 then 0.25, at most eight steps in a printed table | Long enough to see the error halve, short enough for a calculator and one lesson | frame.md unit 7 |

## For Cory

1. **Which route does Calculus serve?** (scope, audience) Either Precalculus first (the parked accelerated path L15, or
   both in one year) with the course as written, or Calculus straight after Algebra II, which needs about 20 days of
   bridge teaching and therefore a named cut (I would cut from units 9 to 11, keeping series to geometric and Taylor
   polynomials). The frame currently recommends the straight route as if it cost nothing.
2. **What "both semesters' content" means.** (scope) The outcome list matches the two-semester exam course, which
   leaves out trigonometric substitution, volumes by shells, work, surface area and centres of mass. A university's
   second-semester course usually includes them. The frame keeps them as extensions; that is a sound reading, but it is
   yours to confirm.

## What I could not judge

- Whether each base-text section holds what the map says (for example whether 2.3 treats ln x, or whether chapter 9
  has the limit comparison test): the copy is not loaded and I did not open the author's site. The scope writer's
  check against the loaded copy, which the frame already requires, covers it.
- The published exam course pacing and topic list are from memory, not opened; finding 1's day estimate rests on them
  and on the pc- row loads.

## Sources

- data/progressions/math.csv (calc-, pc- and the named alg2- and geo- rows): loads, limits, handoffs.
- data/standards/curio-math-electives.txt and data/standards/ccss-math-standards.txt (G-GMD.A.2): the standard text.
- docs/RUBRIC-MATH-HS.md: the bar and the L49 question.
- docs/courses/algebra-ii/frame.md, docs/courses/precalculus/frame.md, docs/courses/physics/frame.md,
  docs/courses/chemistry/frame.md, docs/courses/biology/frame.md: seams and cross-subject leans.
- Base-text scout notes, 2026-11-16, section 3: the Contemporary Calculus table of contents and licence.
- From memory: the published course description for the two-semester calculus exam course (pacing and topic list);
  standard first-year university calculus syllabi.

## For the source list

Nothing new read.
