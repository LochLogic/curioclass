# Social studies grade 4 unit plans: fixes, 2026-11-14

Reads applied: the expert read (docs/reviews/plan-social-studies-grade-4-2026-11-14.md) and the Codex read (docs/reviews/plan-social-studies-grade-4-codex-2026-11-14.md). Work followed the expert's "For the fixer" list in order, then the Codex findings it did not cover.

Gates: `python -X utf8 scripts/unitplan.py check social-studies-grade-4` passes all seven units. `python -X utf8 scripts/sequence.py check social-studies-grade-4` has 0 failures. `python -X utf8 scripts/frame.py check social-studies-grade-4` has 0 failures. The day count (160) and unit totals are unchanged.

## Findings applied

### Unit 1 (s01.md)
- **Expert 1.1 (start-of-year check).** Field 4 no longer has a readiness table or a sitting before day 1. It now reads "Start-of-year check: none needed; retrieval only." The check is the grade 3 record plus access notes from days 1 to 3, and nothing is scored. The handoffs line now points to the day 1 and day 12 retrieval tasks.
- **Expert 1.2.** The field 2 Teaching bullet now models only a source's maker and date. Audience and purpose come in unit 4.
- **Expert 1.3.** The day 6 exit now says "each bar is 60 kilometres".
- **Expert 1.4 and 1.5.** The exit 11 key names the Cherokee Nation. An Inuit example (Nunavut, through ITK) follows the exit table.
- **Expert CW2.** Field 6 now has a teacher note on place names, as of November 2026: the common name first, then the United States federal name since 2025 in brackets.
- **Codex 1.** Q1 now uses the rotated-arrow P/Q direction item, so wrong answer B ("north, because P is higher on the page") shows error B. Packet text adds a measurement inset with north pointing right, plus a north-up locator. Yucatán and Yukon are dropped; Q2 asks which place is a province.
- **Expert CW1 (time).** Field 7 is re-totalled: Q1 9, Q2 12, Q3 6, Q4 8.

### Unit 2 (s02.md)
- **Expert 2.1.**
  - Field 10 now uses ITK in place of the ICC children's page and adds INPI.
  - One community source inside Mexico is still to choose, and is listed as such.
  - FIOB is labelled as a binational organization of Oaxacan Indigenous migrants.
  - The sensitivity study adds Métis governance (the MMF left the Métis National Council in 2021) and Afro-Mexican recognition (2019, widened 2024).
  - Day 23 has an Afro-Mexican line.
- **Expert 2.2.** Day 24 has a teacher background line, as of November 2026. It covers the Mexican court: elections on 1 June 2025, nine justices seated on 1 September 2025, staggered terms for this first group, and a single 12-year term for later justices. It also names Carney, Charles III and Sheinbaum.
- **Expert 2.3.** There is a trade teacher background line, as of November 2026:
  - USMCA, CUSMA and T-MEC: the 1 July 2026 review did not confirm the extension, so the agreement stays in force to 2036 and is now reviewed every year.
  - The 20 February 2026 ruling that the IEEPA does not let the president set tariffs.
  - Because of the word cap, the line sits in the field 6 teacher notes, not in the field 2 Limits.
- **Expert 2.4.** The corroboration row in frame.md now gives unit 2 as first use and unit 4 as used again. The Carried lines in s02 and s04 match.
- **Expert CW1.** Field 7: reading 4, Q6 8.

### Unit 3 (s03.md)
- **Expert 3.1.** Q5 is now one paragraph naming two sources. The two linked paragraphs move to day 56. Field 7: reading 5, Q1 6, Q2 6, Q3 6, Q4 4, Q5 8.
- **Expert 3.2.** A Mesa Verde teacher note names the 26 associated tribes (NPS) and the Ute Mountain Ute Tribal Park.

### Unit 4 (s04.md)
- **Expert 4.1.** Q4 has a century line for 1492 and 1521 (10 cm a century, within 2 mm) and a 1530 to 1550 zoom strip (1 cm a year). On the strip, Coronado's span is 10 to 12 cm and Cartier's 11 to 12 cm, within 5 mm. The look-fors are updated, and Q4 is 8 minutes.
- **Expert 4.2.** Day 71 has a St. Lawrence Iroquoian note, marked as from memory.
- **Expert 4.3.** In days.csv, day 65 and day 73 notes name their retrieval tasks (ss3-early-colonies, ss3-timeline). The s04 day list is synced.
- **Expert 4.4.** The Q2 background gives 1021 CE (Kuitems and others, Nature 2021).
- **Codex 2.** The day 64 goal in days.csv now separates the camp at L'Anse aux Meadows from evidence for, and limits on, encounters elsewhere on the coast. The s04 day list is synced.
- **Expert CW1.** Q6 is one paragraph naming two sources. Field 7: Q4 8, Q6 8.

