# Virtual Gallery

## One idea
Choose and hang a show from a portfolio, then send a visitor through the door: the walk shows what they see first, where the line of frames breaks, which labels run long and whether the order tells your story, and the juror's checklist says what to fix before opening night.

## Not like
- gallery-critique (9-12, roleplay, same group): argues about one finished painting. Here you are the one presenting, choosing and ordering many works; nobody debates.
- city-skyline-studio (9-12, same group): a perspective construction to draw over. The room here is a simple walk-through stage, never a drawing tool.
- art-passport and art-through-time (the art-museum family): museum masterpieces. Here the works are a student portfolio (a made-up student's, or your own photos).
- brand-builder (9-12): designs a brand kit. Here nothing is designed except the show's order, hang and words.
- storyboard-studio (9-12): sequence of shots over time; here sequence is a walk through space.

## Who and how
- Grade 9-12, visual arts, module "Portfolio and Curation (Visual Arts)".
- Topic line: curating and presenting a portfolio
- Driver: students (laptops, alone or in pairs). 25 to 45 minutes; the show is saved on this device so it can continue next class.
- Standards: NCAS VA:Pr4 (select, analyze and interpret work for presentation), VA:Pr5 (develop and refine techniques for presentation), VA:Pr6 (convey meaning through presentation).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Kit theme `theme-912`. Modes (`.seg`): `Select`, `Hang` (the default once 1 work is chosen; `Select` is the default on first load), `Walk`, `Checklist`.

**Select.** Focus: the portfolio grid of 14 painted works, the largest thing on screen, with the brief card above it. A brief card at the top (Content "Shows"): `Where I'm From`, `Water`, `Your theme` (pick one of the five theme tags). Under it the portfolio: 14 works by Jordan Reyes, a made-up high school artist (Content), as cards with image, title, medium, size, year and theme tags. Tap a card to see it big with its details and `Add to show` or `Remove`. A counter: "6 of 6 to 8 chosen". `Star` marks one chosen work as the show's anchor (the one you most want seen). `Add your own` opens a file picker (images only, up to 12): your images join the portfolio for this visit only, with a title field and theme tags you set; a line says "Your own pictures stay on this computer and disappear when you close the page."

**Hang.** Focus: the room, filling the stage, with the selected work's tools beside it. Stage: the gallery room in a three-quarter view from above the door (a simple 3D box: three hangable walls and the door wall with space either side of the door), drawn at real pixels with CSS 3D, its faces covered with the painted plaster and oak textures (Art). Panel: the chosen works as a tray (in the order they will be walked), then tools.
- Drag a work from the tray onto a wall; it hangs at the wall's current center line and slides along the wall. Drag it off the wall back to the tray. Arrow keys move the selected work 5 cm along the wall, Shift 25 cm.
- `Plan` toggle: a top-down plan in the panel, with each wall as a line, frames as ticks with their widths, the door, and the visitor's path; works can be moved on the plan too.
- Per wall: `Center line` slider (120 to 170 cm from the floor), shown on the wall as a faint dashed line with its height in cm and inches.
- Per work: `Light` toggle (a spotlight; unlit works hang in dim light), `Label` editor (title, one-line note), `Bring to front of tray order` and `Move later` (changes walk order), `Remove from wall`.
- `Statement`: opens the artist statement panel, which hangs as an intro panel beside the door.
- The label of each work hangs to its right with its center at 137 cm (54 in) automatically (Content "Rules").
- `Auto space` on a wall spreads its works with equal gaps (an assist; the check still runs).

**Walk.** Focus: the first-person view, filling the stage, with the order strip under it. A first-person view from the door at 160 cm eye height, the same textured room. `Walk the show` moves the visitor along the path (clockwise from the door by default; `Counterclockwise` toggle) and pauses at each work in walk order (2 s each; instant cuts with Motion off and the same 2 s pauses). At each stop the work's label is shown large, readable as in the room. A strip at the bottom shows the order with a mark between any two neighbors that share no theme tag ("jump"). From the door, before walking, a cone shows what a visitor sees first; the first-seen work (Interactions) is named: "First seen: Creek After Rain". `Step` moves one stop; `Back`; `Stop`. Every control works while the walk plays and acts in the same frame: Stop halts where the visitor stands, Step and Back stop and move one stop, a tap on a work in the order strip jumps there, and the Counterclockwise toggle restarts the walk from the door at once. Each move between stops takes 1 s, so a full walk of 8 works is about 24 s.

**Checklist.** Focus: the list of checks, one centered column. The juror's checklist, live (Content "Checks"), each line with a tick or a cross icon, the word, and the numbers, and a `Show me` button that jumps to Hang with the problem highlighted. Under it: `Print show` (a black-on-white sheet: show title, statement, plan with numbers, and each work's label) and `Clear show` (with a confirm).

