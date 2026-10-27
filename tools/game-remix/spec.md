# Game Remix

## One idea
Open a classmate's working game, press Remix, and change the program itself (swap a sprite, rewrite a rule, add or move a line, borrow a whole sprite from another game) while a "What changed" list and colored tags show every difference from the original, and a credit line that can't be deleted keeps saying whose work you built on.

## Not like
- score-keeper (grade 3, same batch): a space game whose lines never change; its Lab dials only turn numbers to watch variables. Here the lines, events, sprites and backdrop all change, and the subject is the difference between a remix and its original. No space theme: a park, a pumpkin patch and a snowy hill.
- code-tracer (grade 4, same batch): predict each value line by line. Nothing here is predicted or graded; you change a program and compare it with the one you started from.
- robot-dance (K, same batch): find one wrong card by watching the right dance. Here debugging means reading the "What changed" list against a working original, and most remixes are not bugs at all.
- loop-garden (grade 2): repeat blocks on a grid for fewest-block stars. No grid, no repeat block, no star rating.
- design-for-a-friend (grade 5): interviews a persona to design an app feature. No coding there; no users here.
- data-table-builder, biased-bot, network-detective, fruit-sorter-ai, data-defenders: different ideas entirely (data, AI training, networks, security); no shared mechanic.

## Who and how
- Grade 5, computer science. Module: Remix a Program (Algorithms and Programming), "Combine and modify programs; systematic debugging". Format studio.
- Driver: students (pairs on laptops). Also works on a projector: the teacher plays an original, the class votes on one change, the teacher makes it.
- 25 to 40 minutes: Arcade (5 to 10), Remix (20 to 30). Arcade plus one remix works as a 15 minute lesson.
- Standards: CSTA 2026 identifiers from the module: E5-PRO-PD-04, E5-PRO-TR-08, E5-PRO-VD-06. 2017 crosswalk for teachers who still use it: 1B-AP-12 (modify, remix or incorporate parts of an existing program), 1B-AP-14 (observe intellectual property rights and give attribution when remixing), 1B-AP-15 (test and debug), 1B-AP-09 (variables store and modify data).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Arcade", "Remix"], grades_label "Grade 5".
- Start from `kit/starter/src.html`. Header: title "Game Remix", small line "Build on it. Change it. Credit it." Modes (`.seg`): **Arcade**, **Remix**, then kit buttons Motion, Sound, Read (ids `motion`, `sound`, `read`).

## Screens and modes
Three parts, laid out at real pixel size per window (no fixed-design scaling): **Stage** (the game, 4:3, logical world 480 x 360 drawn scaled to its box; sprites 48 logical px), **Program card** (HTML, monospace 15 px or more), **Panel** (kit `aside`, `#hint` first). Wide (1000 px and up): stage left with its run bar under it, program card middle, panel right. Under 900 px tall: run bar and panel buttons first. 760 wide: stage, run bar, panel buttons, program card, rest of panel. 375 wide: same order, program card scrolls on its own. At 680x425 and 800x500: stage and program card side by side, panel collapses to a button row (icons with aria-labels) plus `#hint`; "What changed" opens as a drawer.

**Run bar** (every mode): **▶ Play** (becomes **⏸ Pause**, then **▶ Resume**), **■ Stop** (back to start), **Step** (enabled only while paused), speed seg **Slow-mo** / **Normal** (default Normal), and an on-screen pad **◀ ▲ ▼ ▶** and **Space** (60 px) for touch. Over the stage: variable chips for the variables the program uses (`score`, `time`, `lives`), icon plus name plus value.

### Arcade (opens first; explore)
- **Shelf** across the top of the panel (or a strip above the stage in narrow layouts): 7 cards. Row "Originals": Fetch!, Pumpkin Pop, Snow Bounce. Row "Classmates' remixes": Fetch Turbo, Skunk Trouble, Upside Fetch, Pumpkin Rush. Each card: a thumbnail drawn in code (backdrop plus sprite icons), title, credit ("by Maya", or "by Sam, remix of Fetch! by Maya"), and for remixes a one-line note from the remixer (Content).
- Pick a card: it loads on the stage and in the program card (read only). Play it. Lines highlight as they run.
- **Remix this** (big button, accent): makes a copy and opens Remix mode with it.

