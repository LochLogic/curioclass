# Rule 2 readiness fixes, 2026-11-15

Scope: the READINESS-MISSING and WRONG-KIND gaps in science, ELA and math scopes that showed after today's skeleton fix (`scripts/unit_skeleton.py` now treats an earlier-grade row in a unit's skills column as an earlier row of that unit). Only `data/plans/<course>/days.csv` was edited, in 14 courses. No day added, no check moved, no day count changed. Social studies data untouched. Pattern and counting follow `rule2-gaps-fixes-2026-11-15.md`.

## Summary

| Subject | ready_missing rows (units) | wrong_kind | retr_unnamed |
|---|---|---|---|
| science | 35 (17) to 0 (0) | 1 to 0 | 0 to 0 |
| ELA | 2 (1) to 0 (0) | 0 to 0 | 0 to 0 |
| math | 28 (16) to 0 (0) | 3 to 0 | 3 to 2 |

ELA's 6 collect lines are the three justified pairs, left as they were. `sequence.py check` now prints rule 2 notes only for social studies courses.

## Most gaps were the next unit's check, counted in the wrong unit (60 of 65 rows)

The readiness check for unit N+1 sits on unit N's last day (a respond day, `assess` = `readiness`), and those days listed the checked rows in their skills column. Since today's skeleton fix, an earlier-grade row in a unit's skills is an earlier row of that unit. So each row unit N+1 checks was being read as a row unit N assumes, and unit N was asked for its own readiness check on it. A readiness day is never a use (`used_on`), so the ids taught nothing there.

Fix in every case below: the ids leave the readiness day's skills column and stay named by id in its note, which is where the skeleton and `sequence.py` look for a readiness check. Where the note named the rows only in words, the ids were added in the "unit N's readiness check on <ids> (last used grade N)" form. No check lost a row.

