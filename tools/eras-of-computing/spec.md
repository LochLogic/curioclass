# Eras of Computing

## One idea
A long timeline wall in a town library stretches across five era bands (war-time machines in the 1940s, mainframes in the 1950s to 1970s, personal computers from about 1975, the web from 1991, and phones and AI from 2007), and Mr. Okafor, the library's history volunteer (made up, labeled "illustration"), hands the child a pile of actor cards, a government code-breaking team, a university lab working for the army, a big business machine company, a hobby club swapping circuit boards, a garage start-up, a physics lab that shared the web for free, and a standards group, and the child drags each to its era and reads what it added and when; then the child follows one thread, the personal computer, as its effects appear one by one, the planned ones (working from home, learning at school) and the surprises (typing jobs shrinking, data about users piling up, old machines shipped abroad as e-waste), and sorts each as intended or surprise, helped or hurt, and who; finally the town council asks whether to allow drone delivery, and the child builds a case for or against from three patterns on the wall (who gains and loses jobs, whose privacy, where the old drones go) and hears two neighbors answer; at the end the child sees that many kinds of actors built computing and every new technology brings planned and unplanned effects, so judging a new one means asking the old questions, so a student in grades 6 to 8 learns who shaped computing, what it changed, and how to debate a new technology locally.

## Not like
- inventors-hall (3, spec): inventions and inventors. Here actors, effects and a local debate.
- cloud-through-time (Grades 9-12, spec): data centers through time. Here the whole history at middle school depth.
- algorithm-audit (Grades 6-8, spec): bias in a formula. Here effects of a technology over decades.
- family-tech-vote (3, spec): one family's gadget vote. Here a town's choice using history.

## Who and how
- Grades 6-8, Computer Science, module "Computing History and Impact". Standards: MS-SOC-HI-38, MS-SOC-HI-39, MS-SOC-ET-42 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Who shaped computing, what it changed, and debating a new technology locally").
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five eras, ten actor cards, eight effect cards for the personal computer, the council case. Extra: Council night (the class splits for and against on the projector). tool.json `modes: ["Timeline", "Council night"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-SOC-HI-38 | Place actor cards in eras; read what each added | the wall filling | 2 |
| MS-SOC-HI-39 | Sort the personal computer's effects | intended and surprise, helped and hurt | 3 |
| MS-SOC-ET-42 | Build a drone case from three patterns | two neighbors answering | 4 |

## Screens and modes
Header (kit): title "Eras of Computing"; `Timeline`, `Council night`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The library wall with five empty era bands, a pile of actor cards, and Mr. Okafor holding a punch card. The welcome is queued (`welcomeAfter: true`): "Lots of people built computing. Drag the first card to its era." First hint: "Drag the card to an era."

**Place (focus: the wall).** At 1366x768 the wall scrolls across the view with the card tray below; at 680x425 the wall shows one era at a time with arrows. A card that lands in the wrong era slides back with a date clue ("This club met from 1975 to 1986.").

**Follow one thread.** The personal computer's eight effects appear one at a time; the child sorts each on two switches (intended or surprise; helped or hurt) and names who it touched.

**Council.** The council's question appears; the child picks for or against and three patterns from the wall, then hears a neighbor who agrees and one who doesn't.

**Ask the old questions (the aha).** Mr. Okafor: "Every new machine, people planned some effects and got others. Ask who builds it, who it helps, and who it leaves behind."

**The end.** The wall, the sorted effects and the case. `Print` prints them.

**Council night (extra).** Class debate.

## Content
- Ten actors with dated examples named in each card's footnote (Bletchley Park's Colossus team, 1943 to 1945; the ENIAC team at the University of Pennsylvania, 1943 to 1946; IBM's mainframes, 1964; the Homebrew Computer Club, 1975 to 1986; a garage start-up, 1976; CERN's free web, 1991 and 1993; the W3C, 1994), with the women programmers named where sources do.
- Effects are stated as dated, sourced facts; the drone question is made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved until `Check the wall`; effects can be re-sorted until `Done sorting`.
- Keyboard: Tab to cards, eras (arrows choose an era), effect switches and case chips; Enter places or picks.
- With Motion off cards jump to their place.

## Look
- Accent `--brand` #2b3a67 timeline navy (header, era bands, buttons); gold #f4c542 (the card in hand, the council chair); paper #f1f2f7; ink #0d1226; muted #50535f.
- Contrast (WCAG 2.1, computed): white on brand 11.03:1; brand on paper 9.87:1; ink on paper 16.60:1; muted on paper 6.85:1; ink on gold 11.41:1.
- Never color alone: eras carry dates and names; effects carry words and icons.
- Different from this batch (debugger amber, factory red-orange, x-ray plum, test-kit green).

## Art
- Public domain photos where checked (Library of Congress, Smithsonian open access, U.S. Army ENIAC photos), credited on each card (about 6).
- People (illustrated): Mr. Okafor and two neighbors, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): era scenes where no checked photo exists (4, 4:3), the library wall (1, 16:9).
About 14 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Mr. Okafor; `news-reader` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag the card to an era."
- how `sort`: "Tap intended or surprise, then helped or hurt."
- how `who`: "Pick who it touched."
- how `case`: "Pick for or against, then three patterns."
- how `listen`: "Tap a neighbor to hear them."
- event, whole, ask the old questions.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: era bands with date checks, the effect sorter, the case builder, neighbor replies chosen by the patterns picked.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Place | Drop cards anywhere | Each card checks its dates. |
| Sort | Mark everything helped | Each effect has a right side backed by its source. |
| Case | Pick any three patterns | Each pattern must connect to a drone question. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`.
2. `sort`; `who`.
3. `case`; `listen`.
4. Ask the old questions (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Colossus at Bletchley Park (1943 to 1945) and ENIAC at the University of Pennsylvania (1943 to 1946), with women programming ENIAC | The National Museum of Computing, Colossus history | Computer History Museum, "Timeline of Computer History" and ENIAC programmers | yes |
| Homebrew Computer Club 1975 to 1986; the web made free by CERN in 1993 | Computer History Museum, "Timeline of Computer History" | CERN, "A short history of the Web" and the 30 April 1993 release | yes |
| Typing jobs shrank as personal computers spread | U.S. Bureau of Labor Statistics, Occupational Outlook Handbook history for typists and word processors | Monthly Labor Review (2003), "Occupational employment projections", declining clerical jobs | yes |
| Old computers have been shipped abroad as e-waste | Basel Action Network (2002), "Exporting Harm" | U.S. Government Accountability Office (2008), "Electronic Waste" report GAO-08-1044 | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s25, 2026-11-10): every card's dates fall inside its era band; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 wall and tray; at 680x425 one era at a time.
2. Ten actors are placed with what each added. (MS-SOC-HI-38)
3. Eight effects are sorted with who they touched. (MS-SOC-HI-39)
4. A drone case uses three patterns and hears both neighbors. (MS-SOC-ET-42)
5. Every photo is public domain and credited; every date matches its source.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: cards jump; no network requests.

## Open questions
- Data source for the era cards (default used: Computer History Museum timeline plus one second source per card, as in Sources; a full dated card list is checked at Build).
