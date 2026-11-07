OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 0, family 2), should fix 17 (general 8, family 9), polish accepted 16

# Refine: molecule-forge

Merged from refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity.md; all three lenses found nothing
cultural, Native or hard history). Judged as a Curiosity (No. 12) against docs/agents/CODEX-CURIOSITY.md and BASELINE.
Frame roots: Teaching `S:/CurioClass-codex-scratch/molecule-forge/teaching/frames/`, Play
`S:/CurioClass-codex-scratch/molecule-forge/play/` (f1 to f4), Craft `S:/CurioClass-codex-scratch/molecule-forge/craft/`,
shared audit `S:/CurioClass-codex-scratch/molecule-forge/audit-r1/`.
Integrator spot-checks: src.html:376-380 and 726 (bond label), 574-582 (no-grow lines), 497-501 (crystal seed add),
1218-1222 (hint), 688 (Spheres aria-pressed), and the `fact` field of material.json (22 of 32 start "In this model").
All confirmed as the lenses describe.

## Blocker
1. **Bond labels state lengths the model on screen contradicts.** src.html:726 (bond button text) and `length()` at
   src.html:376; Forge, any matched molecule. The visible label is always the radius-sum estimate with a bare "~", even
   after the molecule has glided to its stored PubChem conformer. H2 reads "H single · ~62 pm" while the drawn model is
   74 pm (and the Manual says 74). Benzene, vanillin and aspirin ring bonds read "single ~152" and "double ~132" while
   every ring bond in the model is 139 pm, so the readout teaches the alternating-length misconception the real
   structure disproves. Others more than 5 percent off: O2 115 vs 123, H2O2 O-O 132 vs 145, formic acid C-O 142 vs 135,
   urea and caffeine C-N 147 vs 137 to 139 (14 bond types over 5 percent in Teaching's `dev` measurement, shots2.json).
   Seen: teaching/frames/h2-label.png. Only the aria-label says "radius estimate". A meter that misleads when its
   assumption fails is a blocker (REFINE.md). Fixed looks like: once a structure matches, every bond label shows the
   stored model's distance ("139 pm, model"); while building (no match), the label says "estimate" on screen, not just
   "~", and the aria-label matches. For aromatic rings the order button may still step (it is how the student draws
   either Kekule pattern), but the length shown is the model's equal 139 pm; add one Manual line that benzene's ring
   bonds are all the same length, which is why both drawings name the same molecule. (family:curiosity)
2. **Silicon seeds are told they close into a molecule when the real substance is a giant network.** src.html:579-581,
   Crystal, `noGrow()`. Si + C gets "This closes into a molecule. Grow carbon alone, or two carbons." (play/f2/c11);
   silicon carbide is a real diamond-pattern covalent network, so the line is false. The last fallback ("Two of these
   close up into a small molecule") is equally untrue for other silicon pairs such as Si + N (silicon nitride is also a
   network). Weighed under the misleading-readout rule: the message's assumption (anything that is not one of the seven
   seeds closes into a molecule) fails here and the readout states a falsehood about a real material, so it is a
   blocker. Fixed looks like: any seed this forge does not grow gets an honest line that does not claim what it would
   make in nature when that claim is wrong, e.g. for Si + C "Silicon carbide is a real giant network, like diamond, but
   this forge does not grow it. Try carbon or silicon alone." Keep the C + O line (CO2 really is a molecule). Do not add
   silicon carbide as a crystal (that is a spec change, see open questions). (family:curiosity)

