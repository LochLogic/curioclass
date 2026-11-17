# Frame read: precalculus (Math, Precalculus), 2026-11-16

Expert cold read of docs/courses/precalculus/frame.md, by the brief docs/pipeline/briefs/frame-read.md, against
docs/RUBRIC-MATH-HS.md. I did not write the frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-HS.md, docs/pipeline/briefs/frame-write.md
  (rules and lessons 5 to 16), docs/pipeline/briefs/sequence-write.md rule 2, docs/PRODUCTION-PATH.md (After the core
  subjects), data/plans/later.csv L15 and L49.
- The frame in full; its row in data/plans/frames.csv (precalculus, grade 12, 10 units, 160 days, 50 minutes, 5 a
  week, 32 weeks).
- data/progressions/math.csv: all 25 pc- rows (standard, assumes, models, words, cross_subject, notes), the calc- rows
  that name a pc- row, the owners of A-REI.C.7, G-GPE.A.2, F-IF.C.7d, F-BF.B.4a, A-APR.B.2 and A-APR.B.3;
  data/progressions/math-excluded.csv (header only).
- data/standards/ccss-math-standards.txt: every (+) line (48) and the lettered parts of N-VM.B.4 and N-VM.B.5;
  data/standards/curio-math-electives.txt (CUR-PC.1 to 15, and the CUR-CA lines Calculus builds on).
- Neighbours: docs/courses/algebra-ii/frame.md (Seams, "Where each thread ends", For the lead), and the
  Algebra II treatment of the alg1- and geo- rows this frame calls "used in grade 11";
  docs/courses/calculus/frame.md (brief, Seams, units 1, 2, 4, 6, 7, 9, 10, For the lead, Source map);
  docs/courses/statistics/frame.md (brief, Seams, unit 4, For the lead).
- The base text scout's notes (side-session-notes, base-text-scout-2026-11-16.md): the OpenStax Precalculus 1st
  edition table of contents, licence evidence and the reference-only list.
- Earlier reviews: frame-algebra-ii, frame-algebra-i, frame-geometry and frame-physics (2026-11-14), to tag REPEAT.
- Gates: `scripts/plan.py check`: precalculus 0 failures (10 units, 160 days, 151 in units, 9 for checks and respond
  days); the run exits 1 on another course only (earth-and-space-science: frames.csv disagrees with its frame).
  `scripts/stale.py check`: 60 files, 0 failures. By hand: unit days equal the sums of the rows' loads (18, 16, 14,
  16, 14, 19, 13, 18, 9, 14 = 151); the day and week calendars match; every pc- row is placed once; every pc- assumes
  is in the Seams table; all 66 base sections are placed; every (+) code is owned exactly once across the
  progression (42 codes here: 37 (+) standards and 5 lettered parts), and each CUR-PC code by one row.

## Verdict

A strong frame: the order teaches well (inverses before logarithms and inverse trigonometry, vectors before matrices
and the complex plane, limits gathered last), every (+) code is placed with its lettered parts, the Source map places
all 66 sections with reasons, and the Calculus seam matches row for row from both sides. The most serious fault is
mathematical: CUR-PC.13, its row and unit 10 say every infinite series other than a geometric one with ratio between
-1 and 1 has no finite sum, which is false and which Calculus contradicts (finding 1). The one change that matters
most after that is days: conics (unit 9) has 7 teaching days for two derivations, three standard forms, the general
form and a construction, and should take 2 days from unit 1's review (finding 2). The L49 answer is right in
direction and should be confirmed with the review guard rewritten so the frame meets it (finding 3).

## Findings, most serious first

### 1. CUR-PC.13 states a falsehood about infinite series (serious; firm)

LAYER standard, progression, frame. REPEAT new.

- **What is wrong.** CUR-PC.13 reads "explain why other infinite series have no finite sum"; the pc-sequences-series-
  binomial notes and unit 10 say "why other series have no finite sum". Read plainly, "other" means every series that
  is not a geometric series with ratio between -1 and 1. Many such series converge: 1 + 1/4 + 1/9 + ... (sum pi squared
  over 6), the alternating harmonic series, any telescoping series. calc-series-convergence (Calculus unit 10) teaches
  exactly these with the p-series and comparison tests.
