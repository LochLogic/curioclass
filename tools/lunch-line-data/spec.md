# Lunch Line Data

## One idea
The school cook, Mrs. Lin (made up, labeled "illustration"), needs to plan next week's menu, so the child turns a stack of lunch-choice cards (made-up data, labeled as made up for the lesson) into a picture graph and then a bar graph with up to four choices, dragging each bar to its height, and answers questions (How many chose tacos? How many in all? How many more chose tacos than soup?); then a crate of 12 carrots from the school garden comes in, and the child measures each carrot to the nearest inch with an on-screen ruler and stacks an X above its length on a line plot, then answers "Which length is most common?" and "How many carrots are 6 inches or longer?"; at the end the bar graph and the line plot sit side by side and the child sorts new questions to the right graph, seeing that choices go in a bar graph and measurements go on a line plot, so a second grader learns to measure lengths to the nearest whole unit and show them on a line plot, and to draw picture and bar graphs with up to four categories and solve put-together, take-apart and compare problems using the graphs.

## Not like
- class-poll (1, spec): tallies and picture graphs with up to three choices, same family. Here bar graphs, four choices and line plots.
- graph-glow-up (3, concept): scaled graphs. Here one square per vote.
- estimation-station (2, spec): measuring and estimating. Here measuring to build a line plot.
- garden-grid (2, spec): rows and columns of plots. Here data from the garden.

## Who and how
- Grade 2, Math, module "Line Plots and Bar Graphs". Standards: 2.MD.9 (generate measurement data by measuring lengths of several objects to the nearest whole unit, or by making repeated measurements of the same object; show the measurements by making a line plot, where the horizontal scale is marked off in whole-number units), 2.MD.10 (draw a picture graph and a bar graph (with single-unit scale) to represent a data set with up to four categories; solve simple put-together, take-apart, and compare problems using information presented in a bar graph).
- Format: data. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Three lunch polls (four choices each), a picture graph and a bar graph for each, nine graph questions, two carrot crates of 12, a line plot for each, six line plot questions, the sort-the-question finale. Extra: Measure the room (enter lengths of real classroom things for a line plot; nothing leaves the device). tool.json `modes: ["Cafeteria", "Measure the room"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.MD.10 (draw) | Build picture and bar graphs from cards | pictures stacking; bars rising | 2 |
| 2.MD.10 (solve) | Answer total, part and compare questions | the bars lined up | 3 |
| 2.MD.9 | Measure carrots and stack Xs on a line plot | the ruler; the plot growing | 4 |

## Screens and modes
Header (kit): title "Lunch Line Data"; `Cafeteria`, `Measure the room`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A cafeteria counter with trays, a stack of lunch cards and Mrs. Lin in an apron. A small tag reads "Made-up data for practice." The welcome is queued (`welcomeAfter: true`): "Hi! I need to know what to cook next week. Can you graph what kids chose? Drag the first card to its row." First hint: "Drag a lunch card to its row."

**Graphs (focus: the graph).** At 1366x768 the cards sit at the left and the graph fills the right; at 680x425 the cards are a strip above the graph. First a picture graph (one picture per card), then `Make bars` turns it into a bar graph grid with a scale of one, and the child drags each bar to its height.

**Questions.** "How many chose tacos?" "How many in all?" "How many more chose tacos than soup?" The bars slide side by side for compare questions and the difference glows.

**Carrot crates.** Twelve garden carrots on a cutting board and a ruler in inches. The child drags the ruler to each carrot (the end lines up at 0) and taps the nearest inch. An X stacks above that number on the line plot.

**Which graph? (the aha).** The bar graph and the line plot side by side. Question cards ("How many chose pizza?", "How long are most carrots?") get dragged to the right graph. Mrs. Lin: "Choices go in a bar graph. Measurements go on a line plot."

**The end.** The menu plan and the carrot report. `Print` prints both graphs.

**Measure the room (extra).** The class measures real things and enters lengths; the line plot builds.

## Content
- Three polls with four choices each (made-up data, labeled), two carrot crates of 12 with lengths from 4 to 9 inches, all spoken.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Bars and Xs can be moved until `Check`.
- Keyboard: Tab to cards, bars, the ruler, the plot and answers; arrows move a bar or the ruler; Enter places.
- With Motion off bars and Xs jump into place.

## Look
- Accent `--brand` #8a3a12 cafeteria brick (header, bars, buttons); gold #f4c542 (the compare difference, the item in hand); paper #fcf3ee; ink #281005; muted #5e5049.
- Contrast (WCAG 2.1, computed): white on brand 7.79:1; brand on paper 7.12:1; ink on paper 16.45:1; muted on paper 7.06:1; ink on gold 11.07:1.
- Never color alone: bars carry labels and numbers; Xs are marks, not colors.
- Different from this batch (garden green, mystery violet, terracotta brown, lake teal).

## Art
- People (illustrated): Mrs. Lin, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the cafeteria (1, 16:9), four lunch pictures (4, 1:1), a carrot crate (1, 1:1).
- Drawn in code: graphs, the ruler, carrots at true lengths, the line plot.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the narrator; `bright-teacher` as Mrs. Lin and the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.task + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `card`: "Drag a lunch card to its row."
- how `bar`: "Drag the bar to its height."
- how `ask`: "Tap the answer."
- how `measure`: "Drag the ruler to the carrot, then tap the nearest inch."
- how `sort`: "Drag the question to its graph."
- event, whole, which graph.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
class-poll (family "class-poll"). Uses the shared pieces from the marked block `/* CLASS-POLL ENGINE: begin */ ... /* end */` as described in class-poll's spec: the category graph (here drawn as bars too) and how-many-more line-ups. Tool-only code: the ruler, carrot measuring, the line plot.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Bars | Drag bars to any height | `Check` compares with the cards and shows the first wrong bar. |
| Measure | Tap any inch | The ruler shows the end; a wrong tap highlights the nearest mark. |
| Sort | Drop questions anywhere | Each card bounces back with a reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `card`; `bar`.
2. `ask`.
3. `measure`.
4. Which graph (whole), waits. `sort`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.MD.9, 2.MD.10 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Bar graphs fit categories; line plots fit measurements | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data; Grades 2-5 Measurement Data" | National Council of Teachers of Mathematics, "Principles and Standards", grades 3 to 5 data analysis | yes |
| Measuring from 0, not from 1 or the ruler's edge, is a common grade 2 error | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-10): 9 + 4 + 7 + 3 = 23 lunches and tacos beat soup by 5; the 12 carrots (4 to 9 inches) have 7 most common and 9 at 6 inches or longer; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cards and graph; at 680x425 strip over graph.
2. Picture and bar graphs with four choices are built. (2.MD.10)
3. Nine total, part and compare questions are answered from the bars. (2.MD.10)
4. Two crates of carrots are measured to the nearest inch and plotted. (2.MD.9)
5. Every card is spoken; every control is 56 px or more.
6. Data is labeled made up; Mrs. Lin is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
