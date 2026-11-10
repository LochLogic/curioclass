# Deep Sea Dive

## One idea
At the end of a pier the child maps a rocky coast in cross-section with a diver, Noa (made up, labeled "illustration"): a vertical number line has sea level at 0, a gull at +8 m and Noa at -12 m, and the first question, "Who is farther from the surface?", is answered with absolute value (12 against 8); number-line rounds place creatures and gear at positive and negative heights, pair opposites (+5 and -5 meet at 0), order them, and read -3 > -7 as "-3 m is higher than -7 m", and a sort separates "the diver is deeper" (order) from "the diver is farther from the surface" (absolute value); opposite cards carry signs to other places (a dive shop account at -30 dollars is a debt of 30; water at -2 degrees C); chart rounds widen the map into a coordinate plane with east of the pier positive, so a kelp bed at (-4, -6) and a lighthouse at (3, 10) sit in quadrants named by their signs, and points reflect across the water line or the pier line; distance rounds find that a gull at (2, 6) straight above a fish at (2, -5) is 11 m away; at the end the child sees a negative number as a direction as well as a size, and absolute value as the size alone, so a sixth grader learns signed numbers in context, opposites, ordering and absolute value, and the four-quadrant plane.

## Not like
- hot-air-and-sandbags (7, concept): adding and subtracting signed numbers. Here placing and comparing them.
- sea-search-grid (5, spec): the first quadrant only. Here all four.
- square-root-hunt (8, concept): irrationals on the same number-line engine. Here integers and rationals.
- roller-coaster-rounding (3, spec): a horizontal line of whole numbers. Here a vertical line through zero.

