# Network Help Desk

## One idea
You answer the help desk phone, and the parts of each caller's home network only appear on your map when you ask the question that reveals them, so you learn to sort every "it won't connect" into one of three kinds (the connection, logging in to prove who you are, or permission to do a thing) before you send a fix and watch the test ping go through.

## Not like
- internet-journey (grade 3, same family): rides along with a working message. Here something is broken and you find it by asking.
- packet-race (6-8, same family): routes packets against a clock. Here there is no clock and only one device's path matters.
- network-architect (9-12, same family): designs a whole network. Here the home network is given; you only diagnose it.
- data-defenders (grade 5): security puzzles about stored school data. Here logging in and permission show up as reasons a device is stuck, not as attacks.
- code-tracer (grade 4, built): predicts code line by line. No code here.
- The other three 3-5 mysteries: this one's clues come from a question board, and the "claim" is a cause card backed by the clues that prove it.

## Who and how
- Grade 4, computer science. Module: Wired, Wireless and Login (Systems and Security), "Network connections; authentication vs authorization".
- Topic line: "wired and wireless networks, logging in".
- Driver: students or teacher. Pairs on laptops (one is the caller reading the clue cards aloud), or teacher-led on a projector with the class choosing which question to ask.
- 20 to 30 minutes: four calls (12 min), the other four (12 min), House any time.
- Standards (CSTA 2026, as listed): E4-SYS-NT-14, E4-SYS-SE-13, E4-SYS-HW-12. 2017 crosswalk: 1B-CS-03 (troubleshoot simple hardware and software problems), 1B-NI-05 (how personal information is protected, passwords).
- tool.json: driver "students or teacher", minutes "20-30", modes ["Calls", "House"], grades_label "Grade 4". Kit starter plus `kit:network`.

## Screens and modes
Header (kit): "Network Help Desk", small line "Ask, then fix". Mode buttons: **Calls** (opens first), **House**. Then Motion, Sound, Read.

Stage (both modes): a top-down house plan drawn by the network engine: Living room (router and TV), Office, Kitchen, Bedroom, and the Backyard shed across a lawn. Walls drawn as thick lines, room names in 14 px or more.

Calls panel, top to bottom: the **call card** (caller name, device icon, room, their first words in a speech bubble); **Questions**: six buttons with icons (Content), each greyed with a check once asked; **Clues**: the answers so far as small cards; **Make a claim** (big button); the call strip (8 phone icons, done ones ticked, tap any to open that call); **Call time** readout ("Call time: 3 min").
Claim step (replaces Questions): first **What kind of problem?**, three big kind buttons (Connection, Logging in, Permission, each with its icon); then that kind's **cause cards** (Connection 4, Logging in 2, Permission 1; a "Change kind" button goes back to the three); then "Tap 1 or 2 clues that prove it", then **Send fix**, and **Back to questions**. (Changed 2026-10-28, Cory, after Refine round 1: the student makes the kind sort, it is not printed for them.)

House panel: the selected device's controls (Content), a **Try** row (Internet, Library site, Family printer, Parent settings) and the result chip, plus **Reset house**.

### Mode 1: Calls (the mysteries)
- A call opens: the map shows only the house, the router (lights unknown, drawn as a grey "?" badge) and the caller's device with a "?" link. Other devices are faint outlines.
- Asking a question adds a clue card and lights the matching part of the map: Q1 draws the device's link (cable, Wi-Fi, or the Guest Wi-Fi in orange dashes); Q2 shows the router lights (on and blinking, or dark); Q3 colors the other devices (check badge = online, X badge = offline); Q4 shows the device's screen as a bubble; Q5 shows a login card (none, failed, or "Hi, Leo"); Q6 puts an account badge on the device (Grown-up, Kid, Student, Guest). Each question adds 1 minute to Call time.
- Make a claim: pick a kind, then a cause card, tap 1 or 2 clue cards, Send fix. The clue is judged before the cause.
  - Right cause and at least one key clue: the fix plays (cable plugs in, airplane turns off, the device walks closer, the router powers up, a password retypes with Caps Lock off, a "Student page" opens, a file goes to a family laptop), then a ping dot runs device to router to the internet cloud and back, the device badge turns to "Online" (or "Allowed" or "Signed in"), and the **Solved** card shows the kind stamped (Connection, Logging in or Permission), the questions asked, and the fix sentence. Call strip ticks.
  - No key clue picked (whatever the cause): the same reply for every cause, "That clue doesn't prove a cause yet. Pick a clue that shows what is broken." No Call time added. Send fix stays. The reply never says whether the cause is right.
  - Key clue picked, wrong kind: a kind nudge, "Look at your clues again: is the path broken, did logging in fail, or did logging in work?" Call time +2 minutes.
  - Wrong cause: the caller says "I tried that. It still doesn't work." The ping runs and stops at the broken spot with an X. A nudge names the key question if not yet asked ("Try asking: What does the screen say?"), or quotes the key clue if it was ("Look at this clue again: ..."). Call time +2 minutes.
