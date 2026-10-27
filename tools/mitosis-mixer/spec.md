# Mitosis Mixer

## One idea
Do the classic onion root tip lab on a stained microscope field: find and sort every cell into interphase,
prophase, metaphase, anaphase or telophase by what its chromosomes look like, then turn your counts into how long
each phase lasts (a phase seen in few cells is a short phase), and grow a root to see that the cells mitosis makes
all carry the same DNA yet become root hairs, water pipes and cap cells because different genes switch on.

## Not like
- cell-city (grade 6, cells family): organelles as parts of a city. Here the nucleus only, through one cycle, as a
  lab count.
- membrane-gatekeeper (same group, cells family): one cell's membrane in real time. Here a hundred still cells,
  each frozen at one moment.
- punnett-predictor (same group): meiosis makes four different sex cells. Here mitosis makes two identical cells;
  the sort bins say so.
- sample-machine (math): sampling as a statistics idea. Here a sample is the only way to time something you can never
  watch (a snapshot of many cells), and the math stays one line.
- half-life-dice (sci 10): counting to estimate a rate of decay. Here counting to estimate how long phases last.

## Who and how
Grade 9, science (Life Science module Cell Division and Differentiation: "Mitosis and specialization"). Driver:
students on laptops, often in pairs as in the wet lab. 20 to 40 minutes. Standards: HS-LS1-4 (use a model to
illustrate the role of mitosis and differentiation in producing and maintaining complex organisms).
Topic line: mitosis and cell differentiation.
9-12 dark theme. Header: title, `.seg` modes **Count**, **Grow the root**, kit buttons `motion`, `sound`, `read`.

## Screens and modes
**Count** (opens first). Stage: a round microscope view (eyepiece circle on black) showing a stained onion root
tip, 120 cells in neat files (columns), drawn by the cells engine `Field` in stain style. A **Focus** knob (blur in,
sharp at the middle setting) and **Zoom** `.seg` **100x** / **400x** (400x shows a quarter of the field, pan by
drag or arrow keys) give the microscope feel; the starting state is 400x, in focus, top left.
Panel: five bins as buttons, **Interphase**, **Prophase**, **Metaphase**, **Anaphase**, **Telophase**, each with a
small reference drawing and its count. Sorting: click a cell (it gets an accent ring), then a bin (or press 1 to
5). A sorted cell gets a small number tag of its bin (1 to 5) so the field shows progress; **Undo** last.
A **Data table** (`table.inst`): Phase, Cells counted, Fraction, Estimated time (minutes), filled live from the
counts: time = cells in phase / cells counted x 1,440 minutes. Above it: "Cells counted N of 120" and "Mitotic
index" (dividing cells / cells counted, as a percent).
**Check my sort** (any time): marks cells whose bin differs from the field's true phase (a small dashed outline),
and for each mismatch on click shows the cue: "Chromosomes lined up across the middle: metaphase." No score.
**Add field** (enabled when a field is fully sorted): adds another field and pools the counts in the table (column
"Fields: 2"). **New field** replaces the current unsorted field. **Class data** box: a text area where the teacher
can paste other groups' five counts (comma separated) to pool them; nothing is saved.

**Grow the root** (differentiation). Stage: a root drawn in code from the side, tip at the bottom, with zones
labeled from the tip up: **Root cap**, **Dividing zone** (meristem), **Stretching zone** (elongation), **Maturing
zone** (with root hairs). **Grow** (or Space) runs one round: cells in the dividing zone divide (each into two,
a quick mitosis animation), the root tip moves down, older cells are pushed up into the stretching zone (they get
longer) and then the maturing zone (they become a cell type). Cell types: root cap cell, epidermis, root hair cell,
cortex, xylem (water pipe, thick walls), phloem (food pipe). Click any cell: a **Gene switchboard** opens with the
same six genes for every cell (genes for: dividing, root hair growth, thick pipe walls, food pipe parts, cap slime,
stretching), each shown on or off for that cell. A line under it: "Same DNA in every cell. Different genes are on."
**Compare two cells** puts two switchboards side by side.

