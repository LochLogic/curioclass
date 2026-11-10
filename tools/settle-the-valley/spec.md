# Settle the Valley

## One idea
Over fifty years in five decades, the child places homes, fields, a mill and roads for newcomer families in a river valley where people already live (a village on the high terrace, corn, beans and squash in river clearings, a spring fishing camp at the falls, hunting in the wooded hills), reads the resources on each part of the land (water power at the falls, rich soil on the bottomland, timber on the slopes), and watches the valley redraw each decade as land and people change each other: forests cleared, slope fields worn thin, a mill dam that stops the spring fish run, a mill town and a trading post where roads meet, and one flood year that forces the bottomland families to rebuild or move while the village on the terrace stays dry; at the end a then-and-now slider shows the valley's land and people at the start and the end, so a fourth grader learns how culture shapes the way people use land, how places change over time, why settlements grow where resources are, and how a disaster can move people.

## Not like
- hunter-to-farmer (6, concept): foraging versus farming in early human history. Here two ways of life in one valley over fifty years.
- state-story-timeline (4, concept): real state events. Here one made-up valley with real patterns.
- map-maker (3, spec): placing a town by reading land from above, once. Here placing over decades and seeing the land change back.
- then-and-now-overlay (3, spec): one real street in sources. Here a model valley across fifty years.

