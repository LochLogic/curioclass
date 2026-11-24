# Sequence read: Precalculus, 2026-11-24

Expert cold read of the Curio Class Precalculus scope and sequence (grade 12), done under docs/pipeline/briefs/sequence-read.md with the math lens and docs/RUBRIC-MATH-HS.md (the grade 12 method: the owned-outcome account, one 15 percent cap, the whole modeling cycle). The scope was written 2026-11-23/24 under docs/pipeline/briefs/sequence-write.md; I did not write it.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-HS.md (the grade 12 courses, what each part asks, multilingual learners, begun parts, gaps 1 to 9), docs/pipeline/briefs/sequence-read.md and sequence-write.md.
- docs/courses/precalculus/scope-and-sequence.md in full, its "For the lead" section item by item.
- data/plans/precalculus/days.csv (160 rows, every column) and source-map.csv (87 rows).
- docs/courses/precalculus/frame.md in full (brief, Seams, Models, Units, Course-level checks, Cross-subject, For the lead, Source map).
- data/progressions/math.csv: the 25 pc- rows and their assumes; data/plans/geometry/days.csv and algebra-ii/days.csv for the last use of the five readiness rows.
- docs/courses/CALENDAR.md (rule 4, 9 to 12) and data/plans/calendar.csv rows for precalculus.
- data/standards/ccss-math-standards.txt and curio-math-electives.txt for the owned codes.
- The base text in the source store (S:\CurioClass-sources\openstax-precalculus-1e\, the 1st edition PDF): every section's "In this section, you will" objectives, extracted and compared with all 160 goal cells.
- Earlier reads: sequence-algebra-ii-2026-11-15.md (and its "Across the band"), sequence-geometry and sequence-algebra-i of 2026-11-15, for REPEAT tags.
- Gates, filtered to this course: `plan.py check` (exit 1 from other courses; `sequence precalculus: 0 failure(s)`, `frame precalculus: 0 failure(s)`, no notes), `sequence.py check precalculus` (0 failures, no notes), `frame.py calendar` (lists K to 8 only; grade 12 has no stagger rule beyond week 32), `stale.py check` (0 failures).

## Verdict

A sound, well-argued year: every unit keeps the frame's order, rows and days, every inner order builds (inverses before logarithms and inverse trigonometry, the law of cosines before resultants, matrices before complex multiplication), every readiness row is correctly placed by grade number, and the four modeling tasks keep the whole cycle with draft, feedback and revision inside their units. The biggest risk is the course-level checks: day 158 lists 19 codes under a "prompt per part" rule, two codes it cannot sample as short items, and each check's first day repeats the unit sitting's task form two days later, against rule 2. One standard part (F-TF.A.3 for any real x) is not on any day's goal. Ready after those fixes; no unit, day count or check week moves.

## Findings

### 1. Course-level checks overclaim and do not name the parts they sample (moderate)

- What is wrong: day 158 lists 19 codes in one 50-minute day that also holds the five-code fluency station; with the station at about 15 minutes, that leaves under two and a half minutes per remaining code, and rule 2 asks a prompt for each part of each listed code. G-GPE.A.3 (derive the ellipse and hyperbola equations from the foci) is a derivation, not a short item. Multi-part codes are listed bare: F-TF.C.9 (prove, use) on days 99 and 158, F-TF.A.3 (two parts) on 99 and 158, CUR-PC.1 (six features) and CUR-PC.3 (reading and inequalities) on day 47. RUBRIC-MATH-HS "Begun parts and parent codes": a check that lists a parent code says which parts it samples.
- Why it matters: a unit planner will try to write prompts for every part of every listed code, and the record will claim what 30 minutes cannot gather.
- Fix: day 158 lists the station codes (F-TF.A.3, F-TF.C.9 use, CUR-PC.7, CUR-PC.4, A-APR.D.7) and at most seven short items: N-VM.C.12, A-REI.C.8, CUR-PC.11, N-CN.B.5, CUR-PC.13 (units 7 to 9) and CUR-PC.3, N-VM.B.4b (earlier). Drop CUR-PC.1, G-SRT.D.11, N-VM.C.8, N-VM.C.10, CUR-PC.10, G-GPE.A.3 and CUR-PC.12 (sampled on day 159). Days 47, 99 and 158 write the part beside each multi-part code ("F-TF.C.9, use"; "CUR-PC.1, symmetry and end behavior"), and the check table in the scope does the same.
- Evidence: days.csv days 47, 99, 158; ccss-math-standards.txt; RUBRIC-MATH-HS. Confidence: firm. LAYER: sequence. REPEAT: yes (Algebra I finding 3, Geometry finding 1, Algebra II finding 1).

