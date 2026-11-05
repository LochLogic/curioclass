# Codex report: stage-lighting-plot

## Built

Four-mode, offline lighting-design sandbox for grades 9-12: period research, an instrument plot, live faders and cue stack, and a 40-second rehearsal with relit scenery and a three-line graph. Includes inventory limits, half-meter hanging, editable channels and gels, gobos, Fresnel focus, PAR rotation, boom height, practicals, fades, story-turn editing, device storage and confirmed clearing.

Build only. No commits, deployment or polish round. Work is confined to tools/stage-lighting-plot/ and _scratch/stage-lighting-plot/. The image tool used its own generated-image cache before copying originals into this tool.

## Numbers check

Recomputed in Scratch prepare.py and numbers.json before implementation. Levels use fractions of full, not raw percent.

- FOH ERS 19: throw 11.37190 m, diameter 3.80601 m, energy 0.8790, shown 0.5848.
- First-electric ERS 36 to Nora's chair: throw 5.33198 m, diameter 3.46493 m, energy 1.0605, shown 0.6537.
- First-electric Fresnel: flood diameter 4.97269 m, shown 0.4024; spot diameter 1.88034 m, shown 0.9727.
- Straight-down PAR: throw 4.9 m, axes 1.03002 by 2.44341 m, shown 0.99916.
- The first-electric examples in spec.md omit Nora's x offset. PAR example axes also differ slightly. The computed geometry wins; spec.md is unchanged.
- NOAA approximation: sunrise 09:19.48 CET, sunset 15:14.83 CET, daylight 5.92254 hours, consistent with the research card.
- Contrast: brand/panel 6.732:1; brand/section 6.379:1; brand-ink/brand 7.182:1.
- All 24 instruments at 100 with Fresnels on spot: tested floor mean 0.67395, while seated faces approach 1. The spec's floor-mean-near-1 expectation does not follow from its finite pools.

## Feel check

Played the full design/rehearsal loop, including a keyboard-only two-cue design and three complete 40-second rehearsals across the sparse, turning and six-instrument plots. Best moment: Nora steps away from the table into a separate pool, and the face line turns while the room loses its warm center.

Flattest moment 1: the initial drawing spent too much space on the empty house between stage and FOH. Compressed that drawn gap with an explicit label, kept real throw geometry, centered the plan and enlarged the waiting lantern portrait.

Flattest moment 2: compact settings and the cue inset made revision feel like hunting for controls. Combined settings into a compact grid and reserved preview space beside the horizontally scrolling faders. Moved Edit turns into the transport so it cannot cover graph labels.

Compared a rendered frame against Beat Lab and inspected Snowy Mail Route before implementation. Scratch bar-comparison.jpg places the painted room beside Beat Lab. The scene is intentionally a dim period interior, with a detailed set and responsive pools rather than a decorative backdrop. The plan remains technical and legible. No score or celebration was added.

## Done when

