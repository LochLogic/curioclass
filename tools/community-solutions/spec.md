# Community Solutions

## One idea
In a made-up river town the creek has turned cloudy and the fish are gone, and the student, the newest member of the town's green team, goes to the library desk and opens six case files from real places that used science to protect a resource (a city that cleaned its smoky air, a desert city that used much less water as it grew, a farm region that planted strips of trees along streams, a coast that rebuilt its dunes, a river town that gave its river room to flood, and a river where two dams came down so salmon could return), noting for each the problem, the science used, the cost and the measured change; the student picks two ideas that fit the cloudy creek and combines them into a plan, then defends it at a town meeting where illustrated residents (a farmer, a shop owner, a kid, an angler) ask hard questions, answering each with a fact from the notes; after a vote, a "five years later" screen shows results that match what the real cases showed, and plans backed by data from places where they worked, and that answer the people affected, win the most support, so a fifth grader learns to obtain and combine information about how real communities use science to protect Earth's resources and environment.

## Not like
- town-planner-disaster-ready (4, spec): hazards on a budget. Here protecting a resource with ideas from real places.
- invasive-species-alert (7, concept): managing one ecosystem. Here a community's plan.
- beaver-builders (K, spec): an animal changing a place. Here people fixing one.
- sphere-connections (5, spec): how Earth systems connect. Here how people protect them.

