# Resource Map

## One idea
A map of the United States carries four switchable geology layers (old seas, buried swamp forests, old volcanic zones, porous rock) and four resource cards (oil, coal, copper, groundwater); for each resource the student reads a short "how it forms" story (oil from sea plankton buried and cooked over millions of years, coal from swamp forests buried about 300 million years ago, copper ore from hot fluids near old volcanoes, groundwater held in porous rock and refilled by rain), turns on the layers that matter, drops prediction pins where the resource should be, then reveals the real deposits and sees how close the pins came; human side cards show towns that grew around mines and farms that pump the High Plains aquifer faster than rain refills it; at the end the student explains one resource's uneven map with the processes behind it, so a seventh grader learns to construct a scientific explanation based on evidence for how the uneven distributions of Earth's mineral, energy and groundwater resources are the result of past and current geoscience processes.

## Not like
- plate-puzzle (6, spec): evidence that plates moved. Here what old seas, swamps and volcanoes left behind.
- population-dashboard (12, spec): resource use by country. Here why resources are where they are.
- biome-atlas (12, spec): climate and biomes. Here rocks and what they hold.
- made-from (7, concept): how products are made from resources. Here where the resources come from.

## Who and how
- Grade 7, Science, module "Earth's Resources". Standard: MS-ESS3-1 (construct a scientific explanation based on evidence for how the uneven distributions of Earth's mineral, energy, and groundwater resources are the result of past and current geoscience processes).
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One map, four layers, four resources with three pins each, the reveal, two human side cards, the explanation card. Extra: World view (the same layers on a world map). tool.json `modes: ["Map", "World view"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS3-1 (past processes) | Read the forming story and switch on the matching layer | the layer; the story card | 2 |
| MS-ESS3-1 (distribution) | Pin predictions and reveal real deposits | pins against deposits; the match count | 3 |
| MS-ESS3-1 (current processes, explanation) | Read the aquifer card and explain one resource's map | the High Plains card; the explanation card | 4 |

## Screens and modes
Header (kit): title "Resource Map"; `Map`, `World view`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A plain map of the lower 48 states, a stack of four layer switches and four resource cards face down. The welcome is queued (`welcomeAfter: true`): "Why is there coal in some places and not others? The rocks remember. Flip the oil card." First hint: "Tap the oil card."

**A resource (focus: the map).** At 1366x768 the map fills the left with the cards and switches right; at 680x425 the switches and cards are a sheet. The forming story plays in three short frames. The student switches layers on and off; then drops three pins. `Reveal` shows the real deposits as shaded areas; each pin inside one counts. A card asks which layer helped most.

**Four resources.** Oil: old seas (the Gulf Coast, the Permian Basin in Texas, the North Slope of Alaska as an inset). Coal: buried swamp forests (Appalachia, the Illinois Basin, Wyoming's Powder River Basin). Copper: old volcanic zones (Arizona, Utah's Bingham Canyon, Montana's Butte). Groundwater: porous rock and sand (the High Plains aquifer under parts of eight states, the Floridan aquifer).

**Human side.** Butte, Montana grew around copper mines. Farms on the High Plains pump water faster than rain refills it, and in parts of Kansas and Texas water levels have dropped by more than 100 feet. The card shows a well's water level falling over the years.

**The explanation card (the aha).** "___ is found in ___ because long ago ___. Today ___." Narrator: "Resources aren't sprinkled evenly. They're where Earth's history put them, and some, like groundwater, are still being made and used right now."

**The end.** The four maps with pins and the explanation. `Print` prints them.

**World view (extra).** The same four layers on a world map.

## Content
- Four simplified geology layers and four deposit maps from public domain USGS sources, three-frame forming stories, two human side cards with real figures, the explanation card.
- A note: "Maps are simplified. Real deposits are patchy and change as people find more."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pins can be moved until `Reveal`.
- Keyboard: Tab to cards, switches, the map grid (in cells) and `Reveal`; Enter drops a pin.
- With Motion off forming stories show still frames.

## Look
- Accent `--brand` #4d5d1a olive (header, layer switches, pins); gold #f4c542 (the pin in hand, matched pins); paper #f6f7ef; ink #171c06; muted #555a4a.
- Contrast (WCAG 2.1, computed): white on brand 7.25:1; brand on paper 6.72:1; ink on paper 16.15:1; muted on paper 6.61:1; ink on gold 10.71:1.
- Never color alone: layers and deposits carry hatch patterns and names.
- Different from this batch (granite brown, raindrop blue, tomato red, lake teal).

## Art
- Maps drawn in code from public domain USGS data.
- Local FLUX (`scripts/localart.py`): forming story frames, three per resource (12, 16:9); Butte headframe from a public domain photo where found and checked (1, 4:3).
About 13 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the geologist with the forming stories; `news-reader` as the human side cards and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.resource + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `layer`: "Tap a layer switch to turn it on."
- how `pin`: "Tap the map to drop a pin."
- how `reveal`: "Tap Reveal."
- event, whole, each forming story.
- event, whole, each human side card.
- how `explain`: "Fill in the explanation card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: layer switches, pins, the reveal. Layers and deposits sit in a marked block `/* RESOURCE-MAP DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pins | Drop pins everywhere | Three pins only per resource. |
| Layer question | Tap any layer | The card shows the layer that matched and asks again. |
| Explanation | Name a place | The card needs a past process and a present one. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Forming story (whole), waits.
2. `layer`; `pin`; `reveal`.
3. Human side cards (whole), each waits.
4. `explain`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS3-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Oil forms from buried marine plankton | U.S. Energy Information Administration, "Oil and petroleum products explained" | U.S. Geological Survey, "Petroleum" | yes |
| U.S. coal formed in swamps about 300 million years ago | U.S. Geological Survey, "Coal" | U.S. Energy Information Administration, "Coal explained" | yes |
| Porphyry copper in Arizona, Utah and Montana forms from hot fluids near old magma | U.S. Geological Survey, "Porphyry copper deposits" | Montana Bureau of Mines and Geology, Butte | yes |
| High Plains aquifer underlies parts of eight states; declines of over 100 feet in places | U.S. Geological Survey, High Plains Water-Level Monitoring | Kansas Geological Survey, High Plains aquifer atlas | yes |
| Butte grew as a copper mining city | National Park Service, Butte-Anaconda National Historic Landmark | Montana Historical Society, Butte | yes |
Backed twice: 6. Cut: 0.

Sensitivity note: many U.S. mineral and energy deposits lie on or near tribal lands. The tool shows geology and deposits only, with no tribal land overlay and no single case retold; one card names that tribal nations govern resources on their own lands and links to the National Congress of American Indians.

Checks run (Python, scratchpad r2, 2026-11-10): four resources and four layers; three pins each is 12; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map with cards; at 680x425 sheet.
2. Each resource's forming story is read and its layer switched on. (MS-ESS3-1)
3. Pins are dropped and real deposits revealed for four resources. (MS-ESS3-1)
4. The aquifer card is read and one resource's map is explained with a past and a present process. (MS-ESS3-1)
5. Deposit maps match cited USGS maps.
6. The tribal lands card shows as described; no tribal overlay.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames; no network requests.

## Open questions
- The idea card flags a data source (default used: USGS mineral, energy and High Plains aquifer maps, public domain, simplified and bundled, checked before build).
- Sensitivity flag: mining and drilling on Native lands (default used: geology and deposits only, no tribal overlay, one card on tribal governance with a link to NCAI, fresh-agent read before build).
