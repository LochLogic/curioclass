# Family Tech Vote

## One idea
Around a kitchen table with five chairs and a gadget box in the middle, a made-up family (labeled "illustration") is voting on one new gadget, a smart speaker, a fitness watch or a doorbell camera, and the child sits in each seat in turn: Grandpa Ray, who lives with them and likes the camera for safety; the teen, Imani, who doesn't want the watch tracking her; a parent who works nights; the little brother; and the next-door neighbor, Mrs. Cho, whose sidewalk the camera also films though she never gets a vote; at each seat four cards flip, what it helps, what data it collects, what it costs the planet, and who it leaves out, and the data card shows what the gadget records, how often, and that it is stored on the company's computers, not just at home; each seat's lean lands on a tally, and the child casts the deciding vote with a reason built from cards they flipped, including at least one benefit and one harm; fifth graders then change one setting (record less, keep it on the device) and watch the data card shrink; at the end the child sees that the same gadget is a yes for one person and a no for another, and that the data can reach people who never voted, so a student in grades 3 to 5 learns to weigh the benefits, risks, data and planet costs of a new device for different people.

## Not like
- data-policy-council (Grades 9-12, spec): privacy law. Here one family's choice.
- design-for-a-friend (5, spec): user interviews for a design. Here weighing a device someone else made.
- algorithm-audit (Grades 6-8, spec): bias in a formula. Here trade-offs of a gadget.
- three-route-rules (3, spec): who rules help. Here who a gadget helps.

## Who and how
- Grades 3-5, Computer Science, module "New Tech: Yes or No?". Standards: E3-SOC-ET-17, E4-DAT-IM-11, E4-SYS-IM-15, E5-SOC-ET-17, E5-DAT-IM-11 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Benefits, risks, data and the planet when a family weighs a new gadget").
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three gadgets, five seats, four cards per seat, the tally, the deciding vote, two settings. Extra: Family meeting (five students each take a seat; one device). tool.json `modes: ["Vote", "Family meeting"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-SOC-ET-17, E5-SOC-ET-17 | Sit in each seat; cast and explain the deciding vote | the tally; a reason with a benefit and a harm | 2 |
| E4-DAT-IM-11 | Read the data card; say who could see the data | data leaving the house | 3 |
| E4-SYS-IM-15 | Read the routine and planet card | always-on power; a short life | 3 |
| E5-DAT-IM-11 | Change a setting; read the new data card | the card shrinking | 4 |

## Screens and modes
Header (kit): title "Family Tech Vote"; `Vote`, `Family meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A warm kitchen at dinner time, five chairs around a table, a plain gadget box in the middle, and Grandpa Ray holding the instruction leaflet. The welcome is queued (`welcomeAfter: true`): "We're voting tonight. Pick the gadget we're voting on." First hint: "Tap a gadget."

**Sit (focus: the table).** At 1366x768 the table fills the left with the seat's cards on the right; at 680x425 the cards are a sheet. The child taps a chair; that person speaks one line about how they feel. Four face-down cards flip one by one.

**Data card.** Shows what is recorded (sound after the wake word, heart rate every few minutes, video on motion), how often, and where it is kept, with a picture of the data leaving the house.

**Tally.** Each seat's lean (yes, no, unsure) lands on the tally; Mrs. Cho's lean shows in gray with "can't vote".

**Deciding vote.** The child picks yes or no and builds a reason from flipped cards; the reason needs a benefit and a harm.

**Settings (grade 5).** Two settings: record less, keep data on the device. The data card redraws, and seats may change their lean.

**Yes for one, no for another (the aha).** Narrator: "One gadget, five answers. And the data reached someone who never voted."

**The end.** The tally, the reason and the data card. `Print` prints them.

**Family meeting (extra).** Seats for real students.

## Content
- Generic gadgets with no brand marks; data facts are typical, labeled "how many gadgets like this work".
- The family is multigenerational and labeled "illustration"; no seat is made the villain.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Seats can be revisited; the vote can be changed until `Cast vote`.
- Keyboard: Tab to gadgets, chairs, cards, tally, reason chips and settings; Enter flips or picks.
- With Motion off cards appear face up.

## Look
- Accent `--brand` #8a3a2a kitchen-table rust (header, the tally, buttons); gold #f4c542 (the seat in focus, the deciding vote); paper #faf0ed; ink #2a0d07; muted #5d4f4b.
- Contrast (WCAG 2.1, computed): white on brand 7.72:1; brand on paper 6.90:1; ink on paper 16.18:1; muted on paper 6.98:1; ink on gold 11.14:1.
- Never color alone: leans show words and thumbs; card types have icons.
- Different from this batch (circuit blue, corkboard violet, ramp green, helper teal).

## Art
- People (illustrated): five family members and Mrs. Cho, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the kitchen (1, 16:9), three generic gadgets (3, 1:1).
- Drawn in code: cards, the tally, the data path and the reason builder.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Grandpa Ray; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.gadget + ':' + state.seat + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `gadget`: "Tap a gadget."
- how `sit`: "Tap a chair to sit there."
- how `flip`: "Tap a card to flip it."
- how `vote`: "Tap yes or no, then add a benefit and a harm."
- how `setting`: "Tap a setting to change it."
- event, whole, yes for one, no for another.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: seats with leans per gadget, card decks, the data card with settings, the reason builder.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seats | Vote from one seat | The vote opens after all five seats. |
| Reason | Pick only benefits | The reason needs one benefit and one harm. |
| Settings | Tap without reading | The child names what changed on the data card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `gadget`; `sit`; `flip`.
2. `vote`.
3. `setting`.
4. Yes for one, no for another (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Smart home devices collect data that is often stored by the company, and settings can limit it | Federal Trade Commission, "Internet of Things: Privacy and Security in a Connected World" (2015) | Common Sense Media, "Smart speakers and privacy" guidance for families | yes |
| Always-on electronics use standby power, and short device lives add e-waste | U.S. Department of Energy, "Standby Power" | U.S. Environmental Protection Agency, "Cleaning Up Electronic Waste (E-Waste)" | yes |
| Doorbell cameras can record neighbors and public sidewalks | Electronic Frontier Foundation, guidance on home cameras | UK Information Commissioner's Office, "Domestic CCTV systems" guidance | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s24, 2026-11-10): five seats with four cards each is 20 cards per gadget, 60 in all; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and cards; at 680x425 cards as a sheet.
2. All five seats are visited and the deciding vote is explained with a benefit and a harm. (E3-SOC-ET-17, E5-SOC-ET-17)
3. The data card and the planet card are read, and who could see the data is named. (E4-DAT-IM-11, E4-SYS-IM-15)
4. A setting is changed and its effect on the data card explained. (E5-DAT-IM-11)
5. No brand marks; no seat is the villain.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: cards appear face up; no network requests.

## Open questions
None.
