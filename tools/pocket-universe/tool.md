# Pocket Universe: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: pocket-universe
#### Built
Build only, in S:/CurioClass-codex-pocket-universe/tools/pocket-universe/.
No commits, branch changes, shared-kit changes, art generation, recordings or polish round.
The self-contained draft is 152598 bytes; readable source has 2840 lines, none over 160 characters.
Pocket and Real Solar System, 24 discovery stickers, seven loads including Empty/Starter, live prediction,
150-second tape, branching ghosts, Undo, local saves/replay, keyboard input and synthesized sound are implemented.
The 27 art tokens are laid out and preloaded. Paintings and recordings remain absent, as instructed.
The owned Chrome ports were 9990-9994; the only host port was 8795. All owned browsers and servers were closed.

#### Numbers check
Evidence: S:/CurioClass-codex-scratch/pocket-universe/numbers.json and numeric-results.json.
Independent Python constants/periods/radii/contrast checks plus 38 passing model assertions.
All 24 goal detectors were reached using real integrations; successful search starts are frozen in the results.
Starter: separation 250.000000-250.009801 px over 30 s; period 7.815004 s.
Rescue: original crash 15.747917 s; five Slower taps earns Rescue within 15 s; five Faster taps crashes at 2.933333 s.
Mars's first direction reversal is at world time 2.733333 s, in May 2001; five Venus passes occur by 2007.
Neptune's two-body period is 327.625983 world seconds, about 20.48 s at a fully achieved x16.
Earth's true diameter is 0.00852686 world px at 100 px/AU; its on-screen label also accounts for zoom.
Jupiter/Sun mass ratio is 1/1047.68177; Giant/Planet Hill radii at 300 px are 96.54894/44.81405 px.
38 assertions include momentum conservation, deterministic replay, gravity off, moons, ring, binary, Trojan,
capture, slingshot, Grand tour, black-hole equivalence, Figure eight, moving-frame prediction and star mass limits.
Contrast: brand/panel 8.93:1; brand/section 8.23:1; brand ink/brand 9.25:1; text/panel 16.29:1; muted/panel 7.90:1.
Source discrepancy: the finite Planet mass gives circle speed 200.9975 and escape 284.2534 px/s at 250 px.
The lone-star test-particle circle is 200.0, rather than the source's 200.3. Some example numbers mix conventions.
Halving the Starter star alone leaves its planet slightly bound. One Faster nudge before halving releases it.
The Lightweight finding was corrected to that fact; spec.md was left unchanged.
Whirl dust already beyond 4000 px is dropped. At Gravity 0.45, every remaining mote is beyond 1500 px by 20 s.
The source agent's retrospective random-trial counts and every quoted error estimate were not reproduced exactly.

#### Feel check
Yes, I would keep experimenting after ten minutes: a small nudge can rescue a moon or change a shared orbit.
The required fresh-agent proxy actually played for 10m10s, still wanted to play and earned eight discoveries.
Its best moment was making a binary from Empty, naming it Twin Fireflies, saving and replaying it.
It could explain how sideways speed and gravity combine to bend a path. This was not a human student study.
The two flattest moments were an empty field after escapes and ten seconds of waiting before a replay's first throw.
Changed: off-screen recovery now names World > Fit and 0, and changes back after recovery; quiet replay intervals
show a countdown and name x4. The recorded waiting time is preserved rather than silently changing the replay.
Other build fixes: flush the last quick drag prediction, draw ghosts/trails in the Follow frame, expose all nine
body buttons in the preview, show all seven Wonders, and keep hints visible when the panel scrolls.
Comparison: Scratch/feel-comparison.png places the nudged dance beside Beat Lab. Trails, motion and feedback have
visual depth; the missing painted sky and disks remain visibly plainer than finished art. No finished-art parity claim.
Sound was muted in every test, as required, so audible quality was not judged by ear.

#### Done when
1. PASS: Starter already moves; real held drags hold time, show a live ghost and launch on release. Final aim frame
   shows the 300 px/s escape prediction after the last quick movement, rather than the earlier at-rest crash path.
2. PASS: drag 40 crashes at 1.533 s; drag 100 orbits; drag 150 passes 1500 px and gets an edge arrow.
   Snapshot/restore plus the same step sequence reproduces body data exactly.
