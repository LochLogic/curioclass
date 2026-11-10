# Jump Line

## One idea
On a long empty line drawn along a park path, a grasshopper named Hopper waits at the start, and the child solves a sum like 46 + 38 by dragging jumps of any size (+30, +4, +4) and labeling each, while Hopper hops along and the line writes the steps; subtraction runs backward (84 - 38) or as "how far from 38 to 46?"; bigger numbers come later (270 + 50 crosses 300, 600 - 235); in the path gallery three illustrated classmates (made up, labeled "illustration") show their own paths to the same answer (one jumps to the next ten first, one jumps a hundred and backs up, one has a mistake), and the child picks which paths are right and finishes "It works because..." from sentence pieces; a mental lane asks +10, -10, +100 and -100 from any number, said fast; the four-number path adds up to four two-digit numbers in one walk, so a second grader learns to add and subtract fluently within 100, to add up to four two-digit numbers, to add and subtract within 1000 with a drawn model that can compose or break apart tens and hundreds, to add or subtract 10 or 100 mentally, and to explain why a strategy works.

## Not like
- bead-slider (1, spec): a fixed bead string to 100. Here an open line the child draws, to 1000.
- roller-coaster-rounding (3, spec): rounding on a number line, same family. Here exact jumps.
- place-value-vault (2, spec): reading and comparing three-digit numbers. Here adding and subtracting.
- fact-rally (2, spec): one-digit facts. Here multi-digit strategies.

