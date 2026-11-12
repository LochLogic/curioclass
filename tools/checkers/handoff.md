# Checkers handoff

Build followed by one cold self-check. No git commits, publication, or shared-kit changes.

## Play

Open `checkers.html`, the generated offline game. `src.html` is the readable canonical source.
The game uses the Recess API and its controls, win card, initials board, scores, sound and motion settings.
It has six computer opponents, pass-and-play, five rounds of five puzzles, and a mirrored seeded daily.
Use `?test` for the automatic 173-assertion self-check and `checkersDev` console helpers.
Use `?ladder` for ten full ballot games per adjacent pair, entirely in Workers, with console results.

## Rebuild

From `S:\CurioClass-codex`:

```
python _scratch/checkers/review_run.py 120 python -c "import os,runpy,sys; os.environ['CURIO_DRAFT']='1'; sys.argv=['scripts/bundle_tool.py','checkers']; runpy.run_path(sys.argv[0],run_name='__main__')"
```

The ordinary repository bundler now works. The source keeps the inlined shell in a hidden textarea, then inserts
only its executable code as script text. This avoids both HTML end tags and kit tokens in the shell's header comments.
Keep the source kit stylesheet token without a self-closing slash; the bundler's exact pattern requires that spelling.
The wrapper and all verification scripts are retained in `_scratch/checkers/`.
Do not use `assemble.py` for routine source edits: it is the build's assembly history and will replace the game script
with the scratch modules. The final formatted `src.html` contains everything and needs no runtime dependencies.

## Engine changes wanted

- `kit/recess.js`, opening documentation comment: replace the literal closing script tag in the example with an
  escaped spelling. It currently terminates an inline script while the HTML parser is inside a JavaScript comment.
  The header's stylesheet example also gets expanded by the bundler after the JS is inlined. The local wrapper
  is now replaced by the source-local inert loader; the shell implementation remains unchanged.
- `scripts/bundle_tool.py`: accept an optional self-closing slash in stylesheet kit tokens, or document the exact token.
  No shared file was edited for this build.
- `kit/recess.js`, `card`: trap Tab and Shift+Tab inside its modal. The game now supplies this keyboard guard locally.
- `kit/recess.css`, `.rc-arr`: make initials arrows 44 px high. The game now overrides their height locally.

## Evidence

- `look/`: three 1366x768 hero frames painted and reviewed before game logic; static visual source retained.
- `rules-results.json`: eight edge cases, all puzzle lines, 5000 mirrored positions; `rules_test.js` additionally
  compares 5000 positions against an independent 8x8 generator and checks incremental Zobrist hashes.
- `solver-results.json`: all 25 puzzles independently re-solved. Eleven historical positions solved by exhaustive
  reachable-state retrograde analysis, including every listed alternative and the end distance.
- `ladder-2.json` through `ladder-5.json`, and `ladder-6-5.json`: final adjacent-pair ballot games and search timings.
  `ladder-6.json` is an earlier development run; use `ladder-6-5.json` for the final Titan engine.
- `ladder-3-1.json`: twenty Nova versus Pip games.
- `rounds-1-3.json`, `rounds-4-5.json`, `break-results.json`, `daily-results.json`, `stars-results.json`: actual browser
  state, first-run scoring, Encore sealing, Undo and restart abuse, wrong answers, alternatives, clues and star gates.
- `fullplay/`: full games through the interface against every opponent, plus pass-and-play, with console exceptions checked.
- `final-frames/`, `grab-frames/`, `touch/`, `last-frames/`, `audit/`: responsive, keyboard, pointer, touch, resize, offline,
  comparison, reduced-motion, grayscale and mechanical audit evidence.

## Spec discrepancy

Fence (`r1-5`) does not have the asserted immediate win `10-15`. Blue can jump `21x14` over Amber 17.
`10-14` fills that landing and wins immediately. The shipped book line is unchanged, and `10-15` is judged by the
actual American checkers rules. No shared specification was edited.

## Choices made unattended

Kept all four accepted defaults: mandatory jumps, Amber and Blue side names, Grades K-12, and Titan's three-second budget.
All puzzle material came from the supplied spec, so no external puzzle collection was fetched.
Portrait art is a crop of the same painted arcade. Sprite marks, crowns, halos, robots and sparks are painted.
Transparent targets expand to 44 px around exact square centres in small previews.

## Limits

The cold review closed the clue-only best-score loophole: a clue is a puzzle try and costs one Move, just like a
wrong try. Three clues still play the answer and award one star, but cannot tie an unassisted minimum. The How to
play panel and clue prompt disclose this. Unassisted round minima remain 6, 10, 12, 23 and 40.

The same review keeps the last valid puzzle index after an award, resumes a book reply after Flip, and defers
Hints/resize redraws until a moving puck lands. Puzzle finishes now name the jump or trap and leave more of the
painted board visible. See `codex-review.md` for current verification; the build report records the earlier state.

Tests ran in Windows Chrome, including emulated Chromebook and phone viewports. No physical Chromebook, physical phone,
child or adult human strength trial was available. The top opponent is measured against the ladder, not rated against people.
The independent cold review is recorded in `codex-review.md`. No sign-off or deployment has been performed.

## Live early

Live early for Cory to see, 2026-11-12, process not exempted. tool.draft.json was renamed to tool.json only so the site lists the game; Refine, Exit check, Art and voice, Finish check and Sign-off are still owed.
