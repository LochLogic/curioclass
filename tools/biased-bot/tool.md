# Biased Bot: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: CODEX-BRIEF.md -->

### Codex build brief: biased-bot (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real fourth graders tomorrow.

The tool is `biased-bot`. Its spec is `tools/biased-bot/spec.md`. **Read the spec fully, every line, before you
write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong or
impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

#### 0. Ground rules for this run

- **You may write only inside `tools/biased-bot/`.** Nothing else in the repo. Not `kit/`, not `docs/`, not
  `scripts/`, not other tools.
- If you believe `kit/ml-lab.js` or `docs/families/ml-lab.md` must change (a bug, a missing feature), do NOT change
  them. List the change in `tools/biased-bot/handoff.md` under a heading `## Engine changes wanted`: the file, the
  function, what is wrong, the exact change, and why the tool needs it. Then work around it inside the tool if you
  can, and say how.
- Do not touch the existing art: `tools/biased-bot/art/cafeteria-counter.webp` and `tools/biased-bot/art/prompts.json`
  are already made and stay exactly as they are. Do not draw, generate or download any art. Do not record voice.
- No git commits, no branch changes, no stash. Leave the work as uncommitted files.
- The tool makes no network requests of any kind. You need no internet for this job.
- Scratch space outside the repo: `S:/CurioClass-codex-scratch/` (writable). Put screenshots, Chrome profiles and
  temporary scripts there, never in the repo.
- Ports: Chrome debugging ports **9990 to 9997 only**; the iframe host server on **8795 only**. Other agents are using
  other ports on this machine at the same time.
- Every Chrome you start uses `--mute-audio` (drive.py does this for you). Close every Chrome and server you start.

#### 1. Read these, in this order

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice behavior, testing). Where anything differs, it wins.
1. `tools/biased-bot/spec.md`: everything you build. Read all of it.
2. `docs/agents/BUILD.md`: the build agent brief (the human-agent version of this file).
3. `docs/agents/decisions/BASELINE.md`: the owner's standing decisions.
4. `docs/TOOL-CONTRACT.md`, `docs/KIT.md` (above all the "Voice: Curio.voice" section), `docs/POLISH.md`.
5. `kit/starter/src.html`: start from a copy of it. Also skim `kit/curio.js` and `kit/curio.css` so you use them
   instead of re-implementing anything.
6. `docs/families/ml-lab.md` and `kit/ml-lab.js`: the family engine this tool must use.
7. **The quality bar:** `tools/teach-the-robot/` (`src.html`, `handoff.md`, `notes.md`, `voice/lines.json`,
   `tool.draft.json`). Same engine, grade 2, already through review. Read it to see the level of care expected
   (layouts per size, voice wiring, focus handling, drawing everything at real pixel size). Do not copy its look,
   characters, voice or palette: biased-bot has its own (mustard cafeteria, news-reader voice).
8. Formats: `tools/shape-talk/notes.md` (teacher notes), `tools/calm-corner/art/prompts.json` (art list format, for
   reference only; yours already exists).

#### 2. The rules you must follow (quoted from the docs above)

##### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Images use `art:<name>` tokens only for names in prompts.json." (The only one here: `art:cafeteria-counter`.)
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 4: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool = {state, setMode, allLines, ...}` "so frames can be checked". Also expose the voice log
  (`vlog: V.log`, `get vq() { return V.queue; }`) as teach-the-robot does, and whatever a tester needs to read the
  current jars, results and pad grid.

##### From TOOL-CONTRACT.md "The HTML file must"
1. "Be one file. All CSS, JS, data, images and fonts are inline."
2. "Make no automatic network requests. No external `src=`, stylesheets, `@import`, `url(http...)` or fonts."
3. "Collect nothing. No analytics or cookies. `localStorage` only for per-device conveniences ... wrapped in try/catch."
4. "Have `<html lang>`, `<meta charset>`, `<meta name=\"viewport\">`, a `<title>` and a `<meta name=\"description\">`."
5. "Stay under 2 MB."
6. "Work embedded and full screen. It must be usable in a 16:10 iframe on the tool page and fill the window when opened alone."
Plus: Motion button in the header, `prefers-reduced-motion` as the starting point, "Turning motion off removes
movement only: story pacing and timers stay the same". Credit sources and licenses in a comment near the top.

##### From BASELINE.md (the owner's rules that apply here)
- Rule 2: "Every standard is taught well, above the minimum." Each module code in the spec must be really taught by
  something a student does.
- Rule 4: "Every tool stands alone. ... Defaults must work for a solo user; teacher toggles are extras."
- Rule 7: "Privacy is stated. Wherever a tool records or stores anything, say on screen that it never leaves the
  device." The drawing pad and My cards: say on screen that the drawing stays on this device and is gone when the
  page closes (the spec says nothing is kept).
- Rule 8: teacher notes name where standards touch sensitive topics. The spec's open question (Gender Shades) is
  answered by the spec's own Sources line: "for the teacher notes only". Put it in notes.md, not on screen, and note
  your choice in handoff.md.
- Rule 5: facts stay plain, with care for the people involved. The rooms are fictional; never name a real place or
  group of people on screen or in narration.

##### From STANDARDS.md "Sizes" (check every one, early)
| Size | Why |
|---|---|
| 680x425, 800x500, 1000x625 | the site's 16:10 preview on the tool page |
| 1280x720, **1366x768** | the main use: a school laptop, full screen |
| 1920x1080 | big screens |
| 760 wide | below the 1000 px stack breakpoint |
| 375 wide | phones, inside an iframe host (`python scripts/drive.py biased-bot --host 8795`) |
- "The main controls (the ones a student uses every few seconds) are visible without scrolling at every size. In short
  landscape boxes keep stage and panel side by side with a compact panel instead of stacking."
- "The preview must be readable (scene text about 10 px or more)."
- "Draw the stage at real pixel size and re-lay it out per size ... rather than scaling one fixed design: a 1100 px
  scene scaled into the preview has 6 px text." (So do NOT rely on `Curio.fit` scaling a 1000x620 scene down; lay out
  per size, as teach-the-robot's `layoutFor(W, H)` does.)
- "Tab order: panel controls before long lists of map items."
- "Moving focus on purpose uses `focus({preventScroll: true})`."
- "Fit-to-width guards ... re-measure from the loosest step every time and wait for running animations to finish first."
- Spec, Done when 8: Run, Train Bitsy and the jars on screen without scrolling at 680x425, 1366x768, 760 wide and 375 wide.

##### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
- Narrate only through `Curio.voice` (`V.how` for how-to lines, `V.say` for events, with `valid` and `needs`). Never
  write your own queue.
- One welcome per mode (spec lines 1 and 8).
- "Say how to act. Whenever the tool waits for the student, the line and the hint name the next action and the control."
- "But don't nag. A how-to line is spoken the first time its step comes up; after that it only updates the hint, silently."
- "How-to and teaching lines are spoken once per page load. Event lines (praise, a challenge met, a failed load, a
  result with new numbers) are spoken every time their event happens, and are still dropped when stale. ... Keep an
  explicit set of event line ids in the code."
- "The spoken line matches the state on screen."
- "The hint changes when the state changes. On a tab, panel or mode switch, set the hint at once, then queue the line
  with a `valid` check ... Pick how lines by `V.heard`, never by a counter. The first action never waits behind a line,
  no line names a disabled control, and at a 2 s tap pace no line is lost."
- "Test with held clicks (press, ~120 ms, release)" and read `V.log` to see which clips actually started.
- Spec line 2 (the per-room results) must be recorded as fixed lines: eleven totals per room ("Room 9 got 6 right
  lunches out of 10.", 0 to 10), 33 lines, played in room order. Spoken text must exactly match a line in
  `voice/lines.json` so recordings can replace the browser voice later.
- Lines under about 200 characters, nothing a voice would misread.

##### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." The run is 0.9 s per card with Motion on or off.
- "Nothing overlaps by accident." "Test the extremes": jars at 0 and 30, My cards with many cards, all three rooms
  at 30, the shortest and narrowest boxes.
- "Words match the state. Grammar, counts, plurals." ("1 card", "3 cards"; "1 of 10 right lunches".)
- "Nothing on screen gives the answer away."
- "Keep the action area clear": the menu text is drawn in code over the blank green board in the art; check it lands
  on the board at every size.

#### 3. The engine (use it, do not rewrite it)

`<script src="kit:ml-lab"></script>` after `kit:curio`. It exposes `MLLab`. Use exactly what the spec's "Family
engine" section names: `MLLab.rng(seed)` and `MLLab.uni` for card generation, `MLLab.knn` / `MLLab.train('knn',
items, {features, k: 3})` over the 64 grid cells, `MLLab.evaluate(model, items, {groupBy: item => item.tags.room})`,
and `MLLab.view.groupBars` for the room results. The grid rasterizer and stroke templates stay in your tool.

Warning from the family doc: "a literal closing script tag anywhere in `kit/ml-lab.js` (even inside a comment) ends
the script early". The same applies to your own inline script: never write a literal closing script tag inside it.

**Check the spec's numbers before you build the page.** The family doc says "Every number in a spec table is computed
with the engine and its seed. Check yours in Node before building the page: `const MLLab =
require('../../kit/ml-lab.js')` works without a browser." Write a Node check in the scratch folder that generates the
cards exactly as the spec says (templates, slant, wobble, seeds, rounds, line order, 32x32 sample to 8x8 cells, ink
within 6 units) and reproduces the whole "Checked results" table, row by row, including which digits are misread. If
your numbers differ from the spec, find out why (re-read the spec's formulas precisely: order of operations, the
first-N-of-each-digit rule, seeds per room). If after that they still differ, trust the computation, say exactly what
differs in handoff.md and codex-report.md, and do not change the spec. Then put the identical generation code in
src.html, and in the page confirm the same numbers (a `__tool` hook that runs the table is ideal).

#### 4. Files to make in `tools/biased-bot/`

From BUILD.md "Make these files":
- `src.html` from the starter: the kit stylesheet and script, the tool's palette (the spec's `:root` values), its
  scene and logic.
- `tool.draft.json`: "the tool.json fields from the contract, plus `\"stage\": \"built\"`". Fields: id, status
  ("beta"), hook, outcome, driver, minutes, modes, grades_label, sources, third_party, updated ("2026-10-28"), stage.
  The spec's "Who and how" gives driver, minutes, modes and grades_label. Model it on
  `tools/teach-the-robot/tool.draft.json`.
- `notes.md`: "teacher notes (a 5-minute start, the modes, talk questions, good to know). Look at
  `tools/shape-talk/notes.md`." Use the spec's talk points and the results table; Gender Shades goes here.
- `art/prompts.json`: already exists. Leave it.
- `voice/lines.json`: `{"bank": "news-reader", "voice": "Rasalgethi", "style": "Say clearly and steadily, like a
  trusted radio news reader", "lines": [...]}` with every line `allLines()` returns (use `V.allLines()`), in the
  same shape as `tools/teach-the-robot/voice/lines.json`. Do not record.
- `handoff.md`: "a short note for whoever fixes this tool later: how src.html is laid out, the tricky parts, and what
  you would do next." Include the `## Engine changes wanted` section (write "None" if none).
- `codex-report.md`: your report (section 7).

Do not commit the bundle: `tools/biased-bot/biased-bot.html` is generated build output (git ignores it). Delete
`tools/biased-bot/host.html` (made by `--host`) when you finish.

#### 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex`)

1. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot` (in PowerShell: `$env:CURIO_DRAFT=1; python
   scripts/bundle_tool.py biased-bot`). It must bundle cleanly and the result must be under 2 MB.
2. Frames and real input: `python scripts/drive.py biased-bot <shots.json> <outdir> --port 9990 --profile
   S:/CurioClass-codex-scratch/chrome-prof-9990`. Read the header docstring of `scripts/drive.py` for the shots
   format: each shot `{"name", "w", "h", "js", "clicks", "hold", "gap", "xy", "drag", "keys", "after", "wait",
   "calm", "full", "url", "save"}`. Use held clicks (`"hold": 0.12`) for anything that involves voice. Use `"drag"`
   with whole-pixel, uneven points to draw on the pad (real pointer input, not only a smooth scripted one). drive.py
   prints each shot's js result and every console error, warning and exception: there must be none.
   Put `<shots.json>` and `<outdir>` under `S:/CurioClass-codex-scratch/`.
3. 375 wide: start the host with `python scripts/drive.py biased-bot --host 8795` (it serves until stopped; run it in
   the background and stop it after), then shots with `"url": "http://127.0.0.1:8795/host.html?w=375&h=812"`.
4. Shoot at least: the first screen at every STANDARDS size; Lunch Line mid-run and after a run; each "Done when" row;
   jars at 0 and at 30; old results; the card viewer for each room; Try Your Writing empty, with a drawing, after a
   read, after teaching; Motion off (`"calm": true`); a grayscale frame for Done when 7; the keyboard pen.
5. **Look at every PNG** (open each image file and view it). Fix overlaps, clipping, unreadable text, text under
   10 px in the preview sizes, and anything the spec's "Done when" fails. Recompute every number yourself.
6. Voice: with held clicks at a 2 s pace, read `__tool.vlog` and check every rule in section 2's voice list.

#### 6. Self-check list before you report (BUILD.md "Wave lessons (BR1)", turned into checks)

Every tool in the last wave needed a second review round on these. Check each one explicitly and say how you checked
it in your report.

**Hint and voice**
- [ ] The hint always names the next control, and Read speaks exactly the hint.
- [ ] On a mode switch the hint changes at once, not when a queued line starts.
- [ ] How lines are chosen by `V.heard`, never by counters.
- [ ] The first action never waits behind a line.
- [ ] No line names a disabled control (use `needs`).
- [ ] No line is lost at a 2 s tap pace (held clicks, read `V.log`).

**Focus and layout**
- [ ] Focus is kept when controls rebuild (jar counts, Train, Run/Stop swap), and nothing takes focus on load.
- [ ] Nothing rebuilds under the pointer.
- [ ] The hint's height is reserved so panels don't jump when its text changes.
- [ ] Labels and badges never overlap (cards, jars, bars, mix-ups list, look-alikes).

**Sizes**
- [ ] 44 px targets and an unclipped hint at every STANDARDS size, including 680x425 and 375 wide through the host.

**No giveaways**
- [ ] Badges, meters, names, ids and the length or position of options reveal nothing they should not.
- [ ] No result can be got for free by sweeping a control.

**Honest numbers**
- [ ] Every number or meter says on screen what it assumes (what "right lunches" counts, that Bitsy only sees the
      8 by 8 grid).

**Standards**
- [ ] Every module code (E4-ALG-ML-02, E4-SOC-HU-18, E4-DAT-IM-11, E3-ALG-ML-02) is taught by something a solo
      student does, not only by a teacher question. Say which action teaches which code.
- [ ] Your use of the engine matches `docs/families/ml-lab.md`.

**Motion off**
- [ ] No infinite animations (the kit's `.calm` loops them at 0.01 ms). Timing is the same with Motion off.

Also: no console errors at any size; Escape closes the card viewer and focus returns to the jar that opened it; the
keyboard pen works with arrows and Space; a 7th stroke clears the pad first; empty pad disables "Bitsy, read it!";
all jars at 0 disables Train Bitsy and the hint says to add cards; Start over also empties My cards.

#### 7. Report: write `tools/biased-bot/codex-report.md`

Use this format exactly:

```
# Codex report: biased-bot

