# Codex report: dance-pattern-puzzle

## Built
- Build only in the requested checkout. No git commits, branch operations, shared-file changes or polish round.
- 18 puzzles, six chapters, four-attribute card maker, lens, animated checking and earned letter replay.
- My dance: eight slots, copy/mirror/remove, live prime letters, named forms, six challenges, looping and local save.
- Four original synthesized tracks. Kit voice, figure, floor, phrases, clock, counts and music are used.
- Five new non-person paintings. Sixteen future people pose sets are listed for the next painter.
- All requested source, metadata, notes, manifest, voice, audit-state and handoff files are present.
- The report was deferred until the end to honor the user's instruction to stop as soon as it was written.

## Numbers check
- Independent script and results: `_scratch/dance-pattern-puzzle/data.py` and `numbers.txt`.
- All thirteen ordinary lettered puzzle sequences agree. Facing exceptions follow the table.
- Source prose overstates the facing-chain result: 4-2 ends back after two left quarter turns. The table is correct.
- 36 counts: 30.0 / 22.5 / 18.0 seconds at 72 / 96 / 120 BPM. 44 counts at 72: 36.6667 seconds.
- Tinikling's four replay passes total 26.0114 seconds from 72 and 20.1387 seconds from 96.
- Contrast: white/cobalt 5.726:1; cobalt/paper 5.423:1; ink/paper 15.032:1; muted/paper 6.253:1; wrong outline/white 5.438:1.
- A slow browser count-in can extend the visual count-in until speech finishes. The encore starts without a speech pause.

## Feel check
- Best moment: a repaired strip gains its cobalt letter bands and dances an immediate encore, with primes lighting on mirrored sides.
- Flattest moment 1: the first version paused for the solved sentence before the encore. Changed it to start the encore while that line speaks.
- Flattest moment 2: early previews held a static gesture indefinitely. Added a two-count gesture and return, plus smooth quarter turns.
- Added warm wood shading, grain and nails. The painted festival square fills the scene and chapter map.
- Played a complete keyboard-only puzzle and a full My dance performance. All 18 puzzles also ran through accelerated engine checks.
- The temporary kit figure remains visibly simpler than the paintings, as authorized by the owner. Painted replacements are deferred explicitly.
- Compared with Snowy Mail Route and Beat Lab. Side-by-side frame: `_scratch/dance-pattern-puzzle/bar-comparison.png`.
- The bar frames were reviewed with the first playable frames, rather than before coding. This is a process deviation.

## Done when
1. PASS: all 18 tables load, blanks match, listed answers solve, and displayed letters agree. `rules.json`, `plays-0/6/12.json`.
2. PASS: attribute priority tested for move/side/level/facing, including ignored Clap/Jump sides. Actual wrong run stops at card 6. `interactions.json`.
3. PASS: every puzzle's lens leaves its cards unchanged. Changing marks are outlined, including both attributes in 3-3.
4. PASS: fractional position survives immediate retiming; Tinikling replay is 96,104,112,120 in the test. Count-three frame shows closed poles and Out at z=57.
5. PASS: prime/named letters and all six positive/negative challenge cases checked; an additional hidden-side Clap case passes. Confirmed Clear removes the save.
6. PASS for the stated views: maker, Play and strip at 1366x768 and 1000x625; 375 px wraps to two rows with scrollWidth 375. Compact folk limitations remain below.
7. PASS: real keyboard-only Tab/Enter/Q/arrow/Space input solves 2-1 and finishes its encore. `keyboard.json`.
8. PASS with browser narration: held clicks at two-second gaps start the how line once; repeating events use event kind. Full solve logs contain countIn and solved.
9. PASS for source-to-content correspondence: supplied culture text is retained, each culture card has its painted picture, sources are in notes and metadata.
10. PASS: strip spans the stage below the dancer at the two specified sizes. Standard cards exceed 64x88 at 1366x768, including the ten-card puzzle.
11. PASS: card, maker, Reset, Next and Chapters interrupt and invalidate the run; lens and Read preserve it; tempo changes mid-card. `interactions.json`.

