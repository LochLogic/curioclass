# Water Shapes Earth handoff

Build only. No commits, deployment or polish round.

## Source map

src.html starts from the kit starter frame. CSS provides real-pixel wide, short landscape and stacked layouts.
CONFIG defines each bench's variables and default plan. calculate is the pure numerical model.
Each run snapshots its plan, fairness, seeded trial factors and results before animation begins.
The SVG renderer paints code-driven cracks, liquid, chip area, stream channels, grains and delta over generated art.
Plots use kit/graphing.js Plane. Shared motion, tones and narration use kit/curio.js.
Stable plan controls and step/mode buttons retain focus. Editing a cell cancels playback and invalidates the old view.
The lab book stores completed runs under curio-water-shapes-earth with try/catch. Claims are session-only.
The __tool hook exposes state, models, seed generator, voice log and rendering for review.

## Open questions resolved

- Keep the invented freeze and dissolve rates as the spec leans toward. Label them as lab-model rates on screen and in notes. Do not add measured field rates or new content.

## Conflicting instructions and interpretations

- STANDARDS and POLISH say Motion off removes movement but never timing. That overrides the spec's instant-run wording. Run duration is preserved, with Skip to end live throughout.
- User requires stopping when codex-report.md is written. The report is therefore written once, after verification, rather than as an early rolling document.
- Bar tools were bundled into Scratch mirrors to obey the user's write-only scope. Original bar-tool folders were not changed.
- Dissolve trial noise acts on loss rate, not directly on remaining mass; freeze width stops at 1.00 mm when broken.
- The claim column copies session claims for their own run. Claims do not enter localStorage.
- All 13 specified illustrations were generated using the built-in image tool instead of the spec's older local-FLUX workflow, as requested by the user and current build instructions.
- A Stream Table group tab previews that group's computed final state immediately. It does not rewind the overall clock, so a four-group playback still ends within 20 seconds.

## Art and voice

Prompts, provenance and raw originals are in art/. Assets use art tokens in one image bank.
No people were requested. Textures clip to code-drawn rock halves. All changing measurements stay in code.
voice/lines.json specifies gravel-ranger, Algenib. No recordings were made during Build; browser narration is the fallback.
The jar was redrawn once after full-size inspection found colored spill from the original mixed alpha/key source.
Its final opaque green source uses the supported keyed treatment, with a cropped outer margin, to keep glass neutral.
Other cutouts use the existing despill option. Every selected finished image was inspected at its output size.

## Engine changes wanted

None. Kit, docs and scripts were not edited.

## Review next

Cold review should inspect the simplified frost model, dissolution chip shrinkage, delta sorting and the real-time performance of SVG redraws.
Read codex-report.md for checked states and remaining limitations. Evidence stays in _scratch/water-shapes-earth/.

## Verification outcome

480 discrete plans matched independent Python fixtures. Another 9,600 noisy result values stayed within their no-noise bounds.
All 13 selected images decoded. Hosted phone frames have no page-wide horizontal scroll; Plan still needs vertical scrolling.
Held-click voice logs show one Conclude and Graph how-to, five unfair-plan events and two split events.
Completed runs persist; session claims are not stored; Copy table worked through a real held click.
The complete default student path finished its 10 / 8 / 15 second runs without errors.

The single full audit stopped after 64 frames with KeyError: End in its own key map. No audit.md was produced.
The submitted audit-states.json now uses supported ArrowDown inputs. A second full audit was not run.
Targeted checks reused the audit's size/resize functions: six remaining/extreme states had no mechanical leads,
and held-input resize paths for all three benches reported no runtime errors. The complete walk remains unverified.
Frame inspection prompted compact bench-space, scale-display and slope-card fixes; affected paths were re-shot only.
Chrome sessions and host servers used ports 9990, 9991 and 8795 and were closed. Temporary host.html was removed.

## Numeric footnote

The supplied Sources footnote says a trial can be up to 13 percent from its group's mean.
The exact maximum above a three-trial mean for factors 1.1 / 0.9 / 0.9 is 13.79 percent.
Done when 7 correctly uses the no-noise baseline, and every tested trial meets that bound.

## Cold review changes

Review evidence lives under Scratch/review-*. Cold student play preceded reading this handoff and source.
Step changes hush speech from the old screen so Graph cannot delay Conclude; completed runs queue the finished how-to.
finishRun ignores inactive or invalidated runs, preventing stale completion from entering the book.
Compare selects a real one-variable pair and names its changed values, measured means and relevant water property.
Identical plans are described as repeats; fully confounded plans do not receive causal model answers.
Stream deltas require transported grains. Silt appears only for mixed sediment, which includes pre-suspended fines.
The jar was redrawn and processed with art.py --rekey; its SVG applies saturate(0) to neutralize residual key tint.
The Lab book control states On this device before any automatic save. Notes distinguish model constants from field measurements.
The no-transport state is included in audit-states.json. Review uses Chrome 9940-9947 and host 8745.
On stacked screens Plan now places the editable table before the still bench, keeping the dropdowns above the fold.
Run continues to give the illustrated bench the full stage. The earlier phone Plan scrolling limitation is resolved for primary controls.

## Spec source conflict found in cold review

Hjulström 1935 table 7, printed page 295, gives 8 mm at 0.81 m/s and 30 mm at 2.18-2.21 m/s.
Page 296 explicitly calls the curve a preliminary zone with depth/grain-size qualifications.
The spec's 32 mm pebble cutoff of 1.50 m/s cannot be represented as a faithful rounding of that table.
The tool now identifies cutoffs as model choices in notes and avoids attributing exact cutoffs to Hjulström on screen.
Changing the constants would contradict the spec's flood/4% pebble outcome, so that spec decision remains open.
The source PDF, text extraction and full-page renders are preserved in Scratch. No new measured threshold was substituted.

## Final audit and confirmed corrections

The cold-review audit completed once, exit 0, within 40 minutes. Its 97 frames and report remain in Scratch/review-audit.
Confirmed compact caption spacing and slope-card overlaps are fixed. The claim's existing label now also has explicit ARIA linkage.
Region warnings for the intentional group controls and the specified phone table scroller are documented in the review report.
The lab book now owns its narration and makes background controls inert; closing it restores focus and the current step's hint.
Motion off keeps stream grains static during the timed run, then shows the final outcome. An explicit group preview still acts immediately.
No shared engine, scripts or docs were edited. Main-path/modal voice and affected-size checks follow these narrow corrections; no second audit is run.
