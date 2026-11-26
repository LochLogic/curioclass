# Family Dance Night: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: family-dance-night

#### Built

Built November 2, 2026 in S:/CurioClass-codex. Build only, no commit or polish round.
Writes were confined to tools/family-dance-night and _scratch/family-dance-night, apart from the image tool's managed originals.
The offline bundle is family-dance-night.html, 1,002,464 bytes, about 979 KB.

Seven painted object tables open Watch, Copy, Words and Where from. Each dance has its specified two moves, original synthesized music, geographic home and short community text. Favorite part preserves the class choice for this page visit. First returns light seven ceiling strings and the complete room brightens.

The kit supplies the figures, floor projection, pose library, mirrored phrases, clock, music tracks, count strip, icons, voice queue and access controls. Tool code supplies costumes, moving painted props, additional timbres and the room. The owner-requested temporary figure renderer is isolated for painted replacements.

Required source, draft metadata, teacher notes, voice manifest, audit states, handoff, art manifest and finished art are present. world.json is loaded and inlined. No shared file, spec or neighboring tool was edited. Both bar tools were bundled into Scratch and opened in muted Chrome.

#### Numbers check

Scratch setup.py and numbers.json independently recompute the specification's arithmetic.

- Sixteen counts: 100 bpm = 9.6 seconds; 132 = 7.273; 112 = 8.571; 96 = 10.0; 60 = 16.0.
- Slow is 60 percent tempo; the longest sixteen-count loop is 26.667 seconds. Copy is eight counts at that slower tempo.
- The explicit move lists contain 41 word-move pairs, not the stated 38. Every supplied per-word total is correct and those totals sum to 41. The explicit lists were retained.
- Contrast: white/brand 10.02:1; brand/paper 9.31:1; ink/paper 15.28:1; muted/paper 6.25:1.
- All seven map coordinates are the supplied values, projected onto the locally bundled Natural Earth land outline.

#### Feel check

Walked the teacher-driven K-2 sequence across the seven dances: watch, copy, describe, connect, choose a favorite and return. This was a desktop student-path check, not a classroom trial.

Best moment: the broad painted fans meet over the dancer's head, followed by returning to the room with all seven strings lit. The class's favorite remains visible as a heart badge rather than a score.

Two flattest early moments and fixes:

- The fan wave began with folded fans, weakening its sweeping shape. It now begins open and folds only at the phrase transition. Ceiling strings were moved behind the dancers so raised fans remain visible.
- The lion cloth floated above disconnected-looking legs. It now drapes over the two figures in two connected segments. The skirt sweep also follows the figure's hands, with its ruffles clipped to the cloth.

The preview initially crowded Copy controls and the lowest table buttons. Side-by-side compact move choices, tighter panel spacing and raised table positions fixed those problems. Phone visual order now puts the floor above its controls.

Compared the final fan frame beside Snowy Mail Route in _scratch/family-dance-night/bar-comparison.jpg. The painted room, large props, warm light and clear controls meet the scene-rich bar. The kit figures remain visibly temporary, as the owner directed. Beat Lab was also opened as the interaction bar.

#### Done when

