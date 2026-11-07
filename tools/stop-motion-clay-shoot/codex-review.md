# Codex review: stop-motion-clay-shoot

## Played
Cold solo Grade 4 play reached Rough cut, Plan, Set up, Shoot, Check and Premiere before reading builder notes or source.
The complete repair-to-premiere run followed during verification. The pixel-difference reveal is strong; setup initially felt like changing labels.
Reviewed the Teaching, Play and Craft lenses in one pass. **HOLD:** a spec-level guessing exploit remains; the mechanical audit did not finish.
Workspace was `S:\CurioClass-codex`. No commits. Project writes stayed in this tool and its Scratch folder.

## Findings fixed
- **Blocker, general, Studio Check:** a teleported strawberry earned an unqualified clean-film message. The result and notes now explicitly limit the check to camera, light, hands and figure spacing, and direct students to watch props in Play. No new grading rule was invented.
- **Blocker, general, Premiere:** Finder left on by Check could project the diagnostic pixels. Cinema playback now always shows the full-color film. Verified on the ordinary Check-to-Premiere path.
- **Should fix, general, voice:** Premiere's start event could wait behind an obsolete welcome. Current-state speech starts promptly, queued hints validate against their displayed text, and Stop drops stale speech.
- **Should fix, general, voice:** lighting advice repeated for every repaired frame. Repair tips are once-only teaching lines; actual check and screening results remain events. The twelfth-frame Check instruction stays displayed until used.
- **Should fix, general, Wren:** in-between instructions named Moss while only Wren was editable. They now name the selected figure. Selecting Wren before shooting also gives a Wren-specific how-to.
- **Should fix, general, keyboard:** placed props had mouse-only positioning. Arrow keys on their existing buttons now move them; Shift moves five units. Strawberry moved 82 to 76 using keyboard only, with focus retained.
- **Should fix, general, still-film gate:** equivalent prop arrays in a different order counted as animation. Action detection now compares visible actor fields and prop positions independent of array order.
- **Should fix, general, scene label:** live posing and Setup could say changes glow while showing a normal painting. Labels now use the actual rendering branch.
- **Should fix, general, 375 Setup:** the set selector's lower edge fell outside the iframe. Reduced empty-strip height; the whole selector now fits. Filled strips retain 44-pixel thumbnails and eight visible frames.
- **Polish accepted, general, flattest moment:** the existing studio painting now visibly gains tripod tape, closed blinds/lamp glow and a remote as their controls change. The clay scene and rich palette stay.
- **Polish accepted, general, weakest art:** redrew the wooden title slab with a cleaner silhouette, restrained grain and a broad writing surface. Preserved native transparency through the free art.py rekey resize.

## Findings left
- **Blocker, general, Rough cut:** after a wrong cause, Previous then Next reopens a fresh attempt on the same pair. Cycling cause names can still obtain a diagnosis and its repair without recognizing the image. Confirmed in `cheap-cause-cycle.json`.
- The prescribed four-card retry and repair progress are retained. An independent evidence/transfer gate would add an interaction beyond this spec, so CODEX-REVIEW section 3 requires leaving this to the spec owner. Do not treat four repairs as proof of diagnostic mastery.
- **Should fix, validation:** the automated all-state, every-control, rapid-input and resize sweep remains unverified after the audit's connection failure. This is not a clean mechanical-audit result.

