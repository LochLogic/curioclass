# Recital Stage Directions build handoff

Build only. No commit, branch operation, shared-file change or polish round.

## Structure

The readable single-file source starts from the kit starter. The kit supplies the header settings and voice queue;
the dance engine supplies floors, figures, poses, paths, phrase interpolation, clock, music and count strip.
The content tables precede the renderer, scene layout, interactions and event bindings. `window.__tool` exposes
the state, call checker, phrases, playback controls, renderer and content for a cold review.

Canonical floor coordinates always remain from the seats. Reverse view maps canonical x through a camera transform.
`makeFigure` adapts the engine projection so an actor's position mirrors while their body turns 180 degrees.
Its separate body offset is essential: mirroring the entire skeleton and also turning the body swaps its hands twice.
The two floors crossfade while tiles and actors move over 800 ms. Motion off cuts at the same endpoints.
The transition approximates an orbit using a horizontal camera transform; it is not a full 3D camera.
During layout, the engine briefly receives the unmirrored projection, preventing negative-width decoration rectangles.
All world positions remain unchanged by layout, flip, costume and lighting changes.

The panels precede the stage in DOM order. Stage tiles and plan buttons persist as state changes.
Keyboard arrows follow screen directions after selecting a dancer. V flips. Focus moves intentionally only when its
former control becomes hidden, using preventScroll. Calls accept all valid identities in the unspecified formations.

## Art and the next painter

Two non-person backgrounds were made with the built-in imagegen tool during this build. Full prompts and provenance
are in `art/prompts.json`; originals are in `art/raw/`; final images are `art/house-from-stage.webp` and
`art/recital-backdrop.webp`. Only the free `art.py --rekey <name>` operation processed them. Both finished images
were inspected at their final 1400-pixel width. No people, faces or body parts were generated.

The owner wants painted dancers as the final result. The kit figures are temporary. Fifteen deferred `people: true`
pose sets cover stand, releve, open arms, walking, arabesque, sinking/curling, stamp, point, kick, clap, star jump,
sharp freezes, running, reaching and bowing. Each prompt requests necessary facings, sides, keyframes, badges and
costume variants. The guide uses stand and open-arm sets. These are pose sets, not single cutouts.

`POSE_ART` holds the future art tokens. `renderer.frame`, `renderer.rebuild`, `renderer.icon`, `renderer.extra` and
`makeFigure` are the replacement boundary. Preserve canonical positions, per-frame pose samples and shared clocks;
replace figure drawing inside that boundary. Use actual back and side paintings rather than mirroring a front sprite.
Both comparison clips use six smaller figures, three per piece. The painted renderer must support those too.

## Content decisions

- Followed the spec's leaning to use the dance engine. The catalog currently says family none. Whether this and
  poem-to-movement join the named dance family remains an owner/catalog question; shared files were not edited.
- Followed the owner's painted-dancer decision over the spec's permanent-code-figure wording.
- A fresh read-only agent reviewed the ballet and jazz histories and Rush Hour before implementation.
  The review passed with two conditions: genuinely pre-beat accents and a clearly low jazz freeze. Both are included.
  The clip is an original theatrical-jazz study. The clue headings name pieces and do not generalize entire styles.
  Supporting primary sources: https://www.operadeparis.fr/en/visits/exhibitions/a-certain-air-of-italy-the-paris-opera-from-louis-xiv-to-the-revolution/11-how-it-all-started-court-ballets
  and https://danceinteractive.jacobspillow.org/themes-essays/african-diaspora/jazz-dance-music-and-the-importance-of-swing/
- Used the detailed Content timing: 24 counts at 72 is 20 seconds, despite the earlier screen summary saying about
  15 to 18 seconds. Rush Hour is 13.846 seconds. Source calculations and contrast checks match the numerical appendix.
- The exact title Autumn Leaves and its correct main-idea option share the word leaves. This can cue a word match.
  The build preserves the specified program and choices; a later teaching review should decide whether to rename
  the piece or revise the choices. The clue-selection and replay activity still asks for movement evidence.

## Tricky behavior

Every interrupt invalidates a run token and stops the clock, music, player and pending room-call wait.
Your turn awaits `Curio.voice` before creating the four-count lead-in. Sound off holds the call for its estimated
reading length. Read stops a room phrase before speaking. A Sound change leaves visual counting live;
if Sound is switched off during a call, its remaining estimated reading time is held before the lead-in.
Room counts remain paced identically with Motion off. Slower restarts at 80 beats a minute.
Again retains the last tempo; choosing a phrase or entering Your turn restores the default 100.
The count strip is hidden during each spoken call, then appears for its lead-in and movement counts.

Rush Hour claps land one quarter-count before counts 12 and 16, in both pose sampling and the quarter-beat music
pattern. One final freeze is low. Autumn Leaves uses one dancer's arabesque and staggered low floor curls.
Wrong clues explicitly say they belong to the other piece; correct clues run into their moment and freeze.
The Both levels clip samples high, middle and low moments from both pieces within two counts.

Validated localStorage contains costumes, light colors and lit areas, clue selections, idea choices, watched flags
and the Compare board. It never leaves this device. Start over removes the item without saving empty defaults again.

## Responsive choices and limits

At compact landscape sizes the plan sits beside the usable floor area. Clue cards move to an on-stage evidence rack
so all eight choices fit. On phones, the plan sits below the stage. During clue and idea reading, the phone plan
is hidden and the stage shortens to keep the answer choices visible. Primary phone actions stay fixed at the bottom.
The phone Dress and light and room setup screens require vertical scrolling for secondary controls and setup text.
The strict all-controls-without-scrolling interpretation is therefore not fully met. Review this deliberately.
The phone Compare board uses a full-height board overlay. History cards and placed-card columns may scroll.

## Engine changes wanted

- `kit/dance.js`, `floor().resize`: correct x0/x1 interpretation for the stage's d0=140 projection. To produce an
  85-percent-wide floor, this tool passes a 119-percent-wide box for stage and 85 percent for square.
- `kit/dance.js`, `floor().project/unmap` and figure projection: a documented camera orbit/mirror interface with an
  inverse would replace this tool's local camera adapter. Preserve hand identity and avoid negative rectangle widths.

## Remaining review

Cold review should inspect movement readability, choreography, acoustic balance and browser narration in particular.
No voice recordings were made, as required by the build brief. `easy-coach` / Umbriel is specified in lines.json;
the browser's available voice is the current fallback. Painted people art still needs its separate painter and owner review.
See codex-report.md for verification, frames and the single mechanical audit's disposition.

## Final build checks

The single mechanical audit reached its 40-minute command limit during the control/voice walk. It produced 81 PNGs
but no audit.md. The owned audit Chrome was closed afterward. All 81 frames were viewed in contact sheets.
This is an unfinished audit, not a clean mechanical pass. No second audit or polish round was started.

The final targeted nine-shot batch had no console errors. It checked camera hand identity and canonical positions,
real stage dragging, reverse keyboard arrows, sound changes during a room call, Read stopping the count,
Compare welcome validity, saved lit areas, reload/reset, and five repeating event lines at a two-second tap pace.
Four additional frames checked the 1000x625 setup, a long compact call, three dancers in C and the final low curl.
Phone long-call and three-in-C frames were checked again after the subtitle overlap fix, without console errors.

The guide shrinks and shifts within the center area when C is occupied. The recital dancers retain exact area
centers when alone, so call 5 stays a straight line and call 7 stays a true diagonal. Shared areas use nine-unit
side-by-side offsets. Individual shadow groups hide with their actors, including unplaced dancers in the wings.
Keep that behavior when replacing the renderer with painted figures.
