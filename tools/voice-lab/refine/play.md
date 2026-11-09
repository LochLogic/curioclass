# Play lens: voice-lab (Curiosity No. 03)

Cold Play lens, 2026-11-05. Judged against CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", plus
POLISH.md. Played as a grade 8 student alone at home (and a first grader poking), and as a teacher projecting.
Own frames: `S:/CurioClass-codex-scratch/voice-lab/play/` (p01 to p19). Shared audit: `S:/CurioClass-codex-scratch/voice-lab/audit-r1/`.
Headless Chrome has no microphone, so MIC was judged from the code and the refused path only.

## Short test

- **Would a kid open it unassigned?** Yes with a microphone: seeing your own "ahhh" turn into a stack of stripes is the
  hook, and it needs nothing read. Without a mic (the site's embed, many school Chromebooks) it is a bank of steady
  four-second drones; still good, but much less pull (see F1, F9).
- **Would an adult play for fun?** Yes. Narrow-band harmonics, the clarinet's missing even harmonics (p03), the log ruler
  and the child-versus-adult vowel shift (p19) are real things an adult enjoys finding.
- **Is the real thing the interface?** Yes. The ribbon is real FFT data at 48 kHz, the readouts are live, and no
  painted art sits in the way.
- **Does it work with no finish line?** Yes. No score, goal, level, sticker, finish screen or vowel target anywhere
  (searched src.html; the only "level" hits are the dBFS meter).

Passes all four, so no blocker. The risks are in the first two minutes without a mic and in readouts that go blank.

## Findings

**F1. Embedded view tells the student to do something that cannot work.** should fix, family:curiosity
- Where: first screen in the site iframe; `src.html:122` hint, `toggleMic` at 368.
- What: the tool page iframe has no `allow="microphone"` (checked: host iframe has no allow attribute, p15), so every
  first-time student on the site is told "Press the mic switch, then say ahhh.", presses it, and only then hears
  "No mic here." The spec's open question leaves the template alone, which is fine, but the tool can know up front
  (`document.permissionsPolicy?.allowsFeature('microphone')` / `featurePolicy`) and open on the fallback hint, ideally
  naming Play full screen for the mic.
- How: p15-iframe-first.png; p12-mic-refused (fallback only after the press).

**F2. The big MIC knob is not the mic switch.** should fix, general
- Where: INPUT module, `src.html:131` (rotary is a styled `<select>`) beside the small MIC rocker at 132.
- What: the hint says "Press the mic switch". The eye goes to the large round knob labelled MIC; clicking it opens a
  plain browser drop-down (MIC / CLIPS / TONE) and nothing happens. The actual switch is the small rocker also labelled
  MIC. Two controls both reading MIC, and the wrong one is the obvious one. Better: label the rocker "MIC ON/OFF" (or
  light it) and make the knob a real rotary that steps on click instead of a drop-down.
- How: p13-rotary-click.png.

**F3. PITCH goes blank on whistles, including the tool's own whistle pad.** should fix, general
- Where: `yin()` at `src.html:506` (50 to 1,000 Hz limit).
- What: the built-in whistle glides 680 to 1,120 Hz; PITCH and NOTE drop to dashes for about a third of every loop
  (logged: `0/1050 0/1076 0/1095 ...`). Real whistles sit around 1 to 3 kHz, so "whistle a tune" (spec Things to do 2)
  will show dashes almost the whole time. The generator does the same above 1 kHz (1500 Hz: PITCH dashes, PEAK 1500).
  Better: extend the pitch range to about 4 kHz, or fall back to PEAK for a clean single line.
- How: p02-whistle-pitchlog.png and its log; p11-tone-sweep log.

**F4. F1 / F2 readout is dead in live play.** should fix, family:curiosity
- Where: `updateReadouts()` at `src.html:631` (`state.held&&f?.f1`).
- What: while a vowel plays, the internal estimate is good (ah 710/1100, oo 280/830, child ee 310/3130) and the chart
  cross moves, but the readout strip shows "··· / ···" until Hold is pressed. A student saying "eee, ahh, ooo" sees
  one of five readouts never change and reads it as broken. The spec meant "while a voiced sound is held" as sustained,
  not the Hold pad. Better: show the live estimate (it is already smoothed at 65 ms) and let Hold freeze it.
- How: p06 log (`··· / ···` with current f1 710, f2 1100); p06 and p19 frames.

**F5. Releasing Hold wipes the ribbon.** should fix, general
- Where: `toggleHold()` at `src.html:609` (`else clearHistory()`).
- What: Hold, measure, press Live: the whole picture is gone and starts from empty (history 12 frames right after).
  A teacher who froze a word to point at it loses the context the class was looking at; a student cannot hold, check,
  then compare with the next word. A real analyser resumes scrolling. Better: keep history and let the gap show.
- How: p07-hold-then-live log.

**F6. Vowel chart sits over the newest sound.** should fix, general
- Where: `#vowels` at `src.html:34` (right edge), and the 680x425 rules at 104.
- What: time enters at the right, so the chart covers the live edge: at 1366x768 the last 1.3 s, at 680x425 almost the
  whole ribbon (the ribbon is about 70 px tall there and the chart fills it, 7 of 9 points covered). Saying a vowel
  while watching the chart means not seeing it arrive. Better: dock the chart over the left (oldest) side, or let the
  ribbon shrink beside it.
- How: state-vowel-held-1366x768, state-live-vowels-680x425 (audit, confirmed), p06, p19.

**F7. Hold plus a pad press plays sound but nothing moves.** nit, general
- Where: `playPad()` at `src.html:466`.
- What: with Hold on, pressing a pad lights it and plays it, status reads "CLIPS / HOLD", and the ribbon stays frozen.
  A kid thinks the pad is broken. Better: a pad press returns to Live.
- How: p14-hold-pad-press log ("CLIPS / HOLD | true").

**F8. A/B outlines are hard to read.** polish, general
- Where: memory drawing at `src.html:710-720`.
- What: both outlines are squeezed into the left 30 percent of the glass, on top of the ribbon, on top of each other,
  and the "A spectrum / B spectrum" labels sit across the outlines. Clarinet versus flute (p03) and sss versus shh
  (p18) are the comparisons the pads invite, and they are the hardest thing on screen to read. Better: a darker
  backing panel, wider plot, and the labels outside the traces.
- How: p03-instruments-AB.png, p18-sss-then-shh.png.

**F9. Without a mic, nothing moves but the whistle and siren.** polish, family:curiosity
- Where: `makeBuffer()`, voice bank.
- What: every vowel pad is one steady vowel on one pitch, looped. The spec's best moments ("eee then ooo makes the
  bands jump", "slide your voice and every stripe climbs together", rhyme and two-speaker compares) all need a mic.
  More real material, not a game: a pad that glides ee to ah to oo, and one that slides an "ahh" up an octave, would
  give the no-mic student the same reaction.
- How: p06 (switching pads by hand is the only way to see bands jump).

**F10. The privacy line covers the bottom-left of the data.** polish, general
- Where: `#privacy` at `src.html:31`.
- What: it must stay visible (Done when 2), but it sits over 0 to 300 Hz on the oldest part of the ribbon, where the
  first harmonic and F1 live, and under the A/B traces. Better: put it on the time axis row or in the readout strip
  once a sound is running.
- How: p03, p06, p19, audit vowel-held overlap rows.

**F11. Projected, the numbers are small.** polish, general
- Where: `.readout output{font-size:19px}` and 10 px deck labels, fixed at every size.
- What: at 1920x1080 the readouts stay 19 px and the deck legends 10 px; from the back of a room PITCH and NOTE, the
  two numbers a teacher points at, are hard to read. Better: scale readouts with the viewport (clamp to about 32 px).
- How: audit size-1920x1080.png.

**F12. The chord reads "C2", a note not being played.** polish, family:curiosity
- Where: C major pad; PITCH 65.5 Hz, NOTE C2 +4 (p04).
- What: this is real (C4, E4, G4 repeat together every C2 period), but with no word it looks like an error. Manual
  says pitch is unreliable for chords. Better: turn it into a "Things people have found" entry (the shared period of a
  major chord), which is exactly the kind of depth a month of use should find.
- How: p04-chord-log.png.

**F13. Singing against the tone is gone.** polish, family:curiosity
- Where: `selectInput()` releases the mic in TONE (spec open question, lean taken).
- What: spec Things to do 10 (sing until your PITCH matches 440 Hz) cannot be done: TONE turns the mic off. The lean
  avoids feedback, fair, but the activity is a good one. Possible later: in MIC mode a quiet reference line at a chosen
  frequency drawn on the glass (no sound out) to sing onto.
- How: code read, `src.html:359-366`, 368-371.

**F14. NOTE says +1 cent beside PITCH 440.** nit, general
- Where: tone at 440 Hz: PITCH "440 Hz", NOTE "A4 +1 ¢" (state-tone-1366x768, p11 log).
- What: two readouts of the same number disagree by rounding; a student tuning to 440 sees "+1" and keeps nudging.
  Done when 4 still passes.

## Checked and fine

- No welcome screen, goal, score or finish; the first-run hint is one quiet line, gone on first audio, and Read speaks
  the live state (code read; audit row 0).
- Wide versus Narrow on the same vowel visibly differ (state-narrow-memory: bands, then harmonic lines with 1x to 10x
  markers on them). Clarinet odd harmonics strong, even weak (p03). Child ee band higher than adult ee (p19).
- Tone tracking 80 to 1,000 Hz correct (80.0, 110, 440, 1000); 20 and 40 Hz show dashes honestly.
- 20 s sweep at 16 kHz range: frame median 16.8 ms, p95 17.6 ms (p09, headless, no GPU). No freeze.
- Motion off keeps time (audit clean; code steps the draw at 125 ms, sampling unchanged).
- Manual drawer and plate lower-left at every size, power panel beside them (audit frames).
- Mic refused: CLIPS selected, fallback line shown and spoken, pads work (p12).

## Audit pilot

- Leads confirmed: the vowel chart covering the ribbon at 680x425 and 375x812 (F6); the privacy line over the glass
  (F10); the cramped ribbon at 680x425.
- Leads wrong or harmless: "#ribbon overlaps #status/#hint/#privacy/glass-label" at every size is by design (labels on
  the glass). "hint out of view" in every state is the hint correctly gone after the first sound. "count and word
  disagree: 1 dBFS" is the "-13.1 dBFS" readout, not a count. Manual "choices cut short by a scroll panel" is the
  sources list in a scrolling drawer, fine. Welcome "not heard" after a pad tap is BASELINE rule 16.
- What it missed: F2 (the knob is a drop-down), F3 (pitch blank on whistles), F4 (F1/F2 dead live), F5 (Live wipes
  the ribbon), F1 (the iframe has no mic permission, so the first hint fails on the site), F8 (A/B unreadable), F12.
- Harness note: drive.py's `wait` does not advance requestAnimationFrame in a background headless tab, so ribbons in
  frames reflect time spent in `js`/`after`, not the wait. Frames that need a long ribbon should wait inside `after`.
