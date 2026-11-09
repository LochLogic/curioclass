PASS (exit re-check 2026-11-06, after Codex round 2: Done when 7 met with the GPU on; see last section)
Counts: blockers 1 (general 0, family 1), should fix 11 (general 8, family 3), polish accepted 14

# Refine: sky-dome

Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md`. No sensitivity file (none needed, see Settled
calls). Lens frames live under `S:/CurioClass-codex-scratch/sky-dome/` (`teaching/`, `play/`, `craft/`, `audit-r1/`).
Integrator spot-checks (code read of src.html): the stretched projection (819-827, 1180-1181), the late hint (540-552),
the Sydney message (1291-1294) and Escape (1397-1398) are all as the lenses describe. The astronomy itself checked out
against JPL Horizons, SIMBAD and USNO (Teaching lens): do not touch the position, rise/set or phase math.

## Blocker
1. **The dome stretches the sky, so star patterns are the wrong shape and change shape as they turn.** `src.html:819-827`
   (`projectVector`, and `fromScreen` just below) scales x by `rx` and y by `ry`, which `resize` (`src.html:1180-1181`)
   sets separately from width and height. At 1366x768 rx 621 and ry 233: 1 degree is 24.8 px across and 9.3 px down
   at every zoom, about 2.7 to 1; at 680x425 about 4.6 to 1. Orion is a flat smear (Betelgeuse to Rigel 393 px across,
   92 px down) and the Big Dipper is a long ladle at 22:00 and a tall one at 04:00, so spec Things to do 13 ("the same
   stars, turned") and the first reaction show distortion first. A planetarium whose patterns are wrong is a readout
   that lies; the Manual's "oval viewport" note does not cover it. Seen: `craft/orion-1366-fov50.png`,
   `play/f1/dipper-a.png` beside `play/f1/dipper-b.png`, every `audit-r1/size-*.png`. Fixed: one scale for both axes
   (min of rx, ry, or a true equal-scale view that fills the stage when zoomed in); the 180 degree dome and its brass
   horizon ring are round, with the spare width going to readouts or deck. `fromScreen`, tap hit-testing, labels,
   trails and the ring all use the same scale. Re-shoot Orion at FOV 50 and the Dipper pair. (family:curiosity)

## Should fix
1. **No constellation is named anywhere.** `src.html:953` draws `figure.slice(1)` only; each figure's name
   (`DATA.figures[i][0]`) is bundled but never shown, and the object card has no constellation row. Spec Things to do 4
   (the Sun's constellation), 7 (the Southern Cross: Acrux and Mimosa labelled, nothing says Crux), 12 (Thuban "in
   Draco") and 13 (the Big Dipper) cannot be answered alone; with Lines on the dome shows 88 nameless figures. Seen:
   `teaching/out/noon-daylight-off-lines.png`, `play/f1/noon-nodaylight.png`, `audit-r1/state-running-1366x768.png`,
   `audit-r1/state-southern-sky-1366x768.png`. Fixed: a CONST row on the star, Sun, Moon and planet card, and faint
   figure names drawn while Lines (and Names) are on, placed so they do not crowd star labels. Real material, no game.
   (family:curiosity)
2. **60 fps fails on a Chromebook-class CPU (Done when 7).** `draw()` `src.html:926-951` sets `globalAlpha`,
   `fillStyle` and a separate arc path for each of about 4,600 stars, and every frame runs `querySelectorAll` and
   `getComputedStyle` for label boxes (983-986). Measured at 1366x768, Play 1 h/s, all on: 1x 7.0 ms median, 2x
   20.8 ms (48 fps), 4x throttle 34.7 ms (29 fps); stars alone cost 23.8 ms per draw at 4x (Craft lens, `perf.py`,
   `prof.py`). Fixed: batch stars by colour and alpha bucket into a few paths, or render the star field to an offscreen
   canvas per sidereal step and blit it; read overlay rects and the mono font once on resize. Target 4x throttle
   median at or under 16.7 ms. (general)
3. **The zoom buttons hide the W on the horizon ring.** `.view-tools` `src.html:52` (desktop), `:179` and `:195`
   (narrow) sit over the ring's west marker at the default whole-dome view at 1366x768, 1280x720, 1920x1080, 680x425
   and on the phone. West is where every star the student watches sets. Seen: `craft/w-marker-crop.png`,
   `audit-r1/size-1366x768.png`, `play/crop-phonedome.png`. Fixed: view tools clear of the ring (deck, or outside the
   round dome once Blocker 1 lands); all four letters visible at every checked size. (general)
4. **The spoken hint plays after the student already acted, with the on-screen hint gone.** Capture listener
   `src.html:546-552` queues "Drag the time dial." on the first pointerdown or keydown, and `act()` (540-541) hides
   the on-screen hint on the same gesture. A student who drags the dial or presses Play hears an instruction for what
   they just did; one who taps a lever hears it with no hint on screen. Seen: audit held-click rows 0 to 14, 16 and 18;
   `play/f5/drag-dial.png`; Craft `voice.py` V1 (hint already hidden when the line started at 1.52 s), V8, V9. Fixed:
   say nothing when the first gesture is the time dial, date wheel, Play or the play knob (the time is already
   moving); for any other first gesture, speak the line and keep the on-screen hint visible until the line ends or the
   student moves time, whichever is first. Read and Sound stay as they are (Craft's voice table is right there).
   (family:curiosity)
5. **The Sun has no distance.** Sun card `src.html:1118-1128`: MAG -26.74 but no DIST, while planets show au and the
   Moon km. The 5-ESS1-1 comparison (Sun 1 au, about 8.3 light minutes, against Sirius 8.6 ly) cannot be read off the
   instrument. Seen: `teaching/calc2-out.json` `sunCard`. Fixed: a DIST row on the Sun card in au to three decimals
   plus light minutes. (general)
6. **The Manual leaves out seasons and the Sun's path.** Spec Manual contents (`spec.md` "The Manual") list "seasons
   and the Sun's path"; "Why it changes" (`src.html:336-341`) covers the daily spin, the yearly star drift, phases and
   loops but never says Earth's tilt makes the Sun's path higher and longer in summer, which is what DAYLIGHT shows
   (1-ESS1-2, MS-ESS1-1). Seen: Manual read in full, `audit-r1/state-manual-1366x768.png`. Fixed: a short plain
   paragraph on tilt, the Sun's path and daylight, plus a "Things people have found" entry using the instrument's own
   checked numbers (Denver about 15 h on June 21 and about 9 h 21 min on December 21, USNO), sourced.
   (family:curiosity)
7. **Date and time wheel engravings cannot be read and fail AA.** `wheelControl` `src.html:1257-1258`: `font-size="5"`
   in a 100-unit viewBox (about 5 px), `#e1c68d` on a gold band, about 1.9 to 1. The month and hour marks are the
   instrument's scale. Seen: `craft/wheels-crop.png`. Fixed: dark engraving `#2a1f10` (the spec palette) at 8 px or
   more on the gold, or the marks on the dark inner ring, at 4.5 to 1 or better. (general)
