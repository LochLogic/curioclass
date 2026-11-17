# Fix: math-grade-6 unit 5 (docs/courses/math-grade-6/s05.md), 2026-11-17

Findings merged: 14 (assessment 5, sources 4, sequence 6; sources 4 and sequence 5 are one finding on tool marks and TOOL-ASKS.md). Fixed: 11. Rejected: 3. Held up per lens: assessment 5 of 5, sources 4 of 4, sequence 3 of 6 (4 and 5 fully, 2 in part). Gate: unitplan.py check math-grade-6, s05.md PASS.

Fixed:
- Assessment 1: S6 is now an invented edging strip (5,347 millimetres into 26 pieces); numbers and key kept.
- Assessment 2: P1, E84, E86 and E87 now name "the greater of the two factors' decimal-place counts" for letter C.
- Assessment 3: Judging now says day 91's case is checked by E91, the scaled step of S4 (1814.4 / 48) and the E95 sharing cards. No new item, so S6 and P1 keep their minutes.
- Assessment 4: field 7 says written feedback is returned in minutes 6 to 10 of day 95.
- Assessment 5: H now sits before I in the register (no letter changed).
- Sources 1: the progressions home page (archive.math.arizona.edu/ime/progressions/, the address already used elsewhere in the repository) is named beside the link.
- Sources 2 and 3: field 10 says where the CC BY statement was read, the edition in the credits, that 6.5.2 and 6.5.15 were not read (inferred from the sources-read list), and that the hook and day 93 layout are original text.
- Sources 4 and sequence 5: field 8 gives the place-value chart (light) and area model (key), their days, job and paper verdict; it says TOOL-ASKS.md holds no entry for paper models, as in the sibling grade 6 plans.
- Sequence 2 (in part): day 92's twenty practice minutes are now decimal-by-decimal division with feedback, at least four cases, one with a zero in the quotient.
- Sequence 4: field 8 states printed charts on days 82, 84, 89, 92 only, blank paper from day 93, and that the ruler is for day 86 drawings, not day 93 measuring.

REJECTED: sequence 1 | Days 90 and 91 are fluency days resting on only an 8-minute decimal extension on day 89, so narrow day 89 and give day 91 a 10-minute model | It moves teaching content between days, which the fix brief forbids (no moved content), and the days.csv kinds are fixed | the fix brief (step 3)
REJECTED: sequence 3 | Day 93 should be preceded by a 5-minute mini measurement plan in day 92's synthesis, and 6.5.14 should be marked changed | Day 92's 50 minutes are fully budgeted and a new activity is new content; the source-map mark is a data row, not the plan | the fix brief (step 3)
REJECTED: sequence 6 | Day 89 holds five ideas; move decimal continuation to a 10-minute model on day 90 | It moves content to another day and rewrites day budgets, which the fix brief forbids | the fix brief (step 3)

LEAD:
- days.csv: remove place-value-chart from days 94 and 95, and consider ruler on day 93 (sequence 4).
- source-map.csv: row 6.5.14 should read change, since day 93 turns that lesson into the unaided sitting (sequence 3).
- days.csv and plan: the lead may rule whether days 90 and 91 can stay typed Fluency while day 89 first teaches decimal continuation and decimal sharing in 8 minutes (sequence 1 and 6).
- Day 93's opening on an assessment day cannot retrieve decimal-by-decimal division without reteaching; sequence 2's request to change it was not made.
