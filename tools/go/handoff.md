# Go: build handoff

## Cold review fixes

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

## Build and play

From `S:\CurioClass-codex`:

```powershell
$env:CURIO_DRAFT = '1'
python _scratch/go/run.py 120 python scripts/bundle_tool.py go
```

Open `tools/go/go.html`. Everything needed to play is embedded. There is no server or network dependency.
Keep source edits in `src.html`; the scratch assembly scripts are a record of this build, not a required build system.
The final report gives the measured bundle size and qualification results.

## Contents

- The lamp-lit wooden table, board, bowls, eight painted stone sprites, ink wash, and shelf cover are in `art/`.
- The source contains the rules engine, inline Worker, 19 spec positions, printed lines, daily transforms, and all three modes.
- First stones 8 also accepts its two additional independently proven ladder branches; see the conflict decision below.
- `notes.md` is the grown-ups' note, with the game's Chinese, Japanese, and Korean roots and the area rules.
- `art/prompts.json` records all generated material assets and atlas derivatives. Raw generated PNGs remain in `art/raw/`.
- `../../_scratch/go/` contains the independent solver, rules differential tests, match logs, input tests, audit, look board, and frames.

## Engine changes wanted

1. `kit/recess.js`, header line 2: the literal closing-script example prematurely ends the script when the normal
   bundler inlines it. Escape that example or make `scripts/bundle_tool.py` escape closing-script sequences in JS.
   This build uses an inert canonical `kit:recess` marker and a byte-identical, UTF-8-decoded copy of the shell in
   `shellEncoded`. It calls the real Recess API. No shell behavior was reimplemented.
2. `kit/recess.js`, `initials()`, Save handler: add a one-use guard. Repeated activation of the same saved button
   could add duplicate entries. This game wraps that handler locally with a one-use guard, preserving the shell UI.

## Rules and opponents

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

## Verification map

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

## Sensitivity

The setup credits Go's beginnings in China and its names weiqi, igo, and baduk. The book credit identifies
Hayashi Genbi, Gokyo Shumyo, 1812, and the National Diet Library of Japan, with the original characters.
Art is a modern board, turned bowls, and a lamp-lit table. There are no themed costumes, temples, seals, calligraphy,
or invented cultural titles. The later cold review should check roots, wording, and attribution as the spec requests.

## Limits and accepted defaults

All grades; first visit opens First stones 1. Keep the weak 19x19 computer with its candid picker line.
Chinese and Korean classic problems remain a later pass, as the spec's accepted default says.
The life prover is a local corner AND-OR search with an immutable outside wall and a Benson terminal condition.
It proves the printed endpoints under that model, not all whole-board continuations or every alternate first move.
Puzzles follow the prescribed printed reply lines. No independent global minimum-move claim is made for book problems.
Chromebook hardware and human/club-player strength calibration were unavailable in this Windows build.
Replay and outside-program assistance remain the spec's accepted device-only limitations.

## Specification conflict resolved

The Recess brief says rejecting a valid second solution is a blocker. The spec says to accept only its listed line.
The independent solver found three valid 15-ply ladder captures in f8, including the listed one. White extends on its
last liberty in all three, exactly as specified. All three are accepted, with their compatible prefixes retained
through play and Undo. This is the unattended choice in favor of the brief's valid-play requirement; positions,
opponent replies, star cutoffs, and the canonical route remain intact. The solver evidence is
`../../_scratch/go/f8-valid-lines.json`. Book puzzles retain their prescribed replies; their alternate whole-board
continuations have not been exhaustively classified.
