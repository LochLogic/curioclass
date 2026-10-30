# Family Dance Night

## One idea
The school gym is set for family dance night, and every table around the floor is a family sharing a dance from home: tap a table and its dance fills the floor, slow it down to copy a move, name it with dance words, pick a favorite part, and turn the table card over to see the people, the place and the day the dance belongs to; each table visited lights up one more string of lights over the gym.

## Not like
- art-passport (k-2, explorer): visits artworks on a world map and collects stamps. Here the things are dances you copy with your body, the place is a family's table in your own gym, and the reward is the room getting brighter, not stamps.
- orchestra-zoo (k-2, explorer): meets instruments by family. Here the music is only the beat under the dance; the moves are what the class studies.
- levels-and-pathways (k-2, showdown, dance family): copies levels and pathways from one studio dancer. Here every dance comes from a people and a place, and the questions are what you notice and what it is for.
- feeling-scarf-dance (k-2, studio, this batch): the class makes its own dance about a feeling. Here the class watches, copies and describes dances other people made.
- dance-styles-explorer (9-12, explorer): traces and critiques styles. Here there is no trace or critique: copy, describe, like and connect.

## Who and how
- Grade K-2, dance, module "Dances of Many Places".
- Driver: teacher on a projector or smartboard; the class stands to copy moves, names dance words, votes on favorites. 15 to 25 minutes (two or three tables a day works well).
- Standards: NCAS DA:Re8 (describe movement with dance words), DA:Re9 (say what you like about a dance and why), DA:Cn11 (dances come from people, places and occasions).

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). No mode buttons: the gym is home, and each table opens its own dance view.

**Gym (home).** Focus: the painted gym, wide, with seven tables around the edges of the floor (painted table cutouts, each with the objects that family brought), each with a big round button over it (60 px or more) showing a small icon and the dance's name. Strings of lights cross the ceiling, one per table, dark until that table is visited. A small `Lights` counter in the corner ("3 of 7") with a bulb icon.

**Dance view.** Focus: the dancer(s) in the middle of the gym floor (dance engine code figures, about 50% of the stage height), with that table's painted objects at the side. The panel (right, or below on narrow screens) has four big tabs, each icon plus word:
- `Watch` (eye): `Play` / `Stop` (gold) plays the dance's 16-count loop with its music; `Slow` toggle (60% speed).
- `Copy` (mirror): two move buttons (`Move 1`, `Move 2`, each with its name and a still figure icon). Tap one: the dancer does only that move, slow, facing the class and mirrored so the class copies it like a mirror, with big count numbers. `Count me in` plays a 4-count count-in first.
- `Words` (speech bubble): twelve dance-word chips (icon plus word): `Fast`, `Slow`, `High`, `Low`, `Big`, `Small`, `Smooth`, `Sharp`, `Stamp`, `Hop`, `Turn`, `Shake`. Tap one while a move is showing: the narrator says if the class can see it in that move (Content).
- `Where from` (map pin): the table card turns over: a simple world map (drawn in code) with a pin, the place in words, who dances it and when (two short sentences, spoken), and the prop's painted picture.
- A heart button, `Favorite part`, opens four big choices: `Move 1`, `Move 2`, `The music`, `The <prop>`; the class votes with hands and the teacher taps the winner; the narrator asks why.
- `Back to the gym` (house icon) returns home; the table's lights turn on (with a soft chime) the first time.

## Content
Seven dances. For each: table objects; place and map pin (latitude, longitude); who and when (spoken); dancer look (dance.js colors and extras); music (original, in the style, made in code); two moves (name; what the dancer does; counts; dance words that fit).

