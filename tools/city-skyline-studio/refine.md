OPEN (round 1 merged 2026-11-04, polish not started)
Counts: blockers 1 (general 0, family 1), should fix 10 (general 9, family 1), polish accepted 8

# Refine: city-skyline-studio (round 2026-11-04, after the Codex rework)

The 2026-10-28 Refine is kept in refine-2026-10-28.md and refine-2026-10-28/ (it ran before Codex reworked the tool).
Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: 114 leads. Measure-first run: the lenses
did not read codex-report.md or codex-review.md.

## Blocker

1. **Check my drawing passes flat lines, and Snap teaches them.** `misses()` and `lineEnd()` use `Persp.targets()`
   with its default `horizontal` target, so at Turn 30 three flat lines across the towers get "All 3 lines hit their
   vanishing points" and Snap labels a flat roof edge "horizontal". This is the classic two-point mistake passing the
   tool's one revise step (VA:Cr3). Drop the level target here (snap and check): at Turn 0 or 90 the far VP already
   comes back as a level direction. Keep the upright only at Tilt 0. (Teaching 1) family:perspective

## Should fix

2. **Check my drawing passes on any three upright lines anywhere, then asks "What did you change?"** when no line was
   ever red. Count only receding lines toward the three (or require at least one), and when `checkHadRed` is false ask
   "How did you aim each line at its vanishing point?" instead. (Play 2, Teaching 5) family:perspective
3. **Find the Camera can be solved from the per-setting percents** without reading the outline (target 1 in five
   checks). After a miss show only which settings are off (no percent) and the reading hint for the first one; the
   overall meter may move in coarse steps. (Teaching 2, Play 3) general
4. **The street-level targets (3 m and 2.5 m) ask for precision the picture can't show** at the 12% tolerance, and
   their hint names visible roofs that are not visible. Tie the eye tolerance to what shows (outline horizon within a
   few pixels), or raise them to heights that read clearly (for example 6 m and 4 m), and fix the hint. (Teaching 3)
   general
5. **"Tiers above your eye show their undersides" is false**: the stepped tiers' undersides are hidden; only the water
   tank shows one. Show the fact only when an uncovered bottom is drawn, name the tank, and fix the notes.md question.
   (Teaching 4) general
6. **At 1366x768 the Buildings section is below the fold** while addFirst, buildNext and composeGoal send the student
   there. Put Readouts after Buildings (or fold Readouts to a summary). (Play 1) general
7. **The Build hint is a fixed ladder**: done out of order, the voice moves on but the hint and Read stay on "Drag the
   eye height slider". Pick the rung by what is still undone. (Craft 1) general
8. **Check my drawing voice**: the first line drawn during a check speaks inkMore ("...press Check my drawing") while
   the button reads Stop checking, and checkFix is never spoken. No inkMore while checking; checkFix once, the first
   time a line turns red. (Craft 2) general
9. **A second missed Check camera is silent**. Add a short event line per miss ("Not yet. Two settings are off."),
   reading how-to kept to once. (Craft 3) general
10. **findLens names no action or control**: end it with "Pick a lens, then press Check camera." (Craft 4) general
11. **After Clear city the welcome plays over an empty stage** and addFirst is never spoken. The welcome needs a
    city; addFirst is spoken once when the city empties. (Craft 5) general

## Polish accepted

12. The facts tip sits at the bottom of the panel, out of view at 1366x768: show the current fact under the hint or
    as a stage chip. (Play polish 1) general
13. 760x900 and 375: the stacked hint keeps a four-line reserve, pushing Overlays below the fold; size it to its text
    when stacked. (Play polish 2) general
14. "Your city is off the page" overstates it with a building filling the stage, and offCity's "pick a wider lens"
    misleads when the Horizon is moved: say "Most of your city is off the page", and lead with "Press Auto" (or a
    wider lens while Auto is on). (Play polish 3, Craft 7) family:perspective
15. Find: after a match the big panel button becomes Next target (Start over on target 6). (Play polish 4) general
16. offPage is Build-only; in Find it fires with no student action and delays findCheck. (Play polish 5, Craft 6)
    family:perspective
17. Stage labels scale up with the stage above about 1400 px (13 to 15 px at 1920). (Play polish 6) general
18. Find at 375: VP chips sit on the amber outline; keep them at the stage edge or shorten them. (Craft 8)
    family:perspective
19. "Looking 48 degrees down" with parallel uprights: a readout note that the picture stays upright like a drafting
    view and Tilt shows the real lean, plus the same line in notes.md. (Teaching 7) family:perspective

## To the spec's open questions (not for the builder)

- Composition is one recipe line (`composeGoal`) in a module named "...and Composition": two or three short briefs
  to pick from, saved with the drawing? (Teaching 6)

## Nits (optional)

- Check tests direction, not place: a line in empty sky aimed at VP R passes (Teaching 8, family:perspective)
- Water tower sized in "Floors"; its 8 m width and depth sit below the sliders' 10 m minimum (Play nit 1)
- Empty city readout "Horizon crosses 0 of 0 buildings" (Play nit 2)
- The selection outline shows through nearer buildings (Play nit 3)
- Undo is off after a reload though the strokes are back (Play nit 4)
- Fill on empty sky does nothing, silently (Play nit 5)
- buildNext is cut after 0.2 s when a building is added as it starts (Play nit 6)
- The stage chip reads "Extend" while lines say "Extend outline edges" (Craft 9)
- Clear drawing stays enabled on an empty drawing (Craft 10)
- Scrambled indentation through most functions in src.html (Craft 11)

## Settled calls

- Rule 5 does not apply. Contract clean.
