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
Stage, top: the **era slider** with seven stops (1946, 1951, 1964, 1969, 1993, 2006, 2023), each a labeled tick; drag or use Previous and Next. Focus: the building view, the largest thing on the stage, between the slider and the ledger. Middle: the **building view**: the stop's painted building (art `ct-stop-*`, cutouts) standing on a code-drawn ground line beside a code-drawn scale bar and a plain 1.7 m silhouette at the door (a shape, not a person picture): ENIAC's room, a census machine room, a mainframe room with raised floor and air handlers, a pair of network machine cabinets on two campuses joined by a code-drawn line, a server room in an office tower, a warehouse-sized hall by a river with a power line, a campus of halls with a substation. Each painting is scaled so its footprint matches the sourced size where there is one; where there is none, the view says "not to scale". At each stop the scale bar rescales smoothly (no animation with Motion off) and a footprint label gives the size where a source has one. Bottom: the **ledger card** for the stop: rows **What it did**, **Size**, **Electricity**, **Water**, **Who did the work**, **Where**, each with its sourced value or "No reliable figure for this era" (shown in muted ink, never left blank). Each row has a small ⓘ that opens its source line.
Panel: the stop's title and two or three sentences; a **Compare with** picker (any other stop) that splits the ledger card into two columns.

### Forces
Focus: the timeline stops, where cards land; the building view shrinks above them. Same slider and building view, smaller. Panel: a deck of ten **force cards** (Content). Drag a card onto a stop on the timeline (or select a card, then tap a stop; keyboard: Enter picks a card, arrows move between stops, Enter places). A card placed where it belongs locks with a ✓ and its evidence line; placed where it doesn't, it slides back with a one-line hint naming its real decade ("Not yet: phones in every pocket came after 2007."). Two cards fit more than one stop, and one decoy fits none (Content). A counter reads "Placed 4 of 11". **Reset cards**. No score beyond the counter, no timer.

### Costs
Focus: the electricity chart. Stage: two charts drawn in code on the same years axis (2006 to 2028):
- **Share of U.S. electricity used by data centers**: points 2006 1.5 percent, 2014 1.8 percent, 2023 4.4 percent; a dashed band for the 2028 projection, 6.7 to 12 percent, labeled "projected".
- **Average power usage effectiveness (PUE)**: 2007 2.5, 2024 1.56, with the line "PUE = all the power the building uses / the power the computers use. 2.5 means 1.5 watts of cooling and other overhead for every watt of computing."
Panel: **Towns** section, three town cards, each with its painted picture (art `ct-town-*`) (The Dalles, Oregon; Loudoun County, Virginia; Quincy, Washington) with what drew data centers there and one sourced cost or debate each; and a **What would you track?** checklist (electricity, water, land, jobs, noise, local taxes, chip mining and disposal) that fills a small "Your ledger for 2030" card, kept only on screen.

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
- Decoy: "Sending telegrams by wire" → fits no stop (the telegraph came in the 1840s, a century before the first stop); hint "Not here: the telegraph came in the 1840s, a century before ENIAC." A "Doesn't fit any stop" tray under the timeline accepts it with a ✓.
Placements to finish: the seven single cards (7), "Cheap electricity" at 2006 and at 2023 (2), air conditioning (1), the decoy in the tray (1): 11.

Towns (Costs):
- The Dalles, Oregon: drawn by hydropower and fiber in 2006. Debate: in 2022 the city's newspaper went to court to make the city release how much water the data centers used; the records showed about 355 million gallons in 2021, about 29 percent of the city's water.
- Loudoun County, Virginia: the largest cluster of data centers in the world, by the county's own economic development office. Cost and debate: new power lines and substations across farmland and neighborhoods.
- Quincy, Washington: a farm town on cheap hydropower; data centers became its largest taxpayers. Cost and debate: diesel backup generators and air quality permits.

