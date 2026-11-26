# Virtual Gallery: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: virtual-gallery

#### Built

Four modes: Select, Hang, Walk and Checklist. Real-scale CSS 3D walls, textured plaster and oak, physical frames and bowl shelf, spotlights, plan editing, pointer and keyboard controls, local saving, own-image imports, labels, statement, and print sheet.

Draft stage is built. Final offline bundle: 956,507 bytes (934.1 KB). Source: 1,848 readable lines, maximum 160 characters. Repository changes stay inside tools/virtual-gallery/. No commit and no polish round.

#### Numbers check

- Independent Scratch numbers.py: home 6, water 5, city 5, growing 4, night 2; door-side walls 340 cm each.
- Correction: eight widest framed works plus seven 30 cm gaps need 685 cm, not the spec's 745 cm. Three widest plus two gaps need 254 cm. spec.md is unchanged.
- Frame dimensions add 16 cm per side length. Gap spreads: 40,40,46 = 14.2857%; 40,40,47 = 16.5354%.
- Conversions: 137 cm = 53.94 in; 122 to 168 cm = 48.03 to 66.14 in; 109 to 130 cm = 42.91 to 51.18 in.
- Contrast ratios reproduced: brand/panel 11.524, brand/section 10.920, brand ink/brand 12.294, label ink/wall 12.494, label ink/white 14.339.
- Eight-stop Motion-off walk measured 24,138.7 ms. First-seen tests include vertical distance from the 160 cm eye line.

#### Feel check

- Best moment: walking a personally assembled six-work show, seeing its doorway anchor, then reaching nine ready checks with the student's labels and statement intact.
- Flattest moment 1: the initial distant room made the work too small. Moved the camera closer, corrected the floor plane, and kept the room dominant. At 1366x768 the back and side wall bounding widths measured 738 and 391 px.
- Flattest moment 2: close-up artwork was blurred by Chrome's CSS 3D rasterization. Added projected high-resolution artwork and label replicas, adaptive viewing distance, and a readable label inset. Small views suppress the overlapping replica.
- Completed a real-keyboard six-work run through selection, hanging, lighting, label writing, statement, walking and printing. Result: nine of nine ready checks, zero exceptions.
- Compared the tool beside Beat Lab in Scratch compare-bar.png; also opened Snowy Mail Route. The gallery has rich artwork and material surfaces, with a restrained studio interface appropriate to this grade.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

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

#### Art made

Three images generated during this build with imagegen: warm plaster, honey oak planks, and a monochrome charcoal tomato drawing replacing the supplied colored rendering. Thirteen other supplied works retained. Recompressed oversized supplied assets to the 50 KB-per-work budget. All 16 WebP files total 567,480 bytes (554.2 KB); final bundle is 934.1 KB. Full prompts and provenance are in art/prompts.json; generated PNGs are in art/raw/. Finished textures, portfolio contact sheet and replacement drawing were inspected. No image-generation failures.

#### Art still to paint

None. No people required. Narration recordings were not made, as instructed; browser speech is the fallback.

#### Engine changes wanted

None. Kit, shared scripts, documentation and other tools are unchanged.

#### Left open

- Done when 10: compact secondary workbench controls need scrolling.
- Gap measurements appear in the status, workbench and drag hint rather than dimension rulers drawn between frames.
- The plan connects stops in tray order; the camera uses a directional aisle route between those stops. This resolves the direction/order ambiguity in favor of preserving tray order.
- Several supplied artworks are landscape despite the revised portrait art brief. Existing art is retained; the discrepancy is documented in handoff.md.
- Full audit was not rerun after the targeted repairs. Final browsers and servers are closed; host.html is removed. The branch is left for cold review.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: virtual-gallery

#### Played

Cold grade 9-12 run before builder report/source: compared portfolio, selected home works, starred an anchor, dragged a frame, hung and lit others, auto spaced, entered Walk and Checklist.
An initial memory-registry search incidentally exposed an old build summary. Builder files stayed unopened until after play; every result reported here was independently exercised.
Strong: the textured room, mature gallery typography, varied portfolio media and precise tools. Cold evidence in cold/ and play-*.json.

#### Findings fixed

- Blocker, general, Checklist: punctuation-only titles and statements passed. Written text is now required; numeric and sentence limits still follow the spec. Punctuation UI paste fails after repair.
- Should fix, general, Hang/Walk: landscape paintings were stretched. Both room and sharp visitor artwork preserve aspect ratio within the physical frame.
- Should fix, general, compact Hang: secondary controls were hidden in scrolling workbenches. Every control now fits with 44 px targets at all eight required sizes, including Plan open.
- Should fix, general, Hang: Auto space left stale workbench gaps and celebrated sub-30 cm gaps. All copies update together; narrow gaps give an explicit correction without a success chime.
- Should fix, general, Walk: stopping between works retained the previous work's label. It now holds the actual camera, hides that label and names the between-work state. Speech and jump hints expire when their moment ends.
- Should fix, general, text extremes: long titles crossed order cards and labels. Titles wrap/clamp with full accessible names; visitor text scrolls within its own paper without covering the room heading.
- Should fix, general, keyboard: the entire tray preceded the workbench. Panel controls now precede tray items; actual arrows, Shift, Delete and Enter were exercised.
- Should fix, general, voice: editor instructions and imported/renamed first-seen events lacked declared fixed lines. Added how lines and bounded generic event variants, with stale checks and modal-close hush.
- Should fix, general, diagnostics: Line Show me could select an unrelated wall, and an empty show could name disabled controls. It now highlights a relevant wall or directs an empty show to Select.
- Should fix, general, state guidance: Hang now selects a remaining chosen work after removal, and an unhung selection gets the drag instruction. Chosen-but-unhung Walk names the existing tray and Hang, rather than asking for more choices. Empty phone text spans the strip.
- Should fix, general, facts: the guide's 1675 mm upper label height was copied as 67 inches. UI and notes now use rounded metric values with the correct approximate 66-inch conversion; notes identify the source's inconsistency.
- Polish, general, finish: the walk ended with generic completion. Its ending now reports this show's work and jump counts and invites revision, with no claim to have judged artistic quality.
- Polish, general, graphics: replaced Seed Packets, the map's model-like construction and lettering marks, and the window-box-like fire escape with faithful gouache, paper collage and a photograph of an actual fire escape.
- Polish, general, physical labels: paper widths respect neighboring frame edges; centimeter rulers appear in the room while dragging. Readable visitor insets remain.
- Polish, general: missing one-picture grammar corrected; privacy and invented-home alternatives clarified in notes.

#### Findings left

All confirmed blocker and should-fix items repaired; original materials and portfolio strengths retained. The interrupted audit's missing coverage is named below.

#### Break it

Nine live checks, no quiz, reflection gate or separate best score. Browser functional checks: 39/39; imports: 6/6.

- Selection: five choices, nine choices, and a selected but unhung work fail; six-to-eight fully hung works pass.
- Theme: fewer than five matching works fails. Custom tags are student assertions, deliberately not a machine assessment of imagery.
- Anchor: starring a different work fails. Re-starring First seen is an allowed curatorial decision, not evidence that the original intention was achieved.
- Line: a four-centimeter wall mismatch fails; three passes. A real end-to-end slider sweep reached 170 cm and correctly failed against the other used wall at 145 cm.
- Spacing: 14.2857% passes, 16.5354% fails; equal 29 cm gaps fail. Auto space is the specified assist; an eight-work side wall produces 18.6 cm gaps and still fails explicitly.
- Light: a single unlit work fails; repeatedly toggling does not accumulate credit.
- Labels: punctuation-only title and 26-word note fail; 25-word and blank notes pass as specified. No invented minimum note length.
- Statement: blanks, punctuation, 101 words and a 26-word sentence fail. A one-word statement can meet format limits; the interface and notes now explicitly limit the claim to measured checks.
- Flow: alternating disjoint tags fails; grouping the themes into one jump passes. A shared tag is a proxy, not a judgment about meaning.
- All-ready events re-arm after returning/removing works; no best score persists. No need to walk before meeting the numeric rubric is asserted by the spec.

#### Voice walk

Main path: Select six home works and star Window; Hang each, Light, Auto space; write a label and statement; Walk from the door; Checklist. Held clicks, 2 s gaps, Sound on and default settings, using drive.py's Tab and input helpers.
Heard in order: welcomeSelect, selectMore, welcomeHang, lightHow, hangMore, labelHow, statementHow, welcomeWalk, walkComplete, welcomeChecklist. All four mode how lines start once. Modal Done and mode changes intentionally cut speech whose moment has ended.
The cold and two repaired main-path runs exposed an anchor mismatch instead of giving a win. Final main-path replay has zero runtime exceptions or console errors. All 36 final declared lines match voice/lines.json; the added no-hang side-path line was separately heard and re-shot.
Side path: jump events 5 expected, 5 spoken; Read works with Sound off; stale firstSeen events drop when walking begins. A paused door side path hears firstSeen.

| Lines | Kind | Expected | Started |
| --- | --- | --- | --- |
| Four mode welcomes; selectMore | How | 1 each | 1 each |
| lightHow, hangMore, two editor how lines | How | 1 each | 1 each |
| jump, five held revisits | Event | 5 | 5 |
| themeShort: growing / night / city | Event | 1 / 1 / 0 | 1 / 1 / 0 |
| allTicked re-arming, Sound off | Event | 2 eligible | 2 silent, not consumed |

Counts are starts. Modal Done, a changed theme and mode changes intentionally cut speech whose moment ended; no stale speech continues in the replacement state.

#### Facts checked

