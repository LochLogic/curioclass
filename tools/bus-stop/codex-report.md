# Codex report: bus-stop

## Built
- Build only in `S:\CurioClass-codex`. Tool writes are confined to `tools/bus-stop/` and `_scratch/bus-stop/`.
- Drive: three roads, two forks each, carried riders, counter modeling, shuffled sentence cards, Split and Ten stops,
  Tell first, replay, six earned story tickets, school ending and restoration of the earlier fork.
- Split: two through ten riders, every ordered decomposition, retained lists per number, duplicate feedback,
  linked turn-around pairs and a complete-set line. Three pairs of painted play areas.
- Express: five facts per ride, no repeats, at least two of each sign, first-answer lock, reveal and Again.
- Kit starter frame, Curio.voice, chimes, Sound, Motion and Read. No shared file changed, no commits, no polish round.
- Evidence lives under `_scratch/bus-stop/`. The report was started at the first bundle and completed after checks.

## Numbers check
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

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
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

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Both bar frames; all five quick frames; all twelve full-size frames, including gray/calm and keyboard.
- All six route frames, three side frames and five interaction frames, individually or on labeled contact sheets.
- Updated 680/1366/375 card frames, Split at 680, all 59 processed art assets and the 23-person contact sheet.
- `voice-final.png`, the focused card proofs, rider identity, five-wrong, Go and linked-Split frames.
- All 57 audit PNGs were inspected on the ten labeled audit-contact pages, with the reported collision inspected separately.
- Final Express fit/stability, the uncut active-mode frame, and the unobstructed six-ticket school ending were also viewed.

## Art made
- 59 final assets: 19 stop scenes, 6 play areas, 9 icons, 2 bus poses, 20 child poses and 3 driver portraits.
- 23 people assets, each marked people:true. Built-in image generation; full prompts and copied crops are retained.
- Seven rural scenes were redrawn individually after tall atlas cells failed the layout. Key-color spill was removed.
- Processed art: 1910.8 KB. Final self-contained bundle: 2756.4 KB. Voice recordings: 0 KB. The 2 MB goal is exceeded to keep every teaching scene and person;
  backgrounds were reduced to 800 px at quality 72. The bundle remains below the 6 MB documentation threshold.

## Art still to paint
None. The contact sheet and independent representation review still belong to the later review/shipping workflow.

## Engine changes wanted
None.

## Left open
- Recorded bright-teacher / Autonoe narration is a separate stage, as this Build forbids recording.
- Fixed-spec K.OA.A.4 coverage is four through eight, not every starting number one through nine.
- Fresh representation review and owner contact-sheet view have not been claimed by this Build.
- Some earlier frames precede small focused fixes; corrected frames and logs are named above. Audit was run once,
  and its leads were addressed with focused checks rather than rerunning the complete suite.
- Host files and servers were kept in Scratch, so no host.html was added to the tool folder. Test Chrome and host processes were closed.
