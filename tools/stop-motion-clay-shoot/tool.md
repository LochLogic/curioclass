# Stop-Motion Clay Shoot: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: stop-motion-clay-shoot

#### Built

Built in the verified workspace `S:\CurioClass-codex`. Build only: no git commit, shared-kit edit, deployment, or polish round.

The tool includes the club rough cut, actual rendered-pixel Jump Finder, diagnosis cards, four repairs, manual halfway posing, three story plans, two sets, ten character poses, four props, seeded studio conditions, 48-frame capture, checks, reshooting, keyboard controls, and a cinema with title/end boards and three original synthesized music loops.

Required source, draft metadata, teacher notes, voice text, art, audit states and handoff are present. The generated standalone HTML is 884,950 bytes (864.21 KiB). Its SHA-256 is `0a43ee77ff551977b8ca970b6227520b9944abdab982bd15820f9d86614addfe`.

Evidence and temporary files are in `../../_scratch/stop-motion-clay-shoot/`. The source has 1,205 readable lines, none over 170 characters.

Process deviation: CODEX-BUILD's bar-tool bundling instruction was followed before recognizing its conflict with the user's stricter write boundary. The ignored HTML bundles for snowy-mail-route and beat-lab were regenerated. No source files in either tool were edited. All subsequent project writes stayed in the two authorized folders. The report was deliberately created last because the user required stopping when it was written.

#### Numbers check

Independent computation: `numbers.py` and `numbers.json` in Scratch.

- Explicit timing model: 6 captured frames per second on twos; 12 on ones. Thus 24, 36 and 48 captured frames last 4, 6 and 8 seconds on twos.
- Crossing 100 units in 24 photographs: 4.1667 units per photograph. Movement thresholds: Moss 18 / 2 = 9; Wren 12 / 2 = 6.
- Untaped tripod: `(7/8)^24 = 0.0405689` probability of no bump; expected bumps `24/8 = 3`.
- The planted large move is exactly 14 units, not 14 plus the ordinary movement increment. A correct midpoint splits it into two small moves.
- WCAG contrasts: white/rose 6.074; rose/paper 5.426; rose/panel 4.690; ink/paper 14.552; muted/paper 5.932; ink/panel 12.578.
- The art enumeration is 21 assets, despite the spec's total of 20. All 21 are included.
- The spec's timing terminology conflicts with conventional 24-fps production usage. Its explicit durations win; notes explain the distinction. The hand tip uses 1.5 seconds to match its trigger.

#### Facts checked

Facts were checked against the supplied spec and independently recomputed where numeric. No live web verification or independent inspection of the cited book was performed.

| Student-facing statement | Named source or basis |
| --- | --- |
| Pose, capture, repeat creates stop-motion | Aardman Animate It! resources; Shaw, Stop Motion: Craft Skills for Model Animation, 2nd ed., 2008 |
| A moving camera changes the whole set's edges | Shaw, camera/animation guidance; the spec's frame model |
| Daylight changes can cause flicker; lamp and covered windows stabilize it | Shaw; Into Film stop-motion education guides |
| Tape tripod feet and avoid leaning on the table | Shaw; Into Film; supplied fix cards |
| Keep hands out; remote shutter or waiting avoids the simulated hand | Shaw; Into Film; the 1.5-second duration is the spec's model rule |
| Small moves and onion skins help maintain continuity | Aardman; Shaw; the spec's movement model |
| 100-unit set, 1-unit camera threshold, 8-percent light threshold, half-length movement rule | Explicit teaching thresholds in the spec, not published professional limits |
| Timing, 48-frame cap, 1-in-8 bumps and up-to-12-percent cloud changes | Supplied model; independent arithmetic and functional boundary checks |
| Plan, create, revise, practice production skills, present | National Core Arts Standards Media Arts MA:Cr1, Cr2, Cr3, Pr5 and Pr6, grades 3 to 5 |
| Moss, Wren, stories, club film and toy cinema | Original fictional content specified for this tool |
| Saved on this device, no camera access or upload | localStorage implementation; final source/reference inspection |

#### Break it

34 core assertions pass in `functional-results.json`; 17 additional checks pass in `post-results.json`.

