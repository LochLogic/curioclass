# Second independent frame read: Music, grades K to 2

Date: 2026-11-25  
Course: `music-grades-k-to-2`  
Report returned in chat. No files changed.

## Verdict

**Needs correction before the scope and sequence is written.** The three-year structure, day totals, progression ownership and grade 3 handoff are sound, but the standards inventory and several assessment instructions can produce incomplete or misleading claims of learning. The priority is to separate kindergarten’s two creating statements correctly and make the creating checks require every owned action.

**Finding count: 9.**

## What I read and checked

- The complete [course frame](S:/CurioClass/docs/courses/music-grades-k-to-2/frame.md), its `frames.csv` entry, course-list selector and calendar rows.
- All 24 selected music progression rows for K, 1 and 2, their standards and words-file lines, and the eight receiving grade 3 rows.
- The receiving music frame’s seams, models, units and assessment provisions. There is no preceding music course.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, the shared adoption criteria and arts bar.
- Relevant foundation, production-path, glossary, calendar and decision guidance; earlier arts pre-work, progression, words-file and visual arts frame reviews.
- Relevant mathematics, ELA and physical education frame contacts.
- Outside sources linked below.

No base text is used, so a base-text source map is not applicable.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped before completion because the environment lacks the `markdown` module. Review continued. |
| `python -X utf8 scripts/frame.py check music-grades-k-to-2` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | One stale note in the physical education grades 9 to 12 frame, outside this course. |
| Ownership | All 24 selected progression rows placed once, in their own year. |
| Days | Each year has 60 unit days plus two course check days and two respond days: 64. Band total: 192. |
| Short path | Allocations total 32 sessions in each year and preserve the stated check weeks. |
| Core calendar | All six music course checks avoid the current core check weeks. |

## Findings, most serious first

### 1. Kindergarten’s documentation statement has been folded into another standard

**Severity:** serious  
**LAYER:** standard  
**REPEAT:** yes, standards-inventory errors were raised in `prework-arts-gemini-2026-11-20.md`, finding 1.  
**Confidence:** firm

**Location:** Frame “Standard,” unit 3 and “For the lead,” item 2; `mu-k-document`; both NCAS standards files; arts `STANDARD.md` section 3.2.