1. PASS. At 1366x768 and 680x425, the central figures are the largest dance subjects. All seven home buttons are visible and at least 60 pixels tall. Fan/umbrella figures reserve extra space above their props.
2. PASS for this temporary-figure build. Seven full Watch loops and all fourteen Copy runs completed without console errors. Copy uses Dance.mirror and facing zero; turn motion is in pose yaw. Both pose contact sheets were inspected. Every Copy run stopped after eight counts.
3. PASS. All 252 combinations of seven dances, twelve chips and Move 1/Move 2/both matched the specification's explicit lists. words-content.json records zero mismatches.
4. PASS. Lifecycle checks confirm every old clock is stopped by replacement moves, tabs and Back. Slow changes 100 to 60 bpm on the next count. Read during the fan count-in waited until all four counts finished. Word feedback waits for the next count when music runs.
5. PASS. First visits increment once, revisits retain their check mark, and the seven-table frame shows 7 of 7 with all strings and the brighter room. The final event is queued by that first seven-table completion.
6. PASS. All seven actual origin cards, text and projected pin coordinates were extracted and checked. Where from is an event line and started five times in the held-click repetition test.
7. PASS. At a two-second held-tap pace, words, origin cards, Copy move calls and table names each started five times. Relevant how-to lines started once. The 63-line manifest exactly matches runtime allLines. Read speaks the current visible hint or origin card.
8. PASS. Controls are at least 60 pixels, with words and icons or figure icons. All specified sizes were captured, including the true 375-pixel iframe. Play and tabs are visible in Watch; active choices remain visible in other views. Audit focus and keyboard paths are clean.
9. PASS. Calm mode held an identical pose while clock position advanced from 0.219 to 0.420. Props quantize by count, lights have no calm pulse, timing is unchanged, and the audit found no infinite animation.
10. PASS for offline behavior and transient dance work. FAIL for a literal reading of nothing saved: the required shared kit remembers only curio-motion. Visits and votes are never stored. No art/data tokens or automatic external resource URLs remain in the bundle, and no fetch, XHR or WebSocket is used by the tool.

#### Wave lessons

- PASS, hint and voice: visible hints change synchronously, Read uses the current view, stale run speech is hushed, and how-to lines use the shared heard logic.
- PASS, focus and layout: permanent controls retain identity, deliberate focus uses preventScroll, nothing takes focus on load, and hints reserve space.
- PASS, sizes: all eight STANDARDS layouts were captured and inspected, including 680x425 and the 375 iframe; K-2 targets stay 60 pixels.
- PASS, no giveaways: this is observation and preference, not a scored hidden-answer puzzle. The chips support discussion rather than awarding points.
- PASS, honest numbers: count lengths, tempo scaling, light counts and contrast were recomputed; there is no unexplained estimate meter.
- PASS, standards: the child describes a displayed move, makes and explains a favorite choice, and opens community/place cards. Shared-family registration is requested in handoff because docs edits were forbidden.
- PASS, Motion off: count timing continues, figure/prop motion quantizes and light pulses stop. All paintings are present; temporary kit figures are explicit.
- PASS, short choices: all seven tables, twelve word chips and four favorites stay in view in their relevant states.
- PASS, resize mid-animation: the full audit resized every reached state and walk action without exceptions or stuck controls.
- PASS, first-tap welcome: a table's own name takes precedence; the obsolete gym welcome is skipped unmarked, not played late.
- PASS, unknown as unknown: no hidden condition is falsely displayed as known; map cards show only the supplied geographic information.
- PASS, one look/one meaning: gold plus a check marks a visited table; selected words/favorites use pressed state; the lamp count is separate from preference.
- PASS, truthful badges: the counter tracks unique returns and each heart badge names the actual chosen favorite.
- PASS, hints change back: returning to the gym updates the visible home hint and Read immediately; stopping Watch restores Play guidance.
- PASS, no answer by copied clues: there is no diagnostic quiz. Dance-word labels intentionally support describing observed movement, as the spec directs.

#### Audit leads

The single full audit exited zero after 693.5 seconds, within its forty-minute limit. It produced 57 PNGs, all inspected, and 16 leads. Full dispositions are in _scratch/family-dance-night/audit-responses.md.

- Nine hidden-hint leads: eight home sizes plus the returned-home state inspect the hidden panel #hint. The visible #home-hint owns gym guidance and Read through the custom voice read function. The audit's own Read row confirms the visible home instruction is spoken. No missing student guidance.
- Seven skipped-welcome leads: each table tap speaks its own name and Play guidance. STANDARDS explicitly says to skip the first welcome after a tap's own line, unmarked. Playing it later would be stale. No change.
- All six reached states, Motion off, mid-action resizing, held-click focus/keyboard, five-click repetitions, quick double taps and console checks were otherwise clean.

