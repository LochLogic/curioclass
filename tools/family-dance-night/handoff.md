# Family Dance Night build handoff

Built November 2, 2026 in S:/CurioClass-codex. Build only. No commit, branch change or polish round.
Only tools/family-dance-night and _scratch/family-dance-night were written.

## Structure

src.html starts from kit/starter/src.html and loads kit:curio plus kit:dance. Permanent panel controls precede the stage in the DOM. Tool code holds seven source-content records, fourteen move keyframe sets, the voice table, figure decorations, responsive room, run lifecycle, original ensemble timbres, map and favorite handlers. world.json is the existing local Natural Earth land outline reused without country borders, rendered in Equal Earth projection. The data is bundled inline.

Each new run, tab switch, favorite panel or return stops the old play, clock, music and speech. runId invalidates delayed speech cleanup. Copy uses Dance.mirror with model facing zero; turning moves rotate the pose's yaw inside that class-facing model. The count-in starts the sequencer only at dance count one, avoiding the engine's negative-position loop wrap. Read waits until the first dance count if a count-in is active, then stops the run and reads. Slow uses the engine's next-count tempo change.

Word chips use the last shown move or both moves for a full Watch loop. While music is running, answers wait until the next count. Music is lowered about 6 dB during narration by reattaching the same kit track at half volume; tool timbres use their output gain. A speech generation counter prevents an older completion from raising volume under a newer line. Sound off leaves the clock intact. Motion off samples props and figures once per count and removes light pulses.

Table lights and favorite choices live only in memory. Shared kit Motion remembers its preference. All seven first returns brighten the room and play the final event line. No class data is stored or transmitted.

## Painted-dancer adapter installed in the cold review

createFigureRenderer and decorateFigure hide the Dance.dancer model and draw a complete painted person (one paired costume for the lion). PAINTED is the sole asset/geometry table. It has two key poses per move, 28 individually cropped WebPs across seven consistent characters. The owner-requested people flags, prompts, source and review status are in art/prompts.json. Original pose sheets and the people contact sheet are in _scratch/family-dance-night; raw subject crops stay in art/raw.

Dance still owns the clock, travel, count-in, pose model and mirrored Copy convention. The adapter swaps whole painted poses on counts; Motion on adds a small rhythmic root bounce, and Motion off quantizes that too. Geometry is normalized to the tallest pose per character so the lion bow and low positions do not grow to match the standing pose. A replacement set only needs updated PAINTED sources/normalized widths/heights and corresponding art assets. No shared engine change is required.

The move buttons now use the same painted poses as the stage. The table paintings and warm gym remain. The old lion-head/body, fan and umbrella files are retained as source art, but complete painted figures now carry their own props. Final review must not infer exact traditional choreography from a two-pose movement study. The 2 MB figure is a goal; preserve teaching art.

## Open questions and specification decisions

- Cultural review: take the spec's implied recommendation for a review of all seven dances, props, descriptions and movement simplifications. BASELINE rule 5 resolves the mechanism: a fresh review agent before release, without waiting for outside reviewers. This Build run is not that cold cultural review. No extra agent was spawned.
- Painted dancers: the owner's explicit decision supersedes the old spec art plan. Painted dancers are now installed, with people true on every pose. Owner contact-sheet review remains part of release.
- The specification asks the builder to add this tool to docs/families/dance.md. The write boundary forbids editing docs, so the exact registration request is below.
- The explicit move word lists contain 41 pairs, not the stated 38. All per-word totals in the spec sum to 41 and were retained. Loop durations, 60 percent Slow and the four contrast ratios recompute correctly. Scratch numbers.json has the calculations.
- No recordings were made, as CODEX-BUILD.md directs. All fixed lines are in voice/lines.json using bank clear-teacher / Iapetus and browser-speech fallback. The bank voice is the intended future recording voice, not a claim that the browser can select Iapetus.
- The user's stop-on-report instruction takes precedence over the brief's early-report advice. codex-report.md is written last; intermediate evidence stays in Scratch.
- The bar tools were bundled into Scratch, avoiding writes to their tool folders, and opened in muted Chrome. Their sources and existing art were read only.

## Engine changes wanted

