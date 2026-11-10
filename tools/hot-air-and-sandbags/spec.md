# Hot Air and Sandbags

## One idea
The child flies a hot-air balloon with its pilot, Captain Bea (made up, labeled "illustration"), where every hot-air puff in the basket counts +1 and every sandbag counts -1, and a vertical number line beside the balloon shows the height; the first order, "add 5 puffs and 5 sandbags", leaves the balloon at 0, because opposites make zero; add and subtract rounds show p + q as a trip of |q| from p, up or down, and removing a sandbag lifts the balloon, so p - q is the same as p + (-q), and the distance between two heights is the absolute value of their difference (from -7 to 3 is 10); multiply rounds add 3 groups of 2 sandbags (3 x -2 = -6) and then remove 3 groups of 2 sandbags (-3 x -2 = +6), and the child predicts the sign rules before testing them and checks (-1)(-1) = 1 with the distributive property; divide rounds read a drop of 12 m in 4 minutes as -12 / 4 = -3 m per minute and show -(12/4), -12/4 and 12/-4 as the same flight; missions mix fractions and decimals (from a valley floor at -45.5 m to a ridge at 120.25 m is a climb of 165.75 m); at the end the child sees the sign rules as what adding and removing puffs and sandbags has to do, so a seventh grader learns to add, subtract, multiply and divide rational numbers and to solve real-world problems with all four operations.

## Not like
- deep-sea-dive (6, spec): signed numbers as positions. Here operations on them.
- balance-puzzle (6, spec): solving equations. Here computing with signs.
- square-root-hunt (8, concept): irrational numbers. Here rationals.
- remainder-loop (7, concept): why decimals end or repeat. Here the four operations.

