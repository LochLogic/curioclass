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
**Count** (opens first). Focus: the microscope field. It is the biggest, central thing on the stage (at least 60
percent of the stage width in the wide layout, full width when stacked); the bins and table sit in the panel beside
it. Stage: a round eyepiece view (a circle on black) showing a stained onion root tip, 120 cells in neat files
(columns). Each cell is a painted cell tile (Art) placed by the cells engine `Field`; interphase cells use the
painted interphase tiles, dividing cells use the painted dividing tiles with their chromosomes drawn in code in stain
colors on top (so every count of 16 is exact). The painted tissue texture fills the gaps. A **Focus** knob (blur in,
sharp at the middle setting) and **Zoom** `.seg` **100x** / **400x** (400x shows a quarter of the field, pan by drag
or arrow keys) give the microscope feel; the starting state is 400x, in focus, top left.
Panel: five bins as buttons, **Interphase**, **Prophase**, **Metaphase**, **Anaphase**, **Telophase**, each with a
small reference drawing (code diagram) and its count. Sorting: click a cell (it gets an accent ring), then a bin (or
press 1 to 5). A sorted cell gets a small number tag of its bin (1 to 5) so the field shows progress; **Undo** last.
A **Data table** (`table.inst`): Phase, Cells counted, Fraction, Estimated time (minutes), filled live from the
counts: time = cells in phase / cells counted x 1,440 minutes. Above it: "Cells counted N of 120" and "Mitotic
index" (dividing cells / cells counted, as a percent).
**Check my sort** (any time): marks cells whose bin differs from the field's true phase (a small dashed outline),
and for each mismatch on click shows the cue: "Chromosomes lined up across the middle: metaphase." No score.
**Add field** (enabled when a field is fully sorted): adds another field and pools the counts in the table (column
"Fields: 2"). **New field** replaces the current unsorted field. A small painted photo of the classroom setup (an
onion on a jar of water, Art) sits in the Count info card with the lab note.

**Grow the root** (differentiation). Focus: the root diagram in the middle of the stage, tip at the bottom; the gene
switchboard opens beside it in the panel, never over the root. The root is a code diagram (its cells divide, stretch
and change type, so they must move and bend), drawn from the side with zones labeled from the tip up: **Root cap**,
**Dividing zone** (meristem), **Stretching zone** (elongation), **Maturing zone** (with root hairs). A small painted
inset at the top left (the onion on its jar, Art) with a code zoom box shows where this root tip is. **Grow** (or
Space) runs one round: cells in the dividing zone divide (each into two, a quick mitosis animation), the root tip
moves down, older cells are pushed up into the stretching zone (they get longer) and then the maturing zone (they
become a cell type). Cell types: root cap cell, epidermis, root hair cell, cortex, xylem (water pipe, thick walls),
phloem (food pipe). Click any cell: the **Gene switchboard** opens in the panel with that cell type's painted
micrograph portrait (Art) at the top and the same six genes for every cell (genes for: dividing, root hair growth,
thick pipe walls, food pipe parts, cap slime, stretching), each shown on or off for that cell. A line under it: "Same
DNA in every cell. Different genes are on." **Compare two cells** puts two switchboards side by side, each with its
portrait.

