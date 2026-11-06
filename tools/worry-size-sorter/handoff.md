# Worry Size Sorter handoff

## Structure
`src.html` starts from the kit starter, uses kit CSS and Curio.voice, then contains responsive scene CSS and a single
state machine. `worry-data.json` is loaded by a json token and bundled inline, with all thirteen cards, talk-back sets
and body facts copied from the spec. `__tool` exposes state, pure calculation helpers and narration logs for review.
The 27 WebP images are embedded once in an art map. The background is a CSS art token.

## Tricky parts
Big cards coerce their destination to Big. Personal Small/Medium choices are accepted, including Big by choice.
The Big panel appears immediately; Next waits for the line, capped at four seconds. Mode changes cancel activity timers.
Sort advances no longer hush a Big line that is still finishing after that cap; the spec labels this event never stale.
Read is protected across automatic breathing phases. Cues replace stale cues through the kit queue, rather than hushing Read.
Breathing applies count changes next phase; Motion off keeps durations. The week uses UTC arithmetic on local date
components, never elapsed hours. Storage failures are caught. No typed disclosure is collected.

## Spec decisions and open questions
- Made all 27 named images. The heading's total of 26 is an arithmetic error.
- Used flat green keyed backgrounds rather than the Art section's white, following the newer build brief.
- Used the requested built-in image tool for every asset, including objects called local FLUX in the spec.
- The explicit voice rule holds Next on a Big card for at most four seconds, despite the general immediate-action rule.
- A goal also needs a chosen body-clue reason if there is no meter result. Otherwise the required Because could be empty.
- Worry box cannot use Bedtime in the goal builder. Live YoungMinds Step 3 advises against using the box just before
  bedtime, contradicting the spec's generic three-time builder. Morning and After school remain available. No new topic added.
- Same child in five poses, each marked people true. Contact sheet is in Scratch for the owner's later desk review.
- The fresh sensitivity check passed after m3/m4 escalation notes were kept in Tools and refreshed on worry selection.
  The toes image was redrawn once and rekeyed with enclosed-gap handling.
- Standards override the spec's original week welcome, which named Set my goal while it was disabled.
  The welcome now starts with the enabled tool choices; later builder steps have short once-only how lines.
- Sensitivity review is required by the spec; its result is recorded in codex-report.md.
- Build only forbids recording. Friendly-dad recordings remain a later media step; browser fallback is used now.
- Kept all shared code untouched. Bar tools were copied and bundled in Scratch to respect the write boundary.
- Report working notes stay in Scratch until final delivery, because the owner's stop instruction applies once the final report is written.

## Sensitivity
Review all five Big cards, their reasons, m3 and m4 self-talk, adult-help wording and US 911 instruction.
Abuse, online exploitation and family illness can prompt disclosures. The privacy sentence explicitly says the student
does not have to tell the class. Notes contain calm-response and school reporting guidance.
The same warm-brown-skinned child appears in all five poses. Check anatomy, comfortable expressions, full-body framing,
pose clarity, and avoid interpreting worry signs as a diagnosis. The cards depict places and objects, not frightening events.

## Art still to paint
None planned. People contact sheet and representation check accompany the build evidence.

## Engine changes wanted
None at build time. No shared engine or kit was changed.

## Cold review repairs
The cold reviewer played all thirteen cards, all five clues, all four tool sequences and the week reflection before reading
the build report or source. Evidence is in `_scratch/worry-size-sorter/`, with pre/post cheat traces and sized frames.
Early Finish now reports the week so far, makes chips explicitly optional and resets chip picks for a new goal.
Meter decreases describe the child's report without claiming the tool caused it. Stop remains immediate and labels
an unfinished practice; helper choices remain personal reports, with no score or mastery reward.
Breathing completion names Done rather than Start, keeps keyboard focus, and shows the actual before/after check-in.
Automatic squeeze transitions focus the next control and speak the specific shoulder/toe instruction once.
Short timed event cues name fists, shoulders and toes as well, so closed-eye practice does not depend on finishing
the longer ready-step line. Automatic squeeze transitions preserve Read; manual Stop and mode changes still hush.
The swimming Facts reply no longer guarantees shallow water or an instructor's position. Red Cross swim guidance
supports asking the instructor for help. Notes distinguish state reporting law from school policy.
The toe asset was redrawn with fully closed socks and visibly curled fabric, matching the same child and warm style.
Compact and 1280x720 result buttons share a row so the self-report explanation stays in view. The phone square keeps its labels
inside the illustration. Selecting a written worry refreshes its heading along with the bubble and the panel.
Sort's premise is in Read even when the compact layout folds away the principle line. Unsupported "Many kids say"
and the claim about classmates' thoughts were replaced with explicitly flexible sizing and realistic self-talk.
Review-added lines are synchronized with the voice manifest; actual friendly-dad recordings remain a later media step.
