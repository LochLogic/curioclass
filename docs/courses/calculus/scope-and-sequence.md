# Scope and sequence: Calculus

Course `calculus`, grade 12, draft, 2026-11-24 (fix pass applied 2026-11-24, docs/reviews/sequence-calculus-fixes-2026-11-24.md).

Eleven units keep the frame's order, owned rows and lengths: 14, 22, 14, 15, 16, 9, 9, 17, 10, 12 and 13 days, 151 in all, plus 9 course-level check and respond days, 160 course days. The course meets every school day for 32 weeks, so course day n is school day n and `school_day` is blank. The days live in data/plans/calculus/days.csv and the base-text placements in data/plans/calculus/source-map.csv; this page gives the judgment behind them. Every unit ends with its end-of-unit assessment on its second-last day and a respond day on its last; no unit is over 25 days, so no unit holds a mid-unit assessment. Every day opens with five minutes of spaced, mixed practice; the differentiation rules (from day 24), antiderivatives and substitution (from day 79) and choosing an integration method (from day 90, after day 89 teaches the choice) stay in that opening for the rest of the year, untimed.

## Earlier rows: last use and treatment

Counted by grade number on the accelerated path, the route Cory set (frame, route bullet): Algebra I in grade 8, Geometry 9, Algebra II 10, Precalculus 11, Calculus 12. A row a Precalculus row builds on was used in grade 11 (one hop) and is retrieval; a row no pc- row builds on was last used in grade 10 or earlier and gets a readiness check. The scope gate counts the core grade numbers (Algebra II in grade 11), a floor, so it prints a rule 2 note on the seven rows whose treatment the route changes (marked *); the notes are expected.

| Earlier row | Last use, accelerated path | Treatment here |
|---|---|---|
| alg2-rational-functions | Grade 11 through pc-rational-functions-inequalities and pc-informal-limits | Retrieval day 5 (holes and asymptotes); again day 59 (the box of fixed volume) |
| alg2-polynomial-identities * | Grade 10, Algebra II unit 2 | Readiness check, last ten minutes of day 1; used day 5 |
| geo-arcs-sectors-radians * | Grade 10, through alg2-unit-circle-radians | Readiness check day 1; used day 8, so retrieval days 116 and 129 |
| alg1-piecewise-absolute-value * | Grade 10, through alg2-transformations-functions | Readiness check day 1; used day 10 |
| alg1-graph-features-rates | Grade 11 through pc-rates-of-change | Retrieval day 15 |
| alg2-trig-functions-graphs | Grade 11 through pc-trig-graphs | Retrieval day 22 |
| alg2-number-e-continuous | Grade 11 through pc-exp-log-models | Retrieval days 23 and 97 |
| alg2-exp-log-graphs | Grade 11 through pc-logarithmic-functions | Retrieval days 28 and 108 |
| geo-circle-parabola-equations | Grade 11 through pc-conics | Retrieval day 31 |
| alg1-quadratic-forms-graphs * | Grade 10, through Algebra II unit 6 | Readiness check, last ten minutes of day 36; used day 37 |
| geo-volume-formulas | Grade 9, Geometry unit 5 | Readiness check day 36; used in unit 3, so retrieval day 111 |
| geo-solving-right-triangles * | Grade 11 through pc-inverse-trig and pc-oblique-triangles | Retrieval day 41 (the right-triangle related rates day) |
| alg1-vertex-form-max-min | Grade 9, through Geometry unit 6 | Readiness check, last ten minutes of day 50 |
| geo-modeling-objects-density | Grade 9, Geometry unit 5 | Readiness check day 50 |
| alg2-factors-zeros-graphs * | Grade 10, Algebra II unit 2 | Readiness check day 50; used day 55 |
| alg2-normal-distributions * | Grade 10, Algebra II unit 7 | Readiness check, last ten minutes of day 65; used day 66 |
| alg2-polynomial-division-remainder | Grade 11 through pc-polynomial-complex-zeros | Retrieval day 86 |
| alg2-sequences | Grade 11 through pc-sequences-series-binomial | Retrieval day 96 |
| alg2-logarithms | Grade 11 through pc-logarithmic-functions | Retrieval day 97 |
| geo-cross-sections-solids | Grade 9, Geometry unit 5 | Readiness check, last ten minutes of day 102 |
| alg2-geometric-series | Grade 11 through pc-sequences-series-binomial | Retrieval day 134 |
| alg2-polynomial-arithmetic | Grade 11 through pc-sequences-series-binomial | Retrieval day 145 |

