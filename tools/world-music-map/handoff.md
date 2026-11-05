# World Music Map handoff

Build only. No commit, deployment or polish round.

## Layout and implementation
src.html begins with the kit frame and local responsive CSS, followed by map geometry, ruler and circle renderers, mode logic, then the local audio adapter and lookahead clock. stops.json holds the ten complete stop records and exact sketch events. world.json is loaded by a bundle token. Seven supplied Met photographs remain intact. Four paintings have raw sources and processed WebP assets.

The map uses Equal Earth coordinates with small leader lines when nearby pins need separating. The stop card is 60 percent of the desktop stage. Short landscape previews use buttons first and internal card scrolling. Phone cards cover the map with Back to map. Compare hides the map.

Sound scheduling uses a 25 ms check and a 150 ms horizon. Source nodes retain start times. A setting change cancels future sources and rebuilds the next pulse. Sound off stops the master and the clock. Read stops music before using the kit voice queue. No narration recordings were made, as required by this build brief; the manifest uses knowing-guide and the browser fallback.

## Open question decisions
- Siku photo versus painting: used the spec's painting option. No photo was fetched. BASELINE also says to draw the siku.
- Family engine extraction: kept the adapter inside src.html because writes to kit are forbidden in this run.
- Compare welcome: omitted the optional pin-picking wording because this implementation uses the two pickers while the map is hidden. This keeps the hint tied to visible controls, as STANDARDS requires.

## Engine changes wanted
- File: kit/instruments.js (not present at build start). Functions: audio, stopAll, note, playTune and synth recipes. Extract the local adapter from this tool and orchestra-zoo's reusable routines, retain cents/base-frequency pitch input, tracked source cancellation and the shared noise buffer. This follows the spec while avoiding changes outside the allowed build folders.
- File: future kit/rhythm.js. Functions: startClock and stopClock. Expose the 25 ms timer / 150 ms lookahead clock with per-source cancellation and audio-clock visual events, so this tool and band-practice can share scheduling without changing their musical content.

## Review next
Cold review should listen to the timbre approximations and inspect the models against their musical sources. Synthesized sounds intentionally demonstrate tuning and organization rather than reproduce recordings. Cultural context is supplied by the stop facts and real-music links; each place represents one example rather than all music in that country.

The existing built neighbors orchestra-zoo and vanishing-point-studio have no handoff.md or refine.md files in this checkout. Their available source and the prescribed snowy-mail-route / beat-lab bars were inspected.

Build evidence, bounded command runner, calculations, frames and audit output are in _scratch/world-music-map/. Final check results and remaining limitations belong to codex-report.md.

## Final build checks and repairs
The full audit completed once with 101 mechanical leads. Every original bullet and flagged walk row has a response in _scratch/world-music-map/audit-responses.md. Pin and label packing now reserves whole rectangles, keeps all ten mystery answers visible, and uses leader lines when a pin moves from its true map position. Selected Map stops get placement priority; mystery answers never do.

Targeted checks after the audit cover the affected map sizes, the phone answer board, 48-pulse labels, center captions, same-mode quick taps, shared comparison axes, live drone resumption, and keyboard focus after Next mystery. The full audit was not repeated. Internal card scrolling remains intentional for pitch diagrams or the real-music link in compact views. Primary playback controls and all mystery answers stay visible.

The alternate koto and Rast headings identify comparison tunings. An active mode tap retains its welcome rather than cutting it. The 48-pulse labels use alternating radii. Indian drone plucks are scheduled one pulse at a time so switching on takes effect at the next note. The closing gong is lower and stronger than the smaller gongs.

Two supplied photos exceed the spec's stated 40 KB cap: tabla is 75.8 KB and saron 106.1 KB. They remain unchanged because the complete bundle is comfortably below 2 MB. The spec's example saying 16 fits twice into 48 is implemented as three, using computed division.

## Cold review repairs
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
