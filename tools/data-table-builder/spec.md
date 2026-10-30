# Data Table Builder

## One idea
The class builds its own table on the board (choose the columns, decide whether each answer is a pick from a list, a number or a yes or no, then add one row per student) and the computer turns the same rows into a bar graph, a dot plot or a sorted list in one tap, so the class sees that the question decides which column to look at and the kind of column decides which chart can count it.

## Not like
- me-vs-the-counter (K, CS): a sensor counts bounces and the class races it. Here nothing is measured by a machine; the class designs the table's columns and fills its rows, and the computer's job is to sort, count and chart.
- class-poll (1, math) and lunch-line-data (2, math): one vote or a given data set turned into a picture or bar graph. Here the class decides the columns and their kinds first, and one table holds several questions at once.
- score-keeper (3) and code-tracer (4): variables changing inside a program. Here the data sits still in rows and columns; nothing runs.
- biased-bot (4): a bar chart per room shows a robot's mistakes. Here the charts show the class itself, and nobody is wrong.
- simulation-studio (9-12, same family and group): cleans a real messy log after the fact. Here messy data is prevented up front by giving each column a kind; there is no cleaning step.

## Who and how
- Grade 4, computer science. Module: Tables and Visualizations (Data and Analysis), "Organize data into rows and columns and chart it". Topic line: "rows, columns and charts from our own class data".
- Driver: students or teacher. Best on a projector: the teacher sets up columns with the class, students walk up one at a time to add their row (or call answers out while the teacher taps), then the class answers question cards together. Pairs on laptops can explore the Sample class alone.
- 20 to 35 minutes (columns 5, rows 10 to 15, questions 10).
- Standards (CSTA 2026 ids from the module): E4-DAT-DC-09, E4-DAT-DI-10. 2017 crosswalk: 1B-DA-06 (organize and present collected data visually to highlight relationships and support a claim), 1B-DA-07 (use data to highlight or propose cause and effect relationships, predict outcomes or communicate an idea). Math link for the teacher: 3.MD.B.3 (bar graphs), 4.MD.B.4 (line plots).
- tool.json: driver "students or teacher", minutes "20-35", modes ["Sample class", "Our class"], grades_label "Grade 4".

## Screens and modes
Kit frame (own `:root`, a classroom chalkboard). Header: title "Data Table Builder", small line "Rows, columns, charts"; mode buttons "Sample class" (open book icon) and "Our class" (chalk icon); Motion, Sound, Read.

Layout (both modes): stage on the left split in two: the table on top (about 45 percent), the chart below (about 55 percent, the larger part, since the chart is what answers the question). Panel on the right with `#hint`, then sections "Chart", "Questions" and the mode's own section. Targets at least 48 px (projector use).

The table (engine `renderTable`): one column per field, header shows the column name, a kind badge (List, Number, Yes/No, each with an icon: bullet list, hash, check) and a sort button (arrow; tap toggles up, down, off). Row label is the row number ("Row 7"). Tapping a column header selects it for the chart (outlined in the accent). A footer line under the table: "24 rows, 5 columns".

Chart section (panel): three buttons "Bar graph" (bars icon), "Dot plot" (stacked dots icon), "Sorted list" (lines icon); a "Split by" picker listing the List and Yes/No columns plus "No split" (default). The chart draws whatever is selected; it never refuses.

Questions section: question cards for the current table, one at a time with "Previous" and "Next" arrows. Each card: the question, a "Guess first" row (the choices for a List or Yes/No answer, or a number stepper; the teacher taps the class's guess), "Show me" (reveals the chart), and once shown, the answer sentence and "Our guess was" line. A card counts as answered when the selected column (and split) is the one the card needs; the card then shows a check and "Best chart: Bar graph, because each bar is one choice" (or the card's own reason).

### Mode 1: Sample class (opens first)
Focus: the chart of the selected column, the largest thing on the stage, with that column outlined in chalk yellow
in the table right above it, so the eye goes from the column to its chart; the open question card in the panel names
what to look for.
The made-up Room 4 table below, already filled (24 rows, 5 columns). Everything is open to explore: sort, select columns, switch charts, split. Editing cells is off here ("This is a sample. Switch to Our class to make your own." under the table). Six question cards.

