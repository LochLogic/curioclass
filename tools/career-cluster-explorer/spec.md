# Career Cluster Explorer

## One idea
One small town's harvest festival night takes all 14 career clusters: tap anything you see (the Ferris wheel, the stage lights, your ticket, the goats, the plane overhead) to meet the people whose work made it happen, and a string of 14 lanterns over the fair lights up as you find each cluster.

## Not like
- career-match-quiz (6-8, built, same family): starts from you (your interests) and ranks careers by fit. Here nothing is about you: you start from the world around you and find who makes it run. Its Explore mode places careers on an interest hexagon; here they are placed in a town.
- workplace-scenarios (6-8, same group): lives one day inside one workplace and its choices. Here you meet 83 jobs for a minute each; there are no choices or consequences.
- path-planner (9-12, careers family, not yet specced): plans one route to one goal. Here the Clusters view only shows that every cluster has ways in at every level of training; it plans nothing.
- hospital-shift (9-12, careers family): one cluster in depth. Here all 14 at once.

## Who and how
- Grade 6-8, career and technical education, module "Career Clusters (Career Exploration)".
- Topic line: the 14 career clusters, found at one town festival
- Driver: students (laptops or tablets, alone or in pairs) or the teacher on a projector for a whole-class "who made this?" warm-up. 15 to 30 minutes.
- Standards: CTE.Career Clusters (Advance CTE Career Clusters framework, 2024: the 14 clusters and the occupations in them).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Festival` (default), `Trails`, `Clusters`.

**Festival.** Stage: Maple Bend Harvest Night, a made-up town at dusk, drawn in code as flat layered shapes 2400 x 900 units wide, panning sideways (drag, mouse wheel, arrow keys, or the `◀` `▶` buttons; a thin minimap strip under it shows where you are). Left to right: the ridge with a wind turbine and power lines, the farm and barn, the river and bridge, the fairground (gate, stage, Ferris wheel, food trucks, tents, ball field), Main Street (library, clinic, bank, hotel, town hall, shops), the highway and auto shop, and the sky with a plane and an airport beacon on the far hill. Each hotspot (Content, 37) carries a small glowing marker (44 px target). Across the top of the stage: 14 unlit lanterns on a string, one per cluster, each labeled with its short name.
- Tap a hotspot: a card opens beside it with the thing's name and one line ("The Ferris wheel: tons of steel, bolted and welded, checked every day of the fair."), then its careers as chips (emoji, name, cluster color dot and cluster name).
- Tap a career chip: the career sheet (Family engine) with what they do, median pay, typical entry-level education, job outlook, how people get there and "Try it now".
- Opening a career lights its cluster's lantern; the panel shows "Lanterns lit: 9 of 14" and lists unlit clusters by name with `Where?` buttons that pan to a hotspot holding one (never the same hint twice in a row).
- Panel: `List` toggle shows all 37 hotspots as a plain list (for keyboard and screen readers), `Found` filter (All / Not opened yet), `Start over` (clears lanterns after a confirm).

**Trails.** Pick one of five trails (Content). The scene dims; the trail's hotspots glow and a dotted path links them in order. `Next` and `Back` step along it: each stop pans to its hotspot and shows one career and one sentence ("A truck driver hauls it to the fair."), with its cluster lantern lit. The last stop shows the trail's clusters as a row ("This bag of kettle corn took 5 clusters"). `Open career` at any stop opens the career sheet.

**Clusters.** A 4 x 4 grid of the 14 clusters (two cells left for a key), each with its color, its name and how many of its careers are in the tool. Tap one: its "Ways in" ladder. Columns by typical entry-level education (Handbook categories, merged: "No degree needed" = no formal credential or high school diploma; "Certificate or some college" = postsecondary nondegree award or some college; "Associate's"; "Bachelor's"; "Master's, doctoral or professional"). Each career is a chip in its column with median pay as a small bar (same scale for all clusters, $0 to $250,000) and its outlook word. A line under the ladder counts the columns that have a career ("Ways in at 4 of 5 levels"). `See it at the festival` on a chip jumps to Festival and opens that hotspot.

## Content
**Clusters** (Advance CTE 2024, keys as in `careers.json`): mfg Advanced Manufacturing; ag Agriculture; arts Arts, Entertainment and Design; build Construction; digital Digital Technology; edu Education; energy Energy and Natural Resources; fin Financial Services; health Healthcare and Human Services; hosp Hospitality, Events and Tourism; mgmt Management and Entrepreneurship; mkt Marketing and Sales; public Public Service and Safety; trans Supply Chain and Transportation.

**Hotspots** (id: thing, its one line; careers by `careers.json` id). Every one of the 83 careers appears exactly once.
1. ridge: Wind turbine and power lines on the ridge. "Tonight's lights start up here." wind-tech, lineworker
2. barn: The farm, with solar panels on the barn roof. "The corn for the kettle corn grew here." farmer, solar
3. river: The river below the bridge. "Herons nest here; the water gets tested every month." env-sci, wildlife
4. bridge: The new bridge into town, roadwork beside it. "Built to carry the whole town to the fair." civil-eng, equip-op
5. weather: The forecast board by the gate. "Clear skies until 11. Someone had to know that." meteorologist
6. petting: The petting pen with goats and a calf. "Every animal was checked before the gates opened." vet, vet-tech
7. kettle: The kettle corn stand. "Sweet, salty, and crunchy for weeks in the bag." food-sci
8. ferris: The Ferris wheel. "Tons of steel, bolted and welded, checked every day of the fair." welder, machinist, robotics-tech, ind-eng
9. stage: The main stage, with its lights and scaffold. "A band, a show plan, and a lot of wire." musician, director, electrician, carpenter
10. screen: The big screen beside the stage, showing a game tournament. "Edited clips, animated scores, a game someone designed." film-editor, animator, game-design
11. theater: The theater tent with a short play. "Ten minutes of story, written and performed tonight." actor, writer
12. artrow: Art row: the festival poster, a photo booth and the costume parade float. graphic-design, photographer, fashion
13. library: The new library on Main Street, open late. architect, librarian
14. hotel: The hotel lobby across the street. "Full of out-of-town visitors this weekend." hotel-mgr, interior
15. food: The food trucks and the ice cream freezer. chef, cook, hvac
16. restrooms: Restrooms and the water fountain. "Clean water in, wastewater out." plumber
17. gate: The gate: the ticket app on a phone and the scanner on its Wi-Fi. software-dev, web-dev, it-support, cyber
18. office: The festival office tent, with the crowd counter screen. event-planner, project-mgr, data-sci
19. kids: The kids' craft corner. teacher, preschool
20. help: The community help booth. "Someone to talk to, and help finding help." counselor, social-worker, psychologist
21. field: The youth soccer game under the lights. coach, athletic-trainer
22. firstaid: The first aid tent. nurse, paramedic
23. clinic: The evening clinic and pharmacy on Main Street. doctor, pa, med-assist, pharmacist
24. upstairs: Lit windows above the clinic: a dentist's office and a physical therapy gym. hygienist, pt
25. bank: The bank and its ATM, plus an insurance office next door. accountant, fin-advisor, actuary
26. hardware: The hardware store, the fair's main sponsor, with a "Now hiring" sign. ops-mgr, hr
27. sponsor: The sponsor tent with a "Which snack wins?" survey. marketing-mgr, market-research
28. radio: The local radio booth broadcasting from the fair. pr
29. forsale: A "For sale" sign on a house by the park. realtor
30. braids: The braids and face paint booth. stylist
31. fire: The fire truck parked by the gate, and the dispatch center's lit window. firefighter, dispatcher
32. police: A police officer at the crosswalk. "Back at the lab, someone tests evidence from a stolen bike case." police, forensic
33. townhall: Town hall: festival permits, contracts and the new park plan. lawyer, paralegal, planner
34. truck: A delivery truck at the loading zone. "Paper cups, ice, 600 pounds of corn." trucker, logistician
35. autoshop: The auto shop with a tow truck ready. auto-tech
36. plane: A plane passing overhead, blinking. pilot, flight-attendant, aerospace
37. airport: The airport beacon on the far hill. "Someone is watching that plane on radar." atc, aircraft-mech

**Trails** (stop: career, sentence):
- Behind the kettle corn: farmer "A farmer grows and harvests the corn." / food-sci "A food scientist works out how it stays crunchy in the bag." / trucker "A truck driver hauls it to the fair." / cook "A cook pops it in a huge kettle." / accountant "An accountant tracks what the stand spent and earned." (Clusters: Agriculture, Supply Chain and Transportation, Hospitality, Financial Services; 4.)
- Behind the stage lights: wind-tech "A technician keeps the wind turbine spinning." / lineworker "A line worker keeps power flowing into town." / electrician "An electrician wires the stage." / director "A producer plans the show, minute by minute." / musician "The band plays." / graphic-design "A designer made the poster that brought the crowd." (Energy, Construction, Arts; 3.)
- Behind your ticket: web-dev "A web developer built the page that sells tickets." / software-dev "A software developer built the phone app." / cyber "A cybersecurity analyst keeps card numbers safe." / it-support "An IT specialist keeps the gate scanners online." / data-sci "A data scientist counts the crowd by the hour." / event-planner "An event planner uses those counts to plan next year." (Digital Technology, Hospitality; 2.)
- Behind a twisted ankle: coach "A coach sees a player go down." / athletic-trainer "An athletic trainer checks the ankle on the field." / paramedic "A paramedic decides it needs an X-ray." / doctor "A doctor at the clinic reads the X-ray." / pt "A physical therapist plans six weeks of exercises." (Education, Healthcare and Human Services; 2.)
- Behind the bridge: planner "An urban planner chose where the bridge should go." / lawyer "A lawyer wrote the contracts." / civil-eng "A civil engineer designed it to carry the load." / welder "A welder joined its steel." / equip-op "An equipment operator moved the earth for the road." (Public Service and Safety, Construction, Advanced Manufacturing; 3.)

**Career data** (Family engine): all 83 careers from `tools/career-match-quiz/careers.json` (name, emoji, cluster, does, path, try, pay, hourly, jobs), plus three fields this tool adds for every career from the BLS Occupational Outlook Handbook, 2025-35 edition: `edu` (the Handbook's "Typical entry-level education", exact wording), `outlook` (the projected percent change 2025-35 and the Handbook's word for it, for example "-2% (Decline)"), `ooh` (the profile URL). Where the Handbook covers the occupation inside a larger profile, use that profile and show "Handbook profile: (its title)". If no profile covers it, show "Not in the Handbook" and leave the career out of the outlook line. Pay stays the OEWS May 2025 national median already in `careers.json` (the same survey the Handbook's 2025 pay comes from); musician and actor show hourly pay as the sibling does.

## Interactions in detail
- Lanterns: lit by opening a career (not just a hotspot) so finding a cluster means reading about a job in it. Lit lanterns save on this device (localStorage `career-cluster-explorer-lit`, try/catch); `Start over` clears them.
- When all 14 are lit, the lanterns brighten together once (a short shimmer, none with Motion off) and the event line plays; the scene stays explorable.
- `Where?` picks, for an unlit cluster, a hotspot holding one of its careers that the student has not opened, cycling so the same hotspot is not suggested twice running.
- Hotspot cards stay inside the stage (flip side near edges). Esc closes the card or sheet; focus returns to the marker.
- Panning: inertia off with Motion off; keyboard Tab order follows hotspots left to right, and focusing one pans it into view with `preventScroll` on focus.
- Outlook words come from the Handbook as written; the arrow icon beside them is up, flat or down, never color alone.
- Sizes: stage at real pixels with the scene at stage height (markers at least 44 px at 1366x768); in the 680x425 preview the lanterns shrink to dots with a count and the panel collapses to the `List` button; at 375 wide the card and the career sheet are full-width bottom sheets.

## Look
- Accent (`--brand`) #2dd4bf lantern teal, `--brand-ink` #062a26. Dusk night: sky from #120e2a to #3b2a63 at the horizon, panel #1e1840, ink #f3f0ff, muted #b9b2dd; string lights and lit windows #ffd36e; buildings in plum grays (#2b2450, #3a3166, #4b417c). Each cluster has its own lantern color (14 hues set by the builder, each 3:1 or more on the sky) and its name beside it.
- Contrast: accent on panel 8.95:1; brand-ink on accent 8.25:1; ink on panel 14.86:1; muted on panel 8.31:1; lantern yellow on sky 13.19:1.
- Differs from career-match-quiz's daytime cream, navy and coral, and from the group's camp blue, studio white, pencil paper and red-on-dark film room.

## Art
none: drawn in code (the town as flat layered shapes; careers shown by their emoji from `careers.json`, as in career-match-quiz).

## Voice
Bank voice: `upbeat-guide` (a tour guide walking you around the fair; different from every tool in this group; career-match-quiz has no voice). Style: bright, clear, friendly.
- welcomeFestival (how): "Tap anything glowing at the fair. Then tap a job to meet the person who does it."
- panHow (how, first time a card closes): "Drag the town sideways, or tap the arrows, to see more."
- lanternHow (how, first lantern lit): "That lantern is a career cluster. Find all fourteen."
- allLit (event, all 14 lit; plays once per run of lighting them): "All fourteen lanterns are lit. One night at the fair took every cluster."
- welcomeTrails (how): "Pick a trail, then tap Next to follow it across the fair."
- trailEnd (event, at a trail's last stop; stale if the trail changes): "That took (n) clusters working together."
- welcomeClusters (how): "Tap a cluster to see its ways in, from no degree to grad school."

## Family engine
The careers family engine (described here in full; career-match-quiz is the built sibling it comes from, and path-planner and hospital-shift will feed it too):
- Data: `careers.json`, built by `scripts/careers_data.py` (O*NET 30.2 interests, Job Zones and work context; BLS OEWS pay and jobs through `scripts/bls.py`). This tool's three Handbook fields (`edu`, `outlook`, `ooh`) are added to the same builder so every sibling gets them; career-match-quiz ignores fields it does not use.
- Career sheet: career-match-quiz's `openDetail` sheet, moved to a shared part (for example `kit/careers.js`, the integrating session decides): header (emoji, name, cluster), what they do, facts row (median pay with year, training, people doing it), similar careers, Try it now, and the source line. Siblings add their own blocks (career-match-quiz its match "why" and interest bars; this tool `See it at the festival` and the outlook fact).
- Formatting helpers from career-match-quiz: `payText`, `jobsText`, `money`, cluster names.
This tool feeds it: the 37 hotspots and 5 trails above and the Handbook fields.

## Sources
- The 14 career clusters: Advance CTE, Career Clusters Framework (2024), https://careertech.org/career-clusters/
- Typical entry-level education and job outlook 2025-35 (percent and words): U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, 2025-35 edition, https://www.bls.gov/ooh/ (one profile URL per career in `careers.json`; checked: Graphic Designers, median pay $62,960 in 2025, Bachelor's degree, -2% (Decline), https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm).
- Median pay and job counts: BLS Occupational Employment and Wage Statistics, May 2025, national, as already in `tools/career-match-quiz/careers.json` (built by `scripts/careers_data.py`).
- Career descriptions, paths and Try it now: written for grades 6-8 in `scripts/careers_data.py`.
- Town, hotspots, lines and trails: made up for this tool.

## Done when
1. All 83 careers appear in exactly one hotspot (script check), and each career sheet shows pay with its year, entry education, outlook with "2025-35", and the Handbook link.
2. Three careers' Handbook fields match their live Handbook pages (spot-check, including one inside a larger profile).
3. Lanterns light only on opening a career, survive a reload, and Start over clears them; all 14 lit plays allLit once.
4. Where? always pans to a hotspot holding an unlit cluster's unopened career, never the same one twice running.
5. Each trail steps in order with the right clusters count at the end (4, 3, 2, 2, 3).
6. Clusters ladders place each career in the right education column; pay bars share one scale.
7. Every hotspot is reachable by keyboard and in List; focusing pans it into view without scrolling the page.
8. Markers stay at least 44 px and the lanterns readable at every STANDARDS.md size; the preview is readable.
9. How lines once in five hotspots opened in a row; allLit and trailEnd every time they happen, trailEnd dropped when stale.

## Open questions
- The three Handbook fields (`edu`, `outlook`, `ooh`) go into the shared `careers.json` that the live career-match-quiz bundles. Rebuilding that file changes a live tool's data (its pay and job numbers stay the same; the new fields are unused there). OK to extend it in place, or should this tool keep its own copy until career-match-quiz is next touched?
