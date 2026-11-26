# Band Practice: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: band-practice

#### Built

Build only in `S:\CurioClass-codex`. All authored files are in `tools/band-practice/` and `_scratch/band-practice/`. No git operations, commits, shared-engine writes, deployment, or polish round.

Three modes, three exact original song charts, four playable parts, unquantized synthesized instruments, live listening controls, per-press timing trace, misses/extras, signed averages, bar averages and trends, calibration, silent break with landing, and saved per-song/part ghosts. Five generated paintings are placed. Core results are repeated in the stage desk so they remain useful without scrolling the detailed summary.

Uses the kit starter structure, kit CSS, Curio.init, Curio.voice, Sound and Motion. No network dependencies or microphone recording. Voice bank easy-coach, Umbriel, 19 fixed lines. Browser speech fallback is intentional; no recordings were made.

#### Numbers check

`_scratch/band-practice/recompute.py` and `numbers.json` recompute the source examples with NumPy and SciPy, including 3,000 trials per condition using the actual part positions.

- t critical values: 4.3027, 2.4469, 2.0739, 2.0423 for 4, 8, 24, 32 notes.
- One BPM fast: 25.773, 41.012, 65.574, 10.253 ms/bar at the specified tempos and meters. 101 against 96: 123.762 ms/bar.
- Tightest window: 78.125 ms. Eight calibration clicks span 4.2 s.
- Solo durations: 30.0, 37.895, 48.0, 16.364 s. Ghost durations: 20.0, 25.263, 10.909 s.
- Contrast on background: cyan 9.863:1, ink 15.972:1, muted 7.130:1, early 7.786:1, late 6.737:1, pocket 11.712:1. Ink/panel 14.369:1; muted/panel 6.414:1.
- Current trend rule correctly avoids a direction in 95.17 to 100 percent of steady trials. Four BPM fast/slow is detected in 97.67 to 100 percent of tested 4/4 conditions. Waltz bass ranges from 14.63 to 93.17 percent and has limited power, as the spec explains.
- Difference from spec: the old 5 ms/bar rule falsely reports a direction in 19.77 to 79.23 percent across all listed parts, rather than the stated 52 to 79 percent. The lower end is the dense shaker part. One sparse Waltz condition reached 0.133 percent wrong direction in this independent seed, slightly above the spec's 0.1 percent wording. These are Monte Carlo differences; the current rule was implemented as specified. The spec was not edited.

`verify_sources.py` independently recomputed the browser take summary and fitted tempo in Python. Its timing-rule assertions pass.

#### Feel check

Played held controls and keys, free takes, and complete timed Solo break and Ghost race runs. Best moment: the early shaker dots rise beyond the trace edge during silence, then the returning band lands against the same clock. The break reports rushed, about 100 BPM against 96, with a 2 ms landing in the measured full run.

Two flattest moments and build fixes:

1. The first band strip cropped the instruments into fragments. Fixed the image sizing, cleaned green edges with holes/despill, changed the background crop to show the room, and enlarged the laptop strip while retaining the trace's prominence.
2. Stop originally left the last tap label visible while its real summary sat low in the panel. The stage desk now shows timing error, hits/misses/extras, and average or break trend at once. Offscale labels also use staggered lanes instead of overlapping.

The room and instrument material detail hold up beside the bar tools; the chart is deliberately an accurate work surface. Audio was muted in every automated Chrome, so an actual headphone listening judgment remains open. No claim of a ten-minute listening playtest.

Side-by-side comparison is `_scratch/band-practice/comparison.html`, showing a scripted Band Practice trace beside Beat Lab. Both Beat Lab and Snowy Mail Route were opened before implementation.

| Band Practice | Beat Lab finish reference |
|---|---|
| ![Band Practice](../../_scratch/band-practice/presentation-frames/final-take-frame.png) | ![Beat Lab](../../_scratch/band-practice/bar-frames/beat-lab.png) |

#### Done when