- Rapidly try every cause: wrong guesses do not tag or repair. The cards close; another frame comparison is required before retrying. Positions rotate so a fixed location sequence does not solve the cut. Event speech is tied to the current attempt.
- Tag ordinary small moves: rejected. A correct diagnosis is based on that frame pair's recorded conditions.
- Repeatedly submit the unchanged missing pose: rejected. A valid pose must be near the midpoint and leave both movement gaps within the threshold. No success meter reveals distance to the answer.
- Repeat a correct diagnosis or fix: no extra repairs or score are created. There is no saved best score.
- Snap nothing, one photograph, or 24 identical photographs: no clean-animation message. The tool asks for a pair or an intentional move. One real small move then passes when the studio is stable.
- Make a large Wren move with all studio protections enabled: still detected. Exactly 9 Moss units and exactly 6 Wren units are allowed; values just above are flagged. The light boundary is also tested.
- Use unsafe studio settings for 24 quick pose-and-snap actions: camera, light and hand problems appear. With all protections on and small moves, none appear.
- Rerun Check or reload to reroll luck: photographs and marks remain identical. `studio-before-reload.json` equals `studio-after-reload.json` for all 24 frames and nine marks.
- Change sets between photographs: set selection now applies consistently to the whole film, preventing an unmarked scenery discontinuity.
- Spam Snap past 48: capped. Reshoot removes and replaces the selected photograph at its original position.
- Change speed, onion skin, Finder and the playhead during Play: live. Seeking keeps playing; Stop ends playback immediately.
- Real jittered mouse drag followed by a quick snap: Moss moves six units and the first frame contains a detected hand. Keyboard-only navigation moves six units and captures one photograph.
- Cached thumbnail generation keeps tested snaps below 100 ms: maximum observed 27.6 ms on this machine.

Guessing with repeated comparisons can eventually repair the fictional film. The result records actual repairs, not a claim of diagnostic mastery. Story quality is not scored.

#### Voice walk

`Curio.voice` owns narration and Read. Bank preparation is firm-captain / Alnilam. No voice recordings were made; actual speech uses the kit's browser fallback.

Held clicks used a 120-ms press and a two-second tap pace. Saved logs:

- `voice-main-cut.json`: welcomeCut, finderHow.
- `voice-repair.json`: tagHow, rightCamera, fixedCamera.
- Final `voice-studio.json`: welcomeStudio, setupHow, shootHow. Five subsequent snaps do not repeat how lines.
- `voice-premiere.json`: Read speaks premiereHow, then premiere is an event when the screening starts.

An initial shooting instruction went stale while waiting behind a setup line. Step changes now hush speech belonging to the previous step, so the current how line starts promptly. The final log records intentional cuts of welcomeStudio and setupHow when the student advances; shootHow starts and is not lost. Mode scope and attempt/result validity drop queued stale events. Hints change synchronously and Read uses the current hint.

The audit's complete automated repeat/quick-tap voice walk did not run before interruption. Captured manual paths passed; that broader coverage remains open.

#### Feel check

Played the repair-to-studio-to-premiere path using the interactive controls and model checks, including a real drag and a keyboard-only capture.

Best moment: the hand becomes a bright silhouette while the unchanged garden goes dark, followed by a repair that removes exactly that intrusion. The halfway pose uses two visible ghosts and requires a real positioning choice.

Flattest moment 1: the original small wooden sign made the title spill beyond its writing area. Redrew a wide board and fitted the title onto its surface in up to two lines. The cinema now feels like a screening of the student's film.

Flattest moment 2: compact posing controls and a cropped camera view hid the useful action. Fixed canvas sizing, moved the compact pose bar into the sky area, reduced redundant panel controls, and kept the photograph strip following the current frame.

The handmade clay, felt, paper scenery, overhead studio and toy audience give this tool a distinct place. It is visually richer than the simple reference scene and appropriately less dense than Beat Lab for this age group. Later work changes the challenge from finding planted errors to controlling a student's own studio and story.

![Clay Shoot beside the Beat Lab reference](../../_scratch/stop-motion-clay-shoot/bar-comparison.jpg)

#### Done when

1. PASS: camera view dominates the workbench at 1366x768, 680x425 and 375 wide; strip stays beneath it. Final compact and phone frames inspected.
2. PASS: four planted problems produce their specified differences and accept their causes. The four repaired causes leave no flagged pairs; the manual in-between creates photograph 37.
3. PASS: unsafe 24-frame shoot detects camera, light and hand problems; protected small-move shoot is clean; protected large move is still flagged.
4. PASS: saved photographs and check marks agree exactly after reload. Play and Check read the same records rather than generating fresh luck.
5. PASS: live controls and immediate Stop verified by the additional assertions. Premiere shows the relevant screening controls; diagnostic controls remain in Rough cut and Studio.
6. PASS: title, film and end card playback implemented; all three music choices and silence start successfully. A full screening was observed in the held-click path. No camera or upload API is used.
7. PASS on recorded main and side paths: how lines occur once, events use event narration. Full automated voice stress coverage is incomplete because the audit was interrupted.
8. PASS: frames and choices persist; Rough cut progress reloads; Start over confirms and clears all work. Reset is available from Rough cut for every mode's saved work.

