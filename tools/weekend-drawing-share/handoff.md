# Weekend Drawing Share handoff

## Build scope

Build only, in S:/CurioClass-codex. No commits or polish round. Only tools/weekend-drawing-share and its Scratch folder were written. The report is written last because the user's explicit stop-on-report instruction takes precedence over the brief's early-report advice.

## Structure

src.html starts from the kit starter. Its CSS lays out the illustrated room, tools, 4:3 paper, art words, action bar, and saved shelf. The permanent controls keep their DOM identities. The ART table holds every art token once; images are reused in CSS, canvas, stickers, and thumbnails without duplicating embedded image payloads.

The drawing record holds globally ordered marks, each tagged with its question index. Strokes have integer logical coordinates and relative timestamps, thinned to at least three logical units. Point count is capped at 20,000. Undo removes the last mark across questions. Moving or resizing a sticker changes its original record and retains its question. Art words are separate FIFO pairs per step.

The renderer composites erasing on transparent layers above the paper texture. In Tell it, earlier marks are composited first, then faded together to 40 percent. The current step is drawn over them, preserving its own mark order and relative stroke speed. scheduleFor caps the whole step at four seconds and a minimum travel pace of 600 logical units per second. Calm shows whole strokes on the same schedule. Replay navigation cancels the frame, narration, and revision-scoped continuations synchronously.

Tap a previously placed sticker to select it, then drag it. A stroke started over an unselected sticker draws on it. Newly placed stickers start selected. The 60 pixel Size handle supports pointer resizing and keyboard arrows. Canvas arrows move a selected sticker; Delete removes it. This resolves the conflict between drawing on stamps and dragging them without adding a selection mode.

Save writes a proposed collection before changing memory. Failed writes retain the drawing, dirty status, save list, and ID. Six personal drawings are kept in curio-wds-saves; the built-in sample is separate. Existing saved drawings update their own slot. New drawings need explicit replacement at capacity. Opening another drawing also protects unsaved work. Saved data is validated before loading.

## Narration

Curio.voice owns the queue, Read, sound state, and once-only how-to tracking. Fixed questions and chip lines are events. Revision checks drop obsolete question, replay, and chip lines. Chip selection uses now:true to replace stale ordinary speech while preserving Read priority. Clearing a chip stops its ordinary speech without adding a line. Dialogs update the hint immediately. Read uses the current question or replay question plus chip words; dialog Read uses its current instruction.

voice/lines.json specifies bank curious-librarian, voice Aoede, and the complete allLines list. No narration was recorded, as required by this Build. Browser speech is the current audible fallback, so the requested voice personality is metadata until recordings are made.

## Spec decisions and ambiguities

- The spec has no explicit open-question list.
- The Art mapping says Pip looks down in Tell it; the earlier screen description says ask pose. Used the explicit Art state mapping: ask at questions, listen while drawing, look during replay, happy at completion.
- The spec asks for welcomeAfter:true, while the later BUILD wave lesson says it is only for one-mode tools. Used false, retaining current-action speech and avoiding a late welcome. The kit still supplies the first-tap welcome and sound-on welcome when relevant.
- The fixed two-column tool tray cannot fit all sixteen 60 pixel controls in the shortest preview alongside ten art words and a meaningful sheet. Compact layouts put the tray in Tools. At full laptop widths, colors use three columns so all ten are visible at 1280x720. Art words and next actions stay in view without scrolling; the saved shelf is below the core workspace in short previews.
- The sheet preserves its 4:3 ratio and exactly the same box between Draw and Tell it. Its width is constrained by the available height rather than always occupying 70 percent of the entire stage. The 680x425 sheet is about 273x204 pixels before the final four-pixel hint adjustment.
- The empty-sheet rule takes precedence over the completion wording: after question seven with no marks, the card keeps its question and the hint says Draw something first. It does not direct the child to the disabled Tell it control. Read uses the question card's actual text, including a save-failure message.
- White/brand/paper/ink/muted contrast and the replay examples recompute exactly as specified. The eleven-character point estimate is low for actual [x,y,time] records: the real pointer test averaged about 14.6 characters per point, and a seven-digit timestamp example uses 19. Stroke metadata and stickers add more. The six-slot limit is enforced, but six maximally fragmented drawings are not guaranteed to fit a browser quota. Failure remains polite and non-destructive.
- The first dog painting contained a paper card and extra scene. Redrew it once as a standalone dog cutout. All eighteen finished images are used. No generated people or body parts; people stamps are code-drawn stick figures.
- Existing bundled snowy-mail-route and beat-lab files were opened as the quality bar. Rebundling those folders would violate this task's explicit write boundary, so their existing bundles were used without writes.
- line-safari has no handoff.md or refine.md; act-it-out has a handoff but no refine.md. Read the available neighbor source and handoff, and checked neighboring voice identities.

