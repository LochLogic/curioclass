# Codex report: chess (Recess)

## Built

Built the paper theatre on `kit:recess`: seven offline opponents, friend play, nine five-puzzle acts and the daily. All 45 specified puzzles ship unchanged.
Workspace confirmed as `S:\CurioClass-codex`. Only `tools/chess/` and `_scratch/chess/` were written. No commits, publication or polish round. Bundle: 1,422,392 bytes (1.36 MiB); readable engine: 38,837 bytes.
Unattended choices followed the spec defaults: Grades 3-12, Mouse and White first, friends stay put, hints on, every puppet open. No questions were needed.

## Rules check

The same 0x88 generator drives rules, hints and search. Published perft counts from the game generator:

| Position | Depth | Stated | Computed | Result |
|---|---:|---:|---:|---|
| start | 4 | 197281 | 197281 | PASS |
| Kiwipete | 4 | 4085603 | 4085603 | PASS |
| position3 | 5 | 674624 | 674624 | PASS |
| position4 | 4 | 422333 | 422333 | PASS |
| position5 | 4 | 2103487 | 2103487 | PASS |

- PASS: starting arrangement and 20 moves.
- PASS: sliders cannot jump.
- PASS: knight jumps.
- PASS: pawn double move needs both empty squares.
- PASS: pinned rook cannot expose king.
- PASS: kings cannot touch.
- PASS: king cannot capture defended piece.
- PASS: double check only king can answer.
- PASS: castle w king.
- PASS: castle w queen.
- PASS: castle b king.
- PASS: castle b queen.
- PASS: castling needs b1 empty.
- PASS: castling cannot cross attacked f1.
- PASS: castling cannot leave check.
- PASS: castling cannot land in check.
- PASS: king rights never return.
- PASS: rook rights never return.
- PASS: home rook capture loses right.
- PASS: en passant removes adjacent pawn.
- PASS: en passant expires.
- PASS: en passant exposing rank is illegal.
- PASS: all four quiet promotions.
- PASS: all four capture promotions.
- PASS: fools mate.
- PASS: checkmate precedes halfmove 100.
- PASS: stalemate.
- PASS: fifty moves automatic.
- PASS: threefold automatic.
- PASS: unavailable EP does not change repetition key.
- PASS: pinned EP does not change repetition key.
- PASS: available EP changes repetition key.
- PASS: material K7.
- PASS: material KB6.
- PASS: material KN6.
- PASS: material KNN5.
- PASS: material KP6.
- PASS: same color bishops draw.
- PASS: opposite color bishops can mate.
- PASS: knight versus knight can mate.
- PASS: incremental hashes and sums survive 100 random moves and unmake.

UI checks also passed king-then-rook castling, named pin attacker plus dashed line, all four promotion keys, Escape cancellation, accurate moved-king/moved-rook messages, and every draw card.

## Puzzles and levels

Own solver: exhaustive legal mate enumeration and mate-in-two search against every defence; material minimax at three plies plus four capture plies, with a separate second-move check. All 45 stated lines are legal.
In the table, the line excludes the opponent lead-in. Material margins are best-first versus next-first, then best-finish versus next-finish, in centipawns.

