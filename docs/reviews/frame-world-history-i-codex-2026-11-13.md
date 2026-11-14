# Independent frame review: World History I

**Intended report path:** `docs/reviews/frame-world-history-i-2026-11-13.md`  
**Delivery:** Markdown supplied here. No report or other file was written.

## Verdict

The frame has a coherent structure, complete skill placement and a workable overall day budget, but it needs revision before it is ready to build from. The largest risk is mistaking standard-code coverage for full teaching: cotton technologies are missing, and the plague treatment omits the anchor’s recurring outbreaks beyond the 1300s. The most useful change is to repair those content requirements while restoring counterclaim practice earlier in the year.

**Finding count: 14**, comprising 7 curriculum findings and 7 stale-status findings.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, APPROACH, relevant ROADMAP and BASELINE sections, section 1 of ADOPTION-BAR-SUBJECTS, and the social studies STANDARD.
- The complete World History I frame, its `frames.csv` row, all 37 grade 9 social studies progression rows, and relevant incoming and outgoing progression rows.
- The preceding grade 8 civics frame, the grade 7 world-history handoff frame, and the following World History II frame.
- Massachusetts WHI content requirements, including lettered parts, and the C3 indicators owned by grade 9.
- Relevant ELA, mathematics and science progression rows.
- BASE-TEXTS, the social studies source-scouting report, and the locally held ETSU textbook’s copyright page and contents.
- Earlier social studies progression reviews, their fix reports, cross-subject reviews and fixes, and the kindergarten and grade 1 frame reviews.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: the active Python environment lacks `markdown`. This is an environment failure, not a plan verdict. |
| `python -B -X utf8 scripts/frame.py check world-history-i` | 0 failures |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures |
| `python -B -X utf8 scripts/stale.py check` | 19 files checked, 0 failures |

The standalone frame and progression checks establish their own results. They do not substitute for the unfinished full plan gate.

## Findings, most serious first

### 1. The cotton row teaches exports without teaching textile technologies

**Severity:** serious. **Confidence:** firm. **LAYER:** standard. **REPEAT:** yes, the earlier progression review found incomplete bundled Massachusetts standards.

**Location:** frame unit 5; `data/progressions/social-studies.csv`, `wh1-farming-and-cotton`.