## Wave lessons
| Lesson | Result and evidence |
|---|---|
| Hint and voice | PASS: hint changes synchronously; kit queue, V.heard, valid/run tokens, 28 matching manifest lines and held-click log. |
| Focus and layout | PASS for persistent edits: maker/card buttons are updated in place; reserved hint height; navigation focuses the next card without scrolling. |
| Sizes | FAIL for the strongest all-states interpretation: culture screens and scrolled settings in small previews do not keep everything visible together. |
| No giveaways | PASS: letters wait for a successful run; unknown cards remain question marks; lens does not fill them. |
| Honest numbers | PASS: independent count, tempo and contrast computations; original tunes are described as original. |
| Standards | FAIL for the spec's misplaced K-2 codes; no K-2 activity or catalog edit was added. Grades 3-5 scope follows the supplied activities. |
| Motion off | PASS: static end poses with unchanged timing; lantern loop stops; grayscale frame retains shape/arrow/letter signals. |
| Short choice sets | FAIL in scrolled compact panels: occasional controls can scroll the maker/hint above the panel viewport. All controls remain reachable. |
| Resize mid-animation | PASS in the single audit: every planned state and walk action resized to 760x900 and back; no exceptions or controls left disabled. Final targeted edits were not followed by a full audit rerun. |
| Late welcome | PASS by queue structure: welcomeAfter is not enabled; own-action lines take priority and have state validity checks. |
| Unknown as unknown | PASS: blanks have question marks; maker previews the previous card without revealing the target. |
| One look, one meaning | PASS: side arrow plus letter, three level ticks, facing circle, prime and letter bands. |
| Truthful badges | PASS: solved dots only follow a matching run; challenge checks are tested against positive and negative strips. |
| Hint changes back | PASS: mode, chapter, lens, selection, edit, reset, clear and stop all write a current hint. |
| No answer by copying words | PASS: chapter hints identify the changing attribute, not the missing value. |

## Audit leads
- Completed once in about 34 minutes: `_scratch/dance-pattern-puzzle/audit/audit.md`, 149 leads. Original evidence is retained.
- The run spans build iterations. Earlier size/state frames precede several targeted fixes; it is not a clean final-version rerun.
- Map hint-out-of-view leads at all eight sizes: expected. The panel is hidden on the map; its visible instructions say to pick a chapter, and Read voices the map instruction.
- Five 760x900 dot-overlap pairs: fixed by the three-column chapter map. `final-frames/map-760-final.png` confirms separation.
- My dance mode and mine-work phone leads for all three tempos, Loop, Challenge and Clear: left open as lower-page controls. Main dance/edit controls fit, including Copy/Mirror/Remove.
- Puzzle-selected phone tempo/lens/reset/Chapters/Next below-fold leads: left open. The 84%-visible Dance it lead is fixed; final bottom is 799.8 in an 812 px host.
- Focus falling to the page in puzzle-selected, wrong-card, lens and folk-poles: fixed with shared navigation focus to the first missing card, using preventScroll.
- Walk puzzle navigation focus leads, rows 5 through 27: same shared fix. A held click on puzzle 2-1 lands on card 4; the last walk row was already clean.
- Wrong-card 680 hint-hidden lead: left open when the short side panel has scrolled to lower settings. Scroll back to its hint and maker.
- Lens 680 maker-covered and hint-hidden leads: same compact-panel limitation, left open. Phone Chapters/Next below-fold leads also remain.
- Folk-poles 680/800 strip visibility leads: changed from inaccessible clipping to vertical stage scrolling. Full simultaneous visibility still fails in these short previews.
- All folk phone below-fold leads for In/Out, side, levels, facings, Dance it, tempo, Faster, lens/reset/Chapters/Next, plus keep-region leads: left open. The culture card adds page height.
- Clear-confirm hidden hints at 680/800/1000: expected behind the modal. The dialog itself contains the question and both named actions and is visible in every frame.
- Walk My dance maker leads, all 17 move/side/level/facing buttons: expected inert controls before a slot is selected; the enclosing fieldset is disabled. Real selected-slot editing is covered by the rule/interaction runs.
- Walk missing-map-welcome leads on all six chapter buttons and 18 puzzle dots: expected own-action narration. The spoken row contains the full puzzle instruction; a stale map welcome is skipped.
- Sound cuts its welcome when toggled off, and Read prioritizes its requested line: expected kit behavior.
- Challenge changes moving one other control: left open. Its wrapped text can move the occasional Clear button; the card maker and Dance it stay in place.
- Two rapid active-mode taps cutting wMap/wMine: fixed by making a click on the active mode a no-op. Both final 0.7-second held double-tap logs show one whole welcome, no cut, zero errors.
- Rapid puzzle-coordinate taps cutting the introductory how line on puzzle-0, puzzle-2 and puzzle-3: left open. The new state has a current hint and Read, but an already-started once-only line is not retried in full.
- All ten two-second repeated-click checks: clean. Motion off: clean. Resize during every planned state and walk action: clean, no exceptions or controls left disabled.
- Audit error columns are empty. No audit rerun was started; final targeted frames/logs cover the named fixes.


