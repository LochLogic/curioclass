# Codex review: art-style-match

## Played
Cold Grade 3 solo play before reading builder notes/source: Look, tells/zoom, wrong/right Match, trade, artist/win, four Make scenes, Album.
Projector lens: the large authentic paintings and felt/gilt card table are strengths; surface transformations invite experimenting.

## Findings fixed
- Blocker, general, Make/export: changing a scene/tell could replace the picture being saved. A separate worker exports the frozen tapped scene/recipe.
- Should fix, family:art-museum, Make: smooth mixed in mean colors instead of blurring. Full-resolution smoothing stays within regions and the subject mask.
- Should fix, general, Make art: fragmented boundaries formed jagged black bands. Continuous 3px contours retain the scene and raised paint detail.
- Should fix, general, phone comparison: return controls were below two pictures. The existing action row stays visible, with space for the captions.
- Should fix, general, Match: Escape after winning prompted unavailable artist cards. Idle/won now name their actual next action.
- Should fix, general, Album: the sixth row clipped at common laptop size. Six compact rows now fit; short previews retain scrolling.
- Should fix, general, art/pond-willow: granular keyed silhouette. Two redraws give denser fronds and a cleaner silhouette while retaining left light.
- Should fix, general, art manifest: authentic paintings containing people lacked people flags. Flags added; no people generated.
- Should fix, general, Save: native disabling dropped focus during export. An aria-disabled busy state and guarded handler retain focus.
- Polish, general, Match: the win was mostly text. A paper collection record shows the actual title, attribution and tells spotted, with a finite count stamp.

## Findings left
- Blocker, family:art-museum, prescribed rejection: "No outdoor light here" denies an observable feature in Japanese outdoor scenes. The spec requires this wording and restricted tell sets.
- Should fix, general, prescribed artist step: the Van Gogh style name supplies the following artist answer. Changing that name/step requires a spec decision.
- Should fix, general, prescribed Album years: "late 1880s" includes Irises (1890). Preserved under the no-spec-change rule.
- Should fix, general, VA:Cn11 depth: cultural context is mostly read, not actively related to a work's purpose. A stronger task changes the specified activity.
- Polish, general: the finest keyed foliage remains slightly granular at the largest projection size; both review redraws were used.

## Flattest moment left
Later Match rounds repeat the tell/style/artist sequence. The personal collection record improves the payoff; different progression exceeds this spec.

## Graphics
All 18 authentic museum paintings and 10 generated assets inspected, including every Look pin frame and all four scenes.
Only willow redrawn, twice with OpenAI gpt-image. Final asset: art/pond-willow.webp; prompt/provenance: art/prompts.json.
Felt, gilt frames, rich palettes, painterly surfaces and the other nine generated assets kept. Motion off stops the new stamp and receipt motion.
Bundle: 1,582,175 bytes, below 2 MB. SHA-256 and closed-port checks: Scratch/review-validation.json.
Text contrast ratios recomputed: white/brand 7.54; brand/card 7.00; ink/card 14.91; card/felt 10.63; muted/card 6.00; ink/gold 7.36.

## Audit
Completed once within the 40-minute limit, Chrome 9961 and host 8765. Report: Scratch/review-audit/audit.md. Zero runtime errors; 51 leads:
- 13 picture/pin overlaps: intentional pins on the full-picture activation target, not overlapping pin targets.
- 18 resize flags: different shuffled work identities across fresh loads. Fixed-bedroom Look/zoom, Match and artist checks preserved identity and enabled controls.
- 18 skipped gallery welcomes: correctly stale when a work opens; lookOpen immediately names the next action. Mode welcomes and quick/repeated taps passed.
- 1 Album scroll flag: one collected card lies late in the specified long 18-slot grid. Clear confirmation controls remain visible at 680 and 375.
- 1 confirmed Save focus loss: fixed, then re-shot. A held native Save click retained focus while busy and afterward, and downloaded a 1600x1000 PNG.
Only affected flows were checked after the audit; it was not rerun. Evidence: Scratch/review-audit-confirmation.json and review-audit-confirmed/.

| Line | Kind | Expected starts | Observed starts |
|---|---|---:|---:|
| selectHow | how | 1 | 1 |
| playHow | how | 1 | 1 |
| miss | event | 5 | 5 |
| won | event | 5 | 5 |

Held 2-second pace; Read with Sound off and stale mode/reset checks passed. All 61 declared lines match voice/lines.json.

## Left open
The spec conflicts above remain under CODEX-REVIEW.md's explicit rule against changing the spec or adding an activity during this pass.
Missing shared art-museum engine/document remains in handoff.md; the existing tool-local adapter is retained. Browser narration remains the fallback.
Recipe checks: all 18 tell sets identify their own style; shared clues fit two; exactly 6 of 1,024 toggle mixes name styles.
All 18 paintings won and restored after reload; 1,080 trades preserved useful, duplicate-free hands; Clear/Keep confirmation passed.
Native jittered drag, a full keyboard win, grayscale and Motion off passed. Affected large-screen renders stayed below 300ms.
The frozen 1600x1000 export matched the tapped picture after rapid scene/dot changes, leaving the live buffer at display resolution.
Scratch evidence: review-numbers.json, review-game.json, review-trades.json, review-render.json, review-export.json and review-voice-*.json.
Frames inspected: cold-frames/, review-pins/, review-sizes/ (32 frames, eight sizes), review-fixed/, review-final-render/ and review-narrow-final/.
The temporary iframe host requested a missing favicon; offline tool resource checks showed no HTTP requests or tool runtime errors.
No commits. Repository writes stayed within tools/art-style-match/ and _scratch/art-style-match/. All started browsers/servers are closed; host.html removed.