3. PASS: Rescue, five Slower taps and the faster-crash contrast match the numerical checks above.
4. PASS: every detector 1-24 reached; representative UI discoveries contain actual 160x100 trail snapshots.
5. PASS: J2000 start, May 2001 Mars reversal, five Venus passes/flower by late 2007, true radii and real periods.
   Wall-clock periods lengthen whenever the tool explicitly reports a reduced achieved speed.
6. PASS: scene dominates laptop and preview; tray/time bar are visible at every required size, including the 375 host.
   Scene labels are at least 10 px. Advanced portrait panels scroll below them, as the specified stack requires.
7. PASS: held drag, Pause/speed, mass/speed/turn, Gravity and scrub act immediately. Aiming keeps world time at zero.
   Gravity off also removes pull arrows. Source controls clamp mass to the current kind's tray limits.
8. PASS via the specified fallback/actual-speed alternative: 240 dust did not sustain x4 under 4x CPU throttle,
   so dust is 160. Final 20-mass/160-mote run: mean 16.58 ms, p95 16.70 ms, achieved x1.8 displayed on requested x4.
   Prior runs ranged to x2.9. This is a 60 fps result, not a claim that requested x4 was achieved at full budget.
9. PASS: save/reload preserves stickers; replay body data matches the saved endpoint exactly; blocked storage still plays.
   Save limit, rename, replace/cancel, Delete and Clear confirmations are recorded in save-limit-results.json.
10. FAIL as a finished-art gate: all 27 labeled draft images load and contain no people, but paintings are not present.
    Required voice lines, two-second held taps, Read, Motion off, no external requests and no em dashes were checked.
    Narration uses browser fallback; recording was forbidden. This is the requested built draft, not an art-complete release.
11. PASS for the required fresh-agent proxy: 10m10s, still choosing experiments, eight discoveries and a stated concept.

#### Wave lessons
PASS, Hint and voice: hints update synchronously; Read uses current context. V.heard and pending keys prevent nagging
or competing Follow lines. A first-tap mode action has no late welcome. The stale True size line drops correctly.
PASS, Focus/layout: no focus on load; buttons are not rebuilt under a pointer; book loads restore focus;
hint height is reserved and Flight notes are sticky. Compact body actions come before the longer readout.
PASS, Sizes: all eight STANDARDS sizes, both modes, required host, 44 px controls/body hit diameters and 10 px labels.
PASS, No giveaways: no quiz answer or progress shortcut; stickers depend on measured physical outcomes.
PASS, Honest numbers: Pocket honesty line, real units, scaled true-size caption, finite-mass correction and actual speed.
PASS, Standards: gravity/orbits/galaxies, scale, forces and mass/distance changes are student actions; no family engine.
PASS, Motion off: decorative pulse, twinkle, ring growth, sparks and chip glow stop; content motion and timing continue.
PASS, Short choices: all nine selected-body actions fit the 680 preview; all seven Wonders are visible.
The phone tray is the spec's explicit horizontally scrolling exception.
PASS, Resize mid-animation: the smaller audit found no exceptions or controls left disabled after resize.
PASS, Deferred welcome: welcomeAfter false follows the higher-priority multi-mode standing rule.
PASS, Unknown as unknown: no hidden puzzle clues; missing paintings are labeled placeholders.
PASS, One look/one meaning: solid trails, dashed prediction and dotted discarded future remain distinct, including grayscale.
PASS, Truthful badge: body/parent/lap data, true-size state, Pause/Play and measured running speed match state.
PASS, Hint changes back: True size off, Fit recovery, finished replay and capacity changes return to fitting instructions.
PASS, No copying words: there are no word-matching answers; the science is the mechanic.

