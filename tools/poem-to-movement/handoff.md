# Poem to Movement build handoff

## Structure

`src.html` starts from the kit starter, with a real-pixel responsive stage and a controls-first DOM. `content.json` is inlined by the bundler. It holds six profiles, highlight defaults and the two poem texts. The shared dance engine supplies floor, actor, poses, qualities, clock, counts, music, pathways and path recognition.

The tool's `basePose` adapter expresses the thirteen verbs. `createActor` and `paintActor` isolate the
painted renderer. Two generated atlases contain front and rear views of the same three children, one base
pose per child per view. SVG windows articulate their painted limbs at the shared engine's projected joints.
Card icons use the same painter. The hidden engine actor supplies geometry and a floor shadow only.
The cast is selected independently of the source and stored under `_cast` in this tool's local saved object.

To swap the figure, replace those two assets and the reference rectangles/joint anchors in `paintActor`, or
replace that factory while preserving the actor interface. Timing, qualities, pathways and scoring stay shared.
Both assets are marked `people: true`. The superseded 156 undrawn pose requests are preserved for provenance
in `_scratch/poem-to-movement/prompts-before-review.json`, rather than retained as missing art tokens.
The originals' detailed paintings and studio were kept. Contact sheets and pose checks are in review Scratch.

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

Cold review repairs and validation are recorded in codex-review.md. The original build record remains in codex-report.md. No commits or second full audit.

## Build verification and remaining limits

The one mechanical audit completed with 37 leads. It found no console exceptions, infinite motion or resize failures.
The report groups every lead's disposition. Only focused checks followed the repairs; the whole audit was not rerun.
Evidence is in `_scratch/poem-to-movement/`, including the full audit, numbers, held-input checks, frame sets and comparison.

All six defaults and the storm/rain river revisions passed. Real S and zigzag drags, live edits, backward/forward reorder,
Stop, keyboard creation, Alt-arrow reorder, partner concealment, Motion off and saved-work reloads passed.
Five Viewer plays produced five spoken result events with how lines heard once. The review rechecks the runtime line list against the recording manifest after instruction changes.

The short preview moves the six Viewer source cards below the studio so all are visible together. Both phone poems fit
with 44-pixel highlights. Counts live beside the move caption in Moves and Viewer to clear traveling dancers.
The phrase strip scrolls sideways as the spec requires. Start over and the closing sentence can need vertical scrolling
in short or phone layouts. The miniature Map studio is small in portrait layouts. Narration and synthesized audio still
need a listening review; all Chrome testing was muted. No recorded narration was made, per the build instruction.

## Cold review changes

Fixed stale Viewer results after drawing or clearing a map, retained still-relevant mode narration when Play
starts, shortened entry instructions, and made freeze keep the actual preceding pose without reapplying
different weight/level modifiers. Balanced quality averages are described as equal mixtures.
The result now lands in the studio caption as well as the Viewer's bubble. Model matching has no victory chime.
Partner choices require a complete phrase performance; a solitary card preview or skipped/reordered tail
cannot stand in for watching the whole phrase. Final review evidence and remaining limits are in codex-review.md.

## Sensitivity

Fresh cultural review should check the River's woodblock influence is named without claiming an authentic
Japanese artwork or representing a whole culture. Neither landscape is a historical reproduction.
Inspect both painted cast atlases and articulated low/turning poses for respectful bodies, natural skin tones,
believable prosthesis attachment and equal agency. The children are not tied to a source or stereotyped role.
Students may use their own comfortable seated or standing movement; no body type is graded.

## Spec corrections wanted

The spec's smooth/sharp Flow label disagrees with Gilbert's energy versus free/bound flow distinction.
Notes explain the limit; changing the required student control needs a spec correction.
Broad module anchors do not mean every grade 3-5 substandard is covered by this single-dancer tool.
The old family registration question remains outside the allowed write scope.

## Final audit layout repairs

The single review audit had 23 leads, grouped in codex-review.md. Map's four qualities now share one row,
which restores the desktop Reset at 680 and 1280 widths without reducing the scene. Viewer captions reserve
space for the eye badge and use a short subline so they clear the dancer's feet at 680 width.
Play is sticky while the panel/body scrolls, and the phone result explicitly directs the student to the
personal sentence. Secondary Viewer fields/Reset and the phone Map footer can still need vertical scrolling.
The specified compact phrase strip remains horizontal. All 51 audit frames were inspected; only affected
layout frames were re-shot after the audit. No second full audit was run.

## Saved map slot repair

`state.map` is aligned with cards and contains null for an in-place move. Restore and reorder must preserve
those slots. Filtering them out shifted subsequent travel onto the wrong card. The final real-drag save,
reload, in-place-card reorder and second reload checks preserve all geometry exactly. Evidence:
`_scratch/poem-to-movement/map-slots-*.json` and `map-slot-frames/`.
