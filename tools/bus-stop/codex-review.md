# Codex review: bus-stop

## Played
Grade K, alone with default Sound and Motion, then as a teacher projecting the same controls.
Cold play preceded builder files: Park/Duck Bridge from school to school, all seven-rider Splits, five Express reveals.
The picture-book cast, physical counters and full-bus moment are strong. They are preserved.
Evidence is in `_scratch/bus-stop/review-*`; root is `S:\CurioClass-codex`, Chrome 9960/9964, audit 9961, host 8765.

## Findings fixed
- Should fix, general, Drive: inert cup/seats/Done looked active after modeling. Their disabled states now match the phase.
- Should fix, general, keyboard: accepting a card hid the focused control during departure. Focus now goes to the visible stop sign, then the next action.
- Should fix, general, compact cards: speaker targets were 44 pixels beyond the permitted 680 preview. At 800/1000 they now measure 60 by 60.
- Should fix, general, School at 760: ten-dot patterns forced the equation under its speaker. Scoped compact dots preserve the 20-pixel type and 60-pixel speaker.
- Should fix, general, Split: an empty play area collapsed enough to clip its name. A 100-pixel minimum and bounded labels preserve both pictures.
- Should fix, general, Split at 1280: fixed five-column cells were 56 pixels wide. Responsive wrapping now gives 70 by 70-pixel targets for seven and ten riders.
- Should fix, general, Drive-Split: the old window portrait and departing riders could float over the play areas. Scene actors and the old counter board now hide during Split; trip tickets are retained.
- Should fix, general, speech: a kept grouping could start after counters moved elsewhere. Pending obsolete kept-way lines now drop; current obsolete grouping speech stops.
- Should fix, general, speech: Split and Express buried actions behind story text. Their action instructions now come first, with the premise retained in hints/Read.
- Should fix, general, voice manifest: broad expansion included unreachable false praise. Replaced 2,133 lines with 542 reachable fixed/expanded lines, including School corrections and Read hints.
- Polish, general, flattest interaction: Split counters now travel between areas, kept ways stamp in, and a complete set pulses once. Motion off removes movement.
- Polish, general, weakest art: replaced the bare route-line graphic with illustrated stop medallions, completion checks, landscape depth and a current-stop bus.
  An unpicked fork remains equally faint on both roads, with an unknown stop instead of an implied choice.
- Notes, handoff and audit states document the repairs and the preserved specification limits.

## Findings left
- Blocker, general, prescribed retry design: incremental cup/Done checking followed by trying all sentence cards earns a ticket without interpreting the story.
  The spec explicitly requires greyed wrong cards and live remaining choices. Removing that route needs a changed gate/spec; no unauthorized replacement was made.
- Should fix, general, specification coverage: K.OA.A.4 calls for every starting number 1 through 9; prescribed Ten stops start only at 4 through 8.
  Notes/handoff make the gap explicit. Adding numbers or a new activity is outside this review's permitted content.

## Break it
- On/off modeling: zero, k minus one and legal k plus one rejected on all six paths; exactly k passed. Ten cup taps at Maple Street failed with seven changes.
- Patient increment-and-check plus both wrong cards and the remaining card: reproduced an earned ticket and arrival at Duck Pond before and after fixes. This remains the blocker above.
- Wrong-sign and miscount cards alone never drove the bus or earned a ticket; counter feedback ran before retry. No running total, score, best score or reflection gate exists.
- Split: repeated Keep it recorded one way, not five. Every n from 2 through 10 produced exactly n + 1 distinct ordered ways; duplicates never increased it.
  Moving one counter and keeping each new grouping is a valid enumeration of the actual decompositions. Drive on required two distinct kept ways.
- Ten: capacity capped at ten; underfilled Done rejected; two extra children remained. School needed all ten removals.
- Express: sweeping 0 through 5 and Show me retained the first answer. Five Show me taps completed the specified demonstration ride; tickets do not certify correct answers.
- All six routes ended empty with six actual tickets; Other road restored two tickets and the pre-fork count.
  These exhaustive checks used a short speech/timing stub; the separate main-path walk used normal browser speech and timing.
- Whole-pixel jittered real cup and Split drags changed exactly one counter. Keyboard alone chose Park, added two riders and opened cards with visible focus.

## Voice walk
Normal speech, held 120 ms clicks, two-second Drive action pace, default settings: Park, Maple Street, Duck Pond, Duck Bridge, Split, Ten, School, recap; then Split and Express entry.
The standalone all-way sweep used fast taps as a stale-speech test; it was separate from the paced Drive path.
Spoken order: road/premise, question/result, off instruction/result, fork, on instruction/result, Split instruction, Drive on, Ten instruction/result, School instruction/result, ending, Split welcome, Express instruction/results/ending.
The first on instruction was interrupted before starting at Maple Street and was heard at Duck Bridge; needed instructions stayed in the current hint and Read.

