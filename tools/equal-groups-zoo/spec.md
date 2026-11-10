# Equal Groups Zoo

## One idea
At feeding time a zookeeper, Ms. Ama (made up, labeled "illustration"), gives jobs from a food cart ("5 otters each get 3 fish"), and the child drags food into equal groups while four linked panels change together: the picture of groups, an array of dots, a skip-count (3, 6, 9, 12, 15) and an equation (5 x 3 = 15); division jobs run the same feeding backward in two ways, sharing (24 fish for 6 penguins, how many each?) and grouping (24 fish, 4 per penguin, how many penguins?), each written as 24 / 6 = ? and 6 x ? = 24; array tricks let the child rotate an array (5 x 3 becomes 3 x 5 with the same total), split a 7 x 8 array into 5 x 8 and 2 x 8 with a slider, and group three factors in different orders (2 x 3 x 4); word-problem jobs come with unknowns in every spot; at the end a feeding log shows a division and its missing-factor partner on the same picture, so a third grader learns to see products as equal groups, quotients as sharing or grouping, to solve multiplication and division word problems within 100 with drawings and equations, to find the unknown in any position, to use the commutative, associative and distributive properties as strategies, and to understand division as an unknown-factor problem.

## Not like
- multiplication-dungeon (3, concept): fluency with facts. Here what multiplying and dividing mean.
- garden-grid (2, spec): rows and columns as geometry. Here arrays as multiplication.
- egg-carton-factory (4, spec): factor pairs. Here equal groups and sharing.
- tile-the-floor (3, spec): arrays as area. Here arrays as groups of things.

## Who and how
- Grade 3, Math, module "Meaning of Multiplication and Division". Standards: 3.OA.1 (interpret products of whole numbers, e.g., 5 x 7 as the total number of objects in 5 groups of 7 objects each), 3.OA.2 (interpret whole-number quotients as the number of objects in each share when partitioned equally, or as the number of shares), 3.OA.3 (use multiplication and division within 100 to solve word problems in situations involving equal groups, arrays, and measurement quantities), 3.OA.4 (determine the unknown whole number in a multiplication or division equation relating three whole numbers), 3.OA.5 (apply properties of operations as strategies to multiply and divide), 3.OA.6 (understand division as an unknown-factor problem).
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six animal pens, twelve feeding jobs, eight division jobs (four sharing, four grouping), six word jobs with unknowns in every spot, three array tricks, the feeding log. Extra: Free zoo (the child writes a feeding story and the panels follow). tool.json `modes: ["Zoo", "Free zoo"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.OA.1, 3.OA.3 | Drag food into equal groups | four linked panels | 2 |
| 3.OA.2, 3.OA.4, 3.OA.6 | Share and group food; find the missing number | 24 / 6 and 6 x ? = 24 on one picture | 3 |
| 3.OA.5 | Rotate, split and regroup arrays | 5 x 3 = 3 x 5; 7 x 8 = 5 x 8 + 2 x 8 | 4 |

## Screens and modes
Header (kit): title "Equal Groups Zoo"; `Zoo`, `Free zoo`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny zoo map with six pens (otters, penguins, flamingos, goats, tortoises, parrots), a food cart and Ms. Ama with a clipboard. The welcome is queued (`welcomeAfter: true`): "Feeding time! 5 otters each get 3 fish. Drag fish to the otters." First hint: "Drag a fish to an otter."

**Feeding (focus: the pen).** At 1366x768 the pen is on the left and the four panels stack on the right; at 680x425 the panels become tabs under the pen. As fish land, the array fills, the skip-count grows, the equation updates. Uneven groups: "That otter got 4 and this one got 2. Equal groups, please!"

**Division jobs.** Sharing: 24 fish, 6 penguins; the child deals fish one at a time. Grouping: 24 fish, 4 per penguin; penguins waddle in until the fish run out. Both write 24 / 6 = 4 or 24 / 4 = 6 and the missing-factor partner.

**Word jobs.** "A keeper fills 4 buckets with the same number of carrots. 28 carrots in all. How many in each?" The equation has a box for the unknown in any spot.

**Array tricks.** `Turn` rotates an array; `Split` slides a line through 7 x 8 to show 5 x 8 + 2 x 8; `Group` regroups 2 x 3 x 4 two ways.

**Missing factor (the aha).** The same penguin picture shows 24 / 6 = ? and 6 x ? = 24. Ms. Ama: "Dividing is finding the missing factor."

**The end.** The feeding log. `Print` prints it.

**Free zoo (extra).** The child writes a feeding story; the panels follow.

## Content
- Six animals with their real foods (otters fish, penguins fish, flamingos shrimp pellets, goats hay, tortoises greens, parrots seeds), products within 100, all readable with `Read`. Animals only eat food; no animal is food.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Food can be dragged back to the cart at any time.
- Keyboard: Tab to the cart, each animal, panel tabs and buttons; Enter gives one food; number keys fill the box.
- With Motion off food jumps to animals and penguins appear instead of waddling.

## Look
- Accent `--brand` #24426e penguin navy (header, panels, buttons); gold #f4c542 (the food in hand, the unknown box); paper #f0f3f8; ink #0b1424; muted #4c5466.
- Contrast (WCAG 2.1, computed): white on brand 10.10:1; brand on paper 9.08:1; ink on paper 16.57:1; muted on paper 6.82:1; ink on gold 11.33:1.
- Never color alone: groups carry outlines and counts.
- Different from this batch (mural magenta, backyard green, picnic red, newsletter teal).

## Art
- People (illustrated): Ms. Ama, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the zoo map (1, 16:9), six animals (6, 1:1), six foods (6, 1:1).
- Drawn in code: arrays, the skip-count strip, equations, split lines.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Ms. Ama; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.pen + ':' + state.job + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `feed`: "Drag food to an animal."
- how `share`: "Deal the food one at a time."
- how `solve`: "Type the missing number."
- how `trick`: "Tap Turn, Split or Group."
- event, whole, the missing factor.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
arrays (family "arrays"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* ARRAYS ENGINE: begin */ ... /* end */`: groups linked to an array, a skip-count strip and an equation, array rotate, split and regroup, and missing-factor equations; later arrays tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Groups | Drop food unevenly | The panels wait until groups are equal. |
| Missing number | Type guesses | The picture shows what the guess would make. |
| Split | Slide anywhere | Any split is allowed; the two products always add to the whole, which is the point. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `feed`.
2. `share`; `solve`.
3. `trick`.
4. Missing factor (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.OA.1 to 3.OA.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Equal groups, arrays, sharing and grouping are the core meanings | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking", Table 3 | Greer (1992), "Multiplication and division as models of situations", in Handbook of Research on Mathematics Teaching and Learning | yes |
| Arrays make the commutative and distributive properties visible | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Battista and others (1998), "Students' spatial structuring of 2D arrays of squares", Journal for Research in Mathematics Education | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-10): 5 x 3 = 15 = 3 x 5 with skip-count 3 to 15; 24 / 6 = 4, 24 / 4 = 6 and 6 x 4 = 24; 7 x 8 = 5 x 8 + 2 x 8 = 56; (2 x 3) x 4 = 2 x (3 x 4) = 24; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 pen and panels; at 680x425 panel tabs.
2. Twelve feeding jobs update all four panels. (3.OA.1, 3.OA.3)
3. Eight division jobs and six word jobs find unknowns in any spot. (3.OA.2, 3.OA.4, 3.OA.6)
4. Rotate, split and regroup tricks are used. (3.OA.5)
5. `Read` reads every card; every control is 48 px or more.
6. Ms. Ama is labeled illustration; animals eat their real foods.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
