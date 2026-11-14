# Independent review: English Language Arts, Grade 1

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/frame-english-language-arts-grade-1-2026-11-14.md`  
**Delivery:** Complete report below. No file was written.

## Verdict

The four-unit architecture is sound, but the frame needs revision before downstream planning. Its biggest risk is contradictory foundations sequencing: the unit descriptions and source map can lead a writer to introduce patterns out of the base sequence or label new instruction as review. The most useful immediate change is one consistent foundations map across all four units, followed by completion of the promised anchor-text records before section planning.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, the shared and ELA approaches, the glossary, relevant BASELINE rules, and the requested roadmap sections.
- The complete grade 1 frame, its `frames.csv` row, all 31 grade 1 ELA progression rows, and every grade 1 standard and lettered part in the local full standards file.
- The kindergarten and grade 2 ELA frames, with their progression links into and out of grade 1.
- The grade 1 science frame and relevant social studies units and cross-subject provisions.
- The frame-writing brief, source register, base-text download and licence records, local grade 1 curriculum map and foundations coverage document, and lesson identifiers inside the base-text archives.
- Earlier ELA approach, course, progression, stitch, reconcile and fix reports; relevant grade 1 science and social studies reviews.
- Outside sources linked below.

No curriculum finding rests on unaided memory. Pacing judgments are professional judgments, not demonstrated classroom results.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check`, run first | Stopped before evaluating the plans: `ModuleNotFoundError: No module named 'markdown'` |
| Focused frame check | 0 failures; four units, 160 days, 154 within units |
| ELA progression check | 374 rows, 0 failures |
| `scripts/stale.py check` | 54 files, 0 failures |
| Additional read-only checks | All 31 grade 1 skills placed once; prerequisite and handoff links reciprocal; no standard record absent after parent-code expansion |

The full plan gate remains **unverified**. Its interruption establishes no curriculum failure. I continued because the focused checks completed successfully.

The missing `data/plans/english-language-arts-grade-1/source-map.csv` is **not a finding**: the frame-writing brief explicitly defers that day-level file until the scope and sequence. The prose source map is the applicable artifact here.

## Findings, most serious first

### 1. Foundations instruction does not consistently follow the claimed base sequence

**Severity:** High  
**LAYER:** base text  
**REPEAT:** yes, source-order discrepancies appeared in the earlier ELA progression read  
**Confidence:** firm

**Location:** Grade 1 frame, units 2 to 4, placement rule, and Source map.

**What is wrong:** Unit 3 lists silent-e work, common vowel teams, then r-controlled vowels. Unit 4 describes cycles 19 to 25 largely as review. The published base sequence instead places closed and open syllables and silent-e work in cycles 12 to 18, r-controlled vowels in cycles 19 and 20, and the main vowel-team instruction in cycles 21 to 24. The source-map description of module 3 as “Long vowels, vowel teams” is therefore misleading, and module 4 is assigned collectively to “3 and 4” without a boundary. [Base sequence, PDF page 2](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_Grade1.pdf).

The inflections thread also lacks a complete continuation record. Its progression notes include silent-e dropping in cycle 18, but the frame places `e1-inflections` in unit 2 without naming its later instruction. Conversely, the base introduces suffix `-s` in module 1, which conflicts with the frame’s claim that foundational rows sit where their first element is taught.

**Why it matters:** A writer following the frame literally can write decodables with untaught patterns, omit later inflection instruction, or assess a complete standard before its remaining patterns have been taught.

**Exact fix:**

