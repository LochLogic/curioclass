Verdict: FIX (2 blockers, 5 should fix, 5 nits). The math is right everywhere. The blockers are both in card 6: things on screen give away the prediction.

Verified cold 2026-10-26 on the draft bundle (`CURIO_DRAFT=1`, code-drawn art; voice only partly recorded, which was not held against it). Frames came from a muted headless Chrome driven over CDP with held clicks, real drags and real keys. The 375 px frames used an iframe host.

## Blockers

1. **Card 6 placeholders are the answer.** src.html:176-177: the prediction boxes have `placeholder="3:00 pm"` and `placeholder="150"`. Those are exactly the meeting time and mile the card asks for (recomputed: 75(t - 1) = 300 - 50t, so 125t = 375, t = 3, d = 150). Seen in frame h375-dispatch and in the source. Use neutral placeholders such as "e.g. 1:45 pm" and "e.g. 95", or none.
2. **Card 6 answer can be read before Play.** With the answer hidden ("Your call"), Show gap still works and the clock tab and plane clicks still scrub the clock. At 3:00 pm the gap label reads "gap 0 miles", both ladder markers sit together at mile 150, and both trains overlap in the scene (frame c6-before; js: ring hidden, gap label "gap 0 miles"). The two lines also cross exactly on a labeled grid point (3, 150). Under VERIFY 7 and POLISH ("nothing on screen gives the answer away"), disable Show gap and clock scrubbing (tab, plane click, arrows) until the reveal. Whether the lines should stay on the graph during the prediction is a call for Cory: the spec hides only the ring, the label and the algebra.

## Should fix

3. **Dispatch at 1366x768: Check is below the fold.** With the card 1 panel at 1366x768, Check, Show a hint and Next card sit at y 861-905 and the card text at 777-855 (panel scrollHeight 962, clientHeight 688; frame dispatch-c1-solved, check dispatch-fold). Students press Check after every change, so they have to scroll the panel every time. STANDARDS: main controls visible without scrolling. Consider a compact ticket row, or putting the card text and buttons above the train cards' equations.
4. **"The gap stays N miles forever" can be false.** Repro in Yard: A eastbound from mile 0 at 100 miles per hour; B eastbound from mile 0, departing 1:00 pm, at 100. The banner says "Same speed, same direction: the gap stays 100 miles forever. No solution." At 3:30 pm the gap label reads "gap 50 miles", because A has arrived at Brookport and B is still closing in (check arrive-gap). The spec changed preset 3 for exactly this reason, but free play still reaches it. The words must match the state. Say, for example, "the lines stay 100 miles apart" or "while both are running", or add an arrival note.
5. **Targets under 44 px.** The range sliders are 71x36 (30 px tall in compact) and the number boxes are 80x40 (34 in compact) (targets check at 1366x768; CSS src.html:53-54, 95-96). STANDARDS asks for at least 44 px.
6. **The 680x425 preview page scrolls.** The document is 486 px tall in a 425 px box. Scrolling hides the header and shows a blank band under main (frame of680, scrollY 61). The panel scrolls on its own (overflow auto), so something escapes it. The likely cause is the absolutely positioned `.sr` "Presets" label inside the panel (the panel is not `position: relative`), along with other `.sr` spans in the panel.
7. **Dispatch hint says "press Check" on cards with no Check.** Cards 6 and 7 show the hint "Locked settings come from the ticket. Change the others, then press Check." (frame h375-dispatch), and Read speaks it. Card 6 has Play and card 7 has "It can't be done". Card 7 also has no locked settings.

## Nits

8. The Check message wording "They meet at about 4:17 pm at mile about 171.4, not at Millbrook." (card 1 at its starting speed of 30) reads oddly. "at about mile 171.4" would read better (src.html:997, `mileWords` after "mile").
9. The spec and the code disagree on two hints. Card 3 in code says "Turn on Show gap and watch it as you change B's speed. When does it stop changing?", but the spec says "Watch the gap as you change B's speed...". Card 7 has a hint in code ("Try every case: ...") that the spec does not list. The code versions are fine; update the spec.
10. With Show the algebra on at 1366x768 in Yard, the conclusion lines ("t = 3, so 3:00 pm", "d = 60(3) = 180 miles") and the fact line sit below the fold (frame meet-after-1366).
11. The legend box covers part of Train B's line at 680x425 and at 375 wide (frames w680, h375). The gap label runs across Train A's line at 6:30 pm in "Same speed" (frame same-speed-gap); the halo keeps it readable.
12. Dragging B's speed handle up from Brookport flips B to eastbound, and the terminus rule moves its start to Ashford in the middle of the drag (drag-speedB-flip ended eastbound, mile 0, 100 miles per hour, "meet at 12:00 pm at Ashford"). This is the spec's rule, but it is a surprise under the pointer. The tip explains it.

