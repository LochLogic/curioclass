# Cloud Through Time

## One idea
Drag one slider from 1946 to 2023 and the same job, keeping people's data and doing their computing, moves from one room on a university campus to buildings the size of a town's industrial park, while a ledger beside it keeps the other side of the story: how much electricity and water it takes, who did the work, and which town carries the cost, so "the cloud" turns out to be a place with a power bill.

## Not like
- eras-of-computing (6-8, gap fill, not specced): computing history and impact across eras of devices. Here one technology (the data center) is followed in depth, with its energy, water, labor and towns as numbers.
- art-through-time (9-12 arts, timeline): artworks in time. Here each stop is a building and its costs, and you link causes to it.
- emerging-tech-pitch (this group): judges a technology for one town today. Here the question is how one technology got here and who paid.
- network-architect (9-12 CS): designs a network. Here nothing is designed; the infrastructure is studied as history.
- where-s-my-phone-from (10, data desk): traces a phone's parts and supply chain. Here the object is the data center, not the device (the gap fill chose this on purpose).
- internet-journey (grade 3): follows a message across the internet. Here the story is the buildings that store it and what they cost.

## Who and how
- Grades 9 to 12, computer science. Module: A Technology's Long Story (Computing and Society), "The history of one technology and the infrastructure, energy and labor behind it". Topic line: "the history and costs of data centers".
- Driver: students on laptops, alone or in pairs. 25 to 40 minutes.
- Standards (module codes, CSTA 2026): HS-SOC-HI-38 (the history of a technology and the forces that shaped it: the timeline and Forces mode), HS-SYS-IM-37 (the infrastructure, energy and labor behind a computing system: the ledger and Costs mode). CSTA 2017 crosswalk: 3A-IC-24 (evaluate how computing impacts social and economic practices), 3B-IC-26 (equity and access in the distribution of computing resources), 3B-IC-27 (predict how computational innovations might evolve).
- tool.json: driver "students", minutes "25-40", modes ["Timeline", "Forces", "Costs"], grades_label "Grades 9-12".

## Screens and modes
Own light `:root` (an archive look: paper, ink, a teal accent), with theme-912 class names kept and light values, as data-policy-council does. Header: "Cloud Through Time", small line "Following the data center, 1946 to today". Mode buttons: **Timeline** (opens first), **Forces**, **Costs**. Motion, Sound, Read.

### Timeline
Stage, top: the **era slider** with seven stops (1946, 1951, 1964, 1969, 1993, 2006, 2023), each a labeled tick; drag or use Previous and Next. Middle: the **building view** drawn in code to one shared scale bar (a person 1.7 m tall stands at the door for size): ENIAC's room, a census machine room, a mainframe room with raised floor and air handlers, a pair of network machines in two campuses joined by a line, a server room in an office tower, a warehouse-sized hall by a river with a power line, a campus of halls with a substation. At each stop the scale bar rescales smoothly (no animation with Motion off) and a footprint label gives the size where a source has one. Bottom: the **ledger card** for the stop: rows **What it did**, **Size**, **Electricity**, **Water**, **Who did the work**, **Where**, each with its sourced value or "No reliable figure for this era" (shown in muted ink, never left blank). Each row has a small ⓘ that opens its source line.
Panel: the stop's title and two or three sentences; a **Compare with** picker (any other stop) that splits the ledger card into two columns.

### Forces
Same slider and building view, smaller. Panel: a deck of ten **force cards** (Content). Drag a card onto a stop on the timeline (or select a card, then tap a stop; keyboard: Enter picks a card, arrows move between stops, Enter places). A card placed where it belongs locks with a ✓ and its evidence line; placed where it doesn't, it slides back with a one-line hint naming its real decade ("Not yet: phones in every pocket came after 2007."). Two cards fit more than one stop, and one decoy fits none (Content). A counter reads "Placed 4 of 11". **Reset cards**. No score beyond the counter, no timer.

