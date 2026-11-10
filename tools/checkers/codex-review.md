# Codex review: checkers (Recess)

## Played

Cold review in `S:\CurioClass-codex`, against CODEX-RECESS.md, GAMES.md and the Checkers spec.
Tried the ordinary documented bundle first. It could not start; repaired only the shell loader before continuing cold play.
Played the menu, rules, friend, computer, opening puzzles and daily before reading the builder's report or handoff.
Youngest-reader and adult policies were simulated with real held clicks, keyboard, touch and jittered dragging; no human child trial is claimed.
Played all 25 puzzles and full interface games: beat Pip in 49 plies; losses to Dot 50, Nova 312, Comet 46, Blaze 44, Titan 34.
The friend game finished with Blue winning in 126 plies; also tested an agreed draw. The painted arcade and jumps are strong.

## Findings fixed

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

## Findings left

Titan's depth-10 target is qualified: measured unforced searches reached depths 9 to 64, with a maximum 3002.52 ms. It did not meet a universal depth-10 floor.
Kept the accepted three-second budget. Physical Chromebook/phone timing and strength against a good adult remain unverified; emulation and engine ballots do not establish those claims.
The historical book endings remain intentionally guided lines, as specified; listed alternatives spring back for free.

## Break it

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

## Computer opponent

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

## Voice walk

No narration, Read button or classroom welcome belongs here. Confirmed no voice/lesson kit was added.
Sound-off and switching to Calm during a jump complete correctly; Calm reports zero running animations and the local-file game loads zero HTTP resources.

## Facts checked

Held movement, forced jumps, deferred capture removal, crown stops and draw rules to the supplied American/English checkers spec and its named WCDF/Lyman rules sources, then recomputed the behavior.
Fence's asserted second immediate win `10-15` is false: Blue has `21x14`. Kept the legal book win `10-14`; did not edit the spec.
Historical composer names, 1913 provenance and source/licence attribution remain as supplied in the spec; no new historical collection was fetched.
Class-creep scan: zero whole-word hits for standard, objective, learn, skill, lesson, correct answer or well done; zero em dashes.

## Sensitivity

None requiring a cultural scene review: no people or cultural depictions. Historical problems retain their named composers and source attribution.

## Flattest moment left

Titan's quiet thinking interval and the longer book endings. The thinking lights, live cancellation and instant restart keep those waits manageable; no new mode was added.

## Graphics

Inspected all 21 painted WebP assets and the captured frames/contact sheets. Kept the cover, cabinet world, glass board, acrylic pucks, crowns and six rivals.
Replaced only the contaminated spark using built-in imagegen. Prompt/provenance: `art/prompts.json`; original generation: `art/raw/spark-review.png`; final transparent asset: `art/spark.webp`.
Best moment: a three-capture shot reaches the crown row. [Fresh comparison with the shell demo and Collision Lab](../../_scratch/checkers/review-grab-frames-contact.jpg).
Checked 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, 390x844 and 375x812; phones also through port 8765 iframe hosting.
No clipped primary controls or sub-44 px targets in those checks. Dot/ring and crown distinctions survive grayscale. Calm keeps the painted world.
[Size frames](../../_scratch/checkers/review-size-frames-contact.jpg), [modal frames](../../_scratch/checkers/review-modal-final-frames-contact.jpg), [audit-fix frames](../../_scratch/checkers/review-audit-fix-frames-contact.jpg).
Bundle: **1189.5 KiB (1,218,094 bytes)**, below 6 MB. Final hash and 791,850 art bytes are recorded in [review-manifest.json](../../_scratch/checkers/review-manifest.json).

## Audit

Ran `audit_tool.py` once, last, with a 40-minute limit, Chrome 9961 and host 8765. Completed with 73 leads; no exceptions, stuck resize controls or forever-running Calm animations.
Reviewed every audit frame. Missing #hint/voice logs are Recess exclusions. Empty square aria-labels counted as hidden text and intentional result-over-board overlaps are mechanical false positives.
The covered-cell keyboard issue was fixed; only its affected 680/1366/375/390 frames were re-shot, with 32 disabled cells during results and no console errors. No second audit.
[Complete audit](../../_scratch/checkers/review-audit/audit.md).

## Left open

Hardware/adult strength and Titan's depth target remain qualified above. Shared header/dialog/arrow improvements are named in `handoff.md`; working local fixes are in this game.
The first two short read-only inspection commands completed before the timeout wrapper existed; subsequent shell commands used explicit limits. The Titan batch's nonzero exit is disclosed above.
Writes were confined to this tool and its Scratch folder; no commits, sign-off or deployment. All started Chrome/server resources and the temporary host are closed/removed, with [cleanup evidence](../../_scratch/checkers/review-cleanup.json).
