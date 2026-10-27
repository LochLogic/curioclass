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
Header: title, subtitle "Test it. Never taste it." Modes `Cases` (opens first), `Bench`. Kit buttons.
Stage: a lab bench with a bottle rack (labeled A, B, C...), a test beaker (10 mL sample), and the test tray: `pH
meter`, four indicators (`Methyl orange`, `Bromothymol blue`, `Phenolphthalein`, `Litmus paper`), `Conductivity`
(a bulb that is dark, dim or bright), `Dilute ×10` (10 mL of sample made up to 100 mL with distilled water, then 10
mL of that becomes the new sample; repeatable), `Vinegar drops` (fizz or no fizz) and `Baking soda` (+0.001, +0.01,
+0.1 g buttons, with a running total). `Fresh sample` empties the beaker and takes 10 mL from the bottle again.
Panel: the notebook, a grid of bottles against tests that fills itself as tests run, plus the case card.

### Cases
- C1 Flooded prep room: six bottles A to F and six labels to drag on (Content). The pH meter is "out for repair":
  indicators, conductivity, dilution and vinegar drops only. `Check labels` marks each right or wrong; wrong labels
  can be moved and checked again.
- C2 Same pH, different strength: two bottles read 2.4 on the meter. Task 1: grams of baking soda to neutralize 10
  mL of each (methyl orange turns yellow and fizzing stops). Task 2: dilute each ×10 and read the meter again. Task 3:
  pick the explanation (three choices, one right).
- C3 Spill drill: a virtual spill of 50 mL of 1.0 M hydrochloric acid in a tray. The first step must be `Tell the
  teacher` (the card will not start otherwise). Then add baking soda in steps and watch the pH graph; the card asks
  why baking soda is chosen over a strong base.
Progress saved on this device (localStorage `curio-ph-mystery-liquids`, try/catch), `Clear` resets.

### Bench
Every liquid in Content available by name, every test open, plus a pH ladder card with real food values. For
teachers to demonstrate and for students to check ideas after a case.

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
C2: 10 mL of vinegar needs 0.699 g of baking soda; 10 mL of the HCl needs 0.0034 g. Ratio 208. Diluted ×10, HCl rises
a full unit to 3.40, vinegar only half a unit to 2.92: most of the acetic acid had not split, and it splits as the
split part is used up or diluted. Right explanation: "Vinegar has far more acid in the bottle; only a little of it is
split at a time, and pH counts only the split part."
C3: 50 mL of 1.0 M HCl is 0.050 mol and needs 4.20 g of baking soda (HCl + NaHCO3 → NaCl + H2O + CO2). pH while
adding (model, volume change ignored, CO2 escapes): 0 g 0.00, 2.10 g 0.30, 3.78 g 1.00, 4.16 g 2.00, 4.20 g 7.0;
extra baking soda holds near 8.35, so overshooting is harmless. A strong base would overshoot to a high, caustic pH
(said in words, no number). Right answer: "Extra baking soda cannot push the spill far past neutral."
pH ladder card (real foods, Clemson Cooperative Extension): lime juice 2.00 to 2.35, lemon juice 2.00 to 2.60, vinegar
2.40 to 3.40, apple juice 3.35 to 4.00, tomato juice 4.10 to 4.60.
Safety footer (both modes): "This is a virtual lab. In a real lab: goggles on, never taste or smell a chemical, tell
your teacher about every spill, and follow your school's lab safety rules." Never mix bleach with acids or ammonia
appears in help (a reason the shelf has no bleach).

## Interactions in detail
- Every reading comes from the model above, not from a stored table: strong acid pH = −log C; weak acid and weak
  base use the exact quadratic; dilution divides C by 10 each time; the buffer liquids stay put.
- Baking soda: moles of acid in the sample are fixed; each addition reacts until the acid is used up; fizz shows
  while acid remains; methyl orange and the pH meter follow. The beaker shows "used up" once the acid is gone.
- C1 locks the pH meter (grayed, with the words "out for repair"). The notebook records every test result in words.
- C3 graph: grams of baking soda against pH, points added on each press.
- Keyboard: tests are buttons; labels in C1 are placed with Enter (pick label, then pick bottle), not only drag.
- `window.__tool = {state, setMode, case(id), bottle(letter), test(name), dilute(), soda(g), fresh(), check()}`.

## Look
Accent `--brand #d590b0` (orchid, like red cabbage juice), `--brand-ink #10141a`. Bench `#1e2630`, glass `#cfe3f1` at
25 percent. Indicator colors drawn true (methyl orange `#e0442c` / `#f08a24` / `#f5d02c`; bromothymol `#f2d43a` /
`#5fbf6a` / `#3f74d9`; phenolphthalein clear / `#f7a8d0` / `#e0479a`; litmus `#d9443c` / `#9a6bc4` / `#4a78d6`),
always with the color name written beside the beaker. Bulb: dark `#2a2f38`, dim `#a08a3c`, bright `#fff3a0` plus
the word. Contrast (computed): brand on panel 6.96:1, on --sec-bg 6.60:1, brand-ink on brand 7.43:1.

## Art
- phm-prep-room: "a school chemistry prep room after a small flood, a wooden shelf of plain glass bottles with blank
  white labels, a damp floor, a window with daylight, painterly, no writing anywhere, no people"; 16:9; cutout no;
  people no; behind the case card at the start of C1 under a 70 percent dark overlay (Cloudflare FLUX).

## Voice
Bank voice `firm-captain` (the lab safety lead). No grade 10 science neighbor uses it. `Curio.voice`, scope = mode.
- wCases (how, Cases welcome): "Pick a case card. Run tests from the tray, then drag each label onto a bottle."
- noMeter (how, first press on the locked meter in C1): "The meter's out. Use the indicators and the bulb."
- c2Tip (how, C2 opens): "Both read 2.4. Add baking soda a little at a time and watch for the fizz to stop."
- spillFirst (how, C3 opens): "Spill first rule: press Tell the teacher before anything else."
- solved (event, a case is solved; stale when another case opens): "Case closed. Every bottle is labeled right."

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
- Every pH, gram amount and ratio recomputed in Python (2026-10-27).

## Done when
1. Bench: vinegar reads 2.41, ×10 2.92, ×100 3.42; HCl reads 2.40, ×10 3.40; ammonia 11.12; baking soda 8.35; borax 9.27; distilled 5.6; salt water 7.0.
2. Each indicator shows the color in Content at each of those pH values, with the color word.
3. Conductivity: vinegar and HCl dim, salt water bright, distilled dark.
4. C1: the meter stays locked; all six labels right gives the solved card; `New shelf` reshuffles and the key follows.
5. C2: fizz stops on vinegar at 0.699 g and on HCl at 0.0034 g; the ratio 208 appears in the result card.
6. C3 will not start before `Tell the teacher`; the graph passes 0.30 at 2.10 g, 1.00 at 3.78 g, 7.0 at 4.20 g, and holds 8.35 after.
7. Progress survives a reload; `Clear` resets.
8. Every size in STANDARDS.md keeps the beaker, the test tray and the notebook reachable; keyboard-only works, including labeling; console clean, no network.

## Open questions
- HS-PS1-2 is about outer electrons and periodic trends; this tool teaches patterns of chemical properties (acids with carbonates) but not electrons. Keep the code, or move acids to a module with a better-fitting standard?
- The bulb thresholds (dark, dim, bright by ion concentration) are a model choice, not measured values. OK?