## Who and how
- Grade 2, Math, module "Adding and Subtracting to 1000". Standards: 2.NBT.5 (fluently add and subtract within 100 using strategies based on place value, properties of operations, and/or the relationship between addition and subtraction), 2.NBT.6 (add up to four two-digit numbers using strategies based on place value and properties of operations), 2.NBT.7 (add and subtract within 1000, using concrete models or drawings and strategies based on place value, properties of operations, and/or the relationship between addition and subtraction; relate the strategy to a written method; understand that in adding or subtracting three-digit numbers, one adds or subtracts hundreds and hundreds, tens and tens, ones and ones; and sometimes it is necessary to compose or decompose tens or hundreds), 2.NBT.8 (mentally add 10 or 100 to a given number 100 to 900, and mentally subtract 10 or 100 from a given number 100 to 900), 2.NBT.9 (explain why addition and subtraction strategies work, using place value and the properties of operations).
- Format: sandbox. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Twelve within-100 problems, eight within-1000 problems, six gallery rounds, twelve mental-lane items, three four-number paths. Extra: Path swap (two players solve the same sum and compare paths). tool.json `modes: ["Path", "Path swap"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.NBT.5, 2.NBT.6 | Drag and label jumps within 100; four-number paths | Hopper's hops; the written steps | 2 |
| 2.NBT.7, 2.NBT.8 | Jump across hundreds; the mental lane | 270 + 50 crossing 300; ±10 and ±100 | 3 |
| 2.NBT.9 | Judge gallery paths and finish "It works because" | three paths to one answer | 4 |

## Screens and modes
Header (kit): title "Jump Line"; `Path`, `Path swap`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A sunny park path with a long blank line chalked along it, Hopper at the start, a problem card: 46 + 38. The welcome is queued (`welcomeAfter: true`): "Hey, I'm Hopper! Help me get to the answer. Tap 46 on the line to start, then drag a jump." First hint: "Tap the line to place 46."

**Jumping (focus: the line).** At 1366x768 the line runs across the screen with the steps strip below; at 680x425 the line scrolls and the strip is one row. The child places the start, then drags a jump; a chooser asks its size (+1, +2, +5, +10, +20, +30, +100 or type one). Hopper hops; the strip writes 46 + 30 = 76, 76 + 4 = 80, 80 + 4 = 84.

**Subtraction.** 84 - 38 runs backward. "How far from 38 to 46?" runs forward from 38 and counts the jumps.

**Hundreds.** 270 + 50: the line zooms out to hundreds; the jump to 300 glows "a new hundred!" 600 - 235: the child breaks the jump into -200, -30, -5.

**Path gallery (the aha).** Three classmates' paths for 46 + 38: Ana jumps to 50 first (+4, +30, +4); Ben jumps +40 and back -2; Kai means +30 and +8 but jumps +20, landing on 74 (a slip). The child taps the right ones and fixes Kai's. "It works because..." pieces: "40 is 2 more than 38," "tens are easy to add." Hopper: "Different paths, same answer. Friendly tens make paths short."

**Mental lane.** "10 more than 452?" "100 less than 803?" Quick taps; Hopper hops once to check.

**The end.** A path album with each path the child drew. `Print` prints it.

**Path swap (extra).** Two players solve the same sum and their paths sit side by side.

## Content
- Problems within 100 and 1000, three classmates labeled "illustration", sentence pieces for explaining, all spoken. Mistakes in the gallery are friendly slips, never mocked.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Jumps can be dragged off and redrawn at any time.
- Keyboard: Tab to the line, the jump chooser, gallery paths and sentence pieces; arrows move the start; Enter places a jump.
- With Motion off Hopper appears at each landing and the zoom is a jump cut.

## Look
- Accent `--brand` #356b23 park green (header, the line, buttons); gold #f4c542 (the new hundred, the jump in hand); paper #f2f8ee; ink #0f200a; muted #4b5a45.
- Contrast (WCAG 2.1, computed): white on brand 6.40:1; brand on paper 5.93:1; ink on paper 15.79:1; muted on paper 6.83:1; ink on gold 10.49:1.
- Never color alone: jump labels are written on each arc.
- Different from this batch (closet blue, gym red, court orange, vault indigo).

## Art
- People (illustrated): three classmates (Ana, Ben, Kai), labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the park path (1, 16:9), Hopper in three poses (hop, land, think) (3, 1:1).
- Drawn in code: the line, jump arcs, labels, the steps strip.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Hopper; `curious-librarian` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.problem + ':' + state.at + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `start`: "Tap the line to place the start."
- how `jump`: "Drag a jump and pick its size."
- how `gallery`: "Tap each path that works."
- how `because`: "Drag pieces to finish the sentence."
- how `mental`: "Tap the answer."
- event, whole, a new hundred.
- event, whole, the gallery.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-line (`kit/number-line.js`, as described in roller-coaster-rounding's spec and docs/families/number-line.md). Uses: `NumberLine` (0 to 100 and 0 to 1000 windows), `nl.x` to place Hopper, `nl.jump` for each labeled jump arc, `nl.mark` for the start and landings, `nl.zoom` for tens and hundreds, `nl.on('tap')`. Hopper, the steps strip and the gallery are this tool's own SVG.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Path | Make many +1 jumps | Allowed, but the strip shows the long way and the next problem asks for three jumps or fewer. |
| Gallery | Mark every path right | Kai's slip must be found and fixed. |
| Because | Drag any pieces | Only true pieces fit the chosen path. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `start`; `jump`.
2. New hundred (whole), waits.
3. Gallery (whole), waits. `gallery`; `because`.
4. `mental`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.NBT.5 to 2.NBT.9 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The open (empty) number line supports flexible jump strategies | Bobis and Bobis (2005), "The empty number line: making children's thinking visible", in Making Mathematics Vital, AAMT | Beishuizen (1993), "Mental strategies and materials or models for addition and subtraction up to 100", Journal for Research in Mathematics Education | yes |
| Comparing strategies and explaining why they work is part of grade 2 | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-10): 46 + 30 + 4 + 4 = 84 = 46 + 38; 270 + 50 = 320; 600 - 235 = 365; from 38 to 46 is 8; 23 + 15 + 32 + 19 = 89; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line and strip; at 680x425 scrolling line.
2. Twelve problems within 100 and three four-number paths are jumped. (2.NBT.5, 2.NBT.6)
3. Eight problems within 1000 and twelve mental-lane items are done. (2.NBT.7, 2.NBT.8)
4. Six gallery rounds are judged and explained. (2.NBT.9)
5. Every card is spoken; every control is 56 px or more.
6. Classmates are labeled illustration; slips are never mocked.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps without hops; no network requests.

## Open questions
None.
