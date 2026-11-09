# Play lens: molecule-forge (Curiosity No. 12), round 1

Cold lens, 2026-11-06. Played twice: as a grade 7 student alone at home, and as a teacher projecting at 1366x768.
Bundle `tools/molecule-forge/molecule-forge.html` as built. Own frames in
`S:/CurioClass-codex-scratch/molecule-forge/play/f1` to `f4` (drive.py, held clicks, port 9451; 375 wide through the
iframe host on 8875). Shared audit cited from `S:/CurioClass-codex-scratch/molecule-forge/audit-r1`.

**Counts: 0 blocker, 10 should fix, 7 polish, 4 nit.**

## Short test (Curiosity)

- **Would a kid open it unassigned?** Yes. Two taps on H and water bends and names itself (f1/p02); a carbon and Grow
  builds a 525-atom diamond shell by shell (f2/c02, c03). Real reactions with nothing read.
- **Would an adult play with it for fun?** Yes. Loading caffeine and turning it (f1/p12), closing a ring by drag
  (f3/d01: cyclopropane, "about 60°"), O=Si=O getting its special card (f3/d05) and 40 recognised extra graphs give
  real depth.
- **Is the real thing the interface?** Yes. The model is the only working surface; readouts are live formulas, angles
  and neighbour counts.
- **Does it work with no finish line?** Yes. No score, goal, level, count or "found" marks; the lesson-creep word
  search on src.html hits only the Manual heading "Things people have found". The field guide lists all 39 pages.

Passes all four. The flaws below are about the moments between taps, not the shape.

## Should fix

1. **The closing moment is flat.** Forge, `src.html:453-465` (`edited()`). The spec's payoff for the first two
   minutes is a cyan ring pulsing out, the guide tab lighting with the name, and the name spoken ("Water."). The build
   plays a three-note tone and glides to the conformer; the only visible change is the readout name. No ring, the
   Field guide button never changes, and no name is spoken (`voice/lines.json` holds only the hint; no `V.say`
   anywhere). Crystal test results are not spoken either. Seen on f1/p02 and audit state-water-1366x768.png; source
   check. The spoken name can wait for the shared voice pass (BASELINE 18), but the ring and the lit guide tab are
   visual and should land now. Tag: family:curiosity.
2. **The one hint vanishes on the wrong tap and is spoken stale.** `src.html:1217-1222`: any click anywhere (except
   Read and Sound) hides the hint. Tapping the red oxygen in the well, the most obvious "atom" on screen, adds nothing
   and removes the only instruction (f4/h01: hint hidden, 1 atom); so does Motion (f4/h02). When the first tap *does*
   add H, the voice then says "Tap an atom to snap it on." after the student already did it (f1/p01 voice log; audit
   one-click rows 1 to 9). Better: hide the hint on the first atom actually added; speak it only when the first gesture
   did not add one; word it "Tap an atom in the tray to snap it on." since the oxygen is an atom too. Tag: general.
3. **A stray tray tap in Crystal silently wipes the grown crystal.** `src.html:499-501`: with a one-atom seed, any
   tray tap adds to the seed and sets `crystal=null`. After growing diamond, one tap on H leaves "C · H, Seed plate"
   and an empty bench (f2/c15). The Undo button is hidden in Crystal (`src.html:687`), so only Ctrl+Z gets the diamond
   back, and Grow now refuses ("This closes into a molecule"). Show Undo in Crystal too, or keep the grown specimen
   until Clear seed. Tag: general.
4. **Push outcomes look alike, so the comparison does not land.** Crystal, `src.html:878-883`. Copper "bends" and
   graphite "slides" both draw as the top half translated sideways (f2/c07, f2/c08); the copper frame reads as a
   shear with long stretched bonds, not a bend. Diamond's push goes out and back (`65*sin`), so the end state (and a
   tap mid-test) looks untouched while the strip says "64 bonds cross this cut and none let go" (f2/c05); the spec's
   "count the bonds that hold" has nothing to count. Highlight the crossing bonds at the end, and give bend, slide and
   crack distinct end shapes. Tag: family:curiosity.
5. **Plurals do not match counts.** "1 SPOTS OPEN" (f1/p04, f1/p01), "1 lone pairs" (f1/p06 ammonia), tray labels
   "Hydrogen · 1 spots", "Sodium · 0 spots" (audit control names). `src.html:670, 706, 1047`. POLISH "Words match the
   state". Tag: general.
6. **Na plus Cl in Forge contradicts itself.** The strip reads "ClNa · NOT IN THIS GUIDE" while the result line says
   "Na⁺ Cl⁻ · an ion pair. Grow salt in Crystal." and the guide has a Salt page under NaCl (f3/d03; `src.html:709`).
   Show "Ion pair" (or "Salt, as one ion pair") and NaCl. Tag: family:curiosity.
7. **No-grow messages fail the cheap sweep.** `src.html:574-582`. Na + Na is refused with "These do not build a
   crystal in this forge. Try one atom of each alone." although Na alone grows sodium metal and Cu + Cu grows copper
   (f2/c10). Si + C is told "This closes into a molecule. Grow carbon alone, or two carbons." (f2/c11); silicon carbide
   is a real diamond-pattern network, so this line is untrue (the Teaching lens should weigh it against the Curiosity
   rule on readouts that lie). A single S, H or O seed gets "Two of these close up into a small molecule" (f2/c12).
   Tag: family:curiosity.
