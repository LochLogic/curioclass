# Shadow Measure

## One idea
You can't climb the flagpole, but light makes two similar triangles for you: the sun's parallel rays, a mirror on
the ground, or a streetlight at night each pair the thing you can't measure with a meter stick you can, so you tape
out a few lengths, record them in a lab notebook, say why the triangles are similar, and only then see the real
height and how close you got.

## Not like
- fire-lookout-triangles (gr 12 map): laws of sines and cosines across a forest, no right angles. Here only similar right triangles, no trig at all.
- ramp-and-roof (gr 10, this group): sine, cosine and tangent of a chosen angle. Here no angle is ever measured; the light makes the angles equal and ratios of measured lengths do the work.
- rigid-motion-twins (gr 10, this group): congruence by slides, turns and flips. Here similarity, and the streetlight's shadow is a dilation you can watch.
- smoothie-lab (gr 6 lab): equal ratios in recipes. Here ratios come from measuring a scene, with real measuring error.
- launch-pad (gr 9 simulator): heights over time from a formula. Here heights come from measurements.

## Who and how
- Grade 10, Geometry, module Similarity. Students drive, own laptops or pairs. 15 to 40 minutes.
- Topic line: "similar triangles and dilations".
- Standards (module): G-SRT.A (dilations; similarity transformations; AA from them), G-SRT.B (prove theorems with
  similarity; use similarity criteria to solve problems).
- CCSS clusters: Streetlight and its `Show dilation` layer serve G-SRT.A.1 and A.3; the `Why similar?` step in every
  method serves G-SRT.A.3 and B.5; the notebook's height calculations serve G-SRT.B.5.
- tool.json: driver "students", minutes "15-40", modes ["Sun", "Mirror", "Streetlight"], grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Shadow Measure", subtitle "Measure what you can't climb." Modes `Sun` (opens
first), `Mirror`, `Streetlight`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (a side view of the schoolyard, drawn to scale and re-laid out per size), panel right (the lab
notebook). Under 1000 px wide the panel goes under the stage, notebook steps first. Under 900 px tall the notebook
shows only the current step with `Notebook` to open the table.

Every mode has the same four lab steps in the panel, one at a time: `1 Set up`, `2 Measure`, `3 Why similar?`,
`4 Reveal`. Plus `New trial` and the notebook table (Content).

### Sun
- Scene: sky, grass, a blacktop strip; a meter stick (1.00 m) standing on the blacktop; one tall object picked in
  Set up: `Flagpole`, `Tree`, `Hoop`, `Sign`. Slider `Sun height` 25° to 65° (step 1°); shadows of the stick and
  the object are drawn from the sun's parallel rays.
- Measure: two tapes, one per shadow. Drag a tape's end (or arrow keys, 0.01 m a press) from the base to where you
  see the shadow tip; the tape reads to the nearest 0.01 m. `Record` writes both readings into the notebook.
### Mirror
- Scene: the gym wall (or the flagpole), a small mirror flat on the ground, and a sighting tripod with its eyepiece
  1.50 m up (no person). Set up: drag the mirror to any spot 4 to 12 m from the wall's base.
- Slide the tripod toward or away from the mirror. A round sight window in the panel shows what the eyepiece sees in
  the mirror; when the top of the wall reaches the crosshair (within ±0.10 m of the top) the window says "Top in
  the crosshair". Then tape mirror-to-wall and mirror-to-tripod, and `Record`.
### Streetlight
- Night scene: a streetlight of unknown height, a 1.00 m stick on the ground. Drag the stick anywhere 1 to 8 m from
  the lamp's base; its shadow stretches away from the lamp. Tape the stick-to-lamp distance and the shadow length,
  `Record`.
- Layer toggle `Show dilation`: rays from the shadow tip through the lamp and through the stick's top; the readout
  "The stick is the lamp post dilated by k = 0.21 from the shadow tip" (k = shadow ÷ (shadow + distance)), and any
  point on the lamp triangle you hover maps to its image on the stick triangle. A second stick position stays as a
  ghost so two shadows can be compared.

