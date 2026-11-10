# Shade Builder

## One idea
On a hot summer morning in a backyard with a sandbox, a slide, a blacktop path and grass, Mila (made up) says the sandbox gets too hot to play in by lunch; the student taps spots in sun and in shade and a hand shows a face (cool, warm, ouch) while a heat camera colors the ground as time runs from morning to noon, so the student sees that the sun warms what it shines on; then the student asks Mila questions to set the problem (when is it hot, where do kids sit), sketches a plan, and builds a shade over the sandbox from umbrellas, a tree, a tent or a sail; the sun runs from morning to afternoon, the shadow moves, and the heat camera counts the sandbox squares that stayed cool; a second design runs beside the first and a picture chart compares them (cool squares, whether the shade slid off in the afternoon), and the student picks the better one and says why, so a kindergartner learns that sunlight warms the Earth's surface, designs a structure to reduce that warming, and defines, sketches and compares designs.

## Not like
- push-the-pumpkin (K, spec): designing for pushes and motion. Here designing against warming.
- beaver-builders (K, spec): an animal's structure. Here a person's design.
- weather-wardrobe (K, spec): dressing for the weather. Here sun on the ground.
- shadow-puppet-studio (1, spec): light and materials. Here sunlight and heat.

## Who and how
- Kindergarten, Science, module "Sunlight Warms the Earth". Standards: K-PS3-1 (make observations to determine the effect of sunlight on Earth's surface), K-PS3-2 (use tools and materials to design and build a structure that will reduce the warming effect of sunlight on an area), K-2-ETS1-1 (ask questions, make observations, and gather information about a situation people want to change to define a simple problem that can be solved through the development of a new or improved object or tool), K-2-ETS1-2 (develop a simple sketch, drawing, or physical model to illustrate how the shape of an object helps it function as needed to solve a given problem), K-2-ETS1-3 (analyze data from tests of two objects designed to solve the same problem to compare the strengths and weaknesses of how each performs).
- Format: builder. Driver: one child with a grown-up nearby, or the class on the projector (tool.json `driver: "either"`). Every card is spoken. Controls 64 px or more.
- Observe in sun and shade, three questions to Mila, a sketch, two builds tested from morning to afternoon, a picture chart. Extra: Class gallery (plans saved on one device shown side by side). tool.json `modes: ["Build", "Class gallery"]`, `minutes: "15-20"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K-PS3-1 | Tap spots in sun and shade as the morning goes on | the hand's face; the heat camera colors | 2 |
| K-2-ETS1-1 | Ask Mila three questions to set the problem | Mila's answers; the problem card | 3 |
| K-2-ETS1-2 | Sketch where the shade will go before building | the sketch beside the build | 3 |
| K-PS3-2 | Build a shade from parts and run the sun | the moving shadow; cool squares counted | 4 |
| K-2-ETS1-3 | Test a second design and compare on the chart | the picture chart; the pick and reason | 5 |

## Screens and modes
Header (kit): title "Shade Builder"; `Build`, `Class gallery`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A sunny backyard in the morning: a sandbox, a slide, a blacktop path, grass and one small tree. Mila, labeled "illustration", says: "By lunch the sand is too hot for my feet." The welcome is queued (`welcomeAfter: true`): "Let's find out what the sun does. Tap the sand to feel it." First hint: "Tap the sand."

**Feel the sun (focus: the yard).** At 1366x768 the yard fills the screen with the time bar at the bottom; at 680x425 the time bar shrinks to a sun button. Tapping a spot shows a hand with a face: cool, warm or ouch. A sun button moves time to noon; the heat camera tints the yard (sunny spots go from yellow to red, shaded spots stay blue) and each color also shows a face. The tree's shadow is cooler than the sand next to it.

**Set the problem.** Three question buttons for Mila: "When is it hot?" (from late morning), "Where do you sit?" (the middle of the sandbox), "What can't we do?" (no cutting the tree down). A problem card fills with three pictures.

**Sketch and build (K-2-ETS1-2, K-PS3-2).** The student drags shapes onto a top-down sketch of the sandbox, then builds: an umbrella, a small tree, a tent or a sail on posts. Run the sun from morning to afternoon: the shadow moves across the yard, and the sandbox's 36 squares count cool ones. A sun-only spot shows the shade slid off in the afternoon.

**Two designs (the aha).** A second build runs beside the first with the same sun. A picture chart compares them: cool squares at noon, cool squares in the afternoon, did the shade slide off. The student taps the better design and picks a reason picture ("more cool squares", "stays cool later", "Mila can still play"). Narrator: "The sun warms what it shines on. Shade blocks the sun, so the sand stays cool."

**The end.** Both designs, the chart and the pick. `Print` prints them with a coloring page of the yard.

**Class gallery (extra).** Plans made on one device show side by side.

## Content
- One backyard with four surfaces, the hand faces, the heat camera, three Mila questions, four shade parts, two test runs, the picture chart.
- The heat camera is a picture model with faces, not a temperature reading; a caption says so for grown-ups.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The sun runs on a button; parts snap to the sandbox edges.
- Keyboard: Tab to spots, Mila's questions, parts and the sun button; Enter places a part.
- With Motion off the shadow jumps between morning, noon and afternoon.

## Look
- Accent `--brand` #a3430b sun orange (header, the sun button, the chart); gold #f4c542 (the part in hand, the chosen design); paper #fdf4ec; ink #2b1204; muted #61554c.
- Contrast (WCAG 2.1, computed): white on brand 6.24:1; brand on paper 5.74:1; ink on paper 16.23:1; muted on paper 6.64:1; ink on gold 10.84:1.
- Never color alone: heat colors also show faces (cool, warm, ouch); chart bars carry counts and pictures.
- Different from this batch (pond green, sky blue, snail plum, night indigo).

## Art
- Local FLUX (`scripts/localart.py`): the backyard in morning, noon and afternoon light (3, 16:9).
- People (illustrated) for Mila, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Drawn in code: the heat camera overlay, shadows, parts, the hand faces, the sketch and the chart.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Mila; `upbeat-guide` as the builder guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.design + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `feel`: "Tap a spot to feel it."
- how `ask`: "Tap a question for Mila."
- how `sketch`: "Drag a shape to show where the shade goes."
- how `build`: "Drag a part over the sandbox."
- how `sun`: "Press the sun to make the day go by."
- event, whole, each run's cool count.
- how `pick`: "Tap the better shade."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the sun path, shadows, the heat model, parts, the chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Observe | Skip tapping | The build opens after tapping at least one sunny and one shady spot. |
| Build | Cover the whole yard | Parts are a limited set; Mila's "can't" rule still applies. |
| Compare | Pick at random | The reason picture must match the chart. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `feel`.
2. `ask`; `sketch`; `build`; `sun`.
3. Cool count (whole), waits.
4. `pick`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for K-PS3-1, K-PS3-2, K-2-ETS1-1, K-2-ETS1-2, K-2-ETS1-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Sunlit surfaces warm; shaded surfaces stay much cooler | U.S. Environmental Protection Agency, "Using Trees and Vegetation to Reduce Heat Islands" | Vanos and colleagues, "Hot Playgrounds and Children's Health" (Urban Forestry and Urban Greening, 2016) | yes |
| Shadows move across the day as the sun moves across the sky | NASA Space Place, "What causes shadows?" | National Weather Service, "Sun and shadows" education page | yes |
| Shade structures on playgrounds reduce sun and heat | Centers for Disease Control and Prevention, "Shade Planning for America's Schools" | American Academy of Dermatology, "Shade" guidance | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r25, 2026-11-09): the sandbox is 6 by 6, 36 squares; two designs run with the same three sun times; three Mila questions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 yard and time bar; at 680x425 sun button.
2. Taps and the heat camera show sunny spots warming and shady spots staying cool. (K-PS3-1)
3. Three questions to Mila and a sketch come before building. (K-2-ETS1-1, K-2-ETS1-2)
4. A build is tested from morning to afternoon with cool squares counted. (K-PS3-2)
5. Two designs are compared on the picture chart with a reason. (K-2-ETS1-3)
6. Every card is spoken; heat colors also show faces.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: shadows jump; no network requests.

## Open questions
None.
