# World Music Map: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: world-music-map

#### Built
Built the offline Grade 6-8 listening atlas with all ten stops, Map, Compare and Where in the world?. Includes exact-cent rulers, layered rhythm circles, live experiments, synthesized phrases, drones, playable koto strings, map layers, zoom and pan, keyboard controls, teacher notes and narration manifest.

The bundle is 1,009,987 bytes, about 986 KiB. No automatic external resources, unresolved resource tokens, JavaScript syntax errors or em dashes were found. Source lines remain under 160 characters. No commits, branch changes, deployment or polish round were made.

#### Numbers check
- Independent calculations: `_scratch/world-music-map/compute_checks.py` and `numbers.json`.
- All ten specified contrast pairs match: 8.12, 7.34, 15.17, 6.44, 5.69, 6.34, 11.76, 5.36, 5.77 and 6.38 to one.
- Recomputed offsets, the half-key tie rule, koto gaps, badge counts, phrase totals, cycle durations and line-up lengths. Runtime checks cover all 100 ordered stop pairs.
- Phrase lengths are 16 pulses except Ghana 24 and Zimbabwe 48. Longest musical phrase is 13.333 seconds.
- Full scheduled traces for every cycle match every specified part's hit list. Maximum clock arithmetic difference was about 1.8e-15 seconds.
- Spec correction: 16 fits into 48 three times, not twice as one example says. The implementation computes three.
- Supplied asset discrepancy: tabla is 75.8 KiB and saron 106.1 KiB, exceeding the stated 40 KB photo cap. Kept the supplied images because the complete bundle is below 2 MB.

#### Feel check
Played through the ten stops, the comparison, mystery feedback, switches and keyboard path in muted Chrome. This checks interaction and scheduling, not a human listening review of the synthesized timbres.

Best moment: two different circles meet at their shared first pulse, with the 48-pulse explanation beside them. The closing gong and the mbira's interlocking parts provide distinct musical payoffs.

Two initially flat moments were comparison circles falling below the laptop frame and phone playback controls appearing after the diagrams. Adjusted comparison proportions and put phone playback controls first. Live setting changes, playable koto strings and moving bridges make the specified experiments immediate.

Both prescribed bar tools were bundled into Scratch and opened. The atlas keeps a deliberate museum finish with textured instrument portraits, lit land, engraved-looking rulers and layered circles. It does not need the density of Beat Lab's sequencer to look finished.

![World Music Map beside the Beat Lab finish bar](../../_scratch/world-music-map/feel-comparison.png)

#### Done when
1. PASS: all ten pins open their picture, three facts, ruler, cycle and specified experiment. The 230-check functional run passes after awaiting image decoding.
2. PASS: all cents match the content; half-flat labels read 50 below E and B. Java's four offsets and Scotland's 14 below C sharp and 16 below F sharp are displayed and checked.
3. PASS: every full cycle trace matches its source pulses. Teental has X, 2, 0 and 3; lancaran's lowest, strongest gong sounds on 16.
4. PASS: implemented and exercised every experiment. Checked live Rast retuning, isolated mbira and siku parts, koto bridges and strings, clave rotation, drone memory, slides and grace-note recipes. Siku's isolated ira phrase leaves the correct six sounding entries.
5. PASS: both cycles share a 200-pulse clock, every LCM is computed, equal and divisible cases have their own wording, and comparison rulers share one cents axis even when Scotland extends below zero.
6. PASS: first and second misses give different clues; the third reveals the answer. Correct choices alone increase found count. The shuffled deck excludes found stops.
7. PASS: at 1366x768, the map has 40 percent and the card 60 percent. The ruler and 260 pixel circle dominate the card and remain visible with Play cycle.
8. PASS: a ruler note sounds over a looping cycle. Future queued notes are cancelled and remade on a switch. Drone resumption matched the next scheduled pulse exactly, at 1.525 seconds in the targeted run. Stop fades sources within 35 milliseconds.
9. PASS: five held opens at two-second intervals start each how line at most once. Play hushes narration, Read stops music, and stale Try this guidance is dropped after a switch. Quick active-mode taps no longer cut welcomes.
10. PASS: laptop controls and diagrams fit; the 680x425 Map is readable; all ten answer pins remain visible at every tested size, including a 375 pixel iframe. Seven photos and four paintings are bundled under 2 MB. No picture shows a person.