## Break it
- **Diagnosis/progress:** ordinary frames cannot be tagged; wrong cards do not tag or repair. The step-away-and-back cause cycle still passes, as disclosed above. There is no saved best score.
- **In-between:** repeated unchanged submissions and the far endpoint were rejected; a seven-unit midpoint split the rough cut's 14-unit gap and produced 37 frames with no configured faults. Wren's ten-unit gap required a five-unit midpoint. A complete position sweep was not run; free positional retries remain possible.
- **Technical pass:** empty, one-frame, 24 identical frames and prop-array reordering do not pass. One intentional small move under protected settings does pass. A prop teleport gets only the explicitly scoped result, with a prompt to inspect props.
- **Thresholds:** exactly 9 Moss units, 6 Wren units and 8 percent light change pass; just-over values are marked. Camera changes over one unit are marked.
- **Unsafe shoot:** 24 quick pose-and-snap inputs produced camera, light and hand marks. Protected small moves produced none. A protected large Wren move remained detectable.
- **Reload/reroll:** all 24 unsafe frame records, studio choices and 33 marks matched exactly after reload. Check reads saved conditions and cannot reroll them.
- **Capacity/revision:** 51 Snap calls stopped at 48 frames. Reshooting frame six removed one and inserted its replacement at the same position.
- **Playback:** speed, Finder, onion skin and seeking remained live; seeking kept playback running and Stop stopped immediately. Premiere has no score or reflection gate.
- Thirteen functional assertions passed in `functional-result.json`; live input and frames supplement the model checks. Every test batch that completed reported zero console errors.

## Voice walk
Held mouse presses were 120 ms, with two-second action gaps, Sound on and default studio settings. Playback was allowed to finish before diagnosis.
Path: Play, arrows/strip, Finder, camera/light/hand/move diagnoses and fixes, halfway pose, replay, Studio story, Setup, Shoot twelve small moves, Check, repair light marks, Premiere.
Heard in order: welcomeCut, finderHow, tagHow, rightCamera, fixedCamera, rightLight, fixedLight, rightHand, fixedHand, rightMove, halfway, cutDone, replay cutDone, welcomeStudio, setupHow, shootHow, checkHow, checkMarks, premiereHow, premiere, endFilm.
Evidence: `review-voice/main-path.json` and its frames. Each mode's how-to started when its controls were present. Advancing cuts older speech; queued old-mode lines did not speak afterward.

| Line/group | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| Main-path how-to lines | how/welcome | once each | once each |
| fixedLight across twelve repairs | teaching | 1 | 1; eleven silent repeats |
| checkClean, five Check presses | event | 5 | 5 |
| Moss/Wren shooting instructions, alternating five times | how | 1 each | 1 each |
| Read, including Sound off | read | 3 | 3 |

Read interrupted speech and mode changes released Read. Final allLines and voice/lines.json contain the same 33 strings.
No recordings exist; these checks observe browser-speech starts through the kit log, not a recorded Alnilam performance.

