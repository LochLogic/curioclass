# Codex review: which-way-is-down

## Played

Cold Grade 5 solo play, before the builder's report, handoff, notes or source: four records, reveal, argument, prediction miss and Other worlds. Then a teacher/projector voice walk and focused repair checks. The schoolyards and the converging-arrow reveal are strong; retained their detail and character.

## Findings fixed

- **blocker, general, Argue voice:** three hits announced a strong argument with zero reasoning words. Confirmed in `review-probe/hit-no-reason-2.json`. Speech now obeys the reasoning gate, completing reasoning afterward can announce the newly earned result, and removing words reverses the hint/status and interrupts a stale Strong announcement.
- **should fix, general, Argue entry:** four available records still produced "Record at least three places" because attached cards were counted. Entry now checks available records and names the usable next action. Unavailable-card prompts speak once per Argue entry, not on every tap; the discussion prompt no longer assumes a pupil made a miss.
- **should fix, general, voice:** Zoom out skipped the Globe how-to; long confirmations lost navigation cues at a two-second pace. Shortened the first landing and Record confirmation, synchronized Zoom before its visibility check, and queued the Globe cue after the reveal.
- **should fix, general, predictions:** results named Next place while it was disabled. Result and next-action speech are now separate; Next is named only once enabled. Predict also preserves a useful keyboard focus path. Obsolete claim/evidence headings hide during predictions.
- **should fix, general, keyboard/access:** Go to Drop hid the focused control; it now focuses Drop with preventScroll. Passive pictures use image semantics and leave the tab order; interactive globe/arrow views keep their keyboard surface.
- **should fix, general, vacuum demonstration:** the sealed tube fell with its contents fixed inside. Its shell now stays still while the painted feather and apple fall together inside it.
- **should fix, general, narrow Argue:** six evidence choices pushed the hint below the phone frame. Compact claims and a three-column evidence grid keep every choice, Check/Test and the complete hint visible at 375x812 and 680x425.
- **should fix, general, phone yard:** the school badge covered the child's face. It now occupies clear upper-right sky. The white ruler also gained a dark backing so Antarctic snow cannot hide it. Landed-state bubbles were moved into clear margins after the audit frame exposed a face overlap at 1000x625; rechecked at 1000, 680 and 375 widths.
- **should fix, general, Motion off/reveal:** canvas arrows still grew in calm mode despite the default CSS audit being clean. They now hold still through each 800 ms beat and extend at its end. Rendered pixels remain identical during an active calm reveal.
- **polish, general, Other worlds:** lifted the flattest scene with shaded lane frames, height ticks, contact shadows and brief landing rings; retained the painted surfaces, planets and timing.
- **polish, general, art/facts:** redrew the weakest cutout, the feather tube; qualified 6,371 km as this model's radius; added individually checked geography sources to notes. Updated voice, audit states and handoff.

## Findings left

- **nit, general, people art:** small backpack/hat/accessory continuity differences remain between a few holding and pointing poses; anatomy, weather clothing and the overall illustration style are sound.
- All blocker/should-fix findings identified in this pass are repaired. The narrow argument paper deliberately scrolls for reasoning/history; the main action choices remain visible. Audit coverage limitations and spec boundaries are explicit below.

## Break it

- **Record:** untouched arrows missed all four schools, by 28.8, 90.2, 123.9 and 153.4 degrees. Repeated Record cannot rotate an arrow. A miss supplies the specified teaching scaffold; recording is evidence collection, not independent proof. Real, whole-pixel handle drags hit.
- **Claim check:** tried every claim; only A fitted. Elimination unlocks testing but never earns Strong. Two place cards plus both speed cards left Check disabled. Only three actual place records satisfy the evidence gate.
- **Predictions:** tried unchanged arrows at all eight pool places on both alternating sides, repeated Predict taps and a center tap. All unchanged guesses missed; a center tap left 270 degrees; repeated taps spent exactly one attempt. Switching modes retained the unspent place and index.
- **Strong/reasoning:** three hits with zero words and punctuation stayed below Strong and no longer spoke Strong. Eight filler words can satisfy the explicit word-count gate only after the independent direction hits; scientific reasoning remains teacher-read, as the spec requires. A subsequent miss removed Strong. Native keyboard deletion of earned reasoning cleared both status and hint; deleting again during the award voice cut that obsolete announcement.
- **Reset/storage:** Clear erased records, reasoning and tests. Reloaded test rows remain historical; no saved score restores a streak. No extra award, best score or hidden percentage was added.
- **Timing:** restarted Drop all returned elapsed time to zero; Earth/Mars/Moon landed in that order. Slow-to-normal changed the integrated speed immediately. Motion off preserved the Earth landing time, measured at 574.9 ms, rather than skipping time.
- Proofs: `review-break-results.json`, `review-side-results.json`, `review-main-voice/`, all under `_scratch/which-way-is-down/`.

