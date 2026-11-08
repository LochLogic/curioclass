# Grid Operator build handoff

## Structure
`src.html` starts from the kit starter and uses the shared 9-12 theme and Curio.voice. The local script holds plant inputs, a pure `simulate(plan, week, coal)` function, fleet rendering, playback, a canvas chart, device storage and comparison rendering. No family engine is specified.

The pure model returns all 168 hourly rows, cumulative scores and the tripped unit. Run reveals that record rather than maintaining a second solver. Saved-plan comparison recalculates all three weeks and never trusts stored score claims. Tests can read `window.__tool.state`, the requested top-level getters, `simulate`, `comparisons`, `challengeResults`, `allLines` and `vlog`.

## Open questions resolved
- Keep the specified AEO2023 build costs, historical fuel inputs and supplied annuity factors. This is a comparison model. The cost-date note is visible on the laptop Plan panel and repeated in teacher notes; compact Plan prioritizes the fleet controls.
- Keep paid-off existing coal and the three separate scores. Do not add policy or a carbon-price slider. BASELINE rule 9 mentions that slider, but the detailed spec explicitly leaves it open and defines no slider range, rate or accounting. This is a direct contradiction, resolved toward the complete tool-specific design.
- Give unserved energy no dollar value. Reliability stays a separate measure.
- Treat Pause as holding the current hour, following the explicit Pause behavior and Done when 8. The sentence "Pausing and changing week chips resets the run" conflicts with those instructions. Week changes reset; Pause does not.
- Default battery charging can store renewable surplus only, limited by renewable output. Unavoidable nuclear and coal excess is spilled after curtailment. This resolves the default label against the broader "surplus charges the battery" wording.
- Run's weekly coal toggles are experimental commitments, separate from a saved fleet. Compare commits every retained coal unit on for all three tests. The interface and notes state this assumption.
- Wind and solar share is accepted renewable generation divided by served energy, including renewable charging input. It matches the worked examples; discharge is not counted a second time. This is not a lifecycle energy attribution.
- The literal lowest-value "best" rule also marks the lowest renewable share. The hint and table note explain this. It does not mean a low share is a policy recommendation or that one fleet wins all criteria.
- At 375 pixels, Plan uses two columns in a scrolling fleet editor so the paintings and 44 pixel controls remain legible. Run week, Save plan, charging and the hint stay visible. Compare similarly keeps its controls and hint outside the scrolling evidence table.
- The user requires stopping when codex-report.md is written. The early report scaffold was therefore prepared in Scratch; the tool-folder report is written once, at completion.

## Spec and source discrepancies
- EIA Electric Power Monthly 6.07.A lists 2024 natural-gas turbine capacity factor as 13.9 percent. The spec's 19.9 percent is the adjacent natural-gas steam-turbine value. The peaker card uses 13.9 percent, with no change to dispatch or reference scores.
- The spec labels the entire nuclear cost input as Table 8.4. That table supports 2025 fuel at $6.64/MWh, while $2.67 variable upkeep and $136.91 fixed upkeep come from the AEO2023 large light-water reactor row. The SMR row instead gives $3.38 and $106.92. The supplied $9.31 modeled rate and upkeep are retained for both sizes, while new construction uses the SMR capital cost. This mixed technology assumption needs owner review before release.
- Weekly capital displayed on cards is recomputed from build cost and the explicitly rounded annuity factors. This differs from some rounded table cells by a few dollars, for example nuclear $1,293,870 versus $1,293,877. Full dispatch results reproduce the specified rounded totals.
- The Plan cost-date note corrects the spec's "fuel 2024" statement: nuclear fuel is the 2025 value; coal and gas use 2024 values.
- A heat-wave trip cannot remove capacity from a fleet with no fossil plants. The banner says that no output is removed, and no nonexistent gas-unit trip is narrated. A CC fleet smaller than 200 MW loses only its available MW. No numerical reference case changes.
- Build-only overrides older BUILD.md wording to avoid drawing art. Nine new paintings were generated with the image tool. Original control-room.webp and skyline.webp and their original prompt/provenance records are preserved alongside the new go-prefixed set.
- The reference tools already had bundles. They were opened as supplied to honor the stricter write boundary rather than rebundled in their folders.

