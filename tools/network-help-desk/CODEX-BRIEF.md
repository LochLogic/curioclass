# Codex build brief: network-help-desk (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real fourth graders tomorrow.

The tool is `network-help-desk`. Its spec is `tools/network-help-desk/spec.md`. **Read the spec fully, every line,
before you write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong
or impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

## 0. Ground rules for this run

- **You may write only inside `tools/network-help-desk/`.** Nothing else in the repo. Not `kit/`, not `docs/`, not
  `scripts/`, not other tools.
- If you believe `kit/network.js` or `docs/families/network.md` must change (a bug, a missing feature), do NOT change
  them. List the change in `tools/network-help-desk/handoff.md` under a heading `## Engine changes wanted`: the file,
  the function, what is wrong, the exact change, and why the tool needs it. Then work around it inside the tool, and
  say how. The integrator approves or declines engine changes later.
- The spec has no art: everything is drawn in code (SVG). Do not draw, generate or download any image. Do not record
  voice. Make `art/prompts.json` only if the build tooling requires it (then an empty list in the calm-corner format).
- No git commits, no branch changes, no stash. Leave the work as uncommitted files.
- The tool makes no network requests of any kind. You need no internet for this job.
- **Scratch space: `S:/CurioClass-codex-scratch/network-help-desk/` (writable).** Every screenshot, Chrome profile,
  shots file, audit output and temporary script goes there (or %TEMP%), **never in the repo or the tool folder**. Your
  sandbox cannot delete files afterwards, so anything you leave in the tool folder stays. The last build left stray
  files; do not.
- Ports: Chrome debugging ports **9990 to 9997 only**; the iframe host server on **8795 only**. Other agents may use
  other ports on this machine at the same time.
- Every Chrome you start uses `--mute-audio` (drive.py does this for you). Close every Chrome and server you start.

## 1. Read these, in this order

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice behavior, testing). Where anything differs, it wins.
1. `tools/network-help-desk/spec.md`: everything you build. Read all of it.
2. `docs/agents/BUILD.md`: the build agent brief (the human-agent version of this file), including `audit-states.json`.
3. `docs/agents/decisions/BASELINE.md`: the owner's standing decisions.
4. `docs/TOOL-CONTRACT.md`, `docs/KIT.md` (above all the "Voice: Curio.voice" section), `docs/POLISH.md`.
5. `kit/starter/src.html`: start from a copy of it. Also skim `kit/curio.js` and `kit/curio.css` so you use them
   instead of re-implementing anything.
6. `docs/families/network.md`, `kit/network.js` (read the whole engine), and the "Family engine" section of
   `tools/internet-journey/spec.md`: the family engine this tool must use.
7. **The quality bar:** `tools/internet-journey/` (`src.html`, `handoff.md`, `notes.md`, `refine.md`,
   `voice/lines.json`, `tool.draft.json`). Same engine, grade 3, already through review; its `refine.md` shows what
   reviewers catch. Read it to see the level of care expected (layouts per size, voice wiring, focus handling, map
   drawn at real pixel size). Do not copy its look, scene, voice or palette: network-help-desk has its own (help desk
   green on mint, upbeat-guide voice, a house plan).
8. Formats: `tools/shape-talk/notes.md` (teacher notes), `tools/biased-bot/audit-states.json` if it exists (states file).

## 2. The rules you must follow (quoted from the docs above)

### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 4: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool` with everything the spec lists (`state, net, setMode, openCall(n), ask(n,q), claim(n, cause,
  clues), houseTry(device, target)`) plus `allLines`, the voice log (`vlog: V.log`, `get vq() { return V.queue; }`)
  and whatever a tester needs to read the current call, clues, call time, map badges and House results.

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
- Rule 2: "Every standard is taught well, above the minimum." Each module code in the spec (E4-SYS-NT-14,
  E4-SYS-SE-13, E4-SYS-HW-12) must be really taught by something a student does. Authentication vs authorization is
  the heart of this tool: the Logging in and Permission kinds must be told apart by what the student does, not only
  by a sentence.
- Rule 4: "Every tool stands alone. ... Defaults must work for a solo user; teacher toggles are extras."
- Rule 7: privacy is stated wherever anything is recorded or stored. This tool stores nothing but the kit Motion
  setting; the passwords are pretend (say so where a password appears, if anywhere).
- Rule 5: facts stay plain, with care for the people involved. Callers and the house are fictional; no real brands
  on devices, no real places.

### From STANDARDS.md "Sizes" (check every one, early)
| Size | Why |
|---|---|
| 680x425, 800x500, 1000x625 | the site's 16:10 preview on the tool page |
| 1280x720, **1366x768** | the main use: a school laptop, full screen |
| 1920x1080 | big screens |
| 760 wide | below the 1000 px stack breakpoint |
| 375 wide | phones, inside an iframe host (`python scripts/drive.py network-help-desk --host 8795`) |
- "The main controls (the ones a student uses every few seconds) are visible without scrolling at every size. In short
  landscape boxes keep stage and panel side by side with a compact panel instead of stacking."
- "The preview must be readable (scene text about 10 px or more)." The family doc asks labels 12 px or more at
  680x425; the spec asks room names 14 px or more (keep that at the laptop sizes, and as large as fits in the preview).
- "Draw the stage at real pixel size and re-lay it out per size ... rather than scaling one fixed design." Pass
  `skin.box` in px to `Net.draw` per size, as internet-journey does.
- "Tab order: panel controls before long lists of map items." The spec gives the exact order.
- "Moving focus on purpose uses `focus({preventScroll: true})`."
- "Fit-to-width guards ... re-measure from the loosest step every time and wait for running animations to finish first."
- Spec Done when 7: Questions and Make a claim visible without scrolling at every size; 375 wide works via the host.

### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
- Narrate only through `Curio.voice` (`V.how` for how-to lines, `V.say` for events, with `valid` and `needs`). Never
  write your own queue. `scope: () => state.mode`.
- One welcome per mode (w-calls, w-house).
- "Say how to act. Whenever the tool waits for the student, the line and the hint name the next action and the control."
- "But don't nag. A how-to line is spoken the first time its step comes up; after that it only updates the hint, silently."
- "How-to and teaching lines are spoken once per page load. Event lines (praise, a challenge met, a failed load, a
  result with new numbers) are spoken every time their event happens, and are still dropped when stale. ... Keep an
  explicit set of event line ids in the code." Here the event lines are need-clue, wrong, solved-conn, solved-login,
  solved-perm and shift; the spec gives each one's stale rule.
- "The spoken line matches the state on screen."
- "The hint changes when the state changes. On a tab, panel or mode switch, set the hint at once, then queue the line
  with a `valid` check ... Pick how lines by `V.heard`, never by a counter. The first action never waits behind a line,
  no line names a disabled control, and at a 2 s tap pace no line is lost."
- Callers' words are on screen only, never spoken.
- "Test with held clicks (press, ~120 ms, release)" and read `V.log` to see which clips actually started.
- Spoken text must exactly match a line in `voice/lines.json` so recordings can replace the browser voice later.
  Lines under about 200 characters, nothing a voice would misread.

### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." Fix about 1.5 s, ping 300 ms per hop, Motion on or off.
- "Nothing overlaps by accident." "Test the extremes": all six questions asked (six clue cards) at every size, the
  claim step with two clues selected, Call time after several wrong claims, the Shift report with all 8 calls, the
  tablet dragged to every corner of the plan, all House toggles flipped.
- "Words match the state. Grammar, counts, plurals." ("Call time: 1 min", "Call time: 3 min".)
- "Nothing on screen gives the answer away." The cause board order, clue card order, button styles and map colors
  before a question is asked must not hint at the cause. The faint device outlines must not reveal status.
- "Keep the action area clear": badges, bubbles, login cards and the ping must not cover room names or each other.

## 3. The engine (use it, do not rewrite it)

`<script src="kit:network"></script>` after `kit:curio`. It defines `Net`. Use the parts the spec and family doc
name for this tool: `Net.graph` (router, devices, wire and wifi links, a `cloud` node, the printer), `Net.path` and
`Net.reach` (is there a working path to the cloud or printer), `Net.draw` with a house-plan skin (rooms drawn by the
tool underneath, in `view.layers.back` or an SVG under the map), `view.badge` for the status, account and "?" badges,
per-node `hidden` and `faint`, `Net.token(view, 'ping', ...)` and `Net.send` for the ping, `Net.stop` on any call or
mode change.

**Known gap, read carefully:** the spec says "the engine's Path ignores guest links when the target is a home
device". The engine as it stands has no `guest` concept; it has `skip(link)` and `avoid(node)` options on `path` and
`reach`. Do the guest rule in the tool with `skip` (for a home-device target, skip links marked `guest: true`), and
list under `## Engine changes wanted` whether a built-in option would be better and exactly what it would be. Do not
edit the engine.

