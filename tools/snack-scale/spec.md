# Snack Scale

## One idea
On a playground seesaw held level by a squirrel named Nutmeg, the child drags crackers from a bowl onto each side (up to 10 a side, every cracker in a round exactly the same), taps a side to guess which has more (or taps "the same"), then taps Let go, and the side with more crackers sinks while level means the same; a Match button lines the crackers up in pairs across the seesaw so the leftover crackers glow, showing the same answer a second way, and number tags can be turned on to count each side; in card rounds Nutmeg holds up two numerals (6 and 9) and the child guesses which is more before the seesaw loads that many crackers to check; in the trick round 7 crackers spread wide look like more than 8 crackers bunched up, but the seesaw and the pairs both say 8 wins, so spread out doesn't mean more; at the end a sticker page holds the child's comparisons, so a kindergartner learns to tell whether the number of objects in one group is greater than, less than or equal to the number in another group, by matching and by counting, and to compare two numbers between 1 and 10 written as numerals.

## Not like
- who-wins (K, spec): which object is heavier or longer. Here which group has more, with every snack the same.
- balance-the-beam (1, concept): the equal sign with numbers on both sides, same family. Here more, less and the same.
- sheep-count (K, spec): counting one group. Here comparing two.
- ten-frame-spillover (K, concept): numbers as ten and some more. Here which number is bigger.

## Who and how
- Kindergarten, Math, module "More, Less, Same". Standards: K.CC.6 (identify whether the number of objects in one group is greater than, less than, or equal to the number of objects in another group, e.g., by using matching and counting strategies), K.CC.7 (compare two numbers between 1 and 10 presented as written numerals).
- Format: sandbox. Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- The seesaw with up to 10 a side, the Match button, number tags, eight build rounds, four card rounds, the trick round, a snack switcher (crackers, apple slices, grapes; one kind per round). Extra: Class vote (the class votes before Let go). tool.json `modes: ["Seesaw", "Class vote"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.CC.6 (matching) | Build two groups, guess, let go, then tap Match | the seesaw tipping; pairs and leftovers | 2 |
| K.CC.6 (counting and the trick) | Count with tags; judge spread against bunched | number tags; the trick round | 3 |
| K.CC.7 | Guess which numeral is more, then check on the seesaw | the two cards; the loaded seesaw | 4 |

## Screens and modes
Header (kit): title "Snack Scale"; `Seesaw`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A sunny playground, a red seesaw held level by Nutmeg the squirrel, a bowl of crackers. The welcome is queued (`welcomeAfter: true`): "Hi, I'm Nutmeg! Put crackers on both sides of my seesaw. Then guess which side has more. Drag a cracker onto a side." First hint: "Drag a cracker onto the seesaw."

**Building (focus: the seesaw).** At 1366x768 the seesaw fills the middle with the bowl below and buttons at the side; at 680x425 the bowl is a row under the seesaw. Crackers are at least 64 px. The child guesses with three big buttons: Left has more, Right has more, The same. `Let go`: Nutmeg steps back and the seesaw tips gently (level for the same). Nutmeg says: "This side has more. That side has less."

**Match.** `Match` slides crackers into pairs across the middle. Leftovers glow. "These extra crackers are why this side has more." A `Count` button tags each side's crackers with numbers.

**The trick round (the aha).** Left: 7 crackers spread wide. Right: 8 crackers in a tight pile. "Which side has more?" After the guess, Let go and Match both show 8 wins. Nutmeg: "Spread out doesn't mean more. Match them up or count to be sure!"

**Card rounds (K.CC.7).** Nutmeg holds up two numeral cards (6 and 9, then 3 and 5, then 10 and 7, then 4 and 4). The child taps the bigger number or "the same," then the seesaw loads that many crackers to check.

**The end.** A sticker page with each comparison: pictures and the words more, less, same. `Print` prints it.

**Class vote (extra).** The class votes before each Let go.

## Content
- Identical snacks in each round, the seesaw rule (more sinks, the same stays level), eight build rounds, four card rounds, the trick round, all spoken. Nutmeg and the snacks are never hurt or eaten on screen.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Crackers can be dragged off a side back to the bowl at any time before Let go.
- Keyboard: Tab to the bowl, each side, guess buttons, `Let go`, `Match`, `Count` and cards; Enter places and picks.
- With Motion off the seesaw jumps to its tilt and pairs appear in place.

## Look
- Accent `--brand` #1c5a9e playground blue (header, buttons, numeral cards); gold #f4c542 (leftover crackers, the guess picked); paper #f0f5fb; ink #0a1a2e; muted #4c5766.
- Contrast (WCAG 2.1, computed): white on brand 6.99:1; brand on paper 6.37:1; ink on paper 15.96:1; muted on paper 6.69:1; ink on gold 10.76:1.
- Never color alone: leftovers glow and get a ring; buttons carry words and arrows.
- Different from this batch (meadow green, zoo orange, spy purple, robot red).

## Art
- Local FLUX (`scripts/localart.py`): the playground (1, 16:9), Nutmeg in three poses (hold, cheer, think) (3, 1:1), three snacks (3, 1:1).
- Drawn in code: the seesaw, pairs, tags, numeral cards.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Nutmeg; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `build`: "Drag crackers onto both sides."
- how `guess`: "Tap the side with more, or The same."
- how `letgo`: "Tap Let go."
- how `match`: "Tap Match to make pairs."
- event, whole, each result.
- event, whole, the trick round.
- how `cards`: "Tap the bigger number."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
balance (family "balance"; no engine file yet). This tool builds the balance family's shared pieces first, in a marked block `/* BALANCE ENGINE: begin */ ... /* end */`: a two-sided beam that tips by count (or later by value), pairing across the middle, and number tags; balance-the-beam and balance-puzzle reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Guess | Always guess "left" | Guesses aren't scored; the seesaw and Match still show why. |
| Trick round | Pick the spread side | The seesaw and Match both show it's less. |
| Cards | Tap either card | The seesaw loads both numbers to check. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `build`; `guess`; `letgo`.
2. Result (whole), waits. `match`.
3. Trick round (whole), waits.
4. `cards`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.CC.6, K.CC.7 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Matching and counting are the two strategies for comparing groups | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K, Counting and Cardinality" | National Research Council (2009), "Mathematics Learning in Early Childhood" | yes |
| Young children judge "more" by how spread out a row is (Piaget's number conservation) | Clements and Sarama, "Learning and Teaching Early Math" (2014) | National Research Council (2009), "Mathematics Learning in Early Childhood" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-10): 8 is more than 7 by one leftover; 9 is more than 6; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 seesaw and bowl; at 680x425 row.
2. Eight build rounds are compared with the seesaw and Match. (K.CC.6)
3. The trick round and counting tags show spread doesn't mean more. (K.CC.6)
4. Four numeral card rounds are compared and checked. (K.CC.7)
5. Every round uses one identical snack; every card is spoken; controls are 64 px or more.
6. Nothing is eaten or hurt on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
- Overlap risk with who-wins (default used: every round uses one identical snack so the seesaw tips by how many, never by weight; who-wins keeps weight).