### Mode 2: Our class
Focus: while a row is being added, the entry card at the stage center (it covers the chart, never the table's new
row); after Done, the new row flashes in the table and the chart grows below it; with 3 or more rows, the chart as in
Sample class.
Starts empty with a short card: "1 Choose columns. 2 Add rows. 3 Ask questions." Panel section "Build":
- "Add a column" opens a shelf of ready columns (cards, below) plus "Make my own column". Up to 6 columns. Each column header gets an "x" (remove, with "Remove this column and its answers?" Yes / No).
- "Make my own column": a name box (up to 24 characters), a kind picker (List, Number, Yes/No), then for List: up to 6 choices (each up to 14 characters, "Add a choice"), for Number: smallest and biggest allowed (0 to 100). A line under the kind picker: "Answers come from buttons, so the computer can count them exactly." "Save column" adds it.
- "Add my row" (big button, enabled once there is a column) opens an entry card over the stage: one control per column (List: one button per choice with its text; Number: big minus and plus around the value, which can also be typed; Yes/No: two buttons with check and cross icons). "Done" adds the row (disabled until every column has an answer), "Cancel" closes. Up to 40 rows.
- Cells are editable in the table (click or Enter): List and Yes/No open the same buttons; Number opens the stepper. A row has a delete button at its end (trash icon, confirm).
- Question cards in Our class: one card per column, written from the column (List: "Which [column] is most common in our class?"; Number: "What is a typical [column] in our class?"; Yes/No: "Did more of us say yes or no to [column]?"), plus "Your own question" (a free text box the teacher types, up to 80 characters, then taps the column that answers it).
- Saved on this device automatically (localStorage key `dtb-our-class`): columns and rows only, no names. "Clear our class" (eraser icon) asks "Erase every column and row on this device?" Yes / No.

## Content
Sample class "Room 4" (made up for practice; a line under the table says so). Columns:
- Favorite fruit (List: Apple, Banana, Grapes, Orange, Strawberry; chalk icons from the icon kit in Art)
- Teeth lost (Number, 0 to 20)
- Can you whistle? (Yes/No)
- Way to school today (List: Walk, Bus, Car, Bike)
- Pockets today (Number, 0 to 12)

| Row | Fruit | Teeth | Whistle | Way | Pockets |
|---|---|---|---|---|---|
| 1 | Apple | 8 | Yes | Car | 2 |
| 2 | Strawberry | 9 | Yes | Bus | 3 |
| 3 | Banana | 7 | No | Walk | 1 |
| 4 | Apple | 10 | Yes | Car | 4 |
| 5 | Grapes | 8 | No | Bus | 2 |
| 6 | Strawberry | 6 | Yes | Car | 0 |
| 7 | Apple | 11 | Yes | Bus | 2 |
| 8 | Orange | 8 | No | Walk | 5 |
| 9 | Apple | 9 | Yes | Car | 3 |
| 10 | Strawberry | 5 | Yes | Bus | 2 |
| 11 | Banana | 8 | No | Bus | 1 |
| 12 | Grapes | 10 | Yes | Car | 2 |
| 13 | Apple | 7 | Yes | Walk | 6 |
| 14 | Strawberry | 9 | No | Car | 2 |
| 15 | Grapes | 8 | Yes | Bus | 3 |
| 16 | Banana | 12 | Yes | Car | 0 |
| 17 | Apple | 6 | No | Bus | 2 |
| 18 | Orange | 8 | Yes | Walk | 4 |
| 19 | Strawberry | 10 | No | Car | 1 |
| 20 | Apple | 9 | Yes | Car | 2 |
| 21 | Banana | 7 | Yes | Bus | 3 |
| 22 | Strawberry | 8 | No | Walk | 2 |
| 23 | Grapes | 4 | Yes | Bike | 1 |
| 24 | Apple | 9 | Yes | Bike | 3 |

Checked counts: Fruit Apple 8, Strawberry 6, Banana 4, Grapes 4, Orange 2. Teeth: 4 (1), 5 (1), 6 (2), 7 (3), 8 (7), 9 (5), 10 (3), 11 (1), 12 (1); most often 8, smallest 4, biggest 12. Whistle Yes 16, No 8. Way Car 9, Bus 8, Walk 5, Bike 2. Pockets: 0 (2), 1 (4), 2 (9), 3 (5), 4 (2), 5 (1), 6 (1); total 56. Whistle split by Way: Car 7 yes 2 no; Bus 5 yes 3 no; Walk 2 yes 3 no; Bike 2 yes 0 no.