The Wi-Fi bars are the tool's own rule (spec Content) and set the wifi link's `up`. Recompute the spec's distances and
bars ("Living room 108 (3), Kitchen 255 (2), Bedroom 361 (2), Back door 481 (1), Shed 648 (0)") in a Node check in
the scratch folder before building; the engine's pure block works in Node if it exports (check how internet-journey
tested it). If your numbers differ, trust the computation, say exactly what differs in handoff.md and
codex-report.md, and do not change the spec.

Never write a literal closing script tag inside your inline script, even in a comment.

## 4. Files to make in `tools/network-help-desk/`

From BUILD.md "Make these files":
- `src.html` from the starter: the kit stylesheet and script, the tool's palette (the spec's `:root` values), its
  scene and logic.
- `tool.draft.json`: "the tool.json fields from the contract, plus `\"stage\": \"built\"`". Fields: id, status
  ("beta"), hook, outcome, driver, minutes, modes, grades_label, sources, third_party, updated ("2026-10-28"), stage.
  The spec's "Who and how" gives driver, minutes, modes and grades_label. Model it on
  `tools/internet-journey/tool.draft.json`.
- `notes.md`: "teacher notes (a 5-minute start, the modes, talk questions, good to know). Look at
  `tools/shape-talk/notes.md`." Include the pairs format (one student reads the caller cards aloud), the three kinds,
  and the authentication vs authorization distinction in teacher words with the NIST source.
- `voice/lines.json`: `{"bank": "upbeat-guide", "voice": "Zephyr", "style": "Say brightly and clearly, like an
  upbeat tour guide", "lines": [...]}` with every line `allLines()` returns (use `V.allLines()`), in the same shape
  as `tools/internet-journey/voice/lines.json`. Do not record.
- `audit-states.json`: the states a student reaches beyond the first screen, as real clicks, keys and drags (format
  in the header of `scripts/audit_tool.py`). At least: a call with all six questions asked; the claim step with two
  clues selected; a wrong claim (ping stopped at the X, nudge shown); a Solved card; the Shift report after all 8
  calls; House with the tablet dragged to the shed; House with the router off and a Try result showing. Give `keep`
  regions (the Questions, Make a claim, the Solved card, the Try result chip).
- `handoff.md`: "a short note for whoever fixes this tool later: how src.html is laid out, the tricky parts, and what
  you would do next." Include the `## Engine changes wanted` section (write "None" if none).
- `codex-report.md`: your report (section 7).

Do not commit the bundle: `tools/network-help-desk/network-help-desk.html` is generated build output (git ignores
it). Delete `tools/network-help-desk/host.html` (made by `--host`) when you finish; if you cannot delete it, say so.

## 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex-network-help-desk`)

Scratch below means `S:/CurioClass-codex-scratch/network-help-desk`.

1. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py network-help-desk` (in PowerShell: `$env:CURIO_DRAFT=1;
   python scripts/bundle_tool.py network-help-desk`). It must bundle cleanly and the result must be under 2 MB.
2. Frames and real input: `python scripts/drive.py network-help-desk <scratch>/shots.json <scratch>/frames --port
   9990 --profile S:/CurioClass-codex-scratch/network-help-desk/chrome-prof-9990`. Read the header docstring of
   `scripts/drive.py` for the shots format. Use held clicks (`"hold": 0.12`) for anything that involves voice. Use
   `"drag"` with whole-pixel, uneven points to drag the tablet (real pointer input). drive.py prints each shot's js
   result and every console error, warning and exception: there must be none.
3. 375 wide: start the host with `python scripts/drive.py network-help-desk --host 8795` (it serves until stopped; run
   it in the background and stop it after), then shots with `"url": "http://127.0.0.1:8795/host.html?w=375&h=812"`.
4. Shoot at least: the first screen at every STANDARDS size; each of the 8 calls with all six questions asked; the
   claim step; a wrong claim mid-ping and after; a Solved card of each kind; the Shift report; House at first, with the
   tablet at each spot (Living room, Kitchen, Bedroom, Back door, Shed), and each of the five failing Try rules; Motion
   off (`"calm": true`) mid-fix and mid-ping; a grayscale frame (never color alone: clue selection, badges, link kinds);
   a keyboard-only solved call.
5. **Look at every PNG** (open each image file and view it). Fix overlaps, clipping, unreadable text, text under
   10 px in the preview sizes, and anything the spec's "Done when" fails.
6. Voice: with held clicks at a 2 s pace, read `__tool.vlog` and check every rule in section 2's voice list.
7. Audit: `python scripts/audit_tool.py network-help-desk S:/CurioClass-codex-scratch/network-help-desk/audit --port
   9991 --profile S:/CurioClass-codex-scratch/network-help-desk/chrome-prof-audit` (bundle first). Answer **every**
   lead in its `audit.md` in `codex-report.md` (fixed, or why it is not a real problem). It is mechanical; a clean
   audit is not a clean tool. Check afterwards that the audit put nothing in the tool folder.

## 6. Self-check list before you report (BUILD.md "Wave lessons (BR1)", turned into checks)

Every tool in the last two waves needed a second review round on these. Check each one explicitly and say how you
checked it in your report.

**Hint and voice**
- [ ] The hint always names the next control, and Read speaks exactly the hint.
- [ ] On a mode switch or a call switch the hint changes at once, not when a queued line starts.
- [ ] How lines are chosen by `V.heard`, never by counters.
- [ ] The first action never waits behind a line.
- [ ] No line names a disabled control (use `needs`). (Example: "Make a claim" before any question, if you disable it.)
- [ ] No line is lost at a 2 s tap pace (held clicks, read `V.log`).
- [ ] A fix made in one place does not cut another line (last time a polish fix cut the welcome).

**Focus and layout**
- [ ] Focus is kept when controls rebuild (a question button greying, the Questions panel swapping to the cause
      board and back, the call strip ticking, House toggles), and nothing takes focus on load.
- [ ] Nothing rebuilds under the pointer.
- [ ] The hint's height is reserved so panels don't jump when its text changes.
- [ ] Labels and badges never overlap (map badges, screen bubbles, login cards, clue cards, room names).

**Sizes**
- [ ] 44 px targets and an unclipped hint at every STANDARDS size, including 680x425 and 375 wide through the host.

**No giveaways**
- [ ] Badges, outlines, order, names, ids and button styles reveal nothing about the cause before it is asked.
- [ ] No call can be solved for free by sweeping the cause board (a wrong claim costs Call time and gives a nudge,
      which is the spec's design; make sure the nudge teaches, not just tells the answer).

**Honest numbers**
- [ ] The Wi-Fi bars say on screen that they are "about" (a model: walls and distance weaken Wi-Fi), and Call time
      says what it counts.

**Standards**
- [ ] Every module code (E4-SYS-NT-14, E4-SYS-SE-13, E4-SYS-HW-12) is taught by something a solo student does, not
      only by a teacher question. Say which action teaches which code.
- [ ] Your use of the engine matches `docs/families/network.md`.

**Motion off**
- [ ] No infinite animations (the kit's `.calm` loops them at 0.01 ms). Timing is the same with Motion off.

Also: no console errors at any size; Escape or Back to questions returns focus sensibly; the tablet moves with arrow
keys 20 units per press and stays inside the plan; Reset house restores everything; Start a new shift clears ticks;
an unfinished call keeps its clues when you open another and come back.

## 7. Report: write `tools/network-help-desk/codex-report.md`

Use this format exactly:

```
# Codex report: network-help-desk

## Built
(files made, one line each)

## Numbers check
(the spec's distances and bars next to yours; any difference and why)

## Done when
1. PASS or FAIL: evidence (frame file names, js results, V.log excerpts)
... (all 8 spec items)

## Self-check (section 6)
(each item: PASS or FAIL, and how you checked it)

## Audit leads
(every lead in audit.md: fixed, or why not)

## Frames looked at
(every PNG, with its size and what it shows; say you viewed it)

## Engine changes wanted
(same as handoff.md, or "None")

## Left open
(anything not done, not checked, or that you are unsure of)
```

Be honest: a FAIL you report is worth more than a PASS you did not check. When the report is written, you are done.