### Costs
Stage: two charts drawn in code on the same years axis (2006 to 2028):
- **Share of U.S. electricity used by data centers**: points 2006 1.5 percent, 2014 1.8 percent, 2023 4.4 percent; a dashed band for the 2028 projection, 6.7 to 12 percent, labeled "projected".
- **Average power usage effectiveness (PUE)**: 2007 2.5, 2024 1.56, with the line "PUE = all the power the building uses / the power the computers use. 2.5 means 1.5 watts of cooling and other overhead for every watt of computing."
Panel: **Towns** section, three town cards (The Dalles, Oregon; Loudoun County, Virginia; Quincy, Washington) with what drew data centers there and one sourced cost or debate each; and a **What would you track?** checklist (electricity, water, land, jobs, noise, local taxes, chip mining and disposal) that fills a small "Your ledger for 2030" card, kept only on screen.

## Content
Stops (every number has a source in Sources; the build checks each one against its source and drops a number, never the stop, if the source does not confirm it):
1. **1946, ENIAC, Philadelphia.** Unveiled February 1946 at the University of Pennsylvania's Moore School. What it did: calculated artillery firing tables for the U.S. Army. Size: about 1,800 square feet, about 30 tons, about 17,468 vacuum tubes. Electricity: about 150 kilowatts while running. Water: no reliable figure. Who did the work: six women programmed it (Kathleen McNulty, Jean Jennings, Betty Snyder, Marlyn Wescoff, Frances Bilas, Ruth Lichterman), and for decades they were left out of its story. Where: a university campus.
2. **1951, UNIVAC I and the census.** The first UNIVAC was delivered to the U.S. Census Bureau in 1951. What it did: tabulated census data. Electricity, water: no reliable figure. Who did the work: operators and clerks who prepared data on tape. Where: a government office.
3. **1964, the airline booking network.** An airline's reservation system went live across the country in 1964, linking agents' terminals to two central computers. What it did: booked seats in real time. Size and electricity: no reliable figure; machine rooms of the era used raised floors and heavy air conditioning. Who did the work: reservation agents at terminals and operators on round-the-clock shifts. Where: a central computer center.
4. **1969, the first network link.** On October 29, 1969 the first message crossed ARPANET from UCLA to the Stanford Research Institute. What it did: let researchers share scarce, expensive computers at a distance. Electricity, water: no reliable figure. Who did the work: graduate students and engineers at universities and a defense research agency's contractors. Where: university campuses.
5. **1993, the web opens.** On April 30, 1993 CERN put the World Wide Web software in the public domain. What it did: anyone could publish pages from a server. Electricity, water: no reliable figure. Where: servers moved into office towers and shared "hosting" buildings in big cities.
6. **2006, rented computing and the river town.** In 2006 an online retailer began renting its computing and storage by the hour, and a search company opened a data center in The Dalles, Oregon, by Columbia River hydropower. Electricity: U.S. data centers used about 61 billion kWh in 2006, about 1.5 percent of U.S. electricity (EPA, 2007). Water: no national figure yet. Who did the work: construction crews, then a much smaller staff of technicians on shifts. Where: small towns with cheap power, fiber and tax breaks.
7. **2023, AI server farms.** Electricity: U.S. data centers used about 176 billion kWh (176 TWh) in 2023, about 4.4 percent of U.S. electricity; projected 6.7 to 12 percent by 2028 (Lawrence Berkeley National Laboratory, 2024). Water: about 66 billion liters (17 billion gallons) used directly for cooling in 2023 (same report). Who did the work: electricians and construction crews in the thousands during building; technicians and security staff once running. Where: campuses near power plants and substations, such as Loudoun County, Virginia.
Also on the Timeline, between stops 6 and 7, a note card: "2014: U.S. data centers used about 70 billion kWh, about 1.8 percent of U.S. electricity. Computing grew a lot from 2006 to 2014, but electricity barely did, because buildings got more efficient." (LBNL 2016)

