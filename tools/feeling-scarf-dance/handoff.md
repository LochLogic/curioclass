# Feeling Scarf Dance handoff

Built November 2, 2026, in S:/CurioClass-codex. Build only; no commit and no polish round.

## Structure

src.html starts from the kit starter and uses kit:curio, Curio.voice and kit:dance. It contains the responsive Build, Watch, Your turn and Share views, stable choice controls, the line table, original music tracks, three-step phrase construction and a tool-owned scarf simulation. All art is inline in the generated offline bundle. tool.draft.json remains stage built.

The code is organized as state and voice, controls, the dancer renderer, ribbon simulation, phrase construction, music and run lifecycle, audience feedback, layout and keyboard input. window.__tool exposes the state and renderer for checks. No dance or audience work is persisted. The shared kit still remembers Motion preference as required by STANDARDS.md.

## Owner's painted dancer decision

The current kit figure is temporary. No people, faces or body parts were generated. art/prompts.json contains eleven deferred people assets, all with people true, explicit art tokens and pose/keyframe plans. The five shapes need one main silhouette each; the six moves need their listed phases and front, quarter, side and rear views where a turn or leap requires them. Keep the same dancer, clothing, body proportions and right-hand scarf registration across the set.

createDancerRenderer is the swap boundary. Keep its Dance.dancer model for phrase timing, root motion, projection and world('rHa'). A future renderer subscribes to model.onMove, paints a matching pose atlas or articulated painted parts in floor.layers.actors and hides model.g. Update the small shape icons through icon() as well. The scarf remains the exact live code ribbon, painted with the silk texture, feeling color and pattern. Do not bake it into the dancer images. Your turn hides the whole painted dancer but preserves the model and faint hand marker. Check whole-body support and silhouette at full-screen and 680x425 before approving paintings. The bundle currently has ample room below 2 MB.

## Specification choices and open questions

- There were no explicit unresolved questions in this spec. The owner's final painted-dancer direction overrides the spec's final code-figure art plan; the kit figure is used for now.
- Family mismatch: the catalog says none but the spec explicitly requires Dance. The tool uses Dance.floor, dancer, poses, level, dyn, leap gait, phrase, clock, play, music, counts and icon.
- The spec asks for a dance.md table update, but this run authorizes writes only in the tool and Scratch. The exact proposed row is under Engine changes wanted.
- The hilltop and silk were generated with the built-in image tool, then copied to art/raw and processed only with art.py --rekey. Their full prompts are in art/prompts.json. No paid art pipeline or recordings were used.
- A chain of 24 points contains 23 segments. Segment length is 1.1 / 23 body heights to preserve the specified total length; the spec's 1.1 / 24 figure refers to 24 links and differs from its 24-point requirement.
- The long cloth touches the lower edge of the grassy stage. A tool-local contact constraint lets it settle on the grass instead of clipping below the view. Six constraint passes are followed by a forward length correction.
- Motion off shows a straight scarf and one sampled pose per count. A shared layer translation shifts low poses upward when necessary so the entire hanging scarf stays visible.
- Freeze appears immediately at the last count and holds a motionless image with no music or speech for three seconds. Its spoken reminder follows the quiet hold. This resolves the spec's simultaneous quiet-hold and spoken-freeze requirements.
- Calm uses the engine's piano at a high register for soft chimes because Dance.music exposes no chime instrument. Review that timbre by ear later.
- Your turn uses the same engine phrase and scarf simulation as Watch. It adds a four-count introduction, hides the dancer and optionally mirrors the actor/ribbon layers together. There is no separate performance animation.
- How-to lines for choosing the middle and end explicitly name the Middle and End cards, because Build keeps choices in the part the teacher selected.
- The user's stop-on-report instruction takes precedence over the brief's early-report instruction. Working evidence stayed in Scratch; codex-report.md is written last.
- Feeling idea chooses Happy if no feeling has been selected yet, making its first tap produce a complete, visible suggestion. Any of its three parts and the feeling remain editable.
- The current voice manifest contains 44 unique authored lines. Source and manifest match; no voice recording was made.

## Timing, speech and live changes

Only one engine clock, play and music object is active. Go, Again, Play and mode changes stop the old clock, music and narration, and invalidate the old token. Read stops a run before speaking. No narration is queued during active music. A part change replaces the phrase behind a stable proxy and blends from the current model pose for 180 ms. A feeling change updates tint, ribbon pattern and labels immediately and music on the next count. Slow changes tempo on the next count; Mirror changes the shared transform immediately. Stop holds the current scarf, including after the frame callback is removed.

The requested voice is bank soft-breath, Enceladus, with the spec's soft mindfulness style. No recording was made; browser speech fallback is currently used. Every authored line returned by allLines is in voice/lines.json. How-to keys are handled by V.heard through Curio.voice. Hints update directly before narration decisions, and controls keep their DOM identity. Native dialog focus returns with preventScroll.

Build verification repairs after the one audit: repeated feeling events now have unique queue keys, so a long how-to cannot cause a newer copy of the same feeling name to replace an earlier tap's event. Feeling idea skips the obsolete choose-a-start instruction when it supplies the first feeling itself. Selecting the already active mode is a no-op and does not hush narration. End has an enabled-control instruction even when selected before any other part. The modal choice menu now has its own Read button, which stops music before reading its current hint. Narrow-stage horizontal scarf contacts keep Swirl's cloth inside the painting while preserving segment lengths. These changes get focused checks, not another full audit.

## Engine changes wanted

- docs/families/dance.md, What each tool brings: add the row `feeling-scarf-dance | K-2 | square floor, one dancer, poses/level/dyn, leap, phrase, clock, play, music, counts, icon | class-created 4+8+4 feeling dances; 24-point textured hand scarf, scarf-only performance and audience observations`. No shared file was edited in this scoped run.
- kit/dance.js, floor: consider an option to hide the square platform while retaining the full-height painted landscape. This tool currently hides .dz-floor and sets the backdrop height after floor.resize. It still uses the engine floor's geometry and projection.
- kit/curio.js, init Motion persistence: an optional in-memory-only setting would reconcile literal no-storage specs with the standing shared Motion preference requirement. This build follows the standing requirement and stores no tool work.

## Check evidence

All temporary scripts, number recomputation, bar copies, shots, measurements, voice logs and mechanical audit output are in _scratch/feeling-scarf-dance. Chrome ports 9980 and 9981 and iframe host 8785 were reserved for this tool. Each process has a hard timeout. The host page is removed by the phone-check script. codex-report.md records final outcomes and any limitations; do not infer a full cold review from this Build run.

The mechanical audit's MODES_JS discovers only controls inside header. This tool's separate nav row is not discovered, so audit-states.json explicitly reaches every mode and the size sweep independently covers them all. Its default control walk is therefore not an exhaustive walk of Watch, Your turn and Share. Held-click focused runs cover their main controls, live menus, Mirror, Sound, Read, audience events and the quiet ending.
