# Craft lens: molecule-forge (Curiosity No. 12), round 1

Cold Craft lens, 2026-11-06. Judged against CODEX-CURIOSITY.md, VISION "Curiosities: the second shape", STANDARDS
and BASELINE. Bundle looked at: `tools/molecule-forge/molecule-forge.html` (1,145,511 bytes). My scripts, frames and
Chrome profile: `S:/CurioClass-codex-scratch/molecule-forge/craft/` (perf.py, perf3.py, voice1.py, kb.py, kb2.py,
cut2.py). Shared audit: `S:/CurioClass-codex-scratch/molecule-forge/audit-r1/`.

## What passed (checked, not findings)

- Contract: one file, 1.15 MB (under the 2 MB goal). Network log over a full session (forge, all crystals, grow, push,
  guide): one request, the file itself; the 40 pictures are inline. No console errors or exceptions in any of my runs
  or the audit's.
- Look rules: the well fills the screen at every size; no header, card, pills, score, goal, level or finish anywhere;
  field guide is a plain index with no counts or "found" marks. Maker's plate reads
  `Curio Class Curiosities · No. 12 · Molecule Forge` beside `Manual`, lower-left, at every size including 375.
  Motion, Sound and Read sit on their own power panel. Readouts are monospace with units (pm, degrees, atoms).
- Lesson creep search (score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done)
  over src.html, material.json, crystals.json: no hits.
- Keyboard: Tab reaches the tray, Enter on Hydrogen twice builds water (H2O, Water); T, 8, 6, G grows salt (392 ATOMS ·
  150 INSIDE); X cuts, P pushes; B opens the guide with focus on Close, Escape closes it and returns focus. Drawers trap
  Tab. Focus ring visible on tray and atom-focus buttons (`craft/kb-atomfocus.png`).
- Motion off: pegs stop wobbling but stay as pegs (not colour only), Show stands still and the 30-degree turn buttons
  remain; audit "Motion off: clean".
- Cut open works (`craft/salt-cut-compare.png`: 178 of 392 front atoms removed around the inspected ion).
- Art: 40 `art:` tokens (mf-0 to mf-39), 40 prompts.json entries, all `people: false`; contact sheet
  (`craft/art-sheet.png`) shows no people, faces or hands.
- Words: no em dashes in src.html, notes.md, lines.json, tool.draft.json or the JSON data; "Curio Class" never alone;
  classroom-safe; privacy stated ("Shelf stays on this device" in the footer, "Never leaves this device" on the shelf).
- 60 fps at 4x CPU slowdown (rAF frame intervals, Motion on, 1366x768): idle, 40 atoms relaxing, 40 atoms on Show,
  graphite 600 atoms, diamond 525, salt 392, silica 367, grow and push animations all hold about 60 fps. Two do not:
  see finding 1.

## Findings

1. **Copper and sodium metal drop to 35 fps at 4x slowdown while turning.** Where: `draw()`, src.html:835-982,
   Crystal mode. What: with Show on (or dragging), copper (561 atoms, 2,820 bonds) runs 34.5 fps, median frame 33.3 ms;
   sodium metal (559 atoms, 1,728 bonds) 35 fps. Both are 60 fps at 1x and 2x. Spec Done when 8 asks 600 crystal atoms
   at 60 fps at 4x; graphite (600) passes, the two metals do not. How: `craft/perf3.py`, rAF intervals over 4 s at
   CPU throttle 1, 2 and 4. Level: **should fix**. Tag: family:curiosity.

2. **The spec's spoken lines are missing: no molecule name on first close and no Crystal test result.** Where:
   src.html:328-329 (`L` holds only the hint), 453-465 (`edited()`), 610-634 (`push()`, `current()`). What: spec Voice says
   "only a molecule's name when it first closes this visit ('Water.') and a Crystal test's result line". Neither is ever
   queued; the only line is the first-run hint. So the moment the spec builds the first two minutes around (water bends
   and names itself) is silent, and a non-reader never hears what Push or Current found. How: `craft/voice1.py`, five
   held H taps 2.5 s apart (water then H2 close): log holds only the hint; Push, Current, Push, Current, Push on salt:
   log empty. Level: **should fix**. Tag: family:curiosity.

