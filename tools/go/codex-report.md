# Codex report: go (Recess)

## Built

Built in `S:\CurioClass-codex`, writing only `tools/go/` and `_scratch/go/`. Build only; no commits or polish round.
Three modes, 9/13/19 boards, five offline opponents, handicap, 19 puzzles, daily symmetry/color variations, agreed counting, Undo and instant restart.
Offline bundle: **1,395,248 bytes (1.33 MiB)**. Stage `built`; `recess: true`. No external HTML assets.
Uses the real Recess shell for controls, stars, scores, initials, daily seed, sound settings and win cards. No voice or lesson UI.
The shell header has an unsafe closing-script example; a byte-identical UTF-8 shell copy is loaded safely. Shared kit and shelf data were not edited.
No `voice/lines.json` was needed: bundler and audit both ran without it. `audit-states.json` covers the game modes and count.
Final bundle SHA-256: `7306483e9be4f06966fdb95a997f9fcdb29703376a5ea75d20b6b60eed9f5c3c`. Evidence and shared-file hashes: `../../_scratch/go/evidence.json`.

## Rules check

- PASS: corner 2 liberties and edge 3; orthogonal chains only.
- PASS: capture before suicide, including filling the last liberty while taking stones.
- PASS: two separate chains captured in one move.
- PASS: snapback captures more than one; it is not incorrectly rejected as ko.
- PASS: immediate ko retake rejected; retake after a threat and a pass is legal.
- PASS: positional superko hashes the stones after captures, using two 32-bit Zobrist words (64 bits).
- PASS: passes retain repetition history; two passes open counting.
- PASS: Undo restores stones, captures, hash history and ko ring in the actual UI.
- PASS: area counts stones and single-color enclosed empty regions, with no prisoner bonus; margins end in .5.
- PASS: 200-playout dead proposal; Benson-alive chains never marked. Friend needs both agreements; a toggle clears them.
- PASS: disputed live computer chains resume play with the kid to move; marks favoring White are accepted.
- PASS: all handicap sizes and standard placements, including 8 stones without center and 9 with it.
- PASS: 20,000 differential move checks against the independent rules implementation.

Evidence: `rules-results.json`, `browser-ko/results.json`, `browser-scores/results.json`, and `browser-final/results.json` in Scratch.

## Puzzles and levels

Every canonical line replayed legally in the independent solver and through the UI. All 11 book endpoints were proved alive by local AND-OR search with a Benson terminal.
The book proof assumes an immutable attacker wall outside the corner window. It is a local proof, not a proof of every whole-board alternative.
Counts below are kid placements on the stated route. No global minimum-move or move-based star cutoff is specified for book problems.
| Puzzle | Stated line | Stated/computed kid placements | Independent result |
|---|---|---:|---|
| f1 | `E4` | 1/1 | Capture; unique first move |
| f2 | `A4` | 1/1 | Capture; unique first move |
| f3 | `E4` | 1/1 | Capture; unique first move |
| f4 | `E4` | 1/1 | Unique escape to 3 liberties |
| f5 | `D2 pass C1` | 2/2 | Capture; unique first move |
| f6 | `B1` | 1/1 | Unique two-eye life |
| f7 | `H9` | 1/1 | Unique kill; forces capture in 7 plies |
| f8 | `E4 F5 G5 F4 F3 G4 H4 G3 G2 H3 H2 J3 J4 J2 J1` | 8/8 | Unique first move; 3 valid 15-ply branches |
| b01 | `T19` | 1/1 | Alive, depth 8 |
| b02 | `B19` | 1/1 | Alive, depth 10 |
| b03 | `A18 A16 B16` | 2/2 | Alive, depth 10 |
| b04 | `S2 R1 S1` | 2/2 | Alive, depth 10 |
| b05 | `B1 A2 B2` | 2/2 | Alive, depth 10 |
| b06 | `A2 A4 B1` | 2/2 | Alive, depth 8 |
| b07 | `T2 S1 T4 Q2 R1` | 3/3 | Alive, depth 4 |
| b08 | `B2 C1 B1 D1 C2` | 3/3 | Alive, depth 10 |
| b09 | `T3 S6 T5 S3 R3` | 3/3 | Alive, depth 6 |
| b10 | `A17 B19 B18 A14 C19 A16 A19 B17 B16` | 5/5 | Alive, depth 2 |
| b11 | `C17 C18 D17 E17 B18 D18 A18 B19 A12 A14 B14` | 6/6 | Alive, depth 8 |

Minimum forced captures were searched independently: f5 needs 2 kid placements; f8 needs 8. f7 is solved by the one-move killing shape, not by requiring its later physical capture.
**Brief/spec conflict:** the spec lists one f8 route, but the brief forbids rejecting a valid second solution. Two additional forced-extension captures were found and all three are accepted, including after Undo. Canonical play remains intact. See `f8-valid-lines.json` and `browser-branches/results.json`.
Stars checked: 3 for no miss/hint; 2 for 1-2 misses or first hint; 1 for more misses or second hint. Restart/reopen/Undo do not erase costs. All 176 book symmetry/color combinations replay legally, with correct colors and windows.
Evidence: `solver-results*.json`, `special-solver-results.json`, `browser-suite/results.json`, `browser-extra/results.json`.

