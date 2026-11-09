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

## Cold review repairs
- Invalidating a charge, condition, verdict or filed sentence clears later approvals and stale session results. Answer selectors also invalidate a filed conclusion as soon as they change.
- Admissibility asks explicit mixed Yes/No questions. Corrections persist per case in the page's session record and are identified as guided practice, including after reopening. There is no mastery score.
- Evidence exposure and late-alpha flags persist across Lineup visits and case reopening. Previously chosen standards survive reopening so opening a folder does not silently change alpha.
- At true p = 0.50, Docket labels its second bar as a rejection rate and explains why the unshaded area is not Type II error.
- Stage changes hush obsolete speech. Voice manifest uses a high school clerk style; native browser speech remains unrecorded.
- Proof cards show the error tradeoff. Cereal evidence was redrawn with the box physically on the scale, using built-in imagegen; its prompt and raw PNG are preserved.
- Evidence paintings fit their full frames instead of losing objects to wide or phone crops. Large screens give the art more height; the cereal label follows the painted box on load and resize. Compact headers retain the privacy disclosure even when the session panel has little room.
- Audit paths use the revised condition answers, a real Lineup drag and an added Sentencing state.
- College Board revised the AP numbering for 2026-27 to Units 3 and 4. The legacy spec/catalog labels need an owner-level migration outside this review's write scope.
- The official Common Core text includes simulation requirements in S-IC.B.4 and S-IC.B.5. The specified analytical intervals and treatment tests support only parts of those standards; Docket's coin power simulation does not fill those clauses. Notes now state this limit. Changing curriculum mappings or adding a different simulation would exceed this review's spec and write scope.

## Sensitivity
All seven cases are fictional statistical examples. The clinic case concerns appointment attendance, with no medical advice. The courtroom is a teaching metaphor, not legal guidance. No depicted people, cultural traditions, real defendants or historical trials. Keep the notes' limits on population generalization and legal analogy.

## Next review
Follow REFINE.md for the next cold lenses. The original build report remains historical evidence; this review's repairs and curriculum limits are described above. Native narration still needs listening review when recorded clips are produced. No git commits were made.

## Build verification and repairs
- One complete mechanical audit finished with 51 leads. Its 97 screenshots were visually reviewed. The report is in _scratch/courtroom-statistics/audit/audit.md.
- Afterwards, focused checks repaired the compact Standing Desks charge, stamp/header spacing, same-mode rapid taps that cut welcomes, the daylight loop under Motion off, hidden phone alpha labeling and Sound-button width changes.
- Charts now observe their own rendered size and redraw on the next animation frame, fixing flattened labels after the readouts take space. Sentencing has a dedicated compact arrangement and short bound note.
- Follow-up checks used an isolated Scratch bundle while the original audit finished, then checked the final primary bundle. The full audit and full size sweep were not repeated after these focused fixes.
- Compact real-click follow-ups reached Evidence for all six numerical cases, a verdict for Desks, and dismissal for the viewer poll. Keyboard-only Seeds reached Sentencing. All 75 Docket combinations matched scipy.
- Final audit-states.json also includes the two Docket extremes for the next review. The completed audit used the original nine named states, plus its automatic mode checks.
- The remaining zero-font header leads are intentional icon buttons: visible 18 to 23 px glyphs, 44 px targets and explicit accessible names. A case-folder first tap deliberately skips the general welcome and speaks the case instruction, as STANDARDS requires.
- The context builder uses two compact native selectors for sentence fragments, selectable in either order, with a live sentence preview and File sentence control.

## Cold review verification
- The single cold-review audit finished with 18 leads and 145 inspected frames. Its report is _scratch/courtroom-statistics/review-audit/audit.md. Compact Docket cutoff labels and a visually detected Lineup bracket crossing were repaired, then checked at the affected sizes without repeating the full audit.
- Independent SciPy comparisons passed for six case statistics/tails, 30 intervals and 75 Docket settings. Held-click voice events passed 5/5; keyboard-only Seeds reached Sentencing; the default main path was walked with Motion and Sound on.
- Final before/after regressions preserve poll dismissal through subsequent answers and preserve a pre-evidence alpha change through reopening without a late-change flag. Final focused captures have no console errors, warnings or exceptions. Bundle: 600853 bytes.
- Temporary host removed. Review evidence, previous cereal art and scripts remain in the authorized Scratch folder.
