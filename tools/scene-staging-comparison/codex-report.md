# Codex report: scene-staging-comparison
## Built
Watch, Compare and Layers are built in one offline HTML, using kit:curio.
Includes ten timed moments per production, silhouettes, synthesized cues, five live reactions,
two separate viewers, sample viewers, split ranking, six layers, saved reason chips and six evidence-backed opinions.
All four requested paintings are present. Build only, no commit, no polish round.
Final artifact is byte-identical to the checked Scratch candidate. All required files are present,
host.html is removed, and no test Chrome or server remains listening on ports 9980 to 9987 or 8785.
## Numbers check
Final caption word counts: 18, 15, 12, 12, 10, 9, 17, 14, 6, 15.
128 words / 2.5 plus ten seconds and pauses gives 77.7 seconds and 63.4 seconds.
The supplied counts reproduce 70.1 and 55.8 seconds; the extra 19 caption words explain the 7.6-second difference.
Full real plays measured 78.096 and 63.680 seconds, with all ten moments and boundaries checked.
Contrast: ink/background 15.64, ink/panel 14.19, muted/background 8.03, muted/panel 7.28, gold/background 10.93.
Set checks: duplicate reactions do not increase difference; disjoint sets can give 5; identical sets give 0.
Test-set top production / viewer split was moment 2, difference 3; earlier zero-score ties followed it correctly.
Theo's sample peaks at difference 2 at moments 4 and 9; the earlier-tie rule puts 4 first. Top three: 4, 9, 1.
Missing data from either viewer produces no viewer split; the final delivery check covers both missing-viewer orders.
Evidence: numbers.json, functional.json, full-play.json and content-check.json in Scratch.
## Feel check
Best moment: opening the meadow quarrel after Lost / Laughing stamps, comparing its pauses and blocking,
then turning a reaction into a saved opinion. The parlor and bare stage have visibly different weight and mood.
Flat moment 1: the farce faint initially clipped below the floor. Raised the fallen silhouette so the whole pratfall is visible.
Flat moment 2: close blocking made the two names merge. Replaced those labels with initials and a separate name legend.
Also kept inactive captions at full contrast and froze Layers positions immediately.
Played both whole productions; checked watching, reacting, switching viewers, comparing, inspecting and writing an opinion.
Viewed feel-comparison.jpg, placing the 1366x768 frame beside Beat Lab, plus the Snowy Mail Route bar frame.
The paintings give this its own finished visual character; silhouettes remain deliberately stylized.
## Done when
1. PASS: Watch emphasizes the active frame and five reaction buttons; Compare replaces the frames with enlarged strips.
   Looked at 1366x768 and 680x425 in Watch and Compare.
2. PASS: real 120 ms held taps stamp immediately; Next preserves play, Stop stops, and mid-play Viewer switching separates ownership.
3. PASS: both complete plays reached all ten moments; pauses and formula checked. Motion off keeps the 10.2-second opening moment
   and its 2-second pause with zero running animations. Poses, light and cue code follow the staging table.
   Targeted sound checks confirm no rain at the faint, cancellation of its rain tail, a delayed door slam and a complete blackout overlay.
   Acting is stylized; synthesized effects have not received a by-ear listening review.
4. PASS: independent symmetric-difference examples and tie order checked; no-stamp Show splits is disabled.
5. PASS: all 60 moment/layer combinations populated; both wardrobe images load; chips persist; unstamped opinions are refused.
6. PASS: both viewers' records and chips/opinions survived reload; real Cancel kept work and confirmed Reset cleared all.
7. PASS: five held taps at 2-second pace spoke how lines once and opinionAdded five times.
   No new spoken line during playback; bothDone was observed only after the second production completed.
## Wave lessons
- PASS, hint/voice: next actions named, hints update directly, Read stops playback and reads the hint; helper controls how-line repetition.
- PASS, focus/layout: persistent primary controls, reserved hint, prevented-scroll focus for mode evidence, step limits and Add.
- PASS, sizes: all eight required sizes inspected, including 375 in a host iframe; main Watch controls stay visible.
- PASS, no giveaways: reactions have no right answer, scores or success meter.
- PASS, honest numbers: playback formula documented, differences count types, unknown reactions remain empty.
- PASS, standards: live perception, viewer comparison, evidence-backed opinion and time-context cards teach all four listed standards.
- PASS, Motion off: no ongoing loops; same pauses and timing; all final art present.
- PASS, short choices: reaction buttons and layer tabs stay visible; all seven reason chips fit together at 680 and 375 pixels.
  Secondary Reset can require scrolling at 680x425; the comparison data table can scroll, as explained under Audit leads.
