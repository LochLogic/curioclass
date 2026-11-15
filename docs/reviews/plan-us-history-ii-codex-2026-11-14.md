# Independent second read: US History II unit plans

## What I read

I read `s01.md` through `s12.md`, the course frame and scope and sequence, all 160 rows of `data/plans/us-history-ii/days.csv`, the course’s social studies progression rows and relevant prerequisites, and the loaded Massachusetts USII standards.

I also read the required guidance files, the social studies lens and adoption bar, and relevant foundation, approach and source-access guidance. I did not open the earlier Claude report or the excluded files. No files were changed.

Checks:

- `unitplan.py check us-history-ii`: all 12 plans passed.
- `frame.py check us-history-ii`: passed, 160 days.
- `plan.py check us-history-ii`: passed.
- The repository-wide `plan.py check` stopped because the sandbox lacks the `markdown` module.

The day tables match the CSV’s goals, codes and notes. Their numbered school days correctly expand the CSV’s documented blank-column convention. I found no question marks replacing apostrophes, quotation marks or accented letters.

## Course verdict

The course has a sound historical sequence, substantial source reasoning and a workable composite assessment design. It needs targeted corrections before lesson writing, chiefly to secure the geography assessment, complete unit 8’s daily instructional plan and repair the short capstone schedule. Most historical distinctions are careful, and the checked 2025 and 2026 developments are supported by current sources.

There are **12 findings: three serious, eight moderate and one minor**. “REPEAT: not assessed” applies throughout because this independent read did not consult earlier reports.

## Unit 1: The economic toolkit

No substantive finding.