- Map cycles 12 to 18, lessons 61 to 95, to unit 3.
- Map cycles 19 to 25, lessons 96 to 130, to unit 4.
- Rewrite unit 3’s foundations description as closed and open syllables, silent-e patterns, two-syllable decoding, and inflections on those taught bases.
- Rewrite unit 4 to name **new instruction** in r-controlled vowels, followed by vowel teams, then cumulative application.
- Name `e1-inflections` as continued in unit 3, including the cycle 18 spelling rule. Specify where the progression’s remaining endings are taught and checked.
- Replace the “first element” placement claim with a distinction between the primary owning unit and explicitly recorded teaching and assessment continuations. Preserve the existing owning rows and unit day totals.
- Ensure unit 3 checks assess the patterns taught by then; complete vowel-team evidence follows instruction in unit 4.

This agrees with the progression fix report’s decision to retain silent-e dropping in grade 1. I am not reopening the earlier proposed move to grade 2.

### 2. The anchor texts remain descriptions of future writing

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, the earlier grade 6 ELA course review identified missing anchor sets  
**Confidence:** firm

**Location:** Texts and reading-level bullet; all four unit descriptions; For the lead, item 4.

**What is wrong:** The frame describes stories, poems and informational texts but supplies no completed anchor-text files or records. The second sky-tale tradition is unnamed. The long bird story is a future four-to-five-chapter work, rather than an inspectable text. The frame itself acknowledges the replacement texts remain to be written.

The ELA frame lens explicitly requires anchors on file with placement evidence. The published K to 2 criteria also require documented analysis of anchor complexity. [K to 2 criteria, indicator 2b](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf).

**Why it matters:** Topics and plausible plots cannot establish text quality, vocabulary demands, cultural range, reading load or whether a proposed text supports its assigned standard. Replacing the base books also changes the evidence its questions and assessments depend on.

**Exact fix:** Add an anchor register with a stable text ID, title, file path, text type, read-aloud or student-reading role, source and rights status, qualitative analysis, reader/task analysis, and reason for placement. Identify the second sky tale and its specific tradition and source. Complete the anchors before their sections are planned, then adapt questions and assessments against those actual texts.

Use a suitable measure for read-aloud texts where meaningful. Do not impose a computed grade-band threshold on grade 1 decodables or poetry; record their taught-pattern constraints or qualitative demands instead.

### 3. The science availability table omits and misidentifies progression leans

**Severity:** Medium  
**LAYER:** frame  
**REPEAT:** yes, wrong-content cross-subject references appeared in the ELA progression review  
**Confidence:** firm

**Location:** Science cross-subject table; `e1-informative.cross_subject` and `e1-shared-research.cross_subject`.

**What is wrong:** The progression assigns both writing rows a `1-LS1-1` lean concerning bird body parts. The frame omits `e1-informative` from its availability table and substitutes sky-pattern research for `e1-shared-research`’s recorded bird lean.

The sky project is legitimate additional work. It does not account for the existing bird-research dependency.

**Why it matters:** A unit writer cannot use this table to find every promised dependency or determine whether science has supplied it.

**Exact fix:** Retain the sky entries as additional connections, then add:

| ELA row | Actual lean and first relevant use | Science availability | Bridge |
|---|---|---|---|
| `e1-informative` | `1-LS1-1`, bird-body explanation in ELA unit 3, about week 16 | Science unit 2, approximately weeks 5 to 10 | ELA bird texts explicitly teach each relevant part and function |
| `e1-shared-research` | `1-LS1-1`, bird research in ELA unit 3 | Same science unit | Provided sources supply every fact needed for the research question |

Record `e1-connections` separately against science unit 1, completed around week 4, before ELA unit 2 begins around week 7.

### 4. The social studies bridge is described as spoken when it is written

**Severity:** Medium  
**LAYER:** frame  
**REPEAT:** yes, reciprocal readiness claims were raised in the cross-subject progression review  
**Confidence:** firm

**Location:** Social studies cross-subject row and following paragraph, frame lines 157 and 159.

**What is wrong:** Both passages say social studies keeps its early claim spoken and drawn. Its current frame explicitly teaches a **written claim, reason and closing from unit 3**, with shared writing and a sentence frame before independence.