3. **The first-run hint is spoken after the student has already done it.** Where: src.html:1217-1222. What: the hint
   is queued on the first click anywhere, including a tap on a tray atom. A first tap on Hydrogen snaps H onto oxygen,
   hides the on-screen hint, then the voice says "Tap an atom to snap it on." The line no longer matches the screen
   (STANDARDS, Voice behavior). It should be skipped (unmarked) when the first tap added an atom, and spoken only when
   the first action was something else (a drag on the stage, Motion). How: `craft/voice1.py` first_H (log: spoken,
   2 atoms, hint hidden; frame `craft/v-firstH.png`), audit "One held click" rows 1 to 9 show the same. Level:
   **should fix**. Tag: family:curiosity.

4. **Spheres / Sticks button reports the wrong state to a screen reader.** Where: src.html:688. What: the button's
   label flips to the other mode ("Spheres" then "Sticks") while `aria-pressed` also flips, so with spheres showing a
   screen reader hears "Sticks, toggle button, pressed": Sticks is not on. Either keep one fixed label ("Spheres") with
   aria-pressed, or keep the flipping label and drop aria-pressed. How: code read, confirmed by the sync() logic and
   the 1366 frames (label "Sticks" while spheres show). Level: **should fix**. Tag: general.

5. **At the 680x425 preview the model is a 35 px dot in a corner.** Where: src.html:866-872 (short-window framing,
   `cx = w*.78`) and the max-height:690px layout. What: tray, title and selection text fill the left two thirds of the
   well, and the oxygen with its pegs is drawn about 35 px across at the lower right; water is about 70 px. The well is
   the largest thing (Done when 7 passes on the letter), but the subject is not: the site's tool-page preview shows a
   wooden box and some text. 800x500 is only a little better. How: audit `size-680x425.png`,
   `state-water-680x425.png`, `state-water-800x500.png`. Level: **should fix**. Tag: general.

6. **Read never says what to do, and what it says is not shaped for speech.** Where: src.html:745-747 (`readText`).
   What: (a) on the first screen, while the hint is showing, Read speaks "O. Oxygen. 2 SPOTS OPEN. O · Oxygen 2 spots ·
   0 filled · 2 lone pairs." and leaves out the hint, so a student who cannot read never hears "Tap an atom"
   (CODEX-CURIOSITY: the hint is spoken once, then when Read is pressed). (b) the text is the screen's glyphs: Unicode
   subscripts ("C₈H₁₀N₄O₂"), middle dots, "°", a doubled period ("Straight model.. Si"), "O · O · O · O", newlines. A
   speech engine may read subscripts as "subscript eight" or skip them. Build a spoken string instead ("C 8 H 10 N 4
   O 2, caffeine, all spots full. Selected: oxygen, 2 bonds, about 104 degrees."). How: `craft/voice1.py` reads (water,
   caffeine, pushed silica) and read_soundoff; audit row 12. Level: **should fix**. Tag: general.

7. **The controls are web buttons, not instrument controls.** Where: src.html:17-22, 199, 209-217. What: the look asks
   for toggle switches, faders, lit pads; the spec says "slide the bench switch to Crystal". The bench switch is a
   button showing the current mode with a small grey square; Spheres, Show and Cut open are the same flat buttons as
   Undo and Save. A real two-position slide switch for Forge / Crystal and for Sticks / Spheres, and a lit key for Show
   and Cut, would read as a modelling bench. How: every frame, e.g. audit `size-1366x768.png`. Level: **polish**.
   Tag: family:curiosity.

8. **Sound is thinner than the spec's palette.** Where: src.html:592, 623, 633. What: spec lists crack, bend ring,
   hold clink, slide swish, current hum or one spark. Push plays one sawtooth for salt and the same 360 Hz sine for
   copper, graphite, diamond, silicon and silica; Current is one 120 Hz or 900 Hz blip. Better: one distinct sound per
   outcome so the result is heard as well as read. How: code read. Level: **polish**. Tag: family:curiosity.

9. **Tab order puts every model atom before the bench controls.** Where: src.html:203 (`#atomkeys` inside the well,
   before `#controls`). What: from Hydrogen it took 18 Tab presses to reach Undo with 3 atoms in the well; with 40 atoms
   it is about 55. STANDARDS: panel controls before long lists of map items. How: `craft/kb.py`. Level: **polish**.
   Tag: general.

10. **Field guide at short heights shows only the picture.** Where: src.html:97, 104 (`.guide-body`, 4:3 image at full
   width). What: at 680x425 the guide body is all painting; the page name, fact and its sources (USGS, NASA links) are
   below a scroll with no sign there is more. At 1366x768 the source links are also just below the fold. Put name and
   fact above the picture, or cap the picture height in short windows. How: audit `state-guide-680x425.png`,
   `state-guide-1366x768.png`. Level: **polish**. Tag: general.

