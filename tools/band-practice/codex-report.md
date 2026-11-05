# Codex report: band-practice

## Built

Build only in `S:\CurioClass-codex`. All authored files are in `tools/band-practice/` and `_scratch/band-practice/`. No git operations, commits, shared-engine writes, deployment, or polish round.

Three modes, three exact original song charts, four playable parts, unquantized synthesized instruments, live listening controls, per-press timing trace, misses/extras, signed averages, bar averages and trends, calibration, silent break with landing, and saved per-song/part ghosts. Five generated paintings are placed. Core results are repeated in the stage desk so they remain useful without scrolling the detailed summary.

Uses the kit starter structure, kit CSS, Curio.init, Curio.voice, Sound and Motion. No network dependencies or microphone recording. Voice bank easy-coach, Umbriel, 19 fixed lines. Browser speech fallback is intentional; no recordings were made.

## Numbers check

`_scratch/band-practice/recompute.py` and `numbers.json` recompute the source examples with NumPy and SciPy, including 3,000 trials per condition using the actual part positions.

- t critical values: 4.3027, 2.4469, 2.0739, 2.0423 for 4, 8, 24, 32 notes.
- One BPM fast: 25.773, 41.012, 65.574, 10.253 ms/bar at the specified tempos and meters. 101 against 96: 123.762 ms/bar.
- Tightest window: 78.125 ms. Eight calibration clicks span 4.2 s.
- Solo durations: 30.0, 37.895, 48.0, 16.364 s. Ghost durations: 20.0, 25.263, 10.909 s.
- Contrast on background: cyan 9.863:1, ink 15.972:1, muted 7.130:1, early 7.786:1, late 6.737:1, pocket 11.712:1. Ink/panel 14.369:1; muted/panel 6.414:1.
- Current trend rule correctly avoids a direction in 95.17 to 100 percent of steady trials. Four BPM fast/slow is detected in 97.67 to 100 percent of tested 4/4 conditions. Waltz bass ranges from 14.63 to 93.17 percent and has limited power, as the spec explains.
- Difference from spec: the old 5 ms/bar rule falsely reports a direction in 19.77 to 79.23 percent across all listed parts, rather than the stated 52 to 79 percent. The lower end is the dense shaker part. One sparse Waltz condition reached 0.133 percent wrong direction in this independent seed, slightly above the spec's 0.1 percent wording. These are Monte Carlo differences; the current rule was implemented as specified. The spec was not edited.

`verify_sources.py` independently recomputed the browser take summary and fitted tempo in Python. Its timing-rule assertions pass.

## Feel check

Played held controls and keys, free takes, and complete timed Solo break and Ghost race runs. Best moment: the early shaker dots rise beyond the trace edge during silence, then the returning band lands against the same clock. The break reports rushed, about 100 BPM against 96, with a 2 ms landing in the measured full run.

Two flattest moments and build fixes:

1. The first band strip cropped the instruments into fragments. Fixed the image sizing, cleaned green edges with holes/despill, changed the background crop to show the room, and enlarged the laptop strip while retaining the trace's prominence.
2. Stop originally left the last tap label visible while its real summary sat low in the panel. The stage desk now shows timing error, hits/misses/extras, and average or break trend at once. Offscale labels also use staggered lanes instead of overlapping.

The room and instrument material detail hold up beside the bar tools; the chart is deliberately an accurate work surface. Audio was muted in every automated Chrome, so an actual headphone listening judgment remains open. No claim of a ten-minute listening playtest.

Side-by-side comparison is `_scratch/band-practice/comparison.html`, showing a scripted Band Practice trace beside Beat Lab. Both Beat Lab and Snowy Mail Route were opened before implementation.

| Band Practice | Beat Lab finish reference |
|---|---|
| ![Band Practice](../../_scratch/band-practice/presentation-frames/final-take-frame.png) | ![Beat Lab](../../_scratch/band-practice/bar-frames/beat-lab.png) |

## Done when

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

## Wave lessons

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

## Audit leads

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


## Frames looked at

All builder PNGs in `first-frames`, `second-frames`, `rule-frames`, `layout-frames`, `input-frames`, `final-frames`, `targeted-frames`, `guard-frames`, `night-bus-frames`, `calibration-edge-frames`, `audit-fix-frames`, `phone-clean-frames`, `presentation-frames`, and `repeat-final.png`, plus both bar frames. All audit layout/state frames were inspected through numbered audit contact sheets, with problem frames checked directly. Full standards-size sweep ran once; subsequent shots were targeted to changed states.

## Art made

Five images, no redraws. Art totals 305,304 bytes (298.1 KiB). Final offline bundle is 486,785 bytes (475.4 KiB), under 2 MB. Raw PNGs and five WebPs present; original prompts precede the build. Second free rekey cleaned cutout holes and green edges. No paid art commands, downloaded assets, or recorded audio.

## Art still to paint

None. No people requested or generated.

## Engine changes wanted

Missing `kit/rhythm.js` and `docs/families/rhythm.md`. Local adapter follows Beat Buddies synthesis and clock; exact extraction/API requests are listed in `handoff.md`. Shared folders were not changed.

## Left open

- Full audit was run once and not rerun after the final fixes. Targeted checks cover changed states; cold review is next.
- Owner headphone listening pass; every automated Chrome used --mute-audio.
- Secondary settings and detailed summary scroll in compact layouts. The phone prioritizes Play, Part, the complete stage, and full-width pad.
- Browser speech fallback until the already-listed fixed lines are recorded in a later authorized step.

All owned Chrome/server processes are closed and temporary `host.html` is removed before completion. No commit or polish round.
