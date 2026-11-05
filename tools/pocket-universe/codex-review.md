# Codex review: pocket-universe

## Played

Pass 1: cold solo grade-6 exploration before reading the builder's report or source, then a projector-focused look.
Threw bodies; tried every Wonder, both modes, goals, rewind, saves and keyboard input. The trails are the strongest moment.
Pass 2: fixes and scoped verification only. This is an agent play check, not a human ten-minute user study.

## Findings fixed

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

## Findings left

- Polish: narration uses the browser fallback. Recording audio is outside the brief; audible voice quality was not judged in muted Chrome.
- Nit: highly crowded custom systems can still need Fit or selection to read a particular body; no arbitrary body-count reduction was made.

## Flattest moment left

A stable system can become quiet once its shape is familiar. Wonders, Follow, rewind and the 24 optional targets provide the next experiment.

## Graphics

27 new OpenAI gpt-image paintings, no people or lettering. Prompts and processed assets are in art/; originals are in art/raw/.
Checked every processed sprite at native size, all three skies, both modes at all eight required sizes, grayscale and Motion off.
Art: 369 KiB. Final self-contained bundle: 653,651 bytes, below 2 MB.
Compared with Beat Lab and Snowy Mail Route using Scratch-only bundles; review-comparison.png pairs the frames. Kept the luminous trails, pink accents and spatial detail.

## Audit

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

## Left open

Spec's finite-mass example discrepancy remains documented in handoff.md; the implementation follows the recomputed physics.
No commits, publication, recording or shared source changes. Two passes only. The initial standard bundle emitted scripts/__pycache__/voice.cpython-313.pyc outside the tool folder; it was left untouched afterward.