Sample question cards (column; best chart; answer sentence):
1. "Which fruit does Room 4 like best?" (Favorite fruit; Bar graph, "each bar is one choice") "Apple: 8 of 24."
2. "How many teeth has a Room 4 kid lost?" (Teeth lost; Dot plot, "each dot sits at its number, so you see where most are") "Most often 8. From 4 to 12."
3. "Can more of us whistle, or not?" (Can you whistle?; Bar graph) "Yes 16, No 8. Twice as many can."
4. "How did most of us get to school today?" (Way to school today; Bar graph) "Car 9, Bus 8, Walk 5, Bike 2."
5. "How many pockets is Room 4 wearing in all?" (Pockets today; Sorted list, "the computer adds the column for you") "56 pockets."
6. "Do car riders whistle more than bus riders?" (Can you whistle? split by Way to school today; Bar graph) "Car riders: 7 yes, 2 no. Bus riders: 5 yes, 3 no."

Ready column shelf for Our class (name; kind; choices or range; icon):
- Favorite fruit; List; Apple, Banana, Grapes, Orange, Strawberry
- Favorite season; List; Winter, Spring, Summer, Fall
- Way to school today; List; Walk, Bus, Car, Bike, Other
- Can you whistle?; Yes/No
- Have you ever been on a boat?; Yes/No
- Teeth lost; Number; 0 to 20
- Pockets today; Number; 0 to 12
- Letters in my first name; Number; 1 to 15 (only the count is entered)
- Jumping jacks in 10 seconds; Number; 0 to 30 (the class times it together)

Answer sentences (all modes, computed): Bar graph: "[Top choice]: [n] of [rows]." (a tie: "[A] and [B] tie with [n].", three or more: "[A], [B] and [C] tie with [n]."); Dot plot on a Number column: "Most often [m]. From [min] to [max]." (several modes: "Most often [a] and [b]."); Sorted list on a Number column: "Total: [sum]." and "Biggest: [max]. Smallest: [min]."; Yes/No: "Yes [y], No [n]." Readouts never use averages (grade 4).

Fact line (Sample class, small, under the table): "Kids have 20 baby teeth. Most lose them between about age 6 and age 12."

## Interactions in detail
- Selecting a column header or a chart button redraws the chart in under 100 ms; bars grow and dots drop in over 300 ms (instant with Motion off). A tap during that growth acts at once: the new chart replaces the growing one from its first frame.
- Bar graph: List and Yes/No columns get one bar per choice in the column's own order (not sorted), choices with 0 still shown as an empty slot labeled 0. A Number column gets one bar per whole number from the smallest to the biggest value in the data, with numbers nobody has shown as 0. Bars have the count printed on top.
- Dot plot: Number columns sit on a number line from the column's smallest to biggest value in the data (at least 5 ticks wide), one dot per row stacked. List and Yes/No columns get one stack per choice. With more than 12 dots in a stack, dots shrink so the tallest stack fits.
- Sorted list: rows listed by the selected column (biggest first for numbers, choice order for lists) with the row number; for Number columns the total and biggest and smallest lines.
- Split by: Bar graph draws side-by-side bars per group with a legend (color plus pattern: solid, stripes, dots, cross-hatch, plus the group name on each bar group). Dot plot splits into one row per group. Splitting a column by itself is not offered.
- Tapping a bar or a dot stack highlights those rows in the table (and scrolls the table panel, `preventScroll` on focus).
- Sorting the table never changes the chart; it changes the row order only. Row numbers stay with their rows.
- Our class with no rows: the chart area says "No rows yet. Tap Add my row." Question cards are disabled until a column has 3 rows.
- Removing a column removes its question card; a selected column that is removed resets the chart to the first column.
- Mode switch keeps each mode's state (selected column, chart, card). Sample class has no Reset; Our class has "Clear our class" only.
- Keyboard: panel before stage; table cells reachable with arrows; Enter edits; Escape closes the entry card. Visible focus everywhere.
- Sizes: the chart buttons, "Add my row" and the selected chart visible without scrolling at 1280x720, 1366x768 and 680x425 (the table scrolls inside its own box, at least 6 rows visible). At 760 wide and below, table above chart above panel, with "Add my row" pinned at the bottom of the screen in Our class.

