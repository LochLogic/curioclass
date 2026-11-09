# Codex review: family-dance-night

## Played
Cold play as a K-2 solo learner and a teacher using a 1366x768 projector: all seven tables, all four tabs, both moves, Slow, count-in, words, favorites and returns. Played before reading codex-report.md, handoff.md, notes.md or src.html. The room was inviting; the code figures weakened the dance itself. This was simulated classroom use, not a classroom trial.

## Findings fixed
- **Blocker, family:dance, src.html / Words:** opening Words or stopping Watch early affirmed words from an unseen second move. Reproduced with Slow and Big on the lion. Initial context is now Move 1; an interrupted Watch uses the displayed move; both moves count only after a complete loop. Copy resets the context.
- **Should fix, general, keyboard:** Space on a focused word started hidden Watch playback and replaced its hint. Native controls now retain Space activation; background play/stop is limited to Watch and Copy.
- **Should fix, general, Favorite / Read:** after Where from, Read spoke the hidden origin instead of the visible favorite prompt. The overlay now takes precedence.
- **Should fix, general, voice:** the first Watch instruction could be dropped behind the table name at a 2-second pace; Where from lacked a spoken next action; Copy completion named hidden word chips. Short how-to lines now precede longer events, and Copy completion explicitly names Words. Sound recovery queues only the unheard instruction that still matches the visible hint.
- **Should fix, family:dance, graphics:** temporary figures, floating lion costume and tiny code icons undersold the moves. Installed seven painted characters, two key poses per move, and matching painted move icons. The lion is one costume with four human legs. PAINTED and two renderer functions isolate replacement from the timing engine.
- **Should fix, general, cultural wording:** qualified southern lion dance, distinguished solo Irish step dance from ceili, gave the fan dance a stage setting, and restored Black New Orleans community credit to second line. Added claim-specific sources and contextual limits to notes.
- **Should fix, general, teaching depth:** adjective naming alone was thin for grade 1-2 interpretation. The existing favorite reflection now asks for dance words explaining what the moves show; notes distinguish kindergarten description from grade 1-2 interpretation and context.
- **Polish, Favorite:** the flattest payoff was a generic why prompt over an unrelated frozen pose. Selecting a move now shows its painted pose, restores its pressed choice on revisiting, and names the class's actual favorite on the floor.
- **Art QA:** four first sheets missed the painted house style and were redrawn. Equal-quadrant cropping clipped hands and umbrellas; corrected crops follow complete connected subjects. Final contact sheets were inspected.

## Findings left
- **Should fix, validation:** the final audit failed before its first screenshot. This review does not clear 680x425, 800x500, 1000x625, 1280x720, 1920x1080, 760 wide or the 375-wide iframe. Recheck them in the next workflow. No all-size PASS is claimed.
- No known reproduced product blocker remains. The validation gap above prevents release clearance from this report alone.

## Break it
- **Word feedback, skip Watch:** tap table, Words, Slow/Big. Before: both received Yes without the second move. After: both receive look-again feedback for Move 1.
- **Word feedback, short Watch:** start and stop before Move 2, then choose Slow. Before: Yes. After: look again. A complete Watch loop still enables both moves, as specified.
- **All word contexts:** independently transcribed lists, 7 dances x 12 words x 3 contexts = 252 checks, zero mismatches after fixes. Sweeping chips reveals their fit labels, but gives no score, mastery badge or completion credit. This remains the spec's observation/discussion tool, not an assessment.
- **Hidden-control shortcut:** Space while Sharp has focus now activates that chip and leaves playback stopped; before it started Watch from Words.
- **Reflection / Read:** Where from -> Favorite -> Read now reads the visible vote prompt. Choosing Move 1, Move 2 or music records that preference without claiming a correct reason. Five repeated music selections produced five reflection starts in the side run.
- **Lights:** rapidly enter and leave all seven tables, then revisit one. Counter is exactly 7 of 7; the revisit adds nothing. This deliberately measures visits, not dance skill. Notes now say so.
- **Counts and tempo:** count-in and replacement moves were exercised; they are timing aids with no timing score or saved best. Seven full Watch-loop frames show the expected end-of-loop Copy guidance.
- Evidence: _scratch/family-dance-night/break-before/, recheck/, *-before.json, *-after.json, word-matrix.json and painted-checks/.