## Voice walk

Sound on, default settings, held 120 ms clicks at a two-second pace: Drop/Mark/Record at all four schools, Zoom out through the whole reveal, Argue/claim/three place cards/reasoning/Check/Test, three aimed predictions, then Other worlds/Drop all.
Actually started, in order: fellA, hMarkBtn, hMark, recOk, fellQ, recOk, hNext, fellS, recOk, fellE, recOk, hZoom, rv1, rv2, rv3, wGlobe, wArgue, hCheck, fits, hTest, hit, nextReady, hit, nextReady, hit, strong, nextReady, wWorlds, worlds.
The first Drop tap legitimately skips the Anchorage welcome under BASELINE 16; its instruction remains in the hint and Read. Actions can cut speech whose moment they leave. No stale instruction played over a different mode.

| Line(s) | Kind | Expected | Actually started |
|---|---|---|---|
| hMarkBtn, hMark, hNext, hZoom, wGlobe, wArgue, hCheck, hTest, wWorlds | how | once each on main path | once each |
| recOk, recMiss | event, five repeated submissions | five each | five each |
| hMark, hNext | how, repeat side path | once each | once each |
| hit, strong | event, three successful main tests | three, one | three, one |

Read interrupted speech, worked with Sound off and released promptly on a mode change. All 28 manifest lines match `allLines()`. The post-audit empty-record side path spoke once for five taps, then once more on re-entry. No recordings were made: the build brief forbids recording; these checks used browser fallback. Logs: `review-evidence-summary.json` and `review-side/`.

## Facts checked

