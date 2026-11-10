# Who Has the Power?

## One idea
Six bins sit across a map that zooms from city hall to the world (local, state, tribal, federal, shared, international), and the student sorts 24 real power cards (print money, license drivers, run public schools, set a speed limit on a city street, regulate gaming on tribal land, make a treaty, declare war, collect sales tax, set voting rules) into the bins; each placement opens the source of that power (a clause of the Constitution, the Tenth Amendment, a state constitution, a treaty, tribal sovereignty) and a short real example; then a "moving line" round replays cards whose bin changed over time with the amendment, law or court case that moved them (voting after the 15th, 19th and 26th Amendments, the Voting Rights Act of 1965 and Shelby County v. Holder in 2013; tribal gaming after California v. Cabazon in 1987 and the Indian Gaming Regulatory Act of 1988; school funding after 1965; Real ID; sports betting after Murphy v. NCAA in 2018); at the end three contested cards (marijuana laws, immigration enforcement, regulating online platforms) are placed by the student, who then sees the strongest argument for each side and writes one sentence defending a choice, so a twelfth grader learns to distinguish the powers of local, state, tribal, national and international institutions and explain how the Constitution's powers and limits have changed over time and are still contested.

## Not like
- checks-and-balances (12, spec): branches of one government. Here levels of government.
- build-a-government (12, spec): designing a system. Here who holds which power now.
- bill-to-law-board-game (4, spec): state lawmaking. Here every level at once.
- supreme-court-simulator (12, spec): deciding one case. Here the cases that moved the lines.

