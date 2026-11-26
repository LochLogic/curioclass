# Second independent frame read: Music, grades 6 to 8

Date: 2026-11-25  
Course: `music-grades-6-to-8`  
Report returned in chat. No files changed.

## Verdict

**Needs correction before the scope and sequence is written.** Grade ownership, unit order, annual totals and adjacent-course handoffs are sound, but several teaching and assessment instructions permit partial standards coverage. The priority is to restore the missing actions before those instructions become day plans.

**Finding count: 11.**

## What I read and checked

- The complete course frame, its course-list selector, `frames.csv` entry and all 24 calendar rows.
- All 24 selected music progression rows, neighboring grade 5 and Level 1 rows, and the 63 owned standards’ words-file entries.
- The preceding and following music frames’ relevant units, models, seams and assessment provisions.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the arts adoption criteria.
- Relevant foundation, approach, production-path, baseline, calendar, decision, source and earlier review guidance.
- The cited grade 6 and grade 8 ELA units and their calendar placement.
- The outside sources linked below.

There is no base text or source map to audit.

| Check | Result |
|---|---|
| Course-filtered `scripts/plan.py check music-grades-6-to-8` | Failed because day-level plan files do not exist yet; frame review continued. |
| `scripts/frame.py check music-grades-6-to-8` | **0 failures.** |
| `scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale prose remains. |
| Skill ownership | All 24 selected rows appear exactly once, in their own grade year. |
| Standards inventory | 21 distinct ids per year, 63 across the band. Full actions need the corrections below. |
| Days | Each year: 60 unit days, two course-check days and two respond days, totaling 64. |
| Short path | Each year totals 32 sessions; its check weeks are internally consistent. |
| Calendar | Mid-year checks in week 19 avoid current core-check weeks. Week 32 is permitted for finals. Short-path checks in weeks 17 and 31 also avoid core checks. |
| Cross-subject timing | Both ELA contacts match their frames and calendar rows. Their explicit fallbacks handle overlapping or later instruction. |

The check commands used `python -B -X utf8` to prevent bytecode-cache writes.

## Findings, most serious first

### 1. Creating evidence omits required dimensions

**Severity:** serious  
**LAYER:** frame, progression, standard  
**REPEAT:** yes, incomplete creating evidence recurs in the music 3 to 5 second read, finding 1.  
**Confidence:** firm

**Location:** Units 3, 4, 7, 8, 11 and 12; corresponding invent, document and revise rows and words lines.

Grade 6 generation requires both AB and ABA work. Expressive intent continues through the later creating standards, and finished compositions require craftsmanship and originality. The frame’s evidence does not consistently secure these dimensions. [National music handout, PDF pages 1 to 3](https://nationalartsstandards.org/sites/default/files/2021-11/Music%20at%20a%20Glance.pdf).

**Why it matters:** A correctly labeled score can receive credit without demonstrating the complete creating requirement.

**Exact fix:**

| Location | Correction |
|---|---|
| Unit 3, `MU:Cr1.1.6a` | Keep brief generated examples in **both AB and ABA**. The developed final composition may use either form under `Cr2.1.6a`. Correct the invent row and words line accordingly. |
| Units 7 and 11, `Cr1.1` and `Cr2.1a` | Require a stated expressive aim and mark how the musical decisions convey it, alongside the existing form and structural evidence. Restore this requirement in the affected progression notes and words lines. |
| Units 4, 8 and 12, `Cr3.2a` | Score the finished music for deliberate construction, an identifiable student contribution and communication of its aim. Retain each grade’s existing structural requirements. Naming techniques on the program alone is insufficient. |

Keep ownership in the existing units.

### 2. Performance selection is reduced to general-purpose listening choices

**Severity:** serious  
**LAYER:** frame, progression, standard  
**REPEAT:** yes, partial standard coverage is the same kind as the music 3 to 5 second read, finding 1.  
**Confidence:** firm

**Location:** Units 2, 6 and 10, `MU:Pr4.1.6a`, `.7a` and `.8a`.

Unit 2’s examples include background listening without explicitly selecting repertoire to perform. Units 6 and 10 omit expressive qualities and technical challenges from their required program evidence. These are distinct demands in the national standards. [Official national standards handbook, Performing](https://www.nationalartsstandards.org/index.php/customize-handbook?discipline=Music%2CMusic+%28PK-8%29%2CTheatre&display_options=eq_el%2Cprocess_components&grade_level=6+-+8%2C6th%2C7th%2C8th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting).

**Why it matters:** Students can pass selection without considering what performers must accomplish.

**Exact fix:** Label the `Pr4.1` product a **performance program**. For grades 7 and 8, require each selection’s expressive quality, technical challenge and reason for inclusion. Grade 7 discusses these using shared criteria; grade 8 explains them using personal criteria. Preserve listening choices separately under `Re7.1`, and correct the corresponding progression notes and words lines.

### 3. Interpretation and connecting checks accept incomplete responses

**Severity:** serious  
**LAYER:** frame, progression, standard  
**REPEAT:** yes, incomplete response evidence recurs in the music 3 to 5 second read, finding 2.  
**Confidence:** firm

**Location:** Units 1, 2, 5, 6, 9 and 10; associated course-check samples.

The `Re8.1` checks ask how choices carry intent but do not require genre and cultural or historical context. The connecting evidence similarly accepts one choice or one relationship without securing the broader action. Compare the [official Responding and Connecting requirements](https://www.nationalartsstandards.org/index.php/customize-handbook?discipline=Music%2CMusic+%28PK-8%29%2CTheatre&display_options=eq_el%2Cprocess_components&grade_level=6+-+8%2C6th%2C7th%2C8th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting).

**Why it matters:** Generic statements can earn credit while omitting the connection being claimed.

**Exact fix:**

- Add a contextual clue and its musical consequence to every `Re8.1` prompt, including cumulative samples.
- For `Cn10.1`, retain brief evidence about choices in creating, performing and responding. A short created phrase can sit within the existing application time in units 2, 6 and 10.
- For `Cn11.1`, replace the single either/or tie with a compact connection map covering another art, another subject, context and daily life.

Update the affected progression notes and words lines to preserve these distinctions.

### 4. The no-device alternative does not preserve the listening work

**Severity:** serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely

**Location:** “Devices,” lines 156 to 163; listening and interpretation units.

The fallback describes the studied work on a card and substitutes a teacher-performed original for unseen recordings. A description cannot supply the sound students must analyze. One unspecified tune also cannot replace contrasting interpretations or a program.

**Why it matters:** The promised no-device route can become reading about music while claiming listening outcomes.

**Exact fix:** State that descriptions support contextual study but never replace audible evidence. Require each no-device listening task to provide performable printed exemplars, preparation guidance and the necessary contrasting versions or program excerpts. Its check must preserve the same musical comparison and contextual demand as the playback version. Where an equivalent live task cannot be provided, name the affected ids as unclaimed until suitable listening access is available.

### 5. The Ives public-domain claim and federal-recording shortcut are unsupported

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, the earlier all-band music read raised the Ives score in finding 5.  
**Confidence:** firm that the blanket claims need correction

**Location:** Unit 7; “Base text,” lines 59 to 65.

Unit 7 calls Ives’s *Variations on “America”* a public-domain score. A federal band’s published excerpt carries 1949, 1964 and 1968 copyright notices. The Marine Band’s own recording notes identify protected arrangements used by permission. Federal performance alone therefore does not establish that every underlying musical component is freely reusable. [Published score excerpt](https://www.music.af.mil/Portals/33/Bands/USAF%20AcademyBand/announcement%20letters%20and%20requirements/Trumpet%2010_24-27%202023%20Full%20Package_Final_1_1.pdf?ver=xoQggX3RnoKvPrFBsV3f7w%3D%3D), [Marine Band recording notes](https://www.marineband.marines.mil/Portals/175/Docs/Audio/Educational_Series/charles_ives/charles_ives_america.pdf).

**Why it matters:** A writer may copy material on an incorrect rights assumption.

**Exact fix:** Mark Ives “described and linked; score reuse not established.” Replace the federal-recording shortcut with item-level checks covering the recording, composition and arrangement. Do not copy or embed any component without the required verified rights line.

### 6. Important work selections remain placeholders

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, the music 3 to 5 second read raised unfinished anchors in finding 8.  
**Confidence:** firm

**Location:** Works cells throughout, especially units 1, 2, 4, 5, 8, 9, 10, 11 and 12; “Leave-out.”

Several entries name only an artist, tradition or future selection. The frame contains no work-source URLs. It also says no unit except unit 4 studies sacred or ceremonial work, although unit 8 names ritual roots and unit 12’s performance remains unselected. Brazil’s heritage agency describes samba de roda in both everyday and religious settings. [Brazilian heritage record](https://bcr.iphan.gov.br/bens-culturais/samba-de-roda-do-reconcavo-baiano/).

**Why it matters:** Musical suitability, context and sensitivity cannot be checked against an unspecified performance.

**Exact fix:** Before scope writing, replace every placeholder with a title or identified performance, maker or ensemble, date, primary-source link and the particular feature studied. Replace the blanket sacred-content assurance with work-specific classifications, explicitly covering units 4, 8 and 12. Keep edition-specific rights checks at unit-plan stage.

### 7. Adjacent mid-year checks duplicate unit assessment windows

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 finding 6 and music 3 to 5 finding 3.  
**Confidence:** firm

**Location:** Units 2, 6 and 10; “Days”; mid-year course-check rows.

Each unit has internal check days and a respond day, immediately followed by a course check sampling the same unit. Carrying an artifact unscored prevents duplicate artifact scoring, but leaves consecutive assessment windows. The after-core brief says the adjacent course check serves as the unit assessment when it covers that unit.

**Why it matters:** The scope writer receives conflicting assessment instructions and loses practice time.

**Exact fix:** Make each mid-year course check the preceding unit’s end-of-unit assessment. Include that unit’s complete per-id evidence alongside the cumulative sample, using kept performance and program evidence from preceding application days where necessary. Use the course respond day for both purposes, and convert displaced internal assessment time into rehearsal, revision and supported practice. Preserve annual totals and check weeks.

### 8. Leave-out routes do not make dependent units stand alone

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 finding 4 and music 3 to 5 finding 5.  
**Confidence:** firm

**Location:** “Leave-out”; units 2 to 4, 6 to 8 and 10 to 12.

Interpretation units depend on earlier performance pieces, composing units depend on earlier notation instruction, and concert units require the preceding composition. The retrieval provision addresses previous-year learning rather than an omitted same-year unit.

**Why it matters:** Exercising the promised leave-out choice can remove the material needed for the next unit.

**Exact fix:** Add three entry routes within existing application time:

- Interpretation: a neutral Curio Class original with its minimum score-reading demonstration.
- Composing: a short notation demonstration and fresh personal idea.
- Concert: a newly made, brief personal composition with a draft, critique and revision.

Keep omitted units’ ids unclaimed. State these routes in the Leave-out bullet and affected unit rows.

### 9. Two models are retrieved after their first use

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 finding 5 and music 3 to 5 finding 6.  
**Confidence:** firm

**Location:** “Models carried,” lines 279 and 283.

The listening log’s first-use cell names unit 2, while unit 1 already uses it. The practice plan’s first-use cell names unit 4, while unit 2 rehearses with it.

**Why it matters:** Students entering without the optional preceding course can meet a required routine before its entry support.

**Exact fix:** Set listening-log first retrieval to unit 1’s first listening study. Set practice-plan first retrieval to unit 2’s first rehearsal. Retain unit 4 as the point that adds the owned readiness decision. Include the existing entry reteach at those earlier uses.

### 10. Two-piece checks conflict with the performance-day limit

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Scored evidence,” lines 109 to 115; units 6 and 10.

The general rule allows at most one full performance on an end day. Both units require two contrasting pieces on their single performance check day.

**Why it matters:** Writers must silently reinterpret either the evidence requirement or the session limit.

**Exact fix:** Specify one assessed set containing two short contrasting excerpts, with each student’s contribution identifiable. Cap the complete group turn, including unit 10’s explanation, at the stated four minutes. Retain fuller performances during rehearsal or showing time. If full pieces are intended at the check, allocate separate existing sessions and revise the general rule explicitly.

### 11. Unmarked notes describe completed or nonexistent work

**Severity:** minor  
**LAYER:** process  
**REPEAT:** yes, the earlier all-band music read, finding 1, and music 3 to 5 finding 9.  
**Confidence:** firm for the repository snapshot read

**Locations and exact fixes:**

| Location | Problem | Exact fix |
|---|---|---|
| Frame, For the lead, item 3 | Says the three choose rows lack an invented or public option. All three now contain it. “See Row changes” has no target. | Replace with: “The invented or public option is present in all three choose rows and units 2, 6 and 10.” |
| Frame, For the lead, item 2 | Says `stale.py` flags the preceding music frame. The check reports zero failures. | Delete that status claim; retain the verified seam statement. |
| Frame, For the lead, item 4 | Leaves national wording verification unresolved. | Record that `MU:Pr6.1.8a` includes culturally authentic practices, confirmed from the national source in this read. Retain the work-specific source check. |
| Base-text range summary | Includes Egypt although the current selections no longer identify an Egyptian work. | Remove Egypt from the summary. |
| `ADOPTION-BAR-SUBJECTS.md`, arts pre-work row | Still lists L83 and loading the high school strand ids as owed. | State that the inventory check and 63-id load were completed, matching `STANDARD.md` and the loaded files. |

These corrections belong in living documents. Leave dated review records unchanged.

## Lens checklist at the course-frame layer

“Met” means specified in the frame, rather than demonstrated by finished lessons.

| Lens check | Result |
|---|---|
| Grade standards remain in their own band year | Met |
| All four artistic processes appear each year | Met |
| Technique develops across units and years | Met in design; finding 1 restores missing demands |
| Discipline words support making and responding | Met |
| Students choose, make and show work | Met |
| Critique has a protocol and leads to revision | Met |
| Works span cultures, periods and living makers | Met in intended range; selections need finding 6 |
| Works carry maker, time, place and purpose | Partial; finding 6 |
| Assessment includes performance, response, self-assessment and kept work | Met in form; coverage and scheduling need findings 1 to 3, 7 and 10 |
| Schedule avoids a daily arts period | Met |
| Equipment has free alternatives | Specified; listening equivalence needs finding 4 |
| Set-up and clean-up are counted | Met in stated budgets |
| Hazards and controls are named | Met as planning provisions; safety reads remain owed |
| No forced solo | Met |
| Artistic responding is distinguished from respond days | Met |
| Software supports rather than judges finished performance | Met |
| Arts disciplines remain distinct | Met |
| Music avoids teaching fractions ahead of math | Met |
| Copied cornerstone assessments or questions | None apparent |

## What is right and should not be touched

- Four units per year, with complete grade ownership and coherent reading, interpretation, composing and concert threads.
- The defensible 18, 18, 12 and 12-day allocation.
- Matching grade 5 and Level 1 handoffs, including the high school bridge.
- Both ELA fallbacks and the use of musical beat counts without a new fraction dependency.
- Nonsolo participation, changing-voice options, critique, revision and portfolio growth.
- The honest weekly-time gap: the course provides 80 minutes, or 40 on its shorter path, against the association’s 90-minute recommendation. [Opportunity-to-learn standards, printed page 13](https://nafme.org/wp-content/uploads/2020/08/NAfME-Opportunity-to-Learn-Standards-2020.pdf).

The earlier all-band music read correctly recognized complete id placement. Findings 1 to 3 qualify its positive assessment of per-id evidence: listing an item does not establish that the item checks the full action.

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Keep the year structure, unit order and day totals | Ownership, sequence and arithmetic hold | Course frame |
| Generate both AB and ABA examples, then develop either | Separates generation breadth from the final-product choice | Frame, progression, words file |
| Keep corrected standards in their existing units | Missing parts can be restored without moving ownership | Same |
| Retrieve listening-log and practice-plan earlier | Both are already used earlier | Frame models table |
| Use two short excerpts for the contrasting performance check | Preserves comparison within the existing session budget | Units 6 and 10 |
| Keep culturally authentic practice in grade 8 | National wording is verified; implementation needs a selected community source | Unit 12 |
| Treat Ives as description and link until reuse is verified | Present evidence does not establish unrestricted score reuse | Unit 7 |

## For Cory

- **Money:** The frame proposes optional supplies totaling $35, $20 and $20 per class across the three years, and suggests a $75 annual ceiling. These are planning figures, not verified quotes. The ceiling remains Cory’s decision.

No standard relocation, outside-person engagement or audience change is proposed.

## What I could not judge

- Actual learning time and assessment throughput without finished tasks, scores and audio.
- The quality of still-unselected works, translations, contextual accounts and community-specific teaching.
- Work-specific rights, safety and sensitivity outcomes. The frame itself marks several safety rules as from memory pending their assigned reads.
- Whether the no-device exemplars can be delivered successfully by the intended teacher.

No substantive finding rests solely on model memory. Prior memory guidance informed the review format only.

## For the source list

Add or retain these access and evidence notes:

- [National music handout](https://nationalartsstandards.org/sites/default/files/2021-11/Music%20at%20a%20Glance.pdf): readable PDF; used to check creating requirements and identifiers.
- [Official national handbook](https://www.nationalartsstandards.org/index.php/customize-handbook?discipline=Music%2CMusic+%28PK-8%29%2CTheatre&display_options=eq_el%2Cprocess_components&grade_level=6+-+8%2C6th%2C7th%2C8th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting): readable; used for performance selection, interpretation, connecting and grade 8 performance wording.
- [Marine Band Ives notes](https://www.marineband.marines.mil/Portals/175/Docs/Audio/Educational_Series/charles_ives/charles_ives_america.pdf): readable; identifies editions, arrangements and permission credits.
- [Brazilian heritage record](https://bcr.iphan.gov.br/bens-culturais/samba-de-roda-do-reconcavo-baiano/): readable Portuguese source; used to check samba de roda’s varied settings.
- [UNESCO samba de roda page](https://ich.unesco.org/en/RL/samba-de-roda-from-the-reconcavo-of-bahia-00101): **browser check**. Direct opening returned a human-verification wall. It was not fetched another way; the Brazilian heritage source supplied the usable evidence.

