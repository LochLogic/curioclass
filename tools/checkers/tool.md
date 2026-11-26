# Checkers: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: checkers (Recess)

#### Built

Built in `S:\CurioClass-codex`, with writes confined to `tools/checkers/` and `_scratch/checkers/`.
Readable `src.html`, offline `checkers.html`, built draft metadata, notes, handoff, painted art and provenance are present.
Six computer rivals, pass-and-play, five rounds / 25 puzzles, mirrored daily, resuming, forced jumps, takebacks and shell rewards.
Bundle: **1,202,394 bytes**, below 6 MB. SHA-256: `f019414e94249de2c5ef66881bf81fcf04ae61d2b095bee953929ac453506fc5`.
No commits, shared-kit edits, shelf edits, deployment, review round or polish round. This is a Build handoff.
All four accepted spec defaults were kept without questions. Automated gentle and strong play policies stood in for child/adult play.
No physical child, adult strength trial, Chromebook or phone was available; emulated viewports are not hardware testing.
Palette contrasts independently recomputed: text/frame 15.23, dim/frame 8.33, mint/dark 13.61, must/dark 6.33, grid/dark 4.08; puck ink 8.75 / 5.56.

#### Rules check

`rules-results.json`: 173 in-file assertions PASS; independent 8x8 generator comparison on 5000 positions PASS; 5000 incremental hashes PASS.

| Edge case | Result | Evidence |
|---|---|---|
| Men never capture backward | PASS | Amber 18 versus Blue 14. |
| No flying kings | PASS | King 14 only makes adjacent steps or adjacent jumps. |
| Shorter capture is allowed | PASS | Double has both one-victim and two-victim chains. |
| Crowning ends the move | PASS | 22x31 stops; an existing king continues 22x31x24. |
| King can return across its start | PASS | King 14 loops over 17,25,26,18 and returns to 14. |
| Victims remain until turn end; no double victim | PASS | Generator leaves the position intact; apply removes all four together. |
| Blocked pieces lose | PASS | Amber man 32 is blocked even with a piece left. |
| A quiet move is forbidden while any jump exists | PASS | All generated choices in Double are captures. |

Opening has seven legal moves. Third repetition and 80 quiet turns draw: PASS in rules and actual interface commits.
The counter appears at 40 quiet turns (20 moves each). Men and jumps reset it. Daily mirror: 5000 positions PASS.

#### Puzzles and levels

All 25 re-solved with an independently written coordinate generator in `independent_solver.js`. No imported engine supplied the answers.
The eleven Call endings used exhaustive reachable-state retrograde solves, totaling 9,756,170 states across the separate solves.
Every historical book move preserves a forced win, and every winning alternative exactly matches `also`: PASS.
Minimums enumerate every immediate winning alternative at every solver step, because the game accepts those too.

| Puzzle | Stated / computed player moves | Computed result at book end |
|---|---:|---|
| r1-1 Hop | 1 / 1 | opponent blocked / captured |
| r1-2 Double | 1 / 1 | opponent blocked / captured |
| r1-3 Triple | 1 / 1 | opponent blocked / captured |
| r1-4 Crown | 2 / 2 | opponent blocked / captured |
| r1-5 Fence | 1 / 1 | opponent blocked / captured |
| r2-1 Give one, take two | 2 / 2 | opponent blocked / captured |
| r2-2 Side door | 2 / 2 | material gain 1 |
| r2-3 Middle march | 2 / 2 | material gain 1 |
| r2-4 Edge trick | 2 / 2 | material gain 1 |
| r2-5 Swing | 2 / 2 | material gain 1 |
| r3-1 Long reach | 2 / 2 | material gain 1 |
| r3-2 Back row | 2 / 2 | material gain 1 |
| r3-3 Into the corner | 2 / 2 | material gain 1 |
| r3-4 Three for one | 2 / 2 | material gain 2 |
| r3-5 Mar's corner | 4 / 4 | opponent lost in 42 more plies |
| r4-1 Sturges' squeeze | 3 / 3 | opponent lost in 4 more plies |
| r4-2 Wardell's walk | 4 / 4 | opponent lost in 40 more plies |
| r4-3 Slocum's pin | 5 / 5 | opponent lost in 46 more plies |
| r4-4 Potterdon's pair | 5 / 5 | opponent lost in 40 more plies |
| r4-5 Slocum's crown race | 6 / 6 | opponent lost in 42 more plies |
| r5-1 Wilder's chase | 5 / 5 | opponent lost in 8 more plies |
| r5-2 Brown's long walk | 7 / 7 | opponent lost in 46 more plies |
| r5-3 Wardell's tempo | 7 / 7 | opponent lost in 40 more plies |
| r5-4 Brown's chase | 8 / 8 | opponent lost in 12 more plies |
| r5-5 Brown's pin | 13 / 13 | opponent lost in 24 more plies |

