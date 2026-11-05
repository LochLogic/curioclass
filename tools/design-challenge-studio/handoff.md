# Design Challenge Studio handoff

Build only. No commits, deployment, or polish round.

## Source map
src.html starts from the kit starter. It uses kit:curio and kit:theme-912. Styles adapt the studio wall, four stations and painted option tiles. Data, model functions, station renderers and input handlers follow in that order. Only station changes replace whole layouts; live options, sliders and sort buttons remain in place during their input.

The art bank ensures each painting is bundled once and reused by rendered controls. prompts.json preserves the four existing assets and records sixteen generated assets and raw originals. There are twenty named assets in the spec, despite its stated twenty-one count.

window.__tool exposes the required state plus the two model functions, scoring, Flip finder, save action and voice log. Scratch contains independent Python arithmetic, browser recipes and evidence. The kit handles sound, motion and narration. No recordings were made.

## Tricky parts
The heat model uses explicit Euler steps of sixty seconds for three days. Air conditioning applies only when the current room temperature exceeds 26 degrees and is capped at 10.5 kW and the energy needed to reach 26 after passive gains. This reproduces the spec's 26.54 degrees and 31.01 kWh.

Only passing designs establish each column's normalization range. Full precision is retained until display. The all-equal rule assigns ten, including a one-design scale; the UI still asks for two designs before comparison. A tie changes the Flip finder outcome. The smallest integer distance wins; equal distances search down before up.

Cloudy water chemical protection drops unless a cleaning step precedes it. Microfilter followed by disinfection gets the specified combined rating. The clear-source combination is symmetric. All saved water designs retain their source and step order.

Water totals use the sum of the listed step times, the highest ordinal cost level, any fuel requirement and the least favorable taste category. The spec does not give a complete numerical cost or taste aggregation. These are labeled classroom categories rather than sourced money or measured taste. Chlorine dioxide shows the possible longer contact-time total as well as the minimum batch estimate.

Local storage is guarded with try/catch. Student text is escaped before insertion into markup. The Why explanation is never persisted. Device storage can be unavailable in a managed school browser.

## Open questions resolved
- Keep Challenge 3 saved locally, as the spec leans. Show that it never leaves the device and provide Clear my challenge. The Why box remains session only.
- Keep the invented, rounded room and option costs. Label these classroom assumptions on screen and in teacher notes rather than substitute real procurement data.
- Keep the water simulation framing, local-guidance note, no nitrate/lead-removal warning, high-altitude boiling note and product-label waiting caveat. This does not claim to validate actual household treatment.

## Engine changes wanted
No kit engine change is required. Shared kit and scripts were not changed.

Optional audit helper change: scripts/audit_tool.py, MODES_JS. Include .station-nav button[data-station] in mode discovery, retaining the current header selectors. The spec puts station tabs below the header, so automatic mode control walks do not discover them. Seven explicit audit states plus separate held-input runs cover them here.

Optional audit resilience change: scripts/audit_tool.py, run. Save a checkpoint report after size, state, calm and control-walk phases, before resize stress. A later Chrome disconnect currently loses all accumulated lead results even when all sixty screenshots already exist. Preserve completed checks on an interrupted connection.

## Build verification notes
The named art set is twenty assets: the retained classroom, stream, river and rain-barrel paintings, plus sixteen new assets. The two water treatment paintings with key spill were redrawn once. Finished art totals about 375 KiB.

The independent Python run checked all 256 room combinations and all 1,296 four-criterion weight combinations. Browser room outputs matched Python at full precision. The insulation value rounds to 37.10 degrees, compared with 37.09 in one spec line. The room update and redraw peaked below 7 milliseconds in the thirty-action probe.

Changing the comfort line recalculates every saved room design at the same threshold, so the hours column remains comparable. Existing custom designs missing a newly added item display No value and are excluded until replaced with complete evidence.

The shared host at 127.0.0.1:8785 was serving another build during later phone checks. Invalid phone frames are preserved as failed test evidence. Valid final phone checks use a local srcdoc iframe with the real 375 by 812 viewport. The mechanical audit uses the same assigned host port on 127.0.0.2 via a Scratch wrapper that changes only the test host address. The other build's server was left alone.

## Final audit handoff
The full attempt on Chrome 9981 lost its connection during resize. One smaller retry on unused Chrome 9987 completed, omitting the optional control walk. It produced nineteen grouped leads: eighteen were fixed and verified in targeted states; the phrase Design 1 becomes top was a false count warning. The automated full control-walk aggregate remains a cold-review check, while separate real-input, voice, keyboard, drag and model checks passed.

Scratch/audit-dispositions.md answers every lead. Scratch/audit-snapshot-to-final.diff preserves the completed audit snapshot-to-final changes. Scratch/build-evidence.json records the final bundle hash and size. Scratch/frames-looked-at.json lists the inspected frames. All Scratch references mean S:/CurioClass-codex/_scratch/design-challenge-studio/.

## Review next
Cold review against spec.md and codex-report.md. No polish round has started.

## Cold review changes
Untyped custom inputs now share the 44-pixel input styling; the compact custom Criteria form stays visible. Card placement restores focus; Reset returns focus to its challenge card. Invalid limits keep the last valid value and explicitly say so, with word ratings beside the germ limit. Returning hints name controls for the actual challenge, including an empty custom-evidence state.
Saving now names the saved design immediately and refreshes the custom table without replacing the active input. Missing custom evidence is printed as No value. New narration lines are in voice/lines.json. The microfilter was redrawn for a simpler silhouette and distinct tube paths, with its old WebP preserved in Scratch.
Water time comparisons explicitly use minimum estimates. Spec question left open: clear-source chemical-then-microfilter gets the combination bonus under the supplied rule, while current CDC guidance specifies filter then disinfect. Do not silently change that teaching rule without revising the spec.

## Cold review final audit
The single full review audit finished on Chrome 9951, host 8755. Four grouped leads: Reset could cut the first welcome on a rapid second tap, now fixed by leaving the already-reset start screen in place; an implicit input label was made explicit; Design 1 becomes top is valid grammar; the custom resize lead compared timestamp IDs between fresh pages. A focused live-iframe resize confirmed the same controls remain connected and enabled.
Final targeted checks cover these changes and the Check sort summary/action, visible compact feedback, single-line compact totals, and phone table badge wrapping. They pass. The full matrix was not repeated after these small repairs. Browser speech remains the fallback; no audio was recorded. See codex-review.md and Scratch/review-audit/audit.md.
