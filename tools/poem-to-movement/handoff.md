# Poem to Movement build handoff

## Structure

`src.html` starts from the kit starter, with a real-pixel responsive stage and a controls-first DOM. `content.json` is inlined by the bundler. It holds six profiles, highlight defaults and the two poem texts. The shared dance engine supplies floor, actor, poses, qualities, clock, counts, music, pathways and path recognition.

The tool's `basePose` adapter expresses the thirteen verbs. `createActor` is the single replacement point for painted dancers. The future painter has 156 people requests in `art/prompts.json`: thirteen verbs, three levels, light/strong weight and two keyframes. Actual generated images contain no people. Keep the code figure until those assets have owner review; do not replace the destination with permanent code art.

Light-weight pose reference samples are in `_scratch/poem-to-movement/candidate-frames/pose-guide-a.png` and `pose-guide-b.png`.
The four generated non-person images include a painted empty studio, added because the code floor alone looked flat.

Every people asset has a reserved art token in `PAINTED_POSES`, exported as `__tool.paintedPoses`.
Actor frames carry `artKey`, `artPhase`, `verb`, `weight`, `level` and `flow`; the current kit actor ignores those extra fields.
A painted adapter should keep the previous painted frame for freeze, rather than substituting a standing freeze picture.
Deduplicate shared poses or pack a pose sheet when painting so the final bundle remains below 2 MB.

## Open question decision

The catalog says family none, while the spec explicitly requires the dance engine. Kept the catalog untouched and used the dance engine, following the spec's leaning and KIT's shared-engine rule. A catalog/family-doc update remains outside this tool's allowed write scope.

## Source fidelity

The Gutenberg Rossetti edition reads “bow down their heads,” so the highlight is “bow down,” matching the spec's content table. Train uses the first eight lines, as requested; a comma after “battle” was removed to match Gutenberg. The script's independent numbers agree with all Source arithmetic, including 21 ties among 96 homogeneous phrases.

Rossetti's “thro’” is preserved on the poem card and maps to the content table's expanded “passing through” move label.

## Tricky parts

Quality changes are staged until the next count. Reordering seeks the moved card's new slot at the next count. Motion off samples once per count without shortening playback. Stop cancels the clock and music immediately. A source switch, step switch and reset also hush narration and source sounds.

The map uses a top-down affine floor projector with `Dance.readPath`, so its geometry is judged as drawn. Floor coordinates are padded and clamped. Default paths are regenerated from card choices; drawn coordinates are stored separately. Path-count ties use the declared Straight, Curved, Zigzag order for deterministic results.

A long single part splits continuously between traveling moves. If the drawing has more parts than traveling moves,
the moves take the first parts in order. Backward live reorder seeks are deferred to a microtask after the clock tick.

How lines use Curio.voice, with state-scoped validity and repeating result events. No voice recordings were generated, per the build-only brief. The selected bank voice is gentle-storyteller; browser fallback may sound different.

## Engine changes wanted

- `kit/dance.js`, `floor().draw`: add options to hide the studio barre and choose marley rather than planks. The tool removes those decorative nodes after resize without changing the shared engine.
- `kit/dance.js`, `phrase().at`: expose a pose function for custom verbs, live speed/weight edits and freeze of the actual previous pose. The tool samples the shared phrase's travel and uses its own pose adapter at the shared clock's position.
- `kit/dance.js`, `floor().resize`: allow dancer height below 18 floor units for compact preview proportions. The tool scales the actor down from the minimum when needed.

## Next

Cold review is next. This is a Build only run. No commits or polish round. Verification results and unresolved limits are in codex-report.md.

## Build verification and remaining limits

The one mechanical audit completed with 37 leads. It found no console exceptions, infinite motion or resize failures.
The report groups every lead's disposition. Only focused checks followed the repairs; the whole audit was not rerun.
Evidence is in `_scratch/poem-to-movement/`, including the full audit, numbers, held-input checks, frame sets and comparison.

All six defaults and the storm/rain river revisions passed. Real S and zigzag drags, live edits, backward/forward reorder,
Stop, keyboard creation, Alt-arrow reorder, partner concealment, Motion off and saved-work reloads passed.
Five Viewer plays produced five spoken result events with how lines heard once. The 75 runtime lines match the recording manifest.

The short preview moves the six Viewer source cards below the studio so all are visible together. Both phone poems fit
with 44-pixel highlights. Counts live beside the move caption in Moves and Viewer to clear traveling dancers.
The phrase strip scrolls sideways as the spec requires. Start over and the closing sentence can need vertical scrolling
in short or phone layouts. The miniature Map studio is small in portrait layouts. Narration and synthesized audio still
need a listening review; all Chrome testing was muted. No recorded narration was made, per the build instruction.