## Checked and correct

- **Numbers, recomputed in Python with exact fractions and matched to the screen:**
  - Presets:
    - Head on: t = 3 h, 3:00 pm, 180 miles, Pine Hollow.
    - Catch up: 3:00 pm, 120 miles, Millbrook.
    - Same speed: gap 45 miles at every quarter hour from 0 to 7. A ends at 290 and B at 245 at 7 pm.
    - Same schedule: d = 60t for both, side by side 2:00 pm to 5:00 pm.
    - Too slow: t = -9/2, so 4.5 hours before noon, d = -180.
  - Cards, with each card's only answer on the slider grid:
    - Card 1: B at 60, 3:00 pm, mile 120.
    - Card 2: departs 3:00 pm, meets 6:00 pm at mile 240.
    - Card 3: 35, gap 45.
    - Card 4: 60.
    - Card 5: departs 2:30 pm, meets 4:30 pm at mile 120.
    - Card 6: 3:00 pm, mile 150.
    - Card 8: A at 15 and B at 60, 4:00 pm, mile 240.
  - Starting and wrong states:
    - Card 1 at 30: 30/7 h, about 4:17 pm, about 171.4 miles. At 40: 3:45 pm, mile 150, matching the spec's example message.
    - Card 2 at 2:00 pm: 4:00 pm, mile 160.
    - Card 5 at 2:00 pm: 4:12 pm, mile 132.
    - Card 8 with A at 20: 3:45 pm, mile 225.
    - Card 4 with B at 55: d = 55t + 10.
  - Free play:
    - B at 50: 300/110 h, about 2:44 pm, about 163.6 miles.
    - B at 100: 1.875 h, about 1:53 pm, 112.5 miles.
    - Gap at 3.1488 h: 14.9 miles.
    - Crossing after 7 pm: 300/35 h, about 8:34 pm, about 214.3 miles.
  - Edge cases: a meeting exactly at 7:00 pm (A from mile 70 at 10, B from 0 at 20, both eastbound) counts as One meeting and fires during Play. Waiting labels ("departs 1:00 pm") and "arrived" are correct.
- **Banners, algebra box and Done when:** all four banners and the algebra box match the spec text word for word for presets 1 to 5. Done when 1 to 4 pass. For Done when 5, a real drag of the speed handle changes the slider, both equation forms and the line together; the direction flip works; keyboard on the dots, handle and sliders gives the same results. For Done when 6, every listed answer passes Check, wrong values get plain messages without the answer, card 6 needs both boxes before Play (1 minute / 1 mile tolerance works, re-hide after a changed call works), and card 7 accepts It can't be done and gives the "infinitely many, not two" note at Always together. Done when 7 passes at 1366x768 and 1280x720 in Yard, at 375 wide (usable), and in the 680x425 preview (smallest scene text 11 px). Done when 8 passes: Motion off jumps to 7:00 pm with the meeting label shown, and Motion turned off mid-Play does the same. Sound off makes no speech and no tones (`tone` checks `sound`). Read speaks the hint, then the status.
- **Voice queue:** a first tap on Play skips the welcome unmarked. Show gap, Dispatch and Read each queue their own line (the Read path matches the collision-lab pattern). Beats wait while a long clip plays and are not dropped.
- **Contract:** one file. No fetch, XHR, external src or link, and no network requests. No console errors or exceptions in any shot. Kit used (Plane, slider, say, tone). Every control has visible focus and keys (Space, R, arrows, Home/End on the clock).
- **Lines and words:** all 14 spoken lines in `L` and `allLines()` match voice/lines.json word for word. No em or en dashes and no "Curio" alone in src, notes, spec, lines, prompts or the draft json. No points, timers or streaks.
- **Contrast**, recomputed: brand on paper 7.61, white on brand 8.14, ink on paper 12.63, muted on paper 5.61, A on paper 4.85 and on white 5.18, B on paper 6.27, brand on ticket 7.45, white on the button color 10.33. Letters A and B always ride with the colors, and B's line is dashed 10 6.
- **Art:** all three `art:` tokens have prompts.json entries, and none shows people.

