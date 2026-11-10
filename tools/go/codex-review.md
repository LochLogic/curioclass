# Codex review: go

## Played

Cold play preceded reading the builder report, handoff, notes or source. Judged against CODEX-RECESS.md, GAMES.md and spec.md.
Tried the opening as a young solo player: one tap captures, the painted table grabs, and the next action is clear. Then played adult-style tactical games, all puzzles, daily and friend counting.
Full 9x9 games against every level ended by two passes: Pebble Black by 11.5 (82 moves), Stream White by 4.5 (84), Mountain White by 6.5 (96), Ridge White by 12.5 (112), Summit White by 6.5 (89).
This was automated browser play, not a human strength rating. A second Pebble game rechecked the Save fix.
All 13 offered size/level combinations returned legal replies with the main thread ticking; visible replies: gentle 0.42-0.54 s, Ridge 1.53/2.51/4.03 s, Summit 5.03 s, including the minimum turn pause and delivery overhead.

## Findings fixed

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

## Findings left

No confirmed blocker or should-fix remains. Verification limits and shared-shell requests are named below.

## Break it

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

## Voice walk

No voice, Read, classroom header or lesson flow belongs in this Recess game. None was added. Main path: opening capture, next puzzles, daily, computer setup/play/Undo, friend play/two passes/both agreements.
Class-creep search found only the mandated Pebble line, "Just learned the rules. Makes friendly mistakes." No standards or lesson UI.

## Facts checked

- China, age over 2,500 years and names weiqi/igo/baduk: [British Go Association history](https://www.britgo.org/intro/history) and [About Go](https://www.britgo.org/whatisgo).
- Area counting, no suicide, 7.5 even-game compensation, 6.5 Japanese/Korean compensation and positional superko meaning: [BGA rules comparison](https://www.britgo.org/rules/compare.html). The 0.5 handicap value remains the spec's stated house rule.
- Hayashi Genbi and the 1812 edition: [NII/CiNii bibliographic record BB25936291](https://ci.nii.ac.jp/ncid/BB25936291), including its publication colophon. [NDL manifest](https://dl.ndl.go.jp/api/iiif/861157/manifest.json) freshly fetched: author 林元美, scanned edition 1898, Access Restrictions PDM. No scan images ship.
- Notes now describe settled-area play accurately. The spec's broader claim that filling a neutral point never changes area score is false; the engine correctly gives that point to its stone's owner. Spec left untouched.

## Sensitivity

Fresh review of Chinese roots, Japanese and Korean names, author credit and all 16 painted assets found no stereotype or misattribution. Plain modern board/bowls, no people or themed cultural props. The Japanese-only classic selection is acknowledged; Chinese/Korean classics remain a later pass per the accepted spec default.

## Flattest moment left

The empty setup is naturally still, but its painted light, board and bowls hold the scene. The formerly flat escape/kill finishes now answer with goal-specific text, a decisive-stone glow and, for escape, the three liberties. Kept the strongest moment: eight stones wash off and fill the lid.

## Graphics

Kept all existing painted assets; no missing art or code-drawn object required repainting. Looked at all 16 via `review-contacts/art.png`, the cover full size, and their real on-screen uses.
Inspected every STANDARDS size plus 390x844, calm, sound off and grayscale; phone help/setup may scroll as the Recess spec requires. Normal and hover shell buttons stay legible.
Compared actual Go capture with fresh `review-input/reference-shell.png` and `reference-classroom.png` (Beat Lab): this is its own physical world.
Frames: `review-cold/`, `review-probe/`, all 12 `review-sizes/` frames and all seven `review-input/` frames, with contact sheets in `review-contacts/`. Audit frames/dispositions below.
Final offline bundle: 1,398,421 bytes (1,365.6 KiB), under the Recess 6 MB cap. No art removed.

## Audit

Completed once, last, using `scripts/audit_tool.py` through the bounded Scratch wrapper `review_audit.py`: Chrome 9961, host 8765, 40-minute ceiling. Report: `../../_scratch/go/review-audit/audit.md`.
All 18 audit PNGs inspected in five contact sheets, with both count sizes opened full size. Ten leads, all confirmed as intended Recess behavior:
- Four "Hint out of view" state leads: Hint is intentionally hidden in Computer/Friend/count, because it belongs only to puzzles.
- Four phone setup leads: opponent/head start and the two help disclosures are below the board, per the specified scroll order.
- Two first-screen leads: optional "At the table" help scrolls below the fold at 760/375, while the board and frequent controls remain available.
All other size checks clean; no endless calm animation, exceptions, stuck controls, lost focus, or failed settled Enter path. No product fix was required by the audit. No second audit was run.

## Left open

- No Chromebook hardware or human rating was available. Timings are Windows Chrome 156; this pass did not rerun the complete 244-game qualification ladder.
- Book alternatives beyond the accepted routes are not exhaustively classified. The brief's valid-second-solution rule wins over literal single-route-only wording; all three existing f8 routes are retained.
- Shared shell header escaping and the general initials guard still belong upstream as documented in handoff; local workarounds are present. No shared files edited.
- Unattended defaults kept: all grades, weak 19x19 with candid wording, later Chinese/Korean classics, no new modes. Notes retain the Recess grown-ups format, not lesson headings.
- Initial read-only document reads predated the hard-timeout wrapper; all build/play/proof/audit commands were bounded. Browser startup was slow but completed; an initial host favicon 404 was confined to the test wrapper and corrected there.
- Written only under `tools/go/` and `_scratch/go/`; no commits. All review-owned Chrome instances and servers were closed before this report.
