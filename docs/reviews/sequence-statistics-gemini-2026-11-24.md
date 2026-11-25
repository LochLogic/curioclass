# Cold read: Statistics scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-statistics-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-statistics-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `statistics` (grade 12, open to grade 11 on the accelerated path, math core elective, full year, 160 course days)
**Subject:** statistics
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/statistics.md`, `docs/agents/lenses/math.md`, `docs/RUBRIC-MATH-HS.md`
- `docs/courses/statistics/frame.md`, `docs/courses/statistics/scope-and-sequence.md`
- `data/plans/statistics/days.csv`, `data/plans/statistics/source-map.csv`
- `data/standards/curio-math-electives.txt` (`CUR-ST.1` to `CUR-ST.21`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I verified all gate subjects directly against `days.csv`, `source-map.csv`, `curio-math-electives.txt`, and `CALENDAR.md`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 10: 17, 13, 13, 9, 19, 11, 24, 19, 13, 13 = 151 unit days, plus 9 `C` days = 160). Unit 10's 13 days are spread cleanly as days 47 to 48, 70 to 71, and 152 to 160.
- **Kinds:** 85 Understanding, 35 Application, 11 Fluency, 16 Check, 13 Respond. Every Fluency day practices only procedures taught on earlier days, introduces no new code, and drafts, revises, or edits no writing.
- **Owned standards:** All 31 owned codes (10 Common Core (+) standards and lettered parts: `S-CP.B.9` and `S-MD.A.1` to `S-MD.B.7` including `5a` and `5b`, plus `CUR-ST.1` to `CUR-ST.21`) are taught before being assessed and appear on an `end` assessment day.
- **Math columns (`tools`, `supplies`, `safety`):** `safety` is blank on every row; `tools` and `supplies` are well-formed lists.
- **Assessments and calendar:** Units 1 to 9 end with a sitting on the second-last day and a Respond day on the last (Unit 5 sits twice, days 69 and 77, with day 69's response in the first 15 minutes of day 72); Unit 10's revised report (day 156) and presentations (days 157 to 159) are its end-of-unit evidence with Respond day 160. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 44 to 45 (weeks 9 to 10, respond day 46), 90 to 91 (weeks 18 to 19, respond day 92), and 149 to 150 (weeks 30 to 31, respond day 151).
- **Readiness and retrieval:** Counted by grade number from grade 12, grade 11 Algebra II rows (and grade 9/10 rows renewed by one hop in Algebra II) open as retrieval; grade 10 rows (`alg1-two-way-tables` via Geometry, `geo-conditional-independence`, `geo-addition-rule`) receive readiness checks in the last ten minutes of day 1 (unit 1, after the hook) and day 46 (Check 1's respond day, 3 days before unit 4 opens on day 49).
- **15 percent earlier-course cap (`RUBRIC-MATH-HS.md`):** Counted at most 1,020 of 7,550 unit minutes (13.5 percent), under the 15 percent cap (1,132.5 minutes).

## Verdict

The Statistics scope and sequence is exceptionally strong on data ethics, honest scope of inference (never feeding non-random listings into sampling formulas), simulation before formulas, and the investigative cycle across every unit. Its main defects are placing 14 earlier-grade retrieval skill ids (`alg1-*`, `geo-*`, `alg2-*`) into the `skills` column of `days.csv`, omitting the nine course-level check and respond days (`44 to 46`, `90 to 92`, `149 to 151`) from `source-map.csv`, and an ambitious 15-minute budget for seven independent fluency items on Check 3 (day 149). Fixing those two file-level defects and widening day 149's fluency-station budget will leave the scope ready for unit planning.

## Findings

### 1. Earlier-grade retrieval skill ids are placed in `days.csv` `skills` on 13 days

- **LAYER:** sequence
- **REPEAT:** yes (same kind as Calculus finding 1 and Precalculus finding 1)
- **Confidence:** firm
- **What is wrong:** Thirteen rows of `data/plans/statistics/days.csv` include 14 earlier-grade retrieval ids (`alg1-*`, `geo-*`, `alg2-*`) in the `skills` column alongside the unit's `stat-*` skill: days 5 (`alg1-data-displays`), 6 (`alg1-center-spread`), 12 (`alg2-normal-distributions`), 18 (`alg1-scatter-linear-models`), 19 (`alg1-correlation-causation`), 25 (`alg2-logarithms; alg2-combining-functions-models`), 31 (`alg2-study-design-randomness`), 36 (`alg2-experiments-significance`), 49 (`geo-sample-spaces-events`), 79 (`alg2-sample-estimates-margin`), 130 (`alg2-experiments-significance`), 138 (`alg1-two-way-tables`), and 142 (`alg1-scatter-linear-models`).
- **Why it matters:** `sequence-write.md` rule 2 states explicitly: "`skills` holds only what the day's own unit works on, because the skeleton reads an earlier-grade id in `skills` as a row of the day's own unit." Every one of these retrieval ids is already named in `note`.
- **Exact fix:** Remove all `alg1-*`, `geo-*`, and `alg2-*` ids from the `skills` column on those 13 days in `data/plans/statistics/days.csv`, leaving them in `note` only.

### 2. `source-map.csv` omits all nine course-level check and respond days

- **LAYER:** sequence
- **REPEAT:** yes (same kind as Psychology finding 1)
- **Confidence:** firm
- **What is wrong:** `data/plans/statistics/source-map.csv` maps every unit day cleanly (and zero `ours` days carry the word `Base`), but has no `ours` row for the nine course-level check and respond days (`44, 45, 46, 90, 91, 92, 149, 150, 151`).
- **Why it matters:** `sequence-write.md` rule 8 expects every course day 1 to 160 to be accounted for in `source-map.csv`.
- **Exact fix:** Add one `ours` row for `days` = `44-46; 90-92; 149-151` (`unit` blank or `C`, `decision` = `ours`) to `data/plans/statistics/source-map.csv`.

### 3. Check 3 day 149's 15-minute budget for seven independent fluency items is tight for an untimed station

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** likely
- **What is wrong:** Day 149 (`scope-and-sequence.md` line 120 and `days.csv` line 150) budgets "about 15 minutes" for an untimed, independent fluency station sampling seven outcomes (`CUR-ST.2`, `CUR-ST.3`, `CUR-ST.8`, `CUR-ST.12`, `CUR-ST.13`, `CUR-ST.16`, `CUR-ST.18`), which allows about 2 minutes per item for summary computation, a z-score/normal table lookup, a probability tree/table rule, and conditions plus calculations for four inference procedures, followed by five audit-and-choose items (`CUR-ST.6`, `9`, `11`, `14`, `15`).
- **Why it matters:** Under `RUBRIC-MATH-HS.md` 2b and `BASELINE` rule 30, the fluency station must be genuinely untimed and comfortable in a 50-minute period without rushing students.
- **Exact fix:** Budget 20 to 25 minutes for the 7-item fluency station on day 149 and 20 to 25 minutes for the five crisp audit-and-choose items (or trim the audit-and-choose set to 4 items), updating day 149's `note` in `data/plans/statistics/days.csv` and `scope-and-sequence.md`.

## Judgment of "For the lead" items

All four items in `docs/courses/statistics/scope-and-sequence.md` ("For the lead") are sound:
1. **Unit 7's two-proportion data (two states' microdata samples on days 110 to 111; polio trial randomized half on day 113):** Verified against `frame.md` and `days.csv`; clean and consistent.
2. **Dated microdata files (unit 7 single-state and two-state samples; unit 9 four regional worker samples of ~100 and one national sample of ~400):** Clear, actionable data-prep list for unit plans.
3. **Syncing `data/plans/calendar.csv` with `scripts/frame.py sync`:** Verified needed (`CALENDAR.md` still shows Check 3 on weeks 29 to 30 rather than weeks 30 to 31, days 149 to 151, and the held investigation days 47, 48, 70, and 71 need to appear in their own weeks).
4. **Unit 5's first sitting response (first 15 minutes of day 72, no kit on day 72):** Verified against `days.csv` days 69 to 78; placing Unit 10's held data days 70 and 71 right after day 69 gives the teacher two days to score Sitting 1 and repair expected value before the decision days begin.

## Lens checklist (statistics and math, scope and sequence layer)

- **Investigative cycle named in every unit (or why supplied data are used):** Met across all 10 units (`Cycle:` paragraph in every unit section).
- **Variability and context throughout, real public data with free source and "as of" date:** Met across all 10 units; non-random listings (day 123 home costs) and non-independent series (days 142 to 143 Old Faithful) explicitly flagged as conditions cases rather than fed into sampling formulas.
- **Concepts before recipes (simulation/randomization before formulas; conditions and meaning assessed; scope of inference stated):** Met across Units 3, 4, 6, 7, 8, and 9.
- **Active learning and technology with paper path:** Met (cards, dice, random digit tables, printed tables, printed regression outputs, scales with invented-for-practice fallback).
- **Data ethics and privacy:** Met (no student personal health, money, home, commute, or identity data collected; OpenStax student-survey labs on shoes, place of birth, home language, clothes, TV hours, gender, and pocket money explicitly cut).
- **Math lens checks (every owned code taught in full, spaced untimed fluency with direct year-end station, modeling cycle whole, 15% cap met, shorter path and candidate cells settled):** Met (13.5 percent cap; 10 fold-in days saving 500 minutes / 10 days; senior early-end 5-day order).

## Fact and dataset checks

- **Azzalini and Bowman (1990) Old Faithful geyser dataset (days 14, 84, 142 to 143):** Verified via [Oxford Academic](https://academic.oup.com/) (*Applied Statistics*, 1990). Accurate.
- **Ezekiel (1930) car speeds and stopping distances (day 26):** Verified (Mordecai Ezekiel, *Methods of Correlation Analysis*, 1930). Accurate.
- **1954 polio vaccine field trial, Francis et al. (1955), randomized placebo-controlled half beside observed-control half (days 37, 113):** Verified via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [University of Michigan](https://www.umich.edu/). Accurate.
- **US one-cent coin 1982 metal change (pre-1982 95% copper ~3.11 g vs post-1982 copper-plated zinc ~2.50 g, days 117, 119, 120, 128):** Verified (transition occurred mid-1982, so excluding 1982 is exact). Accurate.
- **NOAA NCEI 1991 to 2020 (and 1961 to 1990) U.S. Climate Normals (days 123 to 126, 131):** Verified via [NOAA](https://www.noaa.gov/) and [Climate.gov](https://www.climate.gov/). Accurate.
- **Other named sources not individually web-checked in this pass:** US Census Bureau ACS commuting/vehicle/county/PUMS tables, NPS visitor use statistics, DOE/EPA fuel economy data, US Census historical counts 1790 to 1900, NOAA GML Mauna Loa CO2 yearly means, NHTSA seat-belt use survey, Mendel (1866) pea counts (not checked individually by link here; all standard public sources, consistent from memory).

## What is right and should not be touched

- **Honest scope of inference and conditions discipline:** Cutting non-random OpenStax student-survey labs, keeping the home-costs listing strictly as a conditions-failure case (day 123), and pairing four separate regional samples (homogeneity, day 138) against one national sample (independence, day 139) makes the statistical reasoning airtight.
- **Unit 5 + Unit 10 interlock (days 69 to 72):** Using Unit 10's two held data-gathering/cleaning days (70 and 71) immediately after Unit 5's random-variable sitting (day 69) gives the teacher turnaround time to grade Sitting 1 and run a 15-minute repair on day 72 before expected-value decisions begin.
- **Unit 8's wrong-then-right contrast (day 132):** Analyzing one paired dataset wrongly as two independent samples and rightly as pairs after both procedures are taught directly builds the design-choice judgment `CUR-ST.17` and `CUR-ST.18` demand.

## What it could not judge

- Lesson-level multilingual learner language goals (`RUBRIC-MATH-HS.md` gap 9, not yet placed in `statistics/scope-and-sequence.md`, unlike Precalculus, and owed in unit plans).
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Remove all 14 `alg1-*`, `geo-*`, and `alg2-*` ids from `skills` on the 13 retrieval days (keep them in `note`) | `sequence-write.md` rule 2 restricts `skills` to the day's own unit so `unit_skeleton.py` does not misread earlier-grade rows as owned | `data/plans/statistics/days.csv` |
| Add an `ours` row for `44-46; 90-92; 149-151` to `source-map.csv` | Accounts for all 160 course days per `sequence-write.md` rule 8 | `data/plans/statistics/source-map.csv` |
| Widen Check 3 day 149's fluency-station budget from ~15 minutes to 20 to 25 minutes | Keeps 7 independent fluency items genuinely untimed in a 50-minute period | `data/plans/statistics/days.csv`, `docs/courses/statistics/scope-and-sequence.md` |

## For Cory

None.

## Sources

- [Oxford Academic](https://academic.oup.com/): verified Azzalini and Bowman (1990) Old Faithful geyser dataset (*Applied Statistics*).
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [University of Michigan](https://www.umich.edu/): verified 1954 polio vaccine field trial and Francis Report (April 12, 1955), including randomized placebo-controlled and observed-control arms.
- [NOAA](https://www.noaa.gov/) and [Climate.gov](https://www.climate.gov/): verified NCEI 30-year U.S. Climate Normals (1991 to 2020).
- Standard reference facts: Ezekiel (1930) stopping-distance dataset and US Mint 1982 cent composition change (3.11 g copper to 2.50 g copper-plated zinc), confirmed in search summaries.
