# pH Mystery Liquids

## One idea
A flooded prep room has left a shelf of unlabeled bottles, and students are the lab crew who must identify them
without ever tasting or smelling: indicator colors, a conductivity bulb, dilution and a baking soda test each tell
something different, and the big lesson comes when two bottles read the same pH but need 208 times different amounts
of baking soda to neutralize, because pH measures the acid that has split, not the acid that is there.

## Not like
- equation-balancer (gr 10, same group): balances equations on a bench. Here the reactions are given, and the work is testing unknowns and reading results.
- mole-bakery (gr 10, same group): baking soda and acids in grams for a recipe. Here baking soda is a test and a spill cleaner, and the question is how much acid is hiding behind a pH reading.
- elements-inspector (gr 6-12, elements): properties of single elements. Here mixtures in water and their behavior.
- fair-dice-investigation (gr 12, statistics): a case solved with tests. Here every test is a chemical one, and safety rules come first.

## Who and how
- Grade 10, Chemistry, Acids, Bases and Solutions. Students drive, in pairs works well. 25 to 40 minutes.
- Topic line: "acids, bases and pH".
- Standards (module): HS-PS1-2 (explain a simple reaction's outcome from patterns of chemical properties: acids with
  carbonates make CO2, salt and water; strong and weak acids react the same way, in different amounts).
- tool.json: driver "students", minutes "25-40", modes ["Cases", "Bench"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Test it. Never taste it." Modes `Cases` (opens first), `Bench`. Kit buttons (Motion, Sound,
Read; Sound starts on as the kit sets it).
Stage: the painted lab bench (phm-bench) with the bottle rack along the back (painted bottles, the letters A, B, C...
written in code on their blank labels), the test beaker front and centre (10 mL sample; the liquid and its color are
drawn in code inside the painted glass), and the test tray in front: `pH meter`, four indicators (`Methyl orange`,
`Bromothymol blue`, `Phenolphthalein`, `Litmus paper`), `Conductivity` (a bulb that is dark, dim or bright),
`Dilute ×10` (10 mL of sample made up to 100 mL with distilled water, then 10 mL of that becomes the new sample;
repeatable), `Vinegar drops` (fizz or no fizz) and `Baking soda` (+0.001, +0.01, +0.1 g buttons, with a running
total). Each tray button shows its painted piece (Art) with the name in code under it. `Fresh sample` empties the
beaker and takes 10 mL from the bottle again.
Panel: the notebook, a grid of bottles against tests that fills itself as tests run, plus the case card.

### Cases
Focus: the test beaker, the largest thing on the stage and in its centre, with the bottle rack right behind it; the
notebook grid is second, in the panel. In C3 the spill tray takes the beaker's place and the pH graph sits beside it
at the same height, so tray and graph share the focus.
- C1 Flooded prep room: six bottles A to F and six labels to drag on (Content). The pH meter is "out for repair":
  indicators, conductivity, dilution and vinegar drops only. `Check labels` marks each right or wrong; wrong labels
  can be moved and checked again. The case card opens over phm-prep-room under a 70 percent dark overlay.
- C2 Same pH, different strength: two bottles read 2.4 on the meter. Task 1: grams of baking soda to neutralize 10
  mL of each (methyl orange turns yellow and fizzing stops). Task 2: dilute each ×10 and read the meter again. Task 3:
  pick the explanation (three choices, one right).
- C3 Spill drill: a virtual spill of 50 mL of 1.0 M hydrochloric acid in the painted spill tray. The first step must
  be `Tell the teacher` (the card will not start otherwise). Then add baking soda in steps and watch the pH graph; the
  card asks why baking soda is chosen over a strong base.
Progress saved on this device (localStorage `curio-ph-mystery-liquids`, try/catch), `Clear` resets.

### Bench
Focus: the test beaker, as in Cases. Every liquid in Content available by name (the names written in code on the
blank bottle labels), every test open, plus a pH ladder card with real food values and a painted picture of each food.
For teachers to demonstrate and for students to check ideas after a case.

