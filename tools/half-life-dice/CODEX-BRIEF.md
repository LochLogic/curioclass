# Codex build brief: half-life-dice (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real tenth-grade chemistry students tomorrow.

The tool is `half-life-dice`. Its spec is `tools/half-life-dice/spec.md`. **Read the spec fully, every line, before
you write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong or
impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

## 0. Ground rules for this run

- **You may write only inside `tools/half-life-dice/`.** Nothing else in the repo. Not `kit/`, not `docs/`, not
  `scripts/`, not other tools.
- If you believe `kit/graphing.js` or `docs/families/graphing.md` must change (a bug, a missing feature), do NOT
  change them. List the change in `tools/half-life-dice/handoff.md` under a heading `## Engine changes wanted`: the
  file, the function, what is wrong, the exact change, and why the tool needs it. Then work around it inside the tool,
  and say how. The integrator approves or declines engine changes later. Ten live tools load graphing.js.
- The spec has no art: dice, nuclei, counter and ruler are drawn in code (SVG or canvas). Do not draw, generate or
  download any image. Do not record voice.
- No git commits, no branch changes, no stash. Leave the work as uncommitted files.
- The tool makes no network requests of any kind. You need no internet for this job.
- **Scratch space: `S:/CurioClass-codex-scratch/half-life-dice/` (writable).** Every screenshot, Chrome profile,
  shots file, audit output and temporary script goes there (or %TEMP%), **never in the repo or the tool folder**. Your
  sandbox cannot delete files afterwards, so anything you leave in the tool folder stays.
- Ports: Chrome debugging ports **9980 to 9987 only**; the iframe host server on **8796 only**. Other agents use
  other ports on this machine at the same time.
- Every Chrome you start uses `--mute-audio` (drive.py does this for you). **Close every Chrome and server you start
  before you finish**, and say in the report that you did. The last build left 18 headless Chromes running.
- The scripts now work in your sandbox as they are: drive.py and audit_tool.py fall back to `scripts/cdp_ws.py` when
  `websockets` is not importable, drive.py retries Chrome with `--in-process-gpu --no-sandbox` by itself, and
  audit_tool.py takes `--host-port`. You should not need any workaround; if you do, say what and why in the report.
- **Start `codex-report.md` early** (the section headings from section 7 as soon as you begin) and fill each section
  as its checks finish. The last build lost its connection minutes before writing a report it had left to the end.
  **Keep the report under 200 lines** (the last one ran to 1406).

## 1. Read these, in this order

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice behavior, testing). Where anything differs, it wins.
1. `tools/half-life-dice/spec.md`: everything you build. Read all of it.
2. `docs/agents/BUILD.md`: the build agent brief (the human-agent version of this file), including `audit-states.json`
   and both lesson lists at the end.
3. `docs/agents/decisions/BASELINE.md`: the owner's standing decisions.
4. `docs/TOOL-CONTRACT.md`, `docs/KIT.md` (above all the "Voice: Curio.voice" section), `docs/POLISH.md`.
5. `kit/starter/src.html`: start from a copy of it. Also skim `kit/curio.js`, `kit/curio.css` and `kit/theme-912.css`
   so you use them instead of re-implementing anything.
6. `docs/families/graphing.md` and `kit/graphing.js` (read the whole engine): `Plane`, `g.point`, `g.fn`,
   `g.segment`, `g.label`, `g.view`, the series colors and dashes, `Plane.fmt`.
7. **The quality bar, two tools:**
   - `tools/outbreak-model/` (`src.html`, `spec.md`, `notes.md`, `exit.md`, `voice/lines.json`): a grade 9-12 tool
     on the same graphing engine with an exponential curve, already through review. See how it uses the plane at
     real pixel size per layout and how its graph stays readable at 680x425.
   - `tools/biased-bot/` (`src.html`, `refine.md`, `polish.md`, `voice/lines.json`): built by you (Codex) in the last
     wave and through the current review process; its `refine.md` shows what the lenses catch and its polish what
     was fixed. It uses `Curio.voice` the way this tool must.
   Do not copy either one's look, scene, voice or palette: half-life-dice has its own (lab-glow green, the
   curious-librarian voice, a dice tray, nuclei and a Geiger counter).
