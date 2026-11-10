# Predator Prey Island

## One idea
On Isle Royale, a wild island in Lake Superior where scientists have counted wolves and moose every winter since 1958, the student runs a simple model of the two populations beside the real counts (shown faint), sets starting wolves, moose, winter snow depth and balsam fir food, lays the model curve over the real one, then picks a year where they differ and tests causes (a hard winter, a food shortage, a disease that reached the wolves around 1980, a new wolf crossing the ice) until the model matches, seeing that food and snow change how many moose survive and calve and that moose numbers drive wolf numbers; side cards show beavers competing with moose for aspen and foxes and ravens feeding at wolf kills; a pattern step gives three cases from other places (lynx and snowshoe hares in northern forests, cleaner fish and their reef clients, two barnacle species sharing a rock) and the student predicts each interaction type and the shape of its graph before checking; at the end the student explains one rise or crash with evidence, so a seventh grader learns to analyze data on how resources affect populations and to explain and predict patterns of interactions (predation, competition, mutual benefit) across ecosystems.

## Not like
- carrying-capacity (9, spec): one population leveling off. Here two that push each other.
- energy-pyramid (7, spec): energy per level, same family. Here numbers over time.
- wolf-pack-survival (3, spec): a pack's needs through seasons. Here sixty years of real counts.
- food-web-wobble (5, concept): removing one species, same family. Here testing causes against data.