## Built
(files made, one line each)

## Numbers check
(the spec's Checked results table next to yours, row by row; any difference and why)

## Done when
1. PASS or FAIL: evidence (frame file names, js results, V.log excerpts)
... (all 8 spec items)

## Self-check (section 6)
(each item: PASS or FAIL, and how you checked it)

## Frames looked at
(every PNG, with its size and what it shows; say you viewed it)

## Engine changes wanted
(same as handoff.md, or "None")

## Left open
(anything not done, not checked, or that you are unsure of)
```

Be honest: a FAIL you report is worth more than a PASS you did not check. When the report is written, you are done.

<!-- end part -->

<!-- part: codex-report.md -->

### Codex report: biased-bot

#### Built

- `src.html`: both modes, seeded cards, real-pixel SVG cafeteria, adaptive panel, pointer and keyboard pad, room viewer, My cards, shared engine and kit narration.
- `tool.draft.json`: beta metadata, stage built, required modes and date, supplied sources and art provenance.
- `notes.md`: five-minute start, modes, discussion, verified table, standards actions, privacy and teacher-only Gender Shades context.
- `voice/lines.json`: 58 unique lines exported from the browser's V.allLines(), including all 33 fixed room totals; news-reader, Rasalgethi; no recordings.
- `handoff.md`: architecture, testing setup, numerical reproduction, narration conflict and engine workaround.
- `codex-report.md`: this report.
- `biased-bot.html`: generated, ignored bundle, 182,478 bytes, under 2 MB. Not committed.

Only this tool folder and the authorized scratch folder were written. The existing spec, brief and both art files were left unchanged. Both art SHA-256 hashes match the initial hashes. No commits, branch changes, stash, downloaded/generated art, recordings or internet research. All Chrome instances started for this work and both test hosts were closed. Ports 8795 and 9990 to 9992 had no listeners at closeout. Temporary host.html was deleted.

Evidence root: `S:/CurioClass-codex-scratch/biased-bot/`.

The exact stock driver command initially failed because the available Python lacked websockets; the ordinary Chrome launch also failed in the managed environment. Checks then used scratch copies of the supplied drivers, a stdlib, localhost-only WebSocket adapter, and muted Chrome with --no-sandbox. The audit's host port was changed in its scratch copy to 8795. Shared scripts were untouched. The final compact-size pass also removed the driver's --hide-scrollbars flag so native Windows scrollbars were actually visible. This exposed and verified the fix for the 44 px target edge case.

Bundle command: `$env:CURIO_DRAFT=1; python scripts/bundle_tool.py biased-bot`. It succeeds with the expected notices about deliberately unrecorded lines. Node syntax checking passes. Static inspection finds no external src/href attributes in the bundle. Drawing data is memory-only; the kit alone remembers Motion in guarded localStorage.

#### Numbers check

Units: right lunches out of 10. Jar order is Room 12 / Room 9 / Room 3. Score order is Room 12 / Room 3 / Room 9.

Before building the page, `numbers.cjs` reproduced the exact templates, random-call order, seeds, first-N-per-digit rule, line interleaving, centering/scaling, 32 by 32 samples, 6-unit ink radius, 8 by 8 features and engine vote. Its generation block is byte-identical inside src.html. `independent_check.py` separately implements the numerical pipeline and nearest-neighbor vote in Python, without importing that JavaScript. Python and the browser's checkTable() match every row and every mistaken digit.

| Jars | Spec scores | Node scores | Python and browser scores | Mistakes checked |
|---|---|---|---|---|
| 15 / 0 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 30 / 0 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 0 / 30 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 3 / 0 | 10 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 6 | Room 9: four 1s read as 4 |
| 15 / 6 / 0 | 10 / 10 / 10 | 10 / 10 / 10 | 10 / 10 / 10 | None |
| 15 / 15 / 15 | 10 / 10 / 10 | 10 / 10 / 10 | 10 / 10 / 10 | None |
| 0 / 15 / 0 | 6 / 6 / 10 | 6 / 6 / 10 | 6 / 6 / 10 | Room 12 and Room 3: four 1s each read as 7 |
| 3 / 0 / 0 | 10 / 10 / 5 | 10 / 10 / 5 | 10 / 10 / 5 | Room 9: two 1s read as 4; three 4s read as 1 |

No numerical difference from the spec. Evidence: `numbers.cjs`, `final-number-lines.json`, `independent_check.py`, `independent-python-results.json`.

Contrast was independently recomputed: white/brand 5.93:1, ink/paper 14.80:1, muted/paper 6.02:1, brand/paper 5.70:1, brand/tile 5.16:1, focus/paper 5.59:1; white on blue 5.28:1, green 5.49:1, berry 5.64:1; ink/pasta 8.12:1. All named pairs pass AA.

#### Done when

1. PASS: `detail/done-1-start.png`, `detail/lunch-full-timed.png`, `done1.json` give [10,10,6]. Four Room 9 mistakes are exactly wrote 1, read 4; the visible list groups them as "Room 9: wrote 1, got tacos (4), 4 cards". V.log starts fixed room lines in Room 12, Room 3, Room 9 order, followed by under. The final wrong-lunch frames show tacos plus a Wanted pasta sticker and pasta icon.
2. PASS: `detail/done-2-more-same.png`, `done2.json` give [10,10,6] with Room 12 at 30. V.log includes `same`, as spoken: "More cards from the same rooms did not help Room 9."
3. PASS: `detail/done-3-three.png` gives [10,10,6] with Room 9 at 3. `detail/done-3-six.png`, `done3.json` give [10,10,10] at 6. V.log includes `all`, as spoken: "Every room got the right lunch. Bitsy learned from everyone."
4. PASS: `detail/done-4-flip.png`, `done4.json` give [6,6,10] after a perfect prior run. The eight mistakes are four 1-to-7 substitutions in each other room. V.log includes `flip`, as spoken: "Now a different room is getting the wrong lunch."
5. PASS: `detail/done-5-old.png` shows grey old results, Train enabled, Run aria-disabled true. Both handlers enforce their disabled state while preserving keyboard focus. After training, Run enables and Train disables; `detail/focus-train.png` retains focus on train.
6. PASS: a whole-pixel, uneven real pointer drag reads 1 in `detail/done-6-read.png` and `done6-read.json`. The grid has the expected two center columns of ink, with edge values 0.3125 and inner values 0.5. Three nearest cards carry Room 12 badges and labels. The early exact-stick relabel probe did not change the guess because existing grids tie exactly; this was investigated, not counted as a pass. The subsequent flagged-1 probe in `supplement/final-writing-read-and-teach.png` and `final-teach.json` changes from 4 to 1 after two correctly labeled My cards. Its three neighbors are My cards, My cards, Room 12. Real teaching clicks were held and two seconds apart.
7. PASS: `detail/grayscale.png` was viewed with all color removed. Circle, square and triangle badges plus complete room names distinguish jars and results. Viewer and look-alike frames also show shape plus name.
8. PASS: all required sizes were shot and viewed. Final compact checks with actual Windows scrollbars are `native/native-scrollbars-680x425.png`, `native/native-scrollbars-760x900.png` and their saved rectangles; Run, Train and every jar control are above the fold. At 680x425, jar step buttons are at least 44.328 by 44 px, bottom 307 px. At 760 wide they are at least 44 px in both dimensions, bottom 321 px. `audit-final/size-1366x768.png` covers the school laptop. `cleanup/phone-clean.png` and `phone-rects.json` use a 375x812 iframe on port 8795: step buttons are 55.5 by 44 px, bottom 390.1 px, with Run and Train bottom 263.1 px. No page scrolling is needed to reach these primary controls.

#### Self-check (section 6)

- PASS, hint names the next control and Read speaks exactly it: hints are set synchronously, independently of speech; `voice-transition-final.json` logs Read with exactly the snapshot's ready hint. Empty, drawing, read, taught, dirty, training, running, stopped and viewer states have separate hints.
- PASS, mode-switch hint changes at once: setMode updates hint before requesting welcome; held mode switches in `voice-transition-final.json` show the correct writing and lunch welcomes and final hint. Old speech is hushed.
- PASS, how lines selected by V.heard: source inspection of hint and readPad; no how-to counters. The kit full audit's five-click repeats report no how line spoken twice.
- PASS, first action never waits behind narration: UI handlers perform actions immediately; no action awaits V.say. First held Run immediately enters running state, without a welcome ahead of it. Jar changes and training hush obsolete narration.
- FAIL, literal "No line names a disabled control": the spec itself requires mutually exclusive instructions. Required line 4 says "Press Train Bitsy, then run the lunch line again." Train is enabled only when Run must be disabled; when Run enables, Train must disable. Required writing welcome similarly names reading as a later step while an empty pad must disable Read. Required wording is preserved. `needs` guards the immediate actionable control, and valid checks guard state, but the later prerequisite-dependent control cannot already be enabled. This conflict is also recorded in handoff.md, rather than falsely marked PASS.
- PASS, no applicable event lost at two-second tap pace: after fixing duplicate event keys, `final-teach.json` logs read4-1, teachHow, learned-2, learned-3 and read1-4 all as spoken, at about 1362, 5070, 12704, 17131 and 21554 ms. Both teaching events survive. The final mode/jar/train/Read sequence logs change and ready as spoken. Stale lines and speech explicitly interrupted by Read or mode/reset are dropped on purpose. The full mechanical audit's ten repeated controls were clean.
- PASS, focus retained and none taken on load: the audit reports no rebuilt control/focus loss in its 14 fresh held-click cases; final-layout-invariants records body focus on load. Train remains focused after completion. Skip returns focus to Run in `supplement/final-skip-focus.png` and its JS snapshot. Run/Stop reuse the same element.
- PASS, nothing rebuilds under the pointer: buttons are created once; counts and disabled attributes update in place. The full audit reports no rebuilt controls. Drawings, results SVG and noninteractive counts may repaint.
- PASS, reserved hint height: 57 px in the shortest layout, 60 px in compact layouts, 66 px wide. Buttons have a fixed 54 px action row. Native scrollbar frames and read-mode frames show the long hint without covering controls.
- PASS, labels and badges: viewed every listed PNG, including all-three-at-30, 99 My cards, every room viewer, stopped/old results, narrow look-alikes and wrong-food stickers. Fixed the initial menu/story overlap, narrow empty-viewer message and compact look-alike widths. The robot name has a real-pixel 10 px floor.
- PASS, 44 px targets and unclipped hint at every size: initial and final mechanical size audits, phone rectangle test, plus final native-scrollbar measurements at 680, 800, 1000 and 760 wide. The compact panel is 316 px so real scrollbar width is accounted for. All tested native-control dimensions are at least 44 px. Scene text is at least 10 px; typography is laid out in real stage pixels.
- PASS, no unintended giveaways: this is an explorer. Room badges intentionally identify source handwriting and never enter features. No score appears before a run; jar names/ids do not encode predictions. The model sees only the 64 ink cells.
- PASS, no free sweep result: changing data only marks results old; it cannot compute a new score until Train and Run. Skip is the explicitly specified way to finish an already started run.
- PASS, honest numbers: visible text defines right lunch, identical 10-card-per-room tests, partial denominators, old/stopped states, and the 8 by 8 grid. Normalization and dataset limits are explained in notes. No synthetic result is presented as evidence about a real school.
- PASS, every module code taught by student action: E4-ALG-ML-02, alter example sources, retrain and compare fixed tests; E4-SOC-HU-18, inspect who receives wrong lunches and repair missing representation; E4-DAT-IM-11, compare group effects of selected data and contribute a personal example privately; E3-ALG-ML-02, label drawings and see changed example-based guesses. These actions work for a solo user.
- PASS, engine use: rng and uni generate examples, train('knn') and knn use exactly 64 features and k=3, evaluate groups by item.tags.room, groupBars renders results. Python, Node and browser independently agree. The engine and family doc were not edited.
- PASS, no infinite animation: both mechanical calm checks report clean. All tool animations have finite iteration counts.
- PASS, motion timing unchanged: actual 30-card durations were 27.3031 seconds on and 27.3150 seconds off. Per-card intervals were 0.9022 to 0.9225 seconds on and 0.9033 to 0.9172 seconds off, including processing overhead. Both use the same 900 ms wait. Training uses the same 600 ms wait in both settings.
- PASS, console errors resolved: detail, cleanup, last, empty-final, voice-final and native passes all report errors in 0 shots. The initial writing-mode negative-width error was traced to the engine and worked around. The generated host's initial favicon 404 was fixed and the clean phone pass has none. Early failures remain in the evidence rather than being concealed.
- PASS, Escape closes viewer and returns to jar: `detail/viewer-escape.png` and snapshot focus jar-12. A final keyboard viewer test tabs into viewer-cards and scrolls 120 px with arrow keys. Close and the scrolling grid form its tab loop.
- PASS, keyboard pen: actual Space and 24 ArrowDown events produce 25 points from [50,15] to [50,87], with the correct ink grid. Evidence: `keyboard.json`, `detail/keyboard-pen.png`.
- PASS, seventh stroke clears first: six prepared strokes, then real Space, ArrowDown, Space leave one stroke [[50,15],[50,18]]. Evidence: `detail/seventh-stroke.png` and driver JS.
- PASS, empty pad disables reading and teaching: `detail/writing-empty.png`, phone writing frame and source/native disabled properties. Clear removes the guess and neighbors as well as ink.
- PASS, all jars zero disables Train and Run and asks for cards: `detail/jars-empty.png`, snapshot dirty true with the add-cards hint. All-three-at-30 disables every More control in `detail/jars-full.png`.
- PASS, Start over empties My cards: `detail/reset-my.png` was prepared with a taught drawing; final snapshot my=0, counts 15/0/0, no result, no ink and reset focus retained.

Mechanical audit leads were individually reviewed. The full audit had seven phone overlap leads; the later size/calm audit had ten. Every one compares text below the scrolling panel's clipping edge with the separately visible stage. Screenshots show no such overlap. The later ten pairs were: result-label/story; Room 12/story line 2; Room 12/story line 3; zero-result label/menu title; zero-result label/story line 3; Room 3/queue title; zero-result label/Tacos; zero-result label/Salad; explanation/robot screen; privacy/robot name. These are clipped-content false positives, not visible collisions. All other mechanical size categories are clean. The final native-scrollbar frames verify the subsequent 316 px compact-panel adjustment.

#### Frames looked at

I opened and viewed every one of the 90 PNG files below. Sizes are the actual PNG dimensions. Phone host images contain a 375x812 tool iframe, even when the outer screenshot is wider. Earlier failures are labeled below; later dedicated frames verify their fixes. All paths are relative to the evidence root above.

| PNG | Pixels | What I viewed |
|---|---|---|
| `initial/initial-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/initial-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `initial/table.png` | 1366x768 | Viewed: Initial browser table and voice export setup, first screen. |
| `initial/writing-empty.png` | 1366x768 | Viewed: Preliminary failure: cafeteria SVG remained over writing mode; subsequently fixed. |
| `audit/calm-1366x768.png` | 1366x768 | Viewed: Motion off, first screen, no infinite animation. |
| `audit/size-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-375x812 (iframe host).png` | 395x832 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit/size-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/done-1-start.png` | 1366x768 | Viewed: Start results: 10, 10, 6 and four Room 9 taco mix-ups. |
| `detail/done-2-more-same.png` | 1366x768 | Viewed: Room 12 at 30, unchanged Room 9 score. |
| `detail/done-3-six.png` | 1366x768 | Viewed: Room 9 at 6, all three scores 10. |
| `detail/done-3-three.png` | 1366x768 | Viewed: Room 9 at 3, score remains 6. |
| `detail/done-4-flip.png` | 1366x768 | Viewed: Only Room 9 training: 6, 6, 10 with 1-to-7 mix-ups. |
| `detail/done-5-old.png` | 1366x768 | Viewed: Old, greyed results, Train enabled and Run disabled. |
| `detail/done-6-read.png` | 1366x768 | Viewed: Actual uneven pointer stick, guess 1, ink grid and three badges. |
| `detail/done-6-taught.png` | 1366x768 | Viewed: Early exact-stick relabel probe, unchanged guess due tied grids; not the passing teaching demonstration. |
| `detail/final-initial-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/final-initial-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `detail/focus-train.png` | 1366x768 | Viewed: After training, focused Train control retains identity. |
| `detail/grayscale.png` | 1366x768 | Viewed: All color removed, room shapes and names remain distinct. |
| `detail/jars-empty.png` | 1366x768 | Viewed: All jars zero, disabled training/run and add-cards hint. |
| `detail/jars-full.png` | 1366x768 | Viewed: Every room at 30, all More buttons disabled. |
| `detail/keyboard-pen.png` | 1366x768 | Viewed: Real keyboard-drawn stick and its grid. |
| `detail/lunch-full-timed.png` | 1366x768 | Viewed: Completed full timed run, 10, 10, 6. |
| `detail/lunch-mid-run.png` | 1366x768 | Viewed: Room 9 flagged 1 served tacos, partial bars and wanted sticker. |
| `detail/motion-off-mid.png` | 1366x768 | Viewed: Motion off during partial run, normal timing. |
| `detail/motion-off-timed.png` | 1366x768 | Viewed: Motion off completed timed run, unchanged scores. |
| `detail/reset-my.png` | 1366x768 | Viewed: Start over after teaching: My cards zero and results cleared. |
| `detail/seventh-stroke.png` | 1366x768 | Viewed: Seventh stroke clears six earlier strokes first. |
| `detail/stop-compact.png` | 680x425 | Viewed: Short-window Stop state and partial results. |
| `detail/viewer-12.png` | 1366x768 | Viewed: Full 30-card jar viewer for 12, grouped 1, 4, 7. |
| `detail/viewer-3.png` | 1366x768 | Viewed: Full 30-card jar viewer for 3, grouped 1, 4, 7. |
| `detail/viewer-9.png` | 1366x768 | Viewed: Full 30-card jar viewer for 9, grouped 1, 4, 7. |
| `detail/viewer-escape.png` | 1366x768 | Viewed: Escape closes viewer and returns focus to Room 12 jar. |
| `detail/writing-760.png` | 760x900 | Viewed: 760-wide writing layout, 300 px pad and ink grid. |
| `detail/writing-compact.png` | 680x425 | Viewed: Short-window writing, full 300 px pad in its stage scroll area. |
| `detail/writing-drawing.png` | 1366x768 | Viewed: Actual pointer drawing and matching live grid, before reading. |
| `detail/writing-empty.png` | 1366x768 | Viewed: Empty writing mode with disabled read and teaching controls. |
| `detail/writing-many-my-cards.png` | 1366x768 | Viewed: 99 My cards, readable counts and neighbor labels. |
| `supplement/final-number-lines.png` | 1366x768 | Viewed: First screen used for numerical, voice and inline-resource checks. |
| `supplement/final-short-mid.png` | 680x425 | Viewed: Compact mid-run, Stop and Skip accessible. |
| `supplement/final-short-result.png` | 680x425 | Viewed: Compact results panel deliberately scrolled to bars and mix-ups. |
| `supplement/final-short-writing-read.png` | 680x425 | Viewed: Earlier narrow result with wrapped neighbor names; later widened cards and automatic stage scroll. |
| `supplement/final-skip-focus.png` | 1366x768 | Viewed: Completed skip returns keyboard focus to Run. |
| `supplement/final-viewer-small.png` | 680x425 | Viewed: Compact Room 9 viewer, all jars at 30. |
| `supplement/final-voice-read-and-switch.png` | 1366x768 | Viewed: Earlier mode/jar/train/Read probe, later refined by final voice transition. |
| `supplement/final-writing-read-and-teach.png` | 1366x768 | Viewed: Passing flagged-1 teaching demonstration, My cards 2, read changes from 4 to 1. |
| `supplement/phone-initial.png` | 550x840 | Viewed: Phone first screen; initial host favicon 404 subsequently fixed. |
| `supplement/phone-results.png` | 550x840 | Viewed: 375-wide results panel deliberately scrolled to all bars and mix-ups. |
| `supplement/phone-viewer.png` | 550x840 | Viewed: 375-wide Room 9 viewer, full-height overlay and card grid. |
| `supplement/phone-writing.png` | 550x840 | Viewed: 375-wide writing mode, main controls, privacy and 300 px pad. |
| `cleanup/final-layout-invariants.png` | 1366x768 | Viewed: First screen used for numerical, voice and inline-resource checks. |
| `cleanup/phone-clean.png` | 550x840 | Viewed: Clean phone first screen and measured controls. |
| `cleanup/small-read-clean.png` | 680x425 | Viewed: Short-window ink grid and three readable look-alikes. |
| `cleanup/small-stop-clean.png` | 680x425 | Viewed: Stopped partial lunch line, card separated from robot screen. |
| `cleanup/viewer-keyboard-clean.png` | 680x425 | Viewed: Focused viewer grid after real keyboard scrolling. |
| `audit-final/calm-1366x768.png` | 1366x768 | Viewed: Motion off, first screen, no infinite animation. |
| `audit-final/size-1000x625.png` | 1000x625 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1280x720.png` | 1280x720 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1366x768.png` | 1366x768 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-1920x1080.png` | 1920x1080 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-375x812 (iframe host).png` | 395x832 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-680x425.png` | 680x425 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-760x900.png` | 760x900 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `audit-final/size-800x500.png` | 800x500 | Viewed: Lunch Line first screen, controls, menu alignment and readable scene. |
| `last/final-big-wrong-lunch.png` | 1366x768 | Viewed: Final school-laptop wrong lunch and feeding card. |
| `last/final-small-wrong-lunch.png` | 680x425 | Viewed: Final compact wrong lunch with wanted-food icon and 10 px robot name. |
| `empty/empty-viewer.png` | 680x425 | Viewed: Correct empty-jar hint, narrow message column found and subsequently fixed. |
| `empty-final/empty-viewer-fixed.png` | 680x425 | Viewed: Empty jar with correct hint and full-width message. |
| `voice-final/voice-transition-final.png` | 1366x768 | Viewed: Final held mode, jar, train and Read transition state. |
| `native/native-scrollbars-1000x625.png` | 1000x625 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-680x425.png` | 680x425 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-760x900.png` | 760x900 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-800x500.png` | 800x500 | Viewed: Final first screen, 316 px panel, actual Windows scrollbars and measured 44 px targets. |
| `native/native-scrollbars-writing-read.png` | 680x425 | Viewed: Final short writing result with actual Windows scrollbars visible. |

#### Engine changes wanted

- File: `kit/ml-lab.js`.
- Function: private `host(el, draw)`, inside `go`, used by `view.groupBars`.
- Problem: hiding a chart sets the host rectangle to zero. The engine forces a 60 px width, while groupBars reserves at least 80 px for labels and another 12 px, producing SVG rect width -32 and console errors.
- Exact change wanted: after reading `const r = el.getBoundingClientRect()`, return without drawing when `r.width <= 0 || r.height <= 0`. Keep the previous measured dimensions so the existing ResizeObserver redraws when a real size returns. Consider also guarding the view's available bar width.
- Why needed: mode switching legitimately hides the Lunch Line results while keeping its state.
- Tool workaround: in writing mode, keep the results at a fixed 326 px width, positioned off screen with `visibility:hidden`, and do not call `bars.update` there. The hidden chart retains valid geometry. No engine or family document was edited.

#### Left open

- The literal disabled-control narration conflict described above is unresolved. Required sequential wording is preserved; the report does not claim that every later-step control is already enabled. It needs a wording decision, not an engine change.
- The supplied art still has its existing review-pending status. It was not edited or reclassified.
- Voice clips were deliberately not recorded. The bank/voice/style and complete fixed line inventory are ready; current speech uses the kit browser fallback. Queue starts were checked through V.log in muted Chrome; recorded-voice quality was not assessed.
- Verification was on Windows headless Chrome 156 with actual CDP clicks, pointer drags and keys, including a 375-wide iframe. Physical school hardware and a live classroom were not tested.

No other requested build work or verification remains open. All eight Done when items pass in these checks; the single literal narration self-check remains FAIL for the documented spec conflict.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 0 (general 0, family 0), should fix 9 (general 8, family 1), polish accepted 11

### biased-bot: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C), refine/sensitivity.md (SE, PASS).
All 8 Done-when pass in every lens. The Teaching lens rebuilt the results from the spec in Python (all 1,330 jar
settings swept) and Craft's `checkTable` reproduces the whole table: no number is wrong. The sensitivity agent
passed the Room 9 framing and the Gender Shades note.

#### Should fix
1. **The Room 9 jar is empty when the tool sends students to it** (T-S1, P-1, SE1; general). After a run the line and
   hint say "Tap a room's jar to see how its students write" (notes step 3: "Tap the Room 9 jar"), but Room 9 starts
   at 0 cards, so the viewer shows "This jar is empty" and the long-flag sentence ("Lots of people learn to write 1
   with a long flag...") never shows. Show each room's writing from its students (the lunch line), not only from the
   jar's cards, so Room 9's writing and that sentence are always reachable from the first run; keep the "normal way
   to write" sentence wherever Room 9's writing first shows. The same goes for any room whose jar is empty.
2. **The hint after a run never names the next experiment** (T-S2, P-2; general, BR1 lesson). It returns to "Press Run
   the lunch line. Predict..." while the voice points at the jars. The hint follows the state: after the first run,
   look at the jars; after looking, try more Room 12 cards; after that, try Room 9 cards. Pick by `V.heard`.
3. **One taught card changes nothing, with no reason given** (T-S3, P polish; family:ml-lab). One card is one of three
   votes, so the first "It's a 1" leaves the read wrong after "Bitsy learned your card". Keep kNN honest: say why on
   screen ("Bitsy looks at the 3 closest cards. Yours is 1 of 3 votes. Teach it once more.") and show the three
   nearest cards for that read. Note it in docs/families/ml-lab.md if the vote view is an engine part.
4. **"Every room got the right lunch. Bitsy learned from everyone." is false where it plays** (T-S4, P-4; general).
   It plays at 15/6/0 with Room 3's jar empty, and with only the student's own cards. Say what is true ("Every room
   got the right lunch this time.") and keep "learned from everyone" for when every room has cards. Change the
   spec's line to match.
5. **A first tap on Run skips the welcome and story for good** (P-3; general). The likeliest first tap leaves ~27 s
   of silence and a non-reader never hears the premise. Use `welcomeAfter` (or an equivalent) so the story comes
   once the run's own line is done.
6. **Results below the fold in small windows** (P-5; general, BR1 lesson). After a run the room bars are below the
   fold at 680x425 and 800x500 (Room 9's bar hidden at 800x500); at 375 they sit in a nested scroll with no cue.
   Keep the results, Room 9 first, in view after a run at every size.
7. **Writing mode stacks at preview sizes** (P-6; general). At 680x425 and 800x500 the pad and "What Bitsy sees"
   stack and a read scrolls the drawing out of view; at 375 the look-alikes the hint names are below the fold. Side
   by side in short landscape boxes (STANDARDS), and the look-alikes in view.
8. **Focus lost at a jar's limit** (C-1; general, BR1 lesson). src.html:85 sets the real `disabled` on the focused
   Fewer or More at 0 or 30; use `aria-disabled` as Train and Run do.
9. **Re-tapping the current mode cuts the welcome for good** (C-2; general). src.html:101 `setMode` hushes even when
   the mode doesn't change. Do nothing when the mode is unchanged.

#### Polish accepted
10. **Engine fix in kit/ml-lab.js** (C polish, the builder's own engine request; family:ml-lab). Approved: `host()`
    skips drawing at zero size and draws on the first real size; groupBars clamps widths at 0, takes an empty-state
    text (no "0 of 0 right lunches" three times before a run) and a size option. Then drop the off-screen parking and
    the `font-size:11px!important` override. Update docs/families/ml-lab.md (or the family section in
    tools/teach-the-robot/spec.md) in the same change, and confirm teach-the-robot and leaf-sorter-ai look and behave
    the same (bundle each and compare frames).
11. Teaching a card shows which jar it went into (T-N2).
12. The empty-jar viewer doesn't say the same thing twice (T-N1).
13. notes.md: "one Room 9 card isn't enough, two are" holds only with Room 12 at 15 and the others empty; say so (T-P2).
14. notes.md: the long-flag 1 is standard in much of Europe and Latin America, so some students may write it; invite
    them to teach Bitsy, never ask who writes like Room 9 (SE2).
15. notes.md: the Gender Shades numbers (up to 34.7% vs at most 0.8% error) and the PMLR link (SE3).
16. notes.md: a talk question for the 0 / 15 / 0 run, "Does Room 12 write wrong now?" (SE4).
17. spec Sources: Gender Shades measured the gaps between groups; it did not see the companies' training data (SE5).
18. art/prompts.json: the cafeteria-counter entry says no people and `"people": false` (SE6).
19. The tray and sticker don't sit on Bitsy mid-run, and "− Fewer" doesn't wrap (C).
20. The Play lens's other polish items that touch only what the student sees, as the builder judges (list them in
    the handoff).

#### Spec open questions (not for the builder)
- Predict: a way to record the class's guess before a run (T-P1). Adds to the spec.

#### Settled calls
- The spec's lines 4 and the Try Your Writing welcome name a control that is disabled at that moment (the builder's
  own flag). BR1 lesson wins: reword them so the line names the step that enables the control first ("Pick the
  cards, then press Train Bitsy"), and change the spec's wording to match.

#### Exit check, round 1

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 194 KB (no clips recorded
yet; browser voice). All driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on ports 9930 and 9932, 375
through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the exit-check scratch folder (s1 to
s10). No console errors, warnings or exceptions in any shot (the only log line was the host page's own favicon 404).

##### Items
1. PASS. Run, Skip, tap the Room 9 jar (`i1-room9-after-run`; `i12-empty9` before any run; `h375-view9`): the viewer
   shows Room 9's ten lunch cards grouped 1, 4, 7 and "Lots of people learn to write 1 with a long flag and 7 with a
   line through it." with the jar at 0.
2. PASS for the path the item names (`i2-hint-path`, hint log): after the run "Room 9 got wrong lunches. Tap the Room 9
   jar...", after Close "Try more of the same writing. Press More under Room 12...", after the 30 / 0 / 0 run "More of
   the same did not help. Try More under Room 9, then Train Bitsy.", at all 10 "Every room got the right lunch. Use
   Fewer and More...". The hint changes at once on each step. New item 21 below covers the step after Room 9 at 3.
3. PASS. A flagged 1 at the start reads 4; after one "It's a 1" the look-alikes show My cards (vote 1) and two Room 12
   cards (vote 4), the note says "Yours is 1 of 3 votes. The other two votes still win." and the hint "Press It's a 1
   once more." (`i3-teach-once`); a second teach reads 1 (`i3-teach-twice`). Same at 375 (`h375-wrteach`). The family
   doc notes it.
4. PASS. 15 / 6 / 0 speaks "all" and not "represented" (`dw3` log); 15 / 15 / 15 speaks both (`i4-represented`). Spec
   line 6 matches.
5. PASS. First tap on Run (`v3-run`): the story is spoken at once, then "Watch the lunch cards, or press Stop or Skip to
   results." When the run is skipped first, the running line drops as stale and the results follow (`dw1`).
6. PASS. After Run and Skip the Room 9 first score strip is fully in view at 680x425, 800x500, 1000x625, 1280x720,
   1366x768, 1920x1080, 760x1000 (`res-*`) and 375 (`h375-res`), with no page scroll.
7. PASS. After a read the pad and "What Bitsy sees" sit side by side and the three look-alikes are in view at every
   size (`wr-*`: the grid's left edge is right of the pad at all seven sizes; `h375-wrread`).
8. PASS. Six held clicks on Room 12's Fewer down to 0: focus stays on `fewer-12`, `aria-disabled="true"`, not
   `disabled`; six Enter presses on More up to 30: focus stays on `more-12` (`i8-focus-limit-click`, `-keys`).
9. PASS. Three taps on Lunch Line 1.5 s apart: the story and the welcome are both spoken, nothing hushed
   (`i9-retap-mode`).
10. PASS. Engine: `host()` returns without drawing and resets W and H at a zero box, and draws on the next real size
    (bars redraw after Lunch, Writing, Lunch: `panel-1366`, aria-label with the numbers); groupBars clamps `bw` and the
    fill share at 0, shows `empty` ("Room scores appear here.", `def-1366x768`) and takes `size`; the off-screen
    parking and `font-size:11px!important` are gone from src.html. Doc against code, line by line: the signature
    `{names, glyphs, order, unit, empty, size}` matches; "empty ... when no group has tested items" matches
    `!keys.some(k => G[k] && G[k].n > 0)`; "size ... minimum 10, scales captions and row spacing" matches
    `Math.max(10, O.size)`, `factor` on rowH, the glyph radius and the caption offset, caption `size - 1` (minimum
    10); "omitted options preserve the original 13 px labels, 12 px captions and layout" holds (size 13, factor 1,
    `lab` is the old formula, caption 12, offset 14); the host bullet matches. Models, seeds and ties are untouched
    (`checkTable` reproduces the spec table exactly, `dw-table`). teach-the-robot: bundled from two scratch copies,
    one with HEAD's ml-lab.js and one with the current one (its own files untouched; the two bundles differ only in
    the engine); first screen, three teaches, a Mystery read and a parade at 1366x768 and 680x425 give identical hint,
    state and panel text, and identical frames except one card's glow caught at a different animation phase (parade
    frame). It calls only `knn` and no views, so the change cannot reach it. leaf-sorter-ai has only a spec here.
11. PASS. "Added to My cards: 1. Label: 1." under the look-alikes, and the My cards line pulses (`i3-teach-once`).
12. PASS. The empty Room 9 viewer says "The jar has 0 training cards." and "Close this view and use More to add
    training cards." (`i12-empty9`), no repeat.
13. PASS. notes.md says the one-versus-two claim assumes Room 12 at 15 and Room 3 at 0.
14. PASS. notes.md: Europe and Latin America, invite students to teach Bitsy, never ask who writes like Room 9.
15. PASS. notes.md: 34.7% against at most 0.8%, with the PMLR link.
16. PASS. notes.md talk question "Does Room 12 write wrong now?" after training only on Room 9.
17. PASS. Spec Sources: Gender Shades measured the gaps without access to the companies' training data.
18. PASS. prompts.json says "no people" and `"people": false`.
19. PASS. Mid-run on a mix-up card (card 3, Room 9): the tray and the "Wanted pasta" sticker do not overlap Bitsy at
    680x425, 800x500, 1366x768 and 1920x1080 (`i19-midrun-*`, bounding boxes); Fewer is one line at every size.
20. PASS on what the Play lens list asked: story first then the short welcome, a larger sticker and x marks on wrong
    queue cards, mix-up wording "Room 9: 4 cards wrote 1 (pasta), got tacos.", no "0 of 0" bars, bigger numbers at
    1920, art kept to its aspect (`xMidYMax slice`), a Bitsy in Writing, the keyboard ring only after a key.
Settled call: PASS. Line 4 is "Pick the cards, then press Train Bitsy." (Train is enabled at that moment) and the
Writing welcome no longer names a disabled control; the spec's wording matches.

##### Done when
1 PASS (10 / 10 / 6, Mix-ups "Room 9: 4 cards wrote 1 (pasta), got tacos.", `dw1`). 2 PASS (30 / 0 / 0 gives 6,
"same" spoken, `dw2`). 3 PASS (15 / 3 / 0 gives 6, 15 / 6 / 0 gives 10 everywhere, "all" spoken, `dw3`). 4 PASS
(0 / 15 / 0 gives 6 / 6 / 10 with 1s read as 7, "flip" spoken, `dw4`). 5 PASS (Run `aria-disabled` after More,
results grey with "(old)", `dw5`). 6 PASS (a stick 1 reads 1, `v1-stick1`; the grid matches the drawing; look-alikes
carry badges; teaching changes later reads). 7 PASS (`dw7-gray`: circle, square, triangle with names). 8 PASS (Run,
Train and the jars on screen at 680x425, 1366x768, 760 wide and 375, no scroll).

##### New finding
21. **should fix, general.** src.html:116, `includeHow`. After a run where Room 9 has some cards and is still at 6,
    the hint reads "Try examples from the other rooms. Use More under a room whose jar is empty." The only empty jar
    is then Room 3, which never helps Room 9 (spec table: 15 / 0 / 30 gives 6), and at 15 / 3 / 3 no jar is empty but
    the hint still says so (`f-includeHow`: counts 15 / 3 / 3, scores 10 / 10 / 6, that hint). A solo student who
    follows the hint goes the wrong way at the tool's key step (BR1 lesson: the hint names the next control and
    matches the state). Better: while Room 9 is under 8 and has cards, "Room 9 still got wrong lunches. Press More
    under Room 9 again, then Train Bitsy."; keep `includeHow` for the 0 / 15 / 0 case, worded for the rooms that are
    actually empty.

##### Polish and nits noticed (not blocking)
22. **polish, general.** An event line waits behind a how line already playing: draw then Read at once, and "Bitsy
    read a 4." is spoken about 4 s after the tap, behind "Press Bitsy, read it!..." (`v1-read5`, `v1-stick1`); the
    fifth "Your card went into My cards." came 5.4 s late behind the `taught` line (`v1-teach5`). The screen updates at
    once and nothing is stale, but cutting a how line when its own control is pressed would keep the voice in step.
23. **nit, family:ml-lab.** docs/families/ml-lab.md: the biased-bot row leaves out `MLLab.glyph` and `train('knn')`,
    which the tool also calls.

##### Regressions looked for
- Sizes (`def-`, `res-`, `wr-` at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000; `h375-def`,
  `h375-res`, `h375-view9`, `h375-wrread`, `h375-wrteach`): no button under 44 px; Run, Train, the jars, their buttons
  and the hint on screen; hint never clipped; no page scroll; nothing focused on load. At 1366x768 the panel's last
  privacy line sits inside the panel's own scroll (it scrolls).
- allLines() against voice/lines.json: 69 and 69, identical in order and wording.
- Motion off (`calm-midrun`, `calm-train`): no running animations, training still takes 0.6 s and cards 0.9 s each;
  Motion on: no infinite animations (`motion-inf`).
- Saving and reset (`reset`, `reset-reload`): after teaching, a run and the viewer, Start over gives jars 15 / 0 / 0,
  My cards 0, a clear pad, "No run yet.", the strip hidden, focus kept on Start over; storage holds only the kit's
  `curio-motion`; no cookies; a reload has no My cards.
- Focus when controls rebuild (`focus-rebuild`): More, Train, Run, the teach buttons and Clear keep focus; Skip hands
  focus to Run; the viewer takes focus to Close and Escape returns it to the jar.
- Network: no resource requests in a full session (PerformanceObserver); no http URLs in the bundle besides the SVG
  namespace. Console clean in every shot.
- Words: no em dashes in src, notes, spec, lines, tool.draft.json, the family doc or the engine; "Curio Class" never
  shortened.

##### Voice check (browser voice, Sound on, Motion on, held clicks)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| story (welcome) | how | once | 1 (stage tap, Tab, Run, Sound back on) |
| lunchWelcome | how | once | 1 |
| running | how | once in 5 runs | 1 |
| Room 12 / Room 3 / Room 9 totals | event | 5 in 5 runs | 5 / 5 / 5 |
| under | event | 5 | 5 |
| lookHow, moreSame | how | once each | 1, 1 |
| change (5 More) | how | once | 1 |
| ready (5 trains) | how | once | 1 |
| inspect (5 jar opens) | how | once | 1 |
| Bitsy read a 4 (5 reads) | event | 5 | 5 |
| readHow, teachHow | how | once each | 1, 1 |
| Your card went into My cards (5 teaches) | event | 5 | 5 |
| taught | how | once | 1 |
| same / all / represented / flip | event | once in their runs | 1 / 1 / 1 / 1 |
| writingWelcome | how | once | 1 |
| Read (5 taps) | read | 5, the hint | 5, each the current hint |

- Stale (`v2-stale`, `v2-stale2`, taps 0.2 s apart): the results and lookHow drop on the jar change or mode switch,
  writingWelcome plays only in Writing, no line plays after its moment.
- First tap: stage and Tab give the story within 0.15 s; Run gives the story then the running line; Lunch Line gives
  the welcome; Try Your Writing gives its welcome; Read speaks the hint only; Sound says nothing, and Sound off then on
  brings the story once (`v3-soundoffon`); More and a jar speak only their own line (the story comes with the first
  Run).
- Read: cuts the story and speaks the hint, with Sound off too; a mode change or Run right after Read starts its line
  at once (`v4-*`).
- Order: spoken lines follow the actions in every log.

##### Gate
1 Done when: all 8 pass. 2 Standards: each code is taught by a solo action (changing sources and retraining; reading
results by room and inspecting Room 9; comparing outcomes by source; labeling a drawing and seeing the neighbors
change), as notes.md maps them. 3 Solo defaults: story card and welcome, hints name the next control, except item 21.
4 Sensitivity: refine/sensitivity.md PASS; nothing in its scope changed against it. 5 Open should fix: item 21.
6 Bundle clean, 194 KB, no console errors, no network. 7 Voice counts right. Gate fails on 5 only.

##### Left open
- 21 (should fix, general): the `includeHow` hint once Room 9 has some cards. Narrow; the integrator may fix it and
  send this check back.
- 22 (polish) and 23 (nit): known, not done unless taken.

#### Exit check, round 2

Cold check, 2026-10-28, the last round. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 190 KB
(194,636 bytes; no clips recorded, browser voice). All driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on
ports 9930 and 9932, 375 through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the exit-check
scratch folder exit-bb2 (`s1` sweep, `s21`, `s22`, `s22b`, `sz`, `h375`, `vc`, `dw`). Logs pair each held click's time
with the voice log and with each utterance's real start and end (a wrapper on `speechSynthesis.speak`). No console
errors, warnings or exceptions in any shot (the only log line was the host page's own favicon 404).

##### Round 1 open items
21. PASS on the three named states. 15 / 3 / 0 (Room 12 / Room 9 / Room 3; scores 10 / 10 / 6): "Room 9 still got
    wrong lunches. Press More under Room 9 again, then Train Bitsy." (`h21-15-3-0`); following it (More under Room 9,
    Train, Run, Skip) gives 10 / 10 / 10 and "Every room got the right lunch..." (`h21-15-3-0-follow`). 15 / 3 / 3: the
    same hint, and following it gives 10 / 10 / 10 (`h21-15-3-3`, `-follow`). 0 / 15 / 0 (6 / 6 / 10): "Try examples
    from the other rooms. Use More under Room 12 or Room 3, then Train Bitsy.", both empty there; one More under Room
    12 lifts Room 12 to 8 and Room 3 to 7 (`h21-0-15-0`, `-follow`). The spec's hint paragraph matches. But the sweep
    of all 1,330 jar settings (`s1/sweep`) finds the same fault one step away: new item 24.
22. PASS. Draw, then Read at once: "Bitsy read a 1." takes the voice 2 ms after the tap and starts 0.2 s later,
    cutting "Press Bitsy, read it!" (`e22-read`). Five teaches at a 2 s pace: each "Your card went into My cards." is
    queued at its tap and cuts the how line playing (`e22-teach5`, `teach5-r0` to `-r2`). After a Skip during "Watch
    the lunch cards..." the first result starts 0.14 s after the tap (`runskip9`). Read still wins: a teach tapped while
    Read speaks waits behind Read and plays after it (`e22-readwins`, `e22-readwins2`: Read at 3.26 s, the card line at
    12.48 s; nothing cut Read). Events never cut events (a queued event keeps `cutHow` off). Items 25 and 26 are what
    the cut-in costs.
23. PASS. docs/families/ml-lab.md's biased-bot row now lists `rng`, `uni`, `MLLab.glyph`, `train('knn')`, `knn`,
    `evaluate` and `groupBars`.

##### Round 1 items spot-checked
1 PASS (`h-view9` at 375 and `view9-*` at every size: Room 9's lunch cards and the long-flag sentence with the jar at
0). 2 PASS (log `vc/lunch`: lookHow after the first run, moreSame after Close, moreMissing after the 30 / 0 / 0 run,
moreRoom9 once Room 9 has cards, allHow at 10). 3 PASS (`wrread-*`, `h-wr`: one teach shows My cards vote 1 and two
Room 12 votes 4, "Yours is 1 of 3 votes. The other two votes still win.", hint "Press It's a 1 once more."). 4 PASS
(30 / 6 / 0 speaks "Every room got the right lunch this time." and not "represented"; 30 / 6 / 3 speaks "Every room has
cards in the training jars...", `vc/lunch`). 5 PASS when the story is left to finish (`e22-runwait`: story, then "Watch
the lunch cards..."); see 25. 6 PASS (`res-*` and `h-res`: the Room 9 first strip on screen at every size). 7 PASS
(`wrread-*` and `h-wr`: pad and "What Bitsy sees" side by side, the three look-alikes in view). 8 PASS (six held
clicks on Room 12 Fewer: focus stays on `fewer-12`, `aria-disabled="true"`, `disabled` false). 9 PASS (three taps on
Lunch Line 1.5 s apart: story and welcome both spoken, `vc/retap`). 10 PASS on the doc against kit/ml-lab.js: `host()`
returns at a zero box and resets W and H; groupBars takes `{names, glyphs, order, unit, empty, size}`; `empty` shows
when no group has `n > 0`; `size` has a minimum of 10 with `factor` on rows, glyphs and captions, caption `size - 1`;
omitted options give 13 px labels and 12 px captions. `checkTable` still reproduces the spec table exactly (`dw`).

##### Done when
1 to 4 PASS (`dw`: checkTable gives 10/10/6, 10/10/6, 10/10/6, 10/10/6, 10/10/10, 10/10/10, 6/6/10 for the spec rows;
Mix-ups "Room 9: 4 cards wrote 1 (pasta), got tacos."; "same", "all" and "represented" spoken in `vc/lunch`). 5 PASS
(More after a run: Run `aria-disabled`, strip "(old)", "Old results. Pick cards and press Train Bitsy."). 6 PASS (a stick
1 reads 1; look-alikes and teaching as in 3). 7 not re-shot (badges and names unchanged). 8 PASS (sizes below).

##### New findings
24. **should fix, general.** src.html:113 to 119, `nextHint`. Room 9 under 8 goes to `moreRoom9`, but Room 9 at 8 or 9
    falls through to `includeHow`. Swept: 22 jar settings, every one with Room 9 at 3 cards and either Room 12 at 6 or fewer or Room 3 at 6 or 9 (for
    example 15 / 3 / 6 gives 10 / 10 / 9 and 15 / 3 / 9 gives 10 / 10 / 8). There the hint says "Try examples from the
    other rooms. Use More under Room 12 or Room 3, then Train Bitsy." while Room 9 is the room still wrong; no amount of
    Room 12 or Room 3 fixes it, and one More under Room 9 does (15 / 6 / 6 and 15 / 6 / 9 give 10 everywhere). Reached
    in two taps from item 21's own 15 / 3 / 3 by trying More under Room 3 (`h21-15-3-6`: strip "Room 9 9 of 10", that
    hint; `h21-15-3-6-follow`: following it, 18 / 3 / 9, leaves Room 9 at 8). "under" is not spoken there either (it
    waits for under 8). Same fault as 21 (BR1: the hint matches the state). Better: send any Room 9 score under 10
    with Room 9 cards to `moreRoom9`, and keep `includeHow` for the states where Room 12 or Room 3 is the low room; the
    spec's "below 8" wording moves with it.
25. **should fix, general.** src.html:131 and 173, `cutHow` in `finish()`. The 22 fix cuts any how line playing, and
    the story welcome counts as one. Tap Run (the story starts, about 7 s), then Skip within those 7 s: the first
    result cuts the story, the story is already marked said and never comes back, and the story card left the stage at
    Run (`e22-runskip`: story from 1.34 s, Skip at 4.50 s, results at 4.51 s; same in `vc/lunch` and `vc/runs5`). This
    brings back round 1's item 5 (a non-reader never hears the premise) on a likely path, and BR1 says no line is lost
    at a 2 s tap pace. Better: never cut `story` (let results wait behind it, or queue it again), or cut only the how
    line whose step the tap just did.
26. **polish, general (kit voice).** When a how line was already speaking and an event cut it, headless Chrome left the
    event's utterance pending in 3 of 5 such runs: no start event, the queue held to the 4.8 s cap, then "interrupted"
    (`teach5`, `teach5-r0`, `-r1`; `-r2` and `runskip9` started at once). In those runs the first "Your card went into
    My cards." was logged spoken but stayed silent, and the next came 4.8 s after its tap. The cut (`cur.cut(); stop()`)
    followed at once by `say0()`'s own `stop()` and `speak()` may be the trigger; it may be headless only. Worth one
    check on a real Chrome with the browser voice before clips land.

##### Regressions looked for
- Sizes (`def-`, `res-`, `wrpre-`, `wrread-`, `view9-` at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
  760x1000; `h-def`, `h-res`, `h-view9`, `h-wr`, `h-reset` at 375 through the host): no button or pad under 44 px, no
  page scroll, the hint never clipped; Run, Train, the jars and their buttons, the strip, the pad, Read and the teach
  buttons all inside the window; no overlapping controls (only the modal viewer over the header at 375); smallest text
  10 px (680x425 writing), 11 px elsewhere; nothing focused on load.
- allLines() against voice/lines.json: 70 and 70, identical in order and wording (moreRoom9 is the new line); longest
  118 characters.
- Motion off (`motionoff-midrun`, `motionoff-train`): no running animations mid-run or while training; cards still
  0.9 s each. Motion on: no infinite animations in any session.
- Reset (`reset-desk`, `h-reset`): after teaching, a run and the viewer, Start over gives 15 / 0 / 0, My cards 0, a
  clear pad, "No run yet.", the strip hidden, focus kept on Start over; storage holds only `curio-motion`; no cookies.
- Focus when controls rebuild: Train keeps focus through training, More keeps it, Skip hands it to Run, the viewer
  takes it to Close, a teach keeps it, Fewer at 0 keeps it.
- Network: no resource entries in any session; no http URLs in the bundle besides the SVG namespace.
- Words: no em dashes in src, notes, spec, lines, tool.draft.json, the family doc, the engine or this file.

##### Voice check (browser voice, Sound on, Motion on, held clicks)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| story (welcome) | how | once | 1 per session (cut by an early Skip, item 25) |
| lunchWelcome | how | once | 1 (`vc/retap`) |
| running | how | once in 5 runs | 1 (`vc/runs5`) |
| Room 12 / Room 3 / Room 9 totals | event | 5 in 5 runs | 5 / 5 / 5 (`vc/runs5`) |
| under | event | 5 | 5 |
| lookHow, moreSame | how | once each | 0 (dropped as stale: the jar was tapped first), 1 in `vc/lunch`; lookHow 1 in `vc/runs5` |
| change (5 More) | how | once | 1 |
| ready (after Train) | how | once | 1 |
| inspect (5 jar opens) | how | once | 1 |
| Bitsy read a 4 (5 reads) | event | 5 | 5 |
| readHow, teachHow | how | once each | 1, 1 |
| Your card went into My cards (5 teaches) | event | 5 | 5 (logged; see 26) |
| same / all / represented | event | once in their runs | 1 / 1 / 1 |
| writingWelcome (Writing tab) | how | once | 1 (`vc/wwelcome`) |
| Read (5 taps) | read | 5, the hint | 5, each the current hint |

At a 2 s pace a jar change hushes the result lines still queued (stale, `vc/lunch`), as in round 1; given time to
finish, all five runs' results play in full.

##### Gate
1 Done when: all pass. 2 Standards: unchanged since round 1, each code taught by a solo action. 3 Solo defaults: the
hints name the next control, except in item 24's states. 4 Sensitivity: refine/sensitivity.md PASS; nothing in its
scope changed. 5 Open should fix: 24 and 25. 6 Bundle clean, 190 KB, no console errors, no network. 7 Voice counts
right except the story lost to an early Skip (25). Gate fails on 5.

##### Left open (to the integrator)
- 24 (should fix, general): `nextHint` sends Room 9 at 8 or 9 to `includeHow`. One condition.
- 25 (should fix, general): `cutHow` cuts the story welcome. One condition.
- 26 (polish): a speech engine stall after a cut, seen headless; known, not done unless taken.

#### Integrator fix (24, 25) and close

Narrow check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`, 189 KB (194,834 bytes; no
clips, browser voice). Driving with `scripts/drive.py`, held clicks (0.12 s), Chrome on ports 9930 to 9938 with its own
profile, 375 through `drive.py --host 9931` (host.html deleted after). Frames and logs are in the scratch folder exit-bb3
(`s1` sweep, `d24`, `s25`, `sz`, `h375`). No console errors, warnings or exceptions in any shot (the only log line was
the host page's own favicon 404).

24. **PASS.** Sweep in the page (`s1/sweep`): all 1,330 jar settings (0 to 30 by 3 per room, not all empty), scored with
    the page's own `training`, `LINE` and `MLLab.train('knn')` / `evaluate` (agrees with `checkTable` on all 8 spec
    rows), each hint read from the page's own `#hint` after setting the state and re-rendering. Hints: allHow 1,065,
    lookHow 120 (all Room 9 at 0), moreRoom9 117, includeHow 28; no other hint and no unknown text. Every includeHow
    setting has Room 9 at 10 (the 22 round 2 states, Room 9 at 8 or 9, now all give moreRoom9: 15 / 3 / 6, 15 / 3 / 3
    and 15 / 3 / 9 give moreRoom9). For all 117 moreRoom9 settings, pressing More under Room 9 repeatedly reaches Room 9
    = 10 before the jar is full, and never drops Room 12 or Room 3 from 10 on the way; from there the hint path ends at
    allHow in all 117. Following the hint from every one of the 1,330 settings (moreRoom9 and moreMissing: More under
    Room 9; lookHow: open the jar; moreSame: More under Room 12; includeHow: More under Room 12 or Room 3) reaches
    "Every room got the right lunch" in all 1,330: no setting points to a hint whose action cannot help.
    Driven with held clicks at a 2 s pace (`d24`): 15 / 3 / 6 (More 9, More 3, More 3, Train, Run, Skip) gives 10 / 10 / 9
    and "Room 9 still got wrong lunches. Press More under Room 9 again, then Train Bitsy." (`h24-15-3-6`); following it
    (More 9, Train, Run, Skip) gives 15 / 6 / 6 at 10 / 10 / 10 and "Every room got the right lunch this time." spoken
    (`h24-15-3-6-follow`). 15 / 3 / 3 gives 10 / 10 / 6 and the same hint (`h24-15-3-3`); one More under Room 9 gives
    10 / 10 / 10, "all" and "represented" spoken (`h24-15-3-3-follow`); a second More 9 keeps 10 / 10 / 10
    (`-follow2`). Focus ends on Run each time. Doc nit (not behaviour): spec.md:105 still says "still scores below 8";
    the code now sends any Room 9 score under 10 with Room 9 cards and a jar under 30 to this hint.
25. **PASS.** Fresh page, story not yet said (`s25`, utterance start and end from a wrapper on `speechSynthesis.speak`):
    - 2 s pace, Run at 1.33 s, Skip at 3.49 s: story 1.55 to 8.70 s in full, then "Room 12 got 10 right..." from 8.97 s,
      the other totals, "Some students got...", the lookHow hint (`r25-skip2`).
    - 0.5 s pace, Run at 1.35 s, Skip at 1.99 s: story 1.52 to 8.64 s in full, results from 8.91 s (`r25-skip05`).
    - The same in the item 21 / 24 drives (`d24`): Skip 2.1 s after Run, results wait for the story's end (7.4 s).
    Round 1 item 5 holds: Run left alone gives the story (1.45 to 8.53 s), then "Watch the lunch cards..." (8.87 to
    12.82 s), then the results (`r25-item5-runwait`). Item 22 holds: Draw then Read, "Bitsy read a 1." queued 2 ms
    after the tap and started 0.24 s later, the "Press Bitsy, read it!" how line cut (`r25-e22-read`); five teaches at a
    2 s pace, each "Your card went into My cards." queued at its tap and the how lines cut (`r25-e22-teach5`); Skip
    during "Watch the lunch cards..." (after the story) cuts it, first result 0.12 s after the tap (`r25-runskip9`); Read
    wins: Read at 3.25 s, the teach tapped during it waits and plays at 12.48 s, Read not cut (`r25-e22-readwins2`).
    Item 26 still seen headless: the first teach event in `r25-e22-teach5` was logged spoken but never started.
- allLines() against voice/lines.json: 70 and 70, identical in order and wording (`sz/lines`).
- Sizes: 1366x768 and 680x425 (`def-`, `res-`, `wr-`) and 375 through the host (`h-def`, `h-res`, `h-view9`, `h-wr`,
  `h-reset`): no page scroll, nothing under 44 px, nothing off screen, the hint never clipped, no overlaps (only the
  viewer over the header at 375, as before), smallest text 10 px (680x425 writing), nothing focused on load, no running
  animations at rest.

##### New observation (outside 24 and 25)
27. **polish or should fix, integrator's call.** A second Run within the story still loses it: Run, Skip, Run, Skip at
    a 2 s pace (`r25-4tap2`: Run 1.34 s, Skip 3.49 s, Run 5.64 s) and at a 0.65 s pace (`r25-skip05b`). The second Run's
    `V.hush()` (src.html:177, `run()`) stops the story at about 4 s in; it is marked said and never comes back, and the
    new run speaks "Watch the lunch cards..." instead. Not the `cutHow` path that 25 fixed, and less likely than Run then
    Skip, but the same cost (the premise lost). Possible fix: let the welcome survive a Run hush, or queue it again if it
    was cut before its end.

##### Gate
24 PASS, 25 PASS. Items 5 and 22 still hold. No should fix left open from rounds 1 and 2; 26 (polish, headless stall)
and the spec.md:105 wording nit are left to the integrator, with 27 above. Bundle clean, 189 KB, no console errors, no
network. **PASS.**

##### Left open after close (integrator)
- 27 (polish, general): Run, Skip, Run inside the story's first 4 s hushes the story for good (`V.hush()` in `run()`). Three taps in 4 s; left for Final look.
- 26 (polish, kit voice): the headless speech stall (an event cutting a how line sometimes never starts); check once in a real Chrome.
- spec.md line 105 changed to "below 10" to match the code (integrator).

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: biased-bot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; family doc docs/families/ml-lab.md and
the engine description in tools/teach-the-robot/spec.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
biased-bot` (177 KB). Ran scripts/audit_tool.py first, then drive.py shots at 1366x768, 1920x1080, 800x500, 760x900,
680x425 and 375x812 through `drive.py --host`.

Counts: blockers 0, should fix 2 (general 2, family 0), polish 7 (general 5, family 2), nits 2 (general 2)

#### Contract (passes)

- One file, 177 KB, no network requests (the only URL in the bundle is the SVG namespace; no fetch, XHR, socket or
  beacon). No console errors or exceptions in any tool shot.
- Kit used for voice, motion, sound, chimes (`Curio.voice`, `Curio.wait`, `Curio.yes`). Engine used as the family
  doc says: `MLLab.rng` and `uni` for the cards, `train('knn', k 3, 64 grid features)`, `knn` for the pad read,
  `evaluate` with `groupBy` room, `view.groupBars`, `glyph`. The rasterizer and templates stay in the tool, as the
  spec says. Nothing re-implemented.
- `__tool.checkTable()` reproduces every row of the spec's results table, including 3/0/0 = 10, 10, 5 and the miss
  lists (Room 9's four 1s read as 4; 0/15/0 reads the other rooms' 1s as 7). Real clicks: start run = 10, 10, 6 with
  "Room 9: wrote 1, got tacos (4), 4 cards".
- Saving and reset: nothing is stored except the kit's `curio-motion` key. Privacy is stated on screen in both modes
  (rule 7). Start over clears jars, results, My cards, the pad and the "all right" flag, and speaks the ready hint.

#### Should fix

1. **Focus lost when a jar hits its limit.** src.html:85 (`update`, `disabled('fewer-'+r ...)` / `'more-'+r`) sets
   the real `disabled` attribute on the button that has focus. Five presses of Room 12 More (to 30), by held click or
   by Enter, leave `document.activeElement` = BODY; the same for Fewer at 0 (shots b-more30, c-fewer0, kb-more). The
   focus ring disappears and a keyboard user's next Enter does nothing. Train and Run already use `aria-disabled` to
   keep focus; do the same here (or move focus to the jar's other button). BR1 lesson "Focus is kept when controls
   rebuild". **general**
2. **Tapping the current mode button cuts the welcome for good.** src.html:101 `setMode` always runs `V.hush()` and
   re-enters, even when `m === state.mode`. Tap the stage (welcome starts at 1.3 s), tap Lunch Line 1.5 s later: the
   log shows `lunchWelcome spoken`, then at 3.0 s `story dropped (hush)` and `story spoken`; the 8 s welcome was cut
   after about 1.6 s and, being marked said, never returns (shot same-mode-tap). Same with Tab then Enter on a fresh
   page (Tab counts as the first key, the welcome starts, Enter on Lunch Line cuts it 80 ms in: v-ft-key), and in
   Try Your Writing (writingWelcome cut, readHow restarted). Return early when the mode is unchanged. **general**

#### Polish

3. **Engine: views draw at zero size.** kit/ml-lab.js:244 `host()` draws at `max(60, size)` when its element is
   hidden, and groupBars then makes negative widths: a `display:none` groupBars logs "attribute width: A negative value
   is not valid (-32)" (shot zero-size). This tool never hits it only because it parks `#results` off screen with
   `visibility:hidden` in write mode (src.html:16, `body.write-mode #results{position:absolute;top:-10000px;...}`)
   instead of hiding it. Engine change: skip drawing while the box is 0 wide or high and draw on the first real size
   (the ResizeObserver already fires then); clamp bar widths at 0. Then the tool can hide `#results` plainly. Update
   ml-lab.md in the same change. **family:ml-lab**
4. **groupBars before a run reads "0 of 0 right lunches" three times** (1366 default frame), and the tool forces its
   text size with `#bars text{font-size:11px!important}` (src.html:16) because the view has fixed 13 and 12 px text.
   Better: an `empty` text option ("No run yet") and a `size` option in groupBars, so siblings don't override with
   `!important`. **family:ml-lab**
5. **"− Fewer" wraps to two lines** ("−" over "Fewer") in every jar at 680x425, 1366x768 and 1920x1080 (the buttons
   are 44 to 50 px wide in a 350 px panel), while "+ More" fits on one. Better: icon-only minus and plus with the
   word under the jar, or "Fewer" without the sign. **general**
6. **Tray and "Wanted pasta" sticker sit on Bitsy's wheels** at 1366x768 and 1920x1080 (shots mixup-frame, s-1920:
   tray `ty = min(H-48, ry+70*rs)`, src.html:121). The mix-up, the moment the lesson hangs on, is half hidden.
   Better: place the tray beside the robot's slot side, clear of the body. **general**