## Who and how
- Grade 12, Social Studies (Civics), module "The Constitution and Federalism". Standards: D2.Civ.1.9-12 (distinguish the powers and responsibilities of local, state, tribal, national, and international civic and political institutions), D2.Civ.4.9-12 (explain how the U.S. Constitution establishes a system of government that has powers, responsibilities, and limits that have changed over time and that are still contested).
- Format: sort. Driver: one student alone, or the class sorting together on one screen (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- 24 power cards, six bins, six moving-line cards, three contested cards with arguments, the defense sentence. Extra: Class sort (a timed whole-class sort with the room's placements shown). tool.json `modes: ["Sort", "Class sort"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.1.9-12 | Sort 24 powers into six bins and read each power's source | the zooming map; the source card | 2 |
| D2.Civ.4.9-12 (changed over time) | Replay six cards whose bin moved, with the case or law | the timeline slider | 3 |
| D2.Civ.4.9-12 (still contested) | Place three contested cards, read both sides and defend a choice | the argument cards; the sentence | 4 |

## Screens and modes
Header (kit): title "Who Has the Power?"; `Sort`, `Class sort`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A map that starts on a city hall and pulls back to a state capitol, a tribal government building, the U.S. Capitol and the world. Six bins along the bottom: Local, State, Tribal, Federal, Shared, International. A card: "Print money." The welcome is queued (`welcomeAfter: true`): "Every rule you live under comes from somewhere. Sort each power to the level that holds it. Drag the card to a bin." First hint: "Drag the card to a bin."

**The sort (focus: the card and bins).** At 1366x768 the map fills the top with bins below; at 680x425 bins sit in two rows. Each placement opens a source card, for example:
- Print money: Federal; Article I, Section 8.
- License drivers: State; the Tenth Amendment's reserved powers and state law.
- Set a city street's speed limit: Local, under state law.
- Collect taxes: Shared (federal, state, local and tribal governments all tax).
- Regulate gaming on tribal land: Tribal and Federal, under the Indian Gaming Regulatory Act, with state compacts for casino gaming.
- Make a treaty: Federal; the President makes treaties with two-thirds of the Senate (Article II, Section 2); international bodies then apply them among nations.
- Tribal nations are governments with their own powers: more than 570 tribes are federally recognized, with relations rooted in treaties, the Constitution's Commerce Clause and cases from Worcester v. Georgia (1832) to McGirt v. Oklahoma (2020).
- A wrong bin opens the source card with "Not quite: here's where it comes from."

**The moving line.** A timeline slider replays six cards:
1. Who can vote: the 15th Amendment (1870), the 19th (1920), the Voting Rights Act (1965), the 26th (1971), Shelby County v. Holder (2013).
2. Gaming on tribal land: California v. Cabazon (1987), the Indian Gaming Regulatory Act (1988).
3. Public schools: state-run, then federal funding from the Elementary and Secondary Education Act (1965).
4. Driver's licenses as federal ID: the Real ID Act (2005), enforced at airports from May 7, 2025.
5. Sports betting: a federal ban struck down in Murphy v. NCAA (2018), now set by each state.
6. The drinking age: states, then a federal highway funding rule (1984), upheld in South Dakota v. Dole (1987).

**Contested today (the aha).** Three cards: marijuana laws (most states allow some use; federal law still lists it as a controlled substance), immigration enforcement (Arizona v. United States, 2012), regulating online platforms (state laws and federal law in tension). The student places each, reads the strongest argument on each side, and writes: "I'd put ___ in ___ because ___." Narrator: "The lines between levels were drawn in 1787. They've been redrawn ever since, and they're being argued over right now."

**The end.** The sorted map, the moving-line notes and the defense sentences. `Print` prints them.

**Class sort (extra).** The class sorts together on a timer; the room's placements show beside the sources.

## Content
- 24 power cards with sources and examples, six moving-line cards with dates and cases, three contested cards with arguments on each side, the sentence template.
- Contested cards present both sides fairly and take no position; tribal facts follow tribal and federal sources.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any card can be moved again before the round ends.
- Keyboard: Tab to the card, bins, slider and argument cards; number keys 1 to 6 choose a bin.
- With Motion off the map changes view without zooming and cards jump to bins.

## Look
- Accent `--brand` #34505e map slate (header, bins, the map); gold #f4c542 (the card in hand, the moving line); paper #f0f4f6; ink #0d1a20; muted #525c61.
- Contrast (WCAG 2.1, computed): white on brand 8.55:1; brand on paper 7.73:1; ink on paper 16.00:1; muted on paper 6.20:1; ink on gold 10.89:1.
- Never color alone: bins carry names and icons; source cards name the clause or case.
- Different from this batch (harvest ochre, clinic teal, clock blue, line crimson).

## Art
- Drawn in code: the zooming map, bins, cards, the slider.
- Generated (`scripts/localart.py`, about 24 small scenes without identifiable people, 4:3): one picture per power card (a mint, a license counter, a street sign, a casino floor, a treaty table).
About 24 images.

## Voice
Two bank voices, each unique in this batch: `bright-teacher` as the sorting guide and hints; `curious-librarian` as the reader of sources, cases and arguments. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag the card to a bin."
- event, whole, each source card.
- how `slide`: "Move the slider to see the line move."
- event, whole, each moving-line case.
- how `defend`: "Place the card, then write one sentence defending it."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the zooming map, bins, source cards, the slider, argument cards. Card data sits in a marked block `/* WHO-HAS-THE-POWER DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Drop everything in Shared | Each card checks against its source; Shared is right only for a few. |
| Moving line | Skip the slider | The contested round opens after all six cards are replayed. |
| Defense | Write "it's complicated" | The sentence needs a bin and a reason tied to a source or argument. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`; source card (whole).
2. `slide`; moving-line cases (whole), waits.
3. `defend`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.1.9-12 and D2.Civ.4.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Coining money (Art. I, Sec. 8); treaties with two-thirds of the Senate (Art. II, Sec. 2); the Tenth Amendment | National Archives, "The Constitution of the United States" | Congress.gov, "Constitution Annotated" | yes |
| More than 570 federally recognized tribes; tribal sovereignty | Bureau of Indian Affairs, "Federally Recognized Indian Tribes" | National Congress of American Indians, "Tribal Nations and the United States" | yes |
| Worcester v. Georgia (1832); McGirt v. Oklahoma (2020) | Oyez, case pages | Supreme Court of the United States, opinions | yes |
| California v. Cabazon (1987); the Indian Gaming Regulatory Act (1988) | National Indian Gaming Commission, "About IGRA" | Oyez, "California v. Cabazon Band of Mission Indians" | yes |
| 15th (1870), 19th (1920), 26th (1971) Amendments; VRA (1965); Shelby County (2013) | National Archives, amendment records | U.S. Department of Justice, "Voting Rights Act" history | yes |
| Real ID Act (2005), enforced May 7, 2025 | Department of Homeland Security, "REAL ID" | TSA, "REAL ID" | yes |
| Murphy v. NCAA (2018); South Dakota v. Dole (1987); Arizona v. United States (2012) | Oyez, case pages | Congress.gov, "Constitution Annotated" | yes |
| Elementary and Secondary Education Act (1965) | U.S. Department of Education, "ESEA" history | National Archives, "Elementary and Secondary Education Act" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: tribal sovereignty is shown as government-to-government, in tribal and federal sources' terms, never as a special privilege; contested cards give both sides fairly; a fresh agent reads the tribal cards before build.

Checks run (Python, scratchpad r24, 2026-11-09): the 26th Amendment was ratified 100 days after Congress passed it (March 23 to July 1, 1971); IGRA came one year after Cabazon; two-thirds of 100 senators is 67; each of six moving-line cards has at least one dated law or case; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and bins; at 680x425 two rows.
2. 24 powers sort into six bins with a source card each. (D2.Civ.1.9-12)
3. Six moving-line cards replay with their laws and cases. (D2.Civ.4.9-12)
4. Three contested cards show both sides and take a defense sentence. (D2.Civ.4.9-12)
5. Tribal cards use tribal and federal sources; contested cards take no position.
6. Wrong placements open the source with a kind correction.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no zoom; no network requests.

## Open questions
- Sensitivity flag: tribal sovereignty facts and contested powers (default used: government-to-government framing from tribal and federal sources, both sides on contested cards, fresh-agent read before build).
