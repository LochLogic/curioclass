# Craft lens: network-help-desk (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json, audit-states.json (no art: the spec says drawn in code).
Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py network-help-desk` (119 KB). Audit run first
(`scripts/audit_tool.py --port 9420`, 3 leads), then my own drive.py runs on port 9422. Evidence in
`S:/CurioClass-codex-scratch/lens-craft/` (audit/, frames/, voice/ with the shots files and outputs).

Counts: blockers 0, should fix 6, polish 5, nit 4.

## Contract

- One file, 119 KB, well under 2 MB. The only URLs in the bundle are the sources in an HTML comment and the SVG
  namespace; no fetch, XHR or import. Kit used for voice, motion, sound, chimes, icons, map and mover
  (`kit:curio`, `kit:network`).
- Console: 0 errors across the audit (every size, every state, every control walk) and my 30-odd drive shots.
- Motion off keeps time: a full call-1 solve took 2745 ms with Motion on and 2745 ms with Motion off (fix 1504 vs
  1506 ms, ping 1230 vs 1231 ms). Audit: nothing runs forever with Motion off.

## Access

- Keyboard: a keyboard-only solve of call 1 works (focus trace: modes, Motion, Sound, Read, q1 to q6, Make a claim,
  cause-1 to cause-9, evidence-1, evidence-4, Send fix; frames/kb-solved.png shows Solved with a visible purple ring
  on Next call). Escape leaves the claim step. Arrow keys move the focused tablet in House (20 units, focus kept).
- Targets: the audit finds no target under 44 px at any size. Selected causes and clues carry a check and "Selected",
  not color alone; badges carry a check, X or word.
- Sound off then on brings the skipped welcome once; Read speaks the hint with Sound off.

## Findings

### Should fix

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

### Polish

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

### Nit

1. Map labels under walls: the audit flags "Phone" and "Laptop" under a rect in the shift report at 1280, 1366 and
   1920; "Laptop" sits on the Living room wall line in every 1366 frame. Nudge the label or the node. general.
2. docs/families/network.md table row for network-help-desk lists "graph, draw, send ('ping'), down nodes and links,
   reach"; the tool also uses path, token, stop, addNode/addLink and icon. family:network.
3. For the Teaching lens: "Right cause. Now tap a clue that proves it." confirms the cause for free (no Call time),
   so trying causes with any non-key clue finds it at 2 min per miss. Spec-mandated; noting only. general.
4. `__tool.claim(n, cause, clues)` from the ask step leaves the panel on Questions while the hint says "Tap Back to
   questions" (frames/call5-wrong.png). Test API only, never reached by a student. general.

## Lines

- `__tool.allLines()` returns 19 lines; voice/lines.json has the same 19, word for word, same order. Every spec line
  (w-calls, ask, claim, need-clue, wrong, the three solved lines, next-call, shift, w-house, far) is present as
  written. The 7 extra lines are hint lines (ask-first, all-clues, shift-next, report, house, watch, retry); each names
  an enabled control at its moment.
- Spoken lines matched their screens in every frame I took, except the stale "far" hint (should fix 1) and the
  welcome after a first question (polish 1).

## Standard voice check (Sound on, Motion on, held clicks 0.12 s)

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

## Art and words

- No `art:` tokens and no prompts.json, as the spec says (all drawn in code, no people, callers as handset icons).
- No em or en dashes in src.html, notes.md, tool.draft.json or voice/lines.json. "Curio Class" only. Classroom-safe.
- Privacy is stated in both panels ("Pretend passwords. Nothing sent or saved. Only Motion is remembered on this
  device."), and that is true: the kit stores only `curio-motion`.

## Wave lessons (BUILD.md)

- Hint and voice: met except should fix 1 (hint not changed when the state changes back).
- Focus and layout: focus kept on rebuilds (audit "rebuilt, focus kept"), none on load, hint height reserved. Labels
  and badges: nit 1, and should fix 2 (tiles sitting on a link).
- Sizes: 44 px targets and an unclipped hint at every size, 375 included. Cause groups hidden at small sizes
  (should fix 3).
- No giveaways: see nit 3 and should fix 5. Honest numbers: bars say "about", Call time says what it counts.
- Family doc matches the engine: no (polish 5, nit 2).
- Motion off: clean.

## Builder claims checked afterwards

Read codex-report.md and handoff.md only after the findings above.
- "Latest targeted audit has zero overlap leads" and "all 470 PNGs were viewed": this audit has two label-under-rect
  leads (nit 1), and the frames show the Internet wire across the phone and Ana's laptop (should fix 2).
- "PASS, no free sweep": the "Right cause" reply still confirms a cause at no cost (nit 3); arguable, spec-driven.
- "PASS, family engine ... Net.path/reach use guest skip": true for the tool; the spec's claim that the engine
  ignores guest links is not, and the family doc was not updated (polish 5).

## Audit pilot

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
