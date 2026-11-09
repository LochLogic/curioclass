# Codex review: push-the-pumpkin
## Played
- Kindergarten solo and teacher projection: Push exploration, all five Find out tests, all three Barn puzzles, wrong guesses, wrong comparisons and judgments. Best moment: the faster ball topples the bucket stack after the board-only wobble.
- Cold frames and first interactions preceded the builder account. Browser stalls and a restarting-roll test delayed full completion; under the stuck-command rule I opened source before the final cold sequence finished. This is a recorded ordering deviation, not a claim of a perfectly blind full run.
## Findings fixed
- **Blocker, general, Barn ghost:** no-piece replay invented a stop at post four instead of the original post five. Both balls now traverse their full recorded paths; calm replay reaches the same endpoints.
- **Should fix, family:pushes-and-pulls, Barn ramp:** uphill outcomes displayed a downhill-facing ramp. Mirror the placed ramp and the canvas snapshot away from Start.
- **Should fix, general, Barn near miss:** the short ball appeared to touch the oversized, offset doorway. Align the opening to the goal post and slightly reduce the building; keep the detailed painting.
- **Should fix, family:pushes-and-pulls, pulling art:** Jo's high, open hand did not grip the wagon. Redraw the pose with a low grasp, align Jo and extend the handle to it in Push and Find out. Rekey all six people cutouts to reduce colored edges.
- **Polish, general, Find out wall:** the payoff relied on text. Add the child's original guess pictures, observed pictures and paired recorded flags. Reflow compact and phone cards after targeted frames exposed overflow.
- Updated notes, handoff and audit states with the relevant corrections; no kit or shared files changed.
## Findings left
- **Nit, general, cutout edges:** a few colored pixels remain under magnification. Classroom-size scenes are clean enough; no further paint round.
- Browser speech is the current fallback. The named upbeat-guide recordings belong to the later media workflow; no audio was recorded here.
## Break it
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
## Voice walk
- Sound on, held 120 ms clicks and two-second action pace, with waits while result gates were live. Chrome muted; clip starts and text checked through __tool.vlog, not claimed as audible listening.
- Push: firstPush, bigFar, sideHow, findOut; side path included wagonHow, pullChoice, pulled, heavy and Read. Optional stale choice instructions may drop once the student has already acted.
- Find out: q1, prediction, try1, try2, compare, r1, surprise, nextHow; q2, prediction, planSmall, fair, try2, compare, r2, surprise; q3pre/q3/r3; q4pre/q4/r4; q5pre/q5/r5; claims, toBarn. Predictions and match/surprise lines accompany each test.
- Barn: b1, wrong verdict/cShort/goal1, judgeHow, worked verdict, a1/a1Fast, nextHow; b2, wrong verdict/cPond/goal2, worked verdict, a2/a2Way; b3, wrong verdict/cShort/goal3/fixHow, judgeBuckets, worked verdict, barnEnd.
- Counts: firstPush how expected 1 / spoken 1 across five Go actions; noRight event 5 / 5; cShort event 5 / 5; judgeHow how 1 / 1. Read and rapid mode switches were exercised without console errors. All 100 manifest lines exactly match allLines().
- The end-wall claims/toBarn tail was captured with real Next from the saved real-walk state after the original walk stopped at the wall. It was not one uninterrupted voice recording.
## Facts checked
- **Strength, direction, stopping and fair comparisons:** [NGSS K-PS2](https://www.nextgenscience.org/dci-arrangement/k-ps2-motion-and-stability-forces-and-interactions) and [NSTA K-PS2](https://my.nsta.org/ngss/DisplayStandard.aspx?id=10&view=dci). Both standards have actual student actions; no magnets or friction assessment.
- **Bigger push changes motion more; heavier modeled pumpkin moves less for the same push; force changes motion in its direction:** [NASA Glenn, Newton's Laws](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/). Distances and toy weights are conditional model values, not measurements or universal object comparisons.
- **An opposite push can slow or stop this ball; a board or collision can turn it or rebound it:** NGSS K-PS2 examples above and [OpenStax, Impulse](https://openstax.org/books/college-physics/pages/8-2-impulse).
- **A downhill ramp speeds the ball; an uphill ramp slows it:** NGSS K-PS2-2 and [OpenStax, Inclined Planes](https://openstax.org/books/physics/pages/5-4-inclined-planes).
- **Faster modeled ball topples the same stack where the slower ball wobbles it:** OpenStax Impulse above, under fixed collision conditions. Impact force also depends on contact duration; no universal speed-to-force claim added.
- Independent numbers: adjacent push ranges stay at least 0.7 post apart, farthest stop 5.15 posts, duration 1.005 to 2.445 seconds. Contrast matches the spec, including white/brand 5.489:1 and ink/paper 14.768:1.
- Spec-only arithmetic left unchanged: random no-repeat first-success means are 5.5, 7.667 and 15 tries, not 5.5, 11.5 and 22.5. The tool does not display those statistics.
## Sensitivity
- No cultural, Native, religious, hard-history or body topic. Jo is one fictional farm child; all six assets have people:true. A fresh representation reviewer should inspect the replacement pulling pose, anatomy, age, consistent identity and absence of stereotypes. No owner approval is claimed.
## Flattest moment left
- The first straight Barn roll is quieter than the turn, splash and bucket payoff. It establishes the required one-post-short baseline; the flat text-only end wall was lifted instead.
## Graphics
- All 23 named paintings inspected on the contact sheet and in scenes. Kept the rich farm art; redrew jo-pull with the built-in image tool; rekeyed six Jo poses. No named art is missing.
- Replacement files: art/raw/jo-pull.png and art/jo-pull.webp; final prompt and people tag are in art/prompts.json. The previous raw pose is preserved in Scratch.
- Art 740286 bytes; final pre-audit bundle 1117150 bytes, about 1091 KB. No recording bytes.
- Every STANDARDS size and mode inspected, including hosted 375x812. Also inspected all nine Barn outcome classes, the compact and phone recap, moving pull at laptop and preview sizes, grayscale, keyboard, calm ghost, and the actual run frames through numbered sheets.
## Audit
- **Audit not finished.** The single final run on Chrome 9941 and host 8745 exited on a 60-second DevTools .enable timeout before saving its first size. The outer limit was 40 minutes.
- No audit.md, PNGs or mechanical leads were produced. Scratch preserves its HTML snapshot and review-audit-failure.txt. No second audit was run; no mechanical PASS is claimed.
- Independent drive batches covered all required sizes, modes and the fixed frames, plus cheap-pass, voice, calm, grayscale and keyboard checks. Their successful rows do not replace the incomplete audit's full resize, focus and voice-edge coverage.
## Left open
- Unattended choices followed the spec and baseline. No questions, commits, recording, deployment or shared-file writes.
- Initial brief reads completed without an added process watchdog. Every bundle, browser batch and audit used an explicit deadline; later shell commands also used bounded runners.
- Several early CDP attempts stalled; their partial evidence is retained. The final successful walks and targeted checks are separate from those failures.
- Sound-off Read and every resize-mid-action combination were not independently completed when the audit failed. These remain verification gaps, not asserted passes.
- Temporary host favicon warning came from the wrapper, not the offline tool; the wrapper was corrected for its focused recheck and is removed at cleanup.
- Cleanup verified: Chrome ports 9940 through 9945 and host 8745 closed; ports 9946 and 9947 were unused; host.html absent.
