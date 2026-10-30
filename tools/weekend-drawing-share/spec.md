# Weekend Drawing Share

## One idea
The drawing remembers how it was made: Pip asks one question at a time, each answer is drawn as its own step with an art word that says why, and Tell it replays the picture step by step so the child who drew it can tell the story in the order it grew.

## Not like
- line-safari (k-2, showdown): its Draw mode is free play with line brushes. Here every mark answers a question about a real day, carries a reason (an art word), and can be replayed in order.
- art-passport (k-2, explorer): looks at other people's art and asks what you see. Here the art is the class's own, and the questions ask why you made it that way.
- act-it-out (k-2, showdown): tells a story with bodies and voices. Here the story is told by a drawing and the artist explains it.
- hallway-art-museum (k-2, builder, this batch): chooses and shows finished art. Here the art is being made, one question at a time.
- sound-and-picture-book (k-2, studio, this batch): builds a made-up three-page story from given pieces. Here it is one free drawing about something that really happened.
- flipbook-studio, storyboard-studio (6-12, studio): plan frames in time. Here the replay is a record of choices, not an animation.

## Who and how
- Grade K-2, visual arts, module "Art About My Life".
- Driver: teacher on a projector or smartboard. One child (or the teacher, following one child's words) draws on the board while the class draws the same day on paper at their seats. 15 to 25 minutes.
- Standards: NCAS VA:Cr3 (refine and complete work: add details, explain choices), VA:Cn10 (synthesize and relate: make art about your own life and experiences).

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Draw` (crayon icon, default), `Tell it` (speech bubble icon). All targets 60 px or more, icon plus word.

**Draw.** Focus: the paper. A big sheet (4:3, about 70% of the stage width) sits on the art-room backdrop. Pip (painted sparrow cutout) perches on the top right corner of the sheet. A question card sits above the sheet: the question's icon, the question in big type, and a step dot row (7 dots, filled as steps get marks).
- Left tray (vertical): `Crayon` (waxy line with grain), `Marker` (smooth even line), `Paint` (soft wide stroke), `Eraser`; `Thin` and `Thick`; 10 color swatches, each with its word under it: red, orange, yellow, green, blue, purple, pink, brown, black, white.
- Under the sheet: `Stickers` (opens a drawer of 12 painted stickers and 3 people stamps), `Undo`, `Next question` (gold, big), `Questions` (opens the 7 question icons to jump to any one).
- Right of the sheet: the art-word chips, 10 big chips (icon plus word, two columns). Under them, the reason line for this step ("Why? Tap an art word.").
- Shelf strip at the bottom of the panel: `New drawing`, `Save`, and up to 6 saved thumbnails (the first is Pip's sample, "Pip's day at the pond"). Tap a thumbnail to open it.

**Tell it.** Focus: the sheet, the same size and place, replaying the current step's marks over the faded earlier steps. Pip sits beside the sheet in its ask pose. The question card shows the step's question and its chips as big badges. Bar under the sheet: `Back step`, `Play step` (replays this step), `Next step` (gold), `Draw more` (back to Draw at this step). A step strip shows one small thumbnail per step with marks; tap one to jump to it.

## Content
**Questions** (Pip asks them in this order; icon in brackets):
1. where [map pin]: "Where were you? Draw the place."
2. who [two round heads]: "Who was there with you? Draw them."
3. doing [running shoe]: "What were you doing? Show it."
4. sky [sun and cloud]: "What was the sky like? Draw it."
5. sound [ear]: "What could you hear? Draw the sound with lines."
6. feel [heart]: "How did you feel? Add a color that shows it."
7. star [star]: "What is the most important part? Make it stand out."

**Art-word chips** (icon; Pip's line when tapped):
- bright colors [sun]: "Bright colors. They make a picture feel happy and loud."
- dark colors [moon]: "Dark colors. They can show night, or a quiet feeling."
- big [big square]: "You made it big. Big things look important."
- small [small square]: "You made it small. Small things look little, or far away."
- in front [near arrow]: "You put it in front, near the bottom. Things in front look close."
- far back [far arrow]: "You put it far back, up high. It looks far away."
- curvy lines [wave]: "Curvy lines. They feel soft, like wind or water."
- zigzag lines [zigzag]: "Zigzag lines. They feel fast, or loud, or bumpy."
- details [magnifier]: "Lots of little details. Now we can look closer."
- middle [target]: "Right in the middle. That is where our eyes go first."

**Stickers** (painted, crayon style, see Art): sun, cloud, rain cloud, tree, flower, house, slide, ball, dog, cat, cake, kite. **People stamps** (drawn in code as crayon stick figures in the chosen color): `Grown-up` (tall), `Kid` (middle), `Baby` (small). A stamp is a starting shape the child then draws on.

**Pip's sample** ("Pip's day at the pond", the first shelf thumbnail, read only; `Draw more` on it starts a copy). Steps, in logical sheet units (1200 by 900):
1. where: a blue curvy pond (closed curve centered 600, 640, about 700 by 220), the tree sticker at 180, 420 (size 260); chips: curvy lines, in front.
2. who: the dog sticker at 820, 560 (size 170) and a Kid stamp at 430, 560 (size 220, orange); chip: in front.
3. doing: a red ball sticker at 640, 470 (size 90) and three short zigzag motion lines beside it; chip: zigzag lines.
4. sky: the sun sticker at 1020, 140 (size 200) and the cloud at 300, 130 (size 220); chips: bright colors, far back.
5. sound: three curved yellow lines out from the dog's mouth ("woof"); chip: curvy lines.
6. feel: orange and yellow dots around the Kid stamp; chip: bright colors.
7. star: a thick gold outline traced around the ball; chips: big, middle.

## Interactions in detail
- A step is the marks (strokes, stickers, stamps) made while its question is showing, plus up to 2 chips. The step dot fills once it has a mark. Marks can be added to any step: `Questions` jumps to that question, and new marks join it.
- Drawing: pointer down draws at once (no waiting on Pip). Strokes are stored in logical sheet units, smoothed and thinned to points at least 3 units apart, so they replay at any size. Eraser strokes are stored too and replay as erasing. One drawing holds at most 20,000 points; past that, the pen stops and Pip says the sheet is full.
- Stickers: tap a sticker in the drawer and it lands in the middle of the sheet at size 220; drag to move it; a corner handle (60 px) resizes it from 80 to 600; it belongs to the step that was showing when it landed.
- Chips: tap a chip and it lights and Pip says its line (event, every tap). Tapping a third chip replaces the first one. Tap a lit chip to clear it (no line).
- `Undo` removes the last mark of any step (stroke, sticker or stamp), up to the whole drawing; it never removes chips. `Next question` after question 7 shows "All done! Tap Tell it." and the question card shows a check.
- `New drawing` asks with two buttons on the card, `Yes, start new` and `Keep drawing`, when the drawing has marks and is not saved.
- `Save` stores the drawing on this device (localStorage `curio-wds-saves`, in try/catch). Six are kept; saving a seventh asks `Replace the oldest` or `Cancel`. Pip's sample is built in and never counts. If storage fails, the card says "Could not save on this device" and nothing else changes.
- Tell it: opens on the first step that has marks. Each step: earlier steps show at 40% opacity, this step's marks redraw in their real order and speed scaled so the step takes at most 4 s (and at least 600 units a second), then the chips appear one by one as badges and Pip says the question, then each chip line. Then it waits for the child: "Tell us about this part. Then tap Next step."
- Tap while it plays: `Next step`, `Back step` or a strip thumbnail ends the step at once (all its marks shown, its lines dropped) and goes. `Play step` restarts the step. `Draw more` stops everything.
- Tell it with no marks at all: the Tell it button is disabled, and its tooltip and the Draw hint say "Draw something first."
- After the last step: the full drawing at full opacity, and Pip's happy pose; the bar shows `Start over` (step 1) and `Draw more`.
- Motion off: strokes appear whole per stroke at the same pace, Pip does not bob. Keyboard: arrows move a selected sticker 10 units, Delete removes it, Right and Left are Next step and Back step in Tell it.

## Look
- Accent (`--brand`) #b4235a crayon raspberry (header, Next question, lit chips). Paper #fdf8f0, ink #2b2024, muted #6b5a60; sheet white #ffffff with a soft shadow; tray and chip panel on #f4ebe0. Lit chip: brand fill with white text and a check icon (not color alone).
- Contrast (WCAG 2.1, computed): white on brand 6.31:1; brand on paper 5.97:1; ink on paper 14.88:1; muted on paper 6.10:1.
- Scene: a warm art room, honey wood and soft daylight, kept out of the sheet so the child's colors win.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people in any image. Pip in soft colored pencil; stickers in wax crayon so they sit in a child's drawing.
- art-room: "A sunny elementary school art room, a long wooden table with jars of crayons and brushes, paintings pinned on a cork wall, soft window light, soft colored pencil illustration, the center of the frame calm and plain"; 16:9; cutout no; people no; the stage backdrop around the sheet (blurred 4 px behind the sheet).
- paper-texture: "Close-up of plain white drawing paper with a soft fiber texture, full frame, even light"; 4:3; cutout no; people no; the sheet's texture under the drawing at 25% opacity.
- pip-listen, pip-ask, pip-happy, pip-look: "A small round brown and cream sparrow with bright eyes, perched, <pose>, soft colored pencil illustration, plain white background", poses: head tilted to one side listening; beak open with one wing raised like asking; both wings up, cheerful; leaning forward looking down; 1:1 each; cutout yes; people no; Pip on the sheet corner, swapped by state (ask when a question appears, listen while drawing, look in Tell it, happy at the end).
- 12 stickers, each "<item>, a child's wax crayon drawing, bold simple shapes, bright colors, plain white background"; 1:1; cutout yes; people no; drawer buttons and marks on the sheet. Items: a round yellow sun with rays; a white puffy cloud; a grey rain cloud with blue drops; a green tree with a brown trunk; a red flower with a stem; a small house with a door and window; a playground slide; a red ball; a brown dog sitting; an orange cat sitting; a birthday cake with candles; a diamond kite with a tail.

18 images, none with people. Drawn in code: the sheet, strokes, people stamps (crayon stick figures, so no painted person is needed), chips, icons, step dots and thumbnails.

## Voice
Bank voice `curious-librarian` (Aoede), style "Say curiously and warmly, like a friendly school librarian". Pip's voice. Not used by any neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or any other K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode`, `welcomeAfter: true`.

- how, welcome (Draw; stale once a mark is made): "Hi, I'm Pip! Let's draw something that really happened to you. I'll ask one question at a time."
- event, each question in Content: spoken when its question card appears (Next question, Questions, or entering Draw on it); stale when the question changes.
- how, after the first mark of the page load (stale when a chip is tapped): "Why did you draw it that way? Tap an art word."
- how, after the first chip of the page load (stale when the question changes): "When this part is done, tap Next question."
- event, each chip line in Content: every tap that lights a chip; stale on the next chip tap or question change.
- event, after question 7's Next question: "All done! Tap Tell it, and tell us your story."
- how, welcome (Tell it; stale when a step is left): "Now you tell the story. I'll show each part the way you drew it."
- event, in Tell it: the step's question and chip lines (above), every step.
- how, first step wait (stale when the step changes): "Tell us about this part. Then tap Next step."
- event, last step done: "What a story! Thank you for sharing it."
- event: "Saved on this device." / "Could not save on this device." / "The paper is full. Tap Undo, or start a new drawing."
- Read speaks the current question (Draw) or the current step's question and its chip words (Tell it), else the hint.

## Family engine
none

## Sources
- National Core Arts Standards, Visual Arts, grades K to 2 (VA:Cr3, VA:Cn10): https://www.nationalartsstandards.org
- Art words (line, color, size, placement for space, detail, emphasis) follow the elements and principles of art as taught in K-2: Getty Museum, "Understanding Formal Analysis" (https://www.getty.edu/education/teachers/building_lessons/formal_analysis.html). Pip's chip lines are general, gentle descriptions, not rules ("can show", "look").
- Art: original paintings (Art). No facts or numbers on screen beyond these.
- Checks run (Python, 2026-10-29): contrast ratios above with the WCAG 2.1 formula. Save size: 20,000 points at about 11 characters each is 220 KB a drawing, 1.32 MB for six, under the usual 5 MB localStorage quota. Replay pace: at the 4 s cap and 600 units a second floor, a 300 unit step takes 0.5 s, 1,200 takes 2.0 s, 4,000 and 9,000 take 4.0 s; seven steps replay in at most 28 s of drawing, and each step waits for the teacher.

## Done when
1. Focus: at 1366x768 and 680x425 the sheet is the largest thing on the Draw and Tell it stages, and the question card is readable (scene text 10 px or more at 680x425).
2. Pip asks all seven questions in order with Next question, and Questions jumps to any one; marks join the question that was showing.
3. A stroke drawn at 1920x1080 and replayed at 760 wide lands in the same place on the sheet (logical units).
4. Chips: two per step at most, the third replaces the first, every lit chip speaks its line every time.
5. Tell it replays each step in drawing order in 4 s or less, then waits; Pip's sample replays all seven steps with the right chips.
6. Tap while it plays: Next step, Back step or a thumbnail during a replay shows the whole step at once and the old lines stop.
7. Save keeps six drawings across a reload, asks before replacing the oldest, and fails politely with storage blocked.
8. How-to lines are spoken once in a run of five Next question taps; question and chip lines are spoken every time.
9. Every control is 60 px or more with an icon and a word; Next question and the chips are visible without scrolling at every size in STANDARDS.md.
10. Motion off: no Pip bob; strokes appear stroke by stroke at the same pace. No network requests; nothing leaves the device.