Round sums, stated and computed: **6, 10, 12, 23, 40**. All 25 also played through the actual browser interface.
Stars verified: 3 without tries; 2 with one clue; 1 with three clues and answer playback. Computer cutoffs 0/1/3/4 takebacks: 3/2/2/1.
Fence correction: the spec claims 10-15 also blocks immediately. It does not: Blue has 21x14. The legal book win 10-14 is shipped unchanged.
Raw solver, alternatives, minimums and browser results are retained in Scratch. No source collection was downloaded.

#### Computer opponent

Every live search is in an offline Blob Worker, with a time budget. Replies wait at least 350 ms. Strong search uses iterative deepening,
two 32-bit Zobrist halves, capped TT, bound flags, prior-best / jump / history ordering, capture extensions and the specified evaluation.

| Rival | Play | Unforced depths measured | Mean / maximum search ms |
|---|---|---:|---:|
| Pip | gentle; 35% slips plus kindness | 1 | 0.04 / 0.24 |
| Dot | gentle; 15% slips plus kindness | 2 | 0.14 / 1.32 |
| Nova | gentle; 5% slips | 4 | 1.58 / 12.68 |
| Comet | no slips | 6 | 8.44 / 63.78 |
| Blaze | no slips | 8 | 63.95 / 553.03 |
| Titan | no slips; 3-second budget | 10 to 19 | 1674.45 / 3002.00 |

These timings are Node on this Windows machine, excluding forced one-choice replies. Browser Worker logs and full interface games are also retained.
A 10 ms main-thread ticker fired 319 times during a 3.2-second Titan interval: no page freeze. Physical Chromebook timing remains unverified.

| Higher versus lower | Higher wins / losses / draws |
|---|---:|
| Dot vs Pip | 6 / 2 / 2 |
| Nova vs Dot | 7 / 0 / 3 |
| Comet vs Nova | 9 / 0 / 1 |
| Blaze vs Comet | 6 / 1 / 3 |
| Titan vs Blaze | 6 / 0 / 4 |

Ten ballot games per adjacent pair, each opening repeated with sides swapped: all higher rungs outscore the rung below. PASS.
Nova versus Pip, 20 games: 19 wins, 0 losses, 1 draw. PASS. No adult strength rating is claimed.
Actual interface full games: Pip beaten in 47 plies; Dot won in 53; Nova 122; Comet 51; Blaze 100; Titan 83. Friend game ended in 80 plies.
`fullplay/results.json` records all seven, with zero browser exceptions. Screens captured at polling boundaries can show the next game.

#### Break it

- PASS: wrong legal puzzle move costs a move and a try, holds visibly for 0.9 s, then restores the position.
- PASS: Undo, Restart, Menu and reload/resume never refund the first-run tally; wrong tries and clues survive restart.
- PASS: listed alternatives spring back without cost; immediate wins are accepted; three tries play the answer and retain the star penalty.
- PASS: Encore storage is separate from the completed first-run seal. Daily replay stays the same puzzle/mirror and makes no second award.
- PASS: computer Undo cancels its Worker and keeps Moves; Menu/Restart cancel searches; no delayed reply appears afterward.
- PASS: friend games make no shell score; Undo reopens a finished friend game. Initials Save removes its controls and adds one row.
- PASS: keyboard solves Hop; real held pointer clicks and jittered drags solve it; actual CDP touch solves it without scrolling.
- PASS: resize during a triple-jump preserves the result and captures all three; no exception. Calm has zero running animations and no pickup transform.
- PASS: a fresh-page Resume keeps the partial round at one Move and one try. Tapping the origin cancels a partial chain; a full king loop can land back on it.
- PASS: painted winner pucks start a victory wave; the result board dims to 0.5 behind its card. Calm skips the wave and the dim transition.
- **FAIL, specification conflict:** three clues can auto-play a first run for minimum Moves (round 1: 6) with one star. The shell records that best.
  This follows the explicit Moves-only score and try-based star formulas, but fails the stronger cheap-best test. No unrequested penalty was invented.

