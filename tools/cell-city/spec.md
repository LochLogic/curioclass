# Cell City

## One idea
At a microscope bench the student views seven real micrographs (onion skin, cheek cells, pond water with single-celled life, a leaf, cork, sand and a plastic shaving), decides for each whether it is made of cells and whether it is one cell or many of different kinds, then zooms from a whole body through the digestive system, the stomach and its lining down into one cell, where each part (membrane, nucleus, mitochondria, cytoplasm, and for a plant cell the wall, vacuole and chloroplasts) is shown as it really looks and the student matches each to its job by watching what stops when that part is switched off; a "city view" switch adds a power plant, city hall and city wall overlay with a note on where the comparison breaks down; at the end a body task (run up a flight of stairs) lights up the muscles, lungs, heart and nerves working together and the student builds an argument with evidence from the zoom, so a sixth grader learns that living things are made of cells, one or many and of different types, how the parts of a cell help it work, and that the body is a system of interacting subsystems made of groups of cells.

## Not like
- membrane-gatekeeper (9, spec): what crosses a cell membrane. Here what cells are and how they build a body.
- mitosis-mixer (9, spec): how cells divide. Here what a cell's parts do.
- how-animals-see (3 to 5, live): eyes and senses. Here every body level from system to organelle.
- particle-zoom (5, spec): zooming into matter's particles. Here zooming into living things.