## Content
Model cell cycle for the onion root tip (labeled "model, 24-hour cycle"): interphase 1,260 min, prophase 90,
metaphase 30, anaphase 15, telophase 45 (total 1,440; mitotic index 180/1,440 = 12.5 percent). Expected cells per
120: 105, 7.5, 2.5, 1.25, 3.75.
Field 1 (every student's first field) has exactly 105, 8, 2, 1, 4 cells (largest-remainder rounding of the
expected counts; the tie between prophase and metaphase at 0.5 goes to the earlier phase), so a correct full sort
gives estimates of 1,260, 96, 24, 12 and 48 minutes and a mitotic index of 12.5 percent. Later fields draw each
cell's phase from the model fractions with the seeded generator (field 2 uses seed 2, and so on), so pooled counts
wander and then settle near the model.
Phase cues (shown in bin cards and Check my sort):
- Interphase: round nucleus, evenly fine purple, a dark nucleolus dot; chromosomes not visible as threads.
- Prophase: thick threads (condensed chromosomes) inside a still-round nucleus; nucleolus gone.
- Metaphase: chromosomes lined up in a band across the middle of the cell.
- Anaphase: two groups of V-shaped chromosomes moving apart toward the ends.
- Telophase: two dark clumps at the ends; a new wall (cell plate) forming between them.
Onion cells have 16 chromosomes (2n = 16); the code-drawn chromosomes show 16 threads in prophase and metaphase, and
16 in each group in anaphase.
Gene switchboard table (on = 1): dividing cell 1 0 0 0 0 1; cap cell 0 0 0 0 1 0; stretching cell 0 0 0 0 0 1;
root hair cell 0 1 0 0 0 0; xylem 0 0 1 0 0 0; phloem 0 0 0 1 0 0; cortex and epidermis 0 0 0 0 0 0 (genes listed
in the order above; a model simplification of thousands of genes).
Hints: Count "<b>Count.</b> Click a cell, then click its phase bin. Count every cell in the field, then read the
time column." / Grow "<b>Grow the root.</b> Press Grow a few times, then click two different cells and compare their
genes."
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
- Focus knob blurs the whole field layer (painted tiles and code chromosomes together, one CSS filter); sorting works
  at any blur. Zoom 100x shows all 120 at once (small cells).
- Tiles: each interphase cell picks one of three interphase tiles and each dividing cell one of three dividing tiles
  by the field seed, with a seeded flip (horizontal, vertical or both) so neighbors rarely match; files keep their
  column alignment. Tiles are scaled to the file width at real pixel size, not one fixed image scaled down.
- The table rounds minutes to whole numbers; fractions to 3 decimals; empty phases show 0 (and "no cells seen: shorter
  than our sample can show" when counted is 120 or more and a phase has 0; a random 120-cell field has no anaphase
  cell about 28 percent of the time, so this line will show).
