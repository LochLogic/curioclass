# Fixes: scope and sequence of algebra-i, 2026-11-15

| Source | Applied | Not applied |
|---|---:|---:|
| Expert findings | 7 | 0 |
| Codex findings | 4 | 1 |
| Applicable lead calls | 12 | 0 |
| Applicable band items, consolidated | 6 | 0 |
| Own findings | 5 | 0 |
| **Total** | **34** | **1** |

Changed only the four owned files. Seven units, their order, ownership and allocations remain unchanged: 151 unit days plus nine course-level check/respond days, totaling 160. All six rows of the expert’s settled table were followed.

File abbreviations below:

- **Scope:** `docs/courses/algebra-i/scope-and-sequence.md`
- **Frame:** `docs/courses/algebra-i/frame.md`
- **Days:** `data/plans/algebra-i/days.csv`
- **Map:** `data/plans/algebra-i/source-map.csv`

## Applied

- **Expert 1:** Days 158–159, Scope check table: added independent linear solving, structural rewriting and quadratic/linear hand graphing. Day 158 reserves the specified ten-minute untimed station.
- **Expert 2:** Days 45, 82, 106, 129, 156 and 160, Scope: named begun codes, their taught parts, retained evidence and later completion; the handoff preserves partial records.
- **Expert 3:** Days 60–61, 108–109 and 158–160, Scope, Frame: narrowed fresh sampled codes, explicitly reused recent unit records without rescoring, changed days 109 and 159 forms, and removed false non-repeat boilerplate.
- **Expert 4:** Scope prerequisite inventory: replaced pending-map statements with verified grade 6–8 day evidence, preserving distinct histogram and dot/box histories.
- **Expert 5:** Days 34: added A-REI.B.3, explicitly limited to equations before inequality instruction.
- **Expert 6:** Map: converted all 294 rows to rule 8 columns, preserving prior notes, identifiers, optional-track information and URLs.
- **Expert 7:** Frame: removed tildes and comma-separated code lists. Owned-code cells now contain only owned codes; begun codes remain explicit in teaching descriptions.
- **Codex 1:** Days 158–159: included rational and letter coefficients with restrictions, independent inequality solving and explicit hand graphing.
- **Codex 2:** Days 14, 16, 50, 56 and 58, Scope: reserved individual three-display and scatter-plot construction records, association descriptions, and separate contextual slope/intercept responses.
- **Codex 4:** Days 10, 26 and 126, Scope, Frame: moved first square-root retrieval before standard deviation; distinguished principal roots, both equation solutions and contextual restrictions.
- **Codex 5:** Scope, Frame: reconciled obsolete readiness directions, available prerequisite records, conditional readiness windows and the counted shorter path.
- **Lead, Every subject 1:** Scope, Frame: applied the grade-number readiness rule through one verified prerequisite ledger.
- **Lead, Every subject 2:** Days, Scope: specified sampled parts, collection windows, reused records, response allocations and limits on extended tasks.
- **Lead, Every subject 3:** Map: applied the common layout and decision vocabulary; original course-level allocations remain explicitly outside units.
- **Lead, Every subject 4:** Scope: each shorter-year fold saves 50 minutes; ten folds reduce 160 meetings to 150, saving 500 minutes. The separate 40-minute path saves 400 minutes.
- **Lead, Every subject 5:** Days, Map: checked prose against public source purposes; supplied fresh source-goal summaries. Bibliographic titles remain identifiers.
- **Lead, Every subject 7:** Frame, Days: fluency remains untimed; timing allocations do not become student speed scores.
- **Lead, Math 1:** Frame: separated owned and begun codes without tildes or ownership changes.
- **Lead, Math 2:** Days 158–159, Scope: reserved direct fluency samples and preserved the limit on extended assessment tasks.
- **Lead, Math 3:** Scope, Frame: replaced competing focus counts with one stated instructional-minute allocation.
- **Lead, Math 4:** Days: added earlier-grade row IDs to retrieval placements.
- **Lead, Math 5:** Days, Scope: added named partial records and year-end samples of F-IF.B.4, F-BF.A.1a and F-LE.A.2.
- **Lead, Math 7:** Days, Map: checked source wording; no similarity flags above the screening threshold remained.
- **Band, direct fluency:** Days 158–159: applied the shared independent-performance correction.
- **Band, assessment claims and collection:** Days, Scope: narrowed course checks, varied forms and reused recent evidence.
- **Band, begun-code handoffs:** Days, Scope: recorded taught families while preserving later ownership.
- **Band, readiness history:** Scope, Frame: removed stale provisional directions and retained correct readiness placements.
- **Band, base fidelity and wording:** Map: retained all 132 main lessons in order and explained modeling-prompt departures.
- **Band, process consistency:** Scope, Frame, Map: aligned source layout, focus method, retrieval tags and code notation.
- **Own 1:** Days, Scope: made A-SSE.A.1a explicit and strengthened F-IF.B.4 feature/sketch and N-Q units/scale/precision reservations. Every taught code now appears on a named check after instruction.
- **Own 2:** Days, Scope: moved assessment evidence off foldable days 24, 71 and 96. All ten shorter-year folds remain unassessed practice.
- **Own 3:** Map: classified 128 optional support lessons as cut from the canonical calendar, preserving their optional availability and matching-core-day information.
- **Own 4:** Days, Scope: identified missing square-root assumptions for two progression rows; exact shared edits are below.
- **Own 5:** Days, Scope, Frame: aligned drawing-tool reservations, supplied a 40-minute year-end check allocation, and removed superseded focus and savings-extension directions.

