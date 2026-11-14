# Expert cold read: science-grade-7 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-science-grade-7-2026-11-14.md`  
**Delivery:** Complete report supplied here. No report file written.

## Verdict

The curriculum verdict is withheld because the required repository-wide plan check fails. Grade 7 science reports zero structural failures, but the [expert procedure](/S:/CurioClass/docs/agents/EXPERT.md:105) requires returning the plan unread after a failed gate. Correct the remaining Grade 6 math declaration, obtain a passing repository-wide check, and then complete this independent science read.

## What I read and ran

Read the expert instructions and science lens. Consulted the science rubric, foundation, plan documentation, relevant checking code, and the earlier kindergarten and Grade 3 science frame reports.

The target frame, its source map and progression rows, neighboring science frames, and corresponding cross-subject frames remain unread to preserve the required cold read.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: default Python lacks `markdown` |
| Unchanged plan checker with an existing dependency directory available | Completed, exit 1: one failure in Grade 6 math |
| Grade 7 science within that completed check | Zero failures; six units, 160 days, 156 unit days, four remaining days |
| Focused `scripts/frame.py check math-grade-6 science-grade-7` | Reproduced the math failure; science reported zero failures |
| Final `python -B -X utf8 scripts/stale.py check` | 45 files checked, zero failures |

The completed plan check used the existing package directory `S:\AI\tts\.venv\Lib\site-packages`, added to that process's import path. No checking functions were replaced, and no packages were installed. Bytecode writing was disabled for this invocation.

No repository edits, turn-management mutations, or defect-ledger writes were performed.

## Findings

### 1. A repository-wide gate failure blocks the required cold read

**Severity:** Blocking prerequisite  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, reproduced by the full and focused checkers

**Location:** Unit 6, **Owned standards** cell in [the Grade 6 math frame](/S:/CurioClass/docs/courses/math-grade-6/frame.md).

**What is wrong:** The completed check reports:

```text
FAIL math-grade-6 unit 6: its rows own 6.EE.C.9, missing from Owned standards
```

This same blocker appears in the [earlier kindergarten science report](/S:/CurioClass/docs/reviews/frame-science-kindergarten-codex-2026-11-14.md:31). It remains unresolved in the current checks; this report does not claim a new curricular discovery.

**Why it matters:** [EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md:105) explicitly says, “If it fails, the plan goes back to its writer unread.” A substantive science verdict would therefore bypass the required prerequisite. The failure establishes no defect in Grade 7 science.

**Exact fix:** The responsible writer should add `6.EE.C.9` to the existing unit 6 **Owned standards** cell, matching the ownership already reported by its progression rows. Rerun the unchanged repository-wide plan check with its actual dependencies available. Once it passes, conduct the complete Grade 7 science cold read.

## Required review coverage

| Required question | Status |
|---|---|
| Every owned skill placed exactly once; other-grade content justified | Structural gate reports no science failure; substance unassessed |
| Every owned standard taught in full | Unassessed |
| Unit boundaries, reasons and prerequisite order | Unassessed |
| School-year fit and proportional unit allocations | Arithmetic recorded above; adequacy unassessed |
| Complete, licensed base-lesson mapping and justified departures | Applicable to this middle-school course; unassessed |
| Incoming and outgoing science seams | Unassessed |
| Math and literacy prerequisites taught first | Unassessed |
| Unmarked stale notes | Unassessed; marked-note checker passed |

### Science lens: course-frame checklist

| Checklist line | Result |
|---|---|
| Every grade performance expectation has a unit that teaches it fully | Unassessed |
| Grades 6 to 8 preserve base-text order or justify departures and check losses | Unassessed |
| High-school band expectations have explicit course ownership | Not applicable |
| Every unit names an anchor phenomenon or design problem | Unassessed |

“Unassessed” cannot honestly be replaced with “met” or “missed” without reading the frame.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Preserve the cold read and withhold the curriculum verdict | The required gate remains failed | This report only |
| Make no instructional changes or recommendations | No course-content evidence was examined | None |

## What is right and should not be touched

Preserve the zero-failure Grade 7 science result as structural evidence. It supports neither approval nor rejection of the course's instructional substance.

## Sources and limits

- [Expert procedure](/S:/CurioClass/docs/agents/EXPERT.md:103): prerequisite and stopping rule.
- [Science lens](/S:/CurioClass/docs/agents/lenses/science.md): course-frame checklist.
- [Science rubric](/S:/CurioClass/docs/RUBRIC-SCIENCE.md): standards, coherence and review boundaries.
- [Earlier kindergarten science report](/S:/CurioClass/docs/reviews/frame-science-kindergarten-codex-2026-11-14.md:31): repeat classification.
- Current checker output: reproduced blocker and structural results.

No outside-source curriculum research was undertaken because the prerequisite stopped the substantive review. Prior memory informed report organization only; no curriculum conclusion rests on memory.

## For Cory

None. The identified correction requires no new scope, money, people or audience decision.

**Verdict:** blocked, curriculum unjudged. **Finding count:** 1 process blocker; 0 curricular findings established. **Report path:** `docs/reviews/frame-science-grade-7-2026-11-14.md`, supplied here only.