## Interactions in detail
- Nothing plays on its own. The slider and the crossfade (400 ms) never block: dragging past a stop mid-fade shows the newer stop at once.
- Slider snaps to the seven stops; the building view crossfades and the scale bar rescales; the person at the door stays 1.7 m so the size change is felt. With Motion off it switches without movement.
- Compare with shows two ledgers side by side; rows with no figure in both show one muted line.
- Forces: a card can be picked up again after it locks only with Reset cards. A wrong placement never costs anything. When all 11 are placed, the panel shows a short paragraph: "Every era's data center was built where money, power and a need met." (no celebration).
- Costs charts: hover or focus a point for its value and source; each chart has a text alternative listing its numbers. The 2028 band is hatched and labeled "projected", never drawn as data.
- What would you track?: checking items fills the ledger card; Copy puts its text on the clipboard. Nothing is saved.
- Keyboard: mode buttons, slider, panel, then the timeline stops; visible focus ring.
- Sizes: the slider, building view and ledger card fit without scrolling at 1366x768 and 1280x720; at 680x425 the building view shrinks above a compact ledger with two rows and a "More rows" toggle. Ledger text at least 13 px; preview text at least 10 px.

## Look
- Own light palette: `--paper #f4efe4` (archive paper), `--panel #ffffff`, `--ink #22201c`, `--muted #5c574c`, `--line #d8cfbd`, accent `--brand #0f6b5a` (deep archive teal: slider thumb, ticks, header rule, locked cards) with white text on it, a second ink `#8a4b14` (copper, for the power line and electricity values).
- Buildings: painted cutouts on the archive paper, with a teal outline under the current stop's building, copper for code-drawn power lines in the view and electricity values, blue `#2b5d8a` for water rows.
- Contrast (computed): brand on paper 5.60:1, on white 6.42:1; white on brand 6.42:1; ink on paper 14.18:1; muted on paper 6.27:1; copper on paper 5.91:1. All pass AA; values never rely on color alone (labels and icons on every row).
- Neighbors: data-policy-council is navy on paper; the other 9-12 CS tools are dark (pink, violet, lemon, sky blue, orange). Teal on archive paper is unused.

## Art
Local FLUX (`scripts/localart.py`), no people (rooms and buildings are shown empty; the people who did the work are named in the ledger). One style: clean isometric painted cutaway on a plain background, the same angle and light for every stop so the size change reads. Charts, the slider, scale bar, silhouette, ledger and force cards stay code.
- ct-stop (kit of 7, one cutout each, one prompt line): "Isometric painted cutaway of {a long room lined with tall black panels of glowing vacuum tubes, cables and plugboards, 1940s | a 1950s machine room with tall grey cabinets, big reels of magnetic tape and a control desk | a 1960s computer room with a raised white tile floor, rows of blue cabinets, tape drives and large air conditioning units | one refrigerator-sized grey computer cabinet with blinking lights on a small stand | a 1990s server room on one floor of a glass office tower, racks of beige servers and a tangle of cables | a long warehouse-sized windowless data hall beside a wide river with a power line and tall towers | a campus of several huge windowless data halls with cooling units on the roofs and a fenced electrical substation}, a still and quiet scene, soft even light, plain white background"; 16:9 (the 1969 cabinet 1:1); cutout yes; people no; stops 1946, 1951, 1964, 1969, 1993, 2006, 2023. Sizing: each sits on the ground line scaled by its sourced footprint against the 1.7 m silhouette; 1969 shows the one cabinet twice, at UCLA and at SRI, with the code-drawn link between.
- ct-town (kit of 3, one prompt line): "{A small river city on a wide river below dry hills, a big dam in the distance and long windowless data halls at the edge of town | farmland and suburban houses crossed by a new line of tall steel power towers, long data halls behind them | flat farm fields with irrigation circles and low windowless buildings beside rows of boxy backup generators}, late afternoon, soft painted illustration"; 4:3; cutout no; people no; The Dalles, Loudoun County, Quincy; the top of each town card.
The preview.svg is code (the slider at 2023 with the campus cutout and the ledger).

