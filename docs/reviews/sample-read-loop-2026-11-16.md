# Sample read of nine Codex unit plans, 2026-11-16

Reader: expert-teacher read, read only. Units: math-grade-2 s03, math-grade-7 s05, algebra-i s04, science-grade-2 s04, biology s03, science-grade-7 s02, english-language-arts-grade-4 s02, english-language-arts-grade-10 s02, english-language-arts-grade-8 s03.

Severity: high = wrong content or an unusable assessment; medium = a teacher must fix it before teaching; low = anything else. Lens = the one-lens read that should have caught it (assessment covers fields 5 to 7, sources field 10, sequence fields 1 to 4 and the day list; none = no lens owns it).

What held up: I worked every math item, key and exit by hand in math-grade-2, math-grade-7 and algebra-i, and all of them are correct. The science arithmetic checks too: the photosynthesis and respiration balances, the fermentation carbon splits and the bond-energy statements in biology, and the 2-gram sleeve item in science-grade-7. The legal quotations in ELA grade 8 match the 1906 Act (section 7, food, second, fourth and fifth clauses; Statutes at Large 34, 768 to 772). The Faraday reserved passage in ELA grade 10 matches lecture I (the saturated salt-column capillarity example). Every doubtful link I tested resolves. That includes saja.org/jobs/535774, which hosts the SAJA style guidance despite its path, and also basskf, scroll.in, the isbe PDFs, Missouri gh1502, nchfp, Springer gb-2005-6-6-r49 (a yeast 13C study, described accurately), PMC3146749, hrcak 49504, ACS energy_foundations, the NPS pages and govinfo. Three sites refused automated fetches (403/503), so I did not check them: loc.gov, ocean.si.edu and gutenberg.org.

## Findings

