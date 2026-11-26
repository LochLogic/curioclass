# Half-Life Dice: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: CODEX-BRIEF.md -->

### Codex build brief: half-life-dice (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real tenth-grade chemistry students tomorrow.

The tool is `half-life-dice`. Its spec is `tools/half-life-dice/spec.md`. **Read the spec fully, every line, before
you write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong or
impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

#### 0. Ground rules for this run

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

#### 1. Read these, in this order

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

#### 2. The rules you must follow (quoted from the docs above)

##### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 10: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool` with everything the spec lists (`state, setMode, die(kind), roll(n), seed(s), card(id),
  setProduct(A, Z), check(), sample(id), noise(on)`) plus `allLines`, the voice log (`vlog: V.log`,
  `get vq() { return V.queue; }`) and whatever a tester needs to read the tray count, the graph points, the tracked
  die, the card result, the ladder and the dating result.

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

##### The spec's open question
The spec asks Cory whether to keep 5,730 years (OpenStax) or switch to 5,700 (NNDC). **Build with 5,730**, as the
spec's Content and Done-when numbers do, and keep the NNDC value where the spec already shows it. Do not decide the
question; it stays in the spec for the owner.

##### From STANDARDS.md "Sizes" (check every one, early)
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

##### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
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

##### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." The roll's 0.4 s, Average 20 runs, the Geiger count time: same with
  Motion off; only the animation goes.
- "Nothing overlaps by accident." "Test the extremes": a coin tray at roll 10 (about 1 left) and a d20 tray at roll 10
  (about 599 left), Average 20 runs on top of a single run, the marked half-life line with its card, every Nucleus
  card with both steppers at their extremes (A 240, Z 94 and Z -1), F1's three products, the ladder with all four
  rungs, the deep core sample with Counting noise on.
- "Words match the state. Grammar, counts, plurals." ("1 roll", "2 rolls", "Rolls survived: 1".)
- "Nothing on screen gives the answer away." The steppers must not start at the right values; Check names which sum
  is off, never the answer; the ruler must not mark the sample's age before Estimate.

#### 3. The engine (use it, do not rewrite it)

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

#### 4. Files to make in `tools/half-life-dice/`

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

#### 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex-half-life-dice`)

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

#### 6. Self-check list before you report (BUILD.md lessons, turned into checks)

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

#### 7. Report: write `tools/half-life-dice/codex-report.md` (under 200 lines; start it early)

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

<!-- end part -->

<!-- part: codex-report.md -->

### Codex report: half-life-dice

#### Built
src.html: three labs, seeded dice, actual-size Plane plots, nuclear equations and carbon dating.
tool.draft.json: beta metadata, Grade 10, students, 25-40 minutes, updated 2026-10-29.
notes.md: pairs start, three modes, discussion, sources, dating limits and device-only privacy.
voice/lines.json: curious-librarian, Aoede, five spec lines plus twelve Read hints; no recordings.
audit-states.json: eleven student states, real clicks, keys and drag, with keep regions.
handoff.md: architecture, numerical rounding, narration inventory and local engine workarounds.
codex-report.md: this report, maintained during the build.
Generated bundle: about 103 KB, below 2 MB. No git commands, engine edits, external images or network access.
Evidence below is under S:/CurioClass-codex-scratch/half-life-dice/.

#### Numbers check
Node numbers.cjs recomputed every requested number before implementation.
Spec / Node half-lives: 1.000/1; 2.409/2.409421; 3.802/3.801784; 5.191/5.190893; 6.579/6.578813; 7.966/7.966167; 13.513/13.513407 rolls.
Spec / Node expected at 10: 1.0/0.976563; 56.3/56.313515; 161.5/161.505583; 263.1/263.075576; 348.7/348.678440; 418.9/418.903888; 598.7/598.736939.
Spec / Node ages: 1906/1905.656693; 3349/3348.796481; 0/0; 5730/5730; 11460/11460; 22920/22920; 53916/53915.810064 years.
340 counts: sqrt = 18.439089. Exact range 11023.412792 to 11920.936689 years; spec 11020 to 11920 rounds to tens.
Methane: 9.230419 eV. Fission/methane: 21668472, about 22 million. Fusion/fission values retain the supplied spec's 17.6 and about 200 MeV.
No numerical disagreement; 5,730 remains the dating half-life, and the owner's NNDC question stays open.

#### Done when
1. PASS: validation.json, d6 expected 161.5056; twenty-run mean 164.45 at 10, maximum deviation 5.5944 over all rolls.
2. PASS: all seven exact half-lives above; real-half.json accepts an observed 4.0 reading; keyboard-roll.json accepts 3.5.
3. PASS: tracked.json keeps 1 in 6 at every age; final-state.json covers decay, a new live die and the restored hint.
4. PASS: validation.json, all seven correct products accepted, mass-only and charge-only errors rejected; compact-right-* and extreme-* viewed.
5. PASS: compact-right-* and ladder-final-680 show all four labeled rungs and 22 million ratio, including the smallest landscape view.
6. PASS: validation.json gives 1906, 3349, 22920 and 53916 with too-old flag. Noise uses sqrt(count); core-flag-final-680 retains its warning with noise.
7. PASS: identical seed reproduces faces, live mask and points. reload.json retains 7 cards and 7 samples; clear.json resets both. Calm timing measured below.
8. PASS: final/ covers all desktop sizes, host-final/ covers 375x812 in an iframe; keyboard paths pass, requests are zero and tool console is clean. Outer host favicon warning is recorded below.

#### Self-check (section 6)
PASS: hint names the next control; voice-read.json records Read speaking exactly the current hint.
PASS: mode handlers set hints synchronously before queuing welcomes; voice-read and keyboard paths verify the visible state.
PASS: Track instruction uses V.heard; welcomes use Curio.voice's once-only keys; no welcomeAfter or custom speech queue.
PASS: controls update immediately; no action awaits narration, including a first Roll click.
PASS: voice entries use valid/needs. Calculate is actionable and explains the Estimate gate without revealing an age.
PASS: held 120 ms clicks at a 2 s pace, voice-track has one teaching line; voice-event starts all five tooOld events.
PASS: final-state.json verifies tracked decay, replacement and noise-off hints return to the matching state.
PASS: controls are created once, inputs retain focus, no load focus; keyboard-nucleus ends focused on Check.
PASS: no controls rebuild under the pointer; graph resize defers during dragging and redraws on drop.
PASS: fixed-height hint bar prevents hint-driven panel jumps.
PASS: critical labels reviewed at 680 and 375; four-rung and graph-bottom clipping were fixed and re-shot.
PASS: all seven dice, cards and samples stay visible, with no scroll panels.
PASS: full audit resized after every state input and active walk click, no exceptions or stuck controls.
PASS: phone-half.json and phone-ruler.json measure both rendered handles at 48x48 px; audit-targets reports no small targets. Buttons are at least 44 px.
PASS: steppers start at 10, 3, away from every answer. Check identifies failed sums; no sample-age marker appears before Estimate.
PASS: sweeping shows only the proposed values. A student must press Check to test conservation, or Estimate then Calculate to compare an age; no hidden answer or score is exposed while dragging.
PASS: observed solid circles, expected long dashes, mean dotted diamonds; live faces, gray x marks and tracked ring remain distinct in grayscale.
PASS: tracked cards distinguish live and decayed nuclei; final-state.json checks both wordings.
PASS: on-screen model labels give dice-as-nuclei, 5,730 years, 13.6 dpm/g and 100 modeled minutes compressed to 1 second.
PASS: HS-PS1-8 actions are rolling/marking decay, balancing all nuclear products, and selecting/checking decay, fission and fusion to compare their energy rungs.
PASS: Plane owns axes, curves, points, segments, keyboard handles, dashes and formatting. SVG dimensions follow actual box sizes; no animated g.view is needed.
PASS: no infinite animations. timing.json measured calm roll 418.6 ms, mean 2193.9 ms and counter 1060.3 ms, including rendering/scheduling overhead.
PASS: the same 400 ms, twenty 100 ms waits and 1000 ms count timer run with either Motion setting.
PASS: keyboard-only roll, half-life, balanced card and dated sample, inputs/keyboard-*.png and JSON.
PASS: validation.json resource requests = []; no tool console errors in the driven sweeps.
PASS: accent contrast computed as 8.24:1 on panel, 7.81:1 on section background, 8.79:1 for brand ink on accent.
PASS: progress persistence and Clear verified; visible totals and Saved on this device only appear with Clear.

#### Audit leads
Full audit: audit/audit.md, 36 leads; audit-final rechecked all sizes and changed states without repeating the unchanged full control walk.
A01 FIXED: 680 Roll tab 38 px wide, explicit minimum width 44 px.
A02 FIXED: 800 Roll tab 38 px wide, same fix.
A03 FIXED: 1000 Roll tab 38 px wide, same fix.
A04 FIXED: 375 Roll tab 40 px wide, same fix plus full-width phone mode row.
A05 FIXED: Dating hint named disabled Calculate; enabled validation button now explains the Estimate gate.
A06 FIXED: mode Dating, Roll tab outside phone edge, phone header now has its own mode row.
A07 FIXED: mode Dating, Nucleus tab outside phone edge, same fix.
A08 INTENTIONAL: expected curve crosses the marker's transparent hit region; the visible handle remains clear and marks a mathematical crossing.
A09 FIXED: dated state, phone Roll tab outside edge, header fix.
A10 FIXED: dated state, phone Nucleus tab outside edge, header fix.
A11 FIXED: too-old state, phone Roll tab outside edge, header fix.
A12 FIXED: too-old state, phone Nucleus tab outside edge, header fix.
A13 FIXED: noise state, phone Roll tab outside edge, header fix.
A14 FIXED: noise state, phone Nucleus tab outside edge, header fix.
A15 EXPECTED: m-roll welcome unheard with Sound off by default; Sound on queues the unheard welcome.
A16 EXPECTED: m-nucleus welcome unheard with Sound off; spoken on sound-enabled entry, voice-read.json.
A17 EXPECTED: m-dating welcome unheard with Sound off; spoken in voice-event.json.
A18 EXPECTED: Motion first tap remains silent while Sound is off.
A19 EXPECTED: Coin first tap remains silent while Sound is off.
A20 EXPECTED: d4 first tap remains silent while Sound is off.
A21 EXPECTED: d6 first tap remains silent while Sound is off.
A22 EXPECTED: d8 first tap remains silent while Sound is off.
A23 EXPECTED: d10 first tap remains silent while Sound is off.
A24 EXPECTED: d12 first tap remains silent while Sound is off.
A25 EXPECTED: d20 first tap remains silent while Sound is off.
A26 EXPECTED: New seed first tap remains silent while Sound is off.
A27 EXPECTED: Roll once first tap remains silent while Sound is off; actions never wait for a welcome.
A28 EXPECTED: Roll to 10 first tap remains silent while Sound is off.
A29 EXPECTED: Reset first tap remains silent while Sound is off.
A30 EXPECTED: Show expected first tap remains silent while Sound is off.
A31 EXPECTED: Average first tap remains silent while Sound is off.
A32 EXPECTED: Track one first tap remains silent while Sound is off; sound-enabled five-tap test speaks its teaching line once.
A33 EXPECTED: Mark first tap remains silent while Sound is off.
A34 EXPECTED: Clear in Nucleus changes nothing when saved progress is already empty; 7-to-0 reset separately verified.
A35 EXPECTED: Clear in Dating changes nothing when saved progress is already empty; same reset evidence.
A36 EXPECTED: clicking the ruler handle without dragging changes nothing; real-ruler.json and keyboard-date.json verify dragging and arrows.
F01 INTENTIONAL: audit-final flags curve crossing the marker's transparent hit region at four sizes, same as A08.
F02 FIXED: phone half-life target was 41 px; geometry observers and 48 px hit area yield 48x48 rendered pixels, phone-half.json.
F03 FIXED: phone age target was 41 px; same fix yields 48x48 rendered pixels, phone-ruler.json.
T01 INTENTIONAL: compact Dating age handle overlaps the 13.6 label only in its transparent hit rectangle; visible glyphs are separate, native frame reviewed.
T02 INTENTIONAL: compact Dating handle is reported under its transparent rectangle; this is its own hit area, no visible occlusion.
T03 INTENTIONAL: compact Dating 6.8 label is reported under that transparent rectangle; text remains legible and pointer input works.
T04 INTENTIONAL: expected curve crosses the half-life transparent hit region at every size, same mathematical crossing as A08.
T05 INTENTIONAL: compact core-noise age hit rectangle touches 13.6; visible glyphs are separate, native frame reviewed.
T06 INTENTIONAL: compact core-noise handle is reported under its transparent rectangle; no visible occlusion.
T07 INTENTIONAL: compact core-noise 6.8 label is under transparent hit geometry only; legible, pointer input verified.
All three audits completed with clean resize stress, no stuck controls, focus loss, infinite animations or tool console errors.
The outer drive.py host emitted favicon.ico 404, and two connection-reset traces on browser shutdown. The tool itself requested no resources and produced no console errors.

