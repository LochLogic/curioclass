# Warming Evidence Desk handoff

## Cold review changes, 2026-11-06

The cold review keeps the original desk and the wide-screen rows. At short landscape sizes, Argue now has four
record columns with distinct claim and evidence buttons, keeping every student choice visible before Compare.
The right-hand reading panel scrolls its longer finding after Compare; its current hint stays above it.
The scientists' detailed reasons and citation links scroll below the student choices in the compact record cards.
The added audit states cover a full board before and after Compare at 680, 800 and 1000 pixels.
The final audit confirmed hidden phone hints and narrow citation targets. The same hint node now moves to the phone
Ask dock or Compare footer, returning to the panel on larger screens. Both phone footers are 95 pixels tall and the
scrolling workspace ends exactly above them. Deep Ask selections hand focus to the matching visible dock control.
Citation buttons have an explicit 44-pixel minimum width. Compact compared views name the scroll action in the hint.

Ask labels Fits as a pattern fit, not proof. Argue states that Same compares claims only and shows its own device-only
save notice. The comparison label uses a compact sans-serif style so Different fits beside the record name.
Already-playing span, solar-axis and eruption instructions stop when the student's action makes them obsolete.
The fixed voice text is unchanged. Read priority and the shared voice engine are unchanged.

The flattest moment was Argue hiding half the records just as the student tried to assemble a case. All four records
and their gathered answers now stay together. The weakest facility icon was redrawn using built-in OpenAI imagegen,
then processed with art.py --rekey. The prompt is in art/prompts.json, the raw image in art/raw/icon-fossil.png and the
finished asset in art/icon-fossil.webp. The older image is preserved only in Scratch. No people were added.

Fresh downloads from NASA, NOAA, LASP, NASA GISS and GCB/OWID match all 725 annual values. Independent arithmetic and
source hashes are in _scratch/warming-evidence-desk/review-sources/. The existing IPCC endpoint correction is sound.

Spec conflict left for its owner: Compare permits a reveal with four unsupported guesses, then copying the visible
scientists' chips yields four claim matches. This is explicitly required by optional evidence and live revisions in
the spec, while CODEX-REVIEW treats a cheap full-agreement path as a blocker. The on-screen claim-only qualification
reduces the false inference but does not certify evidence reasoning. A mastery or evidence gate needs a spec decision.

The cold review's one full audit completed with 30 grouped leads: 13 fixed and 17 accepted as specified phone scrolling,
intentional modal coverage or BASELINE 16 welcome skips. All 59 audit frames and 17 post-repair frames were inspected.
Native post-repair checks cover phone controls, Read with Sound off, deep focus, breakpoint reparenting and jittered
year-cursor input. All owned Chrome and host ports are closed. Detailed evidence: review-audit-dispositions.json and
review-final-validation.json in Scratch. No second full audit was run.

Original builder context: Build only, no commits or deployment. All scratch work is in _scratch/warming-evidence-desk/.

## Source map

src.html derives from kit/starter/src.html and uses kit:curio CSS, Curio.init, Curio.voice, Curio.tone and Curio.stop.
No family engine is specified. Responsive SVG draws the exact annual series at actual stage dimensions.
data.json is loaded through the json:data bundle token. The records retain separate end years; no extrapolation occurs.
The four keys are co2, sun, volcano and fossil; temp is the reference record. Five spans produce twenty board cells.
mean and regression recompute averages and inclusive-endpoint least squares. validateNumbers throws on mismatch.
buildControls creates stable buttons once. Updating a selection changes attributes and text, not those button nodes.
ask keeps the other choice, saves only a newly asked cell, and replaces the visible answer synchronously.
drawChart owns paths, bars, axes, trend lines, mean bars, eruption markers and cursor. CSS owns only the optional fade.
No delayed callback can overwrite a more recent question. Pointer input and chart keys use the same whole-year cursor.
toggleClaim implements the exclusive Doesn't fit choice. agreement compares exact sets, including extra-chip penalties.
compare inserts the scientists' content only after every row has a claim. Revisions update the comparison live.
Stored work includes board questions, claims, up to two evidence choices, and the optional overall choice.
Storage loading filters invalid values and deduplicates. Compared state is deliberately not restored.
Clear desk confirms for three seconds and resets both saved work and revealed conclusions.
Curio.voice owns narration and Read, with scope equal to state.mode, explicit validity checks and once-only how lines.
Read speaks the current answer and its note in Ask, otherwise the hint. __tool exposes model and voice logs for review.
Axis-use flags are per record, so trying CO2 From zero does not consume the Sun's separate how-to.
The axis slot stays reserved when its controls are hidden, keeping board targets steady between records.
The initial tray hands focus to the matching record control. Scientist links hand focus back to Ask controls.
The Board dialog has a blocking veil, keyboard containment, Escape/Close and focus return.
Span controls retain focus when responsive layout moves them between the panel and the compact dock.

## Open questions resolved

- Sulfur dioxide: retain the pollution-haze note. No independently paired annual CEDS and second-inventory series,
  including a checked licence, was validated in this Build. The spec expressly permits this fallback. Its term
  sixth record is inconsistent with the four listed factor records; temperature would make the existing total five.
