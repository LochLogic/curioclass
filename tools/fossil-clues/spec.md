# Fossil Clues

## One idea
In a quarry in the dry sagebrush high desert of southwest Wyoming, near Fossil Butte National Monument, the student splits rock slabs with a hammer, brushes out fossils (a small herring-like fish, a palm leaf, a turtle, a crocodile relative, a stingray), compares each to living relatives on a reference shelf, and logs what kind of place it needed (warm water, frost-free land); the notebook's table points to one conclusion: a warm lake surrounded by palms was here about 52 million years ago; a slider moves the scene from the ancient lake to today's sagebrush basin, and the student sorts organisms (lake fish, crocodiles, palms, pronghorn, sage grouse, sagebrush) into survive well, survive less well or cannot survive here, with a reason from each one's needs; then pronghorn migrate through the area and a highway crosses their path, and the student compares solutions (warning signs, a fence, wildlife overpasses and underpasses) using collision counts from the real crossing at Trappers Point and makes a claim about which works best; at the end a field report holds what lived here then, what lives here now, and the student's claim, so a third grader learns to use fossils as evidence of past organisms and environments, to argue which organisms survive in a habitat, and to judge a solution to a problem caused by a changing environment.

## Not like
- canyon-reader (4, concept): reading rock layers, same engine. Here what fossils say about a place.
- puppy-traits (3, concept): variation within one species. Here change in a whole place.
- life-cycle-wheel (3, spec): stages of one life. Here lives long gone.
- fast-or-slow (2, spec): how long changes take. Here what changed and why it matters.

