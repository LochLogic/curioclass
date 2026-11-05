# Cartoon Soundtrack Mixer handoff

## Built structure
`src.html` extends the kit starter. CSS lays out a theater, canvas picture, timeline and tabbed control desk. All images use art tokens and all sound is synthesized locally. Three modes share one fixed cartoon. The Music, Effects and Story panels update persistent controls in place. A narrow timeline is 720 px wide and follows the playhead.

The script contains original cue presets and ready-made scores, local instrument extensions, shared-clock playback, the cartoon renderer, persistent cue controls, effect placement and dragging, Mood Swap, and device-only saving. `window.__tool` exposes state and telemetry for cold review.

## Timing details
The picture reads the audio context clock when music plays, or the page clock for silent playback. `MS.play` starts each scene's events with `exclusive:false`. It has an 80 ms start offset. Live edits restart only the edited scene at the current phase, with the previous layer fading out. Mood Swap keeps the picture clock and restarts incoming cues at its current phase. Music gates and per-cue loudness wrap the shared voices. Effects schedule against the same context clock.

An event offset compensates for the engine's start delay on live swaps. Runtime beat anchors preserve the melody's beat when Tempo changes. Sound off transfers the picture to the page clock and Sound on transfers back without jumping. Music routes through the engine's dry and room buses. Effects use the same audio context.

## Engine changes wanted
- `kit/music-studio.js`, `INSTR`: move the tool's `tuba` and `strings` definitions into the shared table, with the current signatures. Tuba is sawtooth an octave down through a 700 Hz lowpass; strings are two detuned sawtooths through an 1800 Hz lowpass with 120 ms attack.
- `kit/music-studio.js`, `play`: expose a scheduled absolute start time, initial phase/offset, per-player gain and an 80 ms stop fade. Expose a live event/instrument update that cancels the already scheduled horizon. The current engine requires a local restart to meet the spec's immediate edit and swap behavior.
- `docs/families/music-studio.md`: document those additions together with the engine implementation. No shared files were changed in this build.

## Spec decisions and reconciliation
- Open questions: the spec lists none.
- The art list counts 16 named assets, although its total says 15. All 16 were generated and used.
- The ready-made Funny score uses Boing at 7.2 s, matching the puffed-fur pose. Scary and Sad use Thunder at the 7.0 s flash. All three use Tiny mew at 16.0 s. Content timing was followed; Done when 4's general flash wording conflicts with Funny's explicit score.
- Compact views show the six presets in a native Preset menu so all five musical shapers remain available. Full-size views show all six preset chips.
- On a short landscape preview, the transport sits over the bottom of the movie frame to give the picture more height.
- The required source calculations are in `_scratch/cartoon-soundtrack-mixer/numbers.txt`. Contrast and two-bar timing match the spec. A 375 px full width divided by 24 seconds is 15.625 px/s before margins; the supplied approximate 14 px/s is a layout estimate. The implemented narrow timeline uses the required 30 px/s.
- The stated 680 px estimate of 27 px/s is also inconsistent with a 62 percent width: that formula gives 17.5667 px/s. The 1366 and 1920 estimates agree with the formula after rounding. Actual timeline width follows the responsive layout.
- Fixed narration is prepared in `voice/lines.json` for upbeat-guide/Zephyr. No audio was recorded, per build instructions; browser speech is the current fallback.

## Cold-review focus
Listen to the four timbres on headphones, including live changes and mood swaps. Perceptual listening remains open because Chrome checks are muted. Cold-review repairs below address the box layering, doorway, dense chips and stale hints. The movie remains small in the short preview when both effect lanes are full. No git commit was made.

## Cold review changes, 2026-11-04
The first student play preceded reading the builder's report. The porch plate was repainted without its baked-in box, and kitten-peek was redrawn against the empty box reference. One animated box now persists into the carry scene, and the cat approaches the real small doorway in perspective with clipping at its jamb rather than a flat covering rectangle. Full prompts and the built-in image generation provenance are in art/prompts.json; selected raw assets and finished WebP assets stay in art/.

Crowded effects now spread their reachable labels into two lanes. Exact onset pins and duration strokes remain on the timeline, and crowded labels print their onset. Sparse effects retain proportional chips. The packing calculation uses the actual timeline width on resize. Effect duration is retained when moving near the ending; playback and the displayed duration clip at 24 seconds. Same-time collisions at the right boundary search left for a free quarter-second slot. Selecting a chip updates the hint with its time and length.

Stopped cue edits audition two notes through MS.play with the chosen timbre, loudness, tempo and style, replacing the generic beep. Read, mode changes, Play and Sound changes stop that audition. Read during playback changes the hint to a valid stopped action before reading. The completed score's film label names the student's intended mood, shaped scenes and effect count. The three-way demo now ends on the storm's final frame. Dense short previews still have limited film height because the timeline retains two 44 px effect lanes.

Targeted checks after the single audit repair drag-release hints and canceled drags, open the effect panel when a chip drag starts, and keep stopped phone selections visible. Phone saving disclosure stays visible in its own footer line. Textarea focus is inset so it does not cover the writing prompt. A newer swap drops a queued score-name result and stops a score-name line in progress; Read remains protected. The dense-effects audit fixture now explicitly returns its drag points and resets the narrow scroll viewport before each drag. Its initial audit screenshots were empty; use the separate real-input dense checks for that case.

## Verification and audit
The full audit completed with 64 leads. Repeated 680/800 ruler overlaps and the 42 px Read target were fixed, as were same-mode double taps cutting a welcome. Writing fields now have explicit aria-labelledby. The compact score-shaped audit state now uses the visible Feel menu rather than a hidden wide-screen preset chip. Modal coverage of the movie is intentional. The 375 px scrolling timeline is required by the spec and its playhead now follows stopped seeks as well as playback.

The full audit was not rerun after those repairs. Targeted held-click, keyboard, geometry, voice, sound-clock and frame checks passed. Evidence is under `_scratch/cartoon-soundtrack-mixer/`, especially `audit/audit.md`, `repair-frames/`, `close-frames/`, `timing-*.json`, `final-clock.json` and `feel-compare.png`. All Chrome runs were muted, so perceptual headphone review remains open. The final report gives the dispositions.

## Cold review verification complete
The one full review audit finished with 10 leads and no resize exceptions or controls left disabled. Dispositions and limitations are in codex-review.md. The dense fixture was repaired after its initial empty audit frames; separate real-input runs placed all 16 effects at distinct quarter-second times at 680, 1366 and 375 with no overlapping or undersized chips. Crowded labels now show onset and length. Final affected-frame checks cover stale speech, protected Read, drag time hints, phone disclosure/selection, inset writing focus, demo ending and singular/plural payoff counts. No second full audit was run. Test browsers and hosts were closed and host.html removed.
