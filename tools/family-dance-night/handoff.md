# Family Dance Night build handoff

Built November 2, 2026 in S:/CurioClass-codex. Build only. No commit, branch change or polish round.
Only tools/family-dance-night and _scratch/family-dance-night were written.

## Structure

src.html starts from kit/starter/src.html and loads kit:curio plus kit:dance. Permanent panel controls precede the stage in the DOM. Tool code holds seven source-content records, fourteen move keyframe sets, the voice table, figure decorations, responsive room, run lifecycle, original ensemble timbres, map and favorite handlers. world.json is the existing local Natural Earth land outline reused without country borders, rendered in Equal Earth projection. The data is bundled inline.

Each new run, tab switch, favorite panel or return stops the old play, clock, music and speech. runId invalidates delayed speech cleanup. Copy uses Dance.mirror with model facing zero; turning moves rotate the pose's yaw inside that class-facing model. The count-in starts the sequencer only at dance count one, avoiding the engine's negative-position loop wrap. Read waits until the first dance count if a count-in is active, then stops the run and reads. Slow uses the engine's next-count tempo change.

Word chips use the last shown move or both moves for a full Watch loop. While music is running, answers wait until the next count. Music is lowered about 6 dB during narration by reattaching the same kit track at half volume; tool timbres use their output gain. A speech generation counter prevents an older completion from raising volume under a newer line. Sound off leaves the clock intact. Motion off samples props and figures once per count and removes light pulses.

Table lights and favorite choices live only in memory. Shared kit Motion remembers its preference. All seven first returns brighten the room and play the final event line. No class data is stored or transmitted.

## Owner's painter decision

Final dancers must be painted. The current kit figure is temporary, explicitly authorized by the owner. No people, faces or body parts were generated. Fourteen painted non-person assets were generated with the built-in image tool. Full prompts and house style are in art/prompts.json; PNG originals are in art/raw; final cutouts came from scripts/art.py with --rekey only.

createFigureRenderer is the renderer boundary. Retain the Dance.dancer model and subscribe to onMove, then hide model.g and replace overlay with the painted rig or phase atlas. The model supplies screen joints, root position, pose, facing and grounded support. Keep current timing and mirrored Copy poses. Renderer.spriteNames gives the two manifest names for that dance; each has an explicit art token and people true in prompts.json. These deferred assets are deliberately not loaded as draft placeholders.

There are fourteen deferred people assets, one per move, each requesting the needed phases. Include full-length readiness and the A/B keyframes, alternate foot support for stamps and hops, raised and lowered skirts/fans, front-quarter-side-back turning phases, lion low/high and bow/blink phases, and four visible lion legs under one costume. Preserve the specified clothing colors without treating them as a universal costume for the community. Scratch pose-contact-A.png and pose-contact-B.png show current shapes; the source keyframes are the exact phase reference. Painted assets must remain within the final 2 MB bundle budget.

The contact sheets are in _scratch/family-dance-night/frames. Art contact review is _scratch/family-dance-night/art-contact.jpg.

## Open questions and specification decisions

- Cultural review: take the spec's implied recommendation for a review of all seven dances, props, descriptions and movement simplifications. BASELINE rule 5 resolves the mechanism: a fresh review agent before release, without waiting for outside reviewers. This Build run is not that cold cultural review. No extra agent was spawned.
- Painted dancers: the owner's explicit decision supersedes the spec's final use of code figures. The code figures remain only until the next painter and owner review.
- The specification asks the builder to add this tool to docs/families/dance.md. The write boundary forbids editing docs, so the exact registration request is below.
- The explicit move word lists contain 41 pairs, not the stated 38. All per-word totals in the spec sum to 41 and were retained. Loop durations, 60 percent Slow and the four contrast ratios recompute correctly. Scratch numbers.json has the calculations.
- No recordings were made, as CODEX-BUILD.md directs. All fixed lines are in voice/lines.json using bank clear-teacher / Iapetus and browser-speech fallback. The bank voice is the intended future recording voice, not a claim that the browser can select Iapetus.
- The user's stop-on-report instruction takes precedence over the brief's early-report advice. codex-report.md is written last; intermediate evidence stays in Scratch.
- The bar tools were bundled into Scratch, avoiding writes to their tool folders, and opened in muted Chrome. Their sources and existing art were read only.

## Engine changes wanted

- docs/families/dance.md, What each tool brings table: add family-dance-night, K-2, square floor; seven dances and two lion figures; fourteen mirrored pose phrases; clock, music, counts and icon; family tables, dance words, origins and room lights. Also update the four-tool count. No shared engine change is needed for this build.
- kit/curio.js, init Motion handler: an optional in-memory preference would allow a literal no-storage tool to avoid curio-motion while keeping the shared Motion button. No kit edit was made.

## Validation and next step

The final report records the bounded test batches, frames inspected and the single mechanical audit's disposition. Scratch contains commands, shot lists, logs, numeric checks, pose sheets and audit output. Browser runs use Chrome ports 9970 to 9977 only; iframe hosting uses 8775. Every browser and server started by the build is closed after its batch.

The next workflow is a separate cold review, including cultural-content review and a listening review of the synthesized ensembles. Do not infer cultural authenticity from a passing mechanical check. Install the painted dancer set at the renderer boundary, then review its poses and the remaining offline size budget.

The single audit completed in 693.5 seconds with exit zero and 16 leads. Nine concern the intentionally hidden panel #hint while the gym's visible #home-hint owns Read. Seven concern the intentionally skipped gym welcome when the first table tap speaks its own name, as STANDARDS requires. All states, resizing, focus, calm animation, repeated clicks and console checks were clean. Manual held-click logs additionally cover the interior controls.

After the audit, the ceiling light layer moved behind the dancers so raised fans and umbrellas remain visible on a phone. The focused phone prop frames and a laptop fan frame were rechecked; the full audit was not rerun for this layer-only change. relayout reserves more space above fan and umbrella figures by using a 0.45 height fraction; other figures use 0.53. Keep that prop clearance when installing the paintings.