8. **Read speaks clock time as a duration: "20 hours 22 minutes".** `speakText` `src.html:520`. On a grade 1
   projector that is heard as an amount of time. Seen: audit row 18; Craft voice check ("20 hours 37 minutes"). Fixed:
   spoken as a time of day, for example "8:22 in the evening" (midnight and noon said as such); the on-screen readout
   stays 24-hour. (general)
9. **Long star labels run over neighbours and put the wrong name on the Southern Cross.** Label placement
   `src.html:997-1005` tries right then left with no leader. Over Sydney (2026-05-01 20:04) "Rigil Kentaurus" runs
   right across Crux, "Toliman" is labelled separately at the same point, and Acrux and Hadar get no label; a star dot
   sits on the P of "Pollux". Seen: `play/f3/sydney-sky.png`, `play/crop-cross.png`, `play/crop-rollux.png`. Fixed: a
   label box may not cover another drawn star brighter than about mag 2.5 or another label; a short tick joins a
   label that sits off its star; a close pair (Rigil Kentaurus and Toliman) is labelled once. Acrux gets its label
   over Sydney. (general)
10. **Typing "Sydney" says the place is not bundled.** `$("city").onchange` `src.html:1291-1294`: a name that matches
    two places (Sydney, Australia and Canada) falls through to "Place not in bundled selection. Enter latitude and
    longitude." and marks the field invalid. That message is false. Seen: `play/f3` shot "sydney"; Craft `read.py`.
    Fixed: "Two places match. Choose Sydney · Australia or Sydney · Canada." with the list offered, field not marked
    invalid. (general)
