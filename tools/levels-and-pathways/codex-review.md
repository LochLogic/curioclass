# Codex review: levels-and-pathways
## Played
Cold as a K-2 child following cues and as a projecting teacher, before builder notes/source. Played all four modes,
wrong-answer replay, mixed-level drawn dance and all eight mysteries to the earned gallery. The floor ribbons are strong.
## Findings fixed
- Blocker, general, people art: replaced the code figure with three painted guides in one articulated atlas and
  one dedicated gallery bow. Main, mirror and button figures are painted; the studio, pose library, clock and trails stay.
- Should fix, general, Mystery: immediate level answers cut or dropped right-path praise. Preserve it before the next reply.
- Should fix, general, Mystery return: the hint named disabled Go. Give a return cue, then name Go when available.
- Should fix, family:dance, Draw: lock level/way settings during Dance it so the planned badges and actual ribbon agree.
- Should fix, family:dance, Draw: hide the previous performer and shadow when editing or replacing a plan.
- Should fix, general, input: cancel unfinished pointer drawings on mode changes, Clear and Surprise path.
- Should fix, general, hint: a late Clean floor fade could overwrite the next mode's hint. Guard its run and mode.
- Should fix, general, phone: hints fell below the window. Remove the phone hint's unnecessary minimum height.
- Should fix, general, Draw: lines crossed badge targets and phone badges overlapped. Reserve full targets, avoid ink,
  separate leaders from button bounds and pack four phone badges together; use spare panel space for a taller Draw stage.
- Should fix, general, voice: rapid repeated Middle/Low calls lost events. Interrupt old setting speech with each new event,
  followed by one short next-control cue. A same-mode double tap now preserves its welcome and current work.
- Should fix, general, Read: starting a move cut Read. Preserve Read priority for ordinary actions; mode/reset can release it.
- Polish, general, quiet preparation: immediate warm mat response and four larger count-in dots use the existing beat clock.
- Polish, general, gallery: painted bow and accurate scene description keep the earned ending readable.
## Findings left
- Polish, 375px four-part finish: the duplicate ribbon-end icon crowds Part 4's generous hit rectangle. The numbered cards
  remain distinct and the path is visible. This is the densest composition left after the bounded badge repair.
## Flattest moment left
Returning to the star is a short necessary wait. The cue now explains it; the preparation that follows has a visible beat.
## Graphics
Built-in image generation; full prompts in art/prompts.json and raw PNGs in art/raw. One three-guide atlas plus one bow
replaces 32 deferred pose requests. Both new assets have people true. The figure is swappable through PAINTED_CAST/paintDancer.
A fresh people-art reviewer passed the source cast, 36 articulated endpoints and bow; I inspected 48 gait phases,
the retained studio, mirror and icons in context. Natural skin/hair/body variety; no visible mobility aids in this small cast.
Seated-copy guidance remains. Final art 234.4 KiB; offline bundle 928.4 KiB on disk. Both bar tools compared side by side.
## Audit
**Audit not finished:** the only review audit stopped at its 2400-second limit during stress checks. Partial audit.md has
30 leads and 77 frames. No second full audit. Its snapshots precede the final repairs.
- Seven phone hint/keep leads: fixed; affected defaults, freeze, ribbon and level question re-shot with hints in view.
- Five Draw line/overlap leads: fixed in the drawing plans. Rechecks sampled 24 seeded plans at each of 1280, 1366, 1920,
  680 and 375 widths without overlaps/crossings. Real four-part drags passed at 1366, 680 and 375; phone finish caveat above.
- Two repeated-event leads: Middle and Low now start 5/5 calls at a held 2-second pace; next-control cue starts once.
- Four quick mode-tap leads: one complete welcome, no cut, in each mode after the idempotent mode fix.
- Eleven missing-welcome leads after action-first taps: expected action speech priority under STANDARDS. Keep the action's
  own call; do not insert a late premise. Short, once-per-mode next-control cues address what to do next.
- One resize disabled-label lead: different random plans produced different accessible names. Seeded the fixture;
  actual 1366-to-760-to-1366 resize preserved the same parts and Enter-twice focus, with no exception.
The four-part audit fixture lacked a return expression during that run. Corrected it and verified real drags separately;
its original blank frames are not coverage. All audit frames and final affected frames were opened and inspected.
Every STANDARDS size, all modes, 375px iframe, Motion off, grayscale and keyboard-only Draw were checked before the audit.
Held voice checks: Stretch 5, atMiddle 5, copyMe 1, freeze 1; fast Mystery replies both survive. Read continues with Sound
on/off; with Sound on it finishes before the next full eight-count move. A mode change releases Read immediately.
Recomputed 18 move/level pairs, 36 endpoints, 40-count High/Middle/Low/Middle/High routine, 16-count trips and 8-32 drawn
counts; actual drags covered straight, curved, zigzag, tiny and four-part paths. Highest Low head is about 0.563 body heights.
Final bundle and inventory checks pass: 47 runtime strings match voice/lines.json, no external src/href dependencies,
required notes headings, no em dashes, people flags present. Final focused driver batches logged no browser errors.
## Left open
Six lines use browser speech fallback; existing recordings stay, no audio recorded. Sound-off Read uses a conservative
speech-length estimate because kit exposes no completion event. A kit event would make that wait exact across voices.
Shared readPath retains its documented small-stage limit for very squeezed/shaky compound waves; no kit thresholds changed.
The kit stores its Motion preference; no dance, progress or drawing is stored. No classroom trial or second full audit.
No kit/spec/catalog edits or git commits. Work stayed within the two authorized directories; own Chrome/server closed.