8. Formats: `tools/shape-talk/notes.md` (teacher notes); an example states file at
   `S:/CurioClass-codex-scratch/half-life-dice/example-audit-states.json` (from another tool; the format is in the
   header of `scripts/audit_tool.py`).
9. The element table: `tools/elements-inspector/elements-inspector.html` has `const ELEMENTS = [...]`. Copy only
   atomic number, symbol and name for Z 1 to 94 (the spec: "symbol and name by atomic number only").

## 2. The rules you must follow (quoted from the docs above)

### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 10: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool` with everything the spec lists (`state, setMode, die(kind), roll(n), seed(s), card(id),
  setProduct(A, Z), check(), sample(id), noise(on)`) plus `allLines`, the voice log (`vlog: V.log`,
  `get vq() { return V.queue; }`) and whatever a tester needs to read the tray count, the graph points, the tracked
  die, the card result, the ladder and the dating result.

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
- Rule 2: "Every standard is taught well, above the minimum." HS-PS1-8 is the module code: changes in the nucleus
  (Nucleus mode, the balanced equation built by the student), the energy released in fission, fusion and decay (the
  energy ladder), and decay over time (Roll and Dating lab). Each part must be taught by something a student does,
  not only by a sentence. The heart of Roll is "a die never remembers how long it waited, yet the crowd halves on a
  schedule": the student must see both, side by side.
- Rule 4: "Every tool stands alone. ... Defaults must work for a solo user; teacher toggles are extras."
- Rule 7: privacy is stated wherever anything is recorded or stored. Progress is saved on this device
  (`curio-half-life-dice`): say so in the panel where Clear is, in plain words ("Saved on this device only").
- Rule 5: facts stay plain, with care for the people involved. The real samples (the Dead Sea Scrolls, seeds from
  Tutankhamun's tomb) and the medical isotopes (thyroid treatment, radiation therapy, PET scans) are named plainly and
  respectfully, from the spec's sources only.

### The spec's open question
The spec asks Cory whether to keep 5,730 years (OpenStax) or switch to 5,700 (NNDC). **Build with 5,730**, as the
spec's Content and Done-when numbers do, and keep the NNDC value where the spec already shows it. Do not decide the
question; it stays in the spec for the owner.

### From STANDARDS.md "Sizes" (check every one, early)
| Size | Why |
|---|---|
| 680x425, 800x500, 1000x625 | the site's 16:10 preview on the tool page |
| 1280x720, **1366x768** | the main use: a school laptop, full screen |
| 1920x1080 | big screens |
| 760 wide | below the 1000 px stack breakpoint (check 760x900) |
| 375 wide | phones, inside an iframe host (`python scripts/drive.py half-life-dice --host 8796`) |
- "The main controls (the ones a student uses every few seconds) are visible without scrolling at every size. In short
  landscape boxes keep stage and panel side by side with a compact panel instead of stacking." Here: the die picker,
  Roll once, Roll to 10, Reset, the steppers and Check, the sample shelf, Estimate and Calculate.
- "The preview must be readable (scene text about 10 px or more)." The graph's tick labels and the equation's small
  mass and charge numbers are the risk: at 680x425 they must still read. A 1,000-die tray at 680x425 has tiny
  squares: say on screen what they are (the live summary "640 left after 2 rolls") and keep the decayed mark legible
  (gray plus a small x, never color alone).
- "Draw the stage at real pixel size and re-lay it out per size ... rather than scaling one fixed design." Give the
  Plane its real `width`/`height` per layout.
- "Moving focus on purpose uses `focus({preventScroll: true})`."
- "Fit-to-width guards ... re-measure from the loosest step every time and wait for running animations to finish first."
- **Resizing in the middle of an animation** (a roll's 0.4 s face animation, a `g.view`, Average 20 runs, the Geiger
  count) must not throw or leave anything disabled. The audit now resizes after every input; the last build failed
  this.

### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
- Narrate only through `Curio.voice` (`V.how` for how-to lines, `V.say` for events, with `valid` and `needs`). Never
  write your own queue. `scope: () => state.mode`.
- One welcome per mode (wRoll, wNucleus, wDating). **This tool has three modes: do not use `welcomeAfter`** (it is
  for one-mode tools; in the last build it made the welcome play late, after the first tap's own line).
- "Say how to act. Whenever the tool waits for the student, the line and the hint name the next action and the control."
- "But don't nag. A how-to line is spoken the first time its step comes up; after that it only updates the hint, silently."
- "How-to and teaching lines are spoken once per page load. Event lines ... are spoken every time their event happens,
  and are still dropped when stale. ... Keep an explicit set of event line ids in the code." Here the event line is
  tooOld (stale on the next sample). If you add a line the spec does not give (for example a Check result), write it
  as a hint first; add a spoken line only if the spec's Voice section implies it, and list every line you added in
  handoff.md.
- "The spoken line matches the state on screen."
- "The hint changes when the state changes. On a tab, panel or mode switch, set the hint at once, then queue the line
  with a `valid` check ... Pick how lines by `V.heard`, never by a counter. The first action never waits behind a line,
  no line names a disabled control, and at a 2 s tap pace no line is lost."
- "Test with held clicks (press, ~120 ms, release)" and read `V.log` to see which clips actually started.
- Spoken text must exactly match a line in `voice/lines.json` so recordings can replace the browser voice later.
  Lines under about 200 characters, nothing a voice would misread (write "carbon-14", never "C-14" or "¹⁴C" in a
  spoken line; numbers a voice reads well).

### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." The roll's 0.4 s, Average 20 runs, the Geiger count time: same with
  Motion off; only the animation goes.
- "Nothing overlaps by accident." "Test the extremes": a coin tray at roll 10 (about 1 left) and a d20 tray at roll 10
  (about 599 left), Average 20 runs on top of a single run, the marked half-life line with its card, every Nucleus
  card with both steppers at their extremes (A 240, Z 94 and Z -1), F1's three products, the ladder with all four
  rungs, the deep core sample with Counting noise on.
- "Words match the state. Grammar, counts, plurals." ("1 roll", "2 rolls", "Rolls survived: 1".)
- "Nothing on screen gives the answer away." The steppers must not start at the right values; Check names which sum
  is off, never the answer; the ruler must not mark the sample's age before Estimate.

## 3. The engine (use it, do not rewrite it)

`<script src="kit:graphing"></script>` after `kit:curio`. It defines `Plane`. Use it for the decay graph (axes,
observed points, the expected curve `g.fn` dashed, the 20-run mean, the draggable half-life line via `g.point` or
`g.segment` with keyboard support) and, if it fits, the halving ruler. Read the family doc's notes on `ticks`,
`tickFormat`, series colors (`color: 1..4` also sets a dash, so color is never the only signal), clamping and
`g.view`. The dice tray, the nuclei and the counter are the tool's own SVG or canvas.

The seeded generator is the tool's own (mulberry32, as the spec says). **Check the spec's numbers in Node in the
scratch folder before you build** (half-lives in rolls for all seven dice, expected counts after 10 rolls, the dating
ages, the noise range at 340 counts, the energy ratio). If your numbers differ, trust the computation, say exactly what
differs in handoff.md and codex-report.md, and do not change the spec.

Never write a literal closing script tag inside your inline script, even in a comment.

## 4. Files to make in `tools/half-life-dice/`

From BUILD.md "Make these files":
- `src.html` from the starter: the kit stylesheet and script (`kit:theme-912` as outbreak-model does, if it fits the
  spec's look), the tool's palette (the spec's Look values), its scene and logic.
- `tool.draft.json`: "the tool.json fields from the contract, plus `\"stage\": \"built\"`". Fields: id, status
  ("beta"), hook, outcome, driver, minutes, modes, grades_label, sources, third_party, updated ("2026-10-29"), stage.
  The spec's "Who and how" gives driver, minutes, modes and grades_label. Model it on `tools/outbreak-model/tool.json`
  (and a `tool.draft.json` from a BR2 tool, such as `tools/biased-bot/tool.draft.json` if it exists).