### Remix (the studio)
- The program card becomes editable (see Interactions). At its top, locked **credit lines** (lock icon): "Remix of Fetch! by Maya", plus one per borrowed sprite and one per earlier remixer.
- Above the program card: **Title** (text box, default "Remix of Fetch!") and **Remixer** (text box, default a random nickname from Content), with the note "Use a first name or a nickname."
- **Sprite shelf** under the stage: one card per sprite (up to 5) with **Swap** (costume picker of 12), **Remove**, and drag on the stage while stopped to set its start spot (snaps to a 20 px grid). Plus **+ Sprite** (costume picker), **Borrow** (pick an original, then one of its sprites) and **Backdrop** (park, pumpkin patch, snowy hill, plain).
- **Compare** seg in the run bar: **Original** / **My remix** (default My remix). Play runs whichever is chosen; the program card shows that one (Original read only).
- Panel: `#hint`; **What changed** list (Content: change wording), newest change on top, each row clickable (scrolls to and flashes that line); toggle **Show changes** (on); **↶ Undo** (Ctrl+Z); **Start over** (confirm "Go back to the original? Your changes will be gone. Yes / No"); **Challenges** drawer (optional, Content) with a ✓ per challenge met; **Save on this device** (short label Save) and **My saved** (drawer, inline on a phone).
- **My saved remixes**: up to 6 rows (title, date, Open, Delete) and **Clear saved** (confirm). Save is the only thing that stores anything (localStorage `curio-game-remix`, try/catch; the remix is stored in its compact encoded form). Open asks "Open [title]? Your changes to [title] will be gone unless you saved them." when the current remix has unsaved changes.

Sharing was removed after review (Cory): a remix code was too long for a fifth grader to pass along and did not pull its weight. There is no Share mode, remix code on screen, Load a code or printed card.

## Content

### The language (our own; stored as data, run by a tiny interpreter; never eval or new Function)
Program = `{base, backdrop, sprites:[{slot, costume, x, y, dir, speed}], blocks:[{id, hat, args, lines:[{id, op, args}]}]}`. Rendered to text from data. Every block and line has a stable id; original ones keep theirs, new ones get new ids.

Hats (event lines, bold): `when game starts:` / `when [key] key pressed:` (left arrow, right arrow, up arrow, down arrow, space) / `when [sprite] is clicked:` / `when [sprite] touches [sprite]:` / `when [sprite] touches the bottom:` / `every [N] seconds:` (1, 2, 3, 5, 10) / `when [variable] reaches [N]:` (score: 5, 10, 15, 20, 30, 50; time: 0; lives: 0).

Lines (and their choices):
- `move [sprite] [left/right/up/down] [N]` N 10, 20, 30, 40, 60, 80
- `jump [sprite] to [a random spot / its start / the middle]`
- `set [sprite] speed to [N]` 0 to 8 (30 logical px per second per step)
- `turn [sprite] around` / `bounce [sprite] up`
- `set score to [N]` 0, 5, 10 / `change score by [N]` −5, −3, −2, −1, 0, 1, 2, 3, 5, 10
- `set time to [N]` 10, 15, 20, 30, 40, 60, 90 / `change time by [N]` −2, −1, 1, 2, 5
- `set lives to [N]` 1 to 9 / `change lives by [N]` −1, 1
- `[sprite] says [phrase]` Yum!, Got it!, Ouch!, Oops!, Woof!, Pee-yew!, Brrr!, Hooray!, Too slow!, Nice!
- `play sound [pop / boing / chime / bark / splash / buzz / drum]` (synth via Curio.tone)
- `hide [sprite]` / `show [sprite]` / `wait [0.5 / 1 / 2] seconds`
- `end the game: [Time's up! / You win! / Game over / Great job!]`
Sprite names on screen are the costume name; swapping a costume renames it everywhere ("puppy" becomes "cat" in every line).