11. **Escape anywhere throws focus to the sky.** `src.html:1397-1398`: with no Place sheet open, Escape clicks
    `close-object`, which runs `act()` and `canvas.focus()` even with no readout open, so Escape in the place search or
    on a lever moves focus and hides the hint. Seen: Craft `kb.py` (focus after Escape in `#city` and on `#lines` =
    `sky`). Fixed: Escape closes the readout only when `#object` is open; inside inputs it does nothing beyond the
    input's own behaviour. (general)

## Polish accepted
1. **Manual in plain words first.** `src.html:298-356`, 352-442: "precessed to the chosen date", "proleptic Gregorian",
   "truncated periodic expansion", "local mean solar time (longitude divided by 15)". Plain sentences first, each term
   glossed once; the dataset audit trail (vertex counts, place corrections) moves into a collapsed "Sources and
   checks" `details` beside the licence terms. Nothing removed. (family:curiosity)
2. **Distances shown one way.** `src.html:1123` rounds to whole ly: Sirius "9 ly" on the card, 8.6 in the Manual;
   Alpha Centauri 4 for 4.3. Show one decimal under 20 ly so the card matches the Manual. Seen:
   `teaching/calc2-out.json` `card`. (general)
3. **The classic bright-but-far stars get distances.** Rigel, Deneb, Canopus and Antares show no distance, so Things
   to do 11 has only Betelgeuse as a far, bright star. Add the ones with a NASA or ESA fact page, confirmed against a
   second source, marked ≈ where uncertain; skip any that cannot be confirmed. (general)
4. **Year window shows the BC year.** `#year` `src.html:252-254` shows "-2799" large with "2800 BC" small; typing
   -2800 gives 2801 BC. The window shows the plain year with an era flag (BC or AD) the student can switch, and typing
   "2800 BC" works; astronomical numbering stays in the Manual. Seen: `audit-r1/state-ancient-pole-1366x768.png`.
   (general)
5. **Sun, Moon and planet names stay in daylight.** `src.html:993` drops every label when `day >= .85`. Keep star
   names fading; keep Sun, Moon and visible planet labels. Seen: `play/f5/drag-dial.png`, `play/f1/noon-daylight.png`.
   (general)
6. **Phone plate on one line, rivets clear.** `.plate` `src.html:172` with `::before/::after` at 98-99: at 375 wide it
   wraps ("Sky / Dome") and the dots touch "Curio" and "Dome" (also at 680x425 and 800x500). Smaller size or tighter
   spacing on one line, padding clear of the rivets. Seen: `play/crop-plate.png`. (family:curiosity)
7. **Phone dome toward the spec's 60 percent, readouts kept.** `src.html:1180-1181` (`top=112`), `#hint` `:182`: the
   dome is about 220 px tall at 375x667, the hint sits on the Capella labels, and Sun and Moon rise and set are dropped.
   Grow the dome toward 60 percent of the height at 375x812, keep rise and set reachable (the two-row strip or the
   card), and place the hint off the star labels. Seen: `play/f4/phone-default-tall.png`. (general)
8. **Live-region words use visible names.** `src.html:1286, 1299` announce "milky off", "lat 39.7 degrees". Use the
   lever's visible name ("Milky Way off") and "Latitude 39.7 degrees north". (general)
