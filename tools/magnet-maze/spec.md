# Magnet Maze

## One idea
On a tabletop maze a steel ball sits at the start and a star waits at the end, and the student can't touch the ball: they place and turn bar magnets on the outside of the maze walls to pull it along, and before each level they answer one cause-and-effect question with a prediction ("Will it still pull from twice as far?", "What happens if the magnet is flipped?", "Will it pull through cardboard? Through a wooden block?"), then play to check; some pieces in the maze are aluminum or copper and never move; in static levels the student rubs a balloon on a wool sweater to pick up paper bits, bend a thin stream of water and push a second rubbed balloon away, and a charge meter shows how more rubbing and closer distance change the pull; at the design level three short problem stories (a cabinet door that swings open, steel cans mixed with aluminum cans at a recycling center, a toolbox lid that loses its screws) ask the student to choose one, write what the fix must do and what limits it, then build and test a magnet fix, so a third grader learns to ask questions that find cause and effect in magnetic and electric pulls between objects that don't touch, and to define a simple design problem that magnets can solve.

## Not like
- tug-of-war-arena (3, spec): pulls by touch on a rope. Here pulls without touching.
- electromagnet-lab (8, spec): making a magnet stronger with current. Here what changes a magnet's pull.
- contraption-workshop (4, concept): energy chains in a device. Here one force to steer one ball.
- push-the-pumpkin (K, spec): push size and direction. Here forces across a gap.

