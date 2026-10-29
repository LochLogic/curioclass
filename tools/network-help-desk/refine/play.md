# Play lens: network-help-desk (round 1)

Played cold twice: as a grade 4 student alone at home on a 1366x768 laptop, and as a teacher projecting at 1920x1080.
Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py network-help-desk` (119 KB, no recordings yet). Frames in
`S:/CurioClass-codex-scratch/lens-play/shots/` (my drive.py runs, held clicks), voice logs in `.../lens-play/voice/`
(the printed `V.log` is quoted below), audit in `.../lens-play/audit/`. I looked at every frame named here.

Counts: blockers 0, should fix 11, polish 8, nit 3.

## Should fix

1. **The puzzle can be solved the cheap way: ask "What does the screen say?", then pick the card with the same
   words.** Calls (whole tool). I solved all 8 calls with one question each, 1 minute each (`report-1366.png`: Q1,
   Q4, Q4, Q4, Q2, Q4, Q4, Q1). Six of the eight Q4 answers say the cause card almost word for word: "Network cable
   unplugged" for Cable unplugged, "Incorrect Wi-Fi password" for Wrong Wi-Fi password, "no bars" for Too far, "Wrong
   password. And the Caps Lock light is on" for Wrong account password, "You don't have permission" for Not allowed,
   and the airplane for Wi-Fi turned off. A wrong claim also costs nothing that matters (+2 display minutes), and its
   nudge names the question to ask ("Try asking: What does the screen say?", `c1-wrong-1366.png`), so trying cards
   until one works is free. The student never sorts the problem into a kind; the kind comes stamped from the card's
   group. This misses the BUILD wave lesson "no puzzle can be solved by trying every option for free". The builder
   followed the spec's Content, so this is a spec call for the integrator: for example, make Q4 describe symptoms
   rather than name the cause on some calls (Grandma June: "It says the password is wrong" and the Caps Lock light only
   in Q5), ask the student to pick the kind (Connection, Logging in, Permission) before the cause card, or require one
   proving clue that is not Q4. Tag: general.
2. **"Not allowed", the only Permission card, is hidden at 1366x768 after any nudge.** Claim step. Once the orange
   nudge shows (right cause without a key clue, or a wrong claim), the cause board shrinks and its last row is cut
   off inside a scroll panel: only the "Permission" heading's top edge shows (`c1-needclue-1366.png`,
   `c1-wrong-1366.png`, `c7-solved-1366.png` which is really a wrong claim on Leo, `c8-solved-1366.png` likewise for
   Ana). Calls 7 and 8 are exactly the ones where a student retries after a wrong claim and needs that card. Before
   any nudge it shows (`c1-claim-1366.png`). Tag: general.
3. **At 680x425 the cause board shows only the Connection group.** Claim step (`c1-claim-680.png`,
   `c6-solved-680.png`). Logging in and Permission, and half of the second Connection row, are below a scroll edge
   with no cue, so a student in the site preview sees four causes and may not know the other two kinds exist. Same at
   375 (`audit/state-claim-two-clues-375x812.png`: Logging in heading cut, Permission gone). The audit does not count
   it because the board is a scroll panel. Tag: general.
4. **The "next call" how line is never spoken, and its hint names the wrong control.** Solved card. After a solve the
   log shows the solved line and then nothing: `v-solve1b` waited 16 s, `V.heard('next-call')` is false; in
   `v-solve3` the line is logged `dropped` 2.4 s after each solved line, before any tap. The hint then reads "Tap the
   next phone on the call strip to take another call." while a **Next call** button sits in the Solved card with focus
   on it (`c1-solved-1366.png`, `kb-solve.png`). Say the button that is there: "Tap Next call, or a phone on the call
   strip." and make sure it plays once. Tag: general.
5. **At 680x425 the Next call and Shift report buttons are cut off.** Solved card (`c1-solved-680.png`: only the top
   edge of Next call shows; `report-680.png`: the Shift report button is out of view while the hint says "Tap Shift
   report to compare all eight calls."). My drive click on `#next-call` at 680 did not open the report. The 8th
   phone on the call strip is also clipped at 680 and 375 (`c1-claim-680.png`, `audit/state-solved-375x812.png`).
   Tag: general.