#### Wave lessons
- PASS, hint and voice: hints change synchronously and name controls. Read uses the current hint. Kit heard state controls once-only guidance.
- PASS, focus and layout: rebuilding controls preserves or deliberately moves focus with preventScroll. Next mystery focuses Play phrase, including on phones.
- PASS, sizes: all STANDARDS sizes checked. Primary playback controls and mystery answers stay visible; targets are at least 44 pixels. Small cards use the allowed internal scrolling.
- PASS, no giveaways: mystery pitch, part and instrument names are hidden, including Indian bol text during playback. Badges become neutral dots and no mystery target gets placement priority.
- PASS, honest numbers: tuning models and sketches are labeled; modified Rast and koto headings identify comparison tunings; line-ups are computed.
- PASS, standards: solo actions teach context through stops and musical organization through rulers, cycles and experiments.
- PASS, motion off: full audit found no infinite animation. Sweeping hands stop; sound timing and discrete pulse feedback remain.
- PASS, short choices: all ten mystery answer pins stay visible and separate. Pitch diagrams and the optional source link may scroll inside compact cards, as the spec allows.
- PASS, resize mid-action: actual 1366x768 to 760x900 and back retained the running clock without exceptions. A fixed mystery retains its note IDs across seven sizes.
- PASS, late welcome: first taps with their own teaching line skip the Map welcome. Same-mode taps retain the welcome already speaking.
- PASS, unknown means unknown: mystery headings, pitch labels, part labels, pictures and facts do not expose the stop.
- PASS, one look means one meaning: parts have distinct shapes as well as colors, including after isolating a part.
- PASS, badges tell the truth: layer counts match content; active pulse captions say what the counter means; Stop restores cycle length.
- PASS, hints change back: stopping, closing, changing modes and returning to Map restore the matching next action.
- PASS, no word copying: mystery answers follow musical diagrams and listening, not repeated country or instrument names in a clue.

#### Audit leads
The full audit completed once, within its 40-minute limit, with 101 mechanical leads. It was not rerun after repairs.

Every original bullet and flagged walkthrough row has an individual disposition in [audit responses](../../_scratch/world-music-map/audit-responses.md). The main groups are:
- Fixed all pin/label collisions, clipped pin labels, and hidden answer targets with full rectangle packing and true-position leader lines. The phone packing case now retains all ten answers.
- Fixed center number/caption overlaps and adjacent 48-pulse numbers. Targeted geometry reports empty overlap and clipping arrays.
- Fixed the small real-music link target, phone text below 10 pixels, and moving layer controls.
- Fixed quick mode taps cutting their own welcome. All three targeted quick-tap logs contain one spoken line without a cut.
- Accepted compact card scroll leads: these concern pitch diagrams or the optional Folkways link, rather than hidden answer alternatives. Primary playback and all answer pins are visible.
- Explained welcome-not-heard flags: a first tap's own line must suppress the Map welcome under STANDARDS. Where speaks its welcome text as a how line, which the harness does not count as kind welcome.
- Explained mystery resize and unchanged-note flags: fresh audit pages deal different stops, with different note counts and locations. A constant mystery retains the same note IDs across seven actual viewport sizes. Held and keyboard ruler tests produce pitch events.
- Zoom out at 1x intentionally changes nothing. The source never disables ruler notes.

Full audit motion-off, repeated how-line checks, console-error columns and settled keyboard-focus checks were clean. Post-repair checks used only affected views and behaviors. Geometry evidence is in `geometry-results.json` and `geometry-results-small.json`.

#### Frames looked at
Inspected individual frames and labeled contact sheets for the two bar tools; quick, validation, full-size, music, final, repair, candidate and geometry batches; all 33 full-audit frames; and the targeted overlap repairs.

Coverage includes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe views; all ten cards; all modes; zoom extremes; bridges, parts and live sound; grayscale; Motion off; keyboard-only play; real held clicks and a real map drag.

The first HTTP host batch logged one favicon 404 from its generated host page. Later hosts use a data icon and the targeted batches have no console errors. No favicon or automatic external resource is required by the bundled tool.

#### Art made
Four paintings made with the built-in image tool, plus seven supplied Met photographs. The eleven processed WebPs total 493.5 KiB. The HTML totals 1,009,987 bytes.

Siku was redrawn twice to obtain exactly seven and six pipes. Cuba was redrawn once for traditional tacked bongo heads. All chosen images were processed with art.py --rekey and inspected at saved size. Prompts, provenance and redraw counts are in art/prompts.json; selected raw sources are in art/raw/.

