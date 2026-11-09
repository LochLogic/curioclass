# Dance Hall Decades handoff

Cold review, November 5, 2026. Work stays in this tool and _scratch/dance-hall-decades.
No commit or deployment. Read codex-review.md for the final evidence and audit disposition.

## Source map

- src.html uses kit:curio. HALLS holds the eight source-backed cards; ROWS holds the 32 authored chart positions.
- buildPattern holds counts, active feet, relative floor positions, subdivisions and cues. The same audio clock
  drives the groove, count, footprint and painted pose. Lindy has eight placements in six beats; Hustle has a pickup.
- figureRenderer is the painted-person rendering seam. PAINTED_DANCERS selects two 4-by-2 character sheets;
  PAINTED_DETAILS holds behind-cross, touch, back-tap and scuff studies, with Avery on row one and Jo on row two.
  PAINTED_TURN is the separate grounded-turn study, before the lifted scuff.
- HALL_DANCER and paintedPose map a count to a character, cell and mirror. Sheet coordinates are 384 by 512.
  Replace the four WebPs or this mapping without changing the clock, footprints, content or comparison.
- The former code figure is removed. Seventeen selected painted poses are reused across the eight dances. The
  source sheets retain unused candidate cells; these are not additional classroom poses.
- Painted poses hold on each count, including Motion off. A rear-view teaching model demonstrates relative steps;
  the Electric Slide wall label follows the quarter turn on 17, with a right scuff on 18. Exact footwork remains
  in the labeled diagram. The demonstrator is not a reconstruction of a historical patron or costume.
- The scheduler has a 35 ms lookahead. Tempo changes affect the next unscheduled interval. Tabs leave music running;
  hall/mode changes, Read and hiding the page stop it. No voice plays over the groove.
- Curio.voice handles narration, Read and Sound. Short how-to lines fit the two-second action pace; stories
  are dropped or cut when their hall/tab no longer fits. No recordings were made; browser speech is the fallback.
- Comparison controls stay mounted. Dance changes clear writing tied to that dance; criterion changes clear
  the comparison reason. Writing is explicitly a draft, not a machine-graded cultural judgment. Copy can copy a draft.
- localStorage and clipboard access are guarded. Privacy is stated on screen. Reset clears only this comparison.
- __tool exposes state, setters, pattern, clock trace, voice log, sentence and renderer for inspection.

## Review changes

Painted two varied adult demonstrators and extra touch/turn studies, with people:true on all four assets.
Redrew Avery's two Twist cells to distinguish standing and shallow-dip counter-rotation.
Preserved all eight rich halls and eight object markers. Contact sheet:
_scratch/dance-hall-decades/painted-people-contact.png, on a contrasting background at classroom figure sizes.

Moved Talk about it above the history card, reset historical scrolling on hall changes, repaired stale comparison
evidence, shortened movement/room how-to lines, fixed mirrored arrow origins and paired L/R labels, raised the
Georgia count glyph to prevent descender clipping, corrected the Electric Slide turn count, replaced the broken
Palladium source link, and qualified the spoken disco-backlash interpretation to match the screen.
The final audit confirmed a quiet first Dance-tab tap and a how-to interrupted by quick Next taps. The current
tab now narrates, and the still-valid shared Play instruction finishes across hall changes without stale stories.
Restored the original judge spacing after an overbroad review CSS edit, and separated repeated footprint labels.
The select focus ring sits inside its control so it cannot cover the label above it.

## Sensitivity

Fresh cultural review should check creator credit and institutional exclusion across Black American, Cuban,
Puerto Rican and Latino dance histories; gay communities' role in disco; the attribution of backlash interpretations;
and the disputed Electric Slide origin date. The cross step avoids a stereotyped Native American label, explained
only in teacher notes. Do not reenact segregation or ask a learner to stand for a whole community.

The painted modern demonstrators vary in skin tone, age and body shape. Both are ambulant; the prompt requests
a hearing aid for Jo, but its small scale is not a strong visual accessibility cue. Notes allow seated tracing and
observation. Review anatomy, support weight and stereotyping, including at the actual display sizes.
The contact sheet is ready for the owner; this unattended run makes no claim of owner approval.

## Source conflicts and limits

- Salerno's Electric Slide teaching sheet controls the corrected ending: 15 right back, 16 left touch,
  17 left forward with the quarter turn, 18 right scuff. The supplied spec's ending is inconsistent with it.
- The Stroll remains the specified eight-count side-touch adaptation. Powers's reconstruction uses six-count patterns.
- Mambo remains on one as requested. Library of Dance documents historical on-one as well as on-two timing.
- The requested Hustle tap sequence is not verified as a complete continuous partner basic. It now says short tap
  introduction, and count 3 asks for a right-weight reset before the next left tap. A full replacement would disagree
  with the exact spec sequence, so it is left for a spec decision and an embodied dance-teaching check.
- The fundraiser wording for 1973, attributed 1976 origin date, Ballard recording/release distinction,
  qualified venue access and modern-summary fact-card labels are preserved and checked again.
- Synthetic grooves are original learning sketches. No headphone or professional embodied dance review is claimed.
- No points, timers, completion prizes, cultural rankings or win states were added.

## Engine changes wanted

None. No kit, script, docs or neighboring tool changes were made.

## Evidence

All paths below are in Scratch. Cold play: cold/, cold-play/, cold-hall-*.json and cold-moving.json.
Reproduced stale evidence: cheap-before-stale.json. Fixed comparison: stale-fixed.json and review-cheap/.
Painted integration: review-quick/. Final sizes, keyboard, grayscale and Motion off: review-sizes/.
Main voice path and counts: main-after-audit.json, selected-tab-first.json, quick-next.json and read-side.json.
Focused final rechecks: post-audit-voice/, post-audit-poses/ and post-audit-moving/ with corresponding JSON proofs.
One final audit: review-audit/audit.md and its frames. See codex-review.md for confirmed leads and limits.

## Cleanup limit

Assigned Chrome ports are closed and host.html was removed. Port 8755 still serves this tool after the child
cleanup attempts; Windows exposes no owning listener PID. Closure could not be verified without stopping an
unidentified process. Scratch cleanup-verified.json records the final observation.
