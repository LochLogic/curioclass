# Chess build handoff

Open [chess.html](chess.html) for the complete offline game. [src.html](src.html) is the readable source.
The shelf remains unchanged and this is a Build-only draft. No commit, publication or polish round was started.

## What is here

- `src.html`: all rules, search, 45 puzzles, rendering, motion, sound and persistence; shared Recess shell and stylesheet.
- `lib/recess-safe.min.js`: the shared shell verbatim except its bundler-directive documentation line is omitted.
- `chess.html`: generated offline file, approximately 1.36 MiB including the shell and painted assets.
- `tool.draft.json`: built Recess metadata and sources; `notes.md`: parent and teacher note.
- `art/`: painted theatre, board material, 12-piece atlas, 14-pose puppet atlas, programme paper and 1200x750 cover.
- `audit-states.json`: real-input paths for the playbill, friend, computer, puzzles and daily.
- `codex-report.md`: final results, settings, all 45 solver checks, artwork and remaining limits.

## Rebuild

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

## Evidence map

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

## Computer settings and calibration

Seven levels share one engine and legal-move generator. Raven and Lion differ only in node budget and the specified
opening-choice margin; they receive no score noise or deliberate blunders. Final Lion uses 25,000 nodes and Raven 12,000.
Every search is in a Blob worker. Undo and leaving the game terminate it immediately. The minimum visible think is 500 ms.

Stockfish 19 is a development-only executable in Scratch. Nothing from it, including weights, ships. Fixed Stockfish
times were selected from measured pilot means on this computer, rounded to milliseconds. The final means differ under
parallel batch load; all settings, scores, openings and timings are retained. Elo intervals use the requested logistic
model with draws as half points; the chain intervals include inherited Owl uncertainty.

The pool contains 50 original positions from common openings, four to eight moves in, screened to within 75 centipawns
by this engine's evaluation. Each 40-game anchor uses 20 positions, each once with each color. No opening book ships.

## Scoring and test hooks

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

## Engine changes wanted

- `kit/recess.js`, header comment: remove or escape the literal script and stylesheet HTML examples. The closing script
  tag terminates the inlined script, and the later CSS bundling pass replaces the comment's stylesheet example inside JS.
  `lib/recess-safe.min.js` omits that documentation line locally and uses the same shell runtime.
- `kit/recess.js`, `card()`: provide a focus trap and background inertness. Chess supplies these locally without changing the shell.
- `kit/recess.css`, `.rc-arr`: its initials arrows are 30 px tall. Chess raises them to 44 px locally; the shared shell should do this too.

## Limits and sensitivity

No physical Chromebook was available. Desktop Chrome, the 375 px iframe and 390 px touch viewport were tested; slower-machine
timings in the report are estimates. The 1,000,000 search-nodes-per-second aspiration was not established by these checks.
Lion solves 44 of the 45 tactical positions. Its queen-first computer promotion policy misses ZrgCo's knight mate in two;
the puzzle itself accepts and requires the knight through its four-choice promotion fan, and was played successfully.
No human figures or cultural claims are shown. The final cover uses abstract chess tokens; an earlier human-looking king
was discarded and repainted. All final artwork is original generated gouache and card, with no painted text.
