# Codex report: story-graphs

## Built

Build only in S:\CurioClass-codex. No commits, branch operations, deployment or polish round.
Match, Sketch and Model contain 25 stories, three complete core sets, spare stories and local progress.
The tool uses the unchanged kit voice and graphing engines, a comic notebook, 46 original illustrations,
responsive controls, keyboard drawing, pointer dragging, comparisons, playback and immutable round marks.
Delivered src.html, content.json, tool.draft.json (stage built), notes.md, handoff.md, voice/lines.json,
audit-states.json, art/prompts.json, 46 WebP files and the generated self-contained HTML.
Helpers, contacts, checks and frames are in ../../_scratch/story-graphs/. host.html was removed.
All assigned Chrome ports are closed. A remaining host on 8775 is documented under Left open.
Deadlines: reads usually 30 s, bundles 120 s, drive batches 300 s, the single audit 2,400 s.

## Numbers check

content.py and numbers.json recompute every model display point using exact fractions: all 29 fit.
Only A satisfies independent story rules for M1-M9; every card has the same piece count and start.
A shares its end with a trap in M1-M8. The six-pick guessing chance is 0.024414 percent.
Two-check tag guessing gives 8.163, 2.332 and 0.666 percent for two, three and four pieces.
Pool full: 26 minutes. Tank empty: 30 minutes. Swan gone: 40 hours. Ferry docks: 12 minutes, 30 km/h.
Bowling: 4 times 5 plus 5 is 25; 4 times 2 plus 5 is 13.
Gift card zero: 80/7 smoothies, about 11.4; eleven whole purchases are affordable. Spec rounding noted.
All seven working sketches pass; collinear straight pieces merge correctly.
Seeded random probes, 200,000 per story: K1 0.0525%, K2 0%, K3 0%, K4 0.08%, K5 0.0065%, K6 0.001%, K7 0.009%.
These samples differ from the spec's random sample, rather than from its checker rules.
Contrast recomputed: brand/paper 9.43, white/button 11.97, ink/paper 14.75, muted/paper 5.92,
blue/paper 9.85, orange/white 5.02, right/white 7.13, wrong/white 6.57, focus/paper 4.93.

## Facts checked

- Constructing a model, interpreting its rate and start, qualitative descriptions and sketches:
  Common Core 8.F.B.4 and 8.F.B.5, https://www.thecorestandards.org/Math/Content/8/F/
- Distance slope, faster/steeper, stops and returning toward home:
  OpenStax Physics 2.3, https://openstax.org/books/physics/pages/2-3-position-vs-time-graphs
- Steady flow raises water faster through a smaller cross-section:
  OpenStax Calculus 4.1, https://openstax.org/books/calculus-volume-1/pages/4-1-related-rates
- A tossed ball slows upward and speeds downward, neglecting air resistance:
  OpenStax University Physics 3.5, https://openstax.org/books/university-physics-volume-1/pages/3-5-free-fall
- Rate and initial value in a linear model:
  OpenStax Elementary Algebra 4.5,
  https://openstax.org/books/elementary-algebra-2e/pages/4-5-use-the-slope-intercept-form-of-an-equation-of-a-line
- All people, stories, prices and amounts are fictional. Model labels them Made-up story.
  Every displayed numerical scenario comes from the spec and was recomputed above.
- Teacher context about reading graphs as pictures is attributed to Leinhardt, Zaslavsky and Stein (1990)
  and Shell Centre (1985), as cited by the spec. No historical or cultural claim is taught.

## Break it

- Match: one locked pick; trying a correct card after a wrong pick cannot replace the first choice.
  M1 D produces the backward-time read-back, reveals A and ultimately records Partly, adding M7.
  Shuffled positions, identical styling, equal piece counts and shared endpoints prevent superficial cues.
- Tags: incomplete tags disable Check. A second wrong Check shows the correct tags and struck-through attempts.
  M5's third-piece Straight error marks that piece only. Two failures never earn Matched.
  Shown correct tags now carry checks, not the previous attempt's X; strike-through text stays legible.
- Sketch: hill pictures, a flat ball top, straight tents, wrong bends, missing returns, wrong rates and extra stops fail.
  113 deterministic checks passed, plus 1.4 million random sketches. No example is visible before the second failure.
  Two failures, Clear graph and a correct third practice check keep Shown with tries=3.
  Backward placement spoke once despite repeated attempts. A tenth point was refused; nine remained.
  Free draw returns the original challenge unchanged and awards no mark.
- Model: malformed numbers fail parsing; blanks disable Check. Swapped numbers, wrong signs, reciprocal slopes
  and a first-point intercept all fail. No student line appears before Check or changes while typing.
  Real typing accepted 3/20. Every model point was checked. Meaning choices lock after one tap;
  tapping the revealed correct card after a wrong one cannot change the result.
