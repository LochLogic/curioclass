# Toy Box Sort

## One idea
On a bright bedroom floor the child taps a full toy box to dump out 12 toys, then drags each toy into one of three bins with picture labels (red, blue, yellow), and each bin counts aloud as toys land (10 or fewer a bin); "Which bin has the most?" and the bins slide into a line from most to fewest (5 red, 4 blue, 3 yellow); the same pile is then poured back and sorted by shape (6 balls, 4 blocks, 2 stars) and then by size (7 big, 5 small), so the counts change with the rule; then Robo the toy robot watches the child sort five toys and guesses where the sixth goes using the same feature, and later sorts a new pile by a secret rule while the child taps which one (color, shape or size); at the end the three sorts of the same pile sit side by side with their counts, and Robo says "I only know the rule you showed me," so a kindergartner learns to sort objects into given groups, count how many are in each group and line the groups up by count, and sees that a sorting machine groups things by whatever feature it was shown.

## Not like
- class-poll (1, concept): survey answers and tallies. Here sorting real things by a feature.
- shape-spy (K, spec): naming shapes in a scene. Here shape is one of three sorting rules.
- sheep-count (K, spec): counting one group. Here counting each bin and ordering them.
- picky-robot-shapes (1, concept): a robot's shape rules. Here a robot that learns a rule by watching.

## Who and how
- Kindergarten, Math, module "Sort and Count". Standards: K.MD.3 (classify objects into given categories; count the numbers of objects in each category and sort the categories by count; category counts limited to be less than or equal to 10), EK-ALG-ML-02 (CSTA 2026, paraphrased: grouping objects by a feature and seeing that a computer sorter groups by the feature it was shown; exact wording quoted before build).
- Format: sort. Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- One 12-toy pile sorted three ways, two more piles, two Robo watch rounds, two Robo secret-rule rounds. Extra: My bins (the child picks their own picture labels). tool.json `modes: ["Sort", "My bins"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.MD.3 (sort and count) | Drag toys into labeled bins; hear each bin count | bins filling; spoken counts | 2 |
| K.MD.3 (order by count) | Answer "Which has the most?"; resort the same pile two more ways | bins lining up; changing counts | 3 |
| EK-ALG-ML-02 | Teach Robo with five toys; name Robo's secret rule | Robo's guess; the secret-rule card | 4 |

## Screens and modes
Header (kit): title "Toy Box Sort"; `Sort`, `My bins`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A sunny bedroom floor, a full toy box with a lid and three empty bins. Robo sits on a shelf, eyes closed. The welcome is queued (`welcomeAfter: true`): "Time to clean up! Let's sort these toys. Tap the toy box to dump it." First hint: "Tap the toy box."

**Sorting (focus: the floor and bins).** At 1366x768 the toys spread on the floor with the bins along the bottom; at 680x425 the bins sit in a column at the right and toys scroll on the left. Every toy is at least 64 px. A toy in the wrong bin hops back out: "That one is blue. Find the blue bin." Each landing adds one to the bin's spoken count.

**Most to fewest.** When the floor is clear: "Which bin has the most?" The child taps a bin, then the bins slide into a line from most to fewest with their numbers on the front.

**Same pile, new rule (the aha).** "Let's pour them back and sort a new way!" The labels change to shapes (ball, block, star), then to sizes (big, small). The counts change: 5, 4, 3 by color; 6, 4, 2 by shape; 7, 5 by size. The three sorts sit side by side: "Same toys. Different rule. Different counts!"

**Robo rounds (EK-ALG-ML-02).** Robo opens its eyes: "Show me how you sort." The child sorts five toys; Robo guesses the sixth using the same feature, and says why: "You put the red ones together, so I put it with red." Then Robo sorts a new pile by a secret rule and the child taps Color, Shape or Size. Robo: "I only know the rule you showed me."

**The end.** The three sorts and Robo's rule card. `Print` prints a sorting page.

**My bins (extra).** The child picks picture labels for the bins and sorts any pile.

## Content
- Three piles of 12 toys in three colors, three shapes and two sizes; every bin holds 10 or fewer; four Robo rounds, all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A toy can be dragged out of a bin and back to the floor at any time.
- Keyboard: Tab to the box, each toy, each bin, the rule buttons and Robo's answer buttons; Enter picks up and drops.
- With Motion off toys jump into bins and bins swap places without sliding.

## Look
- Accent `--brand` #b02a37 robot red (header, Robo, buttons); gold #f4c542 (the toy in hand, the most bin); paper #fcf1f2; ink #2b080c; muted #614f52.
- Contrast (WCAG 2.1, computed): white on brand 6.50:1; brand on paper 5.88:1; ink on paper 16.63:1; muted on paper 6.91:1; ink on gold 11.30:1.
- Never color alone: color bins carry a paint splash picture and the color word; toys show their shape clearly.
- Different from this batch (meadow green, zoo orange, playground blue, spy purple).

## Art
- Local FLUX (`scripts/localart.py`): the bedroom floor (1, 16:9), Robo in three poses (watch, guess, sort) (3, 1:1), toys (balls, blocks, stars in three colors and two sizes) (6, 1:1).
- Drawn in code: bins, labels, counts, the rule cards.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the narrator and hints; `smooth-narrator` as Robo. `Curio.voice` with `scope: () => state.mode + ':' + state.pile + ':' + state.rule + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag a toy into its bin."
- how `most`: "Tap the bin with the most."
- how `teach`: "Sort five toys for Robo."
- how `secret`: "Tap Color, Shape or Size."
- event, whole, each bin count as toys land (short, cut off by the next drop).
- event, whole, same pile, new rule.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: bins with rules, counting, ordering, Robo's watch-then-guess rule. Piles sit in a marked block `/* TOY-BOX-SORT DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Drop toys anywhere | Wrong toys hop back with the reason. |
| Most | Tap any bin | The bins line up anyway and show the most. |
| Secret rule | Tap Color each time | Robo shows its bins again and asks once more. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`; counts as toys land.
2. `most`.
3. Same pile, new rule (whole), waits.
4. `teach`; `secret`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.MD.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| EK-ALG-ML-02 is a CSTA 2026 code for grouping by features in early grades | Computer Science Teachers Association, "CSTA K-12 CS Standards" (2026) | data/standards/csta-2026-ids.txt | yes |
| Sorting by one attribute, then re-sorting by another, is core kindergarten data work | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| A learning sorter groups new items by the features in the examples it was given | AI4K12, "Five Big Ideas in AI", big idea 3 (learning) | Touretzky and others (2019), "Envisioning AI for K-12", AAAI | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-10): 5 + 4 + 3, 6 + 4 + 2 and 7 + 5 each make 12; every bin is 10 or fewer; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 floor and bins; at 680x425 bin column.
2. Toys are sorted into labeled bins and each bin is counted. (K.MD.3)
3. Bins are lined up by count and one pile is sorted three ways. (K.MD.3)
4. Robo learns from five toys and the child names a secret rule. (EK-ALG-ML-02)
5. Every bin holds 10 or fewer; every card is spoken; controls are 64 px or more.
6. Robo is a toy; nothing is broken or hurt.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
- EK-ALG-ML-02 wording is not in the repo (default used: paraphrase from the code's place in CSTA 2026; exact wording quoted from the CSTA PDF before build).