## Content
Model cell cycle for the onion root tip (labeled "model, 24-hour cycle"): interphase 1,260 min, prophase 90,
metaphase 30, anaphase 15, telophase 45 (total 1,440; mitotic index 180/1,440 = 12.5 percent). Expected cells per
120: 105, 7.5, 2.5, 1.25, 3.75.
Field 1 (every student's first field) has exactly 105, 8, 2, 1, 4 cells (largest-remainder rounding of the
expected counts), so a correct full sort gives estimates of 1,260, 96, 24, 12 and 48 minutes and a mitotic index of
12.5 percent. Later fields draw each cell's phase from the model fractions with the seeded generator (field 2 uses
seed 2, and so on), so pooled counts wander and then settle near the model.
Phase cues (shown in bin cards and Check my sort):
- Interphase: round nucleus, evenly fine purple, a dark nucleolus dot; chromosomes not visible as threads.
- Prophase: thick threads (condensed chromosomes) inside a still-round nucleus; nucleolus gone.
- Metaphase: chromosomes lined up in a band across the middle of the cell.
- Anaphase: two groups of V-shaped chromosomes moving apart toward the ends.
- Telophase: two dark clumps at the ends; a new wall (cell plate) forming between them.
Onion cells have 16 chromosomes (2n = 16); the stain drawings show 16 threads in prophase and metaphase, and 16 in
each group in anaphase.
Gene switchboard table (on = 1): dividing cell 1 0 0 0 0 1; cap cell 0 0 0 0 1 0; stretching cell 0 0 0 0 0 1;
root hair cell 0 1 0 0 0 0; xylem 0 0 1 0 0 0; phloem 0 0 0 1 0 0; cortex and epidermis 0 0 0 0 0 0 (genes listed
in the order above; a model simplification of thousands of genes).
Hints: Count "<b>Count.</b> Click a cell, then a bin. Count every cell in the field, then read the time column." /
Grow "<b>Grow the root.</b> Press Grow a few times, then click two different cells and compare their genes."
Tips: "A phase seen in few cells is a short phase." / "Interphase is not resting: the cell copies its DNA then." /
"Mitosis makes two cells with the same chromosomes as the parent." / "Root tips divide fast, which is why the lab
uses them."
Model limits line: "Real cycle times change with temperature and with the plant. The 24-hour cycle and the phase
times here are model values, close to typical class results."
Lab note (real-world lab, shown in the Count info card): in a school lab this uses prepared slides or root tips
prepared by the teacher; goggles on, teacher handles the stain and acid.

## Interactions in detail
- Every cell is focusable (Tab moves through files in order, arrow keys move between neighbors); its accessible
  name says "Cell 37, not sorted" or "Cell 37, sorted as metaphase".
