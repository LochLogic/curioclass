# Bead Slider

## One idea
A long string of 100 beads stretches across the screen in ten colored groups of ten, folded into rows like a hundred chart, and a bead counter named Ollie (a friendly otter) asks for one sum at a time ("34 + 20"); the child slides 34 beads to the left, then slides 20 more as two whole tens, and the equation writes itself as 34 + 10 + 10 = 54; for 47 + 6 the ones run past the end of a group, the tool shows those ten ones snapping into one new ten, and 53 appears; quick slides ask "10 more than 63?" and "10 less than 63?" before the beads move, and "60 - 30" slides back three tens with no ones; in the trick round 47 + 30 lands on 77, and the child sees that adding tens keeps the ones bead in the same spot of its group; at the end a slide log lists every equation the child made, so a first grader learns to add within 100 a two-digit number and a one-digit number or a multiple of ten, making a new ten when needed, to find 10 more or 10 less in their head, and to subtract multiples of 10 from 10 to 90.

## Not like
- number-path-rescue (1, spec): reading and writing numerals to 120, same family. Here adding and subtracting tens and ones.
- crayon-boxes (1, concept): tens and ones as bundles to compare. Here sliding to add.
- jump-line (2, concept): an open number line to 1000. Here a bead string to 100.
- make-ten-machine (1, spec): fact strategies within 20. Here sums within 100.

## Who and how
- Grade 1, Math, module "Adding Tens and Ones". Standards: 1.NBT.4 (add within 100, including adding a two-digit number and a one-digit number, and adding a two-digit number and a multiple of 10, using concrete models or drawings and strategies based on place value; understand that in adding two-digit numbers, one adds tens and tens, ones and ones, and sometimes it is necessary to compose a ten), 1.NBT.5 (given a two-digit number, mentally find 10 more or 10 less than the number, without having to count), 1.NBT.6 (subtract multiples of 10 in the range 10 to 90 from multiples of 10 in the range 10 to 90).
- Format: simulator. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- A 100-bead string in ten groups, twelve slide sums, six quick slides, four take-back slides, the trick round, the slide log. Extra: Hidden numbers (numbers on the string hide so the child thinks in tens and ones). tool.json `modes: ["Slide", "Hidden numbers"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.NBT.4 | Slide a start, then tens and ones; make a new ten | beads moving by groups; the new ten snapping | 2 |
| 1.NBT.5 | Answer 10 more or 10 less before the slide | one whole group moving | 3 |
| 1.NBT.6 | Slide back whole tens | 60 - 30 = 30 with no ones moving | 4 |

## Screens and modes
Header (kit): title "Bead Slider"; `Slide`, `Hidden numbers`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A riverside workbench with a long bead string in ten colored groups, folded into ten rows. Ollie the otter holds a card. The welcome is queued (`welcomeAfter: true`): "Hi, I'm Ollie! I count with beads. Let's find 34 + 20. Tap Start." First hint: "Tap Start."

**Sliding (focus: the string).** At 1366x768 the string fills the middle in ten rows with the equation strip below; at 680x425 the rows shrink and the strip sits under them. Buttons: `+10`, `+1`, `-10`, `-1`, and drag on the string. Each slide adds to the strip: 34 + 10 + 10 = 54. When ones pass the end of a group, the ten loose beads snap together and glow: "Ten ones make a new ten!"

**Quick slides (1.NBT.5).** "What is 10 more than 63?" The child taps an answer from three choices; then one whole group slides to check. Then 10 less.

**Take-back slides (1.NBT.6).** "60 - 30." The child taps `-10` three times. "Three tens back. 30."

**The trick round (the aha).** 47 + 30 lands on 77. Ollie: "The ones bead stayed in the same spot in its group! Adding tens only changes the tens."

**The end.** The slide log with every equation. `Print` prints it.

**Hidden numbers (extra).** Numbers on the string hide; the child slides by groups and says the answer before the reveal.

## Content
- 100 beads in ten groups, twelve sums (four with a new ten), six quick slides, four take-back slides, the trick round, all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Undo` moves the last slide back.
- Keyboard: Tab to the string and buttons; arrows move one bead; Shift with arrows moves one ten.
- With Motion off beads jump and the new ten glows without snapping.

## Look
- Accent `--brand` #0d6466 bead teal (header, buttons, the strip); gold #f4c542 (the new ten, the bead in hand); paper #eef8f8; ink #07201f; muted #465a5a.
- Contrast (WCAG 2.1, computed): white on brand 6.93:1; brand on paper 6.40:1; ink on paper 15.72:1; muted on paper 6.76:1; ink on gold 10.45:1.
- Never color alone: groups alternate two colors and also carry a tick every ten.
- Different from this batch (leaf green, curtain crimson, river blue, factory orange).

## Art
- Local FLUX (`scripts/localart.py`): the riverside workbench (1, 16:9), Ollie the otter in three poses (card, cheer, think) (3, 1:1).
- Drawn in code: the bead string, groups, the strip, the log.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Ollie; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.beads + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `slide`: "Tap +10 or +1 to slide beads."
- how `quick`: "Tap the answer, then watch the beads."
- how `back`: "Tap -10 to slide tens back."
- event, whole, a new ten.
- event, whole, the trick round.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-path (family "number-path"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* NUMBER-PATH ENGINE: begin */ ... /* end */`: a 1 to 120 path laid out in rows of ten, moves by tens and ones, a running equation strip, and hidden-number views; number-path-rescue reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sum | Tap +1 many times | Allowed, but the strip shows the long way and Ollie asks for a tens way next round. |
| Quick slide | Guess | The slide checks and the next quick slide changes. |
| Take back | Tap -1 | Take-back rounds lock until whole tens are used. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `slide`.
2. New ten (whole), waits.
3. `quick`; `back`.
4. Trick round (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.NBT.4, 1.NBT.5, 1.NBT.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Bead strings and number paths in tens help children add by tens and ones | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Beishuizen (1993), "Mental strategies and materials or models for addition and subtraction up to 100", Journal for Research in Mathematics Education | yes |
| Composing a ten is the key step in adding two-digit numbers | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-10): 34 + 10 + 10 = 54; 34 + 25 = 59; 47 + 6 = 53 makes a new ten; 37 + 5 = 42; 63 + 10 = 73 and 63 - 10 = 53; 70 - 30 = 40 and 60 - 30 = 30; 47 + 30 ends in 7; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 ten rows and strip; at 680x425 smaller rows.
2. Twelve sums are slid, four with a new ten. (1.NBT.4)
3. Six quick slides find 10 more or 10 less. (1.NBT.5)
4. Four take-back slides subtract whole tens. (1.NBT.6)
5. Every card is spoken; every control is 56 px or more.
6. The trick round shows tens change and ones stay.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
