# Units read: math-grade-6, 2026-11-24

COURSE-RUN stage 4 (Reads) for Math Grade 6, all eight unit plans read together.

## What I read

AGENTS.md, COURSE-RUN stage 4, EXPERT.md, lenses/math.md, UNIT-PLAN.md, GLOSSARY.md; the course frame.md, scope-and-sequence.md, DEFAULTS.md, days.csv and source-map.csv; s01.md to s08.md in order (generated skel blocks and day lists read only where a cross-unit claim pointed at them); the course's rows in data/progressions/math.csv (m6-, plus m3-scaled-graphs and m4-factors-multiples as readiness and retrieval rows); math-grade-5 s10.md (continuity in); math-grade-7 s01.md (continuity out); the math-grade-6 sections of docs/reviews/lead-list-lens-pass-2026-11-17.md. No day files or day skeletons exist for this course, so there are no day faults.

## Verdict

The eight plans hold together well: unit loads match days.csv (18, 21, 20, 20, 14, 22, 22, 16 days), the arc runs area, ratios, rates and percent, fraction division, decimals, expressions and equations, rational numbers, then data, and the two readiness hand-backs (day 119 and day 141) are written the same at both ends. The cross-unit faults were small: a return pointing at the wrong day, a hand-back whose error letters did not match the receiving unit, a broken error-register table, a print-only unit naming a key tool, and UK spellings in every plan. All are fixed; the remaining open items are course data or generator changes for the structure pass.

## Findings

1. **s06 field 6: blank lines split the error register (moderate, fixed).** Three blank lines after row T ended the table, so rows U and V rendered as loose text and any table reader would drop them, though field 7's response groups name them. Removed the blank lines.
2. **s05 field 8: print-only unit names a key tool (moderate, fixed).** "Area model (key)" while every task is on paper breaks UNIT-PLAN rule 9. Changed to "(light)" and the sentence now says the section has no key tool.
3. **s01 field 7: hand-back letters do not match (minor, fixed).** "Unit 6 assesses G and H" uses s01's letters; s06 holds the same errors as M and N (days 108 and 109). Added "(its letters M and N)".
4. **s03 field 3 Returns: wrong day (minor, fixed).** Percent tapes for equations are on day 102 (base 6.6.7, s06 error T), not day 96 (story tapes). Changed to day 102.
5. **US spelling in all eight plans (minor, fixed).** Metres, centimetres, kilometres, litres, millimetres, colour, labelled, modelling, practise (verb), licence and optimisation replaced outside skel blocks and day lists, per AGENTS.md. The generated blocks still carry UK spellings from days.csv notes and generator text; see the structure pass.
6. **Grade 7 s01 field 3 is stale on grade 6 (minor, for the structure pass).** It says the grade 6 unit plans are unwritten; all eight now exist and are read. Not this course's file.
7. **s06 U7 places "one agreeing value cannot prove equivalence" on day 111 (no change).** Day 111 is the false-equivalence critique (days.csv MP3 note), so the talk prompt fits even though error L first appears earlier.
8. **s06 error V "Day 112, after E111" (no change).** It deliberately places the error after the exponent exits.
9. **Readiness hand-backs (no change).** Day 141: s07 R1 and R2 and s08 R1 and R2 are the same cards with the same keys, and both name the day 143 rebuild. Day 119 (m4-factors-multiples): s07 retrieves it on day 136, matching days.csv and the progression (grade 4 row, two grades back).
10. **Goals, exits and practice (no change).** Goal-map verbs match exit and practice shapes in every unit; no review entry points at a row not yet taught; course checks on days 80, 118, 158 and 159 sample only rows taught before them. All s08 keys re-solved cold (quartiles, mean absolute deviation, bins) and are correct.
11. **Continuity (no change).** In: grade 5 unit 10 hands on graph and shape-hierarchy records; s01 day 1 retrieves fraction area and the shape hierarchy. Out: grade 7 unit 1 retrieves m6 ratio, area, decimal, fraction division and unit-conversion rows on days 1 to 12, all taught here; s08 day 160 hands sampling and comparison to grade 7.

## Lead-list items worked

31 items (28 LEAD, 3 CAP rejections). Fixed in a plan: 0. For the structure pass: 22. No change: 9.

