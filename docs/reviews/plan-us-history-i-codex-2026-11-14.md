# Independent second read: US History I unit plans

## What I read

I read all nine unit plans, `docs/courses/us-history-i/s01.md` through `s09.md`, including their assessment items, keys, daily evidence, error registers and generated day lists. I compared them with the course frame, scope and sequence, all 160 rows of `days.csv`, `source-map.csv`, and the relevant owned, assumed and receiving rows in `data/progressions/social-studies.csv`.

I also read the required review guidance, the social studies lens, the shared and social studies adoption criteria, and relevant foundation, approach and standards guidance. I checked the published Massachusetts framework and C3 indicators, selected archival sources, and the two adopted Since Time Immemorial guides. I did not open the prohibited report or the files excluded by the blind rule. No files were changed.

- `python -X utf8 scripts/unitplan.py check us-history-i`: all nine plans passed.
- `python -X utf8 scripts/frame.py check us-history-i`: passed, with 148 unit days and 12 course-level assessment and respond days.
- The broader `plan.py check` stopped because the environment lacks the `markdown` module; this does not withhold the verdict.

## Course verdict

**Revise before section planning.** The course has a coherent inquiry and writing arc, sensible unit handoffs, and substantial safeguards for teaching hard history. The principal defects are two losses of required meaning in the local standards paraphrases, incomplete evidence for several assessments, and an unresolved feedback schedule in unit 5. The stated assessment minutes add up, but several reading and response demands remain insufficiently specified to establish that they fit.

Findings below are numbered across the course. All have **LAYER: plan**. **REPEAT is unverified**, because earlier review reports were not consulted.

## Unit 1: Why break with Britain?

No substantive unit-specific finding.

