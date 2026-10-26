## A 5-minute start

1. Open **Explore** (it starts with **Hand**, cart at 1 m). Drag the cart from 1 m to about 7 m and let go. The clock starts by itself. Ask: why does the velocity graph make a bump, and why does the acceleration graph go up and then down?
2. Pick **Throttle**, press **Clear**, and push the slider to 1.0 m/s. The velocity graph goes flat at 1, and position climbs 1 m every second. Position is the running total of velocity.
3. Pick **Pedal**, press **Clear**, and hold 0.2 m/s² for 5 s. The acceleration graph is flat, velocity climbs to 1.0 m/s, and position curves up about 2.5 m. The force arrow reads 0.40 N (F = m a with a 2.0 kg cart).
4. Let a run reach 12 s, turn on **Show links**, and move across the graphs. The slope printed on each graph matches the ringed value on the graph below it, and the shaded area under velocity matches the bracketed change in position.

## The two modes

- **Explore:** free drive for 12 s, swept like a scope. **Go** / **Pause**, **Clear** (wipes the traces and resets the clock; the cart stays put unless **Start at** was changed, which applies on Clear), **Show links** (on a paused or finished run). Switching control mid-run is allowed and leaves a tick on the time axis.
- **Race:** ten target graphs (position, velocity or acceleration). Pick a card, press **Start** (3, 2, 1, then a 12 s run) and keep your solid line inside the shaded band. Match percent is the share of the 240 samples (every 0.05 s) inside the band; RMS error is printed too. Your best run for each target and control comes back as a dotted ghost (saved on this device; **Forget my bests** clears them). A "hard way" tag means you control a graph two steps from the target (Pedal on a position target, Hand on an acceleration target).

## Talk about it

- Target 6, Turnaround: the cart stops for an instant at 3 s. Is the acceleration zero there? (No: it is -0.5 m/s² the whole time. Velocity zero is not acceleration zero.)
- Why can't a real cart follow target 1 exactly? (The corners in position need an instant jump in velocity, which needs a huge push. **Show all three** marks it.)
- Which control makes the position targets easiest, and which makes them hardest? Why?
- Where on a position graph is the velocity largest? Where on a velocity graph is the cart farthest from the sensor?
- A position graph is not a picture of the path. The cart only moves along a straight track. What does a rising line mean?

## Good to know

- Model: one 2.0 kg cart on a 10 m track, stepped every 1/60 s, sampled every 0.05 s. Top speed 3 m/s. Hand and Throttle change velocity at no more than 2 m/s², so the acceleration graph stays on its scale.
- Hand: the cart matches your pointer's speed (measured over about half a second, so pixel steps and uneven frame timing average out) and closes any gap, so a steady drag stays within a few centimeters and its acceleration graph stays flat. A fast flick or a hard stop lags or runs a little past (up to about a quarter meter), because the cart can change velocity by at most 2 m/s every second. On target 2 that limit alone keeps a pointer held exactly on the line to about 85 percent: a real cart cannot turn around at an instant.
- Throttle: the slider is the velocity you want; the cart eases toward it over about 0.2 s. Pedal: the slider is the acceleration itself. Both: Up and Down step it (0.1 m/s or 0.05 m/s²), Page Up and Page Down step five times as much, Home sets 0. The slider snaps to 0 near the middle. **Spring back** returns it to 0 when you let go.
- End stops: hitting 0 m or 10 m stops the cart at once (velocity drops to 0); the acceleration graph shows an "end stop" mark instead of the huge, brief spike. Pushing the Pedal into a stop keeps the cart parked, and the arrow shows the push with "the end stop pushes back".
- With Show links on, the readouts beside the graphs give the values at the time cursor. In small windows (such as the embedded preview) the graphs print each link once, and the ringed values are read from those readouts.
- Acceleration samples are averages over each 0.05 s and are drawn at the middle of that interval, which is why the slope of velocity and the acceleration value agree.
- Target end points (checked): 1 ends at 8 m, 2 at 1 m, 3 at 9 m, 4 at 8 m, 5 at 8.5 m, 6 at 1.75 m (farthest 6.25 m at 3 s), 7 at 8 m, 8 at 2.5 m, 9 at 9 m, 10 at 2 m. Standing still on target 1 scores 28 percent (inside the band until 3.4 s).
- With Motion off, the cart, ghost and traces still move (they are the data); the countdown numbers do not zoom.
- Standard: HS-PS2-1 (the force readout ties the acceleration graph to F = m a).