1. PASS: 40 ms early, 40 ms late, and zero offsets return the correct signs in the real judge. Actual audio-clock take: 7 hits, 1 miss, 1 extra, 26.714 ms error; trace shapes match. `pure-results.json`, `offset-results.json`, `known-offsets.png`.
2. PASS: consumed notes cannot be hit twice; gaps create extras; skipped notes expire. Tight bass window is 78.125 ms. The full Waltz bass ghost has exactly eight one-note-per-bar hits. A live Night Bus drums run correctly reports three hits, one miss, and one extra. Pure rule, sparse take, and full race evidence.
3. PASS with listening limitation: code schedules no band notes in bars 5 to 8 and resumes on bar 9 using the unchanged clock. Full 96-note shaker take, 25 ms jitter and 4 BPM fast, has no misses or extras; slope +103.851 ms/bar, fitted 100 BPM, and 1.833 ms landing. Twenty seeded 40 ms jitter trials all read steady or uneven. Actual audio silence was not listened to because Chrome was muted.
4. PASS: steady 80 ms median is accepted exactly by the calibration helper; actual timed eight-click run measured 84.667 ms. Uneven and missing taps retain old calibration. getOutputTimestamp mapping with an 80 ms correction yields zero error. Full sequential calibration runs at 350 ms late and 90 ms early correctly clamp to 300 ms and minus 50 ms. `calibration-edge-results.json`, `targeted-results.json`.
5. PASS: 120 ms held Space with Play focused leaves the take running. Pointer press gives one tap. Repeated real CDP keydown events after the held press still yield only one tap and leave Play running after release. Keyboard-only start/tap/stop ends focused on Play. `input-results.json`, `keyboard-results.json`, `repeat-results.json`.
6. PASS: a complete Waltz bass race saves eight dots at 8.939 ms score, draws its ghost on the next take, and Clear bests removes it. Mid-race setup changes cannot save a partial best. `ghost-results.json`, targeted guard check.
7. PASS: no spoken/read entries during the live take; Read is queued and plays after Stop. traceHow is spoken once in five played takes and silent as heard four times; noTaps is spoken five times in five empty takes at a 2 s action pace. Stale results drop on Read/start. Read during the calibration introduction is uninterrupted and gives a restart instruction. Speech lifecycle tests used a short completion stub, not recorded clips. `input-results.json`, `voice-five.json`, `read-intro-results.json`.
8. PASS: required regions fit at 1366x768 and 1280x720. 680x425 has 11 px scene labels and a 120x120 pad. On the 375x812 iframe, Part ends at 279.5 px, full-width pad at 783.5 px, Play at 203.5 px. Secondary settings and detailed results scroll.
9. PASS: trace is widest and central at both requested sizes. At 1366 it is 1020x320.4 px, 48 percent of the stage height; at 680 it is 433x109 px. All four paintings read as a band above it.
10. PASS: Bass gain is zero at the 50.667 ms probe, future Bass sources are cancelled, and the station dims. Live Speed to 110 and Part to Keys preserve playback and create three dividers after the mute. Source nodes are pruned as the clock runs. Stop remains live. `mute-results.json`, `input-results.json`.

#### Wave lessons

