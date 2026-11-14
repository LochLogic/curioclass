# Science Grade 6 frame review, 2026-11-14

Intended report path: `docs/reviews/frame-science-grade-6-2026-11-14.md`

## Verdict

The frame’s soundness remains unjudged because the required plan gate could not complete. The blocker is the review environment’s missing Python dependency, which prevents establishing the prerequisite check result. Restore a working check environment and rerun the gate before completing the curriculum review.

## What I read and ran

Read `docs/agents/EXPERT.md` and `docs/agents/lenses/science.md`. Inspected the science rubric, foundation and roadmap material, checker code, and the earlier Grade 3 frame review.

Part of the target frame was opened while the first check ran. I did not complete or claim the substantive cold read after learning that the prerequisite gate could not run.

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Failed: `ModuleNotFoundError: No module named 'markdown'` |
| Existing `python3.12.exe` launcher, running the same check | Failed: its Python child process could not launch, permission denied |
| `python -X utf8 scripts/stale.py check` | Passed: 41 files, 0 failures |

[EXPERT.md](S:/CurioClass/docs/agents/EXPERT.md) explicitly requires: “If it fails, the plan goes back to its writer unread.” Neither interpreter attempt produced a completed gate result.

No files were intentionally edited, created or deleted. This report is supplied here under the read-only instruction.

## Findings

### 1. The required plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `scripts/lesson.py:15`, imported by `scripts/plan.py check`.

**What is wrong:** The default Python interpreter is LibreOffice’s bundled Python and lacks `markdown`. The checker terminates during day checks, before completing its progression and frame checks. The available alternative launcher also fails with permission denied.

**Why it matters:** The review cannot treat mechanical coverage as settled or proceed under the expert’s required workflow. This is an environment blocker, not evidence that the Grade 6 frame is defective.

**Exact fix:** Configure the review runner to use a working Python environment containing the repository’s required dependencies. Then rerun:

```text
python -X utf8 scripts/plan.py check
```

Once it passes, complete the requested cold read and replace this blocked report with the substantive findings.

**Earlier occurrence:** [Grade 3 frame review](S:/CurioClass/docs/reviews/frame-science-grade-3-codex-2026-11-14.md) reports the same dependency failure. The current run independently confirms it remains unresolved.

## Required review coverage

| Requirement | Status |
|---|---|
| Owned skills placed exactly once | Not assessed |
| Owned standards taught in full | Not assessed |
| Unit purposes, order and prerequisites | Not assessed |
| Course and unit day allocations | Not assessed |
| Base lesson placement, order and licensing | Not assessed |
| Incoming and outgoing seams | Not assessed |
| Cross-subject timing | Not assessed |
| Unmarked stale notes | Not assessed |
| Marked stale notes | Checker passed |

### Science lens, course frame checklist

| Lens line | Disposition |
|---|---|
| Every owned performance expectation has sufficient unit coverage | Not assessed |
| Base order is preserved or departures justified; no topic is lost | Not assessed |
| High school expectation ownership | Not applicable |
| Every unit names an anchor phenomenon or design problem | Not assessed |

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold the curricular verdict | The prerequisite gate did not complete | Intended review report |
| Classify the blocker as process | The traceback establishes an environment failure | Review-runner configuration |

## What should be preserved

No curriculum changes are recommended from this incomplete read.

## What could not be judged

Coverage, coherence, pacing, source fidelity, seams and cross-subject readiness require the completed gate and full cold read. The requested `data/plans/science-grade-6/source-map.csv` was absent at the attempted path; the frame’s embedded source map was not substantively evaluated.

## Sources and memory

Evidence for the finding is the current runtime output, checker import location and linked repository instructions. No outside curriculum sources were consulted because the prerequisite stopped the substantive review. Prior memory informed reporting conventions only; no curricular conclusion rests on memory.

## For Cory

None. No scope, money, people or audience decision is requested.

**Verdict:** Review blocked, curriculum unjudged.  
**Finding count:** 1 process finding.  
**Report path:** `docs/reviews/frame-science-grade-6-2026-11-14.md`, supplied above, not written.

