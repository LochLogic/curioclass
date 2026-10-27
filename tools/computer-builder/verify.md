PASS WITH FIXES

# Verify: computer-builder (Grade 1, Computer Builder)

Verified cold on 2026-10-26 against spec.md, docs/agents/VERIFY.md, STANDARDS.md and BATCH-CS.md. The build is src.html, bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py computer-builder` (452 KB with the six final images, no clips yet). Testing used headless Chrome over CDP with real held clicks (120 ms), jittered mouse drags, real key events, a speech and voice-log monitor, and an iframe host for the 375 wide checks. The real art was rebundled and judged in place.

One must-fix: keyboard focus falls to body. Everything else in "Done when" passes.

## Must-fix

1. **Keyboard focus is lost to body after five buttons.**
   - Evidence: Tab to the button, press Enter, then read document.activeElement. It is BODY after All in one (the button is hidden), Back to desk (its row is hidden), Try it (disabled during the run and still body afterwards), Next job (hidden right after pickJob, because deskChanged sets success to false) and Start in Missing (disabled, still body at the ask phase). A keyboard user has to Tab again from the top of the page each time.
   - Suggested cause: sync() hides or disables the focused control with no focus handoff. Fix this by moving focus to the next sensible control before hiding: the first AIO kind or spot, the AIO button on return, the job card or Try it, the first job card, or the first part tile in Missing. Alternatively, keep Try it and Start enabled with aria-disabled and ignore presses while busy.

## Should-fix

1. **"The computer box! It's the brain." teaches that the case is the processor.**
   - Evidence: The box tile line and the no-box line call the box itself the brain. GCFGlobal (Computer Basics, inside a computer) says the CPU inside the case is the brain. The spec's own tablet and laptop hotspot line, "The brain is hiding inside!", says the same thing as the source.
   - Suggested cause: wording in the spec voice list. Use something like "The computer box! The brain is inside." in spec, src and voice/lines.json together.

2. **Missing round 7 (box unplugged) shows other parts working without a box.**
   - Evidence: Round 7 gives the symptom "Nothing works! Every computer needs a brain." A wrong tap on the screen then lights the desktop, orange stars flow out of the unplugged box, and the line "The screen works!" plays. Other wrong parts flow the same way. This contradicts the round's lesson and the Build mode behavior, where no box gives the no-box line and a "?" puff.
   - Suggested cause: missingTap calls flow(id, d) and setScreen({kind:'desktop'}) for a wrong part without checking m.out === 'box'. render only looks at state.placed.has('box'). When the box is the missing part, wrong taps should show the Build-mode no-box result (dots to the loose plug, "?" puff), plus a short line.

3. **Ghost outlines, dots and stars are faint where they cross the wood desk.**
   - Evidence (recomputed): The spec measures contrast against the wall and the paper only. Most of the graphics sit on the wood: dashed ghost outline on wood 2.12:1, teal in-dots on wood 2.3:1, orange out-stars on wood 2.41:1. All are below the 3:1 non-text minimum. The dots and stars have a white stroke, so they still read, but the dashed ghosts on the desk (the main hint in Jobs) are hard to see in the 1366 screenshots and would be worse on a projector.
   - Suggested cause: the token colors were chosen against the wall only. Darken the ghost stroke, or add a light halo under it, and record wood ratios in the spec.

4. **On narrow placed tiles the check badge covers the part picture.**
   - Evidence: At 375x812, once a part is placed its shelf tile shows the check badge over most of the small part drawing. A non-reader can no longer tell which tile is which.
   - Suggested cause: the badge is positioned and sized for wide tiles. Shrink it and move it to a corner at narrow widths, or dim the tile and keep the picture visible.

5. **Jobs shelf is below the fold at 375x667.**
   - Evidence: At 375x667 in Jobs, the shelf tiles sit at 706-776 px, so the page must scroll to add a part. At 375x812 everything fits.
   - Suggested cause: the panel order is Try it, cards, shelf (accepted below), and the job cards take the height. Use a shorter card row or a two-row card grid at short phone heights. This is low priority, since phones are not the main K-1 use.

6. **The tablet drawing reads as a desktop monitor.**
   - Evidence: The tablet is drawn landscape on a trapezoid stand, about as large as the monitor. In the AIO screenshots it looks like a screen on a stand rather than something you hold. All six tablet hotspot lines play correctly (camera, mic, touchscreen, speakers, brain, pop-up keyboard).
   - Suggested cause: drawing choice. Remove the stand, draw a thin bezel with rounded corners, add a hand or a slight tilt, or make it portrait.

7. **There is no preview.svg.**
   - Evidence: scripts/build_site.py sets `t['preview']=(folder/'preview.svg').exists()` and uses it on the site cards. 72 of 81 tools have one, including robot-dance from this batch.
   - Suggested cause: not built yet. Add one before release (see the deviation note below).

## Nice-to-have and nits

- Nibbles is about 100-110 px tall at 1366 but only about 50 px in the 680x425 preview, where the plug in its paws is barely visible. A minimum size would help.
- At found in Missing, the replug is only a redraw. Showing the loose plug in Nibbles' paws, then the plug sliding in with one flow of dots, would make the cause and effect clearer. The cable looks connected while the part is "missing"; that is needed so the answer isn't given away, so keep it.
- Any long drag counts as removal. Dragging the box about 0.3 of the stage width sideways across the desk removed it. The cable does not follow a dragged part. No line plays on removal, which is fine. Cause: partDown treats a release more than 160k units away as off the desk.
- The backdrop crops the top of the pegboard and its tools under the header. Fit is otherwise good at every size.
- The art/prompts.json backdrop prompt uses negative wording ("No desk, no furniture, no posters, no writing...") and lacks the "blank surfaces" phrasing STANDARDS asks for. The image came out clean, so this only matters for a reroll.
- The laptop brain hotspot sits at the base right, not the middle of the base. The tablet mic is drawn as a single dot while its line says "These tiny holes".
- notes.md calls E1-SYS-HW-11 a 2017 code. It is the 2026 CSTA identifier; 1A-CS-01 is the 2017 one.
- If the very first tap is a desk part whose line comes later (for example the speakers show), the welcome plays first and the part line follows about 4 s later. That is acceptable, but a tile tap skips the welcome and a desk tap does not.
- With browser TTS, after a cancel, Read sometimes ended only on its timeout (about 4 s of silence). This is a speechSynthesis artifact. Recorded clips should remove it; recheck once clips exist.

## Builder deviations

- **Jobs panel order is Try it, cards, shelf.** Accept. The action stays on top and nothing scrolls at the side layouts.
- **At 375 wide, four desk part buttons are 51-58 px wide (60+ tall) and back-row parts are about 48 px apart.** Accept as nice-to-have. Every target is 60+ at 1280, 1366 and 1920, and phones are not the K-1 classroom use. Taps on the back row hit the intended part in testing.
- **Compact 16:10 layout (landscape under 700 px tall): header and panel buttons and hotspots are 44-52 px.** Accept. Measured: header 44, panel 46, hits and spots 48-49. This is the preview size; the projector sizes are 60+.
- **The welcome plays once per mode per session, and Read drops queued lines.** Accept. This matches STANDARDS: no repeat on re-entry, and Read restarts cleanly.
- **No preview.svg.** Should-fix, see above. The site uses it and the batch sibling has one.

## What passed (evidence)

- **Done when 1:** all 7 parts land in their slots, and every name is voiced.
- **Done when 2:** with keyboard and screen only, the tap gives the no-box line, the screen stays dark, and dots run to the loose plug with a "?" puff. After adding the box, the keyboard types H then E, with teal dots moving to the box (sampled coordinates).
- **Done when 3:** "Everyone, say hello!" plays, the wave runs, then the no-speakers line. "Hello, class!" never plays.
- **Done when 4:**
  - AIO is locked until all 7 parts are placed, then the all-built and aio lines play.
  - All 7 laptop hotspots and all 6 tablet hotspots play the right lines.
  - Back to desk restores the built desk.
- **Done when 5:**
  - The cartoon with box and screen plays muted, shows a crossed speaker, and says "No sound!"; only the 2 speaker ghosts pulse.
  - Adding speakers gives success and Next job.
  - An extra keyboard gets Zzz and the rest line.
- **Done when 6:**
  - All six jobs check off, and the six-jobs line plays exactly once (not again on a redo).
  - Picking another job mid-run stops the run.
  - An empty desk gives its line.
- **Done when 7:**
  - All seven rounds play in spec order with their symptom lines, and wrong taps show the part working.
  - Found brings Nibbles with the plug, then the full job.
  - The all-fixed line plays, Start restarts at round 1, and the plug counter counts.
- **Done when 8 (voice):**
  - Lines are marked said on start, and Read on a first tap reads without marking.
  - A mode switch mid-line drops the queue.
  - Read cuts the current line, and lines triggered during Read wait.
  - Sound off stops speech but still updates the hint. Sound on queues the never-said welcome once.
- **Done when 9 (keyboard):**
  - Every control is reachable.
  - Letters type on the screen (C, A, T tested).
  - Spots work with Enter and Space.
  - Tab order is header, shelf, Clear and AIO, then desk parts left to right.
  - Focus loss is the must-fix above.
- **Done when 10 and sizes:**
  - Nothing scrolls at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 or 760 wide. 375x812 fits.
  - Scene text (Zzz, puff) is at least 14 px. The hint caption is 13 px in the preview only.
- **Motion off:**
  - There are no fly copies; a steady arrow replaces the dots, and the blanket fades.
  - Nibbles is static.
  - Missing timings are unchanged (6460/10610 ms with motion vs 6507/10374 ms without).
  - Spots do not scale, and the AIO unlock animation is effectively instant.
- **Real mouse drag at 1366 and 680:**
  - A short drag snaps back with no show.
  - Dragging to the shelf or up onto the wall removes the part.
  - Dragging one speaker removes both.
- **Console:** clean. The only entry was a favicon.ico 404 from the test server. The tool makes no network requests.
- **Lines:** voice/lines.json has 68 lines, identical in order to allLines() and to the spec voice list. There are no duplicates, no em dashes and none over 200 characters. No mp3 clips are recorded yet. The estimated bundle with 68 clips is about 1.3 MB, under 2 MB.
- **Contrast:** every ratio stated in the spec recomputes exactly. The disabled Try it text is 4.7:1.
- **Facts:**
  - Input and output directions are correct.
  - Laptop and tablet parts are correct, and video chat needs camera, mic, screen and speakers.
  - Facts match GCFGlobal, CSTA (E1-SYS-HW-11 / 1A-CS-01), Code.org and the National Zoo (giant panda).
  - The one wording problem is should-fix 1.
- **Grade 1 "reads nothing":**
  - Every control has an icon, and every on-screen word is also voiced.
  - Job cards and rounds are pictures.
  - Motion shows cause and effect: dots in, stars out, the screen glow, the pulsing ghost of the missing part, and the "?" puff at a loose plug.
- **Art (real images in place):**
  - prompts.json matches the spec art list: 6 assets, names, aspects and refs, all reviewed ok, no people.
  - Backdrop is 1600x914, fits, and has a minor pegboard crop.
  - bubbles-bowl reads well.
  - bubbles-photo and panda came out square (640x640, specced 4:3) but slice-crop cleanly into the 4:3 frame. The fish is whole, and the panda keeps its ears and paw.
  - nibbles and nibbles-plug read clearly at 1366 and are small in the preview (nice-to-have above).

## Re-verify

PASS WITH FIXES

Re-verified cold on 2026-10-26 after the builder's fixes. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py computer-builder` (447 KB, six final images, no clips yet). Testing used a muted headless Chrome over CDP (own profile, port 9561) with real held clicks (120 ms, 1 px jitter), whole-pixel jittered drags, real key events, a voice-log reader (`__tool.vlog`), a 50 ms body-focus monitor, and an iframe host for the 375 wide sizes. The must-fix and all seven should-fixes are fixed. Three new should-fix items (two small keyboard and phone problems, one stale spec paragraph) and a few nits remain. None blocks release.

