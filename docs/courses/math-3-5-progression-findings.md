# Mathematics, grades 3 to 5 progression: findings

Moved out of `docs/courses/math-3-5-progression.md` on 2026-11-11, after the curriculum expert's cold read (`docs/reviews/math-3-5-progression-2026-11-11.md`). This is a one-time list of what the first draft of the progression found wrong, missing or undecided in the grade 4 spine and the data files. Unit writers do not need it; the progression page carries what they need.

**Changes from the first draft's list.** D1 and D2 are dropped (duplicates of A2 and A3). The evidence for A9, D4 and E1 and the pointer in E3 are corrected as the review says. A5 gains 2.MD.A.2. Each finding now has the expert's judgment and a status.

**Status words.**

- **applied to the spine 2026-11-11**: the pointer is corrected in `docs/courses/math-4-spine.md`. No day, order or unit changed.
- **open: data/modules.csv**: not yet edited; someone else holds that file and `data/modules.csv`.
- **with Cory**: it changes what the course teaches. The expert's recommendation is written into the progression page, marked "Proposed, waiting for Cory's yes".
- **applied in the progression 2026-11-11**: a note that needed only the progression page.

Page pointers: "Prog. p. 149 (143)" is page 149 of the Progressions PDF, printed page 143. "Std. p. 24" is a page of the official standards PDF.

## (a) Spine builds-on or sets-up entries that were wrong, missing or vague

| # | Where | What | Evidence | Fix | Expert's judgment | Status |
|---|---|---|---|---|---|---|
| A1 | Stretch 4 | Missed 3.NF.A.3c. | Mixed numbers rest on whole numbers as fractions (Prog. p. 151 (145)). | Add 3.NF.A.3c. | Right. The page says it in terms. Also: turning a mixed number into a fraction is addition, not a separate rule (same page). | applied to the spine 2026-11-11 |
| A2 | Stretch 7 | Listed 3.NF.A.2, A.3 and stretch 3. Missed stretch 4. | 4.NF.C.5 adds fractions. | Add stretch 4; say grade 3 gives no tenths or hundredths. | Right. | applied to the spine 2026-11-11 |
| A3 | Stretch 8 | Listed only 3.NBT.A.1, A.3. | Reading, writing, comparing are 2.NBT.A.1 to A.4. | Add the grade 2 codes. | Right. | applied to the spine 2026-11-11 |
| A4 | Stretch 13 | Unit 13.3 "What the remainder means" was coded 4.NBT.B.6 only. | Interpreting remainders is 4.OA.A.3 (Prog. p. 45 (39)). | Add 4.OA.A.3 to the unit; keep its aim. | Right. Prefer adding the code over moving the aim. | applied to the spine 2026-11-11 (`data/units.csv` has no standards column, so its row is unchanged) |
| A5 | Stretch 15 | Listed 3.MD.A.1, A.2 only. | Length units and money are grade 2 (2.MD.A.1 to A.4, C.8); unit size against count is 2.MD.A.2 (Prog. p. 103 (97)). | Add them; mark km, lb, oz, ml, sec as new. | Right. Add 2.MD.A.2. | applied to the spine 2026-11-11 |
| A6 | Stretch 1, sets up | "Grade 5 expressions" was not supported. | 5.OA.A.1, A.2 do not use factors. Real uses: 5.NF.A.1, 5.NBT.A.2. | Replace. | Right. The link to 5.NBT.A.2 is thin; 5.NF.A.1 is the real one. | applied to the spine 2026-11-11 |
| A7 | Stretch 10, sets up | "Grade 5 and 6 ratio thinking" was vague. | Grade 5 uses are 5.NF.B.5 and 5.OA.A.2 (Prog. p. 48 (42)). | Name the codes. | Right. | applied to the spine 2026-11-11 |
| A8 | Stretch 16, sets up | "Grade 7 angle problems" skipped nearer uses. | Stretch 17; 5.G.A.1; 5.G.B.3, B.4. | Add them. | Right. | applied to the spine 2026-11-11 |
| A9 | Stretches 12, 13, limits table | "The standard algorithm is grade 5" was too blunt. | Grade 5 requires fluency (5.NBT.B.5). The Progressions show written methods in grade 4 that shorten into the standard algorithm (Prog. pp. 59 to 60 (53 to 54), 70 to 73 (64 to 67)); the overview says the Standards do not fix one written form. The grade 4 opening asks for "efficient procedures" (Std. p. 27). Division fluency is grade 6 (6.NS.B.2). | Reword: fluency with the standard algorithm is grade 5 (multiplying) and grade 6 (dividing); grade 4 written methods shorten into it and must be explained. | Right, slightly overstated in the first draft; evidence reworded here. | applied to the spine 2026-11-11 |

