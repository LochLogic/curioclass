# Job Shadow Day

## One idea
Behind four doors with name badges wait four workers (made up, labeled "illustration"), a large-animal vet, a farmer, an animator and a bus dispatcher, and the child shadows one through a day of four moments, choosing how the worker uses a computer at each one and seeing the result: the vet's portable X-ray shows a horse's leg in the barn, the farmer's soil map shows which field needs water, the animator's software fills in the frames of a jump, and the dispatcher's map shows a bus stuck in snow; a new-tool moment arrives in every day (a drone for the farmer, a new routing app for the dispatcher), and the child picks how the worker learns it, the help guide, trial and error, or asking a coworker, and sees what each costs in time and mistakes; a teamwork moment needs two people's work combined (the dispatcher shares the map with a driver; the animator hands frames to the sound designer); fifth graders also trace a ripple when the new tool changes the routine, such as the routing app sending a bus down a closed road, following who is affected and who catches it; at the end a badge wall shows each worker's computer moments, the way they learned, and who they worked with, so a student in grades 3 to 5 learns how people in many jobs use computing, learn new tools and work together, and how one system change ripples through a day.

## Not like
- who-uses-this-device (K, spec): tap a worker's device. Here a day of choices.
- industry-device-tour (6, concept): inside industry machines. Here people's choices at work.
- hospital-shift (Grades 9-12, spec): medical careers. Here four everyday jobs.
- team-code-relay (3, concept): teamwork on code. Here teamwork with tools at work.

## Who and how
- Grades 3-5, Computer Science, module "Computing on the Job". Standards: E3-SOC-CE-19, E4-SOC-CE-19, E5-SOC-CE-19, E5-SYS-IM-15 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "How people in many jobs use computing, learn new tools and work together").
- Format: story. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four days of four moments each, four new-tool moments, four teamwork moments, two ripple traces, the badge wall. Extra: Career talk (the class picks a door together on the projector). tool.json `modes: ["Shadow", "Career talk"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-SOC-CE-19 | Choose how the worker uses a computer | the X-ray, the soil map, the frames, the bus map | 2 |
| E4-SOC-CE-19 | Pick how the worker learns a new tool | time and mistakes for each way | 3 |
| E5-SOC-CE-19 | Combine two people's work | the shared map; handed-off frames | 3 |
| E5-SYS-IM-15 | Trace a ripple from a system change | who is affected; who catches it | 4 |

## Screens and modes
Header (kit): title "Job Shadow Day"; `Shadow`, `Career talk`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A hallway with four doors and name badges: Dr. Mae Okafor (vet), Luis Torres (farmer), Priya Nair (animator), Sam Whitehorse (dispatcher). The welcome is queued (`welcomeAfter: true`): "Pick who you'll shadow today. Tap a door." First hint: "Tap a door."

**A moment (focus: the scene).** At 1366x768 the scene fills the left with the choice card right; at 680x425 the card is a sheet. Each moment speaks the problem and offers two or three choices; the result plays and a badge sticker appears on the day's card.

**New tool.** A new tool arrives; three ways to learn it show a short result each (the guide is slow but sure; trial and error is fast with a mistake; asking a coworker is quick and needs someone free). The child picks and can try another way.

**Teamwork.** The day's problem can be solved only by combining work; the child picks what to share and with whom.

**Ripple (grade 5).** A system change starts a chain of cards; the child taps who is affected next and who catches the problem.

**Computers at every job (the aha).** Narrator: "Every worker used a computer, learned something new, and needed a teammate."

**The end.** The badge wall. `Print` prints it.

**Career talk (extra).** Class play.

## Content
- Four workers of varied backgrounds, labeled "illustration"; names are made up.
- Animal care scenes show no injuries beyond a limp; the X-ray is calm.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every moment can be replayed with another choice.
- Keyboard: Tab to doors, choices, learn options, share options and ripple cards; Enter picks.
- With Motion off results show as stills.

## Look
- Accent `--brand` #1d6b52 workday green (header, badges, buttons); gold #f4c542 (the choice in focus, a new sticker); paper #ecf6f2; ink #05211a; muted #4a5753.
- Contrast (WCAG 2.1, computed): white on brand 6.41:1; brand on paper 5.81:1; ink on paper 15.36:1; muted on paper 6.85:1; ink on gold 10.42:1.
- Never color alone: badges carry icons and words; ripple cards carry arrows.
- Different from this batch (map blue, relay purple, museum brown, council red).

## Art
- People (illustrated): four workers and four teammates, labeled "illustration" (Gemini, `people: true`, 8; cutout yes).
- Local FLUX (`scripts/localart.py`): barn, field, studio, dispatch room (4, 16:9), the hallway (1, 16:9).
- Drawn in code: the badge wall, choice cards, the ripple chain and tool screens.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as the narrator; `lively-host` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.worker + ':' + state.moment + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `door`: "Tap a door."
- how `choose`: "Tap what they should do."
- how `learn`: "Tap a way to learn the new tool."
- how `share`: "Tap what to share, then who gets it."
- how `ripple`: "Tap who is affected next."
- event, whole, computers at every job.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: four days as branching moments with results, learn-way costs, the ripple chain, the badge wall.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moments | Tap anything | Results show what happens, and the badge needs a working choice. |
| Learn | Pick the same way every time | The wall asks the child to compare two ways. |
| Ripple | Tap cards at random | Each link must follow from the last. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `door`; `choose`.
2. `learn`; `share`.
3. `ripple`.
4. Computers at every job (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Vets, farmers, animators and dispatchers use digital tools (portable X-ray, soil maps, animation software, dispatch mapping) | U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, entries for veterinarians, farmers, special effects artists and animators, and dispatchers | USDA, precision agriculture reports; American Veterinary Medical Association, equine imaging resources | yes |
| People learn new workplace tools through guides, practice and coworkers | K-12 Computer Science Framework (2016), Impacts of Computing | CSTA K-12 Computer Science Standards (2017), 1B-IC-20 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s23, 2026-11-10): four days of four moments make 16, plus four new-tool and four teamwork moments; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and card; at 680x425 card as a sheet.
2. Four workers' days are shadowed with computer choices. (E3-SOC-CE-19)
3. Ways to learn a new tool are compared, and work is combined with a teammate. (E4-SOC-CE-19, E5-SOC-CE-19)
4. Two ripples from a system change are traced. (E5-SYS-IM-15)
5. Workers are varied and labeled illustration.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: results are stills; no network requests.

## Open questions
- E5-SYS-IM-15 is matched to the module line, not to CSTA 2026 text (default used: a ripple trace of how one system change affects a day; confirm when the CSTA text is filed).
