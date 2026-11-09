# Play lens: living-earth (Curiosity No. 04)

Played cold twice: as a grade 6 student alone at home (anchor MS-ESS2-3), and as a teacher projecting it at 1366x768.
Frames are in `S:/CurioClass-codex-scratch/living-earth/play/` (r1 to r4) plus the shared audit
`S:/CurioClass-codex-scratch/living-earth/audit-r1/`. Chrome on port 9781, started and closed by drive.py.

## Short test (Curiosity)

- **Would a kid open it unassigned?** Yes. Play draws the Ring of Fire out of 26,230 real quakes in 18.7 s
  (measured), the dots bloom, the year and count tick up (r1/play-6s.png, r1/play-end.png). It is a real "whoa".
- **Would an adult play with it for fun?** Yes. The slices are the best thing here: Japan shows the slab dipping
  west to 560 km (r1/slice-japan.png), Peru-Chile to 600 km (r1/slice-peru.png), the Mid-Atlantic only 13 quakes
  at no more than 20 km (r1/slice-atlantic.png), Tonga down to 700 km. Three Stations circles meeting 10 km from the
  2004 epicentre is a real payoff (r2/st-solved.png).
- **Is the real thing the interface?** Yes: real catalogue, real relief, real sections.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, quiz or finish screen anywhere
  (checked src, Manual, every panel). The Stations OFFSET is a distance readout.

Short test passes. Mean frame 16.7 ms over the full play run with every dot (headless, r1 play-end-read).

## Findings

### Should fix

1. **Stations: dragging on the trace can never set the S marker.** src.html:1945-1948. Both markers start at 0 s, and
   a press picks the nearer marker, so a press at the S packet always moves P (S stays at 0 because |t-P| < |t|
   whenever t > P/2). Shown with real mouse input on Sumatra 2004, station A: press at the true S (990.8 s) left
   P = 997.5, S = 0, readout "S−P -997.5 s", with or without P set first (r2/st-drag-S-first.png,
   r2/st-drag-S-afterP.png). Only Shift-drag or the small sliders reach S, and a phone has no Shift. This is the
   tool's main hands-on measurement. Better: start S at the right end (or hide each marker until placed), and let a
   press choose by which packet it is nearer, or give each marker its own grab handle on the trace.
   family:curiosity.
2. **The first-run hint is spoken after the action it asks for, and in the wrong place.** src.html:745-746.
   `touch()` speaks "Drag to spin. Press play." on the first action, whatever it was. Voice log, held clicks:
   after Play it says "Press play" while the archive runs (r3 v-first-play); after the Slice tab it says
   "Drag to spin" where a drag now draws a section line (r3 v-first-slice); after a drag it says "Drag to spin"
   (r3 v-first-drag). The on-screen hint is hidden at the same moment, so the voice and screen disagree.
   Better: if the first action already spun or played, say nothing (or only the half not yet done); never say it once
   a tool is open. family:curiosity (any Curiosity whose hint can only be voiced after the first gesture).