## Who and how
- Grade 4, Social Studies (Geography), module "Human-Environment Interaction". Standards: D2.Geo.4.3-5 (explain how culture influences the way people modify and adapt to their environments), D2.Geo.5.3-5 (explain how the cultural and environmental characteristics of places change over time), D2.Geo.8.3-5 (explain how human settlements and movements relate to the locations and use of various natural resources), D2.Geo.9.3-5 (analyze the effects of catastrophic environmental and technological events on human settlements and migration).
- Driver: one child alone (tool.json `driver: "student"`); `Read` reads every label and line. Controls 44 px or more.
- Five decades, then the then-and-now slider. Extra: Compare two runs (two saved runs side by side for a class). tool.json `modes: ["Valley", "Compare runs"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.
- Setting: an eastern North American river valley in the decades around 1800, made up but modeled on real Eastern Woodlands valleys (see Sensitivity note and Open questions). The page says so in a "How we made this valley" note.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.8.3-5 | Place each newcomer piece and read the resource that draws it there | resource labels on hover or tap (water power, rich soil, timber, a crossing); a reason line per placement | 2 |
| D2.Geo.4.3-5 | Open each group's "How we use the valley" card and match land uses to the group (seasonal fields and burns; plowed fields and fences) | the two cards and the valley map with each group's marks | 3 |
| D2.Geo.5.3-5 | Watch each decade redraw and tap three changes to name what caused them | the valley redrawn with forest, soil and fish counters; changes marked | 4 |
| D2.Geo.9.3-5 | Live the flood year: pick rebuild or move uphill for each bottomland family, then see who could and couldn't | the flood, the families' cards, the village on the terrace | 5 |

## Screens and modes
Header (kit): title "Settle the Valley"; `Valley`, `Compare runs`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The valley from a hilltop in spring: a river with falls at the upper end, wide flat bottomland along the river, a higher flat terrace on one side with a village, cornfields in clearings by the river, smoke from cooking fires, a fishing camp below the falls, wooded slopes rising to the hills. A decade dial reads "Decade 1". The welcome is queued (`welcomeAfter: true`): "This valley is already home to people who have lived here for a very long time. Two newcomer families arrive. Where should they build? Tap the land to see what's there." First hint: "Tap a part of the valley to see what it has."

**Each decade (focus: the valley and a tray).** At 1366x768 the valley fills the screen with the tray at the bottom and counters at the right; at 680x425 the counters fold into a `Counters` tab.
- Tapping land shows what it has: Falls (fast water that can turn a mill wheel; the first people's spring fishing place); Bottomland (rich dark soil, easy to plow, floods some years); Terrace (flat, above the flood line; the first people's village and fields); Slopes (timber, thin soil, steep); a river crossing (a shallow place to cross).
- The tray holds that decade's pieces: decade 1, two homes and two fields; decade 2, a mill, a road and one home; decade 3, two fields and a road; decade 4, the flood year (no pieces); decade 5, one home, one field and a road.
- Placing:
  - Homes and fields can go on the bottomland or the slopes. The terrace and the first people's clearings say: "This land is in use. It's the village's fields." (the piece returns). The narrator, the first time: "In many real valleys, newcomers took land like this, by treaties that were broken or unfair, or by force. In this valley, you'll build around it, and at the end you'll see what usually happened."
  - The mill fits only at the falls. Its reason: "Fast water turns the mill wheel to grind grain and saw logs." Its effect: a dam, and next decade the fish counter drops: "The dam blocks the fish swimming upriver in spring. The village's fishing camp catches far fewer."
  - Roads join homes; where two roads meet near the crossing, a trading post appears.
- Each group's card ("How we use the valley"):
  - The first people: move with the seasons (spring fishing at the falls, summer fields of corn, beans and squash in clearings, fall hunting in the hills, winter in the village); burn the underbrush in the woods to keep them open for hunting and travel; plant in clearings and let them rest.
  - The newcomers: stay in one place all year; clear the forest for plowed fields of wheat; build fences; cut timber for houses and the mill.
  - The child drags six land-use chips to the right card.

**Decade redraw.** At the end of each decade the valley redraws with three counters: Forest (percent of slopes wooded, starts at 80), Slope soil (good, thin, worn), Fish run (starts at 100). Rules: each slope field clears 5 from Forest and wears its soil after two decades; each home clears 5; the mill town cuts 5 more each decade after the mill. Three changes are marked with gold rings; the child taps each and picks its cause from two ("Fields on the slope let rain wash the soil away" / "The river moved").

**Flood year (decade 4).** A spring flood covers the bottomland. Each bottomland piece is damaged. Cards for each newcomer family on the bottomland ask `Rebuild` or `Move uphill`, and show who can:
- The mill family owns the mill and has savings: they can rebuild.
- The Platt family rents their farm: they can't afford to rebuild and move west to find new land (the card shows a road leaving the valley).
- A family with a slope field can move uphill, but the soil there is thin.
- The village on the terrace stays dry. Narrator: "The village was built above the flood line. The people here had watched this river for generations."

**Then and now (end state).** A slider from Decade 1 to Decade 5 shows land and people side by side: forest, fields, the fish run, the mill town and the trading post. Then a note card, read aloud: "In most real valleys like this, newcomers took most of the first people's land during these years, and many were forced to move far away. Their nations are still here today, and many still live in or near their homelands." Last, the child writes one sentence: "The valley changed because..." with three sentence starters. `Print` prints the then-and-now pair and the sentence.

**Compare runs (extra).** Two saved runs (stored only in this browser) side by side with their counters, for a class discussion.

## Content
- One valley with five land types and labeled resources; five decades with set trays; two group cards with six land-use chips; three counters with simple rules; three flood family cards; the end note.
- The valley, the newcomer families and the mill are made up; the land uses of both groups and the flood pattern follow real history (see Sources).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The tray shows only that decade's pieces. `Rebuild` and `Move uphill` show only in the flood year, and only for families that can choose. A family that can't is shown with its reason, not a grayed button.
- Keyboard: Tab through land parts and tray pieces; Enter to pick up and drop.
- With Motion off the redraw swaps without fading and the flood appears without rising water.

## Look
- Accent `--brand` #4a5d23 valley olive (header, the decade dial, counter frames); gold #f4c542 (the selected piece, change rings); paper #f5f7ef; ink #171e0a; muted #55594a.
- Contrast (WCAG 2.1, computed): white on brand 7.29:1; brand on paper 6.74:1; ink on paper 15.84:1; muted on paper 6.67:1; ink on gold 10.53:1.
- Never color alone: land types carry labels; counters carry numbers and words.
- Different from this batch (ripple blue, fix-it plum, barter ochre, skateboard berry).

## Art
- Local FLUX (`scripts/localart.py`): the valley from the hilltop in five decade states and the flood (6, 16:9, same framing so the redraw lines up); the first people's village shown from a distance as a living community (part of the scenes, no close faces, checked against museum and nation-published images for house types and fields).
- People art goes to Gemini with `people: true`: the three newcomer flood families (1 card each; cutout yes).
- Drawn in code: land hit areas, tray pieces, roads, counters, change rings, the slider, the cards.
About 9 images. The first people are not drawn close up in the default (see Open questions).

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the narrator; `casual-peer` as Ezra, the Platt family's kid, on the flood card. `Curio.voice` with `scope: () => state.mode + ':' + state.decade + ':' + state.piece`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each land reading.
- how `place`: "Drag a piece to the land that suits it."
- event, whole, each reason and effect line; `in-use` (first time whole, then short).
- how `cards`: "Drag each chip to the group that uses the land that way."
- how `changes`: "Tap a gold ring to say what changed it."
- event, whole, flood lines and Ezra's line.
- event, whole, `end-note`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: land types with resources, decade trays, placement rules, three counters with simple rules, the flood choices, the then-and-now slider.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Placement | Drop pieces anywhere | Each piece fits only where its resource is; reason lines name the resource. |
| Group cards | Put all chips on one card | Each card takes three; wrong drops say which way of life it fits. |
| Changes | Pick the first cause | Cause order shuffles; a wrong pick replays the before-and-after of that spot. |
| Flood | Rebuild everyone | Only the mill family can; the others' cards say why not. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Taps: land readings (whole).
2. Each decade: `place`; reason lines (whole); `in-use` once; `cards` in decade 1.
3. Redraw: `changes`; cause lines (whole).
4. Flood: flood lines (whole), Ezra (whole).
5. End: `end-note` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.4, 5, 8 and 9 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Eastern Woodlands peoples moved with the seasons, fished at falls in spring, farmed corn, beans and squash in clearings and hunted in fall | Smithsonian National Museum of the American Indian, "Native Knowledge 360" Eastern Woodlands materials | National Park Service, Native American seasonal round pages | yes |
| Native peoples used fire to keep eastern forests open | USDA Forest Service, "Fire and Native American land management" | National Park Service, "Fire in the eastern forest" | yes |
| Mill dams blocked spring runs of fish such as shad and salmon in eastern rivers | NOAA Fisheries, "Dams and fish passage" (river herring and shad) | U.S. Fish and Wildlife Service, Atlantic salmon restoration history | yes |
| Settlers cleared most of the forest in places like New England by the mid-1800s, and plowed slopes lost soil | Harvard Forest, "Land use history of New England" | USDA Natural Resources Conservation Service, soil erosion history | yes |
| Mills and towns grew at falls for water power | Library of Congress, "Industrial Revolution" mill town primary sources | National Park Service, Lowell National Historical Park | yes |
| Newcomers took most Native land through treaties, unfair sales and force, and many nations were removed; those nations continue today | National Museum of the American Indian, "Nation to Nation: Treaties" | National Archives, "Indian Removal" and treaty records | yes |
| Floods hit floodplain settlements hardest; renters and poorer families have fewer ways to recover | FEMA, "Floodplain management" | National Geographic Education, "Floodplain" | partly |
Backed twice: 7. Cut: 1. The renters-recover-less claim is backed by FEMA's recovery guidance only in general terms; the flood cards show it as one family's story, not a rule.

Sensitivity note: a real way of life is portrayed. The valley must never read as empty land; the first people are present from the first screen to the last, their use of the land is shown as skilled, and the end note tells what really happened and that they are still here. A fresh-agent read of the scenes, cards and end note is needed before build, and Cory decides whether to name a real nation (see Open questions).

Checks run (Python, scratchpad r6, 2026-11-09): with the default trays, Forest goes from 80 to no lower than 20 after all placements; each slope field wears its soil two decades after it's placed; the mill can only go at the falls and drops the fish run from 100 to 20 the decade after; three flood families split one rebuild, one move west, one move uphill; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 valley, tray and counters fit; at 680x425 counters are a tab.
2. Each piece fits only land with its resource, and its reason plays. (D2.Geo.8.3-5)
3. Six chips sort three to each group card. (D2.Geo.4.3-5)
4. Each decade redraws with the counters, and the three changes take their causes. (D2.Geo.5.3-5)
5. The flood year damages only bottomland pieces and shows who could rebuild, move uphill or leave. (D2.Geo.9.3-5)
6. The first people appear on every decade's scene, and the end note plays in full.
7. `Rebuild` and `Move uphill` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no fades or rising water; no network requests.

## Open questions
- Sensitivity flag: whether to model the valley on one real nation and place (for example a named Eastern Woodlands nation's homeland, with that nation's own materials and a consultant), and whether the first people speak in their own voice (default used: a made-up valley modeled on Eastern Woodlands patterns, no invented nation name, the first people described by the narrator, shown at a distance, and a fresh-agent read before build).
