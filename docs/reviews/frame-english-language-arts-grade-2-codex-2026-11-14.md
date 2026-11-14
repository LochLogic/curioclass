# Independent expert read: Grade 2 English Language Arts course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-english-language-arts-grade-2-2026-11-14.md`  
**Delivery:** Complete report supplied here. No report file or other file was written.

## Verdict

The frame has a coherent four-unit structure, complete skill placement and a plausible annual time budget, but needs revision before detailed planning. Its largest risk is that the foundations descriptions and ownership claims do not match when the base text actually introduces and completes the patterns. Correct that mapping, restore the full reading and recording requirements, and make the replacement anchor texts reviewable.

**Finding count: 12, comprising seven curriculum findings and five stale-note findings.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, glossary, relevant BASELINE rules, requested ROADMAP sections, approach pages and relevant source-list entries.
- The complete Grade 2 frame, its `frames.csv` row, all 30 Grade 2 ELA progression rows, their prerequisites and handoffs, and the Grade 1 and Grade 3 ELA frames.
- The complete local Grade 2 ELA standards, with live checks against the published standards.
- The Grade 2 science and social studies frames and the seven cross-subject references actually recorded in the ELA progression.
- ELA progression reviews, reconciliation, stitch and fixes; relevant cross-subject reviews; earlier course-frame reviews for repeat classifications.
- The base-text policy and source-store notes; the Grade 2 curriculum map, foundations standards coverage, foundations module 2 and 3 overviews, and lesson inventories in the topic and foundations archives.
- Outside sources listed below, including the published K to 2 review criteria.

The requested `data/plans/english-language-arts-grade-2/source-map.csv` does not exist. **This is not a finding:** `frame-write.md` explicitly defers that day-level CSV to the scope and sequence. The frame’s source-map table is the applicable artifact here.

