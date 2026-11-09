# Fire Lookout Triangles handoff

Build only, 2026-11-05. No commit or polish round. Source and evidence are confined to this tool and `_scratch/fire-lookout-triangles/`.

## Structure
`src.html` follows the kit starter, with the 9-12 theme, a tool palette, four static panel panes, and a responsive SVG map. The panel appears first in DOM order for keyboard navigation, while CSS places the map on the left. SVG coordinates are recomputed in real pixels on resize, with one common scale for miles east and north.

The script is organized as geometry and number parsing; narration; cancelable animations; Spot; Dispatch; Radio; Burn area; SVG drawing; and input wiring. The test hook exposes state, geometry, drawing transforms, and the kit voice log. It exposes no score-setting or completion shortcut. The only stored data are fixed-smoke completion marks in `curio-flt-done`, guarded by try/catch.

Sight handles are persistent HTML slider buttons above the SVG, with pointer capture, 44-pixel targets, and keyboard azimuth controls. Map crosshair input makes Spot and Radio usable with a keyboard. The open Dispatch form moves focus only when its predecessor becomes hidden. Other controls keep their DOM identities.

All animations share a cancellation handle. Replacing a smoke, restarting, changing modes, or replacing a burn cancels the old operation. Draws never replace the handle buttons or the form controls. Reduced motion finishes the geometry and arrival instantly, as the spec explicitly asks.

## Decisions and contradictions
- Open question: leave the instrument unnamed. No inventor, date, or Osborne Firefinder claim was added. This follows the option the spec leans toward.
- Art method: the current build brief and direct request require the image tool, which supersedes the spec's older local-FLUX instruction. Seven missing assets were generated with the built-in image tool, plus one smoke redraw. The existing dusk painting is preserved. All assets have `people: false`.
- Burn viewport: Burn 2 cannot fit in a two-mile square. In the chosen orientation its horizontal extent is 2.513 miles before label margins. The tool fits its exact geometry in a 2.993-mile square; Burns 1 and 3 use two-mile views. This is a viewport correction, not a change to its data or learning goal.
- Layout: STANDARDS takes precedence over the spec's unconditional stacking below 1000 pixels. Short landscape previews keep the panel beside the map. Tall narrow screens stack; phones use a shorter map so the main controls and hint remain visible.
- Spot precision: a tap snaps slightly to the intersection of rounded azimuths. At a boundary, the nearest valid intersection from neighboring whole-degree readings is used to keep smoke on the map. The point, readouts, worked law, and C circle agree exactly. Collinear smoke stays at its tapped position and reports no triangle. This convention is explained in teacher notes.
- Worked examples: Show me is available after two misses, as specified. Any Dispatch run using it is labeled guided and earns no saved check mark. The field log identifies guided runs. There is no best score or Radio/Burn mastery claim to farm by enumerating answers.
- Voice: no audio was recorded, as the brief prohibits it. `voice/lines.json` requests gravel-ranger / Algenib; the runtime uses the kit's browser speech fallback. This does not reproduce the requested timbre. Stale how-to speech can be cut as the task changes; Read retains kit priority.
- Standards: the spec's solo activities apply both laws and the area formula. CCSS G-SRT.D.9 requires deriving the area formula, and D.10 requires proving the laws. Neither derivation is specified or added. These are curriculum scope gaps for the owner to resolve, not claims that proofs are taught.
- Report timing: the direct instruction says to stop when codex-report.md is written. The report is finalized last, rather than creating an early partial report and continuing after that trigger.
- Reference tools: their existing self-contained bundles were opened read-only. Rebundling another tool would violate this run's write boundary. The nearest math neighbor has no handoff or refine file; existing Biased Bot handoff and refine notes supplied additional focus and voice lessons.

## Evidence
Scratch holds `numbers.json`, the source computation script, generated-image path mapping, art contact sheet, reference frames, initial and final size frames, real-input functional/voice/keyboard checks, phone frames, and the mechanical audit. Functional cases independently check the fixed answers and 1,200 randomly generated smokes. Audit states use actual clicks and drags, including guided progress through the locked steps.

Teacher notes distinguish completion marks from assessment, explain rounding and the fictional map, give keyboard instructions, and name sources. Review should retain the painted scene and the subdued instrument style.

## Art still to paint
None. The original magenta-keyed smoke had a colored fringe and was redrawn in opaque gray on green, then processed through the required free rekey pipeline. All other cutouts and textures were inspected together at final display scale.

## Sensitivity
No people, cultures, Indigenous communities, religion, hard history, or bodies appear. The forest and incidents are fictional. This is a classroom geometry model, not operational fire advice. Review the quiet fire depiction for age suitability; no injury or destructive spectacle is shown.

## Engine changes wanted
None. Kit files are unchanged. The built-in queue's `now` option already provides state-change interruption while preserving Read priority.

## Next review
Confirm the proof and area-derivation requirements with the curriculum owner, and decide whether the requested ranger recording should be produced in a separately authorized audio pass. The mechanical audit stopped before its first stage on a DevTools timeout. The build report records that unfinished check and the separate successful checks.

## Cold review repairs, 2026-11-08
The cold playthrough preceded reading builder notes/source. A numerical sweep earned a false independent Dispatch mark. Two rejected checks across a run now set assisted, which survives step transitions; Show me still opens after two misses within a step. The guided event has separate narration and never earns a saved mark. Resetting or choosing a new smoke starts a fresh attempt.

Burn now identifies guided work after repeated checks or Show me. Editing a completed answer immediately clears burnDone, its worked result and map answer, and keeps subsequent work guided because the solution was exposed. Failure hints now name the error and Check area at once. Radio count enumeration is labeled guided; distinct spatial intersections are still required. Its completed two-spot map highlights the farther pin and the southward lake clue, retaining both mathematical solutions.

Radio art was redrawn with the built-in image tool. All five cutouts were re-keyed with holes and despill options through scripts/art.py --rekey. Original radio is preserved in Scratch. The original forest, tower design, textures and restrained palette are retained. No shared kit changes or audio recordings.

Review evidence uses review-* files in Scratch, separate from builder evidence. See codex-review.md for the final audit disposition and remaining spec-level coverage limits.

Compact layout repairs keep the creek label clear of C and preserve the radio image's padding. At the smallest preview, tighter Spot readouts leave the welcome painting readable. Radio pin distances move into clear side margins on phones. In the zero-spot confirmation step, No spot replaces the already answered count choices in the same space and receives focus without scrolling; the count choices return after confirmation. Sight aria values wrap at north just like the visible three-digit azimuth.

The one review audit completed with 109 mechanical leads. Its drag snippets lacked outer returns, so several named states had never been reached by that replay. Eight snippets now return their coordinates; focused real-input replays verify the actual states, including a resize during arrival. Map labels now paint above plumes, and cramped AC/BT annotations use clear phone margins. The Spot button is at least 44 pixels wide, Sound has stable width, and all numeric inputs have explicit accessible names. Completed aiming redraws immediately to remove inactive handles.

The narration-only inventory omitted fixed Read hints. All 44 narration/Read strings now belong to Curio.voice's line inventory and voice/lines.json. Show me updates its hint to the actual next Check action. The main voice walk was repeated afterward. No recording was made.

An in-memory set remembers exact rounded triangles viewed in Spot or given guided status during this page session. Reusing their answers in Dispatch, including restarting a completed guided example, stays guided and earns no new saved mark. This closes cross-mode and restart answer-copy routes while preserving free exploration. It adds no persisted data. Detailed audit dispositions and final evidence are linked from codex-review.md.
