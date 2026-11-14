# Physics course frame: independent review

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-physics-2026-11-14.md`  
**Delivery:** Supplied here. No report file was written.

## Verdict

The curricular verdict is withheld because the required full plan gate could not complete. Focused checks confirm the frame’s mechanical placement and day totals, but the missing Python dependency prevents satisfying the expert’s prerequisite for a substantive read. Restore the check environment, pass the full gate, then complete the independent curriculum review.

**Finding count: 1 process finding.**

## What I read and ran

Read the expert instructions, science lens, science rubric, foundation, glossary, approach, relevant roadmap sections, BASELINE rules 20 to 24, science source-list entries and base-text rules.

During diagnosis I opened the physics frame, its `frames.csv` entry and grade 11 progression rows. I also inspected Chemistry’s incoming handoffs, relevant grade 11 ELA timing, the science progression reviews and fixes, and earlier science frame reviews. This was preliminary inspection, not a completed substantive cold read.

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Terminated with `ModuleNotFoundError: No module named 'markdown'` |
| Existing Python 3.12 launcher, same gate | Could not spawn its interpreter: permission denied |
| Direct Python 3.12 interpreter, same gate | Execution denied |
| `python -B -X utf8 scripts/frame.py check physics` | **0 failures:** 10 units, 160 days, including 149 unit days and 11 check and respond days |
| `python -B -X utf8 scripts/progression.py check science` | **198 rows, 0 failures**, with advisory notes |
| `python -X utf8 scripts/stale.py check` | **50 files, 0 failures** |

The focused checks are useful evidence, but they do not replace the required full gate.

## Findings

### 1. The required full plan gate cannot complete

**Severity:** Blocking for review completion  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `scripts/lesson.py:15`, imported during `scripts/plan.py check`; review-runner Python configuration.

**What is wrong:** The default `python` resolves to the interpreter bundled with LibreOffice. It lacks `markdown`, so the gate terminates before completing its checks. The existing Python 3.12 alternative cannot execute in this environment.

**Why it matters:** The expert instructions explicitly require: “If it fails, the plan goes back to its writer unread.” Consequently, this run cannot issue the requested curricular verdict under that workflow. This is an environment failure, not evidence of a defect in Physics.

**Exact fix:** Configure the review runner to use an executable Python environment containing the repository’s required dependencies. Then run:

```text
python -X utf8 scripts/plan.py check
```

After that gate passes, complete the physics review and replace this blocked report with the substantive findings. No curriculum edit is justified by this finding.

**Earlier occurrence:** The same dependency and alternative-interpreter failures appear in [the Grade 6 independent frame review](S:/CurioClass/docs/reviews/frame-science-grade-6-codex-2026-11-14.md). Current execution independently confirms the blocker remains.

## Required review coverage

| Requirement | Result |
|---|---|
| Owned skills placed exactly once | Mechanically confirmed by the focused physics frame check |
| Standards assigned to the correct unit rows | Mechanically confirmed |
| Every owned standard taught in full | Substantive judgment withheld |
| Unit purposes and prerequisite order | Substantive judgment withheld |
| Course days and check allowance | Arithmetic confirmed: 149 + 11 = 160 |
| Unit allocations fit their instructional load | Substantive judgment withheld |
| Base lesson placement, order and licensing | Not applicable: Physics explicitly has no base text |
| Incoming and outgoing seams | Inspected, substantive judgment withheld |
| Cross-subject instruction taught first | Inspected, substantive judgment withheld |
| Marked stale notes | Checker passed |
| Unmarked stale notes contradicted by current work | Review incomplete |

## Science lens checklist: course frame layer

| Lens line | Disposition |
|---|---|
| Every owned performance expectation has a unit and is taught sufficiently | Placement met mechanically; sufficiency unjudged |
| Grades 6 to 8 preserve the base-text order or justify departures without losing content | Not applicable |
| High school band expectations have named owning courses | Ownership structure passes the progression check; substantive allocation unjudged |
| Every unit names an anchor phenomenon or design problem | Met as a naming requirement; instructional quality unjudged |

## Settled by the expert

| Choice | Reason | File or destination affected |
|---|---|---|
| Withhold the curricular verdict | The mandatory full gate did not complete | This report |
| Classify the blocker as process | Runtime evidence identifies an environment failure | Review-runner configuration |
| Retain the focused check results as partial evidence | They establish precisely bounded mechanical facts | This report |
| Recommend no curriculum changes from this incomplete read | Substantive review requirements remain unfinished | None |

## What is right and should not be changed on this evidence

The focused gate confirms that all 20 Physics skill rows are placed once, their owning standards match their units, and the frame agrees with `frames.csv`. The 160-day total includes explicit course-level checks and respond time. These results provide no reason to alter ownership or day totals.

## What could not be judged

This run cannot establish full standard coverage, sound instructional sequencing, suitable unit pacing, adequate seams, cross-subject readiness or the absence of unmarked stale notes. Those judgments require completing the prescribed review after the full gate passes.

## Outside sources and memory

Preliminary standards consultation opened these primary sources. No curricular conclusion is claimed from that unfinished comparison.

- [NGSS DCI arrangements](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): full-standard reference.
- [Forces and interactions](https://www.nextgenscience.org/dci-arrangement/hs-ps2-motion-and-stability-forces-and-interactions): practices, core ideas and boundaries.
- [Energy](https://www.nextgenscience.org/dci-arrangement/hs-ps3-energy): energy-model requirements.
- [Waves and information transfer](https://www.nextgenscience.org/dci-arrangement/hs-ps4-waves-and-their-applications-technologies-information-transfer): wave, radiation and technology requirements.
- [Earth’s place in the universe](https://www.nextgenscience.org/dci-arrangement/hs-ess1-earths-place-universe): astronomy and early-Earth requirements.
- [Earth’s systems](https://www.nextgenscience.org/dci-arrangement/hs-ess2-earths-systems): interior and landform-model requirements.

Prior memory informed reporting conventions only. All reported command results were verified during this run; no curricular finding rests on memory.

## For Cory

None. This blocker requires an execution-environment repair, not a scope, money, people or audience decision.

**Verdict:** Review blocked, curricular verdict withheld.  
**Finding count:** 1 process finding.  
**Report path:** `docs/reviews/frame-physics-2026-11-14.md`, supplied above, not written.