### Original items

**Must-fix 1 (focus falls to body): fixed.**
- Keyboard only, through all three modes at 1366x768: after every Enter or Space, focus was read at once and again 1 to 12 s later. It was never BODY.
- All in one went to Laptop. Back to desk went to All in one. Clear desk stayed on Clear desk.
- Try it went to the job card. Next job went to the new job card (Write a word). Start went to the first desk part (Camera); the wrong and right part taps kept focus on the part.
- The only body samples were Tab wrapping past the end of the page during the test's own Tab loops, not tool behavior.
- Tab order is unchanged: header, the seven tiles, Clear desk, All in one, then desk parts.
- Typing C A T on the real keyboard showed CAT.

**Should-fix 1 (box called the brain): fixed.**
- The box line and the no-box line now say the brain is inside the box, in src, spec and voice/lines.json.
- The voice log played them word for word.

**Should-fix 2 (round 7 showed parts working): fixed.**
- In round 7, a wrong keyboard tap wiggles the keyboard and teal dots run in to the box. They end in a gray "?" puff on the box.
- The screen stays off (`scr.kind` "off" in four samples over 1.2 s). Then "Nothing happened! This part needs the brain. Try another part." plays.
- Judgment: it reads right. The box's power light is gray, nothing lights up, and the puff sits at the box.
- The spec now describes this behavior.