- Hint and voice: PASS. Immediate state hints name live controls; Read uses the current hint; Curio.voice owns once/event/stale behavior. Held input and five-take logs checked. Ghost avoids the slower-speed line because Speed is locked.
- Focus and layout: PASS. No focus on load; persistent control DOM; pad focus uses preventScroll; no rebuilt buttons under a pointer. Hint space reserved.
- Sizes: PASS for core controls and target sizes. All eight standards sizes inspected, including the hosted phone. Secondary settings scroll in the shortest layouts, listed below.
- No giveaways: PASS / no hidden-answer puzzle. Performance is measured against actual chart times; no slider answers a puzzle.
- Honest numbers: PASS. Timing error and race score have different labels; misses are 150 ms in race score; no matched notes do not claim zero error. Notes document assumptions and thresholds.
- Standards: PASS. Students perform with the ensemble and rehearse from measured evidence, teaching MU:Pr5 and MU:Pr6. Missing rhythm family documentation is explicitly requested below.
- Motion off: PASS. Idle animation is disabled, station feedback changes color only, timing and trace continue. Calm frame inspected.
- Short choices visible: PASS for Part at every size. Final compact layout puts the entire mixer before Song and Speed so its short set of choices stays visible at 680x425.
- Resize mid-animation: PASS in targeted CDP testing from 1366x768 to 760x900 and back during a held key. Playback stays live, the trace remeasures to 489 px at the narrower layout, and no exception or extra tap occurs. Full audit result below.
- Welcome delayed after first tap: PASS. Multi-mode welcome has valid busy checks; Play hushes without waiting. Mode changes update hints immediately.
- Unknown as unknown: PASS / no concealed facts or diagnostic state. No-best race explicitly says no ghost yet in its result.
- One look, one meaning: PASS. Circle/triangle direction/x/gray tick distinguish pocket/early/late/miss/extra, including grayscale.
- Badge says what is true: PASS. Muted stations track the actual gain state; your own part stays fixed on. No-hit takes now say no matched notes rather than a zero-error claim.
- Hint changes back: PASS. Mode, part, take, reset, and calibration completion restore current action hints.
- No answer by copying words: PASS / performance task, no answer cards.

#### Audit leads

The full audit completed once within its 40-minute limit: 27 leads, no console exceptions, no stuck controls after resize, clean Motion off, and clean five-click narration checks. Its snapshot precedes the final repairs. All 54 audit PNGs were inspected via nine contact sheets; only affected states were shot again.

- Read target, 680 and 800 (2 leads): fixed with a 44 px minimum width. Both final measurements are 44x44 with no horizontal scroll.
- Phone iframe lookup and missing hint (2): audit infrastructure failed to acquire the child context. The hint exists. Independent drive.py hosting and a final scratch host exercise all three modes at 375x812 with explicit child-window measurements and zero console errors. Pad ends at 783.5 px, or 784.9 in Solo break. No script infrastructure was changed.
- Calibration modal covering band, part grid, trace, pad, Play, and Part controls (6): intentional. The modal blocks the underlay until Calibrate or Skip; those underlay keep-region leads are not layout failures. The dialog itself fits, and its buttons were separately corrected to cyan/dark text at 9.863:1.
- Summary only 41 percent inside the 1280 window (1): retained. The detailed summary scrolls in the panel; complete core error/count/trend results are repeated in the always-visible stage desk. Keeping the full long summary plus all main controls on one screen would reduce the required trace and pad.
- "1 extras" (1): fixed, with singular/plural labels for hits and extras. Targeted sparse takes show "1 extra" correctly.
- Pad loses focus (1): fixed with explicit preventScroll focus on pointerdown. A held pointer press now leaves focus on the pad.
- Clear bests focus and unchanged empty-state actions in Solo break/Ghost race (3): focus is explicitly retained. Clearing already-empty bests is idempotent. A real held click after scrolling the control into view removes a seeded best, reports it cleared, and retains focus. The complete ghost save/draw/clear test also passes.
- First-tap welcome absent on pad, Play, three mixer buttons, Calibrate (6): pad fixed by removing its unnecessary speech-skip marker; its welcome is now heard. Play intentionally yields to calibration/music, the mixer buttons have their own listenHow line, and Calibrate has its own calibrateHow. Skipping those welcomes is the standing first-action rule, and no welcome may talk over a take or calibration.
- Three mode welcomes cut by quick repeated taps (3): fixed. Re-selecting the same idle mode no longer hushes the line. All three 0.7-second double-tap checks now finish one welcome without a cut.
- Sound shifts four controls and cuts a welcome when muted (2): header movement fixed by a stable Sound minimum width; all five sampled header positions move zero pixels. Cutting speech on Sound off is intentional kit behavior.

Additional build fixes were checked only in affected states: sequential calibration pairing/clamps, pending calibration Read, muted-part restoration, race eligibility, early/late offscale labels, compact mixer visibility, and live status announcements. Final hosted phone checks have no favicon errors; the earlier stock-host favicon 404 belonged to the temporary host fixture, not the offline tool.


