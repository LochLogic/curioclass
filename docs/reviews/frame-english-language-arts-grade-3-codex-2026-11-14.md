# Independent frame review: English Language Arts, Grade 3

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/frame-english-language-arts-grade-3-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files written.

## Verdict

The four-unit structure is coherent, but the frame needs revision before detailed planning. Its biggest risk is that retained base lessons teach and assess skills before the frame assigns their first teaching, while the replacement anchors remain unavailable for checking. Reconcile the teaching order with the retained lessons first, then establish the texts and a feasible literacy schedule.

**Finding count: 11.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, the relevant Roadmap sections, `docs/APPROACH.md`, `docs/APPROACH-ELA.md`, `docs/APPROACH-SOURCES.md`, the glossary, BASELINE rules 20 to 24 and 29, and `docs/sources/BASE-TEXTS.md`.
- The complete Grade 3 frame and its `frames.csv` row.
- All 28 Grade 3 progression rows, their Grade 2 prerequisites and Grade 4 destinations, and both neighboring course frames.
- The Grade 3 science frame and the relevant units and availability calendar of Grade 3 social studies.
- Earlier Grade 3 and Grade 4 ELA frame reviews, relevant ELA progression reviews and dispositions, and the Grade 2 independent review.
- The source store’s notes and manifest; lesson filenames in all twelve Grade 3 module-unit archives; the 2017 curriculum map, particularly PDF pages 1 to 7; and the Life Science companion overview, PDF pages 2 to 5.
- Outside standards, review criteria, research guidance and comparison curriculum documents linked below.