1. PASS: plan, cue board and Run view/graph dominate their modes at 1366x768 and 680x425. Reviewed the full-size frames and all eight sizes.
2. PASS with source corrections: 29 core functional checks include all five specified setups, gel transmission, PAR rotation, low-angle projection, inventory, snapping and unique cue numbering. See post-functional-result.json.
3. PASS within the disclosed simple model: the floor/back wall are mapped to the painting; paired plan/Run frames show the pool at Nora and the corresponding head brightness. Furniture has no independent shadow geometry.
4. PASS: complete two-cue run produces the beat-5 observation and spoken noTurn4. Cues at 1, 2, 5 and 8 produce allTurns. The event check filters changes to cue-bearing beats so blocking alone cannot claim a designer's turn; handoff explains the spec ambiguity.
5. PASS: Stop, Step, Back and beat jumps act in their handler. A live fader was reflected in run levels within 50 ms; seven additional checks verify independent fades, live board tracking, channel remapping, next-cue takeover and blackout. Stop preserves crossing positions and exit opacity; latest-freeze-result.json confirms pixel-identical stopped canvas frames.
6. PASS for blackout, dark narration and finite all-up rendering. All-zero mean is ambient 0.02955 and shows the warning. All-up never errors. FAIL for the separate mean-near-1 expectation; the honest result is 0.67395 for the tested concentrated plot.
7. PASS: keyboard design restored one instrument and two cues in a fresh tab. A held Clear design / confirm sequence empties storage and retains focus on Clear design. Clear and Remove reset obsolete channel readouts; clear also resets the label/fade editor. Storage calls are guarded and its status is visible.
8. PASS: five held hangs at a 2-second pace start aimHow once. noTurn4 and allTurns each start again when their event repeats; dark starts on repeated dark beats. Queued lines carry mode/beat validity through Curio.voice.
9. PASS for the provided cut: all eight beats are taken verbatim from spec.md; dialogue compared against [Project Gutenberg 2542](https://www.gutenberg.org/cache/epub/2542/pg2542-images.html). Parenthetical directions and omissions follow the supplied adaptation.
10. PASS: nine images load, inspected individually and in contact sheets. No generated people or lettering; actors are code silhouettes.

## Wave lessons

- PASS, hint and voice: mode hints change synchronously; Read uses the current hint; Curio.voice owns heard state, stale checks, Read priority and event repetition. Held-click evidence is in run-test-log.txt and voice-five-result.json.
- PASS, focus and layout: no focus on load; board rebuilding restores focus with preventScroll; record/update do not replace their controls. Dialog removal focuses Add turn deliberately.
- PASS, sizes: all eight required sizes, with 375 through port 8775's iframe. Header and primary controls use 44 px targets; compact settings remain in view. Secondary script/cue lists scroll.
- PASS, no giveaways: a sandbox with no hidden correct answer, score or success meter.
- PASS, honest numbers: visible model/gel qualifications, numeric graph ranges and a How the light works note. Computed spec discrepancies are reported.
- PASS, standards: a solo student researches motivated sources, plots technical choices, rehearses, reads the result and revises, covering TH:Cr1, TH:Cr3 and TH:Pr5.
- PASS, Motion off: no infinite animations remain; the 3.53-second check was still in beat 1 and running. Pacing uses the same five-second beat clock.
- PASS, short choice sets: all five research cards, four motivations, four shelf types and eight beat buttons stay visible. Faders intentionally scroll horizontally as the spec requires.
- PASS, resize mid-animation: full audit stress found no exceptions or controls left disabled. Runtime state is independent of canvas size.
- PASS, late welcomes: each mode uses a scoped welcome; no welcomeAfter; a Run welcome becomes stale after Run or Step.
- PASS, unknown as unknown: there is no concealed-state diagnosis. No cue means black/ambient, and its observation says so.
- PASS, one look/one meaning: graph lines differ by color, dash and label; gel choices retain names; actors keep N/H labels.
- PASS, truthful badges: inventory, selected channel, saved state and run status derive from current state. The tool does not award readiness or achievement badges.
- PASS, hints change back: mode changes, hanging, cue loading and clearing update the hint immediately; Read reads that state.
- PASS, no answer by copying: the student composes and evaluates a design; research offers evidence rather than a correct cue recipe.

## Audit leads

The one full audit finished in 1,584.04 seconds (26 minutes 24 seconds), exit 0, with seven leads. All default sizes and mode states were clean. No runtime errors, Motion-off loops, resize failures, repeated-how failures, lost events or quick-tap lost lines were found. All 45 audit PNGs were reviewed in twelve contact sheets.

1. Plan / LIVE BEAT overlap: intentional corner preview, explicitly requested by the spec. Toggle Preview off to use that plan area.
2. Plan / hpBeat number overlap: the same intentional inset caption; no text is clipped.
3. Run canvas keep-region covered at 680: the specified script caption at the bottom of the view.
4. Graph keep-region covered: transparent, real keyboard/tap targets over the beat numbers. They do not obscure the drawing.
5. Hint covered in turn editor: intended native modal backdrop. The dialog supplies its own instructions and controls.
6. Hang on pipe welcome not heard: correct STANDARDS behavior. That first tap speaks aimHow; welcomeHang becomes stale as soon as the light exists. It must not arrive late.
7. Back changes nothing at beat 1: fixed with visible boundary feedback naming Run scene and Step. A held-click recheck passed.

Final targeted changes after the audited bundle also repair independent live faders, channel preservation, repeated-beat cue numbering, actor/turn labels and cleared readouts. Final checks passed 29 core assertions plus seven live-board/fade assertions; targeted layouts and clear/remove checks had no console errors. No full audit was repeated. Scratch audit-dispositions.md records every lead and the final snapshot limits.

## Frames looked at

Scratch bar-frames (2), early-frames (5), sizes-1/2/3-frames (32), run-frames (3), functional-frames, extras-frames (5), keyboard-frames (2), feel-frames (4), targeted-frames (11), final-core-frames (4), final-layout-1/2-frames (14), late-frames (6), graph-final-frames (2), post-audit-frames (3), post-layout-frames (8), and readout-final-frames (2). Contact sheets cover every retained frame in those groups; key laptop, compact and phone views were also opened at full size. Superseded failed setup frames were replaced during the size run. All 45 audit frames were reviewed in contact-audit-1 through contact-audit-12.

## Art made

Nine images, 622,114 bytes (607.53 KiB) total WebP. No redraws were needed; the three lantern cutouts were rekeyed with despill and the PAR resized to a 900 px long side. Final prompts and provenance are in art/prompts.json. Source has 1,980 readable lines, longest line 159 characters. Bundle: 1,158,298 bytes (1,131.15 KiB), under 2 MB. Final node syntax check passed.

Illustrations were made with the built-in image tool; the complete prompt set is tools/stage-lighting-plot/art/prompts.json. No external artwork was downloaded.

## Art still to paint

None.

## Engine changes wanted

None required. Kept the specialized light model local, following the spec's engine direction.

## Left open

- The all-up floor-average expectation is contradicted by the model calculation, as described above.
- The turn-feedback interpretation, simplified projection and furniture lighting remain explicit cold-review topics in handoff.md.
- Gravel-ranger / Algenib narration remains unrecorded under Build's no-recording instruction; browser speech is the fallback. Headphone delivery remains for cold review.
- Pipe names and coordinates follow the supplied table; their SL/SR convention is noted for cold review.
- The kit Sound label changes header widths; the audit noted six controls shifting, with no overlap or lost focus. This remains a cold-review layout choice.

All owned Chrome processes and servers are closed; ports 9970, 9971 and 8775 are clear. host.html is removed. The report is the final build action.
