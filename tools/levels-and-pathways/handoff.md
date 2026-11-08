# Levels and Pathways handoff

## Fix pass, November 4, 2026

The active merged list is refine.md. The fix evidence is in _scratch/levels-and-pathways/fix-before,
fix-before-parts-real, fix-after, fix-targeted, fix-extra and fix-walk. The final status belongs to polish.md.
No kit files, catalog files or sibling tools were edited. No commit was made.

Part controls now sit on their own parts, without leaders. Compact placements are planned together along the
actual part geometry so all four 64-pixel targets remain separate. The studio SVG is a labeled group instead
of an image role, exposing its controls. Guide bands select levels outside Mystery; Mystery disables them.

The painted rig adds rounded underpainting, folded-leg depth ordering, a hand-only green-alpha filter and
a head/neck limit. Low rest hands use solved knee-contact angles. The kneeling silhouette still needs an
art-quality check: these are corrections to an articulated T-pose, not newly painted kneeling illustrations.
No new raster or new people artwork was generated in this pass.

DA:Pr4.1.2a is removed from this tool's claims in src.html, spec.md and notes.md. Move it to choreography-board
for full teaching of facings, symmetrical and asymmetrical shapes, and circling versus turning. The integrator
must update the shared catalog and the receiving tool because those paths are outside this session's scope.

Copy me and bubble space are folded into the Levels welcome. The first move shape appears during the call.
The new Middle cue names body height. Mystery immediately shows the watching hint, teaches that a circle is
curved after round 7, and names Play again only after the gallery bow enables it. Runtime and lines.json
contain 49 identical fixed lines. Changed and added text uses browser voice fallback; no recording was made.

Mystery retains the spec's eight exact rounds and unlimited wrong-answer replays. It measures completion,
not demonstrated mastery. Blind answer enumeration must be reported honestly if it fills a progress dot;
do not add attempts, lives, a new task or a new scoring rule without a spec decision.

Cold review completed November 3, 2026 in S:/CurioClass-codex. No commit. See codex-review.md for the review outcome.

## Files and structure

src.html uses kit:curio and kit:dance. Permanent panel controls precede the stage in DOM order.
The script holds the narration table, six move libraries, pathways and eight exact Mystery rounds, the painted rig,
panel handlers, studio, run lifecycle, drawing recognition and responsive layout. Nothing in kit was changed.
The offline bundle is levels-and-pathways.html. tool.draft.json stays at stage built.

## Painted guides and swapping the figure

The single art/painted-dancers.webp atlas contains three adult guides: varied skin tones, hair and body shapes,
consistent teal clothing and cream shoes. Every person-containing asset has people true. The source sheet and
36 articulated move endpoints received a fresh people-art review. The raw painting is art/raw/painted-dancers.png.
The full built-in imagegen prompt is in art/prompts.json. The original studio painting is retained.

PAINTED_CAST contains landmarks and clip boundaries in the final 1536 by 707 atlas. paintDancer attaches painted
segments to a Dance.dancer model's projected joints. The model group is hidden; its clock, skeleton, grounding,
trails and pose library remain authoritative. The painted head keeps its shape under forward bends. Torso width
follows facing and twist. The main figure, its clipped mirror reflection and the button poses all use the atlas.
setCast swaps only the painted renderer. Each mode uses one consistent guide throughout its trips.

To replace a guide, replace the atlas and that guide's landmarks/clip bounds in PAINTED_CAST, then recheck standing,
raised arms, forward bend, floor shapes and travel. Separate static paintings for every keyframe are unnecessary. One separate painted-gallery-bow cutout keeps the
finished gallery bow readable when a flat puppet torso would be too foreshortened. It appears only at the bow
endpoint; the model still owns its timing, position, mirror projection and shadow.
The former 32 pose requests remain in the manifest as superseded history pointing to this compact rig.

## Review repairs

- Right-path praise survives an immediate level answer, including when it has not begun playing yet.
- During a Mystery return, the hint says to watch the dancer return, then names Go only when it is available.
- A running drawn dance locks its level/way selectors, so its planned badges and actual ribbon remain consistent.
- Editing or replacing a drawn path hides the previous performer and shadow until Dance it is tapped again.
- Mode changes, Clear and Surprise path cancel an unfinished pointer drawing safely.
- Clean floor cannot overwrite the next mode's hint after its fade completes.
- Badge placement reserves the complete 64-pixel hit areas, avoids the full drawn lines and separates leaders
  from interactive bounds. Four phone badges are packed together. Draw uses its spare phone panel space for
  a taller stage and two annotation rows; controls and hint still fit at 375 by 812.
