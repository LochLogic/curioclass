# Pocket Universe: Build handoff

Current status: cold review and scoped exit fixes are recorded in codex-review.md. All 27 paintings are embedded.
The build account below is historical; the appended cold-review sections describe the current implementation.

This is Build only. No commit, branch change, art production, recording or polish round was performed.
All source changes are inside this tool folder. Scratch and evidence are at
S:/CurioClass-codex-scratch/pocket-universe/.

## Files and structure
src.html is the complete readable source, built from the kit starter. It uses kit:curio CSS, script, voice queue,
Motion, Sound and Read. It has no family engine. The generated pocket-universe.html is a self-contained draft.
tool.draft.json keeps stage built and prevents accidental live publication before the art arrives.
art/prompts.json contains the spec's 27 paintings. All remain labeled placeholders; no art was generated.
voice/lines.json uses casual-peer, with 67 fixed lines, including 24 sticker events and 24 findings.

The source order is scene CSS and HTML, the marked NBODY block, pure goal measurements, content tables,
world/load construction, timelines, rendering, sound, simulation scheduling, controls, library and keyboard input.
window.__tool exposes state, world, NBODY, goal measurements, loads, timeline functions and voice logs for verification.

## Physics and goals
NBODY has no DOM access. It exposes step, snapshot, restore, predict and parentOf.
The fixed step is 1/480 second. Kick-drift-kick, one-pixel softening, adaptive power-of-two substeps up to 64,
swept collisions and momentum merges are shared by prediction, replay and live play.
A validated WeakMap acceleration cache reuses the final kick's force only when object identity, mass, gravity
and every position still match. Restoring or changing anything invalidates it automatically.
Promoted stars adopt the Star tray's mass limits. Prediction stores the followed body's future position so its
ghost is drawn in that moving frame, and a trailing 50 ms update flushes the last quick pointer movement.
Dust has zero mass and feels all massive bodies. The measured budget uses the spec's permitted 160-mote fallback.
The active speed button exposes the achieved rate whenever computation falls behind.
The frame budget leaves time for rendering, caches the camera for each draw and clips only invisible trail segments.
The final 4x CPU-throttle run held about 60 fps with 20 masses and 160 motes, reporting x4 running x1.8.

Goals are measured every 1/30 world second. Parent changes reset signed lap accumulation. Goal history lives in
snapshots; earned stickers live outside it and survive rewind. The load alone cannot earn ordinary goals.
Snapshots use the student's actual canvas trails, not stock sticker pictures. The book contains all 24 targets.
The numerical harness reached every detector through real integrations, including capture, slingshot and Grand tour.
Successful search initial conditions and results are frozen in Scratch/numeric-results.json.

## Timelines and saving
The tape records every quarter second for 150 world seconds. Undo restores the previous action, paused.
A change in the past forks the timeline and leaves the discarded future as a dotted trail for 30 world seconds.
Immutable snapshots and trail-point records are shared safely between undo records; their arrays are copied.
This avoids serializing the entire tape on each drag or nudge.

Each mode retains a separate world and tape in memory. Saved universes contain the current state and a replay
from the beginning of the available tape with step-numbered action snapshots. Loading begins a fresh tape at
the saved moment; Replay reconstructs the saved action history. Controls stay live and a change leaves replay.
The replay stops at its saved endpoint. Quiet pre-throw intervals are retained faithfully.

localStorage key: curio-pocket-universe. Data is JSON compressed with the browser's gzip CompressionStream,
inside a gzip-base64-v1 wrapper; uncompressed legacy JSON is accepted. Decompression is asynchronous while the
Starter is already playable. Storage errors are caught and reported without stopping the simulation.
The cap is twelve named saves, with confirmation before replacing the oldest or deleting one.
The final native-input check filled all twelve slots, cancelled and accepted replacement, renamed and deleted
a save, and cancelled and accepted Clear. Each action produced exactly one expected confirmation.

