# Prototype Lab

## One idea
Design a 3D-printed phone stand to a client's brief, then print and test each version on a lab bench (a push gauge that tips it, a dial that measures how much it bends, a slicer that prices it), so every change you make lands as a new row in a lab notebook, and the requirement you keep failing tells you which variable to change next, one at a time.

## Not like
- collision-lab, motion-graph-match (science, built labs): measure physics to learn a law. Here the physics is a means: you meet a brief with trade-offs (stable vs. cheap vs. fast to print).
- startup-booth (this group): selling a product at a price. Here making the product good enough to sell.
- path-planner, hospital-shift (this group): careers you read about. Here the work an engineering technician does.
- compound-interest-head-start (this group): changing a rate and watching a curve. Here several variables, several requirements, and a budget of printer time that makes each test cost something.

## Who and how
- Grade 9-12, career and technical education, module "Engineering and Design Process".
- Topic line: the engineering design process: prototype, test and improve
- Driver: students on laptops, alone or in pairs (one designs, one keeps the notebook). Teacher can project Notebook to compare class designs. 30 to 45 minutes per brief.
- Standards: CTE.Career Clusters.

## Screens and modes
Header: title, topic line, modes (`.seg`): `Design` (default), `Notebook`, `Brief`; then `Read`, `Motion`, `Sound`.

**Brief.** Focus: the client card, centered. The client card: the client's painted picture (Art), who, why, and a requirement table (Content). Three briefs as tabs; the chosen brief stays pinned as a strip under the header in every mode, each requirement with its target. `Start with the sample design` loads version 1.

**Design.** Focus: the side view of the stand with the phone on it, the largest thing on the stage (at least 55% of the stage area at 1366x768); the results card opens beside it, never over the stand at wide sizes.
1. Stage: a side view of the stand drawn in code on a blueprint grid (mm ticks), with the painted phone (Art, a cutout rotated to the lean angle) resting on it. Dimension arrows label base depth and lean angle; the wall shows its thickness to scale (zoomed inset). The phone's balance point is a small target mark with a dotted line straight down to the base, so you can see where it lands.
2. Panel: four controls, each a stepper with its unit, and the change since the last printed version in a small "was" tag:
   - Base depth: 50 to 120 mm, step 10.
   - Lean angle (from the desk): 50 to 75 degrees, step 5.
   - Wall thickness: 2, 3 or 4 mm (`.seg`).
   - Infill: 15%, 30% or 60% (`.seg`).
   - Live slicer estimate under the controls: mass, filament cost, print time (always shown, since a real slicer gives them before printing).
3. `Print and test`: uses printer time from the lab budget (8 hours per brief; a bar shows what is left). The painted printer (Art) slides in over the stand and the stand rises in layers inside its build area, drawn in code (2 seconds; instant with Motion off); then the bench runs three tests in order on the blueprint:
   - Tip test: the painted push gauge (Art) pushes the top of the phone backward with a slowly rising force until the stand tips. Three trials, each recorded to 0.001 N, then the average. The stand rocks back and settles (or falls) in the stage.
   - Flex test: the painted dial gauge (Art, its needle drawn in code) on the back support reads the bend under the phone plus a 0.3 N tap, in mm to 0.01.
   - Angle check: a protractor drawn in code reads the lean angle.
   The whole run lasts about 5 seconds. Every control stays live: a tap on any control or on `Show results now` ends the run at once and shows the results card; a changed control marks the card "results for V3, not your current design".
4. Results card: each requirement with the measured value, target, and pass or miss in words plus a check or cross icon. A version that passes every requirement gets "Meets the brief" and a `Mark as final` button. No other celebration.
5. `Sketch only` (beside Print and test): shows the slicer estimate and the balance point without running tests or using printer time, so students can reason first.
6. Out of printer time: Print and test is disabled with "Printer time used up for this brief. Use Notebook to pick your best version, or ask your teacher to reset." Teacher setting `No time limit` (under a small gear) removes the budget.

**Notebook.** Focus: the table of versions, with the chart under it. A table, one row per printed version: V#, the four variables (changed cells highlighted), the three trials and average tip force, flex, angle, mass, cost, time, and requirement ticks. Above it: a note on each row that changed more than one variable ("2 changes: you can't tell which one helped"). Under it: a chart where you pick the x (any variable or version number) and y (any result), with the requirement drawn as a line. `Copy notebook` copies the table as tab-separated text to this device's clipboard (paste into a spreadsheet). `Conclusion` box: three sentence starters to finish ("The change that helped stability most was...", "The trade-off I accepted was...", "If I had more printer time I would test..."), kept in memory only.

