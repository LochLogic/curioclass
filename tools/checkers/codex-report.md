# Codex report: checkers (Recess)

## Built

Built in `S:\CurioClass-codex`, with writes confined to `tools/checkers/` and `_scratch/checkers/`.
Readable `src.html`, offline `checkers.html`, built draft metadata, notes, handoff, painted art and provenance are present.
Six computer rivals, pass-and-play, five rounds / 25 puzzles, mirrored daily, resuming, forced jumps, takebacks and shell rewards.
Bundle: **1,202,394 bytes**, below 6 MB. SHA-256: `f019414e94249de2c5ef66881bf81fcf04ae61d2b095bee953929ac453506fc5`.
No commits, shared-kit edits, shelf edits, deployment, review round or polish round. This is a Build handoff.
All four accepted spec defaults were kept without questions. Automated gentle and strong play policies stood in for child/adult play.
No physical child, adult strength trial, Chromebook or phone was available; emulated viewports are not hardware testing.
Palette contrasts independently recomputed: text/frame 15.23, dim/frame 8.33, mint/dark 13.61, must/dark 6.33, grid/dark 4.08; puck ink 8.75 / 5.56.

## Rules check

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

## Puzzles and levels

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

## Computer opponent

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

## Break it

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

## Look board

Paintings, cover and these three 1366x768 frames were made and viewed before game logic. The spec gave an obvious night-arcade direction; no alternate world was needed.
Kept tactile acrylic, violet glass, dark cabinets, amber/cyan light and six painted robots. Direction chosen for immediate toy-like appeal.

![Opening](../../_scratch/checkers/look/opening.png)

![Game in progress](../../_scratch/checkers/look/progress.png)

![Crown moment](../../_scratch/checkers/look/best.png)

## Grab check

Most satisfying moment: the third capture lands on the far row and a crown drops onto the glowing puck.
Flattest moment: a cramped preview picker and blank side-panel space. Compact layouts retain the painted world and keep all controls above the fold.
A stray neighboring sprite sliver on Nova was cropped away. No art was replaced with code placeholders.

![Actual crown capture](../../_scratch/checkers/grab-frames/crown-moment.png)

![Beside the shell demo and Collision Lab](../../_scratch/checkers/grab-comparison.jpg)

The cabinet world, glass table, pucks and robot badges are visually distinct from both reference frames. Final visual approval belongs to the owner.

## Class creep check

Whole-word source scan: standard, objective, learn, skill, lesson, correct answer, well done: **0 each**. No standard codes, kit:curio, voice or em dash.
The only rewards UI is the Recess shell. Parent/teacher material is in notes.md, copied from the spec.

## Sources

- Fourteen original positions from the supplied spec: original Curio Class material.
- W. T. Call, Midget Problems (1913), archive.org/details/midgetproblemsal00call: eleven positions and move lists, composer names retained.
  Source status as recorded in the spec: "Copyright, 1913, by William Timothy Call"; public domain in the US, and life-plus-70 countries (Call died 1917).
- J. Lyman, A Game of Draughts (1881), archive.org/details/gameofdraughtsse00lyma: rules cross-check only; Library of Congress: "no known copyright restrictions".
- Modern English draughts / WCDF practice: facts recorded in the spec, no copied prose. No external puzzle fetching was needed.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Prompts, alpha-preserving crops and raw paintings are retained.

## Done when

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

## Frames looked at

Original four generated paintings; three early browser hero frames and their compositing studies; every captured frame via contact sheets, with key frames opened full size.
77 captured PNGs were inspected, including the 16 audit frames and targeted correction / persistence / motion frames.
Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 390x844 and 375x812. Phone also checked through the audit iframe host.
Folders: look, first-frames, check-frames, extra-frames, final-frames, grab-frames, last-frames, touch, fullplay, audit, after-audit-frames, final-fix-frames, reload-frames, cancel-chain-frames, motion-finish-frames.
The original 680 table overflow and earlier keyboard probe are preserved; corrected frames and assertions supersede them. Full grayscale: `grayscale.png`.

## Art made

21 finished WebP files, 787,476 bytes: landscape and portrait arcade, exact board, cover, four pucks, six robots, two halos, four crown frames and sparks.
Generated with the built-in imagegen tool. Raw paintings copied into art/raw; atlas cells split and resized with alpha preserved. Nova crop tightened; no full redraw needed.

## Shell changes wanted

kit/recess.js documentation header contains a literal closing script tag; inlining it ends the script. Its stylesheet example also gets expanded.
The local bundle wrapper strips only that comment prefix from the generated file. Shared implementation and CSS are untouched. Use the wrapper documented in handoff.md.
The shared bundler also requires the non-self-closing stylesheet token. The wrapper normalizes that token in this source.

## Left open

The clue-only minimum-Moves best conflict requires a scoring decision. The explicit spec formulas were kept under the no-improvisation rule.
Physical Chromebook/phone performance, real youngest-grade/adult play and adult strength testing remain unverified. Visual judgment is the owner's.
No sign-off, deployment or independent review has been performed. All started browser/server processes were closed before this report was written.
