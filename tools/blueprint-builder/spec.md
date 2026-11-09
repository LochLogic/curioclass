# Blueprint Builder

## One idea
The student gets one pile of fact bricks about a real topic (a town that keeps flooding, the first transcontinental railroad, beavers changing a river) and builds it to four blueprints (chronology, comparison, cause and effect, problem and solution), each with slots that take only bricks of the right job and signal-word mortar, and the four buildings stand side by side made of the same bricks, so they learn that a text's structure decides what a reader notices first; later levels flip it, and they name the structure of a finished passage from its signal words.

## Not like
- structure-spotter (3, spec): sorting found paragraphs into three bins. Here building one fact pile four ways, and four structures at grade 4.
- how-it-works-diagrams (3-5, spec): a process on a diagram. Here whole-text structure.
- essay-train (5, concept): ordering the student's own essay. Here given facts and named structures.
- main-idea-pinboard (3-5, spec): a main idea and its proof. Here the build of the text.
- dialogue-director (3, spec): a comic into prose. Here facts into structures.

## Who and how
- Grade 4, ELA, module "Text Structures" (Reading Informational). Standard: RI.4.5.
- Driver: one student or a pair (tool.json `driver: "student"`). Every brick and passage is read on tap.
- Three topics, each with 10 to 12 bricks; then six "no blueprint" passages; then one mixed text. tool.json `modes: []`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Nothing is saved; `Print` prints the four buildings as four short texts.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.4.5 (chronology) | Fill the timeline blueprint with dated bricks and time mortar (in 1863, by 1869, then) | the chronology building | 2, 3 |
| RI.4.5 (comparison) | Fill the two-column blueprint with alike and different bricks and mortar (both, in contrast, however) | the comparison building | 2, 3 |
| RI.4.5 (cause and effect) | Join cause and effect bricks with because, as a result, so | the cause building | 2, 3 |
| RI.4.5 (problem and solution) | Place the problem, the fixes and the result with the problem was, one solution, as a result | the problem building | 2, 3 |
| RI.4.5 (reading) | Name a finished passage's structure, mark its signal words and describe it in one sentence | the passage with marked words and a frame | 5 |

## Screens and modes
Header (kit): title "Blueprint Builder"; `Topics`, `Read a building`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An architect's table with four rolled blueprints and a pile of bricks, and Foreman Bea, a beaver in a hard hat. First hint: "Tap a topic to dump its fact bricks on the table." The first tap does; the welcome is queued after it (`welcomeAfter: true`).

**Brick pile.** 10 to 12 bricks, each a fact sentence with a small job tag hidden until placed (date, event, alike, different, cause, effect, problem, fix, result). Tap to hear.

**Blueprint.** Unroll one of four. Its frame has labeled slots (Chronology: 4 dated slots in order; Comparison: two columns with 2 alike and 3 different; Cause and effect: 3 cause-effect pairs; Problem and solution: problem, 2 fixes, result). A brick snaps into a slot only if its job fits; wrong bricks bounce with "This brick is a {cause}, not a {date}." Mortar chips (signal words) go between slots; the frame needs one mortar per joint. Leftover bricks are fine. When every slot and joint is filled, the building stands and reads aloud as a paragraph.

**Side by side.** After all four, the buildings stand together. Question cards: "Which version helps a reader who wants to know why the town flooded?" "...when each step happened?" "...how the two towns differ?" "...what was done about it?" The student taps the building.