#### Art still to paint
None. No people assets were requested or generated.

#### Engine changes wanted
Keep the shared kit unchanged in this build. handoff.md specifies the proposed kit/instruments.js extraction and future rhythm-clock integration, including exact functions, cents input and source cancellation. The working adapter remains local to src.html.

#### Left open
- A cold sonic and cultural review remains next. Browser synthesis intentionally demonstrates rules rather than reproducing recordings. Narration uses the browser fallback; no audio was recorded.
- Compact cards put some pitch diagrams or the optional real-music link inside their own scrolling area. All primary playback controls and all mystery answers remain visible.
- The full audit predates the final repairs; only affected checks were repeated. Its raw 101-lead report is preserved rather than presented as clean.
- The optional siku-photo question is resolved toward the specified painting. No image was fetched.

All Chrome instances and servers started by this build were closed. Ports 9980, 9981 and 8785 were confirmed closed. host.html is absent. No work remains before the build-only handoff.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: world-music-map

#### Played
Played all ten stops cold as a Grade 7 student, using held clicks, rulers, cycles, phrases and switches before reading builder material. Played Compare and wrong mystery paths, then checked the ten-stop deck. Revisited the projection and keyboard paths. The listening atlas has a strong identity; the live tuning and interlocking parts are its best moments.

#### Findings fixed
- Blocker, family:instruments, siku: isolated rows silenced the other row's ruler notes. Every ruler mark now sounds over the active cycle; phrase isolation still leaves holes. Verified the 300-cent arka note while Ira alone was selected.
- Should fix, family:instruments, siku cycle: pulses 6 and 7 sounded notes belonging to the opposite row. The eight pitches now follow A C D E G E D C, matching each part's row.
- Should fix, family:instruments, live slides: replacing lookahead notes now restores the previous audible pitch, so switching Slides on glides from the heard note rather than a cancelled future note. Cancelled events are marked in diagnostic traces.
- Should fix, family:instruments, Cuba art: the tres showed three single strings. Redrew it with six strings in three paired courses; fresh cultural recheck passed.
- Should fix, family:instruments, India: the specified Met sitar lacks sympathetic strings, contradicting the adjacent general fact. Retained the photo with an explicit historical-exception caption and notes clarification. Image descriptions now name the actual pictured objects.
- Should fix, family:instruments, Scales legend: Scotland's nine-note badge counts the chanter range. The legend now states that exception to notes per octave.
- Should fix, general, state feedback: Drone, Slides and Grace notes off no longer claim to restore the original sketch. Retuning clears old pitch details. Playback hints name visible controls; live switches mention Stop.
- Should fix, general, mystery feedback: both miss lines and the success line name the next action. Miss speech is invalidated when its attempt passes.
- Should fix, general, revealed mysteries: Next mystery was below the laptop fold. It now shares the playback grid; the count fits in the heading. Close returns to Map mode while retaining the found set.
- Should fix, general, medium comparison rulers: density-aware rows separate close 44-pixel pitch targets. Comparison circles use the available column width. Phone three-part choices stack so long labels fit.
- Should fix, general, scoped recheck: a deferred pan could run after its stop closed; it now checks the active stop and Map mode. Dense 48-pulse comparison labels use their own readable size instead of the enlarged short-cycle type.
- Polish, family:instruments, comparison payoff: both discs outline together and a highlighted reunion readout holds for two pulses. Timing and discrete feedback remain under Motion off; the readout fits at laptop sizes.
- Polish, family:instruments, part identity: isolating a part retains its original color and shape.
- Polish, general, art size: tall desktop cards show larger instrument portraits while preserving the ruler and circle.

#### Findings left
No confirmed blocker or should-fix remains. Compact cards and Compare use internal scrolling for secondary diagrams or the optional recording link; main playback controls and mystery answers stay available.

#### Flattest moment left
The plain eight-beat examples offer less to discover after one loop than the layered cycles. Kept the specified simple beats rather than adding an activity or musical claim.

#### Graphics
Checked all eleven images at their card size and all four generated portraits at saved size. Retained the seven Met photos and three strong paintings. Replaced the Cuba painting through built-in imagegen; prompt/provenance are in art/prompts.json and its selected raw PNG is in art/raw/wmm-cuba.png. No image contains people. Fresh cultural check: _scratch/world-music-map/sensitivity.md. Bundle: 1,019,680 bytes (995.8 KiB).

