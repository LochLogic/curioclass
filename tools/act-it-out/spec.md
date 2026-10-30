# Act It Out
Renamed from: Story Dress-Up

## One idea
The class is the cast: the board tells a folktale, hands each half of the room a costume piece from a dress-up trunk, and waits while the Sun side and the Moon side become the goat and the troll with their bodies, faces and voices, then swaps the parts and plays it again.

## Not like
- story-stage (ELA K, sandbox): the teacher drags characters onto a stage to retell a tale. Here nothing on the board acts for the class: the two puppets only wear the costume, and the children are the actors.
- my-story-strip (ELA K, studio): draws and labels panels. Here there is no drawing or writing; it is all body, face and voice.
- beat-buddies (k-2, showdown): copies animal moves to a beat and freezes when the music stops. Here there is no beat and no right move: the class invents how the troll walks and talks.
- levels-and-pathways (k-2, showdown, dance group): copies a dancer's levels and pathways. Here the class plays characters inside a story with lines to say.
- line-safari, art-passport, orchestra-zoo, sound-elevator (k-2 arts): looking, listening and drawing tools; none asks children to pretend to be someone.
- two-sides-theater (ELA 2, roleplay): retells one tale from two points of view. Here the two sides of the room play opposite characters at the same time, then trade.
- Title: "Story Dress-Up" sat beside story-stage and my-story-strip; renamed "Act It Out" and the topic line carries the topic.