## Source discrepancies resolved by computation
- Starter separation measured 250.000000 to 250.009801 px in 30 s, period 7.815004 s.
- The lone-star circular test-particle speed at 250 px is 200.0 px/s. Including Planet mass 10 gives
  relative circular speed 200.9975 and escape 284.2534 px/s. Some spec example numbers mix these conventions.
- Halving the Starter star alone leaves its finite-mass planet slightly bound. One Faster nudge before halving
  releases it. The Lightweight finding line was corrected; spec.md was left unchanged.
- True size's Earth diameter label uses the actual screen zoom. The reference 0.0085 is world pixels at 100 px/AU.
- In the whirl at Gravity 0.45, all remaining dust is beyond 1500 px at 20 s; motes already past 4000 px were dropped.
  Do not count dropped motes as failures of that source check.
- Three-body dance, Figure eight nudging, exaggerated Pocket masses and the honesty line, Gravity, Black hole
  in the grade 6 tray, and the 1 January 2000 epoch preserve the owner's settled choices.

## Input, sizing and voice
The canvas uses real stage pixels, not one scaled master layout. All STANDARDS sizes were inspected, including
375x812 in the required host. A body has a minimum 44 px picking diameter; the nearest candidate wins overlap.
Panel controls precede canvas bodies in DOM tab order. Enter on a tray chip is a keyboard circular placement.
Space, Ctrl+Z, F, G, Delete, number keys, zoom, Fit and time-bar arrows are implemented.
The tray moves below the time bar in stacked layouts. Compact Wonders and phone books portal to the body,
so a fixed dialog is not trapped under the header by the stage's isolation stacking context.
Under 900 px tall, all nine body buttons precede the longer readout in a three-column grid. At 680x425 their last
row ends at 402 px. Flight notes stay visible while the panel scrolls. Closed sections explicitly hide their contents.

The spec asked for welcomeAfter true, but STANDARDS and the BUILD multi-mode lesson explicitly prohibit a delayed
welcome after the first action's own line. This tool uses welcomeAfter false, as the higher-priority rule requires.
Voice hints update synchronously and Read speaks the current hint or current discovery. Follow hints are gated
by V.heard, queue state, current mode and the enabled Follow control, so two how-to lines cannot replace each other.
Motion off stops decorative pulse, twinkle, ring growth, sparks and chip glow. Content bodies continue moving.

## Verification and evidence
- Scratch/numbers.json: independent Python constants, periods, radii, mass ratios and contrast ratios.
- Scratch/numeric-results.json: 38 passing assertions and all 24 goal detectors reached.
- Scratch/browser-results.json: real held drag, aiming hold, Undo, rewind/rescue, exact saved replay, storage failure,
  and full-budget CPU-throttled performance. Results vary with concurrent browser load; the UI reports actual speed.
- Scratch/keyboard-results.json and keyboard-real-input.png: actual keyboard-only placement, Follow, Pause,
  Remove, Undo and Ghost, with no exceptions.
- Scratch/full-frames/: both modes at every STANDARDS size. Scratch/extreme-frames/: Wonders, discoveries,
  dance, whirl, full budget, Motion off, True size and grayscale. Targeted fixes are in targeted-frames/.
- Scratch/feel-comparison.png places our nudged dance beside Beat Lab's reference frame.
- Scratch/playtest/fresh-agent-play-report.md: actual 10m10s fresh-agent proxy, still playing, eight discoveries,
  handmade Twin Fireflies binary, saved and replayed. Not a human student study; muted audio was not judged by ear.
- Scratch/audit/: first audit frames; the control walk hit an internal CDP timeout before the report was emitted.
- Scratch/audit-retry/: the permitted smaller retry, with --no-walk, completed. Scratch/audit-lead-ledger.json
  gives a disposition for every one of its 333 leads. See codex-report.md for the grouped explanation.
- Scratch/final-browser-results.json and final-layout-frames/: targeted verification of the final functional and layout fixes.
- Scratch/save-limit-results.json: twelve unique saves, replacement/cancel, rename, Delete and Clear, five confirmations total.