## Content
Phone: 200 g (1.96 N), 150 mm tall, rests on a 10 mm lip whose front is 15 mm behind the front edge of the base. Stand: 70 mm wide; back support 100 mm long. PLA filament: density 1.24 g/cm3, stiffness about 3,500 MPa, $20 a kilogram ($0.02 a gram), and about 4 minutes of printing per gram on a school printer. Values labeled "typical, as of 2026" in the Brief footer.

**Briefs** (clients made up):
- A. Video-call desk stand, for Mr. Delgado's online tutoring. Lean angle 60 to 70 degrees; average tip force at least 0.30 N (a firm screen tap); flex at most 2.0 mm; filament cost at most $0.60; print time at most 120 minutes.
- B. Bedside alarm stand, for a sleep study volunteer. Lean angle 50 to 60 degrees; tip at least 0.30 N; flex at most 2.0 mm; cost at most $0.50; print at most 100 minutes.
- C. Class set of 30, for a middle school library. Lean angle 60 to 70 degrees; tip at least 0.30 N; flex at most 2.0 mm; cost at most $0.45; print at most 90 minutes (so a full set prints in about a school week of overnights).

Sample design (version 1 for every brief): base 60 mm, angle 60 degrees, wall 2 mm, infill 15%.

## Interactions in detail
Model (all lengths in mm, forces in N, g = 9.81):
- Fill factor f = 0.4 + 0.6 x infill (outer walls are solid). Mass of each part = 0.00124 g/mm3 x 70 x t x length x f, with lengths base D, support 100, lip 10. Total mass shown to 0.1 g; cost = r2(mass x 0.02) and time = round(mass x 4) from the unrounded mass.
- Phone balance point x_p = 15 + 75 x cos(angle) from the front edge. Support's balance point x_s = 15 + 50 x cos(angle); base D/2; lip 15.
- Tip force F = [1.962 x (D - x_p) + weight_base x D/2 + weight_support x (D - x_s) + weight_lip x (D - 15)] / (150 x sin(angle) + t), part weights in N. If F <= 0 the stand tips on its own: the result reads "Tips over with no push" and the stage shows it falling back.
- Trials: F x 0.97, F x 1.01, F x 1.02 (always in that order), each to 0.001 N; the average equals F. Pass uses the average, and the notebook flags any single trial under the target ("one trial under 0.30: small margin").
- Flex = P x 100^3 / (3 x 3500 x f x I), with P = 1.962 x cos(angle) + 0.3 and I = 70 x t^3 / 12, to 0.01 mm.
- Angle check reads the set angle (no error).
- Nothing is random. Same design, same numbers, on every machine.
- Notebook and the current brief can be kept in localStorage (`Keep my notebook`); `Clear` deletes it. Conclusion text is not stored.
- Keyboard: steppers take arrow keys; Print and test is Enter from any control. The tip animation has a text alternative ("Pushed to 0.138 N, then tipped back.").
- Sizes: below 760 px the stage sits above the panel; at 680x425 the stage keeps the side view and the results card overlays its lower third; at 375 the controls stack and the notebook table scrolls inside its own box with the version column fixed. The phone and gauges are drawn to the blueprint's mm scale at every size.

**Worked checks:**
- Sample (60 mm, 60 degrees, 2 mm, 15%): mass 14.5 g, $0.29, 58 min; tip trials 0.134, 0.140, 0.141, average 0.138 N (miss); flex 5.34 mm (miss); angle 60 (pass for A and B).
- Wall 3 mm only (60, 60, 3, 15%): tip 0.151 (miss), flex 1.58 (pass), $0.43, 87 min. Infill 60% instead (60, 60, 2, 60%): flex 3.44 (miss), $0.45, 90 min: thickness helps flex far more than infill.
- Base 80 mm too (80, 60, 3, 15%): tip trials 0.466, 0.485, 0.490, average 0.480 (pass), flex 1.58, $0.48, 97 min: meets Brief A and Brief B.
- Brief C's only answer: 60 mm, 70 degrees, 3 mm, 15%: tip trials 0.298, 0.311, 0.314, average 0.308 (pass, with the small-margin flag), flex 1.20, $0.43, 87 min.
- Too much (120, 60, 4, 60%): tip 1.303, flex 0.43, but $1.21 and 243 minutes: fails cost and time.
- Base 50 mm at 50 degrees, 2 mm: the phone's balance point (63.2 mm) is past the base: "Tips over with no push".
- Brief A has 27 passing designs, Brief B 4, Brief C 1, all needing 3 mm walls or (Brief A only) a 4 mm wall at 60 mm and 70 degrees.

