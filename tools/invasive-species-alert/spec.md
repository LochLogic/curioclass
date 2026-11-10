# Invasive Species Alert

## One idea
The student arrives at Loon Lake, a small made-up inland lake town built from documented North American cases, the summer zebra mussels are found on a boat hull, and a lake biologist hands over a new job: over ten years, each year brings two or three response options (boat-wash stations, an awareness campaign, scraping the water plant's intake pipe, a chemical treatment in one bay, doing nothing), and before choosing the student scores each option on a criteria card (cost, harm to native species, effect on clean water and fishing, chance of success); then the year plays out on the lake and in year-by-year graphs: mussels filter the water clear, light reaches deeper, weeds spread, native mussels decline, walleye catches shift, the intake pipe clogs; at the end the student compares their ten-year lake with the "do nothing" lake and writes an argument for one change using the graphs as evidence, so a seventh grader learns to argue that changes to physical or biological parts of an ecosystem affect populations, and to evaluate competing design solutions for keeping biodiversity and ecosystem services.

## Not like
- lake-commons (9, spec): sharing a fishery over generations. Here a new species arriving.
- reserve-designer (9, spec): drawing protected land on a budget. Here responding to an invader year by year.
- food-web-wobble (5, concept): removing one species from a web. Here adding one.
- predator-prey-island (7, concept): two populations rising and falling. Here a whole lake and a town.

## Who and how
- Grade 7, Science, module "Ecosystem Change and Biodiversity". Standards: MS-LS2-4 (construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations), MS-LS2-5 (evaluate competing design solutions for maintaining biodiversity and ecosystem services).
- Format: story. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Ten years, two or three options a year, the criteria card with four criteria, five population graphs (zebra mussels, native mussels, water clarity, weeds, walleye) and one service graph (intake cleanings), the do-nothing comparison, the argument card. Extra: Class lakes (compare ten-year lakes across students). tool.json `modes: ["Lake", "Class lakes"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS2-4 | Watch each year's changes and argue one with graph evidence | the lake scene; the population graphs; the argument card | 2, 4 |
| MS-LS2-5 | Score options on four criteria before each choice | the criteria card; the budget; the services graph | 3 |

## Screens and modes
Header (kit): title "Invasive Species Alert"; `Lake`, `Class lakes`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A wooden dock on a calm lake, a fishing boat pulled up with a crust of small striped shells on its hull. The lake biologist (made up, labeled "illustration") holds a clipboard. A note: "Loon Lake is made up. What happens here is drawn from real lakes." The welcome is queued (`welcomeAfter: true`): "Those stripes are zebra mussels, and they don't belong here. You've got ten years to protect this lake. Tap the hull to take a closer look." First hint: "Tap the boat hull."

**A year (focus: the choice).** At 1366x768 the lake scene fills the left with the criteria card right and graphs below; at 680x425 the graphs and card are sheets. Two or three option cards with a cost from a yearly budget. The student rates each option on the criteria card (low, medium, high for each criterion), then picks. The year plays: the scene changes (clearer water, weeds near shore, a crusted pipe) and each graph adds a point.

**What changes.** Zebra mussels arrived in the Great Lakes in the late 1980s in ships' ballast water. Each filters about a liter of water a day; together they clear the water, so light reaches deeper and weeds spread; they smother native mussels; plankton drops, and fish that eat it change. They clog pipes, which costs towns money. Prevention (boat washing) slows spread; once mussels are in a lake, they almost never leave.

**Years 1 to 10.** Option sets change: early years favor prevention; later years add control. A doing-nothing year is always allowed and shown honestly.

**The comparison (the aha).** Side by side, the student's lake and the do-nothing lake, graphs overlaid. Narrator: "There's no perfect fix. The best tool was stopping them before they got in."

**The argument card.** "When ___ changed, the ___ population ___. My evidence is ___ in year ___." The student taps a graph point to cite it.

**The end.** The graphs, the criteria cards for each year and the argument. `Print` prints them.

**Class lakes (extra).** Ten-year lakes side by side on the projector.

## Content
- A simple yearly lake model with stated rules, ten years of option sets with costs, the criteria card, five population graphs and one service graph, the do-nothing run, the argument card. Effects follow documented cases from USGS and Sea Grant.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- An option can't be picked until the criteria card for that year is filled.
- Keyboard: Tab to options, criteria ratings, graph points and the card; Enter picks.
- With Motion off each year shows before and after stills.

## Look
- Accent `--brand` #0d6b66 lake teal (header, graph lines, the criteria card); gold #f4c542 (the chosen option, the cited graph point); paper #eef7f6; ink #062220; muted #4a5c5a.
- Contrast (WCAG 2.1, computed): white on brand 6.34:1; brand on paper 5.82:1; ink on paper 15.33:1; muted on paper 6.49:1; ink on gold 10.27:1.
- Never color alone: graph lines carry names and markers; ratings carry words.
- Different from this batch (granite brown, raindrop blue, tomato red, olive).

## Art
- People (illustrated): the lake biologist, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the dock in year 1 (1, 16:9), the lake in year 10 with clear water and weeds (1, 16:9), the intake pipe crusted (1, 4:3).
- Zebra mussel close-up from a public domain USGS photo, checked (1, 1:1).
- Drawn in code: graphs, the criteria card, option cards.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the lake biologist; `casual-peer` as a town teen on the dock and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.option + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `rate`: "Tap low, medium or high for each criterion."
- how `pick`: "Tap the option you choose."
- event, whole, each year's result.
- event, whole, the comparison.
- how `argue`: "Tap a graph point to use as evidence."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the yearly lake model, the criteria card, the graphs. Option sets and effect sizes sit in a marked block `/* INVASIVE DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Criteria | Rate everything high | Ratings aren't scored, but the year result shows each one beside what happened. |
| Choice | Do nothing every year | Allowed; the comparison and argument still need evidence from graphs. |
| Argument | Cite any point | The cited point must show the change named. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `rate`; `pick`.
2. Year result (whole), waits. Repeat for ten years.
3. Comparison (whole), waits.
4. `argue`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS2-4, MS-LS2-5 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Zebra mussels arrived in the Great Lakes in the late 1980s in ballast water | U.S. Geological Survey, Nonindigenous Aquatic Species, "Zebra mussel" | NOAA Great Lakes Environmental Research Laboratory, "Zebra and quagga mussels" | yes |
| Each mussel filters about a liter a day; water clears and weeds spread | Minnesota Sea Grant, "Zebra mussels" | NOAA Great Lakes Environmental Research Laboratory | yes |
| Zebra mussels harm native mussels and clog water intakes | U.S. Fish and Wildlife Service, "Zebra mussel" | U.S. Geological Survey, Nonindigenous Aquatic Species | yes |
| Boat cleaning (clean, drain, dry) slows spread; established populations are rarely removed | U.S. Fish and Wildlife Service, "Stop Aquatic Hitchhikers" | Minnesota Department of Natural Resources, "Zebra mussel" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-10): one liter a day is 365 liters a year per mussel; ten years of two or three options; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene, card and graphs; at 680x425 sheets.
2. Each year's change shows on the population graphs. (MS-LS2-4)
3. Each year's options are rated on four criteria before a pick. (MS-LS2-5)
4. An argument cites a graph point that shows the named change. (MS-LS2-4)
5. Effects match the cited USGS and Sea Grant accounts.
6. The made-up lake note and the illustration label show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stills; no network requests.

## Open questions
- The idea card flags a data source (default used: zebra mussel effects from USGS Nonindigenous Aquatic Species, NOAA GLERL and Minnesota Sea Grant, effect sizes checked before build).