## Frames looked at
- All PNGs in `first-frames`, `check-frames`, `late-frames`, `targeted-frames`, `last-frames`, `final-frames`, `feel-frames`, `phone-final-frames`, `count-frames` and `final-rule-frames`.
- All mechanical audit frames through four-frame contact sheets; full-size confirmed leads were inspected separately where needed.
- Every STANDARDS size, both modes, ten-card extreme, three culture cards, lens, wrong card, solved letter bands, confirmation, Motion off and grayscale.
- Final targeted batches have zero console errors, warnings or exceptions. Earlier host favicon 404s belong to the test host; the final static host has none.
- Final `count-frames` and `quick-final-frames` were also inspected; quick mode double-tap logs contain whole welcomes without cuts.

## Art made
- 5 images; 397.2 KiB total art; 941.5 KiB bundle (964,090 bytes), below 2 MB.
- Built-in imagegen, five paintings, no people. Finished WebPs were inspected. No scene redraws; the bamboo pole was re-keyed with despill and key-hue cleanup.
- Prompt set and provenance: `art/prompts.json`. Raw PNGs: `art/raw/`. Credit is in metadata and the HTML comment.

## Art still to paint
- Sixteen `people: true` pose sets: stand, eight core moves and seven folk moves, with side, level, facing and keyframe variants.
- The kit figure is the authorized temporary figure. `renderer.icon`, `renderer.preview`, `renderer.frame` and `POSE_ART` are the swap points.

## Engine changes wanted
- `kit/dance.js`, clock.setBpm: optional immediate fractional retiming. Current workaround: pause, set BPM, resume.
- `kit/dance.js`, floor.resize: allow a smaller dancer-height minimum in short scenes. Current workaround: actor scale.
- No engine files were changed.

## Left open
- Compact folk screens need vertical stage/page scrolling. A scrolled short side panel can hide its hint and maker until scrolled back.
- Rapid puzzle-coordinate taps can cut an introductory how line; current hints remain readable. Challenge text can move the occasional Clear button.
- The full audit was run once; it was not rerun after targeted build fixes. Review the final source together with the original leads and targeted evidence.
- No recorded narration was made, per the brief; the selected clear-teacher/Iapetus manifest falls back to browser narration.
- Painted dancers remain for the next painter and owner review. No people were generated in this build.
- Kept all three folk dances under the user's current-spec leaning instruction; the older baseline says to drop Mayim Mayim. Handoff records this conflict.
- Misplaced K-2 standards and the overly broad facing-chain prose need a later spec/catalog correction outside the allowed folders.
- Cold teaching/cultural review is still next. This build does not claim to be that review.

- Every Chrome and server started for this build is closed. No tool-folder host.html remains.