**Why it matters:** The two frames give conflicting instructions about the first written opinion work and conceal the bridge that actually makes their order viable.

**Exact fix:** Replace both descriptions with:

> Social studies unit 3 teaches a written claim, reason and closing around week 8 through shared writing and a sentence frame before independent writing. ELA unit 4 later develops opinion writing from its own texts and assesses W.1.1.

Keep the existing unit owners. Do not claim ELA has already completed W.1.1 by week 8.

### 5. L.1.4 loses its multiple-meaning requirement

**Severity:** Medium  
**LAYER:** standard  
**REPEAT:** yes, incomplete specification of an owned standard recurs in earlier frame reviews  
**Confidence:** likely

**Location:** Unit 4 and `e1-word-strategies.notes`.

**What is wrong:** Both describe strategies for unknown words, but neither explicitly carries forward work on **multiple-meaning words and phrases**. That requirement belongs to the parent standard, alongside flexible strategy choice. [Official standards, PDF page 27, printed page 27](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=27).

**Why it matters:** A writer can satisfy every listed strategy using only unfamiliar single-meaning vocabulary and still leave part of the claimed standard untaught.

**Exact fix:** Add to unit 4 and the progression note:

> Determine meanings of unknown and multiple-meaning words and phrases. Contrast two uses of a familiar word in the unit texts, explain which sentence clues select each meaning, and apply the routine to a fresh example.

A suitable contrast is *fly* as an action and *fly* as an insect, provided both uses occur in the selected texts. Keep this work in unit 4.

### 6. The model record gives conflicting origins and an incorrect inherited count

**Severity:** Minor  
**LAYER:** progression  
**REPEAT:** yes, conflicting model-introduction prose appeared in ELA progression finding F8  
**Confidence:** firm

**Location:** `e1-opinion.notes`, `e1-informative.notes`, grade 1 Models carried summary, and grade 2’s paragraph-frame attribution.

**What is wrong:** Unit 1 introduces `paragraph-frame`, while the opinion progression note says it introduces the same model in unit 4. The frame identifies this problem but leaves its correction outstanding. The summary also says eight models come from kindergarten; the table and progression support **eleven inherited models and four new ones**.

**Why it matters:** Writers receive two introduction points for one representation, while the summary understates what the kindergarten handoff supplies.

**Exact fix:**

- Change `e1-opinion.notes` to “Uses the paragraph-frame introduced in e1-informative.”
- Make `e1-informative.notes` explicitly name its introduction.
- Attribute grade 2’s inherited paragraph-frame to `e1-informative`.
- Replace “Eight models” with “Eleven models.”
- Close For the lead, item 3, after these wording changes.

No standard or unit moves.

### 7. The open-material review still presents the 2017 foundations licence check as unresolved

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the social studies frame reviews already identified this stale result  
**Confidence:** firm

**Location:** `docs/reviews/ela-open-material-2026-11-12.md`, phonics summary, 2017 Skills Block table, recommendation table, and Open items 1 and 2.

**What is wrong:** These passages still make the foundations base conditional on a file check. The source register and retained source-store evidence record that check as completed.

**Why it matters:** A later worker can reopen a settled dependency or unnecessarily plan a replacement foundations course.

**Exact fix:** Add a dated resolution and mark the linked open items closed:

> Resolved 2026-11-13: the retained 2017 Skills Block evidence supports its use as the foundations base under the repository’s source policy. The 2024 edition remains reference only. See BASE-TEXTS.md and the source store’s licence evidence. Third-party exclusions still require item-level checks.

Preserve the original dated research as history. In the grade 1 frame’s lead item 2, replace the obsolete assignment dispute with this resolved edition distinction.

### 8. The science expert review still says the ELA frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, unavailable-file status claims recur in earlier frame reviews  
**Confidence:** firm

**Location:** `docs/reviews/frame-science-grade-1-2026-11-14.md`, What I read, Cross-subject, and What I could not judge.

