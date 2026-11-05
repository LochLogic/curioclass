# Stage Lighting Plot build handoff

## Structure

src.html starts from the kit starter and theme-912. It contains responsive workspaces, source and script tables, persistence, the instrument model, cue transport, the plan painter, room relighting and the graph. Curio.voice owns narration; no kit file or engine was changed. window.__tool exposes geometry, samples, completed looks, pose and transport for independent checks.

All nine generated paintings are in art/. Full prompts, provenance and keying settings are in art/prompts.json. Original generated PNGs are in art/raw/. The set is neutral-lit for multiplication. Actors are code silhouettes, as specified.

## Model and rendering

- Instrument output and transmission use the stated radius and energy formula. Level is divided by 100. ERS, Fresnel and PAR use different edge widths; Fresnel smooths its outer half. Gobos mask the beam. PAR rotation changes its oval axis.
- Oblique plan pools stretch along the throw direction, capped at six times to keep very low boom angles tractable. Focus rings project onto the floor in this simple model. Head height changes received energy. This is not a full three-dimensional cone-intersection or shadow solver.
- Light buffers are 160 by 90. The painting's floor corners in its 1600 by 900 frame are [0,891], [1600,891], [1280,508.5], [320,508.5]. The back wall occupies [320,67.5], [1280,67.5], [1280,508.5], [320,508.5]. The mask is blurred 2 px and multiplied; practical glows are added separately.
- The floor uses a four-corner trapezoid mapping. Furniture inherits its mapped surface light, without cast shadows. This limitation is stated in How the light works.
- Graph brightness samples the floor on a 20 by 14 grid. Warmth is energy weighted over that floor; the face line samples the specified head points. Each line shows its own numeric range and line pattern. Nora counts as offstage at beat 8.
- The physical FOH gap is compressed only in the plan drawing, and labeled. Throw calculations retain y = -6 m.

## Cues and transport

Cues store levels, with gels belonging to instruments throughout the scene. The last cue at or before a scrubbed beat gives its completed look. Multiple cues on the same beat have decimal numbers; the last defines that beat's target. Fades can continue into a beat without a new cue. A new cue starts from the current live fade levels.

Stop snapshots light levels, actor positions, exit opacity and the practical flicker phase. Step, Back and the graph's accessible beat buttons stop and jump. Switching to Cues can leave the scene running; its board follows the live look, and a fader overrides only its own channel until the next cue. Other channels keep fading. A complete run keeps eight five-second beats, regardless of Motion.

All design storage uses curio-lighting-plot in try/catch. A visible footer reports device-only storage and storage failure. Clear design confirms before removing work. Runtime pose, mode and current beat are not persisted.

## Open questions and spec reconciliations

- Family engine question: keep the model local, following the spec's explicit None direction. Moving a reusable beam model into kit/stage.js is a later architecture decision, not a dependency of this build.
- Source numbers: including Nora's x offset gives first-electric throw 5.33198 m, ERS 36 pool 3.46493 m, Fresnel flood 4.97269 m and spot 1.88034 m. Spec examples appear to omit the offset. At 4.9 m throw, the PAR axes are 1.03002 by 2.44341 m. The implementation follows recomputation; spec.md is unchanged.
- All-up brightness: 24 instruments at 100 with Fresnels on spot produce local face brightness near 1, but a floor mean of 0.67395 in the tested concentrated plot. The spec's mean-near-1 expectation does not follow from its finite pools. No artificial boost was added.
- Turn feedback: the descriptive graph includes face changes caused by blocking. The spoken rehearsal check considers graph changes at recorded cue beats, so blocking alone cannot satisfy a lighting-design turn. This resolves the conflict between the change definition and Done when 4's required two-cue noTurn example. It remains a reviewable interpretation.
- Cue numbers: ordinary cue-bearing beats count 1, 2, 3; additional cues on a beat add 0.5 in record order. The next beat starts at the next unused whole number, so three repeated cues cannot collide with the next beat's number. All cues at a beat fire as one target because the scene has one trigger per beat; the final snapshot wins.
- Pipe coordinates and SL/SR names follow the supplied table exactly. Confirm that the intended naming convention agrees with +x toward house right and SL at x = -6 in the cold review.
- The script uses the provided eight-beat cut verbatim. Dialogue was compared with Project Gutenberg 2542. Its parenthetical directions and omitted material follow the supplied adaptation, rather than claiming to reproduce all original stage directions.

## Review next

Read codex-report.md and Scratch evidence. The recording bank voice is specified as gravel-ranger / Algenib, but no speech was recorded, per Build instructions. Browser speech is the current fallback. Review headphone delivery and the simplified wall/furniture mapping in a cold review.

Secondary long script and cue stacks scroll. Cues intentionally scrolls faders horizontally, including at 375 px. Preview reserves space beside those faders. Compact Hang combines settings into a grid; keys 1 to 5 select a pipe on the plan and Enter hangs, including where the separate pipe picker is hidden.

## Engine changes wanted

None required. No changes to kit/stage.js, kit/curio.js or kit/curio.css were made.

## Final build checks

The one full audit completed in 1,584.04 seconds with seven leads. All default sizes/modes, Motion off, resize stress, held-click runtime checks, repeat speech and quick taps were clean. Six leads are the intentional preview/caption/scrubber/modal layers or the required first-tap welcome skip. Back at beat 1 now gives visible boundary feedback. All 45 audit frames were reviewed. Scratch audit-dispositions.md addresses every lead.

Final targeted changes after that audited bundle keep independent live faders and channel remapping coherent, preserve a normalized channel, keep cue numbers unique, make turn numbers and actor labels legible, and store the native Algenib name with its gravel-ranger bank id. The final core check passed 29 of 29 assertions, plus seven independent live-board/fade checks. Confirmed clearing left the saved design empty and focus on Clear design. Clear and last-instrument removal also reset the obsolete channel readout; clearing resets the cue label and fade editor. Post-audit, post-layout and final readout frames were inspected; no full audit rerun was made.

## Build scope

Build only. No commits, deployment or polish round. Writes are confined to this tool and _scratch/stage-lighting-plot, apart from the image tool's own generated-image cache. The final report records the one audit run and any remaining leads.