## Content
Liquids (in the model; 25 °C):
- White vinegar, 5 percent acetic acid, 0.8326 mol/L (Ka 1.8 × 10⁻⁵): pH 2.41; ×10 2.92; ×100 3.42.
- Dilute hydrochloric acid, 0.0040 mol/L (a strong acid, fully split): pH 2.40; ×10 3.40; ×100 4.40.
- Household ammonia, diluted to 0.10 mol/L (Kb 1.8 × 10⁻⁵): pH 11.12; ×10 10.62.
- Baking soda solution, 0.10 mol/L NaHCO3: pH 8.35 (halfway between carbonic acid's pKa1 6.37 and pKa2 10.33, from
  Ka1 4.3 × 10⁻⁷ and Ka2 4.7 × 10⁻¹¹); dilution leaves it near 8.35 (model).
- Borax solution, 0.025 mol/L: pH 9.27 (boric acid pKa, from Ka 5.4 × 10⁻¹⁰; borax makes equal boric acid and
  borate, so dilution leaves it at 9.27).
- Salt water, 0.50 mol/L NaCl: pH 7.0.
- Distilled water left open to air: pH 5.6 (carbon dioxide from the air dissolves in it).
Conductivity bulb from total ion concentration (model): dark below 0.0005 mol/L, dim to 0.02, bright above. Vinegar
0.0077 and the dilute HCl 0.0080 are both dim (same pH, nearly the same ions), ammonia 0.0027 dim, baking soda 0.20,
borax 0.10 and salt water 1.0 bright, distilled water dark.
Indicators: methyl orange red below 3.1, orange 3.1 to 4.4, yellow above 4.4; bromothymol blue yellow below 6.0,
green 6.0 to 7.6, blue above 7.6; phenolphthalein colorless below 8.2, pink above 8.2 (pale pink 8.2 to 8.6); litmus
red below 4.5, purple between, blue above 8.3.
Vinegar drops: fizz with the baking soda solution only (CO2); every other liquid shows no fizz.
C1 bottles: A ammonia, B salt water, C vinegar, D borax, E distilled water, F baking soda. A teacher can press
`New shelf` to shuffle the letters (seeded). One solving path: conductivity splits bright (B, D, F) from dim (A, C)
and dark (E); methyl orange picks C; phenolphthalein plus vinegar drops split D from F; bromothymol green picks B.
C2: 10 mL of vinegar needs 0.699 g of baking soda; 10 mL of the HCl needs 0.0034 g. Ratio 208. On the 0.001 g
buttons the fizz stops at the press that reaches 0.700 g (vinegar) and 0.004 g (HCl); the result card reports the
exact amounts needed, 0.699 g and 0.0034 g, and the ratio 208. Diluted ×10, HCl rises a full unit to 3.40, vinegar
only half a unit to 2.92: most of the acetic acid had not split, and it splits as the split part is used up or
diluted. Right explanation: "Vinegar has far more acid in the bottle; only a little of it is split at a time, and pH
counts only the split part."
C3: 50 mL of 1.0 M HCl is 0.050 mol and needs 4.20 g of baking soda (HCl + NaHCO3 → NaCl + H2O + CO2). pH while
adding (model, volume change ignored, CO2 escapes): 0 g 0.00, 2.10 g 0.30, 3.78 g 1.00, 4.16 g 2.02, 4.20 g 4.08 (a
trace of acid is left: the exact need is 4.2004 g), 4.201 g and beyond 8.35 (extra baking soda holds near 8.35), so
overshooting is harmless. A strong base would overshoot to a high, caustic pH (said in words, no number). Right
answer: "Extra baking soda cannot push the spill far past neutral."
pH ladder card (real foods, Clemson Cooperative Extension): lime juice 2.00 to 2.35, lemon juice 2.00 to 2.60, vinegar
2.40 to 3.40, apple juice 3.35 to 4.00, tomato juice 4.10 to 4.60.
Safety footer (both modes): "This is a virtual lab. In a real lab: goggles on, never taste or smell a chemical, tell
your teacher about every spill, and follow your school's lab safety rules." Never mix bleach with acids or ammonia
appears in help (a reason the shelf has no bleach).

