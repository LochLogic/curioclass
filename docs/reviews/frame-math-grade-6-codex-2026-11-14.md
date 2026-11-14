# Grade 6 mathematics frame review, 2026-11-14

Intended report path: `docs/reviews/frame-math-grade-6-2026-11-14.md`

Report supplied here only. No report file was created.

## Verdict

The frame’s curricular soundness remains unjudged because the required full plan gate could not complete. The course-only check and stale-note check passed, but neither establishes the prerequisite full-gate result. Restore the checking environment and obtain a passing full gate before completing the independent curriculum review.

## What I read and checked

Read the expert instructions, mathematics lens, mathematics rubric, foundation, Grade 6 frame, its `frames.csv` row, and Grade 6 progression rows. Consulted adjacent mathematics frames, teaching approach documents, source guidance, plan-data documentation, checker code, and earlier mathematics reviews. Some supporting material was inspected in excerpts.

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Failed with `ModuleNotFoundError: No module named 'markdown'` |
| Default Python | Resolves to the LibreOffice Python environment |
| `python -B -X utf8 scripts/plan.py check math-grade-6` | Zero failures, zero items and zero wrong answers checked |
| `python -B -X utf8 scripts/stale.py check` | 56 files, zero failures |
| Requested `data/plans/math-grade-6/source-map.csv` | File does not exist; the frame contains an inline source map |

The course-only result does not validate the frame’s full standards coverage or instructional quality.

[EXPERT.md](/S:/CurioClass/docs/agents/EXPERT.md) requires: “If it fails, the plan goes back to its writer unread.” I continued reading after the failure, contrary to that instruction. Consequently, this report records an incomplete review and issues no substantive curriculum findings.

No turn mutation, dependency installation, defect-ledger write, or report-file write was performed.

## Findings, most serious first

### 1. The prerequisite full plan gate cannot complete

**Severity:** Blocking  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm, directly observed runtime failure

**Location:** [scripts/lesson.py:15](/S:/CurioClass/scripts/lesson.py:15), imported during the full plan check.

**What is wrong:** The default Python environment cannot import `markdown`. The checker terminates before reporting its complete result. This establishes an environment blocker, not a Grade 6 curriculum defect.

**Why it matters:** The expert instructions make a passing full gate a prerequisite for the curricular read. A zero-item course check cannot establish that prerequisite.

**Exact fix:** Configure the review runner to use a Python environment containing the repository’s required dependencies, including Python-Markdown. Rerun the unchanged command:

```text
python -X utf8 scripts/plan.py check
```

Resolve any failures it reports, then commission a fresh independent Grade 6 frame read. Do not modify the checker or substitute an import stub.

**Earlier occurrence:** The same missing dependency is documented in [the Grade 5 mathematics review](/S:/CurioClass/docs/reviews/frame-math-grade-5-codex-2026-11-14.md), finding 1, and [the Grade 4 mathematics review](/S:/CurioClass/docs/reviews/frame-math-grade-4-codex-2026-11-14.md), finding 1.

## Required review coverage

| Requirement | Status |
|---|---|
| Every owned progression skill placed exactly once | Not adjudicated |
| Other grades’ skills explicitly identified as review or extension | Not adjudicated |
| Every owned standard taught in full | Not adjudicated |
| Unit purposes and prerequisite order | Not adjudicated |
| School-year allocation and unit instructional load | Not adjudicated |
| Complete source mapping, justified departures, and licensing | Not adjudicated |
| Grade 5 and Grade 7 seams | Not adjudicated |
| Same-grade cross-subject prerequisites | Not adjudicated |
| Marked stale notes | Automated check passed |
| Unmarked stale notes and outdated review results | Review incomplete |

### Mathematics lens checklist, course frame layer

| Checklist line | Disposition |
|---|---|
| Major work meets the required share by units, days, and time | Not adjudicated |
| Supporting clusters practise major work | Not adjudicated |
| Every source-map row has a keep, split, merge, cut, or ours decision | Not adjudicated |

These lines cannot honestly be marked met, missed, or not applicable while the prerequisite remains unsatisfied.

## Settled by the expert

| Choice | Reason | File or action affected |
|---|---|---|
| Withhold the curriculum verdict | The required full gate did not complete | This report |
| Retain the course-only and stale-check results as limited evidence | Their reported scopes are narrower than the requested review | Subsequent review |
| Make no curriculum recommendations from this incomplete read | Coverage, sequence, and pacing have not been adjudicated | None |

## What is right and should not be touched

No curricular feature was established as sound by this incomplete review. Preserve the frame pending the substantive read.

## Sources and limits

Preliminary outside research reached:

- [K–8 mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): opened for the review framework; indicator-level verification was not completed.
- [Grade 6 comparison curriculum](https://www.fishtanklearning.org/curriculum/math/6th-grade/): opened; sequence comparison was not completed.
- [Federal mathematical problem-solving practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16/Published): recommendation summary inspected.

The [compiled Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf) exceeded the web tool’s size limit. The attempted base-text course-guide address was inaccessible.

No curricular conclusion rests on these preliminary sources or on memory. Prior session memory informed reporting conventions only.

## For Cory

None. The identified blocker requires an environment repair, with no scope, money, people, or audience decision identified.

**Verdict:** Unjudged pending the required full gate. **Finding count:** 1 blocking process finding. **Report path:** `docs/reviews/frame-math-grade-6-2026-11-14.md`, supplied here without creating the file.

