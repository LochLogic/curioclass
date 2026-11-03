# 1. Graph Stories
minutes: 35
materials: pencil, ruler, calculator
ican: I can connect position-time graphs to motion and find velocity from the slope.
pairs: motion-graph-match
directions: Each row of the table gives the points of a position-time graph for one motion, measured from a motion sensor at x = 0. Picture each graph from its points, match it to its story, and find the velocity from the slope.
mistakes: Students often read a position-time graph as a picture of the path (a hill on the graph means going up a hill). A flat line means standing still, not moving at a steady speed. For graph 3, watch the sign: the position decreases, so the velocity is negative. For graph 4, the slope changes, so there is no single velocity.
notes: Slope = change in position / change in time. Graph 1: +2 m/s. Graph 2: 0. Graph 3: -3 m/s. Graph 4: speeding up, x = t^2, so the slope grows: average velocity 4 m/s over 4 s, instantaneous velocity 4 m/s at t = 2 s. Graph 5: +4 m/s for 2 s, then 0. Graph 6: +5 m/s. The motion graph tool lets students drive these shapes after the sheet.

## Warm up
example: A graph goes from (0 s, 0 m) to (4 s, 8 m) in a straight line. Slope = (8 - 0) / (4 - 0) = 2 m/s. The object moves away from the sensor at a steady 2 m/s.

## The six graphs (position in meters)
table: Graph | t = 0 s | t = 1 s | t = 2 s | t = 3 s | t = 4 s
  - 1 | 0 | 2 | 4 | 6 | 8
  - 2 | 10 | 10 | 10 | 10 | 10
  - 3 | 12 | 9 | 6 | 3 | 0
  - 4 | 0 | 1 | 4 | 9 | 16
  - 5 | 0 | 4 | 8 | 8 | 8
  - 6 | 0 | 5 | 10 | 15 | 20

## Main: Match the story
match: Match each graph to its story.
  - Graph 1 = A student walks away from the sensor at a steady, easy pace.
  - Graph 2 = A backpack sits on a bench the whole time.
  - Graph 3 = A dog trots straight back toward the sensor at a steady pace.
  - Graph 4 = A cart starts from rest at the sensor and rolls down a ramp, faster and faster.
  - Graph 5 = A runner sprints away, then stops to wait at a crosswalk.
  - Graph 6 = A cyclist rides away at a steady speed, faster than the walker.
fill:
  - Velocity for graph 1: {+2} m/s
  - Velocity for graph 2: {0} m/s
  - Velocity for graph 3: {-3} m/s
  - Velocity for graph 5, first 2 s: {+4} m/s; last 2 s: {0} m/s
  - Velocity for graph 6: {+5} m/s
  - Average velocity for graph 4 over 4 s: {4} m/s

## Plot one
text: Plot graph 4 and connect the points with a smooth curve. Draw a tangent line at t = 2 s.
graph: Time (s) | 0 4 1 | Position (m) | 0 20 2
  key: 0,0 1,1 2,4 3,9 4,16

## Stretch
write: Use your tangent line to estimate graph 4's velocity at t = 2 s. How does it compare with its average velocity over 4 s?
  lines: 2
  key: The tangent at t = 2 s passes about (1 s, 0 m) and (3 s, 8 m), so the slope is about 8 / 2 = 4 m/s. For x = t^2 this equals the average over 0 to 4 s (16 / 4 = 4 m/s): for steady acceleration, the velocity at the middle time equals the average velocity.
write: Write your own story for a graph that goes from 0 m to 6 m in 3 s, stays at 6 m for 2 s, then returns to 0 m in 2 s. Give each velocity.
  lines: 2
  key: Example: a student walks to a door 6 m away at +2 m/s, waits 2 s (0 m/s), then hurries back at -3 m/s.

