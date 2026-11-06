# Scene Staging Comparison: handoff after cold review

## Structure
One offline src.html with kit:curio. CSS lays out the theater-program desk; the script holds captions,
timing/staging tables, vector actors, synthesized cues, two-viewer storage, split ranking and six layers.
The four original paintings remain. The blue-overall costumes are now also visible on every modern actor.
window.__tool exposes state, content, timeline and focused verification hooks.

## Tricky parts
- Each duration is pause + whitespace caption words / 2.5 + 1 second. Final counts are
  18, 15, 12, 12, 10, 8, 17, 14, 6, 15: 77.3 seconds and 63.0 seconds. The status derives its total.
- Next/Previous preserve playback and cancel the preceding moment's audio. Mode changes stop playback.
- Reactions keep the latest three entries including duplicates; symmetric differences count distinct types.
- Production comparisons use the current viewer's two sets, 0 to 5. Viewer comparisons compare matched
  productions first, counting only productions with both viewers' stamps at that moment, then sum, 0 to 10.
  This resolves the spec's unspecified viewer aggregation without letting production swaps cancel.
- Earlier moments break ties. Zero entries may rank in the top three, but never receive a difference mark.
  Missing stamps are unrecorded evidence. Sample rows never inherit personal split marks.
- An opinion requires the current viewer's own stamp on that production/moment and nonempty text.
  Saving is not semantic grading. Neutral feedback asks students to check their evidence; it certifies no answer.
  Compare now starts its opinion selectors at the inspected production/moment. Viewer changes clear unsaved text.
- Stamps, chips and six shared opinions save locally in try/catch. Reset uses a confirmation dialog.
- No narration over playback. bothDone describes having reactions, not having watched the whole scene.
  stampHow stays a visible hint at eight seconds because the spec forbids narration while playing.
- Read stops the scene, then the kit reads the current hint. New viewer selections hush stale viewer narration.
- Vector initials link each moving actor to its legend. The farce faint has a short fall/bounce and floor impact;
  the hopping actor travels around the chair and the crawling exit clears the stage. Calm removes motion,
  keeping the final pose, pauses and duration. The two plays remain fixed, not student-directed.

## Spec choices
The fictional 1890 production borrows a realistic style associated with the Moscow Art Theatre a decade later;
its time card states the anachronism. Historical audience responses are framed as possible interpretations.
Short landscape keeps two frames side by side for caption readability. Tall widths under 900 stack them;
375 shows one production. Compare's ten-column evidence table scrolls on phones. Secondary details scroll.
The final audit confirmed offscreen reason chips at several sizes and compact Reset below the fold.
Reason chips and their heading now sit with the layer tabs ahead of long evidence, while reaction stamps
stay with the evidence below. The compact panel puts Reset beside its privacy note and removes the redundant
viewer heading. See the review's targeted repair frames; the full audit was not repeated.
The shared-kit engine is unchanged. No recordings were made; smooth-narrator uses browser fallback.

## Sensitivity
Russian literature and property/marriage expectations: review framing, including the fictional 1890 label.
The characters' physical distress and forced engagement are plot elements, not medical or relationship advice.
Students can feel uneasy about the faint; no reaction is scored. Sample viewers are fictional individuals,
not stand-ins for all older people, farming communities or families with heart conditions.

## Art
Four generated paintings retained, with original provenance in art/prompts.json. Wardrobes use empty forms
and hangers, not people. Moving characters are faceless vector silhouettes, as the spec requests.
The review improves those vectors rather than replacing strong painted art.

## Engine changes wanted
None.

## Verification
See codex-review.md for the cold review and current findings. Evidence is confined to
_scratch/scene-staging-comparison, with review-prefixed checks and review-audit.
Original codex-report.md is the builder's historical record, not evidence of review verification.

## Final review verification limits
The cold review's one audit reached its 40-minute limit during resize stress checks. Its 21 recorded leads
are dispositioned in codex-review.md. The complete control walks and voice stress checks finished;
the entire resize matrix did not. Independent phone checks passed, while the audit's phone harness
could not attach on the occupied host port. No fresh full audit was run after scoped repairs.
The final compact hint rechecks require scrollHeight == clientHeight and no overlap with viewer controls.
Rapid Stop now cancels actor animations and freezes selected-moment poses immediately. Before repair,
the entrance drifted after Stop; focused 1366 and 680 tests now show zero animations and zero drift.
Opinion prose uses natural clauses for all five responses, blocking, personal experience and uncertainty.
The main voice walk reached all 20 production moments with Sound on and no narration over playback.
Read/stale checks and five held Add events are preserved in Scratch. No recorded narration was created.
All review Chrome ports are closed. The old test host on 8755 remains because process cleanup was denied;
host.html was removed. See the review report for this unresolved operational cleanup and evidence paths.
