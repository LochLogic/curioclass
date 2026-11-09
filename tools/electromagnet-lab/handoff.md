# Electromagnet Lab handoff

Build only. No commit, deployment or separate polish round. The final build report is codex-report.md.

## Structure

src.html starts from kit/starter/src.html. The order is responsive layout, stable controls, content and state,
fair-test model and actions, DOM rendering, workbench drawing, Field and Notebook, then input bindings.
The kit owns Motion, Sound, Read, tones and the narration queue. No family engine applies.
All moving scientific geometry and the chart are SVG. Twenty generated illustrations are embedded by the bundler.
The standalone file is electromagnet-lab.html. No data file or outside library is loaded by the tool.

## State and gates

Only completed rows are saved in guarded localStorage curio-emlab. Their means are recomputed on loading.
Each row is unique by bench and settings. Retests replace it. A setting change or mode change cancels an active test.
Boards start empty and can only gain a question through differences between class-data rows.
Fair rows match every other current setting. Minimum values and a non-flat spread are independent gates.
First claim and ratio picks are retained. A displayed correction never converts the first answer to a right answer.
The spec's tested, fixed and found, fixed labels mean corrected evidence, not independent mastery.
Claim evidence is frozen after the first pick, except that a too-small ratio can receive a stronger fair set.
Core and Rubbing go directly from their claim to the tested mark. They have no ratio task.

Field has two point poles, a one-unit north Earth field and an exclusion zone around the coil.
Compass movement uses pointer capture or half-centimeter arrow-key steps. A drops an arrow, capped at 40.
Checklist turns use the displayed needle angle after its 0.3-second ease. Instant on/off tapping cannot claim a turn.
Fresh filings use fixed seeded positions and the coil component, so reversing polarity preserves their shape exactly.
The student must sprinkle before a flip and again after a completed turn to unlock the direction question.
Notebook fair runs last three seconds. Next case is live during a run, which cancels rather than silently finishing.

## Art and voice

All 20 specified paintings were generated individually with the built-in image tool during the build.
Every asset has people:false and drawn_by:codex. The manifest has full prompts and the common painted-realism style.
Five first candidates were redrawn: three paper scraps came back as scenes; the table and notebook had distracting apparatus.
The clip dish was redrawn to neutral frosted glass after key removal tinted the transparent glass.
Raw originals are in art/raw and final WebP files are in art. Only art.py --rekey was used for processing.
Art previews, contact sheets and discarded build evidence stay in Scratch.

voice/lines.json declares provider voice Algenib, bank gravel-ranger and the warm shop-teacher direction.
No audio was recorded in Build.
Curio.voice currently falls back to browser speech, so a browser voice is not the specified recorded performer.
How-to lines are once per page load; events use unique queue keys. Read speaks the current hint and the initial data summary.

## Settled choices and contradictions

The spec lists no Open questions. No user questions were asked in this unattended build.

- The user's image-tool instruction supersedes the spec's older Local FLUX route. No people are needed in this scene.
- The seven-line preview mistakenly counted 21 images. The full spec lists 20, all present and used.
- The maximum model mean is 36, while the required noise formula allows a trial of 40. The formula and 40-clip dish win.
- Done when 1 requests 4 times from 10, 20 and 40 turns at one battery. Its 10-turn mean is 3, below its own ratio gate of 4.
  That setup can compare 20 to 40, about 2 times. At two batteries the 10-to-40 comparison is eligible and gives about 4 times.
- Magnetic field scales with turns and current. Actual lifting force and clip count need not. The spec's linear count rule is
  retained as a labeled model; notes explicitly distinguish the physical field relation from this teaching approximation.
- The field's shape would not stay identical if the one-unit Earth component were also used for filings on reversal.
  Filings show the coil component, while the compass includes Earth. This follows the spec's intended shape/direction lesson.
- Full class rows, comparison chips, board and controls cannot all remain open in the short previews. After two inline rows
  are selected they fold to the compare strip and a Class data button. Full rows remain available in that dialog.
  At short landscape sizes the Class data button shares the hint row and the board uses four columns, preserving 44 px targets.
- Answer cards temporarily fold the settings. After a first pick, unrelated distractors fold away and the chosen and supported
  answer remain. This keeps every available choice visible before the first pick and the correction visible afterward.
- At 760 wide the stage stays at 16:10 and is centered narrower than the page so the controls fit the same viewport.
  At 375 wide the stage fills the width. The results table follows the controls and can require page scrolling on a phone.
- Cold review retained the supported claims and rewrote distractors with the same misconceptions and comparable lengths.
  The original longest-answer shortcut solved all three Notebook cases. It no longer does; first answers still remain final.
- The brief asks for an early tool report, while the user says to stop as soon as it is written. An early report draft was kept
  in Scratch and the tool report is written only as the final build action.

