# Graph Studio build handoff

The source is one readable HTML file: instrument CSS and semantic drawers, then parser, tape controls, paper transforms, adaptive sampling, numerical features, input, regressions, tables, notebook and kit voice integration. The bundle inlines kit/curio.js and the optional voice bank map. No raster art or external libraries.

The parser uses bounded recursive descent with operator binding powers; no typed text is evaluated as JavaScript. f and g definitions are looked up separately, circular definitions stay undefined, and evaluation has a fuel limit. Curve coordinates share the same evaluator as table and trace. Least squares uses normalized x before solving small normal systems. Data and fits retain full precision; readouts round. Numeric scrubbing has separate keyboard and precision-drag paths; tape rebuilds wait for a held pointer to release.

Native typing keeps the equation input node in place. `reconcileRulers` updates only its dependent rulers; number tabs update separately. `addLine` retains the new target index across focus restoration. These details matter: replacing the focused input during a trusted input event lost focus in Chrome, and restoring the old input changed the active index during Enter. Both were found and verified with actual CDP text input, not only direct state assignment. Decimal and scientific literals retain their scrubbing precision.

Adaptive refinement has a budget for each pixel segment so a difficult region cannot consume the whole page's refinement budget. Hole probes are numerical at zero and literal constants, not a general symbolic limit system. Key features currently cover ordinary y curves. A fit uses a centered basis in its printed equation; the full-precision function is retained separately. Exact round halves go away from zero; 0^0 is undefined.

Tables remember start and step per pen and can also sample the fitted curve. Square uses axis coordinates, including base-ten decades on log axes. Direct tracing and pins currently operate on equation-tape curves; data fits have their own readout and table.

The report records spec discrepancies. Independent build evidence lives only in _scratch/graph-studio/. No other tool or shared engine was modified. The original build and review reports are historical; see polish.md for the Claude Refine fix round.

## Engine changes wanted

None required. The existing kit's emoji power labels are restyled locally to the plotter's simple lamps. Curio.voice handles speech and Read priority.

## Next review

Check keyboard and real-pointer numeric scrubbing, oscillation alias warnings, large-coordinate numerical features, mobile tape scrolling, and source-data fit discrepancies. General implicit equations and inequalities are explicitly deferred by the spec. Notebook is browser-local and storage errors are reported without erasing the current page.

## Cold review changes

The one-pass review keeps the plotter surface and eight inks. Measurements now sits over the tape with a collapsible columns editor, so fitting leaves the data visible. Drawers use native modeless dialogs: Read remains usable, Escape closes the drawer, and Close restores its handle. The live table updates with parameter edits. Its choices preserve the current selection when recomputed.

Hole probes check approach on both sides at four distances, preventing symmetric poles from posing as finite holes. This remains numerical evidence, not a symbolic proof. Aliasing warnings inspect trigonometric argument ASTs with current parameter values; the warning stays visible in compact views. Live announcements retain the last value after rapid input. Empty ruler bounds and subnormal paper limits are refused explicitly; more than 1,000 data pairs preserves the previous data. Notebook restore refreshes data-source labels too.

Dragging a pin within six paper pixels of the other pin on the same curve snaps their parameters together, so an apparently coincident pair cannot retain a spurious tiny denominator. Table opens directly on an existing fit if the active pen has no curve, starting at the first measurement. Drawer transitions stop an obsolete Read; data Read names the actual dataset and fit, and equation Read expands function names for the ear. Bounds are guarded during pan, zoom and square-grid resize as well as form submission.

Current primary-source checks corrected Census 1940, 1970 and 1980, Saturn rounding, the MathWorld rose link and OpenStax's licence. Manual and draft metadata name versions, measurement units and permissions. No reference text or figures from restrictive licences are bundled. Reproduction and verification evidence is under _scratch/graph-studio/review-*; the builder's report remains historical.

## Sensitivity

The historical Census series excludes many Indigenous people in early enumerations and changes geographic coverage. The Manual now states that plainly and cites the Census Bureau. A later cultural lens should check that wording and ensure no one interprets the curve as all people in fixed present-day boundaries. Census and National Archives explanations were checked independently. No people imagery is present.

## Review verification

Independent review checks passed 45 numerical/data cases and 35 extreme-input cases. Native point dragging, coincident-pin dragging, numeric scrubbing and keyboard rulers were checked separately. The 18 completed exploration segments total 10.390 minutes; one failed Chrome connection run is excluded. The single audit completed in 530.859 seconds on port 9931 with host 8735, producing 33 frames and 60 leads. Its 23-control walk, repeat/quick Read, Motion off and resize checks had no console errors or stuck controls.

Confirmed audit faults were Load at 40 pixels wide and a clipped first ruler in the short landscape preview. Load is now 44 pixels; compact tape navigation, an inline number row and a compact ruler keep the first slider visible. Targeted re-shoots cover 680x425, 800x500, 1366x768 and the 375x812 iframe. A later root/live-region overflow guard gives zero page overflow at all eight required sizes. The Manual's Read follows its visible paragraphs when scrolled. No second audit was run: review-audit is the pre-layout-fix snapshot, and review-auditfix plus review-scrollproof are the final targeted evidence.

No recorded clip, audible audition, physical screen reader or school Chromebook was available. These remain verification limits, not claims of tested hardware. All produced code and metadata remain local and draft.

## Claude Refine fix round 1

See polish.md and _scratch/graph-studio/ for numbered before/after frames and measurements. The original source snapshot is retained in Scratch. Literal rational exponent metadata is attached once by the parser, shared by plot, trace and table. Feature signatures include the view, expressions, parameters and active pen; idle input waits 120 ms, animated rulers refresh at 250 ms. New ink restarts a 1.2 second drawing pass with a bounded carriage and a short synthesized scratch through the kit audio context. A real user gesture activates browser audio. Motion and Sound stop the scratch immediately.

Table uses two columns for ordinary functions, three for polar and parametric ink, and is placed over paper so rulers remain available. Hover, focus and scrubbing highlight the numeric token inside the existing input without replacing the input. A tap keeps its button until click reaches the voice controller. Census sensitivity wording and spec open questions remain unchanged. No shared engine changes, external messages, uploads or commits.

## Fix audit follow-up

The single fix audit completed with 83 mechanical leads and 33 inspected frames. Its 23-control walk, repeated/quick Read, Motion off and resize checks were clean. Most leads describe the settled hint/tag and drawer geometry. Confirmed layout faults were a 40 px Table Next button and a wrapping phone samples footer; local min-width and compact one-line readouts address them. Targeted follow-up frames at all eight table sizes and three phone footer states are in _scratch/graph-studio/audit-followup. The audit itself remains the pre-follow-up snapshot; no second audit was run. Turning-point zero tolerance is capped at 1e-6 so enormous y windows cannot turn a positive minimum into a zero.
