# Fossil and Bone Bench

## One idea
A museum prep bench holds three trays of evidence and a notebook; at the first tray the student places five whale-family fossils into rock layers by age (Pakicetus, a wolf-sized land animal about 50 million years old; Ambulocetus, a walking and swimming animal; Rodhocetus, with shorter legs; Dorudon, fully at sea with tiny back legs about 40 million years ago; and a modern whale with hip bones left inside), and notices the pattern: legs shrink, nostrils move up the head, the body becomes built for swimming; at the second tray the student lays a whale flipper, a bat wing and a human arm side by side and drags color-coded labels onto the same five bone groups in each (upper arm, two forearm bones, wrist, fingers), seeing one plan bent to three jobs; at the third tray the student compares accurate photos of early embryos of a fish, a chicken, a mouse and a human, spots the shared pharyngeal arches and tail, and watches them grow apart into gills, jaws and ears; at the end the notebook holds three kinds of evidence pointing the same way, so an eighth grader learns to analyze patterns in the fossil record, to compare anatomy to infer relationships, and to compare embryos across species to find similarities not seen in the adults.

## Not like
- fossil-clues (3, spec): fossils as clues to old places. Here fossils as clues to change in life forms.
- earth-s-calendar (6, spec): fossils used to build the time scale. Here fossils, bones and embryos showing relationships.
- bug-hunt (8, spec): natural selection in action. Here the evidence for shared ancestry.
- gene-pool (8, concept): how traits pass on. Here how bodies record their history.

