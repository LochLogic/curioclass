# Gene Pool

## One idea
In a garden bed of woodland strawberries (a wild strawberry with two copies of each gene, simpler than the garden kind) one mother plant sends out runners and flowers, and the rows each have their own sun and water settings; the student plants runner babies in a sunny row and a shady row and finds they have identical genes in the gene view but grow to different sizes, so the environment shows; then flowers are pollinated by a second plant and the student plants the seeds, and every seedling's gene view shows a new mix of one copy from each parent (four possible mixes for each gene), so seedlings vary while runners copy; a mutation event changes one letter in the gene that switches on red color, the protein view shows the switch protein's shape change, the fruit turns pale, and the student judges whether that change is harmful, helpful or neutral in this garden (birds skip pale berries, so here it may help); then over four breeding rounds the student chooses which plants to cross to get bigger, sweeter berries, and an info card explains how genetic engineering differs from choosing parents; at the end a garden journal holds the evidence, so an eighth grader learns how environment and genes affect growth, how a gene change can change a protein and a trait, why asexual reproduction makes identical offspring and sexual reproduction makes variation, and how people use technology to change inherited traits.

## Not like
- punnett-predictor (9, spec): probability of trait combinations. Here clones, seeds, mutation and breeding in one garden.
- protein-factory (9, spec): reading codons into proteins. Here one gene change and its effect on a plant.
- bug-hunt (8, spec): natural selection in a population. Here people choosing parents.
- flower-lure (8, spec): structures that win pollinators. Here what pollination passes on.

