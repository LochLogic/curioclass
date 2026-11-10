# Compass Rose Quest

## One idea
Kiki the parrot hunts treasure across a park map by north, south, east and west, and each clue names a place by what the map key says it is ("the place people built for play"), so the class must read the key and tell what nature made from what people built; then the child makes a map of their own room with a key and two direction clues, and Kiki tries to follow it and either finds the treasure or gets lost at the exact clue that wasn't clear.

## Not like
- me-on-the-map (K, built, same me-map family): zooming out from a bedroom to the planet. Here directions and a key on one map, and making a map that someone else follows.
- map-maker (3, concept): scale and a grid for an imaginary town. Here four directions and a picture key for first graders.
- community-helpers-village (1, concept, this batch): placing helpers to make a village work. Here placing map stickers so a reader can find something.
- festival-parade (1, spec): a world map of where festivals traveled. Here reading and making maps.
- teddy-bear-makers (1, concept, this batch): steps in order on a line. Here steps across a map.

## Who and how
- Grade 1, Social Studies (Geography), module "Maps and Globes". Standards: D2.Geo.1.K-2 (construct maps and other representations of familiar places), D2.Geo.3.K-2 (use maps, globes and other simple geographic models to identify cultural and environmental characteristics of places).
- Driver: teacher on the projector with the class calling directions, or one child alone; every clue, key symbol and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Key sort, Park quest (five clues), Globe (three sails), then My map. tool.json `modes: ["Park quest", "Globe", "My map"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.
- My map is kept only while the page is open; `Print` prints it with its key and clues.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.3.K-2 (environmental and cultural characteristics) | Sort the park key's symbols into "Nature made" and "People built", then follow clues that name places by that difference | the key sort and the clue's lit symbol | 2, 3 |
| D2.Geo.3.K-2 (globe) | Sail west, east and south from North America on a simple globe and name what you reach | the ship's path and the ocean or continent label | 4 |
| D2.Geo.1.K-2 (construct a map) | Place room stickers on a grid, drag each into the key, hide treasure and build two direction clues | the child's map, its key and clue tiles | 5 |
| D2.Geo.1.K-2 (test it) | Watch Kiki follow the clues and fix the one that sent Kiki wrong | Kiki's path and the clue that lights where Kiki got lost | 6 |

## Screens and modes
Header (kit): title "Compass Rose Quest"; `Park quest`, `Globe`, `My map`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A painted park seen from above on a 6 by 5 grid of soft squares, with a big compass rose in the corner and an empty key box beside it. Kiki the parrot perches on the compass rose. Seven key symbols sit in a row above the key box. The welcome is queued (`welcomeAfter: true`): "Ahoy! I'm Kiki. Every map has a key that tells what the pictures mean. Tap a picture to hear it. Then drag it: did nature make it, or did people build it?" First hint: "Tap a picture to hear it. Then drag it to Nature made or People built." The first tap says that symbol's name and cuts the welcome.

**Key sort (focus: the key box).** The key box has two halves with icons: "Nature made" (a leaf) and "People built" (a hammer). Seven symbols: pond, hill, woods (nature); playground, store, school, bridge (people). Right drop: the symbol settles and its square on the map glows once. Wrong: "Did people build the pond, or did nature make it? Listen again." When all seven are in, the quest starts.

**Park quest (focus: the map with Kiki's token).** At 1366x768 the map is center and largest; the compass rose (with four big arrow buttons N, E, S, W, each a picture arrow plus its letter and word) is at the right; the clue card is above the map; the key is at the left. At 680x425 the key folds into a `Key` button.
- Each clue is spoken and shown as pictures (start symbol, arrow, number of steps, goal symbol or its key half). The child taps arrow buttons; Kiki hops one square per tap. Kiki can't hop off the map ("That's the edge of the park!").
- When the token reaches the clue's goal, the clue card stamps and the next clue plays. If the child stops on a wrong square and taps `Here?`, Kiki says what's there by its key name and replays the clue.
- Five clues (start at the pond):
  1. "From the pond, go east to the place people built for play." (2 steps east: playground)
  2. "From the playground, go north 2 steps to something nature made." (hill)
  3. "From the hill, go east 2 steps to the store."
  4. "From the store, go south 3 steps to the school."
  5. "From the school, go west 3 steps to the bridge. The treasure is under it!" A chest pops up.
Clues 1 and 2 name the goal only by its key half, so the child must use the key.

**Globe (focus: a simple globe drawn in code).** North America faces the child; a ship sits on its coast. Three sails, each spoken: "Sail west from North America. Tap West." (the Pacific Ocean lights and is named); "Sail east. Tap East." (the Atlantic Ocean); "Go south over land. Tap South." (South America). After each, the child taps "Nature made" or "People built" for one picture the ship passes: a whale on the first sail, a lighthouse on the second, a rainforest on the third. This checks the same idea on a bigger map.

**My map (focus: the child's room grid).** A 4 by 4 room grid with a door at the bottom and north at the top (a small compass rose). Eight room stickers (bed, desk, rug, toy box, window, lamp, bookshelf, plant). The child:
1. Drags at least four stickers onto squares.
2. Drags each placed sticker's picture into the key; a sticker not in the key shows a question mark on the map.
3. Taps a square to hide the treasure (a star).
4. Builds two clues from tiles: [start sticker] [arrow] [1, 2 or 3 steps]. Clue 2 starts where clue 1 ends.
5. Taps `Send Kiki`.
Kiki hops. Results, each its own picture:
- Found it: Kiki digs up the star and dances.
- A clue leaves the room: Kiki bumps the wall and clue 1 or 2 lights where it happened: "Clue 1 sent me into the wall!"
- A clue ends on an empty square that isn't the treasure: "I'm here, by nothing. Which clue should change?" and the clue that ended there lights.
- A start sticker not in the key: "I don't know what this is. It's not in your key!" and the key's empty row glows.
The child fixes a clue or the key and sends Kiki again. `Print` prints the map, key and clues.

## Content
- Park grid (columns 0 to 5 west to east, rows 0 to 4 north to south): woods (0,0); hill (3,1); store (5,1); pond (1,3); playground (3,3); school (5,4); bridge (2,4) over a little stream that runs from the pond off the bottom edge of the map. Every clue's route is checked in Python.
- Globe: North America, South America, the Pacific and Atlantic Oceans named; passing pictures: a whale (nature), a lighthouse (people), a rainforest (nature).
- Room stickers and their key pictures as listed.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; an arrow tap during a line moves Kiki at once.
- Arrow buttons stay live throughout the quest; `Here?` shows only after the first move of a clue.
- `Send Kiki` shows only when four stickers are placed and keyed, the treasure is hidden and both clues are built; the hint names the next missing step instead.
- With Motion off Kiki jumps square to square without hopping and the ship appears at its end point.

## Look
- Accent `--brand` #234a8a map navy (header, the compass rose, the key frame); gold #f4c542 (Kiki's token ring, the treasure star, the lit clue); paper #eef3fa; ink #0a1830; muted #4c586a. Scene: a park seen from above in a storybook style.
- Contrast (WCAG 2.1, computed): white on brand 8.68:1; brand on paper 7.79:1; ink on paper 15.88:1; muted on paper 6.47:1; ink on gold 10.88:1.
- Never color alone: arrows carry letters and words; key halves carry icons and words.
- Different from this batch (brick orange, market teal, capsule slate, workshop raspberry).

## Art
- Local FLUX (`scripts/localart.py`): the park from above, painted to fit the 6 by 5 grid with the seven places in their squares (1, 6:5); seven key symbols in one sticker style (7, 1:1); eight room stickers (8, 1:1); a treasure chest open and closed (2); a whale, a lighthouse, a rainforest (3, 1:1).
- Kiki the parrot (a green and red parrot with a tiny captain's hat), 6 poses (perched, hopping, pointing with a wing, bumping a wall, digging, dancing); 1:1; cutout yes; not a person.
- Drawn in code: the grids, the compass rose and arrows, the globe (continent outlines), the key box, clue tiles.
About 27 images.

## Voice
Bank voice `playful-friend` as Kiki and the narrator (unique in this batch), style: cheerful parrot pirate, never shouting. `Curio.voice` with `scope: () => state.mode + ':' + state.clue + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Ahoy! I'm Kiki. Every map has a key that tells what the pictures mean. Tap a picture to hear it. Then drag it: did nature make it, or did people build it?"
- event `symbol`: the symbol's name.
- event `sort-no`: "Did people build the [thing], or did nature make it? Listen again."
- how `quest` (once): "Now let's find treasure! Tap the arrows to move me."
- event, whole, `clue`: each clue (texts in Park quest).
- event `edge`: "That's the edge of the park!"
- event `here`: "This is the [key name]." then the clue again.
- event `clue-done`: "Yes!" with a stamp sound.
- event, whole, `treasure`: "Treasure! You read the map like a real explorer. Tap Globe to sail the world."
- event, whole, `sail`: each sail line, then the place's name.
- how `my-map`: "Make a map of a room. Drag stickers onto the room."
- how `key-step`: "Now drag each sticker into your key."
- how `hide`: "Tap a square to hide the treasure."
- how `clues`: "Make two clues. Tap a sticker, an arrow and a number."
- how `send`: "Tap Send Kiki."
- event, whole, Kiki's result lines (found, wall, empty square, not in key).
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
me-map has no engine file (docs/families has none); this tool shares only the family name and map look with me-on-the-map. Tool-only code: the grid with key, arrow moves, clue checking, the globe and the room map maker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Key sort | Drag all to one half | Wrong drops come back with a question. |
| Clue | Wander until the stamp | `Here?` must be tapped on the goal; wandering works only if the child taps it on the right square, and clues 1 and 2 name only the key half. |
| Clue | Follow the glowing square | Squares glow only during the key sort, not during clues. |
| Globe | Tap any arrow | Each sail asks for one direction and names what you reach; a different arrow says "That's [direction]. I asked for [direction]." |
| My map | Send Kiki with one clue | `Send Kiki` waits for two clues, a key and a treasure. |
| My map | Put the treasure on a sticker the clue already lands on | Allowed; that is a working map. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a symbol: `symbol`; drop: chime or `sort-no`.
2. Seventh symbol: `quest`, then `clue` 1 (whole).
3. Each arrow tap: a hop; `edge` if needed. `Here?`: `clue-done` then the next `clue` (whole), or `here`.
4. Clue 5 done: `treasure` (whole).
5. Globe: `sail` per sail (whole), then the passing picture question.
6. My map: `my-map`, `key-step`, `hide`, `clues`, `send` in order as each step opens; Send: Kiki's result line (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.1.K-2 and D2.Geo.3.K-2 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The four cardinal directions are north, east, south and west; on most maps north is at the top | Wikipedia, Cardinal direction (checked 2026-11-09) | National Geographic Education, "Cardinal directions" | yes |
| A map key (legend) explains the symbols on a map | National Geographic Education, "Map key" | USGS, map symbols | yes |
| Sailing west from North America reaches the Pacific Ocean; east reaches the Atlantic; South America lies to the south | NOAA Ocean Service, "How many oceans are there?" | National Geographic Education, continents and oceans | yes |
| Natural features (ponds, hills, woods) are made by nature; human features (bridges, schools, stores) are built by people | National Geographic Education, "Human and physical features" | C3 Framework Geography K-2 examples | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-09): from the pond at (1,3), each of the five clue routes lands on its named place (playground (3,3), hill (3,1), store (5,1), school (5,4), bridge (2,4)) and stays on the 6 by 5 map; every key half matches the place each clue names; the My map checker finds "found", "wall", "empty" and "not in key" correctly on 2,000 random room maps; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map, compass rose, clue card and key fit; at 680x425 the key folds.
2. The key sort accepts each symbol only in its half. (D2.Geo.3.K-2)
3. Five clues move Kiki with arrow buttons; the first two name places only by key half. (D2.Geo.3.K-2)
4. The globe sails west, east and south with names. (D2.Geo.3.K-2)
5. My map takes stickers, a key, a treasure and two clues. (D2.Geo.1.K-2)
6. Kiki's four results each show and light the clue at fault. (D2.Geo.1.K-2)
7. Send Kiki and Here? are never named before they show.
8. Tap while it plays: an arrow tap during a line moves Kiki at once; no older line plays after a newer one.
9. Motion off: Kiki jumps without hopping; no network requests.

## Open questions
- None for Cory.
