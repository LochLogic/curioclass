# Industry Device Tour

## One idea
The child rides a tour bus with three stops, a dairy farm, a hospital imaging room and a car plant, and Rosa, the bus driver and tour host (made up, labeled "illustration"), lets the child pick the first stop; at each one the child taps a machine and it opens in four layers, input, storage, processing and output: the milking robot reads a cow's ID tag, looks up her milk record, decides whether she's due, and sends a sick-cow alert when her milk changes; the CT scanner takes hundreds of X-ray slices around a patient and the computer builds them into one 3D picture; the paint-inspection camera photographs every car door and flags the one in fifty with a drip; then each site's worker brings a real problem, the herd manager with 200 cows' records, the radiologist with thousands of images, the line lead whose doors keep failing, and the child picks the thinking move that cracked it, break it down, spot a pattern, or leave out details, and sees how it worked; at the end the child sees that every machine follows input, storage, processing and output, and that the people who run them use computational thinking without being programmers, so a student in grades 6 to 8 learns how devices and computational thinking show up in real jobs.

## Not like
- who-uses-this-device (K, spec): workers' devices for young kids. Here machines opened in layers.
- job-shadow-day (3, spec): a day of choices at one job. Here three industries and thinking moves.
- computing-team-stories (Grades 9-12, spec): the people on computing teams. Here machines and their workers.
- inside-the-keypress (3, spec): one laptop's signal path. Here industrial machines.

## Who and how
- Grades 6-8, Computer Science, module "Computing in Industry". Standards: MS-SOC-CE-44, MS-SYS-HW-31 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Devices and computational thinking in real jobs").
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every layer and card. Controls 48 px or more.
- Three sites, three machines with four layers each, three worker problems with three thinking moves. Extra: Tour guide (a student leads the class through one site on the projector). tool.json `modes: ["Tour", "Tour guide"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-SYS-HW-31 | Open each machine; order its four layers | input, storage, processing, output | 2 |
| MS-SOC-CE-44 | Match each worker's problem to a thinking move | how the move cracked it | 3 |

## Screens and modes
Header (kit): title "Industry Device Tour"; `Tour`, `Tour guide`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A tour bus window with three site cards, and Rosa at the wheel. The welcome is queued (`welcomeAfter: true`): "Three stops today. Tap your first stop." First hint: "Tap a site card."

**Site (focus: the machine).** At 1366x768 the site scene is left with the layer panel right; at 680x425 the panel is a sheet. Tapping the machine opens it; the four layer cards are shuffled and the child drags them into order, then watches one cow, patient or door go through.

**Worker problem.** The worker states the problem in one line; three thinking-move cards; the child picks one, then sees it work (sort the herd by one number, compare each slice to the one before, ignore everything but the drip).

**Back on the bus.** A stamp for the site; the next card glows.

**Same four layers (the aha).** Rosa: "Cows, scans or car doors, it's input, storage, processing, output. And nobody here calls themselves a programmer."

**The end.** A tour map with three stamps and the worker moves. `Print` prints them.

**Tour guide (extra).** One site, led by a student.

## Content
- Machines are generic, no brands; details are simplified and checked against sources.
- Worker problems are made up and labeled "illustration"; the machines are real types.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sites can be visited in any order and revisited; layers can be reordered until `Run it`.
- Keyboard: Tab to site cards, the machine, layer cards (arrows reorder), run and move cards; Enter opens or picks.
- With Motion off the bus doesn't drive; the next site appears.

## Look
- Accent `--brand` #a33a12 factory red-orange (header, layer tabs, buttons); gold #f4c542 (the layer in focus, stamps); paper #fcf1ec; ink #2b0e03; muted #5e4d46.
- Contrast (WCAG 2.1, computed): white on brand 6.62:1; brand on paper 5.97:1; ink on paper 16.23:1; muted on paper 7.21:1; ink on gold 11.07:1.
- Never color alone: layers carry names and icons; stamps carry the site name.
- Different from this batch (debugger amber, timeline navy, x-ray plum, test-kit green).

## Art
- People (illustrated): Rosa and three workers, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Local FLUX (`scripts/localart.py`): the bus window (1, 16:9), three sites (3, 16:9), three machine cutaways (3, 4:3).
- Drawn in code: layer cards, the data path, stamps and the map.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as Rosa; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.site + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `site`: "Tap a site card."
- how `open`: "Tap the machine to open it."
- how `order`: "Drag the four layers into order, then tap Run it."
- how `move`: "Pick the thinking move that cracked it."
- how `next`: "Tap the next stop."
- event, whole, same four layers.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: three machines as four-layer pipelines with a sample item, layer ordering, move demos.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Layers | Try every order | After two misses the child names each layer's job before trying again. |
| Moves | Pick the same move each time | Each worker's problem fits one move best and shows why the others stall. |
| Tour | Visit one site | The map needs three stamps. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `site`; `open`.
2. `order`.
3. `move`; `next`.
4. Same four layers (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Milking robots read each cow's ID, use her records to decide milking, and flag milk changes | Penn State Extension, "Automatic Milking Systems" | University of Minnesota Extension, "Robotic milking" | yes |
| CT scanners combine many X-ray slices into cross-section and 3D images | National Institute of Biomedical Imaging and Bioengineering, "Computed Tomography (CT)" | U.S. Food and Drug Administration, "What is Computed Tomography?" | yes |
| Camera systems inspect car paint for defects on the line | National Institute of Standards and Technology, machine vision in manufacturing | Society of Automotive Engineers, technical papers on automated paint defect inspection | yes |
| Decomposition, pattern recognition and abstraction as thinking moves | K-12 Computer Science Framework (2016), "Computational Thinking" | Wing (2006), "Computational Thinking", Communications of the ACM | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s25, 2026-11-10): one door in fifty is 2 percent, 20 doors in a 1,000-door shift; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 site and panel; at 680x425 panel as a sheet.
2. Three machines are opened and their layers ordered and run. (MS-SYS-HW-31)
3. Three worker problems are matched to thinking moves. (MS-SOC-CE-44)
4. The tour map shows three stamps.
5. No brands; workers are labeled illustration.
6. `Read` reads every layer and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the bus doesn't drive; no network requests.

## Open questions
None.
