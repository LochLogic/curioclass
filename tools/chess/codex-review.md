# Codex review: chess

## Played

Reviewed cold as a Grade 3 solo player and an adult, against CODEX-RECESS.md, GAMES.md and the chess spec.
Played the opening, friend checkmate, illegal input, takebacks, a puzzle, a computer reply and the daily before reading the builder's notes/source.
Then completed all nine acts, daily/Encore, keyboard and touch games, and a full game against every puppet.
The theatre grabs attention; readable paper pieces, warm light, puppets and folding captures remain strong.
The computer-game harness used dev-only Stockfish for human moves and the game's real browser workers for opponents.
Mouse, Rabbit, Fox, Owl, Badger and Raven lost; Lion drew by repetition. No referee or external engine ships.

## Findings fixed

- **blocker, general, rebuild/startup:** the required ordinary bundler broke the shell's HTML-example comment, leaving a blank playbill. A tool-local copy omits only that documentation line; the shell runtime is identical. Plain bundling now works. Kit/scripts untouched.
- **blocker, family:chess, computer award:** opening Playbill or reloading during the win delay could discard earned stars. Reserve the result before the delay and consume it once on celebration, Playbill or reload.
- **should fix, family:chess, loss card:** a boolean argument shadowed `undo`, making "Take back a few moves" dead. Renamed it and restored the real handler; loss Undo reopens play.
- **should fix, family:chess, wrong-try reload:** pagehide saved the temporary wrong board, losing the last solved step. Keep the already-saved playable position and penalty until spring-back completes. Reload now retains both step and tally.
- **should fix, general, results/resume:** the background still announced a turn after checkmate or kept the opening prompt after resume; result/Encore dialogs also lacked their referenced title. Refresh prompts on return, show the terminal result and give every programme heading its dialog ID.
- **should fix, general, opening Restart:** the audit confirmed a dead Restart before any game existed. Disable it until a show starts; keep it live during play.
- **polish, family:chess, puzzle finish:** the flattest payoff was a generic line and burst. Reuse the theatre's tipped king and narrowing spotlight, gild the final move, and name the actual finish. Calm keeps the static picture; the next puzzle keeps its existing timing.

## Findings left

No reproduced blocker or should-fix remains. Hardware/strength limits and accepted external assistance are listed below.
No lesson header, narration, lesson cards or standard codes were added. The grown-up note keeps the Recess spec's format.

## Break it

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

## Voice walk

Not applicable by the Recess brief: there is no narration or Read control. Walked Playbill, friend, computer, puzzles and daily with game sounds; checked mute. The shell owns sound controls.

## Facts checked

- Moves/endings: FIDE rules as specified in `spec.md`, independently checked with python-chess and the published perft positions; Recess's automatic repetition/fifty-move policy is intentional.
- Puzzle IDs, positions, lines and CC0 credit: exact spec/Lichess records; no new dataset fetched. Both OxJo0 mates and ZrgCo's knight promotion were checked.
- Strength claims: inspected the existing 440 anchor-game records, checked grouping/duplicates, and confirmed the engine is unchanged. The builder's Lion estimate is an engine comparison, not a human rating. No new Elo calibration is claimed.
- Privacy wording matches the local-storage-only implementation. Class-creep search finds only Mouse's required "learned how the pieces move" description.

## Sensitivity

None identified: original animal puppets and abstract classic pieces; no people, historical narrative or cultural-origin claims. No new art or sensitive content was introduced.

## Flattest moment left

The longer puppet strength descriptions remain text-heavy. Kept the spec's plain descriptions so choosing a level is honest and clear.

## Graphics

Kept all six painted assets; inspected the 12-piece and 14-pose atlases on the actual dark background, cover, stage, board and programme paper. No repaint was needed.
Inspected every review/audit frame via contact sheets and opened the phone, compact picker, capture and mate details. Checked all STANDARDS sizes, 390x844, calm, mute and grayscale.
Compared the current theatre with the existing shell-demo and Beat Lab frames. It owns a distinct physical world.
Best revised frame: `../../_scratch/chess/review-final/puzzle-finish-motion.png`; phone/calm counterparts are beside it. Bundle: 1,424,185 bytes, below 6 MB.

## Audit

Completed the single audit: 19 leads, 57 frames; no runtime exceptions, resize locks or infinite calm motion.
Fixed its dead opening Restart. The other 18 leads were 8 lesson-hint/Read assumptions, 8 intentional modal-entry focus reports, and 2 checkbox-box measurements. Recess uses #prompt without narration; the Playbill has keyboard focus/background inertness; the checkbox has a tested clickable 44 px-high label, including outside its drawn box.
Inspected all 57 audit frames in `../../_scratch/chess/review-audit-contacts/`. The audit was not rerun. Final small save/resume and Restart corrections received targeted current-bundle regressions and new frames. Audit: `../../_scratch/chess/review-audit/audit.md`.

## Left open

- No physical Chromebook was available. Desktop checks do not prove caps on actual school hardware.
- Retained the builder's documented calibration uncertainty, machine-speed limitation and queen-first computer promotion policy. The policy misses a knight mate in two in the tactical suite; puzzle promotion is correct and the spec requires queen unless knight mates immediately.
- External-engine help and deliberate local-storage editing cannot be prevented in an offline device-only game; these are accepted scope limits, not new reward paths.
- First parallel game batch timed out taking Badger's screenshot after six completed games. Retried Badger alone: full game finished in 36.81 s, longest observed think 0.516 s. Its result is saved before screenshotting.
- Unattended choices followed the brief/spec defaults; no questions, commits, shared-kit changes, publication or second review round. All writes stayed in `tools/chess/` and `_scratch/chess/`; bounded commands used only the named ports.
