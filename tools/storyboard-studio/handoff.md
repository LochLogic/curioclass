# Storyboard Studio build handoff

## Built
One offline HTML tool with Plan, Board and Animatic, two original scenes, actual camera projection, editable boards, continuity markers, sample repairs, local saving and grayscale printing. No commits or polish round.

## Source map
- `src.html` starts with kit styles and the 9-12 theme, then responsive desk, monitor, plan, cards and dialogs.
- The inline script defines scene beats, voice lines, panel factories, persistence, lens geometry and continuity checks first.
- `drawShot` is a small painter's 3D renderer. It clips polygons at the near plane, projects with the actual lens, shades spheres and capsules, and draws the fixed beat's set and poses.
- `drawPlan` draws real-pixel floor plans, one-meter grids, camera wedges, ghosts, character facing and the yellow line.
- `renderBoard`, `renderStrip` and `renderTimeline` build the three sequence views. Strip and timeline nodes stay stable while selection changes.
- `moveCamera` owns bounds and collision checks. Its drag transform is frozen for the gesture so a panning plan does not jitter under the pointer.
- `start`, `enterFrame`, `tick`, `endPause` and `jumpTo` own playback. Timing carries the scheduled deadline across cuts; diagnostics log actual presentation times too.
- `printBoard` builds six grayscale panels per print page, including shot metadata, beats, times, transitions, cut notes and missing beats.
- `window.__tool` exposes state, scene data, geometry, checks, rendering, playback and voice logs for review.

## Data and save behavior
The two student boards live under `storyboard-studio-boards` in localStorage. Storage reads and writes are guarded. Each edit saves both student boards. Practice samples are separate in-memory copies and never replace the saved boards. Reloading restores the student boards, not the practice copy. Clear board confirms and resets only the currently active board.

## Decisions and spec questions
The spec lists no open questions.

- Lens calculations use exact full-frame geometry, rather than rounding the displayed field-of-view table before calculating frame height.
- At shared shot-size cutoffs, 0.3 is close-up, 0.6 is medium close-up, 1 is medium, 2 is wide and 6 remains wide. These choices are documented in teacher notes.
- Dissolves and fades take the first 0.5 second, or the whole panel if shorter, within the chosen duration. Motion off holds the incoming image for that time.
- Near diner walls use cutaways when the camera is outside the room. Otherwise the specified opening camera would film the outside of the door wall.
- An overhead camera looks straight down at its floor-plan position. It does not silently slide above the aim point.
- At compact sizes the panel chip strip becomes the current-panel and adjacent-cut summary at the top. Prev and Next still navigate. The full sequence remains in Board. This keeps the viewfinder, camera and Add panel visible.
- The smallest landscape layouts use a plan inset. At 1000x625 the plan sits below the viewfinder. Compact Board hides Plan fields to give its cards more space. The phone Plan view stacks viewfinder, plan, hint and controls. Phone Board puts the compact scene and hint above the cards.
- The exact ratio of timeline block widths follows panel durations. Long mixed-duration boards scroll horizontally so even a half-second block keeps a 44 px target.
- The line teaching cue precedes new cut warnings on the first Add action. It is heard once; stale queued events are dropped as panels change. A one-panel Board welcome names Add panel and Fix this board rather than asking for an impossible reorder.
- The bus anchor at `(x, 3)` is the door target specified in the aim table. The body extends behind that plane onto the street. Its window and door details render with the front surface so oblique views do not hide them under their own bus body.
- Doors stay closing through beats five and six, and reopen on seven. The tray's small illustrative slide persists through beats seven and eight; both the plan and Slice aim follow it.

## Art made
One generated desk backdrop, `art/editing-desk.webp`, made with the built-in image tool. Full prompt and house style are in `art/prompts.json`; raw PNG is in `art/raw/`. Finished WebP inspected at 1500x844. It decorates the desk only. Every viewfinder drawing and the floor plan remain code so all angles are truthful. No people or body parts were generated.

## Voice
Bank: smooth-narrator. `Curio.voice` owns the queue, Read, Sound and heard keys. No recorded audio was made, as instructed. Browser speech is the runtime fallback. The full fixed-line list is in `voice/lines.json`.

## Checks and evidence
All evidence is under `_scratch/storyboard-studio/`.
- `numbers.py` and `numbers.json`: independent lens fields, sample frame heights, maximum time and contrast calculations.
- `functional.js` and `functional-results.json`: threshold, sample, neutral, jump cut, timing, collision and immediate-control assertions.
- `full/`: the one full STANDARDS size pass, all viewed. `targeted/` and `last/`: only touched states after build fixes.
- `student-check.py`, `student-results.json`, `student/`: real held taps and keyboard repairs, full animatic, print, reload and voice checks.
- `voice-final.json`: five held Add taps at two-second pace. The teaching line starts once, events can recur, stale queued events are dropped.
- `bar/` and `snowy-bar/`: opened existing bundled bar tools. Their source and neighbor handoff/review were read. They were not rebundled, because that would write outside the two authorized folders.
- `audit/`: one final mechanical audit, with its own Chrome profile and host port 8795. See codex-report.md for its result and lead dispositions.

