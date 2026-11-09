# Codex review: dancers-on-tour

## Played

Evidence root: `_scratch/dancers-on-tour/`. One cold review pass, then scoped repairs and rechecks.
Grade-7 solo play and a projected-classroom reading: Gym Scout rings, Adapt and Run; a 15-minute warm-up; Park raised Circle and Run; Theater split/facing and Run. Strong venue paintings and precise live plan; blocked sightline goals make the finish frustrating.
## Findings fixed

- Blocker/general: Safety became green with only an eight-minute gym warm-up, or an out-of-order plan with static holds. Safety and ready now require the existing warm-up checklist; exact numeric risk points remain unchanged.
- Should fix/general: unrelated edits praised notes that were already true. Note acknowledgments now require an actual false-to-true transition.
- Should fix/general: painted dancers deferred despite the owner's decision. Added three people:true cast atlases with six consistent identities and five teaching poses; replaced the visible kit figure behind audienceRenderer.
- Should fix/general: phone frequent controls extended well below the viewport. Packed the existing control desk beneath the plan with 44px targets.
- Polish/general: every run ended with the same generic failure and success sound. Added a personal count of phrases that retained fit, spacing and sightlines; failed runs use a neutral completion tone.
- Should fix/general: a scouting fact could continue over a different card, and result speech could survive an invalidating edit. Stopped stale speech while preserving Read priority; fixed one malformed apostrophe in the manifest. hot-facts-final.json confirms new facts wait for Read.
- Blocker/general: Motion off skipped travel collisions, improving the run recap. Separated path checking from reduced-motion pictures. path-on.json and path-off.json now return identical results.
- Blocker/general: the sprinkler note rewarded endpoint-only clearance although the default run crosses the head exactly. The final repair checks every dancer segment between formations, with the unchanged 0.75 m threshold.
- Should fix/general: stale completed-run captions survived edits/reset. Captions now invalidate with the result; actual Run then Reset returns 32 counts and preserves Park settings.
- Should fix/general: Sound restored after edits could leave mode instructions unheard. Valid current-state welcomes recover in Scout, Adapt and Warm up; all three focused logs pass.
- Should fix/general: phone selected-block arrows fell below the fold. Moved them into the warm-up builder at phone widths, preserving the wide panel layout, focus and real dragging.
- Polish/general: phone theater rings crowded each other. Separated the exits ring without reducing the art.
## Findings left

- Blocker/general, spec conflict: supplied visibility thresholds make whole-venue all-green and theater note 3 unreachable. No threshold was relaxed. Independent calculations/search in numbers-review.json and an exact current-seat, every-slider-step check in canonical-seat-check.json. The straight Park travel paths also lack a joint Fit/Spacing/sprinkler solution in the discrete control search; sprinkler-review.json. These remain blockers, not PASS results.
- Should fix/general, spec conflict: gym warm-up cannot erase its two hard-floor jump points, contrary to Done when 4. Preserved the explicit, safer formula.
## Break it

Before repairs, real held taps set gym [Pulse, Dynamic] to eight minutes and Safety 0/green; theater [Dynamic, Pulse, Holds, Feet] to thirteen minutes and Safety 0/green. After repairs both retain their honest zero point total but show amber Prep and ready=false; correctly ordered theater [Pulse, Dynamic, Feet] still shows green. Evidence: cheats-after.json.
Original/split theater diagonal: swept every slider step; original never passes Fit and Spacing together, split does at 0.85 and 0.90 only. A single green Seen light at too-small spread does not pass spacing or ready.
Warm-up toggles cannot add duplicate blocks. There is no saved best score, quiz, hidden-answer badge or reflection gate. Endpoint-only edits do not clear a run if transitions fail.

- Sprinkler cheat: cold Park Run kept the note ticked with endpoint minimum 1.0 m, while dancer 4 crosses the head on Window-to-Circle travel (minimum 0.0 m). Independent geometry in sprinkler-review.json; post-fix default path is rejected and a geometrically clear probe is accepted; sprinkler-path-after.json. A sweep finds no all-fit/all-spaced Park solution with those straight travel paths, another authored-constraint conflict.
## Voice walk

Held clicks were 0.12 s at a 2 s pace. Cold logs are play-gym.json, play-warm.json, play-park.json, play-theater.json and cold-warm-filled.json. Final main path: plain stage tap, floor ring, Go to Adapt, Warm up, Pulse, Dynamic, Feet, Key moves, Adapt, Diagonal, Run. Heard in order: Scout welcome, gym floor fact, Adapt welcome, Warm up welcome, earned gym-note event, afterRun. No speech during Run. main-final-post.json. Sound-off edits followed by Sound on also recover the current instructions in each mode; sound-*-recovery.json.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Scout, Adapt, Warm up welcomes | how | 1 each on main path | 1 each |
| tooClose | event | 5 crossings | 5 |
| staticHow | how | 1 after unsafe ordering | 1 |
| afterRun | how | 1 per page | 1 |

Five crossing evidence: event-repeat-after.json; static ordering: static-order-voice.json. Side Read/reset/Sound-off Read logs checked; a main-path navigation fixture failed once because it reloaded its own evaluation context, then was replaced with a smaller non-navigating fixture. One initial cheat drive lost Chrome; bounded retry succeeded. No tool exceptions in successful focused runs.
## Facts checked