The Grade 3 course folder contains only `frame.md`. Neither its `texts.csv` nor its `source-map.csv` exists. The frame-writing brief explicitly defers the lesson-level CSV source map to the scope and sequence, so that missing CSV is **not a finding**.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-3` | Passed: 0 failures; 153 unit days and 7 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures. |

The incomplete plan gate does not determine the curricular verdict.

## Findings, most serious first

### 1. Retained base assessments contradict the stated order of first teaching

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, Grade 3’s earlier frame review, finding 1  
**Confidence:** firm

**Location:** “Which row sits where,” Units 1 to 3, Models carried, and Source map.

The frame retains the first module’s assessments while placing several assessed skills later. The base curriculum map, PDF pages 6 to 7, identifies:

| Retained assessment | Required work | Current placement |
|---|---|---|
| Module 1, unit 1, end assessment | RL.3.4 and L.3.4 | Unit 2 |
| Module 1, unit 3, end assessment | Recorded reading, RF.3.4b and SL.3.5; revision, W.3.5 | Unit 2 |
| Module 2 assessments | L.3.1d, e, g, h and i | Units 3 and 4 |

The [base unit description](https://curriculum.eleducation.org/curriculum/ela/grade-3/module-1/unit-3) also identifies the recording and revised reading contract. Its indexed text was available; direct navigation now redirects to the planning page.

**Why it matters:** A writer cannot simultaneously retain those assessments, teach the Grade 3 steps later, and describe the earlier work as exclusively Grade 2 practice.

**Exact fix:** Submit the earlier review’s ownership correction for Cory’s decision: place fluency, writing process, word strategies and literal/nonliteral language in Unit 1; place the sentence and word-form work first taught in Module 2 in Unit 2. Identify later additions and returns by standard part. Name the recording and revised informative product in Unit 1, and reconcile early complete-sentence work with the speaking row rather than silently treating it as first taught in Unit 4. Update the ownership, models, descriptions and progression notes together.

These ownership changes require Cory’s decision.

### 2. Replacement anchors lack the evidence required at the frame layer

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the Grade 2 independent frame review, finding 5  
**Confidence:** firm on the missing evidence

**Location:** Reading level, Long text, and all four unit text sets.

The frame supplies premises, approximate lengths and intended measures, then defers text records to unit planning. It links no actual replacement anchors. A target range does not establish a text’s complexity, cultural specificity, quality or suitability for the retained questions.

The course-frame lens explicitly checks for anchors on file with complexity and placement evidence. The [Grades 3 to 5 criteria, indicator 2b](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Review-Criteria.pdf), likewise calls for documented quantitative, qualitative and task analysis.

**Why it matters:** Replacing the base books removes the text evidence on which its lesson design depended. The proposed staircase and approximately equal literary/informational balance remain unverified.

**Exact fix:** Add an anchor inventory with stable identifiers, actual text locations, reading mode, length, rights, complexity analysis and placement reasons. Put the original drafts on file before closing this finding. Identify sufficient connected material from the second series book to support comparison of its theme, setting and plot. Mark unwritten texts and estimated measures explicitly unverified.

### 3. The 90-minute schedule does not account for its promised work

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 3 frame review, finding 2  
**Confidence:** likely

**Location:** Days; the daily skills-block promise; `e3-reading-range`.

The frame keeps a 60-minute module lesson whole and gives 30 minutes to daily word reading and spelling, followed by alternating fluency or independent-reading conferences. Sentence instruction and responsive small-group teaching have no explicit allocation. Meanwhile, the progression promises daily independent reading.

The base curriculum map identifies five components in its additional hour, including grammar, usage and mechanics within its fluency component. Keeping “fluency” does not explain where that language work goes.

**Why it matters:** Writers may add instruction on top of a full lesson or quietly omit practice. [Federal foundational-reading guidance](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) supports daily connected-text reading with instructional feedback; it does not establish that this proposed compression will work.

**Exact fix:** Supply a weekly timetable totaling no more than 450 minutes, explicitly locating word reading, spelling, sentence work, oral reading with feedback, independent reading and responsive teaching. Reconcile “daily independent reading” with the alternating schedule. Name every removed base component and its replacement or omission. Keep the 90-minute version provisional until representative days are timed; send any longer required block to Cory.

The earlier review’s suggested independent-reading minimum is a planning judgment, not a research-established threshold.

### 4. L.3.3b is reduced to differences between media

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete-standard coverage recurs in earlier ELA frame reviews  
**Confidence:** firm

**Location:** Unit 4; `e3-speaking-reports`.

“What speech can do that a page cannot” concerns the affordances of speech and writing. [L.3.3b](https://www.thecorestandards.org/ELA-Literacy/L/3/) concerns recognizing and observing differences between their **conventions**.

**Why it matters:** A teacher could teach voice and gesture without teaching the claimed language requirement.

**Exact fix:** Add this Unit 4 instruction:

> Compare the announcement’s spoken delivery with its written script. Identify conventions each uses, then rehearse and edit so both follow the conventions appropriate to their form.

Include a short paired model and a check requiring students to identify and apply one difference. Make the progression note say conventions explicitly.

### 5. SL.3.2 is planned only through a read-aloud

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete-standard coverage  
**Confidence:** likely

**Location:** Unit 1’s main-idea work and its ownership of SL.3.2.

The unit description specifies a text read aloud. It does not place the visual and quantitative formats named in [SL.3.2](https://www.thecorestandards.org/ELA-Literacy/SL/3/). The progression mentions a chart, but the unit has no corresponding task.

**Why it matters:** The frame claims full coverage while giving its writer only the oral route.

**Exact fix:** In Unit 1, add a short library-information presentation containing a simple labelled visual and quantities readable with Grade 2 mathematics. Students identify its main idea and supporting details from the combined presentation. Keep ownership in Unit 1 and name this task beside the read-aloud.

### 6. RL.3.5’s progression across poems and drama is unspecified

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete-standard coverage  
**Confidence:** likely

**Location:** Unit 3 and `e3-story-parts`.

Unit 3 names chapter, scene and stanza, but only specifies explaining how successive **chapters** build. Its short play scene offers no stated sequence of scenes, and the unit does not bring back a multi-stanza poem for this purpose.

[RL.3.5](https://www.thecorestandards.org/ELA-Literacy/RL/3/) combines naming parts with describing how successive parts build.

**Why it matters:** The writer could teach three labels while teaching the structural relationship on only one form.

**Exact fix:** Keep ownership in Unit 3. Return to one Unit 2 poem with at least two stanzas and use a short two-scene script. Ask what the later stanza or scene adds to the earlier one, alongside the chapter comparison. Label earlier Unit 2 work as Grade 2 practice until this Grade 3 instruction occurs.

### 7. Two progression notes still conflict with the chosen texts and placement

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, the earlier Grade 3 frame review, finding 4  
**Confidence:** firm

**Location:** `e3-character-actions`, CSV line 94; `e3-compare-two-texts`, line 104.

The character note retains stories involving war, while the frame explicitly excludes war. The comparison note specifies Grade 3 comparison practice on Unit 2 frog texts, although the frame places first teaching in Unit 4 and says earlier units use the Grade 2 form.

**Why it matters:** A writer using the progression can commission different content or teach the later comparison demand early.

**Exact fix:**

- Replace “war or poverty” with “poverty or distance,” matching the current frame.
- Replace the frog-comparison clause with: “Unit 2 reviews Grade 2 comparison of important points; Unit 4 first teaches comparison of both important points and key details.”

Retain the established ownership unless Cory changes it.

### 8. The Grade 4 incoming seam adds an unsupported typed-page prerequisite

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, incorrect teaching-onset claims recur in the ELA progression reviews  
**Confidence:** firm

**Location:** Grade 4 frame, Seams, `e3-writing-process` row, line 76.

Grade 4 says Grade 3 hands on “a typed page.” Grade 3 explicitly sets no typing page count, and [W.3.6](https://www.thecorestandards.org/ELA-Literacy/W/3/) sets none.

**Why it matters:** Grade 4 could assume a typing quantity that the preceding course neither promises nor checks.

**Exact fix:** Replace the incoming description with:

> Planning, revising and editing; supported keyboarding and digital production and publishing.

Keep one page in a sitting as Grade 4’s taught destination.

### 9. The early slavery excerpt needs its own content bridge

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 3 frame review, finding 5  
**Confidence:** likely

**Location:** Unit 1 and Cross-subject.

The Washington selection introduces enslavement in Unit 1. Social studies places its slavery instruction in Unit 5. Sensitivity review is planned, but the frame does not explicitly supply the earlier historical explanation.

**Why it matters:** A teacher may assume that students already understand the context essential to the reading.

**Exact fix:** Add this cross-subject entry:

> ELA Unit 1 supplies a brief, accurate explanation of enslavement and emancipation before the Washington selection. Social studies Unit 5 develops the history later. The ELA task assesses understanding of the selection, not prior historical knowledge.

### 10. An earlier review still leaves the calendar pending nonexistent peer frames

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale dependency notes recur in earlier frame reviews  
**Confidence:** firm

**Location:** `docs/reviews/frame-social-studies-grade-3-codex-2026-11-13.md`, Cross-subject availability, approximately lines 209 to 215.

The passage concludes that the calendar should remain provisional until peer frames exist. Grade 3 mathematics, ELA and science frames now exist.

**Why it matters:** This leaves a completed prerequisite looking like outstanding work.

**Exact fix:** Preserve the historical observation and append:

> Superseded 2026-11-14: the Grade 3 mathematics, ELA and science frames now exist. Check availability against those frames. Retain the social studies spoken-claim bridge because full ELA opinion writing begins in Unit 3.

### 11. The same review retains an obsolete limitation

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale dependency notes  
**Confidence:** firm

**Location:** The same report, “What I could not judge,” line 254.

The limitation still refers to peer course frames that do not yet exist.

**Why it matters:** A later reader can mistake the old limitation for the current review boundary.

**Exact fix:** Add a dated disposition:

> Superseded 2026-11-14: peer frames are available. Their planned teaching order can now be checked; daily scheduling and classroom timing remain unverified.

## Ownership, days and seams

All **28 owned skills occur exactly once** in the ownership column. There are no missing, duplicate or foreign-grade skill identifiers.

| Unit | Days | Owned rows | Judgment |
|---|---:|---:|---|
| 1 | 39 | 11 | Heavy launch, but routines and reading foundations justify substantial time. Finding 1 affects its teaching order. |
| 2 | 38 | 9 | Substantial reading, research, narrative and informative writing justify the allocation. |
| 3 | 39 | 5 | Whole-book reading and sustained writing justify more days than its row count suggests. |
| 4 | 37 | 3 | Research, opinion-writing practice and the final spoken product justify the allocation. |
| Course checks and response | 7 | — | Four assessment days and three respond days. |

The 160-day course leaves 20 days against a 180-day school-year yardstick. No demonstrated annual allocation defect warrants changing the total.

All 39 incoming prerequisite references and 35 outgoing references appear in the Grade 3 seam tables. The Grade 2 foundations handoff is recognized; the Grade 4 typed-page description needs correction under finding 8.

## Source-map judgment

The archive lesson numbers confirm **37 + 38 + 39 + 39 = 153 base lessons**. Unit 1 adds two screening days; Unit 4 merges lessons 8 to 10 into one audio-recording day, removing two days. The resulting 153 unit days are accounted for.

The selected ELA modules remain in order. No non-commercial or reference-only curriculum is mapped as a base.

**Correction to the earlier review:** Its finding 3 calls the stored Life Science module an alternative ELA module. The [companion overview](https://cms.eleducation.org/documents/2847/G3_LifeScience-ModuleOverview_0519.pdf), PDF pages 3 to 5, identifies a science module designed to work alongside ELA Module 2, with science expectations and investigations. It is not a replacement ELA module or an additional missing part of this ELA year.

Add an exclusion note for clarity, but do not import its science lessons into this course’s ELA count.

## Cross-subject judgment

- **Map work:** Social studies Unit 1 overlaps ELA Unit 1. The ELA title-and-key bridge prevents a prerequisite failure.
- **Opinion:** Social studies teaches claims early; ELA teaches full opinion writing later. The spoken and sentence-frame bridge remains necessary.
- **Frog life cycles:** Science’s stated school-day range, approximately 49 to 77, overlaps ELA Unit 2, days 40 to 77. The frog texts must supply the opening knowledge.
- **Habitats:** Science teaches the relevant work approximately days 79 to 104, after the frog unit. The ELA text-based bridge correctly avoids assuming prior science instruction.
- **Slavery:** Finding 9.
- **Grade 5 water:** The deeper Grade 5 topic was decided and is distinguished in the Grade 3 note. Do not reopen that topic choice.

## Lens checklist: course frame layer

| Checklist line | Result |
|---|---|
| Units use specific topics and texts rather than isolated skills or broad themes | **Met in outline.** Unit 3’s eventual series must supply a concrete shared subject. |
| Anchors are on file with measures, qualitative analyses and placement reasons | **Missed.** Finding 2. |
| The year avoids leaning to one era, tradition or text kind | **Missed as verifiable evidence.** The proposed range is promising; actual selections and counts are unavailable. |
| A long text is read whole | **Met as a plan.** Unit 3 explicitly requires a whole chapter book; the manuscript remains unverified. |

Progression, scope-and-sequence, unit and day checklist lines were considered where they reveal dependencies. This report does not certify those other layers.

## Settled by the expert

These are recommendations for the caller. No edits were made.

| Choice | Reason | File or location |
|---|---|---|
| Keep four units and the 160-day total | No demonstrated annual pacing defect | Grade 3 frame; `frames.csv` |
| Teach spoken/written conventions explicitly | Completes the existing language requirement | Unit 4; `e3-speaking-reports` |
| Add visual and quantitative main-idea work | Completes the existing listening requirement without advanced mathematics | Unit 1 |
| Use a multi-stanza poem and two-scene script | Makes the structural relationship teachable across forms | Unit 3 |
| Remove the typed-page prerequisite | Grade 3 promises keyboarding without a quantity | Grade 4 incoming seam |
| Describe Life Science as an excluded science companion | Its own overview establishes its purpose | Grade 3 Source map; disposition of earlier review finding 3 |
| Add dated dispositions to the two obsolete review notes | Preserves history while closing outdated dependencies | Social studies independent review |

## What is right and should remain

Keep the whole-book commitment, repeated research, daily text-based writing, explicit decoding rule, teacher-held fluency timing, meaningful device route and honest statement that paper alone does not complete digital publishing.

Keep the specific sensitivity provisions and the distinction between fresh-agent review and the required qualified human reads. Do not shorten Unit 4 simply because it owns fewer new rows.

## What remains unverified

Actual anchor quality, rights, complexity, representation, reading volume and compatibility with the retained lessons require the texts themselves. Question dependence, assessment coverage and scoring quality require the later assessment and task files. Classroom feasibility requires timing evidence.

No curricular conclusion here rests solely on model memory. Local source copies, current repository evidence and retrieved outside sources support the judgments; access limits are stated below.

## Sources and access

- [Grade 3 reading standards](https://www.thecorestandards.org/ELA-Literacy/RL/3/), [language standards](https://www.thecorestandards.org/ELA-Literacy/L/3/), [speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/3/), and [writing standards](https://www.thecorestandards.org/ELA-Literacy/W/3/): checked required verbs, forms and boundaries.
- [Grades 3 to 5 review criteria](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Review-Criteria.pdf): checked anchor-evidence and foundational-skills expectations. No rubric score assigned.
- [Foundational reading practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21): checked daily connected-text practice and feedback guidance.
- [Base Module 1, unit 3](https://curriculum.eleducation.org/curriculum/ela/grade-3/module-1/unit-3): indexed description corroborated its recording and revision assessments; direct navigation redirected. The locally read curriculum map supplied independent source evidence.
- [Grade 3 comparison skills sequence](https://www.coreknowledge.org/wp-content/uploads/2017/06/CKLA_G3_Scope-and-Sequence_Skills-.pdf) and [content sequence](https://www.coreknowledge.org/wp-content/uploads/2017/06/CKLA_G3_Scope-and-Sequence_LandL.pdf): inspected early systematic skills review and integration with content. Used as reference only.
- [Life Science companion overview](https://cms.eleducation.org/documents/2847/G3_LifeScience-ModuleOverview_0519.pdf): read from the stored PDF; the web tool could not retrieve its current download.

**For the source list:** Record the working criteria CDN address and the Life Science companion’s correct classification. Note that old base-unit web addresses now redirect even when indexed descriptions remain available.

## For Cory

- Decide the proposed standard-ownership moves in finding 1.
- Decide the literacy-block assumption if a complete, timed 90-minute schedule cannot carry the promised work.
- Arrange the qualified ELA and sensitive-content readers, including any payment.

**Verdict:** Revise before detailed planning. **Findings:** 11. **Report path:** `docs/reviews/frame-english-language-arts-grade-3-2026-11-14.md`, delivered here only.