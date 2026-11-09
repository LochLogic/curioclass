# Codex report: push-the-pumpkin

## Built

Three complete modes: Push, five Find out investigations, and three Barn design puzzles. Teacher led, kindergarten, K-PS2-1 and K-PS2-2. The single offline bundle is 1115578 bytes (1089.4 KB). No commits, deployment or polish round.

Required source, draft metadata, notes, voice manifest, audit states, handoff and all named art are present. Work is confined to this tool and its Scratch folder. The starter's kit frame, settings, sound and Curio.voice are used. No shared engine was edited.

## Numbers check

- Independent Python: `../../_scratch/push-the-pumpkin/verify_numbers.py` and `numbers.json`.
- All 76 JavaScript designs agree with the independent Python model: 10 / 22 / 44 designs, 1 / 2 / 2 working designs. Level three outcomes: 17 bounce, 11 patch, 7 wall, 4 short, 2 wobble, 1 hay, 2 worked.
- Noise leaves at least 0.7 post (53.2 design pixels) between adjacent strength ranges. Farthest stop 5.15 posts, within the six-post half path.
- Formula gives 1.005 to 2.445 seconds, correcting the spec's 1.05 to 2.4. The prescribed formula is used.
- No-repeat first-success means are 5.5, 7.667 and 15 tries. The spec's latter two means, 11.5 and 22.5, ignore the second working design. These statistics are not displayed to children.
- Independent random-order check: 4,984 of 10,000 first lanes were Big with the recorded seed. Runtime order uses Math.random and choices are shuffled.
- Contrast agrees with the spec: white/brand 5.489, brand/paper 5.148, ink/paper 14.768, muted/paper 6.555, ink/gold 9.457. Navy/path 3.969 and navy/field 3.982 are non-text marks.

## Facts checked

Every science claim is conditional on this farm's same-object comparisons and fixed story conditions. Post counts, distances, relative toy weights and outcome tables are illustrative values.

