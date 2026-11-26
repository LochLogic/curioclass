# Weekend Drawing Share: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: weekend-drawing-share

#### Built

Built the offline, teacher-led K-2 drawing studio with seven question-tagged parts, ten art words, textured crayon/marker/paint/eraser drawing, twelve painted stickers, three code-drawn people stamps, resizing, Undo, a read-only sample, six local saves, and Tell it replay.

The kit supplies Motion, Sound, Read, tones, and Curio.voice. All images are embedded once and reused. Metadata remains tool.draft.json with stage built. No git commits, branch changes, polish round, or kit edits. The tool makes no external requests. All authored project files are in the two authorized folders.

#### Numbers check

- PASS: white/brand 6.3088:1, brand/paper 5.9668:1, ink/paper 14.8800:1, muted/paper 6.0990:1, matching the spec's rounded ratios.
- PASS: 1200x900 is 4:3. Seven questions, ten art words, twelve painted stickers, four Pip poses, two backgrounds/textures: eighteen images.
- PASS: 300/600 = 0.5 seconds; 1200/600 = 2 seconds; 4000 and 9000 units cap at 4 seconds. Seven capped steps total at most 28 seconds of drawing, with indefinite teacher pauses.
- DIFFERENCE: 20,000 x 11 = 220,000 characters and six x 220,000 = 1,320,000 are arithmetically right, but eleven characters per [x,y,time] point is optimistic. Real input averaged about 14.6. A 19-character integer-point example uses 2,280,006 characters for six 20,000-point arrays before metadata. Six extremely fragmented drawings are not guaranteed to fit a device quota. Save failure is caught without changing the drawing or shelf.
- Evidence: Scratch/setup.py, numbers.txt, real-stroke.json, scenario storage results, and student-result.json.

#### Feel check

Best moment: the child's important outline returns over the faded ball and earlier marks, the chosen big badge appears, and the final Next step restores the whole picture. The result belongs to this artist.

Flattest moment 1: starting a sound stroke over a ball dragged the older ball. Fixed selection so a stroke over an unselected sticker draws normally; tapping an older sticker selects it for movement. The next complete pointer-driven session produced all seven question parts.

Flattest moment 2: the first compact layout gave the paper too little room. Moved art words beside the sheet, kept all ten visible, opened drawing tools in a drawer on compact screens, and made the full-width palette three columns so the last colors stay visible. Also kept the paper box identical across modes and moved the sample label away from its sky art.

Played a complete seven-part session with real pointer input and waited for every part's badges and child-speaking pause. All seven parts completed without exceptions or external requests. I would continue making and explaining this drawing during the intended lesson; replay alone is a short storytelling activity, not a ten-minute game.

Compared with both existing reference bundles. The room, paper, bird, and wax stickers meet the visual finish of the reference while leaving space for children's own marks.

![Weekend Drawing Share beside Snowy Mail Route](../../_scratch/weekend-drawing-share/feel-comparison.png)

#### Done when

