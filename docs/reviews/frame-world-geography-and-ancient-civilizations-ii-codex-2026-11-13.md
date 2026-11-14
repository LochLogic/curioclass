# Independent expert read: World Geography and Ancient Civilizations II

**Date:** 2026-11-13  
**Intended report:** `docs/reviews/frame-world-geography-and-ancient-civilizations-ii-2026-11-13.md`  
**Delivery:** Markdown only. No files changed.

## Verdict

Revise before using this frame to direct unit writing. Its sequence, skill placement and year budget are coherent, but structural completeness conceals missing standard requirements, including omissions in the loaded anchor itself. Restore those requirements within their existing units, make the economics performances explicit, and secure the remaining mathematics prerequisite.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, `FOUNDATION.md`, relevant ROADMAP sections, BASELINE rules 20 to 24, and `GLOSSARY.md`.
- Section 1 and the shared criteria of `ADOPTION-BAR-SUBJECTS.md`; `docs/courses/social-studies/STANDARD.md`.
- `APPROACH.md`, relevant source-access and evidence notes in `APPROACH-SOURCES.md`, and `sources/BASE-TEXTS.md`. No social studies approach page exists.
- The target frame in full, its `frames.csv` row, all 29 grade 7 progression rows, and the relevant loaded standards.
- The grade 6 and grade 8 frames; the grade 9 frame’s opening and receiving seams.
- Relevant mathematics, ELA and science progression rows.
- Earlier social studies progression reviews, their fix report, cross-subject findings and fixes, and the social studies source-material review.
- Official sources linked below. No finding rests solely on memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Targeted `plan.py check world-geography-and-ancient-civilizations-ii` | Zero failures, but zero items checked |
| `frame.py check world-geography-and-ancient-civilizations-ii` | Zero failures |
| `stale.py check` | Zero failures; final run examined 19 files |

The global plan gate remains unverified. This is an environment failure, not evidence that the plan passed or failed. The targeted frame gate independently establishes placement and count consistency.

## Findings, most serious first

### 1. The loaded anchor changes Greek subpart identifiers and drops required India content

**LAYER:** standard  
**REPEAT:** yes, standard-to-plan mismatches recur in the earlier progression reviews; these particular defects are newly identified.  
**Confidence:** firm.

The official Greek democracy standard has five subparts, a to e. The local file combines them into a and b, and the frame explicitly repeats that altered structure. The local India standard also omits Ashoka’s missionary support and the Gupta literature-and-art requirement. See the [official framework, PDF pages 97 and 101](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=97).

**Why it matters:** A complete mapping against the local file can still produce incomplete teaching and incorrect external identifiers.

**Exact fix:**

- Restore `MA.7.T4b.3a` through `3e` in `data/standards/ma-hss-2018.txt`: polis; civic participation and voting rights; legislative bodies; constitution writing; rule of law.
- Restore the omitted India requirements in `MA.7.T1b.2d`, using original paraphrases.
- Update the frame’s parent-code explanation. Its expanded content-code count becomes **61 rather than 58**, holding the other entries constant.
- In existing unit 8, explicitly include constitution writing. In existing unit 2, include the restored India content and distinguish evidence for missionary activity from claims of successful conversion.

No standard needs to move between units.

### 2. Three correctly loaded requirements are still incomplete in the teaching descriptions

**LAYER:** frame, progression  
**REPEAT:** yes, earlier social studies progression reviews, finding 1.  
**Confidence:** firm on the omissions; likely on their instructional consequences.

| Existing placement | Missing requirement | Exact fix |
|---|---|---|
| Unit 3, `ss7-shang-zhou-confucius` | Encouragement of learning under Shang and Zhou | Add an explicit explanation supported by an appropriate source. |
| Unit 10, `ss7-roman-republic` | How Rome’s location contributed to political power | Require a geographical explanation alongside the location and expansion maps. |
| Unit 10, `ss7-republic-to-empire` | Military tactics | Add one concrete example connecting tactics, organization and conquest. |

These requirements appear in the loaded anchor and the [official framework, PDF pages 98 and 101](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=98).

**Why it matters:** Naming the code leaves the writer free to omit the missing performance.

Apply each addition to both the progression notes and the frame’s corresponding “What students learn” cell. Keep the present unit ownership and days.

### 3. The economics repair names the missing topics without securing their full performances

