# Dance Pattern Puzzle: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: dance-pattern-puzzle

#### Built
- Build only in the requested checkout. No git commits, branch operations, shared-file changes or polish round.
- 18 puzzles, six chapters, four-attribute card maker, lens, animated checking and earned letter replay.
- My dance: eight slots, copy/mirror/remove, live prime letters, named forms, six challenges, looping and local save.
- Four original synthesized tracks. Kit voice, figure, floor, phrases, clock, counts and music are used.
- Five new non-person paintings. Sixteen future people pose sets are listed for the next painter.
- All requested source, metadata, notes, manifest, voice, audit-state and handoff files are present.
- The report was deferred until the end to honor the user's instruction to stop as soon as it was written.

#### Numbers check
- Independent script and results: `_scratch/dance-pattern-puzzle/data.py` and `numbers.txt`.
- All thirteen ordinary lettered puzzle sequences agree. Facing exceptions follow the table.
- Source prose overstates the facing-chain result: 4-2 ends back after two left quarter turns. The table is correct.
- 36 counts: 30.0 / 22.5 / 18.0 seconds at 72 / 96 / 120 BPM. 44 counts at 72: 36.6667 seconds.
- Tinikling's four replay passes total 26.0114 seconds from 72 and 20.1387 seconds from 96.
- Contrast: white/cobalt 5.726:1; cobalt/paper 5.423:1; ink/paper 15.032:1; muted/paper 6.253:1; wrong outline/white 5.438:1.
- A slow browser count-in can extend the visual count-in until speech finishes. The encore starts without a speech pause.

#### Feel check
- Best moment: a repaired strip gains its cobalt letter bands and dances an immediate encore, with primes lighting on mirrored sides.
- Flattest moment 1: the first version paused for the solved sentence before the encore. Changed it to start the encore while that line speaks.
- Flattest moment 2: early previews held a static gesture indefinitely. Added a two-count gesture and return, plus smooth quarter turns.
- Added warm wood shading, grain and nails. The painted festival square fills the scene and chapter map.
- Played a complete keyboard-only puzzle and a full My dance performance. All 18 puzzles also ran through accelerated engine checks.
- The temporary kit figure remains visibly simpler than the paintings, as authorized by the owner. Painted replacements are deferred explicitly.
- Compared with Snowy Mail Route and Beat Lab. Side-by-side frame: `_scratch/dance-pattern-puzzle/bar-comparison.png`.
- The bar frames were reviewed with the first playable frames, rather than before coding. This is a process deviation.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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


#### Frames looked at
- All PNGs in `first-frames`, `check-frames`, `late-frames`, `targeted-frames`, `last-frames`, `final-frames`, `feel-frames`, `phone-final-frames`, `count-frames` and `final-rule-frames`.
- All mechanical audit frames through four-frame contact sheets; full-size confirmed leads were inspected separately where needed.
- Every STANDARDS size, both modes, ten-card extreme, three culture cards, lens, wrong card, solved letter bands, confirmation, Motion off and grayscale.
- Final targeted batches have zero console errors, warnings or exceptions. Earlier host favicon 404s belong to the test host; the final static host has none.
- Final `count-frames` and `quick-final-frames` were also inspected; quick mode double-tap logs contain whole welcomes without cuts.

#### Art made
- 5 images; 397.2 KiB total art; 941.5 KiB bundle (964,090 bytes), below 2 MB.
- Built-in imagegen, five paintings, no people. Finished WebPs were inspected. No scene redraws; the bamboo pole was re-keyed with despill and key-hue cleanup.
- Prompt set and provenance: `art/prompts.json`. Raw PNGs: `art/raw/`. Credit is in metadata and the HTML comment.

#### Art still to paint
- Sixteen `people: true` pose sets: stand, eight core moves and seven folk moves, with side, level, facing and keyframe variants.
- The kit figure is the authorized temporary figure. `renderer.icon`, `renderer.preview`, `renderer.frame` and `POSE_ART` are the swap points.

#### Engine changes wanted
- `kit/dance.js`, clock.setBpm: optional immediate fractional retiming. Current workaround: pause, set BPM, resume.
- `kit/dance.js`, floor.resize: allow a smaller dancer-height minimum in short scenes. Current workaround: actor scale.
- No engine files were changed.