## Who and how
- Grade 8, Science, module "Evidence of Common Ancestry". Standards: MS-LS4-1 (analyze and interpret data for patterns in the fossil record that document the existence, diversity, extinction, and change of life forms throughout the history of life on Earth), MS-LS4-2 (apply scientific ideas to construct an explanation for the anatomical similarities and differences among modern organisms and between modern and fossil organisms to infer evolutionary relationships), MS-LS4-3 (analyze displays of pictorial data to compare patterns of similarities in the embryological development across multiple species to identify relationships not evident in the fully formed anatomy).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Tray 1: five fossils, five layers. Tray 2: three limbs, five bone groups, 15 labels. Tray 3: four embryos at three stages. The notebook. Extra: Horse line (a second fossil series, from a small forest horse to today's horse). tool.json `modes: ["Bench", "Horse line"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS4-1 | Place five fossils in layers by age and name the pattern | the layered column; the trait chart | 2 |
| MS-LS4-2 | Label the same five bone groups in three limbs and a fossil limb | the limbs side by side; the labels | 3 |
| MS-LS4-3 | Match shared embryo features and watch them grow apart | the embryo grid; the stage slider | 4 |

## Screens and modes
Header (kit): title "Fossil and Bone Bench"; `Bench`, `Horse line`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A museum prep room with a long bench, three trays under cloths, a notebook open to an empty three-column table. The welcome is queued (`welcomeAfter: true`): "Three trays, three kinds of evidence. Start with the rocks. Tap the first tray." First hint: "Tap tray 1."

**Tray 1, fossils (focus: the column).** At 1366x768 the tray is left with the notebook right; at 680x425 the notebook is a sheet. A rock column with five layers, each with an age. The student drags each fossil skeleton (cast photos and labeled drawings) to its layer. A trait chart fills: legs, nostril position, ear bones, tail. The student taps the pattern: "legs got smaller", "nostrils moved back", "became sea animals". A note: "These are a few fossils from many. The record has gaps."

**Tray 2, bones (focus: the limbs).** A whale flipper, a bat wing and a human arm (with a Rodhocetus leg as a fossil comparison). Five label colors with names: upper arm, forearm (two bones), wrist, fingers. The student drags labels to each limb. All three snap into the same plan. A card: "Same bones, different jobs. Why would a flipper have finger bones?"

**Tray 3, embryos (focus: the grid).** Four columns (fish, chicken, mouse, human), three rows (early, middle, late), from accurate modern photos. The student taps the shared features at the early stage (pharyngeal arches, a tail) and drags the stage slider; the arches become gills in the fish and parts of the jaw and ear in the others. A note: "Old drawings from the 1800s made embryos look more alike than they are. These are photos."

**The notebook (the aha).** Three columns, one per tray, each with a line of evidence. Narrator: "Rocks, bones and embryos. Three different kinds of evidence, and they all point to shared ancestors."

**The end.** The notebook. `Print` prints it.

**Horse line (extra).** A second series: Eohippus to today's horse, toes and teeth changing as forests became grasslands.

## Content
- Five whale-family fossils with ages and traits, three modern limbs and one fossil limb with bone groups, four species at three embryo stages from cited photo sources, five horse-line fossils for the extra, the notebook.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Trays can be done in any order; the notebook needs all three.
- Keyboard: Tab to fossils, layers, labels, bones, embryo cells and the slider; Enter places; arrows move the slider.
- With Motion off the stage slider jumps between three stills.

## Look
- Accent `--brand` #6b4e2a bone tan (header, the notebook, tray frames); gold #f4c542 (the item in hand, shared features); paper #f9f5ee; ink #1f160a; muted #5c5448.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 7.03:1; ink on paper 16.41:1; muted on paper 6.86:1; ink on gold 10.97:1.
- Never color alone: bone labels carry names and patterns as well as colors.
- Different from this batch (radio navy, orchid, safety orange, town green).

## Art
- Fossil casts and skeletons: openly licensed museum photos, checked, or labeled drawings (5, 4:3).
- Limbs: drawn in code from cited diagrams (4).
- Embryos: openly licensed photos from cited sources, checked, licenses recorded (12, 1:1).
- Local FLUX (`scripts/localart.py`): the prep room (1, 16:9).
About 18 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the museum scientist; `knowing-guide` as hints. `Curio.voice` with `scope: () => state.mode + ':' + state.tray + ':' + state.item + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `fossil`: "Drag each fossil to its layer."
- how `pattern`: "Tap the pattern you see."
- how `bones`: "Drag each label onto the matching bones."
- how `embryo`: "Tap a shared feature, then drag the stage slider."
- event, whole, each tray's finish.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the column, labels, the embryo grid. Fossil records sit in a marked block `/* FOSSIL-BENCH DATA: begin */ ... /* end */`, shaped like the FOSSILS DATA records in fossil-clues so they can be shared later.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Layers | Drop fossils anywhere | Each snaps only to the layer matching its age. |
| Bones | Label by color guess | Labels snap only to the right bone group. |
| Embryos | Tap everything | Only shared features count; others show what they are. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `fossil`; `pattern`.
2. Tray finish (whole), waits. `bones`.
3. Tray finish (whole), waits. `embryo`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS4-1, MS-LS4-2, MS-LS4-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Pakicetus about 50 million years old to Dorudon about 40; legs shrink and nostrils move | Smithsonian National Museum of Natural History, "Whale evolution" | University of California Museum of Paleontology, "The evolution of whales" | yes |
| Whale flipper, bat wing and human arm share the same bone groups | University of California Museum of Paleontology, "Homologies" | OpenStax, "Biology 2e", chapter 18 | yes |
| Vertebrate embryos share pharyngeal arches and a tail early | OpenStax, "Biology 2e", chapter 18 | Smithsonian National Museum of Natural History, "Human origins: embryos" | yes |
| Haeckel's 1800s drawings exaggerated embryo likeness | Richardson and colleagues (1997), Anatomy and Embryology | University of California Museum of Paleontology, "Haeckel" | yes |
| Horse series from small forest animals to modern horses | American Museum of Natural History, "Horse evolution" | Florida Museum of Natural History, "Fossil horses" | yes |
Backed twice: 6. Cut: 0.

Sensitivity note: common ancestry can be a sensitive topic in some families. The tool presents evidence the way NGSS asks, says nothing about anyone's beliefs, and uses accurate embryo photos rather than old exaggerated drawings.

Checks run (Python, scratchpad r4, 2026-11-10): five bone groups in three limbs is 15 labels; Pakicetus to Dorudon spans 10 million years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tray and notebook; at 680x425 sheet.
2. Five fossils are placed by age and the pattern named. (MS-LS4-1)
3. Fifteen labels are placed on three limbs and the fossil limb compared. (MS-LS4-2)
4. Shared embryo features are found and followed through three stages. (MS-LS4-3)
5. Every image has a checked license or a drawing label; no Haeckel drawings.
6. The gaps note and the old-drawings note show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: three stills; no network requests.

## Open questions
- Overlap risk with fossil-clues (default used: fossil-clues keeps fossils as clues to past environments for grade 3; this tool uses fossils, bones and embryos as evidence of change and shared ancestry).
- Sensitivity flag: evolution and common ancestry (default used: evidence-first framing as NGSS asks, no comment on beliefs, accurate embryo photos only, fresh-agent read before build).
