# Courtroom Statistics build handoff

## Structure
src.html starts from kit/starter/src.html, includes the shared kit and 9-12 theme, then applies the specified light oak tokens. Static stage sections and controls stay mounted while their visibility changes. Cases, inference routines, state transitions, and responsive SVG drawing live in the single script. __tool exposes the required test API plus goStage, cases, allLines and vlog.

## Open questions resolved
- Keep both proportion brackets. The score-test non-rejection band and AP estimated-SE interval are both shown, with an explanation. The two-proportion score test fits the constrained null proportions for each claimed difference, rather than pretending a zero-difference pooled SE works at every claim.
- Use the light oak theme override. Retain kit/theme-912.css for its instrument controls and override its palette, header and chart colors in the tool.

## Tricky parts
- One-sided Trial intervals use C = 1 - 2 alpha. Their relevant bound corresponds to the directional test, not both outside regions. Mean Lineup uses two-sided tests and C = 1 - alpha, giving exact duality. Proportion AP intervals are not exact score-test inversions.
- Numerical t tails use incomplete beta; critical values and score endpoints use bisection. Docket binomial PMFs use log-gamma and sum the rejection tail. The cutoff deliberately uses the spec's uncorrected normal-z rule.
- Cereal and shoes use real supplied data. Bus and desks have no raw observations, so no invented dot plots are drawn. The conditions card explicitly states that limitation and uses n at least 30.
- Stage tabs unlock in order. Alpha stays live after evidence, raises an objection and invalidates the current verdict and conclusion. Session summaries remain in memory. Mode switching preserves the Trial snapshot.
- Charts measure actual CSS pixels. Resize only redraws SVG, so gavel and Docket controls remain available.
- Browser speech is the fallback; clear-teacher / Iapetus is declared in voice/lines.json. No recordings were made.

## Art
Ten new images were made with the built-in image tool. The previously supplied courtroom-empty.webp stays in use. Full source prompts are in art/prompts.json; raw PNGs are in art/raw. No people are used. Exact curves, brackets, chips and stamps are code, as specified.

## Engine changes wanted
None. No shared-kit edits were made.

## Next review
Build only. No polish round or git commit. Review classroom phrasing, supplied-data assumptions and listening quality, then use the build report for verification evidence and remaining limitations.

## Build verification and repairs
- One complete mechanical audit finished with 51 leads. Its 97 screenshots were visually reviewed. The report is in _scratch/courtroom-statistics/audit/audit.md.
- Afterwards, focused checks repaired the compact Standing Desks charge, stamp/header spacing, same-mode rapid taps that cut welcomes, the daylight loop under Motion off, hidden phone alpha labeling and Sound-button width changes.
- Charts now observe their own rendered size and redraw on the next animation frame, fixing flattened labels after the readouts take space. Sentencing has a dedicated compact arrangement and short bound note.
- Follow-up checks used an isolated Scratch bundle while the original audit finished, then checked the final primary bundle. The full audit and full size sweep were not repeated after these focused fixes.
- Compact real-click follow-ups reached Evidence for all six numerical cases, a verdict for Desks, and dismissal for the viewer poll. Keyboard-only Seeds reached Sentencing. All 75 Docket combinations matched scipy.
- Final audit-states.json also includes the two Docket extremes for the next review. The completed audit used the original nine named states, plus its automatic mode checks.
- The remaining zero-font header leads are intentional icon buttons: visible 18 to 23 px glyphs, 44 px targets and explicit accessible names. A case-folder first tap deliberately skips the general welcome and speaks the case instruction, as STANDARDS requires.
- The context builder uses two compact native selectors for sentence fragments, selectable in either order, with a live sentence preview and File sentence control.
