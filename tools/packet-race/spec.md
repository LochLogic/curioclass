# Packet Race

## One idea
You are the routing table: aim each router's arrow at the neighbor it should pass packets to, so twelve numbered packets reach the far end and rebuild a sentence, and when routers fail mid-race you re-aim fast while lost packets get sent again, racing a ghost of your best run.

## Not like
- internet-journey (grade 3, same family): one message's trip told as a story with fixed routes. Here you set every route yourself and the clock runs.
- network-help-desk (grade 4, same family): diagnoses one device at home. Here there is no home, only routers between a sender and a receiver.
- network-architect (9-12, same family): designs and buys the network. Here the map is given; you control where traffic goes, live.
- phishing-spotter (6-8, same wave group): fast rounds of judgment calls on messages. Here speed is about steering on a map, not reading.
- flowchart-factory, code-kitchen (6-8): programs and procedures; here the "program" is a table of arrows.

## Who and how
- Grades 6 to 8, computer science. Module: Packets and the Internet (Systems and Security), "How data travels and how the internet stays resilient".
- Driver: students (one per laptop, or pairs: one aims, one watches the receiver). Teacher can run Watch on a projector first.
- 15 to 25 minutes: Watch (5 min), three maps raced twice each (15 min).
- Standards (CSTA 2026, as listed): MS-SYS-NT-34, MS-SYS-NT-35. 2017 crosswalk: 2-NI-04 (model the role of protocols in transmitting data across networks and the internet).
- tool.json: driver "students", minutes "15-25", modes ["Watch", "Race"], grades_label "Grades 6-8". Kit starter plus `kit:network`.

## Screens and modes
Header (kit): "Packet Race", small line "Steer the packets". Mode buttons: **Watch** (opens first), **Race**. Then Motion, Sound, Read.

Stage: a transit-map style network. Sender **S** on the left (a laptop icon), receiver **D** on the right (a laptop icon), routers as white station circles with an ink ring and their label (R1 to R10). Each router has an arrow (a blue pointer on its ring) aimed down one of its links. Links are thick grey lines with a white casing, with their delay printed small at the middle ("0.4 s"). Under D, the **slot strip**: 12 numbered boxes; each arriving packet's word drops into its box. Above the stage, the clock bar (Race) with the ghost marker.

Watch panel: `#hint`, map picker (**Town**, **City**, **Coast**), the **Path now** readout ("S R1 R3 R5 R6 D, 1.8 s"), **Reset map**. Tap a router to take it down or bring it back; tap a link to cut or repair it.

Race panel: `#hint`, map picker (same three), **Start** (big, `.gold`), **Restart**, the readouts (Time, Delivered "7 of 12", Dropped, Resent), the **Best** line for this map, **Clear bests**.

### Mode 1: Watch (explore)
The routers aim their own arrows: each arrow points along the first hop of the fastest path (by delay) from that router to D. S sends a packet every 0.4 s without end, looping the sentence; the slot strip refills each time the sentence completes. Taking a router down drops any packet in it or arriving at it (a small puff and "x" mark), then 1.0 s later every arrow recomputes with a ripple out from the broken spot ("routers tell their neighbors"), and Path now updates. If D can't be reached: arrows point at nothing, packets wait at S (up to 6, then dropped), Path now says "No road to D". Restoring brings the route back the same way.

