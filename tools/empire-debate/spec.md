# Empire Debate

## One idea
The student takes a seat in the U.S. Senate gallery in early 1899 as senators argue over the treaty with Spain that would make the Philippines an American colony, picks a side, and answers illustrated opponents round by round with real primary sources from two benches, the expansionists (Senator Henry Cabot Lodge, Albert Beveridge's 1898 "March of the Flag" speech, naval strategist Alfred Thayer Mahan, business petitions for Asian markets) and the anti-imperialists (Senator George Frisbie Hoar, the Anti-Imperialist League's platform, Andrew Carnegie's offer to buy the islands their freedom), where a debate meter rewards precise evidence and admitted weaknesses rather than volume; then a third bench opens with the voices the chamber mostly ignored (Emilio Aguinaldo's June 12, 1898 declaration of independence, the Malolos Republic's constitution, Filipino newspapers, soldiers' letters from the war that broke out two days before the vote); the vote passes 57 to 27, one vote more than needed, and an effects timeline follows the Philippine-American War, colonial rule and independence in 1946, beside Hawaii and Puerto Rico; at the end the student writes a closing argument that uses all three benches and names its own weak spot, so an eleventh grader learns to analyze complex causes and effects, how context shaped each writer's view, to integrate many sources into a reasoned argument, and to make claims with evidence while acknowledging counterclaims.

## Not like
- scramble-for-africa (9, spec): European empire on a map. Here an American vote on empire.
- supreme-court-simulator (12, concept): legal argument. Here a Senate debate.
- claim-repair-shop (10, spec): repairing others' claims. Here building one's own under fire.
- cold-war-crisis-room (10, spec): crisis choices. Here a debate with three benches.

