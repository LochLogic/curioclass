# Flipbook Studio: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: flipbook-studio

#### Built

Built the self-contained Draw, Time and Flip studio from the kit starter, with editable vector starters, onion skins, whole-stroke erasing, per-page Undo/Redo, live holds and fps, clock-based playback, device saving and timed paper printing. Draft stage is built. No commits or separate polish round.

Open questions resolved: omit GIF; retain Print pages as the explicitly described paper flipbook craft. Preserve Blink's specified eight-frame opening hold as an exception to the six-frame editor limit. Full reasoning is in handoff.md.

#### Numbers check

Independent computation: _scratch/flipbook-studio/numbers.json. All published contrast ratios match: 4.91, 5.30, 13.88, 5.54, 9.79, 4.46 and 3.16. Legend text uses the muted text color with full-strength colored dots.

Readouts: ones 12 frames / 1.0 s; twos 24 / 2.0 s; Blink 11 / 0.9 s; nervous Blink 5 / 0.4 s; Ease the ends 18 / 1.5 s. Standard maximum: 288 frames, 48.0 s at 6 fps, 12.0 s at 24 fps, 36 print sheets. Rightmost ball geometry reaches x=890.

Two spec conflicts remain explicit: Blink's 8-frame hold exceeds the general limit; squashed floor drawings require center y=632 for radius 28 and bottom y=660, whereas the unsquashed formula gives 620. The spec was left untouched.

#### Feel check

Best moment: dragging a hold during playback changes the ball's feel without changing a stroke. Copying a page and drawing over its ghost also gives an immediate, tangible result.

Flattest moment 1: compact controls could crowd the paper. Secondary controls now open in a tools drawer while the page, strip and Play remain visible. Nested dialogs return focus to Tools.

Flattest moment 2: many copied drawings put chart numbers on top of one another. Collision-free labels and light leaders now retain all 48 numbers, even at 680x425. A hold drag also locks automatic strip following until release.

Played the draw/copy/erase/revise/time/flip sequence with real mouse input and touch drawing. Compared the studio beside Beat Lab in _scratch/flipbook-studio/bar-comparison.png. Both bar tools were bundled into scratch and opened before implementation. The painted table, paper stack, curl and material detail hold up beside the reference.

#### Done when

1. PASS: real mouse and CDP touch strokes; whole-stroke erasing; Undo restores and Redo removes. See mouse-results.json, eraser-results.json and touch-results.json.
2. PASS: before/after ghosts are blue/green under current strokes in Draw; absent in Time, Flip and the print DOM. Keyboard and mode frames inspected.
3. PASS: all three required readouts independently recomputed and asserted. Blink retains its explicit eight-frame starter exception.
4. FAIL for the literal floor-center formula: Real bounce drawings 3 and 9 use y=632 to satisfy the specified squash and floor contact. Real probes 0,1,3,11 and Even probes 0,1,3,11 were checked; all other tested coordinates and the bunched/even chart behavior pass.
5. PASS: hold edits leave stroke JSON unchanged. At 24 fps, 124 frames advanced over 10.33 loops against 124.8144 expected, an error of 0.8144 frame.
6. PASS: every required desktop/preview size was viewed in all three modes. Paper stays within the measured painted glass. Time retains both chart/page and hold strip.
7. PASS: real held-handle dragging while playing updates timing and preserves artwork; Stop is immediate. A 24-fps compact drag had zero strip movement during the gesture.
8. PASS: Blink prints 11 numbered frames over 8+3 cards, with cut and staple marks. Standard maximum produces 36 sheets. Paths are black, with no painted texture or ghosts.
9. PASS: touch artwork survived reload; confirmed New book saved one empty page; full-storage failure and recovery were asserted.
10. PASS: page, strip, selected thumbnail and Play fit all required sizes. Independent 375-pixel host checks passed with no horizontal overflow; middle selection stayed visible through Time, Draw and Flip.
11. PASS: one onionHow start across five held Copy page actions. Three timing changes at a two-second pace each started holdChanged; newer changes and Stop cut stale speech. Read and mode-switch logs show no delayed queue hang.

The functional suite passed 41/41 assertions. Supplementary real-input, storage, printing, focus, voice, limit and responsive checks are retained in scratch.

#### Wave lessons

- Hint and voice: PASS. Hints update synchronously and name controls. Read speaks the current hint; how-to selection uses V.heard and the kit queue.
- Focus and layout: PASS. Stable controls retain focus; nested modal return is verified. Hint space is reserved. Sound now has a fixed width and caused zero header shift.
- Sizes and targets: PASS. All STANDARDS sizes, 375 host, and 44-pixel controls checked; no clipping found in inspected final frames.
- No giveaways: PASS, not an assessment. There are no hidden answers, scores or solution meters.
- Honest numbers: PASS. Computed readouts, explicit Blink exception, and truthful feedback when holds or fps already match.
- Standards: PASS. Solo students develop artwork, refine timing for intent, and use animation production tools. No family engine applies.
- Motion off: PASS. Audit found no infinite animation; playback continued with the same clock and no curl lift.
- Short choices: PASS. Four starters fit the compact dialog. The sideways frame strip is the explicitly specified editable book sequence.
- Resize mid-animation: PASS. Completed audit stress checks found no exceptions or controls left disabled.
- First-tap welcome: PASS with the spec's stale rules. Page actions and Play deliberately invalidate the Draw welcome; there is no late welcomeAfter queue.
- Unknown as unknown: PASS, not a diagnostic activity; no concealed states are represented as known.
- One look, one meaning: PASS. Ghosts have labeled colors; holds also have numbers; gray label leaders differ from the vermilion motion path.
- Truthful badges: PASS. Counts reflect stored holds and fps; unchanged presets no longer claim new timing.
- Hints change back: PASS. Mode entry, Stop and limits restore an appropriate next action.
- No word-matching answers: PASS, an open studio with no answer cards.

#### Audit leads

Ran the audit once, on Chrome 9991 with host 8795. It completed within 40 minutes: _scratch/flipbook-studio/audit/audit.md. No console exceptions, focus losses or resize failures were reported. Its 35 leads are answered below; the frozen audit precedes the targeted fixes.

- Four tiny-text leads: FIXED. Hidden footer branding now uses a hidden span, with visible text at 10 px. Final compact frame and computed-style check pass.
- Seven “1 seconds” leads: false positives. The regex matches the fractional suffix of “0.1 seconds”; the measurement and plural are correct.
- Two phone-context/hint leads: audit infrastructure could not locate its iframe context. Independent drive.py host runs at the same assigned port verified the actual 375-pixel document, visible hint, controls and zero runtime errors.
- Three sideways-strip leads: intentional, required book timeline scrolling, in bounce-time and page-limit. Selection is brought into view after mode changes and resizing.
- Ten covered keep-region leads: intentional native modal coverage in starter-library and timing-help. Dialog choices and Close remain usable; the background book is deliberately inert.
- Five skipped-welcome leads: intentional stale behavior after New page, Copy page, Delete page, Clear page or Play. This follows the spec; the current hint and Read remain available.
- One minimum-hold dead-control lead: FIXED with immediate limit feedback. The held-click check confirms hold 1 and an actionable hint.
- Three same-mode quick-tap cuts: FIXED by making mode re-selection preserve the current narration. The two-tap recheck logged one welcome start and zero cuts.

Also fixed the Sound label's header shift, bounded print speech to the print operation, and verified unchanged presets/fps without changing the book. Only affected cases were re-shot; the full size matrix and audit were not rerun.

#### Frames looked at

Scratch folders inspected: bar-frames, first-frames, test-frames, interaction-frames, voice-recheck-frames, final-frames, extreme-frames, targeted-frames, post-frames and phone-frames; also touch.png and bar-comparison.png.

Viewed all 21 full-size matrix frames, final five phone frames, grayscale, Motion off, starter/help dialogs, 48-page extremes, the print preview and all 61 audit size/state/calm frames through six contact sheets. Both finished WebP paintings were inspected at final size.

#### Art made

Two original generated paintings: fb-desk and fb-paper. Art totals 98,480 bytes, about 98.5 KB; recorded voice is 0 KB. Final bundle is 219,983 bytes, about 220.0 KB against the 2,000 KB goal. Neither image needed redrawing. No painted people.

#### Art still to paint

None. The schematic Blink face and all editable drawings are intentionally vector strokes, as the spec requires.

#### Engine changes wanted

None. Shared kit, scripts and documentation were not modified.

#### Left open

- The two numerical spec conflicts above need the cold reviewer's attention. Floor contact was prioritized; Blink's explicit starter timing was preserved.
- Narration uses browser speech fallback. The friendly-dad / Achird manifest is ready; no audio was recorded, as instructed.
- Print layout was checked in the browser, not on a physical printer.
- The audit's 375-pixel context detector remains unverified; separate actual iframe checks passed.
- Initial read-only brief/memory commands completed without hard deadlines. Subsequent shell commands used explicit bounded runners.
- The host cleanup helper initially left three processes running. Their exact flipbook-studio host command lines were verified and those processes were closed. Final ports 8795, 9990, 9991 and 9992 are closed; host.html is removed. The scratch helper now terminates and waits on its server handle.
- Report written last to honor the user's stop trigger. No further round follows this file.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: flipbook-studio

#### Played

Cold Grade 7 pass: actual drawing, copying, Time, live hold editing, Flip, Ping-pong and starter/help dialogs before reading the builder's report, handoff, notes or source. The paper and light table invite drawing; timing changes have a tangible effect. Also checked projection use, keyboard and real touch.
Evidence lives in `_scratch/flipbook-studio/`: `cold/`, `before/`, `after/`, `input/`, `voice/`, `phone-recheck/`, `save/`, `review-audit/` and `review-sheets/`.

#### Findings fixed

