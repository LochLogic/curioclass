# Fix report: algebra-ii unit 3 (docs/courses/algebra-ii/s03.md), 2026-11-17

Findings merged: 15 (assessment 4, sources 4, sequence 7). No finding was named by two lenses. Fixed: 11. Rejected: 4.
Held up per lens: assessment 4 of 4, sources 1 of 4 (the others were sound but over the cap), sequence 6 of 7.
Gate: `unitplan.py check algebra-ii` reports PASS for s03.md (1,250 words or fewer outside fields 4, 5, 6).

Fixed:
- Assessment 1: E2a Meets sample now names the power-of-a-power law.
- Assessment 2: E4 prompt names the method for each of E4a to E4e.
- Assessment 3: D wrong answer added to E1a ("sqrt(9) is 3 or -3"); response group line now reads I, J, K, M, N.
- Assessment 4: E4e asks about no real x-intercepts.
- Sources 3: gap table cells use the source-map titles ("Finding Unknown Inputs", "Rational and Irrational Solutions").
- Sequence 1: readiness intro and both retrieval rows now say unit 2 only retrieved in openings and day 45 item 5 is the record.
- Sequence 2: Teaching now models i on day 59, sums on day 60, products on day 61, properties check on day 62.
- Sequence 3: Teaching now puts negative powers and reciprocals on day 51.
- Sequence 4: hook reworded to 3^4 divided by 3^2, 3^4 times 3^2 and 3^4 divided by 3^6, each as one power.
- Sequence 6: gap response names where rational and irrational repair goes (day 46 support, else day 50's first five main-task minutes; day 47 opening capped).
- Sequence 7: Teaching says day 57 models the scaled-cube inverse before stepping back for verification.

REJECTED: sources 1 | The Number and Algebra progression PDFs are linked from a third-party host as dated drafts, with page ranges tied to no named edition | The dates are already in each file name in the link, and I could not verify an official archive address, so a new link would be unchecked; adding edition dates also broke the word cap | the writer's brief (word cap) and UNIT-PLAN length cap
REJECTED: sources 2 | Day 48 converts to full-size lengths but field 10 never says where full-size figures come from | The plan already says the toy dimensions are supplied and "invented for practice", and field 10 says to print "invented for practice" on invented contexts; the extra sentence did not fit the word cap | UNIT-PLAN length cap
REJECTED: sources 4 | The Read link points to the student view, not the teacher pages | The teacher URLs are in source-map.csv rows for unit 3, which field 10 already cites; a clause to say so did not fit the word cap | UNIT-PLAN length cap
REJECTED: sequence 5 | Day 48 is coded N-RN.A.2 but rational exponents come on days 49 to 51, so add that day 48 uses cube roots only | The Teaching fix for this fell over the word cap once the other sequence fixes went in; the cause is the days.csv code, which is a lead item | UNIT-PLAN length cap

LEAD:
- days.csv codes day 48 N-RN.A.2 before rational exponents are taught on days 49 to 51; consider removing that code from day 48, or add to the plan that day 48 uses cube-root notation only (sequence 5).
- Days 60 and 61 (kind Fluency) and day 51 (Fluency) teach new content; consider typing them Understanding or noting it (sequence 2 and 3).
- Day 57 (Application) teaches the new rational inverse; consider its kind (sequence 7).
- The skeleton Check set line still lists "locating powers of i on a drawn plane" as an extension, although scope-and-sequence drops it and field 2 limits exclude complex-plane work; the generated line cannot be edited from the plan (sequence lead note).
- Source-map.csv or the generated field 10 could carry the teacher unit page link and the dated progression editions (sources 1 and 4).
