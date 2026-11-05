# Levels and Pathways handoff

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