1. PASS: the 4:3 sheet is the largest individual stage object at 1366x768 and 680x425. Question text remains readable. Final compact paper is about 267x200 pixels; the smallest scene labels are 10 pixels or larger. Draw and Tell it use the same paper box.
2. PASS: seven Next question actions and the question drawer reach the ordered prompts. The complete student run recorded marks under indexes 0 through 6. The question-seven jump was checked with held clicks.
3. PASS: a timing-jittered, integer-pixel stroke drawn at 1920x1080 was saved, reloaded at 760 wide, and replayed with the same logical point array and placement.
4. PASS: a third art word replaces the oldest, leaving two. Held clicks at two-second intervals started all three selected chip event lines. Clearing a lit chip adds no line. Read keeps priority.
5. PASS: sample schedules were 3050, 500, 418, 500, 252, 420, and about 712 milliseconds. The eraser stress step hit the 4000 millisecond cap. The sample has all seven exact chip sets. The student session waited after every part and showed the relevant badge.
6. PASS: real rapid Next, Back, Play, and thumbnail inputs during replay changed steps immediately and hushed old narration. The final result restores full opacity and happy Pip. Start over and Draw more work.
7. PASS: six saves persisted into a fresh tab, a seventh asked, Cancel preserved the collection, and Replace the oldest retained six. A throwing storage setter left drawing and saves unchanged and showed Could not save on this device.
8. PASS: five held Next question taps at two-second intervals started five question events, with no repeated how-to or late welcome. How-to keys use V.heard; lit chip events start on each selection. Recordings were not made under this Build instruction, so browser speech is the current fallback.
9. PASS for the core workspace: all measured visible controls are at least 60x60, with icons or thumbnails and words. Next question and all ten chips are visible at every required size. Compact saved shelves require scrolling. The audit reported no small targets or clipped core controls. The sample plus all six personal saves fit the final phone view in 64x77 targets.
10. PASS: Motion off reports zero running infinite animations; whole strokes retain replay pacing. The complete local session reported zero external resource requests. Drawings stay on the device.

#### Wave lessons

- Hint and voice: PASS for current-action hints, Read priority, first-tap input, question/chip events, and once-only how-to selection. Targeted drawer-close and confirmation checks passed; obsolete lines were hushed, and canceled confirmation retained all 32 sample marks.
- Focus and layout: PASS for stable control nodes, no focus on load, reserved hints, and explicit preventScroll focus for paper, dialogs, Undo, and completion. The audit found no live-control focus loss; its disabled empty-sheet Tell it focus lead is intentional.
- Sizes: PASS for core controls, readable questions, no horizontal page overflow, 60 pixel targets, and full hint visibility. All STANDARDS sizes were captured in both modes; 375 used host port 8785.
- No giveaways: PASS, a personal art studio with no scored answers or hidden right choices.
- Honest numbers: PASS for recomputed contrast, logical coordinates, and capped timing. The storage estimate discrepancy is explicitly recorded above and in handoff.md.
- Standards: PASS. The child relates art to a lived experience, adds or revises details, chooses art words, and explains the result. No family engine was specified.
- Motion off: PASS, Pip's bob stops and stroke pacing stays unchanged.
- Short choices: PASS for all ten art words, seven question choices, all drawing tools in their compact drawer, and all sticker choices. Saved thumbnails wrap without a short scroll panel. Final six-save frames show all seven cards within 375x812 and 1366x768, with no sideways overflow.
- Resize mid-animation: PASS, the audit resize pass was clean; a separate live 1366 to 760 and back replay retained 1200x900 logical coordinates and completed without exceptions. Canvas coordinates remain logical and resize changes only its displayed box.
- Late welcome: PASS, welcomeAfter is false per the BUILD multi-mode lesson. The Tell it welcome is requested at mode entry, before its first question line. The spec conflict is recorded in handoff.md.
- Unknown as unknown: not applicable; there are no concealed facts or guessed statuses.
- One look, one meaning: PASS, selected chips carry checks as well as raspberry fill; step dots mean marks exist, not that a step is correct.
- Badge says what is true: PASS, badges come from this step's stored chip pair, and the sample stays read only until copied.
- Hint changes back: PASS for mode, question, drawer, dialog, save failure, and reset paths. Targeted drawer-close and confirmation checks passed; obsolete lines were hushed, and canceled confirmation retained all 32 sample marks.
- No copying words: not applicable; there is no diagnosis or answer-matching activity.

#### Audit leads

Completed once in 1894.2 seconds (31.6 minutes): 102 leads, all reviewed. The audit found no small targets, console errors, control jumps, endless motion, resize exceptions, or stuck controls. Its repeated-tap sample was clean. Every geometry/state row is addressed below; all 33 welcome rows follow the standing skip-on-own-line rule. Full per-control mapping: [audit dispositions](../../_scratch/weekend-drawing-share/audit-dispositions.md).

