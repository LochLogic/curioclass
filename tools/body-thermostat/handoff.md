# Body Thermostat handoff

## Structure

src.html starts from the kit starter, uses curio, theme-912 and Plane. CSS lays out an outdoor thermal instrument,
with separate Lab, Experiment and Fever emphases. The single rates function feeds one-second Euler integration,
the body colors, sweat beads, insulation band, vessel state, gauges and notebook trials. Trial snapshots are copied
before integration; they never mutate the live clock. ResizeObserver rebuilds the Plane at real pixel dimensions.
The trial animation is a reveal of completed evidence. New trials and Compare interrupt it without losing a row.
The notebook persists only in memory. No score, grading, accuracy badges or saves exist.

## Decisions and open questions

- Safety copy follows CDC urgency: suspected heat stroke needs emergency care (911) and cooling; hypothermia needs urgent medical help.
  The model stop is explicitly separated from a diagnosis.
- Kept the code-drawn, faceless thermal silhouette because its colors and effects are live model data.
- Used the requested image tool rather than the spec's older local-FLUX route. Art was made in two four-panel sheets,
  cropped to individual raw PNGs, then processed only with art.py --rekey. All eight prompts and provenance are in art/prompts.json.
- Fever has its specified target and clock controls. It holds Lab's environment; return to Lab to edit those conditions.
- Reset in Fever follows the spec's detailed reset rule: after Fever starts, Reset sets core to the current fever target.
  Mode changes always reset core to 37; they remember Fever's target, settings and the page notebook.
- The overview says Reset returns to 37, while the detailed rule allows the current fever target. That includes 40°C,
  which is also the safety boundary. The detailed reset wins; at 40°C it immediately safety-locks. The hint says to lower
  Set point before Reset so this cannot bypass the boundary.
- The spec says shivering starts 0.2°C below target "after vessels have tightened". The formula, rather than a separate delay,
  determines timing. The whole loop uses its written formula without new physiological mechanisms.
- On a phone, controls precede the scene. Experiment puts the notebook toolbar above the thermal strip and graph so Compare stays in view.
  Evidence rows and details can scroll. Short landscape keeps controls and scene side by side.
- The spec's exact exercise heat percentage is not supported by its cited OpenStax section. Activity watts remain labeled model values.
- Live source verification found ASHRAE F21 SI chapter 9 uses 3490 J/(kg K), not the spec's 3470, and rounds evaporation
  heat to 2.43 million J/kg rather than 2.426 million. Kept the explicitly labeled model constants and worked-case behavior;
  flagged the attribution mismatch instead of silently changing the specified model.
- Heat stroke temperature is worded as a "sign", not a standalone diagnosis. The model's 40°C stop remains as specified.
- OpenStax 24.6 covers the feedback responses, but does not directly cover fever's raised target. A source cross-check
  for that already-specified teaching claim is NCBI Bookshelf, StatPearls, Physiology, Fever (NBK562334).
- Chills and fever-break speech have state validity checks: repeated taps cannot claim a normal core when it is already warm,
  or claim sweating when the core is still at 37°C. The hint always gives the next action.
- Optional Suggested trials list omitted. The teacher start gives one controlled pair without introducing a new feature.
- Trial reveals are instant with Motion off, following the spec's explicit trial instruction; the live physical clock keeps its chosen speed.

## Sensitivity

This tool discusses people's bodies, fever, heat illness and cold exposure. A fresh reviewer should check the calm
safety copy, threshold context, and absence of body-size or fitness judgments. The 60 kg mass is a model assumption.
The thermal silhouette is faceless and not a body ideal. No people appear in any generated asset.
The simulation is educational, with deliberately simplified constants; students must not perform the extreme scenarios physically.

## Engine changes wanted

None. No shared engine files changed.

## Media readiness

Eight images are painted and placed. Voice text is ready for soft-breath, but the fixed recordings remain for the later media pipeline.

## Build test cleanup

This machine's LibreOffice Python launcher left host child processes after the parent was closed.
Scratch/close_owned.py matches only body-thermostat with --host 8775, or this tool's exact Chrome profile path.
It closed the five retained host process trees. HTTP then refused the host connection; host.html was removed.

## Cold review, 2026-11-08

- Run trial pauses the live clock so a hidden simulation cannot raise a safety stop over a trial.
- Trial safety panels appear only when the boundary sample is revealed, with their own recorded-trial wording.
- No response active is distinct from Balanced; balance now requires net heat near zero.
- Set-point hints track the actual target and name Pause while the clock is running.
- Re-entering Fever or resetting at a remembered high target uses that target's hint rather than asking to raise an already high target.
- The CDC fever figure is explicitly a screening threshold; high temperature after exercise does not establish a fever diagnosis.
- Experiment's recipe says on or off so it still fits when the student returns with every response already off.
- Compare gives a shared-time temperature difference and a once-per-load spoken guide to reading the traces.
- CDC-based copy names emergency heat care without diagnosing heat stroke from a number; no physical exposure time is implied.
- Kept the eight coherent paintings and enhanced the weaker loop panels with instrument shading and hardware details.
- Current Compendium jogging/running METs differ from the spec. Kept prescribed watts, documented the discrepancy in notes.
- Chrome uses 9940 to 9947; host uses 8745. Review evidence stays in Scratch.

## Cold review verification

One complete audit finished within its 40-minute limit. Its 56 leads are classified in codex-review.md.
All 39 audit frames were inspected. Post-audit checks cover the small copy/hint refinements and a fresh main voice walk.
The apparent dropped cold-response line plays at 22.239 seconds; the audit's quiet window is only 15 seconds.
The final 24 fixed lines match voice/lines.json; no recordings were made. Independent cases A-L and four extremes match.
All assigned review Chrome ports and host 8745 are closed; host.html is absent. No shared-engine changes or git commits.