# 6. Free-Body Diagrams
minutes: 40
materials: pencil, ruler, calculator
ican: I can draw free-body diagrams and use them to find the net force on an object.
directions: For each situation, draw the object as a dot or box and draw every force on it as an arrow pointing away from the object, labeled with its name and size. Longer arrows for bigger forces. Then find the net force (size and direction). Use g = 9.8 N/kg, so weight = mass x 9.8.
mistakes: Students often add a "force of motion" in the direction an object is moving; moving objects need no force to keep going, so a car at a steady speed has net force zero. Watch for forces the object exerts on something else (the book pushing on the table) drawn on the object; only forces acting ON it belong. Students also think the skydiver at terminal velocity has an upward net force because they "slow down"; at a steady speed the forces balance.
notes: Forces for the key, in order. 1: weight 19.6 N down, normal 19.6 N up; net 0. 2: push 50 N right, friction 30 N left, weight 98 N down, normal 98 N up; net 20 N right (a = 2.0 m/s²). 3: weight 588 N down, air resistance 588 N up; net 0. 4: weight 588 N down, air resistance 200 N up; net 388 N down (a = about 6.5 m/s²). 5: weight 4.9 N down only; net 4.9 N down (a = 9.8 m/s²). 6: tension 11,000 N up, weight 9,800 N down; net 1,200 N up (a = 1.2 m/s²). 7: tension 29.4 N up, weight 29.4 N down; net 0. 8: Team A 400 N left, Team B 350 N right; net 50 N left. 9: road's forward push 2,000 N, air and rolling resistance 2,000 N back, weight 14,700 N down, normal 14,700 N up; net 0. 10: friction 0.50 N backward, weight 1.7 N down, normal 1.7 N up; net 0.50 N backward (opposite the motion).

## Warm up
example: A 2.0 kg book rests on a table. Weight = 2.0 x 9.8 = 19.6 N down. The table pushes up with a normal force of 19.6 N. Net force = 19.6 N up - 19.6 N down = **0 N**.
choice: An object moves to the right at a steady speed. The net force on it is:
  - to the right
  * zero
  - to the left
  - equal to its weight

## Main: Ten situations
table: # | Situation | Free-body diagram | Net force
  - 1 | The 2.0 kg book on a table (draw it again). | | {0 N}
  - 2 | A 10 kg box is pushed right with 50 N; friction is 30 N. | | {20 N right}
  - 3 | A 60 kg skydiver falls at a steady (terminal) speed. | | {0 N}
  - 4 | The same skydiver early in the fall; air resistance is 200 N. | | {388 N down}
  - 5 | A 0.50 kg ball in free fall (ignore air). | | {4.9 N down}
  - 6 | A 1,000 kg elevator is pulled up by a cable with 11,000 N. | | {1,200 N up}
  - 7 | A 3.0 kg lamp hangs still from one cord. | | {0 N}
  - 8 | Tug of war: Team A pulls a rope left with 400 N, Team B right with 350 N. Draw the rope. | | {50 N left}
  - 9 | A 1,500 kg car drives at a steady 25 m/s. The road pushes it forward with 2,000 N. | | {0 N}
  - 10 | A 0.17 kg hockey puck slides right on ice and slows down; friction is 0.50 N. | | {0.50 N left}
  height: 0.95

## Think
fill:
  - Acceleration = net force / mass. Box 2: {2.0} m/s². Skydiver 4: about {6.5} m/s². Elevator 6: {1.2} m/s² upward.
  - In situation 9, the air and road resistance on the car must be {2,000} N, because its speed is {steady}.
write: Situations 3 and 4 show the same skydiver. Why does the net force change as the skydiver falls?
  lines: 2
  key: Air resistance grows as the skydiver speeds up. Early on it is smaller than the weight (net force down, speeding up); at terminal speed it equals the weight, so the net force is zero and the speed stays steady.

## Stretch
write: A 5.0 kg sled is pulled by a rope with 40 N at 30° above the ground. Friction is 20 N. Find the forward net force and the normal force.
  lines: 3
  key: Forward part of the pull: 40 x cos 30° = 34.6 N. Net force = 34.6 - 20 = about 14.6 N forward (a = about 2.9 m/s²). Upward part of the pull: 40 x sin 30° = 20 N, so the normal force = 49 - 20 = 29 N.

# 17. Universal Gravitation
minutes: 40
materials: pencil, scientific calculator
ican: I can use Newton's law of universal gravitation to calculate the gravitational force between two objects.
pairs: field-lines
directions: Use F = G m1 m2 / r², with G = 6.67 x 10⁻¹¹ N·m²/kg². Distance r is measured center to center, in meters. Give answers to 3 significant figures in scientific notation.
mistakes: Students often use the distance from the surface instead of from the center: for a satellite, r is Earth's radius plus the altitude. Watch for kilometers left unconverted, and for r not squared. On calculators, students type 6.67 x 10 ^ -11 instead of using the EE or EXP key and get the wrong power of ten; have them check pair 2, which should match the person's weight (mg = 588 N).
notes: Values used: Earth's mass 5.97 x 10²⁴ kg, radius 6.37 x 10⁶ m; Moon's mass 7.35 x 10²² kg, radius 1.74 x 10⁶ m; Earth-Moon distance 3.84 x 10⁸ m; Sun's mass 1.99 x 10³⁰ kg; Earth-Sun distance 1.50 x 10¹¹ m. Pair 7 (97.2 N) is about one sixth of pair 2 (589 N), the familiar Moon-to-Earth weight ratio. The field lines tool shows the same inverse-square drop-off as a picture.

