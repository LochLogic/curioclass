# Shape Spy

## One idea
A spy kid named Juniper (made up, labeled "illustration") hands the child a spyglass and a spy notebook, and in three real-looking scenes (a park, a kitchen, a street) a voice asks for one shape at a time ("Find a circle"); the child taps it and its outline glows with its name, then a position question follows ("What is above the slide?") and the child taps the round sun; each scene hides five flat shapes (circle, square, triangle, rectangle, hexagon) and four solid shapes (cube, cone, cylinder, sphere), including trick finds like a square turned on its corner on a kite or a tiny triangle on a road sign, and Juniper says "Still a square. Turning it doesn't change it."; each find gets filed on the flat page (where it's drawn flat) or on the solid shelf (where it can be spun around); at the end the spy notebook holds every shape found, flat and solid on separate pages, so a kindergartner learns to describe objects in the world using the names of shapes and their relative positions (above, below, beside, in front of, behind, next to), to name shapes whatever their size or which way they're turned, and to tell flat shapes from solid ones.

## Not like
- pattern-block-windows (K, spec): building and putting shapes together. Here finding and naming them.
- toy-box-sort (K, spec): sorting toys by color, shape or size. Here shapes and where they are.
- shape-family-tree (3, concept): families of four-sided shapes. Here first shape names.
- shape-talk (K to 2, live): describing shapes in words. Here spotting them in scenes.

## Who and how
- Kindergarten, Math, module "Shapes All Around". Standards: K.G.1 (describe objects in the environment using names of shapes, and describe the relative positions of these objects using terms such as above, below, beside, in front of, behind, and next to), K.G.2 (correctly name shapes regardless of their orientations or overall size), K.G.3 (identify shapes as two-dimensional (lying in a plane, "flat") or three-dimensional ("solid")).
- Format: explorer. Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Three scenes, nine shapes each, six position words, two trick finds per scene, the flat page and the solid shelf. Extra: I spy (the child picks a shape and a position clue for a friend to find). tool.json `modes: ["Spy", "I spy"]`, `minutes: "10-20"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.G.1 | Tap named shapes and answer position questions | glowing outlines; position words | 2 |
| K.G.2 | Find tilted and tiny shapes | trick finds; "Still a square" | 3 |
| K.G.3 | File each find as flat or solid | the flat page; the solid shelf with spinning shapes | 4 |

## Screens and modes
Header (kit): title "Shape Spy"; `Spy`, `I spy`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A sunny park with a slide, a sun, a kite, a ball, a bench and a road sign. Juniper peeks from behind a tree with a spyglass. The welcome is queued (`welcomeAfter: true`): "Psst! I'm Juniper, a shape spy. Shapes are hiding everywhere. Find a circle. Tap it!" First hint: "Tap a circle in the park."

**Spying (focus: the scene).** At 1366x768 the scene fills the screen with the notebook as a tab on the right; at 680x425 the scene fills the screen and the notebook opens as a sheet. Every tappable shape has a target area of at least 64 px. A right tap glows the outline and Juniper names it. A wrong tap: "That's a ___. Keep looking for a circle!"

**Position questions.** "What is above the slide?" "What is next to the bench?" "What is behind the tree?" The child taps the answer. Six position words across the three scenes.

**Trick finds (K.G.2).** A kite that's a square turned on its corner; a tiny triangle on a road sign; a huge rectangle (a building). Juniper: "Still a square. Turning it doesn't change it." A `Turn it` button spins the found shape on the notebook page.

**Flat or solid (K.G.3).** After each find, two big buttons: Flat page or Solid shelf. Solid finds can be spun with a finger to show all sides; flat ones lie on the page. A ball is a sphere; a drawn circle is flat.

**The notebook (the aha).** Every find with its name, flat on one page and solid on the shelf. Juniper: "Flat shapes lie on paper. Solid shapes you can hold and turn. You found them all!"

**The end.** The notebook. `Print` prints it as a coloring page.

**I spy (extra).** The child picks a shape and taps a position word to make a clue for a friend.

## Content
- Three scenes, five flat and four solid shapes per scene, six position words, two trick finds per scene, all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Scenes can be changed with big arrows at any time.
- Keyboard: Tab to each hidden shape in turn, the answer buttons, `Turn it` and the notebook; Enter taps; arrows spin solids.
- With Motion off outlines glow without pulsing and solids show three still views.

## Look
- Accent `--brand` #6a2c91 spy purple (header, the notebook, buttons); gold #f4c542 (glowing outlines, the spyglass rim); paper #f7f1fb; ink #1e0b2b; muted #584e60.
- Contrast (WCAG 2.1, computed): white on brand 8.82:1; brand on paper 7.95:1; ink on paper 16.64:1; muted on paper 7.08:1; ink on gold 11.35:1.
- Never color alone: outlines carry the shape name.
- Different from this batch (meadow green, zoo orange, playground blue, robot red).

## Art
- People (illustrated): Juniper the spy kid, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the park, the kitchen, the street (3, 16:9).
- Drawn in code: outlines over each scene (hit areas match objects), the notebook, spinning solids.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Juniper; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.scene + ':' + state.target + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `find`: "Tap a shape that matches."
- how `where`: "Tap the thing in that spot."
- how `file`: "Tap Flat page or Solid shelf."
- event, whole, each trick find.
- how `scene`: "Tap the arrow for the next place."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: scene hit areas, the notebook, the solid spinner. Scenes and shapes sit in a marked block `/* SHAPE-SPY DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find | Tap everywhere | Wrong taps name what was tapped and ask again. |
| Position | Tap any object | The answer must be in that spot. |
| Flat or solid | Always tap Flat page | Solids bounce back with "You can hold this one. It's solid." |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `find`; `where`.
2. `file`.
3. Trick find (whole), waits.
4. `scene`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.G.1, K.G.2, K.G.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Children should meet shapes in many sizes and turns, not only standard views | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| Flat and solid shapes and position words in kindergarten | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | National Council of Teachers of Mathematics, "Principles and Standards", Pre-K to 2 geometry | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-10): five flat and four solid shapes make nine per scene; six position words; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and notebook tab; at 680x425 sheet.
2. Shapes are found by name and position questions answered in three scenes. (K.G.1)
3. Tilted, tiny and huge shapes are named. (K.G.2)
4. Every find is filed as flat or solid. (K.G.3)
5. Every card is spoken; every target is 64 px or more.
6. Juniper is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still glows and three views; no network requests.

## Open questions
None.
