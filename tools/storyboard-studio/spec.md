# Storyboard Studio

## One idea
Every panel is a camera you place on the floor plan: how far away sets the shot size, how high sets the angle, and which side of the line between the actors you stand on sets who looks left and who looks right, so the animatic shows you exactly where a cut keeps the audience oriented and where it jumps the line.

## Not like
- city-skyline-studio (9-12): the camera fixes the perspective of one still drawing. Here the camera changes every panel and the subject is the cut between panels: what the audience knows and feels from one shot to the next.
- frame-it (6-8): composes one photo (thirds, leading lines). Here composition is automatic; the choices are shot size, angle, side of the line and order.
- stage-blocker (6-8) and director-s-chair (9-12, theater): the audience sits in one place and the actors move. Here the actors' blocking is fixed by the script and the audience's eye (the camera) moves.
- flipbook-studio (6-8, same group): draw every frame of one motion yourself. Here nothing is drawn by hand; you choose shots, order and timing for a whole scene.
- virtual-gallery (9-12): a sequence through space for a visitor; here a sequence through time for a viewer.

## Who and how
- Grade 9-12, media arts, module "Film and Video Production (Media Arts)".
- Topic line: shots, angles and continuity in film
- Driver: students (laptops, alone or in pairs). 25 to 45 minutes; boards are saved on this device.
- Standards: NCAS Media Arts MA:Cr1.1.HSI (generate ideas: plan a scene), MA:Cr2.1.HSI (develop and refine a plan: the board), MA:Cr3.1.HSI (refine for intent: fix continuity, retime); also MA:Re7.1.HSI (continuity and shot order manage the audience experience).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Kit `theme-912`. Scene picker in the panel top: `The Last Slice` / `Late Bus`. Modes (`.seg`): `Plan` (default), `Board`, `Animatic`.

