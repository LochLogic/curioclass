# Marble Ramp Trials

## One idea
On a kitchen floor a cardboard ramp 1 meter long leans on a stack of books, a marble waits at the top, and Coach Kim (made up, labeled "illustration") hands the child a big stopwatch button: tap Start when the marble goes and Stop when it hits the book at the bottom, again and again; because the child's own taps time each run, real reaction time is in the data, so the table fills with 1.42, 1.38, 1.51, 1.45, 1.40 seconds that never quite match, and one run gets a hidden bump (2.80) while one row gets a typo (14.0); the child taps each odd row to see its replay, picks a cause (a late tap, a bump, a typo), marks the outliers, and sees that the middle value barely moves (1.45 with them, 1.42 without) while the average jumps from about 1.43 to 3.42; then the child raises the ramp in three steps (10, 15 and 20 cm) and switches the surface (bare cardboard, felt, foil), five runs each, and a dot chart shows taller ramps are faster on every surface (about 1.7, 1.4 and 1.2 seconds on cardboard) and felt slows every height; at the end the child sees that measurements always vary a little, so you repeat, find the middle, and explain the outliers before trusting a pattern, so a student in grades 3 to 5 learns why data varies, how to spot outliers, and how two attributes work together.

## Not like
- score-keeper (3, live): variables in a game. Here repeated measurements.
- data-table-builder (4, spec): tables and charts from class data. Here variation and outliers.
- leaf-sorter-ai (5, spec): features for a classifier. Here two attributes in an experiment.
- fair-survey-kit (3, spec): cleaning survey rows. Here measurement spread.

## Who and how
- Grades 3-5, Computer Science, module "Why Data Varies". Standards: E3-DAT-DI-10, E4-DAT-DI-10, E5-DAT-DI-10 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Repeat measurements, spot outliers and relationships between attributes").
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every row and card. Controls 48 px or more.
- Seven timed runs with two seeded oddities, cause replays, a 3-by-3 trial grid of five runs each, the dot chart. Extra: Real ramp (a build card for a real ramp and a table for your own times). tool.json `modes: ["Lab", "Real ramp"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-DAT-DI-10 | Time repeated runs; describe the spread | times that never match | 2 |
| E4-DAT-DI-10 | Find outliers and their causes; decide | the middle barely moves | 3 |
| E5-DAT-DI-10 | Change height and surface; read the chart | taller faster; felt slower | 4 |

## Screens and modes
Header (kit): title "Marble Ramp Trials"; `Lab`, `Real ramp`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A kitchen floor, a cardboard ramp on books, a marble, a big round stopwatch button, an empty table, and Coach Kim with a whistle. The welcome is queued (`welcomeAfter: true`): "Time it yourself. Tap Start when the marble goes." First hint: "Tap Start."

**Time it (focus: the ramp).** At 1366x768 the ramp is left with the table and stopwatch right; at 680x425 the table is a tab. `Start` releases the marble; the child taps `Stop` when it hits the book. The time is the child's own tap, rounded to hundredths. Seven runs; the tool hides a bump in one and a typo in one row.

**Odd ones.** Each row has a replay button. The child picks a cause and marks keep or outlier. Middle and average show with and without outliers.

**Two attributes.** A height dial (10, 15, 20 cm) and a surface switch (cardboard, felt, foil). After the child times a few runs per setting, `Fill the rest` adds simulated runs with tap noise so each cell has five. A dot chart groups them.

**Repeat, then trust (the aha).** Coach Kim: "Every run is a little different. Repeat it, find the middle, and explain the odd ones."

**The end.** The table and chart. `Print` prints them and the build card.

**Real ramp (extra).** Enter your own times.

## Content
- Times come from the child's taps plus a model of a rolling marble, labeled "simulated" where filled.
- Surfaces slow the marble by fixed simulated amounts (felt most), labeled "simulated".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Runs can be redone; marks can be changed until `Find the middle`.
- Keyboard: Space is Start and Stop; Tab to the table (arrows move between rows), replay, cause menus, the height dial and surface switch; Enter picks.
- With Motion off the marble is shown at start and finish only; the child still taps when the "go" and "hit" cues sound and show.

## Look
- Accent `--brand` #2d6b2f ramp green (header, the table, buttons); gold #f4c542 (the stopwatch, the middle marker); paper #eff6ef; ink #0a220b; muted #4b574b.
- Contrast (WCAG 2.1, computed): white on brand 6.45:1; brand on paper 5.87:1; ink on paper 15.32:1; muted on paper 6.91:1; ink on gold 10.36:1.
- Never color alone: outliers carry a ring and the word "outlier"; surfaces carry dot shapes.
- Different from this batch (circuit blue, kitchen-table rust, corkboard violet, helper teal).

## Art
- People (illustrated): Coach Kim, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the kitchen floor with the ramp (1, 16:9).
- Drawn in code: the marble, ramp angle, stopwatch, table and dot chart.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Coach Kim; `smooth-narrator` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `start`: "Tap Start."
- how `stop`: "Tap Stop when it hits the book."
- how `cause`: "Tap replay, then pick a cause."
- how `setting`: "Turn the height dial or tap a surface."
- how `chart`: "Tap a group on the chart."
- event, whole, repeat, then trust.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the rolling-ball model (t = square root of 2L divided by (5/7 g h / L)), tap timing, seeded oddities, middle and average, the dot chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Spread | Tap the same way each time | Real taps still vary, and the child describes the spread. |
| Outliers | Mark everything an outlier | Each mark needs a cause from the replay. |
| Two attributes | Change only height | The chart needs every surface at every height. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `start`; `stop`.
2. `cause`.
3. `setting`; `chart`.
4. Repeat, then trust (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| A solid ball rolling down an incline accelerates at 5/7 g times the sine of the angle | Serway and Jewett, "Physics for Scientists and Engineers", rolling motion chapter | OpenStax, "University Physics Volume 1", section 11.1 | yes |
| Human reaction time adds error to hand timing | Kosinski (2013), "A Literature Review on Reaction Time", Clemson University | National Institute of Standards and Technology, guidance on manual stopwatch uncertainty | yes |
| Medians resist outliers; repeat trials before trusting a pattern | American Statistical Association, "GAISE II" (2020) | National Research Council (2012), "A Framework for K-12 Science Education", Practice 4 | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s24, 2026-11-10): a 1 m ramp at 10, 15 and 20 cm gives about 1.69, 1.38 and 1.19 seconds; the seven times have median 1.45 and mean 3.42, and without the two oddities median 1.42; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 ramp, table and stopwatch; at 680x425 table as a tab.
2. Seven runs are timed by the child and their spread described. (E3-DAT-DI-10)
3. Two outliers are found, their causes named, and the middle compared. (E4-DAT-DI-10)
4. Height and surface are varied and their joint effect described from the chart. (E5-DAT-DI-10)
5. Filled runs are labeled simulated and match the rolling-ball model.
6. `Read` reads every row and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: start and finish cues still work; no network requests.

## Open questions
None.