**Should-fix 3 (graphics faint on wood): fixed in src, but the spec was not updated (see new should-fix 3).** Recomputed in Python (WCAG relative luminance):

| Graphic | wood #d9a86c | light wood #e7bf89 | wood gradient ends #e4b77f / #d4a265 | wall #e9eefb | paper #f4f6fd |
|---|---|---|---|---|---|
| ghost #454e6e | 3.80 | 4.76 | 4.43 / 3.57 | 7.04 | 7.57 |
| teal dots #08606a | 3.38 | 4.22 | 3.94 / 3.17 | 6.26 | 6.73 |
| orange stars #9a3209 | 3.45 | 4.31 | 4.01 / 3.23 | 6.38 | 6.86 |

- All are at least 3 against everything they sit on. They were 2.12, 2.30 and 2.41 on wood before.
- The ghost on its own #ffffff55 fill over wood is 5.0.
- The dashed ghosts are now clearly visible on the desk at 1366 and 680.

**Should-fix 4 (check badge covers the tile picture): fixed.** At 375x812 and 375x667 the check is a small corner badge, and every part picture stays visible.

**Should-fix 5 (Jobs shelf below the fold at 375x667): fixed, with a small trade-off.**
- Every tile, job card and Try it is inside the viewport. The page scrolls 4 px. Judgment: that is negligible.
- The header buttons become icon only. Motion, Sound and Read are 48x60.
- The trade-off: with a job picked, the stage drops to 178 px tall (k 0.26). Desk parts are about 20 to 30 px, and desk targets are 39 to 48 px wide (speakers 39). This is acceptable for a phone, which is not the K-1 classroom use. See nit 4.

