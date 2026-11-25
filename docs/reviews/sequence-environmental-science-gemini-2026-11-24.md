# Cold read: Environmental Science scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-environmental-science-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-environmental-science-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `environmental-science` (grade 12 elective, open to grades 11 and 12, full year, 160 course days)
**Subject:** science
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/science.md`, `docs/RUBRIC-SCIENCE.md`
- `docs/courses/environmental-science/frame.md`, `docs/courses/environmental-science/scope-and-sequence.md`
- `data/plans/environmental-science/days.csv`, `data/plans/environmental-science/source-map.csv`
- `data/standards/curio-science-electives.txt` (`CUR-ENV.1` to `CUR-ENV.21`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I verified all gate subjects directly against `days.csv`, `source-map.csv`, `curio-science-electives.txt`, and `CALENDAR.md`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 9: 18, 15, 18, 15, 16, 15, 14, 18, 20 = 149 unit days, plus 11 `C` days = 160).
- **Kinds:** 62 Understanding, 61 Application, 8 Fluency, 16 Check, 13 Respond. Every Fluency day practices only previously taught methods, introduces no new outcome, and drafts, revises, or edits no writing.
- **Owned standards:** All 21 outcomes (`CUR-ENV.1` to `CUR-ENV.21`) are taught before being assessed and appear on an `end` assessment day. (See Finding 1 regarding non-owned literacy codes placed in the `codes` column.)
- **Supplies and safety:** Every hands-on day (field days 4, 5, 42, 121, 140, 141; bench days 21 to 23, 40, 57, 73, 106, 120) lists supplies and safety controls; all non-hands-on days list `none` in `safety`. (See Finding 5 on phrasing in days 21 to 23.)
- **Assessments and calendar:** Every unit has an end-of-unit assessment (units 1, 5, 8, and 9 split into a revised product/presentation plus a sitting or second end day) and one Respond day, counted once. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 52 to 53 (week 11, respond day 54), 101 to 102 (week 21, respond day 103), and 156 to 158 (week 32, finals week, respond days 159 and 160), matching `CALENDAR.md`.
- **Readiness and retrieval:** Counted by grade number from grade 12, Physics (grade 11) rows open as retrieval, and Biology/Chemistry/grade 7 rows last used in grades 9 or 10 receive readiness checks in the last ten minutes of day 1 (unit 1, after the hook) or the preceding unit's / course-level check's Respond day (days 18, 33, 54, 69, 85, 103, 117; never on any other unit's first day), with repair counted inside the receiving unit.

## Verdict

The Environmental Science scope and sequence is coherent, field-grounded, and thoughtful in its handling of policy boundaries, Navajo Nation sovereignty, and evidence-first climate teaching. Its two most actionable defects are putting non-owned Common Core literacy codes (including `WHST.11-12.2`) into the `codes` column of `days.csv` on `assess=end` days, and an out-of-sync Unit 5 block in `source-map.csv` where Harris chapters 6 and 12 are shifted by one to four days against `days.csv`. Fixing those two issues, correcting day 158's fold-order note, and updating four cells in the Practice and crosscutting concept coverage table will leave the scope ready for unit planning.

## Findings

### 1. Practiced literacy codes are placed in `days.csv` `codes`, including on `assess=end` days

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** `data/plans/environmental-science/days.csv` places nine non-owned Common Core literacy codes (`RST.11-12.1`, `RST.11-12.3`, `RST.11-12.7`, `RST.11-12.8`, `RST.11-12.9`, `WHST.11-12.1`, `WHST.11-12.2`, `WHST.11-12.7`, `WHST.11-12.8`) in the `codes` column across 28 days, including `WHST.11-12.2` on three `assess=end` days (days 16, 82, and 129). `frame.md` explicitly states that these literacy standards are practiced, not owned, and that "No unit teaches and checks a lettered part on purpose, so none is claimed in full, none is an owned standard."
- **Why it matters:** `sequence-write.md` rule 2 requires every `end` assessment day to ask about each part of each code it lists (`WHST.11-12.2` has lettered parts a to f). Leaving literacy codes in `codes` on `end` days contradicts `frame.md` and `scope-and-sequence.md` ("The course owns only CUR-ENV.1 to CUR-ENV.21") and risks a writer or gate treating them as assessed standards. Both Psychology and Earth and Space Science keep practiced literacy codes out of `days.csv` `codes` (recording them in `note` or `scope-and-sequence.md` only).
- **Exact fix:** Remove all `RST.11-12.*` and `WHST.11-12.*` codes from the `codes` column of `data/plans/environmental-science/days.csv` and move them into each day's `note` as `Practiced: RST.11-12.x` / `Practiced: WHST.11-12.x`.

### 2. `source-map.csv` is out of sync with `days.csv` on Unit 5 (days 74 to 78) and omits `ours` rows

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** When town waste (`Harris 12.1, 12.2, 12.4`) was moved earlier in Unit 5, `data/plans/environmental-science/source-map.csv` was not updated to match `days.csv`:
  - `Harris 12.1`, `12.2`, and `12.4` are mapped to day `78` in `source-map.csv`, but `days.csv` adapts them on day `74`.
  - `Harris 6.1` and `6.2` are mapped to day `74` in `source-map.csv`, but `days.csv` adapts them on day `75`.
  - `Harris 6.3` is mapped to day `75` in `source-map.csv`, but `days.csv` adapts it on day `76`.
  - `Harris 6.4` is mapped to day `77` in `source-map.csv`, but `days.csv` adapts it on day `78`.
  In addition, `source-map.csv` has no `ours` rows covering the 123 non-adapted days (`sequence-write.md` rule 8).
- **Why it matters:** A unit writer using `source-map.csv` for Unit 5 will pull the wrong Harris sections on five consecutive days (days 74 to 78).
- **Exact fix:** In `data/plans/environmental-science/source-map.csv`, update `days` for `Harris 12.1`, `12.2`, `12.4` to `74`; `Harris 6.1`, `6.2` to `75`; `Harris 6.3` to `76`; `Harris 6.4` to `78`. Add `ours` rows (one per unit and one for `C` days) so all 160 days are accounted for.

### 3. Day 158's note contradicts `frame.md` and `scope-and-sequence.md` on senior early-end fold order

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Day 158's `note` in `days.csv` reads: `The oldest item (unit 1); the day folds first if seniors leave early (frame Grade 12 calendar).` However, both `frame.md` (Grade 12 calendar) and `scope-and-sequence.md` (Shorter path, line 200) place day 158 **third** in the senior early-end fold order (after day 160, the second respond day, and day 141, unit 9's second field day), specifically so an assessed check day is not dropped before non-assessed days.
- **Why it matters:** A teacher reading `days.csv` day 158 will drop an assessed course-level check day first when seniors lose one or two days, instead of folding day 160 and day 141 first.
- **Exact fix:** Change `the day folds first if seniors leave early` in day 158's `note` in `data/plans/environmental-science/days.csv` to `the day folds third if seniors leave early (after days 160 and 141)`.

### 4. Four small omissions in the Practice and crosscutting concept coverage table

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Checking `docs/courses/environmental-science/scope-and-sequence.md` (lines 218 to 229) against `days.csv` shows four omissions:
  1. Unit 7 column `M` omits day `108` (`Model revision point: one cause tested against its rivals` in `days.csv`).
  2. Unit 8 column `M` omits day `123` (`Model revision point: heat follows land cover` in `days.csv`).
  3. Course-level checks column `D` omits day `156` (reading national demographic transition data and wildlife survey data).
  4. Course-level checks column `Mth` omits days `101` (scoring the stream tolerance index) and `158` (recording supplied quadrat and transect counts as cover with spread).
- **Why it matters:** The coverage table is the evidence trace for `RUBRIC-SCIENCE.md` Gateway 2 (2b, 2c, S11) and must match `days.csv` accurately.
- **Exact fix:** Add `108` to Unit 7 column `M`, `123` to Unit 8 column `M`, `156` to Course-level checks column `D`, and `101, 158` to Course-level checks column `Mth` in `docs/courses/environmental-science/scope-and-sequence.md`.

### 5. Bench-lab `safety` cells on days 21 to 23 contain the word `none` inside a multi-item list

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** likely
- **What is wrong:** Days 21, 22, and 23 carry `soil: gloves on, hands washed after, none from roadsides or old building sites (lead)` in their `safety` column. Rewording `none from` to `no soil from` avoids any false-positive check on the reserved `none` safety marker.
- **Exact fix:** Replace `none from roadsides` with `no soil from roadsides` on days 21, 22, and 23 in `data/plans/environmental-science/days.csv`.

## Judgment of "For the lead" items

1. **Frame fits; all 19 Candidate cells kept inside existing days:** Verified and sound.
2. **Units 1, 5, and 8 sitting moved to next-to-last day; frame updated 2026-11-24:** Sound and closed.
3. **Harris licence read (chapters 11 to 13 CC BY only; chapters 8 and 14 have CC BY-NC sources, so days 93, 119, 147 adapt only CC BY-traced parts):** Sound; important rights safeguard properly flagged for unit writers.
4. **Anchor figures pinned from writer's knowledge (no page opened in that pass):** Sound; see Fact and figure checks below, which verify the main figures by outside link.
5. **`TOOL-ASKS.md` not written; 9 tool names in `days.csv`:** Sound.
6. **ELA 12 senior research presentations (days 150 to 156) overlap unit 9 report (day 151) and presentations (day 153):** Sound to leave as is without moving a unit, as `frame.md` foresaw.
7. **Unit 9 has no Fluency day (capstone):** Sound.

## Lens checklist (science, scope and sequence layer)

- **Anchors are specific phenomena or design problems, not topic headings:** Met across all 9 units (Park Grass 1856 plots, Loess Plateau / Yellow River sediment, 2014 Toledo microcystin bloom, Britain's 2012 to 2024 coal phase-out, Navajo Nation abandoned uranium mines, Japan vs Niger population, Everglades python/mammal decline, Richmond 2017 urban heat and 1930s maps, Philadelphia 2011 green infrastructure).
- **Models built and revised, never used before built:** Met across all 9 units.
- **Engineering design expectations:** Met in Unit 9 (`CUR-ENV.20`, deepening `HS-ETS1-1` to `HS-ETS1-3`), with criteria/constraints/trade-offs used earlier in Units 2, 3, and 7.
- **Equipment has substitutes, no-kit path, and stated costs:** Met (about \$840/year for a class of 30, about \$100 one-child; no-kit paths named on every hands-on day with partial-coverage flags for `CUR-ENV.1, 4, 7, 17, 19`).
- **Evidence meets belief named with evidence first:** Met on day 61 (`Evidence meets belief (climate change): the records come first and the day teaches plainly and respectfully what they show`), with measured CO2, temperature, and power-sector emissions read before Britain's coal records on day 62.
- **Shorter path:** Met (40 to 45 minute period guidance + 10 named fold-in days saving 500 minutes / 10 days, plus senior early-end 5-day order; see Finding 3 on day 158's note).
- **Candidate cells settled:** Met (all 19 kept with 0 added days).

## Fact and figure checks

- **Toledo water crisis (August 2014, ~400,000 people, 3-day do-not-drink advisory, microcystin from Lake Erie bloom, unit 3):** Checked via [ACS](https://www.acs.org/), [NRDC](https://www.nrdc.org/), and [Circle of Blue](https://www.circleofblue.org/). Accurate.
- **Britain's coal share ~40% in 2012 and Ratcliffe-on-Soar closing 30 September 2024 (unit 4):** Checked via [Ember Energy](https://ember-energy.org/) and [The Guardian](https://www.theguardian.com/). Accurate.
- **Navajo Nation >500 abandoned uranium mines, 2005 Diné Natural Resources Protection Act ban, 1979 Church Rock tailings spill, EPA uranium MCL 30 micrograms per liter (unit 5):** Checked via [U.S. EPA](https://www.epa.gov/), [NIH](https://www.nih.gov/), [Science History Institute](https://www.sciencehistory.org/), and [U.S. NRC](https://www.nrc.gov/). Accurate.
- **Everglades road surveys (~99% decline in raccoons and opossums: 99.3% raccoons, 98.9% opossums, unit 7):** Checked via [USGS](https://www.usgs.gov/). Accurate.
- **108-city redlining and urban heat study (Hoffman, Shandas & Pendleton, 2020, unit 8):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [PreventionWeb](https://www.preventionweb.net/) (108 U.S. cities, up to ~7 degrees Celsius difference between A and D grade averages; the 2017 Richmond single-day traverse finding ~9 degrees Celsius / 16 degrees Fahrenheit between coolest and hottest blocks is consistent from memory and flagged for unit-plan pinning).
- **Other named figures not individually web-checked in this pass:** Park Grass experiment starting 1856, Yellow River sediment drop of ~9/10 from mid-20th century, Japan population decline since ~2010 and Niger fertility near 6 / growth >3%, Philadelphia 2011 Green City Clean Waters plan (not checked individually by link here; consistent from memory).

## What is right and should not be touched

- **Navajo Nation Unit 5 framing:** Showing the Nation's own sovereignty, scientists, 2005 ban, and research board alongside the legacy mines (using only publicly released material and distinguishing chemical kidney toxicity of uranium in water from radiation lung-cancer risk of radon in air) is scientifically accurate and deeply respectful.
- **Rival-cause discipline across units:** Units 2 (Loess Plateau practices vs dams and rainfall), 4 (UK carbon price floor vs gas prices, EU rules, renewables, demand), 7 (Everglades pythons vs habitat, roads, disease, storms), and 8 (1930s redlining grades vs pre-existing density, industry, rail) consistently train students to weigh rival hypotheses on evidence.
- **Social studies calendar bridges:** Every Grade 12 Economics and Government lean is explicitly checked against `calendar.csv` and bridged in its own terms where Economics or Government arrives later.

## What it could not judge

- Which specific passages in Harris chapters 8 and 14 trace to CC BY vs CC BY-NC sources (properly deferred to unit writers).
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Move `RST.11-12.*` and `WHST.11-12.*` out of `codes` into `note` as `Practiced:` | Prevents `assess=end` days from claiming unowned multi-part literacy standards | `data/plans/environmental-science/days.csv` |
| Fix Unit 5 day mappings for Harris 6.1 to 6.4 and 12.1, 12.2, 12.4 and add `ours` rows | Re-syncs source map with `days.csv` days 74 to 78 and accounts for all 160 days | `data/plans/environmental-science/source-map.csv` |
| Update day 158 note from "folds first" to "folds third (after days 160 and 141)" | Aligns `days.csv` with `frame.md` and `scope-and-sequence.md` senior early-end fold order | `data/plans/environmental-science/days.csv` |
| Add `108` (Unit 7 `M`), `123` (Unit 8 `M`), `156` (Checks `D`), and `101, 158` (Checks `Mth`) to coverage table | Aligns Practice and crosscutting concept coverage table with `days.csv` | `docs/courses/environmental-science/scope-and-sequence.md` |
| Change `none from roadsides` to `no soil from roadsides` on days 21 to 23 | Avoids `none` inside a multi-item safety list | `data/plans/environmental-science/days.csv` |

## For Cory

None.

## Sources

- [ACS](https://www.acs.org/), [NRDC](https://www.nrdc.org/), and [Circle of Blue](https://www.circleofblue.org/): verified August 2014 Toledo water crisis (~400,000 residents, 3-day advisory, microcystin).
- [Ember Energy](https://ember-energy.org/) and [The Guardian](https://www.theguardian.com/): verified UK coal electricity share (~40% in 2012) and Ratcliffe-on-Soar closure (30 September 2024).
- [U.S. EPA](https://www.epa.gov/), [NIH](https://www.nih.gov/), [Science History Institute](https://www.sciencehistory.org/), and [U.S. NRC](https://www.nrc.gov/): verified >500 abandoned uranium mines on the Navajo Nation, 2005 Diné Natural Resources Protection Act ban, 1979 Church Rock spill, and 30 ug/L EPA uranium drinking-water MCL.
- [USGS](https://www.usgs.gov/): verified Everglades Burmese python road-survey declines (99.3% raccoons, 98.9% opossums).
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [PreventionWeb](https://www.preventionweb.net/): verified 108-city redlining and urban heat island study (Hoffman, Shandas & Pendleton, 2020).
