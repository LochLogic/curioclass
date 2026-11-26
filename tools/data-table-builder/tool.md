# Data Table Builder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: data-table-builder

#### Built

- Build only in S:\CurioClass-codex. Product files are in tools/data-table-builder; work files and evidence are in _scratch/data-table-builder.
- Two independent mode states, a 24-row practice table, typed column design, 40-row collection, three chart views, grouping, sorting, editing, questions and local saving.
- The shared data-desk engine supplies DataTable, renderTable, Chart and statistics. Tool-local adapters supply categorical dot plots, typed controls, dense-stack fitting and chart decoration. Shared files were not edited.
- tool.draft.json has stage built. No commits, branch operations, deployment or polish round. The report is written last to honor the user's report-and-stop instruction.
- Final bundle: 184.7 KB. Source and bundle hashes, checks and artifact paths are in _scratch/data-table-builder/validation-manifest.json.
- The main functional run preceded some scoped repairs; changed paths were checked with focused scenarios instead of repeating the full run.

#### Numbers check

- Recomputed before the main implementation with _scratch/data-table-builder/prepare.py; output: numbers.json. No numerical disagreements with the spec.
- Fruit, in chart choice order: Apple 8, Banana 4, Grapes 4, Orange 2, Strawberry 6; 24 records.
- Teeth: 4:1, 5:1, 6:2, 7:3, 8:7, 9:5, 10:3, 11:1, 12:1. Most often 8; range 4 to 12; Sorted list total 196.
- Whistle: Yes 16, No 8; 16 is twice 8. Travel: Car 9, Bus 8, Walk 5, Bike 2.
- Pockets: 0:2, 1:4, 2:9, 3:5, 4:2, 5:1, 6:1; total 56.
- Whistle by travel, yes/no: Car 7/2, Bus 5/3, Walk 2/3, Bike 2/0.
- WCAG ratios: ink/paper 10.95, ink/panel 9.24, muted/panel 6.05, brand/paper 8.94, brand/panel 7.54, brand-ink/brand 12.63, focus/paper 7.51.
- Series/paper ratios: 7.61, 7.10, 9.61, 6.80, 7.56, 9.77. Patterns and shapes supplement color.

#### Facts checked