**What is wrong:** The report repeatedly says no grade 1 ELA frame exists. It now exists and was available for this comparison.

**Why it matters:** The report leaves a resolvable availability check presented as blocked.

**Exact fix:** Add a dated closure beside those passages:

> Updated 2026-11-14: the grade 1 ELA frame is available and has been compared. Its unit 1 question-answering and informative-writing commitments precede science’s later uses. Retain science’s teacher modelling and sentence-frame bridges. The ELA frame review records the remaining cross-subject corrections.

Keep the original reading limitation as a historical observation.

### 9. The science independent review’s proposed replacement notes perpetuate the same obsolete deferral

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale availability wording is already documented in that review  
**Confidence:** firm

**Location:** `docs/reviews/frame-science-grade-1-codex-2026-11-14.md`, proposed replacement text in findings 3 and 5, Seams and cross-subject timing, and the ELA limitation.

**What is wrong:** The proposed repairs themselves say ELA timing must remain pending because its frame is absent.

**Why it matters:** Applying those repairs now would insert a stale dependency into current planning documents.

**Exact fix:** Replace the ELA-pending clauses with:

> The grade 1 ELA frame is available. Its unit 1 question-answering and informative-writing commitments precede science’s later uses; retain the specified teacher bridges.

Add a dated follow-up to the review’s limitation section. Preserve the separate, still-valid limitation concerning the unavailable full plan gate.

## Ownership, standards, units and days

All 31 owned skills appear exactly once. All **81 grade 1 standard records**, including lettered parts, are represented through explicit codes or their named parents. That establishes placement, not full teaching; findings 1 and 5 qualify substantive coverage.

| Unit | Days | Owned skills | Base topic lessons | Topic-day margin | Judgment |
|---|---:|---:|---:|---:|---|
| Tools and work | 33 | 12 | 31 | 2 | Routines, concrete knowledge and first informative writing justify the allocation |
| Sun, moon and stars | 42 | 10 | 40 | 2 | Narrative, research and sentence work justify the load |
| Birds’ amazing bodies | 41 | 4 | 39 | 2 | Research and foundations instruction explain the small row count and substantial time |
| Caring for birds | 38 | 5 | 36 | 2 | Opinion, comparison, language and final foundations work need the full allocation |
| **Units** | **154** | **31** | **146** | **8** | No unit demonstrably far over or under its share |
| Course checks and responses | **6** | | | | Two two-day checks, each followed by one respond day |

The 160-day course leaves approximately 20 days within a 180-day year. The proposed foundations allocation leaves 8, 7, 6 and 3 days beyond the base lessons in the respective units, using finding 1’s consistent boundaries. These are parallel blocks, so their lesson counts are not added together.

The topic lesson ranges match the local archives. Module 4’s paired lesson bundles must be counted as lesson ranges, not as single archive files. Labs, trade books, videos and later-edition crosswalks have explicit exclusion reasons. No NC or reference-only source is mapped for adaptation.

Kindergarten supplies the stated prerequisite skills and models; grade 2 picks up the grade 1 outputs. The recorded links are reciprocal. Retaining r-controlled work in grade 1 has an explicit base-order rationale, so it is not an unexplained intrusion from another grade.

## ELA lens checklist: course frame

| Lens line | Status | Evidence |
|---|---|---|
| Units use specific topics and texts rather than isolated skills or broad themes | **Met in design** | Tools, sky patterns and two connected bird studies provide coherent topics; actual texts remain outstanding |
| Anchors are on file with analysis and placement reasons | **Missed** | Finding 2 |
| The year has sufficient range of kinds, traditions and perspectives | **Missed for verification** | Stories, poems and information are promised; the second tale tradition and completed text register are absent |
| A long text is read whole | **Missed as an available artifact** | A whole chapter story is planned, but unwritten; finding 2 |