#### Audit leads
The first audit timed out on mouseReleased inside its control walk after the driver's internal 60 s limit.
The command's outer limit was 30 minutes. Its frames survived, but it did not write audit.md.
The brief permits one smaller retry: --no-walk completed. Full control-walk/repeat coverage remains uncompleted.
Report: Scratch/audit-retry/audit.md. Every one of its 333 rows has a disposition in audit-lead-ledger.json.
9 small targets: FIXED with 44 px minimum widths; targeted measurements confirm Read/Clear/Close are 44 px.
6 apparent closed-section overlaps: FIXED by explicitly hiding closed disclosure content; Gravity height is zero.
1 scrolled-out hint: FIXED with sticky Flight notes; saved-book 680 frame measures hint within the viewport.
190 canvas overlaps: intentional canvas application surface under its scene labels and the specified overlay tray.
97 below-fold advanced controls: specified portrait page stack; primary throw, tray and time controls stay in view.
26 hidden underlying scene texts: intentionally covered by an open book; its own contents and Close remain readable.
2 covered keep regions: portrait books intentionally cover time/tray until Close; physics continues behind them.
1 clipped phone choice row: the spec explicitly calls for a sideways scrolling tray; Wonders is fully visible.
1 dropped how line: student already enabled True size, exactly the spec's stale condition; it must not speak afterward.
Motion-off and resize sections were clean. Targeted fixes were re-shot; the full audit was not repeated again.
Independent held-input, keyboard, persistence and ten-minute play checks captured no tool console exceptions/warnings.

