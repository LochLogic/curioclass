# Energy Accountant handoff

Build only. No commits, deployment, or polish round. All scratch material is in _scratch/energy-accountant/.

## Source map

src.html follows the kit starter frame with kit:curio and kit:theme-912. Tool CSS lays out real-pixel scenes, account cards,
two oxygen counters and the chart. No fixed scene is shrunk to fit the preview.
reactions holds balanced equations, independent atom totals and the numerical free-energy allocations.
makeTransfer moves atoms between stocked accounts; applyEntry updates molecule stocks, work and heat.
Each scene has a separate book; all five scenes post into the Ledger mode's shared table. Oxygen mode has its own table.
finishEntry posts a pending animation exactly once before another entry or scene starts. Atom positions are measured
from live account nodes each frame, so resizing does not invalidate a mover.
Stable entry nodes use aria-disabled and a refusal reason so keyboard focus survives a stock changing.
The carbon passport is a ten-step view inside the scene stage. Scene selector and side controls keep their positions;
inactive accounts, painting, ledger table and posting status hide until it closes. It records a possible journey,
not evidence that a student mastered carbon cycling. Its strip can scroll horizontally; the next-step button stays visible.
The wood card is a native dialog. Sliders redistribute whole percentages with a largest-remainder split; Check is unscored.
tick snapshots Oxygen, Cell and Work synchronously, and increments the actual condition's cumulative counters.
Run schedules ten ticks at 400 ms; changing settings affects the next tick. Run again restarts that schedule.
The 36-row NOAA DataTable retains all source means and computed swings. Chart uses a twelve-row pivot with three numeric
series because the engine's line renderer does not implement groupBy. renderTable is read-only.
Curio.voice owns narration and Read. __tool exposes state, model functions, allLines and vlog for review.

## Open questions resolved

- Retain NOAA CO2 in both this tool and climate-dashboard. This tool uses only the 2023 seasonal swing at three stations;
  the separate dashboard's long-term question is different. No source or station was changed.
- Retain the single alanine atom summary as the spec leans toward. On screen it says it is not one real reaction and
  explains soil nitrate nitrogen is represented as ammonia solely for atom counting. No unrequested two-step path added.

## Conflicting instructions and model choices

- The user requires stopping when codex-report.md is written. It is therefore written once after verification,
  instead of creating the early rolling report requested by the general build brief. Evidence accumulates in Scratch.
- The user and current build brief require the built-in image tool. It supersedes the spec's older local FLUX method.
  All fifteen assets were generated during this Build, with full prompts and provenance in art/prompts.json.
- STANDARDS and POLISH say Motion off removes movement, never timing. This takes precedence over the spec's instant
  posting wording: a quiet ledger entry still posts after 1.5 seconds, and a second entry finishes it immediately.
  Oxygen Run keeps ten 400 ms ticks. Toggling Motion during a posting retains its original completion time.
- Sucrose has no numerical energy value and alanine is atom-only. Their energy cells say not quantified. Totals
  distinguish balanced atoms from partially quantified energy. No invented reaction energy was added.
- Clear ledger removes reaction postings and restores the explicitly labeled opening stocks, rather than leaving all
  matter at zero and making every entry impossible. Night restores two glucose on re-entry when below two, as specified.
- Nitrogen stock uses the internal soil key as an NH3 atom-count supply. Cold review made this source visible in
  Leaf by day and Deer, labeled Soil N and Dietary N respectively. It is not a claim that a deer takes nitrogen
  directly from soil or that NH3 assimilation is the actual multi-step synthesis pathway. Energy and work accounts have zero atoms.
- Fermentation products remain in Body. Oxygen counters identify lactic acid and ethanol separately. Products can
  accumulate from both cell types in one oxygen-condition column; the exact mixture stays visible.
- The photosynthesis animation includes gross water exchange to show that released O2 is from water. The displayed
  equation is the requested net equation. Opening accounts hold enough water for those exchanges.
- The passport uses volcanic CO2 release for the final return to Air. This avoids treating all weathering as a CO2 source.
- Exact annual-mean differences are used before rounding: MLO growth 3.035 and SPO 2.825 ppm/year. Rounded displayed
  swings and ranges match the spec. Station toggles keep fixed axes, so toggling never silently rescales a comparison.
- The NOAA source page confirms early 2023 MLO observations were collected at Maunakea during the Mauna Loa closure;
  a data-method note preserves that detail. BRW and SPO source URLs were not accessible in the web verifier; their
  supplied snapshot values are retained. Cold review accessed all three current files directly on 2026-11-08;
  all 36 monthly observations match. Review copies are review-noaa-BRW/MLO/SPO.txt in Scratch.
