# Independent second read: social-studies-kindergarten

**Review date:** 2026-11-14.  
**Disposition:** Revise before writing lessons.  
**Findings:** 11, comprising 5 serious, 4 moderate and 2 minor findings.

## What I read

I read all six unit plans, `docs/courses/social-studies-kindergarten/s01.md` through `s06.md`, including their assessment items, exit tickets, error registers and generated day lists. I compared them with:

- The course’s `frame.md`, `scope-and-sequence.md` and `data/plans/social-studies-kindergarten/days.csv`.
- All nineteen kindergarten progression rows and their receiving grade 1 rows in `data/progressions/social-studies.csv`.
- `AGENTS.md`, `docs/agents/EXPERT.md`, the social studies lens, `docs/GLOSSARY.md`, `docs/courses/UNIT-PLAN.md` and `docs/pipeline/briefs/plan-read.md`.
- The foundation, relevant roadmap sections, shared teaching approach, social studies source notes, subject adoption bar, standard-selection record and BASELINE rules 20 to 24.
- The official Massachusetts kindergarten standards, relevant C3 indicators, California kindergarten standards and the stored New York framework’s kindergarten pages. The stored New York edition identifies itself as revised February 2017.

I did not open the excluded expert report or any file prohibited by the blind rule. No files were edited or intentionally created.

**Gates:** `unitplan.py check social-studies-kindergarten` passed all six plans; `frame.py check social-studies-kindergarten` reported zero failures.

**Broader gate limitation:** `plan.py check` stopped because the environment lacks the Python `markdown` package; the course review proceeded.

## Course verdict

The course has a coherent progression, worthwhile questions, practical paper materials and unusually clear protections against compulsory disclosure and participation. It needs revision before lesson writing because Unit 2 omits part of its anchor standard, and several assessment schedules leave too little specified capacity for the individual explanations they require. The most valuable change is to assign required evidence to named days and child rosters, preserving teaching, response and communication time within the existing totals.

All findings below concern the **plan** layer. **REPEAT status is unassessed:** prior review reports were deliberately not consulted for this independent read.

## Unit 1: Learning together

### 1. Serious: The plan does not specify a workable way to collect its individual oral evidence

**Location:** [s01.md, field 5](/S:/CurioClass/docs/courses/social-studies-kindergarten/s01.md:66), assessment administration and daily exit-ticket instructions.  
**Confidence:** Firm about the missing collection specification; feasibility is a planning judgment.

Five three-child groups receive fifteen minutes per day. Each child must explain rules in two settings, discuss revision, compare views, make a supported claim, and ask and answer questions. Earlier records can supply some parts, but the plan makes their availability conditional.

The daily exits have the same unresolved problem. Two minutes for thirty individual responses allows four seconds per child before prompts, transitions or recording. Several exits require explanations or exchanges, rather than a mark that everyone can make simultaneously.

This matters because a lesson writer could preserve the stated minutes only by substituting group answers, omitting evidence or using the respond day mainly to finish assessment.

**Exact fix:**

- In field 5, replace the conditional earlier-observation arrangement with a required roster: collect item 4’s rule-function evidence on day 5 and item 6’s independent perspective comparison on day 7. Schedule items 1, 2 and 5 explicitly across their existing observation days.
- Replace the instruction that each three-minute group completes the whole conversation with: “Days 8 and 9 collect the remaining fresh explanations for item 3, the closing claim for item 7, and the question exchange for item 8. Consult the completed roster before repeating a prompt.”
- For every daily exit, specify either a simultaneous individual picture response or a named listening sample. Where an explanation is sampled, record other children as unobserved for that component.
- Add a teaching-day budget for days 1 to 7. On day 1, the ten-minute bridge must replace other supported work, rather than sit beside a full ordinary lesson.

## Unit 2: Doing our part

### 2. Serious: Justice is missing from the character study

**Location:** `s02.md`, fields 2 and 5, teaching source descriptions and assessment item 4; `data/standards/ma-hss-2018.txt`, `MA.K.T1.3`.  
**Confidence:** Firm.

