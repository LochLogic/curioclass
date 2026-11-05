# Dance Styles Explorer build handoff

## Structure
src.html starts from the kit starter, loads kit:curio, kit:theme-912 and kit:dance, then owns the responsive study desk, phrases, rhythm lines, measurements, notes and draft. data.json is loaded with the bundler's json token and holds the complete style files, vocabulary and narration table. All artwork uses art tokens. The generated HTML is the offline deliverable.

window.__tool exposes state, mode and style actions, phrases, event lines, metrics, analytical actors and trails, position controls, note actions and narration logs. These hooks support review; they are not a separate product flow.

## Painted dancers: cold review implementation
Eight people-true painted rehearsal sources replace the code figures. createPerformer, paintedView and paintPose form the local swap boundary. PAINT holds image tokens, CUTS holds normalized crop anchors; another painter can swap a source and adjust these without changing playback. The 69 original pose requests remain in the manifest as superseded history, not missing delivery assets.

One source pose per performer is articulated against the shared engine joints. modelJoints supplies local landmark keyframes for first-position heels/knees, rounded fifth arms, grounded tendu, araimandi and the supported baby freeze. The latter uses one extra whole-pose painting; pataka/alapadma use a single four-hand sheet. Measurements, world hand/foot paths and ghosts use the same corrected landmarks. Head aspect and minimum projection sizes prevent edge-on fragments. These remain study models, not expert technique footage.

painted-cast-contact.png in Scratch shows every new people image. The source cast, named hands, supported freeze and repaired final renderings passed the fresh sensitivity reviewer. Owner contact-sheet review is still a pre-shipping step. All ten images were generated with the built-in OpenAI image tool and processed using art.py --rekey. The first freeze had an extra arm and was corrected before integration.

The custom exposure renderer reuses painted sources, caps at 32 half-count ghosts, carries each ghost's phase, and retains solid hand/dotted foot paths. A/B circle/square badges survive in painted live and ghost views. Motion off keeps the same clock and captures.

## Open questions resolved
- Keep the eight specified styles. No substitution adds a new tradition without a spec.
- Keep the factual demo disclaimer. The fresh cultural review passed in this cold review; technical models remain identified as simplified.
- Use upbeat-guide in voice/lines.json as the revision recommends. No narration was recorded, per build instructions; the browser supplies the fallback voice now.
- Keep all eight painted footwear/gear images. Their large style-file frames and paired Compare frames remain in place.
- Owner override: painted dancers are the final direction. The cold review has now painted and integrated the minimal articulated cast.
- The screen brief says People (3), but the Irish and Bharatanatyam content supplies two names, and Breaking includes a crew and an event. The exact supplied content is retained under People and milestones; no third individual was invented.

## Timing, traces and measures
The shared Dance.clock drives every demo. Choosing a style stops old run/music/voice, clears trace and starts the new phrase immediately. Compare uses A's tempo and A's track; each phrase wraps independently. Flamenco's phrase has 24 counts, with a 12-count cycle readout in Compare. Its rhythm line repeats the five accented positions in each cycle. Ballet counts complete waltz bars at 56 counts/min, giving 168 musical beats/min.

Dance.play handles sequencing; a local captureTo adapter samples the phrase at exact half counts, even when Motion is off, instead of taking whichever frame happened to render. It retains at most 32 ghosts from the last 16 counts. The local painted exposure renderer retains the analytical hand and foot paths, with aged painted ghosts and dotted foot paths. Hand and foot colors distinguish A/B; hands remain solid and feet dotted in both.

Measurements are computed independently from the phrase samples, never guessed from a style label. Hip-band thresholds, sampling and the nominal travel height appear in the UI and notes. Independent Python recomputation matches Ballet and Breaking to floating-point precision. Geometry and comparison results are in Scratch geometry-final.json and measure-results.json.

## Critique and persistence
Notes store style, optional comparison partner, starting and ending counts, the shared clock positions, vocabulary term and words. Pointerdown starts a range; releasing Note ends it and opens the form. N is a keyboard alternative for a single count. Selecting a note seeks to its count and exposes its range; comparison notes restore the shared clock so B returns to its original phase. Cross-cycle ranges are identified in their count text. Insert note uses the selected note, otherwise the latest note for the current style. Inputs use plain text and escaped rendering.

Only notes and the three draft strings are saved under dance-styles-explorer. Storage uses try/catch; the critique footer reports a failed save. Clear critique uses a modal confirmation and removes the key. The kit separately stores its shared Motion preference. Copy includes the full draft and all style-tagged notes; a selectable fallback handles a blocked clipboard. Print uses a plain text print surface so long textarea contents are not truncated.

## Responsive layout
Short landscape previews keep stage and panel beside each other. Tall widths from 601 to 999 stack a 232 px desk below the stage, with the eight choices beside a scrollable file. Phones use a 400 px study area, a separate title strip, an eight-option native style selector, a bounded reference scroller and a 64 px hint row. Transport remains visible while the draft or reference scrolls. The compact critique stage is deliberately smaller to retain Note and the note strip. Short stages move level labels to the right and omit the redundant decorative count pips when they would collide; the rhythm labels and numeric count readout remain available.

