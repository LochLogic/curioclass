# Dance Hall Decades: Build handoff

Built in S:/CurioClass-codex. Build only, no commit and no polish round. Read codex-report.md for the final audit
disposition. Evidence, temporary scripts, bar bundles, Chrome profiles and screenshots are in
_scratch/dance-hall-decades/. The final report is written last because the owner explicitly says to stop when it exists.

## Source map

- src.html starts from kit/starter/src.html and inlines kit:curio and kit:dance at bundle time.
- CSS lays out the scene at actual pixel sizes. Halls has a scrolling timeline, an explicit bounded workspace row,
  painted hall and control panel. At short landscape sizes supporting panel text hides so transport stays usable.
- HALLS contains the content and source cards. ROWS contains all thirty-two authored dance positions.
- buildPattern stores count labels, active feet, top-down positions, durations, cues and pose hints. Lindy includes
  swung substeps; Hustle has a lead-in. The audio meter continues through the ends of dance phrases.
- drawFootprints draws travel arrows, L/R stamps and numbered locations. Repeated-location phrases show the active
  stamp rather than piling every stamp on top of the same spot. The count strip gives the full phrase on roomy screens.
- figureRenderer is the swap seam for painted people. It uses Dance.flat, Dance.pose and Dance.mix with tool-specific
  joint overrides until a corresponding real WebP resolves through PAINTED_POSES. Draft SVG tokens stay hidden.
- The original eight grooves use a Curio.audio context and a cancellable bus. A 12 ms scheduler looks 35 ms ahead;
  the visuals consume that same audio-clock event list. Tempo changes affect the next unscheduled interval.
- Curio.voice owns speech. No recorded clips were made. Story requests during Play are held locally until Stop, then
  checked against the current hall and tab. Read stops music before the kit reads the current hint. Hint text changes
  synchronously, including when the same hint node moves into the comparison mode.
- Comparison controls stay mounted. Me sliders, distinct picks, criterion, strengths, fact choices and writing save
  through guarded localStorage. Selected evidence can fill the closing reason, which remains editable. Copy uses the
  clipboard when available and otherwise selects the sentence for manual copying. Reset clears only this comparison.
- __tool exposes state, hall/tab/mode/speed setters, play/stop, pattern, clock traces, voice log and sentence for checks.

## Owner decision: painted dancers

The final tool should have painted dancers. It currently uses the kit's faceless figure, as directed. There are
42 deferred people assets with people:true in art/prompts.json. No people were generated in this run. PAINTED_POSES
references the future art tokens; supplying the WebPs and rebundling activates them without changing the scheduler.
The painter should read each count cue and inspect the diagram, keep the whole body and both feet in frame, and use
one consistent demonstrator across a dance. The optional Stroll couple-strut and Electric quarter-left assets give
the next painter formation and facing coverage. The final scuff pose is right-foot scuff while turning left.

The first painted pass should check the body's support leg, touches without weight, partner connection, opposite
hips and shoulders, and the four-wall turn. The kit figure is deliberately temporary. A painted pose currently
holds per count; continuous interpolation belongs to the code fallback. Review painted mirroring and turning once
the real people exist. Existing no-people paintings were inspected individually and as a dark-background sheet.

## Decisions and source conflicts

There is no separate Open questions section in this spec. The owner's explicit painted-dancer decision is recorded
above. These source conflicts were resolved without changing the teaching topic:

- The Electric Slide's specified final counts were incomplete and contradicted an eighteen-count teaching sheet.
  Use right back, left touch, left forward, right scuff and quarter turn left for counts 15-18. The common version
  and Silver's original twenty-two-count choreography remain distinct. Silver's claimed 1976 date is attributed.
- The Stroll is labeled as an eight-count side-touch adaptation; historical reconstructions use other side patterns.
- Mambo is labeled the requested on-one teaching adaptation. Common ballroom mambo breaks on two. Do not claim this
  generic teaching pattern precisely reconstructs how everyone danced at the Palladium.
- The spec requests a short Hustle tap introduction. It is retained and is not presented as a complete partner basic.
- The unsupported generalized statement about closed hotel ballrooms is softened. The integrated Palladium floor and
  the broader context of segregation are retained with a concrete source card.
- The 1973 event was a fundraiser, so "free parties" is not asserted. Neighborhood creativity remains the focus.
- A line-dance format can welcome newcomers; it cannot establish that no one was ever excluded from wedding settings.
- The Library of Congress distinguishes Ballard's November 1958 recording session from the January 1959 release.
  The screen says released in 1959, correcting the spec's conflation of the two dates.
- No new hard-history mechanics were introduced: no scores, timers, completion rewards or win states.

## Engine changes wanted

None required for this Build. If this scheduling pattern is reused, kit/dance.js, music / clock could expose an
optional explicit audio-clock scheduling time and cancellable output bus, so a future tool can align custom count
subdivisions without a local conductor. Do not change the kit as part of this tool's review.

## Review next

Cold review should prioritize embodied dance accuracy, historical phrasing and source limitations in notes.md,
then headphone listening for the synthesized timbres and voice pacing. The named bank voice is Vindemiatrix,
gentle-storyteller; browser speech does not reproduce that actor. Some third-tab text and comparison writing require
scrolling at compact sizes, while hall navigation and the core dance controls stay visible. The timeline is explicitly
allowed to scroll sideways on phones. The audit is a mechanical check, not a substitute for this content review.


## Final Build checks

One full mechanical audit completed with 52 frames and 276 leads. All audit images were inspected in nine contact
sheets. The report groups every lead by cause and disposition. No runtime or resize errors were found. Targeted
repairs address header targets, textarea names, terminal navigation focus, badge bounds, invisible SVG stamps,
compact comparison layout and repeated-tap narration cuts. Five affected-state snapshots are mechanically clean;
the phone Sound layout and three rapid-tap narration cases also passed. The full audit was not run again.
The original audit and all targeted evidence are in Scratch. Chrome 9990 / 9991 and host 8795 are closed, and
host.html is removed. The final bundle is under 2 MB. No commit or polish round was started.