- The 20 baby teeth and approximately ages 6 to 12 shedding statement: [American Dental Association, Eruption Charts](https://www.mouthhealthy.org/all-topics-a-z/eruption-charts). Checked the page and its primary-tooth PDF on 2026-11-05.
- The PDF gives shedding ages 6-7 through 10-12 across the primary teeth. The fact is general information, not a health assessment of the class.
- Rows as student records, columns as questions/fields and grouping/counting: [CSTA Data and Analysis](https://csteachers.org/k12standards/) and the supplied spec. The current CSTA page identifies the 2026 standards.
- Bar-graph and line-plot teacher links: [Common Core Mathematics](https://www.thecorestandards.org/Math/), 3.MD.B.3 and 4.MD.B.4. These whole-number dot plots are a bridge, not a claim to teach fraction line plots in full.
- Every Room 4 answer, axis count, total, mode and range comes from the supplied fictional records and engine computations, independently checked above. Room 4 is labeled made up.
- Ready-column choices and numeric limits are design rules from spec.md, not claims about a child's body or ability. Readouts never show averages.
- Device-only storage and no-name guidance match the implementation: only columns and row values/identifiers are saved under dtb-our-class; no requests send answers anywhere.

#### Break it

- Question matching: guessed first, deliberately selected the wrong column, then Show me. No match was awarded; the card explained that this chart counts something else. Correct column and split then worked.
- Prediction copying and cycling choices: predictions are ungraded. A revealed guess is locked. The check explicitly says Column matched; it never says the guess was right or that the student mastered the idea.
- Grouped card: checked the required split, self-split exclusion and exact Car/Bus cells. A different split cannot satisfy the fixed card.
- Row gate: tried no answers, one missing answer, 1.5 and 21 in Teeth lost. Done stayed disabled. Four complete rows updated the chart without a chart tap.
- Repeated identical rows are legal observations, not an achievement. There is no saved best, point total, timer, slider score or reward for making the data easy.
- Custom choices: Same/same was rejected as a duplicate; distinct choices saved. Typed choices prevent spelling variants in recorded answers.
- Free-text reflection cheat: x plus any column originally earned an unjustified matching claim. Fixed: own questions now say Column chosen, have no correctness tick and request an explanation. The neutral spoken line was tested. Editing the text or column clears its old result.
- Capacity: a seeded 40-row 0/100 case disabled Add my row, kept all dots inside the plot and counted 40 records. This was a capacity probe, not 40 manual student entries.
- Destructive gates: Cancel kept rows/columns, No kept the table, Yes cleared the key, removing a column removed its question, and canceled backfill left existing data untouched.
- Persistence: edited a value, reloaded, and recovered it. Found and fixed a validator that could discard the 29-character boat column name; its row and singular footer now survive reload.
- Evidence: tests/results.json has 36/36 passing checks. Twelve focused repair scenarios passed; repair-*.json preserves each result.

#### Voice walk

- Curio.voice owns the queue, once-only instructions, Read and sound behavior. The bank is knowing-guide, Sadaltager, status kept. Browser speech is used during Build; no recording service was called.
- Main path used held 120 ms presses at a 2-second gap, with default Sound on. Motion was the first tap, followed by a column, chart changes, a guess, Show me, question navigation and Our class collection.
- Actual starts, in order: w-sample, charts, card, Apple answer, w-ours, kinds, Row 1 added, entry, Row 2 added, Row 3 added, counted.
- charts, card and kinds each started once across repeated chart/card actions. Every row addition on that path started its confirmation. New row instructions now take priority when entry opens.
- Welcome and how-to cuts after their stated moment passes are deliberate. Re-selecting an active mode had incorrectly cut its welcome; the held double-tap repair test now records one uncut welcome.
- Side path: Sound off, column/chart changes, Read, another chart, Sound on. Read spoke the current hint while Sound was off; silent instructions were not consumed.
- Modal Read remained available and was tested with a held click. Tab includes the card plus Read, Sound and Motion.
- The own-question honesty repair adds one neutral fixed event beyond the spec's original list. All 56 lines match the final manifest; the new event started in its focused test.
- Evidence: voice-main.json, voice-side.json, voice-frames, repair-modal-read.json, repair-quick-mode.json and repair-own-question-honesty.json.

#### Feel check

- Best moment: a new row flashes above the chalk tray while its chart immediately gains a bar count or dot. The class's own choices become the picture.
- First flat moment: Sorted list initially appeared after an empty SVG. Fixed SVG display handling; the ordered rows and total now occupy the chart area directly.
- Second flat moment: entry felt like a form. Painted answers, a chart-area card and a two-column desktop layout made it more tactile. The shortest versions still require card scrolling; that remains a gap.
- The table-to-chart link is reinforced by a yellow column outline and bar/stack picking that highlights matching records. Later cards introduce numeric stacks, totals and grouping rather than another favorite-choice question.
- Opened both bar tools, bundled only to Scratch, and compared the laptop scene beside Beat Lab in bar-comparison.png. The board, chalk texture, patterns, painted categories, ambient glint and physical tray give this tool its own visual world.
- This remains an exploratory classroom instrument, with personally relevant data as its payoff. No extra game, topic or scoring system was added.

#### Done when

1. PASS: 24 rows, five columns and choice-ordered fruit counts; functional checks 1-2 and default frames.
2. PASS: 24 tooth dots, seven at 8, range 4-12 and the exact mode sentence; functional dot check and audit teeth-dots frames.
3. PASS: 56 pockets and required grouped whistle cells; functional card tests and comparison.png.
4. PASS: season and teeth columns, three rows enabling questions, fourth row updating the open chart; real-input functional run.
5. PASS: incomplete entries blocked, valid typed answers accepted and column removal deleting its card; functional row/removal checks.
6. PASS: local reload and confirmed clear, including removal of the stored key; persistence/clear checks.
7. PASS: once-only main instructions and row events in the held-click voice walk; five-tap audit checks clean. Done is described conditionally until all answers exist.
8. FAIL: some reachable states do not keep all frequent controls visible. Initial laptop/compact controls and grayscale distinctions pass, but scrolling longer question panels can move chart controls out of view. Add my row is visible initially and pinned on mobile. This is an unresolved layout gap.
9. PASS: Motion off removes growth and idle motion, preserves counts, and the audit found no endless animation.
10. PASS: compact Sample shows six complete rows; chart region 175.5 px versus table region 172.5 px. Entry cards stay inside the chart region and never cover table rows.
11. PASS: rapid chart/column inputs replace the drawing immediately. The audit's mid-action resize checks reported no exceptions or stuck controls.

#### Wave lessons

- Hint and voice: PASS after repairs. Hints change synchronously; once-only choices use V.heard. Modal Read, Sound off and held presses were exercised.
- Focus and layout: PASS for retained controls, no focus taken on load, sorted-table arrow navigation and card focus. Custom-field focus scrolls its own card, not the page.
- Sizes and targets: FAIL for complete choice visibility in the smallest layouts. Frequent controls retain 48 px targets; read-only Sample navigation now enters through the full table widget.
- No giveaways: PASS within the stated explorer scope. Fixed cards confirm field selection, predictions are ungraded, and own questions make no correctness claim.
- Honest numbers: PASS. Fictional source is labeled, values are counted exactly, and no averages or unsupported estimates are shown.
- Standards: PASS for the two CS module codes through typed collection, multiple representations and choosing a field to answer a question. Math links are explicitly limited in teacher notes.
- Motion off: PASS; no infinite animation in the audit.
- Short choice sets: FAIL at short preview heights. Questions, shelf cards and custom forms can need scrolling; editable rows and wide tables also scroll internally.
- Resize mid-animation: PASS; all audited states and changed controls completed without exceptions or remaining disabled controls.
- Late welcome: PASS for the required first-tap policy. Actions with their own line suppress the welcome; they do not defer it behind that line.
- Show unknown as unknown: PASS / not applicable. This is an open-data explorer, not a hidden-clue puzzle; no unknown condition is painted as known.
- One look, one meaning: PASS. Series keep consistent names, colors and shapes/patterns, with a grayscale frame inspected.
- Badge says what is true: PASS after the own-question fix. Known prompts can match a field; arbitrary text only records a chosen field.
- Hint changes back: PASS across modes, charts, entry, cancel, save, clear and question changes.
- No answer by copying words: PASS / not an assessment claim. Recognizing a named field is the taught selection action; no diagnosis or reasoning score is awarded for copying text.

#### Audit leads

- One full audit finished in about 24 minutes, within the 40-minute cap. It recorded 105 leads against its pre-repair snapshot. The full audit was not rerun.
- Every bullet lead is mapped in _scratch/data-table-builder/audit-triage.csv. First-tap and row-movement warnings are mapped there as grouped causes.
- Fixed: small read-only cell entry targets, mobile Add a column overlap and its resulting missing-state/focus leads, singular footer wording, explicit custom-name label and active-mode welcome cuts.
- Fixed: card focus visibility and over-broad inert background handling. The hint and header Read now remain available; modal controls still contain focus.
- Reviewed: the SVG container falsely registered its own visible axis labels as covered. Full-size frames show them clearly.
- Reviewed: compact header text is hidden at font-size zero while a 22 px icon and accessible name remain. The icons are not zero-size visible text.
- Expected: chart buttons, Next, fruit guesses and column selectors can suppress a first-tap welcome when they queue their own line, as STANDARDS explicitly requires.
- Expected: sorting moves data rows; mode changes move mode-specific controls. Sort headers are retained under the pointer.
- Driver limitation: the audit could not acquire its 375 px iframe context. Dedicated 375 px host frames, hit tests and entry probes passed without console errors.
- Left open: short question panels, wide header sets, short shelf/custom forms and secondary mobile controls need scrolling. These are real layout leads, not dismissed as a clean audit.
- Runtime, five-click narration, Motion off and resize stress checks were clean. Initial test-host favicon 404 was removed with a data favicon in the Scratch host wrapper.

#### Frames looked at

- 92 captured frames across bar-frames, first, tests, frames, focused, voice-frames, audit, repairs and finish. Each was inspected directly or on labeled contact sheets, with key problem frames opened at full size.
- The full STANDARDS size sweep ran once late. Subsequent shots covered only repairs and affected views. audit-frame-index.txt lists all 50 audit PNGs.
- Also inspected: all 13 final-size art assets on art-sheet.png, the bar comparison, the grayscale frame, the final preview SVG capture and the own-question record.

#### Art made

- 13 unique gpt-image illustrations, all people false: five fruits, four travel objects and four seasons. Original PNGs remain in art/raw; final keyed WebP files total 25.6 KB.
- Full prompts and provenance are in art/prompts.json. Every piece was inspected on the final dark board. No painted asset needed a redraw.
- Charts, table, chalk dust, tray, shapes, patterns and motion are code. preview.svg reuses five painted fruit icons beside its coded graph.
- Bundle 184.7 KB plus 0 KB recorded voice, against the 2 MB goal. No teaching image was dropped to save size.

#### Art still to paint

None. Thirteen of thirteen painted assets are present; zero people assets.

#### Engine changes wanted

No shared edits were made. See handoff.md for the exact DataTable, renderTable, drawDot and drawBar promotion candidates: kind/choices normalization, counts alias, categorical/grouped dots, fitted dense-stack radii and optional decorations. Count bars and sum already exist.

#### Left open

- Small-screen short-choice visibility and some secondary vertical-flow controls still need design review. This Build is not a clean layout or polish sign-off.
- Six visible rows are verified for the compact Sample and main laptop framing; other table/card layouts can show fewer rows until scrolled, especially editable rows.
- The full audit snapshot predates scoped fixes; current repair evidence and source hashes are preserved. Its 375 px context acquisition was unavailable, although separate real iframe checks passed.
- Sadaltager recordings were intentionally not generated during Build. Browser speech works; the recording manifest is complete.
- Closest legacy neighbor code-tracer had no handoff.md or refine.md to read. Its source and the two designated bar tools supplied the available finish references.
- Spec conflicts and choices are documented in handoff.md: keep the made-up sample, respect write boundaries instead of changing the engine, use the requested image tool, prioritize short landscape controls, and avoid grading free text without evidence.
- All owned Chrome processes and preview servers were closed; host.html was removed. Scoped process inspection found no remaining owned browsers, and final port probes passed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: data-table-builder
#### Played
- Grade 4, solo learner and projector lens. Strong board, useful row-to-chart link, weakest at cramped collection layouts.
- Before builder notes: explored columns, three chart kinds, six cards, wrong-field feedback, the shelf and two-column entry. Chrome disconnected twice during the four-row completion batch; that path was completed and checked after fixes.
- Opened the existing Beat Lab and Snowy Mail Route bundles. One review pass; later runs only checked fixes and required sizes/voice.
#### Findings fixed
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
#### Findings left
- Blocker / spec conflict, field check: enumerating columns eventually earns the prescribed matching tick without reasoning. The spec defines success by field and split alone; a justification or attempt-limit assessment would be a new feature. Retained the narrow honest label and flagged this rather than claiming the cheat was defeated.
- Should fix / spec conflict, compact/mobile: column headers and later phone questions still scroll. Five separate 48 px selection/sort pairs cannot fit the small stage; the specified phone table/chart/panel stack exceeds one screen. A new navigation layout needs a spec decision. This is not an all-sizes layout sign-off.
- Nit: a long choice word can wrap at a narrow panel width. Labels remain complete.
#### Break it
- Prediction copying: chart pixels, summaries and accessible chart content stay covered until a valid guess is committed to inspection. Then the original guess is locked, including wrong-field inspection.
- Field cycling: four wrong fields did not match; fruit did. The frozen guess remained Banana and no best score was saved. This confirms the unresolved spec conflict above; the prescribed check does not establish reasoning.
- Tried wrong guesses, all fields, wrong split, repeated Show me, changing a matched context, and an arbitrary own question. Own questions earn no correctness tick; editing clears their old result.
- Incomplete, blank, fractional, negative and out-of-range entries cannot add rows. Three identical valid observations are legal data, not an achievement.
- Duplicate choices, reversed bounds, six-choice/six-column/40-row limits: checked. A 0-to-100 case retains 101 count slots; all 40 dots count, and a single 40-dot stack fits.
- Cancel/No preserve data; confirmed row/column removal and Clear change it. Saving/reloading and live fourth-row updates were checked.
- No points, percent meter, timer or saved best exists. Evidence: review-final-gates.json, review-extremes-final.json, review-field-cycle.json and review-result-repeat.json in Scratch.
#### Voice walk
- Held 120 ms clicks, default Sound/Motion, 2 s pace. Followed the welcome: stage, column, prediction, column, chart choices, Show me; then all six cards and the grouped comparison.
- Actual starts: w-sample, card, charts, answers 1-5, split, answer 6. Each how-to starts once; every sample answer starts. Expected cuts follow the student's next action.
- Our class: welcome, two columns, three complete rows, column/chart exploration. Starts: w-ours, kinds, entry, Row 1, Row 2, Row 3, counted, charts.
- Counts: card/charts/split/kinds/entry/counted = one each on their path; sample answer events = six; row events = three. Five chart actions do not repeat their instruction.
- Sound-off Read and mode changes were checked. All 56 manifest lines match allLines; narration uses browser speech, with no recorded clips bundled.
- Final Read supplies the skipped/cut premise and current instruction together. Repeated Show me starts its result event on all five held clicks. Repair batches reported no console errors.
#### Facts checked
- All 24 source records match spec.md exactly. Independent computation: fruit Apple 8, Banana 4, Grapes 4, Orange 2, Strawberry 6; whistle Yes 16 / No 8; travel Car 9 / Bus 8 / Walk 5 / Bike 2.
- Teeth mode 8 (7 records), range 4-12, total 196; pockets total 56. Whistle by travel, yes/no: Car 7/2, Bus 5/3, Walk 2/3, Bike 2/0. Source: the fictional Room 4 table; review-numbers.json preserves every distribution.
- 20 primary teeth and shedding around ages 6-12: [ADA MouthHealthy Eruption Charts](https://www.mouthhealthy.org/all-topics-a-z/eruption-charts) and its [primary-tooth chart](https://www.mouthhealthy.org/-/media/project/ada-organization/ada/mouthhealthy/files/activity-sheets/adaprimarytoothdev_eng.pdf), checked 2026-11-08. No clinical judgment is made.
- Rows as records/columns as attributes: [CSTA E4-DAT-DC-09](https://csteachers.org/standard/organize-collected-data-into-a-table-using-a-computational-tool-with-rows-representing-records-and-columns-representing-attributes/). Collection, charts and communicating findings connect to [CSTA's 2017 1B-DA-06/07](https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf).
- Math connections checked against [Common Core 3.MD.B.3](https://www.thecorestandards.org/Math/Content/3/MD/) and [4.MD.B.4](https://www.thecorestandards.org/Math/Content/4/MD/). Notes correctly qualify whole-number plots as a bridge to fraction measurement plots.
- Numeric limits and capacities are spec design rules. Tie, mode, range, total and zero-slot readouts are computed from rows; no averages appear.
- Device-only saving matches source/storage checks; only columns and row values/IDs persist. No requests send class answers. Notes open with the required three sections.
#### Sensitivity
- Tooth loss concerns children's bodies: a sensitivity reviewer should check that developmental variation stays neutral and optional, without comparison or health inference. Jumping-jacks collection remains optional and has no ability score.
- No cultural, religious or hard-history claims; no people in the art. All 13 people:false declarations match the images.
#### Flattest moment left
- Entering a large class remains repetitive. Its payoff is the student's own updated table and chart; a game or new activity would exceed the spec.
#### Graphics
- Inspected all 13 final-size WebPs and their chart/choice placement. None needed replacement. Redrew the procedural board surface; kept the strong painted set, pattern/shape encoding and physical tray.
- Art 25.6 KB; final bundle 195.6 KB. review-comparison.png puts the revised board beside Beat Lab. Every required size, Motion off, grayscale and keyboard frames were inspected; 57 audit frames were reviewed on ten labeled contact sheets with confirmed leads opened separately.
- Primary contrasts: ink/paper 10.95, ink/panel 9.24, muted/panel 6.05, brand text 12.63, hover 14.12, focus 7.51. All six series contrasts match the spec.
#### Audit
- One audit completed in about 25 minutes, within the 40-minute cap. Its snapshot produced 94 lead instances: 48 addressed by the focused fixes, 27 expected icon/welcome/modal behaviors, and 19 instances of the open table/phone constraints. Every instance is mapped in review-audit-triage.csv.
- Repeat speech and resize stress completed without errors or stuck controls. Afterward, checked the affected sizes, mobile shelf/custom/entry hit targets, modal resizing, all keyboard sizes, Read's premise and repeated result speech. The audit was not rerun.
- Final behavioral evidence: 36 functional assertions and 13 boundary assertions passed. This does not override the open blocker or layout findings.
- One full size sweep, followed only by affected-size repair frames. The initial host-only favicon 404 was removed from the harness; subsequent focused batches had no console errors.
#### Left open
- Retained the made-up sample, original topics, ungraded prediction/field-matching semantics and local engine adapters. No new assessment, shared engine edit, audio recording or external service was added.
- The enumeration blocker needs a spec decision about what constitutes evidence of understanding. No ready verdict is claimed.
- CODEX-REVIEW.md section 3 says not to make a fix needing a new feature. Treating justification/attempt limits as a new assessment is this review's scope judgment, not an approval requirement.
- The physical compact/phone constraints above need a spec/layout decision. Multi-column entry still uses internal scrolling; six editable 48 px rows plus a larger chart cannot fit a 425 px height.
- Root verified S:\CurioClass-codex. Writes stayed in the tool and its Scratch folder; no git commits. Owned ports 9940, 9941 and 8745 are closed, and host.html is absent. Final hashes and check counts are in review-final-manifest.json.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Data Table Builder handoff

#### Build structure
src.html starts from the kit starter. CSS defines the chalkboard, responsive table/chart split and chart-area cards. The final script holds column definitions, Room 4, two independent mode states, family-engine adapters, question cards, row entry and local saving.
DataTable owns data changes; renderTable supplies semantic tables; Chart draws bars and dot facets. A local numeric encoding lets the current engine draw categorical dots. Decoration adds art, exact ticks, counts, patterns and motion.
No shared files were changed. No commits or polish round.

#### Open questions resolved
- Keep the fictional Room 4 dataset, explicitly labeled made up. The real data is the class's own collection.
- The brief's image tool overrides the spec's older local FLUX route. All 13 icons are gpt-image art, people false.
- STANDARDS takes precedence over the spec's stacking breakpoint in short landscape: keep stage and controls side by side at 680x425.
- Six rows with 48 px editable targets plus a larger chart do not fit a 425 px height. Compact sample text rows are used; editable rows retain their target height and scroll.
- The spec asks for shared engine modifications but the build boundary forbids them. Use the current engine and local adapters, with desired promotions below.
- Adding a column after rows exist is unspecified. Collect explicit values for each existing row before committing the column; Cancel is transactional.

#### Sensitivity
Teeth lost touches children's bodies. The displayed ADA fact is general; use the sample rather than asking students to compare development. No names or health judgments. The jumping-jacks column is optional. Offer an equally valued alternative; no race or achievement score is attached.
No cultural or religious content. No people in the image set.

#### Engine changes wanted
- kit/data-desk.js, DataTable: normalize kind and choices into existing type/values metadata and expose counts as an alias for count. Sum and count bars already exist.
- kit/data-desk.js, Chart drawDot: support list and yes/no x values with exact categorical ticks and groupBy facets. The tool currently encodes values locally.
- kit/data-desk.js, drawBar: optional count labels, filled patterns and axis artwork. Current tool decorates the engine's output.
- kit/data-desk.js, renderTable: header selection/sort actions, stable row identifiers, typed cell editors and preserving header nodes during sorting would avoid post-render decoration.
Do not promote this code into the kit before the repository's three-consumer rule is met.

#### Next review
The cold review's current evidence is in `_scratch/data-table-builder/review-*`.
`codex-report.md` describes the earlier Build snapshot and its gaps, rather than the repaired source.

#### Cold review changes
- Clear now forces a fresh mode render, replacing the live DataTable as well as state and storage.
- Sample questions cover counts and summaries until a valid guess is followed by a column, chart or split tap, or Show me. The guess locks at that first inspection, including a wrong-field attempt. Our class charts remain live during collection.
- A saved matching result only displays while the current field and split match that question. Arbitrary own questions still earn no correctness tick.
- Instructions stop when entry makes their controls unavailable. The existing 56-line voice manifest remains unchanged.
- The desktop Build controls use a chalkboard tool strip, preserving space for the question. Compact questions use one row of five labeled choices and replace those choices with the recorded guess after inspection.
- Compact shelves use the stage; entry stays in the chart area. Mobile table height now exposes actual rows while keeping chart controls in the initial viewport.
- Primary and pressed buttons keep dark text on light yellow during hover. Chalkboard grain uses subtle directional layers instead of concentric rings. All 13 painted icons are retained.
- Shelf and custom-column cards can use the available viewport. All six custom choices fit together. Mobile Build buttons share one bottom strip and hide while a card is open, so they cannot cover Save column or the shelf.
- Read includes the Room 4 premise if a first action skipped that welcome. Table arrow navigation enters through the visible scroll region rather than the clipped full-height table.
- Multiple-column entry at very short sizes still needs scrolling. Six editable 48 px rows plus a larger chart cannot fit a 425 px screen; changing that constraint needs a spec decision.

#### Cold review disposition
The single audit completed with 94 lead instances against its snapshot. Focused repairs then checked every affected size; the full audit was not repeated. See `codex-review.md` and `_scratch/data-table-builder/review-audit-triage.csv` for dispositions.
The prescribed field/split-only check can be found by enumerating columns. This is left as a blocker under the review's strict Break it rule: replacing it with a reasoning or attempt-limit assessment would add a feature beyond the spec. The label remains the narrow factual Column matched; it never grades the prediction.
The compact header/phone stack constraints remain should-fix spec/layout conflicts. This review does not claim a ready or all-sizes pass.

#### Build snapshot validation (before cold review)
The following records the earlier Build snapshot. The cold-review changes above supersede its repaired layout and behavior gaps.
The functional path passed 36 checks. Twelve focused scenarios passed after audit repairs; the final phone probe also confirmed no overlap between Add a column and the pinned row button.
The one full audit finished in about 24 minutes with 105 leads against its earlier snapshot. `_scratch/data-table-builder/audit-triage.csv` answers the leads by root cause. The full audit was not repeated after scoped repairs.
The 680x425 sample now shows six complete rows. Its chart region is 175.5 px tall versus 172.5 px for the table region. Editable 48 px rows still need scrolling there.
Small previews still require scrolling question choices, column headers and shelf/custom forms. This fails the standing short-choice visibility rule; it is not a clean layout sign-off.
The audit could not acquire its 375 px iframe context. Dedicated phone host frames and same-origin probes passed. Narration is browser speech during Build; all 56 fixed lines are in the Sadaltager manifest, but no audio was recorded.
Read, Motion and Sound remain available while entry cards are open. Tab cycles through the card and these header controls. Read-only Sample table navigation starts from the table widget, then arrow keys enter cells.
The current dot adapter also reduces dense-stack radii below the engine's 2.5 px minimum when necessary. Promote a fitted-radius option in drawDot if other finished tools need it.
Every owned Chrome and preview server was closed, including five host processes that the Windows taskkill calls had left running. host.html was removed. The final port probe passed.
The own-question card is deliberately ungraded. A nonsense prompt with any column must not earn a correctness check: it now says Column chosen, shows that column's data, and asks for an explanation. Its neutral event adds one fixed narration line beyond the spec's original list. Editing the question or changing its chosen column clears the old result.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
