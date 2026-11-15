# Sequence read: Algebra II, 2026-11-15

Expert cold read of the Curio Class Algebra II scope and sequence (grade 11), done under docs/pipeline/briefs/sequence-read.md with the math lens. The named bar, docs/RUBRIC-MATH-K8.md, has no high school notes, so the read applies the lens, the band rules and the earlier reads' settled choices. Third of three high school math reads; this report carries "Across the band" for Algebra I, Geometry and Algebra II.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/algebra-ii/scope-and-sequence.md in full; docs/courses/algebra-ii/frame.md (brief, readiness, fluency, seams, checks).
- data/plans/algebra-ii/days.csv (160 rows) and source-map.csv (161 rows).
- data/progressions/math.csv, grade 9 to 11 rows; data/plans/algebra-i/days.csv and data/plans/geometry/days.csv for the last use of every assumed row.
- The base: Illustrative Mathematics Algebra 2, 1st edition (S:\CurioClass-sources\illustrative-math\hs-algebra-2), every lesson's title, goals and targets, the course standards page and the modeling prompts.
- data/plans/calendar.csv; the physics, chemistry and biology sequence reads (2026-11-14) and the physics and chemistry days for math leans; the math grade 8 sequence read and its "Across the band"; my Algebra I and Geometry reads of today.
- Gate output: plan.py check, sequence.py check, frame.py calendar, stale.py check.

## Verdict

A careful sequence that ends every core math thread: all 120 IM lessons kept in order, ten added load days that each carry a stated need, a prerequisite ledger that tests every earlier row, and a year-end check that samples all four fluency standards directly. A-CED.A.1 is split cleanly between rational (unit 2) and exponential (unit 4) cases, and F-IF.C.9 is revisited on days 25, 89, 130 and 159. Its faults are the band's: course-level checks relist codes recorded two or three days earlier and claim every part of up to 17 codes in 25 minutes, and the ledger still says Geometry has no day map. Ready after those fixes; no day moves.

## Findings

### 1. Course-level checks relist codes recorded days earlier and overclaim (moderate)

- What is wrong: day 70 lists all seven unit 3 codes two days after day 68 recorded them, among 17 codes. Day 110 lists F-BF.B.3 two days after day 108; day 111 lists F-BF.A.1a, F-BF.A.1b and S-ID.B.6a three days after it. Day 159 lists all seven unit 7 codes three days after day 156. Day 158 lists 17 codes and carries one extended periodic model plus the four-standard fluency station in a 25-minute short-response budget. The scope and sequence says "each listed code receives prompts for every part within the task". The notes do change the form (audit and sort instead of direct solving), which is right; the codes and the claim are what is wrong.
- Why it matters: collect once says a check within ten days reuses the record. With the station taking about ten minutes, day 158 has about a minute per remaining code, so the record will not support the claim, and the unit planner will try to honor it.
- Fix: day 70 reuses day 68 for unit 3 and samples units 1 and 2 (F-IF.A.3, F-BF.A.2, A-APR.B.2, A-APR.B.3, A-APR.C.4) through the polynomial audit; day 110 and 111 reuse day 108 for unit 5 and sample units 1 to 4; day 159 reuses day 156 for S-IC and S-ID.A.4 and samples F-IF.C.9, A-SSE.B.4, F-LE.B.5, F-IF.C.8b and F-BF.A.1 through the box-production audit; day 158 keeps the periodic model and the station and lists only the codes those two carry (the four fluency standards, F-TF.A.2, F-TF.B.5, F-IF.B.4, F-IF.C.7e) plus at most three short items. Replace the "every part" sentence with "samples the named parts; end-of-unit assessments carried full coverage".
- Evidence: days.csv days 68, 70, 108, 110, 111, 156, 158, 159; scope-and-sequence.md check table and the paragraph below it. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 8 finding 2; Algebra I finding 3; Geometry finding 1).

### 2. The ledger still says Geometry has no day map (low)

- What is wrong: the ledger says "Geometry has no day map yet", marks the six geo rows "intended grade 10 ownership; day evidence pending", and For the lead item 1 asks for that verification. data/plans/geometry/days.csv exists. I traced it:
  - All six geo rows are taught in Geometry (geo-right-triangle-trig days 68 to 105, geo-scaling-area-volume 84 to 105, geo-circle-parabola-equations 109 to 126, geo-transformations-coordinates 106 to 126, geo-arcs-sectors-radians 134 to 160, geo-sample-spaces-events 144 to 157), so retrieval here is correct.
  - Geometry names Algebra I rows only in five-minute retrieval openings (function notation and inverses on day 86, quadratic forms on day 85, exponential functions on day 92, piecewise on day 99, data displays on day 120). Under the band's reading that retrieval does not reset last use (grade 8 "Across the band"), those rows stay last used in grade 9, and readiness here is correct.
  - One exception: alg1-completing-square is taught on Geometry days 110 and 111 (A-SSE.B.3, circle equations) and assessed on day 125. Its last use is grade 10, so retrieval is enough; day 45 checks it needlessly.