- docs/families/dance.md, What each tool brings table: add family-dance-night, K-2, square floor; seven dances and two lion figures; fourteen mirrored pose phrases; clock, music, counts and icon; family tables, dance words, origins and room lights. Also update the four-tool count. No shared engine change is needed for this build.
- kit/curio.js, init Motion handler: an optional in-memory preference would allow a literal no-storage tool to avoid curio-motion while keeping the shared Motion button. No kit edit was made.

## Validation and next step

The final report records the bounded test batches, frames inspected and the single mechanical audit's disposition. Scratch contains commands, shot lists, logs, numeric checks, pose sheets and audit output. Browser runs use Chrome ports 9970 to 9977 only; iframe hosting uses 8775. Every browser and server started by the build is closed after its batch.

The painted dancer set is installed. The next workflow is a fresh sensitivity review of the painted simplifications and a listening review of the synthesized ensembles. Do not infer cultural authenticity from a passing mechanical check. The renderer boundary and PAINTED table keep future figure replacement local to this tool.

The single audit completed in 693.5 seconds with exit zero and 16 leads. Nine concern the intentionally hidden panel #hint while the gym's visible #home-hint owns Read. Seven concern the intentionally skipped gym welcome when the first table tap speaks its own name, as STANDARDS requires. All states, resizing, focus, calm animation, repeated clicks and console checks were clean. Manual held-click logs additionally cover the interior controls.

After the audit, the ceiling light layer moved behind the dancers so raised fans and umbrellas remain visible on a phone. The focused phone prop frames and a laptop fan frame were rechecked; the full audit was not rerun for this layer-only change. relayout reserves more space above fan and umbrella figures by using a 0.45 height fraction; other figures use 0.53. Keep that prop clearance when installing the paintings.


## Cold-review functional repairs

- Initial Words context is Move 1, not both moves. Watch tracks the displayed move and allows both only after one completed loop. A single Copy move resets that context. This closes the unseen-move affirmation path without adding scores or gates.
- Space retains native activation on focused controls; the background play/stop shortcut is limited to Watch and Copy. It cannot start hidden Watch controls from Words, Where from or Favorite part.
- Read checks the Favorite overlay before the underlying origin tab. Concise mode how-to lines start before longer event descriptions. Visible hints change synchronously.
- Favorite move selection now shows that painted move, preserves the selected card on revisiting, and names the class's choice on the floor. The why prompt asks for dance words and an interpretation of what the moves show; it works aloud alone or with a partner. Grade-specific prompts in notes.md distinguish naming from interpreting.
- Source wording now distinguishes southern lion dance, solo Irish step dance, the staged Korean fan dance, and the Black community origins of second line. See notes.md for claim-specific links.

## Sensitivity

All seven dances represent living cultures. Review the new people contact sheet for respectful anatomy, clothing, ages and body representation; the single cast member is not a representative of everyone in that community. Check the simplified lion rise/bow, zapateado versus skirt study, Irish solo versus ceili distinction, Punjabi harvest summary versus modern forms, buchaechum's named creator and group formations, Black New Orleans origin credit, and Ga-specific Kpanlogo movements and drums. The synthesized ensembles need a listening review and must remain labeled original sketches. No outside-contact gate is added.

Cold-review evidence and final audit will be recorded in codex-review.md. The earlier build audit above is historical and does not certify the painted revision. The review uses Chrome 9960 to 9967 and host 8765, with no shared-file edits or commits.


## Cold-review audit result

The single final review audit did not finish. It failed before the first screenshot while enabling a Chrome CDP domain, at the driver's internal 60-second request timeout. There is no generated audit.md or saved lead list. The 2400-second outer limit was in place. It was not rerun, as CODEX-REVIEW.md requires one audit, last, followed by reporting and stopping on failure.

Current targeted evidence covers 1366x768, all seven Watch loops, 28 pose cutouts, 252 word/context checks, the confirmed keyboard and Read cheats, the final main-path voice log, reduced motion and grayscale. It does not certify the seven other STANDARDS sizes. Recheck those in the next workflow before release. See _scratch/family-dance-night/review-audit/run-failure.md and final-static.json. Chrome 9960 and 9961 and host 8765 had no responding listener at closeout; no tool host.html exists.