### Unit 5 (s05.md)
- **Expert 5.1.** A Whitman teacher note gives measles in 1847, the killings in November 1847, and the Cayuse Five hanged in 1850. The sensitivity study adds Tamástslikt (CTUIR). Q3 is narrowed to one detail each on trail life and settlement life.
- **Expert 5.2 and Codex 4.** "Gutiérrez" and "Ramón" are restored everywhere.
- **Expert 5.3 to 5.5.**
  - An Equiano teacher note.
  - The day 93 key now says "legal in all thirteen colonies".
  - The 1993 Apology Resolution (PL 103-150) is added to the teacher notes and to packet G.
- **Codex 3.**
  - The Q2 grid adds Puerto Rico: 1898, the war with Spain, the Treaty of Paris, a territory and not a state.
  - Packet A adds a Puerto Rico inset.
  - Q8 moves from Hawaii to the Louisiana Purchase (the Mississippi, New Orleans and river trade), with a new key and look-fors.
- **Expert 5.6 and CW1.** Field 7: orientation 2, Q1 3, Q2 4, Q3 3, Q4 2, Q5 2, Q6 3, Q7 4, Q8 4, Q9 8 (one paragraph).

### Unit 6 (s06.md and days.csv)
- **Expert 6.1 and Codex 5.** Both assessments drop the five-map design.
  - **Day 120:** M1 to M3 are kept. M4 is one full constructed Northeast map. M5a to M5d are short readings of completed Florida, Iowa, Arizona and Utah maps.
  - **Day 131:** F3d is one full constructed New Mexico map. F3a, F3b, F3c and F3e are one map-part prompt each, on partly drawn maps.
  - **Portfolio:** the unaided maps from days 113 to 118 are scored as a map portfolio, kept by standard.
  - **D2.Geo.1 rows:** these now name the unfamiliar-place map and the day 113 familiar-place map. "A sixth small outline" is removed.
  - **Field 7, day 120:** orientation 3, locate 9, chronology and statehood 6, M4 12, M5 5.
  - **Field 7, day 131:** orientation 3, locate, date and statehood 5, maps 10 (F3d 6, part prompts 4), inquiry and claim 10, economics 4, capital 3. Each day totals 35, plus marking 5.
- **Expert 6.2 and 6.3.** The F3d key and the day 117 teacher note now say that the Mescalero Apache were held at Bosque Redondo from 1863 and left in 1865. F3d is now a Mescalero Apache map, so the Southwest maps show two nations, Navajo on M5c and Mescalero Apache on F3d. The sensitivity study adds the Mescalero Apache Tribe's own account.
- **Codex 6.** Exploration is restored in the plan:
  - Each Southwest map has a dated exploration-route layer: Anza's 1774 route from Tubac on Arizona, and the 1776 Domínguez and Escalante route from Santa Fe on New Mexico.
  - Day 117 models this layer with Coronado's route.
  - The Southwest look-fors are updated.
  - Field 5 notes that the local standards wording drops exploration (see "For the structure pass").
- **Codex 7.** In days.csv, day 111's code MA.4.T4a.1 becomes MA.4.T4a.3. The s06 day list is synced.
- **Expert CW2.**
  - The M1 Texas key reads "Gulf of Mexico (Gulf of America in United States federal use since 2025)".
  - A dual-label teacher note covers the Gulf and Denali. It sits in field 6, not field 8 as the read asked, to stay under the word cap.
- **Michigan note.** Tidied to "Michigan's 1837 admission is verified against Senate history", since the anchor does not give 1838.

### Unit 7 (s07.md)
- **Codex 8 and 9 (the grade 3 settlement), in place of expert 7.1's underlining.**
  - C1 to C4 are now the scored regional records from days 138 to 141. Each named group gets a sentence in the student's own words, tied to its source, scored and kept by group.
  - C5 is the days 142 and 143 West record plus the final transfer task: describe two groups' contributions from the unseen West strip, then compare one with another region.
  - Underlining is removed. The other four strips are kept unseen as retry material for day 160.
  - The look-fors and the scoring line are rewritten to match.
- **Expert CW1.** A1 is one paragraph naming two sources. The longer argument, with another emphasis, is judged from day 158. Field 7 (30 minutes): cultures transfer 5, hazards 6, movement and catastrophes 6, policy 5, argument 8, plus review 5 and marking 5.
- **Expert 7.2.** A Buffalo Soldiers teacher note for day 141 says they built posts and towns and also fought in the army's wars against the Apache and other nations, and to teach both. The topic is added to the sensitivity study.
- **Expert 7.3.**
  - The sensitivity study adds a community-owned source for each immigrant community: the Filipino American National Historical Society, a Hmong American center and a Somali organization in Maine.
  - It also adds a California Native nation's account of the missions.
  - The Cherokee link is relabelled as the Cherokee Nation (Oklahoma), with a note to add the Eastern Band's own source for the Southeast strip.
- **Expert 7.4.** A disaster aid teacher background line, as of November 2026, sits in field 6.
- **Codex 10.** A claim-to-source record table sits in field 5. It gives the known sources, including Liberation Farms and the Allensworth record, and marks the rest as from memory.