#### Left open
- Compact folk screens need vertical stage/page scrolling. A scrolled short side panel can hide its hint and maker until scrolled back.
- Rapid puzzle-coordinate taps can cut an introductory how line; current hints remain readable. Challenge text can move the occasional Clear button.
- The full audit was run once; it was not rerun after targeted build fixes. Review the final source together with the original leads and targeted evidence.
- No recorded narration was made, per the brief; the selected clear-teacher/Iapetus manifest falls back to browser narration.
- Painted dancers remain for the next painter and owner review. No people were generated in this build.
- Kept all three folk dances under the user's current-spec leaning instruction; the older baseline says to drop Mayim Mayim. Handoff records this conflict.
- Misplaced K-2 standards and the overly broad facing-chain prose need a later spec/catalog correction outside the allowed folders.
- Cold teaching/cultural review is still next. This build does not claim to be that review.

- Every Chrome and server started for this build is closed. No tool-folder host.html remains.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: dance-pattern-puzzle


#### Played

- Played all 18 puzzles and My dance cold as a grades 3-5 student before reading the builder report and handoff; repeated the key choices as a projecting teacher.
- Strong: the festival square, four-attribute progression, prime letters and immediate letter-band encore. Wrong choices stop at the first broken attribute and preserve the student's card.
- Evidence: `_scratch/dance-pattern-puzzle/cold-frames/`, independent letters/count calculations and `keyboard-solve.json`.

#### Findings fixed

- Should fix, family:dance, stage/cards/map: the temporary code figure was much flatter than the setting. Painted a varied three-person cast and used it everywhere through a swappable atlas adapter.
- Should fix, family:dance, pose readability: forearms vanished when foreshortened, shoes hid behind trousers and the forward kick looked grounded. Retained readable limbs, corrected shoe layering and clarified the low kick.
- Should fix, general, compact layout: scrolling settings hid the hint and maker; culture screens pushed the strip and Play apart. Fixed the maker, moved compact culture text below settings and kept the core actions together.
- Should fix, general, card strip: wrapped side arrows inflated small cards and clipped later rows. Kept marks on one line and retuned the compact spacing.
- Should fix, family:dance, preview/finish: captions named a move while the figure returned to standing. Hold the characteristic pose; a solved final move now gains a gold stage edge.
- Should fix, general, cultural content: the baseline drops Mayim Mayim. Reframed its exercise as a general grapevine pattern without that attribution.
- Should fix, general, Seven Jumps: the historical source does not begin with knee lifts. Explicitly identify this short knee-lift/kneeling sequence as a classroom adaptation and correct the source explanation.
- Polish, general, My dance: reserve challenge-card height so the changing text does not shift Clear.
- Should fix, general, My dance counts: removing cards left slot-based count labels and a 16-count heading beside a shorter performed phrase. Count filled cards and label the counts that actually play, including gaps.
- Should fix, general, header focus: the amber ring had only 1.14:1 contrast against cobalt. Use white, 5.73:1, and keep the ring inside compact-header padding.
- Should fix, general, quick given-card taps: a relevant introduction was cut by idle previews. Preserve that line and its chapter explanation while keeping edits and live playback interruptible.
- Polish, general, map/tempo: separate the six compact chapter-button boundaries from their puzzle dots; keep all three compact tempo choices fully visible.
- Voice manifest, teacher notes, art manifest, audit states and handoff updated to match the finished behavior.

#### Findings left

- Should fix, spec/catalog scope: the spec's misplaced K-2 standards need a separate correction outside the permitted folders. No K-2 activity was invented.
- Polish, spec prose: the statement that all facing chains return front is overbroad. Puzzle 4-2 correctly ends back after two left turns; the content table remains correct.

#### Flattest moment left

- Early AB puzzles are deliberately simple. The painted movement, lit count and earned encore carry them; the deeper choices begin with sides and levels.

#### Graphics

