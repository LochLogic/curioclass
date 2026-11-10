# Expression Garden

## One idea
In a community garden the gardener, Mr. Delgado (made up, labeled "illustration"), hands the child a bin of bed tiles (single plants, x-long rows, square beds of s^2 and cube planters of s^3) and asks for 3 rows of (x + 2); the child lays them out and the expression writes itself and names its parts (terms, coefficients, factors), then regroups the same plants as 3 x-strips and 6 singles, so 3(x + 2) = 3x + 6; count rounds set x = 4 and a plant counter fills every bed (18 plants either way), and formulas are evaluated for a cube planter of side 2 (V = s^3 holds 8 cubic feet of soil, A = 6s^2 takes 24 square feet of boards); exponent rounds make 3^2 and 2^3 real as a 3 by 3 bed and a 2 by 2 by 2 planter, and expressions with exponents follow the order of operations (2 + 3^2 x 2 = 20); equivalence rounds ask whether 24x + 18y is the same garden as 6(4x + 3y) by rearranging into 6 identical plots; a trap pair, x + x and x^2, agrees at x = 2 (4 plants each), but the counter at x = 3 shows 6 against 9; at the end the child sees that equivalent expressions are the same garden arranged differently and that one matching value is not proof, so a sixth grader learns to write and evaluate expressions with exponents and variables, use their vocabulary, and generate and identify equivalent expressions.

## Not like
- expression-match (7, concept): equivalent expressions with rational coefficients, same tile engine. Here whole numbers and exponents.
- algebra-tile-studio (9, spec): factoring quadratics. Here the distributive property and like terms.
- expression-escape (5, spec): numerical expressions and grouping. Here letters for numbers.
- community-plot-planner (4, spec): area and perimeter of garden plots. Here plants counted by expressions.