- Grow animates divisions (400 ms) and pushes cells up (Motion off: instant). After 6 rounds the root scrolls so the
  tip stays in view. During the animation every control stays live: clicking a cell opens its switchboard at once
  (the cell's type as it will be after this round), and Grow pressed again finishes the running round at once and
  starts the next.
- Mode change: `V.hush()`; sorting kept.

## Look
Accent `--brand #f1b1ed` (stain orchid), `--brand-ink #10161f`. Microscope field: painted stained tissue inside a
black eyepiece circle; the code chromosomes and reference drawings use cell walls `#c04b8a` (3.49:1 on the field
color `#f3dbe8`: graphics only, never text), chromatin `#7b3fa0` (5.26:1), condensed chromosomes `#3a2550` (10.32:1).
The art prompt keeps the paint in the same pinks and purples so the code chromosomes sit in it. Sorted-cell tags dark
ink on white chips. Grow the root drawn in muted greens and tans with zone labels in ink; the painted onion inset and
cell portraits keep their natural colors in a thin accent frame.
Contrast (computed): brand on --panel 10.10:1, on --sec-bg 9.57:1; brand-ink on brand 10.59:1. Nearest 9-12 accent
#c9b3ff (dE 17); in this group carrying-capacity's #e2a19c is the nearest (dE 35); star-life-story #b894d0 (dE 16).

## Art
Local FLUX (`scripts/localart.py`), no people anywhere, house style "light microscope photo, stained plant tissue"
for the cell images and "natural photo" for the jar. 16 images.
- mm-interphase-a: a single plant cell seen under a light microscope, a rounded rectangle with a thin magenta wall,
  pale pink cytoplasm and a large round purple nucleus with one dark nucleolus dot in the center; 1:1; cutout yes;
  people no; one of three tiles for interphase cells in the field.
- mm-interphase-b: the same kind of cell, slightly taller rectangle, the nucleus a little left of center, fine even
  purple speckle in the nucleus; 1:1; cutout yes; people no; interphase tile.
- mm-interphase-c: the same kind of cell, slightly wider rectangle, a smaller round nucleus with a dark nucleolus
  dot; 1:1; cutout yes; people no; interphase tile.
- mm-dividing-a: a single plant cell seen under a light microscope, a rounded rectangle with a thin magenta wall,
  pale pink cytoplasm and a clear pale lilac center; 1:1; cutout yes; people no; dividing-cell tile, the code draws
  the chromosomes (and the telophase cell plate) on the clear center.
- mm-dividing-b: the same kind of cell, slightly taller, the clear center a little higher; 1:1; cutout yes; people
  no; dividing tile.
- mm-dividing-c: the same kind of cell, slightly wider, soft lilac haze across the clear center; 1:1; cutout yes;
  people no; dividing tile.
- mm-tissue: an even full-frame texture of stained plant tissue under a light microscope, soft pink and lilac
  mounting medium with a few faint blurred cell outlines; 1:1; cutout no; people no; tiled behind the cells inside
  the eyepiece circle.
- mm-onion-jar: a white onion resting on the mouth of a clear glass jar of water on a sunny classroom windowsill,
  many thin white roots hanging into the water; 3:4; cutout no; people no; Count info card and the Grow inset.
- mm-type-dividing: a light microscope view of small packed square plant cells with large nuclei, purple stain;
  1:1; cutout no; people no; switchboard portrait for a dividing (meristem) cell, shown at 96 px.
- mm-type-stretching: a light microscope view of long thin rectangular plant cells in neat rows with large pale
  vacuoles; 1:1; cutout no; people no; portrait for a stretching cell.
- mm-type-cap: a light microscope view of a rounded cap of loose plant cells at a root tip with a glossy slime
  edge; 1:1; cutout no; people no; portrait for a root cap cell.
- mm-type-epidermis: a light microscope view of a single neat outer layer of flat brick-shaped plant cells on a
  root surface; 1:1; cutout no; people no; portrait for an epidermis cell.
- mm-type-root-hair: a light microscope view of one root surface cell with a long thin hair growing out sideways;
  1:1; cutout no; people no; portrait for a root hair cell.
- mm-type-cortex: a light microscope view of large round loosely packed plant cells with small gaps between them;
  1:1; cutout no; people no; portrait for a cortex cell.
- mm-type-xylem: a light microscope view of a plant water pipe, a long open tube with thick walls ringed with spiral
  bands, stained red; 1:1; cutout no; people no; portrait for a xylem cell.
- mm-type-phloem: a light microscope view of a plant food pipe, long narrow cells joined end to end by sieve plates
  with tiny holes, stained green; 1:1; cutout no; people no; portrait for a phloem cell.
Drawn in code (diagrams that must be exact or move): chromosomes and the cell plate on the dividing tiles, bin
reference drawings, the root diagram with its dividing and stretching cells, the switchboard, tags and table.

## Voice
Bank `big-sister` (an older lab partner who has done this lab before): warm, practical, brief. Uses `Curio.voice`,
scope = mode.
- welcomeCount (how; when Count is entered; stale once a cell is sorted): "Welcome to Mitosis Mixer. Click a cell,
  then click its phase bin on the right. Count the whole field."
- firstSort (how; the first cell sorted; stale when another cell is selected): "Nice. Its number tag shows it's
  counted. Click the next cell in the file."
- fieldDone (event; each fully sorted field; stale on Add field or New field): "Field done. Read the time column:
  the rare phases are the short ones. Press Add field for more data."
- check (event; each Check my sort with at least one mismatch; stale on the next sort): "Dashed cells don't match.
  Click one to see the clue."
- checkClean (event; each Check my sort with no mismatch; stale on the next sort): "Every sorted cell matches."
- welcomeGrow (how; when Grow the root is entered; stale once Grow is pressed): "Grow the root. Press Grow a few
  times, then click a cell to see which genes are on."
- compare (how; the first switchboard opened; stale when it closes): "Every cell has the same genes. Only the
  switches differ. Press Compare two cells, then click a second cell."

## Family engine
**cells** family. The engine is described in full in membrane-gatekeeper's spec (`kit/cells.js`). This tool feeds:
`Field` (n 120, files layout, seeded phase mix, an `exact` option for field 1, focus and zoom, and a `tiles` option:
per-phase lists of painted tile images plus a draw hook so the engine places the tile and the code draws the
chromosomes on top), `Phases` (stain drawings for five phases with 16 chromosomes, plus the cytokinesis cell plate),
`CellView` stain style for the bin reference drawings, and the `Parts` nucleus and chromosomes. Grow the root is
tool-local drawing that reuses `CellView` diagram style for the six cell types. Seeded draws use `kit/probability.js`
`Rand(seed)`; that file does not exist yet, so if it is still missing at build, put a seeded generator (mulberry32)
in the engine block and name it `Rand`.

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
- Number checks (Python, 2026-10-29): expected counts per 120 are 105, 7.5, 2.5, 1.25, 3.75; largest remainder
  gives 105, 8, 2, 1, 4 (telophase 0.75 first, then the prophase and metaphase tie at 0.5 broken by phase order);
  times 1,260, 96, 24, 12, 48 minutes; mitotic index 15/120 = 12.5 percent. Pooling: with a mulberry32 stand-in for
  `Rand`, over 1,000 seed sets the metaphase estimate after 10 fields (field 1 plus 9 random) was more than 15
  minutes off 30 in 4 sets (worst 19.2), after 5 fields in 45 sets, after 20 fields in 0; seeds 2 to 10 pooled gave
  1,030, 83, 33, 8, 46 cells and a metaphase estimate of 40 minutes (passes). A random 120-cell field has no
  anaphase cell with probability 0.28.

## Done when
1. Field 1 holds 120 cells: 105 interphase, 8 prophase, 2 metaphase, 1 anaphase, 4 telophase.
2. Sorting field 1 correctly gives times 1,260, 96, 24, 12 and 48 minutes and a mitotic index of 12.5 percent.
3. Check my sort marks a deliberately wrong cell and its click shows the right phase's cue.
4. Add field pools counts; after 10 fields (seeds 2 to 10) the metaphase estimate is within 15 minutes of 30. If
   the real `Rand` misses, report the seeds rather than changing the model.
5. Every cell can be sorted by keyboard alone (Tab or arrows, then 1 to 5); Undo works.
6. Grow the root: after 3 Grows new cells appear in the dividing zone and older ones show a type; any two different
   types show different switchboards and different painted portraits over the same six genes.
7. Code chromosomes show 16 in prophase and metaphase and two groups of 16 in anaphase, sitting inside the painted
   dividing tiles; interphase tiles carry no code chromosomes; the Focus knob blurs tiles and chromosomes together.
8. Focus: in Count the eyepiece field is the largest thing on screen at 1366x768 and 680x425, with the bins beside
   it; in Grow the root the switchboard never covers the root.
9. A tap while Grow animates: clicking a cell opens its switchboard at once, and a second Grow finishes the round and
   starts the next with no wait.
10. Main controls visible at 1366x768 and 680x425; the field and bins work at 375 wide (bins under the field).
11. Each how-to line speaks once in five repeated actions; fieldDone speaks each finished field; no line names a
    disabled control (Add field is only named once the field is done).
12. No network, no em dashes; all 16 images load and none shows a person.

## Open questions
- [mitosis-mixer] The Class data box (a teacher pastes other groups' counts) was removed under the "no moving work
  between devices by hand" rule; Add field still pools many fields on one laptop. Bring back a class pool another
  way, or leave it to the teacher's whiteboard?
- [mitosis-mixer] Painted cell tiles carry the stain look; the chromosomes stay in code so 16 is exact. Would real
  onion root tip micrographs (public domain or CC images) be worth adding later as an optional "real slide" view?
  They could not be checked against a true phase.
