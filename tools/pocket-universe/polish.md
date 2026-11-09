# Polish: pocket-universe (Codex fix, round 1)


Owner-approved instrument pivot. Items 1-6 are fixed. Item 7 remains NOT FIXED for the full-budget 60 fps requirement.
Local test-server cleanup is blocked by Windows permissions. All evidence below is in `_scratch/pocket-universe/` relative to the repository root.

## Blocker

None listed.

## Should fix

None listed.

## Pivot items

1. FIXED: sky front door, one throw hint, tray, no target or count. Before: `before-frames/before-pocket-1366x768.png`; after: `final-smoke-frames/last-default-1366-final.png`, `proof-frames/final-phone.png`. Stage width increased from 1076 to 1366 px at 1366x768; the compact view uses all 680 px.
2. FIXED: removed detectors, award events/chime, sticker book, counters and new sticker persistence. Twenty-four facts are unlocked, unnumbered Manual field notes. Before: `before-frames/before-goals.png`; after: `proof-frames/final-field-notes.png`. `exercise/results.json`: 24 notes, zero obsolete controls, store keys only `saves`; no progress after cheap input patterns.
3. FIXED: Wonders is now Setups, opened from the console or Manual, including the figure eight, Two suns and a fresh Real Solar System. Before: `before-frames/before-wonders.png`; after: `final-state-frames/setups-680x425.png`, `final-state-frames/setups-375x812.png`. All eight loads fit those frames; the audit-discovered intermediate-size cutoff is also fixed, with zero hidden loads and zero scroll overflow at 1000x625 and 1280x720 (`late-proof-frames/`, `setups-fixed-*.json`). Native cross-mode Undo restored Real with nine bodies.
4. FIXED: removed the kit header and right pill panel; made an edge console, rotary Time dial, rewind tape and ruled monospace telemetry. Before: `before-frames/before-selected.png`; after: `proof-frames/final-selected-1366.png`, `proof-frames/final-selected-680.png`. Pocket: 10 pocket u, 201.0 px/s, 250.0 world px, parent and laps. Real: 5.969e24 kg, 30.29 km/s, 0.9833 AU. Reference frame is explicit.
5. FIXED: lower-left Manual and engraved family plate, console power panel, two-position universe switch. Before: `before-frames/before-pocket-1366x768.png`; after: `final-smoke-frames/last-default-1366-final.png`, `proof-frames/final-phone.png`. The phone plate and privacy line have their own rows. Keyboard Manual notes are reachable; Escape restores Manual focus.
6. FIXED: retained visible exaggerated Pocket ratios, Drawn bigger than life, True size and the whirl boundary. After: `proof-frames/final-real-680.png`, `proof-frames/final-true-phone.png`, `final-state-frames/motion-off-1366x768.png`. Physical Earth diameter was measured directly from drawImage and matched computed scale to floating-point precision; see `exercise/results.json` and the final size check below.
7. NOT FIXED: the 60 fps full-budget target is not proven. All eight sizes in both modes, keyboard input, contrast, Motion off, Read, one offline file and revised control names passed their targeted checks. Best full-budget observation at 1366x768 and four-times CPU throttle: 20 masses, 160 motes, 18.74 ms/frame (about 53 fps), with achieved speed visibly below requested x4. See `final-checks/results.json`. A slower adaptive-budget trial was reverted. No 60 fps claim is made.

## Polish accepted

None listed separately.

## Settled calls

Applied: Gravity, Ghost, trails, Follow, Save and My universes remain. Their drawers and keyboard paths work.
Native Enter / Ctrl+Z / Enter repeated all 30 Dust motes exactly, preserving focus on the Dust chip.
Actual Save, page reload and Replay ended at step 1440 with identical bodies. Real Clear retained Real units.
Rescue: original Moon crashed before 16 s; rewind, reselect Moon and five Slower taps kept it for 11 laps at 16 s.
Evidence: `exercise/results.json`, `final-checks/results.json`, `final-checks/replay-endpoint.png`, `final-checks/rescue-after-rewind.png`.