## (b) `data/sequence.csv`, grades 3 to 5 mathematics

The expert opened every line: all fourteen are right, "accurate to the line".

| # | Line | What | Evidence | Fix | Expert's judgment | Status |
|---|---|---|---|---|---|---|
| B1 | 424 | Number patterns builds on meaning-of-multiplication and times-tables only. | 3.OA.D.9 sits in `math-3-patterns-and-two-step-problems`. | Add that module. | Right. The module holds 3.OA.D.8, D.9. | applied to data/sequence.csv 2026-11-11 |
| B2 | 427 | Decimals builds on grade 3 fractions only. | Its real base is 4.NF.A.1 and 4.NF.B.3. | Add the two grade 4 fraction modules, if the file allows same-grade links. | Right. No rule on same-grade links was found; check `scripts/build_site.py` and `scripts/teaching_map.py`, which read the file, before the edit. | applied to data/sequence.csv 2026-11-11 |
| B3 | 430 | Multiplicative comparison misses 3.OA.D.8. | Two-step problems. | Add `math-3-patterns-and-two-step-problems`. | Right. | applied to data/sequence.csv 2026-11-11 |
| B4 | 431 | Conversions builds on scaled graphs and area. | Neither is used. The base is 3.MD.A.1, A.2. | Replace with `math-3-time-volume-and-mass`. | Right. | applied to data/sequence.csv 2026-11-11 |
| B5 | 432 | Area and perimeter formulas builds on scaled graphs and area. | Scaled graphs is not used; perimeter (3.MD.D.8) is missing. | `math-3-area;math-3-perimeter`. | Right. | applied to data/sequence.csv 2026-11-11 |
| B6 | 433 | Multi-digit multiplication and division builds on rounding only. | 3.OA.C.7, 3.OA.B.5, B.6, 3.MD.C.7c (Prog. pp. 70 to 72 (64 to 66)). | Add meaning-of-multiplication, times-tables, area. | Right. | applied to data/sequence.csv 2026-11-11 |
| B7 | 434 | Angles and line plots builds on scaled graphs and area. | Scaled graphs holds 3.MD.B.4, correct for line plots. Area is not used by angles. | Drop area; add `math-3-fractions-as-numbers`. | Right. Scaled graphs stays. | applied to data/sequence.csv 2026-11-11 |
| B8 | 435 | Lines, angles, symmetry builds on area and quadrilaterals. | Area is not used. | Drop area. | Right. | applied to data/sequence.csv 2026-11-11 |
| B9 | 436 | Grade 5 volume builds on conversions and area formulas. | 5.MD.C.5 needs area and multi-digit multiplication, not conversions. | Swap conversions for multi-digit multiplication. | Right. | applied to data/sequence.csv 2026-11-11 |
| B10 | 437 | Fractions as division misses division. | 5.NF.B.3 rests on 4.NBT.B.6 and remainders. | Add multi-digit multiplication and division. | Right. | applied to data/sequence.csv 2026-11-11 |
| B11 | 439 | Expressions builds on factors and number patterns. | 5.OA.A.2 rests on 4.OA.A.1 to A.3 and 4.NBT.B. | Replace with multiplicative comparison and multi-digit operations. | Right. | applied to data/sequence.csv 2026-11-11 |
| B12 | 440, 441 | Both miss grade 4 decimals; 441 misses multi-digit multiplication and division. | 5.NBT.A.3, B.5 to B.7. | Add them. | Right. | applied to data/sequence.csv 2026-11-11 |
| B13 | 443 | Units and line plots builds on conversions and area formulas. | 5.MD.B.2 rests on 4.MD.B.4 and 4.NF.B. | Swap area formulas for angles-and-line-plots and adding-and-multiplying-fractions. | Right. Keep conversions (5.MD.A.1 needs them); swap only area formulas. | applied to data/sequence.csv 2026-11-11 |
| B14 | 445 | Grade 5 patterns lists factors and multiples. | 5.OA.B.3 needs only 4.OA.C.5. | Drop it. | Right. | applied to data/sequence.csv 2026-11-11 |

**Three side notes, `data/modules.csv`.** The expert judged all three right. Status of each: open: data/modules.csv (they wait with that edit; the file to change is `data/modules.csv`).

1. The conversions description mentions area and perimeter formulas; those are in the next module.
2. The grade 3 quadrilaterals description says "partition into equal areas", though 3.G.A.2 sits in the area module.
3. `math-5-multiplying-and-dividing-fractions` holds no division standard: it holds only 5.NF.B.4 to B.6, and 5.NF.B.7 is in fractions-as-division.

