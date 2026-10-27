# Sorting Showdown

## One idea
Five sorting algorithms sort the same list side by side, one comparison per tick, and the winner depends on the data you hand them: insertion sort finishes a nearly sorted list in 34 comparisons while quicksort (last-item pivot) needs 456, then the Growth chart pushes the list from 8 to 1,024 items and the counts split into an n squared family and an n log n family.

## Not like
- api-playground, data-policy-council (9-12, same group): building with modules, and a policy roleplay. Here nothing is built or argued; you choose inputs and watch measured behavior.
- network-architect (9-12 CS): tests a design against a checklist. Here the "design" is a classic algorithm, fixed and correct; only the data and the size change.
- packet-race (6-8 CS): a timed race you steer. Here no one steers and the clock is counted comparisons, not seconds, so the result is the same on every laptop.
- code-tracer (grade 4): steps a tiny program by hand. Here the code is a reference card; the counts and the growth curves are the point.
- leaf-sorter-ai (grade 5): "sorting" leaves into classes with a model. Here sorting means putting a list in order.

## Who and how
- Grades 9 to 12, computer science (AP CSP and AP CSA classes too). Module: Data Structures and Algorithms (Algorithms and Programming), "Design and evaluate algorithms for efficiency and correctness". Topic line: "comparing sorting algorithms and efficiency".
- Driver: students on laptops, or a teacher on a projector asking "who wins this one?" before each run.
- 15 to 30 minutes: Lanes on four data shapes (10 min), Growth (10 min), Draw your own list (5 min).
- Standards (CSTA 2026, as listed): HS-ALG-PS-01, HS-ALG-PS-03, HS-PRO-VD-16. CSTA 2017 crosswalk (matched by topic): 3B-AP-10 (use and adapt classic algorithms to solve computational problems), 3B-AP-11 (evaluate algorithms in terms of their efficiency, correctness and clarity), 3B-AP-12 (compare and contrast fundamental data structures and their uses).
- tool.json: driver "students or teacher", minutes "15-30", modes ["Lanes", "Growth"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`, `kit:graphing`.

## Screens and modes
Header (kit): "Sorting Showdown", small line "Same list, five sorts". Mode buttons: **Lanes** (opens first), **Growth**. Motion, Sound, Read.

### Mode 1: Lanes
Stage: five stacked lanes, laid out at real pixel size. Each lane: the algorithm's name (a button that opens its card), a bar chart of the list (n bars, height = value), and readouts at the right: Comparisons, Moves, and a finish rank ("1st", "tied 2nd") when done. Across the top, the **Tick** counter. Bars being compared are violet with a small ▲ under each; bars just written flash orange with an outline; a finished lane turns its bars green with a ✓ beside the name.

Panel:
- `#hint`.
- **Data** picker (`.btn` group): **Random**, **Nearly sorted**, **Reversed**, **Few unique**, **Draw**.
- **Size**: 16, 32, 64.
- **Run** (big; becomes **Pause**), **Step** (one tick), **Finish** (jump every lane to its end), **Reset** (same list, counters to 0), **New shuffle** (a new seed for Random, Nearly sorted and Few unique; off for Reversed and Draw).
- **Speed** slider: 2 to 400 ticks per second, log scale (default 20).
- **Show equal bars' order** toggle (only for Few unique and Draw): shades bars of the same value from light to dark by their starting position, and adds a Stable column to the results.
- **Results** table (`table.inst`), filled as lanes finish: Algorithm, Comparisons, Moves, Rank, (Stable). Tap a column head to sort the table by it (the table is itself sorted with a stable sort).

Draw: the lanes hide behind one input strip; drag across it (or use arrow keys on a focused bar) to paint heights 1 to n; repeats allowed. **Use this list** copies it to all lanes.

Algorithm card (opens over the lanes from a lane's name): two sentences, the pseudocode (Content), and the facts line with its numbers. **Close** or Escape.

### Mode 2: Growth
Stage: a `kit/graphing` plane. x: list size n at 8, 16, 32, 64, 128, 256, 512, 1024 (plotted at log2 n, labeled with n). y: comparisons, **Linear** (default, 0 to 550,000) or **Log** (1 to 1,000,000, powers of ten). Five series with points joined by lines, each with its own color and dash and an end label; two grey dashed reference curves labeled "n²/2" and "n log₂ n". A trace point on each series reads out (n, comparisons) on hover or arrow keys.
Panel: `#hint`, the **Data** picker (Random, Nearly sorted, Reversed, Few unique), **Linear / Log**, series checkboxes (all on), and the values table for the chosen shape (Content).

## Content

Lists (n items; values 1 to n unless noted). Random numbers come from mulberry32 (seed s): `a = a + 0x6D2B79F5 | 0; t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296`.
- Random (seed 1): start 1..n, Fisher-Yates from the end: for i = n-1 down to 1, j = floor(r() * (i + 1)), swap a[i], a[j]. At n = 32: 13 9 26 32 7 15 14 18 12 31 17 4 10 6 2 25 20 5 27 3 22 24 23 11 19 30 8 28 29 16 1 21.
- Nearly sorted (seed 2): start 1..n, then floor(n / 10) times: i = floor(r() * (n - 1)), swap a[i], a[i+1]. At n = 32 the swapped pairs are 9-10, 11-12, 23-24.
- Reversed: n down to 1.
- Few unique (seed 3): each value 1 + floor(r() * 4), so only 1 to 4. Bars scale to the tallest value.
- New shuffle adds 10 to each seed (11, 12, 13, then 21, 22, 23...).

Algorithms (each counts a comparison when two list items are compared; a move is one write into the list, so a swap is 2):
- **Bubble sort**: passes i = 0..n-2; compare neighbors j, j+1 for j < n-1-i, swap if left is bigger; stop when a pass swaps nothing. Card: "Compares neighbors and swaps them until a pass makes no swaps. Stable. About n²/2 comparisons, but only n - 1 on a list already in order."
- **Selection sort**: for i = 0..n-2 find the smallest of i..n-1 (compare a[j] < a[min]), then swap it into i if needed. Card: "Finds the smallest remaining item and swaps it into place. Not stable. Always n(n - 1)/2 comparisons, and at most n - 1 swaps."
- **Insertion sort**: for i = 1..n-1, while j > 0 and a[j-1] > a[j], swap and step left (each check is a comparison; the failing check counts too). Card: "Slides each new item left until it fits. Stable. About n²/4 comparisons on a random list, and close to n on a nearly sorted one."
- **Merge sort**: top-down, mid = floor((lo + hi) / 2); merge with a copy, taking the left item when left <= right; each item written back is a move. Card: "Splits the list in half, sorts each half, then merges them. Stable. Between ½ n log₂ n and n log₂ n comparisons on any list, but it needs extra space for a copy."
- **Quicksort**: Lomuto partition, pivot = last item; compare a[j] < pivot; swap only when positions differ; recurse left then right. Card: "Splits the list around a pivot, then sorts each side. Not stable. About 1.39 n log₂ n comparisons on average, but n²/2 when the pivot is always the largest or smallest, as on a sorted or reversed list."

Ticks: each tick, every unfinished lane makes exactly one comparison; moves between comparisons are shown with the next one, and any moves after the last comparison land on that last tick. A lane's finish tick equals its comparison count. Ties share a rank.

Counts (comparisons / moves), computed in Python with the rules above:

| n = 32 | Bubble | Selection | Insertion | Merge | Quick |
|---|---|---|---|---|---|
| Random | 496 / 470 | 496 / 54 | 261 / 470 | 124 / 160 | 150 / 118 |
| Nearly sorted | 61 / 6 | 496 / 6 | 34 / 6 | 80 / 160 | 456 / 6 |
| Reversed | 496 / 992 | 496 / 32 | 496 / 992 | 80 / 160 | 496 / 32 |
| Few unique | 475 / 302 | 496 / 44 | 181 / 302 | 114 / 160 | 212 / 86 |

At n = 16 Random: 120, 120, 71, 46, 50 comparisons. At n = 64 Random: 2016, 2016, 1118, 307, 352. Stability on Few unique (16, 32, 64): bubble, insertion and merge stable; selection and quick not.

Growth values (comparisons at n = 8, 16, 32, 64, 128, 256, 512, 1024):
- Random: Bubble 28, 120, 496, 2016, 8128, 32640, 130815, 523773. Selection 28, 120, 496, 2016, 8128, 32640, 130816, 523776. Insertion 19, 71, 261, 1118, 4269, 16778, 65688, 265319. Merge 15, 46, 124, 307, 730, 1713, 3941, 8942. Quick 16, 50, 150, 352, 907, 2085, 5089, 11332.
- Nearly sorted: Bubble 7, 29, 61, 125, 253, 762, 1530, 3066. Selection as Random. Insertion 7, 16, 34, 69, 137, 280, 557, 1118. Merge 12, 33, 80, 196, 454, 1040, 2330, 5169. Quick 28, 109, 456, 1806, 7552, 29731, 118901, 477094.
- Reversed: Bubble, Selection, Insertion and Quick all 28, 120, 496, 2016, 8128, 32640, 130816, 523776. Merge 12, 32, 80, 192, 448, 1024, 2304, 5120.
- Few unique: Bubble 27, 92, 475, 1971, 7750, 31044, 123190, 492150. Selection as Random. Insertion 19, 49, 181, 643, 3021, 12580, 52760, 202275. Merge 17, 44, 114, 280, 673, 1581, 3672, 8236. Quick 19, 57, 212, 626, 2358, 8688, 33550, 131861.
- Reference: n²/2 = 32, 128, 512, 2048, 8192, 32768, 131072, 524288. n log₂ n = 24, 64, 160, 384, 896, 2048, 4608, 10240.
The tool computes these live (the same code as the lanes, with no drawing); the lists above are the check.

## Interactions in detail
- Opens on Lanes, Random, n = 32, paused at tick 0, so the first Run shows merge finishing at tick 124 and bubble last.
- Changing Data or Size resets all lanes. Pause holds every lane at the same tick. Step works while paused. Finish fills the results at once.
- At 400 ticks per second, bars redraw once per animation frame (several ticks per frame); counters stay exact.
- Show equal bars' order: shades go from `#e3d6ff` (first) to `#6c4bc4` (last) within each value; the Stable column reads "yes" or "no (3 pairs swapped)". Not color alone: the column says it.
- Draw: an empty strip starts all at height 1; painting is clamped to 1..n; Use this list is off until at least two bars differ.
- Growth: computing all five series up to 1,024 takes well under a second; the series appear left to right with a short draw-on (none with Motion off). Turning a series off removes its line and its trace point.
- Sound (if on): a soft tick per comparison at speeds up to 20 per second, pitched by the compared bar's height; silent above that. A lane finishing plays one short tone.
- Motion off: no draw-on or flashes; the compared ▲ marks still show.
- Sizes: at 1366x768 all five lanes, Run and the results fit; lanes shrink to 56 px tall minimum and bars to 2 px wide minimum (at n = 64 below about 760 px of lane width the lane pans sideways instead). At 760 wide the panel goes below with Run first. At 375 wide only two lanes show at a time with a lane picker ("Compare: Insertion vs Quick"), default those two.
- Keyboard: Space runs or pauses; Right arrow steps; Tab reaches lane names after the panel controls.
- `window.__tool = {state, setMode, setData(kind, n, seed), runTo(tick), finish(), counts(kind, n)}` for tests.

## Look
- Accent `--brand #c39bff` (violet: the compare marks, Run and the header rule) with `--brand-ink #1c1203`, on `kit:theme-912`.
- Bars `#8a9bb3`; compared bars brand violet with ▲; writes flash `#ff9e64` with an outline; finished bars `--ok #6fdca6` with ✓. Growth series: `--gr-1` to `--gr-4` with their dash patterns plus brand violet (dash `4 3`) for Quick; references `#a6b3c4` dashed.
- Contrast (computed): brand on `--panel` 7.79:1, on `--sec-bg` 7.38:1, on the plane `#0e1520` 8.24:1; brand-ink on brand 8.31:1; bars on the plane 6.47:1; write orange 9.00:1; finished green 10.87:1; reference grey 8.60:1; ink on panel 14.70:1. All pass AA (graphics need 3:1).
- Neighbors: api-playground lemon, network-architect sky blue, ai-evaluator and capture-the-flag pink. No celebration: ranks and a ✓.

## Art
none: drawn in code (bars, lanes, the growth chart, preview.svg).

## Voice
Bank voice `science-narrator` (Charon), "Say in a clear, informative way, like a nature documentary narrator", here watching algorithms behave in the wild. Not used by any group sibling or 9-12 CS neighbor (model-mechanic, 6-8, is its nearest other CS user). Numbers and cards are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-lanes (how, Lanes welcome): "Five sorts, one list. Pick the data, then press Run."
- data (how, first change of Data): "Same five sorts, new data. Watch who finishes first now."
- nearly (event, a Nearly sorted run finishes; stale on reset): "On a nearly sorted list, insertion sort barely has to move."
- quickbad (event, quicksort finishes last on Nearly sorted or Reversed; stale on reset): "Quicksort chose the largest item as its pivot again and again, and fell to n squared."
- stable (how, first time the order toggle is on): "Shaded bars show the order equal items started in. A stable sort keeps it."
- w-growth (how, Growth welcome): "Now grow the list. Switch to Log to see two families of curves."
- log (how, first switch to Log): "On a log scale, the n squared sorts run parallel, and the n log n sorts pull away below."

## Family engine
none. Uses `kit/graphing.js` (docs/families/graphing.md) as a library for the Growth plane: `Plane` with `tickFormat` (x labels as n, y as plain numbers or powers of ten), each series drawn as `g.segment` lines between `g.point` markers (keyboard focusable, with `valueText` readouts), and `g.label` for end labels.

## Sources
- CSTA 2026 ids HS-ALG-PS-01, HS-ALG-PS-03, HS-PRO-VD-16 (`data/standards/csta-2026-ids.txt`); CSTA K-12 CS Standards (2017) 3B-AP-10, 3B-AP-11, 3B-AP-12: https://csteachers.org/k12standards/
- Comparison counts and stability (selection n²/2 compares and at most n exchanges; insertion about n²/4 on average and n - 1 when sorted; merge between ½ n lg n and n lg n; quicksort about 1.39 n lg n on average and n²/2 worst case): Robert Sedgewick and Kevin Wayne, Algorithms, 4th ed., sections 2.1 to 2.3, https://algs4.cs.princeton.edu/20sorting/
- Lomuto partition (last-item pivot): Thomas H. Cormen et al., Introduction to Algorithms, 3rd ed., section 7.1 (PARTITION) and problem notes crediting Lomuto; Jon Bentley, Programming Pearls, 2nd ed., column 11.
- Bubble sort with an early exit and stability definitions: Donald E. Knuth, The Art of Computer Programming, vol. 3, Sorting and Searching, 2nd ed., section 5.2.2 and section 5 (stable sorting).
- mulberry32 generator (Tommy Ettinger, public domain), JavaScript form as listed in bryc, "Pseudorandom number generators", https://github.com/bryc/code/blob/master/jshash/PRNGs.md
- All counts in Content computed in Python with the exact rules above (2026-10-27).

## Done when
1. `counts(kind, 32)` matches the n = 32 table for all four data shapes, comparisons and moves.
2. Lanes, Random, n = 32: after Run, merge finishes at tick 124 (1st), quick 150, insertion 261, bubble and selection tied at 496.
3. Nearly sorted, n = 32: insertion 1st at 34, bubble 61, merge 80, quick 456, selection 496; the nearly and quickbad lines play.
4. Reversed: merge alone finishes early (80); the other four tie at 496.
5. Few unique with the order toggle: Stable reads yes for bubble, insertion and merge, no for selection and quick, with a pair count.
6. Growth values match Content at every n for every shape; Log shows the reference lines; trace readouts by keyboard work.
7. Draw: painting and Use this list run all five lanes on the drawn list; every lane ends sorted.
8. Every size in STANDARDS.md: Run and at least two full lanes visible without page scrolling; 375 wide shows the two-lane picker.
9. Voice: welcome once per mode, how lines once then hint only, event lines each time while fresh; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".