Both documents explain cotton’s economic importance and exports, but neither specifies the technologies that made production possible. WHI.T4.4 requires that technological component as well as trade. The omission would produce days about demand and exports that leave part of the standard untaught. [Massachusetts framework, PDF page 144, printed page 144](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Exact fix:** Add to the progression notes and unit 5’s learning description:

> Explain how cotton processing, spinning, weaving, printing and dyeing supported India’s medieval textile production, and connect improvements in production to cloth exports to Africa and Europe.

Use a production-sequence diagram and evidence from surviving textiles. Keep this within unit 5’s 11 days by replacing part of the generic trade survey, rather than adding another content strand.

### 2. The plague treatment stops before part of its anchor requirement

**Severity:** serious. **Confidence:** firm. **LAYER:** standard. **REPEAT:** yes, incomplete standard coverage is an established earlier finding type.

**Location:** frame unit 6; `wh1-black-death`; `data/standards/ma-hss-2018.txt`, MA.WHI.T3.9.

The frame closes this unit at 1400, and the progression centers the 1300s. The official anchor also requires repeated spread and mortality effects into the fifteenth century; the repository paraphrase loses that detail. [Massachusetts framework, PDF page 144, printed page 144](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** A writer following the repository record would reasonably teach one fourteenth-century outbreak and regard the standard as complete.

**Exact fix:** Restore repeated outbreaks through the 1400s in the standards paraphrase, progression notes and unit 6 description. Retain 1347 to 1351 as the first major European case, then compare later outbreaks using dated evidence and explicit uncertainty.

Change the unit’s stated span to **800 to 1500**, with a note that its slavery comparison deliberately ranges from the 400s to the 1700s. This also makes its early Mediterranean coexistence material an acknowledged chronological return.

### 3. Argument instruction retreats from grade 8 and leaves a reciprocal dependency unresolved

**Severity:** moderate. **Confidence:** likely. **LAYER:** frame. **REPEAT:** yes, earlier cross-subject reads found mistimed reciprocal dependencies.

**Location:** Inquiry arc; unit 10; Models carried; ELA availability table; For the lead item 2.

The grade 8 frame explicitly teaches answering counterclaims and uses that work in its research argument. Grade 9 nevertheless specifies claim paragraphs only through unit 9 and says the counterclaim is taught late. Meanwhile, ELA 9’s argument row leans on `wh1-historical-argument`, but this frame asks ELA to teach argument before history reaches that row.

**Why it matters:** Students lose sustained practice in an inherited skill, and the scheduling instruction does not resolve the dependency recorded in the data. Unit 10 then carries four substantive content rows, the full argument, explanation and action cycle in 18 days.

**Exact fix:**

- Unit 1 retrieves a brief claim, evidence, reasoning and counterclaim response.
- Units 3 and 6 each include a short argument that answers one counterclaim.
- Unit 10 retains ownership of the full high school argument, evidence revision and explanation.
- In ELA’s `e9-w-argument` lean, identify the earlier history practice as available preparation and unit 10 as later transfer.
- Replace For the lead item 2’s proposed need to split the progression row with this distributed-practice arrangement.

No standard needs to move between units. The C3 framework supports distinguishing a developed argument from a sourced explanation, with evidentiary limitations addressed in both. [C3 framework, printed page 59](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 4. The review flags omit two of the course’s hardest units

**Severity:** moderate. **Confidence:** firm. **LAYER:** frame. **REPEAT:** new.

**Location:** unit 6, unit 9 and For the lead item 4.

The people note lists units 2, 4 and 8. Unit 6 contains slavery, religious massacres and the murder of Jewish communities during plague outbreaks. Unit 9 includes the Banda conquest. Neither unit explicitly carries the sensitivity and qualified-reader requirement that the frame assigns elsewhere.

**Why it matters:** A later production handoff could treat the list as the complete review requirement and miss material the frame itself identifies as especially difficult.

**Exact fix:** Add explicit sensitivity-read flags to units 6 and 9. Rewrite the people note:

> Qualified review must cover the course’s Native, religious and hard-history material, including units 2, 3, 4, 6, 7, 8 and 9. Units 6 and 9 are included explicitly because of slavery, massacres and the Banda conquest. The lead records coverage before the affected units ship.

This applies the existing FOUNDATION requirement. It does not authorize recruitment or spending.

### 5. Some check-set additions have unsupported attributions

**Severity:** moderate. **Confidence:** firm. **LAYER:** frame. **REPEAT:** new.

**Location:** Check set adds, especially units 1, 6 and 10; For the lead item 5.

The frame candidly identifies its additions as memory-derived candidates. Fresh checking exposes incorrect or unsupported source labels:

- California grade 7 and New York 9.6 do not name the Hundred Years’ War and Joan of Arc as claimed.
- New York 9.4 supports Afro-Eurasian trade networks, but does not name Polynesian voyaging.
- The current college-level world-history framework does not name Pugachev as the frame claims.

A genuine source exists for the Hundred Years’ War and Joan of Arc: Tennessee 2024, **7.38**. [Tennessee standards](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf).

**Why it matters:** A named state or framework is being used as evidence before the claimed addition has been verified.

**Exact fix:**

- Attribute the Hundred Years’ War and Joan of Arc candidate to Tennessee 7.38.
- Separate unit 1’s candidates: Srivijaya has support in the college-level framework, topic 1.3; the Indian Ocean network has support in New York 9.4.
- Label Polynesian voyaging and Pugachev **writer-proposed examples, source comparison pending**, unless an exact supporting passage is supplied.
- Record edition and section for every retained attribution.

The supporting documents are the [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf), [New York framework](https://www.nysed.gov/sites/default/files/programs/standards-instruction/framework-9-12-with-2017-updates.pdf), and [current college-level world-history framework](https://apcentral.collegeboard.org/media/pdf/ap-world-history-modern-course-and-exam-description.pdf).

### 6. The action route assumes that every student has a school intermediary

**Severity:** moderate. **Confidence:** firm. **LAYER:** frame. **REPEAT:** new.

**Location:** Informed action; unit 10 teacher note; `wh1-historical-argument`.

Every proposed correction goes “through the school.” FOUNDATION names a parent teaching one child at home as an audience, and the frame supplies a solo route elsewhere, but this action has no corresponding home route.

**Why it matters:** A home learner cannot follow the stated procedure.

**Exact fix:** Replace the intermediary wording throughout with:

> Any external communication goes through the teacher or parent, using adult contact details. Students may instead prepare an evidence-based corrected label or annotated account and share it with a chosen audience through that adult. Contacting an institution is optional.

Keep the student’s choice of issue and whether to communicate externally.

### 7. The ELA handoff misidentifies the texts grade 9 teaches

**Severity:** minor. **Confidence:** firm. **LAYER:** frame. **REPEAT:** yes, earlier cross-subject reviews found mismatches between a named lean and its actual task.

**Location:** ELA availability table, `wh1-constitutional-democracy`.

The frame says `e9-ri-purpose-rhetoric` reads two short founding documents. The actual ELA row names Washington’s Farewell Address and the Gettysburg Address. Those texts do not establish prior study of the Constitution and Bill of Rights required here.

**Why it matters:** A writer could omit necessary retrieval or explanation on the assumption that ELA supplies it.

**Exact fix:** Replace that availability cell with:

> ELA 9 reads Washington’s Farewell Address and the Gettysburg Address for rhetoric. This history row retrieves the Constitution and Bill of Rights from grade 8 civics and teaches their world-history significance directly. It does not depend on ELA 9 having taught those documents.

### Stale-status findings

Each finding below is **minor**, **firm**, **LAYER process**, **REPEAT yes**, following the stale-status finding type already recorded in earlier frame and progression reviews.

Preserve dated review evidence. Add a dated resolution or replace the active status sentence, rather than making an earlier reviewer appear to have known a later development.

| # | Location and what is wrong | Why it matters | Exact replacement or resolution |
|---|---|---|---|
| **8** | `progression-social-studies-codex-2026-11-13.md:73` says candidate partial bases are not loaded. ETSU and other approved partial sources are now present and recorded in BASE-TEXTS. | It sends a reader back to completed acquisition work. | “Update, 2026-11-13: approved partial sources are now recorded in BASE-TEXTS.md; ETSU is loaded. No whole-course social studies base text has been adopted.” |
| **9** | The same report, line 254, says the other subject progression files are absent. Math, ELA and science progression files now exist. | It presents an obsolete verification barrier as current. | “Update, 2026-11-13: the other three progression files now exist. Subsequent cross-subject reviews and their fix report address ownership and readiness; teaching order within a year remains a frame check.” |
| **10** | `progression-social-studies-fixes-2026-11-13.md:43` says cross-subject checking waits on those progressions. The subsequent cross-subject pass has occurred. | The fix report leaves completed follow-up work apparently pending. | “Completed by progression-cross-fixes-2026-11-13.md. Same-year availability must still be confirmed in the course frames.” |
| **11** | `social-studies-open-material-2026-11-13.md`, Traps, Recommendation and Open items, still asks Cory to decide on OGL, the retired-book clause and proposed partial bases. BASE-TEXTS records those decisions and loading status. | It reopens settled decisions and conflicts with the operative source record. | Add: “Decisions applied, 2026-11-13: use BASE-TEXTS.md for approved partial sources and their limits. OGL v3.0 was accepted; Cory’s retired-book decision is recorded there. Oak material is obtained per unit. Item-specific rights and content reviews remain required.” Remove those decisions from Open items. |
| **12** | The source-scouting report’s short answer and recommendation still say science goes second because social studies lacks a full base text. | It gives the wrong production order. | “Superseded, 2026-11-13: PRODUCTION-PATH and BASELINE rule 25 place social studies first and mathematics last for the subject-by-subject planning stage. Availability of a complete base text no longer determines that order.” |
| **13** | ROADMAP, “Subjects outside the core,” says the social studies content standard is open for Cory to decide. STANDARD records the decision and completed anchor preparation. | It falsely identifies a prerequisite as unresolved. | “Social studies uses C3 skills and Massachusetts 2018 content, with the course order, check set and exceptions recorded in docs/courses/social-studies/STANDARD.md. That content-standard decision is complete.” |
| **14** | APPROACH’s introduction says science and ELA subject pages follow when their courses open. `docs/APPROACH-ELA.md` already exists. | It hides an existing governing page from readers following the shared approach. | “Subject pages currently include APPROACH-MATH.md and APPROACH-ELA.md. Science and social studies subject pages remain to be written.” |

## Checked and found right

### Ownership and standards placement

All **37 grade 9 skills** appear in exactly one unit. No foreign-grade skill appears in the Skills column. The rows name **49 distinct Massachusetts codes**, including the twelve kingdom and empire options, and **25 C3 indicators**.

The missing-content findings above concern what those codes require, not missing identifiers. The recorded division of MA.WHI.T5.3 between colonial consequences and the Atlantic slave trade is now explicit and should remain.

The frame’s distinction between a survey and one case studied in depth is useful. Its complete solo route should remain.

### Units, order and days

The regional and thematic returns have stated reasons. Forms of power precede their comparisons, medieval knowledge precedes the Renaissance, and the worldwide slavery comparison precedes the Atlantic system.

| Unit | Skills | Days | Assessment of allocation |
|---|---:|---:|---|
| 1 | 5 | 15 | Reasonable for the introductory inquiry and source routines |
| 2 | 4 | 15 | Workable with brief retrieval and one empire in depth |
| 3 | 4 | 16 | Reasonable for content plus interpretation work |
| 4 | 3 | 14 | Workable if the survey does not become several equal-depth studies |
| 5 | 3 | 11 | Tight; teach the missing technology within the existing allocation |
| 6 | 3 | 15 | Reasonable after correcting the stated historical span |
| 7 | 4 | 16 | Workable with disciplined limits on candidate additions |
| 8 | 3 | 16 | Substantial time appropriately assigned to difficult content |
| 9 | 3 | 12 | Workable for a focused science case and short account |
| 10 | 5 | 18 | Crowded if argument instruction begins here; finding 3 reduces that risk |
| Course checks and respond days | | 12 | Explicitly reserved |
| **Total** | **37** | **160** | Fits 32 five-day teaching weeks |

No unit is demonstrably far over or under its share at frame depth. Feasibility remains provisional because period length and actual source-reading demands are not fixed.

### Seams and cross-subject dependencies

The chronological handoff is sound: grade 7 ends near 500, grade 8 supplies civics, and this course deliberately retrieves world history after that gap. World History II explicitly reopens earlier absolutism and revolution material before advancing into the nineteenth century. Its opening overlap is explained.

The earlier mathematics and science leans resolve to actual owning rows in grades 3, 6, 7 and 8. The former dependence on later high school science has been repaired.

No ELA 9 frame exists yet. Consequently, the proposed ELA dates and the separation of difficult texts and major writing deadlines remain coordination requests, not verified availability. Findings 3 and 7 address specific faults already visible without that frame.

### Partial source and source map

There is **no whole-course base text** and no `data/plans/world-history-i/source-map.csv`.

ETSU is an approved partial source, not a lesson-based course adopted end to end. Its contents support the frame’s broad assignments: chapters 1 and 4 for unit 7, chapter 2 for unit 8, chapters 3 and 5 for unit 9, and chapter 5 for unit 10. The different chapter order follows the frame’s stated historical reasons.

A complete base-lesson accounting is therefore not applicable here. Passage selection, omissions, exact day fit and individual image rights remain unverified until the scope and sequence selects material. The frame correctly excludes non-commercial and reference sources from adaptation. The local copyright page confirms the original-content licence and separate image-rights warning. [ETSU publisher record](https://dc.etsu.edu/etsu-oer/13/).

## Lens checklist: course frame layer

“Met” means the error named by the lens was not found.

| Lens line | Result |
|---|---|
| An anchor standard in the Massachusetts topic range has no unit | **Met for placement.** Full teaching remains incomplete in findings 1 and 2. |
| The replaced grade 3 year or grade 8 own-state method retains Massachusetts-only content | **Not applicable** to this course. |
| No unit lists check-set additions, or an addition has no recorded source | **Missed in part.** Every unit lists candidates, but several source attributions fail verification, finding 5. |

## Settled by the expert

These are recommendations for the caller to apply. No file was edited.

| Choice | Reason | Files touched |
|---|---|---|
| Teach cotton through a production sequence linked to exports | Supplies the missing technological component without enlarging the unit | World History I frame; social studies progression |
| Include recurring plague through the 1400s | Restores the anchor’s temporal requirement | Frame; progression; Massachusetts paraphrase |
| Retrieve counterclaim responses in unit 1 and practise them in units 3 and 6 | Preserves the grade 8 handoff while keeping full ownership in unit 10 | Frame; ELA lean wording |
| Keep the existing 160-day budget provisionally | No demonstrated need for a larger year at frame depth | Frame |
| Use a teacher or parent as the action intermediary | Makes the existing audience promise executable | Frame; progression |
| Correct verified candidate attributions and label unsupported examples honestly | Keeps source comparison reviewable | Frame |
| Resolve stale status notes with dated updates | Preserves review history while exposing current state | Files named in findings 8 to 14 |

## For Cory

- **People:** arrange qualified coverage of the Native, religious and hard-history material, including the omitted units identified in finding 4. This review authorizes no outreach or spending.
- **Scope:** no change to course boundaries, grade placement or the 160-day year is recommended.

## Limits and sources

This is a frame review, not certification of unwritten lessons, assessments, selected excerpts or historical sensitivity. The full plan gate still needs to run in an environment with its existing dependencies available. The source-map and same-year ELA limits are stated above.

Sources opened for this review:

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): full WHI requirements and chronological boundaries.
- [C3 framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned inquiry, geography, history and argument indicators.
- [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): check-set attribution verification.
- [Tennessee 2024 standards](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf): verified replacement attribution, especially 7.38.
- [New York framework, with 2017 updates](https://www.nysed.gov/sites/default/files/programs/standards-instruction/framework-9-12-with-2017-updates.pdf): trade-network and medieval-history comparisons.
- [College-level world-history framework, effective fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-world-history-modern-course-and-exam-description.pdf): candidate-example and sequencing checks.
- [ETSU textbook record](https://dc.etsu.edu/etsu-oer/13/): publisher identification. Automated full-text retrieval was blocked; the locally held PDF supplied the copyright and contents checks.

**For the source list:** record the working New York framework address above and the verified Tennessee 7.38 pointer.

No substantive curriculum finding rests on memory. Prior session memory was used only for the cold-review scope convention.

**Final verdict:** revise before building from this frame. **Finding count:** 14. **Report path:** `docs/reviews/frame-world-history-i-2026-11-13.md`, supplied here, not written.

