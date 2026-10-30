# Pocket Universe

## One idea
Throw stars, planets, moons and dust into space with one drag and let one real rule, every mass pulls every other
mass, decide what happens: orbits, crashes, escapes, slingshots, rings and two-sun systems all come out of the same
rule, and a time bar lets you rewind any moment and throw again.

## First minute
No reading needed. The tool opens already moving.
- 0 s: the Starter universe is running at x1. A painted yellow star glows and slowly pulses in the middle; one painted
  planet circles it, a glowing gold trail fading behind it. Along the bottom of the space view, the tray shows painted
  chips (Star, Red dwarf, Black hole, Giant, Planet, Moon, Comet, Dust); Planet is already picked and gently glows.
  A faint dotted arc drifts from the Planet chip into space every 4 s until the first throw (Motion off: shown still).
- 2 s: the student presses anywhere in space. A planet pops in under the pointer with a soft pop. Time holds still
  while they aim. Dragging stretches an arrow from the planet, and a dashed ghost path curls around the star at once,
  bending live as the arrow grows or turns.
- 4 s: release. A whoosh pitched by the throw speed; the planet flies with its own trail color. Time runs again.
- 5 to 12 s: one of three things happens, each with its own sound. It orbits (a bell chime each lap), it crashes
  (thump, white flash ring, the star swells a little and the first sticker, Crash, slides in), or it escapes (a
  falling whoosh, then an arrow at the screen edge with its distance counting up).
- 12 to 20 s: after a crash the time bar's handle glows. Dragging it back plays a tape warble and the crash un-happens:
  the planet is whole again. They let go, throw differently, and the old path stays as a faint dotted ghost so they
  see where the new try splits from the old one.
- 20 to 45 s: more throws. Lap chimes start to make a rhythm: inner planets chime fast, outer ones slow (Kepler's third
  law, heard). A moon tried near a planet either circles it or gets carried off.
- 45 to 60 s: the `Goals` button shows "3 / 24" with a pulse. Opening it shows a sticker book where each found sticker
  is a picture of their own trails at the moment they found it, and the next targets are listed below.

## Not like
- orbit-lab (grade 9, spec): one planet launched from 1 AU by sliders, solved exactly by Kepler's laws, with plots and
  numbers. Here many bodies all pull on each other (numeric, not analytic), thrown by hand, no plots; Kepler's laws
  are felt and heard, not graphed.
- moon-phase-model (grade 6, built): Sun, Earth and Moon lighting geometry and phases, no gravity. Here gravity and
  motion, no lighting.
- field-lines (grade 11, built): fixed masses and charges drawn as field maps. Here nothing is fixed; the field's
  result is motion.
- planet-builder (grade 6 idea card, taken over): its flick, tray, pull arrows, solar-system scale cards and spinning
  disk all live here (the disk as the Black hole whirl load, with an honesty note).
- size-of-everything (built): scale from atoms to galaxies by zooming. Here scale only inside Real Solar System's
  True size switch.
- which-way-is-down (grade 5): gravity points to Earth's center. Here gravity between any two bodies.

## Who and how
Grades 6 to 12, science (Earth and space, physics). Students drive, alone or in pairs; a teacher can run a room
challenge on the projector. 10 to 45 minutes. Explore first: it opens moving, goals are optional.
Standards: MS-ESS1-2, MS-ESS1-3, MS-PS2-4; reaches HS-PS2-4 and HS-ESS1-4.
tool.json: driver "students or teacher", minutes "10-45", modes ["Pocket", "Real Solar System"],
grades_label "Grades 6-12".

## Screens and modes
Header (kit): "Pocket Universe", small line "One rule: every mass pulls." Modes `Pocket` and `Real Solar System`;
kit `Motion`, `Sound`, `Read`.

Layout (by real stage pixels, re-laid out per size): the space view is the biggest, central thing (at 1366x768 about
75 percent of the width, full height under the header minus the time bar). The tray overlays the bottom of the space
view (chips 56 px tall). The time bar sits directly under the space view. The panel (about 290 px) is on the right:
the hint line, Selected body, World, Goals and Universes. Under 900 px tall the panel goes compact (sections fold,
Selected open). At 760 and 375 wide the space view is on top (60 percent of the height), then the time bar, then the
tray as a scrolling row, then the panel.

### Pocket (default)
Focus: the bodies and their trails in the space view.
- Space view: the painted sky, bodies as painted sprites, glowing trails, ghost path while aiming, edge arrows for
  bodies off screen (with distance), pull arrows when on, the merge flashes.
- Tray chips (painted icons, label under each): `Star`, `Red dwarf`, `Black hole`, `Giant`, `Planet`, `Moon`,
  `Comet`, `Dust`. Tap a chip to pick what the next throw makes (one is always picked; Planet at start).
- Time bar: `Play` / `Pause` (Space), speed `Slow` (x0.25), `x1`, `x4`, `x16`, the scrubber (the last 150 s of world
  time; the handle is now), `Undo` (Ctrl+Z), the clock ("12.4 s" world time; Real: a date).
- Selected body section (shows when a body is picked; tap a body to pick it): name and picture ("Giant 2"), mass,
  speed in the view, what it circles and its lap count ("circling Star 1, lap 3"), and buttons `Follow`,
  `Heavier`, `Lighter`, `Faster`, `Slower`, `Turn left`, `Turn right`, `Pulls`, `Remove`.
- World section: Gravity dial (0 to 2, step 0.1, default 1, reads "Gravity x1.0"), `Ghost` (on), Trails `Short`
  (3 s), `Long` (12 s), `Forever`, `Fit`, `+`, `-`, `Clear`.
