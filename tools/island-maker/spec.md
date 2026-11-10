# Island Maker

## One idea
Open ocean waits under a sculpting hand with five tools (raise, lower, smooth, add water, add snow), and the student makes an island: mountains, hills, valleys and plains rise as they shape; water flows downhill into rivers and fills low spots as lakes; a high peak gets snow and a glacier; the tool names each landform and body of water as it forms, and the student can tap to label their own; then the student flips to a top-down map view, builds the key (colors and symbols) and matches map spots to the 3D view; challenges ask for a bay a boat can shelter in and a lake fed by a river; a water hunt counts where the island's water is (ocean, river, lake, snow, glacier) and whether it is solid or liquid, then shows the real Earth (almost all water is in the ocean, and most fresh water is frozen); at the end the island becomes a postcard and a finished map with a key, so a second grader learns to model the shapes and kinds of land and bodies of water in an area, and where water is found on Earth and that it can be solid or liquid.

## Not like
- fast-or-slow (2, spec): how land changes over time. Here what land and water look like.
- erosion-table (4, concept): carving with water and wind. Here shaping and mapping.
- sky-diary (1, spec): the sky. Here the ground and water.
- beaver-builders (K, spec): a pond made by animals. Here a whole island.

## Who and how
- Grade 2, Science, module "Maps of Land and Water". Standards: 2-ESS2-2 (develop a model to represent the shapes and kinds of land and bodies of water in an area), 2-ESS2-3 (obtain information to identify where water is found on Earth and that it can be solid or liquid).
- Format: studio. Driver: one child alone or with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Sculpt with five tools, ten landform and water names, the map with a key, two challenges, the water hunt, the postcard. Extra: Island swap (print the map; a classmate builds the island from it). tool.json `modes: ["Studio", "Island swap"]`, `minutes: "20-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2-ESS2-2 (shapes and kinds) | Sculpt land and water and label each landform and body of water | names appearing as features form | 2 |
| 2-ESS2-2 (map model) | Flip to the map, build the key and match spots to the 3D view; meet two challenges | the map with a key | 3 |
| 2-ESS2-3 | Count the island's water by place and solid or liquid, then see the real Earth | the water hunt chart; the real Earth chart | 4 |

## Screens and modes
Header (kit): title "Island Maker"; `Studio`, `Island swap`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** Open blue ocean seen from a tilted view, a sculpting hand and a tool tray: Raise, Lower, Smooth, Add water, Add snow. The welcome is queued (`welcomeAfter: true`): "Let's make an island! Pick Raise, then drag on the ocean to push up land." First hint: "Tap Raise, then drag on the ocean."

**Sculpt (focus: the island).** At 1366x768 the island fills the screen with the tray at the side; at 680x425 the tray sits below. As the student shapes, features are named: mountain (high and steep), hill (low and round), valley (low land between hills), plain (flat land), river (water flowing downhill), lake (water in a low spot surrounded by land), bay (ocean curving into the land), peninsula (land with water on three sides), snowy peak and glacier (ice that moves slowly downhill). The student can tap any spot and pick a name; a wrong name gets a kind hint.

**Map (2-ESS2-2).** A `Map` button flips to a top-down view. The student builds the key by dragging a color or symbol to each kind (blue for water, brown lines for mountains, white for snow and ice, green for plains). Tapping a map spot lights the same spot in the 3D view. Challenges: "Make a bay a boat can shelter in." "Give the island a lake fed by a river."

**Water hunt (2-ESS2-3).** The guide counts the island's water by place (ocean, rivers, lakes, snow, glacier) and sorts each as liquid or solid. Then the real Earth: almost all water (about 97 out of 100 drops) is salty ocean; of the fresh water, about two-thirds is frozen in ice and glaciers; rivers and lakes hold a tiny part. A drop chart shows 100 drops.

**The postcard (the aha).** The island as a postcard with the student's name, and the map with its key. Narrator: "The same island can be a picture or a map. And water can be liquid in the ocean and rivers, or solid as snow and ice."

**The end.** The postcard and the map. `Print` prints them.

**Island swap (extra).** A printed map goes to a classmate, who builds the island from it.

## Content
- Five sculpt tools, ten named features, the key builder, two challenges, the water hunt with real Earth numbers, the postcard.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Water flows downhill and fills low spots as the land changes.
- `Undo` steps back one stroke.
- Keyboard: Tab to tools, the island, the map and the key; arrow keys move the hand; Enter sculpts.
- With Motion off water fills at once and the map flips without turning.

## Look
- Accent `--brand` #0b6178 lagoon (header, the tray, the key); gold #f4c542 (the tool in hand, the named spot); paper #eef7fa; ink #04202a; muted #4d5b60.
- Contrast (WCAG 2.1, computed): white on brand 7.01:1; brand on paper 6.45:1; ink on paper 15.52:1; muted on paper 6.48:1; ink on gold 10.37:1.
- Never color alone: the key pairs every color with a symbol and a name; the drop chart carries numbers.
- Different from this batch (berry, gadget green, dusk blue, canyon rust).

## Art
- Drawn in code: the sculptable terrain with a painted look, water flow, snow and glacier, the map and key, the drop chart.
- Local FLUX (`scripts/localart.py`): a postcard frame (1, 4:3).
About 1 image.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the island guide and the names; `easy-coach` as the hints and the water hunt. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.feature + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sculpt`: "Pick a tool, then drag on the island."
- event, whole, each new feature's name.
- how `map`: "Tap Map to see it from above."
- how `key`: "Drag a color to each kind of land or water."
- how `hunt`: "Tap each place that has water."
- event, whole, the real Earth chart.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the height-field terrain, water flow, feature naming, the map and key, the water hunt.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sculpt | Make one bump | The map opens after at least five kinds of features exist. |
| Key | Drag colors at random | Each key entry checks against the kind; the hint names it. |
| Water hunt | Call everything liquid | Snow and glacier are checked as solid. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sculpt`.
2. Feature names (whole), waits.
3. `map`; `key`; `hunt`.
4. Real Earth (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 2-ESS2-2, 2-ESS2-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| About 97 percent of Earth's water is ocean; about two-thirds of fresh water is frozen | U.S. Geological Survey, "Where is Earth's Water?" | NOAA, "How much water is in the ocean?" | yes |
| Landform and water body definitions for young learners | National Geographic Society, Encyclopedic entries (landform, bay, peninsula, glacier) | U.S. Geological Survey, "Landforms" education page | yes |
| Glaciers are ice that moves slowly downhill | National Snow and Ice Data Center, "What is a glacier?" | National Park Service, "Glaciers" | yes |
| Map keys pair symbols with meanings | U.S. Geological Survey, "Topographic Map Symbols" | National Geographic Society, "Map key" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r26, 2026-11-09): ten named features; 97 ocean drops of 100 leave 3 fresh, and about two of those 3 are frozen; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 island and tray; at 680x425 tray below.
2. Land and water features are named as they form and can be labeled. (2-ESS2-2)
3. The map has a built key, matches the 3D view and meets two challenges. (2-ESS2-2)
4. The water hunt sorts the island's water and shows the real Earth. (2-ESS2-3)
5. Water flows downhill and fills low spots.
6. Every card is spoken; the key pairs color with symbol and name.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: water fills at once; no network requests.

## Open questions
None.
