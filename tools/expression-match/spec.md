# Expression Match

## One idea
At a game table the child plays a card game against a rival, Jonah (made up, labeled "illustration"), where five expression cards lie face up (4x - 6, 1.05a, 2(l + w), 0.5y, -3x + 12) and the child holds a hand (2(2x - 3), a + 0.05a, 1/2(8x - 12), 0.75y - 0.25y, -3(x - 4)), and a match only counts if the child makes it: move cards (distribute, factor out, combine like terms) rewrite a hand card step by step, each move animating on algebra tiles with negative tiles, until it equals a table card; a move that breaks the rules is shown wrong with a counterexample value (2(x + 3) is not 2x + 3, since at x = 1 they are 8 and 5); rational levels bring 1/2(8x - 12), -3(x - 4) and 0.75y - 0.25y, with factoring out negatives and fractions; story cards carry a context, so a + 0.05a and 1.05a both mean the price plus 5% tax, and 2l + 2w and 2(l + w) both fence a pen, and the child picks which form answers a given question faster; Jonah plays too and sometimes cheats, and the child challenges a bad match by plugging in a value; at the end the child sees equivalent forms as the same quantity, each telling a different part of the story, so a seventh grader learns to add, subtract, factor and expand linear expressions with rational coefficients and to rewrite expressions in context to show how quantities relate.

## Not like
- expression-garden (6, spec): whole numbers and exponents, same tile engine. Here rational coefficients and negatives.
- algebra-tile-studio (9, spec): factoring quadratics. Here linear expressions.
- equation-golf (9, spec): solving equations. Here rewriting expressions.
- expression-escape (5, spec): order of operations with numbers. Here letters and properties.

## Who and how
- Grade 7, Math, module "Equivalent Expressions". Standards: 7.EE.1 (apply properties of operations as strategies to add, subtract, factor, and expand linear expressions with rational coefficients), 7.EE.2 (understand that rewriting an expression in different forms in a problem context can shed light on the problem and how the quantities in it are related; for example, a + 0.05a = 1.05a means that "increase by 5%" is the same as "multiply by 1.05").
- Format: cards. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four rounds of five table cards, move cards, eight story cards, Jonah's six challenge moments. Extra: Two players (two students take turns on one device). tool.json `modes: ["Against Jonah", "Two players"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.EE.1 | Play move cards to rewrite a hand card | tiles distributing, combining, factoring | 2 |
| 7.EE.1 | Challenge a bad match with a value | the counterexample | 3 |
| 7.EE.2 | Pick the form that answers a story question | a + 0.05a against 1.05a | 4 |

## Screens and modes
Header (kit): title "Expression Match"; `Against Jonah`, `Two players`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A green felt game table, five face-up cards, the child's hand, a deck of move cards, and Jonah grinning across the table. The welcome is queued (`welcomeAfter: true`): "Match a card on the table, but you have to make the match yourself. Tap a card in your hand." First hint: "Tap a card in your hand."

**A turn (focus: the hand card).** At 1366x768 the table runs across the top, the tile mat in the middle and the hand below; at 680x425 the mat is a sheet. The child taps a hand card, then a move card; the tiles act it out (2(2x - 3) splits into two groups of 2x and -3, then joins as 4x - 6) and the card rewrites. When it equals a table card the child taps `Claim` and wins the pair. A move that breaks a rule is shown wrong with a value test.

**Rational levels.** Hand cards with fractions, decimals and negatives. Tiles show halves and negatives; factoring out -3 flips signs inside.

**Story cards.** A table card carries a context ("A $40 jacket plus 5% tax"). The child matches a + 0.05a with 1.05a, then answers "How much tax?" and "What's the total?" by picking the form that shows each one.

**Jonah's turn.** Jonah claims pairs. Sometimes the claim is wrong; the child can tap `Challenge`, type a value, and both cards are evaluated. A right challenge wins Jonah's pair.

**Same quantity (the aha).** Jonah: "Fine, they're the same. But a + 0.05a shows the tax, and 1.05a shows the total."

**The end.** The pairs won and the move log. `Print` prints them.

**Two players (extra).** Two students take turns.

## Content
- Twenty table cards and twenty hand cards in four rounds, linear with rational coefficients, eight story contexts (tax, discounts, fences, tips, savings), all readable with `Read`.
- Jonah's cheats are always beatable by a value test.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Moves can be undone until `Claim`.
- Keyboard: Tab to hand cards, move cards, tiles, table cards, Claim and Challenge; Enter plays or claims.
- With Motion off tiles regroup at once.

## Look
- Accent `--brand` #1e6646 card-table green (header, card backs, buttons); gold #f4c542 (the card in hand, a claimed pair); paper #ecf5f0; ink #06200f; muted #4b5850.
- Contrast (WCAG 2.1, computed): white on brand 6.90:1; brand on paper 6.20:1; ink on paper 15.46:1; muted on paper 6.72:1; ink on gold 10.57:1.
- Never color alone: negative tiles carry a minus sign and a pattern; claimed pairs show the owner's name.
- Different from this batch (beaker violet, asphalt slate, bike-path blue, clay sienna).

## Art
- People (illustrated): Jonah, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the game table (1, 16:9), story card pictures (8, 4:3).
- Drawn in code: cards, move cards and tiles.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Jonah; `lively-host` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.turn + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pick`: "Tap a card in your hand."
- how `move`: "Tap a move card to rewrite it."
- how `claim`: "Tap Claim when it matches."
- how `challenge`: "Tap Challenge and type a value."
- how `story`: "Pick the form that answers the question."
- event, whole, same quantity.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
algebra-tiles (`kit/algebra-tiles.js`), as described in algebra-tile-studio's spec. Uses `Poly` with fraction coefficients (`.add .sub .mul .equal .eval`), and `TileMat` with kinds `['x', '1', 'y']`, `negatives: true` and `zeroPairs: true`. Tool-only code: the card game, move cards as `Poly` rewrites with step checks, Jonah's turns and cheats, story cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Claims | Claim a look-alike | Claim checks `.equal`; a wrong claim costs a turn. |
| Moves | Skip to the answer | Cards only change through move cards. |
| Challenges | Never challenge | Jonah's wrong pairs count against the child at the end. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pick`; `move`; `claim`.
2. `challenge`.
3. `story`.
4. Same quantity (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.EE.1, 7.EE.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Different forms of an expression reveal different features | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | Kieran (2007), "Learning and teaching algebra at the middle school through college levels", Second Handbook of Research on Mathematics Teaching and Learning | yes |
| Distributing to only the first term is a common error | Booth, Barbieri, Eyer and Paré-Blagoev (2014), "Persistent and pernicious errors in algebraic problem solving", Journal of Problem Solving | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s18, 2026-11-10): 2(2x - 3) = 4x - 6 = 1/2(8x - 12) and -3(x - 4) = -3x + 12 for x from -5 to 5; 0.75y - 0.25y = 0.5y; a + 0.05a = 1.05a; 2(x + 3) at x = 1 is 8, 2x + 3 is 5; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table, mat and hand; at 680x425 mat as a sheet.
2. Hand cards are rewritten with move cards into table cards, rational levels included. (7.EE.1)
3. Wrong claims are challenged with a value. (7.EE.1)
4. Story cards are answered by choosing the form that shows the quantity. (7.EE.2)
5. Tiles come from the shared algebra-tiles engine with negatives.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: tiles regroup at once; no network requests.

## Open questions
None.