**Plan.** Focus: the viewfinder, the largest thing on the stage (about 60% of the stage width at 1366x768), with the plan beside it where the camera is dragged. Stage left: the set from above (top-down plan, real pixels, 1 m grid at 10% white): characters as colored circles with a facing wedge, props, and the line (axis of action) as a dashed yellow line through the two characters (The Last Slice) or along the runner's path (Late Bus), labeled "The line". The current panel's camera is a camera icon with its field-of-view wedge; earlier panels' cameras show as faint numbered ghosts. Stage right: the viewfinder, 16:9, showing what this camera sees (drawn in code: Content "Drawing"). Over the viewfinder: shot size name, lens, height, and "Side A", "Side B" or "On the line".
- Drag the camera on the plan (arrow keys move it 0.25 m, Shift 1 m). It always aims at the `Aim at` target, so moving it orbits naturally.
- Panel controls: `Aim at` (Ash / Remy / Both / Slice in The Last Slice; Nico / Bus / Stop in Late Bus), `Lens` (24 / 35 / 50 / 85 mm), `Height` (Low / Eye / High / Overhead), `Beat` (which script beat this panel covers; the beat line shows under the viewfinder), `Duration` (0.5 to 8 s, steps of 0.5), `Into this panel` (Cut / Dissolve / Fade from black).
- Buttons: `Add panel` (new camera at the current one's spot, next in order), `Duplicate`, `Delete panel`, `Prev` / `Next` panel.

**Board.** Focus: the grid of panels with the markers between them, filling the stage. The storyboard as a grid of panels (viewfinder drawings at thumbnail size), each with its number, shot size, lens, height, beat text, duration and transition. Drag to reorder (keyboard: select, then `Move earlier` / `Move later`). Between two panels, a marker appears when the cut has a problem (Content "Continuity checks"), with words and an icon: "Line crossed" or "Jump cut". Tap a marker to see why (a tiny plan with both cameras and the line) and `Go to panel`. A notes strip under the grid: "Beats with no panel: 4, 7" and "Running time 0:21". `Print board` (black on white: 6 panels a page with all notes). `Fix this board` loads the scene's sample board (Content) as a copy; `My board` returns to the student's board.

**Animatic.** Focus: the viewfinder, filling the stage. It plays the panels in order at their durations with their transitions; `Captions` toggle shows each beat line at the bottom. A thin timeline under it shows panel blocks to scale, with continuity markers on the cuts; tapping a block jumps there at once. At a "Line crossed" cut the animatic pauses 1 s on a split overlay: the last frame and the next frame side by side with arrows showing who swapped sides of the screen (only with `Show problems` on, default on). `Play`, `Stop`, `Step` (next panel), `Back`, `From panel` (starts at the selected one). Every control works while it plays and acts in the same frame: Stop holds the current frame, Step and Back stop and move one panel, a timeline tap or `Show problems` change shows at once, and a tap during the 1 s pause ends the pause. With Motion off, dissolves and fades become cuts but keep their time (a held frame), so timing is unchanged.

## Content
**Scene 1, The Last Slice.** Set: a pizza place, plan 8 m wide x 6 m deep; a table at the center (1.2 m x 0.8 m), a tray with one slice at (0, 0), the door at (0, -3), a window along the back wall (y = +3). Ash (teal hoodie) seated at (-0.6, 0) facing +x; Remy (yellow jacket) seated at (+0.6, 0) facing -x. Seated eye height 1.2 m; the table top and slice at 0.75 m. The line runs through Ash and Remy (along x). Beats:
1. Ash and Remy share a pizza. One slice is left.
2. Ash looks at the last slice.
3. Remy looks at it too.
4. They both reach at once.
5. Their hands stop over the slice.
6. Ash pulls back and shrugs.
7. Remy slides the tray across to Ash.
8. Ash grins and tears the slice in half.
Poses per beat (drawn in code): head direction (at the other person or at the slice), an arm forward on 4 and 5, Remy's arm pushing on 7, a raised-shoulders shrug on 6.

**Scene 2, Late Bus.** Set: a sidewalk 24 m long along x, street on the +y side, bus stop sign at (+9, 1). Nico (violet backpack) runs from (-10, 0) toward +x; the bus drives along y = 3 toward +x and stops at x = +9. The line runs along Nico's path (y = 0). Aim heights: Nico's head 1.6 m, the bus doors 1.5 m (at the bus's x, y = 3), the stop sign 2.0 m. The bus is at x = -12 on beat 1, -2 on beat 2 and +9 from beat 3 on. Beats with Nico's x position: 1. Nico checks the time. Late. (-10) 2. Nico runs. (-6) 3. The bus pulls up to the stop. (Nico at -3, bus at +9) 4. Nico runs faster. (0) 5. The bus doors start to close. (+4) 6. Nico waves an arm. (+6) 7. The doors open again. (+8)

**Sample boards** (for `Fix this board`):
- The Last Slice, 8 panels, panel n on beat n, 2 s each, all Eye height except panel 5: 1 wide from (0, -3.5) 24 mm aim Both; 2 MCU over Remy's shoulder (1.6, -0.6) 50 mm aim Ash; 3 MCU over Ash's shoulder (-1.6, -0.6) 50 mm aim Remy; 4 medium from (0, -2.2) 35 mm aim Both; 5 close-up of the slice from (0.3, -0.9) High 85 mm aim Slice; 6 MCU of Ash from (1.6, +0.6) 50 mm (crosses the line: Side B); 7 MCU of Remy from (-1.6, -0.6) 50 mm aim Remy; 8 the same camera turned 10 degrees around Remy, away from the line, to (-1.46, -0.97), same lens and height. Markers: Line crossed at 5 to 6 and at 6 to 7, Jump cut at 7 to 8. The fix: move panel 6's camera to y < 0, for example (1.6, -0.6) (clears both crossings), and delete panel 8 or move its camera 30 degrees or more (a lens change alone leaves it one size step away, still a jump cut). Panel 5 was 50 mm in the old spec, which frames 0.84 m (a medium close-up, not the close-up its label says).
- Late Bus, 6 panels, panel n on beat n (beat 7 has no panel), 2 s each, all Eye height: 1 wide from (-8, -6) 24 mm aim Nico; 2 MCU from (-4, -3) 85 mm aim Nico; 3 wide of the bus from (6, -6) 35 mm aim Bus; 4 medium of Nico from (0, +4) 50 mm aim Nico (crosses: Nico now runs right to left); 5 MCU of the doors from (9, -0.5) 85 mm aim Bus; 6 medium of Nico from (6, -3) 50 mm aim Nico. Markers: Line crossed at 3 to 4 and at 4 to 5. The fix: put panel 4's camera on the -y side, for example (0, -4) (clears both). In the old spec panel 2 was a medium, which turned 15 degrees from panel 1 on the same target one size step away and so fired an unlisted Jump cut; as an MCU it is two steps from panel 1's wide. Panel 5 was a close-up from (9, -1.5), which no lens here can frame (85 mm gives 1.07 m).

**Shot sizes** (from the height of the frame at the aimed subject's distance, H = 2 d tan(vertical field / 2), d the straight-line distance from the camera at its height to the aim point; Both aims at the midpoint of Ash and Remy at 1.2 m; cutoffs are the tool's own, the names are standard): Extreme wide H over 6 m; Wide 2 to 6 m (whole body and surroundings); Medium 1 to 2 m (waist up); Medium close-up 0.6 to 1 m (chest up); Close-up 0.3 to 0.6 m (face); Extreme close-up under 0.3 m (a detail).
**Lenses:** vertical field of view for a 16:9 full-frame image (20.25 mm tall): 24 mm 45.7 degrees, 35 mm 32.3, 50 mm 22.9, 85 mm 13.6 (from 2 atan(10.125 / f)).
**Heights:** Low 0.5 m, Eye 1.2 m (seated scene) or 1.6 m (Late Bus), High 2.6 m, Overhead 4 m looking straight down. The tilt aims at the target's head height.

**Continuity checks** (between consecutive panels in the same scene):
- Line crossed: the two cameras are on opposite sides of the line, and neither is neutral. Neutral means within 0.3 m of the line (looking along it) or Overhead. Note: "Crossing the line flips who is on the left. The audience can lose track of where people are. A neutral shot in between lets you cross."
- Jump cut: same aim target, the camera direction to the target changes by less than 30 degrees, and the shot size is the same or one step apart. Note: "Two very similar shots in a row look like a glitch. Change the angle by 30 degrees or more, or change the shot size by two steps."
- These are conventions of continuity editing, not laws: each note ends "Filmmakers break this on purpose sometimes. If you do, mean it."

**Drawing** (viewfinder, in code): a simple 3D projection; characters as smooth mannequins (body capsule, head sphere with a nose wedge so facing reads, arms as capsules) in each character's color; table, tray, slice, sign, bus as boxes and flat shapes; everything else in three marker grays like a hand storyboard. No faces drawn beyond the nose wedge.

## Interactions in detail
- Side: the sign of the cross product of the line's direction (Ash to Remy; Nico's run direction) with (camera minus Ash, or minus Nico's start); in both scenes that is the sign of the camera's y. Shown as "Side A / Side B / On the line" (within 0.3 m of the line, or Overhead).
- The camera can't enter the table or a character (it stops 0.3 m away); it can leave the set by up to 4 m (the plan pans).
- Shot size updates live while dragging; so do the side label and, in the strip, any continuity markers for the cuts into and out of this panel.
- Panels: 1 to 12 per board; each scene has its own board. Deleting the last panel is not allowed (button disabled).
- Durations total 1:36 at most (12 x 8 s). Running time shows as m:ss. The animatic can run past 30 s because it plays the student's own board at the times they set (both sample boards run 16 s and 12 s); every control stays live while it plays.
- Print: viewfinder drawings in grayscale with character colors as outline patterns so they print in black and white.
- Save: both boards save on this device on every change (localStorage `storyboard-studio-boards`); `Clear board` (with a confirm) resets the current scene's board to one wide panel. `Fix this board` never overwrites the student's own board.
- Sizes: plan and viewfinder side by side with the panel controls visible at 1366x768 and up, the viewfinder the wider; at 1000 px and under, the viewfinder stacks above the plan with the controls as one compact row; in the 680x425 preview the viewfinder is the main view with the plan as an inset. At 375 wide: viewfinder, then plan, then controls.

## Look
- Accent (`--brand`) #ff6b6b tally-light red, `--brand-ink` #2a0a0a. Kit `theme-912` base: screening-room dark. The line #ffd166 dashed; cameras white with the current one in the accent; characters Ash #3fb8af, Remy #f2c14e, Nico #a78bfa; viewfinder marker grays #e9e9e6, #8a8f98, #4a4f58 on a paper panel.
- Contrast (rechecked in Python): accent on panel 6.24:1, on section 5.91:1; brand-ink on accent 6.6:1; the line on panel 12.0:1. Markers always pair color with words and an icon.
- Differs from city-skyline-studio (cyan), gallery-critique (pink), virtual-gallery (lime), theory-gym (blue) music-history-radio (magic-eye green on bakelite) and the theme's default amber.

## Art
none: drawn in code. Every viewfinder frame is a 3D projection from a camera the student can put anywhere on the plan at four heights and four lenses, so the mannequins and sets must be redrawn from any angle, which a painted image can't do; the plan is a diagram. The plain mannequins in marker grays are the look of a hand-drawn storyboard on purpose.

## Voice
Bank voice: `smooth-narrator` (a film-school teacher who talks like a narrator; different from every tool in this group, from city-skyline-studio's casual-peer and from every spec in this batch). Style: smooth, warm, unhurried. Uses `Curio.voice`, scope = mode.
- welcomePlan (how; Plan entered; stale once the camera is dragged): "Drag the camera on the plan. The viewfinder shows the shot. Then tap Add panel for the next one."
- lineHow (how; the first time a board has 2 panels; stale when the camera next moves): "The yellow line runs between the actors. Keep the camera on one side and they stay on their own side of the screen."
- welcomeBoard (how; Board entered; stale once a panel is dragged or a marker tapped): "Here is your board. Drag a panel to change the order."
- markerHow (how; the first time Board shows a marker; stale once a marker is tapped): "Tap a marker between two panels to see what went wrong."
- welcomeAnimatic (how; Animatic entered; stale when Play is pressed): "Press Play to watch your board in time."
- lineCrossed (event; every time a cut into the current panel newly becomes crossed; stale when that panel changes again): "That cut crosses the line. Ash and Remy just swapped sides of the screen." (Late Bus: "That cut crosses the line. Nico now runs the other way.")
- jumpCut (event; same trigger and staleness for a jump cut): "These two shots are almost the same. Move the camera 30 degrees, or change the shot size by two steps."
- fixedBoard (event; each time the sample board reaches no markers; stale on the next change): "Clean cuts all the way through. Go to Animatic and press Play to see how it flows."
- animaticPause (event; at each crossed-line pause in Animatic; stale when the pause ends or is tapped away): "Watch the sides swap here."

## Family engine
none

## Sources
- NCAS Media Arts MA:Cr1.1, MA:Cr2.1, MA:Cr3.1, high school proficient: https://www.nationalartsstandards.org/
- 180-degree system, axis of action, eyeline and screen direction, 30-degree rule, shot scale names: David Bordwell, Kristin Thompson and Jeff Smith, Film Art: An Introduction, 12th ed. (McGraw-Hill, 2019), ch. 5 "The Shot: Cinematography" and ch. 6 "The Relation of Shot to Shot: Editing".
- Storyboards and animatics as planning tools; neutral shots to cross the line: Steven D. Katz, Film Directing Shot by Shot (Michael Wiese Productions, 1991), ch. 1 to 3 and the chapters on continuity.
- Field of view from focal length (angle = 2 atan(image height / 2f)); full-frame 36 x 24 mm cropped to 16:9 is 36 x 20.25 mm: standard thin-lens geometry; values computed for this spec.
- Scripts, sets, characters and sample boards: written for this tool.
- Number checks (Python, 2026-10-29), with d the straight-line distance from the camera at its height to the aim point: lens fields 45.7, 32.3, 22.9 and 13.6 degrees. The Last Slice panels frame 2.95 m (wide), 0.92, 0.92 (MCU), 1.27 (medium), 0.50 (close-up, at 85 mm), 0.92, 0.92, 0.92 m; markers exactly Line crossed 5 to 6 and 6 to 7, Jump cut 7 to 8 (10.0 degrees, same size); with panel 6 at (1.6, -0.6) and panel 8 deleted, no markers; panel 8 at 85 mm (0.54 m, close-up) still jumps. Late Bus panels frame 5.34 (wide), 0.86 (MCU), 5.49 (wide), 1.62 (medium), 0.83 (MCU), 1.22 m (medium); markers exactly Line crossed 3 to 4 and 4 to 5; with panel 4 at (0, -4), no markers. Old values that failed: The Last Slice panel 5 at 50 mm framed 0.84 m (MCU, labeled close-up); Late Bus panel 2 as a 50 mm medium fired a Jump cut from panel 1 (15.3 degrees, one size step); Late Bus panel 5 from (9, -1.5) could not be a close-up with any lens. Contrast ratios in Look recomputed.

## Done when
1. Shot size labels match the formula for six placements (recompute H with the lens table), including one at each cutoff.
2. The side label flips exactly when the camera crosses the line; a camera within 0.3 m of the line or Overhead reads "On the line" and never triggers Line crossed.
3. Both sample boards show exactly the markers listed in Content, and the listed fixes clear them.
4. Jump cut fires at 29 degrees with the same shot size and not at 31 degrees or with a two-step size change.
5. The animatic plays durations to within 50 ms per panel, dissolves and fades take their time, and with Motion off the timing is unchanged.
6. A tap while the animatic plays: Stop, Step, Back, a timeline block and Show problems act in the same frame, and a tap ends the 1 s line-crossed pause at once.
7. Focus: the viewfinder is the largest thing in Plan and fills the stage in Animatic at 1366x768 and 680x425; the panel grid fills the stage in Board.
8. Reorder by drag and by keyboard; deleting is blocked at one panel; beats with no panel are listed.
9. Print board is black on white with all notes; boards survive a reload; Fix this board never touches My board.
10. Plan camera, viewfinder and Add panel are visible without scrolling at every STANDARDS.md size.
11. How lines once in five panels added in a row; lineCrossed and jumpCut spoken every time they newly happen and dropped when stale; markerHow never plays on a board with no marker.
