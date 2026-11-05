# Codex review: near-and-far
## Played
Played before builder files as a Grade 4 solo student: Valley, all eight postcard starts, the print hunt and Escape.
Then solved all eight postcards with held clicks, jittered real drags and corner resizing; solved puzzle 1 by keyboard.
Checked the compact/projected view too. The painted valley and earned before/after postcard are strong.
VA:Cr2 is practiced through composition and revision; VA:Re7 through identifying and explaining the print's mistakes.
Evidence is in _scratch/near-and-far/: cold/play/hands frames, review-play/results.json and review-keyboard.json.

## Findings fixed
- Blocker, general, src.html drawSide: the eye was fixed five pixels above ground, unrelated to the 1.5 m camera.
  It now follows the objects' shared vertical scale. Exact cow and post solutions meet eye level.
- Should fix, general, Puzzle 3: its cover goal ticked before the pictures overlapped. Actual overlap is now required.
- Should fix, general, pointer selection: preventDefault discarded focus, so arrows after clicking did nothing.
  Stable object nodes now receive focus with preventScroll. A real click plus arrow moves exactly one percent.
- Should fix, general, Mixed-Up Picture: fitting moved the print but left its spotlight at old coordinates.
  Fit now recomputes the ring; compact and phone zoom frames were checked.
- Should fix, general, fade readout: only misty-near disagreements were explained. Every wrong fade band now gets
  concise advice in Valley and Misty Hills; other postcards retain their specified goal focus.
- Should fix, general, horizon chip: repeated fitting could squeeze its caption into several lines. Prevented wrapping.
- Should fix, general, narration: fixed Read hints were absent from allLines and voice/lines.json. Both now agree.
- Should fix, general, windmill art: masonry contradicted the wooden-tower brief. Repainted a detailed timber tower.
- Should fix, general, selected-cow readout: cropped at 680x425, 1280x720 and 375x812.
  Tightened short-screen shelf spacing, omitted the redundant compact notebook title and shortened fade advice.
  The full readouts, all shelf choices and 44 px controls now fit; the postcard keeps its size.
- Should fix, general, audit-states.json: solved-wipe drag expressions returned no points, so the state was unsolved.
  Added explicit returns. The corrected recipe reaches the earned wipe at 680, 1366 and 375.
- Polish, general: the completed hunt still asked for more finds and repeated completion on revisits.
  Added current next-action wording and a revisit label; completion narration triggers on the newly found eighth error.
- Polish, general: a stationary press cut applicable instructions. Actual movement now invalidates that speech.
- Polish, general: the first cow barely registered in Side View. A shared scale for small subjects gives it 40 px
  at 1366x768 while preserving relative heights. Redrew the flat hills with layered painted texture and natural ends.

## Findings left
- Should fix, spec: Done when 2 promises universal two-pixel post alignment, but the required Solid tolerance allows
  larger errors. Changing that tolerance would change the spec; exact solutions do meet the horizon.
- Should fix, spec goals: other postcards can satisfy their listed goals while displaying an overlap warning.
  Enforcing overlap in all of them would add goals. The written warning remains; Puzzle 3's explicit goals work.

## Flattest moment left
Fine tuning a tiny far object still takes patience. The 44 px grab area, keys and existing target outline support it.
Automatic snapping or another distance control would change the specified interaction and was not added.

## Graphics
Checked all 12 painted assets in the shelf/postcards and the public-domain print at all eight zoom spots.
Redrew hills and windmill with built-in imagegen. Full prompts: art/prompts.json; raw outputs: art/raw/hills.png
and art/raw/mill.png; final assets: art/hills.webp and art/mill.webp. No people were generated.
Kept the valley, nine other cutouts, notebook framing and gold/wipe payoff. Compared with the existing bar frame.
Total final WebP art: 559.7 KiB. Final bundle: 851595 bytes, 833.2 KiB, below 2 MB.

## Audit
One full audit finished inside the 2400-second limit: _scratch/near-and-far/review-audit/audit.md, 32 leads.
- Fixed five confirmed leads: three cropped readouts and two consequences of the invalid wipe recipe.
- Fourteen hill/object overlaps are intentional in that flat starting picture; exposed areas and keyboard selection work.
- Twelve welcome skips follow STANDARDS: a first action's own line wins, with no late empty-Valley welcome.
- One caption keep lead is a hit-test false positive from pointer-events:none; its text is visibly clear.
All 68 audit PNGs were inspected in labeled sheets. Every initial size/mode, Motion off and resize-mid-action was clean.
Scoped rechecks only: review-audit-fixes/results.json and results-last.json. Wipe succeeds at three sizes;
complete cow readouts pass at 680, 1280 and 375. The final two checks have zero leads and zero console errors.
Two scoped wipe warnings classify the temporary BEFORE overlay against an underlying object; these are intentional.
No full audit was rerun after the fixes.

| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| dragHow, five shelf taps | how | 1 | 1 |
| dragHow / sideHow, five real drags | how | 1 each | 1 each |
| ghost, five edits | event | 5 | 5 |
| solved, five completions | event | 5 | 5 |
| find events, including revisits | event | 5 | 5 |

First-tap stage/control/mode/Read/Sound/key cases, fast stale-line changes, Read interruption and Sound-off Read passed.
Independent review-numbers.json matches the camera examples and contrast ratios; exact fence-top errors are zero.
Notes open with the three required sections. Tool storage clears correctly. No external assets or fetch calls.
Chrome ports 9950/9951 and host 8755 are closed; host.html is removed. No commits were made.

## Left open
- A 10 m place / 12 m size post is Solid under the specified ratio yet misses eye level by 22.5 px at 1000x625.
- The first complete balloon is at 193.714 m. The spec's 81 px height and 89.25 px bottom belong to 200 m, not 194 m.
- A saved composition can draw an extreme object below two painted pixels after shrinking the window; its normalized
  cues and 44 px grab target remain intact. Enforcing a new floor would change that composition's depth.
- Narration remains browser fallback. No gravel-ranger clips were recorded, as instructed.