#### Audit
One full audit completed within 40 minutes, with 32 raw leads. Four confirmed overlap leads are fixed; the optional-link, stale-how, first-tap-welcome and randomized-mystery fixture leads have individual dispositions in _scratch/world-music-map/review-audit-responses.md. All 47 audit frames were inspected. Repeated and quick-tap voice checks were clean, with no console exceptions. Only affected views and behaviors were rechecked after the audit; no second full audit ran.

Targeted checks confirmed zero pitch-target overlaps, readable phone part names, stable notes and a running clock through an actual iframe resize, working mystery notes, live slide replacement from the prior audible pitch, Read with Sound off, and Map exit/zoom/pan. The targeted batches had no console errors, warnings or exceptions.
Independent recalculation matched every prescribed scale, hit list, badge count, phrase length, contrast pair and LCM. Contrast spans 5.36:1 to 15.17:1 for the specified pairs. A complete shuffled mystery deck contains ten distinct stops; found reaches ten. Held input, keyboard, grayscale and Motion off frames were inspected.

| Five held opens at two-second intervals | Kind | Expected starts | Actual starts |
| --- | --- | --- | --- |
| Syria introduction | how | 1 | 1 |
| Ruler instruction | how | 1 | 1 |
| Try this instruction | how | 1 | 1 |

Later actions intentionally interrupt speech; fast misses drop stale lines. Music starts by hushing narration. No automatic external resource is required. Evidence and targeted frames are in _scratch/world-music-map/.

#### Left open
- The spec's example says a 16-pulse cycle fits twice into 48; the correct computed value is three. Spec left unchanged.
- Two supplied photos exceed its old 40 KB per-photo target; the complete bundle remains below 2 MB.
- Shared engine extraction is outside the allowed folders; the local adapter and existing engine request remain.
- Browser narration remains because recording is prohibited. Muted automation checks timing and sound events, not a human assessment of synthesized timbres.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### World Music Map handoff

Build only. No commit, deployment or polish round.

#### Layout and implementation
src.html begins with the kit frame and local responsive CSS, followed by map geometry, ruler and circle renderers, mode logic, then the local audio adapter and lookahead clock. stops.json holds the ten complete stop records and exact sketch events. world.json is loaded by a bundle token. Seven supplied Met photographs remain intact. Four paintings have raw sources and processed WebP assets.

The map uses Equal Earth coordinates with small leader lines when nearby pins need separating. The stop card is 60 percent of the desktop stage. Short landscape previews use buttons first and internal card scrolling. Phone cards cover the map with Back to map. Compare hides the map.

Sound scheduling uses a 25 ms check and a 150 ms horizon. Source nodes retain start times. A setting change cancels future sources and rebuilds the next pulse. Sound off stops the master and the clock. Read stops music before using the kit voice queue. No narration recordings were made, as required by this build brief; the manifest uses knowing-guide and the browser fallback.

#### Open question decisions
- Siku photo versus painting: used the spec's painting option. No photo was fetched. BASELINE also says to draw the siku.
- Family engine extraction: kept the adapter inside src.html because writes to kit are forbidden in this run.
- Compare welcome: omitted the optional pin-picking wording because this implementation uses the two pickers while the map is hidden. This keeps the hint tied to visible controls, as STANDARDS requires.

#### Engine changes wanted
- File: kit/instruments.js (not present at build start). Functions: audio, stopAll, note, playTune and synth recipes. Extract the local adapter from this tool and orchestra-zoo's reusable routines, retain cents/base-frequency pitch input, tracked source cancellation and the shared noise buffer. This follows the spec while avoiding changes outside the allowed build folders.
- File: future kit/rhythm.js. Functions: startClock and stopClock. Expose the 25 ms timer / 150 ms lookahead clock with per-source cancellation and audio-clock visual events, so this tool and band-practice can share scheduling without changing their musical content.

#### Review next
Cold review should listen to the timbre approximations and inspect the models against their musical sources. Synthesized sounds intentionally demonstrate tuning and organization rather than reproduce recordings. Cultural context is supplied by the stop facts and real-music links; each place represents one example rather than all music in that country.

The existing built neighbors orchestra-zoo and vanishing-point-studio have no handoff.md or refine.md files in this checkout. Their available source and the prescribed snowy-mail-route / beat-lab bars were inspected.