The frame correctly notices a possible missing `MU:Cr2.1.Kb`, but leaves it as a memory-based browser question. It is verifiable: NAfME’s kindergarten unit identifies choosing ideas as `Ka` and organizing them through notation or recording as `Kb`. New Mexico’s published standards also list them separately. [NAfME kindergarten unit, printed page 7](https://nafme.org/wp-content/uploads/2019/06/General-Music-Responding-Unit-Kindergarten.pdf), [New Mexico music standards](https://web.ped.nm.gov/wp-content/uploads/2024/12/2022_F.24-Music-Grades-K-5.pdf).

The coalition’s at-a-glance handout prints two kindergarten Cr2.1 statements with an `a` label, explaining the parsing problem. It does not justify merging their identities. [Coalition music handout, PDF page 2](https://nationalartsstandards.org/sites/default/files/2021-11/Music%20at%20a%20Glance.pdf).

**Why it matters:** The content is already taught, but the inventory understates kindergarten ownership and assigns its documentation evidence to the wrong code.

**Exact fix:**

- Add `MU:Cr2.1.Kb` to the id file.
- Split the words-file entry into:
  - `MU:Cr2.1.Ka`: “With help, show and pick favorite music ideas.”
  - `MU:Cr2.1.Kb`: “With help, keep your music ideas in picture notation or a recording.”
- Add `Kb` to `mu-k-document` and unit 3.
- Score choosing under `Ka` and the kept notation or recording under `Kb`.
- Change kindergarten’s count to **19** and the band’s to **59**, updating affected subject totals.
- Replace “For the lead,” item 2 with the verified correction and source links.

This disagrees with `arts-words-read-2026-11-20.md`’s conclusion that folding both statements into `Ka` was correct. Leave that dated report intact; correct the living files.

### 2. The creating checks allow required dimensions to go untested

**Severity:** serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment coverage is the same kind as visual arts’ second-model frame read, finding 2.  
**Confidence:** firm for grade 1; likely for the grade 2 implementation risk

**Location:** Units 7 and 11, “End-of-unit evidence”; year 2 year-end check.

Unit 7 checks `MU:Cr1.1.1b` through an idea played in twos and threes **or** happy and sad versions. The standard requires ideas in multiple tonalities **and** meters. A child can therefore pass the stated item without demonstrating one required dimension.

Unit 11 teaches rhythm and melody improvisation, but its check merely asks for “a pattern.” Its free path names claps and found drums. A writer can implement and score only rhythm, leaving the melodic action of `MU:Cr1.1.2a` untested. The year-end sample repeats that ambiguity. [Coalition music handout, PDF page 1](https://nationalartsstandards.org/sites/default/files/2021-11/Music%20at%20a%20Glance.pdf).

**Why it matters:** Correctly listed standards can still receive met marks on partial evidence.

**Exact fix:**

- Unit 7: require two brief generated ideas, one in a teacher-supported major/duple setting and one in a minor/triple setting. Record tonal and metric evidence separately. Verbal labels need not be assessed.
- Unit 11: replace “improvises a pattern” with “improvises a short rhythmic pattern and a short melodic pattern for the stated purpose.”
- Give the melodic task an explicit voice or pitched-instrument path, with a nonsolo option.
- Use the same explicit rhythmic-and-melodic wording in the year 2 year-end sample.

### 3. Mood labels are being used as evidence of tonality

**Severity:** serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely

**Location:** “Techniques that get harder”; units 7 and 9; year 2 mid-year check; corresponding progression notes.

The frame equates major with happy or bright and minor with sad or dark. Unit 9 then scores a bright-or-dark card as evidence of tonality.

These are different judgments. A child’s emotional response does not establish recognition of tonal organization. Cross-cultural experimental evidence also cautions against treating the major/happy and minor/sad association as universal. [Smit and colleagues, 2022](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0269597).

**Why it matters:** Children can learn a misleading definition, while culturally reasonable responses are marked as musical errors.

**Exact fix:** Teach major and minor through short reference patterns, echoing and comparison with a teacher-supported tonal home. Use cards labeled **major** and **minor** for that check. Keep happy, sad, bright and dark as optional descriptions of the listener’s response, never as the scoring key for tonality. Apply this distinction to the progression notes and both affected course checks.

### 4. The leave-out promise lacks a route through dependent units

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, missing-prerequisite entry routes were raised in `prework-arts-read-2026-11-19.md`, finding 24.  
**Confidence:** likely

**Location:** “Leave-out”; units 4, 8 and 12; same-year dependencies in the unit reasons.

The frame says every unit stands alone. Its concert units nevertheless require the motif, reply phrase or A-B piece made in the preceding creating unit. The retrieval provision addresses previous-year learning, not a unit omitted earlier in the same year.

**Why it matters:** A family can exercise the promised leave-out choice and leave the child without the material needed for the next unit.

**Exact fix:** Add an omission entry route to each concert unit:

- Unit 4: make a new short personal motif before revising it.
- Unit 8: make a new personal reply phrase before polishing it.
- Unit 12: make a new personal two-pattern piece before revising it.

Count this within existing application time, mark it as entry support, and retain the omitted unit’s standards as unclaimed. Add a course-wide sentence requiring each dependent unit to reteach its minimum necessary technique when its source unit was omitted.

### 5. The critique model is introduced after earlier units must use it

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Day kinds,” “Models carried,” and units 1 to 4.

Every unit must critique and revise before its check. Yet the models table says the critique protocol begins in unit 4.

**Why it matters:** The first three units require a routine whose teaching is assigned later.

**Exact fix:** Change the critique model’s first-use cell to:

> Unit 1: the teacher models describe, ask, suggest before the unit’s first critique.

List units 2 and 3 as supported reuse and unit 4 as its first use for the formally owned revising standards. Keep `mu-k-revise` and its standards in unit 4.

Also replace unit 1’s “any notation (grade 1’s picture symbols)” exclusion with:

> No notation reading in this unit; kindergarten picture documentation begins in unit 3.

### 6. Adjacent course checks are additional assessments instead of the unit assessments required by the brief

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Days,” “Scored evidence,” units 2, 3, 6, 7, 10 and 11, and “Course-level checks.”

The after-core brief says a course check immediately following a unit serves as that unit’s end-of-unit assessment when it covers the unit. This frame instead gives every unit its own check and respond day, then adds a course check sampling that same just-finished unit.

Using fresh tasks and carrying artifacts unscored avoids scoring an artifact twice. It does not resolve the mismatch with the specified assessment architecture.

**Why it matters:** Each year spends additional sessions assessing immediately repeated content and gives the scope writer conflicting instructions.

**Exact fix:** For units 2, 3, 6, 7, 10 and 11:

- Make the following course check the unit’s end-of-unit assessment.
- Include the unit’s complete per-id evidence alongside the cumulative sample.
- Use the following course respond day for both purposes.
- Reassign the displaced internal check and respond sessions to teaching, rehearsal and revision.
- State this exception in the Days bullet, affected unit rows and course-check cells.

Keep the 64-day annual totals and existing course-check weeks.

### 7. Unit 8 omits a traceable maker and place for its class song

**Severity:** minor  
**LAYER:** frame  
**REPEAT:** yes, incomplete identification of works is the same kind as the visual arts frame read’s finding 8.  
**Confidence:** firm

**Location:** Unit 8, “Processes, anchors and works.”

“Los pollitos dicen” is described only as a traditional song of Spanish-speaking countries. Chile’s education ministry publication, crediting its education museum, identifies Ismael Parraguez as its creator. [Revista de Educación: Ismael Parraguez](https://www.revistadeeducacion.cl/vida-y-obra-de-ismael-parraguez/).

**Why it matters:** The setting instruction loses a named maker and a specific cultural connection.

**Exact fix:** Replace the generic attribution with:

> “Los pollitos dicen,” a children’s song associated with Chile and attributed to Ismael Parraguez; the unit plan identifies the text and tune used and checks that edition’s rights.

Do not infer the rights of an arrangement from the song’s age.

### 8. The connecting-row concern describes wording already corrected

**Severity:** minor  
**LAYER:** process  
**REPEAT:** yes, unmarked stale notes recur in the earlier arts and visual arts frame reads.  
**Confidence:** firm

**Location:** “For the lead,” item 3; unit 6’s sensitivity note.

The current `mu-k-choose` and `mu-g1-choose` notes already connect interests, knowledge or skills to musical choices and provide a public or invented option. The frame still says those rows ask where children hear music or what they hear at home. “See Row changes” also points to no section in this frame.

**Why it matters:** The lead receives a completed repair as outstanding work.

**Exact fix:** Replace item 3 with:

> The current kindergarten and grade 1 choosing rows already connect musical choices to interests, knowledge or skills and include an invented or public option. Units 2 and 6 carry that wording forward.

Delete “see Row changes.” Replace unit 6’s reference to the row’s home-music request with the current public-or-invented choice provision.

### 9. The after-core calendar note is already outdated

**Severity:** minor  
**LAYER:** process  
**REPEAT:** yes, the visual arts second-model frame read, finding 5, identified this same stale coordination claim.  
**Confidence:** firm for the calendar read in this session

**Location:** “For the lead,” item 1.

The note says only grade 2 week 17 shares a music check week with another after-core course. Current calendar rows also show:

| Grade | Music check week | Other courses sharing it |
|---|---:|---|
| K | 19 | Theater |
| 1 | 17 and 25 | Dance |
| 2 | 17 | Dance, ELD, physical education, theater and visual arts |
| 2 | 25 | Dance |

These are after-core coordination issues, not core-calendar failures. Other workers are updating these files concurrently.

**Exact fix:** Replace the dated exclusivity claim with:

> All six music checks avoid the current core check weeks. The lead’s after-core calendar pass must resolve shared weeks across individual courses; consult the current calendar rows rather than this note for the collision list.

Keep calendar coordination with the lead.

## Lens checklist at the course-frame layer

“Met” here means specified by the frame, not demonstrated by finished lessons.

| Lens check | Result |
|---|---|
| Grade ids placed in their own band year | Met against the current inventory; finding 1 corrects that inventory |
| All four artistic processes each year | Met |
| Works span traditions and periods | Met in the planned selections |
| Technique grows across units and years | Met, subject to finding 3 |
| Schedule avoids a daily K to 8 period | Met |
| Every unit has a showing | Met |
| Technique taught before expressive application | Met |
| Response uses taught discipline words | Met |
| Works carry time, place, maker and purpose | Partial; finding 7 and later work-level identification |
| Critique follows a protocol | Specified, but first teaching is misplaced; finding 5 |
| Revision follows feedback | Met |
| Assessment includes making, performing and response | Met in form; coverage needs finding 2 |
| Questions and assessments are original | No copied cornerstone task apparent |
| Set-up and clean-up included | Met in the stated minutes; actual group throughput remains untested |
| Equipment has a free alternative | Met generally; melodic assessment needs an explicit pitched path |
| Space and equipment hazards named | Met as planning provisions; safety read still owed |
| No forced solo | Met |
| Responding process distinguished from respond days | Met |
| Software does not judge finished performance | Met |
| Arts disciplines remain distinct | Met |
| Music does not reteach fractions or duplicate PE dance | Met |

## What is right and should not be touched

- Four units per year, with each year complete on its own.
- The consistent 64-session structure and arithmetically coherent 32-session path.
- All 24 progression rows placed once, with a matching grade 3 handoff.
- Picture notation and beat counts before fractional note values.
- Original music-making, revision, small-group performance, self-assessment and kept work.
- Free materials, nonsolo participation and invented or public alternatives to personal disclosure.
- The stated weekly-time gap. The source confirms a 90-minute K to 2 recommendation; the frame correctly reports its 80-minute and 40-minute provisions. [NAfME opportunity-to-learn standards, printed page 9](https://nafme.org/wp-content/uploads/2020/08/NAfME-Opportunity-to-Learn-Standards-2020.pdf).

## Settled by the expert

These are recommendations for the caller to apply, not edits made in this read.

| Choice | Reason | File touched |
|---|---|---|
| Separate kindergarten choosing and documentation evidence under `Ka` and `Kb` | Both actions already exist in unit 3 | Standards files, progression, arts standard and frame |
| Grade 1 creating evidence must include multiple tonalities and meters | An either/or item permits partial coverage | Frame unit 7 |
| Name rhythmic and melodic improvisation separately | Prevents a percussion-only pass | Frame unit 11 and year-end check |
| Score tonality separately from mood | Mood words are not a tonality key | Frame and affected progression notes |
| Teach the critique routine in unit 1 | It is required before unit 4 | Frame models table and unit 1 |
| Retain existing totals and core-safe course-check weeks | The arithmetic and core placement work | Frame |

## For Cory

- **Money only:** the proposed $75 annual class ceiling remains a spending decision. The frame’s provisional costs are $55, $20 and $20 across the three years, with a free path retained. This read did not price or authorize purchases.

No new scope, audience or outside-person decision is needed for these corrections.

## Limits and source follow-up

This is a frame review, not certification of lessons, assessment guides or classroom feasibility. Recording rights, exact editions, living status, pronunciation guidance, safety claims and supply prices remain to be checked at their assigned stages. The frame’s safety rules remain **from memory** until its specified safety read verifies them.

Two older NAfME standards PDF addresses were inaccessible through the web tool. The coalition handout, NAfME kindergarten unit and state standards sources supplied the needed evidence without an alternate fetch of a blocked page.

For the source list, retain the linked NAfME kindergarten unit to resolve the Cr2.1 coding issue and the linked experimental study to distinguish tonality from emotional response. The experiment is not evidence that this curriculum will produce particular learning outcomes.

Prior session memory supplied only general review prompts about totals, complete standard actions and prerequisites. All findings above rest on the current repository read or linked sources.

