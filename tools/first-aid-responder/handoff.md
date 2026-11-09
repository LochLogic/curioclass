# First Aid Responder handoff

## Current fix, November 4, 2026
The merged round 1 list is refine.md. This fix changes only this tool and its scratch folder.
Before and after evidence is in _scratch/first-aid-responder/fix-before and fix-after.
See polish.md for per-item outcomes, cheats and the single final audit.

## Source map
src.html contains the CSS, six scene data records, mode renderers and interactions.
openScene shuffles once; choose accepts the lowest remaining rank, retires cards in place and adds mistake penalties.
railMarkup sorts ranks for slot grouping, with a single bracket on desktop and repeated position labels on phones.
The burn now has six steps because the accepted refine adds early adult notification while keeping the provider check last.
finishScene shows both Never do reasons even for perfect runs. updateScenePanel replays the prior ghost's stamps.
The more visible Ghost marker is labeled and advances along the rail; a first best says it is ready for the next race.

## CPR scoring and state
The gauge normally keeps the median of five intervals for jitter tolerance. Two outliers in the last ten intervals
(outside 440 to 700 milliseconds) expose a repeated burst/wait pattern: if the five-interval mean is outside the band,
the gauge and coach use that mean. One stray tap still gets median smoothing. A pause over two seconds clears the needle and window.
The round score uses elapsed time, not compression count: median and mean rates must be in band, each credited interval
must be 440 to 700 milliseconds and receives at most 600 milliseconds. These are tool scoring guards, not clinical thresholds.
Leading and trailing inactivity reduce the score; pauses over ten seconds disqualify a ghost. Partial rounds cannot save.
Saved CPR ghosts use scoring: time-v2; old tap-based scores are ignored. Scene records retain their existing format.
Only Start replaces a finished round's summary and trace. Reflex taps and mode returns preserve both.
Space works on entry and after Stop because focus goes to the chest, with preventScroll.
Coach pause speech requires a running round and at least one compression. It is silent during free-practice pauses and dialogs.
Metronome starts on; a strong completed round suggests turning it off next time. Sound Off stops scheduled oscillators.
The trace covers 80 to 140, with explicit too-slow/too-fast words and a taller band.

## Narration and access
Curio.voice supplies welcome priority, how-line memory, Read and stale checks. Fixed lines come from L and allLines().
voice/lines.json must match allLines word for word. No audio was recorded during this fix; browser fallback remains.
Pointer choices keep their feedback. Keyboard choices can move focus, but Read still explains the last choice.
finishRead uses full action sentences and reasons; summaryRead uses spoken units and names pauses, without DOM text concatenation.
window.__tool exposes the state, actions, scene data, line manifest, voice log and deterministic metronome probe for checks.

## Facts settled from live sources
Red Cross bleeding guidance keeps the original pad, allows one more and rejects stacking multiple pads.
AHA/Red Cross 2024 supports direct pressure and trained tourniquet use for life-threatening limb bleeding.
Calling for help shares rank with gloves. Seizure unknown history calls immediately; first seizure, injury, breathing
or waking difficulty, recurrence and duration also appear in the scene and guide. The nurse is requested while staying.
The guide additionally names water, pregnancy and diabetes with loss of consciousness, following CDC.
Exertional heat stroke uses neck-down cold-water immersion when available, with cold towels and ice packs as fallback.
Links and the live source-check date are in notes.md and polish.md. Earlier report conflicts are historical, now settled.

## Sensitivity
Health practice is neutral and non-graphic. The merged settled call says baseline rule 5 does not apply.
Teacher notes acknowledge students who have witnessed an emergency or death and offer the other modes.
The tool is practice and awareness, not certification; its existing footer and local-storage privacy statement remain.

## Art
The existing nine painted assets are retained. Their prompts and provenance are in art/prompts.json, originals in art/raw.
The painted manikin remains marked people: true because it depicts a body form. No new people or art were generated.
The chest target, gauge, trace, cards, ghost and rails are drawn in code. Motion off removes movement, not time.

## Open questions
The spec's overdose scene and timer-default questions remain open. This fix adds no seventh scene and keeps Timer on.
There was no unattended question needing an answer: accepted refine instructions settled the content changes.

## Engine changes wanted
None.

## Final verification
The single mechanical audit finished with 42 leads and no runtime, resize or repetition failures.
It predates three scoped follow-ups: compact bracket spacing, compact completed-summary space, and the repeated-outlier
gauge guard confirmed by two more meter cheats. Targeted final evidence for all three is in fix-exit/.
The bracket has zero measured overlap at 680, 1366, 1920 and 375 wide, including the phone burn's split shared group.
At 680x425, completed summaries hide the redundant clock and coach box so the entire result fits. Active rounds keep them.
Pointer retirement deliberately lets focus leave a used card; native Enter still transfers focus to another usable card.
polish.md records every audit lead, the final bundle size, retained optional nits and the exact before/after numbers.
