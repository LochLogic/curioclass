# Director's Chair

## One idea
Direct the same short scene, the Guard's report from Sophocles' Antigone, as a guest director in five theaters (Greek, Noh, commedia, Elizabethan, modern realist); each house has its own stage shape and rules, and watching your choices from its seats shows what that tradition makes the audience notice.

## Not like
- globe-theatre-stage (ELA 12, explorer, shakespeare family): switches line delivery in Shakespeare scenes on one 3D Globe. Here the scene is not Shakespeare, the Globe is one house of five, and the variable is each tradition's staging rules and stage shape, not the reading of a line.
- stage-blocker (6-8, same family and engine): free blocking on one modern proscenium, tested against notes for sightlines. Here the stages are historical, the blocking comes from directing choices inside each tradition's rules, and the result is interpretation, not a pass or fail.
- gallery-critique (9-12, roleplay): argues about a painting from evidence. Here you make the choices and compare productions.
- dramatic-irony-theater (ELA 8, story) and storyboard-studio (9-12, media): watch a scene or plan camera shots. Here the audience is live, seated, and changes with the theater.
- Overlap note settled: took the suggested reshape (five traditions instead of tone, pacing and setting switches).

## Who and how
- Grade 9-12, theater, module "Theater History and Directing (Theater)": theatrical traditions; directing choices.
- Topic line: theater traditions and directing
- Driver: students on laptops, alone or in pairs; a teacher can project one house and let the class vote each choice. 40 to 50 minutes (one or two houses per sitting works too).
- Standards: NCAS TH:Re8 (interpret intent and meaning), TH:Cn11 (relate theater to its cultural and historical context); also TH:Cr2 (a directing concept shaped by history and culture), TH:Re7 (respond to the choices in each version), TH:Re9 (justify the director's note with evidence).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit, theme-912). Mode buttons (`.seg`): `Tour` (default), `Compare`.

**Tour.** Focus: the five painted house cards, large, filling the stage. Five house cards in a row (stacked at narrow widths), in history order, each with its picture (Art), name, place and date line, and a status ("not staged" or "staged" with a check). Tap a card to arrive. Any order is fine.

**Arrival.** Focus: the house picture, wide across the stage, with the rules beside it. The house picture with its name and date line, the house rules (three or four short lines), and the cast list ("Here the Guard is played by..."), each masked role shown with its painted mask (Art). Button `Begin`.

**Scene.** Focus: the House view from the chosen seat, the biggest thing on screen (at least 60% of the width at 1366x768), with the choice card beside it in the panel so a choice and its result are seen together. The stage area is the engine's House view from the chosen seat, with the ground plan in a corner inset (seats shown; tap one to sit there). Panel, top to bottom: `Seat` (cycles the house's three seats; names in Content), the script (eight beats, current one highlighted, speaker names as this house casts them), `Prev beat`, `Next beat`, `Play scene` (plays all beats with the engine's tweening). At each choice beat (three per house) the panel shows a choice card with two options, each a name and one line; choosing applies its blocking to that beat and every later beat until the next choice, plays the beat, and opens the "What the audience notices" card (two sentences, plus the engine's focus leader from the current seat: "From the yard, the eye goes to the Guard."). `Change choice` reopens the card. After the third choice, `Program note`: the three choices with their first notice sentence, and `Back to tour`.
- `Adjust` (toggle, off by default): drag actors on the inset plan (it grows to half the stage). The house rules are checked softly: a broken rule shows a note in words ("In Noh, entrances come along the bridgeway"), never blocks the move.

**Compare** (enabled after two houses are staged). Focus: the grid of small House views, filling the stage. A `Beat` picker (buttons 1, 4, 6, 8). Small House views of every staged house from its front seat side by side (wrapping to two rows), each with the house name, the chosen option at that beat (or "house default") and its notice line. Below: `Director's note` (a text box, 600 characters, prompt "Which theater made the Guard most sympathetic, and how?"), `Save on this device`, `Clear` (localStorage `curio-directors-chair`, which also keeps choices per house).

