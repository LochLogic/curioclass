# Pattern Painter

## One idea
In the town square a giant 10 by 10 multiplication-table mural waits for color, and Detective Rue (made up, labeled "illustration") opens two kinds of cases: in pattern cases the child colors squares by a rule (every even product, every multiple of 5, the square numbers, the 4s column next to the 2s column) so the pattern pops, predicts the next square before painting it, and then completes the reason from sentence pieces ("4 times a number is always even, because 4 = 2 x 2"); in receipt cases a witness makes a two-step claim ("I bought 3 packs of 8 markers and gave away 9, so I have 33 left"), and the child estimates first (24 minus about 10 is about 14), flags the claim as not reasonable, then solves with a letter for the unknown (3 x 8 - 9 = m, so m = 15); the addition table gets one case too (each diagonal adds the same); at the end the mural is a bright patchwork with each rule's reason on a plaque, so a third grader learns to solve two-step word problems with all four operations, writing them as equations with a letter for the unknown and checking answers by estimation, and to find patterns in the multiplication and addition tables and explain them with properties of operations.

## Not like
- lost-and-found (2, spec): add and subtract only. Here all four operations and estimation.
- rule-machine (4, concept): patterns from a given rule. Here finding and explaining the rule.
- multiplication-dungeon (3, concept): fact fluency. Here patterns in the table.
- equal-groups-zoo (3, spec): what multiplying means. Here why table patterns hold.

## Who and how
- Grade 3, Math, module "Patterns and Two-Step Problems". Standards: 3.OA.8 (solve two-step word problems using the four operations; represent these problems using equations with a letter standing for the unknown quantity; assess the reasonableness of answers using mental computation and estimation strategies including rounding), 3.OA.9 (identify arithmetic patterns (including patterns in the addition table or multiplication table), and explain them using properties of operations).
- Format: mystery. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The 10 by 10 multiplication mural, an addition-table mural, six pattern cases, six receipt cases (two with right claims), sentence pieces for reasons, the plaques. Extra: Case maker (the teacher writes receipt claims). tool.json `modes: ["Square", "Case maker"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.OA.9 (find) | Color by a rule; predict the next square | the pattern popping | 2 |
| 3.OA.9 (explain) | Complete the reason from pieces | the plaque | 3 |
| 3.OA.8 | Estimate, flag, then solve with a letter | the estimate beside the claim; the equation | 4 |

## Screens and modes
Header (kit): title "Pattern Painter"; `Square`, `Case maker`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A brick wall in a town square with a pale 10 by 10 multiplication table painted on it, paint cans below, and Detective Rue with a notebook. The welcome is queued (`welcomeAfter: true`): "Case one: color every even product on the mural. Tap a paint can, then tap a square." First hint: "Tap a paint can."

**Pattern cases (focus: the mural).** At 1366x768 the mural fills the left with the case card at the right; at 680x425 the mural scrolls and the card is a sheet. The child paints squares; a wrong square drips and fades with a note ("7 x 3 = 21, odd"). After a few, `Predict` asks which square comes next before it's painted.

**Reasons.** Sentence pieces: "because 4 = 2 x 2," "an even number times any number," "5 x an even number ends in 0." The child drags pieces to finish the reason; it goes on a plaque under the pattern.

**Receipt cases.** A witness card: "3 packs of 8 markers, gave away 9, so 33 left." Step one: estimate (a slider with friendly numbers). Step two: Reasonable or Not reasonable. Step three: write the equation with a letter (3 x 8 - 9 = m) and solve. Two of six claims are right, so flagging everything fails.

**The addition table.** A 0 to 9 addition mural: each down-right diagonal adds the same number. The child colors one and gives the reason.

**Not luck (the aha).** The finished mural with plaques. Detective Rue: "Every pattern has a reason. And an estimate catches a wrong answer before you even calculate."

**The end.** The mural and the case file. `Print` prints a coloring mural.

**Case maker (extra).** The teacher writes claims; nothing leaves the device.

## Content
- The 1 to 10 multiplication table and the 0 to 9 addition table, six rules, six receipt claims with all four operations, all readable with `Read`. Witnesses make honest mistakes; no one is accused.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Paint can be wiped from any square.
- Keyboard: Tab to cans, the mural (arrows move between squares), pieces and buttons; Enter paints and places.
- With Motion off paint appears without dripping.

## Look
- Accent `--brand` #8e2a6b mural magenta (header, paint can labels, buttons); gold #f4c542 (the predicted square, the estimate); paper #fbf0f6; ink #2a0a1f; muted #5e4c57.
- Contrast (WCAG 2.1, computed): white on brand 7.80:1; brand on paper 7.02:1; ink on paper 16.27:1; muted on paper 7.14:1; ink on gold 11.12:1.
- Never color alone: painted squares also get a pattern fill (dots, stripes) per rule.
- Different from this batch (penguin navy, backyard green, picnic red, newsletter teal).

## Art
- People (illustrated): Detective Rue and three witnesses, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Local FLUX (`scripts/localart.py`): the town square with the blank wall (1, 16:9).
- Drawn in code: the murals, paint, plaques, the estimate slider.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as Detective Rue; `news-reader` as the witnesses and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `paint`: "Tap a paint can, then a square."
- how `predict`: "Tap the square that comes next."
- how `reason`: "Drag pieces to finish the reason."
- how `estimate`: "Slide to your estimate, then tap Reasonable or Not reasonable."
- how `solve`: "Type the equation with a letter, then the answer."
- event, whole, not luck.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the murals, rule checks, the reason builder, receipt cases. Rules and cases sit in a marked block `/* PATTERN-PAINTER DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Paint | Paint every square | Wrong squares drip and fade; the case needs only the rule's squares. |
| Receipt | Flag every claim | Two claims are right; flagging them asks for the estimate again. |
| Reason | Drag any pieces | Only true reasons lock onto the plaque. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `paint`; `predict`.
2. `reason`.
3. `estimate`; `solve`.
4. Not luck (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.OA.8, 3.OA.9 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Table patterns can be explained with properties of operations | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Carpenter, Franke and Levi (2003), "Thinking Mathematically: Integrating Arithmetic and Algebra in Elementary School" | yes |
| Estimating first helps students judge whether answers are reasonable | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Sowder (1992), "Estimation and number sense", in Handbook of Research on Mathematics Teaching and Learning | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-10): 3 x 8 - 9 = 15, not 33, and the estimate 14 is within 1; 75 of the 100 products are even and 36 are multiples of 5; the 4s column is double the 2s; ten square numbers; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 mural and card; at 680x425 scrolling mural.
2. Six pattern cases are colored and predicted. (3.OA.9)
3. Each pattern gets a reason on a plaque. (3.OA.9)
4. Six receipt cases are estimated, judged and solved with a letter. (3.OA.8)
5. `Read` reads every card; every control is 48 px or more.
6. People are labeled illustration; witnesses are never accused.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no drips; no network requests.

## Open questions
None.