Audit ran once to completion: 58 leads. Focus loss, short-preview Back buttons, 9 px rival text, title spacing, small checkbox and narrow HUD spacing were fixed.
Affected screens were rechecked only. Legal 44 px hit circles are disjoint; their bounding rectangles overlap at diagonal corners in tiny previews.
Missing classroom #hint / Read / voice logs are expected: this game uses #prompt and has no narration. Calm and audit resize checks were clean.

#### Look board

Paintings, cover and these three 1366x768 frames were made and viewed before game logic. The spec gave an obvious night-arcade direction; no alternate world was needed.
Kept tactile acrylic, violet glass, dark cabinets, amber/cyan light and six painted robots. Direction chosen for immediate toy-like appeal.

![Opening](../../_scratch/checkers/look/opening.png)

![Game in progress](../../_scratch/checkers/look/progress.png)

![Crown moment](../../_scratch/checkers/look/best.png)

#### Grab check

Most satisfying moment: the third capture lands on the far row and a crown drops onto the glowing puck.
Flattest moment: a cramped preview picker and blank side-panel space. Compact layouts retain the painted world and keep all controls above the fold.
A stray neighboring sprite sliver on Nova was cropped away. No art was replaced with code placeholders.

![Actual crown capture](../../_scratch/checkers/grab-frames/crown-moment.png)

![Beside the shell demo and Collision Lab](../../_scratch/checkers/grab-comparison.jpg)

The cabinet world, glass table, pucks and robot badges are visually distinct from both reference frames. Final visual approval belongs to the owner.

#### Class creep check

Whole-word source scan: standard, objective, learn, skill, lesson, correct answer, well done: **0 each**. No standard codes, kit:curio, voice or em dash.
The only rewards UI is the Recess shell. Parent/teacher material is in notes.md, copied from the spec.

#### Sources

- Fourteen original positions from the supplied spec: original Curio Class material.
- W. T. Call, Midget Problems (1913), archive.org/details/midgetproblemsal00call: eleven positions and move lists, composer names retained.
  Source status as recorded in the spec: "Copyright, 1913, by William Timothy Call"; public domain in the US, and life-plus-70 countries (Call died 1917).
- J. Lyman, A Game of Draughts (1881), archive.org/details/gameofdraughtsse00lyma: rules cross-check only; Library of Congress: "no known copyright restrictions".
- Modern English draughts / WCDF practice: facts recorded in the spec, no copied prose. No external puzzle fetching was needed.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Prompts, alpha-preserving crops and raw paintings are retained.

#### Done when

| Spec item | Result / evidence |
|---|---|
| Recess shell, no lesson kit or duplicate rewards UI | PASS; exact kit tokens in source, shared API in use. |
| Dev self-check and mirror test | PASS; 173 assertions, every line, 5000 mirrors. |
| Draws and no-progress counter | PASS; scripted edge tests and real interface draw paths. |
| Gentle engine design and Nova/Pip run | PASS; depths 1/2/4, seeded slips/kindness, 19/0/1. |
| Strong engine and budgets | PASS on this machine; fixed 6/8, Titan 10-19, maximum 3002 ms. Chromebook hardware UNVERIFIED. |
| Ten-game adjacent ladder | PASS; every higher rung scores more. |
| Cancel thinking on Undo/Restart/Menu | PASS; no stale moves after 3.6-second waits. |
| Book / also / immediate-win puzzle handling | PASS; solver and browser paths. |
| Round scores, stars, first-run seals and Encores | PASS specified formulas; strict cheap-best guarantee FAIL as explained above. |
| Grayscale side marks, stacked kings and crowns | PASS; full gray frame and source art inspected. |
| Calm motion and sound off | PASS; zero animations, static pickup, muted interface. |
| Mouse / touch / keyboard and required sizes | PASS; preview, desktop and phone frames, touch and resize paths. |
| No em dash; Curio Class; notes | PASS; source scan and required notes present. |
| One offline file below 6 MB | PASS; local-file Titan reply, zero HTTP resource requests. |
| Look board / painted cover before logic; painted sprites | PASS; three early frames and 21 finished WebP assets. |

