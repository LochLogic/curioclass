# Cold read: Precalculus scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-precalculus-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-precalculus-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `precalculus` (grade 12, open to grade 11 on the accelerated path, math core elective, full year, 160 course days)
**Subject:** math
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/math.md`, `docs/RUBRIC-MATH-HS.md`
- `docs/courses/precalculus/frame.md`, `docs/courses/precalculus/scope-and-sequence.md`
- `data/plans/precalculus/days.csv`, `data/plans/precalculus/source-map.csv`
- `data/standards/curio-math-electives.txt` (`CUR-PC.1` to `CUR-PC.16`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I verified all gate subjects directly against `days.csv`, `source-map.csv`, `curio-math-electives.txt`, and `CALENDAR.md`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 10: 16, 16, 14, 16, 14, 19, 13, 18, 11, 14 = 151 unit days, plus 9 `C` days = 160).
- **Kinds:** 96 Understanding, 22 Application, 12 Fluency, 17 Check, 13 Respond. Every Fluency day practices only skills taught on earlier days, introduces no new code, and drafts, revises, or edits no writing.
- **Owned standards:** All 58 owned codes (42 Common Core (+) standards and lettered parts plus `CUR-PC.1` to `CUR-PC.16`) are taught before being assessed and appear on an `end` assessment day.
- **Math columns (`tools`, `supplies`, `safety`):** `safety` is blank on every row; `tools` and `supplies` are well-formed lists.
- **Source map:** Every course day 1 to 160 is mapped in `data/plans/precalculus/source-map.csv` (zero unmapped days).
- **Assessments and calendar:** Every unit has an end-of-unit sitting on its second-last day (Unit 6 sits twice, days 85 and 97, as the frame sets) and one Respond day on its last, counted once. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 47 to 48 (week 10, respond day 49), 99 to 100 (weeks 20 to 21, respond day 101), and 158 to 159 (week 32, finals week, respond day 160), matching `CALENDAR.md`.
- **15 percent earlier-course cap (`RUBRIC-MATH-HS.md`):** Counted at most 1,105 of 7,550 unit minutes (14.6 percent), under the 15 percent cap (1,132.5 minutes).

## Verdict

The Precalculus scope and sequence is well structured, strong on both language goals and the eight math practices, and cleanly integrated with the 18 seams it hands on to Calculus. Its biggest remaining defects are placing 37 earlier-grade retrieval skill ids (`alg1-*`, `geo-*`, `alg2-*`) into the `skills` column of `days.csv` (forbidden by `sequence-write.md` rule 2), splitting Unit 3's Respond day (day 46) with a scored modeling-report revision, and leaving two stale cross-references (`For the lead 3` and `For the lead 4`) in `scope-and-sequence.md`. Removing those retrieval ids from `skills`, cleaning up the stale pointers, and adjusting six `ours` notes will make the scope ready for unit planning.

## Findings

### 1. Earlier-grade retrieval skill ids are placed in `days.csv` `skills` on 28 days

- **LAYER:** sequence
- **REPEAT:** yes (same kind as Calculus finding 1)
- **Confidence:** firm
- **What is wrong:** Twenty-eight rows of `data/plans/precalculus/days.csv` include 37 earlier-grade retrieval ids (`alg1-*`, `geo-*`, `alg2-*`) in the `skills` column alongside the unit's `pc-*` skill: days 1, 2, 6 (2 ids), 10 (2 ids), 17 (2 ids), 18, 20, 24, 27, 33 (2 ids), 34, 39, 50 (2 ids), 55, 56, 62, 66, 80 (2 ids), 86, 110, 115, 122, 126, 133 (2 ids), 144 (2 ids), 147, 149, and 152 (2 ids).
- **Why it matters:** `sequence-write.md` rule 2 states explicitly: "`skills` holds only what the day's own unit works on, because the skeleton reads an earlier-grade id in `skills` as a row of the day's own unit." Every one of these retrieval ids is already named in `note`.
- **Exact fix:** Remove all `alg1-*`, `geo-*`, and `alg2-*` ids from the `skills` column on those 28 days in `data/plans/precalculus/days.csv`, leaving them in `note` only.

### 2. Unit 3 places scored modeling-report revision on the Respond day (day 46), and two stale `For the lead` pointers remain in `scope-and-sequence.md`

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:**
  1. On day 46 (`kind` = `Respond`), Unit 3 splits the period into 25 minutes of response to the day 45 end-of-unit sitting and 25 minutes of revising the wolf-count modeling report (scored after day 46). This cuts the unit's end-of-unit response time in half and places scored work after the end-of-unit sitting (unlike Units 6, 7, and 8, which revise their modeling reports on an Application day before the sitting: days 96, 112, and 130).
  2. `docs/courses/precalculus/scope-and-sequence.md` still contains two stale cross-references to deleted "For the lead" items: line 65 cites `(For the lead 4)` and line 85 cites `(For the lead 3)`, whereas the "For the lead" section (lines 166 to 172) now has only items 1 and 2.
- **Why it matters:** Halving Unit 3's Respond day leaves 25 minutes for group reteaching and parallel retries across 30 students on three outcomes (`F-BF.B.5`, `CUR-PC.4`, `CUR-PC.5`), and the broken pointers mislead the unit writer.
- **Exact fix:** Remove the stale `(For the lead 4)` and `(For the lead 3)` pointers from lines 65 and 85 of `docs/courses/precalculus/scope-and-sequence.md`. If Unit 3's report revision is kept on day 46 (permitted by `frame.md` line 10, which only excludes end days and first-teaching days), state plainly in Unit 3's prose that day 46 splits 25/25 because day 42 teaches logistic fitting and day 43 drafts; alternatively, move the wolf-count revision (25 minutes) onto day 44's second half (one night turnaround with the one-page feedback form) so day 46 stays a full 50-minute Respond day.

### 3. Six `ours` days carry the word `base` in their `note`

- **LAYER:** sequence
- **REPEAT:** yes (same kind as Calculus finding 2)
- **Confidence:** firm
- **What is wrong:** Days 24, 29, 95, 107, 125, and 134 are `ours` days (no base lesson adapted), but their `note` cells say `the base text has no...` (`sequence-write.md` rule 8: `Days that adapt no base lesson never carry "Base" in their goal or note`).
- **Exact fix:** Reword `the base text has no...` to `OpenStax 1e has no...` or `written by Curio Class` on days 24, 29, 95, 107, 125, and 134 in `data/plans/precalculus/days.csv`.

## Judgment of "For the lead" items

The two open items in `docs/courses/precalculus/scope-and-sequence.md` ("For the lead") are sound:
1. **Progressions documents not yet in the source store:** Sound; keeping the ten Candidate Progressions checks at zero student days and flagging N-CN and N-VM as having no Progressions document is honest and accurate.
2. **Frame For the lead 5 (`calc-continuity` note):** Sound; rightly noted as a Calculus-row edit while Precalculus teaches both rows it names.

## Lens checklist (math, scope and sequence layer)

- **Every owned code taught in full (no partial standard left unfinished):** Met across all 58 owned codes, including every lettered part (`F-BF.B.4b` to `4d`, `N-VM.B.4a` to `4c`, `N-VM.B.5a` to `5b`).
- **Problems join units on purpose:** Met (for example, day 121 joining Unit 5's trig equations with Unit 8's polar curves; day 124 comparing polar complex multiplication with Unit 7's rotation matrix; day 155 road-to-calculus set joining Units 2, 3, and 10; extended tasks on checks 1, 2, and 3).
- **Fluency given spaced, mixed, untimed practice and direct year-end sampling:** Met (rational expressions from day 26, logarithm rules from day 37, exact trig values from day 53, identities from day 76, completing the square from day 20, kept in daily 5-minute openings; direct untimed fluency station on day 158).
- **Modeling cycle kept whole:** Met across Units 3, 6, 7, and 8 (and compact cycle for `F-TF.B.7` on day 63).
- **Language goals and eight practices (`RUBRIC-MATH-HS.md` gap 4 and gap 9):** Met at scope level (language goals stated for every section with explicit progression toward independence across units 1 to 10; all 8 practices mapped to specific task days).
- **Shorter path:** Met (45-minute period guidance + 10 non-overlapping fold-in days saving 500 minutes / 10 days, first five matching the senior early-end order).
- **Candidate cells settled:** Met (all 10 Progressions checks kept at zero student days; extensions explicitly kept or dropped with reasons).

## Fact and mathematical checks

- **Carbon-14 half-life of about 5,730 years (day 39):** Verified (Cambridge half-life 5,730 years; see Sources). Accurate.
- **Yellowstone gray wolf reintroduction 1995 to 2004 NPS annual reports (day 43):** Verified via [National Park Service](https://www.nps.gov/) (reintroduction began January 1995; NPS Yellowstone Wolf Project published annual reports including 2004). Accurate; unit plan checks whether the logistic fit is reasonable before locking the dataset.
- **Mathematical checks:** Logistic linearization $\ln(y / (L - y))$ against time (day 42), $r = 4\cos\theta$ as a circle (day 116), and $(-1 + \sqrt{3}\,i)^3 = 8$ (day 124) are all mathematically exact.
- **Other named sources not individually web-checked in this pass:** International standard atmosphere table (day 8), public star catalogue apparent magnitudes (day 40), NOAA tide predictions (day 63), planetary orbital distances fact sheet (day 137) (deferred to unit plans, not checked here).

## What is right and should not be touched

- **Language-goal progression and practice mapping:** Precalculus explicitly sets out how language supports fade across units 1 to 10 (sentence frames and word banks -> frames for new forms only -> spoken frames only) and pins every MP1 to MP8 practice to a concrete day, directly addressing `RUBRIC-MATH-HS.md` gaps 4 and 9.
- **Unit 6's two sittings with a targeted bridge opening (days 85 to 98):** Returning written feedback on day 87 and drawing day 89's opening from day 85's most-missed law-of-cosines items right before students use the law of cosines for vector resultants is smart classroom design.
- **Check 3 extended task (day 159):** Asking for instantaneous rate of change of height against time on a Unit 8 parametric path (from secant slopes of a table, explicitly never $dy/dx$ along the curve) tests `CUR-PC.15` in earlier-unit content without repeating Unit 10's sitting or encroaching on Calculus.

## What it could not judge

- Whether the 14.6 percent earlier-course minute estimate holds under the 15 percent cap once actual lesson task minutes are tallied in the unit plans (the margin is 27.5 minutes across the year, so unit plans must watch review minutes carefully).
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Remove all 37 `alg1-*`, `geo-*`, and `alg2-*` ids from `skills` on the 28 retrieval days (keep them in `note`) | `sequence-write.md` rule 2 restricts `skills` to the day's own unit so `unit_skeleton.py` does not misread earlier-grade rows as owned | `data/plans/precalculus/days.csv` |
| Remove stale `(For the lead 4)` and `(For the lead 3)` pointers on lines 65 and 85 | Those items no longer exist after the 2026-11-24 fix pass | `docs/courses/precalculus/scope-and-sequence.md` |
| Reword `the base text has no...` on days 24, 29, 95, 107, 125, and 134 | Complies with `sequence-write.md` rule 8 on `ours` days | `data/plans/precalculus/days.csv` |

## For Cory

None.

## Sources

- [National Park Service (nps.gov)](https://www.nps.gov/): verified Yellowstone gray wolf reintroduction beginning in January 1995 and NPS Yellowstone Wolf Project annual reports through 2004.
- Standard physical constant: carbon-14 half-life of approximately 5,730 years (Cambridge half-life, from memory / confirmed in search summary).
