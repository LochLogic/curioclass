# Made From

## One idea
A nylon jacket hangs on a hook with a card asking "Where did this come from?", and the student traces it backward through a chain of steps (jacket, woven fabric, nylon thread, melted nylon, two chemicals joined into long chains in a factory, chemicals made from crude oil and natural gas, oil and gas pumped from rock) and then forward to what it changed for people (nylon stockings in 1940, parachutes and ropes in World War II, cheap tough clothing, waste that doesn't rot); then two more products get the same trace: a plastic water bottle (oil and gas to PET plastic, uses and recycling) and a pain reliever (willow bark used for pain for thousands of years, its natural chemical changed in a lab into aspirin in 1897, now made from chemicals that start as oil); for each step the student drags the right picture into the chain and taps whether the step is natural, a chemical change or a shaping step, and for the forward side sorts effects into helps and costs; at the end three chains sit side by side and the student writes what they all share, so a seventh grader learns that synthetic materials come from natural resources through chemical processes and that they affect society.

## Not like
- reaction-kitchen (7, spec): what makes a reaction. Here reactions that turn resources into products.
- resource-map (7, spec): where resources are found. Here what they become.
- molecule-builder (7, concept): building molecules. Here following materials through factories.
- mystery-powders (5, spec): identifying materials. Here where materials come from.

## Who and how
- Grade 7, Science, module "Synthetic Materials". Standard: MS-PS1-3 (gather and make sense of information to describe that synthetic materials come from natural resources and impact society).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three products, each with five to seven backward steps and four forward effects, step-type tags, the helps and costs sort, the side-by-side card. Extra: Your pick (trace a fourth product from a list of three: a fleece blanket, a phone case, a car tire). tool.json `modes: ["Trace", "Your pick"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS1-3 (from natural resources) | Build each backward chain and tag each step | the chain; step tags | 2 |
| MS-PS1-3 (chemical process) | Mark which steps make new substances | chemical change badges | 3 |
| MS-PS1-3 (impact on society) | Sort forward effects into helps and costs; write what the chains share | the forward side; the side-by-side card | 4 |

## Screens and modes
Header (kit): title "Made From"; `Trace`, `Your pick`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A coat hook with a bright nylon jacket, a water bottle on a shelf and a pill bottle on a table, each with a tag. The welcome is queued (`welcomeAfter: true`): "Everything here started somewhere in nature. Let's follow it back. Tap the jacket." First hint: "Tap the jacket."

**Backward (focus: the chain).** At 1366x768 the product is left and the chain runs as a path to the right ending at the earth; at 680x425 the chain runs top to bottom and scrolls. Each empty link offers three pictures; the student drags the right one in and taps its tag: Natural, Chemical change (new substance), or Shaping (same substance, new shape). A card per link says what happens in one line.

**Forward.** From the product, four effect cards fan out (for nylon: stockings in 1940, parachutes in World War II, cheap tough clothes, waste that lasts for hundreds of years). The student sorts each into Helps or Costs; some fit both and the tool accepts either with a reason.

**Three products.** Nylon (crude oil and natural gas, chemicals joined into long chains, invented at DuPont in 1935); the PET bottle (oil and gas, chemicals joined into PET, molded; recycled into fiber or new bottles, though in the United States less than a third are); aspirin (willow bark used for pain since ancient times; its chemical, salicin, led to salicylic acid; Felix Hoffmann at Bayer made aspirin in 1897; today it's made from chemicals from oil).

**Side by side (the aha).** Three chains in a row. Narrator: "Every synthetic thing starts as something natural, gets changed by chemistry into something new, and then changes how people live." The student writes: "All three ___. One way they help is ___. One cost is ___."

**The end.** Three chains, sorts and the sentence. `Print` prints them.

**Your pick (extra).** One more product traced the same way.

## Content
- Three main and three extra products, each with checked steps from cited sources, step tags, four effects per product, the side-by-side card.
- A note: "Factories vary. These are the common steps."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A wrong picture returns to the tray with a one-line hint.
- Keyboard: Tab to products, links, pictures, tags and effects; Enter places.
- With Motion off the chain fills without sliding.

## Look
- Accent `--brand` #2f6250 factory teal (header, chain links, tags); gold #f4c542 (the link in focus, chemical change badges); paper #f0f6f3; ink #0b1f18; muted #4d5a55.
- Contrast (WCAG 2.1, computed): white on brand 7.04:1; brand on paper 6.43:1; ink on paper 15.68:1; muted on paper 6.59:1; ink on gold 10.55:1.
- Never color alone: tags carry words and icons; helps and costs carry plus and minus marks.
- Different from this batch (spruce, prairie amber, signal magenta, indigo).

## Art
- Local FLUX (`scripts/localart.py`): the room with three products (1, 16:9), about 20 chain pictures (oil well, refinery, pellets, thread, fabric, willow tree, lab flask and so on) (20, 1:1).
- Drawn in code: the chain, tags, effect cards.
About 21 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the guide who traces things; `news-reader` as the forward effect cards and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.product + ':' + state.link + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `link`: "Drag the right picture into the empty link."
- how `tag`: "Tap Natural, Chemical change or Shaping."
- how `sort`: "Drag each effect to Helps or Costs."
- event, whole, each product's forward story.
- how `write`: "Fill in the side-by-side card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the chain builder, tags, sorts. Product steps and effects sit in a marked block `/* MADE-FROM DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Chain | Drag pictures until one sticks | Each wrong try costs nothing, but the tag still needs the step type. |
| Tags | Tag everything Shaping | The chemical change steps reject it with a reason. |
| Sentence | Copy one effect | The card needs a natural resource, a help and a cost. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `link`; `tag`.
2. `sort`; forward story (whole), waits.
3. `write`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS1-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Nylon invented at DuPont in 1935; stockings sold in 1940; used for parachutes in World War II | American Chemical Society, National Historic Chemical Landmarks, "Nylon" | Science History Institute, "Wallace Carothers" | yes |
| Nylon and PET are made from chemicals from oil and natural gas | U.S. Energy Information Administration, "Oil and petroleum products explained: use" | American Chemical Society, "Plastics" | yes |
| Less than a third of U.S. PET bottles are recycled | U.S. Environmental Protection Agency, "Plastics: material-specific data" | NAPCOR, PET recycling report | yes |
| Willow bark contains salicin; Hoffmann at Bayer made aspirin in 1897 | Science History Institute, "Aspirin" | Royal Society of Chemistry, "Aspirin" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-10): three products; nylon's 1935 invention came before 1940 stockings; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 product and chain; at 680x425 vertical chain.
2. Three chains are built back to a natural resource. (MS-PS1-3)
3. Chemical change steps are tagged in each chain. (MS-PS1-3)
4. Effects are sorted and the shared pattern written. (MS-PS1-3)
5. Every step matches a cited source.
6. The common-steps note shows.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: chain fills without sliding; no network requests.

## Open questions
- The idea card flags a data source (default used: process steps per product from ACS, Science History Institute, EIA and EPA, checked before build).