- Selection, refinement, conveying meaning: [NCAS anchors 4/5/6](https://www.nationalartsstandards.org/), practiced through choosing, hanging, sequencing and writing.
- Label center 137 cm, metric range 122 to 167.5 cm, seated eye range 109 to 129.5 cm, 25-word sentences and 75 to 100-word labels: [Smithsonian Guidelines, II/III](https://www.sifacilities.si.edu/sites/default/files/Files/Accessibility/accessible-exhibition-design1.pdf). Its official indexed passages were retrieved; direct PDF fetch timed out. Rounded ranges and the 67-inch source inconsistency are identified in notes.
- Portfolio selection and refinement: [College Board AP Art and Design](https://apcentral.collegeboard.org/courses/about-ap-art-and-design). The nine checks are this fictional brief's rubric, not AP scoring or legal requirements.
- Fictional artist, credits, media, dimensions, years and five tags: checked every portfolio row against spec Content. Counts independently recomputed: home 6, water 5, city 5, growing 4, night 2; actual theme speech exercised.
- Fictional room geometry and timing: (800 - 120)/2 = 340 cm; mats/frames add 16 cm; eight widest plus seven 30 cm gaps = 685 cm, correcting the spec's 745 cm. First seen independently compared with 2,001 edge samples in three layouts. Motion-off eight-stop run: 24.158 s.
- Rubric arithmetic and units: 40/40/46 cm gaps spread 14.2857%; 40/40/47 spread 16.5354%. 137 cm = 53.94 in; 168 cm = 66.14 in. Recomputed contrast ratios: brand/panel 11.52, brand/section 10.92, brand ink/brand 12.29, label ink/wall 12.49, ink/white 14.34; repaired Walk eyebrow/cream 6.25.

#### Sensitivity

No named cultural tradition, Indigenous content, religion or hard history. A cultural reviewer should check that the fictional Reyes surname is not treated as a cultural proxy and that home/origin prompts allow invented settings without family disclosure. Notes now explicitly provide that choice. Seated eye height is a design reference, not one universal body or view.

#### Flattest moment left

Lighting six works remains a repetitive workbench task. Per-work control is the spec's decision; a new bulk feature was not added. The generic walk ending was lifted with a specific recap.

#### Graphics

All 16 finished images inspected, including room and card use. Three assets redrawn with built-in imagegen, copied into art/raw and converted with art.py --rekey; prompts and provenance saved. No people required or depicted; every asset explicitly marks people false.
Art: 720,234 bytes. Bundle 1,170,809 bytes (1143.4 KB), under 2 MB. Two dense replacements exceed the old 50 KB per-work target, preserving material detail. Several retained works are landscape despite the spec's blanket portrait instruction; they are preserved without distortion.
Compared with both existing bar tools without rebundling outside the allowed folder. review-bar-comparison.png places this gallery beside Beat Lab; the room retains its materials, light, depth and precise controls.

#### Audit

Audit not finished: one run, with the required 40-minute cap, was interrupted by the session restart after Motion off. Its partial review-audit/audit.md and all 89 saved frames were reviewed. No second full audit was started.
All eight initial sizes, every mode, all seven listed populated/dialog states and Motion off completed. The partial report's resize/control-walk placeholders are not counted as passes. Independent held-click main/side walks, controls, keyboard, and a fresh 1366-to-760-to-1366 mid-walk resize passed without exceptions or disabled controls.
All 17 grouped leads are disposed: 14 repeated warnings concern the required scrolling diagnostic checklist, including its inert background behind Clear; these are not hidden answer choices. Three concern the deliberately covered background hint in Label, Statement and Clear dialogs, whose own instructions and controls remain visible.
Audit frames also prompted the empty-phone text correction; focused post-audit frames cover it, removed selections, chosen-but-unhung guidance, and measured-check wording at 680 and 375. No confirmed audit defect remains open. Full automated resize/control-walk coverage remains incomplete.
Wave checks: current hints and once-only how lines, retained focus and controls before tray, 44 px targets, explicit measurement assumptions, meaningful VA:Pr4/5/6 actions, no infinite Motion-off loops, resize recovery, truthful badges, restored hints, and no hidden-answer game. Frame folders and JSON logs are under _scratch/virtual-gallery/; all generated frames were opened directly or in contact sheets.

#### Left open

Spec limit: a short statement and self-assigned tags can meet the numeric rubric without strong interpretation. Claims are explicitly limited to measured checks; adding a semantic gate would change the spec. No best score or artistic mastery claim remains.
Full automated resize/control-walk audit stages were interrupted; their coverage is not represented as complete.
Retained landscape source art and two assets over the individual 50 KB target are deliberate quality choices; the bundle stays well below 2 MB. Camera direction changes travel while retaining the required tray stop order.
Unattended choices follow the spec and baseline; no questions asked. No git commits or writes to shared engines/docs/scripts. All task Chrome/server sessions are closed and host.html is removed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

ROUND 2 (exit check 2026-11-06): should fix 8 partly (empty-show Show me on Selection, Theme, Labels drops focus; Labels says "Tap Label to edit" with no Label control); blocker 1, polish 1 and 13 now fixed
Counts: blockers 1 (general 1, family 0), should fix 12 (general 10, family 2), polish accepted 15

### Refine: virtual-gallery

Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity lens; all three lenses found
nothing cultural, Native or hard-history, and the integrator agrees). Frames are under
`S:/CurioClass-codex-scratch/virtual-gallery/` (`play/`, `craft/`, `teaching/`, `audit-r1/`). Integrator
spot-checks: the door view (blocker 1, read `src.html:1371` and `:1467`, opened `play/f5/u1-sidewalls-door.png`),
the Hang camera (should fix 1, opened `play/f1/02-front-walls.png`) and the art sizes (should fix 3, read every
`art/*.webp` with PIL). All three hold.

#### Blocker
1. **Walk door view names a "First seen" work the picture does not show.** `src.html:1467` (`doorCamera` looks
   straight down the room) with `src.html:1371` (Walk focal 0.82 x width, about 31 degrees each side). The far
   corners of the side walls sit about 33 degrees off axis from the door, so no side-wall work is ever in frame,
   while `firstSeen()` (`src.html:734`) ranks side-wall works. With the back wall empty (Done when 3, second layout)
   the stage is bare plaster, the cone sits on empty wall and the readout says "First seen: Laundromat"
   (`play/f5/u1-sidewalls-door.png`). Fixed looks like: the door view is wide enough that every work `firstSeen()`
   can name is in frame (widen the door focal, keep the camera pointing straight ahead so "straight ahead" still
   means what the Anchor Why says), and the named frame is marked in the scene (see polish 1). Re-shoot the three
   Done when 3 layouts. (general)

#### Should fix
1. **Hang room hides the door wall and its works.** `src.html:1466` `overviewCamera` sits above the door looking in,
   so works on "Door, left" and "Door, right" are behind the camera: the status says "6/6 hung" while four frames show,
   the door is never drawn, and Hang on wall for a door wall looks like nothing happened (`play/f1/02-front-walls.png`).
   The same camera leaves the floor at about 45% of the stage with 40 px frames at 1366x768 and 20 px at 760x900
   (`play/f1/01-home-hung.png`, `play/f3/s7-760-hang.png`). Fixed: pull back or raise the camera (or draw the door wall
   cut away with its frames and the door gap) so all four walls and the door read, with the walls, not the floor,
   filling the stage. (family:virtual-gallery)
2. **Checklist hides most of the nine checks in a scroll panel.** Checklist, `src.html:221-236`: each row is about
   108 px because `Why` takes its own line, so 3.5 of 9 rows show at 1366x768 and one at 680x425; the Show me buttons
   below the fold are off screen. BUILD.md lesson: a short set of choices never hides in a scroll panel. Seen by all
   three lenses (`craft/out/f5-checklist-1366.png`, `craft/out/f6-checklist-680.png`, `play/f1/17-checklist-scroll.png`,
   `audit-r1/state-mode-04checklist-1366x768.png`). Fixed: `Why` beside `Show me` in the row (both 44 px targets), row
   about 56 px, so all nine fit at 1366x768 and most fit in the preview; two columns at wide sizes if needed. (general)
3. **Seven portrait works are drawn landscape, so each frame shows a strip of picture in a tall empty mat.**
   `art/window, teapot, creek, crows, laundromat, rainglass, nightpool` are 800x622 (prompts ask 4:3) against spec Art
   ("Each 3:4 portrait") and the portrait sizes in `src.html:578-591`; `object-fit:contain` leaves blank mat above and
   below (`audit-r1/state-walk-stop-1366x768.png`, `craft/out/v4-walk-play.png`, detail panel in
   `audit-r1/size-1920x1080.png`). Kitchen Window also has a stray cropped orange object at its right edge. Fixed:
   redraw those seven at 3:4 portrait (no people, no lettering, at most 50 KB each), with the Kitchen Window crop
   cleaned in the redraw. (general)
4. **Portfolio cards show no theme tags and no size.** Select, `src.html:869-874`: cards show title, medium and year
   only; spec Select says cards carry "image, title, medium, size, year and theme tags". Choosing six home works means
   opening all 14 cards one by one (`audit-r1/size-1366x768.png`, `play/f1/14-custom-night.png`). Fixed: size and tags
   on each card, the brief's tag highlighted as it is in the detail panel. (general)
5. **The large label card in Walk covers the wall label it repeats.** `.visitor-label` (`src.html:203`) sits
   bottom-right over the sharp wall label; a long title or note is cut mid-word ("coff", "woke u"), which is exactly
   the "labels run long" case the walk is meant to show (`play/f1/05-walk-longnote.png`, `teaching/f/walk-stop3.png`).
   Fixed: place the card so it never overlaps the current work or its wall label (for example the opposite side of the
   stage from the label, or under the stage). (family:virtual-gallery)
6. **A squeezed label becomes a vertical strip of letters in Walk.** `wallArt` (`src.html:1053-1059`) hides a label
   with under 12 px of room, but `drawWalkArt` and `travelTo` (`src.html:1412`, `:1624`) reset every label's
   visibility to '' while moving and between stops, so a 0-width label with `overflow-wrap:anywhere` shows as a tall
   column of single letters between abutting frames (`play/f2/r9-stop-midtravel.png`, `play/f2/r9-zoom.png`). Fixed:
   keep the squeezed-label rule through every Walk redraw. (general)
7. **No wall label at 1100 px wide and under in Walk.** `src.html:259` hides `.walk-room .sharp-label` at max-width
   1100 while `drawWalkArt` still hides the original (`src.html:1464`), so at 1000x625 and 680x425 the work at the stop
   has bare wall beside it (`play/f1/12-walk-1000.png`). Fixed: at those sizes keep one readable label at the stop
   (the sharp one scaled down, or leave the original visible). (general)
8. **Hang with nothing chosen speaks a Walk line and shows a work that is not in the show.** `welcomeKey()`
   (`src.html:708`) returns `noWalk` in Hang ("...hang it on a wall before walking"), the same line follows Show me on
   an empty show (`src.html:1758`), and the workbench title is Creek After Rain from `fresh()` (`src.html:633`) with
   every control disabled (`craft/b.log` v11-ft-mode, `audit-r1/state-mode-02hang-1366x768.png`). Fixed: a Hang line of
   its own ("The tray is empty. Tap Select and add works to the show."), added to `L` and `voice/lines.json`, and an
   empty workbench with no work title. (general)
9. **The jump line is cut off at every jump during Walk the show.** `travelTo` calls `V.hush()` when the visitor
   leaves a stop (`src.html:1617`), and "Here the story jumps. Nothing ties these two together." runs longer than the
   2 s stop (`src.html:1697`): 6 of 6 jump lines cut about 3 s in (`craft/a.log`, `craft/c.log` v4-walk-play); with
   Step they play whole. Spec Done when 11 wants jump every time. Fixed: at a jump stop, start the move only after the
   jump line ends (other stops keep 2 s); Stop, Step, Back and strip taps still act at once. (general)
10. **Every feedback message is announced twice, and a drag floods the screen reader.** `#hint` (`src.html:530`) and
    `#announce` (`src.html:565`) are both `aria-live="polite"` and `feedback()` (`src.html:721-723`) writes the same
    text to both; a drag rewrites `#hint` on every pointer move (`src.html:1878`). Fixed: one live region, and the drag
    hint updates only when the wall or the rounded drop position changes. (general)
11. **Nine of nine tick with no label note written.** Labels check (`src.html:782`, `:806-809`): titles are prefilled
    and blank notes pass, so the label-writing half of the show is never asked for while the walk shows "0 words" on
    every card (Play cheap pass `play/f1/07-checklist-ticked.png`, Teaching `teaching/t1.js` `untouchedLabels: true`).
    Fixed inside the spec's check 7: the Labels line adds a warning, the way the path crossing does, "n labels have no
    note yet" (not a fail; see Settled calls and the open questions for making it a requirement). (general)
12. **The 145 cm default center line is unexplained, and the cited guide says something different.** `fresh()`
    `src.html:632` (`lines` default 145), the wall readout "145 cm · 57.1 in", the Line check and its Why
    (`src.html:796`). The spec sources only the 120 to 170 slider; the Smithsonian guide (section II.A) centers small
    items no higher than 1015 mm (40 in) for seated viewers. Fixed: the Line Why says 145 cm is a starting height for
    standing visitors that this tool uses, not a rule from the guide, and that the guide hangs small items lower so
    seated visitors can see them. No new number on screen without a source. (general)

#### Polish accepted
1. **The first-seen cone is decoration and sits over the work it names.** `.cone-note` (`src.html:219-220`) is a fixed
   triangle at screen center above the frames (z-index 4), aimed at nothing and tinting the named work green; the
   first-seen work is named only in a small mono line (`play/f1/03-walk-door.png`, `craft/out/f4-walk-door.png`).
   Better: aim the cone from the door toward the first-seen frame, draw it at floor level under the frames, and outline
   or spotlight that frame. Do this with blocker 1. (general)
2. **Walk at 680x425: overlays cover the room.** The show card covers the left third and the label card the right third
   of a 190 px stage (`play/f1/11-walk-680.png`). Better: shrink or tuck both overlays at preview sizes so the work at
   the stop stays clear. (general)
3. **Neighbouring wall labels in Walk are blurred smears.** 3 px `.wall-label` text magnified by the camera
   (`src.html:131-134`); only the current stop gets the sharp overlay (`craft/out/v4-walk-play.png`, `play/f1/13-walk-1920.png`).
   Better: blank the text of neighbouring labels while the camera is close (cheapest), or draw them sharp too. (general)
4. **Clockwise / Counterclockwise only changes the camera route.** `src.html:1551`, `:1665`: stops stay in tray order,
   so a student expecting the visit to reverse sees the same sequence. Better: name the button for what it does
   ("Route: clockwise") and say in the hint that the visit order is the tray order. (general)
5. **The walk ends flat.** "Your walk complete · 6 works · 0 story jumps" (`src.html:1704`). Better: add one clause
   comparing First seen with the starred work ("First seen was your starred work" or "First seen was X; you starred
   Y"). (general)
6. **Show me on Anchor is vague.** "Move the selected work or adjust its wall." (`src.html:1754`). Better: say what
   makes a work first seen: the frame closest to straight ahead from the door. (general)
7. **A student whose first tap is Add to show never hears the star.** `selectMore` replaces the welcome
   (`src.html:1006`, audit row 21) and does not mention Star. Better: selectMore ends with "Star the one you most want
   seen." (update `voice/lines.json`). (general)
8. **Order strip numbers and the anchor star are clipped.** `.order-item small` (`src.html:193-201`) sits in a second
   grid row cut by the item border; "3 ★" shows its top half (`craft/zoom-order.png`). Better: put the number before
   the title in the first row. (general)
9. **Seated band wording.** Hang panel line "seated eye level, 109 to 130 cm": the guide's figure is for a wheelchair
   user. Better: "wheelchair user's eye level, 109 to 130 cm". (general)
10. **Double full stop after "a.m."/"p.m." titles.** "Starred: Kitchen Window, 7 a.m.. First seen" (`src.html:793`).
    Skip the added period when the title already ends in one. (general)
11. **"Laundroma t" breaks mid-word in the order strip at 680x425** (`.order-title` overflow-wrap,
    `play/f1/11-walk-680.png`). Break between words only. (general)
12. **Flow line wording.** "0 of 1 allowed jumps in tray order." (`src.html:815`) reads oddly. Better: "0 jumps in tray
    order (1 allowed)." (general)
13. **Truncated control text.** Wall select "Right wall · 6(" with the plan open at 1366x768 (`craft/out/f8-hang-plan.png`);
    tray captions "4 ★ · hun" at 680x425 (`audit-r1/state-compact-full-workbench-680x425.png`). Shorten or let them
    wrap. (general)
14. **Center line slider has no `aria-valuetext`** (`src.html:1139`); announce "145 cm, 57.1 in". Also
    `printShow()` reuses the pattern id `plan-floor-main` (`src.html:1324`); give the print copy its own id. (general)
15. **blockmap (127 KB) and fireescape (98 KB) are over the spec's 50 KB per image.** Re-encode to 50 KB or less if
    they hold up at card and wall size; if not, leave them and note why (the bundle is 1.17 MB, under the 2 MB goal).
    (general)

#### Settled calls
- **Tags on cards (Play 3) vs hide the tags (Teaching 2).** The spec says cards carry theme tags, so Play wins: show
  them (should fix 4). Teaching's "hide tags until chosen, then justify each off-theme work" changes what Select
  teaches, so it goes to the open questions.
- **Cheap all-ticks path (Teaching 3, Play 9).** Within the spec only a Labels warning is taken (should fix 11).
  Requiring a written note, a minimum statement length, or locking the star before the walk would change checks 3, 7
  and 8, so they go to the open questions. The checklist and allTicked line are already honest that meaning is not
  checked, which is why this is not a blocker.
- **Voice lines differ from the spec (Craft nit 11).** Keep the code: allTicked "Every measured check is ticked. Review
  the meaning of your show before opening." is the more honest line, given the checks cannot read meaning; welcomeWalk
  "Tap Walk the show." is fine. Do not change these; the spec's Voice text is the thing to update (open questions).
- **Autoplay stop length (Play 15).** Keep 2 s per stop and the 24 s walk (spec, Done when 6); Stop and Step let a
  student read. Only jump stops wait for their line (should fix 9).
- **Blocker 1 fix direction.** Widen the door view rather than turn the camera, so "straight ahead from the door"
  keeps meaning what the Anchor Why and `firstSeen()` say.
- **Show me on ticked rows (Play nit 22).** Leave it: the spec gives each line a Show me, and it is harmless.
- Do not change: the 1 s move / 2 s stop timing with Motion on and off, the keyboard hang path, the Motion-off walk,
  the themeShort lines (growing and night only), the privacy lines, the audit's "#hint covered" rows under modals
  (expected backdrop) and its "focus lost" rows on lower cards (clicks off the fold, not dead controls).

#### To the spec's open questions
- **VA:Pr6 at the high school level (Teaching 1).** This is the only tool on module `arts-9-12-portfolio-and-curation`;
  the HS Pr6 standards are about an exhibition's effect on viewers, and nothing here asks what a visitor should leave
  understanding. Option: one "A visitor should leave understanding ..." line written before Walk, shown at the walk's
  end beside the order strip with which stops carried it, and printed on the sheet. Otherwise move Pr6 off this module
  and say so.
- **Justify selection (Teaching 2).** A one-line "why it belongs" for each chosen work without the theme tag, needed
  before Theme ticks and printed on the sheet (and/or let the student tag works before seeing Jordan's tags).
- **Make the checks ask for writing (Teaching 3, Play 9).** Labels needs a written note per work; Statement needs a
  minimum (for example 2 sentences or 20 words); the star locks once Walk is entered, or the Anchor line records
  "starred before the walk" so First seen is a prediction.
- **Source the 145 cm default (Teaching 4)** with a named source in Sources, or pick a sourced default; and decide
  whether a wall line above the seated band should get a note.
- **Spec Voice text** for welcomeWalk and allTicked to match the code (see Settled calls).
- **Art record.** `src.html:14` and `art/prompts.json` credit OpenAI gpt-image for seeds, bowl, fireescape, blockmap,
  tomatoes, vg-wall and vg-floor while the spec says local FLUX only; BASELINE rule 11 allows it, so update the spec's
  Art line.
- **Your theme naming (Play nit 23).** The brief says "Name your own show" but there is no name field in Select; the
  title stays "Your theme" until the Statement dialog.

#### Not taken
- Play 10 (hang view mostly floor): folded into should fix 1, same camera.
- Craft 9 (Kitchen Window crop): folded into should fix 3, same redraw.
- Play 15 (longer autoplay stops): against spec timing; see Settled calls.
- Play nit 22 (Show me only on unticked rows): spec gives every line a Show me.
- Play nit 23 (Your theme title): needs a spec decision; sent to open questions.
- Craft nit 11 (voice text vs spec): code kept; spec to move.
- Craft nit 12 (art provenance): record item only, sent to open questions.

#### Exit check (2026-11-06)

Cold check by Claude. Frames in `S:/CurioClass-codex-scratch/virtual-gallery/exit/f/` (contact sheets `sheet1-3.png`,
`zoom-left.png`), shots in `exit/shots.json`, audit in `exit/audit-r2/`. Layouts built with `__tool.place()` after
opening Hang, so every position is a legal clamp. No console errors in any shot (an early run that called `place()`
from Select threw in `renderHangTools`; that path is test-only, a student cannot reach it).

##### Blocker
1. **Open.** Back-wall layout (`door-back`) and near-door side layout (`door-sides`) now show and outline the named
   frame. But two legal layouts still name a First seen work the picture does not show:
   - Left wall, far end. `door-sides-far` (Blue Teapot at Left wall x=520) and `door-left-corner` (Kitchen Window,
     `place()` clamped to x=577) both read "First seen: ..." over a bare left wall with no outline (`zoom-left.png`),
     while the DOM box for the frame sits inside the window ([96,301,47,76] and [123,299,42,78]). Right wall at the
     same depth paints (`door-sides`, Codex `last-door-edge-right`), so this is a Left-wall paint or clip fault, not
     field of view. Codex's "left-edge probe, unconfirmed" is confirmed on a legal layout.
   - All works on the door wall (`door-only`): bare room, "First seen: Map of My Block", Anchor passes for a work no
     visitor at the door can see. Codex flagged this as a spec decision. The exit check's reading: the Settled call
     was about which way the camera points, not about ranking walls behind the visitor, so excluding the two door
     walls from `firstSeen()` (and failing Anchor with a line such as "No work is in view from the door") is inside
     the blocker's "every work firstSeen() can name is in frame". If the integrator disagrees, it goes to Cory.

##### Should fix
1. Fixed. Door wall unfolds below the room with the door gap; 6/6 frames show at 1366x768 and 760x900 (`hang-1366`,
   `hang-760`). Frames are still small (about 25 to 40 px) but walls now fill most of the stage.
2. Fixed. Checklist in two columns at 1366x768, all nine rows with Why and Show me visible; 680x425 shows 8 of 9,
   Flow under the fold (`checklist-1366`, `checklist-680`). Audit's "scroll panel" lead at 680 and 375 is this one row.
3. Fixed. Seven works now 600x800, under 50 KB each (Codex `after-art.json`); portrait frames fill their mats in Walk
   and Select (`walk-stop-1366`, `select-1366`).
4. Fixed. Cards show size and theme tags, brief tag highlighted (`select-1366`).
5. Fixed. Long note reads whole on the wall label, duplicate is a disclosure under the room, no overlap
   (`walk-stop-1366`).
6. Fixed. `data-squeezed` kept through redraw (`src.html:527`, `:1542`); Codex `proof/squeezed-moving.png` shows no
   letter strip.
7. Fixed. Readable current wall label at 1000x625 and 680x425 (`walk-stop-1000`, `walk-stop-680`).
8. Fixed. Empty Hang: "The tray is empty" workbench, emptyHang line spoken (`empty-hang`, audit row 1).
9. Fixed. Three of three jump lines spoken whole, about 5 s apart (Codex `proof/jump-autoplay.json` vlog); code awaits
   the line.
10. Fixed. Live regions are `#hint` and `#own-message` only (shot JSON); drag hint writes on change.
11. Fixed. Labels row shows "Warning: 6 labels have no note yet." (`checklist-1366`).
12. Fixed. Line Why says 145 cm is the tool's standing start, not the guide's, and that the guide hangs small items
   lower (Codex `jump-autoplay.json` checks text).

##### Polish (bulk spot-check)
Fixed: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 (seen on the frames above or in the check texts).
Partly: 1 (cone and outline work where the frame paints; missing in both blocker cases). 13 (tray captions "1★ hung"
fit at 680x425, `hang-680-tray`; the wall select still reads "Back wal" there).

##### Regressions
None found in the default screen, each mode once, or the frames tied to the fixes. Hang at 680x425 opened in Plan
(restored state), which is fine.

##### Gate
1. Done when: open. Done when 3 (first seen from the door) fails for the two blocker layouts.
2. Codes: unchanged this round; VA:Pr6 depth stays on the spec's open questions.
3. Solo defaults: work (default screen, empty Hang guidance, Select with tags).
4. Sensitivity: rule 5 does not apply (no lens or merge flag).
5. No blocker or should-fix open: no, blocker 1.
6. Bundle clean: 1.12 MB (under 2 MB), no console errors, no em dashes in src.html; network not re-measured (audit cut short), Codex offline-contract probe shows zero requests.
7. Voice: 37 lines in `voice/lines.json`, matches Codex's allLines count; held-click table clean, emptyHang and
   selectMore heard where expected.

#### Audit pilot
- The audit ran into the 1500 s limit (exit 124) after the click and voice tables; stress checks and the network
  section were not saved. Sizes, mode states and held clicks came through.
- Leads confirmed: checklist row cut by the scroll panel at 680x425 and 375x812 (one row, Flow, accepted as "most
  fit"); Add to show as a first tap does not hear the welcome (accepted by polish 7, selectMore now carries the star).
- Leads wrong or expected: 3 px `wall-label` and 4 px intro text in the cutaway and compact states (scaled 3D text,
  the readable sharp label is drawn separately); "focus lost" on lower cards (off the fold); clipped `order-title`
  at 1366 for "1 ★ Kitchen Window, 7 a.m." (ellipsis by design).
- Missed: the blocker. Every door-view frame has an in-window DOM box, so a box-based check cannot see that a
  Left-wall frame never paints; only the picture shows it.

#### Exit check round 2 (2026-11-06)

Round 2 re-check by a cold Claude agent after Codex round 2 (`polish.md`; round 1 account in `polish-1.md`). Frames in
`S:/CurioClass-codex-scratch/virtual-gallery/exit2/f/` (contact sheets `sheet-door.png`, `sheet-modes.png`), shots in
`exit2/shots.json` and `exit2/s3.json`, audit in `exit2/audit-r2/`. Layouts built with `__tool.place()` after opening
Hang, as in the first exit check. No console errors in any shot.

##### Blocker
1. **Fixed.** All six door layouts at 1366x768 paint and outline the named frame: back wall (`door-back`, Seed
   Packets), near-door sides (`door-sides`), far sides (`door-sides-far`, Blue Teapot now painted at Left x=520),
   left corner clamp (`door-left-corner`, Kitchen Window at x=577, also at 680x425), and a new full Left wall sweep
   (`door-left-mid`, Map of My Block at x=560). All-door-wall (`door-only`): no outline or cone, readout "No work is
   in view from the door", and `firstSeen()` returns null; the Checklist Anchor row fails with "Starred: Kitchen
   Window, 7 a.m. No work is in view from the door." (`door-only-checklist`). The camera still points straight
   ahead (`src.html:836-853` filters the `front` walls only).

##### Should fix
1 to 7 and 9 to 12. Fixed, unchanged from the first exit check (spot-checked on `mode-hang`, `mode-checklist`,
`hang-1366-plan`, `hang-680-tray`; Labels warning and two-column checklist present, door wall unfolds with all six
frames, cards show size and tags on `default`).

8. **Partly.** Empty Hang itself is right (emptyHang line, "The tray is empty" workbench, held-click audit row 1),
   and Show me on Anchor (and the other hung-dependent rows) lands on emptyHang with focus on Select. But Show me on
   an empty show still misleads for three rows (`empty-showme-*.png`, real clicks, nothing chosen): Selection and
   Theme drop focus to the body (target `wall-choice` is not rendered in empty Hang); Labels says "Every selected
   work has a title; notes are 25 words or fewer. Tap Label to edit." with no Label control on screen and focus on
   the body (`empty-showme-labels.png`). Statement is fine (focus on Statement). Codex reported the same and left it
   open (`polish.md` should fix 8). Narrow fix: in `showProblem()` (`src.html:1912-1951`) handle an empty
   `state.chosen` first for selection, theme and labels: `L.emptyHang` and focus `m-select`/`empty-select`.

##### Polish (bulk spot-check)
1. Fixed now: the named frame is outlined in every door layout; no cone or name when nothing is in view.
13. Fixed now: wall select reads "Back" at 680x425 and 1366x768 with Plan open (`hang-680-tray`,
    `hang-1366-plan`); tray captions whole.
The other thirteen stay fixed as in the first exit check.

##### Regressions
None found. Default screen (Select with tags), Hang, Walk, Checklist each once, and the door, corner and empty-Show-me
frames tied to this round's fixes. Left-wall `preserve-3d` shows no seam on the back wall in any frame.

##### Gate
1. Done when: pass (Done when 3, first seen from the door, now holds for every layout tried).
2. Codes: unchanged; VA:Pr6 depth stays on the spec's open questions.
3. Solo defaults: work.
4. Sensitivity: rule 5 does not apply.
5. No blocker or should-fix open: no, should fix 8 partly (empty Show me on Selection, Theme, Labels).
6. Bundle clean: 1,120,120 bytes (under 2 MB), no console errors in drive shots or audit, no em dashes in src.html;
   network not re-measured (the audit hit its 1500 s limit, exit 124, after the click and voice tables again); Codex's round 2 offline probe recorded zero requests.
7. Voice: 37 lines in `voice/lines.json`, matching Codex's allLines count; held-click table clean (emptyHang on Hang,
   selectMore with the star on Add to show, noWalk only in Walk).

#### Audit pilot (exit check, round 2)
- Ran into the 1500 s limit (exit 124) after the click, five-held-click and two-quick-tap tables; network section not
  saved. Its Chrome was left behind and was stopped by this check.
- Leads confirmed: Checklist Show me on Selection, Theme and Labels "rebuilt, focus lost" (empty show), reproduced
  with real clicks (should fix 8).
- Leads wrong or expected (all settled earlier): checklist Flow/Statement rows below the fold at 680x425 and
  375x812; `#hint` behind modal backdrops; 3 to 8 px text in the cutaway and intro panel (scaled 3D text);
  `order-title` ellipsis at 1366; "focus lost" on off-fold portfolio cards; Add to show replaces the welcome
  (selectMore carries the star).
- Missed: the wrong "Tap Label to edit" line on an empty Labels Show me (it checks focus, not the words of a hint).

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: virtual-gallery (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/virtual-gallery/virtual-gallery.html` as built (not re-bundled).
Own frames and logs: `S:/CurioClass-codex-scratch/virtual-gallery/craft/out/` (shots in `shots.json`, logs `a.log`,
`b.log`, `c.log`). Shared audit: `S:/CurioClass-codex-scratch/virtual-gallery/audit-r1/`.

Counts: blocker 0, should fix 4, polish 5, nit 6.

#### Findings

##### Should fix

1. **Seven portrait works are drawn as landscape pictures, so every frame shows a small picture floating in a tall
   empty mat.** Where: `art/prompts.json` (window, teapot, creek, crows, laundromat, rainglass, nightpool all ask
   `"aspect": "4:3"`, and the files are 800x622), against spec Art ("Each 3:4 portrait, the listed size read as width
   x height") and the sizes in `src.html:578-591` (30 x 40, 28 x 36, 46 x 61, 23 x 30, 36 x 48, 40 x 50, 50 x 70, all
   taller than wide). The frame is drawn at the real portrait size and the image is `object-fit:contain`, so a 46 x 61
   cm canvas shows as a landscape strip with blank mat above and below; the card says "46 x 61 cm" while the picture is
   wider than tall. How seen: `audit-r1/state-walk-stop-1366x768.png` (Creek, grey bands top and bottom),
   `craft/out/v4-walk-play.png` (Laundromat), `audit-r1/size-1920x1080.png` (detail panel: a tall empty box with a
   landscape creek in the middle); image sizes read with PIL. Better: redraw these seven at 3:4 (or the listed ratio)
   so the picture fills its frame, as busstop, seeds and tomatoes already do. Tag: general.

2. **The jump line is cut off mid-sentence at every jump during Walk the show.** Where: `src.html:1617` (`travelTo`
   calls `V.hush()` when the visitor leaves a stop) with the 2 s stop at `src.html:1697`. "Here the story jumps.
   Nothing ties these two together." runs longer than the 2 s pause, so the move to the next stop hushes it. How seen:
   `craft/a.log`/`c.log` v4-walk-play: 6 jumps, 6 `jump` spoken, all 6 with `cut: hush` about 3 s after starting.
   With Step (v16) the 4 jump lines play whole. Better: hold the stop until a jump line has finished (or start the move
   only after it ends), or drop it with `valid` instead of a hush. Tag: general.

3. **The checklist shows only part of the nine checks.** Where: Checklist, `src.html:227-236` (each row about 108 px
   tall, because the `Why` summary takes its own 44 px line under the text). At 1366x768 the list scrolls 1041 px in a
   422 px box (3.5 rows visible), at 680x425 1041 in 132 (one row). A student cannot see their show's status at a
   glance, which is the point of the mode. How seen: `craft/out/f5-checklist-1366.png`, `f6-checklist-680.png`,
   `audit-r1/state-mode-04checklist-*.png`; audit lead "choices cut short by a scroll panel" at every size. Better:
   put `Why` beside `Show me` (both 44 px targets, side by side) so a row is about 56 px; nine rows then fit at
   1366x768, and the preview sizes show most of them. Tag: general.

4. **Every feedback message is announced twice to a screen reader.** Where: `src.html:530` (`#hint` is
   `aria-live="polite"`), `src.html:565` (`#announce` is also polite), `src.html:721-723` (`feedback()` writes the same
   text to both). Also `src.html:1878`: a drag rewrites the live `#hint` on every pointer move, so a screen reader is
   flooded while dragging. How seen: code read. Better: one live region (drop `#announce`, or take `aria-live` off
   `#hint` and keep the announcer), and update the drag hint only when the wall or the rounded drop position changes.
   Tag: general.

##### Polish

5. **Order strip numbers and the anchor star are clipped.** Where: Walk, `.order-item small` (`src.html:193-201`):
   the stop number sits in a second grid row cut by the item's bottom border; "3 ★" shows only its top half.
   How seen: `craft/zoom-order.png` (from `out/f4-walk-door.png`, 1366x768). Better: put the number in the first row
   (before the title) or give the item room for it. Tag: general.

6. **Neighbouring wall labels in Walk are blurred smears.** Where: Walk stops, `.wall-label` at a 3 px font
   (`src.html:131-134`) magnified by the 3D camera; only the current work's label gets the sharp overlay
   (`drawWalkArt`). How seen: `craft/out/v4-walk-play.png`, left edge: a large white label with unreadable grey blur.
   Better: draw any label that is in view at a stop with the same sharp path, or blank its text while the camera is
   close. Tag: general.

7. **Hang with nothing chosen speaks a Walk line.** Where: `welcomeKey()` `src.html:708` gives `noWalk` in Hang:
   "Tap Select to choose a work, then tap Hang and hang it on a wall before walking." The student is already in Hang
   and has not asked to walk. The same line is the hint after `Show me` on an empty show (`src.html:1758`). How seen:
   `craft/b.log` v11-ft-mode (first tap Hang, `noWalk` spoken); audit table rows 1 and 2. Better: a Hang line of its
   own ("The tray is empty. Tap Select and add works to the show."), in `L` and voice/lines.json. Tag: general.

8. **The first-seen cone is drawn over the artwork it names.** Where: Walk at the door, `.cone-note`
   (`src.html:219-220`) sits above the frames (z-index 4), tinting the first-seen work green. How seen:
   `craft/out/f4-walk-door.png` (Bus Stop, 10 p.m. under the cone). Better: draw it lower (floor level, below the
   frames) or as an outline, so the work the student is judging stays clean. Tag: general.

9. **Kitchen Window has a stray cropped object at its right edge.** Where: `art/window.webp`, an orange strip of a
   neighbouring element cut by the picture edge. How seen: `audit-r1/size-1920x1080.png`, first card. Better: fold into
   the redraw in finding 1. Tag: general.

##### Nit

10. Two images are over the spec's 50 KB per-image cap: blockmap 127 KB, fireescape 98 KB. The bundle is 1.17 MB, well
    under the 2 MB goal, so this is only a spec mismatch. Tag: general.
11. Lines differ from the spec's Voice section: welcomeWalk is "Tap Walk the show." (spec: "...to follow a visitor
    through the door."), allTicked is "Every measured check is ticked. Review the meaning of your show before opening."
    (spec: "Every check is ticked. Your show is ready to open."). voice/lines.json matches the code word for word; the
    integrator decides whether the spec or the code moves. Tag: general.
12. Art provenance: `src.html:14` and prompts.json name OpenAI gpt-image for seeds, bowl, fireescape, blockmap,
    tomatoes, vg-wall and vg-floor, while the spec says local FLUX only. No people in any of the 16 (all
    `people: false`, none seen); BASELINE rule 11 allows Codex drawing, so this is a record item. Tag: general.
13. Truncated control text: the Wall select reads "Right wall · 6(" with the plan open at 1366x768
    (`out/f8-hang-plan.png`); tray captions read "4 ★ · hun" at 680x425 (`audit-r1/state-compact-full-workbench-680x425.png`).
    Tag: general.
14. The center line slider has no `aria-valuetext` (`src.html:1139`), so it is announced as "145" with no unit. Add
    "145 cm, 57.1 in". Tag: general.
15. `printShow()` builds a second SVG with the same pattern id `plan-floor-main` as the open plan (`src.html:1324`),
    a duplicate id in the page while the print sheet exists. Tag: general.

#### Contract

- One file, 1,170,809 bytes (2 MB goal met). No `http` URLs in the bundle; `performance.getEntriesByType('resource')`
  empty after a full hang (`f1-hang8`). No console errors or exceptions in 27 shots (one exception came from my own
  harness calling `__tool.place` outside Hang, not reachable from the page).
- Kit used: `Curio.voice`, `Curio.init`, `Curio.tone/yes`, `theme-912`, kit focus ring. Not re-implemented.
- Frame times (rAF deltas, 1366x768, muted headless Chrome with software rendering): Walk the show with 8 works,
  1863 frames, median 16.7 ms, p95 16.7 ms, max 33.4 ms, 1 frame over 20 ms. Motion off walk: max 16.8 ms.
- Access: every control is a real button, select or range with 44 px targets (audit clean at all sizes); kit
  focus ring visible; keyboard hang path works (`k1`: Enter on a tray work hangs it at 400 cm, ArrowRight x2,
  Shift+ArrowRight, ArrowLeft gives 430 cm; `k2`: Delete returns it, focus stays on the tray work). Pass/fail is icon
  plus words ("Meets check" / "Needs attention"), never color alone. Contrast of small text checked: medium line
  7.5:1, save note 7.8:1, tray caption 7.1:1, visitor small 6.3:1. Motion and Sound work (audit Motion off clean).
- Words: no em dashes in src, notes, lines, prompts; "Curio Class" everywhere; classroom-safe; privacy stated in the
  footer, the own-pictures line and the checklist note.
- Art tokens: all 16 `art:` tokens have prompts.json entries and files.

#### Voice check (held clicks 0.12 s, Sound on, Motion on, 1366x768)

| line | kind | run | expected | spoken |
|---|---|---|---|---|
| welcomeSelect | how | card first tap, then 5 adds | 1 | 1 |
| selectMore | how | 5 adds, 3.5 s apart | 1 | 1 (then silent x4) |
| welcomeHang | how | 5 hangs | 1 | 1 |
| lightHow | how | 5 hangs; then Light x5 | 1 | 1 |
| hangMore | how | 5 hangs | 1 | 1 |
| inspect (Hang welcome, work hung) | how | Hang entered 5 times | 1 | 1 |
| welcomeWalk | how | Walk entered 5 times | 1 | 1 |
| firstSeen | event | Walk entered 5 times | 5 | 5 |
| welcomeChecklist | how | Checklist entered 5 times | 1 | 1 |
| themeShort | event | growing, night, growing, city, night | 4 | 4 (none for city) |
| jump | event | Walk the show, 6 jumps | 6 whole | 6, all cut (finding 2) |
| jump | event | Step x5, 4 jumps | 4 | 4 whole |
| walkComplete | event | end of walk | 1 | 1 |

- Stale lines (v7, taps 0.2 s apart through Walk, Step x3, Hang, Checklist, Walk, Walk the show, Stop): every line was
  cut or dropped by the next action; nothing played after its moment.
- First tap: Read speaks the hint only (v8); Sound says nothing, Sound on again brings welcomeSelect once (v9); Tab
  brings the welcome (v10); a mode button speaks that mode's welcome (v11, but see finding 7); Walk the show skips the
  welcome and speaks only its own line (v12); Step brings continueWalk (v16).
- Read during the welcome cuts it and speaks the hint (v13); Read works with Sound off (v14); a mode change right after
  Read speaks at once (v13, 0.1 s after the tap).
- Order: lines follow the actions in every run.
- Each spoken line was checked against the frame at its time; finding 7 is the one that does not fit its screen.

#### Audit pilot

- Confirmed: "choices cut short by a scroll panel" on Checklist and clear-confirm (finding 3).
- Confirmed but not a finding: "#hint covered" in label-open, statement-open and clear-confirm: the modal backdrop
  dims the hint, but each dialog carries its own instructions and Done button.
- Wrong or harmless: "welcome not heard" after a first tap on Add to show follows the spec (welcomeSelect is stale once
  a work is added), though that student never hears "Star the one you most want seen" (a Play/Teaching call).
  "focus lost" on cards 15 to 18 and "nothing changed" / "covered" on the lower Why and Show me rows: the click landed
  on the footer or outside the scroll box for controls cut by the fold, not dead controls.
- Missed: landscape art in portrait frames (1), the jump line cut during the walk (2), the double live region (4),
  clipped order-strip numbers (5), blurred neighbour labels (6), the cone over the art (8).

No cultural, Native or hard-history content found; nothing flagged for a sensitivity review.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: virtual-gallery (round 1)

Played twice: as a 9-12 student alone at home (first run, no teacher, held clicks, real drags and keys) and as a
teacher projecting at 1366x768 and 1920x1080. Bundle as built (not re-bundled). Frames in
`S:/CurioClass-codex-scratch/virtual-gallery/play/f1` to `f5`; audit frames in `.../audit-r1`.

What works: the Select welcome names the action, the 6 to 8 counter and badges read clearly, drag from the tray to a
wall (jittered pointer) and to a side wall both land where dropped (f2/r2, r3, r6), keyboard Enter on a tray work
hangs it and arrows move it 5 or 25 cm (f2/r4), Plan replaces the room at 680x425 and 375 (f1/10, f3/s4), Walk
keeps 1 s moves and 2 s stops with Motion on and off (f2/r7 and r8: stop changes at 0, 3.0, 6.0, 9.0 s in both),
Stop mid-move holds between works and Step resumes (f2/r9, r10), jump marks and the jump line land on the right stop
(f1/08), allTicked plays once all nine checks pass (f4/t1), the night and growing hints are right (f1/14, f4/t2).

#### Findings

##### Blocker

1. **Walk, door view: "First seen" names a work the view does not show.** `src.html:1467` (doorCamera looks
   straight down the room) with `src.html:1371` (focal 0.82 x width, about 62 degrees across) never shows the side
   walls, while `firstSeen()` (`src.html:734`) ranks side-wall works. With the back wall empty (Done when 3's second
   layout) the door view is a bare wall and the readout says "First seen: Laundromat". The walk's whole promise is
   "shows what they see first"; here the picture and the readout disagree, and the cone sits on empty wall.
   Seen: f5/u1-sidewalls-door.png. Better: widen the door view (or turn the camera toward the first-seen work) so the
   named work is in frame and marked. general.

##### Should fix

2. **Hang room hides the door walls.** `src.html:1466` overviewCamera sits above the door looking in, so works on
   "Door, left" and "Door, right" are behind the camera: the status says "6/6 hung" while four frames show, and the
   door itself is never drawn. A student who picks Door, left and taps Hang on wall sees nothing happen.
   Seen: f1/02-front-walls.png. Better: pull the camera back or up so the door wall is in view, or draw the door wall
   cut away with its frames. family:virtual-gallery.
3. **Portfolio cards show no theme tags (and no size).** `src.html:869-874` shows title, medium and year only; the
   spec's Select says cards carry "image, title, medium, size, year and theme tags". Choosing six "home" works means
   opening all 14 cards one by one to read tags in the side panel, which is the slowest part of the first two minutes.
   Seen: audit size-1366x768.png, f1/14-custom-night.png. general.
4. **The checklist hides most checks in a scroll panel.** `src.html:221-236`: nine 108 px rows in an inner scroller,
   about 3.5 visible at 1366x768 (fewer at 680x425). A student cannot see the state of the show at a glance, and the
   "Show me" buttons below the fold are off screen. BUILD.md lesson "a short set of choices never hides in a scroll
   panel". Seen: audit state-mode-04checklist-1366x768.png, f1/07, f1/17. Better: compact rows (Why inline or as a
   tooltip, Show me only on unticked rows), or two columns at wide sizes. general.
5. **A squeezed label turns into a vertical strip of letters in Walk.** `wallArt` (`src.html:1053-1059`) hides a
   label with under 12 px of room, but `drawWalkArt` and `travelTo` (`src.html:1412`, `1624`) reset every label's
   visibility to '' while moving and between stops, so a 0-width label with `overflow-wrap:anywhere` shows as a
   tall column of single letters between two abutting frames. Seen: f2/r9-stop-midtravel.png (zoom f2/r9-zoom.png).
   general.
6. **No wall label at 1100 px wide and under in Walk.** `.walk-room .sharp-label {display:none}` at max-width 1100
   (`src.html:259`) while `drawWalkArt` still hides the original label (`src.html:1464`), so at 1000x625 and 680x425
   the work at the stop has bare wall beside it. "Which labels run long" is invisible in the preview sizes.
   Seen: f1/12-walk-1000.png. general.
7. **The large label card covers the wall label it repeats.** `.visitor-label` (`src.html:203`) sits bottom-right
   over the sharp wall label; with a long title or note the wall label is cut mid-word ("coff", "woke u"). The two
   copies collide exactly when the label is long, the case the walk is meant to show. Seen: f1/05-walk-longnote.png.
   family:virtual-gallery.
8. **Hang with nothing chosen: wrong words and a work that is not in the show.** `welcomeKey` returns `noWalk` in
   Hang (`src.html:708`), so the student in Hang hears "Tap Select to choose a work, then tap Hang and hang it on a
   wall before walking", and the workbench title is Creek After Rain (the `fresh()` default, `src.html:633`) with
   every control disabled. Seen: audit state-mode-02hang-1366x768.png and its table row 1. Better: a Hang-specific
   line ("Tap Select and add works to the show first.") and an empty workbench. general.
9. **Nine of nine with no label written.** Cheap pass: six home works, Hang on wall six times, Auto space, Light
   each, star whatever is centred, a four-word statement ("These places are home."): every check ticks and "Every
   measured check is ticked" plays. Titles are prefilled and blank notes pass (`src.html:782`), so the label-writing
   half of the show is never asked for, while the walk shows "0 words" on every card. Seen: f1/07-checklist-ticked.png,
   f4/t1 log. Better: Labels counts a note as written (or flags "n labels have no note" as a warning the way the path
   crossing is). general.

##### Polish

10. **The hang view is mostly floor.** At 1366x768 the floor fills about 45% of the stage and frames are about 40 px
    tall (f1/01); at 760x900 the room is a small box with frames about 20 px and the door-light trapezoid floats in
    empty space under the floor (f3/s7-760-hang.png). Better: a lower, closer camera so the walls fill the stage.
11. **The cone is decoration.** `.cone-note` (`src.html:219`) is a fixed triangle at screen centre, not aimed at
    anything, and the first-seen work gets no mark in the scene, only a small mono line bottom-left (f1/03, f3/s8).
    Better: outline or spotlight the first-seen frame and point the cone at it.
12. **Walk at 680x425: overlays cover the room.** The show card covers the left third and the label card the right
    third of a 190 px stage; the neighbour frame sits under the show card (f1/11-walk-680.png).
13. **Neighbour works and labels blur in Walk.** Only the current stop is redrawn sharp; neighbours are 3 px CSS
    labels scaled up and look smeared, worst at 1920x1080 (f1/13, f1/06).
14. **Clockwise / Counterclockwise only changes the camera route.** `src.html:1551`, `1665`: the stop order stays the
    tray order, so a student who toggles expecting the visit to reverse sees the same sequence. Better: a label such
    as "Route: clockwise" plus a hint line, or make it reverse the visit.
15. **Autoplay stops are too short to read a label.** 2 s per stop (spec) against POLISH's 1400 + 75 ms per character:
    a 25-word note needs about 12 s. The student can press Stop, but the autoplay walk never lets a label be read.
16. **The walk ends flat.** "Your walk complete · 6 works · 0 story jumps" (`src.html:1704`) says nothing about the
    anchor; one line comparing First seen with the star would land the lesson of the walk.
17. **Show me on Anchor is vague.** "Move the selected work or adjust its wall." (`src.html:1754`) does not say what
    makes a work first seen (closest to straight ahead from the door).
18. **A student whose first tap is Add to show never hears "Star the one you most want seen."** The tap's own
    selectMore line replaces the welcome, and selectMore does not mention the star (audit row 21, confirmed in code
    `src.html:1006`).

##### Nit

19. Double full stop after titles ending in "a.m." or "p.m.": "Starred: Kitchen Window, 7 a.m.. First seen" (`src.html:793`; f3/s2 hint text).
20. "Laundroma t" breaks mid-word in the order strip at 680x425 (`.order-title` overflow-wrap; f1/11).
21. "0 of 1 allowed jumps in tray order" reads oddly (`src.html:815`); "0 jumps (1 allowed)".
22. Show me appears on ticked rows too (f1/07).
23. "Your theme" keeps that title in Select whatever tag is picked; the show can only be named in the Statement
    dialog in Hang.

Counts: blocker 1, should fix 8, polish 9, nit 5. Nothing cultural, Native or hard-history; no sensitivity review
needed (the "Where I'm From" prompt is handled in notes.md, Teaching with care).

#### Audit pilot

- **Confirmed:** the checklist rows cut by a scroll panel (finding 4); Add to show as a first tap skipping the
  welcome (finding 18, polish only, since selectMore still names the next step); the Hang mode spoken line (table
  row 1) is the wrong-words lead in finding 8; clean size rows and Motion-off timing held on my frames.
- **Wrong or benign:** "keep region #hint covered" in label-open, statement-open and clear-confirm is the modal
  dialog's backdrop over the footer, expected for a modal. "Focus lost" on cards bowl to blockmap is the click
  landing below the fold on partly visible cards (my own scripted clicks there hit the footer); a real user scrolls.
- **Missed:** the door view that shows nothing while naming First seen (blocker 1), door-wall works invisible in Hang
  (2), cards without tags (3), the vertical letter strip (5), labels gone at 1100 px and under (6), the label card
  covering the wall label (7), the Creek After Rain empty workbench (8), the nine-of-nine cheap pass (9).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: virtual-gallery (round 1)

Cold Teaching lens, 2026-11-05. Read spec.md, src.html, notes.md, tool.draft.json, the shared audit
(`S:/CurioClass-codex-scratch/virtual-gallery/audit-r1/audit.md`). Not a Curiosity (lesson norms apply). Own checks
ran through `scripts/drive.py` on the built bundle (port 9801), scripts and frames in
`S:/CurioClass-codex-scratch/virtual-gallery/teaching/` (`t1.js`, `t2.js`, `t3.js`, `f/*.png`).

Second sources, read for this lens: the Smithsonian Guidelines for Accessible Exhibition Design PDF (text extracted
locally) and the NCAS Visual Arts "at a glance" PDF (2021 rev., text extracted locally) for the HS performance
standards under VA:Pr4, Pr5, Pr6.

#### Findings

##### 1. VA:Pr6 is mentioned, not taught at the high school level (should fix, general)
- Where: module `arts-9-12-portfolio-and-curation` (VA:Pr4;VA:Pr5;VA:Pr6), notes.md "Standards and sources"; this is
  the only tool on the module (`data/tools-concepts.csv:207`), so nothing else covers the code.
- What: the HS performance standards under Pr6 are all about the exhibition's effect on viewers: Pr6.1.Ia "Analyze
  and describe the impact that an exhibition or collection has on personal awareness of social, cultural, or political
  beliefs and understandings", IIa "Make, explain, and justify connections between artists or artwork and social,
  cultural, and political history", IIIa "Curate a collection ... to impact the viewer's understanding of social,
  cultural, and/or political experiences". The tool's Pr6 activities are a tag-based Flow check and a statement whose
  meaning is never looked at ("Format checked; review the meaning yourself"). Nothing asks what a visitor will come
  away understanding, and the Walk never compares the visitor's experience with the curator's intent beyond the
  First seen work. The notes' claim ("VA:Pr6 is practiced through arranging a visitor sequence, writing a statement,
  and revising the show after walking it") describes the anchor wording, not the 9-12 standard.
- How seen: NCAS at-a-glance PDF text; src.html `checks()` (lines 810 to 816); cheap-pass run below.
- Better: a real activity, not a thin one (BASELINE rule 2): before Walk, the curator writes one line "A visitor
  should leave understanding ..." (Where I'm From is a natural fit: a neighborhood, a family routine, a community);
  the walk ends on that line beside the order strip and asks which stops carried it and which jump broke it, and the
  printed sheet keeps it. Otherwise move Pr6 off the module to a tool that teaches exhibition impact (gallery-critique
  or the art-museum family) and say so.

##### 2. Selection (VA:Pr4) reduces to matching lime tags; nothing asks the student to justify a choice (should fix, family:none / general)
- Where: Select mode, `tagsHTML()` (src.html:663, `.tag.match` lime highlight), Theme check (src.html:789).
- What: HS Pr4 asks students to "analyze, select, and critique" (IIa) and "critique, justify, and present choices"
  (IIIa). The tool pre-tags every work and highlights the tag that matches the brief, and the Theme check counts those
  tags, so a student passes Theme by picking lime chips without looking at a single picture. The key skill "Choose
  works for a theme and explain the exceptions" (notes.md) has no place to explain anything: a work without the tag
  joins silently, and the Water brief, which needs one such work, never asks why.
- How seen: t1.js cheap run (6 home-tagged works, nothing read) passes Theme; `tagsHTML()`.
- Better: hide the tags until the student has chosen (or let the student tag works, then compare with Jordan's
  tags), and give every chosen work without the theme tag a one-line "why it belongs" box that the Theme check needs
  before it ticks; print those lines on the sheet. That is the "justify" in the standard.

##### 3. All nine checks tick with no writing beyond one character (should fix, general)
- Where: Labels check (src.html:806 to 809), Statement check (src.html:810), Anchor check (src.html:792).
- What: the REFINE cheap-way test. Choose the six home works, Hang on wall six times, Auto space, light each, star
  whatever Walk names First seen, type "x" as the statement: 9 of 9 met, "Every measured check is ticked" plays.
  Labels passes with every note blank and every title untouched (Jordan's titles are pre-filled), so the key skill
  "Write concise labels ... for an audience" is never exercised; the 25-word limit only ever bites a student who
  chose to write. The statement check accepts "x". The anchor can be starred after Walk has named the first-seen
  work, so it is never a prediction (the notes' key skill "Predict what a visitor notices first" has no predict step).
- How seen: t1.js `cheap` = all nine `true`; `untouchedLabels: true`; `stX: true`. The checklist and allTicked line
  are honest that meaning is not checked, which keeps this from being a blocker.
- Better: Labels needs at least one written note per work (the brief can still allow short ones); the statement
  needs a minimum (for example 2 sentences or 20 words) before Format can tick; lock the star once Walk has been
  entered with a hung show, or record "starred before the walk" vs "after" in the Anchor line so the prediction is
  visible.

##### 4. The 145 cm default center line has no source, and the cited source says something different (should fix, general)
- Where: `fresh()` src.html:632 (`lines` default 145), shown on every wall ("145 cm · 57.1 in"), Line check
  (src.html:796) and its Why.
- What: STANDARDS "Facts": every number on screen has a source in the spec. The spec gives only the slider range
  (120 to 170); 145 cm appears nowhere in Sources. The one cited source, Smithsonian section II.A, says "Mount small
  items (to center line) at no higher than 1015 mm (40 in.)", and most of Jordan's works are small. The Line check
  then passes at any height (all walls at 120 cm pass, t1.js `lineAt120: true`), so the slider teaches only "make the
  walls match", not where a center line belongs for seated and standing visitors, which is the Pr5.1.IIa idea
  ("methods ... appropriate to display artwork in a specific place").
- How seen: t1.js; Smithsonian PDF text (section II.A, and section III wall labels).
- Better: source the default (the common 57 to 60 in / 145 to 152 cm gallery practice needs a named source in the
  spec), say in the Line Why that it is a standing-eye practice and that the guide sets small items lower for seated
  visitors, and let the seated band matter: a short note when a wall's line leaves every frame above the band.

##### 5. Seated eye level is a wheelchair-user average, shown as all seated visitors (nit, general)
- Where: Hang panel muted line ("Faint wall band: seated eye level, 109 to 130 cm"), spec Rules.
- What: the guide gives 1090 to 1295 mm (43 to 51 in) as the average eye level of "A male adult who uses a
  wheelchair". The tool's numbers match (130 is 129.5 rounded); notes "Teaching with care" already says it is a design
  reference. On screen, "wheelchair user's eye level" would be more exact.

#### Done when (spec), tested

| # | Result | How |
|---|---|---|
| 1 | Pass. Counts home 6, water 5, city 5, growing 4, night 2. Hint shows the themeShort text for growing and night only. Voice log shows growing as `themeShort` (silent, "early", n 2); the night line did not get its own log entry, so whether night is ever heard is a lead for Craft | t1.js `tags`, t2.js |
| 2 | Not mine (Play/Craft); place() pushes frames apart and keeps them off corners in my runs | t1.js |
| 3 | Pass on three layouts: back wall full (creek, centered), back wall empty (tomatoes, the side-wall frame nearest the back corner), anchor on a side wall only wins once the back wall is empty or its works sit at the corners, as the spec rule implies | t1.js `fs*` |
| 4 | Pass: spacing 14.29% pass, 16.54% fail, 29 cm gaps fail; 25-word note pass, 26 fail; 100-word statement pass, 101 fail; 26-word sentence fail; blank title fails | t1.js |
| 5 | Pass: tray order, label large and readable at the stop, word count and 137 cm shown | `f/walk-stop3.png` |
| 6 | Timing readout 3 s per stop (7 stops, 21 s), matches the 24 s for 8 | `f/walk-stop3.png` |
| 7 to 12 | Play/Craft; not re-checked | |

#### Facts spot-checked against a second source

Smithsonian PDF (extracted text): labels 1220 to 1675 mm / 48 to 67 in, centerline 1370 mm / 54 in, seated
1090 to 1295 mm / 43 to 51 in, sentences no more than 25 words, labels 75 to 100 words: all match screen and notes
(notes correctly explain 168 cm is 66.1 in). Room arithmetic (340 cm each side of the door), frame size +16 cm,
spacing percentages, tag counts and the 3 s per stop all recomputed and correct. NCAS anchor wording for 4, 5, 6
matches the spec's glosses; the HS performance standards are what finding 1 and 2 are judged against.

#### Grade fit, notes and guardrails

Language is right for 9-12. "Support at home" ideas are doable tonight. "Talk about it" questions are good and
tool-specific. "Teaching with care" names the personal side of Where I'm From and that nobody needs to upload
family photos (rule 8 met). No points, timers or hard history.

**For the sensitivity agent:** nothing cultural, Native or hard-history. Where I'm From invites personal and family
stories (handled in notes); no review needed in my view, flagged only so the integrator can decide.

#### Audit pilot

- Confirmed: Checklist "choices cut short by a scroll panel" at 1366x768: only Selection, Theme, Anchor and half of
  Line show; five of nine checks and their Show me buttons are below the fold of an inner scroll panel
  (`audit-r1/state-mode-04checklist-1366x768.png`). For teaching this matters: the student reads a third of the
  juror's list. (Play/Craft own the fix.)
- Not checked by me: the label-open / statement-open / clear-confirm "#hint covered" rows (a modal over the footer is
  expected) and the `#add-work` "welcome not heard" row (Play/Craft).
- Missed by the audit (it cannot see these): the cheap all-ticks path (finding 3), the tag giveaway in Select
  (finding 2), the unsourced 145 cm default (finding 4), Pr6 coverage (finding 1). Also seen on my own frame: in Walk
  the large visitor-label inset sits over the right half of the wall label it is quoting (`f/walk-stop3.png`), a Play
  item.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: virtual-gallery (Codex fix, round 3 narrow follow-up)

Active list: refine.md's updated first-line verdict and Exit check round 2. The prior completed reports remain polish-1.md and polish-2.md. Evidence root for this pass: `_scratch/virtual-gallery/round3/`.

#### Blocker

1. **FIXED, prior closure retained.** The cold round 2 exit check confirms every door layout, including legal far-left frames and the door-only null result. This pass changes no camera, ranking, art, cone or frame styling. Default/mode and legal-left-corner regression frames recheck the retained presentation.

#### Should fix

1. **FIXED, prior closure retained.** Door cutaway and its real placement data are untouched.
2. **FIXED, prior closure retained.** Two-column checklist and compact scrolling allowance are unchanged.
3. **FIXED, prior closure retained.** Seven portrait replacements and Kitchen Window crop are unchanged.
4. **FIXED, prior closure retained.** Card dimensions and highlighted theme tags are unchanged.
5. **FIXED, prior closure retained.** Label details stays below the stage; readable stop label placement is unchanged.
6. **FIXED, prior closure retained.** Persistent squeezed-label visibility is unchanged.
7. **FIXED, prior closure retained.** Readable labels, including squeezed-corner stop labels from round 2, are unchanged.
8. **FIXED.** Reproduced Selection, Theme and Labels Show me on an empty show with real 0.12-second held clicks at 1366x768 and 680x425. All six before measurements record focus BODY; Labels names the absent Label control. Added one early empty-show guard in showProblem(), before per-work selection or target lookup. Every empty non-Statement request now enters Hang, retains L.emptyHang and focuses the enabled Select mode button with preventScroll. Statement and chosen-work paths bypass this guard. Six inspected after frames in after/ repeat the exact before clicks and sizes. Every after JSON records focus m-select and the exact emptyHang hint; all before JSONs recorded BODY. No phantom Label or wall picker is rendered. The final audit control table also records rebuilt, focus kept for Selection, Theme and Labels Show me, including its two Enter presses; the three dedicated states add no leads at either named size.
9. **FIXED, prior closure retained.** Jump narration timing and immediate transport code are unchanged.
10. **FIXED, prior closure retained.** Shared live region and rounded drag-message filtering are unchanged.
11. **FIXED, prior closure retained.** Missing-note warning and settled format-only checks are unchanged.
12. **FIXED, prior closure retained.** Standing start and seated-viewer guidance are unchanged; no fact or number was added.

#### Polish accepted

1. **FIXED, prior closure retained.** Cone and outline geometry unchanged.
2. **FIXED, prior closure retained.** Compact overlays unchanged.
3. **FIXED, prior closure retained.** Neighbor label text blanking unchanged.
4. **FIXED, prior closure retained.** Route naming and tray order unchanged.
5. **FIXED, prior closure retained.** End recap and null guard unchanged.
6. **FIXED, prior closure retained.** Anchor explanation unchanged for shows with works; empty Anchor gets the same truthful empty guidance as before.
7. **FIXED, prior closure retained.** selectMore retains its star instruction.
8. **FIXED, prior closure retained.** Strip numbering and stars unchanged.
9. **FIXED, prior closure retained.** Wheelchair eye-level wording unchanged.
10. **FIXED, prior closure retained.** Title punctuation helper unchanged.
11. **FIXED, prior closure retained.** Word-boundary wrapping unchanged.
12. **FIXED, prior closure retained.** Flow wording unchanged.
13. **FIXED, prior closure retained.** Short wall choices, complete tray captions and accessible full wall names unchanged.
14. **FIXED, prior closure retained.** Slider valuetext and print pattern id unchanged.
15. **FIXED, prior closure retained.** Compressed image assets unchanged.

#### Settled calls

Applied unchanged: visible tags, blank-note warning rather than a new writing gate, existing allTicked and welcomeWalk lines, walk timing, straight-ahead camera, Show me on every row, keyboard placement, Motion off, themeShort and privacy. No spec open question was implemented. Unattended choice follows the exit check's narrow direction: direct every empty non-Statement request to the existing Select control. No shared file, refine.md or refine/ edit, and no git commit.

#### Cheats tried

All nine empty-show Show me buttons were swept with real held clicks, returning to Checklist between each: zero chosen works and zero passing checks afterward (empty-showme-sweep.json). No title, note, statement or placement was synthesized. Two further paths were tried at both 1366 and 680: empty Statement stays focused on its enabled editor button and still fails its unwritten check; selecting a work with a 26-word note and tapping Labels Show me focuses the real editor and still fails Labels. The settled copy-First-seen, blank-note warning and meaning-check limitations remain unchanged.

#### Voice walk

Held clicks at 0.12 seconds with 2-second gaps: empty-welcome.json records emptyHang spoken once, whole, at the empty Show me destination. voice-empty.json records the same line and Read repeating that exact hint; the Read press intentionally interrupts the automatic welcome. Normal main path: welcomeSelect, welcomeHang, lightHow, welcomeWalk, firstSeen in order (voice-main.json); the early Select welcome and lightHow are cut by later student actions, and the queued selectMore becomes stale on Hang, as the settled baseline permits. No line falsely names Label in empty Hang. All 37 allLines() strings equal voice/lines.json; no narration text was changed.

#### Engine changes wanted

None. The fix is local to showProblem().

#### Audit

Completed exactly once in 1961.08 seconds (32 minutes 41 seconds), exit 0, within the 2400-second outer limit. Chrome port 9911, host port 8715, profile round3/chrome-prof-fix. Full report: `fix-audit/audit.md`. All 106 audit PNGs were inspected in `audit-contact/`.

Eight initial sizes are clean, including the phone iframe. The three added empty Show me states have no leads at 1366x768 or 680x425. In the full Checklist control table, Selection, Theme and Labels Show me now all say rebuilt, focus kept; the later Enter presses are also clean. The former three real focus losses are gone. Motion off, ten five-held-click checks, ten two-quick-tap checks and mid-action resize recovery are clean. No runtime exceptions or controls left disabled. The focused offline probe recorded zero HTTP resources and all 37 voice declarations match allLines().

The remaining 22 leads are the settled cases below. Counts cover every saved row:

- **4 compact checklist scroll rows:** Checklist and Clear confirm at 680x425 and 375x812. Flow is under the fold in the preview; Statement and Flow are below it in the empty phone checklist. The exit check accepts most rows fitting compact sizes. No claim of nine initially visible on a phone.
- **3 covered-hint rows:** Label, Statement and Clear dialogs intentionally put the inactive footer behind their native modal backdrops. Preserved as the settled calls require.
- **6 miniature-text rows:** intro panel and its title, plus two cutaway wall-label cards and their titles, measured at 3 to 8 local CSS pixels. These are the scaled Hang rendering already settled by the exit check; editors and print retain the full text, and Walk's readable labels remain separate.
- **4 order-title clipping rows:** side-first-seen, legal-left-corner, all-door-wall and legal-left-corner-stop at 1366x768. Intentional two-line ellipses; whole titles remain in the parent buttons' accessible names and current readable labels. No mid-word wrap regression.
- **4 off-fold portfolio focus probes:** Wave Bowl, Fire Escape Garden, Rain on the Window and Map of My Block were clicked at unscrolled off-fold centers. These are the settled audit probes, not the three empty Show me failures repaired here.
- **1 first-Add welcome row:** Add to show replaces the welcome with selectMore, whose star instruction is retained. Accepted by polish 7 and baseline rule 16.

No new actionable lead remains from this audit. No second audit, post-audit code repair or post-audit browser run was started.


#### Left open

No reopened blocker or should-fix remains in this narrow follow-up. The spec open questions and settled meaning-check limitations remain unchanged. All 31 focused PNGs were inspected: before, after, checks, voice and regression folders. Default and every mode were re-shot at 1366x768; the legal left corner remains painted. Keyboard recovery at 680x425 moves to Select on Enter with focus retained. Bundle: 1,120,376 bytes; no focused console errors, zero HTTP resources in the offline probe, maximum source line 160 characters, no em dashes. Every command in this follow-up used a process deadline.

All task Chrome and host ports were verified closed. host.html is absent. No second audit or post-audit browser run was started.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Virtual Gallery build handoff

#### Claude Refine fixes, 2026-11-05

This section supersedes the historical camera, landscape-art and compact-label descriptions below. The active list
is refine.md, unchanged. The scoped result and evidence map are in polish.md after the final audit.

The door camera stays straight ahead and adjusts its focal length to include a back- or side-wall first-seen frame's edges.
That frame has a double outline. The floor cone projects from the doorway toward those edges. Hang keeps the main
three-wall room and unfolds the inward-facing door wall below it, with the door gap and both sets of pictures.
The unfolded surfaces use the same placement data and collision solver. Pointer coordinates on them are mapped
back into physical centimeters, so moving a picture there remains an actual hang operation.

Walk's large duplicate label is a disclosure below the room. The current wall label is drawn at readable screen
resolution at every width. Neighboring label cards keep blank paper rather than enlarged 3 px text. Squeezed cards
carry a persistent data-squeezed flag through camera redraws and travel. A jump stop awaits the voice promise as well
as the usual two seconds, while Stop, Step, Back, strip taps and Route retain their immediate interruption behavior.

The checklist uses two columns with Why and Show me side by side. Why opens the same explanation in a dialog.
Blank, whitespace-only or punctuation-only notes keep a visible missing-note warning. Blank notes still meet the
specified format check. One-word statements, matching tags and starring the named first-seen work remain possible
mechanical passes by the settled calls; meaning and prediction are not graded. Do not silently add new writing
requirements or a locked star. The 145 cm default is explicitly the tool's standing-viewer starting height, not
Smithsonian guidance. The guide's lower small-item recommendation is explained in Line Why and notes.md.

Seven landscape works were redrawn with built-in OpenAI imagegen at 3:4 portrait and processed using art.py --rekey.
They are 600 by 800 pixels and each is under 50,000 bytes. Kitchen Window has a clean right window jamb.
Map of My Block and Fire Escape Garden were also compressed below 50,000 bytes and inspected at card and detail size.
No people, lettering, new topics, shared-engine changes or git commits were added. Spec open questions stay open.

##### Round 2 first-seen repair, 2026-11-06

The exit check explicitly resolves the earlier door-wall question: inward-facing door-wall works are behind a
visitor looking straight ahead, so firstSeen() excludes them. With no back- or side-wall work, it returns null,
Anchor fails, and Walk says no work is in view from the door. The visitor may still walk to every hung work.
The end comparison also requires a real first-seen id before claiming it matched the star.

The legal Kitchen Window left corner, placed through place() at x=577 cm, reproduced the missing picture despite
its visible DOM box. The left wall's flattened compositing surface clipped its far-end children in Chrome.
Only the Walk left wall now preserves its 3D children. A controlled preserve-3d probe paints the frame; removing
the child transform, allowing backfaces, and promoting only the frame do not. Do not apply preserve-3d to every
wall: that introduces a texture seam on the back wall. Keep Hang's existing flat wall surfaces.

Compact wall choices read Back, Right, Door R, Door L, Left. The selected wall's full name is in its accessible
label and its full name and dimensions remain in the title. This fits the 63 px preview selector without
changing its 44 px target. Legal-left-corner and all-door-wall fixtures are in audit-states.json.

The corner stop also exposed that drawWalkArt() skipped its readable label when the physical card was squeezed.
The readable overlay now uses the work's projected label-height center and available screen space independently
of the physical card width. The physical squeezed card still stays hidden during travel and at a stop.

Round 2 evidence and the report draft are in _scratch/virtual-gallery/round2/. The final polish.md distinguishes
new before/after repairs from the twelve should-fix items already closed by the cold exit check.

##### Round 3 empty Show me repair, 2026-11-07

The updated refine verdict leaves only the empty Checklist Show me cases from should-fix 8. The three paths
reproduced at both 1366x768 and 680x425: Selection, Theme and Labels lost focus to BODY, and Labels referred to
a Label control which empty Hang does not render.

showProblem() now checks an empty chosen list before choosing any work or per-work target. Every empty request
except Statement enters Hang, retains L.emptyHang and focuses m-select with preventScroll. Statement keeps its
existing enabled editor button, and a selected-work request bypasses this guard. No score, label-writing rule,
voice string, camera, art, room geometry or timing changed. The six matching after frames and focus/hint numbers
are in _scratch/virtual-gallery/round3/after/ and its sibling JSON files. Three dedicated audit states exercise
Selection, Theme and Labels with real clicks at both named sizes. See the new polish.md for the final checks.

#### Cold review, 2026-11-04

The build notes below are historical. The compact scrolling limitation is repaired: all workbench controls retain 44 px targets and fit at every required size, including the desktop Plan supplement. Panel controls precede the tray in keyboard order.

The review preserves the room and portfolio. Seed Packets, Map of My Block and Fire Escape Garden were redrawn with built-in OpenAI imagegen and processed with art.py --rekey. All assets explicitly mark people false. Paintings keep their native aspect within physical frames; dense map/photo replacements exceed the old individual 50 KB target while the whole bundle remains about 1.1 MB.

Checklist claims are limited to measured conditions. Punctuation-only titles/statements fail; length and shared-tag checks remain mechanical. Notes explain the need for human interpretation, and allow fictional home settings. Do not add an arbitrary word minimum or treat nine ticks as an artistic grade.

Other repairs synchronize every gap readout, reject cramped Auto space with corrective feedback, show room gap rulers while dragging, constrain label paper to available frame gaps, preserve between-stop camera state without a stale label, expire obsolete jump speech, bound long text, repair empty diagnostics, and re-arm readiness events. Modal how lines and generic own-work/theme events are in voice/lines.json. The upper metric label range converts to about 66 inches; the Smithsonian guide prints 67, an inconsistency now identified in notes.

Independent evidence is under S:/CurioClass-codex/_scratch/virtual-gallery/: cold/, checks/, student-review/, side/, final-checks/, last/, pre-audit/ and scope-recheck/. Functional checks passed 39/39; imports passed 6/6; actual keyboard deltas were +5/-25 cm, Delete and Enter; the eight-work Motion-off walk took 24.158 seconds. Main-path and side-path voice logs are saved. The one final audit under review-audit/ was interrupted by the session restart after the size/state/Motion-off stages. Its 17 grouped leads concern the specified scrolling checklist and inert modal backgrounds. All 89 frames were inspected; full automated resize/control-walk coverage is incomplete and is not claimed as passing. Focused post-audit re-checks and the disposition are recorded in codex-review.md.

Final state guidance also keeps Hang on a chosen work after removal, directs an unhung selection to hanging, and lets empty-phone text span the strip. Checkmarks now say Meets check, with an explicit limit to measured conditions.

Fresh restarted checks passed the corrected state guidance, all 36 declared narration lines, an actual slider sweep, and a Motion-on mid-walk resize from 1366 to 760 and back. All task Chrome/server sessions are closed; host.html is removed.

No shared engine, scripts or documentation changes. No git commits. The requested review report is the final write and stop point.

#### Structure

src.html begins with the shared kit and grade 9-12 theme, followed by gallery-specific responsive styles. The script contains the exact portfolio, physical room geometry, persistence, voice table, nine independent checks, four views, camera projection, pointer and keyboard input, and editors. Images use art tokens. window.__tool exposes state, geometry, checks, voice log and actions for independent review.

#### Important implementation choices

- The show starts in Select when empty, and Hang after restoring a chosen work. Adding a work keeps Select open so comparison remains easy.
- Hanging is possible by pointer or by selecting a tray work, choosing a wall, and activating Hang on wall. Arrow keys use centimeters and the same collision solver as dragging.
- The camera uses a look-at matrix applied to a CSS 3D room. The first-seen calculation uses physical frame edges and does not infer attention from camera pixels.
- First-seen includes vertical distance to the 160 cm eye line. A low small frame does not receive a zero angle merely because it is centered horizontally.
- Each wall is a flat local compositing plane in the 3D world. This avoids Chrome software-compositor gaps at corners with unlit work. High-resolution artwork and wall-label overlays preserve detail at walk stops.
- Front-wall segments are separate 340 cm surfaces with a 120 cm door opening. The bowl has a 30 cm shelf rather than a mat and frame.
- Plan supplements the room in the desktop panel. A short preview and a phone use the plan as the main Hang view automatically. The full visitor view remains available on the phone.
- A work starts unlit to make the lighting decision visible. The spotlight appears as soon as Light is used.
- First-seen uses the frame area to break angular ties. Shared-tag jumps refer to hung works in tray order.
- Selection does not silently add a statement, star, lights, or tags to imported work.
- Saved shows may contain imported-work references, but no imported image pixels. Restore drops those references and shows the specified message.
- Imported work is not attributed to Jordan Reyes. Its artist name is left blank, including on the room label and the large visitor label.

#### Open questions and spec corrections

The spec contains no explicit open-question list. The following ambiguities were resolved using its stated direction:

- Default mode after a choice: keep Select while actively comparing; restored nonempty shows open in Hang.
- Counterclockwise changes the route direction from the door; the required stops remain in tray order, as the spec explicitly states.
- Spec arithmetic says eight widest framed works need 745 cm. The listed widths, plus 16 cm framing and seven 30 cm gaps, total 685 cm. The actual dimensions are used. spec.md is unchanged.
- Supplied portfolio images include several landscape assets despite the revised spec asking for portrait assets. Existing art is retained at its native aspect in the portfolio and displayed in the specified physical frame sizes. This preserves supplied work rather than inventing a replacement portfolio.
- Imported pictures use a nominal 40 cm long print edge, proportional dimensions, and student-set tags. The size is labeled Preview print. No dimension editor was added because the spec does not request one.
- The bowl's shelf is 30 cm wide; its drawing uses a 22 cm vertical envelope. Only its 18 cm diameter is given in the spec, so this height is a rendering setting, not an additional supplied measurement.

#### Compact layout limitation

At 680x425 and 375 wide, the tray, main view, selection, lighting, label editor, wall picker, Hang on wall, Auto space, Statement and Walk remain accessible in the initial viewport. Secondary height/order/remove controls require scrolling the workbench. This does not meet the strict reading of Done when 10; the report marks it FAIL instead of claiming every tool is simultaneously visible.

Gap numbers are shown in the room status, workbench and drag hint. They are not drawn as dimension rulers between frames on the wall. The plan connects the work stops in tray order; the camera uses a directional aisle route between stops so Counterclockwise can change travel without reversing the required tray order.

#### Build verification

Thirty browser functional assertions passed, including all nine checks on passing and failing cases and a vertical-angle first-seen case. A complete keyboard-only six-work student run reached nine of nine ready checks and produced the printed exhibition sheet with no exceptions. The five-hang held-click voice run logged welcomeHang, lightHow and hangMore once each. The eight-work Motion-off walk measured 24.14 seconds. See Scratch artifacts listed in the report for results and reviewed frames.

#### Mechanical audit and final repairs

The single full audit completed in 1,646 seconds and reported 122 leads. Its Motion off, resize recovery, held-click runtime errors and five-click repetition sections were clean. All 81 audit frames were reviewed in nine contact sheets, with the main sizes and modes also inspected independently at full size.

Final repairs set header targets to at least 44 px, name both textareas explicitly, reserve the compact workbench footer, reduce short-editor height, fix the singular stop count, and make taps on the current mode leave its narration running. Decorative scaled room lettering is hidden from assistive technology; the tray, editors, workbench readouts and large visitor label provide the corresponding accessible information. Small viewer layouts use the large label without an overlapping miniature replica.

Eleven targeted final cases passed, including actual growing/night narration, a same-mode welcome with no cut, a scrolled lower-card pointer click with focus retained, imported work with no false artist attribution, a Motion-off cut at the correct time, visible compact editor Done buttons, automatic phone plan, and visible primary phone controls. The desktop plan supplement was re-shot after its viewport and ink contrast repairs. No full audit was repeated after these changes; audit/audit.md is the earlier snapshot and codex-report.md gives the final dispositions.

The bowl was also checked in Hang and Walk after seating its 18 cm image on the 30 cm shelf; the enlarged view has no transparent frame border consuming its width.

Final bundle: 956,507 bytes. Sixteen WebP assets total 567,480 bytes. Source has 1,848 lines with a maximum line length of 160. All test Chrome instances and servers are closed, and host.html is removed. Repository changes are confined to tools/virtual-gallery/. No git commit or polish round was made.

#### Art

Fourteen portfolio images were already present. Missing warm plaster and oak floor textures are generated during this build with the imagegen skill and converted through scripts/art.py --rekey. A monochrome charcoal tomato drawing replaces the supplied red-colored rendering to match the stated medium. Full prompts and provenance are in art/prompts.json.

#### Engine changes wanted

None. No kit, scripts, documentation or other tools were edited.

#### Review next

Read codex-report.md for measured results and any incomplete requirements. This is Build only, with no git commit or polish round. The report distinguishes verified checks from limitations.

A final whole-pixel, jittered pointer drag on the desktop plan moved Map of My Block from 400 cm to 531.41 cm on the back wall. The room and plan updated together with no console errors. Evidence: Scratch plan-drag-result.json and plan-drag-frames/plan-drag-final.png.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
- 2026-11-25: earlier round polish-1.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/virtual-gallery
- 2026-11-25: earlier round polish-2.md moved to S:/CurioClass-archive/tool-rounds-2026-11-25/virtual-gallery
