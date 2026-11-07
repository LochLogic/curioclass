OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 16 (general 7, family 9), polish accepted 22

# Refine: living-pond

Merged from refine/teaching.md, refine/play.md and refine/craft.md (round 1). Frame folders, all under
`S:/CurioClass-codex-scratch/living-pond/`: Teaching `teaching/frames/`, Play `play/shots/`, Craft `craft/`
(run1 to run4, z-*.png crops), shared audit `audit-r1/`. The short test passes in all three lenses; no score, goal,
level, sticker or finish screen was found. Integrator spot-checked items 1, 4, 5, 7 and 10 in src.html (cited lines
confirmed).

## Blocker
None.

## Should fix
1. **The pond's drama is silent: none of the spec's event lines exist.** src.html:622 (`L` holds only `hint`),
   voice/lines.json (one line), events written only by `logEvent` (src.html:375-524) into the Manual's pond log.
   Craft ran 136 weeks with the feeder on Lots: two freezes, a winterkill and "Heron flew off" were logged and the voice
   said only the hint (craft/run1/voice-events); Play saw the same at year 2 week 50, 0.6 mg/L (play/shots/feeder-lots.png).
   Fixed: add the spec's event lines as `V.say` events ("Ice. No new air gets in until spring.", "Oxygen's low. The
   minnows are gasping at the top.", a winterkill line, heron left, turtle left, "The snails are gone."), each at most
   once in 20 s, maxAge 4 s, with a `valid` that the event is still true; add them to voice/lines.json word for word.
   Plain statements of what happened, never praise. (family:curiosity)
