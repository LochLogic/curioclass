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

**Story player.** The stage fills about 75% of the screen: the story's backdrop, and two peg puppets standing on it, the Sun puppet on the left under a sun badge "Sun side", the Moon puppet on the right under a moon badge "Moon side". Each puppet wears that side's current costume. Below the stage, the teacher bar (60 px buttons, icon plus word): `Back`, `Next` (big, gold, right), `Swap` (two arrows), `Freeze` (snowflake), `Sound effect` (speaker; shows the beat's sound name, disabled when the beat has none), `Home` (house).
- A beat card above the bar shows the beat's line in big type and, for act beats, who acts: "Sun side", "Moon side" or "Everyone" with the badge icons.
- The acting side's puppet stands in a warm spotlight and sways gently; the other puppet dims to 60%. For "Everyone", both are lit.
- Dress beats: the trunk lid opens at the bottom center, the piece flies to the puppet (500 ms; with Motion off it appears), and the narrator asks the class to put it on (mime).
- Choose beats: two big choice buttons on the stage, each with an icon and a word. The choice sets the next act line.
- Freeze beats: a gold picture frame draws around the stage and the word "Freeze!" appears; Next plays a soft camera click and goes on.
- End beat: "The end" on the curtain, with `Swap and play again` (both sides trade parts and the story restarts at beat 1) and `Home`.

**Trunk (explore).** The stage shows one big peg puppet on a chosen backdrop. Under it, the open trunk: a scrolling tray of costume piece buttons (picture plus word), grouped by where they go (head, face, body, feet, tail). Tap a piece: it jumps onto the puppet; one piece per place, so a new hat replaces the old one; tap a worn piece again to take it off.
- Panel strip: `Backdrop` (cycles the six backdrops in Art, starting with little-stage), `Surprise me` (dice: a random outfit of 3 or 4 pieces), `Take it all off`, `Ask` (question mark: speaks the next character question), `Freeze`, and a row of eight sound buttons (icon plus word) that play their effect.

## Content
**Costume pieces** (drawn in code, flat shapes with a dark outline; place in brackets): little horns [head], big curly horns [head], straw hat [head], crown [head], wizard hat [head], fox ears [head], dog ears [head], mouse ears [head], cow horns and bell [head and neck as one piece], hair bow [head], pig snout [face], cat whiskers [face], big troll nose [face], icing buttons [body], candy bow tie [body], apron [body], shawl [body], shaggy cape [body], big boots [feet], bushy tail [tail]. 20 pieces.

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

*Big Turnip* (the sides take turns joining the pulling line; the turnip is drawn in code and grows):
1. tell (garden): "Grandpa planted a tiny turnip seed. He said: Grow, little turnip. Grow big and sweet!"
2. act [Everyone]: "Everyone, be the seed. Curl up small. Now grow, grow, grow, and stretch up tall!" (the turnip grows from a sprout to giant over 4 s; with Motion off, in three steps)
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
- Next advances one beat; Back goes back one beat, restores that beat's costumes and stops speech. Next and Back are never locked: the teacher keeps the pace. Each beat's line is spoken when the beat opens (Voice). There is no timer and no score.
- Costumes are state per beat: going back removes pieces given later. Swap mid-story trades the two puppets' outfits (a 400 ms slide across; with Motion off, a jump), flips the side roles for every later beat, and speaks the Swap line.
- Freeze button (any time, both modes): draws the frame, speaks "Freeze!"; the button becomes `Unfreeze` (melting snowflake); tapping it speaks "Unfreeze!" and clears the frame. Next while frozen also unfreezes.
- Sound effect button replays the beat's sound; the class may also make the sound themselves.
- Choose beats: Next is disabled until a choice is tapped (the hint and Read say so); the choice button stays outlined, and Back to the choice beat lets the teacher pick again.
- Trunk: Surprise me never gives two pieces for the same place. Take it all off empties the puppet with a little hop. The trunk keeps its outfit and backdrop when switching modes (in memory only; nothing is saved).
- Home stops speech and returns to the story tiles; a story restarts at beat 1 with Sun as the first role list.
- Keyboard: Right arrow = Next, Left arrow = Back, F = Freeze, S = Swap, Space on a focused button presses it.

## Look
- Accent (`--brand`) #7d2e7f trunk plum (header, Next border, selected choice). Paper #fbf4ea, ink #2a1f2b, muted #6a5a68; curtain #5a1f5c with darker folds; trunk wood #8a5a34 with brass corners #d2a54a; Sun badge #f2b632 with ink text and a sun icon; Moon badge #2c3e7a with white text and a moon icon (never color alone: icon plus word on every badge).
- Contrast: white on brand 8.2:1; brand on paper 7.5:1; ink on paper 14.5:1; muted on paper 5.9:1; ink on Sun gold 8.7:1; white on Moon navy 10.1:1; white on curtain 11.8:1.
- Puppets: wooden peg dolls drawn in code (round head with two dot eyes and a small smile, rounded body, peg feet), light wood #e8c99a with a #6b4a2b outline. Costume pieces in bright flat colors with the same outline.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8.

## Art
Cloudflare FLUX.2 (`scripts/cfart.py`), backdrops only; puppets, costumes, trunk and the turnip are drawn in code. Each is a full-frame painted storybook scene, soft gouache style, the lower third kept simple and open (the puppets stand there), blank surfaces only.
- meadow-bridge: a small wooden footbridge over a clear stream between two grassy banks, a green hill with long grass beyond, morning light, storybook gouache; 16:10; cutout no; people no; Billy Goats backdrop and a Trunk backdrop.
- cottage-kitchen: a cozy cottage kitchen with a big black iron oven, a wooden table with a rolling pin, a window with gingham curtains, warm light; 16:10; cutout no; people no; Gingerbread beats 1 to 4.
- country-road: a dirt country road between a fenced green field and a muddy pen, hills behind; 16:10; cutout no; people no; Gingerbread beats 5 to 7.
- wide-river: a wide blue river with reeds and a grassy bank in front, far trees across the water; 16:10; cutout no; people no; Gingerbread beats 8 to 13.
- veggie-garden: a cottage vegetable garden with neat rows of leafy plants, a wooden fence and a watering can, a wide empty patch of soil in the center; 16:10; cutout no; people no; Big Turnip backdrop (the turnip is drawn in code in the empty patch).
- little-stage: an empty small wooden theater stage with plum velvet curtains drawn open and warm footlights; 16:10; cutout no; people no; Trunk default backdrop and the story tiles' curtain.

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), style "Say gently and expressively, like a grandmother reading a picture book aloud". Not used by any k-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, calm-corner warm-teacher). `Curio.voice` with `scope: () => state.mode + ':' + state.story`. Every fixed line is recorded.