Preserve the distinction between declared rights and achieved freedom, the comparison of historical interpretations, and the protected assessment petition. The [1777 petition](https://constitutioncenter.org/the-constitution/historic-document-library/detail/prince-hall-petition-to-the-massachusetts-legislature), [Fiske](https://www.gutenberg.org/files/41266/41266-h/41266-h.htm), [Becker](https://www.gutenberg.org/cache/epub/3093/pg3093-images.html), and [Revere appraisal](https://www.nga.gov/stories/articles/paul-revere-artist-american-revolution) are traceable and support the uses checked here.

## Unit 2: A government on trial

### 1. Serious: Task 4 requires case evidence that the assessment conditions do not supply

**Location:** [s02.md](S:/CurioClass/docs/courses/us-history-i/s02.md:90), field 5, Task 4 and Conditions.  
**Confidence:** Firm.

Task 4 requires students to use two sources from their chosen journalism case. The conditions prohibit notebooks and specify supplying only the unseen editorial. The plan therefore does not establish what evidence students can consult for the required comparison. This risks scoring remembered quotations or general knowledge as source analysis.

**Exact fix:** Supply a separate pair of reserved excerpts for each case pathway, with attribution and exact passage boundaries. Add this sentence to Conditions:

> Supply the unseen editorial and the two reserved case-source excerpts for the student’s chosen pathway.

Revise the samples against those actual excerpts and include their reading in the seven-minute allocation.

### 2. Moderate: The adopted guide’s closing work has no settled place inside day 25

**Location:** [s02.md](S:/CurioClass/docs/courses/us-history-i/s02.md:172), field 10, Since Time Immemorial paragraph.  
**Confidence:** Firm.

The plan promises the salmon, sovereignty, justice and cartoon work, including sharing, within fifty minutes. The [stored Level 1 guide](S:/CurioClass-sources/since-time-immemorial/high-school-unit-1-us-history/4-us-hs-unit-1-level-1kt_.pdf), page 2, permits cartoon creation as homework and explicitly places sharing in the next class. Day 26 already belongs to the information-history survey.

**Exact fix:** State that cartoon creation and sharing both occur on day 25. A concrete allocation is five minutes for constitutional retrieval, seven for salmon and justice, twelve for reading, eight for discussion, twelve for the cartoon, three for sharing and three for the exit ticket. Keep adult preparation outside those fifty minutes.

Also add a production instruction replacing the guide’s relative-age phrase “42 year-old decision” with “the 1974 decision.” This preserves the historical fact without carrying an obsolete age into new material.

## Unit 3: Expansion and removal

No substantive unit-specific finding.

The two assessment maps are identifiable. The [Mitchell catalogue](https://www.tsl.texas.gov/apps/arc/maps/index.php/maplookup/00387) supports the stated routes and competing Oregon boundaries, and the [Reynolds record](https://www.senate.gov/artandhistory/history/resources/pdf/ReynoldsPoliticalMapoftheUnitedStates.pdf) supports the later publication date and slavery categories. Preserve the distinction between mapped claims, consent and effective control.

## Unit 4: Mills, cotton and reform

### 3. Serious: The Mann strand drops compulsory schooling

**Location:** [s04.md](S:/CurioClass/docs/courses/us-history-i/s04.md:99), fields 2 and 5, Item 5c, its key, Component P option c, and day 55 evidence.  
**Confidence:** Firm.

The published anchor includes Mann’s campaign for free compulsory education. The local paraphrase and plan retain free schooling but omit compulsion. A student choosing this research strand could complete every stated requirement without examining attendance requirements. See the [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), printed page 124.

**Exact fix:** Replace “free public schooling” with “free public schooling and compulsory attendance” in the relevant standard part and coverage statements. Replace Item 5c with:

> Explain the difference between publicly funded schooling and compulsory attendance. Connect Mann’s campaign with literacy and newspaper and magazine publishing, and identify a limit on access.

Add the distinction to the key, the day 55 organizer and research option c. Correct the source paraphrase in `data/standards/ma-hss-2018.txt` before updating the mechanical text.

### 4. Moderate: The common reform assessment needs a more economical response form

**Location:** [s04.md](S:/CurioClass/docs/courses/us-history-i/s04.md:103), field 5, Item 5 and its five subparts.  
**Confidence:** Judgment call.

Nine minutes must cover five reform strands. The look-fors collectively require numerous people, institutions, connections and themes, including three Transcendentalists and six themes. Labelled phrases help factual entries, but the key also requires explanations. The plan has not demonstrated that this response format fits alongside the other thirty-one working minutes.

**Exact fix:** Retain an independent final version of each common survey organizer as an explicitly scored assessment component. Use it for factual breadth across all five strands. Rewrite the nine-minute Item 5 as two concise explanation tasks testing connections and limits, with a part-by-part coverage table showing what the organizers and final tasks assess together. Keep every strand and the chosen research investigation.

## Unit 5: The Union breaks and is rebuilt

### 5. Serious: The leadership and battle assessment falls below the published standard

**Location:** [s05.md](S:/CurioClass/docs/courses/us-history-i/s05.md:99), fields 2 and 5, Item 4, its look-fors, and day 79 evidence.  
**Confidence:** Firm.

The anchor requires analysis of the three leaders’ policies as well as their roles, and evaluation of battles over both short and long timescales. The local paraphrase loses those requirements. Item 4 asks students to identify offices and explain a consequence of each battle, so its key can be satisfied without the omitted analysis. See the [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), printed page 125.

**Exact fix:** Restore those parts in `data/standards/ma-hss-2018.txt` and field 2. Expand day 79’s evidence into a saved individual organizer that analyzes one consequential policy or strategic decision by Davis, Lee and Grant, and distinguishes immediate from enduring effects of the selected battles.

Name that organizer as an assessment component. Replace the five-minute Item 4 with a fresh source-based comparison that tests one of those judgments, rather than adding all the missing demands to its present five minutes.

### 6. Moderate: Both sustained essay questions are assigned despite the progression’s choice requirement

**Location:** [s05.md](S:/CurioClass/docs/courses/us-history-i/s05.md:132), field 5, P1 and P2.  
**Confidence:** Firm.

The progression’s `us1-argument-writing` row specifies a several-page argument on a question of the student’s choosing. Both unit 5 products prescribe the question and its principal counterclaim. Students can choose their answer, but the plan does not provide the stated question-making responsibility.

**Exact fix:** Introduce each existing question as a model. Add:

> Before drafting, each student writes a narrower arguable question within this essay’s historical subject. The teacher or parent checks that the question permits the required evidence, counterclaim and coverage. The student records any later revision to the question.

Retain the Civil War and Reconstruction subjects, source requirements and writing days.

### 7. Moderate: The feedback calendar contradicts the scope and sequence

**Location:** [s05.md](S:/CurioClass/docs/courses/us-history-i/s05.md:176), Feedback timing; field 7; scope and sequence, unit 5.  
**Confidence:** Firm.

The scope and sequence promises at least two school days for feedback between every draft. Drafts on days 81 and 82, and days 91 and 92, are adjacent. The unit acknowledges the contradiction but leaves its resolution to the lead, although the calendar is needed before lessons can be written.

**Exact fix:** Keep the existing days and settle the feedback method. Replace the scope’s promise with:

> Written teacher feedback on first drafts returns on days 81 and 91. Written peer or adult feedback on the revised drafts is completed during those days and used for the final drafts on days 82 and 92.

Allocate each revision day as five minutes orienting, thirty revising, ten exchanging written feedback and five recording the next revision. Delete “Feedback timing to review” once the documents agree.

## Unit 6: After Reconstruction

No substantive unit-specific finding.

The citizenship comparison distinguishes citizenship, protection as a person, voting and tribal membership. The reserved legal and reception sources are unusually specific. The [Chesnutt review](https://chesnuttarchive.org/item/ccda.rev00221) supports the stated reception summary.

The assessment’s forty working minutes are arithmetically allocated. Its claimed 650-word student packet still needs checking after the teacher interpretations are removed and the exact excerpts are assembled.

## Unit 7: Industry and newcomers

### 8. Serious: Essential assessment evidence remains unidentified

**Location:** [s07.md](S:/CurioClass/docs/courses/us-history-i/s07.md:66), field 5, reserved assessment evidence and migration cards.  
**Confidence:** Firm.

C2 is an unselected photograph. C3 is an unselected commission passage. The later Irish letter, Korean personal account and railway table are also unselected. The key nevertheless assumes that the packet supports particular motives, occupations and comparisons. Those claims cannot yet be checked against the evidence students will receive.

**Exact fix:** Replace each placeholder with an item identifier, exact excerpt or table, provenance and the permitted inference. Specify the railway report’s volume, page, table and original categories. Revise the key wherever the selected evidence does not support a required claim. Then assemble and count the actual packet against the 900-word ceiling.

The [Korean historical archive page](https://contents.history.go.kr/mobile/hm/view.do?levelId=hm_135_0030) already includes an English transcription of Allen’s December 10, 1902 letter. Replace the instruction to locate English text with an instruction to check that transcription against the archival original. It supplies a recruiter’s account; it does not replace the promised immigrant voice.

### 9. Moderate: Two three-minute exits contain too many independent judgments

**Location:** [s07.md](S:/CurioClass/docs/courses/us-history-i/s07.md:92), E116 and E117.  
**Confidence:** Judgment call.

E116 requires reading four new snippets and identifying a motive and occupation for each group. E117 similarly requires three source-based group comparisons and a geographic distinction. These are useful tasks, but three minutes encourages abbreviated listing and makes it difficult to distinguish source reasoning from hurried omissions.

**Exact fix:** Collect the complete comparison organizer during the lesson. Make E116 a final explanation of one contrasting pair. Make E117 a final explanation of one plantation-to-mainland distinction, supported by two source details. Assess the remaining groups through the collected organizer and the end-of-unit assessment.

## Unit 8: The Progressive Era

### 10. Serious: Several reserved evidence sets are still descriptions of future selections

**Location:** [s08.md](S:/CurioClass/docs/courses/us-history-i/s08.md:85), field 5, P3 to P6.  
**Confidence:** Firm.

P3 lacks its independent public record. P4 lacks the selected Terrell paragraph. P5 lacks its photograph identifier. P6 leaves the Niagara passage, court extract and Chicago account unbounded. This prevents checking whether the evidence supports the key and whether the full packet fits 850 words.

**Exact fix:** Complete those selections in field 5 before section planning. Give each document an identifier and exact boundaries, separate student evidence from teacher interpretation, and revise each sample against what the selected documents establish. In P3, explicitly establish whether the paired record is independent of Wells’s newspaper evidence chain.

The [Wells text](https://www.gutenberg.org/cache/epub/14977/pg14977-images.html) makes that evidence chain visible. Repetition of the same underlying report would not supply the independent corroboration the item requires.

## Unit 9: Empire, news and the First World War

### 11. Serious: The final assessment cannot yet substantiate its evidence and timing claims

**Location:** [s09.md](S:/CurioClass/docs/courses/us-history-i/s09.md:93), field 5, Source packet.  
**Confidence:** Firm.

The mortality and wave card, service photograph, shipping and troop table, legal extract, Wilson passage and Senate chronology are not supplied or fully identified. Several tasks depend on them. Consequently, the 700-word ceiling and forty-five-minute working allocation describe a packet that has not yet been defined.

**Exact fix:** Supply the actual reserved cards, item identifiers, table values, passage boundaries and labelled original summaries. For every numerical entry, provide its date and source. Check every answer against that packet, then confirm the word count and response allocation.

Preserve the explicit labels identifying the invented news and opinion cards. They are honestly presented as teaching texts.

### 12. Moderate: E142 repeats the overloaded exit pattern

**Location:** [s09.md](S:/CurioClass/docs/courses/us-history-i/s09.md:133), E142.  
**Confidence:** Judgment call.

The final three minutes require five explanations of power and affected people across five different policies. This is closer to another survey than a short, interpretable exit ticket.

**Exact fix:** Collect the five-policy organizer during the lesson. Replace E142 with:

> Compare two policies from today’s organizer. Explain one difference in how the United States exercised power, using one source detail for each.

Retain the other policies in the organizer and assessment.

## What should remain

Preserve the course’s chronological and thematic handoffs, recurring sourcing routines, composite writing assessments, paper access and independent coverage of survey options. Preserve its treatment of Native nations as continuing governments, Black agency, coercion and unequal enforcement. The informed action permits a reasoned decision not to act and does not reward agreement with a prescribed cause.

I found no corrupted apostrophes, quotation marks or accented letters represented by question marks in the nine plans. URL query characters were excluded from that check.

## Sources, currency and limits

The dated sources checked are real: the [2025 Muscogee Nation statement](https://www.muscogeenation.com/2025/07/08/muscogee-nation-marks-fifth-anniversary-of-mcgirt-ruling-with-sovereignty-day-celebration/), [March 2026 Lowell article](https://blogs.loc.gov/bibliomania/2026/03/04/the-lowell-offering-and-the-literature-of-the-lowell-mill-girls/), and [April 2026 Callais opinion](https://www.supremecourt.gov/opinions/25pdf/24-109_new_jifl.pdf) resolve. The [2022 anti-lynching law](https://www.govinfo.gov/content/pkg/PLAW-117publ107/html/PLAW-117publ107.htm) and [territorial definitions](https://www.doi.gov/oia/islands/politicatypes) support the currency notes checked.

The quoted assessment passages checked against [Douglass](https://www.gutenberg.org/cache/epub/23/pg23-images.html), [Gooding](https://freedmen.umd.edu/gooding.htm) and [Taylor](https://s3-eu-west-1.amazonaws.com/s3-euw1-ap-pe-ws4-cws-documents.ri-prod/9780415896009/Document3-5.pdf) are traceable. No invented historical source was identified among the materials verified. Unselected stimuli remain unverifiable.

The [C3 framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) was checked for the relevant inquiry and geographic demands. California and the current college-level framework opened; New York was read from the stored official PDF after the live request timed out. Tennessee returned 403, so that comparison remains incomplete.

Unreopened historical details and anticipated student errors rest partly on disciplinary memory. Timing judgments above are professional judgments, not observed student completion times. Lesson-level Tomorrow lines and the finished student packets do not yet exist for verification.

## For the fixer

Apply these edits in order:

1. Correct the compulsory-schooling and leadership-policy paraphrases in `data/standards/ma-hss-2018.txt`. Update the affected mechanical fields through the normal generation process.
2. Repair unit 4’s Mann coverage and unit 5’s leadership and battle evidence, including their assessment components and keys.
3. Complete unit 2’s case-source packets and the missing assessment selections in units 7, 8 and 9. Check keys against the actual evidence before adjusting minutes.
4. Settle unit 5’s feedback calendar and student-authored questions in both the unit plan and scope and sequence.
5. Settle day 25’s in-period cartoon work and replace the inherited relative-age wording.
6. Revise unit 4’s common reform assessment and the overloaded exits in units 7 and 9.
7. Recheck packet word counts, source reservations and assessment totals. Rerun the unit-plan and frame checks.

**Settled by the expert:** The proposed question-choice procedure, feedback method, day 25 allocation and exit-ticket reductions are item-level choices inside the existing course days. No standard moves between units or sections, no additional days and no outside readers are proposed.

**For Cory:** None.

## For the structure pass

- Add required qualifiers and verb parts to the standards data. A code appearing in an assessment row does not establish full coverage.
- Give every assessment stimulus a stable identifier, exact boundaries, source, word count and reservation status. Flag required evidence still described as an unspecified photograph, passage or table.
- Represent composite assessment components explicitly, including completion day, scoring day and response day.
- Check draft and feedback calendars against the promises in course prose.
- Add a feasibility record for dense tasks: actual reading, required responses and allocated minutes. Keep arithmetic checks separate from judgments about likely completion.
- Resolve the missing `markdown` dependency in the read-only check path.
- Complete the subject approach and shorter-path validation centrally. The scope explicitly says the shorter routes have not yet been shown to fit, and these unit plans do not settle that work.