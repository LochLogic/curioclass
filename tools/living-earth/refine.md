PASS (exit check 2026-11-06)
Counts: blockers 1 (general 0, family 1), should fix 11 (general 7, family 4), polish accepted 19

# Refine: living-earth

Merged from `refine/teaching.md`, `refine/play.md` and `refine/craft.md` (no sensitivity file; all three lenses found
nothing cultural, Native or hard-history, and disasters appear as data only). Frames: teaching
`S:/CurioClass-codex-scratch/living-earth/teaching/out/`, play `S:/CurioClass-codex-scratch/living-earth/play/`
(r1 to r4), craft `S:/CurioClass-codex-scratch/living-earth/craft/f1/`, shared audit
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`. Integrator spot-checked src.html:1660-1669 (plateMotion),
974-985 (renderSection), 1001 and 1944-1948 (station markers), 1318 (key handler) and 745-746 (touch): each lead holds.

The short test passes in every lens (play runs 1970 to 2025 in 18.7 s, the slices show the slabs, no score or finish
anywhere). Ten quakes and the ComCat totals check out (teaching: 14 events by id, 26,230 events, 44 M8+). Do not undo
any of that while fixing.

## Blocker
1. **Pin SPEED and the Arrows layer show the model's reference-frame drift, not how fast the plate moves.**
   src.html:1660-1669 (`plateMotion`), Pin readout 1695-1696, Read text 1175, Arrows 1797-1806. Speed and heading come
   from Merdith et al. 2021's 0-5 Ma rotation relative to plate 000 (its absolute, palaeomagnetic frame), which carries
   a large rotation shared by every plate. Against ITRF2014 GPS poles (teaching, recomputed in Python): Denver reads
   6.2 cm/yr at 253 deg (GPS 1.6 at 247), Sydney 2.8 at 325 (GPS 5.7 at 19), Perth 4.5 at 356 (6.9 at 34), Cairo 5.5
   at 12 (2.9 at 53), Honolulu 9.3 at 264 (7.1 at 299). Australia, the fastest continent, reads slower than North
   America and in the wrong direction; Arrows show most plates drifting the same way, which hides "two plates heading
   at each other" (spec Things to do 10, 11). Seen: teaching numbers.json, nums2.json, rot.json; pin-sydney.png,
   atlantic-all.png; play r1/pin-denver, pin-hawaii. Fixed looks like: keep Merdith for Rewind; for present-day
   motion, remove the shared rotation (a no-net-rotation frame built from the model's own plates, area-weighted) and
   add the motion relative to the plate across the nearest edge ("opening 2.5 cm/yr" or "closing 6 cm/yr" beside
   EDGE). Check the result against the ITRF2014 table above (within about 1 cm/yr and 20 deg is a pass), redraw the
   Arrows from the same numbers, and re-check the fingernail field note against what the readout now shows. If the
   Merdith rotations cannot give that, leave SPEED as relative-across-edge only and note it in notes.md; switching to
   another plate motion model is a spec question (below). (family:curiosity)

## Should fix
1. **Stations: a drag on the trace can never set the S marker.** src.html:1001 creates each station with `p:0,s:0`;
   1944-1948 picks the nearer marker, so a press at the S packet always moves P (play: press at S 990.8 s on Sumatra
   2004 left P 997.5, S 0, "S−P -997.5 s"; r2/st-drag-S-first.png, r2/st-drag-S-afterP.png). Only Shift-drag (no
   Shift on a phone) or the small sliders reach S. Fixed: start S at the right end of the trace (or hide each marker
   until placed) and give each marker its own grab handle, so a press near either packet moves the right one. Also
   separates the P and S labels that overlap at 0 as an "8" (craft zoom-trace.png). (family:curiosity)
2. **The first-run line is spoken after the action it asks for.** src.html:745-746 `touch()` speaks "Drag to spin.
   Press play." on any first action: after Play it says "Press play" while the archive runs, after a drag it says
   "Drag to spin", after a tool tab it says "Drag to spin" where a drag now draws a slice line; the on-screen hint is
   hidden at the same moment. Seen: play r3 voice logs (v-first-play, v-first-slice, v-first-drag), craft v-play5,
   v-drag-first, audit one-click rows 0 to 13. Fixed: speak only the half not yet done ("Press play." after a drag,
   "Drag to spin." after Play), and nothing once a tool panel is open; give the line a `valid` check. (family:curiosity)
3. **Slice draws the sea floor below the shallow quakes.** src.html:974-985: quake depths are 1:1 but the ETOPO
   profile is multiplied by 20 on the same axis, so a 4 to 5 km sea floor sits at 80 to 100 km and every Mid-Atlantic
   quake (10 to 20 km) floats above it, the opposite of the lesson. Seen: teaching slice-mar.png, slice-japan.png,
   slice-peru.png. Fixed: draw the exaggerated profile in its own strip above the 0 km line (or exaggerate only above
   a sea-level baseline) and label "sea level" and "sea floor"; keep the x20 note. (family:curiosity)
4. **Wave shows three different shadow edges and an unreachable S arrival.** src.html:735-742 (`arrival`), 1096
   (shadow arc), 1104-1106, 936 (globe ring at 104 deg), Manual line 580. The iasp91 table has direct P to 98 deg and
   direct S to 99 deg, so from 99 to 104 deg the readout says "P NO BRANCH · S NO BRANCH" while the receiver sits
   outside the drawn S SHADOW arc; S at 98 to 99 deg arrives at 25:06 to 25:14, past the 25:00 end of the fader and the
   trace. Seen: teaching nums2.json, wave-100.png. Fixed: draw the arc and ring from the table's real edges (about 99
   deg for direct S, 98 to 140 deg for direct P), replace "NO BRANCH" with "no direct wave here", say in the Manual
   that waves bend round the core there (diffracted waves, not drawn), and run the window to 26 min. (family:curiosity)
5. **Stations words do not follow the state.** Panel line src.html:475 keeps "Tap three stations" after three are
   placed, struck and solved; the readout shows "FIT AMBIGUOUS" before anything is measured; Circles with unset
   markers reads "DIST 0 km" and draws zero circles; every revealed quake at the default year is tagged "OUTSIDE
   FILTERS"; under 200 km the label becomes "CATALOG / FIT", a threshold verdict close to Done-when 10's "never a
   rating" (src.html:930, 1846). Seen: play r2/st-solved.png, audit state-stations-1366x768.png. Fixed: one short
   instrument-status line that follows the state ("Tap three places for stations", "Strike to record a quake", "Set
   P and S on each trace", "Circles", "Reveal"), "SET P AND S" until both markers have moved, no FIT text at all,
   the marker labelled "CATALOG" with the offset in km beside it, and no OUTSIDE FILTERS tag on a Reveal (or move the
   year to the event, as the catalogue list does). This is a status line, not numbered steps or progress. (general)
6. **The Manual and panel captions are written for a geophysicist.** Manual src.html:550-664; captions 459, 475, 490,
   499, 507; readouts "NO BRANCH", "UNRESOLVED MODEL AREA", "QUAKES HELD", "FIT AMBIGUOUS". Examples: "finite rotations
   are resolved through the published plate circuit relative to plate 000 ... quaternion interpolation", "normalized
   three-plane fit", "schematic older fossil evidence · modern overlays withheld", "Pn and far-side PKP/PKIKP". Grade
   band 4 to 12, anchor grade 6, solo at home (rule 4). Fixed: each Manual section opens with one or two plain
   sentences at about grade 6 (what to do, what you will see: "Each dot is a real earthquake. Bigger dot, bigger
   quake. Colour shows how deep it was."), with the precise honesty notes kept below a "For the curious" line; one
   plain sentence on S-P beside the markers; captions in plain words ("rays bend through a model Earth");
   "UNRESOLVED MODEL AREA" becomes "plate not known here". "Things people have found" becomes short findings, with
   its two opening paragraphs of instructions moved into the how-to sections. (general)
7. **The selected-quake record card covers the globe when a tool is open.** With a panel open the globe moves left
   (`x = w*0.29`, about src.html:886) and the card at x 25 to 250 covers its west limb: station B and the Reveal marker
   run under it (only the "G" of CATALOG shows). Same at 680x425 and 800x500 with no tool. Seen: play r2/st-solved.png,
   audit state-stations-1366x768.png, state-selected-680x425.png. Fixed: dock the record inside the open tool panel, or
   collapse it to one line while an instrument is open, keeping the globe clear. (general)
8. **Shortcut keys go dead after any button click.** src.html:1318 returns early whenever a BUTTON has focus, so after
   clicking Play, a layer, a tool tab or zoom, Q/V/P/F/A, [ ] and S do nothing, and Space presses the focused button
   (after clicking Volcanoes, Space toggles Volcanoes). Seen: reading the handler (integrator confirmed), craft
   k-space-body. Fixed: let the letter and bracket keys through on buttons; keep Space as Play unless the focused
   button is something else the student would expect Space to press, and say the rule in the Manual. (general)
9. **The Volcanoes layer halves the frame rate on a slow machine.** `drawGeography` draws 1,609 triangles as 1,609
   fill+stroke paths every frame; at 4x CPU throttle the median frame goes 16.7 ms (default) to 33 ms (+Volcanoes) to
   50 ms (all layers). Done-when 6 asks 60 fps on a Chromebook. Seen: craft throttle.py, throttle2.py. Fixed: one
   path for all triangles (one fill, one stroke), or a GL point layer like the quakes; re-measure. (general)
10. **The compact console loses its labels under about 1050 px wide.** At 680x425, 800x500 and 760x900 the depth
    faders read "≥ 0 km" and "≤ 700 km" with no DEPTH, "TIME 1970 SPEED 3 yr/s MAGNITUDE ≥ 5.5" runs as one line, the
    layer buttons show only Q V P F A, the section is about 40 px tall with "A" printed over "2009 km → B", the trace
    is about 50 px and its axis prints "20 25 min" as "2025 min". Seen: audit size-680x425.png,
    state-stations-680x425.png, craft f1/t-pin-760.png, play r2/preview-680-slice.png, preview-680-stations.png.
    Fixed: keep "DEPTH" (or "D ≥", "D ≤"), a gap or rule between fader readouts, layer names (short words, not
    letters), and give an open panel the globe's room at this size (or stack) so the section and trace are usable.
    (general)
11. **The Manual's 29 source links navigate the tool away.** No link has a target; on the site a tap on "USGS record"
    loses the instrument state. Seen: craft grep (0 of 29). Fixed: `target="_blank" rel="noopener"` on every
    external link. (general)

## Polish accepted
1. **Keep the slow turn during the first Play.** src.html:1344 (`!state.touched`) stops the globe on Play, so the
   first run shows only the West Pacific and the Atlantic seam in the spec's first reaction never appears (play
   r1/play-end.png). Keep turning until the student drags. (general)
2. **Wave: label the shadow only once the rays get there, and give the cutaway room.** The violet "S SHADOW" arc and
   readout show before Fire (audit state-wave-1366x768.png); the disc is about 135 to 140 px in a 390 px panel at
   1366x768 (play r1/wave-end.png, craft f1/t-wave.png) and the MANTLE and LIQUID OUTER CORE labels sit in the corners.
   Show the shadow arc and label after the S front reaches the core's far side, let the cutaway fill the panel height,
   and put the layer labels on the layers. (family:curiosity)
3. **Rewind on the Play pad.** Play is disabled in Rewind (play r1/rewind-200-atlantic.png); let it run 0 to 200 Ma (and
   back) at a steady pace, stepping in calm mode. (family:curiosity)
4. **Tap a station triangle to choose its trace.** Today the channel is only a select (play finding 9). Tapping A, B or
   C on the globe selects that trace; keep the select for keyboard. (family:curiosity)
5. **Motion arrows that can be read.** After Blocker 1: a few arrows per plate near its edges, drawn above the dots,
   not one small cyan arrow at the centroid under them (play r1/layers-hawaii.png). (general)
6. **Calm mode steps the wave.** Fire with Motion off jumps to 25:00 (src.html:1223); step it by the minute as year
   playback steps by years (POLISH, calm keeps time). (general)
7. **Read in plain speech.** "1974. 2252 earthquakes in the magnitude 5.5 and greater catalogue under these filters"
   becomes "1974. 2,252 earthquakes of magnitude 5.5 or more so far." (play r3 v-read-after-play). (general)
8. **An in-view quake count for Things to do 13.** QUAKES counts the whole sphere, so "compare the Pacific rim with the
   rest of the world" cannot be done. Add IN VIEW (quakes on the visible face of the globe) beside QUAKES, so a student
   can turn the Pacific to face them and then the Atlantic. (family:curiosity)
9. **A slim drum row in compact layouts.** The drum is hidden below 1050 px (CSS lines 280, 380); the spec keeps it at
   375 under the sheet. A 40 to 50 px row. (family:curiosity)
10. **Mipmaps on the relief texture.** src.html:1495 uses LINEAR with no mipmaps, so Tibet and the Andes shimmer as
    white grain at 1x (craft zoom-tibet.png, play r1/zoom6-tibet.png). `generateMipmap` with LINEAR_MIPMAP_LINEAR (the
    texture is power-of-two). (general)
11. **Station hardware for the speed knob and depth fader.** The spec names a speed knob with four detents and one
    two-handle depth fader; they ship as plain range sliders. Draw the knob with detents and join the two depth
    handles on one track, keeping keys and announced values. (family:curiosity)
12. **Readable type at 1366x768.** Layer names and survey labels 10 px, fader readouts and Read 11 px. Raise anything
    read while using a control to 12 to 13 px, with Read matching Manual. (general)
13. **Teacher notes: a content line and real home ideas.** notes.md gets one line that the M8+ catalog and Strike name
    real deadly events (2004 Sumatra, 2011 Tohoku, 2008 Sichuan, 2015 Nepal, 2023 Kahramanmaras) some students or
    families may have lived through (rule 8). Replace "Ask a family member what a map leaves out" and the paper-map
    string idea with ones doable tonight, such as "pin your town together and look up the last quake felt there".
    (general)

Nits accepted (cheap and clearly right):
14. On load the strip reads YEAR 1970, QUAKES 0, but moving the dial to 1970 gives 475 (src.html:677, 750, 1189). Make
    load and dial agree (start at the end of 1970, or show 0 until play and say so). (general)
15. Strike starts at a random event of the curated set instead of always Sumatra 2004 in a fixed order.
    (family:curiosity)
16. In Rewind, "QUAKES HELD" becomes "QUAKES OFF" (or the pair hides) and the depth legend hides. (general)
17. Station marker faders get a Shift jump (10 s) like every other fader. (general)
18. One Manual line: about 500 ComCat place names show "?" for a lost accent letter, as ComCat itself does.
    (general)
19. The trace axis keeps "20" and "25 min" apart at every size (covered with Should fix 10 if done there). (general)

## Settled calls
- **Audit leads.** All three lenses agree: the ~460 "#globe overlaps" rows (the globe is the full-bleed stage),
  every "hint out of view" row (the hint is meant to go after the first action), and the Manual "keep region" rows
  (modal dialog) are not findings. Do not move overlays off the globe to clear them.
- **No sensitivity agent.** All three lenses: nothing cultural or Native; disasters shown as place, date, depth, size,
  never tolls. Keep it that way; the teacher-notes content line (Polish 13) is all that is needed.
- **Wave giveaway.** Teaching found no giveaways; play saw the shadow labelled before Fire. Settled for play: the
  shadow is the finding, so it shows when the rays get there (Polish 2). No question, score or "found it" moment is
  added.
- **Stations status line and FIT.** The fix (Should fix 5) is an instrument status line, not numbered steps, a
  progress bar or a verdict. The 200 km threshold label goes; the offset stays a km readout (Done-when 10, CODEX-CURIOSITY).
- **Tags on merged items.** Should fix 5 (play general, craft family) and 6 (teaching general, play family) are
  counted general: the fix is the POLISH and rule 4 rule any tool keeps.
- **Keep:** Merdith for Rewind; the M5.5 floor and its Manual line; ComCat place names as ComCat has them; Strike
  naming events by place only; no welcome screen; the honesty notes (moved under "For the curious", not cut).

## To the spec's open questions
- **HS-ESS1-5 (science-9-orbits-and-earth-s-history) is listed under "Also reaches" but nothing shows the ages of
  crustal rocks** (teaching S4). Either add a sea-floor age layer (an ocean age grid such as Seton et al. 2020, CC BY
  4.0 to be verified), readable by Pin and along a Slice, which would also give Hawaii's chain (Things to do 12,
  teaching P1) and the Atlantic opening real ages; or drop science-9 from "Also reaches" (rule 2, never a thin
  activity). Codex does not add the layer in this round.
- **Present-day plate motion source** (Blocker 1). If Merdith's own rotations cannot give a believable no-net-rotation
  speed, should Pin use a present-day plate motion model (ITRF2014-PMM or NNR-MORVEL56, licence to check) instead? That
  changes the spec's source line.
- **Rewind as a test, not only a playback** (teaching P4): a "drag South America to fit Africa" try before or beside
  the model, as Wegener did, with no score. A new mode, so it is the spec's call.
- **Stacked record section** (play 9): A, B and C traces stacked as a real record section instead of one trace at a
  time. A layout change to the Stations panel; worth deciding with the 375x812 sheet in mind.

## Not taken
- Wave: draw the receiver on the globe along a great circle from the source (play 7, second half): the globe ring at
  104 deg already ties the cutaway to the globe; revisit after Should fix 4.
- Kit "✨ Motion" emoji on the power panel (craft 10): a kit change touching every tool, outside this tool's files; log
  it for the kit, not here.
- Reykjavik reading Eurasia at the 0.1 deg model (teaching N4): the panel already says "boundary area"; model honesty.
- Nearest volcano "Unnamed" for Honolulu and Mumbai (teaching N4, play 18): faithful to the NOAA list.
- 375x812 marker sliders too coarse (play 9, second half): covered by the trace drag fix (Should fix 1) and Shift
  jumps (nit 17).

## Exit check (2026-11-06)

Scoped re-check of the merged list on the current bundle (`living-earth.html`, 1,991,170 bytes), with a fresh audit
(`S:/CurioClass-codex-scratch/living-earth/exit/audit-r2/`) and my own drive frames (`S:/CurioClass-codex-scratch/living-earth/exit/d1/` to `d4/`, all 1366x768 unless named).

### Blocker
1. **Fixed.** `plateMotion` now subtracts an area-weighted NNR vector (src.html:2117-2128). Recomputed in the bundle:
   Denver 1.6 cm/yr at 247 deg (ITRF2014 1.6 at 247), Sydney 5.9 at 17 (5.7 at 19), Perth 7.2 at 33 (6.9 at 34), Cairo
   3.2 at 53 (2.9 at 53), Honolulu 6.9 at 294 (7.1 at 299): all five within 0.3 cm/yr and 6 deg (d1 default js).
   Pin at Sydney shows SPEED 5.9 cm/yr at 17 deg plus EDGE MOTION closing 0.4 cm/yr against the Pacific (d1/pin-sydney).
   Arrows now diverge across the Atlantic, South America west, Africa north-east, many arrows near the edges, above
   the dots (d1/arrows.png). The fingernail line now says "a few centimetres a year" and points to EDGE MOTION.

### Should fix
1. **Fixed.** S starts at 1560 s with its own labelled handle at the right end (d3/stations-drag-S.png). A real drag
   from the S handle to the S packet set S 1031.5 s (true S 1031.4), P untouched (d4). Note: a press in the trace body
   still moves the nearer marker (at the S packet with S unplaced that is P), which is the handle design asked for, and
   the P and S labels no longer overlap.
2. **Fixed.** Held click on Play speaks "Drag to spin." only, the globe keeps turning (lon 156.3, running); a fresh
   Slice click speaks nothing (d1 voice-play, voice-slice). Audit one-click table: only Play and Read speak; five-click
   and two-tap rows clean. `valid` checks present (src.html:1092-1093).
3. **Fixed.** Relief in its own "sea level / sea floor x20" strip above the 0 km line; the Mid-Atlantic slice (2025)
   puts 18 quakes, deepest 20 km, just under 0 km (d2/slice-mar-2025.png); Japan slice reads 358 quakes to 560 km.
4. **Fixed.** At 100 deg after 26:00: "P no direct wave here, S no direct wave here", receiver inside the drawn S shadow
   arc (d2/wave-100-end.png); at 99 deg S arrives 25:14 inside the 26:00 window (d2 wave-99-end). Direct P edge 98.
5. **Fixed.** Status follows the state ("Tap three places for stations 0/3", "Set P and S on each trace", "Catalog
   location shown"); readout "SET P AND S" until both are set; no FIT text; Reveal shows OFFSET in km and no OUTSIDE
   FILTERS tag on a 1998 event at year 1970 (d2/stations-solved.png, d3).
6. **Fixed (spot-checked).** Manual opens with plain sentences ("Each dot is a real earthquake. Bigger dots mean bigger
   quakes...") with "For the curious" below; captions plain ("Rays bend through a model Earth"); "S minus P is the wait
   between the two waves" beside the markers. Old readout words (NO BRANCH, FIT AMBIGUOUS, UNRESOLVED MODEL AREA,
   QUAKES HELD) no longer in src.html.
7. **Fixed.** Record docks as one line at the top of the Stations panel (d2/stations-solved.png); at 680x425 it sits on
   its own line between globe and toolbelt (d1/selected-680.png).
8. **Fixed.** After a click on Volcanoes: "]" moved speed 1 to 2, Space toggled the focused Volcanoes (the stated
   rule), a keydown "q" on the focused button toggled Quakes (d2 keys; q dispatched as a page event, the driver has no
   letter keys; Codex's native Q/V/P/F/A walk agrees). Manual states the Space rule.
9. **Fixed (not re-measured).** Volcanoes are a GL point layer; Codex's paired 4x-throttle medians 16.7 ms. Accepted on
   its evidence; no regression seen in frames.
10. **Fixed.** At 680x425 and 800x500: "D >= 0 km / D <= 700 km", spaced readouts, layer names in words, the open
    panel gets usable room, slim drum row present (sheet `S:/CurioClass-codex-scratch/living-earth/exit/sheet2.png`). Audit's two depth "text hidden" rows are
    the joined track's own thumbs (settled by Codex, both thumbs drag).
11. **Fixed.** 30 of 30 Manual links have `target="_blank" rel="noopener"` (d1 manual js, bundle grep).

### Polish (bulk spot-check)
Seen fixed: 1 (turn continues on first Play), 2 (no shadow before rays: "await rays" at T+1:12), 3 (Rewind plays,
d1 rewind), 5, 7 (Read: "1970. 475 earthquakes of magnitude 5.5 or more so far. 343 on this face"), 8 (IN VIEW in the
strip), 9, 11 (dial and joined track visible), 14 (load and dial both 475), 16 (QUAKES OFF in Rewind), 19 (trace axis
"20" and "26 min" apart). Not re-checked: 4, 6, 10, 12, 13, 15, 17, 18 (Codex evidence only; polish never blocks).

### Regressions
None found. Default screen, Slice, Stations, Wave, Rewind and Pin each shot once; the frames tied to each fix above.
OUTSIDE FILTERS remains on a normal catalogue selection outside the filters (src.html:1150), as intended. One exception
in my d1 wave shot was my own probe calling `arrival(100,1)` with a wrong phase key, not the tool.

### Gate
1. Done when: no regression on the short test frames; Codex's checks plus mine hold. Yes.
2. Codes: anchor MS-ESS2-3 taught; science-9 (HS-ESS1-5) stays an open spec question already written down in this file
   (add a sea-floor age layer or drop it from "Also reaches"). Carry it to the Review Desk. Yes, with that note.
3. Solo defaults: one quiet hint, first action speaks only the half not done, Manual plain-first. Yes.
4. Sensitivity: not flagged by any lens; teacher-notes content line added. Not required.
5. No blocker or should-fix open. Yes.
6. Bundle: 1,991,170 bytes (under 2 MB); audit shows no errors in any row; no fetch, external script or stylesheet in the
   bundle (the audit itself does not list network). Yes.
7. Voice: `voice/lines.json` holds exactly the two hint halves, matching the two `V.how` calls; audit counts clean;
   recordings absent, browser-voice fallback. Yes.

## Audit pilot
- Leads confirmed: none new that are findings; Play speaks one line and Read speaks current state (matches my frames).
- Leads wrong: the ~550 "#globe overlaps" rows, Manual-modal "text hidden" and "keep region" rows (settled), the depth
  track "text hidden" rows (joined two-thumb track), marker label "hidden under label" rows (ancestor hit-test, text
  visible in d3/d4 frames), record "hidden under #record-dock" rows (dock is its parent).
- Missed: no network-request check in the report; the trace drag (handle versus body press) needs a held drag, which
  the audit does not do; the first save is written while it still runs, so wait for the "Not finished" banner to clear.
