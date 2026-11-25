# Cold read: Earth and Space Science scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-earth-and-space-science-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-earth-and-space-science-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `earth-and-space-science` (grade 12 elective, open to grades 10 to 12, full year, 160 course days)
**Subject:** science
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/science.md`, `docs/RUBRIC-SCIENCE.md`
- `docs/courses/earth-and-space-science/frame.md`, `docs/courses/earth-and-space-science/scope-and-sequence.md`
- `data/plans/earth-and-space-science/days.csv`, `data/plans/earth-and-space-science/source-map.csv`
- `data/standards/curio-science-electives.txt` (`CUR-ESS.1` to `CUR-ESS.26`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I verified all gate subjects directly against `days.csv`, `source-map.csv`, `curio-science-electives.txt`, and `CALENDAR.md`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 9: 18, 15, 18, 17, 17, 15, 17, 14, 18 = 149 unit days, plus 11 `C` days = 160).
- **Kinds:** 66 Understanding, 48 Application, 12 Fluency, 16 Check, 18 Respond. Every Fluency day practices only skills taught on earlier days, introduces no new outcome, and drafts, revises, or edits no writing.
- **Owned standards:** All 26 outcomes (`CUR-ESS.1` to `CUR-ESS.26`) are taught before being assessed and appear on an `end` assessment day (either a revised product on an Application day with `assess=end` or the sitting on the second-last day of the unit).
- **Supplies and safety:** Every day that names `supplies` also fills `safety` (`none` in lower case when weighed and hazard-free, or hazards and controls in the frame's words). See Finding 4 for one phrasing edge case on day 110.
- **Assessments and calendar:** Every unit ends with an assessment (second-last day sitting, plus revised product where named) and one Respond day, counted once. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 52 to 53 (week 11, respond day 54), 104 to 105 (week 21, respond day 106), and 156 to 158 (week 32, finals week, respond days 159 and 160), matching `CALENDAR.md`.
- **Readiness and retrieval:** Counted by grade number from grade 12, Physics (grade 11) rows open as retrieval, and Chemistry (grade 10) or earlier rows last used in grade 10 receive readiness checks in the last ten minutes of the preceding unit's Respond day or intervening course-level Respond day (days 33, 54, 71, 106, 137; never on a unit's first day), with a one-lesson reteach counted on day 2 of units 3, 4, 5, 7, and 9.

## Verdict

The Earth and Space Science scope and sequence is phenomenon-driven, quantitatively rigorous, and well aligned with `RUBRIC-SCIENCE.md` and the science lens. Its biggest gap is inconsistency in the "Practice and crosscutting concept coverage" table (which drops Day 1 initial-model sketches in units 3 to 9, mis-indexes Unit 9's investigation days, and under-counts models and arguments on course-level check days), along with missing `ours` rows in `source-map.csv`. Fixing the coverage table and adding `ours` rows to the source map will bring the scope into full alignment with `sequence-write.md`.

## Findings

### 1. Practice and crosscutting concept coverage table is inconsistent with `days.csv`

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Checking the "Practice and crosscutting concept coverage" table (`docs/courses/earth-and-space-science/scope-and-sequence.md`, lines 185 to 196) against `data/plans/earth-and-space-science/days.csv` shows three mismatches:
  1. **Initial models in column `M`:** Units 1 and 2 count Day 1 ("sketch an initial model") under `M` (days 1 and 19), but Units 3 to 9 omit their Day 1 initial-model days (34, 55, 72, 89, 107, 124, 138) from `M`, even though all seven goals explicitly require sketching an initial model.
  2. **Unit 9 column `I` (Planning and Carrying Out Investigations):** Lists `140, 152` (explaining sky-log entries and drafting the sky-log summary) rather than day 141 ("Model parallax with a thumb and a protractor") or the sky-log observation days (124, 138).
  3. **Course-level checks row:** Column `M` lists only `160` (a Respond day) and omits `52`, `53`, and `157` (profiling a topographic map, drawing a cross section from a geologic map, mapping groundwater flow, and working a planetary energy-balance model). Column `A` (Engaging in Argument from Evidence) says `none`, even though day 104 judges one line of evidence (`CUR-ESS.10`) and day 158 states a volcano's hazard from monitoring and eruption history (`CUR-ESS.11`).
- **Why it matters:** `sequence-write.md` requires the coverage table to be counted accurately from `days.csv` goals and notes, and `RUBRIC-SCIENCE.md` (Gateway 2, 2b and 2c, S11) relies on this trace to verify three-dimensional coverage across units and checks.
- **Exact fix:** In `docs/courses/earth-and-space-science/scope-and-sequence.md`: (a) add days 34, 55, 72, 89, 107, 124, and 138 to column `M` in Units 3 to 9 so all nine units count initial modeling consistently; (b) update Unit 9 column `I` to `138, 141, 152` (or `141` if only in-class measurement counts, and note the six-week sky log); (c) update the Course-level checks row to `52, 53, 157, 160` in column `M` and `104, 158` in column `A`.

### 2. `source-map.csv` omits all 86 `ours` days

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** `data/plans/earth-and-space-science/source-map.csv` maps every adapted base-text section cleanly (matching `Adapts ...` notes in `days.csv` with zero mismatches), but leaves 86 days (including field days, assessments, respond days, and all 11 `C` days) unmapped with no `ours` rows.
- **Why it matters:** `sequence-write.md` rule 8 specifies `source` = `ours` for days with no base lesson so a reviewer can verify that every day 1 to 160 is accounted for as adapted or original.
- **Exact fix:** Add one `ours` row per unit and one `ours` row for the course-level check and respond days (`52-54; 104-106; 156-160`) to `data/plans/earth-and-space-science/source-map.csv`.

### 3. Day 30 omits the "Evidence meets belief" note on the geologic time scale

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** likely
- **What is wrong:** In Unit 2 ("The rock record"), days 19, 24, 25, and 29 explicitly carry the `Evidence meets belief` note with the evidence placed first. Day 30 ("Read the geologic time scale as a parallel timeline on one scale, argue which events in a section cannot be dated, revise the class model and answer the question board") brings deep time together on the full geologic time scale but omits that note. (Unit 7's climate change days 107, 114, 116, and 118 all carry the note cleanly with natural proxy records taught on days 109 to 113 before human cause is recalled on day 114.)
- **Why it matters:** `sequence-write.md` rule 9 requires every science day where evidence meets a belief (including the age of Earth) to name it in `note` with the evidence first.
- **Exact fix:** Add the `Evidence meets belief: the age of Earth` sentence to day 30's `note` in `data/plans/earth-and-space-science/days.csv` and add day 30 to Unit 2's evidence-meets-belief list in `scope-and-sequence.md`.

### 4. Day 110's `safety` cell uses the word `none` inside a multi-item list

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** likely
- **What is wrong:** Day 110's `safety` cell reads `wood rounds: sanded, or photographs; cutting tools: none; clean-up: 5 minutes`. While `cutting tools: none` is a hazard-control phrase rather than the standalone `none` marker, `sequence-write.md` specifies that `none` in `safety` is reserved for a single lower-case word when a day has no hazard.
- **Why it matters:** Rewording avoids any parser ambiguity and keeps safety phrasing uniform with Unit 1 (`no rock hammers, no hydrochloric acid`).
- **Exact fix:** Change `cutting tools: none` to `no cutting tools` in day 110's `safety` cell in `data/plans/earth-and-space-science/days.csv`.

## Judgment of "For the lead" items

1. **Sitting moved to second-last day, respond day last (applied 2026-11-24):** Sound and closed; aligns with `sequence-write.md` rule 2.
2. **Astronomy 12.5 cut as planetary rings; 12.2 kept on day 134 (applied 2026-11-24):** Sound and closed.
3. **Introduction to Oceanography not in source store:** Sound; unit 6's JetStream + Physical Geology 18.4 + Curio Class text plan is self-contained, and the fallback landing days (81, 90 to 92, 94) are clearly documented if the book is added later.
4. **Anchor evidence still to pin (Ellicott City rainfall/county study/Patapsco gauge, Monadnock summit rock, Copalis River nations):** Sound; properly deferred to unit plans without changing day counts. Web check confirms Mount Monadnock's summit is Devonian Littleton Formation schist and quartzite.
5. **Eight "reads like hands-on" gate notes (days 1, 25, 29, 64, 73, 97, 115, 117):** Verified against `days.csv`; none of those eight days uses physical lab materials.

## Lens checklist (science, scope and sequence layer)

- **Anchors are specific phenomena, not topic headings:** Met across all 9 units (Monadnock, Siccar Point, Copalis River ghost forest and 1700 tsunami, 2016/2018 Ellicott City floods, Nov 2014 Buffalo snow band, 1972 Peru anchovy collapse, 11,700 BP Greenland abrupt warming, Jezero crater and rocky planet temperatures, TRAPPIST-1 transits).
- **Models built and revised, never used before built:** Met (map-model built in unit 1, used in units 2 to 5 and 8; energy-balance computational model built in unit 7, extended in units 8 and 9).
- **Engineering design expectations:** Course owns no engineering outcome; unit 3 retrieves Biology and Chemistry design practices (criteria, constraints, trade-offs) for the coastal town hazard advice. Met.
- **Equipment has substitutes, no-kit path, and stated costs:** Met (provisional cost about \$955/year for a class of 30; no-kit and no-sky paths named on every hands-on day, with practical steps still owed flagged for CUR-ESS.2, CUR-ESS.12, and CUR-ESS.24).
- **Evidence meets belief named with evidence first:** Met in Unit 7 (climate change, days 107, 114, 116, 118) and Unit 2 (days 19, 24, 25, 29; see Finding 3 for day 30).
- **Shorter path:** Met (40 to 45 minute period guidance + 10 named Fluency fold-in days saving 500 minutes / 10 days, plus senior early-end 5-day order).
- **Candidate cells settled:** Met (all 9 units' candidates settled; unit 4's engineering crosscutting element dropped with a clear reason).

## Fact and figure checks

- **Mount Monadnock prominence (~600 m) and Littleton Formation quartzite/schist (day 1 / frame):** Checked via [New Hampshire Geological Survey (nh.gov)](https://www.nh.gov/) and [Wikipedia](https://en.wikipedia.org/). Accurate (prominence ~649 to 660 m, ~600 m above surrounding lowlands; Devonian Littleton Formation schist and quartzite).
- **Copalis River ghost forest (last rings 1699), January 1700 orphan tsunami in Japan, Mount St. Helens May 1980 eruption with 57 deaths (days 34, 42, 44):** Checked via [USGS](https://www.usgs.gov/) and [NOAA](https://www.noaa.gov/). Accurate (Jan 26, 1700 M9.0 Cascadia earthquake; May 18, 1980 Mount St. Helens, 57 deaths).
- **Greenland ice core abrupt warming ~11,700 years ago (day 107):** Checked via [NOAA](https://www.noaa.gov/) and [Columbia University](https://www.columbia.edu/). Accurate (end of Younger Dryas / onset of Holocene, ~11,700 BP).
- **Planetary energy-balance numbers for Venus, Earth, and Mars (days 127 and 128):** Checked against [NASA Planetary Fact Sheets](https://nssdc.gsfc.nasa.gov/). Using NASA Bond albedos (Venus 0.77, Earth 0.294, Mars 0.250), black-body effective temperatures (226.6 K, 254.0 K, 209.8 K), and mean surface temperatures (737 K, 288 K, 210 K): a single fully absorbing layer ($T_s = 2^{1/4} T_e$) yields ~302 K for Earth (~14 to 15 degrees warm), ~250 K for Mars (~40 degrees warm), and ~270 K for Venus (~467 degrees cold, more than 400 degrees cold). Solving $N = (T_s / T_e)^4 - 1$ gives Mars near 0, Earth ~0.65 (under 1), and Venus ~111 (about 100). Accurate.
- **Other named events and constants not individually web-checked in this pass:** James Hutton at Siccar Point (1788), 10x amplitude / ~30x energy per earthquake magnitude step, 2016 and 2018 Ellicott City floods, November 2014 Buffalo snow storm, Peru's 1972 anchovy collapse, TRAPPIST-1's seven planets (not checked individually by link here; consistent from memory).

## What is right and should not be touched

- **Quantitative planetary energy balance (days 125 to 128):** Testing a 1-layer model where it fails visibly on all three planets and then solving for layer count $N$ is an outstanding model-revision sequence, and the numbers check out against NASA fact sheets.
- **Cascadia multi-line evidence arc (unit 3):** Combining seismic lag times, GPS strain, ghost forests, Japanese written records, and published Native nations' oral histories (credited and quoted, never treated as waiting for science to confirm them) models the nature of science and sensitivity rules at their best.
- **Course-level checks and non-repetition:** Clean separation of assessed units (unit 3 deferred to check 2, unit 6 to check 3, unit 9 not resampled in check 3) and explicit per-part minute budgets.

## What it could not judge

- Actual lesson-level reading complexity, supplies cost accuracy, and whether the practical steps still owed on the no-kit path for `CUR-ESS.2`, `CUR-ESS.12`, and `CUR-ESS.24` are resolved adequately in the unit plans.
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Add initial-model days (34, 55, 72, 89, 107, 124, 138) to column `M`, update Unit 9 column `I`, and add `52, 53, 157` to `M` and `104, 158` to `A` in Course-level checks | Makes the Practice and crosscutting concept coverage table consistent with `days.csv` | `docs/courses/earth-and-space-science/scope-and-sequence.md` |
| Add `ours` rows for all 86 non-adapted days (per unit and for `C` days) | Completes day-level accounting in the source map per `sequence-write.md` rule 8 | `data/plans/earth-and-space-science/source-map.csv` |
| Add `Evidence meets belief: the age of Earth` to day 30's note | Covers the full geologic time scale day under `sequence-write.md` rule 9 | `data/plans/earth-and-space-science/days.csv`, `docs/courses/earth-and-space-science/scope-and-sequence.md` |
| Change `cutting tools: none` to `no cutting tools` on day 110 | Avoids using `none` inside a multi-item safety list | `data/plans/earth-and-space-science/days.csv` |

## For Cory

None.

## Sources

- [New Hampshire Geological Survey (nh.gov)](https://www.nh.gov/) and [Wikipedia](https://en.wikipedia.org/): verified Mount Monadnock prominence (~600 m above surrounding lowlands) and Devonian Littleton Formation quartzite/schist bedrock.
- [USGS](https://www.usgs.gov/) and [NOAA](https://www.noaa.gov/): verified Copalis River ghost forest (1699 last rings), January 26, 1700 Cascadia earthquake and orphan tsunami in Japan, and Mount St. Helens May 18, 1980 eruption (57 deaths).
- [NOAA](https://www.noaa.gov/) and [Columbia University](https://www.columbia.edu/): verified Greenland ice core abrupt warming ~11,700 BP at the Younger Dryas to Holocene transition.
- [NASA Planetary Fact Sheets](https://nssdc.gsfc.nasa.gov/): verified Bond albedo, black-body effective temperature, and mean surface temperature of Venus, Earth, and Mars for the days 127 to 128 energy-balance calculations.
