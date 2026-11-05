# Codex report: poem-to-movement

## Built

Offline grades 3-5 tool with six poem, painting and sound sources; 4-6 selected details become an editable dance.
Source, Moves, Map and Viewer use the shared dance engine, with thirteen verbs, four qualities, live edits,
reordering, drawn pathways, a numerical Viewer, partner guessing, revision guidance and local saved work.
The stage has four original painted images, directional light, a temporary kit dancer, count cues and synthesized sound.
All authored files stay inside the two permitted folders. No commits, branch changes or polish round.
Final bundle: 997,177 bytes. Chrome 9990/9991 and host 8795 were closed; temporary host files removed.

## Numbers check

Independently recomputed before implementation: `_scratch/poem-to-movement/numbers.txt`.
All six defaults are recognized. Runner-up margins: Wind .50, Train 1, River 1, Storm .75, Rain 1.25, Drum .75.
There are 21 nearest-profile ties among 96 homogeneous phrases. River revisions reach Storm or Rain at distance .25.
Four/five/six-card dances last 10/12.5/15 seconds, plus a 2.5-second count-in.
All seven specified contrast ratios match: 8.39, 7.79, 14.83, 6.14, 13.09, 12.20 and 15.97.
Poem punctuation and Rossetti's printed "thro'" variant follow the source edition; details are in handoff.md.

## Feel check

Played the source-to-dance-to-Viewer sequence, including wrong guesses, revisions, drawn paths and partner guessing.
Best moment: a river phrase danced with storm qualities receives the storm guess, then two move outlines point
to qualities worth revising. The result follows the visible movement and gives the next edit a purpose.
First flat moment: the bare studio lacked atmosphere. Added the fourth painting, an empty sunlit studio,
and separated the move caption and counts from the moving dancer.
Second flat moment: a long drawn curve repeated as complete trips. Changed it to continuous travel split among
the traveling cards, so a phrase traces the student's whole route.
Comparison: `_scratch/poem-to-movement/feel-comparison.jpg` places the final studio beside Beat Lab.
The paintings and material controls give the scene comparable richness. The kit figure is visibly simpler;
the owner explicitly requested it temporarily, with painted dancers as the destination.

## Done when

1. PASS: Moves/Viewer dancer foreground and visible Play at 1366x768, 680x425 and hosted 375 wide.
   Size, caption and phone frames inspected; final count/caption checks show no dancer collision.
2. PASS: all six defaults and both River-to-Storm/Rain examples pass the independent model and browser checks.
3. PASS: live edits apply on the next count and Stop is immediate. Forward and backward live reorder also continue correctly.
4. PASS: real S and zigzag pointer drags classify correctly and produce matching map symbols.
   Start X, arrows and stationary circles inspected, including the final Rain map; map survives a fresh load.
5. PASS: event checks find no Viewer result speech during the dance; result events follow completion.
6. PASS: all 21 computed ties are retained; Wind/River tie is named and both cards marked in the inspected Viewer frame.
7. PASS: Motion off holds a pose between counts without changing phrase duration; grayscale and calm frames inspected.
8. PASS: highlights, move edits, drawn map and closing sentence survive reload; tested again with a fresh map load.
9. PASS: held-input run at two-second tap pace produced five result events for five Viewer plays and how lines once.
   Evidence: `voice-results-first.json`, merged `input-results.json`; 75 runtime voice lines match the manifest.

## Wave lessons

- Hint and voice: PASS. State hints change immediately, Read uses the current hint, how lines use heard state,
  held-input voice checks pass, and first actions execute immediately.
- Focus and layout: PASS. Keyboard creation, Space play/stop and Alt-arrow reorder pass; partner reveal restores focus.
  Focus survives edits; final card labels, numbers, map status and captions have separate bounds.
- Sizes: PASS for target size and unclipped hints. Full STANDARDS sweep and hosted phone inspected;
  final poem targets measure 44 pixels. Secondary vertical scrolling remains below.
- No giveaways: PASS. Partner choices conceal the source and model result until a choice; conceal/reveal tested.
- Honest numbers: PASS. Viewer identifies its own movement model and displays the quality axes used for its guess.
- Standards: PASS for solo source interpretation, creation, mapping, revision and connection activities.
  FAIL for catalog/family agreement: catalog says none while the spec requires dance; documented outside-scope update.
- Motion off: PASS. Per-count figure, stopped ambient motion, readable temporary actor and no infinite-animation audit leads.
- Short choices without scrolling: FAIL for the explicitly specified scrolling phrase strip at compact sizes.
  Source and partner's six answer cards are visible together; compact Viewer layout was repaired for this.
