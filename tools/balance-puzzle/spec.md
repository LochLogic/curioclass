# Balance Puzzle

## One idea
At a farmers market stall the farmer, Ruth (made up, labeled "illustration"), weighs sealed sacks on a two-pan scale and asks the child to prove what is inside before the sack is opened: a sack x and a 3 kg weight on the left level with 10 kg on the right, so the child removes 3 kg from both pans and x = 7; three identical sacks level with 12 kg, so the child splits both pans into 3 equal groups and one sack is 4 kg; weights include 1/2 kg and 0.25 kg pieces (x + 1/2 = 2 1/4 gives 1 3/4; 4 sacks level with 3 kg gives 0.75 kg each), and opening the sack checks the answer by substitution; write-it levels turn a stall story ("some apples and a 2.5 kg pumpkin weigh 6 kg") into an equation built on the scale and solved (3.5 kg); tipping levels tip the pan instead (the sack plus 2 kg is heavier than 5 kg), the child tests values, finds the sack must be more than 3 kg, writes x > 3, and shades every possible weight on a number line, and sees why there are infinitely many; at the end the child sees solving as finding the values that make the statement true, so a sixth grader learns to solve one-step equations by reasoning, use variables for unknowns, and write and graph simple inequalities.

## Not like
- balance-the-beam (1, spec): the meaning of equals, same engine. Here solving for an unknown.
- equation-golf (9, spec): multi-step equations. Here one step.
- phone-plan-showdown (7, concept): two-step inequalities in context. Here one-step.
- snack-scale (K, spec): comparing amounts with counts. Here weights with fractions and decimals.

