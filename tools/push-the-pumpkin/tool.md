# Push the Pumpkin: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: push-the-pumpkin

#### Built

Three complete modes: Push, five Find out investigations, and three Barn design puzzles. Teacher led, kindergarten, K-PS2-1 and K-PS2-2. The single offline bundle is 1115578 bytes (1089.4 KB). No commits, deployment or polish round.

Required source, draft metadata, notes, voice manifest, audit states, handoff and all named art are present. Work is confined to this tool and its Scratch folder. The starter's kit frame, settings, sound and Curio.voice are used. No shared engine was edited.

#### Numbers check

- Independent Python: `../../_scratch/push-the-pumpkin/verify_numbers.py` and `numbers.json`.
- All 76 JavaScript designs agree with the independent Python model: 10 / 22 / 44 designs, 1 / 2 / 2 working designs. Level three outcomes: 17 bounce, 11 patch, 7 wall, 4 short, 2 wobble, 1 hay, 2 worked.
- Noise leaves at least 0.7 post (53.2 design pixels) between adjacent strength ranges. Farthest stop 5.15 posts, within the six-post half path.
- Formula gives 1.005 to 2.445 seconds, correcting the spec's 1.05 to 2.4. The prescribed formula is used.
- No-repeat first-success means are 5.5, 7.667 and 15 tries. The spec's latter two means, 11.5 and 22.5, ignore the second working design. These statistics are not displayed to children.
- Independent random-order check: 4,984 of 10,000 first lanes were Big with the recorded seed. Runtime order uses Math.random and choices are shuffled.
- Contrast agrees with the spec: white/brand 5.489, brand/paper 5.148, ink/paper 14.768, muted/paper 6.555, ink/gold 9.457. Navy/path 3.969 and navy/field 3.982 are non-text marks.

#### Facts checked

Every science claim is conditional on this farm's same-object comparisons and fixed story conditions. Post counts, distances, relative toy weights and outcome tables are illustrative values.