| ID / act | Stated solver line, with reply | Computed | Result |
|---|---|---|---|
| yd6eW / m1-1 | `d5g2` | mates: d5g2 | PASS |
| BKLTK / m1-1 | `d5g2` | mates: d5g2 | PASS |
| FPBtR / m1-1 | `d4f2` | mates: d4f2 | PASS |
| Oo2Yb / m1-1 | `g6h6` | mates: g6h6 | PASS |
| 9Bsuq / m1-1 | `e3e6` | mates: e3e6 | PASS |
| 6FooS / m1-2 | `c4e6` | mates: c4e6 | PASS |
| WS1ZL / m1-2 | `g3h4` | mates: g3h4 | PASS |
| OxJo0 / m1-2 | `g6h6` | mates: g6h6, g6h5 | PASS |
| LKlGq / m1-2 | `g4g7` | mates: g4g7 | PASS |
| COr8l / m1-2 | `f4f8` | mates: f4f8 | PASS |
| ITD5U / m1-3 | `f3h1` | mates: f3h1 | PASS |
| iziys / m1-3 | `b4e1` | mates: b4e1 | PASS |
| X74cN / m1-3 | `f8d6` | mates: f8d6 | PASS |
| cVJhU / m1-3 | `g3c7` | mates: g3c7 | PASS |
| XkzBv / m1-3 | `d8d1` | mates: d8d1 | PASS |
| jqG75 / m2-1 | `c1c8 e4e8 c8e8` | unique key c1c8, no mate in one | PASS |
| 97cz2 / m2-1 | `c8c1 a4d1 c1d1` | unique key c8c1, no mate in one | PASS |
| bkWnP / m2-1 | `g4d1 d5d1 d8d1` | unique key g4d1, no mate in one | PASS |
| F8NkT / m2-1 | `e4f6 e7f6 d3h7` | unique key e4f6, no mate in one | PASS |
| pdf76 / m2-1 | `c8c1 e2c1 b3d1` | unique key c8c1, no mate in one | PASS |
| su5D2 / m2-2 | `d5e7 g8h7 f2h2` | unique key d5e7, no mate in one | PASS |
| popOX / m2-2 | `b1c1 e3c1 e8e1` | unique key b1c1, no mate in one | PASS |
| hLvdJ / m2-2 | `e4f6 g7f6 d3h7` | unique key e4f6, no mate in one | PASS |
| 1JTIv / m2-2 | `d7h7 g5h7 a7g7` | unique key d7h7, no mate in one | PASS |
| 4KfY8 / m2-2 | `g4f6 e8f8 d2h6` | unique key g4f6, no mate in one | PASS |
| MS7Mo / m2-3 | `e3e2 d1e1 d3g3` | unique key e3e2, no mate in one | PASS |
| 8tsRc / m2-3 | `a7f2 e1d2 e5e3` | unique key a7f2, no mate in one | PASS |
| ZrgCo / m2-3 | `e7e8n d6c6 h7c7` | unique key e7e8n, no mate in one | PASS |
| QtZPh / m2-3 | `f5g6 e8e7 c4f7` | unique key f5g6, no mate in one | PASS |
| c4h9d / m2-3 | `d2g2 e3g3 h6h5` | unique key d2g2, no mate in one | PASS |
| w8biZ / mat-1 | `d5e7 g8h8 e7g6` | margins 1200 / 600 cp | PASS |
| mDxnD / mat-1 | `c6c5 d1d8 e8d8` | margins 200 / 300 cp | PASS |
| ugKOP / mat-1 | `e4f6 e5f6 f3d5` | margins 700 / 900 cp | PASS |
| 8BvWL / mat-1 | `d3h7 g8h7 d2d4` | margins 300 / 500 cp | PASS |
| tHNM3 / mat-1 | `c3d5 e3d4 d5b6` | margins 400 / 400 cp | PASS |
| RRRzQ / mat-2 | `d3b5 a6b5 d1d4` | margins 400 / 800 cp | PASS |
| Xak5l / mat-2 | `d1a4 c8d7 a4b4` | margins 300 / 300 cp | PASS |
| P88XH / mat-2 | `f3g5 f7e8 d1g4` | margins 300 / 300 cp | PASS |
| qMMfE / mat-2 | `d1d5 e5e6 d5h5` | margins 500 / 800 cp | PASS |
| Bv8Tk / mat-2 | `c7d6 g8f7 e8f8` | margins 300 / 300 cp | PASS |
| VQjbl / mat-3 | `c5g1 f3d1 g1h2` | margins 300 / 300 cp | PASS |
| ZuAAs / mat-3 | `f5d3 c2d3 a5g5` | margins 300 / 300 cp | PASS |
| LDMBw / mat-3 | `e5g4 g1g4 f6c3` | margins 300 / 600 cp | PASS |
| PEWkx / mat-3 | `c1f4 e5e6 f4b8` | margins 500 / 400 cp | PASS |
| Q2ZXU / mat-3 | `e5e6 d7e5 e6f7` | margins 400 / 400 cp | PASS |

Act minima computed as 5 player moves for mate-in-one, 10 for the other six acts. Three stars require zero wrong tries/clues, two allow one or two; this was exercised at each cutoff. All nine acts were played through with real board input.
OxJo0 accepts both g6h6 and g6h5; the alternative was also played in the browser. ZrgCo was completed through the knight-promotion fan.

## Computer opponent

