# Bus Stop: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: bus-stop

#### Built
- Build only in `S:\CurioClass-codex`. Tool writes are confined to `tools/bus-stop/` and `_scratch/bus-stop/`.
- Drive: three roads, two forks each, carried riders, counter modeling, shuffled sentence cards, Split and Ten stops,
  Tell first, replay, six earned story tickets, school ending and restoration of the earlier fork.
- Split: two through ten riders, every ordered decomposition, retained lists per number, duplicate feedback,
  linked turn-around pairs and a complete-set line. Three pairs of painted play areas.
- Express: five facts per ride, no repeats, at least two of each sign, first-answer lock, reveal and Again.
- Kit starter frame, Curio.voice, chimes, Sound, Motion and Read. No shared file changed, no commits, no polish round.
- Evidence lives under `_scratch/bus-stop/`. The report was started at the first bundle and completed after checks.

#### Numbers check
`content.py` independently recomputed every path before implementation; results are in `numbers.txt`.
- Park: 3 + 2 = 5, 5 - 1 = 4; branches give 7 or 8; fill with 3 or 2; 10 - 10 = 0.
- Library: 4 + 2 = 6, 6 + 1 = 7; branches give 6 or 5; fill with 4 or 5; 10 - 10 = 0.
- Farm: 5 - 1 = 4, 4 + 3 = 7; branches give 4 or 6; fill with 6 or 4; 10 - 10 = 0.
- Every route stays between zero and ten. Ordinary opposite-sign distractors are true with different results;
  miscounts are false. Ten and School distractors follow their special Content rules.
- Split: n + 1 ordered ways; 3 to 11 slots for n = 2 to 10. Express: 10 addition + 15 subtraction = 25 facts.
- Initial Ten waiting count is empty seats plus two; exactly two remain. The result says two, not the original queue.
- All eight spec contrast ratios reproduced: 8.61, 8.05, 14.24, 5.74, 8.23, 5.19, 15.25 and 3.84 to one.
- Art list arithmetic is 59 assets, despite the printed total of 45. The people count of 23 is correct.