## Content
**The scene.** Sophocles, Antigone, the Guard's report, in F. Storr's translation (Loeb, 1912), cut to eight beats; [...] marks a cut. Two dashes in Storr's text are set as commas here (house rule: no long dashes).
1. Guard: "My lord, I will not make pretense to pant / And puff as some light-footed messenger. / In sooth my soul beneath its pack of thought / Made many a halt and turned and turned again; [...] Thus leisurely I hastened on my road; / Much thought extends a furlong to a league."
2. Creon: "What is thy news? Why this despondency?" Guard: "Let me premise a word about myself? / I neither did the deed nor saw it done, / Nor were it just that I should come to harm."
3. Creon: "Then, sirrah, shoot thy bolt and get thee gone." Guard: "Well, it must out; the corpse is buried; someone / E'en now besprinkled it with thirsty dust, / Performed the proper ritual, and was gone."
4. Creon: "What say'st thou? Who hath dared to do this thing?" Guard: "I cannot tell, for there was ne'er a trace / Of pick or mattock, hard unbroken ground, [...] so lots were cast, / And I, unlucky scapegoat, drew the prize. / So here I am unwilling and withal / Unwelcome; no man cares to hear ill news."
5. Chorus: "I had misgivings from the first, my liege, / Of something more than natural at work."
6. Creon: "O cease, you vex me with your babblement; / I am like to think you dote in your old age. [...] By Zeus I swear, except ye find and bring / Before my presence here the very man / Who carried out this lawless burial, / Death for your punishment shall not suffice."
7. Guard: "May I not speak, or must I turn and go / Without a word?" Creon: "Begone! canst thou not see / That e'en this question irks me?" Guard: "Where, my lord? / Is it thy ears that suffer, or thy heart?" [...] Creon: "What an inveterate babbler! get thee gone!" Guard: "Babbler perchance, but innocent of the crime." (Creon exits.)
8. Guard, alone: "I pray he may be found. But caught or not / (And fortune must determine that) thou never / Shalt see me here returning; that is sure. / For past all hope or thought I have escaped, / And for my safety owe the gods much thanks."
A one-line setup shows above beat 1: "Creon, the new king of Thebes, has forbidden anyone to bury the rebel Polynices. A guard arrives with news."