- biology: day 25 (unit 3's check: s7-reactions-atoms, s7-food-molecules; note now names the ids); day 112 (unit 8: s6-plate-evidence; ids added, "explicitly retrieved in grade 7 day 143" replaced with "last used grade 7"); day 123 (unit 9: s7-biodiversity-solutions, s7-human-impact-design; ids added); day 140 (unit 10: s7-population-consumption; id added).
- physics: days 30 (unit 3: s8-electromagnetic-forces, s8-fields, s8-gravity-mass, s8-gravity-solar-system), 46 (unit 4: s8-kinetic-energy-graphs, s8-potential-energy), 76 (unit 6: s8-wave-amplitude-energy, s6-digital-signals, s6-light-paths), 92 (unit 7: bio-sources-of-variation), 127 (unit 9: s6-surface-change-scales, s6-plate-evidence), 145 (unit 10: s6-geologic-time). Notes already named the ids.
- science-grade-7: day 41 (unit 3's check on s5-identify-materials, s5-new-substances; day 41 is unit 2's end day and keeps `end`). Note unchanged.
- science-grade-8: days 26 (s4-wave-model, s6-light-paths), 46 (s3-magnet-static, s5-gravity-down, and s4-energy-device, which the note retrieves for unit 3), 104 (s3-inherited-traits, s3-environment-traits), 131 (s3-fossils, s3-variation-advantage, s3-habitat-survival, s3-animal-groups, s6-geologic-time). Notes unchanged.
- english-language-arts-grade-9: day 50 (unit 3: e4-grammar, e6-pronouns). Note's "last explicitly taught grade 4 / grade 6" now reads "last used grade 5 / grade 7", the counted last use.
- algebra-i: day 17 (unit 2: m7-two-step-inequalities), day 83 (unit 5: m7-percent-problems); notes reworded to "Unit N's readiness check on <id> (last used grade 7)".
- algebra-ii: day 14 (unit 2: six alg1 rows), day 45 (unit 3: alg1-inverse-functions, alg1-rational-irrational, alg1-quadratic-formula, m8-integer-exponents; the two unflagged rows were moved too so the day reads one way), day 95 (unit 5: alg1-scatter-linear-models, alg1-quadratic-patterns), day 136 (unit 7: alg1-data-displays, alg1-center-spread, alg1-correlation-causation, m7-random-samples).
- geometry: day 26 (unit 2: m8-congruence, m8-volume-curved), day 81 (unit 5: m7-cross-sections, m7-circles, m8-volume-curved; m7-circles and the second m8-volume-curved also moved for consistency), day 143 (see wrong kind below).
- math-grade-4: day 44 (unit 4: m2-money), day 76 (unit 6: m2-unit-size); notes now name the ids.
- math-grade-6: day 141 (unit 8: m3-scaled-graphs); note reworded.
- math-grade-7: day 68 (unit 5; see wrong kind below).
- math-grade-8: day 92 (unit 6: m6-exponents); note reworded to "last used grade 6".

## Real readiness gaps (5 rows, readiness or note added)

- science-grade-3, unit 1: sk-weather-watch (last used grade 1) is taught on day 2. Added to day 1's existing readiness check, note only.
- science-grade-6, unit 1: s4-senses-brain (last used grade 4) is rebuilt on day 13, and unit 1 had no readiness check. Day 1 now carries `assess` = `readiness` with "Last ten minutes, after the hook: unit 1's readiness check on s4-senses-brain ...". Day 13's note says its support is shaped by day 1's check results (worded without "readiness" so day 13 stays a teaching use for unit 6's retrieval).
- algebra-ii, unit 2: alg1-exponential-functions (last used grade 9) is retrieved in unit 2's openings (days 15 to 19, 23). Unit 1 lists it on days 2 to 10, but only as warm-up retrieval, which is not a use, so day 1's check does not carry to unit 2. Added to day 14's readiness note.
- algebra-ii, unit 3: alg1-quadratic-equations-reasoning (last used grade 9) is in unit 3's openings; unit 2 only retrieved it. Day 45's note no longer says "do not check those again"; it now checks this row (factoring still not rechecked).
- math-grade-7, unit 7: m4-angle-concepts (last used grade 4). Days 2 and 3 list it only with retrieval notes, so it is idle since grade 4. Added to day 120's readiness check (skills and note); day 121's opening now rebuilds it from day 120 results and still retrieves m4-protractor.

## Wrong kind (4 rows, readiness row moved to retrieval)

- science-grade-3, unit 4: s1-parent-offspring was used in grade 2 (one-hop), so it wants retrieval. Day 58 loses the id, its `readiness` assess and its readiness sentences (now a whole-day response; goal no longer says "before unit 4 readiness"). Day 59 no longer uses day 58 readiness for grouping. Day 60 now opens "Retrieval: s1-parent-offspring (last used grade 2)", and the claim that grade 2 did not use this content is gone.
- geometry, unit 8: m7-probability-models was last used in grade 9 (algebra I). Day 143's check now covers only m7-compound-events; day 144 retrieves m7-probability-models and rebuilds m7-compound-events from day 143.
- math-grade-6, unit 7: m4-factors-multiples was used earlier this year (one-hop). It was day 119's only readiness row, so day 119 loses `readiness` and becomes a full check 2 response (50 minutes, or 45 on the short path); goal shortened. Day 136 now opens "Retrieval: m4-factors-multiples (used earlier this year)" with the same 10-minute array rebuild.
- math-grade-7, unit 5: m5-add-sub-unlike was used earlier this year. Day 68's check now covers only m5-fraction-add-sub-problems (last used grade 5); day 71 retrieves m5-add-sub-unlike and rebuilds m5-fraction-add-sub-problems from day 68.

No case was fixed by removing a skill the unit uses.

## For Cory or the lead

- **Skeleton quirk (worth a script fix):** `earlier_rows` reads ids on a readiness day for the next unit as the current unit's earlier rows. 60 of the 65 rows were this. The data fix (ids in the note, not the skills column) is safe and passes, but a future writer who lists checked rows in skills will trigger the same false gap. Either the skeleton should skip ids that a next-unit readiness note names, or the brief should say readiness-check rows go in the note, not the skills column.
- **Double checks:** algebra-ii now checks alg1-exponential-functions on days 1 and 14 and alg1-quadratic-equations-reasoning on days 14 and 45, because warm-up retrieval does not count as a use. The scope says unit 1 "teaches again" exponential functions on days 2 to 10. If that is true teaching, those days' notes would need to stop calling it retrieval and the day 14 addition could go. Same shape for math-grade-7 m4-angle-concepts (days 1 to 3 versus day 120).
- **Scope prose now behind the CSV** (scope docs were out of this job's edit scope): science-grade-3 lines 23 and 73 (day 58 readiness on s1-parent-offspring); math-grade-6 lines 40 and 97 (day 119 readiness); geometry line 26 (m7-probability-models); math-grade-7 lines 41 and 44 (m4-angle-concepts, m5-add-sub-unlike); algebra-ii lines 15 and 23 ("no repeated readiness"); science-grade-6 has no day 1 readiness mention.

## Gates

- `sequence.py check` and `frame.py check` on all 14 touched courses: 0 failures. Frame notes on algebra-ii, math-grade-7 and math-grade-8 were already there before the edits.
- `plan.py check`: 0 failures.
- Unit skeletons regenerated with `--force` for the 14 touched courses; `unit_skeleton.py --self-test` and `day_skeleton.py --self-test` pass.
