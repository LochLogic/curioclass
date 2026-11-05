# Codex report: storyboard-studio

## Built

Plan, Board and Animatic for The Last Slice and Late Bus. Actual full-frame projection, camera dragging and keys, four lenses and heights, fixed script poses, up to twelve panels, live continuity checks, practice copies, local saves and grayscale printing.
One self-contained offline HTML file with kit theme and Curio.voice. No commits, branch changes or polish round. Only the authorized tool and Scratch folders were used for project writes. Final report is written last to honor the user's stop-on-report instruction.

## Numbers check

PASS. Independent Scratch script reproduces all source calculations: fields 45.7473, 32.2688, 22.8952 and 13.5859 degrees; sample frame heights agree after rounding; final sample turn 9.9594 degrees. Maximum 96 seconds; samples 16 and 12 seconds.
Contrast: accent/panel 6.24:1, accent/section 5.91:1, brand ink/accent 6.60:1, yellow line/panel 12.00:1, dark ink/paper 9.55:1. No source-number disagreement.

## Feel check

Best: moving the sample's sixth camera across the plan removes two line crossings at once, then a new angle on panel eight removes the jump. The complete sixteen-second scene plays with all eight beats intact.
Flat moment 1: the outside opening camera saw the door wall. Cutaway walls, consistent ground layering, shadows, floor texture and the generated desk now reveal a coherent diner immediately.
Flat moment 2: long cut warnings starved the first line lesson during five rapid Add taps. The once-only line lesson now starts first; superseded event lines are dropped.
The small Board also gave too much height to Plan fields. Its compact layout now uses that space for pictures. This is a build correction, not a separate polish round.
Compared with Beat Lab and opened Snowy Mail Route. Scratch feel-comparison.png puts the tools beside each other. The cinematic desk, camera monitor and shaded mannequins hold their own; the drawing remains an intentional working storyboard.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

All manual shots in first, second, checks, full, targeted, student, voice, last, phone-modes, phone-animatic-final, post-audit and final-targets. The early blank/overlap frames were inspected and repaired. All full-size frames and the grayscale, print, pause, drag and keyboard frames were opened. All 69 audit frames reviewed in eight contact sheets, with affected states also opened individually. The final functional batch passes all 31 assertions.

## Art made

One generated editing-desk image, 1500x844. Full prompt: art/prompts.json. Built-in image tool, copied into art/raw, processed only with art.py --rekey editing-desk. No redraw needed. Final art 115.0 KiB; bundle 268.4 KiB (274,841 bytes), below 2 MB.

## Art still to paint

None. No generated people, faces or body parts. Viewfinder mannequins and sets are code, as the spec requires.

## Engine changes wanted

None. No shared files changed.

## Left open

- No recorded narration, as instructed; smooth-narrator metadata uses browser speech at runtime.
- Depth sorting is a simple storyboard renderer. Very close or oblique views can expose intersecting/coplanar surfaces.
- Compact layouts replace the chip strip with a live current-panel/adjacent-cut summary. Full Board and Prev/Next preserve access.
- Full audit was not rerun after the targeted build fixes listed above. The cold reviewer should use the final bundle and final audit-state file.

- Long authored boards and phone secondary parameters require scrolling, as detailed in the audit dispositions.
