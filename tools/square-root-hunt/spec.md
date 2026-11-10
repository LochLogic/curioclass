# Square Root Hunt

## One idea
In a quiet puzzle room the puzzle master, Wen (made up, labeled "illustration"), points at a number line from 0 to 3 and says somewhere on it is a number that times itself makes 2, and the child has a net to trap it: 1 x 1 = 1 is too small and 2 x 2 = 4 too big, so the root sits between 1 and 2; the line zooms ten times and the child traps it again between 1.4 and 1.5 (1.96 and 2.25), then 1.41 and 1.42, then 1.414 and 1.415, each zoom adding one digit that never settles into a repeat; catch levels go the other way, catching a repeating decimal as a fraction by shifting and subtracting (x = 0.2727..., so 100x - x = 27 and x = 27/99 = 3/11), with the remainder loop from the grade 7 lab shown as a reminder that every fraction's decimal ends or repeats; compare levels place the square root of 50 (trapped between 7.07 and 7.08), 7.1, pi and 22/7 (3.142857...) on one line and find that pi sits just left of 22/7; the child estimates pi squared by squeezing pi first (between 3.14 squared and 3.15 squared, so about 9.87); a sort level bins numbers as rational or irrational with the reason (ends, repeats, or neither); at the end the child sees that every number has a decimal, rational ones end or repeat, and irrational ones can only be approached, which is enough to compare and place them, so an eighth grader learns to tell rational from irrational numbers by their decimals, turn repeating decimals into fractions, and use rational approximations to compare, place and estimate irrational numbers.

## Not like
- deep-sea-dive (6, spec): signed numbers, same number-line engine. Here irrational numbers.
- remainder-loop (7, spec): why fraction decimals end or repeat. Here catching repeats and trapping roots.
- size-of-everything (Grades 7-9, live): scientific notation. Here decimal squeezes.
- exponent-rule-builder (9, spec): rational exponents. Here square roots by approximation.

