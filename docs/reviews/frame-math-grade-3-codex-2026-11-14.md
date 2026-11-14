# Grade 3 mathematics course frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-3-2026-11-14.md`  
Report supplied here only. No file was written.

## Verdict

The frame’s soundness remains unjudged because the required plan check could not complete. The blocking risk is an incomplete validation result, so this run establishes no curriculum defect. Restore the check environment and obtain a passing full check before conducting the substantive cold read.

## What I read and checked

Read:

- `docs/agents/EXPERT.md`
- `docs/agents/lenses/math.md`
- `docs/RUBRIC-MATH-K8.md`
- Relevant checker implementation in `scripts/plan.py`, `scripts/lesson.py`, and `scripts/stale.py`
- `docs/reviews/frame-math-grade-2-codex-2026-11-14.md`, to establish whether the blocker repeats an earlier finding

The course frame, progression rows, source map, neighboring frames, and cross-subject frames were left unread after the prerequisite failed.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default Python location | `C:\Program Files\LibreOffice\program\python.exe` |
| Existing alternative Python launcher | Failed to spawn its interpreter: permission denied |
| `python -X utf8 scripts/stale.py check` | 54 files checked, 0 failures |

No files were edited, created, or deleted. No dependencies were installed, and no turn or defect-ledger mutations were attempted.

## Findings, most serious first

### 1. The prerequisite plan check cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed runtime failure

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`.

**What is wrong:** The default interpreter lacks the `markdown` dependency. The full checker terminates during its day checks before producing a complete result. The available alternative launcher also cannot start its interpreter.

**Why it matters:** [EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md:105) explicitly requires: “If it fails, the plan goes back to its writer unread.” Continuing the curriculum read would bypass that prerequisite. This failure establishes an environment blocker, not a defect in the Grade 3 frame.

**Exact fix:** Configure the runner to use an accessible Python environment containing the checker’s required dependencies. Then rerun:

```text
python -X utf8 scripts/plan.py check
```

Resolve any reported failures and obtain a successful complete result before restarting this review. No curriculum change follows from the current evidence.

**Earlier occurrence:** [Grade 2 mathematics frame review](/S:/CurioClass/docs/reviews/frame-math-grade-2-codex-2026-11-14.md), finding 1, records the same missing dependency and alternative-launcher failure. This run independently confirms that unresolved blocker.

## Required review coverage

| Requirement | Status |
|---|---|
| Owned progression skills placed exactly once | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| School-year capacity, checks, respond days, and unit allocations | Not adjudicated |
| Base-lesson placement, licensing, order, and justified departures | Not adjudicated |
| Grade 2 and Grade 4 seams | Not adjudicated |
| Cross-subject prerequisites | Not adjudicated |
| Unmarked stale notes | Not examined; automated stale check passed |

### Math lens checklist, course frame layer

| Checklist line | Disposition |
|---|---|
| Major work meets the required proportion by units, lessons, and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row records keep, split, merge, cut, or ours | Not adjudicated |

These cannot honestly be marked met, missed, or not applicable before the prerequisite permits the substantive read.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold a curriculum verdict | The required check did not complete | This report |
| Classify the finding as process | Runtime evidence identifies an environment failure | Review-runner configuration |
| Keep the automated stale result separate from manual review | Zero marked-note failures does not establish that unmarked notes are current | This report |

## What is right and should not be touched

The automated stale-note check passed. Preserve the curriculum pending an evidence-based substantive review; this run provides no basis for changing its content.

## What I could not judge

Coverage, standard completeness, pacing, source fidelity, seams, cross-subject timing, and unmarked stale notes remain unjudged. They require a passing full plan check followed by the requested cold read.

## Sources and memory

The finding rests on current command output and repository instructions. Outside-source research was deferred because the prerequisite stopped the curriculum review. Prior session memory informed report structure only; no curriculum judgment rests on memory.

## For Cory

None. No scope, money, people, or audience decision arises from this blocker.

**Verdict:** Unjudged pending a successful full plan check.  
**Finding count:** 1 process blocker.  
**Report path:** `docs/reviews/frame-math-grade-3-2026-11-14.md`, supplied above, not written.