- control below the fold: #new "✦New drawing" top 444 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #save "▣Save" top 444 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #saved-0 "Pip's day at the pond" top 436 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 187x46 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 187x15 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- control below the fold: #new "✦New drawing" top 519 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #save "▣Save" top 519 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #saved-0 "Pip's day at the pond" top 511 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 257x46 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 257x15 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- control below the fold: #new "✦New drawing" top 644 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #save "▣Save" top 644 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #saved-0 "Pip's day at the pond" top 636 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 374x46 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 374x15 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 316x61 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 316x21 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 361x66 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 361x22 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- control below the fold: #new "✦New drawing" top 919 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #save "▣Save" top 919 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- control below the fold: #saved-0 "Pip's day at the pond" top 911 Disposition: Accepted compact shelf placement: auxiliary New, Save, and sample sit below the core workspace. Next and all chips stay visible.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 379x46 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 379x15 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / strong "A little momentworth remembering." 236x48 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / span "Pick a color. Make a mark." 236x16 Disposition: Expected first-use instruction over the empty canvas; pointer events pass through and it disappears on the first mark.
- focus fell to the page after clicking #m-tell (click 1) [every size] Disposition: Expected disabled empty-sheet mode button. Real replay is covered by sample-story and story-finished.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / #sample-note "Pip's sample · Draw more makes a copy" 219x25 [every size] Disposition: Expected noninteractive read-only sample label over an unused bottom margin of the sample paper.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / #sample-note "Pip's sample · Draw more makes a copy" 219x25 [every size] Disposition: Expected noninteractive read-only sample label over an unused bottom margin of the sample paper.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under button.sticker-choice "slide" [680x425] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under button.sticker-choice "slide" [680x425] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under button.sticker-choice "slide" [680x425, 800x500, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under button.sticker-choice "cloud" [800x500, 1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under button.sticker-choice "cloud" [800x500, 1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under #sticker-grid "suncloudrain cloudtreeflowerhouseslideba" [1000x625] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under button.sticker-choice "rain cloud" [1280x720, 1366x768] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under button.sticker-choice "rain cloud" [1280x720, 1366x768] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under img [1280x720, 1366x768, 375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #sticker-grid "suncloudrain cloudtreeflowerhouseslideba" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under #sticker-grid "suncloudrain cloudtreeflowerhouseslideba" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under span.symbol "👥" [680x425, 800x500] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under span.symbol "👥" [680x425, 800x500] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under #question-grid "📍where👥who👟doing⛅sky👂sound♥feel★star" [680x425] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under button "👥who" [800x500, 1280x720, 1366x768] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under div.dialog-head "Which part of your day?✓ Close" [1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under div.dialog-head "Which part of your day?✓ Close" [1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under span.symbol "👥" [1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #questions-dialog "Which part of your day?✓ Close 📍where👥" [1280x720, 1366x768] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under #questions-dialog "Which part of your day?✓ Close 📍where👥" [1280x720, 1366x768] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #questions-title "Which part of your day?" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under #questions-title "Which part of your day?" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under #questions-title "Which part of your day?" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #widths "─Thin━Thick" [680x425, 800x500] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under #widths "─Thin━Thick" [680x425, 800x500] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under span.tray-label "Your colors" [680x425] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under #widths "─Thin━Thick" [800x500, 1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under button "🖌Paint" [1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under button "🖌Paint" [1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under span.tray-label "Make a mark" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: strong "A little momentworth remembering." under span.tray-label "Make a mark" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: span "Pick a color. Make a mark." under span.symbol "▰" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- overlap: #paper "Drawing paper. Draw with a pointer. Sele" / #resize "Resize selected sticker. Arrow keys chan" 60x60 [every size] Disposition: Expected 60-pixel resize handle overlay on the selected sticker, with keyboard resizing supported.
- keep region: #paper: 100% inside the window, 1 of 9 sample points covered or cut by a scroll box [680x425, 375x812] Disposition: Expected Size handle over its selected object on the paper; the handle is 60 pixels and deliberately covers a canvas sample point.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #confirm-title "Start a new drawing?" [680x425, 800x500, 1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #resize "Resize selected sticker. Arrow keys chan" under #confirm-title "Start a new drawing?" [680x425, 800x500, 1000x625, 760x900] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under div.confirm-actions "✓ Yes, start new↶ Keep drawing" [1280x720, 1366x768, 1920x1080] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #resize "Resize selected sticker. Arrow keys chan" under div.confirm-actions "✓ Yes, start new↶ Keep drawing" [1280x720, 1366x768, 1920x1080] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #paper "Drawing paper. Draw with a pointer. Sele" under #confirm-dialog "Start a new drawing?Start a new drawing?" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.
- text hidden under another box or a scroll edge: #resize "Resize selected sticker. Arrow keys chan" under #confirm-dialog "Start a new drawing?Start a new drawing?" [375x812] Disposition: Expected modal occlusion: the open native dialog covers the inactive paper, start prompt, or Size handle. Dialog choices are visible.