- Goals: `Goals 3 / 24` opens the sticker book (an overlay over the space view; time keeps running behind it).
- Universes: `Wonders` (the loads), `Save`, `My universes`.
What responds: everything moves under gravity in real time; every control acts on the next frame.

### Real Solar System
Focus: the Sun and eight planets on their real orbits, and the date.
- Opens on 1 January 2000 with the Sun and the eight planets placed from real orbital elements, real masses and
  real distances (1 AU = 100 world px). The view first fits out to Mars; `Fit` cycles Inner (to 1.7 AU), Giants (to
  10 AU) and All (to 31 AU). The clock shows the month and year ("Mar 2001"). At x1 one Earth year takes 1.99 s.
- Planets are drawn bigger than life (Sun 16 px, giants 9 px, others 6 px) with the label "Drawn bigger than life".
  `True size` (World section) draws every body at its real size: everything shrinks to a dot under one pixel, each
  body gets a thin ring so it can still be found, and the label reads "True size: Earth is 0.0085 px across here".
- Tray in this mode: `Comet`, `Earth-size`, `Jupiter-size`, `Sun-size star`, `Black hole` (1 Sun mass).
- Same time bar, Selected, World (Gravity dial, Ghost, Trails, True size) and Goals. `Follow` on Earth is the key
  view: the Sun and planets as seen from Earth.

## Goals
All 24 show in the sticker book from the start (target line visible, sticker empty). Found ones fill with a 160x100
snapshot of the student's own trails at that moment plus the "What you found" line (Content). Goals never pause,
gate or interrupt play: a found sticker slides in at the panel's top for 3 s with a chime and its line. Order is
easy to hard. Definitions used by the checks:
- Parent: for body i, among bodies at least 3 times heavier, those it is bound to (two-body energy
  v²/2 − G(m_i+m_j)/r < 0, v and r relative to that body); the parent is the nearest of them. A change of parent
  resets the lap count.
- Lap: the angle of i around its parent, added up with sign, reaches a whole 360 degrees.
- Checks run every 1/30 s of world time, on world values, at any speed; Undo or rewinding never removes a sticker.
- Lap goals count bodies with mass only (dust counts only for Ring and Lane clearer). A goal counts only when at least
  one body in it was thrown or changed by the student (so the Starter planet and a load's own bodies earn nothing by
  themselves), except goals that name a load (Rescue, Figure eight) or Real (Backing up, Venus flower), which need the
  action they name.

| # | Sticker | Target | Check (exact) | Secretly teaches |
|---|---|---|---|---|
| 1 | First orbit | Make something go all the way around. | any body completes 1 lap | an orbit is falling and missing |
| 2 | Crash | Make two things hit. | any merge | masses add; momentum is kept |
| 3 | Escape | Throw something away for good. | a body that once had a parent is 1500 px or more from the heaviest body with energy relative to it above 0 | escape speed is 1.41 times circle speed |
| 4 | Straight line | Turn gravity off and watch. | Gravity dial at 0 for 3 s of world time with a moving body | Newton's first law; orbits need a pull |
| 5 | Racetrack | Make an inner planet lap an outer one. | two bodies with the same parent, the inner one 2 laps ahead since both got that parent | closer orbits are shorter and faster |
| 6 | Comet | Make a long, stretched orbit. | a body completes 3 laps on an orbit with eccentricity 0.7 or more (two-body elements at each lap) | speeds up near the star, slow far out |
| 7 | Heavy hitter | Grow one body by crashing things into it. | any body reaches mass 2000 | more mass, more pull; it turns blue-white |
| 8 | Wobble | Make a star circle too. | a star completes 1 lap around the center of mass of itself and its heaviest companion, at 10 px or more from that center | planets tug stars; how exoplanets are found |
| 9 | Moon | Give a planet a moon. | a body completes 5 laps around a parent that itself has a parent | nested orbits; a moon must stay close |
| 10 | Backwards moon | A moon that circles the other way. | 5 laps around a parent, turning opposite to that parent's own laps | backwards moons hold farther out (Triton) |
| 11 | Lightweight | Make a star lighter and set a planet free. | within 1 s after `Lighter` on a star, a body with that star as parent gets energy above 0 relative to it, and later reaches 1500 px | the pull holds the orbit; less mass, less pull |
| 12 | Ring | Make a ring around something. | 20 or more dust motes bound to one body, spread over at least 9 of 12 equal slices around it, and the first of them bound for 3 of its laps | rings are countless tiny moons, smeared by speed |
| 13 | Two suns | Two stars circling each other. | two bodies of mass 300 or more, bound to each other, complete 3 laps around their center of mass | binary stars circle a shared center |
| 14 | Slingshot | Use a planet to fling something out. | a body bound to the heaviest body (energy below 0) passes within 100 px of a different body of mass 10 or more; within 3 s after its closest pass its energy relative to the heaviest body is above 0; then it reaches 1500 px | gravity assist |
| 15 | Moon thief | Move a moon from one owner to another. | a body completes 2 laps around parent A, then 2 laps around a different parent B | capture: which pull wins can change |
| 16 | Trojan | Ride along beside a planet. | a body with the same parent as a planet stays between 25 and 100 degrees ahead of it (or behind it), measured around the parent, for 5 of the planet's laps | Lagrange points L4 and L5 |
| 17 | Tatooine | A planet circling both stars of a pair. | a body completes 3 laps around the center of mass of a pair that earns Two suns, both stars inside its path the whole time | circumbinary planets need room |
| 18 | Rescue | Save the moon in the Rescue load. | in Rescue the moon completes 10 laps around the giant | small changes now, big changes later |
| 19 | Lane clearer | Let a giant sweep its path. | dust within 10 percent of a body's distance from its parent falls to 25 percent or less of the count when its first lap began (20 motes or more then), within 10 of its laps | planets clear their lanes (why Pluto is a dwarf) |
| 20 | Calm black hole | Orbit a black hole. | a body completes 3 laps around a black hole | far off, a black hole pulls like any equal mass |
| 21 | Figure eight | Nudge the three-body dance and keep it dancing. | in Three-body dance, after `Faster` or `Slower` on a dancer, all three survive 10 more rounds (103.3 s world time) with no merge and none more than 600 px from their center | some three-body orbits are sturdy |
| 22 | Backing up | Watch Mars move backward. | in Real, while following Earth, Mars's direction from Earth reverses | retrograde motion: Earth overtakes Mars |
| 23 | Venus flower | Let Venus draw its flower. | in Real, following Earth with Trails Forever, 5 closest passes of Venus seen without a change in between | 13 Venus years are almost 8 Earth years |
| 24 | Grand tour | One throw that visits three planets. | one body passes within 60 px of 3 different bodies of mass 10 or more (Pocket) or of 3 planets within 0.3 AU (Real), with no merge | Voyager 2's grand tour |