- Resize mid-animation: PASS. Audit resize test completed without exceptions, stuck playback or lost controls.
- Late welcome: PASS. No welcomeAfter; first action owns its context. Empty Reset now preserves an already-running guide.
- Unknown as unknown: PASS. Viewer guess and result meters stay hidden before the performance or partner choice.
- One look, one meaning: PASS. Start X, direction arrows, stationary circles and revision dashes inspected separately.
- Truthful badges: PASS. All nearest ties remain ties; source recognition and partner results follow the actual result.
- Returning hints: PASS. Step/source/reset transitions restore state-specific hints; held-input runs cover these changes.
- No copying answer words: PASS. Viewer derives its result from averaged qualities and path, rather than highlighted words.

## Audit leads

The single full audit completed: 37 leads, 35 captured frames, no console exceptions, infinite animations or resize failures.
All leads are accounted for in these groups. Repairs received focused checks; the full audit was not rerun.

- 5 small-target leads, Hang at 680/800/1000/760/375: FIXED with minimum 44-pixel inline targets.
  Final measured targets and both complete phone poems pass.
- 6 move-label/number overlap leads, two each in Moves/Map/Viewer: FIXED label sizing;
  final four-card bounds do not overlap. Some original boxes included blank block/pointer areas.
- 2 AUDIENCE/draw-status overlaps at 680 and 375: FIXED separated status placement; bounds and phone frame checked.
- 1 unnamed textarea lead: FIXED explicit aria-label, in addition to its native associated label.
- 6 secondary-fold leads: OPEN. Map Reset at short/phone sizes; Viewer sentence and/or Reset at short sizes,
  and each below the phone fold. These are reachable by vertical scrolling; primary performance controls remain visible.
- 4 sideways phrase-strip leads, Moves/Map/Viewer at portrait/phone and six cards at 680: ACCEPTED per the spec's strip.
  Keyboard access and Alt-arrow reorder work; this remains a failure of the stronger wave no-scroll lesson.
- 12 welcome-not-heard leads: source choices Train/River/Storm/Rain/Drum, Reset, Listen and five highlights.
  First taps intentionally own their action/context instead of replaying a late picker welcome.
  Source choices teach selection, Listen reads the poem, highlights act immediately. Empty Reset now preserves a guide.
- 1 quick Reset cut-how lead: FIXED empty-source Reset as a no-op while the guide runs.
  Final voice log confirms the full welcome with no cut.

## Frames looked at

Inspected both bar tools, all four finished WebP images, and every PNG captured in the following Scratch sets:
`first-frames`, `check-frames`, `size-frames`, `phone-frames`, `input-frames`, `extra-frames`, `final-frames`,
`candidate-frames`, `final-check-frames`, `lead-frames`, `caption-frames`, `smoke-final-frames`, `rain-map-final-frames`.
The full size run covers all four modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
Hosted 375-wide views include both poems, all modes and final caption placement. Grayscale and Motion off inspected.
All 35 audit PNGs were inspected through six contact sheets; filenames recorded in `audit-viewed.json`.
Later screenshots were limited to changed layouts and interactions. The bar comparison was also inspected.

## Art made

Four original gpt-image paintings: river, storm, paper backing and empty studio. No people generated.
Final WebP total: 290,064 bytes, 283.3 KiB. Final bundle: 973.8 KiB, below 2 MB.
All four processed through art.py --rekey and viewed at output size. No redraws required.
Generated-image credit is in tool.draft.json. All four images are used in the tool.

## Art still to paint

156 requests marked people true: thirteen verbs x three levels x two weights x two keyframes.
The owner wants painted dancers. The kit figure is temporary; createActor isolates the replacement.
All requests have reserved art tokens; frames carry pose, phase and quality metadata for the painted adapter.
Reuse the previous frame for freeze. Deduplicate poses or use an atlas to retain the bundle budget.

## Engine changes wanted

Three exact requests and current workarounds are in handoff.md: dance.floor.draw marley/barre options;
dance.phrase.at custom pose callbacks; dance.floor.resize actor heights below its current minimum.
No shared kit file was changed.

## Left open

- Painted dancer work above remains for the next painter and owner review.
- Browser speech is the fallback. No recorded narration was made, as instructed; planned bank is gentle-storyteller/Vindemiatrix.
- All Chrome testing was muted. Synthesized source timbres, music and narration need human listening review.
- Secondary Reset/closing-sentence scrolling, intentional sideways strip and small portrait Map studio remain.
- Real S and zigzag examples pass; this is not exhaustive recognition testing of every hand-drawn shape.
- Family catalog/doc registration is unresolved outside the permitted folder; the spec's dance-engine option was taken.
- The full audit predates the focused repairs. No second full audit or polish round was started.