### Costumes (12)
puppy, cat, bunny, penguin, ball, snowball, pumpkin, carrot, fish, bee, skunk, crow.

### Original 1: Fetch! by Maya (park). Sprites: puppy (240, 300), ball (random), bee (60, 60, moving right, speed 0 until set).
```
when game starts:
  set score to 0
  set time to 30
  jump ball to a random spot
  set bee speed to 3
every 1 seconds:
  change time by -1
when left arrow key pressed:
  move puppy left 30
when right arrow key pressed:
  move puppy right 30
when up arrow key pressed:
  move puppy up 30
when down arrow key pressed:
  move puppy down 30
when puppy touches ball:
  change score by 1
  play sound bark
  jump ball to a random spot
when puppy touches bee:
  change score by -2
  puppy says Ouch!
  jump puppy to its start
when time reaches 0:
  end the game: Time's up!
```

### Original 2: Pumpkin Pop by Leo (pumpkin patch). Sprites: pumpkin (240, 180), skunk (360, 260).
```
when game starts:
  set score to 0
  set time to 20
  jump pumpkin to a random spot
  hide skunk
every 1 seconds:
  change time by -1
every 2 seconds:
  jump pumpkin to a random spot
every 5 seconds:
  show skunk
  jump skunk to a random spot
when pumpkin is clicked:
  change score by 1
  play sound pop
  jump pumpkin to a random spot
when skunk is clicked:
  change score by -3
  skunk says Pee-yew!
  hide skunk
when time reaches 0:
  end the game: Time's up!
```

### Original 3: Snow Bounce by Ana (snowy hill). Sprites: penguin (240, 320), snowball (240, 40, moving down-right).
```
when game starts:
  set score to 0
  set lives to 3
  set snowball speed to 4
when left arrow key pressed:
  move penguin left 40
when right arrow key pressed:
  move penguin right 40
when penguin touches snowball:
  bounce snowball up
  change score by 1
  play sound boing
when snowball touches the bottom:
  change lives by -1
  play sound splash
  jump snowball to its start
when lives reaches 0:
  end the game: Game over
when score reaches 15:
  end the game: You win!
```

### Classmates' remixes (built in, stored as remix codes made from these changes)
1. **Fetch Turbo** by Sam, remix of Fetch!. Note: "I made it super fast!" Changes: all four `move puppy` 30 to 60; ball `change score by 1` to 2; bee speed 3 to 6. Works.
2. **Skunk Trouble** by Priya, remix of Fetch!. Note: "I borrowed the skunk from Pumpkin Pop." Changes: borrow skunk from Pumpkin Pop by Leo (its `every 5 seconds` and `when skunk is clicked` blocks come along); swap bee to crow. Works. Credit lines: "Remix of Fetch! by Maya", "skunk and its code from Pumpkin Pop by Leo".
3. **Upside Fetch** by Kai, remix of Fetch!. Note: "Help! My puppy can't go up." Change: in `when up arrow key pressed`, `move puppy up 30` became `move puppy down 30`. The bug.
4. **Pumpkin Rush** by Jay, remix of Pumpkin Pop. Note: "Faster pumpkins! But my score is stuck." Changes: `every 2 seconds` became `every 1 seconds`; in `when pumpkin is clicked`, `change score by 1` became `change score by 0`. The bug.

### What changed wording (one row each, tag word first, never color alone)
- **changed** "In when puppy touches ball: change score by 1 → 3"
- **new line** "In when puppy touches bee: play sound buzz"
- **removed** "From every 2 seconds: jump pumpkin to a random spot"
- **moved** "jump ball to a random spot moved up one line" / "moved to when game starts"
- **new event** "when space key pressed" / **removed event** "every 5 seconds"
- **swapped** "puppy is now cat" / **backdrop** "park → snowy hill" / **start spot** "ball starts at (120, 80)"
- **new sprite** "carrot" / **borrowed** "skunk and its code from Pumpkin Pop by Leo" / **removed sprite** "bee (and 2 events that used it)"
- With no changes: "No changes yet. It's still the original."