## Content
World and units (Pocket): world px, seconds, pocket mass units; G = 10,000 px³/(mass unit · s²). Default zoom: the
shorter side of the space view shows 700 world px. One fixed step of 1/480 s of world time.

Tray (Pocket): kind, mass, radius (px), sprites.
| Chip | Mass | Radius | Sprite |
|---|---|---|---|
| Star | 1000 | 22 | pu-star-yellow |
| Red dwarf | 300 | 14 | pu-star-red |
| Black hole | 1000 | 5 | pu-black-hole |
| Giant | 100 | 12 | pu-giant-amber, pu-giant-teal, pu-giant-violet (taken in turn) |
| Planet | 10 | 7 | pu-planet-ocean, -desert, -lava, -ice (in turn) |
| Moon | 0.3 | 4 | pu-moon-gray, -ice, -rust (in turn) |
| Comet | 0.001 | 3 | pu-comet (tail drawn in code, pointing away from the heaviest body) |
| Dust | a puff of 30 motes, mass 0 | 1.5 (drawn) | code dots, 10 px puff, speeds spread ±5 percent |
- A body that reaches mass 300 by crashes or `Heavier` becomes a star (it glows): sprite red below 600, yellow below
  2000, blue (pu-star-blue) at 2000 or more (heavier stars are hotter and bluer). Black holes stay black holes.
- Merges: total mass, total momentum, position at the center of mass, the heavier body's kind; radius grows by
  (new mass / old mass)^(1/3) (a black hole: 5 x (mass/1000)^(1/3)). `Heavier` x2 and `Lighter` /2, limited to
  1/4 and 4 times the kind's tray mass, radius scales the same way.
- Pocket honesty line (World section, small): "Pocket rule: same gravity, but giants are 1/10 of a star and planets
  1/100, so moons fit on screen. Real Jupiter is 1/1048 of the Sun. Real Solar System uses true numbers."

Throws: press in space makes the picked body there; the drag vector sets its velocity: 2 x drag length (world px)
per second, in the drag's direction, added to the followed body's velocity when following (throws are in the view's
frame). Drag is capped at 250 world px (500 px/s). A tap without a drag places it at rest in the view. Press on a body
(within its radius plus 8 px) picks it; dragging from it throws it again. At 250 px from a lone Star: drag 46 px or
less crashes into it, about 100 px circles (201 px/s), 142 px or more escapes (283 px/s).

Wonders (loads; each replaces the universe, Undo brings the old one back). Positions in world px (y up), velocities
px/s:
- Starter (opens the tool): Star (0, 0) v (0, -1.990); Planet (250, 0) v (0, 199.007). Circle, period 7.815 s.
- Empty: nothing at all.
- Two suns: two stars of mass 500 (radius 18) at (-50, 0) v (0, -158.11) and (50, 0) v (0, 158.11). Period 1.99 s.
- Three-body dance: three red dwarfs (300, radius 14) at (194.00, -48.62) and (-194.00, 48.62) with v (57.10, 52.95)
  each, and (0, 0) with v (-114.20, -105.91). One round 10.33 s. Opens at x4.
- Rescue the moon: Star (0, 0) v (0, -17.408); Giant (300, 0) v (0, 174.078); Moon (330, 0) v (0, 384.35) (1.15 times
  its circle speed around the giant: 210.28 relative, circle 182.85). Follow is on the giant. The moon crashes at 15.7 s.
- Ring lane: Star and Giant as in Rescue, plus 240 dust motes on circles at random radii 150 to 450 px (seeded, so the
  load is the same every time).
- Black hole whirl: Black hole of mass 3000 at (0, 0) and 240 dust motes on circles at radii 80 to 450 px (speeds
  612 to 258 px/s). Its line: "A real galaxy holds together with the pull of all its stars and dark matter. This whirl
  has one heavy center, so its outer dust moves slower than a real galaxy's stars."

