# Moon Base Drama

## One idea
The teacher is Commander Ada and the class is her moon base crew: the board is only the base itself (the scenes, the crackling radio from Mission Control and Ada's script card), the class answers her in role with props they mime, true moon facts decide what works, and the story map lets the crew rewind to any choice, say a different line, and watch the story change.

## Not like
- act-it-out (k-2, showdown): two halves of the class act a folktale's characters as the board tells it. Here the teacher is in role too, the class speaks as a crew, and their answers steer the plot.
- gallery-critique (9-12, roleplay): a panel debate about a painting. Here the role play is a drama for young children, with facts from science deciding the plot.
- puppet-show-feelings (k-2, story, this batch): the class watches and directs a puppet. Here the class is inside the story.
- feeling-scarf-dance, family-dance-night (k-2, this batch): movement tools. Here bodies only mime props; the drama is spoken.

## Who and how
- Grade K-2, theater, module "Drama in Role".
- Driver: teacher on a projector or smartboard, in role as Commander Ada (the board shows her lines on a card; a scarf or clipboard helps). The class answers in role; the teacher taps the crew's choice. 20 to 30 minutes.
- Standards: NCAS TH:Cr3 (revise: rewind and change a choice), TH:Re9 (respond: talk about how a choice changed the story), TH:Cn11 (use knowledge from another subject, moon science, in a drama). Moon facts touch NGSS 1-ESS1-1 (patterns of the Sun and Moon) as context only.

## Screens and modes
Header: title, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`, icon plus word): `Crew` (badge icon, default), `Mission` (rocket icon). Every control is 60 px or more with an icon and a word.

**Crew.** Focus: six big job badges in a 3 by 2 grid on the base interior scene, each a painted prop on a round badge with its job word: `Plant Keeper` (watering can), `Engineer` (wrench), `Rover Driver` (rover key), `Medic` (first aid kit), `Scientist` (magnifier and rock bag), `Radio Operator` (headset). Tap a badge: the prop grows, the radio says the job line, and the badge gets a check (the class or a table group takes that job and mimes the prop). `Ada's card` (clipboard, toggle) shows the commander's line for this screen. `Start mission` (gold) when at least one job has a check.

**Mission.** Focus: the scene (painted, full stage) with the radio panel at the bottom left (a speaker grille drawn in code that glows while Mission Control talks) and Ada's card at the top right (big type, for the teacher to read in role; the narrator never reads Ada's lines). Bar: `Back`, `Next` (gold), `Radio again` (replays the Mission Control line), `Ada's card` (show or hide). On a choice beat, two big choice buttons sit on the scene, each with an icon and the crew's line in words ("Fill the batteries now!").
- The story map runs across the top: one node per beat, choice nodes as diamonds with the chosen icon. `Rewind` (curved arrow) opens it big: tap any past choice node to go back to it; later nodes fade (they are the old story) until a new path is chosen.
- The greenhouse meter, top left: three icons that fill or empty as choices land, `Light`, `Water`, `Warm` (bulb, drop, sun), each with 0 to 3 dots.

## Content
**Job lines** (radio, when a badge is tapped):
- Plant Keeper: "Plant Keeper, you water the greenhouse plants. Show me your watering can."
- Engineer: "Engineer, you fix the machines. Show me your wrench."
- Rover Driver: "Rover Driver, you drive the moon buggy. Turn the key and steer!"
- Medic: "Medic, you keep the crew healthy. Open your first aid kit."
- Scientist: "Scientist, you study moon rocks and ice. Hold up your magnifier."
- Radio Operator: "Radio Operator, you talk to Earth. Put on your headset."
**Ada's card on Crew:** "Welcome to Moon Base Luna, crew! Tell me your job. Show me what you brought."

