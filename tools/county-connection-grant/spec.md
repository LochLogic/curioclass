# County Connection Grant

## One idea
A painted map of a rural county shows a small town, ranches spread along gravel roads, and a ridge that blocks radio signals, and the county commissioner, Ms. Begay (made up, labeled "illustration"), hands the child a $500,000 grant and a list of households that need to get online, a dairy family running barn sensors, a grandparent who lives alone and has doctor visits by video, a student with video homework, the library and the clinic; the child taps each household to read what it needs, then picks a device and a connection, fiber that is fast but costs about $40,000 a mile to lay, fixed wireless from a tower that the ridge blocks for two homes, satellite that reaches everyone but caps data, or a cell hotspot, and the map shows coverage, the monthly bill and the speed each home will really get while the budget meter drops; a winter storm cuts power for a day, and only homes with battery backup stay online; then the clinic launches a telehealth app that needs steady video, works only in English, and needs a newer phone, and the map lights up who it now leaves out even though they're "connected"; the child proposes design changes (audio-only visits, more languages, a web version) and watches the map change again; at the end the child sees that the right system depends on each user's needs and limits, and that a design that works for one community can still leave people out, so a student in grades 6 to 8 learns to match computing systems to needs and see how access and design differ across communities.

## Not like
- network-architect (Grades 9-12, spec): designing a school network. Here a county's households and a grant.
- packet-race (Grades 6-8, spec): how packets travel. Here who can get online at all.
- where-s-my-phone-from (10, spec): device supply chains. Here access and fit.
- metadata-x-ray (Grades 6-8, spec): what data reveals. Here who gets connected.

## Who and how
- Grades 6-8, Computer Science, module "Who Gets Connected". Standards: MS-SYS-HW-30, MS-SYS-IM-37, MS-SOC-ET-41 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Match computing systems to needs; how access and design differ across communities").
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every household and card. Controls 48 px or more.
- Eight households, four connection types, four devices, the storm test, the telehealth twist, three design changes. Extra: Commission meeting (the class votes on one plan on the projector). tool.json `modes: ["Grant", "Commission meeting"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-SYS-HW-30 | Match a device and connection to each household's tasks | speed, cost and coverage | 2 |
| MS-SYS-IM-37 | Compare access by distance, cost and terrain; run the storm | the ridge; dark homes in the storm | 3 |
| MS-SOC-ET-41 | Judge the telehealth app; propose changes | who it leaves out, then fewer | 4 |

## Screens and modes
Header (kit): title "County Connection Grant"; `Grant`, `Commission meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The county map with eight households, the ridge, a budget meter at $500,000, and Ms. Begay at a table. The welcome is queued (`welcomeAfter: true`): "Everyone here needs to get online. Tap a household to see what they need." First hint: "Tap a household."

**Match (focus: the map).** At 1366x768 the map is left with the household panel right; at 680x425 the panel is a sheet. The panel lists tasks (video homework, a doctor's video visit, barn sensors) and limits (distance, power, budget). The child picks a device and a connection; the map draws the route, the budget meter drops, and the household shows "enough" or "not enough" for each task.

**Storm.** `Run the storm` cuts power for a day; homes with battery backup stay lit. The child may add backup within the budget.

**Telehealth twist.** The clinic's app launches; homes it leaves out light up with a reason (bandwidth, language, device). Three design-change cards; the child picks up to two and the map redraws.

**Connected isn't enough (the aha).** Ms. Begay: "Everyone's connected, and the app still left people out. Fit the system to the people."

**The end.** The plan, the budget and who the app now serves. `Print` prints them.

**Commission meeting (extra).** Class vote.

## Content
- Costs and speeds are dated estimates with ranges, labeled "estimates, 2024"; the county, people and grant are made up.
- No provider names; connection types only.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Choices can be changed until `Lock the plan`; the storm and twist can be rerun.
- Keyboard: Tab to households, device and connection choices, the storm, design cards; Enter picks.
- With Motion off routes appear without drawing.

## Look
- Accent `--brand` #3f6346 range sage (header, routes, buttons); gold #f4c542 (the household in focus, the budget line); paper #f0f5ef; ink #10200f; muted #4f584e.
- Contrast (WCAG 2.1, computed): white on brand 6.81:1; brand on paper 6.16:1; ink on paper 15.39:1; muted on paper 6.70:1; ink on gold 10.45:1.
- Never color alone: routes carry line styles per type; left-out homes carry an icon and a reason.
- Different from this batch (parachute red, fridge blue, playground orange, gym purple).

## Art
- People (illustrated): Ms. Begay and household members, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Local FLUX (`scripts/localart.py`): the county in a painted rural style (1, 16:9), eight household scenes (8, 4:3).
- Drawn in code: routes, coverage, the ridge shadow, the budget meter.
About 15 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Ms. Begay; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.home + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `home`: "Tap a household."
- how `match`: "Pick a device, then a connection."
- how `storm`: "Tap Run the storm."
- how `twist`: "Tap a lit home to see why it's left out."
- how `change`: "Pick up to two design changes."
- event, whole, connected isn't enough.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the county graph, coverage with the ridge shadow, cost and speed tables, the storm, the app's requirement check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Match | Fiber to every home | The grant runs out after about 8 miles of fiber. |
| Storm | Ignore it | Homes without backup lose the doctor visit that day. |
| Twist | Pick any change | Each change shows which homes it brings back. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `home`; `match`.
2. `storm`.
3. `twist`; `change`.
4. Connected isn't enough (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Rural fiber costs tens of thousands of dollars per mile | Fiber Broadband Association (2024), "Fiber Deployment Annual Report" | NTIA (2023), BEAD program cost guidance and state broadband office estimates | yes |
| The FCC's broadband benchmark is 100 Mbps down and 20 up | Federal Communications Commission (2024), Section 706 Report | NTIA (2023), BEAD Notice of Funding Opportunity, "reliable broadband service" | yes |
| Satellite plans may limit data; terrain blocks fixed wireless | Federal Communications Commission, "Getting Broadband Q and A" | USDA Rural Development, ReConnect program technology guidance | yes |
| Telehealth access depends on bandwidth, device and language | U.S. Department of Health and Human Services, telehealth.hhs.gov, "Health equity in telehealth" | Pew Research Center (2021), "Some digital divide persists between rural, urban and suburban America" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s26, 2026-11-10): 8 miles of fiber at $40,000 is $320,000, leaving $180,000; five satellite homes cost $3,000 to set up and $7,200 a year; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and panel; at 680x425 panel as a sheet.
2. Eight households get a device and connection that meet their tasks. (MS-SYS-HW-30)
3. Access is compared and the storm run. (MS-SYS-IM-37)
4. The telehealth app is judged and changes proposed. (MS-SOC-ET-41)
5. Costs and speeds are dated ranges; no provider names.
6. `Read` reads every household and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: routes appear at once; no network requests.

## Open questions
- Cost, speed and data-cap figures for each connection type (default used: dated 2024 ranges from the Fiber Broadband Association, FCC and NTIA, with fiber at about $40,000 a mile; refresh at Build).
