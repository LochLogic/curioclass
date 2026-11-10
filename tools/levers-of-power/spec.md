# Levers of Power

## One idea
A dangerous crossing near school at pickup time is also a state road problem and part of a worldwide traffic safety crisis; the child zooms between four views (the street, the city, the state, the world), sees at each level the problem's shape, causes and who decides (a fast four-lane road through a school zone; a city traffic office; a state highway department that owns the road; about 1.2 million road deaths worldwide a year), then pulls levers through the roles citizens play (petitioner, voter, testifier, reporter, organizer, juror), and a modeled outcome shows what moved, how long it took and how many people it needed; at the end a capacity board rates what one student alone and what a group could do at each level, and the child picks a realistic plan, so an eighth grader learns to analyze a problem at local, state and global levels, assess individual and group capacity to act, and explain the real roles citizens play.

## Not like
- tools-for-change (5, spec): strategy cards with examples. Here one problem across four levels.
- motion-on-the-floor (8, concept): running one meeting. Here choosing where to act.
- shaping-our-week (8, concept): who shapes daily life. Here how to change one thing.
- smoke-and-honey (6, spec): policy choices in a model town. Here citizens' levers on a real kind of problem.

## Who and how
- Grade 8, Social Studies (Taking Informed Action and Civics), module "Levers of Power". Standards: D4.6.6-8 (draw on multiple disciplinary lenses to analyze how a specific problem can manifest itself at local, regional, and global levels over time, identifying its characteristics and causes, and the challenges and opportunities faced by those trying to address the problem), D4.7.6-8 (assess their individual and collective capacities to take action to address local, regional, and global problems, taking into account a range of possible levers of power, strategies, and potential outcomes), D2.Civ.2.6-8 (explain specific roles played by citizens (such as voters, jurors, taxpayers, members of the armed forces, petitioners, protesters, and office-holders)).
- Format: simulator. Driver: one child alone, or the class pooling levers (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Four zoom levels, six roles, levers with modeled outcomes, the capacity board, the plan. Extra: Class pool (each student pulls one lever and the class sees the combined effect). tool.json `modes: ["One student", "Class pool"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.6.6-8 | Zoom through four levels and tag each level's causes, who decides, challenges and opportunities | the level card with its causes and decider; a data strip over time | 2 |
| D2.Civ.2.6-8 | Choose a role and an action at a level | the role card explaining what that citizen role can do | 3 |
| D4.7.6-8 | Rate on the capacity board what one person and a group can do at each level, then pick a plan | the board's grid; the plan card with steps, time and people | 4 |

## Screens and modes
Header (kit): title "Levers of Power"; `One student`, `Class pool`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A school at pickup time: cars stacked along a wide road, kids waiting at a crossing with no signal, a crossing guard waving, a speed limit sign reading 45. A zoom control on the right: Street, City, State, World. The welcome is queued (`welcomeAfter: true`): "This crossing near school is dangerous. Who can fix it? It depends how far you zoom out. Tap the crossing to look closer." First hint: "Tap the crossing."

**The levels (focus: the level card, D4.6.6-8).** At 1366x768 the scene fills the left with the level card right; at 680x425 the card is a sheet. The town, school and road are made for this game; the processes and world figures are real.
- Street: cars go fast; the crossing has no signal; a near miss happened last month. Who decides: the city's traffic engineer can study it, but this road is a state highway.
- City: the city council and police can add a crossing guard and enforce speed; the city can ask the state for a lower school-zone limit. A data strip: crashes at the crossing over five years (made for this game).
- State: the state department of transportation owns the road and must do a traffic study before changing the limit or adding a signal; the legislature sets funding and school-zone laws. Federal Safe Routes to School money passes through the state.
- World: about 1.19 million people die on roads each year (WHO, 2023); road crashes are a leading cause of death for children and young people aged 5 to 29; the United Nations set a goal of halving road deaths by 2030. Causes named across levels: speed, road design, too few safe crossings.
- At each level the child tags causes, who decides, a challenge and an opportunity from tiles.

**Levers (D2.Civ.2.6-8).** Six roles, each with real powers explained on its card:
- Petitioner: gather signatures asking the city or state for a study.
- Voter: vote for officials who fund road safety (the student can't vote yet, but can urge family; the card says so).
- Testifier: speak at a city council or state hearing.
- Reporter: write to the local news or school paper with the data.
- Organizer: start a group of parents and students; plan a walk audit.
- Juror: jurors decide cases, including crash cases; the card explains that juries hold people responsible but don't change roads directly.
- The child picks a role and an action at a level; the model (made for this game) shows what moved (a study ordered, a guard added, the limit lowered at school times, a signal funded), how long it took (weeks to years) and how many people it needed.

**The capacity board (the aha, D4.7.6-8).** A grid: four levels across, "Me alone" and "Our group" down. The child rates each cell (Can do a lot, Can do some, Can't do much yet) with a reason. Then the plan card: three steps in order from the levers tried, with who, how long, and what success looks like. Narrator: "One voice can start a study. Many voices get a signal built. Choose the level where your lever reaches."

**The end.** The level cards, the levers tried, the board and the plan. `Print` prints them.

**Class pool (extra).** Each student pulls one lever; the class sees combined effects and how long they take.

## Content
- Four levels with causes, deciders and data (the town and crash data made for this game; world figures real), six role cards, about twenty lever actions with modeled outcomes, the capacity board, the plan card.
- The town, school and model are made up and labeled; the state process, federal program and world figures are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Zoom moves one level at a time; each level must be tagged before its levers open.
- Levers can be tried in any order; outcomes stack and show time passing.
- Keyboard: Tab to the zoom, tiles, roles and the board; Enter to pick; arrows to zoom.
- With Motion off zoom cuts between levels without scaling.

## Look
- Accent `--brand` #9a4300 signal orange (header, zoom control, lever cards); gold #f4c542 (the chosen lever, a done step); paper #fcf4ee; ink #2e1500; muted #62514a.
- Contrast (WCAG 2.1, computed): white on brand 6.61:1; brand on paper 6.08:1; ink on paper 15.79:1; muted on paper 6.91:1; ink on gold 10.55:1.
- Never color alone: board cells carry words; outcomes carry icons and labels.
- Different from this batch (printer's sepia, archive green, Philadelphia navy, canal blue).

## Art
- Local FLUX (`scripts/localart.py`): the crossing at pickup (1, 16:9); the city hall council room (1, 16:9); the state capitol hearing room (1, 16:9); a world view of road traffic (1, 16:9); a new signal at the crossing (1, 16:9).
- People art goes to Gemini with `people: true`: six role figures, a student, the crossing guard, a traffic engineer (9; cutout yes).
- Drawn in code: the zoom control, data strips, the board, the plan card.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the narrator; `casual-peer` as a classmate, Dani (made for this game), reading the role cards. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each level card.
- how `tag`: "Tag the causes and who decides at this level."
- how `lever`: "Pick a role, then pick an action."
- event, whole, each role card and outcome.
- how `board`: "Rate what you alone and your group can do at each level."
- how `plan`: "Put three steps in order for your plan."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the zoom levels, tag tiles, role and lever cards with a small outcome model, the capacity board, the plan card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Levels | Zoom straight to World | Each level's levers open only after its tags; tags check. |
| Levers | Try only one role | The board's "Our group" cells need at least three levers tried. |
| Board | Rate everything "Can do a lot" | Each rating needs a reason; "Me alone" at World plays "Can one person change world road deaths alone?" |
| Plan | List three steps in any order | Steps check that a study comes before a signal. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Level card (whole), waits; `tag`.
2. `lever`; role card and outcome (whole).
3. `board`; `plan`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D4.6.6-8, D4.7.6-8 and D2.Civ.2.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| About 1.19 million road deaths a year worldwide; leading cause of death for ages 5 to 29 | WHO, "Global status report on road safety 2023" | WHO, "Road traffic injuries" fact sheet | yes |
| The UN goal of halving road deaths by 2030 (Decade of Action 2021 to 2030) | UN General Assembly resolution 74/299 (2020) | WHO, "Global Plan for the Decade of Action for Road Safety 2021-2030" | yes |
| State highways are owned by state DOTs, which require traffic studies before changing limits or signals | FHWA, Manual on Uniform Traffic Control Devices (signal warrants and speed zoning) | FHWA, "Methods and Practices for Setting Speed Limits" (2012) | yes |
| Federal Safe Routes to School funds pass through states | FHWA, "Safe Routes to School" program page | National Center for Safe Routes to School | yes |
| Citizen roles: petitioners, voters, testifiers, jurors | USA.gov, "Jury service" and "Contact your elected officials" | National Conference of State Legislatures, "Testifying before a legislative committee" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r14, 2026-11-09): four levels by two rows give eight board cells; every lever outcome lists time and people; the plan key orders study before signal; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and card; at 680x425 sheet.
2. Four levels show causes, deciders, challenges and data. (D4.6.6-8)
3. Six roles open levers with real powers and modeled outcomes. (D2.Civ.2.6-8)
4. The capacity board and plan check. (D4.7.6-8)
5. Juror and voter cards say plainly what they can and can't do.
6. Class pool combines levers.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: zoom cuts; no network requests.

## Open questions
None.