## Warm up
table: Constant | Value
  - Earth: mass, radius | 5.97 x 10²⁴ kg, 6.37 x 10⁶ m
  - Moon: mass, radius | 7.35 x 10²² kg, 1.74 x 10⁶ m
  - Earth to Moon, Earth to Sun (center to center) | 3.84 x 10⁸ m, 1.50 x 10¹¹ m
  - Sun: mass | 1.99 x 10³⁰ kg
fill:
  - If the distance between two objects doubles, the force becomes {1/4} as strong. If it triples, {1/9} as strong.
  - If one mass doubles, the force becomes {2} times as strong.

## Main: Eight pairs
example: Two 7.0 kg bowling balls, 0.30 m apart: F = (6.67 x 10⁻¹¹)(7.0)(7.0) / (0.30)² = 3.63 x 10⁻⁸ N.
table: # | Pair | m1 (kg) | m2 (kg) | r (m) | Force (N)
  - 1 | two students | 60 | 50 | 1.0 | {2.00 x 10⁻⁷}
  - 2 | a student and Earth | 60 | 5.97 x 10²⁴ | 6.37 x 10⁶ | {589}
  - 3 | two cars in a parking lot | 1,500 | 1,500 | 2.0 | {3.75 x 10⁻⁵}
  - 4 | a 1,000 kg satellite 400 km above Earth | 1,000 | 5.97 x 10²⁴ | {6.77 x 10⁶} | {8.69 x 10³}
  - 5 | an astronaut on the Moon | 60 | 7.35 x 10²² | 1.74 x 10⁶ | {97.2}
  - 6 | Earth and the Moon | 5.97 x 10²⁴ | 7.35 x 10²² | 3.84 x 10⁸ | {1.98 x 10²⁰}
  - 7 | Earth and the Sun | 5.97 x 10²⁴ | 1.99 x 10³⁰ | 1.50 x 10¹¹ | {3.52 x 10²²}
  - 8 | the Sun and Jupiter | 1.99 x 10³⁰ | 1.90 x 10²⁷ | 7.78 x 10¹¹ | {4.17 x 10²³}
  height: 0.5

## Think
choice: The two students in pair 1 attract each other. Why don't they drift together?
  - Gravity only works on very large objects.
  - The force is cancelled by Earth's gravity.
  * The force is so tiny (about 2 x 10⁻⁷ N) that friction with the floor easily outweighs it.
  - People have no gravitational mass.
fill:
  - The satellite's force (pair 4) is about {89} percent of what it would feel on the ground (9,800 N).
  - Jupiter is about 5.2 times farther from the Sun than Earth, but the Sun pulls on it about {12} times harder, because Jupiter's mass is about {318} times Earth's.

## Stretch
write: Somewhere between Earth and the Moon, their pulls on a spacecraft are equal. How far from Earth's center is that point?
  lines: 3
  key: Set G M_E m / x² = G M_M m / (d - x)². Then x / (d - x) = √(M_E / M_M) = √81.2 = 9.01, so x = 9.01 d / 10.01 = 0.900 d = 0.900 x 3.84 x 10⁸ = about 3.46 x 10⁸ m from Earth's center.

# 23. Coaster Energy Points
minutes: 40
materials: pencil, calculator
ican: I can use conservation of energy to find potential energy, kinetic energy and speed, with and without friction.
directions: A 500 kg coaster car starts at rest at point A. Use g = 9.8 m/s². Find the energy at each point, first with no friction, then when friction turns 10,000 J into thermal energy on each section of track (A to B, B to C, C to D, D to E). Round speeds to 3 significant figures.
mistakes: Students often use the height difference from the point before instead of the height above the ground, or forget to square the speed when solving KE = ½mv². With friction, students subtract only 10,000 J at every point instead of adding up the losses: by point D, three sections have taken 30,000 J.
notes: Total mechanical energy at A = mgh = 500 x 9.8 x 40 = 196,000 J. Speed: v = √(2 KE / m). The heights were chosen so the no-friction speeds come out whole (28, 14, 21 and 7 m/s). With friction the car cannot reach E: it needs 183,750 J of potential energy there, but even before any losses on the last section it has only 196,000 - 30,000 = 166,000 J, so it rolls back down before E.

