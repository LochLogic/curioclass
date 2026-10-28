# Craft lens: city-skyline-studio (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/perspective.js and
docs/families/perspective.md. Bundled with `CURIO_DRAFT=1` (130,896 bytes). Driven with `scripts/drive.py` (held
clicks 0.12 s, Sound on, Motion on unless stated) at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
760x900 and 375x812 (iframe host served from my scratch folder). Frames and logs are in my scratch folder
(`lens-css-craft/out`, `outv`, `out3`, `out4`, `out5`).

Counts: blockers 0, should fix 5 (general 5, family 0), polish 4 (general 3, family 1), nits 6 (general 3, family 3).

## Contract

- One file, 128 KB, well under 2 MB. No network requests: `performance.getEntriesByType('resource')` is 0 at every
  size and mode.
- No console errors, warnings or exceptions in about 40 driven shots (every size, every mode, voice runs, ink,
  keyboard drawing, Find matches).
- Kit used, not re-implemented: `Curio.voice` for all narration (no copied queue), `kit:perspective` for every
  projection, VP, box, divide, snap, shade and hatch. One small duplicate, see nit N2.
- No art tokens; `art/prompts.json` is empty, which matches the spec ("drawn in code").

## Engine vs the spec's family description, and the family doc vs the code

Checked function by function. Every function the spec asks for exists with the asked-for shape: `camera`, `project`,
`ground` (null above the horizon), `vps` (off-page values kept, VP 3 with pitch), `box` (visible faces with screen
points, normal, depth and VP, in draw order), `divide` (projective), `snap`, `shade`. The doc's API block matches the
code's export list and each signature, return shape and default (`maxDeg = 6`, `y = 0`, `y0 = 0`, `near = 1`, shade
thresholds .25 and -.25, tops mid, bottoms dark). Recomputed in node from kit/perspective.js:
- W = 1200, 35 mm: f = 1166.7; turn 45 VPs -566.7 and 1766.7; turn 30 -73.6 and 2620.7; 85 mm at 45 apart 5666.7.
- FOV 73.7, 54.4, 39.6, 23.9 degrees for 24, 35, 50, 85 mm.
- Box edges meet their VPs (and VP 3) within 3e-12 px at pitch 0, 15 and -10; VP 3 at f / tan p (2488 px at 15,
  3781 px at -10); the horizon moves f tan p the other way; an eye-height point lands on the horizon.
- `ground` round-trips `project` at pitch 0, 15 and -10, and is null on the sky side.
- `divide` on a box face and on its screen quad alone (homography) agree to 6e-14 px.
Small doc gaps are nit N1.

## Access

- Keyboard: Tab order is header, the view, then the panel with Camera first. Arrow keys move the selected building
  (Build) and a cursor (Ink, Enter starts and ends a line). Sliders, the sun dial and every button work from the keys.
- Visible focus: the kit ring shows on buttons and sliders (frame c-tab); the view's ring is fine on the dark Build
  stage but weak in Ink (S3).
- 44 px targets: no visible control under 44 px at any size, including 375 wide.
- Color never the only signal: VPs carry labels, fills carry names, the match has a percent, the selected building
  has a dashed outline and the Selected list.
- Motion off: the view jumps straight to the new camera (eye 400 at once; with Motion on it was still at 158 m after
  50 ms). Sound off silences lines; Read still speaks (v6b). Read speaks the hint as recorded lines.

## Lines

`__tool.allLines()` equals `voice/lines.json` word for word (25 lines, same order). Every spoken call goes through a
key of `L` (the matched settings are keys in `L.matchedSet`); the local `say()` only writes the aria-live region.
No line over 200 characters, no unit abbreviations in spoken lines ("meters", "millimeter lens", "degrees").

## Standard voice check

Held clicks, gap 4.5 s for repeats, 0.2 s for the stale run. Headless browser voice (the cap, not `ended`, sometimes
ends a line, so real clips will run tighter).