#### Frames looked at

Original four generated paintings; three early browser hero frames and their compositing studies; every captured frame via contact sheets, with key frames opened full size.
77 captured PNGs were inspected, including the 16 audit frames and targeted correction / persistence / motion frames.
Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 390x844 and 375x812. Phone also checked through the audit iframe host.
Folders: look, first-frames, check-frames, extra-frames, final-frames, grab-frames, last-frames, touch, fullplay, audit, after-audit-frames, final-fix-frames, reload-frames, cancel-chain-frames, motion-finish-frames.
The original 680 table overflow and earlier keyboard probe are preserved; corrected frames and assertions supersede them. Full grayscale: `grayscale.png`.

#### Art made

21 finished WebP files, 787,476 bytes: landscape and portrait arcade, exact board, cover, four pucks, six robots, two halos, four crown frames and sparks.
Generated with the built-in imagegen tool. Raw paintings copied into art/raw; atlas cells split and resized with alpha preserved. Nova crop tightened; no full redraw needed.

#### Shell changes wanted

kit/recess.js documentation header contains a literal closing script tag; inlining it ends the script. Its stylesheet example also gets expanded.
The local bundle wrapper strips only that comment prefix from the generated file. Shared implementation and CSS are untouched. Use the wrapper documented in handoff.md.
The shared bundler also requires the non-self-closing stylesheet token. The wrapper normalizes that token in this source.

#### Left open

The clue-only minimum-Moves best conflict requires a scoring decision. The explicit spec formulas were kept under the no-improvisation rule.
Physical Chromebook/phone performance, real youngest-grade/adult play and adult strength testing remain unverified. Visual judgment is the owner's.
No sign-off, deployment or independent review has been performed. All started browser/server processes were closed before this report was written.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: checkers (Recess)

#### Played

Cold review in `S:\CurioClass-codex`, against CODEX-RECESS.md, GAMES.md and the Checkers spec.
Tried the ordinary documented bundle first. It could not start; repaired only the shell loader before continuing cold play.
Played the menu, rules, friend, computer, opening puzzles and daily before reading the builder's report or handoff.
Youngest-reader and adult policies were simulated with real held clicks, keyboard, touch and jittered dragging; no human child trial is claimed.
Played all 25 puzzles and full interface games: beat Pip in 49 plies; losses to Dot 50, Nova 312, Comet 46, Blaze 44, Titan 34.
The friend game finished with Blue winning in 126 plies; also tested an agreed draw. The painted arcade and jumps are strong.

#### Findings fixed

- **Blocker, general, startup:** ordinary bundling inlined script/style examples from the shell's header and broke execution. A source-local inert loader now survives the ordinary bundler. No kit edits.
- **Blocker, checkers, puzzle Flip:** flipping during the book's reply cancelled it permanently. Flip now restarts the pending book reply.
- **Blocker, checkers, final award:** the puzzle index advanced past the array and resize threw. Keep the last valid index, clear the obsolete Finish overlay, and retain an actionable completion prompt after dismissal/resize.
- **Blocker, checkers, cheap best:** three clues could autoplay for minimum Moves. Each clue now costs one Move and one try, disclosed in the clue prompt, help and notes. A clue-only first round scores 21, not 6, with one star.
- **Should fix, general, Undo:** the first in-flight move had history but a disabled Undo button. Enable Undo as soon as the snapshot exists; cancellation retains its Move cost.
- **Should fix, general, moving pucks:** resize and Hints rebuilt the board during flight. Defer those redraws until landing; the triple jump keeps its sprite and commits once.
- **Should fix, general, keyboard:** Next puzzle and result Undo lost board focus. Restore the roving cell without scrolling. Trap Tab/Shift+Tab inside shell dialogs and make initials arrows 44 px high, locally.
- **Should fix, checkers, feedback:** Crown/Fence/Double failures incorrectly told beginners to give a puck away. Feedback now describes the actual missed crown, block or double jump. Friend mode says Next turn instead of Your side.
- **Should fix, graphics:** the spark atlas cell included neighboring crown fragments. Repainted `art/spark.webp` as one clean transparent cyan spark; retained the rest of the painted set.
- **Polish, play:** generic success text flattened every jump. Specific jump/trap finishes, a puck victory wave and a lower result overlay now preserve the winning position in view.
- **Audit fix, general, keyboard:** covered board buttons remained in the tab order beneath results. Disable cells while a result/award is active; Undo and the next puzzle re-enable them.

