# Teaching lens: living-pond (Curiosity No. 13), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms.
Module: science-5-food-webs-and-matter-cycles (5-LS1-1, 5-LS2-1, 5-PS3-1); reaches 3-LS4-2, 3-LS4-3, MS-LS2-1,
MS-LS2-2, MS-LS2-3, MS-LS4-4, MS-LS4-6.

How I checked: the model script (src.html:342-600, which exports itself) run headless in Node for every Done-when
scenario and every "Things people have found" number (scratch: S:/CurioClass-codex-scratch/living-pond/teaching/sim.js,
sim2.js); the bundle driven with scripts/drive.py on port 9411 (frames in
S:/CurioClass-codex-scratch/living-pond/teaching/frames/); sources checked on the web.

Counts: blocker 0, should fix 7, polish 3, nit 2.

## Findings

1. **should fix, family:curiosity.** Where: chart and tray counts (src.html:539 `A:(s.p[1]+s.p[2])/5`, counts() at
   :762). What: the Algae trace and count add floating and stem algae together, so the headline cascade (net the
   minnows, floating algae bloom, they shade the stem algae, the snails starve) shows on the recorder as "algae up,
   snails down", the opposite of what a grade 5 student expects, with the cause invisible. Stem algae drop from about
   46 to 3 units while the Algae line climbs; the only sign is the faint fade of the stem sprites. How seen:
   frames/t-netminnows.png (net all minnows at Y1 W13, run 45 weeks); Node run: Af 245 to 440, As 45.7 to 3.3, snails
   31.5 to 0. Better: two algae traces or chips (floating, on stems), or the stem share in the tray label.

2. **should fix, family:curiosity.** Where: drawWeb (src.html:1443-1492) and hitboxes (:1239-1246). What: only floating
   algae clumps are tappable as "algae", so the snail's and the turtle's food arrows start at a floating clump at the
   surface, while the model and the Manual's table say both eat algae on stems. It teaches the wrong link in the very
   chain finding 1 depends on. How seen: frames/t-turtle-inspect.png (turtle arrow from "Algae" at the surface); code.

3. **should fix, family:curiosity.** Where: Manual, "Food can slow the shade drift" (src.html:303). What: "With Some
   feeding, the average was 2.10" is true, but by then the Some pond has had winterkill conditions in 6 of 10 winters
   and holds 0.86 minnows; the entry presents it as green water hiding fish and never says the school was nearly wiped
   out each winter. A student who repeats the run sees Minnows 40 one week and near 1 the next and cannot square it with
   the entry. How seen: Node (winterkills 6, minnow count 0.86 at Y10 end); frames/t-feeder-some-y9.png (Y9 W49, O2
   1.5 mg/L, log "Winterkill conditions"). Better: name the winterkills in the entry, or use a feeding level that keeps
   the school.

4. **should fix, family:curiosity.** Where: Manual, "Things people have found" (src.html:292-306). What: the spec's
   Manual asks for each find "in this pond, with real-world sources" (Carpenter, Kitchell and Hodgson 1985 for the
   cascade; Minnesota DNR for winterkill; Lindeman 1942 and OpenStax 46.2 for the energy shares; Endler 1980 for the
   shade drift; Cornell Lab for the heron). The built entries keep only "this is a model result, not a measurement".
   Honest, but the student never learns that real lakes do the same thing, which is what turns a toy run into
   5-PS3-1 and MS-LS2-3 evidence. How seen: frames/t-manual-found.png; spec "The Manual". Better: one plain sentence
   per entry: "Real lakes do this too (source)."

