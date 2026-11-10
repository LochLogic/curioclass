# Plate Puzzle

## One idea
On a world map with the continents as loose pieces and a clue drawer, the student fits the continents back together one kind of evidence per level: level 1 uses coastlines only (Africa and South America), level 2 adds fossils found on both sides of an ocean (Mesosaurus, a small freshwater reptile, in Brazil and South Africa; Glossopteris, a seed fern, across the southern continents), level 3 adds rock belts and old mountain chains that line up across the Atlantic, level 4 adds seafloor age stripes that mirror each other on both sides of the mid-ocean ridge, and level 5 sets the speed (about 2.5 centimeters a year, about as fast as fingernails grow) and plays the plates backward and forward through 200 million years to test the fit; along the way two cards tell the human story, Alfred Wegener proposing drifting continents in 1912 and being widely dismissed, and Marie Tharp's seafloor maps in the 1950s helping turn the argument; at the end the clue board shows four independent kinds of data agreeing, so a sixth grader learns to analyze and interpret data on the distribution of fossils and rocks, continental shapes and seafloor structures as evidence of the past plate motions.

## Not like
- world-layers-map (4, spec): mapping where earthquakes and volcanoes cluster. Here why the pieces moved.
- canyon-reader (4, spec): layers in one canyon. Here rocks matched across oceans.
- erosion-table (4, spec): water and wind shaping land. Here whole continents moving.
- rock-recycler (6, concept): the rock cycle and its energy. Here the plates that carry the rocks.

