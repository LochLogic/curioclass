# Second-model frame read: computer-science-grade-8

2026-11-25. Read-only report supplied inline. No files were created, edited or deleted.

## Verdict

**Needs fixes before scope and sequence writing.** The five-unit structure, progression placement and calendar are sound, but the frame assumes the previous elective was taken and leaves several required data actions insufficiently specified. Add the entry bridges, complete those teaching and assessment promises, and correct the source map while preserving the five units and 64-day budget.

**Findings: 8, most serious first.**

## What I read

- The complete grade 8 frame, adjacent grade 7 and grade 9 frames, and the grade 10 network handoff.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the computer science lens, subject STANDARD and APPROACH.
- FOUNDATION, relevant BASELINE and production-path rules, shared APPROACH, GLOSSARY, adoption bars, source guidance and subject decisions.
- The `grade:8` selector in `course-list.csv`, all 18 selected progression rows, adjacent-grade rows, reciprocal links, `frames.csv` and calendar rows.
- The grade 8 mathematics and ELA Units tables.
- Relevant computer science pre-work, progression and earlier frame reviews, particularly the combined grades 6 to 12 review and grade 7 second-model read.
- All 13 owned statements and their boundaries in the published CSTA PDF, plus the outside sources linked below.

No substantive finding rests on memory.

## Checks and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check computer-science-grade-8` | Passed: 0 failures; note that Seams omits `g10-network-of-networks` |
| `python -X utf8 scripts/plan.py check computer-science-grade-8` | Failed because lesson-stage CSVs are absent; frame review continued |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent placement check | All 18 selected skills placed exactly once; all 13 owned standards placed |
| Independent link and model check | All progression links reciprocal; all 16 input/output models represented |
| Calendar comparison | All nine stored course-calendar ranges match the frame |

The plan check was course-filtered under AGENTS.md. The consolidated gate was not run because it writes output and baseline files.

| Component | Course days | School days | Weeks |
|---|---:|---:|---:|
| Unit 1 | 1 to 13 | 3 to 33 | 1 to 7 |
| Unit 2 | 14 to 28 | 35 to 70 | 7 to 14 |
| Mid-year check and response | 29 to 30 | 73 to 75 | 15 |
| Unit 3 | 31 to 42 | 78 to 105 | 16 to 21 |
| Unit 4 | 43 to 54 | 108 to 135 | 22 to 27 |
| Unit 5 | 55 to 62 | 138 to 155 | 28 to 31 |
| Year-end check and response | 63 to 64 | 158 to 160 | 32 |

The mid-year check avoids core check school days. Its respond day may coincide with science’s check because the middle school rule staggers checks, not responses. The year-end overlap is permitted during finals week.

The unit allocation is **13 + 15 + 12 + 12 + 8 = 60**, plus four course-level check and respond days. The distribution reasonably reflects the programming project, systems design, data investigation and shorter society unit.

All four named cross-subject leans have credible timing or an explicit bridge. This is a single-grade course, so the band-course Year column does not apply.

## Findings

### 1. Students who skipped the previous elective have no entry bridge

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, S1  
**Confidence:** Firm

**Location:** Days; Seams, opening paragraph and Picked up table, lines 165 to 195.

The course is an elective, but every prerequisite is treated as year-before retrieval. The only exception addresses omission of grade 7 unit 4, and even that exception covers `g8-ml-evaluate` and `g8-modify-for-bias` while omitting `g8-ai-tool-day`, which also assumes a row from that unit.

A student without grade 7 computer science can encounter lists, procedures, code analysis and testing without instruction. This violates frame-write rule 32’s requirement to bridge optional-course prerequisites.

**Exact fix:** Add a **Course order** bullet distinguishing returning students’ retrieval from readiness evidence and worked bridges for students missing earlier instruction.

| Upcoming unit | Ten-minute readiness slot | Bridge content to name |
|---|---|---|
| 1 | Last ten minutes of day 1, after the hook | Network paths, CIA triangle, requirements and access needs |
| 2 | Last ten minutes of day 13 | Variable types, procedures, lists, tracing and test-tables |
| 3 | Last ten minutes of day 30 | Table operations and chart choices |
| 4 | Last ten minutes of day 42 | Training versus test data, algorithmic harm and choosing an approach |
| 5 | Last ten minutes of day 54 | Technology suitability, historical effects and automation |

