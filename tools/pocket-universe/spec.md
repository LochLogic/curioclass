# Pocket Universe

## One idea
Throw stars, planets, moons and dust into space with one drag and let one real rule, every mass pulls every other
mass, decide what happens: orbits, crashes, escapes, slingshots, rings and two-sun systems all come out of the same
rule, and a time bar lets you rewind any moment and throw again.

## First minute
Owner-approved instrument pivot, 2026-11-04. The sky is the front door, with one throw line and the tray.
The Starter runs at x1: a painted star and a planet, luminous trails, a live clock. Press in space to place a
body and hold time; drag to aim with a live ghost, release to throw. A crash flashes and lights the rewind tape;
scrubbing makes it un-happen. There is no goal count, sticker, award sound or finish line. The student chooses
what to change, load or follow next. The Manual is there when they want to name something they noticed.

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
challenge on the projector. 10 to 45 minutes. Explore first: it opens moving, with no score or finish line.
Standards: MS-ESS1-2, MS-ESS1-3, MS-PS2-4; reaches HS-PS2-4 and HS-ESS1-4.
tool.json: driver "students or teacher", minutes "10-45", modes ["Pocket", "Real Solar System"],
grades_label "Grades 6-12".

## Screens and modes
Owner-approved instrument pivot supersedes the kit frame and the game layer. No header or right pill panel.
Space fills the viewport behind a physical edge console. The console holds the matter tray, Pause, Undo, a
rotary Time dial (x0.25, x1, x4, x16), the 150-world-second rewind tape, and the clock. The dial can turn by
pointer or arrow keys and reports achieved speed when computation cannot keep up.

The second console row holds a two-position Pocket / Real Solar System switch, World and Body drawers,
Setups, Save, My universes, and the Motion / Sound / Read power panel. Manual lives at the lower-left corner,
beside the engraved plate: "Curio Class Instruments · No. 02 · Pocket Universe". This is the family's Manual
corner, also specified for Span and Spire. Drawers fold upward; books scroll inside their own viewport.

At 1366x768 and 680x425 the sky remains full width. Under 611 pixels wide the tray and transport stack, with
every main control still visible. At 375x812 the full console fits without page scrolling. All other supported
sizes remain 800x500, 1000x625, 1280x720, 1920x1080 and 760 wide. Controls reflow at real pixels.

### Pocket (default)
The painted Starter is already moving. The tray remains Star, Red dwarf, Black hole, Giant, Planet, Moon, Comet,
Dust. Pick a body to show a transparent telemetry readout with thin rules: mass in pocket units, speed relative
to its parent in world px/s, distance from that parent in world pixels, the parent name and completed laps.
Without a parent speed and distance use the simulation origin, explicitly labeled; laps read n/a.
Body exposes Follow, Pulls, Heavier, Lighter, Faster, Slower, Turn left, Turn right and Remove. World keeps the
Gravity dial, Ghost, Short / Long / Forever trails, Fit, zoom and Clear. Pocket's exaggerated mass ratios stay
visible above the console. The whirl also keeps its distributed-mass limitation visible.

### Real Solar System
The console switch enters a separately retained world and tape, beginning on 1 January 2000, with the Sun and
eight planets from the unchanged J2000 initialization. Setups can also load a fresh Real Solar System. Real
readouts use kg, km/s and AU with the same parent or origin reference. The tray remains Comet, Earth-size,
Jupiter-size, Sun-size star, Black hole. Fit cycles Inner, Giants and All. Drawn bigger than life stays visible;
World's True size switch uses physical radii with locating rings and a zoom-correct Earth diameter label.
Following Earth with Forever trails still reveals apparent backward motion and the Venus flower.

### Manual and Setups
Manual is a field guide: throw and rewind basics, model boundaries, units, keyboard controls, local saving,
and "Things people have found". The old 24 facts are short expandable entries, all available, never targets,
locked states or a checklist. Opening a note sets the Read hint and narrates it once. Setups opens from the
console or Manual, with Starter, Empty, Two suns, Three-body dance (the figure eight), Rescue the moon,
Ring lane, Black hole whirl and Real Solar System. Each is a starting point to load, break and change.

## Goals
Removed by Cory's instrument decision, 2026-11-04. No score, goal detector, goal count, sticker book,
progress persistence or award chime. The 24 concepts survive only as unnumbered field notes under Manual /
Things people have found, without target or check text. Orbital tracking remains solely for live parent/lap
telemetry, lap sounds and escape feedback. Undo, rewind, saves and replay have no achievement state.

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

Manual field-note text (opened voluntarily, never awarded; also Read):
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
11. A lighter star can let a planet go. Less mass means a weaker pull; a small speed change can decide whether it escapes.
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
  run drops to the fastest speed that holds and the Time readout shows it ("x16 running x9"). The builder measures
  this with Chrome's CPU throttle at 4x; if x4 cannot hold the full budget, lower dust to 160 and say so. At the limit
  the tray chips grey out and the hint says "Space is full: crash some together, or pick one and tap Remove."
