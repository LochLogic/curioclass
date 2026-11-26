# Poem to Movement: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: poem-to-movement

#### Built

Offline grades 3-5 tool with six poem, painting and sound sources; 4-6 selected details become an editable dance.
Source, Moves, Map and Viewer use the shared dance engine, with thirteen verbs, four qualities, live edits,
reordering, drawn pathways, a numerical Viewer, partner guessing, revision guidance and local saved work.
The stage has four original painted images, directional light, a temporary kit dancer, count cues and synthesized sound.
All authored files stay inside the two permitted folders. No commits, branch changes or polish round.
Final bundle: 997,177 bytes. Chrome 9990/9991 and host 8795 were closed; temporary host files removed.

#### Numbers check

Independently recomputed before implementation: `_scratch/poem-to-movement/numbers.txt`.
All six defaults are recognized. Runner-up margins: Wind .50, Train 1, River 1, Storm .75, Rain 1.25, Drum .75.
There are 21 nearest-profile ties among 96 homogeneous phrases. River revisions reach Storm or Rain at distance .25.
Four/five/six-card dances last 10/12.5/15 seconds, plus a 2.5-second count-in.
All seven specified contrast ratios match: 8.39, 7.79, 14.83, 6.14, 13.09, 12.20 and 15.97.
Poem punctuation and Rossetti's printed "thro'" variant follow the source edition; details are in handoff.md.

#### Feel check

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

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Inspected both bar tools, all four finished WebP images, and every PNG captured in the following Scratch sets:
`first-frames`, `check-frames`, `size-frames`, `phone-frames`, `input-frames`, `extra-frames`, `final-frames`,
`candidate-frames`, `final-check-frames`, `lead-frames`, `caption-frames`, `smoke-final-frames`, `rain-map-final-frames`.
The full size run covers all four modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
Hosted 375-wide views include both poems, all modes and final caption placement. Grayscale and Motion off inspected.
All 35 audit PNGs were inspected through six contact sheets; filenames recorded in `audit-viewed.json`.
Later screenshots were limited to changed layouts and interactions. The bar comparison was also inspected.

#### Art made

Four original gpt-image paintings: river, storm, paper backing and empty studio. No people generated.
Final WebP total: 290,064 bytes, 283.3 KiB. Final bundle: 973.8 KiB, below 2 MB.
All four processed through art.py --rekey and viewed at output size. No redraws required.
Generated-image credit is in tool.draft.json. All four images are used in the tool.

#### Art still to paint

156 requests marked people true: thirteen verbs x three levels x two weights x two keyframes.
The owner wants painted dancers. The kit figure is temporary; createActor isolates the replacement.
All requests have reserved art tokens; frames carry pose, phase and quality metadata for the painted adapter.
Reuse the previous frame for freeze. Deduplicate poses or use an atlas to retain the bundle budget.

#### Engine changes wanted

Three exact requests and current workarounds are in handoff.md: dance.floor.draw marley/barre options;
dance.phrase.at custom pose callbacks; dance.floor.resize actor heights below its current minimum.
No shared kit file was changed.

#### Left open

- Painted dancer work above remains for the next painter and owner review.
- Browser speech is the fallback. No recorded narration was made, as instructed; planned bank is gentle-storyteller/Vindemiatrix.
- All Chrome testing was muted. Synthesized source timbres, music and narration need human listening review.
- Secondary Reset/closing-sentence scrolling, intentional sideways strip and small portrait Map studio remain.
- Real S and zigzag examples pass; this is not exhaustive recognition testing of every hand-drawn shape.
- Family catalog/doc registration is unresolved outside the permitted folder; the spec's dance-engine option was taken.
- The full audit predates the focused repairs. No second full audit or polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: poem-to-movement

#### Played
Cold grades 3-5 solo and projector walk: Wind through Source, Moves, Map, Viewer and Partner before builder notes/source.
Then exercised both paintings, both sounds, six-card Train, wrong reading/revision, ties and saved reloads.
Best moment: the same River phrase can read as Storm, then the outlined cards give revision a purpose.
The paper, landscapes, studio light and direct quality controls were strong and retained.

