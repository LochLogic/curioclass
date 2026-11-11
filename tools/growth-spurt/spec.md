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
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the greenhouse and the two ways of growing stay. Added: three "read it both ways" cards so 4.OA.1 has six items and the child reads an equation as a comparison in both directions; three of the eight word problems now need division, and the child builds the strip diagram instead of watching it redraw; the tray jobs no longer hand over three answers to match (the child divides and types each answer, on two tray sets); the orders went from two to four on the main path, with subtraction and division inside them. A wrong Multiply or Add pick now costs the problem. Mr. Haddad works one problem first.
- Three plant pairs, three read-it-both-ways cards, the comparison switch, the strip diagram, eight word problems, two tray sets of three questions, four multistep orders. Extra: Greenhouse orders (longer multistep orders for the class). tool.json `modes: ["Greenhouse", "Orders"]`, `minutes: "30-40"`, `grades_label: "Grade 4"`.
- Change note (hooks, 2026-11-11): Added the three hooks: six items on your own with the end screen by code, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The phrases times as many, more than, equation, remainder and estimate each show on a strip diagram the first time they are used. Word problems use short sentences and no idioms.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.OA.1 | interpret a multiplication equation as a comparison, both ways; represent comparison statements as equations | the student | Grow a plant in "times as" mode and write the equation; on three cards finish "35 is __ times as many as __ and __ times as many as __" | 6 (3 written from plants, 3 read both ways) | the strip in equal parts; the child's own sentence | 2 |
| 4.OA.2 | multiply or divide to solve comparison word problems, with drawings and equations with a symbol; tell multiplicative from additive comparison | the student | Pick `Times as many` or `More than`, build the strip diagram from bars, write an equation with a letter, solve | 8 (2 multiply, 3 divide, 3 additive) | the child's own strip: equal bars, or two bars and a gap | 3 |
| 4.OA.3 | solve multistep problems with the four operations, including interpreting remainders; equations with a letter; check by estimating | the student | Tray sets: divide, then type the answer each question wants. Orders: estimate, write an equation with a letter, solve | 6 tray questions and 4 orders | the trays filling after the answer; the estimate beside the answer | 4, 5 |

## Screens and modes
Header (kit): title "Growth Spurt"; `Greenhouse`, `Orders`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny greenhouse, a bean and a sunflower in pots, a ruler, a mode switch and Mr. Haddad with a watering can. The welcome is queued (`welcomeAfter: true`): "The sunflower is 3 times as tall as the bean. Drag the bean taller and watch." First hint: "Drag the bean's top up."

**Growing (focus: the plants).** At 1366x768 the plants fill the left with the strip diagram below and the equation card right; at 680x425 the card folds under. In "times as tall" the sunflower grows three centimeters for each one; in "taller by 16" it grows one for one. The strip diagram shows three equal bars or two bars and a gap. The child writes each equation.

**Read it both ways.** After the three plant pairs, three cards show an equation alone (35 = 5 x 7). The child finishes the sentence with four typed numbers: "35 is __ times as many as __ , and __ times as many as __ ." Mr. Haddad reads his own first, as the model: "24 = 3 x 8. So 24 is 3 times as many as 8, and 8 times as many as 3."

**Which one?** Eight problems. Mr. Haddad works a ninth one first, aloud, from picking the kind to checking the answer; it cannot be skipped and `Mr. Haddad's example` reopens it. For each problem the child (1) taps `Times as many` or `More than`, (2) builds the strip: drags equal bars for a times-as-many problem, or one bar and a gap piece for a more-than problem, and labels the part that is unknown with the letter, (3) writes an equation with the letter (p = 4 x 9, or 7 x s = 56, or s = 56 / 7), (4) types the answer. The strip does not draw itself. A wrong kind is not told at once: the child finds out when the strip cannot be labeled to fit the story, the problem is set aside, and it comes back at the end with new numbers.

**Tray jobs.** "50 seedlings, 6 to a tray." The child first types the division, 50 / 6 = __ with __ left. Then three questions, each with a number box and no choices: How many trays to hold them all? (9) How many full trays can be sold? (8) How many seedlings go to the class? (2) After each answer the trays fill on screen to show it. A second set follows with bulbs.