The eighteen Precalculus seams (frame, second Seams table) open as retrieval on the first day that uses each: day 2 (pc-informal-limits, carried by the review day itself), days 5 and 6, 10, 15, 22, 26, 28, 29, 31, 51, 67 (sigma notation), 86, 97, 123, 125, 128, 130 and 134; each note names its pc- row. A retrieval task is ten minutes, practice and never check evidence; a student who misses it gets a brief reminder with the earlier model, and a student without Precalculus gets the row's bridge as a printed catch-up pack (frame, route bullet). Unit 1's readiness check takes the last ten minutes of day 1, after the hook and the lesson; every later check sits on the respond day just before its unit (days 36, 50, 65 and 102), so day 1 of every later unit stays clean for the hook; misses get a reminder with the earlier model in the next unit's first openings (unit 1: days 2 to 4).

**Minutes on earlier courses' rows** (RUBRIC-MATH-HS, the grade 12 courses): the review day on day 2 (50 minutes, which also carries the pc-informal-limits seam), five readiness checks (50), 27 retrieval tasks at ten minutes (270: 17 on the Algebra II, Algebra I and Geometry rows above, most with their Precalculus seam, and 10 on Precalculus rows alone, days 6, 10, 26, 29, 51, 67, 123, 125, 128 and 130) and at most 75 openings on earlier courses' rows (375): at most 745 minutes of 7,550 unit minutes, 9.9 percent, under the 15 percent cap (about 1,130). The frame now carries the same count. Unit plans list their own counts.

## Unit 1. Approaching a value

Course days 1 to 14, weeks 1 to 3. Day 1 hooks with the tangent and area questions, estimates a limit from a table and closes with unit 1's readiness check; day 2 is the frame's one review day on the informal picture; days 3 and 4 add one-sided limits and the three ways a limit fails. Exact limits follow (days 5 to 9: laws and factoring, rationalizing and common denominators, practice choosing a rewrite, the squeeze argument for sin x over x, limits at infinity and asymptotes), then continuity (days 10 to 12), with the intermediate value theorem last because it needs continuity and the if-then language of base 0.5.

Assessment: day 13 samples every clause of CUR-CA.1 to CUR-CA.3; response on day 14. Readiness (day 1): alg2-polynomial-identities, alg1-piecewise-absolute-value and geo-arcs-sectors-radians. Candidate kept: the exit-ticket set on one- and two-sided limits sits in the exit tickets of days 3 and 4, no day added. The formal definition stays an extension (day 7).

## Unit 2. The derivative and how to compute it

