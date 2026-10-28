# Internet Journey

## One idea
Your party invite to a friend breaks into eight numbered pieces that hop through the real stops of the internet (your Wi-Fi router, your internet provider, routers, the message app's server) and rebuild on your friend's tablet, and at each stop you make one choice about what you share, so the closing map shows exactly where your words, and any private details you added, now live.

## Not like
- network-help-desk (grade 4, same family): diagnoses why one device can't get online. Here nothing is broken; you ride along with a message and the story is about what you put in it.
- packet-race (6-8, same family): you steer packets against a clock. Here the route is told as a story with no clock, and the one route choice only changes the timing.
- network-architect (9-12, same family): builds a network. Here the network is given and fixed.
- data-defenders (grade 5): protects a school's stored data. Here the data is your own message, in motion.
- computer-builder (grade 1, built): parts of one computer. Here many machines pass a message along.
- score-keeper, code-tracer (grades 3 to 4, built): programs and variables, no networks.

## Who and how
- Grade 3, computer science. Module: How We Use the Internet (Systems and Security), "Getting information online and protecting personal details".
- Topic line: "how a message travels online, and keeping personal info private".
- Driver: students or teacher. Pairs on laptops, or the teacher on a projector with the class voting on each choice by hands.
- 15 to 20 minutes: Story once (10 min), a second run with different choices (5 min), Trip map (5 min).
- Standards (CSTA 2026, as listed for the module): E3-SYS-NT-14, E3-SYS-SE-13, E3-SYS-IM-15. 2017 crosswalk: 1B-NI-04 (information is broken into packets, sent through many devices and reassembled), 1B-NI-05 (how personal information can be protected).
- tool.json: driver "students or teacher", minutes "15-20", modes [] (story and explore, no score), grades_label "Grade 3". Start from `kit/starter/src.html`, family engine `kit:network`.

## Screens and modes
Header (kit): title "Internet Journey", small line "Where does a message go?". Mode buttons: **Story** (opens first), **Trip map**. Then Motion, Sound, Read.

Stage (both modes): the network map drawn by the engine across the full stage, with a soft dusk sky behind it. Eleven stops from left to right (Content). Under each stop its name in 14 px or more. A dotted trail lights up as pieces travel. On the far right, Juno's tablet shows a slot strip of 8 numbered boxes where pieces land.

Story panel: chapter number and title ("Stop 3 of 7: Your internet provider"), the story text (2 to 3 short sentences), then the choice as two big cards with icons (min 64 px tall). A **Next** button (arrow) appears after the pieces finish moving. **Start over** (circular arrow) at the bottom.

Trip map panel: `#hint`, **Send a test** (paper plane), **Close a road** toggle (road-block icon, on router A), **Speed** (Slow / Quick), and the stop card (filled when a stop is tapped).

### Mode 1: Story (7 chapters)
Each chapter: the map pans so the current stop is centered (on wide screens the whole map shows and the stop gets a ring). The narrator reads the chapter text, the choice cards appear, the student taps one, a short result line shows (and is spoken), then the pieces move on to the next stop and Next appears. Choices are kept in `state.choices` for the ending.

Chapter 7 is the ending: the **Where copies live** board replaces the map's right half: one row per place that now holds a copy (icon, place name, the info chips that went there), then the ending line. Buttons: **Try other choices** (Story from chapter 1, choices cleared) and **See the trip map**.

### Mode 2: Trip map (explore)
All stops are buttons. Tap a stop: the stop card shows its name, a drawn icon and one sentence on what it does (Content). **Send a test** sends 8 pieces of "Hello Juno!" (one letter-group per piece) from your tablet to Juno's; they take the route the engine picks, odd pieces by router C and even pieces by router D (Content), so they land out of order and the slot strip sorts them. **Close a road** downs router A: the next test goes around through router B. Pieces can be tapped while moving to show their envelope (To, From, "Piece 3 of 8", a padlock over the words).

## Content
Map (engine design units 1000 x 600; kinds as in the Family engine):
| id | Name on screen | kind | x, y |
|---|---|---|---|
| you | Your tablet | tablet | 50, 300 |
| home | Your Wi-Fi router | wifi-router | 150, 300 |
| ispA | Your internet provider | isp | 270, 300 |
| rA | Router A | router | 390, 150 |
| rB | Router B | router | 390, 450 |
| srv | The message app's server | server | 500, 300 |
| rC | Router C | router | 610, 150 |
| rD | Router D | router | 610, 450 |
| ispB | Juno's internet provider | isp | 730, 300 |
| home2 | Juno's Wi-Fi router | wifi-router | 840, 300 |
| juno | Juno's tablet | tablet | 950, 300 |

Links (medium, ms per hop at Quick; Slow doubles): you-home wifi 400; home-ispA wire 400; ispA-rA fiber 400; ispA-rB fiber 700; rA-srv 400; rB-srv 700; srv-rC fiber 400; srv-rD fiber 900; rC-ispB 400; rD-ispB 900; ispB-home2 wire 400; home2-juno wifi 400. After the server, odd pieces are sent by rC and even pieces by rD (a fixed split, so the out-of-order landing is the same every time).

Stop cards (Trip map): you "Your tablet turns your words into data and cuts it into numbered pieces." home "Your Wi-Fi router sends the pieces from the air into a wire. Your family's Wi-Fi password keeps strangers off it." ispA "Your internet provider is the company that connects your home to the rest of the internet." rA, rB, rC, rD "A router reads the address on each piece and sends it one step closer to where it is going." srv "The message app keeps a copy on its server, so Juno can read it later." ispB "Juno's internet provider brings the pieces to Juno's home." home2 "Juno's Wi-Fi router sends the pieces through the air to her tablet." juno "Juno's tablet puts the pieces back in number order and shows the message."

The invite. Always: "Come to my party! Saturday at 2." Then three choices in chapter 1, each a pair of cards (the private card carries a red "private" tag with a lock-open icon, never color alone):
- Place: "at Maple Park" / "at my house, 14 Birch Lane" (private: home address)
- Extra: "Can't wait to see you!" / "Call me at 555-0142" (private: phone number; 555-01xx numbers are reserved for fiction)
- Photo: "a photo of my cake" / "a photo of me in my school shirt" (private: shows your school). Photos are drawn in code: a cake, or a child-free shirt-on-hanger icon with a school crest (no person drawn).
The invite is cut into 8 pieces by words (piece 8 is the photo). Note on the photo piece card: "A real photo would be hundreds of pieces."

Chapters (story text, choice A / choice B, result lines):
1. "Your tablet": "You are inviting your friend Juno to your party. Pick what goes in the message. Your tablet will cut it into 8 numbered pieces." Three card pairs (above), then **Send**. Result: "Your tablet cut the invite into 8 pieces. Each one has Juno's address on the outside."
2. "Two Wi-Fi networks": "Your tablet looks for Wi-Fi to send the pieces through the air. Two networks show up." A: "Home Wi-Fi (lock icon). Your family set its password." B: "Free_Fast_WiFi (no lock). Nobody knows whose it is." Result A: "Good pick. Home Wi-Fi locks the pieces in the air, and the app locks the words too. Two locks." Result B: "Your pieces made it. On an open network only the app's lock protected your words. A known network adds a second lock."
3. "Your internet provider": "While your pieces travel, a pop-up appears on your tablet: You won a free game! Type your name and address." A: "Close it and tell a grown-up." B: "Type my name and address." Result A: "Smart. Pop-ups that ask for personal info are often tricks. A grown-up can help you check." Result B: "Your name and address went to a website you don't know. That is a copy you can't take back."
4. "Routers": "Routers pass the pieces along like a relay team. Oh no, Router A just closed for repairs! What will the routers do with pieces 5 to 8?" (a prediction) A: "Wait for Router A to open again." B: "Find another road." Result A (said at the bounce): "Routers don't wait. Pieces 5 to 8 bounced off the closed router, then went another way, through Router B. They got there, just later." Result B: "Yes! Routers found another way, through Router B. The internet has many roads, so one closed road doesn't stop a message." (A plays a bounce animation, about 2 s longer.) Router A is closed from this moment for the rest of the run, so pieces 5 to 8 go by rB either way.
5. "The message app's server": "The app keeps a copy of your invite so Juno can read it later. Then it asks: who can see your profile?" A: "Only friends I know." B: "Everyone on the app." Result A: "Now only people you know can see your profile." Result B: "Now anyone on the app can see your name and photo."
6. "Juno's tablet": "The pieces arrive out of order: 1, 3, 5, 7, then 2, 4, 6, 8. The numbers let Juno's tablet put them back in order." Then a look-up beat (E3-SYS-NT-14): "Juno looks up the way to your party. Her tablet asks a map website, and the answer comes back in seconds. People use the internet to look things up and to talk to each other." Then: "Juno loves the invite. She asks: can I share it with my soccer group?" A: "Ask me first, please." B: "Sure, share it." Result A: "Juno will ask before she shares. Good friends ask first." Result B: "Juno shared it with 12 phones of kids you don't know."
7. "Where copies live" (ending). Rows always shown: Your tablet (the whole invite), The message app's server (the whole invite), Juno's tablet (the whole invite). Added rows: "Juno's soccer group, 12 phones" (if 6B), "A pop-up's website you don't know" (if 3B, chips: name, home address), "Your profile, seen by everyone on the app" (if 5B, chips: name, photo). Each row shows the info chips from the invite: "home address" (if Place B), "phone number" (if Extra B), "your school" (if Photo B). Count line: "Your invite is on N devices." N = 3, plus 12 if 6B. The pop-up row is a website, counted on its own line: "and one website you don't know".
   Ending line, first match wins: E1 (no private chip anywhere and 3A, 5A, 6A): "Your invite reached Juno, and your private details stayed private. Copies of a message can't be taken back, so you shared only what was safe." E2 (any private chip went to more than 3 devices, or 3B): "Your invite reached Juno, but private details went further than you planned. Copies can't be taken back. Next time, share private details only with people you know, and ask a grown-up first." E4 (no private chip, but 6B): "Your invite reached Juno, and then 12 phones of kids you don't know. No private details went along this time, but copies can't be taken back. Ask before a message is shared." E3 (otherwise): "Your invite reached Juno. Some private details went along, but only to Juno and the app's server. Before you share private details, ask a grown-up." The board also names who the trip touched (you, Juno, your family, and the soccer kids if 6B) and one good thing it did for them (E3-SYS-IM-15).

## Interactions in detail
- Pieces are envelope tokens with their number; they leave the tablet 250 ms apart and move hop by hop with the engine's mover. Each chapter moves the pieces only to the next stop (a stop holds them as a little stack with a count badge "8").
- Chapter 4: pieces 1 to 4 have already passed Router A before it closes (scripted); A plays a bounce for pieces 5 to 8 at Router A, then they go by rB. Chapter 6 shows the split after the server (odd by rC, even by rD) so they land 1, 3, 5, 7, 2, 4, 6, 8, each sliding into its numbered slot; the invite text then appears whole on Juno's tablet.
- Choices are final for the run (no back button inside Story, so consequences show); Start over clears them. Switching to Trip map and back returns to the chapter you left.
- Tap or Enter on a choice card picks it; both cards stay visible, the picked one outlined with a check, the other faded.
- Motion off: pieces jump stop to stop at the same timing, no bounce (a "bounced" tag shows for 1 s instead), no map pan (the stop ring moves).
- Nothing is saved. Names in the story are fictional; the invite's address and number are made up (555-01xx). No text entry anywhere.
- Sizes: the map scales its spacing per box at real pixel size; at 760 wide and below the map shows a window of 5 stops around the current one with left and right fade, and the panel goes under it with the choice cards first. At 375 wide the two choice cards stack. Choices and Next are visible without scrolling at every size in STANDARDS.md.
- Keyboard: Tab goes mode buttons, header, choice cards, Next, Start over, then the stops in Trip map. Visible focus ring.
- Expose `window.__tool = {state, net, setMode, choose(ch, pick), ending()}`; `ending()` returns the rows, chips, N and the ending id.

## Look
Accent `--brand #6a3d9a` (dusk violet), on a picture-book dusk map. Band 3-5, own `:root`.
- `--paper #f5f1fa`, `--panel #ffffff`, `--ink #241b33`, `--muted #5e5470`, `--line #e3dbef`, `--btn #6a3d9a`, `--head-ink #ffffff`, `--focus #c2410c`.
- Scene: sky gradient `#2b2550` to `#5b4a8a` with a few drawn stars; stops are rounded tiles `#fff8e1` with ink icons; envelope tokens `#fff8e1` with ink numbers; trail `#f2c14e` (gold); private tag `#b3261e` with white text and a lock-open icon; lock icons gold `#f2c14e`. Labels on the sky are `#e8e2f5`.
- Contrast (computed): white on brand 7.64:1; brand on paper 6.86:1; ink on paper 14.73:1; muted on paper 6.33:1; focus ring on paper 4.65:1; white on private red 6.54:1; ink on token cream 15.45:1; gold on night `#1f1b3a` 9.81:1; sky labels `#e8e2f5` on `#2b2550` 11.21:1. All pass AA.
- Neighbors: computer-builder blue `#2049b8`, score-keeper raspberry `#a82755`, code-tracer pencil orange `#a8461a`, loop-garden green. No other tool in this group uses violet.
- Calm, storybook; no confetti. The ending board is the one flourish (rows slide in one by one).

## Art
- ij-dusk-town: a cozy small town at dusk seen from a hill, rolling hills, glowing windows, wide sky with first stars, painted picture-book style; 16:9; cutout no; people no; behind the left half of the map (your side), dimmed 30 percent. FLUX.2 (`scripts/cfart.py`).
- ij-server-hall: a calm row of tall server cabinets with small blue and green lights in a clean data center, painted picture-book style, blank cabinet doors; 4:3; cutout no; people no; shown in the chapter 5 story card. FLUX.2.
Everything else (stops, icons, envelopes, photos in the invite, the ending board, preview.svg) is drawn in code.

## Voice
Bank voice `smooth-narrator` (Algieba), "Say smoothly and warmly, like an audiobook narrator". A story told aloud suits it; no built CS neighbor uses it (computer-builder bright-teacher, score-keeper friendly-dad, code-tracer clear-teacher, loop-garden hero-coach), and no other tool in this group does. Uses `Curio.voice` with `scope: () => state.mode`.

Story lines (event: spoken each time the chapter opens, so a second run is told again; stale when the chapter changes): the 7 chapter texts in Content, and each result line (event, stale when Next is pressed). Ending lines E1, E2, E3 (event).
Other lines:
- w-story (how, Story welcome): "Welcome to Internet Journey. Follow your message from your tablet to your friend's. At each stop, tap a card to choose."
- next (how, hint after a result): "Press Next to send the pieces on to the next stop."
- w-map (how, Trip map welcome): "This is the whole trip. Tap any stop to see what it does, or press Send a test."
- closed (how, first Close a road): "Router A is closed. Press Send a test and watch the pieces find another road."
- landed (event, Trip map test done; stale on the next Send): "All 8 pieces arrived, and the numbers put them back in order."
- again (how, after the ending): "Press Try other choices to see how a different trip ends."

## Family engine
`kit/network.js` (the network family: internet-journey, network-help-desk, packet-race, network-architect). This spec holds the full description; the siblings say what they feed it.
- **Graph** (pure): `net.graph({nodes, links})`. Node `{id, kind, label, x, y, up:true}` in design units 1000 x 600. Kinds: `laptop tablet phone desktop printer camera tv` (devices), `wifi-router access-point switch core-switch router firewall modem isp server cloud`. Link `{a, b, medium:'wire'|'wifi'|'fiber', ms, mbps, lenM, up:true}`.
- **Path** (pure): `net.path(g, from, to, {by:'ms'|'hops'})`: Dijkstra over nodes and links that are up; ties go to fewer hops, then the lower node index; returns ids or null. `net.reach(g, from)`: the set reachable. `net.flows(g, demands)`: given `[{from, to, mbps}]`, routes each by path and returns load per link (used by network-architect).
- **Packets** (pure): `net.split(text, n, {src, dst})` cuts by words into `{seq, of, src, dst, data}`; `net.join(list)` returns `{text, missing}` with "___" in gaps.
- **Forward** (pure): `net.step(g, table, pkt)`: next node from a table `table[node] = neighborId` (packet-race), decrements `ttl` (default 8) and returns `{at, dropped:'ttl'|'down'|null}`.
- **Mover** (DOM): `net.send(svg, g, pkt, hops, {speed, token})` glides a token along each link for its `ms`, resolves `'arrived'` or `'dropped'` (node or link went down under it). Tokens: `envelope` (this tool), `numbered` square (packet-race), `ping` dot (network-help-desk). Motion off: tokens jump hop to hop with the same timing.
- **Draw** (DOM): `net.draw(svg, g, skin)` maps design units to the box at real pixel size (icons and labels stay at fixed px, only spacing scales), draws one code-drawn icon per kind, wires solid 3 px, fiber 5 px with a light core line, Wi-Fi as a dashed line with three arcs at the radio end; a down node is grey with an X badge and a down link dashed with a break mark. `skin` sets colors, fonts, icon size and label placement. Every node is a focusable button (order given by the tool) and fires `onPick(node)`.
- Pure parts live in one marked block with no DOM, exposed as `__tool.net` for tests.
This tool uses: Graph, Draw, Mover (envelopes), Packets (8 pieces), and a scripted down router (rA). No Path or Forward: routes are scripted per chapter; Trip map uses `net.path` for the test so Close a road reroutes for real.

## Refine changes (round 1)
Cards show no private tags before Send; after Send a "What this message gives away" list names each private detail. A fourth ending, E4 (no private details, but 6B), and E3 now says "only to Juno and the app's server". Chapter 2 shows a second network, Free_Fast_WiFi, on its own stop (open badge there). Chapter 4 is framed as a prediction. Chapter 6 adds the look-up beat (a map website). The safe card alternates sides (place, photo, 3, 5 on the left; extra, 2, 4, 6 on the right). The board names who was touched and one benefit. The Your tablet stop card (Trip map) adds "People use the internet to look things up and to talk to each other." Story runs at Slow. Round 2: on a short stage the Free_Fast_WiFi hotspot sits above your Wi-Fi router (name on its right) so every label reads; 4A pieces go on by Router B right after each bounce, about 2 s after B.

## Open questions
- Packets first for grade 3: the story starts by cutting the invite into numbered pieces before any privacy choice. Is that too much at once for some grade 3 classes, or should Trip map (send a test) come first? Left as is.
- 5B (profile seen by everyone) counts as a stranger copy for E2. Left as is.

## Sources
- CSTA K-12 CS Standards 2026 ids E3-SYS-NT-14, E3-SYS-SE-13 (`data/standards/csta-2026-ids.txt`); CSTA 2017 1B-NI-04, 1B-NI-05: https://csteachers.org/k12standards/
- Messages are broken into packets, each with addressing information, routed separately and reassembled in order: Khan Academy, "The Internet: Packets, routing and reliability" (Computers and the Internet unit), https://www.khanacademy.org/computing/computers-and-internet
- Routers forward packets and pick other routes around failures; ISPs connect homes to the internet: Cloudflare Learning Center, "What is routing?" https://www.cloudflare.com/learning/network-layer/what-is-routing/
- Messaging services store messages on servers; content is encrypted in transit (HTTPS/TLS): Cloudflare Learning Center, "What is HTTPS?" https://www.cloudflare.com/learning/ssl/what-is-https/
- Open public Wi-Fi is less secure than a password-protected network: FTC Consumer Advice, "Are Public Wi-Fi Networks Safe? What You Need to Know", https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know
- Kids should keep personal information (address, phone, school) private and ask a parent before sharing; what's online is hard to take back: FTC Consumer Advice, "Kids and Socializing Online", https://consumer.ftc.gov/articles/kids-and-socializing-online ; Common Sense Education, Digital Citizenship curriculum, lesson "Private and Personal Information", https://www.commonsense.org/education/digital-citizenship
- 555-0100 to 555-0199 are reserved for fictional use: North American Numbering Plan Administrator, https://nationalnanpa.com
- Story, names and places are original to Curio Class.

## Done when
1. A full Story run with all "A" choices shows ending E1, 3 copy rows, "Your invite is on 3 devices", and no private chips.
2. A run with Place B, 3B and 6B shows E2, the soccer group row and the pop-up website row, the address chip on every invite row, and "Your invite is on 15 devices and one website you don't know".
3. Chapter 4 choice A plays the bounce at Router A and arrives about 2 s later than B; Router A stays closed for the rest of the run.
4. Chapter 6 pieces land 1, 3, 5, 7, 2, 4, 6, 8 and slot into numbered boxes; the invite reads whole and matches the chapter 1 choices.
5. Trip map: every stop card matches Content; Send a test lands 8 pieces; with Close a road on, the test goes through Router B (`__tool.net.path` agrees).
6. Voice: chapter and result lines play each time; the welcome plays once, Next's how-to line is spoken once then only shown; Read speaks the hint or chapter text.
7. Every size in STANDARDS.md: choice cards and Next visible without scrolling; map labels at least 12 px in the 680x425 preview; 375 wide works in `drive.py --host`.
8. Motion off, keyboard only run to the ending, console clean, no network requests, nothing stored, the name appears only as "Curio Class".