## Not applied

- **Codex 3, move unit 1 readiness before its opening:** The expert preserves the after-hook placement, and the current binding brief explicitly requires that exception. Readiness remains in day 1’s final ten minutes; no opening day or calendar reallocation was made.

## Settled

| Judgment for DIGEST | Reuse |
|---|---|
| Begun standards carry named partial evidence | Record the family and taught parts; retain later ownership. |
| Recent unit records are reused without rescoring | Do not relist their codes as fresh course-check samples. |
| Removing tildes must preserve ownership | Put begun-code lists in teaching descriptions, outside owned-code cells. |
| Optional support lessons have no canonical day | Mark them cut from the core calendar while preserving optional-track metadata. |
| Shorter-year folds remain unassessed practice | Move evidence reservations to retained days before counting a fold. |
| Focus uses one minute allocation | Planned prerequisite share is 5,406.08 of 6,780 instructional minutes, 79.74 percent; no missing high school threshold is claimed. |

## For the structure pass

1. **`data/progressions/math.csv`, row `alg1-center-spread`, `assumes`:**  
   Old: `m7-compare-populations`  
   New: `m7-compare-populations; m8-roots`

2. **`data/progressions/math.csv`, row `alg1-rearrange-formulas`, `assumes`:**  
   Old: `m8-linear-equations`  
   New: `m8-linear-equations; m8-roots`

3. **`scripts/frame.py`, contribution-note check near lines 549–552:**  
   Old:
   ```python
   missing = sorted(c for c in contrib if c not in cell)
   ```
   New:
   ```python
   missing = sorted(c for c in contrib if c not in ' '.join(u.values()))
   ```
   In the following note, replace `name each as ~CODE in Owned standards` with `name each begun code in What students learn, with its later owner`. This aligns the informational check with the settled no-tilde rule.

4. **`data/plans/later.csv`, row `L25`, final description field:**  
   Old: `RUBRIC-MATH-K8 has only notes for Algebra I, Geometry and Algebra II (high school math expert reads, 2026-11-15). Write a short high school bar the unit plan writers and readers use.`  
   New: `RUBRIC-MATH-K8 contains no high school criteria. Write RUBRIC-MATH-HS before math unit plans, using the high school Publishers' Criteria and current high school review criteria; establish the prerequisite-cluster list, per-course instructional-minute focus method, coherence, rigor, modeling and assessment evidence.`

No unit counts, shared calendar dates or standard ownership edits are requested.

## For Cory

None.

## Gates

| Gate | Final result |
|---|---|
| `python -X utf8 scripts/sequence.py check algebra-i` | **0 failures**, exit 0; source-map layout passes. |
| `python -X utf8 scripts/frame.py check algebra-i` | **0 failures**, exit 0; six informational contribution notes request obsolete tilde syntax, addressed above. |
| `python -X utf8 scripts/frame.py calendar` | Exit 0; no stagger-rule break reported. Algebra I checks remain days 60–61, 108–109 and 158–159, weeks 12–13, 22 and 32. |

Additional verification found no premature fresh-code claims, no taught codes lacking a named check, and no em dashes in the four owned files. Exact assessment timing remains for unit writing, particularly the year-end station and embedded mid-unit days.