#### Wave lessons

| Lesson | Result and evidence |
| --- | --- |
| Hint and voice | PASS on captured walks: synchronous hints, Read, once-only how lines, stale validity checks and prompt current-step speech |
| Focus and layout | PASS targeted: persistent step navigation, retained control focus, preventScroll restoration, no focus on initial load, reserved hint height |
| Sizes and targets | PASS inspected: all eight required sizes, 44-pixel targets, compact controls and 375 iframe states; mobile labels now use actual 10-pixel text |
| No giveaways | PASS: visual evidence, rotating cause cards, retry comparison, no proximity meter, saved best score or answer flag |
| Honest numbers | PASS: live frame durations and counts; explicit simplified timing model and teaching thresholds in notes |
| Standards | PASS: solo planning, setup/capture, diagnosis/revision, production controls and premiere choices teach all five codes |
| Motion off | PASS source and captured frame: idle indicator has animation:none; explicit playback retains its timing |
| Short choice sets stay visible | PASS after targeted fixes: removed duplicate panel image/buttons, extended compact layout, checked six Wren poses on phone |
| Resize mid-animation | OPEN: interrupted audit did not reach its full resize/stress stage; no exception was observed in completed screenshot batches |
| No late welcome after first action | PASS captured paths: current-step hush and kit first-tap behavior; Read-first Premiere skips the welcome correctly |
| Unknown shown as unknown | N/A: no hidden network/map status; untagged frame causes stay unmarked |
| One look, one meaning | PASS: tripod, light, hand and movement symbols have a text legend and cause names; no color-only meaning |
| Badges state what is true | PASS: repairs reflect real changes; empty and still shoots cannot earn the clean-animation message |
| Hints change back with state | PASS captured mode/phase changes and reset; Read follows the displayed hint |
| No answer by copying words | PASS: the diagnostic clue is a rendered difference image, not wording copied from the correct card |

#### Audit leads

The single audit used Chrome 9991 and host 8795 with a 40-minute command limit. The session ended during state checks. The saved partial `audit/audit.md` reports 30 leads and 83 frames. It is a pre-fix, unfinished audit, not a clean final audit. Its default Motion off/Resize summary rows do not establish that those later stages ran. It was not restarted, following the one-audit instruction.

Every saved lead is accounted for below; counts total 30:

| Leads | Disposition |
| --- | --- |
| 8 scrolling-strip leads across sizes | Intentional: the spec requires a sideways 36-to-48-photograph timeline. It now follows the selected photograph; arrow controls and keyboard stepping remain visible. |
| 2 zero-font mobile label leads | Fixed: actual 10-pixel button text replaces pseudo-labels hiding zero-size text. |
| 8 Plan-counter overlaps, repeated in mode and Plan states | Fixed: irrelevant frame counter is hidden during planning. |
| 2 Plan canvas-covered keep leads | Intentional storyboard editor over the set. Global keep region now identifies its owning viewer rather than the covered canvas. |
| 2 Setup short-panel leads | Fixed: removed duplicate overhead thumbnail and redundant onward/reset controls; verified 1000x625 and 1280x720. |
| 1 Wren/pose-bar overlap | Fixed: raised compact pose bar and constrained long labels with full tooltips. Phone six-pose and compact frames inspected. |
| 1 Shoot canvas-covered keep lead | Intentional pose palette over the sky portion of the viewer; actor hit targets remain clear after the fix. |
| 2 Premiere visibility/short-panel leads | Fixed: compact layout through 700 pixels tall and removal of redundant back/reset controls. Premiere button is visible in targeted 680 and 1000 frames. |
| 4 Reset-dialog background keep leads | Intentional modal: background viewer, Play, Stop and hint are blocked while Keep my work/Clear and start are active. |

Fresh targeted batches after the restart report zero console errors. The initial host favicon 404 was a harness request; the host now uses a data favicon and the repeated phone batch has zero errors. Final static checks parse all HTML references and find no external or unresolved asset loads.