- Repeated idle settings speak every event, then give one short next-control cue per mode.
- Re-selecting the current mode does nothing, preserving its welcome and the student's work.
- Ordinary moves/settings preserve Read priority; mode changes and resets can release it. The kit's private
  Read promise is joined through its voice queue while Sound is on. Sound off uses the helper's conservative
  speech-length allowance because the kit exposes no Read completion event. Both paths received held-click checks.
- The quiet preparation is lifted with an immediate warm mat response and four large real-clock count-in dots.
  Motion off preserves the same timing and static cues.

## Teaching and timing

Six moves at three levels retain 36 A/B endpoints. Low shapes remain seated, kneeling or lying; the highest Low
keyframe head is about 0.563 body heights including the head radius. Levels uses 96 beats per minute.
Up and down retains 40 counts, High, Middle, Low, Middle, High. Walk and Slide use 100 beats per minute;
Skip and Gallop use 120. All trips retain 16 counts and a four-count preparation.
Draw counts use largest-remainder allocation with two counts reserved per part, totaling exactly 8 to 32 counts.
The ribbon's colors, patterns and icons remain redundant. Mystery reveals neutral gold before the level answer.
Mystery round 7 is the full curved circle, and all eight rounds end in the ribbon gallery.

## Narration and storage

Curio.voice owns Read, once-per-load how lines and repeated event lines. All 47 runtime strings match lines.json.
Existing recordings are retained. Six lines use browser fallback: Draw welcome, Clean floor, Clear, return-to-star,
choose-a-move and Go cues. No audio was recorded. No dance, drawing or progress is stored or sent anywhere.
The shared Motion control still remembers its setting on this device, as the standing standards require.

## Standards decisions

BASELINE w1-21 keeps dance's figure separate from PE. Mystery teaches DA:Re7.1.Kb. Draw a path supports
DA:Cr1.1.2b through different levels in one dance. DA:Cr3.1.1b is not claimed: one way of moving is chosen per path.
The prior spec routes grade 1 and 2 Re7 expectations to the dance siblings. Catalog and spec were not edited.

## Engine changes wanted

kit/curio.js, Curio.voice return object: add `waitForRead: () => readP`. The returned promise must resolve
when Read finishes or hush cancels it, also with Sound off. Then the tool's afterRead can await that public
method instead of a conservative duration cap. Empty queue barrier lines have been removed locally; this
remaining dependency is not fixed here. No kit change was made.

kit/curio.js, init Motion handler: optional in-memory preference for tools that request no persistence, while
retaining the shared Motion control. No kit change made. Dance.readPath retains its documented limit for finely
squeezed or shaky compound waves on small stages. Do not loosen shared thresholds from a few passing examples.
An explicit Read completion event would remove the Sound-off timing estimate. The four-part phone finish is
still the densest composition: its duplicate ribbon-end icon lies close behind Part 4's generous hit area.
The numbered cards remain readable and do not overlap each other. Keep this as polish for a later pass.

## Evidence

All current review evidence is under _scratch/levels-and-pathways: cold-frames, review-frames, functional-frames,
drag-review-frames, size-frames and review-audit. Driver scripts and machine-readable results are there too.
Use codex-review.md for the exact audit result and remaining limitations. The builder report describes its earlier
build only and is not current review evidence. This review used Chrome 9950 to 9957 and host 8755 only.
The single review audit reached its 2400-second bound with 30 leads and 77 frames; it did not finish stress checks.
Its snapshots precede final repairs. Focused checks answered its real leads; no second full audit was run.
The four-part audit drag fixture lacked a return expression during that run. It is corrected, and actual pointer
drags at 1366 by 768, 680 by 425 and 375 by 812 verified four parts separately. The random mixed-plan fixture is
now seeded so resizing compares the same labels. A deterministic resize and Enter-twice check preserves focus.

## Interrupted fix audit

The November 4 fix audit was started once with a 2400-second limit, Chrome 9911 and host 8715. The session cut off
after seven clean direct viewport sizes and the three mode-entry checks. It did not finish the later states,
resize stress or control walk. The 375x812 audit iframe could not be attached; its missing-hint lead is secondary
to that unread context. Independent phone drive frames exist, but the final four-pixel phone hint-padding
adjustment has no final full-viewport measurement. The resumed session verified unchanged saved artifacts and
finished reporting without a second audit. See polish.md and _scratch/levels-and-pathways/fix-audit/audit.md.
