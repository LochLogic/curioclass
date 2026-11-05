# Codex report: virtual-gallery

## Built

Four modes: Select, Hang, Walk and Checklist. Real-scale CSS 3D walls, textured plaster and oak, physical frames and bowl shelf, spotlights, plan editing, pointer and keyboard controls, local saving, own-image imports, labels, statement, and print sheet.

Draft stage is built. Final offline bundle: 956,507 bytes (934.1 KB). Source: 1,848 readable lines, maximum 160 characters. Repository changes stay inside tools/virtual-gallery/. No commit and no polish round.

## Numbers check

- Independent Scratch numbers.py: home 6, water 5, city 5, growing 4, night 2; door-side walls 340 cm each.
- Correction: eight widest framed works plus seven 30 cm gaps need 685 cm, not the spec's 745 cm. Three widest plus two gaps need 254 cm. spec.md is unchanged.
- Frame dimensions add 16 cm per side length. Gap spreads: 40,40,46 = 14.2857%; 40,40,47 = 16.5354%.
- Conversions: 137 cm = 53.94 in; 122 to 168 cm = 48.03 to 66.14 in; 109 to 130 cm = 42.91 to 51.18 in.
- Contrast ratios reproduced: brand/panel 11.524, brand/section 10.920, brand ink/brand 12.294, label ink/wall 12.494, label ink/white 14.339.
- Eight-stop Motion-off walk measured 24,138.7 ms. First-seen tests include vertical distance from the 160 cm eye line.

## Feel check

- Best moment: walking a personally assembled six-work show, seeing its doorway anchor, then reaching nine ready checks with the student's labels and statement intact.
- Flattest moment 1: the initial distant room made the work too small. Moved the camera closer, corrected the floor plane, and kept the room dominant. At 1366x768 the back and side wall bounding widths measured 738 and 391 px.
- Flattest moment 2: close-up artwork was blurred by Chrome's CSS 3D rasterization. Added projected high-resolution artwork and label replicas, adaptive viewing distance, and a readable label inset. Small views suppress the overlapping replica.
- Completed a real-keyboard six-work run through selection, hanging, lighting, label writing, statement, walking and printing. Result: nine of nine ready checks, zero exceptions.
- Compared the tool beside Beat Lab in Scratch compare-bar.png; also opened Snowy Mail Route. The gallery has rich artwork and material surfaces, with a restrained studio interface appropriate to this grade.

## Done when

1. PASS: exact theme counts; actual growing and night event narration played, and changing to city added no themeShort event. final-theme-result.json.
2. PASS: real jittered drags hang, return and move work on the plan; Enter hangs, arrows move 5 cm, Shift moves 25 cm. A 150-placement collision/bounds test passed. Final plan drag moved the work from 400 to 531.41 cm.
3. PASS: populated back wall, empty back wall and side-anchor layouts name the expected first work; an additional low-frame case checks the 160 cm eye line.
4. PASS: all nine checks have passing and failing fixtures. Explicit tests cover 14.3%/16.5% spacing, a 26-word note, a 101-word statement and a 26-word sentence. Thirty functional assertions passed.
5. PASS: walking follows tray order; labels and shared-tag jumps are visible. Eight-work order and final label were checked; jump narration repeated on revisits.
6. PASS: Stop, Step, Back, order-strip and direction handlers changed state before yielding. Eight stops took 24.14 s. A final calm-cut test held the old view until the one-second cut and arrived with the correct label.
7. PASS: reviewed Select, Hang and Walk at 1366x768 and 680x425. The portfolio, room, and visitor view are the main stage; the compact preview uses the plan.
8. PASS: a browser-created image joined the portfolio, was selectable, and stored no image bytes. Reload removed it with the specified message. Imported work has no false Jordan Reyes attribution.
9. PASS: selection, star, placement and statement survived reload. Confirmed Clear show removed virtual-gallery-show.
10. FAIL: the tray, main view and primary work controls fit, but secondary height/order/remove controls require workbench scrolling in compact sizes. The reserved footer no longer covers those controls.
11. PASS: held clicks at two-second intervals logged welcomeHang, lightHow and hangMore once each across five hangs. firstSeen and jump events repeat and stale events drop. Same-mode taps now preserve the welcome; the final test recorded no cut.
12. PASS: all 16 images load and were inspected. No people or fake lettering. The bowl was checked in both room and visitor views on its shelf.

## Wave lessons

BR1 lessons:

- Hint and voice: PASS. Hints update synchronously, Read uses the current hint, Curio.voice owns the queue, and held-click logs were inspected.
- Focus and layout: PASS for primary flows. Fixed Tab changing the selected tray work; the full keyboard run and scrolled lower-card pointer test preserve focus.
- Sizes: FAIL for simultaneous visibility of every secondary compact workbench control. Header targets are now at least 44 px; short editor Done buttons are visible.
- No giveaways: PASS. This is an open builder with intentionally public curating criteria, not a hidden-answer quiz.
- Honest numbers: PASS. Real dimensions, stated thresholds, live word counts, explicit Preview print sizes for own images, and the spec arithmetic correction are documented.
- Standards: PASS. Students select and interpret, refine presentation, and write and test an exhibition's meaning themselves. There is no family engine.
- Motion off: PASS. Audit found no infinite animation; timing remains unchanged and final cuts keep image and label synchronized.

Network-help-desk lessons:

- Short choices in view: FAIL for secondary compact workbench controls. The longer portfolio and diagnostic checklist intentionally scroll; neither is a short answer-card puzzle.
- Resize mid-animation: PASS. Full audit reported no exceptions or controls left disabled.
- Deferred first-tap welcome: PASS. No welcomeAfter; action-specific speech takes priority. Same-mode repeated taps no longer hush the welcome.
- Unknown as unknown: PASS. Unhung works say tray, unlit works stay dim, and empty shows cannot start walking.
- One look, one meaning: PASS. Chosen ticks, anchor stars, jump words and ready/needs-attention text distinguish states without color alone.
- Badge says what is true: PASS. Counts and readiness derive from current chosen/hung work and actual checks; imported-image persistence is stated.
- Hint changes back: PASS. Mode changes and editor cancellation restore the current instruction immediately.
- No answer by copying words: PASS. There is no diagnosis quiz; students construct, explain and test their own presentation.

## Audit leads

Ran the full audit once, on Chrome 9971 and host 8775. Completed in 1,646 s with 122 leads. Full report: S:/CurioClass-codex/_scratch/virtual-gallery/audit/audit.md. It is a pre-repair snapshot; the full audit was not repeated. Eleven targeted final cases, affected plan re-shots, bowl views and a real plan drag checked the final corrections with zero console errors.

Every lead is covered by these grouped dispositions, including repeated findings across sizes and states:

- Small Read/mode targets: FIXED with 44 px minimum widths; final preview and phone header measurements passed.
- Nine-pixel phone eyebrow/save text: FIXED to 10 px.
- Compact footer overlaps with sliders, order controls and notes: FIXED by reserving the footer outside the scrolling workbench.
- Compact secondary controls outside the viewport: LEFT OPEN as Done when 10; they remain available by scrolling.
- Plan title/door/status collisions: FIXED visual spacing and compact title. Desktop Plan is now a visible panel supplement, with corrected viewport and ink contrast.
- Pointer-hit coverage of noninteractive room HUD text: expected for pointer-events:none overlays; reviewed the actual frames. It does not mean the text is visually covered.
- Clipped/tiny physical wall lettering: scaled model decoration, with corresponding readable controls and visitor labels. The duplicate 3D world is now aria-hidden; the accessible tray and editors remain available.
- Unnamed textarea leads: FIXED with explicit aria-label and count descriptions in addition to their wrapping labels.
- Dialog covering background controls/hint: intentional native modal behavior. The dialog owns the editing task, labels, counts and Done/Close controls; covered background controls are inert.
- Short-preview Statement Done/Close clipped: FIXED. Final 680x425 editor height was 265 px and Done remained visible.
- Duplicate wall-label/inset overlap in short Walk views: FIXED by retaining the readable inset and suppressing the overlapping replica there.
- One-stop plural: FIXED; final frame says 1 stop.
- Checklist Why/Show me outside its initial scroll position: intentional diagnostic-list scrolling. Native disclosures work; Print/Clear remain outside the scrolling list. Offscreen raw-center clicks are not valid control hits.
- Lower portfolio card focus-loss leads: raw centers were clipped at the initial scroll position. A real held click after scrolling to Bowl retained card-bowl focus; the full keyboard run reached lower rows too.
- Current-mode quick taps cutting welcomes: FIXED by making the current mode button idempotent. Final double-tap test logged one welcome with no cut.
- Add to show skipping welcomeSelect: expected by STANDARDS. Its own how-to speaks; welcomeSelect is stale once work is added. Sound/Read explicitly interrupt speech by design.
- Runtime, Motion-off loops, resize recovery and five-click repetition: audit sections were clean. No shared engine changes were made.

## Frames looked at

Scratch root: S:/CurioClass-codex/_scratch/virtual-gallery/.

- bar-frames/: Beat Lab and Snowy Mail Route; compare-bar.png puts the gallery beside Beat Lab.
- initial-frames/, second-frames/, camera-frames/: initial scenes and camera/floor repairs.
- final-frames/: all four modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
- phone-frames/, targeted-frames/, repair-frames/, last-frames/: 375-wide iframe views, fixes and all final targeted cases.
- extra-frames/: Motion off, grayscale, 26-word note, 101-word statement, eight selections, center-line extremes and unlit work.
- interaction-frames/, behavior-frames/, voice-frames/, voice-repair-frames/, functional-final-frames/: input, persistence, walk and voice evidence.
- student-hang.png, student-walk.png, student-checklist.png and print-sheet.png: complete keyboard student run and print-media rendering.
- All 81 audit frames reviewed through audit-contact-1.png to audit-contact-9.png; corresponding main sizes were also inspected directly.
- plan-final-frames/, plan-drag-frames/, bowl-frames/: final plan, real plan movement, and shelf rendering.

## Art made

Three images generated during this build with imagegen: warm plaster, honey oak planks, and a monochrome charcoal tomato drawing replacing the supplied colored rendering. Thirteen other supplied works retained. Recompressed oversized supplied assets to the 50 KB-per-work budget. All 16 WebP files total 567,480 bytes (554.2 KB); final bundle is 934.1 KB. Full prompts and provenance are in art/prompts.json; generated PNGs are in art/raw/. Finished textures, portfolio contact sheet and replacement drawing were inspected. No image-generation failures.

## Art still to paint

None. No people required. Narration recordings were not made, as instructed; browser speech is the fallback.

## Engine changes wanted

None. Kit, shared scripts, documentation and other tools are unchanged.

## Left open

- Done when 10: compact secondary workbench controls need scrolling.
- Gap measurements appear in the status, workbench and drag hint rather than dimension rulers drawn between frames.
- The plan connects stops in tray order; the camera uses a directional aisle route between those stops. This resolves the direction/order ambiguity in favor of preserving tray order.
- Several supplied artworks are landscape despite the revised portrait art brief. Existing art is retained; the discrepancy is documented in handoff.md.
- Full audit was not rerun after the targeted repairs. Final browsers and servers are closed; host.html is removed. The branch is left for cold review.
