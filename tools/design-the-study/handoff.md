# Handoff: design-the-study

Build only, 2026-11-02. No commits, branch operations, shared kit edits or polish round.

## Built
Offline manuscript-and-laboratory simulation for Grade 12. Story has six method rows, seeded individual records, exact decomposition, 1,000-shuffle tests, seven ordered editor letters, three endings and device-only badges. Bench runs 400 fresh studies and pins up to three designs on one horizontal axis.

## Source map
All presentation and logic is in src.html, copied initially from kit/starter/src.html. The light paper tokens override theme-912. The model, permutation test, rendering, voice table and UI actions are separate functions. Curio.voice owns narration behavior; Curio.init, tone and yes supply kit settings and feedback. No family engine applies.

State draft keys: compare = before/groups/days; assignment = choose/tired/random/blocked; order = day2/order; control = water/placebo; blind = everyone/volunteers/double; timing = stopwatch/computer; n = 20/40.

The public window.__tool includes the specified state, setMode, seed, setDraft, run, shuffle, bench and bars hooks, plus model, permutation, flaw, submit, draw, allLines and voice logs. bench returns a promise. The RNG function lives on a run so its shuffle continues the same stream. Calling permutation again advances that stream; reconstruct model(draft, seed) to reproduce its first test.

The person effect is fixed per participant within a study. Every Bench seed rebuilds it. Both-days random order assigns exactly half to drink second. The 20-person study uses odd-numbered IDs. Chance is the arithmetic remainder, so all seven parts sum to the recorded estimate.

Decorative playback takes 1.2 seconds and is canceled on pointerdown before the actual control handler. Results already exist. Bench computation yields every 20 studies and uses a generation guard so edits and mode changes discard stale results. Resize only redraws charts and relocates Clear; it does not replace method controls.

## Responsive decisions
The laboratory overview is an 8 by 5 display of numbered cards, becoming a strip after a run. Inspect cards opens the full 8 by 5 button grid, with arrow navigation and per-volunteer times. At narrow/short sizes the overview is hidden, while the inspector retains all records and 44 px targets. This resolves the physical conflict between a narrow lab column and eight 44 px cards.

Below 400 chart pixels, the waterfall turns horizontally so every component name fits. Narrow chart notes use deliberate ellipsis with the complete text in title. The editor's letter overlays the manuscript so the result remains visible. Revise returns keyboard focus to the named row with preventScroll.

## Open questions: choices taken
1. Keep news-reader, Rasalgethi. Its crisp editor delivery fits; lively-host does not. Browser speech is the current fallback because recording is forbidden in this build.
2. Use the spec's revised short-dark-hair portrait brief as the replacement direction. The existing silver-bun editor-quill.webp is preserved, token registered, and never displayed. Only the opening coded faceless silhouette is present; a reviewed new portrait for letters and endings is still needed. No people were generated.
3. Keep the invented adult energy-drink experiment, rather than the song fallback. Adult ages and the AAP advice appear on the first screen and in notes.
4. Leave S-IC.B.4 and AP Unit 3 sampling to Poll Workshop. This tool covers the experiment comparison, design critique and randomization-test activities.
5. Keep the light manuscript theme overriding the 9-12 dark tokens. The computed contrast ratios agree with the spec.

## Specification defect requiring a decision
The prescribed editor sequence has no rejection for placebo + Everyone knows + Computer. The model correctly adds -15 ms expectation, yet the editor can Published that design and say nobody knew. With a placebo and volunteers-only blinding, computer timing is unbiased in the specified model, but the acceptance sentence still overclaims that nobody knew.

The build preserves the given letter rules instead of inventing an eighth letter or a new teaching rule. This path needs an owner/spec decision before release. Recommended review question: add an expectation rejection for an unblinded placebo, or constrain that combination? Do not call the current editor an exhaustive sound-design validator.

## Art
Five new images made during this build using the built-in OpenAI imagegen tool: reaction-lab, drink-can, water-glass, stopwatch and reaction-box. Full prompts, style and provenance are in art/prompts.json. Raw PNGs are in art/raw; finished WebPs were processed only with art.py --rekey. All five were inspected. Object edges were rekeyed with despill; none needed a redraw.

## Verification pointers
All build evidence is under _scratch/design-the-study/.
- check_model.py and numbers.json: independent NumPy reconstruction, 400 seeds and 1,000 shuffles each.
- functional.js and functional-result.json: exact mixes, decomposition, shuffle determinism and recount, all letters and endings, storage and cancellation, and every 400-study table mean.
- sweep-1/2/3: single full size sweep for Draft, Result and Bench; phone evaluator quoting was repaired in targeted.json.
- special: endings, grayscale, Motion off, three pins and inspector sizing.
- targeted: repaired result layouts, phone runs, full-size keyboard activation and 44.25 px inspector targets.
- play and voice-play.json: whole Story sequence, held clicks at a 2-second pace.
- contrast.json: computed text, focus and border ratios.
- audit/: final mechanical audit output and frames. The report records its disposition.

## Engine changes wanted
None. No kit files were edited.

## Remaining limitations
Revised editor portrait and news-reader recordings are deferred. The compact card overview is not itself interactive; Inspect cards provides the full records. The acceptance-rule defect above remains material. Browser narration has not been listening-reviewed. There has been no live classroom trial or separate cold review.

## Final build verification
The full audit completed once in 24.2 minutes with 566 leads, not a clean result. The original audit passed console, resize, Motion off, five-tap speech and settled keyboard checks. audit-disposition.md in Scratch maps all its bullet leads and walk warnings.

Bounded repairs then fixed compact Run overlap, phone hint coverage, explicit inertness of covered paper and modal backgrounds, real compact reason text, repeated active-mode welcome cuts, first-chip layout movement, ending focus, Escape hint restoration, Clear resize focus, seed zero and fresh seed windows for consecutive Bench batches. Bench advances runIndex by the batch size; seed(n) resets that window.

Post-repair numerical checks passed all nine design mean tolerances. Random-order paired SD was 1.751 ms in the advancing-window run. Compact/letter/record targeted layout scans were clean, quick mode taps preserved one welcome, first-chip position stayed unchanged, and ending keyboard continuation passed. Phone hint top 779 px stays below the lab bottom 773 px; active targets are at least 44 px. Patterns were checked on compact horizontal waterfall bars too.

The full audit and full size sweep were not repeated after those repairs. The report distinguishes original audit evidence from targeted rechecks. The phone three-pin comparison remains visually compressed. The specification defect and media deferrals above remain open. Browser listening and classroom use were not reviewed.