- **Earth's down points toward the spherical center; support an argument with evidence:** [NGSS 5-PS2-1](https://www.nextgenscience.org/pe/5-ps2-1-motion-and-stability-forces-and-interactions). The student records, compares a claim and tests new directions; the standard is practiced, not merely named.
- **Plumb lines follow local gravity; real Earth departs from an ideal sphere:** [NOAA NGS vertical deflection](https://www.ngs.noaa.gov/GEOID/GSVS/deflection-vertical.shtml). Notes distinguish flattening, rotation and local deflections; the diagram is explicitly a model.
- **Mean radius 6,371 km:** [NASA Earth fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Changed the screen's exact "below every school" claim to "in this model".
- **Rounded gravity 9.8, 1.6, 3.7 meters per second each second:** [NASA planetary fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/), [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html), [JPL parameters](https://ssd.jpl.nasa.gov/planets/phys_par.html). Physics uses 9.81/1.62/3.71; Moon/Earth 0.165 and Mars/Earth 0.378 round to 0.17 and 0.38.
- **1.5 m drops:** independently recomputed sqrt(2h/g): 0.553001, 1.360828 and 0.899236 seconds, hence Earth 0.55, Moon 1.36, Mars 0.90. Constant gravity/no air resistance is stated; numeric proof is `review-numbers.json`.
- **Feather and heavier object fall together without air resistance:** [NASA Apollo 15 hammer-feather demonstration](https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_15_feather_drop.html). Repaired the picture so it demonstrates the intended result.
- **Esperanza has families and Escuela Provincial 38:** [Argentina government family arrival](https://www.argentina.gob.ar/node/460649); **63.4 S, approximately 57.0 W:** [official base description](https://www.argentina.gob.ar/node/82609). No claim of Antarctic territorial ownership or "only school" is made.
- **School-town locations/latitude notes:** [Anchorage](https://www.geonames.org/5879400/anchorage.html), [Quito](https://www.geonames.org/3652462/quito.html), [Sydney](https://www.geonames.org/2147714/sydney.html), plus the official Esperanza source above. Notes distinguish city/base points and fictional illustrated pupils from verified school-site surveys.
- **Test coordinates:** checked [Tokyo](https://www.geonames.org/1850147/tokyo.html), [Cairo](https://www.geonames.org/360630/cairo.html), [Oslo](https://www.geonames.org/3143244/oslo.html), [Honolulu](https://www.geonames.org/5856195/honolulu.html), [Nairobi](https://www.geonames.org/184745/nairobi.html), [Cape Town](https://www.geonames.org/3369157/cape-town.html), [Ushuaia](https://www.geonames.org/3833367/ushuaia.html), [Buenos Aires](https://www.geonames.org/3435910/buenos-aires.html). Cairo/Oslo reference points differ within about 0.1 degree from the spec; documented rather than falsely claiming identical rounding.
- **Direction calculations:** recomputed school arrows 298.8/179.8/33.9/116.6; South-Pole gaps 14.4/45.1/61.95/76.7; parallel-axis gaps 28.8/90.2/123.9/153.4. Sydney correctly displays 62.0. Integer hit windows contain 16 settings except Cairo's 17; no probability claim is shown to students.

## Sensitivity

The four fictional children and illustrated Alaska/Ecuador/Australia/Antarctica settings need the fresh sensitivity lens for representation and the small pose continuity differences. None is assigned an Indigenous identity from appearance. A child is an individual, not a stand-in for an entire population. Esperanza is named as an Argentine research base without a territorial claim. All eight people assets are marked `people: true`; no frightening, mocking or stereotyped depiction was found in this pass.

## Flattest moment left

After its first informative comparison, repeating Other worlds has limited depth. The new landing treatment improves that payoff; the four-location evidence sequence and the later unaided predictions remain the session's progression. No new topic or game was added.

## Graphics

Checked all 22 assets, every yard at final laptop size, the eight people poses, the space/ground/world art and the repaired tube in laptop, preview and phone scenes. One built-in OpenAI image redraw; final `art/wwd-feather-tube.webp`, exact prompt in `art/prompts.json`, source in `art/raw/wwd-feather-tube.png`, processed with `art.py --rekey`.
Other worlds and the globe retain the original painted texture and precise code geometry. Motion off stops new landing rings and existing bob/star motion. Grayscale retains named places, solid/dashed meanings, Hit/Miss text and measured gaps.
Compared with existing Snowy Mail Route and Beat Lab frames; retained this tool's richer painted field-trip identity. Art: 1,441,494 bytes; bundle: 2,077,358 bytes (about 2,028.7 KiB), below 2 MiB. Static checks and contrast: ink/paper 13.78:1, muted/paper 5.50:1, white/copper 5.71:1, gold/space 12.56:1, miss/space 7.80:1.

## Audit

Completed once within the 40-minute limit, Chrome 9941 and host 8745: 195 mechanical leads; all 237 printed lead/control rows classified in `review-audit-ledger.md` and `.json`. No unclassified row remains. Resize stress reported no exceptions or controls left disabled; repeat and quick-tap sections were clean.
Reviewed all 67 audit frames in 12 contact sheets and opened affected frames at native size. Intentional canvas/HTML layering, 23 px checkbox squares inside 44 px labels, secondary Start over folding, modal coverage and a Check cue made obsolete by the fixture were distinguished from real faults.
The audit could not discover its 375 px iframe context. Separate hosted 375x812 captures cover all four modes, all six evidence cards, the prediction view and affected yard states. This is a declared harness gap, not a claim that the audit checked phones. Multiple surviving HTTP listeners on the assigned port were identified during cleanup; an older served directory likely explains the missing iframe page.
The audit snapshot preceded the final bubble/focus/passive-surface fixes. Scoped post-audit captures also verify empty-card narration, prediction headings, reveal skip and calm pixel stability; no full audit or second full review was run. These confirmations, including the reasoning-removal reversal, had zero console errors. Chrome attachment failures were retried within bounds; successful paths are preserved.

## Left open

- Eight words are a length check, not a scientific-reasoning evaluator; teacher review is explicitly required by the spec. Filler alone cannot bypass the independent direction predictions.
- Recorded upbeat-guide narration remains for the separate recording workflow; no recording or shared engine change was made here.
- The existing globe uses longitude/latitude rotation without free roll. A new rotation interaction was not added in this one-pass repair.
- The spec names cities/base rather than four identifiable surveyed schools; notes state the illustration boundary. No identities or school names were invented.
- Unattended choices followed the spec/baseline. No commits, deployment, shared-file edits or outreach. Writes are confined to this tool and its Scratch folder. Chrome ports are closed and temporary host.html is removed. **Host cleanup remains blocked by Windows permissions:** six verified Python HTTP listeners on 8745, PIDs 6524, 44320, 44824, 47396, 49844 and 50820, returned Access denied on termination. No elevation or policy change was attempted. `review-host-cleanup.json` preserves the ownership proof and errors; these hosts need closing outside this permission profile before port reuse.
