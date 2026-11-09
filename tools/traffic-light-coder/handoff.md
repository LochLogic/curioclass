# Traffic Light Coder Curiosity fix handoff

## Structure

The user's 2026-11-06 Curiosity instruction supersedes the lesson-shaped spec and Refine.
The street, all twelve existing painted assets, robot-family program/runner and half-second
model remain. The source owns its instrument CSS; it no longer loads kit/curio.css or a kit header.
Motion, Sound, Read and voice still use kit/curio.js. Only Motion persists between visits; Sound is page-lifetime state. No shared file changed.

Live street is open-ended. Setups selects any of the five original traffic scripts, without
progression or completion state. The street record is observational telemetry, not a grade.
It preserves actual light intervals and unsafe-moment replay. The lower-left Manual contains
controls, readouts, exploratory findings, model assumptions, privacy and source licences.
No Curiosity plate number exists in the supplied spec or concept list. The engraved maker's
plate therefore uses the family name and tool name without inventing a number.

## Tricky parts

`makeWorld`, `when`, `execute` and `tickWorld` hold the original model. `summarize` now returns
observations only. `ambulanceStopped` is latched from the vehicle's stopped flag each beat
until the ambulance clears the crossing, including queues beyond the detector window.
`ambulanceStopAt` anchors the cause line to actual light history. Long yellow holds are covered.

Red intervals retain their next state, or null if still open at the observation endpoint.
`carsReturn` is an internal diagnostic requiring each red to end in GREEN within the existing
45 s tool reference. It never grades the user. An open interval is explicitly labelled open.
The dominant rule during the longest red is counted from actual firings, distinguishing
WALK requests from new walks. A request during an active walk does nothing, as before.

The robot runner restarts scheduling after a live program edit and halts a scripted run on edit.
The picker redraws the sentence and tabs after a change and restores focus to the chosen option.
Each script record focuses its heading with preventScroll. The record is a section, not a
non-modal dialog. The true picker and Manual use native modal dialogs.

## Voice

`voice/lines.json` equals `allLines()`. The three strings are the initial curb hint, the explicit
Read response in the picker, and the six-rule capacity line. Only the initial hint may speak
automatically. Every other utterance follows Read, as required for a Curiosity. Old job briefs,
success events and finale are removed. Browser fallback remains; this session records no audio.

## Verification

Scratch holds original source and notes, before/after numerical checks, 64 single-edit variants,
same-size frames, real held-input voice walks, keyboard edits, source downloads and the final audit.
See polish.md for item-by-item dispositions and the measured limits of the verification.
`verify_sources.py` preserves the public-domain federal originals and recomputes 35 / 3.5 = 10 s.
No outside traffic dataset or executable was downloaded. Existing people art was not changed;
the standing people-art desk review is unchanged.

## Engine changes wanted

None required. The existing local instant-advance loop uses the same matching, execution and
tick functions as the family runner. No engine change was made.

## Left open

Owner assignment of a Curiosity number and the legacy module's combined standards coverage.
No new unsafe kind, walker spacing change, external submission, commit or shared-file edit.

## Fix verification complete, 2026-11-06

The single audit completed with 92 frames and 581 indexed leads. Four layout/type causes
were repaired and re-shot in an 11-frame focused follow-up; intentional opaque overlays,
permitted scrolling and Curiosity first-hint behavior are indexed as accepted. Resize stress
finished without exceptions or stuck controls. No full audit was repeated.

The 96 single-edit attempts (77 distinct programs) leave only the two done-condition repairs
with safe crossings and timely green returns. All three long-yellow shortcuts now expose
the actual ambulance stop. A two-ambulance probe verifies any stopped vehicle is observed.
Phone focus and scroll use a work viewport above the power row. Compact text is at least 10 px.
Final bundle is 451,208 bytes; validation.json holds hashes, source/voice searches and metadata.
All started Chrome and host ports are closed. No refine.md edit or commit was made.

Optional audit improvement: scripts/audit_tool.py, MODES_JS, recognize instrument mode groups
outside header as well as lesson headers. Explicit audit states and a held Setups walk cover
that blind spot here; no shared script was edited to accommodate this Curiosity.