### Challenges (optional; each has a Try it button that loads the right game, and a ✓ when its check is true)
After Try it, the challenge stays in view under the hint ("Challenge: ..."), and turns to "✓ Challenge done: ..." when met. Meeting any challenge other than the two bug fixes shows "Challenge done: [challenge]" and says line 17 (every time a challenge is met).
1. Make the ball worth 3 points in Fetch!. (a `change score by 3` in `when puppy touches ball`)
2. Swap the puppy for a different animal. (slot 1 costume is another animal: cat, bunny, penguin, fish, bee, skunk or crow)
3. Make Pumpkin Pop last 40 seconds. (`set time to 40` in `when game starts`)
4. Make Snow Bounce harder with exactly one change. (exactly one What changed row; the hint asks "Play it. Is it harder?")
5. Add a sound when the bee stings. (a `play sound` line in `when puppy touches bee`)
6. Borrow a sprite from another game. (any borrowed row)
7. Fix Upside Fetch. Use What changed to find the bug. (`move puppy up` and no `move puppy down` in `when up arrow key pressed`)
8. Fix Pumpkin Rush without losing the faster pumpkins. (`change score by` 1 or more in `when pumpkin is clicked`, and `every 1 seconds` still jumps the pumpkin)
9. Add a new rule: an event the original didn't have. (any new event row)

### Nicknames (random default; adjective + animal)
Adjectives: Swift, Clever, Sunny, Brave, Quiet, Lucky, Bouncy, Jolly. Animals: Otter, Fox, Heron, Moose, Gecko, Badger, Lynx, Panda.

### On-screen definitions
- "A **remix** is a new project built from someone else's project."
- "**Credit** means saying whose work you used. Credit lines can't be deleted."
- "A **bug** is a part of a program that doesn't work the way you meant. Comparing with a working original is a fast way to find it."