## Cheats tried

- Sweep Time and Gravity while paused; alternate Faster/Slower and Heavier/Lighter 30 times: zero elapsed time, zero laps, zero goal controls, no progress key or award. `exercise/results.json`, cheap-paused-sweeps.
- Cycle famous setups and advance them, then open every field note: all 24 notes are freely available, no counter, earned state or sticker namespace. Reading them is the intended field-guide use, with no pass condition. `exercise/results.json`, cheap-loads-and-manual.
- Let Starter run for 16 world seconds: exactly two completed laps. Turn Gravity off: parent and laps read n/a. No way to bank a best or pass from the readout. `exercise/results.json`, lap-readout.
- Set the Time dial repeatedly while paused: requested rate can change, but RUN is zero and world time stays fixed. The setter no longer substitutes requested speed for a measurement. Final single-shot result: requested 16x, RUN 0x, elapsed 0, store keys only saves (`meter-cheats.json`, `last-number-frames/meter-cheats.png`).
- Legacy sticker data with a named saved universe: the universe name survives; new store keys contain only saves. `exercise/results.json`, legacy-migration.

## Voice walk

Held clicks, 120 ms, at a two-second pace. Main path: tray selection and real drag, then Real and the Time dial.
Side path: Manual, first field note, Manual's Setups, Three-body dance. Logged once each, in order:
Pocket welcome; Real welcome naming the Time dial; Manual introduction; Falling and missing fact; dance intro naming Body.
Read with Sound off logged the current hint. No goal or removed-control line remains. Motion off: zero running infinite animations.
The manifest and runtime allLines match exactly: 77 unique fixed lines. Browser fallback is retained; no recordings made or audible quality claim.
Evidence: `final-checks/results.json`, final-voice-walk, read-with-sound-off, motion-off; `verification.json`.

## Engine changes wanted

No production kit or numerical-integrator change. The NBODY block is byte-for-byte unchanged:
`af34a7e5edf6856f5553bc81b754e744af93c98315c087dd2b8282149eabb85e`.
Shared test-harness request: `scripts/drive.py`, HOST, add an inline empty favicon to its generated parent page.
Additional harness requests: `scripts/audit_tool.py`, MODES_JS, recognize console `.mode-switch` buttons;
PAGE_JS vis, skip unpainted descendants of native closed details. No shared scripts were changed.
The parent host's favicon.ico 404 appears in iframe batches. Standalone tool checks have zero HTTP(S) requests and zero exceptions.

## Model, sources and checks

Updated the approved spec sections Goals, Screens and modes, Look and Teacher note, plus contradictory first-minute, voice and Done when references. The final Real welcome is 49 characters.
Open questions were left unchanged. All 27 existing paintings remain; no new topic, score, art or finish condition was added.
JPL J2000 initialization and NASA masses/diameters are unchanged. Real conversion uses 15,882,691.439 physical seconds per world second.
Independent checks: finite-mass circle speed 200.997512 px/s, period 7.815004 s; Earth mass 5.969477e24 kg;
Earth diameter 0.0085268593 world px. Parent-relative quantities are explained in the Manual and notes.
Sources: existing spec sources, NASA Planetary/Sun Fact Sheets, JPL Approximate Positions Table 1 and OpenStax chapter 13.
Measured contrasts: normal 16.29:1, muted on the lightest console 6.79:1, maker plate 8.32:1, buttons 9.94:1,
button boundary 3.45:1, focus 10.32:1. Source lines over 160 characters: zero. Em dashes: zero.
`verification.json` covers 16 mode/size combinations: no page scroll, tray overflow, outside primary control or obsolete goal control.
Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 375x812 in the required host.
The final bundle is about 633 KiB, with embedded art and browser narration fallback. No commits or shared-file changes.

## Feel check

