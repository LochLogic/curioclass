# Expert cold read: Science, Grade 1 course frame

**Review date:** 2026-11-14  
**Intended report:** `docs/reviews/frame-science-grade-1-2026-11-14.md`  
**Delivery:** Complete report below. No report or repository file was written.

## Verdict

The frame has a coherent order, complete structural ownership, and a plausible 68-session year, but needs revision before unit planning. Its largest risk is incomplete plant coverage hidden behind otherwise strong animal examples and correctly assigned standard codes. Make plant parent-and-young comparisons required in unit 3 and explicitly include plants responding to environmental inputs in unit 2, while preserving the unit order and day allocations.

## What I read

- `docs/agents/EXPERT.md`, the science lens, and `docs/RUBRIC-SCIENCE.md`.
- `docs/FOUNDATION.md`, the relevant Roadmap planning and gap sections, BASELINE rules 20 to 24, and the glossary.
- The complete grade 1 science frame, its `frames.csv` entry, and all ten grade 1 science progression rows.
- The neighboring kindergarten and grade 2 science frames.
- The grade 1 mathematics frame and the relevant calendar and daylight provisions in grade 1 social studies.
- The base-text policy and source register. Grade 1 science has no base text or source map.
- Relevant earlier science progression findings, their fix and reconciliation reports, the grade 4 science review, and comparable course-frame findings.
- Live external standards, evidence statements, review guidance, and curriculum references linked below.

The grade 1 ELA frame and `APPROACH-SCIENCE.md` were absent. No substantive finding rests solely on remembered source content. Pacing judgments and proposed classroom examples are professional judgments.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: importing `lesson.py` raised `ModuleNotFoundError: No module named 'markdown'`. |
| `python -B -X utf8 scripts/frame.py check science-grade-1` | Passed: zero failures; 8 units, 68 days, including 62 unit days and 6 course assessment and respond days. |
| `python -B -X utf8 scripts/progression.py check science` | Passed: 198 rows, zero failures; handoff notes remain. |
| `python -X utf8 scripts/stale.py check` | Passed: 32 files, zero failures. |

The full plan gate remains unverified. Its interruption was an environment dependency error, so it established no curriculum failure. The relevant focused checks completed successfully.

## Findings, most serious first

### 1. Unit 3 makes the necessary plant parent-and-young comparison optional

**Severity:** High  
**LAYER:** standard  
**REPEAT:** yes, incomplete plant coverage also appears in the earlier grade 4 science review  
**Confidence:** firm

**Location:** Grade 1 frame, unit 3, especially “What students learn” and “Check set adds”; progression row `s1-like-parents`.

**What is wrong:** The required plant observation uses leaves gathered from one tree. Those leaves show variation among parts of one organism. They do not establish resemblance between young plants and their parents. Actual young-and-parent plant evidence appears only as a candidate addition. Animal parent-and-young comparisons are required.

