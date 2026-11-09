# Code Kitchen handoff

Built by an earlier agent; cold review completed 2026-11-08, without commits. See codex-review.md for current findings.
For another cold review, follow CODEX-REVIEW.md's play-before-maker-reports order.

## Structure

src.html starts from the kit starter. CSS uses real viewport layout, an editable lined card and a painted station.
The panel precedes the card in DOM order for keyboard use. On phones the station folds into a shallow strip.
The line model is {kind, name, args, depth}: assign, def or call. __tool.line exposes constructors for tests.
The safe expression parser accepts whole numbers, quoted text, True/False, names, str() and +. It never evaluates JavaScript.
The runtime uses explicit call frames and local dictionaries, stopping at 20 nested calls. Each kitchen action waits 350 ms.
Menu mutations update tickets and start a fresh edit counter. Undo restores card and counter together.
Open kitchen and level progress use separate localStorage keys with try/catch.

The Add a line drawer first chooses a kind, then configures the whole line before insertion. This makes an inserted
add_topping("banana") one edit for D12. Indent is inherited from the selected line; use Outdent for a call after a body.
The editor preserves the actual input node when a slot changes, and line/level selection updates classes in place.
The rail is horizontally scrollable on phones, and the latest jars stay visible in the station strip.
Compact screens use the Levels dialog instead of showing the entire twelve-dot strip in the panel.

Kitchen argument ranges apply to each call. Two valid pour_pancakes(8) calls produce sixteen pancakes and a wrong plate,
not a false type or range error. Stacks beyond eight compress their spacing so all cutouts still fit.

## Timing edge case

Forty straight executed lines take about fourteen seconds at 350 ms each. A forty-line source card that reuses procedures
can execute many more than forty lines. Such a run can exceed fourteen seconds. Kept the specified per-line timing;
Cook, Step, Stop, editing, level selection and mode selection remain live. No false infinite-recursion error is used
to cap an otherwise finite program. A genuinely recursive chain still stops at twenty nested calls.

## Open question decision

Accepted the spec's leaning: made all thirteen additional painted kitchen cutouts, with no people,
and preserved the existing diner-pass painting. Full prompts and provenance are in art/prompts.json.
Built-in imagegen generated each asset separately. Originals are copied to art/raw and only art.py --rekey processed them.

## Engine changes wanted

None. No kit, script, documentation or other tool source was changed.

## Follow-up

Read codex-review.md for the cold review's measured checks and remaining limitations. No narration was recorded.
The browser's installed voice is used, so the intended Umbriel timbre cannot be guaranteed by lines.json alone.

The one full mechanical audit finished with 34 leads. Default sizes, calm mode and resize stress were clean.
Build repairs addressed compact forms, sticky primary controls, in-place line focus, five fresh error events,
and a welcome interrupted by Restart. Focused follow-up checks passed; the full audit was not repeated.
Native dialogs intentionally cover the background card and rail. audit-states.json now keeps their foreground
dialog instead of requiring the covered background to remain unobscured.
The audit's missing-welcome flags for first Cook, Step and C7-C9 are expected first-action suppression.

## Cold review changes

Menu transitions clear Undo history. Keeping old snapshots allowed a pre-written changed-menu answer to be restored
with zero counted edits. changeEdits records each phase; D12's ring requires both rated changes to meet par.
Saved par flags need parVersion 2. Older served dots remain, while older rings are re-earned under verified rules.
Pantry excludes assignments local to other recipes. New fixed voice lines cover incomplete runs, saved kitchen,
ticket forms and line composition. Dialog close restores its prior hint and drops instructions for hidden controls.
The pass now names the actual served food and summarizes the student's orders and measured changes.
The syrup was redrawn with built-in imagegen as a thin amber glaze; original art is preserved in Scratch.
Compact Cook starts and level selection restore the panel to its top, so the sticky controls cannot cover the edit counter.
Completed short-landscape runs expose Levels beside the primary controls. Open kitchen shares Cook's row with New ticket
at those sizes, keeping Add a line and Pantry visible. The Manager's note is a named nonmodal dialog; closing it returns
focus to Cook without scrolling. A changed menu clears the old plate and its success message.
Step, Ticket sets and Clear saved have their own once-only instructions. Stop and an actual error edit hush stale error speech.
The single cold-review audit completed within its 40-minute limit, with 89 leads assessed and 75 frames inspected.
Compact layout, current-menu feedback and contextual voice fixes received scoped rechecks in Scratch's review-audit-fixes/
and review-voice-final/. The final verification manifest is _scratch/code-kitchen/review-verification.json.