| Line | Kind | Action (x5) | Expected | Spoken |
|---|---|---|---|---|
| welcomeBuild | welcome | first plain tap (stage, Tab key, lens button) | 1 | 1 (126 ms after the tap) |
| turnHow | how | Eye height stop x5 | 1 | 1 |
| guidesNext | how | Turn x5 | 1 | 1 |
| guidesHow | how | Guides x5 | 1 | 1 |
| buildNext | how | (chained after guidesHow) | 1 | 1 in v1c; lost in v4 and v6c (P2) |
| tiltHow | how | Tilt 0, 1, 0, 1, 0, 1 (three starts) | 1 | 1, then silent x2 |
| (no line) | | Lens x5 | 0 | 0 |
| offPage | event, once a session by spec | Turn, Lens | 1 | 1 (v1b, v1e, v3); dropped "newer" in v4 (P1) |
| welcomeInk | welcome | Ink tab | 1 | 1 |
| inkHatch | how | Hatch x5 | 1 | 1 (then dropped newer 1, silent 3) |
| inkFill | how | Fill x5 | 1 | 1 (silent 4) |
| inkErase | how | Erase x5 | 1 | 1 (silent 4) |
| inkMore | how | 5 keyboard lines | 1 | 1 |
| inkAsk | how | camera change with ink | 1 | 1 |
| welcomeFind | welcome | Find tab | 1 | 1 |
| matched | event | match reached x5 (35 mm, 50 mm, ...) | 5 | 5 |
| "Eye height 1.6 meters, turn 45 degrees, 35 millimeter lens." | event | same | 5 | 5 |
| findNext | how | after a match | 1 while still matched | 1 (v7); dropped stale x5 in v3, correctly, as each match was undone first |

1. Repeats: right (table).
2. Stale lines (v4, taps 0.2 s apart, then Ink, then Build): every line was cut or dropped when its step passed;
   guidesNext cut turnHow, guidesHow cut guidesNext, Ink dropped buildNext (hush), back in Build welcomeBuild was
   dropped as stale (eye already moved). Nothing played after its moment. Lines naming a control carry `needs`
   (`#turn`, `#ov-guides`, `#keepInk`, `#nextT2`, `#hor`, `#tilt`).
3. First-tap timing (one fresh page each): stage tap, welcome in 126 ms; Eye height stop, only turnHow; Ink tab, only
   welcomeInk; Read, the hint only; Sound, nothing, and Sound on again brought the welcome once; Tab key, the welcome;
   Sound off, Find, Sound on, welcomeFind once.
4. Read: Read during welcomeInk stopped it and spoke the hint; with Sound off Read still spoke; a mode change right
   after Read started welcomeFind at once; a line triggered during Read (guidesHow) waited for it.
5. Order: spoken lines followed the actions in every run.

Each spoken line was compared with the state at its time; the misses are S2 and P4.

## Findings

### Should fix

**S1. Find the Camera with Plan on shows the wrong city.** src.html:538 (`drawPlan` loops `S.city`). In Find the view,
the target and the match all use the Example city (`cityFor('find')`), but the Plan inset draws the student's own
Build city. Seen: frame c-plan-find, a Build city of one tower; Find shows nine buildings on the view and one square on
the Plan. A student using the Plan to reason about the hidden camera is misled. Draw the plan from `cityFor(S.mode)`.
*general*

**S2. welcomeInk (and the Line hint) can say the wrong thing.** src.html:744 and :766. The welcome's `valid` only
checks for an empty drawing, but pen and Snap are saved. Seen (c-welcomeink-fill): pen Fill and Snap off saved; on
entering Ink it spoke "Drag to draw. Your lines snap to the vanishing points." while the panel shows Fill (a tap, not
a drag) and Snap off. With Snap off the Line hint (also what Read says) still reads "It snaps to a vanishing
point...". Make the welcome valid only for pen Line with Snap on (or pick a line for the pen), and give the Line hint
a Snap-off version. *general*