- Sound (Web Audio, all synthesized; the kit's Sound button): throw, a short rising whoosh whose pitch follows the
  speed; lap, a soft bell, pitch by the body's kind (stars low, moons high), at most 6 chimes a second; crash, a low
  thump plus a noise burst, louder for bigger masses; into a star, a sizzle; into a black hole, a falling sub tone;
  escape, a falling whoosh that fades; close pass under 40 px, a quick pitch bend; scrubbing, a tape warble at the
  scrub speed; aiming, a faint hum that rises with the drag length.
- Shine: stars glow and pulse slowly (screen blend); trails glow and fade (8 trail colors in turn, Look); a merge
  flashes a white ring that grows and fades over 0.4 s with a few sparks; the black hole's accretion ring turns
  slowly; dust motes twinkle; the picked body has an accent ring. Motion off: no pulse, twinkle, ring growth or sparks
  (motion of the bodies is the content and stays).
- Save on this device: `Save` stores the universe as now, plus a replay (the state at the start of the scrubber's
  window and every change after it, by step number). `My universes` lists up to 12 saves (thumbnail, name you can
  edit, date) with `Load`, `Replay` (plays from the replay start at x1; all controls stay live; a change during a
  replay starts a new unsaved timeline) and `Delete` (asks once). At 12, Save asks to replace the oldest. Saves in localStorage `curio-pocket-universe` (try/catch; works with nothing saved).
- Keyboard: Space play/pause; Ctrl+Z Undo; 1 to 8 pick tray chips; Enter on a chip drops that body 200 px to the
  right of the heaviest body (in the view) with that spot's circle speed; Tab cycles bodies in the space view; F
  Follow; Delete Remove; G Ghost; arrow keys on the focused scrubber step 1 s; + and - zoom; 0 Fit. Wheel zooms at the
  pointer; drag with the right button, or two fingers, pans.
- Mode change: `Curio.stop()`, `V.hush()`; each mode keeps its own universe and scrubber while the page is open.
- Reset is `Clear` (asks once) and Setups > Starter.

## Look
Owner-approved mission-control look, 2026-11-04. Keep nebula pink #ff8fd8, the painted skies and sprites,
the luminous multi-color trails, ghost path, merge flash and quiet sky life. The subject fills the viewport;
the console is machined dark metal with inset launch slots, small screws, squared switches and an illuminated
rotary Time dial. Its engraved plate and lower-left Manual are family marks. No kit header or right pill panel.
Selected telemetry uses Consolas/monospace, physical units in Real and explicit pocket units in Pocket, thin
horizontal rules and a transparent background. Orbit labels remain readable against the sky with a dark outline.
Explanations live in the Manual; the throw hint and model honesty lines remain in view. Motion off removes
decorative movement and preserves simulation time. Text and focus retain WCAG AA contrast.

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
rings in True size, the time dial and tape, the console, telemetry and preview.svg.

## Voice
Bank casual-peer, voice Leda. Keep Curio.voice and scope by mode. welcomeAfter is false, as required by
STANDARDS for more than one mode. No line names Goals, stickers, speed pills or Wonders as a control.
Pocket welcome: "Pick from the tray. Drag in space to throw; a longer drag throws faster."
Real welcome: "Real Solar System. Turn the Time dial to sixteen." Setups retain their once-per-page how-to lines. Crash points to the rewind tape.
The Manual explains its field notes and Setups; opening a field note speaks its fact once, while Read can
repeat the current hint. Save and boundary events remain events, without celebration or scoring.
voice/lines.json equals __tool.allLines(). Reworded narration uses the browser fallback until clips are supplied.

## Family engine
None. Orbit Lab's planned astronomy engine is analytic (Kepler's equation) for one body; this tool needs an N-body
integrator, so it keeps its own in one marked block (`/* NBODY: begin */ ... /* NBODY: end */`) with no DOM access,
exposing `step()`, `snapshot()`, `restore()`, `predict(body, seconds)` and `parentOf(i)`, so a later tool could lift
it.

## Teacher note
Three ways in a period: (1) free play, then each pair shows one change and explains what pulled what;
(2) open any setup, change one variable, rewind and compare the possible futures; (3) follow Earth with Forever
trails and compare the inner and outer planets, then consult the Manual to name a pattern. No target set or
class competition is built in. Standards remain MS-ESS1-2, MS-ESS1-3, MS-PS2-4, HS-PS2-4 and HS-ESS1-4 through
the same physics, scale comparisons, mass controls and evidence from student experiments.

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
3. Rescue: the moon crashes at about 15.7 s; scrub to the start, Slower 5 times, and the moon survives ten laps; Faster makes it crash sooner.
4. No goals, targets, sticker storage or award events remain. Manual has the 24 field notes and Setups
   can load all eight starting points, including a fresh Real Solar System.
5. Real Solar System: following Earth from 1 Jan 2000, Mars starts backing up in May 2001; Venus flower appears with
   Trails Forever by early 2008; Neptune's lap takes about 20.5 s at x16.
6. Focus: the space view is the biggest thing at 1366x768 and in the 680x425 preview; tray and time bar visible
   without scrolling at every size in STANDARDS.md; labels at least 10 px in the preview.
7. A tap while anything moves: the Time dial, Pause, Faster, Heavier, Gravity and the scrubber all change what is
   shown on the next frame; aiming holds time and release resumes.
8. Full budget (20 bodies, 240 dust) holds 60 frames a second at x4 under 4x CPU throttle, or the Time readout shows
   the real speed; the chips grey out at the limit with the full line.
9. Save, reload the page, `My universes` > Replay plays the same throws and crashes; saves survive a reload;
   private window (no storage) still plays.
10. How-to lines once each, no removed control named, no line names a hidden or disabled
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