#### Findings fixed
- Blocker, general, Partner: a held guess before any dance unlocked a correct model result and reflection.
  Require a complete phrase; solo previews, Stop and a reorder straight to the last slot cannot unlock choices.
- Should fix, general, voice: the two-second path cut Make moves and mode guides. Shortened queued instructions,
  retained a still-relevant guide over the count-in, and added the partner's post-performance action line.
- Should fix, family:dance, Map: drawing/clearing paths left an old interpretation attached. Invalidate that result.
- Should fix, family:dance, saved Map: restore and reorder dropped null in-place slots, shifting later travel.
  Preserve card-aligned slots; exact geometry now survives reload, a real reorder drag and another reload.
- Should fix, family:dance, freeze: weight/level modifiers altered the preceding pose. Hold that actual pose unchanged.
- Should fix, general, meters: a 50/50 average was called mostly one side. Name an equal mixture explicitly.
- Should fix, family:dance, art: replaced the temporary capsule figure and all card icons with articulated painted art.
  Two atlases provide three children from front/back, six base views instead of 156 missing pose requests.
- Should fix, general, compact layout: Map Reset was clipped and the Viewer eye covered caption text.
  Compacted Map qualities, reserved the eye, shortened the result subline and kept Play available while scrolling.
- Polish, general, payoff: the reading now appears in the studio's large caption; an ambiguous reading stays ambiguous.
  Removed the model-match victory chime so a supplied recipe is not presented as a skill award.

#### Findings left
- Should fix, spec: smooth/sharp is labeled Flow; Gilbert distinguishes Energy from free/bound Flow.
  The required control remains, with an explicit correction in notes. Changing the spec's vocabulary was not authorized.
- Polish: compact phrase cards scroll sideways, as the spec requires. Secondary reflection/Reset, including the phone Map footer, can require vertical scrolling.
- Nit: paper-puppet joints are visible during deep bends. Source art, shapes and live qualities remain legible.

#### Break it
- Highlight gate: three details and repeat-tapping one detail do not enable Make moves. Six is the largest offered set.
- Recognition: four supplied defaults can match without revision, intentionally per spec. This is an open studio,
  not a mastery assessment; notes now say so. There is no score, best score or saved achievement.
- Partner: guessing immediately previously passed. After repair it returns result null, choices disabled, reflection hidden.
  A complete dance enables one choice; that choice reveals both readings. Skipping to the tail stays blocked.
- Model/meters: independently checked all six defaults, River to Storm/Rain, 96 uniform quality combinations and 21 ties.
  Ties circle both sources. Meters stay hidden before the performance and throughout the partner's blind choice.
- Map: actual whole-pixel S and jittered zigzag drags give curved and zigzag paths. In-place cards stay in place.
  Clearing and drawing invalidate results; edited cards, path geometry and the sentence survive reload. Null slots and reordered geometry compare exactly: `map-slots-*.json`.
- Live controls: a quality tap applies during playback; Stop and keyboard Space stop; Alt-arrow reorder retains focus.
- Reflection: optional personal connection, not a correctness gate and no question assumes an error the child never made.

#### Voice walk
One continuous held-input walk at two-second tap pace, default Sound on: choose Wind, four highlights, Make moves,
Play phrase, wait for the phrase, Map, Draw path and actual S drag, Viewer, Show the Viewer, wait for result.
Final starts, in order: welcomeSource, highlightHow, makeHow, welcomeMoves, mapHow, drawHow, welcomeViewer, guessRight.
Every guide finished without a cut. Log: `_scratch/poem-to-movement/voice-walk-final/main.json`.
| Line kind | Expected | Heard |
| --- | --- | --- |
| Each main-path guide | 1 | 1 |
| Viewer result over five complete plays | 5 | 5 |
| Runtime/manifest lines | Same set | 78/78 |
Repeated result speech stops when a new performance starts; no old result speaks over the next dance.
Partner side path hears partnerHow, partnerChoose, then its result. Read and Sound receive the final audit checks.
Speech uses the browser fallback; no recorded bank voice or human listening claim is made. Chrome was muted as required.

