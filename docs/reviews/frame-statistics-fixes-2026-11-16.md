# Fixes: course frame, Statistics (2026-11-16)

The fix pass on docs/reviews/frame-statistics-2026-11-16.md (12 findings, 2 serious). Files changed: docs/courses/statistics/frame.md, the stat- rows of data/progressions/math.csv (notes only), the CUR-ST lines of data/standards/curio-math-electives.txt, and the frame.py sync outputs.

## Findings

| # | Finding | Fixed how, or why not |
|---|---|---|
| 1 | Six base labs kept unchanged collect personal data | Fixed. 2.8, 7.4, 9.6, 10.5, 11.7 and 11.8 are now "split", each on its own Source map row with the expert's note (11.8 uses the supplied census microdata sample), and the map's opening paragraph says no lab collects students' own money, possessions, home language, gender, body or home location. |
| 2 | Inference on population tables and a complex survey as if they were simple random samples | Fixed. The Real data bullet now says every procedure runs on a real random sample or randomised experiment. Unit 7 uses a supplied simple random sample of about 200 person records from the census bureau's public-use microdata, with the published state percent kept as the known value. The seat-belt survey's published margin is read beside a supplied simple random sample from one site list, with a fallback to reading its margin only. Unit 7 also teaches why a clustered or weighted survey's margin differs from the simple formula. Unit 9 uses a supplied sample of about 400 worker records for homogeneity (by region) and independence (one sample). The microdata source is For the lead 3. |
| 3 | The central limit theorem shown on too skewed a population | Fixed (settled 1). The unit 6 cell and the Real data bullet show the theorem on the uniform parent and Old Faithful's intervals; the county populations are the counter-case for "large enough depends on the shape". |
| 4 | The investigation's inference may rest on a convenience sample; ruler drop clashes with the body rule | Fixed. The Investigation bullet and the unit 10 cell allow two plan kinds: a randomised class experiment (conclusion about these students) or a random sample from public data. The report states its scope of inference. Ruler drop is replaced by recall of a list after one of two study methods, and students never measure or share their bodies. |
| 5 | Owned outcomes thinner than the rows | Fixed. The changes in curio-math-electives.txt (CUR-ST lines only, small edits): CUR-ST.2 adds "display" with its four plots; CUR-ST.3 adds density curves; CUR-ST.13 adds what a p-value does not tell and statistical against practical significance; CUR-ST.15 adds what each design lets you conclude; CUR-ST.16, 18 and 20 add interpretation in context; CUR-ST.18 adds how the test and the interval agree. Matching clauses were added to the notes of stat-quantitative-distributions, stat-position-normal, stat-test-proportion, stat-one-mean, stat-two-means and stat-regression-inference (stat-two-proportions already had its clause). The header's version line is shared with the other two courses and is left for the lead (For the lead 6). |
| 6 | Units 4 and 6 tight; unit 1's review understated | Fixed as the expert proposed. Unit 1 goes from 19 to 17 days and unit 6 from 9 to 11. Row loads: stat-quantitative-distributions about 6 (2.5 review), stat-position-normal about 6 (1 review), stat-sampling-distributions about 11. The unit 4 cell names its about 4 new days. The unit 1 cell and the Days bullet give the review counts the rows carry (about 5.5 in unit 1, about 12 in all). |
| 7 | Chemistry's rate data do not suit a linear slope test | Fixed. In unit 9 the rate data are logged, as in unit 2, and used as a conditions case. Old Faithful is the main slope case, with its non-independence named as a limit. The Cross-subject lean (HS-PS1-5) stays. |
| 8 | Unit 8's data picks are weak | Fixed (settled 5 and 6). Coin masses come from a supplied published set or a 0.01 gram scale, 1982 excluded, and are used first for intervals and as the case whose test answer is known. Paired data are station annual means (or 30-year normals) at stations drawn at random. Two random samples of station means from two regions give the case whose answer is not known in advance. |
| 9 | The Source map's opening names two moves; there are four | Fixed with the expert's replacement text. |
| 10 | The week line leaves out the held investigation days | Fixed. The weeks are recounted in teaching order with the held days and unit 1's new 17 days. Check 1 is now weeks 9 to 10, Check 2 weeks 18 to 19 and Check 3 weeks 30 to 31. |
| 11 | Three frames propose different replacements for shared stale lines | Done as the coordinator directed. The competing replacement texts are removed from For the lead (items 1 and 2 now point at the lead's single shared fix). docs/RUBRIC-MATH-HS.md, docs/agents/lenses/math.md and docs/sources/BASE-TEXTS.md are not edited. |
| 12 | Two small wording faults | Fixed. Unit 4's reason now reads "met in unit 3's random selection and Algebra II's re-randomisation"; unit 1's review count is corrected (finding 6). |

## Settled by the expert, applied

All seven are applied:
1. The central limit theorem demonstration (finding 3).
2. Unit 3 is stratified by the four census regions, one printed copy per group.
3. The paper path names a scientific calculator with a statistics mode, plus a printed binomial table.
4. The unit 9 extension on Mendel's too-good fit.
5. Unit 8's paired station means.
6. Unit 8's coin masses and an open two-sample case.
7. The unit 4 wording.

## Also done

- **Re-entry wording (former For the lead 1, decided yes).** The stat- rows whose assumed row was used in grade 11, directly or one hop, or renewed earlier in this course, now say "Re-entry: a retrieval task inside a day on <row> (<why>)": stat-quantitative-distributions, stat-position-normal, stat-correlation-regression, stat-residuals-transformations, stat-sampling-design, stat-experimental-design, stat-random-variables, stat-sampling-distributions, stat-test-proportion, stat-two-means, stat-chi-square, stat-regression-inference. stat-probability-rules now names its readiness check (geo-conditional-independence, geo-addition-rule) and its retrieval task (geo-sample-spaces-events). stat-categorical-data keeps its readiness check (alg1-two-way-tables, last used in grade 10).
- **L49 shared answer (coordinator addendum).** The Standard and Focus bullets apply the owned-outcome account in place of focus 1a to 1c, plus a minutes line. Review, retrieval and readiness time is counted in minutes in the scope and sequence and capped at 10 percent of instructional minutes; the cap is an item-level choice, and the rows plan about 8 percent. The modeling cycle stays whole (gap 2's record). 1c reads as work at the course's stated level, first-year college.

## Gates after the fixes

- `python -X utf8 scripts/frame.py check statistics`: 0 failures (10 units, 160 days, 151 in units, 9 for checks and respond days).
- `python -X utf8 scripts/stale.py check`: 0 failures.
- `python -X utf8 scripts/progression.py check math`: 382 rows, 1 failure, "CUR-PC.16 named by no skill". That is the Precalculus writer's work in progress, not a stat- row.
- `python -X utf8 scripts/frame.py sync`: run.
- Scratchpad self-check: all 22 stat- rows placed once, Owned standards match the rows, each unit's days equal its rows' loads, and 151 + 9 = 160.

## Unit-level lessons pass (2026-11-16)

frame-write.md lessons 17 to 32 applied to docs/courses/statistics/frame.md. No unit, skill placement, day total or owned standard changed.

- 17 Day kinds: new **Day kinds.** bullet; Fluency is small (summaries and z-scores, the probability rules, the four-move write-up); a simulation that first shows an idea is Understanding.
- 18 Readiness evidence: the Seams table's third column gives each row's treatment and last use (grade, core course, unit, day) from the core days.csv files; all treatments held. The Readiness bullet names the counting grade (12) and what grade 11 changes (nothing, since it needs the accelerated path).
- 19 Scored evidence: new **End-of-unit evidence.** bullet; unit 5 (11 codes) sits twice; the investigation's days are laid out: plan drafted, written feedback, plan revised (days 47 and 48); report drafted (day 154), written feedback, revised and scored (day 156), presentations a third of the class a day (days 157 to 159), respond day (day 160).
- 20 Checks: the three "What it checks" cells name the units sampled, the two task forms and the record reused unscored; the code lists ("S-MD.A.1 to S-MD.B.7 ... each sampled") are gone.
- 21 Inside the period: the Days bullet names collection and a 5-minute kit count on hands-on days.
- 22 Safety: not applicable (math; dice, cards, coins and a scale only).
- 23 Facts sourced: the Real data bullet names every set's free source and "as of" year (Census Bureau, National Park Service, NOAA, the fuel economy data, Azzalini and Bowman 1990, Ezekiel 1930, Francis and colleagues 1955, Mendel 1866, the highway safety agency's seat-belt survey, the climate normals); insurance, screening, goalie and reaction-rate values are labelled invented for practice; the genetics ratios are labelled expected values; the coin set falls back to a labelled invented set only where there is no scale.
- 24 Depth and devices: an "Out:" line in every unit; new **Devices.** bullet (statistics-mode calculator set, devices in pairs; no owned code needs a device, each met in full on paper).
- 25 Tools, texts and costs: each unit's last column names tools and jobs, what Curio Class writes, and a provisional cost for 30 (printing, the dice and card kit, coins, scales, poster paper); ceiling For the lead 8.
- 26 Side standards: WHST.11-12.2 and WHST.11-12.7 practised, not owned.
- 27 Source map: the lesson 27 paragraph added at its head.
- 28 Focus method: the shared method in the same words as Precalculus and Calculus; the cap is now 15 percent (was 10), the plan about 13 percent counted the shared way; For the lead 9.
- 29 Labels: unchanged.
- 30 Sensitivity by unit: the Sensitivity reads bullet now matches each unit's days (health units 3 and 5, money unit 5, microdata income fields dropped in units 7 and 9, identity units 7 and 9, road safety unit 7); units 7 and 8 are no longer listed as health.
- 31 Grade 12 calendar: new bullet: Check 3 then the investigation close the year; five folds in order; For the lead 8.
- 32 Core leans only: unchanged (no lean on another elective).

Gates: frame.py check statistics 0 failures; progression.py check math 382 rows, 0 failures; stale.py check 0 failures.