## Interactions in detail
- **Interpreter.** One game clock. Each event that fires starts its block; a block runs one line per 0.1 s of game time (so its lines visibly take turns). Several blocks may run at once. If a block fires while it is still running, one more run waits (never more). `wait` and `every` use game time. **Slow-mo** runs the whole game clock at one third speed, so lines and motion slow together. Same seed each Play: random spots come from a seeded generator reset on every Play, so the original and a remix get the same luck.
- **Highlight.** A running line gets an accent left bar, pale gold background and ▶; it stays lit at least 250 ms real time, then fades over 600 ms. The hat pulses when its event fires. In Slow-mo and Step the card scrolls to keep the running line in view; in Normal it does not scroll.
- **Pause/Step.** Pause freezes game and lines. Step runs exactly one line (advancing the clock only to the next line, at most 10 s of game time; past that it says "Nothing ran for 10 seconds. Press Resume, then press a key or click a sprite to make something happen."), then pauses again. Space toggles Pause when focus is not on the stage or a text box; S is Step.
- **While a game plays** the hint (and, once, the voice) names its controls from the program's events: key events "Press the key buttons under the stage to play...", click events "Click a sprite on the stage to play.", both, or neither ("Watch each line light up as it runs..."). On Stop or the end banner the hint goes back to what it said before Play.
- **Events.** Keys fire while the stage has focus (click it; a ring and "Keys go to the game" show) or from the on-screen pad; holding repeats every 150 ms. Touch is circle overlap (radius 22), fired once when contact starts, again only after the sprites separate. Hidden sprites don't touch or get clicked. `reaches` fires only when a line changes that variable to that value. Moving sprites bounce off every edge by themselves; `touches the bottom` fires as they hit the bottom edge. `move` clamps inside the stage.
- **End.** `end the game` stops the clock and shows a banner with the message and final values; ■ Stop or ▶ Play starts over. A game with no end runs until Stop.
- **Editing (Remix mode, only while stopped; editing during play stops the game first).** Every choice in a line is a chip: click (or Enter) opens a small menu of exactly the allowed values; arrows move, Enter picks, Escape closes. Each line has a handle with **↑** **↓** (move within its block; at the top or bottom of a block it moves to the end or start of the block above or below) and **✕** (delete). Each block ends with **+ Add a line** (palette grouped Move, Score and time, Look and sound, Game; the new line starts with sensible first choices). Under the last block, **+ Add an event** (palette of hats). Each hat has **✕** (delete block, confirm if it has lines). Keyboard: Alt+Up/Down moves the focused line, Delete removes it.
- **Limits.** 5 sprites, 12 blocks, 8 lines per block, 60 lines total, 40 changes per remix. At a limit the button disables with a one-line reason.
- **Remove sprite** also removes every line and block that names it; confirm says how many. The first sprite can be swapped but not removed.
- **Borrow** adds the sprite (its costume and start spot) and copies every block of that original whose hat and lines name only that sprite or no sprite. It adds a credit line. Borrowing the same sprite twice is refused.
- **Show changes.** New lines and blocks: green bar plus "new" tag. Changed chips: amber underline plus "changed" tag; hover or focus shows "was 1". Moved lines: blue "moved" tag. Removed lines: a struck-through grey ghost where they were, tagged "removed", not run, with a **Put back** button. Diff is by stable ids against the immediate parent (the original, or the classmate's remix you started from).
- **Undo** steps back one change exactly as it was made (a snapshot per change, so two edits of one chip take two Undos; Start over can itself be undone; names typed since are kept). The change log replays from the parent. Changes that cancel out (a line moved down then up, a chip set back) are dropped from the log, so Start over turns off when the list says "No changes yet". Undo stays on: it steps back through each change as made, including the moves that cancelled out.
- **Credit lines** are not chips and have no handle; focusing one shows "Credit lines can't be deleted. Good remixers always say whose work they built on." A remix of a remix keeps the whole chain, newest first, at most 3 remixers deep; past that, Remix this is disabled with "This remix family is full. Start from an original." A remix title that starts "Remix of" is quoted in credit lines, so they never read "Remix of Remix of". The depth limit is kept as a bound on stored data. With no loading it is not reached in normal use (a classmate's remix is one remixer deep and a remix adds one); a saved remix of someone else's remix (only possible in the version that had sharing) opens read only until its first change, and if it is 3 deep it stays read only with the hint "This remix family is full..."
- **Text boxes.** Title max 20 and Remixer max 12 characters, letters, digits, space and ' ! - . only (others are dropped as typed). Rendered as text, never as HTML. Empty Remixer falls back to the random nickname. Names count toward the 240-character stored form: a name that would push it past 240 is cut as typed, with "That title (remixer name) is as long as a saved remix can hold." A change that would push it past 240 is refused with a way out ("That change would make the remix too big to save. Undo a change, or make the title shorter"); default names nobody typed are shortened first. Save refuses anything over 240 before saying anything is saved.
- **Default title.** "Remix of [parent]", else "[parent] Remix" when that is too long; a remix of a title that already says Remix becomes "[Animal]'s [parent title without Remix]" from the nickname ("Panda's Fetch Turbo"), never "Remix of Remix of".
- **Stored form.** Saved remixes and the built-in classmates' remixes are kept as a compact code (never shown). Bytes: version 1, base original (0 to 2), remixer count (1 to 3), then per remixer: title, nickname (6-bit characters from the allowed set), change count, then each change as an op code plus fixed arguments. Crockford base 32, prefix "GR1-", a 2-character checksum, max 240 characters. A stored remix is untrusted input: anything that fails the checksum, version or replay is dropped from My saved remixes.
- **Mode switch** calls `Curio.stop()`, stops the game, keeps the current remix for the page load. Nothing is stored without Save. Remix this (and Try it) asks "Start a new remix?..." whenever the current remix has changes made since it was last saved.
- **Confirm boxes** (delete an event, remove a sprite, start over, start a new remix, open a saved remix, clear saved) show and voice a how line under the question naming both buttons ("Press Delete to remove the event, or Keep it to leave it.").
- **Compact layout** keeps short text labels on the buttons the hints name (Undo, What changed, Sprites, Save, My saved); Start over, Show changes, Challenges and Clear saved stay icon only with their names as labels. In compact Arcade a **What changed** button opens the classmate's changes for remix cards, and bug cards keep a "Has a bug" tag. In wide Arcade the hint and Remix this stay pinned at the top of the panel while the shelf scrolls under them. On a landscape phone (compact under 440 px tall) the pad keeps 44 px buttons in one row under the stage. On a phone (stack) the stage shrinks so the pad and the hint (and in the Arcade, Remix this) stay on the first screen, and Remix this moves focus to the first chip without scrolling.
- **Motion off** (body.calm): sprites jump between positions every 0.25 s instead of gliding; highlights change without fades; no banner sparkle. Timing and sounds stay the same.
- Targets 44 px or more (pad 60 px), visible focus on stage and paper. Tab order: mode buttons, header buttons, run bar, pad, panel buttons, What changed, sprite shelf, program card. Expose `window.__tool = {state, load(id), run(ms), save(), readSaved(), openSaved(i), ...}` (run plays headless for ms of game time with no input and returns the variable values) for verify.

## Look
- Band 3-5, own `:root`: `--paper #f3f8f7`, `--panel #ffffff`, `--ink #16282b`, `--muted #4f6468`, `--line #cfe0de`, `--brand #0b6b6f` (deep teal, the accent; header background and Remix this), `--btn #0b6b6f`, `--head-ink #ffffff`, `--focus #c2410c` (orange ring). Running line `#fff1c2`. Tags: new `#1d7a3a` on `#e3f4e8`, changed `#9a5b00` on `#fff0d6`, moved `#2a5db0`, removed `#8a3b3b`. Code box (Share) `#e8fbf7` on `#10242a`.
- Program card looks like a sticky index card in a maker space: white, teal header strip with the title, credit lines in muted italic with the lock.
- Neighbor check: robot-dance magenta `#b0206a`, score-keeper raspberry `#a82755`, code-tracer pencil orange `#a8461a`, computer-builder cobalt `#2049b8`, loop-garden lawn green. No trace table, no robot or dance theme. Deep teal is unlike all of them.
- Contrast (computed, WCAG): white on brand 6.27:1; brand on paper 5.85:1; ink on paper 14.27:1; muted on paper 5.84:1; muted on white 6.26:1; ink on running line 13.56:1; focus on paper 4.83:1 (non-text, needs 3:1); tag text on white: new 5.39, changed 5.43, moved 6.38, removed 7.58; new on its tint 4.71, changed on its tint 4.83; ink on tints 13.39 and 13.62; code text 14.97:1. All pass AA.

## Art
- park: "a sunny city park seen from above at a gentle angle, soft green lawn, a curving path, two round trees at the edges, a small pond corner, flat vector illustration, open lawn in the middle" (`scripts/cfart.py`); 4:3; cutout no; people no. Backdrop for Fetch!.
- pumpkin-patch: "an autumn pumpkin patch field seen from above at a gentle angle, rows of dark soil and green vines, a wooden fence along the top, flat vector illustration, open space in the middle" (`scripts/cfart.py`); 4:3; cutout no; people no. Backdrop for Pumpkin Pop.
- snowy-hill: "a quiet snowy hillside under a pale blue winter sky, soft drifts, two small pine trees at the edges, flat vector illustration, smooth open snow across the middle and bottom" (`scripts/cfart.py`); 4:3; cutout no; people no. Backdrop for Snow Bounce.
- puppy (base): "a cheerful cartoon puppy standing, seen from the front, tan and white fur, floppy ears, flat vector sticker style, thick dark outline, solid white background" (`scripts/gptart.py`); 1:1; cutout yes; people no. Sprite.
- cat, bunny, penguin, pumpkin, carrot, fish, bee, skunk, crow: same prompt shape ("a cheerful cartoon [thing] ..., flat vector sticker style, thick dark outline, solid white background"), siblings of puppy with `"ref"` and `"ref_mode": "style"`; 1:1; cutout yes; people no. Sprites. Bee, skunk and crow friendly, not scary.
- Drawn in code: ball and snowball (circles with shading), plain backdrop, shelf thumbnails, chips, tags, banners, pad, stage ring, preview.svg (the park backdrop drawn as flat shapes, the puppy chasing a ball, and a program card corner showing a green "new" line).
- If an image is missing, draw the sprite as a colored circle with its name so the tool still works. No spaceship, space rock or night sky (score-keeper), no robots or computer parts (robot-dance, computer-builder).

## Voice
`voice/lines.json`: `"bank": "big-sister"`, `"voice": "Leda"`, style "Say in a friendly, youthful way, like a helpful older student". A fifth grader is learning remix manners from an older kid in the maker club, which fits. Differs from the batch (lively-host, bright-teacher, friendly-dad, clear-teacher) and loop-garden (hero-coach); the only other big-sister tool is conflict-coach (SEL), not a neighbor. On-screen text is the main channel; these are all the fixed lines. Teaching lines and how-to lines play once per page load ("But don't nag"); event lines (9 fixed, 11 saved, 14 challenge done, 15 step found nothing) play every time their event happens. Read is always on demand. Read speaks `#hint`.
1. arcade-welcome: "Welcome to the arcade. These games were made by kids. Pick one, press Play, and watch its code light up as it runs."
2. remix-button: "Like it? Press Remix this. You get your own copy to change, and the maker still gets the credit."
3. remix-welcome: "This is your copy now. Click any word in a box to change it, or add a line. The original stays safe."
4. first-change: "See the tag? What changed keeps a list of every difference from the original."
5. credit: "That top line is the credit. It can't be deleted. Good remixers always say whose work they built on."
6. compare: "Switch to Original and play it again. Same luck, same start. Is your remix different the way you wanted?"
7. borrow: "You borrowed a sprite and its code. That's combining programs. The credit line for it was added for you."
8. bug-remix: "This remix has a bug. Check What changed. The bug is hiding in one of those changes."
9. fixed: "You fixed it! Comparing with a working original is a great way to hunt bugs."
10. undo: "Undo goes back one change at a time, so it's safe to try wild ideas."
11. saved: "Saved on this device."
12. game-end: "Game over. Want to change a rule and try again?"
13. original-view: "This is the original, just as it was. Same luck, same start. Is your remix different the way you wanted?"
14. challenge-done: "Challenge done! It has a check mark in Challenges now."
15. step-idle: "Nothing ran for 10 seconds. Press Resume, then press a key or click a sprite to make something happen."
Which line when: Arcade entry 1; first Play end in Arcade 2; Remix entry 3 (only for a copy the child can change); first change 4 then (first time only) 5; after the first run (Stop or end banner) of a remix with changes, in My remix, 6 (its hint stays until the moment changes); first Original toggle 13; first Borrow 7; opening Upside Fetch or Pumpkin Rush 8; each bug fix 9 (every time a bug game goes from broken to fixed); any other challenge met 14; first Undo 10; Save 11; Step that finds nothing 15; first end banner in Remix 12 (unless 6 plays then).
A queued line plays only if its moment is still here when its turn comes (same mode; 6 only in My remix and not playing; 13 only in Original; 2 only in Arcade; 12 only stopped or ended; 4, 5 and 8 only before the fix); a how line only while the hint still shows it, and a newer how line drops older queued ones. When a change is the fix, 9 plays first and 4, 5 and the changed how line are skipped. The first-tap welcome is skipped when that tap queued or already started a line of its own.

**How-to lines** (Cory's rule: every waiting moment names the next action and its control, in the voice and in the hint; `HOW` in src.html, voiced once, kept in the hint until the moment changes):
- after the first change: "Press Play to try your change, or tap a row in What changed to find that line in the program."
- Original view: "Press Play to watch the original, then press My remix to switch back."
- borrow: "Press Play to watch the borrowed code run."
- Upside Fetch in the Arcade: "To fix it, press Remix this. Then, in What changed, tap the row under Changes Kai made to find the line. Tap the wrong word and pick the right one." In Remix: "In What changed, tap the row under Changes Kai made to find the line. Then tap the wrong word and pick the right one."
- Pumpkin Rush in the Arcade: "To fix it, press Remix this. Then, in What changed, tap Jay's score change to find the line in when pumpkin is clicked. Tap the number and pick a bigger one." In Remix: "In What changed, tap Jay's score change to find the line in when pumpkin is clicked. Then tap the number and pick a bigger one."
- fixed: "Press Play to test your fix." undo: "Press Undo again to go back one more change."
- saved: "To open it later, find it in My saved remixes and press Open." game end: "Change a word in the program, then press Play."
- playing (see Interactions): playKeys, playClick, playBoth, playWatch. Paused: the paused hint, voiced once.
- confirm boxes: "Press Delete to remove the event, or Keep it to leave it." / "Press Remove to take the sprite out, or Keep it to leave it in." / "Press Yes to go back to the original, or No to keep your changes." / "Press Start new to begin a new remix, or Keep mine to go back to your changes." / "Press Open to switch to the saved remix, or Keep mine to go back to your changes." / "Press Clear to remove them all, or Keep them to leave them saved."
voice/lines.json holds every line `allLines()` returns (the spec lines, the how lines and the hints): 42.

## Family engine
none. Keep the interpreter in one marked block `/* REMIX ENGINE: begin */ ... /* end */` with no DOM access (program data in, a step function that yields `{blockId, lineId, effects}`), and the code encoder and diff as pure functions beside it, so a later family could lift them.

## Sources
- CSTA K-12 CS Standards (2017), 1B-AP-09, 1B-AP-12, 1B-AP-14, 1B-AP-15: https://csteachers.org/k12standards/
- Module ids E5-PRO-PD-04, E5-PRO-TR-08, E5-PRO-VD-06: CSTA PK-12 Standards (2026), from `data/standards/csta-2026-ids.txt` and `data/modules.csv`.
- Remix as a new project built from another's, and giving credit: Scratch Wiki, "Remix": https://en.scratch-wiki.info/wiki/Remix ; Scratch Community Guidelines ("give credit when you remix"): https://scratch.mit.edu/community_guidelines
- Attribution as the basic condition of reuse: Creative Commons, "About CC Licenses" (BY): https://creativecommons.org/share-your-work/cclicenses/
- Bug and debugging definitions: Code.org CS Fundamentals glossary: https://code.org/curriculum/docs/k-5/glossary
- Crockford base 32 alphabet: https://www.crockford.com/base32.html
- Games, makers, remixes and nicknames are original to Curio Class (fictional kids).

## Done when
1. Arcade: each of the 7 cards loads, plays, and highlights each line as it runs; Slow-mo slows lines and motion together; Pause then Step runs exactly one line per press.
2. Fetch! played with no input for 31 s of game time (`__tool.run`) ends with "Time's up!", time 0; Snow Bounce with no input loses a life each time the snowball reaches the bottom and ends "Game over" at lives 0.
3. Remix: change a chip, add, move and delete a line, add and delete an event, swap a costume (renamed in every line), set a start spot, change backdrop: each appears in What changed with the right tag word, and Show changes marks it in the card; Put back restores a removed line; Undo reverses each step.
4. Credit line cannot be selected for edit, moved or deleted by mouse or keyboard; Borrow adds the sprite, its blocks and a second credit line; Skunk Trouble shows both credits.
5. Upside Fetch and Pumpkin Rush: What changed shows exactly the changes in Content; fixing the bug meets challenge 7 or 8 and plays line 9.
6. Compare Original / My remix with the same seed: the ball's first random spot is the same in both.
7. The stored form round-trips every built-in remix and a remix of a remix exactly (same program, same credits, same What changed); nothing stored is over 240 characters.
8. Save, reload, Open restores the remix with its credits and changes; Delete removes one; Clear saved empties the list.
9. Every size in STANDARDS.md: Play/Pause, Step and the pad visible without scrolling; program card text 15 px at 1366x768; 375 wide works in `drive.py --host`; keyboard only can play, edit and save; held clicks log the right voice clips, none twice.
10. Search the file: no `eval`, no `new Function`, no network requests, typed text set only as text; "Curio" appears only as "Curio Class" in visible text; console clean through a full session.