#### Frames looked at

All builder PNGs in `first-frames`, `second-frames`, `rule-frames`, `layout-frames`, `input-frames`, `final-frames`, `targeted-frames`, `guard-frames`, `night-bus-frames`, `calibration-edge-frames`, `audit-fix-frames`, `phone-clean-frames`, `presentation-frames`, and `repeat-final.png`, plus both bar frames. All audit layout/state frames were inspected through numbered audit contact sheets, with problem frames checked directly. Full standards-size sweep ran once; subsequent shots were targeted to changed states.

#### Art made

Five images, no redraws. Art totals 305,304 bytes (298.1 KiB). Final offline bundle is 486,785 bytes (475.4 KiB), under 2 MB. Raw PNGs and five WebPs present; original prompts precede the build. Second free rekey cleaned cutout holes and green edges. No paid art commands, downloaded assets, or recorded audio.

#### Art still to paint

None. No people requested or generated.

#### Engine changes wanted

Missing `kit/rhythm.js` and `docs/families/rhythm.md`. Local adapter follows Beat Buddies synthesis and clock; exact extraction/API requests are listed in `handoff.md`. Shared folders were not changed.

#### Left open

- Full audit was run once and not rerun after the final fixes. Targeted checks cover changed states; cold review is next.
- Owner headphone listening pass; every automated Chrome used --mute-audio.
- Secondary settings and detailed summary scroll in compact layouts. The phone prioritizes Play, Part, the complete stage, and full-width pad.
- Browser speech fallback until the already-listed fixed lines are recorded in a later authorized step.

All owned Chrome/server processes are closed and temporary `host.html` is removed before completion. No commit or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: band-practice

#### Played
Cold Grade 7 solo play came before the builder report, handoff, notes and source: Rehearse, a full Solo break and a full Ghost race, including wrong taps. The large trace and missing-part audio give the practice a purpose. Checked the projection view against Beat Lab and Snowy Mail Route without changing those tools.

#### Findings fixed
- Blocker, family:rhythm, `receiveTap`: a late drifting bass tap could match one note but sound a later note or chord. Sound now follows the matched chart position. Browser oscillator test confirms the fifth instead of the octave.
- Blocker, family:rhythm, `updateGhost`: the comparison used differently settled portions of the performances and stopped updating when notes were missed. It now compares the same resolved chart notes and updates on expiration. A silent player correctly falls 150 ms behind the zero-error ghost.
- Should fix, general, result desk: Solo break hid its fitted tempo and landing below the panel fold; Ghost race foregrounded hit-only error rather than its penalized race score. Both now show their own earned result beside the pad, including on the phone.
- Should fix, general, stopped setup changes: a new Song or Part relabeled the old trace and summary. Stopped Song, Part and Speed changes now clear that evidence and select the correct ghost.
- Should fix, general, instructions: Ghost race could recommend its disabled Speed slider. That recommendation is now limited to modes where Speed is available. Mixer narration cannot say fewer players after everyone is restored; Clear bests names the appropriate next mode and confirms the action beside the pad, even with its panel scrolled.
- Should fix, general, stale state: mode/start transitions clear old feedback and color; quiet mode changes discard pending Read. A zero average now says with the band.
- Should fix, general, trace: dense offscale numbers covered notes in compact views, and late bar averages could cover the footer. Compact annotations now show a range and count, with every exact value in the trace title and accessible description. Plot margins keep averages clear of the footer.
- Polish, graphics: redrew the oversized shaker as a hand-sized wooden egg on a worn stool, retaining the room's painted style and warm light. The other four paintings remain.
- Updated notes, handoff and audit states for the revised result presentation. No new music topics or modes.

Independent checks: 24 browser rule checks passed; 40 ms early, 40 ms late and zero keep the right signs; sparse Waltz bass gives 7 hits, 1 miss and 1 extra, with 18.75 ms race error. Ghost save/load/improve/clear and phase-preserving Speed/Part/mute changes passed.

