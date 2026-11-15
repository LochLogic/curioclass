# Independent second read: social-studies-grade-2 unit plans

**Review date:** 14 November 2026  
**Delivery:** Complete report here. No files were changed.

## What I read

I read all seven unit plans, `docs/courses/social-studies-grade-2/s01.md` through `s07.md`, against the complete course frame, scope and sequence, all 96 rows of `days.csv`, the grade 2 social studies progression and its connected grade 1 and grade 3 rows.

I also read AGENTS.md, EXPERT.md, the social studies lens, GLOSSARY.md, UNIT-PLAN.md, plan-read.md, the relevant shared and social studies adoption criteria, FOUNDATION.md, APPROACH.md, the relevant ROADMAP and BASELINE sections, STANDARD.md, and relevant source notes. I checked the Massachusetts descriptions against the official framework and consulted the official C3 indicators. After forming the unit findings, I consulted the earlier grade 2 frame and sequence reviews for settled issues and repeat tags.

No separate section plans exist in this course folder. I did not open the prohibited unit-plan review or the other files excluded by the blind rule.

| Check | Result |
|---|---|
| `python -X utf8 scripts/unitplan.py check social-studies-grade-2` | All seven plans passed. |
| `python -X utf8 scripts/frame.py check social-studies-grade-2` | Zero failures; seven units, 96 days. |
| `python -X utf8 scripts/plan.py check` | Stopped because the Python package `markdown` is missing. |

The incomplete wider gate does not withhold this verdict.

## Course verdict

**Revise locally before lesson writing.** The seven-unit sequence and its handoffs are coherent, and the plans substantially complete the coverage repairs identified at the sequence stage. The most consequential remaining faults are an unsupported attribution to Anna’s oral history and unit 7’s conflict between its presentation schedule and required response time. Preserve the units, standards ownership and day totals while making the corrections below.

**Findings: 11, comprising two serious and nine moderate findings.** No finding rests solely on model memory. Pacing judgments remain planning judgments, except where the stated minutes directly conflict.

## Unit 1: Maps tell stories

### 1. Moderate: the mechanical day goal contradicts the accurate projection explanation

**Location:** `s01.md`, day-list row 10; `days.csv`, day 10; progression row `ss2-projections`.  
**LAYER:** plan and process. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Field 2 correctly distinguishes local angle preservation from the shapes of whole continents. The day goal still says “shapes kept,” without that qualification. The progression repeats it. A writer following the day goal could teach that Mercator preserves continental shapes.

