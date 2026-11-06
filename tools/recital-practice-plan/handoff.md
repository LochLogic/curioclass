# Recital Practice Plan build handoff

## Cold review changes

Preserved the painted rooms, brass program board, model and deterministic takes. Listen now withholds diagnostic x marks, timing ticks, velocity shading, actual BPM and readiness readouts until meter reveal. Reveals are tracked per criterion, so swapping the rubric cannot expose a new meter without a judgment. Agreement uses immutable first ear values, and each meter can be revealed only once per criterion. The sheet follows the same rule.

Shortened Practice, Listen and Recital how lines and added the rating instruction at take completion. Listen entry drops stale planning narration before its short how line. Match voice/lines.json to the source before recording.

Added a shaded SVG keyboard inside the existing recital program card. It lights actual saved pitches using the existing playback frame, resets between pieces and on Stop, and adds no scoring or input. The metronome was processed again with art.py --rekey and holes:true to remove the green fringe.

Skip-all no longer marks a recital complete. The last finished playback records skipped and missing passages on the sheet. Program changes invalidate that record, fewer than two pieces cannot begin, and old saves without this playback record cannot retain a legacy completion badge. Takes and practice progress remain intact.

Compact Listen uses one toolbar so five first-ear rows fit. Revealed comparisons use content-height rows in a keyboard-scrollable region. Phone recital cards use a compact grid; long introductions scroll inside their own area without covering the program or keyboard. Subsecond timing overruns say Just over rather than Over by 0:00.

The final audit confirmed hidden phone reorder buttons. Selected programs now expand to all rows; Notes moves into the phone header with its full accessible name and keeps focus across resizing. The venue paintings remain in the choice cards and full recital scene. Empty/one-piece panels use less blank height. At 1280x720, tighter practice spacing keeps the Flow control visible. Recital BPM stays labeled as the captured target until that take's tempo judgment has been revealed, closing a side path around Listen's blind comparison.

## Structure

src.html starts from the kit starter, with kit:curio and kit:theme-912. CSS lays out four responsive views at real pixel sizes. content.json is bundled through json:content and holds piece facts, note attacks, hand labels, criteria, venue notes and score provenance. The script contains state, model, deterministic takes, program editor, rubric, weekly board, piano-roll renderer, Web Audio voice, recital scheduler and device-only persistence. window.__tool exposes the model, state and principal actions for review.

Recorded takes are stored as immutable note events with a seed, captured tempo, readiness and metrics. Future plans do not regenerate them. Audio schedules oscillator onsets against AudioContext time rather than animation frames. Two detuned triangles have a fast decay. Stop disconnects every oscillator synchronously. Sound off disconnects audio without changing visual timing; Sound on schedules only future notes.

While a take plays on a wide screen, the board contracts to 300 pixels so the piano roll becomes the main view. Closing Listen restores the full board while playback continues. Narrow Listen hides and makes covered controls inert, moving covered keyboard focus to Play take. Native dialogs make the background inert and restore focus on close, including Escape. Start over focuses the new Practice week.

Curio.voice owns fixed narration and Read. Hints change synchronously and lines have validity checks. voice/lines.json names easy-coach, Umbriel. No speech is recorded in this build, so narration uses the browser fallback. Introductions are displayed, not spoken.

## Open questions and resolved ambiguities

The spec has no explicit open-question list. These conflicts or unspecified choices follow its stated direction:

- The user requests image-tool art during the build. All five assets were made with the built-in OpenAI image tool, despite the older Art paragraph naming local FLUX. No generated people or body parts. Audience silhouettes are code shapes as specified.
- The report is assembled in Scratch and written to codex-report.md only at the end. The user's instruction to stop as soon as that file is written takes precedence over the brief's request to start it early.
- The written exponential formula wins over narrative approximations. Four-piece, nine-unit even-split results are 56.36 to 73.67% at 30x5; 73.13 to 89.17% at 45x6; 81.32 to 94.44% at 60x6; and 81.09 to 94.32% at 60x7. The last case is slightly below 60x6 because 420x0.85 is 357, not 360 effective minutes.
- Three-piece Entertainer reaches 63.01% with 270/7 minutes per unit for four weeks. At 35% of each week's minutes it reaches 87.91%, rather than the spec's 85%. The other 65% divided across six units gives Gymnopédie hard 84.96% and Night Bus hard 72.38%, rather than both being 72 to 79%. Formula and difficulties are retained; spec.md is unchanged.
- Exact even splits of 150, 360 and 420 minutes across nine units cannot use the required 15 minute slider step. Formula checks use exact fractions. The 270-minute even split is achievable in the UI at 30 minutes per unit.
- Gymnopédie's complete eight-bar passage takes 20 seconds at the listed tempo even at full readiness. The Entertainer's four 2/4 bars take 6.32 seconds. Neither can meet the overview's 8 to 15 second range without changing music or tempo. Full notes and model tempo win. The complete four-piece keyboard run took 80.7595 seconds, exceeding the roughly one-minute target.
- The Flow rule's one-to-four-second pause takes precedence over the overview's fixed one-second pause.
- The beat meter measures actual root mean square timing offsets from the saved take. The stated standard deviation is a distribution parameter, not a finite-sample guarantee; the model note explains the measurement.
- Fixed meter thresholds remain fixed when descriptors are edited. Shape and Keeps going remain ears-only.
- Practice and First read require three chosen rubric criteria. An early First read routes to Rubric and focuses the first criterion, so a student establishes criteria before hearing a take. The intermediate level 3 and 2 descriptions are fixed neutral scaffolding; the specified level 4 and 1 fields are editable.
- Playback reports actual BPM beside the take's captured target BPM. Later tempo changes affect future takes only. A newly added piece without a selected week's take falls back to its First read.
- Minuet's explicit right-hand sequence wins over engraved ornaments. Satie ties are merged, including the F sharp across bars 9 to 12. Joplin A-section bars 5 to 8 mean printed bars 9 to 12 after the introduction. Mutopia public-domain original-edition sources cross-check the IMSLP scans.
- The compact board uses two columns of 44 pixel rows to preserve the standing target-size rule. A four-piece set keeps nine units visible. Readiness words and numbers move into the unit name block. Five pieces may need board scrolling on short screens.
- All five Add choices remain visible on phones. The selected program's ordering controls scroll inside its shorter strip there. The editable rubric and long introduction dialog also scroll on compact screens. These are documented limitations, not hidden answer choices.
- Venue notes, reflection and introductions are under Venue notes & introductions immediately beneath the program. Its dialog preserves the large program and repertoire choices.
- A piece added after week 4 has no week 4 practiced take. Recital and sheet label the missing take and invite a new practice cycle. No performance is fabricated.
- Recorded weeks are read-only. Their takes can replay while an unplayed week's sliders are edited. Week board closes the listening sheet without stopping the take; First read or Listen returns to Stop.

## Engine changes wanted

None. No kit engine changes are required.

## Sensitivity

This is a small European and American piano selection, not a survey of musical cultures. Keep Christian Petzold's authorship distinct from Bach's notebook and credit Scott Joplin as the composer of The Entertainer, rather than treating the later film as its origin. A cultural reviewer should consider the senior-center notes' assumptions about listeners' childhood repertoire and film familiarity. The fictional venue notes are guidance, not facts about older adults. All five paintings contain no people; the audience uses code silhouettes.

## Art

Five paintings are in art/raw with finished WebP assets in art/. Full prompts and codex provenance are in art/prompts.json. Backgrounds are 1200 pixels wide. Senior and cafe were recompressed at quality 65 to stay below 120 KB each. The metronome uses a green-key cutout with despill and a code pendulum.

## Review next

Read codex-report.md for final checks and audit dispositions. The full audit finished once with 217 leads and 83 frames. _scratch/recital-practice-plan/audit-dispositions.json accounts for 212 bullet leads and the five first-Add welcome leads. Targeted repairs address tempo labels, 44 pixel targets, covered controls, dialog names, compact recital actions and focus. The full audit was not repeated after those repairs. The final functional run passed 49 checks; 16 additional closing assertions passed. Earlier model and boundary checks passed 172 assertions.

Evidence lives at _scratch/recital-practice-plan/ in the repository. This is Build only, with no commits or polish round. Headphone review of the piano and naturalness of browser narration remain human review tasks. Browser voice is a fallback, not a recording of Umbriel.

The required baseline bundle commands refreshed two ignored generated HTML files outside the authorized folders. Their sources were untouched. That was a scope mistake and was disclosed during the build. All authored content and evidence are in the authorized tool and Scratch folders.