## Interactions in detail
- Every reading comes from the model above, not from a stored table: strong acid pH = −log C; weak acid and weak
  base use the exact quadratic; dilution divides C by 10 each time; the buffer liquids stay put. At the exact
  neutral point (acid left 0, no extra soda) the reading is 7.0; any extra baking soda reads 8.35.
- Baking soda: moles of acid in the sample are fixed; each addition reacts until the acid is used up; fizz shows
  while acid remains; methyl orange and the pH meter follow. The beaker shows "used up" once the acid is gone.
- Fizz is a short animation (about 1 s of bubbles drawn in code over the liquid). Any press during it acts at once:
  the next soda press updates the total, color and reading in the same frame; a new test replaces the shown result.
- C1 locks the pH meter (grayed, with the words "out for repair"). The notebook records every test result in words.
- C3 graph: grams of baking soda against pH, points added on each press.
- Keyboard: tests are buttons; labels in C1 are placed with Enter (pick label, then pick bottle), not only drag.
- `window.__tool = {state, setMode, case(id), bottle(letter), test(name), dilute(), soda(g), fresh(), check()}`.

## Look
Accent `--brand #d590b0` (orchid, like red cabbage juice), `--brand-ink #10141a`. The painted bench sets the scene;
code colors on top of it: glass highlight `#cfe3f1` at 25 percent. Indicator colors drawn true (methyl orange
`#e0442c` / `#f08a24` / `#f5d02c`; bromothymol `#f2d43a` / `#5fbf6a` / `#3f74d9`; phenolphthalein clear / `#f7a8d0`
/ `#e0479a`; litmus `#d9443c` / `#9a6bc4` / `#4a78d6`), always with the color name written beside the beaker. Bulb:
dark `#2a2f38`, dim `#a08a3c`, bright `#fff3a0` plus the word. Contrast (computed): brand on panel 6.96:1, on
--sec-bg 6.60:1, brand-ink on brand 7.43:1. Letters on the blank labels `#10141a` on the label's white.

## Art
Local FLUX (`scripts/localart.py`), house style in `art/prompts.json` (cool daylight, slate blues and soft grays,
blank surfaces). No people anywhere. 18 images.
- phm-prep-room (already made, keep): a school chemistry prep room after a small flood, a wooden shelf of plain clear
  glass bottles with blank white labels, a damp tiled floor with shallow puddles, a window with soft daylight, empty
  and quiet; 16:9; cutout no; people no; behind the C1 case card under a 70 percent dark overlay.
- phm-bench: a black epoxy chemistry lab bench seen from the front at eye level, an empty steel shelf on a white tiled
  wall behind, soft cool daylight from the left; 16:9; cutout no; people no; the stage background in both modes.
- phm-bottle: one clear glass reagent bottle with a black screw cap and a blank white paper label, holding clear
  colorless liquid, front view; 3:4; cutout yes; people no; reused for every bottle in the rack (all seven liquids are
  colorless), the letter or name written in code on the label.
- phm-beaker: an empty plain clear glass beaker with a pouring lip and smooth unmarked sides, front view, studio
  light; 1:1; cutout yes; people no; drawn over a code layer: the liquid fill and its indicator color are clipped to
  the beaker's inner outline (a polygon in image coordinates), the glass on top so it reads as inside.
