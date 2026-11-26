# Story Graphs: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: story-graphs

#### Built

Build only in S:\CurioClass-codex. No commits, branch operations, deployment or polish round.
Match, Sketch and Model contain 25 stories, three complete core sets, spare stories and local progress.
The tool uses the unchanged kit voice and graphing engines, a comic notebook, 46 original illustrations,
responsive controls, keyboard drawing, pointer dragging, comparisons, playback and immutable round marks.
Delivered src.html, content.json, tool.draft.json (stage built), notes.md, handoff.md, voice/lines.json,
audit-states.json, art/prompts.json, 46 WebP files and the generated self-contained HTML.
Helpers, contacts, checks and frames are in ../../_scratch/story-graphs/. host.html was removed.
All assigned Chrome ports are closed. A remaining host on 8775 is documented under Left open.
Deadlines: reads usually 30 s, bundles 120 s, drive batches 300 s, the single audit 2,400 s.

#### Numbers check

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

#### Facts checked

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

#### Break it

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

#### Voice walk

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

#### Feel check

Played the core paths through the three modes. Match reached Matched 6, Partly 1; Model Matched 6, Partly 3.
Sketch was split into K1 and a K2-K6 walk after correcting a pointer-test edge click and a connection reset.
Best moment: replacing the hill-picture mistake with a continuously increasing sketch, then seeing its words light up.
Flattest moment 1: narrow, unequal compact graph cards. Equal 2x2 tracks now keep the comparisons fair and readable.
Flattest moment 2: a large, empty description panel in Model. The painted pool and ice swan now fill that space
without adding answer labels. Wrong table checks also retain the given table beside the checked line.
Compared both benchmark tools. feel-comparison.png places this tool beside Beat Lab; bar-comparison.png uses Snowy Mail Route.
The notebook has rich places and characters, direct choices and a clear payoff, with no confetti or points.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Every captured frame was viewed individually or on the inspection sheets; critical 680 and phone states were also opened full size.
Folders: final-frames, extra-frames, extra-recheck, side-frames, side-retry, last-frames, postfix-frames,
art-final-frames, interactions, walk-match, walk-model, walk-sketch, walk-sketch-first and the audit's 49 frames.
The earlier first-retry and compact-retry frames and both benchmark frames were inspected too.
Inspection sheets, art contacts and both side-by-side comparisons remain in Scratch.

#### Art made

46 final images: three Lucia cutouts, 27 comic panels, seven scene banners and nine model objects.
Final art: 1299.0 KiB. Recorded voice: 0 KiB. Final bundle: 1,959,228 bytes, below the 2 MB goal.
All were generated with the image tool and processed only with art.py --rekey NAME.
Redrew 32 assets after a shared prompt introduced unwanted people; also redrew the sprint setting and glass vase.
Final people flags: 14 true, 32 false. The required fresh people-art review passed the full final set.
Prompts, credit and final-size contacts are preserved. No external illustrations were downloaded.

#### Art still to paint

None.

#### Engine changes wanted

kit/graphing.js, point(): use el.focus({preventScroll: true}) on pointerdown to protect embedded layouts.
scripts/audit_tool.py, Audit.key()/drive_keys(): support printable digits, preferably through CDP Input.insertText.
See handoff.md. No shared engine or helper source was edited.

#### Left open

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

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: story-graphs

#### Played

Cold grade 8 play in all three modes preceded builder notes/source: opening choices, sketch points and a Pool model check.
Then exercised all 25 core/spare stories through all summaries, the correct voice path, projection and phone states.
The comic places are strong. Reading back a hill-shaped mistake is the best teaching moment.

#### Findings fixed

- Blocker, family:graphing, Sketch: short pieces covered point dots and intercepted dragging. Number selectors now avoid handles, with dotted leaders. Real drags passed at 375, 680, 760 and 1366; all nine phone point centers remained available.
- Blocker, general, playback: a resize probe raised an exception at the piece lookup on an early frame. Progress now clamps to [0,1]; the same probe passes with no exception or disabled controls.
- Should fix, family:graphing, Sketch: one start/rate failure marked every row X. Checks now identify the responsible row; acceptance rules are unchanged.
- Should fix, family:graphing, Sketch: start/rate errors could read like the story. Read-backs name the start and compare earlier rises/falls across pauses.
- Should fix, general, Match/Sketch: failed-check hints invited another Check without correction. Hints now name X pieces/rows and editing actions.
- Should fix, general, voice: Choice/Check results waited behind stale instructions; Next guidance was lost at two-second pace. Result events interrupt stale speech; shorter Match results leave room for nextHow. General tag guidance remains valid after piece auto-selection.
- Should fix, general, compact feedback: longer diagnostics clipped at 680 and 375. Comparison space increased; affected frames re-shot and inspected.
- Should fix, general, boundaries/voice: right-edge input could ask for an impossible move; Sound off consumed the backward warning. Hints now name Undo/drag; narration is marked used only after it starts. Keyboard piece selection/Undo also stop playback.
- Should fix, general, compact Model: shown-note text referred to a folded graph. It now compares the shown numbers with the story; privacy and all eight meanings fit at 375 and 680.
- Polish, general, summary: bare counts became a notebook recap naming every story and saved mark. Counts, replay and mode choices stay.
- Polish, general, art: Toss's tiny ball was secondary to its yard. Redrawn larger; second edit moved it inside the banner crop. The set's rich style stays.
- Polish, general, comparison: corrected "1 parts" to "1 part".

