# Recital Stage Directions handoff

Cold review in the authorized S:/CurioClass-codex checkout. No commits or shared kit edits.
The original builder report is historical. `codex-review.md` records the current review result.

## Structure

The kit supplies settings, narration, geometry, joint poses, phrases, clocks and synthesized music.
The tool keeps canonical stage coordinates from the seats and maps the camera independently of the dancer's body.
The two floors crossfade over an 800 ms camera transformation. Motion off cuts to the same endpoint.
The current transformation approximates an orbit; it is not a full three-dimensional camera.

`renderer.frame`, `renderer.rebuild`, `renderer.icon`, `renderer.extra` and `makeFigure` remain the figure boundary.
`makeFigure` delegates skeleton projection to the engine, then `paintFigure` draws the painted skin over the joints.
The original code drawing is hidden. Shadows, badges and hand arrows retain the engine's projected coordinates.
The whole figure can still be replaced at this boundary without changing choreography or interaction.

## Painted dancers

`art/dancer-cast.webp` and `art/dancer-backs.webp` are self-painted gouache source sheets, generated during review
with the built-in OpenAI image tool. Both are marked `people: true`, `drawn_by: codex` in `art/prompts.json`.
Original PNGs are in `art/raw/`. Only `scripts/art.py --rekey <name>` processed the final WebPs.
The front and back view of one neutral T pose per dancer supply all the articulated moves.
Three cast members have different skin tones, hair, builds and clothing. All perform both pieces.
The fourth image on each sheet duplicates the guide's back view and is unused; it is not an extra character.
Fifteen old proposed pose sets are preserved as `replaced_pose_requirements`, rather than missing active assets.

To swap art: replace `PAINT_SOURCES`, the sheet placement and `castLandmarks` near `paintFigure`.
The clip rectangles divide head, shirt, waist, sleeves, limbs and shoes. Keep source joint landmarks aligned.
Clothing-only filters preserve paint texture while making live costume changes. Skin and hair are never recolored.
Each crop is clamped to its own cast column to exclude neighbouring fingertips.
The head keeps its volume under a nod, and the arabesque faces sideways so its extended back leg is visible.
The inset icons, guide, main troupe and six-figure Both excerpt all use this same painted adapter.

The two original theater paintings remain in place. Their rich curtains, floorboards, light and depth were retained.
People sheet: `_scratch/recital-stage-directions/people-contact-sheet.png`.
Full prompts and provenance are in `art/prompts.json`; OpenAI illustration credit is in the source and draft metadata.

## Reading and checking

Each piece needs a complete watch, exactly the four supported clue cards and its intended idea before Compare opens.
Clue cards shuffle across positions on a fresh page. Neither column nor card metadata tells the student the owner.
Show me plays actual movement, including for a card that does not fit, and asks the student to judge the evidence.
It does not name which cards are right. Selecting every card fails the reading check.
A wrong idea requires a new complete watch before another guess. The retry flag survives reload.
Changing selected clues clears that piece's accepted idea, so the board cannot inherit a stale reading.

Compare retains all eight source cards and live bin buttons during its two-count excerpts.
Column labels summarize placements; the source cards remain the full-sized editing controls.
Wrong boards get collective feedback without an incremental count that reveals one correct placement at a time.
Each clip uses its source piece's saved production choices. Both shows three dancers from each piece side by side.
The real hint and privacy disclosure move into the board and return to the panel on exit or mode change.
Reset is hidden while that overlay is open; Back restores the original accessible control.
Compare uses the seats view and full floor width, with four explicit grid rows during playback.
Short landscape displays concise versions of the same eight traits, retaining full names as accessible labels.
The six painted dancers remain visible during the high/middle/low Both excerpt.
Replay projection fits between the bin headers and source cards at each viewport, and scales single-piece clips
to that space. The backdrop follows the floor edge. Header controls remain outside the overlay.

