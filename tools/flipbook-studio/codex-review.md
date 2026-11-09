# Codex review: flipbook-studio

## Played

Cold Grade 7 pass: actual drawing, copying, Time, live hold editing, Flip, Ping-pong and starter/help dialogs before reading the builder's report, handoff, notes or source. The paper and light table invite drawing; timing changes have a tangible effect. Also checked projection use, keyboard and real touch.
Evidence lives in `_scratch/flipbook-studio/`: `cold/`, `before/`, `after/`, `input/`, `voice/`, `phone-recheck/`, `save/`, `review-audit/` and `review-sheets/`.

## Findings fixed

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

## Findings left

- **should fix in spec, general:** Blink timing 8,1,1,1 contradicts the six-frame limit; squashed floor contact y=660 requires center y=632 rather than the unsquashed formula's 620. Kept the explicit starter and floor-contact requirements. The brief forbids changing a contradictory spec during review; it remains unchanged. No new feature or kit change was made.

## Break it

- No score, best score, quiz, reflection gate, percent or hidden-answer check exists. Repeating presets or copying blank pages earns nothing. Try this cards are optional creative prompts, not claimed assessment.
- Holds: actual live handle drags plus repeated extreme inputs and plus/minus changes stay within 1-6, preserve stroke JSON, update the readout and affect the current run immediately. Blink's original eight-frame exception remains explicit.
- FPS and presets: ones 12 frames/1.0 s, twos 24/2.0 s, ease 18/1.5 s; FPS changes preserve holds. Repeated matching choices do not falsely report new work.
- Limits: attempted more than 48 pages and a 401st real stroke; caps hold and hints give a next action. A 288-frame standard book generates 36 print sheets, eight frames each. Blink generates 11 cards over two sheets; paths are black and omit texture/ghosts.
- Destructive shortcut: Play, Delete, wait two seconds, Continue now deletes the drawing shown when asked. Cancel keeps the book. New book clears the stored book only after confirmation.
- Storage: edited Blink survived a fresh tab with holds 8,3,1,1 at 8 fps, 13 frames; reset survived a fresh tab. Forced quota failure remains visible; a successful save clears it.
- Clock: 121 frames in 5.0539 s at 24 fps, error 0.294 frame across ten loops. Live edits retain the shown drawing; Stop acts immediately. Motion off keeps the clock running.
- Functional suite: 28/28 assertions; separate real erasing, touch, keyboard, storage and held-click checks. No runtime errors in product checks. One host favicon 404 was removed from the test host; it was not a tool request.

## Voice walk

Sound on, defaults, 120-ms held clicks and two-second pauses: Pencil, draw, Copy page, revise, New page, draw, Time, drag a hold, Play, drag live, Flip, Stop, Ping-pong, Play, Stop.
Spoken starts: `welcomeDraw`, `onionHow`, `welcomeTime`, `holdChanged`, `welcomeFlip`, in action order. Flip's first queued welcome is correctly stale while playing and starts after Stop. `spacingHow` can drop when leaving Time; its assumption remains visible. Logs: `input/main-voice.json`.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| onionHow, five Copy page actions | how | 1 | 1 |
| holdChanged, five live changes | event | 5 | 5 |
| each main-path mode welcome | how | 1 | 1 |
| Eraser instruction, side path | how | 1 | 1 |

Read interrupts speech and works with Sound off; mode changes release Read without a delayed queue. Events supersede stale events; repeated how-to lines stay silent. Browser speech fallback is used, not recorded Achird audio.

## Facts checked

