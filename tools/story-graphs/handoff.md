# Story Graphs build handoff

The readable src.html starts from the kit starter and inlines tool CSS, then the content token, state, voice queue,
renderers and interaction checks. content.json is the only tool data file and is inlined by the bundler.
kit:curio and kit:graphing are unchanged. Graph geometry, snapping, dragging and point nudging use Plane.

Progress stores round state and terminal marks under curio-story-graphs, wrapped in try/catch.
Clear graph and Undo never reset a round's check count. A terminal mark cannot be promoted by later practice.
The one-pick graph and one-tap meaning locks are independent from DOM disabled styling.
Clear progress uses one keyboard-accessible confirmation dialog, with a safe Keep progress default.

Scratch contains generation/build helpers, all number and adversarial checks, screenshots, contacts and audit evidence.
Do not ship Scratch. Every required illustration is registered in art/prompts.json; people assets are marked people: true.

## Decisions and spec discrepancies

- No owner questions are open in the spec. This run is unattended; no question was sent.
- The current build brief and user require the image tool, superseding the older Gemini-only and do-not-draw wording.
- Narration is browser speech through Curio.voice. No recordings were made, as required by Build only.
- The source spec rounds gift-card depletion to 11.4 smoothies. Exact computation is 80/7, and actual whole purchases stop at eleven.
- Preview space folds art as specified. Small-screen meaning cards may scroll inside the stage while the equation stays visible.
- Shuffled orders persist with an in-progress round, so reload cannot reroll a locked pick. Play the set again reshuffles.
- The user says to stop when codex-report.md is written, while CODEX-BUILD requests an early report.
  Working report notes stay in Scratch; the final report write is the last build action.

## Sensitivity

Fictional everyday stories feature Lucia, Maya, her grandfather and an older neighbor. The word abuela is used for
grandmother in Lucia's story. No historical or cultural claims are made. People-art review should check consistency,
age-appropriate poses and respectful depiction. A dedicated fresh people-art check is recorded in Scratch.
That check passed all 46 final assets: 14 with people, 32 without. The sprint continuity redraw also passed.

## Engine changes wanted

kit/graphing.js, point(), pointerdown focus: use focus({preventScroll: true}) instead of plain focus().
The tool uses a fixed viewport, so this did not require an engine edit, but the shared method can scroll embedded pages.

scripts/audit_tool.py, Audit.key()/drive_keys(): accept printable digits, or add a text-input step using CDP Input.insertText.
The audit stopped at KeyError: '1'. The tool-local state fixture now uses input events for this unsupported typing step;
all clicks remain real, and actual typing was independently checked by the full Model walk.

The audit's iframe context lookup also failed on the 375 host. Separate hosted phone frames and voice walks passed.

## Next review

The cold review is recorded in codex-review.md. Source, fixes and independent evidence remain in the permitted
tool and Scratch folders. The next blind lenses should use that report's Sensitivity and Left open sections.

## Cold review changes

Review kept the comic notebook and all 46 illustrations. Toss's ball was redrawn with the built-in imagegen tool
at a useful final-size scale, with the original yard as reference; prompt and raw source are in art/.
Sketch now reports starting position and relative rates across pauses. Its row checks localize the condition that
failed while keeping the same acceptance rules, check budget and immutable saved marks.
After a failed Match or Sketch check, the hint explicitly asks for a correction before the second Check;
Read uses that current instruction. Compact comparison space fits the longer diagnostic read-backs.
Check-result voice events interrupt stale instructions, so the result starts with its on-screen outcome.
The two Match success/show lines are shorter so Next story's how-to can start at a two-second action pace.
The summary retains counts and adds each story's title and saved mark, making the notebook a personal recap.
Numbered Sketch selectors now avoid point handles and use thin dotted leaders when displaced. Real jittered drags
and a nine-point phone sketch confirmed every point center remains available. Piece Enter, grid arrows and Undo
stop playback; its progress clamps to zero to prevent an early-frame negative piece index during resize.
The right-edge and nine-point refusal hints name possible actions. Backward-time narration is marked used only
after it starts, with a per-work voice key; Sound off consumes no warning. General tag guidance remains valid
after automatic selection moves to another piece. Wrong-pick transitions hush speech about the previous controls.
Compact Model's shown note compares numbers with the story, because its graph folds away at that size.
The locked-pick audit fixture now chooses the backward-time variant consistently. A separate correct-tag fixture
preserves that coverage without comparing two random fresh-page branches during resize.
The one completed review audit found 50 leads. Scope-specific rechecks followed its repairs; the audit was not rerun.

## Build cleanup history

The builder reported that its assigned Chrome debugging ports stopped responding and host.html was removed.
It reported that port 8775 still responded with the Story Graphs tool directory. It could not identify the listener PID:
process inventory through tasklist and Windows CIM was denied, while netstat exposed no listening owner.
Do not assume the local host stopped. See _scratch/story-graphs/cleanup.json. The Scratch host harness now
keeps the direct server process handle for termination in future runs; this could not recover the old handle.

The cold review used only Chrome 9960 to 9967 and host 8765. Its own processes are checked separately in
_scratch/story-graphs/review-ports.json; it did not inspect or stop the earlier build's unassigned listener.
