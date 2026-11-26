# Chess: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: chess (Recess)

#### Built

Built the paper theatre on `kit:recess`: seven offline opponents, friend play, nine five-puzzle acts and the daily. All 45 specified puzzles ship unchanged.
Workspace confirmed as `S:\CurioClass-codex`. Only `tools/chess/` and `_scratch/chess/` were written. No commits, publication or polish round. Bundle: 1,422,392 bytes (1.36 MiB); readable engine: 38,837 bytes.
Unattended choices followed the spec defaults: Grades 3-12, Mouse and White first, friends stay put, hints on, every puppet open. No questions were needed.

#### Rules check

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

#### Puzzles and levels

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

#### Computer opponent

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

#### Break it

- PASS wrong tries, clues, Undo, Restart and reload never lower puzzle tallies. Three tries show the line and cap stars; clean acts score 5 or 10.
- PASS finished-act and daily replays use Encore and cannot improve stars/bests. Daily keys are puzzle IDs, preventing date-change farming.
- Fixed a final-celebration reload race: result is now sealed before the delay and its pending award resumes once. Act test retained score 6 / two stars; daily retained score 3 / two stars.
- PASS CPU takeback cutoffs: zero gives three stars, one gives two, four gives one; score stayed 1/2/5 respectively. CPU losses and all draws grant no award; friend games grant none.
- PASS Undo interrupts Lion, removes the appropriate one or two half-moves, keeps Moves, and cannot receive a late worker reply. Loss Undo reopens play.
- PASS initials save disappears after one entry; score-dialog Tab stays trapped. Test hooks use `chess-test`, so loaded test positions cannot affect ordinary scores.
- PASS random mover loses 20/20 to Mouse. Real jittered drag, keyboard-only friend mate, touch-only 390x844 mate, resize during a capture and muted sound were exercised.
- PASS final runtime checks: zero exceptions and zero HTTP requests. Calm check: zero running animations. External-engine assistance remains inherently possible on a device-only game.

#### Look board

Painted before logic: [opening](../../_scratch/chess/look/hero-opening.png), [in progress](../../_scratch/chess/look/hero-play.png), [best-moment concept](../../_scratch/chess/look/hero-best.png), each 1366x768. These are art composites; browser evidence is separate.
The spec made the direction clear, so one crimson/gold paper-theatre direction was kept. The first cover made the king human-looking; it was repainted as an abstract chess token. No painted text.

#### Grab check

Best moment: the queen folds and leaves the stage while the rook lands, [capture frame](../../_scratch/chess/focus/capture.png); the final win tips the king under a narrowing spotlight, [frame](../../_scratch/chess/final/win-light.png).
Flattest moment was the cramped preview picker. The build now gives its controls room and keeps preview squares at 44 px. Side-by-side inspection used [shell demo](../../_scratch/chess/frames/shell-demo.png), [Beat Lab](../../_scratch/chess/frames/classroom.png) and [this world](../../_scratch/chess/final/world-final.png). It reads as a physical toy theatre, distinct from both.

#### Class creep check

PASS: no lesson header, voice, lesson card, standard code, objective, skill or correct-answer text. The sole `learn` substring is the spec-required Mouse strength line, "Just learned how the pieces move"; it describes the opponent.

#### Sources