## Should fix
1. **The closing moment is flat (visual part).** src.html:453-465 `edited()`; Forge. The spec's first-two-minutes
   payoff is a thin cyan ring pulsing out from the molecule and the Field guide tab lighting with the name ("Water").
   The build plays a tone and glides; the only visible change is the strip name, and the Field guide button never
   changes. Seen: play/f1/p02, audit state-water-1366x768.png. Fixed: a single cyan (#5fd4ff) ring pulse on first close
   of each molecule this visit (Motion off: a brief static ring, no animation), and the Field guide tab shows the name
   for a few seconds (and opens on that page if tapped then). The spoken name is deferred (see Settled calls). (family:curiosity)
2. **The first-run hint hides on the wrong tap and is spoken after the student already acted (merged Play SF2, Craft
   F3, Play nit 2).** src.html:1218-1222. Any click anywhere hides the hint and queues the voice line: tapping the red
   oxygen in the well adds nothing but removes the only instruction (play/f4/h01); so does Motion (f4/h02). When the
   first tap does add an H, the voice then says "Tap an atom to snap it on." after it has already snapped on
   (craft/v-firstH.png, craft/voice1.py first_H log, audit one-click rows 1 to 9). The keyboard path (T, 2, G) never
   hides it, leaving the Forge hint over a grown diamond (play/f4/h03). Fixed: hide the hint when the first atom is
   actually added (tap, drag or key, either mode); skip the spoken hint (unmarked, so it can still play later) when the
   first action added an atom, and speak it once only when the first action was something else; word it "Tap an atom
   in the tray to snap it on." (the oxygen is an atom too), updating voice/lines.json and `allLines()` to match.
   (general; Craft tagged it family:curiosity)
3. **22 of 32 molecule pages and all 7 crystal pages show placeholder facts.** material.json `fact`; crystal pages
   built at src.html:1076 (`fact:c.pattern`). Oxygen, Nitrogen, Ammonia, Methane, CO2, Acetone, Propane, Butane,
   Vanillin, Aspirin and 12 more read "In this model: 2 O. 1 double bond."; crystals say only "Every inside atom touches
   4 neighbours." The spec lists a real fact for each page and says they are kept unchanged; the Manual's "Field guide
   facts" repeats the placeholders. Seen: teaching/frames/guide-oxygen.png, guide-diamond.png. Fixed: restore the
   spec's facts (spec.md "Real material and sources") with each page's named source, checked against a second source;
   drop only a fact that truly fails a second source, and say so in notes.md. Crystal pages get both the pattern line
   and the spec's use fact (Mohs 10, pencil lead, chips, quartz and sand, most wire, cut with a knife). (family:curiosity)
4. **A lone atom and its molecule carry the same name.** src.html:709. The opening oxygen reads "Oxygen", identical to
   the O2 page "Oxygen · O2"; a lone H reads "Hydrogen", and so does H2. Atom versus molecule is the anchor idea
   (MS-PS1-1). Seen: teaching/frames/guide-oxygen.png; checks.json `loneH`, `h2`. Fixed: "oxygen atom" / "hydrogen atom"
   for a single atom; the guide name only for a matched molecule. (family:curiosity)
5. **O=Si=O settles bent at about 165 degrees against the groups rule it teaches.** relax() src.html:748; Forge,
   Things to do 7. CO2 glides to 180 (matched) but O=Si=O stops at 165 (Motion on) or 153 (Motion off), and the
   readout says "about 165°" for a shape the Manual calls straight. Any unmatched two-group centre does the same.
   Seen: Teaching `osio-motion` shot, checks.json `osio`. Fixed: relaxation reaches the ideal angle for two-group
   centres (or snaps to it when settled); the same check for 120 and 109.5 targets. (family:curiosity)
6. **The outer-electron link (HS-PS1-1) is claimed but never shown.** Atom table src.html:287 (`ve` defined, never
   displayed). Nothing on screen connects spots to outer electrons. Fixed (inside the spec, which carries valence
   electrons in its atom table): one more part in the selected-atom readout, e.g. "O · 6 outer electrons · 2 spots ·
   2 filled · 2 lone pairs", and the same count in the tray ball's label. Dropping HS-PS1-1 instead would be a spec
   change. (general)
7. **The Manual reads at about grade 14.** src.html:238-276. "element-labelled connections", "computed PubChem
   conformer", "The extra recognized allene record also supplied only a 2D diagram ... two perpendicular pi bonds",
   "cristobalite-like network", "appreciable current", "not an atomic slip solver". Fixed: plain sentences for a grade 6
   to 10 reader ("Hydrogen and silane use a textbook shape instead of a PubChem one"), keeping every honesty point;
   build detail moves to notes.md. (general)
8. **"Things people have found" has 4 of the spec's 9 entries (Teaching polish 7, Play SF8).** src.html:272-273.
   Missing: lone pairs squeeze the angle (109.5, 107, 104.5); 78 °C against -24.8 °C; 92 legal C/N/O structures, 56
   unnamed; the pencil; salt cracks while copper bends; CO2 small but SiO2 giant; silicon a semiconductor; Wöhler 1828.
   Fixed: restore all nine as short separate entries, each with its source as in the spec. (family:curiosity)
9. **A stray tray tap in Crystal silently wipes the grown crystal.** src.html:499-501. With a one-atom seed, any tray
   tap adds to the seed and sets `crystal=null`; after diamond, one tap on H leaves "C · H, Seed plate" and an empty
   bench (play/f2/c15). Undo is hidden in Crystal (src.html:687), so only Ctrl+Z restores it, and Grow then refuses.
   Fixed: show Undo in Crystal too, and keep the grown specimen on the bench until the seed actually changes into a
   new growable seed or Clear seed is pressed. (general)
10. **Push outcomes look alike, so the comparison does not land.** src.html:878-883. Copper "bends" and graphite
    "slides" both draw as the top half shifted sideways (play/f2/c07, c08); diamond's push goes out and back
    (`65*sin`), so its end state looks untouched while the strip says "64 bonds cross this cut and none let go"
    (f2/c05). Fixed: distinct end shapes for crack (gap), bend (rows roll and the block stays whole and bowed), slide
    (sheets offset cleanly) and hold (nothing moves), and the bonds crossing the cut highlighted at the end so the
    student can count the bonds that hold (Things to do 9). A tap mid-test still shows the end state the same frame.
    (family:curiosity)
11. **Copper and sodium metal drop to 35 fps at 4x slowdown while turning.** draw() src.html:835-982, Crystal. Copper
    (561 atoms, 2,820 bonds) 34.5 fps, sodium (559, 1,728 bonds) 35 fps with Show on or dragging; graphite (600) passes.
    Done when 8 fails. Seen: craft/perf3.py. Fixed: 60 fps at 4x for both (e.g. batch bond strokes by colour, skip
    hidden back bonds, or cache the bond list per frame). (family:curiosity)
12. **At the 680x425 preview the model is a tiny dot in a corner (Play SF9, Craft F5).** src.html:866-872 (`cx=w*.78`
    when short) and the max-height:690px layout. The lone oxygen is about 35 px across, water about 70, caffeine about
    130 px pushed into the right corner with the hint over its lower edge; the tool page's first impression is a box
    and text. Seen: audit size-680x425.png, state-water-680x425.png, state-water-800x500.png, play/f2/n05. Fixed: in
    short windows frame the model larger and nearer the well's centre of the free area, and keep the hint clear of it.
    (general)
13. **Read leaves out the hint and is not shaped for speech (Play SF10, Craft F6).** readText() src.html:745-747. On
    the first screen Read speaks the readout but not the hint, so a non-reader never hears what to do (CODEX-CURIOSITY:
    the hint is spoken once, then when Read is pressed). The text is screen glyphs: "C₈H₁₀N₄O₂", middle dots, "°", a
    doubled period ("Straight model.. Si"), capitals. The angle is only read with exactly two neighbours. Seen:
    craft/voice1.py, play/f3/d04, audit row 12. Fixed: build a spoken string ("C 8, H 10, N 4, O 2. Caffeine. All spots
    full. Selected: oxygen, 2 bonds, about 104 degrees."), include the hint while it is showing, and include the
    angle whenever the selected atom has one. (general)
14. **Spheres / Sticks button reports the wrong state to a screen reader.** src.html:688. The label flips to the other
    mode and aria-pressed flips too, so with spheres showing it announces "Sticks, toggle button, pressed". Fixed: one
    fixed label "Spheres" with aria-pressed, or (with Polish 8, a real two-position switch) a switch that
    announces its current position. (general)
15. **Na plus Cl in Forge contradicts itself.** src.html:709. The strip reads "ClNa · NOT IN THIS GUIDE" while the
    result line says "Na⁺ Cl⁻ · an ion pair. Grow salt in Crystal." and the guide has a Salt page (play/f3/d03). Fixed:
    the strip name reads "Ion pair" (or "salt, as one ion pair"), never NOT IN THIS GUIDE for this special card.
    (family:curiosity)
16. **Other no-grow messages do not match the seed (Play SF7, Craft polish 11).** src.html:574-582. Na + Na gets "These
    do not build a crystal in this forge. Try one atom of each alone." though Na alone grows sodium metal (play/f2/c10);
    a single H, O, N, S or Cl gets "Two of these close up into a small molecule" with one atom on the plate (f2/c12).
    Fixed: each line names what to try for that seed (Na + Na: "Sodium metal grows from one sodium atom."; one H, O,
    N, S or Cl: "Hydrogen pairs into a small molecule. Nothing to grow." with the element named). Blocker 2 covers the
    silicon lines. (family:curiosity)
17. **Words do not match the state: plurals and case.** src.html:670, 685, 706, 1047, selectedInfo. "1 SPOTS OPEN"
    (play/f1/p01, craft/v-firstH.png), "1 lone pairs" (f1/p06), tray labels "Hydrogen · 1 spots", "Sodium · 0 spots",
    "Bench switch: forge", "Na · sodium" lower case beside capitalised atoms, also-known names lower case in the strip
    ("formaldehyde", f3/d06). Fixed: singular for 1, and the capitalisation used everywhere else. (general)

## Polish accepted
1. **Drags show the snap.** src.html:1000-1010, 1053-1064. Dragging a tray ball or model atom draws nothing until
   release (play/f3/d01, d02). Draw a ball following the pointer, light the target peg, and stretch the would-be bond.
2. **A second structure does not shrink the first.** A stray atom is parked 300+ pm away and the view reframes, so
   water drops from about 110 px to 55 px (play/f1/p02 vs p03, p04). Park new structures closer or frame the one in
   focus.
3. **NOT IN THIS GUIDE only once a structure is closed.** After the first tap the strip reads "HO · NOT IN THIS GUIDE"
   (play/f1/p01), which sounds like "wrong" mid-build. Leave the name blank while spots are open; keep NOT IN THIS
   GUIDE for closed inventions (f1/p10, Done when 2).
4. **Current reads at projector distance.** The battery's left wire runs through the specimen and flow, a little and
   none look alike (play/f2/c06). Wires stop at the faces; a brighter carrier stream for flow, a sparse one for a
   little, none for none.
5. **The empty seed plate says what to do.** play/f2/c01: a bare ellipse, Grow disabled. Engrave "TAP AN ATOM, THEN
   GROW" on the stand (a first-run style line on the instrument, gone once a seed is on it).
6. **The inspected crystal atom is visible after Grow.** Atom 1's cyan ring is lost among 525 balls (play/f2/c03,
   audit state-salt-1366x768.png). Start inspection on an atom near the viewer.
7. **Manual find on isomers by tap order.** C, O, C taps always make ethanol (play/f1/p08); O, C, H, H, H, C makes
   dimethyl ether. Add a short find: "The order you tap decides which isomer you get."
8. **Instrument controls.** src.html:17-22, 199, 209-217. The bench switch, Sticks / Spheres, Show and Cut open are flat
   web buttons. A two-position slide switch for Forge / Crystal and Sticks / Spheres, and lit keys for Show and Cut
   open, keyboard operable and announcing their value (CODEX-CURIOSITY "Real controls"; spec "slide the bench switch").
9. **Sound per outcome.** src.html:592, 623, 633. Push plays one sound for five outcomes; Current one blip. Use the
   spec's palette: crack, bend ring, hold clink, slide swish, current hum or one spark (tones, not voice).
10. **Tab order: bench controls before model atoms.** src.html:203. 18 Tabs from Hydrogen to Undo with 3 atoms, about
    55 with 40 (craft/kb.py). Move `#atomkeys` after the controls in the DOM / tab order.
11. **Field guide at short heights.** src.html:97, 104. At 680x425 the page is all picture; name, fact and sources are
    below an unmarked scroll (audit state-guide-680x425.png, state-guide-1366x768.png). Cap the picture height in short
    windows or put name and fact above it.
12. **Test line in plain words.** src.html:630. "No current. No mobile carriers in this model." becomes "No current.
    Nothing here can move to carry charge."
13. **Crystal counts name what they count.** Salt reads "392 ATOMS" (they are ions); silica "83 INSIDE" counts only
    Si though inside O atoms are inside too (checks.json `crys`). "392 IONS"; count every inside atom.
14. **Live region writes only on change.** src.html:205, 711, 889. The polite `#readout` is rewritten every frame
    during Grow and every sync.
15. **Canvas font fallback.** src.html:962, 966. `'11px Consolas'` and `'15px Consolas'` gain `, monospace`
    (Chromebooks have no Consolas).
16. **OpenStax links go to openstax.org.** The Manual's OpenStax links point at a personal college mirror
    (ic.arc.losrios.edu/~paynem). Link the openstax.org book sections instead and state the licence shown there.

## Settled calls
- **Spoken lines deferred (BASELINE 18).** The spec's molecule name on first close ("Water.") and the Push / Current
  result lines are not fix items this round; Curiosity voice is one collective Forge effort. Note for that pass: queue
  the name from `edited()` (src.html:453-465) on the first close of each molecule this visit, and the result line from
  `push()` / `current()` (src.html:610-634); both are event lines. Codex does not record or add them now. The visual
  close (Should fix 1) is in scope. The existing hint line's timing (Should fix 2) and Read (Should fix 13) are fixes
  to behaviour already built, so they are in scope.
- **Silicon carbide: blocker, not should fix.** Play asked Teaching to weigh it; Teaching did not see it. Settled under
  the misleading-readout rule (REFINE.md): a no-grow line that states a false fact about a real material is a blocker.
  The fix is honest wording, not a new crystal.
- **Manual finds: should fix, not polish.** Teaching called it polish, Play should fix. A month of depth is one of the
  Curiosity qualities and the spec lists all nine; settled as should fix.
- **Plurals: should fix, not nit.** Teaching and Craft called them nits, Play should fix. "1 SPOTS OPEN" is on screen
  after the very first tap; words must match the state.
- **First-run hint tag.** Play tagged it general, Craft family:curiosity; kept as general (any tool's hint can do this).
- **Illustration credit stays.** Craft asked whether the Manual's "Illustrations generated with OpenAI gpt-image"
  credit breaks BASELINE 15. It is the source credit CODEX-BUILD.md:128-129 requires, not marketing copy; keep it.
- **Do not change:** the no-score, no-goal, no-"found" field guide (all lenses passed it); the full-screen well (all
  audit "overlap #stage" rows are noise); modal drawers making the bench inert; Hill order on the strip (see open
  questions); the Na+ Cl- ion pair, O=Si=O, O3 ring and Cu-Cu special cards and their honesty lines.

## To the spec's open questions
- **Hill order against familiar formulas.** The strip shows H3N, ClH, ClNa, O2Si while guide pages say NH3, HCl, NaCl,
  SiO2 (checks.json `nh3`, `nacl`; play/f3/d05). The spec and Done when 3 fix Hill order; showing the conventional
  formula when the guide knows the molecule would change the spec. Lean: conventional formula on the strip for known
  molecules, Hill for inventions, with the Manual's Hill note kept.
- **Silicon carbide as an eighth crystal (Si + C seed, diamond pattern)?** Would add a page and a growth rule. Lean: no
  for now; the honest no-grow line (Blocker 2) is enough.

## Not taken
- match() stall of about 100 ms at 40 atoms under 4x slowdown (Craft nit 14): a rare edit, fix not clearly cheap.
- Top of a grown crystal under the bench buttons at 760x900 (Craft nit 16): minor; re-look after the framing fix in
  Should fix 12.
- Hint wraps to a lone "on." at 375 (Play nit 3): the new wording in Should fix 2 changes the line; re-look then.
- prompts.json stub descriptions (Craft nit 17): not student-facing.
