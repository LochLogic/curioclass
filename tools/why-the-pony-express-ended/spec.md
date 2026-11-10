# Why the Pony Express Ended

## One idea
A station keeper's desk at dusk holds a locked case file ("Why did the riders stop?") and eight evidence cards from 1860 and 1861 and later (a rate poster, the first telegram across the country, a cost ledger, a newspaper notice, the company owner's memoir, a rider's story, a route map, a Congress mail law); the child opens each card, highlights the line that matters, and pins it under a claim stem ("The Pony Express ended because..."), where every reason needs two cards from different kinds of sources before it locks, then answers a skeptical editor who says "The telegraph alone explains it!" by pointing to the ledger, so a fifth grader learns to build a claim from multiple sources and that the famous answer is only half the story: the company was losing money from the start.

## Not like
- source-scout (5, spec): choosing and rating sources before a claim. Here building and defending the claim.
- evidence-corkboard (8, concept): adds what evidence can't show. Here two sources per reason.
- resource-detective (2, concept): a mystery tracing objects. Here an argument about causes.
- mongol-messenger (concept): relay riders as a race. Here why a relay service ended.
- Look apart from detective tools: a station ledger by lantern light, not a detective office.

## Who and how
- Grade 5, Social Studies (History and Inquiry), module "Why the Pony Express Ended". Standards: D2.His.16.3-5 (use evidence to develop a claim about the past), D3.3.3-5 (identify evidence that draws information from multiple sources in response to compelling questions), D3.4.3-5 (use evidence to develop claims in response to compelling questions), D4.1.3-5 (construct arguments using claims and evidence from multiple sources).
- Format: mystery. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three parts: Open the cards, Build the claim, Answer the editor. Extra: Print the argument (a one-page claim with cited cards). tool.json `modes: ["Case file", "Print the argument"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D3.3.3-5 | Highlight the key line on each card and pin it under a reason; each reason needs two cards of different kinds | the reason slots with two pins each and kind badges | 3 |
| D3.4.3-5 | Choose which reasons stay as evidence comes in; a reason with only one kind of source or none drops out | reasons lock, wait or fade | 4 |
| D2.His.16.3-5 | Finish the claim stem with the locked reasons | the claim sentence on the case file | 4 |
| D4.1.3-5 | Answer the editor's challenge by pointing to a card | the editor's three challenges and the child's cited answer | 5 |

## Screens and modes
Header (kit): title "Why the Pony Express Ended"; `Case file`, `Print the argument`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A relay station at dusk in Nebraska Territory, a lantern on the desk, a locked case file ("Why did the riders stop? October 1861") and eight face-down cards. The station keeper, Mrs. Ellery (made for this game), sets down a cup. The welcome is queued (`welcomeAfter: true`): "The Pony Express ran for about eighteen months, from April 1860 to October 1861. Then it stopped. Why? Turn over a card to start." First hint: "Tap a card to turn it over."

**Open the cards (focus: one card at a time).** At 1366x768 the desk shows all eight cards with the open card large in the middle; at 680x425 one card fills the screen with a strip of eight small cards below.
Each card shows its kind badge (poster, telegram, ledger, newspaper, memoir, rider's story, map, law), its date and its maker. The child highlights the line that matters (two to four lines per card, one or two that matter).
1. Rate poster, 1860 (real): letters cost $5 for each half ounce. Key line: the price.
2. The first telegram across the country, October 24, 1861 (real): California's chief justice, Stephen J. Field, telegraphs President Lincoln. Key line: the message arrives the same day.
3. Cost ledger (made for this game from historians' totals): money in from letters about $90,000 to $100,000 a year; money out for about 400 horses, about 80 riders, and about 150 to 190 stations, much more; the company lost about $200,000 in all. Key line: money out far more than money in.
4. Newspaper notice, Sacramento, October 1861 (real, quoted short): the Pony Express will stop now that the telegraph is through. Key line: the reason given at the time.
5. Memoir, Alexander Majors, "Seventy Years on the Frontier" (1893, real): one of the three owners writes that the Pony Express did not pay. Key line: it didn't pay.
6. Rider's story, "Pony Bob" Haslam (real, told later): in May 1860 during the Pyramid Lake War he rode about 380 miles round trip when stations were burned; the war cost the company over $70,000. Key line: war damage cost money.
7. Route map (real, 1860s): St. Joseph, Missouri, to Sacramento, California, about 1,800 to 1,966 miles, about ten days. Key line: ten days.
8. Congress mail law, March 2, 1861 (real): the central route mail contract goes to the Overland Mail Company; the Pony Express runs only as its partner from July 1861, at $1 a half ounce. Key line: they didn't get the contract on their own.

**Build the claim (focus: the case file).** The case file shows the claim stem "The Pony Express ended because..." and five reason slots:
- The telegraph sent messages in minutes (cards 2 and 4: telegram, newspaper).
- It cost more to run than it earned (cards 3 and 5: ledger, memoir; card 1 helps: even at $5 few people could pay).
- War damage added huge costs (cards 6 and 3: rider's story, ledger).
- It never won its own government mail contract (cards 8 and 5: law, memoir).
- Riders quit because the job was too dangerous (a weak reason: only one known rider ever refused a run; no card backs it, so it fades).
- Each pinned highlight shows its kind badge. A reason locks with two cards of different kinds. Two cards of the same kind: "Both are newspapers. Find a different kind of source." A reason with no support fades: "No card backs this. Drop it?"
- As reasons lock, the claim sentence rewrites itself, joining them: "The Pony Express ended because the telegraph made it too slow to need, and because it cost more to run than it ever earned."

**Answer the editor (the aha).** Mr. Booth, a skeptical newspaper editor (made for this game), challenges three times:
1. "The telegraph alone explains it!" The child points to the ledger (or memoir): it was losing money long before the telegraph. Mr. Booth: "Hm. So the telegraph finished off something already in trouble."
2. "Then why did it run at all?" The child points to the map (ten days instead of weeks by stagecoach and ship) and the poster (people paid for speed).
3. "How do you know the ledger is right?" The child points to the memoir (an owner said it didn't pay): two different kinds of sources agree.
A wrong card plays "Does that card answer what he asked?" Narrator at the end: "Strong claims name more than one cause, and each cause stands on more than one source."

**The end.** The case file unlocks: the final claim, its reasons and pinned cards. `Print` prints the claim as a one-page argument.

**Print the argument (extra).** The final claim, each reason with its two cited cards (kind, date, maker), and the editor's answers, laid out as one page.

## Content
- Eight evidence cards (seven real documents, quoted briefly or summarized, and one ledger made for this game from historians' totals and labeled so), five reasons (four supported, one weak), three editor challenges, the claim joiner.
- Mrs. Ellery and Mr. Booth are made up and labeled; Stephen Field, Alexander Majors, Bob Haslam and the documents are real.
- Numbers shown as historians give them, with ranges where sources differ (route miles, total loss).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Highlight by tapping a line; drag the highlight (or tap-then-place) onto a reason slot.
- Reasons can be dropped by the child; a dropped reason can be brought back.
- Keyboard: Tab to cards and lines; Enter to highlight; arrows choose a reason; Enter to pin.
- With Motion off cards turn without flipping and the lantern doesn't flicker.

## Look
- Accent `--brand` #7a2e0e saddle rust (header, kind badges, reason slots); gold #f4c542 lantern light (the highlighted line, a locked reason); paper #f7efe4 ledger paper; ink #26110a; muted #5f5045.
- Contrast (WCAG 2.1, computed): white on brand 9.44:1; brand on paper 8.28:1; ink on paper 15.79:1; muted on paper 6.77:1; ink on gold 11.06:1.
- Never color alone: locked reasons carry a lock icon and the word "Locked"; kind badges carry words.
- Different from this batch (scout amber, revolution navy, rights plum, change teal).

## Art
- Public domain, checked at spec (Library of Congress and Smithsonian National Postal Museum): an 1860 Pony Express rate poster; a Pony Express route map; a Sacramento Daily Union page, October 1861; a Pony Express cover (envelope) with the $5 stamp. Each with credit.
- People art goes to Gemini with `people: true`: Mrs. Ellery the station keeper (2 poses; cutout yes), Mr. Booth the editor (2 poses; cutout yes), a rider at full gallop (1).
- Local FLUX (`scripts/localart.py`): the relay station at dusk (1, 16:9); the desk under lantern light (1, 16:9).
- Drawn in code: the cards, kind badges, the case file, reason slots, the ledger card.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as Mrs. Ellery, the narrator who reads the cards; `news-reader` as Mr. Booth the editor. `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `turn`: "Tap a card to turn it over."
- event, whole, each card.
- how `mark`: "Tap the line that matters most."
- how `pin`: "Drag your line onto a reason."
- event, whole, the same-kind and no-support hints.
- event, whole, the claim as it rewrites.
- how `answer`: "Tap the card that answers Mr. Booth."
- event, whole, each challenge and reply.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the card desk with highlightable lines, reason slots with a two-kinds rule, the claim joiner, the editor's challenges.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Two sources | Pin two newspapers to one reason | Same kind doesn't lock; the hint asks for a different kind. |
| Claim | Lock only the telegraph | The editor's first challenge can't be answered from telegraph cards; the narrator points to the ledger. |
| Weak reason | Keep "riders quit" | No card backs it; it stays faded and isn't in the claim. |
| Editor | Tap cards at random | A wrong card plays the hint; each challenge has one or two right cards. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `turn`.
2. Cards (whole), each waits. `mark`, `pin`; hints (whole); claim (whole).
3. `answer`; challenges and replies (whole), each waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.16.3-5, D3.3.3-5, D3.4.3-5 and D4.1.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Ran April 3, 1860, to October 1861; about 1,800 or more miles; about ten days | National Park Service, Pony Express National Historic Trail, "History and culture" | Pony Express National Museum, historical timeline | yes |
| Transcontinental telegraph completed October 24, 1861; service ended days later | Pony Express National Museum, timeline | National Park Service, Pony Express NHT | yes |
| $5 per half ounce at the start; $1 per half ounce from July 1, 1861 | Smithsonian National Postal Museum, "Moving the Mail: The Pony Express" | USPS Historian, "The Pony Express" (PDF) | yes |
| The company lost money (about $200,000 is the common figure; estimates run higher) | Encyclopedia of the Great Plains (University of Nebraska), "Pony Express" | Encyclopaedia Britannica, "Pony Express: Final days" | yes, figures vary, shown as "about" |
| The Pyramid Lake War (May to June 1860) cost the company over $70,000; Bob Haslam's long ride | Pony Express National Museum, timeline | National Park Service, Pony Express NHT, riders | yes |
| March 2, 1861 law: central mail contract to the Overland Mail Company; Pony Express as its partner from July 1861 | Pony Express National Museum, timeline | USPS Historian, "The Pony Express" | yes |
| Alexander Majors's memoir says it did not pay | Majors, "Seventy Years on the Frontier" (1893), public domain | Wornall/Majors House Museums, "Alexander Majors and the Pony Express" | yes |
| Only one known rider refused a run | Pony Express National Museum, timeline (Johnson Richardson, May 1860) | National Park Service, riders page | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-09): April 3, 1860, to October 26, 1861, is about 19 months, so "about eighteen months" holds for regular service; $5 down to $1 is an 80 percent cut; each of the four real reasons has two cards of different kinds and the weak reason has none; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 all eight cards on the desk; at 680x425 one card with a strip.
2. Every card shows its kind, date and maker; the ledger says "made for this game".
3. A reason locks only with two cards of different kinds. (D3.3.3-5)
4. The claim rewrites as reasons lock; the weak reason never locks. (D3.4.3-5, D2.His.16.3-5)
5. Each editor challenge is answered by pointing to a card. (D4.1.3-5)
6. Print the argument lays out the claim with cited cards.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flipping or flicker; no network requests.

## Open questions
None.