## Content
**Portfolio** (Jordan Reyes, made up for this tool; id, title, medium, size in cm, year, tags):
1. window: Kitchen Window, 7 a.m., watercolor on paper, 30 x 40, 2025, home.
2. teapot: The Blue Teapot, colored pencil on paper, 28 x 36, 2024, home.
3. creek: Creek After Rain, acrylic on canvas, 46 x 61, 2025, water, growing.
4. busstop: Bus Stop, 10 p.m., oil pastel on paper, 30 x 45, 2025, city, night.
5. crows: Crows on the Wire, linocut print, black ink, 23 x 30, 2024, city.
6. laundromat: Laundromat, ink and wash, 36 x 48, 2025, city, home.
7. tidepool: Tide Pool, collage of painted papers, 40 x 40, 2024, water.
8. seeds: Seed Packets, gouache on paper, 25 x 33, 2025, growing, home.
9. bowl: Wave Bowl, glazed stoneware, 18 cm across, 2025, water. (An object: hangs on a wall shelf, shown on a plinth icon.)
10. fireescape: Fire Escape Garden, digital photograph, 40 x 50 print, 2025, city, growing.
11. rainglass: Rain on the Window, digital photograph, 40 x 50 print, 2024, water, home.
12. blockmap: Map of My Block, mixed-media collage, 50 x 50, 2025, home, city.
13. tomatoes: Tomato Plants in August, charcoal on paper, 45 x 60, 2024, growing.
14. nightpool: Night Pool, acrylic on canvas, 50 x 70, 2025, water, night.
Tags: home, water, city, growing, night.

**Shows** (brief text; theme):
- Where I'm From: "The senior show asks: where are you from? Pick 6 to 8 works that answer it." Theme home (6 works carry it: window, teapot, laundromat, seeds, rainglass, blockmap).
- Water: "The spring show's theme is water. Pick 6 to 8 works." Theme water (5 carry it: creek, tidepool, bowl, rainglass, nightpool), so one or more must be chosen on another strength; the checklist needs only 5.
- Your theme: "Name your own show. Pick a theme tag and 6 to 8 works." City carries 5 (busstop, crows, laundromat, fireescape, blockmap) and can pass; growing carries only 4 (creek, seeds, fireescape, tomatoes) and night only 2 (busstop, nightpool), so for those the checklist shows the student the portfolio can't support the show (a real curating lesson), and says so. (The old spec named only night; growing fails the same check.)

**Room:** 8 m wide (back wall), 6 m deep (side walls), 3.2 m high; door 1.2 m wide in the middle of the front wall, leaving 3.4 m of hangable wall each side. Visitor eye height 160 cm in Walk (the camera height, a setting).