- **24 fps, ones/twos and expressive holds:** Richard Williams, *The Animator's Survival Kit* (2001), spec's named source; live cross-check [Dave Burgess, Animation Mentor, Timing](https://www.animationmentor.com/blog/timing-the-12-basic-principles-of-animation/). Twelve drawings on twos make one second at 24 fps, six drawings per second at the tool's default 12 fps. Updated the explanation.
- **Spacing, slow in/out, even movement and weight:** Frank Thomas and Ollie Johnston, *The Illusion of Life* (1981), chapter 3; live cross-check [Kevin Koch, Animation Mentor, Slow In and Slow Out](https://www.animationmentor.com/blog/slow-in-and-slow-out-the-12-basic-principles-of-animation/). Dot gaps only imply relative speed with equal exposure time; centers are an approximation when shapes change.
- **Starter coordinates, squash and all readouts:** spec's original formulas, independently recomputed in `numbers.py`/`numbers.json`, then checked against four drawings of each bounce and the browser. Real y=140,204.3078,380,632 at indices 0-3, with the stated floor-contact exception; Even y=140,300,460,620. Nominal ball right edge x=890. Blink 11/12=0.9 s; nervous blink 5/12=0.4 s.
- **Standard maximum and print:** 48 six-frame drawings =288 frames, 48.0 s at 6 fps or 12.0 s at 24, 36 sheets. With Blink's retained eight-frame opener and 47 six-frame drawings, the exception permits 290 frames and 37 sheets; the spec's absolute maximum therefore needs correction.
- **Contrast:** [W3C WCAG 2.2 relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Independent computation matches all seven spec pairs: 4.91,5.30,13.88,5.54,9.79,4.46,3.16. Onion legend colors are graphic accents; words use the muted text color and have pattern cues too.
- **NCAS codes:** [NCAS Media Arts at a Glance](https://nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20Updated.pdf). Cr2 is practiced through developing a sequence, Cr3 through revising timing for a chosen effect, Pr5 through drawing, playback, editing and paper production. These are practiced standards, not a claim of assessed mastery.

## Sensitivity

None requiring a cultural review: original ball motion, abstract editable blink face and drawing materials; no named cultures, religion, hard history or health advice. No painted people; both raster manifests correctly say `people:false`. The schematic face teaches animation timing, not anatomy or a claim about real emotions.

## Flattest moment left

A one-drawing loop is intentionally static, and a long hold can look like a pause. The changing hold strip, single-drawing ticks and timing controls explain it; adding a scored challenge or extra animation topic would exceed the spec.

## Graphics

Opened both finished WebP paintings at final use size, every cold/fault/repair frame, grayscale, Motion off, phone frames and audit contact sheets. Starter previews are richer and more faithful; the table, paper grain, palette, large page and editable pencil art remain.
Art is 98,480 bytes; final bundle 227,031 bytes (227 KB). Both images are present, used and coherently lit; no missing art token, redraw or added raster was needed. The code previews derive from the starter drawings. All 73 audit frames were opened on 13 contact sheets; affected repairs were also inspected at full size.

## Audit

**Audit not finished:** one run with a 40-minute deadline, Chrome 9951 and host 8755. The session interruption stopped it after sizes, states, Motion off, control walks, repeats and quick taps; resize-stress checks were not completed. It was not restarted. Partial report: `review-audit/audit.md`.
All 28 leads answered: 8 plural false positives parse the tail of "0.1 seconds"; 4 timeline-scroll leads describe the required editable book strip; 10 covered keep regions are the desk behind native modal dialogs; 6 skipped/cut Draw welcomes follow Eraser's own instruction, four page actions or later Play/Stop key toggles. No console, focus, target-size or layout failures were reported in completed stages. Repeats and quick taps were clean.
The audit misses semantic problems such as speaking to the inert desk, misleading hold cells and color-only ghosts. Those repairs, plus storage recovery, received 22 targeted shots at the affected sizes after the audit; all passed with zero runtime errors. The main voice path was replayed. The audit snapshot predates these narrow final repairs; the audit was not run twice.
Wave lessons: next-action hints, focus retention, all eight sizes/44-pixel targets, honest numbers and assumptions, mapped standards, Motion-off timing, four visible starter choices, first-action voice and matching visual meanings were checked. Hidden-information diagnosis and answer-card matching do not apply to this open studio. Resize stress remains the explicit audit limit.

## Left open

- The two spec conflicts above are explicit rather than silently changing the required starter. No GIF added; keep the specifically authorized paper flipbook craft.
- Print structure and black paths were checked in the browser; no physical printer test. Friendly-dad/Achird recordings remain unmade under the no-recording rule.
- The first two read-only startup commands had a tool wait bound but no process deadline. Subsequent commands use a bounded subprocess runner. Initial Chrome connection reset; its one small retry succeeded. An incomplete custom CDP Enter event was corrected; standard drive.py and corrected keyboard input both passed.
- Audit resize-stress phase is incomplete because the session was interrupted. Completed evidence and partial leads are preserved; no second review pass was started.
- All started Chrome/server processes are closed, ports 9950-9957 and 8755 verified free, and host.html removed. No git commits; writes confined to the two permitted folders. Validation and bundle hash: `review-validation.json` in scratch.
