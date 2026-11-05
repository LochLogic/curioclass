# Band Practice handoff

## Cold review changes, 2026-11-03

Cold play preceded the builder report and source. The review kept the painted room, original charts, large trace and immediate pad feedback.

- `stop` and `renderSummary` now put Solo break's fitted tempo and landing, and Ghost race's penalized score and best comparison, on the stage desk. The phone desk fits three result lines without pushing the 120 px pad below its prior position.
- `updateGhost` compares the same resolved chart notes and runs as misses expire, rather than only on taps. A stopped setup change clears old evidence and refreshes the ghost for the selected song and part.
- `receiveTap` chooses the matched chart note before sounding it. Late drifting bass taps therefore keep the intended pitch and chord. Early first notes retain their full 150 ms matching window.
- Result hints never recommend the disabled Ghost race Speed slider. Mixer narration checks that fewer players really remain, and quiet mode changes discard pending Read instead of starting a stale hint.
- Mode/start transitions clear old feedback. Zero average reads with the band. Clear bests names Ghost race when another mode is selected.
- The shaker was redrawn with the built-in image generation tool, rekeyed from `art/raw/shaker.png`, and checked at its final size. Its egg is now hand-sized relative to the stool. Other paintings were retained.
- Dense offscale values are grouped as a range and count below 700 px trace width, retaining every triangle. All exact visible offscale values are in the canvas title and accessible description. Wider trace labels are bounded to the plot.
- The review audit finished once with 16 leads. Its direct Clear bests check retained focus and cleared seeded data in all modes, but the hint was above the scrolled panel. A two-line post-audit fix repeats the confirmation beside the pad; only those three mode frames were re-shot. No further full audit was run.

Review evidence is under `_scratch/band-practice/review-*`. The final audit status belongs in `codex-review.md`. No shared files, commits or new music topics were introduced.

Build only, 2026-10-31. No commit, branch operation, deployment, or polish round.

## Source map

`src.html` starts from the kit starter structure. It uses kit:curio CSS, Curio.init, Curio.voice, and the shared Sound and Motion settings. The responsive stage uses real CSS pixel sizes instead of scaling a fixed scene. The styles, semantic stage and controls, song data, local audio adapter, timing model, canvas renderer, and handlers appear in that order.

`SONGS` contains the exact three patterns and chord lists, indexed from zero. `CHORDS` supplies close keyboard voicings and bass roots. The student's entire instrument station is absent from the backing audio. Each press sounds the next expected part note immediately; no tap is quantized.

`window.__tool` exposes state, timing/statistics helpers, audio context, gains, source nodes, calibration, bests, and narration logs for cold review. It is a diagnostic hook, not a student control.

## Timing and tricky parts

- Audio uses a 25 ms lookahead and a 150 ms scheduling horizon. `at()` stores visual events, drained against the audio clock by requestAnimationFrame.
- The expected-note ledger is separate from scheduled sounds. It extends 24 bars ahead for Rehearse so early presses can match future notes without sounding them early.
- `tapTime` maps event.timeStamp with getOutputTimestamp and subtracts saved latency. The currentTime handler fallback is used when output timestamps are unavailable. Calibration's shared value is seconds under `curio-tap-latency`.
- Break matching shifts each expected window by the last matched offset; errors retain the original band's reference time. The first tap physically in bar 9 is an uncapped landing candidate. Miss deadlines use the shifted window too.
- Position uses piecewise audio-clock anchors so live Speed or Song changes preserve bar phase. Reconfiguration cancels future sources, drops future visuals, draws a divider, and starts new take statistics. Old dots remain visible in `archive`.
- Muting ramps the member gain to zero over 20 ms and stops its future sources. Unmuting uses the next chart note. Your own instrument is fixed on in the mixer because your taps use their own channel.
- Ghosts save only completed eight-bar takes. Changing the setup after a race starts makes that partial race ineligible for a new best; Play starts a fresh eligible race. This closes a partial-take scoring loophole while keeping controls live.
- `fitLine` returns slope, intercept, and standard error. Small-note t critical values use the spec's table; larger samples use the Student t asymptotic expansion. Fewer than four observations yield too uneven to tell.
- No narration runs during takes or click calibration. Read queues until Stop. Calibration how-to finishes before the eight clicks start. Read during that introduction cancels the preparation and reads a clear restart instruction. Mode changes cancel a pending calibration introduction. Live status text changes only when its words change, avoiding repeated screen-reader announcements on every animation frame.
- Calibration pairs the eight taps in order with the eight clicks, then drops the first two. This allows a consistent delay just over half a beat to clamp to 300 ms rather than being misassigned to the following click. Tested with 350 ms late and 90 ms early inputs.