**S3. The view's focus ring is close to invisible in Ink.** src.html:43. `.stage.kfocus::after` draws a 3 px
`--focus` (#8fe3ff) ring inset on the canvas; in Ink the canvas is cream and light gray, so the ring is about 1.2:1
against both sides. Seen: frame f-ink-focus (7 Tabs to the view in Ink). Fine on the dark Build stage (f-build-focus).
Use a dark ring (or a dark plus light double ring) in Ink. *general*

**S4. The privacy line shows only in Ink.** src.html:186. The city, camera and overlays are saved to localStorage from
Build and Find too (src.html:339-347), but "saved in this browser on this device only" sits in the Ink section, so a
student who stays in Build or Find never sees it (BASELINE rule 7). Add a short line where Build stores things (the
Buildings section) or under the panel in every mode. *general*

**S5. At 760x900 three camera controls are below the fold.** Stack layout (frame build-760x900): Eye height and Turn
show, but Lens, Horizon on page and Tilt need a scroll; STANDARDS asks main controls visible without scrolling at every
size and Done-when 7 names the camera sliders. handoff.md says all camera sliders were visible at 760x900; they were
not here (stage 502 px tall). Shorter stage in stack or a tighter Camera block. The Play lens may also report this.
*general*

### Polish

**P1. A how-to cutting in drops a queued event.** src.html:750 (`how()` passes `now`), with the kit's `say(now)`
dropping the whole queue. Seen (v4): offPage was queued, guidesHow cut in and offPage was logged "dropped newer". It
is a once-a-session line, so the student may not hear it until a VP comes back and leaves again. Better: when cutting
in, keep queued events (or requeue offPage when it is dropped for "newer"). *general*

**P2. The bridge to Ink is easy to lose.** src.html:981. buildNext ("...Then press Ink to draw over your city.") only
rides behind guidesHow, and `guidesSeen` stops it from coming back: lost in v4 (Ink pressed during guidesHow, "hush")
and v6c ("chain"). Same pattern for turnHow when inkAsk replaces it (c-ask, "dropped newer"). The hint still shows the
text. Better: queue buildNext again on the next Build action when it was never said. *general*

**P3. With Tilt, upright strokes can snap to "vertical" instead of VP 3.** kit/perspective.js:204 (`targets` always adds
a screen vertical), used at src.html:1178. In three-point the building edges run to VP 3, but a hand-drawn upright line
near the middle of the page is within 6 degrees of both and often lands on "vertical", which is the one-point/two-point
answer. The spec lists vertical among the targets, so this is a step up, not a bug: drop the screen vertical when the
camera is pitched (or let VP 3 win ties). *family:perspective*

**P4. guidesHow says "two dots" when there are three.** src.html:287 and :981. With Tilt already set, turning on
Guides speaks "Every edge runs to one of the two dots. That's two-point perspective." while VP 3 and its guides are on
screen. A Tilt-aware variant ("...the up-and-down edges run to the third") would match. *general*

### Nits

**N1. Family doc gaps.** docs/families/perspective.md: `camera()` also returns `focalLengths(px)`; `snap()` takes
`cam` but does not use it; `baseY` and `size` assume a level camera (they ignore pitch), which the doc should say.
*family:perspective*

**N2. One engine helper re-written in the tool.** src.html:1064-1072 (`hitOnFace`) repeats the engine's private
`fromCamDir` rotation. Export a `ray(cam, u, v)` from the engine so siblings don't copy it. *family:perspective*

**N3. Engine `vp` naming at turn 0.** At turn 0 the single one-point VP is labeled "VP L" and VP R shows "infinitely
far" (frame c-plan-find, Find's start camera). Correct per the doc, but a one-point label ("VP") would read better for
vanishing-point-studio when it moves on. *family:perspective*

**N4. Small panel type.** src.html:73 (turn tick "45" at 10 px), :108-109 (compact stop labels 10.5 and 10 px), :71
(notes 11 px). Readable but under the stage's own 11 px floor. *general*

**N5. Contrast comment is off.** src.html:29 says --brand-ink on --brand is 10.6:1 (spec says 11.0); it computes to
9.4:1. Still passes AA; fix the number. *general*

**N6. Small code tidy.** src.html:616-618 repeat the off-page comment twice (one stale); `#hatchSp` has no
`aria-valuetext` ("8 px" is read as "8"). *general*

## Words

No em dashes in src.html, notes.md, handoff.md, tool.draft.json, voice/lines.json, kit/perspective.js or the family
doc. "Curio Class" is never shortened in student-facing text (the only bare "Curio" are `Curio.*` calls). Language is
classroom-safe. Privacy is stated in Ink, see S4.
