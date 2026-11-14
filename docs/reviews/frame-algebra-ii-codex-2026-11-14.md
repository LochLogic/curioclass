# Algebra II course frame review, 2026-11-14

Intended report path: `docs/reviews/frame-algebra-ii-2026-11-14.md`

Delivered here only. No file was created, edited or deleted.

## Verdict

The curriculum verdict is withheld because the required full plan check could not complete. Separate frame and progression checks pass, establishing skill placement, owned-code correspondence and day totals within their scope. Restore the checking environment and obtain a passing full gate before completing the independent curriculum read.

## What I read and checked

Read the expert instructions, mathematics lens, K to 8 mathematics rubric, complete Algebra II frame, its `frames.csv` entry and all 26 grade 11 mathematics progression rows.

Also consulted the foundation, teaching approaches, source register, base-text policy, glossary, frame-writing brief, relevant standards text, checking scripts, earlier mathematics reviews, portions of the Algebra I and Geometry frames, and selected cross-subject frame entries. Preliminary base-text reading included the course narrative, source inventory and selected unit and lesson descriptions.

I continued preliminary reading after the runtime failure. That did not satisfy the expert’s required sequence, so this report makes no substantive judgment about curricular soundness.

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py check algebra-ii` | Zero failures; 7 units, 160 days |
| `python -X utf8 scripts/progression.py check math` | 305 rows, zero failures; advisory notes remain |
| `python -X utf8 scripts/stale.py check` | 56 files checked, zero failures |

The available `python` resolves to the office-suite interpreter. Checks of existing interpreter and package locations did not locate an accessible environment containing the missing dependency.

The requested `data/plans/algebra-ii/source-map.csv` does not exist. The frame-writing brief explicitly assigns that day-level file to the later scope and sequence stage. Its absence is therefore **not a frame finding**; the current frame supplies unit-level source-map tables.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly reproduced

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`.

**What is wrong:** The available Python cannot import `markdown`. The full command terminates before producing a complete result. This establishes an environment failure, not a curriculum failure.

**Why it matters:** [EXPERT.md](S:/CurioClass/docs/agents/EXPERT.md) requires: “If it fails, the plan goes back to its writer unread.” The separate checks cannot replace that prerequisite or establish full standards coverage, coherent instruction or adequate pacing.

**Exact fix:** Configure the review runner to use an accessible Python environment containing the repository’s required dependencies, including Python-Markdown. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any reported failures, then commission the complete independent Algebra II read. Do not substitute a stub module or modify checker behavior.

**Earlier occurrence:** [Grade 8 mathematics frame review, finding 1](S:/CurioClass/docs/reviews/frame-math-grade-8-codex-2026-11-14.md). That environment issue remains unresolved here.

### 2. The progression stitch still says the nonlinear-inverse contribution has not been added

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly verified

**Location:** [Mathematics progression stitch, item 20](S:/CurioClass/docs/reviews/progression-math-stitch-2026-11-13.md:62).

**What is wrong:** Item 20 says the applying day is “not yet on” `alg2-rational-exponents`, with neither a standard contribution nor a note. The current row contains `~F-BF.B.4a` and explicitly describes the nonlinear-inverse applying day. Algebra II unit 3 also allocates that day.

**Why it matters:** The note can send a fixer back to completed work or prompt a duplicate day allocation.

**Exact fix:** Preserve the historical decision and replace the outstanding-work wording with:

> Implemented in `data/progressions/math.csv`, `alg2-rational-exponents`: the row carries `~F-BF.B.4a` and describes one applying day on cube roots undoing cubing. Algebra II frame unit 3 allocates that day. Ownership remains with `alg1-inverse-functions`.

This records placement only, without claiming that a lesson has been written.

**Earlier occurrence:** Stale completion and placement notes are the same finding type identified in [the Grade 8 mathematics frame review](S:/CurioClass/docs/reviews/frame-math-grade-8-codex-2026-11-14.md). The specific stitch note remains uncorrected.

## Required review coverage

| Requirement | Verified result or remaining limit |
|---|---|
| Every owned skill placed exactly once | Structural frame check passes for all 26 Algebra II rows |
| Other-grade skills explicitly treated as review or extension | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| Course days fit the year | Structural total passes: 151 unit days plus 9 check and respond days equals 160 |
| Each unit’s days fit its instructional load | Not adjudicated |
| Complete base-lesson placement, order and licensing | Inline map inspected; substantive verification incomplete |
| Incoming seams | Algebra I and Geometry consulted; complete seam judgment withheld |
| Outgoing seams | No Precalculus, Statistics or Calculus frame was found; the target records proposed elective handoffs |
| Cross-subject availability | Selected entries inspected; complete availability judgment withheld |
| Marked stale notes | Checker reports zero failures within its scope |
| Unmarked stale notes | Finding 2 verified; search incomplete |

## Mathematics lens checklist, course frame layer

| Checklist line | Disposition |
|---|---|
| Major work meets the applicable line by units, days and instructional time | Unresolved pending the prerequisite and high-school criteria analysis |
| Supporting clusters practise major work | Unresolved pending the complete curriculum read |
| Every source-map row has a keep, split, merge, cut or ours decision | Inline dispositions present; completeness and fidelity not adjudicated |

The unresolved lines cannot honestly be marked met, missed or not applicable as curriculum conclusions. The K to 8 percentage threshold also needs explicit reconciliation with the high-school criteria before use here.

## What is right and should not be touched

Preserve the passing structural results: seven units, all 26 owned skills placed once, owned-code correspondence and the 160-day total.

Retain the distinction between the frame’s unit-level source map and the later day-level CSV. Do not create an extra frame defect from that scheduled distinction.

## Settled by the expert

| Choice | Reason | File or action affected |
|---|---|---|
| Withhold the curriculum verdict | The mandatory full check has no completed result | This report |
| Retain separate checks as limited structural evidence | Their results are valid within their stated scope | This report |
| Do not flag the absent source-map CSV | The frame-writing brief schedules it for the next layer | None |
| Replace stitch item 20’s outstanding-work claim | The current row and frame already record the contribution | `docs/reviews/progression-math-stitch-2026-11-13.md` |
| Settle no mathematical or pacing changes | The substantive review remains incomplete | None |

## Outside sources and limits

Preliminary research reached these sources:

- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): high-school focus, coherence and widely applicable prerequisites.
- [High School Mathematics Review Criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): the high-school review framework.
- [Base-text Algebra II narrative](https://im.kendallhunt.com/HS/teachers/3/narrative.html): unit dependencies and course design.
- [Comparison Algebra II sequence](https://www.fishtanklearning.org/curriculum/math/algebra-2/): an alternative sequence for comparison.
- [Federal algebra practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/20): recommendations concerning worked solutions, algebraic structure and strategy choice.

The [compiled Mathematics Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf) exceeded the web tool’s retrieval limit. Outside research was incomplete and supports no curriculum verdict here. No finding rests on memory.

### For the source list

Add the reachable high-school publishers’ criteria and high-school review-criteria links above if they are not already recorded.

## For Cory

None arising from the verified findings. No scope, money, people or audience decision is needed to correct the environment or stale note.

**Verdict:** Curriculum unjudged pending the full gate. **Finding count:** 2 process findings, including 1 blocker. **Report path:** `docs/reviews/frame-algebra-ii-2026-11-14.md`, supplied here only.