# Pizza Party

## One idea
At a party table guests arrive two or four at a time, and the child drags a cutter across a round pizza or a rectangle sandwich to share it fairly, while the tool shows each piece's size; fair shares get a happy bite sound and a thumbs up, and an uneven cut gets a funny complaint ("Hey, his half is bigger!") before the pieces slide back together to try again; shares get named out loud (halves, half of, fourths, fourth of, quarters, quarter of), and a sandwich can be cut into halves two ways (two rectangles or two triangles), both fair; in the big moment the same pizza is cut for 2 guests and then for 4, the pieces sit side by side and the fourths are smaller, which surprises children who think 4 is bigger than 2; every cut pizza slides back together into one whole, so a first grader learns to partition circles and rectangles into two and four equal shares, to name the shares with the words halves, fourths and quarters, to describe the whole as two of, or four of, the shares, and to see that more equal shares make smaller shares.

## Not like
- garden-grid (2, concept): rows, columns and thirds. Here only halves and fourths.
- fraction-trail (3, concept): fractions as numbers on a line. Here fair shares of food.
- recipe-scaler (4, concept): the same family later, multiplying fractions. Here first equal shares.
- picky-robot-shapes (1, spec): shape attributes and composing. Here cutting into equal parts.

## Who and how
- Grade 1, Math, module "Halves and Fourths". Standards: 1.G.3 (partition circles and rectangles into two and four equal shares, describe the shares using the words halves, fourths, and quarters, and use the phrases half of, fourth of, and quarter of; describe the whole as two of, or four of the shares; understand for these examples that decomposing into more equal shares creates smaller shares).
- Format: builder. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Six pizzas and six sandwiches, two-guest and four-guest tables, the two-ways sandwich, the 2 then 4 pizza, the rebuild. Extra: Party plan (the child picks guests and food, still only 2 or 4 guests; thirds wait for grade 2). tool.json `modes: ["Party", "Party plan"]`, `minutes: "10-15"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.G.3 (partition) | Drag cut lines on circles and rectangles | piece sizes; fair or not | 2 |
| 1.G.3 (name the shares) | Hear and tap the share words | halves, fourths, quarters; "two of the halves make the whole" | 3 |
| 1.G.3 (more shares, smaller) | Cut one pizza for 2, then for 4 | halves beside fourths | 4 |

## Screens and modes
Header (kit): title "Pizza Party"; `Party`, `Party plan`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A bright party table with balloons, a round pizza on a board, a pizza cutter, two cartoon kids at the table. The welcome is queued (`welcomeAfter: true`): "Two friends are here! Cut the pizza so it's fair. Drag the cutter across the pizza." First hint: "Drag the cutter across the pizza."

**Cutting (focus: the food).** At 1366x768 the food fills the middle with guests around it and share words below; at 680x425 guests become small faces along the top. A cut line snaps to the center when close. Pieces show a size bar. Fair: each guest gets a piece with a happy bite sound (no actual eating shown, the piece just moves to the plate). Uneven: "Hey, his half is bigger!" and the pieces slide back.

**Naming.** After each fair cut, a card: "Each friend gets one half. Two halves make the whole pizza." For four: "one fourth, or one quarter. Four fourths make the whole."

**Two ways (sandwich).** A rectangle sandwich: one cut straight down, then a new sandwich cut corner to corner. "Both are halves! Each friend gets the same amount."

**Two then four (the aha).** The same pizza, cut for 2, then a twin pizza cut for 4. The pieces line up: "Four friends, smaller pieces! More shares make smaller shares."

**Rebuild.** `Put it back` slides the pieces into one whole.

**The end.** A party photo with each fair share and its name. `Print` prints a cutting page.

**Party plan (extra).** The child picks 2 or 4 guests and pizza or sandwich.

## Content
- Circles and rectangles, 2 and 4 equal shares, the share words, all spoken. Made-up cartoon kids labeled "illustration". No thirds or odd guest counts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Put it back` and `Try again` work at any time.
- Keyboard: Tab to the cutter, cut spots around the edge, and buttons; Enter starts and ends a cut.
- With Motion off pieces jump to plates and back.

## Look
- Accent `--brand` #a33219 tomato red (header, the cutter, buttons); gold #f4c542 (a fair cut, the piece in hand); paper #fdf3ef; ink #2b0d05; muted #5f4f49.
- Contrast (WCAG 2.1, computed): white on brand 6.94:1; brand on paper 6.36:1; ink on paper 16.55:1; muted on paper 7.12:1; ink on gold 11.11:1.
- Never color alone: fair pieces get a check and equal size bars.
- Different from this batch (notebook navy, ballot violet, circuit green, brass brown).

## Art
- People (illustrated): four cartoon kids from different families, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Local FLUX (`scripts/localart.py`): the party table (1, 16:9), a pizza and a sandwich from above (2, 1:1).
- Drawn in code: cut lines, pieces, size bars, share cards.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as the guests' complaints and cheers; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.food + ':' + state.guests + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `cut`: "Drag the cutter across the food."
- how `again`: "Tap Try again."
- how `back`: "Tap Put it back."
- event, whole, each share name.
- event, whole, two then four.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-food (family "fraction-food"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* FRACTION-FOOD ENGINE: begin */ ... /* end */`: circle and rectangle foods, snapping cut lines, piece areas with a fairness check, and share names; recipe-scaler reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Cut | Cut anywhere | Uneven pieces get the complaint and slide back. |
| Four | Cut 4 pieces of any size | Only equal fourths pass. |
| Name | Ignore the words | Each card is spoken and printed with the pieces. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `cut`.
2. Share name (whole), waits. `again` if needed.
3. Two then four (whole), waits.
4. `back`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.G.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Fair sharing is the natural start for fractions in grade 1 | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-6 Geometry" | Empson (1999), "Equal sharing and shared meaning", Cognition and Instruction | yes |
| Young children often think more pieces means bigger pieces | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Empson (1999), "Equal sharing and shared meaning", Cognition and Instruction | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-10): a fourth is less than a half; two halves and four fourths each make one whole; halves are 180 degrees and fourths 90; both sandwich cuts give equal halves; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 food and guests; at 680x425 faces on top.
2. Circles and rectangles are cut into two and four equal shares. (1.G.3)
3. Every fair share is named and the whole is described as two or four shares. (1.G.3)
4. The 2 then 4 pizza shows more shares are smaller. (1.G.3)
5. Every card is spoken; every control is 56 px or more.
6. The kids are labeled illustration; no thirds or odd guest counts.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
- The idea card moves 1.G.1 and 1.G.2 out (default used: they go to picky-robot-shapes; this tool teaches 1.G.3 only).
