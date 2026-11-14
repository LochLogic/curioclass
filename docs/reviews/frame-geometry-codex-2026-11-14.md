# Geometry course frame: independent review

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-geometry-2026-11-14.md`  
**Delivery:** Markdown below only. No report file or repository content was changed.

## Verdict

Geometry’s curricular soundness remains unjudged because the required full plan gate could not complete. Separate frame and progression checks pass, but they do not establish instructional coherence, complete standards coverage or adequate pacing. Restore the checking environment, correct the two verified stale notes below, and commission a fresh independent curriculum read after the prerequisite passes.

## What I read and checked

Read the expert instructions, mathematics lens, K to 8 mathematics rubric, Geometry frame, its `frames.csv` entry, its inline source map and all 28 grade 10 mathematics progression rows. Consulted the foundation, teaching approaches, source register, base-text policy, frame-writing brief, checking scripts, earlier mathematics progression reviews and portions of the neighboring Algebra I and Algebra II frames.

I opened curriculum files while investigating the failed checking environment. That exceeded the instruction in [EXPERT.md:105](S:/CurioClass/docs/agents/EXPERT.md:105): “If it fails, the plan goes back to its writer unread.” Consequently, this report records process findings and limited structural observations, without issuing curriculum approval.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default Python | Resolves to the installed office-suite interpreter |
| `python -B -X utf8 scripts/frame.py check geometry` | Zero failures; 8 units, 160 days, comprising 151 unit days and 9 check and respond days |
| `python -B -X utf8 scripts/frame.py check` | Exit 0 |
| `python -B -X utf8 scripts/progression.py check math` | 305 rows, zero failures; advisory notes remain |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures |

The requested `data/plans/geometry/source-map.csv` does not exist. The [frame-writing brief](S:/CurioClass/docs/pipeline/briefs/frame-write.md) explicitly schedules that day-level file for the scope and sequence stage. Its absence alone is therefore not a frame defect.

No dependency installation, checker modification, turn mutation, defect-ledger write or report-file write was attempted.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** [scripts/lesson.py:15](S:/CurioClass/scripts/lesson.py:15), imported during the full plan check.

**What is wrong:** The available default interpreter cannot import `markdown`. The command terminates before producing a complete gate result. This is an execution-environment failure, not evidence of a Geometry curriculum defect.

**Why it matters:** The expert procedure requires a passing prerequisite before the curriculum read proceeds. Successful frame and progression checks cannot substitute for the unfinished full check.

**Exact fix:** Configure the review runner to use an accessible Python environment containing the required dependencies, including Python-Markdown. Run the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any failures it reports, then commission a fresh independent Geometry frame read.

**Earlier occurrence:** [Grade 8 mathematics frame review, finding 1](S:/CurioClass/docs/reviews/frame-math-grade-8-codex-2026-11-14.md).

### 2. The stitch report still says the nonlinear inverse contribution is absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** [progression-math-stitch-2026-11-13.md:62](S:/CurioClass/docs/reviews/progression-math-stitch-2026-11-13.md:62), item 20.

**What is wrong:** The note says `alg2-rational-exponents` has neither `~F-BF.B.4a` nor the proposed applying-day note. Its current progression row contains both. The [reconcile report:77](S:/CurioClass/docs/reviews/progression-math-reconcile-2026-11-13.md:77) also records completion.

**Why it matters:** A later writer could treat completed work as an outstanding change, duplicating instruction or reopening an already resolved ownership decision.

**Exact fix:** Replace the outstanding-work wording in the Pick cell with:

> Completed in the reconcile: `alg2-rational-exponents` carries `~F-BF.B.4a`, assumes `alg1-inverse-functions`, and names one applying day on nonlinear inverses using cube roots. Ownership remains with `alg1-inverse-functions`.

Preserve the historical record without presenting the action as still pending.

**Earlier occurrence:** Same stale completion-note category as findings 2 and 3 in the Grade 8 mathematics frame review.

### 3. The stitch report still says two Geometry rows have no prerequisites

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** [progression-math-stitch-2026-11-13.md:73](S:/CurioClass/docs/reviews/progression-math-stitch-2026-11-13.md:73).

**What is wrong:** The note groups `geo-constructions`, `geo-inscribed-circumscribed` and `geo-addition-rule` as assuming nothing. Currently:

- `geo-constructions` assumes `m7-triangle-conditions`.
- `geo-addition-rule` assumes `alg1-two-way-tables`.
- `geo-inscribed-circumscribed` retains an empty `assumes` field.

The [progression fix report:13](S:/CurioClass/docs/reviews/progression-math-fixes-2026-11-13.md:13) records the first two corrections.

**Why it matters:** The old note contradicts the current prerequisite contract and could encourage removal or neglect of the repaired handoffs.

**Exact fix:** Replace the two-line note with:

> Updated after the progression reads: `geo-constructions` assumes `m7-triangle-conditions`, and `geo-addition-rule` assumes `alg1-two-way-tables`. `geo-inscribed-circumscribed` retains no earlier-grade prerequisite in its `assumes` field.

**Earlier occurrence:** Same stale completion-note category as finding 2.

## Coverage and limits

| Required review area | Status |
|---|---|
| Owned skills placed exactly once | Frame placement check passes for the 28 rows |
| Earlier-grade skills appropriately marked as review or extension | Substantive judgment withheld |
| Every owned standard taught in full | Not established |
| Unit reasons and prerequisite order | Not established |
| Annual day arithmetic | 151 unit days plus 9 course-level days equals 160 |
| Days appropriate to instructional load | Not established |
| Source map | Inline map exists; complete source comparison not finished |
| Incoming and outgoing seams | Not established |
| Cross-subject teaching order | Not established |
| Marked stale notes | Checker passes within its 56-file scope |
| Unmarked stale notes | Findings 2 and 3 verified; search incomplete |

The stale checker’s default scope excludes `docs/reviews/`, which explains why it did not catch the two historical review notes above.

## Mathematics lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Major work receives the required share of units, days and time | Not judged |
| Supporting work practises major work | Not judged |
| Source-map rows carry explicit decisions | Met structurally in the inline map; substantive source fidelity unjudged |
| High school criteria used before judging the frame | Incomplete; outside criteria opened, full review withheld |

Other lens checklists belong to progression, scope and sequence, unit or day reviews. They were not scored here.

## What is right and should be preserved

Preserve the explicit separation between 151 unit days and nine course-level check and respond days. Preserve the inline source map’s explicit decisions and the distinction between adapted base lessons and assessments written by Curio Class. These are useful planning structures, although their instructional adequacy remains unjudged.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Do not flag the missing day-level source-map CSV as a frame defect | The frame-writing brief assigns it to the next planning stage | None |
| Rewrite the two stale notes to reflect completed work | Current progression data and subsequent reports establish completion | `docs/reviews/progression-math-stitch-2026-11-13.md` |
| Make no curriculum or ownership changes from this run | The required prerequisite did not complete | None |

## Sources and memory limits

Preliminary outside research opened:

- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf), for the high school focus requirement.
- [Official Geometry standards](https://www.thecorestandards.org/Math/Content/HSG/), [quantity standards](https://www.thecorestandards.org/Math/Content/HSN/Q/) and [conditional probability standards](https://www.thecorestandards.org/Math/Content/HSS/CP/), for full standard wording.
- [Base-text course narrative](https://im.kendallhunt.com/HS/teachers/2/narrative.html), [scope and sequence](https://im.kendallhunt.com/HS/teachers/2/scope_and_sequence.html) and [lesson-standard map](https://im.kendallhunt.com/HS/teachers/2/lessons_and_standards.html), for intended progression and placement.
- [New York’s archived high school curriculum overview](https://www.nysedregents.org/engageny/a-story-of-functions-curriculum-map-and-overview.pdf), for a second curriculum sequence.
- [Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf), for research guidance.

The [compiled Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf) exceeded the browsing tool’s size limit. Outside-source comparison was not completed, and no curriculum finding rests on these preliminary reads.

Prior session memory informed report structure only. Every finding above was checked against current files or current command output.

## For Cory

None. This report requests no scope, money, people or audience decision.

## For the source list

The high school publishers’ criteria link above is useful for the missing high school bar. The archived New York overview provides an accessible second curriculum sequence; it remains reference material.

**Verdict:** Review blocked; curriculum unjudged. **Finding count:** 3. **Intended report path:** `docs/reviews/frame-geometry-2026-11-14.md`, supplied here only.

