# Misleading Charts

## One idea
You work the fact-check desk at a made-up town paper, and every case is a published chart with a headline: measure it with a ruler that compares how much bigger the picture says against how much bigger the numbers say, name the trick (a cut-off axis, a hand-picked time window, a picture grown in two directions, two different axes, totals instead of rates, uneven time steps), rule on the headline, then redraw the chart honestly and print the correction beside the original.

## Not like
- data-detective (8, data-desk) and box-plot-builder (6, data-desk): honest charts that teach you to read data. Here every chart was drawn to persuade, and the data is never the problem; the drawing is.
- fake-or-fact-lab (6-8, library): checks whether claims and sources are true. Here the numbers are true and given; the question is what the picture does to them, measured with a ruler.
- poll-workshop (9-12, built): the data itself is biased by how it was collected. Here the data is fine and the chart lies.
- design-fixer (6-8, art): fixes where the eye lands on a poster. Here the fix is about axes, scales and rates, and the test is a number (the ruler), not where the eye goes.
- network-help-desk (4, mystery): questions reveal parts of a house map. Here the clues are measuring tools applied to a chart, and each case ends with a redrawn chart.
- algorithm-audit (6-8, this group): audits a rule that decides who gets a seat. Here nobody is ranked; the subject is a picture of data.

## Who and how
- Grades 6 to 8, computer science. Module: Data Detectives (Data and Analysis), "Sort, filter and visualize data; spot misleading charts". Topic line: "spotting and fixing misleading charts".
- Driver: students (pairs on laptops), or a teacher on a projector taking the class's vote on each trick before filing. 25 to 40 minutes (six cases at about 4 minutes each, then the Spin Room).
- Standards (CSTA 2026 ids from the module): MS-DAT-DC-23, MS-DAT-DI-25, MS-DAT-DI-26. 2017 crosswalk: 2-DA-08 (collect data and transform it to make it more useful and reliable), 2-DA-09 (refine models based on the data they generate). References: Tufte, The Visual Display of Quantitative Information (Graphics Press, 1983), "Lie Factor"; Cairo, How Charts Lie (W. W. Norton, 2019). Math link: 6.SP.B.4, 7.RP.A (rates).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Case Files", "Spin Room"], grades_label "Grades 6-8".

## Screens and modes
Kit frame, own `:root` (newsprint). Header: title "Misleading Charts", small line "The Pine Hollow Ledger fact-check desk"; mode buttons "Case Files" (folder icon) and "Spin Room" (spiral icon); Motion, Sound, Read.

### Mode 1: Case Files (opens first)
Focus: the published item with its chart, the biggest thing, left of center on the painted fact-check desk (art: desk-ledger). Stage: the case board. Left, the published item as it appeared (an ad, a newsletter column, a poster, a flyer, a district report, a club web page): a painted blank prop (art: item-*) with its made-up source line, headline and chart drawn in code on its blank area. Right of it (or below on narrow screens, always smaller), the Correction frame, empty until the case is filed.
A case strip across the top of the stage: six folder tabs "Case 1" to "Case 6", each showing "Open" or a "Closed" stamp. Any case can be opened in any order.
Panel, top to bottom:
- `#hint`.
- "Clue tools" section, five buttons (each with an icon): "Ruler" (tap two bars or points; shows drawn heights and data values), "Axis check" (outlines both axes, labels where each starts and its step), "Data sheet" (the numbers behind the chart, a small `table`), "Zoom out" (shows every data point the source had, with the published window shaded), "Per 100" (divides by the group size in the data sheet). Every tool works on every case; a tool that finds nothing says so ("Axis starts at 0. Nothing odd here.").
- "Notebook": each tool used adds a clue card with its finding, in the order found.
- "Your ruling" section: "The trick" (six trick cards, pick one; see Content) and "The headline" (three buttons: "Holds up", "True, but blown up", "Wrong"). "File it" (big button, enabled when both are picked).
- After a correct filing: the "Fix it" section shows the fix toggle for that trick (below); turning it on draws the honest chart in the Correction frame, with the ruler readout under it, and stamps the case "Closed". After a wrong filing: nothing is stamped; the hint names a clue tool not yet used, or, if all were used, the clue card to reread. No score, no count of tries.
"Next case" appears once a case is closed.