## Builder verification (before cold review)
The first functional run passed 30 of 31 checks; it caught inherited arm angles in the pose helper. The helper now expands arms/legs/toe overrides explicitly. A targeted 32-sample Irish check passed, and all eight style frames were inspected afterward. A separate keyboard-only critique run met all five reminders and exercised real Tab, Enter, number-key mode entry and N.

Full size frames, targeted fixes, phone iframe frames, print view, grayscale and Motion off were inspected. Numbers and contrast pairs match the spec. The eight still lifes were generated with the built-in image tool and converted only with art.py --rekey. Flamenco was redrawn once to put nail heads on the soles rather than the uppers.

The full mechanical audit completed once within its 40-minute command limit on Chrome 9982 and host 8785, with 234 reported aggregate leads. Its per-row dispositions are in Scratch audit-disposition.md. The main repeated causes were closed native details rectangles, empty textareas not named by the audit heuristic, and unbounded phone reference content behind the footer. Explicit hiding/naming and the bounded phone desk repair these. Modal coverage and welcome suppression by a demo's own action are intentional. Count steps now allow a first-tap welcome. Motion off, resize recovery, runtime errors, focus recovery and narration repetition sections were clean.

Final checks also repaired pause/resume initialization, stepping beyond A's first phrase, comparison note phase restoration, trace endpoints on resize, Escape hints and plural count citations. Twelve targeted checks, all eight track starts, and a full Breaking observation-to-critique run passed. Targeted post-audit frames checked only the affected states; the full audit was not repeated. All other test runs use Chrome 9980 or 9981. No kit, docs, scripts, other tools or git state were changed. No commit or polish round was started.

Final bundle: 422,294 bytes; eight WebP images total 172,390 bytes. src.html has 1,510 lines with a maximum width of 160 characters. The final keyboard/print run reports no errors and finite geometry after printing. host.html is removed, and all assigned Chrome ports plus host 8785 were checked closed at completion.

## Engine changes wanted
- kit/dance.js, trail.renderExposure: accept ghost spacing, maximum age, per-ghost opacity and foot dash options. Currently capped at 64 lifetime ghosts, fixed 0.22 opacity and solid paths. This tool works around these locally without altering the kit.
- kit/dance.js, trail.capture and play: capture exact half-count poses, not the first frame after a half-count threshold. In calm mode the analytical samples should remain distinct from the displayed discrete pose. captureTo supplies that here.
- kit/dance.js, trail and floor.resize: retained exposure endpoints need re-projection when the display height changes. This tool recalculates each ghost's world-space endpoints from its pose before the final resize render.
- kit/dance.js, floor.resize: ignore zero-sized hidden surfaces or retain the last valid projection. This tool guards layout and rhythm rendering during print/media transitions so hidden elements never produce non-finite geometry. The native beforeprint path also stops playback.
- kit/dance.js, dancer: expose its shadow node or a visibility method. Hiding the second figure's group leaves its independent shadow visible; this tool explicitly hides the matching shadow-layer child.
- kit/dance.js, voiceAt in the music section: optional brass-like stabs, sustained fiddle-like lead and scratch sweep instruments would make the Jazz, Irish and Breaking tracks closer to the spec. Current tracks use the available synthesized instrument palette and are labeled study tracks.
- kit/dance.js, skeleton and dancer: an optional hand-support ground set and articulated hand-shape/eye-direction hooks would improve breaking freezes and Bharatanatyam. The painted-pose adapter should preserve analytical joints rather than replace their calculations.

## Left open
- Owner review of the people contact sheet before shipping. Fresh cultural/representation review passed in refine/sensitivity.md.
- The inherited K-2 codes DA:Re7.1.1b and DA:Re7.1.2b conflict with this high-school spec. Catalog/spec correction is outside the authorized folders.
- No recorded upbeat-guide narration. Browser fallback remains; no audio was recorded.
- front-view painted articulation and synthesized study timbres simplify expert performance. Existing kit requests above remain suggestions, not authorized shared-file edits.
- The cold review's codex-review.md and Scratch review-audit supersede the builder verification status for the reviewed changes.

## Cold-review audit follow-up
The one review audit confirmed a 680 px hand-detail/level-label collision. The compact detail now sits left of the level labels. Painted-hand audit states use the visible native style selector on phones; the original phone steps had clicked a hidden desktop chip and remained on Ballet. Only these affected states were re-shot after the audit; no second full audit was run.
The Critique comparison toggle now updates the count readout immediately and clamps a completed loop when returning to one style.
Silent count steps keep the line already speaking, so a rapid second step no longer cuts off the first-tap welcome.

Saved-note feedback uses immediate event priority, so a closed form's instructions cannot delay its result; Read retains priority.



Opening another note lets its valid saved-note acknowledgment finish. Closed-form instructions can be superseded by Save.