- Fix: replace "day evidence pending" with the Geometry days above, mark the ledger verified, close lead item 1, and drop alg1-completing-square from day 45's readiness (retrieve it before day 65). Geometry finding 2 puts A-SSE.B.3 on its day 125 so the record says so.
- Evidence: scope-and-sequence.md ledger and For the lead 1; Geometry days.csv. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 8 finding 5; Algebra I finding 4).

### 3. Day 106's goal is a close paraphrase of the base goal (low)

- What is wrong: day 106 reads "Build a relationship by adding, subtracting, multiplying or dividing familiar function types"; the base's goal for that lesson is to create new functions by adding, subtracting, multiplying and dividing simpler ones. Similarity 0.68, with the same four-verb list in the same order. Day 81 (logarithm as an exponent, 0.69) is near but reads as the definition any text would state.
- Fix: day 106 and its source-map reason, for example "Combine a constant and a decaying rule into one model for a cooling drink and explain what each part contributes."
- Evidence: days.csv day 106 and the same wording in source-map.csv's reason cell; IM Alg2.5.10 learning goals. Confidence: likely. LAYER: sequence. REPEAT: yes.

### 4. Day 135 lists earlier-course codes no Algebra II day teaches (low)

- What is wrong: day 135 lists F-IF.C.7a and F-IF.C.7b as "earlier-family panels"; no Algebra II teaching day carries either code (Algebra I owns 7a, Geometry taught 7b on days 86 and 101). The panels are retrieval of earlier-course work used to close the parent F-IF.C.7.
- Fix: tag the day's skills with the retrieved rows (alg1-quadratic-forms-graphs, geo-scaling-area-volume) and say in the note "earlier-course evidence for the parent F-IF.C.7", so the check claims only what this course taught (grade 8 call 4).
- Evidence: days.csv days 130, 135; Algebra I and Geometry days. Confidence: likely. LAYER: sequence. REPEAT: new.

### 5. Tilde codes raise false gate notes (low)

- What is wrong: sequence.py check reports A-REI.A.2 (unit 2), A-CED.A.1 (unit 4), F-IF.C.9 (unit 6) and S-ID.A.1 (unit 7) "on no day"; each is on a day, written in the frame with a tilde or after a comma.
- Fix: the lead's gate call, as in Algebra I finding 7.
- Evidence: gate output; frame.md units table. Confidence: firm. LAYER: process. REPEAT: yes.

## Checks the brief asks for

