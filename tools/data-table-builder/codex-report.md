# Codex report: data-table-builder

## Built

- Build only in S:\CurioClass-codex. Product files are in tools/data-table-builder; work files and evidence are in _scratch/data-table-builder.
- Two independent mode states, a 24-row practice table, typed column design, 40-row collection, three chart views, grouping, sorting, editing, questions and local saving.
- The shared data-desk engine supplies DataTable, renderTable, Chart and statistics. Tool-local adapters supply categorical dot plots, typed controls, dense-stack fitting and chart decoration. Shared files were not edited.
- tool.draft.json has stage built. No commits, branch operations, deployment or polish round. The report is written last to honor the user's report-and-stop instruction.
- Final bundle: 184.7 KB. Source and bundle hashes, checks and artifact paths are in _scratch/data-table-builder/validation-manifest.json.
- The main functional run preceded some scoped repairs; changed paths were checked with focused scenarios instead of repeating the full run.

## Numbers check

- Recomputed before the main implementation with _scratch/data-table-builder/prepare.py; output: numbers.json. No numerical disagreements with the spec.
- Fruit, in chart choice order: Apple 8, Banana 4, Grapes 4, Orange 2, Strawberry 6; 24 records.
- Teeth: 4:1, 5:1, 6:2, 7:3, 8:7, 9:5, 10:3, 11:1, 12:1. Most often 8; range 4 to 12; Sorted list total 196.
- Whistle: Yes 16, No 8; 16 is twice 8. Travel: Car 9, Bus 8, Walk 5, Bike 2.
- Pockets: 0:2, 1:4, 2:9, 3:5, 4:2, 5:1, 6:1; total 56.
- Whistle by travel, yes/no: Car 7/2, Bus 5/3, Walk 2/3, Bike 2/0.
- WCAG ratios: ink/paper 10.95, ink/panel 9.24, muted/panel 6.05, brand/paper 8.94, brand/panel 7.54, brand-ink/brand 12.63, focus/paper 7.51.
- Series/paper ratios: 7.61, 7.10, 9.61, 6.80, 7.56, 9.77. Patterns and shapes supplement color.

## Facts checked