- Browser narration is the fallback. calm-professor and all fixed lines are prepared in voice/lines.json; no recordings
  were made, as the Build instructions require. The kit chooses the installed browser voice, so its timbre is not
  guaranteed to match the named bank voice until recordings are supplied.
- Bar tools were bundled into scoped mirrors under Scratch. Original bar-tool folders were not written.

## Sensitivity

The tool shows a muscle fiber and metabolism, so a reviewer should check biological clarity and the distinction
between a chemical model and health advice. There are no people images, diet claims, body judgements, cultural narratives,
religion or hard history. Utqiagvik is named as NOAA's Arctic station location; no cultural claim is made about its community.

## Art

Fifteen generated assets: five scenes, two cells, five round passport vignettes and three station landscapes.
Air stamp was redrawn to remove landscape. Arctic and South Pole station paintings were redrawn to remove mountains
and establish correct flat polar horizons. Station buildings are generic illustrations, not documentary site photographs.
Cutout stamps use the supported despill treatment. Every asset has people:false. Original selected PNGs are in art/raw/.
Atoms, glucose fractions, waste piles, accounts, bars, ledger and chart remain in code because they count or move.

## Engine changes wanted

kit/data-desk.js, Chart.drawXY: implement groupBy, groups and groupLabels for line charts, splitting the numeric y
column into independent station paths with series shapes and dash patterns. It currently connects rows across groups
unless the consumer pivots them into separate columns. This tool uses the supported pivot workaround; no engine was edited.

## Verification evidence

Independent formula parsing and numerical work are in numbers.json and prepare.py in Scratch. property.js exercises
stock conservation, input refusal, destinations, percentages and all oxygen work combinations. Driver JSON files,
per-size layout readings, voice logs, frames and audit output stay in Scratch. Read codex-report.md for final results
and limitations. Cold review is the next phase; no polish round was started in this session.

The full audit ran once, exited successfully after about 33 minutes, and produced 99 frames and 132 mechanical leads.
audit-dispositions.md and .json answer each lead individually. All 99 frames were reviewed in state contact sheets;
flagged Oxygen ledger frames were also inspected at native size. The table overlap leads are older rows passing under
opaque sticky headings and totals, not visible overprinting. No audit runtime exception occurred.
The audit's 375 px iframe lookup failed. Separate hosted drive checks exercise that actual 375 px iframe directly.
Post-audit changes are limited to its findings: label separation, singular grammar, minimum Read width, Soil heading,
stable passport controls, and same-selection narration guards. Only the affected states are rechecked, not a second audit.

Focused held-click checks confirmed four repeated mode/scene selections preserve their complete introduction, the
Night-to-passport side path completes, and five wood Checks each queue and speak their own reveal. An Oxygen-off
event now queues behind its still-valid introduction instead of cutting it; the experiment itself updates immediately.
Read remains interrupting by design. A deliberate mode switch still discards narration from the previous mode.
voice-main-complete.json records the full seventeen-tap main path at the required two-second pace: all three mode
introductions, Oxygen-off event and scientist conclusion complete with no cut. The three-mode 375 px host checks
have zero global horizontal overflow and decoded images. Tables keep their own horizontal scroll at that width.
The final owned-process inventory found seven preview hosts that Windows taskkill had silently left running.
They were identified by exact drive.py energy-accountant --host 8785 arguments and the verified repository cwd,
then terminated with psutil. No owned Chrome remained; all assigned ports are now closed and host.html is removed.

## Cold review, 2026-11-08

Review repaired visible nitrogen provenance, scene-carbon bar scaling, night narration, wood prediction hints and stale subview speech. The passport now has connected stamps, a current C marker and a shaded code fuel token. Compact oxygen icons show the full drawn count, label the numerical remainder and keep waste clear of cell art. All fifteen paintings remain. Review evidence and audit dispositions live in Scratch; codex-review.md is the review record.

Current NOAA monthly files and all nine annual references were independently verified. The one audit completed within 40 minutes. Its saved overlay/scroll/welcome leads were confirmed against frames and the baseline. Voice-transition guards were subsequently rebuilt and checked with held clicks, repeated events and the complete main path. The 36-line voice inventory also includes the fixed Read hints, verified against default and refusal playback. No new feature, kit edit, second audit or commit.