Build evidence, bounded command runner, calculations, frames and audit output are in _scratch/world-music-map/. Final check results and remaining limitations belong to codex-report.md.

#### Final build checks and repairs
The full audit completed once with 101 mechanical leads. Every original bullet and flagged walk row has a response in _scratch/world-music-map/audit-responses.md. Pin and label packing now reserves whole rectangles, keeps all ten mystery answers visible, and uses leader lines when a pin moves from its true map position. Selected Map stops get placement priority; mystery answers never do.

Targeted checks after the audit cover the affected map sizes, the phone answer board, 48-pulse labels, center captions, same-mode quick taps, shared comparison axes, live drone resumption, and keyboard focus after Next mystery. The full audit was not repeated. Internal card scrolling remains intentional for pitch diagrams or the real-music link in compact views. Primary playback controls and all mystery answers stay visible.

The alternate koto and Rast headings identify comparison tunings. An active mode tap retains its welcome rather than cutting it. The 48-pulse labels use alternating radii. Indian drone plucks are scheduled one pulse at a time so switching on takes effect at the next note. The closing gong is lower and stronger than the smaller gongs.

Two supplied photos exceed the spec's stated 40 KB cap: tabla is 75.8 KB and saron 106.1 KB. They remain unchanged because the complete bundle is comfortably below 2 MB. The spec's example saying 16 fits twice into 48 is implemented as three, using computed division.

#### Cold review repairs
The cold pass preserved the map, supplied photos, exact-cent models, layered circles and live sound clock. Replaced the Cuba painting with a tres showing six strings in three paired courses. Fresh cultural review and targeted recheck passed in _scratch/world-music-map/sensitivity.md. The specified historical Met sitar has no sympathetic strings; its card and teacher notes now identify the exception to the general fact. The spec was left intact.

Fixed siku ruler notes being muted by the isolated-row setting. Ruler taps now always sound, while the phrase still leaves the intended holes. Siku cycle pitches now follow A C D E G E D C, so ira/arka labels agree with their notes on all eight pulses. Isolating a part retains its original shape and color.

When replacing future notes, reviseFuture marks cancelled diagnostic events and restores China's glide origin from the last audible note. A queued note must not become the starting pitch for a slide after that note is cancelled. Note traces include the glide's from frequency for the targeted check.

Drone, Slides and Grace notes have accurate off-state explanations. Live setting hints refer to Stop while playing. Comparison-scale and mystery playback hints name visible controls. Miss feedback has attempt-specific validity and includes the next action. The voice manifest matches the revised fixed lines.

Comparison reunion now outlines both discs and highlights the shared-pulse message for two pulses, with identical timing and discrete feedback under Motion off. Compact comparison rulers leave that message in view. Revealed mysteries put Next mystery beside Play cycle, and the found count shares the heading line so the cycle and next action fit together.

Audit-frame followups use density-aware ruler rows for close notes at medium widths, full-size circles within each comparison column, and vertical phone part choices so Kutsinhira fits. Closing a mystery returns to Map mode, keeping its found set, rather than leaving a hidden mystery handler behind a Map hint.

The Scales legend clarifies that Scotland's nine-note badge covers the full chanter range. Other scale badges retain the specified notes-per-octave meaning; the Ewe sketch counts its two bell tones.

The deferred stop-pan callback verifies both Map mode and the active stop before changing zoom or pan. Dense 48-pulse comparison numbers keep a smaller label size than short-cycle numbers; center readouts remain large.

Independent recalculation is in _scratch/world-music-map/numerical_review.py. Targeted frames, sound traces, five-open voice counts and the shuffled ten-stop deck check are in the rechecks folder and JSON files. The review audit is a separate, single final run at _scratch/world-music-map/review-audit. See codex-review.md for its final dispositions. Narration remains browser fallback as recording is prohibited; muted automation verifies sound scheduling rather than a human timbre assessment.

The review audit completed within its 40-minute cap with 32 raw leads. Four confirmed overlap leads were fixed; all other leads are individually explained in _scratch/world-music-map/review-audit-responses.md. All 47 audit frames were inspected. The scoped final batches and assertions passed, including keyboard, live slide origin, Sound-off Read, fixed-mystery resizing, phone part labels and map exit/pan. No second full audit ran. Used Chrome/server ports are closed and host.html is absent.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
