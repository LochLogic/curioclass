# Data Policy Council build handoff

## Cold review changes, 2026-11-03

This section supersedes the original build's portrait and compact-chip limitations below. The review inspected all six existing portraits for clear anatomy, respectful representation, age and style. They now appear on laptop council plates and in member cards; tight layouts retain names and open the painted member card. No paintings were discarded or redrawn. The owner has not yet approved shipment.

Compact day strips now show common record rules above the paintings, with AI-flag distribution labeled separately. Full-size chips use clearer abbreviations. The day footer explains each clause edit and distinguishes a changed count from changed rules on the same records. Unknown Blank moments now have truthful accessible labels. Reset clears the old selected-member outline. Voting with three pins no longer tells students to press a disabled Pin control.

The final audit confirmed a clerk line extending behind the next band on phones, plus clipping below laptop portraits in the math frame. The portrait dais now fits its content; math uses a compact day heading to retain the complete chips. Phones omit the duplicate clerk line because the panel and member/document cards already carry its information. The collection counter retains its full accessible label in compact views. A repeated unchanged preset tap preserves narration; reset after edits, a vote or member responses still works.

Review evidence lives under `_scratch/data-policy-council/review-*`. The final review report is `codex-review.md`. The one review audit completed with 20 leads: seven actionable leads were fixed and thirteen intentional welcome skips were retained. The audit predates the final scoped fixes; its affected frames and narration were rechecked without another full audit. Final math evidence is in `math-fit-complete-frames/`; all task processes were closed. Narration remains browser fallback because recordings are outside the authorized workflow. The supplied legal rules remain selected classroom constraints, including the spec's four blocking options, rather than a complete compliance test.

Built 2026-10-31 in `S:\CurioClass-codex`. Build only. No commits, deployment, or polish round.

## Files and layout

`src.html` starts from the kit starter's document, header, mode controls, stage, panel, and kit initialization. The scene uses real CSS pixel layout. It loads only the shared kit plus inline content and `art:` tokens. Readable sections hold styles, options, legal flags, members, day events, voice lines, pure model functions, rendering, and event wiring. The generated `data-policy-council.html` is the offline bundle. `tool.draft.json` intentionally remains a draft descriptor with stage built.

Nine new people-free paintings are in `art/`, with generation prompts and provenance in `art/prompts.json` and originals in `art/raw/`. Six pre-existing portrait WebPs and their pending-review entries were preserved. They are referenced by art tokens in member data, but displayed portraits remain faceless SVG silhouettes. No people were generated in this run.

Scratch contains the numeric recomputation, exhaustive browser checks, responsive and held-input scripts, frames, reference bundles, and audit evidence. Reference tools were bundled into Scratch to honor the write boundary. No reference tool folder was written.

## The model

`OPTIONS` contains all 22 options and the five supplied member point values. Draft values are numeric indexes 1 through 4, keyed L, R, A, S, E, F. Unset clauses use null. Hall-pass and lunch moments are always collected. Optional moments whose clauses are unset say clause unset rather than implying a settled collection rule.

`totals`, `flags`, `day`, `suggestion`, and `countPassing` are pure model functions. `countPassing()` returns `{passing:156, legal:576, unanimous:0}`. The independent Python check also verifies all source totals, member ranges and contrast ratios. Exhaustive browser checks validate all 2,304 drafts and 8,066 suggestions against point data parsed independently from the unchanged spec. Ties use clause order, then option order, and flagged alternatives are excluded.

## Interaction details

The day updates before scores and policy text. Option and navigation buttons are created once, so changing a choice never rebuilds the control under the pointer or loses focus. Arrow keys select within an option group; Tab moves among groups and actions. The panel comes first in DOM order, then the dais. Nothing takes focus on load. Dialog close restores focus with preventScroll.