9. **Play knob and reverse switch in the brass grammar.** The play knob is a native `<select>` (`src.html:248`) and the
   reverse switch shows only "↶". Spec asks for a knob with detents: draw it as one (keeping its keyboard and announced
   value), and engrave REV beside the switch. (family:curiosity)
10. **Deep-sky hint only when a range shows.** `src.html:1136` always says "Magnitude range reflects the two source
    estimates." (M31 shows one value). Add that sentence only when two values are shown. (general)
11. **"DIST not verified" reads as doubt.** `src.html:1123`: say "no checked value" instead. (general)
12. **Compass letters at the poles.** From either pole every direction is south or north. Add one Manual line saying
    so (Things to do 6 sends students there). Seen: `audit-r1/state-southern-sky-1366x768.png`. (general)
13. **Time dial focus ring overlaps its label.** The 3 px outline runs over "TIME · 24 HOURS". Seen:
    `play/f1/keys-time.png`. (general)
14. **Ring through "AGE" at 680x425.** The brass ring crosses "AGE 26.5 d" (`craft/680-top-right-crop.png`); check
    again after Blocker 1 and clear it if it remains. (general)

## Settled calls
- **The six audit leads ("hint out of view: Drag the time dial.") are wrong leads.** All three lenses agree: a
  Curiosity's hint is gone after the first action. Do not bring the on-screen hint back after an action.
- **Hint timing (Should fix 4).** Play wanted silence after any instrument control; Craft wanted silence only after the
  dial or Play, with the visual hint held while the line plays. Settled toward Craft plus the date wheel and play knob:
  the line is spoken once and only while it is true on screen. No second hint, no extra lines.
- **Read's clock phrasing is a should fix, not polish** (Teaching should fix, Play polish): grade 1 hears this on a
  projector, and a time heard as a duration misleads.
- **"Sydney" is a should fix, not polish** (Play should fix, Craft polish): the message states something false.
- **Hint tag:** family:curiosity (Play), not general (Craft), because the browser needs a gesture before speech, so
  every Curiosity's once-spoken hint meets this.
- **Fixes add real material only.** Constellation names, the Sun's distance and the seasons paragraph are readouts and
  Manual text; none becomes a task, target or checklist (CODEX-CURIOSITY, BASELINE rule 2 read with the Curiosity
  shape).
- **Keep:** the astronomy and its tolerances, Motion off stepping, Same time each night, the Read voice table, the
  Manual's honesty notes (moved, not cut), no network requests, no sky stories.
- **No sensitivity review needed.** No cultural sky stories; star names are IAU identifiers with no origin claims. If
  sky stories are added later, they need one (rule 5).
- **Note for the integrator, not for Codex:** the Craft lens ran `python scripts/check_tools.py --help`, which has no
  help flag and rebundled about 80 non-draft tools' git-ignored `tools/<id>/<id>.html` from their current src.html. No
  tracked file was written; sky-dome was skipped. Matters only if a runner compares bundle timestamps.

## To the spec's open questions
- **Drop science-9-stars-and-the-big-bang from "Also reaches"?** Its codes (HS-ESS1-1, -2, -3: the Sun's life span and
  fusion, Big Bang evidence, nucleosynthesis) are not taught by anything in the instrument; it shows positions,
  magnitude, B-V and temperature. BASELINE rule 2 says remove it and make sure another tool teaches it. Teaching lens
  recommends dropping it (`spec.md` Map, and wherever the module map row is written).
