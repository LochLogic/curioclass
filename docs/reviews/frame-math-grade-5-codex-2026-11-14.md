# Grade 5 Math frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-5-2026-11-14.md`  
Report supplied here only. No report file was created.

## Verdict

The frame’s soundness remains unjudged because the required plan gate could not complete. The blocker is a missing Python dependency, which prevents establishing the prerequisite check result. Restore the check environment and obtain a passing gate before completing the independent curriculum review.

## What I read and checked

Read `docs/agents/EXPERT.md`, the math lens, `docs/RUBRIC-MATH-K8.md` and `docs/FOUNDATION.md`. Inspected the checker code, plan-data guidance, approach documents, source policy, portions of the Grade 5 frame and progression rows, and earlier review reports concerning the same gate failure.

I opened curriculum material after the gate failed. That exceeded the expert instruction to return the plan unread after failure, so this report makes no substantive curriculum judgment.

| Command or check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default Python | Resolves to the LibreOffice Python environment |
| Read-only environment lookup | Did not identify a usable alternative interpreter |
| `python -X utf8 scripts/stale.py check` | Exit 0: 54 files, 0 failures |
| Requested `data/plans/math-grade-5/source-map.csv` | File not found; the frame contains a prose source map whose adequacy was not assessed |

No installation, turn mutation, defect-ledger write or report-file write was attempted.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed runtime failure

**Location:** [scripts/lesson.py:15](/S:/CurioClass/scripts/lesson.py:15), imported during `scripts/plan.py check`.

**What is wrong:** The default interpreter cannot import `markdown`. The command terminates during its day checks before reporting a complete gate result. This establishes an environment failure, not a Grade 5 curriculum defect.

**Why it matters:** [EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md) explicitly requires: “If it fails, the plan goes back to its writer unread.” Issuing findings about coverage, sequence or pacing without satisfying that prerequisite would bypass the required review procedure.

**Exact fix:** Configure the review runner to use a Python environment containing the repository’s required dependencies, including Python-Markdown. Then rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any failures it reports, then commission a fresh independent Grade 5 frame read. Do not alter the checker or substitute an import stub.

**Earlier occurrences:** The same missing dependency is recorded in [the Grade 3 science review](/S:/CurioClass/docs/reviews/frame-science-grade-3-codex-2026-11-14.md) and [the Grade 2 math review](/S:/CurioClass/docs/reviews/frame-math-grade-2-codex-2026-11-14.md).

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned progression skill placed exactly once | Not adjudicated |
| Earlier-grade or later-grade content explicitly justified | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| School-year allocation, checks and respond days | Not adjudicated |
| Unit allocations proportional to their responsibilities | Not adjudicated |
| Complete source mapping, order, omissions and licensing | Not adjudicated |
| Grade 4 and Grade 6 seams | Not adjudicated |
| Same-grade cross-subject prerequisites | Not adjudicated |
| Unmarked stale notes | Search incomplete |
| Marked stale-note check | Passed within the checker’s reported 54-file scope |

### Math lens: course frame checklist

| Checklist line | Status |
|---|---|
| Major work meets the required share by units, days and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row has a keep, split, merge, cut or ours decision | Not adjudicated |

These statuses mean the review is incomplete. They do not mean the frame meets or misses the checklist.

## What is right and should not be touched

No curricular feature was established as sound by this blocked review. Preserve the frame pending the substantive read.

## Settled by the expert

| Choice | Reason | File or action affected |
|---|---|---|
| Withhold the curriculum verdict until the required gate passes | The standing expert instructions explicitly require this prerequisite | Review runner and subsequent review |
| Make no curriculum changes from this report | The observed blocker concerns the check environment | Grade 5 frame and plan data |

## What I could not judge

Coverage, mathematical limits, pacing, source fidelity, seams and cross-subject readiness remain unjudged. Completing those judgments requires a passing full plan gate followed by the requested source-supported cold read.

## Sources and limits

- [Expert instructions](/S:/CurioClass/docs/agents/EXPERT.md): prerequisite and reporting requirements.
- [Math lens](/S:/CurioClass/docs/agents/lenses/math.md): required course frame checklist.
- [Math rubric](/S:/CurioClass/docs/RUBRIC-MATH-K8.md): local adoption bar.
- Earlier reports linked in finding 1: evidence that this process failure repeats.

No outside sources were consulted because the prerequisite stopped substantive review. No curriculum conclusion rests on memory.

## For Cory

None. This report identifies an operational prerequisite, with no scope, money, people or audience decision to settle.

**Verdict:** Unjudged pending the required gate. **Finding count:** 1 blocking process finding. **Intended report path:** `docs/reviews/frame-math-grade-5-2026-11-14.md`, supplied above without creating the file.