#### Facts checked
- Objects, drawings and equations represent operations; word problems stay within ten; ordered pairs record
  decompositions: [CCSS K.OA.A.1 to A.3](https://www.thecorestandards.org/Math/Content/K/OA/), checked live.
- Making ten is K.OA.A.4, and fluency within five is K.OA.A.5: the same official CCSS page, checked live.
- Formal properties of operations appear in grade one: [CCSS 1.OA.B.3](https://www.thecorestandards.org/Math/Content/1/OA/).
  Teacher notes let kindergarten children notice swapped groups without requiring the formal term.
- Every rider count, equation, seat limit, ticket and way count comes from spec Content and the independent arithmetic.
  A ten-seat bus is a fictional constraint. No real bus-capacity, transport-safety or learning-effect claim is made.
- The 2011 Progressions is the spec's second source; the official standards pages were independently opened here.
  No claim is made that the Progressions document itself was re-audited in this build.
- Coverage limit: the fixed Ten stops start with four through eight, while K.OA.A.4 names one through nine.
  That gap is recorded in notes and handoff; no new content was invented.

#### Break it
- Done: tried zero, k minus one and k plus one changes at ordinary on and off stops across all six paths.
  Every incorrect model stayed in show; exactly k opened cards. No running total is displayed.
- Ten cup taps at the first Park stop gave seven additions and failed Done. Returning blue counters repairs the model.
- Wrong-sign and miscount cards stayed at the same stop. Wrong choices grey, act out the sign or count the riders,
  and never give a ticket. Remaining cards lock during their feedback beat.
- Trying every card can eventually find the right one after a valid counter model. This is the spec's retry scaffold,
  not an assessment score. Tickets record modeled sentences, not independent mastery.
- Split: duplicate Keep it never increases the list or unlocks Drive on. Two different ways are required.
  All ways for every n from two through ten were recorded and retained after changing n.
- Ten: the cup caps at ten. Undo and refill keep the model consistent; the two extra children remain at the curb.
- Express: swept all six tiles and Show me after the first answer. The first answer stayed locked; one ticket per fact.
  Five unique facts and both operation types were verified. Reveal tickets do not claim correct student answers.
- Real jittered cup and Split drags worked; an outside cup drop added nothing. Mode switching during departure
  paused the trip and resumed it at the correct next stop with one ticket.
- Fixed defects found by play: departure lock reused across stops; missing Split ticket; stale road-intro scope;
  visible Go after it was used; counters with the wrong ghost motion; and a naive rotating rider identity pool.
- Farm identity test now verifies unique movers, boarders absent from the aboard set, and leavers present in it.
- Five held Done-wrong taps at two-second intervals started five correction events and never advanced.

#### Voice walk
- Main path: real held clicks, two seconds per tap, default Sound, Park via Duck Bridge, through Split, Ten and School.
  `voice-main.json` records an end state with all six tickets; `voice-side.json` records the side path.
- First heard: the Park road line, the starting-rider premise, the sentence question and the correct result.
  Then Duck Pond's story/action line, later on-story/action, Split, kept ways, Drive on, Ten, School and the ending.
- Each how key on/off/split/driveOn/ten/school started exactly once. The first on how can be cut before starting;
  it is selected again by V.heard at the later on stop. No counter decides whether a how was heard.
- Story and action text share a short queued beat where long stories previously crowded out instructions.
  A student acting sooner can cut a line; the current hint and Read retain the needed instruction.
- Side path: Split welcome and kept ways, then Express story/action and Show me. The first tap's own line may cut
  the Express welcome, as BASELINE 16 permits. Scope changes hush old lines immediately.
- Current runtime line expansions exist in `voice/lines.json`; historical logs precede the final singular-grammar fix. No recordings were made.
  The intended bank voice is bright-teacher / Autonoe; runtime uses the kit browser fallback.
- Functional route batches used a 120 ms speech stub to bound arithmetic checks. The separate held-click voice walk
  used the browser speech path with normal timing. Its first run only failed while printing Unicode after saving
  the completed logs; the repeated run completed with zero runtime exceptions.

#### Feel check
- Best moment: the last empty seat fills, the two extra children wave, and the make-ten sentence earns a ticket.
  The ending shows the student's six actual stories, including their grouping at the Split stop, with all ten children waving.
- Flat moment one: riders vanished too simply at Ten. Each added rider now walks to the door while the counter responds
  immediately; undo restores that rider. Motion off preserves the same completion beat.
- Flat moment two: Split's empty list felt passive. Kept equations now carry dot pictures, duplicates flash once,
  and swapped pairs gain a curved connection and a spoken observation.
- Compared Bus Stop beside Snowy Mail Route in `bar-comparison.png`; also opened Beat Lab. Bus Stop has a richly
  painted setting and physical controls. Its deliberate pace suits a teacher-led kindergarten story.
- A child can explore different forks and groupings, rather than repeat the same arithmetic each stop.
  This is not a ten-minute self-directed sandbox; the spec calls for a class-led trip.

#### Done when
1. PASS: 1366x768 uses 84 px seats; scene, chart, cup, Done, replay and cards fit. 680x425 fits with 44 px seats
   and 20 px sentence type. All required sizes were shot, including 375 in an iframe.
2. PASS: all six paths end empty at School with six tickets. Other road restores the pre-fork count and two tickets.
3. PASS: exact change gate; zero, under, over and cup-mash checks reject incorrect models. No total readout.
4. PASS: right cards alone drive and earn tickets; wrong signs animate their operation; miscounts count aloud.
5. PASS: every n has its complete way list; duplicates do not add ways; five turn-around links exist for ten;
   Drive on requires two different kept ways. Equations and dot pictures are recorded.
6. PASS: Ten caps at ten, two extras wait and wave, and only the make-ten card advances.
7. PASS: five within-five facts, unique sample, both signs, first-answer lock, reveal for either answer, no timer.
8. PASS: cup acts during boarding; switching modes during departure is immediate and does not advance the paused trip.
9. PASS with voice-stage limitation: road/fork/place pictures, counter actions, spoken cards and dot tiles support
   a pre-reader. Kit browser speech is present; the selected recorded narrator is still to be produced separately.
10. PASS for recorded logs: five wrong events started five times; each main how started once; Go now hides when used.
11. PASS: calm has no loops or wobble; end poses occur on the same scheduled beats. Gray frame preserves counter shapes.
12. PASS: self-contained data/images/kit, no external request code, no student storage; only kit Motion is remembered.

#### Wave lessons
- Hint and voice: PASS. Hints update synchronously; Read reads the current hint; how decisions use V.heard.
- Focus and layout: PASS after fixes. Static seats/actions and retained Split buttons, preventScroll focus moves, reserved hint space,
  separate speaker targets and an Express result focus destination. Audit leads answered below.
- Sizes: PASS at all eight standard viewports. The spec's 44 px preview exception is recorded in audit-states;
  larger layouts use 60 px main controls. Phone choices all remain on screen.
- No giveaways: PASS for the intended model. Cards shuffle once per stop per page load; no running total or score.
  Trial-and-feedback remains the explicitly required scaffold, not a claim of assessed knowledge.
- Honest numbers: PASS. Counters, story counts and tickets agree. No estimate or meter is presented.
- Standards: PASS within fixed Content, with the narrower make-ten coverage explicitly identified above.
- Motion off: PASS. Infinite CSS motion is removed, feedback timing is preserved, and real art is present.
- Short choice sets: PASS. Three roads/cards, both fork choices and all six Express tiles stay visible.
- Resize mid-animation: PASS in the audit's state flips; no exception or stranded disabled control.
- Welcome timing: PASS. Own-action first lines can replace the welcome; needed context is in hint, Read and story/action.
- Unknown as unknown: PASS. The answer stays off-screen until modeling/reveal; no total badge is shown.
- One look, one meaning: PASS. Solid aboard, ring-and-plus new, dashed-arrow gone, also legible in grayscale.
- Badge truth: PASS. Full means ten seats occupied; tickets store actual completed/revealed equations.
- Reversible hints: PASS. Mode and stop transitions set their own hint at once; replay does not change the model.
- No answer by copying words: PASS. Card totals require the modeled story; the instruction does not name a right card.

#### Audit leads
Audit completed once within the 40-minute bound: `audit/audit.md`, 14 leads, no runtime errors.
- Leads 1 to 3, card speakers overlapping the three results at 760: fixed with 20 px type, tighter spacing and
  dot columns sized to their count. `card-proof-frames/cards-760-fixed.png` returns three true non-overlap checks.
- Lead 4, first term clipped at 760: fixed by the same layout change. The two-digit School-card stress at 680
  also returned three true containment checks. That isolated frame is a layout stress fixture, not a route claim.
- Lead 5, Express reveal focus at 680/800/1000: fixed by a visible, focusable result region. Each focused recheck
  reports express-result, visible true and locked true.
- Leads 6 to 9, missing/cut welcome after Express and the three road signs: intentional own-action speech under
  BASELINE rule 16. Road choice immediately speaks its road and the starting-rider premise; Read retains the role.
- Lead 10, Express event lost after repeated active-mode taps: fixed. Selecting the current mode does not hush or
  restart it. The focused two-tap check keeps fact zero and one uncut how line.
- Leads 11 to 13, quick active Drive/Split/Express taps cutting speech: fixed by the same active-mode guard.
- Lead 14, quick New road resets cutting the welcome: intentional reset; context remains in the initial hint and Read.
  Reset must hush obsolete speech, and a first-action welcome cut is permitted by BASELINE 16.
- Additional visual fixes: Express Show me is wholly visible at 1280 and 680; answer tiles shift at most one pixel
  on reveal. Split moves retain the same button node. Singular Express stories now say one gets off or one more gets on.
- The original audit records leads against the earlier snapshots. Focused proofs answer them; the full audit was not rerun.

#### Frames looked at
- Both bar frames; all five quick frames; all twelve full-size frames, including gray/calm and keyboard.
- All six route frames, three side frames and five interaction frames, individually or on labeled contact sheets.
- Updated 680/1366/375 card frames, Split at 680, all 59 processed art assets and the 23-person contact sheet.
- `voice-final.png`, the focused card proofs, rider identity, five-wrong, Go and linked-Split frames.
- All 57 audit PNGs were inspected on the ten labeled audit-contact pages, with the reported collision inspected separately.
- Final Express fit/stability, the uncut active-mode frame, and the unobstructed six-ticket school ending were also viewed.

#### Art made
- 59 final assets: 19 stop scenes, 6 play areas, 9 icons, 2 bus poses, 20 child poses and 3 driver portraits.
- 23 people assets, each marked people:true. Built-in image generation; full prompts and copied crops are retained.
- Seven rural scenes were redrawn individually after tall atlas cells failed the layout. Key-color spill was removed.
- Processed art: 1910.8 KB. Final self-contained bundle: 2756.4 KB. Voice recordings: 0 KB. The 2 MB goal is exceeded to keep every teaching scene and person;
  backgrounds were reduced to 800 px at quality 72. The bundle remains below the 6 MB documentation threshold.

#### Art still to paint
None. The contact sheet and independent representation review still belong to the later review/shipping workflow.

#### Engine changes wanted
None.

#### Left open
- Recorded bright-teacher / Autonoe narration is a separate stage, as this Build forbids recording.
- Fixed-spec K.OA.A.4 coverage is four through eight, not every starting number one through nine.
- Fresh representation review and owner contact-sheet view have not been claimed by this Build.
- Some earlier frames precede small focused fixes; corrected frames and logs are named above. Audit was run once,
  and its leads were addressed with focused checks rather than rerunning the complete suite.
- Host files and servers were kept in Scratch, so no host.html was added to the tool folder. Test Chrome and host processes were closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: bus-stop

#### Played
Grade K, alone with default Sound and Motion, then as a teacher projecting the same controls.
Cold play preceded builder files: Park/Duck Bridge from school to school, all seven-rider Splits, five Express reveals.
The picture-book cast, physical counters and full-bus moment are strong. They are preserved.
Evidence is in `_scratch/bus-stop/review-*`; root is `S:\CurioClass-codex`, Chrome 9960/9964, audit 9961, host 8765.

#### Findings fixed
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

#### Findings left
- Blocker, general, prescribed retry design: incremental cup/Done checking followed by trying all sentence cards earns a ticket without interpreting the story.
  The spec explicitly requires greyed wrong cards and live remaining choices. Removing that route needs a changed gate/spec; no unauthorized replacement was made.
- Should fix, general, specification coverage: K.OA.A.4 calls for every starting number 1 through 9; prescribed Ten stops start only at 4 through 8.
  Notes/handoff make the gap explicit. Adding numbers or a new activity is outside this review's permitted content.

#### Break it
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

#### Voice walk
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

#### Facts checked
- Objects, drawings, equations and stories within ten: [Common Core K.OA.A.1/A.2](https://www.thecorestandards.org/Math/Content/K/OA/).
- Decompositions, make ten from 1 through 9, fluency within five: the same named body's K.OA.A.3/A.4/A.5; the A.4 coverage gap is above.
- Kindergarten story types and concrete modeling: Common Core Standards Writing Team, [2011 Progressions](https://achievethecore.org/content/upload/Draft-K-5%20Progression%20on%20Counting%20and%20Cardinality%20and%20Operations%20and%20Algebraic%20Thinking.pdf), kindergarten section.
- Formal operation properties in grade one, with informal noticing here: [Common Core 1.OA.B.3](https://www.thecorestandards.org/Math/Content/1/OA/).
- Every route result, distractor, empty-seat count, remaining queue and n + 1 way count: spec Content, independently recomputed in `review-math.py` and exercised in `review-functional.json`.
  Six split totals are 7, 8, 6, 5, 4, 6. Ten complements are 3, 2, 4, 5, 6, 4. Every route stays within zero to ten.
- Express bank: independently recomputed 10 additions plus 15 subtractions, 25 positive-operand facts, results within zero to five; five unique facts per ride, both signs.
- Spec contrast recomputed: white/navy 8.61, ink/paper 14.24, muted/paper 5.74, ink/yellow 8.23, white/blue 5.19, blue/seat 3.84 to one.
- The ten-seat capacity and Ms. Rosa's limited view are fictional story premises, not real transport-capacity or safety guidance. No historical, medical or efficacy claim is made.

#### Sensitivity
The 23 people assets show varied skin tones, hair and everyday dress, a hijab, glasses, a hearing aid and a leg brace; all carry `people: true`.
Fresh representation review should check the hijab and assistive-device depictions, equivalent participation and cutout edges at rider size.
No child is assigned mathematical ability by appearance, and no claim about a religion or disability is taught. Owner contact-sheet review remains part of shipping.

#### Flattest moment left
Express's end is quieter than Drive's illustrated recap: five story tickets, a result and Again. No extra reward or activity was added beyond the spec.

#### Graphics
Inspected all 59 finished images on seven contact pages and their in-tool use. The 19 scenes, six play areas, nine icons, two bus poses and 23 people assets form one consistent set.
No listed image is missing; no bitmap needed replacement. The weak native map and flat Split feedback were enriched without reducing the existing art.
Bundle size: 2,673.7 KB; every illustration retained. Main sizes, 375 iframe, School extremes, grayscale and Motion off frames were opened.
Motion off had zero infinite animations. Tool runs had no console/runtime errors; the temporary host's favicon 404 was harness traffic.

#### Audit
One audit completed within 40 minutes: `_scratch/bus-stop/review-audit/audit.md`, 59 leads, 57 frames inspected on 15 contact pages.
- Four grouped 1280 target leads: confirmed one layout cause, repaired and re-shot at seven and ten riders; targets now measure 70 by 70.
- Forty-eight preview target rows: retain the spec's explicit 44-pixel allowance at 680. Larger layouts were audited at 60.
- Four missing generic welcomes plus one reset-cut welcome: first-tap own speech and reset hush are permitted by BASELINE 16; premise/action text remains in hints and Read.
- Two phone-context leads: the audit could not acquire its iframe context. Independent 375-pixel opening, Express/reveal, Split extremes and recap checks passed with no horizontal scroll or undersized controls.
The automatic phone audit remains unavailable; independent phone frames are not described as a full automatic audit pass.
Resize stress completed without exceptions or stranded controls. Post-audit checks covered only confirmed repairs and the phone gap; the full audit was not repeated.
The later Drive-Split visual repair was checked at 1366, 680 and 375 using reached-state fixtures; real-click audit coverage for that state was added for the next reviewer.

#### Left open
The prescribed elimination cheat and make-ten coverage need spec decisions, so this review does not clear the tool for shipping.
No shared files or commits were made. Only the allowed tool/scratch folders were written; owned Chrome/server processes were closed.
Process note: initial local read commands were not wrapped in kill timeouts; subsequent work used explicit bounded runners.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 9 (general 7, family 2), polish accepted 17
Traced to spec: blockers 1, should fix 4

### Refine: bus-stop

spec.md was updated in this merge (Refine round 1 notes in Content, Interactions, Voice, Done when 6, 7 and 13,
Sources checks, Open questions). Build to the updated spec. Lens files: `refine/teaching.md`, `play.md`, `craft.md`.
Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.

#### Blocker
1. **Miscount card counts the wrong seats on a take-away stop.** src.html:1322-1332 (`pickCard`, miscount branch).
   The count numbers seats 0 to c-1 in order, whatever the child changed. Focus lands on seat 0 at an off stop
   (src.html:1188), so the usual move is to send seat 0 off; then the dashed empty ring is counted "1", the rider still
   in seat 4 is never counted, and Ms. Rosa says "Four riders": it models skipping a rider and counting an empty seat
   at the moment it says "Let's count." Seen: `play/f/p03-off-miscount.png` (Duck Pond, card 5 - 1 = 5), DOM after the
   count `gone counting:1 ... solid:` (Play 1). Integrator read the code: confirmed. Fixed: number only seats holding a
   rider (solid or new), in seat order (spec, Interactions, Miscount). (build) (general)
2. **Express shows the answer before the child answers.** src.html:1538-1541 (`renderExpress`). On "Five riders. Two
   get off. How many now?" the strip already shows 3 solid counters and 2 dashed leaving rings, so the answer is "count
   the yellow ones": no take-away, no fluency, and Express is the only home for K.OA.A.5. The scene also can't tell on
   from off: the same three kids (ids 0 to 2) stand at the curb for every fact. Seen: `teaching/frames/express-minus.png`,
   `play/f/p14-express-minus.png` vs `play/f2/q07` (Teaching 1, Play 2, Play 9). Integrator read the code: confirmed;
   the spec asked for the rings ("b counters wear the leaving ring"), now changed. Fixed (spec, Express facts): before
   the answer the strip holds a plain solid counters; "off" leavers stand at the open door facing out, "on" kids at the
   curb; no leaving ring until the reveal; a fresh set of kids per fact. (spec) (general)

#### Should fix
1. **Ten stop and School cards are solved by the total alone.** src.html:1154-1155 (`makeStop`). Every Ten stop has one
   card ending in 10 ("8 + 0 = 8", "8 + 2 = 10", "8 + 1 = 9"), School one ending in 0, so a child picks "the 10"
   without the make-ten partner (K.OA.A.4); and the School wrong card says "Let's count." then counts nothing ("Zero
   riders"). Seen: `teaching/frames/ten-cards.png`, `play/f/p09-ten-cards.png`, `teaching/frames/school-miscount.png`,
   `craft/path-park.json` 97-99 (Teaching 3 and 6, Play 4, Craft 5). Fixed (spec, Content routes, Card kinds,
   Interactions): Ten stop cards `n + e = 10` | `n + (e-1) = 10` | `n + (e+1) = 10`, a wrong one counts the blue counters
   then "{e} kids got on. Try another card."; School cards `10 - 10 = 0` | `10 - 9 = 0` | `10 - 0 = 0`, a wrong one counts
   the dashed rings then "Ten kids got off. Try another card." Update lines.json and `allLines()`. (spec) (family:bus-stop)
2. **K.OA.A.4 covers starts 4 to 8 only.** content.json routes; notes.md admits it. The standard is "any number from 1
   to 9" (Teaching 4). Settled by BASELINE rule 2: new mode `Fill up` (spec, Screens and modes "Fill up", Voice "Fill up",
   Done when 13): five buses a ride, starts drawn without repeats so two rides use all of 1 to 9, each bus plays as the
   Ten stop with the new same-total cards, e + 1 kids waiting. Reuse the Ten stop code; add its lines to lines.json and
   `allLines()`; add `audit-states.json` entries for it. (spec) (family:bus-stop)
3. **Read in Express loses the question.** Hint `L.express` src.html:444, `expressQuestion()` 1520-1528. The fact's
   story is spoken once and never shown; Read cuts it and says only "Say how many. Tap a number, or Show me.", so a
   pre-reader alone who missed it can't hear it again (rule 4). Seen: `teaching` express-minus shot log (Teaching 2).
   Fixed: the fact's story is the first sentence of the Express hint, so Read repeats it (spec, Voice, Read line). (spec) (general)
4. **The first stop's story plays about 6 s after the kids boarded.** src.html:1144-1145 queue the road line and the
   start-counters line, then `beginStop` 1186-1187 queues the story behind them while the walk starts at once. Measured:
   tap 1.3 s, riders gone 3.9 s, "Maple Street! Two kids get on" at 10.3 s; a Done at 8.4 s drops the story unheard
   (`craft/c.json` intro-timing, `a.json` done5) (Craft 1). The spec listed three lines in a row and a walk with the story
   without saying how they fit. Fixed (spec, Interactions first bullet): on a road's first stop the walk starts when the
   story line starts. (spec) (general)
5. **Express riders walk twice and contradict the strip.** src.html:1569 then 1572/1551. `finishExpress` starts the walk;
   1.5 s later `renderExpress` re-renders the riders with the walk class, so they jump back and walk again while the
   strip and "2 + 3 = 5" already show the result, and they walk into a closed door (`showWorld` open is `!e.locked`,
   1532). Seen: `play/f2/q08-express-wrong.png` at 2.0 s (Play 3). Fixed: one walk per fact through an open door; after
   the reveal the riders stay at their end spots. (build) (general)
6. **No next action once every way is found.** Split mode: after "You found every way to make two. Three ways!" the hint
   stays "Tap a counter across. Then tap Keep it."; Drive's Split stop keeps "Find more ways, or tap Drive on." though
   the spec makes it stale when all ways are found. Seen: `play/f/p16-split-allways.png`, `p17-split-10.png` (Play 5).
   Fixed: Split mode hint after all ways names `More`, `Fewer` and the places ("Tap More or Fewer for a new number, or a
   place."); Drive's says "Tap Drive on." (build) (general)
7. **Split counters under 60 px below 1340 px wide.** src.html:161 (48 px discs) and the `auto-fit` grid at 120/182; with
   10 riders they are 47 to 48 px at 1000x625 and fall into rows of 4 at 680x425 (spec: 70 px counters in rows of 5).
   Seen: `audit-r1/state-split-ten-1000x625.png`, `state-split-ten-680x425.png` (Play 6, Craft 4; Craft's 62x60 at
   1000x625 was the button box with fewer riders, not the 10-rider disc). Fixed: 60 px or more at every size but the
   680x425 preview (44 px there), always 5 per row. (build) (general)
8. **Way list at 680x425 is cramped and crossed by lines.** Each slot's "↔" sits on the last digit ("10 = 9 + 1↔"), and
   turn-around curves run over the second column's slots; at 1366x768 the "↔" touches the digit too. Seen: `play/z18.png`,
   `play/f/p17-split-10.png` (Play 7). Fixed: the "↔" in its own space; at 680x425 drop the curves and keep the marks.
   (build) (general)
9. **Split mode says the same instruction twice in a row.** Entering Split speaks the welcome (src.html:429, 999) then
   `how('split')` (1003), back to back, nothing between (`craft/d.json` split-first, 1.3 s and 6.9 s) (Craft 2). The spec
   gives Split mode one how line (its welcome). Fixed: no second how line after the Split welcome. (build) (general)

#### Polish accepted
1. **Tell first: only Go is live while riders wait.** src.html:1206 (`canEdit` includes 'hold'): cup taps added counters
   before the story and Done shows lit beside Go (`play/f2/q03`, `play/f/p19-tellfirst-hold.png`) (Play 8). Spec now says
   so. (general)
2. **Fold "say the answer out loud" into Express.** The Express welcome is always dropped by the first fact
   (`craft/d.json` express-later) (Craft 3). Remove it from lines.json and `allLines()`; the first fact's how line is
   "Listen, say the answer out loud, then tap the number or Show me." (spec, Voice Express). (general)
3. **Express ride end lands.** After the fifth fact a big empty board (`play/f/p15-express-done.png`). Show the five
   tickets in a big row and Ms. Rosa's cheer face, as Drive's end does (Play 10). (general)
4. **Stop name on the sign face.** `#stop-name` (src.html:44) floats top-right beside the blank painted sign
   (`play/f/p02-park-walk.png`, `audit-r1/state-sentence-cards-1366x768.png`) (Play 11, Craft 6). Set it over each scene's
   sign board, as the spec says. (general)
5. **Seat chart driver mark on the right.** The bus faces right but the chart's driver mark is on the left
   (`play/f/p02`) (Play 12). (general)
6. **Crowded curb.** Seven to ten kids overlap each other and the sign post, worst at 680x425 (`play/f/p20-ten-680.png`,
   `play/f2/q01`, `q02`). Larger groups stand in two rows in perspective, no figure covering another (Play 13). (general)
7. **Split wording.** "Tap a counter across" (src.html:429, 436) becomes the spec's "Tap a rider counter to send it to
   the other side." (Teaching 8, Play 14). (general)
8. **Split equation on one baseline.** Addends sit higher than "n =" (`play/f/p16`, `p17`) (Play 15). (general)
9. **Trip map fork.** The chosen fork stop is drawn on the trunk as "?" and the line splits after it (`play/zmap.png`)
   (Play 16). Split the line at the fork with each branch holding its own stop. (general)
10. **Way list dots.** src.html:132-133, 1442: kept-slot dots are 3 px and sit side by side under the middle; empty slots
    show "· · ·", which reads as three dots (`audit-r1/state-split-small-1366x768.png`, `craft/z2.png`) (Teaching 7,
    Craft 4). Each addend's dots under its numeral, at least 5 px; empty slots a dashed outline only. (family:bus-stop)
11. **Teacher notes without build talk.** notes.md:27 ("as the specification requires"), :48 (voice fallback, will be
    false), :53 ("specified"); :58 labels an achievethecore page as the Progressions (Teaching 9). Reword, drop :48, label
    the link as what it is; add Fill up to the notes. (general)
12. **Remove the `.idle-light` speck** (src.html:62, 297) or hide it while `#split-stage` shows (`craft/z1.png`) (Craft 8). (general)
13. **Ten stop right line capitalised:** "Yes! Seven plus three..." (src.html:1347, lines.json) (Teaching 11, Play 19,
    Craft 7). (general)
14. **Express mix at random,** 2 or 3 adds per ride (src.html:1517 always 2 adds) (Teaching 10, Play 18). (family:bus-stop)
15. **Tell first icon:** a speech bubble, not ☏ (Play 20, spec Screens). (general)
16. **Access labels:** `#cup` label says "Full" when full or disabled (src.html:310); the Split equation is announced
    when a counter moves (aria-live) (Craft 9). (general)
17. **Drive Split ticket records the last kept way,** not the counters as they stand at Drive on (`play/f2/q09`: kept
    7 = 6 + 1, ticket 7 = 4 + 3) (Play 17). (general)

#### Settled calls
- Express giveaway and the same-total Ten and School cards: Play sent both to the spec's open questions because the spec
  wrote them; settled here by "a check must reward the right practice" and BASELINE rule 2, spec.md updated, so Codex
  builds them.
- K.OA.A.4 range: Teaching offered a short Ten round or varying the Ten stop; settled as the `Fill up` mode (rule 2, rule
  1: taught in full, not a thin add-on). Varying the Drive Ten stop alone can't reach 1 to 3 or 9 without breaking the
  route numbers.
- Split counter size: Play (47 to 48 px with 10 riders at 1000x625) and Craft (62x60) measured different states; the
  10-rider case and src.html:161 decide it, so it is a should fix.
- Keep: the cup stops by itself at 10 (Done when 6); welcomes cut by a first tap (BASELINE 16); 44 px controls at the
  680x425 preview (spec allows); wrong cards act out, never buzz; no score, no timer; the trip map "?" circle drawn over
  the road (all three lenses: no overlap on screen).

#### To the spec's open questions
- None for Cory. Everything the lenses routed here was settled from BASELINE and the spec (Settled calls).

#### Not taken
- Elimination drives the bus (Teaching 5): wrong cards are acted out and greyed; gating the rest or a first-try star
  would add friction or a score. Notes already tell the teacher.
- Rider faces on Split counters, kids beside the play areas (Play 14): the plain counter is the K.OA.A.1 object on purpose.
- Bundle 2.74 MB (Craft 10): over the 2 MB goal, under 6 MB, no `Size:` line needed (BASELINE 12).

<!-- end part -->

<!-- part: refine/craft.md -->

### Bus Stop: Craft lens (round 1)

Cold Craft lens on the built bundle `tools/bus-stop/bus-stop.html` (not re-bundled). My own runs:
`S:/CurioClass-codex-scratch/bus-stop/craft/` (a.json to e.json, outputs in `out/`, logs in the *.json files).
Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.

#### Findings

##### Should fix

1. **The first stop's story line plays long after the kids have boarded.** `src.html:1144-1145` queues two intro
   lines on a road pick ("The park road! Off we go." and "Three riders are on the bus. I can't see the back seats, so
   the seat chart shows me."), then `beginStop` (`src.html:1186-1187`) queues the stop story and its how line behind
   them. The riders' walk starts at once and is over in about 2.5 s. Measured (c.json `intro-timing`, real voice, no
   other taps): tap at 1.3 s, riders gone by 3.9 s, "Maple Street! Two kids get on the bus. Tap the cup..." starts at
   10.3 s. So "two kids get on" is spoken about 6 s after they got on, and a child who waits 7 s still hasn't heard
   the stop story (a.json `done5`: Done tapped at 8.4 s dropped the story and how line unheard). The spec's watch step
   has the story line play while the riders walk. Fix: hold the first walk until the story line starts, or shorten
   the intro to one line. Same thing happens on every road. Tag: general.
2. **Split mode says the same instruction twice in a row.** Entering Split queues the welcome
   ("Tap a counter across, then Keep it. Show every way to split the riders.", `src.html:429`, `999`) and then
   `how('split')` (`src.html:1003`), "Tap a counter across. Then tap Keep it." Both are spoken back to back
   (d.json `split-first`: 1.3 s and 6.9 s, nothing else between). That breaks "don't nag". Fix: make the how line
   silent when the welcome just said it (or fold the welcome into the how line). Tag: general.

##### Polish

3. **The Express welcome is never spoken.** `setMode` calls `V.welcome()` and then `expressQuestion()` with
   `now:true` (`src.html:999`, `1004`, `1526`), which drops the queued welcome every time (d.json `express-later`:
   welcome `dropped, newer`; audit row 2 likewise). Its line ("Listen, say the answer out loud...") is in
   lines.json and would be recorded for nothing, and "say the answer out loud", the class part of Express, is never
   heard. Better: drop the Express welcome and put "Say the answer out loud" into `L.express`. Tag: general.
4. **Split counters and way dots lose the five structure at small sizes.** At 680x425 the counters sit in rows of
   4 (frame `audit-r1/state-split-ten-680x425.png`: 4, 4, 2), not the spec's rows of 5 (the `auto-fit` grid at
   `src.html:120` and `182`). In the way list the dot pictures are 3 px and sit side by side in the middle of the
   slot, not under their numbers (`src.html:133`, `1442`; zoom `craft/z2.png` of
   `state-drive-split-1366x768.png`: the dots for "6 + 1" are both under "= 6"). Better: a fixed 5-column group,
   and each addend's dots under its numeral, at least 5 px. Tag: general.
5. **At School, a wrong card says "Let's count." and then counts nothing.** For the two School wrong cards the
   miscount branch (`src.html:1321-1331`) loops `d.stop.c` = 0 times, so the child hears "Let's count." then
   "Zero riders. Try another card." with nothing lit (path logs, `craft/path-park.json` lines 97 and 99). Better:
   for 10 - 9 = 1 point at one ring and say "one rider still on? Look, every seat is empty"; for 10 - 0 = 10 use the
   ghost act-out. Tag: general.
6. **The stop name floats beside the blank painted sign, not on it.** `#stop-name` is pinned top-right
   (`src.html:44`), so a code label hangs next to an empty painted sign (`state-sentence-cards-1366x768.png`,
   `-760x900.png`, `-375x812.png`). The spec puts the name on the blank sign. Better: place the label over the sign
   board in each scene, or crop the sign out. Tag: general.

##### Nit

7. Ten stop right lines start lower case after "Yes!": "Yes! seven plus three equals ten..." (`src.html:1347`, five
   lines in `voice/lines.json`). Use `cap(num(s.a))`. Tag: general.
8. `.idle-light` (`src.html:62`, `297`), an 8 px glinting dot with z-index 8, shows over the Split stop in Drive at
   the left edge (zoom `craft/z1.png` of `state-drive-split-1366x768.png`) and reads as a speck elsewhere. Remove it
   or hide it when `#split-stage` shows. Tag: general.
9. Access: `#cup` keeps the label "Counter cup: add one rider" when full or disabled (`src.html:310`); the Split
   equation (`#split-equation`) is not announced when a counter moves, so a screen reader user hears only "Move
   rider to Slide". Tag: general.
10. Bundle is 2.74 MB (59 webp images, 1.9 MB of art), over the 2 MB goal and under 6 MB, so no `Size:` line is
    required. Tag: general.

#### Checks that came out clean

- **Contract:** one file; no resource requests after load (`performance` resource list empty, a.json `contract`);
  no `http` URLs in the bundle; no console errors or exceptions in any of my 17 shots or the audit; nothing stored
  except the kit Motion setting; kit used (Curio.voice, kit header, kit focus ring).
- **Lines:** `allLines()` = 542 lines = `voice/lines.json` 542 lines, word for word, both directions. All 6 paths
  (each road, both forks via Other road) played with too-few and too-many Done, both wrong cards, Ten-stop over-taps,
  Split stop, then Split mode n = 2 to 10 every way, places, and two Express rides: 282 distinct spoken texts, every
  one in lines.json. Tickets right on every path; the bus never left on a wrong card.
- **Access:** Tab order is header, then panel (Tell first, New road), then road signs (c.json `tab-order`); after a
  right Done focus moves to the first card, then its speaker (`cards-key`); kit `:focus-visible` 4 px ring; new,
  gone and aboard counters differ by mark and ring, not color alone; wrong cards grey and disable. Targets: 60 px or
  more at every size except the 680x425 preview, where the spec allows 44 px. Split counters measured 62x70 at
  1366x768, 70x70 at 1280x720, 62x60 at 1000x625 (e.json).
- **Motion:** frame times during the boarding walk at 1366x768: p50 16.7 ms, p95 16.8 ms, max 16.8 ms (d.json; a
  desktop headless Chrome, not a slow laptop). Motion off: audit clean.
- **Art:** 59 `art:` tokens, 59 prompts.json entries, no extras; all 23 people images (10 kids x 2, Ms. Rosa x 3)
  are `people: true`, drawn by gpt-image (not a local model); the cast covers the spec's hijab, glasses, hearing aid
  and leg brace.
- **Words:** no em dashes in src, notes, spec, content or lines; "Curio Class" never shortened; nothing
  classroom-unsafe.

#### Standard voice check (Sound on, Motion on, held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| "Two kids got on, and you added zero..." (Done too few, 5 taps 7 s apart) | event | 5 | 5 |
| "Maple Street! ... Tap the cup for each new rider..." (first on stop) | how | 1 | 1 when left alone (at 10.3 s, finding 1); dropped unheard when Done comes first |
| Split welcome, then "Tap a counter across. Then tap Keep it." | welcome + how | 1 | 2 (finding 2) |
| Express welcome | welcome | 1 | 0 (finding 3) |
| "How many riders now? ..." after switching back to Drive | how | fits the cards on screen | 1, correct |

- **Stale lines:** road, cup, cup, Done, Split, Drive at 0.2 s gaps: the card sequence was hushed by the mode
  switch, the Split welcome cut by Drive, and only the line for the cards on screen played after. Clean.
- **First tap:** stage tap and a first Tab key both give the welcome within 0.3 s; road sign gives only its own line;
  Read speaks the hint only; Sound says nothing (audit table). Clean.
- **Read:** Read during "The park road!" cut it and spoke the hint; with Sound off Read still spoke. Clean.
- **Order:** spoken lines follow the actions in every log. Clean.

#### Audit pilot

- **Leads confirmed:** first tap on Express or a road sign skips the welcome (true, and fine under BASELINE 16 for
  the roads; for Express it hides a bigger problem, finding 3: the Express welcome never plays at all). 44 px targets
  at 680x425 are real but allowed by the spec.
- **Leads wrong:** "button.split-counter 47x44 [every size]" is wrong: I measured 62x70, 70x70 and 62x60 at
  1366x768, 1280x720 and 1000x625. "Line drawn across text ?" is the trip map road running under the "?" fork circle,
  which is drawn on top (`src.html:1378-1387`, frame `state-seat-work-1366x768.png`): no overlap on screen.
- **Missed:** the late first-stop story line (finding 1, it needs timing against the walk), the back-to-back Split
  instructions (finding 2), the dead Express welcome as a whole-tool fact, rows of 4 and misplaced way dots
  (finding 4), the empty School count (finding 5), the stray idle-light dot (finding 8).
- Nothing cultural, Native or hard-history here; the people art goes to the contact sheet and the fresh
  representation check the spec already names.

<!-- end part -->

<!-- part: refine/play.md -->

### Bus Stop: Play lens (round 1)

Played twice: once as a kindergartner alone at home, Sound on, reading nothing, and once as a teacher projecting
Drive with a class calling out the stories. All three roads, both forks, Split mode from 2 to 10, three Express rides,
Tell first, Other road, Motion off, 1366x768, 760x900 and 680x425. I drove the tool with drive.py (real held clicks,
a jittered drag from the cup to a seat, keys), on Chrome port 9862.
Frames: `S:/CurioClass-codex-scratch/bus-stop/play/f/` (p01 to p23), `f2/` (q01 to q09), `f3/` (r1, r2), plus the
zooms `z18.png` and `zmap.png` in `play/`. Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.
No console errors or exceptions in any of my 34 shots.

What works: the first screen names the action ("Tap a road sign...") and the picture signs need no reading; every
step's hint names its control; wrong cards act themselves out instead of buzzing; the bus never leaves on a wrong
card; Done only passes with exactly k counters (I tried 0, 1, 3, and the cup does stop at 10); Other road brings back
the fork with the chart and tickets as they were (p23: tickets "3 + 2 = 5", "5 - 1 = 4", 4 riders); the end screen
with ten waving kids and the ticket row lands (p11). A kid would replay a road to see the other fork. The short
test passes for Drive; the findings below are about moments that teach the wrong thing or show the answer.

#### Blocker

1. **Drive, miscount card on a take-away stop counts the wrong seats** (src.html:1323-1327). "Let's count" numbers
   seats 0 to c-1 in order, whatever counters the child removed. Focus lands on seat 0 at an off stop (src.html:1188),
   so the usual move is to tap seat 0 to send it off. Then the dashed empty ring gets "1", the rider still sitting in
   seat 4 is never counted, and Ms. Rosa says "Four riders": the tool models skipping a rider and counting an empty
   seat at the exact moment it says "Let's count." Seen: `f/p03-off-miscount.png` (Duck Pond, 5 - 1 = 5 card),
   DOM after the count: `gone counting:1, solid counting:2, solid counting:3, solid counting:4, solid:` (seat 4
   uncounted). Fix: count the seats still holding a rider (solid or new), in seat order. **general**

#### Should fix

2. **Express shows the answer on the take-away strip** (src.html:1538-1541). Before any answer, "Five riders. Three
   get off" draws 2 solid counters and 3 dashed leaving rings, so the answer is just the solid counters: no
   subtracting, no fluency (K.OA.A.5). Add facts are softer (count the counters, then the kids) but are still counting
   all. Seen: `f/p14-express-minus.png`. This is how the spec describes it ("b counters wear the leaving ring"), so it
   goes to the spec's open questions: for example show a counters plain and the b leavers standing at the open door,
   and mark the leaving rings only on the reveal. POLISH, Games and quizzes. **general**

3. **Express, the riders walk twice and contradict the strip** (src.html:1569 then 1572/1551). finishExpress starts the
   walk; 1.5 s later renderExpress re-renders the riders with the walk class again, so the kids jump back to the curb
   and start over while the strip already shows the result and "2 + 3 = 5". They also walk on into a closed door
   (showWorld open is `!e.locked`, src.html:1532). Seen: `f2/q08-express-wrong.png` at 2.0 s: five seats full, the
   sentence shown, three kids still on the curb, door shut. Anything shown twice must match (POLISH). **general**

4. **Ten stop and School cards are solved by the total alone.** At every Ten stop the right card is the only one that
   ends in 10 ("8 + 0 = 8", "8 + 2 = 10", "8 + 1 = 9"), and at School the only one ending in 0. After one trip a child
   picks "the 10" without asking what goes with 8 to make ten, which is the K.OA.A.4 question. Seen:
   `f/p09-ten-cards.png`, `f/p20-ten-680.png`. Better: wrong cards that also say 10 ("8 + 1 = 10", "8 + 3 = 10"), so the
   child matches the blue counters to the second number. Card content is in the spec, so this goes to its open
   questions. **general**

5. **No next action once every way is found.** Split mode: after "You found every way to make two. Three ways!" the
   hint stays "Tap a counter across. Then tap Keep it." although nothing is left to keep; More, Fewer and the places
   are never named. Drive's Split stop: "Find more ways, or tap Drive on." stays when there are no more ways (the spec
   says that line goes stale when all ways are found). Seen: `f/p16-split-allways.png`, `f/p17-split-10.png`
   (hint text in the run log). Say how to act. **general**

6. **Split counters under 60 px below 1340 px wide.** With 10 riders the counters are 47 to 48 px at 1000x625 (the
   `repeat(5)` rule only applies at 1340 px and up). At 1366x768 they are 62x70 (measured, `f3/r1`). Seen: audit
   `state-split-ten-1000x625.png`. K targets are 60 px. **general**

7. **Way list at 680x425 is cramped and crossed by lines.** With 7 to 11 slots in two columns, each slot's "↔" mark
   sits on the last digit ("10 = 9 + 1↔" reads "10 = 9 + 1."), and the turn-around curves run down the gap and over the
   slots of the second column. At 1366x768 the "↔" also touches the last digit, a lighter version. Seen: `play/z18.png`
   (zoom of `f/p18-split-10-680.png`), `f/p17-split-10.png`. In the preview, drop the curves (keep the ↔ in its own
   space) or give the mark room. **general**

#### Polish

8. **Tell first leaves the cup and Done live before Go** (canEdit includes 'hold', src.html:1206). With Tell first on,
   two cup taps added two counters before the story played; Done is lit gold beside Go. Seen: `f2/q03` (changed = 2 in
   hold), `f/p19-tellfirst-hold.png`. Better: only Go is live and lit while the class tells the story. **general**

9. **Express scene cannot tell on from off.** The same three kids (ids 0, 1, 2: Express never moves the kid cursor)
   stand on the curb for every fact; for "get off" they stand exactly where "get on" kids wait, though the spec puts
   leavers at the door. A child who misses the words can't read the story from the picture. Seen: `f/p14` vs
   `f2/q07`. Better: leavers at the open door facing out, a fresh set of kids per fact. **general**

10. **Express ride end is flat.** After the fifth fact the tiles disappear and leave a large empty board with one
   strip, and Ms. Rosa keeps her talking face. Drive's end (tickets in a big row, the kids waving) lands; Express could
   do the same with its five tickets and the cheer face. Seen: `f/p15-express-done.png`. **general**

11. **Stop name floats over a blank painted sign.** The name box sits above and beside the painted stop sign, whose
   face stays empty at every stop (the spec puts the name on the sign). Seen: `f/p02-park-walk.png`,
   `f2/q01-school-after.png`. Better: set the name on the sign face, or crop the blank sign out. **general**

12. **Seat chart faces the other way from the bus.** The painted bus faces right (door and driver on the right); the
   chart's driver mark ◉ is on the left, so the front of the chart is the back of the bus. Seen: `f/p02`. Put the
   driver mark on the right. **general**

13. **Crowded curb.** Seven to ten kids are packed into the right 40 percent of the scene and overlap each other and
   the sign post, most at 680x425. Seen: `f/p20-ten-680.png`, `f2/q01`, `f2/q02`. POLISH: no figure covers another;
   stand larger groups in two rows in perspective. **general**

14. **Split mode has no riders in it.** The counters are plain yellow discs on the swings and slide; the ten kid
   cutouts drawn for the tool never appear, and "Tap a counter across" ("across" is a hard word for K) is the only
   instruction. A rider face on each counter, or kids standing beside each play area, would make 7 = 4 + 3 a story the
   way Drive is. Seen: `f/p16`, `f/p17`. **general**

15. **Split equation steps up and down.** The addends (number over dots) sit higher than "n =", so "10 = 0 + 10"
   looks staggered. Seen: `f/p16`, `f/p17`. Align the numerals on one baseline with the dots below. **general**

16. **Trip map forks in the wrong place.** The chosen fork stop is drawn on the trunk as "?", and the line splits after
   it, at the Park, Library or Farm stop, which sits on the upper branch while the lower branch has no stop. The
   picture of "two roads" doesn't match the choice the child made. Seen: `play/zmap.png` (crop of `f/p03`). **general**

#### Nit

17. The Drive split ticket records the counters as they stand when Drive on is tapped, not a kept way: I kept 7 = 7 + 0
   and 7 = 6 + 1, moved two more and got the ticket "7 = 4 + 3" (`f2/q09`). **general**
18. Every Express ride is 2 add and 3 take-away facts (src.html:1517); a ride is never 3 adds. **general**
19. The Ten stop right line starts lower case after "Yes!" ("Yes! seven plus three equals ten.", src.html:1347 and
   lines.json). Spoken only today; it would show in a caption. **general**
20. "Tell first" uses a telephone glyph ☏; a child alone has no way to know what it does. A speech-bubble icon (as the
   spec says) would read better. **general**

Not reported: the welcome cut by a first tap on a road sign or Express (BASELINE 16; the premise is in the hint and
Read). Voice counts are Craft's; in my muted run the vlog marked every line `silent`, so I could not judge timing by
ear.

#### Audit pilot

- **Leads confirmed:** split counters below 60 px with 10 riders (confirmed at 1000x625, finding 6). The 44 px controls
  at 680x425 are real but the spec allows 44 px in the preview, so not reported.
- **Leads wrong:** "line drawn across text '?'" on the trip map: the road runs under the "?" circle, not across the
  glyph (`play/zmap.png`). "split-counter 47x44 at every size": at 1366x768 the counters measure 62x70 (`f3/r1`, `r2`).
  "Welcome not heard" after Express and road first taps: allowed by BASELINE 16.
- **Missed:** the miscount count landing on the empty seat (blocker 1), the Express double walk (3), the answer on the
  Express strip (2), the Ten and School cards solved by the total (4), the stale hint after all ways (5), the cramped
  680 way list (7), the live cup during Tell first (8), and everything about feel. Its clean rows on sizes, Motion
  off, resize and the 2 s tap pace held where I looked.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Bus Stop: Teaching lens (round 1)

Cold lens, Claude, 2026-11-06. Read spec.md, src.html, notes.md, content.json, voice/lines.json, audit-states.json,
STANDARDS.md, BASELINE.md, REFINE.md and the shared audit (`S:/CurioClass-codex-scratch/bus-stop/audit-r1/audit.md`).
Own frames and logs: `S:/CurioClass-codex-scratch/bus-stop/teaching/frames/` (shots in `../shots.json`).

Checks run:
- Recomputed all 6 route paths from content.json in Python: park 3,5,4 then 7 or 8; library 4,6,7 then 6 or 5;
  farm 5,4,7 then 4 or 6. Every stop's start matches the previous result, Ten stop empties 2 to 6, all within 0 to 10,
  all match the spec's Content. 25 Express facts match the spec (10 add, 15 take-away, largest sum 5).
- CCSS K.OA.A.1 to A.5 wording in the spec matches the standards as published (A.3 asks "more than one way"; the tool's
  "every way" is above the minimum).
- Played Park road via Duck Bridge school to school (frames `ten-start`, `ten-cards`, `school-miscount`, `end`),
  a Farm off stop (`drive-offstop`), Ten stop miscount (`ten-miscount`) and an Express take-away fact with Read pressed
  (`express-minus`). Done passes only on exactly k (code `done()`, src.html:1253); the bus never leaves on a wrong card.

#### Findings

1. **Express take-away facts show the answer before the child answers.** Where: Express, `renderExpress()`
   src.html:1538-1541. On "Five riders. Two get off. How many now?" the five-seat strip already shows 3 solid counters
   and 2 dashed rings with arrows, and the 2 leaving kids already stand on the curb. The answer is "count the yellow
   ones"; no subtraction and no fluency is needed. Add facts show a counters plus b kids, so they are count-all too.
   K.OA.A.5 asks for fluency, which this mode is the only home for. Better: before the answer show the a riders (all
   solid) and the b leavers still at the door, and only mark the gone rings at the reveal; or show the picture for a
   moment then cover the strip while the question is asked. How seen: `teaching/frames/express-minus.png`.
   **should fix**, general.

2. **Read in Express loses the question.** Where: Express hint `L.express` src.html:444, `expressQuestion()` 1520-1528.
   The hint is only "Say how many. Tap a number, or Show me."; the story ("Five riders. Two get off. How many now?")
   is spoken once and never shown. Pressing Read cuts the story and reads only the instruction (vlog: the express how
   line "cut: read", then read = "Say how many. Tap a number, or Show me."). A pre-reader alone at home who missed the
   question has no way to hear it again (rule 4). Better: put the fact's story in the hint (or have Read say it), as
   Drive's See again does for stops. How seen: `express-minus` shot log. **should fix**, general.

3. **The Ten stop never asks the make-ten question.** Where: Ten stop, `addCounter()` src.html:1207-1216 and
   `makeStop()` 1154. The cup stops by itself at the tenth seat and greys to "Full", so the child taps until it stops;
   then the only card whose total is 10 is the right one ("7 + 3 = 10", "7 + 2 = 9", "7 + 0 = 7"), with the bus
   visibly full. A child can drive on without ever knowing the 3. K.OA.A.4 is the number that makes 10. Better: a
   distractor that also says 10 with the wrong addend (`7 + 2 = 10`), so the child must count the blue counters; or
   ask "How many empty seats?" before the cup goes live. How seen: `teaching/frames/ten-cards.png`. **should fix**,
   family:bus-stop.

4. **K.OA.A.4 covers only 4 to 8.** Where: content.json routes; notes.md "Good to know" admits it. The standard says
   "for any number from 1 to 9"; 1, 2, 3 and 9 never come up in a Ten stop. Split mode at 10 does list all eleven ways
   to make ten, which helps, but it is a decomposition task, not "given 3, find the partner". Rule 2 wants the code
   taught well. Better: a short Ten round (Split-style or in Express, any start 1 to 9, fill the empties, pick
   `n + e = 10` against close distractors), or vary the Ten stop's start on Other road. **should fix**, family:bus-stop.

5. **Elimination drives the bus.** Where: Drive tell step, `pickCard()` src.html:1285-1338. With three cards and wrong
   cards greyed for the stop, two wrong taps leave one card; the ticket then records it like any other. No score, and
   each wrong card is acted out, so this is not a blocker, but a child can finish every stop by tapping in order. notes.md
   line 27 says so to the teacher. Better: after a wrong card, the remaining cards stay live only after the child
   re-counts or taps See again, or the ticket marks a first-try stop with a small star. **polish**, family:bus-stop.

6. **School miscount card counts nothing.** Where: School stop, card "10 − 9 = 1", src.html:1321-1332. Ms. Rosa says
   "Let's count." then nothing is counted (no counters) and "Zero riders. Try another card." The empty count shows no
   reason one rider can't be on. Better: point at the ten empty rings ("Every seat is empty. Nobody is still on."), or
   count the ten rings that left. How seen: `teaching/frames/school-miscount.png` and its log. **polish**, family:bus-stop.

7. **Way list dots don't sit under their numbers.** Where: Split, src.html:1442 and `.way-dots` 132. In a kept slot the
   two dot groups sit side by side under the middle of "2 = 2 + 0", so "2 = 1 + 1" shows two lone dots under the first
   1. Empty slots show "· · ·", which reads as three dots to a dot-counting child. Better: dots under each addend as in
   the live equation, and an empty slot with no dots (a dashed outline is enough). How seen:
   `audit-r1/state-split-small-1366x768.png`. **polish**, family:bus-stop.

8. **"Tap a counter across" is vague for K.** Where: `L.split`, `welcomeSplit` src.html:429, 436. The spec's "Tap a rider
   counter to send it to the other side" says where it goes; "across" does not. **polish**, general.

9. **Teacher notes carry build talk.** Where: notes.md:27 ("as the specification requires"), :48 ("Speech uses the
   kit's browser voice fallback in this Build. No voice recordings were made."), :53 ("25 positive-operand facts
   specified"). Teachers don't know the spec or the build; line 48 will be false once voice is recorded. Better:
   "Wrong cards stay grey for that stop", drop line 48, "25 facts within five, no zeros". Also :58 names the
   Progressions but links an achievethecore situation-types page; label it as what it is. **polish**, general.

10. **Express rides are always 2 add and 3 take-away.** Where: `newExpress()` src.html:1517. The spec says "at least 2
    of each"; the code fixes the split, so additions are always the minority. **nit**, family:bus-stop.

11. **Ten stop right line lower case.** Where: src.html:1347 "Yes! seven plus three equals ten." (also in lines.json).
    Harmless for speech; matters only if lines are shown or recorded as text. **nit**, general.

Language, grade fit and guardrails otherwise hold: every choice is a picture or numerals with dots and is spoken, no
score or timer, K teacher-led with a solo path. Done-when 2 to 7 hold on the path I played and in code. Nothing
cultural, Native or hard-history. The rider kids (hijab, hearing aid, leg brace, varied skin tones) go to the BASELINE
11 representation check, not judged here.

Counts: blocker 0, should fix 4, polish 5, nit 2.

#### Audit pilot

- Leads confirmed: none touch teaching. The 44 px targets at 680x425 are the spec's allowed preview size. The Express
  welcome "not heard" after a first tap is allowed by BASELINE 16, and the Express how line still names the action.
- Leads wrong or not mine: "line drawn across text '?'" on the trip map is the fork's unknown stop; the circle is drawn
  over the path (not checked further, Play/Craft).
- Missed (it can't see these): the Express take-away strip giving the answer (1), Read dropping the Express question
  (2), the Ten stop solvable without the make-ten number (3), and the empty count on the School miscount card (6).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: bus-stop (Codex fix, round 1)

Curiosity precedence applied throughout. No welcome, goal, score, level, quiz layer, finish screen or kit header was added.
The inherited scene, art and arithmetic remain; the kit frame became a full-width bus dashboard and lower-left Manual.
Drive on is freely available. School returns to the fork; Express and Fill up continue with rolling tickets.
Voice gives at most one first-use hint, then waits for Read, including the sentence-card Read buttons.
These override the lesson-shaped welcome, two-kept-way quota, automatic narration and fixed ride endings in the older spec.
No questions were asked during this unattended run. Missing plate number is left unassigned, rather than invented.

Evidence below is relative to `_scratch/bus-stop/`. Each listed frame was opened and inspected.
`before/` holds reproductions; `proof/`, `polish-proof/`, `extra/`, `final-frames/` and `phone/` hold after checks.
Numeric JSON beside a frame gives its exact state. `reproduce.py`, `verify.py`, and shots JSON preserve the steps.

#### Blocker
1. **FIXED: miscount seats.** Before `before/b1-off-miscount.png`, the removed seat 0 was numbered 1. The loop now selects occupied objects. `proof/b1-every-seat-pattern.json`: remove [0] counts [1,2,3,4]; remove [4] counts [0,1,2,3]; remove [1,3] counts [0,2,4]. No removed seat counted in any case. 1366x768.
2. **FIXED: Express giveaway and riders.** Before `before/b2-express-before.png`: three solids plus two leaving rings. After `final-frames/express.png` and `after/b2-express-minus.json`: five plain starting counters, leavers facing out at the open door. Consecutive facts advance rider identities. Rings appear only after reveal, as `extra/cheats-and-resume.png` shows. 1366x768.

#### Should fix
1. **FIXED: same-total Ten and School cards and relevant counting.** `before/s1-ten-cards.png` and `before/s1-school-count.png` reproduce distinct totals and counting zero objects. `proof/s1-ten-blue-count.png`: 7+3=10, 7+2=10, 7+4=10, numbering blue counters only. `proof/s1-school-rings-count.png`: all totals zero, numbering dashed rings. The final hint names the actual change. 1366x768. Automatic counting speech is replaced by Read-accessible feedback under Curiosity precedence.
2. **FIXED: Fill up range.** `before/s2-fill-missing.json` has no Fill up control and starts only 4 through 8. Shared Ten-stop machinery now draws from a shuffled nine-start bag. `proof/s2-fill-two-rides.json`: [8,7,9,3,2] then [5,4,6,1,8], covering every integer 1 through 9; all 30 cards end in 10. `final-frames/fill-cards.png`, 1366x768; `phone/phone-fill.png`, 375x812. Five buses continue into another set, without a finish screen.
3. **FIXED: Express Read.** Before `before/s3-express-read.json` contains only the generic action. `proof/s3-read-express.json` logs Read repeating the entire five-riders/two-off story before the action. `proof/s3-read-express.png`, 1366x768.
4. **FIXED: first story timing.** Before `before/s4-first-walk.json`, riders are already moving while only the road line has started. The redundant intro queue is removed. `proof/s4-first-walk.json`: story starts at 1324 ms; walk starts at 1324.5 ms. The story is also in the current Read hint. 1366x768.
5. **FIXED: Express second walk and closed door.** `before/s5-express-rewalk.png` reproduces the reset. `proof/s5-one-express-walk.json` at 2 s: shown=true, zero active walk classes, all three boarders at opacity 0, door open. `proof/s5-one-express-walk.png`, 1366x768.
6. **FIXED: full Split list action.** `before/s6-split-all.png` retains Keep it. `proof/s6-split-all.json` names More, Fewer and a place after all three ways of two. `extra/drive-all-ways-last-kept.json` says only Tap Drive on after all eight ways of seven. 1366x768.
7. **FIXED: Split discs and five-column rows.** Before compact discs measure 35 px in `before/s7-s8-split-ten-1000.json` and `before/s7-s8-split-ten-680.json`. After: 60 px at 1366x768 and 1000x625, 44 px at 680x425, two rows of five. `proof/s7-s8-split-ten-*.json` and final frames prove this. The extra 800x500 regression is fixed and measured at 60 px in `extra/split-ten-800.json`. Phone counters are 60 px: `phone/phone-split-ten.json`.
8. **FIXED: way-list marks and curves.** `before/s7-s8-split-ten-680.png` and its 1366 counterpart reproduce cramped marks. Dedicated arrow padding and outer-margin links replace overlays; compact layouts omit curves. Inspected `proof/s7-s8-split-ten-1366.png`, `final-frames/split-ten-680.png`, and `phone/split-ten-1000.png`. Mark glyph is U+2194, including at 680x425; the 1000-wide equations also stay on one line.
9. **FIXED: duplicate Split instruction.** `before/s9-split-voice.json` logs welcome at 1355 ms and repeated how at 6928 ms. `proof/s9-split-voice.json`, after a 14 s wait, contains one first-use hint and no second instruction. No welcome remains. 1366x768.

#### Polish accepted
1. **FIXED:** Tell first rejects cup, counter and Done edits; See again also waits for Go. `polish-proof/p1-tell-first.json`: hold, changed=[], cup disabled, Done disabled, Go shown. 1366x768.
2. **FIXED:** Express separate welcome removed. One fact-plus-action line includes saying the answer aloud. `polish-proof/p2-express-first-hint.json`, 1366x768; final manifest contains no old welcome.
3. **FIXED with Curiosity override:** no Express end screen. Five tickets stay visible while a fresh story arrives. `polish-proof/p3-express-ticket-roll.json`: five tickets, done=false, tiles visible, no finish overlay. Its 1366x768 frame shows the continuing instrument.
4. **FIXED:** stop names sit on each actual painted face. All 16 used scene images were inspected; six rural/stand scenes need different coordinates and vertical camera positions. `sign-coordinates.json` records the original-art source and measurements. Inspected all seven `sign-proof/sign-*.png` desktop frames and `sign-proof/sign-corn-phone.png` at 375x812. Final `sign-proof/grounded-orchard.png` and `grounded-corn-phone.png` retain a code-drawn foreground street while the camera keeps the original sign visible. Route frames exposed the differing orchard face before this final correction.
5. **FIXED:** driver's chart mark moved right. `polish-proof/p4-p5-maple-sign-driver.json`: right=5px; same frame and `final-frames/drive-cards-680.png` show it.
6. **FIXED:** ten waiting riders stand in two perspective rows, clear of the sign. `extra/crowded-curb.png/json`, 680x425: ten boxes, same-row horizontal gaps over 3 px and vertical row gap over 3 px; start=1 is genuinely generated by Fill up.
7. **FIXED:** Split says “Tap a rider counter to send it to the other side.” `proof/s9-split-voice.json` and `extra/calm.png`, 1366x768; old wording removed from source and voice manifest.
8. **FIXED:** Split equation uses one baseline. `final-frames/split-ten.png`, 1366x768; `final-frames/split-ten-680.png`; `phone/phone-split-ten.png`.
9. **FIXED:** fork medallions are on the actual branches at (165,63) and (165,136), with no selected stop on the trunk. The settled over-road question mark remains a separate junction marker when no branch is chosen (`post-audit/fork-junction.png`, 1366x768). `polish-proof/p9-fork-map.png/json`, 1366x768.
10. **FIXED:** each kept addend owns its dot picture; dots measure 5x5 px. Empty slots have no text. `proof/s7-s8-split-ten-1366.json/png`, `final-frames/split-ten-680.png`; 1000-wide spacing rechecked in `phone/split-ten-1000.png`.
11. **FIXED:** notes remove build talk and the old fallback-stage claim; the situation-types link is correctly named; Fill up is documented. `notes.md` Modes, Good to know, Standards and sources.
12. **FIXED:** idle-light element and styling removed. `final-frames/split-ten.png` and `extra/calm.png`, 1366x768.
13. **FIXED:** “Yes! Seven plus three…” is capitalised in the actual departure/Read hint. `extra/ten-capital-read.json/png`, 1366x768; expansions in the manifest use the same constructor.
14. **FIXED:** 80 generated Express sets produced both 2-add and 3-add mixes, each with five distinct facts. `polish-proof/p14-express-mix.json`: [2,3].
15. **FIXED:** Tell first uses a drawn speech-bubble SVG. Inspected `fix-audit/size-1366x768.png` and `post-audit/default-1366.png`; the final bubble is also visible in the scene-coordinate frames.
16. **FIXED:** cup label is Full when full, unavailable when disabled otherwise; Split equation is polite/atomic live text. `polish-proof/p16-cup-full.json`: Full, disabled=true, aria-live=polite. `proof/s6-split-all.json` confirms live updates. Full-bus hints name Done instead of the disabled cup, and drop the obsolete starting-seat readout. `post-audit/verified-full-focus.json` proves focus stays on Done after repeated full-cup presses and the exact current hint is “Every seat is full! Tap Done to explore the number sentences.”
17. **FIXED:** Drive Split ticket uses the last kept way. `polish-proof/p17-last-kept-ticket.json`: kept 7=6+1, then moved counters to 4+3, ticket remains 7=6+1. All-ways variant records 7=0+7 after another unsaved move: `extra/drive-all-ways-last-kept.json`.

#### Settled calls
- Same-total cards, concealed Express leavers and all nine Fill up starts applied.
- Cup stops at ten; no buzz, score, timer, first-try reward or new assessment gate. Plain Split counters retained.
- Curiosity precedence removes welcome sequences, the two-way travel quota and all ride-end overlays. A road can be explored without selecting a card.
- The over-road question-mark circle is retained at the junction, while both branch stops are separate, as item 9 requires.
- Existing painted art retained, with no new generated assets or downloads. Bundle is about 2.7 MB, under the 6 MB threshold; no Size line is required.
- No `refine.md` or `refine/` file was edited. No git commits. All writes stayed in this tool and its Scratch directory.

#### Cheats tried
- Done with 0, 1, 3, and ten cup taps at an on-2 stop: all remained show; ten taps stopped at seven changed seats. `extra/cheats-and-resume.json`.
- Both false cards in succession: no ticket added; remained tell. Selection by elimination remains allowed as the Refine settled, with no mastery claim.
- Repeated Keep without a move: one recorded way. Sweeping all groupings records real decompositions, not a grade.
- Rapid Express 0 through 5: first value 0 stayed selected; one reveal followed. Show me remains a deliberate exploration control.
- Picking a card just because it ends in ten or zero no longer identifies one candidate: all three totals match.
- Skipping via Drive on is intentional open navigation, not a success result. Fill up preserves the paused Drive state.

#### Voice walk
- Held clicks at 0.12 s, 2 s pace. Curiosity uses one first hint, then explicit Read; no unsolicited story/how queue remains.
- First Drive: Maple Street story-plus-action once; walk onset within 1 ms (`proof/s4-first-walk.json`).
- First Split: rider-counter instruction once, still once after 14 s (`proof/s9-split-voice.json`).
- First Express: fact then “Listen, say the answer out loud…” once (`polish-proof/p2-express-first-hint.json`).
- Read repeats the current full Express fact (`proof/s3-read-express.json`). Card Read speaks “Three plus two equals five” (`extra/card-read.json`). Keyboard Read is logged in `extra/keyboard-only.json`.
- The final runtime allLines array equals voice/lines.json exactly: 703 unique lines, verified from `post-audit/verified-full-focus.json`. No recordings were made; browser speech remains the existing fallback. Tests used muted Chrome and prove narration starts/logs, not recorded-clip listening quality.

#### The real material
- Complete original route data and 25 Express facts: `content.json`, Curio Class, CC BY 4.0 under repository `LICENSE-CONTENT.md`; code MIT under `LICENSE`. No sampling or external dataset added. `number-check.py` independently checks every route, all 25 facts and every fill partner; `numbers.json` records results.
- Named curriculum reference: NGA Center/CCSSO, https://www.thecorestandards.org/Math/Content/K/OA/, public licence https://www.thecorestandards.org/public-license/, rechecked 2026-11-06. Its licence is not CC BY/CC0; therefore no standards text or examples were copied into the instrument.
- Independent range/context check: Student Achievement Partners, https://achievethecore.org/page/932/situation-types-for-operations-in-word-problems, rechecked 2026-11-06. Reference only; no resource content incorporated. Arithmetic is additionally recomputed independently in Python and executed in JavaScript.
- Existing illustrations: generated with OpenAI gpt-image, edited for Curio Class; original project art under CC BY 4.0. No new painted art or outside art downloaded. Foreground street/curb surfaces are drawn in code to keep riders and wheels grounded under the adaptive scene camera. Manual and tool.draft.json name the material and licences.
- Ten-seat capacity and route places are explicitly fiction. No claim about an actual school bus or locality is made.

#### Curiosity short test and lesson creep
- Kid would open it unassigned: yes in my judgment, for moving the riders and choosing the roads. Adult play: the groupings and alternate branches support short exploratory play; no audience study or month-long-use claim is made.
- Real material is the interface: counters, finite arithmetic and conserved groups directly drive the scene. No score or finish is needed: every mode remains open.
- Reference frames opened and used: `before/model-beat-lab.png`, `before/model-elements-inspector.png`, `before/model-span-and-spire.png`, `before/model-pocket-universe.png`. Compare `extra/default.png` and `final-frames/split-ten.png` beside the Beat Lab frame: subject fills the screen, physical controls, no kit header or right-hand lesson panel.
- Search for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done: only the internal wrong-tile CSS class remains; welcome callback returns null. No student-facing ladder or success screen. The inherited optional sentence/number exploration is not a new quiz layer.
- Motion off: zero running animations in `extra/calm.json`. Keyboard-only mode entry and Read work. Phone iframe width and document scroll width both 375; cards bottom 487 px in an 812 px viewport.

#### Engine changes wanted
None. Shared kit, scripts and docs were not edited.

#### Audit
Completed once on port 9911, host 8715, within the 40-minute limit: `fix-audit/audit.md`, 166 mechanical leads. This is the preserved pre-targeted-repair snapshot, not a claim that every lead was a tool defect. No full audit was rerun.

- All 75 size/state/Motion frames were inspected through `audit-contact-0.png` to `audit-contact-9.png`, indexed by `audit-contact-index.txt`; problem frames and the final targeted frames were also opened at full size.
- The repeated 44 px flags at 680x425 are the explicit preview exception. The audit's “every size” text for some 44 px Split targets comes from duplicate identical findings in its aggregation; direct frames and measurements show 60 px outside the preview, including 375x812.
- Real 800x500 overlap repaired: chart bottom 254.09 px, cards top 259.98 px, replay bottom 246.08 px (`post-audit/cards-800.json`, `final-fill-800.json`). Express strip bottom 149.58, result top 154.58 and tiles top 189.58 px (`express-800.json`). All associated frames were inspected.
- Real compact Split label overlap repaired: label bottom 70.5 px, first counter top 72.5 px (`post-audit/split-680.json`).
- Real sign clipping repaired: tall 760-wide label stays within x=660.86 to 720.33; final phone choice label within x=292.73 to 342.08, with the bus ending at x=277.5. The small Corn Stand face is 45x40 px, with scrollHeight=clientHeight=36 (`sign-proof/corn-phone.json`). Every differing source face was rechecked as item 4 records.
- Real full-cup focus loss repaired by moving focus to Done and preventing disabled-cup pointer presses from dropping it. Repeated real held presses finish on Done (`post-audit/verified-full-focus.json`).
- Manual target and title leads repaired: topic summaries 60 px; phone source links 81 and 60 px; title right 227 px, Close left 240.39 px. All four topic headings fit initially, closed, with no title collision (`post-audit/manual-phone.json`, `manual-680.json`). Opening a long field-guide entry intentionally makes the drawer scroll.
- The hint being covered by an open modal Manual is intentional. The Manual's prose is scrollable; it is not a hidden short choice menu. The disabled “empty seat” matches are descriptive nouns in “Tap the cup to fill every empty seat”, not instructions to tap a disabled seat. Cup and Done remain the named actionable controls.
- All 13 held-click rows have no errors or lost keyboard focus. Five-click 2 s repeats and two quick-tap checks for Split, Express, Fill up, Read and all three roads are clean. No welcome is expected under the Curiosity brief.
- Original resize stress is clean: no exceptions or controls left disabled. An additional height-only resize from an 800x900 iframe to 800x500 keeps all ten 60 px counters within their painted area (`post-audit/height-only-resize.json`). Height changes now trigger layout updates as width changes do.
- Fill up also retains its visible waiting rider and three blue counters after a mode round trip, with zero restarted walks (`post-audit/ten-resume.json`).
- All six actual route paths were exercised through their controls and returned to the fork: `post-audit/route-park.json`, `route-library.json`, `route-farm.json`. Every observed count agrees with `numbers.json`; no finish overlay is present.
- Final bundle: 2,717,876 bytes (about 2.7 MB). JavaScript syntax and independent arithmetic checks pass. Focused drive batches report zero console warnings/errors. Scripts, styles, images and data are inline; no external runtime data loader is present. Source/reference links in the Manual do not fetch themselves. All owned Chrome processes and host servers were closed.

#### Left open
- Plate number: absent from this spec and the Curiosities catalog. `plate` is null and the engraved family plate is unnumbered.
- No recording generation was authorised by the applicable Ground rules. Fixed-line synthesis quality awaits the separate voice stage; this fix does not claim clips were heard.
- Two screenshot harness attempts timed out in DevTools; smaller batches succeeded. One earlier artificial Ten test produced undefined art because its fixture omitted rider IDs; corrected fixtures and all later batches had zero console errors.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Bus Stop handoff: Curiosity fix round 1

#### Current structure
The current source uses a full-width painted scene, working counter chart and bus dashboard. It uses kit JavaScript
for voice, tones and Motion/Sound/Read, with its own CSS and controls. No kit stylesheet, header or right-side lesson
panel remains. The lower-left Manual has a closed topic index, sources/licences and keyboard focus return.
New road stays reachable in the console on phones. Read always repeats the current story/action; card Read buttons
temporarily supply their own sentence to the same kit Read mechanism. At most one first-use hint speaks automatically.

Drive, Split, Express and Fill up retain state in memory. Fill up temporarily swaps in its own bus object and restores
the Drive object when leaving. Its shuffled bag covers starts 1 through 9 across the first two five-bus sets.
Express mixes two or three additions per five-story set and advances rider identities. Before reveal its counters
are plain starting riders; leavers wait facing out at the open door. Reveal has one walk, then static end positions.
Ten-stop/Fill-up redraws retain boarded riders as hidden, avoiding a second walk or reappearance after a mode switch.

The occupied-seat count selects solid/new objects; Ten feedback selects new counters; School selects gone rings.
Full cups retain focus on Done even under repeated pointer presses. Full hints describe the current full bus; partial
Ten hints identify the starting seats as starting seats. Split records ordered pairs and uses its last kept way on a
ticket. Five fixed columns and responsive areas preserve 60 px discs, except the explicitly allowed 44 px preview.
Resize handling responds to both height and width changes.

#### Curiosity precedence
The user explicitly classified this as a Curiosity. No welcome, grade, goal, score, level, finish screen or quiz layer
was added. Drive on does not require two recorded ways or a chosen card. School returns to the fork; Express and
Fill up continue into fresh sets with rolling recent tickets. The inherited sentence/number exploration is optional.
The older spec's teacher flow, automatic narration and ending instructions yield to CODEX-CURIOSITY.md.
No Bus Stop plate number exists in the spec or Curiosities catalog. The plate is deliberately unnumbered and metadata
has plate=null. Assignment remains for the owner; do not invent a number from another Curiosity.

#### Real material and art
content.json contains all original routes and all 25 Express facts. Stories, data and original illustrations carry
the project's CC BY 4.0 content licence; code is MIT. The Manual and tool.draft.json name these sources and licences.
The CCSS/SAP links are curriculum references only; their text or examples are not bundled as open data.
The ten-seat bus and all places are explicitly fictional. All arithmetic is independently checked in Scratch.
All existing painted assets are retained. No new painted images or recordings were generated.
Six of the 16 active scene images have differently positioned sign faces. The tool maps each face in image
coordinates and pans the scene to retain it; Scratch sign-coordinates.json records the source and measurement method.
Foreground road/curb drawing keeps wheels and riders grounded without covering the right-hand sign.

#### Evidence and maintenance
polish.md is the current item-level report; refine.md and refine/ are unchanged. Earlier build/review reports are
history. Scratch contains original-src.html, before/, proof/, polish-proof/, extra/, final-frames/, phone/, post-audit/,
sign-proof/ and the one fix-audit/. Audit contact pages/index cover all 75 mechanical frames.
The one audit finished, followed by focused repairs and frames. Its original 166-lead report is retained rather
than overwritten. polish.md resolves the real leads and explains preview/modal/description false positives.
number-check.py is a repeatable independent arithmetic/syntax extraction check. manifest-sync.py regenerates the
voice manifest from the current constructors without changing source. bundle.py is time bounded and saves its log.
Historical mutation helpers in Scratch were single-application edits; do not rerun them on the final source.

#### Sensitivity
People art was not redrawn or assigned new identities or stereotypes. Its original varied rider set and provenance
remain. This fix does not claim a new independent representation review or a recorded-clip listening review.

#### Engine changes wanted
None. No shared kit, script or document was edited.

#### Left open
The maker's plate number is unassigned. Existing browser speech is used until the separately authorised recording
stage; no clip-quality or offline recorded narration claim is made. See polish.md for the exact checked limits.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-08)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