## Who and how
- Grade 6, Math, module "One-Step Equations and Inequalities". Standards: 6.EE.5 (understand solving an equation or inequality as a process of answering a question: which values from a specified set, if any, make the equation or inequality true? use substitution to determine whether a given number in a specified set makes an equation or inequality true), 6.EE.6 (use variables to represent numbers and write expressions when solving a real-world or mathematical problem; understand that a variable can represent an unknown number, or, depending on the purpose at hand, any number in a specified set), 6.EE.7 (solve real-world and mathematical problems by writing and solving equations of the form x + p = q and px = q for cases in which p, q and x are all nonnegative rational numbers), 6.EE.8 (write an inequality of the form x > c or x < c to represent a constraint or condition in a real-world or mathematical problem; recognize that inequalities of the form x > c or x < c have infinitely many solutions; represent solutions of such inequalities on number line diagrams).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve equation levels, six write-it levels, six tipping levels, the sack opener, the number line. Extra: Puzzle swap (a student builds a scale puzzle; a partner solves it in the fewest moves). tool.json `modes: ["Market", "Puzzle swap"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.EE.5 | Open the sack; test values on a tipped scale | substitution; the pan moving | 2, 4 |
| 6.EE.7 | Remove equal weights; split into equal groups | x + 3 = 10 becoming x = 7 | 2 |
| 6.EE.6 | Build a stall story on the scale | the equation from the story | 3 |
| 6.EE.8 | Write x > c; shade the line | infinitely many weights | 4 |

## Screens and modes
Header (kit): title "Balance Puzzle"; `Market`, `Puzzle swap`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A market stall with crates of produce, a two-pan scale, a sealed sack x and a 3 kg weight on the left, 10 kg on the right, and Ruth in a sun hat. The welcome is queued (`welcomeAfter: true`): "What's in the sack? Prove it before you open it. Drag a weight off one pan." First hint: "Drag a weight off one pan."

**Equation levels (focus: the scale).** At 1366x768 the scale fills the middle with the equation under it and the weight shelf right; at 680x425 the shelf is a sheet. Taking weight from one pan alone tips the scale; the child must take the same from both. `Split` divides both pans into equal groups and keeps one. When x stands alone, `Open` checks by substitution and shows the sack's contents.

**Write-it levels.** A story card; the child drags items onto the pans to build it (apples as x, the pumpkin as 2.5 kg, the total as 6 kg), then solves.

**Tipping levels.** The scale tips. The child tries values for x with a dial; each try shows the scale level, tipped left or tipped right. A table logs the tries. The child types x > 3 and drags shading onto the number line from 3 to the right, with an open circle at 3. A card asks how many weights work; the answer "infinitely many" is chosen with a reason (between any two there is another).

**True values (the aha).** Ruth: "Solving is finding what makes it true. Sometimes that's one weight, and sometimes it's a whole stretch of them."

**The end.** The puzzle log. `Print` prints it.

**Puzzle swap (extra).** A partner solves a built puzzle in the fewest moves.

## Content
- Twenty-four levels with whole numbers, fractions (halves, quarters) and decimals (tenths, quarters), all nonnegative, readable with `Read`.
- Weights are in kilograms; sacks hold produce.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Moves can be undone until `Open` or `Check`.
- Keyboard: Tab to weights, pans, Split, Open, the value dial, the number line (arrows move by 1, shift by 0.5) and answer boxes; Enter moves or checks.
- With Motion off the scale snaps to level or tipped.

## Look
- Accent `--brand` #7a2e6b market plum (header, the beam, buttons); gold #f4c542 (the weight in hand, the shaded line); paper #f8eff6; ink #250b20; muted #5c4f59.
- Contrast (WCAG 2.1, computed): white on brand 8.64:1; brand on paper 7.68:1; ink on paper 16.27:1; muted on paper 6.87:1; ink on gold 11.25:1.
- Never color alone: the scale says "level", "left side heavier" or "right side heavier".
- Different from this batch (awning orange, measuring-cup teal, trellis green, deep-sea navy).

## Art
- People (illustrated): Ruth, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the market stall (1, 16:9), produce for stories (6, 1:1).
- Drawn in code: the scale and tilt, weights, sacks, the number line.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Ruth; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `remove`: "Drag the same weight off both pans."
- how `split`: "Tap Split and pick the groups."
- how `open`: "Tap Open to check the sack."
- how `try`: "Turn the dial to try a weight."
- how `shade`: "Drag shading onto the number line."
- event, whole, true values.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
balance (`kit/balance.js`), as described in equation-golf's spec. Uses `Frac`, the equation model with `rel` '=' and '>' or '<', `Balance.moves.sub` and `div` (one step only), `Balance.solutions` for the ray `{at, dir, closed: false}`, and `Beam` with `skin: 'bags'` and `tryX(x)` for tipping. Tool-only code: the stall, stories, the value log, the shading number line.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Equations | Open the sack early | Open is off until x stands alone. |
| Remove | Take weight from one pan | The scale tips and the move is undone. |
| Inequality | Shade one point | The check needs the open circle and the whole ray. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `remove`; `split`; `open`.
2. Write-it levels repeat `remove` and `open`.
3. `try`; `shade`.
4. True values (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.EE.5 to 6.EE.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Balance models support solving equations by doing the same to both sides | Vlassis (2002), "The balance model: hindrance or support for the solving of linear equations with one unknown", Educational Studies in Mathematics | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | yes |
| Inequalities have infinitely many solutions shown as a ray | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 algebra | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s17, 2026-11-10): x + 3 = 10 gives 7; 3x = 12 gives 4; x + 2.5 = 6 gives 3.5; x + 1/2 = 2 1/4 gives 1 3/4; 4x = 3 gives 0.75; x + 2 > 5 gives x > 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scale, equation and shelf; at 680x425 shelf as a sheet.
2. Twelve one-step equations are solved by equal moves and checked by opening the sack. (6.EE.5, 6.EE.7)
3. Six stall stories are built as equations and solved. (6.EE.6)
4. Six tipped scales are tested, written as x > c or x < c, and shaded. (6.EE.5, 6.EE.8)
5. Every value stays nonnegative.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the scale snaps; no network requests.

## Open questions
None.