#### Frames looked at
Viewed every first/ PNG through contact sheets, plus the three 680 originals; initial clipping was fixed.
Viewed every final/ PNG: all three modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
Viewed fixed/ and last/: 375x812 iframe modes, F1, core noise, four-rung ladder and compact graph.
Viewed every extremes/ PNG: all seven cards at A 240 with Z 94 and -1, all seven correct cards, Coin/d20 at 10, mean and grayscale.
Viewed validation/ reload, Clear and numerical result frames.
Viewed all ten inputs/ frames: keyboard paths, real drags, voice, calm roll and calm mean.
Viewed all 102 audit/ PNGs in seventeen contact sheets; reviewed small previews at full size elsewhere.
Viewed all nine compact/ PNGs, including every checked card at 680, tracking and calm noise.
Viewed all 57 audit-final/ and 29 audit-targets/ PNGs in contact sheets; inspected compact Dating/core and phone marker originals.
Viewed end/ (3), host-final/ (7), shipping/ (4) and fission-final/ (1): lifecycle, gate, phone drags, core noise, exact 340 counts and compact F1.
Final F1 frame shows all three emitted neutrons; model has 236 nucleons before and 236 after, 472 circles total.

#### Engine changes wanted
None. Local handle-focus wrappers use preventScroll; geometry observers rebuild the actual-size Plane and defer redraw during a drag.

#### Chromes and servers
Muted Chrome profiles used ports 9980, 9981 and 9982; all profiles, captures and temporary scripts are in scratch.
All drivers and audits finished and closed their launched Chrome process trees. Exact drive.py host parent 648 and verified child server 19672 were stopped; host.html was removed.
ports-final.json confirms 8796 and every port 9980 through 9987 inactive. All audit servers are stopped.
PowerShell Get-CimInstance was denied. A native read-only query found no readable owned match, but all 11 remaining Chrome command lines were inaccessible; a complete machine census cannot be certified.
No test output was written into the tool folder, aside from the required generated bundle.

#### Left open
No functional or visual checks remain open. Full machine Chrome command-line verification is permission-limited as described above.
The owner's 5,730 versus 5,700 question remains unchanged. No narration was recorded, as requested.
Source values were checked against the supplied spec and recomputed locally; source pages were not re-fetched.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit round 1 failed two narrow items; integrator fixed both and verified by driving, 2026-10-29)
Counts: blockers 2 (general 2, family 0), should fix 14 (general 14, family 0), polish accepted 9

### Refine: half-life-dice

Builder: Codex (third single-tool test, 2026-10-29). Lenses: refine/teaching.md (1 / 6 / 4 / 3), refine/play.md
(0 / 8 / 8 / 4), refine/craft.md (1 / 8 / 4 / 3); refine/sensitivity.md PASS (rule 5 referral from Teaching, low
risk: two should fix, one nit, merged below). Merged by the integrator. Sources: T = Teaching, P = Play, C = Craft,
S = Sensitivity. Every finding is tagged general unless marked.

#### Blockers

1. **Sound starts off for the whole tool** (C B1, P S4, T cross-lens note) general. `src.html` ends with
   `Curio.init(...);$('sound').click();`, so the kit's header Sound (on by default) is off on every load and a solo
   student hears no welcome, no trackTip, no tooOld (BASELINE rule 4). The spec puts only the Geiger counter's clicks
   off by default. Remove the click; header Sound stays as the kit sets it. Give the counter its own toggle,
   `Counter clicks`, off by default, next to Counting noise (Settled 1). Fix notes.md ("Sound starts off").
2. **Mark a half-life refuses a correct line and accepts one with no data** (T B1, T S2, P S2, C S7, T nit 13)
   general. The handle snaps to the expected curve's height at each half roll, so it never sits on 500 (d6: 528 or
   482), and acceptance compares the student's own noisy tray with the exact half-life: on the default seed a d12 line
   at 498 gets "Move to half the crowd" and only 544 is accepted; with 0 rolls the card says "Accepted. Expected
   crossing: 4.0 rolls". Settled 2 gives the new rule: the line moves in 25-nucleus steps (pointer and arrow keys), it
   is "on half the crowd" at 500; the card then reads the tray's own crossing (to the half roll) against the exact
   value, and when they differ by more than 0.5 rolls it says why ("One tray scatters. Press Average 20 runs to see
   the crowd hug the exact value."). Before any roll, Mark says "Roll first, then mark the half-life." and accepts
   nothing.

#### Should fix

1. **The dice tray is not readable as dice** (P S1, C S1, T S4) general. The 40 x 25 grid is stretched into a wide
   short box: dice are 3 to 6 px squares in stripes with wide gaps, faces about 5 px at 1366x768, 2 px at 680x425, a
   50 px band at 375; the tracked ring is clipped at the top edge. Keep cells square (fit a centred 40:25 block, or
   choose columns from the box aspect, still 1,000 dice), faces about 9 px or more at 1366x768 and readable on a
   projector at 1920x1080, ring never clipped. Also: a die that rolls 1 is never seen showing 1 (it greys in the same
   frame). Show the roll's faces for a beat with this roll's 1s outlined in the accent (shape, not colour only), then
   grey them, with timing the same with Motion off.
2. **The d20 tray never reaches its half-life** (T S3, P polish 4) general. Rolls stop at 10 while a d20's half-life is
   13.5 and the graph runs to 16. Roll once continues to the graph's last roll for every die (Roll to 10 keeps its
   name and stops at 10); the card says so when a die needs more than 10 rolls (Settled 3).
3. **Roll buttons look live when they do nothing** (P S3, C S6, P polish 3) general. `aria-disabled` has no style, so
   at the last roll, during a roll and during Average 20 runs the buttons stay bright primary and silent. Give
   `[aria-disabled="true"]` a dimmed look, and at the last roll a card line and hint "Every roll is done. Press Reset
   for a fresh tray." Track one after the last roll says "Press Reset to track a die from the start."
4. **Roll once and Roll to 10 swallow the welcome** (C S2) general. They are in `speaks` but never speak, so a first
   tap on Roll once (the control the hint names) skips wRoll and nothing is heard. Remove them from `speaks`, and make
   sure wRoll is not lost while a roll is busy (queue it after the roll, or do not gate the welcome on busy).
5. **The Dating welcome skips Estimate** (P S5, C S3, T polish 10) general. Spoken "Drag on the ruler to estimate,
   then press Calculate" while the hint says to press Estimate first. wDating becomes the hint's words (Settled 4).
   Then Calculate shows as secondary (and its hint says "Press Estimate first") until Estimate is pressed for this
   sample.