**Read a building.** Six passages with no blueprint. The student picks the structure, taps the signal words (at least 2 of the structure's kind), and completes a frame: "This passage uses ___ to show ___."

**Mixed wall.** One passage where chronology and cause share a wall; the student marks both kinds of signal words.

At 1366x768 the pile and blueprint fit; at 680x425 the pile is a drawer.

## Content
Bricks written for Curio Class from sourced facts.
- **A Town That Keeps Flooding** (made-up town of Millbrook on a real kind of problem): floods in spring, a wetland was filled for parking, rain gardens and a restored wetland, fewer floods. Facts about how wetlands soak up floodwater are sourced; the town is labeled made-up.
- **The First Transcontinental Railroad**: work began in 1863 (Central Pacific from Sacramento) and 1865 (Union Pacific moving west from Omaha in earnest); the lines met at Promontory Summit, Utah, on May 10, 1869; a trip across the country fell from months to about a week. Thousands of Chinese immigrant workers built much of the Central Pacific's line through the Sierra Nevada, often for lower pay and in dangerous conditions; Irish immigrants and Civil War veterans worked on the Union Pacific; the railroad crossed lands of Native nations, and its building harmed them and the bison they relied on. Told plainly, in two bricks.
- **Beavers Change a River**: dams slow water, make ponds, raise the water table, create wetlands for birds and fish; comparison of a stream with and without beavers.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Bricks can be pulled back out; mortar chips are reusable.
- Keyboard path: pick a brick, then a slot number.

## Look
- Accent `--brand` #9a4a0c brick orange (header, bricks, blueprint labels); gold #f4c542 (mortar, filled joints); paper #fcf5ef; ink #2a1405; muted #64544a. Scene: a sunny architect's table.
- Contrast (WCAG 2.1, computed): white on brand 6.25:1; brand on paper 5.79:1; ink on paper 16.20:1; muted on paper 6.69:1; ink on gold 10.75:1.
- Never color alone: bricks show their job tag in words once placed; slots are labeled.
- Different from this batch (lagoon teal, word violet, storm slate, kite magenta).

## Art
Local FLUX (`scripts/localart.py`); railroad scenes show workers small and from a distance, with no faces in focus.
- table (1); Foreman Bea (4 poses: carry, point, think, cheer), "A friendly beaver construction foreman in a hard hat <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- topic scenes (6): "<a flooded small-town street / a restored wetland / a steam train crossing a high trestle in the Sierra Nevada / a beaver pond>, painterly, no text"; 16:9.
About 11 images. Drawn in code: blueprints, bricks, mortar, buildings.

## Voice
Bank voice `easy-coach` as Foreman Bea and the brick reader (unique in this batch). `Curio.voice` with `scope: () => state.topic + ':' + state.blueprint + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Same bricks, four buildings. Unroll a blueprint and put each fact brick in a slot that fits its job."
- event, whole, `brick`: the brick's sentence.
- event `bounce`: "This brick is a {cause}, not a {date}."
- how `mortarHow`: "Every joint needs mortar. Pick a signal word to join these bricks."
- event `stands`: "It stands! Listen to your building." then the paragraph (whole).
- how `compareHow`: "Same facts. Which building answers this question best?"
- how `readHow`: "No blueprint this time. Tap the signal words, then name the structure."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: brick pile, blueprint frames, mortar, side-by-side view, reading frame.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Slots | Try every brick in every slot | Bounces explain the brick's job; each try teaches the job tag. |
| Mortar | Any chip in any joint | Each joint takes only its blueprint's signal words (because does not fit a chronology joint). |
| Read a building | Guess the structure | The pick sticks only with 2 signal words of that kind tapped. |
| Side by side | Tap any building | 4 questions to 4 buildings; wrong picks read the building's first sentence. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a topic: `welcome` (queued, first time).
2. Bricks: `brick` (whole); bounces: `bounce`; first joint: `mortarHow`.
3. Full blueprint: `stands`, paragraph.
4. After four: `compareHow`. Read a building: `readHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.4.5 wording | thecorestandards.org, Reading Informational Grade 4 | CCSS ELA 2010 PDF | yes |
| Wetlands store and slow floodwater | US EPA, why are wetlands important | US Fish and Wildlife Service, wetlands | yes |
| Transcontinental railroad: Central Pacific from Sacramento (1863), Union Pacific from Omaha, met at Promontory Summit May 10, 1869 | National Park Service, Golden Spike National Historical Park | Library of Congress, transcontinental railroad | yes |
| Chinese immigrant workers built much of the Central Pacific line, at lower pay and in dangerous conditions; Irish workers and veterans on the Union Pacific | Stanford University, Chinese Railroad Workers in North America Project | National Park Service, Golden Spike, the workers | yes |
| The railroad's building harmed Native nations and the bison herds | National Park Service, Golden Spike | Smithsonian National Museum of the American Indian, transcontinental railroad resources | yes |
| Beaver dams make ponds and wetlands and raise water tables | US Fish and Wildlife Service, beaver | NOAA Fisheries, beaver dam analogs and habitat | yes |
Backed twice: 6. Cut: 1 (a "cross-country trip fell from six months to six days" figure; sources give different numbers, so the bricks say "from months to about a week").

Sensitivity note: the railroad's workers and the harm to Native nations go to the fresh-agent review.

Checks run (Python, scratchpad b12, 2026-11-09): every topic's bricks fill all four blueprints with leftovers allowed; each of the six reading passages holds at least two signal words of its structure; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the pile and blueprint fit; at 680x425 the pile is a drawer.
2. Bricks snap only into slots that fit their job. (RI.4.5)
3. Joints need matching mortar; a full building reads aloud. (RI.4.5)
4. The side-by-side view answers four questions.
5. Read a building needs two signal words and a frame. (RI.4.5)
6. The mixed wall marks both structures.
7. Print shows the four buildings as texts.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: bricks place without dropping; no network requests.

## Open questions
- None for Cory.