**Should-fix 6 (tablet reads as a monitor): fixed.**
- The tablet is now a dark-bezel slab held by two cartoon hands at the bottom corners, with no stand. It reads as a tablet.
- All six tablet hotspot lines play.
- The mic now shows three holes, matching "These tiny holes".

**Should-fix 7 (no preview.svg): fixed.**
- preview.svg (21.6 KB) matches `__tool.previewSVG()` byte for byte, apart from the XML header and a trailing newline.
- It has no external references and no embedded images.
- It renders at 640x400 as a readable desk: box, screen showing "HI", keyboard glowing with teal dots, mouse, speakers, and ghosts for the mic and camera.

**Nice-to-haves and nits from the first pass:**
- **Nibbles size: fixed.** The image is 104 to 111 px at 680x425, 1366x768 and 375x812 (it was about 50 px at 680). The plug is readable at 680.
- **Replug: fixed.** After the found tap, Nibbles holds the plug. The plug arcs into the part's socket while the cable draws in, then one flow runs. With Motion off, a still dashed arrow points from Nibbles to the plug.
- **Drag removes only off the desk: fixed.** Jittered drags at 1366 and 680:
  - The box dragged 0.35 of the stage width sideways stayed on the desk.
  - The keyboard dragged along the desk stayed.
  - A 7 px drag counted as a tap.
  - The mouse dropped on the shelf was removed. The camera dropped on the wall was removed. One speaker dragged up removed both. The screen dropped below the desk's front edge was removed.