The final layer-only change moved ceiling strings behind the figures. Focused phone fan/umbrella views and a laptop fan frame were rechecked with zero console errors. The full audit was not rerun for that rendering-order change.

The first phone host run had a favicon 404 from the test host, not the offline tool. The final host runs include a temporary inline favicon and have zero errors. The host file was removed afterward.

#### Frames looked at

All 64 main-check PNGs, 57 audit PNGs, three early PNGs, five compact-fix PNGs and two bar PNGs were inspected directly or in contact sheets. Scratch retains the original PNGs and shot lists.

- frames/watch-0 through watch-6; copy-0-0 through copy-6-1; pose-contact-A and pose-contact-B.
- frames/home-* and dance-* at every desktop STANDARDS size; phone-home, phone-watch, phone-copy, phone-words, phone-from, phone-favorite and phone-fan-flower.
- Grayscale Words, calm frames, keyboard-run-final, count-in-read, lifecycle, all origins, seven-lights, compact Words/Favorite, skirt-final and fan-final-laptop.
- audit/size-*, state-*, calm-*; audit-sheets/sheet-1 through sheet-7; art-contact.jpg and final bar-comparison.jpg.

#### Art made

Fourteen images, generated with the built-in image tool, copied from managed originals into art/raw and processed only with scripts/art.py --rekey. Total finished art: 613,532 bytes, about 599 KB. Bundle: about 979 KB. No raster redraw was needed after inspection.

One empty gym, seven family-object tables, two lion heads, one lion cloth, two fans and one umbrella. All are used. None contains people. Full prompts, house style, people flags, source and reviewed status are in art/prompts.json. SVG supplies precise moving costumes, props, lights, counts and map placement.

#### Art still to paint

Fourteen deferred people assets, one per move, are listed with people true and explicit art tokens. They request the alternating support, low/high, bow/blink, raised/lowered skirt and fan, and turning phases needed by the next painter. Keep the kit models for timing and pose logic; replace only the isolated figure renderer. Final painted dancers require the owner's review.

#### Engine changes wanted

No shared engine was edited. Handoff gives the exact dance.md registration row and count update for the integrator. An optional in-memory Motion preference in kit/curio.js would resolve the literal no-storage conflict without replacing the kit control.

#### Left open

- Final painted dancers, explicitly deferred by the owner.
- Fresh cultural-content review of all seven dances and simplifications before release, per BASELINE rule 5. No outside-reviewer gate was invented.
- Listening review of the original synthesized ensembles and browser speech. Automated muted Chrome checks verify timing and line starts, not sound quality or cultural authenticity.
- No recorded narration was made, as the build instructions require. clear-teacher / Iapetus is the future recording voice; this build uses browser fallback.
- The shared Motion preference is the only persistent setting. The family-doc registration is deferred because writing docs was prohibited.

All Chrome and server listeners started for this run are closed. host.html is absent. Source is readable at 899 lines, maximum 149 characters. The report was written last to honor the user's stop-on-report instruction.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: family-dance-night

#### Played
Cold play as a K-2 solo learner and a teacher using a 1366x768 projector: all seven tables, all four tabs, both moves, Slow, count-in, words, favorites and returns. Played before reading codex-report.md, handoff.md, notes.md or src.html. The room was inviting; the code figures weakened the dance itself. This was simulated classroom use, not a classroom trial.