**Rules** (shown in a small "Why" note beside each check):
- Wall labels: center at 137 cm (54 in) from the floor; labels between 122 and 168 cm (48 to 67 in) read comfortably seated and standing.
- Label and statement text: no sentence over 25 words; a label at most 75 to 100 words (the tool uses 100 for the statement and 25 words for a work's note).
- A seated visitor's eye level is about 109 to 130 cm (43 to 51 in); the Center line slider shows this band on the wall as a faint strip.
- The other checks (one center line, even gaps, every work lit, flow) are curating practices this tool teaches, not fixed rules; their notes say "Common practice, not a law."

**Checks:**
1. Selection: 6 to 8 works chosen and all hung.
2. Theme: at least 5 hung works carry the show's theme tag.
3. Anchor: the starred work is "First seen" from the door.
4. Line: on each wall, work centers are on the wall's center line (works auto-snap; this fails only if a wall line differs from another by more than 3 cm, "Your walls use different center lines: 145 and 152 cm").
5. Spacing: on each wall with 2 or more works, gaps between frames are even (largest minus smallest is 15% of the mean or less) and at least 30 cm.
6. Light: every hung work is lit.
7. Labels: every work has a title; every note is 25 words or fewer.
8. Statement: written, 100 words or fewer, no sentence over 25 words.
9. Flow: at most one jump in walk order.

## Interactions in detail
- First seen: from the door point (center of the door, 160 cm), the work on any wall whose nearest frame edge is the smallest angle from the straight-ahead line (a work the line passes through scores 0; ties go to the larger work). So a big work near the center beats a small one at the center's edge, and with the back wall empty a side wall's nearest work wins.
- Frames: each work's frame size is its real size plus a 5 cm mat and 3 cm frame; the bowl sits on a 30 cm shelf. Works can't overlap on a wall (they push apart) or run past a corner or into the door gap.
- Gaps are measured frame edge to frame edge, in cm, shown on the wall while dragging.
- Walk order: the tray order; dragging in the tray reorders. `Walk the show` uses it, not wall position, so a curator can choose a path; if the order zigzags across the room, the path line on the plan crosses itself and the check notes "Your path crosses itself" (a warning, not a fail).
- Word counts split on spaces; sentences split on ., ! and ?. Counts show live beside each text box.
- Saving: the show (chosen ids, star, wall positions, center lines, lights, order, labels, statement, show choice) is saved on this device (localStorage `virtual-gallery-show`) on every change; `Clear show` empties it. Own images are never saved; a saved show that referenced them drops those works on reload and says "Your own pictures were not saved, so they left the show."
- Text fields never leave the page; no names are asked for (the artist is the made-up Jordan Reyes, or "Your name here" left blank for own work, never stored).
- Sizes: the room fills the stage at real pixels with walls at least 260 px wide at 1366x768; in the 680x425 preview the plan replaces the 3D view. At 375 wide the plan is the hang view and Walk is full width.

## Look
- Kit `theme-912` base; accent (`--brand`) #b8e07a gallery lime. Room: painted warm white plaster walls (base color #f2efe9 under the texture), painted oak plank floor (base #b98a5a), ceiling #e6e2da, spotlight pools as soft radial gradients in code; labels on white with ink #2b2a28.
- Contrast (rechecked in Python): brand on panel 11.52:1; brand on section 10.92:1; brand-ink #1c1203 on brand 12.29:1; label ink on wall 12.49:1, on the white label 14.34:1.
- Different from gallery-critique (pink on a charcoal wall), city-skyline-studio (cyan), storyboard-studio (red on dark), music-history-radio (green on bakelite), theory-gym (blue on maple), and the art-museum tools' warm gilt look.

## Art
Local FLUX (`scripts/localart.py`), no people, no lettering. 16 images, none for Gemini. Portfolio style line, added to every work's prompt: "a real high school student's artwork, photographed flat and evenly lit, the artwork filling the whole picture edge to edge". Each 3:4 portrait, the listed size read as width x height (1:1 for tidepool, bowl and blockmap), webp, long side 800 px, 50 KB or less; cutout no unless marked; people no; used on the portfolio cards, the big view, inside the frames on the walls, in Walk and on the printed sheet.
- window: a loose watercolor of a kitchen window at early morning, a mug and a plant on the sill, soft yellow light; 3:4.
- teapot: a colored pencil still life of a blue teapot on a checked cloth; 3:4.
- creek: an acrylic painting of a small creek after rain, wet rocks and bright green banks; 3:4.
- busstop: an oil pastel drawing of an empty bus stop shelter with plain blank glass panels at night under a streetlight; 3:4.
- crows: a black ink linocut print of crows on a power line on white paper; 3:4.
- laundromat: an ink and gray wash drawing of an empty laundromat, washing machines in a row; 3:4.
- tidepool: a collage of torn painted papers showing a tide pool with starfish and shells; 1:1.
- seeds: a gouache painting of plain blank paper seed packets and small pots of seedlings on a table; 3:4.
- bowl: a glazed stoneware bowl with a blue wave pattern, seen from slightly above, on a plain white background; 1:1; cutout yes; sits on the code wall shelf.
- fireescape: a photograph of potted plants and herbs on a city fire escape, afternoon light; 3:4.
- rainglass: a photograph of rain drops on a window with blurred city lights behind; 3:4.
- blockmap: a mixed-media collage map of a few city blocks, with paper roofs, painted streets and string paths; 1:1.
- tomatoes: a charcoal drawing of tall tomato plants in a garden; 3:4.
- nightpool: an acrylic painting of an empty outdoor swimming pool at night, glowing blue water; 3:4.
- vg-wall: "A seamless texture of smooth warm white gallery wall plaster, very faint soft shading, evenly lit, filling the frame"; 1:1; cutout no; people no; tiled on the three hangable walls and the door wall in Hang and Walk.
- vg-floor: "A seamless top-down texture of honey oak floor planks running in one direction, soft satin finish, evenly lit, filling the frame"; 1:1; cutout no; people no; tiled on the floor in Hang and Walk.
- Drawn in code: the room geometry, frames and mats (sized to each work), the wall shelf and plinth icon, the labels and their text, spotlights, the plan, the cone and the order strip, all of which must take sizes and positions the student sets.

## Voice
Bank voice: `wise-mentor` (the art teacher helping you prepare a show; different from every tool in this group, from stage-blocker's firm-captain and from every spec in this batch). Style: thoughtful and warm, short. Uses `Curio.voice`, scope = mode.
- welcomeSelect (how; Select entered; stale once a work is added): "Read the brief, then tap a work and tap Add to show. Star the one you most want seen."
- welcomeHang (how; Hang entered; stale once a work is hung): "Drag a work from the tray onto a wall."
- lightHow (how; the first hung work; stale once Light or Label is used): "Tap the hung work, then tap Light and fill in its Label."
- welcomeWalk (how; Walk entered; stale when Walk the show or Step is pressed): "Tap Walk the show to follow a visitor through the door."
- firstSeen (event; each time Walk is entered or the hang changes the first-seen work; stale when Walk is left or the walk starts): "From the door, a visitor sees (title) first."
- jump (event; at each jump the walk reaches; stale at the next stop): "Here the story jumps. Nothing ties these two together."
- welcomeChecklist (how; Checklist entered with a check not ticked; stale once Show me is tapped): "Here is what the juror will check. Tap Show me on anything not ticked."
- allTicked (event; each time the last check turns ticked; stale when one turns back): "Every check is ticked. Your show is ready to open."
- themeShort (event; Your theme set to growing or night; stale when the theme changes): "Only (n) works carry that theme, and the show needs five. That's worth knowing before you start." (n is 4 or 2.)

## Family engine
None.

## Sources
- NCAS Visual Arts VA:Pr4, VA:Pr5, VA:Pr6: https://www.nationalartsstandards.org/
- Wall label height (48 to 67 in, center 54 in optimal), seated eye level (43 to 51 in), sentence length (25 words or fewer), label length (75 to 100 words at most): Smithsonian Guidelines for Accessible Exhibition Design, sections II and III, https://www.sifacilities.si.edu/sites/default/files/Files/Accessibility/accessible-exhibition-design1.pdf
- Selection, sequence and presentation as curating practice: College Board, AP Art and Design Course and Exam Description (2020), Sustained Investigation and Selected Works, https://apcentral.collegeboard.org/courses/ap-art-and-design
- Portfolio works, artist and room are made up for this tool.
- Number checks (Python, 2026-10-29): tag counts home 6, water 5, city 5, growing 4, night 2 (the old spec flagged only night; growing also fails the 5-work theme check, hence themeShort). Room: (800 - 120) / 2 = 340 cm of wall each side of the door. Frames add 16 cm to each side length; the 8 widest framed works with 30 cm gaps need 745 cm, inside the 800 cm back wall, and one 340 cm door-side wall holds 3 of the widest. Ordering all 6 home works, or all 5 water works, together gives 0 jumps, so Flow can pass. Spacing examples: gaps 40, 40, 46 spread 14.3% (pass), 40, 40, 47 spread 16.5% (fail). Unit conversions: 137 cm is 53.9 in, 122 to 168 cm is 48.0 to 66.1 in, 109 to 130 cm is 42.9 to 51.2 in, all matching the source in inches. Walk: 8 stops of 2 s plus 8 moves of 1 s is 24 s. Contrast ratios in Look recomputed.

## Done when
1. Each show's theme counts match Content (6 home, 5 water; Your theme: city 5, growing 4, night 2) and themeShort plays for growing and night only.
2. Hanging, moving along a wall and returning to the tray all work by pointer and keyboard; works never overlap, pass a corner or cover the door.
3. First seen names the right work for three layouts (back wall full, back wall empty, anchor on a side wall).
4. Every check flips correctly: test one failing and one passing case each (spacing at 14.3% and 16.5%, a 26-word note, a 101-word statement).
5. Walk visits works in tray order with labels readable; jumps are marked where neighbors share no tag.
6. A tap while the walk plays: Stop, Step, Back and an order-strip tap act in the same frame; the walk lasts about 24 s for 8 works.
7. Focus: the portfolio grid in Select, the room in Hang and the first-person view in Walk are each the largest thing on screen at 1366x768 and 680x425 (where the plan stands in for the room).
8. Own images join the portfolio, never persist, and a reload drops them with the message.
9. The saved show survives a reload; `Clear show` empties localStorage.
10. Tray, room and the selected work's tools are visible without scrolling at every STANDARDS.md size.
11. How lines once in five hangs in a row; firstSeen and jump every time, dropped when stale; no line names a control that is off.
12. All 16 images load, none shows a person or fake lettering.