**Orders.** Four orders, on the main path. "The library wants 3 times as many marigolds as the 14 the office ordered, plus 25 more for the garden club. How many in all?" The child estimates first in a box (about 40 + 25), writes m = 3 x 14 + 25, and solves. An answer far from the child's own estimate is flagged: "Your estimate was 65. Does 137 make sense?"

**Side by side (the aha).** Both modes run at once on two bean pairs. Narrator: "Three more and three times look alike at the start. Let them grow, and they're nothing alike."

**The end.** The equation cards and tray answers. `Print` prints them.

**Orders (extra).** Longer greenhouse orders.
**On your own.** Six items with Mr. Haddad quiet: no plants, no strip bars offered, no mode buttons, no hints, one answer each. Nothing is marked until all are in.

**Results strip (on the end screen).** For the teacher: for each of 4.OA.1, 4.OA.2 and 4.OA.3, how many of its items on your own were right, in numbers and words, with each item missed and the answer the child gave. It prints with the rest.

## Content
- Made-up greenhouse heights in centimeters (labeled practice numbers), all readable with `Read`.
- Plant pairs, times-as: a sunflower 3 times as tall as an 8 cm bean (24 = 3 x 8); a tomato 4 times as tall as a 7 cm pepper (28 = 4 x 7); a vine 6 times as tall as a 5 cm sprout (30 = 6 x 5). Read both ways: 35 = 5 x 7; 42 = 6 x 7; 18 = 2 x 9.
- Mr. Haddad's worked problem: "A pea is 6 cm. A corn plant is 5 times as tall. How tall is the corn?" c = 5 x 6 = 30.
- Which one? (1) A bean is 9 cm. A sunflower is 4 times as tall. How tall? 36, multiply. (2) A fern is 12 cm. A palm is 15 cm taller. How tall? 27, additive. (3) A cornstalk is 56 cm, 7 times as tall as a sprout. How tall is the sprout? 8, divide. (4) A rose is 45 cm and a daisy is 18 cm. How much taller is the rose? 27, additive. (5) A vine is 48 cm and a seedling is 6 cm. How many times as tall is the vine? 8, divide. (6) A pepper has 7 flowers. A tomato has 5 times as many. How many? 35, multiply. (7) A cactus is 30 cm, which is 6 cm taller than an aloe. How tall is the aloe? 24, additive. (8) A pumpkin vine has 72 leaves, 8 times as many as a squash vine. How many on the squash? 9, divide.
- Tray sets: 50 seedlings, 6 to a tray: 8 full, 2 left; trays needed 9, full trays 8, left over 2. 75 bulbs, 8 to a box: 9 full, 3 left; boxes needed 10, full boxes 9, left over 3.
- Orders: (a) m = 3 x 14 + 25 = 67, estimate about 65. (b) "The greenhouse has 120 pots. Each of 4 shelves holds 18. How many pots are left on the floor?" p = 120 - 4 x 18 = 48, estimate about 40. (c) "96 seed packets are shared equally by 6 classes. Each class gives 5 of its packets away. How many does a class keep?" k = 96 / 6 - 5 = 11, estimate about 10. (d) "85 tulips came in and 3 wilted. The rest go in bunches of 9. How many full bunches?" b = (85 - 3) / 9, which is 9 with 1 left, so 9 bunches; estimate about 9.
- On your own, with what each common wrong answer means:
  - 4.OA.1: "Write an equation for: 42 is 6 times as many as 7." (42 = 6 x 7.) "24 = 3 x 8. Finish: 24 is __ times as many as __." (3 and 8, or 8 and 3.) Writing 42 = 6 + 7 or 6 x 42 means the sentence is not yet read as a comparison.
  - 4.OA.2: "A sunflower is 4 times as tall as a 9 cm bean. How tall is it?" (36 cm.) "A vine is 45 cm. It is 5 times as tall as a sprout. How tall is the sprout?" (9 cm.) An answer of 13 or 50 means "times as" was read as "more than"; 225 means the child multiplied where the smaller amount was wanted.
  - 4.OA.3: "58 seedlings go 8 to a tray. How many trays are needed to hold them all?" (8.) "Mr. Haddad has 3 boxes of 24 pots and uses 50. How many are left?" (22.) An answer of 7 means the remainder was dropped; "7 r 2" means it was not read against the question; 72 means the second step was left out.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The bean drags in whole centimeters; the mode switch can be flipped any time.
