# Storyboard Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: storyboard-studio

#### Built

Plan, Board and Animatic for The Last Slice and Late Bus. Actual full-frame projection, camera dragging and keys, four lenses and heights, fixed script poses, up to twelve panels, live continuity checks, practice copies, local saves and grayscale printing.
One self-contained offline HTML file with kit theme and Curio.voice. No commits, branch changes or polish round. Only the authorized tool and Scratch folders were used for project writes. Final report is written last to honor the user's stop-on-report instruction.

#### Numbers check

PASS. Independent Scratch script reproduces all source calculations: fields 45.7473, 32.2688, 22.8952 and 13.5859 degrees; sample frame heights agree after rounding; final sample turn 9.9594 degrees. Maximum 96 seconds; samples 16 and 12 seconds.
Contrast: accent/panel 6.24:1, accent/section 5.91:1, brand ink/accent 6.60:1, yellow line/panel 12.00:1, dark ink/paper 9.55:1. No source-number disagreement.

#### Feel check

Best: moving the sample's sixth camera across the plan removes two line crossings at once, then a new angle on panel eight removes the jump. The complete sixteen-second scene plays with all eight beats intact.
Flat moment 1: the outside opening camera saw the door wall. Cutaway walls, consistent ground layering, shadows, floor texture and the generated desk now reveal a coherent diner immediately.
Flat moment 2: long cut warnings starved the first line lesson during five rapid Add taps. The once-only line lesson now starts first; superseded event lines are dropped.
The small Board also gave too much height to Plan fields. Its compact layout now uses that space for pictures. This is a build correction, not a separate polish round.
Compared with Beat Lab and opened Snowy Mail Route. Scratch feel-comparison.png puts the tools beside each other. The cinematic desk, camera monitor and shaded mannequins hold their own; the drawing remains an intentional working storyboard.

#### Done when

1. PASS: seven computed frame-height cases include every cutoff. Names and exact geometric heights agree.
2. PASS: sign and boundary tests at -0.3001, -0.3, zero, 0.3 and 0.3001; overhead and neutral shots suppress line crossing. Real keyboard repair changes Side B through neutral to Side A.
3. PASS: both sample marker lists exactly match the spec; both listed fixes clear them.
4. PASS: 29 degrees flags a jump; 31 degrees and a two-size-step change do not.
5. PASS: four half-second panels, Cut/Dissolve/Fade, Motion on and off stay within 50 ms. The real eight-panel run ends in 16.009 seconds.
6. PASS: synchronous Stop, Step, Back, timeline and Show problems assertions; crossed-line pause appears and is dismissed at once. Stop preserves exact canvas pixels.
7. PASS: Plan prioritizes the viewfinder, Animatic uses the whole available stage, Board owns its grid. Checked at laptop and compact sizes.
8. PASS: real drag changes [1,2] to [2,1]; a keyboard-only run enters Board, adds a panel, moves it earlier to [2,1], then later to [1,2], preserving focus. Last-panel deletion is disabled. Missing beats are listed.
9. PASS: print DOM is six plus two panels with all 24 note paragraphs; rendered pixels are grayscale. Saved boards compare equal after an actual reload. Practice repair leaves My board at one panel.
10. PASS: viewfinder, plan and Add are visible at every required size. At 375x812, Add ends at y=766.8 and hint is in view. No sideways scrolling after phone layout repair.
11. PASS: five held Add taps at two-second pace speak lineHow once; repeated jumpCut events start and superseded queued events drop. Two fresh line crossings each speak lineCrossed. Read and Sound recovery pass. A clean one-panel board never speaks markerHow. Quick current-mode taps now preserve each welcome. Browser speech is the fallback; no recordings were made.

#### Wave lessons

- Hint and voice: PASS. State updates hints immediately; one-panel Board and full Plan name enabled next controls. Read follows the current hint. How is selected by V.heard.
- Focus and layout: PASS with the documented scrolling limits below. Stable strip/timeline nodes; deliberate focus recovery uses preventScroll; no focus on load.
- Sizes: PASS with the documented scrolling limits below. Required size sweep, 375 iframe, 44 px controls and reserved hint space.
- No giveaways: PASS. This is an authored studio, not a hidden-answer quiz; markers explain actual geometry.
- Honest numbers: PASS. Focal length, physical height and shot name are explicit; teacher notes give frame formula, cutoffs and transition assumption.
- Standards: PASS. Solo shot planning, board development, continuity repair and retiming teach all four codes.
- Motion off: PASS. Tally animation stops; still transitions keep panel duration.
- Short choices in view: FAIL under a literal no-scroll interpretation. Long authored boards and the twelve-panel strip intentionally scroll; phone secondary parameters follow the primary controls. No answer set is hidden.
- Resize mid-animation: PASS. The completed audit found no exceptions or controls left disabled after every tested resize.
- Welcome after first tap: PASS. Mode scope, entry revision and played state prevent stale welcomes.
- Unknown as unknown: PASS, not applicable. Both fictional scripts and fixed blocking are public.
- One look, one meaning: PASS. Dashed yellow axis, numbered camera ghosts, red selected camera; warnings have icon and words.
- Badge says what is true: PASS. My board versus practice copy and current side derive directly from state.
- Hint changes back: PASS. Mode, panel and scene changes recompute the current instruction.
- No answer by copied words: PASS, not applicable. Students compose and diagnose cuts; no answer-card matching.

