# Growth Spurt

## One idea
In a sunny school greenhouse, Mr. Haddad (made up, labeled "illustration") sets a bean and a sunflower side by side, and the child drags the bean taller while a switch picks the kind of comparison: in "times as tall" the sunflower keeps its multiple (bean 8 cm, sunflower 24 cm, written 24 = 3 x 8, and at a 10 cm bean the sunflower jumps to 30 cm), while in "taller by" it keeps its gap (bean 8 cm, sunflower 24 cm, then 10 and 26), and a strip diagram under the plants redraws to show which comparison is running; word problems ask the child to pick multiply or add before solving ("A pumpkin vine is 4 times as long as the pea vine, which is 9 inches"); then the child packs 50 seedlings into trays of 6 and answers three questions that each want a different use of the remainder (trays to hold them all: 9; full trays to sell: 8; seedlings left for the class: 2); a final greenhouse order is a multistep problem written with a letter for the unknown and checked with an estimate; at the end the child sees that "3 times as many" and "3 more" sound alike but grow apart, so a fourth grader learns to read multiplication as a comparison, to solve multiplicative comparison problems and tell them from additive ones, and to solve multistep problems where the remainder must be interpreted.

## Not like
- equal-groups-zoo (3, spec): what multiplication means. Here multiplication as comparing.
- shrink-ray (5, concept): multiplying by fractions as scaling. Here whole-number "times as".
- smoothie-lab (6-7, live): ratios in recipes. Here comparing two amounts by a factor.
- rule-machine (4, concept): number patterns from a rule. Here comparisons that grow.

## Who and how
- Grade 4, Math, module "Multiplicative Comparison". Standards: 4.OA.1 (interpret a multiplication equation as a comparison, e.g., interpret 35 = 5 x 7 as a statement that 35 is 5 times as many as 7 and 7 times as many as 5; represent verbal statements of multiplicative comparisons as multiplication equations), 4.OA.2 (multiply or divide to solve word problems involving multiplicative comparison, e.g., by using drawings and equations with a symbol for the unknown number to represent the problem, distinguishing multiplicative comparison from additive comparison), 4.OA.3 (solve multistep word problems posed with whole numbers and having whole-number answers using the four operations, including problems in which remainders must be interpreted; represent these problems using equations with a letter standing for the unknown quantity; assess the reasonableness of answers using mental computation and estimation strategies including rounding).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three plant pairs, the comparison switch, the strip diagram, eight word problems, three tray jobs, two multistep orders. Extra: Greenhouse orders (longer multistep orders for the class). tool.json `modes: ["Greenhouse", "Orders"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.OA.1 | Grow the bean in "times as" mode and write the equation | 24 = 3 x 8; the strip in three equal parts | 2 |
| 4.OA.2 | Pick multiply or add, then solve; switch modes and watch | the gap fixed or the multiple kept | 3 |
| 4.OA.3 | Pack trays and pick the remainder answer each question wants; solve an order with a letter | 9, 8 or 2; the estimate check | 4 |

## Screens and modes
Header (kit): title "Growth Spurt"; `Greenhouse`, `Orders`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny greenhouse, a bean and a sunflower in pots, a ruler, a mode switch and Mr. Haddad with a watering can. The welcome is queued (`welcomeAfter: true`): "The sunflower is 3 times as tall as the bean. Drag the bean taller and watch." First hint: "Drag the bean's top up."

**Growing (focus: the plants).** At 1366x768 the plants fill the left with the strip diagram below and the equation card right; at 680x425 the card folds under. In "times as tall" the sunflower grows three centimeters for each one; in "taller by 16" it grows one for one. The strip diagram shows three equal bars or two bars and a gap. The child writes each equation.

**Which one?** Eight problems; for each the child taps Multiply or Add before solving, then types the answer with a letter for the unknown (p = 4 x 9).

**Tray jobs.** 50 seedlings, 6 per tray. Three questions with three different answers: all held (9 trays), full trays to sell (8), left for the class (2). The child picks which answer fits each.

**Orders.** "The library wants 3 times as many marigolds as the 14 the office ordered, plus 25 more for the garden club. How many in all?" The child writes m = 3 x 14 + 25 and estimates first (about 40 + 25).

**Side by side (the aha).** Both modes run at once on two bean pairs. Narrator: "Three more and three times look alike at the start. Let them grow, and they're nothing alike."

**The end.** The equation cards and tray answers. `Print` prints them.

**Orders (extra).** Longer greenhouse orders.

## Content
- Made-up greenhouse heights in centimeters and inches (labeled practice numbers), eight problems, three tray questions, two orders, all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The bean drags in whole centimeters; the mode switch can be flipped any time.
- Keyboard: Tab to the bean, the switch, Multiply and Add, the answer box and the tray picker; arrows grow the bean; Enter checks.
- With Motion off plants change height at once.

## Look
- Accent `--brand` #2f6b2a greenhouse green (header, the strip diagram, buttons); gold #f4c542 (the plant in hand, a right equation); paper #eff7ee; ink #0b200a; muted #4f5c4d.
- Contrast (WCAG 2.1, computed): white on brand 6.45:1; brand on paper 5.90:1; ink on paper 15.68:1; muted on paper 6.47:1; ink on gold 10.54:1.
- Never color alone: modes are named on the switch; bars carry numbers.
- Different from this batch (workshop copper, stadium blue, test-kitchen pink, sieve purple).

## Art
- People (illustrated): Mr. Haddad, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the greenhouse (1, 16:9), plant stems and heads in parts (4, 1:1) so they can grow smoothly, the seedling trays (1, 4:3).
- Drawn in code: the ruler, the strip diagram, stems stretched between parts.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Haddad; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.compare + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `grow`: "Drag the bean's top up."
- how `switch`: "Flip the switch and grow it again."
- how `which`: "Tap Multiply or Add."
- how `tray`: "Pick the answer this question wants."
- event, whole, side by side.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the two growth rules, the strip diagram, tray packing, the order checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Which one | Always tap Multiply | Additive problems come back with the gap drawn. |
| Trays | Give the same answer to all three | Each question checks its own use of the remainder. |
| Orders | Type a number | The order needs an equation with a letter and an estimate first. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `grow`; `switch`.
2. `which`.
3. `tray`.
4. Side by side (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.OA.1, 4.OA.2, 4.OA.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Students often confuse multiplicative and additive comparison | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Van de Walle, Karp and Bay-Williams (2019), "Elementary and Middle School Mathematics: Teaching Developmentally", 10th edition | yes |
| Interpreting remainders by context | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Silver, Shapiro and Deutsch (1993), "Sense making and the solution of division problems involving remainders", Journal for Research in Mathematics Education | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s14, 2026-11-10): 3 x 8 = 24 with a gap of 16, so a 10 cm bean gives 26 cm by the gap; 4 x 9 = 36; 50 seedlings in trays of 6 need 9 trays, fill 8 and leave 2; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 plants, strip and card; at 680x425 card under.
2. "Times as" growth is written as multiplication equations. (4.OA.1)
3. Eight problems are sorted as multiply or add and solved. (4.OA.2)
4. Three tray questions use the remainder three ways; orders use a letter and an estimate. (4.OA.3)
5. `Read` reads every card; every control is 48 px or more.
6. Mr. Haddad is labeled illustration; numbers are labeled practice numbers.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: plants change at once; no network requests.

## Open questions
None.