- **blocker, general, Draw dialogs:** Delete during playback confirmed against a later drawing. The before test left the intended drawing intact and deleted another. Dialog entry now finishes the stroke and pauses playback; the same held-click test removes the intended drawing. Clear uses the same protection.
- **blocker, general, Eraser:** hit testing followed raw control segments while the visible pencil followed a smoothed curve. It now tests the actual Path2D with the eraser's reach. A real drag through a curve 62 units from its control polygon erased it; Undo/Redo restored/removed it.
- **should fix, general, Time teaching:** dot spacing was described as speed with unequal holds, and 24-fps arithmetic sounded universal at the default 12 fps. Guidance now states the equal-hold assumption, including on the compact stage; Why identifies the frame-rate assumption.
- **should fix, general, mode voice:** entering Flip while playing dropped its how-to permanently. Stop now retries the unheard welcome. Compact speech names Options; it no longer points straight to a hidden Ping-pong control.
- **should fix, general, dialog voice:** the first Starters tap could narrate Draw instructions over its inert desk. Dialog entry now hushes guidance and invalidates welcomes; Close retries relevant guidance. Compact starter selection closes its tools drawer so the spoken Play instruction is actionable. Eraser guidance waits for the drawer to close.
- **should fix, general, waiting hints:** Pencil, Eraser, Onion, page selection and FPS could retain a previous action's instructions. These now update immediately, and Eraser has its own once-only instruction.
- **should fix, general, saving:** editing overwrote the full-storage warning. It now persists separately through other actions, is included in Read, and clears after recovery together with a stale failure hint. Rechecked at 680x425 and actual 375x812; fixed the first phone recheck's warning wrap.
- **should fix, general, drawing input:** another finger could replace or end the active stroke. One pointer now owns it; page operations finish it before changing pages and reset held-frame position. Real two-finger input retained one clean stroke.
- **should fix, general, grayscale:** onion direction relied on blue versus green. Previous ghosts remain solid blue; following ghosts are dashed green, with matching legend patterns. Student artwork and printed paths are untouched.
- **should fix, general, Blink strip:** its numeric eight-frame hold filled only six cells, making it look like a six-frame hold. It now occupies eight actual cells and is labeled as a starter exception. The editor still makes ordinary holds 1-6; its drag track stays stable.
- **polish, general, weakest art:** flat starter icons replaced by shaded paper previews showing the actual bounce positions and editable blink phases. Kept both strong paintings and all starter geometry.
- **polish, general, flattest action:** copied pages felt like an unchanged screen. A brief paper-settle movement and responding hold bars now answer editing; Motion off removes these movements.

#### Findings left

- **should fix in spec, general:** Blink timing 8,1,1,1 contradicts the six-frame limit; squashed floor contact y=660 requires center y=632 rather than the unsquashed formula's 620. Kept the explicit starter and floor-contact requirements. The brief forbids changing a contradictory spec during review; it remains unchanged. No new feature or kit change was made.

#### Break it

- No score, best score, quiz, reflection gate, percent or hidden-answer check exists. Repeating presets or copying blank pages earns nothing. Try this cards are optional creative prompts, not claimed assessment.
- Holds: actual live handle drags plus repeated extreme inputs and plus/minus changes stay within 1-6, preserve stroke JSON, update the readout and affect the current run immediately. Blink's original eight-frame exception remains explicit.
- FPS and presets: ones 12 frames/1.0 s, twos 24/2.0 s, ease 18/1.5 s; FPS changes preserve holds. Repeated matching choices do not falsely report new work.
- Limits: attempted more than 48 pages and a 401st real stroke; caps hold and hints give a next action. A 288-frame standard book generates 36 print sheets, eight frames each. Blink generates 11 cards over two sheets; paths are black and omit texture/ghosts.
- Destructive shortcut: Play, Delete, wait two seconds, Continue now deletes the drawing shown when asked. Cancel keeps the book. New book clears the stored book only after confirmation.
- Storage: edited Blink survived a fresh tab with holds 8,3,1,1 at 8 fps, 13 frames; reset survived a fresh tab. Forced quota failure remains visible; a successful save clears it.
- Clock: 121 frames in 5.0539 s at 24 fps, error 0.294 frame across ten loops. Live edits retain the shown drawing; Stop acts immediately. Motion off keeps the clock running.
- Functional suite: 28/28 assertions; separate real erasing, touch, keyboard, storage and held-click checks. No runtime errors in product checks. One host favicon 404 was removed from the test host; it was not a tool request.

#### Voice walk

Sound on, defaults, 120-ms held clicks and two-second pauses: Pencil, draw, Copy page, revise, New page, draw, Time, drag a hold, Play, drag live, Flip, Stop, Ping-pong, Play, Stop.
Spoken starts: `welcomeDraw`, `onionHow`, `welcomeTime`, `holdChanged`, `welcomeFlip`, in action order. Flip's first queued welcome is correctly stale while playing and starts after Stop. `spacingHow` can drop when leaving Time; its assumption remains visible. Logs: `input/main-voice.json`.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| onionHow, five Copy page actions | how | 1 | 1 |
| holdChanged, five live changes | event | 5 | 5 |
| each main-path mode welcome | how | 1 | 1 |
| Eraser instruction, side path | how | 1 | 1 |

Read interrupts speech and works with Sound off; mode changes release Read without a delayed queue. Events supersede stale events; repeated how-to lines stay silent. Browser speech fallback is used, not recorded Achird audio.

#### Facts checked