- **Backdrop crop: fixed.** With xMidYMin, the whole pegboard and its tools show at every size.
- **Laptop brain spot: moved to the middle of the deck. It works at 680 wide and up, but not at 375 wide** (new should-fix 1). At 1366 the open x-ray window covers the middle of the keyboard and the top half of the touchpad, and the touchpad spot sits on its lower border. Judgment: busy but readable; acceptable.
- **Tablet mic: fixed** (three holes).
- **notes.md standards label: fixed.** It now names E1-SYS-HW-11 as CSTA 2026, with 1A-CS-01/02/03 as the 2017 matches.
- **First tap on a part control skips the welcome: fixed.**
  - A first held tap on the speakers on the desk played only "La la la!", with no welcome ahead of it.
  - The skip also applies to a locked All in one (see nit 6).
- **Backdrop prompt wording: unchanged.** It still uses "No desk, no furniture...". The image is clean, so this only matters for a reroll.
- **Read after a cancel: unchanged.** With browser TTS, Read still sometimes ended only on its timeout: a Read of the box line started at 7.07 s and the waiting screen line started at 14.37 s, exactly 2500 + 80 x 60 ms. There are still no clips. Recheck once clips are recorded.

### Spec "Done when", rerun

- **1:** Each of the seven tiles was tapped with a held click.
  - Each part landed in its own slot (1366 frame), and each naming line is in the voice log in order.
  - With all seven placed, the all-built and All in one lines played. Tapping a tile again returned the part, and All in one locked again.
- **2:** With only the screen and keyboard, a keyboard tap gives the new no-box line. The screen stays off, and teal dots run to the loose plug with a "?" puff. After adding the box, taps type H, then HE, with dots sampled moving toward the box.
- **3:** The microphone with the box but no speakers plays "Everyone, say hello!", then the no-speakers line. "Hello, class!" never plays.
- **4:** All in one is locked until all seven parts are placed.
  - All seven laptop hotspots and all six tablet hotspots play their lines at 1366x768 and 680x425.
  - Back to desk returns all seven parts.
- **5:**
  - The cartoon with box and screen plays muted with the crossed speaker, then says "No sound!...". Only the two speaker ghosts pulse (`.ghost.pulse` count 2).
  - Adding the speakers and Try it gives the success line, then "Some parts got a rest. That's OK!" for the extra keyboard, which shows Zzz. Next job appears.
- **6:**
  - All six jobs were finished with held clicks. Six cards show a check.
  - "Six jobs done!" played once and not again on a redo of job 1.
  - The empty-desk line plays.
  - Picking another job mid-run stopped the run and cleared the desk.
- **7:**
  - All seven rounds play in spec order, each with its symptom line, "Which part", a wrong-tap line, Nibbles with the plug, the found line and the full job with its success line.
  - The plug marker counted 1 to 7 of 7.
  - After round 7: the all-fixed line, then Start began round 1 again (1 of 7, speakers).
- **8:** Held clicks throughout.
  - A first tap on a tile names the part with no welcome.
  - A first Read reads the hint and leaves the welcome unsaid.
  - Read during a line cut it and re-read it, and a line queued during Read waited for it.
  - A mode switch dropped the queue, then played the Jobs welcome.
  - With Sound off, the hint still updated and nothing was queued. Sound back on in Missing played the Missing welcome once. Returning to Build played the never-said Build welcome.
  - No line played twice or was cut off by a queued line.
- **9:** Keyboard only reaches and runs every control in all three modes (see must-fix 1).
  - Motion off:
    - Parts appear with no fly copies.
    - Cables show a still arrow instead of moving dots.
    - The blanket fades.
    - Nibbles stands still at the center.
    - The replug uses a still arrow.
  - Timing is unchanged in Missing round 1 (Start to ask 10.41 s with Motion on, 10.51 s off; found to solved 14.09 s on, 14.11 s off).
- **10:**
  - No scroll at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 1366x657, 1280x600 or 375x812, in Build (empty and full), Jobs (running and success) and Missing (idle and ask). No horizontal scroll anywhere.
  - At 375x667 the page scrolls 4 px in Jobs and fits everywhere else.
  - The smallest scene text (Zzz) is 14 px at 680x425 and 760x900. The preview caption is 13 px.