## Warm up
fill:
  - PE = m x g x h, so PE at A = {196,000} J.
  - At A the car is at rest, so KE = {0} J and the total energy is {196,000} J.

## The track
table: Point | A | B | C | D | E
  - Height (m) | 40 | 0 | 30 | 17.5 | 37.5

## Main: No friction
table: Point | PE (J) | KE (J) | Speed (m/s)
  - A | 196,000 | 0 | 0
  - B | {0} | {196,000} | {28.0}
  - C | {147,000} | {49,000} | {14.0}
  - D | {85,750} | {110,250} | {21.0}
  - E | {183,750} | {12,250} | {7.00}

## Main: With friction (10,000 J lost per section)
table: Point | Energy lost so far (J) | PE (J) | KE (J) | Speed (m/s)
  - A | 0 | 196,000 | 0 | 0
  - B | {10,000} | {0} | {186,000} | {27.3}
  - C | {20,000} | {147,000} | {29,000} | {10.8}
  - D | {30,000} | {85,750} | {80,250} | {17.9}
choice: With friction, does the car reach point E?
  - Yes, at about 7 m/s
  - Yes, at a lower speed
  * No: it does not have enough energy left to climb to 37.5 m

## Explain
write: Explain your answer about point E using energy numbers.
  lines: 3
  key: At E the car would need 183,750 J of PE. After three sections it has at most 196,000 - 30,000 = 166,000 J of total energy, less than 183,750 J, so it stops climbing and rolls back before reaching E.
write: The friction energy does not disappear. Where does it go?
  lines: 2
  key: It becomes thermal energy (heat) in the wheels, track and air, plus a little sound. Total energy is conserved.

## Stretch
write: Without friction, what is the tallest hill the car could climb after point A? With friction, what is the highest a hill at E could be if the car must still just reach its top?
  lines: 3
  key: No friction: up to 40 m (the starting height). With friction: total energy after 4 sections is 196,000 - 40,000 = 156,000 J, so h = 156,000 / (500 x 9.8) = about 31.8 m.