## Re-verify

Verdict: FIX (2 small should fix, no blockers). Every earlier blocker and should fix is fixed and nothing regressed. Two small target and fold misses remain.

Re-checked cold 2026-10-26 on a fresh `CURIO_DRAFT=1` bundle (507 KB) with the real FLUX art and all 14 recorded clips. I used a muted headless Chrome on my own port, with held clicks (120 ms), real drags, real keys and a 375 px iframe host. There were no console errors or exceptions in any shot.

### New findings

1. **Card 6 at 680x425: Show a hint and Next card are below the fold** (should fix, small). They sit at y 399-443 in a 425 px box (frame d6-680), so the panel has to scroll to reach them. Card 6's own controls are visible: Play at 135-179 and both prediction boxes at 349-393. Cards 1 and 7 at 680x425 are fine (Check, Hint and Next at 331-375; It can't be done and Hint at 274-318, Next at 324-368). The long card text is what pushes them down, so a compact card text or prediction row would fix it.
2. **Dispatch ticket buttons are 43x44 in the wide layout** (should fix, small). That is 1 px under 44 at 1366x768, 1280x720 and 1920x1080 (eight across in the 400 px panel). The compact layout uses four across and passes. The checkboxes are 20 px, but their labels are 44 px tall and clickable, so they pass.

### Earlier findings

- **1 (blocker): fixed.** The placeholders are now "like 1:45 pm" and "like 95" (src.html:175-176, js check).
- **2 (blocker): fixed.** I checked card 6 before Play with real input:
  - Clock: a real drag of the clock tab, two plane clicks and four ArrowRight presses on the focused tab all leave t = 0. The tab is aria-disabled and dimmed, and the tip says the clock moves only with Play.
  - Hidden answer: Show gap is disabled (a real click leaves it off), the algebra is disabled and hidden, and Jump is disabled. The ring, meeting label, flag and gap bracket are all hidden.
  - Lines: before Play no line is drawn (frame d6-1366). Paused mid-run at 2:21 pm, each line is drawn only to the clock (frame c6-mid).
  - Space: with empty boxes, Space does not play and the tip says to fill in both.
  - Status: it reads "Your call", and the equations stay visible, as the spec says.
  - Reveal: "3 pm" and 150 reveal at the meeting with "You called it" and the stamp. 2:45 and 140 get the try-again message. With Motion off, 3:01 pm and 151 are accepted (1 minute and 1 mile tolerance).
- **3 (should fix): fixed.** Check, Show a hint and Next card are visible without scrolling at every listed size:
  - 1366x768: Check, Hint and Next at 373-417 (card 1), Hint and Next at 439-483 (card 6), It can't be done and Hint at 354-398 (card 7).
  - 1280x720: same positions.
  - 1000x625: Check, Hint and Next at 312-356 (card 1), Hint and Next at 362-406 (card 6), It can't be done, Hint and Next at 274-318 (card 7).
  - 680x425: see new finding 1.
- **4 (should fix): fixed.** In the repro, A and B both run east from mile 0 at 100 miles per hour, with B leaving at 1:00 pm. It now reads "the lines stay 100 miles apart and never cross. No solution. On the track the gap changes while a train waits to leave or after it stops at the end of the line." The gap at 3:30 pm is 50 miles, which matches my recompute. Preset 3 still says "the gap stays 45 miles forever", and its gap reads 45 at all 29 quarter hours.
- **5 (should fix): fixed.** The range sliders and number boxes are now at least 44 px in both layouts. A scan of every visible button, input, select, graph handle and the clock tab at 6 sizes finds only the tickets (new finding 2) and the label-wrapped checkboxes.
- **6 (should fix): fixed.** At 680x425 the document is 425 px tall in a 425 px box, and scrollY stays 0 even after scrollIntoView on the fact line and on the tickets. The panel scrolls on its own. The panel is now `position: relative`.
- **7 (should fix): fixed.** The hint on card 6 is the card-predict line and on card 7 the card-twice line. Read speaks those recorded clips.
- **8 (nit): fixed.** It now reads "They meet at about 4:17 pm at about mile 171.4, not at Millbrook."
- **9 (nit): fixed.** Spec card 3's hint and card 7's hint now match the code.
- **10 and 11 (nits): left as reported.** The legend still covers part of B's line at 375 wide (frame h375-yard).
- **12 (nit): unchanged, by the spec's rule.** A real jittered drag of B's speed handle upward flips B to eastbound from Ashford at 100 miles per hour. The status then reads "They meet at 12:00 pm at Ashford, mile 0.", which is correct.