### Mode 2: Spin Room
A sandbox: you are now on the other side, at an ad agency. Focus: one chart, big and centered on the painted agency desk (art: desk-agency), with the "Picture says / Numbers say" meter under it. Panel:
- "Data" picker: the six case data sets.
- "Client's wish" card for that data set (for example "Make our sales look like they are soaring").
- Spin controls: "Axis starts at" slider (0 to just under the smallest value), "Time window" (from and to pickers), "Draw as" (Bars, Pictures by height, Pictures by height and width; the pictures are the data set's painted icon, art: pic-*), "Second axis" (off or on, with its range slider), "Count" (Totals, Per 100), "Space years" (By time, Evenly).
- "Fact-checker's view" toggle: lists every trick currently in use, each with the honest setting.
- "Make it honest" resets every control to the honest setting.

## Content
Trick cards (name; one-line meaning; the fix toggle):
1. "Cut-off axis": the value axis does not start at 0, so small differences look huge. Fix: "Start the axis at 0".
2. "Hand-picked time": only the months that tell the story are shown. Fix: "Show the whole year".
3. "Picture size": a picture is grown in height and width, so its area grows twice as fast. Fix: "Use bars".
4. "Two different axes": two lines get their own scales, chosen to make them match. Fix: "One chart each, from 0".
5. "Totals, not rates": bigger groups have bigger totals. Fix: "Per 100 students".
6. "Uneven time steps": years with different gaps sit equal distances apart. Fix: "Space by years".

Cases (all places, publishers and numbers made up; each says so in its source line):
1. "Pretzel sales are SOARING!" Ad, Pine Hollow Pretzel Company. Bars: 2024 1,000 bags, 2025 1,050 bags; value axis from 950 to 1,060. Ruler on the two bars: picture 2.0 times taller, numbers 1.05 times bigger; lie factor 20. Trick 1. Ruling: "True, but blown up".
2. "Students have stopped reading." Pine Hollow Middle School newsletter. Bars Nov 840 and Dec 510 library visits, axis from 0. Full year (Zoom out): Sep 820, Oct 860, Nov 840, Dec 510, Jan 830, Feb 850, Mar 870, Apr 800, May 880, Jun 400. School days (Data sheet): Sep 20, Oct 22, Nov 19, Dec 12, Jan 19, Feb 19, Mar 21, Apr 17, May 21, Jun 9. Per school day: Nov 44.2, Dec 42.5, Jan 43.7. Trick 2. Ruling: "Wrong".
3. "Green Team recycled twice as much!" Poster. Two recycling bin pictures (art: pic-recycling): 2024 120 kg, 2025 240 kg; the 2025 bin is twice as tall and twice as wide. Ruler: picture 4 times the area, numbers 2 times; lie factor 3. Trick 3. Ruling: "True, but blown up".
4. "Smoothies help us win!" Snack bar flyer. Two lines, Mar to Jun: smoothies sold 120, 150, 190, 240 (left axis 100 to 250); soccer wins 1, 2, 2, 3 (right axis 0.67 to 3.17, exactly 2/3 to 19/6, ticks 1, 2, 3, chosen so 1 win sits at 120 and 3 wins at 240). Axis check reveals two scales. Note on the corrected chart: "Both go up as spring goes on. Rising together does not show that one causes the other." Trick 4. Ruling: "Wrong".
5. "Oak students are the roughest on laptops." District report. Bars of broken laptops: Oak 45, Elm 30, Birch 27. Students (Data sheet): Oak 900, Elm 300, Birch 450. Per 100: Oak 5, Elm 10, Birch 6. Ruler Oak against Elm: picture 1.5 times; per 100, 0.5 times. Trick 5. Ruling: "Wrong".
6. "Robotics club growth has stalled." Club web page. Line over evenly spaced labels: 2004 6, 2009 11, 2014 16, 2019 21, 2020 22, 2021 23, 2022 24, 2023 25 members. Ruler on the first and last steps: 5 members per step, then 1 per step; by years, 1 member per year all along (19 members over 19 years). Trick 6. Ruling: "Wrong".

Ruler readout (all cases and Spin Room): "Picture: [a] times. Numbers: [b] times." and, when both go the same way, "Lie factor: [(a - 1) / (b - 1)]" rounded to one decimal, with "1 means honest." Lie factor is Tufte's measure. For areas (case 3, pictures in Spin Room) the picture value is the area ratio. When b is 1 (no change) the lie factor line is hidden.

Spin Room client wishes: 1 "Make our sales look like they're soaring." 2 "Make it look like nobody reads anymore." 3 "Make our recycling look enormous." 4 "Make it look like smoothies win games." 5 "Make Oak look like the problem school." 6 "Make the club look like it stopped growing." Each data set's honest settings are the fixes above.

## Interactions in detail
- Ruler: tap a first bar, point or picture, then a second; dashed measuring lines drop to the drawn baseline with the drawn heights in px; the readout appears in the Notebook. The picture ratio is computed from the chart's geometry in data units (bar top minus axis start, or picture area), never from rounded pixels, so case 1 reads exactly 2.0 and 20.0. Tapping a third item starts over. On case 4 the ruler measures each line against its own axis and adds "These two lines use different scales."
- Axis check draws a bracket on each axis with "Starts at 950" or "Starts at 0" and the step; on case 6 it marks each gap with its years ("5 years", "1 year").
- Zoom out animates the hidden data in over 400 ms (instant with Motion off) with the published window shaded; on cases with no hidden data it says "This is all the data the source had."
- Per 100 redraws the bars as rates in a ghost overlay; works only where the data sheet has group sizes (case 2 uses school days and says "Per school day").
- Filing is checked against the case's trick and ruling. A right trick with a wrong ruling (or the reverse) is wrong as a whole; the hint says which half to rethink without giving the answer ("The trick is right. Look again at whether the headline's numbers are true.").
- Fix it: only the case's own fix toggle is shown; the correction redraws over 400 ms. Closed cases keep their correction when reopened. "Reset cases" (in the panel footer, confirm) reopens all six.
- Every animation (Zoom out, the correction redraw, a picture growing in the Spin Room) is under 0.5 s, and a tap during it acts at once: another tool, a case tab or a control finishes the animation instantly and applies the new action.
- Spin Room controls apply at once; the meter updates live. Controls that do not fit a data set are disabled with a reason ("This data has no group sizes"). At the slider's extreme (data set 1, axis at 999) the meter reads 51.0 times and lie factor 1000.0; the number is shown, not capped.
- Keyboard: panel before stage; chart items are focusable in order, Enter selects for the Ruler. Visible focus.
- Sizes: the published item, the clue tools and "File it" visible without scrolling at 1280x720 and 1366x768; at 680x425 the Correction frame becomes a tab beside the published item and the Notebook collapses to its last card. Chart text at least 11 px in the preview.
- Nothing is saved except which cases are closed (localStorage `mc-closed`, cleared by "Reset cases").

## Look
- Accent `--brand #a21caf` (highlighter fuchsia; header rule, selected trick, the highlight marks the ruler leaves). `--head-ink #ffffff` on the brand header strip.
- Own `:root` (newsprint): `--paper #f4f1ea`, `--panel #fffdf8`, `--ink #1c1b19`, `--muted #5d5a52`, `--line #dcd6c8`, `--btn #a21caf`, `--focus #0b6e4f`. Highlighter wash #f9c6f2 behind clue text. Published charts in ink gray #3f3d39 with a serif headline; corrected charts in #2563eb with a "Correction" label, so original and fix differ by label and style, not color alone. "Closed" stamp in fuchsia with a rotated border.
- Painted pieces in a soft realistic newsroom style: the desk in worn oak and paper tones, the agency desk in glossy white and chrome so the switch of sides reads at a glance. The blank props are pale paper, so code charts on them keep their contrast (chart ink on prop paper is checked as ink on panel).
- Neighbors: model-mechanic and phishing-spotter limes, packet-race red, chore-flowcharts cyan, code-kitchen copper, design-fixer indigo, algorithm-audit navy. Fuchsia on newsprint is new among them and among its group siblings (chalk yellow, hot spring orange, deep sky, navy).
- Contrast: white on brand 6.32:1; brand on paper 5.61:1; brand on panel 6.22:1; ink on paper 15.26:1; muted on paper 6.10:1; focus on paper 5.54:1; ink on highlighter 11.79:1; published gray on panel 10.66:1; correction blue on panel 5.08:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), none with people. One style: soft realistic illustration, warm daylight, plain paper surfaces. Every surface that carries text is painted blank; headlines, source lines, axes and labels are drawn in code on it.
- desk-ledger: "Top-down view of a small-town newspaper fact-check desk: worn oak desk, a cork board edge, a coffee mug, a red pencil, a magnifying glass and a clear empty space in the middle, warm daylight"; 16:10; cutout no; people no; Case Files stage background (dimmed under the props).
- desk-agency: "Top-down view of a sleek ad agency desk: glossy white surface, chrome lamp, color swatches fanned at one corner, a stylus and a clear empty space in the middle, cool daylight"; 16:10; cutout no; people no; Spin Room stage background.
- Published item props (6 pieces, one shared prompt "..., blank paper with no printing, soft realistic illustration, plain white background"; 3:4; cutout yes; people no; each sized to fill 55 percent of the stage height, the chart drawn in its blank area): item-ad "a glossy magazine page"; item-newsletter "a folded school newsletter sheet"; item-poster "a poster pinned to a cork board with two red push pins"; item-flyer "a flyer taped to a wall with two strips of tape"; item-report "a stapled district report cover page"; item-webpage "an open laptop with a plain white browser window".
- Picture icons (6 pieces, one shared prompt "a single [object], centered, soft realistic illustration, plain white background"; 1:1; cutout yes; people no; the picture marks in case 3 and in the Spin Room's picture modes, stretched in height only or in both directions as the chart says): pic-pretzels "plain paper bag of pretzels with a blank label"; pic-book "closed library book with a blank cover"; pic-recycling "green plastic recycling crate heaped with cans and bottles"; pic-smoothie "smoothie in a clear cup with a straw"; pic-laptop "closed school laptop"; pic-robot "small wheeled robot kit".
Charts, axes, rulers, stamps, clue cards and preview.svg (a cut-off bar chart with a fuchsia ruler across it and a "Correction" chart beside it) are drawn in code.

## Voice
Bank voice `news-reader` (Rasalgethi), "Say clearly and steadily, like a trusted radio news reader": the desk editor. Not used by a 6-8 CS neighbor (model-mechanic science-narrator, packet-race firm-captain, phishing-spotter lively-host, chore-flowcharts friendly-dad, code-kitchen easy-coach, algorithm-audit calm-professor) or a group sibling; biased-bot (4) uses it in a lunchroom. Headlines, sources and clue cards are read on screen. `Curio.voice`, `scope: () => state.mode + ':' + state.caseId`.
1. wCases (how, Case Files welcome; stale on the first clue tool): "Welcome to the fact-check desk. Every chart here was published. Tap a clue tool, like Ruler, to find out what it's hiding."
2. ruler2 (how, first Ruler pick; stale when the second item is picked): "Tap a second bar. The ruler compares the picture to the numbers."
3. firstClue (how, first clue card; stale when File it is pressed): "Clues go in your notebook. When you know the trick, pick it, rule on the headline, and press File it."
4. filedRight (event, filed right; stale when the fix toggle turns on or the case changes): "Filed. Now turn on the switch in Fix it to correct the chart."
5. filedWrong (event, filed wrong; stale on the next pick or case change): "Not quite. Read the hint, change your picks, then press File it again."
6. closed (event, a case closed; stale when the case changes): "Correction printed. Case [n] is closed." (six fixed lines)
7. allClosed (event, all six closed; stale on mode change): "All six cases are closed. Press Spin Room to see how the tricks are made."
8. wSpin (how, Spin Room welcome; stale on the first control change): "Now you work for the client. Move the spin controls to give them their wish, and watch the meter."
9. factView (how, first Fact-checker's view; stale on Make it honest): "This is what a fact-checker would catch. Press Make it honest to undo every trick."

## Family engine
none. The tool draws its own charts in SVG (bar, line, picture bars, dual axis), because every chart must be drawable wrong on purpose, which the data-desk engine's fixed axis rules do not allow.

## Sources
- Lie factor (size of effect shown in the graphic divided by size of effect in the data): Edward Tufte, The Visual Display of Quantitative Information, Graphics Press, 1983, chapter 2.
- Truncated axes, cherry-picked windows, area scaling, dual axes, totals versus rates: Alberto Cairo, How Charts Lie: Getting Smarter about Visual Information, W. W. Norton, 2019.
- Bar charts should start at zero because bar length encodes the value; rising together is not cause: Cairo (2019).
- CSTA K-12 Computer Science Standards (2017), 2-DA-08 and 2-DA-09: https://csteachers.org/k12standards/
- Pine Hollow, the Ledger, every publisher and every number in the six cases are made up for this tool; all ratios above were computed from them.
- Checks run (Python, 2026-10-29): case 1 picture 2.0, numbers 1.05, lie factor 20.0 (19.99999 in floating point, so it must be rounded, not truncated); case 2 per school day 44.2, 42.5, 43.7, and the published Nov to Dec bars are honest (both 0.607); case 3 area 4 against 2, lie factor 3.0; case 4 the right axis that puts 1 win at 120 and 3 wins at 240 is exactly 2/3 to 19/6 (both lines at 0.133 and 0.933 of the height); case 5 per 100 Oak 5, Elm 10, Birch 6, Oak against Elm 1.5 times in totals and 0.5 times per 100; case 6 19 members over 19 years, 1 per year. Spin Room worst case: axis at 999 gives 51 times and lie factor 1000.

## Done when
1. Case 1's Ruler on the two bars reads "Picture: 2.0 times. Numbers: 1.05 times. Lie factor: 20.0"; Axis check says "Starts at 950".
2. Case 2's Zoom out shows ten months with Nov and Dec shaded; Data sheet per school day gives Nov 44.2 and Dec 42.5.
3. Case 3's Ruler reports area 4 times against numbers 2 times and lie factor 3.0; its right ruling is "True, but blown up".
4. Case 5's Per 100 shows Oak 5, Elm 10, Birch 6; filing "Totals, not rates" with "Holds up" is refused with the "trick is right" hint.
5. Each case closes only with its own trick and ruling, and its fix toggle draws a correction whose ruler reads lie factor 1.0 (or "honest" for cases 2, 4 and 6).
6. In the Spin Room, moving "Axis starts at" on data set 1 to 950 makes the meter read 2.0 times, and Fact-checker's view lists "Cut-off axis".
7. Lines 2, 3, 8 and 9 are each spoken once in a run of five actions; lines 4 to 6 every time.
8. Clue tools and File it visible without scrolling at 1366x768 and 680x425; original and correction told apart in grayscale by label and style.
9. Focus: at 1366x768 and 1000x625 the published item with its chart is the largest thing in Case Files, and the spun chart is the largest in the Spin Room.
10. Tap while it plays: a tap on another clue tool or case tab during Zoom out or the correction redraw finishes it at once and acts; a Spin Room slider dragged during a picture growth updates the meter at every move.
11. Each published item sits on its painted blank prop with the headline and chart readable at 680x425 (text 10 px or more); no FLUX lettering shows on any prop.

## Open questions
- [misleading-charts] Fourteen new painted images (two desks, six blank props, six picture icons), none with people; the old spec drew everything in code. OK?