**Houses** (`Stage.house` data; x across as the front seats see it, negative to their left; y away from them; meters; sizes approximate, drawn after the sources, the tool's own simplification). Each lists: date line; rules; cast; seats; layout; default blocking; three choices (beat: option, blocking; notice).

*Greek theater.* Date line: "Athens, 400s BC (stage drawn after Epidauros, about 330 BC)". frame arc, light daylight.
- Rules: "Every actor wears a mask, and there are no more than three speaking actors." / "The chorus is part of the action: it stays in the round orchestra and answers as a group." / "Actors come on by the side roads or through the stage building's door."
- Cast: Guard, Creon (masks); the Chorus of Theban elders, shown as seven masked figures, the leader marked CL.
- Seats: Front row (0, -1, eye 1.2); Side wedge (-14, 4, eye 4); Top row (0, -45, eye 22).
- Layout: orchestra circle center (0, 10), radius 10; low stage x -10 to 10, y 20 to 23, height 1; stage building wall at y 23 (height 6) with a door at (0, 23); side roads at (-15, 12) and (15, 12). Default: Creon (0, 21.5) facing the front row; chorus in an arc radius 4 around (0, 12) facing the stage, CL at (0, 9); Guard ends beat 1 at (2, 16) facing Creon.
- Beat 1: Long side road (enters by the right road and crosses the orchestra while speaking) / Skene door (appears in the door and stops at (3, 21.5) beside Creon). Notices: "The long walk plays the Guard's dread before Creon says a word. His line about the road becomes something you watch." / "He appears at the king's elbow, so his fear is about Creon, not the road. The long road lives only in his words."
- Beat 5: Draw together (the elders close to radius 3 around (0, 15), all facing Creon; CL at (0, 17)) / Turn to the audience (the elders face the front row; CL steps to (0, 6)). Notices: "Masks cannot change expression, so the group's bodies carry the worry: the whole city leans toward the palace." / "Turned to the seats, the elders share their doubt with the people watching, and the audience joins the council."
- Beat 6: From the stage (Creon stays at (0, 21.5)) / Down into the orchestra (Creon crosses to (0, 12) among the elders, facing the Guard). Notices: "Above the orchestra, before his own door, Creon speaks from the seat of power, and the elders look up at him." / "Down among the elders, the oath happens inside the city, and the chorus around him becomes the crowd he threatens."

*Noh.* Date line: "Japan, from the 1300s (today's Noh stage)". frame open (roofed square plus bridgeway), light even.
- Rules: "The main actor, the shite, wears a mask; the pillars help him find his place." / "Entrances and exits come along the bridgeway, the hashigakari." / "The chorus sits at the side and sings; the pine painted on the back wall never changes." / "Actors move with a slow sliding walk."
- Cast: Guard as the shite (mask); Creon as the waki (unmasked), seated by the front-right pillar; the Chorus line sung by the seated chorus (eight figures, the tool's drawing); four musicians at the back.
- Seats: Front, shomen (0, -5, eye 1.2); Corner, naka-shomen (-6, -5, eye 1.2); Side, waki-shomen (-8, 2.7, eye 1.2, facing across the stage).
- Layout: main stage x -2.7 to 2.7, y 0 to 5.4, height 0.9; four pillars 0.24 m square, height 4.5, at the corners, the eye-fixing pillar (metsuke-bashira) front left; back area y 5.4 to 7.4 with the musicians; chorus seats x 2.7 to 4.2, y 1 to 4.5, kneeling, facing the stage; bridgeway from (-2.7, 6) to the curtain at (-14, 8), width 2.2. Default: Creon kneeling at (2, 0.8) facing stage center; Guard at center (0, 2.7) facing Creon from beat 3.
- Beat 1: The whole bridge (the Guard slides the whole bridgeway at 0.4 m a second to (-2.2, 4.8)) / Stop on the bridge (he stops at (-8, 7) and speaks beats 1 and 2 from there). Notices: "The bridge is the road: the slow slide makes 'a furlong to a league' happen in front of you." / "Stopped on the bridge he is between two worlds, not yet before the king, small against the bare wall."
- Beat 4: The Guard speaks it / The chorus sings it (the chorus takes his words; he moves to (-1, 1.5), stops, faces front, then turns to Creon). Notices: "In his own voice the report stays personal: a frightened man explaining himself." / "When the chorus sings his words and he only moves, the report becomes the story itself, and you watch the mask, not a mouth."
- Beat 8: At the eye-fixing pillar (the Guard at (-2.1, 0.7) facing the front seats) / Leaving on the bridge (he speaks while sliding away to the curtain). Notices: "At the front pillar the mask faces the front seats, where masks read best, and his relief is shared with you." / "Spoken while he slides away, his relief trails off down the bridge; the scene ends in the distance."

*Commedia dell'arte.* Date line: "Italy, from 1545 (the earliest known company)". frame open (trestle platform and backcloth), light daylight.
- Rules: "Stock characters wear half masks; only the young lovers and Pedrolino go without." / "Actors improvise around a scenario and drop in lazzi, rehearsed comic bits." / "Masks hide faces, so gesture and voice carry the character." / "A trestle stage and a painted backcloth in the open air."
- Cast: Guard as a zanni, the servant clown; Creon as the Capitano, the boasting soldier; the Chorus line given to the Dottore, the know-it-all scholar. All in half masks.
- Seats (standing crowd): Front of the crowd (0, -2, eye 1.6); Side of the crowd (-6, 1, eye 1.6); Back of the crowd (0, -12, eye 1.6).
- Layout: platform x -3 to 3, y 0 to 4, height 1.5; backcloth at y 4 (height 4) with entrances at its left end, right end and a center slit. Default: Capitano (1, 2) facing the zanni; Dottore (2.3, 2.8); zanni ends beat 1 at (-1, 1.5).
- Beat 1: Lazzo of the long road (the zanni starts, stops, turns back and starts again three times between x -3 and -1; caption "lazzo") / Straight in. Notices: "The crowd laughs before a word of news: the dread becomes a joke you are in on, and the zanni owns the stage." / "Without the lazzo the scene starts on the plot, and the crowd waits to see who this masked servant is."
- Beat 4: Tell the crowd (he goes to the front edge (0, 0.4) and faces the crowd for "drew the prize") / Tell the Capitano. Notices: "Told to the crowd, his bad luck is a complaint shared with you, so you take his side." / "Told to the Capitano, it is a servant pleading with a master, and you watch the master."
- Beat 6: Boast and mock (Capitano at (0, 1) facing the crowd; the zanni behind him at (0, 2.6) copying every gesture) / Played straight (Capitano faces the zanni, who kneels at (-0.5, 1.5)). Notices: "Behind the boaster's back the copying zanni steals the focus, and the threat turns into a laugh at the man making it." / "Played straight, the threat lands: the crowd goes quiet, and the comedy has a moment of real danger."

*Elizabethan playhouse.* Date line: "London, the Globe, 1599". frame thrust, light daylight.
- Rules: "Plays run in the afternoon, by daylight." / "Groundlings stand in the yard around three sides of the stage." / "Almost no scenery: the words tell you where you are." / "Doors at the back for entrances, a balcony above."
- Cast: Guard, Creon, and an old counsellor speaks the Chorus line.
- Seats: Yard, at the stage (0, -1.5, eye 1.6); Yard, at the side (-9, 3, eye 1.6); Middle gallery (0, -12, eye 6).
- Layout: stage x -6.5 to 6.5, y 0 to 8, height 1.5; back wall at y 8 (height 8) with doors at (-4, 8) and (4, 8) and a center opening; balcony x -3 to 3, y 8 to 9, height 5; two stage pillars (0.5 m round, height 8) at (-4, 6) and (4, 6). Default: Creon (0, 5) facing front; counsellor (3, 5.5); Guard enters by the left door.
- Beat 1: To the groundlings (the Guard comes to the front edge (-2, 0.8) and faces the yard) / To Creon (he stops at (-2, 4) facing Creon). Notices: "In daylight he can see the people standing an arm's length away, and his slow journey is told to them as friends." / "Played to Creon, the journey is an excuse to a king, and the yard watches a private fear from close by."
- Beat 6: From the balcony (Creon leaves by the center opening at beat 5 and swears from the balcony) / At the edge of the yard (Creon at (1, 1) facing the Guard at (-2, 3)). Notices: "From the balcony the oath comes from above everyone, like a law." / "At the edge of the thrust the groundlings are almost inside his threat; the yard sees his face, the far side his back."
- Beat 8: To the yard (the Guard at (0, 0.8) facing the yard) / To the door (at (0, 5) facing the center opening Creon left by). Notices: "Alone at the edge, 'thou never shalt see me here' lands on the crowd as a shared joke." / "Said to the empty doorway, the line is aimed at the absent king, and the yard hears a man still afraid."

*Realist box set.* Date line: "Europe, late 1800s (the fourth wall idea: Diderot, 1758)". frame proscenium, light areas (only room sources: desk lamp, window, ceiling light; the lights panel works here and nowhere else).
- Rules: "The room has three walls; the fourth is where the audience sits, and the actors act as if it were solid." / "Real furniture and objects; light seems to come from lamps and windows." / "Nobody speaks to the audience."
- Cast: Guard as a night watchman with a cap; Creon as the head of state at his desk; an aide speaks the Chorus line.
- Seats: Stalls, center (0, -6, eye 1.1); Stalls, side (-6, -4, eye 1.1); Gallery (0, -14, eye 6).
- Layout: the stage-blocker proscenium (10 by 7 m); back wall at y 6.5 with a door at (1.5, 6.5); a window in the left side wall at (-4.8, 3.5); desk at (1.5, 3), desk chair (1.5, 3.8), two chairs at (-1, 2.5) and (-2, 4). Default: Creon seated at the desk; aide (3.3, 4.5) facing Creon; Guard enters by the door to (-0.5, 4.5).
- Beat 1: Creon keeps writing (seated, head down; the Guard waits at (0, 5) with his cap in his hands) / Creon stands (at (0.5, 3.5) facing the Guard). Notices: "Making him wait says everything about power without a word, and you watch like a fly on the wall." / "Standing to meet him, Creon is polite and dangerous at once, and the room feels like a real office."
- Beat 4: Offered a chair (the Guard sits on the chair at (-1, 2.5), facing Creon) / At attention (stands stiffly at (-0.5, 4)). Notices: "On the edge of a chair he is a tired working man, and the ordinary room makes his fear real." / "At attention every line is a report to a superior, and you read the gap between his words and his stiffness."
- Beat 8: Alone, to himself (at (0.5, 5), back to the house, quiet) / Cheated out (at (-1.5, 1.5) facing the window, in profile). Notices: "Back to us, his relief is private; we overhear it through the fourth wall." / "Turned toward the window we see his face without being spoken to, and the fourth wall still holds."

## Interactions in detail
- The beat order is fixed; choices change blocking and the notice, never the words. Speaker names per house replace "Chorus" (Chorus leader, the chorus, the Dottore, the counsellor, the aide).
- A choice applies its blocking from its beat to the next choice beat; later choices start from it, so a Greek Guard who took the side road is still out in the orchestra at beat 2 (that is the branching).
- Engine weights for this tool (the tool's own, labeled "rough guide"): masked actors score body position only at full front (+2) or one-quarter (+1.5), else 0 (a mask reads from the front); `chorusGaze`: each chorus figure facing an actor adds +0.5, up to +3 (Greek, Noh); `address`: a speaker facing the house within 45 degrees in an option marked "to the crowd" or "to the yard" adds +2 (commedia, Elizabethan). Lights matter only in the realist house.
- Adjust rule checks: Greek, the chorus stays inside the orchestra circle; Noh, entrances and exits use the bridgeway and the chorus stays seated; realist, a speaker facing the stalls center full front gets "This reads as talking to the audience."
- Play scene: 2 s per beat plus cross time (Noh slides at 0.4 m a second, the tool's choice); Motion off jumps between blockings, same pacing. Most houses run 20 to 30 s. Noh runs about 80 s when the Guard takes the whole bridge (12.2 m, 31 s) and leaves on it (14.0 m, 35 s): the slow slide is what the Noh notices teach, so it is kept, and every control stays live while it plays: Next beat finishes the current cross at once and shows the next beat, Prev beat goes back at once, Seat changes the view at once mid-cross, and tapping Play scene again stops it.
- Reset on a house (`Restart house`) clears its three choices; the tour status follows. Saved data: choices per house and the director's note only.

## Look
- Accent (`--brand`) #ff9e5e footlight orange, on the kit `theme-912` base. Scene colors per house (canvas only): Greek limestone #d8cdb8 under a pale sky; Noh cypress #d9b77a, pine #2f5d3a, roof #3b2f2a; commedia backcloth ochre #c9873a; Globe oak #8a5a34 and plaster #efe6d2; realist wallpaper #5d6b4f with warm lamp pools. Figures: Guard #ffd84d, Creon #5ec8ff, chorus and others #d9a3ff, each with initials; masks drawn as pale face shapes.
- Contrast (recomputed in Python): brand on panel 8.49:1; brand on section 8.05:1; brand-ink #1c1203 on brand 9.06:1; theme ink and muted as in theme-912.
- Different from 9-12 arts neighbors: gallery-critique #f39cbc, city-skyline-studio #6fd6e8, virtual-gallery #b8e07a, music-history-radio #4fd18b, storyboard-studio #ff6b6b, dance-styles-explorer #c9b3ff, and the theme default amber #f2a93b (more orange and lighter).

## Art
Local FLUX (`scripts/localart.py`; the five house cards were drawn this way and wait for review in `art/prompts.json`). No people; blank surfaces. Every stage view stays in code, on purpose: the engine's House view and plan must move actors, turn them and test sightlines from each seat, which a painting cannot do.

House cards (Tour and Arrival), house style in `prompts.json` (detailed painterly architectural illustration, natural light, an empty venue):
- greek-theatre: an ancient open-air stone theater on a hillside in Greece, semicircular stone seats around a round flat stone floor, a low stone stage building behind, olive-covered hills, late afternoon light; 16:9; cutout no; people no.
- noh-stage: a traditional Japanese Noh stage of pale cypress wood under its own roof, a large painted pine tree on the back wall, a roofed bridgeway leading off to the left, four square pillars, polished floor, soft even light; 16:9; cutout no; people no.
- commedia-piazza: a wooden trestle stage in an Italian town square, a painted cloth backdrop of a street of houses hung behind it, cobblestones, stone buildings and a church tower around, morning light; 16:9; cutout no; people no.
- globe-playhouse: inside a round timber Elizabethan playhouse, three tiers of wooden galleries, open to the sky, a raised wooden stage jutting into an open yard, two painted pillars holding a canopy over the stage; 16:9; cutout no; people no.
- box-set-study: a realistic theater set of an 1890s study seen through a proscenium arch, three wallpapered walls, a desk with a green lamp, a door at the back, a curtained window at the side, a dark auditorium in front; 16:9; cutout no; people no.

Masks (new): objects, no person wears them. One shared prompt line: "<mask>, a single theater mask lying on dark cloth, seen from the front, soft museum light, realistic painted detail, plain dark background"; 1:1; cutout yes; people no (a carved or leather object, not a face; Cory to confirm, open question); shown at about 72 px beside each masked role in the Arrival cast list and on the plan inset's legend. Masks:
- mask-greek: a pale linen and plaster Greek tragic mask with wide open mouth and eye holes and painted brows.
- mask-noh: a carved and painted wooden Noh mask of a middle-aged man, calm, with a smooth ivory surface and small eye holes.
- mask-zanni: a brown leather commedia half mask with a long hooked nose and small eye holes.
- mask-capitano: a brown leather commedia half mask with a very long straight nose and a fierce brow.
- mask-dottore: a black leather commedia half mask covering only the forehead and nose, with round red cheeks painted beside it.

The figures in the House view stay simple code shapes with initials, and their masks are drawn there as pale face shapes (they turn with the actor).

## Voice
Bank voice `science-narrator` (Charon), style "Say in a clear, informative way, like a nature documentary narrator": the narrator of a travel documentary about the world's theaters. Not used by any voiced neighbor (gallery-critique calm-professor, city-skyline-studio casual-peer, virtual-gallery wise-mentor, theory-gym and stage-blocker firm-captain, music-history-radio news-reader, storyboard-studio smooth-narrator, brand-builder hs-narrator, dance-styles-explorer upbeat-guide). The play text is on screen, never voiced. `Curio.voice` with `scope: () => state.mode + ':' + state.house`. How lines speak once per page load, then only update the hint. No line plays while Play scene runs; queued lines wait for it to end.
- welcomeTour (how; Tour entered; stale when a house card is tapped): "Welcome, guest director. Five theaters, one scene. Tap a theater to begin."
- arrive.<house> (how, one per house; Arrival opens; stale when Begin or Back to tour is tapped): "The Greek theater: the chorus lives in the round orchestra. Read the rules, then tap Begin." / "The Noh stage: a bridge, four pillars and a painted pine. Read the rules, then tap Begin." / "A commedia stage in the square: masks, tricks and a crowd. Read the rules, then tap Begin." / "The Globe, by daylight, with the crowd on three sides. Read the rules, then tap Begin." / "A realist room with its fourth wall. Read the rules, then tap Begin."
- sceneHow (how; the first Scene opens; stale when Next beat or Play scene is tapped): "Read the beat, then tap Next beat to move on, or Play scene to watch it run."
- choiceHow (how; the first choice card; stale when a choice is tapped): "Tap one of the two choices. Then watch from a seat and read what the audience notices."
- seatHow (how; the first notice card; stale when Seat is tapped or the beat changes): "Tap Seat to watch the same moment from somewhere else."
- programNote (event; the third choice in a house; stale when Back to tour or Change choice is tapped): "Program note written. Tap Back to tour for the next theater."
- compareReady (event; the second house staged; stale when Compare is opened): "Two theaters staged. Tap Compare to see them side by side."
- allStaged (event; all five staged; stale when Compare is opened): "You've directed all five. Tap Compare to see them side by side."
- welcomeCompare (how; Compare entered; stale when a beat is tapped): "Tap a beat number. Every theater you staged shows that moment side by side."
- Read speaks the hint; on a notice card it speaks the notice.

## Family engine
`kit/stage.js`, family stage; the full description is in stage-blocker's spec. This tool feeds it: five houses (`greek`, `noh`, `commedia`, `globe`, `box`) with outlines, levels (Greek stage, Noh stage and bridgeway, commedia platform, Globe stage and balcony), blockers (Greek stage wall, Noh pillars, commedia backcloth, Globe back wall and pillars, box set walls), three seats each, frames arc, open, thrust and proscenium, and lights daylight, even and areas; cast with `mask: 'full'` (Greek, Noh shite) or `'half'` (commedia); the eight beats; one snapshot per option built from the coordinates above; and the weight terms `chorusGaze`, `address` and the mask rule. It uses `sight`, `bodyPos`, `focus`, `view.plan` (inset and Adjust), `view.house` and `play`; not `check` (no notes here).

## Sources
- Scene text: Sophocles, Antigone, trans. F. Storr, Sophocles vol. 1 (Loeb Classical Library, Heinemann and Macmillan, 1912); public domain; Project Gutenberg ebook 31, https://www.gutenberg.org/ebooks/31
- Three actors and the chorus as part of the action: Aristotle, Poetics, trans. S. H. Butcher (1895), parts IV and XVIII, Project Gutenberg ebook 1974.
- Greek stage, side and door entrances, masks, the first evidence of a round orchestra at Epidauros about 330 BC: Colette Hemingway, "Theater in Ancient Greece", The Met Heilbrunn Timeline of Art History (2004), https://www.metmuseum.org/essays/theater-in-ancient-greece
- Noh stage, pillars, bridgeway, chorus seats, painted pine, masks and seats: the-noh.com, "Noh stage", https://www.the-noh.com/en/world/stage.html ; sliding walk: https://www.the-noh.com/en/trivia/113.html ; the waki is never masked, and the chorus often chants the shite's lines while the shite dances: Stanford University, "Noh as Intermedia", https://noh.stanford.edu/actors ; Noh from the 1300s: UNESCO, Nogaku theatre, https://ich.unesco.org/en/RL/nogaku-theatre-00012
- Commedia scenario, lazzi, stock characters and who wore masks, earliest company 1545: The Met, "Commedia dell'arte", Heilbrunn Timeline, https://www.metmuseum.org/essays/commedia-dellarte ; character types: Pierre Louis Duchartre, The Italian Comedy (1929).
- Globe 1599, afternoon performances, groundlings in the yard, thrust stage, tiring house, heavens: Shakespeare's Globe, "Shakespeare's London Theatres" teacher resource, https://cdn.shakespearesglobe.com/uploads/2022/08/Shakespeares-London-Theatres.pdf
- Fourth wall (Diderot, 1758) and its use in nineteenth-century naturalist staging: Encyclopaedia Britannica, "fourth wall", https://www.britannica.com/art/fourth-wall
- National Core Arts Standards, Theatre, high school (TH:Re8, TH:Cn11): https://www.nationalartsstandards.org
- Stage sizes, coordinates, figure counts, weights and notices: this tool's own drawing and interpretation, labeled as such.

- Checks run in Python (2026-10-29): the Look contrast pairs (rounded values corrected to 8.49, 8.05 and 9.06). Blocking positions checked against each house outline: every Greek spot lies inside the orchestra circle (the closed-up elders reach 8 m from its center, inside its 10 m radius) or on the stage strip; the Noh stop on the bridge (-8, 7) lies on the bridgeway's center line (6.94 at x -8), and the eye-pillar spot is 0.6 m clear of the pillar; every commedia, Globe and box set spot lies inside its stage. Noh slide times at 0.4 m a second: the whole bridge 12.2 m = 30.6 s, leaving on the bridge 14.0 m = 34.9 s, so a full Noh Play scene runs about 80 s, explained in Interactions.

## Done when
1. Every house plays all eight beats in order with this house's speaker names, and each of its three choice beats offers its two options.
2. Each option's blocking matches the coordinates above (check the snapshot numbers in Python) and carries forward to the next choice.
3. The notice card shows the right two sentences, and the focus leader line changes with the seat when the engine says it should (for example, a Noh pillar hides the Guard from the side seat at some spot).
4. Masked figures score body position only at full front or one-quarter; the address bonus applies only in commedia and Elizabethan "to the crowd" options; lights work only in the realist house.
5. Program note lists the three choices; Compare unlocks after two houses and shows one beat across every staged house.
6. Adjust flags each house rule in words and never blocks a move.
7. Focus: in Scene at 1366x768 the House view is the biggest thing on screen with the choice card beside it; in Tour the five painted cards fill the stage; each masked role in the cast list shows its mask.
8. A tap during Play scene acts at once: Next beat in the middle of the Noh bridge slide puts the Guard at the end of the slide and shows the next beat, Seat changes the view mid-cross, and Play scene again stops it.
9. Save on this device keeps choices and the note across a reload; Clear empties `curio-directors-chair`.
10. The House view, Next beat and the choice card are visible without scrolling at 680x425, 1366x768 and 760 wide; scene text 10 px or more in the preview.
11. How-to lines spoken once in five actions; no line plays during Play scene; no em dashes in any on-screen text, including the play text.

## Open questions
- Five painted masks (Greek, Noh, three commedia) were added to the cast list as objects on local FLUX. They are face-shaped: fine on the local model, or send them to Gemini for review like people?