- PASS, resize: final audit found no exceptions or controls left disabled after repeated resizing during actions.
- PASS, first-tap welcome: stopped reaction taps speak it; Viewer 2's own how line takes priority; Play suppresses narration.
  Play from Layers enters Watch quietly. Reset does not speak a Play instruction over its confirmation dialog.
- PASS, unknowns: no stamp is shown as no stamp, not as neutral or agreement.
- PASS, one meaning: gold top / blue edge have text keys; reactions have both symbols and word labels.
- PASS, badge truth: viewer, production, moment, save status and play status follow actual state.
- PASS, changing hints: mode, moment and viewer changes update the current hint immediately.
- PASS, no copying: opinions require a personal stamp and an authored reason, with no correct wording to copy.
## Audit leads
The single final audit completed within its 40-minute limit: 27 leads. Motion off, repeated resizing,
five held taps and two rapid taps were clean. No JavaScript exceptions or controls stuck disabled were reported.
Every lead is individually answered in _scratch/scene-staging-comparison/audit-dispositions.md and its JSON companion.
- 9 compact Reset-scroll leads retained: Reset is a secondary confirmation control, not a response choice.
  The primary Play, stepping and reaction controls remain visible; the panel scrolls to Reset.
- 3 evidence-field-name leads fixed with an explicit aria-label; targeted check confirms it.
- 3 compact table-width leads fixed by reducing its label column to 58 pixels; horizontal overflow is now zero at 680 pixels.
- 2 phone table-scroll leads retained: ten moment columns keep 44-pixel targets. The phone now explicitly says to swipe for moments 1 to 10.
- 1 disabled-step hint lead fixed: only Next is named during play, except at moment 10, where Previous is named.
- 1 modal keep lead is expected background coverage. The fixture now keeps the dialog instead of demanding an uncovered background hint.
- 8 first-tap welcome leads: the 5 reaction cases are fixed. The 2 Play cases intentionally suppress narration;
  Viewer 2 intentionally speaks its own how line first, following STANDARDS.
Frame-led repairs also contain Layers columns, keep reason chips together, enlarge diagram labels, preserve the whole pratfall,
keep inactive captions readable and show the latest reaction word in the miniature strip.
Targeted repairs passed with no browser warnings, errors or exceptions. The full size sweep and audit were not repeated.
The first whole-play drive promise exceeded CDP's 60-second reply limit; one smaller external-polling retry passed both full plays.
A Scratch phone probe initially used the wrong host path; its corrected retry passed with real held taps and zero console errors.
## Frames looked at
All PNGs in bar-frames, early-frames, final-frames, focused-frames, content-frames,
phone-frames, phone-final-frames and full-play-frames were opened and inspected.
Also opened every PNG in repair-frames, phone-repair-frames, phone-repair-final-frames, small-repair-frames,
sound-tail-frames, layers-play-frames, audit-repair-frames, phone-delivery-frames and delivery-frames.
All 65 audit PNGs were inspected in audit-contacts/sheet-01.jpg through sheet-11.jpg.
Final sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe.
Also looked at grayscale, keyboard focus, Motion off, near/far blocking, faint, costume art, samples, first/last moment and Reset dialog.
## Art made
4 generated paintings, individually inspected at final size: two sets and two wardrobe displays.
Total WebP art 320,874 bytes, about 313 KB. Final bundle 514,101 bytes, about 502 KB, under 2 MB.
No redraws were needed. Raw originals, full house style, prompts and drawn_by provenance are retained.
## Art still to paint
None. No generated people, faces or body parts. Characters are faceless code silhouettes.
## Engine changes wanted
None. Shared engines, docs, scripts and other tool sources were not changed.
## Left open
- The full audit was not repeated after its targeted repairs. Its 27 baseline leads and all dispositions are preserved in Scratch.
- Reset is below the initial compact panel fold at 680x425. It remains accessible by scrolling the panel.
- Viewer-to-viewer ranking unions each viewer's two production sets before comparing. The spec does not define this aggregation;
  production-specific swaps can cancel in this ranking. The four displayed rows preserve the underlying evidence.
- Short landscape keeps two frames side by side for readability; tall widths under 900 stack them. Phones show one frame.
- Phone Compare scrolls horizontally; opinion and Layers details can need vertical scrolling. Secondary controls need compact scrolling.
- Embraces and kisses are suggestive poses rather than detailed physical acting.
- Browser narration and synthesized cue timbre need listening review. No recordings were made, as instructed.