6. **Estimate is free, and the ruler can't be read between ticks** (P S6, T S7) general. Estimate takes the untouched
   pin (1,000 years) and Calculate prints the exact age; "Close" can be found by drag-Estimate-repeat. The ruler marks
   only whole halvings, so the two real samples (10.8 and 9.07) sit between ticks with nothing to read (straight
   reads are 24 and 14 percent off). Add minor marks at their log positions (12, 11, 10, 9, 8, 7 dpm/g, and the same
   between later halvings), labelled where they fit; the pin starts unplaced for each sample and Estimate needs a
   moved pin; one Estimate per sample, then Calculate shows both side by side ("You read 3,000 years. Exact: 3,349.
   Off by 10 percent.") with no "Close" verdict before Calculate.
7. **Counting noise never varies** (P S7) general. Every recount of cave charcoal is 337 because the count is seeded on
   the sample index. Add `Count again` (with noise on) that draws the next count from the same seeded stream, so the
   same seed still gives the same sequence (Done when 7), and list the counts so far so the spread shows (Settled 5).
   The ± range stays the square root of the current count.
8. **The Geiger counter clicks the same for every sample** (C S8) general. Ten tones per count whatever the activity
   (deep core 9 tones, fresh leaf 10). Click once per counted decay, thinned (about count / 20, at seeded random times
   over the second), so a living leaf crackles and the deep core ticks twice. Plays only when Counter clicks is on.
9. **The nucleus drawing gives wrong pictures** (T S5, P S8, C S4, P polish 1, C P2) general. The legend is split as
   "Before: protons p+ (solid)" over the left and "Products: neutrons n (outlined)" over the right, read as titles;
   protons and neutrons differ by colour only (1.04:1 luminance; the 0.5 px stroke does not show); protons fill the
   centre with a neutron shell (the spiral colours the first Z dots); light nuclei are loose clouds. Titles "Before"
   and "After (your product)" over the sides, one legend line "● proton p+  ○ neutron n" with a real shape or
   lightness difference (a hollow ring or much darker neutron), protons and neutrons mixed through the cluster
   (seeded), dots sized so neighbours touch, and symbols and the arrow clear of the dots at every size (375 wide).
10. **The energy ladder has no scale and its bars cross their labels** (T S6, C S5, P polish 7) general. Bars start at
    methane on a log scale with no ticks, so methane looks like zero and carbon-14 decay like half of fission (it is
    about 1/1,300); at 680x425 and 375 each bar strikes through the next label. Draw a faint axis with ticks at
    1 eV, 1 keV, 1 MeV and 100 MeV (labelled), bars from 1 eV, at least about 22 px per rung or labels beside short
    bars, never touching a bar. (A student action on the ladder is an open question for Cory, below; do not add one.)
11. **"Dead Sea Scrolls paper" is wrong for the artifact** (S 1) general. The scrolls are mostly parchment with some
    papyrus. Name the sample "Dead Sea Scrolls fragment" everywhere (src.html, notes.md; the spec now says so), keep
    10.8 dpm/g.
12. **Teacher notes: real artifacts, textbook values; cancer care** (S 2, T nit 14) general. notes.md Good to know: one
    line that both are real artifacts but the activity values are simplified textbook examples (published radiocarbon
    studies give a range of dates across many scrolls, and real dates are calibrated; the Tutankhamun value fits the
    tomb's date of about 1323 BCE), and one line that the N3 to N5 cards touch on cancer care and thyroid treatment,
    which a student may know from their own family (rule 8). The optional context line (the scrolls are ancient Jewish
    texts found near Qumran; the seeds come from an Egyptian king's burial) may go in too.
13. **Two cards keep naming a step that is done** (P polish 8, C P1) general. After Mark is pressed the half card still
    says "Press Mark a half-life..."; after a wrong Check the change box still says "Check both sums to test it".
    "Drag the line to 500, then read the roll number." and "Fix the sum that is off, then press Check again." (and
    the hints to match).
14. **The fusion and fission energies are credited to a page that does not state them** (T polish 11) general.
    OpenStax Chemistry 2e 21.4 gives neither 17.6 nor about 200 MeV. Settled 6: the values stay, credited to OpenStax
    College Physics 2e 32.5 (D-T, 17.59 MeV) and 32.6 (average U-235 fission, 200 MeV), checked by the integrator on
    2026-10-29. Update the credits comment in src.html, tool.draft.json sources and notes.md.

#### Polish accepted

1. Each roll lands: "98 of 591 live dice decayed this roll (17 percent)" in the summary, so the same fraction at every
   age shows in the student's own data, beside the tracked die's fixed chance (T polish 8, P polish 5).
2. N4 shows the gamma ray in the equation once balanced (⁰₀γ), since gamma is one of the three decays HS-PS1-8 names
   (T polish 9).
3. Steppers: add -10 and +10 steps (or press-and-hold repeat) and "or type a number" by the boxes; the start values
   stay away from every answer (P polish 2). F1 now needs 131 presses.
4. Track one rings a seeded random live die away from the edges, never clipped (P polish 3, C N2).
5. One look, one meaning: toggles that are on (Show expected, Mark a half-life, Counting noise, Counter clicks) get one
   style, distinct from the primary action buttons; Clear and New seed set apart from the seven choices; each Clear
   resets its own mode's progress, or says "Clear all progress" and asks once (P polish 6, C P3).
6. 375 wide: the graph keeps at least about 140 px of plot height (C P4).
7. Positron written ⁰₊₁e as in the spec (T nit 12, P nit 1).
8. Graph label with a true minus and a superscript n (P nit 2, C N1, family:graphing for the label style).
9. Small words: "Counting noise" not wrapping at 1366 and 800; card buttons keep a short name at 375 (P nit 3); the
   deep core with noise reads "near the end of the clock's range" when the range reaches below 50,000 years (P nit 4);
   N3 "Thyroid treatment and imaging" (S nit).

Declined: folding the six @media layers into one per breakpoint (C N3); a refactor, not a student-facing change. Do
it only if it makes the layout fixes safer.

#### Settled by the integrator

1. **Sound.** Header Sound stays as the kit sets it (on). The spec's "sound off by default" is the Geiger counter's
   clicks only: a `Counter clicks` toggle, off by default. Spec line updated.
2. **Mark a half-life rule.** The spec's "accepts a reading within 0.5 rolls of the exact value" fails for one noisy
   tray (Teaching's d12 case). Replaced in the spec: the line is accepted at 500 (25-nucleus steps), the card reports
   the tray's own crossing and the exact value, and explains the scatter when they differ by more than 0.5 rolls;
   nothing is accepted before a roll. Done when 2 updated to match.
3. **Roll cap.** The spec never set one; Roll once continues to the graph's end for each die. Spec line added.
4. **wDating line.** "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." (the hint's wording, so
   one recording serves both). Spec Voice updated.
5. **Count again.** A button, not a mode; within the spec's Counting noise. Spec line added.
6. **Sources.** 17.6 MeV and about 200 MeV credited to OpenStax College Physics 2e 32.5 and 32.6 (fetched 2026-10-29:
   "17.59 MeV" for D-T; "the average fission reaction of 235U produces 200 MeV"). Spec Sources updated.
7. **Sample name.** "Dead Sea Scrolls fragment" (Sensitivity). Spec Content updated.
8. Not findings: the audit's "Age estimate over 13.6 and 6.8" (transparent hit area only), "expected curve across the
   half-life line" (the reading itself), "Clear changed nothing" (empty progress). Check giving both sums is the
   balancing skill, not a giveaway (Play, Teaching).

#### Spec open questions

- **For Cory: give the student an action on the energy ladder?** (T S6, rule 2). HS-PS1-8 asks for "the energy
  released in fission, fusion and decay"; today the ladder is only shown after Check. Teaching proposes one small
  action, for example: after a card balances, the student taps the rung band where they think its energy lands
  (chemistry, keV, MeV, hundreds of MeV) before it is revealed. It would teach the scale by prediction; it adds a step
  to every card. Not sent to polish; the ticks (Should fix 10) go in either way.
- (Existing, the spec's own) 5,730 or 5,700 years: unchanged, for Cory.

#### Exit check, round 1

Fresh cold agent, 2026-10-29. Frames in S:/CurioClass-codex-scratch/half-life-dice/exit/ (defaults/, b2/, b4/, b5/, b6/). Bundle 118 KB, no console errors or exceptions in any shot (only the host page's favicon 404), zero resource requests (b5/net).

- Blocker 1: held. Sound on at every size (defaults/*), Counter clicks off; held Roll once starts wRoll (b2/voice-first-roll); 0 clicks by default, leaf 68, core 2, 0 with Sound off (b2/clicks-*).
- Blocker 2: held. Before a roll Mark says "Roll first" and refuses 500 (b2/mark-before-roll-500); 525 refused, 500 accepted by keys and by a real drag (b2/mark-525, mark-500-keys, mark-500-drag); d12 8.5 vs 7.966 gives the scatter line (b2/mark-d12-cap).
- Should fix 1: held at the named targets. Square cells, faces 10.8 px at 1366, 16 px at 1920, ring clear, landed 1s outlined, same 400 ms in calm (defaults/roll-3-1366x768, b2/normal-landing-1920, b2/calm-landing). Note: at 680x425 and 375 cells are still 4 px with 3 px faces, a texture rather than dice (defaults/roll-3-680x425, roll-3-375x812); not named in the fix, integrator's call.
- Should fix 2: held. d20 rolls to 16, 465 left, crossing 14.5; Roll to 10 stops at 10 and the card says Roll once continues (b2/d20-16, d20-roll10-card).
- Should fix 3: held. Roll buttons dim during a roll, Average and at the cap; cap card and hint name Reset; Track one at the cap says "Press Reset to track a die from the start." (defaults/roll-3-1366x768, b2/cap-d6, cap-d6-track, average-mid).
- Should fix 4: held. First held Roll once speaks wRoll (b2/voice-first-roll); five rolls 2 s apart, wRoll once, nothing lost (b6/voice-5-rolls).
- Should fix 5: held. wDating equals the hint and is spoken on entry (b2/voice-dating); Calculate stays secondary with "Press Estimate first" until Estimate (b5/date-calc-first, date-drag-est-calc).
- Should fix 6: not held (regression). Unplaced pin, moved pin needed, one locked Estimate, no verdict before Calculate, "You read 1,800 years. Exact: 1,906. Off by 6 percent." all hold (b5/date-drag-est-calc). But the new minor labels repeat rounded values at different ages: "0.04 0.04" and "0.02 0.02" at 1366, "0.03 0.03" and "0.02 0.02 0.02" at 1920, around the deep core's own 0.02 (b5/ruler-1366x768, ruler-1920x1080; defaults/dating-1366x768). Fix: more digits there, or skip a label whose text matches a neighbour.
- Should fix 7: held. Cave counts 337, 324, 366, 333, same on a second load and at 375; history listed; ± 18 for 333 (b5/count-again, count-again-repeat, count-again-375).
- Should fix 8: held. Clicks follow the count (leaf 68, core 2), off by default, gated by header Sound (b2/clicks-on-leaf-core).
- Should fix 9: not held at 375 and 760x900. Titles, one legend, mixed touching nucleons and the grayscale difference hold (b4/gray-N2-1366, gray-F2-680). The arrow overlaps the Ba nucleus on F1 when balanced at 375 and 760x900 (defaults/ladder-F1-375x812, ladder-F1-760x900; b4/nuc-sweep-375x812, nuc-sweep-760x900). All other cards and sizes clear (b4/nuc-sweep-*).
- Should fix 10: held. Axis with 1 eV, 1 keV, 1 MeV, 100 MeV, bars from 1 eV, no text/bar overlaps at 375, 680x425, 800x500 (defaults/ladder-F1-*).
- Should fix 11: held. "Dead Sea Scrolls fragment" in tool and notes, 10.8 kept (defaults/dating-1366x768).
- Should fix 12: held. notes.md Good to know has the artifacts line and the N3 to N5 family line.
- Should fix 13: held. Active Mark card says "Drag the line to 500, then read the roll number."; wrong Check change box and hint say "Fix the sum that is off, then press Check again." (b2/mark-525, b4/wrong-check-1366).
- Should fix 14: held. Credits comment, tool.draft.json and notes cite College Physics 2e 32.5 and 32.6.
- Polish 1: held ("124 of 715 live dice decayed this roll (17 percent).", defaults/roll-3-*).
- Polish 2: held (N4 balanced shows gamma, b4/N4-gamma). Polish 3: held (+10/-10 on desktop, type hint, hold repeat 10 to 21, b4/stepper-hold).
- Polish 4: held (ring inside the tray, crop-1366-tray). Polish 5: held (toggles inset outlined, actions solid, dashed New seed and Clear; each Clear only its own mode, b5/persist-b-reload).
- Polish 6: held (phone plot 138 px, b6/phone-plot). Polish 7: held (0 +1 e, b4/N5-positron). Polish 8: held (true minus, superscript n).
- Polish 9: partly held. Counting noise on one line at 1366 and 800; core noise reads "Near the end of the clock's range" (b6/core-noise); N3 "Thyroid treatment and imaging". Not held: at 375 the card buttons still show only N1 to F2 (defaults/nucleus-375x812). Polish, not blocking.
- Settled 1 to 8: held as written (sound, 500-only rule, roll cap, wDating line, Count again button, sources, sample name; the Settled 8 non-findings still are).
- Done when 1: held (expected 161.51 at 10, 20-run mean within 5.6 at every roll, b2/done-1-2). Done when 2: held (all seven exact values match Content; 500 accepted with tray and exact value).
- Done when 3: held (chance 1 in 6 at every age, b2/done-3-track). Done when 4: held (all seven accept only the right product, mass and charge failures named, b4/nucleus-checks).
- Done when 5: held (four rungs and the 22 million line). Done when 6: held (1,906; 3,349; 22,920; core too old with tooOld spoken; ± is the root of the count, b5/date-ages, date-core-voice).
- Done when 7: held (same seed same tray, new seed differs, progress survives reload, Clear resets, calm shows faces, b5/seed-same, persist-*, b2/calm-landing).
- Done when 8: held except the items above. Tray, graph and buttons in view at all six sizes (defaults/*; nucleus at 680x425 has 5 px of panel cut, controls visible); Tab reaches every control in order, the pin and line handles take arrows with a visible ring (b5/kb-*, b6/pin-focus).
- Gate: codes taught (energy-ladder action stays Cory's open question), solo defaults good, sensitivity PASS, voice counts right (22 lines in lines.json match the tool exactly), contract clean. Open: Should fix 6 and 9 as above.

#### Audit pilot (exit)

audit-exit/audit.md was not written when this check finished (frames only, still running); no leads to mark.

#### Integrator fixes after exit round 1 (2026-10-29)

- Should fix 9, fission arrow over Ba at 375 and 760x900: the arrow moved from mid-stage into the title row (y 33,
  16 px), between "Before" and "After (your product)". Checked F1 balanced at 680x425, 800x500, 760x900, 1366x768,
  1920x1080 and 375 (host): arrow box touches 0 nucleons and 0 text. Frames: exit/fix/fix-ladder-F1-*.png.
- Should fix 6 regression, repeated ruler minor labels: a minor label is skipped when its text is already on the ruler.
  Checked at all five ruler sizes: 0 repeated labels (14 to 44 labels). Frames: exit/fix/fix-ruler-*.png.
- Not blocking, left for Cory: Polish 9 partly held (at 375 the card buttons show only N1 to F2, no short names); the
  dice tray at 680x425 and 375 still reads as a texture (4 px cells, 3 px faces), fine at the sizes the review named.
- No fresh exit round was run on these two changes (one SVG text position, one label filter); the drive checks above
  are the evidence.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: half-life-dice (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, tool.draft.json, codex-report.md and handoff.md (the last
two read as claims). No art/prompts.json: the spec has no art, so step 5 does not apply. Bundle used as built
(tools/half-life-dice/half-life-dice.html, 107,155 bytes, newer than src.html and the kit). Shared audit:
S:/CurioClass-codex-scratch/half-life-dice/audit-r1/audit.md. My frames and logs:
S:/CurioClass-codex-scratch/half-life-dice/lens-craft/ (voice/*.json and .png, frames/*.png and .json).

Counts: blockers 1, should fix 8, polish 4, nit 3.

#### Blocker

**B1. Sound starts off for the whole tool, not just the Geiger clicks.** src.html:145 `Curio.init(...);$('sound').click();`
flips the kit's Sound (default on, not saved) to off on every load. The spec puts only the counter clicks off by
default ("A Geiger counter clicks (sound off by default)"). Because of this, a student gets no narration at all
unless they find Sound: no welcome, no trackTip, no tooOld. notes.md ("Sound starts off") documents the wrong
behavior. Seen in: voice/def-first-roll.json (first tap Roll once, Sound `false`, log empty), every audit frame
(header shows the muted Sound icon), and the audit's "welcome not heard" rows for 19 first taps. Better: remove the
`.click()`, keep header Sound on as the kit does, and give the counter its own clicks toggle (off by default, as the
spec says), or gate the tone on Counting noise. Then update notes.md. Without this the voice check cannot pass under
the defaults (gate item 7). *general*

#### Should fix

**S1. The dice tray can't be read at any size.** drawTray (src.html:113) fits the fixed 40 x 25 grid to the box, so
cells are much wider than tall (about 26 x 7 px at 1366x768) and each die is a square sized to the short side. The
tray shows as 40 thin striped columns with 5 to 6 px dice. Faces are not readable, the tracked ring is hard to find,
and at 375 wide the whole tray is a 50 px band. Seen in: frames/zoom-tray-1366.png, tray-1920.png (still stripes at
1920x1080), d20-ten.png (two-digit faces become specks), h375-tray.png. The spec wants "each a small square with its
face". Better: keep cells square, either by fixing the tray box to the 40:25 aspect and centering it, or by giving the
tray row enough height (as is, the graph takes most of the height). Faces are still readable at about 9 px. *general*

**S2. Roll once and Roll to 10 are listed in `speaks` but never speak.** src.html:93 `speaks:'#track,#calculate,#roll-once,#roll-ten'`.
A first tap on Roll once (the control the hint names) skips the welcome, so nothing is heard. wRoll stays unheard
until the student changes mode, which means the premise "Every 1 is a decay." is lost for the most likely first
action. Seen in: voice/ft-rollonce.json (Sound turned on before the tap, log empty after 8 s); compare ft-die.json
(d20 first, wRoll after 134 ms). Better: drop `#roll-once,#roll-ten` from `speaks`. The welcome's own
`valid: !state.busy` then drops it during the roll and leaves it unmarked, so it should go through V.welcome() again
once the roll ends, or the welcome should not be gated on busy. *general*

**S3. The Dating welcome tells students to skip a step.** Spoken wDating: "Pick a sample. Drag on the ruler to estimate,
then press Calculate." The hint shown at the same moment reads "Pick a sample. Drag the ruler pin, press Estimate, then
press Calculate." A student who does what they heard gets "Press Estimate to record your ruler pin before Calculate."
To keep the spoken line naming an enabled control, the builder left Calculate enabled, styled primary, ahead of the
step it needs (handoff.md says so). Seen in: voice/rep-modes.json and read-cut.json (wDating spoken while the hint shows
hint12); frames from the audit, state-mode-dating-lab-*.png (Estimate and Calculate look the same). Better: wDating
becomes the hint12 wording (a small spec line change for the integrator to settle), and Calculate shows as secondary or
says "Estimate first" until Estimate is pressed. *general*

**S4. Protons and neutrons differ only by color, and the legend words are wrong.** Protons `#ff8f6b` and neutrons
`#9fb3c8` have a luminance contrast of 1.04:1 (computed), so in grayscale and for many color-blind students they look
alike. The 0.5 px neutron stroke does not show (frames/zoom-nuclei-1366.png). The legend is split across the two
halves as "Before: protons p+ (solid)" and "Products: neutrons n (outlined)" (src.html:131), which reads as though the
left side holds only protons and the right side only neutrons. Seen in: audit state-right-1366x768.png,
nucleus-f1-1366.png, h375-ladder.png. Better: a clear difference in shape or lightness (a hollow ring for neutrons, or a
much darker neutron fill), and one legend line, "● proton p+  ○ neutron n", over both sides. *general*

**S5. Energy ladder bars cross their labels at 375 wide.** drawLadder places each label 5 px above its bar, but the row
pitch at that height is about 13 px, so every bar strikes through the next label ("D-T fusion: 17.6 MeV" is crossed
out). Seen in: frames/h375-ladder.png, zoom-ladder-375.png, and audit state-right-375x812.png. The audit marked this
state clean. Better: set a minimum row height (label above bar, about 22 px per rung), or put labels to the right of
short bars. *general*

**S6. Disabled roll buttons look live.** After 10 rolls, and during a roll, Roll once and Roll to 10 get
`aria-disabled="true"` (src.html:105), but nothing in the kit, the theme or the tool styles that state. They stay bright
green primary buttons that do nothing and say nothing. The same goes for Average 20 runs while it runs. Seen in: audit
state-d6-ten-1366x768.png, d20-ten.png. Better: a dimmed style for `[aria-disabled="true"]` (and a short "10 rolls done.
Press Reset for a fresh tray." in the card). *general*

**S7. The half-life line can't be put on 500, and it is "Accepted" before any roll.** The handle's `snap` puts y on
expected(n) for whole and half rolls (src.html:115), so for a d6 the line jumps from 528.3 to 482.3 and never sits at
500. Yet the hint says "Drag the graph handle to 500 nuclei" and the card says "Move the line to half the starting
crowd." On a fresh tray (0 rolls) the card reads "Accepted. Expected crossing: 4.0 rolls" because it falls back to the
expected curve. Seen in: frames/mark-reach.json (every reachable y, each step labeled; 3.5 and 4 both accepted at 0
rolls), audit state-marked-680x425.png. The spec asks for the reading to snap to half rolls, not the line. Better: let
the line move in steps of 10 to 25 nuclei (so 500 is reachable), snap the reading to half rolls, and ask for a roll
before accepting a mark. Teaching may weigh the giveaway side too. *general*

**S8. The Geiger counter clicks the same for every sample.** countSample (src.html:129) plays one tone per 100 ms
frame, 10 per count, whatever the activity. Measured with Sound on: deep core wood (2 counts) gave 9 tones, fresh leaf
(1,360 counts) gave 10 (frames/geiger.json). A counter's sound is a meter, and here it says a dead sample and a living
leaf are equally active. Better: click once per counted decay, thinned (for example, about count / 20 clicks spread at
Poisson-random times over the second), so the leaf crackles and the core ticks twice. This goes with B1's separate
clicks toggle. *general*

#### Polish

**P1. The half-life card still says "Press Mark a half-life" after Mark is pressed.** With Mark on and the handle not yet
moved, #half-card reads "Press Mark a half-life. Move the line to half the starting crowd." (frames/h375-tray.png,
tray-1920.png and d20-ten.png with Mark pressed). Better: "Drag the line to 500, then read the roll number." *general*

**P2. Small nuclei don't look packed.** Nucleons are drawn on a sunflower spiral with a fixed radius and dot size worked
out from the circle, so C-14 is 14 scattered 3 px dots with gaps (zoom-nuclei-1366.png), and H-2 and H-3 are two or
three dots far apart, with the symbol drawn over them at 375 (h375-ladder.png). The spec says "packed protons and
neutrons". Better: size the dots so neighbors touch (dot radius about rad / sqrt(A) x 0.9) and shrink the nucleus to
fit A. Large nuclei (U, Ba, Kr) already look right. *general*

**P3. One Clear wipes both modes, with no confirmation.** Clear in Nucleus also clears the dated samples
(frames/clear-cross.json: "3/7 samples dated" became 0 after Clear in Nucleus). Better: each Clear resets its own mode,
or the button says "Clear all progress" and asks once. *general*

**P4. At 375 wide the graph's plot area is about 45 px tall** (h375-tray.png, audit state-tracked-375x812.png): 1000, 500
and 0 crowd together and the observed points are hard to tell from the curve. With S1 fixed, give the graph a minimum
of about 140 px of plot at phone width. *general*

#### Nits

- **N1.** The graph's equation label uses an ASCII hyphen and a caret, "N = 1000 × (1 - 1/6)^n" (src.html:115). A true
  minus and a superscript n would match Plane.fmt's style. *family:graphing*
- **N2.** Track one always picks the lowest-numbered live die, so the first tracked die is always die 1 in the top
  left corner (frames/tray-1920.png). A seeded random live die would feel less staged. *general*
- **N3.** The style block is six layers of @media overrides restating the same selectors (src.html:4 to 64), which
  will make the polish round's layout fixes (S1, S5, P4) easy to get wrong. Fold them into one block per breakpoint
  while fixing. *general*

#### Checked and clean

- **Contract:** one file, 107 KB; no `src=`, external `href`, `@import` or `url(http`; the only `new Audio` is the kit's
  clip player. No console errors or exceptions in my 41 driven shots (the only error was the host page's favicon 404).
  Kit used for Motion, Sound, Read, tones, voice and Plane, with nothing re-implemented. Title, description, lang,
  charset and viewport are present.
- **Access:** the Tab order runs header, die picker, roll controls, toggles (frames/tab-order.json). Nothing takes focus
  on load (focus-load: BODY). The focus ring is clearly visible (focus-die.png). Targets are 44 px (audit clean at every
  size). Live and decayed dice differ by more than color (6.76:1 plus an x). Motion off: no animations, and roll timing
  is kept (calm-roll.json: still busy at 150 ms, 0 animations).
- **Lines:** all 17 strings from `__tool.allLines()` match voice/lines.json word for word, in order (frames/lines.json).
  `tooOld` is in EVENT_IDS. The 12 hint lines are Read-only and correct for their states.
- **Words:** no em dashes in src.html, notes.md, lines.json, tool.draft.json or handoff.md. "Curio Class" is never
  shortened. Classroom-safe throughout. Privacy: "Saved on this device only" sits under the cards and samples in both
  modes.

#### Standard voice check

Driven with held clicks (0.12 s), Sound on (switched on before the first tap with a scripted click, because of B1),
Motion on, 1366x768. Gaps were 5 s for repeats and 0.2 to 1.2 s for the stale runs. Logs: lens-craft/voice/*.json.

| line | kind | action | expected | spoken |
|---|---|---|---|---|
| trackTip | how | Track one x5 | 1 | 1 (then not queued) |
| wRoll | welcome | first tap on a die | 1 | 1 |
| wRoll | welcome | first tap on Roll once | 1 | **0** (S2) |
| wRoll | welcome | first tap with Sound at its default | 1 | **0** (B1) |
| wNucleus | welcome | Nucleus x2 in a mode cycle | 1 | 1 |
| wDating | welcome | Dating lab entry | 1 | 1 (wording S3) |
| tooOld | event | Calculate x5 on deep core | 5 | 5 |
| read | read | Read x5 | 5 | 5 |
| (none) | - | Roll once x5, Check x5, die x5 | 0 | 0 |

1. **Repeats:** right for every line the tool speaks (table). The first two tooOld lines were cut by the next one
   (`now`), because the headless browser voice ran past the 5 s gap. That is expected for an event line with `now`.
2. **Stale:** Dating, core, Estimate, Calculate, Roll, Reset at 1.2 s: tooOld was cut by the mode change (`hush`),
   then wRoll started and was cut by Reset. Nothing played after its moment. Track then Reset at 0.2 s: trackTip
   was cut (`hush`) and not replayed. Mode buttons at 0.2 s: each welcome was cut by the next mode, and only the
   current one was left (voice/stale-*.json).
3. **First tap:** stage (tray) gives wRoll at 129 ms; key (Tab) gives wRoll at 2 ms; Nucleus gives wNucleus at
   144 ms; Track one gives trackTip only; Read gives the hint only; d20 gives wRoll. Roll once gives nothing (S2).
   With the default Sound: any first tap gives nothing (B1), and Sound as the first tap turns Sound on and gives
   wRoll, which is right for a Sound-on tap. Sound on, off, on (1.1 s apart) brings wRoll once, cut by the off, and
   it does not come back. That is kit behavior (a line is marked said when it starts), not this tool's.
4. **Read:** Read 0.75 s into wNucleus cut it and spoke the hint. Dating 0.75 s after Read started wDating at once.
   Read with Sound off spoke the hint (voice/read-cut.json, read-soundoff.json).
5. **Order:** Track then Dating lab 0.4 s later: trackTip was cut, wDating followed. No older line played after a
   newer one (voice/order.json).

#### Audit pilot

**Leads confirmed:**
- "Welcome not heard" after 19 first taps: true, and the main cause is B1 (Sound starts off), which the audit row for
  `#sound` hints at (welcome heard only there). With Sound on, the same rows clear except Roll once and Roll to 10,
  which stay silent for a separate reason (S2).
- The header Sound starts off: confirmed at src.html:145. The spec scopes "off by default" to the Geiger clicks only.

**Leads that were wrong:**
- "Age estimate overlaps 13.6" and "6.8 under rect" at 680x425 (four states): this is only the handle's transparent
  hit rectangle. The visible diamond sits below the bar, clear of every label (frames/zoom-ruler-680.png).
- "Expected curve drawn across Half-life line" (marked, five sizes): the dashed curve meets the handle where the line
  crosses it, which is the reading itself, not a clash.
- "Clear: nothing changed" in both modes: the audit ran on empty progress. Clear works (clear-cross.json), but see P3.

**Found that it missed:**
- S1: the tray is unreadable at every size. The audit checks boxes, not canvas content.
- S5: ladder bars cross their labels at 375. The audit's "line drawn across" check did not catch SVG `line` elements
  over `text` in this state.
- S3: the spoken welcome and the hint give different steps.
- S4: nucleon colors at 1.04:1, with a misleading legend.
- S6: aria-disabled buttons styled as live.
- S7: the half-life line can't reach 500, and a mark is accepted with no data.
- S8: the Geiger clicks don't follow the count.
- P1 and P3: card wording that is wrong for the state, and Clear's reach across modes.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: half-life-dice

Played cold twice: as a grade 10 student alone at home (Sound as the tool starts it, no teacher), and as a teacher
projecting at 1366x768 and 1920x1080. Bundle: tools/half-life-dice/half-life-dice.html (built 2026-10-29 00:22).
My frames: S:/CurioClass-codex-scratch/half-life-dice/lens-play/f1/ (shots1-4.json beside it). Audit frames looked
at: S:/CurioClass-codex-scratch/half-life-dice/audit-r1/ (size-1366x768, state-marked-1366, state-d6-ten-1920,
state-tracked-680 and -375, state-mode-nucleus-1366, state-right-1366 and -375, state-wrong-1366, state-fission-680
and -375, state-mode-dating-lab-1366 and -800x500, state-noise-1366 and -375, state-too-old-680,
state-average-760x900, state-mid-roll-680).

Counts: **0 blockers, 8 should fix, 8 polish, 4 nits.**

#### Should fix

1. **The tray of dice is not a tray of dice at most sizes.** Roll mode, `drawTray()` (src.html line 104). The 40 x 25
   grid is stretched into a wide, short box and each die is sized by the row height, so the dice become 40 vertical
   stripes of 3 to 6 px squares with 15 to 20 px gaps. At 1366x768 the faces are about 5 px and can't be read, and at
   680x425 the tray is a band of 2 px slivers. Only 760x900 and 1920x1080 look like a tray. The ring on a tracked die
   is cut off by the canvas top (die 1 is in row 0). For a teacher projecting, this is the tool's main picture.
   Seen: size-1366x768, state-mid-roll-680x425, state-tracked-375x812, my 01, 02, 05 and the zoom z05.png. What
   better looks like: keep the cells square and centre a block that fits (or pick the column count from the box's
   aspect, still 1,000 dice), with faces at 9 px or more at 1366x768. **general**
2. **"Drag the graph handle to 500 nuclei" can't be done, and the half-life can be marked without rolling.** Roll,
   Mark a half-life (`snap` in drawGraph, line 107). The handle snaps to the expected curve's height at each half
   roll, so a careful drag to 500 lands on 482 (or 527). The reading then comes from that snapped height, so it is
   nearly always the snap step, whatever the tray did. With 0 rolls the card says "Accepted. Expected crossing:
   4.0 rolls. Exact for a d6: 3.802." The cheap path is Mark, then arrow keys until "Accepted", with no dice rolled.
   Dragged to the bottom it reads "Expected crossing: 25.5 rolls", off the graph. Seen: my 04 (drag to 500: y 482.25,
   "Accepted. Your tray: 4.0 rolls"), 04b, audit state-marked-1366x768. Better: snap the line to 25-nucleus steps so
   500 is reachable, read the crossing from the tray's own points, and ask for Roll to 10 first, with the card saying
   so before it marks anything. **general**
3. **Roll once and Roll to 10 look live after roll 10 and do nothing.** Roll (`updateRoll` sets only
   `aria-disabled`, and the kit has no style for it). At 10 rolls both buttons keep their bright primary fill, a click
   is silent, and nothing says that Reset starts a new tray. Seen: my 02 (coin, 0 left after 10 rolls, buttons
   unchanged), 03, 06. Better: a disabled look, and a hint or card line at 10 rolls that names Reset or New seed.
   **general**
4. **Sound starts off on every load, so a student on their own never hears a welcome.** The load script calls
   `$('sound').click()` after `Curio.init` (line 138), which turns the kit's default (on) off, every time. The spec
   asked only for the Geiger clicks to start off ("A Geiger counter clicks (sound off by default)"). With Sound off,
   all three mode welcomes and trackTip are silent. The audit's 19 "not heard" rows come from this. Seen: audit click
   table, my 22 (first tap on Roll once: empty log, Sound aria-pressed false). Better: leave narration on as the kit
   does and give the counter's tone its own off-by-default setting, or stay silent but say on screen that Sound turns
   on the narration. **general**
5. **The Dating lab welcome skips Estimate.** wDating, "Pick a sample. Drag on the ruler to estimate, then press
   Calculate." (spec line, lines.json). A student who follows it presses Calculate and gets "Press Estimate to record
   your ruler pin before Calculate." The hint (hint12) has the right order. Seen: my 12 (Calculate first), 20 and 21
   (the line is spoken). Better: "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." (the
   hint's words, so one recording serves both). **general**
6. **The estimate step can be skipped for free.** Dating (`estimate`, `calculate`). Estimate takes the untouched pin
   at 1,000 years and Calculate then prints the exact age. "Close." can also be found by sweeping: drag a bit, press
   Estimate, repeat. So "read the age from the ruler first" costs nothing and has no stake. Seen: audit
   state-noise-1366x768 and state-too-old-680x425 ("Estimate: 1,000 years. Compare with the halving ticks." then the
   full answer), my 13. Better: Estimate is only accepted after the pin has moved for this sample, the pin starts at
   0, and Calculate shows the estimate and the exact age side by side ("You read 3,000. Exact: 3,349. Off by 10
   percent."), with no "Close" before Calculate. **general**
7. **Counting noise never varies.** Dating (`countSample` seeds on the sample index). Cave charcoal with noise counts
   337 every time: three noise off-and-on toggles, switching to Hearth and back, all 337. New seed is only in Roll
   mode. A student who turns on "noise" sees one fixed number with a ± after it, and the idea that a recount differs
   by about the square root of the count never shows. Seen: my 10 (`[337, 337, 337, ["hearth", 621], ["cave again",
   337]]`). Better: a `Count again` button that draws the next count from the same seeded stream (so the same seed
   still gives the same sequence, Done when 7), with the counts so far listed so the student sees the spread.
   **general**
8. **The nucleus captions read as "before = protons, products = neutrons".** Nucleus, `drawNuclei` (line 117): the
   left caption is "Before: protons p+ (solid)" and the right one is "Products: neutrons n (outlined)". They are one
   legend split in two, but each sits over a side as its title. "Outlined" also means the proposed product's dashed
   box in the equation below. Seen: state-mode-nucleus-1366x768, state-right-375x812 (zoom z-375-right.png). Better:
   titles "Before" and "After (your product)" over the sides, and one legend line with a dot of each colour:
   "proton p+" and "neutron n". **general**

#### Polish

1. **Light nuclei look like a loose cloud, not a nucleus.** Dot size is capped at 4 px inside a radius set by the
   box, so C-14 and F-18 are 14 to 18 dots scattered across 150 px, while U-238 and the fission fragments are packed
   balls. At 375 wide the symbol labels "C" and "N" sit on the dots and the arrow overlaps the Ba nucleus. Seen:
   state-right-1366x768, my 16 (F-18), state-fission-375x812, z-375-right.png. Better: size the dots so light nuclei
   are packed too, and keep labels and the arrow clear of the drawings.
2. **Steppers start at A 10, Z 3 on every card.** F1 needs 131 presses of + and 53 more; N2 needs 224 and 87 (the
   builder's own audit state clicks + 131 times). Typing works, but nothing says so. Better: start at the parent's
   values, or add -10 and +10 steps or a press-and-hold repeat, and say "or type a number" by the boxes.
3. **Track one is easy to miss and can lead nowhere.** It always rings die 1 in the top-left corner (the first live
   index), where the ring is clipped. After roll 10 it still rings a die and the card says "Chance it decays next
   roll", but no roll is possible. Seen: my 05, 06, z05.png. Better: pick a live die near the middle (seeded), and
   after roll 10 say "Press Reset to track a die from the start."
4. **The d20 tray never reaches its half-life.** Rolls stop at 10, the d20 half-life is 13.5 rolls, and the graph
   already runs to 16, so the card can only ever say "Expected crossing". Seen: my 03. Better: let d20 roll to 16
   (Roll to 16 when the graph goes there), so every die's tray crosses 500.
5. **Each roll is a flat moment.** Dice that decayed this roll turn the same gray as old decays, so the student can't
   see "about 1 in 6 of the live dice went this time". The hint stays "Pick a die, then press Roll once" through rolls
   1 to 9. Better: outline this roll's new decays until the next roll (shape, not only colour), with "162 decayed
   this roll" in the summary, and after roll 1 a hint that points at the graph or Track one.
6. **One look has two meanings.** The green primary fill marks both "do this" (Roll once, Roll to 10, Estimate,
   Calculate, Check) and "this toggle is on" (Show expected, Mark a half-life, Counting noise). Clear sits in the card
   row after F2 and in the sample row after Deep core, styled like an eighth choice, and wipes saved progress with no
   confirm. New seed sits in the die row like an eighth die. Seen: state-right-1366x768, state-noise-1366x768.
   Better: one style for toggles that are on; Clear and New seed set apart from the choices, and Clear asks once.
7. **The energy ladder's log scale has no scale.** The bars start at methane, so the methane rung is a 5 px stub,
   and there are no powers of ten, so "log scale" is a word, not something to read. At 680 and 375 the labels crowd
   the bar above. Seen: state-right-1366x768, state-fission-680x425, z-375-right.png. Better: a faint axis at 1 eV,
   1 keV, 1 MeV and 100 MeV, bars starting at 1 eV, and labels that never touch a bar.
8. **Two cards keep saying the step that is done.** After Mark a half-life is pressed, the half card still says
   "Press Mark a half-life. Move the line to half the starting crowd." (my 03, until the line moves). After a wrong
   Check the change box still says "Your proposed product is outlined. Check both sums to test it." (state-wrong).
   Better: "Drag the orange line to 500." and "Fix the sum that is off, then press Check again."

#### Nits

1. The positron shows as ⁰₁e. The spec writes ⁰₊₁e, and a "+1" pairs with the -1 on the electron (my 16).
2. The graph title "N = 1000 × (1 - 1/6)^n" uses a caret and a hyphen; a superscript n and a real minus read better
   when projected.
3. "Counting noise" wraps onto two lines at 1366x768 and 800x500. At 375 the card buttons lose their names (N1 to F2
   only).
4. Deep core with noise dates to 48,186 years (range 44,834 to 53,916) and says "Too old to date well". Fine with the
   range, but "near the end of the clock's range" fits that number better (my 11).

#### Voice (Sound turned on first; held clicks, 2.2 s gaps)

| line | kind | expected | spoken |
|---|---|---|---|
| wRoll | how | 1 | 1 (on Sound on) |
| trackTip | how | 1 in 5 Track one taps | 1 |
| wNucleus | how | 1 | 1 |
| wDating | how | 1, not again on return | 1 |
| tooOld | event | 3 of 3 core dates | 3 |

Order and staleness looked right in these runs. The problems are which words (Should fix 5) and that Sound starts
off (Should fix 4).

#### Checked and fine

- The Nucleus Check gives both sums ("Mass numbers: 14 ≠ 10. Charges: 6 ≠ 2.") but never the product. Working from
  the sums is the balancing skill itself, so I don't count it as a giveaway. The element name follows Z as intended.
- Reset in the middle of Roll to 10 stops cleanly (rolls 0, not busy). Calculate during a count says to let it
  finish. Motion off keeps the 400 ms roll (my 08).
- Average 20 runs hugs the dashed curve (mean 164.45 at roll 10), and the dotted mean reads clearly at 760x900.
- Fresh leaf: an estimate of 0 years is "Close." (my 13). No console errors in any of my shots.

#### Audit pilot

- **Leads confirmed:** the 19 "welcome not heard" rows are real for a student who keeps the defaults. The cause is
  Sound starting off (Should fix 4), not the voice code: with Sound on, every welcome played once (my 20, 21).
- **Leads that were wrong:** the Dating lab overlap at 680x425 (g "Age estimate" over "13.6", "6.8" under a rect) is
  the pin's transparent hit box; on state-too-old-680x425 the pin and both labels are clear and legible. The "line
  drawn across" in the marked state is the expected curve crossing the half-life line, which is the point of the
  activity. Clear's "nothing changed" is the empty-progress case.
- **What it missed:** the tray's stretched grid and unreadable faces at 1366x768 and 680x425 (Should fix 1): it
  checks text and boxes, not what a canvas draws. It also missed the dead Roll buttons after roll 10 (they are only
  aria-disabled, so the walk marks them ok), the half-life line that can't reach 500 and the marking with no rolls,
  the hollow Estimate gate, the noise count that never changes, a welcome line that names the wrong next control, the
  nucleus captions that read as titles, and SVG labels drawn on the nucleon dots and the arrow over the Ba nucleus at
  375 wide (text over shapes in the same drawing, not over boxes).

<!-- end part -->

<!-- part: refine/sensitivity.md -->

PASS

Sensitivity review, half-life-dice (rule 5). Read: spec.md, src.html (SAMPLES, CARDS, hints, date result text, sample-kind label), notes.md, voice/lines.json.

Summary: the two real samples are named plainly and once each, with no joke, game framing or flourish. Neither sample is human remains, and the tomb appears only as where the seeds were found. The voice (curious-librarian) only gives instructions and never jokes about the samples. The medical and fission mentions are short, neutral and accurate. Nothing blocks.

#### Findings

1. Where: src.html SAMPLES `scrolls` name "Dead Sea Scrolls paper"; spec.md Content; notes.md Good to know.
   What: the Dead Sea Scrolls are mostly parchment (animal skin), with some papyrus, not paper. Even if the textbook says "paper", it is inaccurate for the real artifact. Suggest "Dead Sea Scrolls fragment" (or "parchment"), keeping the 10.8 dpm/g textbook value.
   Level: should fix

2. Where: notes.md Good to know (the line naming the OpenStax examples); src.html sample-kind label "OpenStax example".
   What: a teacher needs one sentence saying these are real artifacts, but the activity values are textbook illustrations, not the measurements from the published radiocarbon studies. The published dates for the scrolls span roughly the 3rd century BCE to the 1st century CE across different scrolls, so the tool's 1,906 years (uncalibrated) falls at the young end. The Tutankhamun figure (about 3,350 years) agrees with the tomb's known date of about 1323 BCE. Suggest: "Both are real artifacts. The activity values are simplified textbook examples; published radiocarbon studies of the scrolls give a range of dates across many scrolls, and real dates are calibrated." Optional context for the class: the scrolls are ancient Jewish texts, many of them religious, found near Qumran. The seeds come from the burial of an Egyptian king. Plain naming is already respectful, so this context is optional.
   Level: should fix

3. Where: src.html CARDS N3 context "Thyroid treatment."
   What: accurate. Iodine-131 is also used in thyroid imaging, so "Thyroid treatment and imaging" would be fuller. Optional.
   Level: nit

4. Where: src.html CARDS N4, N5, F1, F2; energy ladder.
   What: no change needed. Cobalt-60 (radiation therapy), fluorine-18 (PET scans) and the uranium-235 fission and D-T fusion examples are neutral and accurate, with no mention of weapons or disasters, and they match OpenStax 21.3 and 21.4 and NNDC.
   Level: none (noted for the record)

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: half-life-dice

I read spec.md, src.html, notes.md, voice/lines.json, codex-report.md and handoff.md cold, treating the builder's
claims as claims. I worked on the existing bundle, tools/half-life-dice/half-life-dice.html. Frames and scripts are in
S:/CurioClass-codex-scratch/half-life-dice/lens-teaching/ (f1/ and f2/ frames, the nums.py recompute, shots1.json,
shots2.json). I read and cite the shared audit (audit-r1) but did not re-run it. The 5,730 vs 5,700 question belongs
to the owner and is not reported here.

Counts: blockers 1, should fix 6, polish 4, nit 3.

#### Blockers

1. **Roll, Mark a half-life (src.html:116 markMove, :117 snap):** the card tells a student to move a line that already
   sits at half the crowd. Acceptance compares the crossing on the student's own noisy tray with the exact half-life
   (within 0.5 rolls), so when the tray runs slow or fast, a correctly placed line is refused.
   - Default seed, d12: a line at 498 nuclei gets "Move to half the crowd. Your tray: 8.5 rolls. Exact for a d12:
     7.966." The only line accepted is at 544 nuclei ("Accepted. Your tray: 8.0 rolls").
   - Seen in f1/t02-d12-line498.png against f1/t03-d12-line544.png, and recomputed in nums.py. My mulberry32 copy
     reproduces the tool's tray points exactly.
   - The same tray noise affects d8 and d10: their accepted lines are at 513 and 504, and the snapped line just below
     500 is refused.

   The feedback is wrong about what the student did. It teaches that their reading is the mistake, when the real
   lesson is that one tray scatters around the exact value. Better: accept the line by where it sits (500, or the
   step nearest 500), then report "Your tray crossed at 8.7 rolls; exact 7.97; one tray scatters, try Average 20 runs".
   The spec's own rule (accept within 0.5 rolls of exact) fails for a single tray, and the integrator should record
   that against the spec. Tag: general (an estimate that misleads when its assumption does not hold).

#### Should fix

2. **Roll, Mark a half-life handle (src.html:117 snap):** the hint says "Drag the graph handle to 500 nuclei", but the
   handle snaps to the expected curve's value at each half roll, so for most dice it cannot sit at 500. On a d6 it
   jumps between 528 and 482 (its aria valuetext reads "528 nuclei; move to half the starting crowd"). The student is
   asked for something the control will not do. And because the line follows the expected curve, the tool picks the
   reading. Seen in f1/t04-d6-marked.png and the valuetext in the shots1 output. Better: snap y to 500 (or to steps of
   25) and let the card read the crossing on the tray. Tag: general.

3. **Roll, d20 (src.html:109, roll capped at 10):** the tray stops at roll 10, but a d20's half-life is 13.5 rolls. A
   d20 student never sees their own tray reach half, and the card falls back to "Expected crossing", even though the
   graph is drawn out to roll 16. The spec does not set this cap: "Roll to 10" is a button, not a limit. The
   comparison "bigger die, longer half-life" loses its slowest case. Seen in f1/t05-d20-marked.png (Roll once is
   disabled after roll 10). Better: let Roll once continue to the graph's end (16 for d20), or say on the card that a
   d20 needs more than 10 rolls. Tag: general.

4. **Roll, tray (src.html:109 roll, :112 drawTray):** the student never sees a 1 cause a decay. A die that rolls 1 turns
   gray in the same frame its face would appear, so no 1 is ever drawn. At 1366x768 the faces are also about 5 px and
   can't be read (f1/zoom-tray.png, cropped from t02). The rule card says "Every 1 has decayed", but nothing on screen
   shows it. Better: hold the new faces for a beat with the 1s outlined in the accent, then gray them, and draw faces
   at a readable size wherever the tray has room. Tag: general.

5. **Nucleus, drawing (src.html:126 drawNuclei):** the drawing gives two wrong pictures of a nucleus.
   - (a) The legend is split across the two halves: "Before: protons p+ (solid)" sits over the left nucleus and
     "Products: neutrons n (outlined)" over the right. It reads as "before is protons, products are neutrons", and
     neither color is visibly solid or outlined.
   - (b) Protons fill the center and neutrons form an outer shell, because the spiral layout colors the first Z dots
     as protons. That is a specific wrong structure. Small nuclei also show as scattered dots, where the spec asks for
     "packed".

   Seen in f1/t08-nucleus-default.png, f1/t11-f1-right.png and the audit's state-right-680x425.png. Better: one legend
   line with colored swatches ("● proton ● neutron"), protons and neutrons mixed through the cluster, and the dots
   packed. Tag: general.

6. **Nucleus, energy ladder (src.html:127 drawLadder):** the bars start from methane's value on a log scale with no
   tick marks. Methane looks like zero, and carbon-14 decay looks like more than half of fission, though it is about
   1/1,300 of it. The ratio line says "Log scale", but nothing on the bars shows the powers of ten. At 680x425 each bar
   is also drawn through the next rung's label ("D-T fusion" is struck through in the audit's
   state-right-680x425.png).
   This ladder is the energy half of HS-PS1-8 (the scale of nuclear energy against chemical energy), and the student
   only reads it. Better: ticks at each power of ten (1 eV, 1 keV, 1 MeV, 1 GeV), points or bars from a stated origin,
   and labels clear of the bars. Also give the student one action, such as placing the rung for the card they just
   balanced before it is revealed, so the energy comparison is something they do, not only something they are shown
   (BASELINE rule 2: taught well, not thinly). Tag: general.

7. **Dating lab, ruler (src.html:135 drawRuler, :132 "Close" test):** the ruler cannot be read closely enough for the
   10 percent "Close" check. It labels only whole halvings (13.6, 6.8, 3.4 and so on), so the two real samples fall
   between ticks with nothing to show the log spacing.
   - Reading 10.8 straight across from 13.6 to 6.8 gives 2,359 years against 1,906 (24 percent off).
   - Reading 9.07 the same way gives 3,817 years against 3,349 (14 percent off).
   - Both get "Compare with the halving ticks."
   - Every practice sample sits exactly on a labeled tick.

   So the Estimate step is either trivial (the practice samples) or a sweep: drag, press Estimate, repeat until
   "Close", free and unlimited. Recomputed in Python; seen in f1/t13-scrolls-calc.png and f1/t14-cave-noise.png.
   Better: minor activity marks between the ticks at their log positions (12, 11, 10, 9, 8, 7 dpm/g), and one Estimate
   per sample before Calculate. Tag: general.

#### Polish

8. **Roll, tracked die and the "no memory" idea (src.html:106 updateRoll):** "Chance it decays next roll: 1 in 6" is a
   fixed string, so Done when 3 passes because the screen says so. Better: a line per roll from the crowd ("This roll:
   98 of 591 decayed, 17%"), so the student sees the same fraction at every age in their own data. Tag: general.

9. **Nucleus, N4 gamma:** gamma is one of the three decays HS-PS1-8 is limited to, but it appears only in words after
   Check. Better: show ⁰₀γ in the N4 equation once it is balanced. Tag: general.

10. **Dating lab, wDating welcome (spec line):** "Drag on the ruler to estimate, then press Calculate" skips the
    Estimate button, and Calculate needs Estimate first. The hint (hint12) has the steps in the right order. Better:
    "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." This is the spec's line, so the
    integrator decides. Tag: general.

11. **Sources line (tool.draft.json and notes.md "Good to know"):** 17.6 MeV and "about 200 MeV" are credited to
    OpenStax 21.4, but that page gives neither number. I fetched it on 2026-10-29. It gives the Ba-141 + Kr-92 + 3 n
    equation, fission at 1.8 × 10¹⁰ kJ/mol (186.6 MeV per event), and D-T fusion at 1.69 × 10⁹ kJ/mol with a mass
    loss of 0.0188 amu (17.5 MeV). The spec asked the builder to confirm these values against the page, and
    codex-report says the pages were not fetched. The values themselves are physically right (the D-T Q-value is
    17.59 MeV). Better: cite NNDC or another named source for the two MeV values, or mark them as derived.
    Tag: general.

#### Nits

12. **Nucleus, positron (src.html:120 iso):** N5 shows ⁰₁e where the spec writes ⁰₊₁e. The plus sign helps students
    read it as a positron. Tag: general.
13. **Roll, Mark before any roll:** with no rolls yet, the card accepts a line read from the expected curve alone
    ("Expected crossing"). It does no harm, but the student's tray is skipped (f1/t06-premark-norolls.png).
    Tag: general.
14. **Rule 8, notes.md:** N3 to N5 name thyroid treatment, radiation therapy and PET scans. A teacher-note line saying
    these touch on cancer care (a student may have someone in treatment) would fit rule 8. Tag: general.

#### Sensitivity referral (rule 5)

Low risk, for the integrator to route. The Dead Sea Scrolls (religious texts) and seeds from Tutankhamun's tomb (a
burial) are named samples. Both are OpenStax examples and are used factually. I did not judge them.

#### Standards (rule 2)

HS-PS1-8 is the only code on the module.
- Changes in the nucleus: taught by balancing seven products. This is a real student action and it works.
- Decay over time: taught by rolling and marking. It works, with findings 1 to 4.
- Energy released in fission, fusion and decay compared with other changes: shown, not done (finding 6).

The code can stay once finding 6 gives the student an action. N5's positron decay goes past the standard's limit to
alpha, beta and gamma. That extension is fine and is not a finding.

#### Done when

1. PASS. The d6 expected count at roll 10 is 161.5, and the mean of 20 runs stays within 5.59 of the expected curve at
   every roll (default seed, recomputed with my mulberry32 copy, which matches the tool's tray). The worst over 7 more
   seeds was 6.29.
2. PARTIAL. All seven exact half-lives match Content (1.000, 2.409, 3.802, 5.191, 6.579, 7.966, 13.513 rolls). But
   accepting a marked half-life within 0.5 rolls fails as a teaching check: correct lines are refused (finding 1), and
   a d20 is never read from the tray (finding 3).
3. PASS as written: the same "1 in 6" at ages 0 to 6 (f1/t07-track.png). See polish 8.
4. PASS. Check compares the mass and charge sums. They are linear, so exactly one (A, Z) passes per card. Seen right
   on N2 and F1 and wrong on N5 ("Charges: 9 ≠ 11"). The other products are fixed, so nothing beyond the sums the spec
   asks for gives the answer away.
5. PASS on content: four rungs and the 22 million ratio (200 MeV ÷ 9.2304 eV = 2.17 × 10⁷). How it reads is
   misleading (finding 6).
6. PASS. Ages are 1,906, 3,349, 22,920 and 53,916 years, with "Too old to date well" on the last. The noise run gave
   337 counts ± 18 and a range of 11,095 to 11,996 years (recomputed). At 340 counts: ±18.4, a range of 11,023 to
   11,921, matching the spec's rounded 11,020 to 11,920. The mammoth bone at 22,920 years correctly gets no flag.
7. PASS. Reset repeats the same tray (t24-seed returned true). Progress survived a fresh tab (3/7 cards, 4/7 samples),
   and Clear set it to 0/7, which stayed after a reload. For Motion off I cite the audit's clean row.
8. Cited from the audit: every size clean, the Enter-twice keyboard check ok, no console errors (also none in my 21
   driven shots). This lens did not re-shoot it.

Other numbers recomputed:
- Methane: 890.6 kJ/mol ÷ NA = 9.2304 eV per molecule.
- Per nucleon: fusion 3.52 MeV, fission 0.847 MeV.
- Ruler labels: 13.6/2^k, all correct (0.2125 shows as 0.212, which is fine).
- OpenStax 21.3 confirms the 5,730-year half-life, the 13.6 activity, the Scrolls at about 1,900 years, the
  Tutankhamun seeds at 9.07 and about 3,350 years, and the 30,000 and 50,000 year limits.

#### Giveaways checked

- Nucleus: no hidden answer. The steppers start at 10 and 3, the element name follows the student's own Z, and Check
  gives only the sums the spec asks for.
- Dating: no age shows before Calculate, but "Close" can be found by sweeping (finding 7).
- Roll: the exact half-life prints on the card from the first drag. The spec wants that, but because of finding 1,
  "Accepted" can also be found by sweeping: drag until it appears.

#### Language and guardrails

The language is plain and right for grade 10. The ln(ratio) steps are shown, never asked of the student. There is no
hard history and there are no points or timers. The health topics (thyroid treatment, radiation therapy, PET) are
neutral (nit 14).

#### Cross-lens notes (not counted)

Sound starts off: the last lines of src.html call $('sound').click() at load. The spec asks only for the Geiger
clicks to start off, but as built no welcome is heard until the student turns Sound on. This is for Play and Craft to
settle under rule 4.

#### Audit pilot

- **Leads confirmed:** at 680x425 the Dating handle's hit area overlaps "13.6" and "6.8", but only the invisible hit
  area does. The visible text is clear on the frames, so it is not a teaching issue. "Welcome not heard" after every
  first tap is real, and the cause is that Sound starts off (cross-lens note).
- **Leads that were wrong or empty:** in the marked state, "expected path drawn across Half-life line" is the curve
  meeting the line, not a defect. Clear "nothing changed" only because there was no saved progress yet; my t22 shows
  Clear takes 3/7 back to 0/7.
- **Missed:** the ladder bars drawn through their labels at 680x425 show in the audit's own frame
  (state-right-680x425.png), but its "lines drawn across labels" check did not flag them. It also missed the issues
  in this file, which are teaching, giveaway or meaning problems the audit does not claim to see:
  - the wrong acceptance feedback on a correct half-life line (1);
  - the handle that cannot reach 500 (2);
  - the d20 roll cap (3);
  - no 1 ever shown, and 5 px faces (4);
  - the split, mislabeled nucleon legend and the proton-core drawing (5);
  - the log ladder with no ticks (6);
  - the ruler that can't be read (7);
  - the source attribution (11).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: half-life-dice

Blocker 1 done: default Sound is on; separate Counter clicks defaults off; first-roll-voice log starts wRoll after a held Roll tap; notes corrected.
Blocker 2 done: 25-nucleus steps accept 500 after a roll; no-data Mark refuses; d12 observed 8.5 versus exact 7.966 explains scatter, functional JSON.
Should fix 1 done: adaptive square cells, 10.8 px faces at 1366 and 16 px at 1920; centered ring and outlined landing 1s viewed in normal and calm frames.
Should fix 2 done: d20 reaches roll 16 and 465 survivors; its observed half crossing is 14.5; Roll to 10 remains separate.
Should fix 3 done: busy, averaging and cap states dim via aria-disabled; cap and Track cards name Reset; functional JSON verifies both buttons.
Should fix 4 done: Roll controls removed from speaks; first held Roll once starts wRoll with default Sound, polish-first-voice.json.
Should fix 5 done: wDating matches the hint and recording bank; Calculate is secondary until a recorded Estimate and explains its gate.
Should fix 6 done: pin starts unplaced, movement required, one locked Estimate, log-position minor marks, exact age and percent difference revealed only by Calculate.
Should fix 7 done: cave counts 337, 324, 366 repeat for the same seed; Count again and count history verified in functional JSON.
Should fix 8 done: seeded uneven click times, 68 clicks for a leaf versus 2 for deep core; toggle off is silent, header Sound gates tones.
Should fix 9 done: Before/After titles, one legend, mixed touching filled/ring nucleons; grayscale N2 frame shows 184 protons and 292 neutrons.
Should fix 10 done: 1 eV origin and four labeled log ticks; rung and tick labels have zero bounding-box overlaps at 375, 680x425 and 800x500; all three final frames viewed.
Should fix 11 done: Dead Sea Scrolls fragment replaces the old name in tool and notes; activity stays 10.8.
Should fix 12 done: teacher notes explain real artifacts, simplified textbook activities, calibration, tomb date and family medical sensitivity.
Should fix 13 done: active Mark card names dragging to 500; wrong Check card and hint name fixing the failed sum then Check again.
Should fix 14 done: credits, metadata and notes cite College Physics 2e 32.5 and 32.6 for the energy values.
Polish 1 done: every roll reports decayed/live-before counts and percent beside the tracked chance.
Polish 2 done: N4 correct equation includes mass-zero, charge-zero gamma, checked in functional JSON.
Polish 3 done: desktop +/-10, typing hint and held +/- repeat; start values remain 10 and 3.
Polish 4 done: separate seeded tracking chooses an interior live cell; pad and ring keep it inside the canvas.
Polish 5 done: toggles share an inset outlined style, actions stay solid; New seed/Clear are dashed; each Clear resets only its own progress.
Polish 6 done: phone graph reserves 231 px with no padding, rendered plot is 138 px, about 140; long d20 scatter state now has zero scroll.
Polish 7 done: positron equation shows +1 below e, functional N5 equation checked.
Polish 8 done: graph label uses a true minus and superscript n, native frames viewed.
Polish 9 done: noise labels stay on one line, phone cards retain short names, core range wording and N3 context updated.
Settled 1 done: Sound on, Counter clicks off, functional defaults and held welcome checked.
Settled 2 done: 500-only line acceptance, observed crossing and scatter explanation, no pre-roll acceptance.
Settled 3 done: graph-end roll cap with d20 continuing past 10, functional roll-16 check.
Settled 4 done: exact revised wDating line used for welcome and hint, bank equality checked.
Settled 5 done: Count again is a button inside noise, advancing the seeded stream and showing history.
Settled 6 done: reaction and energy citations separated in credits, metadata and teacher notes.
Settled 7 done: fragment name used throughout the current tool and teacher notes.
Settled 8 done: transparent hit-area intersections and empty Clear are understood as intentional; final audit review pending.

#### Checked

Evidence is in S:/CurioClass-codex-scratch/half-life-dice/.
Functional sweep: all seven half-lives and products, separate mass/charge failures, all seven sample ages, sqrt(count), seed reproduction and independent Clears.
d6 expected at 10 is 161.5056; twenty-run mean 164.45; maximum error across rolls 5.5944.
First and adjusted sweeps cover all three modes at 680, 800, 760, 1366, 1920 and 375 through drive.py host 8796.
All 36 initial/fit frames viewed through six contact sheets, with compact and phone originals inspected.
Five functional frames include a grayscale nucleus and matching 210 ms normal/calm landing beats.
The tool made zero resource requests and its driven console was clean; the outer drive.py host emitted its favicon 404.
Compact ladder re-drive: ladder-final-375/680/800.json all have overlaps=[] and scroll=[0,0]; three polish-ladder-final frames viewed.
Keyboard-only Tab/Space/arrows paths pass for roll/500 marker, balanced N1 and Estimate/Calculate; polish-keyboard-*.json.
Exact noisy 340 count gives sigma 18.4391 and 11,023 to 11,921 years; polish-noise340.json.
Final scratch shipping copy: phone d20 scatter, F1 and core noise all have zero scroll; four frames viewed, console clean.
First Calculate now also starts wDating; polish-calculate-voice.json. Automatic narration uses only the five spec lines.
Official full audit and cleanup are running; the bundle under audit is held stable. Final source fixes will be re-bundled afterwards.

#### Left open

The full audit and process cleanup remain to be completed. Compact ladder spacing is checked and complete.
Owner questions unchanged. No ladder action added; no recordings, git or edits to review files or codex-report.md.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Half-Life Dice handoff

The self-contained src.html uses Curio.voice, theme-912 and Plane. Data precedes state, rolling, nuclear balancing, dating and stable event bindings. The tool has no network requests. Geometry observers rebuild Plane at actual pixel size, defer during a drag and preserve focus with preventScroll. No engine files changed.

#### Polish changes

Roll uses adaptive square cells for exactly 1,000 dice, as allowed by refine Should fix 1. At 1366x768 faces are 10.8 px; projector faces are 16 px. A 400 ms roll includes a final-face beat with outlined 1s before gray decay marks. Motion off keeps the whole timing. Tracking uses a separate seeded stream and excludes edge cells.

Mark moves in 25-nucleus steps. It accepts exactly 500 after a roll, reports only an observed crossing rounded to a half roll, and explains scatter beyond 0.5 rolls from exact. Before crossing, it asks for more rolls. There is no expected-curve fallback. Roll once reaches the graph end, roll 16 for d20; Roll to 10 still stops at 10.

Header Sound stays on. Counter clicks is separate and starts off. Poisson counts advance a persistent sample stream; Count again lists the next counts. Click times use another seeded stream, about one click per 20 decays, with individual clicks for samples of 20 counts or fewer. Count again preserves a recorded estimate for comparison with each measurement.

Each sample starts with an unplaced ruler pin. Estimate needs movement and locks the reading; Calculate reveals the comparison and logarithm steps. No accuracy verdict is available before Calculate. Minor ruler marks follow logarithmic activity positions, with labels admitted only where they fit.

Nucleons use a touching hexagonal cluster, with exact proton/neutron counts mixed by a seeded shuffle. Protons are filled, neutrons are dark-centered rings. F1 draws three emitted neutrons; N4 adds the mass-zero charge-zero gamma only after a successful Check. Negative proposed charge is labeled Not a nucleus. The energy axis starts at 1 eV and has labeled logarithmic ticks. No prediction action was added to the ladder.

The sources, artifact name and teacher sensitivity notes follow the integrator's settled calls. Carbon dating retains 5,730 years. The spec's 11,020 to 11,920 noise endpoints are tens-rounded versions of 11,023.41 to 11,920.94.

Clear removes only its own mode's progress. The stored key remains curio-half-life-dice, with try/catch and visible device-only privacy wording. Inputs support typing, desktop +/-10 buttons and held +/- repeat.

#### Voice changes

voice/lines.json equals V.allLines(), 22 unique strings. wDating changed to: "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate."
The following Read hints were changed or added; none adds automatic narration:
- "Watch Average 20 runs finish. Press Reset for a fresh tray."
- "Drag the line to 500, then read the roll number. Arrow keys move by 25 nuclei."
- "Every roll is done. Press Reset for a fresh tray."
- "Fix the sum that is off, then press Check again."
- "Press Reset to track a die from the start."
- "Roll first, then mark the half-life."
- "Press Estimate first to record your moved ruler pin, then press Calculate."
- "Watch the model counter finish. Then press Calculate to compare this count with your recorded estimate."
- "The line is on 500. Press Roll once until your tray crosses it."
- "Compare your tray with the exact value. Press Average 20 runs to see the crowd settle."
The other automatic lines remain the supplied wRoll, trackTip, wNucleus and tooOld. tooOld is the explicit repeatable event. Roll and Calculate buttons no longer suppress the first welcome. There is no post-roll welcome retry, so a first Track instruction cannot acquire a late welcome; wRoll remains valid during the first roll as requested in refine.

#### Engine changes wanted

None. All fixes use local layout, drawing, control and focus code.

#### Verification

See polish.md for this round and the scratch polish-* and audit-polish evidence. codex-report.md remains the original build record. The two owner questions remain open: carbon-14 half-life choice and a student action on the energy ladder.

<!-- end part -->

## Log

- 2026-11-25: CODEX-BRIEF.md folded in (last changed 2026-10-29)
- 2026-11-25: codex-report.md folded in (last changed 2026-10-29)
- 2026-11-25: refine.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/sensitivity.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-29)
- 2026-11-25: polish.md folded in (last changed 2026-10-29)
- 2026-11-25: handoff.md folded in (last changed 2026-10-29)