Use the prerequisite rows already listed in Seams. State which supplied example teaches each flagged gap before students apply it, with time inside the existing Understanding lessons.

Extend the omitted-grade-7-unit-4 provision to **all three affected rows**, including `g8-ai-tool-day`. Remove “never as a readiness check” as an unconditional rule.

### 2. Unit 3 does not explicitly place every required data action

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete boundary coverage recurs in earlier computer science reads; these omissions are new  
**Confidence:** Firm

**Location:** Unit 3, line 253; Evidence, lines 85 to 97.

The current plan names predictions, a six-part summary and stage decisions, but leaves three requirements unstated:

- DI-25: judging whether a prediction is sensible for unfamiliar inputs.
- DI-27: explaining the investigation’s motivation, key decisions and whether its results were expected or satisfactory.
- IM-29: connecting stage choices to both misleading conclusions and impaired model outcomes.

These are present in the [published boundaries, PDF pages 74, 75 and 78](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=74). Day 40 currently permits a chart **or** model outcome, leaving the writer free to omit one consequence.

**Exact fix:**

- Day 32: add one prediction for an unfamiliar input and require a reason to trust, qualify or reject it. Connect this relationship-based prediction to the classifier work that follows.
- Day 36: add motivation, collection or construction method, key decisions, and expected versus satisfactory results to the model summary and checklist.
- Days 37 and 38: require those fields in the student’s draft, feedback and revised summary.
- Day 39: explicitly include presentation choices among the stages that can distort results.
- Day 40: use one small supplied example showing the consequences in both a chart and a model-results table.
- Day 41: include prediction justification and both downstream consequences among the look-fors; score the expanded summary checklist with the revised product.

These additions clarify the existing owned standards without moving ownership or adding a unit.

### 3. The course checks need bounded task loads

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, S3  
**Confidence:** Likely

**Location:** Course-level checks, lines 261 and 262.

Each check receives about 35 minutes. The mid-year sitting combines a fifteen-line program traced for two inputs, three credit cases, a usability response and two systems tasks. The year-end sitting combines a design analysis, a sourced argument, a history response and four earlier-unit items.

Without limits, the eventual writer can satisfy every listed demand while producing an impractical sitting.

**Exact fix:** Keep the existing calendar and bound the checks as follows.

| Check | Task budget |
|---|---|
| Mid-year | Trace of at most ten lines: 10 minutes; two credit cases and one credit line: 8; usability response: 7; attack/prevention item: 5; access item: 5 |
| Year-end | Emerging-design case: 10 minutes; short sourced argument and rebuttal: 15; scatter prediction and model-limit items: 10 |

Carry day 57’s history record unscored instead of adding a new history performance. Carry unit 3’s stage-bias and unit 4’s generated-code records unscored instead of adding those two sampling items.

These are planning limits, not measured completion times. Check them against the actual items later.

I differ from the combined review’s proposed blanket two-lesson rule: the current calendar can remain if these particular sittings are bounded.

### 4. The cybersecurity source map excludes the defenses lesson for the wrong reason

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, source-content mismatches recur in the grade 6 and grade 7 second-model reads  
**Confidence:** Firm

**Location:** Base text; For the lead item 2; Source map cybersecurity row, line 323.

