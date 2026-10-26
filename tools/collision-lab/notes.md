## A 5-minute start

1. Open **Air Track**. Pick preset **2. Equal masses, Velcro** and press **Launch** (or Space). Glider A hits B and they move off together at +0.30 m/s. Read the ledger line: momentum before 0.150 kg·m/s, after 0.150 kg·m/s, kinetic energy kept 50 percent. Ask: where did half the energy go?
2. Pick preset **1. Equal masses, spring** and launch. A stops dead and B leaves at +0.60 m/s: momentum and energy both kept.
3. Pick preset **3. Heavy hits light**, launch, then tick **Ride with center of mass**. The view now travels at +0.33 m/s with the center of mass: the two momentum bars are equal and opposite and the Total bar reads 0.000 before and after.
4. Switch to **Crumple Zone**. Launch with **Steel** (a 158 N spike lasting 9.9 ms), then **Spring** (10 N over 157 ms). Both shaded areas are 1.00 N·s, because both gliders reverse from +1.00 to minus 1.00 m/s.

## The three modes

- **Air Track:** a 2.00 m frictionless track with gliders A and B (0.20 m long, 0.10 to 1.00 kg, minus 1.00 to +1.00 m/s). Bumpers set the coefficient of restitution e: Spring 1.00, Rubber 0.60, Velcro 0.00 (they stick), Custom 0 to 1. Drag a glider (or Tab to it and use the arrows) to change its start spot. The ledger shows momentum (bars from a center zero line) and kinetic energy, Before and After. **Measurement noise** adds up to plus or minus 2 percent to every measured velocity and makes Rubber's e vary from 0.55 to 0.65, so recorded points scatter near the y = x line. **Predict** asks for both velocities after the collision before Launch unlocks. **Slow motion** plays at a quarter speed; **Jump to collision** appears when contact is more than 8 s away.
- **Crumple Zone:** one glider (0.20 to 1.00 kg, 0.20 to 2.00 m/s) hits a force sensor through a nose. The force-time graph is drawn stretched in time (a 10 ms hit takes about 1.5 s to draw); the shaded area is the impulse. The last three runs stay as dashed ghosts. **Lock graph axes** keeps the scale so a taller curve shows "peak off scale". The **Spec sheet** has four design specs; picking one locks the mass and speed and checks each limit after every launch.
- **Notebook:** recorded runs in two tables (**Copy table** pastes into a spreadsheet as columns with units in the headers), three plots and four conclusion boxes. Everything is saved on this device only; nothing is sent anywhere.

## Talk about it

- What stayed the same in every Air Track run, even with noise on? What changed from bumper to bumper?
- Velcro keeps no bounce, yet momentum is still conserved. Where did the kinetic energy go? (Into deforming the bumper, sound and heat.)
- In the center of mass frame, Velcro keeps 0 percent of the kinetic energy and Rubber keeps 36 percent (e squared). Why is that different from the lab frame numbers?
- Steel and Spring give the same impulse but very different peak forces. Why does a longer contact time mean a smaller force?
- Why does a bounce need a bigger impulse than a stop?

## The spec sheet (teacher key)

| Spec | Glider | Energy to absorb | Works with Crumple |
|---|---|---|---|
| 1. Gentle stop | 0.50 kg at 1.00 m/s | 0.25 J | crush force 5.0 to 9.5 N at 5.0 cm |
| 2. Heavy cart | 1.00 kg at 1.50 m/s | 1.125 J | at least 18.75 N at 6.0 cm (19.0 to 29.5 N on the slider) |
| 3. Fast and light | 0.50 kg at 2.00 m/s | 1.00 J | 10.0 to 14.5 N at 10.0 cm |
| 4. Heavy and fast | 1.00 kg at 2.00 m/s | 2.00 J | **cannot be met** |

Spec 4 is the impossible one. To stop without bouncing, the crumple force times the crush length must be at least the kinetic energy: F times 0.10 m at least 2.00 J, so F is at least 20 N, over the 15 N limit. A smaller crush force bottoms out and spikes to hundreds of newtons on the steel backing. The card never says which spec is impossible; students prove it with "Energy at impact" and the crush length. Steel, Spring and Rubber always bounce, so they fail "must not bounce" on every spec. (The spec calls spec 4 "The impossible brief"; on screen it is named "Heavy and fast" so the name does not give it away.)

## Good to know

- Model (one block in the code, the forces engine): v1 after = (m1 v1 + m2 v2 + m2 e (v2 minus v1)) / (m1 + m2), and the same for v2 with the roles swapped. Gliders stop at an end stop (no bounce off the end), and a run ends there or 3 s after the collision. If a glider reaches an end stop before A catches B, the run counts as no collision.
- Noses: Steel k = 50,000 N/m and Spring k = 200 N/m (elastic); Rubber loads at 1,000 N/m and unloads at 4,000 N/m (e = 0.50); Crumple crushes at a steady force over its length, then a 50,000 N/m steel backing takes the rest ("Bottomed out"). Integrated with velocity Verlet every 0.00001 s.
- Checked results at 0.50 kg and 1.00 m/s: Steel 158.1 N, 9.9 ms, 0.32 cm; Spring 10.0 N, 157.1 ms, 5.00 cm; Rubber 22.4 N, 52.7 ms, 2.24 cm, rebounds at minus 0.50 m/s; Crumple 6.0 N and 5.0 cm stops in 4.17 cm over 83.3 ms; Crumple 2.0 N and 5.0 cm bottoms out at 122.5 N and rebounds at minus 0.76 m/s. Impulse matches the change in momentum within 0.1 percent every time.
- Sign convention on the crumple bench: toward the wall is positive, so the change in momentum is negative (the wall pushes the glider away from it); the graph and the impulse readout show the size of that push.
- Preset 7, The chase, keeps 67 percent of the kinetic energy (both gliders end at +0.40 m/s).
- With Measurement noise on, a Spring run can read slightly more than 100 percent kinetic energy kept (up to about 108). The Notebook plots the measured value as it is, with a note under the plot. Ask: can a collision really make energy, or is this the measurement?
- The air track's e column in the Notebook is the e used for that run (with noise on, Rubber's random value).
- Keyboard: Space launches and R resets on the two benches (not while typing in a box or with a button focused, where Space presses that button).
- With Motion off, a run jumps straight to its end and the ledger, graph and readouts fill at once; the narration is unchanged.
- Clear table asks for a second press before it removes the rows.