## Who and how
- Grade 8, Math, module "Irrational Numbers". Standards: 8.NS.1 (know that numbers that are not rational are called irrational; understand informally that every number has a decimal expansion; for rational numbers show that the decimal expansion repeats eventually, and convert a decimal expansion which repeats eventually into a rational number), 8.NS.2 (use rational approximations of irrational numbers to compare the size of irrational numbers, locate them approximately on a number line diagram, and estimate the value of expressions (e.g., pi squared)).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six squeeze levels, five catch levels, four compare lines, one sort bin of twelve numbers. Extra: Race (fewest zooms to trap a root to three places, on the projector). tool.json `modes: ["Hunt", "Race"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.NS.1 (catch) | Shift and subtract to catch repeats | 0.2727... = 3/11 | 3 |
| 8.NS.1 (sort) | Bin numbers with a reason | ends, repeats, neither | 4 |
| 8.NS.2 (squeeze) | Trap roots between decimals; zoom | 1.414 < root 2 < 1.415 | 2 |
| 8.NS.2 (compare, estimate) | Place roots, pi and 22/7; estimate pi squared | one line, four marks | 4 |

## Screens and modes
Header (kit): title "Square Root Hunt"; `Hunt`, `Race`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A quiet room with a long table, a number line from 0 to 3 glowing on it, a net tool, and Wen holding a magnifier. The welcome is queued (`welcomeAfter: true`): "A number times itself makes 2. Trap it. Drag the net's left edge to a whole number." First hint: "Drag the net's left edge."

**Squeeze (focus: the line).** At 1366x768 the line fills the width with a squares panel below; at 680x425 the panel is a sheet. The child drags both net edges; the panel squares each edge (1.4 x 1.4 = 1.96). If 2 is between the squares, the net closes and `Zoom` opens the next tenth. Digits stack in a growing decimal. Levels: root 2, root 3, root 10, root 50, root 0.5, and one perfect square (root 49) that stops at once.

**Catch.** A repeating decimal card. The child picks the shift (times 10 or times 100), types the subtracted line, and solves for x. Cards: 0.2727..., 0.333..., 0.142857..., 1.1666..., 0.0909....

**Compare.** Four marks to place on one line by squeezing each: root 50, 7.1, and then pi and 22/7 on a zoomed line. The child estimates pi squared from the pi trap.

**Sort.** Twelve numbers into rational and irrational bins, each with a reason card.

**Close enough (the aha).** Wen: "You can't write all of it. But you can always trap it, and that is enough to know where it lives."

**The end.** The trophy wall of trapped numbers. `Print` prints it.

**Race (extra).** Fewest zooms to three places.

## Content
- Every number shown to the digits needed, all readable with `Read`.
- Pi is given as known to be irrational, not proved.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Net edges can move until `Zoom`; catch lines can be retyped.
- Keyboard: Tab to the net's left and right edges (arrows move a tick), Zoom, the squares panel, catch boxes, compare marks and bins; Enter zooms or checks.
- With Motion off zooms jump without the slide.

## Look
- Accent `--brand` #6a2c5c puzzle plum (header, the net, buttons); gold #f4c542 (the edge in hand, the trapped number); paper #f8eff6; ink #230a1e; muted #5a4f57.
- Contrast (WCAG 2.1, computed): white on brand 9.87:1; brand on paper 8.77:1; ink on paper 16.47:1; muted on paper 6.94:1; ink on gold 11.39:1.
- Never color alone: the net shows "too small" and "too big" at each edge.
- Different from this batch (glacier blue, timber olive, harbor teal, cranberry).

## Art
- People (illustrated): Wen, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the puzzle room (1, 16:9).
- Drawn in code: the zooming line, net, squares panel and bins, because precision matters.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Wen; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.zoom + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `net`: "Drag the net's edges until the squares trap the number."
- how `zoom`: "Tap Zoom."
- how `catch`: "Pick the shift, then type the subtracted line."
- how `place`: "Drag the mark onto the line."
- how `sort`: "Drag the number to a bin and pick a reason."
- event, whole, close enough.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-line (`kit/number-line.js`), as described in roller-coaster-rounding's spec. Uses `NumberLine` with tenfold windows, `nl.zoom` for each squeeze, `nl.span` for the net, `nl.mark` for compare marks, and `nl.on('tap')`. The repeat display reuses the `/* REMAINDER ENGINE */` block from remainder-loop's spec. Tool-only code: the squares panel, catch solver with `Frac` (as described in equation-golf's spec), the sort bins.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Squeeze | Drag edges wide | `Zoom` opens only when the net is one tick wide. |
| Catch | Type a fraction from a calculator | The shifted and subtracted lines are checked. |
| Compare | Guess the order of pi and 22/7 | The marks must sit inside their own traps. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `net`; `zoom`.
2. `catch`.
3. `place`; `sort`.
4. Close enough (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.NS.1, 8.NS.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The square root of 2 is irrational | Euclid, "Elements", Book X | Niven (1961), "Numbers: Rational and Irrational", Mathematical Association of America | yes |
| Pi is irrational | Lambert (1768), proof of irrationality | Niven (1947), "A simple proof that pi is irrational", Bulletin of the American Mathematical Society | yes |
| Repeating decimals are rational by shift and subtract | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | Niven (1961), "Numbers: Rational and Irrational", Mathematical Association of America | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s21, 2026-11-10): 1.4, 1.41 and 1.414 squared fall under 2 and 1.5, 1.42 and 1.415 above; 27/99 = 3/11; 7.07 squared < 50 < 7.08 squared; pi < 22/7 = 3.142857...; 3.14 squared < pi squared < 3.15 squared and pi squared is about 9.87; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line and panel; at 680x425 panel as a sheet.
2. Six roots are trapped by zooming, with the squares shown at each edge. (8.NS.2)
3. Five repeating decimals are caught as fractions. (8.NS.1)
4. Four marks are placed, pi squared is estimated, and twelve numbers are sorted with reasons. (8.NS.1, 8.NS.2)
5. The remainder display reuses remainder-loop's block.
6. `Read` reads every card and digit; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: zooms jump; no network requests.

## Open questions
None.
