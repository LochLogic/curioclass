# Flipbook Studio

## One idea
Timing is the animation: keep the same drawings and only change how long each one stays on screen, and a ball goes from robot to rubber, a blink from lazy to startled; a hold strip under the pages and a spacing chart over them make that timing something you can see and drag.

## Not like
- frame-it (6-8, built): composes one still photo with a camera. Here nothing is a camera; it is a stack of drawings and the time between them.
- vanishing-point-studio (6-8, built) and city-skyline-studio (9-12): drawing over geometry guides. Here the guide is a timing chart, and the drawing is loose pencil on purpose.
- design-fixer (6-8): fixes one still layout for the eye. Here the subject is change over time.
- storyboard-studio (9-12, same group): plans camera shots and cuts for a whole scene. Here you draw every frame yourself and work inside one shot, one motion.
- brand-builder (9-12, same group): clean vector design for print and screens. Here it is a sketchbook and a pencil.
- beat-lab and band-practice (music): timing in sound. Here timing is in pictures; there is no music.

## Who and how
- Grade 6-8, media arts, module "Animation Basics (Media Arts)".
- Topic line: frames, timing and spacing in animation
- Driver: students (laptops or tablets, alone or in pairs). 15 to 40 minutes; the book is saved on this device.
- Standards: NCAS Media Arts MA:Cr2.1.6-8 (develop, refine and model a media artwork), MA:Cr3.1.6-8 (refine for intent: here timing), MA:Pr5.1.6-8 (skills for producing: animation tools and techniques).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Draw` (default), `Time`, `Flip`.

The book is always the stage: one page (4:3, drawn at real pixels) on a desk, with the page corner curled. Under it, in every mode, the **frame strip**: one thumbnail per drawing, numbered, with its hold length shown as a bar to its right (1 to 6 cells wide). Above the strip a readout: "12 drawings, 24 frames, 2.0 seconds at 12 per second".

**Draw.** Tools in the panel: `Pencil`, `Eraser`, size `Fine` / `Medium` / `Bold`, color `Graphite` / `Blue pencil` / `Red` / `Ink`. `Onion skin` toggle (on by default): the drawing before shows in blue at 35% and the one after in green at 35%, under the current page. `Onion: 1` / `2` steps. Buttons: `New page` (blank, inserted after the current one), `Copy page` (a copy inserted after; animators trace and change), `Delete page` (asks first when the page has strokes), `Undo`, `Redo`, `Clear page`. Tap a thumbnail to go to it; drag thumbnails to reorder; arrow keys Left and Right step pages. `Starters` opens the starter books (Content); loading one replaces the book after a confirm when the book has strokes.

**Time.** The page shows the current drawing with no onion skin. The strip grows tall: each drawing's hold bar has a handle; drag it (or `-` and `+` on the selected drawing) to hold that drawing for 1 to 6 frames. Panel: `Frames per second`: `6`, `8`, `12`, `24`. Hold presets: `On ones` (every hold 1), `On twos` (every hold 2), `Ease the ends` (holds of 3, 2, then 1 in the middle, then 2, 3 at each end of the book), `Hold the key` (the selected drawing held 6, others unchanged). `Spacing chart` toggle (on by default): over the page, a dot for where each drawing's center is (the center of its strokes' bounding box), joined in order, numbered, so close dots read "slow here" and far dots "fast here". `Play` / `Stop` and `Loop` live here too, so a change is heard and seen at once.

**Flip.** The page fills the stage; `Play` riffles the book: the page corner lifts with each new drawing (with Motion off, pages swap with no lift and the same timing). `Loop`, `Ping-pong` (plays forward then back), `Step` (one frame), `Back`. A small tick sounds once per new drawing shown, not per held frame, so you can hear the holds (Sound off: silent). `Print pages` makes a black-on-white sheet of all drawings, 8 to a sheet, numbered, with a cutting line and a staple margin, for a real paper flipbook (held drawings print once per frame so the paper book keeps the timing).

## Content
**Starter books** (all drawn in code as strokes, so they can be edited like the student's own; page 960 x 720 units):
1. `Real bounce`: 12 drawings of a ball, radius 40, center x = 80 + 70 i, y = 620 minus 480 times |cos(pi i / 6)| for i = 0 to 11. Drawings 3 and 9 (on the floor) are squashed: 1.3 times as wide, 0.7 times as tall, bottom on the floor line y = 660. Holds all 1, 12 per second. The spacing chart shows dots bunched at the tops and spread near the floor.
2. `Even bounce`: the same ball and the same 12 x positions, but y moves in equal steps (y = 620 minus 480 times the triangle wave |1 minus (i mod 6) / 3|), no squash. Holds 1, 12 per second. The spacing chart shows even dots. Put next to Real bounce, it moves like a machine.
3. `Blink`: a face drawn simply (an oval head, two eyes, a mouth line) in 4 drawings: eyes open, half closed, closed, half closed. Holds 8, 1, 1, 1 at 12 per second (a calm blink about every second). Try holds 2, 1, 1, 1 for a nervous blinker.
4. `Blank book`: 1 empty page.

**On-screen notes** (a `Why` button in Time opens these, one short paragraph each):
- "Film runs at 24 frames per second. Animators often draw on twos: each drawing shown for 2 frames, so 12 drawings make a second."
- "Shooting on ones (a new drawing every frame) looks smoother and is used for fast action; twos are half the drawing and still look smooth for most motion."
- "Slow in and slow out: real things speed up and slow down gradually, so animators bunch drawings near the ends of a move and spread them in the middle."
- "Timing (how many frames) and spacing (how far apart the drawings are) are what make a thing feel heavy or light. The same drawings can feel very different."

**Try this** cards (optional, in the panel under Why; no score, no check): "Make the Real bounce feel like a bowling ball: fewer frames at the top, longer hold on the floor." / "Make the Even bounce feel alive without redrawing: use only the hold handles." / "Make the Blink look surprised." / "Draw a 6-page walk of a dot across the page with even spacing, then fix its spacing so it starts slow and stops slow."

**Limits** (the tool's own choices): up to 48 drawings; up to 6 frames hold per drawing; up to 400 strokes per page.

## Interactions in detail
- Drawing: pointer events with pressure ignored; strokes are smoothed point lists stored as vectors (so thumbnails, print and the spacing chart redraw sharp). Fine 3, Medium 6, Bold 12 units wide. The eraser removes whole strokes it touches (simpler for this age and keeps undo clean).
- Undo and Redo are per page, 50 steps.
- Onion skin draws the neighbors under the page, never into it; it is off in Time and Flip and in Print.
- Hold handle drag snaps to whole frames; keyboard: the selected thumbnail takes `-` and `+`; holds show as a number too ("x3"), never color alone.
- Readout math: frames = sum of holds; seconds = frames / fps, one decimal. Changing fps never changes the holds.
- Spacing chart: a drawing with no strokes gets no dot and breaks the line; a single drawing shows one dot. Dots are numbered so order is clear when a path crosses itself.
- Play timing uses requestAnimationFrame against a clock (not setInterval), so 24 per second does not drift; at 24 the page swaps with no corner lift even with Motion on (too fast to see).
- Starter loaded: hint names the next action ("Tap Time, then drag the hold handles.").
- Save: the book (strokes, holds, fps) saves on this device on every change (localStorage `flipbook-studio-book`, wrapped in try/catch); `New book` clears it after a confirm. If storage is full, a line says "This book is too big to save here. It still works until you close the page."
- Sizes: the page and the strip's selected thumbnail are visible without scrolling at every STANDARDS.md size; below 900 px tall the strip shows one row and scrolls sideways; at 375 wide the panel tools become one row of icon buttons above the strip.

## Look
- Accent (`--brand`) #c8341a vermilion pencil. Desk #3a3f4a (a gray-blue drawing desk), page #fbf6ea cream with a faint paper grain drawn in code, ink #2b2622, muted #6b6258; onion before #2f6fd6, onion after #2e9e5b (shown at 35% as reference; at full strength in the legend); spacing chart dots and line in the accent.
- Contrast: accent on page 4.91:1; white on accent buttons 5.3:1; ink on page 13.88:1; muted on page 5.54:1; page-colored text on the desk 9.79:1; onion legend colors 4.46:1 and 3.16:1 on the page (graphics, above 3:1).
- Light, papery, hand-made. Differs from the group's dark film room (storyboard-studio), clean studio white (brand-builder), festival night (career-cluster-explorer) and camp blue (workplace-scenarios), and from frame-it's amber and design-fixer's indigo.

## Art
none: drawn in code (the desk, page, paper grain, page curl and all starter books are vector shapes).

## Voice
Bank voice: `friendly-dad` (a relaxed parent who animates at the kitchen table; different from every tool in this group and from design-fixer's big-sister). Style: relaxed, a little amused, short.
- welcomeDraw (how): "Draw on the page. Then tap New page or Copy page and change it a little."
- onionHow (how, the first time a second page exists): "The blue ghost is the page before. Draw the next step a little further on."
- welcomeTime (how): "Drag a hold handle under a drawing to keep it on screen longer. Then press Play."
- spacingHow (how, first time the spacing chart is on with 3 or more dots): "Dots close together mean slow. Far apart means fast."
- welcomeFlip (how): "Press Play to flip the book. Try Ping-pong."
- starterBounce (event, after loading Real bounce or Even bounce; stale when the book changes): "Here is a bouncing ball. Press Play, then try the other bounce and compare."
- holdChanged (event, after a hold change while playing; stale at the next change): "Same drawings, new timing. Watch how it feels now."
- printed (event): "Print the pages, cut on the lines and staple the left edge."
- tooBig (event): "This book is too big to save here. It still works until you close the page."

## Family engine
none

## Sources
- NCAS Media Arts MA:Cr2.1, MA:Cr3.1, MA:Pr5.1, grades 6 to 8: https://www.nationalartsstandards.org/
- 24 frames per second; shooting on ones and on twos; timing and spacing charts: Richard Williams, The Animator's Survival Kit (Faber and Faber, 2001), chapters "Timing and Spacing" and "Ones and Twos".
- Slow in and slow out; timing as a principle of animation: Frank Thomas and Ollie Johnston, The Illusion of Life: Disney Animation (Abbeville Press, 1981), chapter 3, "The Principles of Animation".
- Starter books, notes wording and Try this cards: written for this tool.

## Done when
1. Drawing, erasing, undo and redo work by mouse and touch; the eraser removes whole strokes; undo restores them.
2. Onion skin shows the page before in blue and after in green, never prints, and is off in Time and Flip.
3. The readout is right for three cases (recompute): 12 drawings on ones at 12 fps is 1.0 s; on twos is 2.0 s; Blink starter at 12 fps is 11 frames, 0.9 s.
4. Real bounce and Even bounce positions match the formulas in Content (check four drawings each), and the spacing chart shows bunched versus even dots.
5. Hold handles change only timing: strokes are untouched; Play at 24 fps keeps time over 10 loops (within 1 frame).
6. Print pages repeats held drawings once per frame, numbers them, and includes cut and staple marks.
7. The book survives a reload; New book clears it; the full-storage message appears when storage throws.
8. Page, strip and Play are visible without scrolling at every STANDARDS.md size.
9. Each how line is spoken once in five pages drawn in a row; holdChanged is spoken on each change while playing and dropped when stale.

## Open questions
- Keep only Save on this device and Print pages, or also add `Download GIF` (an in-page GIF encoder, about 10 KB of code) so students can keep the animation as a file? It is a download of their own work, not a share code.