## Engine changes wanted
No production kit or family engine changes.
Audit tooling request: scripts/audit_tool.py, Audit.walk_mode/press. Log the current control before dispatch,
handle a native JavaScript confirmation explicitly, and preserve already-completed results when a CDP request times out.
The first audit timed out after 60 seconds on mouseReleased and discarded its in-memory report. The exact control
was not logged; a native confirmation is a possible cause, not a proven one. The permitted smaller retry omits walk.

## Left for review
Painted art and recorded narration are absent by instruction. This is not a claim that finished artwork has shipped.
The toy's depth passed the fresh-agent proxy; real students and audible sound quality were not tested.
The source's retrospective random trial counts and every archival astronomy source were not independently re-created.
No network research was performed because the build brief explicitly forbids it and provides the source content.


## Cold review, 30 October 2026
The earlier sections describe the historical build. This review supersedes their missing-art status.
All 27 paintings are now generated with OpenAI gpt-image, processed through art.py --rekey and embedded.
The pink palette, physical integrator, luminous trails and optional 24-goal structure are retained.
Review Scratch: C:/Users/Cory/AppData/Local/Temp/curio-codex/pocket-universe/.
Only tools/pocket-universe/ was intentionally edited; no commits or shared engine changes were made.

Corrections: Real Clear keeps true units; pack/unpack restores the mode for cross-mode Undo; replay stops at
its exact endpoint; merely selecting a body in the past no longer forks the tape. Save rolls back its whole
previous save list on storage failure and guards concurrent writes. Confirmations use a native HTML dialog
instead of blocking window.confirm, preserving keyboard focus and allowing CDP checks to complete.
Space activates focused controls and pauses from the canvas. Cancelled scrub pointers release their state.
Figure eight restarts its survival timer after each new nudge; Trojan requires a planet companion.
Startup disclosure events preserve the opening hint. Off-screen arrows use the usable view perimeter.
A crash lights the time bar until rewind or the next throw, lifting the weakest teaching transition.
Rapid Save events have distinct queue keys; async Save opts out of the first-tap welcome.
Narration remains browser fallback, with no recordings made, as the brief requires.

Fresh physics execution: 38/38 assertions; all 24 detectors reached from actual integrated trajectories.
Hard-case initial states were reused as fixtures, not their prior PASS results. See review-numeric.js/results.
Targeted UI checks cover exact replay, mode restoration, Real Clear, save failure, keyboard-only actions,
Motion off, grayscale and held-click voice pacing. All eight required sizes were viewed in both modes.
The host page alone requests favicon.ico and gets 404; the tool has an inline empty favicon and no requests.
Full budget at 4x CPU throttle: 20 bodies, 160 dust, mean 16.88 ms/frame; requested x4 reports x2.7.
Bar tools were bundled into Scratch only and compared visually, without writing their tool folders.
The final mechanical audit is recorded in codex-review.md, which is the review's exit record.

Exit corrections confirmed from audit states: True size now draws the physical radius without a minimum
body-dot size; its locating ring remains separate. Canvas drawImage measurements match Earth's computed
screen diameter to floating-point precision at 1366x768 and 680x425. Welcomes do not queue over an open
book or confirmation. The empty library names Close and Save, and all 96 fixed narration/Read lines are
listed in the voice manifest. Dynamic names and numerical hints still use browser speech.
The audit's original bundle was kept unchanged while these narrow corrections were verified against a
Scratch bundle; the verified bundle replaces it on exit. There is no second audit or third review pass.

Dust Undo is also exact: pack/unpack retains the creation counter and art-variant counters, so the seeded
30-mote puff repeats with identical IDs, positions, velocities and colors. A real Enter, Ctrl+Z, Enter check
passed. resize now moves the tray only when its parent changes and restores focus across a real move,
so Undo keeps the focused chip usable for the next Enter. Evidence: dust-undo-result.json in Review Scratch.

Final audit status: Audit not finished: stopped at the required 30-minute limit; no audit.md was emitted. Initial/mode layouts, listed states and Motion-off frames survived, but the full walk/repeat/resize result is unverified. No retry or third pass was started. See Scratch/review-audit.log and review-audit/.