- Tray kit (one shared prompt line, each piece a separate cutout, 1:1, people no): "a single piece of school lab
  equipment on a plain light gray background, front view, studio light, blank surfaces", pieces: phm-meter (a
  handheld pH meter with a blank gray screen and a probe on a coiled cable), phm-dropper (a small amber glass dropper
  bottle with a blank white label; reused for the four indicators and Vinegar drops, names in code), phm-litmus (a
  strip of plain white test paper), phm-tester (a conductivity tester: two steel probes wired to a small clear bulb
  in a holder), phm-wash (a soft plastic wash bottle with a bent spout), phm-flask (an empty 100 mL volumetric flask
  with a long thin neck), phm-soda (a white plastic jar of white powder with a steel lab scoop resting on top),
  phm-tray (a shallow white plastic spill tray, seen at an angle), phm-goggles (clear lab safety goggles with a
  gray strap). Sizing rule: on the stage each piece is drawn at its real height against the 20 cm bottle (meter 18,
  dropper 9, litmus strip 7, tester 15, wash bottle 20, flask 22, soda jar 10, goggles 6 tall); in the tray every
  piece fits the same 64 px box. The tester's bulb glow and the meter's reading are code over the blank parts.
- Food kit for the pH ladder card (one shared prompt line, 1:1, cutout no, people no): "a still life of one food on
  a plain pale wooden table, soft daylight, close up", pieces: phm-lime (a cut lime and a small glass of lime juice),
  phm-lemon (a cut lemon and a small glass of lemon juice), phm-vinegar (a clear glass cruet of pale vinegar),
  phm-apple (a glass of golden apple juice beside a red apple), phm-tomato (a glass of red tomato juice beside a
  ripe tomato). Each sits beside its pH range on the ladder.
Drawn in code: liquid fills and indicator colors, fizz bubbles, bulb glow, meter reading, letters and names on
labels, the notebook grid, the C3 pH graph, the pH ladder scale, preview.svg.

## Voice
Bank voice `firm-captain` (the lab safety lead). No grade 10 or 11 science neighbor or batch sibling uses it.
`Curio.voice`, `scope: () => state.mode`. Hints change at once on every mode, case or step change; lines queue with a
`valid` check.
- wCases (how; Cases welcome; stale once a case card is opened): "Press a case card in the panel to open your first
  job."
- c1 (how; C1 opens; stale once Check labels is pressed): "Press a test in the tray to run it. Then drag each label
  onto a bottle and press Check labels."
- noMeter (how; first press on the locked meter in C1; stale when C1 closes): "The meter is out for repair. Press an
  indicator or Conductivity instead."
- wrong (event; every Check labels with a wrong label; stale when a label moves): "Some labels are wrong. Move the
  crossed ones and press Check labels again."
- c2Tip (how; C2 opens; stale once the fizz has stopped on both bottles): "Both read 2.4. Press the baking soda
  buttons a little at a time and watch for the fizz to stop."
- spillFirst (how; C3 opens; stale once Tell the teacher is pressed): "Spill rule one. Press Tell the teacher before
  anything else."
- c3Soda (how; Tell the teacher pressed; stale on the first soda press): "Good. Now press the baking soda buttons and
  watch the pH graph climb."
- solved (event; a case is solved; stale when another case opens): "Case closed. Every bottle is labeled right."
- wBench (how; Bench welcome; stale on the first test): "Press a bottle to fill the beaker, then press any test in the
  tray."

## Family engine
None. The liquid model is a small `LIQUIDS` table in the tool (C, Ka or Kb or buffer pH, ions) with the pH and
conductivity functions above.