Unattended decision: the Recess brief calls a cheap best a blocker. Treating a clue as a scored puzzle try follows that priority while preserving all unassisted minima and the specified star cutoffs.

#### Findings left

Titan's depth-10 target is qualified: measured unforced searches reached depths 9 to 64, with a maximum 3002.52 ms. It did not meet a universal depth-10 floor.
Kept the accepted three-second budget. Physical Chromebook/phone timing and strength against a good adult remain unverified; emulation and engine ballots do not establish those claims.
The historical book endings remain intentionally guided lines, as specified; listed alternatives spring back for free.

#### Break it

Rules: all 173 in-file assertions pass. A reviewed coordinate-based generator matched 5000 positions; incremental hashes and 5000 daily mirrors pass.

| Rules edge case | Result |
|---|---|
| Men cannot capture backward | PASS |
| Kings cannot fly | PASS |
| Shorter complete captures may be chosen | PASS |
| A new crown ends the chain; an existing king continues | PASS |
| A king may return through its start | PASS |
| Victims remain until turn end and cannot be captured twice | PASS |
| Blocked pieces lose | PASS |
| A quiet move is forbidden while any jump exists | PASS |

Reviewed and reran the coordinate solver on freshly extracted shipped data: 25 legal lines; 9,756,170 historical reachable states; every historical book move preserves the win; all winning alternative lists match.
Actual pointer play earned round scores **6, 10, 12, 23, 40**, each with three stars. All 18 listed alternative moves were also exercised without a Move or try penalty.
- Illegal, occupied, backward and quiet-while-jump input: no board change. Partial chains remain uncommitted; tapping the origin cancels.
- Wrong legal moves: one Move/try. Restart, Menu/Resume and reload retain costs. Undo during a hop cancels without refund.
- Clue spam: first round 21 Moves/one star; one clue plus genuine play gives 7 Moves/two stars. Encore play cannot replace the first score or award again.
- Daily: genuine first completion gives three stars; same-day replay is Encore and makes no second award.
- Computer Undo cutoffs 0/1/3/4 give 3/2/2/1 stars. Wins disable Undo; every tested loss and the friend result reopen with Undo.
- Undo/Restart/Menu during Titan thinking: no stale reply after 3.4 seconds. Resume makes exactly one reply. A 10 ms main-thread ticker fired 236 times during one Titan turn.
- Twelve rapid initials Save taps made one board row. Friend play produced no shell award.
- Third repetition and 80 quiet turns draw; 20-each counter appears. Keyboard solves Hop; actual touch and jittered drag solve it; resize/Hints during a triple jump preserve the result.

Evidence: [rules](../../_scratch/checkers/review-rules-results.json), [solver](../../_scratch/checkers/review-solver-results.json), [abuse](../../_scratch/checkers/review-break-results.json), [rewards](../../_scratch/checkers/review-rewards-results.json).

#### Computer opponent

Ten fresh Node ballot games per adjacent pair, sides swapped; all higher rungs outscore the rung below. Separate 20-game Nova/Pip run: 19 wins, 0 losses, 1 draw.

| Higher rung | Wins / losses / draws |
|---|---|
| Dot over Pip | 6 / 2 / 2 |
| Nova over Dot | 7 / 0 / 3 |
| Comet over Nova | 9 / 0 / 1 |
| Blaze over Comet | 6 / 1 / 3 |
| Titan over Blaze | 4 / 1 / 5 |

Measured unforced depths: 1, 2, 4, 6, 8, then 9-64. Maximum search milliseconds: 0.39, 2.37, 18.90, 127.91, 1153.71, 3002.52.
Full interface games used the shipped Workers. Ballots used the freshly extracted engine in Node, not a browser `?ladder` run.
All 50 completed ballot records are present; the long Titan command returned a nonzero runner exit after writing its final result, so its process exit is not claimed clean.
[Ladder results and timing summary](../../_scratch/checkers/review-ladder-summary.json).

#### Voice walk

No narration, Read button or classroom welcome belongs here. Confirmed no voice/lesson kit was added.
Sound-off and switching to Calm during a jump complete correctly; Calm reports zero running animations and the local-file game loads zero HTTP resources.

#### Facts checked