Recomputed the spec's durations, 4.2 s calibration span, 78.125 ms tight window, t critical values, drift examples and WCAG ratios in Python. Cyan/background is 9.863:1; ink/background 15.972:1; muted/background 7.130:1. The browser fit independently gives 99.802 BPM, displayed as 100. Seeded 3,000-trial steady conditions give 95.2 to 100 percent steady/uneven; the separate twenty-run check had no false directional calls.

A complete real-clock Solo break had 96 hits, no misses or extras, zero scheduled band notes in bars 5 to 8, and a 0 ms return-clock error. The fitted fast player read 100 against 96. Actual held Space, repeat suppression, J/F, pointerdown, pad focus and keyboard-only start/tap/stop passed. No network requests or runtime exceptions in that run. An actual eight-click calibration accepted 80 ms; uneven/clamp/timestamp tests passed.

Voice checks use the kit log. Counts below used a short speech-completion stub at a two-second action pace; the final audit uses browser narration.

| Line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| traceHow | how, five takes | 1 | 1 |
| noTaps | event, five takes | 5 | 5 |

Read waited through a take, spoke after Stop and worked with Sound off. No narration started during the full clocked take. All 19 fixed narration strings match `voice/lines.json`.

#### Findings left
No confirmed blocker or should-fix remains. The audit's 16 mechanical leads were checked: six are the modal intentionally covering its underlay; five are welcomes skipped for Play, the three mixer how-to lines and calibration; five are Clear bests focus/unchanged flags across the three modes. Real held clicks after scrolling that button into view clear a seeded best, retain focus and keep the button visible in every mode. The unscrolled audit coordinates do not exercise that control. The direct frames did confirm that its hint could be above the scrolled panel; that confirmation is now repeated visibly beside the pad. Existing recording/engine limitations are listed below.

#### Flattest moment left
Night Bus drums has one playable hit per bar. It is the least busy role, but retaining that space is the specified one-drop ensemble lesson. The formerly flat Solo break result now lands visibly beside the pad.

#### Graphics
All five finished paintings were inspected individually and in use: room, drums, bass, keys and shaker. One redrawn, none missing, none containing people. Built-in image generation; full house style and replacement asset prompt are in `art/prompts.json`, with selected raw art at `art/raw/shaker.png`. Final painting: `art/shaker.webp`.
Final art 290,938 bytes (284.1 KiB); final offline bundle 472,416 bytes (461.3 KiB). No missing art or network dependencies.
Changed preview, laptop, grayscale, Motion off and 375 px iframe frames were opened. Audit frames were inspected through numbered contact sheets, with problem frames opened directly. The central trace and painted band were retained, not flattened.

#### Audit
Completed once within its 40-minute limit. `review-audit/audit.md` records 16 leads, all answered above. All eight size checks, listed states, Motion off, repeated speech and quick taps were clean. Resize stress completed without exceptions or disabled controls left stuck. All 61 audit PNGs were opened via 16 contact sheets; modal and result frames were also inspected directly. The audit predates only the two-line visible Clear bests confirmation fix. Its three affected mode frames were re-shot with held clicks, successful clearing, retained focus, visible feedback and no console errors. No second audit or polish round.

#### Left open
- No narration recordings or unmuted headphone listening judgment. Browser speech is the existing fallback; every test Chrome used mute-audio, as required.
- The absent shared rhythm engine/document remain the precisely described requests in `handoff.md`; kit and docs were outside the write scope.
- Compact layouts scroll secondary settings and the long summary. Play, Part, the trace and 120 px pad stay visible; the phone pad ends at 783.5 px in its 812 px host.
- Ghost race's exclusion of extra taps from its score is specified and retained; extras remain visible. Compact offscale numbers are grouped on canvas, with exact values retained in the title and accessible description.
- One cold review pass, then affected rechecks and one final audit. Only `tools/band-practice/` and `_scratch/band-practice/` were authored. No commits, shared-file changes, or leftover owned Chrome/server processes.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Band Practice handoff

