# Fraction Wall Duel

## One idea
A card game played against Rosa (a made-up rival, labeled "illustration") on a shared fraction wall: Rosa plays 3/4 face up and the child plays a card from a hand of five, both fractions light up as bars on the wall, and the bigger fraction wins the round, but only if the child names a reason the wall can show: rename to the same pieces (3/4 is 9/12, 5/6 is 10/12), the same number of pieces (3/5 against 3/8, and fifths are bigger), or the half line (5/8 is past 1/2, 3/7 is not); playing an equal fraction steals the round, but only after the child splits each third into two sixths on the wall to prove 2/3 is 4/6; later decks add tenths and hundredths, and trap cards that compare half of a big pizza with half of a small one, which the rule book voids because the wholes differ; at the end the child's winning reasons are listed, and the child sees that a fraction's size depends on both numbers and that one amount wears many names, so a fourth grader learns to explain and make equivalent fractions by splitting pieces, and to compare two fractions with different numerators and denominators by common pieces, common counts or the half benchmark, for the same whole.

## Not like
- fraction-trail (3, spec): fractions as places on a line. Here a wall and reasons.
- how-many-fit (6, concept): dividing fractions, same wall engine. Here equivalence and comparing.
- fraction-kitchen (5, concept): adding unlike fractions with cups. Here comparing them.
- money-and-meters (4, spec): tenths and hundredths in four views. Here a card duel.

## Who and how
- Grade 4, Math, module "Equivalent Fractions and Comparing". Standards: 4.NF.1 (explain why a fraction a/b is equivalent to a fraction (n x a)/(n x b) by using visual fraction models, with attention to how the number and size of the parts differ even though the two fractions themselves are the same size; use this principle to recognize and generate equivalent fractions), 4.NF.2 (compare two fractions with different numerators and different denominators, e.g., by creating common denominators or numerators, or by comparing to a benchmark fraction such as 1/2; recognize that comparisons are valid only when the two fractions refer to the same whole; record the results with symbols >, =, or <, and justify the conclusions, e.g., by using a visual fraction model).
- Format: cards. Driver: one student alone against the computer rival (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- A wall from halves to twelfths plus tenths and hundredths, three decks (twelve rounds each), three reasons, the steal split, trap cards, the rule book. Extra: Two players (two students on one screen, hands hidden by a pass-the-device screen). tool.json `modes: ["Duel Rosa", "Two players"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.NF.1 | Split each piece into n pieces to prove a steal | thirds splitting into sixths; 2/3 = 4/6 | 2 |
| 4.NF.2 (compare) | Win with a reason: same pieces, same count or the half line | bars and the reason animating | 3 |
| 4.NF.2 (same whole) | Void trap cards with different wholes | the rule book's same-whole page | 4 |

## Screens and modes
Header (kit): title "Fraction Wall Duel"; `Duel Rosa`, `Two players`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A fraction wall on a game table, a hand of five cards and Rosa grinning across the table with 3/4 face up. The welcome is queued (`welcomeAfter: true`): "Rosa played 3/4. Beat it, or match it to steal! Drag a card onto the table." First hint: "Drag a card onto the table."

**A round (focus: the wall).** At 1366x768 the wall fills the middle with hands below and above; at 680x425 the wall scrolls sideways and the hand is a tray. Both fractions light up as bars. If the child's is bigger, three reason buttons appear: same pieces, same count, half line. The chosen reason animates: rows split until pieces match (3/4 to 9/12, 5/6 to 10/12), or same counts are compared by piece size, or a half line drops across the wall. A wrong reason doesn't win; the wall shows why and the child picks again.

**Steals.** Playing 4/6 on Rosa's 2/3 opens a split tool: the child splits each third into two pieces, and the bars line up exactly. Steal.

**Later decks.** Deck 2 adds tenths and hundredths (3/10 against 25/100). Deck 3 adds trap cards: "half of the big pizza" against "half of the small pizza". The child opens the rule book and voids the round.

**Rosa's turn.** Rosa sometimes makes a claim with a wrong reason, and the child can challenge it.

**Final score (the aha).** The list of rounds and reasons. Rosa: "You didn't just win. You proved it every time. Same amount, many names."

**The end.** The reason list. `Print` prints it and a paper fraction wall.

**Two players (extra).** Hands hidden by a pass-the-device screen.

## Content
- Three decks of 24 cards, denominators 2, 3, 4, 5, 6, 8, 10, 12 and 100, four trap cards, the rule book, all readable with `Read`.
- Rosa is a friendly rival; losing a round just deals again.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be put back until a reason is picked.
- Keyboard: Tab to cards, the reason buttons, the split tool, the rule book and challenge; Enter plays.
- With Motion off bars split and line up at once.

## Look
- Accent `--brand` #9a3d12 brick orange (header, the wall frame, card backs); gold #f4c542 (the card in hand, a winning bar); paper #fbf1ec; ink #2b1005; muted #5e5049.
- Contrast (WCAG 2.1, computed): white on brand 6.88:1; brand on paper 6.19:1; ink on paper 16.03:1; muted on paper 6.95:1; ink on gold 10.95:1.
- Never color alone: bars carry fraction labels; the child's and Rosa's bars carry names.
- Different from this batch (craft-fair plum, quilt navy, track teal, workbench olive).

## Art
- People (illustrated): Rosa, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the game table (1, 16:9), card back art (1, 3:4).
- Drawn in code: the wall, bars, split lines, cards, the half line.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Rosa; `knowing-guide` as the referee and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.deck + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `play`: "Drag a card onto the table."
- how `reason`: "Pick a reason the wall can show."
- how `split`: "Tap Split to cut each piece."
- how `trap`: "Open the rule book."
- event, whole, final score.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-wall (family "fraction-wall"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* FRACTION-WALL ENGINE: begin */ ... /* end */`: a wall of rows from 1 down to twelfths plus tenths and hundredths, bars for any a/b, row splitting by n with matching checks, the half line, and exact comparison with `Frac`; how-many-fit reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reasons | Tap reasons until one works | Each wrong reason is shown false on the wall and the round counts it. |
| Steals | Play any card that looks equal | The split must line the bars up exactly. |
| Traps | Play them as normal cards | The rule book voids them; the round needs the void. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `play`; `reason`.
2. `split`.
3. `trap`.
4. Final score (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NF.1, 4.NF.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Comparing by common denominators, common numerators or benchmarks like 1/2 | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
| Equivalent fractions shown by splitting each part into n parts | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Van de Walle, Karp and Bay-Williams (2019), "Elementary and Middle School Mathematics: Teaching Developmentally", 10th edition | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): 3/4 = 9/12 and 5/6 = 10/12, so 5/6 > 3/4; 3/5 > 3/8; 3/7 < 1/2 < 5/8; 2/3 = 4/6; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 wall and hands; at 680x425 wall scrolls, hand as a tray.
2. Steals are proved by splitting each piece into n pieces. (4.NF.1)
3. Every win is backed by a reason the wall shows. (4.NF.2)
4. Trap cards with different wholes are voided. (4.NF.2)
5. `Read` reads every card; every control is 48 px or more.
6. Rosa is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: bars split at once; no network requests.

## Open questions
None.