## Who and how
- Grade 11, Social Studies (U.S. History), module "The U.S. as a World Power". Standards: D2.His.14.9-12 (analyze multiple and complex causes and effects of events in the past), D2.His.5.9-12 (analyze how historical contexts shaped and continue to shape people's perspectives), D2.His.16.9-12 (integrate evidence from multiple relevant historical sources and interpretations into a reasoned argument about the past), D4.1.9-12 (construct arguments using precise and knowledgeable claims, with evidence from multiple sources, while acknowledging counterclaims and evidentiary weaknesses).
- Format: roleplay. Driver: one student alone, or the class debating live with the same benches (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Six debate rounds, about twenty-four source cards on three benches, the vote, the effects timeline, the closing argument. Extra: Class debate (two teams argue live; the meter scores each answer the same way). tool.json `modes: ["Senate gallery", "Class debate"]`, `minutes: "40-50"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.1.9-12 | Answer each opponent's claim with a source, a counterclaim and a named weakness | the opponent's claim; the answer builder; the debate meter | 2 |
| D2.His.5.9-12 | Open each source's context card (who, when, why) and its "remembered today" line | the context card; Philippine memory today | 3 |
| D2.His.14.9-12 | Link causes (markets, naval bases, racial ideas, rivalry with Europe) to effects on the timeline | the cause tiles; the effects timeline | 4 |
| D2.His.16.9-12 | Write the closing argument with sources from all three benches | the closing builder with bench counters | 5 |

## Screens and modes
Header (kit): title "Empire Debate"; `Senate gallery`, `Class debate`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Senate chamber, February 1899, seen from the gallery. Two benches of source cards on either side: Expansionists and Anti-imperialists. A third bench at the back is covered with a cloth. A calendar reads February 1899. The welcome is queued (`welcomeAfter: true`): "The Senate is about to decide whether the United States will rule the Philippines. Choose a side, and argue it with evidence. Tap a bench." First hint: "Tap a bench to choose your side."

**Debate rounds (focus: the claim and the answer).** At 1366x768 the chamber fills the left with the answer builder right; at 680x425 the builder is a sheet. Six rounds; each opens with an illustrated opponent (a composite senator, labeled) making one claim from the other bench. The student builds an answer: a source card, a counterclaim, and a line naming a weakness in their own evidence. The meter scores precision (does the source say that?), relevance and an honest weakness; volume and repeated cards score nothing.
- Expansionist cards: Mahan's case for naval bases and coaling stations; business petitions for the China market; Beveridge's "March of the Flag" (1898) with its racial claims; Kipling's "The White Man's Burden" (published February 1899), framed as a source to analyze, not repeat; Lodge's Senate arguments; the cost of letting Germany or Japan take the islands.
- Anti-imperialist cards: the Anti-Imperialist League platform (1899); Hoar's Senate speech (January 1899) on consent of the governed; Carnegie's offer to pay $20 million, the price paid to Spain, for Philippine independence; labor fears of competition; racist arguments against annexation too, labeled so.

**The third bench (D2.His.5.9-12).** After round three the cloth lifts: Aguinaldo's declaration of independence (June 12, 1898); the Malolos Constitution and the First Philippine Republic (January 1899); Apolinario Mabini's writings; La Independencia newspaper; letters from Filipino and American soldiers after fighting began on February 4, 1899. Each card's context line names who wrote it, when and why, and a "remembered today" line notes that June 12 is the Philippines' Independence Day.

**The vote and effects (D2.His.14.9-12).** February 6, 1899: the treaty passes 57 to 27, one vote more than two-thirds. The effects timeline: the Philippine-American War (1899 to 1902, with fighting in some regions for years after); about 4,200 American soldiers and about 20,000 Filipino soldiers killed, and as many as 200,000 Filipino civilians dead from violence, famine and disease; the 1902 Senate hearings on torture; the Jones Act (1916); the Tydings-McDuffie Act (1934); independence on July 4, 1946. Beside it, Hawaii (annexed July 1898) and Puerto Rico (ceded by the same treaty). The student links each cause tile to its effects.

**The closing argument (the aha, D2.His.16.9-12).** "The Senate's decision was ___ because ___ [source]. The strongest case against me is ___ [source]. The voices left out show ___ [source]. My weak spot is ___." Bench counters show one source from each bench. Narrator: "Both sides in the chamber argued about the Philippines. Very few asked the Filipinos."

**The end.** The rounds, the timeline and the closing argument. `Print` prints them.

**Class debate (extra).** Two teams argue live with the same benches and meter.

## Content
- About twenty-four real source cards (excerpts under 15 words, credited), six composite opponents (labeled), the vote, the effects timeline, the closing builder.
- Racist period language is quoted only where a card needs it, briefly, framed with its context and labeled; atrocities are named in plain words with no images of bodies or torture.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- An answer needs all three parts before the round scores.
- The third bench opens after round three and must be used in the closing argument.
- Keyboard: Tab to benches, cards, the builder, the timeline and the closing; Enter to pick and place.
- With Motion off the cloth lifts without sliding and the meter jumps to its value.

## Look
- Accent `--brand` #7b3a10 Senate rust (header, benches, the meter); gold #f4c542 (the card in hand, a linked cause); paper #faf3ee; ink #24100a; muted #5f554f.
- Contrast (WCAG 2.1, computed): white on brand 8.55:1; brand on paper 7.79:1; ink on paper 16.58:1; muted on paper 6.60:1; ink on gold 11.19:1.
- Never color alone: benches carry names and icons; the meter carries a number and words.
- Different from this batch (olive drab, brain magenta, web teal, civic blue).

## Art
- Public domain political cartoons and photographs (Library of Congress, ids checked at build): Puck and Judge cartoons on annexation (themselves evidence, with their racist imagery framed and captioned); the Senate in 1899; Aguinaldo's portrait; American and Filipino soldiers. Each with credit.
- People (illustrated) for the six composite opponents, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the Senate gallery (1, 16:9).
About 14 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the composite opponents, introduced each time as "a senator's argument, built from real speeches"; `calm-professor` as the narrator, source reader and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each opponent's claim.
- how `answer`: "Pick a source, a counterclaim and your weak spot."
- event, whole, each source's context.
- event, whole, the vote.
- how `link`: "Link each cause to its effects."
- how `close`: "Write your closing argument from all three benches."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the debate rounds, answer builder, meter, three benches, the vote, the timeline, the closing builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rounds | Play the same card every round | Each round scores relevance to that claim; a repeat scores nothing. |
| Weak spot | Leave it blank or write "none" | The round won't score without a named weakness. |
| Closing | Use one bench | The counters need one source from each bench. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Opponent (whole), waits; `answer`.
2. After round three, the third bench's context (whole).
3. The vote (whole); `link`.
4. `close`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.9-12, D2.His.5.9-12, D2.His.16.9-12 and D4.1.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Senate approved the treaty February 6, 1899, 57 to 27 | U.S. Senate Historical Office, "The Senate Approves the Treaty of Paris" | Office of the Historian, U.S. Department of State, "The Philippine-American War" | yes |
| Fighting began February 4, 1899; deaths of soldiers and civilians | Office of the Historian, "The Philippine-American War, 1899-1902" | Library of Congress, "The World of 1898: The Spanish-American War" | yes |
| Aguinaldo's declaration of June 12, 1898; the Malolos Republic (January 1899) | National Historical Commission of the Philippines | Library of Congress, "The World of 1898" | yes |
| The Anti-Imperialist League platform; Carnegie's $20 million offer | Library of Congress, "The World of 1898" | Nasaw, "Andrew Carnegie" (Penguin, 2006) | yes |
| Beveridge's "March of the Flag" (1898); Hoar's Senate speech (1899) | Congressional Record, 55th Congress | Kramer, "The Blood of Government" (North Carolina, 2006) | yes |
| The 1902 Senate hearings on the war | U.S. Senate, Committee on the Philippines hearings (1902) | Kramer (2006) | yes |
| The Jones Act (1916), Tydings-McDuffie (1934), independence July 4, 1946 | Office of the Historian | National Archives | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the tool contains racist period rhetoric (in both camps) and wartime atrocities. Racist language is quoted briefly, only where a card needs it, with context and a label; atrocities are named plainly without images of bodies or torture. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r21, 2026-11-09): 57 of 84 votes is one more than two-thirds (56); the war began 2 days before the vote; independence came 47 years after the vote; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chamber and builder; at 680x425 sheet.
2. Each round's answer has a source, a counterclaim and a weak spot. (D4.1.9-12)
3. Every source opens a context card, and the third bench shows memory today. (D2.His.5.9-12)
4. Causes are linked to effects on the timeline. (D2.His.14.9-12)
5. The closing argument uses all three benches and names a weak spot. (D2.His.16.9-12)
6. Composite opponents are labeled; racist quotes are brief, framed and labeled.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
- Sensitivity flag: racist period rhetoric and wartime atrocities (default used: brief framed quotes only where needed, no images of bodies or torture, period cartoons captioned as evidence, fresh-agent read before build).