### Checks

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check`, attempted first | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Targeted Grade 2 plan check | Zero failures, but zero assessment items checked |
| Direct frame checks for ELA grades 1, 2 and 3 | Zero failures |
| ELA progression check | 374 rows, zero failures |
| Independent Grade 2 placement check | 30 owned skills, each placed once; no missing, duplicate or foreign skills |
| `python -X utf8 scripts/stale.py check` | Final run: 56 files, zero failures |

The full plan gate remains unverified. The substantive review below is advisory, not a gate-cleared acceptance. No dependency was installed and no defect-ledger entry was written.

No curriculum finding rests solely on model memory. Prior workspace memory was used only for report conventions; current files and opened sources supply the evidence.

## Findings, most serious first

### 1. Foundations ownership and descriptions contradict the retained source sequence

**Location:** Frame lines 11, 125 to 128 and Source map  
**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, source-order discrepancies recur in `progression-ela-codex-2026-11-13.md`, F1  
**Confidence:** firm

**What is wrong.** Unit 1 claims additional vowel teams within cycles 1 to 5. Those cycles review Grade 1 teams. Additional teams begin in cycle 7, continue in cycle 11 and include `aw` and `au` in cycle 19.

Unit 4 is described as review, although cycles 20 to 26 introduce further spelling changes, schwa patterns, prefixes and endings. Meanwhile, the frame says an owning unit teaches and checks its row to the Grade 2 standard. That cannot describe completion of `e2-vowel-teams` in unit 1 or all the named affix and inconsistent-pattern work in unit 2.

The source map also assigns cycles 13 to 19 collectively to “2 and 3”, without identifying the boundary. The [2017 foundations sequence](https://files.eleducation.org/web/resources/Section-5_SkillsBlock-Year-at-a-Glance_Grade2_071417.pdf), PDF page 2, establishes the order.

**Why it matters.** Writers could assess untaught patterns, omit late-year instruction or write decodables against the wrong inventory.

**Exact fix.**

- Describe unit 1 as review of known vowel teams plus spelling generalizations.
- Describe units 2 and 3 as introducing their actual additional teams and patterns.
- Describe unit 4 as new instruction followed by cumulative review.
- Replace the ambiguous foundations mapping with cycles 1 to 5 in unit 1, 6 to 12 in unit 2, 13 to 19 in unit 3, and 20 to 26 in unit 4.
- Add explicit completion points for each continuing foundations row and restrict each assessment to patterns already taught.

If ownership continues to mean completion, propose `e2-vowel-teams` ownership in unit 3 and completion ownership for the continuing affix and inconsistent-pattern rows in unit 4. Those unit moves require Cory’s decision. Do not silently accelerate the source sequence to preserve the existing cells.

### 2. The planned speaking task does not complete its assigned recording requirement

**Location:** Writing calendar, Paper path and devices, unit 3 and `e2-tell-and-record`  
**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, `progression-ela-codex-2026-11-13.md`, F3, identified incomplete recording alternatives  
**Confidence:** firm

**What is wrong.** Unit 3 records a researched informational presentation about a pollinator. SL.2.5 specifically requires recordings of stories or poems. An informational report does not establish that performance. The frame also permits a live presentation without carrying forward the progression row’s explicit unfinished-recording boundary.

The same routine uses formal English for recording and informal English in pair talk, but does not explicitly require students to **compare** those uses for L.2.3a. See the [speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/2/) and [language standards](https://www.thecorestandards.org/ELA-Literacy/L/2/).

**Why it matters.** A teacher can complete every named product while leaving claimed requirements undemonstrated.

**Exact fix.**

Within unit 3:

- Retain the researched pollinator presentation.
- Record the existing bee story or a unit poem, individually or through a small-group contribution.
- Add a drawing where it clarifies the story or recounted experience.
- Have students compare two versions of a short utterance, explaining how its informal and formal wording differ.
- State: “A live presentation supports the speaking goals but leaves SL.2.5 unfinished until the child contributes to a story or poem recording.”

Keep recordings local and retain the privacy alternatives.

### 3. The reading endpoint narrows the Grade 2 standard to the band’s low end

**Location:** Texts and the reading level; end-of-year course check; outgoing seam  
**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, reading-range and support boundaries recur in the ELA progression reviews  
**Confidence:** firm

**What is wrong.** The frame sets independent reading at the low end of the grades 2 to 3 band and checks only that endpoint. RL.2.10 and RI.2.10 require proficient comprehension within the band, with scaffolding available at its high end. The current progression row already preserves that distinction. See the published [literature](https://www.thecorestandards.org/ELA-Literacy/RL/2/) and [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/2/) standards.

**Why it matters.** A writer could avoid supported encounters with harder band texts and hand Grade 3 a narrower reading experience than its frame assumes.

**Exact rewritten rule:**

> By year end, students read and comprehend literary and informational texts within the grades 2 to 3 band proficiently, with scaffolding as needed at its high end. Records distinguish independent performance from supported performance.

Retain an independent cold reading sample. Add supported comprehension evidence from harder band texts across units 3 and 4, and carry both kinds of evidence into the handoff.

### 4. Unit 3 leaves the base text’s written research product unaccounted for

**Location:** Unit 3, writing calendar and Source map  
**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, incomplete required performances recur in earlier progression and frame reads  
**Confidence:** likely

**What is wrong.** The source map retains every module 3 lesson, but the unit description and candidate assessment name research notes and a recorded presentation without explicitly retaining the informational paragraph and illustrated presentation product those lessons develop.

The base assessment sequence includes planning, drafting and revising the pollinator paragraph before presenting the research. See the [module 3 assessment overview](https://curriculum.eleducation.org/sites/default/files/curriculum/modules/1529/g2m3modulelessonsassesmentoverview110317.pdf).

**Why it matters.** A busy writer could replace sustained writing from research with notes and oral reporting while still claiming to retain the source lessons.

**Exact fix.**

Add to unit 3:

> Students use their shared research notes to plan, draft, revise and edit an informational paragraph about a pollinator. They combine the paragraph with labelled drawings or captions and use that written work in the presentation.

Name that product in the writing calendar and candidate assessment. Mark W.2.2 and W.2.5 as review from their owning units. In unit 4, explicitly identify the return to gathering information from provided sources before opinion writing.

Retain the 41-day allocation.

### 5. Replacement anchors have no reviewable text records

**Location:** Texts and the reading level; all four Units rows  
**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, missing anchor evidence recurs in the ELA rubric and course reviews  
**Confidence:** firm on the missing evidence

**What is wrong.** The frame specifies categories and story premises, but defers every text record to later unit planning. The Grade 2 course folder contains only the frame. There are no linked replacement anchors with measures, qualitative analyses, reading modes and placement reasons.

Naming a chapter-length school story does not establish its actual demand. Replacing the trade books also removes the base text’s existing complexity evidence.

The [K to 2 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf), indicator 2b, require documented complexity evidence. The [K to 2 Publishers’ Criteria](https://www.thecorestandards.org/assets/Publishers_Criteria_for_K-2.pdf) also distinguish rich read-alouds from texts children read themselves.

**Why it matters.** The reader cannot judge the year’s staircase, cultural range or whether each proposed replacement supports the retained lessons.

**Exact fix.**

Provide a linked anchor inventory identifying each text, its file or commissioning status, literary or informational kind, length, reading mode, preliminary complexity analysis, placement reason and source or rights record.

Keep unwritten texts explicitly unverified. Before closing the frame’s anchor-text finding, supply the actual anchors and completed analyses. Include explicit higher-band student reading in units 3 and 4, rather than assigning every demanding text to read-aloud.

### 6. Three seam statements misidentify what is new

**Location:** Unit 1 reason; `ela.csv`, `e3-fluency` and `e2-rhythm-and-meaning`  
**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, incorrect onset and introduction claims recur in both ELA progression reads  
**Confidence:** firm

| Problem | Why it matters | Exact replacement |
|---|---|---|
| Unit 1 says students meet chapter books here, although Grade 1 already plans a whole four-to-five-chapter story | Repeats an introduction instead of defining increased demand | “This extends Grade 1’s whole chapter story through a new school story, sustained rereading and more independent text-based responses.” |
| `e3-fluency` says Grade 3 adds poetry and recording, although Grade 2 already includes poems and owns story or poem recording | Misstates the outgoing performance | “Grade 2 creates story or poem recordings. Grade 3 adds an explicit emphasis on fluent recorded reading, with accuracy, appropriate rate and expression for listeners.” |
| `e2-rhythm-and-meaning` says similes and metaphors are named in grades 3 and 4, while the Grade 3 row reserves named kinds for Grade 4 | Gives the next writer conflicting boundaries | “Grade 3 distinguishes literal and nonliteral meanings; Grade 4 explicitly teaches simple similes and metaphors in context.” |

The final correction follows [L.4.5a](https://www.thecorestandards.org/ELA-Literacy/L/4/). These are wording repairs, not standard moves.

### 7. The cross-subject table does not faithfully trace the progression’s leans

**Location:** Cross-subject section  
**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, incomplete availability records recur in the cross-subject reviews  
**Confidence:** firm

**What is wrong.** The table omits `e2-fables-folktales`’ culture connection, substitutes `e2-images-and-text`, omits `e2-informative`’s plant-investigation connection, changes the research reference from 2-LS2-2 to 2-LS2-1, and substitutes `e2-tell-and-record` for the discussion row’s interview connection.

Several source teaching points remain “its own calendar” or “when it comes”, although the source frames now exist.

**Why it matters.** Teachers cannot distinguish an actual prerequisite from a later application or a topic connection requiring local teaching.

**Exact fix.** Replace the dependency record with these seven actual leans:

| ELA row | Source teaching point | Availability and bridge |
|---|---|---|
| `e2-fables-folktales` | Social studies unit 6, culture and migration | Not guaranteed before ELA unit 4 begins. Introduce each tale’s people, place and cultural context within ELA |
| `e2-compare-texts` | Social studies unit 5, two accounts | Normally precedes ELA unit 4; ELA still teaches literary-version comparison |
| `e2-opinion` | Social studies unit 2, sourced claim | Earlier than ELA unit 4; retain ELA’s full writing instruction |
| `e2-discussion` | Social studies unit 6, interviews | Later application of ELA unit 1 discussion, not its prerequisite |
| `e2-connections-series` | Science unit 6, pollinator models | Later than ELA unit 3’s opening; ELA texts teach the needed process |
| `e2-research` | Science unit 6, pollinators | Supply observations and sources locally until science reaches it |
| `e2-informative` | Science unit 5, plant investigations | A later application of ELA writing; supplied evidence supports earlier ELA work |

Retain fossil knowledge as an additional topic connection, labelled accordingly. Do not imply that science investigations have already occurred.

### 8 to 12. Five stale review notes still treat the ELA frames as absent

All five findings concern `docs/reviews/frame-science-grade-2-codex-2026-11-14.md`.

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, unmarked stale notes recur in earlier frame reviews  
**Confidence:** firm

Preserve the historical review. Add a dated superseding disposition beside each note, using the replacement below.

| Finding | Location and stale claim | Why it matters | Exact current disposition |
|---|---|---|---|
| **8** | Line 22: Grade 2 ELA frame does not yet exist | Defers a comparison now possible | “Superseded 2026-11-14: the Grade 2 ELA frame exists at docs/courses/english-language-arts-grade-2/frame.md.” |
| **9** | Line 160: proposed repair says Grade 1 ELA remains pending | Would introduce a stale note into another frame | “The Grade 1 ELA frame exists. Verify these connections against its unit sequence and retain local bridges where science comes first.” |
| **10** | Line 178: proposed repair says Grade 2 ELA remains pending | Same problem in the mathematics follow-up | “The Grade 2 ELA frame exists. Use its stated teaching points when verifying the cross-subject calendar.” |
| **11** | Line 215: absent Grade 2 frame prevents timing verification | Conceals the available teaching order | “Grade 2 ELA teaches discussion in unit 1, narrative and revision in unit 2, research in unit 3 and opinion writing in unit 4. Science retains bridges wherever it uses these performances earlier.” |
| **12** | Line 259: exact ELA availability cannot be judged without the frame | Leaves a resolved artifact dependency open | “The ELA frame is available. Frame-level timing can be compared; exact lesson timing remains for the scope and sequence.” |

The stale checker’s clean result does not detect these claims.

## Ownership, standards, reasons and days

All 30 owned skills are placed exactly once. No unjustified ownership of another grade’s skill was found. The problems are the descriptions, completion points and performances identified above.

| Unit | Days | Owned skills | Base topic lessons | Days beyond topic lessons |
|---|---:|---:|---:|---:|
| Schools and community | 32 | 8 | 30 | 2 |
| Fossils | 42 | 11 | 39 | 3 |
| Pollination | 41 | 5 | 38 | 3 |
| Providing for pollinators | 39 | 6 | 36 | 3 |
| **Units** | **154** | **30** | **143** | **11** |
| Course checks and respond days | **6** | | | |
| **Course total** | **160** | | | |

The annual allocation fits the repository’s 160-day yardstick and reserves four course-check days and two respond days. No unit is demonstrably far over or under its share. The smaller skill count in unit 3 does not justify shortening research, writing and presentation work.

The 130 foundations lessons fit within 154 unit days, leaving 24 foundations blocks for additional work. That annual arithmetic does not settle the ambiguous within-unit mapping in finding 1.

The topic sequence is defensible: classroom routines first, fossil reading and narrative next, pollinator research before conservation opinion. The retained source lesson ranges account for the topic year. Combined lesson PDFs must be counted by lesson numbers, not file count.

The source policy permits the 2017 base and excludes the later non-commercial editions. No prohibited edition is explicitly mapped. Individual replacement-text rights remain unverified.

## Seams and lens checklist

The incoming Grade 1 skill and model links are substantially sound. Grade 3 retains explicit long-word instruction and fluency work, so this frame does not abandon foundations at the transition. Findings 3 and 6 repair misleading descriptions of that handoff.

| Course-frame lens line | Result |
|---|---|
| Units use specific topics and texts rather than isolated skills or broad themes | **Met at topic level**; actual text evidence remains incomplete |
| Anchor texts are on file with complexity evidence and placement reasons | **Missed**, finding 5 |
| Texts provide a defensible range of traditions, eras and kinds | **Not established**; the proposed mix is promising, but the anchors are unavailable |
| A long text is read whole | **Met as a planning commitment**; the actual text remains unverified |

The two-block design, decoding prohibition on guessing, continuing fluency, frequent text discussion, three writing types and explicit response days should remain. Question quality, decodable alignment, assessment scoring and actual text sensitivity cannot be certified from this frame.

## Settled by the expert

These are recommendations for the caller to apply, not edits made here.

| Choice | Reason | File affected |
|---|---|---|
| Retain four units, 160 days and existing topic allocations | Source lesson counts support the budget | Grade 2 frame |
| Describe cycles 20 to 26 as instruction plus review | They introduce additional content | Grade 2 frame |
| Record an existing unit 3 story or poem | Completes the recording genre requirement | Grade 2 frame |
| Keep unsupported and supported reading evidence distinct | Preserves the Grade 2 band requirement | Grade 2 frame |
| Explicitly retain the pollinator paragraph and illustrated product | Makes the retained research lessons concrete | Grade 2 frame |
| Use the seven actual progression leans | Repairs the dependency record without changing scope | Grade 2 frame |
| Replace the three misleading onset statements | Existing standards and neighboring frames settle them | Grade 2 frame and `ela.csv` |
| Add dated dispositions to the five stale review notes | Preserves history while closing obsolete dependencies | Science Grade 2 review |

## For Cory

- **Scope:** decide the foundations ownership changes proposed in finding 1 if ownership continues to mean completion within the named unit.
- **Audience and time:** confirm the existing 120-minute daily literacy assumption and omission of the additional exploration hour.
- **People and money:** identify the qualified ELA and cultural readers already required by the frame. No contact or spending is authorized by this report.

## Sources and limits

- [Grade 2 literature](https://www.thecorestandards.org/ELA-Literacy/RL/2/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/2/), [foundations](https://www.thecorestandards.org/ELA-Literacy/RF/2/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/2/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/2/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/2/): required performances and boundaries.
- [2017 Grade 2 foundations sequence](https://files.eleducation.org/web/resources/Section-5_SkillsBlock-Year-at-a-Glance_Grade2_071417.pdf): cycle order. Checked beside local module overviews.
- [Module 3 assessment overview](https://curriculum.eleducation.org/sites/default/files/curriculum/modules/1529/g2m3modulelessonsassesmentoverview110317.pdf): written research before presentation.
- [K to 2 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf): foundations and anchor-evidence expectations. No rubric score assigned.
- [K to 2 Publishers’ Criteria](https://www.thecorestandards.org/assets/Publishers_Criteria_for_K-2.pdf): cumulative foundations and distinct student-reading and read-aloud demands.
- [WWC foundational-skills guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21): explicit decoding, word analysis and daily connected reading.
- [Core Knowledge skills sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/CKLA_K2_Skills_ScopeSequence.pdf), Grade 2 portions: a second curriculum comparison for integrated reading, spelling, writing and checks; reference only.

The live base-text planning and terms pages returned no usable substantive text. Licensing conclusions therefore rest on the repository’s policy and saved source evidence, not a fresh legal-text verification. The replacement anchors, classroom timing and complete plan gate remain unverified.

**For the source list:** add the working official K to 2 Publishers’ Criteria address and the current K to 2 review-criteria link if absent.

**Verdict:** coherent structure, revision required before detailed planning. **Finding count:** 12. **Report path:** `docs/reviews/frame-english-language-arts-grade-2-2026-11-14.md`, supplied here only.

