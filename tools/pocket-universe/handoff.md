# Pocket Universe: instrument handoff

Owner-approved pivot, 4 November 2026. The source now frames the existing gravity sandbox as mission control.
There are no goals, award detectors, sticker events, progress counters or sticker storage in new saves.
The 24 existing concepts live as unnumbered, unlocked Manual field notes. Setups includes a fresh Real Solar System.
The seven pivot items and their evidence are recorded in polish.md. The performance requirement is not fully met.

## Source map
src.html contains the instrument CSS and console, the unchanged NBODY numerical block, observational orbit tracking,
the tray/planet/finding tables, storage and timelines, drawing and sound, scheduling, readouts, drawers and input.
__tool exposes world/state, NBODY, measureOrbits, timelines, findings, setup loaders, allLines and vlog for checks.
The source remains readable, with no lines over 160 characters and no em dashes. All 27 paintings are retained.

## Console and drawers
The sky spans the viewport. The canvas covers the visible sky above the edge console, avoiding hidden raster work.
The camera uses real pixels and adapts its usable sky margins in short windows. Every main control fits at all
eight STANDARDS sizes. The phone is tested through the required 375x812 iframe host.
The lower-left Manual sits beside the No. 02 maker's plate. World and Body fold upward, with Close and Escape.
Short-window drawers use the available height. Setups shows all eight loads at once on the phone and short preview.
Manual notes scroll inside the book; their summaries are keyboard reachable. Escape restores the Manual button.
The console precedes the canvas in keyboard order. The clock, time dial, tape and tray remain available on the edge.

## Physics and readouts
The NBODY block is byte-for-byte identical to the received source. Engine SHA-256:
af34a7e5edf6856f5553bc81b754e744af93c98315c087dd2b8282149eabb85e
measureOrbits tracks parent and signed angular accumulation for lap readouts and sound, with no pass/fail condition.
Parent remains the nearest bound body at least three times heavier. Speed/distance are relative to that parent,
or to the explicitly labeled simulation origin if none exists. Laps reset when the parent changes.
Pocket uses pocket u, world px and px/s. Real converts to kg, AU and km/s using the original model time scale.
True size still draws the physical diameter, separate from the locating ring; its Earth label follows actual zoom.
Pocket's exaggerated ratios, the Real size label and the whirl's distributed-mass boundary stay in the sky.

## Saves and deterministic timelines
The localStorage key and gzip wrapper are unchanged. Legacy named saves remain readable. Their retired sticker
namespace is ignored and omitted on the next write. New stores contain only saves. Save thumbnails preserve aspect.
Actual Save / reload / Replay returned exactly to step 1440 with identical bodies. Real Clear keeps Real units;
Undo crosses a setup's mode boundary correctly. A real Enter / Ctrl+Z / Enter repeated all 30 Dust motes exactly,
including IDs, positions and velocities, with focus retained. Rewind, reselect Moon, Slower five times: 11 laps at 16 s.

## Narration and access
The Leda/casual-peer bank is retained, through Curio.voice. Seventy-seven manifest lines equal runtime allLines.
Removed controls have no remaining spoken references. Body/World directions name their drawers. Real names the Time dial.
Held clicks at a two-second pace logged the Pocket/Real welcomes, Manual, a field note and the dance intro once each.
Read works with Sound off. Motion off has no running infinite decoration; physical motion continues as content.
Text, muted text, maker plate and button text contrast ratios are 16.29, 6.79, 8.32 and 9.94 to one.
Narration uses the existing browser fallback; no recordings were generated or judged by ear in muted Chrome.

## Performance and not done
The expensive per-trail canvas shadow blur was replaced with layered luminous strokes, retaining the painted sky,
glowing paths and sprites. Hidden canvas area is no longer rasterized. Physics scheduling yields after each fixed
step and reports achieved speed as RUN beside requested TIME. A requested rate is never substituted for a measurement.
The best observed full-budget 1366x768 run at four-times CPU throttle was 18.74 ms/frame, about 53 fps,
with 20 masses and all 160 motes. It reported the lower achieved world speed. This does not prove the 60 fps target.
An adaptive-budget trial was slower and was reverted. Further work belongs in this tool's renderer/scheduler,
with compositor-aware profiling and another full-budget measurement. The numerical integrator must stay unchanged.

## Evidence
Current Scratch: S:/CurioClass-codex/_scratch/pocket-universe/.
before-frames and before-src.html preserve the received front door, goals, Wonders, mode and telemetry.
final-frames covers both modes at all sizes. final-state-frames and proof-frames cover the drawers, notes, units,
True size, Motion off and grayscale. final-checks/results.json and exercise/results.json contain native-input checks.
verification.json recomputes units, contrasts, source/engine checks and layout bounds. fix-audit is the final audit.
Historical build/review reports remain in this tool folder; the former handoff is preserved in Scratch.

## Engine changes wanted
No production kit or numerical-engine change is requested. Shared test-harness request only:
scripts/drive.py, HOST: add an inline empty favicon to the generated parent host. Its favicon.ico 404 is emitted
by that test host, not by the tool. Standalone tool checks show no HTTP(S) requests and no exceptions.
Shared scripts remain unchanged.

## Decisions taken unattended
The approved instrument decision overrides the old game spec. Its affected sections, first minute, voice and
Done when references now describe the implementation. Open questions were left alone.
Manual is in the lower-left family corner. All field notes are freely readable, never a hidden achievement list.
Speed/distance use an explicit physical reference frame. No new art, topic, score or finish condition was added.
No commits, shared-file changes, uploads or deployments were made.

## Fix audit exit
The single full audit completed, producing 247 leads and 33 frames. Every lead has a disposition in Scratch/
audit-lead-ledger.json: 245 expected canvas/drawer/native-details/first-tap layers, and two defects fixed with
focused proofs. Setups now shows all eight loads without scrolling at 1000x625, 1280x720 and 680x425.
The Real welcome is now 49 characters, so the two-second held-click path speaks True size at its live moment.
The full audit input was frozen in Scratch/audit-input.html while these narrow fixes were checked separately.
Final default and Real 1366x768 frames, phone bounds, voice manifest and setup-mode memory were rechecked.
Power buttons keep a fixed 68 px footprint, with zero movement when Sound changes. An open drawer suppresses
an unrelated throw welcome. Loading a setup in the other mode retains the previous mode's bodies and time.

The audit mode finder only recognizes header groups, so it detected zero automatic modes in this instrument.
Both modes nevertheless have independent eight-size coverage. The old pretty phone size label silently skipped
the listed phone states; audit-states.json now uses the actual 375x812 name for the next run. Existing phone
proofs cover the front door, Real, Body, Setups and True size. Do not claim this audit covers the final bundle in full.
Additional shared harness requests: scripts/audit_tool.py, MODES_JS, recognize .mode-switch buttons; PAGE_JS vis,
ignore the unpainted descendants of native closed details rather than treating their layout boxes as visible text.
The full-budget 60 fps requirement is still open, as stated above. No fresh lenses or second full audit were run.

## Test-server cleanup blocked
All Chrome debugging ports are closed and tools/pocket-universe/host.html was removed. The hidden local server
on 127.0.0.1:8725, PID 54024, remains running. Its command line was verified as this task's drive.py --host
process, but Windows denied termination. No permission escalation was attempted. Identity is preserved in
Scratch/host-owner-identity.json. This resource cleanup remains open for the next operator.
