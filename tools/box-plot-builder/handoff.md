# Box Plot Builder handoff

## Structure
`src.html` starts from the kit starter. CSS builds a newspaper working desk. The inline datasets, line table, state,
range-box adapter, Explore rendering, Build state machine, Headline state and event wiring follow in that order.
The shared kit handles sound, motion and narration. DataTable and Chart handle statistics, dots, histograms and boxes.
Each Build set keeps its own session progress. Only Our class is saved, under `curio-bpb-class`, inside try/catch.
Help history also stays in memory for this page session. Start over resets the build but preserves marks for fields
Sam supplied, so a reset cannot turn copied answers into independently found credit. The button says this on screen.
Cold review also preserves attempt counts across Start over, preventing unlimited first guesses before help is marked.

## Cold review changes
- Pair feedback waits until the shape reason is committed before explaining the shape. The reason can no longer be copied from the preceding feedback.
- Class number parsing ignores empty comma/space separators rather than turning a trailing comma into a zero.
- Active how-to speech gives way when its step has passed. Results remain whole, and the final File control has its own once-only how-to line.
- Filed reports lead with the actual selected center and spread; focus enters the report for keyboard reading.
- Box labels have separated text positions with fine leaders to their exact marks. Headline text has a stronger paper veil.
- The Our class card now has a shaded notebook and pencil drawing. Existing paintings and the editorial palette are retained.
- Headline buttons retain their DOM identity when the verdict arrives, preserving focus.
- Short previews place the four change tiles on the newspaper margin, keeping Put back and histogram bins in view.
- Long grids get a shorter heading at laptop heights. Dot stacks are fitted locally to their real plotting frame so they cannot draw across the title.
- At phone widths, MAD and Pick give their space to the current graph and controls instead of retaining the completed card grid. The class entry form is compact on laptops.
- A filed phone report uses the remaining screen height, so its lead and earned fields replace the tiny cropped title view.
- Explore welcomes use day, game or value and wait until a draggable dot view is present. A partial Headline check names only the city still editable. Fixed lines are kept exactly in voice/lines.json.
- Dragging back to the original values restores the generic hint and hushes stale movement teaching. Selection rings follow the fitted dot positions too.
- Keyboard point selection refits the finished chart redraw, keeping all 60 equal class values and their selection ring inside the plot.
- The Headline DOM exposes shuffled position only, with no stable option-answer index; button identity is kept privately through each verdict.
- Audit states retain their real click paths; repeated number-spinner presses are represented by input entry events for a bounded audit.
- Reporter edge despill is configured, but the permitted rekey pipeline could not run: its Python environment was denied execution. Original paintings are retained.

## Decisions and contradictions
- There are no open spec questions. Kept Luka Dončić and the intended school range-whisker convention.
- The spec approves editing `kit/data-desk.js` and its family doc. The user permits writes only in this tool and
  its scratch folder. A local adapter keeps the engine's quartile box and axis and replaces whisker endpoints.
- The brief says to create the report early and stop when it is written. The user's explicit stop condition wins:
  working evidence is kept in Scratch and the complete report is written last.
- CODEX-BUILD requires generated art while BUILD says do not draw. Followed CODEX-BUILD and the user's image request.
- Numeric card sizes of 64 by 44 cannot fit ten columns in a 680-wide view with a 60 percent stage. The grid retains
  ten columns and has one keyboard/pointer selection surface; compact visual cards shrink while text stays readable.
- Facts chip rows appear in sequence so each complete choice set fits without hiding options in a scroll panel.
  Completed rows remain recorded in the final report. This is a layout choice within the ordered Facts step.
- Headline's prohibition on statistic readouts is applied before the editorial decision; the prescribed draft and
  earned final headline necessarily contain their supplied mean, IQRs and ranges.
- Source card uses `TMAX`, as the anti-copy requirement asks, rather than spelling out maximum temperature beside it.
- The configured voice is news-reader/Rasalgethi. No recording is authorized; browser speech is the build fallback.
- Our class uses at most 24 histogram bins, with widths derived from its padded axis. This prevents a wide input
  range from generating millions of bars. Input magnitudes are bounded at one million for this classroom tool.
- Histograms include an exact fixed right endpoint in the final bin. The canonical data table stays exact; a
  chart-only copy nudges that endpoint just inside the last interval for the current engine's bin calculation.
- The plot's accessible alternative retains the raw values but removes the engine's precomputed observation count.
  This keeps the Facts counting task from being answered by reading an automatic count.

## Engine changes wanted
- `kit/data-desk.js`, `Chart.drawBox`: add `whiskers: 'range'`, choosing min/max and omitting outlier marks only when
  requested. Keep default 1.5-IQR behavior. Document in `docs/families/data-desk.md`.
- `Chart.startDrag` and `keyPoint`: clamp snapped edits to the fixed axis domain. This tool wraps DataTable.set.
- Expose a drag-cancel method. This tool dispatches pointercancel on reset, set switch, mode switch and resize.
- `Chart.histBins`: include a value equal to the fixed domain maximum in the last bin. Default half-open bin
  arithmetic currently drops it. This tool uses a chart-only endpoint adjustment while keeping true statistics.

## Sensitivity
Sam is a fictional young adult reporter. All three portraits have `people: true`. Review hands, consistent identity,
friendly expression and respectful representation on the Scratch people contact sheet. No cultural or body curriculum.
Luka is named as the real data subject; no portrait or likeness is generated.
Fresh-agent representation check completed: consistent youthful adult identity, plausible hands, friendly expressions,
no stereotypes or child-facing concerns. The contact sheet remains for the owner's review.

## Build boundary
No git commits, branch actions, shared-file changes, publishing or polish round. All test evidence is in
`_scratch/box-plot-builder/`. The report records remaining limitations and exact checks.

## Verification left open
The builder's audit failed before collecting leads. The single cold-review audit later collected 14 leads and
71 frames, then stopped during later Build states with a Chrome connection reset (WinError 64). Its partial
audit.md is in Scratch/review-audit. Class-form clipping was confirmed and repaired; focused frames show
Show/Clear within 680x425 and the full laptop controls within 1366x768. The other leads were checked against
real label associations, ordinal headings, the transparent chart input layer and actual visible choices.
Direct review checks cover the required Explore and Headline sizes, keyboard-only completion, phone frames,
Motion off, grayscale, score cheats, data recomputation and real browser speech. The sports-grid size matrix
was interrupted even on its smaller retry. The audit's later states, calm, resize and walk stages did not run;
their placeholder headings are not passes. No second audit was run.
The compact card grid uses a single large selection surface; its individual visual cards are smaller than 44 px.
Our class has a longer entry form and may require panel scrolling. Browser speech is a timing-tested fallback;
the configured news-reader recordings have not been produced or heard.
