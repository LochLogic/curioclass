# Fixes: scope and sequence of algebra-ii, 2026-11-15

Counts cover applicable finding groups. Partly applied findings appear in both columns.

| Source | Applied | Not applied |
|---|---:|---:|
| Expert | 5 | 1 subpart |
| Codex | 4 | 2 |
| Lead calls | 11 | 0 |
| Band items | 8 | 0 |
| Own findings | 6 | 0 |

Only the four authorized files changed. Seven units, their order, ownership, allocations and the 160-day total remain unchanged.

## Applied

- **Expert 1:** days.csv and scope-and-sequence.md: narrowed course-level code lists; reused days 68, 107–108 and 155–156; bounded day 158 to its periodic model, direct fluency station and named feature responses.
- **Expert 2:** scope-and-sequence.md, frame.md and days.csv: verified Geometry handoffs, removed provisional claims, dropped completing-square readiness and placed retrieval before complex quadratics.
- **Expert 3:** day 106 and source-map.csv: replaced the close paraphrase with a cooling-model purpose; retained arithmetic combinations and domain limits.
- **Expert 4:** day 135 and scope-and-sequence.md: tagged retrieved rows, distinguished earlier-course panels from fresh child-code claims, and retained distributed parent F-IF.C.7 evidence.
- **Expert 5:** frame.md: removed tilde notation and placed contributions outside Owned standards. Remaining obsolete gate advice is listed for the structure pass.

- **Codex 1:** assessment rows and narrative: added solve-and-write inverses on day 68, narrowed day 107, assigned complete feature evidence to day 135, and separated experimental evidence from sampling/study-type evidence.
- **Codex 2, partly:** prerequisite ledger and days 45–46: verified Geometry evidence, removed completing-square readiness, and added integer-exponent readiness.
- **Codex 4:** days.csv, scope-and-sequence.md and frame.md: replaced unresolved focus estimates with explicit planned-minute allocations. Focus is **4,190/6,500 minutes, 64.46 percent**, using the [published high school prerequisite table](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf).
- **Codex 5:** frame.md and days 32–33: reconciled readiness directions, required supplied anonymous outcomes without pulse collection, and made midpoint response replace the usual warm-up.

- **Lead, Every subject 1:** frame and prerequisite ledger use grade-number counting and actual teaching/assessment evidence.
- **Lead, Every subject 2:** assessment reservations identify sampled parts, reused records, response time and concurrent work for 30 students.
- **Lead, Every subject 3:** source-map.csv uses the required eleven-column layout, including URL.
- **Lead, Every subject 4:** shorter-path table gives ten named folds, 50 minutes saved each, totaling 500 minutes and 150 meetings.
- **Lead, Every subject 5:** checked wording against public source goals; rewrote close wording in goals and source metadata.
- **Lead, Math 1:** frame separates owned codes from contributions, with semicolon delimiters and no tildes.
- **Lead, Math 2:** end days reserve at most one extended performance; day 158 directly samples all four fluency expectations.
- **Lead, Math 3:** focus counts substantive minutes once, excluding assessment and respond days.
- **Lead, Math 4:** earlier-grade retrievals carry row ids in skills.
- **Lead, Math 5:** recent high school records are reused; completing-square readiness is removed.
- **Lead, Math 7:** source purposes and adaptation choices use fresh wording.

- **Band 1, direct fluency:** retained and budgeted the independent, untimed day 158 station.
- **Band 2, overclaim/Collect once:** narrowed fresh assessment claims and named retained records.
- **Band 3, begun codes:** added local records for sequence construction, rational-equation reasoning, and polynomial/exponential graph features; ownership remains unchanged.
- **Band 4, readiness:** replaced stale last-use claims and kept retrieval distinct from assessment evidence.
- **Band 5, source fidelity:** retained all 120 lessons in order and all eight public prompts, with adaptation reasons.
- **Band 6, process drift:** standardized source-map fields, minute counting, retrieval tags and frame code presentation.
- **Band 7, task forms:** preserved model construction and recommendation forms alongside audits and sorts.
- **Band 8, performance load:** documented one extended performance per end day, retained products and class-size-30 evidence arrangements.

- **Own 1:** day 14, frame and ledger: added inspection/factoring readiness before quadratic-equation reasoning first used on day 20.
- **Own 2:** scope-and-sequence.md and days 35/44: added part-specific evidence reservations, including the complicated rational-rewrite technology requirement and printed trace route.
- **Own 3:** days 34, 81 and 150, plus source metadata: rewrote additional close mathematical phrasing.
- **Own 4:** source-map.csv: distinguished source goals from adaptation goals; documented deferred complex-plane illustrations and both modeling-prompt order departures.
- **Own 5:** days.csv: completed generic drawn-tool and calculator specifications with paper routes; retained supplies and empty math safety cells.
- **Own 6:** frame and scope: closed the catalogue-id question using the existing frames.csv mapping; added prior-year Chemistry/ELA ledger entries and retrieval tags.