Best moment: a real jittered held drag bends a ghost around the star, then release starts its own colored trail.
Two flat moments addressed: the old goal/panel frame became an edge console; cramped preview orbits got usable sky margins.
The painted sky, sprites, luminous trails, pulsing stars and quiet sky life remain. Layered glow replaces costly per-trail blur.
Both bar tools were opened read-only. Pocket Universe keeps the density and material of an instrument without copying their scene.

| Pocket Universe | Beat Lab |
|---|---|
| ![Pocket Universe](../../_scratch/pocket-universe/final-smoke-frames/last-default-1366-final.png) | ![Beat Lab](../../_scratch/pocket-universe/proof-frames/bar-beat-lab.png) |

## Audit

Completed once within the 40-minute deadline, exit 0, on Chrome 9921 / host 8725: `fix-audit/audit.md`.
Its 247 leads have individual dispositions in `audit-lead-ledger.json`: 245 expected, two confirmed and fixed.

- Expected: 180 overlap and 61 hidden-text reports concern the canvas under HUD/drawers, inactive controls behind a modal, or unpainted native closed-details text. Frames show readable foreground content and visible Close/Cancel controls.
- FIXED: Setups hid its last two choices at 1000x625. Expanded its book height through 720px; all 8 choices are visible, with 0 hidden and 0 scroll overflow at 1000x625, 1280x720 and 680x425. Before: `fix-audit/state-setups-book-1000x625.png`; after: `late-proof-frames/setups-fixed-1000x625.png` and companion sizes.
- FIXED: the 119-character Real welcome delayed True size until that instruction became stale, even at two-second input pacing. Reduced it to 49 characters. `late-voice-drive.log` and `true-size-voice-paced.json`: real and trueSize both spoken once, with no cut; the how-to starts at 9.983 s before the size toggle.
- Expected: four first-tap welcome flags are Save's own event or books whose context hides the throw controls. STANDARDS requires skipping that generic welcome, unmarked, rather than speaking it over the current action.
The audit used a frozen input, retained as `audit-input.html`. Narrow fixes were checked against a separate Scratch bundle, then the final normal bundle and final 1366 default/Real frames were checked. No second full audit or fresh lenses.
Scope: MODES_JS only searches header controls and found zero automatic modes; independent tests cover both modes at all eight sizes. Listed phone states used an old friendly size label and were skipped; their metadata is now normalized to 375x812 for the next audit. The existing phone proofs are separate evidence.
Supplement: the power panel no longer shifts when Sound changes (all three x coordinates unchanged at 680x425). Mode-switch setup loading preserves both worlds, including Pocket time (`last-smoke-summary.json`, `setup-mode-memory.json`).
The 60 fps target remains NOT FIXED. This is not a clean full-gate claim.

## Not done

- Local test server on 127.0.0.1:8725 remains running. Its command line was verified as this task's drive.py host, PID 54024. Windows returned Access denied on termination; no permission escalation was attempted. All Chrome debugging ports are closed. See `host-owner-identity.json`.
- Full-budget 60 fps remains unproven. Further renderer/compositor work and another measurement are needed; keep the numerical engine unchanged.
- A fresh ten-minute student play check was not rerun in this one fix pass. No fresh lenses were launched.

## Left open

Unattended decisions: use the approved instrument pivot over the old game frame; put Manual in the lower-left family corner;
make every field note freely readable; show parent-relative telemetry with an explicit origin fallback.
The last two-shot number batch lost Chrome/CDP; it was retried once as smaller single-shot commands.
Final size check at 680x425: measured Earth diameter 0.004564377643047484 px; computed 0.004564377643047695 px; label 0.0046 px (`final-size-number.json`).
The final 77-line manifest matches runtime in both final 1366 frames and the mode-memory check. The last pair reports zero errors.
All 119 generated before/after, intermediate and audit frames were inspected, using native critical frames and ten contact sheets (`qa-frame-index.json`, `qa-sheets/`).
Generated host cleanup: removed (verified absent). Remaining test ports: [8725].
Final bundle: 648,641 bytes. `final-manifest.json` records exact file and frozen-audit hashes.