#### Audit leads

Completed once in 1408 seconds, exit 0: 67 leads, retained in `_scratch/storyboard-studio/audit/audit.md`. No console errors, infinite motion, resize exceptions or stuck-disabled controls. No full rerun after targeted fixes.
The A numbers below follow the audit's 67 leads in section order, grouping repeated findings without omitting any.

- A01-A06, Sizes/phone parameters: retained page-flow limit. Aim, Lens, Height, Duration, Beat and transition follow the primary action rows. Viewfinder, camera, hint and Add fit without scrolling, as Done when 10 requires.
- A07, one-panel Board at 680: fixed. Compact Board now hides Plan fields; its grid grew to 179.5 px and shows the complete first card. New 680, 800 and 1000 frames inspected.
- A08-A09, Animatic checkbox targets: false positive on the 21 px glyph. Clickable labels measure 79.5x44 and 115.1x44; clicking the label changes its checkbox.
- A10-A15, two-panel phone parameters: same retained page-flow limit as A01-A06.
- A16-A19, sample Board scroll panels: improved compact picture space; scrolling retained for the long authored board. All panels and markers remain reachable. This is the strict wave-lesson FAIL above.
- A20-A26, lower phone panels/markers: retained long-board page flow. No content omitted.
- A27-A28, whole phone grid and notes keep regions: corrected audit-state assumptions. A long authored page cannot keep its bottom notes in the first viewport; the state now keeps the primary sample/My board controls.
- A29, marker-dialog hint coverage: expected modal occlusion. Removed the inappropriate global background-hint keep requirement.
- A30-A31, underlying Board scroll content during marker modal: inactive background content. The modal owns focus and has its own diagram, explanation, Close and Go to panel.
- A32-A35, lower phone panels behind marker modal: same inactive background/page-flow explanation.
- A36-A37, phone hint outside viewport during marker modal: expected after scrolling to a marker. The active instruction is in the modal; the background hint is inert.
- A38-A39, bus phone Aim/Beat: same parameter page flow as A01-A06.
- A40, hint covered by Clear confirmation: expected modal occlusion; corrected global keep constraint.
- A41-A46, phone parameters behind Clear confirmation: inactive background plus documented parameter page flow.
- A47-A48, playing checkbox targets: same measured 44 px label hit areas as A08-A09.
- A49, viewfinder sample points covered by captions: expected, specified caption overlay. Captions can be turned off immediately; the frame itself is fully in view.
- A50, twelve-panel strip sideways: retained authored-sequence scroll. Added automatic reveal of the active chip; panel 12 is wholly visible inside the strip after selection. Prev/Next remain available.
- A51-A56, maximum-board phone parameters: same page-flow limit; primary camera, frame, hint and Add/Delete region remain visible.
- A57-A59, idle Stop/Back/Step changed nothing on a single frame: expected boundary behavior. Multi-panel playing and paused assertions verify all three act synchronously.
- A60-A61, Add/Duplicate skip welcome: required first-tap behavior when their own line lesson starts. Welcome remains unmarked and can be heard on another valid mode entry.
- A62, first panel-chip tap skipped welcome: fixed. Re-selecting the current panel no longer invalidates the welcome; a held first-chip tap speaks welcomePlan.
- A63-A64, Add/Duplicate event loss: stale panels were superseded by new edits, so their queued cut warnings were dropped as required. Visible markers and tones answer immediately. The current event speaks when its state remains current; two fresh crossing events were independently verified.
- A65-A67, quick mode taps cut welcomes: fixed. Current-mode taps no longer hush narration; all three welcomes start and have no cut flag in the targeted 0.7-second test.
Header toggle shifts were also corrected: measured movement is zero. Stopped fade frames survive a redraw, final transitions end on the full incoming frame, and bus door details stay attached to their actual target surface. Targeted batches have zero console errors.