The supplied asset-return calculations and supply-and-demand equilibria recompute correctly. Preserve the distinction between liquidity and solvency, the modern Federal Reserve structure and its historical origins, and predicted economic consequences versus observations actually present in the banking table. The Federal Reserve’s current description supports the organizational explanation. [Federal Reserve structure](https://www.federalreserve.gov/faqs/about_12593.htm)

The 40-minute assessment is dense, but its earlier collection of A4 and the longer A8 argument makes the allocation plausible with the promised grids and brief responses.

## Unit 2: Tradition and modernity

No substantive finding.

Preserve the qualifications concerning citizenship, voting access, cultural visibility and legal equality. The linked Hurston record identifies the intended essay, and the genomics source supports the rejection of eugenics as sound science. [Hurston catalogue record](https://www.gutenberg.org/ebooks/73549), [Eugenics and Scientific Racism](https://www.genome.gov/about-genomics/fact-sheets/Eugenics-and-Scientific-Racism)

The assessment’s ten short responses require the concise format already specified. They should not grow into ten additional paragraphs during lesson production.

## Unit 3: Depression and New Deal

### 1. Moderate: the mechanical rationale still directs writers toward the wrong economics chapter

**Location:** `docs/courses/us-history-ii/s03.md`, field 3, mechanical “Why this unit, here”; the corresponding unit 3 rationale in `frame.md`.

**Problem and consequence:** The rationale says chapters 25 and 26 may be adapted for the two Depression explanations. Field 10 correctly says chapter 26 is not monetarism, while the course introduction correctly sources the monetary account separately. A writer following the mechanical rationale could build the wrong comparison.

**Exact fix:** In the frame’s unit 3 rationale, replace:

> Principles of Economics 2e chapters 25 and 26 may be adapted for them.

with:

> Chapter 25 supports the Keynesian account; the Federal Reserve’s Great Depression history supports the monetary account.

Regenerate the corresponding skeleton text in `s03.md`. Keep field 10’s warning.

**LAYER:** process and plan. **REPEAT:** not assessed. **Confidence:** firm, from the conflicting live instructions.

## Unit 4: Isolation, fascism and the Holocaust

### 2. Moderate: day 53 incorrectly places camp liberation after the war

**Location:** `data/plans/us-history-ii/days.csv`, day 53 goal; generated day list in `s04.md`.

**Problem and consequence:** “Liberation of the camps and the Nuremberg trials: what the Allies did after the war” places both events after the war. Major camp liberations occurred during the Allied advance in 1944 and 1945. This undermines a unit whose assessment depends on distinguishing responses before, during and after the war. [Liberation of Nazi Camps](https://encyclopedia.ushmm.org/content/en/article/liberation-of-nazi-camps)

**Exact fix:** Replace the day 53 goal with:

> Wartime liberation of the camps, survivors’ immediate needs, and the postwar Nuremberg trials: different Allied responses and their limits.

Regenerate the day list. Keep U6’s existing distinction between liberation, relief and prosecution.

**LAYER:** plan and data. **REPEAT:** not assessed. **Confidence:** firm.

### 3. Moderate: the authoritative day goal requires disagreement even when corroboration finds agreement

**Location:** `days.csv`, day 49 goal; generated day list in `s04.md`.

**Problem and consequence:** The goal ends “how the sources disagree.” The substantive S49 instructions correctly allow agreement to strengthen a bounded conclusion. The conflicting goal could make a lesson writer manufacture a disagreement between records serving different purposes.

**Exact fix:** Replace:

> what happened, what it changed, and how the sources disagree

with:

> what happened, what it changed, and where the sources agree, differ or leave uncertainty

Retain S49’s explicit warning against manufacturing disagreement.

**LAYER:** plan and data. **REPEAT:** not assessed. **Confidence:** firm, from the internal contradiction.

## Unit 5: The home front and the bomb

No substantive finding.

The assessment’s selected 1988 statutory provisions support the apology, acknowledged losses and redress explanation. The later museum account also supports the interpretation task actually assigned. Preserve the distinction between reasons offered, proposed alternatives and demonstrated necessity. [Public Law 100-383](https://www.govinfo.gov/content/pkg/STATUTE-102/pdf/STATUTE-102-Pg903.pdf), [Decision to Drop the Bomb](https://www.trumanlibrary.gov/museum/presidential-years/decision-to-drop-the-bomb)

The explicit treatment of Soviet entry, survivor accounts from both cities and uncertainty about alternative outcomes should remain.

## Unit 6: The Cold War at home and abroad

### 4. Serious: the geography assessment can reward hypothetical effects without establishing observed spatial change

**Location:** `s06.md`, field 5, A6 and its sample; U6, day 77.

**Problem and consequence:** A6 principally compares the reserved 1955 highway plan with the earlier 1951 trafficway plan. Source C establishes discriminatory access but supplies no located settlement outcome. The answer consequently explains what routes *could* do while correctly acknowledging that plans cannot establish actual development. That does not securely assess the claimed evaluation of economic and political impacts within and among urban, suburban and rural regions. [C3 Framework, printed page 42](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

**Exact fix:** Add **G77** to field 5 as an individually collected component of D2.Geo.8. Use the existing 20-minute evaluation block on day 77. Require:

> Using the dated settlement layers and one identified land-use record, locate an observed change within the city, within a suburb and at the rural fringe. Evaluate how a public decision and an economic activity contributed to those patterns and connections. Distinguish observed change from proposed routes and identify a competing explanation.

Name the actual settlement and land-use records in field 10. Add a scored sample containing located observations from those records.

Keep A6 as the unseen transfer task, but make its look-fors distinguish proposed consequences from G77’s observed changes. Count G77 once within the composite assessment.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** likely, based on the specified evidence and assessment criteria.

## Unit 7: The civil rights movement and its laws

### 5. Moderate: day 90’s practiced indicator does not match its task

**Location:** `s07.md`, field 2 and E90; `days.csv`, day 90 note.

**Problem and consequence:** D2.His.3.9-12 concerns changing historical significance over time. E90 instead compares how the positions of Little Rock parents and the President shaped contemporary accounts. The named practice therefore overstates what this task demonstrates. [C3 Framework, printed pages 45 to 46](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

**Exact fix:** Replace day 90’s practice tag with **D2.His.5.9-12** in the plan and CSV note. Amend E90 to require one specific feature of the 1957 setting that shaped each account’s emphasis. Keep its comparison of institutional responsibilities and its distinction from Montgomery.

**LAYER:** plan and data. **REPEAT:** not assessed. **Confidence:** firm.

The checked Callais summary is accurate at the stated level: the Court invalidated the challenged map and narrowed the relevant Section 2 districting analysis. Do not replace this with a claim that the entire Voting Rights Act was repealed. [Louisiana v. Callais](https://www.supremecourt.gov/opinions/25pdf/24-109_new_jifl.pdf)

## Unit 8: Presidents and the war in Vietnam

### 6. Serious: seven teaching days lack an operational time plan

**Location:** `s08.md`, days 103 to 109.

**Problem and consequence:** These days have content goals and five-minute exits, but no allocation of their remaining minutes among opening, teaching, source analysis and synthesis. Later collection days are timed precisely. The missing allocations conceal the workload of the Great Society, escalation and massacre, refugee histories, and Nixon’s diplomacy and Watergate.

**Exact fix:** Add a daily instructional table for days 103 to 109 identifying the source selections, teaching, independent or guided work, exit and model holder.

Use this initial allocation for days 103 and 105 to 109:

> Opening 5; direct teaching 15; source analysis 20; synthesis 5; exit 5.

For day 104 use:

> Readiness response or retrieval 10; direct teaching 15; source analysis 20; exit 5.

Within each row, divide the source block among the actual topics rather than assigning every listed document an unspecified reading. Preserve the existing allocations for days 110 to 113.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm.

### 7. Moderate: several exits check only a small fragment of their day’s goal

**Location:** `s08.md`, daily evidence table, especially days 104, 105, 106 and 109.

**Problem and consequence:** E104 checks Cuba but not Kennedy’s Vietnam policy. E105 can be answered without distinguishing any of the four initiatives. E106 checks one inference about Tet, and E109 checks normalization chronology while leaving Watergate and arms control unobserved. The teacher cannot identify the main gaps before the composite assessment.

**Exact fix:** Replace these exits with concise structured responses:

- **E104:** Contrast Kennedy’s Cuba decision with one Vietnam advisory decision, using an attributed detail for each.
- **E105:** Match four fresh policy cases to Medicare, Medicaid, a War on Poverty program and immigration reform; explain each mechanism and intended beneficiary.
- **E106:** Connect Tonkin authorization to escalation, distinguish Tet’s military and political consequences, and identify American responsibility for the deliberate murder of civilians at My Lai.
- **E109:** Explain one diplomatic gain and one separate abuse-of-power finding from fresh source selections; distinguish the 1972 opening from 1979 normalization.

Give each answer component an error letter and look-for. Fit these responses into finding 6’s daily allocations.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm.

## Unit 9: Movements for rights since the 1960s

### 8. Moderate: the Chicano and Asian American additions leave no required evidence of learning

**Location:** `s09.md`, E116, field 5 and day 116 pacing.

**Problem and consequence:** Day 116 promises both movements, but its exit assesses farmworker and Native sovereignty tactics only. Neither addition has a required later assessment component. Their inclusion could become a passing mention without evidence that students understood either.

**Exact fix:** Expand E116 with two short rows:

> For the East Los Angeles walkouts and the International Hotel campaign, identify a particular demand, a tactic and the institution being pressured.

Accept education-related demands directed toward school authorities for the walkouts, and protection against eviction directed toward relevant housing or property authorities for the hotel campaign. Require attribution and reject claims that either example represents every participant or organization. Both examples are traceable through the plan’s linked collections. [East Los Angeles walkouts](https://guides.loc.gov/latinx-civil-rights/east-la-walkouts), [Asian American activism guide introduction](https://blogs.loc.gov/ofthepeople/2023/11/ccdi-junior-fellow-spotlight-olivia-hewang-identity-and-solidarity-asian-american-activism-in-the-1960s-and-70s/)

On day 116, change synthesis from five to two minutes and the exit from five to eight. Retain the existing farmworker and sovereignty comparison.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm.

The 2026 background checks were not invented: the September Title IX recodification and Huerta foundation’s reported death date are supported by the linked records. [September 2026 final rule](https://www.govinfo.gov/content/pkg/FR-2026-09-29/html/2026-19929.htm), [Huerta foundation memorial](https://doloreshuerta.org/in-memory-of-dolores-huerta/)

## Unit 10: Liberals, conservatives and the Cold War’s end

No additional substantive finding.

Preserve the distinction between explaining a tradition fairly and accepting its causal claims. The reserved Johnson message is correctly identified as January 17, 1968. [Johnson’s message](https://www.presidency.ucsb.edu/documents/annual-message-the-congress-the-state-the-union-29)

The geographically inappropriate mechanical “general form” paragraph belongs in the structure fixes below.

## Unit 11: The United States since 1990

### 9. Moderate: the generated goal retains the Gulf War claim that the prose has already corrected

**Location:** `days.csv`, day 140 goal; `frame.md`, unit 11 addition; generated passages in `s11.md`.

**Problem and consequence:** The plan’s limits correctly place the Gulf War before Soviet dissolution, but day 140 still calls it “the first post-Cold War use of force.” The absolute “first” depends on an unstated period boundary and overlooks earlier interventions under common boundaries. The Gulf campaign ended in February 1991. [Gulf War chronology](https://history.state.gov/milestones/1989-1992/gulf-war), [Panama intervention chronology](https://history.army.mil/Research/Reference-Topics/Army-Campaigns/Brief-Summaries/Armed-Forces-Expeditions/Panama/)

**Exact fix:** Replace the day 140 goal with:

> The 1990 to 1991 Gulf crisis and coalition war during the Cold War’s ending; the September 11 attacks.

In the frame’s addition, replace “as the first post-Cold War use of force” with “during the Cold War’s ending.” Regenerate the mechanical passages.

**LAYER:** plan and data. **REPEAT:** not assessed. **Confidence:** firm.

## Unit 12: Capstone

### 10. Serious: the ten-day option removes 35 writing minutes without relocating the work

**Location:** `s12.md`, “Ten-day option,” field 5 collection schedule and presentation schedule.

**Problem and consequence:** The standalone path assigns 30 drafting minutes, 30 revision minutes and 35 completion minutes, totaling 95. The shorter path folds hand-in into presentation day. That presentation already consumes 50 minutes, so the completion block disappears and only 60 writing minutes remain. The same 1,500 to 2,000-word product is still required.

**Exact fix:** Give the ten-day option its own ten-session table. Preserve the product and recover the missing 35 minutes:

- In the shortened corroboration session, allocate opening 5, model 5, corroboration 10, independent drafting 25 and exit 5.
- In the shortened revision session, allocate feedback 5, revision and completion 40, and exit 5.

Together with the retained 30-minute drafting session, this restores 95 writing minutes. Place action before the combined presentation and hand-in session, as already required. Keep the two critiques distinct and preserve separate assessment and response sessions.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm about the missing allocation; the repaired workload remains untested.

### 11. Moderate: the one-child route requires an adult to supply an additional sourced argument

**Location:** `s12.md`, “Two rooms,” C151.

**Problem and consequence:** The adult writing partner must provide a separate sourced argument for critique, but no such argument or source pair is identified. This transfers substantive curriculum preparation to the parent and can make the critique task unavailable.

**Exact fix:** Add a supplied fallback to C151 and field 10’s production list:

> For one child, provide a separate 400-word argument, two cited source excerpts and the same critique form. The adult supplies discussion and feedback; the child completes the critique independently.

Label the argument as Curio Class original. Give it a defensible strength and an evidence-based weakness, with corresponding scoring samples. Keep it distinct from the model and reserved U159 packet.

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm.

### 12. Minor: the deliberately flawed explanation has an unintended ambiguity about who resigned

**Location:** `s12.md`, E152 explanation and answer.

**Problem and consequence:** “The April concert caused her earlier February resignation” leaves “her” ambiguous between Anderson and Eleanor Roosevelt. The intended test is reversed chronology, but the key does not explicitly resolve the actor.

**Exact fix:** Replace that clause with:

> Anderson’s April concert caused Eleanor Roosevelt’s earlier February resignation from the Daughters of the American Revolution.

In the answer, explicitly identify Roosevelt’s February 26 resignation and Anderson’s April 9 concert. Preserve the deliberate causal reversal for students to critique. [National Park Service account](https://www.nps.gov/hofr/learn/historyculture/marian-anderson.htm), [Roosevelt resignation record](https://www.dar.org/outreach/marian-anderson/nsdar-archives-marian-anderson-documents-january-april-1939)

**LAYER:** plan. **REPEAT:** not assessed. **Confidence:** firm.

## What should remain

Keep the chronological architecture, explicit counterclaims, independent collection of longer products, paper paths, source-purpose routines and distinctions between laws, implementation and lived access.

Keep community agency alongside harms, present-day Native governments, and the prohibitions on compelled disclosure and victim or perpetrator role play. The reviewed original captions and flawed explanations are identified as instructional constructions; I found no substantiated case of an invented historical quotation being presented as genuine.

## For the fixer

Apply these edits in order:

1. Repair unit 6’s geography evidence and collection arrangement, finding 4.
2. Write unit 8’s daily instructional table, then replace its incomplete exits, findings 6 and 7.
3. Write the ten-session capstone schedule and supplied one-child critique task, findings 10 and 11.
4. Correct the authoritative day goals for liberation, corroboration and the Gulf War, findings 2, 3 and 9.
5. Correct the unit 3 source rationale and day 90 practice mapping, findings 1 and 5.
6. Add the required Chicano and Asian American evidence, finding 8.
7. Clarify the resignation actor, finding 12.
8. Regenerate affected mechanical content and rerun the scoped unit-plan, frame and plan checks.

## For the structure pass

1. **Check operational daily planning.** Extend `scripts/unitplan.py` and the writing brief to detect missing instructional allocations in a merged plan. A goal row and a five-minute exit do not establish a complete day.

2. **Check assessment evidence separately from code presence.** Require each composite component to identify its collection day, independent work, source record, criteria and allocated minutes. The present passing gate does not expose unit 6’s evidence problem.

3. **Remove inappropriate localization boilerplate.** `s10.md` and `s11.md` mechanically direct national USII standards into “the class’s own place.” Restrict that skeleton instruction to the standards actually designated for own-state treatment.

4. **Separate settled choices from unfinished production.** Require source-dependent assessment records to name a particular document or dataset before the assessment is considered fully specified. Excerpt preparation can remain later work; generic descriptions such as “a worker account” should remain visibly unresolved.

5. **Check shorter paths independently.** Require a separate time ledger showing where merged or removed blocks’ required work goes.

6. **Refresh handoff metadata.** Remove the obsolete statements that units 6, 7 and 8 are unwritten from `s05.md`, `s06.md` and `s07.md`. Correct `s06.md`’s return to the completed flashpoint map from day 132 to day 131.

7. **Keep comparison limitations visible.** Tennessee’s official standards and crosswalk returned 403 in this read too. Its detailed unit comparisons remain unverified, rather than established by the presence of a comparison-table row.

## Settled by the expert

The proposed exit formats, day allocations, geography collection arrangement, shorter-path time repair and supplied critique fallback are item-level recommendations within the existing standards and day totals. No additional course days or external contacts are proposed.

## For Cory

The skeleton currently labels each whole unit as one section, including units lasting 10 to 17 days, while the glossary defines sections as one to six days. Confirm whether these are temporary section placeholders before section planning; redistribution of standards between sections remains your decision.

## Limits of this read

I checked selected primary documents, numerical answers, disputed chronology and recent developments against live sources. I did not visually inspect every image or map, clear reproduction rights, or verify every eventual teaching excerpt. The New Deal geography packet and the densest assessment sittings still need their finished materials reviewed for workload.

Historical findings above rest on the current files and linked sources. Memory was used only for the review-format and scope conventions.