#### Frames looked at

Inspected the artwork contact sheet, both bar-tool frames, all early/functional/size/voice/drag/keyboard/gray/calm frames, 83 saved audit frames, and the final targeted frames. Scratch `sheets/` contains four-frame visual sheets covering these PNGs; key compact, cinema and default frames were also opened at full size.

Required-size coverage: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 through host 8795. Latest targeted evidence is in `post/`, `post-phone/`, `final-check/` and `final-phone/`. The last phone frame shows Wren's six poses and photographs 41 to 48 with no page-width overflow.

#### Art made

21 final images, 594,872 bytes (580.93 KiB) of optimized WebP. Generated with the built-in image tool; processed only with the free art.py rekey operation. Five assets were redrawn once: kitchen, Moss tuck, overhead studio, pebble and wooden title board. Final art contains no people. The rejected kitchen candidate is explicitly marked people:true in Scratch's rejected-art manifest and is not used.

Original budget: approximately 1,100 KB images plus 350 KB voice within a 2 MB goal. Actual voice assets: 0 KB, because this is an unrecorded build. Total standalone bundle: 864.21 KiB. The prepared voice text and original Web Audio loops remain included in code.

#### Art still to paint

None. All 21 specified assets are generated, optimized, inspected and used.

#### Engine changes wanted

None. All workarounds and music remain in this tool.

#### Left open

- Full mechanical audit completion, automated rapid/repeated-click voice coverage, remaining state extremes and resize stress. The partial report and targeted final evidence are preserved for cold review.
- Alnilam recordings are not present; browser voice timbre varies. Fixed text is ready in voice/lines.json, and no recording service was called during Build.
- The spec's unconventional timing vocabulary is retained with an explicit teacher explanation. No open questions were listed in the spec; unattended choices and contradictions are documented in handoff.md.
- The bar-bundle write-boundary deviation is recorded under Built and in handoff.md.

Final static and syntax checks pass. Ports 9990 through 9997 and 8795 were checked closed. The host file is removed. No commits were made. Build stops with this report.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: stop-motion-clay-shoot

#### Played
Cold solo Grade 4 play reached Rough cut, Plan, Set up, Shoot, Check and Premiere before reading builder notes or source.
The complete repair-to-premiere run followed during verification. The pixel-difference reveal is strong; setup initially felt like changing labels.
Reviewed the Teaching, Play and Craft lenses in one pass. **HOLD:** a spec-level guessing exploit remains; the mechanical audit did not finish.
Workspace was `S:\CurioClass-codex`. No commits. Project writes stayed in this tool and its Scratch folder.

#### Findings fixed
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

#### Findings left
- **Blocker, general, Rough cut:** after a wrong cause, Previous then Next reopens a fresh attempt on the same pair. Cycling cause names can still obtain a diagnosis and its repair without recognizing the image. Confirmed in `cheap-cause-cycle.json`.
- The prescribed four-card retry and repair progress are retained. An independent evidence/transfer gate would add an interaction beyond this spec, so CODEX-REVIEW section 3 requires leaving this to the spec owner. Do not treat four repairs as proof of diagnostic mastery.
- **Should fix, validation:** the automated all-state, every-control, rapid-input and resize sweep remains unverified after the audit's connection failure. This is not a clean mechanical-audit result.

#### Break it
- **Diagnosis/progress:** ordinary frames cannot be tagged; wrong cards do not tag or repair. The step-away-and-back cause cycle still passes, as disclosed above. There is no saved best score.
- **In-between:** repeated unchanged submissions and the far endpoint were rejected; a seven-unit midpoint split the rough cut's 14-unit gap and produced 37 frames with no configured faults. Wren's ten-unit gap required a five-unit midpoint. A complete position sweep was not run; free positional retries remain possible.
- **Technical pass:** empty, one-frame, 24 identical frames and prop-array reordering do not pass. One intentional small move under protected settings does pass. A prop teleport gets only the explicitly scoped result, with a prompt to inspect props.
- **Thresholds:** exactly 9 Moss units, 6 Wren units and 8 percent light change pass; just-over values are marked. Camera changes over one unit are marked.
- **Unsafe shoot:** 24 quick pose-and-snap inputs produced camera, light and hand marks. Protected small moves produced none. A protected large Wren move remained detectable.
- **Reload/reroll:** all 24 unsafe frame records, studio choices and 33 marks matched exactly after reload. Check reads saved conditions and cannot reroll them.
- **Capacity/revision:** 51 Snap calls stopped at 48 frames. Reshooting frame six removed one and inserted its replacement at the same position.
- **Playback:** speed, Finder, onion skin and seeking remained live; seeking kept playback running and Stop stopped immediately. Premiere has no score or reflection gate.
- Thirteen functional assertions passed in `functional-result.json`; live input and frames supplement the model checks. Every test batch that completed reported zero console errors.