The frame groups lessons 3 and 5 as titles suggesting attacks run from a machine. The public description of [lesson 5](https://www.raspberrypi.org/curriculum/archived/key-stage-3/cybersecurity/there-s-no-place-like-127-0-0-1) instead teaches network threats and defenses.

[Lesson 6](https://www.raspberrypi.org/curriculum/archived/key-stage-3/cybersecurity/under-attack), mapped as protection teaching, is a concluding defense game followed by assessment. The public descriptions already resolve this distinction.

**Exact fix:**

- Map selected conceptual defenses from lesson 5 to day 5’s protection plan.
- Mark lesson 6 left out: its consolidation game and assessment are replaced by Curio Class’s protection task and unseen assessment.
- Describe lesson 3’s exclusion accurately: its account-hacking scenario and English legal content are outside this adaptation. Retain any needed threat descriptions through Curio Class’s own toy cases.
- Describe lesson 4 as selected malware content, explicitly excluding its independent web research and bot-influence activity.
- Update the matching unit description and lead note. Keep the pending per-file rights check.

Also coordinate with grade 7 finding 5: if its recommended exclusion of the sequences unit’s lesson 3 is applied, replace grade 8’s claim that grade 7 adapts lessons “2 to 4” with the actual retained lessons and a separate exclusion reason for lesson 3.

### 5. The outgoing network seam omits its grade 10 destination

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, M6  
**Confidence:** Firm

**Location:** Handed on table, line 201.

`g8-network-failure.hands_on` includes both `g9-network-sketch` and `g10-network-of-networks`. The frame lists only the grade 9 destination. The structural checker identifies this omission.

**Exact fix:** Add:

| This course hands on | Unit here | Row that picks it up | What it does with it |
|---|---|---|---|
| g8-network-failure: packet paths, failures and backup links | 1 | g10-network-of-networks, grade 10 unit 3 | Join small networks, trace packets through routers and compare the internet with a local network |

Clarify the closing paragraph: grade 9 pickups are year-before retrieval; grade 10 and grade 11 destinations determine readiness from their actual intervening use.

### 6. Resolved row changes remain described as pending

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, combined grades 6 to 12 review, M4  
**Confidence:** Firm

**Location:** Seams, lines 169, 182 and 193 to 195; For the lead item 6, lines 308 and 309.

The progression already contains the reciprocal code-review link and the revised disability wording. The frame still calls the link a proposal and points to row changes in a separate final message. That message is not a durable part of the frame.

The grade 7 frame also does not specify grade 8’s day 42 timing, despite the attribution.

**Exact fix:**

- Replace the parenthesis in line 182 with simply **`g8-text-project`**.
- Replace lines 193 to 194’s exception with: **“Every incoming handoff above is reciprocal in data/progressions/computer-science.csv.”**
- Delete For the lead item 6 because the named changes are already present.
- Delete “as the grade 7 frame says” from the day 42 provision. Keep day 42 as this frame’s explicit timing, expanded under finding 1.

Do not rewrite the dated earlier reports.

### 7. The outside-standard share uses course days instead of teaching days

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review, S2  
**Confidence:** Firm

**Location:** Standard, lines 49 to 51; For the lead item 4.

The frame divides approximately four list-work days by all 64 course days. C1 specifies teaching days.

The present allocation has five assessment days and five respond days, leaving **54 teaching days**. Four of 54 is approximately **7.4 percent**, still below the limit.

**Exact fix:** Replace both calculations with:

> Approximately four lesson equivalents of list work out of 54 teaching days, about 7.4 percent. The scope and sequence confirms this allocation and counts any other outside-standard teaching within the same limit.

The earlier combined report’s proposed denominator of 56 does not match the current five check and five respond allocations.

### 8. The header retains UK spelling

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, combined grades 6 to 12 review  
**Confidence:** Firm

**Location:** Opening course line, line 3.

**Exact fix:** Change **“catalogue id”** to **“catalog id”**, following AGENTS.md.

## Lens checklist: course-frame layer

| Lens requirement | Result |
|---|---|
| All five concepts receive substantive teaching | Met |
| Programming does not dominate the year | Met: 15 of 60 unit days |
| Constructs and models precede application | Met for returning students; entry treatment needs finding 1 |
| Text-code transition is supported | Met through the preceding grades’ bridge; missing-course fallback needs finding 1 |
| Read, predict and modify before independent creation | Met in unit 2 |
| Unplugged work in every unit | Met |
| Notional machine and systematic debugging | Met through traces, test-tables, one-change retesting and logs |
| Collaboration, design and ethics inside content | Met |
| Society uses evidence and multiple views | Met as a frame requirement; source packets remain to be checked |
| AI connected to data and algorithms | Met: unit 3 prepares unit 4, and unit 4 returns to the programming project |
| Owned standards at their boundary depth | Part met: finding 2 |
| Unsupported Specialty or S2 claims | Not applicable: none claimed |
| Purposeful tools, privacy and paper paths | Met under the current subject rules |
| Projects and code included in assessment | Met; check workload needs finding 3 |
| Support for a non-specialist teacher | Required by the inherited APPROACH; finished explanations cannot yet be judged |
| Unsupported general benefits of coding claimed | Met: none found |

## What is right and should remain

- All 18 progression rows are placed once, with ownership distinguished from reuse.
- Unit order supports the programming project, data investigation and later classifier work.
- The math and ELA leans have credible calendar placements and fallbacks.
- Projects include draft, feedback, revision and later scoring.
- Privacy, toy security systems and disability test conditions are carefully specified.
- Device-dependent data attainment is honestly marked partial on the paper path.
- Source-package and third-party checks are explicitly pending.

## Settled by the expert

| Choice | Reason | File for the fixer |
|---|---|---|
| Keep five units and 64 course days | Counts and broad allocation are defensible | Grade 8 frame |
| Keep current check dates with bounded tasks | Calendar is valid; item load can be reduced | Grade 8 frame |
| Expand existing data tasks rather than add a unit | Missing actions fit the current investigation | Grade 8 frame |
| Use cybersecurity lesson 5 for conceptual defenses | Public lesson description identifies its actual content | Grade 8 frame |
| Retain day 42 as the pre-unit-4 readiness slot | It precedes the unit and preserves its opening hook | Grade 8 frame |
| Use 54 teaching days provisionally for C1 | Matches the current assessment and response allocation | Grade 8 frame |

## For Cory

- **Scope and attainment rule:** The published PS-05 boundary permits students prohibited from using generative AI to validate teacher-generated output. The current subject rule marks the standard partial whenever a school lacks a live approved tool. Recommend allowing suitably documented, teacher-generated saved outputs to demonstrate full attainment through student validation, while preserving the prohibition on student live-tool use. This changes a settled subject rule, so the fixer must not apply it without Cory’s decision. See [CSTA, PDF page 43](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=43).

No spending, audience or outside-person decision is needed for the eight frame repairs.

## What I could not judge

- Actual assessment duration, scoring reliability, tool behavior and finished teacher explanations.
- Complete archived lesson packages, their individual licenses and third-party exceptions. Public descriptions were readable; package downloads require login.
- Complete factual accuracy and balance of the future society packets.

Two requested source pages refused automated reads:

| Source | Status | Alternative checked |
|---|---|---|
| [CISA, Recognize and Report Phishing](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) | **browser check**, 403 | FTC phishing guidance opened successfully |
| [ASPE, National Survey Trends in Telehealth Use in 2021](https://aspe.hhs.gov/reports/hps-analysis-telehealth-use-2021) | **browser check**, 403 | The updated ASPE report also returned 403 |

Neither blocked page was fetched another way. Search results do not constitute verification of the telehealth case.

## Sources

- [2026 CSTA standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): owned statements and boundaries, including the saved-output exception.
- [PRIMM pedagogy summary](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf): support for reading supplied programs before modifying and creating.
- [Archived key stage 3 curriculum](https://www.raspberrypi.org/curriculum/archived/key-stage-3): source-unit inventory and sequencing.
- [Cybersecurity unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/cybersecurity), with individual lessons linked in finding 4: source-map verification.
- [Sequences unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data) and [Warm up](https://www.raspberrypi.org/curriculum/archived/key-stage-3/python-programming-with-sequences-of-data/warm-up): introductory list content and lesson inventory.
- [Data science unit](https://www.raspberrypi.org/curriculum/archived/key-stage-3/data-science) and [Make a change](https://www.raspberrypi.org/curriculum/archived/key-stage-3/data-science/make-a-change): investigation and reporting placement.
- [FTC phishing guidance](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams): accessible alternative for prevention background.
- [FTC Fair Credit Reporting Act page](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act): inspected the proposed legal source route; it does not alone establish the complete pre-1970 historical narrative.
- [2024 United States Data Center Energy Usage Report](https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report): confirmed publication and scope; future packet claims still need checking.

## For the source list

Add the individual cybersecurity lesson URLs and their content distinctions to `APPROACH-SOURCES.md`. Record the CISA and ASPE access failures as **browser check**, alongside the accessible FTC alternative.