## Computer opponent

All searches run in a Blob Worker with work and time budgets. The page watchdog can terminate the Worker at its ceiling and use the last legal best move; progress is sent every 40 ms. Replies are cached by full position/history and level.
| Level | How it plays | 9x9 target | Final empty-board search sample |
|---|---|---:|---:|
| Pebble | Noisy one-move heuristic; friendly mistakes | heuristic | 6.2 ms; visible turn at least 400 ms |
| Stream | Tactical heuristic, ladder reading, avoids self-atari | heuristic | 5.4 ms; visible turn at least 400 ms |
| Mountain | UCT, table priors, widening, kindness cap | 600 playouts | 456.0 ms / 600 playouts |
| Ridge | UCT to win; 3000 target on big boards | 4000 playouts | 1505.7 ms / 2040 playouts |
| Summit | Strongest UCT; 9x9 only | 30000 playouts | 5005.5 ms / 6279 playouts |

Final 13x13 samples: Mountain 504.7 ms, Ridge 2505.0 ms. Final 19x19: Mountain 500.8 ms, Ridge 4005.2 ms. Legal moves in all 13 offered size/level combinations; delivery overhead was under 6 ms.
Empty-board throughput samples: about 1254 playouts/s on 9x9 Summit, 479 on 13x13 Ridge, 148 on 19x19 Ridge. Ceilings can stop below the work target.
These measurements are Windows Chrome 156 on the available host, not a Chromebook measurement or a human playing rating.
| Browser pair, stronger first | Size | Wins | Result |
|---|---:|---:|---|
| pebble/random | 9 | 37/40 | PASS |
| stream/pebble | 9 | 33/40 | PASS |
| mountain/stream | 9 | 26/40 | PASS |
| ridge/mountain | 9 | 35/40 | PASS |
| summit/ridge | 9 | 17/20 | PASS |
| mountain/stream | 13 | 12/20 | PASS |
| ridge/mountain | 13 | 19/20 | PASS |

All **244 browser games ended by two passes**, colors alternating. Mountain won 24 kindness games against Pebble; median margin of the first 20 wins was **7.5**, below 25. PASS.
The separate actual-UI full games ended: Pebble White by 10.5; Stream White by 18.5; Mountain Black by 1.5; Ridge Black by 73.5; Summit White by 46.5. Win and loss paths both exercised.
Evidence: `qualification.json`, `browser-ladder/results.json`, `browser-games/results.json`, `browser-postfix/results.json`.

## Break it

- PASS: wrong tries and both hint caps survive restart/reopen; solved-then-Undo restores the attempt cost.
- PASS: random play loses to Pebble over the qualification set; pure passing loses and earns no score.
- PASS: a genuine 23.5-point win after 4 undos earns 1 star, no best and no initials prompt.
- PASS: handicap win by 30.5 earns 2 stars under its own `-h4` key; no mixing with even games.
- PASS: repeated Save on the same earned win now creates one entry. The first UI run exposed duplicates; the local shell-handler guard fixed them.
- PASS: same move after Undo gets the same CPU response; Summit Undo/mode switch cancels promptly, with no delayed timer harming the next mode.
- PASS: friend and daily send null scores; neither creates initials entries. Marking live White dead resumes play.
- PASS: restart restores the old board and ko history; switching modes dismisses the old-game toast.
- PASS: real 13/19 touch drag, tap-to-confirm and Place; illegal touch shows no ghost in board/loupe and explains liberties.
- PASS: full game through count and both agreements by real keyboard input; held chain and held capture clicks; resize stress.
- PASS: calm has no continuous motion; sound-off and grayscale frames inspected. No runtime network assets or requests after load.
One full audit ran, once, with 21 original leads. Its dispositions:
- Fixed focus loss after Play, puzzle/daily choice and count entry with `focus({preventScroll:true})`; first load still takes no focus.
- Fixed compact counting overflow: last control bottom 416 at 680x425; final desktop count bottom 762.66 at 1366x768.
- Fixed 760-wide puzzle chooser position: bottom 892 within the 900-high frame.
- Phone setup menus/about/help may scroll below the board, as the Recess spec explicitly requires. Optional help below the fold is intentional.
- Hidden Hint outside Puzzles is intentional. Missing voice logs are correct for Recess. Dropdown/mode shifts are expected.
The early immediate calm assertion and early desktop-count overflow remain in raw evidence; stable-state calm and focused final count checks supersede them. Audit was not rerun after fixes.

## Look board

The direction was obvious from the brief: tactile honey wood, slate, shell and one warm lamp. One direction, retained; no redraws. Real painted materials and these 1366x768 compositions preceded game logic (timestamps checked).
![Opening](../../_scratch/go/look/opening.png)
![In progress](../../_scratch/go/look/in-progress.png)
![Best moment](../../_scratch/go/look/best-moment.png)

## Grab check