## Final audit and targeted build corrections
The audit finished in 1408 seconds with 67 leads. It found no console errors, infinite motion, resize exceptions or controls left disabled by resizing. All 69 audit PNGs were reviewed in eight contact sheets; problem states were also opened individually.

After that one audit, compact Board gained picture space, header toggle widths became stable, repeated current-mode taps stopped interrupting welcomes, the current panel chip scrolls into view, and timeline progress updates immediately. Stopped partial transitions now survive a redraw and playback ends on the complete incoming image. Bus door geometry and attached details were corrected. The audit was not rerun after these fixes.

`post-audit/` verifies the affected layouts, a keyboard-only reorder run, two spoken lineCrossed events from two new crossings, intact welcomes, full label hit areas and active-panel visibility. `final-targets/` verifies bus drawing and beat continuity, held fade pixels across a redraw, first-chip welcome and all 31 functional assertions again. Both batches report zero console errors.

The final audit-state file removes the mistaken requirement that the inactive background hint remain uncovered while a modal owns focus. It keeps the actual modal controls instead. Long phone boards also no longer claim that their entire grid and bottom notes must fit in the first viewport.

## Engine changes wanted
None. No kit, documentation, script or other tool was edited.

## Review cautions
The renderer uses depth-sorted shapes, not a full depth buffer. Very close or unusual placements can expose intersecting mannequin and prop surfaces. Inspect framing and educational accuracy, not photorealism.

On a phone the long Board scrolls as a page. Its primary scene, Add and reorder/sample controls are above the cards. Plan's less frequent lens, beat and duration controls follow the first visible action rows.

The strict short-choice audit rule remains a review lead for long authored boards and the twelve-panel strip. The tool preserves all notes and 44 px targets rather than squeezing an entire board into a small preview. Phone secondary parameters also require page scrolling. These are documented limits, not claims of an entirely clean mechanical audit.

Raw browser speech can hold the queue longer than natural recorded clips. The queue prioritizes the first line lesson, drops superseded queued events and keeps Read interruptible on a mode change. No claim of listening to recorded narration is made.

## Cold review, 2026-11-04

The cold reviewer played both scenes and all modes before reading this handoff or the source. The editing desk, shaded mannequins, marker-gray sets, exact sample cameras and continuity geometry were retained.

- Modal Read buttons speak the active cut explanation or Clear confirmation. Modal entry hushes background narration, and welcomes are invalid while a dialog is open.
- All Board hint variants, collision feedback, modal instructions and complete dialog readings are now registered in `allLines()` and `voice/lines.json`.
- The floor-plan line label moved away from camera numbers. The procedural slice gained a shallow shaded edge, crust and flat toppings; its details render with its surface. The sharing beat separates the halves, and the looking-at-slice beats now lower the nose wedge.
- Animatic completion shows this board's panel count and total running time.
- Camera clearance now respects height: High and Overhead are above the table and actors. `cameraBlocked` handles Low/Eye footprints; `clearCamera` finds a nearby free position if a beat or height change creates a collision. This prevents zero-distance views when Nico moves into a camera and permits centered overhead shots. Hints distinguish Plan from Board and explain the next control.
- Dialogs keep their action row visible while long combined explanations can scroll. Closing or cancelling hushes Read; the Finished status clears on context changes. Sharing halves stay near the specified table-height Slice target.
- The audit states include the sharing beat. All review evidence uses `review-*` paths in Scratch, separate from build evidence.

The independent review checks passed 43 assertions, actual held keyboard repair/reorder, jittered pointer reorder, phone primary-control visibility, real reload persistence, practice-copy isolation, grayscale print notes and no external requests. Recomputed lens fields, sample heights, continuity thresholds and timing agree with the spec. Motion on/off panel presentation stays within 50 ms. Review voice logs show one line lesson in five Add taps and two spoken events for two fresh line crossings.

Review audit outcome and final scoped corrections are recorded in `codex-review.md`, written after the audit and rechecks. Long authored sequences and phone secondary fields still require scrolling; this is a documented tension with the blanket no-scroll checklist, retained to preserve the specified pictures and 44 px controls. No recorded voice was made.

The review audit completed once in 1571.5 seconds with 56 leads, no console errors, no infinite animation and no resize exceptions or stuck-disabled controls. All 72 audit PNGs were inspected in 20 contact sheets. Its lead groups are fully answered in the review report. The final geometry/dialog/status corrections received scoped rechecks, not another full audit: 11 assertions passed, combined-warning buttons fit at 680 and 375, and all 37 voice strings match the manifest. Final frames are in `review-final-checks/` and `review-final-phone/`. A temporary host-only favicon 404 was corrected in the test harness and the affected phone shot rerun cleanly. Test hosts and Chrome instances were closed.

The final audit disposition also adds an explicit scroll cue to the practice-board hint and marker narration. `review-scroll-check/` confirms the cue speaks and remains unclipped at 1366x768 and 680x425. The final offline bundle is 280,381 bytes.

All test Chrome processes and temporary host servers are closed by their runners. `host.html` is removed by the phone runner. The audit serves its own host inside Scratch.