2. **Seven controls are browser dropdowns, not instrument controls.** src.html:228, 230, 240-244 (Speed, Lens, Feeder,
   Bottom, Decomposers, Canopy, Year are native `<select>`). The bottom third reads as a settings form
   (audit-r1/size-1366x768.png, play/shots/*). CODEX-CURIOSITY "Real controls" and the spec ("Canopy dial", "Year
   dial", Decomposers `On` / `Off`) ask for dials and switches. Fixed: detented rotary switches with the value printed
   on them for speed, lens, feeder, bottom, canopy and year, a lever toggle for decomposers; arrow keys step each, each
   announces its value, a soft click on Sound; same values and keys (< >, L) as now. (family:curiosity)
3. **The Algae trace hides the cascade.** src.html:539 (`A:(s.p[1]+s.p[2])/5`), counts() at :762. Floating and stem
   algae are summed, so "net the minnows" reads as "algae up, snails down" with the cause invisible: stem algae fall
   from about 46 to 3.3 while the line climbs (teaching/frames/t-netminnows.png; Node: Af 245 to 440, As 45.7 to 3.3,
   snails 31.5 to 0). Fixed: show the two apart, either two algae traces (floating, on stems) with their own chips and
   end labels, or at least the stem share on the tray and in the counts. (family:curiosity)
4. **Snail and turtle food arrows start at the wrong algae.** src.html:1239-1248 (only floating clumps get hitboxes;
   the stem sprites at :1248 get none) and drawWeb (:1443-1492). The arrows run from a floating clump at the surface
   while the model and the Manual say snails and the turtle eat algae on stems (teaching/frames/t-turtle-inspect.png).
   Fixed: give the stem algae hitboxes (kind "stem algae") and draw the snail and turtle arrows from them. (family:curiosity)
5. **No first-run hint on screen below 900 px.** src.html:142 (`#hint{display:none}` under max-width 900). At 680x425,
   800x500, 760x900 and 375x812 the student gets no instruction before acting, and voice speaks only after a touch
   (audit-r1/size-680x425.png, size-760x900.png, size-375x812 (iframe host).png; play/shots/narrow-680-winter.png).
   Fixed: the one-line hint on the tank rim at every size (a short form such as "Tap a creature below" where room is
   tight). (general)
6. **The spoken hint arrives after the action it describes.** src.html:662-667 (`afterTouch`). If the first touch was
   a tray tap, the student hears "Tap a creature to drop it in." 1.4 s after doing it (craft/run1/voice-adds; audit
   held-click rows 6 to 13). Fixed: skip the line when the first touch was itself an Add or Food tap (its `valid`
   checks that nothing has been dropped yet); otherwise it stays as the spec says, once after the first touch.
   (family:curiosity)
7. **"Whole run" turns invisible when on.** src.html:42 and 85: `button[aria-pressed=true]` sets white text, then
   `.chartbar button` (same specificity, later) sets a transparent background, so the pressed label is white on cream
   paper (craft/z-whole.png, play/shots/year10-whole.png). Fixed: a pressed style for chart-bar buttons with its own
   dark fill (`#0b4f56` with white) or an inked underline. (general)
8. **The oxygen meter has no marks at 3 and 2.** src.html:1597-1619. Ticks only at 0, 5, 10, 15, 20; "3 gasp / 2 kill"
   is a loose 10 px caption in the corner, dropped entirely when the meter is under 120 px (680x425 frames). Fixed:
   a shaded red band 0 to 3 on the arc with labelled ticks at 3 "fish gasp" and 2 "winterkill", as the spec's
   readouts say, kept at short sizes. (general)
9. **The Energy ledger zeroes the moment the year ends.** src.html:531-535 (yearly reset), sync() :816-822. At week 51
   heat out is 102 percent of caught; one week later every line reads 0 and "0.0% OF SUN" (play/shots/energy-yr1.png);
   mid-year it reads 88 percent (teaching/frames/t-energy-y10.png). Thing to do 4 is "a whole year". `s.lastEnergy` is
   kept but never shown. Fixed: a "last year" line (or column) beside this year's, shown once a year has closed. (general)
10. **Following a matter dot is a long flat wait, and the keyboard can only follow muck.** src.html:1765 (Enter in
    Matter always `follow(14)`), `follow`/`updateTracker` :1092-1110. Play followed a dot from each of 8 pools for 52
    weeks: only animal-start dots touched an animal; the muck dot stayed "Muck" 26 weeks (play/shots/matter-follow.png).
    Fixed: Enter follows the dot nearest the arrow-key drop point (as Life does with `inspectCreature`), and the trip box
    shows how many weeks the dot has been where it is. Do not change the model's flows (see Settled calls). (general)
11. **The Manual reads as a model specification, above grade 5.** Manual `#manualbody` (src.html:259-306) and the Energy
    ledger labels. "a counterfactual, not a prediction after further changes", "flow-weighted probabilities",
    "outgoing flows share a proportional limit", "Caught is gross algae growth x 10", ledger "STORES USED", "GRAZERS NET"
    (teaching/frames/t-manual-found.png, t-energy-y10.png). Fixed: each section opens with a plain grade 5 paragraph
    ("the dashed line is the pond you didn't change", "kept in algae after they breathe", "plant eaters"), model detail
    below it for adults; ledger labels in plain words. Exact terms stay in the honesty paragraph. (general)
12. **The feeding entry hides the winterkills.** Manual "Food can slow the shade drift" (src.html:303). "With Some
    feeding, the average was 2.10" is true, but that pond had winterkill conditions in 6 of 10 winters and holds 0.86
    minnows by year 10 (Node; teaching/frames/t-feeder-some-y9.png, Y9 W49, 1.5 mg/L). Fixed: name the winterkills in
    the entry, or report a feeding level that keeps the school; numbers from the build's own runs. (family:curiosity)
13. **"Things people have found" lost their real-world sources.** Manual src.html:292-306. The spec asks each find "in
    this pond, with real-world sources" (Carpenter, Kitchell and Hodgson 1985 cascade; Minnesota DNR winterkill;
    Lindeman 1942 and OpenStax 46.2 energy shares; Endler 1980 shade drift; Cornell Lab heron; USGS oxygen). Fixed: one
    plain sentence per entry, "Real lakes do this too (source).", keeping "this is a model result". (family:curiosity)
14. **5-LS1-1 is not visible: nothing says algae are built from air and water.** Manual "Model and honesty"
    (src.html:281) and the algae inspect label. The pool is "Water & air" and also holds nutrients; a trip like "Muck >
    Decomposers > Water & air > Floating algae" lets a student conclude algae are built from rotted muck
    (teaching/frames/t-matter-trip.png). Fixed: the Manual and the algae inspect label say algae build their bodies from
    carbon dioxide (air) and water using sunlight, and that the nutrients from muck are a small share lumped into this
    pool. (family:curiosity)
15. **The shade drift has no history (MS-LS4-6).** Shade strip src.html:243, sync :808. Only the current AVG SHADE is
    shown; the drift over ten winters can only be seen by writing numbers down (teaching/frames/t-shade-y10.png).
    Fixed: an optional AVG SHADE trace on the recorder, a chip like the population chips, off by default, own dash and
    end label. (family:curiosity)
16. **Status grammar.** src.html:716: "The pond is full of minnow." / heron / turtle / snail. Fixed: plurals ("The pond
    is full of minnows.") or "No room for more minnows." (general)

## Polish accepted
1. **Latest event on the tank.** A one-line monospace readout on the tank rim showing the newest pond-log line (from
   `logEvent`), so a student with Sound off still sees "Ice. New air is sealed out." or "Heron flew off." The Manual's
   pond log stays the record. (play/shots/feeder-lots.png) (general)
2. **Energy diagram labels.** drawEnergy src.html:1432-1441: small labels on the sun arrows, heat columns and "kept"
   arrow (Sun, Algae, Snails, Minnows, Decomposers); attribute an eater's heat to the eater, and give decomposers'
   breakdown of muck its own heat column (teaching/frames/t-energy-y10.png). (family:curiosity)
3. **Matter trip names the decomposers.** updateTracker src.html:434-441, 1098-1110: write the Muck to Water & air step
   as "Muck > broken down by decomposers > Water & air". (family:curiosity)
4. **Ghost lines easier to tell from real lines.** src.html:611, 1538: ghosts much paler (about 0.35 alpha) or thin
   dotted grey (play/shots/net-all-minnows.png). (general)
5. **Tray labels.** src.html:784: "36 · 1 = 1" becomes "36"; show "1 = N" only when N is above 1; no wrap in net mode
   (play/shots/net-swipe.png). Keep the "1 = N" key Done when 10 needs. (general)
6. **Winter looks like winter.** drawTank ice: a thicker ice sheet creeping from the edges, a darker, dimmer water column
   under ice, slower fish (play/shots/ice-winter.png). Motion off: no movement change needed beyond the colour. (general)
7. **Chart readable when projected.** End labels and legend larger at 1280 px wide and up; the dial's labels likewise. (general)
8. **Frame-rate headroom.** src.html:1781 redraws chart and oxygen canvases every frame: redraw them only on `advance()`
   or a change; skip the tank redraw with Motion off; compute the net swipe's ghost once at swipe end, not per scoop
   (src.html:1670-1677; 60 ms long task measured). At 4x CPU throttle Life at the limits dropped 15 of 180 frames
   (craft/throttle.py). (general)
9. **Sounds like water.** src.html:653-661: short filtered-noise bursts for splash, net swish and ice crackle in place
   of sine blips; keep the 150 ms spacing and Fast rule. (family:curiosity)
10. **Chart room at 680x425.** src.html:155-163: fold the legend into the plot's top margin at short heights so the trace
    gets more than about 35 px; keep "13.4 mg/L" off the dial's base line (craft/z-680chart.png). (general)
11. **New, then Save.** src.html:1083-1084, 955-968: after Save in the New dialog, go on to Starter or Empty (or label
    the button "Save only") (craft/run1/new-save). (general)
12. **Habitat panel closes on Escape and an outside tap** at short screens (src.html:943-946, 1725;
    craft/run2/habitat-680.png). (general)
13. **Station label clear of the cattails.** src.html:223, 1231: move "Living Pond / FIELD STATION / 13" left of the
    reeds or draw the reeds lower (craft/z-station.png, play/shots/tap-minnow.png). (general)
14. **Compact ledgers at short heights.** At 680x425 the Matter and Energy ledgers cover about 40 percent of the tank
    (craft/run2/matter-680.png): two lines there (IN POND and the trip; caught and heat out). (general)
15. **Turtles asleep apart.** src.html:1157-1159: spread the sleeping turtles or put extras on the log
    (play/shots/limits-fps.png). (general)
16. **Empty pond label.** src.html:1363: "NO TURTLE · NO HERON" when neither was ever there, not "walked off / flew off"
    (play/shots/empty-pond.png). (general)
17. **Manual "Muck can hold most of the matter":** say "20 clumps (100 units)" to match the chart. (family:curiosity)
18. **Food web arrows to Muck** for the turtle and heron (the model sends 30 percent there, src.html:449, 458). (family:curiosity)
19. **Run button's pressed state.** src.html:773-774: drop aria-pressed or use a plain label so a screen reader does not
    hear "Hold, pressed" for a running pond; avoid the Roman numeral glyph in the accessible name. (general)
20. **Calendar "Year 1" in monospace** like the other readouts (src.html:58). (family:curiosity)
21. **Replay restores the chart speed** it found when it ends (src.html:984). (general)
22. **Tank focus ring visible**: draw it inside the canvas edge (negative outline-offset or inset ring), since `.tank`
    clips the outside one (src.html:43, 50). (general)

## Settled calls
- **Event lines stay.** CODEX-CURIOSITY says voice speaks the hint once and then only on Read; the spec lists event
  lines. They are readings of what happened (ice, low oxygen, a kind gone), not how lines, praise or goals, so the
  spec's lines are built (should fix 1). They must never coach or congratulate.
- **The hint is spoken after the first touch**, as the spec and BASELINE rule 16 say. Only the stale case (first touch
  was a stocking tap) changes (should fix 6). The audit's "welcome not heard" rows are not findings.
- **Play's "log right"** in the spec's Look means the wooden log on the right of the tank, not a pond-log strip. The
  pond log stays in the Manual; polish 1 adds only a one-line latest-event readout.
- **Do not change the model's flows** to make matter trips reach animals faster. The model is carried from git 018ace9b
  and Done when 6 passes (Teaching: a muck trip reached Minnow). Should fix 10 is about which dot is followed and
  showing the wait.
- **Manual numbers come from the build's own runs**, not the spec's summary numbers (for example muck 92.1 percent, 11
  weeks, 1.03 percent). Teaching recomputed every one in Node and they match; do not revert them.
- **Real controls (should fix 2)** keep the same values, keys and defaults; no new settings, no presets added.
- **Tag splits:** the hint below 900 px is general (Play), not family (Craft); the matter-follow item is general
  (Craft). Energy ledger reset is a should fix (Play), not polish (Teaching): it breaks thing to do 4.
- **Audit noise, not findings:** every `#pond` overlap row; "text under 10 px" on the TIME and LENS labels at 375
  (deliberately hidden, selects carry aria-labels); "keep region" for #ledger and for #run/#speed/#tray under the modal
  drawer; "hint out of view" at 1000 px and up in states (cleared by the first touch); the tray scrolling sideways at
  375 (the spec asks for a scrolling row).
- No score, goal, level, sticker or finish to add or remove; none of the fixes may add one.

## To the spec's open questions
- **MS-LS4-6 reach.** Should fix 15 adds a shade trace so the trait change is shown as numbers over generations. If
  Cory does not want a seventh chart chip, the alternative is to drop the MS-LS4-6 reach (rule 2).
- **OpenStax licence.** The spec's Sources line says OpenStax Biology 2e is CC BY 4.0; Teaching found CC BY-NC-SA 4.0
  stated at the source (the Manual already says so). The tool cites it as a source only, no text or figures reused, so
  nothing in the tool changes; the spec line should be corrected.

## Not taken
- Play 1's "log strip on the tank per spec Look": misread of the Look line; replaced by polish 1.
- Changing matter flow weights so more trips reach animals: model is fixed (Settled calls).
- Dropping MS-LS4-6 now: moved to open questions; the trace is the fix.