## Not applied

- **Expert 2, piecewise subpart:** did not retain grade 9 as its last assessment use. Current Geometry day 101 explicitly assesses piecewise and absolute-value cases. That record supports retrieval on Algebra II day 96.
- **Codex 2, function notation and inverses:** did not change these to grade 10 retrieval classifications. Geometry days 86 and 106 retrieve them without establishing fresh full-row teaching or assessment. The expert’s strict last-use ruling controls.
- **Codex 3:** did not add a separate opening assessment allocation. The current binding brief permits Unit 1 readiness in day 1’s final ten minutes after the hook; the expert accepts that placement.

## Settled

| Judgment | Reuse in later writing |
|---|---|
| Last use | Retrieval alone does not reset last use; explicit teaching or assessment does. |
| Geometry exceptions | Completing the square and the currently assessed piecewise/absolute-value cases receive retrieval. |
| Integer exponents | Day 45 checks zero, negative and combined powers before extension. |
| Course-level evidence | Fresh code lists exclude recently retained unit records. |
| Begun standards | Record the taught part locally; preserve eventual ownership and completion. |
| F-IF.C.7 | Distributed family evidence closes the parent; part d remains assessed in unit 2 only. |
| Source map | 120 lessons, eight prompts, 33 original rows; source goals and adaptation choices remain distinct. |
| Shorter route | Ten folds save 500 minutes; assessment and response reservations remain. |
| Identifiers | Keep course `algebra-ii` and catalogue id `algebra-2` in their mapped roles. |

## For the structure pass

1. **data/progressions/math.csv, notes, all 22 grade-11 rows containing this sentence**

   Old:
   `Skips grade 10 on purpose: Geometry carries no algebra or functions unit, so Algebra II builds on Algebra I directly (IM course order Algebra I, Geometry, Algebra II).`

   New:
   `Algebra II builds on Algebra I across Geometry. Actual Geometry teaching and assessment can renew an earlier row; the verified Algebra II prerequisite ledger determines readiness or retrieval.`

2. **data/progressions/math.csv, notes, all 22 grade-11 rows containing this prefix**

   Old:
   `Re-entry (recall required): open with a short readiness check on `

   New:
   `Re-entry: the verified Algebra II scope-and-sequence ledger sets readiness or retrieval for `

   Preserve the following row-id list and support sentence.

3. **data/progressions/math.csv, alg2-rational-exponents, assumes**

   Old:
   `geo-scaling-area-volume; alg1-rational-irrational; alg1-inverse-functions`

   New:
   `geo-scaling-area-volume; alg1-rational-irrational; alg1-inverse-functions; m8-integer-exponents`

4. **data/progressions/math.csv, alg2-experiments-significance, notes**

   Old:
   `Teacher note: experiments about health (heart rates, caffeine) use class-safe activities only; no student shares medical information.`

   New:
   `Teacher note: health-study examples use supplied anonymous outcomes only; no pulse collection or student health disclosure.`

5. **scripts/frame.py, lines 549–552, contribution-note logic**

   Old:
   `missing = sorted(c for c in contrib if c not in cell)`

   New:
   `missing = sorted(c for c in contrib if c not in ' '.join(u.values()))`

   Replace message text `name each as ~CODE in Owned standards` with `name each in What students learn`.

6. **docs/RUBRIC-MATH-HS.md**

   Old: file absent.

   New: file the high school bar, including the published prerequisite table, instructional-minute method, direct fluency evidence, begun-part records and distributed parent-code convention. The existing K–8 rubric contains no high school notes.

No calendar, frames.csv, ownership or catalogue-id edit is needed.

## For Cory

None.

## Gates

| Gate | Final result |
|---|---|
| `python -X utf8 scripts/sequence.py check algebra-ii` | Exit 0; **0 failures**, including source-map layout. |
| `python -X utf8 scripts/frame.py check algebra-ii` | Exit 0; **0 failures**. Five advisory contribution notes still request obsolete tilde notation; exact shared-script fix listed above. |
| `python -X utf8 scripts/frame.py calendar` | Exit 0. Algebra II does **not** break the high school stagger rule. Checks remain days 70–71, 110–111 and 158–159, with response on 72, 112 and 160. |

Actual item durations, especially day 31 and the shorter-period route, remain for unit planning to verify.
