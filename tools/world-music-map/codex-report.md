# Codex report: world-music-map

## Built
Built the offline Grade 6-8 listening atlas with all ten stops, Map, Compare and Where in the world?. Includes exact-cent rulers, layered rhythm circles, live experiments, synthesized phrases, drones, playable koto strings, map layers, zoom and pan, keyboard controls, teacher notes and narration manifest.

The bundle is 1,009,987 bytes, about 986 KiB. No automatic external resources, unresolved resource tokens, JavaScript syntax errors or em dashes were found. Source lines remain under 160 characters. No commits, branch changes, deployment or polish round were made.

## Numbers check
- Independent calculations: `_scratch/world-music-map/compute_checks.py` and `numbers.json`.
- All ten specified contrast pairs match: 8.12, 7.34, 15.17, 6.44, 5.69, 6.34, 11.76, 5.36, 5.77 and 6.38 to one.
- Recomputed offsets, the half-key tie rule, koto gaps, badge counts, phrase totals, cycle durations and line-up lengths. Runtime checks cover all 100 ordered stop pairs.
- Phrase lengths are 16 pulses except Ghana 24 and Zimbabwe 48. Longest musical phrase is 13.333 seconds.
- Full scheduled traces for every cycle match every specified part's hit list. Maximum clock arithmetic difference was about 1.8e-15 seconds.
- Spec correction: 16 fits into 48 three times, not twice as one example says. The implementation computes three.
- Supplied asset discrepancy: tabla is 75.8 KiB and saron 106.1 KiB, exceeding the stated 40 KB photo cap. Kept the supplied images because the complete bundle is below 2 MB.

## Feel check
Played through the ten stops, the comparison, mystery feedback, switches and keyboard path in muted Chrome. This checks interaction and scheduling, not a human listening review of the synthesized timbres.

Best moment: two different circles meet at their shared first pulse, with the 48-pulse explanation beside them. The closing gong and the mbira's interlocking parts provide distinct musical payoffs.

Two initially flat moments were comparison circles falling below the laptop frame and phone playback controls appearing after the diagrams. Adjusted comparison proportions and put phone playback controls first. Live setting changes, playable koto strings and moving bridges make the specified experiments immediate.

Both prescribed bar tools were bundled into Scratch and opened. The atlas keeps a deliberate museum finish with textured instrument portraits, lit land, engraved-looking rulers and layered circles. It does not need the density of Beat Lab's sequencer to look finished.

![World Music Map beside the Beat Lab finish bar](../../_scratch/world-music-map/feel-comparison.png)

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
Inspected individual frames and labeled contact sheets for the two bar tools; quick, validation, full-size, music, final, repair, candidate and geometry batches; all 33 full-audit frames; and the targeted overlap repairs.

Coverage includes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe views; all ten cards; all modes; zoom extremes; bridges, parts and live sound; grayscale; Motion off; keyboard-only play; real held clicks and a real map drag.

The first HTTP host batch logged one favicon 404 from its generated host page. Later hosts use a data icon and the targeted batches have no console errors. No favicon or automatic external resource is required by the bundled tool.

## Art made
Four paintings made with the built-in image tool, plus seven supplied Met photographs. The eleven processed WebPs total 493.5 KiB. The HTML totals 1,009,987 bytes.

Siku was redrawn twice to obtain exactly seven and six pipes. Cuba was redrawn once for traditional tacked bongo heads. All chosen images were processed with art.py --rekey and inspected at saved size. Prompts, provenance and redraw counts are in art/prompts.json; selected raw sources are in art/raw/.

## Art still to paint
None. No people assets were requested or generated.

## Engine changes wanted
Keep the shared kit unchanged in this build. handoff.md specifies the proposed kit/instruments.js extraction and future rhythm-clock integration, including exact functions, cents input and source cancellation. The working adapter remains local to src.html.

## Left open
- A cold sonic and cultural review remains next. Browser synthesis intentionally demonstrates rules rather than reproducing recordings. Narration uses the browser fallback; no audio was recorded.
- Compact cards put some pitch diagrams or the optional real-music link inside their own scrolling area. All primary playback controls and all mystery answers remain visible.
- The full audit predates the final repairs; only affected checks were repeated. Its raw 101-lead report is preserved rather than presented as clean.
- The optional siku-photo question is resolved toward the specified painting. No image was fetched.

All Chrome instances and servers started by this build were closed. Ports 9980, 9981 and 8785 were confirmed closed. host.html is absent. No work remains before the build-only handoff.