Real Solar System (start 1 January 2000; 1 AU = 100 px; Sun 1000 mass units; planets placed by Kepler's equation from
the elements, all in one plane; Sun given the recoil so total momentum is zero):
| Body | a (AU) | e | mean longitude (deg) | perihelion longitude (deg) | mass (10²⁴ kg) | mass (units) | diameter (km) |
|---|---|---|---|---|---|---|---|
| Sun | | | | | 1,988,500 | 1000 | 1,391,400 |
| Mercury | 0.38709927 | 0.20563593 | 252.25032 | 77.45780 | 0.330 | 0.000166 | 4,879 |
| Venus | 0.72333566 | 0.00677672 | 181.97910 | 131.60247 | 4.87 | 0.002449 | 12,104 |
| Earth | 1.00000261 | 0.01671123 | 100.46457 | 102.93768 | 5.97 | 0.003002 | 12,756 |
| Mars | 1.52371034 | 0.09339410 | -4.55343 | -23.94363 | 0.642 | 0.000323 | 6,792 |
| Jupiter | 5.20288700 | 0.04838624 | 34.39644 | 14.72848 | 1898 | 0.954488 | 142,984 |
| Saturn | 9.53667594 | 0.05386179 | 49.95424 | 92.59888 | 568 | 0.285642 | 120,536 |
| Uranus | 19.18916464 | 0.04725744 | 313.23810 | 170.95428 | 86.8 | 0.043651 | 51,118 |
| Neptune | 30.06992276 | 0.00859048 | -55.12003 | 44.96476 | 102 | 0.051295 | 49,528 |
Real tray: Comet 0.000001 units; Earth-size 0.003002; Jupiter-size 0.954488; Sun-size star 1000; Black hole 1000.
Crash radii in Real are true radii (Earth 0.0043 px): only the Sun (0.465 px) is easy to hit, which is the point.
Real periods at x1: Mercury 0.48 s, Earth 1.99 s, Jupiter 23.6 s, Neptune 327.6 s (20.5 s at x16).

Sticker "What you found" lines (shown when found; also Read):
1. An orbit is falling and missing: it falls toward the star the whole time, but moves sideways fast enough to miss.
2. The masses add up, and the new body keeps going with the push of both.
3. From any spot, escape speed is about 1.41 times the speed for a circle.
4. With no pull, a moving thing goes straight at a steady speed. Gravity is what bends the path.
5. Closer orbits are shorter and faster. Mercury takes 88 days; Neptune takes 165 years.
6. On a stretched orbit, a body races past the star and crawls far away. Halley's Comet returns about every 76 years.
7. More mass, more pull: the neighbors' orbits tighten. Big stars burn hotter and bluer.
8. A planet tugs its star around in a small circle. Astronomers find planets around other stars by that wobble.
9. A moon stays only close to its planet. Farther out, the star's pull carries it away.
10. Moons that go backwards stay steady farther out. Neptune's big moon Triton goes backwards.
11. Halve a star's mass and a planet on a circle has just enough speed to escape.
12. A ring is countless tiny moons. Inner bits move faster, so a clump smears into a circle. Saturn's rings are ice.
13. Two stars circle a point between them, their center of mass. Nearly half of Sun-like stars have a partner.
14. A close pass behind a moving planet borrows some of its speed. Voyager 2 did this at Jupiter, Saturn and Uranus.
15. Which pull wins can change in a close pass, so moons can be lost and caught.
16. Sixty degrees ahead of or behind a planet, the pulls balance. Jupiter has thousands of Trojan asteroids there.
17. A planet can circle two suns if it stays far out, a bit more than twice their spacing. Kepler-16b is one.
18. A slower moon stayed closer and safer. A small change now is a big change later.
19. A big planet sweeps its path clear. Clearing its lane is part of being a planet; Pluto has not cleared its lane.
20. Far away, a black hole pulls just like a star of the same mass. It only swallows what comes very close.
21. Three equal stars can share one figure-eight path, found in 1993. Small nudges keep it going; big ones break it.
22. Earth passes Mars on the inside track, so Mars seems to back up for a while about every 26 months.
23. Seen from Earth, Venus draws five loops in eight years: 13 Venus years almost equal 8 Earth years.
24. Voyager 2 flew past Jupiter, Saturn, Uranus and Neptune in 12 years.

## Interactions in detail
- The model: Newton's law of gravitation between every pair of bodies (F = G m1 m2 / r², softening 1 px), leapfrog
  (kick, drift, kick) with the fixed 1/480 s step, so it is deterministic: the same start and the same actions always
  give the same future. Each step is split into 2^k equal substeps (k up to 6) when any pair's distance over its
  relative speed is under 20 steps (fast close passes near a black hole). Collisions check the closest approach along
  each substep, so a fast body cannot skip through a small one. Dust motes feel every body but pull nothing.
- Aiming: while a pointer is down in space, time holds (the clock reads "aiming"); the ghost shows the thrown body's
  next 3 s of world time with every other body moving too, ending at a red X on a crash or at 2000 px; recomputed at
  most every 50 ms. `Ghost` off hides it. Release resumes at the speed that was on.