## Content
Objects (true heights are this schoolyard's own, invented, except the hoop):
- Flagpole 8.40 m, tree 11.25 m, hoop rim 3.05 m (10 ft, the regulation rim height), sign 2.40 m, gym wall 6.75 m,
  streetlight 4.80 m. Meter stick 1.00 m. Tripod eyepiece 1.50 m.
Height formulas the notebook uses (shown with the student's numbers):
- Sun: height = stick × (object shadow ÷ stick shadow).
- Mirror: height = eye height × (mirror-to-wall ÷ mirror-to-tripod).
- Streetlight: lamp height = stick × (shadow + distance) ÷ shadow.
`Why similar?` cards (pick two for the angle-angle reason): "Both stand straight up on level ground: right angles",
"The sun's rays are parallel, so they meet the ground at the same angle", "At a mirror the angle in equals the angle
out", "Both triangles share the angle at the shadow tip", and two that don't prove anything: "The shadows are about
the same color" and "The two triangles look about the same shape". Correct pairs: Sun: right angles + parallel
rays. Mirror: right angles + angle in equals angle out. Streetlight: right angles + shared angle.
Notebook table columns: Trial, Method, Object, Reading 1 (m), Reading 2 (m), Estimate (m), Real (m), Off by (%).
`Reveal` fills Real and Off by = |estimate − real| ÷ real × 100, one decimal.

## Interactions in detail
- Geometry: shadow length = height ÷ tan(sun height). The tape shows a reading rounded to 0.01 m from where its end
  sits; the estimate uses the recorded readings, so careless taping shows up honestly as error. Estimates are
  rounded to 0.01 m for display; Off by uses the unrounded estimate rounded at the end.
- Worked readings (exact tape placement): Sun 40°, flagpole: stick 1.19, flag 10.01, estimate 8.41 m, off 0.1%.
  Sun 25°, tree: 2.14 and 24.13, estimate 11.28 m, off 0.2%. Sun 55°, hoop: 0.70 and 2.14, estimate 3.06 m, off
  0.2%. Mirror, wall 6.75 m, mirror at 9.00 m: crosshair at tripod distance 2.00 m, estimate 6.75 m. Streetlight,
  stick 5.00 m from the lamp: shadow 1.32, estimate 4.79 m, off 0.3%; at 3.80 m: shadow 1.00, estimate 4.80 m.
- `Record` is enabled only once both tapes have been moved off zero. `3 Why similar?` must have a correct pair
  before `4 Reveal` opens; a wrong card shakes and says why ("Color doesn't fix any angle.").
- Edge cases: a zero stick shadow can't happen (sun height capped at 65°). If a tape reading is 0, Record is off.
  Off by over 10% adds "Check where each tape ends." Changing the sun, mirror or stick after Record starts a new
  trial. The streetlight dilation k is always between 0 and 1 (shown with two decimals).
- Keyboard: Tab to a tape end or the tripod, arrow keys move 0.01 m, Shift+arrow 0.10 m. Each tape's
  aria-valuetext is "stick shadow tape, 1.19 meters".
- Reset: `New trial` keeps the notebook; `Clear notebook` empties it. The notebook lives for the page session only.
- `window.__tool = {state, setMode, setSun(deg), tape(name, meters), record(), why(cardA, cardB), reveal()}`.

## Look
Accent `--brand #ffd0f0` (sidewalk-chalk pink: the marks where shadow tips are chalked on the blacktop),
`--brand-ink #10161f`. Day scene: sky `#b9d4ea`, grass `#8fb07a`, blacktop `#3b3f45`, shadows black at 45%; scene
labels in `#10161f`. Night: sky `#0b1020`, lamp glow `#ffe7a3`, labels `#e8edf3`. Tape `#f3f0e8` with dark ticks.
Contrast (computed): brand on --panel 12.80:1, on --sec-bg 12.13:1; brand-ink on brand 13.43:1; scene ink on sky
11.82:1, on grass 7.49:1; chalk on blacktop 7.83:1; night labels 16.08:1. No 9-12 math tool uses a pale pink;
nearest are which-model-wins' #ff8fd0 and the silver #c7d2de.

## Art
- sm-schoolyard: "a quiet school playground seen from the side at mid afternoon, flat painted style, open sky above
  a low brick school building far in the back, a strip of grass, blank surfaces"; 16:9; cutout no; people no;
  FLUX (cfart). Used as the far backdrop only (above the horizon line); every object that casts a shadow is drawn in
  code to scale. Night uses the same image under a dark blue overlay.

## Voice
Bank voice `big-sister` (helpful older student), style "friendly and youthful, like a lab partner one grade ahead".
Not used by any grade 9 to 11 math tool (hole-hunter, gr 12, uses it). `Curio.voice`, `scope: () => state.mode`.
- wSun (how): "Pick an object. Then drag each tape from the base to the tip of its shadow, and tap Record."
- wMirror (how): "Set the mirror down. Slide the tripod until the top of the wall sits in the crosshair."
- wLight (how): "Drag the stick anywhere. Tape its distance to the lamp and its shadow, then tap Record."
- why (how, first time step 3 opens): "Pick two reasons that make the angles match. Then tap Reveal."
- crosshair (event, top enters the crosshair; stale if the tripod moves out): "There. The top is in the crosshair."
- close (event, Reveal with Off by under 2%; stale on new trial): "Very close. Your triangles did the climbing."
- far (event, Reveal with Off by over 10%; stale on new trial): "That one's off. Check where each tape ends."

## Family engine
none.

## Sources
- G-SRT text: Common Core State Standards for Mathematics, High School Geometry, Similarity, Right Triangles, and Trigonometry, https://www.thecorestandards.org/Math/Content/HSG/SRT/
- Hoop rim 10 feet above the floor: NBA Official Rule No. 1, Court Dimensions and Equipment, https://official.nba.com/rule-no-1-court-dimensions-equipment/ (read 2026-10-27; the same height is used in school play). On screen: "Rim height: 10 ft (3.05 m), rule as of 2026."
- Law of reflection (angle in equals angle out): OpenStax, College Physics 2e, 25.2 "The Law of Reflection", https://openstax.org/books/college-physics-2e/pages/25-2-the-law-of-reflection
- Sun rays treated as parallel (the sun is very far away): OpenStax, College Physics 2e, 25.1 "The Ray Aspect of Light", https://openstax.org/books/college-physics-2e/pages/25-1-the-ray-aspect-of-light
- AA similarity and dilations: Euclid's Elements VI.4 (equiangular triangles have proportional sides), D. E. Joyce edition, https://mathcs.clarku.edu/~djoyce/java/elements/bookVI/propVI4.html
- Every worked reading above was recomputed in Python (2026-10-27).

## Done when
1. Sun 40°, flagpole: exact taping gives 1.19 and 10.01, estimate 8.41 m, Reveal shows 8.40 m and 0.1%.
2. Sun 25°, tree: 2.14 and 24.13 give 11.28 m and 0.2% (Off by uses the unrounded estimate 11.2757).
3. Mirror at 9.00 m: the crosshair message appears with the tripod near 2.00 m; recording 9.00 and 2.00 gives 6.75 m.
4. Streetlight, stick at 5.00 m: shadow 1.32, estimate 4.79 m, off 0.3%; `Show dilation` reads k = 0.21.
5. Reveal stays locked until a correct `Why similar?` pair is chosen; the color card is refused with its reason.
6. A tape left 0.20 m short of the tip gives an honest error in Off by.
7. Keyboard alone can run a Sun trial to Reveal; every size in STANDARDS.md keeps the tapes and the current step visible without page scrolling.
8. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- none.