Welcome rows: #m-draw 🖍 Draw, 🖍Crayon, ▰Marker, 🖌Paint, ▱Eraser, ─Thin, ━Thick, red, orange, yellow, green, blue, purple, pink, brown, black, white, #paper Drawing paper. Draw with a poi, ☀bright colors, ☾dark colors, ▣big, ▫small, ↓in front, ↑far back, ∿curvy lines, ϟzigzag lines, ⌕details, ◎middle, #stickers 🌻Stickers, #next-question ➜Next question, #questions ❔Questions, #new ✦New drawing, #saved-0 Pip's day at the pond. Disposition for every listed control: Expected first-tap welcome skip: this control supplies its own current-action line. STANDARDS says to skip the welcome unmarked; welcomeAfter is false for this multi-mode tool.

Post-audit repairs: close dialogs hush old instructions; confirmations stop replay; sticker placement has a valid once-only action line; an empty ending does not name disabled Tell it; Read matches a failed-save card; saved thumbnails wrap rather than scroll sideways. Targeted checks passed with zero console errors. The full audit was not rerun.

The first marked-step audit fixture omitted the outer return expected by audit_tool.py, so those particular frames stayed blank. The fixture is corrected in audit-states.json for cold review. The separate real-drag checks and full student run did exercise freehand drawing. The automatic Tell it mode walk starts with no marks and therefore encounters its deliberately disabled button; explicit sample-story and story-finished states cover replay with work.

#### Frames looked at

- Both reference frames in Scratch/bar-frames, plus feel-comparison.png.
- The art contact sheet and all eighteen cutouts/backgrounds; final-size placement was checked in the workspace and enlarged sticker resize frame.
- All first-frames and first-frames-v2 frames, twelve scenario-frames, twelve regression-frames, nine student-frames, and sixteen final-frames. Revised compact/phone frames were inspected after the hint/host fixes. QA contact sheets are in Scratch/qa-sheets.
- All 86 audit PNGs were inspected through eight contact sheets, with relevant dialogs and small layouts checked against full frames. Blank marked-step fixtures are disclosed above.
- All 14 postfix-frames, including live resize, marked 680, empty ending, failed-save Read, sample copy, both phone badges, and seven-card phone/laptop shelves. Final shelf frames were reopened after moving the privacy caption below the wrapped cards.

#### Art made

Eighteen finished images, nineteen generations including one dog redraw. 1072.0 KiB of finished WebP art; final standalone HTML 1507.0 KiB, below 2 MB. Background, paper fibers, four sparrow poses, and twelve wax crayon stickers are all placed. Green and magenta keys were processed only with the free art.py --rekey form. Sticker images were increased to 500 pixels wide for large resized placement.

#### Art still to paint

None. No generated people. Grown-up, Kid, and Baby are code-drawn crayon stick figures, as specified.

#### Engine changes wanted

None. No kit or family engine files were changed.

#### Left open