Force cards (where they lock; evidence line):
- "War: the Army needed firing tables fast" → 1946. Evidence: ENIAC was funded by the Army's Ordnance Department.
- "Counting the nation" → 1951. Evidence: the first UNIVAC went to the Census Bureau.
- "Booking seats across the country, instantly" → 1964.
- "Research money to share expensive computers" → 1969. Evidence: ARPANET was built so researchers could use distant computers.
- "Free, open rules anyone could build on" → 1993.
- "Renting computing instead of buying it" → 2006.
- "Cheap electricity and tax breaks" → 2006 and 2023 (everywhere card).
- "Training and running large AI models" → 2023.
- "Air conditioning to carry away heat" → any stop from 1964 on (everywhere card). Placing it once on 1964, 1993, 2006 or 2023 locks it there and shows faint copies on the other three; it counts once.
- Decoy: "Phones in every pocket" → fits no stop (it came after 2007); hint "Not yet: phones in every pocket came after 2007." A "Doesn't fit any stop" tray under the timeline accepts it with a ✓.
Placements to finish: the seven single cards (7), "Cheap electricity" at 2006 and at 2023 (2), air conditioning (1), the decoy in the tray (1): 11.

Towns (Costs):
- The Dalles, Oregon: drawn by hydropower and fiber in 2006. Debate: in 2022 the city's newspaper went to court to make the city release how much water the data centers used; the records showed about 355 million gallons in 2021, about 29 percent of the city's water.
- Loudoun County, Virginia: the largest cluster of data centers in the world, by the county's own economic development office. Cost and debate: new power lines and substations across farmland and neighborhoods.
- Quincy, Washington: a farm town on cheap hydropower; data centers became its largest taxpayers. Cost and debate: diesel backup generators and air quality permits.

## Interactions in detail
- Slider snaps to the seven stops; the building view crossfades and the scale bar rescales; the person at the door stays 1.7 m so the size change is felt. With Motion off it switches without movement.
- Compare with shows two ledgers side by side; rows with no figure in both show one muted line.
- Forces: a card can be picked up again after it locks only with Reset cards. A wrong placement never costs anything. When all 11 are placed, the panel shows a short paragraph: "Every era's data center was built where money, power and a need met." (no celebration).
- Costs charts: hover or focus a point for its value and source; each chart has a text alternative listing its numbers. The 2028 band is hatched and labeled "projected", never drawn as data.
- What would you track?: checking items fills the ledger card; Copy puts its text on the clipboard. Nothing is saved.
- Keyboard: mode buttons, slider, panel, then the timeline stops; visible focus ring.
- Sizes: the slider, building view and ledger card fit without scrolling at 1366x768 and 1280x720; at 680x425 the building view shrinks above a compact ledger with two rows and a "More rows" toggle. Ledger text at least 13 px; preview text at least 10 px.

## Look
- Own light palette: `--paper #f4efe4` (archive paper), `--panel #ffffff`, `--ink #22201c`, `--muted #5c574c`, `--line #d8cfbd`, accent `--brand #0f6b5a` (deep archive teal: slider thumb, ticks, header rule, locked cards) with white text on it, a second ink `#8a4b14` (copper, for the power line and electricity values).
- Building drawings: line art in ink on paper with teal for the current stop's building, copper for power lines, blue `#2b5d8a` for water rows.
- Contrast (computed): brand on paper 5.60:1, on white 6.42:1; white on brand 6.42:1; ink on paper 14.18:1; muted on paper 6.27:1; copper on paper 5.91:1. All pass AA; values never rely on color alone (labels and icons on every row).
- Neighbors: data-policy-council is navy on paper; the other 9-12 CS tools are dark (pink, violet, lemon, sky blue, orange). Teal on archive paper is unused.

## Art
none: drawn in code (seven building line drawings, the scale figure as a plain silhouette, charts, preview.svg: the slider at 2023 with the campus drawing and the ledger).

## Voice
Bank voice `knowing-guide`, style "Say in a knowledgeable, friendly way, like a museum curator": a curator walking a gallery of buildings. Not used by a 9-12 CS tool or a group sibling. Light narration:
1. how, welcome (Timeline): "Drag the slider through time. Watch the building grow, and read the ledger for what it cost."
2. event, first arrival at 1946 by the slider (stale if the slider has moved on): "Six women programmed this machine. For decades, almost no one knew their names."
3. event, arrival at 2023 (stale if moved on): "Same job, a much bigger building. Look at the electricity row."
4. how, welcome (Forces): "Drag each force onto the year it shaped. Some fit more than one year."
5. how, welcome (Costs): "These lines are the cloud's power bill. Tap a town to see who pays it."
Read speaks the hint. Numbers are never spoken.

