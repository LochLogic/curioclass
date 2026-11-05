# Codex report: weekend-drawing-share

## Built

Built the offline, teacher-led K-2 drawing studio with seven question-tagged parts, ten art words, textured crayon/marker/paint/eraser drawing, twelve painted stickers, three code-drawn people stamps, resizing, Undo, a read-only sample, six local saves, and Tell it replay.

The kit supplies Motion, Sound, Read, tones, and Curio.voice. All images are embedded once and reused. Metadata remains tool.draft.json with stage built. No git commits, branch changes, polish round, or kit edits. The tool makes no external requests. All authored project files are in the two authorized folders.

## Numbers check

- PASS: white/brand 6.3088:1, brand/paper 5.9668:1, ink/paper 14.8800:1, muted/paper 6.0990:1, matching the spec's rounded ratios.
- PASS: 1200x900 is 4:3. Seven questions, ten art words, twelve painted stickers, four Pip poses, two backgrounds/textures: eighteen images.
- PASS: 300/600 = 0.5 seconds; 1200/600 = 2 seconds; 4000 and 9000 units cap at 4 seconds. Seven capped steps total at most 28 seconds of drawing, with indefinite teacher pauses.
- DIFFERENCE: 20,000 x 11 = 220,000 characters and six x 220,000 = 1,320,000 are arithmetically right, but eleven characters per [x,y,time] point is optimistic. Real input averaged about 14.6. A 19-character integer-point example uses 2,280,006 characters for six 20,000-point arrays before metadata. Six extremely fragmented drawings are not guaranteed to fit a device quota. Save failure is caught without changing the drawing or shelf.
- Evidence: Scratch/setup.py, numbers.txt, real-stroke.json, scenario storage results, and student-result.json.

## Feel check

Best moment: the child's important outline returns over the faded ball and earlier marks, the chosen big badge appears, and the final Next step restores the whole picture. The result belongs to this artist.

Flattest moment 1: starting a sound stroke over a ball dragged the older ball. Fixed selection so a stroke over an unselected sticker draws normally; tapping an older sticker selects it for movement. The next complete pointer-driven session produced all seven question parts.

Flattest moment 2: the first compact layout gave the paper too little room. Moved art words beside the sheet, kept all ten visible, opened drawing tools in a drawer on compact screens, and made the full-width palette three columns so the last colors stay visible. Also kept the paper box identical across modes and moved the sample label away from its sky art.

Played a complete seven-part session with real pointer input and waited for every part's badges and child-speaking pause. All seven parts completed without exceptions or external requests. I would continue making and explaining this drawing during the intended lesson; replay alone is a short storytelling activity, not a ten-minute game.

Compared with both existing reference bundles. The room, paper, bird, and wax stickers meet the visual finish of the reference while leaving space for children's own marks.

![Weekend Drawing Share beside Snowy Mail Route](../../_scratch/weekend-drawing-share/feel-comparison.png)

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

- Both reference frames in Scratch/bar-frames, plus feel-comparison.png.
- The art contact sheet and all eighteen cutouts/backgrounds; final-size placement was checked in the workspace and enlarged sticker resize frame.
- All first-frames and first-frames-v2 frames, twelve scenario-frames, twelve regression-frames, nine student-frames, and sixteen final-frames. Revised compact/phone frames were inspected after the hint/host fixes. QA contact sheets are in Scratch/qa-sheets.
- All 86 audit PNGs were inspected through eight contact sheets, with relevant dialogs and small layouts checked against full frames. Blank marked-step fixtures are disclosed above.
- All 14 postfix-frames, including live resize, marked 680, empty ending, failed-save Read, sample copy, both phone badges, and seven-card phone/laptop shelves. Final shelf frames were reopened after moving the privacy caption below the wrapped cards.

## Art made

Eighteen finished images, nineteen generations including one dog redraw. 1072.0 KiB of finished WebP art; final standalone HTML 1507.0 KiB, below 2 MB. Background, paper fibers, four sparrow poses, and twelve wax crayon stickers are all placed. Green and magenta keys were processed only with the free art.py --rekey form. Sticker images were increased to 500 pixels wide for large resized placement.

## Art still to paint

None. No generated people. Grown-up, Kid, and Baby are code-drawn crayon stick figures, as specified.

## Engine changes wanted

None. No kit or family engine files were changed.

## Left open

- Narration is browser speech. The curious-librarian/Aoede bank and every fixed line are listed, but no audio was recorded under the Build restriction.
- Six extremely large, fragmented drawings may exceed a browser quota. The data stays in memory on save failure, and no saved slot is discarded until the write succeeds.
- The compact workspace uses a Tools drawer and puts the saved shelf below the first viewport; it preserves all core actions and art words in view.
- The audit includes intentional overlays and compact auxiliary controls below the fold. It is not a zero-lead report. The corrected drag fixture and final narrow repairs await the independent cold review.
- The full audit is not rerun after targeted repairs. A separate cold review remains the next workflow step.
- Host, Chrome cleanup, and final packaging: all owned test Chrome instances and servers closed; no listener remained on 9980, 9981, or 8785; temporary host.html removed.

Build only. No commits and no polish round.
