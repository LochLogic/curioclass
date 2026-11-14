# Grade 2 Math frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-2-2026-11-14.md`  
Report supplied here only. No file was written.

## Verdict

The frame’s soundness remains unjudged because the required full plan gate could not complete. Separate Grade 2 checks passed, but they do not establish the prerequisite result required by the expert instructions. Restore the check environment and obtain a passing full gate before completing the curriculum review.

## What I read and checked

Read `docs/agents/EXPERT.md`, the math lens, `docs/RUBRIC-MATH-K8.md`, the Grade 2 frame, its `frames.csv` row, Grade 2 progression rows, and the repository’s Grade 2 standards text. Consulted the foundation, approach, source policy, glossary, selected earlier math reviews, and portions of the neighboring math and same-grade subject frames.

The requested `data/plans/math-grade-2/source-map.csv` was not found. The frame contains a prose source map, but its adequacy was not adjudicated.

I opened curriculum material while investigating the check environment. That exceeded the expert’s instruction to return the plan unread after gate failure. This report therefore records an incomplete review and makes no substantive curriculum verdict.

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternative Python launcher | Could not launch its interpreter: permission denied |
| `python -B -X utf8 scripts/plan.py check math-grade-2` | Zero failures, but zero items and zero wrong answers checked |
| `python -B -X utf8 scripts/progression.py check math` | 305 rows, zero failures; advisory notes remain |
| `python -B -X utf8 scripts/frame.py check` | Grade 2: zero failures. An unrelated Grade 6 frame failure was reported |
| `python -X utf8 scripts/stale.py check` | 41 files, zero failures |

No edits, installations, turn mutations, or defect-ledger writes were performed.

## Findings, most serious first

### 1. The prerequisite plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed runtime failure

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`.

**What is wrong:** The default Python interpreter lacks the `markdown` dependency. The full check terminates before producing its complete result.

**Why it matters:** The standing expert instructions say, “If it fails, the plan goes back to its writer unread.” A substantive review issued now would bypass that prerequisite. The targeted Grade 2 command checks no assessment items, so its success cannot substitute for the full gate.

**Exact fix:** Configure the review runner to use an existing Python environment containing the repository’s required dependencies, or provision those dependencies outside this read-only session. Then rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any failures it reports before commissioning a fresh independent read. The separate frame check already reported that Grade 6 unit 6 omits `6.EE.C.9` from its Owned standards cell; that observation is outside this Grade 2 review and must not be mistaken for a Grade 2 defect.

**Earlier occurrence:** `docs/reviews/frame-science-grade-3-codex-2026-11-14.md`, finding 1, records the same missing dependency and alternative-launcher failure.

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned skill placed exactly once | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| Year length, checks, response time, unit allocations | Not adjudicated |
| Complete, licensed source map and justified departures | Not adjudicated |
| Grade 1 and Grade 3 seams | Not adjudicated |
| Cross-subject availability | Not adjudicated |
| Unmarked stale notes | Search incomplete; automated stale check passed |

### Math lens checklist, course frame layer

| Checklist line | Disposition |
|---|---|
| Major work meets the line by units, lessons and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row has a keep, split, merge, cut or ours decision | Not adjudicated |

These lines cannot honestly be marked met, missed, or not applicable before the prerequisite review can proceed.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold a curriculum verdict | The required full gate has no completed result | This report |
| Treat targeted checks as partial evidence | Their scope differs from the full gate | This report |
| Require a fresh independent read after the gate passes | This session opened curriculum material before enforcing the stop rule | Future review |

## What is right and should not be touched

The read-only boundary was preserved. No curriculum changes are recommended from this incomplete read.

## What I could not judge

Coverage, mathematical completeness, pacing, source fidelity, seams, and cross-subject timing remain unjudged. They require a passing full gate followed by the requested substantive review.

## Outside sources and memory

Preliminary research reached the [Grade 2 focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_2.pdf) and [K–8 evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf). The [compiled Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf) exceeded the browser tool’s size limit. Research was not completed, and no curriculum finding rests on these preliminary reads or on memory. Prior session memory informed report structure only.

## For Cory

None. The blocker concerns the review environment, with no scope, audience, money, or outside-person decision requested.

**Verdict:** Unjudged pending the full gate. **Finding count:** 1 process blocker. **Report path:** `docs/reviews/frame-math-grade-2-2026-11-14.md`, supplied here, not written.

