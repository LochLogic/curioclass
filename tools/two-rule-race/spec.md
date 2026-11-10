# Two Rule Race

## One idea
Two garden snails, Pip and Moss, start side by side at 0 on a garden path with a ruler along it, and each follows its own rule card ("start at 0, add 3 each minute" and "start at 0, add 6 each minute"); the child presses Go, and each minute both snails step forward while a table of matched terms grows (Pip 0, 3, 6, 9; Moss 0, 6, 12, 18), and before each new pair appears the child predicts it; the pairs then become ordered pairs (Pip, Moss) that the child plots on a first-quadrant grid, and the points fall in a straight row; in relationship rounds the child types what is true for every pair ("Moss is always 2 times Pip") and the tool tests the claim against every term, through new rule pairs (add 2 and add 8, add 5 and add 10, then add 4 and add 6, where Moss is always 3/2 times Pip); in a build round the child writes two rules that make a goal relationship (Moss always 4 times Pip) and races them; at the end the table, the grid and the stated relationship sit together, so a fifth grader learns to generate two numerical patterns from two rules, identify relationships between corresponding terms, form ordered pairs from them, and graph the pairs on a coordinate plane.

## Not like
- two-trains (8, live): lines that meet. Here both start at 0, and the point is the relationship between terms.
- rule-machine (4, spec): one pattern and its hidden features. Here two patterns compared.
- sea-search-grid (5, concept): reading coordinates, same grid engine. Here plotting pairs from rules.
- growth-spurt (4, spec): "times as" comparisons. Here comparisons across whole patterns.

## Who and how
- Grade 5, Math, module "Patterns and Relationships". Standards: 5.OA.3 (generate two numerical patterns using two given rules; identify apparent relationships between corresponding terms; form ordered pairs consisting of corresponding terms from the two patterns, and graph the ordered pairs on a coordinate plane; for example, given the rule "Add 3" and the starting number 0, and given the rule "Add 6" and the starting number 0, generate terms in the resulting sequences, and observe that the terms in one sequence are twice the corresponding terms in the other sequence; explain informally why this is so).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five rule pairs, the race path, the table, the first-quadrant grid (Pip 0 to 30 across, Moss 0 to 60 up), the relationship tester, the build round. Extra: Class bets (the class bets on the relationship before Go on the projector). tool.json `modes: ["Garden race", "Class bets"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.OA.3 (generate) | Press Go and predict each next pair | the snails stepping; the table growing | 2 |
| 5.OA.3 (relationship) | State a relationship true for every pair; explain why | the tester checking every term | 3 |
| 5.OA.3 (graph) | Plot ordered pairs on the grid | points in a straight row | 4 |

## Screens and modes
Header (kit): title "Two Rule Race"; `Garden race`, `Class bets`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A garden path with a ruler along it, Pip and Moss at the start line, and two rule cards. The welcome is queued (`welcomeAfter: true`): "Pip adds 3 each minute. Moss adds 6. Where will they be after one minute? Type your guess, then tap Go." First hint: "Type your guess, then tap Go."

**The race (focus: the path).** At 1366x768 the path runs along the top with the table left and the grid right below; at 680x425 the table and grid are tabs. Each Go moves both snails one minute; the table adds a row. Six minutes per race.

**Plotting.** The child drags each pair (3, 6), (6, 12) onto the grid; a snail icon marks each point. The points line up from (0, 0).

**Relationship.** The child types a claim from sentence starters ("Moss is always ___ times Pip", "Moss is always ___ more than Pip") and taps Test. The tester checks every row and marks any row where it fails ("Moss is always 3 more" fails at minute 2). The child picks a reason card: "Moss adds twice as much each minute, and they started together."

**More pairs.** Add 2 and add 8 (4 times); add 5 and add 10 (2 times); add 4 and add 6 (3/2 times, or "Moss is half again Pip").

**Build (the aha).** "Make Moss always 4 times Pip." The child writes two rules and races them. Narrator: "Two rules made two patterns, and the relationship shows up three ways: in the table, on the grid and in the rules themselves."

**The end.** Tables, grids and claims. `Print` prints them.

**Class bets (extra).** The class bets before Go.

## Content
- Five rule pairs starting at 0, six minutes each, a grid with Pip 0 to 30 across and Moss 0 to 60 up, all readable with `Read`.
- Snails are cheerful; nobody loses badly, and the race is about the pattern.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Points can be moved until `Check`.
- Keyboard: Tab to the guess box, Go, table rows, the grid (arrows move a point by 1), the claim box and Test; Enter places or tests.
- With Motion off snails jump to their new spots.

## Look
- Accent `--brand` #3d6b2e garden moss (header, the table, buttons); gold #f4c542 (the point in hand, a claim that holds); paper #f0f6ec; ink #10200b; muted #525c4e.
- Contrast (WCAG 2.1, computed): white on brand 6.29:1; brand on paper 5.72:1; ink on paper 15.48:1; muted on paper 6.37:1; ink on gold 10.47:1.
- Never color alone: Pip and Moss carry names on the path, table and grid.
- Different from this batch (clockmaker brass, campfire red, lab teal, cart blue).

## Art
- Local FLUX (`scripts/localart.py`): the garden path (1, 16:9), Pip and Moss with character (2, 1:1).
- Drawn in code: the ruler, the table, the grid, snail icons for points.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the garden narrator; `wise-mentor` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.pair + ':' + state.minute + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `go`: "Type your guess, then tap Go."
- how `plot`: "Drag the pair onto the grid."
- how `claim`: "Finish the sentence, then tap Test."
- how `build`: "Write two rules, then tap Go."
- event, whole, build.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
coordinate (`kit/coordinate.js`), as described in coordinate-proof-lab's spec. Uses `RuleTable` with two "start and add" rules and `pairs()`, `CoordPlane` with `quadrant: 'first'`, range 0 to 30 across and 0 to 60 up (the engine's 0 to 30 default stretched on one axis) and `snap: 1`, and `plotPairs` with a snail icon. No polygons. Tool-only code: the race path, the relationship tester.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Wait for the table | Go needs a guess first; the score counts right guesses. |
| Claim | Type "Moss is bigger" | The tester needs a number and checks every row. |
| Build | Copy an earlier pair | The goal relationship is new (4 times). |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `go`.
2. `plot`; `claim`.
3. `build`.
4. Build (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.OA.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Relationships between corresponding terms prepare for proportional reasoning | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-7 Ratios and Proportional Relationships" | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad s15, 2026-11-10): add 3 and add 6 from 0 give 0, 3, 6, 9, 12 and 0, 6, 12, 18, 24, so Moss is always 2 times Pip; add 4 and add 6 give Moss 3/2 times Pip at every minute; add 2 and add 8 give 4 times; in six minutes Pip reaches at most 30 and Moss at most 60; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 path, table and grid; at 680x425 tabs.
2. Five rule pairs are generated with each pair predicted first. (5.OA.3)
3. A relationship is stated, tested on every row and explained. (5.OA.3)
4. Ordered pairs are plotted on the first-quadrant grid. (5.OA.3)
5. `Read` reads every card; every control is 48 px or more.
6. The relationship tester marks the row where a claim fails.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: snails jump; no network requests.

## Open questions
None.