- Checked the original five paintings and added one atlas, marked `people: true`, with three people and three master views each. No existing painting was deleted.
- Built-in imagegen prompt/provenance: `art/prompts.json`; finished cast: `art/dancer-cast.webp`; raw master: `art/raw/dancer-cast.png`.
- Three painted views per person supply all articulated moves, sides, levels and facings. `PAINTED_ATLAS`, `CAST_RECTS` and `paintDancer` are the swap points.
- Fresh cultural/people review: PASS, `_scratch/dance-pattern-puzzle/sensitivity.md`. Front/back, low, kick, jump and phone frames inspected.
- Bundle: 1,126 KiB (1,153,067 bytes). The unused original water-well picture remains in art and is not bundled or shown.

#### Audit

- Completed once in 2,141.8 seconds, exit 0, before the 40-minute limit: `_scratch/dance-pattern-puzzle/review-audit/audit.md`.
- 89 mechanical leads reviewed against the 62 audit frames (all inspected through `audit-sheets/`, with confirmed leads opened full size).
- Fixed the six compact-map boundary overlaps and the three quick-tap introduction cuts; targeted frames/logs in `final-repair-frames/` confirm the shared fixes.
- Hidden map-hint leads are expected: the visible map has its own equivalent instruction and Read uses it.
- Optional-settings scroll leads remain intentional; the actual answer choices, hint, strip and Play stay visible together. Compact tempo choices are now wholly visible. Dialog-background controls are intentionally inert.
- The 17 inert-maker/focus rows are inherited disabled fieldset controls before a slot is selected, not lost focus during editing. Selected-slot and keyboard paths passed.
- Map/puzzle welcome flags are expected own-action narration: the full puzzle instruction speaks directly instead of a stale map welcome. Sound and Read interrupt their old lines intentionally.
- All ten two-second repeated-click checks passed. Motion off and every mid-action resize/stress check passed; error columns are empty.
- Only repair-specific frames were re-shot afterward. No second full audit or review pass was run.
- Independent letter checking matches the table. The separate generic-letter check's Tinikling flag is its intentional In/In/Out label exception.

#### Left open

- Browser narration remains because the brief prohibits recording audio. Fixed lines match the manifest; held-click checks show countIn 5/5 and lens how-to 1/5. Read interrupts and follows mode state.
- Keyboard-only Enter/Q/arrows/Space solved puzzle 2-1 from a fresh save and finished its encore. All standard sizes, Motion off, grayscale and the 375-pixel host were inspected.
- Compact culture text and occasional settings require vertical scrolling; the strip, maker and Dance it stay together. No sideways phone scroll.
- No commits or shared source edits. Process slips: the initial read lacked a time bound; an early DOM dump exposed a source tail before cold play finished; the two bar examples were inadvertently rebundled to ignored HTML outputs outside the permitted folders.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Dance Pattern Puzzle: handoff after cold review

#### Structure

`src.html` contains the 18 puzzle records, four-attribute maker, responsive festival scene and My dance rules.
`letters`, `patternName`, `challengeFits` and `firstBroken` are separate rule functions exposed through `window.__tool`.
Card buttons and maker controls persist during edits. Navigation rebuilds the strip and deliberately focuses its first blank with preventScroll.
`dance` owns one engine clock, player and music bus. Every interrupt invalidates its run token.
`retime` pauses, changes BPM and resumes at the same fractional count. The shared kit was not edited.

#### Painted dancers

The stage, card icons, move buttons and chapter map all use painted dancers.
`art/dancer-cast.webp` is one swappable atlas: three people, each with front, profile and back views.
The cast varies skin tone, age, hair and body build. Its manifest entry carries `people: true` and `drawn_by: codex`.
Full prompt and provenance are in `art/prompts.json`; the generated master is `art/raw/dancer-cast.png`.

`PAINTED_ATLAS`, `CAST_RECTS` and `paintDancer` form the adapter. Source rectangles use the original 1254-pixel master coordinates.
The re-keyed atlas is mapped back into those coordinates with x=15, y=8, width=1225 and height=1240.
The adapter puts painted head, shirt, arm, trouser and shoe pieces over the engine's projected joints.
The engine's original figure shapes are hidden; its skeleton, depth ordering, poses and timing remain in use.
There are three master views per person rather than a separate painting for every combination of move, side, level and facing.
Back views use an actual back painting; profile heads are mirrored only for the opposite profile.
Shoes render after their shin and foreshortened arms retain a readable hand/forearm length.
`actor.paintCast(index)` changes the cast. Chapters cycle through it; My dance uses the tan child.

