# internet-journey: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; bundle with `CURIO_DRAFT=1` (194 KB).
Driven with `scripts/drive.py` (ports 9441-9443, own profile). Every ending recomputed for all 256 choice combinations
(`__tool.ending(c)` against the spec's rules, in Python). Standard wording read from the official PDF, "2026 CSTA PK-12
Computer Science Standards" (statements and boundary statements, pp. 83-89 and Appendix A p. 180), since the repo holds
only the ids.

Counts: blocker 1, should fix 4, polish 3, nit 3.

## Standards (rule 2)

| Code | Statement (CSTA 2026) | Taught by | Verdict |
|---|---|---|---|
| E3-SYS-SE-13 | Evaluate how sharing information online might reveal personally identifiable information and other details. Boundary names "providing their address in response to a pop-up ... saying they won a prize" and seemingly harmless details that reveal PII. | Chapter 1 cards (address, phone, school shirt photo), chapter 3 pop-up (the boundary's own example), chapter 5 profile, chapter 6 sharing, the Where copies live board, a second run to compare. | Taught well, but see should fix 4: the "private" tags do the evaluating for the student. |
| E3-SYS-NT-14 | Explain how people access the internet to gain information and communicate with each other. Boundary: devices that connect, using a search engine to look up facts, video chat; "not expected to describe ... routing protocols ... or data packet transmission." | The communicate half: tablet, Wi-Fi router, internet provider (chapters 1 to 3, stop cards). | Half taught. Should fix 2. |
| E3-SYS-IM-15 | Describe how widely used computing systems may impact an individual's life and community. Boundary: benefits and harms (safety, privacy...), identify which individuals or communities are impacted and how. | The board shows harms to "you" (copies on a server, profile seen by everyone, 12 strangers' phones). | Partly taught. Should fix 3. |

## Done when

| # | Check | How | Result |
|---|---|---|---|
| 1 | All A: E1, 3 rows, "Your invite is on 3 devices", no chips | frame 02-allA-end, board text | PASS |
| 2 | Place B, 3B, 6B: E2, soccer and pop-up rows, address chip on every invite row, "15 devices and one website you don't know" | frame 03-E2-spec; N = 3 + 12 = 15 | PASS |
| 3 | Chapter 4 A bounces, about 2 s later than B; Router A closed for the rest | real time: A 6.97 s, B 4.20 s, so 2.77 s later; rA X badge at the ending (03) | PASS on behavior; timing is nit 2 |
| 4 | Chapter 6 lands 1, 3, 5, 7, 2, 4, 6, 8 into slots; invite reads whole and matches chapter 1 | `state.landOrder` [1,3,5,7,2,4,6,8] in every run; "Juno sees" matched the picks (02, 05, 09). Recomputed at Slow: odd arrive 3.2, 3.7, 4.2, 4.7 s, even 5.45, 5.95, 6.45, 6.95 s | PASS |
| 5 | Trip map stop cards match Content; test lands 8; Close a road goes through Router B and `net.path` agrees | 11-map-cards (all 11 word for word); 12: landed 1,3,5,2,7,4,6,8 (recomputed at Quick: 3.20, 3.70, 4.20, 4.45, 4.70, 4.95, 5.45, 5.95 s); 13: route via rB, `net.path` = you,home,ispA,rB,srv,rC,ispB,home2,juno | PASS |
| 6 | Voice: chapter and result lines each time, welcome once, Next how-to once then shown, Read speaks chapter text | held-click runs v4a, v4b: welcome spoken once; ch1 to ch3 and results spoken; `next` spoken once then silent; after Start over ch1, ch2 and result spoken again; Read read the ch3 text | PASS (full counts are the Craft lens's) |
| 7 | Sizes; map labels at least 12 px at 680x425 | v2-680: SVG text 12.5 to 14 px | PASS for labels; other sizes are the Play lens's |
| 8 | Motion off, keyboard, console, network, storage, name | console clean in all 20 frames; no fetch, XHR or storage in src.html or kit/network.js; "Curio Class" only | PASS for what I checked; keyboard and Motion off runs left to Craft and Play |

## Findings

### Blocker

**B1. Ending E3 says something false for "all safe, but Sure, share it".** `src.html:451-453` (`ending()`), mode Story,
chapter 7. With no private card in chapter 1, 3A, 5A and 6B, the board shows "Juno's soccer group, 12 phones" and "Your
invite is on 15 devices", no private chips at all, yet the story text and the spoken ending say "Some private details
went along, but only to people you know." Both halves are wrong: no private details went, and the invite did reach
12 kids the student doesn't know. Seen in frame 04-E3-6Bonly; the 256-run sweep finds it in 4 runs (ch2 and ch4 either
way). The code follows the spec's first-match rules literally (the builder flagged it in handoff.md). A grade 3
student who picked every safe card and then said "Sure, share it" is a likely run, and the line contradicts the board
in front of them. Better: a fourth ending for this case, for example "Your invite reached Juno, and then 12 phones of
kids you don't know. No private details went along this time, but copies can't be taken back. Ask before a message is
shared." (add to voice/lines.json and `allLines()`). **general**

### Should fix

**S1. Choosing Free_Fast_WiFi turns your own home router "open".** Chapter 2, `src.html:597` (badge on `home`), frame
07-ch2-B. The pieces already sit at "Your Wi-Fi router" (chapter 1 moved them there) before the student picks a network;
picking B puts a red "open" badge on the stop still labeled "Your Wi-Fi router", whose Trip map card says "Your
family's Wi-Fi password keeps strangers off it." The picture teaches that your family's router became the stranger's
network. Better: in chapter 2 keep the pieces on the tablet until the pick (chapter 1 moves them only to the edge of the
tablet), and on 2B relabel that stop "Free_Fast_WiFi" for the rest of the run (or draw it as a separate hotspot), so the
map matches the choice. **general**

**S2. E3-SYS-NT-14 is only half taught.** The code is "how people access the internet to gain information and
communicate with each other". The tool teaches the communicate half through the access chain (device, Wi-Fi, internet
provider). Nothing the student does is getting information: no looking something up, no page coming back from a server.
Also, the boundary says grade 3 is "not expected to describe ... routing protocols ... or data packet transmission", and
CSTA's research summary (Appendix A, p. 180) puts the network-of-networks picture in middle school
(MS-SYS-NT-34, MS-SYS-NT-35, module computer-science-6-8-packets-and-the-internet). The packets and rerouting are the
2017 1B-NI-04 crosswalk, fine as the story's vehicle, but they don't carry NT-14. A real activity that teaches the
missing half: in Trip map, a **Look something up** test (you ask the app's server, or a library website, a question and
the answer's pieces come back to your tablet), plus one line on the tablet stop card naming both uses ("People use the
internet to look things up and to talk to each other"). Otherwise move NT-14 to a tool where looking things up is the
task. The packet-centric focus versus CSTA 2026's grade placement goes to the spec's open questions. **general**

**S3. E3-SYS-IM-15 is only partly taught.** The code asks students to describe how a widely used system impacts an
individual's life and community: benefits and harms, and which people or communities are affected. The board shows harms
to "you" only. No moment names a benefit (the app let you invite Juno from home, she can read it later), and nothing asks
who else is touched (Juno, the 12 soccer kids who now hold your address, your family whose home address is out). The
notes' "Talk about it" has no impact question either. A real activity: a closing "Who did this app touch?" step on the
board where the student taps people (you, Juno, your family, the soccer group) and sees one benefit or harm for each,
drawn from the run's choices, plus a matching discussion question in notes.md. If that can't be done well here, move
IM-15 to a grade 3 tool built around benefits and harms. **general**

**S4. The "private" tags do SE-13's evaluating for the student.** Chapter 1 cards, `src.html:357-359` and `ptag()`, frame
01-default. Every risky card carries a red "private" tag before the student chooses, including "a photo of me in my
school shirt" tagged "your school", which is exactly the "seemingly harmless detail" the boundary statement wants
students to notice themselves. The standard's verb is evaluate; here the label decides. Not a scored quiz, but the
same rule applies (POLISH, nothing gives an answer away). Better: no tags on the cards; after Send, the invite card
marks what the message reveals ("This tells people where you live", "This shows your school") so the student checks
their own pick, and the board keeps its chips. The spec asks for the tags, so this goes to the spec's open questions
with the recommendation. **general**

### Polish

**P1. Chapter 4 makes the student pick the route, then says routers did.** Card A "Take the closed road anyway" versus
result B "Routers found another way". The lesson ("routers find another road") is undercut by a choice that puts the
sender in charge of routing, and real routers don't send pieces into a router they know is down. Better: make it a
prediction ("Router A is closed. What will the routers do?" Stop the message / Find another road), then show the reroute
either way. Spec change, so open questions. **family:network**

**P2. The safe card is always on the left.** All 8 pairs put the safe pick as card A. On the second run ("pick the
opposite cards", notes.md) a student just taps the other side. Better: alternate sides per chapter (fixed, not random,
so the teacher's notes stay right). **general**

**P3. E3 says "only to people you know" while the board shows the chip on the app's server.** Frame 05-E3-placeB:
"home address" chip on "The message app's server" row, yet the line says the details went "only to people you know".
Better: "...went along, but only to Juno and the app's server." **general**

### Nit

**N1. Envelope "To: Juno's tablet".** Trip map envelope card (`src.html:1042`) and chapter 1 result. In the spec's own
model the app's server keeps the copy, so pieces are really addressed to the server first. Fine as a grade 3
simplification; if touched, "To: Juno (through the app)". **family:network**

**N2. Chapter 4 A is 2.77 s later than B, spec says about 2 s.** Measured in real time (6.97 s vs 4.20 s). Trim the bounce
or change the spec to "about 3 s". **family:network**

**N3. "Juno sees" ends without a period with the phone card.** Frame 09: "...14 Birch Lane. Call me at 555-0142". The
invite text has no end punctuation when Extra is B. Add a period. **general**

## Other checks

- Facts: every on-screen number recomputed (8 pieces; 3 or 15 devices; land orders in both modes; 555-0142 sits in
  NANPA's 555-0100 to 555-0199 fiction range). Wi-Fi and HTTPS lock lines, pop-up, and "ask a grown-up" lines match the
  spec's Sources (Cloudflare, FTC, Common Sense). Notes match the tool.
- Endings across all 256 runs: E2 220, E3 32, E1 4; every one matches the spec's rules as the builder read them
  (5B counts as private details going to everyone).
- Language: plain and right for grade 3; the grown-up word "packets" is kept to the notes.
- Guardrails: grade 3, no points, timers or win states; no health or hard-history content.
- Sensitivity (rule 5): nothing cultural, Native or hard-history. No flag.

Frames: out/01-default, 02-allA-end, 03-E2-spec, 04-E3-6Bonly, 05-E3-placeB, 06-allB-end, 07-ch2-B, 08-ch3-B,
09-ch6-allB-photo, 11-map-cards, 12-map-test, 13-map-closed, 14-ch4-A/B-timing, 15-ch5; out2/v2-680; out3/v4a, v4b.