## Evidence and review

Scratch contains original image paths, number calculations, raw-input scenarios, storage tests, voice logs, all-size frames, student-session frames, and the final mechanical audit output. Chrome ports 9980 and 9981 and host port 8785 are used. Test Chrome instances are muted and closed by the drivers. The host wrapper deletes its temporary host.html in finally.

The reviewer should check the feel of drawing over an unselected sticker versus selecting it and classroom voice pacing with real browser speech. Saved thumbnails wrap, with compact 60-pixel-plus cards, rather than hiding a short collection in a horizontal scroll panel. Cold review is the next workflow step.

The first audit's marked-step drag fixture omitted the outer return expected by audit_tool.py. Its marked-step frames therefore stayed blank. The fixture was corrected for the next review; real freehand input was separately checked with drive.py and the complete student run. The full audit is not rerun for this fixture correction.

## Engine changes wanted

None. No kit files were changed.

## Cold review changes

The cold reviewer played the blank studio and complete sample before reading this handoff. Keyboard Size now clamps the sticker center to its new bounds, just like pointer resizing. Successful Save refreshes the question card so a previous quota failure cannot remain visible. Brush, width, and color speech interrupts obsolete picker speech and checks the selected value before starting.

Replay now reveals art-word badges one by one as soon as drawing finishes and immediately shows the child-speaking prompt. It keeps question-then-art-word narration in order without making visual feedback wait for speech. The revision guard cancels stale badge continuations. The dog was repainted through built-in imagegen with prominent wax texture; its raw PNG, prompt, and processed WebP replace the photographic-looking dog. No new feature, topic, mode, engine change, recording, or git commit.

Read's short chip names and waiting phrases are now registered in the voice table and voice/lines.json. Confirmation Read uses the registered instruction rather than an unregistered title-plus-message concatenation. The exact allLines and manifest sets match.

The cold review's single final audit completed on Chrome 9941 and host 8745 with a 2400-second limit. All 92 frames were inspected. Its 109 leads were intentional overlays, compact auxiliary shelf placement, and the expected skipped first-tap welcomes. All 68 held-click rows retained focus and control identity with no errors or jumps; ten repeat and ten quick-tap cases were clean; final resize stress found no exceptions or stuck controls. Dispositions are in Scratch/review-audit-dispositions.md. The final bundle is 1505 KB. Focused checks also covered the repaired storage retry, keyboard edge resize, exact logical points after reload, Read priority, five art-word events and one how-to, the point cap, capped replay, grayscale and Motion off. Recorded narration and a classroom trial remain open.

## Final Build checks

The one full audit completed in 31.6 minutes with 102 leads. All are dispositioned in the report and Scratch/audit-dispositions.md. Geometry leads are intentional overlays, modal occlusion, or compact auxiliary shelf placement. No small targets, console errors, resize exceptions, endless motion, control jumps, or stuck controls were reported.

After that audit, narrow fixes were checked for closing-dialog narration, paused confirmations, valid sticker-placement help, empty-sheet completion, save-failure Read, and wrapped saved thumbnails. Fourteen targeted frames were inspected. The final phone holds the sample plus six saves in 64x77 targets; the privacy caption follows the wrapped shelf and may need a slight scroll at capacity. All target checks passed with zero console errors. The full audit was not rerun. No host.html or owned Chrome/server listener remains.