## Sources
- HS-PS1-2: NGSS Lead States (2013), Next Generation Science Standards, https://www.nextgenscience.org/
- Ka of acetic acid, carbonic acid (Ka1, Ka2) and boric acid: OpenStax, Chemistry 2e, Appendix H "Ionization Constants of Weak Acids"; Kb of ammonia: Appendix I "Ionization Constants of Weak Bases", https://openstax.org/books/chemistry-2e/pages/h-ionization-constants-of-weak-acids
- pH, strong and weak acids, indicator ranges: OpenStax, Chemistry 2e, 14.2 "pH and pOH", 14.3 "Relative Strengths of Acids and Bases", 14.7 "Acid-Base Titrations" (its indicator color-range figure), https://openstax.org/books/chemistry-2e/pages/14-7-acid-base-titrations
- Electrolytes and conductivity: OpenStax, Chemistry 2e, 11.2 "Electrolytes".
- Rain and clean water near pH 5.6 from dissolved carbon dioxide: U.S. EPA, "What is Acid Rain?", https://www.epa.gov/acidrain/what-acid-rain (checked 2026-10-27).
- Food pH ranges: Clemson Cooperative Extension (P. Ingham), "pH Values of Common Foods and Ingredients" (checked 2026-10-27), https://www.clemson.edu/extension/food/
- Lab safety: American Chemical Society, Guidelines for Chemical Laboratory Safety in Secondary Schools (2016), https://www.acs.org/
- Number checks (Python, 2026-10-29, exact quadratics with the constants above): vinegar 2.413, 2.915, 3.422; HCl
  2.398, 3.398, 4.398; ammonia 11.125 and 10.618; baking soda 8.347; borax 9.268; ions 0.0077 (vinegar), 0.0080
  (HCl), 0.0027 (ammonia), all dim. Every C1 liquid's four indicator colors listed and the solving path holds (C the
  only red methyl orange in the dim pair; D pink and F pale pink, F the only fizz; B the only green bromothymol).
  C2: 0.6994 g and 0.00336 g, ratio 208.2; with 0.001 g steps 0.699 g still leaves acid, so the fizz stops at 0.700 g
  (and at 0.004 g for HCl): text changed to say so. C3: 4.2004 g needed; 4.16 g gives pH 2.02 (was printed 2.00, the
  exact 2.00 is at 4.158 g); 4.20 g leaves 0.0042 mmol and reads 4.08, not 7.0 (was printed 7.0, fixed); 4.201 g
  passes the neutral point and reads 8.35.

## Done when
1. Bench: vinegar reads 2.41, ×10 2.92, ×100 3.42; HCl reads 2.40, ×10 3.40; ammonia 11.12; baking soda 8.35; borax 9.27; distilled 5.6; salt water 7.0.
2. Each indicator shows the color in Content at each of those pH values, with the color word.
3. Conductivity: vinegar and HCl dim, salt water bright, distilled dark.
4. C1: the meter stays locked; all six labels right gives the solved card and "Case closed."; a wrong label gives the
   wrong line each time; `New shelf` reshuffles and the key follows.
5. C2: fizz stops on vinegar at the 0.700 g press and on HCl at 0.004 g; the result card shows 0.699 g, 0.0034 g and
   the ratio 208.
6. C3 will not start before `Tell the teacher`; the graph passes 0.30 at 2.10 g, 1.00 at 3.78 g, 4.08 at 4.20 g, and
   jumps to 8.35 at 4.201 g and holds there.
7. Focus: the beaker is the largest, central thing on the stage at 1366x768 and in the 680x425 preview; in C3 the
   tray and graph are side by side and both larger than the panel's notebook.
8. A tap while the fizz plays: a soda press updates the total, color and reading in the same frame; pressing a
   different test replaces the result at once.
9. How-to lines once each per load, then hint only; no line names the pH meter while it is locked except noMeter.
10. Progress survives a reload; `Clear` resets.
11. All 18 images load, none shows a person or lettering; bottle letters and tray names are readable code text.
12. Every size in STANDARDS.md keeps the beaker, the test tray and the notebook reachable; keyboard-only works, including labeling; console clean, no network, no em dashes.

## Open questions
- HS-PS1-2 is about outer electrons and periodic trends; this tool teaches patterns of chemical properties (acids with carbonates) but not electrons. Keep the code, or move acids to a module with a better-fitting standard?
- The bulb thresholds (dark, dim, bright by ion concentration) are a model choice, not measured values. OK?
- [ph-mystery-liquids] With 0.001 g steps the C3 graph never lands exactly on 7.0 (4.20 g reads 4.08, 4.201 g reads
  8.35). The spec now says so. Fine, or add a finer step so students can land on neutral?