- **24 fps, ones/twos and expressive holds:** Richard Williams, *The Animator's Survival Kit* (2001), spec's named source; live cross-check [Dave Burgess, Animation Mentor, Timing](https://www.animationmentor.com/blog/timing-the-12-basic-principles-of-animation/). Twelve drawings on twos make one second at 24 fps, six drawings per second at the tool's default 12 fps. Updated the explanation.
- **Spacing, slow in/out, even movement and weight:** Frank Thomas and Ollie Johnston, *The Illusion of Life* (1981), chapter 3; live cross-check [Kevin Koch, Animation Mentor, Slow In and Slow Out](https://www.animationmentor.com/blog/slow-in-and-slow-out-the-12-basic-principles-of-animation/). Dot gaps only imply relative speed with equal exposure time; centers are an approximation when shapes change.
- **Starter coordinates, squash and all readouts:** spec's original formulas, independently recomputed in `numbers.py`/`numbers.json`, then checked against four drawings of each bounce and the browser. Real y=140,204.3078,380,632 at indices 0-3, with the stated floor-contact exception; Even y=140,300,460,620. Nominal ball right edge x=890. Blink 11/12=0.9 s; nervous blink 5/12=0.4 s.
- **Standard maximum and print:** 48 six-frame drawings =288 frames, 48.0 s at 6 fps or 12.0 s at 24, 36 sheets. With Blink's retained eight-frame opener and 47 six-frame drawings, the exception permits 290 frames and 37 sheets; the spec's absolute maximum therefore needs correction.
- **Contrast:** [W3C WCAG 2.2 relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Independent computation matches all seven spec pairs: 4.91,5.30,13.88,5.54,9.79,4.46,3.16. Onion legend colors are graphic accents; words use the muted text color and have pattern cues too.
- **NCAS codes:** [NCAS Media Arts at a Glance](https://nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20Updated.pdf). Cr2 is practiced through developing a sequence, Cr3 through revising timing for a chosen effect, Pr5 through drawing, playback, editing and paper production. These are practiced standards, not a claim of assessed mastery.

#### Sensitivity

None requiring a cultural review: original ball motion, abstract editable blink face and drawing materials; no named cultures, religion, hard history or health advice. No painted people; both raster manifests correctly say `people:false`. The schematic face teaches animation timing, not anatomy or a claim about real emotions.

#### Flattest moment left

A one-drawing loop is intentionally static, and a long hold can look like a pause. The changing hold strip, single-drawing ticks and timing controls explain it; adding a scored challenge or extra animation topic would exceed the spec.

#### Graphics

Opened both finished WebP paintings at final use size, every cold/fault/repair frame, grayscale, Motion off, phone frames and audit contact sheets. Starter previews are richer and more faithful; the table, paper grain, palette, large page and editable pencil art remain.
Art is 98,480 bytes; final bundle 227,031 bytes (227 KB). Both images are present, used and coherently lit; no missing art token, redraw or added raster was needed. The code previews derive from the starter drawings. All 73 audit frames were opened on 13 contact sheets; affected repairs were also inspected at full size.

#### Audit

**Audit not finished:** one run with a 40-minute deadline, Chrome 9951 and host 8755. The session interruption stopped it after sizes, states, Motion off, control walks, repeats and quick taps; resize-stress checks were not completed. It was not restarted. Partial report: `review-audit/audit.md`.
All 28 leads answered: 8 plural false positives parse the tail of "0.1 seconds"; 4 timeline-scroll leads describe the required editable book strip; 10 covered keep regions are the desk behind native modal dialogs; 6 skipped/cut Draw welcomes follow Eraser's own instruction, four page actions or later Play/Stop key toggles. No console, focus, target-size or layout failures were reported in completed stages. Repeats and quick taps were clean.
The audit misses semantic problems such as speaking to the inert desk, misleading hold cells and color-only ghosts. Those repairs, plus storage recovery, received 22 targeted shots at the affected sizes after the audit; all passed with zero runtime errors. The main voice path was replayed. The audit snapshot predates these narrow final repairs; the audit was not run twice.
Wave lessons: next-action hints, focus retention, all eight sizes/44-pixel targets, honest numbers and assumptions, mapped standards, Motion-off timing, four visible starter choices, first-action voice and matching visual meanings were checked. Hidden-information diagnosis and answer-card matching do not apply to this open studio. Resize stress remains the explicit audit limit.

#### Left open

- The two spec conflicts above are explicit rather than silently changing the required starter. No GIF added; keep the specifically authorized paper flipbook craft.
- Print structure and black paths were checked in the browser; no physical printer test. Friendly-dad/Achird recordings remain unmade under the no-recording rule.
- The first two read-only startup commands had a tool wait bound but no process deadline. Subsequent commands use a bounded subprocess runner. Initial Chrome connection reset; its one small retry succeeded. An incomplete custom CDP Enter event was corrected; standard drive.py and corrected keyboard input both passed.
- Audit resize-stress phase is incomplete because the session was interrupted. Completed evidence and partial leads are preserved; no second review pass was started.
- All started Chrome/server processes are closed, ports 9950-9957 and 8755 verified free, and host.html removed. No git commits; writes confined to the two permitted folders. Validation and bundle hash: `review-validation.json` in scratch.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit check 2026-11-06)
Counts: blockers 0 (general 0, family 0), should fix 9 (general 8, family 1), polish accepted 14

### Refine: flipbook-studio

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; no lens found a sensitive
topic). Not a Curiosity: judged as a lesson tool. Frame roots: Teaching `S:/CurioClass-codex-scratch/flipbook-studio/teaching/frames/`,
Play `S:/CurioClass-codex-scratch/flipbook-studio/play/out/`, Craft `S:/CurioClass-codex-scratch/flipbook-studio/craft/frames/`,
shared audit `S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/`. Integrator spot-checked items 1, 3 and 4 in
src.html (confirmed: the play loop moves `state.index` at src.html:1190 and `-`/`+` act on `page()` =
`state.pages[state.index]`; `save()` catch calls `V.say('tooBig')` on every failed save; `printBook()` hushes in
`finally` right after `window.print()`).

#### Blocker
(none)

#### Should fix
1. **`-`, `+` and `Hold the key` hit whichever drawing is playing.** src.html:1504-1505 (`changeHold(page().hold±1)`),
   preset `key` src.html:1146; the play loop sets `state.index` (src.html:1190). While the book loops, three `+` taps on
   Even bounce raised drawings 2, 8 and 12, none chosen; the `xN` readout between the buttons flickers. Seen:
   `play/out/t9-hold-plus-playing.png` and its log. Fixed: keep a selected drawing separate from the playing index;
   while playing, `-`, `+` and `Hold the key` act on the drawing the student last selected, and the readout between
   the buttons names it ("Drawing 5: x1") and stays still. Hold handle drags already work and must keep working. (general)
2. **On ones and on twos are taught at film's 24 per second, but every starter runs at 12.** Why note src.html:457-460,
   preset `twos` src.html:1144, notes.md "A 5-minute start". On twos at 12 gives 6 new drawings a second: the Real
   bounce just plays slow and choppy, the opposite of "still look smooth". Seen: `teaching/frames/t9-twos-12.png`,
   `audit-r1/state-timing-help-1366x768.png`. Fixed: say it where the student acts. Why note gains a sentence like
   "At 12 per second, this book on ones already looks like film on twos. To see film's twos, tap 24, then On twos."
   After the On twos preset at 12 per second or less, the hint names the result ("On twos at 12 per second: 6 new
   drawings a second. Tap 24 to see film's twos."). notes.md's 5-minute start says the same (tap 24 first). Do not
   change the starters' fps (see open questions). (general)
3. **`tooBig` is spoken again on every change while storage fails.** src.html:557-564 `save()` catch. With setItem
   throwing, five actions 2.5 s apart spoke it 5 times (twice within 170 ms) and pushed out onionHow both times.
   Seen: `craft/frames/f1-toobig` and log. Fixed: speak it once per failure run; speak again only after a save has
   worked and then failed again (the footer warning and hint stay). Students on locked-down school browsers hit this
   on every mark. (general)
4. **The `printed` line can never be heard.** src.html:1416-1424 `printBook()`: `V.say` queues, `window.print()` blocks,
   then `finally { finishPrint() }` runs `V.hush()` before the line starts. Seen: `craft/frames/b7-print` log
   "printed dropped hush". Fixed: speak the line before opening print (start print after the line has begun, e.g. a
   short timeout or awaiting the line start), or speak it after `afterprint` as the next step; either way the hint
   and the line say the same words. (general)
5. **Starter loaded: the hint and the spoken line disagree.** src.html:1028-1029. Real/Even bounce speak "Press Play,
   then load the other bounce from Starters and compare." while the hint shows "Tap Play to watch. Tap Time, then
   drag the hold handles." Read speaks the hint, so the Real versus Even comparison (the core contrast) never shows,
   and a student with Sound off never meets it. Seen: `play/out/s1-starter-real-hint` log. Fixed: one sentence,
   shown and spoken: the hint shows the starterBounce line (keep the compare step). (general)
6. **The bowling ball Try this card asks for a move the hold controls cannot make.** src.html:466. Real bounce holds
   all start at 1, so "fewer frames at the top" gives "This hold is already 1 frame" (src.html:1119-1124) and a solo
   student stops. Seen: tried by Teaching and Play; `audit-r1/state-timing-help-1366x768.png`. Fixed: give the card a
   first move with the hold controls, e.g. "Make the Real bounce feel like a bowling ball: tap On twos, then give the
   top drawings 1 frame and the floor drawings 4." (Play's wording; it keeps the card about timing only). Update the
   same card in notes.md if it is there. (family:flipbook, merged with Play 7 tagged family:none)
7. **"Hold the key" uses a word the tool never teaches, and nothing asks the student to plan (MA:Cr2.1).** src.html:341
   and the Why dialog. Cr2.1.6-8 is "organize/design, propose, and evaluate ... plans"; the tool has organizing and
   evaluating but no planning step, and "key" is undefined. Seen: code read of every control and card. Fixed: one Why
   sentence defining a key drawing (the drawings that mark where a move starts, turns and ends; Williams, "Keys,
   extremes and breakdowns") and one Try this card that plans before drawing, e.g. "Plan a jump: draw the start, the
   top and the landing first (your keys), then add the drawings in between with onion skin, closer together near the
   top." Add the matching line in notes.md and the source. (general)
8. **The playing hint says "tap Time" while in Time, and says nothing about drawing while playing.** src.html:528.
   Seen: `play/out/t4-time-playing-hint`. Fixed: the playing hint follows the mode. In Time: "Drag a hold handle or
   tap a preset to change the feel. Tap Stop to pause." In Draw: "Tap Stop to draw." (a stroke is silently ignored
   while playing, src.html:1320; also show a not-allowed cursor on the page while playing). In Flip the current line
   fits. (general; folds in Play nit 10)
9. **Empty-state line fails contrast.** `#empty span`, src.html:91-94: #84786a on #fbf6ea at 12 px is 3.99:1 (under
   4.5:1, paper grain lowers it more). Seen: `craft/frames/a-default-1366`. Fixed: use the spec's muted #6b6258
   (5.54:1). (general)

#### Polish accepted
10. **Flip gets its own layout.** Spec: Flip is "the page alone, as big as the stage allows"; now it lays out exactly
    like Draw (`audit-r1/state-mode-flip-1366x768.png`, `play/out/f1-flip-playing`). In Flip, shrink the strip to a slim
    progress row (numbers and the playing marker) and give the page the height. Keep Done when 6 and 10. (family:none)
11. **Empty book: Time and Flip invite Play on nothing.** src.html:538-541 (`play/out/f2-empty-flip`, `f3-empty-time`).
    When no drawing has strokes, the hint in Time and Flip says "Draw on the page in Draw, or tap Starters for a
    ready-made book." (general)
12. **Blink spacing chart shows one stray dot.** drawChart src.html:650; all four centers are (480, 350)
    (`teaching/frames/t7-blink-time.png`). When every dot coincides, draw one dot and a caption: "These drawings do not
    travel: the change is in shape, so timing does all the work." (family:flipbook)
13. **Ease the ends on a loop slows only one top.** preset `ease` src.html:1145. After the preset, the hint says what it
    did: "Ease the ends slowed the first and last drawings of the book. For a bounce, hold each top drawing longer by
    hand." (family:flipbook)
14. **Readout and hint are the smallest text when projected.** `#readout` 12 px, `#hint` 13 px at every size
    (`audit-r1/state-live-flip-1920x1080.png`). Scale both up on large windows, about 16 px at 1920 wide. (general)
15. **Compact sizes hide Undo inside Tools.** 680x425 and 800x500 (`audit-r1/size-680x425.png`,
    `state-mode-flip-680x425.png`): the lone Tools/Timing/Options button sits beside empty space. Put Undo next to
    Tools on that row. (general)
16. **Blue pencil matches the onion "before" ghost; Red matches the chart.** Blue pencil and onion before are both
    #2f6fd6; Red and the chart are both #c8341a (`craft/frames/e1-blue-pencil-onion`, `e2-red-pencil-chart`). Shift
    Blue pencil to an indigo or cyan clearly apart from the ghost (keep it at or above 3:1 on the page), and give the
    chart dots a light outline ring so they read as an overlay; the chart stays in the accent (spec Look). (family:drawing)
17. **Heavy books get slow.** `changed()` repaints all thumbnails; `save()` writes the whole book on every stroke end,
    hold step and reorder; points saved at full float precision (src.html:1305-1308). At the spec's limits a render
    took 67 ms, a reorder 109 ms, the save 3.86 M characters (`craft/frames/d1-heavy`). Repaint only the changed
    thumbnail, round saved points to 0.1 unit, debounce the save during a drag. Old saved books must still load.
    (general)
18. **notes.md says "the spec".** "Good to know": rewrite as "The Blink starter opens with an 8-frame hold on its first
    drawing (a calm blink). Editing it switches to the 1 to 6 frame range." (general)
19. **notes.md Support at home: a rolled ball does not start slow.** Replace with "Drop a ball and let it bounce. Watch
    where it seems to hang at the top and where it rushes at the floor, then compare with Real bounce." (general)
20. **Nit: "twos are half the drawing".** src.html:459: "half the drawings". (general)
21. **Nit: a missed erase still pushes an undo step.** src.html:1331-1334: push only when a stroke is removed, so Undo
    never appears to do nothing. (general)
22. **Nit: tapping the hold track rounds to the wrong cell.** src.html:885 `Math.round(x/15)`: use the cell tapped
    (`Math.ceil`, clamped 1 to 6); handle drag unchanged. (family:drawing)
23. **Nit: canvas label promises arrow keys on an unfocusable canvas.** src.html:369: reword to match (e.g. "Arrow keys
    Left and Right step pages") or make the stage focusable; arrows already work from the page. (general)

#### Settled calls
- Welcome after a first tap on New page, Copy page, Delete page or Clear page (Play 6, audit lead): not a bug. The spec
  makes welcomeDraw stale when a page button is tapped, and the hint still shows it. Do not change.
- Audit leads "count and word disagree: 1 seconds" (it read "0.1 seconds"), keep-region covered in starter-library and
  timing-help (modal dialogs), and "choices cut short" on `#film` (the strip scrolls sideways by spec): all three lenses
  agree these are wrong. Do not change.
- Bowling card wording (item 6): Teaching offered "delete one top drawing in Draw", Play "start on twos". Took Play's,
  so the card stays about timing with the hold controls, as the Even bounce card is.
- Ones/twos (item 2): fixed in words and hints, not by changing the starters' fps (that is a Content change).
- Chart color (item 16): the spec puts the chart in the accent; fix by outlining dots and moving Blue pencil, not by
  recoloring the chart.
- Keep: the voice line set (12 lines, matched both ways), Ping-pong without a doubled end drawing, the 24 per second
  clock, print with repeated held drawings, Motion off and Read behavior. All lenses passed these.

#### To the spec's open questions
- Should the bounce starters open at 24 per second on twos, so "on twos" is true by default (Teaching 1)? This changes
  Content and every readout check in Done when 3.
- If the planning Try this card (item 7) is judged too thin for MA:Cr2.1.6-8, give Cr2.1 a 6-8 home in another tool of
  the module (storyboard-studio is 9-12) per BASELINE rule 2.

#### Not taken
- Teaching 4, an intent goal in the Blink starter line and a Try this card shown in Time: changes a spoken line (voice
  regen) and adds panel content; the Blink card already asks "calm or startled?". Revisit in round 2 if Teaching still flags it.
- Play 7 second half, a "Load Real bounce" button on each Try this card: new controls in the dialog, not needed once
  the card has a first move.
- Craft nit 9, 10 to 11 px labels: all pass contrast; a size pass across the tool is not cheap or clearly right here.

#### Exit check (2026-11-06)

Cold exit check by Claude on the current bundle (232,975 bytes). Fresh audit: `S:/CurioClass-codex-scratch/flipbook-studio/exit/audit-r2/`
(Chrome 9731, host 8914, exit 0). Own frames and logs: `S:/CurioClass-codex-scratch/flipbook-studio/exit/frames/` and
`exit/x*.json` (shots in `exit/shots.json`, real held clicks at 1366x768 unless named).

##### Should fix
1. FIXED. Even bounce, drawing 5 selected, Time, playing, three held `+` taps 0.4 s apart: holds became
   `[1,1,1,1,4,1,1,1,1,1,1,1]` while the playing index was elsewhere (11). The readout sampled every 50 ms read only
   "Drawing 5: x1" to "x4", no flicker to other drawings (`x1-plus-playing.png`, `x1.json`). Hold the key then `-` while
   playing on Real bounce drawing 3 changed only drawing 3 (`x1b.json`). A real handle drag on drawing 4 still sets 5.
2. FIXED. On twos at 12 shows "On twos at 12 per second: 6 new drawings a second. Tap 24 to see film's twos." (`x2.json`).
   Why note has the "At 12 per second ... tap 24, then On twos" sentence (`x2-why.png`, src.html:476-479); notes.md
   5-minute start says tap 24 first. Starters stay at 12.
3. FIXED. setItem throwing, five held actions 2.5 s apart (hold, hold, Copy page, hold, hold): tooBig spoken once; after a
   good save and a new failure, once more (`x3.json`). Footer warning stays.
4. FIXED. Real Print path (headless Chrome): "printed" logged as spoken, printing false after, hint the same words
   (`x4.json`). `finishPrint()` no longer hushes; print waits for the line when Sound is on.
5. FIXED. Real bounce from the Starters dialog: hint and spoken line are both the starterBounce sentence with the compare
   step (`x5.json`).
6. FIXED. Card reads "tap On twos, then give the top drawings 1 frame and the floor drawings 4." After On twos every hold is
   2, so 1 and 4 are both reachable; tops (y 140) are drawings 1 and 7, floors (y 632) 4 and 10 (`x6.json`). notes.md matches.
7. FIXED. Why defines key drawings; "Plan a jump" card present in bundle and notes.md, with the Williams source.
8. FIXED. Playing hints: Draw "Tap Stop to draw." with cursor not-allowed; Time "Drag a hold handle or tap a preset ...";
   Flip keeps its line (`x8a/b/c.json`).
9. FIXED. `#empty span` color #6b6258 (src.html:111).

Fixed: 9 of 9 should-fix. Polish spot-checked in bulk: 10 (Flip slim numbered strip, page fills the stage,
`r-1920-flip.png`), 11 (empty hint src.html:568), 12 (one ringed dot plus caption, `r-blink-time.png`), 13 (ease hint
src.html:1244), 15 (Undo beside Tools at 680x425, `r-compact-680.png`), 16 (Blue pencil #3b3da8), 20, 22 (`Math.ceil` on
track tap), 23 (canvas label) all present. 14, 17, 18, 19, 21 taken on polish.md's evidence and a notes.md read; not re-measured.

##### Regressions
None found. Default screen, Time (playing and Blink), Flip at 1920x1080 and the 680x425 compact layout look right; no
console errors in any of 16 driven shots or the audit.

##### Gate
1. Done when: the checks tied to the fixes pass (readout arithmetic, holds 1 to 6, Flip page size, print); nothing else
   changed since round 1 lenses passed them. Pass.
2. Codes: MA:Cr2.1.6-8 now has a planning card and key drawings taught; Cr3.1 and Pr5.1 unchanged. Pass.
3. Solo defaults: starters, hints and the bowling card all lead to a doable next move. Pass.
4. Sensitivity: not required (no lens found a sensitive topic). Pass.
5. No blocker or should-fix open. Pass.
6. Bundle: 232,975 bytes (under 2 MB), no console errors, no external URLs or fetch in the bundle, no em dashes. Pass.
7. Voice: the 12-line set unchanged; tooBig once per failure run, printed and starterBounce heard once each. Pass.

#### Audit pilot
- Leads: 32, the same set as round 1's audit. Confirmed none as defects: 8 "1 seconds" (reads "0.1 seconds"/"1.0 seconds",
  settled), 4 sideways film strip (by spec), 10 modal keep-region (Starters and Why dialogs), 10 welcome-after-first-tap
  (settled stale-welcome rule; Time and Flip on a blank book now hint Draw or Starters by item 11).
- Leads wrong: all 32, as above.
- Missed: the audit cannot see items 1, 3 and 4 (selection while playing, repeated tooBig, print speech); they needed
  targeted drives. It also reports no network column, so the network check here is a bundle read.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: flipbook-studio (round 1)

Cold Craft lens, 2026-11-05. Bundle `tools/flipbook-studio/flipbook-studio.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/flipbook-studio/craft/frames/` (shot files `shotsA..F.json` beside them).
Not a Curiosity (no "(Curiosity No." line), so judged against lesson norms.

#### Contract: passes

- One file, 227,031 bytes (goal 2 MB). Only embedded data: two `data:image/webp` (fb-desk, fb-paper). No `http`
  URL in the bundle except the SVG namespace; no fetch, XHR, WebSocket or import.
- No network requests: `performance.getEntriesByType('resource')` is empty after load (a-default-1366).
- No console errors or exceptions in any of my 25 shots or in the audit.
- Kit used, not re-implemented: `Curio.voice`, `Curio.tone`, `Curio.init`, `Curio.onMotion`, `Curio.reduce`, kit header.
- Play clock: 24 fps on Real bounce for 5.3 s (127 drawings shown, over 10 loops): worst drift 9.7 ms, last -1.0 ms,
  well inside one frame (41.7 ms). rAF frame times median 16.7, p95 16.7, max 16.8 ms (c3-clock24). Done when 5 holds.

#### Access: passes, with one contrast miss

- Every visible control is at least 44 x 44 px at 1366x768 and at 375 wide (a-default-1366, a-default-375x).
- Tab reaches header, then every panel control, then the strip (panel before the long list, as STANDARDS asks). Every
  stop shows a 4 px solid outline (gold in the header, #a52a13 in the panel) (c5-keys).
- Color is never the only signal: onion before is solid, after is dashed; holds show "x3" as text; selected
  thumbnail has a border and `aria-current`; mode and toggle buttons use `aria-pressed`.
- Motion off and Sound: the audit's Motion-off row is clean; the curl and paper-settle check `Curio.reduce`.
- Read: speaks the hint, cuts a playing line, works with Sound off; Sound back on brings the skipped welcome once
  (b8-read-during, b9-read-soundoff).

#### Lines and art: pass

- `voice/lines.json` (12 lines) and `allLines()` (12) match word for word both ways (a-default-1366 check).
- Art tokens `art:fb-desk` and `art:fb-paper` both have prompts.json entries, `people: false`; no people drawn.
- Words: no em dashes in src, bundle, notes, spec or lines; "Curio Class" never "Curio" alone; classroom safe;
  privacy stated on screen twice ("Saved on this device. Your drawings never leave it." and the footer).

#### Standard voice check

Held clicks (0.12 s), Sound on, Motion on, gaps 2 to 3 s; headless Chrome has no system voice, so line lengths are
the kit's cap and some "cut" marks are only the next action arriving (not a finding).

| line | kind | expected in 5 actions | spoken | run |
|---|---|---|---|---|
| welcomeDraw | how | 1 | 1 | b4-modes (5 Draw entries) |
| welcomeTime | how | 1 | 1 | b4-modes |
| welcomeFlip | how | 1 | 1 | b4-modes |
| spacingHow | how | 1 | 1 (then silent x3) | b4-modes |
| onionHow | how | 1 in five pages drawn | 1 (then silent x4) | b1-five-pages (Done when 11) |
| eraserHow | how | 1 | 1 (then silent/dropped) | b5-eraser |
| starterBounce | event | 4 of 4 loads | 4 | c1-starters |
| starterBlink | event | 1 | 1 | c1-starters |
| holdChanged | event | 5 while playing | 5 | b2-hold-playing (Done when 11) |
| printed | event | 1 | **0 (dropped, hush)** | b7-print |
| tooBig | event | once per failure, but see finding 2 | 5 in 5 actions | f1-toobig |

Stale lines (c2-stale, 10 actions 0.6 s apart through Starters, Time, Play, hold +, Flip, Stop, Draw, New book):
no line played after its moment; welcomeFlip was dropped as stale while the book played and spoken after Stop; order
followed the actions. Read during welcomeTime cut it and spoke the hint at once. First-tap rows: the audit's table
covers them; I did not re-shoot. welcomeFlipCompact (compact Flip) was not exercised by me.

#### Findings

1. **should fix** (general). `src.html:1416-1424` `printBook()`: the `printed` line ("Print the pages, cut on the
   lines and staple the left edge.") can never be heard. `V.say` only queues (the pump starts in a microtask), then
   `window.print()` blocks the thread, and the `finally { finishPrint() }` runs `V.hush()` synchronously when the
   dialog closes, before the queued line can start. Seen: b7-print log `printed dropped hush`. In headless print
   returns at once; in desktop Chrome the order is the same, so the spoken how-to-make-the-paper-book is lost every
   time (the hint still shows it). Better: speak it before opening print (await the line, or `setTimeout` the print
   call after it starts), or speak it after `afterprint` as the next step.
2. **should fix** (general). `src.html:557-564` `save()` catch: when storage is unavailable or full, `tooBig` is
   queued as an event on every change, so each stroke, Copy page or hold change says "This book is too big to save
   here..." again. f1-toobig (setItem throwing, five actions 2.5 s apart): spoken 5 times, twice within 170 ms at one
   point, and the onionHow lesson was pushed out (dropped) both times it came up. It is a standing condition, not a
   new event: say it once per failure run (speak again only after a save has worked and then fails again). Students on
   locked-down school browsers where localStorage throws would hear it on every mark.
3. **should fix** (general). Empty-state line "Draw here, or open a starter book." (`#empty span`, `src.html:91-94`)
   is #84786a on the #fbf6ea page at 12 px: 3.99:1, under AA 4.5:1 (recomputed in Python; the paper texture lowers it
   a little more). Frame a-default-1366. Darken to the spec's muted #6b6258 (5.54:1).
4. **polish** (family:drawing). Pencil colors collide with the tool's own overlays: `Blue pencil` is #2f6fd6, exactly
   the onion "before" ghost color, and `Red` is #c8341a, exactly the spacing chart's dots and line. Frames
   e1-blue-pencil-onion (a full-strength blue stroke beside 35% blue ghosts reads as one more ghost) and
   e2-red-pencil-chart (a red stroke on drawing 1 sits in the chart's color). Better: shift Blue pencil to a cyan or
   indigo distinct from the ghost, and draw the chart in a color no pencil uses (or outline its dots).
5. **polish** (general). Heavy books get slow: `changed()` calls `render()`, which repaints all 48 thumbnails, and
   `save()` writes the whole book on every stroke end, hold step and reorder. With the spec's limits (48 drawings,
   a 400-stroke page plus 120 strokes on the others) one full render took 67 ms, a reorder 109 ms, and the save was
   3.86 million characters, near Chrome's ~5 MB localStorage quota (d1-heavy, on this fast desktop; a modest
   laptop is several times slower, so a hold drag while playing would stutter). Points are saved at full float
   precision (`position()` in `src.html:1305-1308`). Better: repaint only the changed page's thumbnail, round points
   to 0.1 unit, and debounce the save during a drag. Normal classroom books (a dozen pages, a few strokes each) are
   unaffected: playback held 16.7 ms frames.
6. **nit** (general). `src.html:1331-1334`: the eraser pushes an undo step on every press even when it touches no
   stroke, so Undo after a missed erase appears to do nothing.
7. **nit** (family:drawing). `src.html:885`: a tap on the hold track uses `Math.round(x/15)`, so tapping the left
   half of cell 3 sets a hold of 2. `Math.ceil` would match the cell tapped (the handle drag is unaffected).
8. **nit** (general). `src.html:369`: the canvas label says "Use arrow keys to step pages", but the canvas is not
   focusable; the arrows do work from the page, so the words are only slightly off.
9. **nit** (general). Several labels are 10 to 11 px (eyebrows, hold captions, page numbers, footer privacy line,
   strip label); all pass contrast, but 10 px is small for a laptop at arm's length.

Nothing cultural, Native or hard-history: no sensitivity review needed.

Counts: blockers 0, should fix 3, polish 2, nits 4.

#### Audit pilot

- Leads confirmed: none of the audit's leads is a real Craft defect.
- Leads wrong: "count and word disagree: 1 seconds" at every size: the readout says "1 drawing, 1 frame, 0.1 seconds
  at 12 per second", which is correct English (the check read "0.1" as "1"). "keep region covered" in
  starter-library and timing-help: those are modal dialogs, covering is expected. "choices cut short by a scroll
  panel" on `#film`: the spec asks for a sideways-scrolling strip and the selected thumbnail is kept in view.
  "Welcome not heard" after New page, Copy page, Delete page, Clear page, Play, Starters, New book: these follow the
  spec's stale rules for welcomeDraw (a page button counts as starting) and the welcome returns after Stop or a closed
  dialog; whether the premise should still be spoken is the Play lens's call, not a voice bug.
- What it missed: the `printed` line that can never play (finding 1), `tooBig` repeating on every action (2), the
  empty-state contrast (3), pencil colors that match the onion and chart colors (4), and cost on a large book (5).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: flipbook-studio (round 1)

Played twice: as a grade 7 student alone at home (blank book first, then the starters), and as a teacher projecting
at 1366x768 and 1920x1080. Frames are in `S:/CurioClass-codex-scratch/flipbook-studio/play/out/` (mine) and
`S:/CurioClass-codex-scratch/flipbook-studio/audit-r1/` (shared audit). Driven with `scripts/drive.py`, held clicks
(0.12 s), real drags on the page and on the hold handles.

What works well: the first screen invites a mark ("A little mark. A little motion."), the onion ghost arrives with
its own line right after New page or Copy page (d1-drawn-new, d2-copy: welcomeDraw dropped at the first stroke,
onionHow spoken once), the Real bounce spacing chart reads at a glance (state-bounce-time-1366x768), a hold drag while
the book loops changes timing at once and speaks holdChanged (t3-drag-while-playing), Ping-pong turns at both ends
without a doubled end drawing (t6-ping: 11,10 ... 1,0,1), and 24 per second keeps time (t5-24fps: 123 frames in
5115.6 ms against 5125 ms expected, under one frame). Print repeats held drawings (p1-print: Blink prints 11 cards,
8 + 1 + 1 + 1, numbered, staple margin, no paper texture).

#### Findings

1. **Time mode, `-` / `+` and `Hold the key` while playing (src.html:1504-1505, 1146; `page()` follows the playing
   drawing).** While the book loops, the selected drawing is whichever one is on screen, so `+` changes a drawing
   picked by chance, and the `×N` readout between the buttons flickers with every drawing. Three `+` taps 2.5 s apart
   on Even bounce raised drawings 2, 8 and 12 (holds `1,2,1,1,1,1,1,2,1,1,1,2`), none of them chosen. `Hold the key`
   has the same problem. The spec says everything stays live while playing, and the handles do, but these two
   controls become a lottery, and they are the keyboard path to holds. Better: while playing, `-`, `+` and `Hold the
   key` act on the drawing the student last selected (keep a separate selection from the playing index), or name the
   drawing on the button area ("Drawing 5: ×1"). Seen: t9-hold-plus-playing.png and its log. **should fix**,
   general.

2. **Starter loaded: the hint and the spoken line say different things (src.html:1028-1029).** After Real bounce the
   voice says "Press Play, then load the other bounce from Starters and compare." The hint says "Tap Play to watch.
   Tap Time, then drag the hold handles." Read speaks the hint, so the Real versus Even comparison (the tool's core
   contrast) is never on screen, and a student with Sound off never meets it. Better: one sentence shown and spoken,
   and the compare step kept (for example the spoken line as the hint, with Time named after the compare). Seen:
   s1-starter-real-hint log (starterBounce spoken, hint differs). **should fix**, general (anything shown twice
   matches).

3. **Hint while playing names the mode you are in (src.html:528).** In Time, pressing Play sets the hint to "Drag a
   hold handle or tap Time to change the feel." Time is already pressed. Words should match the state: in Time,
   "Drag a hold handle or tap a preset to change the feel. Tap Stop to pause."; in Draw and Flip the current line
   fits. Seen: t4-time-playing-hint. **should fix**, general.

4. **Flip has no focus of its own (spec, Screens and modes: "the page fills the stage").** Flip lays out exactly like
   Draw: same page size, same strip at the same height, only the panel buttons change (state-mode-flip-1366x768,
   f1-flip-playing, state-live-flip-1920x1080). The spec's Flip is "the page alone, as big as the stage allows", the
   watching moment. Done when 6 still passes (the page is the biggest thing), so this is a missed moment, not a
   break. Better: in Flip shrink the strip to a slim progress row (numbers and the playing marker) and give the page
   the height. **polish**, family:none (this tool).

5. **Empty book: Time and Flip invite Play on nothing (src.html:538-541).** A student who opens Flip or Time first on
   the blank book is told "Press Play to flip the book" or "Drag a hold handle ... Then press Play"; Play runs a
   single blank page with ticks, then the playing hint asks them to drag a hold handle (f2-empty-flip, f3-empty-time).
   Better: when no drawing has strokes, the hint in Time and Flip says "Draw on the page in Draw, or tap Starters for a
   ready-made book." **polish**, general.

6. **A first tap on New page, Copy page, Delete page or Clear page on the blank page gets no line (audit lead,
   confirmed in code: insertPage and the delete/clear handlers set `drawTouched`, so `welcomeValid` fails, and with a
   blank previous page there is no onionHow).** The hint still shows welcomeDraw, so the screen is right; only the
   spoken premise is lost for a student who starts on a button. Mild; Draw is mostly entered by drawing. **polish**,
   general.

7. **Try this, card 1 has no first move with the hold controls (why dialog, "fewer frames at the top").** Real
   bounce is already all on ones, so the hold handles cannot give the top fewer frames; the student must think of On
   twos first, or delete drawings. A grade 7 student alone tried the handles, hit 1, and stops. Better: "Start on
   twos, then give the top drawings 1 frame and the floor drawing 4." Also each card could carry a "Load Real bounce"
   style button; now the student must close the dialog, open Starters and confirm the replace. Seen:
   state-timing-help-1366x768. **polish**, family:none.

8. **Projected, the numbers that teach are the smallest text (readout 12 px, hint 13 px at every size).** At
   1920x1080 the readout "12 drawings, 12 frames, 1.0 seconds at 12 per second" is the line a teacher points at, and
   it is 12 px under a 1600 px stage (state-live-flip-1920x1080). Better: scale `#readout` and `#hint` up on large
   windows (about 16 px at 1920). **polish**, general.

9. **Compact sizes: the lone `Tools` / `Timing` / `Options` button is a half-width cell beside empty space, and
   Undo hides inside it (680x425, 800x500).** Undo is a control a drawer uses every few seconds; at the preview size
   it is two taps away (size-680x425, state-mode-flip-680x425, state-bounce-time-680x425). Better: put Undo next to
   Tools on that row (the space is there). **polish**, general.

10. **Drawing while the book plays does nothing and says nothing.** In Draw with Play on, the cursor stays a
    crosshair and a stroke is silently ignored (src.html:1320); the hint talks about holds. Better: a not-allowed
    cursor while playing, or the hint "Tap Stop to draw." **nit**, general.

Nothing found on: the default screen at every size, every mode button, the extremes (hold ×6, hold ×1, 6 and 24 per
second, 48 drawings, Blink's ×8 starter hold with its "starter" label), Motion off, the starter library, Ping-pong,
Step and Back, the onion legend (solid before, dashed after reads without color).

#### Audit pilot

- **Confirmed:** welcome not heard after a first tap on New page, Copy page, Delete page, Clear page and Play
  (finding 6; Play on a blank book is finding 5). Eraser "not heard" is fine: it speaks its own line. Starters and New
  book "cut (hush)" are fine: they open a dialog, and the starter line follows.
- **Wrong:** "count and word disagree: 1 seconds" matched inside "0.1 seconds"; the readout's plural is right.
  "Choices cut short by a scroll panel" on `#film` is the drawing strip, which scrolls sideways by design (spec) and
  keeps the selected tile in view; it is not a short choice set. The keep-region leads on starter-library and
  timing-help are the modal dialogs covering the page, as expected.
- **Missed:** `-`, `+` and Hold the key hitting whichever drawing is playing (finding 1, the worst); the starter hint
  and spoken line disagreeing (2); "tap Time" shown while in Time (3); Flip with no layout of its own (4); empty-book
  Play (5); the Try this card with no first move (7). None of these is mechanical: each needs a run with a goal in
  mind.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: flipbook-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, audit-states.json and the shared audit
(`S:/CurioClass-codex-scratch/flipbook-studio/audit-r1`). Checks ran through `scripts/drive.py` (port 9831), shots and
frames in `S:/CurioClass-codex-scratch/flipbook-studio/teaching/` (`shots.json`, `frames/`). No console errors in any
shot. Not a Curiosity: judged as a lesson tool.

#### Findings

##### 1. On ones and on twos are taught at film's 24 per second, but the tool runs at 12 by default
- Where: src.html:457-460 (Why notes), preset `twos` (src.html:1144), notes.md "A 5-minute start".
- What: the Why card says twos "still look smooth for most motion" and ties twos to 24 per second. Every starter
  plays at 12 per second, so On twos here gives 6 new drawings a second: the Real bounce just plays in slow motion,
  choppy (frame t9: "12 drawings, 24 frames, 2.0 seconds at 12 per second"). A student who presses On twos sees the
  opposite of what the card says, and the 5-minute start then asks "what feels heavier now?" about a change that only
  halves the speed. At this tool's 12 per second, its "ones" already equal film's twos. The only screen hedge is
  "This book's frame rate can be different"; notes.md says it plainly ("at this tool's default 12 fps it produces 6
  drawings per second"), but the student never sees that.
- Better: say it where the student acts. For example, the Why note: "At 12 per second, this book on ones already looks
  like film on twos. To see film's twos, tap 24, then On twos." and a hint after On twos at 12 or less naming the
  drawings per second. If the integrator prefers, starting the bounce starters at 24 per second on twos would make
  the vocabulary true by default, but that changes the spec's Content (open question, not builder work).
- How seen: frame `teaching/frames/t9-twos-12.png`; Why text in `audit-r1/state-timing-help-1366x768.png`; preset
  readouts recomputed below.
- Level: should fix. Tag: general (a named technique taught under a different rate than the one on screen).

##### 2. MA:Cr2.1.6-8 is only lightly taught: nothing asks the student to plan or propose
- Where: spec "Who and how" glosses Cr2.1 as "develop, refine and model"; the standard's text is "Organize (gr 6) /
  Design (gr 7-8), propose, and evaluate artistic ideas, plans, prototypes, and production processes for media arts
  productions, considering expressive intent". notes.md "Sources and standards".
- What: the tool has organizing (reorder pages, Copy page) and evaluating (compare Real and Even bounce), but no step
  where the student plans a motion before drawing it. Animation's own planning process, keys then in-betweens, is
  absent: "Hold the key" (src.html:341) uses the word key without the tool ever saying what a key drawing is.
- Better: one real planning activity, not a thin one. For example a Try this card, with a matching line in notes,
  "Plan a jump: draw the start, the top and the landing first (your keys), then add the drawings in between with onion
  skin, closer together near the top." and one Why sentence defining a key drawing (Williams, Survival Kit, "Keys,
  extremes and breakdowns"). Then "Hold the key" means something. If the integrator judges that out of scope, move
  Cr2.1 to the tool that plans (storyboard-studio is 9-12, so it needs a 6-8 home) per BASELINE rule 2.
- How seen: code read of every control and card; standard text from the NCAS-based grade 6-8 listing.
- Level: should fix. Tag: general.

##### 3. The bowling ball card asks for a move the hold controls cannot make
- Where: src.html:466, "fewer frames at the top, longer hold on the floor".
- What: every Real bounce hold starts at 1, the minimum, so "fewer frames at the top" cannot be done with the hold
  handles the card sits beside. A solo student tries minus on a top drawing, gets "This hold is already 1 frame", and
  is stuck. The only way is Delete page in Draw, which the card does not name.
- Better: "Make the Real bounce feel like a bowling ball: hold the floor drawings longer, then delete one top drawing
  in Draw so it hangs less in the air." (or start the card from On twos so tops can drop to 1).
- How seen: tried it (changeHold to 0 on a hold-1 drawing returns the "already 1 frame" hint, src.html:1119-1124).
- Level: should fix. Tag: family:flipbook (hold-only editing).

##### 4. Intent prompts are hidden behind Why / Try this; a solo student never meets one
- Where: starter lines and hints (src.html:1028, voice `starterBlink`), Try this cards inside the Why dialog; at
  heights under 650 px the Why button moves into the Timing dialog (secondary rows).
- What: Cr3.1 is "refine for intent". The Blink starter's line says "drag the hold handles and press Play" with no
  intent to aim for, though its card says "calm or startled?". The bounce line does set a compare task (good). A
  student at home reaches an intent only if they open Why / Try this.
- Better: give the Blink starter a goal in its hint, e.g. "Here is a calm blink. Tap Time, drag the first hold down
  to 2 and press Play: now it is nervous." and show one Try this card under the presets in Time at sizes where it fits.
- How seen: `teaching/frames/t7-blink-time.png`, hint text returned by the shot.
- Level: polish. Tag: general.

##### 5. Spacing chart on the Blink shows one red dot on the nose
- Where: drawChart (src.html:650), Blink starter in Time.
- What: the four blink drawings share one bounding-box center, so the chart draws a single dot with four crowded
  numbers between the eyes. It is accurate (the face does not travel) but reads as a stray mark, and the real lesson
  (a blink is all timing, no travel) is not said.
- Better: when every dot coincides, draw one dot and a caption line such as "These drawings do not travel: the change
  is in shape, so timing does all the work."
- How seen: `teaching/frames/t7-blink-time.png`; centers recomputed: all four [480, 350].
- Level: polish. Tag: family:flipbook.

##### 6. Ease the ends on a looping bounce slows only one of its two tops
- Where: preset `ease` (src.html:1145), spec Content.
- What: holds become 3,2,1,...,1,2,3 by position in the book. Real bounce has tops at drawings 1 and 7; drawing 1 gets
  3 frames, drawing 7 gets 1, so the two bounces get different hang times. A student may take this as what slow in and
  slow out means for a bounce.
- Better: the hint after the preset says what it did: "Ease the ends slowed the first and last drawings of the book.
  For a bounce, hold each top drawing longer by hand." (no spec change).
- How seen: readout "12 drawings, 18 frames, 1.5 seconds" with holds 3,2,1,1,1,1,1,1,1,1,2,3 (shot t1).
- Level: polish. Tag: family:flipbook.

##### 7. Teacher notes say "the spec"
- Where: notes.md "Good to know": "The Blink starter retains the spec's explicit 8-frame first hold until edited".
- What: internal build jargon in teacher-facing notes; a teacher does not know what "the spec" is.
- Better: "The Blink starter opens with an 8-frame hold on its first drawing (a calm blink). Editing it switches to the
  1 to 6 frame range."
- Level: polish. Tag: general.

##### 8. Support at home: the rolled ball does not start slow
- Where: notes.md "Support at home", third idea.
- What: a gently rolled ball leaves the hand at its fastest and slows down; "starts slow, moves quickly and stops" is
  not what a family will see, and it does not match either starter.
- Better: "Drop a ball and let it bounce. Watch where it seems to hang at the top and where it rushes at the floor,
  then compare with Real bounce." (matches the tool and can be done tonight).
- Level: polish. Tag: general.

##### 9. "twos are half the drawing"
- Where: src.html:459.
- What: should be "half the drawings" (spec has the same slip).
- Level: nit. Tag: general.

#### Done when (tested)

| # | Result | How |
|---|---|---|
| 1 | pass (code) | eraser filters whole strokes by isPointInStroke; remember() before each stroke and erase, per page, 50 steps. Touch not driven here (Play/Craft) |
| 2 | pass (code) | onion only when mode is draw and not playing (src.html:723); print builds from strokes only |
| 3 | pass | shot t1: "12 drawings, 12 frames, 1.0 seconds"; twos "24 frames, 2.0 seconds"; Blink "4 drawings, 11 frames, 0.9 seconds" (11/12 = 0.917) |
| 4 | pass | centers recomputed: Real (150,204) (220,380) (290,632 squashed, bottom 660, width 104 = 1.3 x 80) (360,380); Even (150,300) (220,460) (290,620) (360,460). Chart bunched vs even: `audit-r1/state-bounce-time-1366x768.png`, `teaching/frames/t8-even-time.png` |
| 5 | pass | strokes identical after two hold changes, a preset and 24 fps (t1); 24 fps, 10 loops of 0.5 s: loop starts 510 to 5010 ms, at most 1 ms off ideal (t2) |
| 6 | pass (audit) | audit clean rows for every size and mode; keep-region leads only inside modal dialogs |
| 7 | pass | hold set to 6 on the drawing on screen while looping: next drawing came 517 ms later (500 expected) (t3); stop cancels the frame loop at once |
| 8 | pass | Real bounce on twos prints 24 numbered cards on 3 sheets; dashed cut borders, STAPLE margin, plain white, no paper texture |
| 9 | pass | Blink with hold edit survived a fresh tab (t5, t6: holds 8,3,1,1); setItem throwing shows the footer warning with the exact line (t4) |
| 10 | pass (audit) | page, strip and Play in view at every size |
| 11 | left to Craft | voice counts are the Craft lens's check |

Numbers recomputed: Ease the ends 3+2+8x1+2+3 = 18 frames, 1.5 s; 48 drawings held 6 = 288 frames = 48.0 s at 6,
12.0 s at 24, 36 sheets; Blink opener 8 + 47 x 6 = 290 frames, 37 sheets (notes.md matches). |cos| bounce vs a true
parabola: 204 vs 193.3, 380 vs 353.3 (within 27, as the spec says).

#### Other checks
- Giveaways: no predict, quiz or hidden-information mode; nothing to give away.
- Facts: 24 frames per second as a common film rate, ones and twos, slow in and slow out, timing and spacing match the
  spec's Sources (Williams 2001; Thomas and Johnston 1981, ch. 3). Both Animation Mentor links in notes.md exist (the
  site refuses automated fetches; found by search).
- Guardrails: grade 6-8, students drive; no hard history, health or cultural content. Nothing for the sensitivity
  agent. Rule 8: the media arts standards here cover no sensitive topic.
- Language: plain and right for grade 6-8, apart from items 7 and 9.

#### Audit pilot
- Leads wrong: "count and word disagree: 1 seconds" at every size is the substring of "0.1 seconds" (1 frame / 12 =
  0.083, shown as 0.1). Not a bug. The starter-library and timing-help keep-region leads come from modal dialogs the
  states open on purpose (their `keep` is [] yet the audit still checked the global list).
- Leads confirmed: the film strip scrolls sideways in bounce-time, delete-pauses-book and page-limit; that is the
  spec's own design (one row that scrolls), not a teaching problem.
- Missed (outside its reach): items 1 to 9 above, chiefly the ones/twos rate mismatch and the untaught planning
  standard.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: flipbook-studio (Codex fix, round 1)

Evidence paths below are relative to `_scratch/flipbook-studio/`. Every should-fix was reproduced before editing at 1366x768 with `scripts/drive.py`. Before frames: `fix-before/s01-*` through `s09-*`. Accepted polish used after frames and measurements. The final report is written only after checking, honoring the user's stop trigger; this draft was maintained in Scratch during work.

#### Blocker

None in refine.md.

#### Should fix

1. FIXED. Playback and student selection now have separate indexes. The baseline reproduction used Real bounce with the same twelve x1 holds; the reviewer used Even bounce. Both use the same timing controls and playback path. Three live plus taps changed only selected drawing 5 from x1 to x4, with a stable named readout; before they changed drawings 4, 6 and 11. `fix-before/s01-selected-live.png`, `fix-after/s01-selected-live.png`. Additional live minus and Hold the key tests changed only drawing 7 and drawing 5 respectively: `fix-functional/check-selection-minus.png`, `check-selection-key.png` and matching JSON.
2. FIXED. Why and the 5-minute start distinguish film's 24 fps twos from the starter's 12 fps twos. The preset hint explicitly says 6 new drawings per second at 12, and names 24 as the next action. Starters remain 12 fps. `fix-before/s02-twos.png`, `fix-after/s02-twos.png`, `fix-after/s07-planning.png`, `fix-voice/read-twos.png`; 24 displayed duration combinations checked in `check-numbers-sweep.json`.
3. FIXED. Warning speech is triggered only on transition into failed storage, and rearms after a successful save. Baseline: 5 spoken starts for 5 failed saves. After: 1 for the same five-copy sequence, with the persistent warning still visible. A separate five-action run, success, then new failure produced exactly 2 warning starts, one per failure run: `fix-target/check-storage-recovery.png`, `check-storage-recovery.json`. No repeated warning displaced onion guidance in the after-copy run.
4. FIXED. Print now awaits its narration before opening print, and Sound off prints without a speech delay. Baseline `printed` was dropped by hush; the real headless print path now logs one spoken `printed` and `printing:false`: `fix-last/print-real.png`, `print-real.json`. The hint is the same sentence. A simulated afterprint-only approach was rejected because real headless Chrome did not emit afterprint. Physical printer output was not tested.
5. FIXED. Bounce starters use the exact starterBounce sentence for both hint and speech, preserving the comparison instruction. `fix-before/s05-starter.png`, `fix-after/s05-starter.png`; the held-click log in `before-starter.json` now contains the matching after-state sentence. The file name predates the recheck; the baseline mismatch is preserved in the before frame and progress notes.
6. FIXED. The bowling card and notes now begin with On twos, then prescribe top=1 and floor=4. Applying it gave holds `[1,2,2,4,2,2,1,2,2,4,2,2]`, 26 frames, and identical artwork. `fix-before/s06-bowling.png`, `fix-after/s06-bowling.png`, `fix-functional/check-bowling.png`, `check-bowling.json`.
7. FIXED. Why defines key drawings and the new optional card plans start, top and landing before in-betweens; the same activity and Richard Williams source are in notes. `fix-before/s07-planning.png`, `fix-after/s07-planning.png`, `fix-target/s07-plan-card.png`. Source: Richard Williams, The Animator's Survival Kit (2001), "Keys, extremes and breakdowns", as named in the Refine item. No additional scored planning gate was added.
8. FIXED. Playing hints now follow Draw, Time and Flip. Draw says Tap Stop to draw and uses a not-allowed cursor. Time names hold handles and presets. `fix-before/s08-playing-draw.png`, `s08-playing-time.png`, their matching `fix-after/` frames and computed cursor `not-allowed`.
9. FIXED. Empty-state text uses #6b6258. Contrast rose from 3.994:1 to 5.543:1 on #fbf6ea, independently computed in `fix-numbers.json`. `fix-before/s09-contrast.png`, `fix-after/s09-contrast.png`.

#### Polish accepted

10. FIXED. Flip uses a 55 px strip with 44 px numbered buttons, selected border and separate playing underline. At 1366x768 the page is 650.4 by 487.8 px, versus Draw's 634.5 by 475.9. `fix-target/p10-flip.png`, `p10-flip.json`. All three modes passed at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x760 and the 375x812 iframe. Page, strip, Play and hint are in bounds, with document scroll [0,0], in all 25 measured states: `fix-validation.json`, `fix-sizes/`, `fix-phone/`. Frames were inspected individually or on contact sheets.
11. FIXED. Empty Time and Flip now direct the student to Draw or Starters; their invalid Play welcomes are suppressed. `fix-polish/p11-empty-time.png`, `p11-empty-flip.png` and matching JSON.
12. FIXED. Blink's four centers are all `[480,350]`; the chart draws one ringed dot and shows the shape-change explanation. `fix-polish/p12-blink.png`, `p12-blink.json`.
13. FIXED. Ease the ends explicitly describes the first and last drawings and asks for manual holds at each bounce top. Holds remain `[3,2,1,1,1,1,1,1,1,1,2,3]`. `fix-polish/p13-ease.png`, `p13-ease.json`.
14. FIXED. At 1920x1080, both readout and hint compute to 16.128 px. `fix-polish/p14-large.png`, `p14-large.json`.
15. FIXED. Compact Undo is beside Tools, with a 44 px height at both 680x425 and 800x500. The 680 undo action removed the newly added stroke and exposed one Redo step. `fix-polish/p15-undo-680.png`, `p15-undo-800.png`, `fix-functional/check-undo-visible.png` and matching JSON.
16. FIXED. New Blue pencil is indigo #3b3da8, 8.050:1 on the page. Previous-page onion remains blue. Chart dots remain vermilion and have a light outline ring. Old blue strokes still load unchanged. `fix-polish/p16-blue-onion.png`, `p16-red-chart.png`, `fix-numbers.json`.
17. FIXED. Artwork edits repaint one thumbnail; holds and fps repaint none. Reorders reuse existing canvases. Input and legacy points round to 0.1 drawing unit. A 48-page, 400-stroke-per-page legacy book loaded in full and saved from 4,350,113 to 2,078,073 characters. Ten steady renders measured 0.1-0.7 ms; reorder 12.4 ms; an artwork change cleared only `thumb-2`. A real hold drag with 18 samples now saves once on release. `heavy-seed.json`, `heavy-measure.json`, `drag-save.json`, `fix-target/heavy-measure.png`, `fix-last/drag-save.png`. Measurements are this machine, not a universal speed guarantee.
18. FIXED. Good to know now describes the calm Blink opener and the 1 to 6 editor directly, with no reference to "the spec". Verified in notes.md.
19. FIXED. Support at home now asks families to drop and bounce a ball, observe the hang at the top and rush at the floor, then compare with Real bounce. Verified in notes.md.
20. FIXED. Why says "half the drawings". `fix-after/s07-planning.png`.
21. FIXED. A missed erase leaves undo length 0 rather than adding an empty step. `fix-polish/p21-missed-erase.png`, `p21-missed-erase.json`. A sampled real erase then Undo gave removed=0 strokes, undo=1, restored=1 stroke (`erase-hit-undo.json`, `fix-final-targets/erase-hit-undo.png`).
22. FIXED. A real tap in the second track cell now selects hold 2; handle dragging still uses its existing rounding. `fix-last/p22-track-cell.png`, `p22-track-cell.json`. Earlier synthetic drags hit the handle or sent a move after the tap; those intermediate checks are retained and are not the passing evidence.
23. FIXED. The canvas label now says "Arrow keys Left and Right step pages" without promising canvas focus. Keyboard Step twice already reached drawing 3 with focus retained and no document scroll (`keyboard-flip.json`). Two actual ArrowRight keys also reached drawing 3; the returned label matches the revised wording (`arrows-final.json`, `fix-finish/arrows-final.png`).

#### Settled calls

- Applied: retained the permitted first-tap welcome behavior for page operations, modal keep-region behavior, horizontal scrolling film strip and decimal seconds wording.
- Applied: used the timing-only bowling recipe, preserved 12 fps starters, moved Blue pencil rather than the accent chart.
- Retained the 12-line voice manifest, Ping-pong's no-double-end implementation, clock, held-frame print construction, Motion off and Read. `fix-numbers.json` confirms all 12 manifest lines equal the source table. A 120-frame/10-loop clock check at 24 fps took 5022.7 ms, error 0.545 frame (`check-24-clock.json`); no clock code changed.
- Left the spec's two open questions and Not taken items alone.

#### Cheats tried

- Repeated live plus taps: only the selected drawing changed. Two additional patterns, live minus after On twos and live Hold the key, also changed only the selected drawing.
- Swept all 6 editable hold values against all 4 frame rates in deliberately scrambled hold order: all 24 frame/seconds totals agreed with independent arithmetic. No score, meter award, quiz, correctness badge or completion gate exists (`awards:0`). Presets are creative timing controls, not evidence of a learned skill.
- Applied the bowling recipe without redrawing: it changes timing only, with no automatic pass claim. Planning remains an optional making activity, not a gate that can be passed by clicking every choice.
- Repeated failed saves with both page copies and hold increments, then recovered and failed again: warnings speak once per continuous failure; visible warning persists until recovery.
- Track tap and hold drag: second cell gives 2; drag reaches 6 and saves once. Held prints still construct 24 cards on 3 sheets from 12 drawings on twos (`check-print-held.json`).

#### Voice walk

Held clicks were 0.12 s with a 2 s pace, Sound on; Chrome was muted as required. Logs record spoken starts, not a human listening session. No recordings were made or regenerated.

- Main walk in `voice-main.json`: welcomeDraw, onionHow, welcomeTime, spacingHow, holdChanged, welcomeFlip, printed, each once. The final drawn-book walk (`voice-main-drawn.json`) started onionHow, welcomeTime, holdChanged, welcomeFlip and printed once each, in that order. The first drawing made welcomeDraw stale, as permitted. At the 2 s pace, later actions cut several long how lines; printed completed without a cut. Only one drawing had strokes, so spacingHow correctly had no three-dot trigger on this path.
- Starter comparison walk: starterBounce once, with exactly matching hint (`fix-after/s05-starter.png`).
- Storage walk: tooBig once across five failed actions, then once more after successful recovery and a fresh failure (`check-storage-recovery.json`).
- Side walk in `voice-side.json`: starterBlink, welcomeTime, welcomeDraw, then Read speaks eraserHow. The fast Why entry drops stale spacing speech; Read correctly replaces a pending eraser line. These unrelated cuts are retained honestly, not presented as full uninterrupted clips.
- Final real print recheck: printed starts once before print and finishes without a hush cut (`print-real.json`).

#### Visual and play regression

Best moment: changing a live hold changes the feel while the same ball drawings keep moving. The two flat moments addressed were Flip repeating Draw's layout and the bowling card leading into a minimum-hold dead end; Flip now has the slim progress row and the card has an achievable first move. The painted table, paper grain, onion guides and responsive hold bars are retained. Compared the final desk with the existing bar-tool bundles at the same 1366x768 size: `fix-last/print-real.png`, `bar-beat-lab.png`, `bar-snowy-mail-route.png` and `fix-last-sheet-0.png`. Their existing bundles were read without writing to either tool. The desk remains detailed and does not look plainer. Grayscale, Motion off, keyboard Step and direct arrows were inspected in `fix-finish/` and `fix-voice/`.

Final bundle: 232,975 bytes, no external load URLs, no source em dashes. `fix-validation.json` records the SHA-256. Targeted drive runs had no product console errors. The generated phone host initially requested a missing favicon; a data favicon in that temporary test host removed the 404 in `fix-phone-clean/`. The host was removed and its server closed.

#### Engine changes wanted

None. All fixes are tool-local.

#### Audit

Completed once, last, within the 40 minute limit, using Chrome 9911 and host 8715. Exit code 0. Report: `fix-audit/audit.md`. The audit's copied bundle and the delivered bundle have the same SHA-256. No product console errors, focus failures or resize exceptions were reported. Motion off passed. Nine controls passed five held clicks, and eleven passed the quick-tap check.

All 32 leads are accounted for:

- Eight size leads, "1 seconds": the visible text is "0.1 seconds". This is the explicitly settled decimal-parsing false positive. The default frame and readout measurements confirm it.
- Four sideways-strip leads: bounce-time at 680x425 and 1366x768, delete-pauses-book, and page-limit. These are the specified horizontally scrolling film strip. Selected drawings and main controls stay in view; do not flatten the strip or remove drawings to silence this flag.
- Ten modal keep-region leads: Starters and Why each cover #page, #play, #readout and #hint, plus a duplicate #page entry quoting the new chart caption. These are the settled intentional modal overlays, also visible in our own `fix-before/s07-planning.png` and `fix-after/s07-planning.png`. The extra caption wording does not change the cause. No desk control is meant to be used through a modal.
- Ten first-tap welcome leads: #m-time and #m-flip on a blank book intentionally suppress an invitation to Play nothing (item 11); #eraser speaks its own eraserHow instead of welcomeDraw, confirmed in the audit's spoken column and repeat check; #new-page, #copy-page, #delete-page and #clear-page follow the explicitly settled stale-welcome rule; #play acts at once and cuts welcome; #starters and #new-book open dialogs and hush desk guidance. In each case, the fitting hint and Read remain available. BASELINE rule 16 permits the skip or cut. These are not missing necessary instructions.

No new unresolved product lead was found. Resize stress finished cleanly after the repeat checks. The audit's Chrome and host were closed on normal completion. It was not rerun.

#### Left open

- No changes were made to refine.md or refine/, and no git commits were made. Writes are confined to tools/flipbook-studio/ and _scratch/flipbook-studio/.
- Initial brief reads used the command tool's yield setting before the terminating subprocess wrapper was added. All build, drive, diagnostic and audit commands thereafter have explicit terminating limits: 2 minutes bundle, 5 minutes drive batch, 40 minutes audit; short reads 15-30 seconds.
- One Chrome connection reset was retried as smaller batches, which completed. Test corrections and intermediate failures remain in Scratch. The initial after-test reused three before-named JSON paths; baseline PNGs were preserved, and observed before counts were recorded in report-progress.md.
- Existing browser speech fallback remains; no recorded clips exist. Physical printed paper was not checked.
- Existing spec conflicts remain: Blink's explicit eight-frame opening hold and the squashed floor center at y=632 so its bottom meets y=660. No new decision or feature was inferred from unanswered questions.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Flipbook Studio handoff

Build only, 2026-11-04. No commits or separate polish round. All work is confined to this tool and `_scratch/flipbook-studio/`.

#### Layout of the source

`src.html` starts from the kit starter and uses `kit:curio` CSS, Motion, Sound, Read, tones and the `Curio.voice` queue. It then contains the desk layout, modal tools, vector drawing and timing engine. The page is resized in real pixels by `layout()`. Drawings remain in a 960 by 720 coordinate space. `svgPath()` supplies the same smoothed curves to canvas and print.

The main sections are saved-book validation, per-page history, drawing and spacing chart, stable thumbnail controls, starter factories, editing, animation clock, printing, modal tools and input wiring. `window.__tool` exposes state, operations, voice log, clock transitions and print construction for repeatable checks.

#### Tricky parts

- `requestAnimationFrame` advances against an accumulated clock deadline. Held frames do not emit extra ticks. Edits rebase the clock on the drawing being shown, rather than restarting the loop.
- A hold drag retains pointer capture on a stable slider. Playback and hold edits update controls in place. Only structural page operations rebuild the strip, restoring thumbnail focus when applicable.
- Undo and Redo snapshot strokes per page, capped at 50 undo states. Eraser measures distance to a stroke's segments and removes the complete stroke.
- Thumbnail drag reorders the pages; Alt + Left and Alt + Right provide a keyboard equivalent. The selected thumbnail is kept visible using only the strip's horizontal scroll, without scrolling the document.
- In compact landscapes and on phones, secondary tools move into a modal, then return to their original DOM positions. This preserves their event handlers. Main page operations and Play remain in view.
- Print repeats each drawing once per held frame, eight per sheet. It uses only black vector paths, cutting boundaries, frame numbers and the staple margin. No onion skin, chart or painted texture is in the print DOM.
- Saved data is validated before loading. Storage writes are wrapped in try/catch. A storage failure updates the visible hint as well as the status label.
- Spacing labels use collision-free grid rings and light gray leaders when centers coincide. Layout is cached by canvas width and book revision. All 48 labels were checked for overlap in the smallest preview.
- Each dialog keeps its own return-focus target, including a starter library opened from the compact Tools dialog.
- Re-selecting the current mode preserves its narration. The selected thumbnail is kept in view after resizing or changing modes. A live hold drag locks automatic strip following until release so its handle stays under the pointer.
- Limits and unchanged presets acknowledge that nothing changed. Print speech is valid only during the print operation and is hushed when it closes.
- Live timing speech supersedes its prior event at the next change. Hold drags announce once on release; Stop hushes it. Read retains the kit's priority. A deferred spacing explanation can play after Stop.

#### Artwork and placement

Two original OpenAI gpt-image paintings are in `art/`, with prompts and raw PNGs retained. No painted people. The Blink starter is an editable schematic face made from strokes, as required by the spec.

The measured clear glass in `fb-desk` occupies approximately x=13.3%-86.8%, y=10.6%-87.6%. The page uses an inset rectangle x=15.1%-85%, y=12.7%-85.3%, intersected with the visible cover crop. Pencils stay outside this region. The paper texture is shown at 26% opacity over cream, keeping the page quiet enough for pencil strokes.

#### Open questions resolved unattended

- Omit Download GIF. The spec leans toward saved work on this device plus its existing Print pages craft.
- Keep Print pages. The spec explicitly retains the physical flipbook activity; this is not a print card for transferring work between devices.
- Preserve Blink's explicit 8,1,1,1 timing, totaling 11 frames and 0.9 seconds at 12 fps. This conflicts with the general six-frame hold limit. Editing that exceptional hold returns it to the normal 1-6 range. The cold review corrected the bar to eight actual cells with a starter label. That track stays stable during a captured drag; normal holds retain six-cell tracks.
- On Real bounce drawings 3 and 9, preserve the explicitly required floor contact at y=660 with a 28-unit vertical radius. This places the squashed center at y=632, while the unsquashed formula says 620. Other drawings follow the formula exactly.
- Use the requested image tool rather than the older local-FLUX wording in the spec. The current build brief and user instruction require self-generated art during the build.
- Write `codex-report.md` last, since the user's explicit stop trigger overrides the brief's request to create it after the first bundle. Intermediate results are retained in scratch.
- Voice recordings were not made, as instructed. `friendly-dad` / Achird is recorded in the line manifest; the kit currently uses browser speech fallback.

#### Engine changes wanted

None. No shared kit files were changed.

#### Claude Refine fix, round 1, 2026-11-05

- `state.selected` is the student's timing selection; `state.index` is the drawing currently shown by playback. The hold readout, minus, plus and Hold the key use the selection. Explicit thumbnail and handle actions change it. Stop selects the paused drawing. A red underline marks playback separately from the selected border.
- Thumbnail canvases are painted on creation or an artwork change, with only the edited thumbnail repainted. Reorder moves existing tiles and restores focused controls. Stroke paths and centers are cached by their data; holds and frame rate do not invalidate artwork.
- Input and loaded legacy points are rounded to a tenth of a drawing unit. Legacy blue strokes remain accepted and keep their original color. New Blue pencil uses indigo so it differs from the preceding-page ghost.
- Hold drags debounce saves for 180 ms and flush on release or pagehide. Other changes save immediately. The storage warning speaks once per continuous failure, with a successful save allowing a later failure to speak again.
- Print narration finishes before the dialog opens, with the same words in the hint. Sound off opens print immediately. A second tap while narration is pending cannot duplicate printing. Canceling narration cancels that pending print. This also works in headless Chrome, which does not emit `afterprint`.
- Flip uses a slim numbered strip. Coincident chart centers use one ringed dot and an explanatory caption. Compact Draw exposes Undo beside Tools.
- The Why dialog and teacher notes now distinguish film's 24 fps twos from the starter's 12 fps twos, give a feasible bowling-ball timing recipe, define key drawings and ask students to plan their keys before in-between drawings.
- No spec open question was taken up. Keep the 12 fps starters and exceptional Blink opener. No new art, recordings or shared engine changes were needed.
- Evidence and reproducible checks are under `_scratch/flipbook-studio/fix-*` and the associated shots JSON files. The final fix report is `polish.md`.

#### Validation evidence

Scratch contains the independent number recomputation, bar-tool bundles and frames, real mouse and touch input checks, saved-book reload check, functional assertions, narration logs, all-size frames and the final mechanical audit. `codex-report.md` records the final outcomes and any remaining leads.

#### Cold review repairs, 2026-11-04

The cold review played the UI before reading this handoff. Keep the two measured raster paintings and the editable starter geometry.

- Dialogs now finish an active stroke and pause playback before opening. A confirmed Delete or Clear therefore applies to the drawing the student saw, rather than a later playback drawing.
- Spacing guidance now explicitly assumes equal holds, on the stage at compact sizes too. The Why text identifies 24 fps as a common film rate and states that twos means 12 drawings per second at that rate.
- Stop retries an unheard mode welcome after entering that mode during playback. Compact Flip speech names Options. Eraser has its own once-only guidance; Pencil, Onion and thumbnail selection restore matching hints.
- Modal entry hushes desk guidance. No welcome names the inert desk behind a dialog; closing without changing the book brings the still-relevant instruction back. Loading a starter from a compact drawer closes that drawer so Play is reachable. First Play and dialog-opening actions explicitly skip stale welcomes.
- The eraser tests the actual smoothed Path2D, including its stroke width. One pointer owns each stroke; another finger cannot overwrite it or finish it. Structural edits finish the current stroke and reset held-frame state.
- A separate persistent save warning remains visible through subsequent actions and is included in Read. It clears after a successful save. The warning was rechecked at 680x425 and inside a 375x812 host.
- Onion direction has a pattern as well as color: previous drawings are solid blue and following drawings dashed green. The student strokes, thumbnails, timing view and printed paths stay unchanged.
- Flat starter icons now use the starter geometry in shaded paper previews. New and copied pages settle into place briefly, and hold bars respond with short transitions. Motion off removes these movements.

Review evidence is in scratch `before/`, `after/`, `input/`, `voice/`, `phone-recheck/` and `review-audit/`. The independent functional check passed 28 assertions. The real mouse/touch walk, five-repeat narration check and keyboard navigation reported no runtime errors. Keyboard Step twice reached drawing 3; Alt + Right reordered a thumbnail, and focus stayed visible with no page scrolling.

The first custom keyboard test used an incomplete CDP Enter event; its corrected event and the standard drive.py keyboard test both passed. The test error was not a product defect.

The review audit ran once with a 40-minute deadline, Chrome 9951 and host 8755. The session interruption stopped it after all size/state checks, Motion off, held-control walks, five-repeat and quick-tap checks. Its 28 leads are retained in scratch `review-audit/audit.md`; the resize-stress phase was not completed. Do not read its provisional clean stress heading as a completed check. The audit was not restarted, following the one-pass instruction.

Final targeted rechecks covered the onion pattern, truthful eight-cell starter bar, compact modal guidance and storage recovery at their affected sizes. The saved-book, mouse/touch and keyboard checks passed. The final bundle and evidence hash are in scratch `review-validation.json`; codex-review.md records the remaining spec conflicts and validation limits.

#### Next reviewer

The two numerical spec conflicts above remain explicit. The cold review's actual 375-pixel iframe checks passed, including the save warning and eight-frame starter bar. Its single audit was interrupted before resize stress; retain that limitation rather than treating the provisional stress heading as a pass. Physical printer output was not tested. See codex-review.md and scratch review-validation.json for the review evidence. No further review or polish round was started.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