- **Source map against the base:** every IM Algebra 2 lesson has a row, 120 base lessons in order. Decisions: 127 keep, 33 ours, 1 merge (modeling prompt 1 into day 12), no cut. The ours days are assessments, response and readiness, and ten load days, each with a reason that holds: 29 (division practice before the Remainder Theorem), 43 (payment derivation), 52 (exponent rewrites before radical equations), 57 (nonlinear inverses, the F-BF.B.4a contribution), 83 (estimation before calculator logarithms), 87 (all parts of A-SSE.B.3 and F-IF.C.8), 115 (measured arcs), 133 (daylight fit), 140 (sampling rebuild for m7-random-samples) and 145 (hand simulation). The layout (base_unit, base_lesson, stretch, day, decision, reason, source_url) is the closest of the three to rule 8.
- **Base order and departures:** unit and lesson order kept; the orbital prompt stays after Alg2.2.3 with supplied data.
- **Our words:** all 120 base-linked goal cells compared with their lesson's title, goals and targets. Six above 0.6; one close paraphrase (finding 3). **Copy rate: 1 of 120 (0.8 percent).**
- **Focus:** on teaching days, 81 of 137 days carry N-RN, N-Q, A-SSE, A-APR, A-CED, A-REI or F-IF codes (59 percent; 49 percent weighted); adding F-LE.A, F-BF.A.1 and S-IC.A.1, 92 days (67 percent). Unit 6 (F-TF) and unit 7 (S-IC) hold the rest, as the course's standards require. No high school bar sets a line.
- **Widely applicable prerequisites:** polynomial arithmetic and structure (A-APR, A-SSE.A.2), rational expressions and equations, rational exponents and radicals, exponential and logarithmic equations, and function building (F-BF) are each taught and assessed.
- **Coherence from Algebra I and Geometry:** Algebra I quadratics, factoring and the formula reopen with readiness before units 2 and 3; exponential functions extend to rational inputs and logarithms in unit 4; Geometry's scaling (area and volume) leads to rational exponents on day 47, right-triangle trigonometry and radians lead to the unit circle on days 113 to 117, coordinate transformations lead to function transformations on day 96, and sample spaces are distinguished from random samples on day 140.
- **Modeling across the course:** eight public prompts on days 12, 18, 48, 91, 105, 134 and 155 (prompts 1 and 2 share day 12), with the daylight fit on day 133 as a further modeling day; supplied data throughout.
- **Rigor:** understanding, fluency and application days in every unit; polynomial arithmetic, rational rewriting, structural rewriting and transformations rotate through the mixed opening.
- **Year-end fluency:** day 158 directly samples A-APR.A.1, A-APR.D.6, A-SSE.A.2 and F-BF.B.3 at untimed independent work. Correct; only the code list around it is crowded (finding 1).
- **Readiness by grade number:** correct after finding 2. The frame says "idle two or more grades" and "used the year before". Every check sits in the last ten minutes of the respond day before its unit (14, 45, 72, 95, 136) or of day 1 after the hook.
- **End days:** each holds one extended task plus short items; unit 6's three end days (133, 134, 135) each hold one. Correct.
- **A-CED.A.1 and F-IF.C.9:** rational case assessed day 44, exponential case day 94; F-IF.C.9 revisited days 25, 89, 130 and checked day 159. Correct.
- **Physics hand-off:** Physics unit 6 (waves, days 77 to 92) precedes Algebra II's periodic unit (day 113); Physics carries the bridge and Algebra II day 129 retrieves waves as a context. The orbital prompt (day 18) uses supplied data and does not presume Physics unit 3. The Algebra I leans are in "Across the band".
- **Calendar:** checks on days 70 to 71, 110 to 111 and 158 to 159 match calendar.csv; week 32 is finals.
- **Shorter path:** present, with ten fold-in days, none assessed.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | 59 percent of teaching days on core algebra clusters; F-TF and S-IC hold the rest |
| Progression coherence | yes | ends every thread; seams to electives named |
| Standard taught in part with no finishing day | yes | A-CED.A.1, F-IF.C.7 parts named |
| Problems that join units | yes | series to loans, transformations through earlier families |
| Fluency spaced and mixed | yes | direct station day 158 |
| Practices named | yes | all eight, tied to days |
| Models consistent | yes | area diagrams for division, unit circle, hand simulation before technology |
| Readiness by grade number | yes | one needless check (finding 2) |
| End days not stacked | yes | one extended task each |
| Collect once | no | days 70, 110, 111, 159 (finding 1) |
| Our words | yes | 0.8 percent |
| Source-map layout | partly | closest to rule 8; differs from the other two |

## What is right and should not be touched

- The ten added load days and their stated reasons.
- The day 158 fluency station and the F-IF.C.7d exclusion with its record convention.
- Hand simulation before technology, margins from simulation rather than formulas.
- Supplied anonymous data, dated nonpartisan polls, no health disclosure on day 154.
- The finance and Government bridges named by week.

## What I could not judge

- Whether the day 31 split and the 25-minute short-response budgets hold with real items; the scope and sequence already flags this.
- Whether the generic tools (graphing, simulation, normal distribution) exist in the catalogue.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Days 70, 110, 111 and 159 reuse the records of days 68, 108 and 156; day 158 lists only what the model and station carry | Collect once; overclaim (finding 1) | days.csv; check table |
| "Every part within the task" sentence replaced | Overclaim | scope-and-sequence.md |
| Ledger verified against Geometry days; lead item 1 closed | Day map exists (finding 2) | scope-and-sequence.md |
| alg1-completing-square leaves day 45 readiness; retrieved before day 65 | Taught and assessed in Geometry | days.csv day 45 |
| Day 106 goal reworded | Close paraphrase (finding 3) | days.csv day 106 |
| Day 135 tags retrieved rows and labels 7a, 7b as earlier-course evidence | Claims only what is taught (finding 4) | days.csv day 135 |

## Across the band

Patterns in Algebra I, Geometry and Algebra II, read beside the grade 8 "Across the band".