#### Findings fixed
- **Blocker, family:dance, src.html / Words:** opening Words or stopping Watch early affirmed words from an unseen second move. Reproduced with Slow and Big on the lion. Initial context is now Move 1; an interrupted Watch uses the displayed move; both moves count only after a complete loop. Copy resets the context.
- **Should fix, general, keyboard:** Space on a focused word started hidden Watch playback and replaced its hint. Native controls now retain Space activation; background play/stop is limited to Watch and Copy.
- **Should fix, general, Favorite / Read:** after Where from, Read spoke the hidden origin instead of the visible favorite prompt. The overlay now takes precedence.
- **Should fix, general, voice:** the first Watch instruction could be dropped behind the table name at a 2-second pace; Where from lacked a spoken next action; Copy completion named hidden word chips. Short how-to lines now precede longer events, and Copy completion explicitly names Words. Sound recovery queues only the unheard instruction that still matches the visible hint.
- **Should fix, family:dance, graphics:** temporary figures, floating lion costume and tiny code icons undersold the moves. Installed seven painted characters, two key poses per move, and matching painted move icons. The lion is one costume with four human legs. PAINTED and two renderer functions isolate replacement from the timing engine.
- **Should fix, general, cultural wording:** qualified southern lion dance, distinguished solo Irish step dance from ceili, gave the fan dance a stage setting, and restored Black New Orleans community credit to second line. Added claim-specific sources and contextual limits to notes.
- **Should fix, general, teaching depth:** adjective naming alone was thin for grade 1-2 interpretation. The existing favorite reflection now asks for dance words explaining what the moves show; notes distinguish kindergarten description from grade 1-2 interpretation and context.
- **Polish, Favorite:** the flattest payoff was a generic why prompt over an unrelated frozen pose. Selecting a move now shows its painted pose, restores its pressed choice on revisiting, and names the class's actual favorite on the floor.
- **Art QA:** four first sheets missed the painted house style and were redrawn. Equal-quadrant cropping clipped hands and umbrellas; corrected crops follow complete connected subjects. Final contact sheets were inspected.

#### Findings left
- **Should fix, validation:** the final audit failed before its first screenshot. This review does not clear 680x425, 800x500, 1000x625, 1280x720, 1920x1080, 760 wide or the 375-wide iframe. Recheck them in the next workflow. No all-size PASS is claimed.
- No known reproduced product blocker remains. The validation gap above prevents release clearance from this report alone.

#### Break it
- **Word feedback, skip Watch:** tap table, Words, Slow/Big. Before: both received Yes without the second move. After: both receive look-again feedback for Move 1.
- **Word feedback, short Watch:** start and stop before Move 2, then choose Slow. Before: Yes. After: look again. A complete Watch loop still enables both moves, as specified.
- **All word contexts:** independently transcribed lists, 7 dances x 12 words x 3 contexts = 252 checks, zero mismatches after fixes. Sweeping chips reveals their fit labels, but gives no score, mastery badge or completion credit. This remains the spec's observation/discussion tool, not an assessment.
- **Hidden-control shortcut:** Space while Sharp has focus now activates that chip and leaves playback stopped; before it started Watch from Words.
- **Reflection / Read:** Where from -> Favorite -> Read now reads the visible vote prompt. Choosing Move 1, Move 2 or music records that preference without claiming a correct reason. Five repeated music selections produced five reflection starts in the side run.
- **Lights:** rapidly enter and leave all seven tables, then revisit one. Counter is exactly 7 of 7; the revisit adds nothing. This deliberately measures visits, not dance skill. Notes now say so.
- **Counts and tempo:** count-in and replacement moves were exercised; they are timing aids with no timing score or saved best. Seven full Watch-loop frames show the expected end-of-loop Copy guidance.
- Evidence: _scratch/family-dance-night/break-before/, recheck/, *-before.json, *-after.json, word-matrix.json and painted-checks/.

#### Voice walk
Final default path used actual CDP held presses of 120 ms and 2-second action gaps, with time to watch the loop, finish Copy and hear the origin. Plain floor tap -> welcome -> table -> Play -> Copy -> Move 1 -> Words -> High -> Where from -> Favorite -> Move 1 -> Read -> Back.

Actual starts, in order: welcome; Tap Play; table name; Tap Copy; choose a move; Lion wakes up; Tap Words; choose a dance word; Yes, high; Tap Read; lion origin; vote instruction; interpretation reflection; Read of that reflection; lights event.