- Frozen data: use the supplied 2026-11-05 source snapshot, recomputed and checked on 2026-11-06. Preserve the date
  on screen. Refresh with climate-dashboard at the yearly review. No runtime network access is needed.

## Spec corrections and implementation choices

- The user says to stop when codex-report.md is written. Evidence and a draft report accumulate in Scratch;
  codex-report.md is written once, at the end, instead of the build brief's early-report instruction.
- The requested image tool takes precedence over the Art section's older local-FLUX wording. Five images were
  generated during Build, copied to art/raw, processed only through art.py --rekey and inspected at final size.
- IPCC's human-caused 1.07 °C estimate ends in 2010-2019; the observed 1.09 °C ends in 2011-2020. The reveal labels
  both correctly rather than presenting them as precisely the same period, as the spec does.
- The CMIP7 file matches all specified haze point checks, but Agung peaks at 0.03649 in 1963, not in 1964.
  The requested 1964 value 0.02562 is correct. Eruption dates and all four temperature comparisons remain unchanged.
  Distinct annual eruption maxima rank 1884, 1992, 1963, 1983 in this data. Adjacent post-eruption years must not
  be counted as separate eruptions when ranking the events.
- The Argue welcome omits Then tap Compare because that control begins disabled. The hint names Compare once ready.
- STANDARDS' 44-pixel targets take precedence over the spec's 30-pixel board rows. At short landscape sizes the spans
  move into a dock beneath the charts and Board opens a wider popover. This keeps the chart and primary Ask controls
  usable without shrinking type below 10 pixels.
- At short landscape Argue sizes, all claim and collected-evidence choices fit in four columns; the scientists'
  longer reasons scroll after Compare while the overall answer and Compare stay visible. All candidate chips retain
  44-pixel height. The 375-pixel layout follows the spec's stacked order
  and scrolls vertically inside the workspace; its panel is below the charts and answer. A fixed phone question dock mirrors the same
  record, span and axis controls so primary Ask actions remain in view without compressing the real charts.
  Phone Compare is fixed to the bottom too. These are responsive access to existing actions, not extra activities.
  The workspace ends above this opaque footer, and the header stays visible. Mode changes return the workspace to the top.
- Agreement is a literal comparison of selected claims, not a mastery score. Evidence selection is not graded.
  Copying scientists' claims after Compare is possible and intentional for revision. No best score is stored.
- Browser voice is the fallback. friendly-dad / Achird scripts are complete, but no recordings were made during Build.
  The installed browser voice cannot guarantee the bank voice's timbre until recorded clips are provided.
- The two bar tools were bundled into scoped Scratch mirrors. Their original folders were not written.

## Sensitivity

No people images, personal disclosure, religion, hard history, Indigenous cultural narratives or body judgements.
This is global environmental science. A reviewer should check that the observatory and industrial paintings read
as illustrations, and that Fits is understood as consistency in one span rather than causal proof from correlation.
Mauna Loa and the eruption names identify source locations, with no claims about local cultures.

## Art

Five scientific gouache paintings, each marked people:false and drawn_by:codex. Largest finished display is 72 pixels;
the 144-pixel WebP assets provide room for sharp display. The raw selected PNGs stay in art/raw. All five are used.
No missing people assets or stand-ins. Rich chart details remain exact SVG rather than painted approximations.
Prompts and style are in art/prompts.json; final paths are art/icon-co2.webp, art/icon-sun.webp,
art/icon-volcano.webp, art/icon-fossil.webp and art/icon-temp.webp. The built-in image tool was used.

## Engine changes wanted

Optional: kit/curio.js, Curio.voice.say, add an explicit replace:false option that skips same-key queue replacement
for repeatable event sequences. Two Compare taps two seconds apart otherwise drop the first queued finding line.
This tool works around it with unique per-Compare keys on both parts of each sequence. Shared files were not edited.

## Original build verification map

Scratch prepare.py and check_numbers.py reproduce the source computations. numbers.json, number-checks.json and
snapshot-provenance.json retain outputs and input hashes. functional.js and functional-results.json cover all 4,096
legal claim-set combinations, the main state rules, axis invariance, evidence FIFO, no-data and reveal gating.
Driver shot files, layout readings, frames, voice logs and the final mechanical audit remain in Scratch.
codex-report.md records the final checks, corrections and any remaining limitations for the cold reviewer.

The one full audit completed in about 29 minutes: 53 frames and 250 leads. audit-dispositions.md and .json answer
each original lead. The pre-fix bundle is preserved as audited-before-layout-fixes.html in Scratch.
Post-audit repairs addressed phone clipping, laptop Clear fit, narrow argument heights, eruption labels, graph ticks
and focus. post-frames and repair-*.json supersede earlier frames in those views. No second full audit was run.
Targeted probes have no overlap, tiny text, small targets or clipping; the open modal intentionally covers the background.
Phone dock and deep panel controls were both driven with real input. Header and footer share a workspace boundary
at y=742 in the 375x812 iframe, so content cannot draw under the fixed dock.
focus-repairs.json verifies focus on span-3 across compact/wide reparenting and a real scientist-link jump back to Ask.
The final exhaustive functional check still permits exactly one full-agreement configuration out of 4,096.
