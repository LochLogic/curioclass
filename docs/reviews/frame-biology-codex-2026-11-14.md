# Biology course frame review, 2026-11-14

**Intended report path:** `docs/reviews/frame-biology-2026-11-14.md`  
**Delivery:** Complete report supplied here; no report file written.

## Verdict

The biology frame remains unjudged because the required plan gate could not complete. The blocker is the review environment’s missing Python dependency, so this run establishes no curriculum defect or passing coverage result. Restore the check environment and rerun the gate before completing the cold read.

## What I read and ran

Read `docs/agents/EXPERT.md`, `docs/agents/lenses/science.md`, and `docs/RUBRIC-SCIENCE.md`. Inspected the foundation, approach, glossary, roadmap, checker code, and earlier Grade 6 science frame report.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Terminated with `ModuleNotFoundError: No module named 'markdown'` |
| Existing `python3.12.exe` launcher, running the same gate | Could not spawn its Python child process: permission denied |
| `python -X utf8 scripts/stale.py check` | Passed: 47 files, 0 failures |

The default interpreter resolves to `C:\Program Files\LibreOffice\program\python.exe`.

[EXPERT.md](S:/CurioClass/docs/agents/EXPERT.md) explicitly says: “If it fails, the plan goes back to its writer unread.” I therefore withheld the substantive read of the biology frame, progression rows, ownership data, source map, and neighboring frames.

## Findings

### 1. The required plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`; review-runner Python configuration.

**What is wrong:** The default interpreter lacks `markdown`. The gate terminates during its day checks, before returning a complete result. The existing alternative launcher also fails because it cannot spawn its interpreter.

**Evidence:** The current run produced both failures directly. The [earlier Grade 6 frame review](S:/CurioClass/docs/reviews/frame-science-grade-6-codex-2026-11-14.md) records the same environment problem, establishing the repeat classification.

**Why it matters:** The expert workflow requires the gate before curricular judgment. Treating this incomplete execution as settled coverage would give the writer and subsequent reviewers a false prerequisite result. This is an environment failure, not evidence that biology’s frame is defective.

**Exact fix:** Configure the review runner to invoke an accessible Python environment containing the repository’s required dependencies, including `markdown`. Rerun:

```text
python -X utf8 scripts/plan.py check
```

Resolve any actual gate failures it then reports. Once the gate passes, complete the biology cold read and replace this blocked report with the substantive review. Do not modify or bypass the checker to obtain a passing result.

## Required review coverage

| Requirement | Disposition |
|---|---|
| Owned progression skills placed exactly once; other-grade work justified | Not assessed |
| Every owned standard taught in full | Not assessed |
| Unit purposes, order, and prerequisite models | Not assessed |
| Course calendar, checks, respond days, and unit allocations | Not assessed |
| Base-text lesson placement, order, exclusions, and licensing | Applicability and coverage not assessed |
| Incoming and outgoing course seams | Not assessed |
| Cross-subject prerequisites taught first | Not assessed |
| Marked stale notes | Checker passed |
| Unmarked stale notes contradicted by repository evidence | Not assessed |

The stale check’s passing result covers its configured scan only. It does not establish that unmarked notes or review results are current.

## Science lens checklist: course frame layer

| Lens line | Disposition |
|---|---|
| Every owned performance expectation has sufficient unit coverage | Not assessed |
| Grades 6 to 8 preserve base order or justify departures without topic loss | Not applicable to the biology frame |
| High school band expectations have explicit course ownership | Not assessed |
| Every unit names an anchor phenomenon or design problem | Not assessed |

“Not assessed” does not mean met or missed.

## Settled by the expert

| Choice | Reason | File or configuration affected |
|---|---|---|
| Withhold the curricular verdict | The prerequisite gate did not complete | Intended biology review report |
| Classify the blocker as process | Runtime evidence identifies interpreter and dependency failures | Review-runner configuration |
| Make no curriculum recommendations yet | The target received no substantive cold read | None |

## What is right and should not be touched

No curricular judgment was reached. This report provides no basis for changing the biology frame or its data.

## What could not be judged

All substantive review questions remain open. Completing them requires a successful plan gate followed by the requested full reading and outside-source verification.

## Sources and memory

- [Expert instructions](S:/CurioClass/docs/agents/EXPERT.md): prerequisite gate and reporting requirements.
- [Science lens](S:/CurioClass/docs/agents/lenses/science.md): course frame checklist.
- [Science rubric](S:/CurioClass/docs/RUBRIC-SCIENCE.md): review bar and layer boundaries.
- [Earlier Grade 6 frame review](S:/CurioClass/docs/reviews/frame-science-grade-6-codex-2026-11-14.md): repeat classification, independently confirmed in this run.
- Current command output: direct evidence of the blocker and stale-check result.

No outside curriculum sources were consulted because the prerequisite stopped the substantive review. Prior memory informed reporting conventions only; no curricular conclusion rests on memory.

## For Cory

None. No scope, money, people, or audience decision is requested.

**Verdict:** Review blocked; biology frame unjudged. **Finding count:** 1 process finding. **Report path:** `docs/reviews/frame-biology-2026-11-14.md`, supplied above, not written.

