# Puppy Traits

## One idea
A family photo shows a mother dog, a father dog and six puppies, each with trait tags (coat color, spots, ear shape, size, knowing tricks, weight), and the student inspects each puppy beside its parents, fills a trait table and a bar chart (how many have floppy ears, how many have spots), and sees that the litter is alike but not the same; then two sisters go to different homes for a year, one with long walks and good food and one with little exercise, and one learns tricks, and the student marks which differences came from parents and which came from food, training and where they live; two sunflower seeds from the same plant grow in sun and in shade to show the same thing in plants; then in the wild, deer mice live on pale sand hills and on dark soil, each litter varies in coat color, an owl spots the mice that don't match the ground first, and over ten generations the student watches pale coats become common on pale sand and dark coats on dark soil; at the end a sorted trait board holds the evidence and an explanation card says why pale mice do better on pale sand, so a third grader learns that traits are inherited from parents and vary in a group, that the environment can shape traits, and that small differences can help some individuals survive.

## Not like
- who-s-my-baby (1, spec): young look like but not exactly like parents. Here sorting why, with data.
- trait-lab (12, spec): genes and crosses. Here traits you can see.
- life-cycle-wheel (3, spec): stages of a life. Here differences within a family.
- fossil-clues (3, spec): environments over deep time. Here survival over a few generations.

## Who and how
- Grade 3, Science, module "Traits and Variation". Standards: 3-LS3-1 (analyze and interpret data to provide evidence that plants and animals have traits inherited from parents and that variation of these traits exists in a group of similar organisms), 3-LS3-2 (use evidence to support the explanation that traits can be influenced by the environment), 3-LS4-2 (use evidence to construct an explanation for how the variations in characteristics among individuals of the same species may provide advantages in surviving, finding mates, and reproducing).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The litter of six with five traits, the two-homes story, the sunflowers, the mice over ten generations, the trait board and explanation card. Extra: Class litter (the class tallies traits together). tool.json `modes: ["Litter", "Class litter"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-LS3-1 | Inspect six puppies beside their parents and fill a table and chart | the trait table; the bar chart | 2 |
| 3-LS3-2 | Mark which year-later differences came from the home, and compare sun and shade sunflowers | the two sisters; the two sunflowers | 3 |
| 3-LS4-2 | Watch ten generations of mice on two grounds and explain the change | the generation chart; the explanation card | 4 |

## Screens and modes
Header (kit): title "Puppy Traits"; `Litter`, `Class litter`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A family photo: a mother dog, a father dog and six puppies on a porch. The welcome is queued (`welcomeAfter: true`): "Six puppies, one family. What did they get from their parents? Tap a puppy to look closer." First hint: "Tap a puppy."

**The litter (focus: the puppy).** At 1366x768 the puppy fills the left with the table and chart right; at 680x425 the table is a sheet. Each puppy shows its coat color, spots, ear shape and size next to both parents. The student taps the matching trait in the table. The chart fills as they go: in this litter four of six have floppy ears and two of six have spots. A card asks "Are the puppies all the same?" and the answer comes from the chart.

**Two homes (3-LS3-2).** Two sisters grow up for one year. One gets long walks and good food and learns three tricks; one gets little exercise and too many treats. A year later: same coat, same ears, but different weight, and only one knows tricks. The student sorts each trait into "came from parents" or "shaped by food, training and home". Then two sunflower seeds from one plant: the one in sun grows tall, the one in shade stays short.

**The mice (3-LS4-2).** Deer mice on pale sand hills and on dark forest soil. Each litter varies from pale to dark. An owl flies over (shown swooping, never catching on screen); the tally shows that mice that match the ground are spotted less. A chart shows ten generations: pale coats become common on sand and dark coats on soil. A note says real scientists tested this with clay model mice and found owls and other hunters attacked the mismatched ones more.

**The trait board (the aha).** Every trait sorted with its evidence, and an explanation card: "Pale mice do better on pale sand because ___." Narrator: "Puppies get traits from their parents, but they're not all the same. Their homes shape them too. And in the wild, a small difference can be the reason one mouse lives to have babies."

**The end.** The board and the card. `Print` prints them.

**Class litter (extra).** The class tallies the litter's traits together.

## Content
- Six puppies and two parents (made-up mixed-breed family), five traits, the two-homes story, two sunflowers, the mouse model with a stated rule, the board and card.
- The owl is never shown catching a mouse; the tally counts mice spotted.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each sort can be changed until the board is checked.
- Keyboard: Tab to puppies, table cells, the sort bins and the generation slider; arrow keys move the slider; Enter picks.
- With Motion off the owl does not fly and generations step without moving.

## Look
- Accent `--brand` #2f6b3a collar green (header, the table, the board); gold #f4c542 (the puppy in focus, the chosen trait); paper #f1f7f2; ink #0b1f0f; muted #4f5a51.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.88:1; ink on paper 15.88:1; muted on paper 6.63:1; ink on gold 10.61:1.
- Never color alone: traits carry words; chart bars carry numbers; coat shades carry the words pale, medium, dark.
- Different from this batch (magnet red, postcard orange, ocean navy, lane indigo).

## Art
- Local FLUX (`scripts/localart.py`): the dog family on a porch (1, 16:9), six puppy close-ups (6, 1:1), the two sisters a year later (2, 1:1), sunflowers in sun and shade (2, 3:4), mice on sand and on soil (2, 16:9), an owl swooping (1, 4:3).
- Drawn in code: the table, chart, sort bins, generation chart, board.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as the puppies' owner; `big-sister` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.pup + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `inspect`: "Tap the trait that matches this puppy."
- event, whole, the chart's answer.
- how `sort`: "Drag each trait to where it came from."
- how `generations`: "Tap Next generation and watch the chart."
- event, whole, the generation result.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the trait table, chart, sort, the mouse generation model.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Table | Tap any trait | Each cell checks against the puppy's picture. |
| Sort | Put everything in "from parents" | Weight and tricks check against the two-homes story. |
| Explanation | Leave it blank | The card needs a reason that names matching the ground. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `inspect`; chart (whole), waits.
2. `sort`.
3. `generations`; result (whole).
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-LS3-1, 3-LS3-2, 3-LS4-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Offspring inherit traits and vary within a litter | University of Utah Genetic Science Learning Center, "Heredity and Traits" | National Human Genome Research Institute, "Trait" (glossary) | yes |
| Diet, exercise and training change weight and behavior | American Veterinary Medical Association, "Pet obesity" | Cornell University College of Veterinary Medicine, "Feeding your dog" | yes |
| Sunflowers grown in shade grow differently from those in sun | University of Illinois Extension, "Sunflowers" | Royal Horticultural Society, "Sunflowers" | yes |
| Deer mice coat color matches local soil; mismatched models are attacked more | Vignieri, Larson and Hoekstra, Evolution (2010) | Barrett and colleagues, Science (2019) | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r28, 2026-11-09): four of six floppy-eared puppies is about 67 percent and two of six spotted is about 33 percent; ten generations on two grounds; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 puppy and table; at 680x425 sheet.
2. Six puppies are compared with parents in a table and chart showing variation. (3-LS3-1)
3. Traits are sorted by parents or home, with sunflowers as plant evidence. (3-LS3-2)
4. Ten generations of mice show matching coats becoming common, with an explanation. (3-LS4-2)
5. The owl never catches a mouse on screen.
6. The clay model study is described accurately.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flying owl; no network requests.

## Open questions
None.
