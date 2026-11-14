# Independent frame review: Science, Kindergarten

**Date:** 2026-11-14  
**Report path:** `docs/reviews/frame-science-kindergarten-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The frame is substantially sound but needs three local instructional corrections before the scope and sequence is written. Its largest remaining coverage risk is that the needs-and-places model omits air, an explicit part of the core idea supporting K-ESS3-1. Complete that model, remove the unsupported seasonal unit swap, and tighten the early weather-counting bridge while preserving the six units and 64 days.

## What I read

- `docs/agents/EXPERT.md`, the science lens, and `docs/RUBRIC-SCIENCE.md`.
- `docs/FOUNDATION.md`, `docs/APPROACH.md`, relevant roadmap sections, BASELINE rules, the glossary, the source register, the base-text record, and the science decisions dated November 12 and 13.
- The complete kindergarten science frame, its `frames.csv` row, all 11 kindergarten science progression rows, and the receiving progression rows.
- The complete grade 1 science frame. Kindergarten has no preceding science course.
- The kindergarten mathematics and ELA frames, plus relevant social studies connections.
- The earlier kindergarten reviews, the kindergarten-to-grade-2 fix record, and relevant science progression and neighboring-course reviews.
- Live outside sources listed below.

`docs/APPROACH-SCIENCE.md` does not exist. Kindergarten science has no base text, so the absent `data/plans/science-kindergarten/source-map.csv` is not a defect.

No curriculum finding below rests on memory.

## Gates

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check`, run first | Could not finish: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/stale.py check` | 56 files checked; one failure in the unrelated grade 7 ELA frame, line 32. |
| `python -X utf8 scripts/frame.py check science-kindergarten` | Passed: zero failures, six units, 64 days, including 58 unit days and six course-level days. |

The global-check limitation and unrelated stale-note failure do not withhold this curriculum verdict.

## Coverage, order and time

Every kindergarten progression skill appears exactly once in a Skills cell. No Skills cell claims another grade’s skill.

| Unit | Days | Owned skills | Standards |
|---|---:|---|---|
| 1. Pushes and pulls | 9 | `sk-push-pull` | K-PS2-1 |
| 2. Weather watch | 10 | `sk-weather-watch`; `sk-forecast-severe` | K-ESS2-1; K-ESS3-2 |
| 3. Ramps and targets | 9 | `sk-define-problem`; `sk-ramp-design` | K-2-ETS1-1; K-PS2-2 |
| 4. Living things and what they need | 12 | `sk-living-needs`; `sk-needs-places`; `sk-change-environment` | K-LS1-1; K-ESS3-1; K-ESS2-2 |
| 5. Sunlight warms | 11 | `sk-sun-warms`; `sk-shade-design` | K-PS3-1; K-PS3-2 |
| 6. Caring for our place | 7 | `sk-reduce-impact` | K-ESS3-3 |

The performance verbs, clarification examples and assessment boundaries are otherwise represented adequately at frame level. K-ESS3-1 needs the addition in finding 1. This judgment checks the official [kindergarten evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/Kindergarten%20Evidence%20Statements%20June%202015%20asterisks.pdf) and [engineering evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf), rather than counting codes alone.

The ordinary order holds: observing and cause-and-effect precede later investigations; weather introduces patterns; problem definition precedes ramp design within unit 3; living-needs patterns precede the place model and environmental argument within unit 4. Finding 2 concerns the optional alternative order.

The allocations are defensible. Unit 4 receives 12 lessons for three connected expectations; unit 5 receives 11 for observation and engineering; unit 6 receives seven for communicating and supporting a solution. No unit is demonstrably far over or under its workload.

The 64 sessions occupy 32 weeks at two sessions weekly, leaving approximately four weeks within the stated 36-week year. Four assessment sessions and two respond sessions are already included. The daily weather routine is additional time and is disclosed. Pacing remains a planning judgment until lessons are tried; the outside review guidance likewise asks for feasible pacing and reasoned scheduling, rather than prescribing a universal science-day total. [K–5 evidence guide, indicator 3i](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf).

## Findings, most serious first

### 1. The needs-and-places model omits air

**Location:** Science frame, unit 4, line 110; `sk-needs-places.notes`.  
**Severity:** Moderate. **LAYER:** standard. **REPEAT:** yes, incomplete standard coverage appeared in the earlier kindergarten finding 2. **Confidence:** firm.

**What is wrong:** The model connects organisms and places through food, water, sunlight and shelter, but never includes air. Its supporting core idea explicitly includes water, air and land resources. The progression’s vocabulary list contains “air” under `sk-living-needs`, but a vocabulary entry does not secure teaching or use in the model. [K-ESS3-1 evidence statement, foundation box and model components](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-ESS3-1%20Evidence%20Statements%20June%202015%20asterisks.pdf).

**Why it matters:** A writer can implement the frame faithfully and still omit an owned core-idea element. This is the same distinction between listing an expectation and fully developing its ideas that the [K–5 criteria, indicator 2a](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Review_20_Criteria_2_0_ddd732f02c.pdf) require.

**Exact fix:** Add to unit 4 and `sk-needs-places.notes`:

> The picture model includes water, air and resources from the land. Children identify air as a need of the plants, land animals and people shown, and connect local resources, such as water, soil and wood, to the needs they meet. No explanation of gases or breathing mechanisms is required.

Include these relationships in the unit’s unfamiliar-case model task. Keep the standard in unit 4 and retain its 12 days.

### 2. The permitted unit swap breaks a stated prerequisite

**Location:** Science frame, Models carried, line 98; unit 5, line 111; For the lead, item 3, lines 184–186.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** yes, science progression finding 9 identified models used before their introduction. **Confidence:** firm.

**What is wrong:** The seasonal note permits swapping units 4 and 5. Unit 5 explicitly uses the evidence sentence introduced in unit 4, and the Models carried table calls this use review. The swapped order therefore relies on instruction that has not happened.

**Why it matters:** Teachers following the permitted alternative lose the frame’s explanation-and-evidence progression. Coherent instruction must identify and build on earlier learning. [EQuIP, building progressions and unit coherence](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf).

**Exact fix:** Replace For the lead, item 3 with:

> **Seasonal order.** Keep units 4 and 5 in their stated order. Unit 4 uses saved fall photographs; unit 5 uses a suitable sunny day and its matched-material or no-kit alternative. Unit 5 follows unit 4 because it reuses the evidence sentence taught there. Unit 6 uses an outdoor pick-up where conditions permit.

This removes an unsupported alternative without moving any standard.

### 3. The weather-counting bridge needs a workable number limit

**Location:** Science frame, unit 2, line 108; Mathematics cross-subject table, line 145.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** yes, cross-subject readiness and bridges recur in earlier frame reviews. **Confidence:** likely.

**What is wrong:** The early bridge says “numbers within 20.” Mathematics is still developing quantities within ten during this period; counting collections to 20 is owned in mathematics unit 6. Moreover, a complete month can contain more than 20 observations of one condition, so the stated ceiling does not reliably fit the required record.

**Why it matters:** A writer could either demand untaught independent counting or shorten the record to fit the ceiling. Neither is necessary: teacher-supported counting and picture comparisons can preserve the weather investigation.

**Exact fix:** Replace the bridge with:

> Keep the complete daily record. Children compare rows by matching picture squares and count selected groups of up to ten with support. The teacher counts and labels larger totals, which children use with the picture rows to discuss monthly patterns. Independent counting of larger collections is not assessed before mathematics teaches it.

Apply the same limit to the unit plan and early assessment directions. Preserve whole-number observations and the monthly comparison required by [K-ESS2-1](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/Kindergarten%20Evidence%20Statements%20June%202015%20asterisks.pdf).

### 4. The science rubric understates the planning material that exists

**Location:** `docs/RUBRIC-SCIENCE.md`, lines 54–55.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, explicitly reported in grade 1 science finding 6 and carried forward in the fix record. **Confidence:** firm.

**What is wrong:** The rubric calls the grade 4 scope and sequence and middle school base text the “only material.” The science progression and course frames now exist.

**Why it matters:** The active review guide can send later readers past relevant evidence.

**Exact fix:** Replace that paragraph with:

> Science planning material includes the science progression, course frames, the grade 4 scope and sequence draft, and the middle school base text. These establish planning commitments; they do not establish that a finished science course exists.

### 5. The rubric’s nature-of-science gap is already partly closed

**Location:** `docs/RUBRIC-SCIENCE.md`, Gateway 2 connections row, line 64.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, stale planning-status notes recur in the earlier reviews. **Confidence:** firm.

**What is wrong:** “No plan names where the nature of science is taught” is contradicted by the kindergarten frame’s Practices across the year bullet, which assigns this work to units 1, 2 and 4.

**Why it matters:** The note confuses an existing planning commitment with the later task of demonstrating it in lessons.

**Exact fix:** Replace the gap sentence with:

> Course frames now name planned locations for nature-of-science learning. Scope and sequence, unit and lesson reviews must verify that students actually do this work.

### 6. ELA’s weather bridge retains the old science chronology

**Location:** `docs/courses/english-language-arts-kindergarten/frame.md`, line 103.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, identified in the kindergarten-to-grade-2 fix record’s cross-subject notes. **Confidence:** firm.

**What is wrong:** The bridge says science’s recording “deepens them later.” Science now starts recording in week 1 and teaches its weather unit approximately during weeks 5–10, overlapping ELA’s weather work from about week 7.

**Why it matters:** The outdated chronology obscures an available shared record.

**Exact fix:** Replace the final clause with:

> Science’s weather chart is already running from week 1, and its weather unit overlaps this work. Use that record where available; otherwise the ELA texts and picture journal supply the observations needed here.

### 7. Earlier reviews still present missing ELA frames as a current limitation

**Location:** Earlier kindergarten expert report, lines 13, 121 and 135; neighboring grade 1 independent report, line 131.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, stale availability notes are an established review finding. **Confidence:** firm.

**What is wrong:** These passages say the relevant ELA frame is absent or unwritten. Those frames exist, and the science fix record already incorporates their timing.

**Why it matters:** A reader can mistake a valid historical limitation for an outstanding prerequisite.

**Exact fix:** Preserve the original observations as dated history, but replace the present-tense availability notes with a current-status addendum:

> At the earlier read, the ELA frame was unavailable. It now exists, and the science frame records its unit timing. For kindergarten, SL.K.3, SL.K.5 and W.K.2 are available before the identified science uses; W.K.1 arrives later and science uses its stated spoken-and-dictated bridge.

For the grade 1 report, state that the ELA frame now exists and timing is recorded in the revised science frame. Do not imply that this kindergarten review independently re-reviewed every grade 1 ELA dependency.

## Seams and cross-subject checks

There is no incoming science-course seam. Unit 1 explicitly builds observing and recording habits without assuming prior science instruction.

Every outgoing kindergarten `hands_on` entry has a reciprocal `assumes` entry in its receiving progression row. Grade 1 picks up the weather-record habit, needs and systems, problem definition, evidence-supported claims, motion, sunlight and shade. Longer handoffs to grades 2–4 are named rather than presented as immediate grade 1 content.

Mathematics’ direct-comparison bridges for early motion work are appropriate. Weather counting needs finding 3. The ELA timing is now checkable: its questioning, informative communication and drawing supports precede the named science uses; the later opinion-writing standard has an explicit spoken bridge. Science does not assume kindergarten social studies content.

## Science lens checklist: course frame layer

| Checklist line | Result | Evidence |
|---|---|---|
| Every grade performance expectation has a unit and is fully represented | **Missed in part** | All are placed; finding 1 identifies an omitted supporting core-idea element. |
| Grades 6–8 preserve base-text order and check losses | **Not applicable** | Kindergarten has no base text. |
| High-school expectations have clear course owners | **Not applicable** | Kindergarten course. |
| Every unit names an anchor phenomenon or design problem | **Met** | All six identify an observable event, record or design problem. |

## What is right and should remain

Keep the week 1 weather routine, saved fall photographs, human case in the place model, and individual unfamiliar-case tasks. These earlier fixes are present and are not reopened.

Also preserve the connected engineering units, revised class models, spoken and visual vocabulary, teacher-held records, explicit respond days, materials alternatives, and sensitive handling of severe-weather experiences. Young children can engage in causal explanation and investigation with suitable support; reducing this course to naming and sorting would weaken it. [Taking Science to School, chapter 3, read in part](https://www.nationalacademies.org/read/11625/chapter/5).

## Settled by the expert

These are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File affected |
|---|---|---|
| Keep six units and 64 sessions, with existing allocations | No demonstrated load imbalance warrants moving days | Science frame; `frames.csv` |
| Include air and explicit land-resource relationships in unit 4’s model | Completes an already-owned core idea | Science frame; `sk-needs-places.notes` |
| Keep unit 4 before unit 5 | Preserves the stated evidence-sentence prerequisite | Science frame, For the lead item 3 |
| Keep complete weather records and scaffold larger counts | Preserves science evidence without demanding untaught independent mathematics | Science frame, cross-subject bridge |
| Retain the unfamiliar-case task in every unit | Distinguishes transfer from rehearsing the anchor | Science frame; subsequent unit plans |

## What I could not judge

This frame does not establish lesson feasibility, assessment scoring quality, complete band-wide practice-element coverage, actual materials costs, or final investigation safety. Those require the later scope and sequence, unit plans, assessment items and investigation sheets.

The missing science approach page remains missing, so that status note is accurate. No full course score is assigned from a frame.

## Outside sources and access limits

All sources below were accessed live, at the portions described.

- [Official standards, DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): kindergarten expectations, core ideas and boundaries.
- [Kindergarten evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/Kindergarten%20Evidence%20Statements%20June%202015%20asterisks.pdf) and [engineering statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf): required performances.
- [Appendix E](https://www.nextgenscience.org/sites/default/files/resource/files/AppendixE-ProgressionswithinNGSS-061617.pdf), [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf), and [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf): relevant early-grade progression passages.
- [EQuIP rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence, prior learning and three-dimensional tasks.
- [Current K–5 criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Review_20_Criteria_2_0_ddd732f02c.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf): selected coverage and pacing indicators.
- [Elementary sunlight overview](https://openscied.org/instructional-materials/k-1-energy-sunlight/) and [plants-and-animals overview](https://openscied.org/instructional-materials/k-4-ecosystems-plants-animals/): reference comparison of phenomenon, investigation and design organization.
- [Core Knowledge K–2 pacing guide](https://www.coreknowledge.org/wp-content/uploads/2023/09/CKCurriculumPacingGuides_k-2.pdf): a second public curriculum comparison. Its different scope and schedule are not a pacing mandate.

The direct elementary reference scope-and-sequence download returned HTTP 403. Public unit descriptions were available; full reference lessons were not reviewed or copied.

### For the source list

Record the current K–5 criteria address above, the direct kindergarten evidence-statement links, and the accessible elementary unit-overview addresses. Record the blocked scope-and-sequence download as an access limitation.

## For Cory

- **Audience and time:** Confirm the proposed two 30-minute kindergarten science sessions weekly, plus the daily weather routine.
- **Money:** Confirm or revise the proposed $40 annual classroom materials ceiling after quantities are estimated.
- **People:** Arrange the disaster-aware reader and required investigation-safety reader before the relevant completion decisions.

**Verdict:** Revise locally before scope-and-sequence writing. **Finding count:** 7, comprising 3 instructional findings and 4 process findings. **Report path:** `docs/reviews/frame-science-kindergarten-2026-11-14.md`, supplied here without creating or changing a file.