All mode how-to lines started once and matched their screens. Side run: word-answer events 5/5 and favorite events 5/5, with no repeated how-to; that side log predates the final reflection wording. The final main path rechecked the new wording. Fresh-page Sound off -> table -> Copy -> Sound on spoke the previously unheard Copy instruction. Read also worked with Sound off. Source and manifest match all 64 fixed lines.

Muted Chrome verifies starts and timing, not acoustic quality. Browser speech is the current narrator; no recorded Iapetus voice is claimed. A supplemental seven-loop timing request hit the driver's internal 60-second cap; its smaller main-path retry completed.

#### Facts checked
- **Southern lion:** Guangdong style, festive good-luck wishes and two performers in one costume: [Singapore Chinese Cultural Centre](https://culturepaedia.singaporeccc.org.sg/social-practices/southern-lion-dance/) and [National Museums Scotland teacher notes](https://files.nms.ac.uk/production/Legacy/Images/National%20and%20International/ea-traditions-and-celebrations-teachersnotes-hlf.pdf?dm=1712512715). Wording now concerns this southern style.
- **Jarabe Tapatio:** Jalisco and festive performance: [Tamaulipas Secretariat of Education](https://comunidaddelsaber.tamaulipas.gob.mx/contenido_mimurales/14). [Los Rancheros' own performance gallery](https://losrancheros.org/es/video/) names its Jarabe Tapatio performances. The skirt study is not presented as the complete partner dance.
- **Irish step:** still arms, active feet, performance/competition, and distinction from team dancing: [IDTANA](https://idtana.org/types-of-irish-dancing/). Older relaxed step style: [ITMA's Tubridy collection](https://www.itma.ie/playlists/tubridy-dance/). Removed the ceili conflation.
- **Bhangra:** Punjab, harvest celebrations, weddings/parties, hops and shoulder shrugs: [BBC School Radio, programme 3](https://downloads.bbc.co.uk/schoolradio/pdfs/danceworkshop_autumn_2009.pdf). Notes distinguish that introduction from changing staged and diaspora forms.
- **Buchaechum:** Korean stage dance, hanbok, fans, flowers and waves: [Korea.net / National Gugak Center workshop](https://www.korea.net/Events/Overseas/view?articleId=26726). Kim Baek-bong and 1954 in notes: [Korea.net learning account](https://www.korea.net/NewsFocus/HonoraryReporters/view?articleId=202577). Group formations are distinguished from this single-dancer study.
- **Second line:** Black New Orleans communities, societies, brass bands and following dancers: [National Park Service, Jazz Origins](https://www.nps.gov/jazz/learn/historyculture/history_early.htm). Community credit is now on the origin card.
- **Kpanlogo:** Ga / Greater Accra, communal drumming, arm swings, torso and footwork: indexed p. 40 of [Ghana NaCCA's curriculum](https://nacca.gov.gh/wp-content/uploads/2024/10/Physical-Education-and-Health-Core.pdf). 1960s context: [University of Ghana Dance Ensemble brochure](https://ias.ug.edu.gh/sites/ias/files/styles/thumbnail/GDE-Brochure_reduced.pdf).
- **Standards:** description, interpretation, preference with reasons and cultural connection held against [NCAS Dance at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance.pdf). The added reflection deepens the existing activity; oral reasoning is not automatically assessed.
- **Numbers:** independently recomputed 16-count durations: 9.6, 7.273, 8.571, 10 and 16 seconds at 100, 132, 112, 96 and 60 bpm. Slow at 60 percent gives a longest loop of 26.667 seconds. Contrast ratios are 10.02, 9.31, 15.28 and 6.25. Explicit word lists total 41 pairs, not the spec's 38. See review-numbers.json.
- **Maps and music:** place labels match the cultural sources above. Numeric anchors remain the spec's GeoNames values; live coordinate refresh was unavailable. Music is labeled original synthesis, not a traditional recording or verified authentic rendition.

#### Sensitivity
All seven dances concern living cultures. The people sheets show different ages, skin tones and body shapes without presenting one figure as a whole community. Every new person asset is marked people true.

A fresh sensitivity reviewer should examine example clothing, simplified lion wake/bow, zapateado versus skirt study, solo Irish versus ceili, Punjabi harvest versus modern forms, buchaechum's creator and group geometry, Black New Orleans credit, and Ga-specific movements/drums. The Cervantino source contains conflicting 1945/1954 wording; notes use the corroborated Korea.net 1954 account. The two-pose turns are introductory movement studies, not documentary choreography. Music still needs a listening review.

Owner/sensitivity contact sheets: _scratch/family-dance-night/review-people-1.png through review-people-3.png. No outside-contact approval gate was added.

#### Flattest moment left
An unsuitable word still gets only the spec's short look-again response. It does not explain a misconception automatically. The class or solo learner must point to the movement and discuss it; adding a scored quiz would change the brief.

#### Graphics
Retained the warm gym, seven object tables, maroon controls, count display and growing lights. Inspected all fourteen original paintings and all 28 finished people poses. Painted icons now match the stage. The strongest new moment is the complete lion rising, rather than a painted head over elongated code legs.

The cast has two key poses per move, with a local renderer/geometry table for swapping figures. Complete subjects were recropped before scripts/art.py --rekey. Four off-style sheets were redrawn. Art: 1,581,114 bytes; offline bundle: 2,293,859 bytes (2.19 MiB). Kept teaching art above the 2 MB goal; below the 6 MB notes threshold. No missing art token remains.

#### Audit
**Audit not finished.** The single 2400-second-limited invocation used Chrome 9961, host 8765 and the dedicated review profile. It exited with TimeoutError in CDP domain enabling before the first screenshot. It produced no audit.md, PNGs or actionable leads. It was not rerun, following CODEX-REVIEW's audit-once stop rule.

Failure record: _scratch/family-dance-night/review-audit/run-failure.md. Targeted 1366x768 runs reported zero console errors; grayscale and Motion off were inspected. The calm painted pose stayed identical while its clock advanced. Those checks do not replace the missing responsive audit.

#### Left open
- Seven other STANDARDS sizes, resize stress and the full mechanical walk need verification in the next workflow. Do not infer a pass from the builder's older audit.
- Recorded clear-teacher narration and an acoustic/cultural listening review remain future work; the build rules prohibited making recordings here.
- Exact GeoNames coordinate refresh and the temporarily unavailable Edomex lesson page were not independently cleared live. Notes retain their provenance and other verified sources.
- The spec's 38-pair total should become 41; spec/shared-family edits were outside the write boundary. Shared Motion remembers its setting locally; dance visits and votes are transient.
- Unattended choices: followed the owner's painted-cast decision over the older code-figure art plan; used two key poses per move; retained browser narration and the observation format. No new mode, score, upload or outreach.
- The initial location/brief read completed in 0.2 seconds without an explicit timeout wrapper. Subsequent shell commands were bounded. No git commit or shared-file change was made.
- Chrome 9960/9961 and host 8765 had no responding listener at closeout. No host.html remains in the tool folder. Evidence map: _scratch/family-dance-night/README-REVIEW.md.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Family Dance Night build handoff

Built November 2, 2026 in S:/CurioClass-codex. Build only. No commit, branch change or polish round.
Only tools/family-dance-night and _scratch/family-dance-night were written.

#### Structure

src.html starts from kit/starter/src.html and loads kit:curio plus kit:dance. Permanent panel controls precede the stage in the DOM. Tool code holds seven source-content records, fourteen move keyframe sets, the voice table, figure decorations, responsive room, run lifecycle, original ensemble timbres, map and favorite handlers. world.json is the existing local Natural Earth land outline reused without country borders, rendered in Equal Earth projection. The data is bundled inline.

Each new run, tab switch, favorite panel or return stops the old play, clock, music and speech. runId invalidates delayed speech cleanup. Copy uses Dance.mirror with model facing zero; turning moves rotate the pose's yaw inside that class-facing model. The count-in starts the sequencer only at dance count one, avoiding the engine's negative-position loop wrap. Read waits until the first dance count if a count-in is active, then stops the run and reads. Slow uses the engine's next-count tempo change.

Word chips use the last shown move or both moves for a full Watch loop. While music is running, answers wait until the next count. Music is lowered about 6 dB during narration by reattaching the same kit track at half volume; tool timbres use their output gain. A speech generation counter prevents an older completion from raising volume under a newer line. Sound off leaves the clock intact. Motion off samples props and figures once per count and removes light pulses.

Table lights and favorite choices live only in memory. Shared kit Motion remembers its preference. All seven first returns brighten the room and play the final event line. No class data is stored or transmitted.

#### Painted-dancer adapter installed in the cold review

createFigureRenderer and decorateFigure hide the Dance.dancer model and draw a complete painted person (one paired costume for the lion). PAINTED is the sole asset/geometry table. It has two key poses per move, 28 individually cropped WebPs across seven consistent characters. The owner-requested people flags, prompts, source and review status are in art/prompts.json. Original pose sheets and the people contact sheet are in _scratch/family-dance-night; raw subject crops stay in art/raw.

Dance still owns the clock, travel, count-in, pose model and mirrored Copy convention. The adapter swaps whole painted poses on counts; Motion on adds a small rhythmic root bounce, and Motion off quantizes that too. Geometry is normalized to the tallest pose per character so the lion bow and low positions do not grow to match the standing pose. A replacement set only needs updated PAINTED sources/normalized widths/heights and corresponding art assets. No shared engine change is required.

The move buttons now use the same painted poses as the stage. The table paintings and warm gym remain. The old lion-head/body, fan and umbrella files are retained as source art, but complete painted figures now carry their own props. Final review must not infer exact traditional choreography from a two-pose movement study. The 2 MB figure is a goal; preserve teaching art.

#### Open questions and specification decisions

- Cultural review: take the spec's implied recommendation for a review of all seven dances, props, descriptions and movement simplifications. BASELINE rule 5 resolves the mechanism: a fresh review agent before release, without waiting for outside reviewers. This Build run is not that cold cultural review. No extra agent was spawned.
- Painted dancers: the owner's explicit decision supersedes the old spec art plan. Painted dancers are now installed, with people true on every pose. Owner contact-sheet review remains part of release.
- The specification asks the builder to add this tool to docs/families/dance.md. The write boundary forbids editing docs, so the exact registration request is below.
- The explicit move word lists contain 41 pairs, not the stated 38. All per-word totals in the spec sum to 41 and were retained. Loop durations, 60 percent Slow and the four contrast ratios recompute correctly. Scratch numbers.json has the calculations.
- No recordings were made, as CODEX-BUILD.md directs. All fixed lines are in voice/lines.json using bank clear-teacher / Iapetus and browser-speech fallback. The bank voice is the intended future recording voice, not a claim that the browser can select Iapetus.
- The user's stop-on-report instruction takes precedence over the brief's early-report advice. codex-report.md is written last; intermediate evidence stays in Scratch.
- The bar tools were bundled into Scratch, avoiding writes to their tool folders, and opened in muted Chrome. Their sources and existing art were read only.

#### Engine changes wanted

- docs/families/dance.md, What each tool brings table: add family-dance-night, K-2, square floor; seven dances and two lion figures; fourteen mirrored pose phrases; clock, music, counts and icon; family tables, dance words, origins and room lights. Also update the four-tool count. No shared engine change is needed for this build.
- kit/curio.js, init Motion handler: an optional in-memory preference would allow a literal no-storage tool to avoid curio-motion while keeping the shared Motion button. No kit edit was made.

#### Validation and next step

The final report records the bounded test batches, frames inspected and the single mechanical audit's disposition. Scratch contains commands, shot lists, logs, numeric checks, pose sheets and audit output. Browser runs use Chrome ports 9970 to 9977 only; iframe hosting uses 8775. Every browser and server started by the build is closed after its batch.

The painted dancer set is installed. The next workflow is a fresh sensitivity review of the painted simplifications and a listening review of the synthesized ensembles. Do not infer cultural authenticity from a passing mechanical check. The renderer boundary and PAINTED table keep future figure replacement local to this tool.

The single audit completed in 693.5 seconds with exit zero and 16 leads. Nine concern the intentionally hidden panel #hint while the gym's visible #home-hint owns Read. Seven concern the intentionally skipped gym welcome when the first table tap speaks its own name, as STANDARDS requires. All states, resizing, focus, calm animation, repeated clicks and console checks were clean. Manual held-click logs additionally cover the interior controls.

After the audit, the ceiling light layer moved behind the dancers so raised fans and umbrellas remain visible on a phone. The focused phone prop frames and a laptop fan frame were rechecked; the full audit was not rerun for this layer-only change. relayout reserves more space above fan and umbrella figures by using a 0.45 height fraction; other figures use 0.53. Keep that prop clearance when installing the paintings.


#### Cold-review functional repairs

- Initial Words context is Move 1, not both moves. Watch tracks the displayed move and allows both only after one completed loop. A single Copy move resets that context. This closes the unseen-move affirmation path without adding scores or gates.
- Space retains native activation on focused controls; the background play/stop shortcut is limited to Watch and Copy. It cannot start hidden Watch controls from Words, Where from or Favorite part.
- Read checks the Favorite overlay before the underlying origin tab. Concise mode how-to lines start before longer event descriptions. Visible hints change synchronously.
- Favorite move selection now shows that painted move, preserves the selected card on revisiting, and names the class's choice on the floor. The why prompt asks for dance words and an interpretation of what the moves show; it works aloud alone or with a partner. Grade-specific prompts in notes.md distinguish naming from interpreting.
- Source wording now distinguishes southern lion dance, solo Irish step dance, the staged Korean fan dance, and the Black community origins of second line. See notes.md for claim-specific links.

#### Sensitivity

All seven dances represent living cultures. Review the new people contact sheet for respectful anatomy, clothing, ages and body representation; the single cast member is not a representative of everyone in that community. Check the simplified lion rise/bow, zapateado versus skirt study, Irish solo versus ceili distinction, Punjabi harvest summary versus modern forms, buchaechum's named creator and group formations, Black New Orleans origin credit, and Ga-specific Kpanlogo movements and drums. The synthesized ensembles need a listening review and must remain labeled original sketches. No outside-contact gate is added.

Cold-review evidence and final audit will be recorded in codex-review.md. The earlier build audit above is historical and does not certify the painted revision. The review uses Chrome 9960 to 9967 and host 8765, with no shared-file edits or commits.


#### Cold-review audit result

The single final review audit did not finish. It failed before the first screenshot while enabling a Chrome CDP domain, at the driver's internal 60-second request timeout. There is no generated audit.md or saved lead list. The 2400-second outer limit was in place. It was not rerun, as CODEX-REVIEW.md requires one audit, last, followed by reporting and stopping on failure.

Current targeted evidence covers 1366x768, all seven Watch loops, 28 pose cutouts, 252 word/context checks, the confirmed keyboard and Read cheats, the final main-path voice log, reduced motion and grayscale. It does not certify the seven other STANDARDS sizes. Recheck those in the next workflow before release. See _scratch/family-dance-night/review-audit/run-failure.md and final-static.json. Chrome 9960 and 9961 and host 8765 had no responding listener at closeout; no tool host.html exists.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