## (c) Order: something asked for before it is taught

| # | Where | What | Evidence | Fix | Expert's judgment | Status |
|---|---|---|---|---|---|---|
| C1 | Stretch 11 (day 89) before stretches 12 and 13 (days 94, 106) | The pilot unit applies area formulas before multi-digit multiplication and division exist. | Prog. p. 112 (106) says the numbers in grade 4 area problems "can now be any of the numbers used in Grade 4". | First draft: keep the pilot's numbers inside grade 3 range and bring area back with larger numbers in stretches 12 to 14, or move it. | Right, and the evidence is weaker than the first draft said. "Can" is permission; the margin codes on that page are 4.NBT.4, 4.NF.3d and 4.OA.4, and its examples are small. Recommendation: keep day 89, limit the numbers on days 89 to 93, and make sure area with larger sides returns in units 12 and 13 and in stretch 14. A course whose only 4.MD.A.3 items have grade 3 numbers would be marked down, so the return must not be lost. Likely. | with Cory (rule written in the progression, stretch 11) |
| C2 | Stretch 10 (day 80) | Takes part of 4.OA.A.3 before remainders. | The spine already holds remainders to stretch 14. | None needed; unit plans keep remainders out of stretch 10. | Right. | applied in the progression 2026-11-11 (stretch 10 limits) |

## (d) Grade 3 expectations assumed that are not grade 3 standards

| # | Where | What | Evidence | Fix | Expert's judgment | Status |
|---|---|---|---|---|---|---|
| D3 | Stretch 16 | Fraction of a turn rests on 3.NF.A.1, but circles cut into equal shares is 2.G.A.3; grade 3 never asks for it by name. | Standards file. | The readiness check should test it, not assume it. | Right. Also 1.G.A.3. | applied in the progression 2026-11-11 (stretch 16 readiness item 2) |
| D4 | Fluency plan, "times tables from day 1, grade 3 maintenance" | Right code, but fact fluency is not safe to assume. | The Progressions say reaching fact fluency may take much time and that extra time and support are essential where needed (Prog. p. 37 (31)). | Treat the first weeks as a check, not only upkeep. | Right; the first draft quoted the wrong words, corrected here. Recommendation: keep the label "grade 3 maintenance" and add a facts check in days 1 to 6, repeated before day 94, with help in warm-ups and not in lesson days. Firm. | with Cory (written in the progression, fluency section) |

## (e) Grade 4 units that may teach past the grade's limit

| # | Where | What | Evidence | Fix | Expert's judgment | Status |
|---|---|---|---|---|---|---|
| E1 | Stretch 15, and stretch 7's "comes back" | Money and metric problems with decimals can slide into decimal arithmetic. | 4.MD.A.2 allows "simple fractions or decimals", but no grade 4 standard computes with decimals; that is 5.NBT.B.7. Prog. p. 89 (83) says, of grade 4 measurement data, that decimal computations "are not expected until Grade 5". It is a general statement, which makes this finding stronger. | Unit plans: decimals may be read, compared and renamed in a smaller unit; sums are done in the smaller unit or as fractions. | Right. Recommendation: a five-point rule a unit writer can follow. Firm. | with Cory (rule written in the progression, stretch 7; it also governs stretch 15 and the limits table) |
| E2 | Unit 8.3, rounding to any place, 3 days | The standard says "to any place"; the Progressions say rounding beyond the leftmost one or two places "need not be practiced" (Prog. p. 69 (63), margin). | Same. | First draft: consider 2 days and give the day to stretch 13. | Right. Recommendation: keep three days and re-aim the third at estimating and checking sums and differences. The first draft's option is also defensible. Judgment call. | with Cory (written in the progression, stretch 8) |
| E3 | Stretch 17 | Triangle sorting by sides and angles is in the Progressions (Prog. p. 132 (126)), not the standard. | 4.G.A.2. | Keep it out of checks. | Right; pointer corrected to p. 132 (126). | applied in the progression 2026-11-11 (stretch 17 limits) |
| E4 | Stretch 14 | No stated cap on steps. | Prog. p. 44 (38): no more than three. | State the cap in the limits table. | Right. | applied to the spine 2026-11-11 |

## One more point the review raised

The review's finding 1 (the stretch 16 angle limit: grade 4 does find angles on a straight line and where two lines cross) is applied in the progression page. The review lists it, with C1, D4, E1 and E2, among the items that change what the course teaches and should go to the Review Desk. It is not one of the four marked "with Cory" above, and the spine is unchanged on that point.