#### Frames looked at

All manual shots in first, second, checks, full, targeted, student, voice, last, phone-modes, phone-animatic-final, post-audit and final-targets. The early blank/overlap frames were inspected and repaired. All full-size frames and the grayscale, print, pause, drag and keyboard frames were opened. All 69 audit frames reviewed in eight contact sheets, with affected states also opened individually. The final functional batch passes all 31 assertions.

#### Art made

One generated editing-desk image, 1500x844. Full prompt: art/prompts.json. Built-in image tool, copied into art/raw, processed only with art.py --rekey editing-desk. No redraw needed. Final art 115.0 KiB; bundle 268.4 KiB (274,841 bytes), below 2 MB.

#### Art still to paint

None. No generated people, faces or body parts. Viewfinder mannequins and sets are code, as the spec requires.

#### Engine changes wanted

None. No shared files changed.

#### Left open

- No recorded narration, as instructed; smooth-narrator metadata uses browser speech at runtime.
- Depth sorting is a simple storyboard renderer. Very close or oblique views can expose intersecting/coplanar surfaces.
- Compact layouts replace the chip strip with a live current-panel/adjacent-cut summary. Full Board and Prev/Next preserve access.
- Full audit was not rerun after the targeted build fixes listed above. The cold reviewer should use the final bundle and final audit-state file.

- Long authored boards and phone secondary parameters require scrolling, as detailed in the audit dispositions.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: storyboard-studio

#### Played

Cold, as a grade 10 student alone, with a projected-class view considered: composed a sequence, played both samples through, inspected cuts, repaired cameras, reordered, retimed and printed. Played before reading builder notes or source. Walked Teaching, Play and Craft personally. Strong studio atmosphere and immediate camera feedback; the ending needed a clearer visual payoff.

#### Findings fixed

- Blocker, general, Plan: floor-footprint collision checks blocked cameras above objects, preventing centered overhead framing. A beat could also move Nico into an Eye camera. Clearance now respects height, and beat/height changes move an obstructed lower camera to a nearby clear position with an explanation. Rechecked High, Overhead, lowering and Nico's moving beat.
- Should fix, general, dialogs: Read was inaccessible behind native modal focus and its callback read the background hint. Added modal Read, active explanation/confirmation text, next-action narration and stale-welcome guards. Close, Keep and Escape hush speech. Combined explanations scroll while their action row remains visible.
- Should fix, general, voice: dynamic Board/collision hints were absent from the line registry. All variants and complete dialog readings now appear verbatim in allLines and voice/lines.json. Overhead hints explain the next action and distinguish Plan from Board.
- Should fix, general, mini-plan: The line label collided with camera numbers. Moved it into open space.
- Should fix, general, Board: the first sample view could name markers below the visible grid without explaining how to reach them. Added an explicit scroll cue to its hint and narration; checked it at laptop and compact sizes.
- Polish, general, renderer: the slice was a flat shape and the final beat barely changed. Added a shallow shaded wedge, raised crust, flat toppings, downward-looking poses and two separated halves near table height. Kept the marker grays and camera-dependent drawing.
- Polish, general, Animatic: playback ended without a clear status. Added Finished with this board's panel count and running time; it clears when the context changes.

#### Findings left

- Polish/spec tension, general: long authored boards, twelve-panel strips and mixed-duration timelines scroll. Phone secondary fields follow the first viewport. Readable pictures, 44 px controls and the specified stacked phone layout prevent satisfying the blanket no-scroll checklist simultaneously. The primary viewfinder, camera and Add remain visible.
- Nit, general, renderer: very close or oblique placements can expose painter-sort intersections. The working-storyboard renderer is retained.

#### Flattest moment left

The sample's final camera still aims at Remy during Ash's sharing action. Its exact coordinates and target are prescribed and produce the jump-cut exercise. A student's wider or Ash-facing revision shows the action better. The sharing pose and prop now visibly change when framed to include them.

#### Graphics

Checked the existing 1500x844 editing-desk image at final size and in the layouts. No generated people, missing art tokens or placeholders. Kept the backdrop; redrew the procedural slice and adjusted poses because arbitrary camera projection requires code. No new raster assets. Existing bar comparison inspected without writing to other tools. Final bundle: 280,381 bytes, about 274 KiB.

#### Audit

Completed once in 1571.5 seconds, within the 40-minute limit: 56 leads, no console errors, no infinite motion, no resize exceptions and no stuck-disabled controls. Evidence: `_scratch/storyboard-studio/review-audit/`. All 72 audit PNGs inspected in 20 contact sheets. No second full audit; final fixes received scoped rechecks.