## Voice walk
Final default path used actual CDP held presses of 120 ms and 2-second action gaps, with time to watch the loop, finish Copy and hear the origin. Plain floor tap -> welcome -> table -> Play -> Copy -> Move 1 -> Words -> High -> Where from -> Favorite -> Move 1 -> Read -> Back.

Actual starts, in order: welcome; Tap Play; table name; Tap Copy; choose a move; Lion wakes up; Tap Words; choose a dance word; Yes, high; Tap Read; lion origin; vote instruction; interpretation reflection; Read of that reflection; lights event.

All mode how-to lines started once and matched their screens. Side run: word-answer events 5/5 and favorite events 5/5, with no repeated how-to; that side log predates the final reflection wording. The final main path rechecked the new wording. Fresh-page Sound off -> table -> Copy -> Sound on spoke the previously unheard Copy instruction. Read also worked with Sound off. Source and manifest match all 64 fixed lines.

Muted Chrome verifies starts and timing, not acoustic quality. Browser speech is the current narrator; no recorded Iapetus voice is claimed. A supplemental seven-loop timing request hit the driver's internal 60-second cap; its smaller main-path retry completed.

## Facts checked
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

## Sensitivity
All seven dances concern living cultures. The people sheets show different ages, skin tones and body shapes without presenting one figure as a whole community. Every new person asset is marked people true.

A fresh sensitivity reviewer should examine example clothing, simplified lion wake/bow, zapateado versus skirt study, solo Irish versus ceili, Punjabi harvest versus modern forms, buchaechum's creator and group geometry, Black New Orleans credit, and Ga-specific movements/drums. The Cervantino source contains conflicting 1945/1954 wording; notes use the corroborated Korea.net 1954 account. The two-pose turns are introductory movement studies, not documentary choreography. Music still needs a listening review.

Owner/sensitivity contact sheets: _scratch/family-dance-night/review-people-1.png through review-people-3.png. No outside-contact approval gate was added.

## Flattest moment left
An unsuitable word still gets only the spec's short look-again response. It does not explain a misconception automatically. The class or solo learner must point to the movement and discuss it; adding a scored quiz would change the brief.

## Graphics
Retained the warm gym, seven object tables, maroon controls, count display and growing lights. Inspected all fourteen original paintings and all 28 finished people poses. Painted icons now match the stage. The strongest new moment is the complete lion rising, rather than a painted head over elongated code legs.

The cast has two key poses per move, with a local renderer/geometry table for swapping figures. Complete subjects were recropped before scripts/art.py --rekey. Four off-style sheets were redrawn. Art: 1,581,114 bytes; offline bundle: 2,293,859 bytes (2.19 MiB). Kept teaching art above the 2 MB goal; below the 6 MB notes threshold. No missing art token remains.

## Audit
**Audit not finished.** The single 2400-second-limited invocation used Chrome 9961, host 8765 and the dedicated review profile. It exited with TimeoutError in CDP domain enabling before the first screenshot. It produced no audit.md, PNGs or actionable leads. It was not rerun, following CODEX-REVIEW's audit-once stop rule.

Failure record: _scratch/family-dance-night/review-audit/run-failure.md. Targeted 1366x768 runs reported zero console errors; grayscale and Motion off were inspected. The calm painted pose stayed identical while its clock advanced. Those checks do not replace the missing responsive audit.

## Left open
- Seven other STANDARDS sizes, resize stress and the full mechanical walk need verification in the next workflow. Do not infer a pass from the builder's older audit.
- Recorded clear-teacher narration and an acoustic/cultural listening review remain future work; the build rules prohibited making recordings here.
- Exact GeoNames coordinate refresh and the temporarily unavailable Edomex lesson page were not independently cleared live. Notes retain their provenance and other verified sources.
- The spec's 38-pair total should become 41; spec/shared-family edits were outside the write boundary. Shared Motion remembers its setting locally; dance visits and votes are transient.
- Unattended choices: followed the owner's painted-cast decision over the older code-figure art plan; used two key poses per move; retained browser narration and the observation format. No new mode, score, upload or outreach.
- The initial location/brief read completed in 0.2 seconds without an explicit timeout wrapper. Subsequent shell commands were bounded. No git commit or shared-file change was made.
- Chrome 9960/9961 and host 8765 had no responding listener at closeout. No host.html remains in the tool folder. Evidence map: _scratch/family-dance-night/README-REVIEW.md.