- **No change (9):** s01 Sources 1 (open student tasks are read at day writing); s01 Sequence 3 (the plan already states both major-work shares); s01 CAP sources 3, 4, 5 (verified-or-none still holds; no verified edition or US source in hand); s03 and s06 TOOL-ASKS.md asks (every unit is paper only, so rule 9 needs no TOOL-ASKS entry; s05 now says so); s05 day 93 opening (an assessment day cannot reteach); s08 Sequence 4 (field 2 deliberately limits 6.SP.B.5d on day 150 to linking a departure to mean and MAD, and E150 uses it that way).
- **For the structure pass (22):** listed below.

## For the structure pass

days.csv (data/plans/math-grade-6/days.csv), each still true today:
- Days 28 and 29 tools: remove coordinate-plane (and ratio-table unless a changed example uses it).
- Days 49, 58, 59 tools: cut to two parts a day (rule 8); days 49, 57, 58, 59 notes: remove the "On a 45-minute period" boilerplate (course period is 50 minutes).
- Day 65 tools: add number-line. Day 71: goal drop "missing-width"; tools drop area-model.
- Days 94 and 95 tools: remove place-value-chart; consider ruler on day 93.
- Day 103 tools: cut to tape-diagram; equation-balance. Day 106: consider kind Understanding rather than Fluency.
- Day 130 tools: drop coordinate-plane and array; supplies drop grid paper.
- Supplies: day 142 ruler and teacher-supplied paper strips; day 144 printed dot plots; day 148 paper counters; day 149 paper strips; day 150 paper data cards; day 153 paper number cards.
- s01 Sequence 2: decide whether area-model and net stay in the tools column for print-only days, and whether the U6 table gets a tool column.
- Notes text: US spelling (metres, centimetres, kilometres, litres, colour, labelled, modelling) so regenerated skel blocks and day lists match the plans.
- Lead ruling (s05): whether days 90 and 91 stay Fluency while day 89 first teaches decimal continuation and decimal sharing in eight minutes.
- Fermi day (s02): a fully modeled Fermi day before day 37 would need a days.csv change; no day may be added.

Generator (scripts/unit_skeleton.py or its inputs):
- Practices line in the skeleton stops after "MP2" (s03, s04); regenerate in full.
- s02 sensitive-topics line ends "Standards in full: 6.RP.A.3b, 6.RP.A.3c, 6.RP.A.3d"; list only the unit's own parts.
- s06 source-map summary: filter to the unit's days (days 118 and 119 are outside it; "ours 5" should be 3); decide whether the weight line may name Student Achievement Partners.
- s08 skel hazard line: remove the pointer See "For the lead" item 5.
- s04 assumed-rows table: list m5-fraction-area for the day 60 fraction-by-fraction prompt.

source-map.csv (data/plans/math-grade-6/source-map.csv):
- Row 6.5.14: keep to change (day 93 is the unaided sitting).
- Row 6.4.17: change keep if the frame meant day 77 as a sitting only.

Sources (course-wide, verified before adding):
- s01 Sources 2: read IM 6.1.11 for the inclusive trapezoid definition and name where the progression states it; if IM differs, add "definition changed from the base text" to day 10.
- s01 Sources 3 to 5, s03, s04 Sources 3: one fixed progression edition with printed pages; one verified US school safety guide for scissors and boxes (replacing the shared UK page); the standards publisher and license line; the NIST link (s03).
- s04 Sources 2 (also s05, s07): the progression writers' own Number System draft, if it exists, to replace the conference handout link.

Other course:
- docs/courses/math-grade-7/s01.md field 3 Handoffs: replace "the unit plans are unwritten" with a note that grade 6 unit plans exist (read 2026-11-24) while delivery evidence and Tomorrow lines are still unavailable.

## Gate results

- `python -X utf8 scripts/unitplan.py check math-grade-6`: PASS s01 to s08.
- `python -X utf8 scripts/sequence.py check math-grade-6`: 0 failures.
- `python -X utf8 scripts/goalmap.py audit math-grade-6`: no FAIL lines.

## For Cory

Nothing. No finding touches scope, audience, money or people.