Course days 15 to 36, weeks 3 to 8. Secant slopes close in on a tangent before any rule (day 15); the definition, tables and derivative graphs, and differentiability follow (days 16 to 19). The rules come in order of what each needs: power, sum and constant multiple, then product and quotient, then sine and cosine from the addition formula (day 22, which derives the limit of (cos h - 1)/h from day 8's sin h over h and needs the quotient rule for the other trigonometric functions), then e to the x and ln x read from slopes (day 23), with practice on day 24 and an application on day 25. The chain rule (days 26 and 27) comes before inverses because the inverse derivative is the chain rule on f(g(x)) = x; ln x is proved on day 28, the inverse trigonometric derivatives on day 29, and b to the x on day 30 finishes CUR-CA.5. Implicit differentiation and higher derivatives close the teaching (days 31 to 33), and day 34 practices every rule.

Assessment: day 35, one sitting with its untimed, independent rules section, covering CUR-CA.4 to CUR-CA.7; response on day 36, whose last ten minutes hold unit 3's readiness check. Candidate kept: the rules station inside day 35's sitting, no day added. Logarithmic differentiation stays an extension (day 33).

## Unit 3. Rates in context and local approximation

Course days 37 to 50, weeks 8 to 10. Rates with units and straight-line motion first (days 37 to 40), then related rates (days 41 and 42: triangles, containers), the modeling task drafted on day 43, practice of the related rates steps on day 44 and the model validated and revised on day 45, two nights after the draft so the written feedback can be done well; last the tangent line approximation and the rule of L'Hospital (days 46 to 48), which leans on day 33's second derivative and leads to unit 11's Taylor polynomials.

Assessment: day 49 on CUR-CA.8 to CUR-CA.10; response on day 50, whose last ten minutes hold unit 4's readiness check. The related rates report is scored on the rubric only after its day 45 revision. Readiness (day 36): alg1-quadratic-forms-graphs and geo-volume-formulas. Candidate kept: one related rates task scored on a written explanation of each step, practiced on day 44 and placed on day 49, no day added. Newton's method stays an extension. Sensitivity: ladder and container contexts only, no falls (days 41 and 43).

## Unit 4. What derivatives say about a graph, and best choices

Course days 51 to 65, weeks 11 to 13. Critical points and the extreme value theorem (days 51 and 52) come before the mean value theorem (day 53) and the first derivative test (day 54); concavity, the second derivative test and the linked graphs of f, f' and f'' follow (days 55 to 58). Optimization (day 59) then works in new design settings (day 60), the design modeling task is drafted on day 61, day 62 practices the whole unit, and day 63 validates and revises the design, two nights after the draft.

Assessment: day 64 on CUR-CA.11 to CUR-CA.13; response on day 65, whose last ten minutes hold unit 5's readiness check. Readiness (day 50): alg1-vertex-form-max-min, geo-modeling-objects-density and alg2-factors-zeros-graphs. Candidate kept: the justification item (a claim about f from a graph of f' only), practiced on day 58 and placed on day 64, no day added. Curve-sketching asymptotes stay an extension.

## Unit 5. Accumulation and the fundamental theorem

Course days 66 to 81, weeks 14 to 17. Sums of rate times width build the riemann-rectangles model before any antiderivative: left, right and midpoint sums, with sigma notation retrieved from Precalculus on day 67 where it is first used, then trapezoidal and unequal-step table sums, then the definite integral as their limit (days 66 to 69). Accumulation functions read from a rate graph (day 70) lead to the fundamental theorem, part one with practice (days 71 and 72), part two (day 73) and net change in context from a rate rule and a rate graph (day 74). Indefinite integrals, the inverse trigonometric forms and substitution close the unit (days 75 to 79).

Assessment: day 80 on CUR-CA.14 to CUR-CA.16; response on day 81. Readiness (day 65): alg2-normal-distributions. Candidate kept: the table-based accumulation item (unequal steps), taught on day 68 and placed on day 80, no day added. Simpson's rule stays an extension.

## Unit 6. More ways to integrate

Course days 85 to 93, weeks 17 to 19. Parts, partial fractions with division first, completing the square and the squares of sine and cosine (days 85 to 88), then day 89, an Application day that first teaches choosing a method from the form of the integrand (a CUR-CA.17 clause), so it is not typed Fluency; the choice stays in the openings from day 90. Improper integrals follow the methods that evaluate them (days 90 and 91) and come before unit 10's integral test.

Assessment: day 92 on CUR-CA.17 and CUR-CA.18; response on day 93. Candidate kept: the choose-the-method sort inside day 89, no day added. Trigonometric substitution stays an extension.

## Unit 7. Equations about rates