#### Findings left

No blocker or should-fix remains. No demonstrated score bypass found.

#### Break it

- Match: held-click backward-time trap, then correct card; first pick stayed locked. Repeating Up/Straight and Check twice produced Shown.
- Tags: incomplete Check disabled; M5 piece 3 Straight gave [true,true,false,true]. Two wrong checks show rather than award Matched.
- Sketch: trivial straight line twice produced Shown. Clear, copy shown T/S solution and third Check retained Shown, tries 3. Free draw preserved challenge state and awarded nothing.
- Wrong hill, missing return, changed candle rate, flat ball top, straight tent, one-rate snow, bottle-rate and sled-bend errors failed; collinear splits passed.
- Model: blank/malformed inputs cannot pass; zero guesses twice reveal numbers. Sweeping all meaning cards locks first choices: Partly/Shown, never Matched in the attack.
- R2 swapped, reciprocal and first-row errors produced distinct notes; 4 and 5 passed. R3 locked the loss-of-3 meaning. No student line appears while typing.
- All 25 stories settled via cheap wrong-answer paths without promotion; all spares and summaries reached. 59 focused assertions passed. No meter, timer, best score or reflection gate exists.
- Reload matched saved state exactly; cancel kept it; confirmed Clear reset marks. Historical marks cannot be promoted by later practice.

#### Voice walk

Held 120 ms input, two-second gaps, Sound on: plain stage tap, select, Choose, Up/T, Flat, Up/T, Check, Next; Sketch (0,0),(6,2),(10,8), S, Check, Next; Model 50/200, Check, meanings, Read.
Heard: wMatch, matchChoose, pickRight, tagHow, tagCheck, tagsRight, nextHow, wSketch, sketchCheck, bendHow, sketchRight, wModel, modelRight, meaningRight-m, meaningRight-b, Read.
The plain-stage-first walk heard wMatch; the earlier card-first walk legitimately skipped it. Action cuts are allowed. Every mode how-to started on the repaired path.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| matchChoose, five selections | how | 1 | 1 |
| nextHow, five completed checks | how | 1 | 1 |
| tagsRight, five separate rounds | event | 5 | 5 |

Side walk: Free draw, rapid mode switches, Read with Sound off, mode change during Read. Queue ended empty with no stale mode line afterward.
Runtime fixed lines and voice/lines.json agree. Browser speech is used; no recorded clips exist.

#### Facts checked

