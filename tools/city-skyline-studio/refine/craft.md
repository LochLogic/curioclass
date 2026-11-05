# Craft lens: city-skyline-studio (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json and the CURIO_DRAFT=1 bundle. Driven with
`scripts/drive.py` (held clicks 0.12 s, Sound on, Motion on, real keys) in three runs of 37 fresh pages at 1366x768.
Frames and logs: the craft scratch folder (`refine/city-skyline-studio/craft/out-rep`, `out-run2`, `out-run3`, with
rep.log, run2.log, run3.log). Shared audit: `audit-r1/audit.md` and its frames.

Counts: blockers 0, should fix 5, polish 3, nit 3.

## Contract and access (clean)

- One file, 1,009,411 bytes (under the 2 MB goal). No network requests (Resource Timing empty after all three modes;
  no http(s) reference in the page). No console errors, warnings or exceptions in any of the 37 pages.
- Kit used: `Curio.voice`, `Curio.init`, theme-912, `kit:perspective`; nothing re-implemented that I could see.
- Keyboard: Tab reaches the mode buttons, header, the stage (visible cyan focus ring, out-run3/focus-tab2.png) and the
  panel; arrows step sliders, Page Up/Down jump eye stops, arrows move a building, Enter draws in Ink. Targets: the
  audit's 44 px check is clean at every size and my frames agree. Color is never the only signal (red misses are also
  dashed and counted; VPs are labeled; pressed buttons fill). Motion off is clean (audit). Sound off, Read still
  speaks (run2 read-soundoff).
- `voice/lines.json` matches `__tool.allLines()` word for word: 40 and 40, none missing either way.
- Art: one asset, `art:dusk-sky`, has its prompts.json entry, no people (none needed). Words: no em or en dashes on
  screen in any mode, in src.html, notes.md or lines.json; "Curio Class" only, never "Curio" alone; classroom-safe;
  privacy stated in every mode ("saved in this browser on this device only", the reflection note included).

## Findings

1. **should fix, general.** src.html `hintNow()` (Build branch, about line 1500) against the spoken lines. The Build
   hint is a fixed ladder (eye, then turn, then guides), so when a student does the steps in another order the voice
   moves on but the hint and Read stay on the first rung. Seen: run1 rep-turn (first action Turn: spoken "Turn on
   Guides under Overlays...", hint and Read still "Drag the eye height slider..."); run2 read-during (Guides first:
   guidesHow then buildNext spoken, Read then says "Drag the eye height slider..."); run3 tilt-how (tiltHow spoken, hint
   unchanged). STANDARDS: the hint changes when the state changes, and the spoken line matches it. Better: pick the
   hint rung by what is still undone and let it follow the line a step just queued.
2. **should fix, general.** Ink with Check my drawing on (`commit()` line 2046 and the check branch of `hintNow`). The
   first line drawn during a check speaks inkMore, "Keep drawing, or try Hatch and Fill. Then press Check my
   drawing...", while the button already reads "Stop checking" and the hint shows checkHow or checkFix. And checkFix
   ("Fix the dashed red lines...") is never queued anywhere, so a student with red lines hears nothing about fixing
   them. Seen: run1 rep-check (five missing lines: inkMore 1, checkFix 0), run3 reflect. Better: no inkMore while
   `S.check`; checkFix as a how-to the first time a line turns red.
3. **should fix, general.** Find, `checkCamera()` miss branch. A missed Check camera is a result, but only its reading
   hint is voiced, as a how-to: the first miss speaks findEye and every later miss on the same setting is silent (no
   line, no tone), though the panel shows a fresh "Not yet: N settings are off" each time. Seen: run1 rep-findmiss (5
   presses: findEye spoken 1, then `silent heard` 4). A student pressing Check camera again hears nothing happen.
   Better: a short event line per miss ("Not yet. Two settings are off.") with the reading how-to kept to once.
4. **should fix, general.** `L.findLens` "Read the lens: the farther apart the outline's vanishing points, the longer
   the lens. Close together means a wide lens." is the only Find reading line that names no action or control (the
   others say Press Extend outline edges, turn until, Tilt until). Cory's rule: every waiting moment names the next
   action and the control. Better: end with "Pick a lens, then press Check camera."
5. **should fix, general.** Build after Clear city (run3 clearcity). With Clear city as the first tap, the welcome then
   played "Drag the eye height slider and watch the horizon stay with your eyes." over an empty stage while the hint
   showed addFirst ("Your city is empty. Tap Tower..."); addFirst itself is never spoken. The welcome's `valid` only
   checks `!S.eyeMoved`. Better: the welcome needs a city, and addFirst is spoken once when the city empties.
6. **polish, general.** offPage on entering Find (run2 ft-find): "One vanishing point just went off the page" plays
   five seconds after the Find welcome with no student action; the target's camera simply starts that way. Better: in
   Find, arm offPage only after the first camera change.