- After all 8 calls: a **Shift report**: each call's caller, kind and questions asked. Buttons: **Start a new shift** (clears ticks), **Open House**.

### Mode 2: House (explore)
All devices shown: Desktop (Office, cable), Laptop (Living room), Tablet (Bedroom, draggable anywhere on the plan), Phone (Kitchen), Printer (Office, cable), TV (Living room). Tap the router to flip its power. Tap the desktop's cable end to unplug or plug it. Tap a device to select it; the panel shows: **Wi-Fi** On/Off, **Network** Home/Guest, **Account** Parent/Kid/Guest, **Caps Lock** On/Off (laptop and desktop), and the Try row. Dragging the tablet changes its Wi-Fi bars live (0 to 3, Content). Try results, first failing rule wins:
1. Router off: "No connection" (all devices). 2. Wired device unplugged, or wireless with Wi-Fi off or 0 bars: "No connection". 3. Library site with Caps Lock on: "Wrong password" (Logging in). 4. Family printer from the Guest network: "Not allowed: guests can't reach home devices" (Permission). 5. Parent settings with a Kid or Guest account: "Not allowed: Parent account only" (Permission). 6. Otherwise: "Online", "Signed in", "Printed" or "Allowed", with a ping dot run on the map.

## Content
House plan (design units 1000 x 600): router (300, 330) in the Living room; Office desktop (120, 150) and printer (180, 120), both wired; Living room laptop (360, 420); Kitchen spot (520, 200); Bedroom spot (650, 420); Back door spot (760, 470); Shed spot (920, 520). Wi-Fi bars by straight distance d from the router (a model, labeled "about" on screen: walls and distance weaken Wi-Fi): d up to 250 = 3 bars; 251 to 420 = 2; 421 to 560 = 1; over 560 = 0. Computed: Living room 108 (3), Kitchen 255 (2), Bedroom 361 (2), Back door 481 (1), Shed 648 (0).

Questions (same six every call): Q1 "Is it on a cable or on Wi-Fi?" Q2 "What do the lights on the router show?" Q3 "Do other devices in the house work?" Q4 "What does the screen say?" Q5 "Did it ask you to log in? Did that work?" Q6 "Whose account is it?"

Causes (group): Cable unplugged; Wi-Fi turned off; Too far from the router; Router has no power (Connection). Wrong Wi-Fi password; Wrong account password (Logging in). Not allowed (Permission).

Calls (answers Q1 to Q6; key clues; cause; fix sentence on the Solved card):
| # | Caller, device, room, first words | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Key | Cause | Fix |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Grandpa Lou, desktop, Office: "My computer says no internet!" | "A cable. The blue one." | "Lights on and blinking." | "My tablet works fine." | "A little computer picture with a red X in the corner." | "It never got that far." | "Mine. A grown-up account." | Q4, Q1 (both together) | Cable unplugged | Plug the cable back in at both ends. |
| 2 | Mia, tablet, Bedroom: "My games won't load." | "Wi-Fi, I think." | "All the lights are on." | "Mom's phone works." | "There's a little airplane at the top." | "Not yet." | "My kid account." | Q4 (Q3 only alongside it) | Wi-Fi turned off | Turn airplane mode off so Wi-Fi comes back on. |
| 3 | Mr. Patel, laptop, Kitchen: "It keeps asking me something." | "Wi-Fi." | "Lights on." | "The kids' tablets work." | "It shows our Wi-Fi name and asks for the password again." | "It keeps asking for the Wi-Fi password." | "Mine. A grown-up account." | Q4, Q5 | Wrong Wi-Fi password | Type the Wi-Fi password from the sticker on the router. |
| 4 | Sam, phone, Shed: "Nothing loads out here." | "Wi-Fi." | "Lights on." | "It works fine in the house." | "The Wi-Fi sign has no bars." | "No." | "My kid account." | Q4, Q3 | Too far from the router | Move closer to the router, or add a Wi-Fi extender by the back door. |
| 5 | Aunt Rosa, laptop, Living room: "The whole house is offline!" | "Wi-Fi." | "No lights at all. It's dark." | "Nothing works. Not even the TV." | "No networks found." | "No." | "Mine. A grown-up account." | Q2, Q3 | Router has no power | Plug the router's power back in and wait for the lights. |
| 6 | Grandma June, laptop, Living room: "The library website hates me." | "Wi-Fi." | "Lights on." | "Everything else works." | "It says the password is wrong. And the Caps Lock light is on." | "It asks for my library password, then says it's wrong." | "Mine. My library account." | Q4, Q5 | Wrong account password | Turn off Caps Lock, then type the password again. |
| 7 | Leo, school laptop, Bedroom: "My homework site is broken." | "Wi-Fi." | "Lights on." | "Yes." | "A page with a lock on it that says Teachers only." | "Yes, I logged in fine. It says Hi, Leo." | "My student account." | Q4, Q6 | Not allowed | Nothing is broken. That page is for teachers; open the Student page. |
| 8 | Ana (visiting), laptop, Kitchen: "I can't print my ticket." | "Wi-Fi. The Guest Wi-Fi." | "Lights on." | "The family's laptops can print." | "Printer not found." | "The guest Wi-Fi had its own password, and it worked." | "A guest. I'm visiting." | Q1, Q6 | Not allowed | Send the file to a family laptop to print. The Guest Wi-Fi keeps visitors away from home devices on purpose. |