## Who and how
- Grade 6, Math, module "Negative Numbers". Standards: 6.NS.5 (understand that positive and negative numbers are used together to describe quantities having opposite directions or values (e.g., temperature above/below zero, elevation above/below sea level, credits/debits, positive/negative electric charge); use positive and negative numbers to represent quantities in real-world contexts, explaining the meaning of 0 in each situation), 6.NS.6 (understand a rational number as a point on the number line; extend number line diagrams and coordinate axes to represent points on the line and in the plane with negative number coordinates: opposites, signs of coordinates as quadrants, reflections across one or both axes, finding and positioning numbers and ordered pairs), 6.NS.7 (understand ordering and absolute value of rational numbers: inequalities as positions, statements of order in real-world contexts, absolute value as distance from 0, distinguishing comparisons of absolute value from statements about order), 6.NS.8 (solve real-world and mathematical problems by graphing points in all four quadrants of the coordinate plane, including using coordinates and absolute value to find distances between points with the same first coordinate or the same second coordinate).
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight number-line rounds, six opposite cards, eight chart rounds with reflections, six distance rounds. Extra: Dive log (the class plots a shared dive log on the projector). tool.json `modes: ["Coast", "Dive log"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.NS.5 | Place heights; read signs in other contexts | 0 as sea level, zero balance, freezing | 2 |
| 6.NS.6, 6.NS.7 | Pair opposites; order; sort order from absolute value | the vertical line; distance arrows to 0 | 2 |
| 6.NS.6 | Plot in four quadrants; reflect | the water line and pier line as mirrors | 3 |
| 6.NS.8 | Find distances between points sharing a coordinate | |6| + |-5| = 11 as two arrows | 4 |

## Screens and modes
Header (kit): title "Deep Sea Dive"; `Coast`, `Dive log`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cross-section of a rocky coast: sky above, sea below, a seabed, a pier with a vertical number line at its end, a gull at +8 and Noa at -12. The welcome is queued (`welcomeAfter: true`): "Who is farther from the surface, the gull or Noa? Tap one." First hint: "Tap the gull or Noa."

**Number line (focus: the line).** At 1366x768 the line runs top to bottom on the left with the scene right and cards below; at 680x425 cards are a sheet. The child drags creatures and gear to heights from cards (a crab at -9.5, a pelican at +3 1/2). Distance arrows to 0 appear on tap. Order rounds line up four items; the child types the inequality and reads it aloud in words. The sort sends claims into "order" or "distance from the surface".

**Opposites.** Cards from other places: a dive shop account, water temperature, a cave above and below the tide line. For each the child says what 0 means and places the opposite.

**Chart.** The line tips into a coordinate plane: x as meters east of the pier, y as height. The child plots points from cards, names quadrants by signs, and reflects points across the water (x-axis) or the pier (y-axis); the reflected point shows a dashed mirror path.

**Distance.** A gull at (2, 6) above a fish at (2, -5): the child adds the two distances to the water line, 6 + 5 = 11. Buoys and boats on the same height line work the same way across.

**Direction and size (the aha).** Noa: "A minus sign tells you which way. Absolute value tells you how far."

**The end.** The coast map. `Print` prints it.

**Dive log (extra).** The class plots one dive together.

## Content
- Heights and positions in whole numbers, halves and tenths from -20 to +20, all readable with `Read`.
- The sea is calm and friendly; nothing is in danger.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Items can be moved until `Check`.
- Keyboard: Tab to items, the line (arrows move by 1, shift and arrows by 0.5), the plane (arrows move a point), cards and answer boxes; Enter places or checks.
- With Motion off the line becomes the plane at once and reflections jump.

## Look
- Accent `--brand` #13406b deep-sea navy (header, axes, buttons); gold #f4c542 (the item in hand, distance arrows); paper #ecf2f8; ink #061629; muted #4c5562.
- Contrast (WCAG 2.1, computed): white on brand 10.64:1; brand on paper 9.44:1; ink on paper 16.13:1; muted on paper 6.69:1; ink on gold 11.18:1.
- Never color alone: signs are always written; above and below carry words.
- Different from this batch (awning orange, measuring-cup teal, trellis green, market plum).

## Art
- People (illustrated): Noa in dive gear, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the coast cross-section (1, 16:9), eight creatures and items (8, 1:1).
- Drawn in code: the number line, the plane, arrows and mirror paths.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Noa; `wise-mentor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag the item to its height."
- how `order`: "Type the inequality."
- how `sort`: "Drag the claim to Order or Distance."
- how `plot`: "Tap the plane at the card's point."
- how `reflect`: "Tap Reflect, then pick a mirror."
- event, whole, direction and size.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-line (`kit/number-line.js`), as described in roller-coaster-rounding's spec. Uses `NumberLine` turned vertical (-20 to 20, ticks every 1 and 5), `nl.x` to place items, `nl.span` for distance-to-zero arrows, `nl.mark` for guesses, `nl.on('tap')`. The four-quadrant chart uses the coordinate engine's `CoordPlane` with `quadrant: 'all'` and `snap: 0.5` (coordinate-proof-lab's spec). Tool-only code: the scene, the claim sort, mirror paths.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Order by the digits | -12 against -3 is checked as lower. |
| Sort | Call every claim order | The deck mixes both, and each is checked. |
| Distance | Subtract the coordinates as written | 6 - 5 = 1 is caught; the arrows show two parts. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`; `order`; `sort`.
2. `plot`; `reflect`.
3. Distance rounds use `plot`.
4. Direction and size (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.NS.5 to 6.NS.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Students confuse order with absolute value for negatives | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | Bofferding (2014), "Negative integer understanding: characterizing first graders' mental models", Journal for Research in Mathematics Education | yes |
| Sea level is the zero of elevation | NOAA, "What is sea level?" (National Ocean Service) | USGS, "Elevation" glossary | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s17, 2026-11-10): |-12| > |8|; -3 > -7; (2, 6) to (2, -5) is 6 - (-5) = 11; (-4, -6) is in quadrant III and (3, 10) in quadrant I; (3, 10) reflects to (3, -10) and (-3, 10); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line, scene and cards; at 680x425 cards as a sheet.
2. Items are placed, opposites paired, order written and claims sorted from absolute value. (6.NS.5, 6.NS.6, 6.NS.7)
3. Points are plotted in all four quadrants and reflected across both axes. (6.NS.6)
4. Distances between points sharing a coordinate are found. (6.NS.8)
5. Noa is labeled illustration; nothing in the scene is in danger.
6. `Read` reads every card and every position; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the plane appears at once; no network requests.

## Open questions
None.
