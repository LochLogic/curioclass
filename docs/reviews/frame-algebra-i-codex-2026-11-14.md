# Algebra I course frame review

Date: 2026-11-14  
Intended report path: `docs/reviews/frame-algebra-i-2026-11-14.md`  
Delivery: Complete report supplied here. No file created or edited.

## Verdict

The Algebra I frame’s curricular soundness remains unjudged because the required repository-wide plan check could not complete. The separate frame check passes, but that establishes structural consistency rather than complete standards treatment, instructional coherence or adequate pacing. Restore the checking environment, correct the verified stale notes below, and commission a fresh independent curriculum read.

## What I read and checked

Read the expert instructions, mathematics lens, mathematics rubric, Algebra I frame and its inline source map, `frames.csv` entry, and Grade 9 progression rows. Consulted the foundation, teaching approaches, source register, base-text policy, frame-writing brief, checking scripts, earlier mathematics reviews, and portions of the Grade 8 and Geometry frames.

I opened curriculum material while investigating the failed check. That exceeded the expert instruction to return the plan unread after failure, so this report withholds substantive curriculum judgments.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Default Python | Resolves to the installed office-suite Python |
| Existing alternative Python launcher | Could not launch its interpreter: permission denied |
| `python -B -X utf8 scripts/frame.py check algebra-i` | Zero failures; 7 units, 160 days, comprising 151 unit days and 9 remaining days |
| `python -B -X utf8 scripts/progression.py check math` | 305 rows, zero failures; advisory notes remain |
| `python -X utf8 scripts/stale.py check` | 56 files, zero failures |
| `python -X utf8 scripts/plan.py check algebra-i` | Zero items and zero wrong answers checked; this does not substitute for the full check |

The requested `data/plans/algebra-i/source-map.csv` does not exist. The frame-writing brief assigns that day-level file to the scope and sequence stage; its absence alone is not a frame defect.

## Findings, most serious first

### 1. The prerequisite plan check cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly reproduced

**Location:** `scripts/lesson.py:15`, imported during the repository-wide plan check.

**What is wrong:** The default interpreter cannot import `markdown`. The command terminates without producing a complete gate result. This is an environment failure, not evidence of an Algebra I curriculum defect.

**Why it matters:** `docs/agents/EXPERT.md` explicitly states: “If it fails, the plan goes back to its writer unread.” A passing structural frame check cannot replace this prerequisite.

**Exact fix:** Configure the review runner to use an accessible Python environment containing the repository’s required dependencies, including Python-Markdown. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any reported failures, then commission a fresh independent Algebra I frame read. Preserve the actual checking functions and dependency behavior.

**Earlier occurrence:** `docs/reviews/frame-math-grade-8-codex-2026-11-14.md`, finding 1.

### 2. The incoming frame incorrectly says the Algebra I and Geometry frames are unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly verified

**Location:** `docs/courses/math-grade-8/frame.md:66`.

**What is wrong:** The outgoing seam introduction says the Algebra I and Geometry frames “are not written.” Both files now exist.

**Why it matters:** The note gives a false reason to postpone checking both ends of the handoff required by this brief.

**Exact fix:** Replace the introduction with:

> Handed on to Algebra I and Geometry. Their current frames are `docs/courses/algebra-i/frame.md` and `docs/courses/geometry/frame.md`. The table below names the receiving progression rows.

This corrects availability only; it does not establish that the seams match.

**Earlier occurrence:** The Grade 8 review, finding 2. The correction remains unapplied in the current file.

### 3. Two incoming-frame notes incorrectly say N-Q.A.3 has no progression row

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly verified

**Locations:** `docs/courses/math-grade-8/frame.md:81` and `:158`.

**What is wrong:** Both notes explain a missing scientific-notation handoff by saying N-Q.A.3 has no row. The current progression places ownership in `geo-solving-right-triangles` and carries `~N-Q.A.3` in `alg1-scatter-linear-models`.

**Why it matters:** A fixer could undertake unnecessary ownership work or overlook Algebra I’s existing contribution when checking the seam.

**Exact fix:** Replace the scientific-notation seam cell with:

> No outgoing progression link is recorded. N-Q.A.3 is owned by `geo-solving-right-triangles` and begun in `alg1-scatter-linear-models`.

Replace the corresponding explanation in “For the lead,” item 6, with:

> `m8-scientific-notation` has no outgoing progression link. N-Q.A.3 already has an owner, `geo-solving-right-triangles`, and a beginning placement in `alg1-scatter-linear-models`.

Do not infer a new dependency from this status correction.

**Earlier occurrence:** The Grade 8 review, finding 3. Both statements remain in the current file.

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned skill placed exactly once | Structural frame check passes |
| Other-grade content justified as review or extension | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| School-year arithmetic | Structural result: 151 unit days plus 9 remaining days equals 160 |
| Instructional adequacy of unit allocations | Not adjudicated |
| Base-lesson completeness, order, cuts and licensing | Inline map present; verification incomplete |
| Incoming and outgoing seams | Not adjudicated |
| Cross-subject availability | Not adjudicated |
| Marked stale notes | Checker passes within its reported scope |
| Unmarked stale notes | Findings 2 and 3 verified; search incomplete |

### Mathematics lens: course frame checklist

| Checklist line | Disposition |
|---|---|
| Major work satisfies the applicable focus criteria | Unresolved |
| Supporting clusters practise major work | Unresolved |
| Every source-map row has a keep, split, merge, cut or ours decision | Not fully adjudicated |

These unresolved lines cannot honestly be marked met, missed or not applicable.

## Settled by the expert

| Choice | Reason | File or action affected |
|---|---|---|
| Withhold the curriculum verdict | Required full check did not complete | Review |
| Do not flag the absent day-level source-map CSV | The frame-writing brief schedules it for the next stage | None |
| Correct the unwritten-frame claim | Both receiving frames exist | Grade 8 seam introduction |
| Separate missing linkage from existing N-Q.A.3 ownership | The progression already places the standard | Grade 8 seam cell and lead item 6 |

## What is right and should not be touched

Preserve the passing structural results. The frame places its owned progression rows consistently with the checker and records a 160-day allocation. Those results alone justify no content, order or pacing changes.

## Outside sources and limits

- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): located the applicable high school focus criteria for the deferred review.
- [Base-text Algebra I course landing page](https://im.kendallhunt.com/HS/teachers/1/index.html): opened; lesson inventories and pacing were not independently verified.
- [Official Building Functions standards page](https://www.corestandards.org/Math/Content/HSF/BF/): retrieval failed.

The required outside-source curriculum study was not completed. No finding rests on remembered curriculum facts; prior-session memory informed reporting conventions only.

## For Cory

None arising from the established process findings. Existing scope and audience questions in the frame remain unadjudicated.

**Verdict:** Review incomplete; curriculum unjudged. **Finding count:** 3 process findings, including 1 blocker. **Report path:** `docs/reviews/frame-algebra-i-2026-11-14.md`, supplied above only.

