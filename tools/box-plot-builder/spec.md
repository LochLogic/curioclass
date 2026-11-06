# Box Plot Builder

## One idea
Drag one real day or one real game along a dot plot and watch the two centers part ways: the Mean marker chases the
dot while the Median marker stays put (until the dot crosses the middle), so the shape of the data decides which
summary tells the truth, and then you prove it by building Sam's box plot and report by hand from the same real data.

## Not like
- question-lab (gr 6, sort, concept): which questions are statistical, plus center and spread of a simulated class seen loosely. Here no question sorting; real NOAA and NBA data, the five-number summary built card by card, mean and MAD computed, and the measure chosen by shape.
- data-table-builder (gr 4, data-desk, spec): the class collects its own data and picks a chart for a question. Here the data are given and real; one numeric column; the work is center, spread and shape, not table design.
- data-desk-distributions (gr 12, data-desk, spec): describes whole distributions with evidence chips, SD, z-scores and the normal model. Here grade 6 measures only (median, mean, IQR, MAD), whiskers to min and max, and the drag that moves a center.
- data-detective (gr 8, data-desk, concept): paired data, scatter plots, lines of fit. Here one variable only.
- lunch-survey-cleanup (gr 6-8, data-desk, concept): fixing messy rows. Here the data are clean; the question is which summary to print.
- seed-sprout-data (gr 5, lab, concept): line plots of measurements in fractions. Here grade 6 summaries of a distribution.
- Datasets: none shared with siblings (simulation-studio has Old Faithful; data-desk-distributions has presidents, statehood and World Bank). This tool claims NOAA daily highs (San Diego Sept 2024, Chicago O'Hare May 2024, Miami and Denver July 2024) and Luka Doncic's 2023-24 game log.

## Who and how
- Grade 6, math, module Summarizing Data. Driver: students (solo by default; a teacher can project Explore for a class talk). 25 to 40 minutes (Explore 8, Build 15 to 20 for one data set, Headline 7).
- Standard on the module: 6.SP.B (6.SP.4 and 6.SP.5a to 5d, all taught below).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Explore", "Build", "Headline"], grades_label "Grade 6".
- No personal prompts. The optional "Our class" set in Explore stores numbers only, on this device, and says so on screen (BASELINE rule 7).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.SP.4 (dot plot, histogram, box plot) | In Explore, switch Dot plot and Histogram over the same data, change the bin width; in Build, line the values up and tap the five cards that make the box | the same days as stacked dots, as bars, and as the box strip under both; their own box assembling from their five picks | Done 2, 4 |
| 6.SP.5a (number of observations) | Build step 1: work out n from the data card (a date range, or 82 team games minus 12 missed) and type it | the NOAA or box-score card in its own codes, no count printed anywhere | Done 3 |
| 6.SP.5b (attribute, how measured, units) | Build step 1: translate the card's codes (TMAX, PTS, °F) into plain words, one pick per row | three chip rows under the card | Done 3 |
| 6.SP.5c (median, mean, IQR, MAD; striking departures) | Build steps 2 to 4: tap the middle, quartile and end cards; type the IQR; divide the shown total for the mean; divide the shown sum of distances for the MAD; Luka's set asks why one game stands apart | ordered card grid, the box, distance lines to the mean on the dot plot | Done 4, 5 |
| 6.SP.5d (choose measures by shape and context) | Explore: drag and watch which center moves; Build step 5: pick the pair (Median and IQR, or Mean and MAD) and the reason; Headline: two cities with one mean, pick the headline that tells the whole story | the Mean and Median markers parting; "21 of 30 days were cooler than the mean"; two box plots, one wide, one narrow | Done 1, 6, 7 |

## Screens and modes
Kit frame with the tool's own `:root` (newsprint, below). Header: "Box Plot Builder", small line "What's a typical day?";
mode buttons `Explore` (dots icon), `Build` (box plot icon), `Headline` (newspaper icon); Motion, Sound, Read.
Layout at 1366x768 in every mode: stage left (about 66 percent), panel right (about 34 percent). The panel top is
Sam's strip: Sam's cutout (96 px tall) beside a speech bubble that holds the current hint (`#hint`). Everything a mode
needs sits above the fold at 1366x768, 1280x720 and 1000x625. At 680x425 and 800x500 the stage and panel stay side by
side; Sam's cutout folds away (the bubble stays as plain hint text), set cards become text chips, and the stage keeps
at least 60 percent of the width.

On load: Explore, San Diego September 2024, Dot plot view. Nothing plays before the first tap. Sam's bubble reads:
"What's a typical day here? Drag any dot along the line and watch the Mean and Median markers." The first tap on a dot
starts dragging it (the main path); a first tap anywhere else does that control's job at once (BASELINE rule 16).

### Explore (opens first)
Focus: the dot plot, the biggest thing on the stage (about 70 percent of the stage height), with the box strip under it
on the same fixed axis. Two markers ride above the plot: Mean (rust dashed line, diamond flag reading "Mean") and Median
(teal solid line, square flag reading "Median"). Flags carry words, never values.
- Panel, top to bottom: Sam's strip; set cards (San Diego Sept 2024, Chicago May 2024, Miami July 2024, Denver July
  2024, Luka Doncic 2023-24, Our class); view buttons `Dot plot` and `Histogram`; `Bins -` and `Bins +` (shown in
  Histogram view); four readout tiles headed "Since the real data": Mean moved, Median moved, IQR changed, MAD
  changed (signed, hundredths trimmed, with the unit: "+0.53 °F", "0 °F"); `Put back` (disabled until a dot moved).
