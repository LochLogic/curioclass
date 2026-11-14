# Fixes: math course frames, grades 3 to 5, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-math-grade-<n>-2026-11-14.md`) and the Codex reruns
(`frame-math-grade-<n>-codex-rerun-2026-11-14.md`) for grades 3, 4 and 5 to the three frames,
`data/progressions/math.csv` and one sentence of the grade 2 frame's Seams section. The older
`frame-math-grade-<n>-codex-2026-11-14.md` reads withheld their verdicts over a gate failure and were not used. Every
expert finding and every "Settled by the expert" row is applied; each Codex finding was weighed on its merits; the
writers' own "For the lead" items were weighed too.

Base-text claims were checked against the source store (S:\CurioClass-sources\illustrative-math, lesson titles,
Addressing tags and activity timelines read with a script): grade 3 lessons 3.2 and 3.5 tag 3.OA.D.9 and 3.16 tags
3.OA.C.7; 3.8 to 3.10 are the three subtraction-algorithm lessons; grade 4 lessons 2.1 and 2.2 tag no grade 4
standard; 7.13 to 7.15 tag 4.MD.C.7; 5.11 is "Pounds and Ounces"; no dollars-and-cents problem sits in 5.10 to 5.13;
grade 5 lesson 1.10 and 2.13 tag 5.OA.A.1; 5.8.1 and 5.8.2 are 10 + 15 + 20 and 10 + 20 + 15 minutes, 5.8.7 and 5.8.8
10 + 15 + 20 and 10 + 15 + 15.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check math-grade-3 math-grade-4
math-grade-5` 0 failures each (grade 3 8 units, 160 days, 144 in units; grade 4 9, 160, 145; grade 5 10, 160, 145);
`scripts/frame.py check math-grade-2` 0 failures; `scripts/progression.py check math` 305 rows, 0 failures;
`scripts/stale.py check` 0 failures. Unit counts and totals unchanged; grade 4 moved one day from unit 2 to unit 9.

## Grade 3

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Supply-table header rewritten (the science and social studies frames are written, the bridges are theirs); 3.MD.B.4 bridge "whole inches or whole centimetres until unit 7"; 3.MD.A.2 bridge "washers held, no grams"; 3.MD.B.3 "no bridge needed: science unit 3 starts near school day 49" |
| Expert | 2 | Applied | Unit 3 says lessons 2 and 5 begin m3-arithmetic-patterns (addition table); unit 4 finishes 3.OA.D.9 with the multiplication table and the addition-table patterns recalled |
| Expert | 3 | Applied | 3.3 merge row: day 1 lesson 8's warm-up and first activity, lesson 9's main activity; day 2 lesson 10's two activities; one synthesis and our exit question a day |
| Expert | 4 | Applied | 3.8.12 to 15: decision "cut", reused as warm-up routines |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Applied | Unit 3 rounds within 1,000 to 10 or 100, three-digit numbers to the ten also taught and checked (3.NBT.A.1 in full; base lesson 3.15 does it); m3-round notes match |
| Codex | 2 | Applied | Fluency bullet: short spaced practice of understood facts (2, 5, 10) from unit 1 (base 1.15), kept up in units 2 and 3 (3.16 practises facts); unit 4 owns the strategies and adds division facts. The row already names practice in units 1 and 3 |
| Codex | 3, 7 | Applied | Same as expert 1 |
| Codex | 4 | Applied | Unit 7 practices MP2 (anchor: base 6.12, measurement situations as tape diagrams and equations) and MP5; the Practices bullet lists where all eight sit |
| Codex | 5 | Applied | Same as expert 2 |
| Codex | 6 | Applied | For the lead item 1: 9,600 minutes in 45-minute periods is about one third more (214 periods); a 160-day, 45-minute path cuts the minutes by a quarter. The choice stays Cory's |
| Codex | conflict | Expert kept | Codex calls the merge selection and the "split" label not defects; the expert settled both, and a defined word and a named selection cost nothing |
| Writer | lead 1 | For Cory | Time a day |
| Writer | lead 2, 3 | Kept | The base text's unit 8 as 8 year-review days (its lessons add no standard; both readers agree); unit 4 split at its section edge |
| Writer | lead 4 | Kept | Inclusive trapezoid for grades 3 to 5: the base text's own definition from grade 4, named in grade 5 lesson 7.5; the grade 4 and 5 frames say the same |
| Writer | lead 5 | Updated | Now names the two row notes this pass changed |
| Found in passing | | Applied | Sensitivity bullet: no community reader needed, but a qualified math content reviewer reads every check item and key before the course is called finished (FOUNDATION 7.3; Codex grade 5 finding 3, applied in all three grades) |

Counts: applied 4 expert + 7 Codex (3 of them duplicates of expert findings); rejected 0; for Cory 1.

## Grade 4

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | 4.7.14 and 4.7.15 un-merged (all of 4.MD.C.7 by equation, a day each); 4.2.1 and 4.2.2 (grade 3 review, no grade 4 tag) merged into one readiness day. Unit 2 18 to 17 days, unit 9 21 to 22; units 3 to 8 one day earlier in every Cross-subject cell. Major work stated two ways: about 101 of 160 (63 percent) strictly, about 130 (81 percent) by the guide's rule; optional lessons cut for the day budget, not the line. For the lead item 2 rewritten as settled |
| Expert | 2 | Applied | Money (4.MD.A.2 in full): unit 4 base 3.18 writes cents as hundredths of a dollar after a coin readiness check; unit 6 adds money problems in dollars and cents to base 5.10 and 5.13; source-map notes say so, with the year review (7 to 6) as the fallback day. Progression: m2-money now also hands on to m4-decimal-notation (both rows) |
| Expert | 3 | Applied | Supply header rewritten; 4.MD.A.2 row says math keeps the base text's order and social studies unit 1 keeps its routine. Replacement text for the science and social studies frames: Cross-subject notes below |
| Expert | 4 | Applied | Base 9.7 keeps its comparison work; its country cost tables become prices of school items in two named towns |
| Expert | 5 | Applied | A merge rule under the source map for every merged day (one warm-up, the first lesson's main activity short, the second lesson's activities, about 45 minutes of activity, one synthesis, our exit question, dropped activities named in the day-level map) |
| Expert | 6 | Applied | 4.9.10 to 12: decision "cut", warm-up routines |
| Expert | settled | Applied | All six rows |
| Codex | 1 | Applied | Unit 6: before unit 7, known facts, repeated addition and break-apart strategies; conversions by 12 and 16 (base 5.11) with small amounts and the method shown; place value for 10, 100, 1,000. m4-unit-conversion notes match |
| Codex | 2 | Applied in part | Its selections written into the 7.1 and 2, 7.3 and 4, 9.1 and 2, 9.7 and 8 rows, under the expert's rule. Its 7.14 and 7.15 selection rejected: the expert un-merged that pair |
| Codex | 3 | Applied | Science bridges taken from the science frame as it stands: weathering in whole centimetres and equal cupfuls, no conversion; waves name peak, trough and peak-to-peak distance only; the code rule stated and followed (science unit 3 before math unit 7); the budget two steps of whole-number adding and subtracting |
| Codex | 4 | Applied | "outright" now "predominantly major" (unit 7 holds four patterns lessons); the time sentence now says grade 3 facts from the start and the grade 4 algorithm in warm-ups after unit 5, the share to be checked in minutes; day counts marked provisional |
| Codex | 5 | Applied | Same as expert 6 |
| Codex | 6 | For the lead | Headers in `docs/courses/math-4-spine.md` and `docs/courses/math-4/`: outside this pass's files, and closed to this pass by its blind rule, so not checked here |
| Codex | 7 | For the lead | `docs/RUBRIC-MATH-K8.md` status cells: outside this pass's files |
| Codex | 8 | For the lead | Superseded note on `frame-math-grade-4-codex-2026-11-14.md`: outside this pass's files |
| Codex | settled | Applied | Nine units and order kept; patterns stay in unit 7; inclusive trapezoid kept; merge selections as above |
| Writer | lead 2 | Settled | By expert 1 |
| Writer | lead 5 | Applied | m4-patterns notes now say base unit 6 section A (Curio Class unit 7), base 1.3 a first look only. This wording ("IM grade 4 units 1 and 6") is the likely source of the science frame's base-unit-1 claim |
| Writer | lead 1, 3, 4 | Kept | Time a day (for Cory); unit edges on section lines; base unit 9 as year review |

Counts: applied 6 expert + 4 Codex in full and 1 in part; rejected 0 (one part of Codex 2); for the lead 3; for Cory 1.

## Grade 5

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, example changed | Brackets added to base 1.10 and braces to base 2.13, one check 1 item on each; unit 1, unit 3 and both source-map rows say so. The expert's example, 2 x [3 x (4 + 1)], nests grouping symbols, which the m5-expressions row and the Progressions (OA PDF 47 (41)) rule out for grade 5 ("exploratory, no nested grouping symbols"). The example is now [4 x 3] x 5 + 2 x (3 x 5): one symbol to a group, never nested. An item-level choice; the settlement is kept |
| Expert | 2 | Applied | Header (three rows record science leans; the frames are written, the bridges are theirs); grams on one scale with no conversion; 5.NBT.A.2 bridge taken from the science frame as it now reads (light-travel time and a scale model, no number over 1,000,000), which has changed since the expert read; For the lead item 4 settled, no fallback |
| Expert | 3 | Applied | 8 of 10 units mainly major (80 percent); unit 8 about half; days about 133 to 137 of 160, provisional until minutes |
| Expert | 4 | Applied | Merge rule under the source map; routines row "cut" |
| Expert | settled | Applied | All five rows |
| Codex | 1 | Applied | Multiplication day: lesson 1's first activity short, lesson 2's two activities (the worked method and the errors with zeros, which Codex names as the pair's point; its own pick kept only lesson 2's first); volume day: lesson 7's first activity, lesson 8's two |
| Codex | 2 | Applied | Unit 1 practices MP7 and MP5 (choosing cubes, a drawing or an expression and checking another way); MP2 stays in units 2 and 9; the Practices bullet lists all eight |
| Codex | 3 | Applied | Math content reviewer sentence (FOUNDATION 7.3), in all three grades |
| Codex | 4 | Applied in part | Every "Check set adds" pointer now matches its rows' notes in the rows' convention (compiled edition, PDF page (printed page)): units 1 to 10. Rejected: citing the standalone 2015 draft, since the rows and frames use one edition. Grades 3 and 4 pointers checked: they already match |
| Codex | 5 | Applied | Same as expert 2; science unit 6 line-plot bridge and science unit 4 bar-graph bridge quoted from the science frame |
| Codex | 6 | Applied | Same as expert 4 |
| Codex | 7, 8 | For the lead | `docs/RUBRIC-MATH-K8.md`: outside this pass's files |
| Codex | settled | Applied | Ten units, 160 days, unit 9's unlike denominators, MP5, review selections, cut routines, science bridges |
| Writer | lead 4 | Settled | The late coordinate plane stays (the base text's order); science grade 5 bridges its unit 4 with bar graphs and social studies grade 5 needs no grid |
| Writer | lead 1, 2, 3 | Kept | Time a day (for Cory); edges on section lines; base unit 8 as year review |
| Writer | lead 5 | Updated | Names the m5-expressions notes change |

Counts: applied 4 expert + 4 Codex in full and 1 in part; rejected 0 (one part of Codex 4); for the lead 2; for Cory 2.

## Progression changes (data/progressions/math.csv, 8 rows)

| Row | Change |
|---|---|
| m3-round | Notes: three-digit numbers to the ten also taught and checked (IM 3.15); optional 3.21 cut |
| m3-arithmetic-patterns | Notes: addition-table patterns in IM unit 3 (lessons 2, 5), multiplication table in unit 4 (lesson 9) |
| m2-money | hands_on adds m4-decimal-notation |
| m4-decimal-notation | assumes adds m2-money; notes: IM 3.18 writes cents as hundredths after a coin readiness check |
| m4-measurement-problems | Notes: Curio Class adds money contexts in decimal notation to IM 5.10 and 5.13 |
| m4-unit-conversion | Notes: conversions by 12 and 16 (IM 5.11) use facts, repeated addition and break-apart strategies before unit 7 |
| m4-patterns | Notes: IM grade 4 unit 6 section A (Curio Class unit 7); 1.3 a first look only |
| m5-expressions | Notes: brackets (1.10) and braces (2.13) added, never nested |

Grade 2 frame, Seams section: the threads-that-skip sentence now says m2-money hands on to m4-decimal-notation and
m4-measurement-problems; the grade 3 frame's skip line says the same. Grade 6 frame: not edited; no handoff with
grade 6 changed.

## Cross-subject notes (for the other subjects' fixers; no other frame was edited)

- **Science grade 4.** The 4.OA.C.5 row already names math grade 4 unit 7; that is the right Curio Class unit
  (base unit 6 section A; base unit 1 touches it in lesson 1.3 only, and the m4-patterns notes no longer say "units
  1 and 6"). After this pass the math days are one earlier from unit 3 on: unit 6 about days 77 to 95, unit 7 96 to
  110, unit 8 113 to 127, unit 9 128 to 149. The science Cross-subject cells (78 to 96, 97 to 111, 114 to 128, 129 to
  149) can take those numbers; every bridge stands.
- **Social studies grade 4.** For the lead item 3, replacement: "The math frame keeps 4.MD.A.2 in its unit 6 (about
  days 77 to 95), the base text's order; unit 1's routine stays." Cross-subject rows: "the grade 4 math scope on file"
  becomes "math grade 4 unit 6 (about days 77 to 95)" for 4.MD.A.2 and "math grade 4 unit 5 (about days 58 to 76)"
  for 4.NBT.B.4.
- **Science grade 5.** m5-decimal-operations records a 5-PS1-2 lean (decimal masses); the science frame weighs in
  whole grams and lists no such need. Its fixer may add a "not needed" row; nothing fails without it.
- **Science grade 3, social studies grades 3 and 5, ELA grades 3 to 5:** the math frames now match them; no change
  needed.

## For the lead (outside this pass's files)

- `docs/RUBRIC-MATH-K8.md`, Gateway 2 practices row (Codex grade 5, 7): "Practices are named in the current frames and
  the grade 4 worked unit. Each course's scope and sequence must show all eight through named tasks; frame
  assignments alone do not establish coverage." Teacher-supports row (Codex grade 5, 8): "The shared and math
  approaches are written, with sources. Course materials must show how they carry them out." Status cells (Codex
  grade 4, 7): mark the gaps as found on 2026-11-11 and give each its own current status.
- `docs/courses/math-4-spine.md` and `docs/courses/math-4/` headers (Codex grade 4, 6): Codex's replacement text is in
  its report; this pass could not open those files.
- `docs/reviews/frame-math-grade-4-codex-2026-11-14.md` (Codex grade 4, 8), and the grade 3 and 5 ones: a line that
  the rerun supersedes them.
- Source list (Codex grades 3, 4, 5): the standalone NBT 2015 and NF 2018 drafts as fallbacks for the compiled
  Progressions, labelled so their pages are never mixed with the compiled edition's.

## For Cory

- **Time a day (audience).** Grades 3 to 5 math at 60 minutes, five days a week, 160 days. A 45-minute block needs
  about one third more periods, or a separate path with a quarter fewer minutes.
- **Math content reviewer (people, money).** FOUNDATION 7.3 asks one to read every check item and key before a math
  course is called finished: who, and any pay.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Addition-table patterns begin in unit 3 (base 3.2, 3.5); unit 4 finishes 3.OA.D.9 | 3 | Where the base text teaches them |
| Rounding includes three-digit numbers to the ten, taught and checked | 3 | 3.NBT.A.1 in full |
| Facts practice starts in unit 1 with understood facts; unit 4 owns the strategies | 3 | Spaced practice all year; the row names units 1 and 3 |
| Unit 7 carries MP2 (base 6.12); grade 5 unit 1 carries MP5; all eight practices placed in each grade | 3, 5 | Every practice has a home |
| Merge rule: one warm-up, the first lesson's main activity short, the second's activities, about 45 minutes, one synthesis; dropped activities named in the day-level map | 3, 4, 5 | Two 60-minute lessons in one day |
| Warm-up routines from the last base unit: decision "cut" | 3, 4, 5 | "split" means a unit split |
| Science and social studies bridges quoted from their frames; the supply tables say those frames are written | 3, 4, 5 | One bridge per need; no math ahead of math |
| Grade 4: 7.14 and 7.15 a day each; 2.1 and 2.2 one readiness day (unit 2 17 days, unit 9 22) | 4 | 4.MD.C.7 in full; the merged pair reviews grade 3 |
| Grade 4 major work: about 63 percent strictly, about 81 by the guide's rule | 4 | The guide counts supporting work tied to major work |
| Money as cents in hundredths (base 3.18) and dollars-and-cents problems added to base 5.10 and 5.13; m2-money hands on to m4-decimal-notation | 4 | 4.MD.A.2 names money; the base text has none in its unit 5 |
| Conversions by 12 and 16 before unit 7 by facts, repeated addition and break-apart | 4 | Base 5.11 is kept |
| Base 9.7's country cost tables replaced with school-item prices | 4 | The frame's money-context rule |
| Brackets in base 1.10, braces in base 2.13, one check 1 item each, never nested | 5 | 5.OA.A.1 in full within the Progressions' no-nesting limit |
| Grade 5 major work by units 8 of 10 | 5 | Unit 8 is about half supporting |
| Coordinate plane stays in unit 10; no fallback | 5 | Science bridges with bar graphs |
| Check-set pointers follow the rows' notes (compiled Progressions, PDF (printed)) | 5 | One edition, one convention |
| A qualified math content reviewer reads every check item and key before a course is finished | 3, 4, 5 | FOUNDATION 7.3 |
| Inclusive trapezoid definition, grades 3 to 5 | 3, 4, 5 | The base text's own, named in grade 5 lesson 7.5 |
