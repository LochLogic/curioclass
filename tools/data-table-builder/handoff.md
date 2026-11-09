# Data Table Builder handoff

## Build structure
src.html starts from the kit starter. CSS defines the chalkboard, responsive table/chart split and chart-area cards. The final script holds column definitions, Room 4, two independent mode states, family-engine adapters, question cards, row entry and local saving.
DataTable owns data changes; renderTable supplies semantic tables; Chart draws bars and dot facets. A local numeric encoding lets the current engine draw categorical dots. Decoration adds art, exact ticks, counts, patterns and motion.
No shared files were changed. No commits or polish round.

## Open questions resolved
- Keep the fictional Room 4 dataset, explicitly labeled made up. The real data is the class's own collection.
- The brief's image tool overrides the spec's older local FLUX route. All 13 icons are gpt-image art, people false.
- STANDARDS takes precedence over the spec's stacking breakpoint in short landscape: keep stage and controls side by side at 680x425.
- Six rows with 48 px editable targets plus a larger chart do not fit a 425 px height. Compact sample text rows are used; editable rows retain their target height and scroll.
- The spec asks for shared engine modifications but the build boundary forbids them. Use the current engine and local adapters, with desired promotions below.
- Adding a column after rows exist is unspecified. Collect explicit values for each existing row before committing the column; Cancel is transactional.

## Sensitivity
Teeth lost touches children's bodies. The displayed ADA fact is general; use the sample rather than asking students to compare development. No names or health judgments. The jumping-jacks column is optional. Offer an equally valued alternative; no race or achievement score is attached.
No cultural or religious content. No people in the image set.

## Engine changes wanted
- kit/data-desk.js, DataTable: normalize kind and choices into existing type/values metadata and expose counts as an alias for count. Sum and count bars already exist.
- kit/data-desk.js, Chart drawDot: support list and yes/no x values with exact categorical ticks and groupBy facets. The tool currently encodes values locally.
- kit/data-desk.js, drawBar: optional count labels, filled patterns and axis artwork. Current tool decorates the engine's output.
- kit/data-desk.js, renderTable: header selection/sort actions, stable row identifiers, typed cell editors and preserving header nodes during sorting would avoid post-render decoration.
Do not promote this code into the kit before the repository's three-consumer rule is met.

## Next review
The cold review's current evidence is in `_scratch/data-table-builder/review-*`.
`codex-report.md` describes the earlier Build snapshot and its gaps, rather than the repaired source.

## Cold review changes
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

## Cold review disposition
The single audit completed with 94 lead instances against its snapshot. Focused repairs then checked every affected size; the full audit was not repeated. See `codex-review.md` and `_scratch/data-table-builder/review-audit-triage.csv` for dispositions.
The prescribed field/split-only check can be found by enumerating columns. This is left as a blocker under the review's strict Break it rule: replacing it with a reasoning or attempt-limit assessment would add a feature beyond the spec. The label remains the narrow factual Column matched; it never grades the prediction.
The compact header/phone stack constraints remain should-fix spec/layout conflicts. This review does not claim a ready or all-sizes pass.

## Build snapshot validation (before cold review)
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