- The 20 baby teeth and approximately ages 6 to 12 shedding statement: [American Dental Association, Eruption Charts](https://www.mouthhealthy.org/all-topics-a-z/eruption-charts). Checked the page and its primary-tooth PDF on 2026-11-05.
- The PDF gives shedding ages 6-7 through 10-12 across the primary teeth. The fact is general information, not a health assessment of the class.
- Rows as student records, columns as questions/fields and grouping/counting: [CSTA Data and Analysis](https://csteachers.org/k12standards/) and the supplied spec. The current CSTA page identifies the 2026 standards.
- Bar-graph and line-plot teacher links: [Common Core Mathematics](https://www.thecorestandards.org/Math/), 3.MD.B.3 and 4.MD.B.4. These whole-number dot plots are a bridge, not a claim to teach fraction line plots in full.
- Every Room 4 answer, axis count, total, mode and range comes from the supplied fictional records and engine computations, independently checked above. Room 4 is labeled made up.
- Ready-column choices and numeric limits are design rules from spec.md, not claims about a child's body or ability. Readouts never show averages.
- Device-only storage and no-name guidance match the implementation: only columns and row values/identifiers are saved under dtb-our-class; no requests send answers anywhere.

## Break it

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

## Voice walk

- Curio.voice owns the queue, once-only instructions, Read and sound behavior. The bank is knowing-guide, Sadaltager, status kept. Browser speech is used during Build; no recording service was called.
- Main path used held 120 ms presses at a 2-second gap, with default Sound on. Motion was the first tap, followed by a column, chart changes, a guess, Show me, question navigation and Our class collection.
- Actual starts, in order: w-sample, charts, card, Apple answer, w-ours, kinds, Row 1 added, entry, Row 2 added, Row 3 added, counted.
- charts, card and kinds each started once across repeated chart/card actions. Every row addition on that path started its confirmation. New row instructions now take priority when entry opens.
- Welcome and how-to cuts after their stated moment passes are deliberate. Re-selecting an active mode had incorrectly cut its welcome; the held double-tap repair test now records one uncut welcome.
- Side path: Sound off, column/chart changes, Read, another chart, Sound on. Read spoke the current hint while Sound was off; silent instructions were not consumed.
- Modal Read remained available and was tested with a held click. Tab includes the card plus Read, Sound and Motion.
- The own-question honesty repair adds one neutral fixed event beyond the spec's original list. All 56 lines match the final manifest; the new event started in its focused test.
- Evidence: voice-main.json, voice-side.json, voice-frames, repair-modal-read.json, repair-quick-mode.json and repair-own-question-honesty.json.

## Feel check

- Best moment: a new row flashes above the chalk tray while its chart immediately gains a bar count or dot. The class's own choices become the picture.
- First flat moment: Sorted list initially appeared after an empty SVG. Fixed SVG display handling; the ordered rows and total now occupy the chart area directly.
- Second flat moment: entry felt like a form. Painted answers, a chart-area card and a two-column desktop layout made it more tactile. The shortest versions still require card scrolling; that remains a gap.
- The table-to-chart link is reinforced by a yellow column outline and bar/stack picking that highlights matching records. Later cards introduce numeric stacks, totals and grouping rather than another favorite-choice question.
- Opened both bar tools, bundled only to Scratch, and compared the laptop scene beside Beat Lab in bar-comparison.png. The board, chalk texture, patterns, painted categories, ambient glint and physical tray give this tool its own visual world.
- This remains an exploratory classroom instrument, with personally relevant data as its payoff. No extra game, topic or scoring system was added.

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

- 92 captured frames across bar-frames, first, tests, frames, focused, voice-frames, audit, repairs and finish. Each was inspected directly or on labeled contact sheets, with key problem frames opened at full size.
- The full STANDARDS size sweep ran once late. Subsequent shots covered only repairs and affected views. audit-frame-index.txt lists all 50 audit PNGs.
- Also inspected: all 13 final-size art assets on art-sheet.png, the bar comparison, the grayscale frame, the final preview SVG capture and the own-question record.

## Art made

- 13 unique gpt-image illustrations, all people false: five fruits, four travel objects and four seasons. Original PNGs remain in art/raw; final keyed WebP files total 25.6 KB.
- Full prompts and provenance are in art/prompts.json. Every piece was inspected on the final dark board. No painted asset needed a redraw.
- Charts, table, chalk dust, tray, shapes, patterns and motion are code. preview.svg reuses five painted fruit icons beside its coded graph.
- Bundle 184.7 KB plus 0 KB recorded voice, against the 2 MB goal. No teaching image was dropped to save size.

## Art still to paint

None. Thirteen of thirteen painted assets are present; zero people assets.

## Engine changes wanted

No shared edits were made. See handoff.md for the exact DataTable, renderTable, drawDot and drawBar promotion candidates: kind/choices normalization, counts alias, categorical/grouped dots, fitted dense-stack radii and optional decorations. Count bars and sum already exist.

## Left open

- Small-screen short-choice visibility and some secondary vertical-flow controls still need design review. This Build is not a clean layout or polish sign-off.
- Six visible rows are verified for the compact Sample and main laptop framing; other table/card layouts can show fewer rows until scrolled, especially editable rows.
- The full audit snapshot predates scoped fixes; current repair evidence and source hashes are preserved. Its 375 px context acquisition was unavailable, although separate real iframe checks passed.
- Sadaltager recordings were intentionally not generated during Build. Browser speech works; the recording manifest is complete.
- Closest legacy neighbor code-tracer had no handoff.md or refine.md to read. Its source and the two designated bar tools supplied the available finish references.
- Spec conflicts and choices are documented in handoff.md: keep the made-up sample, respect write boundaries instead of changing the engine, use the requested image tool, prioritize short landscape controls, and avoid grading free text without evidence.
- All owned Chrome processes and preview servers were closed; host.html was removed. Scoped process inspection found no remaining owned browsers, and final port probes passed.