| # | Unit | Field | What is wrong | Why it matters | Severity | Lens |
|---|---|---|---|---|---|---|
| 1 | math-grade-2 s03 | Day list, field 5 | Days 55 and 56 are coded Fluency and Application but are run as assessment-observation days. Base lessons 17 and 18 are mapped "keep" but are turned into assessment, so the header's three fluency days are really two. | The fluency practice the unit claims does not happen, and the source map misreports which lessons are taught. | medium | sequence |
| 2 | math-grade-2 s03 | Field 7, day list | Unit 2's response takes 10 minutes of day 39 (this unit's first teaching day) and 10 of day 40, which days.csv does not record. This unit's own response sits on unit 4's days 58 and 59, and days.csv notes this only on day 57. | It crowds the opening lesson and hides time taken from the next unit. | low | sequence |
| 3 | math-grade-2 s03 | Field 5 | 2.NBT.B.5 and 2.OA.A.1 are listed as owned, but they get no new evidence; the plan reuses unit 2's records. | Rule 5: owned codes need end-of-unit evidence. | low | assessment |
| 4 | math-grade-2 s03 | Field 1 weight | The major-work accounting counts the line-plot days 52 to 54 as only 5 supporting minutes. | The major-work share is overstated. | low | sequence |
| 5 | math-grade-7 s05 | Field 5, day list | S1 is produced and scored on day 88, a Fluency day ("No new content"), and the plan calls it "practice" yet scores it. days.csv says the scored 25-minute application is made on day 89 and reused on day 90, but the plan makes day 89 unscored practice. S1's percent-change context comes before the day 89 lesson that teaches it. | Scored work is made on the wrong day, before it is taught, and the plan contradicts days.csv. | medium | assessment |
| 6 | math-grade-7 s05 | U3 exit 69 | The exit (position -11, return to zero) nearly repeats the day 69 hook (-6 degrees, return to zero). | The exit is not a fresh case (rule 4). | low | assessment |
| 7 | math-grade-7 s05 | U3 exit 86 | It lists error K (fraction division with the divisor unchanged), but the exit has no fraction division. | The error letter cannot occur. | low | assessment |
| 8 | math-grade-7 s05 | U3 exit 87 | The context uses "4.5 identical parts". | Half a part is an incoherent count for students. | low | assessment |
| 9 | math-grade-7 s05 | Field 2 | 7.EE.B.4a is coded on days 85 to 87, but only one-step equations (6.EE) are taught there. Unit 6 completes the standard, and it is not assessed here. | The coding overstates what the unit covers. | low | sequence |
| 10 | math-grade-7 s05 | Field 2 hook, field 10 | The hook says "field 10 names its source structure", but field 10 does not. | The reference leads nowhere. | low | sources |
| 11 | algebra-i s04 | Field 5 | The day 70 graph record is scored for F-IF.B.4 and F-IF.B.6, yet day 70 (base lesson 8) is the first day students estimate rates from a graph and sketch from a verbal description. | First-teaching work is scored, against the plan's own rule. | medium | assessment |
| 12 | algebra-i s04 | U3 exit 63 | The wrong answer is lettered B (ordered-pair reversal), but the item asks about the direction of a function. | The wrong repair is triggered. | low | assessment |
| 13 | algebra-i s04 | Fields 2, 5 | S-ID.B.6a and 6c, A-CED.A.4 and A-REI.A.1 are owned with no tilde and have no field 5 item. The scope and sequence assesses them elsewhere, but the plan does not say so. | A reader cannot tell where these codes are assessed. | low | assessment |
| 14 | algebra-i s04 | Field 5 vs day list | Field 5 overrides days.csv's directions to score the day 66, 68, 73, 74 and 76 records. The plan discloses the mismatch but does not route it to the lead. | Two governing files disagree. | low | sequence |
| 15 | science-grade-2 s04 | Field 5 | The 2-PS1-3 rocket item is split across days 45 and 46. The second half of the class watches peers do the same unfamiliar task on day 45, then does it on day 46. | Half the class sees the item before sitting it. | medium | assessment |
| 16 | science-grade-2 s04 | Field 8 | The plan puts every child in fitted splash goggles on day 42, while days.csv says only the adult wears eye protection, and the $5 cost line does not cover class goggles. | The safety and supply lines contradict each other. | low | sources |
| 17 | science-grade-2 s04 | Field 4 | The retrieval rows s1-see-with-light and s1-like-parents are odd prerequisites for a matter unit. | It is a progression-data issue that wastes retrieval minutes. | low | sequence |
| 18 | biology s03 | Field 5 | The day 41 and 42 sittings are four 20-minute probes, all unscored. Every score comes from the day 37 and 38 drafts of the familiar pond case, revised on day 40. days.csv day 41 calls for an "unseen organism" model. | 80 minutes of unaided transfer evidence never counts, and the scores rest only on a familiar, coached case. | medium | assessment |
| 19 | biology s03 | Field 10 | The sensitivity-read sources are irrelevant to the unit: an autistic self-advocacy reproductive-autonomy page and rootedinrights.org. The "day 33 muscle record" is named, but the plan never describes day 33's muscle content. | The reads cannot do their job, and a scored record is undefined. | medium | sources |
| 20 | biology s03 | Field 5 | RST.9-10.3 has no scored check. WHST.9-10.2a to f are scored from responses drafted before the writing model on day 39. | One standard goes unassessed, and the writing scores come from work drafted before the skill was taught. | medium | assessment |
| 21 | biology s03 | Field 10 | NSTA's high school Safety Acknowledgment Form, a student contract, is cited as "school guidance". | It is the wrong kind of source for a safety check. | low | sources |
| 22 | science-grade-7 s02 | Fields 5, 8 | Field 8 says "Chemical trials are disabled; use data", but item 3 (4 points) and MS-PS1-6 require a physical build and retest on day 39. | As written, no student can earn a complete MS-PS1-6 result, so the unit cannot run as designed. | high | none |
| 23 | science-grade-7 s02 | Field 8 | The cost line reads "$160 per class, $62 per child, $10 printing; gloves exceed listed 100, so costs need correction". | The figures contradict each other, and the last clause is a pipeline note left inside the plan. | medium | none |
| 24 | science-grade-7 s02 | Fields 2, 5 | The hands-on device uses salt dissolution, which the unit's own limit says is not a chemical change. The item's invented "isolated product" evidence papers over this. (NGSS's clarification does cite dissolving calcium chloride.) | It teaches a muddled chemical/physical boundary. | medium | sequence |
| 25 | science-grade-7 s02 | Field 10 | NSTA's middle school Safety Acknowledgment Form is cited as guidance. | It is the wrong kind of source, the same fault as finding 21. | low | sources |
| 26 | science-grade-7 s02 | Field 8 | The frame calls for a ration-heater teacher demonstration; the plan bans it without flagging the change. | It is an unflagged departure from the frame. | low | sequence |
| 27 | science-grade-7 s02 | Field 5 | Item 3's sample warming numbers do not match field 10's simulated data (minute 4: 23 versus 25). | The key and the data disagree. | low | assessment |
| 28 | english-language-arts-grade-4 s02 | Fields 2, 10 | Every core text is unwritten: the anchor book, the five expert articles, the branching story and the reference cards. Fight to Survive! is "to confirm", and the vocabulary list "awaits manuscripts". | The unit cannot be taught, and its keys cannot be checked against real texts. | medium | sources |
| 29 | english-language-arts-grade-4 s02 | Field 5, D44c | The key relies on "sharp barbs", which is not in P44. | Students are marked against a detail they could not read. | medium | assessment |
| 30 | english-language-arts-grade-4 s02 | Field 6 | Letter A carries two misconceptions: a claim with no textual support (D75f, RF.4.4a), and an invented biological power (D70d). | It breaks the one-misconception-per-letter rule, so the repair misfits. | low | assessment |
| 31 | english-language-arts-grade-4 s02 | Field 5 | P56 is reused for the day 62 explanation. | A check passage is reused in a later check (rule 4). | low | assessment |
| 32 | english-language-arts-grade-4 s02 | Field 2, day list | W.4.2a to e have no Understanding day. | Informative writing is scored without being taught in this unit. | low | sequence |
| 33 | english-language-arts-grade-10 s02 | Field 5, C1 | Day 41's RI.9-10.3 item asks about the primer's farming-first order and the nuclear-transfer comparison. That repeats the day 34 supporting question, the day 34 practice prompt and the day 34 exit, on the same passages. | The item measures recall of a taught answer, not analysis. | medium | assessment |
| 34 | english-language-arts-grade-10 s02 | Field 5 | W.9-10.9b, SL.9-10.1a to d, L.9-10.4a to d and L.9-10.6 are owned but have no field 5 row. The word logs and discussion records are "scored on day 41" only in prose. | Rule 5 coverage is missing, and the teacher has no item, key or error letter for 10 parts. | medium | assessment |
| 35 | english-language-arts-grade-10 s02 | Field 5, reading capacity | Huxley's essay (about 8,800 words) gets 55 first-reading minutes, about 160 words a minute for dense 1868 prose that needs clause bracketing. The plan admits the rate is demanding and leaves it. | Most grade 10 readers will not finish, and days 29 to 31 depend on it. | medium | sequence |
| 36 | english-language-arts-grade-10 s02 | Field 5, N6 | The non-meeting sample (unexplained jargon for the audience) is lettered F (speaker not identifiable). "Ooplast" is not a term; the word is ooplasm. | The error letter is wrong, and the sample contains a nonword. | low | assessment |
| 37 | english-language-arts-grade-10 s02 | Field 10 | Faraday, Shelley and Bacon are used (Faraday for the assessment), but they are not in the text set, while field 10 says editions are in the text set. The tissue essay anchor is unwritten. | The records are incomplete, and one anchor is missing. | low | sources |
| 38 | english-language-arts-grade-10 s02 | Field 2 | The text set lists Pasteur and Tyndall fallbacks that the plan omits, but ela-texts.csv still carries them. | The files disagree. | low | sources |
| 39 | english-language-arts-grade-8 s03 | Field 5, A86.1 | The "cold" day 86 article restates the taught feature's central idea, its three supporting ideas and its qualification. The meeting answers match E63, E65, E76 and A75.1 almost word for word. | The end-of-unit RI.8.2 item measures recall, not central-idea analysis of an unfamiliar text. | high | assessment |
| 40 | english-language-arts-grade-8 s03 | Field 5, A86.2, A86.3, A86.6 | A86.3 tests precede (pre-, ced) and preservative (serv), the exact language-model teaching examples from days 68 and 73. The plan itself says "Do not use those teaching examples as the cold questions". qualified, prohibit and permit are on the week 16 and week 18 word lists. | The L.8.4 and L.8.5 strategy items test memorised words. | medium | assessment |
| 41 | english-language-arts-grade-8 s03 | Field 5 | RI.8.8, W.8.9 and SL.8.1 are owned and practised but have no end-of-unit item. W.8.2 and W.8.5 are stated to be formative only. | Rule 5 coverage is missing. | low | assessment |
| 42 | english-language-arts-grade-8 s03 | Field 10 | The anchor feature g8-u3-02 (3,000 to 4,000 words, read on days 63 to 65, 75 and 77) is unwritten, and E63, E65 and E76 depend on inserts inside it. | The unit cannot open until it is commissioned. | low | sources |

## Counts

Per unit (high / medium / low, total):

| Unit | High | Medium | Low | Total |
|---|---|---|---|---|
| math-grade-2 s03 | 0 | 1 | 3 | 4 |
| math-grade-7 s05 | 0 | 1 | 5 | 6 |
| algebra-i s04 | 0 | 1 | 3 | 4 |
| science-grade-2 s04 | 0 | 1 | 2 | 3 |
| biology s03 | 0 | 3 | 1 | 4 |
| science-grade-7 s02 | 1 | 2 | 3 | 6 |
| english-language-arts-grade-4 s02 | 0 | 2 | 3 | 5 |
| english-language-arts-grade-10 s02 | 0 | 3 | 3 | 6 |
| english-language-arts-grade-8 s03 | 1 | 1 | 2 | 4 |
| **Total** | **2** | **15** | **25** | **42** |

Per lens: assessment 21, sequence 10, sources 9, none 2.

## Repeated kinds (seen in two or more units)

1. **A check reuses taught material, so it is not fresh** (4 units: ELA 8, ELA 10, math 7, science 2). Example: ELA 8's day 86 cold article restates the taught feature's central idea (finding 39).
2. **Owned codes with no end-of-unit item or pointer** (5 units: math 2, algebra, biology, ELA 10, ELA 8). Example: ELA 10 has no field 5 row for W.9-10.9b, SL.9-10.1 or L.9-10.4 and 6 (finding 34).
3. **Scored work made on a first-teaching, fluency or pre-model day** (4 units: math 2, math 7, algebra, biology). Example: algebra scores the day 70 graph record on the day the skill is first taught (finding 11).
4. **The plan and days.csv disagree** (5 units: math 2, math 7, algebra, biology, science 7). Example: math 7 scores S1 on day 88 where days.csv puts the scored application on day 89 (finding 5).
5. **The error letter does not fit the item, or one letter carries two misconceptions** (4 units: math 7, algebra, ELA 4, ELA 10). Example: algebra exit 63 uses B (ordered-pair reversal) for a function-direction error (finding 12).
6. **Core texts are unwritten** (3 units: ELA 4, ELA 10, ELA 8). Example: every ELA 4 text is "to write" (finding 28).
7. **Weak or irrelevant safety and sensitivity sources** (2 units: biology, science 7). Example: the NSTA student acknowledgment form is cited as school safety guidance (findings 21, 25).
8. **Supply and safety lines contradict the items or each other** (2 units: science 2, science 7). Example: science 7 disables chemical trials, yet item 3 needs a build and retest (finding 22).

## Most serious

1. Finding 22 (science-grade-7 s02): the chemical trials are disabled, but MS-PS1-6 needs a physical build and retest, so the unit cannot be run as designed.
2. Finding 39 (english-language-arts-grade-8 s03): the cold RI.8.2 article restates the taught central idea, so the end-of-unit reading check measures recall.
3. Finding 18 (biology s03): the transfer sittings are unscored and every score rests on coached drafts of the familiar pond case.

Note on the lenses: the assessment lens should have caught 21 of the 42 findings, and the 2 that no lens owns are both science field 8 supply and safety lines. Field 8 has no lens owner, and it held the only unit-breaking fault.