7. **Full-size queue jumps and forgets.** src.html:117 `start=state.running?Math.min(20,Math.floor(state.done/10)*10):0`
   applies when not compact too, so at 1366x768 the 30-card queue drops to cards 11 to 30 once 10 are served ("13 of
   30 served" shows 20 cards), then snaps back to all 30 at the end; after a run no card shows whether it was read
   right. Better: keep all 30 when they fit, and mark each served card with a small tick or the food it got (shape,
   not color). **general**
8. **Keyboard pen and screen readers miss the read.** Lifting the keyboard pen (Space, src.html:149) never calls
   `hint(true)`, so a keyboard student never hears "Press Bitsy, read it!" (the pointer path does, on pointerup);
   and `#guess` ("Bitsy reads: 4") is not live, so with Sound off a screen reader gets only "Compare the three
   look-alikes", not the guess. Better: speak the how on pen lift; put the guess in the live hint or make `#guess`
   `aria-live`. **general**
9. **Lunch-line card badges are tiny with color off.** The queue cards carry only an 8 px glyph (r = 4, src.html:117)
   and no name; in a grayscale frame at 680x425 and 375 the circle and square are hard to tell apart. Done when 7
   still passes through the jars, bars and viewer (shot s-gray). Better: badge radius 6 or more, or a room number
   under each card in the wide layout. **general**

#### Nits

10. "Room 9 got 1 right lunches out of 10." (and Room 12 / Room 3 at 1): the fixed lines for 1 say "lunches"; the
    bars say "1 of 1 right lunches" early in a run. "1 right lunch". Lines and voice/lines.json together. **general**
11. The pad canvas is `role="img"` but takes keys (src.html:20); `role="application"` with the same label tells a
    screen reader it is interactive. **general**

#### Access (passes, except items 1, 8)

Tab order: Lunch Line, Try Your Writing, Motion, Sound, Read, Train, Run, then each jar and its live buttons, Start
over (disabled Fewer buttons skipped). Visible 3 px focus ring. The viewer takes focus on Close, traps Tab between
Close and the card grid, Escape closes it and returns focus to its jar. Skip moves focus to Run when it disappears;
Stop keeps focus (same button). Train keeps focus while busy (`aria-disabled`). Nothing takes focus on load. Audit:
no target under 44 px at any size. Rooms are shape plus name in jars, bars, viewer and look-alikes.

#### Lines (pass)

`__tool.allLines()` returns 58 lines and voice/lines.json holds the same 58, word for word, in the same order. Spec
lines 1 to 11 match the code text exactly; the 17 extra hint lines are the panel hints Read speaks. No em dashes in
src.html, notes.md, lines.json or tool.draft.json; "Curio Class" never shortened in text. Every line under 200
characters. Each spoken line was compared with the frame state in the runs below; none names a hidden or disabled
control (`needs` on every how line; `under` needs `#jar-9`).

#### Standard voice check (1366x768, Sound on, Motion on, held clicks 120 ms)

| Line | Kind | Action x5 | Expected | Spoken |
|---|---|---|---|---|
| change "Press Train Bitsy, then run..." | how | More (Room 9) x5, gap 4 s | 1 | 1 |
| Room 12 got 10 / Room 3 got 10 / Room 9 got 6 | event | Run + Skip x5, gap 14 s | 5 each | 5 each |
| under "Some students got the wrong lunch..." | event | same runs | 5 | 5 |
| read1 "Bitsy read a 1." | event | Bitsy, read it! x5, gap 4 s | 5 | 5 |
| teachHow "If Bitsy got it wrong..." | how | same | 1 | 1 |
| learned "Bitsy learned your card." | event | It's a 7 x5, gap 4 s | 5 | 5 |
| same "More cards from the same rooms..." | event | Room 12 to 30, Train, Run (real clicks) | 1 | 1 |
| all "Every room got the right lunch..." | event | 15/6/0 run | 1 | 1 |
| flip "Now a different room..." | event | 0/15/0 after all-right | 1 | 1 |
| inspectEmpty (viewer on an empty jar) | how | first tap on Room 9 jar | 1 | 1 |

- Stale (gap 0.2 s: Run, Skip, More, Train, Try Your Writing, Lunch Line, Start over): Room 3 and Room 9 results and
  under dropped by hush at the More tap; lunchWelcome and story dropped stale on return (results exist); "ready"
  spoken after Start over, matching the screen. No line played after its moment.
- First tap: stage tap gives lunchWelcome at 0.15 s, then story; Run (a `speaks` button) gives nothing until its
  results; Try Your Writing gives only writingWelcome; a jar gives only its viewer line; Read speaks the hint only;
  Sound says nothing, and Sound back on brings lunchWelcome once. Tab then Enter: see should-fix 2.
- Read: Read during the welcome cuts it and speaks the hint (story dropped); with Sound off Read still speaks; a mode
  change right after Read starts writingWelcome at once.
- Order: every run's lines follow the actions in order.
- Audit walk (five clicks 2 s apart on every speaking control): clean.

#### Layout (passes)

Run, Train Bitsy and every jar button are on screen without scrolling at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900 and 375x812 (host). The hint is unclipped at all of them. In Try Your Writing the pad,
Bitsy read it and the teach buttons are on screen at 375 (pad top 319, 300 px), and the read scrolls the sight panel
into view at 680x425. Results scroll inside the panel in the 680x425 preview and at 375, as the notes say. Motion off:
no animations at all 2.5 s into a run.

Frames looked at: audit size-* and calm frames; f1 a to m; f2 s-write-375ish, s-write-1366, s-write-760,
s-midrun-680, s-midrun-1366, s-viewer9-1366, s-gray, s-1920; f3 h375-write, h375-results, h375-viewer; f5
mixup-frame (scratch folder lens-bb-craft).

#### Audit pilot

- Confirmed: none of its 11 leads were real. All 11 were the 375 overlaps between the scrolled results panel and the
  stage SVG text; the panel clips its overflow, so they are false (frame size-375x812). Its clean rows for targets,
  fold, hint, focus on load, Motion off and the five-click voice walk matched my own runs.
- Missed (needs more than one click or a look at the frame): focus lost when More reaches 30 or Fewer reaches 0;
  re-tapping the current mode cutting the welcome; the engine's zero-size drawing; the tray and sticker over Bitsy
  mid-run; the wrapped "− Fewer" label (wrapped, not clipped). It could test a disabled-under-focus check after
  repeated clicks and a same-mode re-tap, and should ignore overlaps that a scrolling ancestor clips.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: biased-bot

Played cold twice: as a grade 4 student alone at home (no teacher, can't read the screen well), and as a teacher
projecting Lunch Line to a class at 1366x768 and 1920x1080. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
biased-bot` (177 KB, clean). Frames via `scripts/drive.py` (port 9972) and `--host` for 375; audit via
`scripts/audit_tool.py` (ports 9970-9971). No console errors in any shot (the only log line was the host page's own
favicon 404).

Frames looked at: default, end of a full run, mid-run (4 of 30), Writing default, Writing after a read, Room 9 viewer,
at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900; 375x812 (host) default, results, results
scrolled, Writing, Writing after a read, viewer; plus at 1366x768 a mix-up mid-run, Room 9 viewer at the start (empty
jar), all jars empty, all jars at 30, old results, stopped, grayscale results, Motion off run, a jittered mouse drag of
a flagged 1, the keyboard pen.

Checked and fine: Done when 1 (10/10/6, four "wrote 1, got tacos"), 2 ("same" spoken after Room 12 to 30), 3 (Room 9 at
3 still 6; at 6 all 10 and "all" spoken), 4 (Room 12 and Room 3 to 6 with 1s read as 7, "flip" spoken), 5 (Run
disabled and results greyed "Old results" after a jar change), 6 (a stick 1 reads 1, grid matches, look-alikes show
badges; a flagged 1 reads 4, two teaches flip it to 1, and three taught flagged 1s bring Room 9 to 10 in the lunch
line), 7 (panel badges and bars by shape and name in grayscale), 8 (Run, Train and jars on screen at every size). How
lines are spoken once ("change" once, then silent); event lines repeat per run. Keyboard pen draws. No sideways
scroll at any size.

#### Blockers

None.

#### Should fix

1. **The jar the voice sends you to is empty.** Lunch Line, `openViewer` (src.html:117) with the start jars. After the
   first run the voice says "Some students got the wrong lunch. Tap a room's jar to see how its students write." (it
   `needs` `#jar-9`). Room 9's jar starts at 0, so tapping it shows "This jar has no training cards yet. / This jar is
   empty. Press Close, then More to add cards." and nothing else: no Room 9 handwriting, and the one line that names
   the style ("Lots of people learn to write 1 with a long flag...") is replaced. The central discovery step dead-ends
   for the solo student in the room it matters for. Better: when a jar is empty, still show that room's writing (for
   example its 10 lunch-line cards, labeled "Room 9's lunch cards, not in the jar yet") with the flag sentence, then
   "Press More under Room 9 to put some in the jar." Seen: frame `view9-start` (1366x768); audit walk row 11.
   general.
2. **The hint doesn't change when a run ends.** `nextHint()` (src.html:72) returns `ready` after a finished run, so
   the panel and Read keep saying "Press Run the lunch line. Predict how many right lunches each room will get." on
   top of a 10/10/6 result, while the voice says to tap a jar. A student who presses Read after the run hears
   "predict" for a run that already happened, and the waiting moment never names the next real step. Better: an
   after-run hint keyed on the result ("Room 9 got wrong lunches. Tap a jar to see how each room writes, or change
   the jars and press Train Bitsy."; once all are 10: "Try training on just one room."). Seen: snapshot hint in every
   `res-*` shot; `v-seq-same` log. BR1 lesson "hint and voice". general.
3. **Tapping Run first means the story is never heard and nothing is said for 27 s.** `speaks:'#run'` (src.html:71)
   skips the welcome on a Run first tap, `run()` never queues the `running` how line, and the `story` line's `valid`
   (`!state.results`) is false from the first card on. Run is the big gold button the hint points at, so it is the
   most likely first tap: a non-reader gets no premise ("Room 12 trained Bitsy with their own handwriting") and no
   word until the results. Seen: `v-firstrun` held click on `#run`, `vlog` empty after 5 s; audit walk row 5 spoken
   blank. Better: on the first run speak the story (short) and "Watch the cards. Press Skip to results to jump ahead."
   once. general.
4. **"Bitsy learned from everyone" is said when it didn't.** `all` (src.html:52, 107) plays the first time all rooms
   reach 10. The usual route (notes step 4, Done when 3) is Room 12 15, Room 9 6, Room 3 0: Room 3 has no cards in
   the jar, so the line is untrue on screen (the jar says "0 cards") and blurs the talk point that Room 3's messy
   writing was never the problem. Seen: `v-seq-all-flip` log with jars 15/6/0. Better: "Every room got the right
   lunch. Bitsy needed to see Room 9's way of writing." (the line is from the spec, so the spec line changes too).
   general.
5. **The result of a run is below the fold in the preview and on a phone.** At 680x425 the panel ends at "Full run:
   10 cards per room." with no bars; at 800x500 only Room 12's bar shows (Room 9, the one that changed, is hidden);
   at 375 the results sit inside a 350 px panel that scrolls on its own inside the page scroll. Nothing tells the
   student to scroll. Seen: `res-680x425`, `res-800x500`, `h375-res` (and `h375-res-scroll` shows they exist).
   Better: in compact sizes put a one-line score strip on the stage after a run ("Room 12 10/10, Room 3 10/10,
   Room 9 6/10" with badges), or scroll the panel to the results when a run ends. general.
6. **Writing mode stacks pad and "What Bitsy sees" in short windows, so you can't compare them.** At 680x425 and
   800x500 the pad (300 px) and the grid stack in the stage; after "Bitsy, read it!" `readPad` scrolls the stage to
   the grid and the drawing goes off screen. At 375 the look-alikes the hint asks you to "compare" are below the
   page fold. STANDARDS: keep side by side with a compact layout in short landscape boxes. Seen: `wrread-680x425`,
   `wrread-800x500`, `h375-wrread`. Better: shrink the pad (about 200 px) and grid to sit side by side under 900 px
   wide. general.

#### Polish

1. **Welcome and story say the same thing twice, and the action isn't last.** On a stage tap: "Good morning. Room 12
   trained Bitsy to read lunch cards with their own handwriting. Press Run the lunch line..." then 8 s later "Room 12
   built Bitsy to read lunch cards, and they trained it with their own handwriting. Now the whole school uses it."
   (`v-firststage` log). Better: story first, then one short "Press Run the lunch line to see how it does." general.
2. **One teach often changes nothing, and nobody says why.** A flagged 1 reads 4; after one "It's a 1" it still reads
   4 (k = 3), after two it reads 1 (`w-drag`: reads 4, 4, 1, 1, 1). A solo student thinks teaching failed. The hint
   after teaching ("Press Clear pad to try another, or Bitsy, read it! to compare.") could say, when the read didn't
   change: "Bitsy still sees more look-alikes that say 4. Teach it one more card." This is also the tool's best
   moment for "one example is not enough; two are". family:ml-lab.
3. **The mix-up moment is small and quiet.** The "Wanted pasta" sticker is 11 px text tucked under Bitsy, partly over
   its wheels, with no sound (`lunch-mixup`). It is the harm the tool is about. Better: a larger sticker beside the
   tray, a soft "wrong" cue from the kit, and mark wrong cards in the queue (a small tray icon or X) so after the run
   the stage shows which four cards went wrong, not only the text list. general.
4. **Every run speaks all three room totals (about 9 s) before the line that matters.** After five runs a student has
   heard "Room 12 got 10 right lunches out of 10" five times (`v-seq-same`, `v-seq-all-flip`). They are event lines
   per the spec, so this is a spec question: after the first run, speak only the rooms whose total changed, or lead
   with "same"/"flip". general.
5. **Teacher projection: the numbers are small.** Bar captions are forced to 11 px (`#bars text{font-size:11px!important}`,
   src.html:16) and Mix-ups is 13 px, so at 1920x1080 on a projector "6 of 10 right lunches" can't be read from the
   back (`res-1920x1080`). Better: scale captions with the panel at large sizes, and show the room totals on the stage
   too (see should fix 5). general.
6. **Mix-up wording.** "Room 9: wrote 1, got tacos (4), 4 cards" puts two different 4s side by side. Better: "Room 9:
   4 cards wrote 1 (pasta), got tacos." general.
7. **Empty bars say "0 of 0 right lunches"** before any run (`def-1366x768`, `jars-empty`); "No run yet" is already
   above. Better: leave the captions blank until a run. family:ml-lab (the `groupBars` empty state).
8. **Room badges on the lunch-line cards are about 8 px.** Circle and square read as the same dot in grayscale and on
   a projector (`gray-res`, zoomed). The 30 cards are where a class first spots Room 9's flagged 1s. Better: badges
   about 14 px, or a room-colored strip with the shape on each card. general.
9. **The cafeteria art is stretched to the stage** (`preserveAspectRatio:'none'`, src.html:124): at 760x900 the counter
   and trays are pulled tall (`def-760x900`). Real art will show this more. Better: `xMidYMax slice` and place the menu
   board from the image's own box. general.
10. **Writing mode is a plain form.** No Bitsy, no cafeteria: a blank pad and a grid on flat mint (`wr-1366x768`). A
    small Bitsy beside "What Bitsy sees" holding the guess on its screen would tie the two modes together. general.

#### Nits

1. Mid-run the room label ("Room 12") above the feeding card stays after the card has slid and faded (`mid-1366x768`):
   the label is outside the animated group. general.
2. Drawing with the mouse leaves the keyboard pen's blue ring at its last keyboard spot on the pad (`w-drag`). Show the
   ring only after a key press. general.
3. "− Fewer" wraps to a lone minus over "Fewer" at most sizes (`def-1366x768`). general.
4. The empty-jar viewer says it is empty twice in two different sentences (`view9-start`). general.

#### Audit pilot

- Leads confirmed: none needed fixing; the sizes, Motion off and five-click rows matched my frames (targets, fold for
  Run/Train/jars, how lines once). Leads that were wrong: all 11 overlaps at 375 are panel text hidden by the
  panel's own scroll box, measured against the stage SVG below it; nothing overlaps on screen (`h375-def`).
- It missed: the empty Room 9 viewer (row 11 only shows the line), the stale hint after a run, results below the fold
  after a run, Writing's stacked layout after a read, and the silent Run first tap (row 5 shows "spoken" blank but
  doesn't flag it); it can't see past one click, so none of the run-end or teach states.

Teaching lens (read after the above): agree on the empty Room 9 jar (its S1 = my should fix 1), the post-run hint
(S2 = 2), "learned from everyone" (S4 = 4) and the doubled empty-jar text; differ only in level on the one-teach
moment (its S3 should fix, my polish 2: I'd accept its level, since the screen says "learned" then gets it wrong); it
also caught `teach` training untrained jar changes (N2), which I missed; my silent Run first tap and the compact-size
results and Writing layout (should fix 3, 5, 6) are not in its list.

<!-- end part -->

<!-- part: refine/sensitivity.md -->

PASS

### Sensitivity agent: biased-bot (round 1)

Fresh read of REFINE.md (Sensitivity agent), BASELINE rules 5 to 8, spec.md, src.html (all on-screen strings, hints,
viewer text, aria labels), notes.md, voice/lines.json, art/prompts.json, tool.draft.json and refine/teaching.md.
Not bundled or driven: every line checked here is a static string in src.html or lines.json, and the teaching lens
already drove the states. Gender Shades checked against the PMLR listing and the authors' PDF.

Counts: blockers 0, should fix 1, polish 3, nit 2.

#### What was checked and holds up

- **No real group is named or stereotyped on screen.** Rooms are numbers with a badge shape and color. Narration and
  hints never name a country, language or people (spec Voice: "Narration never names a real place or group of
  people"; confirmed in all 58 lines). The only real-world framing on screen is the Room 9 viewer line "Lots of
  people learn to write 1 with a long flag and 7 with a line through it.", which is accurate and normalizing.
- **No one way of writing is called wrong.** Mix-ups read "Room 9: wrote 1, got tacos", putting the error on Bitsy,
  not the writer. "Right lunch = Bitsy reads the written number correctly." defines correctness as the robot's job.
  The 0 / 15 / 0 run moves the harm onto Room 12 and Room 3 ("Now a different room is getting the wrong lunch."),
  which shows the symmetry: the plain style is not the "right" one either. Room 3 (big, wobbly writing) scores 10,
  and the notes use it to counter the "messy writing" explanation. Good.
- **No one is blamed.** Room 12 "built Bitsy ... with their own handwriting"; nothing calls that careless or mean.
  The fix is inclusion ("whose examples they are"), not punishment.
- **Numeral-style fact.** A long-upstroke 1 and a crossed 7 are common in much of continental Europe and Latin
  America (the cited Wikipedia section agrees). Stated only in the spec and linked in the notes; fine.
- **Gender Shades is accurate.** Buolamwini and Gebru, "Gender Shades: Intersectional Accuracy Disparities in
  Commercial Gender Classification", PMLR 81:77-91 (FAT* 2018). Three commercial gender classifiers (Microsoft, IBM,
  Face++) were tested on a new benchmark balanced by skin type and gender (Pilot Parliaments Benchmark, 1,270
  parliamentarians); darker-skinned women had the highest error, up to 34.7%, against at most 0.8% for
  lighter-skinned men. The notes' summary ("commercial gender classification systems ... highest error rates for
  darker-skinned women"; "the tested task was binary gender classification, not a test of every form of face
  recognition"; the lesson is to check results by group, not only an overall average) is correct and carefully
  scoped. It is marked teacher background only and is not in the scene or narration. Appropriate for grade 4
  teacher notes.
- **Rule 8.** Notes carry a "Sensitive context and sources" section. Rule 6: no unsafe language. Rule 7: privacy is
  stated on screen ("Your drawing stays on this device...") and in the notes.
- **People in art.** One asset, `cafeteria-counter`; the prompt has no people and the spec says "people no". Nothing
  is marked `people: true` and nothing needs to be.

#### Findings

**SE1. should fix, general. The normalizing line is easy to miss, so a student's first and only view of Room 9's
style can be as the cause of wrong lunches.** (src.html `openViewer`, line 117; hint/voice `L.under`; notes "A
5-minute start" step 3.) The one on-screen statement that the flag 1 is a normal way to write ("Lots of people
learn...") shows only in the Room 9 jar viewer and only when that jar has cards. At the start it is empty, so the
post-run prompt "Tap a room's jar to see how its students write." leads to "This jar has no training cards yet."
(same root cause as teaching S1). A student who writes a flagged 1, often one who learned to write in another
country or from family, sees "Room 9: wrote 1, got tacos" four times and nothing that says their way is ordinary.
Better: when S1 is fixed, keep the framing line on whatever view shows Room 9's writing first (for example the empty
jar viewer showing Room 9's lunch cards: "Room 9's lunch cards. Lots of people learn to write 1 with a long flag
and 7 with a line through it. Bitsy has none of these in its jar."). Optionally add it once to the post-run Mix-ups
area when Room 9 has misses: "Room 9's 1s are written a common way Bitsy never saw."

**SE2. polish, general. Notes: tell the teacher who in the class may write like Room 9, and not to call them out.**
(notes "Sensitive context and sources", paragraph 1.) The notes say "Do not ask a child to represent an entire real
group" but don't say where the style comes from, so a teacher may not anticipate that newcomer or multilingual
students, or students taught by family from Europe or Latin America, write their 1s this way. Better, add: "The
long-flag 1 and crossed 7 are standard in much of Europe and Latin America, so some students in your class may write
them. In Try Your Writing, invite anyone who writes a different way to teach Bitsy, but don't ask who writes like
Room 9 or single a student out. Treat their style as a skill the robot lacked."

**SE3. polish, general. Notes: give the Gender Shades numbers and link so a teacher can check them.** (notes
"Sensitive context", paragraph 2, and the source bullet.) The summary is right but unquantified and unlinked.
Better: "...examined three commercial gender classification systems (2018) and found error rates up to 34.7% for
darker-skinned women, against at most 0.8% for lighter-skinned men." Source bullet: add "pages 77-91,
https://proceedings.mlr.press/v81/buolamwini18a.html".

**SE4. polish, general. Notes: state the symmetry as the respect point, not only the technical one.** (notes "Talk
about it", bullet 5.) The 0 / 15 / 0 run is the clearest evidence that neither style is wrong, but the bullet frames
it only as harm moving. Better, append: "Does that mean Room 12 writes wrong now? What does that tell you about
whose writing was ever 'wrong'?"

**SE5. nit, general. Spec Sources overstates what Gender Shades showed.** (spec.md "Sources", bullet 2.) It is cited
for "How unrepresentative training data makes a model fail for some groups". The paper measured accuracy gaps by
group and showed common benchmarks were skewed toward lighter-skinned faces; it could not see the vendors' training
data. The notes already scope it correctly. Better: "Buolamwini and Gebru ... for the teacher notes only: measured
accuracy gaps by skin type and gender in commercial classifiers."

**SE6. nit, general. Art prompt does not say "no people".** (art/prompts.json `cafeteria-counter`.) A cafeteria
scene can pull in lunch staff. Local models never draw people, so add "no people, empty counter" to the prompt and
`"people": false` to the entry so a regenerate can't slip one in. (The spec names Cloudflare FLUX.2 while the entry
says flux1-schnell local; the art lens should settle which.)

#### Sources

- [PMLR 81: Gender Shades](https://proceedings.mlr.press/v81/buolamwini18a.html)
- [Authors' PDF copy](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS089/PDF_files/Gebru_18.pdf)
- [MIT Media Lab publication page](https://www.media.mit.edu/publications/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/)
- [University at Buffalo summary (vendors named)](https://www.buffalo.edu/catt/ai-resources/ai-in-practice/the-dataset-doesnt-lie.html)

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: biased-bot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json; bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot` (177 KB). Audit first (`scripts/audit_tool.py`, ports
9960-9961), then `scripts/drive.py` with held clicks and real pad drags on port 9962, own profile. Numbers recomputed
in Python from the spec alone (own mulberry32, templates, card generation, 32 by 32 rasterizer, k = 3 vote with
position tie-break; a reversed training order gives the same table). Scratch: lens-bb-teaching (calc.py, sweep.py over
all 1330 jar settings, pad.py; frames f1 to f7, audit/).

Counts: blockers 0, should fix 4 (general 3, family 1), polish 2 (general 2), nit 2 (general 2).

#### Standards (rule 2)

Module computer-science-4-training-data-matters: "How training data shapes what an ML model outputs".

- **E4-ALG-ML-02**: taught by doing. The student changes whose cards are in the jars, presses Train Bitsy and reruns
  the same 30 cards; the room bars and Mix-ups show what changed. Taught, but S2 lets a solo student skip the "more of
  the same does nothing" half.
- **E4-SOC-HU-18**: taught. The bars are split by room, so the student sees the harm land on Room 9 and fixes it by
  including Room 9's writing; 0 / 15 / 0 lets a solo student move the harm onto the other rooms (line 7 plays). S1
  weakens the "look at how they write" step.
- **E4-DAT-IM-11**: taught by the controlled comparisons (same test cards, one jar changed per run, results by group).
  The "predict" half exists only as hint text with nothing to commit to (P1).
- **E3-ALG-ML-02**: taught in Try Your Writing: label your own drawing, Bitsy retrains, the look-alikes and later reads
  change. Real, but S3 makes the first try look like it did nothing.
- CSTA crosswalk and AI4K12 are reference only; 1B-DA-07 has the same gap as P1.

No code is only mentioned; none needs to move.

#### Done when

| # | Result | How checked |
|---|---|---|
| 1 | pass | held Run, Skip: 10 / 10 / 6; Mix-ups "Room 9: wrote 1, got tacos (4), 4 cards" (one row with its count, as the spec's panel describes); Python: four Room 9 1s read as 4 (f1 dw1-run) |
| 2 | pass | 30 / 0 / 0 retrained: 10 / 10 / 6; vlog: three results, "under", then "More cards from the same rooms did not help Room 9." spoken (f5 v2-same) |
| 3 | pass | Room 9 at 3: 10 / 10 / 6, no "all" line; at 6: 10 / 10 / 10 and "Every room got the right lunch..." spoken (f6) |
| 4 | pass | 0 / 15 / 0: 6 / 6 / 10, eight 1s read as 7 (salad), "Now a different room is getting the wrong lunch." spoken (f5 v4-flip) |
| 5 | pass | More Room 3 after a run: Run aria-disabled, "Old results. Train Bitsy, then run again.", box greyed (f1 dw5-old) |
| 6 | pass, see S3 | real drag of a stick 1: "Bitsy reads: 1", 16 ink cells, three Room 12 look-alikes with badges (f7 w1-stick). Flag 1 drag reads 4; It's a 1 once: still 4; twice: 1, look-alikes My cards, My cards, Room 12 (f7 w2-flag) |
| 7 | pass | grayscale frames: circle / square / triangle plus "Room N" on jars, bars, cards and viewer (f1 dw7-gray, dw7-gray-bars) |
| 8 | pass | audit frames 680x425, 1366x768, 760x900 and 375x812 host: Run, Train Bitsy and all six jar buttons above the fold |

#### Facts and numbers

All eight rows of the spec's checked table and the notes' table match my Python exactly, including the notes' mix-up
detail ("Room 9 loses two 1s to 4 and three 4s to 1" at 3 / 0 / 0; four 1s per other room read as 7 at 0 / 15 / 0).
Results do not depend on training order. Two My cards labelled 1 (flag style) also fix Room 9 in the lunch line
(10 / 10 / 10), which the tool shows correctly (f7 w3-flag-run). The Gender Shades citation and summary (highest error
for darker-skinned women, binary gender classification, PMLR 81, 2018) are right; the numeral-style claim matches the
cited Wikipedia section; the screen names no real place or group.

#### Findings

**S1. should fix, general. "Tap a room's jar to see how its students write" leads to an empty jar.**
(src.html `L.under`, `openViewer`; notes "A 5-minute start" step 3.) After the first run the voice and hint say to tap
a room's jar, and notes step 3 says "Tap the Room 9 jar. Compare its 1 with Room 12's 1." But Room 9's jar starts at
0, so the viewer says "This jar has no training cards yet." and "This jar is empty. Press Close, then More to add
cards." (f1 dw1-under-jar9). The key framing line ("Lots of people learn to write 1 with a long flag...") only shows
once Room 9 has jar cards, so a student who looks first, as told, never sees it. Same after 0 / 15 / 0: the rooms now
getting wrong lunches are the empty jars. Better: an empty jar's viewer shows that room's 10 lunch-line cards ("Room
9's lunch cards. Bitsy has none of these in its jar.") with the framing line for Room 9; or point the line at the lunch
cards on the stage. Fix notes step 3 to match.

**S2. should fix, general. After a run the hint does not name the next experiment.** (src.html `nextHint` -> 'ready'.)
After every run the hint goes back to "Press Run the lunch line. Predict how many right lunches each room will get."
(f1 dw1-run), that is, rerun the same jars, which teaches nothing. The tool's one idea is the contrast: more Room 12
cards change nothing, a few Room 9 cards fix it. A solo student (rule 4) who goes straight to Room 9 never meets the
first half; line 5 only plays if they happen to add Room 12 or Room 3 cards first. Better: a post-run hint when a room
is under 10 that names the experiment and the control, e.g. "Room 9 got wrong lunches. Press More under Room 12. Will
more of the same cards help?", then after that run "Now try More under Room 9." (how lines, once each, `V.heard`).

**S3. should fix, family:ml-lab. The first "Teach Bitsy my way" visibly does nothing, with no reason given.**
(src.html `teach`, hint 'taught'.) A flag-style 1 reads 4; It's a 1 once, then Bitsy, read it!: still 4, because the
student's card is one of three votes against two Room 12 4s (Python: 200 of 200 fresh flag-1 drawings still read 4
after one taught card; 200 of 200 read 1 after two). The screen says "Bitsy learned your card." and then gets it wrong
again; a grade 4 student concludes teaching is broken. Only the teacher notes explain it. Better: after a teach that
does not flip the read, show the vote in the look-alikes ("Your card is 1 of the 3 look-alikes. Bitsy goes with the
most votes. Teach one more.") so the k = 3 vote becomes part of what E3-ALG-ML-02 teaches. Family lesson: any k > 1
tool needs the vote visible when one example can't win it.

**S4. should fix, general. "Bitsy learned from everyone" is false in the state that triggers it.** (src.html `L.all`,
spec voice line 6.) Done-when 3 reaches all 10s at 15 / 6 / 0, with Room 3's jar empty. Two My cards also trigger it
with no Room 9 cards at all (f7 w3). The table's point is that Room 3 needed no cards of its own because it writes the
same shapes; "learned from everyone" teaches the opposite. Better: "Every room got the right lunch. Bitsy has now seen
every way these numbers are written." (lines.json and the clip change with it).

**P1. polish, general (spec open question). The predict step has nothing to commit to.** Hint 'ready' says "Predict
how many right lunches each room will get", but a solo student can't record a guess, so the prediction half of
E4-DAT-IM-11 / 1B-DA-07 lives only in a teacher question. A quick guess per room, shown beside the bars after the run,
would make it something the student does. It adds a control, so it goes to the spec's open questions.

**P2. polish, general. The "one Room 9 card is not enough, two are" talk point needs its condition.** (notes Talk
about it, bullet 4; spec talk points.) True with Room 12 at 15 and Room 3 at 0, but the sweep finds all 10s with one
Room 9 card of each digit (6 / 3 / 6, 3 / 3 / 9, 0 / 3 / 9), and 3 / 6 / 0 hurts Room 12 (8) and Room 3 (7). Say "with
Room 12 at 15 and the other jars empty" in the notes so a teacher isn't caught out by a pair that found one of these.

**N1. nit, general. The empty-jar viewer says the same thing twice** ("This jar has no training cards yet." and "This
jar is empty. Press Close, then More to add cards.", f1 dw1-under-jar9). Moot if S1 is fixed.

**N2. nit, general. Teaching a card also trains untrained jar changes.** `teach` retrains on `state.counts` and clears
`dirty`, so jar changes made without Train Bitsy get trained silently from the writing mode. Use `state.trained`.

#### Giveaways, language, guardrails

- No hidden-information or quiz mode; nothing before a run shows its result. Badges are drawn but never features
  (features are the 64 cells only). Nothing to solve by sweeping; the sweep is the activity.
- Language is plain grade 4 on screen ("Right lunch = Bitsy reads the written number correctly."). Notes name the
  sensitive context (rule 8).
- Grade 4: no K-2 or hard-history guardrails apply.

#### For the sensitivity agent (rule 5, not judged here)

Room 9 stands in for people who learned a different numeral style (the cited source ties it to much of Europe and
Latin America), and the tool's arc is a group harmed by being left out of the data. Notes also carry the Gender Shades
parallel (skin tone and gender). Worth a fresh sensitivity read of the Room 9 framing and that teacher note.

#### Audit pilot

- Confirmed: sizes clean at all eight sizes (my Done-when 8 check agrees), Motion off clean, and the held-click walk's
  spoken lines (jar clicks speak 'inspect' / 'inspectEmpty', More / Fewer speak 'change').
- Wrong: all 11 leads at 375x812 are false. They are panel content scrolled out of view inside the 350 px
  `overflow:auto` panel (result label, bars, notes) counted as overlapping the stage text below it.
- Missed (all teaching, all past one click): the empty Room 9 jar behind the post-run line (S1; the walk logged
  "This jar is empty" for #jar-9 with no way to judge it), the post-run hint (S2), the first teach doing nothing (S3),
  the false "learned from everyone" (S4), every number, and whether the Done-when lines play (needs multi-run
  sequences).
- Tooling note: in my drive.py runs a shot's `"wait"` did not let page timers run (a real Run click, then a 31 s
  `wait`: 0 of 30 cards done, and the result lines looked stuck after the first). Awaiting inside the `"after"` JS
  worked. Voice counts taken across a `"wait"` should be read with care.

<!-- end part -->

## Fix

<!-- part: polish.md -->

Curio Class Biased Bot polish, 2026-10-28. Rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`: 188 KB. Evidence: [handoff](handoff.md), [validation](polish-checks/validation.json), [evidence map](polish-checks/evidence.md). All eight Done-when requirements pass at 1366x768, 680x425, 800x500, 375x812 and 1920x1080; 55 matrix cases plus targeted interactions and final pointer checks, with no browser console errors.

1. Every room viewer now shows its ten lunch cards separately from training cards, including Room 9's handwriting-normalization sentence at zero cards; opened the initial Room 9 and Room 3 viewers and inspected their cards and captions.
2. Hints follow the experiment state and V.heard: inspect Room 9, try more Room 12, then include Room 9; drove run, viewer open/close, More, Train and another run, checking guide-after-view and guide-after-same logs and frames.
3. Teaching refreshes the actual three nearest votes and explains a losing one-of-three vote; drove a flagged 1 through read 4, first teach still 4, second teach 1 at every size, with My cards highlighted; documented the tool-owned vote view in the family docs.
4. Success says only that every room got the right lunch this time, with the three-room training claim guarded separately; changed spec line 6 and drove both 15/6/0 and 15/15/15 runs, verifying the all and represented voice logs.
5. The first Run tap preserves the story and then the running instruction through welcomeAfter; drove a cold Run through its full duration and checked spoken order and timing. Recorded clips are absent, so this checks draft scheduling rather than recorded-audio quality.
6. A Room 9-first stage score strip stays visible while detailed bars remain in the panel; drove completed and old-result runs and inspected all five sizes, including the phone host.
7. Compact writing keeps the pad and ink grid side by side and places all three votes below them; drove actual pointer reads at all five sizes and inspected final taught layouts at 680x425 and 375x812, including the privacy line.
8. Fewer and More use aria-disabled with guarded handlers; repeatedly clicked to 0 and 30 and confirmed the focused button stayed active, aria-disabled was true and native disabled was false.
9. Selecting the current mode returns before hush; re-tapped Lunch Line during its welcome and checked that the story and subsequent action remained in the voice log.
10. Engine hosts defer zero-size drawing and redraw at the next real size; groupBars clamps widths and adds optional empty and numeric size settings while preserving defaults; updated docs/families/ml-lab.md, removed parking/font overrides, and drove hidden/show/narrow-width checks. Bundled both requested siblings before and after: teach-the-robot predictions match, three final frames are pixel identical, and the compact frame differs by only 18 text pixels with unchanged layout. leaf-sorter-ai has only spec.md, so bundling yields no page and its requested frame/behavior comparison could not be done.
11. Teaching identifies My cards through its count, highlighted vote, hint and receipt where space permits; drove first and second teaches and checked the destination feedback. Also confirmed a pending room-jar edit remains untrained after teaching.
12. Removed the repeated empty-jar sentence; opened the final zero-card Room 9 viewer and checked its single count statement plus distinct More instruction.
13. Qualified the one-versus-two Room 9 example claim with Room 12 at 15 and Room 3 at 0 in notes.md; checked the wording and drove the matching 3-card and 6-card runs at all five sizes.
14. Notes describe long-flag 1 as standard in much of Europe and Latin America, invite anyone to teach their writing and prohibit singling out students; checked the notes and the neutral Room 9 viewer shown in the driven flow.
15. Notes now give Gender Shades errors up to 34.7% versus at most 0.8%, PMLR 81 pages 77-91 and the paper link; checked the exact text and confirmed the student scene and voice inventory keep this teacher context out.
16. Added the Room 12 respect question to notes.md; drove the 0/15/0 result showing 6/6/10 and eight 1-to-7 mistakes, then checked that the question matches that experiment.
17. Spec Sources now distinguish measured group gaps from unavailable company training data; checked the exact source wording and confirmed the existing Open questions section is byte-for-byte unchanged after text decoding.
18. Cafeteria metadata now says Empty counter, no people and people:false; parsed the JSON and inspected the unchanged illustration in the driven lunch frames.
19. Moved the tray and enlarged Wanted sticker beside Bitsy's full hull and made Fewer a single nonwrapping word; drove mid-run mistakes at 680 and 1366 and inspected their tray, sticker and jar controls.
20. Applied the other chosen student-facing Play polish, listed in handoff.md: story/action order, teaching event first, clear mix-up wording, persistent queue marks, larger badges/captions, proportional art, writing Bitsy, moving room label and keyboard-only pen ring; drove and inspected matrix, mid-run, keyboard, pointer and projection cases. Independent Python reproduces all eight table rows and every misread; JavaScript syntax checks pass; voice/lines.json exactly equals allLines() at 69 lines.
Settled call: Changed spec line 4 and runtime guidance to Pick the cards, then press Train Bitsy; the writing welcome prompts drawing before Read, with Read guidance after ink exists; drove dirty jars, empty jars and a real keyboard stroke to verify enabled next steps. No new open questions; the review's Spec open questions remain untouched.

Automatic approval review rejected temporary Chrome profile cleanup with the reason blocked by policy. Those folders remain under polish-checks/; the host and test browsers have stopped. The generated teach-the-robot bundle from the requested sibling check remains available; its source is unchanged. Review files were not edited and no git commands were run.

#### Round 2

Curio Class verification evidence, screenshots, scripts and retained Chrome profile: `%TEMP%\curio-class-biased-bot-round2-20261028-153305`. All 27 driven frame cases passed with no browser console errors; every frame was inspected. Rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py biased-bot`: 189 KB, identical to the tested bundle. The 70 voice inventory lines exactly equal live `allLines()`. No new open questions; review files, kit files and existing spec open questions are unchanged.

21. Added a Room 9-specific hint whenever it has training cards but still scores below 8; kept includeHow for the other-room experiment and named Room 12 or Room 3 explicitly; updated the spec and voice inventory. Drove 15/3/0 and 15/3/3 at all five review sizes, then followed More under Room 9, Train and Run to 10/10/10; drove 0/15/0 and confirmed the other-room instruction and improvement after adding Room 12 cards.
22. Event feedback now uses the existing voice API to cut a playing instructional line without clearing the hint, while preserving queued events and explicit Read priority; documented this in the spec. With a real pointer-drawn flagged 1 and held clicks, read and teach events began 2 ms after their clicks, a later teach cut the taught instruction in 1 ms, all five teaching events played, and an event waited for an explicitly requested Read. Screenshots and voice logs are retained outside the repo; these are draft timing checks, not a listening review of recorded clips.
23. Added `MLLab.glyph` and `train('knn')` to the biased-bot family row. During the driven More, Train, Run and Skip flow, runtime wrappers counted 122 glyph calls and one knn training call in the sampled case; all eight existing results-table rows still match. JavaScript syntax and the voice inventory equality check pass.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

Curio Class Biased Bot polish handoff, 2026-10-28.

The accepted Play polish in item 20 is implemented as follows: the premise precedes the short action prompt; same/flip/all teaching events lead the three fixed room totals; mix-ups say how many cards wrote which number and received which food; queue cards retain served ticks or crosses; room badges are 14 pixels; large result captions scale for projection; cafeteria art uses proportional cover cropping with menu placement derived from the original image; a small Bitsy displays the writing guess; the feeding card's room label moves with the card; the keyboard pen ring appears only after keyboard input. The tray and larger Wanted sticker sit beside Bitsy's full hull, with a soft kit cue for a mistake. Detailed result bars remain available, while the stage totals stay visible in compact views.

Teaching immediately refreshes the actual three votes and highlights My cards. It uses the last trained room jars, preserving pending jar changes until Train Bitsy. In the shortest landscape view the separate receipt is hidden to keep the privacy line visible; the My cards count, highlighted vote and hint still show the destination. The classifier, seeds, rasterizer and dataset were not changed.

Verification evidence is in polish-checks/. All eight Done-when requirements passed at 1366x768, 680x425, 800x500, 375x812 and 1920x1080. The matrix has 55 driven cases, including one-teach and two-teach states. A final real pointer stroke was read correctly at every size; a real keyboard stroke, focus at jar limits, repeated current-mode clicks, viewer navigation, pending training, voice ordering, motion timing and hidden engine hosts were also driven. Screenshots were inspected directly and in labeled contact sheets. The final compact teaching frames supersede the earlier receipt-clipping frames; the final projection frames supersede the earlier label-spacing frames.

The current draft bundle is 188 KB. Its 69 voice inventory lines exactly equal the browser's allLines(). No recorded voice clips are present in this checkout: narration checks use the draft voice scheduler and its spoken/queued log, not a listening review of recordings. No voice service was called. No console errors occurred in the matrix, interaction, final, projection or sibling driver runs.

Item 10 sibling comparison: teach-the-robot was bundled before and after the engine change. Its initial 1366 frame and six-card and sixteen-card frames are pixel identical. At 680 only 18 pixels in two button text glyphs differ; layout is unchanged. Predictions for all ten parade pets match before and after both trained states. The requested generated sibling bundle remains available. leaf-sorter-ai contains only spec.md; both requested bundle attempts produced no runnable page, so its frame and behavior comparison could not be performed. Its source was left alone.

The review files and the spec's Open questions section were left unchanged. No new product or specification question was introduced. The missing leaf-sorter-ai fixture remains a verification limitation. Automatic approval review blocked deletion of the temporary Chrome profile folders with the reason "blocked by policy"; those folders remain under polish-checks/. The local host and test browsers have stopped.

<!-- end part -->

## Log

- 2026-11-25: CODEX-BRIEF.md folded in (last changed 2026-10-28)
- 2026-11-25: codex-report.md folded in (last changed 2026-10-28)
- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/sensitivity.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: polish.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