## Who and how
- Grade 5, Science, module "Protecting Earth". Standards: 5-ESS3-1 (obtain and combine information about ways individual communities use science ideas to protect the Earth's resources and environment).
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six real case files, a notes sheet with four fields, the plan builder, four residents with three questions each, the vote, five years later. Extra: Case teams (groups each take one case file and teach it to the class). tool.json `modes: ["Green team", "Case teams"]`, `minutes: "30-40"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-ESS3-1 (obtain) | Read six case files and note problem, science, cost and change | the case files; the notes sheet | 2 |
| 5-ESS3-1 (combine) | Combine two cases' ideas into one plan for the town | the plan builder | 3 |
| 5-ESS3-1 (communicate) | Answer residents' questions with facts from the notes | the town meeting; the vote; five years later | 4 |

## Screens and modes
Header (kit): title "Community Solutions"; `Green team`, `Case teams`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A small river town where a creek runs cloudy past farms and shops; an empty fishing dock. The welcome is queued (`welcomeAfter: true`): "Welcome to the green team! Our creek is cloudy and the fish are gone. Other towns have fixed problems like this. Tap the library to read how." First hint: "Tap the library."

**The library (focus: the case file).** At 1366x768 the case file fills the left with the notes sheet right; at 680x425 notes are a sheet. Six case files, each with a photo, a short story, a before-and-after number or picture, and a source line:
1. Chattanooga, Tennessee: once named the dirtiest air in the country in 1969, it cleaned its air with new rules and cleaner industry and met national air standards by 1989.
2. Las Vegas, Nevada area: paid people to replace thirsty lawns with desert plants and used much less water per person while the city grew.
3. Chesapeake Bay farms: planted strips of trees and grass along streams to catch mud and fertilizer before it reached the water.
4. A New Jersey shore town: rebuilt tall sand dunes with plants, and towns with dunes saw less damage in storms.
5. Napa, California: gave the river room to spread in floods with wetlands and wider banks instead of only taller walls.
6. The Elwha River, Washington: two dams were removed between 2011 and 2014 after decades of work by the Lower Elwha Klallam Tribe and others, and salmon came back.
For each, the student fills four notes: problem, science used, cost, measured change.

**The plan (focus: the plan builder).** The student drags two ideas into a plan for the cloudy creek (for example, stream-side tree strips plus wetlands for floods) and writes how they fit together.

**The town meeting.** Four residents (illustrations): a farmer ("Will I lose land?"), a shop owner ("What does it cost?"), a kid ("When will the fish come back?"), an angler ("How do you know it works?"). The student answers with facts from their notes; answers with a fact earn support.

**Five years later (the aha).** After the vote, the creek runs clearer and fish return in the amounts real cases showed, with the source shown. Narrator: "Communities don't have to guess. They can learn from places where science already worked, and they can listen to the people it affects."

**The end.** The notes, the plan and the meeting results. `Print` prints them.

**Case teams (extra).** Groups each take one case and teach it to the class.

## Content
- Six real case files with checked facts, a made-up town and residents (labeled "illustration"), the plan builder, twelve resident questions, the vote and results.
- Case results are stated as reported by the sources, with no promises beyond them.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Notes can be edited until the meeting.
- Keyboard: Tab to case files, note fields, the plan builder, residents and answer choices; Enter picks.
- With Motion off five years later shows a before and after picture.

## Look
- Accent `--brand` #2e6b4f river green (header, the notes, the plan); gold #f4c542 (the open case, a supported answer); paper #eff7f3; ink #0b2219; muted #4f5c55.
- Contrast (WCAG 2.1, computed): white on brand 6.30:1; brand on paper 5.78:1; ink on paper 15.33:1; muted on paper 6.43:1; ink on gold 10.27:1.
- Never color alone: support shows as a count and words; case files carry place names.
- Different from this batch (globe blue, tea amber, bakery rose, night indigo).

## Art
- People (illustrated): four residents, labeled "illustration" (Gemini, `people: true`, 4; cutout yes).
- Public domain photos for the six cases (EPA, USGS, NPS, USDA, NOAA) where found and checked, with credits; otherwise generated and labeled (6, 4:3).
- Local FLUX (`scripts/localart.py`): the town and creek before and after (2, 16:9), the meeting hall (1, 16:9).
- Drawn in code: notes, the plan builder, the vote.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the case file reader; `wise-mentor` as the green team leader and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `read`: "Tap a case file to open it."
- how `note`: "Fill in the four notes."
- how `plan`: "Drag two ideas into your plan."
- how `answer`: "Pick an answer with a fact from your notes."
- event, whole, five years later.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: case files, notes, the plan builder, the meeting, the vote. Case data sits in a marked block `/* CASES DATA: begin */ ... /* end */` with sources.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Notes | Skip reading | The plan builder needs notes from at least four cases. |
| Plan | Pick one idea | The plan needs two ideas. |
| Meeting | Pick answers without facts | Only answers that cite a note earn support. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `read`; `note`.
2. `plan`.
3. `answer`; five years later (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-ESS3-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Chattanooga's air: worst in 1969, met national standards by 1989 | U.S. Environmental Protection Agency, Region 4, Chattanooga air history | Chattanooga-Hamilton County Air Pollution Control Bureau | yes |
| Southern Nevada lawn replacement and lower water use per person | Southern Nevada Water Authority, "Water Smart Landscapes" | U.S. Bureau of Reclamation, Lower Colorado River conservation reports | yes |
| Stream-side forest buffers catch sediment and nutrients | Chesapeake Bay Program, "Forest buffers" | USDA Natural Resources Conservation Service, "Riparian forest buffer" | yes |
| Dunes reduced storm damage on the New Jersey shore | U.S. Army Corps of Engineers, New Jersey shore protection reports | New Jersey Department of Environmental Protection, coastal engineering | yes |
| Napa River "living river" flood project | U.S. Army Corps of Engineers, Napa River flood project | Napa County Flood Control and Water Conservation District | yes |
| Elwha dam removal 2011 to 2014 and the salmon return; the Lower Elwha Klallam Tribe's role | National Park Service, Olympic National Park, "Elwha River restoration" | U.S. Geological Survey, Elwha River science; Lower Elwha Klallam Tribe | yes |
Backed twice: 7. Cut: 0.
Sensitivity note: the Elwha case is on the homeland of the Lower Elwha Klallam Tribe, whose decades of work helped bring the dams down; the case names the Tribe as a leader, not a bystander, and links to its own site; Chattanooga's air history also touches who lived nearest the smoke, told plainly without blame; a fresh review agent reads all six cases before build.

Checks run (Python, scratchpad r30, 2026-11-09): six cases with four notes each is 24 notes; four residents with three questions each is twelve; Chattanooga took 20 years from 1969 to 1989; the Elwha dams came down over about three years (2011 to 2014); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 case and notes; at 680x425 sheet.
2. Six real cases are read with four notes each. (5-ESS3-1)
3. Two cases' ideas are combined into one plan. (5-ESS3-1)
4. Residents' questions are answered with facts, and five years later matches the real cases. (5-ESS3-1)
5. Every case fact matches its cited sources.
6. The Elwha case credits the Lower Elwha Klallam Tribe and links to its site.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after pictures; no network requests.

## Open questions
- The idea card flags a data source (default used: six cases from EPA, SNWA and Reclamation, the Chesapeake Bay Program and NRCS, USACE and NJDEP, Napa County and USACE, and NPS and USGS for the Elwha, each fact checked before build).
- Sensitivity flag: tribal lands and environmental justice (default used: the Elwha case credits the Lower Elwha Klallam Tribe as a leader with a link to its own site, Chattanooga's history told plainly without blame, fresh-agent read of all six cases before build).
