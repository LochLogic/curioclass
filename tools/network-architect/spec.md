# Network Architect

## One idea
Wire a whole high school on its floor plan (core switch, access switches, Wi-Fi, fiber or copper runs, subnets and firewall rules) and then run the same tests a real network team would (reach, cable length, ports, Wi-Fi load, addresses, peak traffic, security, a cable cut, budget), where every failure points at the exact room, cable or rule that broke.

## Not like
- packet-race (6-8, same family): steers packets live on a given map. Here you buy and place the network and nothing moves until you test it.
- network-help-desk (grade 4, same family): diagnoses one home device by asking. Here you prevent problems across a building with design rules and measured tests.
- internet-journey (grade 3, same family): a message's trip as a story. Here the internet is one handoff line in the server room.
- capture-the-flag (9-12, same wave group): finds and patches holes in made-up systems. Here security is one test among nine: firewall rules between networks you designed.
- computer-builder (grade 1, built builder): one computer's parts. Here a building of networks.
- api-playground, simulation-studio (9-12): software and data; nothing physical.

## Who and how
- Grades 9 to 12, computer science. Module: Networks of Networks (Systems and Security), "Diagram networks; how the internet works".
- Topic line: "designing and testing a school network".
- Driver: students, one laptop each or pairs. 30 to 45 minutes (Sample 5 min, a first passing design 25 to 40 min).
- Standards (CSTA 2026, as listed): HS-SYS-NT-34, HS-SYS-NT-35, HS-SYS-HW-29. 2017 crosswalk: 3A-NI-04 (scalability and reliability: routers, switches, servers, topology, addressing), 3B-NI-03 (bandwidth, load, delay, topology), 3A-CS-02 (levels of interaction between hardware and software).
- tool.json: driver "students", minutes "30-45", modes ["Sample", "Build"], grades_label "Grades 9-12". Kit starter with `kit:theme-912` and `kit:network`.

## Screens and modes
Header (kit, 9-12 theme): "Network Architect", small line "Juniper Ridge High School". Mode buttons: **Sample** (opens first), **Build**. Then Motion, Sound, Read.

Stage: a blueprint floor plan of the made-up Juniper Ridge High School (180 m by 100 m, Content), at real pixel size per box with a scale bar ("20 m"). Rooms are outlined boxes with their name and device chips ("12 desktops, Staff, wired"). Equipment sits on a room's shelf (a row inside the room). Cables are drawn as corridor-style elbows (horizontal then vertical) with their length label; copper amber solid, fiber violet with a dashed core line; a run over its limit is red, dashed, labeled "150 m: over 100 m copper limit". Bundles (two or more cables between the same pair) draw as one line with "x2".

Panel (`.sec` cards, scrolls inside itself; Run tests and Budget pinned at the top):
1. **Budget**: "30,300 of 32,000 credits" and **Run tests** (big button).
2. **Parts**: Core switch, Access switch, Access point (each with cost and specs), then **Cable** with **Copper** / **Fiber** toggle, then **Remove** (removes the selected item or cable). Internet plan: **1 Gbps** (included) / **2 Gbps** (+4,000).
3. **Networks**: a table: Staff, Students, Guest, Cameras, Servers; devices; size select (/26, /25, /24, /23, /22); usable addresses.
4. **Rules**: an Allow/Block matrix. Rows (from): Staff, Students, Guest, Cameras. Columns (to): Internet, Records server, Video recorder, Staff, Students, Guest, Cameras (a network to itself is always Allow, greyed). Cells R7 does not name (Staff to Students, Guest or Cameras) may be either.
5. **Report**: the test report (monospace) and the Brief checklist R1 to R9 with PASS/FAIL marks after a run.

### Mode 1: Sample (explore)
The finished sample design (Content) is loaded and passes every test. Tap any cable to cut it (it shows a break) or any switch to power it off. Within 300 ms the plan shades every room that lost the internet (hatched, with "offline" label) and the Report panel lists who lost what ("Gym: guests lost internet; cameras lost the video recorder"). Tap again to restore. **Reset sample** restores all. **Copy to Build** loads the sample into Build to change.