Held movement, forced jumps, deferred capture removal, crown stops and draw rules to the supplied American/English checkers spec and its named WCDF/Lyman rules sources, then recomputed the behavior.
Fence's asserted second immediate win `10-15` is false: Blue has `21x14`. Kept the legal book win `10-14`; did not edit the spec.
Historical composer names, 1913 provenance and source/licence attribution remain as supplied in the spec; no new historical collection was fetched.
Class-creep scan: zero whole-word hits for standard, objective, learn, skill, lesson, correct answer or well done; zero em dashes.

#### Sensitivity

None requiring a cultural scene review: no people or cultural depictions. Historical problems retain their named composers and source attribution.

#### Flattest moment left

Titan's quiet thinking interval and the longer book endings. The thinking lights, live cancellation and instant restart keep those waits manageable; no new mode was added.

#### Graphics

Inspected all 21 painted WebP assets and the captured frames/contact sheets. Kept the cover, cabinet world, glass board, acrylic pucks, crowns and six rivals.
Replaced only the contaminated spark using built-in imagegen. Prompt/provenance: `art/prompts.json`; original generation: `art/raw/spark-review.png`; final transparent asset: `art/spark.webp`.
Best moment: a three-capture shot reaches the crown row. [Fresh comparison with the shell demo and Collision Lab](../../_scratch/checkers/review-grab-frames-contact.jpg).
Checked 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 390x844 and 375x812; phones also through port 8765 iframe hosting.
No clipped primary controls or sub-44 px targets in those checks. Dot/ring and crown distinctions survive grayscale. Calm keeps the painted world.
[Size frames](../../_scratch/checkers/review-size-frames-contact.jpg), [modal frames](../../_scratch/checkers/review-modal-final-frames-contact.jpg), [audit-fix frames](../../_scratch/checkers/review-audit-fix-frames-contact.jpg).
Bundle: **1189.5 KiB (1,218,094 bytes)**, below 6 MB. Final hash and 791,850 art bytes are recorded in [review-manifest.json](../../_scratch/checkers/review-manifest.json).

#### Audit

Ran `audit_tool.py` once, last, with a 40-minute limit, Chrome 9961 and host 8765. Completed with 73 leads; no exceptions, stuck resize controls or forever-running Calm animations.
Reviewed every audit frame. Missing #hint/voice logs are Recess exclusions. Empty square aria-labels counted as hidden text and intentional result-over-board overlaps are mechanical false positives.
The covered-cell keyboard issue was fixed; only its affected 680/1366/375/390 frames were re-shot, with 32 disabled cells during results and no console errors. No second audit.
[Complete audit](../../_scratch/checkers/review-audit/audit.md).

#### Left open

Hardware/adult strength and Titan's depth target remain qualified above. Shared header/dialog/arrow improvements are named in `handoff.md`; working local fixes are in this game.
The first two short read-only inspection commands completed before the timeout wrapper existed; subsequent shell commands used explicit limits. The Titan batch's nonzero exit is disclosed above.
Writes were confined to this tool and its Scratch folder; no commits, sign-off or deployment. All started Chrome/server resources and the temporary host are closed/removed, with [cleanup evidence](../../_scratch/checkers/review-cleanup.json).

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Checkers handoff

Build followed by one cold self-check. No git commits, publication, or shared-kit changes.

#### Play

Open `checkers.html`, the generated offline game. `src.html` is the readable canonical source.
The game uses the Recess API and its controls, win card, initials board, scores, sound and motion settings.
It has six computer opponents, pass-and-play, five rounds of five puzzles, and a mirrored seeded daily.
Use `?test` for the automatic 173-assertion self-check and `checkersDev` console helpers.
Use `?ladder` for ten full ballot games per adjacent pair, entirely in Workers, with console results.

#### Rebuild

From `S:\CurioClass-codex`:

```
python _scratch/checkers/review_run.py 120 python -c "import os,runpy,sys; os.environ['CURIO_DRAFT']='1'; sys.argv=['scripts/bundle_tool.py','checkers']; runpy.run_path(sys.argv[0],run_name='__main__')"
```