## Family engine
none

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- ENIAC (1946 unveiling, size, tubes, power, Army funding, the six programmers): Penn Engineering, "ENIAC": https://www.seas.upenn.edu/about/history-heritage/eniac/ ; Encyclopaedia Britannica, "ENIAC": https://www.britannica.com/technology/ENIAC ; ENIAC Programmers Project: https://eniacprogrammers.org/
- UNIVAC I delivered to the Census Bureau, 1951: U.S. Census Bureau, "UNIVAC I": https://www.census.gov/about/history/bureau-history/census-innovations/technology/univac-i.html
- Airline reservation system live 1964: IBM History, "Sabre: the first online reservation system": https://www.ibm.com/history/sabre
- First ARPANET message, October 29, 1969, and its purpose: Internet Society, "Brief History of the Internet": https://www.internetsociety.org/internet/history-internet/brief-history-internet/
- Web software public domain, April 30, 1993: CERN, "The birth of the Web": https://home.cern/science/computing/birth-web
- Rented computing launched 2006: Amazon press release on S3, March 14, 2006 (company kept off screen): https://press.aboutamazon.com/
- The Dalles data center, 2006: The New York Times, "Hiding in Plain Sight, Google Seeks More Power", June 14, 2006; water records 2021: The Oregonian/OregonLive, December 2022 coverage of the city's release after the lawsuit.
- 2006: 61 billion kWh, 1.5 percent: U.S. EPA ENERGY STAR, "Report to Congress on Server and Data Center Energy Efficiency", August 2, 2007.
- 2014: about 70 billion kWh, 1.8 percent: Shehabi et al., "United States Data Center Energy Usage Report", LBNL, June 2016.
- 2023: 176 TWh, 4.4 percent; 2028 projection 6.7 to 12 percent; direct water about 66 billion liters: Shehabi et al., "2024 United States Data Center Energy Usage Report", LBNL, December 2024: https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- Average PUE 2.5 (2007) and 1.56 (2024): Uptime Institute, Global Data Center Survey 2024: https://uptimeinstitute.com/
- Loudoun County, largest data center market: Loudoun County Department of Economic Development, "Data Centers": https://biz.loudoun.gov/key-business-sectors/data-centers/
- Quincy, Washington data centers and generator permits: Washington State Department of Ecology, Quincy data center air permits: https://ecology.wa.gov/
- Building drawings are illustrations at the stated sizes; where no size is sourced, the drawing says "not to scale".

## Done when
1. The slider has seven stops; 1946 shows about 1,800 square feet, 17,468 tubes, 150 kilowatts, and names all six programmers.
2. 2006 shows 61 billion kWh and 1.5 percent; 2023 shows 176 TWh, 4.4 percent and 66 billion liters; 1951 to 1993 show "No reliable figure" rows in muted ink.
3. Compare with 1946 and 2023 shows two ledgers side by side.
4. Forces: "Phones in every pocket" placed on 2006 slides back with the after-2007 hint; placed in the tray it locks; "Cheap electricity" locks at both 2006 and 2023; the counter reaches 11.
5. Costs: the electricity chart has three points and a hatched 2028 band labeled "projected"; PUE shows 2.5 and 1.56 with the explanation line.
6. Each ⓘ opens a source line that matches Sources; the verify agent spot-checks five numbers against their sources.
7. Slider, building and ledger fit without scrolling at 1366x768; the light palette passes the stated ratios.
8. Voice: line 2 does not play when the slider passes 1946 quickly to another stop; each how-line plays once in five actions.

## Open questions
- [cloud-through-time] Company names stay off screen ("an online retailer", "a search company", "an airline"), but towns and ENIAC/UNIVAC are named. Is that the right line for history?
- [cloud-through-time] The Dalles water figures (355 million gallons, 29 percent, 2021) come from newspaper coverage, not a government report. Keep them, or show only that the records were released after a lawsuit?
