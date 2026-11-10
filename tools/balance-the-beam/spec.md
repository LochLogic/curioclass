# Balance the Beam

## One idea
In a gym a mouse acrobat named Tumble waits to cross a balance beam that hangs on a center post, and number blocks (each showing its dots) hang from hooks on both ends, so the beam itself is the equal sign: it only levels when both sides are worth the same; in true-or-false rounds an equation hangs on the beam (7 = 8 - 1, 5 + 2 = 2 + 5, 4 + 1 = 5 + 2) and the child taps Level or Tips before the beam moves to show it; in missing-block rounds one block is blank (8 + ? = 11, 5 = ? - 3, 6 + 6 = ? + 4) and the child picks a block from a tray until the beam levels and Tumble cartwheels across; in the trick round 4 + 1 = 5 + 2 seems to read right ("the answer is 5!") but the beam tips, and 6 = 6 levels with no plus sign at all, so a first grader learns that the equal sign means "the same as," to decide whether equations with addition and subtraction are true or false, and to find the unknown number in any position of an addition or subtraction equation with three whole numbers.

## Not like
- snack-scale (K, spec): which group has more, same family. Here the equal sign and unknowns.
- balance-puzzle (6, concept): solving with mystery bags. Here first equations within 20.
- make-ten-machine (1, spec): turning hard facts into easy ones. Here what the equal sign means.
- story-replay (1, spec): matching sentences to stories. Here judging bare equations.

## Who and how
- Grade 1, Math, module "The Equal Sign". Standards: 1.OA.7 (understand the meaning of the equal sign, and determine if equations involving addition and subtraction are true or false), 1.OA.8 (determine the unknown whole number in an addition or subtraction equation relating three whole numbers).
- Format: puzzle. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Twelve true-or-false beams (answer first, answer last, sums on both sides, no sign at all), twelve missing-block beams with the unknown in every spot, the trick round. Extra: Build a beam (the child builds an equation for a friend to test). tool.json `modes: ["Gym", "Build a beam"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.OA.7 | Tap Level or Tips, then watch | the beam level or tipping | 2 |
| 1.OA.7 (the trick) | Judge 4 + 1 = 5 + 2 and 6 = 6 | "the same as" on the post | 3 |
| 1.OA.8 | Pick the missing block in any spot | the beam leveling; Tumble crossing | 4 |

## Screens and modes
Header (kit): title "Balance the Beam"; `Gym`, `Build a beam`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A bright gym, a beam on a center post with a big = painted on it, hooks on each end, Tumble the mouse on a platform. The welcome is queued (`welcomeAfter: true`): "Hi! I'm Tumble. I can only cross when the beam is level. Is 7 = 8 - 1 level? Tap Level or Tips." First hint: "Tap Level or Tips."

**True or false (focus: the beam).** At 1366x768 the beam fills the middle with Level and Tips buttons below; at 680x425 blocks shrink and the buttons sit side by side under the beam. After the tap the beam moves. Each block shows its number and its dots, so a child can count to check.

**Missing block.** One hook holds a blank block. A tray of blocks 0 to 20 sits below. The child drags a block to the blank; the beam tips or levels. Unknowns go in every spot: 8 + ? = 11, ? - 3 = 5, 5 = ? - 3, 6 + 6 = ? + 4.

**The trick round (the aha).** 4 + 1 = 5 + 2 hangs. Many children say "Level, because 4 + 1 is 5." The beam tips toward 5 + 2. Then 6 = 6: the beam levels with no plus sign. The post lights up: "= means the same as."

**The end.** Tumble's cartwheel record with each level beam. `Print` prints it.

**Build a beam (extra).** The child hangs blocks on both sides; a friend taps Level or Tips.

## Content
- Number blocks 0 to 20 with dots, 24 beams within 20, the trick round, all spoken. Tumble never falls; a tipped beam just waits.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A block can be swapped any time before the beam checks.
- Keyboard: Tab to Level, Tips, the blank, and the tray; arrows pick a tray block; Enter hangs it.
- With Motion off the beam jumps to its tilt and Tumble appears across.

## Look
- Accent `--brand` #a1262f gym red (header, the post, buttons); gold #f4c542 (the level glow, the block in hand); paper #fcf0f1; ink #2a080b; muted #5e4c4e.
- Contrast (WCAG 2.1, computed): white on brand 7.41:1; brand on paper 6.66:1; ink on paper 16.58:1; muted on paper 7.20:1; ink on gold 11.35:1.
- Never color alone: Level and Tips carry a flat line and a slanted line icon and words.
- Different from this batch (closet blue, park green, court orange, vault indigo).

## Art
- Local FLUX (`scripts/localart.py`): the gym (1, 16:9), Tumble in three poses (wait, cartwheel, think) (3, 1:1).
- Drawn in code: the beam and post, blocks with dots, the tray.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as Tumble; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.beam + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `judge`: "Tap Level or Tips."
- how `fill`: "Drag a block to the blank hook."
- how `build`: "Hang blocks on both sides."
- event, whole, each beam result (short).
- event, whole, the trick round.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
balance (family "balance"). Uses the shared pieces from the marked block `/* BALANCE ENGINE: begin */ ... /* end */` as described in snack-scale's spec: the two-sided beam, here tipping by value instead of count. Tool-only code: number blocks with dots, the blank hook, the tray.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Judge | Always tap Level | The beam moves anyway; a tally shows right calls only. |
| Missing block | Try every block | Allowed; the beam shows "tips left" or "tips right" so tries narrow down, and the next beam changes. |
| Trick | Read left to right | The beam tips and the post explains. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `judge`.
2. Result (whole), waits.
3. `fill`.
4. Trick round (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.OA.7, 1.OA.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Many children read = as "the answer comes next," and 8 + 4 = ? + 5 style items reveal it | Falkner, Levi and Carpenter (1999), "Children's understanding of equality", Teaching Children Mathematics | McNeil and Alibali (2005), "Why won't you change your mind? Knowledge of operational patterns hinders learning and performance on equations", Child Development | yes |
| Balance models help children see the equal sign as "the same as" | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Falkner, Levi and Carpenter (1999), "Children's understanding of equality", Teaching Children Mathematics | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-10): 7 = 8 - 1 and 5 + 2 = 2 + 5 are true; 4 + 1 = 5 + 2 is false; 8 + 3 = 11; 5 = 8 - 3; 6 + 6 = 8 + 4; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 beam and buttons; at 680x425 smaller blocks.
2. Twelve true-or-false beams are judged and checked. (1.OA.7)
3. The trick round shows = means the same as. (1.OA.7)
4. Twelve missing blocks are found with the unknown in every spot. (1.OA.8)
5. Every card is spoken; every control is 56 px or more.
6. Tumble never falls.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
