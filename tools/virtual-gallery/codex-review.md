# Codex review: virtual-gallery

## Played

Cold grade 9-12 run before builder report/source: compared portfolio, selected home works, starred an anchor, dragged a frame, hung and lit others, auto spaced, entered Walk and Checklist.
An initial memory-registry search incidentally exposed an old build summary. Builder files stayed unopened until after play; every result reported here was independently exercised.
Strong: the textured room, mature gallery typography, varied portfolio media and precise tools. Cold evidence in cold/ and play-*.json.

## Findings fixed

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

## Findings left

All confirmed blocker and should-fix items repaired; original materials and portfolio strengths retained. The interrupted audit's missing coverage is named below.

## Break it

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

## Voice walk

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

## Facts checked

- Selection, refinement, conveying meaning: [NCAS anchors 4/5/6](https://www.nationalartsstandards.org/), practiced through choosing, hanging, sequencing and writing.
- Label center 137 cm, metric range 122 to 167.5 cm, seated eye range 109 to 129.5 cm, 25-word sentences and 75 to 100-word labels: [Smithsonian Guidelines, II/III](https://www.sifacilities.si.edu/sites/default/files/Files/Accessibility/accessible-exhibition-design1.pdf). Its official indexed passages were retrieved; direct PDF fetch timed out. Rounded ranges and the 67-inch source inconsistency are identified in notes.
- Portfolio selection and refinement: [College Board AP Art and Design](https://apcentral.collegeboard.org/courses/about-ap-art-and-design). The nine checks are this fictional brief's rubric, not AP scoring or legal requirements.
- Fictional artist, credits, media, dimensions, years and five tags: checked every portfolio row against spec Content. Counts independently recomputed: home 6, water 5, city 5, growing 4, night 2; actual theme speech exercised.
- Fictional room geometry and timing: (800 - 120)/2 = 340 cm; mats/frames add 16 cm; eight widest plus seven 30 cm gaps = 685 cm, correcting the spec's 745 cm. First seen independently compared with 2,001 edge samples in three layouts. Motion-off eight-stop run: 24.158 s.
- Rubric arithmetic and units: 40/40/46 cm gaps spread 14.2857%; 40/40/47 spread 16.5354%. 137 cm = 53.94 in; 168 cm = 66.14 in. Recomputed contrast ratios: brand/panel 11.52, brand/section 10.92, brand ink/brand 12.29, label ink/wall 12.49, ink/white 14.34; repaired Walk eyebrow/cream 6.25.

## Sensitivity

No named cultural tradition, Indigenous content, religion or hard history. A cultural reviewer should check that the fictional Reyes surname is not treated as a cultural proxy and that home/origin prompts allow invented settings without family disclosure. Notes now explicitly provide that choice. Seated eye height is a design reference, not one universal body or view.

## Flattest moment left

Lighting six works remains a repetitive workbench task. Per-work control is the spec's decision; a new bulk feature was not added. The generic walk ending was lifted with a specific recap.

## Graphics

All 16 finished images inspected, including room and card use. Three assets redrawn with built-in imagegen, copied into art/raw and converted with art.py --rekey; prompts and provenance saved. No people required or depicted; every asset explicitly marks people false.
Art: 720,234 bytes. Bundle 1,170,809 bytes (1143.4 KB), under 2 MB. Two dense replacements exceed the old 50 KB per-work target, preserving material detail. Several retained works are landscape despite the spec's blanket portrait instruction; they are preserved without distortion.
Compared with both existing bar tools without rebundling outside the allowed folder. review-bar-comparison.png places this gallery beside Beat Lab; the room retains its materials, light, depth and precise controls.

## Audit

Audit not finished: one run, with the required 40-minute cap, was interrupted by the session restart after Motion off. Its partial review-audit/audit.md and all 89 saved frames were reviewed. No second full audit was started.
All eight initial sizes, every mode, all seven listed populated/dialog states and Motion off completed. The partial report's resize/control-walk placeholders are not counted as passes. Independent held-click main/side walks, controls, keyboard, and a fresh 1366-to-760-to-1366 mid-walk resize passed without exceptions or disabled controls.
All 17 grouped leads are disposed: 14 repeated warnings concern the required scrolling diagnostic checklist, including its inert background behind Clear; these are not hidden answer choices. Three concern the deliberately covered background hint in Label, Statement and Clear dialogs, whose own instructions and controls remain visible.
Audit frames also prompted the empty-phone text correction; focused post-audit frames cover it, removed selections, chosen-but-unhung guidance, and measured-check wording at 680 and 375. No confirmed audit defect remains open. Full automated resize/control-walk coverage remains incomplete.
Wave checks: current hints and once-only how lines, retained focus and controls before tray, 44 px targets, explicit measurement assumptions, meaningful VA:Pr4/5/6 actions, no infinite Motion-off loops, resize recovery, truthful badges, restored hints, and no hidden-answer game. Frame folders and JSON logs are under _scratch/virtual-gallery/; all generated frames were opened directly or in contact sheets.

## Left open

Spec limit: a short statement and self-assigned tags can meet the numeric rubric without strong interpretation. Claims are explicitly limited to measured checks; adding a semantic gate would change the spec. No best score or artistic mastery claim remains.
Full automated resize/control-walk audit stages were interrupted; their coverage is not represented as complete.
Retained landscape source art and two assets over the individual 50 KB target are deliberate quality choices; the bundle stays well below 2 MB. Camera direction changes travel while retaining the required tray stop order.
Unattended choices follow the spec and baseline; no questions asked. No git commits or writes to shared engines/docs/scripts. All task Chrome/server sessions are closed and host.html is removed.
