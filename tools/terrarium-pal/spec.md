# Terrarium Pal

## One idea
A glass terrarium sits on a windowsill with a bean plant, a land snail named Pip and a pill bug named Roly (both made up), and a care tray holds a water drop, a lamp, a lettuce leaf and a lid with air holes; over a sped-up week the student chooses each day what to give each living thing and taps to the next day; the plant perks up or droops, Pip comes out or tucks into its shell, Roly wanders or curls up; a picture log keeps each day with a face for each one; try-it cards ask "What if the plant gets lettuce but no light?" and the plant can't use the lettuce and droops, so light is what it needs; at the end the student places the plant, the snail, the pill bug and a child on a sorting board (needs water, needs air, needs food, needs light) using the log as evidence, so a kindergartner learns the pattern that all living things need water and air, animals need to eat, and plants need light instead of food.

## Not like
- plant-experiment-shelf (2, concept): a fair test of light and water, same engine. Here caring for a jar over a week.
- beaver-builders (K, spec): animals changing a place. Here what living things need.
- who-s-my-baby (1, concept): babies and parents. Here needs.
- weather-wardrobe (K, spec): what people wear. Here what living things need.

## Who and how
- Kindergarten, Science, module "What Living Things Need". Standards: K-LS1-1 (use observations to describe patterns of what plants and animals, including humans, need to survive).
- Format: creature. Driver: one child with a grown-up nearby, or the class on the projector (tool.json `driver: "either"`). Every card is spoken. Controls 64 px or more.
- Seven days of care, four try-it cards, the picture log, the sorting board. Extra: Class care (the class votes each day's care on the projector). tool.json `modes: ["Care", "Class care"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K-LS1-1 (observe) | Give or hold back water, light, food and air each day | the plant, snail and pill bug changing; the picture log | 2 |
| K-LS1-1 (test) | Try a card that swaps one need | the plant ignoring lettuce; the snail tucking in without water | 3 |
| K-LS1-1 (pattern) | Sort four living things by what they need, using the log | the sorting board | 4 |

## Screens and modes
Header (kit): title "Terrarium Pal"; `Care`, `Class care`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A glass terrarium on a sunny windowsill: a small bean plant, Pip the snail on a stone, Roly the pill bug under a leaf. The care tray: a water drop, a lamp, a lettuce leaf, a lid with air holes. The welcome is queued (`welcomeAfter: true`): "These three live in the jar. What do they need? Pick something to give, then tap to the next day." First hint: "Drag something from the tray to the jar."

**A day of care (focus: the jar).** At 1366x768 the jar fills the left with the tray and log right; at 680x425 the log is a sheet. The student drags items to each living thing (or the whole jar). A big `Next day` button moves on. The plant perks up with water and light, droops without them; Pip comes out with damp air and food, tucks into its shell when dry or hungry; Roly wanders when the soil is damp and there are old leaves, curls up when dry. The lid with holes gives air; a closed lid with no holes makes all three slow and sleepy, and the narrator explains air.

**Try-it cards (the test).** Four cards change one thing:
1. "The plant gets lettuce but no light." The plant droops; lettuce doesn't help it.
2. "Pip gets light but no water." Pip tucks in.
3. "The lid has no holes." Everyone slows down.
4. "Roly gets old leaves and damp soil." Roly wanders and eats.
- After each, everything recovers with care.

**The sorting board (the aha).** Four columns with pictures: needs water, needs air, needs food, needs light. The student drags the plant, Pip, Roly and a child into every column that fits, tapping a log day as proof. Narrator: "Every living thing needs water and air. Animals need to eat. Plants make their own food with light."

**The end.** The log and the sorting board. `Print` prints them as a picture page.

**Class care (extra).** The class votes each day's care on the projector.

## Content
- One terrarium, three living things, four tray items, seven days, four try-it cards, the sorting board with four living things.
- Nothing dies on screen: a neglected snail stays in its shell, a pill bug curls up, the plant wilts, and all recover with care.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drags snap to the living thing or the jar; a wrong drop slides back with a spoken hint.
- Keyboard: Tab to tray items, the jar, `Next day`, cards and the board; Enter picks up and places.
- With Motion off the plant and animals change pose without animating.

## Look
- Accent `--brand` #7a4a8c snail plum (header, the tray, the log); gold #f4c542 (the item in hand, today in the log); paper #f8f2fa; ink #22102a; muted #5c5262.
- Contrast (WCAG 2.1, computed): white on brand 6.59:1; brand on paper 5.99:1; ink on paper 16.22:1; muted on paper 6.72:1; ink on gold 10.98:1.
- Never color alone: faces show how each one is doing; columns carry pictures and spoken names.
- Different from this batch (pond green, sun orange, sky blue, night indigo).

## Art
- Local FLUX (`scripts/localart.py`): the terrarium on a windowsill (1, 16:9).
- Illustrated living things with states: the plant (perky, droopy), Pip (out, tucked in), Roly (wandering, curled), a child (Gemini, 4 characters with state sheets; cutout yes; the child labeled "illustration", `people: true`).
- Drawn in code: the tray, the log, the sorting board.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Pip the snail; `easy-coach` as the care guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `give`: "Drag something from the tray to the jar."
- how `next`: "Tap Next day."
- event, whole, each day's change.
- event, whole, each try-it card.
- how `sort`: "Drag each one to what it needs."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
terrarium (family "terrarium"; no engine file yet). This tool builds the terrarium family's shared pieces first, in a marked block `/* TERRARIUM DATA: begin */ ... /* end */`: the living-thing states, the need rules and the picture log; plant-experiment-shelf reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Care | Give everything every day | Allowed; the try-it cards still show what each one really needs. |
| Try-it | Skip them | The sorting board opens after all four cards. |
| Sorting | Put everything everywhere | The plant in "needs food" is checked; the hint points to try-it card 1. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `give`; `next`.
2. Day change (whole), waits.
3. Try-it cards (whole).
4. `sort`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for K-LS1-1, and that plants do not need to take in food | NGSS Lead States, "Next Generation Science Standards" (2013), K-LS1-1 clarification | data/standards/ngss-pes.txt | yes |
| Plants make their own food using light | NASA Earth Observatory, "Photosynthesis" | U.S. Department of Agriculture, "How plants grow" | yes |
| Land snails need moisture and retreat into the shell when dry | Smithsonian Environmental Research Center, "Land snails" | University of Florida IFAS, "Featured Creatures: land snails" | yes |
| Pill bugs need damp places, eat decaying leaves and roll up | University of Florida IFAS, "Featured Creatures: pillbug" | University of Kentucky Entomology, "Sowbugs and Pillbugs" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r25, 2026-11-09): seven days; four try-it cards each change one thing; the plant fits three of four columns and the animals and child each fit three; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 jar and tray; at 680x425 sheet.
2. Seven days of care show changes in all three living things in the log. (K-LS1-1)
3. Four try-it cards each change one thing and recover. (K-LS1-1)
4. The sorting board puts four living things by their needs with a log day as proof. (K-LS1-1)
5. Nothing dies on screen.
6. Every card is spoken; controls are 64 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pose changes only; no network requests.

## Open questions
None.
