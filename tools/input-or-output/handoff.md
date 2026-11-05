# Handoff: Input or Output?

## Structure

src.html starts from the kit starter. It uses the kit header, motion, tone and Curio.voice queue.
G holds gadget and part definitions; L is the complete spoken line table. Each mode has per-gadget exploration state.
The stage uses a responsive gadget area, real HTML hotspot buttons, SVG wires and dots, and a separate sorting/result board.
Jobs share an elapsed-time clock: five seconds normally, 5.8 seconds for the microwave's setup and full five-second countdown.
A generation token invalidates speech and delayed sounds when interrupted.
The covered-volume case and internal-heater refusal are explicit cases, not inferred from the general input rule.

## Open question taken

- class-wave: keep its people asset in prompts.json and its art token in src.html, following the spec's leaning.
  It remains pending for the owner's painter. A tasteful faceless group silhouette is drawn in code for the call square.
  No people were generated.

## Engine changes wanted

None.

## Next review

This is Build only. No commit or polish round. Browser narration is a fallback; no audio was recorded.
Use codex-report.md for the final verification evidence and limitations.

## Build verification repairs

- The one full audit completed with 44 leads. Subsequent repairs were checked with focused frames and interaction runs,
  not another full audit. Keep that distinction when judging the evidence.
- Tall 760-pixel layouts put the board below the gadget. Phones keep it beside the gadget so all six 72-pixel hotspots,
  job controls and prediction controls fit without scrolling.
- Compact microwave layouts show the changing time inside the labelled Display hotspot, avoiding a time label under
  the right-hand callouts. A covered display hides that miniature clock too. Wide layouts draw time on the painting.
- Microwave open/shut overlays use separate geometry. Trying the heater closes the pictured door before showing warm food.
- Mode re-entry and selecting the current gadget restore the result pose and its still signal trail without replaying sounds.
- Tried tiles do not drop again. Re-selecting a mode does not cut its welcome. Cover instructions are how lines, not events.
- A rapid later part tap can cut an already-started how line. Read still speaks the current hint. Recordings and a listening
  review remain work for a later run.

## Specification tension retained

- The generic covered-input narration says the gadget is stuck. The tablet camera and microphone Content rows
  specify a call that continues with one missing stream. This build follows those visible Content outcomes and retains
  the exact generic result line requested by the Voice section. A later editor should reconcile that line with the two cases.
- The module shown by neighbors.py still lists E2-SYS-SE-12. This tool does not claim to teach it. Catalog and module
  edits are outside the two writable folders authorized for this build.
- The song job uses the recognizable opening two phrases of Twinkle, Twinkle within the required five-second job.
- Narration manifests specify big-sister / Leda, but the build uses available browser speech because recording was prohibited.