### Every unit
- **Expert CW3.** The Tennessee rows now read "Not yet compared; the 2024 standards PDF on tn.gov refuses automated reading. STANDARD.md governs."
- **Expert CW4.**
  - The line "Since Time Immemorial is not used." is deleted. The read allowed deletion, since it is a note to the writer, not the teacher.
  - The "Step back on N" lines are rewritten as "On N students work without a teacher model" (s02, s03, s04, s06, s07).
- **No em dashes.** None remain in the seven plans, frame.md or days.csv.
- **Restored "?" characters.** None remain.

## Findings not applied
- **Expert 7.3, "cherokee.gov is the Eastern Band".** This is wrong. cherokee.gov is the Cherokee Nation, Tahlequah, Oklahoma (fetched 2026-11-14). The link is labelled correctly instead, and the Eastern Band is added as the Southeast source still to find.
- **Expert 7.1, underlining on all strips with sentences on two.** Codex 8 was followed with the grade 3 settlement (row 2: other code parts are judged from products made during the unit), because underlining only recognizes supplied text. The expert's minutes were adjusted to fit the new design.
- **Expert 4.1, tolerance of 1 cm on the zoom strip.** I used 5 mm, because at 1 cm a year a 1 cm tolerance cannot tell neighbouring years apart.
- **Expert 6.1, "maps 9" on day 131.** I used 10 (F3d 6, part prompts 4), because the full Southwest map has the most parts. The day still totals 35.
- **Expert CW2, dual-label line "in s06 field 8".** It is in s06 field 6, because field 8 would push s06 over the 1,250-word cap.
- **Expert 2.3, trade background "in field 2 Limits".** It is in s02 field 6, for the same cap reason.
- **Codex "Since Time Immemorial" rewrite option.** Not used; the line is deleted instead (see "Every unit").

Where the reads disagreed:
- **Unit 6:** both reads agree on a portfolio plus one full map, so I combined them.
- **Unit 7:** I followed Codex and the grade 3 settlement.
- **Unit 1:** I followed the grade 5 settlement ("None needed; retrieval only").

## Unverified
- **Billy Frank Jr. statue dedication.** The statue was installed in summer 2026. The dedication could not be confirmed, so it is not written.
- **St. Lawrence Iroquoian kinship note (s04 day 71).** From memory, and marked so. The sensitivity read must confirm which nations name this kinship.
- **Ute Mountain Tribal Park wording (s03).** From memory.
- **Equiano birthplace debate and the Buffalo Soldiers note.** From memory, though both are well established.
- **The Oregon Trail claim on day 86.** Not judged.
- **Unit 7 strip and exit statements.** Most are still from memory; the claim-to-source table marks which ones.
- **Unit 6 state atlas feature selections.** Still from memory, as the plan already says.

The checked facts are listed in the session record. They were checked against primary or wire sources and include:
- Carney, Sheinbaum and Charles III;
- the IEEPA ruling of 20 February 2026 and the USMCA review of 1 July 2026;
- the FEMA Review Council report of 7 May 2026, with nothing enacted;
- EO 14172;
- the Mexican court's staggered first terms;
- the MMF leaving the Métis National Council in 2021, and Afro-Mexican recognition (2019, widened 2024);
- the Mescalero Apache at Bosque Redondo, 1863 to 1865;
- the Norse date of 1021;
- Anza in 1774 and Domínguez and Escalante in 1776;
- the Whitman dates and PL 103-150;
- Puerto Rico in 1898;
- Mesa Verde's 26 associated tribes.

## For the structure pass
- **Assessment time budget.** Add the CW1 minutes rule to the plan writer's brief and to UNIT-PLAN.md field 7. Have a check flag assessment tables with more rows than their minutes allow.
- **Models-carried order.** scripts/unit_skeleton.py should sort "from" and "used again" by unit number, or reject a frame row whose first use comes after a later use.
- **Retrieval notes.** Add a check that every retrieval task a plan names is in the days.csv notes, and the reverse.
- **Current facts line.** The writer's brief should ask for a dated "as of" teacher line for living institutions, leaders, renamed places and court rulings.
- **Tennessee wording.** Change the template text that produces "blocked site not retried".
- **Since Time Immemorial.** Remove the line from the template or brief that produces it in every field 10.
- **Encoding.** The writer's output step turned é and ó into "?" in s05. Check its encoding.
- **MA.4.T4d.5 paraphrase.**
  - data/standards/ma-hss-2018.txt drops "early European exploration" from the anchor wording.
  - The progression row (data/progressions/social-studies.csv, ss4-state-maps) drops it too.
  - Restore it in both, then refresh the s06 skeleton line.
- **MA.4.T4.2 wording.** Codex flagged that the local wording needs checking against the anchor PDF.
- **Provisional section labels.** Section owners ("section 6.1" and others) are still provisional across the units.
- **Safe mechanical refresh (Codex 8 in its structure list).** Add a way to refresh skeleton blocks and day lists from the CSVs without rewriting the plan text. Here the day list rows for 64, 65, 73 and 111 were synced by hand.
- **Word cap.** At 1,250 words outside fields 4 to 6, background lines are pushed into field 6. Consider whether field 8 and field 2 teacher background should be exempt.

## For Cory
None.