| Line kind | Expected starts | Observed starts |
|---|---:|---:|
| on / off / split / Drive on / Ten / School / Express how | 1 each | 1 each |
| standalone Split welcome | 1 | 1 |
| repeated wrong Done event | 5 | 5 |
| Read, including Sound off | 2 | 2 |

Every spoken/read line in the main log is in `voice/lines.json`; runtime allLines and the 542-line manifest agree exactly.
Side checks exercised Read interruption, Sound off, fast mode changes/reset and delayed Split speech. No obsolete mode line followed a switch.
Recorded bright-teacher/Autonoe clips remain a later production stage; this review used browser narration and recorded no audio.

## Facts checked
- Objects, drawings, equations and stories within ten: [Common Core K.OA.A.1/A.2](https://www.thecorestandards.org/Math/Content/K/OA/).
- Decompositions, make ten from 1 through 9, fluency within five: the same named body's K.OA.A.3/A.4/A.5; the A.4 coverage gap is above.
- Kindergarten story types and concrete modeling: Common Core Standards Writing Team, [2011 Progressions](https://achievethecore.org/content/upload/Draft-K-5%20Progression%20on%20Counting%20and%20Cardinality%20and%20Operations%20and%20Algebraic%20Thinking.pdf), kindergarten section.
- Formal operation properties in grade one, with informal noticing here: [Common Core 1.OA.B.3](https://www.thecorestandards.org/Math/Content/1/OA/).
- Every route result, distractor, empty-seat count, remaining queue and n + 1 way count: spec Content, independently recomputed in `review-math.py` and exercised in `review-functional.json`.
  Six split totals are 7, 8, 6, 5, 4, 6. Ten complements are 3, 2, 4, 5, 6, 4. Every route stays within zero to ten.
- Express bank: independently recomputed 10 additions plus 15 subtractions, 25 positive-operand facts, results within zero to five; five unique facts per ride, both signs.
- Spec contrast recomputed: white/navy 8.61, ink/paper 14.24, muted/paper 5.74, ink/yellow 8.23, white/blue 5.19, blue/seat 3.84 to one.
- The ten-seat capacity and Ms. Rosa's limited view are fictional story premises, not real transport-capacity or safety guidance. No historical, medical or efficacy claim is made.

## Sensitivity
The 23 people assets show varied skin tones, hair and everyday dress, a hijab, glasses, a hearing aid and a leg brace; all carry `people: true`.
Fresh representation review should check the hijab and assistive-device depictions, equivalent participation and cutout edges at rider size.
No child is assigned mathematical ability by appearance, and no claim about a religion or disability is taught. Owner contact-sheet review remains part of shipping.

## Flattest moment left
Express's end is quieter than Drive's illustrated recap: five story tickets, a result and Again. No extra reward or activity was added beyond the spec.

## Graphics
Inspected all 59 finished images on seven contact pages and their in-tool use. The 19 scenes, six play areas, nine icons, two bus poses and 23 people assets form one consistent set.
No listed image is missing; no bitmap needed replacement. The weak native map and flat Split feedback were enriched without reducing the existing art.
Bundle size: 2,673.7 KB; every illustration retained. Main sizes, 375 iframe, School extremes, grayscale and Motion off frames were opened.
Motion off had zero infinite animations. Tool runs had no console/runtime errors; the temporary host's favicon 404 was harness traffic.

## Audit
One audit completed within 40 minutes: `_scratch/bus-stop/review-audit/audit.md`, 59 leads, 57 frames inspected on 15 contact pages.
- Four grouped 1280 target leads: confirmed one layout cause, repaired and re-shot at seven and ten riders; targets now measure 70 by 70.
- Forty-eight preview target rows: retain the spec's explicit 44-pixel allowance at 680. Larger layouts were audited at 60.
- Four missing generic welcomes plus one reset-cut welcome: first-tap own speech and reset hush are permitted by BASELINE 16; premise/action text remains in hints and Read.
- Two phone-context leads: the audit could not acquire its iframe context. Independent 375-pixel opening, Express/reveal, Split extremes and recap checks passed with no horizontal scroll or undersized controls.
The automatic phone audit remains unavailable; independent phone frames are not described as a full automatic audit pass.
Resize stress completed without exceptions or stranded controls. Post-audit checks covered only confirmed repairs and the phone gap; the full audit was not repeated.
The later Drive-Split visual repair was checked at 1366, 680 and 375 using reached-state fixtures; real-click audit coverage for that state was added for the next reviewer.

## Left open
The prescribed elimination cheat and make-ten coverage need spec decisions, so this review does not clear the tool for shipping.
No shared files or commits were made. Only the allowed tool/scratch folders were written; owned Chrome/server processes were closed.
Process note: initial local read commands were not wrapped in kill timeouts; subsequent work used explicit bounded runners.