8. **"Things people have found" was cut to four sentences.** Manual, `src.html:272-273`. The spec lists nine short
   finds with sources (lone pairs squeeze the angle 109.5 / 107 / 104.5; 78 °C against -24.8 °C; 92 legal C/N/O
   structures with 56 unnamed; the pencil; crack against bend; CO2 against SiO2; silicon warm; Wöhler 1828). This is
   the month-of-use depth a Curiosity is judged on, and the 92/56 one invites inventing. Restore them as short
   separate entries. Tag: family:curiosity.
9. **The 16:10 preview shows a tiny model.** At 680x425 caffeine is drawn about 130 px wide, pushed into the right
   corner (`src.html:867-868`, `cx=w*.78` when short), smaller than the tray, with the hint text over its lower edge
   (f2/n05; audit size-680x425.png for the lone oxygen). The preview beside "Play full screen" is the tool page's first
   impression. Tag: general.
10. **Read speaks what a voice will misread.** `readText()` (`src.html:745-747`) sends "C₈H₁₀N₄O₂. Caffeine. ALL
    SPOTS FULL. O · Oxygen 2 spots · 2 filled..." (f3/d04; audit row 12 for oxygen). Subscript digits, middle dots
    and capitals in a projected class are a garble; the spec also asks Read for the angle, which is only included when
    the selected atom has two neighbours. Spell formulas out ("C 8, H 10, N 4, O 2") and say "all spots full".
    Tag: general.

## Polish

1. **Drags give no feedback until release.** `src.html:1000-1010, 1053-1064`. Dragging a tray ball or a model atom
   draws nothing: no ghost ball, no lit peg, no stretched bond; the result just appears on release (f3/d01, f3/d02
   worked, but blind). A model kit is all about the snap; a ball following the pointer and the target peg lighting
   would make ring closing discoverable.
2. **A second structure shrinks the first.** A lone atom is placed 300+ pm away and the view reframes to both, so
   water drops from about 110 px to 55 px wide in a mostly empty well (f1/p02 against f1/p03, f1/p04). Frame the
   structure in focus, or park the stray atom closer.
3. **"NOT IN THIS GUIDE" mid-build.** After the very first tap the strip reads "HO · NOT IN THIS GUIDE"
   (f1/p01): to a student building water it sounds like "wrong". Leave the name blank (or "BUILDING") until every spot
   is full; keep NOT IN THIS GUIDE for closed inventions, where it is a good moment (f1/p10).
4. **Current barely shows.** The battery's left wire is drawn straight through the specimen (f2/c06), and flow (14
   small dots), "a little" (3) and none are hard to tell apart at projector distance. A brighter carrier stream and
   wires that stop at the faces would let "a sea, a little, none" read without the strip.
5. **The empty seed plate is a bare ellipse with no next step.** f2/c01: "SEED PLATE · EMPTY", Grow disabled, nothing
   on the plate says to tap an atom. The spec wants a small specimen stand; an engraved "TAP AN ATOM, THEN GROW" on
   it would name the action without breaking the Curiosity rules. Tag: family:curiosity.
6. **The inspected crystal atom is buried.** After Grow, atom 1 sits in the middle and its cyan ring is lost among
   525 balls (f2/c03, audit state-salt-1366x768.png) until Cut open. Start inspection on an atom near the viewer, or
   auto-cut briefly on the first tap.
7. **Ether by taps.** C, O, C taps always make ethanol (f1/p08) because the next atom joins the most open spot. O, C,
   H, H, H, C does make dimethyl ether. A Manual find ("the order you tap decides which isomer you get") turns this
   into a discovery instead of a dead end.

## Nit

1. Also-known names show lower case in the strip ("formaldehyde", f3/d06) beside "Water", "Ethanol".
2. Keyboard path T, 2, G leaves the Forge hint "Tap an atom to snap it on." on screen over the grown diamond
   (f4/h03); the hint only hides on a click.
3. At 375 wide the hint wraps to a lone "on." (f2/n01).
4. Silica-style formulas read "O₂Si" in the strip and "SiO₂" in the guide (f3/d05); the Manual explains Hill order,
   but a student comparing the two sees a mismatch.

## Checked and fine

First screen at every size (audit size-*.png), water and H2 by taps (f1/p02 to p04), methane about 109° and ammonia
about 106° after the glide (f1/p05, p06), CO2 at 180° (f1/p09), 40-atom cap message (f1/p11), caffeine and benzene
loads (f1/p12, p14; f3/d07), Spheres (f1/p13), all seven crystals grow to their stated counts, salt cracks with a gap
and 5 neighbours at the face (audit state-salt-fracture), graphite and silica messages (f2/c08, c09), Show with Motion
off keeps the 30° buttons (f3/d07), 375 Forge and Crystal layouts (f2/n01 to n04). Frame times during Crystal Show at
1x: median 16.7 ms (f4/h04; Craft owns the 4x check).

## Audit pilot

- **Leads confirmed:** the "spoken" column showing the hint after an atom tap (rows 1 to 9) is the stale-hint problem
  in should fix 2.
- **Leads wrong (noise):** every "overlap #stage / ..." row at every size (the well is a full-screen canvas with the
  tray, power panel and readouts laid over it by design); "hint out of view" in every state (the hint hides after the
  first click by design); guide "Close / h2" overlap (the Close button sits beside the heading, no overlap on
  state-guide-1366x768.png); "keep region hidden" for the guide and Manual (modal drawers make the bench inert);
  "choices cut short" for the USGS and NASA links (source links further down a scrolling page, not choices).
- **Missed:** the flat closing moment, plurals, the crystal wiped by a stray tap, look-alike Push outcomes, the Na Cl
  readout contradiction, wrong no-grow messages, the cut Manual finds, the tiny 680x425 model and the Read text.
  None of these are mechanical-layout leads.

Nothing here is cultural, Native or hard history; no sensitivity review needed from this lens.