- Strength comparisons and one-variable investigations: [NGSS K-PS2](https://www.nextgenscience.org/topic-arrangement/kforces-and-interactions-pushes-and-pulls).
- Pushes or pulls can change direction; a push opposite motion can stop a rolling ball: the same NGSS clarification, and [NASA Glenn, Newton's Laws](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/).
- A bigger push changes motion more; the heavier modeled pumpkin moves less for the same push: [NASA Glenn, Newton's Second Law](https://www.grc.nasa.gov/www/k-12/BGP/newton2.html). Equal conditions and relative toy weights are model assumptions.
- A ramp can speed a ball, and a structure can turn it: NGSS K-PS2-2's named design examples. The uphill-ramp failure is the inverse change in speed under the same model.
- Collision pushes can turn or rebound an object: NGSS K-PS2-1 and [OpenStax, Impulse](https://openstax.org/books/college-physics/pages/8-2-impulse).
- The faster modeled ball can topple the same bucket stack where the slower one only rocks it: OpenStax's momentum/impulse relation, with fixed collision conditions. This is not a universal speed threshold or a measured bucket experiment.
- No magnets, friction assessment, force addition, personal questions or new science topics were added. Jo and the farm are fictional.

#### Break it

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

#### Voice walk

Sound defaults on. Held clicks use 120 ms presses at a two-second tap pace. Chrome is muted as required; starts were checked through `__tool.vlog`, not claimed as an audible listening review. All 100 manifest lines match allLines. No audio was recorded.

- Push: firstPush once across five Go taps, then sideHow, findOut, wagonHow, pullChoice, pulled; Read repeats the current hint. Evidence: `voice-push.json`.
- Find out, in order: q1, prediction, try one/two, comparison, r1 and match; q2, planBig, fair, both tries, comparison, r2 and surprise; q3pre/q3/r3; q4pre/q4/r4; q5pre/q5/r5; claims, toBarn. Every prediction and result was heard. Evidence: `voice-find.json`.
- Barn: b1; five noRight/cShort pairs; goal1/fixHow; working verdict, a1/a1Fast, Next; b2, working verdict, a2/a2Way; b3, judgeBuckets, working verdict, barnEnd. Both analysis questions wait for the ghost race. Evidence: `voice-barn.json`.
- Current hints retain the situation and name a live next action. A stale optional choice catalogue is dropped after locking. Mode switches hush obsolete speech. The kit protects Read and preserves unsaid how lines.
- upbeat-guide is the selected bank voice. The build uses browser speech until that voice's recordings are supplied in the later media workflow.

#### Feel check

Best moment: the failed board-only bucket run wobbles, then adding the Start ramp makes the same board turn a faster ball into a tumbling stack. The student's own wrong judgment remains beside the corrected outcome.

Two flat moments were fixed: an apparently open doorway made the first failed roll ambiguous, so the door overlay now closes the whole opening until judgment; Jo's high hands made pushes look detached, so both pushing poses were repainted with low hands. The pond was also repainted as a usable isolated field object.

`bar-comparison.png` places the earned Barn finish beside Snowy Mail Route. Both bar tools were bundled into Scratch and opened without writing to their source folders. The farm retains comparable scene depth, large controls and visible causal feedback. This is a build self-check, not a classroom playtest or a polish round.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

130 build-check/reference PNGs reviewed, including the audit frames through numbered contact sheets and the preserved failed host check. Scratch directories: `first-frames`, `check-frames`, `functional`, `outcome-frames`, `final-frames`, `resume-frames`, `audit`, `post-frames`, `geometry-frames`, `strength-frames`, `catalog-frames`, `phone-wall-frames`. All art was inspected on contact sheets and in the scenes. Grayscale, keyboard, drag, Motion off and a 375-pixel iframe host are included.

#### Art made

23 named images, 724.2 KB of WebP, using the built-in OpenAI image tool. All are in art/raw and processed through art.py --rekey with despill. Three assets were redrawn: pond, jo-small, jo-big. All six Jo assets carry people: true and passed the fresh representation check, including the repainted poses. Full prompts and revisions are in art/prompts.json; sheets and review are in Scratch.

Voice: 0 KB recorded audio, as instructed. Final bundle 1089.4 KB against the 2 MB goal.

#### Art still to paint

None of the named assets. The spec's printed 19-plus-six total differs from its 17-plus-six named list; every named image is used. The contact sheet is ready for the owner; this unattended run does not claim the owner has personally seen it.

#### Engine changes wanted

None.

#### Left open

- Recordings for upbeat-guide remain part of the later voice workflow; browser narration is the current fallback.
- No classroom observation or audible listening evaluation was performed. A cold review is still expected under the build workflow.
- Spec arithmetic and first-piece interpretation corrections are documented in handoff.md; spec.md was left untouched.
- Reference-bar opening happened at the first-playable stage; the final scene was compared beside the reference before completion.
- All runners completed their Chrome/server cleanup, and every used debug/host endpoint is closed. host.html was moved into Scratch. WMI process inventory was denied, so cleanup was confirmed through runner completion and endpoint checks.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: push-the-pumpkin
#### Played
- Kindergarten solo and teacher projection: Push exploration, all five Find out tests, all three Barn puzzles, wrong guesses, wrong comparisons and judgments. Best moment: the faster ball topples the bucket stack after the board-only wobble.
- Cold frames and first interactions preceded the builder account. Browser stalls and a restarting-roll test delayed full completion; under the stuck-command rule I opened source before the final cold sequence finished. This is a recorded ordering deviation, not a claim of a perfectly blind full run.
#### Findings fixed
- **Blocker, general, Barn ghost:** no-piece replay invented a stop at post four instead of the original post five. Both balls now traverse their full recorded paths; calm replay reaches the same endpoints.
- **Should fix, family:pushes-and-pulls, Barn ramp:** uphill outcomes displayed a downhill-facing ramp. Mirror the placed ramp and the canvas snapshot away from Start.
- **Should fix, general, Barn near miss:** the short ball appeared to touch the oversized, offset doorway. Align the opening to the goal post and slightly reduce the building; keep the detailed painting.
- **Should fix, family:pushes-and-pulls, pulling art:** Jo's high, open hand did not grip the wagon. Redraw the pose with a low grasp, align Jo and extend the handle to it in Push and Find out. Rekey all six people cutouts to reduce colored edges.
- **Polish, general, Find out wall:** the payoff relied on text. Add the child's original guess pictures, observed pictures and paired recorded flags. Reflow compact and phone cards after targeted frames exposed overflow.
- Updated notes, handoff and audit states with the relevant corrections; no kit or shared files changed.
#### Findings left
- **Nit, general, cutout edges:** a few colored pixels remain under magnification. Classroom-size scenes are clean enough; no further paint round.
- Browser speech is the current fallback. The named upbeat-guide recordings belong to the later media workflow; no audio was recorded here.
#### Break it
- No points, percent meter, best score or saved mastery claim exists. Predictions are evidence, not a scored answer.
- **Predictions:** tapped Big, Small, Same rapidly; Big remained locked. Go cannot run before a prediction. Choice order varies.
- **Q1/Q2 comparison:** force the lower lane to be wrong, then tap both. Correction advances, but the first wrong comparison remains recorded. Strength badges hide while choosing; visible stop positions supply the evidence.
- **Q2 fair plan:** select Ball and run both tries. The unfair run is rejected, second lane clears, page stays empty and Ball is disabled; Pumpkin is required.
- **Page gates:** Go while busy and early Next do not skip a try or a result. All five pages filled from their own observations.
- **Barn judgments:** always Yes on short and wobble remains wrong and cannot finish a level. Not yet on a working run is corrected, with that wrong first judgment retained.
- **Design search:** all 76 legal designs independently enumerated and checked against the JavaScript model; 10/22/44 designs with 1/2/2 working ones. No correct-only glowing spot or fixed answer-card position.
- **Analysis:** tap Slower then Faster. The original Slower remains stored and gets its evidence-based correction. The spec permits continuing after correction; no mastery score is awarded.
- **Rapid controls:** twelve Go taps preserve the eight-flag cap. Repeated Roll restarts the run and never manufactures a judged success. Real whole-pixel dragging places the uphill ramp correctly.
- Evidence: review-cheats.json, review-more.json, their saved state files, review-model-result.json and review_assert.py in Scratch. Runtime assertions passed.
#### Voice walk
- Sound on, held 120 ms clicks and two-second action pace, with waits while result gates were live. Chrome muted; clip starts and text checked through __tool.vlog, not claimed as audible listening.
- Push: firstPush, bigFar, sideHow, findOut; side path included wagonHow, pullChoice, pulled, heavy and Read. Optional stale choice instructions may drop once the student has already acted.
- Find out: q1, prediction, try1, try2, compare, r1, surprise, nextHow; q2, prediction, planSmall, fair, try2, compare, r2, surprise; q3pre/q3/r3; q4pre/q4/r4; q5pre/q5/r5; claims, toBarn. Predictions and match/surprise lines accompany each test.
- Barn: b1, wrong verdict/cShort/goal1, judgeHow, worked verdict, a1/a1Fast, nextHow; b2, wrong verdict/cPond/goal2, worked verdict, a2/a2Way; b3, wrong verdict/cShort/goal3/fixHow, judgeBuckets, worked verdict, barnEnd.
- Counts: firstPush how expected 1 / spoken 1 across five Go actions; noRight event 5 / 5; cShort event 5 / 5; judgeHow how 1 / 1. Read and rapid mode switches were exercised without console errors. All 100 manifest lines exactly match allLines().
- The end-wall claims/toBarn tail was captured with real Next from the saved real-walk state after the original walk stopped at the wall. It was not one uninterrupted voice recording.
#### Facts checked
- **Strength, direction, stopping and fair comparisons:** [NGSS K-PS2](https://www.nextgenscience.org/dci-arrangement/k-ps2-motion-and-stability-forces-and-interactions) and [NSTA K-PS2](https://my.nsta.org/ngss/DisplayStandard.aspx?id=10&view=dci). Both standards have actual student actions; no magnets or friction assessment.
- **Bigger push changes motion more; heavier modeled pumpkin moves less for the same push; force changes motion in its direction:** [NASA Glenn, Newton's Laws](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/). Distances and toy weights are conditional model values, not measurements or universal object comparisons.
- **An opposite push can slow or stop this ball; a board or collision can turn it or rebound it:** NGSS K-PS2 examples above and [OpenStax, Impulse](https://openstax.org/books/college-physics/pages/8-2-impulse).
- **A downhill ramp speeds the ball; an uphill ramp slows it:** NGSS K-PS2-2 and [OpenStax, Inclined Planes](https://openstax.org/books/physics/pages/5-4-inclined-planes).
- **Faster modeled ball topples the same stack where the slower ball wobbles it:** OpenStax Impulse above, under fixed collision conditions. Impact force also depends on contact duration; no universal speed-to-force claim added.
- Independent numbers: adjacent push ranges stay at least 0.7 post apart, farthest stop 5.15 posts, duration 1.005 to 2.445 seconds. Contrast matches the spec, including white/brand 5.489:1 and ink/paper 14.768:1.
- Spec-only arithmetic left unchanged: random no-repeat first-success means are 5.5, 7.667 and 15 tries, not 5.5, 11.5 and 22.5. The tool does not display those statistics.
#### Sensitivity
- No cultural, Native, religious, hard-history or body topic. Jo is one fictional farm child; all six assets have people:true. A fresh representation reviewer should inspect the replacement pulling pose, anatomy, age, consistent identity and absence of stereotypes. No owner approval is claimed.
#### Flattest moment left
- The first straight Barn roll is quieter than the turn, splash and bucket payoff. It establishes the required one-post-short baseline; the flat text-only end wall was lifted instead.
#### Graphics
- All 23 named paintings inspected on the contact sheet and in scenes. Kept the rich farm art; redrew jo-pull with the built-in image tool; rekeyed six Jo poses. No named art is missing.
- Replacement files: art/raw/jo-pull.png and art/jo-pull.webp; final prompt and people tag are in art/prompts.json. The previous raw pose is preserved in Scratch.
- Art 740286 bytes; final pre-audit bundle 1117150 bytes, about 1091 KB. No recording bytes.
- Every STANDARDS size and mode inspected, including hosted 375x812. Also inspected all nine Barn outcome classes, the compact and phone recap, moving pull at laptop and preview sizes, grayscale, keyboard, calm ghost, and the actual run frames through numbered sheets.
#### Audit
- **Audit not finished.** The single final run on Chrome 9941 and host 8745 exited on a 60-second DevTools .enable timeout before saving its first size. The outer limit was 40 minutes.
- No audit.md, PNGs or mechanical leads were produced. Scratch preserves its HTML snapshot and review-audit-failure.txt. No second audit was run; no mechanical PASS is claimed.
- Independent drive batches covered all required sizes, modes and the fixed frames, plus cheap-pass, voice, calm, grayscale and keyboard checks. Their successful rows do not replace the incomplete audit's full resize, focus and voice-edge coverage.
#### Left open
- Unattended choices followed the spec and baseline. No questions, commits, recording, deployment or shared-file writes.
- Initial brief reads completed without an added process watchdog. Every bundle, browser batch and audit used an explicit deadline; later shell commands also used bounded runners.
- Several early CDP attempts stalled; their partial evidence is retained. The final successful walks and targeted checks are separate from those failures.
- Sound-off Read and every resize-mid-action combination were not independently completed when the audit failed. These remain verification gaps, not asserted passes.
- Temporary host favicon warning came from the wrapper, not the offline tool; the wrapper was corrected for its focused recheck and is removed at cleanup.
- Cleanup verified: Chrome ports 9940 through 9945 and host 8745 closed; ports 9946 and 9947 were unused; host.html absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Push the Pumpkin

Build only. No commits or polish round. Writes confined to this tool and its Scratch folder.

#### Structure

The kit starter supplies the document, settings and narration. Tool CSS lays out a real-pixel canvas beside a picture-card panel. Canvas drawings use generated paintings plus precise code posts, arrows, flags, trails and buckets. Accessible HTML controls overlay the comparison lanes and barn placement spots. Controls use tap placement and pointer drags.

The three state machines live in `src.html`: Push keeps its eight flags; Find out retains five test objects and honest first predictions and comparisons; Barn retains each level's design, run snapshot, original verdict and analysis answer. The rule model is separate from drawing. Editing during a roll changes only the next design, not the run snapshot.

`Curio.voice` owns the queue, Read and sound settings. The voice manifest selects upbeat-guide. No audio was recorded in this build. Browser speech is the fallback. Scope is mode plus test or level. Mode changes cancel obsolete speech; how lines use the kit's heard set.

#### Spec differences and decisions

- The named asset list has 17 non-person assets plus six Jo poses, 23 total. Its printed total says 19 plus six. All named assets are included.
- Noise plus the stated roll-time formula gives 1.005 to 2.445 seconds, rather than 1.05 to 2.4. Follow the formula, which remains below 2.5 seconds.
- The first-piece rule applies to obstacles after a Start ramp has changed speed. Otherwise the required ramp-and-board level cannot work. Exact enumeration matches all three design counts and every level-three outcome count.
- A random no-repeat search with two successes has expected first success at (n + 1) / 3: 7.667 and 15 tries for levels two and three, not 11.5 and 22.5. No such statistic is displayed to children.
- Open questions: the spec lists none. Jo has medium brown skin, curly dark hair, a mustard jacket, teal overalls and boots, consistent across six poses. The fresh representation check and owner contact sheet are retained in Scratch.
- The current build brief explicitly permits Codex-generated people and requires its image tool. This supersedes older Gemini-only and do-not-draw wording in BUILD and ART.

#### Sensitivity

No cultural, Native, religious or hard-history content. Jo is a fictional child. Check the six people-marked poses for anatomy, respectful representation and consistency before publication.

#### Engine changes wanted

None. Shared kit, scripts and docs were not modified.

#### Cold review changes

The ghost comparison now reaches the same no-piece endpoint as the original run. Uphill ramp pieces are mirrored in both the live HTML spot and the canvas result. The Barn opening is aligned to the door post and sized so the short ball stays visibly outside it. The test wall now shows the learner's picture choices and two recorded stop flags, rather than relying on text alone.

Jo's pulling pose was redrawn with a low backward grasp, matching the original child and painted style. All six people cutouts were rekeyed with enclosed-key cleanup to reduce their colored fringe. These assets remain people-marked in prompts.json. See the cold review report and review evidence in Scratch for independent checks and any remaining limits.

The cold review's final audit did not finish: Chrome DevTools timed out before the first size and no audit.md was saved. Independent all-size, design-model, cheap-pass and voice checks completed, but the full mechanical gate and all resize/voice edge cases remain unverified. See Scratch review-audit-failure.txt. All review Chrome endpoints and host 8745 were closed; host.html was removed.

#### Review next

See codex-report.md for measured checks, source links and any limitations. Record upbeat-guide narration in the later media workflow. This build has no classroom observation claim.

#### Verification details

Scratch `check_model.py` compares all 76 JavaScript designs with an independent Python model. `functional.py` walks all five tests and three levels using held pointer clicks, with intentional wrong comparisons, the unfair plan, wrong verdicts, a wrong analysis answer and a mid-roll edit. `voice_walk.py` walks the main Find out and Barn paths with Sound on, plus five repeated failed verdicts and the Push side path. `resume-shots.json` checks leaving during feedback and returning to the test or ghost comparison.

Images total about 724 KB. The pond was redrawn to remove an unwanted miniature farm, and the two pushing poses were redrawn with low hands. Every cutout was processed with despill enabled. The updated Jo sheet passed the fresh people-art check. The contact sheet is available to the owner in Scratch; this unattended build does not claim the owner has personally reviewed it.

The single full audit found 22 leads. Its HTML snapshot remains in Scratch. Four actual issues were repaired: compact Go clipping, a privacy-label overlap, a stale choice catalogue and focus loss on busy Go. The remaining leads concern first-action welcome skipping, inactive spots and comparisons across randomized or naturally completed runs. Focused checks verify those dispositions without a second full audit.

Final responsive rules keep the 680-pixel preview side by side, use 60-pixel ordinary-size controls, stack the 760-pixel portrait scene over a stable control desk, and give the completed phone wall extra height. Current hints retain the question situation for Read. Student work is session-only; the shared kit remembers Motion on this device.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