- Pick and change: tap a body to pick it (a ring in the accent). `Faster` / `Slower` change its speed in the view by
  1 percent per tap; `Turn left` / `Turn right` turn its motion 5 degrees; `Heavier` / `Lighter` as in Content;
  `Remove` deletes it; `Follow` keeps it centered (the view moves with it; trails are drawn in that frame, so following
  Earth shows Mars's loops); tap `Follow` again or empty space with nothing picked to stop. `Pulls`: arrows from the
  picked body toward every other massive body, length by force (biggest 80 px), and a line naming the top three as
  percents of the total ("Star 1: 91 percent").
- Time: the scrubber holds snapshots every 0.25 s of world time for the last 150 s. Dragging it shows the past (bodies
  and trails as they were). Any change made in the past (a throw, a nudge, a mass, gravity, a load) starts a new
  timeline; the old future stays as a faint dotted ghost for 30 s of world time. `Undo` goes to just before the last
  change and drops its future with no ghost. Speeds change at once; Pause stops on the next frame.
- Gravity dial: scales G for everything. A circle stays bound only above 0.5 (at 0.5 or below every circling body
  leaves); at 0.6 a circle at r stretches out to 5r; at 2 it falls in to r/3. In the whirl at 0.45, all 240 motes
  are past 1500 px after 20 s.
- Edges: bodies beyond 20,000 px from the heaviest body are removed with "Gone: Planet 3 flew away"; dust beyond
  4,000 px is dropped. A body on screen edge keeps an edge arrow with its distance.
- Budget (school Chromebook, 60 frames a second): 20 bodies with mass, 240 dust motes (8 puffs). Per step that is 190
  body pairs plus 4,800 mote pulls; x1 runs 8 steps a frame, x4 32, x16 128. If a frame's physics passes 10 ms, the
  run drops to the fastest speed that holds and the speed button shows it ("x16 running x9"). The builder measures
  this with Chrome's CPU throttle at 4x; if x4 cannot hold the full budget, lower dust to 160 and say so. At the limit
  the tray chips grey out and the hint says "Space is full: crash some together, or pick one and tap Remove."
- Sound (Web Audio, all synthesized; the kit's Sound button): throw, a short rising whoosh whose pitch follows the
  speed; lap, a soft bell, pitch by the body's kind (stars low, moons high), at most 6 chimes a second; crash, a low
  thump plus a noise burst, louder for bigger masses; into a star, a sizzle; into a black hole, a falling sub tone;
  escape, a falling whoosh that fades; close pass under 40 px, a quick pitch bend; scrubbing, a tape warble at the
  scrub speed; sticker found, a three-note rising arpeggio; aiming, a faint hum that rises with the drag length.
- Shine: stars glow and pulse slowly (screen blend); trails glow and fade (8 trail colors in turn, Look); a merge
  flashes a white ring that grows and fades over 0.4 s with a few sparks; the black hole's accretion ring turns
  slowly; dust motes twinkle; the picked body has an accent ring. Motion off: no pulse, twinkle, ring growth or sparks
  (motion of the bodies is the content and stays).
- Save on this device: `Save` stores the universe as now, plus a replay (the state at the start of the scrubber's
  window and every change after it, by step number). `My universes` lists up to 12 saves (thumbnail, name you can
  edit, date) with `Load`, `Replay` (plays from the replay start at x1; all controls stay live; a change during a
  replay starts a new unsaved timeline) and `Delete` (asks once). At 12, Save asks to replace the oldest. Stickers
  and saves in localStorage `curio-pocket-universe` (try/catch; works with nothing saved).
- Keyboard: Space play/pause; Ctrl+Z Undo; 1 to 8 pick tray chips; Enter on a chip drops that body 200 px to the
  right of the heaviest body (in the view) with that spot's circle speed; Tab cycles bodies in the space view; F
  Follow; Delete Remove; G Ghost; arrow keys on the focused scrubber step 1 s; + and - zoom; 0 Fit. Wheel zooms at the
  pointer; drag with the right button, or two fingers, pans.
- Mode change: `Curio.stop()`, `V.hush()`; each mode keeps its own universe and scrubber while the page is open.
- Reset is `Clear` (asks once) and Wonders > Starter.

## Look
Accent (`--brand`) #ff8fd8, nebula pink: 8.93:1 on --panel #12131f, 8.23:1 on --sec-bg #1a1b2b; --brand-ink #1a0a17
on it 9.25:1. Text #eef0ff on panel 16.29:1; muted #a3a8c8 7.90:1. Clear of orbit-lab #a9c4ff, field-lines #e8b54a,
moon-phase-model gold #f2c14e, star-life-story violet #b894d0, conic-focus-finder #8ff0ff.
Space: the painted sky under a #05060d wash at 35 percent. Trail colors in turn (each on #05060d): #ffd166 14.03,
#7fe3ff 13.81, #9dff8a 16.47, #ff9f7a 10.11, #c9a7ff 10.07, #6ff5c8 15.00, #ffe3f1 16.86, #ff8fd8 9.80. Ghost path
dashed #eef0ff at 70 percent; crash X #ff5c6c (6.74:1); ghost timeline dotted at 35 percent of the body's color.
Trails are never the only signal: picked bodies also show their name, and goals use text.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 27 images, all in a soft painted gouache style (orbit-lab's
planets are photo-like; these must look different).
- pu-sky-nebula: a deep space sky in soft painted gouache, a faint pink and violet nebula cloud drifting across one
  side, scattered small stars; 16:9; cutout no; Pocket background.
- pu-sky-deep: a deep black space sky in painted gouache with many tiny faint stars and a pale band of the Milky Way
  along the bottom; 16:9; cutout no; Real Solar System background.
- pu-sky-dust: a dark space sky in painted gouache with a warm brown dust lane and a few bright blue stars; 16:9;
  cutout no; Three-body dance and Black hole whirl background.
- pu-star-yellow: a glowing yellow-white star in painted gouache, a soft round glow, centered on pure black; 1:1;
  cutout no (screen blend); Star.
- pu-star-red: a small glowing orange-red star in painted gouache, soft glow, centered on pure black; 1:1; screen
  blend; Red dwarf and stars under 600.
- pu-star-blue: a big blazing blue-white star in painted gouache with a wide glow, centered on pure black; 1:1;
  screen blend; stars of 2000 or more.
- pu-black-hole: a black circle wrapped in a thin glowing orange and gold ring of swirling gas, painted gouache, seen
  slightly from above, on pure black; 1:1; screen blend; rotated slowly in code.
- pu-giant-amber: a banded amber and cream gas giant planet with a swirling storm, painted gouache, lit from the left,
  full disk on pure black; 1:1; cutout yes; Giant.
- pu-giant-teal: a smooth teal ice giant planet with faint pale bands, painted gouache, lit from the left, full disk
  on pure black; 1:1; cutout yes; Giant.
- pu-giant-violet: a violet and rose banded gas giant with a thin flat ring, painted gouache, lit from the left, on
  pure black; 1:1; cutout yes; Giant.
- pu-planet-ocean: a small blue ocean planet with white cloud swirls and green islands, painted gouache, lit from the
  left, full disk on pure black; 1:1; cutout yes; Planet.
- pu-planet-desert: a small tan desert planet with rust canyons, painted gouache, lit from the left, full disk on
  pure black; 1:1; cutout yes; Planet.
- pu-planet-lava: a small dark rocky planet with glowing orange lava cracks, painted gouache, full disk on pure
  black; 1:1; cutout yes; Planet.
- pu-planet-ice: a small white and pale blue frozen planet with icy ridges, painted gouache, lit from the left, full
  disk on pure black; 1:1; cutout yes; Planet.
- pu-moon-gray: a small gray moon covered in round craters, painted gouache, lit from the left, full disk on pure
  black; 1:1; cutout yes; Moon.
- pu-moon-ice: a small cracked white ice moon with pale blue lines, painted gouache, full disk on pure black; 1:1;
  cutout yes; Moon.
- pu-moon-rust: a small lumpy rust-red moon, painted gouache, lit from the left, on pure black; 1:1; cutout yes; Moon.
- pu-comet: a small dark lumpy icy comet nucleus with bright frosty patches, painted gouache, on pure black; 1:1;
  cutout yes; Comet (the tail is code).
- pu-sun: the Sun in painted gouache, a glowing golden ball with soft orange swirls and a warm glow, on pure black;
  1:1; screen blend; Real.
- pu-mercury, pu-venus, pu-earth, pu-mars, pu-jupiter, pu-uranus, pu-neptune: each planet in painted gouache, lit from
  the left, full disk on pure black (Mercury gray and cratered; Venus pale yellow clouds; Earth blue oceans, white
  clouds, green and brown land; Mars rust red with a white polar cap; Jupiter tan and cream bands with a red oval
  storm; Uranus smooth pale cyan; Neptune deep blue with a dark oval spot); 1:1 each; cutout yes; Real bodies, tray
  chips (Earth-size, Jupiter-size) and labels.
- pu-saturn: Saturn in painted gouache, pale gold bands and wide flat tilted rings, lit from the left, on pure black;
  16:9; cutout yes; Real.
Drawn in code: trails, ghost paths, arrows, pull arrows, merge flashes and sparks, dust, comet tails, edge arrows,
rings in True size, the time bar, the sticker snapshots (they are the student's own trails), preview.svg.

## Voice
Bank `casual-peer` ("Say casually and naturally, like a friendly teenager explaining something"), here an older kid
who plays this for fun and shows you a trick. Not used by any space neighbor (orbit-lab wise-mentor, star-life-story
smooth-narrator, field-lines hs-narrator, moon-phase-model none). `Curio.voice`, `scope: () => state.mode`,
`welcomeAfter: true`. Nothing speaks before the first tap (kit).
- welcome (how; Pocket welcome; stale once anything is thrown): "Pick something from the tray, then drag in space to
  throw it. A longer drag throws it faster."
- crash (how; first crash; stale once the time bar is dragged): "Crash. Drag the time bar back to undo it, then throw
  again."
- escape (how; first escape; stale on the next throw): "That one got away. It was too fast for the star to pull it
  back."
- follow (how; after 5 laps of anything, when a Giant or Planet exists; stale once Follow is on): "Tap a planet, then
  tap Follow. Now your throws aim around it, so you can give it a moon."
- goals (how; first sticker; stale once Goals is opened): "Tap Goals to see your stickers and what to try next."
- real (how; Real welcome; stale once the speed changes or a body is followed): "This is our real solar system, on
  the first day of 2000. Tap x16 to watch the outer planets move."
- realFollow (how; 10 s into Real; stale once Earth is followed): "Tap Earth, then tap Follow. Watch Mars from Earth
  for a few years."
- trueSize (how; Real, first time Fit shows All; stale once True size is on): "Tap True size to see how small the
  planets really are."
- Wonders intros (how; once each when loaded; stale on the next load):
  twoSuns "Two suns. Throw a planet around both of them, far out.";
  dance "Three stars share one figure eight. Tap a dancer, then tap Faster once.";
  rescue "This moon keeps crashing. Drag the time bar to the start, tap the moon, then tap Slower a few times.";
  lane "A giant in a dust disk. Watch its path.";
  whirl "A whirl around a black hole. Drag Gravity down to 0.4 and watch."
- full (event; budget reached; stale when a body is removed or merged): "Space is full. Crash some together, or pick
  one and tap Remove."
- gone (event; a body removed past 20,000 px; stale after 3 s): "Gone. It flew too far to follow."
- saved (event; Save): "Saved on this device."
- sticker (event; each sticker found; stale after 4 s): "New sticker: " plus the name, one recorded line per sticker
  (24 lines: "New sticker: First orbit." through "New sticker: Grand tour.").
Hints (silent, in the panel, Read speaks them): Pocket default is the welcome; while aiming "Let go to throw. The
dashed line shows where it will go."; with a body picked "Drag from it to throw it again, or use Faster, Slower and
Turn."; in a rewound past "Throw or change something to start a new timeline, or tap Play."

## Family engine
None. Orbit Lab's planned astronomy engine is analytic (Kepler's equation) for one body; this tool needs an N-body
integrator, so it keeps its own in one marked block (`/* NBODY: begin */ ... /* NBODY: end */`) with no DOM access,
exposing `step()`, `snapshot()`, `restore()`, `predict(body, seconds)` and `parentOf(i)`, so a later tool could lift
it.

## Teacher note
Three ways in a period: (1) free play for 15 minutes, then each pair shows the room one thing they made and says what
pulled what; (2) a goal set: Moon, Two suns, Tatooine and Lane clearer, then talk about why some orbits last;
(3) a room challenge on the projector: Grand tour, or the most laps a moon can make before it is stolen, with the
class calling out throws. Standards: MS-ESS1-2 (gravity's role in orbits, binaries and the whirl), MS-ESS1-3 (Real
Solar System scale and True size), MS-PS2-4 (Pulls, Heavier and Lighter, the Gravity dial as evidence that gravity
attracts and depends on mass and distance); for high school HS-PS2-4 and HS-ESS1-4.

## Sources
- Newton's law of gravitation, escape speed, center of mass: OpenStax, University Physics Volume 1, chapter 13,
  https://openstax.org/books/university-physics-volume-1/pages/13-introduction
- Orbital elements (J2000, 1800 to 2050 fit): JPL, "Approximate Positions of the Planets", Table 1,
  https://ssd.jpl.nasa.gov/planets/approx_pos.html
- Planet masses, diameters, periods (Mercury 88 days, Neptune about 165 years): NASA Planetary Fact Sheet,
  https://nssdc.gsfc.nasa.gov/planetary/factsheet/ ; Sun mass and diameter: NASA Sun Fact Sheet,
  https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html ; Jupiter is 1/1048 of the Sun (1898 / 1,988,500).
- Moon stability limits (prograde about 0.49 Hill radius, retrograde about 0.93): Domingos, Winter and Yokoyama 2006,
  MNRAS 373:1227. Triton's backwards orbit: NASA, https://science.nasa.gov/neptune/moons/triton/
- Planets around binaries (outside about 2.3 times the spacing for equal stars; inside about 0.3 around one):
  Holman and Wiegert 1999, AJ 117:621. Kepler-16b: Doyle et al. 2011, Science 333:1602. Nearly half of Sun-like stars
  have companions: Raghavan et al. 2010, ApJS 190:1.
- Trojan points need the planet under about 1/26 of the star (Routh 0.0385): Murray and Dermott, Solar System
  Dynamics (1999), 3.8. Jupiter's thousands of Trojans: NASA Lucy, https://science.nasa.gov/mission/lucy/
- Figure-eight three-body orbit: Moore 1993, Phys. Rev. Lett. 70:3675; Chenciner and Montgomery 2000, Annals of
  Mathematics 152:881 (initial values used here).
- Gravity assist and Voyager 2 (Jupiter 1979, Saturn 1981, Uranus 1986, Neptune 1989; launched 1977): NASA JPL,
  Basics of Space Flight, https://science.nasa.gov/learn/basics-of-space-flight/ and
  https://science.nasa.gov/mission/voyager/
- Clearing the neighborhood and Pluto: IAU 2006 Resolution B5. Saturn's rings are mostly ice: NASA,
  https://science.nasa.gov/saturn/ . Halley's Comet about 76 years: NASA,
  https://science.nasa.gov/solar-system/comets/1p-halley/
- Exoplanet wobble (radial velocity): NASA, https://science.nasa.gov/exoplanets/how-we-find-and-characterize/
- Mars oppositions about every 26 months and the 2001 to 2010 dates; Venus inferior conjunctions 2001 to 2007: NASA
  Mars close approach page, https://science.nasa.gov/mars/ , and the JPL Horizons system.
- Galaxies held by all their mass and dark matter: Rubin and Ford 1970, ApJ 159:379.
- Number checks (Python, 2026-10-29, the model above: G 10,000, step 1/480 s, leapfrog, softening 1 px, merges by
  momentum, adaptive substeps). Scripts in the spec agent's scratchpad (pu.py, t1 to t27).
  - Starter: separation stays 250.000 to 250.012 px over 30 s; period 7.815 s. Circle at 250 px around a lone Star:
    7.65 laps in 60 s, energy drift 5e-11. Sideways throws at 250: crash below 91.3 px/s (drag 45.7), circle 200.3,
    escape at 283.3 (drag 141.6); drag 30 crashed at 1.45 s; drag 150 reached 1500 px at 8.5 s.
  - Moons around Giant at 300 (Hill radius 96.5 px): prograde at 20 to 40 px with 0.85 to 1.0 of circle speed held
    60 s; at 50 px (0.52 Hill) lost at 18.2 s; 60 px crashed. Backwards moons at 50, 60, 70 px (up to 0.73 Hill) held
    60 s. Planet (Hill 44.8 px): moons at 12 to 18 px held.
  - Rescue: moon at 30 px, 1.15 times circle speed crashes at 15.7 s; 0.85 to 1.10 times (Slower 5 to 30 taps)
    reaches 10 laps (by 7.1 to 14.7 s); 0.80 or less crashes at once; 1.20 or more crashes by 4.3 s.
  - Two suns (separation 100): 3 laps in 6 s. Planets around both at 230 to 350 px held 120 s (19 to 9.6 laps); at
    150 crashed at 1.3 s, at 200 after 4.6 laps (26.5 s). Around one star of a pair 400 apart: 50, 80, 120 px held
    60 s; 160 px (0.4) lost and crashed at 22.6 s. Matches Holman and Wiegert.
  - Trojan (Planet 10 at 300): exact L4 swings 54.3 to 65.3 degrees; 45 and 75 degree starts and 0.97 speed stay
    inside 25 to 100; 1.03 speed becomes a horseshoe (fails, as it should). Giant 100 (1/11 of the star) never holds:
    above the Routh limit.
  - Slingshot: of 178 random bound comet throws near a Giant, 13 escaped to 1500 px and 10 of those after a pass
    under 100 px of the Giant (about 6 percent of random throws), so the goal is reachable by trying and rewinding.
  - Grand tour (Planets at 180, 300, 450 px): 2 of 400 random throws visited all three within 60 px with no crash;
    23 visited two. Hard on purpose.
  - Figure eight (student-made, around two stars): 0 of 1,080 random throws looped one star each way twice, so the
    goal uses the Three-body dance instead. Dance: returns within 0.24 px after one round; nudges of 1 percent (20
    rounds), 2 percent (crash at round 17.9), 5 percent (11.9) and 10 percent (20 rounds) all pass the 10-round goal;
    20 percent crashes at round 3.7, sideways 10 percent at 3.8.
  - Black hole: Planet path after 20 s identical (0.0 px) around a Star or a Black hole of the same mass. Worst case
    plunge to 8 px from a 3000 black hole (2,739 px/s): energy error 0.54 percent fixed step, 0.39 percent with
    substeps (16).
  - Lightweight: halving a star under a circling Planet gives energy +206 (unbound); it reaches 1500 px at 14.4 s.
    Doubling: the circle at 250 drops to 86 px at its closest; tripling to 52 (no crash).
  - Gravity off: the planet moves on a straight line (x stays 250.00, y 602.99 after 3 s). Dial thresholds above
    match vis-viva; whirl at 0.45: 240 of 240 motes past 1500 px in 20 s; at 0.6: 90; at 1.0: 0.
  - Ring: a 30-mote puff thrown at circle speed 30 to 40 px from a Giant: 28 to 30 bound after 3 laps, 11 of 12
    slices filled; at 55 px: 14 bound after 10 laps.
  - Lane clearer (Ring lane): dust within 270 to 330 px went 46, 10, 5, 6, 0, 2 over 5 Giant laps (met after 1); a
    Planet (10) left 15 of 46 after 10 laps (not met: only giants clear fast).
  - Wobble: a Star with a Giant circling at 300 px (Rescue without the moon) moves on a 27.3 px circle; the Starter's
    Planet moves its Star only 2.5 px, under the 10 px the goal needs.
  - Real Solar System: lap counts after 12 years match Kepler within 0.03 (Saturn 0.437 against 0.407, from its
    partial ellipse); energy drift 7e-9; no merges. Mars backs up starting May 2001, Jul 2003, Oct 2005, Nov 2007,
    Dec 2009 (each about a month before the real oppositions of 13 Jun 2001, 28 Aug 2003, 7 Nov 2005, 24 Dec 2007,
    29 Jan 2010). Venus closest passes Mar 2001, Oct 2002, Jun 2004, Jan 2006, Aug 2007 (real inferior conjunctions
    30 Mar 2001, 31 Oct 2002, 8 Jun 2004, 13 Jan 2006, 18 Aug 2007), 5 in 7.97 years. 13 x 224.701 = 2921.1 days;
    8 x 365.25 = 2922.0. Earth's true diameter at 100 px per AU: 0.0085 px.
  - Contrast ratios computed with the WCAG formula (Look).

## Done when
1. Opening shows the Starter moving within 1 s; a press and drag in space shows the ghost path at once, and release
   throws with the whoosh; no instructions are needed to make an orbit, a crash and an escape.
2. Sideways throws at 250 px from a lone Star: drag 40 crashes, drag 100 circles (about 7.8 s a lap), drag 150 leaves
   and shows an edge arrow; the same throw replayed after Undo gives the same path to the pixel.
3. Rescue: the moon crashes at about 15.7 s; scrub to the start, Slower 5 times, and the Rescue sticker comes by about
   15 s; Faster makes it crash sooner.
4. Each of the 24 stickers can be earned by the checks in Goals (a test pass with scripted throws from Sources), and
   each found sticker shows the student's own trails.
5. Real Solar System: following Earth from 1 Jan 2000, Mars starts backing up in May 2001; Venus flower appears with
   Trails Forever by early 2008; Neptune's lap takes about 20.5 s at x16.
6. Focus: the space view is the biggest thing at 1366x768 and in the 680x425 preview; tray and time bar visible
   without scrolling at every size in STANDARDS.md; labels at least 10 px in the preview.
7. A tap while anything moves: a speed button, Pause, Faster, Heavier, Gravity and the scrubber all change what is
   shown on the next frame; aiming holds time and release resumes.
8. Full budget (20 bodies, 240 dust) holds 60 frames a second at x4 under 4x CPU throttle, or the speed button shows
   the real speed; the chips grey out at the limit with the full line.
9. Save, reload the page, `My universes` > Replay plays the same throws and crashes; stickers survive a reload;
   private window (no storage) still plays.
10. How-to lines once each, every sticker line spoken each time one is found, no line names a hidden or disabled
    control; 27 images load, none shows a person; no network, no em dashes.
11. A fresh player with no instructions is still choosing to play after 10 minutes, and can name one thing they
    figured out.

## Open questions
- [pocket-universe] Pocket masses are exaggerated (Giant 1/10 of a star, Planet 1/100) so moons fit on screen, with an
  honesty line and true numbers in Real. OK, or keep Pocket at real ratios and lean on zoom?
- [pocket-universe] A student-made figure eight around two stars almost never happens (0 in 1,080 random throws), so
  the Figure eight goal is "nudge the Three-body dance and keep it going". OK?
- [pocket-universe] The Gravity dial is the one knob real space does not have (it is the same as scaling every mass).
  Keep it for Straight line, Lightweight-style what-ifs and the whirl, or drop it?
- [pocket-universe] Black hole in the grade 6 tray: physically honest here (it pulls like any equal mass), but it is a
  showy item. Keep?
- [pocket-universe] Real Solar System starts on 1 January 2000 (the date the orbital elements are for), so the Mars
  and Venus events land on checkable real dates. Start there, or on today's date?