Lead numbers below follow the report's rows in order:

- A01-A06: phone secondary fields below the first viewport. Retained layout limit above; independently measured Add bottom at 766.8 px in the 375x812 iframe, with viewfinder and camera visible and no horizontal overflow.
- A07-A08: 21 px checkbox glyphs. False positive: their clickable labels measure 79.5x44 and 115.1x44 px.
- A09-A14: two-panel phone secondary fields. Same retained page-flow limit as A01-A06.
- A15-A23: sample cards/markers outside the initial grid or phone viewport. Added spoken and visible scroll guidance; retained the authored sequence's readable pictures and all cut notes.
- A24-A30: scrolled background cards and hint behind a marker modal. Inactive background; the active diagram, explanation, Read, Close and Go to panel are visible. Rechecked a combined warning at 680 and 375.
- A31-A32: Late Bus phone Aim/Beat fields. Same secondary-field page flow.
- A33-A38: secondary fields behind Clear confirmation. Inactive background; the active confirmation and its three controls fit.
- A39-A40: playing-state checkbox glyphs. Same measured 44 px label targets as A07-A08.
- A41: viewfinder sample points covered by captions. Specified caption overlay, immediately switchable; the viewfinder itself is fully in view.
- A42-A48: twelve-panel strip scrolling and phone secondary fields. Retained sequence/page flow; active panel 12 is revealed and navigation remains available.
- A49-A51: Add, Duplicate and Clear skip the welcome. Required first-tap behavior: their own relevant line starts instead. Welcomes remain scoped and unmarked when skipped.
- A52-A54: idle Stop/Back/Step change nothing on a one-panel board. Expected boundary behavior; multi-panel playback assertions confirm immediate control actions.
- A55-A56: older Add/Duplicate warnings dropped as newer panels supersede them. Required staleness behavior, confirmed in the revision checks and logs; two fresh line-crossing events spoke twice.

43 independent functional assertions passed before the final scoped fixes; 11 scoped assertions passed afterward. Recomputed lens fields, all sample frame heights, 96-second maximum, exact sample markers, neutral boundary and 29/31-degree cases. Motion-on/off panel timing stayed within 50 ms. Real held keyboard repair/reorder and jittered pointer reorder passed. Reload preserved boards; practice copies stayed separate. Print is grayscale with patterns and notes. Checked every required size, phone iframe, grayscale and touched frames. Contrast: accent/panel 6.24:1; button ink/accent 6.60:1. All four standard codes are practiced through planning, ordering, continuity repair and retiming. No hidden-answer or unknown-clue mechanic applies.

Voice counts:

| Line/action | Kind | Expected | Spoken |
|---|---|---|---|
| lineHow across five held Add taps, 2 s apart | how | 1 | 1 |
| Two fresh line crossings | event | 2 | 2 |
| Dialog Read | read | Current dialog | Matched |

All 37 runtime line strings match the manifest. Audit rapid-tap checks were clean. State hints update immediately, focus survives reorder, warnings pair words with icons, and Motion off preserves timing. Final desktop and phone rechecks have no tool console errors. A host-only favicon 404 was corrected in the temporary harness and its affected shot rerun cleanly.

#### Left open

- No recorded narration, following the no-recording build rule. Browser speech remains the fallback.
- Phone secondary fields and long-sequence scrolling are documented limits, not an entirely clean mechanical-audit claim.
- High/Overhead clearance uses the specified physical heights above the actors and table; no scripts, sample cameras, continuity thresholds, topics or modes changed.
- No commits. Review writes stayed in the two allowed folders. Test Chrome instances and servers are closed; host.html is absent. This report was written last to honor the stop instruction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Storyboard Studio build handoff

#### Built
One offline HTML tool with Plan, Board and Animatic, two original scenes, actual camera projection, editable boards, continuity markers, sample repairs, local saving and grayscale printing. No commits or polish round.

#### Source map
- `src.html` starts with kit styles and the 9-12 theme, then responsive desk, monitor, plan, cards and dialogs.
- The inline script defines scene beats, voice lines, panel factories, persistence, lens geometry and continuity checks first.
- `drawShot` is a small painter's 3D renderer. It clips polygons at the near plane, projects with the actual lens, shades spheres and capsules, and draws the fixed beat's set and poses.
- `drawPlan` draws real-pixel floor plans, one-meter grids, camera wedges, ghosts, character facing and the yellow line.
- `renderBoard`, `renderStrip` and `renderTimeline` build the three sequence views. Strip and timeline nodes stay stable while selection changes.
- `moveCamera` owns bounds and collision checks. Its drag transform is frozen for the gesture so a panning plan does not jitter under the pointer.
- `start`, `enterFrame`, `tick`, `endPause` and `jumpTo` own playback. Timing carries the scheduled deadline across cuts; diagnostics log actual presentation times too.
- `printBoard` builds six grayscale panels per print page, including shot metadata, beats, times, transitions, cut notes and missing beats.
- `window.__tool` exposes state, scene data, geometry, checks, rendering, playback and voice logs for review.