Course days 94 to 102, weeks 19 to 21. Writing and checking a differential equation (day 94), slope fields on printed grids (day 95), then Euler's method by hand with slope-field matching beside it (day 96): slope fields take two teaching days and separable models four, as the rows' loads (4 and 5 of the unit's 9) ask. Separable equations with exponential growth and decay (day 97) are all the cooling model needs, so the modeling task is drafted on day 98; logistic growth follows (day 99), and day 100 validates the cooling model against a new reading and revises the report (25 minutes), two nights after the draft, with mixed practice in the rest of the period.

Assessment: day 101 on CUR-CA.19 and CUR-CA.20; response on day 102, whose last ten minutes hold unit 8's readiness check; the respond day carries no revision. Candidate kept: the slope field matching item and one Euler table by hand, practiced on day 96 and placed on day 101, no day added. Mixing problems stay an extension. Sensitivity: decay uses a tracer or dating context with given data, populations are fish or bacteria, no disaster or illness (days 97 to 100).

## Unit 8. Measuring with integrals

Course days 103 to 119, weeks 21 to 24. Net change, average value and motion (days 103 to 105), the collision-test accumulation (day 106) and the tank modeling task drafted (day 107); area between curves (days 108 to 110), with the tank report revised on day 110; the Cavalieri day before any volume integral (day 111), then cross sections, discs and washers with the sphere and spherical ring checked by integration (days 112 to 115); arc length last, checked on the circle (days 116 and 117).

Assessment: day 118 on CUR-CA.21 to CUR-CA.24 and G-GMD.A.2; response on day 119. Candidate kept: the volume item with a sketched slice and its expression explained, practiced on day 115 and placed on day 118, no day added. Shells and work stay extensions. Sensitivity: the collision context is a test cart or helmet liner with no injury figures (day 106).

## Unit 9. Motion in the plane and polar regions

Course days 123 to 132, weeks 25 to 27. Parametric slope and concavity (days 123 and 124), vector-valued motion (days 125 and 126) and an application from a table of positions (day 127), then polar slope as a parametric curve in theta, polar area from thin sectors and the area between two polar curves (days 128 to 130).

Assessment: day 131 on CUR-CA.25 and CUR-CA.26; response on day 132. Candidate kept: the motion-in-the-plane item from a table of positions, inside day 127, no day added. The rose-petal area found two ways stays an extension (day 130).

## Unit 10. Infinite series

Course days 133 to 144, weeks 27 to 29. Sequences and partial sums first (days 133 and 134), then the integral, comparison and limit comparison tests (days 135 and 136) and practice choosing among them (day 137); then the alternating series test with its error bound, absolute and conditional convergence and the ratio test (days 138 to 140), an application writing which test and why (day 141) and mixed practice (day 142).

Assessment: day 143 on CUR-CA.27 and CUR-CA.28; response on day 144. Candidate kept: the which-test-and-why item, inside day 141 and on day 143, no day added. The harmonic series' slow growth is shown on day 134.

## Unit 11. Taylor polynomials and power series

Course days 145 to 157, weeks 29 to 32. Taylor polynomials grow from unit 3's tangent line (days 145 to 147), then the Lagrange error bound and an approximation to a stated accuracy (days 148 and 149); power series follow, with intervals of convergence from the ratio test (days 150 and 151), the common series (day 152), new series by substitution, powers, differentiation and integration (days 153 and 154), and an integral approximated from a series with its error bounded (day 155, joining units 5, 10 and 11).

Assessment: day 156 on CUR-CA.29 and CUR-CA.30; response on day 157. Candidate kept: one approximation with its error bound worked by hand, inside day 149 and on day 156, no day added. e to the i theta stays a look-ahead extension (day 155).

## Course-level checks

| Check | Days | Weeks | Short items (first day) | Extended task (second day) |
|---|---|---|---|---|
| Check 1, mid-year | 82 and 83, respond 84 | 17 | Fresh items from units 1 to 4: CUR-CA.2 to CUR-CA.7, CUR-CA.10 to CUR-CA.12 | Units 3 and 4: a motion or rate situation ending in an optimization (CUR-CA.8, CUR-CA.13) |
| Check 2 | 120 and 121, respond 122 | 24 to 25 | Fresh items from units 5 to 7 (CUR-CA.14 to CUR-CA.20) and a few from units 1 to 4 (CUR-CA.5, CUR-CA.11) | An accumulation function with a differential equation and its slope field (CUR-CA.15, CUR-CA.19, CUR-CA.20) |
| Check 3, year-end | 158 and 159, respond 160 | 32 | Fresh items from units 1 to 10 weighted to 9 and 10, and the untimed fluency station sampling CUR-CA.5, CUR-CA.6, CUR-CA.7, CUR-CA.16 and CUR-CA.17 directly | A derivative, an integral and a series in one situation (CUR-CA.4, CUR-CA.15, CUR-CA.28) |

Each check comes right after a unit's end-of-unit assessment (units 5, 8 and 11), so it draws no items on that unit: its items come from earlier units, and that unit's record from its end day is reused unscored with its date. Each check day lists only the codes it samples. The first day's short items never repeat the form of the unit sitting two days before (rule 2): each gives a worked solution to critique and correct, two claims to choose between with a reason, or cases to sort and justify; the day 158 fluency station stays direct, with no supplied work and never inside a critique. Grade 12 has no stagger rule beyond the week 32 finals week, and every check sits on the frame's target weeks.

## Shorter path

**A shorter period (45 minutes).** The opening drops from five minutes to three on teaching days, and each teaching day's practice set is cut by its last few items (the exit ticket stays); check and assessment sittings keep their items and run the extended task in the full period. Below 45 minutes, a school runs the check 1 to 3 extended tasks over two periods and folds the days below.

**A year about 10 days short.** Ten fold-in days, each a practice or review day whose work goes into a neighbor's day and the openings, nothing assessed and no owned part cut, and never a feedback, revision, check or respond day, nor a day between a modeling draft and its revision. The first four follow the frame's trim order (A tight course: improper integrals and arc length each lose one of their two days, then days 142 and 2), and the fifth, day 7, is the next fold the frame's Grade 12 calendar names, so the first five serve seniors who leave early.

| Fold-in day | Folds into | Minutes saved |
|---|---|---|
| 91 (improper integrals, unbounded integrand) | Day 90, both kinds on one day; the 1/x and 1/x squared swap kept | 50 |
| 117 (arc length practice) | Day 116 and the openings of days 118 to 119 | 50 |
| 142 (mixed series practice) | The openings of days 143 to 147 | 50 |
| 2 (review of the informal picture) | Days 1 and 3 and the openings of days 3 to 5 | 50 |
| 7 (choosing a rewrite for 0/0 limits) | Day 6 and the openings of days 8 to 10 | 50 |
| 19 (derivative practice by definition) | Day 18 and the openings of days 20 to 22 | 50 |
| 72 (practice with accumulation derivatives) | Day 71 and the openings of days 73 to 75 | 50 |
| 137 (choosing a series test) | Day 141, which already asks which test and why | 50 |
| 151 (interval of convergence practice) | Day 150 and the openings of days 152 to 154 | 50 |
| 40 (a whole motion in a new case) | Day 39 and the openings of days 41 to 43 | 50 |

Total: 10 days, 500 minutes, leaving 150 of the frame's 160 course days; up to 5 days (the first five rows) for early-leaving seniors, more than 5 is the frame's For the lead 6. Day 96 left the list (its slope-field matching now sits beside the Euler table), and day 62 (unit 4's practice) stays off it because it sits between the design draft and its revision.

## For the lead

1. **Base CC 2.3 is missing from the CC BY store.** Closed (expert agreed): the archive listing has no 2.3 file; days 22 and 23 stay ours, and the source map marks 2.3 cut with that reason.
2. **Archive numbering differs from the frame's Source map.** Closed: the frame's Source map now follows the archive numbering (fix pass, 2026-11-24). Site sections 8.6 Integration Tactics, 8.7 Approximating Antiderivatives and 5.5 Tubes have no archive copy (day 89 adapts 4.8 for choosing a method; day 74 is ours).
3. **The route.** Closed (expert finding 2): the readiness count follows the accelerated path, the route Cory set; the frame's route and readiness bullets now say one thing, and the gate's core count is a floor whose seven rule 2 notes are expected.
4. **Same task form within two weeks.** Closed (expert finding 3): each check's first day keeps its codes and takes a new form (critique and correct, choose between claims, sort and justify).
5. **Unit 7's report revision on the respond day.** Closed (expert finding 4): unit 7 is reordered so the cooling model is drafted on day 98 and revised on day 100; day 102 is a respond day only.

Read first: unit 2's rule order (days 20 to 30) and unit 7's new order (days 94 to 102).