## Who and how
- Grade 6, Science, module "Cells and Body Systems". Standards: MS-LS1-1 (conduct an investigation to provide evidence that living things are made of cells; either one cell or many different numbers and types of cells), MS-LS1-2 (develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function), MS-LS1-3 (use argument supported by evidence for how the body is a system of interacting subsystems composed of groups of cells).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Seven samples, five zoom levels (system, organ, tissue, cell, organelle), an animal cell and a plant cell with switch-off tests, the city view, the stair run, the argument card. Extra: Sample sheet (a printable sheet for a real microscope day). tool.json `modes: ["Explore", "Sample sheet"]`, `minutes: "30-40"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS1-1 | Sort seven micrographs: cells or not, one or many, kinds | the micrograph; the bench log | 2 |
| MS-LS1-2 | Switch off one part at a time and match it to its job | the cell; what stops; the parts table | 3 |
| MS-LS1-3 | Zoom through the levels and argue from the stair run | the zoom path; the lit systems; the argument card | 4 |

## Screens and modes
Header (kit): title "Cell City"; `Explore`, `Sample sheet`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A lab bench with a microscope and a tray of seven slides; beside it a body figure with see-through system layers. The welcome is queued (`welcomeAfter: true`): "Is everything alive made of the same tiny pieces? Let's look. Drag a slide under the microscope." First hint: "Drag the onion slide onto the microscope."

**The bench (focus: the micrograph).** At 1366x768 the micrograph fills a round eyepiece on the left with the log right; at 680x425 the log is a sheet. The student turns the focus knob, then answers three cards: Made of cells? One cell or many? One kind or several? The scale bar shows the size (a cheek cell is about 60 micrometers across). Cork shows empty boxes: the cells Robert Hooke named in 1665, no longer alive. Sand and plastic show no cells.

**The zoom (focus: one level at a time).** Tap the stomach on the body figure; the view zooms in five steps with a breadcrumb: digestive system, stomach, stomach lining tissue, one lining cell, its parts. Each level names its job in one line ("Tissue: many cells of one kind doing one job together").

**Inside the cell (MS-LS1-2).** The cell as it looks under an electron microscope first, drawn plainly. Tap a part to name it; then tap `Switch off` on that part and watch what stops (mitochondria off: the cell runs out of energy and its pumps slow; membrane off: the inside leaks; nucleus off: no new instructions, repairs stop). The student drags each part to its job in the parts table. A plant cell toggle adds the wall, the big vacuole and chloroplasts, with sunlight.

**City view.** A switch overlays a city: mitochondria as power plants, nucleus as city hall, membrane as the city wall with gates. A note: "A city plans on purpose; a cell does not. And a power plant doesn't make itself."

**The stair run (the aha).** The body figure runs up stairs; muscles, lungs, heart and nerves light up with a line each (nerves signal, muscles pull, lungs bring in oxygen, the heart pumps it). The student fills an argument card: "The body is a system of systems because ___. My evidence from the zoom: ___." Narrator: "Every step you take is trillions of cells, grouped into tissues and organs, working together."

**The end.** The bench log, the parts table and the argument on one page. `Print` prints it.

**Sample sheet (extra).** A printable page for a real microscope day: the same seven samples with blank sort boxes.

## Content
- Seven micrographs (openly licensed, licenses recorded), five zoom levels for the stomach path, an animal cell with 4 parts and a plant cell with 3 more, switch-off results for each, the city overlay with its limit note, the stair-run systems, the argument card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The zoom always shows a breadcrumb; tapping any level jumps there.
- Keyboard: Tab to slides, the focus knob, sort cards, zoom levels, cell parts, `Switch off` and the table; Enter selects.
- With Motion off zooms cut between levels and the stair run shows still frames.

## Look
- Accent `--brand` #2f6b3a cell green (header, the breadcrumb, the parts table); gold #f4c542 (the selected part, the part switched off); paper #f1f7f1; ink #0d1f10; muted #4b5a4d.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.88:1; ink on paper 15.82:1; muted on paper 6.73:1; ink on gold 10.58:1.
- Never color alone: cell parts carry labels and outlines; lit systems carry names.
- Different from this batch (schoolyard brick, current blue, strata plum, magma red).

## Art
- Micrographs: openly licensed or public domain images (CDC Public Health Image Library, NIH, Wikimedia Commons with license checked and recorded) (7, 1:1).
- Local FLUX (`scripts/localart.py`): the lab bench (1, 16:9), the body figure with system layers (1, 3:4), the city overlay (1, 16:9).
- Drawn in code: the zoom levels, the cell and its parts, the parts table, the stair run.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the lab guide at the bench; `upbeat-guide` as the zoom guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.part + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `slide`: "Drag the next slide onto the microscope."
- how `sort`: "Tap your answer on each card."
- how `zoom`: "Tap the stomach on the body to zoom in."
- how `part`: "Tap a part, then tap Switch off."
- event, whole, each switch-off result.
- event, whole, the stair run.
- how `argue`: "Fill in the argument card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
cells (family "cells"; no engine file yet). This tool builds the cells family's shared pieces first, in a marked block `/* CELLS DATA: begin */ ... /* end */`: the zoom path with levels and breadcrumb, cell part records (name, job, switch-off result, plant only or not) and micrograph records with licenses, so later cells tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Bench | Say "cells" for every slide | Sand and plastic fail, and the log asks what was seen. |
| Parts | Drag parts to jobs at random | Each wrong match replays that part's switch-off result. |
| Argument | Write one word | The card needs evidence from at least two zoom levels. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `slide`; `sort`.
2. `zoom`; `part`.
3. Switch-off result (whole), waits.
4. Stair run (whole), waits. `argue`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS1-1, MS-LS1-2, MS-LS1-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Robert Hooke named cells from cork in Micrographia (1665) | Royal Society, "Micrographia" collection | University of California Museum of Paleontology, "Robert Hooke" | yes |
| Jobs of membrane, nucleus, mitochondria, cell wall, vacuole and chloroplasts | National Human Genome Research Institute, "Talking Glossary" | OpenStax, "Biology 2e", chapter 4 | yes |
| A human cheek cell is about 60 micrometers across | OpenStax, "Biology 2e", chapter 4 (cell sizes) | Nikon MicroscopyU, "Cheek cell" gallery notes | yes |
| Body levels: cells, tissues, organs, organ systems | OpenStax, "Anatomy and Physiology 2e", chapter 1 | NIH National Cancer Institute SEER Training, "Body organization" | yes |
| Exercise uses muscle, nervous, respiratory and circulatory systems together | NIH National Heart, Lung, and Blood Institute, "How the Lungs Work" | OpenStax, "Anatomy and Physiology 2e", exercise and the heart | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-10): seven samples, five made of cells and two not; five zoom levels; four parts in the animal cell plus three plant parts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 eyepiece and log; at 680x425 sheet.
2. Seven samples are sorted for cells, number and kinds. (MS-LS1-1)
3. Every part is switched off and matched to its job, in an animal and a plant cell. (MS-LS1-2)
4. The zoom is walked and an argument with evidence from two levels is made. (MS-LS1-3)
5. Every micrograph's license is recorded and checked.
6. The city view shows its limit note.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: cuts and still frames; no network requests.

## Open questions
- The idea card flags a data source (default used: seven micrographs from the CDC Public Health Image Library, NIH and Wikimedia Commons, each license checked and recorded before build).