#### Data and save behavior
The two student boards live under `storyboard-studio-boards` in localStorage. Storage reads and writes are guarded. Each edit saves both student boards. Practice samples are separate in-memory copies and never replace the saved boards. Reloading restores the student boards, not the practice copy. Clear board confirms and resets only the currently active board.

#### Decisions and spec questions
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

#### Art made
One generated desk backdrop, `art/editing-desk.webp`, made with the built-in image tool. Full prompt and house style are in `art/prompts.json`; raw PNG is in `art/raw/`. Finished WebP inspected at 1500x844. It decorates the desk only. Every viewfinder drawing and the floor plan remain code so all angles are truthful. No people or body parts were generated.

#### Voice
Bank: smooth-narrator. `Curio.voice` owns the queue, Read, Sound and heard keys. No recorded audio was made, as instructed. Browser speech is the runtime fallback. The full fixed-line list is in `voice/lines.json`.

#### Checks and evidence
All evidence is under `_scratch/storyboard-studio/`.
- `numbers.py` and `numbers.json`: independent lens fields, sample frame heights, maximum time and contrast calculations.
- `functional.js` and `functional-results.json`: threshold, sample, neutral, jump cut, timing, collision and immediate-control assertions.
- `full/`: the one full STANDARDS size pass, all viewed. `targeted/` and `last/`: only touched states after build fixes.
- `student-check.py`, `student-results.json`, `student/`: real held taps and keyboard repairs, full animatic, print, reload and voice checks.
- `voice-final.json`: five held Add taps at two-second pace. The teaching line starts once, events can recur, stale queued events are dropped.
- `bar/` and `snowy-bar/`: opened existing bundled bar tools. Their source and neighbor handoff/review were read. They were not rebundled, because that would write outside the two authorized folders.
- `audit/`: one final mechanical audit, with its own Chrome profile and host port 8795. See codex-report.md for its result and lead dispositions.

#### Final audit and targeted build corrections
The audit finished in 1408 seconds with 67 leads. It found no console errors, infinite motion, resize exceptions or controls left disabled by resizing. All 69 audit PNGs were reviewed in eight contact sheets; problem states were also opened individually.

After that one audit, compact Board gained picture space, header toggle widths became stable, repeated current-mode taps stopped interrupting welcomes, the current panel chip scrolls into view, and timeline progress updates immediately. Stopped partial transitions now survive a redraw and playback ends on the complete incoming image. Bus door geometry and attached details were corrected. The audit was not rerun after these fixes.

`post-audit/` verifies the affected layouts, a keyboard-only reorder run, two spoken lineCrossed events from two new crossings, intact welcomes, full label hit areas and active-panel visibility. `final-targets/` verifies bus drawing and beat continuity, held fade pixels across a redraw, first-chip welcome and all 31 functional assertions again. Both batches report zero console errors.

The final audit-state file removes the mistaken requirement that the inactive background hint remain uncovered while a modal owns focus. It keeps the actual modal controls instead. Long phone boards also no longer claim that their entire grid and bottom notes must fit in the first viewport.

#### Engine changes wanted
None. No kit, documentation, script or other tool was edited.

#### Review cautions
The renderer uses depth-sorted shapes, not a full depth buffer. Very close or unusual placements can expose intersecting mannequin and prop surfaces. Inspect framing and educational accuracy, not photorealism.

On a phone the long Board scrolls as a page. Its primary scene, Add and reorder/sample controls are above the cards. Plan's less frequent lens, beat and duration controls follow the first visible action rows.

The strict short-choice audit rule remains a review lead for long authored boards and the twelve-panel strip. The tool preserves all notes and 44 px targets rather than squeezing an entire board into a small preview. Phone secondary parameters also require page scrolling. These are documented limits, not claims of an entirely clean mechanical audit.

Raw browser speech can hold the queue longer than natural recorded clips. The queue prioritizes the first line lesson, drops superseded queued events and keeps Read interruptible on a mode change. No claim of listening to recorded narration is made.

#### Cold review, 2026-11-04

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