- **Why it matters.** It is the one outcome Calculus's series unit picks up from. A day writer would write an exit
  ticket whose key teaches a false rule, and a student who learns it must unlearn it a term later.
- **Fix.** CUR-PC.13 (data/standards/curio-math-electives.txt): "Write sums in sigma notation, find the sum of an
  infinite geometric series when the ratio lies between -1 and 1, and explain why an infinite geometric series with
  any other nonzero ratio has no finite sum." Same clause in the pc-sequences-series-binomial notes and in unit 10's
  What students learn ("and why a geometric series with any other nonzero ratio has no finite sum"). Optional, inside
  the row's days: one partial-sum table of 1 + 1/2 + 1/3 + ... set beside 1 + 1/4 + 1/9 + ..., stated as "some
  non-geometric series grow without bound and some do not; Calculus tells them apart".

### 2. Unit 9 (conics) is short for what it owns; unit 1 has room (moderate; likely)

LAYER progression, frame. REPEAT yes (days by load, as in the biology and psychology reads).

- **What is wrong.** Unit 9 has 9 days, which by the frame's own reading of load includes the end-of-unit assessment
  and its respond day: 7 teaching days. Inside them sit a retrieval day (circle and parabola), the ellipse derived
  from its foci, the hyperbola derived from its foci (G-GPE.A.3), standard forms of all three conics with their
  features and graphs (hyperbola asymptotes included), the general second-degree equation completed to standard form
  and named (CUR-PC.12), a reactivated construction followed by the tangent from an outside point with its proof and a
  coordinate check (G-C.A.4). That is about 9 teaching days of work. Common precalculus pacing gives conics 2 to 3
  weeks (from memory). Unit 1, by contrast, has 18 days with 3.5 planned days of pure review in pc-function-analysis
  ("about 7 days, half of them review"), whose only new tool is interval notation.
- **Why it matters.** A unit writer cannot fit two derivations and a proof-backed construction into 7 days without
  dropping the derivations to statements, which leaves G-GPE.A.3 ("derive") taught in part.
- **Fix.** Row loads (lead applies, no standard moves): pc-function-analysis "Load: about 5 days, 1.5 of them review
  of Algebra II unit 5 transformations and Algebra I domain and range"; pc-conics "Load: about 11 days; 1 reviews the
  circle and parabola equations of Geometry". Frame: unit 1 16 days, unit 9 11 days, total unchanged (151 in units).
  New calendar: unit 1 days 1 to 16, unit 2 17 to 32, unit 3 33 to 46, check 1 47 to 49, unit 4 50 to 65, unit 5 66 to
  79, unit 6 80 to 98, check 2 99 to 101, unit 7 102 to 114, unit 8 115 to 132, unit 9 133 to 143, unit 10 144 to 157,
  check 3 158 to 160. Readiness days become 49 (unit 4), 101 (unit 7) and 132 (unit 9). Weeks: unit 1 weeks 1 to 4,
  unit 2 4 to 7, unit 3 7 to 10, check 1 week 10, unit 4 10 to 13, unit 5 14 to 16, unit 6 16 to 20, check 2 20 to 21,
  unit 7 21 to 23, unit 8 23 to 27, unit 9 27 to 29, unit 10 29 to 32 (update the Cross-subject weeks to match). The
  Days bullet's sentence on unit 9 changes to "unit 9 (11 days, conics) carries one row with two derivations and a
  construction". Watch, no change: unit 7 (13 days, 9 codes and a modeling task) is tight but its codes are quick;
  the unit plan keeps its modeling task to 2 days.

### 3. The L49 answer: confirm it, but its review guard is contradicted by the rows (moderate; likely)

LAYER process, frame. REPEAT new.