Stockfish 19, `UCI_LimitStrength=true`, one thread, development only. Final evidence: 440 anchor games including 40 at half Lion budget, plus 600 chain games. Colors alternate; 20 positions per 40-game anchor come from a 50-position pool of common openings, four to eight moves in, screened within 75 cp by our evaluation.
Stockfish used fixed times from rounded, measured pilot means: Owl 6 ms, Badger 52 ms, Raven 55 ms, Lion 150 ms; half Lion 75 ms. Final measured means vary with positions and parallel load. Adjudication: both engines above 1000 cp for five moves; draw after 150 moves each.
Elo uses logistic maximum likelihood, draws as half. The 95% intervals are model-based; chain intervals propagate Owl uncertainty. These are engine comparisons, not human FIDE ratings.

| Puppet / target | Final depth / nodes / blunder / noise cp | Games and anchor scores | Elo (95%) | Search mean / peak ms |
|---|---|---|---|---|
| Mouse / 450 | 1 / 5k / 40% / 190 | 200 versus next puppet; next scores 182.5/200 | 308 (146-469) | 0.6 / 20.2 |
| Rabbit / 750 | 1 / 20k / 20% / 100 | 200 versus next puppet; next scores 162.5/200 | 715 (577-852) | 0.6 / 74.4 |
| Fox / 1050 | 1 / 60k / 12% / 60 | 200 versus next puppet; next scores 186.0/200 | 970 (847-1093) | 0.7 / 31.9 |
| Owl / 1350 | 2 / 150k / 4% / 40 | 1320: 23/40; 1500: 18/40 | 1419 (1341-1498) | 7.2 / 456.0 |
| Badger / 1650 | 4 / 500k / 1% / 20 | 1500: 31/40; 1800: 15/40 | 1713 (1629-1797) | 46.7 / 822.6 |
| Raven / 1950 | budget / 12k / 0 / 0 | 1800: 28.5/40; 2000: 26/40; 2250: 16/40 | 2093 (2022-2164) | 65.9 / 1214.3 |
| Lion / 2250 | budget / 25k / 0 / 0 | 2000: 26/40; 2250: 18.5/40; 2400: 19/40 | 2245 (2176-2314) | 104.8 / 1958.7 |

PASS all target tolerances. Half Lion: 12,500 nodes, 17/40 versus 2250, estimate 2197 (2089-2306), 51.5 ms mean; point estimate drops 48 Elo.
Visible thinking is at least 500 ms. Caps are 1/1/1.5/2/3/5/8 seconds. A 3x-desktop estimate remains below those caps; this is not a physical Chromebook measurement.
Browser worker matches, final settings (wins/draws/losses for the stronger puppet):

- PASS Mouse vs random: 20/0/0 over 20 full games.
- PASS Rabbit vs Mouse: 19/1/0 over 20 full games.
- PASS Fox vs Rabbit: 19/0/1 over 20 full games.
- PASS Owl vs Fox: 20/0/0 over 20 full games.
- PASS Badger vs Owl: 20/0/0 over 20 full games.
- PASS Raven vs Badger: 19/0/1 over 20 full games.
- PASS Lion vs Raven: 8/1/1 over 10 full games.

Search features live in `createChessEngine`: `Position` has typed-array make/unmake, incremental material/PST and two-half Zobrist hashing; `Search.run` has iterative deepening, root bounds and aspiration; `Search.search` has PVS, the 2^21-entry table, null move with verification, LMR, check extension, futility and late-move pruning.
`Search.order/pick` use table move, SEE/MVV-LVA, promotion, killers, counter-move and history with maluses; `Search.qsearch` has check evasions, stand pat, SEE and delta pruning. `Search.evaluate` contains tapered material/PST, mobility, king safety, pawn structure and endgame terms. Table memory is about 30 MiB, not file size.
Final hot-path cleanup uses numeric hash history and shared typed tables rather than per-node strings, arrays or emitter closures. A 46-position fixed-budget comparison matched the previous engine exactly in move, depth, node count and score; `allocation-parity.json` preserves the proof. Root-level choice objects remain outside the recursive search.
Lion tactical suite: PASS 44/45 (97.8%) within budget. The one miss is the documented queen-first computer-promotion policy on ZrgCo; the actual puzzle works. No Stockfish code, weights or opening book ship.

## Break it