11. **No-grow message says "Two of these" for one atom.** Where: src.html:581. What: a single H, O, N, S or Cl on the
   seed plate gives "Two of these close up into a small molecule. Nothing left to grow." Words do not match the plate.
   How: code read (`crystalRule` returns nothing for one H; falls through to the last line). Level: **polish**.
   Tag: general.

12. **Singular/plural and case slips.** Where: src.html:670 ("1 spots"), 706 ("1 SPOTS OPEN"), 1047 (tray labels
   "Hydrogen · 1 spots", "Sodium · 0 spots"), 685 ("Bench switch: forge" lower case). How: `craft/v-firstH.png`
   (readout "1 SPOTS OPEN"), kb.py focus labels. Level: **nit**. Tag: general.

13. **The live region churns during growth.** Where: src.html:205 (`#readout aria-live="polite"`), 889 (counts rewritten
   every frame while growing) and 711 (every sync rewrites all four fields even when unchanged). A screen reader may
   re-announce the strip many times per Grow. Write only on change. How: code read. Level: **nit**. Tag: general.

14. **A tap at 40 atoms stalls about 100 ms at 4x.** Where: `match()`, src.html:417-426 (isomorphism tried against all
   72 entries on every edit). One melt plus add at 40 atoms took 101.5 ms at 4x slowdown. How: `craft/perf2.py`.
   Level: **nit**. Tag: family:curiosity.

15. **Canvas text names Consolas only.** Where: src.html:962, 966 (`'11px Consolas'`, `'15px Consolas'`). Chromebooks
   have no Consolas, so "SEED PLATE" and the battery's "+ −" fall back to the default sans. Add `, monospace`. Level:
   **nit**. Tag: general.

16. **At 760x900 the top of a grown crystal draws under the bench buttons.** How: audit
   `state-salt-fracture-760x900.png` (the upper half's corner sits behind "Crystal" / "Field guide"). Level: **nit**.
   Tag: general.

17. **For the integrator, not judged here:** the Manual's OpenStax links go to a personal college mirror
   (ic.arc.losrios.edu/~paynem) instead of openstax.org, and its note that the current OpenStax site lists CC BY-NC-SA
   should be checked (Teaching lens territory). The illustrations credit names a company and links openai.com
   (src.html:1241); BASELINE rule 15 says public copy names no companies, so decide whether a credit line counts.
   prompts.json entries are stubs ("Hydrogen: sun, real object or place") that do not record what was drawn. Level:
   **nit**. Tag: general.

Nothing cultural, Native or hard-history here; no sensitivity review needed from this lens.

## Standard voice check

Sound on, Motion on, held clicks (0.12 s), 1366x768, fresh page per run (`craft/voice1.py`).

| line | kind | expected | spoken |
|---|---|---|---|
| "Tap an atom to snap it on." | how | once, and only while it still fits | once in five taps; but after an atom tap it plays when the atom has already snapped on (finding 3) |
| molecule name on first close ("Water.", "Hydrogen.") | event (spec) | once per molecule per visit | 0 of 2 (finding 2) |
| Push result, salt, x3 | event (spec) | 3 | 0 |
| Current result, salt, x2 | event (spec) | 2 | 0 |
| bond step x5 (C-C) | none | 0 | 0 |
| Read, Sound off | read | speaks the readout | spoke it (finding 6 on content) |

First-tap timing: stage tap gives the hint; tray atom tap gives the hint late and stale; key "1" first gives nothing
(fine); Sound first nothing; Read first the readout only (audit). Stale lines and order: with one line there is
nothing to go stale across mode switches; mode switch and drawers call `V.hush()`. `allLines()` and
voice/lines.json agree word for word on the one line.

## Audit pilot

- Leads confirmed: guide "choices cut short by a scroll panel" (USGS, NASA links below the fold), real but minor
  (finding 10). The held-click table's spoken column also shows finding 3, though the audit did not flag it.
- Leads wrong: all of the roughly 200 "overlap: #stage / ..." rows (the stage is the full-screen well; every control
  sits on it by design); "keep region hidden" for #readout, #controls, #tray in the guide and manual states (modal
  drawers make main inert and cover it on purpose); "hint out of view" in every state (the hint hides after the first
  action, as the Curiosity brief asks); guide "button.close / h2 overlap" (the h2 box has 80 px right padding, no text
  collides).
- What it missed: missing name and result lines (2), metals at 35 fps under 4x slowdown (1), inverted aria-pressed
  on Spheres/Sticks (4), the 35 px model in the 680x425 preview (5), Read content and speech shape (6), Tab order
  through 40 atom stops (9), the one-atom no-grow wording (11).