### Mode 2: Race
- Before Start, arrows are unset (a grey dot, no pointer) and the routers can be aimed. Tap a router: its arrow turns to the next link clockwise; Shift+tap or right-click turns it back; keyboard Left and Right do the same on the focused router. On City the sender has two links, so S has an arrow too.
- Start: the clock runs; S sends packets 1 to 12, one every 0.4 s (last at 4.4 s). Each packet follows the arrows hop by hop at each link's delay.
- A packet at a router with no arrow waits there (blinking); a router holds at most 6 waiting packets; the 7th is dropped ("full"). A packet whose arrow leads into a down router or a cut link is dropped ("down"). Each hop takes one from the packet's hop count (TTL 8); at 0 it is dropped ("TTL: is there a loop?").
- Scheduled failures (Content) fire at their times: the router greys with an X, or the link shows a break, with a red flash on the clock bar.
- Resend: S sends any packet again if it has not reached D within 3.0 s of its last send. (In this model D's "got it" notes reach S instantly.)
- The clock stops when all 12 boxes are filled. The **Result** card: Time, Dropped (by reason), Resent, Average hops, Par for the map, and Best. A new best saves to this device and becomes the ghost.
- Ghost: while racing, faint outline numbers fill the slot strip at the moments the best run's packets arrived, and a ghost marker moves along the clock bar to the best time.

## Content
Sentences (12 words, one per packet):
- Town: "Big messages travel as small packets that each find their own way."
- City: "Each packet carries a number, so the message gets rebuilt in order."
- Coast: "When one road breaks, routers find another, so the internet keeps working."

Maps (design units 1000 x 600; link delays in seconds):
- **Town**: S (60,300), R1 (220,300), R2 (400,150), R3 (400,450), R4 (600,150), R5 (600,450), R6 (800,300), D (940,300). Links: S-R1 0.3, R1-R2 0.4, R1-R3 0.4, R2-R3 0.5, R2-R4 0.4, R3-R5 0.4, R4-R5 0.5, R4-R6 0.4, R5-R6 0.4, R6-D 0.3. Failures: R4 down at 3.0 s. Fastest path before: S R1 R2 R4 R6 D (1.8 s, tied with S R1 R3 R5 R6 D); after: S R1 R3 R5 R6 D (1.8 s). Par 6.2 s.
- **City**: S (60,300), R1 (200,180), R2 (200,420), R3 (380,90), R4 (380,300), R5 (380,510), R6 (600,180), R7 (600,420), R8 (800,300), D (940,300). Links: S-R1 0.3, S-R2 0.3, R1-R3 0.4, R1-R4 0.3, R2-R4 0.3, R2-R5 0.4, R3-R4 0.3, R4-R5 0.3, R3-R6 0.4, R4-R6 0.4, R4-R7 0.4, R5-R7 0.4, R6-R8 0.4, R7-R8 0.4, R6-D 0.7, R8-D 0.3. Failures: R4 down at 2.5 s, R6 down at 5.0 s. Fastest before: S R1 R4 R6 D (1.7 s); after R4: S R1 R3 R6 D (1.8 s); after R6 too: S R2 R5 R7 R8 D (1.8 s). Par 6.2 s.
- **Coast**: S (50,300), R1 (160,300), R2 (290,150), R3 (290,450), R4 (440,60), R5 (440,300), R6 (440,540), R7 (610,150), R8 (610,450), R9 (780,300), R10 (800,90), D (950,300). Links: S-R1 0.3, R1-R2 0.4, R1-R3 0.4, R2-R4 0.4, R2-R5 0.3, R3-R5 0.3, R3-R6 0.4, R4-R7 0.5, R5-R7 0.4, R5-R8 0.4, R6-R8 0.5, R7-R9 0.4, R8-R9 0.4, R7-R10 0.3, R10-D 0.4, R9-D 0.3. Failures: R5 down at 2.0 s, link R7-R10 cut at 4.5 s, R5 back up at 8.0 s. Fastest before: S R1 R2 R5 R7 R10 D (2.1 s); with R5 down and R7-R10 cut: S R1 R2 R4 R7 R9 D (2.3 s, tied with S R1 R3 R6 R8 R9 D). Par 6.7 s.
Par = last send (4.4 s) + the fastest path that no failure ever touches (all computed with Dijkstra in Python).

Arrow direction order for "clockwise": by the link's angle from the router, measured from straight up, clockwise.

## Interactions in detail
- Tapping a router during a race never pauses it. Re-aiming affects packets that arrive after the tap; a packet already on a link keeps going.
- A loop (two routers pointing at each other) sends packets back and forth until TTL ends them; the hint says so the first time ("ttl" line).
- Down routers can't be aimed (tap shakes it). In Watch, tapping S or D does nothing.
- Restart re-runs the same map with arrows kept as they were set (to plan from a known start), clock reset; a second Restart within 2 s clears arrows too ("Arrows cleared" toast).
- Switching maps or modes stops the run. Watch and Race keep their own map choice for the page load.
- Bests: localStorage `curio-packet-race` = {map: {time, arrivals[12]}}, try/catch wrapped; Clear bests empties it (confirm step: "Clear all three bests?" Yes/No).
- Motion off: packets jump link to link at the same timing; puffs and ripples become a 400 ms outline flash.
- Sizes: the map draws at real pixel size (station circles 44 px minimum so they stay tap targets); at 760 wide the panel goes below with Start and the readouts first; at 375 wide the map scrolls sideways inside its box (the slot strip stays pinned under it) and routers stay 44 px. Start, Restart and the slot strip visible without page scrolling at every size in STANDARDS.md.
- Keyboard: Tab order is modes, header, map picker, Start, Restart, then routers left to right; Left/Right turn the focused router's arrow; Enter in Watch toggles it.
- `window.__tool = {state, net, setMode, setMap(id), aim(router, neighbor), start(), runTo(seconds)}`; `runTo` steps the model with no animation for tests.

## Look
Accent `--brand #b42318` (signal red, for Start, failures and the header rule). Band 6-8, own `:root`. A printed transit map.
- `--paper #f6f3ea`, `--panel #ffffff`, `--ink #1d1d1f`, `--muted #5b5850`, `--line #e1dccd`, `--btn #1d1d1f`, `--head-ink #ffffff`, `--focus #1d4ed8`.
- Scene: links `#8a8578` 8 px with a white 2 px casing; stations white with a 3 px ink ring; arrows `#1d4ed8`; packets ink squares with white numbers; down routers `#6b6b6b` with a white X; cut link dashed with a red break mark `#b42318`; ghost outlines `#5b5850` dashed. Delay labels 12 px muted.
- Contrast (computed): white on brand 6.57:1; brand on paper 5.93:1; ink on paper 15.17:1; muted on paper 6.40:1; focus/arrow blue on paper 6.04:1; white on ink packets 16.83:1; white on arrow blue 6.70:1; down grey on paper 4.80:1. All pass AA.
- Neighbors: phishing-spotter dark arcade lime, network-architect blueprint blue, internet-journey violet. No celebration: a new best shows "New best" in the Result card, nothing more.

## Art
none: drawn in code. The map, stations, arrows, packets, slot strip, laptops and preview.svg are SVG.

## Voice
Bank voice `firm-captain` (Alnilam), "Say firmly but kindly, like a ship captain giving clear directions", here a network dispatcher. Not used by any group sibling or CS neighbor (marching-band, a music tool, is its other user). Slot words, readouts and router names are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-watch (how, Watch welcome): "Packets are flowing from S to D. Tap a router to take it down, and watch the network find another road."
- rerouted (event, first reroute after each change; stale on the next change): "The routers found a new path."
- noroad (event; stale when a road returns): "There's no road to D. Bring a router back up."
- w-race (how, Race welcome): "You are the routing table now. Tap each router to aim its arrow, then press Start."
- unset (how, first packet waiting at an unaimed router): "A packet is waiting. Tap that router to aim it."
- down (event, each scheduled failure; stale after 3 seconds): "A router just went down. Re-aim the arrows around it."
- cut (event, link cut; stale after 3 seconds): "A link was cut. Find another way."
- ttl (how, first TTL drop): "That packet ran out of hops. Two arrows may be pointing at each other."
- resend (how, first resend): "Lost packets are sent again. Keep the road open."
- done (event, all 12 delivered): "Message complete. Check your time."
- best (event, new best): "New best. That run is your ghost now."

## Family engine
`kit/network.js`, described in full in tools/internet-journey/spec.md. This tool uses: **Graph** (the three maps), **Path** (Watch arrows: first hop of `net.path(g, router, 'D', {by:'ms'})`; Par), **Forward** (`net.step` with the player's arrow table, TTL 8, drops for down nodes and links), **Packets** (`net.split` of the sentence into 12, `net.join` for the slot strip), **Mover** with `numbered` tokens, and **Draw** with a transit-map skin (station circles, casing lines, delay labels). Router queues (6) and the 3.0 s resend timer are this tool's own.

## Sources
- CSTA 2026 ids MS-SYS-NT-34, MS-SYS-NT-35 (`data/standards/csta-2026-ids.txt`); CSTA 2017 2-NI-04: https://csteachers.org/k12standards/
- Routers forward packets by a routing table of next hops, and routing protocols update routes after failures: Cloudflare Learning Center, "What is routing?" https://www.cloudflare.com/learning/network-layer/what-is-routing/
- Packets carry a time to live (hop limit) so looping packets are discarded: Cloudflare Learning Center, "What is time-to-live (TTL)?" https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/ ; RFC 791 (Internet Protocol), https://www.rfc-editor.org/rfc/rfc791
- Sequence numbers and resending lost data after a timeout: RFC 9293 (Transmission Control Protocol), https://www.rfc-editor.org/rfc/rfc9293 ; Khan Academy, "Transmission Control Protocol", https://www.khanacademy.org/computing/computers-and-internet
- Networks with many redundant paths keep working when parts fail: Paul Baran, "On Distributed Communications" (RAND, 1964), https://www.rand.org/pubs/research_memoranda/RM3420.html
- Maps, delays, failure times and sentences are original to Curio Class; paths and par times computed with Dijkstra in Python.

## Done when
1. `net.path` on each map gives the fastest paths and delays listed in Content, before and after each failure; par times are 6.2, 6.2 and 6.7 s.
2. Watch: taking R4 down on Town drops packets at R4, then within about 1 s every arrow recomputes and Path now reads a 1.8 s path; restoring it returns the original.
3. Race on Town with arrows set along S R1 R3 R5 R6 D before Start finishes at 6.2 s with 0 drops (`runTo`).
4. Race on Town with arrows along R4: packets drop at 3.0 s, are resent 3.0 s after their send, and the run still completes once re-aimed.
5. Two routers aimed at each other drop packets with reason TTL after 8 hops; the ttl line plays once.
6. Unaimed router holds up to 6 packets, drops the 7th as "full".
7. Bests save per map and the ghost fills the slot strip at the saved arrival times; Clear bests (after Yes) empties them.
8. Every size in STANDARDS.md: Start, the slot strip and routers usable without page scrolling; 375 wide pans the map; routers stay 44 px.
9. Voice: welcome once per mode, how lines once, failure lines each time while fresh; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".

## Open questions
- The format is a race, but the explore-first rule puts Watch first (packets flowing, tap a router to break it) with Race one tap away. Open on Watch as written, or straight on Race?