The ordinary repository bundler now works. The source keeps the inlined shell in a hidden textarea, then inserts
only its executable code as script text. This avoids both HTML end tags and kit tokens in the shell's header comments.
Keep the source kit stylesheet token without a self-closing slash; the bundler's exact pattern requires that spelling.
The wrapper and all verification scripts are retained in `_scratch/checkers/`.
Do not use `assemble.py` for routine source edits: it is the build's assembly history and will replace the game script
with the scratch modules. The final formatted `src.html` contains everything and needs no runtime dependencies.

#### Engine changes wanted

- `kit/recess.js`, opening documentation comment: replace the literal closing script tag in the example with an
  escaped spelling. It currently terminates an inline script while the HTML parser is inside a JavaScript comment.
  The header's stylesheet example also gets expanded by the bundler after the JS is inlined. The local wrapper
  is now replaced by the source-local inert loader; the shell implementation remains unchanged.
- `scripts/bundle_tool.py`: accept an optional self-closing slash in stylesheet kit tokens, or document the exact token.
  No shared file was edited for this build.
- `kit/recess.js`, `card`: trap Tab and Shift+Tab inside its modal. The game now supplies this keyboard guard locally.
- `kit/recess.css`, `.rc-arr`: make initials arrows 44 px high. The game now overrides their height locally.

#### Evidence

- `look/`: three 1366x768 hero frames painted and reviewed before game logic; static visual source retained.
- `rules-results.json`: eight edge cases, all puzzle lines, 5000 mirrored positions; `rules_test.js` additionally
  compares 5000 positions against an independent 8x8 generator and checks incremental Zobrist hashes.
- `solver-results.json`: all 25 puzzles independently re-solved. Eleven historical positions solved by exhaustive
  reachable-state retrograde analysis, including every listed alternative and the end distance.
- `ladder-2.json` through `ladder-5.json`, and `ladder-6-5.json`: final adjacent-pair ballot games and search timings.
  `ladder-6.json` is an earlier development run; use `ladder-6-5.json` for the final Titan engine.
- `ladder-3-1.json`: twenty Nova versus Pip games.
- `rounds-1-3.json`, `rounds-4-5.json`, `break-results.json`, `daily-results.json`, `stars-results.json`: actual browser
  state, first-run scoring, Encore sealing, Undo and restart abuse, wrong answers, alternatives, clues and star gates.
- `fullplay/`: full games through the interface against every opponent, plus pass-and-play, with console exceptions checked.
- `final-frames/`, `grab-frames/`, `touch/`, `last-frames/`, `audit/`: responsive, keyboard, pointer, touch, resize, offline,
  comparison, reduced-motion, grayscale and mechanical audit evidence.

#### Spec discrepancy

Fence (`r1-5`) does not have the asserted immediate win `10-15`. Blue can jump `21x14` over Amber 17.
`10-14` fills that landing and wins immediately. The shipped book line is unchanged, and `10-15` is judged by the
actual American checkers rules. No shared specification was edited.

#### Choices made unattended

Kept all four accepted defaults: mandatory jumps, Amber and Blue side names, Grades K-12, and Titan's three-second budget.
All puzzle material came from the supplied spec, so no external puzzle collection was fetched.
Portrait art is a crop of the same painted arcade. Sprite marks, crowns, halos, robots and sparks are painted.
Transparent targets expand to 44 px around exact square centres in small previews.

#### Limits

The cold review closed the clue-only best-score loophole: a clue is a puzzle try and costs one Move, just like a
wrong try. Three clues still play the answer and award one star, but cannot tie an unassisted minimum. The How to
play panel and clue prompt disclose this. Unassisted round minima remain 6, 10, 12, 23 and 40.

The same review keeps the last valid puzzle index after an award, resumes a book reply after Flip, and defers
Hints/resize redraws until a moving puck lands. Puzzle finishes now name the jump or trap and leave more of the
painted board visible. See `codex-review.md` for current verification; the build report records the earlier state.

Tests ran in Windows Chrome, including emulated Chromebook and phone viewports. No physical Chromebook, physical phone,
child or adult human strength trial was available. The top opponent is measured against the ladder, not rated against people.
The independent cold review is recorded in `codex-review.md`. No sign-off or deployment has been performed.

#### Live early

Live early for Cory to see, 2026-11-12, process not exempted. tool.draft.json was renamed to tool.json only so the site lists the game; Refine, Exit check, Art and voice, Finish check and Sign-off are still owed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-10)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-10)
- 2026-11-25: handoff.md folded in (last changed 2026-11-11)