- how, welcome (Stories): "Welcome to Act It Out! Teacher, tap a story to begin. Or tap Trunk to play dress-up."
- event, story start: "The Three Billy Goats Gruff." / "The Gingerbread Boy." / "The Great Big Turnip." (stale on Home)
- event, every story beat line in Content (both variants of beats with choices, and the bear line): spoken each time the beat opens, stale when the beat changes.
- how, first act or dress beat: "When everyone has had a turn, tap Next." (then hint only)
- how, first choose beat: "Let the class choose. Then tap their choice." (needs the choice buttons)
- how, first Swap seen on an end beat: "Tap Swap and play again to trade parts."
- event: "Swap! Sun side and Moon side, trade parts." / "Freeze! Everyone be a statue." / "Unfreeze!"
- how, welcome (Trunk): "This is the dress-up trunk. Tap a costume piece to dress the puppet."
- how, after the second piece: "Tap Ask, and the class can answer my question."
- event: each character question in Content (spoken every time Ask is tapped; stale on the next tap).
- event, Surprise me: "Ta-da! Who could this be?"
- event, Take it all off: "All clean. Let's dress up someone new."
- Read speaks the current beat line (or the hint).

## Family engine
none

## Sources
- Billy Goats: "The Three Billy-Goats Gruff", in George Webbe Dasent, Popular Tales from the Norse (Edinburgh, 1859), from Asbjornsen and Moe; public domain. Retold here in original words, softened (no injury).
- Gingerbread Boy: "The Gingerbread Boy", St. Nicholas Magazine, vol. 2, no. 7 (May 1875); public domain. Retold in original words; the cow, pig and fox chase follows the tale's pattern.
- Big Turnip: "Repka" (The Turnip), in Aleksandr Afanasyev, Narodnye russkie skazki (1855 to 1863); public domain. Retold in original words; the bear choice is this tool's own addition, marked as a choice.
- National Core Arts Standards, Theatre, grades K to 2 (TH:Cr1, TH:Pr4): https://www.nationalartsstandards.org
- Sound effects, puppets and costumes: original, made in code.

## Done when
1. All three stories play start to end with Next only, every beat's line spoken (log shows `spoken` once per beat visit), and Back restores the previous beat's costumes exactly.
2. On every act and dress beat the acting side's puppet is lit and the beat card names the side with its icon and word; Swap flips the roles for the rest of the story and the puppets' outfits.
3. Choose beats keep Next disabled until a choice is tapped, and the next act line matches the choice (booming or squeaky; fast or slow; bear then mouse).
4. Freeze works from both modes and any beat, speaks "Freeze!" and "Unfreeze!" every time, and Next while frozen unfreezes.
5. Trunk: one piece per place (a new hat replaces the old), Surprise me never doubles a place, Ask cycles all five questions, every sound button plays.
6. How-to lines are spoken once in a run of five Next taps; story lines and Freeze lines are spoken every time.
7. Every control is 60 px or more with an icon and a word; the main bar is visible without scrolling at 680x425, 1366x768 and 1920x1080.
8. Motion off: no sway, slides or growing animation, and the turnip shows in three steps; story pacing is unchanged.
9. Nothing is stored; no network requests.

## Open questions
- The Gingerbread Boy's classic ending has the fox eat him (told gently, beat 12). Keep it, or end with him jumping safely to the far bank?