## Art
Nine go-prefixed assets are used: control-room backdrop, skyline strip and seven plant images. No asset shows people. All are in `art/prompts.json`, with `drawn_by: codex`. Full image-tool prompts and generated paths are also preserved in Scratch. New raw PNGs are in art/raw; the permitted `art.py --rekey` converted them. The system Python uses the existing TTS environment's site-packages for image processing because the other Python executable could not launch in this sandbox.

## Sensitivity
None of the specified cultural, religious, hard-history or body topics apply. Fuel CO2 is direct combustion CO2 only; the visible model note lists excluded social and environmental factors. This is not advice for a real grid design.

## Engine changes wanted
None confirmed. Before changing scripts/audit_tool.py's Audit.size child-context lookup, verify host ownership and the served root. The LibreOffice Python launcher left four actual python-core/bin/python.exe host children alive after launcher-based taskkill. All four had the exact grid-operator --host 8765 command and this workspace as cwd; they were closed using the verified process identities. Multiple hosts on the assigned port are a plausible cause of the audit's missing iframe context, rather than a demonstrated Audit.size defect. Separate same-origin phone frames/checks worked. Scratch owned-host-cleanup.json records the identities, and close_owned_hosts.py performs the scoped cleanup. No shared files were changed.

## Review next
See codex-report.md for measured validation, frames, remaining limitations and the one final audit's dispositions. No commit, deployment, recordings or polish round was performed.

The full audit finished with 44 leads and began before the last repairs. It is not a clean final snapshot. The focused lead JSON files and frames, main/side voice walks, repeated-event records and quick-tap narration checks in Scratch document the repaired behavior. The original audit's whole-table keep leads are intentional scrolling regions, not missing metrics.

## Cold review changes
The cold reviewer played Plan, all three weeks, empty and populated Compare before reading the builder files.
Escape and Reset now restore the appropriate next-action hint; Reset restores the closed challenge drawer.
Build-limit taps explain their bound without resetting a run. Save states device-only storage on its button.
Plan keeps historical cost dates and the SMR/large-reactor upkeep assumption visible in its footer at compact sizes.
Compare states its retained-coal and lowest-value badge assumptions above the evidence. The spec-mandated lowest renewable-share badge remains a teaching concern requiring a spec decision.
Short landscape challenge actions share a row so all four cards remain visible.
The scorecard now shows the actual peak-covered or worst-gap hour, using existing skyline art and a proportional supplied/demand strip.
Queued run-event narration expires at completion. The ten fixed narration lines remain unchanged.
Wind was redrawn using the built-in image tool. Its final full prompt is in art/prompts.json, raw in art/raw/go-wind.png, final in art/go-wind.webp. All nine used pictures were inspected, with no people.
Review evidence is in _scratch/grid-operator; the final review report records the audit and unresolved spec choices.

Confirmed audit repairs: challenge notes are explicitly 10px. The completed-run Scorecard control replaces the inactive Step hour slot in the top toolbar; Replay or a new week restores Step. This keeps reopening the report above the fold at 680px and on phones. The neutral supply-and-demand heading also remains accurate during shortages. The audit snapshot predates these narrow repairs; targeted post-audit frames verify them.

The review audit completed within its 40-minute limit with 23 leads. Six grouped UI leads were repaired, two concern the intentionally scrolling comparison, thirteen are permitted first-edit welcome staleness, and two are the phone execution-context harness gap above. Thirteen post-audit frames/checks pass with no console errors: reopened Scorecard at every standard size and phone, challenge notes/card visibility at affected sizes and phone, and keyboard focus after stepping to the final hour. Focus transfers to Scorecard only when hiding the completed Step control would otherwise leave focus on the body. The final review report names the remaining spec-bound badge/challenge concerns. No second audit was run.