## Who and how
- Grade 3, Science, module "Fossils and Changing Environments". Standards: 3-LS4-1 (analyze and interpret data from fossils to provide evidence of the organisms and the environments in which they lived long ago), 3-LS4-3 (construct an argument with evidence that in a particular habitat some organisms can survive well, some survive less well, and some cannot survive at all), 3-LS4-4 (make a claim about the merit of a solution to a problem caused when the environment changes and the types of plants and animals that live there may change).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six slabs, a reference shelf, the then-and-now slider, the survive sort with six organisms, the crossing with three solutions and real counts, the field report. Extra: Dig crew (the class splits slabs together on the projector). tool.json `modes: ["Quarry", "Dig crew"]`, `minutes: "25-35"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-LS4-1 | Split slabs, compare fossils with living relatives and log each one's needs | the fossil; the reference shelf; the notebook table | 2 |
| 3-LS4-3 | Sort six organisms by how well they'd survive today, with a reason | the then-and-now slider; the sort | 3 |
| 3-LS4-4 | Compare three crossing solutions with collision counts and make a claim | the crossing chart; the claim | 4 |

## Screens and modes
Header (kit): title "Fossil Clues"; `Quarry`, `Dig crew`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A quarry face of pale layered rock under a big sky, sagebrush all around. A hammer, a brush and a field notebook. The welcome is queued (`welcomeAfter: true`): "This dry land is full of secrets in the rock. Split the slab. What lived here? Tap the hammer, then tap the slab." First hint: "Tap the hammer, then the slab."

**Slabs (focus: the fossil).** At 1366x768 the slab fills the left with the reference shelf and notebook right; at 680x425 the shelf is a sheet. Six slabs: a small fish (Knightia, Wyoming's state fossil), a palm leaf, a turtle shell, a crocodile relative's jaw, a stingray, a leaf from a warm-climate tree. The student brushes each out, drags it beside its living relative on the shelf, and picks what it needed (warm water, fresh lake water, frost-free land). The notebook table fills; a claim card asks "What was this place like?" and accepts "a warm lake with palms around it".

**Then and now (3-LS4-3).** A slider moves the scene from the ancient lake to today's high desert with cold winters and little rain. Six organisms to sort: lake fish, crocodiles, palms, pronghorn, sage grouse, sagebrush. Each goes in Survive well, Survive less well or Cannot survive here, with a reason picked from its needs (needs a lake; needs warm winters; eats sagebrush). Some can be argued two ways, and the tool accepts either with a matching reason.

**The crossing (3-LS4-4).** Pronghorn walk one of the longest land migrations in the lower 48 states, and a highway crosses their path near Pinedale. Three solutions: warning signs, a fence alone, fences with overpasses and underpasses. A chart shows real counts: after two overpasses and six underpasses opened at Trappers Point in 2012, collisions with deer and pronghorn there dropped by about 80 percent. The student makes a claim: "The best solution is ___ because ___. It costs ___."

**The field report (the aha).** Then, now and the claim on one page. Narrator: "The rock remembers a lake that's been gone for millions of years. The animals living here now still need help when the land changes."

**The end.** The field report. `Print` prints it.

**Dig crew (extra).** The class splits slabs together.

## Content
- Six fossils from the Green River Formation with living relatives, the then-and-now slider, six organisms with needs, three solutions with real collision counts, the report template.
- Real fossil photos from public domain sources where found and checked; others generated and labeled.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A slab splits on tap; brushing reveals the fossil in strokes.
- Keyboard: Tab to tools, the slab, the shelf, the slider, the sort and the chart; Enter splits and places.
- With Motion off fossils appear without brushing and the slider jumps.

## Look
- Accent `--brand` #7a5a2e sandstone (header, the notebook, the slider); gold #f4c542 (the fossil being brushed, the chosen solution); paper #faf6ef; ink #241a0b; muted #5c564c.
- Contrast (WCAG 2.1, computed): white on brand 6.31:1; brand on paper 5.85:1; ink on paper 15.88:1; muted on paper 6.74:1; ink on gold 10.52:1.
- Never color alone: sort bins carry words and icons; chart bars carry numbers.
- Different from this batch (clay pot, team blue, wheel violet, winter teal).

## Art
- Local FLUX (`scripts/localart.py`): the quarry (1, 16:9), the ancient lake (1, 16:9), today's basin (1, 16:9), a pronghorn overpass (1, 16:9).
- Fossil close-ups: public domain National Park Service photos from Fossil Butte where found and checked, otherwise generated and labeled (6, 1:1); living relatives (6, 1:1).
- Drawn in code: the slab split, the notebook table, the sort, the chart.
About 16 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the paleontologist; `wise-mentor` as the wildlife biologist at the crossing and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.slab + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `split`: "Tap the hammer, then the slab."
- how `brush`: "Drag the brush over the rock."
- how `compare`: "Drag the fossil next to its living relative."
- event, whole, the "what was this place like" claim.
- how `sort`: "Drag each one to how well it would survive here today."
- event, whole, the crossing story.
- how `claim`: "Pick the best solution and say why."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fossils (family "fossils"; no engine file yet). This tool builds the fossils family's shared pieces first, in a marked block `/* FOSSILS DATA: begin */ ... /* end */`: the slab split and brush, fossil records with living relatives and needs, and the then-and-now slider; canyon-reader reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fossils | Skip the shelf | The notebook needs a living relative for each fossil. |
| Sort | Put everything in Survive well | Each placement needs a reason that matches the organism's needs. |
| Claim | Pick signs because they're cheap | Allowed if the reason uses the chart; the report shows the counts beside it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `split`; `brush`; `compare`.
2. Place claim (whole), waits.
3. `sort`; crossing story (whole); `claim`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-LS4-1, 3-LS4-3, 3-LS4-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Fossil Lake was a warm subtropical lake about 52 million years ago; fish, palms, turtles, crocodilians and stingrays | National Park Service, Fossil Butte National Monument | U.S. Geological Survey, "Green River Formation" | yes |
| Knightia is Wyoming's state fossil | Wyoming Secretary of State, state symbols | National Park Service, Fossil Butte, "Knightia" | yes |
| Pronghorn migration through the Pinedale area (Path of the Pronghorn) | U.S. Forest Service, Bridger-Teton, "Path of the Pronghorn" | Wyoming Migration Initiative, "Pronghorn" | yes |
| Trappers Point: two overpasses and six underpasses (2012); collisions dropped about 80 percent | Wyoming Department of Transportation, Trappers Point project | Sawyer and colleagues, Wildlife Society Bulletin (2016) | yes |
| Sagebrush habitat and the sage grouse | U.S. Fish and Wildlife Service, "Greater Sage-Grouse" | Bureau of Land Management, "Sagebrush ecosystem" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r27, 2026-11-09): six slabs and six organisms; two overpasses and six underpasses is eight crossings; an 80 percent drop from 100 collisions leaves 20; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 slab and shelf; at 680x425 sheet.
2. Six fossils are compared with living relatives and point to a warm lake. (3-LS4-1)
3. Six organisms are sorted by survival with reasons. (3-LS4-3)
4. Three solutions are compared with real counts and a claim is made. (3-LS4-4)
5. Fossil photos are public domain and checked, or labeled generated.
6. The crossing numbers match the cited reports.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no brushing animation; no network requests.

## Open questions
- The idea card flags a data source (default used: Fossil Butte and Green River Formation facts from the National Park Service and USGS, and Trappers Point counts from WYDOT and Sawyer and colleagues (2016), checked against the reports before build).
