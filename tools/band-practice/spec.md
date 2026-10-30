# Band Practice

## One idea
You hold one part in a four-piece band and every note you tap lands on a timing trace in milliseconds, early above the line and late below; then the band drops out for four bars and comes back exactly on time, so you find out whether you rush or drag when nobody is holding the beat for you.

## Not like
- beat-buddies (K-2, built, same family): a class claps a steady beat and rhythm cards together; nothing is measured. Here every tap is timed against the band, and the lesson is the ensemble: who you listen to, and holding the tempo alone.
- marching-band (grade 2): rows and arrays of musicians. No timing.
- beat-lab (9-12): you program a beat on a grid and it plays perfectly. Here nothing is quantized; you perform live.
- note-ninja (3-5): notes fly toward a line to be read. Here there is no note highway on purpose: you play by ear, with a one-bar part card only as a reference.
- world-music-map (this group): looks at rhythm cycles on a circle. Here you play inside one groove and get measured.
- song-form-builder, theory-gym, music-history-radio (this group): form, analysis, eras.
- choreography-board (6-8): dance phrases to music. phishing-spotter, packet-race (other races): not music.

## Who and how
- Grade 6-8, music, module "Ensemble Skills (Music)".
- Topic line: playing in time with a band
- Driver: students (own laptops, headphones strongly suggested; the setup card says so). 15 to 30 minutes.
- Standards: NCAS MU:Pr5 (rehearse, evaluate and refine), MU:Pr6 (present; performing with an ensemble).
- Header: title, topic line, modes **Rehearse** (default), **Solo break**, **Ghost race**, then kit `motion`, `sound`, `read`.

## Screens and modes