#### Frames looked at
Scratch is S:/CurioClass-codex-scratch/pocket-universe/.
Both bar frames; quick-frames/*; Pocket/Real at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
760x900 and hosted 375x812 in full-frames/*; phone books/library; extreme-frames/* including grayscale and Motion off.
All 102 PNGs from the audit attempts were inspected on paired contact sheets, with representative native-size checks.
Final-layout-frames/*, buttons-first-frames/*, render-final-frames/*, keyboard-real-input.png,
final-aim-escape.png, final-aim-follow.png, final-replay-idle.png, final-true-size-off.png and feel-comparison.png.
The fresh agent inspected its representative student-run frames; its full evidence/report is in Scratch/playtest/.

#### Engine changes wanted
No production kit or family changes. Audit tooling request: scripts/audit_tool.py, Audit.walk_mode/press,
log the current control, handle native confirmations explicitly and preserve partial results on CDP timeout.
A native-confirmation cause is plausible, not proven for the failed audit's unlogged control.

#### Left open
Painted art, recorded narration and human-student/audio-by-ear validation. No generation or polish was authorized.
The complete audit control walk/repeat pass did not finish; the smaller audit and independent checks are not a substitute
for claiming it completed. The original source's exact random-trial rates/error estimates were not all reproduced.
Performance varies with hardware and encounter geometry; the full-budget benchmark kept all counts alive on outer orbits.
The initial location lookup finished in 0.14 s but used the tool's default wait rather than an explicit stop deadline.
All subsequent build/test subprocesses had explicit deadlines. host.html was removed and owned test processes closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: pocket-universe

#### Played

Pass 1: cold solo grade-6 exploration before reading the builder's report or source, then a projector-focused look.
Threw bodies; tried every Wonder, both modes, goals, rewind, saves and keyboard input. The trails are the strongest moment.
Pass 2: fixes and scoped verification only. This is an agent play check, not a human ten-minute user study.

#### Findings fixed

- Blocker, general, src.html: Real Clear created a Pocket world under Real controls. It now retains Real masses and radii.
- Blocker, general, timeline: cross-mode Undo and mode changes lost mode or rewind state. Pack/unpack retains both tapes correctly.
- Blocker, general, replay: simulation stepped past the saved endpoint. Replay now stops at the exact saved body state.
- Should fix, general, rewind: selecting a body in the past discarded its future. Only an actual throw/change now forks it.
- Should fix, general, storage: failed replacement lost the oldest save in memory. Failure restores the complete previous list.
- Should fix, general, keyboard: Space stole focused buttons; cancelled scrub pointers stayed active. Both paths are corrected.
- Should fix, general, confirmations: blocking browser prompts prevented reliable input checks. Accessible modal dialogs preserve the same asks.
- Should fix, general, goals: Figure eight could reuse an old survival timer; Trojan accepted a moon companion. Both checks now match the targets.
- Should fix, general, hint/voice: startup disclosure events overwrote the opening hint; asynchronous Save triggered a welcome and lost repeated events.
  Startup preserves the throw instruction; Save has distinct event keys and a correct first-tap opt-out; crash/goals guidance stays sequenced.
- Should fix, general, preview: distant-planet labels clustered over inner orbits and disappeared under the tray. Perimeter labels stay readable.
- Should fix, general, art: every painting was a labeled placeholder. Generated and placed all 27 specified paintings; retained the palette and trails.
- Polish, general, crash: lit the time bar and named rewind on the stage so a failed throw points directly toward another experiment.
- Verification regression corrected: one helper misread UTF-8; restored every symbol and checked the rendered output before the audit.
- Blocker, general, True size: a minimum rendered radius contradicted the scale label. Actual body radii now match the computed screen size; locating rings stay visible.
- Should fix, general, books: welcomes named covered controls and the empty library named absent actions. Welcomes now wait; the empty state names Close and Save.
- Blocker, general, reproducibility: Undo did not restore creation counters, so seeded dust throws differed. Counters now restore; Enter, Ctrl+Z, Enter reproduces all 30 motes exactly.
- Should fix, general, focus: Undo reparented the focused tray even when its placement was unchanged. Resize now keeps the node in place and restores focus across actual moves.

#### Findings left

- Polish: narration uses the browser fallback. Recording audio is outside the brief; audible voice quality was not judged in muted Chrome.
- Nit: highly crowded custom systems can still need Fit or selection to read a particular body; no arbitrary body-count reduction was made.

#### Flattest moment left

A stable system can become quiet once its shape is familiar. Wonders, Follow, rewind and the 24 optional targets provide the next experiment.

#### Graphics

27 new OpenAI gpt-image paintings, no people or lettering. Prompts and processed assets are in art/; originals are in art/raw/.
Checked every processed sprite at native size, all three skies, both modes at all eight required sizes, grayscale and Motion off.
Art: 369 KiB. Final self-contained bundle: 653,651 bytes, below 2 MB.
Compared with Beat Lab and Snowy Mail Route using Scratch-only bundles; review-comparison.png pairs the frames. Kept the luminous trails, pink accents and spatial detail.

#### Audit

Audit not finished: stopped at the required 30-minute limit; no audit.md was emitted. Initial/mode layouts, listed states and Motion-off frames survived, but the full walk/repeat/resize result is unverified. No retry or third pass was started. See Scratch/review-audit.log and review-audit/.
Narrow exit corrections were re-shot against a separate Scratch bundle without changing the running audit bundle.
True-size canvas geometry matches the physical diameter at laptop and preview sizes; book/dialog first taps are silent.
Independent checks: 38/38 current-source physics assertions; all 24 goal detectors reached through integrated trajectories.
Recomputed periods, speeds, mass ratio, Hill radius and Earth diameter. Starter 7.815 s; Rescue crash 15.748 s; Mars reversal May 2001.
Exact replay, Real Clear, cross-mode Undo, mode/tape retention, failed-save rollback, dust Undo and actual keyboard input passed.
Motion off: identical paused canvas after 0.5 s, zero animations. Voice manifest matches all 96 runtime lines. No tool console errors.
| Line | Kind | Expected | Spoken |
| Saved on this device | event, five taps 2 s apart | 5 | 5 |
| Pocket welcome | welcome, repeated mode entries | 1 | 1 |
| Real welcome | welcome, repeated mode entries | 1 | 1 |
Read, rapid mode changes and Sound off were checked with held input. Host-only favicon 404 is not a tool request.
Full budget at 4x CPU throttle: 20 masses, 160 motes, mean 16.88 ms/frame; requested x4 visibly reports achieved x2.7.

#### Left open

Spec's finite-mass example discrepancy remains documented in handoff.md; the implementation follows the recomputed physics.
No commits, publication, recording or shared source changes. Two passes only. The initial standard bundle emitted scripts/__pycache__/voice.cpython-313.pyc outside the tool folder; it was left untouched afterward.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (pivot to an instrument; Cory approved it and the look, 2026-11-04)
Counts: blockers 0, should fix 0, pivot items 7

### Pivot: pocket-universe becomes an instrument (owner's decision, Cory, 2026-11-04)

This is not a normal Refine list. Cory decided that Pocket Universe becomes an **instrument**: read docs/VISION.md
("Instruments: the second shape") and docs/CURIOSITIES.md ("The look" and "Pivoting the super tools") first. An
instrument is shaped around a real thing, the student drives, and there is no score or finish line. Pocket Universe's
real thing is a gravity sandbox watched from mission control. The physics, the trails, rewind and the Real Solar
System stay exactly as honest as they are. What changes is the frame around them.

Owner's decision overrides the spec: update the affected sections of `spec.md` (Goals, Screens and modes, Look,
Teacher note) to match what you build, and say so in `polish.md`. The no-new-features rule in CODEX-FIX.md does not
apply to the items below; it still applies to anything else.

#### Pivot items

1. **The sky is the front door.** First open: space, the tray, and one line of how to throw. No goal count, sticker
   book or target is on screen.
2. **Goals leave the screen.** The 24 goals and the sticker book go. What they taught moves into the Manual as
   "Things people have found": short entries the student can read after discovering them, never targets to chase.
   No "Goals 0 / 24" anywhere, no sticker slide-in, no chime for a found goal.
3. **Wonders become the setups book.** The Wonders stay as a book of famous setups to load, break and change
   (the figure eight, a two-sun system, the real Solar System), opened from the Manual or the console.
4. **The look of mission control** (docs/CURIOSITIES.md "The look"): the space view fills the screen; telemetry in
   monospace with units (selected body's mass, speed, distance, what it circles, laps); a time dial and scrubber in
   place of the speed pills; orbit readouts with thin rules. The kit frame goes: no header pill row and no
   right-hand pill panel. Controls sit on a console along the edge of the view.
5. **Family marks.** A small engraved maker's plate in a corner: "Curio Class Instruments · No. 02 · Pocket
   Universe". A `Manual` drawer in the same corner as Span and Spire's. Motion, Sound and Read stay, on the
   console's own power panel. Pocket and Real Solar System become two switch positions on the console.
6. **Keep the honesty lines.** The exaggerated masses note, "Drawn bigger than life" and True size stay visible
   where they are true.
7. **Keep BASELINE.** Keyboard play, contrast, reduced motion, the Read voice, one offline file, the 60 frames a
   second budget on a school Chromebook, and every size the tool supports now (re-shoot each). Reword any voice line
   that names a removed control or a goal.

#### Size of this round

This is a bigger change than a normal fix: the frame of the tool is redrawn around an unchanged engine. Take the
time a build would. If something cannot be done well in one pass, do the parts you can do well, leave the rest,
and list it under "Not done" in `polish.md` with what it would need. A half-made look is worse than the old one.

#### Settled calls

- Keep the Gravity dial, Ghost, trails, Follow, Save and My universes.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: pocket-universe (Codex fix, round 1)


Owner-approved instrument pivot. Items 1-6 are fixed. Item 7 remains NOT FIXED for the full-budget 60 fps requirement.
Local test-server cleanup is blocked by Windows permissions. All evidence below is in `_scratch/pocket-universe/` relative to the repository root.

#### Blocker

None listed.

#### Should fix

None listed.

#### Pivot items

1. FIXED: sky front door, one throw hint, tray, no target or count. Before: `before-frames/before-pocket-1366x768.png`; after: `final-smoke-frames/last-default-1366-final.png`, `proof-frames/final-phone.png`. Stage width increased from 1076 to 1366 px at 1366x768; the compact view uses all 680 px.
2. FIXED: removed detectors, award events/chime, sticker book, counters and new sticker persistence. Twenty-four facts are unlocked, unnumbered Manual field notes. Before: `before-frames/before-goals.png`; after: `proof-frames/final-field-notes.png`. `exercise/results.json`: 24 notes, zero obsolete controls, store keys only `saves`; no progress after cheap input patterns.
3. FIXED: Wonders is now Setups, opened from the console or Manual, including the figure eight, Two suns and a fresh Real Solar System. Before: `before-frames/before-wonders.png`; after: `final-state-frames/setups-680x425.png`, `final-state-frames/setups-375x812.png`. All eight loads fit those frames; the audit-discovered intermediate-size cutoff is also fixed, with zero hidden loads and zero scroll overflow at 1000x625 and 1280x720 (`late-proof-frames/`, `setups-fixed-*.json`). Native cross-mode Undo restored Real with nine bodies.
4. FIXED: removed the kit header and right pill panel; made an edge console, rotary Time dial, rewind tape and ruled monospace telemetry. Before: `before-frames/before-selected.png`; after: `proof-frames/final-selected-1366.png`, `proof-frames/final-selected-680.png`. Pocket: 10 pocket u, 201.0 px/s, 250.0 world px, parent and laps. Real: 5.969e24 kg, 30.29 km/s, 0.9833 AU. Reference frame is explicit.
5. FIXED: lower-left Manual and engraved family plate, console power panel, two-position universe switch. Before: `before-frames/before-pocket-1366x768.png`; after: `final-smoke-frames/last-default-1366-final.png`, `proof-frames/final-phone.png`. The phone plate and privacy line have their own rows. Keyboard Manual notes are reachable; Escape restores Manual focus.
6. FIXED: retained visible exaggerated Pocket ratios, Drawn bigger than life, True size and the whirl boundary. After: `proof-frames/final-real-680.png`, `proof-frames/final-true-phone.png`, `final-state-frames/motion-off-1366x768.png`. Physical Earth diameter was measured directly from drawImage and matched computed scale to floating-point precision; see `exercise/results.json` and the final size check below.
7. NOT FIXED: the 60 fps full-budget target is not proven. All eight sizes in both modes, keyboard input, contrast, Motion off, Read, one offline file and revised control names passed their targeted checks. Best full-budget observation at 1366x768 and four-times CPU throttle: 20 masses, 160 motes, 18.74 ms/frame (about 53 fps), with achieved speed visibly below requested x4. See `final-checks/results.json`. A slower adaptive-budget trial was reverted. No 60 fps claim is made.

#### Polish accepted

None listed separately.

#### Settled calls

Applied: Gravity, Ghost, trails, Follow, Save and My universes remain. Their drawers and keyboard paths work.
Native Enter / Ctrl+Z / Enter repeated all 30 Dust motes exactly, preserving focus on the Dust chip.
Actual Save, page reload and Replay ended at step 1440 with identical bodies. Real Clear retained Real units.
Rescue: original Moon crashed before 16 s; rewind, reselect Moon and five Slower taps kept it for 11 laps at 16 s.
Evidence: `exercise/results.json`, `final-checks/results.json`, `final-checks/replay-endpoint.png`, `final-checks/rescue-after-rewind.png`.

#### Cheats tried

- Sweep Time and Gravity while paused; alternate Faster/Slower and Heavier/Lighter 30 times: zero elapsed time, zero laps, zero goal controls, no progress key or award. `exercise/results.json`, cheap-paused-sweeps.
- Cycle famous setups and advance them, then open every field note: all 24 notes are freely available, no counter, earned state or sticker namespace. Reading them is the intended field-guide use, with no pass condition. `exercise/results.json`, cheap-loads-and-manual.
- Let Starter run for 16 world seconds: exactly two completed laps. Turn Gravity off: parent and laps read n/a. No way to bank a best or pass from the readout. `exercise/results.json`, lap-readout.
- Set the Time dial repeatedly while paused: requested rate can change, but RUN is zero and world time stays fixed. The setter no longer substitutes requested speed for a measurement. Final single-shot result: requested 16x, RUN 0x, elapsed 0, store keys only saves (`meter-cheats.json`, `last-number-frames/meter-cheats.png`).
- Legacy sticker data with a named saved universe: the universe name survives; new store keys contain only saves. `exercise/results.json`, legacy-migration.

#### Voice walk

Held clicks, 120 ms, at a two-second pace. Main path: tray selection and real drag, then Real and the Time dial.
Side path: Manual, first field note, Manual's Setups, Three-body dance. Logged once each, in order:
Pocket welcome; Real welcome naming the Time dial; Manual introduction; Falling and missing fact; dance intro naming Body.
Read with Sound off logged the current hint. No goal or removed-control line remains. Motion off: zero running infinite animations.
The manifest and runtime allLines match exactly: 77 unique fixed lines. Browser fallback is retained; no recordings made or audible quality claim.
Evidence: `final-checks/results.json`, final-voice-walk, read-with-sound-off, motion-off; `verification.json`.

#### Engine changes wanted

No production kit or numerical-integrator change. The NBODY block is byte-for-byte unchanged:
`af34a7e5edf6856f5553bc81b754e744af93c98315c087dd2b8282149eabb85e`.
Shared test-harness request: `scripts/drive.py`, HOST, add an inline empty favicon to its generated parent page.
Additional harness requests: `scripts/audit_tool.py`, MODES_JS, recognize console `.mode-switch` buttons;
PAGE_JS vis, skip unpainted descendants of native closed details. No shared scripts were changed.
The parent host's favicon.ico 404 appears in iframe batches. Standalone tool checks have zero HTTP(S) requests and zero exceptions.

#### Model, sources and checks

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

#### Feel check

Best moment: a real jittered held drag bends a ghost around the star, then release starts its own colored trail.
Two flat moments addressed: the old goal/panel frame became an edge console; cramped preview orbits got usable sky margins.
The painted sky, sprites, luminous trails, pulsing stars and quiet sky life remain. Layered glow replaces costly per-trail blur.
Both bar tools were opened read-only. Pocket Universe keeps the density and material of an instrument without copying their scene.

| Pocket Universe | Beat Lab |
|---|---|
| ![Pocket Universe](../../_scratch/pocket-universe/final-smoke-frames/last-default-1366-final.png) | ![Beat Lab](../../_scratch/pocket-universe/proof-frames/bar-beat-lab.png) |

#### Audit

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

#### Not done

- Local test server on 127.0.0.1:8725 remains running. Its command line was verified as this task's drive.py host, PID 54024. Windows returned Access denied on termination; no permission escalation was attempted. All Chrome debugging ports are closed. See `host-owner-identity.json`.
- Full-budget 60 fps remains unproven. Further renderer/compositor work and another measurement are needed; keep the numerical engine unchanged.
- A fresh ten-minute student play check was not rerun in this one fix pass. No fresh lenses were launched.

#### Left open

Unattended decisions: use the approved instrument pivot over the old game frame; put Manual in the lower-left family corner;
make every field note freely readable; show parent-relative telemetry with an explicit origin fallback.
The last two-shot number batch lost Chrome/CDP; it was retried once as smaller single-shot commands.
Final size check at 680x425: measured Earth diameter 0.004564377643047484 px; computed 0.004564377643047695 px; label 0.0046 px (`final-size-number.json`).
The final 77-line manifest matches runtime in both final 1366 frames and the mode-memory check. The last pair reports zero errors.
All 119 generated before/after, intermediate and audit frames were inspected, using native critical frames and ten contact sheets (`qa-frame-index.json`, `qa-sheets/`).
Generated host cleanup: removed (verified absent). Remaining test ports: [8725].
Final bundle: 648,641 bytes. `final-manifest.json` records exact file and frozen-audit hashes.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Pocket Universe: instrument handoff

Owner-approved pivot, 4 November 2026. The source now frames the existing gravity sandbox as mission control.
There are no goals, award detectors, sticker events, progress counters or sticker storage in new saves.
The 24 existing concepts live as unnumbered, unlocked Manual field notes. Setups includes a fresh Real Solar System.
The seven pivot items and their evidence are recorded in polish.md. The performance requirement is not fully met.

#### Source map
src.html contains the instrument CSS and console, the unchanged NBODY numerical block, observational orbit tracking,
the tray/planet/finding tables, storage and timelines, drawing and sound, scheduling, readouts, drawers and input.
__tool exposes world/state, NBODY, measureOrbits, timelines, findings, setup loaders, allLines and vlog for checks.
The source remains readable, with no lines over 160 characters and no em dashes. All 27 paintings are retained.

#### Console and drawers
The sky spans the viewport. The canvas covers the visible sky above the edge console, avoiding hidden raster work.
The camera uses real pixels and adapts its usable sky margins in short windows. Every main control fits at all
eight STANDARDS sizes. The phone is tested through the required 375x812 iframe host.
The lower-left Manual sits beside the No. 02 maker's plate. World and Body fold upward, with Close and Escape.
Short-window drawers use the available height. Setups shows all eight loads at once on the phone and short preview.
Manual notes scroll inside the book; their summaries are keyboard reachable. Escape restores the Manual button.
The console precedes the canvas in keyboard order. The clock, time dial, tape and tray remain available on the edge.

#### Physics and readouts
The NBODY block is byte-for-byte identical to the received source. Engine SHA-256:
af34a7e5edf6856f5553bc81b754e744af93c98315c087dd2b8282149eabb85e
measureOrbits tracks parent and signed angular accumulation for lap readouts and sound, with no pass/fail condition.
Parent remains the nearest bound body at least three times heavier. Speed/distance are relative to that parent,
or to the explicitly labeled simulation origin if none exists. Laps reset when the parent changes.
Pocket uses pocket u, world px and px/s. Real converts to kg, AU and km/s using the original model time scale.
True size still draws the physical diameter, separate from the locating ring; its Earth label follows actual zoom.
Pocket's exaggerated ratios, the Real size label and the whirl's distributed-mass boundary stay in the sky.

#### Saves and deterministic timelines
The localStorage key and gzip wrapper are unchanged. Legacy named saves remain readable. Their retired sticker
namespace is ignored and omitted on the next write. New stores contain only saves. Save thumbnails preserve aspect.
Actual Save / reload / Replay returned exactly to step 1440 with identical bodies. Real Clear keeps Real units;
Undo crosses a setup's mode boundary correctly. A real Enter / Ctrl+Z / Enter repeated all 30 Dust motes exactly,
including IDs, positions and velocities, with focus retained. Rewind, reselect Moon, Slower five times: 11 laps at 16 s.

#### Narration and access
The Leda/casual-peer bank is retained, through Curio.voice. Seventy-seven manifest lines equal runtime allLines.
Removed controls have no remaining spoken references. Body/World directions name their drawers. Real names the Time dial.
Held clicks at a two-second pace logged the Pocket/Real welcomes, Manual, a field note and the dance intro once each.
Read works with Sound off. Motion off has no running infinite decoration; physical motion continues as content.
Text, muted text, maker plate and button text contrast ratios are 16.29, 6.79, 8.32 and 9.94 to one.
Narration uses the existing browser fallback; no recordings were generated or judged by ear in muted Chrome.

#### Performance and not done
The expensive per-trail canvas shadow blur was replaced with layered luminous strokes, retaining the painted sky,
glowing paths and sprites. Hidden canvas area is no longer rasterized. Physics scheduling yields after each fixed
step and reports achieved speed as RUN beside requested TIME. A requested rate is never substituted for a measurement.
The best observed full-budget 1366x768 run at four-times CPU throttle was 18.74 ms/frame, about 53 fps,
with 20 masses and all 160 motes. It reported the lower achieved world speed. This does not prove the 60 fps target.
An adaptive-budget trial was slower and was reverted. Further work belongs in this tool's renderer/scheduler,
with compositor-aware profiling and another full-budget measurement. The numerical integrator must stay unchanged.

#### Evidence
Current Scratch: S:/CurioClass-codex/_scratch/pocket-universe/.
before-frames and before-src.html preserve the received front door, goals, Wonders, mode and telemetry.
final-frames covers both modes at all sizes. final-state-frames and proof-frames cover the drawers, notes, units,
True size, Motion off and grayscale. final-checks/results.json and exercise/results.json contain native-input checks.
verification.json recomputes units, contrasts, source/engine checks and layout bounds. fix-audit is the final audit.
Historical build/review reports remain in this tool folder; the former handoff is preserved in Scratch.

#### Engine changes wanted
No production kit or numerical-engine change is requested. Shared test-harness request only:
scripts/drive.py, HOST: add an inline empty favicon to the generated parent host. Its favicon.ico 404 is emitted
by that test host, not by the tool. Standalone tool checks show no HTTP(S) requests and no exceptions.
Shared scripts remain unchanged.

#### Decisions taken unattended
The approved instrument decision overrides the old game spec. Its affected sections, first minute, voice and
Done when references now describe the implementation. Open questions were left alone.
Manual is in the lower-left family corner. All field notes are freely readable, never a hidden achievement list.
Speed/distance use an explicit physical reference frame. No new art, topic, score or finish condition was added.
No commits, shared-file changes, uploads or deployments were made.

#### Fix audit exit
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

#### Test-server cleanup blocked
All Chrome debugging ports are closed and tools/pocket-universe/host.html was removed. The hidden local server
on 127.0.0.1:8725, PID 54024, remains running. Its command line was verified as this task's drive.py --host
process, but Windows denied termination. No permission escalation was attempted. Identity is preserved in
Scratch/host-owner-identity.json. This resource cleanup remains open for the next operator.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-05)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