- Marks: Next requires a settled round; spare additions happen once. Reload preserved Shown.
  Clear progress asks once in an accessible dialog, then resets all marks and spare counts.
  Editing a checked sketch now identifies the saved result as historical, without claiming the edited graph passes.

## Voice walk

Muted Chrome used held clicks, about 120 ms, at a two-second tap pace. Narration uses Curio.voice and browser speech.
The first Match selection correctly skips the welcome: matchChoose, pickWrong, tagHow, tagsRight, nextHow.
Later rounds exercised pickRight, tagsWrong and tagCheck. A queued tagCheck initially saw the old disabled button;
it now queues after the rebuilt controls. The targeted retest heard matchChoose, pickRight, tagHow, tagCheck, tagsRight.
Sketch heard wSketch, sketchCheck, bendHow, sketchWrong and sketchRight. The Free draw side path heard freeHow.
Repeated backward placements produced one spoken backInTime. How lines were heard once, not repeated per point.
Model heard wModel, modelWrong, modelRight and meaning results. Result keys are distinct for m and b,
so one queued result cannot replace the other. Retest: modelRight, meaningRight-m, meaningRight-b, Read.
Read spoke the current hint and Lucia bubble. First-tap cuts and later action cuts are allowed by BASELINE rule 16.
voice/lines.json specifies playful-friend and the requested style; no audio was recorded during Build.

## Feel check

Played the core paths through the three modes. Match reached Matched 6, Partly 1; Model Matched 6, Partly 3.
Sketch was split into K1 and a K2-K6 walk after correcting a pointer-test edge click and a connection reset.
Best moment: replacing the hill-picture mistake with a continuously increasing sketch, then seeing its words light up.
Flattest moment 1: narrow, unequal compact graph cards. Equal 2x2 tracks now keep the comparisons fair and readable.
Flattest moment 2: a large, empty description panel in Model. The painted pool and ice swan now fill that space
without adding answer labels. Wrong table checks also retain the given table beside the checked line.
Compared both benchmark tools. feel-comparison.png places this tool beside Beat Lab; bar-comparison.png uses Snowy Mail Route.
The notebook has rich places and characters, direct choices and a clear payoff, with no confetti or points.

## Done when

1. PASS: cards/tag graph, sketch plane, and model representation/template dominate their stages.
2. PASS: full-size and compact frames keep the needed controls visible; 375 host and all eight target sizes inspected.
3. PASS: real M1 D pick, backward read-back, A check, Partly mark and M7 spare verified.
4. PASS: M5 correct tags and the third-piece-only X verified; second-failure shown tags inspected at 680.
5. PASS: K1 hill fails with heads back toward home; working T/S sketch passes. Playback is 1.2 s per part, 2.4 s here.
6. PASS: K4 plateau reads three parts against two and fails; the working L/S sketch passes.
7. PASS: R2 4/5 passes; swapped note verified with actual typing; reciprocal and first-point notes tested directly.
8. PASS: R3 four-card sets use the same number; first tap locks and the right loss-of-3 meaning receives the check.
9. PASS: Next interrupts playback; Motion off lights both rows with no dot or infinite animation.
   An independent resize probe began during playback, retained points and left Next enabled.
10. PASS: the held-click voice walks and targeted repairs above verify the requested pacing, Read and once-only how lines.
11. PASS: reload, local privacy, confirmation reset, naming, no em dashes and offline bundle checked.
    Completed browser walks logged zero product console errors or HTTP requests. The mechanical audit remains partial.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously; Read reads them; queue timing and unique result keys retested.
- Focus and layout: PASS. No focus taken on load; focus now moves from a removed Choose to piece 1 and from a
  disabled check or locked meaning choice to the next useful control. Targeted focus and all layout frames inspected.
- Sizes: PASS. Compact graph targets now measure about 45.97 pixels; named ground/empty/lobby labels have room.
- No giveaways: PASS. Uniform graph cards, shuffled choices, locked attempts, no live model line or answer meter.
- Honest numbers: PASS. Fiction is labeled, units are explicit in Model, computations are independently checked.
- Standards: PASS. Solo actions teach both 8.F.B.4 and 8.F.B.5 through all four linear-model representations.
- Motion off: PASS. No infinite animations; static row highlighting verified independently of the interrupted audit.
- Short choice sets: PASS. All four graphs and all eight meanings fit the inspected laptop and compact states.
- Resize mid-animation: PASS for the independent playback probe; the audit's complete resize sweep did not run.
- Delayed welcome: PASS. No welcomeAfter; the initial selection can skip the welcome without losing the premise.
- Unknown as unknown: PASS. Student model lines and example sketches stay hidden until the permitted checks.
- One look, one meaning: PASS. Blue givens, orange dashed student work, plus check/X icons and textual marks.
- Badge truth: PASS. Shown cannot become Matched; post-check edits now use historical-result wording.
- Hints change back: PASS. Mode switches, Free draw return and clears restore the appropriate next action.
- No copying words: PASS. Graph choices require shapes; all meaning cards contain the same number with competing units/roles.