Kind lines on the Solved card: Connection "The path was broken: a cable, the Wi-Fi radio, distance or power." Logging in "The path was fine. The device had to prove who it was with the right password." Permission "Logging in worked. The account just isn't allowed to do that, and that is on purpose."

## Interactions in detail
- Calls can be taken in any order; the strip opens any call; an unfinished call keeps its clues for the page load.
- Clue cards can be tapped to select them only during the claim step (selected = thick outline and a check, never color alone). Max 2 selected; a third tap swaps out the oldest.
- Asking every question is allowed; nothing locks. Call time is display only: no score, no stars.
- Key clues: a call is proved by any one of its key clues, except call 1, which needs Q4 and Q1 together (the screen shows a broken connection, the cable answer says which). Call 2's only key is Q4; its Q3 ("Mom's phone works") rules out the router but proves nothing alone. With only one of the two, call 1 gets the "doesn't prove a cause yet" reply.
- Wrong-claim nudge uses the first key clue not yet asked; if both are asked, it quotes the first key clue.
- Fix and ping: about 1.5 s fix animation, then the ping (engine mover, 300 ms per hop). Motion off: fix shows as a before/after swap and the ping jumps hop to hop, same timing.
- House: the tablet drags with pointer or arrow keys (20 units per press, snaps inside the plan); bars update every move. Reset house puts everything back. Nothing saved to localStorage except the kit Motion setting.
- Sizes: the plan draws at real pixel size per box; under 1000 wide the panel goes below with Questions and Make a claim first; at 375 wide the plan shows the caller's room and router with the rest faded, and the question buttons are a 2 x 3 grid. Questions and Make a claim are visible without scrolling at every size.
- Keyboard: Tab order is modes, header, Questions, Make a claim, clue cards, call strip, then map items. In House: arrow keys move the selected tablet.
- `window.__tool = {state, net, setMode, openCall(n), ask(n,q), claim(n, cause, clues), houseTry(device, target)}`.

## Look
Accent `--brand #1f6f43` (help desk green, the color of a good link light). Band 3-5, own `:root`. A bright daytime office console beside a house plan.
- `--paper #eef5f1`, `--panel #ffffff`, `--ink #17261f`, `--muted #50625a`, `--line #d5e3db`, `--btn #1f6f43`, `--head-ink #ffffff`, `--focus #6b3fd1`.
- Plan: floors `#fbf8f1`, walls `#3b4a43`, lawn `#dcebd2`; Wi-Fi arcs `#2a7fb8`; Guest Wi-Fi dashes `#a4471b`. Status badges: Online check on `#1f6f43`, Problem "!" on `#a4471b`, Unknown "?" on `#5f6b66`, each with white text and its glyph. Kind stamps: Connection, Logging in, Permission each with its own icon (plug, key, hand).
- Contrast (computed): white on brand 6.15:1; brand on paper 5.56:1; ink on paper 14.22:1; muted on paper 5.86:1; focus ring on paper 5.82:1; ink on floor 14.85:1; white on problem `#a4471b` 6.01:1; unknown grey on white 5.55:1. All pass AA.
- Neighbors: code-tracer orange `#a8461a` on cream, game-remix teal `#0b6b6f`, score-keeper raspberry. Green on mint office paper is new in this group.