- **science-5-sun-stars-and-shadows: add a SHADOW readout or call the reach partial?** Day, night and seasonal stars are
  taught; shadow length and direction are not. A SHADOW row on the Sun card (a 1 m stick's shadow length and
  direction from the Sun's ALT and AZ) would cover it; otherwise the reach is partial and rule 2 applies.
- **The default view and the "faint ground silhouette".** At the whole-dome view looking straight up the horizon is
  the rim, so the spec's first-view ground silhouette never shows (`audit-r1/size-1366x768.png`). Either the opening
  view tilts toward the horizon or the spec line changes to the brass ring alone.

## Not taken
- Dropping the compass letters at the poles: the one-line Manual note (Polish 12) is enough and keeps the ring stable.
- A rolling odometer drawing for the year: the era fix (Polish 4) solves what the student misreads; a full odometer
  animation is optional decoration.
- Typing "2800 BC" being mandatory to reach Thuban: covered by Polish 4; no separate change.

## Exit check (2026-11-06)

Cold exit check by Claude on the current bundle (`sky-dome.html`, 584,934 bytes, not rebundled). Frames and logs in
`S:/CurioClass-codex-scratch/sky-dome/exit/` (`audit-r2/`, `drive/`, `drive.log`, `perf.py`, `perf2.py`).

### Merged items

- **Blocker 1, stretched sky: fixed.** `resize` sets `rx=ry` (`src.html:1435`); `projectVector` and `fromScreen` share
  it. Orion at FOV 50 (21:00 Denver, 2026-01-14) has its true shape: Betelgeuse to Rigel 158 px across, 99 px down
  (was 393 by 92). The ring is round in every `audit-r2/size-*.png`. Note: the re-shoot landed at
  `craft/orion-1366-fov50.png` (my helper's output path was wrong), so the Craft lens's original frame there was
  overwritten by the fixed one; the original is still beside Codex's `fix-before-orion/`.
- **Should fix 1, constellation names: fixed.** CONST row on the Sun card (Taurus, June 21) and star cards; faint
  figure names with Lines and Names on (Orion, Canis Minor, Monoceros; Crux and Centaurus over Sydney).
- **Should fix 2, 60 fps on a Chromebook profile: open.** Re-measured at 1366x768, Play 1 h/s, 21:00 Denver (night, so
  the star field is drawn): 1x throttle holds 16.7 ms frames; 4x throttle with Lines, Names, Ground, Milky Way and
  Trails on gives draw 18.6 ms median (27.3 p95) and frame interval 66.7 ms median (15 fps); with those off, draw
  14.8 ms but frames still 50 ms (20 fps). The rAF interval is well above the draw time, so work outside `draw()`
  (readouts, label layout, time step) also costs per frame. A daytime measure looks fine only because stars are not
  drawn; measure at night. Codex's own account agrees this is open.
- **Should fix 3, zoom buttons over W: fixed.** Zoom sits below the round ring; N, E, S, W clear at 1366x768
  (`drive/default-1366.png`) and every audit size.
- **Should fix 4, late spoken hint: fixed.** Held clicks on the time dial, date wheel, Play and rate knob speak nothing
  (audit rows 3, 4, 6, 9). A first Lines click speaks "Drag the time dial." with the on-screen hint still shown
  (`drive.log` first-lines-hint: hidden false). Observation, not open: Year era and Now also move time yet speak the
  line once (rows 5, 7); a quick second tap cuts it. Within the settled call ("whichever is first"), left as is.
- **Should fix 5, Sun distance: fixed.** "DIST 1.016 au · 8.5 light min" on June 21 (`drive.log` sun-card).
- **Should fix 6, seasons in the Manual: fixed.** Tilt paragraph (`src.html:402-403`) and the Denver "A longer Sun
  path" entry (`:410`).
- **Should fix 7, wheel engravings: fixed.** Dark `#2a1f10` marks at 9 units with a gold halo (`src.html:1530`);
  legible on `drive/default-1366.png` and the 375 frames.
- **Should fix 8, Read clock phrasing: fixed.** "January 14, 2026. 8:22 in the evening. Denver. ..." (`drive.log`
  read-clock); audit row 20 "10:16 in the morning".
- **Should fix 9, colliding star labels: fixed.** Sydney 2026-05-01 20:04: Acrux, Hadar, Mimosa, Gacrux labelled; one
  "Rigil Kentaurus / Toliman" label (`audit-r2/state-sydney-lines-1366x768.png`).
- **Should fix 10, Sydney message: fixed.** Typing "Sydney" offers "Sydney · Australia" and "Sydney · Canada",
  announces "Two places match. Choose ...", aria-invalid unset.
- **Should fix 11, Escape focus: fixed.** Escape in `#city` leaves focus in `#city` (`src.html:1684-1688`).
- **Polish (spot-checked in bulk): fixed as described.** Seen: plain Manual with "Sources and checks" collapsed,
  AD/BC era button, daylight body names (Sun, Venus, Mercury, Moon, Mars, Jupiter at 10:22), one-line plate with clear
  rivets at 375, phone rise and set rows kept, REV engraved, brass rate knob, polar compass line in the Manual. Canopus
  and Deneb distances left out under Polish 3's skip allowance.

Fixed: 11 of 12 (blocker 1 of 1, should fix 10 of 11). Polish: 14 of 14 addressed.

### Regressions

None found. Default screen, the nine audit states at eight sizes, Motion off, the resize stress and the held-click walk
are clean: no exceptions, no console errors or warnings, nothing left disabled, no control moved more than 12 px. The
Sydney frame with Lines and Names on is dense but readable.

### Gate

1. Every Done when: **no.** Done when 7 (60 fps on a school Chromebook profile) fails at 4x throttle, see Should fix 2.
   The rest hold as checked by the lenses and the fixes (astronomy math unchanged).
2. Codes taught or moved: unchanged from round 1; the two spec open questions (science-9 reach, SHADOW readout) are
   still for the integrator, not a fix item.
3. Solo defaults work: yes (opens on tonight's sky over the home city, one quiet hint, no welcome).
4. Sensitivity: not needed (no sky stories), per Settled calls.
5. No blocker or should-fix open: **no**, Should fix 2.
6. Bundle clean: yes. 585 KB, under 2 MB; zero console errors; the only requests are the tool file itself.
7. Voice counts: right. `voice/lines.json` holds the one line "Drag the time dial."; Read is dynamic; the calm-professor
   recording is still absent (browser fallback), a recording item, not a count error.

## Audit pilot

- Leads: 10, all "hint out of view: Drag the time dial." across the nine states plus two quick-tap "how line cut"
  rows (Year era, Now). All are wrong leads under the settled Curiosity hint call; none confirmed.
- Useful rows: held-click table (silent dial, wheel, Play, knob; Read phrasing) and the clean stress, Motion off and
  size rows were enough to confirm Should fix 4 and 8 and the regressions sweep.
- Missed: performance. The audit has no frame-rate row, and a daytime run would hide the star-field cost anyway;
  Should fix 2 needed a separate throttled night measure. It also reports no network row directly (checked by hand).

## Exit re-check (2026-11-06, Claude integrator, after Codex round 2)
The one open item was should fix 2 / Done when 7 (60 fps, 1366x768, night, all stars and lines on, 4x CPU throttle).
Codex's round 2 numbers (frame interval median 45 ms) came from scripts/drive.py, which starts Chrome with
--disable-gpu, so WebGL ran on the Microsoft Basic Render Driver (software). A school Chromebook draws WebGL on its GPU.
Same scene and script (Codex's r2-precision-shots final-night), run twice in this session:
- GPU off (Microsoft Basic Render Driver): 4x draw median 6.7 / p95 8.5 ms, frame interval median 28.9 / p95 35.8 ms.
- GPU on (ANGLE D3D11): 4x draw median 5.6 / p95 8.6 ms, frame interval median 7.4 / p95 10.7 ms; 1x interval 7.0 ms.
The CPU-side draw fits the 16.7 ms frame with room to spare at 4x, and with a GPU the frame interval is well under it.
This PC's GPU is far stronger than a Chromebook's, so the GPU number is an upper bound; the CPU-side draw at 4x is the
honest Chromebook reading and it passes. Verdict: Done when 7 met. No other item was open; Codex's round 2 polish.md
records the regression checks. Evidence: the Claude session scratchpad skygpu folder (soft-* and gpu-* json).
Lesson for later checks: WebGL tools must be timed with the GPU on, or the gate reads the software rasteriser.