### Mode 2: Build
Starts empty except the fixed server room items: Internet handoff, Firewall (cabled to the handoff, fixed), Records server, Video recorder. Place parts by choosing a part then tapping a room (up to 4 items per room shelf, 10 in the Gym). Cable: choose Copper or Fiber, tap one end then the other (equipment, or a room's wired device chip, which takes one port per device). The cable's length shows as it is placed. Wireless chips need no cable: they use the access points in the same room. Run tests writes the report; nothing is checked live except the budget and cable lengths. **Clear design** (confirm Yes/No). The design saves on this device (localStorage `curio-network-architect`) with **Clear saved**.

## Content
Rooms (center x, y in meters; size): Server room SR (40, 50; 10 x 10), Office OF (20, 20; 24 x 16), Library LB (40, 85; 30 x 18), Classrooms A1 to A6 (75, 90, 105, 120, 135, 150 by 20; 13 x 16 each), Gym GY (165, 75; 28 x 34).
Cable length = |dx| + |dy| between the two room centers + 10 m slack (5 m each end); the same room is 10 m. Computed from SR: OF 60, LB 45, A1 75, A2 90, A3 105, A4 120, A5 135, A6 150, GY 160. From A2: A1 25, A3 25, A4 40, A5 55, A6 70. Limits: copper 100 m, fiber 300 m.

Device chips (network, count, wired or wireless, Mbps each at the 10 a.m. test / the 7 p.m. game night test, target):
- OF: desktops, Staff, 12 wired, 2 / 0, internet. Printers, Staff, 2 wired, 0 / 0. Staff laptops and phones, Staff, 6 wireless, 2 / 2, internet.
- LB: desktops, Students, 4 wired, 5 / 0, internet. Laptops, Students, 30 wireless, 5 / 0, internet.
- A1 to A6, each: Chromebooks, Students, 30 wireless, 5 / 0, internet. Teacher laptop, Staff, 1 wireless, 2 / 0, internet.
- GY: cameras, Cameras, 4 wired, 6 / 6, video recorder. Visitors, Guest, 300 wireless, 0 / 1, internet.
- SR (fixed): Records server and Video recorder, Servers.
Totals (computed): 10 a.m. internet 1,118 Mbps (students 1,070, staff 48); cameras 24 Mbps to the recorder. Game night internet 312 Mbps (guests 300, staff 12); cameras 24.
Address need = devices + 1 gateway: Staff 27, Students 215, Guest 301, Cameras 5, Servers 3. Usable addresses per size (2 to the power of host bits, minus 2): /26 62, /25 126, /24 254, /23 510, /22 1,022. Default size /24 for all (so Guest fails until it is /23 or larger).

Parts (specs and costs are Curio Class model values in credits, shown as such):
- Core switch: 48 copper ports at 1 Gbps, 4 fiber ports at 10 Gbps; 6,000.
- Access switch: 24 copper ports at 1 Gbps plus 2 uplink ports (copper 1 Gbps or fiber 10 Gbps); 1,500.
- Access point: plan 40 clients each (a model rule); one copper port; 600.
- Firewall (fixed, already placed): 5 Gbps throughput, 8 copper and 2 fiber ports; 5,000 (counted in the budget).
- Copper run: 0 credits, 1 Gbps, up to 100 m. Fiber run: 300 credits, 10 Gbps, up to 300 m.
- Internet plan: 1 Gbps included; 2 Gbps adds 4,000. Budget 32,000.
A bundle of parallel cables between the same two items adds their speeds (link aggregation). A link is overloaded above 80 percent.

Requirements (the Brief, R1 to R9, each a test):
- R1 Reach: every device chip reaches its target (internet via the firewall, or the video recorder).
- R2 Cables: every copper run 100 m or less, every fiber run 300 m or less; fiber only between switches, the core and the firewall.
- R3 Ports: no item uses more copper, fiber or uplink ports than it has.
- R4 Wi-Fi: every room with wireless chips has at least ceil(clients / 40) access points (OF 1, LB 1, each A room 1, GY 8).
- R5 Addresses: every network's size fits its address need.
- R6 Traffic: at both tests no link, the firewall or the internet plan is above 80 percent.
- R7 Security: Guest reaches only the internet; Students reach the internet only (not the Records server, Video recorder, Staff or Cameras); Cameras reach only the Video recorder; Staff reach the internet, Records server and Video recorder. (Default rules are all Allow, as the old network was.)
- R8 Cut: cut any one cable that joins two of these (an access switch, the core switch, the firewall; each cable of a bundle counts on its own) and every office chip still reaches the internet, and Staff still reach the Records server. Cables to access points and device chips, and the fixed handoff line, are not cut.
- R9 Budget: total 32,000 credits or less.

Report lines (one per test; examples of format): `R2 CABLES  FAIL  A6 access point: 150 m copper (limit 100 m)`; `R5 ADDRESS FAIL  Guest needs 301 addresses; /24 gives 254`; `R6 TRAFFIC FAIL  10 a.m.: A2 switch uplink 912 of 1000 Mbps (91%)`; `R7 SECURITY FAIL  Guest to Records server is Allow (should be Block)`; `R9 BUDGET  PASS  30,300 of 32,000`. Every FAIL line is a button that highlights the room, cable or rule cell.

Sample design (passes all nine; computed): core switch in SR; office access switch in OF with 2 copper uplinks to the core (60 m, bundle 2 Gbps), OF chips on it plus 1 AP (15 of 24 ports); library desktops (4) and 1 AP cabled straight to the core (45 m); A wing access switch in A2 with 1 fiber uplink (90 m) and 6 APs on copper (A1 25, A2 10, A3 25, A4 40, A5 55, A6 70 m); gym access switch in GY with 1 fiber uplink (160 m), 8 APs and the 4 cameras (12 of 24 ports); core to firewall 2 fiber (10 m, bundle 20 Gbps); Records server and Video recorder on the core (10 m); internet plan 2 Gbps; sizes Staff /26, Students /24, Guest /23, Cameras /26, Servers /26; rules as R7. Cost: 5,000 + 6,000 + 3 x 1,500 + 16 x 600 + 4 x 300 + 4,000 = 30,300. Loads at 10 a.m.: internet 1,118 of 2,000 (56%), firewall 22%, core-firewall 6%, A2 uplink 912 of 10,000 (9%). Game night: internet 16%, gym uplink 324 of 10,000 (3%).
Known traps the tests catch: one copper uplink for the whole A wing (912 of 1,000, 91%); one copper core-to-firewall link (1,118 of 1,000); the 1 Gbps internet plan (112%); a copper run to the gym (160 m) or to A3 and beyond from SR; Guest at /24; default Allow rules; a single core-to-firewall cable (fails R8).

## Interactions in detail
- Selecting: tap an item to select (outline and "selected" tag); Delete or Remove removes it and its cables. Tapping a cable selects it.
- Flows: each chip's demand goes along `net.path` (by hops, ties to the lower index) to its target; firewall rules apply where the path crosses the firewall (all paths between networks do: the firewall routes between them). Loads sum per link (a bundle is one link with summed speed) and on the firewall and internet plan.
- Cut test (R8): for each equipment-to-equipment cable (each member of a bundle counts separately), mark it down, recheck reach for the office chips and Staff to Records server; the first failing cable is named.
- A cable longer than its limit still places (red) so students see why; fiber between a chip and a switch is refused with a tip ("Fiber connects network equipment; devices use copper").
- Budget updates live, red text plus "over" when above 32,000.
- Motion off: no shading fade or cable draw animation. No celebration: an all-PASS report adds one line "All nine requirements pass."
- Sizes: plan left, panel right at 1000 wide and up; under 900 px tall Budget and Run tests stay pinned and the panel scrolls; at 760 wide the panel goes under the plan with Run tests first; at 375 wide the plan pans and zooms inside its box (pinch or + and - buttons) and room labels stay 12 px or more. Run tests visible without page scrolling at every size in STANDARDS.md.
- Keyboard: Tab goes modes, header, Budget, Run tests, Parts, Networks, Rules, Report, then rooms and items; Enter places the chosen part in a focused room; C starts a cable from the focused item.
- `window.__tool = {state, net, setMode, load(design), test()}`; `test()` returns the nine results with numbers.

## Look
Accent `--brand #7cc4ff` (blueprint sky blue) on the 9-12 theme. `--brand-ink #0b1a2a`.
- Plan: blueprint `#0f2238` with a 5 m grid `#1d3a5c` and walls `#cfe3f7`; labels `#e8edf3`, chips `#a6b3c4`; copper `#e8c07a` solid; fiber `#c9a0ff` with a dashed core; over-limit and FAIL `#ff8a8a` dashed with a text label; equipment tiles `#9fe0c9` (switches) and `#7cc4ff` (access points) with ink glyphs; offline rooms hatched with an "offline" label.
- Contrast (computed): brand on theme panel `#141b25` 9.23:1, on `--sec-bg` 8.75:1; brand-ink on brand 9.37:1; walls on blueprint 12.24:1; labels 13.66:1; chips 7.55:1; copper 9.38:1; fiber 7.62:1; FAIL red 7.08:1; switch tiles 10.70:1. All pass AA; line kinds also differ by dash pattern, never color alone.
- Neighbors: theme default amber is left to other 9-12 tools; capture-the-flag uses pink on the same theme; packet-race red on paper.

## Art
none: drawn in code. Plan, equipment glyphs, cables and preview.svg are SVG.

## Voice
Bank voice `calm-professor` (Schedar), "Say evenly and clearly, like a calm, friendly college professor". Not used by any CS neighbor or group sibling. 9-12: narration is short and rare; report lines are read on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-sample (how, Sample welcome): "This design passes every test. Tap a cable or a switch to break it, and see which rooms go dark."
- w-build (how, Build welcome): "Pick a part, then tap a room to place it. Cable it up, then press Run tests."
- cable (how, first cable started): "Tap the other end. Copper reaches 100 meters; fiber reaches 300."
- fails (event, a run with failures; stale on the next run): "Some tests failed. Tap a failed line to see where."
- pass (event, all nine pass; stale on any change): "All nine requirements pass."

## Family engine
`kit/network.js`, described in full in tools/internet-journey/spec.md. This tool uses: **Graph** (built by the player: equipment nodes, chip nodes, cable links with `medium`, `mbps`, `lenM`; bundles merged by the tool), **Path/reach** (R1, R7, R8, and Sample's offline shading), **flows** (R6 loads), and **Draw** with a blueprint skin (rooms drawn by the tool; corridor elbows for links). No Mover or Packets.

## Sources
- CSTA 2026 ids HS-SYS-NT-34, HS-SYS-NT-35, HS-SYS-HW-29 (`data/standards/csta-2026-ids.txt`); CSTA 2017 3A-NI-04, 3B-NI-03, 3A-CS-02: https://csteachers.org/k12standards/
- Twisted-pair copper Ethernet channels are limited to 100 m: ANSI/TIA-568.2-D (balanced twisted-pair channel, 100 m) and IEEE 802.3 clauses for 1000BASE-T and 10GBASE-T (100 m reach).
- 10 Gb/s over multimode fiber (10GBASE-SR on OM3) reaches 300 m: IEEE 802.3ae (10 Gigabit Ethernet), clause 52.
- Usable IPv4 host addresses in a subnet are 2 to the power of host bits minus 2 (network and broadcast): RFC 950 and RFC 4632 (CIDR), https://www.rfc-editor.org/rfc/rfc4632
- Link aggregation combines parallel links into one logical link: IEEE 802.1AX.
- Firewalls control traffic between network segments; keep guest and device (camera) networks separate: CISA, "Layering Network Security Through Segmentation" (infographic, 2022), cisa.gov; NIST SP 800-41 Rev. 1, "Guidelines on Firewalls and Firewall Policy", https://csrc.nist.gov/pubs/sp/800/41/r1/final
- Streaming HD video at about 5 Mbps per stream (basis for the 5 Mbps model value): Netflix Help Center, "Internet connection speed recommendations", https://help.netflix.com/en/node/306
- Planning about 1 Mbps per student of internet as a school target (context for the internet plan): SETDA, "The Broadband Imperative III" (2019), https://www.setda.org
- Part costs, port counts, 40 clients per access point, the 80 percent line and the school are Curio Class model values, labeled as such on screen.

## Done when
1. Sample loads and `test()` returns all nine PASS with the Content numbers (cost 30,300; internet 56%; A2 uplink 9%).
2. In Sample, cutting the A2 fiber hatches A1 to A6 as offline; cutting one of the two office uplinks changes nothing; Reset sample restores.
3. Build traps each fail the right test with the right line: one copper A-wing uplink (91%), 1 Gbps plan (112%), copper SR to GY (160 m), Guest /24 (301 vs 254), default Allow rules, single core-to-firewall cable (R8).
4. Cable lengths match the Content table for every room pair used in the sample.
5. Fiber to a device chip is refused with the tip; a red over-limit cable still places.
6. Budget is live and correct; Clear design and Clear saved both confirm first; a saved design reloads after refresh.
7. Every size in STANDARDS.md: Run tests and Budget visible without page scrolling; 375 wide pans and zooms the plan.
8. Keyboard-only build of a passing design is possible; Motion off; console clean; no network requests; the name only as "Curio Class".