- `notes.md`: "teacher notes (a 5-minute start, the modes, talk questions, good to know). Look at
  `tools/shape-talk/notes.md`." Include the pairs format, the "dice have no memory" idea in teacher words, the 5,730
  vs 5,700 note, and the carbon-dating limits with the OpenStax source.
- `voice/lines.json`: `{"bank": "curious-librarian", "voice": "Aoede", "style": "Say curiously and warmly, like a
  friendly school librarian", "lines": [...]}` with every line `V.allLines()` returns, in the same shape as
  `tools/biased-bot/voice/lines.json`. Do not record.
- `audit-states.json`: the states a student reaches beyond the first screen, as real clicks, keys and drags (format in
  the header of `scripts/audit_tool.py`). At least: a d6 tray after Roll to 10 with Show expected; Average 20 runs
  done; a marked half-life with its card; Track one after several rolls; a Nucleus card with a wrong Check (which sum
  is off) and the same card checked right with the ladder showing; F1 checked; the Dating lab with an estimate made
  and Calculate shown; the deep core sample (too old); Counting noise on with the cave charcoal; a state that resizes
  mid-roll if the format allows. Give `keep` regions (the die picker and roll buttons, the steppers and Check, the
  sample shelf, the result card).
- `handoff.md`: "a short note for whoever fixes this tool later: how src.html is laid out, the tricky parts, and what
  you would do next." Include the `## Engine changes wanted` section (write "None" if none).