### Re-checked and correct

- **Math, recomputed in Python with exact fractions, all matching the screen:**
  - Presets: Head on 3:00 pm, 180 miles (Pine Hollow). Catch up 3:00 pm, 120 (Millbrook). Same speed gap 45 at every quarter hour, with A at 290 and B at 245 at 7 pm. Same schedule side by side 2:00 to 5:00 pm. Too slow t = -9/2, d = -180, shown as "4.5 hours before noon, at mile −180".
  - Algebra box: every preset matches, for example "d = 50(−4.5) + 45 = −180 miles".
  - Each card's only answer on the slider grid: card 1 B 60 (3:00 pm, mile 120); card 2 3:00 pm (6:00 pm, 240); card 3 35 (gap 45); card 4 60; card 5 2:30 pm (4:30 pm, 120); card 6 3:00 pm, mile 150; card 8 A 15 and B 60 (4:00 pm, 240). Each passes Check.
  - Wrong values give plain messages without the answer: card 1 at 30 says about 4:17 pm (30/7 h), about mile 171.4 (1200/7), and at 40 says 3:45 pm, mile 150. Card 2 at 2:00 pm says 4:00 pm, 160. Card 3 at 50 says 3:00 pm, 150, and at 20 says "Lines cross, trains don't meet". Card 4 at 55 says d = 55t + 10. Card 5 at 2:00 pm says 4:12 pm, 132. Card 8 with A at 20 says 3:45 pm, 225.
  - Card 7: Always together gives the "infinitely many, not two" note (only while card 7 is unsolved), and It can't be done solves it. Locked settings refuse changes with the "Set by dispatch" tip.
- **Art:** the real FLUX webps are in. The trains are drawn at their own aspect at every size, with no squash: A 4.32-4.35 (source 4.33) and B 5.39-5.41 (source 5.41). They are 130/162 px at 1366, 121/151 at 1280, 108/135 at 1000, 87/108 at 680 and 375, and 139/173 at 1920. The alpha box is tight (rows 0-159), the picture bottom sits on the rail, and zoomed crops show the wheels on the rail. Westbound trains are mirrored (scale(-1,1)) with the locomotive leading west, and the badges stay unmirrored. A waiting train fades to 40 percent with "departs 1:00 pm". All 3 tokens have prompts.json entries, and no people are shown.
- **Voice:** each line is in its clip, logged from Audio.play:
  - All 14 lines.json lines have clips, and lines.json, `L` and local.json agree word for word.
  - A first held tap on Play plays yard-ladder, skips the welcome unmarked, then plays first-meet after the ladder line ends. The chime sounds at the meeting.
  - A first tap on Show gap plays the gap line. Read then pauses it and plays the hint clip, then the status by browser voice.
  - The welcome plays on an empty tap, and Dispatch cuts it for dispatch-welcome. Ticket 6 cuts that for card-predict, and ticket 7 for card-twice.
  - Read as the first tap speaks first and queues the welcome after it (the collision-lab pattern).
  - Sound off as the first tap gives no clips, tones or speech through a full Play. Turning Sound back on queues the welcome, and Sound off mid-clip pauses it.
- **Motion off:** with Motion off before Play, or turned off mid-Play, the clock jumps to 7:00 pm with metAt 3, the "meet 3:00 pm, mile 180" label and the flag showing.
- **Keyboard:** on dot A, ArrowRight and ArrowUp give 12:15 pm and mile 5. Tab moves to A's speed handle, and two ArrowUp presses give 70 miles per hour. Space on the body plays.
- **375 wide:** the iframe host stacks the layout with no sideways scroll (scrollWidth 375).
- **Contract:** one file with no http src or href, fetch or XHR. No em or en dashes and no "Curio" alone in the src, spec, notes, lines, prompts or draft json.

## Integrator note (2026-10-26)

Re-verify 2 items (card 6 buttons at 680x425, ticket buttons 44 px), the ON TIME stamp beside a wrong answer and nit 11 were fixed by the builder; the integrator looked at rv2-d6-680.png (all card 6 controls in the 425 box) and rv2-d1-wrong.png. Going live.
