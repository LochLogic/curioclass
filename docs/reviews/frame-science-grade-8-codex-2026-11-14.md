# Science Grade 8 course frame review
Date: 2026-11-14  
Intended report path: `docs/reviews/frame-science-grade-8-2026-11-14.md`  
Delivery: Complete report supplied here. No report file written.

## Verdict

The frame’s curricular soundness remains unjudged because the required repository-wide plan gate fails. The grade 8 science frame reports zero structural failures, but the expert procedure requires returning the plan unread after a gate failure. Correct the identified synchronization defect and restore the ordinary check environment before completing this independent curriculum review.

## What I read and checked

Read the [expert instructions](/S:/CurioClass/docs/agents/EXPERT.md), [science lens](/S:/CurioClass/docs/agents/lenses/science.md), foundation, glossary, base-text record, and science progression reconciliation and fixes reports. Inspected the science rubric, teaching approach, relevant roadmap and baseline guidance, source register, plan documentation, checking scripts, and earlier science frame reviews.

The target frame, its source map, progression rows, adjacent frames, and cross-subject frames were left manually unread after the prerequisite failed.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternative Python launcher | Could not start its interpreter: permission denied |
| Repository-wide check with the execution accommodation below | Exit 1; one reported failure, in grade 6 math |
| Grade 8 science frame within that run | Zero failures; six units, 160 days, 156 allocated to units and four remaining for checks and respond days |
| `python -B -X utf8 scripts/frame.py check math-grade-6` | Reproduced the same failure |
| `python -X utf8 scripts/stale.py check` | 41 files checked, zero marked failures |

**Execution accommodation:** The missing package is used for rendering. I supplied an in-memory module that raises an exception if any rendering attribute is requested, then ran the unchanged checker. No checking function was replaced, no rendering was requested, and no dependency was installed. This exposes the gate result, but the ordinary command still needs a working dependency environment.

No file edits, defect-ledger writes, or report writes were performed.

## Findings

### 1. The required repository-wide gate fails outside this course

**Severity:** Blocks this review  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly reproduced

**Location:** [Grade 6 math frame, unit 6](/S:/CurioClass/docs/courses/math-grade-6/frame.md:121).

**What is wrong:** The checker reports:

```text
FAIL math-grade-6 unit 6: its rows own 6.EE.C.9, missing from Owned standards
```

Unit 6 already names `m6-dependent-variables` and describes moving related quantities between equations, tables, and graphs. Its source-order note also explicitly places work for `6.EE.C.9` in this unit. The missing code is therefore a synchronization defect in the frame’s **Owned standards** cell.

The ordinary prerequisite command also cannot complete in the available default Python environment because `markdown` is missing.

**Why it matters:** [EXPERT.md:105](/S:/CurioClass/docs/agents/EXPERT.md:105) states: “If it fails, the plan goes back to its writer unread.” A substantive science verdict now would disregard that prerequisite. This establishes a process blocker, not a defect in grade 8 science.

**Exact fix:**

1. Add `6.EE.C.9` to unit 6’s **Owned standards** cell in `docs/courses/math-grade-6/frame.md`, matching its existing skill placement and teaching description.
2. Configure the review runner to use an accessible Python environment containing `markdown`.
3. Rerun the unchanged repository-wide command, `python -X utf8 scripts/plan.py check`.
4. After it passes, complete the requested cold read and replace this blocked report with the substantive review.

**Earlier occurrence:** The [kindergarten science frame review](/S:/CurioClass/docs/reviews/frame-science-kindergarten-codex-2026-11-14.md:31) identifies the same unresolved gate failure. It remains current, so this report records it as repeated rather than presenting it as a new discovery.

## Required review coverage

| Requirement | Status |
|---|---|
| Owned progression skills placed exactly once | Not assessed |
| Every owned standard taught in full | Not assessed |
| Unit purposes and prerequisite order | Not assessed |
| School-year fit and proportional unit allocations | Arithmetic reported by the gate; instructional adequacy not assessed |
| Complete base-lesson mapping, sequence, omissions, and licensing | Not assessed |
| Incoming and outgoing course seams | Not assessed |
| Cross-subject prerequisites taught first | Not assessed |
| Unmarked stale notes | Not assessed |
| Marked stale notes | Checker passed within its reported 41-file scope |

### Science lens: course frame layer

| Checklist line | Status |
|---|---|
| Each owned performance expectation has a unit that teaches it fully | Not assessed |
| Grades 6 to 8 preserve base-text order and document departures or losses | Applicable, not assessed |
| High school band expectations have explicit course ownership | Not applicable |
| Every unit names an anchor phenomenon or design problem | Not assessed |

“Not assessed” is necessary here. The evidence does not support marking these lines met or missed.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold the curriculum verdict | The required gate fails and the expert instructions explicitly stop the read | Intended review report |
| Treat the missing math code as a documentation synchronization fix | The skill, teaching description, and source-order note already place it in unit 6 | `docs/courses/math-grade-6/frame.md` |
| Make no science content, ordering, or pacing recommendation yet | Structural results alone cannot establish instructional soundness | None |

## What is right and should not be touched

The grade 8 science frame returns zero structural failures in the completed checking run. Preserve that result as limited structural evidence. No science curriculum change is supported by this review.

## What I could not judge

All substantive curriculum questions remain open. They require the passing prerequisite, the complete cold read specified in the brief, and verification against outside standards and base-text sources.

No outside research was undertaken because the review stopped at the required prerequisite. Prior memory informed report organization only; no curriculum conclusion rests on memory.

## Sources

- [Expert instructions](/S:/CurioClass/docs/agents/EXPERT.md:103): mandatory prerequisite and stop rule.
- [Grade 6 math frame](/S:/CurioClass/docs/courses/math-grade-6/frame.md:121): verified the missing ownership code against existing instructional placement.
- [Earlier kindergarten science review](/S:/CurioClass/docs/reviews/frame-science-kindergarten-codex-2026-11-14.md:31): established that the process finding is repeated.
- [Science lens](/S:/CurioClass/docs/agents/lenses/science.md): identified the frame-layer questions left open.

## For Cory

None. The identified fixes concern documentation synchronization and the execution environment.

**Verdict:** blocked, curriculum unjudged. **Finding count:** 1 process blocker; 0 curricular findings established. **Report path:** `docs/reviews/frame-science-grade-8-2026-11-14.md`, supplied here only.