## Who and how
- Grade 8, Science, module "Reproduction and Heredity". Standards: MS-LS1-5 (construct a scientific explanation based on evidence for how environmental and genetic factors influence the growth of organisms), MS-LS3-1 (develop and use a model to describe why structural changes to genes (mutations) located on chromosomes may affect proteins and may result in harmful, beneficial, or neutral effects to the structure and function of the organism), MS-LS3-2 (develop and use a model to describe why asexual reproduction results in offspring with identical genetic information and sexual reproduction results in offspring with genetic variation), MS-LS4-5 (gather and synthesize information about the technologies that have changed the way humans influence the inheritance of desired traits in organisms).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One mother plant, three rows (full sun, half shade, shade), a gene view with three genes (size, sweetness, red color), a protein view, the mutation event, four breeding rounds, the engineering card, the garden journal. Extra: Strawberry history (how two wild American strawberries crossed in an 1700s French garden became the garden strawberry). tool.json `modes: ["Garden", "Strawberry history"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS1-5 | Grow identical runners in different rows and compare sizes | the rows; identical gene views; size labels | 2 |
| MS-LS3-2 | Compare runners with seedlings in the gene view | copies on runners; mixes on seedlings | 3 |
| MS-LS3-1 | Trigger the mutation and judge its effect | the letter change; the protein shape; the pale fruit | 4 |
| MS-LS4-5 | Run four breeding rounds and read the engineering card | the berry chart by round; the card | 5 |

## Screens and modes
Header (kit): title "Gene Pool"; `Garden`, `Strawberry history`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A raised garden bed in morning light, a mother strawberry plant with runners snaking out, three rows with sun and water labels. A garden journal on a stool. The welcome is queued (`welcomeAfter: true`): "This plant can make babies two ways. Let's see what each way passes on. Drag a runner into the sunny row." First hint: "Drag a runner into the sunny row."

**Runners (focus: the rows).** At 1366x768 the bed is left with the gene view right; at 680x425 the gene view is a sheet. Runners planted in three rows grow over a fast-forward; sizes differ. Tap any plant: the gene view shows two copies of each of three genes, the same on every runner.

**Seeds.** A bee visits; a second plant's pollen arrives. The student plants five seeds. Each seedling's gene view shows one copy from each parent, mixed differently. The journal asks: "Why are runners all the same but seedlings different?"

**Mutation (focus: the protein).** A card: "One seed has a change." The red-color gene shows one letter changed; the protein view shows the switch protein folding differently; the berries come out pale. The student picks harmful, helpful or neutral and gives a reason; the card notes it depends on the setting.

**Breeding.** Four rounds: pick two parents, plant seeds, keep the best. A chart shows berry size and sweetness rising. The engineering card explains that breeders choose parents, while genetic engineering changes a gene directly in a lab.

**The journal (the aha).** Four pages of evidence. Narrator: "Genes set what a plant can be. Sun and water decide how much of it shows. Runners copy, seeds mix, and people have been choosing parents for thousands of years."

**The end.** The journal. `Print` prints it.

**Strawberry history (extra).** The garden strawberry's story.

## Content
- Woodland strawberry facts (two copies of each gene, runners and seeds), three model genes with stated alleles, a model growth rule (genes set the maximum, sun and water set the share), the pigment mutation from published work on white woodland strawberries, four breeding rounds, the engineering card, the history extra.
- A note: "The gene view is a model. Real plants have many genes for each trait."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any plant can be tapped for its gene view at any time.
- Keyboard: Tab to runners, rows, seeds, plants, the mutation card, parents and the journal; Enter acts.
- With Motion off growth shows as start and end stills.

## Look
- Accent `--brand` #b0233f strawberry red (header, the journal, gene letters); gold #f4c542 (the changed letter, the plant in focus); paper #fcf1f3; ink #2b0710; muted #614e53.
- Contrast (WCAG 2.1, computed): white on brand 6.65:1; brand on paper 6.02:1; ink on paper 16.67:1; muted on paper 6.98:1; ink on gold 11.32:1.
- Never color alone: alleles carry letters; mixes carry parent labels.
- Different from this batch (skate purple, storm slate, wave blue, pond green).

## Art
- Local FLUX (`scripts/localart.py`): the garden bed (1, 16:9), red and pale woodland berries (2, 1:1), the 1700s garden for the extra (1, 16:9).
- Drawn in code: plants growing, gene view, protein view, charts.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as the gardener; `clear-teacher` as the gene guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `runner`: "Drag a runner into a row."
- how `seed`: "Drag a seed into the bed."
- how `gene`: "Tap a plant to see its genes."
- event, whole, the mutation card.
- how `judge`: "Tap harmful, helpful or neutral."
- how `breed`: "Tap two parents, then tap Cross."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
genetics (family "genetics"; no engine file yet). This tool builds the genetics family's shared pieces first, in a marked block `/* GENETICS DATA: begin */ ... /* end */`: gene records with two copies, a cross that picks one copy from each parent, a clone copy, a one-letter mutation with its protein effect, so later genetics tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rows | Plant all runners in sun | The journal needs plants from two rows. |
| Mutation | Pick an effect without a reason | A reason from the setting is required. |
| Breeding | Pick parents at random | Allowed; the chart shows slower gains and asks why. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `runner`; `gene`.
2. `seed`.
3. Mutation card (whole), waits. `judge`.
4. `breed`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS1-5, MS-LS3-1, MS-LS3-2, MS-LS4-5 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Woodland strawberry (Fragaria vesca) has two copies of each chromosome; garden strawberry has eight | Shulaev and colleagues (2011), Nature Genetics, "The genome of woodland strawberry" | USDA Agricultural Research Service, strawberry genetics | yes |
| Strawberries spread by runners (clones) and by seeds | University of Minnesota Extension, "Growing strawberries" | Royal Horticultural Society, "Strawberries" | yes |
| A change in a pigment control gene (MYB10) gives white woodland strawberries | Hawkins and colleagues (2016), Plant Biotechnology Journal | Lin-Wang and colleagues (2014), Plant, Cell and Environment | yes |
| The garden strawberry came from crossing two American species in 1700s France | USDA Agricultural Research Service, strawberry history | University of California, Davis, strawberry breeding program | yes |
| Breeding chooses parents; genetic engineering changes genes directly | U.S. Food and Drug Administration, "Agricultural biotechnology" | National Academies of Sciences (2016), "Genetically Engineered Crops" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-10): one copy from each of two parents with two copies each gives four mixes per gene; four breeding rounds; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bed and gene view; at 680x425 sheet.
2. Identical runners grow to different sizes in different rows. (MS-LS1-5)
3. Runners show copies and seedlings show mixes in the gene view. (MS-LS3-2)
4. The mutation shows a letter, a protein and a trait change, judged with a reason. (MS-LS3-1)
5. Four breeding rounds run and the engineering card is read. (MS-LS4-5)
6. The model note shows; pigment facts match the cited papers.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: start and end stills; no network requests.

## Open questions
- The idea card flags a data source (default used: woodland strawberry genetics and the MYB10 white-fruit example from the cited papers, checked before build).
- Code move: the idea card moves MS-LS1-4 to flower-lure (default used: this tool teaches MS-LS1-5, MS-LS3-1, MS-LS3-2 and MS-LS4-5).