## Who and how
- Grade 7, Science, module "Ecosystems and Interactions". Standards: MS-LS2-1 (analyze and interpret data to provide evidence for the effects of resource availability on organisms and populations of organisms in an ecosystem), MS-LS2-2 (construct an explanation that predicts patterns of interactions among organisms across multiple ecosystems).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Real counts from 1959 on, a two-population model with four sliders and four cause cards, three mismatch years to explain, three side cards, three outside cases. Extra: Count day (how researchers count from small planes, with a practice count). tool.json `modes: ["Island", "Count day"]`, `minutes: "30-40"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS2-1 | Change food and snow, match the model to real counts in three mismatch years | the count graph; model and real curves; cause cards | 2, 3 |
| MS-LS2-2 | Name interaction types on the island and predict three outside cases | side cards; prediction graphs; the reveal | 4 |

## Screens and modes
Header (kit): title "Predator Prey Island"; `Island`, `Count day`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The island from above in winter, white with dark spruce, ringed by lake ice. Below, the real count graph is faint: wolves on one axis, moose on the other. Four sliders. The welcome is queued (`welcomeAfter: true`): "Wolves and moose have shared this island for decades. Scientists counted them every winter. Can your model tell their story? Tap Run." First hint: "Tap Run to start the model."

**The model (focus: the graph).** At 1366x768 the island sits left with the graph right; at 680x425 the graph fills the screen and the island is a tab. Each run draws the model's lines over the real counts. A match meter shows how close they are in each decade.

**Mismatch years.** Three flags on the real graph: 1980 to 1982 (wolves fell from 50 to 14), 1995 to 1997 (moose fell from about 2,400 to about 500), and the late 2010s (wolves down to 2). For each, the student drags cause cards onto the model: disease reaching the wolves (canine parvovirus), a hard winter with deep snow and ticks, too little fir to eat, a wolf pack inbreeding with no new wolves arriving. A good cause pulls the model toward the real line. The 2018 and 2019 card tells how 19 wolves were moved to the island.

**Side cards.** Beavers and moose both eat aspen (competition). Foxes and ravens eat at wolf kills. Balsam fir grows back when moose are few.

**Pattern step.** Three cases: lynx and snowshoe hare (predator and prey, about a ten-year cycle in fur records), cleaner fish and reef clients (both benefit), two barnacles on a rock (competition for space). The student picks the interaction type and sketches a graph shape, then sees the real pattern.

**The aha.** Narrator: "Food, weather and each other set these numbers. And the same kinds of partnerships and fights show up in forests, reefs and tide pools."

**The end.** The model and real curves, the causes chosen, the three predictions and one explanation sentence. `Print` prints them.

**Count day (extra).** How researchers count from a small plane, with a practice count of moose on a snowy slope.

## Content
- Annual wolf and moose counts from the Isle Royale long-term study (bundled), a stated two-population model with food and snow terms, four cause cards with effects, three side cards, three outside cases with real graphs.
- A model note: "This model is simple. Real numbers have more causes."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sliders and cause cards can change between runs; the real line never changes.
- Keyboard: Tab to sliders, `Run`, mismatch flags, cause cards and predictions; arrows move sliders; Enter places.
- With Motion off the model line draws at once.

## Look
- Accent `--brand` #3b5249 spruce (header, the model line, the sliders); gold #f4c542 (the mismatch flag in focus, the card in hand); paper #f2f5f3; ink #0f1a16; muted #4f5a55.
- Contrast (WCAG 2.1, computed): white on brand 8.44:1; brand on paper 7.69:1; ink on paper 16.22:1; muted on paper 6.54:1; ink on gold 10.95:1.
- Never color alone: wolf and moose lines carry icons and dash styles; model and real carry labels.
- Different from this batch (prairie amber, signal magenta, indigo, factory teal).

## Art
- Local FLUX (`scripts/localart.py`): the island in winter from above (1, 16:9), moose browsing fir (1, 4:3), wolves on lake ice from a distance, no hunt scene (1, 4:3).
- Public domain NPS photos where found and checked for the plane and researchers (1, 4:3).
- Drawn in code: graphs, sliders, cause cards, the outside case graphs.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the island narrator; `firm-captain` as the survey pilot and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.flag + ':' + state.case + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `run`: "Tap Run to start the model."
- how `cause`: "Drag a cause card onto the model."
- event, whole, each mismatch year's story.
- how `predict`: "Pick the interaction, then sketch the graph."
- event, whole, each case reveal.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
ecosystem (family "ecosystem"; no engine file yet). This tool builds the ecosystem family's shared pieces first, in a marked block `/* ECOSYSTEM ENGINE: begin */ ... /* end */`: species records, a yearly population step with resource terms, and a graph with model and real lines; energy-pyramid and food-web-wobble reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Causes | Drop every card on every flag | Each flag needs its single best cause; extras move the model away. |
| Predictions | Pick predator and prey each time | Two of three cases aren't, and the reveal shows why. |
| Explanation | One word | The sentence needs a resource or interaction and a year. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `run`; `cause`.
2. Mismatch story (whole), waits. Repeat for three flags.
3. `predict`; case reveal (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS2-1, MS-LS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Isle Royale wolf and moose counts since 1958; wolves 50 in 1980, 14 in 1982; moose about 2,400 to about 500 in 1995 to 1997 | Michigan Technological University, "Wolves and Moose of Isle Royale" annual reports | National Park Service, Isle Royale, "Wolves and moose" | yes |
| Canine parvovirus reached the wolves around 1980 | Michigan Technological University annual reports | Peterson and colleagues, Proceedings of the Royal Society B (1998) | yes |
| Wolves fell to 2; 19 wolves moved to the island in 2018 and 2019 | National Park Service, Isle Royale, wolf relocation | U.S. Fish and Wildlife Service and State University of New York ESF project pages | yes |
| Lynx and hare cycle about every ten years in fur records | Elton and Nicholson (1942), Journal of Animal Ecology | University of Alberta, Kluane Boreal Forest Ecosystem Project | yes |
| Barnacle competition on rocky shores; cleaner fish mutualism | Connell (1961), Ecology | Smithsonian Ocean, "Cleaner fish" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-10): wolves from 50 to 14 is a 72 percent drop; moose from 2,400 to 500 is a 79 percent drop; 1958 to 2018 is 60 years of counts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 island and graph; at 680x425 graph with tab.
2. The model is run against the real counts with food and snow changed. (MS-LS2-1)
3. Three mismatch years are explained with matching causes. (MS-LS2-1)
4. Three outside cases are predicted and checked. (MS-LS2-2)
5. Counts match the cited annual reports.
6. No hunt or kill scenes; the model note shows.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: lines draw at once; no network requests.

## Open questions
- The idea card flags a data source (default used: Isle Royale annual counts from the Michigan Tech and NPS reports, bundled with their year, plus the three outside cases from the cited papers, checked before build).
