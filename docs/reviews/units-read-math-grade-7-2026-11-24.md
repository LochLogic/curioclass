# Units read: math-grade-7, 2026-11-24

COURSE-RUN stage 4 (Reads) for Curio Class math-grade-7.

## What was read

- Scope and sequence for math-grade-7.
- Unit plans s01 to s08 read together: fields, merged U-fields, goal maps, retrieval and readiness tables, and response allocation.
- days.csv rows for the course, including days 120 to 124.
- Continuity in: grade 6 s01 to s03 Returns and Carried lines, and grade 6 s08 field 3.
- Continuity out: grade 8 s01 fields 3 and 4.
- Lead list (docs/reviews/lead-list-lens-pass-2026-11-17.md): no math-grade-7 sections.

## Verdict

The eight units form a sound arc: proportional reasoning, then rational numbers, then expressions and equations, then geometry and probability. Hand-backs between units hold, and continuity runs cleanly from grade 6 and out to grade 8 unit 1. The faults were small cross-unit slips: one wrong day pointer, one readiness item labeled as retrieval, stale handoff wording and a stale course focus total. Focus accounting differs between units, but the course stays above 65 percent under any consistent rule.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| F1 | medium | s06 field 3 Returns pointed at day 122 for angle equations. days.csv and s07 put them on day 124, and day 122 has no equations. | fixed (s06: day 124) |
| F2 | medium | s07 field 4 called item 3 (m5-shape-hierarchy, last used in grade 5) retrieval. The two-grades-back rule, the scope and sequence and day 120 all make it readiness. | fixed (s07: item labeled readiness; "All four items are readiness") |
| F3 | low-medium | s08 day 153 gave 3 minutes of written feedback in-period for S153. That is not workable as teacher feedback for 30 students. | fixed (s08: partner written feedback against the S153 look-fors; teacher scores after day 154) |
| F4 | low | s01 and s02 Handoffs said the grade 6 unit plans were unwritten. They now exist, and they tie and withdraw ratio tables, double number lines and tapes. | fixed (s01, s02) |
| F5 | low | s04 Carried said "Introduce the tape diagram on day 47". Tapes are a grade 6 model (m6-ratio-parts-problems). | fixed (s04: "Restore grade 6's tape diagram") |
| F6 | low | s04 day 63 and s05 day 74 use the verb "distinguish" with production exits labeled recognise. | no change: the checker treats distinguish as a recognise verb, so the label is correct for the gate; the exits still include a recognising part |
| F7 | low-medium | Focus accounting differs: units 1 and 7 count assessment-production minutes as major, the other units exclude them. s02 quoted a stale course total (4,101 of 6,302). | fixed in part (s02 stale sentence cut); scope-and-sequence recount for the structure pass |
| F8 | minor | A blank line in the s06 field 4 retrieval table split the day 109, 112 and 115 rows into a headerless table. | fixed (s06) |

Checked and found to hold:

- Sampled item arithmetic in units 1 to 8.
- Retrieval entries point only at rows already taught.
- Mid-unit and end-of-unit timing.
- Day 68 readiness from unit 4 into unit 5.
- Grade 6 unit 8 continuity into the grade 7 unit 8 retrieval on days 148 and 149.
- Grade 8 day 1 and 2 retrieval of m7-scale-drawings, m7-triangle-conditions and m7-angle-relationships.
- Day 71 is the first Fluency day for 7.NS.A.1d. The properties are named on day 70, so no change is needed.

## Lead-list items worked

None: the lead list has no math-grade-7 sections (0 fixed, 0 rejected).

## Day faults

None: no day skeletons exist for math-grade-7 yet.

## For the structure pass

- docs/courses/math-grade-7/scope-and-sequence.md focus paragraph: pick one rule for assessment-production minutes and recount.
  - Under the units' own figures: about 3,997 of 6,129 minutes, 65.2 percent.
  - With unit 1 and unit 7 production also excluded: about 3,977 of 6,029 minutes, 66.0 percent.
  - The 65 percent line holds either way. The current 4,177 of 6,390 (65.4 percent) mixes both rules.

## For Cory

Nothing on scope, audience, money or people.

## Gate results

- unitplan.py check math-grade-7: PASS on s01 to s08.
- sequence.py check math-grade-7: 0 failures.
- goalmap.py audit math-grade-7: no failures.