- Strength comparisons and one-variable investigations: [NGSS K-PS2](https://www.nextgenscience.org/topic-arrangement/kforces-and-interactions-pushes-and-pulls).
- Pushes or pulls can change direction; a push opposite motion can stop a rolling ball: the same NGSS clarification, and [NASA Glenn, Newton's Laws](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/).
- A bigger push changes motion more; the heavier modeled pumpkin moves less for the same push: [NASA Glenn, Newton's Second Law](https://www.grc.nasa.gov/www/k-12/BGP/newton2.html). Equal conditions and relative toy weights are model assumptions.
- A ramp can speed a ball, and a structure can turn it: NGSS K-PS2-2's named design examples. The uphill-ramp failure is the inverse change in speed under the same model.
- Collision pushes can turn or rebound an object: NGSS K-PS2-1 and [OpenStax, Impulse](https://openstax.org/books/college-physics/pages/8-2-impulse).
- The faster modeled ball can topple the same bucket stack where the slower one only rocks it: OpenStax's momentum/impulse relation, with fixed collision conditions. This is not a universal speed threshold or a measured bucket experiment.
- No magnets, friction assessment, force addition, personal questions or new science topics were added. Jo and the farm are fictional.

## Break it

- Prediction sweep: selecting another card after the first choice cannot overwrite the prediction. Go is unavailable before the prediction, and Q2 also requires a plan.
- Always lower lane and mash both lanes: lane order varies, badges disappear for comparison, a miss shows post dots, and the first compare remains wrong after correction. The page cannot fill from a wrong compare.
- Pick the faster Ball as Q2's plan: the unfair run plays, is rejected, leaves the page empty and greys out that plan. The fair Pumpkin plan is required.
- Mash Go or Next: no test skips its prerequisite or completed tries. Result narration finishes before Next can open the next question. Busy test taps cannot add a second run.
- Always Yes: the first short roll and the slow bucket wobble remain failures. Always Not yet on a working run is corrected; the original wrong judgment remains in the try record.
- Guess every analysis card: only the first answer is recorded. A wrong analysis receives an evidence-based correction rather than an invented score.
- Search designs: all allowed spots glow, including wrong placements. There is one of each piece and one board at a time. There is no best score, point reward or saved success to inflate.
- Change a piece mid-roll: the visible new design applies to the next Roll; the active run uses its immutable design snapshot. Roll restarts immediately. Rapid Push Go plants the interrupted flag and preserves the eight-flag cap.
- Clear, Pull visibility, all three strength orderings, wrong predictions, wrong comparisons, unfair plans, wrong judgments and wrong analyses were exercised. Evidence: `functional/state.json`, `model-check.txt`, and `strength-*.json` in Scratch.
- Leaving during a result or verdict initially risked a hidden Next or a stranded ghost phase. Fixed; both result-resume and calm-ghost-resume checks pass.

## Voice walk

Sound defaults on. Held clicks use 120 ms presses at a two-second tap pace. Chrome is muted as required; starts were checked through `__tool.vlog`, not claimed as an audible listening review. All 100 manifest lines match allLines. No audio was recorded.

- Push: firstPush once across five Go taps, then sideHow, findOut, wagonHow, pullChoice, pulled; Read repeats the current hint. Evidence: `voice-push.json`.
- Find out, in order: q1, prediction, try one/two, comparison, r1 and match; q2, planBig, fair, both tries, comparison, r2 and surprise; q3pre/q3/r3; q4pre/q4/r4; q5pre/q5/r5; claims, toBarn. Every prediction and result was heard. Evidence: `voice-find.json`.
- Barn: b1; five noRight/cShort pairs; goal1/fixHow; working verdict, a1/a1Fast, Next; b2, working verdict, a2/a2Way; b3, judgeBuckets, working verdict, barnEnd. Both analysis questions wait for the ghost race. Evidence: `voice-barn.json`.
- Current hints retain the situation and name a live next action. A stale optional choice catalogue is dropped after locking. Mode switches hush obsolete speech. The kit protects Read and preserves unsaid how lines.
- upbeat-guide is the selected bank voice. The build uses browser speech until that voice's recordings are supplied in the later media workflow.

## Feel check

Best moment: the failed board-only bucket run wobbles, then adding the Start ramp makes the same board turn a faster ball into a tumbling stack. The student's own wrong judgment remains beside the corrected outcome.

Two flat moments were fixed: an apparently open doorway made the first failed roll ambiguous, so the door overlay now closes the whole opening until judgment; Jo's high hands made pushes look detached, so both pushing poses were repainted with low hands. The pond was also repainted as a usable isolated field object.

`bar-comparison.png` places the earned Barn finish beside Snowy Mail Route. Both bar tools were bundled into Scratch and opened without writing to their source folders. The farm retains comparable scene depth, large controls and visible causal feedback. This is a build self-check, not a classroom playtest or a polish round.

## Done when

1. PASS: scene dominates the laptop layout; controls and hint remain in view. All STANDARDS sizes were shot. The compact locked-prediction layout was repaired and targeted again.
2. PASS: Small/Medium/Big ordering for Ball, Pumpkin and Wagon; opposite-side travel; wagon-only Pull; two-post following; eight flags and Clear. Model bounds and actual strength runs agree.
3. PASS: predictions lock, comparison badges hide, first taps remain recorded, wrong comparisons show dots, order varies.
4. PASS: all five pages fill from actual tries; the direction, pull, pass-Jo and stop-at-Jo runs match the specified endpoints.
5. PASS: the unfair Ball try runs and is rejected; only the fair Pumpkin comparison fills Q2.
6. PASS: judgment precedes door/cheer state, try records retain said/actual, first roll is short, and the slow bucket run wobbles.
7. PASS: all nine outcome classes were drawn and inspected; all allowed spots glow; both ghost comparisons precede their analysis cards; first analysis taps persist.
8. PASS: rapid Go, choice changes, Roll restarts and immutable run snapshots; result-before-question narration; mode changes do not strand results.
9. PASS for the instrumented solo path: picture choices, voiced questions, choices, next steps and full Sound-on Find out/Barn completion. No child-user observation is claimed.
10. PASS: firstPush heard once; five failed Barn verdicts and causes all heard. No stale choice catalogue starts after locking.
11. PASS: same roll/ghost beats with Motion off, stable end states, no infinite CSS animation, inline resources only.

## Wave lessons

- Hint and voice: PASS. Read repeats current context; how lines use V.heard; main and side voice paths retained in Scratch.
- Focus and layout: PASS after the targeted fixes. Busy Go retains focus; entering predictions/plans focuses a live card; results use a deliberate scene focus before Next.
- Sizes: PASS. All eight required sizes inspected; compact/phone exceptions use 44 px and ordinary school-size controls use at least 60 px. No scene text is below ten pixels.
- No giveaways: PASS. Prediction order shuffled, comparison strength badges hidden, all legal placement spots glow, original answers retained.
- Honest numbers: PASS. No score or hidden precision meter. Model assumptions and story values are named in notes.
- Standards: PASS. The learner actually predicts, plans, compares, judges and analyzes; both listed standards have interactive work.
- Motion off: PASS. End-state beats retain timing, including the ghost comparison. Art is present rather than placeholder circles.
- Short choices: PASS after compact grid repair. No short answer set is hidden in a scrolling panel.
- Resize mid-animation: PASS after targeted checks of the audit's three resize leads; the model clock and canvas geometry remain independent.
- Welcome timing: PASS under BASELINE 16. First taps with their own action/instruction skip the Push welcome; Find out and Barn speak their actual opening questions.
- Unknown, consistent meanings, truthful badges and reversible hints: PASS. No verdict state appears before judgment; predictions and original verdicts stay distinct from observed results.
- No copied-word answers: PASS. Comparison uses stop locations; design analysis follows the ghost paths rather than a displayed correctness meter.

## Audit leads

The full audit completed with 22 leads and no browser exceptions. All base sizes were clean. All five-click and quick-tap rows were clean.

- 1 compact Go clipping lead: fixed with a two-column compact choice set. Final 680, 800 and 1000 checks return empty geometry-error lists; 60-pixel ordinary-size targets were verified separately.
- 1 stale choice-catalogue lead: fixed with a prediction-phase validity guard. Final Sound-on log drops choices1 as stale, then speaks pred-big and try1. An already-playing question may finish, as specified.
- 1 privacy/Go overlap lead: fixed with shorter cards at 1280x720. The repaired frame has clear separation. Privacy copy now distinguishes unsaved work from the kit's remembered Motion preference.
- 1 Go-focus lead: fixed by retaining the busy Go control and guarding its handler. A held-click check preserves test-go focus. Results and prediction transitions deliberately focus a live target without scrolling.
- 2 randomized prediction resize leads (#guess-big, #guess-same): fresh pages shuffle card positions, so comparing enabled card IDs across those pages is not a valid lock test. Targeted semantic checks for both choices retain the selected key and disable exactly the other cards through resize.
- 1 Roll resize lead: the longer resized run naturally reached judgment, where Roll and the tray are hidden/disabled. The targeted check reaches thumbs, accepts Not yet and confirms Roll and pieces return; no stuck state.
- 3 inactive-spot leads (Start, post three, post four-and-a-half): intentional. Without a selected piece no spot glows; the spec says these taps do nothing. All legal spots glow once a piece is selected.
- 12 welcome leads: m-find, m-barn, pick-ball, pick-pumpkin, pick-wagon, size-0, size-1, size-2, side-barn, side-gate, go and clear. Each first tap has its own instruction/action. Skipping the Push welcome is permitted by BASELINE 16; the current premise remains in the hint/Read, and mode opening questions were heard.

Additional focused repairs keep the 760-pixel portrait scene proportionate, retain a usable phone end wall, place the ready ball at the Start ramp's top, and keep Jo beside the stopped pulled wagon. An initial phone-wall check hit a host-runner ownership race; its cleanup was corrected and that host check was repeated successfully.

The single full audit is a pre-fix snapshot, retained in `audit/host/tool.html`. Repairs were checked in focused shots rather than running a second full audit. Audit target 44 reflects the compact allowance; focused checks additionally require 60 at the ordinary school sizes.

## Frames looked at

130 build-check/reference PNGs reviewed, including the audit frames through numbered contact sheets and the preserved failed host check. Scratch directories: `first-frames`, `check-frames`, `functional`, `outcome-frames`, `final-frames`, `resume-frames`, `audit`, `post-frames`, `geometry-frames`, `strength-frames`, `catalog-frames`, `phone-wall-frames`. All art was inspected on contact sheets and in the scenes. Grayscale, keyboard, drag, Motion off and a 375-pixel iframe host are included.

## Art made

23 named images, 724.2 KB of WebP, using the built-in OpenAI image tool. All are in art/raw and processed through art.py --rekey with despill. Three assets were redrawn: pond, jo-small, jo-big. All six Jo assets carry people: true and passed the fresh representation check, including the repainted poses. Full prompts and revisions are in art/prompts.json; sheets and review are in Scratch.

Voice: 0 KB recorded audio, as instructed. Final bundle 1089.4 KB against the 2 MB goal.

## Art still to paint

None of the named assets. The spec's printed 19-plus-six total differs from its 17-plus-six named list; every named image is used. The contact sheet is ready for the owner; this unattended run does not claim the owner has personally seen it.

## Engine changes wanted

None.

## Left open

- Recordings for upbeat-guide remain part of the later voice workflow; browser narration is the current fallback.
- No classroom observation or audible listening evaluation was performed. A cold review is still expected under the build workflow.
- Spec arithmetic and first-piece interpretation corrections are documented in handoff.md; spec.md was left untouched.
- Reference-bar opening happened at the first-playable stage; the final scene was compared beside the reference before completion.
- All runners completed their Chrome/server cleanup, and every used debug/host endpoint is closed. host.html was moved into Scratch. WMI process inventory was denied, so cleanup was confirmed through runner completion and endpoint checks.
