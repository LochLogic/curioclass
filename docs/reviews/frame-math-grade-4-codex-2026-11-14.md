# Grade 4 mathematics frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-4-2026-11-14.md`

Report supplied here only. No report file was written.

## Verdict

The frame’s curricular soundness remains unjudged because the required full plan gate could not complete. Separate frame checks passed, but they do not establish the prerequisite result required by the expert instructions. Restore the check environment and obtain a passing full gate before completing the independent curriculum review.

## What I read and checked

Read `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the Grade 4 frame, its `frames.csv` row, all 27 Grade 4 progression rows, and the Grade 4 standards text.

Also consulted the foundation, teaching approach, source policy, neighboring mathematics frames, the Grade 4 ELA frame, existing source-map data, the base lesson inventory, checker code, and earlier mathematics and frame reviews. Some supporting documents were inspected in excerpts.

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Exit 1: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternative Python launcher | Could not launch its interpreter: permission denied |
| `python -B -X utf8 scripts/frame.py check math-grade-3 math-grade-4 math-grade-5` | Zero failures for all three frames |
| `python -X utf8 scripts/stale.py check` | 55 files checked, zero failures |

The Grade 4 frame gate confirmed nine units, 145 days within units, and 15 remaining course days. Its skill-placement and owned-code checks passed.

The requested `data/plans/math-grade-4/source-map.csv` does not exist. An older map exists at `data/plans/math-4/source-map.csv`, and the frame contains an inline source map. Their curricular reconciliation remains unjudged.

EXPERT.md says: “If it fails, the plan goes back to its writer unread.” I opened curriculum material before enforcing that stop rule. Consequently, this report records an incomplete review and does not issue substantive curriculum findings.

No dependency installation, turn mutation, or defect-ledger write was performed.

## Findings, most serious first

### 1. The required full plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed runtime failure

**Location:** `scripts/lesson.py:15`, imported during the full plan check.

**What is wrong:** The default Python interpreter lacks the `markdown` dependency. The check terminates before producing its complete result.

**Why it matters:** The expert’s prerequisite remains unsatisfied. Passing the separate frame gate establishes structural facts, but cannot substitute for the full check or authorize a curriculum verdict under the standing review instructions.

**Exact fix:** Configure the review runner to use an existing Python environment containing the required dependencies, or provision them outside this read-only session. Then rerun:

```text
python -X utf8 scripts/plan.py check
```

Resolve any failures it reports. Once it passes, commission a fresh independent read covering the complete brief.

**Earlier occurrence:** The same environment blocker appears in `docs/reviews/frame-science-grade-3-codex-2026-11-14.md`, finding 1, and `docs/reviews/frame-math-grade-2-codex-2026-11-14.md`, finding 1.

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned skill placed exactly once | Structural frame check passed |
| Every standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| Course days and unit allocations | Structural totals passed; instructional load not adjudicated |
| Complete, licensed source map and justified departures | Not adjudicated |
| Grade 3 and Grade 5 seams | Not adjudicated |
| Cross-subject availability | Not adjudicated |
| Marked stale notes | Automated check passed |
| Unmarked stale notes | Review incomplete |

### Mathematics lens checklist, course frame layer

| Checklist line | Disposition |
|---|---|
| Major work meets the line by units, lessons, and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row has a keep, split, merge, cut, or ours decision | Not adjudicated |

These cannot honestly be marked met, missed, or not applicable while the prerequisite review is blocked.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Withhold a curriculum verdict | The full prerequisite gate has no completed result | This report |
| Retain separate frame results as partial evidence | They establish structure within their stated scope | This report |
| Settle no mathematical or pacing changes | The substantive review is incomplete | None |

## What is right and should not be touched

The frame’s structural checks pass, including its nine-unit count, skill placement, owned-code correspondence, and day totals. Those results should be retained as evidence without extending them into claims about teaching quality or standards completeness.

## Outside sources and memory

Preliminary outside research reached:

- [Grade 4 focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_4.pdf), for major-work classifications and required fluency.
- [K–8 mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf), for the review framework.
- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-4/course-guide/scope-and-sequence.html), for source order.
- [Comparison curriculum map](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum%20Map/EM_GPK5_CurriculumMap.pdf), for an alternative sequence.

The [compiled Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf) exceeded the web tool’s size limit. Outside research was not completed, and no curriculum conclusion rests on these preliminary reads or on memory. Prior session memory informed report structure only.

## For Cory

None. The blocker requires an environment repair, with no scope, money, people, or audience decision identified.

**Verdict:** Unjudged pending the full gate. **Finding count:** 1 process blocker. **Report path:** `docs/reviews/frame-math-grade-4-2026-11-14.md`, supplied here, not written.

