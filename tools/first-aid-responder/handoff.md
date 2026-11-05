# First Aid Responder handoff

## Cold review update, November 3, 2026
The cold reviewer first completed six scenes, five guide cards and a real two-minute CPR round before reading this file.
New painted fa-manikin replaces the silhouette; fa-field now has the blocking sled and shade tent, and fa-kitchen has
the pan. The cafeteria sign lettering was removed while retaining its composition. These were generated with the built-in OpenAI image tool.
Production descriptions, provenance and the
body-form people flag are in art/prompts.json; originals are in art/raw/. Earlier Art and Validation sections are history.

Accepted steps now fly to their slots without delaying state changes. Motion off skips the flight and keeps the clock.
Phone scene clock, ghost and three action buttons move into scene-utilities before the rail. restoreSceneControls moves
them back to the permanent panel before destroying a scene; resize moves the same nodes, retaining their handlers.

CPR summaries persist during subsequent free practice, clear-records and mode returns. practiceAfterSummary distinguishes
the live free-practice trace from the retained round statistics. Only Start replaces the summary. Read includes it.
Coaching validity checks the exact current instruction and Coach voice setting. Long trace gaps are disconnected.
Every rounded percentage result is now declared in allLines and voice/lines.json. There are still no recorded clips.
The clock rounds tenths before splitting minutes, preventing a 0:60.0 display. Compact trace axis labels are separated.

The single review audit completed with 37 leads and 98 frames, without runtime or resize errors. Its confirmed phone
finish-button clipping was fixed with tighter card spacing; compact hint text and gauge spacing were corrected.
The compact rail's intentional ellipsis is explicit, with full action text in its title and completion list.
Clear now owns a valid dialog instruction and restores the prior hint on cancel; Sound reserves its header width.
Post-audit evidence is in review-exit/ and exit-phone-finish-*.json. There is no second full audit.

Focused functional evidence, frames, source checks and the one review audit live in _scratch/first-aid-responder/.
The source/spec disagreements below remain: do not claim every Done when passes. Current Red Cross gauze qualifications
and the incomplete seizure 911 list require a spec decision. AHA 2024 was retrieved in this review; the old retrieval
limitation below no longer applies. No engine changes were made.

Build only, October 31, 2026. No commits, shared kit changes or deployment.

## Source map
`src.html` uses the shared kit and 9-12 theme. Its CSS defines the school response desk, compact preview, and phone layout.
The scene data contains the complete supplied actions and reasons, plus compact display titles. `openScene` builds a shuffled
deck once per attempt; `choose` retires cards in place and fills the rail without reshuffling under the pointer.
`finishScene` saves eligible records. `updateScenePanel` replays the captured prior best, so setting a new best does not move
the opponent during the current attempt. Shared ranks are accepted from the lowest remaining rank.

CPR uses `compress`, `startRound`, `endRound`, `coach`, `drawTrace`, and an ahead-of-time Web Audio metronome.
`Curio.voice` owns speech priority, Read, how-line memory, stale checks and the test log.
`window.__tool` exposes state, actions, data, narration log, median and a deterministic scheduler probe for validation.
`far-best` holds validated scene records and one best full CPR trace, with try/catch around every storage access.

## Open questions resolved for this build
1. Leave opioid overdose out. The six-scene content and picker are the spec's concrete lean; adding a seventh would extend the taught scope.
2. Keep Timer On by default, following the race/ghost specification and its Timer Off alternative. Every run requires accuracy to finish.
Timer Off is one tap away and permanently disqualifies that attempt from saving, including if it is switched back on.

## Art
Six pre-existing school paintings were retained. Two new images were made with the built-in image tool: `fa-aed` and `fa-kit`.
Their complete prompts and provenance are in `art/prompts.json`; raw originals are in `art/raw/`.
Rekeying uses only `scripts/art.py --rekey`, with holes and despill enabled to remove magenta edging.
`fa-manikin` is marked `people: true` because it depicts a body form. The required token is reserved, and a code-drawn
faceless training silhouette currently supplies the pad. Owner-reviewed replacement art remains outstanding.
The existing field image has a school lawn and cooler rather than the spec's blocking sled and shade tent.

## Content discrepancies for the next reviewer
- The actual five-interval median does not guarantee an always-in-band needle at 30 ms jitter.
  Scratch/numbers.json records 99.54% minimum in band after five warm-up intervals across 200 seeded rounds, with an occasional 122.23 reading.
  At 50 ms the recomputed minimum is 94.91%, and at 80 ms it is 84.26%, below the spec's 98% and 87% claims.
  Keep the real calculation; do not clamp it to make the check appear to pass.
- Current Red Cross bleeding guidance permits another gauze pad but cautions against stacking multiple pads.
  The supplied scene's more general add-cloth wording remains intact and needs owner/spec reconciliation before release.
- Current Red Cross burn cooling range is 5 to 20 minutes, so the spec's at-least-ten-minute action is retained.
- AHA full 2024 first aid and the supplied CDC heat URL could not be retrieved. AHA 2025, Red Cross CPR/choking/bleeding/burns/heat,
  and CDC seizure pages were checked. Sources are linked in notes.md.

## Validation evidence
All temporary scripts, numeric checks, browser result JSON, frames, Chrome profiles and audit output are in
`_scratch/first-aid-responder/`. The report records the final checks and any remaining failures.
No recorded speech was made. The voice manifest specifies firm-captain; the browser voice is the current fallback.
The first native HTML drag failed in `drive.py`. It was replaced with pointer capture, a floating card copy,
and explicit rail hit testing. The real whole-pixel drag now places a correct card, while a wrong drag adds exactly one penalty.
Mode switches cancel a pending drag. Taps and keyboard placement also pass.

## Build fixes after the single audit
The audit reported 47 leads and finished within its time limit. Its full output and all 82 frames are in Scratch/audit.
Targeted checks cover the later fixes; the full audit was deliberately not repeated.
Compact gauge labels were enlarged, focused-card hints shortened, completion controls brought into view, and phone hints
moved into a reserved header row. Phone summaries scroll into view after a round. Re-tapping an already open mode preserves
its welcome and current work. The gauge hides its needle until a rate is measurable.
Phone Timer, Restart, All scenes and Clear remain below the primary scene list; these utility controls require vertical scrolling.

## Engine changes wanted
None.