## Audit leads

Single run: ../../_scratch/story-graphs/audit/audit.md. It saved 31 leads through Free draw states, then stopped
at scripts/audit_tool.py:412, KeyError: '1'. The full calm, walk and resize stages were not reached.
The partial report's default clean lines in those sections are not evidence that those stages ran.
Every saved lead is addressed here, grouped by its shared cause:

- Wrapped sentence and Made-up story bounding-box overlaps: inspected; inline fragments occupy separate visible text,
  although their union rectangles overlap. No glyph collision was found in the named compact/portrait frames.
- Empty model inputs reported unnamed: explicit aria-labels added alongside their existing associated labels; retested.
- Dialog hides background text and covers #hint/#actions: expected modal behavior. Its two current controls stay visible,
  background controls are inert, Keep progress receives focus, and confirmation/cancel return focus safely.
- Card-label/verdict overlap: inspected; the label rectangle spans the card while the check/X occupies its far right.
  The Graph number and verdict glyph do not collide.
- Choose focus fell to the page: fixed with successor focus. Retest focus is tag-piece-0; Model ends at next.
- Graph path crosses numbered pieces/text: the plotted stroke passes behind opaque foreground circles; frames show it masked.
- Three 43-pixel sketch targets at 680: fixed with content-box sizing and larger hit circles; retest about 45.97 pixels.
- Audit 375 iframe context/#hint failure: helper coverage gap; the independent 375 host showed the hint and controls,
  and its cleaned recheck logged zero errors. Read was separately verified.
The numeric audit fixture now uses input events for the helper's unsupported digit step; actual Model typing was already tested.
Only affected states were re-shot after repairs; the whole audit was not rerun. Final fixes also corrected gas wording,
compound-sentence links, shown-tag icons/strikes, post-check edit wording and pointer-based chip dragging.

## Frames looked at

Every captured frame was viewed individually or on the inspection sheets; critical 680 and phone states were also opened full size.
Folders: final-frames, extra-frames, extra-recheck, side-frames, side-retry, last-frames, postfix-frames,
art-final-frames, interactions, walk-match, walk-model, walk-sketch, walk-sketch-first and the audit's 49 frames.
The earlier first-retry and compact-retry frames and both benchmark frames were inspected too.
Inspection sheets, art contacts and both side-by-side comparisons remain in Scratch.

## Art made

46 final images: three Lucia cutouts, 27 comic panels, seven scene banners and nine model objects.
Final art: 1299.0 KiB. Recorded voice: 0 KiB. Final bundle: 1,959,228 bytes, below the 2 MB goal.
All were generated with the image tool and processed only with art.py --rekey NAME.
Redrew 32 assets after a shared prompt introduced unwanted people; also redrew the sprint setting and glass vase.
Final people flags: 14 true, 32 false. The required fresh people-art review passed the full final set.
Prompts, credit and final-size contacts are preserved. No external illustrations were downloaded.

## Art still to paint

None.

## Engine changes wanted

kit/graphing.js, point(): use el.focus({preventScroll: true}) on pointerdown to protect embedded layouts.
scripts/audit_tool.py, Audit.key()/drive_keys(): support printable digits, preferably through CDP Input.insertText.
See handoff.md. No shared engine or helper source was edited.

## Left open

- Port 8775 still responds with this tool's directory. Host cleanup could not identify the owning PID because
  process inventory was denied; no unrelated process was stopped. All Chrome ports are closed and host.html
  is removed. cleanup.json records this limit. The Scratch launcher now retains a direct server handle for future runs.
- Full mechanical audit coverage is unfinished because of the helper KeyError and iframe-context failure. The next
  cold review should run it with the corrected tool-local fixture. Do not interpret this report as a clean full audit.
- M8/M9 and K7 spare rules were checked with independent content/checker fixtures; M9 was also rendered and exercised.
  Their complete student-set paths were not all walked from the first core story.
- Browser narration is intentional for Build; recordings were not made.
- The build brief asked for benchmark bundles, which regenerated their ignored HTML outputs before the write-only
  conflict was recognized. No benchmark source or shared code was edited; all authored artifacts are in the two allowed folders.
- No owner question was sent. No further implementation or polish round was started after this report's final write.