**LAYER:** progression, frame  
**REPEAT:** yes, earlier social studies progression reviews, finding 1.  
**Confidence:** likely.

Unit 4 now mentions skilled pay, exchange rates and lending risk. These additions improve coverage, but do not explicitly require students to explain supply or demand changes across those markets. Unit 11 mentions joblessness in its progression note, while its stated comparison remains about rising and falling prices.

The [C3 economics indicators](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf#page=37) require more than recognizing those terms.

**Why it matters:** A writer can satisfy the present prose with descriptions while omitting the claimed reasoning.

**Exact fix:**

- For `D2.Eco.6.6-8`, specify four short applications: a good or service, labor, credit and currency exchange. For each, students explain a supply or demand change and its effects on price and quantity.
- For `D2.Eco.12.6-8`, require a comparison of effects on different groups for **inflation, deflation and unemployment separately**.
- Use clearly labeled illustrative cases where historical evidence is insufficient. Do not make the unverified 33 CE example carry unemployment coverage automatically.

This disagrees with the fix report’s conclusion that the earlier economics findings were fully closed. Topic presence improved; the complete performances remain unsecured.

### 4. Unit 11 has an unprotected same-year mathematics dependency

**LAYER:** frame  
**REPEAT:** yes, the cross-subject reviews identified the same availability problem.  
**Confidence:** likely.

The frame requests grade 7 percent instruction before unit 11, days 134 to 144. The mathematics progression owns that content in `m7-percent-problems`, but no grade 7 mathematics frame currently establishes its timing.

The frame already supplies fallbacks for time offsets, research and argument. It supplies none for the percent dependency.

**Why it matters:** A teacher could reach the Roman economy work before students have learned the required calculation.

**Exact fix:** Replace the unit 11 mathematics request with:

> Pending(docs/courses/math-7/frame.md): confirm that m7-percent-problems precedes this unit. Until confirmed, teach the required tax-rate and percent-change method here with a worked example and brief practice before applying it to Roman evidence.

Keep grade 6 percent knowledge as a prerequisite only for tasks within its stated limits. Record all same-year ELA timings as requests awaiting the corresponding frame, rather than verified availability.

### 5. Unit 5’s compelling question can be answered without its historical evidence

**LAYER:** frame  
**REPEAT:** new.  
**Confidence:** judgment call.

“How do we compare societies fairly?” invites a general methodological answer. Students could answer it without studying Buddhism’s movement or comparing the named societies.

**Why it matters:** The question does not bind this otherwise defensible combination of content into an inquiry.

**Exact fix:** Replace it with:

> Which better explains similarities among these societies: their environments or their connections?

Retain fair comparison as a supporting question. Require students to support and qualify their answer using the unit’s maps, timelines and sources. Keep the 11 days.

### 6. The adoption bar still labels settled choices as unresolved

**LAYER:** process  
**REPEAT:** yes, stale status and pointers were findings in the earlier progression reviews.  
**Confidence:** firm.

Under “Decided,” `ADOPTION-BAR-SUBJECTS.md` says choices 1 and 5 “are not settled.” Its later section explicitly records both decisions as settled.

**Why it matters:** A reader can mistake completed decisions for active approval barriers.

**Exact replacement:**

> Choices 1 and 5 were settled in DESK-ANSWERS on 2026-11-12 and 2026-11-13. Their decisions and the historical questions are recorded below.

Retain the historical questions, clearly labeled as historical.

### 7. C3 edition confirmation remains listed as outstanding after an official-source read

**LAYER:** process  
**REPEAT:** yes, stale status wording.  
**Confidence:** firm.

The adoption bar’s standards paragraph and preparation table still require publisher confirmation. The earlier progression review records an official C3 read, and this review independently opened the publisher’s framework and citation information.

**Why it matters:** The preparation list requests work already performed.

**Exact replacement in both locations:**

> C3 publisher source confirmed: NCSS, 2013. The earlier progression review used the revised 2017 PDF. Preserve the exact version URL in the source record.

This closes edition identification, not a separate claim that every local indicator has been transcribed correctly.

### 8. ROADMAP still says social studies waits on an undecided content standard

**LAYER:** process  
**REPEAT:** yes, stale status wording.  
**Confidence:** firm.

The current ROADMAP’s “Subjects outside the core” paragraph says the social studies content standard is open and Cory must decide it. `STANDARD.md` and the adoption bar record the completed decision.

**Why it matters:** The repository’s governing order page presents an obsolete blocker.

**Exact replacement:**

> Superseded 2026-11-13: Cory selected the social studies standard method. P1 implementation is recorded in docs/courses/social-studies/STANDARD.md. Current production order follows docs/PRODUCTION-PATH.md.

Preserve the paragraph’s earlier history with that annotation.

### 9. The source-material review still requests two completed authorization decisions

**LAYER:** process  
**REPEAT:** yes, stale status wording.  
**Confidence:** firm.

`social-studies-open-material-2026-11-13.md` still asks Cory to accept OGL v3.0 and decide the retired-text AI clause. `BASE-TEXTS.md` records both decisions, and the review’s own later follow-up records OGL acceptance.

**Why it matters:** A reader could unnecessarily stop permitted source work.

**Exact status note to replace the outstanding decision request and annotate its conditional recommendations:**

> Settled 2026-11-13: Cory accepted OGL v3.0 and recorded his decision on the retired CC BY texts’ AI clause. BASE-TEXTS.md governs current use. Item-level rights checks and restrictions on third-party material remain.

This reports the repository’s decisions; it supplies no new legal conclusion.

### 10. The source-material review still describes completed loading as awaiting approval

**LAYER:** process  
**REPEAT:** yes, stale status wording.  
**Confidence:** firm.

The follow-up table calls the tribal-sovereignty and financial-education collections “Ready to load on Cory’s yes.” `BASE-TEXTS.md` records their completed loading.

**Why it matters:** Subsequent workers may repeat acquisition or request approval again.

**Exact replacements:**

- Tribal-sovereignty collection: “Loaded 2026-11-13. Current folder and inventory are recorded in BASE-TEXTS.md. Adaptation still requires the specified sensitivity and rights checks.”
- Financial-education collection: “Loaded 2026-11-13: 134 of 135 activities, 262 PDFs; one activity has a dead source link. See BASE-TEXTS.md.”

### 11. The earlier independent progression review’s loading statement is now stale

**LAYER:** process  
**REPEAT:** yes, stale status wording.  
**Confidence:** firm.

`progression-social-studies-codex-2026-11-13.md` says candidate partial bases “are not yet loaded.” The current source record shows several loaded collections.

**Why it matters:** This earlier review is explicitly part of later reviewers’ reading packs.

**Exact replacement:**

> At the time of the original read, candidate partial bases had not been loaded. Subsequent loading is recorded in docs/sources/BASE-TEXTS.md. No whole-course social studies base text has been adopted, so whole-course base-text ordering remains not applicable.

## Coverage, sequence and time

### Owned skills and days

Every one of the **29 owned progression skills appears exactly once**. No foreign-grade skill appears in the Skills column. Earlier content is generally identified as review, retrieval or reteaching.

| Unit | Days | Owned skills | Load judgment |
|---|---:|---:|---|
| 1 | 11 | 2 | Reasonable |
| 2 | 14 | 3 | Reasonable; retain room for finding 1 |
| 3 | 12 | 2 | Reasonable |
| 4 | 14 | 2 | Dense economics work; make finding 3 explicit |
| 5 | 11 | 2 | Reasonable comparison and diffusion unit |
| 6 | 11 | 2 | Feasible provisionally; source selection matters |
| 7 | 9 | 2 | Reasonable with the existing arithmetic fallback |
| 8 | 15 | 3 | Four action days leave 11 for historical instruction and assessment |
| 9 | 15 | 3 | Eight research days leave seven for wars and mythology; protect that allocation |
| 10 | 13 | 3 | Reasonable after completing the specified requirements |
| 11 | 11 | 3 | Tightest combination of conceptual work and prerequisites |
| 12 | 12 | 2 | Reasonable synthesis and argument allocation |
| **Units** | **148** | **29** | |
| **Course checks and respond days** | **12** | | |
| **Year** | **160** | | |

The year fits the repository’s 160-day yardstick, leaving about 20 days within a nominal 180-day calendar. The three check/respond blocks fall on days **63 to 66, 117 to 120 and 157 to 160**.

I found no defensible basis for moving days between units now. Skill counts alone do not measure load. The proposed 45-minute period and the dense units require later feasibility checks.

### Reasons and seams

The regional sequence and geography-before-history pattern hold. Placing the Silk Roads after both India and early China gives the exchange inquiry its prerequisites. The named Japan chronology exception and modern time-zone placement have reasons.

Grade 6’s maps, source routines, timeline, comparison framework and research work are picked up. Grade 8 receives the promised democracy, republic, perspective, research and economic foundations. The grade 9 receiving frame confirms the continuation from about 500 CE and identifies retrieval after the civics-year interruption.

The Models carried table places the inherited models before their required applications. Unit 9 deepens claim and evidence work already used earlier; it should not be interpreted as its first teaching.

### Sources and base-text mapping

No whole-course base text is adopted, and no source map exists. Consequently, exhaustive base-lesson placement and base-text boundary preservation are **not applicable at this layer**. No NC or reference-only lesson is mapped.

The frame correctly treats possible partial bases as conditional, with item-level rights checks. Choosing to adapt a particular unit later should trigger its corresponding source-map obligations.

## Course-frame lens checklist

| Checklist line | Status | Evidence |
|---|---|---|
| Every anchor standard in the course’s topic range has a unit | **Missed in substance** | Placement passes, but findings 1 and 2 identify incomplete requirements. |
| Replaced grade 3 content and grade 8 “your state” avoid Massachusetts-only content | **Not applicable** | This is grade 7. |
| Units identify check-set additions and record their sources | **Met at frame level** | Candidate additions name their check-set origins; confirmation belongs to unit comparison tables. |

The progression, scope and sequence, unit and day checklists are not separately scored here. Their relevant implications are addressed above; actual source difficulty, supporting questions and assessment performances remain later-layer work.

## Settled by the expert

Recommendations for the caller to apply. None was edited during this read.

| Choice | Reason | File touched |
|---|---|---|
| Restore authentic Greek subpart identifiers and complete their parent reference | Prevents false external mappings | Standards file; target frame |
| Complete the identified requirements in their existing units | Repairs coverage without moving standards | Social studies progression; target frame |
| Require explicit economic change-and-effect applications | Makes claimed performance observable | Same files, units 4 and 11 |
| Supply local percent instruction unless earlier availability is confirmed | Removes the unprotected prerequisite | Target frame |
| Replace unit 5’s generic question | Makes historical evidence necessary | Target frame |
| Apply findings 6 to 11 as status corrections | Preserves history while removing obsolete blockers | Named process documents |

## What is right and should be retained

- The 29 skills have clear, exclusive unit homes.
- The regional sequence and neighboring-course handoffs are coherent.
- Writing grows from short claims to research and a multi-cause argument.
- Checks use unseen sources and reserve respond days.
- Indigenous peoples appear in the present tense.
- Hard-history notes prohibit harmful role play and protect private family information.
- Informed action leaves the issue and response to students.

## What I could not judge

- The complete global plan gate, because its dependency is unavailable.
- Confirmed same-year mathematics and ELA availability, because those grade 7 frames are absent.
- Actual lesson duration, reading accessibility, source balance and assessment quality.
- Final accuracy of the 33 CE case.
- A complete Tennessee and New York comparison. Their attempted official document routes were blocked or failed.
- Whether future adaptations satisfy item-level rights requirements.

## For Cory

- **People:** Arrange the required qualified community and hard-history reading before affected materials go live. This review does not replace that work.
- No new scope, audience or spending decision is required for the repairs above.

## Outside sources and access limits

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): checked grade 7 requirements against the local anchor.
- [NCSS C3 Framework](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf): checked indicator meanings and publisher identification.
- [California content standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): checked the Han, Persia and Greek-literature candidates.
- [Investigating History grade 7 overview](https://www.doe.mass.edu/investigatinghistory/curriculum/g7-course-guidebook.pdf): inspected regional organization, pacing and grade 6 dependencies. Its different allocations are a comparison, not proof that this frame needs the same days.
- [Oak primary history sequence](https://www.thenational.academy/teachers/programmes/history-primary/units): inspected the candidate curriculum structure and younger intended level.
- [Tennessee standards review](https://www.tn.gov/sbe/committees-and-initiatives/standards-review/social-studies.html): direct access returned 403; no detailed comparison claimed.
- [New York K to 8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): direct access failed; no full comparison claimed.

**For the source list:** Add the accessible Investigating History grade 7 overview and record Oak’s current `/programmes/` route. Preserve the Tennessee and New York access limitations.

**Verdict:** Revise before unit writing. **Finding count:** 11. **Report path:** `docs/reviews/frame-world-geography-and-ancient-civilizations-ii-2026-11-13.md`, delivered here only.