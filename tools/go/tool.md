# Go: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: go (Recess)

#### Built

Built in `S:\CurioClass-codex`, writing only `tools/go/` and `_scratch/go/`. Build only; no commits or polish round.
Three modes, 9/13/19 boards, five offline opponents, handicap, 19 puzzles, daily symmetry/color variations, agreed counting, Undo and instant restart.
Offline bundle: **1,395,248 bytes (1.33 MiB)**. Stage `built`; `recess: true`. No external HTML assets.
Uses the real Recess shell for controls, stars, scores, initials, daily seed, sound settings and win cards. No voice or lesson UI.
The shell header has an unsafe closing-script example; a byte-identical UTF-8 shell copy is loaded safely. Shared kit and shelf data were not edited.
No `voice/lines.json` was needed: bundler and audit both ran without it. `audit-states.json` covers the game modes and count.
Final bundle SHA-256: `7306483e9be4f06966fdb95a997f9fcdb29703376a5ea75d20b6b60eed9f5c3c`. Evidence and shared-file hashes: `../../_scratch/go/evidence.json`.

#### Rules check

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

#### Puzzles and levels

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

#### Computer opponent

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

#### Break it

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

#### Look board

The direction was obvious from the brief: tactile honey wood, slate, shell and one warm lamp. One direction, retained; no redraws. Real painted materials and these 1366x768 compositions preceded game logic (timestamps checked).
![Opening](../../_scratch/go/look/opening.png)
![In progress](../../_scratch/go/look/in-progress.png)
![Best moment](../../_scratch/go/look/best-moment.png)

#### Grab check

Most satisfying: the final ladder capture washes eight stones away in a staggered ripple and fills the lid. The actual frame is `../../_scratch/go/references/best-real.png`.
Flattest: empty setup has no stones to animate. Painted light/grain/bowls keep it a physical table; Play is first. Dropdown chevrons, board padding and count layout were corrected during Build.
The table is visibly its own world beside both the shell demo and the digital classroom reference:
![Go beside the demo and Beat Lab](../../_scratch/go/grab-check.png)

#### Class creep check

One search hit: the mandated Pebble picker line, "Just learned the rules. Makes friendly mistakes." Kept as specified. No standard codes, objectives, lesson card, welcome voice or classroom header.
Nominal palette contrasts recomputed: cream/room 15.31, cream/lit room 12.00, ink/board 6.40, ink/grain 4.74, river/board 4.99. Painted grayscale frame also inspected.

#### Sources