1. **Lion Dance.** Table: a lion head mask, red lanterns, a big drum. Place: Guangdong, southern China (23.0, 113.1). "The lion dance comes from southern China. Two dancers become one lion, for good luck at the Lunar New Year." Look: two dancers under the painted lion (head on the front dancer's chest and head joints, body cloth over both backs); only their legs show (bottom #c8102e, shoes #f2e6da). Music: 100 bpm, big drum (kick and low tom) with crash cymbals (filtered noise) on 2 and 4, a gong on count 1 of every 8. Moves: (1) Lion wakes up: the head rises from low to high and shakes side to side, the mouth opens and closes; 8 counts; High, Low, Shake. (2) Lion bows: the lion steps forward, dips the head low, blinks, rises; 8 counts; Low, Slow, Big.
2. **Jarabe Tapatio** (folklorico). Table: colorful ribbons, a wide-brim hat, a folded skirt. Place: Jalisco, Mexico (20.7, -103.3). "Folklorico dancers in Mexico dance the jarabe at fiestas. Their feet tap a rhythm on the floor." Look: dancer top #f6f1e7, bottom (a wide skirt drawn in code, ruffled, in #e4572e, #2b9348 and #f2c14e bands), shoes #3a2a1c. Music: 132 bpm, 3/4 with 6/8 feel, bright strings (pluck) and a trumpet line (sawtooth through a low-pass). Moves: (1) Zapateado: quick stamping steps, heel and toe, in place; 8 counts; Fast, Stamp, Small. (2) Skirt swirl: holding the skirt out with both hands, sweeping it up and down while turning; 8 counts; Turn, Big, Smooth.
3. **Irish Step Dance.** Table: a fiddle, hard shoes, a tin whistle. Place: Ireland (53.3, -6.3). "Irish dancers keep their arms still at their sides while their feet move fast. They dance at ceili parties." Look: top #1b5e20, bottom #1b5e20, shoes #111111. Music: 112 bpm reel, fiddle-like line (sawtooth with vibrato), bodhran-like drum (low tom). Moves: (1) Still arms, busy feet: arms straight down, quick toe steps; 8 counts; Fast, Small, Hop. (2) Hop and kick: hop on one foot, kick the other high, switch; 8 counts; Hop, High, Sharp.
4. **Bhangra.** Table: a dhol drum, a bright embroidered scarf, a basket of wheat. Place: Punjab, a region in India and Pakistan (31.6, 74.9). "Bhangra comes from Punjab. Farmers danced it to celebrate the harvest, and people dance it at weddings and parties today." Look: top #f2a900, bottom #ffffff, a turban drawn in code in #c2185b. Music: 96 bpm, dhol pattern (kick on 1, slap on the "and" of 2, the chaal swing in eighths), a pluck melody. Moves: (1) Shoulder bounce: arms up high, shoulders bounce on every count; 8 counts; High, Shake, Fast. (2) Bhangra hop: hop on one foot, the other knee up, arms up, switch; 8 counts; Hop, High, Big.
5. **Korean Fan Dance** (buchaechum). Table: two painted fans, a ribbon, a small drum. Place: Korea (37.6, 127.0). "In the Korean fan dance, dancers open and close big painted fans. Together the fans look like flowers and waves." Look: top #f06292 jacket, bottom (a long full skirt drawn in code) #4fc3f7; a painted fan in each hand (open and closed cutouts). Music: 60 bpm, 3/4, a soft flute-like line (sine with breath noise) and an hourglass-drum pattern (low and high tom). Moves: (1) Fan wave: both fans open, sweeping up and down slowly like a wave; 8 counts; Smooth, Slow, Big. (2) Flower: fans held together in a circle above the head, the dancer turns slowly; 8 counts; Turn, High, Smooth.
6. **Second Line.** Table: a decorated umbrella, a trumpet, a handkerchief. Place: New Orleans, Louisiana, USA (29.95, -90.07). "In New Orleans, people dance in the street behind a brass band. The dancers who follow the band are called the second line." Look: top #ffd23f, bottom #1d3557, a painted umbrella in the right hand, a white handkerchief (code) in the left. Music: 100 bpm swung, brass band (sawtooth chords), tuba bass, snare and bass drum. Moves: (1) Strut: big bouncy steps forward and back, knees up; 8 counts; Big, Hop, Fast. (2) Umbrella twirl: the umbrella spins up high while the dancer turns; 8 counts; Turn, High, Smooth.
7. **Kpanlogo.** Table: kpanlogo drums, a shaker, a bright patterned cloth. Place: Accra, Ghana (5.6, -0.2). "Kpanlogo is a dance of the Ga people of Accra, Ghana. Drummers and dancers play together at celebrations." Look: top and bottom a patterned cloth pattern drawn in code (#f4a300 and #00695c), shoes #6d4c41. Music: 112 bpm, kpanlogo drums (high and low tom pattern), a shaker in eighths, a bell (wood) timeline. Moves: (1) Shoulder roll and arm swing: loose arms swing forward and back with rolling shoulders; 8 counts; Smooth, Big. (2) Low bounce: knees bent, bouncing low, arms out, stepping side to side; 8 counts; Low, Fast, Small.

**Word answers:** in the move: "Yes! I see <word>." Not in it: "Hmm, look again. Do you see <word>?" (no other feedback; the class decides).
**Favorite part lines:** "Why do you like it? Tell a friend."

## Interactions in detail
- Tables can be visited in any order and again. The lights for a table turn on when the class leaves its first visit (event chime), and stay on for the page visit (nothing saved). All seven: the gym's main lights brighten and the line for all seven plays (event).
- One run at a time (dance.md rule): Play, a move button, Count me in, a tab switch or Back to the gym stops the old clock, music and voice first.
- Tap while it plays: Slow, a move button or a word chip acts at once (Slow changes the speed from the next count, at most 0.6 s at 100 bpm; the chip's answer waits until the move finishes its count, then plays over a lowered music level; a move tapped mid-run starts at once).
- Copy view: facing 0 (to the class) and `Dance.mirror` applied, so the dancer's right is the class's right; the count numbers are big over the floor.
- Words: chips answer for the move last shown (Move 1, Move 2, or the full loop, which counts as both moves).
- Where from: the map is a simple world outline with country borders off; the pin is a big dot with a label. The two sentences are spoken.
- Sound off: no music, the dancers still move to the clock.
- Motion off: one pose per count (the engine's calm mode); the lights switch on without a fade.
- Keyboard: Tab order is table buttons, then (in a dance) the tabs and their controls; Space plays or stops; Escape goes back to the gym.

## Look
- Accent (`--brand`) #7f1d1d maroon gym banner (header, Play, table buttons' ring). Paper #fbf6ee, ink #2a1c18, muted #6a5850. Gym: honey maple floor, painted cinderblock walls in cream, warm string lights (#f7d774) that are dark grey until lit.
- Each dance's colors live on its dancer and objects, never in the chrome. Every table button pairs its icon with its name.
- Contrast (WCAG 2.1, computed): white on brand 10.02:1; brand on paper 9.31:1; ink on paper 15.28:1; muted on paper 6.25:1.
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people: dancers are the dance engine's code figures (no faces), and each table shows a family's objects only. One warm painted picture-book style.
- gym: "An empty school gymnasium decorated for a family dance night, a shiny maple wood floor, cream cinderblock walls, a small stage at the back, strings of unlit bulbs across the ceiling, warm evening light, painted picture book illustration, the floor open and clear"; 16:9; cutout no; people no; home and the dance view backdrop (the `square` floor's backdrop).
- 7 table cutouts, each "A small round table with a white cloth holding <objects>, painted picture book illustration, plain white background", 4:3, cutout yes, people no: a red and gold Chinese lion dance head, two red paper lanterns and a big red drum; colorful ribbons, a wide-brim charro hat and a folded ruffled skirt; a fiddle, a pair of black hard dance shoes and a tin whistle; a dhol drum, a bright embroidered phulkari scarf and a basket of wheat; two large painted Korean dance fans with pink flowers and a small hourglass drum; a decorated parade umbrella with fringe, a trumpet and a white handkerchief; two tall carved kpanlogo drums, a gourd shaker and a folded bright patterned cloth.
- lion-head-closed, lion-head-open: "A Chinese southern lion dance head, red, gold and white with a fluffy fringe and big eyes, mouth <closed / open>, side front view, painted picture book illustration, plain white background"; 1:1; cutout yes; people no; on the front lion dancer, swapped on beats.
- lion-body: "A long red and gold lion dance body cloth with a fluffy fringe edge, spread flat, side view, painted picture book illustration, plain white background"; 16:9; cutout yes; people no; over both lion dancers' backs, bent in code into two to three segments.
- fan-open, fan-closed: "A large Korean dance fan with pink peony flowers and a feathered edge, <fully open / folded closed>, painted picture book illustration, plain white background"; 1:1; cutout yes; people no; in each hand of the fan dancer, swapped and rotated by the move.
- umbrella: "A decorated second line parade umbrella with gold fringe and sequins, open, painted picture book illustration, plain white background"; 1:1; cutout yes; people no; in the second line dancer's hand, spun in code.
14 images, none with people. Drawn in code: the dancers and floor (engine), skirts, turban, handkerchief and patterned cloth (they bend and swing), the lights, the world map and pins, chips, tabs.

## Voice
Bank voice `clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient elementary school teacher". The host of the night, speaking plainly about each family's dance. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.table + ':' + state.tab`. Music rule: lines wait for a run to end or play over the music lowered 6 dB; no line plays during a count-in.

- how, welcome (Gym; stale when a table is tapped): "Welcome to family dance night! Each table has a dance from home. Tap a table."
- event, a table opens: "The <name>!" (7 lines)
- how, first table opened (stale when Play is tapped): "Tap Play to watch the dance."
- how, first loop ends (stale when Copy is tapped): "Want to try it? Tap Copy, then tap a move."
- event, a move shown in Copy: "<move name>. Stand up and copy me!" (14 lines)
- how, first Copy move ends (stale when a chip is tapped): "What did you see? Tap a dance word."
- event: the word answers ("Yes! I see <word>." / "Hmm, look again. Do you see <word>?", 12 words each, 24 lines).
- event, Where from: the two sentences for that dance (7 lines).
- event, Favorite part tapped: "Why do you like it? Tell a friend."
- event, first visit lights on: "Thank you for sharing your dance! The lights are on."
- event, all seven: "Every family shared a dance. The whole gym is glowing!"
- Read speaks the hint, or the open card's sentences.

## Family engine
Dance (`kit/dance.js`, docs/families/dance.md), though the catalog lists this tool with no family. Uses: `Dance.floor(svg, 'square', {backdrop: gym})`, `Dance.dancer` (one per dance; two for the lion), `Dance.poses` and partial poses for the 14 moves (keyframes written by the builder from the descriptions in Content, checked in a contact sheet), `Dance.mirror`, `Dance.phrase`, `Dance.clock` with `countIn: 4`, `Dance.play`, `Dance.music` for drum and pluck parts, `Dance.counts`, `Dance.icon` for the move buttons. Tool code: skirts, turban, handkerchief and patterned cloth on the figure; the painted props on hand joints (`d.world('rHa')`, `'lHa'`); the lion head on the front dancer's head; extra timbres (gong, crash cymbal, brass, fiddle, flute) in Web Audio. The builder adds this tool to the dance.md table.

## Sources
- National Core Arts Standards, Dance, grades K to 2 (DA:Re8, DA:Re9, DA:Cn11): https://www.nationalartsstandards.org
- Lion dance (southern style from Guangdong; two dancers, drum, cymbals and gong; Lunar New Year and good luck): Smithsonian Folkways / Smithsonian Center for Folklife, "Lion Dance" (https://festival.si.edu); Library of Congress, Chinese New Year resources.
- Jarabe tapatio (Jalisco; Mexico's national dance; zapateado footwork; dancing around the hat): Encyclopaedia Britannica, "jarabe" (https://www.britannica.com/art/jarabe); Ballet Folklorico de Mexico de Amalia Hernandez, repertoire notes.
- Irish step dance (arms at sides, quick footwork, ceili and feis): Encyclopaedia Britannica, "Irish dance" / "step dancing" (https://www.britannica.com/art/step-dancing).
- Bhangra (Punjab, harvest festival Vaisakhi, dhol drum, today at weddings and parties): Encyclopaedia Britannica, "bhangra" (https://www.britannica.com/art/bhangra).
- Korean fan dance, buchaechum (fans with peonies, group shapes like flowers and waves): Korea Tourism Organization / Korea.net, "Buchaechum" (https://www.korea.net).
- Second line (dancers following the brass band in New Orleans parades, umbrellas and handkerchiefs): New Orleans Jazz National Historical Park, NPS, "Second Line" (https://www.nps.gov/jazz); Smithsonian Folklife Magazine.
- Kpanlogo (Ga people of Accra, Ghana, 1960s; drums and dance at celebrations): Encyclopaedia Britannica, "Ga" and Ghana music entries; Ladzekpo, C. K., "Kpanlogo" notes (Columbia University, African music teaching pages).
- All music is original, made in code in the style of each tradition; no traditional or recorded tune is reproduced. Teacher notes link to real performances (outbound links only).
- Map pins: city or region coordinates (Guangzhou area, Guadalajara, Dublin, Amritsar, Seoul, New Orleans, Accra) from GeoNames (https://www.geonames.org); the world outline from Natural Earth 1:110m (public domain).
- Checks run (Python, 2026-10-29): 16-count loops: 9.6 s at 100 bpm (lion, second line), 7.3 s at 132 (jarabe), 8.6 s at 112 (Irish, kpanlogo), 10.0 s at 96 (bhangra), 16.0 s at 60 (fan dance); Slow at 60% makes the longest 26.7 s, with Stop always live. Every move's dance words are drawn from the 12 chips; each chip is true for at least one move (Fast 5, Slow 2, High 6, Low 3, Big 6, Small 3, Smooth 5, Sharp 1, Stamp 1, Hop 4, Turn 3, Shake 2; 38 word-move pairs over 14 moves). Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the dancers are the central, largest thing in a dance view; in the gym all seven table buttons are visible and 60 px or more.
2. All seven dances loop with their music and both moves play in Copy, mirrored and facing the class, with no console error; a contact sheet of the 14 moves shows each as its own shape.
3. Every word chip answers per the move's word list.
4. Tap while it plays: Slow, a move button, a tab or Back to the gym acts at once (a new run stops the old one first); a chip answer never talks over a count-in.
5. Lights turn on per first visit, the counter matches, and all seven brighten the gym with its line.
6. Where from shows the right pin and speaks the two sentences for every dance.
7. How-to lines are spoken once in five actions; table names, word answers and Where from lines are spoken every time.
8. Every control is 60 px or more with an icon and a word; Play and the tabs are visible without scrolling at every size in STANDARDS.md.
9. Motion off: one pose per count, no light fades; music timing unchanged.
10. No network requests; nothing is saved.

## Open questions
- Cultural review: like the ASL tools, should each of the seven dances (and its costume colors, props and one-sentence description) be checked by someone from that tradition before release? The spec keeps descriptions short and sourced, but code figures in costume colors can still read as stereotypes.