# 28. Series vs Parallel Lab
minutes: 45
materials: 2 AA cells in a holder (3 V), 3 identical small bulbs in holders, 6 wires with clips, digital multimeter, goggles
ican: I can build series and parallel circuits, measure voltage, and explain differences in bulb brightness.
directions: Build each circuit, predict first, then measure the voltage across the battery and across each bulb with the meter (red probe to the side nearer the battery's + end). Rate each bulb's brightness from 0 (off) to 3 (bright, like one bulb alone).
mistakes: Students often connect the meter in series (in the path) to measure voltage; a voltmeter goes across the part, one probe on each side. Students also think the first bulb in a series circuit "uses up" the current and glows brighter; identical bulbs in series glow the same. Measured values come out a little below 1.5 V and 3.0 V because the cells and wires have resistance; that is normal.
notes: Expected values with fresh cells and identical bulbs: one bulb about 3.0 V; two in series about 1.5 V each; three in series about 1.0 V each; two or three in parallel about 3.0 V each. In parallel, each bulb is as bright as a single bulb, but the battery runs down faster because it supplies more current. Safety: never connect a wire straight across the battery (a short circuit makes the wire and cells hot); disconnect between measurements; use only small cells, never a wall outlet.

## Warm up
fill:
  - A voltmeter measures the energy each charge gives up (voltage), so it connects {across} a bulb, one probe on each side.
  - In a {series} circuit there is only one path for the current. In a {parallel} circuit there are separate branches.
text: Prediction: Two bulbs in series and two bulbs in parallel. Which will be brighter, and why?
lines: 2

## Main: Data
table: Circuit | Battery voltage (V) | Voltage across each bulb (V) | Brightness of each (0 to 3) | Unscrew one bulb: what happens?
  - One bulb | {about 3.0} | {about 3.0} | {3} | {it goes out}
  - Two in series | {about 3.0} | {about 1.5 each} | {1 to 2 (dimmer)} | {both go out}
  - Three in series | {about 3.0} | {about 1.0 each} | {about 1 (dimmest)} | {all go out}
  - Two in parallel | {about 3.0} | {about 3.0 each} | {3} | {the other stays lit}
  - Three in parallel | {about 3.0} | {about 3.0 each} | {3} | {the others stay lit}
  height: 0.55
note: Students record their own measured values; the key shows expected values.
draw: Circuit diagram of two bulbs in series and two bulbs in parallel, with the meter shown | 1.8

## Analyze
fill:
  - In series, the bulb voltages {add up to} the battery voltage.
  - In parallel, each bulb's voltage is {equal to} the battery voltage.
choice: Why are bulbs in parallel brighter than the same bulbs in series?
  * Each parallel bulb gets the full battery voltage, so more current flows through it.
  - Parallel circuits make more electricity.
  - The current in series is used up by the first bulb.
  - Parallel bulbs are closer to the battery.
write: Homes are wired in parallel. Use your data to give two reasons why.
  lines: 3
  key: Each device gets the full voltage, so it works at its normal power no matter how many others are on. And if one device is switched off or burns out, the others keep working, unlike a series circuit, where one break turns everything off.

## Stretch
write: The parallel bulbs were all bright, but the battery runs down faster. Explain using energy.
  lines: 2
  key: Each parallel bulb draws as much current as a single bulb, so the battery supplies two or three times the total current and gives out energy two or three times as fast. Its stored energy is used up sooner.

# 39. Bending Light in Water
minutes: 45
materials: clear rectangular plastic box or dish, water, sheet of paper on a corkboard or thick cardboard, 4 pins, protractor, ruler, calculator
ican: I can trace light rays through water and calculate the index of refraction from my measurements.
directions: Trace the box on the paper and fill it with water. Push two pins (A and B) in a line toward the box at an angle. Looking through the water from the far side, push pins C and D so all four look like one straight line. Remove the box, connect the pin holes to the outline, draw the ray through the water, and measure the angles from the normal.
mistakes: Students often measure angles from the surface of the box instead of from the normal (the line at 90° to the surface). Watch for calculators in radian mode: sin 30 should give 0.5. Students also expect the light to bend away from the normal entering water; light slows down in water and bends toward the normal.
notes: The thin plastic walls barely change the result, since the ray leaves parallel to how it entered. Sample data are rounded to whole degrees, so the single values run 1.32 to 1.34; the accepted index of refraction for water is 1.33. For row 50°, rounded sines give 1.33 and unrounded give 1.34; accept both. Safety: pins point down into the board; collect them at the end; wipe up spills at once.

## Warm up
fill:
  - The line drawn at 90° to the surface where the ray enters is called the {normal}.
  - Snell's law: n = sin(angle in air) / sin(angle in water). For water, n should be close to {1.33}.
choice: As light passes from air into water it:
  - speeds up and bends away from the normal
  - keeps the same speed and direction
  - stops at the surface
  * slows down and bends toward the normal

## Main: Sample data
table: Angle in air (°) | Angle in water (°) | sin (air) | sin (water) | n
  - 20 | 15 | {0.342} | {0.259} | {1.32}
  - 30 | 22 | {0.500} | {0.375} | {1.33}
  - 40 | 29 | {0.643} | {0.485} | {1.33}
  - 50 | 35 | {0.766} | {0.574} | {1.33 to 1.34}
  - 60 | 41 | {0.866} | {0.656} | {1.32}
fill:
  - Average n = {1.33}
graph: sin (angle in water) | 0 0.7 0.1 | sin (angle in air) | 0 0.9 0.1
  key: 0,0 0.676,0.9
note: The slope of the line is n, about 1.33. Students plot the five sample points; all lie on or very near the key line.

## Main: My data
table: Angle in air (°) | Angle in water (°) | sin (air) | sin (water) | n
  - | | | |
  - | | | |
  - | | | |
fill:
  - My average n = {about 1.3} Percent error = (|my n - 1.33| / 1.33) x 100 = {your value} percent

## Stretch
write: Light going from water into air at more than a certain angle does not come out at all (total internal reflection). Use n = 1.33 to find this critical angle, where the angle in air would be 90°.
  lines: 2
  key: sin(critical angle) = 1 / 1.33 = 0.752, so the critical angle is about 48.8°. At larger angles in water, the light reflects back inside.
