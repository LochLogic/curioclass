# Math Grade 8 course frame review

Date: 2026-11-14  
Intended report path: `docs/reviews/frame-math-grade-8-2026-11-14.md`  
Delivery: Report supplied here only. No file created or edited.

## Verdict

The frame’s curricular soundness remains unjudged because the required full plan gate could not complete. Separate frame and progression checks pass, but they cannot establish full standards coverage, instructional coherence or adequate pacing. Restore the checking environment, correct the stale notes identified below, and complete a fresh independent curriculum read after the prerequisite passes.

## What I read and checked

Read the expert instructions, mathematics lens, mathematics rubric, target frame, its `frames.csv` entry, its inline source map and the 24 Grade 8 progression rows. Consulted the foundation, teaching approaches, source register, base-text policy, glossary, frame-writing brief, checking scripts, earlier reviews, and portions of the neighboring mathematics and same-grade science frames.

The requested `data/plans/math-grade-8/source-map.csv` does not exist. The frame-writing brief explicitly schedules that day-level file for the scope and sequence stage, so its absence alone is not a frame defect.

I opened curriculum material while investigating the failed checking environment. That exceeded the expert instruction to return the plan unread after failure. This report therefore records process findings and limited structural results, without issuing a substantive curriculum judgment.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default Python | Resolves to the installed office-suite Python |
| Existing alternative Python launcher | Could not launch its interpreter: permission denied |
| `python -B -X utf8 scripts/frame.py check math-grade-8` | Zero failures; 8 units, 160 days, 154 allocated to units and 6 remaining for checks and respond days |
| `python -B -X utf8 scripts/progression.py check math` | 305 rows, zero failures; advisory notes remain |
| `python -B -X utf8 scripts/frame.py check` | Exit 0 |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures |

No dependency installation, checker modification, turn mutation, defect-ledger write or report-file write was attempted.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly reproduced

**Location:** [scripts/lesson.py:15](/S:/CurioClass/scripts/lesson.py:15), imported during the full plan check.

**What is wrong:** The available default interpreter cannot import `markdown`. The command terminates before producing a complete gate result. This is an execution-environment failure, not evidence of a Grade 8 curriculum defect.

**Why it matters:** [EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md) explicitly says: “If it fails, the plan goes back to its writer unread.” The independent curriculum review cannot be completed under that procedure without the prerequisite result.

**Exact fix:** Configure the review runner to use an accessible Python environment containing the repository’s required dependencies, including Python-Markdown. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any reported failures, then commission a fresh independent Grade 8 frame read. Preserve the real checking functions and dependency behavior.

**Earlier occurrence:** [Grade 5 mathematics frame review, finding 1](/S:/CurioClass/docs/reviews/frame-math-grade-5-codex-2026-11-14.md).

### 2. The outgoing seam introduction incorrectly says the receiving frames are unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly verified

**Location:** [Grade 8 frame:66](/S:/CurioClass/docs/courses/math-grade-8/frame.md:66).

**What is wrong:** The introduction says the Algebra I and Geometry frames “are not written.” Both [Algebra I](/S:/CurioClass/docs/courses/algebra-i/frame.md) and [Geometry](/S:/CurioClass/docs/courses/geometry/frame.md) now have frame files.

**Why it matters:** The note gives the next reader a false reason to postpone checking both ends of the handoff.

**Exact fix:** Replace the introduction with:

> Handed on to Algebra I and Geometry. Their current frames are `docs/courses/algebra-i/frame.md` and `docs/courses/geometry/frame.md`. The table below names the receiving progression rows.

This correction establishes file availability only. It does not establish that the seams match.

**Earlier occurrence:** The same kind of stale availability note appears in [the Economics frame review, finding concerning loaded source collections](/S:/CurioClass/docs/reviews/frame-economics-codex-2026-11-13.md).

### 3. Two notes incorrectly say N-Q.A.3 has no progression row

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly verified