## Look
- Accent `--brand #ffd84d` (chalk yellow): header rule, selected column outline, pressed chart button. `--brand-ink #1d1a05`.
- Own `:root` (a green chalkboard): `--paper #1d3a2f`, `--panel #24463a`, `--ink #f4f1e8` (chalk white), `--muted #b9c9bf`, `--line #3d5f52`, `--btn #2c5546`, `--head-ink #f4f1e8`, `--focus #7fd4ff`. A faint chalk-dust texture drawn in CSS (no image). Table lines look hand-ruled (1.5 px, slightly uneven dash in CSS).
- Chart series (`--dd-1` to `--dd-6`, chalk colors, always with a shape or pattern too): #8fd3ff circle, #ffb38a square, #c8f08f triangle, #f7a8d8 diamond, #d0c2ff star, #f2e6a0 ring.
- Neighbors: code-tracer rust on cream, score-keeper raspberry on navy, biased-bot mustard on cream, network-help-desk green on mint, me-vs-the-counter gym orange on cream. A dark chalkboard with yellow chalk is unlike all of them and unlike its group siblings.
- Contrast: ink on paper 10.95:1, ink on panel 9.24:1, muted on panel 6.05:1, brand on paper 8.94:1, brand on panel 7.54:1, brand-ink on brand 12.63:1, focus on paper 7.51:1; series on paper 7.61, 7.10, 9.61, 6.80, 7.56, 9.77:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`); no people. Mostly a table and charts (drawn in code), so the only painted pieces are
the answer icons the class sees on the entry card buttons, the chart labels and the column shelf.
- Chalk icon kit (13 pieces, one prompt: "A simple [object] drawn in soft colored chalk on a dark green chalkboard,
  centered, hand-drawn chalk texture"); 1:1; cutout yes (the chalkboard knocked out, chalk strokes kept); people no;
  shown at 28 to 48 px beside a choice's word on the entry card buttons, the bar graph's axis, dot plot stacks, the
  sorted list and the column shelf; always with the word, never alone: icon-apple, icon-banana, icon-grapes,
  icon-orange, icon-strawberry, icon-walk (a pair of sneakers), icon-bus (a yellow school bus), icon-car, icon-bike,
  icon-winter (a snowflake), icon-spring (a tulip), icon-summer (a sun), icon-fall (an orange leaf).
"Other", Yes and No, kind badges, the chalkboard (CSS chalk-dust texture), table, charts, legends and preview.svg (the
chalkboard table with a yellow-outlined Fruit column and its bar graph below, with the fruit icons) are drawn in code;
the teacher's own column choices have no icon. 13 images, 0 with people.

## Voice
Bank voice `knowing-guide` (Sadaltager), "Say in a knowledgeable, friendly way, like a museum curator": a curator who treats the class's table as a collection worth labeling well. Not used by any CS neighbor (me-vs-the-counter easy-coach, code-tracer clear-teacher, score-keeper friendly-dad, biased-bot news-reader, network-help-desk upbeat-guide, game-remix big-sister) or a group sibling. Rows, cells and answer sentences are read on screen; Read speaks the hint.
`Curio.voice`, `scope: () => state.mode`.
How (spoken the first time its moment comes, then hint only):
1. w-sample (Sample class entered; stale on the first column tap): "This is Room 4's table. Each row is one student.
   Each column is one question. Tap a column name to chart it."
2. charts (first column charted; stale on a chart button): "Same rows, new chart. Tap Bar graph, Dot plot or Sorted
   list."
3. split (first Split by choice; stale on the next chart change): "Now the chart splits into groups, so you can compare
   them."
4. card (first question card shown; stale on Show me): "Guess first and tap the class's guess. Then tap the column
   that answers the question, and press Show me."
6. w-ours (Our class entered with no columns; stale on Add a column): "Let's build our own table. Tap Add a column to
   choose what to ask."
7. kinds (first column saved; stale on Add my row): "Each column has a kind: a list, a number, or yes or no. Add more
   columns, or tap Add my row."
8. entry (first entry card opened; stale on Done or Cancel): "Tap one answer for each column. Then tap Done."
10. counted (rows reach 3 for the first time; stale on a column tap): "Now the computer can count. Tap a column name
    and pick a chart."
Events (every time; stale as noted):
5. A Sample card answered: its answer sentence, six fixed lines: "Apple: 8 of 24." "Most often 8. From 4 to 12." "Yes
   16, No 8. Twice as many can." "Car 9, Bus 8, Walk 5, Bike 2." "56 pockets." "Car riders: 7 yes, 2 no. Bus riders: 5
   yes, 3 no." Stale when the card or column changes.
9. A row added: "Row 1 added." through "Row 40 added." (forty fixed lines). Stale after 3 seconds or on the next tap.
11. An Our class card answered: "That column answers it. Look at the chart and say what it shows." Stale when the card
    changes.
Which line when: each line is queued at the moment named above; 5 and 11 follow Show me.

## Family engine
data-desk (`kit/data-desk.js`, docs/families/data-desk.md). Uses `DataTable` (the sample rows, or the class rows), `renderTable` (editable in Our class), `t.on('change')` so the chart follows every new row, and `Chart` types `bar` and `dot` with `x` and `groupBy`. This tool needs three engine additions (add them to the engine and the family doc in the same change, keeping existing calls working): column `kind: 'number' | 'list' | 'yesno'` with `choices` for lists; `bar` and `dot` with only `x` set count rows per value (empty choices drawn as 0); `t.stats(key).sum` and `t.counts(key)` (count per choice). The sorted list, question cards, entry card and column shelf stay in this tool.
Dataset: the made-up Room 4 sample (no other sibling uses it). Family data rule note: the real data in this tool is the class's own; the sample is labeled made up.

## Sources
- Baby teeth: children have 20 primary teeth, which fall out from about age 6 to age 12: American Dental Association, MouthHealthy, "Eruption Charts": https://www.mouthhealthy.org/all-topics-a-z/eruption-charts
- Rows as records and columns as fields; organizing data for a computer to count: Code.org CS Fundamentals, "Data" lessons, and CSTA K-12 Computer Science Standards (2017) 1B-DA-06 and 1B-DA-07: https://csteachers.org/k12standards/
- Bar graphs and line plots at grades 3 and 4: Common Core State Standards for Mathematics 3.MD.B.3 and 4.MD.B.4: https://www.thecorestandards.org/Math/
- Room 4 and its answers are made up; every count above was computed from the table.
- Checks run (Python, 2026-10-29, on the 24 rows above): Fruit Apple 8, Strawberry 6, Banana 4, Grapes 4, Orange 2;
  Teeth counts 4:1, 5:1, 6:2, 7:3, 8:7, 9:5, 10:3, 11:1, 12:1 (most often 8, from 4 to 12); Whistle Yes 16, No 8 (16
  is twice 8); Way Car 9, Bus 8, Walk 5, Bike 2; Pockets 0:2, 1:4, 2:9, 3:5, 4:2, 5:1, 6:1, total 56; Whistle by Way
  Car 7 and 2, Bus 5 and 3, Walk 2 and 3, Bike 2 and 0. All match the spec. Every contrast ratio in Look recomputed
  with the WCAG 2.1 formula and matches.

## Done when
1. Sample class opens with 24 rows and 5 columns; tapping Favorite fruit and Bar graph shows Apple 8, Strawberry 6, Banana 4, Grapes 4, Orange 2 in choice order.
2. Teeth lost as a Dot plot runs 4 to 12 with the tallest stack (7) at 8, and the sentence "Most often 8. From 4 to 12."
3. Card 5 answered with Pockets today shows "56 pockets."; card 6 with Whistle split by Way shows Car 7 and 2, Bus 5 and 3.
4. In Our class, adding Favorite season and Teeth lost, then three rows, enables the cards; a fourth row updates the open chart without a tap.
5. "Done" stays disabled until every column in the entry card has an answer; removing a column removes its card.
6. Reloading the page keeps Our class; "Clear our class" then Yes empties it and the saved key.
7. Lines 2, 4 and 7 are each spoken once in a run of five chart or card actions; line 9 after every row; no line names a disabled control.
8. Chart buttons, "Add my row" and the chart are visible without scrolling at 1366x768 and 680x425; series are told apart in grayscale by shape and pattern.
9. Motion off: bars and dots appear at once; counts are identical.
10. Focus: at 1366x768 and 680x425 the chart is the largest thing on the stage, right under its outlined column; in
    Our class the entry card never hides the table's newest row.
11. Tap while it plays: a chart button or column tap while bars are growing shows the new chart at once, with no stale
    line.

## Open questions
- The family rule asks for real data with a source. Here the real data is the class's own, and the practice table (Room 4) is made up and labeled so. Keep the made-up sample, or replace it with a small real public table?