- [Lichess database](https://database.lichess.org/#puzzles): CC0, source states "Database exports are released under the Creative Commons CC0 license." Only the exact 45 spec rows ship.
- [Official Lichess mirror](https://huggingface.co/datasets/Lichess/chess-puzzles): `license:cc0-1.0`; selection provenance in the spec. No new puzzle set was gathered.
- [FIDE Laws](https://handbook.fide.com/chapter/E012023): classic moves and endings, with original wording and the spec's automatic draw policy.
- Original paintings generated with OpenAI gpt-image, atlas normalization and WebP encoding for Curio Class. Original engine/UI/synthesized sound; original Staunton-family silhouettes.
- [Stockfish](https://stockfishchess.org/download/), GPL v3: dev-time test executable only, kept in Scratch.

#### Done when

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

#### Frames looked at

Three pre-logic hero composites; 16 play frames via `play/contact.png` plus phone/pin/capture details; all 11 size/comparison frames; final picker, acts, preview, world, win and Black-perspective capture frames; grayscale proof.
All 57 audit PNGs were inspected in `audit-contacts/contact-1.png` through `contact-4.png`. Audit found 347 leads, principally intentional modal/coordinate overlaps, modal focus and two short picker overflows. Background inertness, decorative coordinate semantics, board focus and compact CPU/act pickers were fixed; targeted browser checks confirmed every picker control visible, 44 px squares and live grid focus. No whole audit was rerun.
The audit's Read/voice hints do not apply to Recess. Its covered background cells are intentional; the final version makes that background inert. `final/last-checks.json` confirms the shell focus trap and capture ownership. No voice stub was required.

#### Art made

Six final painted WebP assets: theatre, board material/frame, twelve-piece atlas, fourteen-pose puppet atlas, paper and 1200x750 cover. Total 1,215,704 bytes. One cover redraw. All final pieces and portraits retain real alpha; atlases were cropped/aligned without green-keying away their painted edges.
The board frame and controls reuse painted material. Code draws exact cells/hit areas, coordinates, legal dots, rings, attack line and lighting geometry. No missing art.
Palette checks independently reproduced: text/curtain 8.38, text/backdrop 16.96, text/floor 15.01, gold/floor 11.49; ink/light 10.88, ink/dark 3.64, ivory/dark 3.63; menu text 11.87. Ivory/ink outlines and the grayscale frame preserve side readability.

#### Shell changes wanted

Escape or remove literal HTML examples in the `kit/recess.js` header: they break script parsing and trigger the CSS inliner inside JavaScript. The generated-file workaround is `_scratch/chess/bundle.py`; shared files were not edited. Shell-native focus trapping/inertness and 44 px initials arrows are also wanted; Chess supplies these fixes locally.

#### Left open

Physical Chromebook validation and the 1M search-nodes/second aspiration are not established. Lion's queen-first promotion policy misses the knight mate in two in its tactical test; puzzle play is correct. Elo intervals are model-based and broader for the lower chain.
The unused 2M-node pilot hit its 20-minute command limit; the superseded 400k-node batch was stopped after final tuning. Both are preserved separately. Final calibration, final browser matches, full audit and all reported scoring checks completed. No Chrome/server started for this build remains intentionally running.
Artifact map: `handoff.md`; hashes and exact validation evidence: `_scratch/chess/verification-manifest.json`. Build only.

#### Move review (2026-11-09)

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

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: chess

#### Played

Reviewed cold as a Grade 3 solo player and an adult, against CODEX-RECESS.md, GAMES.md and the chess spec.
Played the opening, friend checkmate, illegal input, takebacks, a puzzle, a computer reply and the daily before reading the builder's notes/source.
Then completed all nine acts, daily/Encore, keyboard and touch games, and a full game against every puppet.
The theatre grabs attention; readable paper pieces, warm light, puppets and folding captures remain strong.
The computer-game harness used dev-only Stockfish for human moves and the game's real browser workers for opponents.
Mouse, Rabbit, Fox, Owl, Badger and Raven lost; Lion drew by repetition. No referee or external engine ships.

#### Findings fixed

- **blocker, general, rebuild/startup:** the required ordinary bundler broke the shell's HTML-example comment, leaving a blank playbill. A tool-local copy omits only that documentation line; the shell runtime is identical. Plain bundling now works. Kit/scripts untouched.
- **blocker, family:chess, computer award:** opening Playbill or reloading during the win delay could discard earned stars. Reserve the result before the delay and consume it once on celebration, Playbill or reload.
- **should fix, family:chess, loss card:** a boolean argument shadowed `undo`, making "Take back a few moves" dead. Renamed it and restored the real handler; loss Undo reopens play.
- **should fix, family:chess, wrong-try reload:** pagehide saved the temporary wrong board, losing the last solved step. Keep the already-saved playable position and penalty until spring-back completes. Reload now retains both step and tally.
- **should fix, general, results/resume:** the background still announced a turn after checkmate or kept the opening prompt after resume; result/Encore dialogs also lacked their referenced title. Refresh prompts on return, show the terminal result and give every programme heading its dialog ID.
- **should fix, general, opening Restart:** the audit confirmed a dead Restart before any game existed. Disable it until a show starts; keep it live during play.
- **polish, family:chess, puzzle finish:** the flattest payoff was a generic line and burst. Reuse the theatre's tipped king and narrowing spotlight, gild the final move, and name the actual finish. Calm keeps the static picture; the next puzzle keeps its existing timing.

#### Findings left

No reproduced blocker or should-fix remains. Hardware/strength limits and accepted external assistance are listed below.
No lesson header, narration, lesson cards or standard codes were added. The grown-up note keeps the Recess spec's format.

#### Break it

- **Rules PASS:** all five perft totals match: 197281, 4085603, 674624, 422333, 2103487. Another 1,339 legal-move sets match independent python-chess.
- **41 edge cases PASS:** starting arrangement, blocked sliders, knight jump, pawn double block, pins, adjacent kings, defended captures and double check; both castles for both colors, b1 occupancy, attacked transit/landing, check, permanently lost rights and home-rook capture; en passant removal, expiry and rank pin; all four quiet/capture promotions; mate, stalemate, repetition, fifty moves, mate precedence, legal-EP repetition identity and every material case. Exact individual results: `../../_scratch/chess/review-rules/rules.json`.
- **Puzzles PASS:** shipped rows exactly match all 45 spec rows. Independent legality, all mate-in-one alternatives and 15 unique mate-in-two keys pass. Repeated the material solver; every first/second move has at least a pawn's margin. Independent Stockfish also chose all 30 stated material moves.
- **Act scoring PASS:** every act completed through board controls. Mate-in-one scores 5; mate-in-two and win-a-piece score 10; all clean runs award three stars.
- **Guessing/clues PASS:** wrong moves and clues count; three daily clues earn one star. Restart/reload cannot erase the tally. Reload during a wrong move now preserves the solved step too.
- **Replay PASS:** a completed daily returns as Encore; a clean replay cannot improve its stars or open another shell award. Daily remains keyed to puzzle ID, not date.
- **Undo PASS:** every puppet's think can be cancelled without a late reply; no lowered move tally. Puzzle reply Undo, friend Undo after mate, and CPU loss-card Undo work. CPU wins disable Undo.
- **Rapid input PASS:** 30 repeated move attempts during thinking make only one human move and no award. Undo rejects the late reply; rapid initials saving adds one row.
- **Access/motion PASS:** complete real-keyboard game, Ctrl+Z, complete touch games at 390 and 375, jittered drag, actual resize during capture, promotion focus/Escape, calm and muted finishes. No runtime exceptions in targeted checks.
- Evidence: `../../_scratch/chess/review-rules/`, `review-play/`, `review-final/`, `review-cheats/`; helper scripts remain in Scratch. Test hooks use the separate `chess-test` namespace.

#### Voice walk

Not applicable by the Recess brief: there is no narration or Read control. Walked Playbill, friend, computer, puzzles and daily with game sounds; checked mute. The shell owns sound controls.

#### Facts checked

- Moves/endings: FIDE rules as specified in `spec.md`, independently checked with python-chess and the published perft positions; Recess's automatic repetition/fifty-move policy is intentional.
- Puzzle IDs, positions, lines and CC0 credit: exact spec/Lichess records; no new dataset fetched. Both OxJo0 mates and ZrgCo's knight promotion were checked.
- Strength claims: inspected the existing 440 anchor-game records, checked grouping/duplicates, and confirmed the engine is unchanged. The builder's Lion estimate is an engine comparison, not a human rating. No new Elo calibration is claimed.
- Privacy wording matches the local-storage-only implementation. Class-creep search finds only Mouse's required "learned how the pieces move" description.

#### Sensitivity

None identified: original animal puppets and abstract classic pieces; no people, historical narrative or cultural-origin claims. No new art or sensitive content was introduced.

#### Flattest moment left

The longer puppet strength descriptions remain text-heavy. Kept the spec's plain descriptions so choosing a level is honest and clear.

#### Graphics

Kept all six painted assets; inspected the 12-piece and 14-pose atlases on the actual dark background, cover, stage, board and programme paper. No repaint was needed.
Inspected every review/audit frame via contact sheets and opened the phone, compact picker, capture and mate details. Checked all STANDARDS sizes, 390x844, calm, mute and grayscale.
Compared the current theatre with the existing shell-demo and Beat Lab frames. It owns a distinct physical world.
Best revised frame: `../../_scratch/chess/review-final/puzzle-finish-motion.png`; phone/calm counterparts are beside it. Bundle: 1,424,185 bytes, below 6 MB.

#### Audit

Completed the single audit: 19 leads, 57 frames; no runtime exceptions, resize locks or infinite calm motion.
Fixed its dead opening Restart. The other 18 leads were 8 lesson-hint/Read assumptions, 8 intentional modal-entry focus reports, and 2 checkbox-box measurements. Recess uses #prompt without narration; the Playbill has keyboard focus/background inertness; the checkbox has a tested clickable 44 px-high label, including outside its drawn box.
Inspected all 57 audit frames in `../../_scratch/chess/review-audit-contacts/`. The audit was not rerun. Final small save/resume and Restart corrections received targeted current-bundle regressions and new frames. Audit: `../../_scratch/chess/review-audit/audit.md`.

#### Left open

- No physical Chromebook was available. Desktop checks do not prove caps on actual school hardware.
- Retained the builder's documented calibration uncertainty, machine-speed limitation and queen-first computer promotion policy. The policy misses a knight mate in two in the tactical suite; puzzle promotion is correct and the spec requires queen unless knight mates immediately.
- External-engine help and deliberate local-storage editing cannot be prevented in an offline device-only game; these are accepted scope limits, not new reward paths.
- First parallel game batch timed out taking Badger's screenshot after six completed games. Retried Badger alone: full game finished in 36.81 s, longest observed think 0.516 s. Its result is saved before screenshotting.
- Unattended choices followed the brief/spec defaults; no questions, commits, shared-kit changes, publication or second review round. All writes stayed in `tools/chess/` and `_scratch/chess/`; bounded commands used only the named ports.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Chess build handoff

Open [chess.html](chess.html) for the complete offline game. [src.html](src.html) is the readable source.
The shelf remains unchanged and this is a Build-only draft. No commit, publication or polish round was started.

#### What is here

- `src.html`: all rules, search, 45 puzzles, rendering, motion, sound and persistence; shared Recess shell and stylesheet.
- `lib/recess-safe.min.js`: the shared shell verbatim except its bundler-directive documentation line is omitted.
- `chess.html`: generated offline file, approximately 1.36 MiB including the shell and painted assets.
- `tool.draft.json`: built Recess metadata and sources; `notes.md`: parent and teacher note.
- `art/`: painted theatre, board material, 12-piece atlas, 14-pose puppet atlas, programme paper and 1200x750 cover.
- `audit-states.json`: real-input paths for the playbill, friend, computer, puzzles and daily.
- `codex-report.md`: final results, settings, all 45 solver checks, artwork and remaining limits.

#### Rebuild

From `S:\CurioClass-codex`, run:

```powershell
$env:CURIO_DRAFT = '1'
python _scratch/chess/run.py 120 python scripts/bundle_tool.py chess
```

The ordinary repository bundler now works directly. The cold review found that rebuilding with the required command
reintroduced the shell-header fault. Chess now loads a local copy of the actual shared shell through the bundler's
library token. Only its HTML-example documentation line is omitted, preventing premature script termination and CSS
inlining inside JavaScript. No shell runtime code, kit file or bundler was changed.

The original working pieces and assembly helper are `_scratch/chess/engine.js`, `game.js` and `build.py`.
For future edits, change `src.html` and use the ordinary bundler above. `build.py` deliberately reassembles older working pieces.
The formatter and all third-party development packages are confined to Scratch and do not ship.
The final allocation cleanup removed transient hot-path arrays/closures and string history comparisons. A 46-position
comparison retained exactly the same move, depth, node count and score at fixed node budgets; see `allocation-parity.json`.

#### Evidence map

- `_scratch/chess/perft.json`, `rules.json`: five published perft positions and 41 rule checks.
- `solutions-0.json`, `solutions-30.json`: independent exhaustive mate checks and material-search margins for all 45 puzzles.
- `calibration-final-evidence.json`, `final-metrics.json`: the final 440 anchor games, 600 chain games and statistics.
- `browser-final-matches.json` (Owl/Fox, Badger/Owl), `browser-shipped-matches.json` (lower three pairs and Raven/Badger),
  `browser-lion-matches.json` (Lion/Raven): the 130 final browser games. Earlier files are pilot runs, not final evidence.
- `play/checks.json`: real keyboard, touch and drag paths, all nine completed acts, daily, persistence and Encore.
- `focus/checks.json`, `focus/runtime.json`: stars at every takeback cutoff, CPU win/loss, every result card, alternate mate,
  isolated test scores and zero HTTP requests; `reload-race.json`: reload before the final award, for act and daily.
- `look/hero-*.png`: the three painted composites made before rules code. `final/`, `frames/`, `play/`: browser frames.
- `audit/audit.md`: the single full mechanical audit; `audit-contacts/`: all 57 audit frames, inspected as four sheets.
- `verification-manifest.json`: final artifact hashes and checks. Interrupted and superseded pilots remain separate in Scratch.

#### Computer settings and calibration

Seven levels share one engine and legal-move generator. Raven and Lion differ only in node budget and the specified
opening-choice margin; they receive no score noise or deliberate blunders. Final Lion uses 25,000 nodes and Raven 12,000.
Every search is in a Blob worker. Undo and leaving the game terminate it immediately. The minimum visible think is 500 ms.

Stockfish 19 is a development-only executable in Scratch. Nothing from it, including weights, ships. Fixed Stockfish
times were selected from measured pilot means on this computer, rounded to milliseconds. The final means differ under
parallel batch load; all settings, scores, openings and timings are retained. Elo intervals use the requested logistic
model with draws as half points; the chain intervals include inherited Owl uncertainty.

The pool contains 50 original positions from common openings, four to eight moves in, screened to within 75 centipawns
by this engine's evaluation. Each 40-game anchor uses 20 positions, each once with each color. No opening book ships.

#### Scoring and test hooks

Completed acts record their result before the celebration delay. An unfinished award resumes exactly once after reload;
replays become Encores. Undo never decreases the move tally. The shell owns all stars, scores, initials and win cards.
Appending `?test` enables developer hooks and a separate `chess-test` storage namespace. Test positions cannot set the
normal game's best scores. Ordinary play has no hook object. A computer win is required for CPU awards; friend games,
draws and CPU losses never award them.

The cold review also reserves a computer win before its celebration delay. `awardComputer()` consumes it once,
including after reload or opening the Playbill. Puzzle wins retain their existing first-run/Encore policy.
Loss-card Undo now points to the actual handler. Terminal prompts say the result, and every programme dialog has a title.
Puzzle finishes now reuse the theatre's tipped king and spotlight, with static equivalents in calm motion.
`save()` ignores a wrong-try preview: its penalty is already stored, so refreshing during spring-back resumes the
last solved step instead of saving the temporary wrong board. The targeted reload regression lives in `review-cheats/`.
Closing the Playbill refreshes the prompt too, including a resumed puzzle step, pending reply or terminal result.
Restart is disabled on the opening Playbill until a game exists; thereafter it resets the current show immediately.
Review evidence is in `_scratch/chess/review-rules/`, `review-play/`, `review-final/` and `review-audit/`.

#### Engine changes wanted

- `kit/recess.js`, header comment: remove or escape the literal script and stylesheet HTML examples. The closing script
  tag terminates the inlined script, and the later CSS bundling pass replaces the comment's stylesheet example inside JS.
  `lib/recess-safe.min.js` omits that documentation line locally and uses the same shell runtime.
- `kit/recess.js`, `card()`: provide a focus trap and background inertness. Chess supplies these locally without changing the shell.
- `kit/recess.css`, `.rc-arr`: its initials arrows are 30 px tall. Chess raises them to 44 px locally; the shared shell should do this too.

#### Limits and sensitivity

No physical Chromebook was available. Desktop Chrome, the 375 px iframe and 390 px touch viewport were tested; slower-machine
timings in the report are estimates. The 1,000,000 search-nodes-per-second aspiration was not established by these checks.
Lion solves 44 of the 45 tactical positions. Its queen-first computer promotion policy misses ZrgCo's knight mate in two;
the puzzle itself accepts and requires the knight through its four-choice promotion fan, and was played successfully.
No human figures or cultural claims are shown. The final cover uses abstract chess tokens; an earlier human-looking king
was discarded and repainted. All final artwork is original generated gouache and card, with no painted text.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-09)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-09)
- 2026-11-25: handoff.md folded in (last changed 2026-11-09)
