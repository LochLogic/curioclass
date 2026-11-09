# Codex review: story-graphs

## Played

Cold grade 8 play in all three modes preceded builder notes/source: opening choices, sketch points and a Pool model check.
Then exercised all 25 core/spare stories through all summaries, the correct voice path, projection and phone states.
The comic places are strong. Reading back a hill-shaped mistake is the best teaching moment.

## Findings fixed

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

## Findings left

No blocker or should-fix remains. No demonstrated score bypass found.

## Break it

- Match: held-click backward-time trap, then correct card; first pick stayed locked. Repeating Up/Straight and Check twice produced Shown.
- Tags: incomplete Check disabled; M5 piece 3 Straight gave [true,true,false,true]. Two wrong checks show rather than award Matched.
- Sketch: trivial straight line twice produced Shown. Clear, copy shown T/S solution and third Check retained Shown, tries 3. Free draw preserved challenge state and awarded nothing.
- Wrong hill, missing return, changed candle rate, flat ball top, straight tent, one-rate snow, bottle-rate and sled-bend errors failed; collinear splits passed.
- Model: blank/malformed inputs cannot pass; zero guesses twice reveal numbers. Sweeping all meaning cards locks first choices: Partly/Shown, never Matched in the attack.
- R2 swapped, reciprocal and first-row errors produced distinct notes; 4 and 5 passed. R3 locked the loss-of-3 meaning. No student line appears while typing.
- All 25 stories settled via cheap wrong-answer paths without promotion; all spares and summaries reached. 59 focused assertions passed. No meter, timer, best score or reflection gate exists.
- Reload matched saved state exactly; cancel kept it; confirmed Clear reset marks. Historical marks cannot be promoted by later practice.

## Voice walk

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

## Facts checked

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

## Sensitivity

Fictional everyday cast and abuela merit a fresh cultural/people-art look: Lucia's continuity, Maya, grandfather/neighbor age portrayal, incidental people and family-language assumptions.
All 46 images inspected; 14 people assets correctly flagged. No stereotypes or culture-wide claims found; no Native, religious or hard-history content.

## Flattest moment left

Model description rounds remain static before Check. Their painted objects are strong; hiding the line protects the mathematical task.

## Graphics

Retained the violet comic notebook, directional light, 27 comic panels, seven banners, nine objects and three Lucia cutouts. All 46 checked at final sizes; none missing.
k4-ball alone redrawn with two generated candidates. Built-in imagegen prompt/provenance: ../../_scratch/story-graphs/review-art-provenance.json. Final art/raw/k4-ball.png processed only with art.py --rekey k4-ball.
Art 1,331,752 bytes; bundle 1,966,722 bytes (1920.6 KiB), below 2 MB. No people in the redraw.
Existing Beat Lab and Snowy Mail Route bundles opened read-only; neither rebundled outside scope. Side-by-side: review-bar-comparison.png.

## Audit

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

## Left open

Browser narration awaits recorded assets in the later media workflow; this review records no audio.
No new topic, mode, shared-kit change, commit or deployment. Authored edits stay in the two permitted folders.
Cold play before source covered opening interactions in each mode; the exhaustive 25-story traversal followed source inspection. Unattended choices followed the spec/baseline. Working report stayed in Scratch until the final stop-action write.