## Who and how
- Grade 6, Science, module "Plate Tectonics". Standard: MS-ESS2-3 (analyze and interpret data on the distribution of fossils and rocks, continental shapes, and seafloor structures to provide evidence of the past plate motions).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six continent pieces, five levels, four fossil clues, three rock belt clues, the seafloor age map, the time slider, two story cards, the clue board. Extra: Future Earth (run the plates 50 million years ahead). tool.json `modes: ["Puzzle", "Future Earth"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS2-3 (shapes) | Fit coastlines | Africa and South America pieces locking | 2 |
| MS-ESS2-3 (fossils and rocks) | Line up fossil ranges and rock belts across oceans | fossil and rock overlays matching across the join | 3 |
| MS-ESS2-3 (seafloor) | Match mirrored age stripes and run time back | the age map; the time slider | 4 |

## Screens and modes
Header (kit): title "Plate Puzzle"; `Puzzle`, `Future Earth`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A blue world with the continents lifted off like puzzle pieces, slightly scattered. A clue drawer at the side, closed. The welcome is queued (`welcomeAfter: true`): "Some of these pieces look like they fit. Do they really? Drag South America toward Africa." First hint: "Drag South America next to Africa."

**Level 1, coastlines (focus: the join).** At 1366x768 the map fills the left with the clue drawer right; at 680x425 the drawer is a sheet. The pieces snap when the edges of the continental shelves line up (the shelf, not the beach, is drawn). A note: "Shapes alone could be luck. Let's find more clues."

**Level 2, fossils.** The drawer opens fossil overlays: Mesosaurus (Brazil, South Africa), Glossopteris (South America, Africa, India, Antarctica, Australia), Lystrosaurus and Cynognathus. The student moves India, Antarctica and Australia until each fossil's range makes one patch. A card asks: "Could a small freshwater reptile swim an ocean?"

**Level 3, rocks.** Rock belt overlays: old mountains in the eastern United States lining up with ones in Scotland and Norway; matching rock in Brazil and West Africa. The student nudges North America and Europe until the belts join.

**Level 4, seafloor.** The ocean turns into age stripes: young rock at the ridge in the middle of the Atlantic, older rock toward each coast, the pattern mirrored. The student drags the time slider back; stripes peel off at the ridge and the continents close up.

**Level 5, speed and time.** The student sets the speed with a fingernail comparison (about 2.5 cm a year) and plays 200 million years: Pangaea assembles, then splits. The tool shows 2.5 cm a year for 200 million years is 5,000 km.

**Story cards.** Wegener (1912) had shapes, fossils and rocks but no way to move continents and was widely dismissed. Marie Tharp, working with Bruce Heezen, mapped the ridge and the rift in its middle; their 1957 North Atlantic map helped turn the argument.

**The clue board (the aha).** Four tiles light up: shapes, fossils, rocks, seafloor. Narrator: "One clue could be chance. Four different kinds that all say the same thing are hard to argue with."

**The end.** The clue board with one line of evidence per tile. `Print` prints it.

**Future Earth (extra).** The plates run 50 million years ahead with a note that the future map is a model.

## Content
- Six continent pieces from public domain reconstructions, four fossil ranges, three rock belt overlays, a seafloor age map, the time slider (0 to 200 million years), two story cards, the clue board.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces snap only within a tolerance of the reconstruction fit; a piece can be rotated with a handle.
- Keyboard: Tab to pieces, the rotate handle, overlays, the slider and tiles; arrows move and rotate; Enter places.
- With Motion off the time slider jumps in 50-million-year steps.

## Look
- Accent `--brand` #8a2f2f magma red (header, the ridge, the slider); gold #f4c542 (the piece in hand, matching overlays); paper #fbf3f1; ink #2a0d0b; muted #5f514f.
- Contrast (WCAG 2.1, computed): white on brand 8.31:1; brand on paper 7.59:1; ink on paper 16.53:1; muted on paper 6.91:1; ink on gold 11.12:1.
- Never color alone: seafloor ages carry numbers and stripe patterns; overlays carry fossil names.
- Different from this batch (schoolyard brick, cell green, current blue, strata plum).

## Art
- Map pieces and the seafloor age map drawn in code from public domain data.
- Gemini or local FLUX: Mesosaurus, Glossopteris, Lystrosaurus, Cynognathus as labeled reconstructions (4, 1:1); a portrait card each for Wegener and Tharp from public domain or openly licensed photos, checked (2, 3:4).
About 6 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the story cards and the clue board; `wise-mentor` as the puzzle guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `fit`: "Drag a continent until its edge fits."
- how `fossil`: "Drag the pieces until each fossil makes one patch."
- how `rock`: "Nudge the pieces until the rock belts join."
- how `time`: "Drag the time slider back."
- event, whole, each story card.
- event, whole, the clue board.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the pieces, snapping, overlays, the time slider. Plate positions by time, fossil ranges and the age map sit in a marked block `/* PLATE-PUZZLE DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fit | Push pieces together anywhere | Snaps happen only at the reconstruction fit. |
| Overlays | Skip to level 5 | Each level opens only after its clue lines up. |
| Clue board | Tap tiles | Each tile asks which piece of evidence matched across the join. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `fit`; `fossil`; `rock`; `time`.
2. Story cards (whole), each waits.
3. Clue board (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS2-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Mesosaurus, Glossopteris, Lystrosaurus and Cynognathus ranges across southern continents | U.S. Geological Survey, "This Dynamic Earth" (fossil evidence map) | University of California Museum of Paleontology, "Wegener and continental drift" | yes |
| Wegener proposed continental drift in 1912 and was widely dismissed | U.S. Geological Survey, "This Dynamic Earth", historical perspective | NASA Earth Observatory, "Alfred Wegener" | yes |
| Marie Tharp and Bruce Heezen published the North Atlantic map in 1957 | Library of Congress, "Marie Tharp" collection | Columbia Climate School, Lamont-Doherty, "Marie Tharp" | yes |
| Mirrored seafloor ages around mid-ocean ridges | NOAA NCEI, "Age of the Ocean Floor" | U.S. Geological Survey, "This Dynamic Earth", magnetic stripes | yes |
| The Atlantic widens a few centimeters a year, about as fast as fingernails grow | U.S. Geological Survey, "This Dynamic Earth" | NASA Earth Observatory, "Plate tectonics" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-10): 2.5 cm a year for 200 million years is 5,000 km; 1912 to 1957 is 45 years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and drawer; at 680x425 sheet.
2. Coastlines are fit at the shelf edges. (MS-ESS2-3)
3. Fossil ranges and rock belts are joined across oceans. (MS-ESS2-3)
4. Seafloor stripes are matched and time is run back to Pangaea. (MS-ESS2-3)
5. Plate positions match the cited public domain reconstruction.
6. Wegener and Tharp cards use checked images and dates.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: 50-million-year steps; no network requests.

## Open questions
- The idea card flags a data source (default used: public domain plate positions from USGS and NOAA NCEI seafloor age grids, simplified and bundled, checked before build; no network).
- Code move: the idea card moves MS-ESS2-1 and MS-ESS2-2 to rock-recycler (default used: this tool teaches MS-ESS2-3 only).
