# Codex review: school-wall-mural

## Played

A grade 7 cold opening pass covered all four modes before builder files: neighbor cards, ranking/inspection, sidewalk, bus ride, paint swaps and Board answers. Rubric edits, year-five extremes and enlarged A were checked afterward, along with projection-sized layouts. Rich places and the factory tradeoff are the highlights.
## Findings fixed

- Blocker, general, Board: an old defense survived rubric changes. Rubric changes now restart its questions; banner edits invalidate visual evidence. A nonleader now says it trails by a positive margin rather than claiming a negative lead.
- Should fix, general, Board: cited evidence erased actual weaknesses. The reply keeps the chosen design's low-scoring concerns and reasons, alongside the student's answers.
- Should fix, general, Street test: revised A still offered the removed bridge in recall. It now offers large windows; repeat rides hide recall while the wall passes.
- Should fix, general, Street test: revising an unpinned leader could switch the mural being tested. Revisions now pin that design.
- Should fix, general, graphics: ranking crops hid mural landmarks. Every thumbnail shows the full painting.
- Should fix, general, compact layouts: rubric/selector controls, Listen cards, Board answers and street results fell outside the frame. Reflowed controls/cards and bounded scenes keep the main choices and readouts visible. Applied paint buttons give way to Changes; all five Undo controls fit together. Reset remains visible in both drawer states.
- Should fix, general, waiting hints: adding/removing criteria or revising could leave an old or completed instruction. Hints now name the current next control; stale Add speech is dropped.
- Polish, general, interaction: added immediate sound to Equal weights, Undo, closing/back navigation and Summers changes; fixed singular focal-shape wording.
- Polish, general, weakest art: redrew the empty boardroom with three attentive, varied adults in the existing gouache style, marked people: true; checked faces, hands and representation.
- Polish, general, flattest moment: Board now presents the student's mural, evidence and unresolved tradeoffs together instead of a generic success paragraph.
## Findings left

No confirmed blocker or should-fix remains in the checked paths. Nit, general: banner words remain artwork-sized in miniature views; Inspect provides the large view.
## Flattest moment left

Some Board topics offer one answer, so that step remains more evidence gathering than an argument. The exact cards are specified; adding alternatives would change the spec.
## Graphics

Checked fifteen paintings, all placed; retained the enlarged factory after confirming the bridge is removed. Replaced board-room only, using the built-in OpenAI image tool and art.py --rekey. Prompt: art/prompts.json. Final asset: art/board-room.webp.
Existing Beat Lab and Snowy Mail Route bundles were opened without rebuilding outside the allowed folders; side-by-side comparison is in Scratch. Rich paper surfaces and full murals are retained.
Bundle: 1516.9 KiB. New board art: 72 KB; fifteen paintings placed. All 110 audit PNGs were inspected, along with the targeted frames.
## Audit

One full audit completed in about 35 minutes, Chrome 9941 and host 8745, with a 2,400-second limit: 14 leads. Four confirmed fold leads were fixed (Board answers, bus recall, custodian Back, post-swap Board/Reset). Six welcome flags follow the required first-tap rule. Four resize flags were refuted by fresh selector/resize checks for Equal weights, Reset and custodian/Back; all pass with no exceptions. Dispositions: _scratch/school-wall-mural/review-audit-dispositions.md.
Layout frames predate the repairs, and later live-file walks may read rebuilt bundles while the iframe uses its initial copy. This is not a frozen final-bundle certification. Only repaired states were re-shot; the full audit was not rerun. Changes/Undo manifest coverage was extended for future audits.
Independent checks: all 16,383 weightings, all angles, enlarged angle, compound fading and contrast match; equal weights of 2 correctly total B 40, D 38, C 36, A 30.
Targeted assertions, save/reload/Reset and real mid-action resize checks pass. Bus Motion on/off measured 1712/1715 ms, and both interruption paths pass. Keyboard retains stepper focus; grayscale is usable; calm has no running infinite animation.

| Line | Kind | Expected | Spoken |
| --- | --- | ---: | ---: |
| newLeader | event | 10 | 10 |
| busAsk | event | 5 | 5 |
| busHow | how, five entries | 1 | 1 |
| boardDone | event | 2 | 2 |

Read works with Sound off and is released by mode/Reset; all 23 fixed lines match voice/lines.json. Narration remains browser speech, as recordings are outside this run.
## Left open

- Product-specific pigment certification is not established by a pigment code. [Golden's pigment chart](https://goldenartistcolors.com/products/golden-artist-acrylics/fluid/pigment-data) confirms several specified examples and product variation; the tool labels its grades/model and notes this limitation. The spec supplies no exact paint products.
- Paintings illustrate the stated model and are not calibrated scale drawings. A literal 40 cm swallow eye is a spec assumption, not a measurement from the image.
- The spec's equal-weight totals are weight-1 sums; its Equal weights control says 2. The exact sum-of-products rule is retained and the discrepancy remains documented.
- All testing Chrome/server processes are closed; host.html is absent.
- Process limitation: the cold opening pass did not exercise weight changes or move Summers to five before reading builder notes; those checks were completed afterward.
- The first guide-read commands completed promptly but lacked explicit kill timers. Subsequent shell commands used explicit limits. No commits; writes stayed within the two allowed folders.