- PASS wrong tries, clues, Undo, Restart and reload never lower puzzle tallies. Three tries show the line and cap stars; clean acts score 5 or 10.
- PASS finished-act and daily replays use Encore and cannot improve stars/bests. Daily keys are puzzle IDs, preventing date-change farming.
- Fixed a final-celebration reload race: result is now sealed before the delay and its pending award resumes once. Act test retained score 6 / two stars; daily retained score 3 / two stars.
- PASS CPU takeback cutoffs: zero gives three stars, one gives two, four gives one; score stayed 1/2/5 respectively. CPU losses and all draws grant no award; friend games grant none.
- PASS Undo interrupts Lion, removes the appropriate one or two half-moves, keeps Moves, and cannot receive a late worker reply. Loss Undo reopens play.
- PASS initials save disappears after one entry; score-dialog Tab stays trapped. Test hooks use `chess-test`, so loaded test positions cannot affect ordinary scores.
- PASS random mover loses 20/20 to Mouse. Real jittered drag, keyboard-only friend mate, touch-only 390x844 mate, resize during a capture and muted sound were exercised.
- PASS final runtime checks: zero exceptions and zero HTTP requests. Calm check: zero running animations. External-engine assistance remains inherently possible on a device-only game.

## Look board

Painted before logic: [opening](../../_scratch/chess/look/hero-opening.png), [in progress](../../_scratch/chess/look/hero-play.png), [best-moment concept](../../_scratch/chess/look/hero-best.png), each 1366x768. These are art composites; browser evidence is separate.
The spec made the direction clear, so one crimson/gold paper-theatre direction was kept. The first cover made the king human-looking; it was repainted as an abstract chess token. No painted text.

## Grab check

Best moment: the queen folds and leaves the stage while the rook lands, [capture frame](../../_scratch/chess/focus/capture.png); the final win tips the king under a narrowing spotlight, [frame](../../_scratch/chess/final/win-light.png).
Flattest moment was the cramped preview picker. The build now gives its controls room and keeps preview squares at 44 px. Side-by-side inspection used [shell demo](../../_scratch/chess/frames/shell-demo.png), [Beat Lab](../../_scratch/chess/frames/classroom.png) and [this world](../../_scratch/chess/final/world-final.png). It reads as a physical toy theatre, distinct from both.

## Class creep check

PASS: no lesson header, voice, lesson card, standard code, objective, skill or correct-answer text. The sole `learn` substring is the spec-required Mouse strength line, "Just learned how the pieces move"; it describes the opponent.

## Sources