## Who and how
- Grade 7, Math, module "Operations with Rational Numbers". Standards: 7.NS.1 (apply and extend previous understandings of addition and subtraction to add and subtract rational numbers; represent addition and subtraction on a horizontal or vertical number line diagram: a. describe situations in which opposite quantities combine to make 0; b. understand p + q as the number located a distance |q| from p, in the positive or negative direction depending on whether q is positive or negative; c. understand subtraction of rational numbers as adding the additive inverse, p - q = p + (-q); show that the distance between two rational numbers on the number line is the absolute value of their difference; d. apply properties of operations as strategies to add and subtract rational numbers), 7.NS.2a to 7.NS.2c (multiplication extended to rational numbers using the distributive property, leading to rules like (-1)(-1) = 1; integers can be divided provided the divisor is not zero, and -(p/q) = (-p)/q = p/(-q); apply properties of operations to multiply and divide rational numbers), 7.NS.3 (solve real-world and mathematical problems involving the four operations with rational numbers). 7.NS.2d moves to remainder-loop.
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight add and subtract flights, six multiply flights, four divide flights, six missions, the sign-rule notebook. Extra: Flight plans (students trade flight-plan puzzles). tool.json `modes: ["Flight", "Flight plans"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.NS.1 | Add and remove puffs and sandbags | the balloon on a vertical line; zero pairs | 2 |
| 7.NS.2a to 7.NS.2c | Add or remove groups; split a drop over time | -3 x -2 = 6; -12 / 4 = -3 | 3 |
| 7.NS.3 | Fly missions with fractions and decimals | heights and climbs worked out | 4 |

## Screens and modes
Header (kit): title "Hot Air and Sandbags"; `Flight`, `Flight plans`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A balloon at 0 over a green valley, a basket with a puff jar and a sandbag pile, a vertical number line on the left, and Captain Bea in goggles. The welcome is queued (`welcomeAfter: true`): "Add 5 puffs and 5 sandbags. Where are we? Drag a puff into the basket." First hint: "Drag a puff into the basket."

**Add and subtract (focus: the basket).** At 1366x768 the sky fills the middle with the number line left and the notebook right; at 680x425 the notebook is a tab. Puffs and sandbags pair off as zero pairs. `Remove` takes items out; removing a sandbag rises one. Each move writes its number sentence (-4 - (-3) = -1) and an arrow on the line. Distance rounds ask how far between two heights.

**Multiply.** Group buttons add or remove groups (3 groups of 2 sandbags). Before each, the child predicts the sign; the notebook collects the rule. A card shows -1 x (1 + -1) = 0 expanded to explain (-1)(-1) = 1.

**Divide.** A flight log: down 12 m in 4 minutes. The child types the rate; three equal flights show -(12/4), -12/4 and 12/-4 landing at the same spot.

**Missions.** Six problems with fractions and decimals: a climb from -45.5 m to 120.25 m, a drop of 3 1/2 m a minute for 6 minutes, a fuel puzzle.

**Not tricks (the aha).** Captain Bea: "The sign rules aren't tricks. They're what adding and removing puffs and sandbags has to do."

**The end.** The notebook of rules and flights. `Print` prints it.

**Flight plans (extra).** Partners trade puzzles.

## Content
- Heights from -50 to 130 m; integers in early flights, then fractions and decimals; all readable with `Read`.
- Weather is calm; the balloon never crashes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Moves can be undone until `Check`.
- Keyboard: Tab to the puff jar, sandbag pile, Remove, group buttons, the line and answer boxes; Enter moves or checks; plus and minus keys add a puff or a sandbag.
- With Motion off the balloon jumps to its new height.

## Look
- Accent `--brand` #1a5a8f balloon sky blue (header, the line, buttons); gold #f4c542 (the item in hand, the height marker); paper #edf4fa; ink #061c30; muted #4b5664.
- Contrast (WCAG 2.1, computed): white on brand 7.23:1; brand on paper 6.52:1; ink on paper 15.55:1; muted on paper 6.72:1; ink on gold 10.61:1.
- Never color alone: puffs and sandbags have shapes and carry +1 and -1.
- Different from this batch (signal orange, midway red, diner teal, licorice purple).

## Art
- People (illustrated): Captain Bea, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the valley and sky (1, 16:9), the balloon (1, 1:1), a ridge (1, 16:9).
- Drawn in code: puffs, sandbags, the number line, arrows.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Captain Bea; `gentle-storyteller` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.flight + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `add`: "Drag a puff or a sandbag into the basket."
- how `remove`: "Tap Remove, then tap an item."
- how `predict`: "Tap plus or minus for the answer's sign."
- how `rate`: "Type the meters per minute."
- how `mission`: "Type the answer."
- event, whole, not tricks.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: zero pairs, the vertical number line with arrows, group moves, exact rationals with `Frac` as described in equation-golf's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Subtract | Always go down | Removing a sandbag goes up, and the check uses the height. |
| Signs | Guess positive | Predictions are scored, and both signs appear equally. |
| Missions | Ignore the negative | -45.5 to 120.25 is checked as 165.75. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `add`; `remove`.
2. `predict`.
3. `rate`; `mission`.
4. Not tricks (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.NS.1 to 7.NS.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The hot-air balloon model for signed-number operations | Janvier (1985), "Comparison of models aimed at teaching signed integers", Proceedings of PME 9 | Vig, Murray and Star (2014), "Model breaking points conceptualized", Educational Psychology Review | yes |
| (-1)(-1) = 1 follows from the distributive property | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | Wu (2011), "Understanding Numbers in Elementary School Mathematics", AMS | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s19, 2026-11-10): 5 + (-5) = 0; 3 x -2 = -6 and -3 x -2 = 6; -12 / 4 = -3 and -(12/4) = -12/4 = 12/-4; 120.25 - (-45.5) = 165.75; |-7 - 3| = 10; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 sky, line and notebook; at 680x425 notebook as a tab.
2. Eight flights add and subtract with zero pairs and distances. (7.NS.1)
3. Multiply and divide flights produce the sign rules, with the distributive check. (7.NS.2a to 7.NS.2c)
4. Six missions use all four operations with fractions and decimals. (7.NS.3)
5. Captain Bea is labeled illustration; the balloon never crashes.
6. `Read` reads every card and the height; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the balloon jumps; no network requests.

## Open questions
- The idea card moves 7.NS.2d out of this tool (default used: remainder-loop teaches why a fraction's decimal ends or repeats; this tool keeps 7.NS.1, 7.NS.2a to 7.NS.2c and 7.NS.3).