## Who and how
- Grade 6, Math, module "Expressions and Exponents". Standards: 6.EE.1 (write and evaluate numerical expressions involving whole-number exponents), 6.EE.2 (write, read, and evaluate expressions in which letters stand for numbers: a. write expressions that record operations with numbers and with letters standing for numbers; b. identify parts of an expression using mathematical terms (sum, term, product, factor, quotient, coefficient); view one or more parts of an expression as a single entity; c. evaluate expressions at specific values of their variables, including expressions that arise from formulas used in real-world problems, performing arithmetic operations, including those involving whole-number exponents, in the conventional order when there are no parentheses to specify a particular order; for example, use the formulas V = s^3 and A = 6s^2 to find the volume and surface area of a cube with sides of length s = 1/2), 6.EE.3 (apply the properties of operations to generate equivalent expressions), 6.EE.4 (identify when two expressions are equivalent, i.e., when the two expressions name the same number regardless of which value is substituted into them).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight build orders, six count rounds, six exponent rounds, six equivalence rounds with two trap pairs. Extra: Layout gallery (the class posts different layouts for the same expression on the projector). tool.json `modes: ["Garden", "Layout gallery"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.EE.1 | Build square beds and cube planters; evaluate | 3^2 and 2^3 as plants; order of operations | 3 |
| 6.EE.2 | Build from words; name parts; evaluate formulas | labels on terms and coefficients; the counter | 2 |
| 6.EE.3 | Regroup beds | 3(x + 2) and 3x + 6 as one layout | 2 |
| 6.EE.4 | Test pairs at several values | the trap pair splitting at x = 3 | 4 |

## Screens and modes
Header (kit): title "Expression Garden"; `Garden`, `Layout gallery`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny community garden with an empty plot, a bin of bed tiles, a watering can, and Mr. Delgado leaning on a rake. The welcome is queued (`welcomeAfter: true`): "Plant 3 rows of x plus 2. Drag a row onto the plot." First hint: "Drag an x-row onto the plot."

**Build (focus: the plot).** At 1366x768 the plot fills the left with the expression bar and the counter right; at 680x425 the counter is a tab. Each drop updates the expression; tapping a part of it lights its tiles and names it (term, coefficient, factor). `Regroup` slides the same tiles into a new arrangement, and the bar shows both forms with an equals sign.

**Count rounds.** A slider sets x (whole numbers 0 to 10, then 1/2); the counter fills every bed and totals the plants. A cube planter card asks for soil (V = s^3) and boards (A = 6s^2) at s = 2, then at s = 1/2 (1/8 and 1 1/2).

**Exponent rounds.** Square beds and cube planters show 3^2 = 9 and 2^3 = 8 as plants. Expression cards with exponents are worked step by step in the conventional order.

**Equivalence rounds.** Two gardens side by side. The child tests values with the slider and decides "same garden" or "different". The trap pair x + x and x^2 matches at x = 2; the child must test another value before the decision unlocks, and at x = 3 they split.

**Same garden (the aha).** Mr. Delgado: "Same plants, moved around, is the same garden. One matching count doesn't prove it."

**The end.** Layouts and tests. `Print` prints them.

**Layout gallery (extra).** Layouts posted side by side.

## Content
- Twenty-six rounds with whole-number coefficients and exponents, formulas at whole and fraction values, all readable with `Read`.
- Variables: x and y; s for side length in formulas.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles can be moved and regrouped until `Check`; the slider can be moved any time.
- Keyboard: Tab to tile kinds, the plot (arrows move a tile), Regroup, the expression parts, the slider and decision buttons; Enter places or checks.
- With Motion off tiles regroup at once and the counter shows the total.

## Look
- Accent `--brand` #3a6a1e trellis green (header, the expression bar, buttons); gold #f4c542 (the tile in hand, the lit part); paper #f0f6ea; ink #11220a; muted #525a4c.
- Contrast (WCAG 2.1, computed): white on brand 6.44:1; brand on paper 5.85:1; ink on paper 15.18:1; muted on paper 6.52:1; ink on gold 10.27:1.
- Never color alone: tile kinds have distinct shapes and labels (x, s^2, s^3, 1).
- Different from this batch (awning orange, measuring-cup teal, deep-sea navy, market plum).

## Art
- People (illustrated): Mr. Delgado, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the community garden (1, 16:9), sun and paths (1, 16:9).
- Drawn in code: beds, tiles and plants at exact sizes, the counter.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Delgado; `gentle-storyteller` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.x + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `build`: "Drag a bed onto the plot."
- how `regroup`: "Tap Regroup."
- how `count`: "Slide x, then read the counter."
- how `test`: "Try another value of x."
- how `decide`: "Tap Same garden or Different."
- event, whole, same garden.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
algebra-tiles (`kit/algebra-tiles.js`), as described in algebra-tile-studio's spec. Uses `Poly` for exact expressions in x and y, `.equal` and `.eval(x)` for the counter and tests, and `TileMat` with kinds `['x', '1', 'y']` and no negatives; the square bed and cube planter are this tool's own tiles that report s^2 and s^3. Tool-only code: the plot skin, the plant counter, parts naming, the trap pairs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Regroup | Type 3x + 6 | The layout must be built and regrouped first. |
| Equivalence | Test one value | The decision stays locked until two values are tested, and traps match at the first. |
| Exponents | Multiply base by exponent | 2^3 is counted as 8 plants on screen. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `build`; `regroup`.
2. `count`.
3. `test`; `decide`.
4. Same garden (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.EE.1 to 6.EE.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Testing one value does not show two expressions are equivalent | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | Kieran (2007), "Learning and teaching algebra at the middle school through college levels", Second Handbook of Research on Mathematics Teaching and Learning | yes |
| Area tiles model the distributive property | NCTM Illuminations, "Algebra Tiles" | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s17, 2026-11-10): 3(x + 2) = 3x + 6 for x from -5 to 9, and 18 at x = 4; 2^3 = 8 and 6 x 2^2 = 24; (1/2)^3 = 1/8 and 6 x (1/2)^2 = 1 1/2; 3^2 = 9; 2 + 3^2 x 2 = 20; 24x + 18y = 6(4x + 3y) on a grid of values; x + x = x^2 at 2, and 6 against 9 at 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 plot, bar and counter; at 680x425 counter as a tab.
2. Eight orders are built, parts named, and regrouped into equivalent forms. (6.EE.2, 6.EE.3)
3. Expressions and formulas with exponents are evaluated in order. (6.EE.1, 6.EE.2)
4. Six pairs are tested at more than one value and judged, traps included. (6.EE.4)
5. Tiles come from the shared algebra-tiles engine.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: tiles regroup at once; no network requests.

## Open questions
None.