The Massachusetts original includes justice among the qualities children encounter in characters. The local paraphrase omits it, and the plan follows that shortened list throughout teaching and assessment. This is a substantive omission, separate from the settled issue of codes lacking their own-word lines. See [Massachusetts 2018, printed page 33](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

Children can complete every listed prompt without identifying an example of putting an unfair situation right.

**Exact fix:**

- Correct the local `MA.K.T1.3` paraphrase to include justice.
- In field 2, change “fair, caring, responsible and in-charge characters” to “fair, caring, just, responsible and in-charge characters.”
- In *The Paper Workshop*, include a character correcting an exclusion so another character receives an equal opportunity to participate.
- In *The Puppet Basket*, revise Rae’s scene to show Rae noticing an excluded participant and restoring an equal turn. Keep this different from the teaching incident.
- Add a separate item 4 prompt and record: “Who helps put an unfair situation right? Show what the character did.” A supported identification of Rae’s corrective action meets it.
- Update the corresponding day and assessment descriptions through their data source.

### 3. Moderate: The informed-action lesson has no activity budget

**Location:** `s02.md`, fields 2 and 5, day 14.  
**Confidence:** Firm.

Day 14 includes hearing proposals, listening to reasons, seeking agreement, voting, counting, planning, acting and an exit ticket. The plan budgets assessment days 17 and 18 but does not allocate day 14’s twenty minutes.

The activity is appropriate. Its missing budget leaves the writer to decide which essential part disappears when discussion runs long.

**Exact fix:** Add this day 14 allocation:

| Activity | Minutes |
|---|---:|
| Reconnect with the question | 2 |
| Hear two prepared proposals and reasons | 4 |
| Seek a shared revision | 3 |
| Vote and compare/count the towers | 3 |
| Carry out the first accessible action | 5 |
| Record the result | 1 |
| Exit ticket | 2 |

State that day 13 produces the two proposal cards. If agreement needs longer, use a reversible first trial and revisit its result on day 17. Preserve the class’s choice of problem.

## Unit 3: Where things are

### 4. Moderate: The assessed picture graph lacks an explicit teaching allocation

**Location:** `s03.md`, field 2’s teaching sequence and field 5, assessment item 4 and days 24 to 26.  
**Confidence:** Likely.

Item 4 requires each child to construct a picture graph of observed features. That is a legitimate part of [C3 D2.Geo.1.K-2, printed page 41](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf). However, the teaching sequence names position words, comparison, keys and addresses without naming instruction in constructing or reading that graph.

The graph appears inside an already busy making-and-observation allocation. A writer could treat it as an assessed prerequisite rather than something this course teaches.

**Exact fix:**

- Add to field 2: “On day 24, model a two-category picture graph from observed feature counts, using one picture for each feature and a labeled place for zero.”
- On day 25, make a supported graph alongside the model.
- On day 26, collect the independent graph from a different bounded patch, alongside the independent map evidence.
- Name these tasks in the day descriptions and reallocate existing modeling minutes. Do not assume a mathematics lesson has already taught graph construction.

The address examples, school-location tasks and map-key handoff are otherwise coherent.

## Unit 4: Long ago and today

### 5. Serious: The fresh-source conversation is concentrated into an inadequate listening allowance

**Location:** [s04.md, field 5](/S:/CurioClass/docs/courses/social-studies-kindergarten/s04.md:62), day 39 administration and items 3 and 4.  
**Confidence:** Likely.

Day 39 allows eight minutes to hear missing source explanations and claims. Both assessment photographs are withheld until that day, so earlier rehearsal claims cannot establish the fresh-source performance. Eight minutes across thirty children provides sixteen seconds each for source use, comparison, a reasoned choice and continuity.

Day 40 offers ten further minutes, but those minutes also hold fresh tries after reteaching. Marking unheard responses honestly does not establish that the remaining work fits.

**Exact fix:**

- Move the independent ordering products into the existing observation allocations on days 36 and 37, after instruction, using the reserved fresh sets.
- On day 38, retain six minutes for the four-domain comparison and allocate ten minutes to fifteen children’s fresh-source conversations, with two minutes to reopen and two for the exit.
- On day 39, allocate fifteen minutes to the other fifteen children and genuinely missing parts, with two minutes for introduction and three for closure.
- Update field 5 to say that the fresh-source assessment begins on day 38. Keep the relevant source pair withheld until each child’s assessment.
- Reserve day 40 primarily for response and rechecking. Identify unfinished evidence separately from errors.

These are proposed planning allocations, not measured classroom timings.

### 6. Moderate: Day 37’s exit does not check using a historical source to learn about the past

**Location:** [s04.md, field 5, day 37 exit](/S:/CurioClass/docs/courses/social-studies-kindergarten/s04.md:80).  
**Confidence:** Firm.

The exit asks whether two present-day gray and colored drawings are old. It diagnoses a useful misconception about appearance, but a correct answer does not show how a historical source informs knowledge of the past. That is the owned verb in [C3 D2.His.10.K-2, printed page 48](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Exact fix:** Move the gray-picture contrast into the teaching response. Replace the exit with a fresh historical-source task, reserved solely for this purpose.

A concrete candidate is Dorothea Lange’s October 1939 photograph of children entering a school bus at Dead Ox Flat, identified in the [Library of Congress school-photograph essay](https://blogs.loc.gov/picturethis/2017/08/back-to-the-chalkboard-schooltime-photos-in-the-fsaowi-collection/?loclr=blogpic).

Use: “What can this photograph help us learn about how some children traveled to school long ago? Point to your clue.” The answer should connect the pictured boarding of a bus to past school travel, without generalizing to all children. Inspect the image before fixing its final print and answer examples.

## Unit 5: Days we remember

### 7. Serious: Day 47 carries too much new explanation, followed by an unspecified observation rotation

**Location:** `s05.md`, fields 2 and 5, day 47 and assessment items 5 and 6.  
**Confidence:** Likely.

The six-minute reading-and-modeling allowance must introduce the anthem’s history and explain the Pledge’s several unfamiliar phrases. Subsequent observations must establish each child’s understanding across those phrases, four symbols, a book question and answer, a holiday, a cultural comparison and a closing claim.

The plan distinguishes rehearsal from independent evidence correctly. It does not assign enough of the latter to specific children and days to demonstrate that the twenty-minute route holds.

**Exact fix:**

- Begin explaining the Pledge alongside the flag on day 45: loyalty and the flag standing for the country.
- On day 46, introduce republic, one nation and indivisible.
- On day 47, retain the anthem story and explain the remaining Pledge phrases.
- Use brief retrieval on days 48 and 49.
- Add the corresponding practice codes to the affected `days.csv` rows and regenerate the day list.
- In field 5, assign named child rosters and specific symbol parts to days 45 to 49. Day 50 should confirm missing parts and collect the fresh-source task, rather than serve as the assumed home for unspecified overflow.

Keep the voluntary-participation language. The plan’s distinction between understanding the text and choosing to recite is supported by [Barnette](https://www.govinfo.gov/content/pkg/USREPORTS-319/pdf/USREPORTS-319-624.pdf).

### 8. Moderate: The traditions work lacks the anchor’s local-community connection

**Location:** `s05.md`, fields 5 and 10, days 48 and 49.  
**Confidence:** Likely.

The two selected accounts are real and responsibly bounded: the [Jewish Hanukkah account](https://reformjudaism.org/jewish-holidays/hanukkah) and the [documented Japanese American festival](https://blog.janm.org/2023/02/07/hopping-into-the-year-of-the-rabbit-at-janms-2023-oshogatsu-family-festival/). However, the plan prescribes them for every classroom without connecting the comparison to traditions represented locally.

The Massachusetts clarification emphasizes members of the local community. See [printed page 34](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Exact fix:** Add a localization instruction to field 10: before day 48, identify a publicly documented local celebration or tradition from its community’s own published account. Connect one existing example to that local account, or replace one teaching example while retaining a supported comparison. Name the selected source and adapt the assessment cards accordingly. Require no family disclosure, guest or outside contact.

### 9. Minor: The current-Pledge link needs replacement

**Location:** `s05.md`, field 10, “Primary symbols.”  
**Confidence:** Firm.

The long Pledge URL returned 404 during this read. The source is real and traceable at a working shorter address.

**Exact fix:** Replace its URL with [Pledge of Allegiance: 1892](https://bensguide.gpo.gov/j-pledge-allegiance). Retain the instruction to use the text without adopting the page’s participation directions.

### 10. Minor: The handoff contains stale and inaccurate references

**Location:** [s05.md, field 3](/S:/CurioClass/docs/courses/social-studies-kindergarten/s05.md:40).  
**Confidence:** Firm.

“No unit 6 plan exists yet” is false in the reviewed set. The holiday retrieval is assigned specifically to year-end day 63, rather than both days 62 and 63.

**Exact fix:**

- Delete “No unit 6 plan exists yet.”
- Replace “Year-end days 62 to 63 retrieve holidays” with “Year-end day 63 retrieves holidays.”
- Link the unit 6 handoff to `s06.md`, field 4’s retrieval tasks.

## Unit 6: Work and trade

### 11. Serious: Twenty seconds per child does not adequately budget the required oral evidence

**Location:** [s06.md, field 5](/S:/CurioClass/docs/courses/social-studies-kindergarten/s06.md:70), days 58 to 60.  
**Confidence:** Likely.

Day 59 expects descriptions of two work scenes, a connection to observed school work and a supported closing claim. The administration proposes about twenty seconds per child. Day 58 similarly combines operating the store with hearing every child’s choice, reason, questions and answers.

Those allowances omit meaningful capacity for prompts, source reference, recording and clarification. The ten-minute fresh-try allowance on day 61 must also accommodate response, so it cannot be treated as unlimited completion time.

**Exact fix:**

- Replace the twenty-second assumption with a roster of ten children per day across days 58 to 60, reserving ten minutes of individual listening within each day’s existing work allocation.
- Introduce the reserved work scenes early enough for the first roster, without using them as worked examples.
- Distribute items 1 and 7 across those conversations, and specify which other parts are supplied by dated observations and simultaneous individual picture responses.
- Keep the fresh bakery task on day 60. Record knowledge and skill separately, as the plan already requires.
- Change item 7’s collection date from day 59 only to days 58 to 60, while retaining the class’s day 59 return to the question.
- State what happens if required evidence remains unheard after day 61: preserve that status in the year-end record rather than infer attainment.

The economic content itself is generally accurate, including the distinction between paid and unpaid work and the need to describe knowledge and skills. The bakery source is traceable through the [Library of Congress essay](https://blogs.loc.gov/picturethis/2021/11/a-slice-of-american-life-from-the-fsa-owi-photograph-collection/).

## What is sound and should remain

The unit questions generally permit more than one supported answer. The course moves sensibly from classroom participation to geography, chronology, remembrance and economics. All nineteen kindergarten progression rows have reciprocal receiving links in grade 1.

Keep the actual classroom action in Unit 2, the school-address privacy protection, the distinction between illustrations and historical records, the refusal to rank cultures or eras, and the treatment of access supports separately from content prompts.

I found no invented teaching source presented as an existing publication. Original stories, diagrams and records are explicitly identified as original or still to make. I found no suspicious question marks replacing apostrophes, quotation marks or accented letters in the six plans.

## Sources and limits

The principal outside checks were:

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): kindergarten content and clarifications.
- [C3 framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned civic, geographical, historical and economic verbs.
- [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): the recorded kindergarten comparison additions.
- [New York framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): live retrieval failed; I read the stored official February 2017 edition’s kindergarten pages.
- [The Lion and the Mouse](https://read.gov/aesop/007.html): the named fable and its content.
- [Cambridgeport contact page](https://cambridgeport.cpsd.us/explore-cport/contact-cambridgeport-school) and [Madison school page](https://madison.osd.wednet.edu/78859_1): the two current school addresses.
- [El Indio photograph](https://www.loc.gov/item/2017739497/), [San Antonio photograph](https://www.loc.gov/item/2017739367/) and [school-pump photograph](https://www.loc.gov/item/2017737271/): archival identities, dates and attribution.
- [Richmond Hamilton Farm](https://www.nps.gov/neri/learn/historyculture/richmond-hamilton-farm.htm): the historical-work reference.
- [Aquinnah history](https://wampanoagtribe-nsn.gov/wampanoag-history) and [Winslow and Peters accounts](https://americanindian.si.edu/nk360/thanksgiving/sq4ss1.html): living-community framing and distinct historical perspectives.
- [Great Seal history](https://diplomacy.state.gov/wp-content/uploads/2022/10/Great-Seal-PDF.pdf), [hand press](https://diplomacy.state.gov/items/great-seal-hand-press/), [anthem history](https://www.nps.gov/fomc/learn/historyculture/the-national-anthem.htm) and [flag facts](https://womenshistory.si.edu/spotlight/flag-day/flag-facts): symbol records and source traceability.
- [Public Law 118-206](https://www.govinfo.gov/content/pkg/PLAW-118publ206/pdf/PLAW-118publ206.pdf): the December 2024 national-bird designation. It does not invalidate the plan’s account of the eagle’s earlier use on the seal.

Tennessee’s official standards and crosswalk remained blocked. Its comparison is therefore incomplete across all six plans, as the plans acknowledge. Some archival pages were recoverable through indexed official records, but I did not independently inspect the full photograph images. Final image selection, accessibility, classroom timing and completed sensitivity coverage remain unverified.

Anticipated-error prevalence and actual child response times are not established by these documents. My timing judgments are planning judgments, not findings from classroom observation. Prior-session memory informed report organization only; no curricular finding rests on it.

## Settled by the expert

These are item-level recommendations for the fixer, not edits already made.

| Choice | Reason | File |
|---|---|---|
| Represent justice through correcting an exclusion and restoring an equal turn. | Covers the omitted concept without adding a separate topic. | `s02.md` |
| Teach graph construction explicitly before collecting the independent graph. | Removes an unstated prerequisite. | `s03.md` |
| Spread fresh-source conversations across existing final teaching and assessment days. | Protects explanation and response time. | `s04.md`, `s06.md` |
| Begin Pledge meanings alongside the earlier symbol lessons. | Reduces day 47’s concentration of new language. | `s05.md` |
| Use the working shorter federal Pledge URL. | Restores direct traceability. | `s05.md` |

## For the fixer

1. Correct `MA.K.T1.3` in the standards data, then update Unit 2’s mechanical standard text, teaching examples and assessment record.
2. Revise Unit 1’s evidence roster and exit-collection methods. Add the missing teaching-day budgets.
3. Add Unit 2’s day 14 allocation and identify the proposal preparation on day 13.
4. Add graph modeling, supported practice and independent collection to Unit 3.
5. Redistribute Unit 4’s ordering products and fresh-source conversations. Replace the day 37 exit.
6. Spread Unit 5’s Pledge teaching and assign observation rosters. Add the local-community connection, replace the broken URL and correct the handoff references.
7. Replace Unit 6’s twenty-second collection assumption with a roster and explicit evidence assignments.
8. Update `days.csv` wherever a recommendation changes a day’s task or codes, then regenerate affected tables through the repository’s established process.
9. Run the named unit-plan gate and course structural check again. Inspect the selected images before fixing their final prompts and answer examples.

## For the structure pass

1. **Check observation assessments substantively.** `scripts/unitplan.py` checks assessment-table coverage only for `assess` values `end` and `mid`. These six plans use `observe`, so their passing result does not establish item coverage. Add observation-aware checking by unit, code and part, accounting for tables whose first column is an item number.
2. **Preserve anchor detail in paraphrases.** Correct the justice omission in `data/standards/ma-hss-2018.txt`. Add a verification record for semantic lists and clarification statements so mechanical propagation cannot make an omission look complete.
3. **Require an evidence-collection plan.** Add fields for class size, simultaneous response methods, listening rosters, required parts, teacher recording time and completion capacity distinct from reteaching.
4. **Make daily budgets complete.** Require each teaching day’s allocation to include exits, retrieval, bridges and observation. A repeated statement that these occur “inside existing minutes” is insufficient.
5. **Track comparison status explicitly.** Record the Tennessee comparison as unverified until the relevant kindergarten text is actually read. Record the stored New York edition as February 2017.
6. **Track source inspection separately from traceability.** A valid catalog record should not imply that the photograph’s visible details or final print have been checked.

## For Cory

No new decision about scope, audience, money or outside people is required by these findings.