## Art

Five generated paintings are present and used: room, drums, bass and amplifier, keyboard on X stand, shaker on stool. No people. Prompts include house style and `drawn_by: codex`; raw PNGs are retained as required. `art.py --rekey` made the WebPs. A second rekey enabled holes and despill to clean green fringing; no image needed redrawing.

## Choices and open questions

The spec has no explicit open-question list. Used the specified easy-coach voice, original song tempos, moving break windows, eight-bar ghosts, and saved device calibration. The user's image-tool direction supersedes the spec's older local FLUX route.

The family engine and family document are absent. The build brief prohibits writing kit or docs, so the Beat Buddies audio synthesis and clock are adapted locally. This is the only shared-engine exception; it is not a new music topic.

At 375 wide, Play and Part controls precede the band and the full-width pad is visible by 784 px. Song, Speed, mixer, calibration, and detailed results continue down the page. At compact landscape sizes those secondary controls scroll in the side panel. Core results also appear in the lower stage desk so a stopped take is useful without scrolling the longer summary.

## Engine changes wanted

- New `kit/rhythm.js`, based on `tools/beat-buddies/src.html` audio(), tone(), pluck(), noise(), SND, at(), startClock(), stopClock(). Preserve the compressor, room routing, source lifecycle, and audible timbre.
- `startClock(bpm, step, {lead, steps:4})`: add configurable steps per beat and phase-preserving rescheduling for live changes. Track per-part source nodes so mute can cancel scheduled notes and ramp a part gain over 20 ms.
- `tapTime(event)`: use getOutputTimestamp mapping, fallback currentTime, then subtract the saved calibration. Export latency get/set/reset, using the shared localStorage key and documenting seconds as the storage unit.
- `judge(t, expected, maxWin)`: nearest unmatched expected note, capped by neighboring gaps, with moving-window support as an option for silent breaks. Return the original-clock offset.
- `fitLine(xs,ys)`: least-squares slope/intercept and slope standard error. The spec's trend and tempo reporting need both.
- New `docs/families/rhythm.md`: document these APIs before siblings depend on the engine. Neither shared path was written in this build.

## Cold review notes

Evidence and temporary scripts are in `_scratch/band-practice/`. Read the final report for exact coverage and audit leads. Audio test Chromes were muted, so timbre and headphone feel still deserve an owner's listening pass. Voice recordings were intentionally not generated; all 19 fixed lines use the kit's browser fallback until recorded.

The numerical recheck reproduces the current trend rule, contrast, durations, matching window, and tempo examples. The spec's old-rule false-positive range is narrower than the recomputed range across all its listed parts; see the report. No specification file was edited.

The full mechanical audit completed once with 27 leads. Concrete target/focus/header/repeated-mode issues were repaired and checked with held clicks in `audit-fix-frames`. Modal underlay coverage and the scrolling detailed summary are intentional. The auditor could not acquire the phone iframe context; independent drive.py host checks and final clean scratch-host checks cover all three modes at 375x812. Full audit was not rerun after fixes. Its report and all 54 frame originals remain in Scratch.
