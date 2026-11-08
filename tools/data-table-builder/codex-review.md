# Codex review: data-table-builder
## Played
- Grade 4, solo learner and projector lens. Strong board, useful row-to-chart link, weakest at cramped collection layouts.
- Before builder notes: explored columns, three chart kinds, six cards, wrong-field feedback, the shelf and two-column entry. Chrome disconnected twice during the four-row completion batch; that path was completed and checked after fixes.
- Opened the existing Beat Lab and Snowy Mail Route bundles. One review pass; later runs only checked fixes and required sizes/voice.
## Findings fixed
- Blocker, general, Clear: same-mode early return kept the old DataTable alive after erasing state/storage. Force a full rebuild; reload recovered four rows, then confirmed Clear removed all three copies.
- Blocker, family:data-desk, prediction: counts and exact answers were visible before guessing. Sample charts now wait for a valid prediction and inspection; that prediction locks when data appears. Our class charts remain live.
- Should fix, family:data-desk, results: the matching badge survived another selected field/split. Display it only for the matching current context.
- Should fix, general, layout: chart controls scrolled away and questions/choices were squeezed. Pin the instrument controls; move Build to a board tool strip; compact five-choice cards; replace locked options with the recorded guess.
- Should fix, general, narrow forms: shelf and custom controls were clipped. Use the available viewport, fit all six custom choices, and keep each entry choice set together.
- Should fix, general, mobile: the pinned row button covered Add a column and Save. Put all three Build buttons in one strip, hide it while a card is open, and expose actual table rows.
- Should fix, general, voice: lines described covered charts or unavailable entry controls. Gate chart/split instructions on the visible drawing, stop stale events, and keep the skipped/cut premise available through Read.
- Should fix, general, full-table hints: Add my row was named at the 40-row cap. Direct students to enabled editing/chart controls instead.
- Should fix, general, focus: the full-height table was the keyboard target. Enter cells through its visible scroll region; retain arrow navigation and prevent page jumps.
- Should fix, general, contrast: hovered yellow controls inherited a dark background with dark text. Keep the light surface; hover text contrast is 14.12:1.
- Polish, play: preserve the rewarding live chart after every collected row, including the third; no prediction cover over class collection.
- Polish, art: replace distracting concentric board rings with directional grain and light; retain the tray, painted icons, patterns and shapes.
## Findings left
- Blocker / spec conflict, field check: enumerating columns eventually earns the prescribed matching tick without reasoning. The spec defines success by field and split alone; a justification or attempt-limit assessment would be a new feature. Retained the narrow honest label and flagged this rather than claiming the cheat was defeated.
- Should fix / spec conflict, compact/mobile: column headers and later phone questions still scroll. Five separate 48 px selection/sort pairs cannot fit the small stage; the specified phone table/chart/panel stack exceeds one screen. A new navigation layout needs a spec decision. This is not an all-sizes layout sign-off.
- Nit: a long choice word can wrap at a narrow panel width. Labels remain complete.
## Break it
- Prediction copying: chart pixels, summaries and accessible chart content stay covered until a valid guess is committed to inspection. Then the original guess is locked, including wrong-field inspection.
- Field cycling: four wrong fields did not match; fruit did. The frozen guess remained Banana and no best score was saved. This confirms the unresolved spec conflict above; the prescribed check does not establish reasoning.
- Tried wrong guesses, all fields, wrong split, repeated Show me, changing a matched context, and an arbitrary own question. Own questions earn no correctness tick; editing clears their old result.
- Incomplete, blank, fractional, negative and out-of-range entries cannot add rows. Three identical valid observations are legal data, not an achievement.
- Duplicate choices, reversed bounds, six-choice/six-column/40-row limits: checked. A 0-to-100 case retains 101 count slots; all 40 dots count, and a single 40-dot stack fits.
- Cancel/No preserve data; confirmed row/column removal and Clear change it. Saving/reloading and live fourth-row updates were checked.
- No points, percent meter, timer or saved best exists. Evidence: review-final-gates.json, review-extremes-final.json, review-field-cycle.json and review-result-repeat.json in Scratch.
## Voice walk
- Held 120 ms clicks, default Sound/Motion, 2 s pace. Followed the welcome: stage, column, prediction, column, chart choices, Show me; then all six cards and the grouped comparison.
- Actual starts: w-sample, card, charts, answers 1-5, split, answer 6. Each how-to starts once; every sample answer starts. Expected cuts follow the student's next action.
- Our class: welcome, two columns, three complete rows, column/chart exploration. Starts: w-ours, kinds, entry, Row 1, Row 2, Row 3, counted, charts.
- Counts: card/charts/split/kinds/entry/counted = one each on their path; sample answer events = six; row events = three. Five chart actions do not repeat their instruction.
- Sound-off Read and mode changes were checked. All 56 manifest lines match allLines; narration uses browser speech, with no recorded clips bundled.
- Final Read supplies the skipped/cut premise and current instruction together. Repeated Show me starts its result event on all five held clicks. Repair batches reported no console errors.
## Facts checked
- All 24 source records match spec.md exactly. Independent computation: fruit Apple 8, Banana 4, Grapes 4, Orange 2, Strawberry 6; whistle Yes 16 / No 8; travel Car 9 / Bus 8 / Walk 5 / Bike 2.
- Teeth mode 8 (7 records), range 4-12, total 196; pockets total 56. Whistle by travel, yes/no: Car 7/2, Bus 5/3, Walk 2/3, Bike 2/0. Source: the fictional Room 4 table; review-numbers.json preserves every distribution.
- 20 primary teeth and shedding around ages 6-12: [ADA MouthHealthy Eruption Charts](https://www.mouthhealthy.org/all-topics-a-z/eruption-charts) and its [primary-tooth chart](https://www.mouthhealthy.org/-/media/project/ada-organization/ada/mouthhealthy/files/activity-sheets/adaprimarytoothdev_eng.pdf), checked 2026-11-08. No clinical judgment is made.
- Rows as records/columns as attributes: [CSTA E4-DAT-DC-09](https://csteachers.org/standard/organize-collected-data-into-a-table-using-a-computational-tool-with-rows-representing-records-and-columns-representing-attributes/). Collection, charts and communicating findings connect to [CSTA's 2017 1B-DA-06/07](https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf).
- Math connections checked against [Common Core 3.MD.B.3](https://www.thecorestandards.org/Math/Content/3/MD/) and [4.MD.B.4](https://www.thecorestandards.org/Math/Content/4/MD/). Notes correctly qualify whole-number plots as a bridge to fraction measurement plots.
- Numeric limits and capacities are spec design rules. Tie, mode, range, total and zero-slot readouts are computed from rows; no averages appear.
- Device-only saving matches source/storage checks; only columns and row values/IDs persist. No requests send class answers. Notes open with the required three sections.
## Sensitivity
- Tooth loss concerns children's bodies: a sensitivity reviewer should check that developmental variation stays neutral and optional, without comparison or health inference. Jumping-jacks collection remains optional and has no ability score.
- No cultural, religious or hard-history claims; no people in the art. All 13 people:false declarations match the images.
## Flattest moment left
- Entering a large class remains repetitive. Its payoff is the student's own updated table and chart; a game or new activity would exceed the spec.
## Graphics
- Inspected all 13 final-size WebPs and their chart/choice placement. None needed replacement. Redrew the procedural board surface; kept the strong painted set, pattern/shape encoding and physical tray.
- Art 25.6 KB; final bundle 195.6 KB. review-comparison.png puts the revised board beside Beat Lab. Every required size, Motion off, grayscale and keyboard frames were inspected; 57 audit frames were reviewed on ten labeled contact sheets with confirmed leads opened separately.
- Primary contrasts: ink/paper 10.95, ink/panel 9.24, muted/panel 6.05, brand text 12.63, hover 14.12, focus 7.51. All six series contrasts match the spec.
## Audit
- One audit completed in about 25 minutes, within the 40-minute cap. Its snapshot produced 94 lead instances: 48 addressed by the focused fixes, 27 expected icon/welcome/modal behaviors, and 19 instances of the open table/phone constraints. Every instance is mapped in review-audit-triage.csv.
- Repeat speech and resize stress completed without errors or stuck controls. Afterward, checked the affected sizes, mobile shelf/custom/entry hit targets, modal resizing, all keyboard sizes, Read's premise and repeated result speech. The audit was not rerun.
- Final behavioral evidence: 36 functional assertions and 13 boundary assertions passed. This does not override the open blocker or layout findings.
- One full size sweep, followed only by affected-size repair frames. The initial host-only favicon 404 was removed from the harness; subsequent focused batches had no console errors.
## Left open
- Retained the made-up sample, original topics, ungraded prediction/field-matching semantics and local engine adapters. No new assessment, shared engine edit, audio recording or external service was added.
- The enumeration blocker needs a spec decision about what constitutes evidence of understanding. No ready verdict is claimed.
- CODEX-REVIEW.md section 3 says not to make a fix needing a new feature. Treating justification/attempt limits as a new assessment is this review's scope judgment, not an approval requirement.
- The physical compact/phone constraints above need a spec/layout decision. Multi-column entry still uses internal scrolling; six editable 48 px rows plus a larger chart cannot fit a 425 px height.
- Root verified S:\CurioClass-codex. Writes stayed in the tool and its Scratch folder; no git commits. Owned ports 9940, 9941 and 8745 are closed, and host.html is absent. Final hashes and check counts are in review-final-manifest.json.