Mercator preserves small local shapes, while distorting the shapes and areas of large regions. The distinction is explicit in the [federal map-projection explanation](https://store.usgs.gov/assets/mod/storefiles/PDF/16573.pdf).

**Why it matters.** Students could learn the very misconception the fuller plan tries to prevent.

**Exact fix.** In the canonical day 10 goal, replace:

> shapes kept, lands far from the equator drawn too big

with:

> shapes of very small areas kept, but large land shapes and sizes changed; lands far from the equator drawn too big

Make the corresponding correction in `ss2-projections`, then refresh the mechanical copy in `s01.md`. Retain field 2’s accurate teacher explanation.

### 2. Moderate: unit 1 lacks the language support supplied in later units

**Location:** `s01.md`, field 8.  
**LAYER:** plan. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Access accommodations are specific, but there is no equivalent vocabulary and sentence-frame provision for English learners. Later units supply this explicitly.

**Why it matters.** This unit introduces the language used throughout the year. Difficulty explaining a map part could be mistaken for difficulty understanding it.

**Exact fix.** Add a short language paragraph to field 8:

> Teach title, key, compass rose, scale, maker, date and place with labeled pictures and gestures. Rehearse “The key tells me ___” and “Each scale length stands for ___, so the distance is ___.” Accept pointing and home-language explanations before recording an English response. Judge map reasoning separately from English production.

Keep the existing access accommodations and alternative-map extension.

## Unit 2: Land, water and climate

### 3. Moderate: units 1 and 2 omit an explicit student progress record

**Location:** `s01.md` and `s02.md`, fields 7 and 10.  
**LAYER:** plan. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Students compare short answers with an answer key, but neither plan specifies a student self-check record showing what improved or what needs another try. Later units explicitly provide this. The shared adoption criterion C8 calls for students judging and tracking their work in every unit.

**Why it matters.** Teacher grouping records do not give children a corresponding account of their own progress.

**Exact fix.** Add a small illustrated self-check strip to each unit’s materials and remaining-work list. During the existing final review or feedback slot on days 16 and 29, children mark:

> I can show this now.  
> I improved this part.  
> I want another try at this part.

Have each child point to one piece of work supporting a mark. Use the last two minutes of the existing review slot, without adding time.

**Other unit 2 judgments.** The plan now secures continents, oceans and features on both representations, ocean habitability, environmental effects, and physical and cultural change. The 25-minute fresh assessment is crowded, but its paper globes and retained observations make an overrun less certain than unit 7’s explicit scheduling conflict. Preserve those observations.

The glacier dates are supported by the [2025 explanation of the 1984 and 2024 images](https://science.nasa.gov/earth/earth-observatory/glacial-losses-in-the-swiss-alps-154043/), and the weather-climate distinction agrees with the [current federal explanation](https://oceanservice.noaa.gov/facts/weather_climate.html).

## Unit 3: Living with the land

**No additional material finding.**

The plan identifies evidence for settlement reasons, environmental and cultural effects, community interdependence, production costs, tools, learned skills and disaster effects. Cedar Inlet is explicitly invented. The action includes choosing, carrying out and reviewing a safe contribution.

Day 44 remains demanding: seven linked responses in 25 minutes. I cannot certify its eventual layout or completion time, but I found no definite arithmetic overrun. Preserve the retained disaster observations and avoid expanding the response burden during production.

The named flood guide and recovery accounts are traceable: [town flood guide](https://montpelier-vt.org/610/Flood-Guide), [city recovery account](https://www.montpelier-vt.org/DocumentCenter/View/11065/Flood-Anniversary_July-24-2024), and [community reopening account](https://www.montpelieralive.com/blog/visiting-montpelier-after-the-july-2023-flood). The plan correctly distinguishes the recovery dates.

## Unit 4: Countries and trade

### 4. Moderate: day 51’s exit does not measure most of its comparison goal

**Location:** `s04.md`, field 5, daily evidence for day 51.  
**LAYER:** plan. **REPEAT:** yes, goal-to-evidence narrowing appeared in the earlier sequence review. **Confidence:** firm.

**What is wrong.** Day 51’s goal compares history, culture, language and government. Its exit checks culture, sourcing and fact versus opinion. It gives no direct evidence of the history, language or government comparison.

**Why it matters.** The teacher must wait until day 55’s larger assessed comparison to discover those gaps.

**Exact fix.** Replace the day 51 exit with a compact four-row comparison:

> Using Country Cards A, record one supported contrast in history, culture, language and government. Point to the card supporting each contrast.

The expected contrasts are the supplied 1947 and 1932 history facts, the named cultural examples, Japanese and Arabic, and representative government and hereditary governing authority. Keep the source-credit routine before reading. Reserve the completed comparison for independent evidence rather than demonstrating its answers first.

Day 55 should retain its fresh comparison and sourced trade claim.

### 5. Moderate: the canonical trade explanation is narrower than the plan’s own correction

**Location:** `s04.md`, field 3 mechanical rationale and day-list row 52; `days.csv`, day 52; progression row `ss2-trade-world`.  
**LAYER:** plan and process. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Field 2 correctly says countries can trade things both produce. The mechanical rationale and day goal still explain trade through resources or skills that the other country “lacks.”

**Why it matters.** The short canonical statement can become the lesson’s rule, contradicting the fuller explanation.

Trade also occurs for different varieties and lower costs, without either country being unable to produce the item. See the [central-bank explanation of international trade](https://www.stlouisfed.org/publications/page-one-economics/2013/11/01/the-global-economy-its-a-small-world-after-all).

**Exact fix.** Replace:

> each has resources and skills the other lacks

with:

> buyers seek useful resources, skills, different products or lower costs, including things both countries can produce

Make the matching correction in the progression and frame rationale, then refresh the mechanical copies.

## Unit 5: People on the move

### 6. Serious: the reserved Anna task attributes unsupported content to a real memory

**Location:** `s05.md`, field 5, day 65 daily evidence.  
**LAYER:** plan. **REPEAT:** new. **Confidence:** likely.

**What is wrong.** The task specifies an Anna memory of “feeling unable to speak at reunion.” The linked excerpt describes reunion, crying, food, curtains and embarrassment. It does not contain that stated feeling. The [linked oral-history transcript](https://www.nps.gov/elis/learn/education/oral-history-ei-89.htm) therefore does not support the reserved passage as described.

**Why it matters.** A writer could manufacture a feeling and present it as Anna’s testimony in a unit teaching source accuracy.

**Exact fix.** Replace the opening of the day 65 task with:

> A held-back part of Anna’s memory describes feeling embarrassed while accepting food after arriving. Compare it with an explicitly invented present-day newcomer who hopes to meet a cousin.

Replace the answer guidance with:

> Identify Anna’s remembered embarrassment and the invented newcomer’s stated hope. Explain a supported similarity or difference without claiming that both expressed the same feeling.

Reserve the food passage for this task. Keep the reunion passage for the opening hook. If a different authenticated excerpt is intended, identify that exact source before retaining the present wording.

### 7. Moderate: dated recent accounts are sometimes described as current views

**Location:** `s05.md`, field 5, day 62 task, Present Card and “Instruction sets.”  
**LAYER:** plan. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** The plan labels the interview date, but also calls Rahaf’s views “present-day” and describes her preference about visiting Syria “today.” The source records an interview on 3 June 2018. Omar’s supplied case describes resettlement in 2015.

**Why it matters.** Children could hear an eight-year-old preference as a statement of what Rahaf thinks in November 2026. This also weakens the course’s careful distinction between event dates, source dates and the present.

**Exact fix.**

- Replace “Rahaf’s present-day views” with “Rahaf’s views recorded in her 2018 interview.”
- Replace references to her preference “today” with “in that interview.”
- Add “The family was resettled in Luxembourg in 2015” to Omar’s route card.
- Describe these sources as recent accounts when contrasting them with the older memories. Keep the invented present-day comparison clearly labeled as invented.

These dates are explicit in the [Rahaf transcript](https://www.learningforjustice.org/sites/default/files/2018-06/TT-Raghad-Interview-Transcript.pdf) and [Omar teaching source](https://www.unhcr.org/uk/sites/uk/files/legacy-pdf/59d3811f7.pdf).

## Unit 6: Family stories and culture

### 8. Moderate: the ideas-movement task asks “why” without supplying or keying a reason

**Location:** `s06.md`, field 5, day 77 daily evidence.  
**LAYER:** plan. **REPEAT:** yes, completing the movement indicator across units was an earlier sequence finding. **Confidence:** firm.

**What is wrong.** The task asks what knowledge moved, how and why. Its musician card states that she moves and teaches songs, but gives no reason for sharing them. The answer explains what and how, then compares practices. It never answers why.

The [C3 movement indicator](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) includes both reasons and means.

**Why it matters.** Unit 5 relies on unit 6 to complete the ideas part of this indicator. The present evidence leaves one requested component unrecorded.

**Exact fix.** Change the musician card to:

> A musician moves by train and teaches songs in her new town so neighbors can sing together.

Add to the answer:

> The songs moved with a person and through teaching. She shared them so neighbors could sing together.

Record the reason separately from the means. Keep the warning against inferring that the other neighbor migrated.

### 9. Moderate: the mechanical goals retain universal claims rejected by the authored guidance

**Location:** `s06.md`, day-list rows 77 and 78; corresponding `days.csv` goals; progression row `ss2-culture-migration`.  
**LAYER:** plan and process. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Day 77 says foods, words and music are “now shared by everyone.” Day 78 asks for “one goal the whole community shares.” The authored tasks correctly avoid assuming universal participation or a unanimous preference.

**Why it matters.** A lesson writer could turn bounded examples into claims about every resident.

**Exact fix.**

- Day 77: replace “now shared by everyone” with “shared with other people in the receiving community.”
- Day 78: replace “one goal the whole community shares” with “one possible shared community goal, supported by the supplied examples.”
- Make the matching change in `ss2-culture-migration` and the scope-and-sequence wording.

Retain the authored statement that no single goal is claimed as everyone’s actual preference.

## Unit 7: A country up close

### 10. Serious: required response time cannot fit the stated presentation schedules

**Location:** `s07.md`, field 5, “Thirty-minute teaching path,” and field 6, “Next teaching moves.”  
**LAYER:** plan. **REPEAT:** new. **Confidence:** firm.

**What is wrong.** Days 90 and 91 each schedule thirty turns of about 45 seconds. Field 6 also requires ten minutes of response the next day when more than a third miss an exit.

Even allowing the response to include the model:

> 10 minutes response + 22.5 minutes turns + 2 minutes exit = 34.5 minutes.

That excludes transitions. The optional ten minutes cannot carry required learning under the stated core-path rule.

**Why it matters.** A class needing the promised response must lose either response time, individual evidence or the 30-minute path.

**Exact fix.** Distribute the performances within days 89 to 91:

- During day 89’s supported work, collect ten early combined oral and digital presentations, allowing 90 seconds each, 15 minutes total.
- On day 90, collect the remaining twenty digital turns, 15 minutes total.
- On day 91, collect the remaining twenty oral presentations, 15 minutes total.
- On days 90 and 91, reserve ten minutes for response including any model, three for transitions and two for the exit.
- Permit revisions through day 91 and score the latest authenticated work.

Update the rotation record and corresponding day notes. Students awaiting turns continue their paper work. This preserves one shared device, the paper path and all existing days.

### 11. Moderate: the Kenya source lead returned unrelated gambling content

**Location:** `s07.md`, field 10, country-menu table.  
**LAYER:** plan. **REPEAT:** new. **Confidence:** firm about the observed response.

**What is wrong.** Opening the [listed Kenya ministry address](https://mfa.go.ke/index.php/kenya) returned unrelated gambling links before the country material. An indexed version contains a country profile, but the address was not a clean reference during this read. This observation does not establish the cause.

**Why it matters.** The packet writer is directed to use this address as an official starting source. Its current returned content needs scrutiny before any extraction.

**Exact fix.** Replace that lead with the [official repository record for Kenya Facts and Figures 2026](https://repository.knbs.or.ke/entities/publication/dd01b86d-eef9-4a27-bd88-b16fe3350752). Mark it:

> Adult reference lead. Repository description inspected; booklet still to read. Reference only, with original factual captions to write.

The repository states a noncommercial licence. Do not infer permission to adapt its prose, tables or images. The direct booklet download failed during this read.

## What should remain

Preserve the maps-to-regions-to-resources sequence, countries before mapped migration, interviews after migration, and the final report gathering the year’s learning. The plans consistently carry sourcing and claim supports forward, identify grade 3 destinations, and acknowledge that last-day lesson files and Tomorrow lines do not yet exist.

Also preserve the clearly labeled invented cases, source-dependence checks, living Native nations, private interview alternatives, continued writing support, observed performances and separately counted respond days. I found no further material handoff break.

The explicit UTF-8 scan found no misplaced question marks, replacement characters or em dashes in the seven unit files. Reykjavík, Māori and Sámi are correctly encoded.

## Source verification and limits

Beyond the sources linked with findings, I checked the following relevant records:

| Area | Sources and result |
|---|---|
| Standards | [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) and [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf) were readable. Direct [Tennessee](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf) and [New York](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf) access failed; those comparisons remain limited to official indexed material and the repository’s comparison records. |
| Government | [Japan’s government explanation](https://web-japan.org/kidsweb/explore/government/), [the emperor’s constitutional role](https://www.kunaicho.go.jp/en/learn/institution/seido/seido01.html) and the [Saudi Basic Law record](https://www.wipo.int/wipolex/en/legislation/details/7973) support the selected distinctions. |
| Historical voices | [Smith’s narrative](https://nationalhumanitiescenter.org/pds/maai/freedom/text3/furro.pdf), [Catherine’s memory](https://www.nps.gov/elis/learn/education/oral-history-ei-116a.htm), [Angel Island interviews](https://www.aiisf.org/vault/16questions), [Antin’s 1899 account](https://www.gutenberg.org/cache/epub/20638/pg20638-images.html) and [1912 memoir](https://www.gutenberg.org/files/20885/20885-h/20885-h.htm) are traceable. |
| Living communities and culture | [Cherokee Nation history](https://www.cherokee.gov/about-the-nation/history/), [Eastern Band government](https://www.ebci.gov/), [Cherokee language education](https://www.cherokee.gov/life-events/learning-the-cherokee-language/) and [Posadas’s biography](https://www.arts.gov/honors/heritage/artemio-posadas) were reachable. The [Posadas interview](https://www.arts.gov/stories/podcast/artemio-posadas) returned an error directly, but its indexed transcript supported the shorter-gatherings detail. |
| Research sources | [Statistics Iceland’s fisheries page](https://www.statice.is/statistics/business-sectors/fisheries/) supports Page I’s work facts and record types. I attempted all sixteen country-menu leads; several blocked access or timed out. Portal access does not verify the unwritten packets. |

I did not find a fictitious whole source presented as real. Finding 6 concerns an unsupported detail attributed to a real source. Historical map margins, selected photograph crops, final packet reading difficulty and actual completion times remain incompletely verified. No conclusion about those rests on memory.

## For the fixer

Apply these edits in order:

1. Correct Anna’s reserved passage and answer guidance in `s05.md`, finding 6.
2. Reallocate unit 7’s performances and response slots in `s07.md` and day notes, finding 10.
3. Replace the Kenya source lead and record its inspection limits, finding 11.
4. Correct Mercator wording in day 10, the progression and mechanical copy, finding 1.
5. Correct the trade rationale and day 52 goal across their canonical records, finding 5.
6. Remove the universal culture and shared-goal wording from days 77 and 78 and their upstream records, finding 9.
7. Supply and score the reason for ideas moving on day 77, finding 8.
8. Replace day 51’s exit with the four-category comparison, finding 4.
9. Correct the dating language for Rahaf and Omar, finding 7.
10. Add unit 1’s language support, finding 2.
11. Add student self-check strips to units 1 and 2 within existing review time, finding 3.

Refresh mechanical copies through the pipeline after canonical data changes. Do not hand-edit generated tables or overwrite authored plan fields.

## For the structure pass

1. **Check complete mechanical rows.** `unitplan.py` currently checks day numbers and kinds, but does not compare every copied goal and note with `days.csv`. Add that comparison to catch drift after canonical corrections.

2. **Require a conditional response budget.** Add to the plan brief: show that the minimum-length lesson still fits when its stated whole-class response rule activates. For serial interviews and presentation turns, give the class size, turn count and total minutes.

3. **Require explicit student self-checking.** Add a brief field identifying the student’s record, collection day and existing time slot. Teacher records alone should not satisfy this requirement.

4. **Keep source leads separate from inspected evidence.** Require the exact passage, image or record used, its inspection status and any access limitation. A reachable official homepage should not count as a completed packet-source check.

5. **Synchronize the frame’s rights wording.** Replace its blanket public-domain description of island memories with the unit plans’ more careful item-level source and rights status.

6. **Keep the approximately 86-lesson route unvalidated.** The unit plans do not establish minutes for its proposed combined lessons. Preserve that status until each combination has a concrete budget retaining its evidence.

7. **Read and scan explicitly as UTF-8.** This avoids false corruption findings while still detecting replacement characters and question marks inside damaged words.

**For Cory:** No new scope, audience, money or outside-person decision is needed for these corrections.