7. **polish, general.** offCity line and hint, "Move Horizon on page, or pick a wider lens." (out-run3/offcity.png,
   Horizon at 600% above). A wider lens does not bring that horizon back, and the one-tap fix, Auto, is not named.
   Better: "Your city is off the page. Press Auto, or move Horizon on page."
8. **polish, family:perspective.** Find at 375 wide (audit state-mode-find-the-camera-375x812.png): the "VP (off the
   page)", "VP R: infinitely far" and horizon chips sit on top of the small amber outline, the thing the student has to
   read. Better: on narrow stages keep VP chips at the stage edge or shorten them so the outline stays clear.
9. **nit, general.** The stage chip button reads "Extend" while the hint and lines say "Press Extend outline edges"
   (audit state-find-missed-check-1366x768.png); only its aria-label has the full name. "Extend edges" would match.
10. **nit, general.** Clear drawing stays enabled on an empty drawing and does nothing (audit "nothing changed"),
    while Undo and Redo show disabled. Could match them.
11. **nit, general.** src.html has scrambled indentation through most functions (statements after `;` pushed to new
    deeply indented lines, for example `checkCamera()` and `syncCam()`), which makes the source hard to review.

## Standard voice check

Repeats (run1, five actions, gaps longer than the lines):

| line | kind | expected | spoken |
|---|---|---|---|
| turnHow (5 eye stops) | how | 1 | 1 |
| offPage (same run, at 150 m) | event, once per session by spec | 1 | 1 |
| guidesNext (5 Turn key steps) | how | 1 | 1 |
| guidesHow (Guides on and off x5) | how | 1 | 1 (buildNext follows once, as a sequence) |
| welcomeBuild (5 lens taps, no own line) | welcome | 1 | 1 |
| inkMore (5 lines, Snap on) | how | 1 | 1 |
| checkFix (5 missing lines, check on) | how | 1 | **0** (inkMore spoken instead; finding 2) |
| findEye (5 missed Check camera) | how | 1 | 1 |
| miss result (same 5) | event | 5 | **0** (finding 3) |
| matched + settings (5 matched checks) | event | 5 + 5 | 5 + 5 |
| findNext (same) | how | 1 | 1 (then `silent heard` 4) |

Stale lines (run2 stale-build, stale-find, stale-ink: taps 0.35 s apart, then a mode switch): no line played after its
moment. Superseded lines were dropped (`newer`, `hush`, `stale`); welcomeBuild was dropped `stale` once the eye had
moved; nothing named a hidden control.

First-tap timing (fresh page each): stage tap, welcome at 150 ms; a stop, only turnHow (the welcome is later dropped as
stale because the eye moved, which fits the state); 85 mm, only offPage, then Sound off and on brought welcomeBuild
once; Guides, only guidesHow, then Ink brought welcomeInk; Ink and Find buttons, their welcome within 150 ms; Read
first, the hint only; Sound first, nothing, then Sound on brought the welcome once; a key (eye slider ArrowRight),
turnHow only. Nothing spoke before a tap. Clear city first: finding 5.

Read: Read during guidesHow cut it and spoke the hint (the queued buildNext dropped `hush`, unmarked); Read with Sound
off spoke; a mode change 0.7 s after Read started welcomeInk 140 ms later; an event during Read (offPage) waited for Read
to end. What Read says is wrong when the hint is stale (finding 1).

Order (run2 order-build, 1.5 s apart): turnHow, guidesHow, buildNext in action order; no older line after a newer one.

## Audit pilot

Confirmed on my frames or runs:
- Held-click table: a first tap on a stop, 50/85 mm or Guides skips the welcome. Confirmed, but right for those taps
  (each has its own line); the welcome comes back on Sound off and on or the next mode entry while it still fits. Not a
  finding by itself.
- "#clearInk nothing changed" on an empty drawing: confirmed, nit 10.
- 760x900 and 375: Overlays, Buildings, Show render, Save, Check my drawing below the fold. Confirmed, but the camera
  sliders, pens, values and Undo/Redo (the every-few-seconds controls) are on screen, as STANDARDS asks. Not reported
  by Craft.

Wrong leads:
- "#cv / #hint overlap" and "#hint keep region covered" at 680x425 and 800x500: in compact layout the hint band sits
  over the top of the stage on purpose and is fully readable (size-680x425.png).
- "#cv / #fchipT, #fchipM, #checkCam2, #extendQuick overlap": the Find chip is a deliberate stage overlay on the sky,
  clear of the outline at 1366x768 and 680x425.
- "#cv nothing changed" in Ink and Find: a plain tap draws nothing in Line mode, and Find's stage is not a control.
- "choices cut short by a scroll panel" naming Check camera at 680x425 and 800x500: Check camera is also on the stage
  chip, on screen.

Missed by the audit:
- Hint and Read stuck on the first Build rung when steps are done out of order (finding 1).
- Check-mode voice: inkMore in the wrong state, checkFix never spoken (finding 2).
- A repeated missed Check camera is silent (finding 3); the five-click rows did not include Check camera.
- The welcome playing over an emptied city (finding 5), and the wording items (4, 6, 7, 9).