**Locations:** [Grade 8 frame:81](/S:/CurioClass/docs/courses/math-grade-8/frame.md:81) and [Grade 8 frame:158](/S:/CurioClass/docs/courses/math-grade-8/frame.md:158).

**What is wrong:** Both notes explain the missing scientific-notation handoff by saying N-Q.A.3 has no row. In the current progression, `geo-solving-right-triangles` owns N-Q.A.3 and `alg1-scatter-linear-models` carries `~N-Q.A.3`. The narrower statement that `m8-scientific-notation` has no outgoing link remains accurate.

**Why it matters:** A fixer could undertake unnecessary ownership work or overlook the existing rows when examining the actual handoff.

**Exact fix:** Replace the scientific-notation seam cell with:

> No outgoing progression link is recorded. N-Q.A.3 is owned by `geo-solving-right-triangles` and begun in `alg1-scatter-linear-models`.

Replace the corresponding explanation in “For the lead,” item 6, with:

> `m8-scientific-notation` has no outgoing progression link. N-Q.A.3 already has an owner, `geo-solving-right-triangles`, and a beginning placement in `alg1-scatter-linear-models`.

Do not infer a new dependency from this status correction.

**Earlier occurrence:** Same stale completion or placement-note category as finding 2.

## Required review coverage

| Requirement | Status |
|---|---|
| Owned skills placed exactly once | Structural gate passes |
| Other-grade content justified as review or extension | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| School-year arithmetic | Structural gate reports 154 unit days plus 6 course-level days |
| Instructional adequacy of unit allocations | Not adjudicated |
| Base-lesson completeness, order, cuts and licensing | Inline map present; substantive verification incomplete |
| Incoming and outgoing seams | Not adjudicated |
| Same-grade cross-subject readiness | Not adjudicated |
| Marked stale notes | Checker passes within its reported scope |
| Unmarked stale notes | Findings 2 and 3 verified; search incomplete |

### Mathematics lens: course frame checklist

| Checklist line | Status |
|---|---|
| Major work meets the line by units, days and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row has a keep, split, merge, cut or ours decision | Not adjudicated |

These unresolved lines cannot honestly be marked met, missed or not applicable.

## Settled by the expert

| Choice | Reason | File or action affected |
|---|---|---|
| Withhold the curriculum verdict | The required full gate did not complete | Review |
| Do not flag the absent day-level source-map CSV as a frame defect | The frame-writing brief assigns it to the next planning stage | None |
| Replace the unwritten-frame claim with the existing paths | Both receiving frames exist | Grade 8 frame, seam introduction |
| Separate the missing scientific-notation link from N-Q.A.3 ownership | The current progression already places N-Q.A.3 | Grade 8 frame, seam table and lead item 6 |

## What is right and should not be touched

Preserve the passing structural results: the frame’s skill and ownership checks pass, and its day allocation totals 160. These results support no change to content, unit order or pacing on their own.

## What I could not judge

Full standards treatment, prerequisite coherence, pacing adequacy, source fidelity, seams and cross-subject availability remain unresolved. They require the passing prerequisite and the complete source-supported cold read.

## Outside sources and limits

- [Base-text Grade 8 transformations overview](https://im.kendallhunt.com/MS/teachers/3/1/index.html): opened to inspect its lesson inventory and license statement.
- [Base-text Grade 8 data overview](https://im.kendallhunt.com/MS/teachers/3/6/index.html): opened to inspect its lesson inventory.
- [Mathematics Progressions, compiled edition](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf): retrieval failed because the document exceeded the web tool’s size limit.

Outside-source research was not completed and supports no curriculum verdict here. No finding rests on memory.

## For Cory

None. The established findings concern the checking environment and factual status notes.

**Verdict:** Review incomplete; curriculum unjudged. **Finding count:** 3 process findings, including 1 blocker. **Report path:** `docs/reviews/frame-math-grade-8-2026-11-14.md`, supplied above only.