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
  Cold review painted and installed the classroom call image with built-in imagegen, following BASELINE rule 11.
  class-wave is marked people:true; its full prompt and provenance are in art/prompts.json.

## Engine changes wanted

None.

## Next review

The build and one cold review are complete when codex-review.md exists. No commits. Browser narration is a fallback; no audio was recorded.
Use codex-review.md for current review evidence; codex-report.md preserves the earlier build evidence.

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

## Cold review changes

- Mode entry begins with actionable guidance, then the descriptive welcome while it still fits.
- Try It queues the Job instruction before optional input/output definitions. This makes Job start on the tested two-second main path.
- The completed sorting board gains a teal border and all-parts-found heading; the picker check still means only that each part was tried.
- The classroom call inset uses the finished people illustration, with a landscape aspect ratio and the same covered-camera dark state.
- Motion off explicitly suppresses the physical sticky note landing animation.
- The fox image aligns to the bottom of its animation box so its feet land on the game ground.
- Notes name the discussion-only prediction limits and the spec's generic narration conflict. Live supplemental definition and melody sources were added.

## Sensitivity

class-wave is a new people image, drawn with built-in OpenAI imagegen and marked people:true.
It shows three children with varied skin tones and hair, everyday clothes and glasses, waving in a classroom.
One background redraw removed kitchen objects. A fresh cultural reviewer should inspect representation, hands, faces and the inset crop.
No Native, religious or hard-history content. The melody uses its anonymous French source credit.

## Review verification

Current evidence lives in _scratch/input-or-output/review-voice/, review-checks/, review-sizes/ and review-audit/.
The main walk uses held 120 ms clicks, two-second steps, normal job waits and Sound on. Its log records starts and cuts, not a listening review.
Do not call missing fixed recordings or the inherited catalog standard resolved. Those require work beyond the review's authorization.

## Audit-confirmed repairs

The final audit exposed the open microwave clock under Beeper at 760x900. All layouts at or below 900 pixels now use the existing labelled Display callout clock.
A covered Display still hides that clock. Four compact THINK headings used font-size zero; they now use a proper screen-reader-only style with the same visible chip/bar layout.
The call's Hello now takes the queue at its 1.6-second visual beat; it no longer waits behind the job label and disappears on two-second restarts.
Notes clarify that the 2017 troubleshooting crosswalk practices hardware-fault description only. The single full audit is not repeated after these narrow fixes.