## Look
- Own `:root` (a blueprint): `--paper #0b1a30`, `--panel #10233f`, `--ink #e8f0ff`, `--muted #9fb6d9`, `--line #24406a`, grid `#7fd6ff` at low opacity. Accent `--brand #ff9f43` (safety orange: Print and test, the phone's balance mark, the active control), `--brand-ink #2a1400`.
- Pass `#6be3a1` with a check and the word "pass"; miss `#ff6b6b` with a cross and "miss".
- The painted phone, printer and gauges sit on the blueprint with a soft dark shadow so they read as real objects over a drawing.
- Contrast: accent on panel 7.71:1, on paper 8.54:1; brand-ink on accent 8.59:1; ink on panel 13.75:1; muted on panel 7.62:1; pass 9.84:1; miss 5.67:1; grid cyan 9.72:1.
- Differs from this batch's dark tools (spring green, jade, periwinkle, violet, apricot) and its light ones (journal, map, office) and from collision-lab's look. Its orange is deeper and more saturated than paycheck-decoder's pale apricot, and the blueprint navy sets it apart.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. Shared style line: "clean realistic product photo style, soft studio light". Webp.
- pl-phone: "a plain black smartphone seen from the side edge-on, with a slim profile and side buttons, plain white background, (style)"; 9:16; cutout yes; people no; rests on the stand, rotated to the lean angle, drawn 150 mm tall at the blueprint's scale.
- pl-printer: "a compact desktop 3D printer with an open frame, an empty glass build plate and a spool of orange filament on top, front view, plain white background, (style)"; 1:1; cutout yes; people no; slides in over the stand during the print; the rising layers are drawn in code inside its build area (the builder marks the plate rectangle).
- pl-push: "a handheld digital push force gauge with a flat metal tip and a blank gray display, side view, plain white background, (style)"; 16:9; cutout yes; people no; moves in from the back to push the phone's top; the force reading is drawn in code on its display.
- pl-dial: "a round dial indicator gauge on a small magnetic stand with a blank white face and a thin plunger, front view, plain white background, (style)"; 3:4; cutout yes; people no; touches the back support; the needle and numbers are drawn in code over the blank face.
- Brief pictures (4:3; cutout no; people no; on the Brief card, 480 px wide), shared style "warm realistic painting, soft room light":
  - pl-brief-a: "a tidy desk with an open laptop showing a plain blue screen, a webcam and a notebook, (style)".
  - pl-brief-b: "a bedside table at night with a lamp, a glass of water and an empty phone stand, (style)".
  - pl-brief-c: "a bright middle school library with tables and shelves of books with plain spines, (style)".
- 7 images, none with people. Drawn in code: the stand (it changes shape with every control), blueprint grid, dimension arrows, balance mark, layers, protractor, gauge readings, results card, notebook and chart.

## Voice
Bank voice `science-narrator` (Charon), "Say in a clear, informative way, like a nature documentary narrator": a lab supervisor narrating the bench. Not used by another tool `neighbors.py` lists or by this batch (its other users are director-s-chair, 9-12 arts, and model-mechanic, 6-8 CS). `Curio.voice`, `scope: () => state.mode`. Numbers and the notebook are on screen; lines are short.
- welcomeBrief (how; on entering Brief; stale when the sample is loaded or a brief tab is tapped): "Read the brief, then tap Start with the sample design."
- designHow (how; first visit to Design; stale when Print and test or Sketch only is tapped): "Change a control, then tap Print and test. Sketch only is free."
- oneThing (how; the first time two variables change before a print; stale on the next print): "Two changes at once. You won't know which one helped."
- tipResult (event; after each tip test; stale on the next print or control change): "Tipped at (average) newtons. The brief asks for 0.30."
- tippedAlone (event; stale on the next print or control change): "It tipped with no push. Look where the balance point lands."
- flexResult (event; only on a miss; stale on the next print or control change): "It bent (flex) millimeters. The brief allows 2."
- meetsBrief (event; stale on the next print): "Every requirement met. Tap Mark as final, or keep improving."
- outOfTime (event; when the budget runs out; stale when the mode changes): "That's the printer time for this brief. Tap Notebook to pick your best version."
- welcomeNotebook (how; on entering Notebook; stale when an axis is picked): "Pick what to plot on each axis. Look for the change that moved the result."

## Family engine
none.

## Sources
- Engineering design process (define, research, imagine, plan, create, test, improve): TeachEngineering, University of Colorado Boulder, "Engineering Design Process" (https://www.teachengineering.org/populartopics/designprocess); NASA, "The Engineering Design Process" educator guide (https://www.nasa.gov/stem), as of October 2026.
- Tipping and balance (torque about an edge): OpenStax College Physics 2e, chapter 9 "Statics and Torque" (https://openstax.org/details/books/college-physics-2e).
- Cantilever bending (deflection = P L^3 / 3 E I): OpenStax University Physics Volume 1, chapter 12 "Static Equilibrium and Elasticity" (https://openstax.org/details/books/university-physics-volume-1).
- PLA density (about 1.24 g/cm3) and stiffness (about 3.5 GPa): typical published filament datasheet values, as of 2026; the tool names no brand. Price $20 per kilogram and 4 minutes per gram are round classroom values, labeled as such.
- Clients, briefs and the bench are made up for this tool. Data as of: October 2026.
- Checks run (Python, 2026-10-29, the model above over all 432 designs): every worked check reproduces except two trial values, now fixed: the sample's second trial is 0.140 (0.13845 x 1.01 = 0.1398), not 0.139, and Brief C's first trial is 0.298 (0.30753 x 0.97 = 0.2983), not 0.299. Passing designs: Brief A 27, Brief B 4 (70/60/3/15, 80/50/3/15, 80/55/3/15, 80/60/3/15), Brief C 1. Only 60/70/3/15 passes with a single trial under 0.30 (the small-margin flag). At a 1 N tip target, Brief A keeps 5 designs (110 and 120 mm bases, 3 mm walls, 15%) and Briefs B and C none. The 8-hour budget is about 8 prints of the sample (58 minutes each) or 5 of the Brief A answer at 80 mm (97 minutes).

## Done when
1. Every worked check above matches to the shown precision (0.1 g, $0.01, 1 minute, 0.001 N, 0.01 mm).
2. The tip trials always come out x0.97, x1.01, x1.02 and average to F; a single trial under target is flagged even when the average passes.
3. A design whose phone balance point is past the base tips with no push, in words and in the stage.
4. Print and test spends printer time; Sketch only does not; the budget ends prints at 8 hours unless No time limit is on.
5. Notebook highlights changed cells, notes multi-change versions, plots any variable against any result with the requirement line, and Copy notebook pastes cleanly into a spreadsheet.
6. Brief C accepts only 60 mm, 70 degrees, 3 mm, 15%.
7. Keep my notebook and Clear work; the Conclusion text is never stored.
8. Focus: at 1366x768 and 680x425 the stand with its phone is the largest thing in Design, the table in Notebook and the client card in Brief.
9. Tap while it plays: a stepper tap or Show results now during the print or a test ends the run at once with the results card, and no stale result line plays after.
10. The phone turns with the lean angle at every step from 50 to 75 degrees and stays on the lip; all 7 paintings load with no person or fake lettering.
11. Controls, Print and test and the results card are visible without scrolling at every STANDARDS.md size; pass and miss always carry a word and an icon.
12. How lines once each in five actions in a row; result lines every time, dropped when stale.

## Open questions
- A 0.30 N tip target stands in for "a firm screen tap". A real tap can be closer to 0.5 to 1 N; at 1 N only five Brief A designs (110 or 120 mm bases) pass, and no Brief B or C design does. Keep 0.30 N as a classroom simplification (said in the Brief footer), or raise it and loosen cost and time?
- The 8-hour printer budget per brief is a game limit. Keep it on by default, or default to No time limit?