- **Judgment on the proposal.** The direction is right. Focus 1a to 1c score the share of time on the non-(+)
  prerequisite clusters; a course that owns only (+) codes and its own outcomes has nothing for them to measure, and
  an owned-outcome account (every owned code taught in full, assessed on a named check after its unit) is the honest
  replacement. Keeping coherence, assessment, rigor with direct fluency, the practices, supports and the multilingual
  criteria in full is right, and it is the same answer the Statistics and Calculus frames give.
- **What is wrong.** (a) The account says "no day only reteaches an earlier course's row", but the rows' own loads
  plan whole review days: 3.5 in pc-function-analysis, 2 each in pc-polynomial-complex-zeros, pc-rational-functions-
  inequalities and pc-trig-graphs, 1 each in eight more rows, 16.5 days in all (about 1 unit day in 9). A writer told
  both cannot follow both. (b) Rubric gap 1 says "plus standards are marked optional and never count toward focus";
  in these courses they are required, and the answer does not say so. (c) Gap 2 (the modeling record) is not
  addressed; see finding 6. (d) The three grade 12 frames each propose a different replacement for the same rubric
  sentence; the lead needs one.
- **Fix.** Frame, Focus bullet: replace "the rows' load notes cap review (each says how many of its days review
  Algebra II, Geometry or Algebra I), and no day only reteaches an earlier course's row (the rubric's gap 7, read for
  this course)" with "review is capped at the days the rows' load notes name (16.5 of 151, about one day in nine), and
  each review day reviews only what that row's new work uses that week (the rubric's gap 7, read for this course)".
  One text for docs/RUBRIC-MATH-HS.md, for all three frames: "Precalculus, Statistics and Calculus own (+) codes and
  Curio Class's own outcomes (data/standards/curio-math-electives.txt), so focus criteria 1a to 1c do not apply and no
  focus percentage line is set. Each of their frames states an owned-outcome account instead: every owned code taught
  in full in a named unit and assessed on a named check after it, and review capped at the days the rows' load notes
  name. In these courses (+) codes are required, not optional. Everything else in this file applies in full, gaps 2 to
  9 included." Optional, a judgment call: one information line (not a gate) giving the share of unit days on the
  function and trigonometry work Calculus builds on (units 1 to 5 and 10: 92 of 151 days, 61 percent; 90 of 151 after
  finding 2).

### 4. The own-outcome list leaves taught work without a code (moderate; likely)

LAYER standard, progression. REPEAT new.

- **What is wrong.** CUR-PC.1 to 15 are in our own words, each owned by one row, and cover the course well, with
  three gaps. (a) Finding every zero of a degree 3 or 4 polynomial (the factor theorem, rational candidates, conjugate
  pairs) takes about 4 of unit 2's days, but no code holds it: N-CN.C.9 asks only to know the fundamental theorem and
  show it for quadratics. (b) The values of secant, cosecant and cotangent on the unit circle: CUR-PC.5 names only
  their graphs, and Calculus's derivative rules lean on them. (c) The power-reducing formulas (base 7.3), from which
  the half-angle formulas of CUR-PC.6 come.
- **Why it matters.** The owned-outcome account assesses codes; work without a code has no guaranteed assessment item,
  and the zero-finding is the most-used algebra of the year.
- **Fix.** New outcome owned by pc-polynomial-complex-zeros, numbered in teaching order as CUR-PC.2, with CUR-PC.2 to
  15 renumbered to 3 to 16 (the list, the pc- rows and this frame; nothing else cites them yet): "Find every zero of a
  polynomial of degree 3 or 4 with integer coefficients, real and complex, using the factor theorem, rational
  candidates and conjugate pairs, and write the polynomial as a product of linear factors." CUR-PC.5 (new 6): begin
  "Find the values of all six trigonometric functions from the unit circle, and graph them, ...". CUR-PC.6 (new 7):
  "... and use the double-angle, power-reducing and half-angle formulas to find exact values and to simplify." Unit 2
  and unit 5 cells name the codes accordingly.

### 5. The paper path has no way to fit a logistic model (moderate; firm)

LAYER frame. REPEAT yes (paper path, as in the ELA 9 to 12 reads).

