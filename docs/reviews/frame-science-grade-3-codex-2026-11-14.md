# Science Grade 3 frame review, 2026-11-14

Intended report path: `docs/reviews/frame-science-grade-3-2026-11-14.md`

## Verdict

The frame’s soundness is unjudged because the required plan gate could not complete. The blocking issue is a missing Python dependency, which prevents establishing the prerequisite check result. Restore a working check environment and rerun the gate before conducting the cold read.

## What I read and ran

Read [EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md) and the [science lens](/S:/CurioClass/docs/agents/lenses/science.md), and inspected the science rubric and relevant checker code.

Commands:

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternative Python launcher | Could not launch its interpreter: permission denied |
| `python -X utf8 scripts/stale.py check` | Exit 0: 37 files checked, 0 failures |

The expert instructions explicitly say: “If it fails, the plan goes back to its writer unread.” Accordingly, I did not open the target frame, its rows, or the adjacent frames. This is an incomplete curriculum review, not a failed curriculum judgment.

No files were intentionally edited, created or deleted. No dependency installation or defect-ledger write was attempted.

## Findings

### 1. The required plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** new  
**Confidence:** firm, based on the runtime traceback and corresponding import.

**Location:** [scripts/lesson.py:15](/S:/CurioClass/scripts/lesson.py:15), imported while `scripts/plan.py check` performs its day checks.

**What is wrong:** The available default Python interpreter lacks the `markdown` dependency. The check terminates before reporting a complete result, including its progression and frame checks. This is an environment blocker; it does not establish a defect in the science-grade-3 frame.

**Why it matters:** The required prerequisite for the expert read remains unresolved. Reporting coverage, pacing or coherence as checked would overstate the evidence.

**Exact fix:** Configure the review runner to use an existing Python environment containing the repository’s required dependencies, or provision those dependencies outside this read-only session. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

After it passes, conduct the requested cold read and replace this blocked report with the substantive review.

## Required review coverage

| Requirement | Status |
|---|---|
| Owned skills placed exactly once | Not assessed |
| Standards taught in full | Not assessed |
| Unit purposes and order | Not assessed |
| Course and unit day allocations | Not assessed |
| Base-text applicability and source map | Not assessed |
| Previous-grade and next-grade seams | Not assessed |
| Cross-subject prerequisites | Not assessed |
| Unmarked stale notes | Not assessed |
| Marked stale-note check | Passed within the checker’s reported 37-file scope |

### Science lens, course frame layer

| Checklist line | Status |
|---|---|
| Every grade performance expectation has a unit that teaches it fully | Not assessed |
| Grades 6 to 8 preserve base-text order or explain departures | Not applicable to Grade 3 |
| High school expectations have explicit course ownership | Not applicable to Grade 3 |
| Every unit names an anchor phenomenon or design problem | Not assessed |

“Not assessed” is intentional. Neither “met” nor “missed” is supported without reading the frame.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Make no curriculum recommendation before the prerequisite gate completes | The standing expert instructions require the plan to return unread after gate failure | This report only |

## What is right and should not be touched

No curricular judgment is supported. Preserve the frame pending the required read.

## What I could not judge

All substantive frame questions remain open. They require a passing plan gate followed by the complete reading and external-source verification specified in the brief.

No outside research was undertaken because the review stopped before substantive analysis. Prior memory informed report organization only; no curriculum conclusion rests on memory.

## For Cory

None. The identified blocker concerns the execution environment, not scope, money, people or audience.

**Verdict:** blocked, frame unjudged. **Finding count:** 1 process blocker, 0 curricular findings established. **Report path:** `docs/reviews/frame-science-grade-3-2026-11-14.md`, supplied here only, not written.