The fresh sensitivity review passed the cast and placed poses after the kick was clarified.
Evidence: `_scratch/dance-pattern-puzzle/sensitivity.md`, `kick-frames/kick-clear.png` and the targeted review frames.
The original five non-person paintings remain, including the unused water-well image. No existing painting was deleted.

#### Review changes

- The card maker and Play stay fixed while occasional settings scroll separately in short landscape views.
- Compact Side and Level share a row. All maker choices remain visible and at least 44 pixels tall.
- Phones show the strip, hint, maker and Play together. The culture card follows the settings on compact views;
  it remains above the strip on larger screens. Read includes its full text in either position.
- Side marks no longer wrap and inflate compact cards. Tinikling uses its numbered cards and tap/tap/close row in short views.
- Preview and completion hold the characteristic movement pose, matching the caption and card.
- A solved finish has a gold stage edge. The low forward kick is lifted enough to read from the front.
- The challenge card reserves its height, so changing its prompt does not shift Clear.
- My dance labels and the count strip count the filled cards that actually play, including after removals.
- Header keyboard focus is white against cobalt. Idle given-card previews preserve a still-relevant spoken introduction.

#### Teaching and culture

All four attributes are checked, except that Clap and Jump ignore side.
The two facing-pattern letter displays deliberately ignore facing; answer checking still includes it.
Around the square has no letter labels. Adding-on groups and Seven Jumps round boundaries have thicker borders.

The owner's baseline drops Mayim Mayim. The former puzzle is now a general grapevine pattern exercise.
Seven Jumps is explicitly a short classroom adaptation using knee lifts and kneeling.
Burchenal's 1915 primary text begins with stamps, then knees, elbows and forehead; the tool no longer claims that its knee lifts are that historical sequence.
Tinikling keeps the Philippines attribution, bird connection, three-count pattern and tape/rope classroom alternative.
Tunes are original synthesized music, not traditional melodies. Source links and the adaptation explanation are in notes.md.

Tinikling has nine one-count cards. Its poles close every third count, with the dancer outside.
The solved replay has four passes at base BPM, base+8, base+16 and base+24, capped at 120.
Other cards have two counts. Motion off keeps time and holds each characteristic end pose.

#### Voice and storage

`Curio.voice` provides once-only how lines, repeating events, stale-line checks and Read priority.
`voice/lines.json` matches `allLines()` including the revised culture text. Narration uses browser fallback; no recordings were made.
Count-in waits for its spoken line when needed. Lens and Read keep the dance running.
Local storage is guarded, validated and disclosed. Clear confirms, clears the dance and solved dots, and removes the save.

#### Verification and remaining scope

Cold play covered every puzzle, wrong answers and My dance before the builder report, handoff and systematic source read.
An early DOM dump accidentally included a source tail; the cold review report records this process slip.
Independent calculations confirm count durations, capped replay timing and the ordinary letter sequences.
Standard-size, phone-host, Motion-off, grayscale, held-click voice, keyboard and targeted pose evidence is in Scratch.
The single final audit completed in 2141.8 seconds with 89 mechanical leads: `_scratch/dance-pattern-puzzle/review-audit/audit.md`.
Final repairs were checked only with targeted frames and held-input logs; no second audit was run.
The cold review report groups every lead and explains expected disabled, hidden and optional-scrolling cases.

The spec's misplaced K-2 codes and overbroad claim that every facing chain returns front need a later spec/catalog correction.
Puzzle 4-2 correctly ends facing back after two left quarter turns. No new K-2 activity was added.
Compact culture text and occasional settings require scrolling; the frequently used strip, maker and Play remain together.

#### Engine changes wanted

- `kit/dance.js`, `clock().setBpm`: optionally support immediate fractional retiming. The tool's pause/set/resume workaround works now.
- `kit/dance.js`, `floor().resize`: consider a smaller dancer-height minimum for short scenes. The tool currently adjusts actor scale.

No commits, branch operations or shared source edits were made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
