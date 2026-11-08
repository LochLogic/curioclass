## What it teaches
Students can build, test, compare and combine a bridge or tower using forces and evidence. They can explain why a long squeezed beam buckles and why a stiffer tower can respond worse to a particular shake.

## Key skills
- Trace a load through a structure as pull and squeeze.
- Choose criteria and constraints from the people who use a design.
- Change one part and compare the result of the same load test.
- Use a model to compare and combine promising designs.
- Relate a tower's own sway speed to the speed of a shake.

## Support at home
- Look at a bridge from a safe public path. Ask where triangles keep its shape and where its weight goes into the ground.
- Fold paper into a flat strip and a zigzag strip. Rest each between two books and compare how it bends under a light household object.
- Notice a water tower or rooftop tank. Talk about how height helps water reach a tap, without climbing or entering restricted areas.

## A five-minute start
Open Bridge and press Go. The bare deck folds because its joints cannot hold the shape. Drag from a joint to an empty grid point, then connect that point to another joint. Keep closing triangles and test the pickup again. Choose a bigger truck when it crosses.

## Modes
Bridge starts with a bare 24 m deck. Choose a material, drag from joints to add members, or tap an existing member to change its material. Shift drag moves a free joint. Erase, Undo and Redo support revision. The arrows and double lines distinguish pull and squeeze even without color. Worst spots computes the selected truck's whole crossing, including positions between the joints. Save to Yard keeps a design on this device. Open Manual, then the yard logbook to choose a brief and inspect recorded observations.

Tower starts with two pinned table joints. Build up from them in triangles. Drag its top sideways and release to pluck it; Shift with an arrow on the grid provides a keyboard pluck. Shake uses a steady sinusoidal acceleration, with a two-second ramp and a fifteen-second test. Wind is specified at ten meters and grows with height. A tank supplies water pressure as well as mass. A lighter load changes the tower's sway speed, which can move it closer to a shake's speed.

Yard compares up to three saved designs. Test all fills the truck, wind and Valley quake results. Open changes a copy. Borrow overlays another design's members as pink ghosts; tap individual members to adopt their shape and material, or Borrow all. A matching member takes the borrowed material. The Old farm bridge sample is always available, including before the first save. It can be opened and revised as a copy; its card cannot be renamed or deleted.

## Three ways to use a period
Allow ten minutes of free play, then ask what students discovered about squeezed members. For a directed investigation, pick up a Bridge or Tower brief in the optional logbook. For a room challenge, have pairs choose every promise and compare the least expensive designs in the Yard. Students can compare by swapping laptops; there is no transfer code or upload.

## Talk questions
- Which member changes from pull to squeeze as the truck passes? What happens if it is a cable?
- Did making the bridge deeper shorten or lengthen the member that failed?
- Did the heavier truck put more force into every design? How did its axle spacing matter?
- Which promised result did a pier improve, and which promises did it break?
- If a tower failed, did changing its material move its sway speed toward the shake or away from it?
- What part would you borrow from another design, and which test would tell you whether it helped?

## Good to know
This is a pin-jointed, two-dimensional axial-member model, not a design certification tool. The bridge represents one of two identical sides. Each side carries half the vehicle; its slab load is 2.0 kN per meter. Each member carries its full stated self-weight. Timber has one simplified 20 MPa strength in pull and squeeze. Euler buckling assumes pinned ends. Cables cannot carry squeeze. Crossed members connect only when there is a joint.

Budget starts off. Its optional dial sets a comparison limit. Done closes the adjustment dialog while the limit stays on, without locking construction or tests. The county brief independently stays at $9,000. Prices are classroom estimates, not construction quotes. Displacement is magnified by twenty in the bridge and wind views and by five during shakes; True size removes magnification. Motion off removes animated movement without shortening a test. Steady shakes are synthetic test inputs, not a replay of a historical earthquake.

Tap pressure is 9.81 kPa per meter of water head; the surface is three meters above the top joint. A top joint at 26 m gives about 284 kPa or 41.3 psi. The grid and twenty-meter tower examples use the SI values in spec.md. Recomputed numerical disagreements with the spec's reference examples are listed in handoff.md.

Keyboard: Tab to controls and the grid. Arrows move a grid cursor. Enter starts and finishes a member. Delete erases a member at the cursor. Keys 1 to 5 choose material. Space runs or stops when the grid or page has focus. R rebuilds after collapse. Shift drag moves a joint. Save and logbook entries use localStorage with a session fallback; nothing leaves the device.

## Standards and sources
MS-ETS1-1: choose promises as criteria and constraints. MS-ETS1-2: compare test evidence in the Yard. MS-ETS1-3: Borrow combines parts of compared designs. MS-ETS1-4: repeated live model tests support revision. The same actions extend to HS-ETS1-2, HS-ETS1-3 and HS-ETS1-4.

Physical sources: Hibbeler, Structural Analysis, direct stiffness method; MIT OCW 1.050 truss notes; USDA Wood Handbook FPL-GTR-282 (2021), chapters 5 and 7; AISC Steel Construction Manual and ASTM A36; FHWA Bridge Formula Weights and 23 CFR 658.17; Chopra, Dynamics of Structures; ASCE 7 wind commentary; NASA Glenn sea-level air density; OpenStax elasticity and hydrostatics. Vehicle facts and simplified values follow spec.md. No source lookup or network request occurs in the tool.

## The instrument console
Bridge and Tower are two rigs in the same test yard. Manual opens beside the maker's plate at the lower left.
It holds the how-to, honesty notes and yard logbook. The power panel holds Motion, Sound and Read. There is no
score or finish line. Load, worst-member use and actual top sway appear on needle gauges; numeric readouts remain
valid beyond the needle scale. Loose frames read LOOSE and an empty rig reads NO FRAME.