## Art
none: drawn in code. House plan, devices, router lights, caller portraits as simple icon badges (a phone handset with the caller's initial, no faces), badges, stamps and preview.svg are SVG.

## Voice
Bank voice `upbeat-guide` (Zephyr), "Say brightly and clearly, like an upbeat tour guide", here the help desk team lead. Not used by any neighbor (code-tracer clear-teacher, game-remix big-sister, score-keeper friendly-dad) or by any tool in this group. Callers' words are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-calls (how, Calls welcome): "Welcome to the help desk. A caller can't get online. Tap a question to ask it. Each answer lights up part of their house."
- ask (how, hint while asking): "Ask questions until you know what kind of problem it is. Then tap Make a claim."
- claim (how, after a kind is picked): "Tap the cause you think it is. Then tap one or two clues that prove it, and press Send fix."
- need-clue (event, no key clue picked, any cause; stale on any tap): "That clue doesn't prove a cause yet. Tap a clue that shows what is broken."
- kind (how, claim step start): "What kind of problem is it? Tap Connection, Logging in or Permission."
- wrong-kind (event, key clue but wrong kind; stale when a question is asked): "Look at your clues again. Is the path broken, did logging in fail, or did it work?"
- wrong (event; stale when a question is asked): "The caller tried that, and it still doesn't work. Ask another question, or check your clues."
- solved-conn, solved-login, solved-perm (event, on Solved; stale when a call opens): "Solved. It was a connection problem: the path was broken." / "Solved. It was a logging in problem: the device had to prove who it was." / "Solved. It was a permission problem: logging in worked, but that account isn't allowed. That's on purpose."
- next-call (how, after the first Solved): "Tap the next phone on the call strip to take another call."
- shift (event): "That's every call. Look at your shift report: which questions found the problem fastest?"
- w-house (how, House welcome): "This is a house you can change. Tap a device, change something, then try the internet, a website or the printer."
- far (how, first time the tablet drops to 0 bars): "No bars. Walls and distance weaken Wi-Fi. Drag the tablet closer to the router."

## Family engine
`kit/network.js`, described in full in tools/internet-journey/spec.md. This tool uses: **Graph** (the house: router, devices, wire and wifi links, a `cloud` node for the internet, a `printer` node on the home network; the Guest network is a second link kind from the router marked `guest:true`; for a home-device target the tool passes `skip: l => l.guest` to Path and reach, the recipe in docs/families/network.md), **Path/reach** (is there a working path from the device to the cloud or printer), **Draw** with a house-plan skin (rooms drawn by the tool underneath), and **Mover** with `ping` tokens. Wi-Fi bars are the tool's own rule (Content) setting a wifi link's `up`.

## Sources
- CSTA 2026 ids E4-SYS-NT-14, E4-SYS-SE-13 (`data/standards/csta-2026-ids.txt`); CSTA 2017 1B-CS-03, 1B-NI-05: https://csteachers.org/k12standards/
- Authentication (verifying identity) vs authorization (the access rights granted): NIST CSRC Glossary, "authentication" and "authorization", https://csrc.nist.gov/glossary/term/authentication and https://csrc.nist.gov/glossary/term/authorization
- Passwords are case sensitive, so upper and lower case letters count as different (Caps Lock causes "wrong password"): CISA, "Use Strong Passwords", https://www.cisa.gov/secure-our-world/use-strong-passwords
- Wi-Fi signal weakens with distance and through walls; extenders and mesh points extend coverage: Wi-Fi Alliance, "Discover Wi-Fi", https://www.wi-fi.org/discover-wi-fi
- Guest networks keep visitors separate from home devices: CISA, "Home Network Security", https://www.cisa.gov/news-events/news/home-network-security
- Airplane mode turns off Wi-Fi and other radios: FCC, "Wireless Devices on Airplanes", https://www.fcc.gov/consumers/guides/wireless-devices-airplanes
- Wi-Fi bar thresholds are a Curio Class model, labeled "about" on screen. Callers and houses are original.

## Done when
1. Each call, asked all six questions, shows exactly the Content answers, and the map lights the matching part for each.
2. Each call solved with its cause and one key clue shows the right kind stamp and fix sentence; the ping reaches the cloud (or printer, or page).
3. Right cause with only non-key clues asks for a proving clue; a wrong cause stops the ping at an X and gives the nudge for the first unasked key question.
4. Call time counts +1 per question, +2 per wrong claim; no score anywhere; the Shift report lists all 8 calls.
5. House: router off makes every Try fail; tablet in the shed shows 0 bars and fails; Caps Lock on fails Library site only; Guest network fails Family printer only; Kid account fails Parent settings only.
6. Voice: welcomes once per mode; how lines spoken once then hint only; solved lines every time; Read speaks the hint; held clicks behave as in STANDARDS.md.
7. Every size in STANDARDS.md: Questions and Make a claim visible without scrolling; 375 wide works in `drive.py --host`.
8. Keyboard-only call solved; Motion off keeps timing; console clean; no network requests; the name only as "Curio Class".
