# Expert cold read: science-kindergarten course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-kindergarten-2026-11-14.md`  
**Delivery:** Report supplied here. No files changed.

## Verdict

The curriculum verdict is withheld because the required repository-wide plan check still fails. Kindergarten science itself reports zero gate failures, but [EXPERT.md, line 105](/S:/CurioClass/docs/agents/EXPERT.md:105) explicitly requires returning the plan unread when that check fails. Resolve the remaining gate failure and rerun the prerequisite before completing this independent curriculum read.

## What I read and checked

Read the expert instructions, science lens, science rubric, foundation, general teaching approach, base-text record, and relevant portions of the roadmap, baseline rules, source register, plan documentation, and checking scripts.

The kindergarten science frame, its progression rows, neighboring frames, and cross-subject frames were deliberately left unread after the prerequisite failed.

| Check | Observed result |
|---|---|
| Requested `python -X utf8 scripts/plan.py check` | Could not complete initially: default Python lacks `markdown` |
| Plan check with the workaround described below | Latest run: exit status 1, one remaining failure |
| Kindergarten science result within that run | Zero failures; six units, 64 days, 58 unit days and six days remaining |
| Science progression result within that run | 198 rows, zero failures |
| `python -X utf8 scripts/stale.py check` | 30 files checked, zero failures |

**Execution limitation:** The missing package is used by rendering functions. To execute the checks without installing anything or changing files, I supplied an in-memory module that raises an exception if rendering is requested. No checking function was changed, and no rendering function was called. This establishes the reported checking results, but the ordinary command still needs a working dependency environment.

Two frame synchronization failures appeared in the first completed run and disappeared before verification. They are not reported as current findings.

## Findings

### 1. The required prerequisite still fails outside this course

**LAYER:** process  
**REPEAT:** new  
**Severity:** Blocks this review  
**Confidence:** firm

**What is wrong:** The latest repository-wide check reports:

```text
FAIL math-grade-6 unit 6: its rows own 6.EE.C.9, missing from Owned standards
```

The focused `scripts/frame.py check math-grade-6` reproduces the same failure.

**Why it matters:** The standing expert procedure says: “If it fails, the plan goes back to its writer unread.” Continuing to a kindergarten science verdict would disregard that explicit prerequisite. This is a review-process blocker, not evidence of a kindergarten science curriculum defect.

**Exact fix:** The responsible writer should add `6.EE.C.9` to unit 6’s **Owned standards** cell in `docs/courses/math-grade-6/frame.md`, consistent with the ownership reported by the gate. Then rerun the repository-wide plan check in an environment with its required dependencies. Once it passes, complete this kindergarten science cold read.

## Required review coverage

These judgments remain open. A passing structural check does not settle their substance.

| Required review | Status |
|---|---|
| Owned skills placed exactly once, with appropriate grade ownership | Not assessed |
| Every owned standard taught in full | Not assessed |
| Unit coherence, reasons, and prerequisite order | Not assessed |
| School-year fit and allocation proportional to learning | Not assessed; arithmetic result recorded above |
| Base-text source map | Not applicable: the base-text record identifies science K to 5 as original courses |
| Incoming and outgoing seams | Not assessed |
| Math and literacy prerequisites taught first | Not assessed |
| Unmarked stale notes in the course and related reviews | Not assessed; marked-note check passed |

### Science lens: course-frame checklist

| Checklist line | Status |
|---|---|
| Every grade performance expectation has a unit and is fully represented | Not assessed |
| Grades 6 to 8 base-text order and loss check | Not applicable |
| High-school band ownership | Not applicable |
| Every unit names an anchor phenomenon or design problem | Not assessed |

The substantive lines cannot honestly be marked met or missed without reading the frame.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold the curriculum verdict and preserve the cold read | The required prerequisite remains failed | Intended review report only |
| Make no instructional recommendations yet | No course-content evidence was examined | None |

## What is right and should remain

The gate separately reports kindergarten science and the science progression with zero failures. Preserve those results as structural evidence, while keeping the substantive curriculum judgment open.

## Sources and limits

- [Expert procedure](/S:/CurioClass/docs/agents/EXPERT.md:105): mandatory stopping condition.
- [Science lens](/S:/CurioClass/docs/agents/lenses/science.md): course-frame checklist.
- [Science rubric](/S:/CurioClass/docs/RUBRIC-SCIENCE.md): review boundaries and full-standard expectations.
- [Base-text record](/S:/CurioClass/docs/sources/BASE-TEXTS.md): kindergarten science has no base text.
- Live checker output: the current blocker and structural results.

No outside-source curriculum research was undertaken after the prerequisite failed. Prior memory informed report organization only; no educational judgment rests on memory.

## For Cory

None. No new scope, money, people, or audience decision was identified.

**Verdict:** Review blocked, curriculum verdict withheld. **Finding count:** one process blocker, zero assessed curriculum findings. **Report path:** `docs/reviews/frame-science-kindergarten-2026-11-14.md`, supplied above and not created.