**Mission beats** (scene; Mission Control line, spoken; Ada's card, not spoken; meter change):
1. base: "Moon Base Luna, this is Mission Control. On the Moon, a day lasts about two weeks, and the night lasts about two weeks too. The long night begins soon." Ada: "Crew! When the Sun goes down, our greenhouse gets no sunlight for two whole weeks. What do our plants need?" (Class: light, water, warmth, air.)
2. greenhouse: "Your plants need light, water, warmth and air. Right now, every meter is low." Ada: "We have three jobs before dark. Ready, crew?" Meter: Light 1, Water 1, Warm 1.
3. choice, surface-solar: "Our solar panels make power only while the Sun shines." Ada: "How do we keep the plant lamps on all night?"
   - A `Fill the batteries now!` (sun and battery): "Good thinking. The Sun is shining now, so the panels can fill the batteries." Light +2.
   - B `Wait until dark` (moon): "Mission Control here. Remember: no Sun at night means no solar power. Your batteries are low." Light +0; Ada: "Hmm. Should we rewind and try again?"
4. choice, rover then ice-crater: "Your water tank is low. Scientists found ice hiding in dark craters near the Moon's south pole." Ada: "Where can we get water?"
   - A `Ice in the dark crater` (ice cube): "Great. Rover Driver, steer to the crater. Scientist, find the ice!" Water +2.
   - B `A river` (wave): "Mission Control here. Our maps show no rivers on the Moon. But look: something shines in that dark crater." Water +1 (they find it late).
5. ice-crater: "The ice block is heavy. But on the Moon, things weigh only about one sixth as much as on Earth." Ada: "Who can carry it? Show me how you lift it on the Moon!" (Everyone mimes a slow, floaty lift; no choice.)
6. choice, airlock: "Moon nights are colder than any freezer on Earth, and there is no air outside the base." Ada: "How do we keep the plants warm?"
   - A `Wrap it in a blanket` (blanket): "Yes! A thick blanket keeps the warmth in." Warm +2.
   - B `Open the doors for air` (door): "Careful! There is no air outside. Opening the doors would let our air out. Engineer, shut them fast!" Warm +0.
7. airlock: "Moon dust is sharp and sticky. Brush off your suits before you go inside." Ada: "Medic, check the crew. Everyone, brush off the dust!" (Mime; no choice.)
8. greenhouse (night): the ending depends on the meter (each of Light, Water, Warm at 3 is "full"):
   - All three full: "Mission Control to Moon Base Luna. The long night is here, and your greenhouse is glowing. Great work, crew!"
   - Two full: "The long night is here. The greenhouse is OK, but one part is low. Can you rewind and fix it?"
   - One or none full: "The long night is here, and the plants are droopy. Rewind and make a different choice!"
   Ada (all endings): "Crew, which choice made the biggest difference? Tell me why."

**Rewind lines:** going back to a choice: "Rewinding to <beat name>. What will you say this time?" (one line per choice beat: "the batteries", "the water", "the warmth").

## Interactions in detail
- Next and Back are never locked except Next on a choice beat until a choice is tapped (no line names Next then). Any tap stops the radio at once and acts.
- A choice tapped: the button stays outlined, the radio says its result line, the meter fills its dots (400 ms; Motion off: at once), and the map node gets the choice icon.
- Rewind: going back to a choice beat restores the meter to what it was before that choice and fades every later node; picking again redraws the path from there. Back (one beat) also undoes a choice's meter change when it leaves the beat after it.
- The radio glows only while Mission Control speaks, and a soft radio crackle (filtered noise, 200 ms, made in code) plays before each line. Sound off: the line is shown in a radio caption under the grille.
- `Ada's card` is on by default; hiding it is for teachers who improvise.
- Greenhouse night scene: the painted greenhouse is darkened in code, and its lamps glow by the Light dots (0 to 3); plants droop (a code scale on the leaf layer) when Water or Warm is under 3.
- Nothing is stored. Leaving Mission keeps the story; `New mission` (on the end beat and in the map) starts again at beat 1 with the jobs kept.
- Keyboard: Right and Left are Next and Back, R is Rewind, A toggles Ada's card.

## Look
- Accent (`--brand`) #3a4a5c moon slate (header, Next, the map path). Paper #f2f3f5, ink #1a1f26, muted #555d68. Scenes: lunar greys and black sky with the blue Earth; warm amber #f2b632 for lamp glow and the radio light; meter icons with dots (count, not color).
- Contrast (WCAG 2.1, computed): white on brand 9.08:1; brand on paper 8.17:1; ink on paper 14.92:1; muted on paper 6.00:1; Ada's card is ink on #fff8e6 (above 14:1).
- Different from the k-2 arts neighbors: line-safari #c0612b, art-passport #1f5f8b, beat-buddies #c2482f, orchestra-zoo #2f7a4a, sound-elevator #3d4fa8, act-it-out #7d2e7f, levels-and-pathways #00798c.

## Art
Local FLUX (`scripts/localart.py`). No people: suits hang empty, the crew is the class. One clean painted children's science-book style.
- base: "Inside a cozy round moon base control room, a big round window showing the grey lunar surface and the blue Earth in a black sky, consoles with blank screens, soft painted children's science book illustration"; 16:10; cutout no; people no; Crew and beat 1.
- greenhouse: "Inside a moon base greenhouse dome, rows of leafy green plants and tomatoes in trays under round grow lamps, the grey lunar surface outside the glass, painted children's science book illustration"; 16:10; cutout no; people no; beats 2 and 8 (darkened in code for night).
- surface-solar: "The grey lunar surface with rows of solar panels in bright sunlight, long black shadows, a small moon base dome in the distance, black sky with the blue Earth, painted children's science book illustration"; 16:10; cutout no; people no; beat 3.
- ice-crater: "The rim of a deep dark lunar crater, the inside in black shadow with patches of white ice glinting, low sunlight on the rim, black sky, painted children's science book illustration"; 16:10; cutout no; people no; beats 4 and 5.
- airlock: "A moon base airlock room with two white space suits hanging empty on wall hooks, a dust brush on a hook, a round hatch door, painted children's science book illustration"; 16:10; cutout no; people no; beats 6 and 7.
- rover: "A small six-wheeled moon buggy with a flat bed and an antenna, side view, painted children's science book illustration, plain white background"; 16:9; cutout yes; people no; drives across ice-crater on beat 4.
- ice-block: "A big rough block of clear blue ice, painted children's science book illustration, plain white background"; 1:1; cutout yes; people no; beat 5.
- 6 props, each "<prop>, painted children's science book illustration, plain white background", 1:1, cutout yes, people no: a green watering can; a silver wrench; a chunky rover key on a ring with a moon tag; a white first aid kit with a red cross; a magnifying glass and a small cloth rock bag; a pair of radio headphones with a microphone. Crew badges.
13 images, none with people. Drawn in code: the radio panel and glow, the meter, the story map, Ada's card, the night darkening and lamp glow, the leaf droop.

## Voice
Bank voice `firm-captain` (Alnilam), style "Say firmly but kindly, like a ship captain giving clear directions". It is Mission Control on the radio; Commander Ada is the teacher. Not used by any K-2 arts neighbor (line-safari bright-teacher, art-passport knowing-guide, beat-buddies lively-host, orchestra-zoo playful-friend, sound-elevator hero-coach, act-it-out gentle-storyteller, levels-and-pathways warm-teacher) or by another K-2 spec in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.beat`.

- how, welcome (Crew; stale when a badge is tapped): "Mission Control to Moon Base Luna. Teacher, you are Commander Ada. Tap a job badge for each crew member."
- event: each job line in Content (every tap).
- how, first job checked (stale when Start mission is tapped): "When the crew is ready, tap Start mission."
- event: each beat's Mission Control line and each choice result line in Content (spoken when the beat opens or the choice is tapped; stale when the beat changes).
- how, first choice beat (stale when a choice is tapped): "Commander, read your card. When the crew answers, tap their choice."
- how, first non-choice beat after beat 1 (stale when the beat changes): "When the crew is done, tap Next."
- event, each ending line in Content.
- event, each rewind line in Content.
- how, first rewind (stale when a choice is tapped): "The old story fades. Tap a choice to make a new one."
- Read speaks the Mission Control line of the beat (never Ada's card), else the hint.

## Family engine
none

## Sources
- National Core Arts Standards, Theatre, grades K to 2 (TH:Cr3, TH:Re9, TH:Cn11): https://www.nationalartsstandards.org. Teacher in role: Heathcote and Bolton (1995), Drama for Learning, Heinemann.
- A lunar day (sunrise to sunrise) is about 29.5 Earth days, so about two weeks of daylight and two weeks of night: NASA Science, "Moon Facts" (https://science.nasa.gov/moon/facts/).
- Moon temperatures fall to about -130 C (-208 F) at night near the equator, colder in polar craters; the coldest home freezer is about -18 C: NASA Science, "Moon Facts"; Earth's coldest recorded air temperature is -89.2 C (Vostok, 1983, WMO): so "colder than any freezer on Earth" holds.
- No air (no breathable atmosphere) on the Moon: NASA Science, "Moon Facts" (an exosphere only).
- Water ice in permanently shadowed craters near the south pole: NASA LCROSS results, Colaprete et al. (2010), Science 330, 463 to 468; NASA "Ice Confirmed at the Moon's Poles" (2018).
- Moon gravity about 1/6 of Earth's (1.62 versus 9.81 meters per second squared): NASA Moon Fact Sheet (https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html).
- Lunar dust is sharp and clings to suits: NASA, "The Dust Problem", Apollo 17 crew reports (Gaier, NASA/TM-2005-213610).
- Solar panels make power only in sunlight; batteries store it: US Department of Energy, "How Does Solar Work?" (https://www.energy.gov/eere/solar/how-does-solar-work).
- Checks run (Python, 2026-10-29): 29.5 / 2 = 14.75 days of night ("about two weeks"); 1.62 / 9.81 = 0.165, and 1/6 = 0.167 ("about one sixth"). Meter walks for all 8 paths (2 x 2 x 2 choices): starting 1, 1, 1; A adds 2 and B adds 0, 1, 0 for Light, Water, Warm; all A gives 3, 3, 3 (all full); the best with any B is two full (B at water gives Water 2, so two full); all B gives 1, 2, 1 (none full). Every path reaches one of the three endings, and every ending is reachable. Contrast ratios as listed.

## Done when
1. Focus: at 1366x768 and 680x425 the scene fills the stage with Ada's card readable (scene text 10 px or more) and the choice buttons large on the scene.
2. All 8 choice paths play to the ending the meter predicts; the meter shows 1, 1, 1 at beat 2 and the right dots after each choice.
3. Rewind to any choice restores the meter and fades later nodes; a new choice redraws the path.
4. Ada's lines are never spoken; every Mission Control line is spoken when its beat opens, and Radio again replays it.
5. Tap while it plays: Next, Back, Rewind or a choice tapped mid-line cuts the radio at once and acts; no stale line follows.
6. Next is disabled only on choice beats until a choice is tapped, and no line names it then.
7. How-to lines are spoken once in a run of five Next taps; beat and result lines every time.
8. Every control is 60 px or more with an icon and a word; the bar is visible without scrolling at every size in STANDARDS.md.
9. Motion off: no rover drive or meter fill animation; the night darkening appears at once.
10. No network requests; nothing is saved.