- Keyboard: Tab to the bean, the switch, Multiply and Add, the answer box and the tray picker; arrows grow the bean; Enter checks.
- With Motion off plants change height at once.
- Access: every action works by tap and by keyboard. Bars and number cards can be dragged, or picked with a tap and placed with a tap. The two plants and the two modes carry names in words, never color alone. Motion can be paused.
- On your own: one answer each, no feedback until the sixth is in.

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
- how `both`: "Type the four numbers to finish the sentence."
- how `which`: "Tap Times as many or More than."
- how `strip`: "Drag bars to build the strip. Put the letter on the part you don't know."
- how `tray`: "Type the answer this question wants."
- how `order`: "Type your estimate first."
- event, whole, Mr. Haddad's two examples.
- event, whole, side by side.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `own`: "Six more on your own. No hints this time."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None (family "none"). Tool-only code: the two growth rules, the strip diagram, tray packing, the order checker.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Both ways | Copy the equation's numbers in order | Four boxes: the two directions use the factors in swapped places, and a sentence with the product in the wrong box fails. |
| Which one | Always tap `Times as many` | Three of eight are additive; a wrong kind is found only at the strip, and the problem comes back with new numbers, so guessing costs a whole extra problem. |
| Strip | Wait for it to draw | The child drags every bar; nothing is drawn for them. |
| Solve | Always multiply the two numbers | Three times-as-many problems need division; 56 x 7 and 48 x 6 fail. |
| Trays | Give the same answer to all three; type the quotient each time | The three answers differ (9, 8, 2 and 10, 9, 3); each box is checked for its own question, with no choices to pick from. |
| Orders | Type a number | The order needs an estimate, then an equation with a letter that fits the story, then the answer. |
| On your own | Retry until right; lean on the hints | One answer each, no hints or models, and nothing is marked until all are in. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `grow`; `switch`.
2. `both`. Mr. Haddad's example (whole). `which`; `strip`.
3. `tray`; `order`.
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
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): 4 x 7 = 28, 6 x 5 = 30, 5 x 7 = 35, 6 x 7 = 42, 2 x 9 = 18; the eight answers 36, 27, 8, 27, 8, 35, 24, 9; 75 = 8 x 9 + 3, so 10 boxes, 9 full, 3 left; 3 x 14 + 25 = 67; 120 - 4 x 18 = 48; 96 / 6 - 5 = 11; 82 = 9 x 9 + 1; always-multiply slips 392 and 288 and 576 differ from the answers.
Checks run for the items on your own (Python, 2026-11-11): 6 x 7 = 42; 4 x 9 = 36; 45 / 5 = 9; 58 = 8 x 7 + 2, so 8 trays; 3 x 24 - 50 = 22.

## Done when
1. Focus and fold: at 1366x768 plants, strip and card; at 680x425 card under.
2. Three "times as" growths are written as equations and three equations are read as comparisons both ways. (4.OA.1)
3. Eight problems are sorted as times-as-many or more-than, drawn as strips by the child, and solved with a letter; three need division. (4.OA.2)
4. Two tray sets: the child divides and types three different answers for each, with no choices given. (4.OA.3)
5. Four orders are solved with an estimate first and an equation with a letter; two use subtraction or division. (4.OA.3)
6. Mr. Haddad's worked problem plays first and can be reopened.
7. `Read` reads every card; every control is 48 px or more.
8. Mr. Haddad is labeled illustration; numbers are labeled practice numbers.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: plants change at once; no network requests.
11. Six items on your own run with no model or hint, one answer each; the end screen shows the result by code and the items missed. (4.OA.1, 4.OA.2, 4.OA.3)
12. Every spoken instruction is also on screen, and each key word shows with a picture or example at first use.
13. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
None.