Most satisfying: the final ladder capture washes eight stones away in a staggered ripple and fills the lid. The actual frame is `../../_scratch/go/references/best-real.png`.
Flattest: empty setup has no stones to animate. Painted light/grain/bowls keep it a physical table; Play is first. Dropdown chevrons, board padding and count layout were corrected during Build.
The table is visibly its own world beside both the shell demo and the digital classroom reference:
![Go beside the demo and Beat Lab](../../_scratch/go/grab-check.png)

## Class creep check

One search hit: the mandated Pebble picker line, "Just learned the rules. Makes friendly mistakes." Kept as specified. No standard codes, objectives, lesson card, welcome voice or classroom header.
Nominal palette contrasts recomputed: cream/room 15.31, cream/lit room 12.00, ink/board 6.40, ink/grain 4.74, river/board 4.99. Painted grayscale frame also inspected.

## Sources

- First stones f1-f8: original Curio Class positions in the spec, ours. The two extra f8 answer branches are independently solved from the same original position.
- [Gokyo Shumyo, National Diet Library pid 861157](https://dl.ndl.go.jp/pid/861157): 11 positions and answers transcribed in the spec from the 1898 edition. Live [IIIF metadata](https://dl.ndl.go.jp/api/iiif/861157/manifest.json) says **Access Restrictions: PDM** (Public Domain Mark), author 林元美, publisher 東生書店, date 1898. Raw metadata retained in Scratch. No scan images ship.
- Original book title, Hayashi Genbi and 1812 attribution follow the checked sources recorded in the spec; credit includes 碁経衆妙 and 林元美.
- [British Go Association rules comparison](https://www.britgo.org/rules/compare.html): area scoring, suicide prohibition, repetition and 7.5 extra points checked. Rules are not copyrightable; wording and engine are ours.
- [British Go Association history](https://www.britgo.org/intro/history): China, ancient references, weiqi and baduk checked; igo wording follows the spec. Modern art avoids cultural stereotypes.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Sounds and engine written for this game. No modern puzzle collection used.

## Done when

- PASS: every listed rules edge case, including actual-UI ko/Undo.
- PASS: suicide/ko lines, legal ghosts only, including large-board phone loupe.
- PASS: area marks, dead proposal/Benson exclusion, two friend agreements, disputed CPU marks, half-point margins.
- PASS: all 19 canonical puzzle routes, f5 pass, and all three proven f8 routes.
- FAIL literal single-route-only f8 wording: deliberately resolved in favor of the brief requiring valid alternatives to be accepted.
- PASS: seeded daily and 176 symmetry/color/window checks; null daily score.
- PASS on available host: responsive Worker searches and all size/level watchdog checks. FAIL to verify the named Chromebook hardware: none was available.
- PASS: all required browser ladder pairs and game counts, plus 24 kindness wins with median 7.5.
- PASS: two-move CPU Undo, undo costs and deterministic replay.
- PASS: real phone aim/confirm, complete keyboard friend game, desktop controls above fold.
- PASS: calm, sound off, shell key ownership, Ctrl+Z handler integration and no network dependencies.
- PASS: painted-first world/look board/cover, one offline file below 6 MB, all required build artifacts.

## Frames looked at

- All 3 pre-logic look frames; all 3 first-playable frames; all 12 required-size/calm/grayscale/capture frames.
- All 6 reference/capture/setup/classic frames; all 4 focused post-audit size/phone frames.
- All 18 audit PNGs, with `audit-contacts/0.png` and `1.png`; original leads checked against their frames.
- All 19 remaining browser/input PNGs via `final-contacts/checks-0.png` through `checks-2.png`, with phone/keyboard frames also opened individually.
- All 16 WebP assets via `final-contacts/art.png`, at game size in the UI; cover and raw material/sprite images inspected.

## Art made

7 painted originals, 8 derived stone cutouts and 1 board-material crop: **16 WebPs, 947,156 bytes**. Board surface and edge are one painted slab. Cover is 1200x750, no text. Alpha retained; no paid art CLI calls.
No remaining art placeholders. Code draws grid/marks/hit geometry and places painted sprites. Drops, ink wash, lid piles, lamp light and sounds honor shell settings.

## Shell changes wanted

1. Escape the literal closing-script example in the `kit/recess.js` header, or make the bundler escape it before inlining. Local safe-load workaround documented in handoff.
2. Add a one-use guard to `initials()` Save. Local guard is implemented without replacing the shell UI.
No shared file was changed.

## Left open

- Chromebook-specific speed and a human/club-player strength rating remain unverified; the local browser ladder is evidence of ordering, not a rating.
- Book proofs are local corner proofs; alternate whole-board continuations and global minimum moves were not exhaustively classified. The explicit f8 conflict is resolved above.
- Spec defaults retained unattended: all grades, weak 19x19 computer with candid wording, Chinese/Korean classics later, no extra people or themed props.
- Replaying a memorized win and using another program remain accepted device-only limitations. No accounts or network enforcement added.
- Cold Recess/sensitivity review and owner visual judgment are next; no review/polish or publication was started. All owned Chrome instances and the host were closed.