## Who and how
- Grade 3, Science, module "Magnets and Static Electricity". Standards: 3-PS2-3 (ask questions to determine cause and effect relationships of electric or magnetic interactions between two objects not in contact with each other), 3-PS2-4 (define a simple design problem that can be solved by applying scientific ideas about magnets).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Nine magnet levels in three sets (distance, which pole faces, what is in between), three static levels, the design level with three stories, the level map. Extra: Class question (the class votes on each level's prediction). tool.json `modes: ["Maze", "Class question"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-PS2-3 (magnetic) | Predict and test how distance, pole direction and material between change the pull | the ball moving or not; field lines | 2 |
| 3-PS2-3 (electric) | Rub balloons more or less and bring them closer or farther | the charge meter; paper, water and balloon moving | 3 |
| 3-PS2-4 | Write criteria and limits for a problem, then build and test a magnet fix | the design card; the test result | 4 |

## Screens and modes
Header (kit): title "Magnet Maze"; `Maze`, `Class question`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wooden tabletop maze seen from above, a steel ball at the start, a gold star at the end, and a tray with two bar magnets marked N and S. The welcome is queued (`welcomeAfter: true`): "Get the ball to the star. You can't touch it. Drag a magnet to the edge of the maze." First hint: "Drag a magnet next to the ball."

**Magnet levels (focus: the maze).** At 1366x768 the maze fills the left with the question card and level map right; at 680x425 the card is a sheet. Each level opens with a question and three answer choices. The student places and turns magnets; the ball rolls toward a pull and stops when the pull is too weak. A `Field` switch draws field lines.
- Distance set: the same magnet one, two and four squares away; the pull fades fast with distance.
- Pole set: the ball now rides in a small cart with its own magnet. Facing the same poles pushes the cart away and facing opposite poles pulls it close. A plain steel ball is pulled by either pole, and the card says so.
- Between set: cardboard, a wooden block, a plastic sheet and an aluminum plate between magnet and ball; the pull goes through all of them. Aluminum and copper coins on the floor never move.

**Static levels (3-PS2-3).** A balloon and a wool sweater. Tap and drag to rub; the charge meter rises with each rub. Three tests: pick up paper bits, bend a thin stream of water from a faucet, push a second rubbed balloon away. Closer means a stronger pull or push; more rubbing means more charge. A note says static charge leaks away on damp days.

**Design level (3-PS2-4).** Three stories, each with a picture: a cabinet door that keeps swinging open, a recycling center where steel and aluminum cans are mixed, a toolbox lid that loses its screws. The student picks one and fills a card: "The fix must ___ (criteria). It can't ___ (limits, such as cost, size, or must still open easily)." Then they build from parts (magnets of three strengths, a strip, a belt) and test. The test shows if the criteria are met.

**The level map (the aha).** Every question with the student's answer and the test result. Narrator: "Magnets and charges can pull and push without touching. You found out what makes that pull stronger or weaker, and you used it to fix a real problem."

**The end.** The level map and the design card. `Print` prints them.

**Class question (extra).** The class votes before each level.

## Content
- Nine magnet levels, three static levels, three design stories, parts with stated strengths, the level map.
- The model's pull falls off with distance on a stated rule; it is shown, not measured.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Magnets snap to grid edges; a second tap turns a magnet end for end.
- Keyboard: Tab to magnets, grid edges, the question choices, `Field`, the balloon and the design card; arrow keys move the held magnet; Enter places.
- With Motion off the ball jumps to where it stops and field lines appear without drawing.

## Look
- Accent `--brand` #b3261e magnet red (header, the N pole, the level map); gold #f4c542 (the star, the held magnet); paper #fdf1f0; ink #2a0907; muted #5e5150.
- Contrast (WCAG 2.1, computed): white on brand 6.54:1; brand on paper 5.92:1; ink on paper 16.67:1; muted on paper 6.87:1; ink on gold 11.32:1.
- Never color alone: poles carry the letters N and S; the charge meter carries a number; materials carry names.
- Different from this batch (collar green, postcard orange, ocean navy, lane indigo).

## Art
- Local FLUX (`scripts/localart.py`): the maze table (1, 16:9), the balloon and sweater (1, 4:3), three problem stories (3, 4:3).
- Drawn in code: the maze grid, magnets, the ball, field lines, the charge meter, paper bits, the water stream, parts.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as the maze buddy and hints; `calm-professor` as the question card and design level. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Pick your answer, then tap Play."
- how `place`: "Drag a magnet to the edge of the maze."
- event, whole, each level's result.
- how `rub`: "Drag the balloon on the sweater."
- how `design`: "Pick a problem and write what the fix must do."
- how `test`: "Tap Test to try your fix."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the grid, the pull rule, field lines, the charge meter, the design checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Levels | Skip the prediction | Play stays off until a choice is picked. |
| Maze | Drop magnets everywhere | Each level has a limit of two magnets. |
| Design | Build without a card | Test stays off until criteria and limits are written. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `place`.
2. Result (whole), waits.
3. `rub`; `design`; `test`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-PS2-3, 3-PS2-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Like poles push apart, opposite poles pull; pull weakens with distance; passes through paper, wood, plastic | National High Magnetic Field Laboratory, "Magnet Academy" | NASA, "Magnetism" (Imagine the Universe) | yes |
| Aluminum and copper are not pulled by a magnet | National High Magnetic Field Laboratory, "Magnet Academy" | U.S. Geological Survey, "Magnetic properties of minerals and metals" | yes |
| Rubbed balloons pick up paper, bend water and push each other apart | The Physics Classroom, "Static Electricity" | NASA Jet Propulsion Laboratory, "Static electricity" classroom activity | yes |
| Recycling centers use magnets to pull steel cans from aluminum | U.S. Environmental Protection Agency, "How do recycling facilities work" | Steel Recycling Institute, "Steel can recycling" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r28, 2026-11-09): nine magnet levels in three sets of three plus three static levels is twelve; three design stories; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 maze and card; at 680x425 sheet.
2. Nine magnet levels test distance, pole direction and material between, each after a prediction. (3-PS2-3)
3. Three static levels show charge and distance changing the pull. (3-PS2-3)
4. A design problem is written with criteria and limits and a magnet fix is tested. (3-PS2-4)
5. Aluminum and copper pieces never move.
6. The level map lists every question and result.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: end positions only; no network requests.

## Open questions
None.