A rapid second Calls tap within one second is ignored so the first call can finish; later taps toggle normally.
The decorative guide does not intercept stage taps.
Calls are optional practice, without a cumulative score. The first three check only the named dancer;
the feedback explicitly identifies the other dancers as not called. Calls four through eight check whole formations.
Manual Bow is a neutral action; only completing the timed counts earns the closing encouragement.
The tool does not observe or grade a student's physical execution.

Rush Hour's first routes cross in canonical floor coordinates. Midpoints stay on each straight route.
The two intersections have staggered arrivals; see Scratch crossings-review.json for independent geometry.
The first ballet block resets facing, so repeated watches do not inherit an arabesque's sideways view.

## Timing, voice and saving

Every interrupt invalidates the playback token. Mode changes also cancel an unfinished camera flip.
Your turn awaits each spoken call before its four-count lead-in. Sound off preserves the estimated reading time.
Starting from setup lets its current welcome finish before the first call. Compare's first placement also preserves
its current how-to line. Mode changes, Stop, Read and a mid-phrase restart still interrupt obsolete speech.
Read stops a room phrase before speaking. Stop cancels pending calls, music and the count clock.
Slower restarts at 80 beats a minute. The regular phrase tempo is 100.
The full held-click voice walk is `_scratch/recital-stage-directions/voice-walk.json`.
`voice/lines.json` has the same fixed line set as `__tool.allLines()`; browser speech remains the recording fallback.

Saved settings include costumes, lights, lit areas, clues, answers, watched/retry flags and the Compare board.
The on-screen privacy line states that choices remain on this device. Start over removes this storage item.

## Responsive behavior

The phone uses one compact header row, an inset plan, and a production desk with all short choice sets visible.
The plan remains visible during clue and idea reading. Main phone actions remain fixed at the bottom.
Undersized perspective cells are noninteractive pictures; the inset provides full-sized named touch and keyboard
targets. Larger floor cells accept taps, and dancers can still be dragged onto every area of the floor. No tiny floor tile enters the Tab sequence.
Compact Compare uses the full viewport width. Long history footnotes may scroll inside columns.
The full-sized source trait controls stay visible; the duplicated placement labels are not extra small buttons.

## Sources and standards decisions

The Content timing wins over the earlier screen summary: Autumn Leaves is 20 seconds; Rush Hour is 13.846 seconds.
Room phrases have 28 movement counts and 16 lead-in counts: 26.4 seconds at 100, 33 seconds at 80, plus calls.
The stage geography matches National Park Service and Music Center teaching material.
Ballet court history matches Paris Opera; terms match San Francisco Ballet's Nutcracker Family Guide and Pittsburgh Ballet Theatre's Ballet Vocabulary.
Jazz origins and rhythmic variety match Jacob's Pillow essays. These two original studies do not define whole styles.

The spec's DA:Re9 claim is broader than this comparison activity. The NCAS handbook chiefly puts identifying style
traits under DA:Re7; DA:Re9 asks for evaluation with criteria and reasons. Notes no longer claim full Re9 coverage.
Changing the shared catalog or adding an evaluation activity exceeds this review's write and topic scope.
The specified title and long main-idea choices remain; movement evidence is independently required to pass.

## Sensitivity

A fresh cultural reviewer should check the short jazz history and the original theatrical-jazz study against the
broader African American vernacular tradition. The history retains African American credit.
Inspect the people contact sheet and animated cast for representation and readable, dignified movement.
No style is assigned by skin tone, hair, body or gender. Smaller and seated student movements are supported in notes.

## Engine changes wanted

- `kit/dance.js`, `floor().resize`: make x0/x1 describe actual front-edge pixels for the stage's d0=140 projection.
- `kit/dance.js`, floor projection/inverse and figure projection: add an orbit/mirror interface with a correct inverse,
  preserving hand identity and avoiding negative-width decoration. The tool currently uses a local adapter.

## Review evidence

Scratch holds cold play, no-watch guessing before/after, evidence and board sweeps, exhaustive 8,000-case call checks,
voice walks/repeats, keyboard and drag checks, phone and compact frames, arithmetic and the one final review audit.
See `codex-review.md` for the audit's actual disposition and any remaining limitations.