#### Voice walk
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

#### Facts checked
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

#### Sensitivity
None requiring a cultural reviewer: original fictional clay animals and toy scenery, no cultural, religious or historical representation. The only human-body image is a neutral code-drawn filming-hand silhouette. All 21 generated assets are marked people:false; no people were missing from this tabletop simulation.

#### Flattest moment left
Fixing window-light flicker can require many nearly identical individual light repairs. The main default shoot needed eleven. It demonstrates the setup choice but drags; a batch correction would exceed the specified per-frame fix.

#### Graphics
Inspected all 21 assets on a contact sheet, the character poses directly, and their use in the camera, Setup and cinema frames. The spec says 20 but enumerates 21; all enumerated assets stay. Kept the tactile clay/felt/paper style and toy audience.
The built-in image tool redrew `art/title-wood.webp`; its final prompt and provenance are in `art/prompts.json`, with the PNG in art/raw. No downloaded art or recorded audio.
Final art: 602,054 bytes. Standalone bundle: 898,333 bytes, 877.3 KiB. No missing art tokens or external loads. All required default sizes were opened: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 in host 8765.
Also opened populated modes, capacity, in-between, long title, grayscale and Motion off frames. Motion off had zero running infinite animations. Keyboard figure movement was used in the full path; prop positioning retained visible focus.

#### Audit
One attempt, last: `audit_tool.py stop-motion-clay-shoot _scratch/stop-motion-clay-shoot/review-audit --port 9961 --profile S:/CurioClass-codex/_scratch/stop-motion-clay-shoot/chrome-prof-review --host-port 8765`, with a 2,400-second process limit.
Exited 1 before the first frame: ConnectionResetError, WinError 64, in the CDP WebSocket handshake. It wrote no audit.md and no mechanical leads. Not retried. Failure details are preserved in review-audit/review-failure.txt.
Independent checks above are evidence only for their stated paths. The audit failure does not establish passing resize stress, all controls, or every mode at every size.

#### Left open
- Spec owner must resolve the cause-card guessing exploit and free in-between retries before claiming assessment validity. No extra quiz, scoring system or gate was added during review.
- Retained the spec's explicit durations. Into Film's usual 24-fps production example uses twelve unique images per second on twos; this tool uses six. Teacher notes explain the distinction.
- No further audit or polish pass. All assigned Chrome ports and host 8765 were verified closed; tool-folder host.html was removed.
- Unattended choices followed the specified stories, default unsafe studio and explicit duration examples. No questions or permission requests were sent.
- Process deviation: the initial short file-read batches completed without an explicit process-kill timeout; subsequent commands used a bounded runner. No long-running command was left unbounded.
- Cold-play limit: the initial tour sampled all modes but completed the four repairs only after source inspection. The later full voice walk was therefore verification, not a second cold play.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Stop-Motion Clay Shoot build handoff

#### Structure
`src.html` starts from the kit starter structure. The style block lays out an animation light box and a compact control desk. The script holds content, saved state, common frame rendering, pixel differences, Rough cut, Studio, Premiere, input, and voice. `window.__tool` exposes the model and functional hooks for reproducible checks.

Frames contain set name, character coordinates and poses, props, camera offset, light multiplier and hand layer. The 100-unit coordinate system is independent of viewport size. Bumps accumulate in the saved camera offset. Check and Play consume the same saved records. A difference image subtracts actual rendered RGB pixels and maps change magnitude to lime on near black.

Rough-cut camera repair realigns all later images, including an inserted halfway pose. Light and hand repairs remove their planted problems. The missing pose must lie within 1.1 units of the midpoint and leave both movement gaps within the figure's threshold. Studio insertion uses the same test; a very large gap may need reshooting because one midpoint cannot make both halves small enough.

Wrong cause guesses close the cards and require stepping away and back before another guess. Cards rotate positions by frame and attempt. Progress records film repairs, not diagnostic mastery. Empty, single-frame and entirely still shoots cannot earn the clean-shoot message. At least one intentional pose, figure or prop change is required, alongside the continuity rules.