- [Lichess database](https://database.lichess.org/#puzzles): CC0, source states "Database exports are released under the Creative Commons CC0 license." Only the exact 45 spec rows ship.
- [Official Lichess mirror](https://huggingface.co/datasets/Lichess/chess-puzzles): `license:cc0-1.0`; selection provenance in the spec. No new puzzle set was gathered.
- [FIDE Laws](https://handbook.fide.com/chapter/E012023): classic moves and endings, with original wording and the spec's automatic draw policy.
- Original paintings generated with OpenAI gpt-image, atlas normalization and WebP encoding for Curio Class. Original engine/UI/synthesized sound; original Staunton-family silhouettes.
- [Stockfish](https://stockfishchess.org/download/), GPL v3: dev-time test executable only, kept in Scratch.

## Done when

- PASS perft at every required depth: five exact totals above.
- PASS both castles/colors, b1 occupancy, attacked paths, moved king/rook and their kind lines.
- PASS en passant timing, removed pawn and exposed-rank pin.
- PASS four promotions by buttons/keys, Queen first, Escape cancels.
- PASS mate, stalemate, repetition, fifty moves and all insufficient-material cases.
- PASS pin explanation, named attacker and dashed line.
- FAIL physical Chromebook cap check: unavailable. PASS desktop budgets, live controls and immediate worker cancellation; slow-device times are explicitly estimates.
- PASS calibration: all point estimates within target tolerances, intervals reported, 120 Lion games and half-budget comparison, no runtime Stockfish.
- PASS listed search features and tactical-suite threshold (44/45).
- PASS final browser ladder: 20 games per lower pair and 10 Lion/Raven; every stronger puppet wins more often.
- PASS all 45 exact puzzle lines, every mate-in-one alternative and unique mate-in-two key.
- PASS CPU two-half-move Undo, star cost and nondecreasing Moves.
- PASS puzzle Restart tally, first-run award and Encore, including final-animation reload.
- PASS complete keyboard and 390x844 touch games; controls above fold at 1366x768 and targeted compact previews.
- PASS calm motion: static shadows/rims, flat fallen pieces, no running animation.
- PASS U/R/M/S belong to the shell; H/F/C/P to the game; Ctrl+Z works.

## Frames looked at

Three pre-logic hero composites; 16 play frames via `play/contact.png` plus phone/pin/capture details; all 11 size/comparison frames; final picker, acts, preview, world, win and Black-perspective capture frames; grayscale proof.
All 57 audit PNGs were inspected in `audit-contacts/contact-1.png` through `contact-4.png`. Audit found 347 leads, principally intentional modal/coordinate overlaps, modal focus and two short picker overflows. Background inertness, decorative coordinate semantics, board focus and compact CPU/act pickers were fixed; targeted browser checks confirmed every picker control visible, 44 px squares and live grid focus. No whole audit was rerun.
The audit's Read/voice hints do not apply to Recess. Its covered background cells are intentional; the final version makes that background inert. `final/last-checks.json` confirms the shell focus trap and capture ownership. No voice stub was required.

## Art made

Six final painted WebP assets: theatre, board material/frame, twelve-piece atlas, fourteen-pose puppet atlas, paper and 1200x750 cover. Total 1,215,704 bytes. One cover redraw. All final pieces and portraits retain real alpha; atlases were cropped/aligned without green-keying away their painted edges.
The board frame and controls reuse painted material. Code draws exact cells/hit areas, coordinates, legal dots, rings, attack line and lighting geometry. No missing art.
Palette checks independently reproduced: text/curtain 8.38, text/backdrop 16.96, text/floor 15.01, gold/floor 11.49; ink/light 10.88, ink/dark 3.64, ivory/dark 3.63; menu text 11.87. Ivory/ink outlines and the grayscale frame preserve side readability.

## Shell changes wanted

Escape or remove literal HTML examples in the `kit/recess.js` header: they break script parsing and trigger the CSS inliner inside JavaScript. The generated-file workaround is `_scratch/chess/bundle.py`; shared files were not edited. Shell-native focus trapping/inertness and 44 px initials arrows are also wanted; Chess supplies these fixes locally.

## Left open

Physical Chromebook validation and the 1M search-nodes/second aspiration are not established. Lion's queen-first promotion policy misses the knight mate in two in its tactical test; puzzle play is correct. Elo intervals are model-based and broader for the lower chain.
The unused 2M-node pilot hit its 20-minute command limit; the superseded 400k-node batch was stopped after final tuning. Both are preserved separately. Final calibration, final browser matches, full audit and all reported scoring checks completed. No Chrome/server started for this build remains intentionally running.
Artifact map: `handoff.md`; hashes and exact validation evidence: `_scratch/chess/verification-manifest.json`. Build only.

## Move review (2026-11-09)

Added display-only review to every computer level and pass-and-play, including finished games. A painted-paper move book holds First, Back, Forward and Latest, with a tappable move list. The historical board includes its last-move marks and captured pieces; the selected move is highlighted. A paper ribbon names the position and one Back to the game button restores live play. The book folds on phones. Existing painted materials were reused.

Home enters review, Left/Right step and End returns live. Live board arrows keep their existing square navigation; Left/Right also enter review when focus is outside the board. Pieces cannot be selected, dragged or played in review. Flip turns only the review view. The live position, worker, move tally, takebacks and reward records are independent. Computer replies leave the review cursor fixed and add a waiting-move cue. A result reached during review waits to open its card until the player returns. Result cards, including the shell-owned computer win card, offer Replay the moves. No review cursor is persisted; reload uses the existing live-game resume path.

Rebundled with CURIO_DRAFT=1 and scripts/bundle_tool.py: 1,433,998 bytes. Chrome used debugging port 9990, muted audio, isolated Scratch profiles and host port 8795. Build limit: 120 seconds; functional batch: 270 seconds; final-layout batch: 210 seconds; targeted Flip batch: 180 seconds. Each test runner also bounds its async work and shuts down its own Chrome/server.

Chrome test results (37 functional checks, 14 final-layout/edge checks and one targeted Flip check):

| Test | Result |
|---|---|
| 30-move game: all 60 half-moves backwards and forwards | PASS |
| Review cannot change live state, move tally, takebacks or rewards | PASS |
| Tapping move 13 selects its exact position and highlights it | PASS |
| Back to the game restores live board and editable grid | PASS |
| Keyboard-only game reaches checkmate | PASS |
| Checkmate result card opens replay at start | PASS |
| Keyboard Right steps replay forward | PASS |
| Keyboard Left steps replay backward | PASS |
| Keyboard Home enters opening review from live board | PASS |
| Keyboard End restores live checkmate | PASS |
| Friend Undo after review still removes one half-move and retains Moves | PASS |
| Repetition draw offers replay from result card | PASS |
| Draw review remains finished and grants no stars | PASS |
| Worker continues and review stays put: Mouse | PASS |
| Computer takeback stays separate: Mouse | PASS |
| Worker continues and review stays put: Rabbit | PASS |
| Computer takeback stays separate: Rabbit | PASS |
| Worker continues and review stays put: Fox | PASS |
| Computer takeback stays separate: Fox | PASS |
| Worker continues and review stays put: Owl | PASS |
| Computer takeback stays separate: Owl | PASS |
| Worker continues and review stays put: Badger | PASS |
| Computer takeback stays separate: Badger | PASS |
| Worker continues and review stays put: Raven | PASS |
| Computer takeback stays separate: Raven | PASS |
| Worker continues and review stays put: Lion | PASS |
| Computer takeback stays separate: Lion | PASS |
| Reload mid-review loads live state and no review cursor | PASS |
| Resume after mid-review reload stays live | PASS |
| Cheat: replayed mating move and repeated review cannot earn a star | PASS |
| Real CPU win after takeback still earns two stars | PASS |
| Computer win card replay cannot improve stars/best or create initials entries | PASS |
| 390x844 move book folds by default and fits stage | PASS |
| Phone touch selects a historical move and blocks play | PASS |
| Phone folded review keeps Back to the game above the fold | PASS |
| Calm review has no running animation | PASS |
| Chrome has no runtime exceptions | PASS |
| 1366x768 review board and every stage control above fold | PASS |
| Final review layout hides redundant live prompt | PASS |
| 1366x768 live controls fit with move book open | PASS |
| Historical board reconstructs castling | PASS |
| Historical board reconstructs en passant | PASS |
| Historical board reconstructs promotion | PASS |
| Computer checkmate leaves review in place with waiting cue | PASS |
| Returning after computer checkmate opens loss card with replay and takeback | PASS |
| Loss-card replay opens read-only history | PASS |
| 390x844 expanded review exposes all four steps, return and move list | PASS |
| 390x844 folded review keeps game controls above fold, with calm still | PASS |
| Phone return restores live pieces and closes review ribbon | PASS |
| Puzzle mode unchanged and move book hidden | PASS |
| Final Chrome runtime has no exceptions | PASS |
| Flip during review changes only the view; return restores live orientation | PASS |

The 30-move fixture covers 60 legal half-moves, checked at every position in each direction, with last-move markers and current-move highlighting. The reward attack repeatedly attempts a mating move from history and cycles review 50 times: no award and no state changes. A subsequent real win after a takeback still earns two stars; replay cannot improve its best/stars or add initials entries. All reward tests use the existing chess-test namespace.

Initial setup FAIL: the first bundler invocation skipped the draft and the first test loaded the previous bundle. Enabled CURIO_DRAFT, rebuilt and reran successfully. The first visual pass exposed an overly tall review wing; reduced the book height and replaced the redundant live prompt during review. The final desktop and phone bounds checks PASS. No remaining move-review failures.

Frames inspected directly (final 1366x768 frames and exact 390x844 iframe crops):

- [Desktop review](../../_scratch/chess/move-review/final/review-1366x768.png)
- [Desktop live position](../../_scratch/chess/move-review/final/live-1366x768.png)
- [Checkmate result card](../../_scratch/chess/move-review/final/checkmate-card-1366x768.png)
- [Checkmate replay](../../_scratch/chess/move-review/final/checkmate-replay-1366x768.png)
- [Repetition-draw replay](../../_scratch/chess/move-review/final/draw-replay-1366x768.png)
- [Computer checkmate waiting while reviewing](../../_scratch/chess/move-review/final/computer-checkmate-waiting-1366x768.png)
- [Phone live with folded book](../../_scratch/chess/move-review/final/live-folded-390x844.png)
- [Phone review with expanded book](../../_scratch/chess/move-review/final/review-expanded-390x844.png)
- [Phone review with folded book](../../_scratch/chess/move-review/final/review-folded-390x844.png)

Exact checks and fixtures: `../../_scratch/chess/move-review/checks.json`, `final/checks.json`, `final/flip-check.json` and `thirty-move-game.json`. The seven preliminary frames were also inspected; final frames above supersede their layout. Tests and verification manifest remain in Scratch. Only tools/chess/ and _scratch/chess/ were written. Protected shared-file hashes match; no git commits.