## Voice
Bank voice `knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a museum curator": a curator walking a gallery of buildings. Not used by a 9-12 CS tool or a group sibling. `Curio.voice`, `scope: () => state.mode`. Light narration; Read speaks the hint. Numbers are never spoken.
1. wTimeline (how; Timeline entered; stale when the slider moves): "Drag the slider through time, or press Next. Watch the building grow, and read the ledger for what it cost."
2. eniac (event; first arrival at 1946 by the slider, after it rests there 1 s; stale if the slider has moved on): "Six women programmed this machine. For decades, almost no one knew their names."
3. bigger (event; first arrival at 2023, after it rests there 1 s; stale if moved on): "Same job, a much bigger building. Look at the electricity row."
4. wForces (how; Forces entered; stale when a card is placed): "Drag each force card onto the year it shaped, or tap a card and then tap a year. Some fit more than one year."
5. wCosts (how; Costs entered; stale when a town card is opened): "These lines are the cloud's power bill. Tap a town card to see who pays it."
6. allPlaced (event; all 11 placed; stale when Reset cards is pressed): "Every era's data center was built where money, power and a need met." 

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
- Building paintings are illustrations scaled to the stated sizes; where no size is sourced, the drawing says "not to scale".
- Telegraph decoy: Library of Congress, "Samuel F. B. Morse Papers": first public telegraph message, May 24, 1844, https://www.loc.gov/collections/samuel-morse-papers/
- Checks run (Python, 2026-10-29): kWh and percent agree on total U.S. use (61 / 1.5% = 4,067 TWh in 2006, 70 / 1.8% = 3,889 in 2014, 176 / 4.4% = 4,000 in 2023); 66 billion liters = 17.4 billion gallons, matching "about 17"; PUE 2.5 means 1.5 W of overhead per watt of computing and 1.56 means 0.56 W. Placements total 11 (7 single cards, cheap electricity twice, air conditioning once, the decoy once). Found and fixed: the first decoy, "Phones in every pocket", told students it fit no stop because it came after 2007, but 2023 is after 2007; a student placing it at 2023 would have been told a true link was wrong. It is now a telegraph card that predates every stop.

## Done when
1. The slider has seven stops; 1946 shows about 1,800 square feet, 17,468 tubes, 150 kilowatts, and names all six programmers.
2. 2006 shows 61 billion kWh and 1.5 percent; 2023 shows 176 TWh, 4.4 percent and 66 billion liters; 1951 to 1993 show "No reliable figure" rows in muted ink.
3. Compare with 1946 and 2023 shows two ledgers side by side.
4. Forces: "Sending telegrams by wire" placed on any stop slides back with the 1840s hint; placed in the tray it locks; "Cheap electricity" locks at both 2006 and 2023; the counter reaches 11.
5. Costs: the electricity chart has three points and a hatched 2028 band labeled "projected"; PUE shows 2.5 and 1.56 with the explanation line.
6. Each ⓘ opens a source line that matches Sources; the verify agent spot-checks five numbers against their sources.
7. Slider, building and ledger fit without scrolling at 1366x768; the light palette passes the stated ratios.
8. Voice: line 2 does not play when the slider passes 1946 quickly to another stop; each how-line plays once in five actions.
9. Focus: the building view is the largest thing on the Timeline stage at 1366x768 and in the 680x425 preview; the 1946 and 2023 buildings differ in drawn size against the same silhouette.
10. Taps during a crossfade: dragging or pressing Next mid-fade shows the newest stop at once, with no old building left behind.
11. Art: seven stop cutouts and three town pictures load; no image shows a person.

## Open questions
- [cloud-through-time] Company names stay off screen ("an online retailer", "a search company", "an airline"), but towns and ENIAC/UNIVAC are named. Is that the right line for history?
- [cloud-through-time] The Dalles water figures (355 million gallons, 29 percent, 2021) come from newspaper coverage, not a government report. Keep them, or show only that the records were released after a lawsuit?
- [cloud-through-time] The Dalles debate line says the newspaper went to court to make the city release the water records. As I recall the coverage, it was the city that sued to block The Oregonian's records request, and it settled and released them in December 2022. The build's fact check should confirm and reword (content facts were left as they were).
- [cloud-through-time] The 1946 stop is about the six women, but the art shows ENIAC's room empty. Use the U.S. Army's public-domain photo of ENIAC with its programmers instead (no generated people)?
- [cloud-through-time] Decoy changed from "Phones in every pocket" (it truly fits 2023) to a telegraph card. OK?