Studio step navigation is persistent DOM, and title-board selection updates existing controls. The compact pose bar moves into the viewer at heights up to 700 pixels, with full labels available in tooltips. Plan uses storyboard cards over the set. The irrelevant Plan frame counter is hidden. Redundant onward buttons are hidden in favor of the persistent step controls. Start over remains in Rough cut and clears work in every mode.

The set choice applies to the whole film. It changes each saved frame's set name, keeping the backdrop consistent rather than silently permitting a mid-film scenery jump. Thumbnail images are cached, and the strip follows the current photograph without scrolling the page.

#### Spec decisions and conflicts
- No open questions were listed. Unattended choices follow the supplied examples.
- The enumerated Art section contains 21 assets, though its total says 20. All 21 are generated and used.
- The explicit durations win: on twos is 6 captured frames per second; on ones is 12. The spec's production terminology is inconsistent with conventional 24-fps playback. Teacher notes explain it.
- The hand trigger is 1.5 seconds. Its fix text is adjusted from one second to one and a half seconds to match the actual rule.
- CODEX-BUILD requests an early report, but the user's stronger instruction says to stop when it is written. The report is created only after the checks.
- BUILD's older no-art instructions and the spec's FLUX suggestion are superseded by the user's explicit instruction to generate artwork with the image tool.
- Images use magenta keys, including green subjects, and record `people: false`. The only hand is a gray code silhouette. No generated people.
- The bar tools were bundled as CODEX-BUILD asked, before recognizing that generated outputs also fall outside the user's write boundary. No source files in other tools were edited. Their ignored bundles were regenerated; this is a recorded process deviation.

#### Voice
Curio.voice owns the queue and once-only how lines. The tool changes hints synchronously. `voice/lines.json` prepares firm-captain / Alnilam. No audio recordings were made. Browser voices determine the actual spoken timbre until the owner records the lines.

#### Sensitivity
Friendly fictional clay animals, original toy scenery and a generic filming-hand silhouette. No cultural, religious, historical or human-body teaching content. No people images require a contact review.

#### Engine changes wanted
None. No shared kit or engine changes were made.

#### Next review
Use the report and Scratch evidence for cold review. Reviewers should pay particular attention to the spec's timing vocabulary, compact-panel scrolling, the quality of the generated pose set, and the difference between a clean technical check and a compelling animated story. This run is Build only, with no commit or polish round.

The one mechanical audit was interrupted by the session restart. Its saved partial report contains 30 leads. Completed targeted checks address its layout findings; the full automated walk and remaining state/resize coverage are still open for the cold reviewer. The full audit was not restarted, following the one-audit build instruction.

#### Cold review repairs
Premiere now always projects the full-color film, even after Check leaves Finder on. Current-state speech interrupts stale queued hints;
the twelfth-frame Check instruction stays on screen until used. Wren's in-between instructions name the selected figure.
Props have keyboard positioning on their existing buttons. The technical result explicitly states its four checked dimensions;
it does not certify prop continuity or story quality. Equivalent prop arrays no longer count as animation merely because their order changed.
Setup's existing painting now shows the selected window/blinds, tripod tape and remote. The wooden title slab was redrawn with native alpha.
Its manifest uses cutout:false to preserve that alpha through the required art.py rekey resize, rather than keying an already transparent PNG.
The source timing remains the spec's 6 unique pictures per second on twos; conventional production terminology remains a spec issue.
The rough-cut retry can still be guessed by cycling causes after stepping away and back. A separate evidence or transfer gate would change
the prescribed interaction; this is left explicit for the spec owner rather than adding a new quiz during review.

Teaching repair tips now use once-only how narration. Wren selection has its own current-figure shooting hint.
Scene labels describe the pixels actually shown, including Setup and live posing with Finder selected.

#### Cold audit disposition
The single review audit used debugging port 9961, host 8765 and a 2,400-second process limit. It exited before the first
frame with ConnectionResetError, WinError 64, during the CDP WebSocket handshake. It wrote no audit.md and was not retried.
The review's independent screenshots, 13 functional assertions, reload comparison, complete default voice path and side
voice/keyboard checks are in Scratch's review-* artifacts. These do not establish completion of the automated resize,
every-control or all-state-at-all-size walk. All assigned ports were closed and host.html was removed before reporting.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
