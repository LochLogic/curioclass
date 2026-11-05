# Codex review: city-skyline-studio


## Played

- Cold Grade 9-12 student pass in Build, Ink and Find before reading the builder files; then projection, drawing,
  keyboard and target checks. The low-eye skyline and roof reveal are strong; keep their scale and dusk atmosphere.
- Inspected all eight STANDARDS sizes in all three modes, grayscale, Motion off, empty city and extreme camera/building settings.

## Findings fixed

- **Blocker, family:perspective, Build after Find:** `view.find` survived Object.assign and kept Find's focal scaling.
  Explicitly reset it on mode entry and easing. Verified Build's rendered focal length equals its readout again.
- **Should fix, family:perspective, target navigation:** focal scaling and horizon readouts stayed on the previous target.
  Refresh controls/readouts whenever the target changes.
- **Should fix, general, Find keyboard:** a matched stage Check hid the focused button; Next focused a panel copy below the fold.
  Move focus to visible Next, then the visible stage Check, with preventScroll. Two Enter presses reach target 2.
- **Should fix, general, portrait Ink:** Undo/Redo were below the fold. Reserve stage space through that button row;
  Undo bottom is 895/900 px at 760 wide and 807/812 px in the 375 host.
- **Should fix, general, layout:** long hints shifted controls. Reserve five landscape hint lines and keep Horizon's value row stable.
- **Should fix, family:perspective, teaching:** "every edge" incorrectly included uprights; tilted Ink promised screen verticals.
  Distinguish receding edges/uprights, name VP 3 when tilted, and qualify the horizon-crossing fact for short buildings.
- **Should fix, general, voice:** historical eye/guide counters could consume unheard instructions; phone Find depended on
  offscreen panel copies. Retry unheard how-to lines with V.heard and use visible Check/Extend as prerequisites.
- **Should fix, general, grayscale checking:** red alone identified bad ink. Added a dash pattern, retaining red and thickness.
- **Should fix, family:perspective, Clear/Undo:** restoring cleared ink lost its saved camera and skipped the old-camera warning.
  Undo/Redo now restore the strokes, camera and Keep state together; checked Clear, Undo, Redo and a subsequent camera change.
- **Polish, general, flattest action:** the snapped-line tag vanished on release. Keep its direction beside the completed line;
  clear it on the next drawing action or Undo/Redo.
- **Polish, family:perspective, weakest art:** the water tower was a bare tank on four posts. Added projected bands, seams,
  rivets, a top rim and steel cross-bracing; retained its construction frame, exact projection and the strong sky painting.

## Findings left

- **Should fix, general/spec conflict:** secondary Overlays, Buildings and export controls still require scrolling in
  portrait/short layouts. The spec explicitly requires Camera-only preview and a scrolling phone panel; a full simultaneous
  choice layout needs a spec decision. Primary Camera, pens, values and Undo/Redo fit. This is not an all-controls-visible pass.
- **Polish, general:** five corrected/new voice strings fall back to browser speech. Recording is forbidden in this review.

## Flattest moment left

- Later camera targets repeat setting adjustments after the construction idea is understood. Preserved the six specified targets.

## Graphics

- Checked the sole bitmap, dusk-sky.webp, at its 1600x900 output and in-scene. Kept it; no missing art tokens or people assets.
- Improved the weakest code-drawn structure, the water tower, and inspected street/roof views. No asset was removed.
- Compared the retained scene finish with the existing Beat Lab comparison frame. Bundle: 1,007,012 bytes, about 983 KiB.

## Audit

- The single final audit completed, exit 0, within 40 minutes: 113 leads, all read and grouped below. No full rerun.
- Fixed ineffective drag/key fixtures exposed by the saved frames, then rechecked actual 15-degree Tilt and both ink drags.
- The empty-clear lead led to the camera-metadata fix above. Rechecked Clear/Undo/Redo and the required camera warning.
- Canvas/hint/target-chip overlaps and covered hint sample points are intentional overlays; the frames are readable.
  Check/Extend have visible stage copies, so leads naming their scrolled panel copies do not block either action.
- Fold/short-choice leads remain the explicit spec conflict above. High-eye readouts shift secondary building controls;
  mode switches and opening Sun also move controls as expected. Camera controls and focus remain intact.
- Skipped welcomes after a first tap's own line follow STANDARDS; Read/Sound intentionally skip or stop speech.
  Canvas taps and clearing empty ink are expected no-ops. Real-work paths were checked separately.
- Motion off, repeat/rapid input, settled Enter paths, resizes, and console checks passed. All 39 audit frames inspected.
- The audit snapshot predates the corrected fixture bodies, shorter eye-height hint and Undo metadata fix.
  Only their affected frames were re-shot afterward; five revised narration lines use browser fallback.
- Python recomputed the worked VPs/FOV, 60 m crossings and tilt. Browser edge error <=2.22e-12 px; all six targets scored 100%.
- Real snapped line, hatch/fill, Undo/Redo, saved ink reload, keyboard revision/reflection, note and guide-free PNG passed.
- At 1920x1080, 20-building redraws averaged 4.365 ms, within a 16.7 ms frame budget; this is not a classroom hardware test.
- Contrast: cyan/panel 10.27:1, cyan/section 9.73:1, ink/cyan 9.43:1, label/chip 16.72:1.

| Voice line | Kind | Expected | Spoken |
|---|---|---:|---:|
| turnHow across five held stop changes | how | 1 | 1 |
| Matched across five held checks, 2 s apart | event | 5 | 5 |
| Hidden settings for those checks | event | 5 | 5 |
| Next target after repeated checks settle | how | 1 | 1 |
| Read with Sound off | read | 1 | 1 |

- Voice manifest matches allLines exactly; repeated-match queue drained. All narration was tested muted via held clicks.

## Left open

- Spec conflict and five browser-fallback lines above. No kit changes, other-tool writes, recordings or git commits.
- Evidence: `_scratch/city-skyline-studio/review-*`, `final-targeted/`, `review-audit/`.
