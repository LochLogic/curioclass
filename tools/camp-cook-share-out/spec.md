# Camp Cook Share-Out

## One idea
At summer camp the child helps the camp cook, Jo (made up, labeled "illustration"), share food fairly: 3 pans of cornbread go to 4 hungry tables, and the child cuts each pan into fourths and hands them out until each table holds 3 fourths, so 3 / 4 = 3/4 of a pan, and the share is written as both a division and a fraction; then half a pan is split among 3 tables (1/2 / 3 = 1/6 of a pan, seen by cutting the half into three slices and checking how many make a whole pan); then the cook counts quarter-cup scoops in 2 cups of trail mix (2 / 1/4 = 8 scoops) and thirds of a pan in 3 pans (9 slices); a share board keeps every result as a division sentence, a fraction and a picture, and word problems come from camp jobs (a 1/3-pound block of cheese shared by 2 campers; 4 cups of cocoa poured into 1/2-cup mugs); at the end the child sees that a fraction is a division and that dividing by a unit fraction counts how many fit, so a fifth grader learns to interpret a fraction as division of the numerator by the denominator, and to divide unit fractions by whole numbers and whole numbers by unit fractions.

## Not like
- how-many-fit (6, concept): dividing fractions by fractions. Here unit fractions and wholes.
- fraction-kitchen (5, spec): adding unlike fractions. Here sharing and dividing.
- shrink-ray (5, concept): multiplying fractions as scaling. Here fractions as division.
- recipe-scaler (4, spec): a whole number times a fraction. Here division.

## Who and how
- Grade 5, Math, module "Fractions as Division". Standards: 5.NF.3 (interpret a fraction as division of the numerator by the denominator (a/b = a / b); solve word problems involving division of whole numbers leading to answers in the form of fractions or mixed numbers), 5.NF.7 (apply and extend previous understandings of division to divide unit fractions by whole numbers and whole numbers by unit fractions: a. interpret division of a unit fraction by a non-zero whole number and compute such quotients; b. interpret division of a whole number by a unit fraction and compute such quotients; c. solve real world problems involving division of unit fractions by non-zero whole numbers and division of whole numbers by unit fractions).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four sharing rounds (pans to tables), three unit-fraction-by-whole rounds, three whole-by-unit-fraction rounds, six camp job problems, the share board. Extra: Teacher sets (the teacher picks pan and table counts). tool.json `modes: ["Camp kitchen", "Teacher sets"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.NF.3 | Cut pans and hand shares to tables | 3 pans for 4 tables is 3/4 each; 3 / 4 = 3/4 | 2 |
| 5.NF.7a, 5.NF.7b | Split a part among tables; count scoops in cups | 1/2 / 3 = 1/6; 2 / 1/4 = 8 | 3 |
| 5.NF.7c | Solve camp job problems | the share board | 4 |

## Screens and modes
Header (kit): title "Camp Cook Share-Out"; `Camp kitchen`, `Teacher sets`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A camp kitchen under pines, 3 pans of cornbread on the counter, 4 picnic tables of campers waving, and Jo in a camp apron. The welcome is queued (`welcomeAfter: true`): "Three pans, four tables. How much does each table get? Tap a pan to cut it." First hint: "Tap a pan to cut it."

**Sharing (focus: the counter).** At 1366x768 the counter is on the left, the tables along the right and the share board below; at 680x425 the board is a tab. The child picks a cut (halves, thirds, fourths, sixths) and drags pieces to tables. Fair shares glow; the board writes 3 / 4 = 3/4 and draws it. Rounds: 3 pans for 4 tables, 2 for 3, 5 for 4 (1 1/4 each), 7 for 2 (3 1/2 each).

**Part of a pan.** Half a pan for 3 tables: the child cuts the half into 3 and sees each slice is 1/6 of a whole pan. Then 1/3 pan for 2 (1/6), 1/4 pan for 3 (1/12).

**How many fit.** 2 cups of trail mix in 1/4-cup scoops: the child scoops and counts 8. Then 3 pans in thirds (9), 4 cups of cocoa in 1/2-cup mugs (8).

**Camp jobs.** Six word problems, each drawn before solving.

**Two sides (the aha).** Side by side: 1/2 / 3 = 1/6 and 3 / 1/2 = 6. Jo: "A fraction is a sharing. And dividing by a small piece counts how many pieces fit."

**The end.** The share board. `Print` prints it.

**Teacher sets (extra).** The teacher sets pans and tables.

## Content
- Pans, scoops, mugs and cheese blocks drawn in code for exact sizes; twenty rounds; all readable with `Read`.
- Divisors and unit fractions stay within the standard (unit fractions and whole numbers only).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces can be moved between tables until `Share`.
- Keyboard: Tab to pans, the cut picker, pieces, tables, the scoop and the board; Enter cuts or hands out.
- With Motion off pieces appear at their tables.

## Look
- Accent `--brand` #a8361b campfire red (header, the share board, buttons); gold #f4c542 (the piece in hand, a fair share); paper #fbf0ec; ink #2d0e06; muted #5f514b.
- Contrast (WCAG 2.1, computed): white on brand 6.55:1; brand on paper 5.85:1; ink on paper 15.95:1; muted on paper 6.79:1; ink on gold 10.97:1.
- Never color alone: fair shares show a check and the share in numbers.
- Different from this batch (clockmaker brass, lab teal, cart blue, garden moss).

## Art
- People (illustrated): Jo and four tables of campers, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the camp kitchen (1, 16:9).
- Drawn in code: pans, cuts, scoops, cups, mugs, the board.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Jo; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.cut + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `cut`: "Tap a pan, then pick a cut."
- how `share`: "Drag a piece to a table."
- how `scoop`: "Tap the scoop and count."
- how `job`: "Type the answer."
- event, whole, two sides.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: pans and cuts, fair-share checks, scoop counting, the share board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sharing | Pile everything on one table | Shares must be equal and use all the food. |
| How many fit | Type a guess | The scoops must be counted on screen first. |
| Jobs | Flip the division | The picture is drawn first; 3 / 1/2 and 1/2 / 3 look different. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `cut`; `share`.
2. `scoop`.
3. `job`.
4. Two sides (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.NF.3, 5.NF.7 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Fair sharing shows a fraction as division | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Empson and Levi (2011), "Extending Children's Mathematics: Fractions and Decimals", Heinemann | yes |
| Dividing a whole by a unit fraction counts how many pieces fit | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s15, 2026-11-10): 3 / 4 = 3/4; 1/2 / 3 = 1/6; 1/3 / 2 = 1/6; 2 / 1/4 = 8; 3 / 1/3 = 9; 5 / 4 = 1 1/4 and 7 / 2 = 3 1/2; 4 / 1/2 = 8; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 counter, tables and board; at 680x425 board as a tab.
2. Four sharing rounds write the share as a division and a fraction. (5.NF.3)
3. Unit fractions are divided by wholes and wholes by unit fractions. (5.NF.7a, 5.NF.7b)
4. Six camp jobs are solved with pictures. (5.NF.7c)
5. `Read` reads every card; every control is 48 px or more.
6. Jo and the campers are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: pieces appear at tables; no network requests.

## Open questions
- The idea card flags overlap with how-many-fit and fraction-kitchen (default used: unit fractions and whole numbers only, shared at camp; how-many-fit keeps fraction by fraction division; fraction-kitchen keeps adding unlike fractions).