- **Year-end fluency is now direct in two of three.** Geometry (day 158) and Algebra II (day 158) each give an untimed independent station for every fluency expectation; Algebra I (days 158 to 159) uses only critique forms, the fault grades 5 to 8 had. The grade 8 call 1 rule works where it was applied.
- **Course-level checks relist and overclaim in all three.** Each relists codes recorded two or three days earlier (Algebra I days 61 and 109, Geometry 46, 47, 104 and 159, Algebra II 70, 110, 111 and 159) and each carries an "every part of each listed code" sentence. The forms do change, which is right; the code lists and the sentence are the fault. Algebra I's "this task form has not appeared" boilerplate is false on day 109.
- **Begun codes reach no record.** Algebra I teaches F-IF.B.4, F-LE.A.2, F-BF.A.1a and others for 8 to 21 days each without naming them on a check; the owners assess them later in other contexts only. Read across the three courses, key features of linear, quadratic and exponential graphs (F-IF.B.4) are recorded only for trigonometric functions. This is the one new pattern.
- **Readiness by grade number is applied correctly in all three,** with the strict reading that retrieval does not reset last use. Geometry verified against real day maps; Algebra I and Algebra II carry stale "day evidence pending" notes from before those maps existed.
- **Base fidelity is complete.** All 376 IM lessons kept in order across the three; only modeling prompts move or are cut, each with a reason that holds. Copy rates 0, 0 and 0.8 percent.
- **Process drift:** two source-map layouts here plus three in grades 6 to 8; focus computed three ways and no high school bar to set a line; tilde codes in frames raise false gate notes in all three.

**Hand-offs between the courses (all hold):**

- Grade 8 to Algebra I: linear functions, equations and systems, integer exponents, irrational numbers and scatter plots, each retrieved in its first Algebra I use.
- Grade 8 to Geometry (skipping Algebra I): rigid motions, dilations, the Pythagorean theorem, coordinate distance and curved volumes, each with a readiness check before its unit.
- Algebra I to Geometry: function notation, rearranging formulas, completing the square, systems and two-way tables, retrieved where Geometry uses them; Geometry teaches completing the square anew for circles.
- Geometry to Algebra II: scaling to rational exponents, right-triangle trigonometry and radians to the unit circle, coordinate transformations to function transformations, sample spaces to sampling.
- Algebra I to Algebra II: quadratics, factoring, exponentials, inverses, piecewise functions and data, each with readiness after a year idle.

**Hand-offs the science courses lean on:**

- Biology (grade 9) and Chemistry (grade 10) hold: each lean is taught in Algebra I before or with a named bridge, and Chemistry carries bridges for Geometry's later N-Q completion.
- Physics (grade 11) does not, by the counted rule. It leans on F-IF.B.6, alg1-writing-equations-constraints (unit 1, weeks 1 to 4), alg1-rearrange-formulas (units 1 to 3 and 6), alg1-quadratic-patterns (units 3 and 4) and S-ID.B.6 (unit 9) and treats all as "earlier year: retrieval". Neither Geometry nor Chemistry teaches F-IF.B.6, quadratic patterns or S-ID.B.6 in grade 10; Geometry only retrieves rearranging (day 114) and Chemistry uses A-CED.A.4 on one day. Algebra II itself gives readiness checks on writing equations (day 14), quadratic patterns and scatter models (day 95), so two grade 11 courses read the same rows differently.

**Calls for the lead (one rule each, for docs/pipeline/briefs/sequence-write.md):**

1. Grade 8 calls 1 to 3 stand unchanged for high school: direct year-end station, check days list only sampled codes, a retrieval opening is never check evidence. Add: a course-level check reuses any record from the last ten days and does not relist its codes.
2. An end-of-unit assessment names each begun code whose taught part it samples, with the part ("F-IF.B.4, quadratic").
3. Decide the open physics item 5 with the trace above: either science courses apply the grade-number readiness rule to their math leans (Physics then adds readiness for F-IF.B.6, writing equations and rearranging before unit 1, quadratic patterns before unit 3, S-ID.B.6 before unit 9, each in the last ten minutes of the preceding respond day), or the rule says math leans in science are exempt.
4. One source-map layout for grades 6 to 11, one focus method, a high school bar filed, and frames that list codes with semicolons and no tilde (or a gate that reads the tilde).

## For Cory

Nothing. Moving a begun standard between courses would be Cory's, but no move is proposed; the fix in Algebra I finding 2 names partial records instead.

## Sources

- Illustrative Mathematics Algebra 2, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math\hs-algebra-2: lesson order, goals, modeling prompts.
- Common Core State Standards for Mathematics, high school (data/standards), and the high school Progressions for algebra, functions, statistics and modeling (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md: no high school criteria; the lens applied instead.

## For the source list

- The same high school bar named in the Algebra I report.
