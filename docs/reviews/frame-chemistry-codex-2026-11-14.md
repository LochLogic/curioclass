# Chemistry course frame review, 2026-11-14

Intended report path: `docs/reviews/frame-chemistry-2026-11-14.md`  
Delivery: supplied here only. No report file was written.

## Verdict

The chemistry frame's soundness remains unjudged because the required full plan gate could not complete. The chemistry frame checker and science progression checker pass, but neither establishes the full prerequisite required by `docs/agents/EXPERT.md`. Restore the checking environment and rerun the full gate before completing the substantive curriculum review.

## What I read and checked

Read the expert instructions and science lens. Inspected the science rubric, foundation, approach, roadmap, source record, relevant baseline rules and source-list entries.

Opened the chemistry frame in full, its grade 10 science progression rows and its `frames.csv` row. Also inspected the Biology and Physics frames, relevant Algebra I, Geometry, ELA 10 and World History II material, and earlier science progression and frame reports.

I continued preliminary reading after the full gate failed. That did not follow the expert instruction to return the plan unread, and those preliminary observations are not presented as a completed curriculum review.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Terminated with `ModuleNotFoundError: No module named 'markdown'` |
| `python -B -X utf8 scripts/plan.py check chemistry` | Terminated with `ValueError: not enough values to unpack (expected 2, got 1)` |
| `python -B -X utf8 scripts/frame.py check chemistry` | Passed, 0 failures |
| `python -B -X utf8 scripts/progression.py check science` | Passed, 198 rows, 0 failures; advisory notes remain |
| `python -X utf8 scripts/stale.py check` | Passed, 46 files, 0 failures |

The frame checker reports 11 units, 160 total days, 149 unit days and 11 days for course-level checks and respond days.

## Findings

### 1. The required full plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`.

**What is wrong:** The selected Python is the interpreter bundled with the installed office suite. It lacks the `markdown` dependency, so the full checker terminates before establishing its complete result. The attempted course-specific command also crashes rather than providing a substitute result.

**Why it matters:** The standing expert instructions explicitly require: “If it fails, the plan goes back to its writer unread.” Passing focused frame and progression checks establishes useful structural facts, but does not satisfy that prerequisite. This is a review-environment blocker, not evidence that the chemistry frame is defective.

**Exact fix:** Configure the review runner to use a working Python environment containing the repository's required dependencies. Run the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

After it passes, complete the chemistry cold read and replace this blocked report with the substantive review. Do not record this report as curriculum approval.

**Earlier occurrence:** The same dependency failure is documented in [the Grade 3 frame review](/S:/CurioClass/docs/reviews/frame-science-grade-3-codex-2026-11-14.md) and [the Grade 6 frame review](/S:/CurioClass/docs/reviews/frame-science-grade-6-codex-2026-11-14.md). This run independently confirms the blocker persists.

## Required review coverage

| Requirement | Disposition |
|---|---|
| Owned skills placed exactly once | Structural placement passes the focused frame checker; substantive ownership review incomplete |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes, order and prerequisites | Not adjudicated |
| Course days | Mechanical allocation passes; feasibility and unit load not adjudicated |
| Source map | Chemistry declares no base text; source-map file absent, consistent with that declaration |
| Incoming and outgoing seams | Preliminary inspection only |
| Cross-subject readiness | Preliminary inspection only |
| Marked stale notes | Checker passes within its reported scope |
| Unmarked stale notes | Review incomplete |

### Science lens, course frame layer

| Checklist line | Disposition |
|---|---|
| Every owned performance expectation has sufficient unit coverage | Not adjudicated |
| Grades 6 to 8 preserve base order or explain departures | Not applicable |
| High school expectations have explicit course ownership | Ownership is recorded; substantive completeness not adjudicated |
| Every unit names an anchor phenomenon or design problem | Present in all 11 unit rows; scientific adequacy not adjudicated |

“Not adjudicated” does not mean met or missed.

## Settled by the expert

| Choice | Reason | File or system affected |
|---|---|---|
| Withhold the curricular verdict | The required full gate did not complete | This report |
| Retain the focused check results with their limits | They establish structural facts without replacing the full gate | This report |
| Classify the blocker as process | The traceback establishes an execution-environment failure | Review-runner configuration |
| Recommend no curriculum edits from this incomplete read | Preliminary inspection is insufficient for the requested expert verdict | Chemistry frame and progression |

## What is right and should not be touched

Preserve the frame pending completion of the review. Its focused structural check passes, including the recorded skill placement and day allocation.

## What I could not judge

This report does not establish full standards coverage, scientific accuracy, coherent model development, realistic investigation time, adequate alternatives to hands-on work, complete seams or cross-subject readiness. Those remain required work after the full gate passes.

No dependency installation, turn mutation, defect-ledger entry or repository edit was attempted.

## Outside sources and memory

These sources were opened for preliminary context. They support no curricular finding in this blocked report:

- Official standards: [Structure and Properties of Matter](https://www.nextgenscience.org/topic-arrangement/hsstructure-and-properties-matter), [Chemical Reactions](https://www.nextgenscience.org/topic-arrangement/hschemical-reactions), [Energy](https://www.nextgenscience.org/topic-arrangement/hsenergy), [Earth's Systems](https://www.nextgenscience.org/topic-arrangement/hsearths-systems), and [Human Sustainability](https://www.nextgenscience.org/topic-arrangement/hshuman-sustainability).
- Individual expectations: [HS-ESS2-4](https://www.nextgenscience.org/pe/hs-ess2-4-earths-systems), [HS-ETS1-2](https://www.nextgenscience.org/pe/hs-ets1-2-engineering-design), and [HS-PS1-8](https://www.nextgenscience.org/pe/hs-ps1-8-matter-and-its-interactions).
- Review criteria: [EQuIP Science Rubric, version 3.0](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf).
- Investigation context: [Particle Modeling of Hand Warmers](https://teachchemistry.org/classroom-resources/particle-modeling-of-hand-warmers) and [Changing State: Freezing](https://www.acs.org/middleschoolchemistry/lessonplans/chapter2/lesson4.html).

The process finding rests on current command output and repository instructions. No conclusion rests on memory.

## For Cory

None. Resolving the checking environment requires no scope, money, people or audience decision identified by this read.

**Verdict:** Review blocked, chemistry frame unjudged. **Finding count:** 1 process finding. **Report path:** `docs/reviews/frame-chemistry-2026-11-14.md`, supplied here only.