6. **The skipped welcome comes back after the student has already acted.** Calls, first tap. Tap a question first and
   the log reads `ask` (1.3 s) then the welcome at 6.6 s: "Ask questions until you know ... Then tap Make a claim."
   followed by "Welcome to the help desk ... Tap a question to ask it." (`v-ask5`, `v-all6`, `v-askfirst`). At a 2 s
   pace the welcome lands while the student is on their fourth question. The tool sets `welcomeAfter: true`, which
   KIT.md says is for one-mode tools; this tool has two modes, so STANDARDS applies: skip the welcome on a first tap
   that has its own line and let Sound off/on or the next mode entry bring it. The audit's "welcome heard" column marks
   this as fine; it cannot hear the order. Tag: general.
7. **A broken link uses the Guest look.** Map, Calls and House. A cut cable or a 0-bar Wi-Fi link is drawn in orange
   dashes (`c1-all6-1366.png`, `c4-all6-1366.png`, `house-shed-1366.png`), and the legend says orange dots mean
   "Guest". A student reading the legend sees Grandpa Lou's desktop "on the Guest network". Give the broken state its
   own style (grey with the break mark, or red X on the link) and keep orange for Guest only. Tag: family:network.
8. **Router off still shows Wi-Fi waves and working links.** House (`house-routeroff-1366.png`). The router tile is
   orange with "Off" and every device has an X, but the blue arcs still radiate and every cable and Wi-Fi link is drawn
   up. The picture says the network still works. Draw the links down (or faded) and drop the arcs when the power is
   off. Call 5 (router has no power) has the same problem: the dark router still shows Wi-Fi arcs to Aunt Rosa's
   laptop (`c5-all6-1366.png`). Tag: general.
9. **The Shed spot is drawn on the Shed's wall, not in the Shed.** Sam's phone (Call 4) sits on the Bedroom/Shed wall
   over the "Back door" label (`c4-all6-1366.png`); after the fix it moves onto the "Back door" label, covering it
   ("k door", `c4-solved-1366.png`). In House the tablet at the shed spot also lands on the wall (`house-shed-1366.png`,
   `audit/state-house-shed-375x812.png`), and the drawn Shed room is empty. The rooms are drawn on screen fractions
   while devices use the design box, so they don't line up near the edges. A student told "it works fine in the
   house" should see the phone out in the Shed. Tag: general.
10. **Ana's laptop is badged "Allowed" when she is not allowed.** Call 8 solved (`c8-solved-1366.png`). The fix is to
    send the file to a family laptop because the guest can't reach the printer, but Ana's guest laptop gets a green
    "Allowed" badge, and both laptops are labelled "Laptop", so the student can't tell which one printed. Badge Ana's
    laptop "Sent" (or leave her "Guest" badge) and label the two "Ana's laptop" and "Family laptop". Tag: general.
11. **"about 1 bars of 3".** House readout (`house-corner-1366` result: "At this spot: about 1 bars of 3"). Words match
    the state (POLISH): "about 1 bar of 3". Tag: general.

## Polish

1. **Small maps hide device names, and two pairs of icons look alike.** At 760, 680 and 375 the map draws icons only
   (`d-760.png`, `house-760.png`, `house-680.png`). Desktop and TV are the same monitor; Phone and Tablet are the same
   rectangle. In House the student taps devices by look, and "Tablet" is the one to drag. Short labels (or distinct
   icons) would fix it. The handoff calls the names "redundant"; at these sizes they are not.
2. **The 680x425 and 375 maps are crowded.** Badges cover icons and room labels ("Grown-up" over the desktop and
   printer, "On" over the TV and laptop, the Living room label under a badge at 375), devices straddle walls, "Office"
   sits on the top wall (`c1-all6-680.png`, `c1-solved-680.png`, `audit/state-claim-two-clues-375x812.png`). The spec
   asked for 375 to show the caller's room and router with the rest faded; it shows the whole house instead. A
   per-call crop at small sizes would make the preview readable.
3. **The internet cloud sits inside the Kitchen.** Every Calls frame: the router's cable runs across the Kitchen to a
   cloud by the Kitchen wall, crossing the Phone and Ana's laptop labels (the audit's shift-report lead). Put the cloud
   outside the house on the lawn, so "the internet" is clearly not a room.
4. **The Solved card drops the clue that proved it.** Clues hide on solve and the card says only "Questions asked: Q1,
   Q4" (`c1-solved-1366.png`). Show the proving clue's text ("Proved by: A little computer with an X: Network cable
   unplugged."). It is the moment the lesson should land. The shift report could also mark the key question per call,
   since it asks "which questions found the problem fastest?" but never says.