### 2. Each check's first day repeats the unit sitting's task form two days later (moderate)

- What is wrong: rule 2 says "A course-level check never repeats a task form given in the last two weeks." Days 45, 97 and 156 are sittings of unseen short items; days 47, 99 and 158 are again unseen short items. The scope names this (For the lead 2) and proposes keeping it because the frame's check design says so.
- Why it matters: the rule exists so a check reads a different face of the same skills; drawing items from earlier units changes the content, not the form. Keeping it sets a precedent the Statistics and Calculus scopes would copy.
- Fix: do not keep. The first check day changes form, no day added: an audit-and-repair set (worked solutions from units 1 and 2 with errors to find, explain and correct, plus "which method and why" items), the form the Algebra II read accepted. The year-end fluency station stays direct with no supplied work, as rule 2 requires; it is a station, not the item set. The frame's Course-level checks paragraph ("short unseen items on the first check day") and table change with it.
- Evidence: sequence-write.md rule 2 ("Collect once"); frame Course-level checks; days.csv days 45, 47, 97, 99, 156, 158. Confidence: likely. LAYER: frame. REPEAT: new.

### 3. F-TF.A.3's "any real x" part is on no day (moderate)

- What is wrong: F-TF.A.3 asks students to use the unit circle to express sine, cosine and tangent of pi minus x, pi plus x and 2pi minus x in terms of their values at x, where x is any real number. Day 51's goal uses the symmetries only "to find exact values at every multiple of the special angles". A writer will build a special-angle table day and day 64 will test only that. Smaller, same kind: F-TF.A.4 is about the trigonometric functions, and day 52 names only sine and cosine (tangent's oddness and period pi are left out); N-VM.C.10 states the determinant fact for any square matrix, and only day 105's 2 by 2 carries it.
- Why it matters: an owned (+) code assessed in part, with no later day that finishes it (the lens's first scope and sequence error).
- Fix: day 51's goal adds "and write sin, cos and tan of pi minus x, pi plus x and 2pi minus x in terms of their values at x for any real x, checked at a non-special angle on the calculator"; day 52 adds tangent; day 64's note says F-TF.A.3 has a prompt for each part (special triangles; the general symmetry). Day 111 adds N-VM.C.10 to its codes and its goal "read the tool's 3 by 3 determinant and see that a zero determinant leaves no inverse".
- Evidence: ccss-math-standards.txt F-TF.A.3, F-TF.A.4, N-VM.C.10; days.csv 51, 52, 64, 105, 111. Confidence: firm. LAYER: sequence. REPEAT: new.

### 4. The Shorter path folds days into each other (low)

- What is wrong: day 129 folds into the openings of days 130, 133 and 134, and day 133 folds into the openings of days 129 to 132; both are in the same ten-day plan, so each folds into the other. Days 14 and 18 both fold into the openings of days 19 and 20, so two days' work lands on the same five minutes.
- Why it matters: a school taking the ten-day path has no place for the conic retrieval or the parametric practice, and the totals line counts minutes it cannot use.
- Fix: replace fold-in day 129 with day 69 (addition formula practice, into the openings of days 70 to 73; no other fold uses them); day 133 folds into the openings of days 129, 130 and 132; day 14 folds into the openings of days 17 and 23 to 25. Total stays 10 days, 500 minutes; the first five rows (the early-leaver order) are unchanged.
- Evidence: scope-and-sequence.md Shorter path table. Confidence: firm. LAYER: sequence. REPEAT: new.

### 5. Two earlier rows are used before their retrieval (low)

- What is wrong: day 34 teaches ln as the inverse of e to the x; e (alg2-number-e-continuous) is retrieved only on day 39. Day 20 shows the fundamental theorem for quadratics by completing the square; alg1-completing-square is retrieved only on day 133, and the opening line "completing the square stays in that opening" names no start day.
- Why it matters: nothing is to be used before it is brought back; a student who has forgotten e or completing the square meets both cold on a first-teaching day.
- Fix: day 34's five-minute opening is the retrieval task for alg2-number-e-continuous (note and skills); day 39 keeps its review of alg2-exponential-growth-rational-inputs and continuous growth applied. Day 20's opening is a retrieval task for alg1-completing-square, and the scope's opening sentence says completing the square stays in the openings from day 20. The Earlier rows table and the minutes line take both (two openings, 10 minutes, inside the stated "at most 70"). Optionally the progression adds alg1-completing-square to pc-polynomial-complex-zeros's assumes.
- Evidence: days.csv 20, 34, 39, 133; math.csv assumes. Confidence: firm. LAYER: sequence (progression for the optional assumes). REPEAT: new.

### 6. No day is tied to a practice (low)

- What is wrong: the frame places all eight practices by unit (C3 column); the scope names none, and no goal or note says where a practice is the task's demand. RUBRIC-MATH-HS lists "named tasks per practice in each scope and sequence" as a gap; rubric gap 4 carries it to the unit plans.
- Why it matters: unit plans then name practices in passing, the lens's unit-level error.
- Fix: one line per unit section in the scope naming the day where each of its frame practices is the demand, for example MP3 days 20, 66, 72, 134; MP4 days 43, 63, 93, 106, 128; MP5 day 41 (tool choice: semi-log or log-log), day 75; MP1 days 84, 155; MP7 days 9, 22, 109; MP8 days 103, 146, 150; MP2 days 40, 92; MP6 days 2, 154.
- Evidence: frame Practices bullet; RUBRIC-MATH-HS "What each part asks". Confidence: likely. LAYER: sequence. REPEAT: new.

### 7. No line on how the language goals grow (low)

- What is wrong: every section has a language goal (good), all of the same kind (explain, say, describe, justify, with a sentence frame). RUBRIC-MATH-HS multilingual criterion 2 and gap 9 ask the scope for a line on how language goals grow across the course toward independence.
- Fix: one sentence under Language goals: units 1 to 3 give sentence frames and a word bank on every goal; units 4 to 7 give frames for new forms only (proof links, law choice, matrix meaning); units 8 to 10 drop frames on the written goals and keep them for spoken ones; precision rises from naming features (unit 1) to justifying each step (units 5, 6, 9).
- Evidence: scope-and-sequence.md Language goals; RUBRIC-MATH-HS. Confidence: likely. LAYER: sequence. REPEAT: new.

### 8. Two kept Progressions checks rest on documents that may not exist (low)

- What is wrong: units 2 ("Number, complex numbers") and 8 ("Number, the complex plane") keep a Progressions check; as far as I know (from memory) no Progressions document covers the (+) complex number or vector and matrix clusters. Units 6 and 7 already carry the right note; 2 and 8 do not.
- Fix: units 2 and 8 take unit 6's note ("the unit plan records that no Progressions document covers it, and the check ends there") for their N-CN part.
- Evidence: from memory; scope units 2, 6, 7, 8. Confidence: likely. LAYER: process. REPEAT: new.

### 9. Day 116's goal is close to the base objective (low)

- What is wrong: "Convert points and equations between polar and rectangular form" against the base 8.3 objective "Transform equations between polar and rectangular forms" (similarity 0.80, highest of 160 goals; day 117 at 0.75 repeats it). Every other goal is 0.65 or below.
- Fix: day 116 "Turn a polar point into x and y with the unit circle and back with the angle's quadrant, then rewrite r = 4 cos theta as a circle's equation"; day 117 "Practice moving points and curves between the two grids."
- Evidence: base PDF section 8.3 objectives; days.csv 116, 117. Confidence: likely. LAYER: sequence. REPEAT: yes (Algebra II finding 3).

### 10. Day 141, a Fluency day, lists a derivation code (low)

- What is wrong: day 141 practices standard forms and naming conics (CUR-PC.13) and lists G-GPE.A.3, which is the derivation from the foci; no practice task derives.
- Fix: day 141's codes are CUR-PC.13 only.
- Evidence: days.csv 136, 138, 141. Confidence: firm. LAYER: sequence. REPEAT: new.

### 11. Stale lines in the frame (low)

- What is wrong: the frame's Day kinds bullet says Fluency is "about one day in eight" (the scope has 12 of 151); its Base text bullet still says "the scope writer checks each placement against the loaded PDF" (done; the scope says they match); its Check 3 cell names three fluencies, not the four the station samples.
- Fix: in the scope fix pass, the frame reads "about one day in twelve", "checked against the loaded PDF (scope, 2026-11-24)", and Check 3 names A-APR.D.7 in the station.
- Evidence: frame.md; scope intro and For the lead 1, 6. Confidence: firm. LAYER: frame. REPEAT: new.

## Checks the brief asks for

- **Order inside each unit:** holds, apart from finding 5. Each arc reaches its compelling question: day 31's every zero, day 43's wolf counts, day 63's tide, day 77's equations from models, day 93's boat, day 106's network, day 128's ball, day 140's general conic, day 155's road-to-calculus set.
- **Assessments:** every unit's end day lists every owned code and part (unit 6 over days 85 and 97); response counted once on each respond day; no unit over 25 days, so no mid-unit assessment. Each end day holds one sitting.
- **Readiness or retrieval:** every row in the scope's table matches the pc- rows' assumes. The five readiness rows are each last used in grade 10 (Geometry days 26, 67, 104, 118, 143; no Algebra II day uses them), and every check sits in the last ten minutes of the respond day just before its unit (49, 101, 132). No year-before row gets readiness; no older row is only retrieved; no unit's first day holds a check. geo-solving-right-triangles is retrieved in unit 6 after unit 4's use, correctly.
- **Checks that do not repeat:** each check follows a unit end and draws no items on it, and says so (days 47, 99, 158); day 159 asks unit 10's rate skill in unit 8's content. The form still repeats (finding 2).
- **Standards in full:** every lettered part is on a day (4b, 4c, 4d; N-VM.B.4a to c; 5a, 5b). One part missing (finding 3).
- **Days by load:** each row's days match the frame's loads within a day (for example unit 6: 6, 5 and 6 teaching days for loads of about 7, 6 and 6 with the two sittings and the respond day). No run is far over or under.
- **Calendar:** checks on weeks 10, 20 to 21 and 32, as the frame and calendar.csv give; grade 12 has only the week 32 finals rule. No same-year leans; the five earlier-year leans each carry the frame's bridge (days 42, 56, 92, 128, 137). No stagger break.
- **Candidate cells:** all ten settled: ten Progressions checks kept at zero student days, every extension kept inside a day or dropped with a reason (units 4, 5, 8).
- **Shorter path:** present, 45-minute and ten-day versions; the ten-day table needs finding 4.
- **Source map:** rule 8 layout; every base section 1.1 to 12.4 and Appendix A placed or cut with a reason; order departures (8.8 forward, chapter 9 before 8.3 to 8.7, 12.4 before 12.1, 4.7's logistic after 4.8) each carry a reason and "no" harm with why. Day notes and source-map days agree.
- **Our words:** 1 of 160 goals close to a base objective (finding 9).
- **Minutes line:** 14.5 review days match the frame's row loads exactly; 725 + 30 + 350 = 1,105 of 7,550, 14.6 percent. Finding 5 adds two openings inside the stated 70.
- **Kinds:** 96, 22, 12, 17, 13 as stated; every Fluency day practices only what an earlier day taught.
- **Stale notes:** stale.py clean; frame lines in finding 11.

## Lens checklist (scope and sequence layer)

| Lens item | Holds | Note |
| --- | --- | --- |
| Standard taught in part with no finishing day | no | F-TF.A.3 general x (finding 3) |
| Problems that join units on purpose | yes | days 48, 100, 121, 124, 130, 155, 159 |
| Fluency given spaced, mixed practice | yes | named fluencies in the openings all year; direct station day 158 |
| Owned-outcome account | yes | every owned code taught in one unit and assessed on its end day |
| 15 percent cap | yes | 14.6 percent, summed in the scope |
| Modeling cycle whole | yes | units 3, 6, 7, 8 draft, feedback, revision; tide compact cycle |
| Readiness by grade number | yes | all five checks correct |
| Collect once | yes | records reused with dates |
| Checks claim only what they sample | no | day 158 and part labels (finding 1) |
| Practices tied to tasks | no | finding 6 |
| Language goals grow | no | finding 7 |
| Models introduced and carried | yes | vector-arrow 86, matrix 102, polar-grid 115, construction warm-up 134 |
| Major work share | not applicable | grade 12 method replaces it |

## What is right and should not be touched

- The inner orders: one lettered inverse part a day (10 to 12), the logarithm entering as unit 1's inverse, inverses of trigonometric functions after the graphs that show monotonic intervals, proof rules set on day 66 before any formula.
- The readiness placements and the Earlier rows table, including the one-hop reasoning.
- Unit 6's two sittings with one respond day, and the four modeling tasks each with a revision on a day that is neither the end day nor a first-teaching day.
- The paper path and device notes, especially A-REI.C.9 never met by a given inverse alone.
- The Calculus hand-on table and day 121's polar intersections.
- The sensitivity choices (carbon dating, wolves, ships and planes with no military context, points never bets).

## What I could not judge

- Whether 30 written-feedback forms can return in two school days for unit 8 (draft 128, revision 130); a pilot teacher would tell.
- The Calculus scope's day numbers in the hand-on table (I did not open the Calculus scope).
- What the high school Progressions say on each kept check; they are not in the source store and I did not reach them.

## For the lead (the scope's items, judged)

1. **Fluency count:** agree. The kinds follow the days; the frame line changes (finding 11).
2. **Same task form:** do not keep; change the first check day's form (finding 2).
3. **Unit 6 response on day 98:** keep, and draw day 89's opening from day 85's most-missed law-of-cosines items, since day 89 reuses the law; the feedback goes back on day 87 as planned. Response time stays counted once on day 98.
4. **Report turnaround:** keep with the one-page form; note unit 8's two-evening gap (draft 128, feedback 130) in the unit plan.
5. **Progressions documents:** load the free high school Progressions (Algebra, Functions, Modeling, Geometry) into the source store before the unit plans; mark the N-CN and N-VM parts "no document" (finding 8).
6. **A-APR.D.7 in the station:** agree; the frame's Check 3 cell names it (finding 11).
7. **Check 3's extended task:** agree, with the rate fixed as one coordinate (height) against time at an instant, estimated from secant slopes of a table, never dy/dx along the curve, which is Calculus's.
8. **Frame For the lead 5:** agree it stays open; it is a Calculus-row edit.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 158 lists the station codes plus seven short items (N-VM.C.12, A-REI.C.8, CUR-PC.11, N-CN.B.5, CUR-PC.13, CUR-PC.3, N-VM.B.4b) | Samples only what 30 minutes can (finding 1) | days.csv 158; scope check table |
| Days 47, 99, 158 name the part beside each multi-part code | Parent codes say which parts (finding 1) | days.csv; scope check table |
| Day 51 adds the any-real-x symmetry; day 52 adds tangent; day 64 prompt per part | F-TF.A.3, F-TF.A.4 in full (finding 3) | days.csv 51, 52, 64 |
| Day 111 carries N-VM.C.10 with a 3 by 3 determinant on the tool | Square matrices, not only 2 by 2 (finding 3) | days.csv 111 |
| Shorter path: day 69 replaces 129; 133 into openings 129, 130, 132; 14 into openings 17, 23 to 25 | No fold into a folded day (finding 4) | scope Shorter path |
| alg2-number-e-continuous retrieved in day 34's opening; alg1-completing-square in day 20's | Nothing used before it is brought back (finding 5) | days.csv 20, 34, 39; scope table |
| Day 116 and 117 goals reworded | Our words (finding 9) | days.csv 116, 117 |
| Day 141 lists CUR-PC.13 only | A practice day does not claim a derivation (finding 10) | days.csv 141 |
| Day 89's opening drawn from day 85's most-missed law-of-cosines items | Lead item 3 | days.csv 89 |
| Day 159's rate is height against time from secant slopes | Lead item 7; keeps dy/dx with Calculus | days.csv 159 |
| Units 2 and 8 take unit 6's Progressions note | Finding 8 | scope units 2, 8 |

## For Cory

Nothing. No finding changes scope, money, people or audience.

## Sources

- OpenStax Precalculus, 1st edition (CC BY 4.0), source store PDF: section objectives for the our-words comparison and the source-map placements.
- Common Core State Standards for Mathematics, data/standards/ccss-math-standards.txt: the (+) code texts (F-TF.A.3, F-TF.A.4, N-VM.C.10, G-GPE.A.3 and the rest).
- data/standards/curio-math-electives.txt: CUR-PC.1 to CUR-PC.16.
- docs/RUBRIC-MATH-HS.md: the grade 12 method, parent-code rule, gaps 4 and 9.
- High school Progressions (Common Core Standards Writing Team) and the High School Publishers' Criteria: from memory, not reached; nothing above rests on them except finding 8, marked likely.

## For the source list

- The OpenStax Precalculus PDF's objectives extract cleanly with pymupdf by splitting on the marker "In this section, you will:" (73 sections); useful for every later our-words check on this course.