- First stones f1-f8: original Curio Class positions in the spec, ours. The two extra f8 answer branches are independently solved from the same original position.
- [Gokyo Shumyo, National Diet Library pid 861157](https://dl.ndl.go.jp/pid/861157): 11 positions and answers transcribed in the spec from the 1898 edition. Live [IIIF metadata](https://dl.ndl.go.jp/api/iiif/861157/manifest.json) says **Access Restrictions: PDM** (Public Domain Mark), author 林元美, publisher 東生書店, date 1898. Raw metadata retained in Scratch. No scan images ship.
- Original book title, Hayashi Genbi and 1812 attribution follow the checked sources recorded in the spec; credit includes 碁経衆妙 and 林元美.
- [British Go Association rules comparison](https://www.britgo.org/rules/compare.html): area scoring, suicide prohibition, repetition and 7.5 extra points checked. Rules are not copyrightable; wording and engine are ours.
- [British Go Association history](https://www.britgo.org/intro/history): China, ancient references, weiqi and baduk checked; igo wording follows the spec. Modern art avoids cultural stereotypes.
- Illustrations generated with OpenAI gpt-image, edited for Curio Class. Sounds and engine written for this game. No modern puzzle collection used.

#### Done when

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

#### Frames looked at

- All 3 pre-logic look frames; all 3 first-playable frames; all 12 required-size/calm/grayscale/capture frames.
- All 6 reference/capture/setup/classic frames; all 4 focused post-audit size/phone frames.
- All 18 audit PNGs, with `audit-contacts/0.png` and `1.png`; original leads checked against their frames.
- All 19 remaining browser/input PNGs via `final-contacts/checks-0.png` through `checks-2.png`, with phone/keyboard frames also opened individually.
- All 16 WebP assets via `final-contacts/art.png`, at game size in the UI; cover and raw material/sprite images inspected.

#### Art made

7 painted originals, 8 derived stone cutouts and 1 board-material crop: **16 WebPs, 947,156 bytes**. Board surface and edge are one painted slab. Cover is 1200x750, no text. Alpha retained; no paid art CLI calls.
No remaining art placeholders. Code draws grid/marks/hit geometry and places painted sprites. Drops, ink wash, lid piles, lamp light and sounds honor shell settings.

#### Shell changes wanted

1. Escape the literal closing-script example in the `kit/recess.js` header, or make the bundler escape it before inlining. Local safe-load workaround documented in handoff.
2. Add a one-use guard to `initials()` Save. Local guard is implemented without replacing the shell UI.
No shared file was changed.

#### Left open

- Chromebook-specific speed and a human/club-player strength rating remain unverified; the local browser ladder is evidence of ordering, not a rating.
- Book proofs are local corner proofs; alternate whole-board continuations and global minimum moves were not exhaustively classified. The explicit f8 conflict is resolved above.
- Spec defaults retained unattended: all grades, weak 19x19 computer with candid wording, Chinese/Korean classics later, no extra people or themed props.
- Replaying a memorized win and using another program remain accepted device-only limitations. No accounts or network enforcement added.
- Cold Recess/sensitivity review and owner visual judgment are next; no review/polish or publication was started. All owned Chrome instances and the host were closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: go

#### Played

Cold play preceded reading the builder report, handoff, notes or source. Judged against CODEX-RECESS.md, GAMES.md and spec.md.
Tried the opening as a young solo player: one tap captures, the painted table grabs, and the next action is clear. Then played adult-style tactical games, all puzzles, daily and friend counting.
Full 9x9 games against every level ended by two passes: Pebble Black by 11.5 (82 moves), Stream White by 4.5 (84), Mountain White by 6.5 (96), Ridge White by 12.5 (112), Summit White by 6.5 (89).
This was automated browser play, not a human strength rating. A second Pebble game rechecked the Save fix.
All 13 offered size/level combinations returned legal replies with the main thread ticking; visible replies: gentle 0.42-0.54 s, Ridge 1.53/2.51/4.03 s, Summit 5.03 s, including the minimum turn pause and delivery overhead.

#### Findings fixed

- Blocker [family:go], `cancel`: switching modes during a wrong puzzle animation permanently blocked new moves. Clear wrong/hold/aim state and pending timers. Reproduced before, passes after.
- Blocker [family:go], `undo`: count-stage Undo was free against the computer. Every actual computer Undo now counts toward stars and score eligibility; count still undoes only the last pass.
- Blocker [general], initials: same-task clicks on the newly created or detached Save button could duplicate an earned entry before the observer guarded it. A synchronous capture guard closes the race; spam now saves once.
- Should fix [family:go], pointer input: the exact right/bottom grid boundary missed clicks. Listen over the painted board margin; an actual final-corner ladder capture now works, with phone aim rechecked.
- Should fix [family:go], Restart restore: interrupted counting could skip the dead proposal and say it was a move. Resume the pending proposal and restore count/result wording.
- Should fix [family:go], `proposal`: the final timed rollout contributed ownership but was omitted from the denominator. Count every completed rollout; one-run and 200-run checks pass and Benson-alive stones stay protected.
- Should fix [family:go], Undo guidance: the largest lost group survived Undo incorrectly. Snapshot and restore it with the board.
- Should fix [family:go], escape/kill puzzles: wrong hints and identical "A living shape" results contradicted the goal. Match the goal, show escape liberties and light the decisive stone with a soft ring.
- Should fix [general], shell cards: global hover styles made dark labels unreadable. Scope hover and restore light card buttons; normal/hover contrast is legible.
- Should fix [general], access: name shell dialogs from their heading, keep Tab inside them, put gridcells in rows, and clear cancelled touch aims. Real keyboard and touch checks pass.
- Should fix [general], notes: removed an unmeasured claim about adult strength and qualified the statement about playing inside settled own area.

#### Findings left

No confirmed blocker or should-fix remains. Verification limits and shared-shell requests are named below.

#### Break it

- Rules PASS: corner/edge liberties, capture before suicide, two-chain capture, snapback, ko/threat/answer, positional superko after captures, pass history, area/neutral points and handicap arrangements. Independently compared 18,000 random move attempts across 9/13/19.
- Puzzles PASS: all 19 canonical routes and all 21 accepted routes through the UI, including f5's pass and the three valid f8 branches. Fresh re-run of the existing array-copy local prover confirmed all 11 book endpoints alive; this is a bounded corner proof, not exhaustive whole-board uniqueness.
- Daily PASS: all 176 symmetry/color combinations replay legally. Cold daily used the date-seeded corner; no score or initials are awarded.
- Stars PASS: 0/1/2/3 misses give 3/2/2/1; first/second hint cap at 2/1. Fifty rapid wrong inputs count one blocked attempt; restart, reentry and Undo retain costs.
- Computer rewards PASS: four actual Undos give one star, null best and no initials on a winning count fixture. Handicap fixture gives two stars and 26.5 only under `cpu-9-pebble-h4`. An even fixture gives three stars; repeated/detached Save gives one entry.
- Count PASS: one friend agreement does not finish; a dead mark clears both; both finish with no best. Marking a live two-eye White group dead resumes play with Black, with no reward. Pending-count restart/restore re-proposes.
- Abuse PASS: pass-only game ends White by 88.5 and earns nothing; cancelled puzzle replies/wins do not enter another mode; Summit Undo/mode cancellation and replay are safe and deterministic in the tested positions. Puzzle and count restart paths also pass.
- Input PASS: real 13/19 phone drags, Place, suicide, cancel; real U/Ctrl+Z/M/P, keyboard friend completion and dialog Tab cycle; resize during Summit and during an eight-stone capture. Zero game exceptions or remote requests in these runs.
- Prior ladder logs were independently recounted, not rerun: 9x9 stronger-level wins 37/40, 33/40, 26/40, 35/40, 17/20; 13x13 12/20 and 19/20. All 244 logged games, including 24 kindness games, ended by passes; first 20 Mountain win margins have median 7.5.
- Evidence: `../../_scratch/go/review-rules-results.json`, `review-proof-results.json`, `review-full-suite-results.json`, `review-rewards-results.json`, `review-input/results.json`, `review-prior-qualification.json`. Early failing evidence remains; focused passes supersede the fixed leads.

#### Voice walk

No voice, Read, classroom header or lesson flow belongs in this Recess game. None was added. Main path: opening capture, next puzzles, daily, computer setup/play/Undo, friend play/two passes/both agreements.
Class-creep search found only the mandated Pebble line, "Just learned the rules. Makes friendly mistakes." No standards or lesson UI.

#### Facts checked

- China, age over 2,500 years and names weiqi/igo/baduk: [British Go Association history](https://www.britgo.org/intro/history) and [About Go](https://www.britgo.org/whatisgo).
- Area counting, no suicide, 7.5 even-game compensation, 6.5 Japanese/Korean compensation and positional superko meaning: [BGA rules comparison](https://www.britgo.org/rules/compare.html). The 0.5 handicap value remains the spec's stated house rule.
- Hayashi Genbi and the 1812 edition: [NII/CiNii bibliographic record BB25936291](https://ci.nii.ac.jp/ncid/BB25936291), including its publication colophon. [NDL manifest](https://dl.ndl.go.jp/api/iiif/861157/manifest.json) freshly fetched: author 林元美, scanned edition 1898, Access Restrictions PDM. No scan images ship.
- Notes now describe settled-area play accurately. The spec's broader claim that filling a neutral point never changes area score is false; the engine correctly gives that point to its stone's owner. Spec left untouched.

#### Sensitivity

Fresh review of Chinese roots, Japanese and Korean names, author credit and all 16 painted assets found no stereotype or misattribution. Plain modern board/bowls, no people or themed cultural props. The Japanese-only classic selection is acknowledged; Chinese/Korean classics remain a later pass per the accepted spec default.

#### Flattest moment left

The empty setup is naturally still, but its painted light, board and bowls hold the scene. The formerly flat escape/kill finishes now answer with goal-specific text, a decisive-stone glow and, for escape, the three liberties. Kept the strongest moment: eight stones wash off and fill the lid.

#### Graphics

Kept all existing painted assets; no missing art or code-drawn object required repainting. Looked at all 16 via `review-contacts/art.png`, the cover full size, and their real on-screen uses.
Inspected every STANDARDS size plus 390x844, calm, sound off and grayscale; phone help/setup may scroll as the Recess spec requires. Normal and hover shell buttons stay legible.
Compared actual Go capture with fresh `review-input/reference-shell.png` and `reference-classroom.png` (Beat Lab): this is its own physical world.
Frames: `review-cold/`, `review-probe/`, all 12 `review-sizes/` frames and all seven `review-input/` frames, with contact sheets in `review-contacts/`. Audit frames/dispositions below.
Final offline bundle: 1,398,421 bytes (1,365.6 KiB), under the Recess 6 MB cap. No art removed.

#### Audit

Completed once, last, using `scripts/audit_tool.py` through the bounded Scratch wrapper `review_audit.py`: Chrome 9961, host 8765, 40-minute ceiling. Report: `../../_scratch/go/review-audit/audit.md`.
All 18 audit PNGs inspected in five contact sheets, with both count sizes opened full size. Ten leads, all confirmed as intended Recess behavior:
- Four "Hint out of view" state leads: Hint is intentionally hidden in Computer/Friend/count, because it belongs only to puzzles.
- Four phone setup leads: opponent/head start and the two help disclosures are below the board, per the specified scroll order.
- Two first-screen leads: optional "At the table" help scrolls below the fold at 760/375, while the board and frequent controls remain available.
All other size checks clean; no endless calm animation, exceptions, stuck controls, lost focus, or failed settled Enter path. No product fix was required by the audit. No second audit was run.

#### Left open

- No Chromebook hardware or human rating was available. Timings are Windows Chrome 156; this pass did not rerun the complete 244-game qualification ladder.
- Book alternatives beyond the accepted routes are not exhaustively classified. The brief's valid-second-solution rule wins over literal single-route-only wording; all three existing f8 routes are retained.
- Shared shell header escaping and the general initials guard still belong upstream as documented in handoff; local workarounds are present. No shared files edited.
- Unattended defaults kept: all grades, weak 19x19 with candid wording, later Chinese/Korean classics, no new modes. Notes retain the Recess grown-ups format, not lesson headings.
- Initial read-only document reads predated the hard-timeout wrapper; all build/play/proof/audit commands were bounded. Browser startup was slow but completed; an initial host favicon 404 was confined to the test wrapper and corrected there.
- Written only under `tools/go/` and `_scratch/go/`; no commits. All review-owned Chrome instances and servers were closed before this report.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Go: build handoff

#### Cold review fixes

The cold review kept the painted table, stones, bowls, ink capture and puzzle routes. Changes in `src.html`:
- Cancel clears wrong-move, hold and touch state, so switching modes during a wrong try cannot lock play.
- Pointer input covers the painted board margin, giving edge and corner intersections their full hit area.
- Every computer Undo, including the last pass at counting, increments the undo cost. Loss guidance is snapshotted too.
- Restart restore resumes an unfinished count proposal and restores the count/result status.
- Time-limited ownership proposals include every completed rollout in their denominator.
- Escape and kill puzzles have matching hints/results and an outcome ring; escape shows its three liberties.
- Shell card hover/contrast stays legible; cards have a heading label and keep Tab focus. Grid points belong to rows.
- Initials Save is guarded synchronously on capture as well as by observation, including same-task/detached-button spam.

The review evidence lives in `../../_scratch/go/review-*`. `codex-review.md` is written only after the final audit.
The grown-ups' note now describes Summit without an unmeasured human rating and qualifies the settled-area scoring statement.

Build only. Source: `src.html`. Offline bundle: `go.html`. Shelf metadata: `tool.draft.json`, stage `built`, Recess enabled.
No shared files were edited and no git commands or commits were made.

#### Build and play

From `S:\CurioClass-codex`:

```powershell
$env:CURIO_DRAFT = '1'
python _scratch/go/run.py 120 python scripts/bundle_tool.py go
```

Open `tools/go/go.html`. Everything needed to play is embedded. There is no server or network dependency.
Keep source edits in `src.html`; the scratch assembly scripts are a record of this build, not a required build system.
The final report gives the measured bundle size and qualification results.

#### Contents

- The lamp-lit wooden table, board, bowls, eight painted stone sprites, ink wash, and shelf cover are in `art/`.
- The source contains the rules engine, inline Worker, 19 spec positions, printed lines, daily transforms, and all three modes.
- First stones 8 also accepts its two additional independently proven ladder branches; see the conflict decision below.
- `notes.md` is the grown-ups' note, with the game's Chinese, Japanese, and Korean roots and the area rules.
- `art/prompts.json` records all generated material assets and atlas derivatives. Raw generated PNGs remain in `art/raw/`.
- `../../_scratch/go/` contains the independent solver, rules differential tests, match logs, input tests, audit, look board, and frames.

#### Engine changes wanted

1. `kit/recess.js`, header line 2: the literal closing-script example prematurely ends the script when the normal
   bundler inlines it. Escape that example or make `scripts/bundle_tool.py` escape closing-script sequences in JS.
   This build uses an inert canonical `kit:recess` marker and a byte-identical, UTF-8-decoded copy of the shell in
   `shellEncoded`. It calls the real Recess API. No shell behavior was reimplemented.
2. `kit/recess.js`, `initials()`, Save handler: add a one-use guard. Repeated activation of the same saved button
   could add duplicate entries. This game wraps that handler locally with a one-use guard, preserving the shell UI.

#### Rules and opponents

Positional superko uses a pair of independent 32-bit Zobrist words, serialized as 16 hex digits: 64 bits total,
stones only. Captures precede the suicide and repetition checks. Passing retains history. Undo restores snapshots.
Counting uses area plus 7.5, or 0.5 in handicap games. Dead-chain proposals use 200 light playouts and exclude
Benson-alive chains. Marking live White stones dead makes the computer resume play.

Every opponent search is in a Blob Worker. Node/playout budgets and elapsed-time ceilings are both present.
The page also owns a watchdog: the Worker sends its current best move every 40 ms; at the ceiling it is terminated
and the best legal move received is used. Cancelled timers cannot terminate a subsequent search.
Mountain's progress choices apply the same kindness cap as its final choice. Replies are cached per full game
position/history and level so Undo and replay cannot fish for another answer.

The browser core-engine ladder and the actual UI games have separate evidence. Raw search timings include an
iteration finishing after its loop deadline; the final page watchdog closes that overrun. The targeted final
watchdog test covers every offered size/level combination. No numerical human playing rating was established.

#### Verification map

- `../../_scratch/go/rules-results.json`: edge cases and 20,000 differential move checks.
- `../../_scratch/go/solver-results.json`, `solver-results-b02.json`, `solver-results-b03.json`,
  `solver-results-b05.json`, `special-solver-results.json`: independent local proofs and printed-line replay.
- `../../_scratch/go/browser-ladder/results.json`: browser self-play, colors alternating, full configured budgets.
- `../../_scratch/go/browser-games/results.json`: full UI games against all five computer levels.
- `../../_scratch/go/browser-scores/results.json`: four-undo win, handicap cap, repeated Save, pass spam, dead-chain dispute.
- `../../_scratch/go/interactions/results.json`: real touch aiming/confirmation, full keyboard game, held click and capture.
- `../../_scratch/go/browser-suite/results.json`: every puzzle, daily, attempts, Undo, agreement, and cancellation.
- `../../_scratch/go/browser-extra/results.json`: 176 transformed book-line replays, hint caps, and final calm check.
- `../../_scratch/go/browser-postfix/results.json`: audit focus fixes and final search watchdog timing.
- `../../_scratch/go/audit/audit.md`: one complete audit. Its 21 original leads are dispositioned in the final report;
  focused follow-up frames show fixes, without rerunning the audit.
- `../../_scratch/go/grab-check.png`: Go beside the Recess demo and Beat Lab.

#### Sensitivity

The setup credits Go's beginnings in China and its names weiqi, igo, and baduk. The book credit identifies
Hayashi Genbi, Gokyo Shumyo, 1812, and the National Diet Library of Japan, with the original characters.
Art is a modern board, turned bowls, and a lamp-lit table. There are no themed costumes, temples, seals, calligraphy,
or invented cultural titles. The later cold review should check roots, wording, and attribution as the spec requests.

#### Limits and accepted defaults

All grades; first visit opens First stones 1. Keep the weak 19x19 computer with its candid picker line.
Chinese and Korean classic problems remain a later pass, as the spec's accepted default says.
The life prover is a local corner AND-OR search with an immutable outside wall and a Benson terminal condition.
It proves the printed endpoints under that model, not all whole-board continuations or every alternate first move.
Puzzles follow the prescribed printed reply lines. No independent global minimum-move claim is made for book problems.
Chromebook hardware and human/club-player strength calibration were unavailable in this Windows build.
Replay and outside-program assistance remain the spec's accepted device-only limitations.

#### Specification conflict resolved

The Recess brief says rejecting a valid second solution is a blocker. The spec says to accept only its listed line.
The independent solver found three valid 15-ply ladder captures in f8, including the listed one. White extends on its
last liberty in all three, exactly as specified. All three are accepted, with their compatible prefixes retained
through play and Undo. This is the unattended choice in favor of the brief's valid-play requirement; positions,
opponent replies, star cutoffs, and the canonical route remain intact. The solver evidence is
`../../_scratch/go/f8-valid-lines.json`. Book puzzles retain their prescribed replies; their alternate whole-board
continuations have not been exhaustively classified.

#### Live early

Live early for Cory to see, 2026-11-12, process not exempted. tool.draft.json was renamed to tool.json only so the site lists the game; Refine, Exit check, Art and voice, Finish check and Sign-off are still owed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-10)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-10)
- 2026-11-25: handoff.md folded in (last changed 2026-11-11)