## Facts checked
| Fact | Named source and finding |
| --- | --- |
| Pose, photograph, repeat; small moves; remove hands; revise bad frames | [Into Film, How to Animate, pp. 4-6](https://www.intofilm.org/intofilm-production/7070/stop-motion-how-to-animate-resource.pdf). Consistent. |
| Secure camera; mark tripod feet; onion skins compare neighboring poses | [Into Film, Introduction, p. 6](https://www.intofilm.org/intofilm-production/165/introduction-to-stop-motion-animation-resource-intofilm.pdf). Consistent. |
| Constant artificial light and covered windows reduce lighting changes | [Signals film education, Lighting](https://signals.org.uk/activity-guides/stop-motion-animation/). Consistent; no claim that one lamp is the only valid professional setup. |
| Remote avoids touching the camera; camera stays steady | [Autodesk, Stop-Motion Animation](https://www.autodesk.com/solutions/stop-motion-animation). Corroborates the practical advice; the simulated hand rule is separate. |
| Four-beat planning, revising, production practice and presentation choices | [National Core Arts Standards, Media Arts](https://www.nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf), Cr1/Cr2/Cr3/Pr5/Pr6. Students plan, shoot, compare, repair and present; this is practice, not certification of every grade-level clause. |
| On twos holds each image for two playback frames | [Aardman, Behind the Craft: The Grand Getaway](https://aardman.com/latest-news/2024/january/behind-the-craft-wallace-gromit-in-the-grand-getaway/). Definition agrees; the tool's playback rate is unusually slow. |
| Timing and model numbers | Independently recomputed: 24/36/48 photographs last 4/6/8 seconds on twos; ones is twice as fast. A 100-unit crossing in 24 images is 4.1667 units per image. No-bump probability is 0.0405689; expected bumps are 3. |
| Thresholds, waiting time and fictional content | Spec-defined simulation: 100-unit set, lengths 18/12, half-length thresholds 9/6, camera threshold 1, light 8 percent, cloud wander up to 12 percent, hand timeout 1.5 seconds, seeded 1-in-8 bumps. Not published professional limits. Moss, Wren and the club story are fictional. |
| Contrast | Independently recomputed WCAG ratios: white/rose 6.074, rose/paper 5.426, rose/panel 4.690, ink/paper 14.552, muted/paper 5.932, ink/panel 12.578. |
| Saved locally; no webcam/upload | Source and bundle inspection: localStorage is guarded; no camera, upload or external asset request is used. All tested reloads retained work. |

Shaw's book was not independently inspected. Accessible named guidance above was checked live; no unsupported book verification is claimed.

## Sensitivity
None requiring a cultural reviewer: original fictional clay animals and toy scenery, no cultural, religious or historical representation. The only human-body image is a neutral code-drawn filming-hand silhouette. All 21 generated assets are marked people:false; no people were missing from this tabletop simulation.

## Flattest moment left
Fixing window-light flicker can require many nearly identical individual light repairs. The main default shoot needed eleven. It demonstrates the setup choice but drags; a batch correction would exceed the specified per-frame fix.

## Graphics
Inspected all 21 assets on a contact sheet, the character poses directly, and their use in the camera, Setup and cinema frames. The spec says 20 but enumerates 21; all enumerated assets stay. Kept the tactile clay/felt/paper style and toy audience.
The built-in image tool redrew `art/title-wood.webp`; its final prompt and provenance are in `art/prompts.json`, with the PNG in art/raw. No downloaded art or recorded audio.
Final art: 602,054 bytes. Standalone bundle: 898,333 bytes, 877.3 KiB. No missing art tokens or external loads. All required default sizes were opened: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 in host 8765.
Also opened populated modes, capacity, in-between, long title, grayscale and Motion off frames. Motion off had zero running infinite animations. Keyboard figure movement was used in the full path; prop positioning retained visible focus.

## Audit
One attempt, last: `audit_tool.py stop-motion-clay-shoot _scratch/stop-motion-clay-shoot/review-audit --port 9961 --profile S:/CurioClass-codex/_scratch/stop-motion-clay-shoot/chrome-prof-review --host-port 8765`, with a 2,400-second process limit.
Exited 1 before the first frame: ConnectionResetError, WinError 64, in the CDP WebSocket handshake. It wrote no audit.md and no mechanical leads. Not retried. Failure details are preserved in review-audit/review-failure.txt.
Independent checks above are evidence only for their stated paths. The audit failure does not establish passing resize stress, all controls, or every mode at every size.

## Left open
- Spec owner must resolve the cause-card guessing exploit and free in-between retries before claiming assessment validity. No extra quiz, scoring system or gate was added during review.
- Retained the spec's explicit durations. Into Film's usual 24-fps production example uses twelve unique images per second on twos; this tool uses six. Teacher notes explain the distinction.
- No further audit or polish pass. All assigned Chrome ports and host 8765 were verified closed; tool-folder host.html was removed.
- Unattended choices followed the specified stories, default unsafe studio and explicit duration examples. No questions or permission requests were sent.
- Process deviation: the initial short file-read batches completed without an explicit process-kill timeout; subsequent commands used a bounded runner. No long-running command was left unbounded.
- Cold-play limit: the initial tour sampled all modes but completed the four repairs only after source inspection. The later full voice walk was therefore verification, not a second cold play.