## Who and how
- Grade K-2, theater, module "Pretend and Play (Theater)": creative drama and storytelling with movement.
- Topic line: pretend play and acting out a story
- Driver: teacher on a projector or smartboard; the class acts at their seats or in a cleared space. 15 to 25 minutes.
- Standards: NCAS TH:Cr1 (generate and conceptualize ideas: invent and inhabit an imaginary place, imagine costumes and props), TH:Pr4 (select, analyze and interpret work: use body, face and voice for a character); also TH:Cr2 (the class shapes the story at Choose beats), TH:Pr5 (voice, sound, costumes and sound effects), TH:Pr6 (each side performs for the other).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Stories` (book icon, default), `Trunk` (trunk icon). Every control is at least 60 px with an icon and a word.

**Stories (home).** Three big story tiles on a plum curtain, each with its backdrop thumbnail and the costume piece that marks it: `Billy Goats` (little horns), `Gingerbread Boy` (icing buttons), `Big Turnip` (straw hat). Tap one to start it.

**Stories focus:** the three story tiles, large, centered on the little-stage backdrop.

**Story player.** Focus: the acting side's puppet in its spotlight, wearing its costume; the puppets stand in the middle of the stage at about half the stage height, the beat card above them and the bar below. The stage fills about 75% of the screen: the story's backdrop, and two painted peg puppets standing on it, the Sun puppet (art: puppet-sun) on the left under a sun badge "Sun side", the Moon puppet (art: puppet-moon) on the right under a moon badge "Moon side". Each puppet wears that side's current costume (painted piece cutouts placed on the puppet's anchor points). Each puppet's face (two dot eyes and a mouth) is drawn in code on its blank wooden head: a smile while acting, an O mouth on Freeze, a calm smile otherwise. Below the stage, the teacher bar (60 px buttons, icon plus word): `Back`, `Next` (big, gold, right), `Swap` (two arrows), `Freeze` (snowflake), `Sound effect` (speaker; shows the beat's sound name, disabled when the beat has none), `Home` (house).
- A beat card above the bar shows the beat's line in big type and, for act beats, who acts: "Sun side", "Moon side" or "Everyone" with the badge icons.
- The acting side's puppet stands in a warm spotlight and sways gently; the other puppet dims to 60%. For "Everyone", both are lit.
- Dress beats: the trunk (art: trunk-closed, swapped for trunk-open) opens at the bottom center, the piece flies to the puppet (500 ms; with Motion off it appears), and the narrator asks the class to put it on (mime).
- Choose beats: two big choice buttons on the stage, each with an icon and a word. The choice sets the next act line.
- Freeze beats: a gold picture frame draws around the stage and the word "Freeze!" appears; Next plays a soft camera click and goes on.
- End beat: "The end" on the curtain, with `Swap and play again` (both sides trade parts and the story restarts at beat 1) and `Home`.

**Trunk (explore).** Focus: one big puppet (puppet-sun) in the center of the stage, about two thirds of the stage height, wearing the outfit. The stage shows the puppet on a chosen backdrop. Under it, the open trunk: a scrolling tray of costume piece buttons (picture plus word), grouped by where they go (head, face, body, feet, tail). Tap a piece: it jumps onto the puppet; one piece per place, so a new hat replaces the old one; tap a worn piece again to take it off.
- Panel strip: `Backdrop` (cycles the six backdrops in Art, starting with little-stage), `Surprise me` (dice: a random outfit of 3 or 4 pieces), `Take it all off`, `Ask` (question mark: speaks the next character question), `Freeze`, and a row of eight sound buttons (icon plus word) that play their effect.

## Content
**Costume pieces** (painted cutouts, see Art; place in brackets): little horns [head], big curly horns [head], straw hat [head], crown [head], wizard hat [head], fox ears [head], dog ears [head], mouse ears [head], cow horns and bell [head and neck as one piece], hair bow [head], pig snout [face], cat whiskers [face], big troll nose [face], icing buttons [body], candy bow tie [body], apron [body], shawl [body], shaggy cape [body], big boots [feet], bushy tail [tail]. 20 pieces.

**Sounds** (Web Audio, synthesized, under 1.5 s, gentle; none scary): `Trip trap` (two light wood clicks, 900 and 1100 Hz, 120 ms apart), `TRIP TRAP` (the same an octave lower, louder, slower), `Splash` (white noise through a falling low-pass, 2000 to 300 Hz), `Oven ding` (sine bell 1320 Hz, slow decay), `Running feet` (eight quick soft clicks), `Snap` (one sharp click plus a low thump), `Heave-ho` (rising filtered noise whoosh), `Pop` (pitch drop 600 to 150 Hz plus a thump). The trunk plays a three-note sparkle (C6 E6 G6) when it opens.

**Stories.** Original retellings of public-domain folktales (Sources). `type [side] (backdrop) sound`: line. Act and dress lines name the side.

*Billy Goats* (Sun side = goats, Moon side = troll; after Swap, the reverse):
1. tell (meadow-bridge): "Once upon a time, three billy goats lived near a hill of sweet green grass. To get there, they had to cross a bridge."
2. tell: "But under the bridge lived a grumpy troll."
3. dress [Moon] shaggy cape, big boots, big troll nose: "Moon side, you are the troll! Put on your shaggy cape and your big, heavy boots."
4. dress [Sun] little horns: "Sun side, you are the goats! Put on your horns."
5. act [Sun] Trip trap: "The littlest goat goes first. Trip, trap, trip, trap. Sun side, tiptoe, quiet and small."
6. choose: "How does the troll talk? Tap Big and booming, or Squeaky and small." Buttons: `Big and booming` (big sound waves), `Squeaky and small` (tiny waves).
7. act [Moon]: booming: "Moon side, say it big and booming: Who is that tripping over my bridge?" or squeaky: "Moon side, say it squeaky and small: Who is that tripping over my bridge?"
8. act [Sun]: "Sun side, be a brave little goat. Say: Wait for my big brother. He is much bigger than me!"
9. act [Sun] TRIP TRAP, piece big curly horns: "Here comes the biggest goat. TRIP, TRAP! Sun side, stomp, big and slow."
10. freeze [Everyone]: "The troll jumps up. The big goat lowers his horns. Everyone, freeze like a statue!"
11. tell Splash: "Bump! The big goat bumps the troll right off the bridge. Splash! Into the river he goes."
12. act [Everyone]: "Now everyone, be the goats munching sweet grass on the hill. Munch, munch. Show me your happy face."
13. end: "The end! Tap Swap and play again, and the Sun side and Moon side trade parts."

*Gingerbread Boy* (Sun side = the Gingerbread Boy, Moon side = everyone who chases him):
1. tell (kitchen) Oven ding: "One morning, a little old woman baked a gingerbread boy. Ding! She opened the oven door."
2. dress [Sun] icing buttons, candy bow tie: "Sun side, you are the Gingerbread Boy! Put on your icing buttons and your candy bow tie."
3. act [Sun] Running feet: "Out he jumped, and away he ran! Sun side, run in your seats and say: Run, run, as fast as you can! You can't catch me, I'm the Gingerbread Boy!"
4. dress [Moon] apron: "Moon side, you are the little old woman and the little old man. Put on your aprons. Wave your arms and call: Stop! Stop!"
5. dress [Moon] cow horns and bell (road): "Now Moon side, you are a cow in the field. Put on your bell. Say: Moo! Stop, little cookie!"
6. choose (road): "How does the Gingerbread Boy run past the pig? Tap Super fast, or Slow and silly." Buttons: `Super fast` (speed lines), `Slow and silly` (snail).
7. act [Both] pig snout on Moon: super fast: "Moon side, you are the pig. Oink! Sun side, run past the pig super fast!" or slow: "Moon side, you are the pig. Oink! Sun side, run past the pig in slow motion, slow and silly!"
8. tell (river): "Then the Gingerbread Boy came to a wide river. He could not swim! A sly fox sat on the bank."
9. dress [Moon] fox ears, bushy tail: "Moon side, you are the fox. Put on your pointy ears and your bushy tail. Say it sweet and sly: Hop on my tail. I will carry you across."
10. act [Sun]: "Sun side, hop onto the fox's tail. Now onto his back. Now onto his nose!"
11. freeze [Everyone]: "Everyone, freeze! The Gingerbread Boy is on the fox's nose. Show me with your face: worried, or happy?"
12. tell Snap: "Snap! The clever fox gobbled him up. And that was the end of the Gingerbread Boy." (see Open questions)
13. end: "The end! Tap Swap and play again, and the Sun side and Moon side trade parts."

*Big Turnip* (the sides take turns joining the pulling line; the turnip is painted (art: turnip-sprout, turnip-giant) and grows):
1. tell (garden): "Grandpa planted a tiny turnip seed. He said: Grow, little turnip. Grow big and sweet!"
2. act [Everyone]: "Everyone, be the seed. Curl up small. Now grow, grow, grow, and stretch up tall!" (the sprout cutout grows and cross-fades into the giant turnip, its lower half hidden behind a soil band drawn in code, over 4 s; with Motion off, in three steps)
3. dress [Sun] straw hat, Heave-ho: "Sun side, you are Grandpa. Put on your straw hat. Grab the leaves and pull! Heave-ho! It would not come up."
4. dress [Moon] shawl, Heave-ho: "Moon side, you are Grandma. Put on your shawl. Hold on to Grandpa and pull! Heave-ho! It would not come up."
5. dress [Sun] hair bow, Heave-ho: "Sun side, you are the granddaughter. Put on your bow. Pull! Heave-ho! Still stuck."
6. dress [Moon] dog ears, Heave-ho: "Moon side, you are the dog. Woof! Pull! Heave-ho! Still stuck."
7. dress [Sun] cat whiskers, Heave-ho: "Sun side, you are the cat. Meow! Pull! Heave-ho! Still stuck."
8. choose: "Who should help next? Tap the Tiny mouse, or the Big bear." Buttons: `Tiny mouse`, `Big bear`. Bear: "A big bear came to help. Everyone, be the bear. Pull! Heave-ho! Even the bear could not do it. Maybe someone tiny can help." then beat 9. Mouse: beat 9 at once.
9. dress [Everyone] mouse ears: "Everyone, you are the tiny mouse. Put on your little ears. Squeak! Now everyone pull together. One, two, three, heave-ho!"
10. freeze [Everyone] Pop: "Pop! Out came the turnip, and everyone tumbled down in a heap! Freeze in your funny heap!"
11. end: "And they all ate turnip soup. The end! Tap Swap and play again, and the Sun side and Moon side trade parts."

**Character questions** (Trunk `Ask`, in order, then repeat): "How does this character walk? Show me." / "What does this character sound like? Say hello." / "How does this character feel today? Show me with your face." / "Where does this character live? Tell a friend." / "What does this character want more than anything? Tell a friend."

## Interactions in detail
- Next advances one beat; Back goes back one beat, restores that beat's costumes and stops speech. Next and Back are never locked (the one exception is Next on a choose beat, below): the teacher keeps the pace. A tap on any control while a line is spoken or something moves (a piece flying, a swap slide, the turnip growing) acts at once: the line stops, the motion jumps to its end state, and the new beat or action starts. Each beat's line is spoken when the beat opens (Voice). There is no timer and no score.
- Costumes are state per beat: going back removes pieces given later. A piece for a place the puppet already wears replaces the old one (big curly horns over little horns, fox ears over cow horns, hair bow over straw hat). Swap mid-story trades the two puppets' outfits (a 400 ms slide across; with Motion off, a jump), flips the side roles for every later beat, and speaks the Swap line.
- Freeze button (any time, both modes): draws the frame, speaks "Freeze!"; the button becomes `Unfreeze` (melting snowflake); tapping it speaks "Unfreeze!" and clears the frame. Next while frozen also unfreezes.
- Sound effect button replays the beat's sound; the class may also make the sound themselves.
- Choose beats: Next is disabled until a choice is tapped (the hint and Read say so); the choice button stays outlined, and Back to the choice beat lets the teacher pick again.
- Trunk: Surprise me never gives two pieces for the same place. Take it all off empties the puppet with a little hop. The trunk keeps its outfit and backdrop when switching modes (in memory only; nothing is saved).
- Home stops speech and returns to the story tiles; a story restarts at beat 1 with Sun as the first role list.
- Keyboard: Right arrow = Next, Left arrow = Back, F = Freeze, S = Swap, Space on a focused button presses it.

## Look
- Accent (`--brand`) #7d2e7f trunk plum (header, Next border, selected choice). Paper #fbf4ea, ink #2a1f2b, muted #6a5a68; curtain #5a1f5c with darker folds; trunk wood #8a5a34 with brass corners #d2a54a; Sun badge #f2b632 with ink text and a sun icon; Moon badge #2c3e7a with white text and a moon icon (never color alone: icon plus word on every badge).
- Contrast: white on brand 8.2:1; brand on paper 7.5:1; ink on paper 14.5:1; muted on paper 5.9:1; ink on Sun gold 8.7:1; white on Moon navy 10.1:1; white on curtain 11.8:1.
- Puppets and costume pieces are painted (Art) in one gouache style: honey and walnut wood puppets, bright costume colors, a soft dark outline. Faces drawn in code in #3a2a1c. Each backdrop's palette is warm storybook greens, creams and blues, kept clear of the plum accent.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8.

## Art
Local FLUX (`scripts/localart.py`); one soft gouache storybook style for every image, asked in one session. No image has a person: the puppets are wooden toys with blank heads, and their faces are drawn in code.

Backdrops: full-frame painted storybook scenes, the lower third kept simple and open (the puppets stand there), blank surfaces only.
- meadow-bridge: "A small wooden footbridge over a clear stream between two grassy banks, a green hill with long grass beyond, morning light, soft gouache storybook painting"; 16:10; cutout no; people no; Billy Goats backdrop and a Trunk backdrop.
- cottage-kitchen: "A cozy cottage kitchen with a big black iron oven, a wooden table with a rolling pin, a window with gingham curtains, warm light, soft gouache storybook painting"; 16:10; cutout no; people no; Gingerbread beats 1 to 4.
- country-road: "A dirt country road between a fenced green field and a muddy pen, rolling hills behind, soft gouache storybook painting"; 16:10; cutout no; people no; Gingerbread beats 5 to 7.
- wide-river: "A wide blue river with reeds and a grassy bank in front, far trees across the water, soft gouache storybook painting"; 16:10; cutout no; people no; Gingerbread beats 8 to 13.
- veggie-garden: "A cottage vegetable garden with neat rows of leafy plants, a wooden fence and a watering can, a wide patch of bare brown soil in the center, soft gouache storybook painting"; 16:10; cutout no; people no; Big Turnip backdrop (the turnip grows in the bare patch).
- little-stage: "An empty small wooden theater stage with plum velvet curtains drawn open and warm footlights, soft gouache storybook painting"; 16:10; cutout no; people no; Trunk default backdrop and behind the story tiles.

Puppets, trunk and turnip (cutouts, front view, plain white background):
- puppet-sun: "A wooden peg doll toy standing, front view, a round smooth blank wooden head, a rounded honey-colored wooden body, small peg feet, a tiny painted yellow sun on its chest, soft gouache storybook painting, plain white background"; 3:4; cutout yes; people no; Sun side and the Trunk puppet; sways in code; face drawn in code.
- puppet-moon: the same peg doll in darker walnut wood with a tiny painted blue moon on its chest; 3:4; cutout yes; people no; Moon side.
- trunk-closed: "A wooden dress-up trunk with brass corners and a curved lid, closed, soft gouache storybook painting, plain white background"; 4:3; cutout yes; people no; bottom center on dress beats and above the Trunk tray.
- trunk-open: the same trunk with its lid open and colorful cloth spilling over the edge; 4:3; cutout yes; people no; swapped in when the trunk opens.
- turnip-sprout: "A tiny green turnip sprout with two round leaves, soft gouache storybook painting, plain white background"; 1:1; cutout yes; people no; Big Turnip beat 2 start.
- turnip-giant: "A giant round white and purple turnip with a big bunch of leafy green tops and a curly root, soft gouache storybook painting, plain white background"; 1:1; cutout yes; people no; grows in the garden and pops out on beat 10.

Costume pieces: 20 cutouts, each "<item>, a child's dress-up costume piece, front view, bright colors, soft gouache storybook painting, plain white background"; 1:1; cutout yes; people no; worn by the puppets and shown on the Trunk tray buttons. Each is painted alone and the builder scales it to its place: head pieces to the head width, face pieces to the face, body pieces to the body, boots to both feet, the tail behind the body on the right. Items: little goat horns on a headband; big curly ram horns on a headband; a straw hat; a gold paper crown; a starry blue wizard hat; pointy orange fox ears on a headband; floppy brown dog ears on a headband; round grey mouse ears on a headband; cow horns on a headband with a brass cow bell on a ribbon; a big red hair bow; a pink pig snout on elastic; white cat whiskers on a small pink nose; a big lumpy green troll nose; three round white icing buttons; a red and white striped candy bow tie; a blue checked apron; a flowered shawl; a shaggy brown cape; a pair of big black boots; a bushy orange fox tail.

32 images in all, none with people. Drawn in code: the puppets' faces, the spotlight, the gold freeze frame, the soil band, badges, beat cards, buttons, icons and preview.svg (controls, labels and shapes that must fit the stage size).

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), style "Say gently and expressively, like a grandmother reading a picture book aloud". Not used by any k-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, calm-corner warm-teacher). `Curio.voice` with `scope: () => state.mode + ':' + state.story`. Every fixed line is recorded.

- how, welcome (Stories; stale when a story or Trunk is tapped): "Welcome to Act It Out! Teacher, tap a story to begin. Or tap Trunk to play dress-up."
- how, first tell beat of the page load, after its story line (stale when Next is tapped): "Tap Next when you are ready for more of the story."
- event, story start: "The Three Billy Goats Gruff." / "The Gingerbread Boy." / "The Great Big Turnip." (stale when beat 1 is left, or on Home)
- event, every story beat line in Content (both variants of beats with choices, and the bear line): spoken each time the beat opens, stale when the beat changes.
- how, first act or dress beat, after its beat line (stale when the beat changes): "When everyone has had a turn, tap Next."
- how, first choose beat, after its beat line (stale when a choice is tapped; it never names Next, which is disabled until then): "Let the class choose. Then tap their choice."
- how, first end beat (stale when Swap and play again or Home is tapped): "Tap Swap and play again to trade parts."
- event, Swap / Freeze / Unfreeze tapped (stale on the next of these taps or a beat change): "Swap! Sun side and Moon side, trade parts." / "Freeze! Everyone be a statue." / "Unfreeze!"
- how, welcome (Trunk; stale when a piece is tapped): "This is the dress-up trunk. Tap a costume piece to dress the puppet."
- how, after the second piece (stale when Ask is tapped): "Tap Ask, and the class can answer my question."
- event: each character question in Content (spoken every time Ask is tapped; stale on the next tap).
- event, Surprise me (stale on the next Trunk tap): "Ta-da! Who could this be?"
- event, Take it all off (stale on the next Trunk tap): "All clean. Let's dress up someone new."
- Read speaks the current beat line (or the hint).

## Family engine
none

## Sources
- Billy Goats: "The Three Billy-Goats Gruff", in George Webbe Dasent, Popular Tales from the Norse (Edinburgh, 1859), from Asbjornsen and Moe; public domain. Retold here in original words, softened (no injury).
- Gingerbread Boy: "The Gingerbread Boy", St. Nicholas Magazine, vol. 2, no. 7 (May 1875); public domain. Retold in original words; the cow, pig and fox chase follows the tale's pattern.
- Big Turnip: "Repka" (The Turnip), in Aleksandr Afanasyev, Narodnye russkie skazki (1855 to 1863); public domain. Retold in original words; the bear choice is this tool's own addition, marked as a choice.
- National Core Arts Standards, Theatre, grades K to 2 (TH:Cr1, TH:Pr4): https://www.nationalartsstandards.org
- Sound effects: original, made in code. Puppets, costumes, trunk, turnip and backdrops: original paintings (Art).
- Checks run (Python, 2026-10-29): every contrast ratio in Look recomputed with the WCAG 2.1 formula (white on brand 8.17, brand on paper 7.48, ink on paper 14.47, muted on paper 5.87, ink on Sun gold 8.66, white on Moon navy 10.11, white on curtain 11.76; all match the stated values to rounding). Sounds: TRIP TRAP an octave lower is 450 and 550 Hz; the sparkle C6 E6 G6 is 1046.5, 1318.5 and 1568.0 Hz. Each story walked beat by beat: Billy Goats 13 beats, Gingerbread 13, Turnip 11 (the bear choice adds one spoken line, not a beat); every piece a dress or act beat hands out is in the 20-piece list; where a later beat gives a puppet a second piece for the same place (big curly horns over little horns, fox ears over cow horns, hair bow over straw hat) the new piece replaces the old one, as in Trunk. No score, timer or tolerance to check.

## Done when
1. All three stories play start to end with Next only, every beat's line spoken (log shows `spoken` once per beat visit), and Back restores the previous beat's costumes exactly.
2. On every act and dress beat the acting side's puppet is lit and the beat card names the side with its icon and word; Swap flips the roles for the rest of the story and the puppets' outfits.
3. Choose beats keep Next disabled until a choice is tapped, and the next act line matches the choice (booming or squeaky; fast or slow; bear then mouse).
4. Freeze works from both modes and any beat, speaks "Freeze!" and "Unfreeze!" every time, and Next while frozen unfreezes.
5. Trunk: one piece per place (a new hat replaces the old), every painted piece sits on its place on both puppets at every size, Surprise me never doubles a place, Ask cycles all five questions, every sound button plays.
6. Focus: at 1366x768 and 680x425 the acting puppet in its costume is the brightest, central thing in the story player, and the Trunk puppet is the largest thing on the Trunk stage.
7. Tap while it plays: Next, Back, Swap or Freeze tapped mid-line, mid-flight, mid-swap or mid-turnip-grow acts at once; the old line stops and no stale line plays after.
8. How-to lines are spoken once in a run of five Next taps; story lines and Freeze lines are spoken every time.
9. Every control is 60 px or more with an icon and a word; the main bar is visible without scrolling at every size in STANDARDS.md.
10. Motion off: no sway, slides or growing animation, and the turnip shows in three steps; story pacing is unchanged. Nothing is stored; no network requests.

## Open questions
- The Gingerbread Boy's classic ending has the fox eat him (told gently, beat 12). Keep it, or end with him jumping safely to the far bank?