- **What is wrong.** Unit 3's modeling task fits a logistic model to wildlife counts. The paper path names semi-log
  paper, which straightens exponential data but not logistic data, and "curve fitting uses technology". A student on
  the paper path cannot do the unit's modeling task.
- **Why it matters.** The paper path is a promise that every task can be done without a device (frame-write lesson
  14).
- **Fix.** Technology and the paper path bullet, add: "A logistic fit on paper: estimate the carrying capacity L from
  where the counts level off, plot ln(y / (L - y)) against time on grid paper, fit a line by eye, and read the growth
  rate from its slope and the midpoint year from where it crosses zero; residuals are checked in a printed table."
  (This follows from y = L / (1 + A e^(-kt)), which gives ln(y / (L - y)) = kt - ln A.)

### 6. The one modeling standard has no modeling task, and MP4 is under-placed (minor; firm)

LAYER frame. REPEAT new.

- **What is wrong.** F-TF.B.7 is the only owned code with the modeling star; unit 4 teaches it (the tide task) but has
  no modeling task and no MP4. Units 7 and 8 each take a modeling task through the full cycle but do not list MP4;
  MP4 sits only in units 3 and 6.
- **Why it matters.** Rubric 1a and gap 2 ask that modeling standards meet the full cycle and be recorded.
- **Fix.** Modeling bullet: "F-TF.B.7, the course's one starred code, is met in unit 4 through the tide task taken
  through a compact cycle (assumptions, model, solve with an inverse function, interpret, check against the tide
  table) inside pc-inverse-trig's days." Practices: MP4 added to units 4, 7 and 8 (C3 cells and the Practices
  bullet: MP4 units 3, 4, 6, 7, 8).

### 7. The identity-proof rule is stricter than mathematics (minor; likely)

LAYER progression, frame. REPEAT new.

- **What is wrong.** Unit 5 and the pc-trig-identities notes say identities are proved "never by working on both sides
  at once". Rewriting each side separately into the same expression is a valid proof. What is invalid is treating the
  identity as an equation and doing the same operation to both sides (squaring, cross-multiplying) as if it were
  already true.
- **Why it matters.** The answer-key agent and teachers will mark sound proofs wrong, and students learn the rule
  without the reason.
- **Fix.** Unit 5 and the row note: "proved by a chain of equal expressions: usually one side rewritten into the
  other, or each side rewritten separately into the same expression; never by doing the same operation to both sides
  of the identity as if it were already known to be true."

### 8. N-VM.B.4a is named in part (minor; firm)

LAYER frame. REPEAT yes (standard named in part, as in the Algebra I, Algebra II and Geometry reads).

- **What is wrong.** Unit 6 names adding vectors three ways but not the part's second sentence: the magnitude of a
  sum is typically not the sum of the magnitudes.
- **Fix.** Unit 6: "vectors added end to end, componentwise and by the parallelogram rule, and why the magnitude of a
  sum is usually less than the sum of the magnitudes (N-VM.B.4a)".

### 9. Source map: four notes to correct (minor; firm)

LAYER base text. REPEAT yes (Source map wording).

- 7.3: "Reduction formulas as an extension only" conflicts with CUR-PC.6, since the half-angle formulas are derived
  from the power-reducing (reduction) formulas. Note: "Double-angle, power-reducing and half-angle formulas
  (CUR-PC.6); the power-reducing formulas taught as the step to the half-angle formulas."
- 7.4: decision "cut" with unit 5 placed. Write unit "none", decision "cut", note "Not owned by any row; the product-
  to-sum derivation stays as unit 5's extension." 
- 9.3: "Algebra I owns A-REI.C.7" is wrong; geo-slope-criteria-lines (Geometry) owns it. Note: "Geometry owns
  A-REI.C.7 (geo-slope-criteria-lines) and Algebra I the graphing of inequalities (A-REI.D.12); no pc- row owns it."