- `codex-report.md`: your report (section 7).

Do not commit the bundle: `tools/half-life-dice/half-life-dice.html` is generated build output (git ignores it).
Delete `tools/half-life-dice/host.html` (made by `--host`) when you finish; if you cannot delete it, say so.

## 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex-half-life-dice`)

Scratch below means `S:/CurioClass-codex-scratch/half-life-dice`.

1. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py half-life-dice` (in PowerShell: `$env:CURIO_DRAFT=1;
   python scripts/bundle_tool.py half-life-dice`). It must bundle cleanly and the result must be under 2 MB.
2. Frames and real input: `python scripts/drive.py half-life-dice <scratch>/shots.json <scratch>/frames --port 9980
   --profile S:/CurioClass-codex-scratch/half-life-dice/chrome-prof-9980`. Read the header docstring of
   `scripts/drive.py` for the shots format. Use held clicks (`"hold": 0.12`) for anything that involves voice. Use
   `"drag"` with whole-pixel, uneven points for the half-life line and the ruler (real pointer input). drive.py prints
   each shot's js result and every console error, warning and exception: there must be none.
3. 375 wide: start the host with `python scripts/drive.py half-life-dice --host 8796` (it serves until stopped; run it
   in the background and stop it after), then shots with `"url": "http://127.0.0.1:8796/host.html?w=375&h=812"`.
4. Shoot at least: the first screen at every STANDARDS size; each mode at every size; the extremes in section 2;
   Motion off (`"calm": true`) mid-roll and after Average 20 runs; a grayscale frame (never color alone: live vs
   decayed dice, observed vs expected vs mean curves, protons vs neutrons); a keyboard-only path through each mode
   (a roll, a marked half-life, a checked card, a dated sample).
5. **Look at every PNG** (open each image file and view it). Fix overlaps, clipping, unreadable text, text under
   10 px in the preview sizes, and anything the spec's "Done when" fails.
6. Voice: with held clicks at a 2 s pace, read `__tool.vlog` and check every rule in section 2's voice list.
7. Audit: `python scripts/audit_tool.py half-life-dice S:/CurioClass-codex-scratch/half-life-dice/audit --port 9981
   --host-port 8796 --profile S:/CurioClass-codex-scratch/half-life-dice/chrome-prof-audit` (bundle first). Answer
   **every** lead in its `audit.md` in `codex-report.md` (fixed, or why it is not a real problem), in one line each.
   It is mechanical; a clean audit is not a clean tool. Check afterwards that the audit put nothing in the tool folder.
8. Last: close every Chrome you started (on ports 9980 to 9987) and the host server; check with PowerShell that no
   chrome.exe has `CurioClass-codex-scratch/half-life-dice` in its command line.

## 6. Self-check list before you report (BUILD.md lessons, turned into checks)

Every tool in the last waves needed a second review round on these. Check each one and say in one line how.

**Hint and voice**
- [ ] The hint always names the next control, and Read speaks exactly the hint.
- [ ] On a mode switch the hint changes at once, not when a queued line starts.
- [ ] How lines are chosen by `V.heard`, never by counters. No `welcomeAfter`.
- [ ] The first action never waits behind a line.
- [ ] No line names a disabled control (use `needs`).
- [ ] No line is lost at a 2 s tap pace (held clicks, read `V.log`).
- [ ] A hint that changes with a state changes back when the state does (a tracked die that decays, noise off again).

**Focus and layout**
- [ ] Focus is kept when controls rebuild (the die picker, card picker, steppers, sample shelf), and nothing takes
      focus on load.
- [ ] Nothing rebuilds under the pointer.
- [ ] The hint's height is reserved so panels don't jump when its text changes.
- [ ] Labels never overlap (graph labels and the half-life card, equation numbers, ladder rung labels, ruler ticks).
- [ ] **A short set of choices never hides in a scroll panel**: all seven dice, all seven cards and all seven samples
      in view at every size, no scroll.
- [ ] Resizing mid-roll, mid-view-change and mid-count throws nothing and leaves nothing disabled.

**Sizes**
- [ ] 44 px targets and an unclipped hint at every STANDARDS size, including 680x425 and 375 wide through the host.

**No giveaways and one meaning**
- [ ] Steppers start away from the answer, Check never names the answer, the ruler shows no age before Estimate.
- [ ] Nothing can be solved for free by sweeping (say how a student could sweep a stepper or the ruler and why it
      still teaches, or what stops it).
- [ ] Each look in a legend means one thing (observed, expected and mean curves; live, decayed and tracked dice).
- [ ] What a card says is true for the state shown (a tracked die that has decayed is not "surviving").

**Honest numbers**
- [ ] The dice say on screen that they are a model of nuclei; the ages say they use 5,730 years and living carbon at
      13.6 dpm/g; Counting noise says it is a model of counting time.

**Standards**
- [ ] HS-PS1-8 is taught by things a solo student does in each mode. Say which action teaches which part.
- [ ] Your use of the engine matches `docs/families/graphing.md`.

**Motion off**
- [ ] No infinite animations (the kit's `.calm` loops them at 0.01 ms). Timing is the same with Motion off.

Also: no console errors at any size; same seed, same tray; progress survives a reload and Clear resets it; keyboard
only works in every mode.

## 7. Report: write `tools/half-life-dice/codex-report.md` (under 200 lines; start it early)

Use this format exactly:

```
# Codex report: half-life-dice

## Built
(files made, one line each)

## Numbers check
(the spec's numbers next to your Node results; any difference and why)

## Done when
1. PASS or FAIL: evidence (frame file names, js results, V.log excerpts)
... (all 8 spec items)

## Self-check (section 6)
(each item: PASS or FAIL, and how you checked it, one line)

## Audit leads
(every lead in audit.md: fixed, or why not, one line each)

## Frames looked at
(frame groups with sizes and what they show; say you viewed them)

## Engine changes wanted
(same as handoff.md, or "None")

## Chromes and servers
(what you started and that you closed it)

## Left open
(anything not done, not checked, or that you are unsure of)
```

Be honest: a FAIL you report is worth more than a PASS you did not check. When the report is written, you are done.
