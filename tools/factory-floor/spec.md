# Factory Floor

## One idea
The student runs a Lancashire cotton business (made for this game) from a cottage spinning wheel in 1760 to a steam-powered mill in 1900; each decade they spend profits on capital (the spinning jenny, the water frame, the mule, the steam engine, the power loom) or on human capital (training, a mechanics' institute, later schooling), and a productivity meter shows the hours it takes to spin 100 pounds of cotton fall from about 50,000 by hand to about 135 by the 1820s, while a real-wage line barely moves for decades and then climbs; a town layer grows around the mill (migrants from farms and from Ireland, terraces, a canal and a railway, disease, child labor and the Factory Acts, each with real figures), the supply line shows plainly that the raw cotton came from the U.S. South, grown by enslaved people, and a world map shows the machines spreading to other countries and pulling people there too; at the end a 1760 and 1900 split view and change and continuity cards show what rose, what workers paid, and what stayed the same, so a ninth grader learns change and continuity in the era, why investment in capital and skills raises growth and living standards, and how spreading technology moved people.

## Not like
- mill-town (8, spec): a Lowell worker's story. Here an owner's choices over 140 years.
- baron-or-builder (11, concept): judging industrialists. Here running the mill.
- printing-press (7, spec): one machine spreads ideas. Here many machines raise output.
- manor-life (7, spec): seasons on a medieval manor. Here decades in a mill town.

## Who and how
- Grade 9, Social Studies (World History, Economics and Geography), module "The Industrial Revolution". Standards: D2.His.2.9-12 (analyze change and continuity in historical eras), D2.Eco.13.9-12 (explain why advancements in technology and investments in capital goods and human capital increase economic growth and standards of living), D2.Geo.7.9-12 (analyze the reciprocal nature of how historical events and the spatial diffusion of ideas, technologies, and cultural practices have influenced migration patterns and the distribution of human population).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Fourteen decades, the productivity meter and real-wage line, the town layer, the supply line, the world map, the split view and the cards. Extra: Silk mill 1872 (Japan's Tomioka Silk Mill, built with French machines, shows the same technology spreading). tool.json `modes: ["Mill", "Silk mill 1872"]`, `minutes: "30-40"`, `grades_label: "Grade 9"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.13.9-12 | Each decade, choose a capital or human-capital investment and watch output per worker and real wages | the productivity meter; the real-wage line; the ledger | 2 |
| D2.Geo.7.9-12 | Follow migrants into the town and machines out to other countries on the world map, and link each move to its cause | the town layer; the world map with arrows | 3 |
| D2.His.2.9-12 | Sort cards into Changed and Continued, and read the 1760 and 1900 split view | the split view; the change and continuity board | 4 |

## Screens and modes
Header (kit): title "Factory Floor"; `Mill`, `Silk mill 1872`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A cottage in 1760: a spinning wheel, a basket of raw cotton, and a ledger: "Spin 100 pounds of cotton. How many hours of work will it take?" The student guesses; the answer appears: about 50,000 hours by hand. The welcome is queued (`welcomeAfter: true`): "This is Lancashire, England, 1760. You'll run a cotton business for 140 years. Every choice you make changes the work, the workers and the town. Open the ledger." First hint: "Tap the ledger."

**The decades (focus: the mill and the meters).** At 1366x768 the mill and town fill the left with the meters right; at 680x425 the meters are a tab. Each decade: one or two choices from the ledger, an event card, and the meters update.
- Capital: the spinning jenny (about 1765); Arkwright's water frame and his Cromford mill (1771); Crompton's mule (1779); Watt's rotary steam engine (1780s); the power loom (spreading from the 1820s); the self-acting mule (1825).
- Human capital: train mechanics; join the Manchester Mechanics' Institute (1824); later, schooling for the town's children. Skilled mechanics keep the machines running, and output rises more when they are there.
- The productivity meter shows hours to spin 100 pounds: about 50,000 by hand, about 2,000 on an early mule, about 135 on the self-acting mule. Rounded and labeled "from historians' estimates".
- The real-wage line: barely rising from about 1790 to 1840 (historians call this "Engels' pause"), then roughly doubling by 1900. Labeled as a rounded series with its source.
- The model behind profits and output is made for this game and labeled so.

**The town layer.** Every upgrade pulls people in: farm families, then Irish migrants, especially during the famine of 1845 to 1852. Terraces, a canal, a railway (Liverpool to Manchester, 1830). Event cards with real figures: Manchester grows from about 25,000 people in the 1770s to about 300,000 by 1850; children as young as five or six in mills; the 1833 Factory Act (no children under nine in textile mills, hours limits and inspectors); the 1842 Chadwick report, which found laborers in Manchester died at an average age of 17, mostly because so many children died; the 1847 Ten Hours Act.

**The supply line.** Raw cotton arrives by ship. A plain card: by the 1850s most of Lancashire's raw cotton came from the U.S. South, grown and picked by enslaved people. From 1861 to 1865 the U.S. Civil War cuts the supply and Lancashire mills go quiet (the cotton famine); many Lancashire workers back the Union anyway. Named plainly with sources; no images of enslaved people's suffering.

**The world map (D2.Geo.7.9-12).** Machines spread out from Lancashire (to Belgium, New England in the 1790s with Samuel Slater, Germany, India, Japan), and people move in (to Manchester) and out (British mechanics abroad). The student links each arrow to its cause.

**The split view and the board (the aha, D2.His.2.9-12).** 1760 and 1900 side by side: hours of work per pound, real wages, life in the town, who works. Then eight cards to sort into Changed (output per worker, real wages after 1840, schooling, the railway) or Continued (long hours for decades, the cotton supply's tie to slavery until 1865, owners deciding pay, women's lower wages). Narrator: "Over the long run, machines and skills made people far richer. The first generations paid for it."

**The end.** The ledger, the meters, the town, the map and the board. `Print` prints them.

**Silk mill 1872 (extra).** Japan's Tomioka Silk Mill: French machines and engineers, young women workers recruited from across Japan; the student finds what is the same and what is different.

## Content
- Fourteen decades of choices and events, the productivity and real-wage series, the town layer with about ten event cards, the supply line card, the world map with arrows, the split view, eight board cards, the Tomioka extra.
- The business and its owner are made up and labeled; machines, dates, laws, figures and places are real and sourced; series are rounded and labeled.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each decade waits for a choice; the student can't skip ahead.
- Picking only capital and never training slows output gains later, with a reason line.
- Keyboard: Tab to the ledger, choices, the town, the map and the board; Enter to choose and place.
- With Motion off machines don't spin and the town grows in steps.

## Look
- Accent `--brand` #3f4a55 mill soot (header, the ledger, meters); gold #f4c542 (the choice in hand, a sorted card); paper #f3f4f5; ink #121519; muted #555b61.
- Contrast (WCAG 2.1, computed): white on brand 9.04:1; brand on paper 8.21:1; ink on paper 16.63:1; muted on paper 6.24:1; ink on gold 11.26:1.
- Never color alone: meter lines carry labels and values; map arrows carry names.
- Different from this batch (ochre, cartographer blue, Atlantic indigo, field olive).

## Art
- Local FLUX (`scripts/localart.py`): the cottage (1, 16:9); the mill floor at four stages (4, 16:9); the town at four stages (4, 16:9); the Tomioka mill (1, 16:9).
- Public domain (Science Museum Group, Library of Congress, ids checked at build): engravings of the spinning jenny, the mule and power-loom weaving (Baines, 1835); a print of the Liverpool and Manchester Railway. Each with credit.
- People art goes to Gemini with `people: true`: the owner at three ages, a child piecer, a mechanic, an Irish migrant family, a Tomioka worker (7; cutout yes).
- Drawn in code: the ledger, meters, world map, board.
About 21 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as the narrator and event cards; `easy-coach` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.decade + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each event card.
- how `choose`: "Pick this decade's investment in the ledger."
- event, whole, each meter change.
- how `map`: "Link each arrow on the map to its cause."
- event, whole, the supply line card.
- how `board`: "Sort each card into Changed or Continued."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the decade ledger, the productivity model, the meters, the town layer, the world map, the split view and the board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Ledger | Pick the same choice every decade | Each machine buys once; skipping skills slows gains, with a reason line. |
| Map | Link arrows at random | Each link checks against its cause. |
| Board | Put everything in Changed | Each card checks; "long hours" in Changed plays a reason line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `choose`; event card (whole), waits; meter change (whole).
2. Supply line card (whole), in the 1850s decade.
3. `map`.
4. `board`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.9-12, D2.Eco.13.9-12 and D2.Geo.7.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Hours to spin 100 pounds: about 50,000 by hand, about 2,000 on an early mule, about 135 on the self-acting mule | Allen, "The British Industrial Revolution in Global Perspective" (Cambridge, 2009) | Catling, "The Spinning Mule" (1970), as cited by Freeman and Louca (Oxford, 2001) | yes, rounded |
| Machine dates: jenny about 1765, Cromford 1771, mule 1779, rotary engine 1780s, self-acting mule 1825 | Science Museum Group, cotton machinery collection | Britannica, "Textile: history" | yes |
| Real wages stalled about 1790 to 1840, then roughly doubled by 1900 | Allen, "Engels' pause," Explorations in Economic History (2009) | Feinstein, "Pessimism Perpetuated," Journal of Economic History (1998) | yes, rounded |
| The 1833 Factory Act and the 1847 Ten Hours Act | UK Parliament, Living Heritage, "The 1833 Factory Act" | UK National Archives, "Factory Acts" | yes |
| Chadwick's 1842 report: average age at death of laborers in Manchester 17 | Chadwick, "Report on the Sanitary Condition of the Labouring Population" (1842) | UK National Archives, education resources on public health | yes |
| Manchester grew from about 25,000 (1770s) to about 300,000 (1850) | Manchester City Council, local history | Britannica, "Manchester" | yes, rounded |
| Most of Lancashire's raw cotton came from the enslaved South by the 1850s; the cotton famine 1861-65 | Beckert, "Empire of Cotton" (Knopf, 2014) | UK National Archives, "Lancashire cotton famine" | yes |
| Tomioka Silk Mill (1872), French machines | UNESCO World Heritage, "Tomioka Silk Mill" | Tomioka City, mill history | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: child labor, early deaths and slavery in the cotton supply are shown with real figures and sources; the supply line card names enslaved people's labor plainly with no images of suffering; child workers appear at work, never hurt. A fresh-agent read of the event and supply cards is needed before build.

Checks run (Python, scratchpad r17, 2026-11-09): 50,000 hours to 135 is about 370 times faster; machine dates in order (1765, 1771, 1779, 1781, 1825); fourteen decades from 1760 to 1900; four Changed and four Continued cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 mill and meters; at 680x425 meters tab.
2. Each decade's choice moves the productivity meter and real-wage line, with skills mattering. (D2.Eco.13.9-12)
3. The town and world map link migration and spreading machines to causes. (D2.Geo.7.9-12)
4. The split view and board sort change and continuity. (D2.His.2.9-12)
5. The supply line card names slavery plainly once, with sources.
6. Silk mill 1872 loads with its comparison.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no spinning machines; no network requests.

## Open questions
- Sensitivity flag: child labor, early deaths and slavery in the cotton supply (default used: real figures with sources, slavery named plainly in one card with no images of suffering, children never shown hurt, fresh-agent read before build).