**Why it matters:** A writer following the main path could complete the unit without evidence for the plant half of the claimed performance. The official evidence statement includes observations of young and adult plants and patterns between parents and offspring. [Grade 1 life science evidence statements, PDF page 4](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf#page=4).

**Exact fix:**

- Keep the leaf collection as an opening observation.
- Move the plant parent-and-young comparison into required learning.
- Use documented photographs of a parent plant and young plants grown from its seeds, or a live equivalent with photographs available as the fallback.
- Require children to identify a shared feature and a difference, then support an account covering both plants and animals.
- Align `s1-like-parents.notes` and require a fresh plant comparison in the unit assessment.

Keep the six days. Replace some repeated animal comparison work with the plant comparison.

### 2. Unit 2 does not explicitly teach plants responding to environmental inputs

**Severity:** Medium  
**LAYER:** standard  
**REPEAT:** yes, omission of a required core-idea element is an established science-review finding type  
**Confidence:** likely

**Location:** Grade 1 frame, unit 2; progression row `s1-parts-mimic`.

**What is wrong:** The description explicitly teaches animals sensing and responding. Its plant examples describe parts and jobs, including leaves facing light, without specifying an observable plant response to a changed input. The optional addition is another animal response.

**Why it matters:** The core idea attached to `1-LS1-1` includes plants responding to external inputs. A static part-and-job chart can omit that element while the frame continues to claim the expectation in full. [Official grade 1 core ideas, PDF page 12](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf#page=12).

**Exact fix:** Add this required provision to unit 2 and the progression note:

> Compare a dated photograph sequence showing a young plant’s shoot changing its growth direction toward light. Children identify what changed around the plant and the response they observed. Add the example to the part-and-job chart and revisit it in a short check.

Use a prepared photograph sequence if classroom growth is inconclusive. Keep the explanation observational, without hormones or cellular mechanisms. This fits within the existing twelve days.

### Stale-note findings

Each numbered row is a separate finding.

**Severity:** Low  
**LAYER:** process  
**REPEAT:** yes, stale planning notes were identified in earlier progression and frame reviews  
**Confidence:** firm

| # | Location and what is wrong | Why it matters | Exact replacement |
|---|---|---|---|
| **3** | Grade 1 science frame, Cross-subject introduction, lines 145 to 146: other subjects’ frames are described as being written later. Grade 1 mathematics and social studies frames now exist. | Leaves a resolvable timing comparison presented as future work. | “The grade 1 mathematics and social studies frames are available. Mathematics unit 1 supplies three-category data work; unit 6 supplies formal length ordering and measurement. Science uses its direct-comparison bridge in unit 3 and its supported measurement bridge where needed in unit 6. The ELA frame is pending, so its timing remains unverified.” |
| **4** | Kindergarten science frame, Cross-subject introduction, lines 129 to 130: other subjects’ frames are described as being written later. Kindergarten mathematics and social studies frames exist. | Sends the next reader toward an outdated dependency status. | “The kindergarten mathematics and social studies frames are available for the timing comparison. The kindergarten ELA frame is pending. The table below records science’s first need and its bridge where another subject teaches the skill later.” |
| **5** | Grade 1 mathematics frame, Cross-subject introduction, lines 143 to 144: other subjects’ frames are described as being written later. Grade 1 science and social studies frames exist. | Obscures the opportunity to close the reciprocal availability checks now. | “The grade 1 science and social studies frames are available. Mathematics teaches three-category data work in unit 1 before science uses it. Science’s early leaf comparison uses its stated direct-comparison bridge before formal length work in mathematics unit 6. ELA timing remains pending its frame.” |
| **6** | `docs/RUBRIC-SCIENCE.md`, lines 54 to 55: the grade 4 scope and sequence and middle school base text are called the only material. The science progression and course frames now exist. | The active bar understates available planning evidence and can misdirect later reviews. | “Science planning material now includes the science progression, course frames, the grade 4 scope and sequence draft, and the middle school base text. These establish planning commitments; they do not establish that a finished science course exists.” |

These statements escape the current stale-note checker. Historically dated observations in earlier reports were not counted merely because the repository has since changed.

## Ownership, standards, order and days

All ten owned progression skills appear in exactly one owning unit. Review and extension uses are identified sufficiently to distinguish them from ownership.

| Unit | Days | Owned skills and standards | Expert judgment |
|---|---:|---|---|
| 1. Sun, moon and stars | 8 | `s1-sky-patterns`; `1-ESS1-1` | Appropriate opening for the observation habit and sky predictions. |
| 2. Parts that help | 12 | `s1-parts-mimic`, `s1-sketch-shape`; `1-LS1-1`, `K-2-ETS1-2` | Largest allocation is justified by observation, biological examples, modelling and construction. Finding 2 applies. |
| 3. Like their parents | 6 | `s1-like-parents`; `1-LS3-1` | Reasonable after naming external parts. Finding 1 applies. |
| 4. Sound | 7 | `s1-sound-vibrates`; `1-PS4-1` | Both directions of the sound and vibration relationship are planned. |
| 5. Light | 10 | `s1-see-with-light`, `s1-light-materials`; `1-PS4-2`, `1-PS4-3` | Two investigations justify the allocation; illumination and the four material effects are represented. |
| 6. Sending a message | 8 | `s1-signal-device`; `1-PS4-4` | Correctly follows sound, light and planned sketches. Time allows building and testing. |
| 7. Parents and young | 6 | `s1-parent-offspring`; `1-LS1-2` | Texts and media support identifying signal-and-response patterns. |
| 8. Daylight and seasons | 5 | `s1-daylight-seasons`; `1-ESS1-2` | Defensible because observations continue outside the counted lessons. |

The nine grade-specific expectations and the assigned engineering expectation are all placed. Findings 1 and 2 qualify the claim of full substantive coverage. The remaining expectations have adequate frame-level teaching commitments against the [official standards](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf).

The 62 unit sessions plus four course assessment sessions and two respond sessions fit 34 weeks at two sessions weekly. No unit is demonstrably far over or under its share. Actual feasibility still requires lesson timing.

Keep the split daylight unit: one fall launch and four spring sessions, counted once. Its observation method has an explicit fallback where dismissal remains in daylight throughout the year. Fixed-time observations are consistent with the examples in the [official daylight evidence statement, PDF page 24](https://www.nextgenscience.org/sites/default/files/Elem%20%2B%20Exec%20Summary%20June%202015.pdf#page=24).

## Seams and cross-subject timing

The neighboring science frames substantiate the main handoffs:

- Kindergarten supplies observation records, needs, systems, simple design and evidence-backed claims.
- Grade 1 introduces structure and function before the planned sketch and later communication device use it.
- Grade 2 picks up material properties, design comparisons, information from multiple sources, written accounts and plant investigations.
- Long-range content links are distinguished from immediate grade 2 practice links.

The mathematics comparison supports three-category data work being available first. Formal length ordering comes later than science unit 3, so retain the direct, aligned-end comparison bridge. Mathematics itself acknowledges that bridge. Measurement instruction and science unit 6 occur near one another; retain science’s explicit modelling of equal units and no gaps.

The mathematics reference to seasonal data creates no instructional cycle: mathematics begins with class data, then science reuses the method. Social studies can begin its calendar before science draws a seasonal daylight conclusion.

ELA teaching-first order remains **unverified** because its frame is absent. Read-alouds, dictation, teacher modelling and sentence frames provide useful interim access.

## Science lens checklist: course-frame layer

| Checklist line | Result | Evidence |
|---|---|---|
| Every grade performance expectation has a unit, and claimed expectations are taught fully | **Missed substantively** | Structural placement passes; findings 1 and 2 identify incomplete teaching commitments. |
| Grades 6 to 8 preserve base-text order and check losses from changes | **Not applicable** | Grade 1 has no base text. |
| High school band expectations have clear course owners | **Not applicable** | Elementary course. |
| Every unit names an anchor phenomenon or design problem | **Met** | All eight units name an observable event, continuing record or design problem. |

The frame also commits to question boards, connected investigations, revised class models, safety controls and materials alternatives. Those commitments are appropriate. Whether lessons actually deliver them, and whether unit assessments demonstrate transfer, belongs to the subsequent artifact reads. [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf).

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | File or rows touched |
|---|---|---|
| Keep all eight units in their current order | Prerequisites precede dependent designs and explanations. | Grade 1 science frame |
| Keep 68 sessions and the existing unit allocations | No demonstrated workload imbalance warrants moving days. | Frame and `frames.csv` |
| Require plant parent-and-young evidence within unit 3 | Completes the already-owned expectation without moving it. | Unit 3; `s1-like-parents.notes` |
| Add an observable plant-response example within unit 2 | Makes the existing core-idea obligation explicit. | Unit 2; `s1-parts-mimic.notes` |
| Keep the split daylight unit and count its launch once | Seasonal evidence needs a continuing record. | Frame and future scope and sequence |
| Preserve supported direct comparison before formal mathematics length instruction | The early science task can remain accessible within its existing bridge. | Cross-subject notes and unit 3 |

## What is right and should be preserved

The frame gives real reasons for its order. Biology supplies useful design knowledge; sound and light precede communication; the daylight record runs across the year. Spoken and visual vocabulary, optional home observations, animal-based family examples, materials alternatives and explicit safety cautions are strong provisions.

The course-level checks use unfamiliar cases and each has a respond day. Keep both features.

## What I could not judge

This read does not establish lesson feasibility, assessment quality, element-by-element practice coverage, working materials substitutions, costs or final investigation safety. Those artifacts are unwritten or outside this frame read. The full plan gate and ELA timing also remain unverified.

## Sources

All links below were accessed live. No paywalled source supports a finding.

- [Official standards, DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): owned expectations, core ideas and boundaries.
- [Grade 1 life science evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf): plant responses and parent-and-young evidence.
- [Elementary evidence statements](https://www.nextgenscience.org/sites/default/files/Elem%20%2B%20Exec%20Summary%20June%202015.pdf): daylight investigation.
- [Appendix F](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf) and [Appendix G](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20G%20-%20Crosscutting%20Concepts%20FINAL%20edited%204.10.13.pdf): practice and crosscutting-concept guidance.
- [K-5 science evidence guide v2.0](https://cozy-dream-721ab6aab0.media.strapiapp.com/Science_20_K_5_20_Evidence_20_Guide_2_0_796df92bd4.pdf): selected coverage, repetition and pacing guidance.
- [OpenSciEd elementary curriculum overview](https://openscied.org/curriculum/elementary-school/explore-the-curriculum/): reference comparison of grade 1 topic organization, not copied content or a pacing mandate.
- [Taking Science to School, chapter 3](https://www.nationalacademies.org/read/11625/chapter/5): background research context on young children’s science learning, read in part.

### For the source list

Add the directly verified life science evidence bundle and current K-5 evidence-guide address above. Record that the curriculum comparison used public overview material, not a complete independent review of its lessons.

## For Cory

- **Money:** Confirm or revise the proposed $40 annual classroom materials ceiling after a quantities-based estimate.
- **People:** Identify the science safety reader and the reader familiar with adoptive, foster and separated families before the relevant completion claims.

**Verdict:** Revise before unit planning. **Finding count:** 6, comprising 2 content findings and 4 stale-note findings. **Report path:** `docs/reviews/frame-science-grade-1-2026-11-14.md`, delivered here only.