- Re-sorting a cell moves it between bins (counts update). Undo goes back one step (up to 50).
- Focus knob only blurs the drawing; sorting works at any blur. Zoom 100x shows all 120 at once (small cells).
- The table rounds minutes to whole numbers; fractions to 3 decimals; empty phases show 0 (and "no cells seen: shorter
  than our sample can show" when counted is 120 or more and a phase has 0).
- Grow animates divisions (400 ms) and pushes cells up (Motion off: instant). After 6 rounds the root scrolls so the
  tip stays in view.
- Mode change: `V.hush()`; sorting kept.

## Look
Accent `--brand #f1b1ed` (stain orchid), `--brand-ink #10161f`. Microscope field: background `#f3dbe8` (stained
tissue) inside a black eyepiece circle, cell walls `#c04b8a` (3.49:1 on the field: graphics only, never text),
chromatin `#7b3fa0` (5.26:1), condensed chromosomes `#3a2550` (10.32:1). Sorted-cell tags dark ink on white chips.
Grow the root drawn in muted greens and tans with zone labels in ink.
Contrast (computed): brand on --panel 10.10:1, on --sec-bg 9.57:1; brand-ink on brand 10.59:1. Nearest 9-12 accent
#c9b3ff (dE 17); in this group carrying-capacity's #e2a19c is the nearest (dE 35).

## Art
none: drawn in code (stained field, phases, root and zones).

## Voice
Bank `big-sister` (an older lab partner who has done this lab before): warm, practical, brief. Uses `Curio.voice`,
scope = mode.
- welcomeCount (how): "Welcome to Mitosis Mixer. Click a cell, then pick its phase. Count the whole field."
- welcomeGrow (how): "Grow the root. Press Grow a few times, then click a cell to see which genes are on."
- firstSort (how, first cell sorted): "Nice. Its number tag shows it's counted. Keep going across the files."
- fieldDone (event, each fully sorted field; stale on Add field): "Field done. Read the time column: the rare phases
  are the short ones."
- check (event, each Check my sort; stale on the next sort): "Dashed cells don't match. Click one to see the clue."
- compare (how, first switchboard): "Every cell has the same genes. Only the switches differ."

## Family engine
**cells** family. The engine is described in full in membrane-gatekeeper's spec (`kit/cells.js`). This tool feeds:
`Field` (n 120, files layout, seeded phase mix, an `exact` option for field 1, focus and zoom), `Phases` (stain
drawings for five phases with 16 chromosomes, plus cytokinesis cell plate), `CellView` stain style, and the
`Parts` nucleus and chromosomes. Grow the root is tool-local drawing that reuses `CellView` diagram style for the
six cell types. Seeded draws use `kit/probability.js` `Rand(seed)`.

## Sources
- Onion root tip lab, counting cells in each phase and estimating phase length from a 24-hour cycle: College Board,
  AP Biology Investigative Labs: An Inquiry-Based Approach (2012), Investigation 7 "Cell Division: Mitosis and
  Meiosis" (checked 2026-10-27).
- Phases of mitosis and their features, interphase as DNA copying: OpenStax Biology 2e, section 10.2 "The Cell
  Cycle" (CC BY 4.0), https://openstax.org/books/biology-2e/pages/10-2-the-cell-cycle
- Root zones (cap, meristem, elongation, maturation), root hairs, xylem and phloem: OpenStax Biology 2e, section
  30.3 "Roots", https://openstax.org/books/biology-2e/pages/30-3-roots
- Same genome in every cell, different genes expressed: OpenStax Biology 2e, section 16.1 "Regulation of Gene
  Expression".
- Allium cepa 2n = 16: Royal Botanic Gardens, Kew, Plant DNA C-values Database (verify confirms the entry).
- Lab safety for root tip squashes (goggles, teacher handles stain and hydrochloric acid): AP Biology Investigative
  Labs (2012), Investigation 7 safety notes.
- Phase times and gene switchboard: model values, labeled as such.

## Done when
1. Field 1 holds 120 cells: 105 interphase, 8 prophase, 2 metaphase, 1 anaphase, 4 telophase.
2. Sorting field 1 correctly gives times 1,260, 96, 24, 12 and 48 minutes and a mitotic index of 12.5 percent.
3. Check my sort marks a deliberately wrong cell and its click shows the right phase's cue.
4. Add field pools counts; after 10 fields the metaphase estimate is within about 15 minutes of 30.
5. Every cell can be sorted by keyboard alone (Tab or arrows, then 1 to 5); Undo works.
6. Grow the root: after 3 Grows new cells appear in the dividing zone and older ones show a type; any two different
   types show different switchboards over the same six genes.
7. Chromosome drawings show 16 in prophase and metaphase and two groups of 16 in anaphase.
8. Main controls visible at 1366x768 and 680x425; the field and bins work at 375 wide (bins under the field).
9. Each how-to line speaks once in five repeated actions; fieldDone speaks each finished field.
10. No images, no network, no em dashes.

## Open questions
- [mitosis-mixer] The field is drawn in code. Would real onion root tip micrographs (public domain or CC images)
  be worth adding later as an optional "real slide" view? They could not be checked against a true phase.
