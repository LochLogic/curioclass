# Independent sequence review: World Geography and Ancient Civilizations II

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-world-geography-and-ancient-civilizations-ii-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

Revise before unit writing. The regional order, cross-subject timing and overall day allocations are sound, but several assessment descriptions permit narrower work than their attached standards require, and two content requirements remain insufficiently assigned. Complete the teaching and assessment blueprints within the existing units, then reconcile the shared calendar with the actual sequence.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, the shared adoption criteria and social studies bar, and `docs/courses/social-studies/STANDARD.md`.
- The target scope and sequence, all 160 rows of `days.csv`, and the complete course frame.
- All 29 grade 7 progression rows, relevant incoming and receiving rows, and their reciprocal links.
- The loaded grade 7 anchor standards, C3 indicators, and literacy-standard file.
- `CALENDAR.md`, grade 7 calendar records, and relevant mathematics and ELA frame entries.
- FOUNDATION, relevant ROADMAP sections, BASELINE rules 20 to 24, the glossary, shared approach, source-access notes, base-text record, and sequence briefs.
- Both earlier reviews of this course frame, relevant progression and baseline findings, their repair records, and pertinent earlier sequence findings.
- Outside sources linked below. Memory supplied review-method reminders only; no finding depends on an unverified remembered fact.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: missing Python dependency `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; grade 7 social studies target weeks are 13, 24 and 32, with no reported stagger break. |
| `python -X utf8 scripts/frame.py check world-geography-and-ancient-civilizations-ii` | Zero failures. |
| Targeted `plan.py check world-geography-and-ancient-civilizations-ii` | Zero sequence failures. |
| `python -X utf8 scripts/stale.py check` | Zero failures across 56 files. |

The global gate’s environment failure does not withhold this verdict.

## Findings, most serious first

### 1. Assessment descriptions do not secure the full performances claimed

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, assessment coverage mismatches recur in the earlier progression and sequence reviews.  
**Confidence:** Firm about the written omissions; actual assessment items are not yet available.

Assessment slots and code lists are present. Several descriptions nevertheless direct substantially narrower evidence than the teaching or claimed code requires.

| Assessment | Coverage not secured | Exact repair |
|---|---|---|
| Unit 1, day 10 | Sourcing an object does not explicitly require corroborating sources or inference about its place of origin. Population movement and resulting land-use change are also unspecified. | Supply an unfamiliar object with contextual evidence. Require supported inferences, including origin and audience, plus a short population-to-land-use explanation. |
| Unit 2, day 24 | An edict “sourced” need not be evaluated for usefulness. | Ask separately what the edict can establish about Ashoka’s rule and about subjects’ lives, with a limitation. |
| Unit 3, day 36 | The dynastic cycle and an inscription or saying can leave encouragement of learning, Confucian teachings and Taoism unchecked. | Name these components explicitly, using brief connected prompts. |
| Unit 4, day 50 | One price-source reading can omit several markets, competition, trade barriers, interregional interactions and Buddhism’s arrival in China. | Specify compact economic scenarios and a historical route/source task that together cover those demands. Count suitable retained work from days 44 to 48 where necessary. |
| Unit 5, day 61 | One freely chosen comparison can omit either India or China despite claiming both parent comparison standards. | Count the separate India and China comparisons from days 56 and 57, alongside the unseen transfer task. Include the Japanese development requirement in finding 2. |
| Unit 7, day 85 | Reading a keyed physical map and calculating offsets do not ensure political-map work or the historical longitude, date-line and observatory components. | Add a political-map/text task and a short historical explanation. |
| Unit 9, day 114 | A finished report alone need not show source evaluation, comparison of secondary arguments or the student’s critique of another explanation. Ranking one war’s causes also leaves the wider war standard uncertain. | Assess a named research portfolio and specify causes and consequences across all three required conflicts. |
| Unit 10, day 132 | “The turn to empire” does not explicitly assess tactics, military organization and decentralized administration. | Require an explanation connecting the taught military example and provincial administration to expansion or longevity. |
| Unit 11, day 143 | Only inflation is named, although day 138 teaches inflation, deflation and unemployment separately. | Assess effects on contrasting groups for all three, and identify the trade-policy benefits and costs being assessed. |
| Unit 12, day 155 | A multi-cause argument can discuss causes without explaining effects. | Require consequences as well as causes in the argument or an accompanying short response. |

**Why it matters:** A unit writer could follow these descriptions faithfully while leaving required learning unchecked.

**Exact course-wide fix:** Turn the assessment summaries into brief coverage blueprints. Identify each required performance and its on-demand task or retained individual evidence. Preserve the unseen-source task, the existing assessment day and the single respond day; flag any blueprint that cannot fit instead of silently dropping components.

This follows the repository’s full-coverage requirement. The external assessment criteria likewise emphasize demonstrated content and disciplinary skill, rather than code attachment alone. [Social studies materials criteria, criterion 6](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf)

### 2. Two content requirements are not sufficiently assigned to teaching days

**Severity:** Serious  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, required components disappearing inside broad descriptions recur in the earlier frame reads.  
**Confidence:** Firm on the requirements; likely on the resulting omissions.

| Location | Problem | Exact fix |
|---|---|---|
| Unit 5, days 52 to 54, `MA.7.T2c.1` | Arrival and spread are assigned, but development of Buddhism within Japan through the thirteenth century is not explicit. Day 53 instead lists Shinto shrines, court life and literature. | Make day 53 explicitly teach change in Japanese Buddhism across the required period. Connect the cultural evidence on days 53 and 54 to that development. Retain the literary examples selectively. |
| Unit 6, days 72 to 74, `MA.7.T3b.1` | Ancient archaeological evidence is attached to Australia’s very deep past. The Māori day names voyaging and present-day iwi, without assigning an archaeological inference about early Māori culture. | Name an appropriate Māori archaeological example and the inference students make from it, alongside Māori social organization and living communities. |

These are distinct components in the [official grade 7 requirements, printed pages 98 to 99](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=98).

**Why it matters:** Naming the region, period or people does not ensure that the missing historical work occurs.

**Day-cost repair:** Keep unit 5’s three East Asian days, with more explicit purposes. In unit 6, finish the two-place comparison on day 70 and use days 71 to 74 for the Australian and Māori social and evidence work. This changes the balance from five geography days and three peoples days to four and four, preserving the synthesis, assessment and response.

### 3. Unit 8 claims a comparison indicator while teaching one procedure

**Severity:** Serious  
**LAYER:** sequence, frame, progression  
**REPEAT:** yes, activity-to-indicator mismatches recur in the progression reviews; this particular mismatch remains newly identified.  
**Confidence:** Firm.

Days 92 to 94 run one deliberation and action cycle. The progression explicitly says grade 7 uses one procedure and grade 8 compares procedures. However, `D2.Civ.9.6-8` requires comparison across groups and settings. [C3 Framework, printed page 33](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=33)

**Why it matters:** Successful participation in one procedure cannot establish the claimed comparison performance. Day 99 attaches the indicator without naming comparative evidence.

**Exact fix:** Within day 92, compare the classroom’s proposed procedure with the taught Athenian assembly and one supplied present-day decision procedure. Students identify differences in participation, speaking and decision rules before choosing their classroom rules. Retain an individual comparison for the unit assessment.

Keep grade 8’s advance as a broader comparison and evaluation of which procedures suit different questions.

This disagrees with the earlier repair’s acceptance of one procedure as sufficient for the grade 7 claim. The distinction rests on the publisher’s wording, not memory.

### 4. The new research moves begin as applications without named teaching

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, missing models before new writing demands recur in earlier frame and sequence reads.  
**Confidence:** Likely.

The frame calls comparison of secondary arguments and critique of explanations new learning. Day 107 immediately asks students to compare arguments; day 110 immediately asks them to critique a classmate’s explanation. Neither names a model or guided attempt.

Earlier research experience and ELA preparation are useful prerequisites, but they do not establish these particular performances.

**Why it matters:** Writers may build independent tasks before showing students how to distinguish an argument from a topic or evaluate explanatory structure.

**Exact fix:**

- Begin day 107 with a short model comparing two historical arguments, then a guided comparison before students use their own pair.
- Begin day 110 with a model critique of an explanation’s organization, then peer critique.
- Retain each student’s comparison and critique in the assessed portfolio.
- Keep all eight research days.

Explicit teaching followed by supported practice is consistent with the [secondary writing practice guide, recommendation 1](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_secondary_writing_110116.pdf). That source supports the teaching approach, not an exact minimum number of minutes.

### 5. The three war days distribute their load poorly

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, uneven local workloads were identified in the earlier grade 4 sequence read.  
**Confidence:** Judgment call.

Unit 9 reserves:

- One day for Persian background already encountered in grade 6.
- One day for both the Persian and Peloponnesian Wars, including causes, results and Thucydides.
- One day for Alexander plus a causal ranking.

The problem is the distribution within the three days, rather than the eight research days that follow.

**Why it matters:** Day 102 is likely to become compressed narration, leaving little room for the causal reasoning the course owns.

**Exact fix:**

| Day | Revised purpose |
|---|---|
| 101 | Brief Persian retrieval, followed by the Persian Wars’ causes and consequences. |
| 102 | Peloponnesian War causes and consequences, with Thucydides compared against another account. |
| 103 | Alexander’s conquests and consequences, followed by a compact causal ranking. |

Keep mythology on day 104 and research on days 105 to 112. No unit resizing is warranted.

### 6. The required shorter path is absent

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, explicitly identified in earlier sequence reviews.  
**Confidence:** Firm on the omission.

The course specifies 160 meetings of 50 minutes, totaling 8,000 minutes. It provides no shorter route, although FOUNDATION section 5 and adoption criterion C2 require one where less time is available.

**Why it matters:** Teachers must improvise reductions, potentially removing source analysis or response time.

**Exact fix:** Add a shorter-route table identifying the time budget, essential tasks, shorter source selections, and reductions to repeated drafting or sharing. Preserve required content, models, individual evidence, assessments and response. Have subsequent unit plans budget that route explicitly.

The minimum timetable or additional audience this route should serve belongs to Cory.

### 7. The shared calendar does not represent the held action day

**Severity:** Minor  
**LAYER:** process, sequence  
**REPEAT:** yes, the earlier kindergarten sequence read found the same generator limitation.  
**Confidence:** Firm.

| Placement | Shared calendar | Actual sequence |
|---|---|---|
| Unit 8 | Days 87 to 101 | Days 87 to 100, plus day 120 |
| Unit 9 | Days 102 to 116 | Days 101 to 115 |
| Check 2 | Days 117 to 118 | Days 116 to 117 |
| Check 2 response | Days 119 to 120 | Days 118 to 119 |

The writer identifies this correctly, but “fix if the calendar should match” leaves an authoritative planning record unresolved.

**Why it matters:** Other writers coordinating through `calendar.csv` receive incorrect dates.

**Exact fix:** Make calendar generation consume existing daily sequences and emit separate segments for interrupted units. Regenerate the shared calendar. Preserve the current action look-back and check weeks; annotating only the frame would leave the machine-readable discrepancy.

### 8. Current guidance still contains superseded status statements

**Severity:** Minor  
**LAYER:** process, progression, standard  
**REPEAT:** yes, stale status statements were findings in the earlier frame reads.  
**Confidence:** Firm.

The stale gate passes, but these statements remain:

| File or row | Stale statement | Exact replacement |
|---|---|---|
| `ss7-buddhism-empires` progression notes | The standards paraphrase “omits two parts.” | Remove that parenthesis. The current anchor includes missionaries and Gupta literature and art. |
| `STANDARD.md`, section 1 | Literacy standards are not loaded and their loading is open. | State that RH, RST and WHST were loaded on 2026-11-14 in `data/standards/ccss-literacy-6-12.txt`; distinguish loading from course placement. |
| Adoption bar’s social studies standards paragraph | Its literacy-loading status remains open. | Point to the loaded file and current placement record. |

**Why it matters:** Later writers are instructed to compensate for a repaired omission or repeat completed preparation.

These are current-status corrections. Historical reports can retain their dated observations.

## Order, coverage and days by load

The main prerequisite order is sound: geography precedes regional history; India and China precede Silk Road synthesis; early source work precedes research; Roman institutions and economics precede the concluding argument.

All five Greek democracy subparts have explicit teaching placements on days 89 to 91. The five Greek accomplishment options appear on days 105 and 112. Each student researching one option is appropriate; requiring every student to research all five would misread the standard.

| Unit | Total days | Teaching days | Load judgment |
|---|---:|---:|---|
| 1 | 11 | 9 | Reasonable geography and archaeological inquiry balance. |
| 2 | 14 | 12 | Reasonable; preserve edict evaluation and achievements. |
| 3 | 12 | 10 | Reasonable; make full assessment coverage explicit. |
| 4 | 14 | 12 | Dense but defensible, with four economics days. |
| 5 | 11 | 9 | Three East Asian days and six comparison days; sharpen the Japanese development assignment. |
| 6 | 11 | 9 | Five geography days versus three peoples days; rebalance within the unit as finding 2 specifies. |
| 7 | 9 | 7 | Tight but plausible; protect historical explanation alongside calculation. |
| 8 | 15 | 13 | Four action days leave nine historical teaching days; comparison must fit within the action work. |
| 9 | 15 | 13 | Three wars/background days, one mythology day, eight research days and one synthesis day; redistribute the first three. |
| 10 | 13 | 11 | Reasonable. |
| 11 | 11 | 9 | Five economics days and four engineering/language days are defensible. |
| 12 | 12 | 10 | Appropriate emphasis on argument and synthesis. |

No unit exceeds 25 days, so no mid-unit assessment is required. Assessment and response time is counted once. Day 121 places the named branches-of-government readiness check at its first use; retaining that conservative check is acceptable. Recent grade 6 learning is generally retrieved within teaching days.

## Calendar and same-year leans

The actual check dates are 63 to 64, 116 to 117 and 157 to 158, in weeks 13, 24 and 32. Neither mid-year check overlaps another subject’s check day.

| Lean | Availability and judgment |
|---|---|
| Signed arithmetic for day 84 | Mathematics unit 5 spans days 69 to 91; its frame places addition and subtraction around 69 to 77. The local clock/number-line bridge remains appropriate. |
| Percent for unit 11 | Mathematics unit 4 ends on day 68, well before day 134. Met. |
| Research and credibility | ELA unit 3, days 61 to 86, precedes research beginning on day 105. Met. |
| Athens | ELA unit 4 overlaps social studies unit 8. Both frames supply their own necessary context. Met. |
| Mythological allusions | Social studies day 104 precedes ELA’s later unit 5 allusion work. Met. |
| Latin roots | ELA unit 3 precedes days 141 to 142. Met. |
| Argument and counterclaim | ELA unit 4 precedes unit 12. Met. |

These conclusions use the available calendar and frame resolution. Exact lesson-level availability remains subject to the other courses’ eventual daily sequences.

## Candidate cells and source map

Both content candidates are settled:

- Homer’s epics: retained within day 104, with no added day.
- Han China and Rome comparison: retained within day 153, with no added day.

The Persian opener is placed content rather than an unresolved candidate. Finding 5 retains it while shortening retrieval.

No whole-course base text is adopted, and no particular partial-base lessons are mapped. Exhaustive base-lesson placement and source-order checking are therefore not applicable now. Selecting an actual partial base later must trigger its mapping and item-level rights checks.

## Lens checklist for the scope and sequence layer

| Checklist line | Status |
|---|---|
| Questions require the unit’s historical or geographical evidence and permit supported conclusions | **Met provisionally.** Questions connect to the planned content; actual source sufficiency awaits unit plans. |
| History follows time order, or gives a reason | **Met.** Regional restarts follow the anchor; Japan’s extended period and modern time zones are explained. |
| Contested events carry more than one telling | **Met in design.** Indo-Aryan arrival and Rome’s transformation are treated as evidential questions. Preserve multiple accounts in the war work. |
| Writing from sources recurs and builds from short to long | **Met**, with the missing explicit research models in finding 4. |

## What is right and should remain

Retain the regional order, parallel timelines, comparison without ranking peoples, recurring sourced claims, eight research days, and the counterclaim handoff to grade 8.

Preserve present-day Indigenous communities, community-authored materials, privacy protections, and prohibitions on harmful role play. The current FOUNDATION decision governs sensitivity review; the earlier requests for outside community reviewers are superseded and should not be reopened.

## Settled by the expert

Recommendations for the caller to apply; none was edited here.

| Choice | Reason | Files touched |
|---|---|---|
| Assess named retained work alongside unseen transfer tasks | Secures breadth without expanding every examination | Days CSV; scope and sequence; later unit plans |
| Complete Japanese Buddhist development within days 52 to 54 | Restores the existing owned requirement | Days CSV; frame and progression wording |
| Use four geography and four peoples days in unit 6 | Makes room for Māori social and archaeological work | Days CSV; scope and sequence |
| Add procedural comparison before unit 8’s deliberation | Supports the claimed C3 performance | Days CSV; frame; progression |
| Model argument comparison and explanation critique | Teaches the new moves before independent use | Days 107 and 110 |
| Redistribute the three Greek-war days | Protects analysis without changing unit length | Days 101 to 103 |
| Retain day 121’s readiness check | It is a conservative check at first use, already budgeted | Existing sequence retained |
| Preserve the held action day and synchronize the calendar | Corrects the record without undoing the action cycle | Calendar generator and generated records |
| Bound the 33 CE example to its evidence | The opened account describes credit contraction, land sales and falling land prices; it does not alone establish general price deflation or unemployment | Unit 11 source notes and eventual lesson |

For day 138, use a clearly labelled illustrative general-deflation case if broader price evidence is unavailable. [Tacitus, *Annals* 6.16 to 6.17](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Tacitus/Annals/6A%2A.html)

## What I could not judge

- Actual assessment coverage, scoring and duration before items and retained-evidence requirements exist.
- Reading accessibility, final source balance and individual rights lines.
- Classroom feasibility of the dense days.
- A full unit-by-unit comparison with all three check states. The attempted New York framework fetch timed out.
- The absent subject-specific approach page, already acknowledged in the governing documents.

## Sources and reading limits

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): targeted grade 7 content requirements.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): targeted owned-indicator wording.
- [Social studies materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): all three pages, especially sequence, source use and assessment.
- [Secondary writing practice guide](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_secondary_writing_110116.pdf): recommendations overview and explicit strategy-teaching guidance.
- [Investigating History grade 7 overview](https://www.doe.mass.edu/investigatinghistory/curriculum/g7-course-guidebook.pdf): prerequisite, pacing and assessment sections. Its allocations are comparisons, not required minima.
- [Primary history curriculum sequence](https://www.thenational.academy/teachers/programmes/history-primary/units): candidate-unit structure and younger intended level.
- [Ancient Greece and Rome curriculum overview](https://www.coreknowledge.org/free-resource/ckhg-unit-2-ancient-greece-rome/): overview only, not its complete lessons.
- [California standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): targeted Homer, Persia and classical-world comparisons.
- [Tacitus, *Annals* 6](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Tacitus/Annals/6A%2A.html): the bounded 33 CE evidence described above.

**For the source list:** Add the Tacitus passage and its evidential limits if absent. Record the New York access failure; do not treat this read as its completed comparison.

## For Cory

- **Audience and time:** Set the minimum timetable the shorter route should support: shorter daily periods, fewer meetings, or both. No reduction in required standards is proposed.

**Verdict:** Revise before unit writing. **Finding count:** 8. **Report path:** `docs/reviews/sequence-world-geography-and-ancient-civilizations-ii-2026-11-14.md`, delivered here only.