### Layout (all modes)
- Focus (all modes): the timing trace, where every tap lands; it is the widest, central thing on the stage (at least 40% of the stage height at 1366x768). The band above it is the context; the Tap pad is the student's hand.
- **Band** (top of the stage): four painted instrument stations in a row in front of the painted rehearsal room (Art), no people: Drums (a kit), Bass (a bass guitar leaning on an amp), Keys (a keyboard on a stand), Shaker (a shaker on a stool). Each lights on its hits (a glow in code under the cutout). Your station has a cyan outline and the tag "You".
- **Part card** (under the band): one bar of your part on a grid (16 cells, or 12 in the waltz) with counts under it ("1 e & a 2 e & a ..."; waltz "1 e & a 2 e & a 3 e & a"), your hits as filled cells. While playing, the current step is highlighted.
- **Timing trace** (full width under the part card): x is time in bars, y is your offset from the band from -150 ms (late, bottom) to +150 ms (early, top) with a center line "with the band". Each hit is a dot: early a triangle up (#ff8a5c), late a triangle down (#a98bff), in the pocket a circle (#6ee7a0). Misses are a hollow x on the center line; extra taps are small gray ticks along the top. Under the trace, a small bar per bar: that bar's average offset.
- **Tap pad**: a large button (at least 120 by 120 px, bottom right of the stage), "Tap (Space, J or F)".
- Panel: `hint`, **Play** (becomes **Stop**), **Song** select, **Part** (four icon buttons: Drums, Bass, Keys, Shaker), **Speed** slider (beats a minute; range per song), **Who you hear** (four toggles, one per band member; your own member is fixed on), **Count-in** toggle (on), **Calibrate**, and the take summary card.

### Rehearse (explore)
- Play gives a one-bar count-in (stick clicks, the count shown big), then the 8-bar song loops until Stop. The trace shows the last 8 bars and scrolls. Change Part, Speed or Who you hear any time, and it takes effect at once: the band keeps its clock, a divider is drawn on the trace at that moment and a new take starts from it.
- After Stop: the take summary (Content).

### Solo break
- 12 bars at the chosen speed (16 to 48 s by song and speed: longer than 30 s only for the slower 4/4 speeds, because the student plays the whole time and Stop is always live): bars 1 to 4 the band plays, bars 5 to 8 the band is silent (the stations dim, the trace is shaded "band out"; only your own taps sound), bars 9 to 12 the band comes back exactly on the band's clock.
- After bar 12: the break summary: drift ("rushed", "dragged", "held steady" or "too uneven to tell", with milliseconds per bar; rule in Timing rules), your tempo during the break against the band's ("You played at about 101 beats a minute. The band was at 96."), and the landing: your offset on the first hit after the band returned.

### Ghost race
- 8 bars at the song's set speed (Speed locked so races are fair). Your best take for this song and part is the ghost: its dots are drawn faint on the trace as you play, and a small meter shows who is ahead so far.
- After the take: "Timing error 23 ms (ghost 29 ms). 2 missed." A lower error becomes the new ghost. Bests are saved on this device per song and part, with **Clear bests**. No confetti.

## Content

### Songs (written for Curio Class; 8-bar loops; steps are 16ths, step 1 is beat 1)
1. **Hallway Funk**, 4/4, 96 a minute (Speed 70 to 120). Chords: Em7, Em7, A7, A7, Em7, G, A, B7.
   - Drums: kick 1, 7, 11; hi-hat 1 3 5 7 9 11 13 15; snare 5, 13. Your drums part: the snare on 5 and 13.
   - Bass: 1 root, 7 root, 9 fifth, 11 octave (around E2).
   - Keys: short chord stabs on 3, 7, 11, 15 (the "ands"), close voicing near middle C.
   - Shaker: 1 3 5 7 9 11 13 15, louder on 5 and 13.
2. **Night Bus** (a one-drop reggae groove), 4/4, 76 a minute (Speed 60 to 96). Chords: Am, Am, Dm, Dm, Am, Am, E7, E7.
   - Drums: kick and rim click together on 9 only (beat 3); hi-hat 1 3 5 7 9 11 13 15. Your drums part: the rim on 9.
   - Bass: 1 root, 7 root, 11 fifth, 12 octave.
   - Keys: skank chords on 5 and 13 (beats 2 and 4), short.
   - Shaker: 1 3 5 7 9 11 13 15.
3. **Waltz for the Rain**, 3/4, 132 a minute (Speed 96 to 160); 12 steps per bar. Chords: C, Am, F, G, C, Am, G7, C.
   - Drums (brushes): soft kick on 1 from the band; your drums part: a brush on 1, 5, 9 (every beat).
   - Bass: 1 root (one note a bar).
   - Keys: chords on 5 and 9 (beats 2 and 3).
   - Shaker: 1 3 5 7 9 11.
- When you play a part, the band's copy of that part is silent, and each tap sounds your part's next note at the moment you tap (bass pitch, chord or hit from the chart above). A note you miss leaves a hole in the music.

### Timing rules (all thresholds are the tool's own choices, shown in the teacher notes as such)
- Tap time: the audio clock time of the key or pointer press, from `event.timeStamp` mapped with `AudioContext.getOutputTimestamp()` (fallback: `currentTime` at the handler), minus the calibrated latency.
- Each tap is matched to the nearest expected note of your part within a window of 150 ms or half the gap to the neighboring expected note, whichever is smaller. A tap outside every window is an extra. An expected note with no tap is a miss once its window passes.
- Offset = expected time minus tap time, so positive is early. In the pocket: 25 ms or less either way. "A little early" or "a little late": 26 to 60 ms. "Early" or "late": more than 60 ms.
- Take summary: hits, misses, extras; average offset with sign ("on average 12 ms early"); timing error = the average of the offsets' sizes; a line for the most common result ("Most of your notes were a little early.").
- Matching in the break: in bars 5 to 8 each expected note's window is centered on its expected time moved by the last matched offset (so a player who drifts steadily is still matched note by note); offsets are still measured against the band's clock. Offsets beyond 150 ms draw at the trace's edge with a small arrow and their number. The landing is the first tap in bar 9 matched to the nearest note of bar 9 with no 150 ms cap; within 60 ms either way is "right with them" (landedWith), otherwise "apart" (landedApart).
- Rushing and dragging (trend, not one note): fit a straight line to your offsets over time in bars (least squares). In Solo break use bars 5 to 8; in Rehearse, the last 4 bars, shown as a word next to the bar chart. With slope b (ms per bar) and its standard error se: "rushing" when b times 4 is 60 ms or more and b is more than t times se (t the two-sided 95% value for the number of notes minus 2: 4.30 for 4 notes, 2.45 for 8, 2.07 for 24, 2.04 for 32); "dragging" the same with b negative; "held steady" when b times 4 is under 60 ms; otherwise "too uneven to tell". Parts with one note a bar (Night Bus drums, Waltz bass) give only 4 notes, so small drifts there read steady or uneven, never a false rush.
- Your tempo in the break: fit tap time against expected time over bars 5 to 8; your beats a minute = band beats a minute divided by the slope. Shown to the nearest whole number.
- Ghost race score: timing error with each miss counted as 150 ms.

### Calibration
- **Calibrate**: 8 clicks at 100 a minute (4.2 s from first to last click); tap with each. Drop the first 2; the median of how late the other 6 were (tap time minus click time, before any correction) becomes the latency (clamped to -50 to 300 ms) and is saved on this device as `curio-tap-latency` (meant for every rhythm tool), with **Reset calibration** beside it. If those 6 taps spread more than 60 ms from their median, it says "Those taps were uneven. Try again." and keeps the old value.
- Before any calibration, the latency defaults to the context's `outputLatency` (or `baseLatency`, or 0). The first Play offers "Calibrate first? It takes about ten seconds." with **Calibrate** and **Skip**.

### Teacher note facts (notes.md, not on screen)
- "One drop": a reggae drum pattern that leaves beat 1 empty and lands kick and snare together on beat 3.
- Skank: the short offbeat chords of reggae guitar or keys.

## Interactions in detail
- Input: Space, J or F (keydown, `e.repeat` ignored), or pointerdown on the Tap pad (never click, which fires late). While a take runs, those keys are caught at the document with preventDefault so Space never presses a focused button, and focus moves to the pad with `focus({preventScroll: true})`.
- Scheduling: the band plays from the lookahead clock (Family engine); visuals follow the audio clock, never timers.
- Who you hear: muting a member silences it at once (its gain ramps to zero in 20 ms and its already-scheduled notes are cancelled) and its station dims at once; unmuting brings it in on its next note. The summary lists who you heard ("with Bass and Shaker only").
- Everything stays live during a take: Stop, Song, Part, Speed, Who you hear, mode buttons and Read act at once (Read waits only while a take runs, since no line plays during a take; it reads when the take stops).
- Stop mid-take keeps the trace and gives a summary of what was played. Switching modes stops and clears.
- Edge cases: no taps at all gives "No taps yet. Press Space or the pad on your part's notes." A take where more than a quarter of notes are missed suggests a slower speed. Tabbing away (page hidden) stops the take.
- Motion off: stations stop pulsing (they change color only); the trace still draws.
- Sizes: at 1366x768 the band, part card, trace, Tap pad, Play and Part buttons are visible without scrolling. Under 900 px tall the band shrinks to icons in a row. In the 680x425 preview the band, part card and trace show, scene text at least 11 px. At 375 wide: band icons, part card, trace, then the pad full width.

## Look
- Accent (`--brand`) #38d1e8 stage-light cyan on a dark rehearsal room: background #14161c, panel #1d2029, ink #eef1f6, muted #9aa3b5. Early #ff8a5c, late #a98bff, pocket #6ee7a0 (each with its own shape).
- Contrast: brand on background 9.86:1 (dark text #14161c on brand buttons 9.86:1); ink on background 15.97:1, on panel 14.37:1; muted on background 7.13:1, on panel 6.41:1; early 7.79:1, late 6.74:1, pocket 11.71:1 on the background.
- The painted rehearsal room is dim and cool so the cyan and the hit glows stand out; the trace, part card and pad sit on solid #14161c and #1d2029 panels, so every ratio above holds over the painting.
- Different from beat-buddies (red #c2482f on pale green), beat-lab (orange on near black), frame-it (amber), design-fixer (indigo), and the other tools in this group.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. One style: "soft painted look, dim warm rehearsal-room light".
- rehearsal-room: "an empty school band rehearsal room in dim evening light, pale painted brick walls, rows of empty black music stands and folding chairs, a worn wooden floor with a few cables, a warm lamp glow in one corner, soft painted look"; 16:9; cutout no; people no; behind the band strip at the top of the stage, darkened 30% so the stations read.
- Stations (4 cutouts, one shared prompt "<item>, front three-quarter view, soft painted look, dim warm rehearsal-room light, plain white background"; 4:3; cutout yes; people no; one per station in a row of four, the same image used small as the icon row under 900 px tall; each brightens and gets a cyan or white glow in code on its hits, a dimmed copy when muted):
  - drums: a small drum kit with a kick drum with a blank head, a snare, a hi-hat and one cymbal, with sticks resting on the snare
  - bass: a red electric bass guitar leaning against a small black amplifier with a blank front
  - keys: a black electronic keyboard on a simple X stand
  - shaker: an egg-shaped wooden shaker resting on a tall wooden stool
- 5 images, none with people. Drawn in code: the part card, the timing trace, the per-bar chart, the Tap pad, the "You" tag and outline, the ghost dots and every label (charts and controls).

## Voice
Bank voice: `easy-coach` (a relaxed band director; no tool in this group or among its neighbors uses it). Style from the bank. `Curio.voice` with `scope: () => state.mode`. No line ever plays during a take or calibration; lines wait for the music to stop, and a line queued for a take that is already over is dropped.
- welcome (how; entering Rehearse; stale when Play is tapped): "Pick a part and press Play. Tap your part on the pad or the space bar."
- calibrateHow (how; when Calibrate is tapped, before the first click; stale when the clicks start): "Tap the pad or the space bar with each click. Eight clicks, as steady as you can."
- calibrated (event; stale when Play is tapped): "Got it. Your timing is set."
- calibrateUneven (event; stale when Calibrate or Play is tapped): "Those taps were uneven. Press Calibrate and try again."
- traceHow (how; after the first take stops; stale when Play is tapped): "Dots above the line were early. Dots below were late. Try to keep them on the line."
- listenHow (how; the first time a band member is muted while stopped, or after the take in which it was muted; stale when Play is tapped): "Fewer players now. Listen to who's left and lock in with them."
- welcomeBreak (how; entering Solo break; stale when Play is tapped): "Press Play. The band plays four bars, drops out for four, then comes back. Keep tapping on your own."
- breakRushed, breakDragged, breakSteady, breakUneven (event; after a Solo break take; stale when another take starts): "You rushed while the band was out." / "You dragged while the band was out." / "You held steady on your own." / "Your taps were too uneven to tell. Try again, nice and even."
- landedWith, landedApart (event; after the drift line; stale when another take starts): "When the band came back, you were right with them." / "When the band came back, you were apart. Listen for beat one."
- welcomeGhost (how; entering Ghost race; stale when Play is tapped): "Play eight bars. Your best take becomes the ghost to beat. Press Play."
- ghostNew (event; stale when Play is tapped): "New best. That's your new ghost."
- ghostHolds (event; stale when Play is tapped): "The ghost holds. Press Play to try again."
- noTaps (event; a take with no taps, after Stop; stale when Play is tapped): "No taps yet. Press Play, then tap the space bar or the pad on your part's notes."
- manyMissed (event; a take with more than a quarter missed; stale when Play or Speed is touched): "A lot of notes went by. Slide Speed down and press Play."
- Numbers are on screen only, so every spoken line is fixed and recordable.

## Family engine
rhythm (no family doc yet; this spec holds the full description; beat-buddies, K-2, is the built reference). Lift beat-buddies' audio from its src.html into `kit/rhythm.js`: `audio()` (master, compressor, room delay), `tone`, `pluck`, `noise`, the `SND` hits (kick, snare, clap, block, bell), the event list `at(t, fn)` drained by requestAnimationFrame, and the lookahead clock `startClock(bpm, step, lead)` / `stopClock()` (25 ms timer, 150 ms horizon). Additions this tool makes: steps per beat (`startClock(bpm, step, {lead, steps: 4})`), `tapTime(event)` (audio time of an input event, minus the saved latency), `latency` get, set and reset (localStorage `curio-tap-latency`), `judge(t, expected, maxWin)` returning `{i, offset}` or `{extra: true}`, and `fitLine(xs, ys)` (least squares). This tool feeds it the three songs as step patterns per part and the chord list per bar. world-music-map plays its cycles on the same clock. beat-buddies keeps its copy until it is next reworked.

## Sources
- National Core Arts Standards, Music MU:Pr5, MU:Pr6: https://www.nationalartsstandards.org/
- Audio clock, output latency and output timestamps: W3C Web Audio API, `AudioContext.outputLatency`, `baseLatency`, `getOutputTimestamp()`, https://www.w3.org/TR/webaudio/
- Reggae offbeat chords: Britannica, "Reggae", https://www.britannica.com/art/reggae-music ; one-drop drum pattern: Wikipedia, "One drop rhythm", https://en.wikipedia.org/wiki/One_drop_rhythm
- Waltz in triple meter with the bass on beat 1: Britannica, "Waltz", https://www.britannica.com/art/waltz
- Songs, parts and all timing thresholds: written for Curio Class (the thresholds are the tool's own choices).
- t values for the trend rule: Student's t distribution, two-sided 95% (any statistics table; scipy.stats.t.ppf(0.975, n - 2)).
- Checks run (Python with numpy and scipy, 2026-10-29): simulated players (3,000 runs each) with timing jitter of 25 and 40 ms (standard deviation) over the four break bars. The old rule (more than 5 ms a bar) called a perfectly steady player "rushing" or "dragging" in 52 to 79% of runs (1-note-a-bar parts worst), so it was replaced. The new rule (Timing rules) reads a steady player as steady in 95 to 100% of runs on every part tested (Hallway Funk drums at 70, 96 and 120; shaker and bass at 96; Night Bus drums at 60 and 76; Waltz bass at 96, 132 and 160; Waltz drums at 160). A player 2 beats a minute fast reads "rushed" in 91 to 100% of runs on Hallway drums at 96 and Night Bus drums at 60, and 100% on the shaker; 4 beats a minute fast or slow reads right in 98 to 100% on the 4/4 parts. On Waltz bass (one note a bar, 4 notes) 4 beats a minute fast or slow reads right in only 14% (at 160, 40 ms jitter) to 93% (at 96, 25 ms) of runs and "steady" or "too uneven" otherwise; the wrong direction came up in 0.1% of runs or fewer. Drift per bar for 1 beat a minute fast: 25.8 ms at 96, 41.0 at 76, 65.6 at 60, 10.3 at 132 (3/4). The on-screen example (101 against 96) drifts 124 ms a bar, more than the 150 ms window after two bars, which is why the break uses the moving window. Matching windows: the tightest is Night Bus bass (steps 11 and 12) at 96, half the gap = 78 ms, still wider than the 60 ms "early" line. Calibration: 8 clicks at 100 a minute span 4.2 s, so "30 seconds" became "about ten seconds". Solo break lengths: 12 bars of 4/4 at 96 is 30 s, at 76 is 37.9 s, at 60 is 48 s; 3/4 at 132 is 16.4 s; Ghost race 8 bars is 20 s (Hallway), 25.3 s (Night Bus), 10.9 s (Waltz). Contrast ratios in Look recomputed with the WCAG 2.1 formula (values as stated).

## Done when
1. With a scripted tapper at known offsets (40 ms early, 40 ms late, on time), the trace and summary show early, late and pocket correctly, with signs right (recompute in Python).
2. Misses and extras are counted correctly when taps are skipped or doubled, including at the waltz's one-note-a-bar bass.
3. Solo break silences the band for exactly bars 5 to 8 and brings it back on the band's clock; a scripted shaker tapper 4 beats a minute fast with 25 ms jitter reads "rushed" and its tempo readout matches the fitted value; a steady tapper with 40 ms jitter reads "held steady" or "too uneven to tell", never rushed or dragged, in 19 of 20 runs.
4. Calibration with a steady tapper 80 ms behind the clicks sets the latency to about 80 ms and later taps read in the pocket; uneven taps keep the old value.
5. Space never activates a focused button during a take; the pad uses pointerdown; held real-key input (press, about 120 ms, release) is timed from the press.
6. Ghost race saves a best, draws it faint next time, and Clear bests removes it.
7. No line plays during a take; how lines once in five takes in a row; result lines every take, dropped when stale.
8. Band, part card, trace, pad and Play are visible without scrolling at 1366x768 and 1280x720; preview readable at 680x425.
9. Focus: at 1366x768 and 680x425 the timing trace is the widest, central thing on the stage, and the four painted stations read as a band above it.
10. Tap while it plays: during a take, muting a member silences it within 50 ms and dims its station at once; Speed, Part and Stop act at once with a divider on the trace; the Tap pad keeps timing taps throughout.