- The reason for the order change ("matrices (chapter 9) come before polar coordinates (8.3 to 8.7), because the
  vector-arrow model is needed first") fits the move of 8.8, not of chapter 9. Lead paragraph and 8.3 note: "vectors
  (8.8) move up beside the laws of sines and cosines, because the vector-arrow model is needed before the complex
  plane; matrices (chapter 9) come before polar coordinates so that rotation by a matrix and rotation by multiplying
  complex numbers can be compared in unit 8."
- 11.5 and 12.4 use "split" for a section partly kept and partly left out, where split means across two units. Write
  "keep" with the note "in part: ..." as now.

### 10. Small consistency points (minor; firm)

LAYER frame, progression. REPEAT yes (models table and seam wording, as in the biology and chemistry reads).

- Models carried, unit-circle: "Units that use it again" omits unit 8 (pc-polar-graphs takes unit-circle in). Write
  "5, 8".
- Course-level checks, Check 2: "new sampling on units 1 to 5" but its list ends with "oblique triangles and vectors"
  (unit 6). Write "new sampling on units 1 to 5, and unit 6's record reused".
- Standard bullet: "the 42 (+) codes" are 37 (+) standards and 5 lettered parts (N-VM.B.4a to c, N-VM.B.5a and b).
  Write "42 codes: the 37 (+) standards the core courses deferred and 5 lettered parts".
- Handed on to Calculus, calc-implicit-differentiation: the calc- row says circles and ellipses. Write "Tangent lines
  to circles and ellipses; the circle's tangent matches the radius-tangent right angle of unit 9's construction".
- calc-continuity names only pc-function-analysis, but informal continuity is CUR-PC.15 (pc-informal-limits). Row
  note (lead applies): "assumes pc-function-analysis and pc-informal-limits"; this frame's table row adds
  "pc-informal-limits (unit 10)".

### 11. Stale notes: one missed, and three frames propose three texts (minor; firm)

LAYER process. REPEAT yes (stale notes in shared docs).

- docs/courses/algebra-ii/frame.md For the lead 4 ("The electives have no rows ... use that table ... when the
  Precalculus, Statistics and Calculus progressions are written") is stale; the rows exist. Replacement: "4. **The
  electives' rows.** Done 2026-11-16: the pc-, stat- and calc- rows exist and the electives' frames' Seams pick up each
  thread in the table above."
- The Precalculus, Statistics and Calculus frames each give a different replacement for the same lines in
  docs/sources/BASE-TEXTS.md ("Math past Algebra 2 ..."), docs/agents/lenses/math.md ("Past Algebra 2 has no base
  text and no progression"), docs/courses/algebra-ii/frame.md ("No row of the progression is handed on") and
  docs/RUBRIC-MATH-HS.md (finding 3). The lead applies one text each once all three frames are settled. Lens line:
  "Past Algebra 2: Precalculus, Statistics and Calculus have progression rows (pc-, stat-, calc-, grade 12) and Curio
  Class's own outcome list; each frame names its base text." BASE-TEXTS: drop the line from "Our own" once the three
  base-text rows are added (Precalculus 1st edition, OpenStax Statistics with Lane, Hoffman's Contemporary Calculus).

## Checked and found right (do not undo)

- The order: unit 1's inverses feed logarithms (unit 3) and inverse trigonometry (unit 4); exact values (unit 4)
  before identities (unit 5); oblique triangles with vectors (unit 6), the law of cosines giving resultants
  (G-SRT.D.11's "resultant forces"); vectors before matrices before the complex plane; limits last. No skill or model
  is used before it is taught.
- Every (+) code and every lettered part is placed, and each is taught in full apart from finding 8. Mathematical
  statements checked and right: the special-angle and pi plus or minus x work, restriction for inverse trigonometric
  functions, the addition-formula proof by unit-circle distance, (-1 + root 3 i) cubed = 8, the determinant as an area
  factor and as the test for an inverse, two-step connections as a matrix square, the ellipse (a cos t, b sin t).
- The Source map's cuts: 9.6 Gaussian elimination and 9.8 Cramer's rule (A-REI.C.9 sends 3 by 3 inverses to
  technology, and the paper path's given-then-checked inverse still lets the student solve), 10.4 and 10.5, 9.4 left
  to Calculus, 11.7 and the arithmetic-sequence and linear-function cuts. Complex roots as an extension only.
- The base text: 1st edition only, CC BY 4.0, archive version named, 2nd edition excluded even as reference; figures
  carried only on their own CC BY or public-domain credit.
- The readiness and retrieval count (rule 2): the Algebra II frame does treat each alg1- and geo- row this frame calls
  used in grade 11; readiness only for geo-solving-right-triangles, geo-rigid-motion-definitions, geo-dilations,
  alg1-linear-systems and geo-circle-angle-relationships, each on the respond day before its unit.
- The Calculus seam: 13 rows, the same on both sides, each with a just-in-time teach in Calculus. Statistics owns
  S-CP.B.9; combinations shown here without ownership.
- Fluency without a timer, the untimed year-end station, and the sensitivity picks.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Not applicable (focus 1a to 1c replaced, finding 3) |
| A supporting cluster that does not practise major work | Not applicable for the same reason |
| A source map row with no keep, split, merge, cut or ours decision | Met; four notes to correct (finding 9) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| CUR-PC.13 and its row and unit text say "a geometric series with any other nonzero ratio" | The current wording is false; a wording fix inside the outcome's intent | data/standards/curio-math-electives.txt; data/progressions/math.csv (pc-sequences-series-binomial); docs/courses/precalculus/frame.md (unit 10) |
| The logistic paper method: ln(y / (L - y)) against time on grid paper | The one paper method that straightens logistic data | docs/courses/precalculus/frame.md (Technology and the paper path) |
| The tide task in unit 4 is F-TF.B.7's compact modeling cycle | Already in the unit; no day change | docs/courses/precalculus/frame.md (Modeling, unit 4) |
| Identity proofs: either side, or both sides separately, by a chain of equal expressions | Mathematically valid; keeps keys sound | data/progressions/math.csv (pc-trig-identities); docs/courses/precalculus/frame.md (unit 5) |
| N-VM.B.4a's magnitude clause named in unit 6 | Completes the part's wording | docs/courses/precalculus/frame.md (unit 6) |
| Gaussian elimination and Cramer's rule stay cut; complex roots stay an extension | Not owned; the standard sends 3 by 3 to technology | docs/courses/precalculus/frame.md (Source map) |
| Source map notes for 7.3, 7.4, 9.3, the chapter 9 reason, 11.5 and 12.4 | Facts and decision words | docs/courses/precalculus/frame.md (Source map) |

## For Cory

- **One grade 12 slot.** On the core route a student has one grade 12 math year, so Precalculus then Calculus needs
  the parked accelerated path (L15) or two math periods in one year. This frame and the Calculus frame make
  compatible but different picks (this one: record L15 as the route to Precalculus then Calculus, plan no both-in-one-
  year path; Calculus: Calculus straight after Algebra II with just-in-time teaches, L15 parked). One Desk card for
  both. Recommendation: Calculus's pick for now (both already work under it), with this frame's line added to L15's
  note.

## What I could not judge

- The base text's section contents: the copy is not loaded, so the map was checked against the table of contents only.
  That 8.8 has the dot product but no projection, and 3.6 the rational zero theorem, rests on memory.
- Published pacing for conics and matrices: from memory, not checked against a source this run.
- Whether the Physics frame's weeks for orbits and net force still precede these units after finding 2's calendar
  shift (both are grade 11, an earlier year, so the order holds whatever the weeks).

## Sources

- CCSS Mathematics, data/standards/ccss-math-standards.txt: the text of every (+) code and lettered part.
- data/standards/curio-math-electives.txt: CUR-PC and the CUR-CA outcomes on the seam.
- The base text scout's notes, 2026-11-16: OpenStax Precalculus 1st edition table of contents and licence evidence
  (https://openstax.org/books/precalculus/pages/preface; archive JSON as cited there).
- Convergence of the p-series and the alternating harmonic series, the logistic linearisation, the validity of
  two-sided identity proofs: standard mathematics, firm.

## For the source list

- Nothing new read this run.
