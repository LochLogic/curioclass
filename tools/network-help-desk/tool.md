# Network Help Desk: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: CODEX-BRIEF.md -->

### Codex build brief: network-help-desk (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Other agents
built the 76 live tools; they follow the rules below, and a reviewer will check your work against them in depth
(three blind lenses: Teaching, Play, Craft). Build it as if it ships to real fourth graders tomorrow.

The tool is `network-help-desk`. Its spec is `tools/network-help-desk/spec.md`. **Read the spec fully, every line,
before you write anything.** The spec is the source of truth: build what it says, nothing more. If the spec is wrong
or impossible, do not improvise: build everything else, and write the problem in `handoff.md` and `codex-report.md`.

Always write the site's name as "Curio Class", never "Curio" alone. Never use an em dash anywhere (code comments, UI
text, notes, lines, reports): use a comma, a period, a colon or a plain hyphen.

#### 0. Ground rules for this run

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

#### 1. Read these, in this order

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

#### 2. The rules you must follow (quoted from the docs above)

##### From BUILD.md "Rules"
- "One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas."
- "Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them."
- "Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time."
- "Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone." (Grade 4: 44 px.)
- "Facts only from the spec's Sources. No em dashes. \"Curio Class\", never \"Curio\" alone."
- Keep `window.__tool` with everything the spec lists (`state, net, setMode, openCall(n), ask(n,q), claim(n, cause,
  clues), houseTry(device, target)`) plus `allLines`, the voice log (`vlog: V.log`, `get vq() { return V.queue; }`)
  and whatever a tester needs to read the current call, clues, call time, map badges and House results.

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
- Rule 2: "Every standard is taught well, above the minimum." Each module code in the spec (E4-SYS-NT-14,
  E4-SYS-SE-13, E4-SYS-HW-12) must be really taught by something a student does. Authentication vs authorization is
  the heart of this tool: the Logging in and Permission kinds must be told apart by what the student does, not only
  by a sentence.
- Rule 4: "Every tool stands alone. ... Defaults must work for a solo user; teacher toggles are extras."
- Rule 7: privacy is stated wherever anything is recorded or stored. This tool stores nothing but the kit Motion
  setting; the passwords are pretend (say so where a password appears, if anywhere).
- Rule 5: facts stay plain, with care for the people involved. Callers and the house are fictional; no real brands
  on devices, no real places.

##### From STANDARDS.md "Sizes" (check every one, early)
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

##### From STANDARDS.md "Voice behavior" (use `Curio.voice`; KIT.md documents it)
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

##### From POLISH.md (the ones that bite here)
- "Never shorten timing for reduced motion." Fix about 1.5 s, ping 300 ms per hop, Motion on or off.
- "Nothing overlaps by accident." "Test the extremes": all six questions asked (six clue cards) at every size, the
  claim step with two clues selected, Call time after several wrong claims, the Shift report with all 8 calls, the
  tablet dragged to every corner of the plan, all House toggles flipped.
- "Words match the state. Grammar, counts, plurals." ("Call time: 1 min", "Call time: 3 min".)
- "Nothing on screen gives the answer away." The cause board order, clue card order, button styles and map colors
  before a question is asked must not hint at the cause. The faint device outlines must not reveal status.
- "Keep the action area clear": badges, bubbles, login cards and the ping must not cover room names or each other.

#### 3. The engine (use it, do not rewrite it)

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

#### 4. Files to make in `tools/network-help-desk/`

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

#### 5. How to check your work (exact commands, run from the repo root `S:/CurioClass-codex-network-help-desk`)

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

#### 6. Self-check list before you report (BUILD.md "Wave lessons (BR1)", turned into checks)

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

#### 7. Report: write `tools/network-help-desk/codex-report.md`

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

<!-- end part -->

<!-- part: codex-report.md -->

### Codex report: network-help-desk

#### Built

- `src.html`: kit starter based, help desk green on mint, SVG house, eight evidence-based Calls and a changeable House, self-contained after bundling.
- `tool.draft.json`: beta metadata, built stage, Grade 4, Calls and House, spec sources, updated 2026-10-28.
- `notes.md`: five-minute start, pairs with a student reading callers, modes, three kinds, NIST authentication versus authorization, discussion and privacy.
- `voice/lines.json`: 19 runtime lines, upbeat-guide bank, Zephyr, prescribed style, no recordings.
- `audit-states.json`: real click/key/uneven integer drag recipes for six clues, two selected clues, wrong claim, Solved, eight-call report, shed and router-off House, with keep regions.
- `handoff.md`: state/layout guide, completed Numbers check and Engine changes wanted sections, engine workarounds.
- `codex-report.md`: this report, the only tool file written during report-only recovery.
- `network-help-desk.html`: generated ignored bundle, 123,086 bytes, below 2 MB. SHA-256: ee0b525191174c480e267f81fc87c512cda42337111b6b1e071f8277b958c88f.

Evidence paths below are relative to `S:/CurioClass-codex-scratch/network-help-desk/`, unless explicitly naming a tool file. No art, image downloads or recordings were needed. Saved validation reports no tool-folder host.html. Handoff sections were already complete and were left unchanged during recovery.

#### Numbers check

The pre-build `numbers.cjs` Node check loads the actual engine and uses router (300,330). Unrounded Euclidean distance drives thresholds: at most 250 gives 3 bars, at most 420 gives 2, at most 560 gives 1, otherwise 0.

| Spot | Spec distance (bars) | Computed distance | Rounded distance (bars) |
|---|---|---|---|
| Living room (360,420) | 108 (3) | 108.1665 | 108 (3) |
| Kitchen (520,200) | 255 (2) | 255.5386 | 256 (2) |
| Bedroom (650,420) | 361 (2) | 361.3862 | 361 (2) |
| Back door (760,470) | 481 (1) | 480.8326 | 481 (1) |
| Shed (920,520) | 648 (0) | 648.4597 | 648 (0) |

Kitchen differs: sqrt(220 squared + 130 squared) is about 255.5386, rounding to 256, not 255. Its 2 bars are unchanged. The tool trusts the computation; the spec was not edited. `more-log.txt` records actual pointer drags to these spots within one design unit of pointer rounding, yielding bars 3, 2, 2, 1, 0. The Node check also exercises cloud reachability and guest exclusion for home printing.

#### Done when

1. PASS: `validation.json` records 48 exact answers and eight exact fixes. The final saved `frozen-all-calls.json` contains all six answers for all eight calls and matches the captured Content table. Each all-six call was captured in `frames/`, then again in `audit-fix-frames/audit-fix-call1-1366.png` through `audit-fix-call8-1366.png` plus eight corresponding 680 frames. These show link, router/other-device, screen, login and account evidence appearing with the appropriate questions.
2. PASS: final frozen data has the correct fix for every call, Connection stamps for 1, 2, 4, 5; Logging in for 3, 6; Permission for 7, 8; and success:true, arrived:true for every ping. Calls 1 through 7 reach the cloud/page and return; call 8 uses the family laptop to the printer and returns. Solved cards of all three kinds were viewed in the saved frames. `frozen-frames/frozen-all-calls.png` shows eight completed report rows.
3. PASS: every final right-cause/non-key attempt returned need-clue. `more-log.txt` records wrong claims for calls 1, 3, 6, 7, 8 stopping at fault/router/cloud with time 3 after one question and one wrong claim, and nudges naming the first unasked key question. `final-frames/wrong-mid.png` and `wrong-after.png` show ping travel, retained X and nudge. When both keys were asked, `audit-exit/state-wrong-claim-680x425.png` quotes the first key clue. `wrong-followup.json` verifies recovery without stale tokens or exceptions.
4. PASS: questions add 1 effort minute, wrong claims add 2. Held stress has time 5 after one question and two wrong claims. All-six final calls have 6 min; frozen JSON has eight report rows. `frozen-frames/frozen-all-calls.png` and `final-frames/shift-final.png` show the report. The final Solved card offers Shift report, keeping the last fix readable first. Call time states what it counts and that it is not a clock. No score/stars/countdown. Singular 1 min and larger values were viewed.
5. PASS: `house-rules.json` records all 24 router-off Try combinations failing, then the four-target Caps Lock/Guest/Kid matrices. Caps Lock fails Library site only; Guest fails Family printer only; Kid fails Parent settings only. `more-log.txt` adds desktop cable unplugged, Wi-Fi off and all five real tablet drags. Shed gives 0 bars and No connection. Four `native-*.json` files verify actual native controls. `audit-exit/state-house-shed-680x425.png` and `state-house-router-off-375x812.png` show failures. `quick-final/guest-printer-self.png` covers Guest printing to the printer itself; `frozen-log.txt` verifies the projected desktop cable route succeeds.
6. PASS for saved runtime and held-input coverage: `voice-stress.json` and `voice-stress-final-log.txt` count w-calls 1, w-house 1, ask 1, claim 1, solved-conn 2, next-call 1, wrong 2, need-clue 1, house 1, using 120 ms holds and 2 s pacing. Full audit repeated/quick-click sections are clean. `welcome-repeat.json` verifies corrected call-strip welcome behavior. Read was exercised in both modes and with Sound off, using the current hint. Final runtime's 19 lines exactly match the voice file. All three solved event types are implemented; repeated spoken-event sampling specifically covered Connection, not every kind. That coverage limit is retained under Left open.
7. PASS: all eight standard viewports were captured and viewed: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and a 375x812 iframe. `audit-exit/size-*.png` checks each clean at 44 px targets, with Questions and Make a claim visible without scrolling. Portrait puts the map above the panel while retaining panel-first tab order; short landscape stays side by side. Phone PNGs are 395x832 including a 20 px host matte; the tool iframe is 375x812. An equivalent scratch host on 8795 was used, not the tool-folder host flow, as disclosed below.
8. PASS within saved browser coverage: `keyboard-final.json` records a keyboard-only solved call and focus next-call. `quick-final-log.txt` records Right/Down moving the tablet from (650,420) to (670,440), retaining focus. Motion-on timings were about 1515 ms fix/1248 ms ping; Motion-off 1510/1237 ms, consistent with fixed 1.5 s plus 300 ms per hop and frame scheduling. Live-toggle JSON covers mid-fix/mid-ping with zero continuing fix animations and unchanged pacing. Final drivers and stress report zero console errors and empty resource lists. The stress network-domain log has only the local file document. Static validation finds no tool fetch/XHR/WebSocket/external CSS import, no em dashes; the site's name is Curio Class. No tests were rerun during recovery.

#### Self-check (section 6)

- PASS, hint/Read: one shared hint sits in the active panel. Empty claim names Questions; all-six names Make a claim; claim names Send fix; solved names next phone or Shift report; House names Try/tablet. `quick-final-log.txt` and Read entries in `voice-stress.json` cover both modes. Read uses exactly the hint.
- PASS, immediate hint on mode/call switch: synchronous hint update precedes voice queuing; held mode/call changes and corrected House frames show the active instruction immediately.
- PASS, V.heard: explicit heard-based how selection; repeated-click audit clean; ask and claim spoken once in stress.
- PASS, first action: no narration gate; fresh-page held-control audit exercises each button. Questions take effect on first click; empty Make a claim stays in Questions with a useful hint.
- PASS, disabled/stale controls: needs/valid checks and watch/retry/all-clues hints guard queued steps. Need-clue drops on any next tap; wrong drops when a question is asked. Central call-step selection prevents obsolete ask/claim instructions.
- PASS for sampled 2 s pace: full repeated-input audit clean; two wrong and two solved Connection events logged, welcomes/how once. Every event kind was not separately spoken twice, a coverage limit rather than a claimed test.
- PASS, welcome not cut by unrelated fixes: first full audit found call-strip hush cuts. Corrected by preserving applicable generic welcome, treating same-call taps as no-ops and stopping only obsolete step lines. `welcome-repeat.json` has ask then w-calls once despite repeated call taps. Read/Sound intentionally affect speech at the user's request.
- PASS, focus rebuild: persistent question/evidence DOM, selection ring instead of map replacement, preventScroll focus restoration for state redraws. Full audit settled-Enter checks retained focus; `keyboard-final.json`, `arrows-final.json` and native-control JSON cover keyboard selection/control changes. No focus is taken on load.
- PASS, held pointer: handlers mutate after click/release, with no pointer-down panel replacement. Drag uses pointer capture and retains tablet/focus. Already-selected tablet is intentionally a no-op.
- PASS, reserved hint: duplicate inactive hint removed; shared active hint and compact gaps fix clipping. Latest compact measurements place hint bottom at 419 within 425, 494 within 500 and 711 within 720. Final phone/680 House hint is visible.
- PASS, labels/badges: per-box projection, compact icons, separate screen/login strip, centered status badges, account offsets and room obstacle fitting replace early crowded layouts. Cable control participates in obstacle fitting. Latest targeted audit has zero overlap leads; all 470 PNGs were viewed. Grayscale retains check/outline/pattern cues.
- PASS, targets/sizes: latest eight-size audit clean, 44 px interactive targets and unclipped active hint. Decorative 14 px ping has no pointer events or pointer cursor. Scrollable cards retain full hit areas.
- PASS, no giveaways: uniform unknown badges/faint outlines before questions, fixed cause styles/order and question-order clues. Key/cause IDs do not appear as visible hints. Status appears only after relevant evidence.
- PASS, no free sweep: all eight frozen right-cause/non-key claims rejected; wrong attempts cost 2 effort minutes and teach a next question or quote evidence. No scoring/timed punishment.
- PASS, honest numbers: about bars and walls/distance model visible; Call time says 1 per question/2 per wrong claim, not a clock. Kitchen rounding disclosed above and in handoff.
- PASS, standards by solo action: E4-SYS-NT-14 through cable/Wi-Fi/router/distance tests and tablet movement; E4-SYS-SE-13 through password/Caps Lock versus successfully logged-in Leo/Ana access, Guest printer versus Internet and Kid settings versus Library; E4-SYS-HW-12 through collecting evidence, claiming, testing and revising a diagnosis. Authentication and authorization require different student actions.
- PASS, family engine: Net.graph includes router/devices/cloud/printer/wire/Wi-Fi/guest-marked links; Net.path/reach use guest skip; Net.draw receives real-pixel skin.box with rooms underneath, hidden/faint nodes and badges; Net.token/send own 300 ms hops; Net.stop on call/mode changes. Canonical design coordinates remain separate from projected drawing/cable via points.
- PASS, Motion off: no infinite animation in any saved audit. Fixed 1500 ms and 300 ms hop pacing retained; live-toggle JSON covers both phases and return-hop position. Engine cached-calm workaround is documented below.
- PASS, console: final saved size/state sweeps and frozen driver say errors in 0 shots; stress runtimeErrors/resources empty. Early launch/driver issues are disclosed under Left open.
- PASS within saved interaction coverage, Escape/Back: claim returns focus to Make a claim with preventScroll; settled-Enter and keyboard paths remain usable. Back exercised in held stress. No separate report-recovery rerun.
- PASS, arrows/bounds: final Right/Down gives (670,440), tablet focused. Real drags cover five spots; four corner frames and state-check bounds establish 0..1000 by 0..600 clamping.
- PASS, Reset house: `state-check.json` has reset:true, restored defaults, tokens:0 after changes/mode switch.
- PASS, new shift: `quick-final-log.txt` has report:false, cleared:true, focus:q1.
- PASS, unfinished call: `state-check.json` has kept:true. `interrupted-fix.json` shows safe rollback and no stale completion/token; `wrong-followup.json` confirms a new question clears a failed ping before solving.

#### Audit leads

The initial attempted audit in `audit/` was interrupted, leaving PNGs but no completed audit.md. Its frames are included below; no completed lead list is available. The first complete full audit is `audit-final/audit.md` (135 leads). Despite its folder name it predates fixes. Follow-ups: `audit-layout` 26, `audit-house` 42, `audit-house-last` 8, `audit-exit` 0.

Each listed mechanical lead is reproduced below with source line/context and disposition, including repeated occurrences. The final targeted regression covers initial Calls/House at all eight sizes, six-clue/wrong at 680/375, claim/Solved at 1366, shed/router-off at 680/375 and Motion off. The first full run covers all seven states at every size including Shift and full held/repeated voice. The final source was not subjected to another complete all-state/all-size voice audit after the small voice-step and projected-wire changes; frozen all-call/cable tests are the later functional evidence.

audit-final/audit.md, reported 135 leads:

- L11, **680x425** (20 controls): : overlap: text "Living room" / text "?" 7x4

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L14, **800x500** (20 controls): : overlap: text "Living room" / text "?" 7x6

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L19, **1280x720** (20 controls): : overlap: text "Back door" / tspan "Tablet" 9x4

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L26, **760x900** (20 controls): : overlap: text "Bedroom" / tspan "Phone" 41x8

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L27, **760x900** (20 controls): : overlap: text "Back door" / tspan "Tablet" 10x9

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L28, **760x900** (20 controls): : text hidden under another box or a scroll edge: text "Living room" under rect

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L29, **760x900** (20 controls): : text hidden under another box or a scroll edge: tspan "Desktop" under rect

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L30, **760x900** (20 controls): : text hidden under another box or a scroll edge: tspan "Router" under rect

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L31, **760x900** (20 controls): : text hidden under another box or a scroll edge: tspan "Printer" under rect

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L34, **375x812 (iframe host)** (20 controls): : overlap: text "Living room" / text "?" 5x3

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L39, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "TV" 50x29 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L40, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Laptop" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L41, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Tablet. Drag or use arrow keys, 20 units" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L42, **mode House** (click #m-house): : hint out of view: "Ask questions until you know what kind of problem it is. Then tap Make a claim." [every size]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L43, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 29x19 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L44, **mode House** (click #m-house): : overlap: g "Desktop" / #cable-end "Unplug desktop cable" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L45, **mode House** (click #m-house): : overlap: g "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L46, **mode House** (click #m-house): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Back door" 23x4 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L47, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L48, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / tspan "Desktop" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L49, **mode House** (click #m-house): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L50, **mode House** (click #m-house): : overlap: tspan "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L51, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 26x12 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L52, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L53, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 27x61 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L54, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "Printer" 68x44 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L55, **mode House** (click #m-house): : overlap: g "Desktop" / g "TV" 68x34 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L56, **mode House** (click #m-house): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Back door" 24x19 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L57, **mode House** (click #m-house): : overlap: g "Phone" / text "Bedroom" 61x21 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L58, **mode House** (click #m-house): : overlap: g "TV" / #cable-end "Unplug desktop cable" 44x44 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L59, **mode House** (click #m-house): : overlap: g "TV" / text "Living room" 27x21 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L60, **mode House** (click #m-house): : overlap: g "TV" / text "Plug" 22x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L61, **mode House** (click #m-house): : overlap: g "TV" / text "out" 17x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L62, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Router. On. Tap to turn off." under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L63, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L64, **mode House** (click #m-house): : text hidden under another box or a scroll edge: tspan "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L65, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Desktop" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L66, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Printer" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L67, **mode House** (click #m-house): : text hidden under another box or a scroll edge: text "Back door" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L68, **mode House** (click #m-house): : text hidden under another box or a scroll edge: tspan "Tablet" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L69, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / g "TV" 49x39 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L70, **mode House** (click #m-house): : overlap: g "Phone" / text "Kitchen" 7x7 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L71, **mode House** (click #m-house): : overlap: g "Phone" / text "Bedroom" 13x4 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L74, **six-clues** (audit-states.json): : overlap: text "Office" / text "Grown-up" 5x12 [680x425]

  FIXED: account badges use room-specific offsets, including compact Office placement. Later six-clue/claim/wrong frames and audit-exit are clear.

- L75, **six-clues** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 9x9 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L76, **six-clues** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 10x5 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L77, **six-clues** (audit-states.json): : overlap: text "Living room" / text "On" 12x8 [375x812]

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L80, **claim-two-clues** (audit-states.json): : overlap: text "Office" / text "Grown-up" 5x12 [680x425]

  FIXED: account badges use room-specific offsets, including compact Office placement. Later six-clue/claim/wrong frames and audit-exit are clear.

- L81, **claim-two-clues** (audit-states.json): : keep region: #claim-clues: 100% inside the window, 6 of 9 sample points covered or cut by a scroll box [680x425, 800x500, 760x900, 375x812]

  ANSWERED: original selector named the entire six-card list inside its intentional scroller. Recipe now keeps .claim-clues, the visible evidence viewport, plus Send fix. Cards retain 44 px targets/check/outline, primary actions stay visible. Later claim audits clean.

- L82, **claim-two-clues** (audit-states.json): : keep region: #claim-clues: 100% inside the window, 3 of 9 sample points covered or cut by a scroll box [1000x625, 1280x720, 1366x768, 1920x1080]

  ANSWERED: original selector named the entire six-card list inside its intentional scroller. Recipe now keeps .claim-clues, the visible evidence viewport, plus Send fix. Cards retain 44 px targets/check/outline, primary actions stay visible. Later claim audits clean.

- L83, **claim-two-clues** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 9x9 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L84, **claim-two-clues** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 10x5 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L85, **claim-two-clues** (audit-states.json): : overlap: text "Living room" / text "On" 12x8 [375x812]

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L88, **wrong-claim** (audit-states.json): : small target: g 14x14 (svg) [every size]

  ANSWERED: decorative 14 px ping inherited the engine token cursor. Non-pick tokens now have no pointer cursor/events; interactive targets stay at least 44 px. Later audit-exit has no small-target lead.

- L89, **wrong-claim** (audit-states.json): : overlap: text "Office" / text "Grown-up" 5x12 [680x425]

  FIXED: account badges use room-specific offsets, including compact Office placement. Later six-clue/claim/wrong frames and audit-exit are clear.

- L90, **wrong-claim** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 9x9 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L91, **wrong-claim** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 10x5 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L92, **wrong-claim** (audit-states.json): : overlap: text "Living room" / text "On" 12x8 [375x812]

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L95, **solved** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 9x9 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L96, **solved** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 10x5 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L97, **solved** (audit-states.json): : overlap: text "Living room" / text "On" 12x4 [375x812]

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L100, **shift-report** (audit-states.json): : text hidden under another box or a scroll edge: tspan "Phone" under rect [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L101, **shift-report** (audit-states.json): : text hidden under another box or a scroll edge: tspan "Laptop" under rect [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L102, **shift-report** (audit-states.json): : overlap: text "Bedroom" / tspan "Laptop" 45x8 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L105, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "TV" 50x29 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L106, **house-shed** (audit-states.json): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Shed" 4x10 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L107, **house-shed** (audit-states.json): : hint out of view: "Ask questions until you know what kind of problem it is. Then tap Make a claim." [every size]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L108, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 29x19 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L109, **house-shed** (audit-states.json): : overlap: g "Desktop" / #cable-end "Unplug desktop cable" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L110, **house-shed** (audit-states.json): : overlap: g "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L111, **house-shed** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L112, **house-shed** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / tspan "Desktop" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L113, **house-shed** (audit-states.json): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L114, **house-shed** (audit-states.json): : overlap: tspan "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L115, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 26x12 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L116, **house-shed** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L117, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "Laptop" 27x61 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L118, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "Printer" 68x44 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L119, **house-shed** (audit-states.json): : overlap: g "Desktop" / g "TV" 68x34 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L120, **house-shed** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 61x8 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L121, **house-shed** (audit-states.json): : overlap: g "TV" / #cable-end "Unplug desktop cable" 44x44 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L122, **house-shed** (audit-states.json): : overlap: g "TV" / text "Living room" 27x6 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L123, **house-shed** (audit-states.json): : overlap: g "TV" / text "Plug" 22x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L124, **house-shed** (audit-states.json): : overlap: g "TV" / text "out" 17x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L125, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Router. On. Tap to turn off." under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L126, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L127, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: tspan "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L128, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Printer" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L129, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "TV" 49x39 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L130, **house-shed** (audit-states.json): : overlap: g "Phone" / text "Kitchen" 7x7 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L131, **house-shed** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 13x4 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L134, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "TV" 55x29 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L135, **house-router-off** (audit-states.json): : overlap: g "Laptop" / g "Tablet. Drag or use arrow keys, 20 units" 15x44 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L136, **house-router-off** (audit-states.json): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Bedroom" 35x13 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L137, **house-router-off** (audit-states.json): : hint out of view: "Ask questions until you know what kind of problem it is. Then tap Make a claim." [every size]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L138, **house-router-off** (audit-states.json): : overlap: g "Laptop" / g "Tablet. Drag or use arrow keys, 20 units" 5x37 [800x500]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L139, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "Laptop" 34x10 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L140, **house-router-off** (audit-states.json): : overlap: g "Desktop" / #cable-end "Unplug desktop cable" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L141, **house-router-off** (audit-states.json): : overlap: g "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L142, **house-router-off** (audit-states.json): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Back door" 23x4 [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L143, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L144, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / tspan "Desktop" 44x10 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L145, **house-router-off** (audit-states.json): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L146, **house-router-off** (audit-states.json): : overlap: tspan "Desktop" / text "Plug" 22x5 [1280x720, 1366x768, 1920x1080, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L147, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Router. Off. Tap to turn on." under rect [1280x720, 760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L148, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Desktop" under rect [1280x720]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L149, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "Laptop" 31x3 [1366x768]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L150, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L151, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "Laptop" 32x52 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L152, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "Printer" 73x44 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L153, **house-router-off** (audit-states.json): : overlap: g "Desktop" / g "TV" 73x25 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L154, **house-router-off** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 61x8 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L155, **house-router-off** (audit-states.json): : overlap: g "Printer" / text "Off" 8x17 [760x900]

  FIXED: centered badges, separated compact router and room labels, used one power text badge without a duplicate failure glyph. Initial/House audit-exit frames clean.

- L156, **house-router-off** (audit-states.json): : overlap: g "TV" / #cable-end "Unplug desktop cable" 44x44 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L157, **house-router-off** (audit-states.json): : overlap: g "TV" / text "Living room" 27x6 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L158, **house-router-off** (audit-states.json): : overlap: g "TV" / text "Plug" 22x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L159, **house-router-off** (audit-states.json): : overlap: g "TV" / text "out" 17x15 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L160, **house-router-off** (audit-states.json): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / text "Back door" 24x5 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L161, **house-router-off** (audit-states.json): : overlap: text "Back door" / tspan "Tablet" 10x5 [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L162, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L163, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: tspan "TV" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L164, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Printer" under rect [760x900]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L165, **house-router-off** (audit-states.json): : small target: g 14x14 (svg) [375x812]

  ANSWERED: decorative 14 px ping inherited the engine token cursor. Non-pick tokens now have no pointer cursor/events; interactive targets stay at least 44 px. Later audit-exit has no small-target lead.

- L166, **house-router-off** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / g "TV" 49x39 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L167, **house-router-off** (audit-states.json): : overlap: g "Phone" / text "Kitchen" 7x7 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L168, **house-router-off** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 13x4 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

Held-control and voice-table leads in the first complete audit:

- #call-1 welcome cut (hush): FIXED, same-call tap no longer hushes; applicable welcome preserved. `welcome-repeat.json` has ask then w-calls once after repeated call taps.
- #call-2 welcome cut (hush): FIXED, changing to an unsolved asking call preserves a generic Calls welcome, while canceling stale call-specific events.
- #call-3 welcome cut (hush): FIXED by the same scoped welcome preservation; final stress and repeated-call test verify this behavior.
- #call-4 welcome cut (hush): FIXED by scoped welcome preservation and immediate hint update.
- #call-5 welcome cut (hush): FIXED by scoped welcome preservation and immediate hint update.
- #call-6 welcome cut (hush): FIXED by scoped welcome preservation and immediate hint update.
- #call-7 welcome cut (hush): FIXED by scoped welcome preservation; solved events remain tied to their call.
- #call-8 welcome cut (hush): FIXED by scoped welcome preservation; mode scope still cancels obsolete Calls speech when House opens.
- Sound first tap cuts welcome: EXPECTED user-requested Sound off, kit behavior, not an unrelated step canceling narration.
- Read first tap has welcome not heard: EXPECTED, Read speaks the current hint at the user's request. Read tested in both modes and with Sound off.
- Questions move 8 of 20 controls: FIXED layout isolation. The eight call-strip items had shifted as clues grew. Later lower scroller contains evidence growth, while Questions, Make a claim and reserved hint stay fixed; later six-clue/claim frames verify primary positions.
- House Try moves 2 of 12 controls: FIXED, result-chip area reserves height even when empty.
- Router, desktop, laptop, phone, printer, TV, cable-end rebuilt with focus kept: ANSWERED, state redraws restored focus and settled Enter was clean. Device selection was improved further to ring-only updates; router/cable changes act after release and preserve focus.
- Selected Tablet nothing changed: EXPECTED, already selected, not dead. Real uneven drags and final arrow JSON prove movement/focus.
- All settled-Enter checks, five held clicks 2 s apart and quick taps 0.7 s apart: clean in saved full audit. Motion off has nothing running forever. No console-error lead.

audit-layout/audit.md, reported 26 leads:

- L29, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 3x7 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L30, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Laptop" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L31, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Tablet. Drag or use arrow keys, 20 units" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L32, **mode House** (click #m-house): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L33, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L34, **mode House** (click #m-house): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L35, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L46, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 3x7 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L47, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Tablet. Drag or use arrow keys, 20 units" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L48, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: text "Shed" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L49, **house-shed** (audit-states.json): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L50, **house-shed** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L51, **house-shed** (audit-states.json): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L52, **house-shed** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L55, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "TV" 7x21 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L56, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / #cable-end "Unplug desktop cable" 8x7 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L57, **house-router-off** (audit-states.json): : overlap: g "Laptop" / g "Tablet. Drag or use arrow keys, 20 units" 15x44 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L58, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Router. Off. Tap to turn on." under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L59, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Laptop" under rect [680x425, 375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L60, **house-router-off** (audit-states.json): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L61, **house-router-off** (audit-states.json): : overlap: g "Laptop" / g "Tablet. Drag or use arrow keys, 20 units" 5x37 [800x500]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L62, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 18x17 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L63, **house-router-off** (audit-states.json): : overlap: text "Living room" / text "out" 5x8 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L64, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 13x9 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L65, **house-router-off** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 6x16 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L66, **house-router-off** (audit-states.json): : text hidden under another box or a scroll edge: g "Tablet. Drag or use arrow keys, 20 units" under rect [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

audit-house/audit.md, reported 42 leads:

- L29, **mode House** (click #m-house): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 37x12 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L30, **mode House** (click #m-house): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / #cable-end "Unplug desktop cable" 5x7 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L31, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Router. On. Tap to turn off." under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L32, **mode House** (click #m-house): : text hidden under another box or a scroll edge: g "Laptop" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L33, **mode House** (click #m-house): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L34, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 29x38 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L35, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / text "Plug" 18x14 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L36, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / text "out" 16x15 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L37, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 21x27 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L38, **mode House** (click #m-house): : overlap: g "Router. On. Tap to turn off." / text "out" 7x15 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L39, **mode House** (click #m-house): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 20x10 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L40, **mode House** (click #m-house): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 35x18 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L41, **mode House** (click #m-house): : overlap: g "Laptop" / text "out" 17x9 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L44, **house-shed** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 37x12 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L45, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Router. On. Tap to turn off." under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L46, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Laptop" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L47, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: g "Tablet. Drag or use arrow keys, 20 units" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L48, **house-shed** (audit-states.json): : text hidden under another box or a scroll edge: text "Shed" under rect [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L49, **house-shed** (audit-states.json): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L50, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 29x38 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L51, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / text "Plug" 18x14 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L52, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / text "out" 16x15 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L53, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / #cable-end "Unplug desktop cable" 21x27 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L54, **house-shed** (audit-states.json): : overlap: g "Router. On. Tap to turn off." / text "out" 7x15 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L55, **house-shed** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 20x10 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L56, **house-shed** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 35x18 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L57, **house-shed** (audit-states.json): : overlap: g "Laptop" / text "out" 17x9 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L60, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "Laptop" 11x56 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L61, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / g "TV" 7x49 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L62, **house-router-off** (audit-states.json): : overlap: g "Laptop" / g "Tablet. Drag or use arrow keys, 20 units" 9x56 [680x425]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

- L63, **house-router-off** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 42x12 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L64, **house-router-off** (audit-states.json): : overlap: g "Tablet. Drag or use arrow keys, 20 units" / #cable-end "Unplug desktop cable" 10x7 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L65, **house-router-off** (audit-states.json): : hint out of view: "Tap a device, change its controls, then tap a button in Try. Drag the tablet or move it with arrow keys." [680x425]

  FIXED: removed duplicate inactive hint; moved shared hint into active panel, reserved height and compacted House gaps. Final House/phone frames and audit-exit keep it visible.

- L66, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / #cable-end "Unplug desktop cable" 29x38 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L67, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / text "Plug" 18x14 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L68, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / text "out" 16x15 [1280x720]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L69, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / #cable-end "Unplug desktop cable" 21x27 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L70, **house-router-off** (audit-states.json): : overlap: g "Router. Off. Tap to turn on." / text "out" 7x15 [1366x768]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L71, **house-router-off** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 25x10 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L72, **house-router-off** (audit-states.json): : overlap: g "Laptop" / #cable-end "Unplug desktop cable" 40x18 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L73, **house-router-off** (audit-states.json): : overlap: g "Laptop" / text "out" 17x9 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L74, **house-router-off** (audit-states.json): : overlap: g "Phone" / text "Bedroom" 6x16 [375x812]

  FIXED: per-pixel scene layout separates device tiles; compact maps omit redundant device-name text while preserving accessible names. Repositioned router/desktop/laptop/TV/tablet, adjusted badge offsets and fitted room names around obstacles. Later matching frames and targeted audit-exit are clean.

audit-house-last/audit.md, reported 8 leads:

- L29, **mode House** (click #m-house): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 34x16 [680x425, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L30, **mode House** (click #m-house): : overlap: text "Living room" / text "out" 17x13 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L31, **mode House** (click #m-house): : overlap: text "Living room" / text "out" 17x11 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L32, **mode House** (click #m-house): : overlap: g "TV" / #cable-end "Unplug desktop cable" 43x11 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L35, **house-router-off** (audit-states.json): : overlap: #cable-end "Unplug desktop cable" / text "Living room" 34x16 [680x425, 760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L36, **house-router-off** (audit-states.json): : overlap: text "Living room" / text "out" 17x13 [680x425]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L37, **house-router-off** (audit-states.json): : overlap: text "Living room" / text "out" 17x11 [760x900]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

- L38, **house-router-off** (audit-states.json): : overlap: g "TV" / #cable-end "Unplug desktop cable" 43x11 [375x812]

  FIXED: placed 44 px cable control away from device tiles, routed projected wire through it, included cableBox in room-label avoidance, and separated compact TV. Matching audit-exit House frames have no residual cable/room/device overlap.

audit-exit/audit.md, reported 0 leads:

No listed leads. Every initial size clean, included state checks nothing new, Motion off nothing runs forever.

#### Frames looked at

Viewed all 470 PNGs below. Original 155 were viewed via `sheets/sheet-01.jpg` through `sheet-26.jpg`; remaining 315 via `new-sheets/new-01.jpg` through `new-35.jpg`. Each contact sheet shows full screenshots with filenames. Critical compact/phone/claim/House/keyboard frames were also opened individually. Latest individually opened frames include `audit-exit/size-680x425.png`, `audit-exit/state-house-router-off-375x812.png` and `frozen-frames/frozen-gray-guest.png`.

Historical captures preserve development failures. Their overlaps and obsolete layouts are superseded by later fixes, not claimed as passing final states. Early driver JSON sometimes evaluated before screenshot wait, so later awaited JSON supplies final outcome assertions. Every entry below was viewed, including failed/superseded captures.

- `early/house-680.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early/initial-1366.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early/initial-680.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early/six-1366.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early2/house-680.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early2/initial-1366.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-01.jpg`.
- `early2/initial-680.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `early2/six-1366.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `frames/call1-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `frames/call1-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `frames/call2-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `frames/call2-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-02.jpg`.
- `frames/call3-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call3-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call4-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call4-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call5-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call5-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-03.jpg`.
- `frames/call6-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/call6-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/call7-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/call7-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/call8-all6.png`: 1366x768, numbered caller evidence/fix state; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/call8-solved.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-04.jpg`.
- `frames/claim-1000x625.png`: 1000x625, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/claim-1366x768.png`: 1366x768, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/claim-1920x1080.png`: 1920x1080, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/claim-680x425.png`: 680x425, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/claim-760x900.png`: 760x900, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/claim-800x500.png`: 800x500, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-05.jpg`.
- `frames/clues1-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-06.jpg`.
- `frames/clues1-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-07.jpg`.
- `frames/clues6-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues6-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues7-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues7-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues7-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues7-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-08.jpg`.
- `frames/clues7-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues7-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues7-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues8-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues8-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues8-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-09.jpg`.
- `frames/clues8-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/clues8-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/clues8-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/clues8-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/first-1000x625.png`: 1000x625, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/first-1280x720.png`: 1280x720, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-10.jpg`.
- `frames/first-1366x768.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/first-1920x1080.png`: 1920x1080, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/first-680x425.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/first-760x900.png`: 760x900, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/first-800x500.png`: 800x500, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/house-1000x625.png`: 1000x625, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-11.jpg`.
- `frames/house-1280x720.png`: 1280x720, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/house-1366x768.png`: 1366x768, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/house-1920x1080.png`: 1920x1080, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/house-680x425.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/house-760x900.png`: 760x900, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/house-800x500.png`: 800x500, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-12.jpg`.
- `frames/logic.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/cable-unplugged.png`: 1366x768, desktop cable failure; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/calm-fix.png`: 1366x768, Motion fix/ping check; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/calm-ping.png`: 1366x768, Motion fix/ping check; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/caps-lock.png`: 1366x768, Caps Lock/library authentication control or result; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/gray-selected.png`: 1366x768, grayscale evidence, badges and line patterns; historical development capture. Viewed in `sheets/sheet-13.jpg`.
- `more-frames/guest-printer.png`: 1366x768, Guest printing permission case; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/house-rules.png`: 1366x768, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/keyboard-solved.png`: 1366x768, keyboard-only call path and focus; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/kid-settings.png`: 1366x768, Kid Parent-settings permission case; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/motion-fix.png`: 1366x768, Motion fix/ping check; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/motion-ping.png`: 1366x768, Motion fix/ping check; historical development capture. Viewed in `sheets/sheet-14.jpg`.
- `more-frames/router-off.png`: 1366x768, House router-off Try result; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/tablet-back-door.png`: 1366x768, tablet at named Wi-Fi model spot; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/tablet-bedroom.png`: 1366x768, tablet at named Wi-Fi model spot; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/tablet-kitchen.png`: 1366x768, tablet at named Wi-Fi model spot; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/tablet-living-room.png`: 1366x768, tablet at named Wi-Fi model spot; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/tablet-shed.png`: 1366x768, shed tablet, 0-bar connection result; historical development capture. Viewed in `sheets/sheet-15.jpg`.
- `more-frames/timing-False.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/timing-True.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/voice-held.png`: 1366x768, held-click voice/welcome state; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/wifi-off.png`: 1366x768, Wi-Fi off failure; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/wrong-1.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/wrong-3.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-16.jpg`.
- `more-frames/wrong-6.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `more-frames/wrong-7.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `more-frames/wrong-8.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `latest-early/house-680.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `latest-early/initial-1366.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `latest-early/initial-680.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-17.jpg`.
- `latest-early/six-1366.png`: 1366x768, interaction/layout state named in filename; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-1000x625.png`: 1000x625, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-1280x720.png`: 1280x720, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-1366x768.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-18.jpg`.
- `audit/size-680x425.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/size-760x900.png`: 760x900, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/size-800x500.png`: 800x500, first Calls screen at named viewport; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/state-claim-two-clues-1000x625.png`: 1000x625, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/state-claim-two-clues-1280x720.png`: 1280x720, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/state-claim-two-clues-1366x768.png`: 1366x768, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-19.jpg`.
- `audit/state-claim-two-clues-1920x1080.png`: 1920x1080, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-claim-two-clues-375x812.png`: 395x832, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-claim-two-clues-680x425.png`: 680x425, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-claim-two-clues-760x900.png`: 760x900, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-claim-two-clues-800x500.png`: 800x500, cause board and evidence selection; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-20.jpg`.
- `audit/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-375x812.png`: 395x832, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-680x425.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-760x900.png`: 760x900, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-21.jpg`.
- `audit/state-mode-house-800x500.png`: 800x500, House map/labels/device controls; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-shift-report-1000x625.png`: 1000x625, eight-call Shift report/completion; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-shift-report-1280x720.png`: 1280x720, eight-call Shift report/completion; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-shift-report-680x425.png`: 680x425, eight-call Shift report/completion; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-shift-report-800x500.png`: 800x500, eight-call Shift report/completion; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-six-clues-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-22.jpg`.
- `audit/state-six-clues-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-375x812.png`: 395x832, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-23.jpg`.
- `audit/state-six-clues-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-1000x625.png`: 1000x625, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-1280x720.png`: 1280x720, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-1366x768.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-1920x1080.png`: 1920x1080, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-375x812.png`: 395x832, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-24.jpg`.
- `audit/state-solved-680x425.png`: 680x425, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-solved-760x900.png`: 760x900, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-solved-800x500.png`: 800x500, Solved card, kind and fix; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-wrong-claim-1000x625.png`: 1000x625, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-wrong-claim-1280x720.png`: 1280x720, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-wrong-claim-1366x768.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-25.jpg`.
- `audit/state-wrong-claim-1920x1080.png`: 1920x1080, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-26.jpg`.
- `audit/state-wrong-claim-375x812.png`: 395x832, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-26.jpg`.
- `audit/state-wrong-claim-680x425.png`: 680x425, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-26.jpg`.
- `audit/state-wrong-claim-760x900.png`: 760x900, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-26.jpg`.
- `audit/state-wrong-claim-800x500.png`: 800x500, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `sheets/sheet-26.jpg`.
- `audit-exit/calm-1366x768.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-1000x625.png`: 1000x625, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-1280x720.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-1366x768.png`: 1366x768, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-680x425.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-760x900.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/size-800x500.png`: 800x500, first Calls screen at named viewport. Viewed in `new-sheets/new-01.jpg`.
- `audit-exit/state-claim-two-clues-1366x768.png`: 1366x768, cause board and evidence selection. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-house-router-off-375x812.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-house-router-off-680x425.png`: 680x425, House router-off Try result. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-house-shed-375x812.png`: 395x832, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-house-shed-680x425.png`: 680x425, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls. Viewed in `new-sheets/new-02.jpg`.
- `audit-exit/state-mode-house-375x812.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-mode-house-680x425.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-mode-house-760x900.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-mode-house-800x500.png`: 800x500, House map/labels/device controls. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-six-clues-375x812.png`: 395x832, questions and collected clue cards. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-six-clues-680x425.png`: 680x425, questions and collected clue cards. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-solved-1366x768.png`: 1366x768, Solved card, kind and fix. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-wrong-claim-375x812.png`: 395x832, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-03.jpg`.
- `audit-exit/state-wrong-claim-680x425.png`: 680x425, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-03.jpg`.
- `audit-final/calm-1366x768.png`: 1366x768, Motion fix/ping check; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-1000x625.png`: 1000x625, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-1280x720.png`: 1280x720, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-1366x768.png`: 1366x768, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-680x425.png`: 680x425, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-760x900.png`: 760x900, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/size-800x500.png`: 800x500, first Calls screen at named viewport; historical development capture. Viewed in `new-sheets/new-04.jpg`.
- `audit-final/state-claim-two-clues-1000x625.png`: 1000x625, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-1280x720.png`: 1280x720, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-1366x768.png`: 1366x768, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-1920x1080.png`: 1920x1080, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-375x812.png`: 395x832, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-680x425.png`: 680x425, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-760x900.png`: 760x900, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-claim-two-clues-800x500.png`: 800x500, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-house-router-off-1000x625.png`: 1000x625, House router-off Try result; historical development capture. Viewed in `new-sheets/new-05.jpg`.
- `audit-final/state-house-router-off-1280x720.png`: 1280x720, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-1366x768.png`: 1366x768, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-1920x1080.png`: 1920x1080, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-375x812.png`: 395x832, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-680x425.png`: 680x425, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-760x900.png`: 760x900, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-router-off-800x500.png`: 800x500, House router-off Try result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-shed-1000x625.png`: 1000x625, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-shed-1280x720.png`: 1280x720, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-06.jpg`.
- `audit-final/state-house-shed-1366x768.png`: 1366x768, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-house-shed-1920x1080.png`: 1920x1080, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-house-shed-375x812.png`: 395x832, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-house-shed-680x425.png`: 680x425, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-house-shed-760x900.png`: 760x900, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-house-shed-800x500.png`: 800x500, shed tablet, 0-bar connection result; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-07.jpg`.
- `audit-final/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-mode-house-375x812.png`: 395x832, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-mode-house-680x425.png`: 680x425, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-mode-house-760x900.png`: 760x900, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-mode-house-800x500.png`: 800x500, House map/labels/device controls; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-shift-report-1000x625.png`: 1000x625, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-shift-report-1280x720.png`: 1280x720, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-shift-report-1366x768.png`: 1366x768, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-shift-report-1920x1080.png`: 1920x1080, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-08.jpg`.
- `audit-final/state-shift-report-375x812.png`: 395x832, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-shift-report-680x425.png`: 680x425, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-shift-report-760x900.png`: 760x900, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-shift-report-800x500.png`: 800x500, eight-call Shift report/completion; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-1000x625.png`: 1000x625, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-1280x720.png`: 1280x720, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-1366x768.png`: 1366x768, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-1920x1080.png`: 1920x1080, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-375x812.png`: 395x832, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-09.jpg`.
- `audit-final/state-six-clues-680x425.png`: 680x425, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-six-clues-760x900.png`: 760x900, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-six-clues-800x500.png`: 800x500, questions and collected clue cards; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-1000x625.png`: 1000x625, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-1280x720.png`: 1280x720, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-1366x768.png`: 1366x768, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-1920x1080.png`: 1920x1080, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-375x812.png`: 395x832, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-680x425.png`: 680x425, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-10.jpg`.
- `audit-final/state-solved-760x900.png`: 760x900, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-solved-800x500.png`: 800x500, Solved card, kind and fix; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-1000x625.png`: 1000x625, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-1280x720.png`: 1280x720, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-1366x768.png`: 1366x768, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-1920x1080.png`: 1920x1080, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-375x812.png`: 395x832, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-680x425.png`: 680x425, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-760x900.png`: 760x900, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-11.jpg`.
- `audit-final/state-wrong-claim-800x500.png`: 800x500, wrong claim, failure marker/nudge or recovery; historical development capture. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call1-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call1-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call2-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call2-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call3-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call3-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call4-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call4-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-12.jpg`.
- `audit-fix-frames/audit-fix-call5-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call5-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call6-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call6-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call7-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call7-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call8-1366.png`: 1366x768, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-call8-680.png`: 680x425, numbered caller evidence/fix state. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-first-1280.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-13.jpg`.
- `audit-fix-frames/audit-fix-first-680.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-first-760.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-house-1280.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-house-1366.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-house-1920.png`: 1920x1080, House map/labels/device controls. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-house-680.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-14.jpg`.
- `audit-fix-frames/audit-fix-house-760.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-14.jpg`.
- `audit-house/calm-1366x768.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-14.jpg`.
- `audit-house/size-1000x625.png`: 1000x625, first Calls screen at named viewport. Viewed in `new-sheets/new-14.jpg`.
- `audit-house/size-1280x720.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-1366x768.png`: 1366x768, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-680x425.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-760x900.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/size-800x500.png`: 800x500, first Calls screen at named viewport. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/state-house-router-off-1000x625.png`: 1000x625, House router-off Try result. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/state-house-router-off-1280x720.png`: 1280x720, House router-off Try result. Viewed in `new-sheets/new-15.jpg`.
- `audit-house/state-house-router-off-1366x768.png`: 1366x768, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-router-off-1920x1080.png`: 1920x1080, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-router-off-375x812.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-router-off-680x425.png`: 680x425, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-router-off-760x900.png`: 760x900, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-router-off-800x500.png`: 800x500, House router-off Try result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-shed-1000x625.png`: 1000x625, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-shed-1280x720.png`: 1280x720, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-shed-1366x768.png`: 1366x768, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-16.jpg`.
- `audit-house/state-house-shed-1920x1080.png`: 1920x1080, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-house-shed-375x812.png`: 395x832, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-house-shed-680x425.png`: 680x425, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-house-shed-760x900.png`: 760x900, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-house-shed-800x500.png`: 800x500, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls. Viewed in `new-sheets/new-17.jpg`.
- `audit-house/state-mode-house-375x812.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-18.jpg`.
- `audit-house/state-mode-house-680x425.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-18.jpg`.
- `audit-house/state-mode-house-760x900.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-18.jpg`.
- `audit-house/state-mode-house-800x500.png`: 800x500, House map/labels/device controls. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/calm-1366x768.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/size-1000x625.png`: 1000x625, first Calls screen at named viewport. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/size-1280x720.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/size-1366x768.png`: 1366x768, first Calls screen at named viewport. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-18.jpg`.
- `audit-house-last/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/size-680x425.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/size-760x900.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/size-800x500.png`: 800x500, first Calls screen at named viewport. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-1000x625.png`: 1000x625, House router-off Try result. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-1280x720.png`: 1280x720, House router-off Try result. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-1366x768.png`: 1366x768, House router-off Try result. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-1920x1080.png`: 1920x1080, House router-off Try result. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-375x812.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-19.jpg`.
- `audit-house-last/state-house-router-off-680x425.png`: 680x425, House router-off Try result. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-house-router-off-760x900.png`: 760x900, House router-off Try result. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-house-router-off-800x500.png`: 800x500, House router-off Try result. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-375x812.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-680x425.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-20.jpg`.
- `audit-house-last/state-mode-house-760x900.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-21.jpg`.
- `audit-house-last/state-mode-house-800x500.png`: 800x500, House map/labels/device controls. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/calm-1366x768.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-1000x625.png`: 1000x625, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-1280x720.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-1366x768.png`: 1366x768, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-1920x1080.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-375x812 (iframe host).png`: 395x832, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-680x425.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-21.jpg`.
- `audit-layout/size-760x900.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/size-800x500.png`: 800x500, first Calls screen at named viewport. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-1000x625.png`: 1000x625, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-1280x720.png`: 1280x720, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-1366x768.png`: 1366x768, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-1920x1080.png`: 1920x1080, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-375x812.png`: 395x832, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-680x425.png`: 680x425, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-760x900.png`: 760x900, cause board and evidence selection. Viewed in `new-sheets/new-22.jpg`.
- `audit-layout/state-claim-two-clues-800x500.png`: 800x500, cause board and evidence selection. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-1000x625.png`: 1000x625, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-1280x720.png`: 1280x720, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-1366x768.png`: 1366x768, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-1920x1080.png`: 1920x1080, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-375x812.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-680x425.png`: 680x425, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-760x900.png`: 760x900, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-router-off-800x500.png`: 800x500, House router-off Try result. Viewed in `new-sheets/new-23.jpg`.
- `audit-layout/state-house-shed-1000x625.png`: 1000x625, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-1280x720.png`: 1280x720, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-1366x768.png`: 1366x768, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-1920x1080.png`: 1920x1080, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-375x812.png`: 395x832, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-680x425.png`: 680x425, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-760x900.png`: 760x900, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-house-shed-800x500.png`: 800x500, shed tablet, 0-bar connection result. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-mode-house-1000x625.png`: 1000x625, House map/labels/device controls. Viewed in `new-sheets/new-24.jpg`.
- `audit-layout/state-mode-house-1280x720.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-1366x768.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-1920x1080.png`: 1920x1080, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-375x812.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-680x425.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-760x900.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-mode-house-800x500.png`: 800x500, House map/labels/device controls. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-six-clues-1000x625.png`: 1000x625, questions and collected clue cards. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-six-clues-1280x720.png`: 1280x720, questions and collected clue cards. Viewed in `new-sheets/new-25.jpg`.
- `audit-layout/state-six-clues-1366x768.png`: 1366x768, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-six-clues-1920x1080.png`: 1920x1080, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-six-clues-375x812.png`: 395x832, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-six-clues-680x425.png`: 680x425, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-six-clues-760x900.png`: 760x900, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-six-clues-800x500.png`: 800x500, questions and collected clue cards. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-solved-1000x625.png`: 1000x625, Solved card, kind and fix. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-solved-1280x720.png`: 1280x720, Solved card, kind and fix. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-solved-1366x768.png`: 1366x768, Solved card, kind and fix. Viewed in `new-sheets/new-26.jpg`.
- `audit-layout/state-solved-1920x1080.png`: 1920x1080, Solved card, kind and fix. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-solved-375x812.png`: 395x832, Solved card, kind and fix. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-solved-680x425.png`: 680x425, Solved card, kind and fix. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-solved-760x900.png`: 760x900, Solved card, kind and fix. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-solved-800x500.png`: 800x500, Solved card, kind and fix. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-wrong-claim-1000x625.png`: 1000x625, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-wrong-claim-1280x720.png`: 1280x720, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-wrong-claim-1366x768.png`: 1366x768, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-wrong-claim-1920x1080.png`: 1920x1080, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-27.jpg`.
- `audit-layout/state-wrong-claim-375x812.png`: 395x832, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-28.jpg`.
- `audit-layout/state-wrong-claim-680x425.png`: 680x425, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-28.jpg`.
- `audit-layout/state-wrong-claim-760x900.png`: 760x900, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-28.jpg`.
- `audit-layout/state-wrong-claim-800x500.png`: 800x500, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/corner-0-0.png`: 1366x768, tablet at named corner, drag boundary. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/corner-0-600.png`: 1366x768, tablet at named corner, drag boundary. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/corner-1000-0.png`: 1366x768, tablet at named corner, drag boundary. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/corner-1000-600.png`: 1366x768, tablet at named corner, drag boundary. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/grayscale-final.png`: 1366x768, grayscale evidence, badges and line patterns. Viewed in `new-sheets/new-28.jpg`.
- `final-frames/keyboard-final.png`: 1366x768, keyboard-only call path and focus. Viewed in `new-sheets/new-29.jpg`.
- `final-frames/shift-final.png`: 1366x768, eight-call Shift report/completion. Viewed in `new-sheets/new-29.jpg`.
- `final-frames/state-check.png`: 1366x768, House reset/state checks. Viewed in `new-sheets/new-29.jpg`.
- `final-frames/voice-final.png`: 1366x768, held-click voice/welcome state. Viewed in `new-sheets/new-29.jpg`.
- `final-frames/wrong-after.png`: 1366x768, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-29.jpg`.
- `final-frames/wrong-mid.png`: 1366x768, wrong-claim ping during travel. Viewed in `new-sheets/new-29.jpg`.
- `frozen-frames/frozen-all-calls.png`: 1366x768, eight-call Shift report/completion. Viewed in `new-sheets/new-29.jpg`.
- `frozen-frames/frozen-gray-guest.png`: 1366x768, grayscale evidence, badges and line patterns. Viewed in `new-sheets/new-29.jpg`.
- `frozen-frames/frozen-house-680.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-29.jpg`.
- `frozen-frames/frozen-wire.png`: 1366x768, desktop wired Internet succeeds. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-check-1280.png`: 1280x720, House map/labels/device controls. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-check-1366.png`: 1366x768, House map/labels/device controls. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-check-680.png`: 680x425, House map/labels/device controls. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-check-760.png`: 760x900, House map/labels/device controls. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-check-800.png`: 800x500, House map/labels/device controls. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-fail-1280.png`: 1280x720, House router-off Try result. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-fail-1366.png`: 1366x768, House router-off Try result. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-fail-680.png`: 680x425, House router-off Try result. Viewed in `new-sheets/new-30.jpg`.
- `house-check/house-fail-760.png`: 760x900, House router-off Try result. Viewed in `new-sheets/new-31.jpg`.
- `house-check/house-fail-800.png`: 800x500, House router-off Try result. Viewed in `new-sheets/new-31.jpg`.
- `house-check/welcome-repeat.png`: 1366x768, held-click voice/welcome state. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/final-calm.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/final-phone-result.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/final-portrait.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/final-projector.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/interrupted-fix.png`: 1366x768, interrupted fix switched to House. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/native-account.png`: 1366x768, native House control change. Viewed in `new-sheets/new-31.jpg`.
- `last-checks/native-caps.png`: 1366x768, Caps Lock/library authentication control or result. Viewed in `new-sheets/new-32.jpg`.
- `last-checks/native-network.png`: 1366x768, native House control change. Viewed in `new-sheets/new-32.jpg`.
- `last-checks/native-wifi.png`: 1366x768, native House control change. Viewed in `new-sheets/new-32.jpg`.
- `live-motion/live-calm-fix.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-32.jpg`.
- `live-motion/live-calm-ping.png`: 1366x768, Motion fix/ping check. Viewed in `new-sheets/new-32.jpg`.
- `phone-frames/all-eight-latest.png`: 1366x768, eight-call Shift report/completion. Viewed in `new-sheets/new-32.jpg`.
- `phone-frames/latest-first-1000.png`: 1000x625, first Calls screen at named viewport. Viewed in `new-sheets/new-32.jpg`.
- `phone-frames/latest-first-1280.png`: 1280x720, first Calls screen at named viewport. Viewed in `new-sheets/new-32.jpg`.
- `phone-frames/latest-first-1366.png`: 1366x768, first Calls screen at named viewport. Viewed in `new-sheets/new-32.jpg`.
- `phone-frames/latest-first-1920.png`: 1920x1080, first Calls screen at named viewport. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/latest-first-680.png`: 680x425, first Calls screen at named viewport. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/latest-first-760.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/latest-first-800.png`: 800x500, first Calls screen at named viewport. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-caps.png`: 395x832, Caps Lock/library authentication control or result. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-claim.png`: 395x832, cause board and evidence selection. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-clues.png`: 395x832, questions and collected clue cards. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-first.png`: 395x832, first Calls screen at named viewport. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-house.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-33.jpg`.
- `phone-frames/phone-result.png`: 395x832, House router-off Try result. Viewed in `new-sheets/new-34.jpg`.
- `phone-frames/phone-solved.png`: 395x832, Solved card, kind and fix. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/all-clues-final.png`: 1366x768, questions and collected clue cards. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/arrows-final.png`: 1366x768, tablet arrows and focus. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/empty-claim.png`: 680x425, cause board and evidence selection. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/guest-printer-self.png`: 1366x768, Guest printing permission case. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/portrait-latest.png`: 760x900, first Calls screen at named viewport. Viewed in `new-sheets/new-34.jpg`.
- `quick-final/reset-shift.png`: 1366x768, eight-call Shift report/completion. Viewed in `new-sheets/new-34.jpg`.
- `recheck/claim-new-1000.png`: 1000x625, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-34.jpg`.
- `recheck/claim-new-1280.png`: 1280x720, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `recheck/claim-new-1366.png`: 1366x768, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `recheck/claim-new-680.png`: 680x425, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `recheck/claim-new-760.png`: 760x900, cause board and evidence selection; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `recheck/keyboard-solved.png`: 1366x768, keyboard-only call path and focus; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `recheck/voice-held.png`: 1366x768, held-click voice/welcome state; historical development capture. Viewed in `new-sheets/new-35.jpg`.
- `room-check/phone-room-check.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-35.jpg`.
- `room-check2/phone-room-check.png`: 395x832, House map/labels/device controls. Viewed in `new-sheets/new-35.jpg`.
- `wrong-followup/wrong-then-question.png`: 1366x768, wrong claim, failure marker/nudge or recovery. Viewed in `new-sheets/new-35.jpg`.

#### Engine changes wanted

- `kit/network.js`, `path` and `reach`: optional `homeOnly: true` could exclude links marked `guest: true`, combined with the caller's existing `skip` predicate. The engine currently has no guest concept. This is a convenience request, not a blocking bug. This tool works around it with `skip: link => target === 'printer' && link.guest` and keeps guest-to-internet routes available. No engine or family document was edited.
- `kit/network.js`, `glide`: it captures `calm()` once at the start of a hop. Read `calm()` in each tick instead, so switching Motion off during a hop stops movement immediately while keeping the same completion time. This tool works around it by observing token transforms and calling Net.place at the last completed hop while Curio.reduce is true. Hop callbacks advance that displayed position, including the return trip. The kit Motion callback also cancels a finite fix animation without shortening its 1.5 second wait. No engine file was edited.

#### Left open

- No build, browser sweep, audit or product edit was rerun during report-only recovery. This report uses saved logs, JSON, manifests, audits and already viewed PNGs. While assembling it, saved final eight-call answers/fixes were compared with captured spec data and the 19 runtime lines with the voice file. This is evidence validation, not a new browser test.
- Coverage is layered: audit-final is the complete all-state/all-size plus held/repeated voice run, with 135 leads subsequently addressed. Audit-exit is a zero-lead targeted regression, not another complete final-source sweep. The small final voice-step and projected-wire changes were followed by frozen eight-call, wired House and grayscale checks, not a full repeated voice audit. Repeated solved speech sampled Connection, not two spoken replays of every login/permission kind. All three outcomes and their lines are implemented; eight-call outcome data passes.
- Scratch-only WebSocket workaround: default Python lacked websockets. Scratch `websockets.py` is a small standard-library CDP transport used through PYTHONPATH by drive/audit. No repo script was edited and the shipped tool has no WebSocket request/dependency. Stock test commands without this adjustment could not complete.
- GPU flag workaround: ordinary Chrome launches failed in the restricted environment. Test Chrome used `--headless=new --disable-gpu --in-process-gpu --no-sandbox --no-first-run`, allowed debugging ports, scratch profiles and `--mute-audio`. These are local test launch flags, not shipped behavior. Successful driver used port 9994, audit 9991. An ordinary unmodified Chrome launch was not established here.
- Host port workaround: stock audit derives host port from the debug port, conflicting with allowed 8795. Scratch `run-audit.py` changes that value in memory to 8795 without repo edits. Other phone checks use an equivalent scratch-only host at 8795. The exact tool-folder `drive.py --host 8795` flow was not used because the sandbox cannot delete its generated host.html. No tool-folder host was made; the equivalent 375x812 iframe was exercised.
- Kitchen 255 versus rounded 256 is a spec discrepancy; two bars are unchanged. Exact values are in Numbers check and handoff. The spec was not changed.
- No Zephyr recordings, as requested. Bundle missing-recording notices are expected. Browser speech fallback and Curio.voice logs supplied voice checks; recording-backed audible classroom review remains outside this run. No image/audio was downloaded/generated.
- The first audit attempt in audit/ stopped before producing audit.md. An early driver sweep hit a test-expression/selector timing assertion; later targeted/awaited checks replaced it. Early keyboard JSON captured before completion; keyboard-final.json is the later successful result. Earlier artifacts remain explicitly historical.
- Test Chrome/server shutdown after the dropped connection is not established by saved evidence. Report-only recovery did not inspect or alter processes, so cleanup is not claimed as verified. Saved validation reports no host.html in the tool folder. Frames/profiles/helpers remain in scratch; this report's temporary assembly script was placed in the allowed temporary directory.
- Shift report opens from the final Solved card's button so the last fix remains readable first. All eight report rows are present, and Start a new shift clears ticks/clues/effort. Handoff documents this for integration review.
- Handoff's Numbers check and Engine changes wanted sections were complete, so no handoff edit was needed. No source/supporting tool file changes, git commands, commits, branch changes or stashes were made during recovery. Engine requests are for integrator review; no engine/family file was edited.

<!-- end part -->

## Refine

<!-- part: refine.md -->

PASS (exit round 2 failed one narrow item, router links sharing the cable's run at 680x425 and 800x500; integrator fixed it and verified by driving, 2026-10-29)
Counts: blockers 0 (general 0, family 0), should fix 15 (general 13, family 2), polish accepted 11

### Refine: network-help-desk

Builder: Codex (single-tool test, 2026-10-28). Lenses: refine/teaching.md (0 / 8 / 6 / 2), refine/play.md
(0 / 11 / 8 / 3), refine/craft.md (0 / 6 / 5 / 4). Merged by the integrator. Each item names its sources
(T = Teaching, P = Play, C = Craft) and keeps its tag. Spec changes are marked; one cluster waits on Cory.

#### Should fix

1. **The cause can be found without diagnosing** (T S1, S2, P1; P on Play 1; C nit 3; T P2) general. SPEC CHANGE,
   WAITS ON CORY (see Spec open questions). Three ways in: the "Right cause" reply confirms a cause on any weak clue,
   so sweeping the 7 cards is free; the cause board prints the kind over each card, so the student never sorts
   Connection vs Logging in vs Permission (the sort that carries E4-SYS-SE-13); and six Q4 answers name the cause card
   almost word for word, so "ask Q4, copy the words" solves most calls (Play solved all 8 with one question each).
   Missed wave lesson (no free sweep). The need-clue double wording (T P6, P nit 1) goes with this fix.
2. **The map draws unknown parts as working** (T S3, C 5, P 8) general. After Q1 alone call 1 shows the cable plugged
   in, calls 2 and 4 a working Wi-Fi link, call 3 a joined Wi-Fi link though the password failed; call 5 and House
   router-off still show Wi-Fi arcs and live links from a dead router. Until its question is asked a part is drawn
   as unknown (the grey dotted "?" style), never as working; a router with no power draws no arcs and every link
   down.
3. **The Internet cloud sits inside the Kitchen; its line runs through devices** (T S4, C 2, P polish 3, audit lead,
   C nit 1) family:network. The router-to-Internet line crosses the Phone, Mr. Patel's and Ana's laptops and their
   labels, so they look wired into the path. Put the cloud outside the house walls at every size (the 375 layout
   already does), or route the link with `via` so no tile or label sits on it.
4. **The cause board hides whole groups** (T S6, P 2, P 3, C 3) general. At 1366x768 after any nudge "Not allowed"
   (the only Permission card, the answer to calls 7 and 8) drops below the board's scroll edge; at 680x425 only the
   Connection group shows; at 800x500, 760x900 and 375 Logging in or Permission are cut under the clue title. All
   seven causes (or, after item 1, all three kinds and the chosen kind's causes) in view in every claim state at
   every size, no scroll.
5. **A resize during a wrong-claim ping throws and locks the call** (T S7) general. `runPing` adds a `fault` node the
   ResizeObserver redraw drops; `linkPoints` throws on `px`; the call stays busy with Send fix and Back disabled.
   Carry the fault node into the redraw, or let the redraw wait for the ping. Re-test by resizing mid-ping on calls
   1, 2, 4, 5 and mid-fix on every kind.
6. **Call 8's Solved badge says "Allowed" on the guest laptop** (T S5, P 10, C 6) general. Ana is still not allowed;
   a family laptop printed. Badge her "Sent" (or keep "Guest") and put the check on the family laptop and printer;
   label the two "Ana's laptop" and "Family laptop". Keep "Allowed" for Leo's Student page. Settled: the Permission
   kind line becomes "Logging in worked. That account or network just isn't allowed to do that, and that is on
   purpose." (fits calls 7 and 8), and the Logging in line "The Wi-Fi or website was in reach. The device had to
   prove who it was with the right password." (fits calls 3 and 6; T N2). Update voice/lines.json if a spoken line
   changes; the solved lines stay as the spec wrote them.
7. **A broken link uses the Guest look** (P 7, C 4) family:network. Down links are the same orange dashes as Guest.
   Set the skin's `down` color to its own style (grey dashes with the break mark, or red with an X) and add "Broken"
   to the legend; orange stays Guest only. No engine change needed (skin colors).
8. **The next-call line is lost and its hint names the wrong control** (P 4; C heard it once in 5) general. Play's
   log shows it dropped 2.4 s after the solved line or never queued. Make it play once after the first Solved, and
   word line and hint for what is there: "Tap Next call, or a phone on the call strip." (spoken line change: update
   lines.json).
9. **680x425: Next call, Shift report and the 8th phone are cut off** (P 5, C polish 3) general. The hint names Shift
   report while it is out of view. At short heights put Next call beside the stamp, keep Shift report in view, and
   let the call strip fit all 8 phones (680 and 375).
10. **The skipped welcome plays after the first tap's own line** (P 6, C polish 1) general. Settled by STANDARDS and
    KIT.md: `welcomeAfter` is for one-mode tools; this tool has two. Drop `welcomeAfter`; on a first tap that has its
    own line, skip the welcome and let Sound off/on or the next mode entry bring it (as the kit does by default).
11. **The Shed spot is drawn on the Shed's wall** (P 9) general. Rooms are drawn on screen fractions while devices use
    the design box, so they drift apart near the edges: Sam's phone and the shed tablet sit on the wall over "Back
    door". Derive the room drawing from the same design-to-pixel transform as the devices, so every named spot lands
    inside its room at every size.
12. **House "No bars" hint sticks after the tablet comes back in range** (C 1) general. `moveTablet` never calls
    `updateHint`; Read then speaks a false line. Restore the House hint when bars go above 0.
13. **"about 1 bars of 3"** (P 11) general. "about 1 bar of 3".
14. **Builder talk in the teacher notes** (T S8) general. Delete "although the spec lists 255" sentence; the line
    before already says the thresholds are a Curio Class model. Also "design units" / "20 units per press" in notes
    and the tablet aria-label become "one small step per press" (T N1).
15. **The first-screen hint names no control** (P polish 7, wave lesson "hint names the next control") general.
    "Tap a question to ask the caller. Then tap Make a claim." (if this is the `ask` line, update lines.json).

#### Polish accepted

1. The Solved card shows the clue that proved it ("Proved by: ..."), and the Shift report marks each call's key
   question (P polish 4).
2. House results carry the kind stamp (plug, key, hand) and a pass/fail glyph; `houseTry` already computes the kind
   (T P3, P polish 5).
3. House shows only the settings a device has: no Account for printer and TV; a printer on Guest reads "Not allowed:
   the printer is on the Guest Wi-Fi, away from home devices" (T P4).
4. Call 5's wrong-claim X sits on the dark router, not mid-link (T P5); the X on calls 3 and 8 must not cover the
   router icon (P nit 3).
5. Small maps: short device labels at 12 px or more (or distinct icons) so desktop/TV and phone/tablet can be told
   apart; room names 14 px at the laptop sizes and as large as fits in the preview (P polish 1, C polish 2)
   family:network.
6. 375 wide: per spec, show the caller's room and the router with the rest faded, so badges stop covering icons and
   room labels; at 680x425 badges and room names never overlap (P polish 2).
7. Wi-Fi bars drawn beside the tablet on the map while dragging, so the drag is the experiment (P polish 6).
8. 1920x1080: map notes, legend and call time large enough to read projected (P polish 8).
9. House at 680x425: fixed room-label spots per layout ("Living room" stays in the Living room); drop the half-cut
   duplicate "About" line in the panel (C polish 4).
10. Badges ("Online", "On") never sit over a device tile or another device (P nit 2).
11. Labels "Phone" and "Laptop" off the wall lines and the cloud link (C nit 1).

#### Settled by the integrator

- Engine change wanted, `glide` reads `calm()` per tick: APPROVED. Backward compatible; re-check internet-journey's
  Motion-off frames and timing after it, and remove the tool-side Net.place workaround.
- Engine change, skin `linkStyle(link)`: APPROVED (from C polish 5). An optional skin function returning
  `{color, width, dash}` (any may be omitted) for a link that is up, applied in `draw` and `update`; down links keep
  `colors.down`. Backward compatible (no option, no change). Document it in docs/families/network.md's skin options
  (the integrator added the guest recipe that names it), re-check internet-journey's frames, and move the tool's
  guest styling onto it.
- Engine change wanted, `homeOnly` on path/reach: DECLINED. The tool's `skip: l => l.guest` is the documented way;
  the integrator adds the guest recipe to docs/families/network.md and corrects the spec's Family engine line.
- Not findings: audit "Tablet: nothing changed" (selected by default; all three lenses); `__tool.claim` from the ask
  step (test API only, C nit 4); Kitchen 255 vs 255.54 (nothing on screen shows a distance).
- C nit 2 (network.md table row lists fewer engine parts): integrator doc edit with the guest recipe.

#### Spec open questions

- **Item 1: SETTLED by Cory 2026-10-28, "all three".** The integrator wrote it into spec.md (claim step, need-clue,
  kind and wrong-kind lines, Q4 answers for calls 1, 3, 6, 7, call 1 keys Q4 and Q1 together). The proposal as asked:

- **Item 1, for Cory.** The spec's own design (labeled groups, Q4 answers, "Right cause" reply) lets a student skip
  the diagnosis. Proposed, all three together: (a) judge the clue before the cause: if no selected clue is a key
  clue, every cause gets the same reply ("That clue doesn't prove a cause yet. Pick a clue that shows what is
  broken."); (b) the claim step starts with three kind buttons (Connection, Logging in, Permission), then shows that
  kind's causes; a wrong kind gets a kind nudge ("Logging in worked here. Look at the login clue."); (c) Q4 answers
  on calls 1, 3, 6 and 7 describe what the caller sees rather than name the cause, and call 1's keys become Q4, Q1
  (call 2's Q3 is a rule-out clue only, accepted alongside Q4) (T P1).

#### Integrator fix after polish (2026-10-28)

- Call 2's keys were Q4, Q3 in the spec; the proposal Cory approved made its Q3 a rule-out clue, accepted only
  alongside Q4 (Codex flagged it under Left open in polish.md). Spec row and Key clues line, and `CALLS[1].keys` in
  src.html, are now Q4 only. Q3 alone on call 2 now gets the need-clue reply; Q3 with Q4 still solves.

#### Exit check, round 1

Checked cold on the worktree build (bundle 131,561 bytes, rebuilt with the same md5), with drive.py on ports 9961 and
9962 and the 375 host on 8804, real held clicks where it matters, every frame looked at. Polish.md read as claims.

Should fix:
- 1 Cause found without diagnosis: held. Kind buttons come first; a weak clue gets need-clue for any cause and no time
  (call 1 with Q2, Q4 alone, Q1 alone; call 2 with Q3 alone); wrong kind +2; wrong cause +2 with a ping and a nudge
  quoting the key clue; Q4 answers describe what the caller sees. Checked by claim() runs and held clicks.
- 2 Map draws unknown as working: held. Unknown links grey dotted after Q1 on calls 1 to 4; call 5 and House router
  off show every link down, no Wi-Fi arcs. Frames.
- 3 Cloud inside the Kitchen, line through devices: not held (partly). The cloud is outside the walls and the line
  misses the device tiles, but the Internet line crosses the "Back door" label at every size and the "Internet" label
  at 1280, 1366 and 1920; call 4's fixed Wi-Fi link runs through the Tablet tile and the fixed phone sits on the
  house's right wall. Frames and zoom crops.
- 4 Cause board hides groups: held for kinds and causes (all in view at every size). The clue cards in the same step
  are not (see New 1).
- 5 Resize mid-ping throws: held. Own test on the 375 host: calls 1 to 7 claimed, the iframe resized four times
  mid-ping and mid-fix; no errors, busy false, Send fix and Back enabled after, solves recorded.
- 6 Call 8 "Allowed" badge: held. "Sent" on Ana's laptop, labels "Ana's laptop" and "Family laptop", checks on the
  family laptop and printer, kind lines match. Frames.
- 7 Broken link uses the Guest look: held. Broken is grey dashes with a break mark, Guest orange dash-dot, legend
  shows Broken. Frames.
- 8 Next-call line lost, wrong hint: held. Held clicks through calls 1 to 4: next-call spoken once about 4 s after
  the first solve, silent after; each solved line spoken every time; hint reads right.
- 9 680x425 controls cut: held. Solved state has Next call beside the stamp and all 8 phones; shift report buttons in
  view. Frames.
- 10 Skipped welcome late: held. No welcomeAfter; a first question tap speaks ask only; Sound off and on brings the
  welcome back once. vlog.
- 11 Shed spot on the wall: held for the shed (tablet and phone inside the Shed in call 4 and House). The call 4 fixed
  phone on the right wall is logged under 3.
- 12 "No bars" hint sticks: held. Drag to the shed speaks "far"; arrow keys back give the house hint.
- 13 "1 bars": held ("1 bar" in code and frame).
- 14 Builder talk in notes: held (no 255, units or spec; "one small step per press").
- 15 First hint names no control: held ("Tap a question to ask the caller. Then tap Make a claim.").

Polish accepted:
- 1 Proved by and key marks: held. Solved cards show "Proved by: Qn" and the answer.
- 2 House kind stamps: held.
- 3 Device-only settings: held (the tablet panel shows only its own controls).
- 4 X placement: held (call 5 X on the dark router, call 3 beside the router).
- 5 Small-map labels and icons: partly held; compact desktop/TV and phone/tablet icons are only slightly distinct.
- 6 375 faded: not held. Badges sit over tiles and a check covers the "Office" label at 375 (calls 1, 3, 6).
- 7 Bars by the tablet: held ("2 / 3" under the tablet).
- 8 1920 readable: held.
- 9 680 House labels, no duplicate About: mostly held; at 680x425 and 1000x625 the help text runs behind Reset house
  and the Router and Desktop cable buttons sit in house-scroll (map taps still work).
- 10 Badges never over tiles: not held. 680x425: router "On" under the printer tile, the TV check on the desktop
  tile; 760x900: "On" under the printer, the TV tile on a wall; 1366 call 5: the "?" badge on the TV tile; caller
  badges (Online, Grown-up, Sent, Allowed, Guest, Signed in) float on the top wall away from their device.
- 11 Phone and Laptop labels off walls, the cloud link: not held. "Laptop" sits on the Kitchen wall in call 3 at 1366,
  "Ana's laptop" on a wall in call 8; the cloud link crosses Back door (see 3).

Settled calls: held. Welcome not re-said after a first tap (Should fix 10); Motion off keeps timing (fix about 1503
vs 1512 ms, ping 1232 vs 1223 ms); only Motion is saved.

Engine changes:
- glide reads calm() per tick: held. internet-journey bundled (210 KB): first screen at 1366 and 680 fine, a send
  takes 5852 ms with Motion on and 5989 ms off, bounce 4A at 6204 vs 6211 ms, 4B about 4.2 s, all 8 pieces arrive,
  the calm mid-bounce frame shows "bounced", no console errors.
- skin linkStyle: held. Custom color, width and dash for up links only; defaults unchanged; documented in
  docs/families/network.md with the Guest recipe.

Integrator fix after polish: held. Call 2 Q3 alone gives need-clue; Q4 solves; Q3 with Q4 and a wrong cause gives
wrong. CALLS[1].keys is [4].

New (not on the merged list):
- New 1 (should fix, BUILD lesson "a short set of choices never hides in a scroll panel"): the claim step's clue
  cards sit in a scroll panel. 680x425: only Q1 and Q2 show, 4 of 6 hidden with no peek (even the Q1 + Q4 minimum is
  clipped); 375: Q1 and Q2 show, Q3 and Q4 peek; 800x500 and 760x900: Q5 and Q6 hidden (keys on calls 3, 6, 7, 8).
  The Questions-step clue list is cut the same way at 375 and 1000x625.
- New 2 (nit): in the shed drop the X badge covers the "Shed" label.

Gate:
1. Every Done when: passes, except that Done when 7 holds only in letter (Questions and Make a claim are in view at
   every size; the claim step's clue choices are not). All 8 calls solved by held clicks; House combos fail only the
   right targets; keyboard-only solve works; 375 works in the host.
2. Codes taught: held. CSTA E4-SYS-NT-14, E4-SYS-SE-13, 1B-CS-03, 1B-NI-05 are taught by the calls and House.
3. Solo defaults: held. Opens on call 1 with the first hint naming the control; no setup needed.
4. Sensitivity: n/a (no people pictured, no rule 5 topic; callers are icon badges).
5. No open blocker or should-fix: fails (New 1, Should fix 3).
6. Bundle: 127 KB, no console errors in any shot (only the host favicon 404), no network requests.
7. Voice counts: right (table below).

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| w-calls | welcome | once per mode, back once after Sound off and on | once; once more after the Sound cycle |
| w-house | welcome | once | once |
| ask | how | once, then hint | once (dropped under the welcome, then once) |
| kind | how | once | once |
| claim | how | once | once |
| house | how | once | once (dropped if the mode changes first) |
| all-clues | how | once | once |
| next-call | how | once | once in 4 solves |
| need-clue | event | 5 of 5 | 5 |
| wrong | event | 5 of 5 | 5 |
| wrong-kind | event | 5 of 5 | 5 |
| solved-* | event | 4 of 4 | 4 |
| far | event | on a drag to the shed | spoken |
| read | Read | speaks the hint, also with Sound off | read both times |
| stale line after a mode change or reset | none | 0 | 0 |

#### Audit pilot (exit)

- Leads confirmed: the claim-step clue cards "cut short by a scroll panel" (680x425, 375, 800x500, 760x900); the
  Internet line across "Back door" and "Internet"; "Laptop" and "Ana's laptop" on walls; house-scroll hiding the
  cable buttons at 680x425 and 1000x625; the 375 router and "2 / 3" overlap.
- Leads wrong or noise: most "line drawn across" leads on tile tspans (Printer, Router, TV, Desktop) and on badge
  text ("On", "Off", "Plug out") are wall or route lines passing near a label and read fine on the frames. The
  "welcome not heard after a first tap" rows are the settled behavior (Should fix 10), not a finding.
- Missed: badges under tiles ("On" under the printer at 680x425 and 760x900), the "?" on the TV tile in call 5,
  caller badges detached from their device on the top wall, call 4's fixed link through the Tablet tile, the fixed
  phone on the right wall, the X over the "Shed" label.

#### Exit check, round 2

Cold, on the worktree bundle (md5 eac43f34, 145,718 bytes), drive.py on 9961/9962, 375 host on 8804; frames in
S:/CurioClass-codex-scratch/network-help-desk/exit-r2/f/ (claim, early, solved, regress), sheets in exit-r2/sheets/.
Every call with Q1 to Q6 asked and its kind chosen, plus call 1 with each kind and with no kind, at all six sizes;
every call after Q1 only and every call solved at all six sizes. Frames looked at, zoomed where close.
- 1 Clue cards in a scroll panel: held. All six cards fully in view, no scroll or clip ancestor, Send fix and Back in
  view, at 680x425, 800x500, 760x900, 1366x768, 1920x1080 and 375 (claim/<size>-c1..c8-claim, -c1-kind-*).
- 2 Lines: not held (narrow). Held parts: the Internet line no longer crosses "Back door" or "Internet" at any size
  (680x425-c5-claim and 375x812-c5-claim: the break mark ends right against the "B", touching, not over); call 4's
  fixed phone sits inside the Bedroom and its Wi-Fi link misses the Tablet at every size (solved/*-c4-solved).
  Not held: at 680x425 the fixed Wi-Fi link in call 4 runs along the Internet cable from the router, so only a short
  blue stub shows and the path reads as a cable (solved/680x425-c4-solved); the same shared run puts call 3's Wi-Fi
  and call 8's Guest dashes on top of the cable at 680x425 and 800x500 (680x425-c3/c8-solved, 800x500-c3/c8-solved,
  claim frames too). Fix: give links leaving the router their own lane, or route the cable first and avoid it.
- 3 Badges and labels: held. "On" sits beside the router (not under the printer); call 5's "?" sits beside the
  router, clear of the TV (early/1366x768-c5-q1); caller badges sit on their own device; no check over "Office" at
  375; "Laptop" and "Ana's laptop" inside the Kitchen. A rect test over every badge, label, tile, room name and wall
  found no overlap in 168 frames. Polish only: 800x500-c4-solved the router's Wi-Fi arcs draw through the "On" badge;
  680x425-c3-solved "Signed in" and -c4-solved "Online" end a few px from the house's right wall.
Other notes (polish): the Internet cable often runs on or just beside a wall (680 calls 1 and 4 solved, 800 call 4
solved) and through the Shed at 680, 800 and 1366; reads as a wall line, not a crossing.
Regression look: held. Real held clicks solved call 1 (Connection), call 3 (Logging in, also at 680x425) and call 7
(Permission): stamps, fix, "Proved by" and focus on Next call right. Shift report at 1366, 680 and 375: all 8 rows,
Start a new shift and Open House in view. House at 1366 and 680: router off shows every link down and "No
connection". Keyboard: Tab from the claim step reaches kind, cause, all six clue cards, Send fix, Back and the strip
in order at 1366 and 680; Enter toggles a card. Console: no errors or exceptions (only the host server's favicon 404).
Shared audit: audit-r2exit/audit.md did not exist when this check finished (frames only); not waited for.

#### Integrator fix after exit round 2 (2026-10-29)

- Item 2, links leaving the router on the Internet cable's run (call 4 Wi-Fi at 680x425; call 3 Wi-Fi and call 8 Guest
  at 680x425 and 800x500): routeMapLinks now remembers each routed link's segments, adds lanes 7 px either side of
  them to the route grid, and charges 400 for any step along an earlier link's line, so each later link takes its
  own lane. Checked by re-running the exit check's 48 solved shots, the claim shots at 680x425 and 800x500 and its 12
  regression shots: call 4's Wi-Fi reads as one blue path to the tablet, call 3's Wi-Fi and call 8's Guest run in
  their own lanes, no route issues, the exit check's badge and label rect tests still empty, a call of each kind solves,
  Shift report and House as before, no console errors (host favicon only). Frames: exit-r2/lanes/, exit-r2/lanes-regress/.
- Left as is: the printer cable meets the Internet cable at the router's corner (an 11 to 30 px junction, not a
  shared run), and the Polish notes from exit round 2 (Wi-Fi arcs through the "On" badge at 800x500 on call 4 solved;
  two badges a few px from the right wall at 680).
- No fresh exit round was run on this change; the drive checks above are the evidence.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: network-help-desk (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, audit-states.json (no art: the spec says drawn in code).
Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py network-help-desk` (119 KB). Audit run first
(`scripts/audit_tool.py --port 9420`, 3 leads), then my own drive.py runs on port 9422. Evidence in
`S:/CurioClass-codex-scratch/lens-craft/` (audit/, frames/, voice/ with the shots files and outputs).

Counts: blockers 0, should fix 6, polish 5, nit 4.

#### Contract

- One file, 119 KB, well under 2 MB. The only URLs in the bundle are the sources in an HTML comment and the SVG
  namespace; no fetch, XHR or import. Kit used for voice, motion, sound, chimes, icons, map and mover
  (`kit:curio`, `kit:network`).
- Console: 0 errors across the audit (every size, every state, every control walk) and my 30-odd drive shots.
- Motion off keeps time: a full call-1 solve took 2745 ms with Motion on and 2745 ms with Motion off (fix 1504 vs
  1506 ms, ping 1230 vs 1231 ms). Audit: nothing runs forever with Motion off.

#### Access

- Keyboard: a keyboard-only solve of call 1 works (focus trace: modes, Motion, Sound, Read, q1 to q6, Make a claim,
  cause-1 to cause-9, evidence-1, evidence-4, Send fix; frames/kb-solved.png shows Solved with a visible purple ring
  on Next call). Escape leaves the claim step. Arrow keys move the focused tablet in House (20 units, focus kept).
- Targets: the audit finds no target under 44 px at any size. Selected causes and clues carry a check and "Selected",
  not color alone; badges carry a check, X or word.
- Sound off then on brings the skipped welcome once; Read speaks the hint with Sound off.

#### Findings

##### Should fix

1. **House, stale "far" hint** (src.html, `moveTablet`). Once the tablet reaches 0 bars the hint becomes "No bars.
   Walls and distance weaken Wi-Fi. Drag the tablet closer to the router." and never changes back when the tablet
   returns in range: `moveTablet` calls `renderHouse()` but not `updateHint()`. Seen: drag shed then back to (400,330)
   gives bars "about 3 bars of 3" with the "No bars" hint; arrow keys to (670,520) give "about 2 bars of 3" with the
   same hint (voice/out, shots3 `house-far`, shots2 `house-far-keys`). Read then speaks a false line. Better: when bars
   go above 0, `updateHint()` back to the House hint. general.
2. **Calls map, the Internet wire runs through other devices** (src.html `makeGraph` / `displayPosition`, cloud at
   (850,80)). The cloud sits inside the Kitchen, and the Router to Internet line passes straight across the Phone tile
   (frames/kb-solved.png, audit state-claim-two-clues-1366x768.png) and across Ana's laptop in call 8
   (frames/call8-q1.png, audit state-shift-report-1366x768.png). It reads as if the phone or laptop is wired into the
   path, on a tool whose whole job is reading paths. Better: put the cloud outside the house walls (top right, over
   the lawn) or route that link with `via` around the rooms, so no device tile sits on it at any size.
   family:network.
3. **Cause board hides whole groups at small sizes** (claim step CSS `.claiming .cause-board`, `.claim-clues`).
   At 680x425 only the four Connection causes show; Logging in and Permission are below a scroll with no cue
   (audit state-claim-two-clues-680x425.png). At 800x500 the "Logging in" legend sits cut under the "Tap 1 or 2 clues"
   title (state-wrong-claim-800x500.png); at 760x900 the Permission group is hidden and the board's scrolled content
   shows under the title (state-claim-two-clues-760x900.png); 375 is the same. "Not allowed" is the answer to 2 of
   the 8 calls, and the spec asks for 7 cards in 3 labeled groups. Better: a compact 3-group board (smaller buttons,
   two or three per row, short legends) that fits without scrolling, or at least a visible "more causes" edge.
   general.
4. **A down link looks like the Guest link** (src.html `Net.draw` colors `down:'#a4471b'`, guest stroke `#a4471b`
   dashed). In House a tablet in the shed gets an orange dashed link that matches the legend's "Guest" swatch
   (audit state-house-shed-375x812.png); in Calls the unplugged cable is the same orange dash
   (frames/call1-q1q4.png). Only a small break mark tells them apart. Better: give down links their own look in the
   legend (for example grey dashes with the break mark, listed as "Broken") and keep orange for Guest only.
   family:network.
5. **Q1 draws a broken link as working** (src.html `updateMap`, `l.up=... s.asked.includes(4)?original.up:true`).
   After Q1 in call 1 the desktop cable is drawn solid and connected (frames/call1-q1.png); it only turns broken after
   Q4. Calls 2 and 4 do the same with Wi-Fi. The map shows a state that is not true. Better: after Q1 draw the medium
   (cable, Wi-Fi, Guest) in a neutral "status unknown" style, and show up or down only once a clue reveals it. Keeps
   the no-giveaway intent without a false picture. general.
6. **Ana's solved badge says "Allowed"** (src.html `updateMap`, Permission maps to "Allowed"). After call 8 her guest
   laptop carries a green "Allowed" badge (audit state-shift-report-1366x768.png), but the lesson is that the guest is
   still not allowed to reach the printer; the file went through a family laptop. Better: a badge that matches the
   fix ("Sent", or the check on the family laptop and printer), keep "Allowed" for Leo's Student page. general.

##### Polish

1. **First question tap: the welcome plays after the student already acted** (`welcomeAfter:true`). A first tap on a
   question speaks "Ask questions until you know..." and then "Welcome to the help desk... Tap a question to ask it."
   (voice/out, shots3 `first-q1-poll`: ask at 1.3 s, welcome at 6.7 s). KIT.md says `welcomeAfter` is for one-mode
   tools; this one has two. Better: on a first question tap play the welcome's first two sentences only, or skip it
   (it returns on the next Calls entry). Open question already in BATCH-BR-LOG. general.
2. **Device names vanish at the preview sizes** (`label: smallMap()?'none'...`, room names 12 px). At 680x425,
   800x500 and 375 the devices are icons only and rooms are 12 px; the spec asks room names at 14 px or more and the
   family doc asks labels kept at 12 px or more at 680x425, not dropped (audit size-680x425.png). Better: short labels
   at 12 px, or an aria-free legend chip for the caller's device. family:network.
3. **Clipped endings at 680x425.** On Solved, Next call (which takes focus) is cut at the bottom of the scrolled Solved
   card, and call 8 in the strip needs a sideways scroll (audit state-solved-680x425.png, size-680x425.png; 375 too).
   Both are scroll panels, so the audit rightly skips them. Better: shorten the Solved card at short heights (put
   Next call beside the stamp) and let the strip wrap or shrink to 8 across. general.
4. **House at 680x425**: the obstacle search pushes "Living room" up into the Office, and the "About: walls and
   distance weaken Wi-Fi." line shows half cut under Reset house (audit state-mode-house-680x425.png). Better: fixed
   room-label spots per layout, and drop the duplicate "About" line in the panel when the stage note already shows it.
   general.
5. **Guest is a tool-side patch on engine DOM** (src.html `updateMap` sets stroke and dasharray on engine link paths
   after every `view.update()`; houseTry and runPing pass `skip: l => l.guest`). It works (Guest then Home restores
   the blue stroke, checked), but the spec's "Family engine" says the engine's Path ignores guest links, and neither
   kit/network.js nor docs/families/network.md has a guest concept. The family rule says new engine features go into
   the engine and the doc together. Better: a `guest` link style in the skin colors and a documented `skip` recipe in
   network.md, or correct the spec line (handoff.md already asks for `homeOnly`). family:network.

##### Nit

1. Map labels under walls: the audit flags "Phone" and "Laptop" under a rect in the shift report at 1280, 1366 and
   1920; "Laptop" sits on the Living room wall line in every 1366 frame. Nudge the label or the node. general.
2. docs/families/network.md table row for network-help-desk lists "graph, draw, send ('ping'), down nodes and links,
   reach"; the tool also uses path, token, stop, addNode/addLink and icon. family:network.
3. For the Teaching lens: "Right cause. Now tap a clue that proves it." confirms the cause for free (no Call time),
   so trying causes with any non-key clue finds it at 2 min per miss. Spec-mandated; noting only. general.
4. `__tool.claim(n, cause, clues)` from the ask step leaves the panel on Questions while the hint says "Tap Back to
   questions" (frames/call5-wrong.png). Test API only, never reached by a student. general.

#### Lines

- `__tool.allLines()` returns 19 lines; voice/lines.json has the same 19, word for word, same order. Every spec line
  (w-calls, ask, claim, need-clue, wrong, the three solved lines, next-call, shift, w-house, far) is present as
  written. The 7 extra lines are hint lines (ask-first, all-clues, shift-next, report, house, watch, retry); each names
  an enabled control at its moment.
- Spoken lines matched their screens in every frame I took, except the stale "far" hint (should fix 1) and the
  welcome after a first question (polish 1).

#### Standard voice check (Sound on, Motion on, held clicks 0.12 s)

| line | kind | expected | spoken |
|---|---|---|---|
| w-calls | welcome | 1 | 1 (5 questions in a row) |
| ask | how | 1 of 5 question taps | 1, then not queued |
| all-clues | how | 1 | 1 (on opening a call with all six asked) |
| claim | how | 1 across claims | 1 across 5 claims and 5 Send fix taps |
| need-clue | event | 5 of 5 Send fix | 5 |
| wrong | event | 5 of 5 Send fix | 5 (Call time 11 = 1 + 5 x 2) |
| solved-conn / solved-login | event | every solve | 4 of 4 / 1 of 1 (5 calls in a row) |
| next-call | how | 1 of 5 solves | 1 |
| w-house | welcome | 1 | 1 |
| far | how | first 0 bars | 1 by drag; dropped (valid failed) when queued behind the welcome by keys |
| shift, solved-perm | event | every time | not counted by me (shift reached in the audit state only) |

- Stale: q1, q4, Make a claim, a cause, House, Reset at 0.2 s: ask, then claim (ask cut), then w-house (claim cut);
  nothing old played after; final hint is the House hint.
- First tap: the stage and a key (Tab) bring the welcome within about 0.15 s; a mode button brings only its own
  welcome; Read speaks the hint only; Sound says nothing and Sound off then on brings the welcome once; a question
  brings its own line, then the welcome (polish 1).
- Read: during "ask" it stops the line and speaks the hint; with Sound off it speaks the hint; House right after Read
  starts w-house at once.
- Order: spoken lines followed the actions in every run.

#### Art and words

- No `art:` tokens and no prompts.json, as the spec says (all drawn in code, no people, callers as handset icons).
- No em or en dashes in src.html, notes.md, tool.draft.json or voice/lines.json. "Curio Class" only. Classroom-safe.
- Privacy is stated in both panels ("Pretend passwords. Nothing sent or saved. Only Motion is remembered on this
  device."), and that is true: the kit stores only `curio-motion`.

#### Wave lessons (BUILD.md)

- Hint and voice: met except should fix 1 (hint not changed when the state changes back).
- Focus and layout: focus kept on rebuilds (audit "rebuilt, focus kept"), none on load, hint height reserved. Labels
  and badges: nit 1, and should fix 2 (tiles sitting on a link).
- Sizes: 44 px targets and an unclipped hint at every size, 375 included. Cause groups hidden at small sizes
  (should fix 3).
- No giveaways: see nit 3 and should fix 5. Honest numbers: bars say "about", Call time says what it counts.
- Family doc matches the engine: no (polish 5, nit 2).
- Motion off: clean.

#### Builder claims checked afterwards

Read codex-report.md and handoff.md only after the findings above.
- "Latest targeted audit has zero overlap leads" and "all 470 PNGs were viewed": this audit has two label-under-rect
  leads (nit 1), and the frames show the Internet wire across the phone and Ana's laptop (should fix 2).
- "PASS, no free sweep": the "Right cause" reply still confirms a cause at no cost (nit 3); arguable, spec-driven.
- "PASS, family engine ... Net.path/reach use guest skip": true for the tool; the spec's claim that the engine
  ignores guest links is not, and the family doc was not updated (polish 5).

#### Audit pilot

- Confirmed: the shift-report "Phone"/"Laptop" labels under a rect (nit 1). Its clean rows held on my own runs:
  Motion off, focus on load, console, 44 px targets, the five-clicks and quick-tap voice rows (my counts agree).
- Wrong: "Tablet: nothing changed" is not a dead control; the tablet is selected by default, so a tap on it changes
  nothing by design.
- Missed: the stale "far" hint (needs a drag back, a state no one listed), the Internet wire through device tiles, the
  down link looking like Guest, the false "connected" link after Q1, the "Allowed" badge on Ana, and the welcome
  played after a first question's own line (it reports "heard", not the order). It also cannot see the cause board's
  hidden groups, Next call cut in the Solved card or call 8 off the strip at 680x425, since all three sit in scroll
  panels it skips by design: a lens still has to look at the claim and Solved frames at the small sizes.
- Verdict: useful as a first pass (clean rows I could cite, one real lead, one false one), but it caught 1 of my 15
  findings; it does not replace the lens.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: network-help-desk (round 1)

Played cold twice: as a grade 4 student alone at home on a 1366x768 laptop, and as a teacher projecting at 1920x1080.
Bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py network-help-desk` (119 KB, no recordings yet). Frames in
`S:/CurioClass-codex-scratch/lens-play/shots/` (my drive.py runs, held clicks), voice logs in `.../lens-play/voice/`
(the printed `V.log` is quoted below), audit in `.../lens-play/audit/`. I looked at every frame named here.

Counts: blockers 0, should fix 11, polish 8, nit 3.

#### Should fix

1. **The puzzle can be solved the cheap way: ask "What does the screen say?", then pick the card with the same
   words.** Calls (whole tool). I solved all 8 calls with one question each, 1 minute each (`report-1366.png`: Q1,
   Q4, Q4, Q4, Q2, Q4, Q4, Q1). Six of the eight Q4 answers say the cause card almost word for word: "Network cable
   unplugged" for Cable unplugged, "Incorrect Wi-Fi password" for Wrong Wi-Fi password, "no bars" for Too far, "Wrong
   password. And the Caps Lock light is on" for Wrong account password, "You don't have permission" for Not allowed,
   and the airplane for Wi-Fi turned off. A wrong claim also costs nothing that matters (+2 display minutes), and its
   nudge names the question to ask ("Try asking: What does the screen say?", `c1-wrong-1366.png`), so trying cards
   until one works is free. The student never sorts the problem into a kind; the kind comes stamped from the card's
   group. This misses the BUILD wave lesson "no puzzle can be solved by trying every option for free". The builder
   followed the spec's Content, so this is a spec call for the integrator: for example, make Q4 describe symptoms
   rather than name the cause on some calls (Grandma June: "It says the password is wrong" and the Caps Lock light only
   in Q5), ask the student to pick the kind (Connection, Logging in, Permission) before the cause card, or require one
   proving clue that is not Q4. Tag: general.
2. **"Not allowed", the only Permission card, is hidden at 1366x768 after any nudge.** Claim step. Once the orange
   nudge shows (right cause without a key clue, or a wrong claim), the cause board shrinks and its last row is cut
   off inside a scroll panel: only the "Permission" heading's top edge shows (`c1-needclue-1366.png`,
   `c1-wrong-1366.png`, `c7-solved-1366.png` which is really a wrong claim on Leo, `c8-solved-1366.png` likewise for
   Ana). Calls 7 and 8 are exactly the ones where a student retries after a wrong claim and needs that card. Before
   any nudge it shows (`c1-claim-1366.png`). Tag: general.
3. **At 680x425 the cause board shows only the Connection group.** Claim step (`c1-claim-680.png`,
   `c6-solved-680.png`). Logging in and Permission, and half of the second Connection row, are below a scroll edge
   with no cue, so a student in the site preview sees four causes and may not know the other two kinds exist. Same at
   375 (`audit/state-claim-two-clues-375x812.png`: Logging in heading cut, Permission gone). The audit does not count
   it because the board is a scroll panel. Tag: general.
4. **The "next call" how line is never spoken, and its hint names the wrong control.** Solved card. After a solve the
   log shows the solved line and then nothing: `v-solve1b` waited 16 s, `V.heard('next-call')` is false; in
   `v-solve3` the line is logged `dropped` 2.4 s after each solved line, before any tap. The hint then reads "Tap the
   next phone on the call strip to take another call." while a **Next call** button sits in the Solved card with focus
   on it (`c1-solved-1366.png`, `kb-solve.png`). Say the button that is there: "Tap Next call, or a phone on the call
   strip." and make sure it plays once. Tag: general.
5. **At 680x425 the Next call and Shift report buttons are cut off.** Solved card (`c1-solved-680.png`: only the top
   edge of Next call shows; `report-680.png`: the Shift report button is out of view while the hint says "Tap Shift
   report to compare all eight calls."). My drive click on `#next-call` at 680 did not open the report. The 8th
   phone on the call strip is also clipped at 680 and 375 (`c1-claim-680.png`, `audit/state-solved-375x812.png`).
   Tag: general.
6. **The skipped welcome comes back after the student has already acted.** Calls, first tap. Tap a question first and
   the log reads `ask` (1.3 s) then the welcome at 6.6 s: "Ask questions until you know ... Then tap Make a claim."
   followed by "Welcome to the help desk ... Tap a question to ask it." (`v-ask5`, `v-all6`, `v-askfirst`). At a 2 s
   pace the welcome lands while the student is on their fourth question. The tool sets `welcomeAfter: true`, which
   KIT.md says is for one-mode tools; this tool has two modes, so STANDARDS applies: skip the welcome on a first tap
   that has its own line and let Sound off/on or the next mode entry bring it. The audit's "welcome heard" column marks
   this as fine; it cannot hear the order. Tag: general.
7. **A broken link uses the Guest look.** Map, Calls and House. A cut cable or a 0-bar Wi-Fi link is drawn in orange
   dashes (`c1-all6-1366.png`, `c4-all6-1366.png`, `house-shed-1366.png`), and the legend says orange dots mean
   "Guest". A student reading the legend sees Grandpa Lou's desktop "on the Guest network". Give the broken state its
   own style (grey with the break mark, or red X on the link) and keep orange for Guest only. Tag: family:network.
8. **Router off still shows Wi-Fi waves and working links.** House (`house-routeroff-1366.png`). The router tile is
   orange with "Off" and every device has an X, but the blue arcs still radiate and every cable and Wi-Fi link is drawn
   up. The picture says the network still works. Draw the links down (or faded) and drop the arcs when the power is
   off. Call 5 (router has no power) has the same problem: the dark router still shows Wi-Fi arcs to Aunt Rosa's
   laptop (`c5-all6-1366.png`). Tag: general.
9. **The Shed spot is drawn on the Shed's wall, not in the Shed.** Sam's phone (Call 4) sits on the Bedroom/Shed wall
   over the "Back door" label (`c4-all6-1366.png`); after the fix it moves onto the "Back door" label, covering it
   ("k door", `c4-solved-1366.png`). In House the tablet at the shed spot also lands on the wall (`house-shed-1366.png`,
   `audit/state-house-shed-375x812.png`), and the drawn Shed room is empty. The rooms are drawn on screen fractions
   while devices use the design box, so they don't line up near the edges. A student told "it works fine in the
   house" should see the phone out in the Shed. Tag: general.
10. **Ana's laptop is badged "Allowed" when she is not allowed.** Call 8 solved (`c8-solved-1366.png`). The fix is to
    send the file to a family laptop because the guest can't reach the printer, but Ana's guest laptop gets a green
    "Allowed" badge, and both laptops are labelled "Laptop", so the student can't tell which one printed. Badge Ana's
    laptop "Sent" (or leave her "Guest" badge) and label the two "Ana's laptop" and "Family laptop". Tag: general.
11. **"about 1 bars of 3".** House readout (`house-corner-1366` result: "At this spot: about 1 bars of 3"). Words match
    the state (POLISH): "about 1 bar of 3". Tag: general.

#### Polish

1. **Small maps hide device names, and two pairs of icons look alike.** At 760, 680 and 375 the map draws icons only
   (`d-760.png`, `house-760.png`, `house-680.png`). Desktop and TV are the same monitor; Phone and Tablet are the same
   rectangle. In House the student taps devices by look, and "Tablet" is the one to drag. Short labels (or distinct
   icons) would fix it. The handoff calls the names "redundant"; at these sizes they are not.
2. **The 680x425 and 375 maps are crowded.** Badges cover icons and room labels ("Grown-up" over the desktop and
   printer, "On" over the TV and laptop, the Living room label under a badge at 375), devices straddle walls, "Office"
   sits on the top wall (`c1-all6-680.png`, `c1-solved-680.png`, `audit/state-claim-two-clues-375x812.png`). The spec
   asked for 375 to show the caller's room and router with the rest faded; it shows the whole house instead. A
   per-call crop at small sizes would make the preview readable.
3. **The internet cloud sits inside the Kitchen.** Every Calls frame: the router's cable runs across the Kitchen to a
   cloud by the Kitchen wall, crossing the Phone and Ana's laptop labels (the audit's shift-report lead). Put the cloud
   outside the house on the lawn, so "the internet" is clearly not a room.
4. **The Solved card drops the clue that proved it.** Clues hide on solve and the card says only "Questions asked: Q1,
   Q4" (`c1-solved-1366.png`). Show the proving clue's text ("Proved by: A little computer with an X: Network cable
   unplugged."). It is the moment the lesson should land. The shift report could also mark the key question per call,
   since it asks "which questions found the problem fastest?" but never says.
5. **House results don't name the kind.** The result chip looks the same for "Online", "No connection", "Wrong
   password" and "Not allowed" (`house-try-1366.png`, `house-routeroff-1366.png`), though the code computes the kind.
   A stamp (plug, key, hand) like the Solved card would let House reinforce the three kinds, and a pass/fail glyph
   would help.
6. **The Wi-Fi bars live only in small grey text in the panel.** House: dragging the tablet, the student must look away
   from the map to "At this spot: about 2 bars of 3" (`house-1366.png`). Bars drawn next to the tablet on the map would
   make the drag the experiment. There is also an empty gap under the Try row where the result chip is reserved.
7. **First-screen hint names no control.** "Ask questions until you know what kind of problem it is." (`d-1366.png`).
   For a solo student: "Tap a question to ask the caller. Then tap Make a claim."
8. **Projector sizes.** At 1920x1080 the call time, privacy line, legend and map notes are 11 to 13 px
   (`d-1920.png`); a class reading clue cards off the screen would want the map notes and legend larger.

#### Nit

1. Need-clue shows the same message twice, in the nudge and the hint ("Right cause. Which clue proves it? Tap a
   different clue." / "Right cause. Now tap a clue that proves it.", `c1-needclue-1366.png`).
2. The "Online" and "On" badges sit over the device tile and the router link (`c1-solved-1366.png`, `c4-solved-1366.png`
   where "Online" also covers the Tablet).
3. The wrong-claim X on calls 3 and 8 covers the router icon (`c8-solved-1366.png` wrong-claim frame).

#### What worked

Every call opens on a clear call card; each question lights the right part of the map (`c1-all6`, `c4-all6`,
`c5-all6`, `c7-all6`, `c8-all6` match the spec's answers); the wrong ping stops at the break with an X; the kind stamps,
fix sentences and kind lines are right for calls 1 to 8; Call time counts +1 and +2 (`v-wrong5`: 11 min after one
question and five wrong claims); keyboard-only solve works and focus lands on Next call (`kb-solve.png`); Motion off
keeps the fix wait (`c3-mid-calm-1366.png`, `c3-solved-calm-1366.png`); House results follow the rule order (library
with Caps Lock, printer on Guest, shed 0 bars, router off all checked).

#### Voice check (browser voice, held clicks, Sound on)

| line | kind | expected | spoken |
|---|---|---|---|
| ask (5 questions, 6 s apart) | how | 1 | 1 |
| claim | how | 1 | 1 |
| all-clues | how | 1 | 1 |
| ask-first (Make a claim twice, no clue) | how | 1 | 1 |
| wrong (5 wrong sends) | event | 5 | 5 |
| need-clue (5 sends) | event | 5 | 5 |
| solved-conn / solved-login (3 solves) | event | 3 | 3 |
| next-call | how | 1 | **0** (dropped or never queued; should fix 4) |
| w-calls after a question as first tap | welcome | skipped until Sound or mode | **played after the tap's line** (should fix 6) |

First taps: Sound says nothing (`v-first-sound`); Read speaks the hint only (`v-first-read`); House gets its welcome
(`v-first-house`); the stage and Tab get the welcome; Sound off and on brings the welcome once (`v-sound-offon`). Read
during a line stops it and a mode change after Read starts at once (`v-read-during`). Fast taps then House and back:
house welcome cut by the switch, calls welcome plays, no stale how line (`v-fast-stale`).

#### Audit pilot

Ran `audit_tool.py --port 9410` (full walk, 3 leads). Sizes, Motion off, focus on load, console errors and the voice
repeats were clean, and my own frames agree; I cite those rows.

- **Confirmed:** shift-report "Phone" and "Laptop" labels under another box: the router-to-cloud cable crosses both
  labels at 1280 and up (polish 3).
- **Wrong:** "Tablet: nothing changed". The tablet is selected by default, so a tap on it has nothing to change; it is
  not dead (drag and arrow keys work, `house-shed-1366.png`).
- **Missed:** the clipped cause cards at 1366 after a nudge and at 680/375 (inside a scroll panel, so it is skipped by
  design, but here the scroll panel hides a whole kind); the Next call and Shift report buttons cut off at 680; the
  next-call line never spoken; the welcome played after the first tap's own line (its column says "heard", which reads
  as a pass); and everything about meaning: the Q4 giveaway, the broken-link and Guest style clash, the router-off arcs,
  the Shed position, the "Allowed" badge on Ana, "1 bars".

Builder claim checked afterwards: handoff.md says compact maps leave out device names as "redundant"; at 760 and below
the desktop/TV and phone/tablet icons can't be told apart (polish 1).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: network-help-desk

Cold read of spec.md, src.html, notes.md, voice/lines.json (no art folder: the spec says art is drawn in code), the
draft bundle (`CURIO_DRAFT=1`, 119 KB), then my own drives at 1366x768 (`drive.py`, port 9402, held clicks and
`__tool` calls) and `audit_tool.py` (ports 9400 and 9401). Frames and JSON results are in
`S:/CurioClass-codex-scratch/lens-teaching/` (`frames/`, `drive/`, `audit/`, `calls-result.json`, `house-result.json`).
I did not read codex-report.md, handoff.md or CODEX-BRIEF.md before writing the findings.

Counts: blockers 0, should fix 8, polish 6, nit 2.

#### Standards on the module (rule 2)

Module computer-science-4-wired-wireless-and-login: E4-SYS-NT-14, E4-SYS-SE-13, E4-SYS-HW-12 ("Network connections;
authentication vs authorization").

- **E4-SYS-NT-14 (network connections): taught.** Q1 reveals cable, Wi-Fi or Guest Wi-Fi on the map; calls 1, 2, 4, 5
  are four different broken paths; House lets the student pull the desktop cable, turn Wi-Fi off, flip the router and
  drag the tablet through 3, 2, 1, 0 bars. Something the student does, every time.
- **E4-SYS-HW-12 (troubleshoot and test a fix): taught.** Ask, back a cause with a clue, send the fix, watch the test
  ping, and a wrong claim pings to the broken spot. Weakened by the cheap paths in S1 and P2, but the loop is real.
- **E4-SYS-SE-13 (authentication vs authorization): taught, but thinner than the tool's "One idea" promises.** Calls
  3 and 6 (Logging in) against 7 and 8 (Permission), and House (Caps Lock fails Library site only; Kid or Guest
  account fails Parent settings only), do put the difference in front of the student. But the student never has to
  sort a call into a kind: see S2.

#### Done when

| # | Check | Result | How I saw it |
|---|---|---|---|
| 1 | All six answers per call, map lights the matching part | Pass on text (all 48 answers match the Content table word for word); map caveat in S3 | `calls-result.json`: each call opened, Q1 to Q6 asked, clue text, badges, screen and login notes read after each |
| 2 | Cause plus one key clue: right stamp and fix sentence, ping reaches the cloud, printer or page | Pass, 8 of 8 (Connection 1, 2, 4, 5; Logging in 3, 6; Permission 7, 8; call 8 pings laptop to printer) | same run, solved card text and `state.ping.arrived` |
| 3 | Right cause with non-key clue asks for a proving clue; wrong cause stops at an X with the nudge for the first unasked key | Pass, 8 of 8 (nudge checked with no key asked, then with the first key asked, for every call) | `nudge*.json`, frames `t-c1-needclue`, `t-c5-wrong` |
| 4 | +1 per question, +2 per wrong claim, no score, Shift report lists 8 | Pass (6 questions = 6 min, one wrong claim = 8 min; need-clue adds nothing; report has 8 rows) | `calls-result.json`, frame `t-report` |
| 5 | House rules | Pass: router off fails all 24 device and target pairs; shed tablet 0 bars fails all four; Caps Lock fails Library site only; Guest network fails Family printer only; Kid and Guest accounts fail Parent settings only | `house-result.json` (6 devices x 4 targets in 10 states) |
| 6 | Voice | Audit voice rows, see Audit pilot; the Craft lens owns the full count table | audit |
| 7 | Sizes | See Audit pilot | audit |
| 8 | Keyboard-only solve; Motion off keeps timing; console clean | Keyboard: pass (call 1 solved with Tab and Enter only, focus lands on Next call). Motion off: pass (fix 1503 ms on, 1510 ms off; ping 1221 ms on, 1222 ms off). Console: clean in every normal run, but S7 throws | `kb.json`, frames `t-c6-solved`, `t-c6-solved-calm` |

#### Facts

- Wi-Fi bars recomputed from router (300, 330), straight distance in design units: Living room 108.17 (3), Kitchen
  255.54 (2), Bedroom 361.39 (2), Back door 480.83 (1), Shed 648.46 (0). The code's thresholds (250, 420, 560) give
  the same bars as the spec. The spec's "Kitchen 255" is 255.54 cut short; it changes nothing on screen (no distance
  is ever shown, only "about N bars of 3").
- Call fix sentences, kind lines and cause groups match the spec. Airplane mode, case-sensitive passwords, guest
  networks and distance through walls each trace to a listed source.
- The "Allowed" badge on Ana's laptop after call 8 states something the lesson says is false: S5.

#### Findings

##### S1. Should fix (general): the cause can be found by trying every card
Where: Calls, claim step (`claim()`, the `need-clue` branch). What: with any one clue selected (even one that proves
nothing), a right cause answers "Right cause. Which clue proves it? Tap a different clue." and a wrong cause answers
"I tried that." So a student can ask one question, pick that clue, and tap down the 7 cause cards until "Right cause"
appears, then try clues. It costs only display minutes. All 8 calls answer `need-clue` for the right cause with a
non-key clue (`calls-result.json`). This is the wave lesson "no puzzle can be solved by trying every option for
free". Better: judge the clue before the cause. If no selected clue is a key clue, answer the same way for every cause
("That clue doesn't prove a cause yet. Pick a clue that shows what is broken."), so the reply never confirms a cause on
weak evidence. Spec change (the need-clue line), so the integrator may route it.

##### S2. Should fix (general): the student never sorts a call into one of the three kinds
Where: Calls, claim step and Solved card; spec "One idea". What: the tool promises "you learn to sort every 'it won't
connect' into one of three kinds", and that sort is what carries E4-SYS-SE-13. But the cause board prints the kind
over each card (Connection, Logging in, Permission), and the Solved card stamps it afterwards. A student who matches
the screen words to a card (P2) solves calls 3, 6, 7 and 8 without once deciding "is this logging in or
permission?". Better: make the kind the student's own call. Either the claim step opens with three big kind buttons
and then shows only that kind's causes (a wrong kind gets a kind nudge: "Logging in worked here. Look at Q5."), or
the cause cards come unlabeled and the student picks the kind stamp before Send fix. House could ask the same (P3).
Spec change; integrator may route it to open questions, but rule 2 says the code should be taught well, not only met.

##### S3. Should fix (general): the map draws unknown parts as working
Where: Calls map (`updateMap`, `l.up=...asked.includes(4)?original.up:true`; router `n.up=!s.asked.includes(2)||m.up`).
What: after Q1 alone, call 1 shows a solid, plugged-in cable from the desktop to the router (frame `t-c1-q1`); call
3 shows a working Wi-Fi link though the Wi-Fi password failed (`t-c3-q1`); call 5 shows the router sending Wi-Fi arcs
and a live line to the internet before Q2, though it has no power (`t-c5-q1`). The map then reverses itself on Q4 or
Q2. A student reading the map as evidence learns the wrong thing first ("the cable is fine"). Better: until the
question that reveals it is asked, draw the part as unknown (the grey dotted "?" style the tool already uses before
Q1), never as working.

##### S4. Should fix (general): the internet cloud sits in the Kitchen and its line runs through devices
Where: Calls and House map, cloud node at (850, 80) inside the house outline. What: the router-to-internet line passes
through the Phone in House and in calls 1, 5 and 6 (frames `t-house`, `t-c1-q1`, `t-c5-q1`), and through Mr. Patel's
laptop in call 3 and Ana's in call 8 (`t-c3-q1`, `t-c8-solved`). Those devices look cabled to the internet, which is
exactly the thing Q1 asks about. Better: put the Internet cloud outside the house walls (beyond the top right corner,
on the lawn side) so its line crosses no room with a device. The 375 wide layout already does this (audit frame
`size-375x812 (iframe host).png`); the wide layouts don't.

##### S5. Should fix (general): call 8's Solved badge says "Allowed" on the guest laptop
Where: Calls, call 8 Solved (`updateMap`, solved badge text by kind). What: after the fix, Ana's guest laptop wears a
green "Allowed" badge (frame `t-c8-solved`), while the fix sentence says the Guest Wi-Fi keeps her away from home
devices on purpose. She is still not allowed; a family laptop prints. The kind line also says "The account just
isn't allowed" where the block is the guest network. Better: Ana's badge "File sent" (or keep "Guest") with the check
on the family laptop, and a kind line that fits both calls 7 and 8 ("Logging in worked. That account or network just
isn't allowed to do that, on purpose.").

##### S6. Should fix (general): after a nudge the Permission cause is cut off at 1366x768
Where: Calls, claim step at 1366x768. What: once a wrong claim or the need-clue reply puts the nudge on screen, the
cause board shrinks and the Permission group shows only its heading; "Not allowed" is below the board's edge (frames
`t-c5-wrong`, `t-c1-needclue`). The board scrolls, so the audit does not flag it, but a student retrying a call sees
two kinds and not the third. With two clues and no nudge it fits (`t-c1-claim`). Better: all seven cards in view in
every claim state at 1366x768 (tighter cards, or the nudge under Send fix in the space the clue strip leaves).

##### S7. Should fix (general): a resize during a wrong-claim ping locks the call
Where: Calls, connection calls 1, 2, 4, 5 (`runPing` adds a `fault` node; a `ResizeObserver` redraw rebuilds the map
without it). What: when the map box changes size during the wrong-claim ping, the engine throws (`px` in
`linkPoints`, an uncaught exception) and the call stays `busy`: Send fix and Back to questions both stay disabled and
the questions are hidden. Only another phone or a mode change gets out. Reproduced by changing the map's size 250 ms
into the ping (`dbg3.json`) and by asking a question and claiming at once through `__tool` (`dbg.json`). A teacher
dragging a projector window or a tablet turning sideways will hit it. Better: carry the fault node into the redraw,
or finish the ping before redrawing.

##### S8. Should fix (general): the teacher notes talk about the spec
Where: notes.md, Good to know. What: "Kitchen distance rounds to 256 design units, although the spec lists 255, with
two bars either way." A teacher has never seen a spec, and no distance is shown in the tool. Better: delete the
sentence; the line before it already says the thresholds are a Curio Class model.

##### P1. Polish (general): two key clues don't prove their cause
Where: spec Content, calls 1 and 2 keys. What: call 1 accepts Q1 "A cable. The blue one." as proof of "Cable
unplugged", and call 2 accepts Q3 "Mom's phone works." as proof of "Wi-Fi turned off". Each only rules something out.
The step says "Tap 1 or 2 clues that prove it". Call 1's nudge after both keys are asked also quotes Q1 instead of the
screen clue. Better: call 1 keys [4, 1] (nudge quotes the screen), and accept a rule-out clue only alongside the
direct one, or drop it from the keys. Spec change.

##### P2. Polish (general): the screen answer repeats the cause card's words
Where: Q4 answers, calls 1, 3, 7. What: "Network cable unplugged" matches "Cable unplugged", "Incorrect Wi-Fi password"
matches "Wrong Wi-Fi password", "You don't have permission" matches "Not allowed". Q4 is a key clue in 6 of 8 calls,
so "ask Q4, copy the words" is the fastest strategy for most of a shift. Real error screens do say these things, so
this is not wrong, but it turns three calls into word matching. Better: describe what the caller sees in their words
("A little computer with a red X and a cable picture", "It shows our Wi-Fi name and asks for the password again",
"A page with a lock on it: Teachers only"), so the student still has to name the cause.

##### P3. Polish (general): House results don't name the kind
Where: House, result chip (`houseTry` computes `h.result.kind` but `renderHouse` shows only the text). What: "Wrong
password" and "Not allowed: Parent account only" appear with no Connection, Logging in or Permission stamp, so House
never links back to the three kinds. Better: show the same stamp (plug, key, hand) in the result chip.

##### P4. Polish (general): House offers settings that make no sense for the printer and TV
Where: House panel with Printer or TV selected. What: both get Network and Account menus and every Try button. Setting
the printer to Guest makes every home device's Family printer try answer "Not allowed: guests can't reach home
devices" (all six, `house-result.json`, `printer-guest`), blaming a Home laptop for being a guest. The TV "Signed in"
to the Library site and the printer printing to itself read oddly. Better: for the printer and TV show only what they
have (power path, Network for the TV), hide Account, and word a printer-on-guest result as "Not allowed: the printer
is on the Guest Wi-Fi, away from home devices".

##### P5. Polish (general): call 5's wrong-claim X lands on the Wi-Fi link, not the dark router
Where: Calls, call 5 wrong claim (`runPing`, calls 1, 2, 4, 5 share the mid-link fault). What: the X sits halfway
between Aunt Rosa's laptop and the router (frame `t-c5-wrong`); the broken spot is the router itself. Better: for
call 5 stop the ping at the router with the X there.

##### P6. Polish (general): the need-clue reply shows two wordings at once
Where: Calls, claim step after right cause and weak clue. What: the nudge says "Right cause. Which clue proves it? Tap
a different clue." and the hint under it says "Right cause. Now tap a clue that proves it." (frame `t-c1-needclue`).
Better: one sentence in one place (and see S1, which changes the reply anyway).

##### N1. Nit (general): "design units" and "20 units per press"
Where: notes.md (House), tablet aria-label. What: an engine term a grade 4 student or teacher won't know. Better:
"one small step per press".

##### N2. Nit (general): Wi-Fi password call says "The path was fine"
Where: call 3 Solved kind line. What: Mr. Patel's laptop never joined the Wi-Fi, so the path to the internet was not
fine; the radio was in reach but the router refused it. Fine at grade 4, but "The Wi-Fi was in reach. The device had
to prove who it was with the right password." would fit both login calls.

#### Grade, language, guardrails, sensitivity

- Language reads right for grade 4: short questions, plain cause names, "Logging in" and "Permission" on screen, the
  technical words (authentication, authorization) only in the teacher notes. Callers' words are on screen only.
- Grade 4, students or teacher: not K-2, no teacher-led requirement. Not hard history, not health. Call time is
  labeled "not a clock" and is display only; no score, stars or win state.
- Rule 7: privacy is stated in both panels ("Nothing sent or saved. Only Motion is remembered on this device.").
- Rule 8: the standards here cover no sensitive topic; nothing missing in the notes.
- Rule 5: nothing cultural, Native or hard-history. No sensitivity agent needed.

#### Wave lessons (BUILD.md)

- No giveaways: missed (S1, and P2 as a lighter case).
- Honest numbers: bars say "about" on screen and Call time says what it counts. Pass.
- Standards: every code is done by the student, but SE-13's sort is thin (S2).
- Focus and layout, hint and voice, sizes, Motion off: see the Audit pilot rows and the Play and Craft lenses.

#### Audit pilot

`python scripts/audit_tool.py network-help-desk <scratch>/audit --port 9400 --profile <scratch>/profile`, full walk,
3 leads. Report: `S:/CurioClass-codex-scratch/lens-teaching/audit/audit.md`.

Leads I confirmed:
- shift-report, "Laptop" text under another box at 1280x720, 1366x768, 1920x1080: confirmed on
  `state-shift-report-1366x768.png`: the router-to-internet line runs through Ana's "Laptop" label. Same cause as S4.
- shift-report, "Phone" under a rect: confirmed in part. In call 8 the Kitchen phone sits under Ana's laptop tile,
  so it is not visible at all. Harmless for teaching; part of the S4 placement problem.

Leads that were wrong (or not a flaw):
- House, "Tablet ... nothing changed": the tablet is already the selected device on a fresh House page, so a tap
  changes nothing by design. Not a dead control.

Clean rows I cite instead of re-shooting: all 8 sizes (Questions and Make a claim in view, Done when 7), Motion off,
focus on load, no console errors in the walk, the five-click and quick-tap voice rows for the mode buttons, Read and
Q1 to Q6 (Done when 6, as far as the audit reaches; the Craft lens owns the full count table).

What it missed (found by this lens):
- S7, the uncaught exception and locked call when the map resizes during a wrong-claim ping: the walk never resizes
  mid-ping, so its "no console errors" row does not cover it.
- S6, the Permission cause cut off after a nudge at 1366x768: the cause board is a scroll panel, so the audit treats
  a hidden card as fine. A scroll panel that hides one of three answer groups is a teaching problem.
- S1, S2, S3, S5, P1, P2 (giveaways, the kind sort, the map drawing unknown parts as working, "Allowed" on the guest
  laptop, weak proof clues): outside what it can see, as its header says.
- S4 at the wide sizes: it saw one label crossed in one state, not that the internet line crosses devices on every
  call screen.

Verdict: useful as a floor. Its clean size, Motion off and voice rows saved me re-shooting; its three leads were
small. The findings that matter here all came from driving the calls and reading the map.

#### Builder claims checked afterwards (codex-report.md, read after the findings above)

- "PASS, no free sweep: all eight frozen right-cause/non-key claims rejected": the claims are refused, but the reply
  says "Right cause", which is the sweep (S1).
- "PASS, no giveaways ... Status appears only after relevant evidence": the map shows the cable plugged in (call 1),
  the Wi-Fi link working (call 3) and the router broadcasting (call 5) before the revealing question (S3).
- "Final drivers and stress report zero console errors": true for the runs it made; a resize during a wrong-claim
  ping throws (S7).
- "PASS, standards by solo action ... Authentication and authorization require different student actions": they
  need different cause cards, but the kind is printed on the board, so the student never makes the sort (S2).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: network-help-desk

Should fix 1, done: kind precedes cause; evidence precedes both judgments; all 56 weak-clue cause attempts agree; call 1 rejects either key alone and accepts Q1 plus Q4; four Q4 answers updated (functional.json).
Should fix 2, done: untested links stay grey dotted, even after Q1; unknown=true verified for calls 1 to 4; router-off links are down with no live link arcs (exit-data.json, last-house frames).
Should fix 3, done: cloud outside the walls, router-cloud via points clear devices and labels; inspected across review sizes.
Should fix 4, done: all three kinds and the selected kind's causes remain visible; 48 claim states across six sizes have no control/layout leads (layout-exit-log.txt).
Should fix 5, done: redraw retains the synthetic fault node; wrong-ping resizes on 1, 2, 4, 5 and mid-fix resizes on Connection, Logging in, Permission finish without exceptions (functional.json).
Should fix 6, done: Ana is Sent, with Ana's laptop and Family laptop labels; checks on family laptop/printer; revised kind explanations; final Sent badge is grey without an allowed check.
Should fix 7, done: broken links use grey dashes and break marks, Guest uses orange and its own pattern; Broken added to legend; skin contract checked up/down/update (extra.json).
Should fix 8, done: solved/next-call kit sequence protects the how line; exact Next call/phone wording; held-input log records next-call once (voice-polish.json).
Should fix 9, done: Next call/Shift report beside stamp, fixed eight-phone footer; both 680 and 375 Shift-ready/report checks have no leads and eight rows (extra.json).
Should fix 10, done: removed welcomeAfter; first-question log contains ask only, later Sound on brings the skipped welcome; two-mode welcomes remain once each.
Should fix 11, done: floors and named tablet spots share the drawing transform; shed drag lands inside its floor at every review size; fixed device icons have responsive room positions.
Should fix 12, done: moving back in range updates the House hint immediately; far and near hints recorded, Read checked (voice-polish.json).
Should fix 13, done: one-bar output is exactly about 1 bar of 3; real five-spot drags verified 3, 2, 2, 1, 0 (verify.json).
Should fix 14, done: removed spec discrepancy/builder wording from notes; notes and tablet label say one small step per press; actual arrow increment remains 20.
Should fix 15, done: first hint and ask line name Questions/Make a claim using the accepted Tap a question wording; voice bank matches runtime.
Polish 1, done: Solved shows Proved by evidence; Shift rows mark asked key questions, including both required Grandpa Lou clues.
Polish 2, done: House successes and failures carry a kind stamp and correct check/X; all four success chips and a Caps Lock failure asserted after correcting the glyph (glyph-final.json).
Polish 3, done: printer/TV have no Account control; wired devices have no Wi-Fi control; printer-on-Guest message is exact (extra.json).
Polish 4, done: call 5 failure at router; calls 3/8 marker offset beside router; stopped locations recorded and frames checked.
Polish 5, done: distinct code-drawn icons on compact maps, labels 14 px at laptops, compact room labels 12 px; reviewed actual-size frames.
Polish 6, done: at 375 non-caller devices stay faded; compact room/status placements separated; latest claim states clear at 680/375.
Polish 7, done: count chip follows tablet with obstacle-aware placement; actual uneven drags captured while pointer held at all five spots.
Polish 8, done: projector map notes/legend 17 px and call time 16 px; 1920 captures checked.
Polish 9, done: fixed room-label locations within each room; removed duplicate panel About line; House hint remains visible at 680.
Polish 10, done: badges outside tiles, compact side placements, invisible focus shapes excluded when unfocused; remaining phone audit rectangle lead assessed visually, not treated as a clean audit.
Polish 11, done: Phone/Laptop labels clear walls/cloud route; compact distinct icons omit redundant names; full-size map checked.
Settled glide approval, done: integrated approved engine change and removed tool observer/Net.place workaround.
Settled linkStyle approval, done: integrated and documented optional skin function; tool Guest styling uses it, with no post-update path painting.
Settled homeOnly decline, done: no new route option; guest printer uses documented skip predicate; handoff updated.
Settled non-findings, done: selected Tablet no-op retained; claim-from-ask remains a test API; Kitchen distance discrepancy kept out of student/teacher UI.
Settled family-table call, done: integrator Recipes and table left intact; only skin-options list changed.
Settled owner all-three decision, done: kind sort, clue-first judgment and revised Q4/two-clue call 1 applied together.
Engine glide, done: calm() read each tick; fixed waits unchanged; live-toggle fix/ping about 1506/1235 ms and 1504/1212 ms, respectively (extra.json).
Engine linkStyle, done: optional color/width/dash on up links in draw/update; down retains colors.down; omitted option unchanged; sibling send/bounce checks pass (extra.json, sibling.json).

#### Checked

- Evidence root: `C:/Users/Cory/AppData/Local/Temp/network-help-desk-polish/`, permitted temporary-space alternative because this session cannot write the S: scratch root; no test artifacts placed in the repo.
- Both tools bundled successfully; network-help-desk remains well below 2 MB; no recordings generated.
- Done when 1 to 4: all eight calls, exact revised content, weak/single-key rejection, kinds, fixes, successful return pings, effort and eight-row Shift report checked.
- Done when 5: all 24 router-off combinations fail; Caps Lock, Guest, Kid and printer-self special cases checked; five real drags give expected bars.
- Done when 6: 120 ms held clicks at 2 s pace; ask-first skips welcome, welcomes once, Next call once, Read current hint, restored near-range hint; no console errors.
- Done when 7: 680x425, 800x500, 760x900, 1366x768, 1920x1080 and 375 iframe claim states checked; full audit also includes 1000x625/1280x720.
- Done when 8: keyboard-only solved, resize interruption safe, same Motion waits, empty resource lists, no network request code; Curio Class naming retained.
- Audit states now include every kind, selected clues, weak clue, wrong kind, and an actual iframe resize immediately after Send fix with zero step gap.
- Sibling: first screens, real eight-piece Send, Motion on/off, and engine bounce at 1366/680; no errors, all eight pieces arrive; send 802 to 816 ms versus expected 800, bounce 2003 to 2223 ms versus expected 2000, including background scheduling.
- Initial audit: all 201 leads answered individually in [audit-dispositions.json](C:/Users/Cory/AppData/Local/Temp/network-help-desk-polish/audit-dispositions.json); fixes cover hidden hints, disabled-control naming, report actions and label/cable/badge collisions; welcome suppression and selected Tablet no-op follow integrator decisions.
- Latest claim sweep: 60 Calls captures, including 48 claim states, all mechanically clean; House follow-up covers on/off/shed at six sizes.
- Final phone House lead is a router group bounding rectangle intersecting the visible count chip in empty space; count text is fully readable and no tile is covered.
- [Final-source audit](C:/Users/Cory/AppData/Local/Temp/network-help-desk-polish/audit-polish-final/audit.md): completed after last change, exit 0; 17 leads individually answered: 14 intentional welcome skips, selected Tablet no-op, two phone router/count bounding rectangles. No console errors or focus losses; all 20 repeated/quick-tap checks clean.
- Frames: all 523 PNGs viewed, 406 saved plus 117 final-audit frames in 60 contact sheets; critical phone/680 Shift frames also opened full size. Manifests: frames-manifest.json and final-frames-manifest.json.
- Voice file equals the 21-line V.allLines list; event lines remain repeatable and how lines once per page.
- Closed every Chrome and server started: roots 20944, 44560 and recovery 17612 all exited; Browser.close used after Windows denied taskkill. Ports 8795/9990/9991 verified closed again, saved in recovery-cleanup.json; no repo host.html remains.
- No git operations; refine.md, lens files and codex-report.md unchanged.

#### Left open

- Written spec accepts any one key except call 1; call 2 therefore still accepts Q3 alone, although the proposal aside describes Q3 as rule-out evidence alongside Q4.
- Test environment only: scratch-derived standard-library WebSocket/CDP transport replaces a missing Python package; Chrome uses --disable-gpu and --in-process-gpu. No transport or flag workaround is shipped in the tool.
- The installed auditor lacks --host-port; a temporary in-memory wrapper changes its host binding to 8795. Repo audit/drive scripts are unchanged. No recording-backed audible classroom review.

#### Round 2

1. not done: six compact claim cards implemented; final held-input checks and frame review are running at all six requested sizes.
2. not done: obstacle-aware via routes and an interior call 4 phone position implemented; final map/solve checks are running.
3. not done: badges constrained beside their own tiles, clear of labels and walls; final map and House checks are running.
Audit: current main-checkout auditor, including choices-cut-short and line-crossing checks, is running from scratch against this worktree on 9991/8795; repository audit scripts are unchanged.
Evidence: `S:/CurioClass-codex-scratch/network-help-desk/r2/`; final audit output is `S:/CurioClass-codex-scratch/network-help-desk/audit-r2/`.
Left open: final audit, remaining frame review and owned Chrome/server cleanup are pending.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Network Help Desk handoff

`src.html` is a kit-starter tool: inline styles, Calls/House controls, SVG scene and content/state logic. `CALLS`, `QUESTIONS`, `CAUSES`, `KIND_TEXT` and `L` hold the teaching content. Caller words stay on screen only. The four revised Q4 answers follow the updated spec.

A claim selects `chosenKind`, then that kind's cause. Three stable kind buttons stay visible beside the chosen causes. `claim` judges evidence first, then kind, then cause. All weak evidence gets the same reply, no cause confirmation or added effort. Call 1 requires both Q4 and Q1. Other calls follow the written any-one-key rule. A third selected clue replaces the oldest. APIs are one-based; optional fourth claim argument supplies a kind for tests. `chooseKind` is exposed too.

The fixed footer keeps eight 44 px phones in view. Solved puts Next call or Shift report beside the stamp, with the fix and proof below in a scroller. Shift report actions stay at the top. Only clue/report bodies scroll; kind/cause buttons do not. Questions/evidence buttons keep stable nodes and focus. No focus is taken on load.

`makeGraph` and `syncGraph` hold connectivity in model coordinates. `renderGraph` projects it into real pixels. Room floors and named tablet spots use the same design-to-pixel transform. Some fixed device icons have responsive positions within their rooms to keep hit areas apart. Room labels have fixed positions per layout. The internet cloud is outside the walls; its route has via points clear of devices. Unknown links are grey dotted; broken links are grey with break marks; Guest is orange with a distinct dash pattern.

`runPing` uses Net.token/send and 300 ms hops, after the fixed 1500 ms fix. A wrong physical connection test inserts a hidden fault point. `state.fault` carries it into redraws during a resize; model synchronization skips drawing-only nodes/links. Call 5 stops at the router. Failed login/guest markers sit beside the router. Every call/mode change stops movers and clears retained tokens. An interrupted fix rolls back. Motion uses the engine's per-tick calm check, no tool-side token observer or Net.place workaround.

House uses Net.path/reach, with `skip: l => l.guest` for printer targets. It exposes only applicable device settings, has kind/pass-fail results and live tablet bar counts. Arrow keys still move 20 model units, described to students as one small step. Bounds remain 0..1000 by 0..600. Returning in range restores the House hint. Reset restores defaults.

Voice is Curio.voice with mode scope, immediate tool-owned hint and Read returning that exact hint. No welcomeAfter on this two-mode tool. A first action's own line skips the welcome; a later mode entry or Sound on can bring it. Solved plus the once-only Next call how line is a kit sequence, so another how line cannot replace it while waiting. Obsolete claim instructions stop when Send fix is pressed; a generic welcome is not included in that cancellation. Every V.allLines string is in voice/lines.json. No recordings.

#### Numbers check

Unrounded model distances from (300,330): Living room 108.1665, Kitchen 255.5386, Bedroom 361.3862, Back door 480.8326, Shed 648.4597. Rounded: 108, 256, 361, 481, 648. The spec lists Kitchen 255; its two bars are unchanged. Thresholds use unrounded distance, and the spec was not edited. Nothing on screen displays a distance.

#### Engine changes wanted

None. Both approved backward-compatible changes are implemented in kit/network.js: glide reads calm() every tick, and optional skin.linkStyle supplies up-link color/width/dash in draw and update. The skin option is documented. The proposed homeOnly path/reach option was declined; the documented guest skip recipe is used. Recipes and the family table were left intact.

Polish evidence is under the allowed temporary directory, `C:/Users/Cory/AppData/Local/Temp/network-help-desk-polish/`. It includes the full audit, follow-up page checks, real-input voice logs and internet-journey regression. See polish.md for exact results, open issues and browser/server cleanup. The previous codex-report.md is an unchanged historical build report.

<!-- end part -->

## Log

- 2026-11-25: CODEX-BRIEF.md folded in (last changed 2026-10-29)
- 2026-11-25: codex-report.md folded in (last changed 2026-10-29)
- 2026-11-25: refine.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-29)
- 2026-11-25: polish.md folded in (last changed 2026-10-29)
- 2026-11-25: handoff.md folded in (last changed 2026-10-29)