#### Facts checked
- Rossetti credit, all eight lines and `thro’` edition variant: [Project Gutenberg 76703](https://www.gutenberg.org/cache/epub/76703/pg76703-images.html).
  The 1872 original date is distinguished from the 1893 enlarged edition: [UPenn Sing-Song](https://digital.library.upenn.edu/women/rossetti/singsong/singsong.html).
- Stevenson credit, first eight lines and punctuation: [Project Gutenberg 25609](https://www.gutenberg.org/cache/epub/25609/pg25609-images.html).
  Collection date 1885: [Scottish Poetry Library](https://www.scottishpoetrylibrary.org.uk/poem/railway-carriage/).
- Creation, revision, grade 3 picture-map notation and connecting dance to experience: [NCAS Dance](https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&grade_level=3rd%2C4th%2C5th).
  Notes now distinguish these activities from complete coverage of every grade-level subpart, including multi-dancer notation.
- Speed, weight, levels, pathways and the Energy/Flow distinction: Alabama State Department of Education,
  [Arts Education Course of Study, Appendix D](https://arts.alabama.gov/PDF/AIE/ALC/2017%20Arts%20Education%20COS.pdf), adapted from Anne Green Gilbert.
- The original River's woodblock influence: The Met, [Woodblock Prints in the Ukiyo-e Style](https://www.metmuseum.org/essays/woodblock-prints-in-the-ukiyo-e-style).
- The original Storm's dramatic landscape convention: The Met, [Romanticism](https://www.metmuseum.org/essays/romanticism).
  Neither image is attributed to a historical artist or presented as a historical reproduction.
- Viewer profiles, arithmetic and synthesized moments are authored models, not claims about universal dance meanings.
  Independent script: `numbers-review.json`; margins .50, 1, 1, .75, 1.25, .75; 21/96 ties.
  At 96 beats/minute, 4/5/6 moves take 10/12.5/15 seconds plus 2.5 count-in seconds.
  All seven specified WCAG contrast ratios reproduce: 8.39, 7.79, 14.83, 6.14, 13.09, 12.20, 15.97.

#### Sensitivity
Fresh cultural review should inspect the Japanese woodblock influence without treating one landscape as a culture,
and verify the original-art credit remains clear. Inspect the cast, deep bends and turns for respectful bodies,
natural skin tones, believable prosthesis attachment and equal agency. No child is linked to a source or stereotype.
Comfortable seated/standing adaptations are named in notes; no body type or ability receives a score.
People contact sheet: `_scratch/poem-to-movement/review-contact/people-magenta.jpg`.

#### Flattest moment left
The second unedited replay adds little: a default recipe is already readable. The spec leaves experimentation open.
The first payoff is stronger now because the interpretation lands on stage, beside the child's own phrase.

#### Graphics
Retained and inspected all four original WebPs at output size; painted two new front/rear cast atlases with imagegen.
Assets: `art/dancer-cast.webp` and `art/dancer-cast-back.webp`, both `people: true`, drawn_by codex, credited.
Checked source paintings, cutouts on magenta, small card icons, high/low poses, rear views, grayscale and Motion off.
`createActor`/`paintActor` isolate replacement; shared engine joints, timing, paths and pose logic stay in use.
One independently selected cast per device avoids giving Partner a source clue. No missing art tokens remain.
Six WebPs total: 446.1 KiB; final bundle 1127.0 KiB (1,154,003 bytes). Beat Lab comparison is `review-comparison.jpg`.

#### Audit
One audit completed within the 40-minute limit: 23 leads, 51 frames, Chrome 9961 and host 8765.
Opening screen clean at all eight sizes; no console exceptions, endless animation or resize failures.
- 1 desktop Map Reset lead group: fixed at 680 and 1280; targets remain at least 44 pixels.
- 6 secondary-scroll lead groups: retained as scrolling fields/footers, including phone Map Reset.
  Play remains visible; the phone result and Read explicitly direct students to the personal sentence below.
- 5 sideways phrase-strip groups: retained as the spec explicitly requires; keyboard access/reordering verified.
- 11 welcome warnings: expected first-tap contextual instructions/poem reading replace a stale picker welcome.
  The continuous main path hears every guide once; audit repeat/quick-tap checks were clean.
All 51 audit images inspected, with manifests/contact sheets in `audit-contact/`.
Only affected frames re-shot at 680, 800, 1280, 1366 and hosted 375. Final caption/phone batch: zero errors.
A Scratch host-only favicon 404 was corrected in that test shim; the tool has no external references.
The saved-map exact comparison caught a further slot-shift defect; its four scoped checks pass with zero errors.
Wave lessons checked: live hints/focus, targets, no blind-source leaks, disclosed averages, real standards activities,
calm timing, complete source/partner choices, resize safety, contextual welcomes, truthful labels and returning hints.
The full audit predates these focused repairs. No second full audit or new polish round.

#### Left open
Flow/Energy spec correction, broader grade-level standard coverage and family catalog registration need changes outside scope.
Audio timbre and browser narration were instrumented with real timing; a human listening review remains unperformed.
All Chrome/server ports started here are closed. No git commits, deployments or writes to other tools. The review is one look/fix/check pass; no second full audit.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Poem to Movement build handoff

#### Structure

`src.html` starts from the kit starter, with a real-pixel responsive stage and a controls-first DOM. `content.json` is inlined by the bundler. It holds six profiles, highlight defaults and the two poem texts. The shared dance engine supplies floor, actor, poses, qualities, clock, counts, music, pathways and path recognition.

The tool's `basePose` adapter expresses the thirteen verbs. `createActor` and `paintActor` isolate the
painted renderer. Two generated atlases contain front and rear views of the same three children, one base
pose per child per view. SVG windows articulate their painted limbs at the shared engine's projected joints.
Card icons use the same painter. The hidden engine actor supplies geometry and a floor shadow only.
The cast is selected independently of the source and stored under `_cast` in this tool's local saved object.

To swap the figure, replace those two assets and the reference rectangles/joint anchors in `paintActor`, or
replace that factory while preserving the actor interface. Timing, qualities, pathways and scoring stay shared.
Both assets are marked `people: true`. The superseded 156 undrawn pose requests are preserved for provenance
in `_scratch/poem-to-movement/prompts-before-review.json`, rather than retained as missing art tokens.
The originals' detailed paintings and studio were kept. Contact sheets and pose checks are in review Scratch.

#### Open question decision

The catalog says family none, while the spec explicitly requires the dance engine. Kept the catalog untouched and used the dance engine, following the spec's leaning and KIT's shared-engine rule. A catalog/family-doc update remains outside this tool's allowed write scope.

#### Source fidelity

The Gutenberg Rossetti edition reads “bow down their heads,” so the highlight is “bow down,” matching the spec's content table. Train uses the first eight lines, as requested; a comma after “battle” was removed to match Gutenberg. The script's independent numbers agree with all Source arithmetic, including 21 ties among 96 homogeneous phrases.

Rossetti's “thro’” is preserved on the poem card and maps to the content table's expanded “passing through” move label.

#### Tricky parts

Quality changes are staged until the next count. Reordering seeks the moved card's new slot at the next count. Motion off samples once per count without shortening playback. Stop cancels the clock and music immediately. A source switch, step switch and reset also hush narration and source sounds.

The map uses a top-down affine floor projector with `Dance.readPath`, so its geometry is judged as drawn. Floor coordinates are padded and clamped. Default paths are regenerated from card choices; drawn coordinates are stored separately. Path-count ties use the declared Straight, Curved, Zigzag order for deterministic results.

A long single part splits continuously between traveling moves. If the drawing has more parts than traveling moves,
the moves take the first parts in order. Backward live reorder seeks are deferred to a microtask after the clock tick.

How lines use Curio.voice, with state-scoped validity and repeating result events. No voice recordings were generated, per the build-only brief. The selected bank voice is gentle-storyteller; browser fallback may sound different.

#### Engine changes wanted

- `kit/dance.js`, `floor().draw`: add options to hide the studio barre and choose marley rather than planks. The tool removes those decorative nodes after resize without changing the shared engine.
- `kit/dance.js`, `phrase().at`: expose a pose function for custom verbs, live speed/weight edits and freeze of the actual previous pose. The tool samples the shared phrase's travel and uses its own pose adapter at the shared clock's position.
- `kit/dance.js`, `floor().resize`: allow dancer height below 18 floor units for compact preview proportions. The tool scales the actor down from the minimum when needed.

#### Next

Cold review repairs and validation are recorded in codex-review.md. The original build record remains in codex-report.md. No commits or second full audit.

#### Build verification and remaining limits

The one mechanical audit completed with 37 leads. It found no console exceptions, infinite motion or resize failures.
The report groups every lead's disposition. Only focused checks followed the repairs; the whole audit was not rerun.
Evidence is in `_scratch/poem-to-movement/`, including the full audit, numbers, held-input checks, frame sets and comparison.

All six defaults and the storm/rain river revisions passed. Real S and zigzag drags, live edits, backward/forward reorder,
Stop, keyboard creation, Alt-arrow reorder, partner concealment, Motion off and saved-work reloads passed.
Five Viewer plays produced five spoken result events with how lines heard once. The review rechecks the runtime line list against the recording manifest after instruction changes.

The short preview moves the six Viewer source cards below the studio so all are visible together. Both phone poems fit
with 44-pixel highlights. Counts live beside the move caption in Moves and Viewer to clear traveling dancers.
The phrase strip scrolls sideways as the spec requires. Start over and the closing sentence can need vertical scrolling
in short or phone layouts. The miniature Map studio is small in portrait layouts. Narration and synthesized audio still
need a listening review; all Chrome testing was muted. No recorded narration was made, per the build instruction.

#### Cold review changes

Fixed stale Viewer results after drawing or clearing a map, retained still-relevant mode narration when Play
starts, shortened entry instructions, and made freeze keep the actual preceding pose without reapplying
different weight/level modifiers. Balanced quality averages are described as equal mixtures.
The result now lands in the studio caption as well as the Viewer's bubble. Model matching has no victory chime.
Partner choices require a complete phrase performance; a solitary card preview or skipped/reordered tail
cannot stand in for watching the whole phrase. Final review evidence and remaining limits are in codex-review.md.

#### Sensitivity

Fresh cultural review should check the River's woodblock influence is named without claiming an authentic
Japanese artwork or representing a whole culture. Neither landscape is a historical reproduction.
Inspect both painted cast atlases and articulated low/turning poses for respectful bodies, natural skin tones,
believable prosthesis attachment and equal agency. The children are not tied to a source or stereotyped role.
Students may use their own comfortable seated or standing movement; no body type is graded.

#### Spec corrections wanted

The spec's smooth/sharp Flow label disagrees with Gilbert's energy versus free/bound flow distinction.
Notes explain the limit; changing the required student control needs a spec correction.
Broad module anchors do not mean every grade 3-5 substandard is covered by this single-dancer tool.
The old family registration question remains outside the allowed write scope.

#### Final audit layout repairs

The single review audit had 23 leads, grouped in codex-review.md. Map's four qualities now share one row,
which restores the desktop Reset at 680 and 1280 widths without reducing the scene. Viewer captions reserve
space for the eye badge and use a short subline so they clear the dancer's feet at 680 width.
Play is sticky while the panel/body scrolls, and the phone result explicitly directs the student to the
personal sentence. Secondary Viewer fields/Reset and the phone Map footer can still need vertical scrolling.
The specified compact phrase strip remains horizontal. All 51 audit frames were inspected; only affected
layout frames were re-shot after the audit. No second full audit was run.

#### Saved map slot repair

`state.map` is aligned with cards and contains null for an in-place move. Restore and reorder must preserve
those slots. Filtering them out shifted subsequent travel onto the wrong card. The final real-drag save,
reload, in-place-card reorder and second reload checks preserve all geometry exactly. Evidence:
`_scratch/poem-to-movement/map-slots-*.json` and `map-slot-frames/`.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