- Narration is browser speech. The curious-librarian/Aoede bank and every fixed line are listed, but no audio was recorded under the Build restriction.
- Six extremely large, fragmented drawings may exceed a browser quota. The data stays in memory on save failure, and no saved slot is discarded until the write succeeds.
- The compact workspace uses a Tools drawer and puts the saved shelf below the first viewport; it preserves all core actions and art words in view.
- The audit includes intentional overlays and compact auxiliary controls below the fold. It is not a zero-lead report. The corrected drag fixture and final narrow repairs await the independent cold review.
- The full audit is not rerun after targeted repairs. A separate cold review remains the next workflow step.
- Host, Chrome cleanup, and final packaging: all owned test Chrome instances and servers closed; no listener remained on 9980, 9981, or 8785; temporary host.html removed.

Build only. No commits and no polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: weekend-drawing-share

#### Played
Cold play before builder notes: as a K-2 artist, drew a place, chose an art word, added a person, and saved; then retold Pip's seven-part sample and tried compact drawers. The warm room and paper invite drawing; the final whole picture is worth sharing. Also checked the teacher's projected workflow. One review pass, with focused rechecks only.

#### Findings fixed
- **Should fix, general, src.html keyboard Size:** growing a sticker near an edge clipped it outside the sheet. Clamp its center after keyboard resizing, matching pointer behavior. Before/after frames and a keyboard-only placement/move/resize run confirm the repair.
- **Should fix, general, src.html Save:** a successful retry after blocked storage left the failure message on the question card. Refresh the card on successful Save; the original question returns and the saved hint agrees.
- **Should fix, general, src.html picker speech:** queued colors, brushes, and widths could name obsolete choices. Interrupt ordinary picker speech and validate the selected value. Read remains protected; red/orange were dropped and only current yellow followed Read.
- **Should fix, general, src.html and voice/lines.json:** Read used short chip names and waiting text absent from allLines/lines.json. Register the exact phrases and read the registered confirmation instruction. The two line sets now match exactly.
- **Polish, general, replay payoff:** badges and the invitation to speak waited behind long narration while the picture sat still. Reveal reasons one by one as drawing finishes and show the speaking invitation immediately; retain question-then-chip speech and revision guards. Added audit states for this and keyboard edge resizing.
- **Polish, general, art:** the dog looked photographic beside wax stickers. Repainted it with rich crayon grain using built-in imagegen, saved the prompt in art/prompts.json and raw PNG in art/raw/dog.png, then ran art.py --rekey dog with despill. Kept all other art and the studio's finish. Updated notes and handoff.

#### Findings left
- **Polish, general:** New drawing, Save and the saved shelf need page scrolling in short previews and the 760-wide portrait layout. Core drawing/replay actions, hints, and all ten art words remain visible. This preserves the 4:3 paper and 60-pixel controls.
- No known blocker or should-fix remains from this pass.

#### Flattest moment left
Opening Tools, choosing a color and closing it adds a pause in the smallest preview. The full classroom view keeps the tray open. Squeezing the controls would weaken the drawing space.

#### Graphics
Checked all 18 processed assets on a fresh contact sheet and in their final contexts, including the dog at drawer, normal, and maximum sizes. Four Pip poses remain consistent. Verified Pip's complete sprite on contrasting magenta. The quiet unoccupied backdrop follows the explicit spec; people stamps are editable code-drawn figures, with no generated people assets to mark or stereotype. One dog redrawn; no assets removed. Bundle 1505 KB. Beat Lab reference frame inspected without writing in its folder.

#### Audit
The single final audit completed in about 33 minutes, within its 2400-second limit, on Chrome 9941 and host 8745. All 92 frames were opened. Its 109 leads were reviewed: 76 size/state leads for intentional overlays, modal occlusion, pointer-transparent badges, the Size handle, disabled empty Tell it, and compact auxiliary shelf placement; 33 welcome leads follow the standing skip-on-own-action-line rule. Full dispositions: _scratch/weekend-drawing-share/review-audit-dispositions.md. No further source repair was warranted by the audit.