## Evidence

Scratch is S:/CurioClass-codex/_scratch/electromagnet-lab. numbers.json enumerates all 192 coil settings and 20 Static settings.
model-checks.json independently checks numerical anchors, 40,000 ratio sets and palette contrast.
checks.json records the full functional and cheat walk. claims-checks.json tests every direction option, Core's four-value gate,
and the four ratio families. field-checks.json includes the rapid-toggle attempt and observed needle-turn checks.
The initial oversized drive expression exceeded its internal 60-second evaluation cap. The bounded CDP runner launches the
scenario and polls small results instead. Subsequent scripted checks complete; this does not modify the shared driver.
size-frames contains the one full size pass. phone-frames covers the real 375 px iframe and other work states.
input-frames checks real jittered dragging and keyboard movement. Voice and final audit evidence are in Scratch too.
Build and check commands run from the authorized root with deadlines. Chrome uses only assigned ports, with muted audio.
The iframe server uses 8785 and is stopped after its shots. No host.html is created inside the tool folder.

## Sensitivity

No cultural, religious, historical or body content. No people appear in the illustrations.
Science and electrical heating claims are sourced in notes.md. This is an on-screen lab, not instructions for wiring a real coil.

## Engine changes wanted

None. No shared kit, engine, documentation or other tool was edited.

## Left open

Recorded Algenib narration remains for the owner's recording pipeline, as requested by Build only.
The default 4-times numerical example needs a future spec correction. The spec file was left unchanged.
The build's fast-voice failure was repaired in cold review; the held-click walk now hears the how-much instruction,
all mode welcomes after the permitted first-tap skip, and all three fair-result events. Review evidence supersedes the build timing note.
Desktop headless checks do not establish actual school-device performance or human audio quality.

## Cold review repairs

The review first played the bundle without reading this handoff or the build report. Its evidence has the review-
prefix in Scratch. The new review report is the current disposition; codex-report.md preserves the original build evidence.
Coil and Static expose their comparison on entry. Their numeric chart axes use actual distances between settings.
The six supported claims are unchanged. Distractor wording balances lengths while preserving the original wrong ideas.
Results are brief enough for two-second input. Obsolete how-to lines stop when their action is taken; results stay whole.
The Field switch stays available during its question, and warming does not replace the question's instruction.
A filings sample records its polarity. A later opposite-polarity sample unlocks the question, even after an early flip.
The fourth checklist item now expires its observation after the displayed needle settles. Changing the core, position,
power or other coil settings cancels that observation. A small real turn gets a stronger-setup cue, with a compact version.
Notebook's fair runs show both settings and the changing counts. Case 3 uses the painted brass compass, dial ticks,
glass and metal highlights, and a centered needle instead of the plain circle. The same alignment fixes the Field compass.
The existing compass painting was rekeyed with despill and handle-hole removal. No new paintings or recordings were needed.
The review uses only Chrome 9960 through 9967 and the temporary host on 8765. Shared kit and scripts are unchanged.
The single independent review audit exited on its internal 60-second CDP domain-enable timeout before making
audit.md or any frames. It was not rerun under the incomplete-audit stop rule. Review audit coverage of 800x500,
1000x625, 1280x720, 1920x1080 and 760 wide remains unverified; earlier builder evidence is not a substitute.
The review directly inspected 680x425, 1366x768 and a real 375x812 iframe. The failure receipt and closeout hashes
are in Scratch/review-audit-failure.md and Scratch/review-closeout.json. All assigned ports were closed at closeout.

## Initial audit repairs

The audit was run once. Its original leads are retained, with dispositions in the report.
The compact Class data button now sits beside a narrower hint. Mobile header controls keep readable words at 10 px.
Dialog titles reserve space for Close. Header button widths are stable when Sound changes.
Short Field previews fold the shared controls into Coil settings and show four compact checklist labels.
The dialog uses fresh button clones with shared state and guarded focus restoration. A held-click check changed batteries to 3.
Closing it restores the relevant Field instruction. Full laptop layouts retain all three setting rows.
Answer cards fold unrelated controls until their one allowed choice is made; the filings result has Back to paper.
The paper and notebook fill the workspace when results are hidden. Scene captions have light plaques for contrast.
Post-frames, post-phone-frames, last-phone-frame and dialog-frames verify the affected states without a second full audit.
The audit's initial phone copy predates these repairs; the focused phone checks use the final source and bundle.
All 48 original audit leads are answered in the report. All 74 audit PNGs were inspected in 20 numbered contact sheets.
Seven focused resize checks preserve all four modes and complete Coil, Static and Notebook animations across resizing.
Original resize leads used header coordinates from before its width repair; fresh held clicks use each current button's position.
All started Chrome instances and the port 8785 server are closed. final-checks.json records cleanup and artifact integrity.
