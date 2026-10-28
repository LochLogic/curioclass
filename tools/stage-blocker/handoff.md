# stage-blocker: build handoff (2026-10-28)

## What was built

- `src.html` (bundled as `stage-blocker.html`, CURIO_DRAFT=1), `tool.draft.json` (stage "built"), `notes.md`,
  `art/prompts.json` (no art: plan, seat view, figures and set drawn in code), `voice/lines.json` (firm-captain,
  Alnilam, 15 lines after the round 1 exit check; clips not generated yet, the browser voice stands in).
- New family engine `kit/stage.js` (global `Stage`) and family doc `docs/families/stage.md` (every option).
  director-s-chair reuses it. `docs/KIT.md` does not list stage.js yet (outside my write scope).

## How src.html is laid out

Content (catalog, the proscenium house, scenes with notes), building a scene's beats (`buildScene`: start snapshot,
carry, then `preset` edits such as Ben dropped upstage of Ava in beat 2), state, voice (`L`, `hintKey()` picks the
hint; `setHint()` speaks a how-to the first time it comes up), views (plan, inset seat view, house view, mini plan),
panel renderers, editing (`editNow` = Stage.edit on the current beat + carry), beats/seats/tabs/modes, Run, Free
stage, wiring, keyboard on the plan, layout (`relayout`), start. `window.__tool` has hooks for tests (place, turn,
light, check, finishRun, plan(), house(), vlog...).

## Decisions (settings, not facts)

- Facing is absolute: 0 faces straight out (-y). Body positions are measured to whichever seat is chosen.
- Default lights: downstage row full, center half, upstage off (so The Trophy's coach on the upstage platform has to
  be lit by the student for some beats).
- Wing slots: off-stage actors wait two to a row in their wing; an actor whose home is the Door waits behind it.
- `exits` counts the wing the actor was sent to (`actor.wing`), falling back to the nearest entrance; dragging Ben
  into the SR wing is an SR exit.
- Seat view inset: width clamp(26% of the stage area, 150, 440 px), beside the plan or above it when the plan keeps
  74% of its size, else a "Seat view" chip. "Focus: a rough guide" sits top left in Block, top right in House and Run.
- Seat camera frames the playing area up to 3.4 m (`fitPts`), not the whole 5.5 m opening, so figures read larger.
- Praise ("Notes met on this beat") only on a beat the student changed. The hint gives "upstaged" and "hidden"
  priority over the welcome, but only once the student has edited or changed beat (`state.placedOnce`).
- Area and piece labels give way to actor tokens on the plan; the SR/SL entrance arrows are quiet (the wings are
  labeled).

## Tricky parts

- Run awaits the "Places, please" line (`wait: true`), then holds each beat max(2200, 1400 + 75 per character).
- Free stage autoloads a save on start; buildScene + saved cast and beats.
- A how-to line that starts playing just before a mode switch is cut by V.hush and counts as heard (the hint and Read
  still have it).

## Refine round 1 (2026-10-28)

Every blocker, should-fix and accepted polish item in refine.md is done; details per item are in the builder's report.
Decisions made along the way (settings, not facts):

- Open to the house (blocker 2): "has the focus" fails first if the actor is three-quarter or full back to A3, B3 or
  C3; "not upstaged" also needs the actor open to B3. Engine, spec sentence and docs/families/stage.md changed together.
- Enters (item 6): the wing or Door the actor waited in during the previous beat (`P.wing`), the nearest entrance only
  when that is not known. A drop into the house (y < 0) is refused and the actor goes back where it was.
- Plan space (item 17): the house rows are compressed on the plan (rows at -1, -1.85, -2.7 m, balcony at -3.85 m;
  `planAt` rays keep the true seat positions for the maths, with a faint dotted link). The little map uses the far
  layout (HOUSE_MAP). House and Run get a 5 x 3 seat button grid plus Balcony instead of "Next seat".
- House view frames the scene (`state.fit` from `sceneFit()`: every on-stage actor and piece over all beats, at least
  5 m wide), so figures are bigger and the camera does not jump between beats.
- First tap (item 15): pointer capture on every pointerdown, plus a synthetic click from the plan when the tapped
  element was redrawn away before pointerup, so the kit's first-tap welcome hears the tap (about 1.2 s, was 2.7 s or
  dropped as stale).
- Stack layout (item 18): mode panels come before the scene row and the long lists; the plan height leaves the tabs row
  in view at 760x900.

Polish taken from 25 to 29:
- 25 "Run again" is the label only after a finished run (the first run says "Run").
- 26 Stop puts you back on the beat you started the run from.
- 27 Beat 1 of The Note gets a direction ("Ava reads the note aloud, then looks up.") and the quote marks inside the
  line are gone; spec changed to match.
- 28 The beat-list legend says what the marks mean, worded for Free stage when there are no notes.
- 29 Focus score labels move below the bar when another token covers their usual spot.

Left open: clips for the changed lines (welBlock, welHouse) and the new runFree are not recorded; docs/KIT.md still
has no stage.js row; muting before the first tap (kit nit 4) is the kit's; "enters" accepts an actor who waited in SL
wing but first appears at DSR (the check reads where they waited, not the path).

## Exit check round 1 fixes (2026-10-28)

- A. Free stage has its own welcome, `welFree` ("Drag an actor from a wing onto the stage. Then pick the speaker and
  type their line under Beats."), chosen by `welKey()` in hintKey and the kit welcome; it is in L, so allLines() and
  voice/lines.json have it (clip not recorded yet).
- B. The notes list keeps one height across a scene's beats (`reserveNotes`): measured with every beat's notes and
  their real whys showing, per scene, beat count and panel width, re-measured after each edit (never mid-drag),
  grow-only. Beats with no notes say "No notes on this beat." in scenes that have notes. All beats now holds still
  (The Note and The Trophy 785 px, Bus Stop 713 px at 1366x768; 1009 px at 375; also after edits).
  Chose this over moving All beats above the notes, which would push the notes far down the panel.
- Nit: `Stage.initials` keeps letters and digits only ("O'Neil" gives On, "Jean-Luc" Je); family doc says so.