5. **House results don't name the kind.** The result chip looks the same for "Online", "No connection", "Wrong
   password" and "Not allowed" (`house-try-1366.png`, `house-routeroff-1366.png`), though the code computes the kind.
   A stamp (plug, key, hand) like the Solved card would let House reinforce the three kinds, and a pass/fail glyph
   would help.
6. **The Wi-Fi bars live only in small grey text in the panel.** House: dragging the tablet, the student must look away
   from the map to "At this spot: about 2 bars of 3" (`house-1366.png`). Bars drawn next to the tablet on the map would
   make the drag the experiment. There is also an empty gap under the Try row where the result chip is reserved.
7. **First-screen hint names no control.** "Ask questions until you know what kind of problem it is." (`d-1366.png`).
   For a solo student: "Tap a question to ask the caller. Then tap Make a claim."
8. **Projector sizes.** At 1920x1080 the call time, privacy line, legend and map notes are 11 to 13 px
   (`d-1920.png`); a class reading clue cards off the screen would want the map notes and legend larger.

## Nit

1. Need-clue shows the same message twice, in the nudge and the hint ("Right cause. Which clue proves it? Tap a
   different clue." / "Right cause. Now tap a clue that proves it.", `c1-needclue-1366.png`).
2. The "Online" and "On" badges sit over the device tile and the router link (`c1-solved-1366.png`, `c4-solved-1366.png`
   where "Online" also covers the Tablet).
3. The wrong-claim X on calls 3 and 8 covers the router icon (`c8-solved-1366.png` wrong-claim frame).

## What worked

Every call opens on a clear call card; each question lights the right part of the map (`c1-all6`, `c4-all6`,
`c5-all6`, `c7-all6`, `c8-all6` match the spec's answers); the wrong ping stops at the break with an X; the kind stamps,
fix sentences and kind lines are right for calls 1 to 8; Call time counts +1 and +2 (`v-wrong5`: 11 min after one
question and five wrong claims); keyboard-only solve works and focus lands on Next call (`kb-solve.png`); Motion off
keeps the fix wait (`c3-mid-calm-1366.png`, `c3-solved-calm-1366.png`); House results follow the rule order (library
with Caps Lock, printer on Guest, shed 0 bars, router off all checked).

## Voice check (browser voice, held clicks, Sound on)

| line | kind | expected | spoken |
|---|---|---|---|
| ask (5 questions, 6 s apart) | how | 1 | 1 |
| claim | how | 1 | 1 |
| all-clues | how | 1 | 1 |
| ask-first (Make a claim twice, no clue) | how | 1 | 1 |
| wrong (5 wrong sends) | event | 5 | 5 |
| need-clue (5 sends) | event | 5 | 5 |
| solved-conn / solved-login (3 solves) | event | 3 | 3 |
| next-call | how | 1 | **0** (dropped or never queued; should fix 4) |
| w-calls after a question as first tap | welcome | skipped until Sound or mode | **played after the tap's line** (should fix 6) |

First taps: Sound says nothing (`v-first-sound`); Read speaks the hint only (`v-first-read`); House gets its welcome
(`v-first-house`); the stage and Tab get the welcome; Sound off and on brings the welcome once (`v-sound-offon`). Read
during a line stops it and a mode change after Read starts at once (`v-read-during`). Fast taps then House and back:
house welcome cut by the switch, calls welcome plays, no stale how line (`v-fast-stale`).

## Audit pilot

Ran `audit_tool.py --port 9410` (full walk, 3 leads). Sizes, Motion off, focus on load, console errors and the voice
repeats were clean, and my own frames agree; I cite those rows.

- **Confirmed:** shift-report "Phone" and "Laptop" labels under another box: the router-to-cloud cable crosses both
  labels at 1280 and up (polish 3).
- **Wrong:** "Tablet: nothing changed". The tablet is selected by default, so a tap on it has nothing to change; it is
  not dead (drag and arrow keys work, `house-shed-1366.png`).
- **Missed:** the clipped cause cards at 1366 after a nudge and at 680/375 (inside a scroll panel, so it is skipped by
  design, but here the scroll panel hides a whole kind); the Next call and Shift report buttons cut off at 680; the
  next-call line never spoken; the welcome played after the first tap's own line (its column says "heard", which reads
  as a pass); and everything about meaning: the Q4 giveaway, the broken-link and Guest style clash, the router-off arcs,
  the Shed position, the "Allowed" badge on Ana, "1 bars".

Builder claim checked afterwards: handoff.md says compact maps leave out device names as "redundant"; at 760 and below
the desktop/TV and phone/tablet icons can't be told apart (polish 1).