The 80 percent task count, actual decodable alignment, question quality and lesson-level supports require later artifacts. They are not passed by this frame read.

## What is right and should remain

- Preserve the topic sequence and the deeper second bird unit.
- Preserve separate rich read-aloud and foundations blocks, explicit decoding, spelling and the ban on guessing words from pictures.
- Preserve repeated research, the three writing types, frequent discussion and digital-production routes that distinguish paper participation from completing a technology requirement.
- Preserve the baseline check, unfamiliar assessment texts, respond days and grade 2 handoff record.
- Preserve privacy provisions, optional home observations, safe bird-watching alternatives and qualified cultural reads.

## Settled by the expert

These are recommendations for the caller. Nothing was edited.

| Choice | Reason | File affected |
|---|---|---|
| Retain four units and 33, 42, 41 and 38 days | The two parallel blocks and base lesson counts support them | Grade 1 frame |
| Place foundations cycles 12 to 18 in unit 3 and 19 to 25 in unit 4 | Gives every lesson one destination and preserves base order | Grade 1 frame |
| Record later foundations instruction as explicit continuation | Prevents “review” from concealing untaught patterns | Grade 1 frame |
| Keep silent-e dropping in grade 1 | The settled base-text placement is cycle 18 | Frame and progression notes |
| Add multiple-meaning work within existing unit 4 ownership | Completes an already-owned requirement | Frame and `e1-word-strategies` |
| Identify paragraph-frame’s first use as unit 1 | Matches the actual informative-writing sequence | Progression and neighboring frame |
| Correct inherited models to eleven | Matches the table and kindergarten handoff | Grade 1 frame |

## What I could not judge

The full plan gate, completed anchor quality, final cultural and rights clearance, actual decodable vocabulary, assessment scoring guidance, classroom minutes and the effectiveness of response routines remain unverified. The current publisher planning and terms pages returned navigation without usable body content, so those pages were not treated as freshly verified licence evidence.

## Sources and source-list notes

- [Official ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): grade 1 requirements, including the complete L.1.4 wording.
- [Published grade 1 foundations sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_Grade1.pdf): cycle order and the transition from syllables and silent-e patterns to r-controlled vowels and vowel teams.
- [K to 2 review criteria, July 2025](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf): selected foundations, text-analysis, writing and research indicators. No course score was assigned.
- [K to 2 Publishers’ Criteria](https://achievethecore.org/content/upload/2._Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf): read-aloud complexity and the distinction between language comprehension and beginning independent reading.
- [Federal foundations practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21): systematic sound-to-print instruction and daily connected-text reading.
- Local curriculum map: block purposes, module structure and assessment distinctions. :codex-file-citation{path="S:/CurioClass-sources/el-education-k5-2017/grade-1/curriculumtools_curriculummap-grade1_072017.pdf" purpose="source"}
- Local foundations coverage document: instruction, assessment and continued practice across modules. :codex-file-citation{path="S:/CurioClass-sources/el-education-k5-2017/program/skills-block/curriculumtools_skillsblock-standards-scope-and-sequence_grade1_052217_0.pdf" purpose="source"}

**For the source list:** Add the working K to 2 criteria URL and grade 1 sequence URL. Update the K to 2 Publishers’ Criteria entry to identify the portions inspected in this review. Record the publisher-page retrieval limitation.

## For Cory

- **Audience and time:** Confirm the proposed 120-minute daily ELA allocation alongside the other grade 1 subjects.
- **Audience and access:** Set the remaining K to 2 device assumption so the shared-device publishing route has an assured setting.
- **People and money:** Identify the qualified ELA and tradition readers required by the planned original texts, including arrangements for any paid reads.

**Verdict:** Revise before downstream planning. **Finding count:** 9, comprising 6 curriculum or planning findings and 3 stale-note findings. **Report path:** `docs/reviews/frame-english-language-arts-grade-1-2026-11-14.md`, delivered here only.