3. **Stations caption never moves on.** src.html:475 and the readout line. The panel keeps saying
   "Tap three stations" after three are placed, struck and solved (r2/st-solved.png), and the readout shows
   "FIT AMBIGUOUS" before anything has been measured (audit state-stations-1366x768.png), which reads like an error.
   It is a five-step procedure (place three, Strike, set six markers across three channels, Circles, Reveal) with no
   word on screen about the next one. Better: one short instrument-style line that follows the state ("Strike to
   record a quake", "Set P and S on each station", "Circles"), and no FIT text until Reveal. POLISH "words match the
   state". general.
4. **The quake record card covers the globe when a tool is open.** The card sits at the left edge (x 25 to 250) and
   the globe moves left to make room for the tool panel, so the card covers the west of the globe: in Stations the
   catalogue circles and station B run under the card text (r2/st-solved.png; audit state-stations-1366x768.png).
   Same at 680x425 and 800x500 with no tool open (audit state-selected-680x425.png). Better: dock the record inside the
   tool panel when one is open, or move it above the drum. general.
5. **The Manual is written for adults.** src.html:550-603. "Normalized three-plane fit", "finite rotations are
   resolved through the published plate circuit relative to plate 000 ... quaternion interpolation", "palaeomagnetic
   reference frame", "Pn and far-side PKP/PKIKP". The grade band is 4 to 12 and the anchor is grade 6; a student who
   opens the drawer to learn how Stations works will not get through it. The panel captions carry the same register
   ("±150 km swath · quake depths 1:1 · surface relief ×20", "schematic older fossil evidence · modern overlays
   withheld", "0–5 Ma average, in its own reference frame"). Better: each Manual section opens with two plain
   sentences a grade 6 student can follow (what to do, what you will see), with the precise honesty notes kept
   below them. "Things people have found" also opens with two paragraphs of instructions ("Change only the depth
   floor and compare the patterns"); the brief wants short findings read after the fact. family:curiosity.

### Polish

6. **The globe stops turning the moment Play is pressed.** src.html:1344 (`!state.touched`). The first play run
   shows only the West Pacific (r1/play-end.png), so "the thin line down the middle of the Atlantic" in the spec's
   first reaction never appears unless the student thinks to drag. Better: keep the slow turn during play until the
   student drags. general.
7. **Wave gives its finding away and the globe source does not matter.** The cutaway prints the violet "S SHADOW"
   arc and the readout says "S SHADOW" before Fire is pressed (audit state-wave-1366x768.png), and since the cutaway
   always puts the source on top, tapping a new source changes nothing in it (the Manual says so). The disc is about
   135 px across in a 390 px box at 1366x768 (r1/wave-end.png), so the 25-minute ray fan is crowded. Better: reveal
   the shadow label only after the rays have reached the far side, draw the receiver on the globe along a great
   circle from the source, and give the cutaway the room. family:curiosity.
8. **Rewind can only be dragged.** The big Play pad is disabled in Rewind (r1/rewind-200-atlantic.png). "Watch the
   fossil belts join up" wants a run from 0 to 200 Ma on the same pad. family:curiosity.
9. **Stations makes the student switch channels with a select.** Three stations, six markers, one trace at a time
   behind a dropdown; tapping a station triangle on the globe does nothing. A real record section stacks the three
   traces. Better: stack A, B and C (each short) or let a tap on a triangle choose its trace. On 375x812 the P and S
   sliders are about 80 px for 1,500 s (about 19 s per pixel, roughly 150 km of distance), too coarse to land a
   circle (audit state-stations-375x812.png). family:curiosity.
10. **Motion arrows are hard to read.** One small cyan arrow per plate at its centroid, under the dots
    (r1/layers-hawaii.png); "find two plates heading straight at each other" is hard to do. Better: a few arrows
    along each plate near its edges, drawn above the dots. general.
11. **Calm mode skips the wave.** Fire with Motion off jumps straight to 25:00 (src.html:1223). Year playback in calm
    steps by years and keeps time (r2/calm-play.png); Wave should step too (POLISH, calm keeps time). general.
12. **Preview size (680x425) instruments are too small to use.** The section is about 40 px tall and its "A" label
    prints over "2009 km → B" (r2/preview-680-slice.png); the station trace is about 50 px (r2/preview-680-stations.png);
    layer buttons shrink to Q V P F A with no word for Relief or Arrows; the depth faders lose the word DEPTH
    (audit size-680x425.png). Better: give the open panel the globe's room at this size, or stack. general.
13. **Read reads stiffly.** "1974. 2252 earthquakes in the magnitude 5.5 and greater catalogue under these filters."
    (r3 v-read-after-play). Better: "1974. 2,252 earthquakes of magnitude 5.5 or more so far." general.
14. **"OUTSIDE FILTERS" on the revealed Stations quake.** At the default year 1970 every revealed quake is labelled
    OUTSIDE FILTERS (r2/st-solved.png), which reads as an error at the payoff moment. Better: drop the tag on a
    Reveal, or move the year to the event as the catalogue list already does. general.

### Nit

15. At load the time dial says 1970 and QUAKES 0 (state.year 1970.0), but dragging the dial back to 1970 shows 1970's
    quakes (year + .999). Read at load says "0 earthquakes". src.html:677 versus 1189. general.
16. The Tibetan Plateau reads as a white hatched patch at 1x (moire in the shaded relief), visible on every default
    frame; fine at 4x (r1/zoom6-tibet.png). general.
17. Strike always starts at Sumatra 2004 and cycles the same fixed order. A random start would make the second visit
    fresh. family:curiosity.
18. Pin at Honolulu names its nearest volcano "Unnamed · 105 km" (r1/pin-hawaii.png). general.

### For the Teaching lens (not judged here)

- Pin SPEED reads 6.2 cm/yr for Denver and 9.3 cm/yr at 264° for Honolulu (r1 pin-denver, pin-hawaii). These are the
  Merdith model's 0 to 5 Ma palaeomagnetic-frame average, as the Manual says, but a student will read them as how fast
  their ground moves now, and they are well above the usual present-day figures for North America. Worth a check
  against "a readout that misleads is a blocker".
- Nothing cultural or Native here. The Strike list names deadly events (2004 Sumatra, 2011 Tohoku, 2015 Nepal) by
  place only, with no tolls, as the spec asks; no sensitivity review needed in my view.

## Frames looked at

Audit: size-* (all nine), state-selected/slice/stations/wave/rewind/pin/manual at 1366x768, state-stations and
state-stations-cleared and state-wave at 375x812, state-slice 680x425, calm-1366x768.
Mine: r1 first-0s, play-6s, play-end, japan-deep300, slice-japan, slice-peru, slice-atlantic, mag8, mag8-select,
layers-hawaii, zoom6-hawaii, zoom6-tibet, rewind-100-atlantic, rewind-200-atlantic, pin-denver, wave-end; r2
st-drag-S-first, st-drag-S-afterP, st-solved, narrow-760-slice, preview-680-slice, preview-680-stations, calm-play;
r3 voice logs (first tap by Play, Slice, drag, Read; Play x5; Sound off and on).

## Audit pilot

- **Confirmed:** the record card over the globe at 680x425 and 800x500 (finding 4; it also happens at 1366x768 with a
  tool open, which the audit listed only inside the "overlap: #globe" block); the tool-tab "how line cut (hush)" rows
  point at the same wrong first-hint line as finding 2.
- **Wrong:** every "overlap: #globe" row (the globe canvas is the full-bleed stage, every overlay sits on it by
  design; about 400 of the 523 rows); "hint out of view" in every state (the hint is meant to be gone after the first
  action); Manual "keep region covered" rows (the Manual is a modal dialog); the marker label overlaps in
  stations and stations-cleared at small sizes (the labels sit above the sliders and read, see audit
  state-stations-cleared-375x812.png).
- **Missed:** the Stations drag that cannot set S (finding 1), the first hint spoken after its action (2), the
  stuck Stations caption (3), Manual and caption reading level (5), the globe stopping on Play (6), the Wave
  shadow labelled before Fire (7), calm Wave jumping to the end (11), Read wording (13).
