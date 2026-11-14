# Grade 7 Math course frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-7-2026-11-14.md`  
Report delivered here only. No file was created or changed.

## Verdict

The frame’s soundness remains unjudged because the required plan gate could not complete. The blocking risk is an unavailable checking dependency, which prevents establishing the prerequisite result. Restore the review environment and obtain a passing gate before completing the independent curriculum read.

## What I read and checked

Read:

- [Expert instructions](S:/CurioClass/docs/agents/EXPERT.md).
- [Math lens](S:/CurioClass/docs/agents/lenses/math.md).
- [Math rubric](S:/CurioClass/docs/RUBRIC-MATH-K8.md).
- [Foundation](S:/CurioClass/docs/FOUNDATION.md).
- Relevant checker excerpts and earlier blocked [Grade 5 math](S:/CurioClass/docs/reviews/frame-math-grade-5-codex-2026-11-14.md) and [biology](S:/CurioClass/docs/reviews/frame-biology-codex-2026-11-14.md) reports.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default interpreter | Resolves to `C:\Program Files\LibreOffice\program\python.exe` |
| Existing Python 3.13 interpreter | Execution denied |
| That interpreter’s existing `markdown` package | Reading denied |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |

The [expert instructions](S:/CurioClass/docs/agents/EXPERT.md) explicitly require: “If it fails, the plan goes back to its writer unread.” Accordingly, I did not read the target frame, its ownership rows, source map, progression rows, or neighboring frames.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed and corroborated by earlier reports

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`; review-runner Python configuration.

**What is wrong:** The available interpreter cannot import `markdown`. The command terminates before returning a complete gate result. An existing alternative interpreter is inaccessible in this sandbox.

**Evidence:** The current command output establishes the failure. The [earlier Grade 5 math report](S:/CurioClass/docs/reviews/frame-math-grade-5-codex-2026-11-14.md) records the same missing dependency, establishing the repeat classification.

**Why it matters:** The required prerequisite remains unsatisfied. A substantive verdict would bypass the expert workflow and could mislead the writer about what was checked. This runtime failure establishes no defect in the Grade 7 curriculum.

**Exact fix:** Configure the review runner to use an accessible Python environment containing the required dependencies, including `markdown`. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any actual gate failures it reports. After it passes, complete the requested independent Grade 7 frame read. Do not change or bypass the checker to obtain a passing result.

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned progression skill placed exactly once | Not assessed |
| Other-grade skills identified as justified review or extension | Not assessed |
| Every owned standard taught in full | Not assessed |
| Unit reasons and prerequisite order | Not assessed |
| School-year fit, course checks, and respond days | Not assessed |
| Unit days proportional to their responsibilities | Not assessed |
| Base lessons completely mapped, with justified omissions and departures | Not assessed |
| Source licensing and exclusion of reference-only material | Not assessed |
| Grade 6 incoming and Grade 8 outgoing seams | Not assessed |
| Same-grade cross-subject prerequisites | Not assessed |
| Marked stale notes | Checker passed within its configured 56-file scan |
| Unmarked stale notes and outdated review results | Not assessed |

### Math lens checklist: course frame layer

| Checklist line | Status |
|---|---|
| Major work meets the required share by units, days, and time | Not assessed |
| Supporting clusters practise major work | Not assessed |
| Every source-map row has a keep, split, merge, cut, or ours decision | Not assessed |

“Not assessed” does not mean met, missed, or not applicable. The prerequisite prevented those classifications.

## Settled by the expert

| Choice | Reason | Affected file or action |
|---|---|---|
| Withhold the curricular verdict | The required gate did not complete | This report |
| Classify the blocker as process | The evidence concerns the execution environment | Review-runner configuration |
| Make no curricular recommendation | The target frame remains unread | None |

## What is right and should not be touched

No curricular feature was established as sound or defective. This report provides no basis for changing the frame or its plan data.

## What could not be judged

All substantive curriculum questions remain open. They require a passing full plan gate, the specified repository readings, and outside-source verification.

## Sources and memory

The linked repository instructions establish the review procedure; the earlier reports establish recurrence. Current command output supplies the runtime evidence.

No outside curriculum sources were consulted because the prerequisite stopped substantive review. Prior memory informed reporting conventions only; no curriculum conclusion rests on memory.

## For Cory

None. No scope, money, people, or audience decision is requested.

**Verdict:** Review blocked; frame unjudged. **Finding count:** 1 blocking process finding. **Report path:** `docs/reviews/frame-math-grade-7-2026-11-14.md`, supplied here without writing the file.