5. **should fix, general.** Where: Manual throughout (src.html:259-306) and the Energy ledger. What: the language is
   pitched well above grade 5 (and hard for grades 6 to 8): "a counterfactual, not a prediction after further
   changes", "flow-weighted probabilities", "outgoing flows share a proportional limit when a pool is short", "Algae
   net production subtracts their respiration; grazer net production subtracts body maintenance from growth",
   "inherited shade shares drift", ledger "STORES USED", "GRAZERS NET". How seen: frames/t-manual-found.png,
   frames/t-energy-y10.png. Better: plain words ("the dashed line is the pond you didn't change"; "kept in algae after
   they breathe"; "plant eaters"), with the exact terms kept for the honesty paragraph.

6. **should fix, family:curiosity.** Where: Matter lens and Manual "Model and honesty" (src.html:281). What: 5-LS1-1
   asks students to argue that plants get their growing material chiefly from air and water, not soil. Here the pool
   is "Water & air", which the Manual says also holds the nutrients, and a muck dot's trip runs Muck, Water & air,
   Algae. Nothing on screen lets a student say "the algae's body came mostly from air and water, not from the mud";
   a student could as easily conclude the algae are built from rotted muck. How seen: Matter trips from
   frames/t-matter-trip.png run ("Muck > Decomposers > Water & air > Floating algae > Minnow > Muck"); Manual text.
   Better: in the Manual and the algae inspect label, say algae build from carbon dioxide (air) and water with sunlight,
   and that the nutrients from muck are a small share lumped into this pool. If that can't be shown honestly, 5-LS1-1
   is mentioned, not taught (rule 2).

7. **should fix, family:curiosity.** Where: shade strip (src.html:243, sync :808). What: MS-LS4-6 (a reach code) asks
   for a mathematical representation of a trait changing over generations. The tool shows only the current AVG SHADE;
   there is no history of it, so the drift the Manual describes over ten winters can only be seen by writing numbers
   down. How seen: frames/t-shade-y10.png (AVG SHADE 1.21, no record of earlier values; Whole run shows populations
   only). Better: an optional shade trace on the recorder (a chip like the population chips), or drop the MS-LS4-6
   reach. MS-LS4-4 and 3-LS4-2 are fine as they stand.

8. **polish, family:curiosity.** Where: updateTracker and the decomposer flows (src.html:434-441, 1098-1110). What: 80
   percent of what decomposers break down goes straight from Muck to Water & air (as their breath), so most trips read
   "Muck > Water & air" and skip the decomposers, the very role 5-LS2-1 names. How seen: three of four trips in the
   t-matter-trip run. Better: label that step "Muck > broken down by decomposers > Water & air".

9. **polish, family:curiosity.** Where: Energy ledger (sync, src.html:816-822). What: the ledger shows only the year so
   far and resets at week 0, so "heat out against caught" reads 88 percent at week 32 and only nears 100 in the last
   weeks; at Fast a student rarely sees the closed year. The model already keeps `lastEnergy`. How seen:
   frames/t-energy-y10.png (88.1 percent at Y10 W32); Node: last full year 99.9 percent. Better: a "last year" line.

10. **polish, family:curiosity.** Where: drawEnergy (src.html:1432-1441). What: the sunlight arrows, four heat columns
    and the green "kept" arrow carry no labels, and the heat columns are grouped by the pool the matter leaves, so an
    eater's digestive breathing is drawn on its prey's column and decomposers breaking down muck (the largest heat
    source) has no column at all. How seen: frames/t-energy-y10.png; code. Better: small labels (Sun, Algae, Snails,
    Minnows, Decomposers) and heat attributed to the eater.

11. **nit, family:curiosity.** Manual, "Muck can hold most of the matter": "algae above 100 units after 11 weeks" is
    true (Node: 11 weeks), but the chart and tray show clumps, so the student sees 20. Say "20 clumps (100 units)".

12. **nit, family:curiosity.** drawWeb gives the turtle and heron no arrow to Muck, though the model sends 30 percent
    of what they eat there (src.html:449, 458).

Nothing cultural, Native or hard-history: no sensitivity review needed. No giveaway concerns (no quiz or hidden
answer). No score, goal, level, sticker or finish screen found (lesson-creep grep on src.html: no hits beyond two uses
of "level" in oxygen prose).

## Done when (the teaching-relevant ones, tested)

| # | Result | Evidence |
|---|---|---|
| 1 | PASS | Opens running; ice from week 41, about 19 s at Normal from week 3 (T < 4 for weeks 41 to 51). |
| 2 | PASS | Node, Starter 520 weeks: all six kinds kept, total 742.000 (drift 4e-12), year 10 snail counts 21 to 36 ("about 19 to 34"). |
| 3 | PASS | Net all minnows Y1 W13: floating algae 440 by W30, snails 4.7 vs ghost 9.5 by W30, heron off W15, turtle off W25. |
| 4 | PASS | Decomposers off: muck 92.1 percent at Y1 end; turtle walked off W33, before any kind went; back on, algae past 100 units in 11 weeks. |
| 5 | PASS (see finding 3) | Lots for two summers: winterkill Y2 W48, minnows gone W109. Some: minnows survive ten winters but with 6 winterkills, 0.86 left. Sand 3.50 to 2.27 by Y3 end; gravel 3.50 all ten years. |
| 6 | PASS (see finding 9) | Muck trip reaches Minnow; last full year heat 99.9 percent of caught; mid-year ledger 88 percent. |
| 7 | PASS | Canopy 25: all six kept; 50: nymphs gone Y3 W25; Cold: nymphs gone Y3 W43; Mild: no ice, all kept; each 742.00. |

## Facts checked against a second source (13)

All Manual numbers recomputed in Node and matched: 1.03 percent caught, 9.65 percent grazers, nymph-netted snail peak
73.4 vs ghost 32.8, muck 92.1 percent, 11 weeks, shades 1.22 / 2.10 / 5.78, canopy and Year outcomes. External: OpenStax
Biology 2e licence is CC BY-NC-SA 4.0 at the source, as the Manual says (the spec's "CC BY 4.0" is out of date); USGS
confirms cold water holds more oxygen and decay uses it (no mg/L table there); oxygen fit 14.6 at 0 °C and 9.6 at
20 °C against the standard freshwater table 14.6 and 9.1 (Manual states the 0.5 gap); Minnesota DNR confirms ice,
low light and decay drive winterkill and uses 2.0 mg/L as its alert line; citations Lindeman 1942 Ecology 23(4),
Holling 1959 Can. Entomol. 91, Gillooly et al. 2001 Science 293, Endler 1980 Evolution 34(1), Carpenter, Kitchell
and Hodgson 1985 BioScience 35 all correct; heron sight-hunting in shallows, painted turtles overwintering in mud and
dragonfly nymphs' extendable lower lip and fish prey match the cited pages' known content. No readout found lying;
the Manual is careful to call its numbers model results and the pond made-up.

## Frames looked at

Mine: t-default-2s, t-netminnows, t-turtle-inspect, t-energy-y1, t-energy-y10, t-manual-found, t-shade-y10,
t-feeder-some-y9, t-decomp-off, t-winterkill-lots, t-matter-trip (frames/ in my scratch). Audit: size-1366x768,
state-matter and state-energy at 1366x768.

## Audit pilot

- Leads confirmed: none that bear on teaching.
- Leads wrong (for this lens): the #pond overlap rows at every size are the full-bleed canvas under its own overlays,
  noise as the brief warned; "hint out of view" at 1366x768 is wrong, the hint shows bottom-right of the transport in
  size-1366x768.png; the "welcome not heard" rows are the first-run hint being dismissed by the first action, which is
  the Curiosity design and BASELINE rule 16.
- Missed (outside its reach): all twelve findings above, chiefly the combined algae trace hiding the cascade, the food
  arrows from the wrong algae, and the confounded feeding entry.
