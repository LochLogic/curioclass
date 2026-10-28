# Codex build brief: biased-bot (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real fourth graders tomorrow.

The tool is `biased-bot`. Its spec is `tools/biased-bot/spec.md`. **Read the spec fully, every line, before you
write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong or
impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

## 0. Ground rules for this run

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

## 1. Read these, in this order

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

## 2. The rules you must follow (quoted from the docs above)

### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Images use `art:<name>` tokens only for names in prompts.json." (The only one here: `art:cafeteria-counter`.)
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 4: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool = {state, setMode, allLines, ...}` "so frames can be checked". Also expose the voice log
  (`vlog: V.log`, `get vq() { return V.queue; }`) as teach-the-robot does, and whatever a tester needs to read the
  current jars, results and pad grid.

### From TOOL-CONTRACT.md "The HTML file must"
1. "Be one file. All CSS, JS, data, images and fonts are inline."
2. "Make no automatic network requests. No external `src=`, stylesheets, `@import`, `url(http...)` or fonts."
3. "Collect nothing. No analytics or cookies. `localStorage` only for per-device conveniences ... wrapped in try/catch."
4. "Have `<html lang>`, `<meta charset>`, `<meta name=\"viewport\">`, a `<title>` and a `<meta name=\"description\">`."
5. "Stay under 2 MB."
6. "Work embedded and full screen. It must be usable in a 16:10 iframe on the tool page and fill the window when opened alone."
Plus: Motion button in the header, `prefers-reduced-motion` as the starting point, "Turning motion off removes
movement only: story pacing and timers stay the same". Credit sources and licenses in a comment near the top.

### From BASELINE.md (the owner's rules that apply here)
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

### From STANDARDS.md "Sizes" (check every one, early)
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

### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
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

### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." The run is 0.9 s per card with Motion on or off.
- "Nothing overlaps by accident." "Test the extremes": jars at 0 and 30, My cards with many cards, all three rooms
  at 30, the shortest and narrowest boxes.
- "Words match the state. Grammar, counts, plurals." ("1 card", "3 cards"; "1 of 10 right lunches".)
- "Nothing on screen gives the answer away."
- "Keep the action area clear": the menu text is drawn in code over the blank green board in the art; check it lands
  on the board at every size.

## 3. The engine (use it, do not rewrite it)

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

## 4. Files to make in `tools/biased-bot/`

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

## 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex`)

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

## 6. Self-check list before you report (BUILD.md "Wave lessons (BR1)", turned into checks)

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

## 7. Report: write `tools/biased-bot/codex-report.md`

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
