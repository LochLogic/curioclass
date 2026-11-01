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
