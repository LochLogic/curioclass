# Cold read: Calculus scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-calculus-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-calculus-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `calculus` (grade 12, math core elective, full year, 160 course days)
**Subject:** math
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/math.md`, `docs/RUBRIC-MATH-HS.md`
- `docs/courses/calculus/frame.md`, `docs/courses/calculus/scope-and-sequence.md`
- `data/plans/calculus/days.csv`, `data/plans/calculus/source-map.csv`
- `data/standards/curio-math-electives.txt` (`CUR-CA.1` to `CUR-CA.30`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I verified all gate subjects directly against `days.csv`, `source-map.csv`, `curio-math-electives.txt`, and `CALENDAR.md`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 11: 14, 22, 14, 15, 16, 9, 9, 17, 10, 12, 13 = 151 unit days, plus 9 `C` days = 160).
- **Kinds:** 93 Understanding, 20 Application, 16 Fluency, 17 Check, 14 Respond. Every Fluency day practices only procedures taught on earlier days, introduces no new code, and drafts, revises, or edits no writing.
- **Owned standards:** All 31 owned codes (`CUR-CA.1` to `CUR-CA.30` plus `G-GMD.A.2`) are taught before being assessed and appear on an `end` assessment day.
- **Math columns (`tools`, `supplies`, `safety`):** `safety` is blank on every row as required for math; `tools` and `supplies` are well-formed semicolon-separated lists.
- **Source map:** Every course day 1 to 160 is mapped in `data/plans/calculus/source-map.csv` (zero unmapped days).
- **Assessments and calendar:** Every unit has an end-of-unit sitting on its second-last day and a Respond day on its last, counted once. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 82 to 83 (week 17, respond day 84), 120 to 121 (weeks 24 to 25, respond day 122), and 158 to 159 (week 32, finals week, respond day 160), matching `CALENDAR.md`.
- **15 percent earlier-course cap (`RUBRIC-MATH-HS.md`):** Counted at most 745 minutes of 7,550 unit minutes (9.9 percent), well under the 15 percent cap (1,132.5 minutes).

## Verdict

The Calculus scope and sequence is mathematically tight, logically ordered, and well aligned with `RUBRIC-MATH-HS.md` and the math lens, with clean repairs already applied to Unit 2's derivative-rule sequence, Unit 7's modeling-revision timing, and the non-repeating course-level check forms. Its main remaining defect is placing 17 earlier-grade retrieval skill ids (`alg1-*`, `geo-*`, `alg2-*`) inside the `skills` column of `days.csv`, which `sequence-write.md` forbids because the unit skeleton reads any id in `skills` as owned by that unit. Removing those ids from `skills` (they are already named in `note`) and cleaning up two minor `note` wordings will make the scope ready for unit planning.

## Findings

### 1. Earlier-grade retrieval skill ids are placed in `days.csv` `skills` on 17 days

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Seventeen rows of `data/plans/calculus/days.csv` include earlier-grade retrieval ids (`alg1-*`, `geo-*`, `alg2-*`) in the `skills` column alongside the unit's `calc-*` skill: days 5 (`alg2-rational-functions`), 15 (`alg1-graph-features-rates`), 22 (`alg2-trig-functions-graphs`), 23 (`alg2-number-e-continuous`), 28 (`alg2-exp-log-graphs`), 31 (`geo-circle-parabola-equations`), 41 (`geo-solving-right-triangles`), 59 (`alg2-rational-functions`), 86 (`alg2-polynomial-division-remainder`), 96 (`alg2-sequences`), 97 (`alg2-number-e-continuous; alg2-logarithms`), 108 (`alg2-exp-log-graphs`), 111 (`geo-volume-formulas`), 116 (`geo-arcs-sectors-radians`), 129 (`geo-arcs-sectors-radians`), 134 (`alg2-geometric-series`), and 145 (`alg2-polynomial-arithmetic`).
- **Why it matters:** `sequence-write.md` rule 2 states explicitly: "`skills` holds only what the day's own unit works on, because the skeleton reads an earlier-grade id in `skills` as a row of the day's own unit." Every one of these 17 days already names its retrieval row id in `note`, so keeping it in `skills` risks polluting generated unit skeletons.
- **Exact fix:** Remove all `alg1-*`, `geo-*`, and `alg2-*` ids from the `skills` column on those 17 days in `data/plans/calculus/days.csv`, leaving them in `note` only.

### 2. Two `ours` days carry the word `base` in their `note`

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Days 23 and 74 are `ours` days (no base lesson adapted), but their `note` cells read `Ours (base CC 2.3 is not in the store)` and `Ours (base CC 8.7 has no archive copy)`.
- **Why it matters:** `sequence-write.md` rule 8 states: `Days that adapt no base lesson never carry "Base" in their goal or note.` Even in lower case, the word invites a false-positive gate or writer check.
- **Exact fix:** Reword day 23's note to `Ours (CC 2.3 is not in the store)` and day 74's note to `Ours (CC 8.7 has no archive copy)` in `data/plans/calculus/days.csv`.

### 3. Minor discrepancy between `frame.md` and `scope-and-sequence.md` on the senior early-end trim count for improper integrals

- **LAYER:** frame
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** `frame.md` ("A tight course" and "Grade 12 calendar") describes the first trim step as "improper integrals (unit 6) from 3 days to 1 and arc length (unit 8) from 2 days to 1... saving 3 days." In `days.csv`, `calc-improper-integrals` has two teaching days (days 90 and 91, with days 92 and 93 as the unit sitting and respond day), so folding day 91 into day 90 saves 1 day, not 2. `scope-and-sequence.md`'s Shorter path table handles this correctly by adding day 7 (choosing a rewrite for 0/0 limits) as the fifth senior fold-in day (days 91, 117, 142, 2, 7), but `frame.md` still states "from 3 days to 1... saving 3 days."
- **Why it matters:** A teacher or unit writer reading `frame.md` will look for a third improper-integrals teaching day that does not exist in `days.csv`.
- **Exact fix:** Update `frame.md` ("A tight course" and "Grade 12 calendar") when next edited to say "improper integrals (unit 6) from 2 days to 1 and arc length (unit 8) from 2 days to 1, saving 2 days" and include day 7 as the fifth senior fold-in day.

## Judgment of "For the lead" items

All five items in `docs/courses/calculus/scope-and-sequence.md` ("For the lead") are marked closed and verified sound:
1. **Base CC 2.3 missing from CC BY store (days 22 to 23 ours, 2.3 marked cut):** Sound.
2. **Archive numbering synced with `frame.md`; 8.6, 8.7, and 5.5 absent from archive:** Sound.
3. **Accelerated path route and seven expected core-count rule 2 notes:** Sound and clearly documented in both `frame.md` and `scope-and-sequence.md`.
4. **Course-level check day 1 non-repeating task forms (critique and correct, choose between claims, sort and justify) while day 158 fluency station stays direct:** Sound; satisfies `sequence-write.md` rules 2 and 3.
5. **Unit 7 reordered (cooling model drafted day 98, revised day 100, day 102 respond only):** Verified against `days.csv` days 94 to 102; sound.

## Lens checklist (math, scope and sequence layer)

- **Every owned code taught in full (no partial standard left unfinished):** Met across all 31 owned codes (`CUR-CA.1` to `CUR-CA.30` and `G-GMD.A.2`). Unit 2's derivative-rule order (days 20 to 30) and Unit 7's differential-equation order (days 94 to 102) have zero forward dependencies.
- **Problems join units on purpose:** Met (for example, day 111 to 114 joining Geometry and integration for the sphere and spherical ring; day 155 joining units 5, 10, and 11 to approximate a non-elementary definite integral with a series and alternating error bound; extended tasks on checks 1, 2, and 3).
- **Fluency given spaced, mixed, untimed practice and direct year-end sampling:** Met (differentiation rules from day 24, antiderivatives and substitution from day 79, choosing an integration method from day 90, kept in daily 5-minute openings; untimed rules station on day 35; direct untimed fluency station on day 158).
- **Modeling cycle kept whole (no step cut):** Met across Units 3, 4, 7, and 8 (draft, at least two nights for written feedback, validation against a new instant/constraint/reading, and revision on a dedicated Application day).
- **Shorter path:** Met (45-minute period guidance + 10 named fold-in days saving 500 minutes / 10 days, with no assessed, feedback, revision, or respond day cut).
- **Candidate cells settled:** Met (all 11 unit candidates kept with 0 added days; all extensions kept strictly as extensions).

## Fact and mathematical checks

- No dated historical events or external statistical datasets are cited in `days.csv` (all contexts are labeled invented for practice; half-lives are deferred to the National Nuclear Data Center at unit-plan stage, not checked here).
- Mathematical claims verified: $\lim_{h\to 0}(\cos h - 1)/h$ derived from $\lim_{h\to 0}(\sin h)/h$ (day 22); $1/x$ vs $1/x^2$ swapping convergence on $[1,\infty)$ and $(0,1]$ (days 90 and 91); logistic fastest growth at $P = K/2$ (day 99); Cavalieri's principle hemisphere vs cylinder minus cone (day 111); circle arc length integrated on $[0, r/2]$ to avoid the vertical tangent at $x = r$ (day 116). All accurate.

## What is right and should not be touched

- **Unit 2 rule sequence (days 20 to 30):** Teaching $\ln x$ slope graphically on day 23, then proving $(\ln x)' = 1/x$ from $e^{\ln x} = x$ after the chain rule on day 28, and finishing $b^x$ and $\log_b x$ on day 30 is mathematically airtight.
- **Day 89 typed Application (not Fluency):** Choosing an integration method from the form of the integrand is a first-taught clause of `CUR-CA.17`, so typing day 89 Application and putting method-choice into daily openings from day 90 respects `GLOSSARY.md` cleanly.
- **Day 158 direct fluency station:** Keeping the year-end fluency station direct and untimed (with no supplied work and never inside a critique) while using critique/sort/choose forms for the other short items satisfies both `RUBRIC-MATH-HS.md` 2b and `sequence-write.md` rules 2 and 3.

## What it could not judge

- Lesson-level problem quality, pacing inside dense single days (such as day 22 covering sine, cosine, all other trig derivatives, and special-angle values), and multilingual-learner language goals (flagged in `RUBRIC-MATH-HS.md` gap 9 for unit plans).
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Remove all `alg1-*`, `geo-*`, and `alg2-*` ids from `skills` on the 17 retrieval days (keep them in `note`) | `sequence-write.md` rule 2 restricts `skills` to the day's own unit so `unit_skeleton.py` does not misread earlier-grade rows as owned | `data/plans/calculus/days.csv` |
| Remove the word `base` from `ours` day notes on days 23 and 74 | Complies with `sequence-write.md` rule 8 | `data/plans/calculus/days.csv` |
| Note `frame.md` improper-integrals trim count as 2 days to 1 (not 3 to 1) when next edited | Aligns `frame.md` with `days.csv` (days 90 and 91) and `scope-and-sequence.md` | `docs/courses/calculus/frame.md` |

## For Cory

None.

## Sources

- Repository standards and rubric documents only (`docs/RUBRIC-MATH-HS.md`, `docs/agents/lenses/math.md`, `data/standards/curio-math-electives.txt`); no outside factual or statistical datasets are cited in `calculus/days.csv`.