- Graph descriptions/sketches and constructing/interpreting linear models: [Common Core 8.F.B.4/5](https://www.thecorestandards.org/Math/Content/8/F/).
- Slope as signed velocity, steepness as speed, stopped/returning, average speed from change/time: [OpenStax Physics 2.3](https://openstax.org/books/physics/pages/2-3-position-vs-time-graphs).
- Steady inflow raises water faster through a smaller cross-section: [OpenStax Calculus 1, 4.1](https://openstax.org/books/calculus-volume-1/pages/4-1-related-rates).
- Toss slows upward to an instant of zero vertical speed, speeds downward, negligible air resistance: [OpenStax University Physics 1, 3.5](https://openstax.org/books/university-physics-volume-1/pages/3-5-free-fall).
- Rate, units, initial value at input zero, working back from later rows: [OpenStax College Algebra 2e, 4.1](https://openstax.org/books/college-algebra-2e/pages/4-1-linear-functions), [Elementary Algebra 2e, 4.5](https://openstax.org/books/elementary-algebra-2e/pages/4-5-use-the-slope-intercept-form-of-an-equation-of-a-line).
- Graph-as-picture misconception and credits/date: [Leinhardt, Zaslavsky and Stein, 1990](https://journals.sagepub.com/doi/10.3102/00346543060001001), [Shell Centre, 1985](https://www.mathshell.com/materials.php?item=lfg&series=tss).
- Fictional R1-R9 rate/start pairs recomputed exactly: (50,200), (4,5), (-3,90), (6,20), (3/20,1), (-3.5,40), (-1.5,60), (9,34), (-0.5,6). Every point fits.
- Spec arithmetic: pool full at 26 min; tank empty at 30; swan at 40 h; ferry docks at 12 min, 30 km/h; card's linear zero 80/7 smoothies, eleven whole purchases affordable.
- Independent predicates accept A only in all nine Match stories; 27 traps fail, equal piece counts/starts. Six random picks: 0.024414%; two tag guesses per piece: 8.163%, 2.332%, 0.666% for 2/3/4 pieces.
- Evidence: review-numbers.py/json, review-static.py, review-browser/tests.json and real-attacks.json in Scratch. Notes have the required opening headings and identify idealized/qualitative physics.

#### Sensitivity

Fictional everyday cast and abuela merit a fresh cultural/people-art look: Lucia's continuity, Maya, grandfather/neighbor age portrayal, incidental people and family-language assumptions.
All 46 images inspected; 14 people assets correctly flagged. No stereotypes or culture-wide claims found; no Native, religious or hard-history content.

#### Flattest moment left

Model description rounds remain static before Check. Their painted objects are strong; hiding the line protects the mathematical task.

#### Graphics

Retained the violet comic notebook, directional light, 27 comic panels, seven banners, nine objects and three Lucia cutouts. All 46 checked at final sizes; none missing.
k4-ball alone redrawn with two generated candidates. Built-in imagegen prompt/provenance: ../../_scratch/story-graphs/review-art-provenance.json. Final art/raw/k4-ball.png processed only with art.py --rekey k4-ball.
Art 1,331,752 bytes; bundle 1,966,722 bytes (1920.6 KiB), below 2 MB. No people in the redraw.
Existing Beat Lab and Snowy Mail Route bundles opened read-only; neither rebundled outside scope. Side-by-side: review-bar-comparison.png.

#### Audit

Completed once within the 2400-second limit: ../../_scratch/story-graphs/review-audit/audit.md, Chrome 9961, host 8765. All 81 audit frames inspected. Its 50 leads were resolved as follows:

- 17 inline-text/fiction-label bounding overlaps: glyphs remain separated in the inspected frames; no collision.
- 5 dialog/background leads: intentional modal coverage; active dialog controls remain visible and keyboard safe.
- 12 verdict/graph-path leads: labels occupy full-width boxes, but Graph text and check/X glyphs are separate; strokes pass behind opaque number circles.
- 6 point/selector overlap leads: confirmed and repaired; jittered drag, dense nine-point and phone tag frames re-shot.
- 1 singular-word lead: fixed.
- 1 resize lead: fresh shuffled cards reached different branches. Fixture now deterministically chooses a variant; a separate correct-tag fixture was added. Same-choice resize kept Tag and controls enabled.
- 8 missing/cut welcome leads: allowed by BASELINE 16; premise/action remain in bubble, hint and Read.
The separate passing-sketch resize probe caught the playback exception described above; its repaired recheck logged zero errors. The full audit was not repeated.
Craft: all eight STANDARDS sizes inspected. Keyboard-only K1 earned Matched; a real drag clamped at its neighbor. Motion off lit both result rows with no moving dot/infinite animation; grayscale stayed readable.
Final main/side voice and real cheat rechecks logged zero product errors. Initial confirmation scripts needed iframe timing/synchronous CDP fixes; host favicon/closed-connection messages were outside the tool.
All review Chrome ports 9960-9967 and host 8765 closed; no tool host.html remains. Evidence map and hashes: ../../_scratch/story-graphs/review-verification.json.

#### Left open

Browser narration awaits recorded assets in the later media workflow; this review records no audio.
No new topic, mode, shared-kit change, commit or deployment. Authored edits stay in the two permitted folders.
Cold play before source covered opening interactions in each mode; the exhaustive 25-story traversal followed source inspection. Unattended choices followed the spec/baseline. Working report stayed in Scratch until the final stop-action write.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Story Graphs build handoff

The readable src.html starts from the kit starter and inlines tool CSS, then the content token, state, voice queue,
renderers and interaction checks. content.json is the only tool data file and is inlined by the bundler.
kit:curio and kit:graphing are unchanged. Graph geometry, snapping, dragging and point nudging use Plane.

Progress stores round state and terminal marks under curio-story-graphs, wrapped in try/catch.
Clear graph and Undo never reset a round's check count. A terminal mark cannot be promoted by later practice.
The one-pick graph and one-tap meaning locks are independent from DOM disabled styling.
Clear progress uses one keyboard-accessible confirmation dialog, with a safe Keep progress default.

Scratch contains generation/build helpers, all number and adversarial checks, screenshots, contacts and audit evidence.
Do not ship Scratch. Every required illustration is registered in art/prompts.json; people assets are marked people: true.

#### Decisions and spec discrepancies

- No owner questions are open in the spec. This run is unattended; no question was sent.
- The current build brief and user require the image tool, superseding the older Gemini-only and do-not-draw wording.
- Narration is browser speech through Curio.voice. No recordings were made, as required by Build only.
- The source spec rounds gift-card depletion to 11.4 smoothies. Exact computation is 80/7, and actual whole purchases stop at eleven.
- Preview space folds art as specified. Small-screen meaning cards may scroll inside the stage while the equation stays visible.
- Shuffled orders persist with an in-progress round, so reload cannot reroll a locked pick. Play the set again reshuffles.
- The user says to stop when codex-report.md is written, while CODEX-BUILD requests an early report.
  Working report notes stay in Scratch; the final report write is the last build action.

#### Sensitivity

Fictional everyday stories feature Lucia, Maya, her grandfather and an older neighbor. The word abuela is used for
grandmother in Lucia's story. No historical or cultural claims are made. People-art review should check consistency,
age-appropriate poses and respectful depiction. A dedicated fresh people-art check is recorded in Scratch.
That check passed all 46 final assets: 14 with people, 32 without. The sprint continuity redraw also passed.

#### Engine changes wanted

kit/graphing.js, point(), pointerdown focus: use focus({preventScroll: true}) instead of plain focus().
The tool uses a fixed viewport, so this did not require an engine edit, but the shared method can scroll embedded pages.

scripts/audit_tool.py, Audit.key()/drive_keys(): accept printable digits, or add a text-input step using CDP Input.insertText.
The audit stopped at KeyError: '1'. The tool-local state fixture now uses input events for this unsupported typing step;
all clicks remain real, and actual typing was independently checked by the full Model walk.

The audit's iframe context lookup also failed on the 375 host. Separate hosted phone frames and voice walks passed.

#### Next review

The cold review is recorded in codex-review.md. Source, fixes and independent evidence remain in the permitted
tool and Scratch folders. The next blind lenses should use that report's Sensitivity and Left open sections.

#### Cold review changes

Review kept the comic notebook and all 46 illustrations. Toss's ball was redrawn with the built-in imagegen tool
at a useful final-size scale, with the original yard as reference; prompt and raw source are in art/.
Sketch now reports starting position and relative rates across pauses. Its row checks localize the condition that
failed while keeping the same acceptance rules, check budget and immutable saved marks.
After a failed Match or Sketch check, the hint explicitly asks for a correction before the second Check;
Read uses that current instruction. Compact comparison space fits the longer diagnostic read-backs.
Check-result voice events interrupt stale instructions, so the result starts with its on-screen outcome.
The two Match success/show lines are shorter so Next story's how-to can start at a two-second action pace.
The summary retains counts and adds each story's title and saved mark, making the notebook a personal recap.
Numbered Sketch selectors now avoid point handles and use thin dotted leaders when displaced. Real jittered drags
and a nine-point phone sketch confirmed every point center remains available. Piece Enter, grid arrows and Undo
stop playback; its progress clamps to zero to prevent an early-frame negative piece index during resize.
The right-edge and nine-point refusal hints name possible actions. Backward-time narration is marked used only
after it starts, with a per-work voice key; Sound off consumes no warning. General tag guidance remains valid
after automatic selection moves to another piece. Wrong-pick transitions hush speech about the previous controls.
Compact Model's shown note compares numbers with the story, because its graph folds away at that size.
The locked-pick audit fixture now chooses the backward-time variant consistently. A separate correct-tag fixture
preserves that coverage without comparing two random fresh-page branches during resize.
The one completed review audit found 50 leads. Scope-specific rechecks followed its repairs; the audit was not rerun.

#### Build cleanup history

The builder reported that its assigned Chrome debugging ports stopped responding and host.html was removed.
It reported that port 8775 still responded with the Story Graphs tool directory. It could not identify the listener PID:
process inventory through tasklist and Windows CIM was denied, while netstat exposed no listening owner.
Do not assume the local host stopped. See _scratch/story-graphs/cleanup.json. The Scratch host harness now
keeps the direct server process handle for termination in future runs; this could not recover the old handle.

The cold review used only Chrome 9960 to 9967 and host 8765. Its own processes are checked separately in
_scratch/story-graphs/review-ports.json; it did not inspect or stop the earlier build's unassigned listener.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