All 68 held-click rows retained control identity and focus, with no errors or control jumps. All ten five-click cases and ten quick-tap cases were clean. Final resize stress found no exceptions or controls left disabled. Motion off had no endless animations. The automatic mode walk starts empty, so actual Tell it behavior is covered by the separate sample/replay states and cold play. No second audit or polish round. Owned Chrome/server listeners are closed; host.html is absent.

Focused checks passed with zero console errors: identical 1920-to-760 stroke coordinates after reload, six saves and explicit replacement/Cancel, polite storage failure and successful retry, 20,000-point cap, 4000ms maximum replay, exact seven sample chip pairs, rapid replay navigation, keyboard-only drawing via stamps, grayscale, Motion off, and Read priority. All focused frames were opened. The corrected reload fixture scrolls the saved card into view before clicking it.

| Voice line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| Five successive questions | event | 5 | 5 |
| Big, selected five times | event | 5 | 5 |
| Next question how-to | how | 1 | 1 |

Recomputed white/brand 6.3088:1, brand/paper 5.9668:1, ink/paper 14.8800:1, muted/paper 6.0990:1. Replay examples match 0.5, 2, 4, 4 seconds. The spec's 11-character point storage estimate is optimistic: the tested integer triple uses about 19 characters. Save failure remains non-destructive. Both standards are practiced by making, revising, explaining and retelling the child's own experience; there is no scored wrong answer or hidden answer to give away. Notes open with the three required sections and accept the child's own reasons. Wave checks cover current hints, stable focus, sizes, honest counts, visible choices, motion, resize, and state-matched speech.

#### Left open
- Recorded curious-librarian narration remains absent; browser speech is the fallback. Recording is outside this task's rules.
- Keep the builder's documented welcomeAfter:false choice: the multi-mode wave lesson overrides the spec's true flag. No late welcome was introduced.
- No classroom trial, new features, engine changes, or commits. Authored project changes stayed in the two authorized folders. The report draft stayed in Scratch until completion to obey the explicit stop-on-report instruction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Weekend Drawing Share handoff

#### Build scope

Build only, in S:/CurioClass-codex. No commits or polish round. Only tools/weekend-drawing-share and its Scratch folder were written. The report is written last because the user's explicit stop-on-report instruction takes precedence over the brief's early-report advice.

#### Structure

src.html starts from the kit starter. Its CSS lays out the illustrated room, tools, 4:3 paper, art words, action bar, and saved shelf. The permanent controls keep their DOM identities. The ART table holds every art token once; images are reused in CSS, canvas, stickers, and thumbnails without duplicating embedded image payloads.

The drawing record holds globally ordered marks, each tagged with its question index. Strokes have integer logical coordinates and relative timestamps, thinned to at least three logical units. Point count is capped at 20,000. Undo removes the last mark across questions. Moving or resizing a sticker changes its original record and retains its question. Art words are separate FIFO pairs per step.

The renderer composites erasing on transparent layers above the paper texture. In Tell it, earlier marks are composited first, then faded together to 40 percent. The current step is drawn over them, preserving its own mark order and relative stroke speed. scheduleFor caps the whole step at four seconds and a minimum travel pace of 600 logical units per second. Calm shows whole strokes on the same schedule. Replay navigation cancels the frame, narration, and revision-scoped continuations synchronously.

Tap a previously placed sticker to select it, then drag it. A stroke started over an unselected sticker draws on it. Newly placed stickers start selected. The 60 pixel Size handle supports pointer resizing and keyboard arrows. Canvas arrows move a selected sticker; Delete removes it. This resolves the conflict between drawing on stamps and dragging them without adding a selection mode.

Save writes a proposed collection before changing memory. Failed writes retain the drawing, dirty status, save list, and ID. Six personal drawings are kept in curio-wds-saves; the built-in sample is separate. Existing saved drawings update their own slot. New drawings need explicit replacement at capacity. Opening another drawing also protects unsaved work. Saved data is validated before loading.

#### Narration