The six clause selectors stay visible; one clause's option group is open at a time. This resolves the spec's scrolling-panel description against the newer rule that a short choice set must not hide options. In short landscape and phone layouts the options use two columns. At 760 wide the panel sits below the stage. Narrow day strips scroll sideways. Labels below 1,500 pixels use abbreviated chips, with full text in titles and the moment's accessible label. In compact stacked layouts the chips are hidden to preserve the scene and controls; the policy document still provides the full rules. This is a visible departure from the literal all-sizes chip description.

Read the draft opens all six numbered sections and their full flags. Ask the room stores every member's suggestion, opens the first dissenting member's card, and leaves all other responses available through their nameplates. A changed clause also updates one member's quotation beneath the dais. Members' words are displayed, never voiced.

On compact Compare desks the three pin cards sit side by side, so Load, Unpin, Clear pins and Back to Draft remain visible. All six choice summaries remain available in the stage's own scroll area. Dialog hints name Close immediately and return to the next policy action when closed. Dialog-opening first taps suppress the vendor welcome, which would otherwise name controls behind the modal. The Ask instruction was adjusted to name Close before choosing a suggested clause and option. Re-tapping the already-selected mode preserves narration. Resetting to Vendor proposal restores the vendor welcome's valid context.

Vote uses a cancellation token and five 600 millisecond roll-call steps after its initial 600 millisecond beat. Any changed clause cancels it immediately, clears revealed votes and results, and hushes speech. Pin during voting stores only choices. Pins are page-local snapshots, with no localStorage or network transmission. On the third pin, keyboard focus moves to Compare because Pin becomes disabled. Other controls remain active throughout a vote.

Show the math exposes all six clause values under each member's bar on wide screens. On screens 800 pixels or narrower it opens a member card instead, keeping small nameplates readable. The bars share a -12 to +10 visual scale with a Yes line at 2; the exact points are available in member cards. Extreme values outside the bar scale clamp at the edge, while the displayed total remains exact.

## Voice and motion

Uses `Curio.voice` with mode scope, explicit freshness checks and an owned synchronous hint. Read reads the current hint. Ask is selected with `V.heard` and is spoken once; flag, clear and vote-result lines are events. The vendor welcome expires after the first edit because its wording no longer fits. Compare has distinct empty and pinned welcomes. Clear never names a disabled vote control. Every voice line is in `voice/lines.json`, with bank news-reader / Rasalgethi. No narration was recorded; browser speech is the build fallback.

Motion off removes CSS loops, card lift, plate flips and bar transitions; the roll-call pacing remains unchanged. Kit tones accompany choices and voting. No student score, countdown, confetti or mascots.

## Open questions resolved

1. **Real laws or generic state law:** kept FERPA, COPPA and California's SOPIPA, as the spec leans toward a realistic California setting. The exact supplied flag texts remain intact. Notes explain selected-rule and contractor-exception limits; this is a classroom model.
2. **Portraits or icons:** kept all six portrait slots and pre-existing files pending owner review. This run follows the explicit no-people instruction and uses tasteful faceless silhouettes in code until the owner clears the portraits. No existing portrait was regenerated or overwritten.

## Engine changes wanted

None. Shared kit, documentation, scripts, reference tools, and other tool folders were not changed.

## Review boundaries

This is the build handoff, not an independent cold review or a polish round. The final report names any audit leads and literal-spec gaps without treating a mechanical check as a judgment of teaching quality. The owner can review existing portraits and commission narration separately. Do not interpret the lack of a legal flag as certification of an actual district policy.

One full audit completed in 1,472.8 seconds with 32 mechanical leads. It checked the preserved pre-fix bundle at `_scratch/data-policy-council/audit/host/tool.html`. The report answers all lead categories; native modal coverage and intentionally skipped stale welcomes are distinguished from actual defects. The one-audit instruction was honored. Final changes have a saved source diff and targeted geometry, held-click, narration and phone frames; the full audit is not represented as a clean audit of the later bundle.
