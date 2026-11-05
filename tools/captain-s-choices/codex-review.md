# Codex review: captain-s-choices

## Played

Cold Grade 9 solo season before builder notes/source; six dilemmas, four circles, season card. Then a projector-style keyboard season.
The chat and returning-player epilogues carry real weight; the supplied choices make the prosocial path conspicuous.

## Findings fixed

- Should fix, general, opening: mixed-team/self-officiation context vanished when choosing skipped the welcome. Visible premise and Read now retain it.
- Should fix, general, keyboard: Enter on a different focused card committed an earlier selection. Focused card now previews correctly; real Tab/Enter verified.
- Should fix, general, discussion: closing its Read left speech playing after the dialog. Close now hushes narration and restores focus.
- Should fix, general, compact chat: new replies could remain below old messages. Redrawn larger screen, refitted overlay, compact header and immediate reply scroll.
- Polish, general, spirit circles: consecutive Harbor/Granite cards skipped the narrative bridge. Fixed-result transitions and specific Next labels establish Granite's loss and upcoming chat.
- Polish, general, season: added the fictional-assessment boundary and visible no-save/no-send statement.

## Findings left

- Should fix, general, spec choice design: several first choices improve the same dial as the second option while avoiding its social costs; all-a is the conspicuous desirable path.
  The spec promises tradeoffs/no right answer but supplies those exact effects and outcomes. Revising them would change the spec; left unchanged as required.

- Polish, general, narration: no recordings. Browser fallback is functional; the build/review rules prohibit recording audio.

## Flattest moment left

The four spirit circles still repeat the same rating grammar. Granite now has context; deeper choice tradeoffs require a spec revision.

## Graphics

All seven paintings inspected in scenes; three cutouts checked on magenta. No people, faces, stereotypes or missing art tokens.
Weakest asset was the phone: too much bench around a narrow screen. Redrawn with built-in imagegen; prompt/provenance in art/prompts.json.
Final phone: art/raw/phone.png -> art/phone.webp via art.py --rekey phone. All strong fields, jerseys, clipboard and bus retained.
Existing Beat Lab and Snowy Mail Route bundles opened read-only; finish retained without changing the scene's style.
Art totals 497.3 KiB; offline bundle 1,007.1 KiB. All seven art tokens resolve. No network resource references or em dashes.
Verified contrast ratios: coral/panel 7.74:1; coral/secondary 7.34:1; dark jersey letters/coral 8.04:1; hint/panel 10.95:1.

## Audit

One audit completed within the 40-minute bound; no rerun. Evidence: _scratch/captain-s-choices/review-audit/audit.md.
Eight leads triaged against the frames and narration logs:

- One grammar false positive: "Game 1 ends" correctly uses a singular verb.
- Three first-choice welcome skips: required immediate selection hushes the intro; the premise now stays visible.
- One Start over welcome skip: reset speaks the chapter event and retains the visible premise.
- Three quick-tap pick-instruction cuts: commitment makes that instruction stale; Next becomes the current instruction.
No confirmed fault remained from these leads. Sizes, all 17 states, console, targets, Motion off and resize stress were clean.
All 65 audit frames inspected in review-audit-sheets, plus full-size targeted frames. No post-audit source change or second review.
Independent Python arithmetic covered 729 paths and 2,916 circles; browser checks passed 235 assertions across four complete paths.
All-a dials 10/7/10/8, spirits 11/10/14/13; all-b 1/9/0/1, spirits 10/10/6/8. Both 6c endings and clamp wording checked.
Real CDP digit/Enter season, repeated-digit preview, focused-choice regression and reload clearing passed.
WFDF receiving-foul wording and spirit categories/scale independently checked against primary sources linked in notes.md.
Teacher notes retain the required three opening sections and practical home activities.
All standards sizes, all listed states, grayscale, Motion off, modal focus and held-click voice frames were inspected.
Wave lessons checked: immediate hints/Read, stable controls/focus, 44 px targets, complete choice sets, explicit story-model assumptions,
no pre-commit effects, truthful fixed scores, no hidden diagnostic states, no color-only meaning, and SHAPE.S3 practiced by the student.

| Voice check | Expected | Spoken |
|---|---:|---:|
| Chapter 1 event, five held resets | 5 | 5 |
| Intro, uninterrupted plain first tap | 1 | 1 |
| Pick instruction, uninterrupted welcome | 1 | 1 |
| Next instruction, first consequence | 1 | 1 |

Five held clicks at two-second pace were clean for every speaking control; quick-tap cuts are triaged in the final audit entry.

## Left open

No shared-kit edits or commits. Repository writes stayed inside the tool and its Scratch folder. Owned Chrome/server processes closed after each check.
No face art added: the spec explicitly requires the jersey cast and no faces.
The drive.py HTTP wrapper requested a missing favicon; that 404 was outside the bundled tool. Audit console checks were clean.