Curio.voice owns the queue, Read, sound state, and once-only how-to tracking. Fixed questions and chip lines are events. Revision checks drop obsolete question, replay, and chip lines. Chip selection uses now:true to replace stale ordinary speech while preserving Read priority. Clearing a chip stops its ordinary speech without adding a line. Dialogs update the hint immediately. Read uses the current question or replay question plus chip words; dialog Read uses its current instruction.

voice/lines.json specifies bank curious-librarian, voice Aoede, and the complete allLines list. No narration was recorded, as required by this Build. Browser speech is the current audible fallback, so the requested voice personality is metadata until recordings are made.

#### Spec decisions and ambiguities

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

#### Evidence and review

Scratch contains original image paths, number calculations, raw-input scenarios, storage tests, voice logs, all-size frames, student-session frames, and the final mechanical audit output. Chrome ports 9980 and 9981 and host port 8785 are used. Test Chrome instances are muted and closed by the drivers. The host wrapper deletes its temporary host.html in finally.

The reviewer should check the feel of drawing over an unselected sticker versus selecting it and classroom voice pacing with real browser speech. Saved thumbnails wrap, with compact 60-pixel-plus cards, rather than hiding a short collection in a horizontal scroll panel. Cold review is the next workflow step.

The first audit's marked-step drag fixture omitted the outer return expected by audit_tool.py. Its marked-step frames therefore stayed blank. The fixture was corrected for the next review; real freehand input was separately checked with drive.py and the complete student run. The full audit is not rerun for this fixture correction.

#### Engine changes wanted

None. No kit files were changed.

#### Cold review changes

The cold reviewer played the blank studio and complete sample before reading this handoff. Keyboard Size now clamps the sticker center to its new bounds, just like pointer resizing. Successful Save refreshes the question card so a previous quota failure cannot remain visible. Brush, width, and color speech interrupts obsolete picker speech and checks the selected value before starting.

Replay now reveals art-word badges one by one as soon as drawing finishes and immediately shows the child-speaking prompt. It keeps question-then-art-word narration in order without making visual feedback wait for speech. The revision guard cancels stale badge continuations. The dog was repainted through built-in imagegen with prominent wax texture; its raw PNG, prompt, and processed WebP replace the photographic-looking dog. No new feature, topic, mode, engine change, recording, or git commit.

Read's short chip names and waiting phrases are now registered in the voice table and voice/lines.json. Confirmation Read uses the registered instruction rather than an unregistered title-plus-message concatenation. The exact allLines and manifest sets match.

The cold review's single final audit completed on Chrome 9941 and host 8745 with a 2400-second limit. All 92 frames were inspected. Its 109 leads were intentional overlays, compact auxiliary shelf placement, and the expected skipped first-tap welcomes. All 68 held-click rows retained focus and control identity with no errors or jumps; ten repeat and ten quick-tap cases were clean; final resize stress found no exceptions or stuck controls. Dispositions are in Scratch/review-audit-dispositions.md. The final bundle is 1505 KB. Focused checks also covered the repaired storage retry, keyboard edge resize, exact logical points after reload, Read priority, five art-word events and one how-to, the point cap, capped replay, grayscale and Motion off. Recorded narration and a classroom trial remain open.

#### Final Build checks

The one full audit completed in 31.6 minutes with 102 leads. All are dispositioned in the report and Scratch/audit-dispositions.md. Geometry leads are intentional overlays, modal occlusion, or compact auxiliary shelf placement. No small targets, console errors, resize exceptions, endless motion, control jumps, or stuck controls were reported.

After that audit, narrow fixes were checked for closing-dialog narration, paused confirmations, valid sticker-placement help, empty-sheet completion, save-failure Read, and wrapped saved thumbnails. Fourteen targeted frames were inspected. The final phone holds the sample plus six saves in 64x77 targets; the privacy caption follows the wrapped shelf and may need a slight scroll at capacity. All target checks passed with zero console errors. The full audit was not rerun. No host.html or owned Chrome/server listener remains.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