- **Console:** clean in every run. The only entry was a favicon.ico 404 from the test server. Network requests were the page and data: images only.
- **Lines:** `allLines()` returns 69 lines and equals voice/lines.json in order. Both equal the spec voice list. There are no duplicates, no em dashes and none over 200 characters.
- **Art:** all six real images are in place and read well at every size.

### New findings

1. **Should fix: at 375 wide, the laptop's brain spot can't be tapped at its center.**
   - Evidence: at 375x667 and 375x812, the touchpad spot (70 px, y 380 to 450 at 375x667) covers the lower 38 px of the brain spot (y 348 to 418). `elementFromPoint` at the brain spot's center returns Touchpad.
   - A real held click on the brain spot played "This touchpad is the mouse..." and lit the touchpad.
   - Only the top strip of the brain spot is reachable.
   - At 680x425 the overlap is 13 px, and the center still hits the brain. 800 wide and up are fine.
   - Cause: the brain spot moved down to the middle of the deck (465, 444), only 59 design units above the touchpad (465, 503). The spot stays 64 px while k shrinks to about 0.4.
   - Fix: move the brain spot up (for example y 420) or lay the two out side by side when k is small.

2. **Should fix: after Try it, keyboard focus stays on the job card, so a second Enter re-picks the job and clears the desk.**
   - Evidence: Jobs, Write a word, box and screen on the desk, focus on Try it, Enter. Focus moved to the job card as claimed. It stayed there after the run ended at 1.5 s and was still there at 5.5 s. A second Enter (the natural "try it again") called pickJob, and the desk emptied.
   - The code means to hand focus back. rescueFocus keeps `rescued = Try it` for that. But tryIt calls `render()` before `sync()`. render's rescueFocus runs while Try it is still disabled, so `live(rescued)` is false and `rescued` is cleared before sync re-enables Try it.
   - Fix: re-enable Try it before render, or have the post-run sync() return focus to Try it when the job card holds it.

3. **Should fix: the spec's Look paragraph still lists the old scene colors and has no wood ratios.**
   - Evidence: spec.md lines 130 to 135 still say in dots #0e7c86, out stars #c2410c and ghost #6b7594, with contrast stated against the wall and paper only. src now uses #08606a, #9a3209 and #454e6e.
   - The first verify asked for the wood ratios to be recorded.
   - Fix: update the colors and add the ratios from the table above.

4. **Nit: 375x667 Jobs fits by shrinking the desk to a thumbnail.**
   - Desk parts are about 20 to 30 px. Desk targets are 39 to 48 px wide, and the header buttons are 48 px wide, against the 60 px K-2 rule.
   - This is acceptable as a phone fallback (the earlier deviation for 375 wide).

5. **Nit: browser-window laptop sizes use the compact layout.**
   - 1366x657 and 1280x600 (a laptop browser that is not full screen) fall under the compact rule (side layout under 700 px tall).
   - There the laptop and tablet spots are 50 to 51 px, and some desk targets are 48 to 58 px (mouse 49x68 at 1366x657, keyboard 255x54 at 1280x600).
   - Tiles and panel buttons stay large, and nothing scrolls. The 48 px exception was accepted for the 16:10 preview; these sizes are real classroom windows, so consider a threshold nearer 560 px, or keep 60 px spots when k is about 0.85 or more.

6. **Nit: a first tap on the locked All in one loses the Build welcome.**
   - `aio` is in the first-tap skip list, but a locked button does nothing.
   - Evidence: a held click on locked All in one as the first tap gave an empty voice log, and the welcome is held until the next mode entry or Sound on.
   - Fix: skip only when the button is enabled.

7. **Nit: the hint keeps "Tap All in one!" after a part is removed.**
   - The button locks again, but the caption still invites the tap, and Read would say it.
   - Seen at 1366 after removing the screen from a full desk.

8. **Nit: the pop-up keyboard highlight is misaligned on the tablet.**
   - The yellow highlight ring frames the lower two key rows. The top row of the popped keyboard sits above the ring and runs under the bezel edge.
   - Seen at 1366, in the frame after the "Keyboard on the screen" spot.