- Formations, dimensions, nearest distances, all venue spread intervals and 17.142857 seconds: independently recomputed from the authored coordinates in spec.md; numbers-review.json.
- Warm-up sequence and dynamic movement: IADMS, The Importance of a Good Warm-Up, revision June 22, 2025: https://iadms.azurewebsites.net/media/glfba5xu/iadms-resource-paper-the_importance_of_a_good_warm-up.pdf
- Hard floors and sprung floors: Ausdance Safe dance practice, https://ausdance.org.au/articles/details/safe-dance-practice; CDMT Safe Dance and Floors, https://cdmt.org.uk/safe-dance-and-floors/
- Long static stretching can acutely affect power, depending on dose/context: Behm and Chaouachi 2011, PMID 21373870, https://pubmed.ncbi.nlm.nih.gov/21373870/. This is not a universal ban on all static stretching.
- DA:Pr4, 5, 6: NCAS Dance handbook, https://www.nationalartsstandards.org/; planning activities support spatial design, preparation decisions and adapting to venues. They do not demonstrate physical technique by themselves.
- Venues, temperatures, distances, safety points, minutes, blanket/seat eye heights, obstacles and sun direction are fictional model inputs from spec.md, not universal guidance. Fit and sight rules are explicitly labeled rules of thumb.
- Hand checks of sight rule: gym A2, x 0/z -1.4/eye 1.0, loses Wedge dancer 6 behind dancer 1; C2, x 0/z -4/eye 2.6, sees all six. Park Circle at spread 1: low 0/9, middle 1/9 under the same model.
- WCAG 2.1 contrast, independently recomputed: ink/background 15.47, ink/panel 13.78; muted 8.05/7.17; brand 11.36/10.13. contrast-review.json uses the W3C relative-luminance formula.
## Sensitivity

Bodies and safe preparation need review. Painted cast varies skin tone, hair and lean-to-broad builds without assigning cultural or gender roles. Inspect anatomy and ordinary forefoot-supported releve, consistent identity, low/middle heights, and representation. No physical task or body ranking; the invented dance claims no cultural lineage. Contact sheet: painted-contact.jpg.
## Flattest moment left

The new phrase-specific recap lifts the former generic end-of-run message, and the painted cast lifts the weakest art.
The specified visibility goal cannot be completed. Repeated amber after a good fit is the largest remaining frustration and requires a spec decision.
## Graphics

Kept six strong venue/surface paintings. Added front/back/right cast atlases, mirrored left; five poses reuse arms-wide as jump preparation and the traveling step as middle-level Circle. All atlases people:true, generated with built-in OpenAI image tool; front releve redrawn once. Raw assets and atlas prompts retained; 32 superseded prompt records are archived outside the active nine-asset queue. Final bundle 1,567,093 bytes (about 1530.4 KiB); nine finished WebPs total 1,043,356 bytes. Contact sheet and final-size stage frames opened.
## Audit

One full audit completed, exit 0, within the 40-minute cap, port 9961, host 8765: review-audit/audit.md, 279 leads and 95 frames, all inspected (review-audit-contact-00 through -15). No second full audit.

- Default eight sizes, Motion off, resize stress, console checks, repeated clicks and quick taps completed. Compact and phone states were also inspected individually.
- Confirmed and fixed: phone warm-up reorder controls and clipped menu edges; close theater rings. Post-fix all 18 warm-up targets end by y=660 at 375x812 and remain at least 44px. Actual drag and 375-to-760-to-375 resize pass with focus retained and scrollY=0.
- Dense plan overlaps are transparent 46px targets over exact metric positions; real dense tap plus Enter twice selects dancer 3 correctly. Visible numbers stay legible; bodies were not shifted to disguise crowding.
- Closed-disclosure text/privacy overlaps are not painted. The open-disclosure check measures a 24px gap. The optional rule summary and long preparation checks may scroll on short screens; the short choice sets and frequent controls fit.
- Five first-ring welcome leads follow STANDARDS first-action priority: the ring speaks its own fact and skips the generic welcome. The main stage-first path hears Scout, Adapt and Warm up once each.
- Successful direct-file drives have no console errors. HTTP wrapper shots log only its favicon.ico 404, not a tool resource failure. The one-file tool has no external resource URLs. All started browsers/servers are closed and host.html removed.
- Live real drag: spread 1.35 while clock position advances 0.30 to 1.50. Live Window swap and 105% tempo remain running. Reset clears completed status and preserves Park; run-status and post-resize evidence.
- Final receipt: review-verification.json. The audit preceded these scoped final repairs; only touched states and the main voice path were re-shot.
## Left open

Not release-ready: the spec-level completion conflicts above remain. Browser fallback narration is tested by starts/logs in muted Chrome; recorded-voice and by-ear quality are not claimed.
No questions were asked in the unattended session. Chose explicit formulas over conflicting worked examples, preserved the specified thresholds, used five poses and three views to minimize redundant art, kept browser narration per the no-recording rule. No commits; manual file writes stayed in the allowed tool/scratch folders. Generated-image service outputs were copied into the tool as the build rules require.