- Drag: any dot on the dot plot, pointer or keys (engine drag, whole-number snap), clamped to the axis. A moved dot is
  drawn hollow with the ring color and keeps its ring. After the first move, faint ghost lines mark where Mean and
  Median started ("start"), and a thin arrow shows how far each traveled.
- Histogram view: the same data in bins (start 60 °F for temperatures, 0 for points); markers stay; dragging is off
  and the hint says "Tap Dot plot to drag a dot."
- What the picture shows for each outcome: a dot dragged outward on one side: Mean flag slides, Median flag still,
  Median tile "0"; a dot dragged across the middle: both flags move, Median tile non-zero; Put back: every dot home,
  ghosts gone, tiles at 0.
- Our class card: a box "Type up to 60 numbers, separated by spaces or commas", a unit box (12 characters), `Show`.
  A line under it: "These numbers stay on this device. Nothing is sent anywhere." Saved in localStorage
  `curio-bpb-class` (try/catch) with `Clear`. Axis: data min and max padded by half the range, nice ticks.

### Build
Focus: the card grid while steps 2 to 4 run (center of the stage), the dot plot with distance lines in step 4; the
dot plot shrinks to about 30 percent of the stage height above the grid. Box strip hidden until the student's box is
built. Mean and Median markers hidden in Build.
- Set picker in the panel: San Diego, Chicago, Luka (three cards; progress kept per set for the session; `Start over`
  clears the current set's build).
- A five-step bar in the panel: 1 Facts, 2 Box plot, 3 Mean, 4 MAD, 5 Pick. The current step's controls sit under it.
- Step 1 Facts: the data card (Content) in a newsprint box at the top of the panel. "How many values?" number box and
  `Check`. Then three chip rows, one pick each: What was measured, How it was measured, Units.
- Step 2 Box plot: `Line up` sorts the dots into a grid of cards, 10 per row, smallest first, each card showing its
  value (64 x 44 px; Luka's 70 cards make 7 rows). Then in order: tap the middle card (two cards when n is even);
  the grid splits into a lower and an upper half (median card set aside when n is odd); tap the middle card of each
  half; tap the smallest and largest card. Each correct pick drops a labeled tick (Min, Q1, Median, Q3, Max) onto the
  box axis; after the fifth, the box and whiskers draw between them. Then "Type the IQR" box and `Check`.
- Step 3 Mean: a line "The 30 highs add up to 2,321 °F." (per set) and "Type the mean, to the tenths place" + `Check`.
- Step 4 MAD: the dot plot grows back; the mean line appears; each dot gets a horizontal line to it, drawn left to
  right in under 900 ms, with a counter "Distances so far: ..." ending at the total (Content). Type the MAD + `Check`.
- Step 5 Pick: "Sam can print one center and one spread." Two buttons `Median and IQR`, `Mean and MAD`; then three
  reason chips. One pick each. Then `File the report`.
- Report card (stage, over the grid): Sam's short article built from the student's values, each value with a mark:
  check "found" (first or second try), or "Sam showed" / "Sam fixed". A line "You found 12 of 14 on your own." (14 fields: n, measured, how, units, the five cards, IQR, mean, MAD, pair, reason). No
  other score, no celebration beyond Curio.yes() once.

### Headline
Focus: the two box plots, stacked on one shared axis (75 to 105 °F, a tick every 1 °F, labels every 5), each with its
dot plot above it, Miami on top, Denver below; the box plots are the largest marks on the stage.
- Above them, Sam's draft headline in newsprint type: "Miami and Denver had the same July: average high 91.7 °F."
  and an editor's note "Is that the whole story?"
- Panel step A: "Read each box plot. Type each city's IQR." Two boxes (Miami IQR, Denver IQR) and `Check`.
- Panel step B: four headline buttons (Content), shuffled on each visit, one pick. The verdict and its reason show
  under the picked button; the right headline then prints on the front page with both IQRs and both ranges.
- No readout of any statistic in this mode.

## Content
Daily highs (°F), in date order. Sources and checks in Sources.
- San Diego International Airport, September 1 to 30, 2024 (n 30): 75, 78, 81, 82, 89, 86, 90, 94, 93, 83, 74, 75, 75,
  76, 72, 74, 73, 73, 74, 74, 74, 75, 74, 74, 72, 73, 72, 71, 72, 73. Sorted: 71, 72 x4, 73 x4, 74 x7, 75 x4, 76, 78,
  81, 82, 83, 86, 89, 90, 93, 94. Median 74 (cards 15 and 16, both 74), Q1 73 (card 8), Q3 81 (card 23), min 71, max
  94, IQR 8, range 23, sum 2,321, mean 77.37 (77.4), sum of distances 159.4, MAD 5.31 (5.3). 21 of 30 days below the
  mean. Hot spell September 5 to 9: 89, 86, 90, 94, 93. Shape: lopsided, long high tail.
  Card: "Station: SAN DIEGO INTERNATIONAL AIRPORT, CA US. Element: TMAX (maximum temperature). Unit: °F. Dates:
  2024-09-01 to 2024-09-30. Source: NOAA NCEI, GHCN-Daily."
- Chicago O'Hare International Airport, May 1 to 31, 2024 (n 31): 75, 81, 69, 81, 64, 70, 75, 79, 63, 67, 70, 83, 81,
  62, 67, 75, 81, 85, 76, 86, 89, 80, 81, 77, 76, 73, 74, 72, 70, 70, 79. Median 75 (card 16), Q1 70 (card 8), Q3 81
  (card 24), min 62, max 89, IQR 11, sum 2,331, mean 75.19 (75.2), sum of distances 174.2, MAD 5.62 (5.6). 16 below
  the mean, 15 above. Shape: roughly balanced. Card as above with "CHICAGO OHARE INTERNATIONAL AIRPORT, IL US" and
  2024-05-01 to 2024-05-31.
- Miami International Airport, July 1 to 31, 2024 (n 31): 88, 92, 91, 92, 93, 91, 93, 92, 92, 92, 91, 90, 91, 92, 89,
  91, 92, 92, 93, 92, 93, 90, 92, 92, 91, 92, 93, 93, 93, 92, 92. Min 88, Q1 91, median 92, Q3 92, max 93, IQR 1, range
  5, sum 2,842, mean 91.68, MAD 0.89. (Explore and Headline only.)
- Denver International Airport, July 1 to 31, 2024 (n 31): 89, 88, 93, 83, 81, 91, 78, 83, 90, 93, 98, 102, 99, 101,
  98, 90, 89, 92, 93, 87, 79, 84, 89, 95, 97, 93, 95, 96, 99, 100, 97. Min 78, Q1 88, median 93, Q3 97, max 102, IQR 9,
  range 24, sum 2,842, mean 91.68, MAD 5.32. Same sum as Miami, so the same mean. (Explore and Headline only.)
- Luka Doncic (Dallas Mavericks), points in each regular-season game he played, 2023-24 (n 70; Dallas played 82, he
  did not play in 12): 33, 49, 35, 18, 34, 23, 29, 31, 44, 30, 16, 26, 35, 25, 30, 30, 41, 36, 40, 32, 35, 33, 39, 40,
  38, 28, 39, 50, 39, 39, 19, 41, 34, 31, 33, 33, 34, 73, 28, 45, 40, 19, 35, 39, 32, 26, 27, 41, 33, 45, 30, 37, 38,
  39, 35, 39, 27, 21, 37, 18, 34, 29, 28, 26, 47, 30, 25, 37, 39, 29 (October 25, 2023 to April 10, 2024). Median 34
  (cards 35 and 36, both 34), Q1 29 (card 18), Q3 39 (card 53), min 16, max 73 (January 26, 2024, at Atlanta), IQR 10,
  sum 2,370, mean 33.86 (33.9), sum of distances 446.3, MAD 6.38 (6.4). Mode 39 (8 games). Shape: balanced middle with
  one far-off game. Card: "Player: Luka Doncic, Dallas Mavericks. Column: PTS. Season: 2023-24 regular season. Team
  games: 82. Did not play: 12. Source: Basketball-Reference.com game log." (Name shown with its accent: Dončić.)
- Axes (fixed, so charts never jump while dragging): temperatures 60 to 110 °F; points 0 to 90; Headline 75 to 105.
- Bin widths: temperatures 1, 2, 5, 10 (start 2); points 2, 5, 10 (start 5). San Diego at width 2 from 60: 70-72: 1,
  72-74: 8, 74-76: 11, then 1, 1, 1, 2, 0, 1, 1, 1, 1, 1 (the long high tail is visible).
- Step 1 chip rows (one correct, shown first here; shuffled on screen; lengths within about 25 percent):
  - Temperature sets, measured: "The highest temperature each day" / "The temperature at noon each day" / "The
    average temperature each day" / "The lowest temperature each day".
  - Temperature sets, how: "A weather station at the airport" / "A survey of people in the city" / "A weather app's
    forecast for the day" / "A count of sunny hours each day".
  - Units: "degrees Fahrenheit" / "degrees Celsius" / "inches of rainfall" / "miles per hour" (Luka: "points" / "minutes" / "games" / "shots").
  - Luka, measured: "Points he scored in each game" / "Points his team scored in each game" / "Minutes he played in
    each game" / "Shots he took in each game". How: "Kept in each game's official box score" / "A survey of fans
    after each game" / "Guessed from a basketball video game" / "Counted from one highlight video".
- Step 5 answers: San Diego: Median and IQR, reason "Lopsided: a long tail on one side". Chicago: Mean and MAD, reason
  "Roughly balanced, no far-off values". Luka: Median and IQR, reason "One value far from the rest". The three reason
  chips are those three on every set.
- Step 5 feedback (on screen, after the pick): San Diego "The hot spell pulls the mean up to 77.4 °F, but 21 of 30
  days were cooler than that. The median, 74 °F, is a typical day." Chicago "Balanced data: mean 75.2 and median 75
  agree, and the mean uses every day." Luka "One 73-point night is far from the rest. Here it moves the mean only a
  little, because there are 70 games; try dragging it in Explore."
- Headline options (A is right; A and C are the same length, word for word except the city order):
  A "Same 91.7 °F average high, but Denver's July swung far more than Miami's"; B "Miami and Denver had the same July,
  with a 91.7 °F average high each"; C "Same 91.7 °F average high, but Miami's July swung far more than Denver's";
  D "Denver's July was hotter than Miami's, judging by the average high". Reasons: A "Right: IQR 1 °F against 9 °F,
  range 5 °F against 24 °F."; B "The mean matches, but the spreads don't. Readers would expect Denver to feel like
  Miami."; C "Check the boxes: Miami's is the narrow one."; D "Both averages are 91.7 °F, so neither is hotter by
  that measure."
- Report card text (filled with the student's values): "[Place], [month]: the [measured], [how], in [units], on [n]
  [days or games]. Typical: [center pair]. Five-number summary: [min], [Q1], [median], [Q3], [max]."

## Interactions in detail
- Stats: engine `t.stats` (median of halves, the median left out when n is odd; matches the cards above). Mean and
  MAD checks accept any typed number within 0.05 of the true value (so 77.4 and 77.37 pass, 77.3 fails with "Close:
  round to the tenths place"). n and IQR must be exact.
- Typed fields (n, IQR, mean, MAD, both Headline IQRs): up to two tries. A miss gets a short reason (Interactions
  below); after the second miss Sam shows the working on screen (for the mean: "2,321 ÷ 30 = 77.37, about 77.4"), the
  field fills, and it is marked "Sam showed". Check is disabled while the box is empty.
- Chip and headline picks: one try. A wrong pick turns warn color with its reason, the right one is marked, the field is
  marked "Sam fixed". All other options lock.
- Card taps: strict position. A tap on a card with the right value at the wrong position counts as a miss with "Same
  number, but count: the middle has as many cards before it as after it." Other misses: "That's card 12. Count in
  from both ends." Two misses: the right card(s) pulse and fill in, marked "Sam showed". Even n: both middle cards
  must be tapped (any order); since both equal 74 or 34, the bubble adds "Both are 74, so the median is 74. If they
  differed, the median would be halfway between."
- Keyboard: the grid is one focus stop; arrows move by card, Enter taps. Chips and buttons in tab order, panel first.
- Explore drag edge cases: clamp at the axis ends; several dots can be moved; switching sets puts all dots back (hint
  says so); `Put back` also stops a drag in progress. Tiles update on every snap step.
- Animations: Line up (dots fly to the grid, 500 ms), a tick dropping to the axis (250 ms), the box drawing (400 ms),
  distance lines (under 900 ms). With Motion off each is instant. A tap during any of them acts at once on the final
  layout (the animation jumps to its end first); nothing waits for an animation.
- Mode switches keep each mode's state; `V.hush()` on every switch, then the hint for that mode's current step.
- `window.__tool = {state, setMode, setSet(id), drag(i, value), putBack(), build: {step, tap(pos), type(field, v),
  pick(row, k)}, headline: {type(city, v), pick(k)}, stats(), allLines, vlog}`.

## Look
Newsprint. paper `#f5f1e8`, panel `#ffffff`, cards and data card `#fbf8f1`, ink `#1e2229`, muted `#5a5f68`, header
`#e9e3d6`, button line `#767b84`, focus `#1f5fd1`, ok `#1d7a3c`, warn `#a3261b`. Accent `--brand #0d6670` (deep teal:
Median marker, step bar, primary buttons). Mean marker `#b23c17` (rust, dashed, diamond). Dots `--dd-1 #2d4a7a`;
moved dots and grid highlights `--dd-ring #b06f00`. Differs from neighbors (plum, chalk yellow, pink, gold, orange).
Contrast (computed): ink on paper 14.16:1, on panel 15.96:1; muted 5.69:1 / 6.42:1; brand 5.91:1 / 6.66:1; white on
brand 6.66:1; mean rust 5.25:1 / 5.91:1; dots 7.85:1; ring 3.64:1 (non-text); button line 3.77:1 (non-text); focus
5.15:1; ok 4.78:1; warn 6.54:1; ink on header 12.48:1. Mean and Median also differ by dash, flag shape and word.

## Art
Codex or Gemini for people (`people: true`, on Cory's contact sheet, fresh-agent representation check); local FLUX for
the rest. One style: warm painted editorial illustration, soft daylight.
- sam-ask: "A friendly young adult newspaper reporter with a notepad and pencil raised, curious look, rolled shirt sleeves, waist-up, plain light background"; 3:4; cutout yes; people yes; Sam's strip while a question waits.
- sam-pleased: same reporter, smiling and nodding, pencil tapping the notepad; 3:4; cutout yes; people yes; after a right answer and on the report card.
- sam-puzzled: same reporter, eyebrows raised, looking at the notepad, hand on chin; 3:4; cutout yes; people yes; after a miss and on the Headline draft.
- newsroom-desk: "A sunny small-town newsroom desk with a coffee mug, stacked blank newspapers and a desk lamp, painted"; 16:9; cutout no; people no; behind Sam's strip (cropped) and the report card frame.
- set-sandiego: "San Diego bay on a hot clear afternoon, palm trees and calm blue water, painted"; 4:3; set card.
- set-chicago: "A Chicago lakefront park in late spring with new green trees and a blue lake, painted"; 4:3; set card.
- set-miami: "A humid Miami beach in midsummer with turquoise water and towering white clouds, painted"; 4:3; set card.
- set-denver: "Denver's foothills in summer with the Rocky Mountains behind and a dry golden field, painted"; 4:3; set card.
- set-basketball: "An orange basketball resting on a polished hardwood court under arena lights, painted"; 4:3; set card.
Set names are typed in code under each card; no lettering in any image. Charts, grid, markers, report card text and
preview.svg are drawn in code. Sam stays the same person in all three poses and is fully visible in the strip.

## Voice
Bank voice `news-reader` (Rasalgethi, "Say clearly and steadily, like a trusted radio news reader"): Sam, a steady
reporter who wants the true story. Not used by a neighbor (data-table-builder knowing-guide, data-desk-distributions
upbeat-guide, which-model-wins science-narrator, simulation-studio gravel-ranger). `Curio.voice`, `scope: () =>
state.mode + ':' + state.set`. Grade 6: values, cards and reasons are read on screen; Read speaks the hint. No line
contains a number a voice must read from data.
- wExplore (how; Explore welcome; stale once any dot has moved): "Sam's question: what's a typical day? Drag any dot along the line, and watch which marker moves, the Mean or the Median."
- meanMoved (how; first time Mean moved at least 0.25 while Median moved 0; stale on Put back or set change): "The mean chased that dot. The median didn't move at all."
- medianMoved (how; first time Median moves; stale on Put back or set change): "Now the median moved too. That dot crossed over the middle."
- histo (how; first Histogram tap; stale when Dot plot is tapped): "Same data, counted in bins. Tap Bins plus or Bins minus to change the width. Tap Dot plot to drag again."
- wBuild (how; Build welcome; stale once n is checked): "Sam needs facts first. Read the data card, type how many values there are, then tap Check."
- facts (how; after n is right or shown): "Now say what was measured. Tap one answer in each row. Each row gets one try."
- lineUp (how; step 2 start, needs `#lineup`): "Tap Line up. The values will sort from smallest to largest."
- midOdd / midEven (how; after Line up, odd or even n): "Tap the middle card. It has as many cards before it as after it." / "This set has an even count, so two cards share the middle. Tap both of them."
- quart (how; after the median): "Now the halves. Tap the middle card of the lower half, then the middle card of the upper half."
- ends (how; after the quartiles): "Last, tap the smallest card and the largest card. The whiskers reach them."
- iqr (how; after the box draws, needs `#iqr-in`): "Your box runs from Q1 to Q3. Type the IQR, the width of the box, then tap Check."
- mean (how; step 3): "Share the total out evenly. Divide it by the number of values, type the mean, then tap Check."
- mad (how; step 4, after the lines finish): "Each line is one distance from the mean. The MAD is the average distance. Type it, then tap Check."
- pick (how; step 5): "Sam can print one center and one spread. Tap the pair that fits, then tap the reason."
- right (event; every correct field; whole): "Right." / missTry (event; first miss on a field; whole): "Not yet. Read the note, then try once more." / shown (event; field shown after two misses; whole): "Here's how Sam worked it out." / fixed (event; wrong one-try pick; whole): "Sam fixed that one. Read why."
- filed (event; File the report; whole): "Report filed. The check marks show what you found yourself."
- wHeadline (how; Headline welcome; stale once an IQR is checked): "Sam's headline says the two Julys were the same. Read both box plots, type each city's IQR, then tap Check."
- pickHead (how; after both IQRs are right or shown): "Now tap the headline that tells the whole story. You get one pick."
- headRight (event; whole): "That's the story. Same mean, very different spreads." / headWrong (event; whole): "The editor flagged that one. Read why, under it."
Event lines play every time their event happens, and at most once per Check press. How lines are spoken once per page
load, then hint only.

## Family engine
data-desk (`kit/data-desk.js`). Uses DataTable (one column per set: `high` with unit °F, or `pts`), `t.stats`, Chart
types `dot` (with `drag(true)`, `dragStep {x: 1}`, fixed `xDomain`, `highlight` for moved dots), `histogram` (`bins`
`{width, start}`, `animate` 300), and `box` (`marks: ['mean']` in Explore). The tool draws its own Mean and Median
markers, ghosts, distance lines, card grid and report card (they need words without values and ghosts the engine does
not have). One engine addition, made in the engine and docs/families/data-desk.md in the same change, existing calls
unchanged: box option `whiskers: 'range'` (whiskers to min and max, no outlier marks; grade 6 box plots), default
stays the 1.5 IQR rule. The Build box uses it with the student's five values drawn by the tool, then the engine box
(`whiskers: 'range'`) overlays it to confirm the match.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| n typed (Build 1) | guess; type numbers until right; copy a count from the screen; leave empty and press Check; the common wrong (31 for September, 82 for Luka) | answer space is wide and only two tries, then "Sam showed"; no count is printed anywhere (set cards name the month, not the count; Explore tiles show changes only; the card gives a date range or 82 minus 12); Check is disabled while empty; 31 and 82 fail with a reason |
| Measured / how / units chips | guess; elimination; position; longest option; matching words from the card | one try per row, then locked and marked "Sam fixed"; shuffled every visit; lengths within about 25 percent; the card uses codes (TMAX, PTS, °F), not the chip wording, so matching words does not work; guessing all three right is 1 in 64 |
| Median card tap | guess; tap every card; tap the visual center; tap a card showing the most common value; read the median off Explore | strict position with two misses, then "Sam showed" (guess odds 2 in 30 or worse); a same-value card at the wrong position is a miss; the mode differs from the median in Chicago (81 vs 75) and Luka (39 vs 34); in San Diego seven cards show 74, so the value alone gives no position; Explore's Median flag has no number; the visual center of an ordered grid is the median, which is the skill |
| Quartile card taps | as above; count quarters of all n (card 7 or 8 of 30) | strict position (San Diego Q1 card 8, Q3 card 23); card 7 is the same value 73 and counts as a miss with the count reason; box strip hidden until built |
| Min and max taps | tap the ends | that is the skill; guessing elsewhere fails |
| IQR typed (Build and Headline) | type the range; type Q3 alone; guess; mash Check | range (23, 27, 57; Miami 5, Denver 24) and Q3 fail with "IQR is Q3 minus Q1"; two tries; no IQR printed in Build or Headline (Explore shows only "IQR changed") |
| Mean typed | type the median; divide by n minus 1; truncate; type the total | 74, 80.03 (2,321 ÷ 29), 77.3 and 2,321 all miss by more than 0.05; two tries; no mean value on screen anywhere (Explore flags have no numbers) |
| MAD typed | type the IQR; divide by n minus 1; type the total; half the range | San Diego 8, 5.50, 159.4, 11.5 all fail (MAD 5.31); Chicago 174.2 ÷ 30 = 5.81 fails; Luka 446.3 ÷ 69 = 6.47 fails; two tries |
| Step 5 pair and reason | always pick Median and IQR; always the same reason; guess | one try each; the right pair is Median and IQR for San Diego and Luka but Mean and MAD for Chicago; each set's reason differs; guessing both right is 1 in 6 |
| Headline pick | pick the longest; pick by position; pick the mean-only draft; elimination | one pick, shuffled; A and C have identical length and words except city order, so only reading the boxes separates them; B (the common wrong, mean only) is marked "Sam fixed" with its reason; guess odds 1 in 4 |
| "Found on your own" count | inflate by retries | only first and second tries on typed fields and first picks count; shown and fixed fields never count |
| Explore tiles and markers | none (no check) | they show changes, never values, so they cannot feed Build or Headline answers |

## Heard in order
Grade 6, so not every line is voiced, but results must land before the next prompt:
- Build typed field: tap Check, then (1) right, or missTry, or shown, played whole; (2) only after it, the next step's
  how line (facts, lineUp, mean, mad...). The next step's controls are live at once; a tap on them drops the queued
  how line, never the result line.
- Build card taps: right or missTry (whole), then the next pick's how line (quart, ends, iqr). Two quick right taps queue
  one "Right." each, at most once per tap.
- Step 5: fixed or right for the pair, then the same for the reason, then filed after File the report.
- Headline: right or missTry or shown per IQR (Miami first, then Denver), then pickHead; after the pick, headRight or
  headWrong whole, before anything else.
- The welcome may be cut by the first tap (BASELINE rule 16); its content stays in the hint and Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| San Diego daily highs, Sept 2024 (30 values above) | NOAA NCEI GHCN-Daily, station USW00023188, TMAX, via ncei.noaa.gov/access/services/data/v1, pulled 2026-11-06 | NWS San Diego CF6SAN monthly climate report (F-6), September 2024, archived by Iowa Environmental Mesonet AFOS | yes, all 30 |
| Chicago O'Hare daily highs, May 2024 | NCEI GHCN-Daily USW00094846 | NWS CF6ORD, May 2024 | yes, all 31 |
| Miami daily highs, July 2024 | NCEI GHCN-Daily USW00012839 | NWS CF6MIA, July 2024 | yes, all 31 |
| Denver daily highs, July 2024 | NCEI GHCN-Daily USW00003017 | NWS CF6DEN, July 2024 | yes, all 31 |
| TMAX is the day's highest temperature, in °F as pulled | NCEI GHCN-Daily documentation (TMAX = maximum temperature) | NWS F-6 form, column "MAX" under "TEMPERATURE IN F" | yes |
| Luka Doncic 2023-24 regular-season points, 70 games; Dallas played 82, he missed 12 | Basketball-Reference.com, doncilu01 game log 2024 (82 rows, 12 Did Not Play or Inactive) | ESPN athlete game log, 2023-24 regular season (70 games once the All-Star Game, listed as a 7-point game vs EAST, is removed) | yes, same 70 values |
| 73 points on January 26, 2024, at Atlanta | Basketball-Reference game log | ESPN game log (2024-01-27 UTC, at Atlanta Hawks) | yes |
| Quartiles: median of each half, median left out when n is odd | Illustrative Mathematics Grade 6 Unit 8 Lesson 15 "Quartiles and Interquartile Range" | Khan Academy "Interquartile range (IQR)" review | yes |
| Grade 6 box plot whiskers run to the minimum and maximum | IM Grade 6 Unit 8 Lesson 16 "Box Plots" | Khan Academy "Box plot review" | yes |
| MAD is the average distance of the values from the mean | IM Grade 6 Unit 8 Lessons 11 and 12 | Khan Academy "Mean absolute deviation (MAD) review" | yes |
| Not symmetric or with far-off values: median and IQR are often better; roughly symmetric: mean and MAD work | IM Grade 6 Unit 8 Lessons 14 and 18 (lesson summaries) | OpenStax Introductory Statistics 2e, 2.6 "Skewness and the Mean, Median, and Mode" (the mean is pulled toward the tail) | yes; the tool says "fits" and "often", not "always" |
| 6.SP.4 and 6.SP.5 wording | thecorestandards.org/Math/Content/6/SP | the module row in data/tools-concepts.csv | yes |
Backed twice: 11 claims. Cut: 0 ("a heat wave" was not used as a claim; the tool says "hot spell, September 5 to 9",
which is the data itself; no record temperatures are claimed).
Number checks (Python 3, 2026-11-06), all match Content: every set's n, sum, min, Q1, median, Q3, max, IQR, mean, MAD,
sum of distances and card positions (school quartile rule); San Diego 21 below the mean, Chicago 16 and 15; histogram
counts at widths 1, 2, 5, 10; MAD from the rounded displayed totals still rounds to 5.3, 5.6, 6.4; the 0.05 tolerance
passes 77.4, 75.2, 33.9, 5.3, 5.6, 6.4 and fails every wrong behavior in "Can it be beaten?" (n minus 1 divisors,
truncation, median, IQR, range, totals). Drag effects: San Diego 94 to 110 moves the mean +0.53, median 0, IQR 0;
moving the five hot-spell days to 74 moves the mean -2.73, median 0, IQR -6; moving 71 to 110 moves the median +0.5
(crosses the middle); Luka 73 to 34 moves the mean -0.56, median 0; Chicago 89 to 110 moves the mean +0.68; Miami 88 to
110 moves the mean +0.71 and the IQR +1. Miami and Denver sums are both 2,842, so both means are 91.677.

## Done when
1. Focus and one idea: in Explore, dragging San Diego's 94 to 110 slides the Mean flag (tile "+0.53 °F") while the
   Median flag and tile stay at 0; dragging 71 to 110 moves the Median by 0.5; Put back restores all.
2. Dot plot, Histogram and the box strip show the same data on one fixed axis; Bins plus and minus give the counts in
   Content; dragging is off in Histogram with the hint naming Dot plot.
3. Build step 1 on each set: no count shows anywhere before the student types n; 31 for San Diego fails; chips allow
   one try and mark "Sam fixed".
4. Build step 2: Line up gives 10 cards a row in order; San Diego needs cards 15 and 16, then 8 and 23; card 7 (also
   73) is a miss; after two misses the card fills as "Sam showed"; the built box matches the engine's range box.
5. Mean and MAD accept 77.4 and 5.3 (San Diego), 75.2 and 5.6 (Chicago), 33.9 and 6.4 (Luka) and reject the wrong
   values listed in "Can it be beaten?".
6. Step 5 marks Median and IQR right for San Diego and Luka and Mean and MAD right for Chicago, with the reasons.
7. Headline: IQRs 1 and 9 are right; headline A prints with both IQRs and ranges; B, C and D show their reasons; the
   four buttons reshuffle on each visit.
8. A tap during Line up, a tick drop, the box draw or the distance lines acts at once on the final layout.
9. At 1366x768 every mode's focus and controls sit above the fold (Luka's 7-row grid included); at 680x425 the stage
   and panel stay side by side with Sam's cutout folded.
10. Voice: how lines once each, result lines before the next prompt, no line names a disabled control; Our class says
    on screen that numbers stay on the device; no network requests, no console errors.

## Open questions
- [box-plot-builder] A named living athlete (Luka Doncic, 2023-24 with Dallas) is the sports set. Fine, or use a team's points per game instead (less striking: no far-off value)?
