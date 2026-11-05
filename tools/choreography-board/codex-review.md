# Codex review: choreography-board

## Played
Grade 7 solo walkthrough before reading builder notes: starter playback, revision, split Compare, Ghost, phrase making/saving and complete Show; then projector and keyboard checks. The theater and synchronized revision were strong; the provisional figures and buried choices weakened them.

## Findings fixed
- **Should fix, family:dance, src.html/art:** replaced the code performers with a natural range of four painted dancers, preserving costume colors, badge shapes, timing, floor registration and the isolated renderer adapter.
- **Should fix, family:dance, grounded rendering:** the first articulated painting distorted low and waist-bent bodies. Following the owner's correction, painted complete curl, kneel, crouch, sit, lie, roll and bow poses for each dancer. Corrected the fourth bow's prosthesis side. Fresh people-art review passed.
- **Should fix, family:dance, movement data:** Push and pull used an ordinary lunge without the push; Leap across repeated one running leg position. Added the extended push and alternating running keyframes.
- **Should fix, general, Build/editor:** short choice sets disappeared in long scrolling panels. Added persistent section navigation, compact native choices and one visible move group at a time. Play and the eight initial device buttons fit the checked sizes.
- **Should fix, general, Compare:** reasons were buried below measures. Separated Before, Measures and Reasons; compact reason selection and notes fit. Explicitly hid collapsed version-list content, eliminating phantom overlap boxes.
- **Should fix, general, device options:** selecting an option reset scrolling and hid focus. Preserved focus and provided compact Device/Device option pickers so choosing an option does not hide the other device choices. Meanings and the next action remain in the hint.
- **Should fix, general, history/voice:** History's instruction named unavailable Undo/Redo controls. Reworded it; section changes now update hints immediately and stop stale speech. All 31 fixed lines match the voice manifest.
- **Should fix, general, history:** Go back to Before failed to record a version when the dances matched. It now appends a version. Clear saved removes storage and returns focus to Play; empty-stage guidance names Phrases.
- **Polish, family:dance, artwork adapter:** repaired neck registration and repeated-thumbnail clip IDs; shared atlas references avoid copying large image strings into every cached icon.
- **Polish, general, Show:** the ending felt generic. Its closing title now names the student's phrase/count total and chosen devices/reason, with a complete painted bow. Fixed singular wording.

## Findings left
- **Polish, family:dance:** complete grounded paintings change on count boundaries. Continuous floor transitions and additional facing/energy variants remain less detailed than upright movement. The fourth dancer's physical prosthesis is preserved rather than mirrored with the whole sprite.
- **Polish, general:** narration still uses browser speech. Hero-coach recordings remain unmade, consistent with the instruction not to record audio.

## Flattest moment left
The holds between complete floor paintings are more abrupt than the continuous upright rig. They preserve natural anatomy and readable count shapes; the stage, music, canon and playhead keep their timing.

## Graphics
Kept the warm theater, lighting, proportional timeline and detailed studio styling. Added three people:true atlases with the built-in image tool: four upright dancers in front/back views plus seven complete poses per dancer, 36 registered views in total. No unmade art tokens remain.
Prompts and provenance: art/prompts.json. Finished paintings: cb-dancer-cast.webp, cb-grounded-cast.webp and cb-floor-bow-cast.webp. Whole-body poses and upright registration remain easy to replace without changing choreography data or clocks.
Inspected the paintings at stage/thumbnail sizes, including grayscale and the final Lie palette path. People review: _scratch/choreography-board/people-review.md. Compared the finish with Beat Lab and Snowy Mail Route.
Final bundle: 1,852,639 bytes, 1809.2 KiB (1.77 MiB).

## Audit
The single audit completed within its 40-minute limit, using Chrome 9931 and host 8735. It reported 113 grouped leads. All 97 audit PNGs were inspected in 13 contact sheets.
No audit console errors, small-target findings, resize exceptions, stuck controls or infinite Motion-off animations. Held-click focus/Enter paths and all speaking-control five-tap and quick-tap checks passed.
Confirmed Compare and option-visibility leads were fixed. Expected leads are proportional timeline/count-slot scrolling, panel hints hidden by Show or its inert confirmation dialog, first-tap welcome suppression for a control's own instruction/music, and idle Show Stop doing nothing. Closed-details overlap reports were not painted overlaps; explicit hidden state also removes their DOM boxes.
Every audit row has a disposition in _scratch/choreography-board/review-audit/dispositions.json. Twenty latest targeted layout inspections passed, leaving only intentional timeline scrolling. Final targeted batches had no console errors. The full audit was not rerun after the scoped repairs.
Independent arithmetic and browser checks confirmed 38-count maximum blocks, 7-count double-time/canon blocks, the 96-count limit, starter/maximum run lengths and Rise's dancer-count recount before/after Retrograde and Half time. Specified text contrast pairs exceed AA.

| Voice line | Kind | Expected over five taps | Spoken |
|---|---|---|---|
| Mirror explanation | how | 1 | 1 |
| Over-limit refusal | event | 5 | 5 |

Saved reasons/notes survived reload; returning to identical Before, Clear saved and empty guidance passed targeted checks. Evidence is in post-audit-verification.json, semantic-final-frames and compact-native-frames under Scratch.

## Left open
Grounded transition/facing fidelity and recorded narration above. No kit changes, commits or deployment. Test Chrome/server processes were closed and host.html removed. This was one cold review and one full audit, followed only by repairs and targeted re-checks.