#### Cold review changes, 2026-11-03

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

#### Source map

`src.html` starts from the kit starter structure. It uses kit:curio CSS, Curio.init, Curio.voice, and the shared Sound and Motion settings. The responsive stage uses real CSS pixel sizes instead of scaling a fixed scene. The styles, semantic stage and controls, song data, local audio adapter, timing model, canvas renderer, and handlers appear in that order.

`SONGS` contains the exact three patterns and chord lists, indexed from zero. `CHORDS` supplies close keyboard voicings and bass roots. The student's entire instrument station is absent from the backing audio. Each press sounds the next expected part note immediately; no tap is quantized.

`window.__tool` exposes state, timing/statistics helpers, audio context, gains, source nodes, calibration, bests, and narration logs for cold review. It is a diagnostic hook, not a student control.

#### Timing and tricky parts

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

#### Art

Five generated paintings are present and used: room, drums, bass and amplifier, keyboard on X stand, shaker on stool. No people. Prompts include house style and `drawn_by: codex`; raw PNGs are retained as required. `art.py --rekey` made the WebPs. A second rekey enabled holes and despill to clean green fringing; no image needed redrawing.

#### Choices and open questions

The spec has no explicit open-question list. Used the specified easy-coach voice, original song tempos, moving break windows, eight-bar ghosts, and saved device calibration. The user's image-tool direction supersedes the spec's older local FLUX route.

The family engine and family document are absent. The build brief prohibits writing kit or docs, so the Beat Buddies audio synthesis and clock are adapted locally. This is the only shared-engine exception; it is not a new music topic.

At 375 wide, Play and Part controls precede the band and the full-width pad is visible by 784 px. Song, Speed, mixer, calibration, and detailed results continue down the page. At compact landscape sizes those secondary controls scroll in the side panel. Core results also appear in the lower stage desk so a stopped take is useful without scrolling the longer summary.

#### Engine changes wanted

- New `kit/rhythm.js`, based on `tools/beat-buddies/src.html` audio(), tone(), pluck(), noise(), SND, at(), startClock(), stopClock(). Preserve the compressor, room routing, source lifecycle, and audible timbre.
- `startClock(bpm, step, {lead, steps:4})`: add configurable steps per beat and phase-preserving rescheduling for live changes. Track per-part source nodes so mute can cancel scheduled notes and ramp a part gain over 20 ms.
- `tapTime(event)`: use getOutputTimestamp mapping, fallback currentTime, then subtract the saved calibration. Export latency get/set/reset, using the shared localStorage key and documenting seconds as the storage unit.
- `judge(t, expected, maxWin)`: nearest unmatched expected note, capped by neighboring gaps, with moving-window support as an option for silent breaks. Return the original-clock offset.
- `fitLine(xs,ys)`: least-squares slope/intercept and slope standard error. The spec's trend and tempo reporting need both.
- New `docs/families/rhythm.md`: document these APIs before siblings depend on the engine. Neither shared path was written in this build.

#### Cold review notes

Evidence and temporary scripts are in `_scratch/band-practice/`. Read the final report for exact coverage and audit leads. Audio test Chromes were muted, so timbre and headphone feel still deserve an owner's listening pass. Voice recordings were intentionally not generated; all 19 fixed lines use the kit's browser fallback until recorded.

The numerical recheck reproduces the current trend rule, contrast, durations, matching window, and tempo examples. The spec's old-rule false-positive range is narrower than the recomputed range across all its listed parts; see the report. No specification file was edited.

The full mechanical audit completed once with 27 leads. Concrete target/focus/header/repeated-mode issues were repaired and checked with held clicks in `audit-fix-frames`. Modal underlay coverage and the scrolling detailed summary are intentional. The auditor could not acquire the phone iframe context; independent drive.py host checks and final clean scratch-host checks cover all three modes at 375x812. Full audit was not rerun after fixes. Its report and all 54 frame originals remain in Scratch.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
