# Mill Town

## One idea
The child plays Lucy, a young woman (made for this game) leaving her family's New England farm in 1834 for the textile mills of Lowell, Massachusetts: in branching chapters she chooses whether to go, how to spend or save her wages, whether to join the 1836 turnout against higher boardinghouse charges, whether to sign the 1845 petition for a ten-hour day, and whether to write for a workers' paper, while real events and short real words from mill workers frame each choice; a side panel shows each worker making far more cloth than a hand weaver could and cloth getting cheaper, and asks who shared the gain; at the end a change and continuity board and a means-of-change card compare the mill workers' tools (turnouts, petitions, newspapers) with today's, so an eighth grader learns what changed and what continued with the factory, how people pushed for reform then and now, and why living standards can rise as productivity improves.

## Not like
- factory-floor (9, concept): an owner's tycoon view. Here a worker's story.
- manor-life (7, spec): medieval work through seasons. Here factory work by the clock.
- levers-of-power (8, spec): modern civic action. Here 1830s and 1840s reform.
- reconstruction-amendments (8, spec): changing law after a war. Here workers pushing a state legislature.

## Who and how
- Grade 8, Social Studies (History, Civics and Economics), module "Reform and the Industrial North". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.Civ.14.6-8 (compare historical and contemporary means of changing societies, and promoting the common good), D2.Eco.13.6-8 (explain why standards of living increase as productivity improves).
- Format: story. Driver: one child alone, or the class voting at the turnout meeting (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Six chapters from 1834 to 1846, the productivity panel, the board and the means card. Extra: Class vote (the class votes at the 1836 meeting and at the petition table). tool.json `modes: ["Lucy's story", "Class vote"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.13.6-8 | Advance the productivity panel each chapter and answer who shared the gain (owners, workers, buyers) | yards per worker rising; the price of a yard falling; Lucy's wage line | 2 |
| D2.Civ.14.6-8 | Choose whether to join the turnout, sign the petition and write for the paper; then match each 1830s and 1840s tool to a present-day one | the choice results; the means-of-change card | 3, 5 |
| D2.His.2.6-8 | Sort eight cards into Changed and Continued | the board with reasons | 4 |

## Screens and modes
Header (kit): title "Mill Town"; `Lucy's story`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A farm kitchen in New Hampshire, 1834: a hearth, a spinning wheel no one uses much anymore, and on the table a recruiter's handbill for the Lowell mills and an open trunk. The welcome is queued (`welcomeAfter: true`): "Lucy is sixteen. The mills in Lowell pay cash wages to young women from farms like hers. Should she go? Tap the handbill." First hint: "Tap the handbill."

**Chapters (focus: the scene and choice).** At 1366x768 the scene fills the left with the productivity panel right; at 680x425 the panel is a tab.
1. Leave the farm (1834): go now or stay a year. The story goes on either way (if she stays, she leaves the next spring).
2. The boardinghouse and the bell (1834 to 1835): mill bells for waking, work and meals; days of about twelve hours, six days a week; a keeper's rules; wages of a few dollars a week, with board taken out. Choice: save, send money home, or buy a new dress and a library ticket.
3. The 1836 turnout: the company raises the charge for board, a cut in pay by another name. About 1,500 young women walk out. Choice: join or keep working. A real line from a worker who was there, read in short.
4. Writing (1840s): the Lowell Offering prints workers' stories; the Voice of Industry argues for workers' rights. Choice: write a story, write a protest, or neither.
5. The ten-hour petition (1845): the Lowell Female Labor Reform Association, led by Sarah Bagley, petitions the Massachusetts legislature; women testify at a hearing; the committee declines to act. Choice: sign, collect signatures, or stay out.
6. 1846 and after: more Irish immigrant workers take jobs in the mills as farm women leave; Lucy chooses her next step (stay, go home, move west, become a teacher).
- Each choice changes Lucy's savings, health and friendships, with a reason line.

**The productivity panel (D2.Eco.13.6-8).** Each chapter: yards of cloth per worker per day (a hand weaver about a few yards; a power-loom weaver tending two, then three or four looms, many times more), and the price of plain cotton cloth falling. The model is rounded and labeled "made for this game from historians' figures." A question each chapter: "Who got the gain this time: the owners (profits), the workers (wages), or buyers (cheaper cloth)?" with an answer from the record.

**The plain note.** A card: the cotton the mills spun was grown and picked by enslaved people in the South. Named plainly with a source; no images.

**The board (D2.His.2.6-8).** Changed (factory clocks replace farm seasons; women earn cash wages; cheaper cloth for everyone; new workers' papers) or Continued (families still depend on daughters' work; women can't vote; long hours; owners decide pay). Each sort plays a reason line.

**Means of change (the aha, D2.Civ.14.6-8).** The child matches each mill worker's tool to a present-day one: turnout to strike; petition to the legislature to online and paper petitions and testimony; workers' newspaper to social media and union newsletters; association to union. Then a line: "One tool that still works today is ___ because ___." Narrator: "They didn't win the ten-hour day in 1845. They kept pushing, and later workers did."

**The end.** Lucy's path, the panel, the board and the means card. `Print` prints them.

**Class vote (extra).** The class votes at the turnout meeting and at the petition table; Lucy follows the vote.

## Content
- Six chapters with choices and outcomes, short real worker quotes (under 15 words each, credited), the productivity panel model, the plain note, eight board cards, the means card.
- Lucy, her family and friends are made up and labeled; Lowell, the 1836 turnout, the papers, Sarah Bagley, the petition and the figures are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Choices branch Lucy's story; every branch reaches all six chapters.
- The panel updates after each chapter; its question waits for an answer.
- Keyboard: Tab to choices, the panel, board cards and the means card; Enter to choose.
- With Motion off looms don't move and bells don't swing.

## Look
- Accent `--brand` #8e3b2e mill brick (header, chapter banners, the panel); gold #f4c542 (the choice in hand, a sorted card); paper #fbf2ef; ink #2c0f0a; muted #62514c.
- Contrast (WCAG 2.1, computed): white on brand 7.46:1; brand on paper 6.77:1; ink on paper 16.15:1; muted on paper 6.80:1; ink on gold 10.94:1.
- Never color alone: panel lines carry labels and values; board columns carry words.
- Different from this batch (committee green, amendment indigo, colonial leather, transit teal).

## Art
- Public domain: an engraving of the Lowell mills (Library of Congress); a page of the Lowell Offering (Library of Congress or Harvard Library digital collections); a mill time table of bells (Lowell National Historical Park or Baker Library, checked at build). Each with credit.
- Local FLUX (`scripts/localart.py`): the farm kitchen (1, 16:9); a weave room with power looms (1, 16:9); a boardinghouse dining room (1, 16:9); the turnout in the street (1, 16:9); a legislative hearing room (1, 16:9).
- People art goes to Gemini with `people: true`: Lucy at three ages, her friend, a boardinghouse keeper, Sarah Bagley (from descriptions; no known portrait), an Irish immigrant worker (7; cutout yes).
About 15 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `big-sister` as Lucy's own voice. `Curio.voice` with `scope: () => state.mode + ':' + state.chapter + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each chapter scene.
- how `choose`: "Pick what Lucy does."
- event, whole, each result.
- how `panel`: "Who got the gain this time? Pick one."
- event, whole, the plain note.
- how `board`: "Drag each card to Changed or Continued."
- how `means`: "Match each old tool to one used today."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the branching story, Lucy's three meters, the productivity panel model, the board, the means card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Panel | Always answer "workers" | Each answer checks against the record; the reason line shows who gained. |
| Board | Put everything in Changed | Each card checks; "women can't vote" in Changed plays a reason line. |
| Means | Match at random | Each pair checks; the line needs a because. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Chapter scene (whole), waits; `choose`; result (whole).
2. `panel`; plain note (whole) in chapter 2.
3. `board`.
4. `means`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8, D2.Civ.14.6-8 and D2.Eco.13.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Young women from New England farms worked in Lowell's mills for cash wages, living in boardinghouses, about twelve hours a day | National Park Service, Lowell National Historical Park, "The Mill Girls" | Dublin, "Women at Work" (Columbia, 1979) | yes |
| The 1836 turnout of about 1,500 over higher board charges | Dublin (1979) | Robinson, "Loom and Spindle" (1898) | yes |
| The Lowell Offering and the Voice of Industry | Library of Congress, "The Lowell Offering" | National Park Service, Lowell NHP | yes |
| The 1845 ten-hour petition, Sarah Bagley, the hearing and the committee's refusal | Dublin (1979) | National Park Service, Lowell NHP, "Sarah Bagley" | yes |
| Power-loom weavers produced many times a hand weaver's output; cloth prices fell | Britannica, "Textile: the power loom" | Dublin (1979) | yes, rounded |
| Irish immigrants increasingly worked the mills from the late 1840s | National Park Service, Lowell NHP | Dublin (1979) | yes |
| Southern cotton spun in the mills was grown by enslaved people | National Park Service, Lowell NHP, "Cotton and slavery" | Beckert, "Empire of Cotton" (Knopf, 2014) | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the mills' dependence on cotton grown by enslaved people is named in one plain card with sources and no images. A fresh-agent read of that card is needed before build.

Checks run (Python, scratchpad r15, 2026-11-09): chapters in date order (1834, 1834 to 1835, 1836, 1840s, 1845, 1846); twelve hours a day for six days is 72 hours a week; every branch reaches chapter 6; four Changed and four Continued cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and panel; at 680x425 panel tab.
2. The productivity panel updates and asks who gained each chapter. (D2.Eco.13.6-8)
3. Six chapters branch on choices about the turnout, the paper and the petition. (D2.Civ.14.6-8)
4. The board sorts eight cards with reasons. (D2.His.2.6-8)
5. The means card matches old and new tools with a because. (D2.Civ.14.6-8)
6. Class vote steers the meeting and petition.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving looms; no network requests.

## Open questions
- Sensitivity flag: the mills' cotton came from enslaved people's labor (default used: one plain card with sources, no images, fresh-agent read before build).
